"""One-run offline development audit; no application changes or model calls.

Relation mappings and qualitative reading notes below were inspected by Codex.
They are assistant-assisted review, not independent human annotation or a new
benchmark metric. Run once; existing generated reports are never overwritten.
"""
from collections import Counter, defaultdict
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import statistics
import sys

OUT = Path(__file__).resolve().parent
RUN = OUT.parent
EVAL = RUN.parents[2]
ROOT = EVAL.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(EVAL))
from eval_common import digest, read_jsonl, source_manifest, write_json, write_jsonl
from eval_data import load_b_traces
from eval_score import score_b_run


# Explicit relation correspondences, inspected against each plan and output.
# These are not inferred from matching values or from equal runtime/gold IDs.
IDENTITY2 = {'u1': 'u1', 'u2': 'u2'}
IDENTITY3 = {**IDENTITY2, 'u3': 'u3'}
MAPPINGS = {
    1: {'u3': 'u2'}, 2: IDENTITY2, 3: {'u2': 'u1', 'u3': 'u2'},
    4: {'u5': 'u5'}, 5: {'u1': 'u1', 'u2': 'u2', 'u3': 'u3', 'u4': 'u4'},
    6: {'u1': 'u1', 'u2': 'u3', 'u5': 'u5'},
    7: IDENTITY2, 8: IDENTITY2, 9: IDENTITY2,
    10: {'u3': 'u2'}, 11: {'u2': 'u1', 'u3': 'u2'}, 12: IDENTITY2,
    13: IDENTITY2, 14: IDENTITY3, 15: IDENTITY3,
    16: {'u5': 'u5'}, 17: {'u1': 'u1', 'u2': 'u3', 'u3': 'u2', 'u4': 'u4'},
    18: {'u1': 'u1', 'u5': 'u5'},
    19: {'u1': 'u1', 'u3': 'u3'}, 20: IDENTITY3, 21: IDENTITY3,
    22: {'u1': 'u1'}, 23: {'u1': 'u1'}, 24: {'u1': 'u1'},
    **{n: IDENTITY2 for n in range(25, 37)},
    37: {}, 38: {'u1': 'u2', 'u2': 'u1'}, 39: {'u1': 'u1'},
    40: {'u1': 'u2', 'u2': 'u1'}, 41: {'u1': 'u2', 'u2': 'u1'},
    42: {'u1': 'u2', 'u2': 'u1'},
    43: IDENTITY2, 44: IDENTITY2, 45: IDENTITY2,
    **{n: {'u1': 'u1'} for n in range(46, 49)},
    **{n: {'u2': 'u1'} for n in range(49, 52)},
    52: {}, 53: {}, 54: {}, 55: IDENTITY2, 56: IDENTITY3, 57: IDENTITY3,
    58: {}, 59: {}, 60: {},
}

UNMAPPED = {
    (3, 'u1'): 'Biographical/article-identification claim is outside the gold relations.',
    (5, 'u5'): 'Selected span states the director, not the later-death comparison; full output contains the conclusion elsewhere.',
    (11, 'u1'): 'Identity tautology is outside the gold father/grandfather relations.',
    (13, 'u3'): 'Selected span states a birth date, not the later-birth comparison; full output contains the conclusion elsewhere.',
    (17, 'u5'): 'Selected span states a death date, not the later-death comparison; full output contains the conclusion elsewhere.',
    (19, 'u2'): 'Selected span names Brian Part although this claim metadata/citation concerns John Mosca. Do not approve a mismatched span.',
    **{(n, 'u3'): 'Selected span states an Olympic year, not the earlier-athlete comparison; the conclusion is elsewhere in the full output.' for n in [40, 41, 42]},
    (52, 'u2'): 'Compound producer/release-year value does not isolate a gold unit; run also contains a retraction.',
    (53, 'u1'): 'Producer credit is neither the gold release year nor the requested prior job.',
    (54, 'u1'): 'Producer credit is neither the gold release year nor the requested prior job.',
}

