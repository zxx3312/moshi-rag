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

    def latency_s(self, obs: Observation) -> float:
        """Measured time of the judgment for this observation; charged to the simulated clock."""
        ...


class OracleJudge:
    """Upper bound: a unit is SUPPORTED once any gold support set is fully visible.

    This is the explicitly separate oracle input path required by B's schema;
    gold never reaches the policy except through these labels. Gold has no
    contradiction annotations, so this judge never returns CONTRADICTED.
    """
    name = "oracle"

    def __init__(self, gold_records: Iterable[Mapping]):
        self._gold = {r["sample_id"]: r["units"] for r in gold_records}

    def latency_s(self, obs: Observation) -> float:
        return 0.0

    def judge(self, obs: Observation) -> Dict[str, UnitJudgment]:
        """Same rule as the SFT targets (b_work/step4/build_sft.py): a support set needs every dependency,
        a presupposition set at least one; a [[]] conclusion cites its dependencies' evidence."""
        visible = {e.evidence_id for e in obs.evidence}
        units = {u["unit_id"]: u for u in self._gold[obs.sample_id]}
        out: Dict[str, UnitJudgment] = {}

        def visit(uid: str) -> UnitJudgment:
            if uid not in out:
                unit = units[uid]
                parents = [visit(d) for d in unit["depends_on"]]
                ok = [p.label == SUPPORTED for p in parents]
                complete = [s for s in unit["support_sets"] if set(s) <= visible]
                presupposed = [s for s in unit.get("presupposition_sets", []) if set(s) <= visible]
                if complete and all(ok):
                    cites = complete[0] or [c for p in parents for c in p.citations]
                    out[uid] = UnitJudgment(SUPPORTED, tuple(dict.fromkeys(cites)), unit.get("expected_answer"),
                                            unit.get("by_omission", False))
                elif presupposed and (any(ok) or not ok):
                    out[uid] = UnitJudgment(SUPPORTED, tuple(presupposed[0]), unit.get("expected_answer"),
                                            by_presupposition=True)
                else:
                    out[uid] = UnitJudgment(UNRESOLVED)
            return out[uid]

        for uid in units:
            visit(uid)
        return out


JUDGE_SYSTEM = """You check which answer units are supported by the evidence a voice assistant has received so far.

For every unit give one label:
- SUPPORTED: the evidence explicitly states the unit's value. Give the value and the ids of the evidence sentences that state it.
  No inference: "an Italian film directed by X" does not say where X was born.
  A sentence about one member does not support a claim about its whole category: "Tervia montana (a species)
  is in family F" does not say which family the genus Tervia is in.
  One exception: if a sentence is the defining description of an entity (e.g. "Y is an American film director and
  producer.") and the unit asks whether the entity has a property of a kind such a description lists (occupation,
  nationality, category), a property it does not list counts as "no". Label SUPPORTED with by_omission true.
  Negations that need outside knowledge (e.g. "Minnesota is not in Europe") stay UNRESOLVED.
  Second exception: what the question itself takes as given counts. If it names the candidates ("which of A and B",
  "X, Y and which Z") then evidence confirming one candidate, or listing a group from which the question has named
  all but one, identifies the answer. Label SUPPORTED with by_presupposition true. This does not apply to comparing
  values such as dates, to "both" or "same" questions, or to any fact the question does not state.
  A unit cannot be SUPPORTED unless every unit in its depends_on is SUPPORTED.
  A conclusion unit (comparison, yes/no) is SUPPORTED when all its depends_on units are SUPPORTED; derive it from their values and cite their evidence.
- CONTRADICTED: two evidence sentences give conflicting values for the same unit (e.g. one says born 1950, another 1952).
  A yes/no unit whose answer is "no" is NOT contradicted: label it SUPPORTED with value "no".
- UNRESOLVED: anything else. Use value null and no citations.

Citations are evidence ids such as e1, never unit ids. A conclusion unit cites the evidence of the units it depends on.

{u1} in a description means the value of unit u1.
Each evidence sentence is shown with its document title in parentheses; a pronoun such as "he" or "the team" refers to the title's subject.
Use only the listed evidence, never your own knowledge. Reply with JSON only.
  For exactly two named candidates where the question presupposes one unique answer, evidence explicitly ruling out one candidate also identifies the other. Label the conclusion SUPPORTED with by_presupposition true."""

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
            "by_presupposition": {"type": "boolean"},
        },
        "required": ["unit_id", "label", "value", "citations", "by_omission", "by_presupposition"],
    }}},
    "required": ["units"],
}


def _judge_request(question: str, units: List[dict], evidence: List[tuple]) -> str:
    """evidence: (id, document title or None, text). The title tells the judge who "he" / "the team" is."""
    lines = "\n".join(f"[{eid}] ({title}) {text}" if title else f"[{eid}] {text}" for eid, title, text in evidence)
    return f"Question: {question}\n\nUnits:\n{json.dumps(units)}\n\nEvidence received so far:\n{lines}"


