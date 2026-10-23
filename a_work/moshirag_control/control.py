"""Training-free control of MoshiRAG: constrain its text stream, optionally override its
audio tokens, and schedule reference injections, all on the model step clock (12.5 steps/s).

Moshi samples a text token and then the audio tokens of each step. Constraining the text
alone does not control the audio (full_v1), so quiet modes can also replace the audio tokens
with silence, and CLIP replays a recorded clip of the model's own speech (text + audio):
  * silence                    -> PAD text (+ silent audio when the plan mutes audio)   Wait
  * clip                       -> replay the model's own recorded words, then `after`    Backchannel, Progress, release cue
  * speak_once                 -> free until one utterance ends, then held quiet         Partial Answer
  * free                       -> no restriction                                        Final Answer
  * say                        -> text-only phrase forcing (full_v1; does not drive audio)

Pure Python: the GPU job calls allowed() before sampling text, reads audio_action for the
same step, calls on_sampled() after sampling, and injections_due() for references.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, List, Mapping, Optional, Sequence, Tuple

FREE, SILENCE, SAY, SPEAK_ONCE, CLIP = "free", "silence", "say", "speak_once", "clip"
MODES = (FREE, SILENCE, SAY, SPEAK_ONCE, CLIP)
HELD = "held"


@dataclass(frozen=True)
class Segment:
    """A control mode starting at start_s (seconds after the question ends) and lasting
    until the next segment starts. Before the first segment the model is free.
    CLIP replays `clip` and then continues as `after` for the rest of the segment."""
    start_s: float
    mode: str
    phrase: str = ""
    clip: str = ""
    after: str = SILENCE


@dataclass(frozen=True)
class Injection:
    time_s: float
    text: str
    label: str


@dataclass(frozen=True)
class Plan:
    condition: str
    segments: Tuple[Segment, ...]
    injections: Tuple[Injection, ...]
    mute_audio: bool = False


@dataclass(frozen=True)
class TokenIds:
    pad: int
    epad: int
    ret: Optional[int] = None


def seconds_to_steps(t: float, frame_rate: float) -> int:
    return int(round(t * frame_rate))


class TextController:
    """Per-run state machine. Steps are LM steps since the run started (= input frame index)."""

    def __init__(
        self,
        plan: Plan,
        *,
        question_end_step: int,
        frame_rate: float,
        ids: TokenIds,
        encode: Callable[[str], Sequence[int]],
        clips: Optional[Mapping[str, Sequence[int]]] = None,
        max_pad_run: int = 8,
        hold_after_pads: int = 12,
    ):
        clips = clips or {}
        for s in plan.segments:
            if s.mode not in MODES or s.after not in (FREE, SILENCE, SPEAK_ONCE):
                raise ValueError(f"unsupported segment {s}")
            if s.mode == CLIP and s.clip not in clips:
                raise ValueError(f"clip {s.clip!r} not loaded")
        self.plan = plan
        self.ids = ids
        self.clips = {k: list(v) for k, v in clips.items()}
        self.max_pad_run = max_pad_run
        self.hold_after_pads = hold_after_pads
        self.question_end_step = question_end_step
        self.segment_steps = [question_end_step + seconds_to_steps(s.start_s, frame_rate) for s in plan.segments]
        self.injection_steps = [question_end_step + seconds_to_steps(i.time_s, frame_rate) for i in plan.injections]
        self._phrases: Dict[str, List[int]] = {s.phrase: list(encode(s.phrase)) for s in plan.segments if s.mode == SAY}
        self._injected = [False] * len(plan.injections)

        self._seg_idx: Optional[int] = None
        self._pos = 0  # position inside the current phrase or clip
        self._prev: Optional[int] = None
        self._pad_run = 0
        self._spoke = False
        self._held = False
        self._mode = FREE
        self.audio_action: Optional[Tuple] = None  # None | ("silence",) | ("clip", name, frame)
        self.rows: List[dict] = []  # one per step: mode, restricted, token, audio

    @property
    def last_scheduled_step(self) -> int:
        clip_end = [s + len(self.clips[g.clip]) for s, g in zip(self.segment_steps, self.plan.segments) if g.mode == CLIP]
        return max(self.segment_steps + self.injection_steps + clip_end + [self.question_end_step])

    def _enter(self, step: int) -> Optional[Segment]:
        idx = None
        for i, s in enumerate(self.segment_steps):
            if step >= s:
                idx = i
        if idx != self._seg_idx:
            self._seg_idx = idx
            self._pos = 0
            self._spoke = False
            self._held = False
        return None if idx is None else self.plan.segments[idx]

    def _quiet(self) -> List[int]:
        return [self.ids.pad] + ([self.ids.ret] if self.ids.ret is not None else [])

    def _mute(self) -> Optional[Tuple]:
        return ("silence",) if self.plan.mute_audio else None

    def allowed(self, step: int) -> Optional[List[int]]:
        """Token ids the model may sample at this step (None: no restriction). Also sets audio_action."""
        seg = self._enter(step)
        mode = FREE if seg is None else seg.mode
        if mode == CLIP:
            clip = self.clips[seg.clip]
            if self._pos < len(clip):
                self._mode, self.audio_action = CLIP, ("clip", seg.clip, self._pos)
                return [clip[self._pos]]
            mode = seg.after
        self._mode, self.audio_action = mode, None

        if mode == FREE:
            return None
        if mode == SILENCE:
            self.audio_action = self._mute()
            return self._quiet()
        if mode == SPEAK_ONCE:
            if self._held:
                self._mode, self.audio_action = HELD, self._mute()
                return self._quiet()
            return None
        phrase = self._phrases[seg.phrase]
        if self._pos >= len(phrase):
            self.audio_action = self._mute()
            return [self.ids.pad]
        nxt = phrase[self._pos]
        if self._prev == self.ids.epad or self._pad_run >= self.max_pad_run:
            return [nxt]
        return [self.ids.pad, self.ids.epad, nxt]

    def on_sampled(self, step: int, token: int, restricted: bool) -> None:
        mode = self._mode
        if mode == CLIP:
            self._pos += 1
        elif mode == SAY:
            phrase = self._phrases[self.plan.segments[self._seg_idx].phrase]
            if self._pos < len(phrase) and token == phrase[self._pos]:
                self._pos += 1
        self._pad_run = self._pad_run + 1 if token == self.ids.pad else 0
        if mode == SPEAK_ONCE and not self._held:
            if token not in (self.ids.pad, self.ids.epad, self.ids.ret):
                self._spoke = True
            elif self._spoke and self._pad_run >= self.hold_after_pads:
                self._held = True
        self._prev = token
        audio = None if self.audio_action is None else self.audio_action[0]
        self.rows.append({"step": step, "mode": HELD if self._held and mode == SPEAK_ONCE else mode,
                          "restricted": restricted, "token": token, "audio": audio})

    def injections_due(self, step: int) -> List[Tuple[int, Injection]]:
        """Injections to hand over at this step so the model consumes them from the next step on."""
        due = []
        for i, (s, inj) in enumerate(zip(self.injection_steps, self.plan.injections)):
            if not self._injected[i] and s <= step + 1:
                self._injected[i] = True
                due.append((i, inj))
        return due
