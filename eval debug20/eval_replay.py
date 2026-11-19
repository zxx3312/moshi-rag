"""Wall-paced debug evidence replay through the existing Cascade, without gold."""
import asyncio
from collections import defaultdict
from dataclasses import replace
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import time
from urllib.parse import quote

from cascadesystem.config import Settings
from cascadesystem.controller import Cascade
from cascadesystem.llm import TinkerLLM
from cascadesystem.presentation import split_sentences
from cascadesystem.audio import SpeechOutput

from eval_data import load_b_traces
from eval_common import git, write_json, write_jsonl
from eval_common import public_settings, reauthentication, source_manifest
from eval_audio import TraceAudio


POLICY = 'cascadesystem_question_only'


class NoSearch:
    async def search(self, query):
        raise AssertionError('Trace evaluation must not invoke external search')


class TraceEvidence:
    """The scheduler owns future events. Only a due batch crosses the iterator."""
    def __init__(self, trace, started):
        self.started = started
        self.batches = defaultdict(list)
        ids = set()
        for event in trace['events']:
            uid, at, text = event.get('evidence_id'), event.get('visible_time_s'), event.get('text')
            if (not isinstance(uid, str) or not uid or uid in ids or
                    type(at) not in {int, float} or not math.isfinite(at) or
                    not isinstance(text, str) or not text.strip()):
                raise ValueError('Invalid or duplicate B trace evidence')
            title = event.get('source', {}).get('document_id')
            if not isinstance(title, str) or not title.strip():
                raise ValueError('Trace sentence needs a document title')
            ids.add(uid)
            self.batches[at].append({'evidence_id': uid, 'title': title, 'text': text,
                                    'url': 'https://trace.invalid/' + quote(trace['trace_id'], safe='') + '/' + quote(uid, safe=''),
                                    'resolved_title': title, 'entity_resolution': 'unspecified'})
        complete = trace.get('retrieval_complete_time_s')
        if complete is not None:
            if type(complete) not in {int, float} or not math.isfinite(complete) or complete < max(self.batches, default=complete):
                raise ValueError('Invalid B trace completion time')
        self.complete = complete

    async def __aiter__(self):
        times = sorted(self.batches)
        index = 0
        while index < len(times):
            await asyncio.sleep(max(0, times[index] - (time.monotonic() - self.started)))
            due, elapsed = [], time.monotonic() - self.started
            while index < len(times) and times[index] <= elapsed:
                due.extend(self.batches[times[index]])
                index += 1
            if due:
                yield due
        if self.complete is not None:
            await asyncio.sleep(max(0, self.complete - (time.monotonic() - self.started)))


def policy_rows(run, trace):
    """Keep declared facts; unknown acoustic times stay null. IDs are never aligned."""
    rows, issues = [], []
    run_id = trace['trace_id'] + '__' + POLICY + '__s0'
    for event in run.get('events', []):
        if event.get('type') != 'utterance':
            continue
        action = event.get('action')
        if action == 'Correction':
            # B cannot score retractions yet. Preserve the output but exclude the entire run.
            issues.append({'reason': 'B scorer does not implement retractions', 'sequence': event['sequence']})
            action = 'Progress'
        if action not in {'Wait', 'Backchannel', 'Progress', 'Partial Answer', 'Final Answer'}:
            raise ValueError('Unsupported cascade action in B log adapter')
        text = event.get('text', '')
        claims = []
        event_claims = event.get('claims', [])
        for claim in event.get('claims', []):
            value = claim.get('value', '')
            sentences = split_sentences(text)
            candidates = [sentence for sentence in sentences if value and value.casefold() in sentence.casefold()]
            # A repeated value or a sentence containing several declared values
            # cannot identify an atomic relation. Retain the utterance context;
            # never pick an earlier sentence about another person/relation.
            isolated = (len(candidates) == 1 and not any(
                other is not claim and other.get('value') and
                other['value'].casefold() in candidates[0].casefold() for other in event_claims))
            span = candidates[0] if isolated else text
            claims.append({'controller_unit_id': claim['unit_id'], 'text': span, 'value': value,
                           'cited_evidence_ids': claim.get('citations', []), 'start': None, 'end': None,
                           'span_basis': 'unique_value_sentence' if isolated else 'utterance_context_unaligned'})
        rows.append({**{key: trace[key] for key in ['schema_version', 'data_version', 'sample_id', 'trace_id',
                                                   'time_origin', 'clock']},
                     'run_id': run_id, 'policy': POLICY, 'seed': 0,
                     'decision_time_s': event['time_s'], 'action': action, 'text': text,
                     'evidence_snapshot_ids': event.get('evidence_snapshot_ids', []),
                     'output_start_time_s': None, 'output_end_time_s': None,
                     'claim_spans': claims, 'status': 'ok',
                     'cascade_sequence': event.get('sequence'), 'cascade_action': event.get('action'),
                     'decision_time_basis': 'controller_output_commit',
                     'audio_enabled': run.get('evaluation', {}).get('audio_enabled', False)})
    if not rows:
        rows.append({**{key: trace[key] for key in ['schema_version', 'data_version', 'sample_id', 'trace_id',
                                                   'time_origin', 'clock']},
                     'run_id': run_id, 'policy': POLICY, 'seed': 0, 'decision_time_s': 0.0,
                     'action': 'Wait', 'text': '', 'evidence_snapshot_ids': [],
                     'output_start_time_s': None, 'output_end_time_s': None, 'claim_spans': [], 'status': 'error'})
    if issues or run.get('status') in {'error', 'timeout', 'cancelled'}:
        for row in rows:
            row['status'] = 'error'
    return rows, issues


