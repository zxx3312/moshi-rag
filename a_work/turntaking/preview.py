"""Rough self-check metrics for A's debugging only.

B's eval/ framework is the source of truth for reported numbers. This preview
maps claims to gold units by controller_unit_id, which only holds when the
controller units were copied from gold (oracle/demo runs).
"""
from __future__ import annotations

from typing import Dict, List, Mapping, Optional


def _visible_ids(trace: Mapping, t: float) -> set:
    return {e["evidence_id"] for e in trace["events"] if e["visible_time_s"] <= t}


def claim_supported(claim: Mapping, gold_units: Mapping[str, Mapping], trace: Mapping) -> bool:
    """A claim is supported if a gold support set was fully visible when it was spoken."""
    unit = gold_units.get(claim["controller_unit_id"])
    if unit is None:
        return False
    visible = _visible_ids(trace, claim["start"])
    return any(set(s) <= visible for s in unit["support_sets"])


def preview_metrics(records: List[Mapping], trace: Mapping, gold: Mapping) -> Dict[str, Optional[float]]:
    gold_units = {u["unit_id"]: u for u in gold["units"]}
    claims = [c for r in records for c in r["claim_spans"]]
    ok = [c for c in claims if claim_supported(c, gold_units, trace)]

    necessary = {uid for uid, u in gold_units.items() if u["necessary"]}
    first_ok_end: Dict[str, float] = {}
    for c in ok:
        first_ok_end.setdefault(c["controller_unit_id"], c["end"])
    complete = necessary <= first_ok_end.keys()

    return {
        "ttfr": records[0]["output_start_time_s"] if records else None,
        "ttfgi": min((c["start"] for c in ok), default=None),
        "ttca": max(first_ok_end[u] for u in necessary) if complete else None,
        "claims": len(claims),
        "unsupported": len(claims) - len(ok),
    }
