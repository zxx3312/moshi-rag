"""Training/checkpoint lifecycle and held-out judge evaluation, with injectable SDK."""
from collections import Counter
import asyncio
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import random
import re
import time
import uuid

from ..models import Evidence, Unit, validate_judgments
from ..transport import ProviderError
from .data import DEFAULT_DATA, ROOT, git, load_prepared, prompt_hash, sha, write_json, write_rows
from .sdk import BASE_MODEL, RENDERER

DEFAULT_RUNS = ROOT / 'cascadesystem/artifacts/training/runs'


def source_identity():
    files = {}
    for path in sorted((ROOT / 'cascadesystem').rglob('*.py')):
        if not {'artifacts', '.venv', '__pycache__'}.intersection(path.parts):
            files[path.relative_to(ROOT).as_posix()] = sha(path.read_bytes())
    return sha(json.dumps(files, sort_keys=True).encode())


def new_run():
    return DEFAULT_RUNS / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:8])


def encoded_rows(backend, rows, max_length, max_target_tokens):
    kept, excluded = [], Counter()
    for index, row in enumerate(rows):
        encoded = backend.encode(row)
        tokens, weights = encoded['tokens'], encoded['weights']
        if len(tokens) != len(weights) or len(tokens) < 2 or not all(w in {0, 1, 0.0, 1.0} for w in weights):
            raise ValueError('Invalid renderer token weights')
        if len(tokens) > max_length:
            excluded['context_too_long'] += 1
        elif sum(weights) > max_target_tokens:
            excluded['target_too_long'] += 1
        elif sum(weights[1:]) <= 0:
            excluded['empty_target'] += 1
        else:
            kept.append((index, encoded))
    if not kept:
        raise ValueError('No usable tokenized rows remain')
    return kept, dict(excluded)


def check_checkpoint(value):
    # SDK run IDs can include a client suffix, e.g. <uuid>:train:0.
    if not isinstance(value, str) or not re.fullmatch(r'tinker://[A-Za-z0-9._:-]+/sampler_weights/[A-Za-z0-9._-]+', value):
        raise ValueError('Expected a Tinker sampler_weights checkpoint path')
    return value


def checkpoint_info(run):
    meta = json.loads((Path(run) / 'best.json').read_text(encoding='utf-8'))
    if meta.get('base_model') != BASE_MODEL or meta.get('judge_prompt_sha256') != prompt_hash():
        raise ValueError('Checkpoint base model or judge prompt differs from this code')
    check_checkpoint(meta['checkpoint'])
    return meta


