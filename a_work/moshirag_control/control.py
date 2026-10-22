"""Training-free control of MoshiRAG: constrain its inner-monologue text stream and
schedule reference injections, both on the model step clock (12.5 steps per second).

Moshi samples one text token per step and generates the audio for that step
conditioned on it, so restricting the allowed text tokens controls what it says:
  * only PAD                    -> it stays silent (Wait)
  * PAD / EPAD / next word      -> it speaks a fixed phrase at its own pace (Backchannel, Progress)
  * no restriction              -> it answers freely from the injected evidence (Partial, Final)

Pure Python: the GPU job calls allowed() before sampling, on_sampled() after it,
and injections_due() to know when to hand the model a reference.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, List, Optional, Sequence, Tuple

FREE, SILENCE, SAY, SPEAK_ONCE = "free", "silence", "say", "speak_once"
MODES = (FREE, SILENCE, SAY, SPEAK_ONCE)


@dataclass(frozen=True)
class Segment:
    """A control mode starting at start_s (seconds after the question ends) and
    lasting until the next segment starts. Before the first segment the model is free."""
    start_s: float
    mode: str
    phrase: str = ""


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
        max_pad_run: int = 8,
        hold_after_pads: int = 12,
    ):
        for s in plan.segments:
            if s.mode not in MODES:
                raise ValueError(f"unknown mode {s.mode!r}")
        self.plan = plan
        self.ids = ids
        self.max_pad_run = max_pad_run
        self.hold_after_pads = hold_after_pads
        self.question_end_step = question_end_step
        self.segment_steps = [question_end_step + seconds_to_steps(s.start_s, frame_rate) for s in plan.segments]
        self.injection_steps = [question_end_step + seconds_to_steps(i.time_s, frame_rate) for i in plan.injections]
        self._phrases: Dict[str, List[int]] = {s.phrase: list(encode(s.phrase)) for s in plan.segments if s.mode == SAY}
        self._injected = [False] * len(plan.injections)

        self._seg_idx: Optional[int] = None
        self._phrase_pos = 0
        self._prev: Optional[int] = None
        self._pad_run = 0
        self._spoke = False
        self._held = False
        self.rows: List[dict] = []  # one per step: mode, restricted, token

    @property
    def last_scheduled_step(self) -> int:
        return max(self.segment_steps + self.injection_steps + [self.question_end_step])

    def _segment(self, step: int) -> Optional[int]:
        idx = None
        for i, s in enumerate(self.segment_steps):
            if step >= s:
                idx = i
        return idx

    def _enter(self, step: int) -> Optional[Segment]:
        idx = self._segment(step)
        if idx != self._seg_idx:
            self._seg_idx = idx
            self._phrase_pos = 0
            self._spoke = False
            self._held = False
        return None if idx is None else self.plan.segments[idx]

    def _quiet(self) -> List[int]:
        return [self.ids.pad] + ([self.ids.ret] if self.ids.ret is not None else [])

    def allowed(self, step: int) -> Optional[List[int]]:
        """Token ids the model may sample at this step, or None for no restriction."""
        seg = self._enter(step)
        if seg is None or seg.mode == FREE:
            return None
        if seg.mode == SILENCE:
            return self._quiet()
        if seg.mode == SPEAK_ONCE:
            return self._quiet() if self._held else None
        phrase = self._phrases[seg.phrase]
        if self._phrase_pos >= len(phrase):
            return [self.ids.pad]
        nxt = phrase[self._phrase_pos]
        if self._prev == self.ids.epad or self._pad_run >= self.max_pad_run:
            return [nxt]
        return [self.ids.pad, self.ids.epad, nxt]

    def on_sampled(self, step: int, token: int, restricted: bool) -> None:
        seg = None if self._seg_idx is None else self.plan.segments[self._seg_idx]
        mode = FREE if seg is None else seg.mode
        if mode == SAY:
            phrase = self._phrases[seg.phrase]
            if self._phrase_pos < len(phrase) and token == phrase[self._phrase_pos]:
                self._phrase_pos += 1
        self._pad_run = self._pad_run + 1 if token == self.ids.pad else 0
        if mode == SPEAK_ONCE and not self._held:
            if token not in (self.ids.pad, self.ids.epad, self.ids.ret):
                self._spoke = True
            elif self._spoke and self._pad_run >= self.hold_after_pads:
                self._held = True
        self._prev = token
        self.rows.append({"step": step, "mode": "held" if self._held else mode, "restricted": restricted, "token": token})

    def injections_due(self, step: int) -> List[Tuple[int, Injection]]:
        """Injections to hand over at this step so the model consumes them from the next step on."""
        due = []
        for i, (s, inj) in enumerate(zip(self.injection_steps, self.plan.injections)):
            if not self._injected[i] and s <= step + 1:
                self._injected[i] = True
                due.append((i, inj))
        return due
