"""Adapt fixed B SFT train/dev only, without changing its annotations or rules."""
from collections import Counter
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import re
import subprocess

from ..llm import JUDGE
from ..models import Evidence, plan_from_json, validate_judgments

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DATA = ROOT / 'cascadesystem/artifacts/training/data'
B_REF = 'ea390574eadd301354d5de46f0d28d328cca5bad'
FILES = {
    'train.jsonl': 'b_work/step4/sft/sft_train.jsonl',
    'dev.jsonl': 'b_work/step4/sft/sft_dev.jsonl',
    'stats.json': 'b_work/step4/sft/sft_stats.json',
    'candidates.jsonl': 'b_work/step4/prepared/samples_sft_candidates.jsonl',
    'gold.jsonl': 'b_work/step4/gold_sft.jsonl',
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def prompt_hash():
    return sha(JUDGE.encode('utf-8'))


def read_rows(path):
    return [json.loads(line) for line in Path(path).read_text(encoding='utf-8-sig').splitlines() if line.strip()]


def write_json(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')


def write_rows(path, rows):
    Path(path).write_text(''.join(json.dumps(row, ensure_ascii=False, allow_nan=False) + '\n' for row in rows), encoding='utf-8')


def git(*args):
    return subprocess.run(['git', '-c', 'safe.directory=' + ROOT.as_posix(), *args], cwd=ROOT,
                          capture_output=True, check=True).stdout


def convert_record(record, sample, gold):
    """Return a compatible supervised record or an explicit exclusion reason.

    Full context is used offline to reconstruct literal visible sentences only;
    the request's visible set is the sole source of model evidence.
    """
    meta = record['metadata']
    if meta.get('data_version') != 'sft-v0' or meta.get('split') not in {'train', 'dev'}:
        raise ValueError('Only B sft-v0 train/dev records are allowed')
    if sample.get('source_split') != 'train' or sample.get('project_split') != meta['split']:
        raise ValueError('SFT source or question split mismatch')
    if sample['sample_id'] != meta['sample_id'] or gold['sample_id'] != meta['sample_id']:
        raise ValueError('SFT question identity mismatch')
    # Preserve the current no-omission policy. Do not relabel B's annotations.
    if any(u.get('by_omission') for u in gold['units']):
        return None, 'question_uses_omission_rule'
    messages = record['messages']
    if messages[-2]['role'] != 'user' or messages[-1]['role'] != 'assistant':
        raise ValueError('Invalid B SFT chat record')
    prefix = 'Question: ' + sample['question'] + '\n\nUnits:\n'
    request = messages[-2]['content']
    if not request.startswith(prefix):
        raise ValueError('SFT input question does not match its source')
    suffix = request[len(prefix):]
    raw_units, end = json.JSONDecoder().raw_decode(suffix)
    delimiter = '\n\nEvidence received so far:\n'
    if not suffix[end:].startswith(delimiter):
        raise ValueError('Unknown B evidence request format')
    evidence_text = suffix[end + len(delimiter):]
    catalog = {}
    for doc_index, (title, sentences) in enumerate(sample['context'], 1):
        for sentence_index, text in enumerate(sentences):
            catalog[f'd{doc_index}s{sentence_index}'] = (title, text.strip())
    visible = re.findall(r'^\[([^\]]+)\]', evidence_text, re.M)
    if len(set(visible)) != len(visible) or any(eid not in catalog for eid in visible):
        raise ValueError('Invalid visible SFT evidence IDs')
    reconstructed = '\n'.join(f'[{eid}] ({catalog[eid][0]}) {catalog[eid][1]}' for eid in visible)
    if reconstructed != evidence_text:
        raise ValueError('SFT source text differs from its visible request')
    gold_units = {u['unit_id']: u for u in gold['units']}
    if {u['unit_id'] for u in raw_units} != set(gold_units):
        raise ValueError('SFT input units do not match annotations')
    units = plan_from_json({'units': [{
        'unit_id': u['unit_id'], 'description': u['description'],
        'depends_on': u['depends_on'], 'necessary': gold_units[u['unit_id']]['necessary'],
        'queries': [u['description']], 'subject': '',
    } for u in raw_units]})
    evidence = [Evidence(eid, catalog[eid][0], 'https://training.invalid/' + eid, catalog[eid][1], 0)
                for eid in visible]
    targets = json.loads(messages[-1]['content'])['units']
    if {u['unit_id'] for u in targets} != set(gold_units) or len(targets) != len(units):
        raise ValueError('Invalid SFT target unit set')
    target = {'judgments': []}
    for row in targets:
        if row.get('by_omission'):
            return None, 'target_uses_omission_rule'
        supported = row['label'] == 'SUPPORTED'
        if row['label'] not in {'SUPPORTED', 'UNRESOLVED', 'CONTRADICTED'}:
            raise ValueError('Unknown SFT label')
        cites = row['citations'] if supported else []
        if any(eid not in visible for eid in cites):
            raise ValueError('Training target cites future evidence')
        target['judgments'].append({'unit_id': row['unit_id'], 'label': row['label'],
            'value': row['value'] if supported else '', 'citations': cites,
            'quotes': [{'evidence_id': eid, 'text': catalog[eid][1]} for eid in cites],
            'reason': 'Supported by the cited visible sentences and dependencies.' if supported
                      else 'The current visible evidence does not establish this unit.'})
    checked = validate_judgments(target, units, evidence)
    if any(checked[row['unit_id']].label != row['label'] for row in target['judgments']):
        return None, 'target_incompatible_with_current_dependency_contract'
    payload = {'question': sample['question'], 'output_language': 'en',
               'units': [asdict(u) for u in units], 'required_unit_ids': [u.unit_id for u in units],
               'visible_evidence_ids': visible, 'evidence': [asdict(e) for e in evidence]}
    return {'sample_id': meta['sample_id'], 'split': meta['split'], 'payload': payload, 'target': target,
            'metadata': {'b_trace_id': meta['trace_id'], 'time_s': meta['time_s'],
                         'question_type': meta['question_type'], 'unit_source': 'B annotated descriptions'}}, None


def prepare(output=DEFAULT_DATA, ref=B_REF):
    output = Path(output)
    if output.exists():
        raise ValueError('Prepared directory already exists; inspect it or choose a new --output')
    commit = git('rev-parse', '--verify', ref + '^{commit}').decode().strip()
    raw = {name: git('show', commit + ':' + path) for name, path in FILES.items()}
    parse = lambda name: [json.loads(line) for line in raw[name].decode('utf-8-sig').splitlines() if line.strip()]
    candidates = {s['sample_id']: s for s in parse('candidates.jsonl')}
    golds = {g['sample_id']: g for g in parse('gold.jsonl')}
    records = {split: parse(split + '.jsonl') for split in ['train', 'dev']}
    ids = {split: {r['metadata']['sample_id'] for r in rows} for split, rows in records.items()}
    if ids['train'] & ids['dev']:
        raise ValueError('A question appears in both train and dev')
    questions = {split: {candidates[sid]['question'].casefold().strip() for sid in values}
                 for split, values in ids.items()}
    if questions['train'] & questions['dev']:
        raise ValueError('Duplicate question text across train/dev')
    converted, counts, exclusions = {}, {}, []
    for split, rows in records.items():
        converted[split], skipped = [], Counter()
        for index, record in enumerate(rows):
            sid = record['metadata']['sample_id']
            item, reason = convert_record(record, candidates[sid], golds[sid])
            if reason:
                skipped[reason] += 1
                exclusions.append({'split': split, 'source_index': index, 'sample_id': sid, 'reason': reason})
            else:
                converted[split].append(item)
        if not converted[split]:
            raise ValueError('No compatible ' + split + ' records remain')
        counts[split] = {'input_questions': len(ids[split]), 'input_examples': len(rows),
            'kept_questions': len({r['sample_id'] for r in converted[split]}), 'kept_examples': len(converted[split]),
            'excluded_examples': dict(skipped),
            'labels': dict(Counter(t['label'] for r in converted[split] for t in r['target']['judgments']))}
    output.mkdir(parents=True)
    (output / 'raw').mkdir()
    for name, value in raw.items():
        (output / 'raw' / name).write_bytes(value)
    for split, rows in converted.items():
        write_rows(output / (split + '.jsonl'), rows)
    write_rows(output / 'exclusions.jsonl', exclusions)
    manifest = {'mode': 'cascade_judge_sft', 'data_version': 'sft-v0', 'b_commit': commit,
        'source_paths': FILES, 'source_sha256': {name: sha(value) for name, value in raw.items()},
        'files_sha256': {split + '.jsonl': sha((output / (split + '.jsonl')).read_bytes()) for split in converted},
        'judge_prompt_sha256': prompt_hash(), 'counts': counts,
        'limitations': ['No CONTRADICTED examples in B sft-v0.', 'No dedicated single-answer/multipart training coverage.',
            'Units are annotated descriptions, not current model decompositions; subjects are unspecified.',
            'Quotes are copied full visible sentences, not independently reviewed minimal spans.',
            'Omission-based questions are excluded, not relabeled.']}
    write_json(output / 'manifest.json', manifest)
    return manifest


def load_prepared(folder=DEFAULT_DATA):
    folder = Path(folder)
    meta = json.loads((folder / 'manifest.json').read_text(encoding='utf-8'))
    if meta.get('mode') != 'cascade_judge_sft' or meta.get('data_version') != 'sft-v0':
        raise ValueError('Only prepared judge SFT data is allowed')
    if meta['judge_prompt_sha256'] != prompt_hash():
        raise ValueError('Judge prompt changed; prepare a fresh dataset')
    rows = {}
    for split in ['train', 'dev']:
        path = folder / (split + '.jsonl')
        if sha(path.read_bytes()) != meta['files_sha256'][path.name]:
            raise ValueError('Prepared SFT data hash mismatch')
        rows[split] = read_rows(path)
        if any(r.get('split') != split for r in rows[split]):
            raise ValueError('Invalid SFT split')
    if {r['sample_id'] for r in rows['train']} & {r['sample_id'] for r in rows['dev']}:
        raise ValueError('Train/dev question overlap')
    if ({r['payload']['question'].casefold().strip() for r in rows['train']} &
            {r['payload']['question'].casefold().strip() for r in rows['dev']}):
        raise ValueError('Duplicate question text across train/dev')
    return rows, meta
