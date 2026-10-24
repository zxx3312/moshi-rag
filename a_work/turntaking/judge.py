"""Judge API: label each answer unit against the evidence visible right now.

    judge(obs) -> {unit_id: UnitJudgment(label, citations)}

Three planned implementations: OracleJudge (gold support sets, done),
PromptJudge (LLM prompt, done), and a LoRA SFT judge (W3).
"""
from __future__ import annotations

import json
from typing import Dict, Iterable, List, Mapping, Protocol

from .schema import (
    CONTRADICTED, FULLY_SUFFICIENT, INSUFFICIENT, LABELS, PARTIALLY_SUFFICIENT, SUPPORTED,
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
                out[unit["unit_id"]] = UnitJudgment(SUPPORTED, tuple(complete[0]), unit.get("expected_answer"))
            else:
                out[unit["unit_id"]] = UnitJudgment(UNRESOLVED)
        return out


JUDGE_SYSTEM = """You check which answer units are supported by the evidence a voice assistant has received so far.

For every unit give one label:
- SUPPORTED: the evidence explicitly states the unit's value. Give the value and the ids of the evidence sentences that state it.
  No inference: "an Italian film directed by X" does not say where X was born.
  One exception: if a sentence is the defining description of an entity (e.g. "Y is an American film director and
  producer.") and the unit asks whether the entity has a property of a kind such a description lists (occupation,
  nationality, category), a property it does not list counts as "no". Label SUPPORTED with by_omission true.
  Negations that need outside knowledge (e.g. "Minnesota is not in Europe") stay UNRESOLVED.
  A unit cannot be SUPPORTED unless every unit in its depends_on is SUPPORTED.
  A conclusion unit (comparison, yes/no) is SUPPORTED when all its depends_on units are SUPPORTED; derive it from their values and cite their evidence.
- CONTRADICTED: two evidence sentences give conflicting values for the same unit (e.g. one says born 1950, another 1952).
  A yes/no unit whose answer is "no" is NOT contradicted: label it SUPPORTED with value "no".
- UNRESOLVED: anything else. Use value null and no citations.

Citations are evidence ids such as e1, never unit ids. A conclusion unit cites the evidence of the units it depends on.

{u1} in a description means the value of unit u1.
Use only the listed evidence, never your own knowledge. Reply with JSON only."""

JUDGE_SCHEMA = {
    "type": "object",
    "properties": {"units": {"type": "array", "items": {
        "type": "object",
        "properties": {
            "unit_id": {"type": "string"},
            "label": {"type": "string", "enum": list(LABELS)},
            "value": {"type": ["string", "null"]},
            "citations": {"type": "array", "items": {"type": "string"}},
            "by_omission": {"type": "boolean"},
        },
        "required": ["unit_id", "label", "value", "citations", "by_omission"],
    }}},
    "required": ["units"],
}


def _judge_request(question: str, units: List[dict], evidence: List[tuple]) -> str:
    lines = "\n".join(f"[{eid}] {text}" for eid, text in evidence)
    return f"Question: {question}\n\nUnits:\n{json.dumps(units)}\n\nEvidence received so far:\n{lines}"


# Fictional worked example: a "no" conclusion is SUPPORTED, and a property missing from a
# defining description is SUPPORTED by_omission. No evaluation question is used.
EXAMPLE = (
    _judge_request(
        "Are Mara Lindqvist and Oskar Feld both painters?",
        [{"unit_id": "u1", "description": "whether Mara Lindqvist is a painter", "depends_on": []},
         {"unit_id": "u2", "description": "whether Oskar Feld is a painter", "depends_on": []},
         {"unit_id": "u3", "description": "whether both are painters", "depends_on": ["u1", "u2"]}],
        [("e1", "Mara Lindqvist is a Swedish painter and illustrator."),
         ("e2", "Oskar Feld is a Danish architect and furniture designer.")]),
    {"units": [
        {"unit_id": "u1", "label": "SUPPORTED", "value": "yes", "citations": ["e1"], "by_omission": False},
        {"unit_id": "u2", "label": "SUPPORTED", "value": "no", "citations": ["e2"], "by_omission": True},
        {"unit_id": "u3", "label": "SUPPORTED", "value": "no", "citations": ["e1", "e2"], "by_omission": False}]},
)


def judge_messages(obs: Observation) -> List[dict]:
    units = [{"unit_id": u.unit_id, "description": u.description, "depends_on": list(u.depends_on)}
             for u in obs.units]
    request = _judge_request(obs.question, units, [(e.evidence_id, e.text) for e in obs.evidence])
    return [{"role": "system", "content": JUDGE_SYSTEM},
            {"role": "user", "content": EXAMPLE[0]},
            {"role": "assistant", "content": json.dumps(EXAMPLE[1])},
            {"role": "user", "content": request}]


class PromptJudge:
    """LLM judge over (question, units, visible evidence).

    Labels only change when new evidence arrives, so each (sample, visible evidence) is judged
    once and cached. With no evidence every unit is UNRESOLVED and the model is not called.
    A SUPPORTED label whose citations are missing or not yet visible is downgraded to UNRESOLVED.
    A unit with dependencies may cite those units by id; such citations expand to their evidence.
    """
    name = "prompt"

    def __init__(self, client):
        self.client = client
        self._cache: Dict[tuple, Dict[str, UnitJudgment]] = {}
        self.log: List[dict] = []

    def judge(self, obs: Observation) -> Dict[str, UnitJudgment]:
        visible = tuple(e.evidence_id for e in obs.evidence)
        key = (obs.sample_id, visible, obs.units)
        if key in self._cache:
            return self._cache[key]
        if not visible:
            out = {u.unit_id: UnitJudgment(UNRESOLVED) for u in obs.units}
            self._cache[key] = out
            return out

        n_calls = len(self.client.calls)
        error, raw = None, {}
        try:
            raw = self.client.chat_json(judge_messages(obs), purpose="judge", schema=JUDGE_SCHEMA)
        except (ValueError, OSError) as e:  # unusable reply or endpoint failure: judge nothing as supported
            error = repr(e)
        replies = {r.get("unit_id"): r for r in raw.get("units", []) if isinstance(r, dict)}

        out, downgraded = {}, []
        for u in obs.units:  # in id order, so dependencies are processed first
            r = replies.get(u.unit_id, {})
            label = r.get("label") if r.get("label") in LABELS else UNRESOLVED
            cites = []
            for c in r.get("citations") or []:
                if c in u.depends_on and c in out:
                    cites += [x for x in out[c].citations if x not in cites]
                elif isinstance(c, str) and c not in cites:
                    cites.append(c)
            cites = tuple(cites)
            value = r.get("value") if isinstance(r.get("value"), str) else None
            if value is not None and value.strip().lower() in ("", "null", "none"):
                value = None
            if label == SUPPORTED and (any(c not in visible for c in cites) or (not cites and not u.depends_on)):
                downgraded.append(u.unit_id)
                label, cites, value = UNRESOLVED, (), None
            omission = label == SUPPORTED and r.get("by_omission") is True
            out[u.unit_id] = UnitJudgment(label, cites if label != UNRESOLVED else (), value, omission)
        self._cache[key] = out
        latency = sum(c.latency_s for c in self.client.calls[n_calls:])
        self.log.append({"sample_id": obs.sample_id, "time_s": obs.time_s, "evidence": list(visible),
                         "latency_s": round(latency, 3), "error": error, "downgraded": downgraded,
                         "labels": {k: v.label for k, v in out.items()}, "reply": raw})
        return out


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
