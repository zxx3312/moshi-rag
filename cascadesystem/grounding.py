"""Build verification context from selected facts and their visible dependencies."""
from dataclasses import asdict

from .models import resolve_text


def dependency_ids(ids, units):
    by_id = {unit.unit_id: unit for unit in units}
    closure = set()

    def include(uid):
        if uid in closure:
            return
        closure.add(uid)
        for parent in by_id[uid].depends_on:
            include(parent)

    for uid in ids:
        include(uid)
    return [unit.unit_id for unit in units if unit.unit_id in closure]


def verification_context(ids, units, judgments, sources):
    """Ancestors explain grounding; they are not extra facts permitted in the draft."""
    selected = set(ids)
    closure = set(dependency_ids(ids, units))
    dependencies = [unit for unit in units if unit.unit_id in closure - selected]
    context = []
    citations = set()
    for unit in units:
        if unit.unit_id not in closure:
            continue
        judgment = judgments[unit.unit_id]
        if judgment.label != 'SUPPORTED':
            raise ValueError('Output requires supported facts and all their dependencies')
        citations.update(judgment.citations)
        if unit.unit_id not in selected:
            context.append({'unit_id': unit.unit_id, 'description': resolve_text(unit.description, judgments),
                            'value': judgment.value, 'citations': list(judgment.citations),
                            'quotes': judgment.quotes, 'context_only': True})
    visible = {source.evidence_id for source in sources}
    if not citations <= visible:
        raise ValueError('Verification cannot use an invisible citation')
    return {'dependency_units': [asdict(unit) for unit in dependencies],
            'DEPENDENCY_FACTS': context,
            'evidence': [asdict(source) for source in sources if source.evidence_id in citations]}


def draft_units_valid(reply, ids):
    """Require the verifier to account for exactly the units permitted in this output."""
    expressed = reply.get('expressed_unit_ids')
    return (isinstance(expressed, list) and all(isinstance(uid, str) for uid in expressed)
            and len(expressed) == len(set(expressed)) and set(expressed) == set(ids))