def _reply(*units) -> dict:
    keys = ("unit_id", "label", "value", "citations", "by_omission", "by_presupposition")
    return {"units": [dict(zip(keys, u)) for u in units]}


# Fictional worked examples; no evaluation question is used. (1) A "no" conclusion is SUPPORTED and a
# property missing from a defining description is by_omission. (2, 3) by_presupposition: choosing
# between named candidates, and eliminating the group members the question names.
EXAMPLES = [(
    _judge_request(
        "Are Mara Lindqvist and Oskar Feld both painters?",
        [{"unit_id": "u1", "description": "whether Mara Lindqvist is a painter", "depends_on": []},
         {"unit_id": "u2", "description": "whether Oskar Feld is a painter", "depends_on": []},
         {"unit_id": "u3", "description": "whether both are painters", "depends_on": ["u1", "u2"]}],
        [("e1", "Mara Lindqvist", "She is a Swedish painter and illustrator."),
         ("e2", "Oskar Feld", "Oskar Feld is a Danish architect and furniture designer.")]),
    _reply(("u1", "SUPPORTED", "yes", ["e1"], False, False),
           ("u2", "SUPPORTED", "no", ["e2"], True, False),
           ("u3", "SUPPORTED", "no", ["e1", "e2"], False, False)),
), (
    _judge_request(
        "In between Ilse Varga and Tomas Reed, who won the Halden Prize?",
        [{"unit_id": "u1", "description": "whether Ilse Varga won the Halden Prize", "depends_on": []},
         {"unit_id": "u2", "description": "whether Tomas Reed won the Halden Prize", "depends_on": []},
         {"unit_id": "u3", "description": "which of them won the Halden Prize", "depends_on": ["u1", "u2"]}],
        [("e1", "Tomas Reed", "In 1980 he won the Halden Prize."),
         ("e2", "Ilse Varga", "Ilse Varga is a Hungarian poet.")]),
    _reply(("u1", "UNRESOLVED", None, [], False, False),
           ("u2", "SUPPORTED", "yes", ["e1"], False, False),
           ("u3", "SUPPORTED", "Tomas Reed", ["e1"], False, True)),
), (
    _judge_request(
        "The Lark Theatre was founded by Anna Bell, Piotr Nowak, and which actor known as \"The Voice\"?",
        [{"unit_id": "u1", "description": "third founder of the Lark Theatre", "depends_on": []},
         {"unit_id": "u2", "description": "founder known as \"The Voice\", given {u1}", "depends_on": ["u1"]}],
        [("e1", "Lark Theatre", "It was founded by the actors Anna Bell, Piotr Nowak and Rui Costa.")]),
    _reply(("u1", "SUPPORTED", "Rui Costa", ["e1"], False, False),
           ("u2", "SUPPORTED", "Rui Costa", ["e1"], False, True)),
)]


def judge_messages(obs: Observation, with_examples: bool = True) -> List[dict]:
    units = [{"unit_id": u.unit_id, "description": u.description, "depends_on": list(u.depends_on)}
             for u in obs.units]
    request = _judge_request(obs.question, units,
                             [(e.evidence_id, (e.source or {}).get("document_id"), e.text) for e in obs.evidence])
    messages = [{"role": "system", "content": JUDGE_SYSTEM}]
    for example_request, example_reply in EXAMPLES if with_examples else ():
        messages += [{"role": "user", "content": example_request},
                     {"role": "assistant", "content": json.dumps(example_reply)}]
    return messages + [{"role": "user", "content": request}]


