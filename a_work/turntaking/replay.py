"""Text-level trace replay: step a simulated clock, show each policy only the
evidence visible so far, and write one policy_log record per non-Wait action.

Open questions for B (kept as parameters until agreed):
  * decision_cost_s: how much simulated time a judge/LLM call consumes (pending).
  * Wait ticks are not logged; only actions that produce output are.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List, Mapping, Optional

from .policies import Policy
from .schema import (
    BACKCHANNEL, FINAL, PARTIAL, PROGRESS, SCHEMA_VERSION, WAIT,
    Decision, Evidence, Observation, Unit,
)

# Simulated speaking time per output piece; placeholder until a TTS-based cost model exists.
SHORT_UTTERANCE_S = 1.0
CLAIM_S = 2.0

FIXED_TEXT = {
    BACKCHANNEL: "Mm, let me check.",
    PROGRESS: "I'm still looking that up.",
}


def load_jsonl(path) -> List[dict]:
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def write_jsonl(path, records: Iterable[Mapping]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def units_without_gold(gold_record: Mapping) -> List[Unit]:
    """Strip answers and support sets from gold units. Only valid for oracle runs;
    ordinary runs must decompose the question themselves."""
    return [
        Unit(u["unit_id"], u["description"], u["necessary"], tuple(u["depends_on"]))
        for u in gold_record["units"]
    ]


def _parse_events(trace: Mapping) -> List[Evidence]:
    events = [
        Evidence(e["evidence_id"], e["text"], float(e["visible_time_s"]), e["source"])
        for e in trace["events"]
    ]
    return sorted(events, key=lambda e: e.visible_time_s)


def _render(decision: Decision, units: Mapping[str, Unit]):
    """Placeholder generator: brackets mark where an LLM would phrase each claim.

    Returns (text, duration_s, claim_spans relative to output start).
    """
    if decision.action in FIXED_TEXT:
        return FIXED_TEXT[decision.action], SHORT_UTTERANCE_S, []
    pieces, spans, offset = [], [], 0.0
    for uid in decision.claimed_units:
        cites = list(decision.citations.get(uid, ()))
        piece = f"[{uid}: {units[uid].description} <- {','.join(cites) or 'no evidence'}]"
        pieces.append(piece)
        spans.append({
            "text": piece, "controller_unit_id": uid, "cited_evidence_ids": cites,
            "start": offset, "end": offset + CLAIM_S,
        })
        offset += CLAIM_S
    if decision.action == PARTIAL:
        pieces.append("I'm still checking the rest.")
        offset += SHORT_UTTERANCE_S
    elif not pieces:
        pieces.append("That's all I could confirm.")
        offset += SHORT_UTTERANCE_S
    return " ".join(pieces), offset, spans


def replay(
    trace: Mapping,
    units: List[Unit],
    policy: Policy,
    *,
    tick_s: float = 0.5,
    decision_cost_s: float = 0.0,
    max_extra_s: float = 5.0,
    seed: int = 0,
) -> List[dict]:
    events = _parse_events(trace)
    complete: Optional[float] = trace.get("retrieval_complete_time_s")
    if complete is None and events:
        complete = events[-1].visible_time_s
    end_t = (complete or 0.0) + max_extra_s
    unit_map = {u.unit_id: u for u in units}
    run_id = f"{trace['trace_id']}__{policy.name}__s{seed}"

    policy.reset()
    records, busy_until, step = [], float("-inf"), 0
    t = 0.0
    while t <= end_t:
        if t >= busy_until:
            visible = tuple(e for e in events if e.visible_time_s <= t)
            obs = Observation(
                sample_id=trace["sample_id"], question=trace["question"], time_s=t,
                evidence=visible, units=tuple(units),
                retrieval_done=complete is not None and t >= complete,
            )
            decision = policy.decide(obs)
            if decision.action != WAIT:
                text, duration, spans = _render(decision, unit_map)
                start = t + decision_cost_s
                for s in spans:
                    s["start"] += start
                    s["end"] += start
                records.append({
                    "schema_version": SCHEMA_VERSION,
                    "data_version": trace["data_version"],
                    "sample_id": trace["sample_id"],
                    "trace_id": trace["trace_id"],
                    "run_id": run_id,
                    "policy": policy.name,
                    "seed": seed,
                    "time_origin": trace["time_origin"],
                    "clock": trace["clock"],
                    "decision_time_s": t,
                    "action": decision.action,
                    "text": text,
                    "evidence_snapshot_ids": [e.evidence_id for e in visible],
                    "output_start_time_s": start,
                    "output_end_time_s": start + duration,
                    "claim_spans": spans,
                    "status": "ok",
                    "unit_labels": decision.unit_labels,
                })
                busy_until = start + duration
                if decision.action == FINAL:
                    break
        step += 1
        t = round(step * tick_s, 6)
    return records
