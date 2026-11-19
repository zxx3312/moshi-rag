"""B debug evidence replay: prepare, run, and score. No real-time search."""
import argparse
import asyncio
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys
import uuid


EVAL_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(EVAL_ROOT.parent))

from eval_data import prepare_b_debug
from eval_replay import run_b_debug
from eval_score import score_b_run
from cascadesystem.audio import AudioError


DEFAULT_INPUTS = EVAL_ROOT / 'artifacts/inputs/b-debug-v0'


def arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    prepare = commands.add_parser('prepare', help='Export only B debug trace/gold and freeze B scorer version')
    prepare.add_argument('--ref', default='origin/b-data-eval')
    prepare.add_argument('--output', type=Path, default=DEFAULT_INPUTS)
    run = commands.add_parser('run', help='Run GPT-OSS-120B on timed debug evidence and apply B scorer')
    run.add_argument('--inputs', type=Path, default=DEFAULT_INPUTS)
    run.add_argument('--output', type=Path)
    run.add_argument('--schedule', choices=['short', 'long', 'immediate', 'all'], default='short')
    run.add_argument('--timeout', type=float, default=180)
    run.add_argument('--resume', action='store_true')
    run.add_argument('--limit', type=int, help='Number of unique debug questions; all keeps three schedules per selected question')
    run.add_argument('--tts', choices=['none', 'windows'], default='none', help='Create WAV speech during each answer')
    run.add_argument('--play', action='store_true', help='Play each sentence as its WAV is ready; requires --tts windows')
    score = commands.add_parser('score', help='Score saved logs using B unchanged scorer; no API calls')
    score.add_argument('--inputs', type=Path, default=DEFAULT_INPUTS)
    score.add_argument('--run', type=Path, required=True)
    score.add_argument('--output', type=Path, required=True)
    score.add_argument('--reviews', type=Path, help='Checked claim-to-gold mappings with source_log_sha256')
    score.add_argument('--allow-value-match', action='store_true', help='B approximate unique-value mapping diagnostic')
    return parser.parse_args()


def main(args):
    if args.command == 'prepare':
        directory, manifest = prepare_b_debug(args.ref, args.output)
        print(json.dumps({'inputs': str(directory.resolve()), 'questions': manifest['questions'],
                          'traces': manifest['traces'], 'b_commit': manifest['b_commit']}, indent=2))
        return 0
    if args.command == 'run':
        if args.resume and args.output is None:
            raise ValueError('--resume requires the existing --output directory')
        output = args.output or EVAL_ROOT / 'artifacts/runs' / (
            datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:8])
        directory = asyncio.run(run_b_debug(args.inputs, output, schedule=args.schedule,
                                            timeout_s=args.timeout, resume=args.resume, limit=args.limit,
                                            tts=args.tts, play=args.play))
        report = directory / 'b_eval'
        summary = score_b_run(args.inputs, directory, report)
    else:
        report = args.output
        summary = score_b_run(args.inputs, args.run, report, reviews=args.reviews,
                              allow_value_match=args.allow_value_match)
    print(f"Evaluated {summary['questions']} questions / {summary['runs']} runs.")
    print('B status: ' + ', '.join(f'{key}={value}' for key, value in summary['status_counts'].items()))
    print('Claims pending mapping review: ' + str(sum(g['claims_needing_review'] for g in summary['groups'])))
    print('B report: ' + str((report / 'summary.md').resolve()))
    print('Unmapped claims remain in review_queue.jsonl; null scores are not zero or correct.')
    audio_failed = False
    if args.command == 'run' and args.tts != 'none':
        audio_summary = json.loads((directory / 'audio_summary.json').read_text(encoding='utf-8'))
        audio_failed = bool(audio_summary['failed_runs'])
        print('Audio index: ' + str((directory / 'audio_summary.json').resolve()))
    return int(audio_failed or any(k in summary['status_counts'] for k in ['invalid', 'error', 'missing']))


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    try:
        raise SystemExit(main(arguments()))
    except (AudioError, ValueError, OSError, KeyError, json.JSONDecodeError, subprocess.CalledProcessError) as error:
        print('Evaluation setup/input failed: ' + (str(error) if isinstance(error, (ValueError, AudioError)) else type(error).__name__),
              file=sys.stderr)
        raise SystemExit(2)
    except KeyboardInterrupt:
        print('Cancelled; saved sample files are retained.', file=sys.stderr)
        raise SystemExit(130)