class PromptJudge:
    """LLM judge over (question, units, visible evidence).

    Labels only change when new evidence arrives, so each (sample, visible evidence) is judged
    once and cached. With no evidence every unit is UNRESOLVED and the model is not called.
    A SUPPORTED label whose citations are missing or not yet visible is downgraded to UNRESOLVED.
    A unit with dependencies may cite those units by id; such citations expand to their evidence.
    A conclusion unit (two or more dependencies: comparisons, "both"/"same" questions) gets its label
    from its dependencies, not from the model: SUPPORTED when all are SUPPORTED, CONTRADICTED when any
    is CONTRADICTED, else UNRESOLVED. The model still provides the value ("no", "Mark Gurr"). One shortcut:
    derive_conclusion accepts a by_presupposition choice between candidates the question names.
    """
    def __init__(self, client, with_examples: bool = True, name: str = "prompt"):
        """A trained LoRA judge uses the same class with its adapter's client and with_examples=False."""
        self.client = client
        self.with_examples = with_examples
        self.name = name
        self._cache: Dict[tuple, Dict[str, UnitJudgment]] = {}
        self._latency: Dict[tuple, float] = {}
        self.log: List[dict] = []

    @staticmethod
    def _key(obs: Observation) -> tuple:
        return obs.sample_id, tuple(e.evidence_id for e in obs.evidence), obs.units

    def latency_s(self, obs: Observation) -> float:
        """Latency of the real model call, also when the result now comes from the cache: a replay
        of another delay schedule would have had to wait for that call too."""
        return self._latency.get(self._key(obs), 0.0)

    def judge(self, obs: Observation) -> Dict[str, UnitJudgment]:
        visible = tuple(e.evidence_id for e in obs.evidence)
        key = self._key(obs)
        if key in self._cache:
            return self._cache[key]
        if not visible:
            out = {u.unit_id: UnitJudgment(UNRESOLVED) for u in obs.units}
            self._cache[key] = out
            return out

        n_calls = len(self.client.calls)
        error, raw = None, {}
        try:
            raw = self.client.chat_json(judge_messages(obs, self.with_examples), purpose="judge", schema=JUDGE_SCHEMA)
        except (ValueError, OSError) as e:  # unusable reply or endpoint failure: judge nothing as supported
            error = repr(e)
        out, downgraded = normalize_reply(raw, obs.units, visible, obs.question)
        self._cache[key] = out
        latency = sum(c.latency_s for c in self.client.calls[n_calls:])
        self._latency[key] = latency
        self.log.append({"sample_id": obs.sample_id, "time_s": obs.time_s, "evidence": list(visible),
                         "latency_s": round(latency, 3), "error": error, "downgraded": downgraded,
                         "labels": {k: v.label for k, v in out.items()}, "reply": raw})
        return out


def normalize_reply(raw: Mapping, units: Iterable[Unit], visible: Iterable[str], question: str):
    """Validate one model reply: ({unit_id: UnitJudgment}, ids downgraded for invalid citations)."""
    visible = set(visible)
    replies = {r.get("unit_id"): r for r in raw.get("units", []) if isinstance(r, dict)}
    out, downgraded = {}, []
    for u in units:  # in id order, so dependencies are processed first
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
        presupposed = r.get("by_presupposition") is True
        if is_conclusion(u):
            label, cites, presupposed = derive_conclusion(u, out, value, presupposed, question)
            value = value if label == SUPPORTED else None
        elif label == SUPPORTED and (any(c not in visible for c in cites) or (not cites and not u.depends_on)):
            downgraded.append(u.unit_id)
            label, cites, value = UNRESOLVED, (), None
        supported = label == SUPPORTED
        out[u.unit_id] = UnitJudgment(label, cites if label != UNRESOLVED else (), value,
                                      supported and r.get("by_omission") is True, supported and presupposed)
    return out, downgraded


def is_conclusion(unit: Unit) -> bool:
    """Bridge hops depend on one unit; conclusions combine two or more (unit_schema.md 3.3, 3.4)."""
    return len(unit.depends_on) >= 2


def derive_conclusion(unit: Unit, labels: Mapping[str, UnitJudgment], value, claims_presupposition: bool, question: str):
    """(label, citations, by_presupposition) of a conclusion unit from its dependencies' labels.

    With only some dependencies SUPPORTED the conclusion normally stays open. The exception needs the model's
    by_presupposition claim and two structural checks, so comparisons of values (dates) and "both" questions
    cannot pass: a dependency settled as "yes" (or "no", which rules out one of exactly two candidates), and
    a value that is a candidate named in the question.
    """
    deps = [labels.get(d, UnitJudgment(UNRESOLVED)) for d in unit.depends_on]

    def citations(items):
        cites = []
        for d in items:
            cites += [c for c in d.citations if c not in cites]
        return tuple(cites)

    if any(d.label == CONTRADICTED for d in deps):
        return CONTRADICTED, (), False
    if all(d.label == SUPPORTED for d in deps):
        return SUPPORTED, citations(deps), False
    accepted = ("yes", "no") if len(deps) == 2 else ("yes",)
    confirmed = [d for d in deps if d.label == SUPPORTED and (d.value or "").strip().lower() in accepted]
    answer = (value or "").strip().lower()
    if claims_presupposition and confirmed and answer not in ("", "yes", "no") and answer in question.lower():
        return SUPPORTED, citations(confirmed), True
    return UNRESOLVED, (), False


def resolve_dependencies(units: Iterable[Unit], raw: Mapping[str, UnitJudgment]) -> Dict[str, UnitJudgment]:
    """A unit counts as SUPPORTED only if every unit it depends on is SUPPORTED too
    (for a by_presupposition unit, at least one: the question stands in for the rest)."""
    by_id = {u.unit_id: u for u in units}
    resolved: Dict[str, UnitJudgment] = {}

    def visit(uid: str) -> UnitJudgment:
        if uid not in resolved:
            own = raw.get(uid, UnitJudgment(UNRESOLVED))
            deps = [visit(d).label == SUPPORTED for d in by_id[uid].depends_on]
            deps_ok = all(deps) or (own.by_presupposition and any(deps))
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
