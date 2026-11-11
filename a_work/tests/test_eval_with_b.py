"""Exercise the wrapper against B's real, locally available evaluator without models."""
import json
import hashlib
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

A_WORK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(A_WORK))
from turntaking.judge import OracleJudge
from turntaking.llm import FakeClient
from turntaking.generate import Generator
from turntaking.policies import EvidenceAware
from turntaking.replay import replay, units_without_gold, write_jsonl


class EvaluatorWrapperTest(unittest.TestCase):
    def test_reviews_are_separate_and_invalid_logs_fail(self):
        repo = A_WORK.parent
        ref = subprocess.run(["git", "rev-parse", "--verify", "origin/b-data-eval"], cwd=repo,
                             capture_output=True, text=True)
        if ref.returncode:
            self.skipTest("B evaluator branch is not available locally")
        trace = {"schema_version": "1.0", "data_version": "test", "sample_id": "s", "trace_id": "s_long",
                 "question": "Who leads Alpha?", "time_origin": "question_end", "clock": "simulated",
                 "trace_type": "controlled_mock", "retrieval_complete_time_s": 2.0,
                 "events": [{"evidence_id": "e1", "text": "Alice leads Alpha.", "visible_time_s": 2.0,
                             "source": {"document_id": "Alpha"}}]}
        gold = {"schema_version": "1.0", "data_version": "test", "sample_id": "s",
                "units": [{"unit_id": "u1", "description": "leader", "necessary": True, "depends_on": [],
                           "expected_answer": "Alice", "support_sets": [["e1"]]}]}
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            write_jsonl(root / "trace.jsonl", [trace])
            write_jsonl(root / "gold.jsonl", [gold])
            (root / "run_config.json").write_text(json.dumps({"trace": str(root / "trace.jsonl"),
                                                            "gold": str(root / "gold.jsonl")}))
            policy = EvidenceAware(OracleJudge([gold]))
            records = replay(trace, units_without_gold(gold), policy,
                             generator=Generator(FakeClient([{"text": "Alice leads Alpha."}])))
            # An independent controller ID requires a review; mapping must not change its value.
            for row in records:
                row["policy"] = "test_policy"
                row["run_id"] = "s_long__test_policy__s0"
                for claim in row["claim_spans"]:
                    claim["controller_unit_id"] = "custom_unit"
            write_jsonl(root / "policy_log.jsonl", records)
            write_jsonl(root / "trace_metrics.jsonl", [{"policy": "test_policy", "final_correct": True,
                                                        "unsupported": 0, "claims": 1}])
            review = {"run_id": records[-1]["run_id"], "record_index": len(records) - 1,
                      "claim_index": 0, "gold_unit_id": "u1", "reviewer": "test_fixture",
                      "source_log_sha256": hashlib.sha256((root / "policy_log.jsonl").read_bytes()).hexdigest()}
            write_jsonl(root / "reviews.jsonl", [review])
            base = [sys.executable, str(A_WORK / "eval_with_b.py"), str(root), "--ref", ref.stdout.strip()]
            result = subprocess.run(base, cwd=repo, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            original = (root / "b_eval/summary.json").read_bytes()
            refused = subprocess.run(base + ["--reviews", str(root / "reviews.jsonl")], capture_output=True, text=True)
            self.assertEqual(refused.returncode, 2)
            reviewed = base + ["--reviews", str(root / "reviews.jsonl"), "--out", str(root / "assisted")]
            result = subprocess.run(reviewed, cwd=repo, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual((root / "b_eval/summary.json").read_bytes(), original)
            scored = json.loads((root / "assisted/claim_scores.jsonl").read_text().splitlines()[0])
            self.assertEqual((scored["mapping_source"], scored["label"]), ("review", "SUPPORTED"))
            records[-1]["evidence_snapshot_ids"] = ["future_nonexistent_evidence"]
            write_jsonl(root / "policy_log.jsonl", records)
            stale = subprocess.run(reviewed, cwd=repo, capture_output=True, text=True)
            self.assertEqual(stale.returncode, 2)
            self.assertIn("source_log_sha256", stale.stderr)
            failed = subprocess.run(base + ["--out", str(root / "invalid")], cwd=repo, capture_output=True, text=True)
            self.assertEqual(failed.returncode, 1, failed.stdout + failed.stderr)


if __name__ == "__main__":
    unittest.main()
