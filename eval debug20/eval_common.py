"""Local paths, JSON IO, frozen-source provenance, and public configuration."""
import hashlib
import json
from pathlib import Path
import subprocess


EVAL_ROOT = Path(__file__).resolve().parent
ROOT = EVAL_ROOT.parent


def git(*arguments):
    return subprocess.run(['git', '-c', 'safe.directory=' + ROOT.as_posix(), *arguments],
                          cwd=ROOT, capture_output=True, check=True).stdout


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_jsonl(path):
    return [json.loads(line) for line in Path(path).read_text(encoding='utf-8-sig').splitlines() if line.strip()]


def write_json(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')


def write_jsonl(path, rows):
    Path(path).write_text(''.join(json.dumps(row, ensure_ascii=False, allow_nan=False) + '\n' for row in rows),
                          encoding='utf-8')


def source_manifest():
    combined, files = hashlib.sha256(), {}
    for package in ['cascadesystem', EVAL_ROOT.name]:
        paths = sorted((p for p in (ROOT / package).rglob('*') if p.suffix in {'.py', '.ps1'}
                        and not {'artifacts', '.venv', '__pycache__'}.intersection(p.parts)), key=lambda p: p.as_posix())
        for path in paths:
            relative, raw = path.relative_to(ROOT).as_posix(), path.read_bytes()
            files[relative] = hashlib.sha256(raw).hexdigest()
            combined.update(relative.encode() + b'\0' + raw + b'\0')
    return {'sha256': combined.hexdigest(), 'files': files}


def public_settings(settings):
    return {name: getattr(settings, name) for name in [
        'base_url', 'model', 'judge_model', 'judge_reasoning_effort',
        'wiki_language', 'user_agent', 'timeout_s', 'max_tokens', 'reasoning_effort',
        'progress_s', 'feedback_timeout_s', 'search_limit', 'max_units', 'max_searches',
        'max_sources', 'source_chars', 'evidence_chars', 'concurrency']}


def reauthentication(error):
    return any(token in error for token in ['HTTP 401 ', 'HTTP 403 '])
