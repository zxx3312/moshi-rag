"""Check premise timing, paired inputs, and public traces using fictional data."""

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from b_work.step3.build_traces import (
    EVENT_KEYS, SOURCE_KEYS, TRACE_KEYS, alternative_documents, build_trace,
    document_batches, supported_times, validate, validate_pair,
)


SCRIPT = Path(__file__).resolve().parents[1] / "build_traces.py"


class TraceFixture(unittest.TestCase):
    def setUp(self):
        """Use invented people and isolated output files."""
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.folder = Path(temporary.name)
        self.sample = {
            "schema_version": "1.0", "data_version": "test-revised-v1",
            "sample_id": "fictional_1", "dataset": "custom", "type": "comparison",
            "question_number": 151, "question": "Which of Alice and Bob is a director?",
            "answer": "Alice", "gold_answer": "Alice",
            "context": [["Alice", ["Alice is a director.", "Alice works in film."]],
                        ["Bob", ["Bob is an engineer."]],
                        ["River", ["The river flows through the town."]],
                        ["Alice interview", ["Alice directs films."]],
                        ["Town", ["The town has a market."]]],
            "supporting_facts": [["Alice", 0], ["Bob", 0]],
        }
        self.gold = {
            "schema_version": "1.0", "data_version": "test-revised-v1",
            "sample_id": "fictional_1", "source_type": "comparison", "question_type": "comparison",
            "units": [
                {"unit_id": "u1", "description": "whether Alice is a director", "necessary": False,
                 "expected_answer": "yes", "depends_on": [], "support_sets": [["d1s0"]]},
                {"unit_id": "u2", "description": "whether Bob is a director", "necessary": False,
                 "expected_answer": "no", "depends_on": [], "support_sets": []},
                {"unit_id": "u3", "description": "director among the named candidates", "necessary": True,
                 "expected_answer": "Alice", "depends_on": ["u1", "u2"], "support_sets": [[]],
                 "presupposition_sets": [["d1s0"]], "by_presupposition": True},
            ],
        }
        self.samples_path = self.folder / "samples.jsonl"
        self.gold_path = self.folder / "gold.jsonl"
        self.out = self.folder / "traces.jsonl"
        self.review = self.folder / "review.md"
        self.report = self.folder / "report.json"
        self.write_inputs()
        for path in (self.out, self.review, self.report):
            path.write_text("Keep previous output.\n")

    def write_inputs(self):
        """Save only this test's paired fictional records."""
        self.samples_path.write_text(json.dumps(self.sample) + "\n")
        self.gold_path.write_text(json.dumps(self.gold) + "\n")

    def run_cli(self, extra=(), out=None):
        """Run the real CLI with protected temporary outputs."""
        return subprocess.run(
            [sys.executable, "-B", str(SCRIPT), "--samples", str(self.samples_path),
             "--gold", str(self.gold_path), "--out", str(out or self.out),
             "--review", str(self.review), "--report", str(self.report), *extra],
            capture_output=True, text=True)


class SupportTimingTests(TraceFixture):
    def test_premise_can_answer_with_one_unknown_candidate(self):
        validate_pair(self.sample, self.gold)
        trace = build_trace(self.sample, "short", [1.0, 3.0], self.gold)
        self.assertEqual(supported_times(self.gold, trace), {"u1": 1.0, "u2": None, "u3": 1.0})

    def test_premise_can_beat_a_complete_normal_path(self):
        self.gold["units"][1]["support_sets"] = [["d2s0"]]
        trace = build_trace(self.sample, "short", [1.0, 3.0], self.gold)
        found = supported_times(self.gold, trace)
        self.assertEqual(found["u2"], 3.0)
        self.assertEqual(found["u3"], 1.0)

    def test_premise_waits_for_its_evidence_and_a_parent(self):
        self.gold["units"][2]["presupposition_sets"] = [["d4s0", "d5s0"]]
        trace = {"events": [{"evidence_id": eid, "visible_time_s": time}
                            for eid, time in [("d1s0", 5.0), ("d4s0", 1.0), ("d5s0", 3.0)]]}
        self.assertEqual(supported_times(self.gold, trace)["u3"], 5.0)
        trace["events"] = trace["events"][:-1]
        self.assertIsNone(supported_times(self.gold, trace)["u3"])

    def test_premise_cannot_skip_every_parent(self):
        self.gold["units"][0]["support_sets"] = []
        trace = {"events": [{"evidence_id": "d1s0", "visible_time_s": 1.0}]}
        self.assertIsNone(supported_times(self.gold, trace)["u3"])

    def test_premise_only_single_needs_no_parent(self):
        final = deepcopy(self.gold["units"][2])
        final.update(unit_id="u1", support_sets=[], depends_on=[])
        self.gold.update(question_type="single", units=[final])
        validate_pair(self.sample, self.gold)
        trace = build_trace(self.sample, "short", [1.0, 3.0], self.gold)
        self.assertEqual(supported_times(self.gold, trace), {"u1": 1.0})

    def test_premise_alternative_arrives_with_its_unit_anchor(self):
        self.gold["units"][0].update(presupposition_sets=[["d4s0"]], by_presupposition=True)
        self.assertEqual(alternative_documents([1, 2], self.gold)[4], 1)
        batches = document_batches(self.sample, 2, self.gold)
        self.assertIn(1, batches[0])
        self.assertIn(4, batches[0])
        self.assertEqual(sorted(batches[0] + batches[1]), [1, 2, 3, 4, 5])

    def test_missing_source_facts_use_gold_document_order(self):
        self.sample["supporting_facts"] = []
        trace = build_trace(self.sample, "short", [1.0, 3.0], self.gold)
        validate(trace, self.sample)
        self.assertEqual(supported_times(self.gold, trace)["u3"], 1.0)


