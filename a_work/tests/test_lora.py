import json
import sys
import tempfile
import unittest
from pathlib import Path

A_WORK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(A_WORK))

from eval_sft import parse_request  # noqa: E402
from train_lora_judge import IGNORE, batches, encode, load_examples, strip_examples  # noqa: E402
from turntaking.judge import JUDGE_SYSTEM, OracleJudge, PromptJudge, judge_messages, resolve_dependencies  # noqa: E402
from turntaking.llm import FakeClient  # noqa: E402
from turntaking.schema import SUPPORTED, UNRESOLVED, Evidence, Observation, Unit  # noqa: E402

E1 = Evidence("d1s0", "He won.", 1.0, {"document_id": "Bo Kim"})
UNITS = (Unit("u1", "whether Ann Lee won", False), Unit("u2", "whether Bo Kim won", False),
         Unit("u3", "which of them won", True, ("u1", "u2")))


def obs(units=UNITS, question="In between Ann Lee and Bo Kim, who won?"):
    return Observation("s", question, 1.0, (E1,), units, False)


class FakeTokenizer:
    """Each character is one token."""

    def apply_chat_template(self, messages, tokenize, add_generation_prompt, enable_thinking):
        assert not tokenize and add_generation_prompt and enable_thinking is False
        return "".join(m["content"] for m in messages) + "|"

    def __call__(self, text, add_special_tokens):
        assert add_special_tokens is False
        return {"input_ids": [ord(c) for c in text]}


class TrainingDataTest(unittest.TestCase):
    MESSAGES = [{"role": "system", "content": "s"}, {"role": "user", "content": "ex"}, {"role": "assistant", "content": "ex"},
                {"role": "user", "content": "q"}, {"role": "assistant", "content": "a"}]

    def test_strip_examples_keeps_system_and_final_turn(self):
        self.assertEqual([m["content"] for m in strip_examples(self.MESSAGES)], ["s", "q", "a"])

    def test_load_examples_strips_and_limits(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "x.jsonl"
            path.write_text("\n".join(json.dumps({"messages": self.MESSAGES}) for _ in range(3)))
            rows = load_examples(path, limit=2)
        self.assertEqual(len(rows), 2)
        self.assertEqual(len(rows[0]), 3)

    def test_encode_masks_prompt_and_drops_long(self):
        messages = strip_examples(self.MESSAGES)
        ids, labels = encode(messages, FakeTokenizer(), 100, end_token="$")
        self.assertEqual("".join(map(chr, ids)), "sq|a$")
        self.assertEqual(labels, [IGNORE] * 3 + [ord("a"), ord("$")])
        self.assertIsNone(encode(messages, FakeTokenizer(), 4, end_token="$"))

    def test_batches_pad_and_cover_everything(self):
        items = [([1], [1]), ([1, 2, 3], [IGNORE, 2, 3]), ([1, 2], [1, 2])]
        out = list(batches(items, 2, pad_id=0))
        self.assertEqual(out[0][0], [[1, 0, 0], [1, 2, 3]])
        self.assertEqual(out[0][1], [[1, IGNORE, IGNORE], [IGNORE, 2, 3]])
        self.assertEqual(out[0][2], [[1, 0, 0], [1, 1, 1]])
        self.assertEqual(sum(len(b[0]) for b in out), 3)


class RuntimeMatchesTrainingTest(unittest.TestCase):
    def test_lora_judge_prompt_has_no_examples(self):
        client = FakeClient([{"units": []}])
        PromptJudge(client, with_examples=False, name="lora").judge(obs())
        self.assertEqual([m["role"] for m in client.messages[0]], ["system", "user"])
        self.assertEqual(client.messages[0][0]["content"], JUDGE_SYSTEM)
        self.assertIn("explicitly ruling out one candidate", JUDGE_SYSTEM)

    def test_ruling_out_one_of_two_identifies_the_other(self):
        reply = {"units": [
            {"unit_id": "u1", "label": SUPPORTED, "value": "no", "citations": ["d1s0"]},
            {"unit_id": "u2", "label": UNRESOLVED, "value": None, "citations": []},
            {"unit_id": "u3", "label": SUPPORTED, "value": "Bo Kim", "citations": ["d1s0"], "by_presupposition": True}]}
        labels = resolve_dependencies(UNITS, PromptJudge(FakeClient([reply])).judge(obs()))
        self.assertEqual((labels["u3"].label, labels["u3"].by_presupposition), (SUPPORTED, True))

    def test_ruling_out_needs_exactly_two_candidates(self):
        units = UNITS[:2] + (Unit("u3", "third", False), Unit("u4", "which won", True, ("u1", "u2", "u3")))
        reply = {"units": [
            {"unit_id": "u1", "label": SUPPORTED, "value": "no", "citations": ["d1s0"]},
            {"unit_id": "u4", "label": SUPPORTED, "value": "Bo Kim", "citations": ["d1s0"], "by_presupposition": True}]}
        labels = PromptJudge(FakeClient([reply])).judge(obs(units))
        self.assertEqual(labels["u4"].label, UNRESOLVED)

    def test_parse_request_round_trip(self):
        request = judge_messages(obs(), with_examples=False)[-1]["content"]
        question, units, visible = parse_request(request)
        self.assertEqual(question, obs().question)
        self.assertEqual([u.unit_id for u in units], ["u1", "u2", "u3"])
        self.assertEqual(units[2].depends_on, ("u1", "u2"))
        self.assertEqual(visible, ["d1s0"])


class OraclePresuppositionTest(unittest.TestCase):
    GOLD = {"sample_id": "s", "units": [
        {"unit_id": "u1", "description": "a", "necessary": False, "expected_answer": "yes", "depends_on": [], "support_sets": [["d2s0"]]},
        {"unit_id": "u2", "description": "b", "necessary": False, "expected_answer": "no", "depends_on": [], "support_sets": []},
        {"unit_id": "u3", "description": "c", "necessary": True, "expected_answer": "Ann Lee", "depends_on": ["u1", "u2"],
         "support_sets": [[]], "by_presupposition": True, "presupposition_sets": [["d2s0"]]}]}

    def judged(self, evidence_id):
        e = Evidence(evidence_id, "x", 1.0, {})
        units = tuple(Unit(u["unit_id"], u["description"], u["necessary"], tuple(u["depends_on"])) for u in self.GOLD["units"])
        o = Observation("s", "q", 1.0, (e,), units, False)
        return resolve_dependencies(units, OracleJudge([self.GOLD]).judge(o))

    def test_presupposition_set_supports_conclusion(self):
        labels = self.judged("d2s0")
        self.assertEqual((labels["u1"].label, labels["u2"].label), (SUPPORTED, UNRESOLVED))
        self.assertEqual((labels["u3"].label, labels["u3"].by_presupposition, labels["u3"].citations), (SUPPORTED, True, ("d2s0",)))

    def test_nothing_supported_without_its_evidence(self):
        self.assertEqual(self.judged("d9s9")["u3"].label, UNRESOLVED)


if __name__ == "__main__":
    unittest.main()
