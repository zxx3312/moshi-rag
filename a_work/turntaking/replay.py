"""Text-level trace replay: step a simulated clock, show each policy only the
evidence visible so far, and write one policy_log record per non-Wait action.

The judge's measured latency (Decision.cost_s) is charged to the clock: output starts when the judge
returns, and no new decision is made before that. Decomposition time (setup_cost_s) delays the first
judgment. Fixed costs stay parameters until agreed with B (decision_cost_s).
With a generator, every utterance is timed by the TTS (cascade.py): its latency delays the output and its
audio sets how long the agent speaks. With an ASR result, nothing that needs the question starts before
the transcript is ready.
Wait ticks are not logged; only actions that produce output are (open question for B).
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Optional

from .cascade import Heard, RateTTS, Speech
from .generate import find_value
from .policies import Policy
from .schema import (
    BACKCHANNEL, FINAL, PARTIAL, PROGRESS, SCHEMA_VERSION, SUPPORTED, WAIT,
    Decision, Evidence, Observation, Unit,
)

# Speaking time of the bracket placeholders, used only without a generator.
SHORT_UTTERANCE_S = 1.0
CLAIM_S = 2.0

# Fixed utterances are rendered ahead of time, so they cost no TTS latency.
FIXED_TEXT = {
    BACKCHANNEL: "Let me check.",
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
        value = decision.values.get(uid)
        said = f" = {value}" if value else ""
        piece = f"[{uid}: {units[uid].description}{said} <- {','.join(cites) or 'no evidence'}]"
        pieces.append(piece)
        spans.append({
            "text": piece, "controller_unit_id": uid, "value": value, "cited_evidence_ids": cites,
            "start": offset, "end": offset + CLAIM_S,
        })
        offset += CLAIM_S
    if not pieces:
        pieces.append("That's all I could confirm.")
        offset += SHORT_UTTERANCE_S
    return " ".join(pieces), offset, spans


def _value_span(text: str, value: Optional[str], speech: Speech) -> tuple:
    """(start, end, found): the part of the utterance that says the value. A value the text does not
    contain is taken to span the whole utterance."""
    i = find_value(text, value)
    if i < 0:
        return 0.0, speech.duration_s, False
    return speech.time_at(i), speech.time_at(i + len(value)), True


def _spans(text: str, claims: List[dict], speech: Speech) -> List[dict]:
    spans = []
    for claim in claims:
        start, end, found = _value_span(text, claim["value"], speech)
        spans.append({"text": text, **claim, "start": start, "end": end, "value_in_text": found})
    return spans


def _generate(decision: Decision, obs: Observation, units: Mapping[str, Unit], generator, known: Dict[str, str]):
    """Real sentences instead of the placeholder. Returns (text, claims, latency_s); the claims have no
    times yet, those come from the speech."""
    evidence = {e.evidence_id: e for e in obs.evidence}

    def cited(ids):
        return [((evidence[i].source or {}).get("document_id"), evidence[i].text) for i in ids if i in evidence]

    if decision.free_answer:
        text, answers, latency = generator.free(obs.question, cited(list(evidence)))
        claims = [{"controller_unit_id": "answer", "value": answer, "cited_evidence_ids": list(evidence)}
                  for answer in answers]
        return text, claims, latency

    def describe(uid):
        d = units[uid].description
        for k, v in known.items():
            d = d.replace("{" + k + "}", v)
        return re.sub(r"\{\w+\}", "the earlier result", d)  # the model must never see a raw placeholder

    known.update({u: v for u, v in decision.values.items() if v})
    labels = decision.unit_labels or {}
    claimed = set(decision.claimed_units)
    missing = [describe(u) for u, unit in units.items()
               if u not in claimed and labels.get(u) != SUPPORTED and (unit.necessary or decision.action == PARTIAL)]
    say = [(describe(u), decision.values.get(u) or "") for u in decision.claimed_units]
    text, latency = generator.grounded(obs.question, say, missing, obs.retrieval_done)
    claims = [{"controller_unit_id": uid, "value": decision.values.get(uid),
               "cited_evidence_ids": list(decision.citations.get(uid, ()))} for uid in decision.claimed_units]
    return text, claims, latency


def replay(
    trace: Mapping,
    units: List[Unit],
    policy: Policy,
    *,
    tick_s: float = 0.5,
    decision_cost_s: float = 0.0,
    setup_cost_s: float = 0.0,
    max_extra_s: float = 5.0,
    seed: int = 0,
    generator=None,
    concurrent: bool = False,
    tts=None,
    heard: Optional[Heard] = None,
) -> List[dict]:
    """With concurrent, judging and generation keep running while the agent speaks, from the moment their
    inputs exist, so the next utterance can start as soon as the current one ends. Otherwise they start at the
    first decision after it ends. Models that share a server may slow each other; that is not simulated.

    tts times the utterances a generator writes (default: RateTTS). heard is the ASR result for the question
    (default: the trace's own text, ready when the question ends)."""
    tts = tts or RateTTS()
    question, question_ready_s = (heard.text, heard.latency_s) if heard else (trace["question"], 0.0)
    setup_cost_s += question_ready_s  # the question cannot be split into units before it has been heard
    events = _parse_events(trace)
    complete: Optional[float] = trace.get("retrieval_complete_time_s")
    if complete is None and events:
        complete = events[-1].visible_time_s
    end_t = (complete or 0.0) + max_extra_s
    unit_map = {u.unit_id: u for u in units}
    run_id = f"{trace['trace_id']}__{policy.name}__s{seed}"

    policy.reset()
    records, busy_until, step = [], float("-inf"), 0
    speaking_until, work_from = None, 0.0  # work_from: when the model finished its last utterance
    known: Dict[str, str] = {}
    t = 0.0
    while t <= max(end_t, busy_until + tick_s):  # an utterance past the horizon still gets its next decision
        if t >= busy_until:
            visible = tuple(e for e in events if e.visible_time_s <= t)
            obs = Observation(
                sample_id=trace["sample_id"], question=question, time_s=t,
                evidence=visible, units=tuple(units),
                retrieval_done=complete is not None and t >= complete,
                units_ready=t >= setup_cost_s,
            )
            decision = policy.decide(obs)
            cost = decision_cost_s + decision.cost_s
            decided, earliest = t, t
            if concurrent and speaking_until is not None:
                inputs = [work_from, setup_cost_s]
                inputs += [visible[-1].visible_time_s] if visible else []
                inputs += [complete] if obs.retrieval_done else []
                decided, earliest = max(inputs), speaking_until
            if decision.action == WAIT:
                busy_until = max(t, decided + cost)  # still thinking: no new decision before the judge returns
                speaking_until = None
            else:
                generation_cost = tts_cost = 0.0
                if generator is None:
                    text, duration, spans = _render(decision, unit_map)
                else:
                    if decision.action in (PARTIAL, FINAL):
                        decided = max(decided, question_ready_s)  # a rule baseline needs the question too
                        text, claims, generation_cost = _generate(decision, obs, unit_map, generator, known)
                        speech = tts.synthesize(text)
                        tts_cost = speech.latency_s
                    else:
                        text, claims = FIXED_TEXT[decision.action], []
                        speech = tts.synthesize(text)
                    duration, spans = speech.duration_s, _spans(text, claims, speech)
                start = max(earliest, decided + cost + generation_cost + tts_cost)
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
                    "decision_time_s": decided,
                    "decision_cost_s": cost,
                    "generation_cost_s": generation_cost,
                    "tts_cost_s": tts_cost,
                    "action": decision.action,
                    "text": text,
                    "evidence_snapshot_ids": [e.evidence_id for e in visible],
                    "output_start_time_s": start,
                    "output_end_time_s": start + duration,
                    "claim_spans": spans,
                    "status": "ok",
                    "unit_labels": decision.unit_labels,
                })
                busy_until = speaking_until = start + duration
                work_from = start
                if decision.action == FINAL:
                    break
        step += 1
        t = round(step * tick_s, 6)
    return records
