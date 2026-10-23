"""Split a question into controller-side answer units (a_work/unit_schema.md, sec. 3).

The decomposer sees only the question: no evidence, no gold answers. Few-shot examples
are fictional so that no evaluation question leaks into the prompt.
"""
from __future__ import annotations

import json
from typing import List, Tuple

from .schema import Unit

QUESTION_TYPES = ("single", "bridge", "comparison", "bridge_comparison", "multipart")

SYSTEM = """You split a user's question into answer units for a voice assistant that answers while a search is still running.

An answer unit is the smallest piece of information needed to answer, small enough that one evidence sentence can state it.

Rules by question type:
- single: the question asks for one fact. One unit, necessary=true.
- bridge: the answer needs an intermediate entity first (e.g. "where was the director of film X born"). One unit per hop. The intermediate hop has necessary=false. The final hop has necessary=true and depends_on the intermediate hop; refer to the intermediate result as {u1} (its unit id in braces).
- comparison: two or more items are compared (who/which is older, same or different, both or not). One unit per item's fact with necessary=false, plus a final conclusion unit with necessary=true that depends_on all fact units.
- bridge_comparison: a comparison where each item first needs a bridge (e.g. "which film's director died later"). For each item: a bridge unit (necessary=false) and a fact unit that depends_on it (necessary=false). Then a conclusion unit (necessary=true) that depends_on the fact units.
- multipart: the question explicitly asks several things. One necessary unit per part, no dependencies.

Constraints:
- Never answer, guess or hint at any value. Descriptions say what to find, not what it is.
- Do not make a unit for an entity the question already names; units are things still to be found.
- Kinship beyond parents (grandfather, grandmother, uncle, ...) is a bridge: first the parent, then that parent's parent or sibling.
- Use 1 to 5 units with ids u1, u2, ... in order. depends_on may only list earlier units.
- Reply with JSON only."""

EXAMPLES: List[Tuple[str, dict]] = [
    ("What is the capital of Veloria?", {"question_type": "single", "units": [
        {"unit_id": "u1", "description": "capital of Veloria", "necessary": True, "depends_on": []}]}),
    ("Who founded the company that makes the Zephyr bicycle?", {"question_type": "bridge", "units": [
        {"unit_id": "u1", "description": "company that makes the Zephyr bicycle", "necessary": False, "depends_on": []},
        {"unit_id": "u2", "description": "founder of {u1}", "necessary": True, "depends_on": ["u1"]}]}),
    ("Which river is longer, the Arlen or the Meru?", {"question_type": "comparison", "units": [
        {"unit_id": "u1", "description": "length of the Arlen river", "necessary": False, "depends_on": []},
        {"unit_id": "u2", "description": "length of the Meru river", "necessary": False, "depends_on": []},
        {"unit_id": "u3", "description": "which river is longer", "necessary": True, "depends_on": ["u1", "u2"]}]}),
    ("Which novel's author was born first, Glass Harbor or The Quiet Field?", {"question_type": "bridge_comparison", "units": [
        {"unit_id": "u1", "description": "author of Glass Harbor", "necessary": False, "depends_on": []},
        {"unit_id": "u2", "description": "birth date of {u1}", "necessary": False, "depends_on": ["u1"]},
        {"unit_id": "u3", "description": "author of The Quiet Field", "necessary": False, "depends_on": []},
        {"unit_id": "u4", "description": "birth date of {u3}", "necessary": False, "depends_on": ["u3"]},
        {"unit_id": "u5", "description": "whose author was born first", "necessary": True, "depends_on": ["u2", "u4"]}]}),
    ("When did the Orion Library open, and who designed it?", {"question_type": "multipart", "units": [
        {"unit_id": "u1", "description": "opening date of the Orion Library", "necessary": True, "depends_on": []},
        {"unit_id": "u2", "description": "designer of the Orion Library", "necessary": True, "depends_on": []}]}),
]

UNIT_SCHEMA = {
    "type": "object",
    "properties": {
        "question_type": {"type": "string", "enum": list(QUESTION_TYPES)},
        "units": {"type": "array", "minItems": 1, "maxItems": 5, "items": {
            "type": "object",
            "properties": {
                "unit_id": {"type": "string"},
                "description": {"type": "string"},
                "necessary": {"type": "boolean"},
                "depends_on": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["unit_id", "description", "necessary", "depends_on"],
        }},
    },
    "required": ["question_type", "units"],
}


def build_messages(question: str) -> List[dict]:
    messages = [{"role": "system", "content": SYSTEM}]
    for q, answer in EXAMPLES:
        messages += [{"role": "user", "content": f"Question: {q}"},
                     {"role": "assistant", "content": json.dumps(answer)}]
    messages.append({"role": "user", "content": f"Question: {question}"})
    return messages


def validate_units(raw: dict) -> Tuple[str, List[Unit]]:
    """Check the decomposition against the schema rules; raise ValueError if it is unusable."""
    qtype = raw.get("question_type")
    if qtype not in QUESTION_TYPES:
        raise ValueError(f"unknown question_type {qtype!r}")
    units, seen = [], []
    for i, u in enumerate(raw.get("units") or [], 1):
        uid = f"u{i}"
        if u.get("unit_id") != uid:
            raise ValueError(f"unit {i} has id {u.get('unit_id')!r}, expected {uid}")
        deps = tuple(u.get("depends_on") or ())
        if any(d not in seen for d in deps):
            raise ValueError(f"{uid} depends on a unit that is not earlier: {deps}")
        desc = str(u.get("description", "")).strip()
        if not desc:
            raise ValueError(f"{uid} has no description")
        units.append(Unit(uid, desc, bool(u.get("necessary")), deps))
        seen.append(uid)
    if not 1 <= len(units) <= 5:
        raise ValueError(f"{len(units)} units, expected 1-5")
    if not any(u.necessary for u in units):
        raise ValueError("no necessary unit")
    if len(units) == 1:
        qtype = "single"  # one unit is a single-answer question whatever the label says
    return qtype, units


def decompose(question: str, client) -> Tuple[str, List[Unit], bool]:
    """Return (question_type, units, fell_back). Falls back to one necessary unit if the reply is unusable."""
    try:
        raw = client.chat_json(build_messages(question), purpose="decompose", schema=UNIT_SCHEMA)
        qtype, units = validate_units(raw)
        return qtype, units, False
    except ValueError:
        return "single", [Unit("u1", question, True, ())], True
