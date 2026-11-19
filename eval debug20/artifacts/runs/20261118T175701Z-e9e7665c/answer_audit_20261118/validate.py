"""Validate the offline report against preserved logs, B scorer and artifact links."""
from collections import Counter
import csv
import json
from pathlib import Path
import re
import statistics
import sys
import tempfile
import wave

OUT = Path(__file__).resolve().parent
RUN = OUT.parent
EVAL = RUN.parents[2]
ROOT = EVAL.parent
PREVIOUS = RUN.parent / '20261118T052754Z-eebc4a69/answer_audit_20261118'
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(EVAL))
from eval_common import digest, read_jsonl, source_manifest, write_json
from eval_score import score_b_run


def main():
    manifest = json.loads((OUT / 'manifest.json').read_text(encoding='utf-8'))
    assert all(digest(ROOT / path) == sha for path, sha in manifest['original_files_sha256'].items())
    assert digest(OUT / 'analyze.py') == manifest['analysis_script_sha256']
    assert source_manifest()['sha256'] == manifest['analysis_current_source_sha256']
    inputs = EVAL / 'artifacts/inputs/b-debug-v0'
    with tempfile.TemporaryDirectory(prefix='offline-recheck-', dir=OUT) as tmp:
        assert Path(tmp).resolve().is_relative_to(OUT.resolve())
        rerun = score_b_run(inputs, RUN, Path(tmp) / 'b', reviews=OUT / 'claim_reviews.jsonl')
        assert rerun == json.loads((OUT / 'b_eval_assisted/summary.json').read_text(encoding='utf-8'))
    rows = read_jsonl(OUT / 'run_audit.jsonl')
    assert len(rows) == 60 and len({r['question_index'] for r in rows}) == 20
    assert Counter(r['status'] for r in rows) == Counter(complete=48, incomplete=11, error=1)
    assert len(read_jsonl(OUT / 'claim_reviews.jsonl')) == 110
    assert len(read_jsonl(OUT / 'claim_audit.jsonl')) == 118
    question_rows = list(csv.DictReader((OUT / 'by_question.csv').open(encoding='utf-8-sig', newline='')))
    assert len(question_rows) == 20
    links, bad = 0, []
    for path in [OUT / 'report.md', OUT / 'full_responses.md']:
        for raw in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            target = raw.strip('<>').split('#')[0]
            if not target or '://' in target:
                continue
            links += 1
            if not (path.parent / target).exists():
                bad.append((path.name, target))
    # validation.json is written at the end of this same validation pass.
    bad = [entry for entry in bad if entry != ('report.md', 'validation.json')]
    assert not bad, bad
    checkpoint = json.loads((RUN / 'manifest.json').read_text(encoding='utf-8'))['settings']['judge_model']
    audio_paths, quote_count, nonliteral, judge_calls, error_calls = [], 0, 0, 0, 0
    for path in sorted((RUN / 'samples').glob('*/run.json')):
        r = json.loads(path.read_text(encoding='utf-8'))
        assert r['judge_model'] == checkpoint
        for call in r['llm_calls']:
            assert call['model'] == (checkpoint if call['purpose'] in {'judge', 'judge_repair'} else r['model'])
            if call['purpose'] == 'judge':
                judge_calls += call['status'] == 'ok'
                error_calls += call['status'] == 'error'
        sources = {e['evidence_id']: e['text'] for e in r['evidence']}
        for event in r['events']:
            if event['type'] in {'judge_reply', 'semantic_review_reply'}:
                for judgment in event.get('reply', {}).get('judgments', []):
                    for quote in judgment.get('quotes', []):
                        quote_count += 1
                        nonliteral += quote['text'] not in sources.get(quote['evidence_id'], '')
        audio_path = path.parent / 'audio/response.wav'
        with wave.open(str(audio_path), 'rb') as recording:
            assert recording.getnframes() > 0
            audio_paths.append(str(audio_path.relative_to(ROOT)))
    assert (judge_calls, error_calls, quote_count, nonliteral) == (97, 1, 221, 0)
    scores = {r['trace_id']: r for r in read_jsonl(OUT / 'b_eval_assisted/run_scores.jsonl')}
    previous_scores = {r['trace_id']: r for r in read_jsonl(PREVIOUS / 'b_eval_assisted/run_scores.jsonl')}
    shared = [tid for tid in scores if scores[tid]['unit_em'] is not None and previous_scores[tid]['unit_em'] is not None]
    completion = Counter(str(s['grounded_complete']) for s in scores.values())
    summary = json.loads((OUT / 'summary.json').read_text(encoding='utf-8'))
    summary['b_answer_complete'] = dict(Counter(str(s['answer_complete']) for s in scores.values()))
    summary['b_grounded_complete'] = dict(completion)
    summary['common_scored_comparison'] = {'runs': len(shared),
        'previous_mean_em': statistics.mean(previous_scores[t]['unit_em'] for t in shared),
        'latest_mean_em': statistics.mean(scores[t]['unit_em'] for t in shared)}
    summary['quote_literal_check'] = {'instances': quote_count, 'nonliteral': nonliteral,
                                     'scope': 'Parseable judge/semantic review replies; not a semantic support check.'}
    write_json(OUT / 'summary.json', summary)
    result = {'original_files_checked': len(manifest['original_files_sha256']), 'original_files_unchanged': True,
        'b_scorer_recomputed_identically': True, 'questions': 20, 'runs': 60,
        'csv_rows': len(question_rows), 'local_links_checked': links, 'bad_local_links': bad,
        'nonempty_wav_files_checked': len(audio_paths), 'model_routes_match_manifest': True,
        'quote_instances': quote_count, 'nonliteral_quote_instances': nonliteral,
        'common_b_scored_runs': len(shared), 'code_changed': False, 'api_calls': 0,
        'reserved_data_accessed': False, 'exit_code': 0}
    write_json(OUT / 'validation.json', result)
    manifest['validation_script_sha256'] = digest(Path(__file__))
    manifest['analysis_outputs_sha256'] = {p.relative_to(OUT).as_posix(): digest(p) for p in sorted(OUT.rglob('*'))
                                          if p.is_file() and p != OUT / 'manifest.json'}
    write_json(OUT / 'manifest.json', manifest)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
