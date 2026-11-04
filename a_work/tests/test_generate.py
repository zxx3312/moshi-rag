import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

A_WORK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(A_WORK))

from turntaking.generate import Generator  # noqa: E402
from turntaking.judge import OracleJudge  # noqa: E402
from turntaking.llm import CallRecord, FakeClient  # noqa: E402
from turntaking.policies import EvidenceAware, FirstEvidence  # noqa: E402
from turntaking.preview import preview_metrics  # noqa: E402
from turntaking.replay import _value_span, replay, units_without_gold  # noqa: E402

TRACE = {"schema_version": "1.0", "data_version": "t", "sample_id": "s", "trace_id": "s_long", "question": "Who and when?",
         "time_origin": "question_end", "clock": "simulated", "trace_type": "controlled_mock",
         "events": [{"evidence_id": "e1", "visible_time_s": 2.0, "text": "Led by Alice.", "source": {"document_id": "Alpha"}},
                    {"evidence_id": "e2", "visible_time_s": 8.0, "text": "Released on June 1.", "source": {"document_id": "Alpha"}}],
         "retrieval_complete_time_s": 8.0}
GOLD = {"sample_id": "s", "units": [
    {"unit_id": "u1", "description": "leader", "necessary": True, "expected_answer": "Alice", "depends_on": [], "support_sets": [["e1"]]},
    {"unit_id": "u2", "description": "release date of {u1}", "necessary": True, "expected_answer": "June 1", "depends_on": [], "support_sets": [["e2"]]}]}


class Client(FakeClient):
    """Replies by request content; every call takes latency seconds."""

    def __init__(self, latency=0.0):
        super().__init__([])
        self.latency = latency

    def chat_json(self, messages, *, purpose, schema=None, max_tokens=None):
        self.messages.append(messages)
        self.calls.append(CallRecord(purpose, self.latency, None, None))
        request = messages[-1]["content"]
        if "Evidence so far" in request:
            return {"text": "I think it is Bob.", "answers": ["Bob"]} if "June 1" not in request else {"text": "It is Alice.", "answers": ["Alice"]}
        said = "Alice" if "- leader: Alice" in request else "June 1"
        return {"text": f"It is {said} so far."}


class GroundedTest(unittest.TestCase):
    def run_policy(self, latency=0.0):
        client = Client(latency)
        policy = EvidenceAware(OracleJudge([GOLD]))
        return client, replay(TRACE, units_without_gold(GOLD), policy, generator=Generator(client))

    def test_partial_prompt_gets_only_supported_facts(self):
        client, records = self.run_policy()
        request = client.messages[0][-1]["content"]
        self.assertIn("- leader: Alice", request)
        self.assertNotIn("Led by Alice.", request)  # the model read evidence aloud
        self.assertNotIn("June 1", request)
        self.assertNotIn("Released on", request)
        self.assertIn("Still checking:\n- release date of Alice", request)  # placeholder filled from the known value

    def test_finished_search_reports_what_is_unconfirmed(self):
        client = Client()
        Generator(client).grounded("q", [("leader", "Alice")], ["date"], [], True)
        self.assertIn("Could not confirm:\n- date", client.messages[0][-1]["content"])

    def test_backchannel_not_passed_as_said(self):
        client, _ = self.run_policy()
        self.assertNotIn("let me check", client.messages[0][-1]["content"])

    def test_long_partial_does_not_cut_off_final(self):
        class Wordy(Client):
            def chat_json(self, messages, *, purpose, schema=None, max_tokens=None):
                reply = super().chat_json(messages, purpose=purpose, schema=schema)
                return {"text": reply["text"] + " word" * 30}
        records = replay(TRACE, units_without_gold(GOLD), EvidenceAware(OracleJudge([GOLD])), generator=Generator(Wordy()))
        self.assertEqual(records[-1]["action"], "Final Answer")
        self.assertEqual(preview_metrics(records, TRACE, GOLD)["unsupported"], 0)
        self.assertIsNotNone(preview_metrics(records, TRACE, GOLD)["ttca"])

    def test_reply_without_value_falls_back_to_facts(self):
        class Vague(Client):
            def chat_json(self, messages, *, purpose, schema=None, max_tokens=None):
                super().chat_json(messages, purpose=purpose, schema=schema)
                return {"text": "I'm still checking the date."}
        generator = Generator(Vague())
        text, _ = generator.grounded("q", [("leader", "Alice")], ["date"], [], False)
        self.assertEqual(text, "leader: Alice. I'm still checking the rest.")
        self.assertEqual(generator.fallbacks, 1)

    def test_rambling_reply_falls_back_to_facts(self):
        class Rambling(Client):
            def chat_json(self, messages, *, purpose, schema=None, max_tokens=None):
                super().chat_json(messages, purpose=purpose, schema=schema)
                return {"text": "Alice" + " word" * 40}
        text, _ = Generator(Rambling()).grounded("q", [("leader", "Alice")], [], [], True)
        self.assertEqual(text, "leader: Alice.")

    def test_later_turn_knows_what_was_said(self):
        client, _ = self.run_policy()
        self.assertIn("It is Alice so far.", client.messages[1][-1]["content"])

    def test_generation_latency_delays_output(self):
        _, records = self.run_policy(latency=1.0)
        partial = next(r for r in records if r["action"] == "Partial Answer")
        self.assertEqual((partial["decision_time_s"], partial["generation_cost_s"], partial["output_start_time_s"]), (2.0, 1.0, 3.0))

    def test_backchannel_needs_no_model(self):
        client, records = self.run_policy()
        self.assertEqual(records[0]["action"], "Backchannel")
        self.assertEqual(len(client.calls), 2)
        self.assertEqual(preview_metrics(records, TRACE, GOLD)["unsupported"], 0)


