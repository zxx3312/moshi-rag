"""Explicit final-run entry for the revised B 300-question/900-trace set.

No data or model access occurs for --help. Reserved data requires --final-run.
The original Debug20 implementation and GPT judge prompts are unchanged.
"""
import argparse
import asyncio
from collections import Counter, defaultdict
from dataclasses import replace
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import uuid

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(REPO / 'eval debug20'))

from cascadesystem.audio import AudioError
from cascadesystem.config import Settings
from cascadesystem.llm import TinkerLLM
from cascadesystem.training.engine import checkpoint_info
from eval_common import digest, git, public_settings, read_jsonl, reauthentication, write_json, write_jsonl
from eval_common import source_manifest as shared_source_manifest
from eval_data import frozen_commit, load_evaluator
from eval_replay import TraceEvidence, policy_rows, run_trace

B_COMMIT = 'ea390574eadd301354d5de46f0d28d328cca5bad'
TRACE_DIR = 'b_work/test_set/traces/eval_revised_v1'
SOURCES = {'public/traces.jsonl': TRACE_DIR + '/traces.jsonl',
           'private/source_gold_0.jsonl': 'b_work/test_set/revisions/batch01_05_v1/gold.jsonl',
           'private/source_gold_1.jsonl': 'b_work/test_set/revisions/batch06_10_v1/gold.jsonl'}
MODE = 'b_final_revised_trace'
POLICY = 'cascade_gpt120_lora_question_only'
INPUTS = ROOT / 'artifacts/inputs/eval-revised-v1'
JUDGE_RUN = REPO / 'cascadesystem/artifacts/training/runs/gpt120-judge-v1'
TRACE_KEYS = {'schema_version', 'data_version', 'sample_id', 'trace_id', 'trace_type',
              'time_origin', 'clock', 'question', 'events', 'retrieval_complete_time_s'}
EVENT_KEYS = {'evidence_id', 'scheduled_time_s', 'visible_time_s', 'source', 'text'}


def authorize(final_run):
    if not final_run:
        raise ValueError('Reserved evaluation requires explicit --final-run. '
                         'CLAUDE.md permits F1 only when this is the final run; use Debug20 for development.')


def parse_rows(raw):
    return [json.loads(line) for line in raw.decode('utf-8-sig').splitlines() if line.strip()]


def runtime_trace(trace):
    # B's revised builder retains blank sentences. They remain in the frozen
    # input/scorer, while the Cascade already accepts only nonblank sources.
    # Keep the ORIGINAL completion time, even if its last event was blank.
    return {**trace, 'events': [e for e in trace['events'] if e['text'].strip()]}


