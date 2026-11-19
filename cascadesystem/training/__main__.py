"""Prepare, train, evaluate and run a GPT-OSS evidence judge on Tinker."""
import argparse
import asyncio
import json
import os
from pathlib import Path
import subprocess
import sys

from ..config import Settings
from .data import B_REF, DEFAULT_DATA, ROOT, load_prepared, prepare
from .engine import checkpoint_info, evaluate, train


def arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    prep = commands.add_parser('prepare', help='Offline export of fixed B SFT train/dev only')
    prep.add_argument('--ref', default=B_REF)
    prep.add_argument('--output', type=Path, default=DEFAULT_DATA)
    inspect = commands.add_parser('inspect', help='Inspect prepared data counts/hashes without SDK or API')
    inspect.add_argument('--inputs', type=Path, default=DEFAULT_DATA)
    training = commands.add_parser('train', help='Real Tinker LoRA training; requires SDK and API key')
    training.add_argument('--inputs', type=Path, default=DEFAULT_DATA)
    training.add_argument('--output', type=Path)
    training.add_argument('--epochs', type=int, default=3)
    training.add_argument('--batch-size', type=int, default=8)
    training.add_argument('--rank', type=int, default=16)
    training.add_argument('--lr', type=float, default=1e-4)
    training.add_argument('--max-length', type=int, default=24576)
    training.add_argument('--max-target-tokens', type=int, default=4096)
    training.add_argument('--seed', type=int, default=42)
    training.add_argument('--smoke', action='store_true', help='At most two training batches, four dev rows, one epoch; not a quality result')
    training.add_argument('--resume', action='store_true', help='Explicitly restore the last completed epoch; repeat any partial epoch')
    scoring = commands.add_parser('evaluate', help='Real held-out SFT dev predictions; never debug or reserved questions')
    select = scoring.add_mutually_exclusive_group(required=True)
    select.add_argument('--run', type=Path, help='Training directory containing best.json')
    select.add_argument('--base', action='store_true', help='Evaluate unadapted GPT-OSS-120B on the same dev rows')
    scoring.add_argument('--inputs', type=Path, default=DEFAULT_DATA)
    scoring.add_argument('--output', type=Path, required=True)
    scoring.add_argument('--limit', type=int, help='Number of dev snapshots, not independent questions')
    scoring.add_argument('--max-tokens', type=int, default=4096)
    running = commands.add_parser('run', help='Use best checkpoint for judge calls only, leaving the base model for other stages')
    running.add_argument('--run', type=Path, required=True)
    running.add_argument('--debug20', action='store_true', help='Run eval debug20/run.py instead of the conversational CLI')
    running.add_argument('inference_args', nargs=argparse.REMAINDER, help='Arguments after -- go to the chosen CLI')
    return parser.parse_args()


def inference_command(args):
    metadata = checkpoint_info(args.run)
    tail = args.inference_args
    if tail[:1] == ['--']:
        tail = tail[1:]
    if not tail:
        raise ValueError('Supply inference arguments after --, for example -- --question "..."')
    env = dict(os.environ)
    env['CASCADE_JUDGE_MODEL'] = metadata['checkpoint']
    env['CASCADE_JUDGE_REASONING_EFFORT'] = 'low'
    command = ([sys.executable, str(ROOT / 'eval debug20/run.py')] if args.debug20
               else [sys.executable, '-m', 'cascadesystem']) + tail
    return command, env


def main(args):
    if args.command == 'prepare':
        manifest = prepare(args.output, args.ref)
        print('Prepared data: ' + str(args.output.resolve()))
        print(json.dumps(manifest['counts'], indent=2))
        return 0
    if args.command == 'inspect':
        _, manifest = load_prepared(args.inputs)
        print(json.dumps({'counts': manifest['counts'], 'limitations': manifest['limitations']}, indent=2))
        return 0
    if args.command == 'run':
        command, env = inference_command(args)
        print('Judge checkpoint: ' + env['CASCADE_JUDGE_MODEL'], flush=True)
        process = subprocess.Popen(command, cwd=ROOT, env=env)
        try:
            return process.wait()
        except KeyboardInterrupt:
            try:
                process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                process.terminate()
                process.wait()
            return 130
    # Optional packages are needed only for real training/tokenization/prediction.
    from .sdk import CloudBackend
    settings = Settings.from_env()
    if not settings.api_key:
        raise ValueError('Set TINKER_API_KEY in cascadesystem/.env; never put it in a command or dataset')
    if args.command == 'evaluate':
        if (args.limit is not None and args.limit < 1) or args.max_tokens < 1:
            raise ValueError('Evaluation counts must be positive')
        checkpoint = checkpoint_info(args.run)['checkpoint'] if args.run else None
        backend = CloudBackend(settings.api_key)
        summary = asyncio.run(evaluate(backend, inputs=args.inputs, output=args.output,
                                       checkpoint=checkpoint, limit=args.limit, max_tokens=args.max_tokens))
        print('Dev report: ' + str((args.output / 'summary.md').resolve()))
        return int(bool(summary['counts'].get('invalid_records')))
    backend = CloudBackend(settings.api_key)
    asyncio.run(train(backend, inputs=args.inputs, output=args.output, epochs=args.epochs,
        batch_size=args.batch_size, rank=args.rank, learning_rate=args.lr, max_length=args.max_length,
        max_target_tokens=args.max_target_tokens, seed=args.seed, smoke=args.smoke, resume=args.resume))
    return 0


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    try:
        raise SystemExit(main(arguments()))
    except KeyboardInterrupt:
        print('Cancelled. Saved states/results are retained.', file=sys.stderr)
        raise SystemExit(130)
    except Exception as error:
        # SDK/provider errors may contain request bodies: never print their raw text.
        message = str(error) if isinstance(error, (ValueError, FileNotFoundError)) else type(error).__name__
        print('Training/evaluation stopped: ' + message, file=sys.stderr)
        raise SystemExit(1)
