import sys
import unittest
from pathlib import Path

A_WORK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(A_WORK))

from turntaking.judge import OracleJudge  # noqa: E402
from turntaking.policies import EvidenceAware, FirstEvidence, FixedProgress, TimeOnly, WaitAll  # noqa: E402
from turntaking.preview import claim_supported, preview_metrics, value_match  # noqa: E402
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



class TimedJudge:
    """Oracle labels with a fixed latency per evidence set; counts real judge calls."""
    name = "timed"

    def __init__(self, gold, latency):
        self.oracle, self.latency, self.calls = OracleJudge(gold), latency, 0

    def judge(self, obs):
        self.calls += 1
        return self.oracle.judge(obs)

    def latency_s(self, obs):
        return self.latency if obs.evidence else 0.0


class JudgeClockTest(unittest.TestCase):
    TRACE = {"schema_version": "1.0", "data_version": "t", "sample_id": "s", "trace_id": "s_long", "question": "q",
             "time_origin": "question_end", "clock": "simulated", "trace_type": "controlled_mock",
             "events": [{"evidence_id": "e1", "visible_time_s": 2.0, "text": "a", "source": {}},
                        {"evidence_id": "e2", "visible_time_s": 8.0, "text": "b", "source": {}}],
             "retrieval_complete_time_s": 8.0}
    GOLD = {"sample_id": "s", "units": [
        {"unit_id": "u1", "description": "first", "necessary": True, "expected_answer": "x", "depends_on": [], "support_sets": [["e1"]]},
        {"unit_id": "u2", "description": "second", "necessary": True, "expected_answer": "y", "depends_on": [], "support_sets": [["e2"]]}]}

    def run_policy(self, latency=1.5, **kw):
        policy = EvidenceAware(TimedJudge([self.GOLD], latency))
        return replay(self.TRACE, units_without_gold(self.GOLD), policy, **kw)

    def test_latency_delays_output(self):
        records = {r["action"]: r for r in self.run_policy()}
        partial, final = records["Partial Answer"], records["Final Answer"]
        self.assertEqual((partial["decision_time_s"], partial["decision_cost_s"], partial["output_start_time_s"]), (2.0, 1.5, 3.5))
        self.assertEqual((final["decision_time_s"], final["output_start_time_s"]), (8.0, 9.5))
        self.assertEqual(partial["claim_spans"][0]["start"], 3.5)

    def test_cost_charged_once_per_evidence_set(self):
        total = sum(r["decision_cost_s"] for r in self.run_policy())
        self.assertEqual(total, 3.0)

    def test_setup_cost_delays_first_judgment(self):
        records = self.run_policy(latency=0.0, setup_cost_s=3.0)
        partial = next(r for r in records if r["action"] == "Partial Answer")
        self.assertEqual(partial["decision_time_s"], 3.0)  # e1 arrived at 2 s, decomposition ended at 3 s
        self.assertEqual(records[0]["action"], "Backchannel")  # acknowledging needs no units
        self.assertEqual(records[0]["output_start_time_s"], 0.0)


class EarlyEvidenceTest(unittest.TestCase):
    def test_no_final_answer_before_units_are_ready(self):
        trace = dict(JudgeClockTest.TRACE, retrieval_complete_time_s=0.0,
                     events=[dict(e, visible_time_s=0.0) for e in JudgeClockTest.TRACE["events"]])
        policy = EvidenceAware(TimedJudge([JudgeClockTest.GOLD], 0.0))
        records = replay(trace, units_without_gold(JudgeClockTest.GOLD), policy, setup_cost_s=2.0)
        self.assertEqual([r["action"] for r in records], ["Backchannel", "Final Answer"])
        self.assertEqual(records[-1]["decision_time_s"], 2.0)
        self.assertEqual(len(records[-1]["claim_spans"]), 2)


class PreviewTest(unittest.TestCase):
    GOLD = {"sample_id": "s", "units": [
        {"unit_id": "u1", "description": "a", "necessary": False, "expected_answer": "1966", "depends_on": [], "support_sets": [["e1"]]},
        {"unit_id": "u2", "description": "b", "necessary": False, "expected_answer": "1918", "depends_on": [], "support_sets": [["e2"]]},
        {"unit_id": "u3", "description": "c", "necessary": True, "expected_answer": "Ann", "aliases": ["Ann Lee"],
         "depends_on": ["u1", "u2"], "support_sets": [[]]}]}
    TRACE = {"events": [{"evidence_id": "e1", "visible_time_s": 2.0}, {"evidence_id": "e2", "visible_time_s": 8.0}]}

    def units(self):
        return {u["unit_id"]: u for u in self.GOLD["units"]}

    def claim(self, uid, start, value=None):
        return {"controller_unit_id": uid, "start": start, "end": start + 2, "value": value}

    def test_empty_support_set_needs_dependencies(self):
        self.assertFalse(claim_supported(self.claim("u3", 3.0), self.units(), self.TRACE))
        self.assertTrue(claim_supported(self.claim("u3", 8.0), self.units(), self.TRACE))

    def test_presupposed_unit_needs_one_dependency(self):
        units = self.units()
        units["u3"] = dict(units["u3"], by_presupposition=True)
        self.assertTrue(claim_supported(self.claim("u3", 3.0), units, self.TRACE))
        self.assertFalse(claim_supported(self.claim("u3", 1.0), units, self.TRACE))

    def test_wrong_value_is_unsupported(self):
        self.assertFalse(claim_supported(self.claim("u1", 3.0, "1950"), self.units(), self.TRACE))

    def test_by_value_ignores_controller_ids(self):
        units = self.units()
        self.assertTrue(claim_supported(self.claim("u9", 3.0, "1966"), units, self.TRACE, by_value=True))
        self.assertTrue(claim_supported(self.claim("u9", 8.0, "Ann Lee"), units, self.TRACE, by_value=True))
        self.assertFalse(claim_supported(self.claim("u9", 3.0, "1918"), units, self.TRACE, by_value=True))  # e2 not yet
        self.assertFalse(claim_supported(self.claim("u1", 3.0, "Bob"), units, self.TRACE, by_value=True))

    def test_value_match_uses_whole_words(self):
        self.assertTrue(value_match("no", ["no"]))
        self.assertFalse(value_match("no", ["Norman"]))
        self.assertTrue(value_match("July 16, 1969", ["July 16"]))


if __name__ == "__main__":
    unittest.main()
