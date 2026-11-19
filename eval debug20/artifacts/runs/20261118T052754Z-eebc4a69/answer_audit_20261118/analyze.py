"""Offline, assistant-assisted debug review. No model calls or source changes."""
from collections import Counter, defaultdict
import csv
from datetime import datetime, timezone
import json
from pathlib import Path
import statistics
import sys

OUT = Path(__file__).resolve().parent
RUN = OUT.parent
EVAL = RUN.parents[2]
ROOT = EVAL.parent
sys.path.insert(0, str(EVAL))
sys.path.insert(0, str(ROOT))
from eval_common import digest, read_jsonl, source_manifest, write_json, write_jsonl
from eval_data import load_b_traces
from eval_score import score_b_run

PAIR = {'u1': 'u1', 'u2': 'u2'}
THREE = {**PAIR, 'u3': 'u3'}
# Inspected semantic relations, not automatic matching of IDs or answer values.
MAPPING = {
    1: PAIR, 2: PAIR, 3: PAIR, 4: {}, 5: {'u5': 'u5'},
    6: {'u1': 'u1', 'u3': 'u3', 'u5': 'u5'},
    7: PAIR, 8: PAIR, 9: PAIR, 10: {'u2': 'u2'}, 11: {}, 12: {},
    13: THREE, 14: THREE, 15: THREE, 16: {}, 17: {},
    18: {**THREE, 'u4': 'u4', 'u5': 'u5'},
    19: THREE, 20: THREE, 21: THREE,
    **{n: PAIR for n in range(22, 37)},
    **{n: {'u1': 'u2'} for n in range(37, 40)},
    **{n: {'u1': 'u2', 'u2': 'u1', 'u3': 'u3'} for n in range(40, 43)},
    43: PAIR, 44: PAIR, 45: PAIR,
    **{n: {'u1': 'u1'} for n in range(46, 49)},
    49: {}, 50: {}, 51: {}, 52: {}, 53: {}, 54: {},
    55: THREE, 56: THREE, 57: THREE, 58: PAIR, 59: PAIR, 60: PAIR,
}
NOTES = {
    1: 'All conditions convey the correct grandfather. Long states father then father-of-father without a later withdrawal.',
    2: 'Immediate fails plan-review dependency validation; short and long give the correct film.',
    3: 'All conditions identify the correct city, adding Italy, which remains outside the strict expected value.',
    4: 'Immediate answers correctly. Short is blocked by an unnecessary identity unit; long fails self-placeholder validation in plan review.',
    5: 'All conditions clearly name the correct later-born person; repeated-name spans now retain full utterance context.',
    6: 'Immediate and short fail plan-review dependency validation; long correctly names the film, with a differently formatted optional death date.',
    7: 'All conditions explicitly answer Yes. Country values United States differ from gold American, although the core conclusion is correct.',
    8: 'Immediate still misses visible Jamaican-born evidence; short and long explicitly answer Jamaica.',
    9: 'Both requested dates correct in all conditions; partial output appears in long only.',
    10: 'Both requested dates correct in all conditions; partial output appears in long only.',
    11: 'Both requested dates correct in all conditions; partial output appears in long only.',
    12: 'Both requested dates correct in all conditions; partial output appears in long only.',
    13: 'All conditions explicitly answer Roger Staubach. Nickname facts map to the necessary gold identity relation; support is left to B.',
    14: 'All conditions state the correct comparison winner. First-ever participation wording is stronger than the reference participation-year relation.',
    15: 'All conditions explicitly answer Bay of Fundy without withdrawing the supported city.',
    16: 'All conditions answer only the Kronick premise. The requested No remains absent; B relies on omission-based negation.',
    17: 'All conditions say Elytis received the award in 1979, then answer an invented interval question with uncertainty. Award-year claims are outside gold relations.',
    18: 'All conditions omit the requested prior job; two say producer. Visible former-Speaker evidence remains unused.',
    19: 'All conditions explicitly state No and the two different families. Verify citation support separately; wording alone does not prove genus-level support.',
    20: 'All conditions now identify Jake Zyrus and explicitly say Charice.',
}
ERRORS = {4, 12, 16, 17}
UNCERTAIN = {49, 50, 51}
MISSING = {11, 22, 46, 47, 48, 52, 53, 54}


def category(n):
    return ('operational_error' if n in ERRORS else 'answer_then_confusing_uncertainty' if n in UNCERTAIN
            else 'partial_or_missing' if n in MISSING else 'explicit_core_answer')