async def train(backend, *, inputs=DEFAULT_DATA, output=None, epochs=3, batch_size=8, rank=16,
                learning_rate=1e-4, max_length=24576, max_target_tokens=4096, seed=42,
                smoke=False, resume=False):
    if any(type(n) is not int or n < 1 for n in [epochs, batch_size, rank, max_length, max_target_tokens]):
        raise ValueError('Training counts must be positive integers')
    if not math.isfinite(learning_rate) or learning_rate <= 0 or max_length > 32768:
        raise ValueError('Invalid learning rate or context exceeds the 32K base model')
    if resume and output is None:
        raise ValueError('--resume requires --output')
    data, metadata = load_prepared(inputs)
    if smoke:
        epochs = 1
        data = {'train': data['train'][:min(2 * batch_size, len(data['train']))], 'dev': data['dev'][:4]}
    output = Path(output) if output else new_run()
    config = {'base_model': BASE_MODEL, 'renderer': RENDERER, 'judge_prompt_sha256': prompt_hash(),
        'data_sha256': metadata['files_sha256'], 'b_commit': metadata['b_commit'],
        'epochs': epochs, 'batch_size': batch_size, 'rank': rank, 'learning_rate': learning_rate,
        'max_length': max_length, 'max_target_tokens': max_target_tokens, 'seed': seed, 'smoke': smoke,
        'runtime_source_sha256': source_identity(), 'sdk_versions': backend.versions}
    if output.exists() and not resume:
        raise ValueError('Training output exists; use a new directory or explicit --resume')
    if resume:
        prior = json.loads((output / 'config.json').read_text(encoding='utf-8'))
        if prior != config:
            raise ValueError('Resume requires identical code, data, SDK versions and training settings')
    # Tokenize and reject overlong examples before reserving a remote training model.
    encoded, exclusions = {}, {}
    for split in ['train', 'dev']:
        encoded[split], exclusions[split] = encoded_rows(backend, data[split], max_length, max_target_tokens)
    if not resume:
        output.mkdir(parents=True)
        write_json(output / 'config.json', config)
        write_json(output / 'tokenization.json', {'kept': {s: len(rows) for s, rows in encoded.items()},
            'excluded': exclusions, 'kept_indices': {s: [i for i, _ in rows] for s, rows in encoded.items()}})
        write_json(output / 'provenance.json', {'parent_commit': git('rev-parse', 'HEAD').decode().strip(),
            'dirty': bool(git('status', '--porcelain', '--untracked-files=normal')),
            'note': 'Tinker remote GPU type/job ID unavailable; not a formal H100 latency experiment.'})
    attempt = uuid.uuid4().hex[:8]

    def event(kind, **values):
        with (output / 'events.jsonl').open('a', encoding='utf-8') as journal:
            journal.write(json.dumps({'at_utc': datetime.now(timezone.utc).isoformat(), 'attempt': attempt,
                                      'type': kind, **values}, allow_nan=False) + '\n')

    state = json.loads((output / 'resume.json').read_text(encoding='utf-8')) if resume else None
    next_epoch = state['completed_epoch'] + 1 if state else 1
    if next_epoch > epochs:
        print('Training already completed: ' + str(output.resolve()))
        return output
    event('starting', resume=resume, next_epoch=next_epoch)
    print('Training directory: ' + str(output.resolve()), flush=True)
    finish_status = 'success'
    try:
        await backend.start(rank, state=state['state'] if state else None, seed=seed)
        if not state:
            saved = await backend.save('epoch-0000')
            write_json(output / 'resume.json', {**saved, 'completed_epoch': 0})
        best = json.loads((output / 'best.json').read_text(encoding='utf-8')) if (output / 'best.json').exists() else None
        for epoch in range(next_epoch, epochs + 1):
            order = list(range(len(encoded['train'])))
            random.Random(seed + epoch).shuffle(order)
            train_sum = train_weight = 0.0
            for step, start in enumerate(range(0, len(order), batch_size), 1):
                batch = [encoded['train'][i][1] for i in order[start:start + batch_size]]
                loss_sum, weight = await backend.train_batch(batch, learning_rate)
                if not math.isfinite(loss_sum) or weight <= 0:
                    raise ValueError('Invalid training loss')
                train_sum += loss_sum
                train_weight += weight
                event('optimizer_step', epoch=epoch, step=step, loss=loss_sum / weight)
                print(f'Epoch {epoch}/{epochs}, step {step}: loss={loss_sum / weight:.4f}', flush=True)
            dev_sum = dev_weight = 0.0
            for start in range(0, len(encoded['dev']), batch_size):
                batch = [row for _, row in encoded['dev'][start:start + batch_size]]
                loss_sum, weight = await backend.loss_batch(batch)
                if not math.isfinite(loss_sum) or weight <= 0:
                    raise ValueError('Invalid validation loss')
                dev_sum += loss_sum
                dev_weight += weight
            saved = await backend.save(f'epoch-{epoch:04d}')
            event('checkpoint_saved', epoch=epoch, **saved)
            check_checkpoint(saved['checkpoint'])
            result = {**saved, 'epoch': epoch, 'base_model': BASE_MODEL,
                'judge_prompt_sha256': prompt_hash(), 'train_loss': train_sum / train_weight,
                'dev_loss': dev_sum / dev_weight, 'smoke': smoke, 'renderer': RENDERER}
            write_json(output / f'epoch-{epoch:04d}.json', result)
            if best is None or result['dev_loss'] < best['dev_loss']:
                best = result
                write_json(output / 'best.json', best)
            write_json(output / 'resume.json', {**saved, 'completed_epoch': epoch})
            event('epoch_completed', **result)
            print(f"Epoch {epoch}: dev loss={result['dev_loss']:.4f}; saved {saved['checkpoint']}", flush=True)
        event('completed', best_epoch=best['epoch'])
        print('Best checkpoint: ' + best['checkpoint'])
        print('Run evaluation before using this checkpoint as a judge.')
        return output
    except BaseException as error:
        finish_status = 'interrupted' if isinstance(error, (KeyboardInterrupt, asyncio.CancelledError)) else 'errored'
        event('interrupted' if isinstance(error, (KeyboardInterrupt, asyncio.CancelledError)) else 'failed',
              error_type=type(error).__name__)
        raise
    finally:
        await backend.close(status=finish_status)


