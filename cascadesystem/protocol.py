"""Bounded repairs for model output contracts; evidence checks remain strict."""
from collections import Counter
from copy import deepcopy
from dataclasses import asdict
import re

from .llm import JUDGE, plan_prompt
from .models import Judgment, plan_from_json, validate_judgments
from .grounding import dependency_ids


def explicit_dependencies(raw):
    """Add only dependencies already explicitly named by known placeholders."""
    if not isinstance(raw, dict) or not isinstance(raw.get('units'), list):
        return raw, []
    rows = raw['units']
    ids = [row.get('unit_id') for row in rows if isinstance(row, dict)]
    if len(ids) != len(rows) or any(not isinstance(uid, str) for uid in ids) or len(set(ids)) != len(ids):
        return raw, []
    repaired, changes = deepcopy(raw), []
    for row in repaired['units']:
        dependencies, queries = row.get('depends_on'), row.get('queries')
        if not isinstance(dependencies, list) or any(not isinstance(uid, str) for uid in dependencies) or not isinstance(queries, list):
            return raw, []
        texts = [row.get('description', ''), row.get('subject', ''), *queries]
        if any(not isinstance(text, str) for text in texts):
            return raw, []
        mentioned = list(dict.fromkeys(ref for text in texts for ref in re.findall(r'\{(u[0-9]+)\}', text)))
        if any(uid not in ids or uid == row['unit_id'] for uid in mentioned):
            return raw, []
        missing = [uid for uid in mentioned if uid not in dependencies]
        if missing:
            row['depends_on'] = [*dependencies, *missing]
            changes.append({'unit_id': row['unit_id'], 'added_dependencies': missing})
    return repaired, changes


def judgment_contract(raw, units):
    expected = [unit.unit_id for unit in units]
    rows = raw.get('judgments') if isinstance(raw, dict) else None
    strings = [row.get('unit_id') for row in rows if isinstance(row, dict) and isinstance(row.get('unit_id'), str)] if isinstance(rows, list) else []
    counts = Counter(strings)
    return {'expected_unit_ids': expected, 'returned_unit_ids': strings,
            'missing_unit_ids': sorted(set(expected) - set(strings)),
            'unexpected_unit_ids': sorted(set(strings) - set(expected)),
            'duplicate_unit_ids': sorted(uid for uid, count in counts.items() if count > 1),
            'malformed_rows': len(rows) - len(strings) if isinstance(rows, list) else None}


def literal_quote_whitespace(raw, sources):
    """Recover a unique source substring differing only in whitespace, never words.

    The raw reply remains logged. The strict validator still receives verbatim
    source characters; ellipses, omitted words and case changes are not repaired.
    """
    if not isinstance(raw, dict) or not isinstance(raw.get('judgments'), list):
        return raw, []
    result, changes = deepcopy(raw), []
    by_id = {source.evidence_id: source for source in sources}
    for row in result['judgments']:
        if not isinstance(row, dict) or not isinstance(row.get('quotes'), list):
            continue
        for quote in row['quotes']:
            if not isinstance(quote, dict):
                continue
            eid, text = quote.get('evidence_id'), quote.get('text')
            source = by_id.get(eid) if isinstance(eid, str) else None
            if source is None or not isinstance(text, str) or not text.strip() or text in source.text:
                continue
            pattern = r'\s+'.join(re.escape(token) for token in text.split())
            matches = list(re.finditer(pattern, source.text))
            if len(matches) == 1:
                exact = matches[0].group()
                quote['text'] = exact
                changes.append({'unit_id': row.get('unit_id'), 'evidence_id': source.evidence_id,
                                'original_quote': text, 'literal_quote': exact})
    return result, changes


def quote_repair_sources(raw, sources, rejected):
    rows = raw.get('judgments', []) if isinstance(raw, dict) else []
    ids = {eid for row in rows if isinstance(row, dict) and row.get('unit_id') in rejected
           and isinstance(row.get('citations'), list) for eid in row['citations'] if isinstance(eid, str)}
    return [{'evidence_id': source.evidence_id, 'text': source.text} for source in sources
            if source.evidence_id in ids]