async def run_trace(trace, settings, directory, timeout_s, llm_factory=TinkerLLM, *,
                    tts='none', play=False, speech_factory=SpeechOutput):
    directory.mkdir(parents=True, exist_ok=False)
    started, events = time.monotonic(), []
    # Keep the full public context. Limits derive only from public evidence, never gold.
    settings = replace(settings, max_sources=max(1, len(trace['events'])),
                       source_chars=max([len(e['text']) for e in trace['events']] or [1]),
                       evidence_chars=max(1, sum(len(e['text']) for e in trace['events'])))
    llm = llm_factory(settings)
    audio = TraceAudio(directory / 'audio', mode=tts, play=play, started_at=started, speech_factory=speech_factory)
    cancelled = None
    with (directory / 'events.jsonl').open('x', encoding='utf-8') as stream:
        async def emit(event):
            events.append(event)
            stream.write(json.dumps(event, ensure_ascii=False) + '\n')
            stream.flush()
            await audio.submit(event)
        try:
            result = await asyncio.wait_for(Cascade(llm, NoSearch(), settings).run(
                trace['question'], emit, history=None, started_at=started,
                evidence_stream=TraceEvidence(trace, started)), timeout=timeout_s)
        except (Exception, asyncio.CancelledError) as error:
            result = {'status': 'cancelled' if isinstance(error, asyncio.CancelledError) else
                                'timeout' if isinstance(error, TimeoutError) else 'error',
                      'error_type': type(error).__name__, 'question': trace['question'], 'events': events,
                      'evidence': [e['evidence'] for e in events if e['type'] == 'evidence'],
                      'llm_calls': list(getattr(llm, 'calls', []))}
            if isinstance(error, asyncio.CancelledError):
                cancelled = error
        pipeline_wall_s = time.monotonic() - started
        audio_result = await audio.finish(cancelled=cancelled is not None)
    result['audio'] = audio_result
    result['evaluation'] = {'mode': 'b_debug_trace', 'trace_id': trace['trace_id'],
                            'sample_id': trace['sample_id'], 'total_wall_s': time.monotonic() - started,
                            'question_timeout_s': timeout_s, 'audio_enabled': tts != 'none', 'history_enabled': False,
                            'text_pipeline_wall_s': pipeline_wall_s,
                            'effective_settings': public_settings(settings),
                            'timing_kind': 'unknown', 'scheduler': 'wall-paced fixed B arrivals'}
    write_json(directory / 'run.json', result)
    if cancelled is not None:
        raise cancelled
    return result