def validate_public(traces):
    """Validate public shape/arrivals without reading any gold or future model input."""
    groups, ids = defaultdict(dict), set()
    expected = {'immediate': {0.0}, 'short': {1.0, 3.0}, 'long': {2.0, 8.0}}
    for trace in traces:
        if (set(trace) != TRACE_KEYS or trace.get('schema_version') != '1.0' or
                trace.get('trace_type') != 'controlled_mock' or trace.get('clock') != 'simulated' or
                trace.get('time_origin') != 'question_end' or
                not isinstance(trace.get('question'), str) or not trace['question'].strip()):
            raise ValueError('Unexpected revised public trace shape/type; reject possible gold leakage')
        tid, sid = trace['trace_id'], trace['sample_id']
        if not isinstance(tid, str) or not isinstance(sid, str) or not sid or tid in ids:
            raise ValueError('Missing or duplicate revised trace identity')
        schedule = tid.rsplit('_', 1)[-1]
        if schedule not in expected or schedule in groups[sid]:
            raise ValueError('Duplicate or unknown arrival schedule')
        if not trace['events'] or any(set(e) != EVENT_KEYS for e in trace['events']):
            raise ValueError('Unexpected public evidence fields')
        times = {e['visible_time_s'] for e in trace['events']}
        if (not times <= expected[schedule] or
                any(e['scheduled_time_s'] != e['visible_time_s'] for e in trace['events']) or
                trace['retrieval_complete_time_s'] != max(times)):
            raise ValueError('Revised evidence arrival schedule differs from the fixed B definition')
        evidence_ids = [e['evidence_id'] for e in trace['events']]
        if (any(not isinstance(eid, str) or not eid for eid in evidence_ids) or
                len(evidence_ids) != len(set(evidence_ids)) or
                any(not isinstance(e['text'], str) for e in trace['events'])):
            raise ValueError('Invalid revised sentence identity or text')
        for event in trace['events']:
            source = event['source']
            if (not isinstance(source, dict) or
                    set(source) != {'dataset', 'document_id', 'document_index', 'sentence_index'} or
                    not isinstance(source.get('document_id'), str) or not source['document_id'].strip()):
                raise ValueError('Unexpected source fields; reject possible gold leakage')
        TraceEvidence(runtime_trace(trace), 0)
        groups[sid][schedule] = trace
        ids.add(tid)
    if len(groups) != 300 or len(traces) != 900:
        raise ValueError('Expected exactly 300 revised questions and 900 traces')
    for schedules in groups.values():
        if set(schedules) != set(expected) or len({t['question'] for t in schedules.values()}) != 1:
            raise ValueError('Each question must have the same question in all three schedules')
        signatures = [{e['evidence_id']: (e['text'], e['source']) for e in t['events']}
                      for t in schedules.values()]
        if any(s != signatures[0] for s in signatures[1:]):
            raise ValueError('Evidence content differs between schedules')
    return {'questions': 300, 'traces': 900,
            'schedules': dict(Counter(t['trace_id'].rsplit('_', 1)[-1] for t in traces))}


def prepare(output, *, ref=B_COMMIT, final_run=False):
    authorize(final_run)  # Before ANY data read, git extraction or directory creation.
    output = Path(output)
    if output.exists():
        raise ValueError('Input destination exists; reuse it for run, do not overwrite final data')
    commit = frozen_commit(ref)
    raw = {name: git('show', commit + ':' + source) for name, source in SOURCES.items()}
    traces = parse_rows(raw['public/traces.jsonl'])
    counts = validate_public(traces)
    gold_bytes = b''.join(raw[name].rstrip() + b'\n' for name in
                          ['private/source_gold_0.jsonl', 'private/source_gold_1.jsonl'])
    gold = parse_rows(gold_bytes)
    evaluator, hashes = load_evaluator(commit)
    evaluator.prepare_inputs(traces, gold)
    if len(gold) != 300 or sum(len(g['units']) for g in gold) != 817:
        raise ValueError('Revised gold counts differ from the documented frozen set')
    upstream = git('show', commit + ':' + TRACE_DIR + '/manifest.json')
    json.loads(upstream)
    raw['private/gold.jsonl'] = gold_bytes
    raw['source_data_manifest.json'] = upstream
    for name, content in raw.items():
        path = output / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    manifest = {'mode': MODE, 'split': 'eval_reserved', 'b_commit': commit, **counts,
                'source_paths': SOURCES, 'evaluator_sha256': hashes,
                'files_sha256': {name: digest(output / name) for name in raw},
                'note': 'Explicit final evaluation; revised gold only, no original batch gold.'}
    write_json(output / 'manifest.json', manifest)
    return manifest


def load_public(inputs, *, final_run=False):
    authorize(final_run)
    inputs = Path(inputs)
    manifest = json.loads((inputs / 'manifest.json').read_text(encoding='utf-8'))
    if manifest.get('mode') != MODE or manifest.get('split') != 'eval_reserved':
        raise ValueError('Expected an explicitly prepared revised final-evaluation bundle')
    if digest(inputs / 'public/traces.jsonl') != manifest['files_sha256']['public/traces.jsonl']:
        raise ValueError('Final public trace hash mismatch')
    traces = read_jsonl(inputs / 'public/traces.jsonl')
    validate_public(traces)
    return traces, manifest  # Deliberately do not open private/ or gold.


