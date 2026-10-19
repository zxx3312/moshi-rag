import sys
import unittest
from pathlib import Path

A_WORK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(A_WORK))

from turntaking.judge import OracleJudge  # noqa: E402
from turntaking.policies import EvidenceAware, FirstEvidence, FixedProgress, TimeOnly, WaitAll  # noqa: E402
from turntaking.preview import preview_metrics  # noqa: E402
from turntaking.replay import load_jsonl, replay, units_without_gold  # noqa: E402
from turntaking.schema import ACTIONS, FINAL  # noqa: E402

TRACES = load_jsonl(A_WORK / "demo/trace.jsonl")
GOLDS = {g["sample_id"]: g for g in load_jsonl(A_WORK / "demo/gold.jsonl")}


def run_all():
    policies = [WaitAll(), FixedProgress(), TimeOnly(), FirstEvidence(), EvidenceAware(OracleJudge(GOLDS.values()))]
    for trace in TRACES:
        gold = GOLDS[trace["sample_id"]]
        for p in policies:
            yield trace, gold, p, replay(trace, units_without_gold(gold), p)


class ReplayTest(unittest.TestCase):
    def test_no_future_evidence_and_valid_actions(self):
        for trace, _, _, records in run_all():
            times = {e["evidence_id"]: e["visible_time_s"] for e in trace["events"]}
            for r in records:
                self.assertIn(r["action"], ACTIONS)
                for eid in r["evidence_snapshot_ids"]:
                    self.assertLessEqual(times[eid], r["decision_time_s"])
                for c in r["claim_spans"]:
                    self.assertTrue(set(c["cited_evidence_ids"]) <= set(r["evidence_snapshot_ids"]))

    def test_every_policy_finishes(self):
        for _, _, p, records in run_all():
            self.assertEqual(records[-1]["action"], FINAL, p.name)

    def test_evidence_aware_oracle_never_unsupported(self):
        for trace, gold, p, records in run_all():
            m = preview_metrics(records, trace, gold)
            if p.name.startswith("evidence_aware"):
                self.assertEqual(m["unsupported"], 0)
            if p.name == "first_evidence":
                self.assertGreater(m["unsupported"], 0)


if __name__ == "__main__":
    unittest.main()