class BaselineTest(unittest.TestCase):
    def test_baseline_answer_scored_by_value_can_be_wrong(self):
        records = replay(TRACE, units_without_gold(GOLD), FirstEvidence(), generator=Generator(Client()))
        self.assertEqual(records[-1]["claim_spans"][0]["value"], "Bob")
        metrics = preview_metrics(records, TRACE, GOLD, by_value=True)
        self.assertEqual((metrics["claims"], metrics["unsupported"]), (1, 1))

    def test_abstention_makes_no_claim(self):
        class Abstain(Client):
            def chat_json(self, messages, *, purpose, schema=None, max_tokens=None):
                super().chat_json(messages, purpose=purpose, schema=schema)
                return {"text": "The evidence does not say.", "answers": ["Unknown."]}
        records = replay(TRACE, units_without_gold(GOLD), FirstEvidence(), generator=Generator(Abstain()))
        self.assertEqual(records[-1]["claim_spans"], [])
        metrics = preview_metrics(records, TRACE, GOLD, by_value=True)
        self.assertEqual((metrics["claims"], metrics["unsupported"], metrics["ttfgi"]), (0, 0, None))

    def test_unusable_reply_is_no_answer(self):
        def bad(messages):
            raise ValueError("bad reply")
        text, answer, _ = Generator(FakeClient([bad])).free("q", [])
        self.assertEqual((text, answer), ("I'm not sure.", []))

    def test_each_answer_is_one_claim(self):
        class Two(Client):
            def chat_json(self, messages, *, purpose, schema=None, max_tokens=None):
                super().chat_json(messages, purpose=purpose, schema=schema)
                return {"text": "It was Alice on June 1.", "answers": ["Alice", "June 1"]}
        records = replay(TRACE, units_without_gold(GOLD), FirstEvidence(), generator=Generator(Two()))
        self.assertEqual([c["value"] for c in records[-1]["claim_spans"]], ["Alice", "June 1"])
        self.assertLess(records[-1]["claim_spans"][0]["start"], records[-1]["claim_spans"][1]["start"])
        metrics = preview_metrics(records, TRACE, GOLD, by_value=True)
        self.assertEqual((metrics["claims"], metrics["unsupported"]), (2, 1))  # e2 is not visible yet

    def test_cache_reports_latency_again(self):
        generator = Generator(Client(2.0))
        first = generator.free("q", [("t", "x")])
        second = generator.free("q", [("t", "x")])
        self.assertEqual(first, second)
        self.assertEqual(second[2], 2.0)
        self.assertEqual(len(generator.client.calls), 1)


class ValueSpanTest(unittest.TestCase):
    def test_value_position_in_speech(self):
        self.assertEqual(_value_span("abcd fgh j", "fgh", 10.0), (5.0, 8.0, True))
        self.assertEqual(_value_span("abc", "zzz", 3.0), (0.0, 3.0, False))
        self.assertEqual(_value_span("abc", None, 3.0), (0.0, 3.0, False))
        self.assertEqual(_value_span("I know", "no", 6.0), (0.0, 6.0, False))
        self.assertEqual(_value_span("No, it is not.", "no", 14.0), (0.0, 2.0, True))


class RunReplayGenerateTest(unittest.TestCase):
    def test_runs_with_generation(self):
        import run_replay
        decomp = {"question_type": "single", "units": [
            {"unit_id": "u1", "description": "answer", "necessary": True, "depends_on": []}]}

        class C(FakeClient):
            def __init__(self, *a, **k):
                super().__init__([])

            def chat_json(self, messages, *, purpose, schema=None, max_tokens=None):
                self.calls.append(CallRecord(purpose, 0.1, None, None))
                return {"decompose": decomp, "judge": {"units": []}, "generate": {"text": "Yes.", "answers": ["yes"]}}[purpose]

        with tempfile.TemporaryDirectory() as out, mock.patch.object(run_replay, "ChatClient", C), \
                mock.patch.object(sys, "argv", ["run_replay.py", "--out", out, "--generate"]), mock.patch("builtins.print"):
            run_replay.main()
            rows = [json.loads(l) for l in (Path(out) / "trace_metrics.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertTrue((Path(out) / "generate_calls.jsonl").exists())
        self.assertGreater(max(r["generation_cost_s"] for r in rows if r["policy"] == "wait_all"), 0)


if __name__ == "__main__":
    unittest.main()
