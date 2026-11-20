"""Check the parameter sweep reaches the normal replay entry point."""
import argparse
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import run_parameter_case
import run_replay
from turntaking.llm import CallRecord, FakeClient


class ParameterSweepTest(unittest.TestCase):
    def test_cases_change_one_parameter_from_baseline(self):
        baseline = run_parameter_case.CASES[0][1:]
        self.assertEqual(baseline, (3.0, 1.0, 3.0))
        self.assertEqual(len({case[0] for case in run_parameter_case.CASES}), 7)
        for case in run_parameter_case.CASES[1:]:
            self.assertEqual(sum(a != b for a, b in zip(case[1:], baseline)), 1)

    def test_replay_passes_parameters_to_all_policy_copies(self):
        class Client(FakeClient):
            def __init__(self, *args, **kwargs):
                super().__init__([])

            def chat_json(self, messages, *, purpose, schema=None, max_tokens=None):
                self.calls.append(CallRecord(purpose, 0.1, None, None))
                return {"decompose": {"question_type": "single", "units": [
                            {"unit_id": "u1", "description": "answer", "necessary": True, "depends_on": []}]},
                        "judge": {"units": []},
                        "generate": {"text": "Yes.", "answers": ["yes"]}}[purpose]

        args = ["run_replay.py", "--generate", "--concurrent", "--time-only-at-s", "5",
                "--fixed-progress-at-s", "3", "--evidence-progress-after-s", "1"]
        with tempfile.TemporaryDirectory() as out, \
                mock.patch.object(run_replay, "ChatClient", Client), \
                mock.patch.object(run_replay, "TimeOnly", wraps=run_replay.TimeOnly) as time_only, \
                mock.patch.object(run_replay, "FixedProgress", wraps=run_replay.FixedProgress) as fixed, \
                mock.patch.object(run_replay, "EvidenceAware", wraps=run_replay.EvidenceAware) as evidence, \
                mock.patch.object(sys, "argv", args + ["--out", out]), mock.patch("builtins.print"):
            run_replay.main()
            config = json.loads((Path(out) / "run_config.json").read_text())
        time_only.assert_called_once_with(5.0)
        fixed.assert_called_once_with(3.0)
        self.assertEqual(len(evidence.call_args_list), 6)
        self.assertTrue(all(call.args[1] == 1.0 for call in evidence.call_args_list))
        self.assertEqual(config["time_only_at_s"], 5.0)
        self.assertEqual(config["fixed_progress_at_s"], 3.0)
        self.assertEqual(config["evidence_progress_after_s"], 1.0)

    def test_negative_and_nonfinite_thresholds_are_rejected(self):
        for text in ("-1", "inf", "nan"):
            with self.subTest(text=text), self.assertRaises(argparse.ArgumentTypeError):
                run_replay.nonnegative_seconds(text)
