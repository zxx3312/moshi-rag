"""Turn a progressive-evidence trace into a MoshiRAG control plan for each condition.

All times are seconds after the question ends. At every evidence arrival the model
receives the concatenation of all evidence visible so far (one reference per injection).

v1 (text-only control, full_v1):
  free      no text control; evidence injected on schedule            (MoshiRAG as is)
  wait      PAD text until the last evidence arrives, then free       (Wait-All)
  progress  text-forces PROGRESS_PHRASE, PAD until the last evidence  (Fixed Progress)
  notready  no text control; a "not ready" reference at t=0, then evidence
  ours      PROGRESS_PHRASE; one utterance per earlier arrival; free once the last arrives

v2 (quiet modes also silence the audio tokens; clips replay the model's own recorded speech):
  wait_av        silent (text + audio) until the last evidence, then free
  wait_av_kick   as wait_av, but release with the "oh" clip
  progress_clip  "look_it_up" clip, silent until the last evidence, release with "oh"
  progress_inj   "not ready" reference; one utterance, then silent; release with "oh"
  ours_v2        "look_it_up"; at each earlier arrival "oh" + one utterance, then silent;
                 release with "oh" once the last evidence arrives
  ours_v3        as ours_v2, but every injection also states what is still missing (the
                 units' `pending` sentences) and the last one adds SEARCH_COMPLETE_TEXT
"""
from __future__ import annotations

from typing import List, Mapping, Sequence

from control import CLIP, FREE, SAY, SILENCE, SPEAK_ONCE, Injection, Plan, Segment

PROGRESS_PHRASE = "Let me look that up."
NOT_READY_TEXT = "The search is still running. No information about this question is available yet."
SEARCH_COMPLETE_TEXT = "The search is complete."
PROGRESS_CLIP, RELEASE_CLIP = "look_it_up", "oh"
CLIPS = (PROGRESS_CLIP, RELEASE_CLIP)

CONDITIONS_V1 = ("free", "wait", "progress", "notready", "ours")
CONDITIONS_V2 = ("wait_av", "wait_av_kick", "progress_clip", "progress_inj", "ours_v2", "ours_v3")
CONDITIONS = CONDITIONS_V1 + CONDITIONS_V2
MULTI_EVIDENCE_ONLY = ("ours", "ours_v2", "ours_v3")


def evidence_injections(events: Sequence[Mapping], units: Sequence[Mapping] = (),
                        status_notes: bool = False) -> List[Injection]:
    """One cumulative reference per arrival. With status_notes, append the `pending` sentence of
    every unit whose support is not yet complete, and SEARCH_COMPLETE_TEXT to the last reference."""
    events = sorted(events, key=lambda e: e["visible_time_s"])
    out, seen = [], []
    for k, e in enumerate(events):
        seen.append(e)
        parts = [x["text"] for x in seen]
        if status_notes:
            ids = {x["evidence_id"] for x in seen}
            parts += [u["pending"] for u in units if u.get("pending") and not set(u["support"]) <= ids]
            if k == len(events) - 1:
                parts.append(SEARCH_COMPLETE_TEXT)
        out.append(Injection(
            time_s=float(e["visible_time_s"]),
            text=" ".join(parts),
            label="+".join(x["evidence_id"] for x in seen) + ("+notes" if status_notes else ""),
        ))
    return out


def build_plan(condition: str, events: Sequence[Mapping], units: Sequence[Mapping] = ()) -> Plan:
    injections = evidence_injections(events, units, status_notes=condition == "ours_v3")
    if not injections:
        raise ValueError("trace has no evidence events")
    times = [i.time_s for i in injections]
    last = times[-1]
    release = Segment(last, CLIP, clip=RELEASE_CLIP, after=FREE)
    mute = condition in CONDITIONS_V2

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
    elif condition == "wait_av":
        segments = [Segment(0.0, SILENCE), Segment(last, FREE)]
    elif condition == "wait_av_kick":
        segments = [Segment(0.0, SILENCE), release]
    elif condition == "progress_clip":
        segments = [Segment(0.0, CLIP, clip=PROGRESS_CLIP, after=SILENCE), release]
    elif condition == "progress_inj":
        segments = [Segment(0.0, SPEAK_ONCE), release]
        injections = [Injection(0.0, NOT_READY_TEXT, "not_ready")] + injections
    elif condition in ("ours_v2", "ours_v3"):
        segments = [Segment(0.0, CLIP, clip=PROGRESS_CLIP, after=SILENCE)]
        segments += [Segment(t, CLIP, clip=RELEASE_CLIP, after=SPEAK_ONCE) for t in times[:-1]]
        segments.append(release)
    else:
        raise ValueError(f"unknown condition {condition!r}; expected one of {CONDITIONS}")
    return Plan(condition, tuple(segments), tuple(injections), mute_audio=mute)