def main():
    inputs = EVAL / 'artifacts/inputs/b-debug-v0'
    traces, im = load_b_traces(inputs)
    runtime = json.loads((RUN / 'manifest.json').read_text(encoding='utf-8'))
    assert (runtime['mode'], runtime['split'], runtime['data_version']) == ('b_debug_trace', 'debug', 'debug-v0')
    assert len(traces) == len(runtime['trace_ids']) == 60 and im['questions'] == 20
    original = [RUN / 'manifest.json', RUN / 'policy_log.jsonl', RUN / 'source-manifest.json',
                RUN / 'audio_summary.json', inputs / 'gold.jsonl', inputs / 'traces.jsonl']
    original += list((RUN / 'b_eval').glob('*'))
    original += list((RUN / 'samples').glob('*/run.json'))
    original += list((RUN / 'samples').glob('*/events.jsonl'))
    original = [p for p in original if p.is_file()]
    hashes = {str(p.relative_to(ROOT)): digest(p) for p in original}
    current_source = source_manifest()
    golds = {g['sample_id']: g for g in read_jsonl(inputs / 'gold.jsonl')}
    logs = defaultdict(list)
    for row in read_jsonl(RUN / 'policy_log.jsonl'):
        logs[row['trace_id']].append(row)
    runs, reviews, claim_audit, transcript, review_latencies = [], [], [], [], []
    for path in sorted((RUN / 'samples').glob('*/run.json')):
        n = int(path.parent.name)
        r = json.loads(path.read_text(encoding='utf-8'))
        rows = logs[r['evaluation']['trace_id']]
        gold = golds[rows[0]['sample_id']]
        units = {u['unit_id']: u for u in r['units']}
        targets = {u['unit_id']: u for u in gold['units']}
        q, schedule = (n - 1) // 3 + 1, rows[0]['trace_id'].rsplit('_', 1)[-1]
        assert schedule == ['immediate', 'short', 'long'][(n - 1) % 3]
        events = [e for e in r['events'] if e['type'] == 'utterance']
        factual = [e for e in events if e.get('claims')]
        review_latencies.extend(c['latency_s'] for c in r['llm_calls'] if c['purpose'] == 'plan_review')
        entry = {'sample': f'{n:04d}', 'question_index': q, 'question': r['question'],
            'trace_id': rows[0]['trace_id'], 'schedule': schedule, 'status': r['status'],
            'content_reading': category(n), 'notes': NOTES[q],
            'expected_necessary_answers': [u['expected_answer'] for u in gold['units'] if u['necessary']],
            'partial_outputs': sum(e['action'] == 'Partial Answer' for e in events),
            'corrections': sum(e['action'] == 'Correction' for e in events),
            'fallback_factual_outputs': sum(bool(e.get('fallback')) for e in factual),
            'text_pipeline_wall_s': r['evaluation']['text_pipeline_wall_s'],
            'total_wall_s': r['evaluation']['total_wall_s'],
            'outputs': [{'time_s': e['time_s'], 'action': e['action'], 'text': e['text']} for e in events]}
        runs.append(entry)
        transcript.extend([f'## {n:04d} / Question {q} / {schedule}', '', r['question'], '',
            'Expected core answer(s): ' + '; '.join(entry['expected_necessary_answers']), '',
            f"System: {r['status']}; assisted reading: {category(n)}.", '', NOTES[q], ''])
        transcript.extend(f"- [{e['time_s']:.3f}s | {e['action']}] {e['text']}" for e in events)
        transcript.append('')
        for ri, row in enumerate(rows):
            for ci, claim in enumerate(row['claim_spans']):
                uid = claim['controller_unit_id']
                target = MAPPING[n].get(uid)
                if target:
                    reason = ('Inspected relation: ' + units[uid]['description'] + ' -> ' + targets[target]['description']
                              + '. Keep the original value/text/citations for B checks; not matched by value.')
                    reviews.append({'run_id': row['run_id'], 'record_index': ri, 'claim_index': ci,
                        'gold_unit_id': target, 'source_log_sha256': hashes[str((RUN / 'policy_log.jsonl').relative_to(ROOT))],
                        'reviewer': 'Codex assisted relation review; not independent human annotation', 'reason': reason})
                else:
                    assert n in {49, 50, 51, 52, 54}, (n, uid)
                    reason = ('Award year is not the gold yes/no or named-winner relation.' if q == 17
                              else 'Producer credit is not the gold release year or requested prior job.')
                claim_audit.append({'sample': f'{n:04d}', 'record_index': ri, 'claim_index': ci,
                    'controller_unit_id': uid, 'gold_unit_id': target, 'value': claim['value'],
                    'text': claim['text'], 'reason': reason})
    assert len(runs) == 60
    (OUT / 'review_assisted').mkdir(exist_ok=False)
    review_file = OUT / 'review_assisted/claim_reviews.jsonl'
    write_jsonl(review_file, reviews)
    write_jsonl(OUT / 'run_audit.jsonl', runs)
    write_jsonl(OUT / 'claim_audit.jsonl', claim_audit)
    assisted = score_b_run(inputs, RUN, OUT / 'b_eval_assisted', reviews=review_file)
    approx = score_b_run(inputs, RUN, OUT / 'b_eval_value_diagnostic', allow_value_match=True)
    scores = {s['trace_id']: s for s in read_jsonl(OUT / 'b_eval_assisted/run_scores.jsonl')}
    by_question = []
    for q in range(1, 21):
        subset = [r for r in runs if r['question_index'] == q]
        row = {'question_index': q, 'question': subset[0]['question'],
            'expected_necessary_answers': '; '.join(subset[0]['expected_necessary_answers']), 'notes': NOTES[q]}
        for r in subset:
            s = scores[r['trace_id']]
            row.update({r['schedule'] + '_sample': r['sample'], r['schedule'] + '_reading': r['content_reading'],
                r['schedule'] + '_system_status': r['status'], r['schedule'] + '_b_status': s['status'],
                r['schedule'] + '_b_em': s['unit_em'], r['schedule'] + '_b_grounded_complete': s['grounded_complete']})
        by_question.append(row)
    with (OUT / 'by_question.csv').open('x', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(by_question[0])); writer.writeheader(); writer.writerows(by_question)
    (OUT / 'full_responses.md').write_text('# All 60 latest debug responses\n\n'
        'Unchanged utterances, in order. Assistant-assisted development review; text times are not atomic speech times.\n\n'
        + '\n'.join(transcript), encoding='utf-8')
    old_run = RUN.parent / '20261118T042104Z-af3cd283'
    previous = read_jsonl(old_run / 'answer_audit_20261117/run_audit.jsonl')
    previous_by_trace = {r['trace_id']: r for r in previous}
    changes = [{'sample': r['sample'], 'question_index': r['question_index'], 'schedule': r['schedule'],
                'previous': previous_by_trace[r['trace_id']]['content_reading'], 'latest': r['content_reading']}
               for r in runs if previous_by_trace[r['trace_id']]['content_reading'] != r['content_reading']]
    write_jsonl(OUT / 'comparison.jsonl', changes)
    summary = {'run': RUN.name, 'questions': 20, 'runs': 60,
        'controller_statuses': dict(Counter(r['status'] for r in runs)),
        'assisted_reading': dict(Counter(r['content_reading'] for r in runs)),
        'reading_by_schedule': {s: dict(Counter(r['content_reading'] for r in runs if r['schedule'] == s))
                                for s in ['immediate', 'short', 'long']},
        'questions_explicitly_answered_in_all_three': [q for q in range(1, 21)
            if all(r['content_reading'] == 'explicit_core_answer' for r in runs if r['question_index'] == q)],
        'raw_claims': len(claim_audit), 'assisted_mappings': len(reviews), 'unmapped_claims': len(claim_audit)-len(reviews),
        'assisted_b_groups': assisted['groups'], 'value_diagnostic_b_groups': approx['groups'],
        'b_statuses': assisted['status_counts'],
        'partial_runs_by_schedule': {s: sum(r['partial_outputs'] > 0 for r in runs if r['schedule'] == s)
                                     for s in ['immediate', 'short', 'long']},
        'fallback_factual_outputs': sum(r['fallback_factual_outputs'] for r in runs),
        'correction_outputs': sum(r['corrections'] for r in runs),
        'plan_review_calls': len(review_latencies), 'plan_review_call_median_s': statistics.median(review_latencies),
        'text_pipeline_wall_median_all_runs_s': statistics.median(r['text_pipeline_wall_s'] for r in runs),
        'total_wall_median_all_runs_s': statistics.median(r['total_wall_s'] for r in runs),
        'comparison': changes,
        'note': 'Reading categories describe core-answer coverage and final uncertainty, not full semantic accuracy. B strict scores retain their coverage limits.'}
    write_json(OUT / 'summary.json', summary)
    assert {str(p.relative_to(ROOT)): digest(p) for p in original} == hashes
    assert source_manifest() == current_source
    write_json(OUT / 'manifest.json', {'created_utc': datetime.now(timezone.utc).isoformat(),
        'run_source_sha256': runtime['source_sha256'], 'analysis_current_source_sha256': current_source['sha256'],
        'run_parent_commit': runtime['code_commit'], 'run_dirty': True, 'b_commit': im['b_commit'],
        'original_files_sha256': hashes, 'original_files_unchanged': True,
        'review_identity': 'Codex assisted, not independent human annotation', 'api_calls': 0,
        'analysis_script_sha256': digest(Path(__file__)), 'reviews_sha256': digest(review_file)})
    print(json.dumps({k: v for k, v in summary.items() if k not in ['assisted_b_groups', 'value_diagnostic_b_groups', 'comparison']}, indent=2))
    print('ASSISTED B', json.dumps(assisted['groups'], indent=2))
    print('VALUE DIAGNOSTIC', json.dumps(approx['groups'], indent=2))
    print('Original files unchanged:', len(hashes))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
