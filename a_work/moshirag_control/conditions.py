"""Turn a progressive-evidence trace into a MoshiRAG control plan for each condition.

All times are seconds after the question ends. At every evidence arrival the model
receives the concatenation of all evidence visible so far (one reference per injection).

  free      no text control; evidence injected on schedule            (MoshiRAG as is)
  wait      silent until the last evidence arrives, then free         (Wait-All)
  progress  says PROGRESS_PHRASE, silent until the last evidence      (Fixed Progress)
  notready  no text control; a "not ready" reference at t=0, then evidence
  ours      says PROGRESS_PHRASE; at each earlier arrival speaks one utterance
            and is held silent again; free once the last evidence is in
"""
from __future__ import annotations

from typing import List, Mapping, Sequence

from control import FREE, SAY, SILENCE, SPEAK_ONCE, Injection, Plan, Segment

PROGRESS_PHRASE = "Let me look that up."
NOT_READY_TEXT = "The search is still running. No information about this question is available yet."

CONDITIONS = ("free", "wait", "progress", "notready", "ours")


def evidence_injections(events: Sequence[Mapping]) -> List[Injection]:
    events = sorted(events, key=lambda e: e["visible_time_s"])
    out, seen = [], []
    for e in events:
        seen.append(e)
        out.append(Injection(
            time_s=float(e["visible_time_s"]),
            text=" ".join(x["text"] for x in seen),
            label="+".join(x["evidence_id"] for x in seen),
        ))
    return out


def build_plan(condition: str, events: Sequence[Mapping]) -> Plan:
    injections = evidence_injections(events)
    if not injections:
        raise ValueError("trace has no evidence events")
    times = [i.time_s for i in injections]
    last = times[-1]

    if condition == "free":
        segments = []
    elif condition == "wait":
        segments = [Segment(0.0, SILENCE), Segment(last, FREE)]
    elif condition == "progress":
        segments = [Segment(0.0, SAY, PROGRESS_PHRASE), Segment(last, FREE)]
    elif condition == "notready":
        segments = []
        injections = [Injection(0.0, NOT_READY_TEXT, "not_ready")] + injections
    elif condition == "ours":
        segments = [Segment(0.0, SAY, PROGRESS_PHRASE)]
        segments += [Segment(t, SPEAK_ONCE) for t in times[:-1]]
        segments.append(Segment(last, FREE))
    else:
        raise ValueError(f"unknown condition {condition!r}; expected one of {CONDITIONS}")
    return Plan(condition, tuple(segments), tuple(injections))