def source_manifest():
    shared = shared_source_manifest()
    files = dict(shared['files'])
    for path in sorted(ROOT.rglob('*.py')):
        if not {'artifacts', '__pycache__'}.intersection(path.parts):
            files[path.relative_to(REPO).as_posix()] = digest(path)
    identity = hashlib.sha256(json.dumps(files, sort_keys=True).encode()).hexdigest()
    return {'sha256': identity, 'files': files}


async def one_trace(trace, settings, folder, timeout, factory, tts, play):
    try:
        await run_trace(runtime_trace(trace), settings, folder, timeout, factory, tts=tts, play=play)
    finally:
        # Reuse the unchanged trace engine, then label this NEW output's actual scope.
        path = folder / 'run.json'
        if path.is_file():
            result = json.loads(path.read_text(encoding='utf-8'))
            result['evaluation']['mode'] = MODE
            result['evaluation']['split'] = 'eval_reserved'
            result['evaluation']['empty_evidence_sentences_ignored'] = sum(
                not event['text'].strip() for event in trace['events'])
            write_json(path, result)
    return result


def continuation_plan(parent, output, identity, snapshot):
    """Allow an explicitly separate operational continuation, never a hidden code mismatch."""
    parent, output = Path(parent).resolve(), Path(output).resolve()
    if parent == output or parent.is_relative_to(output) or output.is_relative_to(parent):
        raise ValueError('Continuation output must be a separate new directory, outside the parent run')
    if output.exists():
        raise ValueError('Continuation output exists; resume it with --resume instead')
    old = json.loads((parent / 'manifest.json').read_text(encoding='utf-8'))
    old_source = json.loads((parent / 'source-manifest.json').read_text(encoding='utf-8'))
    old_hash = hashlib.sha256(json.dumps(old_source['files'], sort_keys=True).encode()).hexdigest()
    if old_source.get('sha256') != old_hash or old.get('source_sha256') != old_hash:
        raise ValueError('Parent source manifest identity is inconsistent')
    for key, value in identity.items():
        if key not in {'source_sha256', 'audio_error_policy'} and old.get(key) != value:
            raise ValueError('Continuation refused: parent data, model/checkpoint or settings differ: ' + key)
    protected = {name: value for name, value in snapshot['files'].items()
                 if name.startswith(('cascadesystem/', 'eval debug20/'))}
    old_protected = {name: value for name, value in old_source['files'].items()
                     if name.startswith(('cascadesystem/', 'eval debug20/'))}
    if not protected or old_protected != protected:
        raise ValueError('Continuation refused: shared model/controller/prompt/scorer code changed')
    samples = []
    for folder in sorted((parent / 'samples').iterdir()):
        if not folder.is_dir() or not folder.name.isdigit():
            continue
        index = int(folder.name)
        path = folder / 'run.json'
        if not 1 <= index <= len(identity['trace_ids']) or not path.is_file():
            raise ValueError('Parent contains an unfinished or out-of-range sample; preserve it and inspect separately')
        result = json.loads(path.read_text(encoding='utf-8'))
        if result.get('evaluation', {}).get('trace_id') != identity['trace_ids'][index - 1]:
            raise ValueError('Parent saved sample/trace identity differs')
        samples.append({'sample': folder.name, 'run_sha256': digest(path)})
    if not samples:
        raise ValueError('Parent has no saved attempts to continue')
    return {'parent': str(parent), 'parent_manifest_sha256': digest(parent / 'manifest.json'),
            'parent_source_sha256': old_hash, 'current_source_sha256': snapshot['sha256'],
            'shared_method_source_unchanged': True, 'inherited_samples': samples,
            'note': 'Operational continuation only; inherited successes and failures are preserved without API retries.'}


def stop_after_result(result, *, reused=False, continue_on_audio_error=False):
    audio = result.get('audio', {})
    audio_failed = audio.get('enabled') and audio.get('status') != 'ok'
    if reused:
        if audio_failed:
            print('Retained saved audio failure; moving to unsaved traces without retrying this answer.', flush=True)
        return False
    authentication = [e.get('error', '') for e in result.get('events', [])
                      if e.get('type') == 'failure' and reauthentication(e.get('error', ''))]
    if authentication:
        print('Stopped after API authentication/permission failure: ' + '; '.join(authentication), flush=True)
        return True
    if audio_failed:
        print('Audio failure retained: ' + '; '.join(audio.get('errors') or [audio.get('status', 'unknown')]), flush=True)
        if continue_on_audio_error:
            print('Continuing text evaluation; this audio failure remains in audio_summary.json.', flush=True)
        else:
            print('Stopped after audio failure; remaining traces stay missing.', flush=True)
            return True
    return False


