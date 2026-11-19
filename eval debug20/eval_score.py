"""Apply B original value, support, dependency and review rules without model calls."""
import json
from pathlib import Path

from eval_common import digest, read_jsonl, write_json, write_jsonl
from eval_data import load_b_traces, load_evaluator


def score_b_run(inputs, run, output, *, reviews=None, allow_value_match=False):
    """Invoke B's actual evaluator with unknown speech timing and no aligned IDs."""
    inputs, run, output = Path(inputs), Path(run), Path(output)
    traces, manifest = load_b_traces(inputs)
    if digest(inputs / 'gold.jsonl') != manifest['files_sha256']['gold.jsonl']:
        raise ValueError('B debug gold hash mismatch')
    runtime = json.loads((run / 'manifest.json').read_text(encoding='utf-8'))
    if (runtime.get('mode') != 'b_debug_trace' or runtime.get('b_commit') != manifest['b_commit'] or
            runtime.get('traces_sha256') != manifest['files_sha256']['traces.jsonl']):
        raise ValueError('B scoring requires a matching B trace run, not live Wikipedia results')
    selected = set(runtime['trace_ids'])
    traces = [t for t in traces if t['trace_id'] in selected]
    if len(traces) != len(selected):
        raise ValueError('Run names an unknown or duplicate trace')
    gold = read_jsonl(inputs / 'gold.jsonl')
    logs = read_jsonl(run / 'policy_log.jsonl')
    review_rows = read_jsonl(reviews) if reviews else []
    for row in review_rows:
        if row.get('source_log_sha256') != digest(run / 'policy_log.jsonl'):
            raise ValueError('Reviewed mappings must name the unchanged source log SHA256')
    evaluator, hashes = load_evaluator(manifest['b_commit'])
    scores, claims = evaluator.evaluate_corpus(
        traces, gold, logs, review_rows=review_rows, allow_value_match=allow_value_match,
        timing_kind='unknown', expected_policies=[runtime['policy']], expected_seed=0)
    summary = evaluator.summarize(scores, traces)
    config = {'b_commit': manifest['b_commit'], 'evaluator_sha256': hashes,
              'runner_commit': runtime['code_commit'], 'source_sha256': runtime['source_sha256'],
              'timing_kind': 'unknown', 'aligned_policies': [], 'allow_value_match': allow_value_match,
              'mapping_scope': 'approximate value mapping' if allow_value_match else 'checked mappings only',
              'inputs_sha256': {str(p): digest(p) for p in [inputs / 'traces.jsonl', inputs / 'gold.jsonl',
                                                          run / 'policy_log.jsonl']}}
    if reviews:
        config['reviews_sha256'] = digest(reviews)
    summary['config'] = config
    output.mkdir(parents=True, exist_ok=False)
    write_jsonl(output / 'run_scores.jsonl', scores)
    write_jsonl(output / 'claim_scores.jsonl', claims)
    write_jsonl(output / 'review_queue.jsonl', [c for c in claims if c['label'] == 'NEEDS_REVIEW'])
    write_jsonl(output / 'validation_issues.jsonl', [{'run_id': r['run_id'], **issue}
                                                   for r in scores for issue in r['validation_issues']])
    write_json(output / 'summary.json', summary)
    write_json(output / 'evaluation_config.json', config)
    (output / 'summary.md').write_text(evaluator.make_report(summary), encoding='utf-8')
    return summary