async def evaluate(backend, *, inputs=DEFAULT_DATA, output, checkpoint=None, limit=None, max_tokens=4096):
    data, meta = load_prepared(inputs)
    rows = data['dev'][:limit] if limit else data['dev']
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    write_json(output / 'config.json', {'base_model': BASE_MODEL, 'checkpoint': checkpoint,
        'renderer': RENDERER, 'judge_prompt_sha256': prompt_hash(), 'max_tokens': max_tokens,
        'limit': limit, 'b_commit': meta['b_commit'], 'dev_sha256': meta['files_sha256']['dev.jsonl'],
        'runtime_source_sha256': source_identity(), 'sdk_versions': backend.versions})
    write_json(output / 'provenance.json', {'parent_commit': git('rev-parse', 'HEAD').decode().strip(),
        'dirty': bool(git('status', '--porcelain', '--untracked-files=normal')),
        'note': 'Remote Tinker snapshot diagnostics; no formal GPU or speech timing claim.'})
    counters, details = Counter(), []
    finish_status = 'success'
    try:
        for index, row in enumerate(rows):
            started = time.monotonic()
            record = {'index': index, 'sample_id': row['sample_id'], 'status': 'ok'}
            raw_labels = {}
            try:
                reply = await backend.sample(row['payload'], checkpoint, max_tokens)
                record['reply'] = reply
                payload = row['payload']
                units = [Unit(u['unit_id'], u['description'], u['necessary'], tuple(u['depends_on']), tuple(u['queries']), u['subject'])
                         for u in payload['units']]
                predictions = validate_judgments(reply, units, [Evidence(**e) for e in payload['evidence']])
                raw_labels = {u['unit_id']: u['label'] for u in reply['judgments']}
                record['validated'] = {uid: {'label': p.label, 'value': p.value, 'reason': p.reason}
                                       for uid, p in predictions.items()}
            except (ValueError, ProviderError) as error:
                predictions = {}
                counters['invalid_records'] += 1
                record['status'] = 'invalid'
                record['error_type'] = type(error).__name__
            for target in row['target']['judgments']:
                want = target['label']
                prediction = predictions.get(target['unit_id'])
                got = prediction.label if prediction else 'INVALID'
                raw_label = raw_labels.get(target['unit_id'], 'INVALID')
                counters['units'] += 1
                counters['label_matches'] += got == want
                counters['raw_label_matches'] += raw_label == want
                counters['raw_false_supported'] += want != 'SUPPORTED' and raw_label == 'SUPPORTED'
                counters['rejected_supported_units'] += raw_label == 'SUPPORTED' and got != 'SUPPORTED'
                counters['not_supported_targets'] += want != 'SUPPORTED'
                counters['supported_targets'] += want == 'SUPPORTED'
                counters['false_supported'] += want != 'SUPPORTED' and got == 'SUPPORTED'
                counters['missed_supported'] += want == 'SUPPORTED' and got != 'SUPPORTED'
                if want == got == 'SUPPORTED':
                    counters['both_supported'] += 1
                    counters['value_matches'] += prediction.value.casefold().strip() == target['value'].casefold().strip()
            record['wall_s'] = time.monotonic() - started
            details.append(record)
            write_rows(output / 'predictions.jsonl', details)
            print(f'Dev {index + 1}/{len(rows)}: {record["status"]}', flush=True)
    except BaseException as error:
        finish_status = 'interrupted' if isinstance(error, (KeyboardInterrupt, asyncio.CancelledError)) else 'errored'
        raise
    finally:
        await backend.close(status=finish_status)
    ratio = lambda a, b: counters[a] / counters[b] if counters[b] else None
    summary = {'records': len(rows), 'counts': dict(counters), 'base_model': BASE_MODEL,
        'checkpoint': checkpoint, 'renderer': RENDERER, 'judge_prompt_sha256': prompt_hash(),
        'b_commit': meta['b_commit'], 'dev_sha256': meta['files_sha256']['dev.jsonl'],
        'label_agreement': ratio('label_matches', 'units'),
        'raw_label_agreement': ratio('raw_label_matches', 'units'),
        'raw_false_supported_rate': ratio('raw_false_supported', 'not_supported_targets'),
        'false_supported_rate': ratio('false_supported', 'not_supported_targets'),
        'missed_supported_rate': ratio('missed_supported', 'supported_targets'),
        'value_em_when_both_supported': ratio('value_matches', 'both_supported'),
        'note': 'Unprefixed metrics use validated judgments; raw metrics precede citation/dependency filtering. '
                'Held-out SFT snapshot/unit metrics, not independent questions, full-answer accuracy or B UCR.'}
    write_json(output / 'summary.json', summary)
    (output / 'summary.md').write_text('# Judge SFT dev evaluation\n\n'
        + '\n'.join(f'- {k}: {summary[k]}' for k in ['records', 'label_agreement', 'raw_label_agreement',
            'raw_false_supported_rate', 'false_supported_rate', 'missed_supported_rate', 'value_em_when_both_supported'])
        + '\n\n' + summary['note'] + '\n', encoding='utf-8')
    return summary