async def run_final(inputs, output, settings, *, final_run=False, resume=False, timeout=180,
                    tts='none', play=False, factory=TinkerLLM, continue_from=None,
                    continue_on_audio_error=False):
    authorize(final_run)
    if resume and continue_from is not None:
        raise ValueError('Use either --resume or --continue-from, not both')
    if (not 1 <= timeout <= 3600 or tts not in {'none', 'windows'} or
            play and tts != 'windows' or tts == 'windows' and os.name != 'nt'):
        raise ValueError('Invalid timeout/audio settings; Windows TTS requires native Windows')
    traces, data = load_public(inputs, final_run=True)
    factory(settings)  # Credentials/config preflight before creating an output directory.
    snapshot = source_manifest()
    identity = {'mode': MODE, 'split': 'eval_reserved', 'b_commit': data['b_commit'],
        'traces_sha256': data['files_sha256']['public/traces.jsonl'],
        'trace_ids': [t['trace_id'] for t in traces], 'policy': POLICY,
        'settings': public_settings(settings), 'source_sha256': snapshot['sha256'],
        'timeout_s': timeout, 'timing_kind': 'unknown', 'audio': {'tts': tts, 'play': play},
        'audio_error_policy': 'continue' if continue_on_audio_error else 'stop'}
    output = Path(output)
    adoption = continuation_plan(continue_from, output, identity, snapshot) if continue_from is not None else None
    if resume:
        old = json.loads((output / 'manifest.json').read_text(encoding='utf-8'))
        if any(old.get(k) != v for k, v in identity.items()):
            raise ValueError('Final resume refused: source, checkpoint, data or settings changed')
    else:
        output.mkdir(parents=True, exist_ok=False)
        if adoption is not None:
            parent = Path(adoption['parent'])
            print(f"Copying {len(adoption['inherited_samples'])} saved attempts into the new continuation directory...", flush=True)
            for saved in adoption['inherited_samples']:
                shutil.copytree(parent / 'samples' / saved['sample'], output / 'samples' / saved['sample'])
                if digest(output / 'samples' / saved['sample'] / 'run.json') != saved['run_sha256']:
                    raise ValueError('Copied parent sample identity changed; no inference has started')
            write_json(output / 'continuation.json', adoption)
            shutil.copy2(parent / 'manifest.json', output / 'parent-manifest.json')
            shutil.copy2(parent / 'source-manifest.json', output / 'parent-source-manifest.json')
        write_json(output / 'manifest.json', {**identity,
            'code_commit': git('rev-parse', 'HEAD').decode().strip(),
            'worktree_dirty': bool(git('status', '--porcelain')),
            'started_at_utc': datetime.now(timezone.utc).isoformat()})
        write_json(output / 'source-manifest.json', snapshot)
    print('Final GPT+LoRA directory: ' + str(output.resolve()), flush=True)
    for index, trace in enumerate(traces, 1):
        folder = output / 'samples' / f'{index:04d}'
        path = folder / 'run.json'
        reused = (resume or adoption is not None) and path.exists()
        if reused:
            result = json.loads(path.read_text(encoding='utf-8'))
            if result.get('evaluation', {}).get('trace_id') != trace['trace_id']:
                raise ValueError('Saved sample identity differs from final trace selection')
        else:
            print(f'[{index}/900] Question: {trace["question"]}', flush=True)
            result = await one_trace(trace, settings, folder, timeout, factory, tts, play)
        rows, issues = policy_rows(result, trace)
        for row in rows:
            row['policy'] = POLICY
            row['run_id'] = trace['trace_id'] + '__' + POLICY + '__s0'
        write_jsonl(folder / 'policy_log.jsonl', rows)
        write_json(folder / 'adapter_issues.json', issues)
        print(f'[{index}/900] {trace["trace_id"]}: {result["status"]}', flush=True)
        if stop_after_result(result, reused=reused, continue_on_audio_error=continue_on_audio_error):
            break
    rows = []
    for index in range(1, 901):
        path = output / 'samples' / f'{index:04d}' / 'policy_log.jsonl'
        if path.exists():
            rows.extend(read_jsonl(path))
    write_jsonl(output / 'policy_log.jsonl', rows)
    if tts != 'none':
        audio_runs = []
        for index in range(1, 901):
            path = output / 'samples' / f'{index:04d}' / 'run.json'
            if path.exists():
                result = json.loads(path.read_text(encoding='utf-8'))
                audio_runs.append({'trace_id': result['evaluation']['trace_id'],
                                   'status': result.get('audio', {}).get('status', 'missing')})
        write_json(output / 'audio_summary.json', {'runs': audio_runs,
            'failed_runs': sum(r['status'] != 'ok' for r in audio_runs)})
    return output


