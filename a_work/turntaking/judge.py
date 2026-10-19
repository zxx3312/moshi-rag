"""Judge API: label each answer unit against the evidence visible right now.

    judge(obs) -> {unit_id: UnitJudgment(label, citations)}

Three planned implementations: OracleJudge (gold support sets, done),
PromptJudge (LLM prompt, W2), and a LoRA SFT judge (W3).
"""
from __future__ import annotations

from typing import Dict, Iterable, Mapping, Protocol

from .schema import (
    CONTRADICTED, FULLY_SUFFICIENT, INSUFFICIENT, PARTIALLY_SUFFICIENT, SUPPORTED,
    UNRESOLVED, Observation, Unit, UnitJudgment,
)


class Judge(Protocol):
    name: str

    def judge(self, obs: Observation) -> Dict[str, UnitJudgment]: ...


class OracleJudge:
    """Upper bound: a unit is SUPPORTED once any gold support set is fully visible.

    This is the explicitly separate oracle input path required by B's schema;
    gold never reaches the policy except through these labels. Gold has no
    contradiction annotations, so this judge never returns CONTRADICTED.
    """
    name = "oracle"

    def __init__(self, gold_records: Iterable[Mapping]):
        self._gold = {r["sample_id"]: r["units"] for r in gold_records}

    def judge(self, obs: Observation) -> Dict[str, UnitJudgment]:
        visible = {e.evidence_id for e in obs.evidence}
        out = {}
        for unit in self._gold[obs.sample_id]:
            complete = [s for s in unit["support_sets"] if set(s) <= visible]
            if complete:
                out[unit["unit_id"]] = UnitJudgment(SUPPORTED, tuple(complete[0]))
            else:
                out[unit["unit_id"]] = UnitJudgment(UNRESOLVED)
        return out


class PromptJudge:
    """LLM judge over (question, units, visible evidence). To be implemented in W2."""
    name = "prompt"

    def judge(self, obs: Observation) -> Dict[str, UnitJudgment]:
        raise NotImplementedError("PromptJudge is planned for W2")


def resolve_dependencies(units: Iterable[Unit], raw: Mapping[str, UnitJudgment]) -> Dict[str, UnitJudgment]:
    """A unit counts as SUPPORTED only if every unit it depends on is SUPPORTED too."""
    by_id = {u.unit_id: u for u in units}
    resolved: Dict[str, UnitJudgment] = {}

    def visit(uid: str) -> UnitJudgment:
        if uid not in resolved:
            own = raw.get(uid, UnitJudgment(UNRESOLVED))
            deps_ok = all(visit(d).label == SUPPORTED for d in by_id[uid].depends_on)
            resolved[uid] = own if own.label != SUPPORTED or deps_ok else UnitJudgment(UNRESOLVED)
        return resolved[uid]

    for uid in by_id:
        visit(uid)
    return resolved


def sufficiency_state(units: Iterable[Unit], labels: Mapping[str, UnitJudgment]) -> str:
    units = list(units)
    if all(labels[u.unit_id].label == SUPPORTED for u in units if u.necessary):
        return FULLY_SUFFICIENT
    if any(labels[u.unit_id].label == SUPPORTED for u in units):
        return PARTIALLY_SUFFICIENT
    return INSUFFICIENT


__all__ = [
    "Judge", "OracleJudge", "PromptJudge", "resolve_dependencies", "sufficiency_state",
    "SUPPORTED", "UNRESOLVED", "CONTRADICTED",
]