class TraceContentTests(TraceFixture):
    def test_trace_keeps_source_text_and_has_no_gold_fields(self):
        trace = build_trace(self.sample, "short", [1.0, 3.0], self.gold)
        validate(trace, self.sample)
        self.assertEqual(list(trace), TRACE_KEYS)
        self.assertEqual(trace["data_version"], "test-revised-v1")
        self.assertEqual(len(trace["events"]), 6)
        self.assertIn("The river flows through the town.", [e["text"] for e in trace["events"]])
        for event in trace["events"]:
            self.assertEqual(set(event), EVENT_KEYS)
            self.assertEqual(set(event["source"]), SOURCE_KEYS)
        self.assertNotIn("gold_answer", trace)
        self.assertNotIn("units", trace)

    def test_validator_rejects_gold_metadata_and_changed_text(self):
        original = build_trace(self.sample, "short", [1.0, 3.0], self.gold)
        for place in ("trace", "event", "source", "text"):
            with self.subTest(place=place):
                trace = deepcopy(original)
                if place == "trace":
                    trace["expected_answer"] = "Alice"
                elif place == "event":
                    trace["events"][0]["support_sets"] = [["d1s0"]]
                elif place == "source":
                    trace["events"][0]["source"]["necessary"] = True
                else:
                    trace["events"][0]["text"] += " This is the gold answer."
                with self.assertRaises(ValueError):
                    validate(trace, self.sample)

    def test_validator_rejects_wrong_ids_even_when_the_count_matches(self):
        trace = build_trace(self.sample, "short", [1.0, 3.0], self.gold)
        trace["events"][0]["evidence_id"] = "d99s0"
        with self.assertRaisesRegex(ValueError, "not every context sentence"):
            validate(trace, self.sample)

    def test_whole_document_cannot_arrive_at_two_times(self):
        trace = build_trace(self.sample, "short", [1.0, 3.0], self.gold)
        event = next(e for e in trace["events"] if e["evidence_id"] == "d1s1")
        event.update(scheduled_time_s=3.0, visible_time_s=3.0)
        trace["events"].sort(key=lambda e: e["visible_time_s"])
        with self.assertRaisesRegex(ValueError, "document was split"):
            validate(trace, self.sample)


class TraceCliTests(TraceFixture):
    def test_cli_combines_paired_inputs_with_custom_schedules(self):
        other_sample, other_gold = deepcopy(self.sample), deepcopy(self.gold)
        other_sample.update(sample_id="fictional_2", question_number=181)
        other_gold["sample_id"] = "fictional_2"
        more_samples, more_gold = self.folder / "more_samples.jsonl", self.folder / "more_gold.jsonl"
        more_samples.write_text(json.dumps(other_sample) + "\n")
        more_gold.write_text(json.dumps(other_gold) + "\n")
        config = self.folder / "schedules.json"
        config.write_text(json.dumps({"now": [0.0], "later": [2.0, 5.0]}))
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), "--samples", str(self.samples_path), str(more_samples),
             "--gold", str(self.gold_path), str(more_gold), "--schedule-config", str(config),
             "--out", str(self.out), "--review", str(self.review), "--report", str(self.report)],
            capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        traces = [json.loads(line) for line in self.out.read_text().splitlines()]
        self.assertEqual(len(traces), 4)
        self.assertEqual({t["data_version"] for t in traces}, {"test-revised-v1"})
        self.assertIn("## Q151", self.review.read_text())
        self.assertIn("## Q181", self.review.read_text())
        report = json.loads(self.report.read_text())
        self.assertEqual(report["question_count"], 2)
        self.assertFalse(report["gold_fields_in_trace"])
        self.assertEqual(report["records"][0]["final_supported_at"], 0.0)

    def test_bad_inputs_keep_all_previous_outputs(self):
        original_sample, original_gold = deepcopy(self.sample), deepcopy(self.gold)
        for case in ("version", "premise_id", "premise_flag", "cycle", "duplicate"):
            with self.subTest(case=case):
                self.sample, self.gold = deepcopy(original_sample), deepcopy(original_gold)
                if case == "version":
                    self.sample["data_version"] = "wrong"
                elif case == "premise_id":
                    self.gold["units"][2]["presupposition_sets"] = [["d99s0"]]
                elif case == "premise_flag":
                    self.gold["units"][2]["by_presupposition"] = False
                elif case == "cycle":
                    self.gold["units"][0]["depends_on"] = ["u3"]
                self.write_inputs()
                if case == "duplicate":
                    self.samples_path.write_text(self.samples_path.read_text() * 2)
                before = {p: p.read_bytes() for p in (self.out, self.review, self.report)}
                result = self.run_cli()
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_output_cannot_overwrite_an_input(self):
        before = self.gold_path.read_bytes()
        result = self.run_cli(out=self.gold_path)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("must not overwrite an input", result.stderr)
        self.assertEqual(self.gold_path.read_bytes(), before)

    def test_invalid_schedules_keep_all_previous_outputs(self):
        for times in ([1, 2, 3], [True], [-1], [3, 1], [float("nan")]):
            with self.subTest(times=times):
                config = self.folder / "schedules.json"
                config.write_text(json.dumps({"bad": times}))
                before = {p: p.read_bytes() for p in (self.out, self.review, self.report)}
                result = self.run_cli(["--schedule-config", str(config)])
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_non_debug_inputs_cannot_use_default_debug_outputs(self):
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), "--samples", str(self.samples_path), "--gold", str(self.gold_path)],
            capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Non-debug traces need separate", result.stderr)


if __name__ == "__main__":
    unittest.main()
