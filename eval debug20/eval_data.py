"""Load B's unchanged scorer from a frozen commit; never guess unit alignment."""
import hashlib
import importlib
import importlib.util
import json
from pathlib import Path
import re
import sys

from eval_common import EVAL_ROOT, digest, git, read_jsonl, write_json


EVALUATOR_FILES = ('__init__.py', 'records.py', 'score.py', 'run_eval.py')
DEBUG_FILES = {'traces.jsonl': 'b_work/step3/traces_debug.jsonl',
               'gold.jsonl': 'b_work/step3/gold_debug.jsonl'}


def frozen_commit(ref):
    commit = git('rev-parse', '--verify', ref + '^{commit}').decode().strip()
    if not re.fullmatch('[0-9a-f]{40}', commit):
        raise ValueError('B evaluator needs an immutable Git commit')
    return commit


def load_evaluator(commit):
    """Read only four scorer source files, outside the tracked application tree."""
    commit = frozen_commit(commit)
    folder = EVAL_ROOT / 'artifacts/evaluators' / commit
    folder.mkdir(parents=True, exist_ok=True)
    hashes = {}
    for name in EVALUATOR_FILES:
        raw = git('show', commit + ':b_work/eval/' + name)
        target = folder / name
        if target.exists() and target.read_bytes() != raw:
            raise ValueError('Cached B evaluator differs from its frozen commit')
        if not target.exists():
            target.write_bytes(raw)
        hashes[name] = hashlib.sha256(raw).hexdigest()
    package = '_cascade_b_eval_' + commit
    if package not in sys.modules:
        spec = importlib.util.spec_from_file_location(package, folder / '__init__.py',
                                                    submodule_search_locations=[str(folder)])
        module = importlib.util.module_from_spec(spec)
        sys.modules[package] = module
        spec.loader.exec_module(module)
    return importlib.import_module(package + '.run_eval'), hashes


def prepare_b_debug(ref, output):
    """Export fixed debug paths only. Never enumerate or read a reserved split."""
    commit = frozen_commit(ref)
    evaluator, hashes = load_evaluator(commit)
    blobs = {name: git('show', commit + ':' + source) for name, source in DEBUG_FILES.items()}
    rows = {name: [json.loads(line) for line in raw.decode('utf-8-sig').splitlines() if line.strip()]
            for name, raw in blobs.items()}
    for records in rows.values():
        if any(r.get('schema_version') != '1.0' or r.get('data_version') != 'debug-v0' for r in records):
            raise ValueError('Only B debug-v0 input is permitted')
    evaluator.prepare_inputs(rows['traces.jsonl'], rows['gold.jsonl'])
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    for name, raw in blobs.items():
        (output / name).write_bytes(raw)
    manifest = {'mode': 'b_debug_trace', 'split': 'debug', 'data_version': 'debug-v0',
                'b_commit': commit, 'evaluator_sha256': hashes,
                'source_paths': DEBUG_FILES,
                'files_sha256': {name: digest(output / name) for name in DEBUG_FILES},
                'questions': len(rows['gold.jsonl']), 'traces': len(rows['traces.jsonl'])}
    write_json(output / 'manifest.json', manifest)
    return output, manifest


def load_b_traces(inputs):
    """Prediction reads traces only. Gold remains exclusively with the scorer."""
    inputs = Path(inputs)
    manifest = json.loads((inputs / 'manifest.json').read_text(encoding='utf-8'))
    if (manifest.get('mode'), manifest.get('split'), manifest.get('data_version')) != ('b_debug_trace', 'debug', 'debug-v0'):
        raise ValueError('Only prepared B debug traces are allowed')
    if digest(inputs / 'traces.jsonl') != manifest['files_sha256']['traces.jsonl']:
        raise ValueError('B debug trace hash mismatch')
    traces = read_jsonl(inputs / 'traces.jsonl')
    if any(t.get('data_version') != 'debug-v0' or t.get('schema_version') != '1.0' for t in traces):
        raise ValueError('Only B debug-v0 traces are allowed')
    return traces, manifest