async def run_b_debug(inputs, output, *, schedule='all', timeout_s=180, resume=False,
                      settings=None, llm_factory=TinkerLLM, tts='none', play=False, limit=None,
                      speech_factory=SpeechOutput):
    traces, data = load_b_traces(inputs)
    if schedule not in {'all', 'immediate', 'short', 'long'} or not 1 <= timeout_s <= 3600:
        raise ValueError('Invalid B debug schedule or timeout')
    traces = [t for t in traces if schedule == 'all' or t['trace_id'].endswith('_' + schedule)]
    if limit is not None:
        if type(limit) is not int or limit < 1:
            raise ValueError('--limit must be a positive question count')
        sample_ids = list(dict.fromkeys(t['sample_id'] for t in traces))[:limit]
        traces = [t for t in traces if t['sample_id'] in sample_ids]
    if tts not in {'none', 'windows'} or play and tts == 'none':
        raise ValueError('--play requires --tts windows')
    if not traces or len({t['trace_id'] for t in traces}) != len(traces):
        raise ValueError('Empty or duplicate B trace selection')
    settings = settings or Settings.from_env()
    llm_factory(settings)  # Fail credential/configuration checks before creating output.
    snapshot = source_manifest()
    identity = {'mode': 'b_debug_trace', 'split': 'debug', 'data_version': 'debug-v0',
                'b_commit': data['b_commit'], 'traces_sha256': data['files_sha256']['traces.jsonl'],
                'trace_ids': [t['trace_id'] for t in traces], 'policy': POLICY,
                'settings': public_settings(settings), 'source_sha256': snapshot['sha256'],
                'timeout_s': timeout_s, 'timing_kind': 'unknown', 'schedule': schedule,
                'audio': {'tts': tts, 'play': play}}
    output = Path(output)
    if resume:
        old = json.loads((output / 'manifest.json').read_text(encoding='utf-8'))
        if any(old.get(key) != value for key, value in identity.items()):
            raise ValueError('B resume refused: inputs, code, selection or settings changed')
    else:
        output.mkdir(parents=True, exist_ok=False)
        write_json(output / 'manifest.json', {**identity, 'code_commit': git('rev-parse', 'HEAD').decode().strip(),
                                            'worktree_dirty': bool(git('status', '--porcelain')),
                                            'started_at_utc': datetime.now(timezone.utc).isoformat(),
                                            'note': 'Debug controlled evidence; optional local audio; no formal speech-claim alignment.'})
        write_json(output / 'source-manifest.json', snapshot)
    print('B replay directory: ' + str(output.resolve()), flush=True)
    for index, trace in enumerate(traces, 1):
        folder = output / 'samples' / f'{index:04d}'
        if resume and (folder / 'run.json').exists():
            result = json.loads((folder / 'run.json').read_text(encoding='utf-8'))
            if result.get('evaluation', {}).get('trace_id') != trace['trace_id']:
                raise ValueError('B resume result/trace mismatch')
        else:
            if tts != 'none':
                print(f'[{index}/{len(traces)}] Question: {trace["question"]}', flush=True)
            result = await run_trace(trace, settings, folder, timeout_s, llm_factory,
                                     tts=tts, play=play, speech_factory=speech_factory)
        logs, issues = policy_rows(result, trace)
        write_jsonl(folder / 'policy_log.jsonl', logs)
        write_json(folder / 'adapter_issues.json', issues)
        print(f'[{index}/{len(traces)}] {trace["trace_id"]}: {result["status"]}; '
              f'{result["evaluation"]["total_wall_s"]:.2f}s', flush=True)
        if result.get('audio', {}).get('enabled') and result['audio']['status'] != 'ok':
            print('Audio error: ' + '; '.join(result['audio'].get('errors', ['unknown audio failure'])), flush=True)
            print('Stopped after audio failure. See samples/.../audio/audio_index.json; remaining traces are missing.', flush=True)
            break
        if any(e.get('type') == 'failure' and reauthentication(e.get('error', '')) for e in result.get('events', [])):
            print('Stopped after authentication/permission failure; remaining traces are missing.', flush=True)
            break
    all_rows = []
    for index in range(1, len(traces) + 1):
        path = output / 'samples' / f'{index:04d}' / 'policy_log.jsonl'
        if path.exists():
            all_rows.extend(json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip())
    write_jsonl(output / 'policy_log.jsonl', all_rows)
    if tts != 'none':
        audio_results = []
        for index in range(1, len(traces) + 1):
            path = output / 'samples' / f'{index:04d}' / 'run.json'
            if path.exists():
                run = json.loads(path.read_text(encoding='utf-8'))
                audio_results.append({'trace_id': run.get('evaluation', {}).get('trace_id'),
                                      'status': run.get('audio', {}).get('status', 'missing'),
                                      'wave': run.get('audio', {}).get('wave', {}).get('path')})
        write_json(output / 'audio_summary.json', {'runs': audio_results,
                   'failed_runs': sum(r['status'] != 'ok' for r in audio_results)})
    return output

