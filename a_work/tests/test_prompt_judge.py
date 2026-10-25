import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

A_WORK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(A_WORK))

from turntaking.decompose import decompose, validate_units  # noqa: E402
from turntaking.judge import PromptJudge, resolve_dependencies  # noqa: E402
from turntaking.llm import FakeClient, parse_json_object  # noqa: E402
from turntaking.schema import SUPPORTED, UNRESOLVED, Evidence, Observation, Unit  # noqa: E402

UNITS = (Unit("u1", "director of Being Twenty", False), Unit("u2", "birthplace of {u1}", True, ("u1",)))
E1 = Evidence("e1", "Being Twenty is a 1978 Italian film directed by Fernando Di Leo.", 3.0, {})
E2 = Evidence("e2", "Fernando Di Leo was born in San Ferdinando di Puglia.", 8.0, {})


def obs(evidence, t=0.0):
    return Observation("s1", "Where was the director of film Being Twenty born?", t, tuple(evidence), UNITS, False)


def reply(*units):
    return {"units": [dict(zip(("unit_id", "label", "value", "citations"), u)) for u in units]}


class ParseTest(unittest.TestCase):
    def test_strips_think_block_and_fences(self):
        text = '<think>hmm</think>\n```json\n{"units": []}\n```'
        self.assertEqual(parse_json_object(text), {"units": []})

    def test_rejects_non_json(self):
        with self.assertRaises(ValueError):
            parse_json_object("I cannot answer that.")


class DecomposeTest(unittest.TestCase):
    BRIDGE = {"question_type": "bridge", "units": [
        {"unit_id": "u1", "description": "director of Being Twenty", "necessary": False, "depends_on": []},
        {"unit_id": "u2", "description": "birthplace of {u1}", "necessary": True, "depends_on": ["u1"]}]}

    def test_valid_bridge(self):
        qtype, units, fell_back = decompose("q", FakeClient([self.BRIDGE]))
        self.assertEqual((qtype, fell_back), ("bridge", False))
        self.assertEqual(units[1].depends_on, ("u1",))

    def test_forward_dependency_falls_back(self):
        bad = json.loads(json.dumps(self.BRIDGE))
        bad["units"][0]["depends_on"] = ["u2"]
        qtype, units, fell_back = decompose("Where was he born?", FakeClient([bad]))
        self.assertTrue(fell_back)
        self.assertEqual([(u.unit_id, u.necessary) for u in units], [("u1", True)])

    def test_single_unit_is_single(self):
        one = {"question_type": "bridge", "units": [
            {"unit_id": "u1", "description": "x", "necessary": True, "depends_on": []}]}
        self.assertEqual(validate_units(one)[0], "single")

    def test_requires_a_necessary_unit(self):
        bad = json.loads(json.dumps(self.BRIDGE))
        bad["units"][1]["necessary"] = False
        with self.assertRaises(ValueError):
            validate_units(bad)