def score(inputs, run, output, *, final_run=False, allow_value_match=False, reviews=None):
    authorize(final_run)
    inputs, run, output = Path(inputs), Path(run), Path(output)
    traces, data = load_public(inputs, final_run=True)
    runtime = json.loads((run / 'manifest.json').read_text(encoding='utf-8'))
    if (runtime.get('mode') != MODE or runtime.get('b_commit') != data['b_commit'] or
            runtime.get('traces_sha256') != data['files_sha256']['public/traces.jsonl'] or
            runtime.get('trace_ids') != [t['trace_id'] for t in traces]):
        raise ValueError('Final scorer requires a matching complete 900-trace selection')
    if digest(inputs / 'private/gold.jsonl') != data['files_sha256']['private/gold.jsonl']:
        raise ValueError('Revised final gold hash mismatch')
    gold = read_jsonl(inputs / 'private/gold.jsonl')  # Scoring only, never sent to the provider.
    logs = read_jsonl(run / 'policy_log.jsonl')
    review_rows = read_jsonl(reviews) if reviews else []
    if any(r.get('source_log_sha256') != digest(run / 'policy_log.jsonl') for r in review_rows):
        raise ValueError('Review mappings must bind the exact source log hash')
    evaluator, hashes = load_evaluator(data['b_commit'])
    scores, claims = evaluator.evaluate_corpus(traces, gold, logs, review_rows=review_rows,
        allow_value_match=allow_value_match, timing_kind='unknown', expected_policies=[POLICY], expected_seed=0)
    summary = evaluator.summarize(scores, traces)
    summary['config'] = {'b_commit': data['b_commit'], 'evaluator_sha256': hashes,
        'runner_commit': runtime['code_commit'], 'source_sha256': runtime['source_sha256'],
        'timing_kind': 'unknown', 'aligned_policies': [], 'allow_value_match': allow_value_match,
        'mapping_scope': 'B approximate value matching diagnostic' if allow_value_match else 'checked mappings only',
        'inputs_sha256': {str(p): digest(p) for p in [inputs / 'public/traces.jsonl',
                          inputs / 'private/gold.jsonl', run / 'policy_log.jsonl']}}
    output.mkdir(parents=True, exist_ok=False)
    for name, rows in [('run_scores', scores), ('claim_scores', claims),
                       ('review_queue', [c for c in claims if c['label'] == 'NEEDS_REVIEW'])]:
        write_jsonl(output / (name + '.jsonl'), rows)
    write_json(output / 'summary.json', summary)
    write_json(output / 'evaluation_config.json', summary['config'])
    (output / 'summary.md').write_text(evaluator.make_report(summary), encoding='utf-8')
    return summary


