"""Offline assistant-assisted debug audit; never calls a model or changes run data."""
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
PREVIOUS = RUN.parent / '20261118T052754Z-eebc4a69'
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(EVAL))
from eval_common import digest, read_jsonl, source_manifest, write_json, write_jsonl
from eval_data import load_b_traces
from eval_score import score_b_run

# Relations inspected in each saved plan/utterance against B's debug units.
# Matching runtime IDs alone is not evidence of semantic alignment.
PAIR = {'u1': 'u1', 'u2': 'u2'}
THREE = {**PAIR, 'u3': 'u3'}
FIVE = {**THREE, 'u4': 'u4', 'u5': 'u5'}
MAPPING = {
    **{n: PAIR for n in range(1, 4)},
    **{n: FIVE for n in range(4, 7)},
    **{n: PAIR for n in range(7, 10)},
    **{n: {'u2': 'u1', 'u3': 'u2'} for n in range(10, 13)},
    **{n: THREE for n in range(13, 16)},
    **{n: FIVE for n in range(16, 19)},
    **{n: THREE for n in range(19, 22)},
    **{n: PAIR for n in range(22, 37)},
    **{n: {'u1': 'u2'} for n in range(37, 40)},
    **{n: {'u1': 'u2', 'u2': 'u1', 'u3': 'u3'} for n in range(40, 43)},
    **{n: PAIR for n in range(43, 46)},
    **{n: THREE for n in range(46, 49)},
    **{n: {} for n in range(49, 52)},
    52: {'u1': 'u2'}, 53: {'u2': 'u2'}, 54: {'u2': 'u2'},
    **{n: THREE for n in range(55, 58)},
    **{n: PAIR for n in range(58, 61)},
}
NOTES = {
    1: '三条件都给出正确祖父；long先说父亲再补祖父，最终引用仅列祖父句，交B核对链条支持。',
    2: '三条件核心电影正确；short最终比较只引用一方死亡日期，引用完整性不足。',
    3: '三条件都给出城市，不再额外加Italy；short/long先报导演再报出生地。',
    4: '三条件核心祖父正确；仍有多余身份单元，附加身份声明没有对应gold单元，保留待复核。',
    5: '三条件生日、比较结论均明确；short/long分别先回答一方日期。',
    6: '三条件都取到两位导演与日期，但LoRA把较早去世者Hotel Paradis当成较晚者；基础模型核验正确拦截，末尾均未给正确结论。',
    7: '三条件明确Yes；桥接国籍用United States而gold为American，存在严格值口径差异。',
    8: '三条件均明确Jamaica；immediate较上一轮恢复，short/long先报导演。',
    9: 'Apollo 11两日期全部正确；short/long有部分回答。',
    10: 'Perseverance两日期全部正确；short/long有部分回答。',
    11: 'Voyager 1两日期全部正确；long分段，short合并回答。',
    12: 'Voyager 2两日期全部正确；short/long有部分回答。',
    13: '三条件明确Roger Staubach；计划缩为昵称识别，完整共同创办条件没有独立验证。',
    14: '三条件给出正确比较对象；first-ever措辞强于现有某年参赛证据，long比较引用只列一方。',
    15: '三条件语音文字均说出Bay of Fundy；long声明值仅Fundy，城市仅Saint John，与gold严格值不一致。',
    16: 'immediate/short将Jon误判为电视编剧，被核验拦截且连带丢掉正确William事实；long一次judge JSON失败。',
    17: '三条件都说过Elytis在1979年获奖，但仍误拆成两人获奖时间之间的区间，末尾不确定。',
    18: 'immediate答出Speaker of the House，值比gold短；short/long仅确认制片人，未给所问此前职业。',
    19: 'immediate引用身份校验拒绝Gordonia并阻断结论；short给出No与两科，long仍用物种证据支持属。',
    20: '三条件都明确Charice；short/long使用专辑原名Charice句，严格mononym支持待B核对。',
}
ERRORS = {48}
CONFUSING = {49, 50, 51}
MISSING = {16, 17, 18, 46, 47, 53, 54, 55}


def category(n):
    return ('operational_error' if n in ERRORS else 'answer_then_confusing_uncertainty' if n in CONFUSING
            else 'partial_or_missing' if n in MISSING else 'explicit_core_answer')


def call_stats(runs):
    grouped = defaultdict(list)
    failures = Counter()
    for run in runs:
        for call in run['llm_calls']:
            if call['status'] == 'ok':
                grouped[call['purpose']].append(call['latency_s'])
            else:
                failures[call['purpose'] + ':' + call['status']] += 1
    return {'ok': {p: {'n': len(v), 'median_s': statistics.median(v)} for p, v in grouped.items()},
            'non_ok': dict(failures)}