# Per-question reading notes are descriptive development findings, not changes
# to B's labels, expected answers, timing definition, or scoring rules.
NOTES = {
    1: 'Correct requested grandfather in all three. Long adds an unnecessary article fact and retracts it.',
    2: 'Correct chosen film in all three. Short has a date-format difference and a mismatched comparison claim span.',
    3: 'Correct city in all three, with added country Italy. B strict expected value lacks that country suffix.',
    4: 'Immediate/short answer correctly. Long already says Sir Thomas Fiennes, then asks for one generation too far and ends uncertain.',
    5: 'Correct later-born person in all three. Immediate uses ISO dates and assigns the comparison claim to a birth-date sentence.',
    6: 'Correct chosen film in all three. Short dates use day-month order; its comparison span points to a death-date sentence.',
    7: 'Correct same-country answer in all three. Immediate assigns the John Mosca claim to the Brian Part sentence.',
    8: 'Only director name is answered. Jamaica remains missing despite visible Jamaican-born evidence in d7s0.',
    9: 'Both requested Apollo 11 dates correct. Short/long split the two dates into partial and final outputs.',
    10: 'Both requested Perseverance dates correct. Short/long give the launch date before the landing date.',
    11: 'Both requested Voyager 1 dates correct. Short/long split the answer across outputs.',
    12: 'Both requested Voyager 2 dates correct. Short/long split the answer across outputs.',
    13: 'Immediate abstains after non-exact quote validation. Short/long say Roger Staubach; structured value/citations do not cleanly represent gold relations.',
    14: 'Correct comparison winner in all three. Every winner claim span points to the Olympic-year sentence rather than the comparison conclusion. First-ever wording is stronger than participation-year evidence.',
    15: 'Immediate/long answer Bay of Fundy. Short retracts/rephrases the city and misses the bay despite ingested d7s0.',
    16: 'All three confirm only William Kronick. Jon Turteltaub and the final No remain unanswered. B uses an omission-based negative.',
    17: 'All three explicitly confirm Elytis received the award, then say they cannot identify the winner. Extra dependency on Nin blocks the final selection.',
    18: 'All three discuss producer credit but omit the requested prior job. Immediate adds an immediately-before condition; none answers House Speaker.',
    19: 'Immediate gives two different families but omits an explicit No. Short/long explicitly conclude different families, but cite a species-level Osbeckia stellata sentence for a genus-level fact. Their value No is not literally present in the selected not-in-the-same-family span.',
    20: 'All three abstain. Visible evidence and raw review identify Jake Zyrus/Charice, but entity-identity validation rejects the bridge.',
}

UNCERTAIN_AFTER_ANSWER = {12, 49, 50, 51}
MISSING = {22, 23, 24, 37, 44, 46, 47, 48, 52, 53, 54, 58, 59, 60}


def reading(n):
    if n in UNCERTAIN_AFTER_ANSWER:
        return 'answer_then_confusing_uncertainty'
    if n in MISSING:
        return 'partial_or_missing'
    if n == 55:
        return 'implicit_comparison_only'
    return 'explicit_core_answer'


