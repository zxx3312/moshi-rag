"""Fictional integration checks for data isolation, failure accounting and frozen inputs."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import types
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import main_experiments as prep
import run_main_experiments as run
from turntaking.llm import CallRecord, FakeClient


def corpus():
    traces = []
    for schedule, times in prep.SCHEDULES.items():
        events = [{"evidence_id": "e1", "scheduled_time_s": times[0], "visible_time_s": times[0],
                   "text": "Mira designed the fictional Alder device.",
                   "source": {"dataset": "fictional", "document_id": "Alder", "document_index": 0, "sentence_index": 0}}]
        traces.append({"schema_version": "1.0", "data_version": "fictional", "sample_id": "f1",
                       "trace_id": "f1_" + schedule, "trace_type": "controlled_mock", "clock": "simulated",
                       "time_origin": "question_end", "question": "Who designed Alder?", "events": events,
                       "retrieval_complete_time_s": times[0]})
    gold = [{"sample_id": "f1", "question_type": "single", "source_type": "fictional",
             "units": [{"unit_id": "u1", "description": "designer", "necessary": True,
                        "expected_answer": "Mira", "depends_on": [], "support_sets": [["e1"]]}]}]
    return traces, gold


def validator():
    return types.SimpleNamespace(prepare_inputs=lambda t, g: ({r["trace_id"]: r for r in t}, {r["sample_id"]: r for r in g}))


class PreparationTest(unittest.TestCase):
    def test_slurm_probe_executes_and_records_test_only_command(self):
        with tempfile.TemporaryDirectory() as tmp:
            args = argparse.Namespace(bundle=Path(tmp), concurrency=2, test_only=True)
            done = types.SimpleNamespace(returncode=0, stdout="", stderr="estimated start")
            with mock.patch.object(prep, "verify_bundle", return_value={"shards": [[0]]}), mock.patch.object(
                    prep.subprocess, "run", return_value=done) as probe, mock.patch("builtins.print"):
                self.assertEqual(prep.command(args), 0)
            executed = probe.call_args.args[0]
            self.assertEqual(executed[:2], ["sbatch", "--test-only"])
            self.assertNotIn("--parsable", executed)
            saved = json.loads((args.bundle / "slurm_test.json").read_text())
            self.assertEqual(saved["command"], executed)
            self.assertEqual(saved["mode"], "test_only_no_submission")

    def test_three_schedules_share_one_question_and_content(self):
        traces, gold = corpus()
        result = prep.inspect_data(traces, gold, prep.SCHEDULES, validator())
        self.assertEqual((result["questions"], result["traces"], result["gold_units"]), (1, 3, 1))

    def test_gold_fields_in_public_trace_are_rejected(self):
        traces, gold = corpus()
        traces[0]["units"] = gold[0]["units"]
        with self.assertRaisesRegex(ValueError, "gold leakage"):
            prep.inspect_data(traces, gold, prep.SCHEDULES, validator())

    def test_gold_fields_in_source_are_rejected(self):
        traces, gold = corpus()
        traces[0]["events"][0]["source"]["expected_answer"] = "Mira"
        with self.assertRaisesRegex(ValueError, "gold leakage"):
            prep.inspect_data(traces, gold, prep.SCHEDULES, validator())

    def test_missing_schedule_is_rejected(self):
        traces, gold = corpus()
        with self.assertRaisesRegex(ValueError, "all three schedules"):
            prep.inspect_data(traces[:2], gold, prep.SCHEDULES, validator())

    def test_changed_evidence_between_schedules_is_rejected(self):
        traces, gold = corpus()
        traces[1]["events"][0]["text"] = "A different statement."
        with self.assertRaisesRegex(ValueError, "content differs"):
            prep.inspect_data(traces, gold, prep.SCHEDULES, validator())

    def test_future_scheduled_time_is_rejected(self):
        traces, gold = corpus()
        traces[0]["events"][0]["scheduled_time_s"] = 8.0
        with self.assertRaisesRegex(ValueError, "Scheduled/visible"):
            prep.inspect_data(traces, gold, prep.SCHEDULES, validator())

    def test_blank_source_sentences_are_preserved_and_counted(self):
        traces, gold = corpus()
        for trace in traces:
            trace["events"][0]["text"] = ""
        result = prep.inspect_data(traces, gold, prep.SCHEDULES, validator())
        self.assertEqual(result["blank_evidence_events"], 3)
        self.assertTrue(all(t["events"][0]["text"] == "" for t in traces))

    def test_snapshot_edit_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            artifact = folder / "source.py"
            artifact.write_bytes(b"original")
            run.save_json(folder / "manifest.json", {"files": [{"path": str(artifact),
                "sha256": hashlib.sha256(b"original").hexdigest()}]})
            run.verify_bundle(folder)
            artifact.write_bytes(b"changed")
            with self.assertRaisesRegex(ValueError, "changed"):
                run.verify_bundle(folder)


class ExecutionTest(unittest.TestCase):
    class Client(FakeClient):
        def __init__(self, *args, **kwargs):
            super().__init__([])
            self.tape = []

        def chat_json(self, messages, *, purpose, schema=None, max_tokens=None):
            self.calls.append(CallRecord(purpose, 0.1, None, None))
            self.messages.append(messages)
            return {"decompose": {"question_type": "single", "units": [
                        {"unit_id": "u1", "description": "designer", "necessary": True, "depends_on": []}]},
                    "judge": {"units": []}, "generate": {"text": "Mira.", "answers": ["Mira"]}}[purpose]

    def test_ordinary_worker_rejects_gold_before_reading_files(self):
        args = argparse.Namespace(phase="main", gold=Path("must-not-read"))
        with mock.patch.object(run, "load_jsonl", side_effect=AssertionError("file opened")):
            with self.assertRaisesRegex(ValueError, "must not receive"):
                run.worker(args)

    def test_ordinary_worker_runs_all_schedules_without_gold_units(self):
        traces, _ = corpus()
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            source = folder / "traces.jsonl"
            run.write_jsonl(source, traces)
            args = argparse.Namespace(phase="main", trace=source, gold=None, out=folder / "output",
                                      base_url="unused", lora_base_url="unused")
            with mock.patch.object(run, "ChatClient", self.Client), mock.patch.object(
                    run, "units_without_gold", side_effect=AssertionError("gold units used")):
                run.worker(args)
            rows = run.load_jsonl(args.out / "execution.jsonl")
            self.assertEqual(len(rows), 24)
            self.assertEqual({r["policy"] for r in rows}, set(run.MAIN_POLICIES))
            self.assertTrue(all(r["state"] == "completed" for r in rows))
            logs = run.load_jsonl(args.out / "policy_log.jsonl")
            times = {t["trace_id"]: {e["evidence_id"]: e["visible_time_s"] for e in t["events"]} for t in traces}
            self.assertTrue(all(times[r["trace_id"]][eid] <= r["decision_time_s"]
                                for r in logs for eid in r["evidence_snapshot_ids"]))

    def test_watchdog_failure_is_kept_and_oracle_gets_separate_gold(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            manifest = {"shards": [[0]], "questions": ["public-question.jsonl"], "gold": "private-gold.jsonl"}
            run.save_json(folder / "bundle/manifest.json", {})
            args = argparse.Namespace(bundle=folder / "bundle", shard=0, out=folder / "output", resume=False,
                                      base_url="unused", lora_base_url="unused", worker_timeout_s=1)
            commands = []

            def timeout(cmd, **kwargs):
                commands.append(cmd)
                raise subprocess.TimeoutExpired(cmd, 1)

            with mock.patch.object(run, "verify_bundle", return_value=manifest), mock.patch.object(
                    run.subprocess, "run", side_effect=timeout):
                self.assertEqual(run.run_shard(args), 1)
            self.assertNotIn("--gold", commands[0])
            self.assertIn("--gold", commands[1])
            self.assertEqual(json.loads((args.out / "shard_status.json").read_text())["failed"], 2)
            args.resume = True
            with mock.patch.object(run, "verify_bundle", return_value=manifest), mock.patch.object(run.subprocess, "run") as again:
                self.assertEqual(run.run_shard(args), 1)
                again.assert_not_called()

    def test_paired_latency_excludes_unknown_and_failed_runs_but_reports_coverage(self):
        scores = []
        for index, state in [(1, "ok"), (2, "missing")]:
            for policy in ("wait_all", "evidence_aware+lora_real"):
                scores.append({"trace_id": f"f{index}_long", "policy": policy,
                               "status": state, "ttfgi_s": 8 if policy == "wait_all" else 5, "ttca_s": None})
        rows = prep.paired_times(scores)
        row = next(r for r in rows if r["policy"] == "evidence_aware+lora_real" and r["schedule"] == "long" and r["metric"] == "ttfgi_s")
        self.assertEqual((row["expected_traces"], row["pairs"], row["median_earlier_s"]), (2, 1, 3))


if __name__ == "__main__":
    unittest.main()