def main():
    inputs = EVAL / 'artifacts/inputs/b-debug-v0'
    traces, im = load_b_traces(inputs)
    runtime = json.loads((RUN / 'manifest.json').read_text(encoding='utf-8'))
    assert (runtime['mode'], runtime['split'], runtime['data_version']) == ('b_debug_trace', 'debug', 'debug-v0')
    assert len(traces) == len(runtime['trace_ids']) == 60 and im['questions'] == 20
    assert runtime['settings']['judge_model'].endswith('/sampler_weights/epoch-0001')
    originals = [p for directory in [RUN, PREVIOUS] for p in directory.rglob('*')
                 if p.is_file() and not p.is_relative_to(OUT)]
    originals += [inputs / name for name in ['manifest.json', 'traces.jsonl', 'gold.jsonl']]
    hashes = {p.relative_to(ROOT).as_posix(): digest(p) for p in originals}
    current_source = source_manifest()
    golds = {g['sample_id']: g for g in read_jsonl(inputs / 'gold.jsonl')}
    logs = defaultdict(list)
    for row in read_jsonl(RUN / 'policy_log.jsonl'):
        logs[row['trace_id']].append(row)
    review_rows, claims, runs, transcript, full_runs, diagnostics = [], [], [], [], [], []
    paths = sorted((RUN / 'samples').glob('*/run.json'))
    assert len(paths) == 60
    log_hash = digest(RUN / 'policy_log.jsonl')
    for path in paths:
        n = int(path.parent.name)
        r = json.loads(path.read_text(encoding='utf-8')); full_runs.append(r)
        rows = logs[r['evaluation']['trace_id']]
        gold = golds[rows[0]['sample_id']]
        units = {u['unit_id']: u for u in r['units']}; targets = {u['unit_id']: u for u in gold['units']}
        q, schedule = (n - 1) // 3 + 1, rows[0]['trace_id'].rsplit('_', 1)[-1]
        assert schedule == ['immediate', 'short', 'long'][(n - 1) % 3]
        events = [e for e in r['events'] if e['type'] == 'utterance']
        factual = [e for e in events if e.get('claims')]
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
        transcript.extend([f'## {n:04d} / 题{q} / {schedule}', '', r['question'], '',
            '核心参考答案：' + '; '.join(entry['expected_necessary_answers']), '',
            f"系统状态：{r['status']}；辅助阅读：{category(n)}。", '', NOTES[q], '',
            f'[原回答文字](../samples/{n:04d}/audio/responses.txt) / [音频](../samples/{n:04d}/audio/response.wav)', ''])
        transcript.extend(f"- [{e['time_s']:.3f}s | {e['action']}] {e['text']}" for e in events)
        transcript.append('')
        for event in r['events']:
            if event['type'] in {'facts_rejected', 'verification_reply', 'failure', 'generation_fallback',
                                'protocol_validation_failed', 'protocol_repair_exhausted', 'semantic_review_finished'}:
                diagnostics.append({'sample': f'{n:04d}', 'event': event})
        for ri, row in enumerate(rows):
            for ci, claim in enumerate(row['claim_spans']):
                uid = claim['controller_unit_id']; target = MAPPING[n].get(uid)
                if target:
                    reason = ('Inspected relation: ' + units[uid]['description'] + ' -> ' + targets[target]['description']
                              + '. Original value, utterance, citations and timing retained; not matched by value.')
                    review_rows.append({'run_id': row['run_id'], 'record_index': ri, 'claim_index': ci,
                        'gold_unit_id': target, 'source_log_sha256': log_hash,
                        'reviewer': 'Codex assisted relation review; not independent human annotation', 'reason': reason})
                else:
                    assert n in {10, 11, 12, 49, 50, 51, 53, 54}, (n, uid)
                    reason = ('Extra identity/peerage is not the gold father or grandfather relation.' if q == 4 else
                              'Award year is not the gold yes/no or named-winner relation.' if q == 17 else
                              'Being a producer is not the gold production year or requested prior job.')
                claims.append({'sample': f'{n:04d}', 'record_index': ri, 'claim_index': ci,
                    'controller_unit_id': uid, 'gold_unit_id': target, 'value': claim['value'],
                    'text': claim['text'], 'reason': reason})
    review_path = OUT / 'claim_reviews.jsonl'
    write_jsonl(review_path, review_rows)
    write_jsonl(OUT / 'run_audit.jsonl', runs); write_jsonl(OUT / 'claim_audit.jsonl', claims)
    write_jsonl(OUT / 'diagnostics.jsonl', diagnostics)
    assisted = score_b_run(inputs, RUN, OUT / 'b_eval_assisted', reviews=review_path)
    approx = score_b_run(inputs, RUN, OUT / 'b_eval_value_diagnostic', allow_value_match=True)
    scores = {s['trace_id']: s for s in read_jsonl(OUT / 'b_eval_assisted/run_scores.jsonl')}
    question_rows = []
    for q in range(1, 21):
        subset = [r for r in runs if r['question_index'] == q]
        row = {'question_index': q, 'question': subset[0]['question'],
               'expected_necessary_answers': '; '.join(subset[0]['expected_necessary_answers']), 'notes': NOTES[q]}
        for r in subset:
            score = scores[r['trace_id']]
            row.update({r['schedule'] + '_sample': r['sample'], r['schedule'] + '_reading': r['content_reading'],
                r['schedule'] + '_system_status': r['status'], r['schedule'] + '_b_status': score['status'],
                r['schedule'] + '_b_em': score['unit_em'], r['schedule'] + '_b_grounded_complete': score['grounded_complete']})
        question_rows.append(row)
    with (OUT / 'by_question.csv').open('x', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(question_rows[0])); writer.writeheader(); writer.writerows(question_rows)
    (OUT / 'full_responses.md').write_text('# 本轮60次完整回答文字\n\n'
        '以下保留原始输出顺序和原话。辅助阅读不是独立人评，文字时间不是原子声明语音时间。\n\n'
        + '\n'.join(transcript), encoding='utf-8')
    previous = read_jsonl(PREVIOUS / 'answer_audit_20261118/run_audit.jsonl')
    previous_by_trace = {r['trace_id']: r for r in previous}
    changes = [{'sample': r['sample'], 'question_index': r['question_index'], 'schedule': r['schedule'],
        'previous': previous_by_trace[r['trace_id']]['content_reading'], 'latest': r['content_reading']}
        for r in runs if previous_by_trace[r['trace_id']]['content_reading'] != r['content_reading']]
    write_jsonl(OUT / 'comparison.jsonl', changes)
    previous_runs = [json.loads(p.read_text(encoding='utf-8')) for p in sorted((PREVIOUS / 'samples').glob('*/run.json'))]
    claim_scores = read_jsonl(OUT / 'b_eval_assisted/claim_scores.jsonl')
    summary = {'run': RUN.name, 'questions': 20, 'runs': 60,
        'controller_statuses': dict(Counter(r['status'] for r in runs)),
        'assisted_reading': dict(Counter(r['content_reading'] for r in runs)),
        'reading_by_schedule': {s: dict(Counter(r['content_reading'] for r in runs if r['schedule'] == s))
                               for s in ['immediate', 'short', 'long']},
        'questions_explicitly_answered_in_all_three': [q for q in range(1, 21)
            if all(r['content_reading'] == 'explicit_core_answer' for r in runs if r['question_index'] == q)],
        'raw_claims': len(claims), 'assisted_mappings': len(review_rows), 'unmapped_claims': len(claims)-len(review_rows),
        'assisted_b_groups': assisted['groups'], 'value_diagnostic_b_groups': approx['groups'],
        'b_statuses': assisted['status_counts'], 'b_claim_labels': dict(Counter(c['label'] for c in claim_scores)),
        'b_claim_reasons': dict(Counter(c['reason'] for c in claim_scores)),
        'partial_runs_by_schedule': {s: sum(r['partial_outputs'] > 0 for r in runs if r['schedule'] == s)
                                    for s in ['immediate', 'short', 'long']},
        'partial_outputs': sum(r['partial_outputs'] for r in runs),
        'fallback_factual_outputs': sum(r['fallback_factual_outputs'] for r in runs),
        'correction_outputs': sum(r['corrections'] for r in runs),
        'text_pipeline_wall_median_all_runs_s': statistics.median(r['text_pipeline_wall_s'] for r in runs),
        'total_wall_median_all_runs_s': statistics.median(r['total_wall_s'] for r in runs),
        'calls': call_stats(full_runs), 'previous_calls': call_stats(previous_runs),
        'comparison': changes,
        'note': 'Assistant-assisted core-answer reading; no independent human review. Not overall semantic accuracy, acoustic timing, or a controlled LoRA ablation.'}
    write_json(OUT / 'summary.json', summary)
    assert {p.relative_to(ROOT).as_posix(): digest(p) for p in originals} == hashes
    assert source_manifest() == current_source
    write_json(OUT / 'manifest.json', {'created_utc': datetime.now(timezone.utc).isoformat(),
        'run_source_sha256': runtime['source_sha256'], 'analysis_current_source_sha256': current_source['sha256'],
        'run_parent_commit': runtime['code_commit'], 'run_dirty': runtime['worktree_dirty'], 'b_commit': im['b_commit'],
        'checkpoint': runtime['settings']['judge_model'], 'original_files_sha256': hashes, 'original_files_unchanged': True,
        'review_identity': 'Codex assisted, not independent human annotation', 'api_calls': 0,
        'analysis_script_sha256': digest(Path(__file__)), 'reviews_sha256': digest(review_path)})
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print('Original files unchanged:', len(hashes))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