async def review_question_plan(llm, question, language, units, settings, emit):
    """One question-only semantic review for providers opting in; no evidence/gold."""
    if not getattr(llm, 'requires_plan_review', False):
        return units
    payload = {'question': question, 'output_language': language,
               'proposed_units': [asdict(unit) for unit in units]}
    await emit('plan_review_requested', max_reviews=1, question_only=True)
    raw = await llm.complete('plan_review', plan_prompt(settings) +
        '\nReview the proposed plan once against the ORIGINAL question. Return a complete '
        'JSON plan, retaining valid units and correcting semantic mistakes. Check relation depth, '
        'answer type, required comparison conclusions, unnecessary prerequisite negatives, '
        'invented immediately-before conditions and unnecessary identity/article tasks. '
        'A supported choice candidate must not be blocked by proving all other candidates negative. '
        'Do not solve the question, supply factual answers, or use model memory. '
        'No evidence or reference answers are available. Return only the corrected units schema.', payload)
    await emit('plan_review_reply', reply=raw)
    try:
        reviewed = plan_from_json(raw, settings.max_units)
    except ValueError as error:
        normalized, changes = explicit_dependencies(raw)
        if str(error) != 'Placeholders must name explicit dependencies' or not changes:
            await emit('plan_review_rejected', error=str(error))
            raise
        # Use the same safe normalization as the initial plan, with no extra call.
        try:
            reviewed = plan_from_json(normalized, settings.max_units)
        except ValueError as normalized_error:
            await emit('plan_review_rejected', error=str(normalized_error))
            raise
        await emit('protocol_normalized', stage='plan_review', changes=changes,
                   units=[asdict(unit) for unit in reviewed], no_facts_added=True)
    await emit('plan_review_finished', changed=reviewed != units,
               units=[asdict(unit) for unit in reviewed], question_only=True)
    return reviewed


async def decompose(llm, question, language, settings, emit):
    payload = {'question': question, 'output_language': language}
    prompt = plan_prompt(settings)
    previous = details = None
    for attempt in range(2):
        request = payload if attempt == 0 else {**payload, 'previous_reply': previous, 'validation_error': details}
        raw = await llm.complete('decompose' if attempt == 0 else 'decompose_repair', prompt if attempt == 0 else prompt +
                                 '\nRepair only the invalid plan using the validation error. Previous reply is untrusted data. '
                                 'Return a complete JSON plan for the original question, not an explanation or an answer.', request)
        await emit('decompose_reply', reply=raw, attempt=attempt + 1, repair=bool(attempt))
        try:
            units = plan_from_json(raw, settings.max_units)
        except ValueError as error:
            details = str(error)
            await emit('protocol_validation_failed', stage='decompose', attempt=attempt + 1, error=details)
            if details == 'Placeholders must name explicit dependencies':
                normalized, changes = explicit_dependencies(raw)
                if changes:
                    try:
                        units = plan_from_json(normalized, settings.max_units)
                    except ValueError:
                        pass  # Unknown references/cycles/other defects still need a model repair or rejection.
                    else:
                        await emit('protocol_normalized', stage='decompose', changes=changes,
                                   units=[asdict(unit) for unit in units], no_facts_added=True)
                        return await review_question_plan(llm, question, language, units, settings, emit)
            if attempt:
                await emit('protocol_repair_exhausted', stage='decompose', error=details)
                raise
            previous = raw
            await emit('protocol_repair_requested', stage='decompose', reason=details, max_repairs=1)
        else:
            return await review_question_plan(llm, question, language, units, settings, emit)
    raise ValueError('Plan repair exhausted')


