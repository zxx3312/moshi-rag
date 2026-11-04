"""Rough self-check metrics for A's debugging only; B's evaluator is authoritative.

Claims map to gold units by controller_unit_id, which only holds when the controller units were
copied from gold. With by_value the claim maps by its value instead, for decomposed units. That is
rough: a yes/no value can match several gold units, and a correct value for an intermediate step
gold does not list counts as unsupported.
"""
from __future__ import annotations

import re
from typing import Dict, List, Mapping, Optional, Sequence


def norm(text: Optional[str]) -> str:
    return re.sub(r"[^a-z0-9 ]", "", (text or "").lower()).strip()


def value_match(pred: Optional[str], answers: Sequence[str]) -> bool:
    """Whole-word containment either way, so "no" does not match "Norman"."""
    p = f" {norm(pred)} "
    return p.strip() != "" and any(a and (f" {a} " in p or p in f" {a} ") for a in map(norm, answers))


def answers_of(unit: Mapping) -> List[str]:
    return [unit["expected_answer"]] + list(unit.get("aliases", []))


def _visible_ids(trace: Mapping, t: float) -> set:
    return {e["evidence_id"] for e in trace["events"] if e["visible_time_s"] <= t}


def supported_units(gold_units: Mapping[str, Mapping], visible: set) -> set:
    """Gold units supported by this evidence, with dependencies: a [[]] conclusion needs its units."""
    memo: Dict[str, bool] = {}

    def supported(uid: str) -> bool:
        if uid not in memo:
            unit = gold_units[uid]
            deps = [supported(d) for d in unit["depends_on"]]
            deps_ok = all(deps) or (unit.get("by_presupposition", False) and any(deps))
            memo[uid] = deps_ok and any(set(s) <= visible for s in unit["support_sets"])
        return memo[uid]

    return {uid for uid in gold_units if supported(uid)}


def claimed_gold_units(claim: Mapping, gold_units: Mapping[str, Mapping], by_value: bool = False) -> List[str]:
    if by_value:
        return [uid for uid, u in gold_units.items() if value_match(claim.get("value"), answers_of(u))]
    uid = claim["controller_unit_id"]
    if uid not in gold_units:
        return []
    value = claim.get("value")
    return [uid] if value is None or value_match(value, answers_of(gold_units[uid])) else []


def supported_claim_units(claim: Mapping, gold_units: Mapping[str, Mapping], trace: Mapping,
                          by_value: bool = False) -> List[str]:
    """Gold units this claim states correctly, with their support visible when it was spoken."""
    ok = supported_units(gold_units, _visible_ids(trace, claim["start"]))
    return [uid for uid in claimed_gold_units(claim, gold_units, by_value) if uid in ok]


def claim_supported(claim: Mapping, gold_units: Mapping[str, Mapping], trace: Mapping, by_value: bool = False) -> bool:
    return bool(supported_claim_units(claim, gold_units, trace, by_value))


def preview_metrics(records: List[Mapping], trace: Mapping, gold: Mapping, by_value: bool = False) -> Dict[str, Optional[float]]:
    gold_units = {u["unit_id"]: u for u in gold["units"]}
    claims = [c for r in records for c in r["claim_spans"]]
    first_ok_end: Dict[str, float] = {}
    starts, unsupported = [], 0
    for c in claims:
        units = supported_claim_units(c, gold_units, trace, by_value)
        if not units:
            unsupported += 1
            continue
        starts.append(c["start"])
        for uid in units:
            first_ok_end.setdefault(uid, c["end"])

    necessary = {uid for uid, u in gold_units.items() if u["necessary"]}
    complete = necessary <= first_ok_end.keys()
    return {
        "ttfr": records[0]["output_start_time_s"] if records else None,
        "ttfgi": min(starts, default=None),
        "ttca": max(first_ok_end[u] for u in necessary) if complete else None,
        "claims": len(claims),
        "unsupported": unsupported,
        "judge_cost_s": sum(r.get("decision_cost_s", 0.0) for r in records),
        "generation_cost_s": sum(r.get("generation_cost_s", 0.0) for r in records),
        "value_not_in_text": sum(c.get("value_in_text") is False for c in claims),
    }
