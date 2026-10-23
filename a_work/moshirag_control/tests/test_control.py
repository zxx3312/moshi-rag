import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from conditions import PROGRESS_PHRASE, build_plan  # noqa: E402
from control import CLIP, FREE, SAY, SILENCE, SPEAK_ONCE, Plan, Segment, TextController, TokenIds  # noqa: E402

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


CLIPS = {"look_it_up": [301, 3, 302, 3], "oh": [401, 402, 3]}


def make_v2(plan, qe=10):
    return TextController(plan, question_end_step=qe, frame_rate=12.5, ids=IDS, encode=PHRASE_IDS.__getitem__,
                          clips=CLIPS)


class AudioControlTest(unittest.TestCase):
    def test_v1_wait_leaves_audio_alone(self):
        ctrl = make_v2(build_plan("wait", EVENTS))
        ctrl.allowed(12)
        self.assertIsNone(ctrl.audio_action)

    def test_wait_av_mutes_audio_until_release(self):
        ctrl = make_v2(build_plan("wait_av", EVENTS))
        self.assertEqual(ctrl.allowed(12), [IDS.pad, IDS.ret])
        self.assertEqual(ctrl.audio_action, ("silence",))
        self.assertIsNone(ctrl.allowed(110))
        self.assertIsNone(ctrl.audio_action)

    def test_progress_clip_replays_then_mutes_then_kicks(self):
        ctrl = make_v2(build_plan("progress_clip", EVENTS))
        drive(ctrl, 125, lambda allowed, _: allowed[0] if allowed else 999)
        by_step = {r["step"]: r for r in ctrl.rows}
        self.assertEqual([by_step[s]["token"] for s in range(10, 14)], CLIPS["look_it_up"])
        self.assertEqual(by_step[14]["mode"], SILENCE)
        self.assertEqual(by_step[14]["audio"], "silence")
        self.assertEqual([by_step[s]["token"] for s in range(110, 113)], CLIPS["oh"])
        self.assertEqual(by_step[110]["audio"], "clip")
        self.assertEqual(by_step[113]["mode"], FREE)
        self.assertIsNone(by_step[113]["audio"])

    def test_clip_audio_frames_advance(self):
        ctrl = make_v2(Plan("t", (Segment(0.0, CLIP, clip="oh"),), (), mute_audio=True), qe=0)
        frames = []
        for step in range(4):
            allowed = ctrl.allowed(step)
            frames.append(ctrl.audio_action)
            ctrl.on_sampled(step, allowed[0], True)
        self.assertEqual(frames, [("clip", "oh", 0), ("clip", "oh", 1), ("clip", "oh", 2), ("silence",)])

    def test_progress_inj_holds_with_silent_audio(self):
        plan = build_plan("progress_inj", EVENTS)
        self.assertEqual(plan.injections[0].label, "not_ready")
        ctrl = make_v2(plan, qe=0)
        script = [500, 501] + [IDS.pad] * 20
        drive(ctrl, len(script), lambda allowed, step: script[step] if allowed is None else allowed[0])
        held = [r for r in ctrl.rows if r["mode"] == "held"]
        self.assertTrue(held)
        self.assertEqual(held[-1]["audio"], "silence")

    def test_ours_v2_segments(self):
        plan = build_plan("ours_v2", EVENTS)
        self.assertEqual([(s.start_s, s.mode, s.clip, s.after) for s in plan.segments], [
            (0.0, CLIP, "look_it_up", SILENCE), (2.0, CLIP, "oh", SPEAK_ONCE), (8.0, CLIP, "oh", FREE)])

    def test_missing_clip_rejected(self):
        with self.assertRaises(ValueError):
            make(build_plan("progress_clip", EVENTS))

    def test_last_scheduled_step_includes_clip(self):
        ctrl = make_v2(build_plan("wait_av_kick", EVENTS))
        self.assertEqual(ctrl.last_scheduled_step, 110 + len(CLIPS["oh"]))


UNITS = [
    {"unit_id": "u1", "support": ["e1"]},
    {"unit_id": "u2", "support": ["e2"], "pending": "The release date is still being searched."},
]


class StatusNotesTest(unittest.TestCase):
    def test_ours_v3_notes_pending_then_complete(self):
        plan = build_plan("ours_v3", EVENTS, UNITS)
        first, last = plan.injections
        self.assertEqual(first.text, "Alpha is led by Alice. The release date is still being searched.")
        self.assertEqual(last.text, "Alpha is led by Alice. Alpha was released on June 1. The search is complete.")
        self.assertEqual([s.mode for s in plan.segments], [s.mode for s in build_plan("ours_v2", EVENTS).segments])

    def test_other_conditions_have_no_notes(self):
        for cond in ("free", "ours_v2", "progress_clip"):
            texts = [i.text for i in build_plan(cond, EVENTS, UNITS).injections]
            self.assertFalse(any("searched" in t or "complete" in t for t in texts), cond)


if __name__ == "__main__":
    unittest.main()