def main():
    inputs = EVAL / 'artifacts/inputs/b-debug-v0'
    traces, input_manifest = load_b_traces(inputs)
    assert input_manifest['questions'] == 20 and len(traces) == 60
    runtime = json.loads((RUN / 'manifest.json').read_text(encoding='utf-8'))
    assert runtime['mode'] == 'b_debug_trace' and len(runtime['trace_ids']) == 60
    assert runtime['b_commit'] == input_manifest['b_commit']
    originals = [RUN / 'policy_log.jsonl', RUN / 'manifest.json', inputs / 'gold.jsonl', inputs / 'traces.jsonl']
    originals += list((RUN / 'b_eval').glob('*'))
    originals += list((RUN / 'samples').glob('*/run.json'))
    originals += list((RUN / 'samples').glob('*/events.jsonl'))
    originals = [p for p in originals if p.is_file()]
    before = {str(p.relative_to(ROOT)): digest(p) for p in originals}
    source_before = source_manifest()
    assert source_before['sha256'] == runtime['source_sha256']
    log_sha = digest(RUN / 'policy_log.jsonl')
    logs = defaultdict(list)
    for row in read_jsonl(RUN / 'policy_log.jsonl'):
        logs[row['trace_id']].append(row)
    golds = {g['sample_id']: g for g in read_jsonl(inputs / 'gold.jsonl')}
    assert len(golds) == 20 and len(logs) == 60
    runs, reviews, audit_claims, reports = [], [], [], []
    for path in sorted((RUN / 'samples').glob('*/run.json')):
        n = int(path.parent.name)
        question_index = (n - 1) // 3 + 1
        r = json.loads(path.read_text(encoding='utf-8'))
        trace_id = r['evaluation']['trace_id']
        rows = logs[trace_id]
        schedule = trace_id.rsplit('_', 1)[-1]
        assert schedule == ['immediate', 'short', 'long'][(n - 1) % 3]
        gold = golds[rows[0]['sample_id']]
        units = {u['unit_id']: u for u in r['units']}
        gold_units = {u['unit_id']: u for u in gold['units']}
        factual = [e for e in r['events'] if e['type'] == 'utterance' and e.get('action') in ['Partial Answer', 'Final Answer']]
        speaking = [e for e in r['events'] if e['type'] == 'utterance']
        entry = {'sample': f'{n:04d}', 'question_index': question_index,
                 'sample_id': rows[0]['sample_id'], 'trace_id': trace_id,
                 'question': r['question'], 'schedule': schedule,
                 'controller_status': r['status'], 'content_reading': reading(n),
                 'notes': NOTES[question_index],
                 'expected_necessary_answers': [u['expected_answer'] for u in gold['units'] if u['necessary']],
                 'first_fact_text_ready_s': next((e['time_s'] for e in factual if e.get('claims')), None),
                 'last_text_ready_s': speaking[-1]['time_s'] if speaking else None,
                 'partial_outputs': sum(e['action'] == 'Partial Answer' for e in speaking),
                 'correction_outputs': sum(e['action'] == 'Correction' for e in speaking),
                 'fallback_factual_outputs': sum(bool(e.get('fallback')) for e in factual if e.get('claims')),
                 'outputs': [{'time_s': e['time_s'], 'action': e['action'], 'text': e['text']} for e in speaking],
                 'raw_run_sha256': digest(path)}
        runs.append(entry)
        for ri, row in enumerate(rows):
            for ci, claim in enumerate(row['claim_spans']):
                uid = claim['controller_unit_id']
                gold_uid = MAPPINGS[n].get(uid)
                reason = UNMAPPED.get((n, uid))
                assert gold_uid or reason, (n, uid)
                if gold_uid:
                    assert gold_uid in gold_units
                    reason = ('Relation inspected against the question, plan, full output and gold description: '
                              + units[uid]['description'] + ' -> ' + gold_units[gold_uid]['description']
                              + '. Map relation only; preserve value, span and citations for B to check.')
                    reviews.append({'run_id': row['run_id'], 'record_index': ri, 'claim_index': ci,
                                    'gold_unit_id': gold_uid, 'source_log_sha256': log_sha,
                                    'reviewer': 'Codex assisted review; not independent human annotation',
                                    'reason': reason})
                audit_claims.append({'sample': f'{n:04d}', 'record_index': ri, 'claim_index': ci,
                                     'controller_unit_id': uid, 'gold_unit_id': gold_uid,
                                     'value': claim['value'], 'text': claim['text'], 'reason': reason})
        reports.extend([f"## {n:04d} / Question {question_index} / {schedule}", '', r['question'], '',
                        'Expected necessary answer(s): ' + '; '.join(entry['expected_necessary_answers']), '',
                        f"Controller: {r['status']}. Assisted reading: {reading(n)}.", '', NOTES[question_index], ''])
        for e in speaking:
            reports.append(f"- [{e['time_s']:.3f}s | {e['action']}] {e['text']}")
        reports.append('')
    assert len(runs) == 60 and {r['question_index'] for r in runs} == set(range(1, 21))
    review_dir = OUT / 'review_assisted'
    review_dir.mkdir(exist_ok=False)
    review_file = review_dir / 'claim_reviews.jsonl'
    write_jsonl(review_file, reviews)
    write_jsonl(OUT / 'claim_audit.jsonl', audit_claims)
    write_jsonl(OUT / 'run_audit.jsonl', runs)
    assisted = score_b_run(inputs, RUN, OUT / 'b_eval_assisted', reviews=review_file)
    diagnostic = score_b_run(inputs, RUN, OUT / 'b_eval_value_diagnostic', allow_value_match=True)
    scores = {s['trace_id']: s for s in read_jsonl(OUT / 'b_eval_assisted/run_scores.jsonl')}
    by_question = []
    for q in range(1, 21):
        group = [r for r in runs if r['question_index'] == q]
        row = {'question_index': q, 'question': group[0]['question'],
               'expected_necessary_answers': '; '.join(group[0]['expected_necessary_answers']),
               'notes': NOTES[q]}
        for r in group:
            s = scores[r['trace_id']]
            row.update({r['schedule'] + '_sample': r['sample'],
                        r['schedule'] + '_reading': r['content_reading'],
                        r['schedule'] + '_system_status': r['controller_status'],
                        r['schedule'] + '_b_status': s['status'],
                        r['schedule'] + '_b_em': s['unit_em'],
                        r['schedule'] + '_b_grounded_complete': s['grounded_complete']})
        by_question.append(row)
    with (OUT / 'by_question.csv').open('x', encoding='utf-8-sig', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(by_question[0]))
        writer.writeheader()
        writer.writerows(by_question)
    (OUT / 'full_responses.md').write_text('# All 60 debug responses, unchanged and in output order\n\n'
        'Assistant-assisted development audit, not independent human grading. '
        'Text times are not measured atomic-claim speech times.\n\n' + '\n'.join(reports), encoding='utf-8')
    counts = Counter(r['content_reading'] for r in runs)
    statuses = Counter(r['controller_status'] for r in runs)
    summary = {'run': RUN.name, 'questions': 20, 'condition_runs': 60,
               'controller_statuses': dict(statuses), 'assisted_reading_categories': dict(counts),
               'reading_by_schedule': {name: dict(Counter(r['content_reading'] for r in runs if r['schedule'] == name))
                                       for name in ['immediate', 'short', 'long']},
               'questions_explicitly_answered_in_all_three': [q for q in range(1, 21)
                    if all(r['content_reading'] == 'explicit_core_answer' for r in runs if r['question_index'] == q)],
               'mapped_claim_reviews': len(reviews), 'raw_declared_claims': len(audit_claims),
               'raw_unmapped_claims': len(audit_claims) - len(reviews),
               'assisted_b_statuses': assisted['status_counts'],
               'assisted_b_groups': assisted['groups'],
               'value_diagnostic_b_groups': diagnostic['groups'],
               'partial_runs': sum(r['partial_outputs'] > 0 for r in runs),
               'fallback_factual_outputs': sum(r['fallback_factual_outputs'] for r in runs),
               'partial_runs_by_schedule': {name: sum(r['partial_outputs'] > 0 for r in runs if r['schedule'] == name)
                                            for name in ['immediate', 'short', 'long']},
               'retraction_samples': [r['sample'] for r in runs if r['correction_outputs']],
               'note': 'Reading categories assess visible core-answer coverage and final uncertainty, not full semantic factuality or formal benchmark accuracy. B scores use unchanged spans and strict expected values. Overall UCR may remain null.'}
    write_json(OUT / 'summary.json', summary)
    after = {str(p.relative_to(ROOT)): digest(p) for p in originals}
    assert before == after, 'An original artifact changed during analysis'
    assert source_manifest() == source_before, 'Runtime source changed during analysis'
    write_json(OUT / 'manifest.json', {'analysis_created_utc': datetime.now(timezone.utc).isoformat(),
               'analysis_script_sha256': digest(Path(__file__)), 'run': RUN.name,
               'b_commit': input_manifest['b_commit'], 'run_source_sha256': runtime['source_sha256'],
               'run_code_commit': runtime['code_commit'], 'run_code_dirty': runtime.get('code_dirty'),
               'original_files_sha256': before, 'original_files_unchanged': True,
               'reviews_sha256': digest(review_file), 'review_identity': 'Codex assisted; not independent human annotation',
               'api_calls': 0, 'gpu_jobs': 0, 'scope': 'debug-v0 only',
               'reading_definitions': {
                   'explicit_core_answer': 'Requested core answer(s) explicitly stated across the response without a later notice undoing the answer; not a check of every ancillary claim.',
                   'answer_then_confusing_uncertainty': 'Correct answer information is stated, but final wording says the requested answer cannot be confirmed or introduces an extra unresolved relation.',
                   'implicit_comparison_only': 'Supporting facts permit the answer, but the requested comparison conclusion is not explicitly given.',
                   'partial_or_missing': 'A requested core answer remains absent.'}})
    print(json.dumps({k: v for k, v in summary.items() if k not in ['assisted_b_groups', 'value_diagnostic_b_groups']}, indent=2))
    for label, report in [('ASSISTED B', assisted), ('VALUE DIAGNOSTIC', diagnostic)]:
        print(label)
        for g in report['groups']:
            print(json.dumps({k: g.get(k) for k in ['runs', 'unit_scored_runs', 'mean_unit_em_on_scored_runs',
                              'mean_unit_f1_on_scored_runs', 'claims', 'scored_claims', 'claims_needing_review',
                              'unsupported_claims', 'unsupported_claim_rate', 'recorded_grounded_completions',
                              'completion_unknown_runs']}, indent=2))
    print('Original files checked unchanged:', len(before))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