class PromptJudgeTest(unittest.TestCase):
    def test_no_evidence_skips_model(self):
        client = FakeClient([])
        labels = PromptJudge(client).judge(obs([]))
        self.assertEqual({k: v.label for k, v in labels.items()}, {"u1": UNRESOLVED, "u2": UNRESOLVED})
        self.assertEqual(client.calls, [])

    def test_partial_evidence(self):
        client = FakeClient([reply(("u1", SUPPORTED, "Fernando Di Leo", ["e1"]), ("u2", UNRESOLVED, None, []))])
        labels = PromptJudge(client).judge(obs([E1], 3.0))
        self.assertEqual(labels["u1"].value, "Fernando Di Leo")
        self.assertEqual(labels["u2"].label, UNRESOLVED)
        self.assertIn("Being Twenty is a 1978", client.messages[0][-1]["content"])

    def test_future_or_missing_citation_downgraded(self):
        client = FakeClient([reply(("u1", SUPPORTED, "Fernando Di Leo", []), ("u2", SUPPORTED, "Italy", ["e2"]))])
        judge = PromptJudge(client)
        labels = judge.judge(obs([E1], 3.0))
        self.assertEqual(labels["u1"].label, UNRESOLVED)  # no citation
        self.assertEqual(labels["u2"].label, UNRESOLVED)  # e2 not visible yet
        self.assertEqual(judge.log[0]["downgraded"], ["u1", "u2"])

    def test_cached_per_evidence_set(self):
        client = FakeClient([reply(("u1", SUPPORTED, "Fernando Di Leo", ["e1"]))])
        judge = PromptJudge(client)
        judge.judge(obs([E1], 3.0))
        judge.judge(obs([E1], 3.5))
        self.assertEqual(len(client.calls), 1)

    def test_endpoint_error_means_nothing_supported(self):
        def boom(messages):
            raise ValueError("bad reply")
        judge = PromptJudge(FakeClient([boom]))
        labels = judge.judge(obs([E1, E2], 8.0))
        self.assertTrue(all(v.label == UNRESOLVED for v in labels.values()))
        self.assertIn("bad reply", judge.log[0]["error"])

    def test_conclusion_may_cite_dependency_units(self):
        units = (Unit("u1", "birth year of A", False), Unit("u2", "birth year of B", False),
                 Unit("u3", "who was born later", True, ("u1", "u2")))
        o = Observation("s2", "Who was born later, A or B?", 8.0, (E1, E2), units, False)
        client = FakeClient([reply(("u1", SUPPORTED, "1966", ["e1"]), ("u2", SUPPORTED, "1918", ["e2"]),
                                   ("u3", SUPPORTED, "A", ["u1", "u2"]))])
        labels = PromptJudge(client).judge(o)
        self.assertEqual(labels["u3"].label, SUPPORTED)
        self.assertEqual(labels["u3"].citations, ("e1", "e2"))

    def test_null_string_value_is_none(self):
        client = FakeClient([reply(("u1", UNRESOLVED, "null", []))])
        self.assertIsNone(PromptJudge(client).judge(obs([E1], 3.0))["u1"].value)

    def test_by_omission_kept_only_when_supported(self):
        client = FakeClient([{"units": [
            {"unit_id": "u1", "label": SUPPORTED, "value": "Fernando Di Leo", "citations": ["e1"], "by_omission": False},
            {"unit_id": "u2", "label": UNRESOLVED, "value": None, "citations": [], "by_omission": True}]}])
        labels = PromptJudge(client).judge(obs([E1], 3.0))
        self.assertFalse(labels["u1"].by_omission)
        self.assertFalse(labels["u2"].by_omission)
        client = FakeClient([{"units": [
            {"unit_id": "u1", "label": SUPPORTED, "value": "no", "citations": ["e1"], "by_omission": True}]}])
        self.assertTrue(PromptJudge(client).judge(obs([E1], 3.0))["u1"].by_omission)

    def test_dependency_still_enforced(self):
        client = FakeClient([reply(("u1", UNRESOLVED, None, []), ("u2", SUPPORTED, "San Ferdinando", ["e2"]))])
        labels = resolve_dependencies(UNITS, PromptJudge(client).judge(obs([E1, E2], 8.0)))
        self.assertEqual(labels["u2"].label, UNRESOLVED)


class TitleAndTypeTest(unittest.TestCase):
    def test_evidence_shown_with_document_title(self):
        e = Evidence("d6s1", "He won the silver medal at the 1988 Olympic Games.", 1.0, {"document_id": "Emilio Sanchez"})
        client = FakeClient([{"units": []}])
        PromptJudge(client).judge(obs([e], 1.0))
        self.assertIn("[d6s1] (Emilio Sanchez) He won", client.messages[0][-1]["content"])

    def test_question_type_inferred_from_units(self):
        import eval_judge

        def unit(uid, nec, deps=(), ss=(("e",),)):
            return {"unit_id": uid, "necessary": nec, "depends_on": list(deps), "support_sets": [list(x) for x in ss]}
        cases = {
            "single": [unit("u1", True)],
            "bridge": [unit("u1", False), unit("u2", True, ["u1"])],
            "comparison": [unit("u1", False), unit("u2", False), unit("u3", True, ["u1", "u2"], [()])],
            "bridge_comparison": [unit("u1", False), unit("u2", False, ["u1"]), unit("u3", False),
                                  unit("u4", False, ["u3"]), unit("u5", True, ["u2", "u4"], [()])],
            "multipart": [unit("u1", True), unit("u2", True)],
        }
        for expected, units in cases.items():
            self.assertEqual(eval_judge.question_type({"units": units}), expected)
        self.assertEqual(eval_judge.question_type({"question_type": "single", "units": cases["bridge"]}), "single")


class EvalScriptTest(unittest.TestCase):
    def test_runs_on_mock_data(self):
        import eval_judge
        decomp = {"question_type": "single", "units": [
            {"unit_id": "u1", "description": "answer", "necessary": True, "depends_on": []}]}

        class Client(FakeClient):
            def __init__(self, *a, **k):
                super().__init__([])

            def chat_json(self, messages, *, purpose, schema=None, max_tokens=1024):
                self.calls.append(mock.Mock(purpose=purpose, latency_s=0.1, completion_tokens=20))
                return decomp if purpose == "decompose" else {"units": []}

        with tempfile.TemporaryDirectory() as out, mock.patch.object(eval_judge, "ChatClient", Client), \
                mock.patch.object(sys, "argv", ["eval_judge.py", "--out", out]), mock.patch("builtins.print"):
            eval_judge.main()
            summary = (Path(out) / "summary.md").read_text()
        self.assertIn("## Decomposition", summary)
        self.assertIn("(30 traces)", summary)
        self.assertIn("missed SUPPORTED", summary)


if __name__ == "__main__":
    unittest.main()
