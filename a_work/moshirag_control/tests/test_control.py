import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from conditions import PROGRESS_PHRASE, build_plan  # noqa: E402
from control import FREE, SAY, SILENCE, SPEAK_ONCE, Plan, Segment, TextController, TokenIds  # noqa: E402

IDS = TokenIds(pad=3, epad=0, ret=32001)
PHRASE_IDS = {PROGRESS_PHRASE: [101, 102, 103], "Hi there": [201, 202]}
EVENTS = [
    {"evidence_id": "e2", "visible_time_s": 8.0, "text": "Alpha was released on June 1."},
    {"evidence_id": "e1", "visible_time_s": 2.0, "text": "Alpha is led by Alice."},
]


def make(plan, qe=10):
    return TextController(plan, question_end_step=qe, frame_rate=12.5, ids=IDS, encode=PHRASE_IDS.__getitem__)


def drive(ctrl, steps, choose):
    """Run the controller; choose(allowed, step) picks the sampled token."""
    for step in range(steps):
        allowed = ctrl.allowed(step)
        ctrl.on_sampled(step, choose(allowed, step), allowed is not None)


class ConditionTest(unittest.TestCase):
    def test_cumulative_injections_sorted(self):
        plan = build_plan("free", EVENTS)
        self.assertEqual([i.label for i in plan.injections], ["e1", "e1+e2"])
        self.assertEqual(plan.injections[1].text, "Alpha is led by Alice. Alpha was released on June 1.")

    def test_ours_segments(self):
        plan = build_plan("ours", EVENTS)
        self.assertEqual([(s.start_s, s.mode) for s in plan.segments],
                         [(0.0, SAY), (2.0, SPEAK_ONCE), (8.0, FREE)])

    def test_notready_adds_first_injection(self):
        plan = build_plan("notready", EVENTS)
        self.assertEqual([i.label for i in plan.injections], ["not_ready", "e1", "e1+e2"])
        self.assertEqual(plan.injections[0].time_s, 0.0)


class ControllerTest(unittest.TestCase):
    def test_free_before_question_end_and_silence_after(self):
        ctrl = make(build_plan("wait", EVENTS))
        self.assertIsNone(ctrl.allowed(9))
        self.assertEqual(ctrl.allowed(10), [IDS.pad, IDS.ret])
        self.assertEqual(ctrl.allowed(10 + 99), [IDS.pad, IDS.ret])
        self.assertIsNone(ctrl.allowed(10 + 100))  # 8 s * 12.5 = 100 steps

    def test_say_speaks_phrase_then_pads(self):
        ctrl = make(Plan("t", (Segment(0.0, SAY, "Hi there"),), ()), qe=0)
        # Model prefers PAD whenever allowed; the controller must still finish the phrase.
        drive(ctrl, 30, lambda allowed, _: IDS.pad if IDS.pad in allowed else allowed[0])
        spoken = [r["token"] for r in ctrl.rows if r["token"] not in (IDS.pad, IDS.epad)]
        self.assertEqual(spoken, [201, 202])
        self.assertEqual(ctrl.allowed(31), [IDS.pad])

    def test_epad_forces_next_word(self):
        ctrl = make(Plan("t", (Segment(0.0, SAY, "Hi there"),), ()), qe=0)
        ctrl.on_sampled(0, IDS.epad, True)
        self.assertEqual(ctrl.allowed(1), [201])

    def test_speak_once_holds_after_utterance(self):
        ctrl = make(Plan("t", (Segment(0.0, SPEAK_ONCE),), ()), qe=0)
        script = [IDS.pad] * 3 + [500, 501] + [IDS.pad] * 20
        drive(ctrl, len(script), lambda allowed, step: script[step] if allowed is None else allowed[0])
        modes = [r["mode"] for r in ctrl.rows]
        self.assertEqual(modes[4], SPEAK_ONCE)
        self.assertIn("held", modes)
        held_at = modes.index("held")
        self.assertEqual(held_at, 4 + ctrl.hold_after_pads)
        self.assertEqual(ctrl.allowed(len(script)), [IDS.pad, IDS.ret])

    def test_injection_handed_over_one_step_early(self):
        ctrl = make(build_plan("free", EVENTS), qe=10)
        self.assertEqual(ctrl.injections_due(10 + 23), [])
        due = ctrl.injections_due(10 + 24)  # e1 at 2 s = step 35; handed over at 34
        self.assertEqual([inj.label for _, inj in due], ["e1"])
        self.assertEqual(ctrl.injections_due(10 + 24), [])

    def test_unknown_mode_rejected(self):
        with self.assertRaises(ValueError):
            make(Plan("t", (Segment(0.0, "shout"),), ()))


if __name__ == "__main__":
    unittest.main()