def arguments(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    prep = sub.add_parser('prepare', help='Explicitly export revised final inputs, without running models')
    prep.add_argument('--ref', default=B_COMMIT)
    prep.add_argument('--output', type=Path, default=INPUTS)
    running = sub.add_parser('run', help='Run current GPT-120B with the saved judge LoRA over all 900 traces')
    running.add_argument('--judge-run', type=Path, default=JUDGE_RUN)
    running.add_argument('--output', type=Path)
    running.add_argument('--timeout', type=float, default=180)
    running.add_argument('--resume', action='store_true')
    running.add_argument('--continue-from', type=Path, help='Copy all saved attempts into a separate new run after verifying unchanged method/model/data')
    running.add_argument('--continue-on-audio-error', action='store_true', help='Retain synthesis failures and continue text evaluation; authentication failures still stop')
    running.add_argument('--tts', choices=['none', 'windows'], default='none')
    running.add_argument('--play', action='store_true')
    scoring = sub.add_parser('score', help='Score saved predictions using original B rules, without API calls')
    scoring.add_argument('--run', type=Path, required=True)
    scoring.add_argument('--output', type=Path, required=True)
    scoring.add_argument('--reviews', type=Path)
    for command in [running, scoring]:
        command.add_argument('--inputs', type=Path, default=INPUTS)
        command.add_argument('--allow-value-match', action='store_true', help='B approximate mapping diagnostic, not independent semantic review')
    for command in [prep, running, scoring]:
        command.add_argument('--final-run', action='store_true', help='Explicit acknowledgment: this is final evaluation, not development')
    return parser.parse_args(argv)


def main(args):
    authorize(args.final_run)
    audio_failed = False
    if args.command == 'prepare':
        manifest = prepare(args.output, ref=args.ref, final_run=True)
        print(f"Prepared {manifest['questions']} questions / {manifest['traces']} traces; no model calls.")
        return 0
    if args.command == 'score':
        report = args.output
        summary = score(args.inputs, args.run, report, final_run=True,
                        allow_value_match=args.allow_value_match, reviews=args.reviews)
    else:
        if args.resume and args.continue_from is not None:
            raise ValueError('Use either --resume or --continue-from, not both')
        if args.continue_from is not None and args.output is None:
            raise ValueError('--continue-from requires a separate new --output directory')
        if args.resume and args.output is None:
            raise ValueError('--resume requires the original --output directory')
        metadata = checkpoint_info(args.judge_run)
        if metadata.get('smoke'):
            raise ValueError('A smoke-test checkpoint is not a final-evaluation checkpoint')
        settings = Settings.from_env()
        if settings.model != 'openai/gpt-oss-120b':
            raise ValueError('This entry requires CASCADE_MODEL=openai/gpt-oss-120b')
        settings = replace(settings, judge_model=metadata['checkpoint'], judge_reasoning_effort='low')
        output = args.output or ROOT / 'artifacts/runs' / (
            datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:8])
        directory = asyncio.run(run_final(args.inputs, output, settings, final_run=True,
            resume=args.resume, timeout=args.timeout, tts=args.tts, play=args.play,
            continue_from=args.continue_from, continue_on_audio_error=args.continue_on_audio_error))
        report = directory / 'b_eval'
        if report.exists():
            report = directory / ('b_eval-' + uuid.uuid4().hex[:8])
        summary = score(args.inputs, directory, report, final_run=True, allow_value_match=args.allow_value_match)
        if args.tts != 'none':
            audio_failed = bool(json.loads((directory / 'audio_summary.json').read_text(encoding='utf-8'))['failed_runs'])
    print('B status: ' + json.dumps(summary['status_counts']))
    print('B report: ' + str((report / 'summary.md').resolve()))
    print('Pending mappings remain unknown. Approximate value matching is not independent human review.')
    return int(audio_failed or any(k in summary['status_counts'] for k in ['error', 'invalid', 'missing']))


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    try:
        raise SystemExit(main(arguments()))
    except KeyboardInterrupt:
        print('Cancelled; saved attempts are retained. Resume only with the same frozen settings.', file=sys.stderr)
        raise SystemExit(130)
    except (AudioError, ValueError, OSError, KeyError, json.JSONDecodeError, subprocess.CalledProcessError) as error:
        message = str(error) if isinstance(error, (ValueError, AudioError)) else type(error).__name__
        print('Final evaluation setup failed: ' + message, file=sys.stderr)
        raise SystemExit(2)
