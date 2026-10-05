"""Controlled retrieval backend: every request returns the same fixed reference.

The latency is expressed on the *model stream clock* (Mimi frames, 12.5 Hz),
not as a wall-clock ``sleep``. In MoshiRAG's offline harness
(``moshi.inference_utils.inference_job.InferenceJob``) the model is paused while
a retrieval is pending and the measured wall-clock latency is converted into a
number of model steps (``floor(elapsed * frame_rate)``). Specifying that step
count directly is what ``sleep(N)`` would emulate, but without polling jitter
and independent of GPU speed.

This module is pure stdlib so ``--dry-run`` can exercise it on a login node.
"""

from __future__ import annotations

import math
import time
from dataclasses import dataclass


def delay_to_steps(delay_s: float, frame_rate: float) -> int:
    """Convert a delay in seconds to whole model steps (round half up)."""
    if delay_s < 0 or not math.isfinite(delay_s):
        raise ValueError(f"retrieval delay must be a finite value >= 0, got {delay_s}")
    if frame_rate <= 0:
        raise ValueError(f"frame_rate must be > 0, got {frame_rate}")
    return int(math.floor(delay_s * frame_rate + 0.5))


@dataclass(frozen=True)
class RetrievalResult:
    reference_text: str
    delay_s: float
    # The reference becomes visible to the model this many steps after the request step.
    available_after_steps: int
    request_index: int
    # Wall-clock monotonic times, for profiling only (not conversational timing).
    wall_request_time: float
    wall_return_time: float
    context: str


class FixedReferenceBackend:
    """Returns ``reference_text`` for every request; latency is enforced by the caller in model steps."""

    def __init__(self, reference_text: str, delay_s: float, frame_rate: float):
        if not reference_text or not reference_text.strip():
            raise ValueError("fixed reference_text must be non-empty")
        self.reference_text = reference_text
        self.delay_s = float(delay_s)
        self.frame_rate = float(frame_rate)
        self.delay_steps = delay_to_steps(self.delay_s, self.frame_rate)
        self.requests: list[RetrievalResult] = []

    @property
    def effective_delay_s(self) -> float:
        return self.delay_steps / self.frame_rate

    async def retrieve(self, context: str) -> RetrievalResult:
        t0 = time.monotonic()
        result = RetrievalResult(
            reference_text=self.reference_text,
            delay_s=self.delay_s,
            available_after_steps=self.delay_steps,
            request_index=len(self.requests),
            wall_request_time=t0,
            wall_return_time=time.monotonic(),
            context=context,
        )
        self.requests.append(result)
        return result