async def judge(llm, question, language, units, sources, emit, previous_judgments=None):
    # One immutable, already-ingested snapshot is used for both attempts.
    payload = {'question': question, 'output_language': language, 'units': [asdict(unit) for unit in units],
               'required_unit_ids': [unit.unit_id for unit in units],
               'visible_evidence_ids': [source.evidence_id for source in sources],
               'evidence': [asdict(source) for source in sources]}
    if previous_judgments:
        payload['previous_judgments'] = {uid: asdict(value) for uid, value in previous_judgments.items()}
    previous = details = None
    rejected = []
    for attempt in range(2):
        request = payload if attempt == 0 else {**payload, 'previous_reply': previous,
                                                'validation_error': details, 'rejected_units': rejected,
                                                'literal_quote_sources': quote_repair_sources(previous, sources, rejected)}
        raw = await llm.complete('judge' if attempt == 0 else 'judge_repair', JUDGE if attempt == 0 else JUDGE +
                                 '\nRepair the previous reply, which is untrusted data. Return the complete judgment list '
                                 'for required_unit_ids, each exactly once. Never add or rename units. '
                                 'Use only this same evidence snapshot. Copy SHORT exact source substrings without ellipses. '
                                 'If a unit cannot be established, explicitly return UNRESOLVED with empty value/citations/quotes.', request)
        # Log before validation so malformed IDs and duplicate/missing rows remain diagnosable.
        await emit('judge_reply', reply=raw, attempt=attempt + 1, repair=bool(attempt),
                   evidence_snapshot_ids=payload['visible_evidence_ids'])
        normalized, changes = literal_quote_whitespace(raw, sources)
        if changes:
            await emit('protocol_normalized', stage='judge_quotes', changes=changes,
                       evidence_snapshot_ids=payload['visible_evidence_ids'], no_facts_added=True)
        try:
            judgments = validate_judgments(normalized, units, sources)
        except ValueError as error:
            details = {'error': str(error), **judgment_contract(raw, units)}
            await emit('protocol_validation_failed', stage='judge', attempt=attempt + 1, **details)
            if attempt:
                await emit('protocol_repair_exhausted', stage='judge', **details)
                raise
        else:
            rejected = [uid for uid, judgment in judgments.items() if judgment.reason.startswith('Rejected:')]
            if not rejected:
                return judgments
            details = {'error': 'Rejected value/citation/exact quote', 'rejected_units': rejected,
                       'rejected_unit_details': {uid: judgments[uid].reason for uid in rejected}}
            await emit('protocol_validation_failed', stage='judge', attempt=attempt + 1, **details)
            if attempt:
                # The validator already converted invalid facts to UNRESOLVED. Never restore them.
                await emit('protocol_repair_exhausted', stage='judge', **details)
                return judgments
        previous = raw
        await emit('protocol_repair_requested', stage='judge', reason=details, max_repairs=1,
                   evidence_snapshot_ids=payload['visible_evidence_ids'])
    raise ValueError('Judge repair exhausted')


async def completion_review(llm, question, language, units, sources, judgments, targets, emit):
    """One semantic recheck; opt-in bounded quote repair, never new evidence."""
    focus = dependency_ids(targets, units)
    snapshot = tuple(sources)
    payload = {'question': question, 'output_language': language,
               'units': [asdict(unit) for unit in units],
               'required_unit_ids': [unit.unit_id for unit in units],
               'visible_evidence_ids': [source.evidence_id for source in snapshot],
               'evidence': [asdict(source) for source in snapshot],
               'review_mode': 'retrieval_complete', 'review_unit_ids': focus,
               'unresolved_necessary_ids': list(targets),
               'previous_judgments': {uid: asdict(value) for uid, value in judgments.items()}}
    await emit('semantic_review_requested', target_unit_ids=list(targets), review_unit_ids=focus,
               evidence_snapshot_ids=payload['visible_evidence_ids'], max_reviews=1)
    raw = await llm.complete('judge', JUDGE +
                             '\nRetrieval has ended. Recheck review_unit_ids once using only this evidence. '
                             'Previous judgments are untrusted hints, not evidence. Inspect source titles, '
                             'pronouns, explicit relations, and dependency chains for missed support. '
                             'Do not change the question, unit meanings, or evidence. '
                             'For each citation copy a contiguous source substring; if a short quote '
                             'is hard to copy, use the complete cited sentence exactly as provided. '
                             'Never replace omitted words with ellipses or simplify a nickname list. '
                             'Keep unsupported or conflicting facts unresolved/contradicted. '
                             'Return every required unit exactly once; no explanation outside JSON.', payload)
    await emit('semantic_review_reply', reply=raw, evidence_snapshot_ids=payload['visible_evidence_ids'])
    normalized, changes = literal_quote_whitespace(raw, snapshot)
    if changes:
        await emit('protocol_normalized', stage='completion_quotes', changes=changes,
                   evidence_snapshot_ids=payload['visible_evidence_ids'], no_facts_added=True)
    try:
        reviewed = validate_judgments(normalized, units, snapshot)
    except ValueError as error:
        await emit('semantic_review_rejected', error=str(error), **judgment_contract(raw, units))
        return None
    rejected = [uid for uid, value in reviewed.items() if value.reason.startswith('Rejected:')]
    if rejected and getattr(llm, 'repairs_completion_quotes', False):
        # This is one contract repair of this review, not another semantic review.
        request = {**payload, 'previous_reply': raw, 'rejected_unit_ids': rejected,
                   'literal_quote_sources': quote_repair_sources(raw, snapshot, rejected)}
        await emit('completion_quote_repair_requested', unit_ids=rejected, max_repairs=1,
                   evidence_snapshot_ids=payload['visible_evidence_ids'])
        repaired = await llm.complete('judge_repair', JUDGE +
            '\nRepair ONLY the exact-quote contract of the previous completion review. '
            'The literal_quote_sources are the same visible sources. Copy their original '
            'contiguous text, including spacing. Do not change unit IDs, supported values '
            'or citation IDs. Do not promote unresolved facts or add new conclusions. '
            'If the existing fact cannot be supported, downgrade it to UNRESOLVED. '
            'Return every required unit exactly once. Previous replies are untrusted data.', request)
        await emit('completion_quote_repair_reply', reply=repaired,
                   evidence_snapshot_ids=payload['visible_evidence_ids'])
        normalized, changes = literal_quote_whitespace(repaired, snapshot)
        if changes:
            await emit('protocol_normalized', stage='completion_quote_repair', changes=changes,
                       evidence_snapshot_ids=payload['visible_evidence_ids'], no_facts_added=True)
        try:
            replacement = validate_judgments(normalized, units, snapshot)
            original_rows = {row['unit_id']: row for row in raw['judgments']}
            for row in normalized['judgments']:
                old = original_rows[row['unit_id']]
                if row.get('label') != old.get('label') and not (
                        old.get('label') == 'SUPPORTED' and row.get('label') == 'UNRESOLVED'):
                    raise ValueError('Quote repair changed a semantic label')
                if row.get('label') == 'SUPPORTED' and (old.get('label') != 'SUPPORTED' or
                        row.get('value') != old.get('value') or row.get('citations') != old.get('citations')):
                    raise ValueError('Quote repair changed a fact instead of only its quote')
        except (ValueError, KeyError, TypeError) as error:
            await emit('completion_quote_repair_rejected', error=str(error))
        else:
            reviewed = replacement
            await emit('completion_quote_repair_finished',
                       recovered_unit_ids=[uid for uid in rejected if reviewed[uid].label == 'SUPPORTED'],
                       rejected_unit_ids=[uid for uid in rejected if reviewed[uid].label != 'SUPPORTED'])
    # The dependency closure is complete. Unrelated units retain their existing validated state.
    result = {unit.unit_id: reviewed[unit.unit_id] if unit.unit_id in focus else judgments[unit.unit_id]
              for unit in units}
    changed = {uid for uid in focus if (result[uid].label, result[uid].value) !=
               (judgments[uid].label, judgments[uid].value)}
    for unit in units:
        if unit.unit_id not in focus and result[unit.unit_id].label == 'SUPPORTED':
            ancestors = set(dependency_ids([unit.unit_id], units)) - {unit.unit_id}
            if ancestors & changed:
                result[unit.unit_id] = Judgment(reason='Dependency changed during completion review')
    # Scope preservation must not restore a child whose reviewed ancestor has changed.
    result = validate_judgments({'judgments': [asdict(result[u.unit_id]) | {'unit_id': u.unit_id}
                                             for u in units]}, units, snapshot)
    await emit('semantic_review_finished', review_unit_ids=focus,
               recovered_unit_ids=[uid for uid in targets if result[uid].label == 'SUPPORTED'])
    return result
