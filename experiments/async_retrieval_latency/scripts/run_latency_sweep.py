#!/usr/bin/env python
"""Controlled retrieval-latency stress test for MoshiRAG (offline, fixed reference).

For every (sample, seed, delay) the same user WAV is fed to MoshiRAG. When the model
emits its retrieval token, a mock backend returns the same fixed reference, which is
injected ``delay`` seconds (stream time) after the retrieval request. The model is
loaded once, and runs execute one after another on a single GPU.

Dry run (safe on a login node; imports no torch and loads no model):

    python experiments/async_retrieval_latency/scripts/run_latency_sweep.py \
        --manifest experiments/async_retrieval_latency/configs/samples.jsonl --dry-run

Real run: see ../slurm/run_latency_sweep.slurm. It needs REFERENCE_ENCODER_URL to
point at a running ``moshi.server_conditioner``.
"""

from __future__ import annotations

import argparse
import asyncio
import contextlib
import datetime
import importlib.metadata
import importlib.util
import json
import logging
import math
import os
import platform
import shlex
import signal
import socket
import subprocess
import sys
import tempfile
import time
import traceback
import wave
from copy import deepcopy
from pathlib import Path
from typing import Any

EXP_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = EXP_DIR.parents[1]
MOSHI_PKG_PARENT = REPO_ROOT / "moshi"
sys.path.insert(0, str(EXP_DIR))

from mock_retrieval import FixedReferenceBackend, delay_to_steps  # noqa: E402
from analysis.metrics import DEFAULT_AUDIBLE_DB, DEFAULT_SPEECH_DB, compute_metrics  # noqa: E402

DEFAULT_DELAYS = [0.0, 0.5, 1.0, 2.0, 3.0, 5.0, 8.0]
DEFAULT_SEED = 42424242  # same seed as moshi.run_inference
# Mimi frame rate, used only by --dry-run; the real run reads it from the loaded model.
DRY_RUN_FRAME_RATE = 12.5
# Top-level modules the GPU run needs (checked with find_spec, which does not import them).
REQUIRED_MODULES = [
    "torch", "numpy", "sphn", "sentencepiece", "safetensors", "huggingface_hub", "einops",
    "aiohttp", "httpx", "openai", "websockets", "gradium", "transformers",
    "fastapi", "uvicorn", "pydantic",
]

logger = logging.getLogger("latency_sweep")


# ----------------------------------------------------------------------
# Arguments and manifest
# ----------------------------------------------------------------------


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--manifest", type=Path, required=True, help="JSONL with sample_id, wav, reference_text[, question, answer].")
    p.add_argument("--retrieval-delay", type=float, nargs="+", default=DEFAULT_DELAYS,
                   help="Retrieval latency conditions in seconds (stream time after the retrieval request).")
    p.add_argument("--seeds", type=int, nargs="+", default=[DEFAULT_SEED],
                   help="Sampling seeds. The RNG is re-seeded before every run.")
    p.add_argument("--sample-ids", nargs="+", default=None, help="Only run these sample ids.")
    p.add_argument("--max-samples", type=int, default=None, help="Only run the first N samples.")
    p.add_argument("--output-root", type=Path, default=EXP_DIR / "results")
    p.add_argument("--run-name", type=str, default=None, help="Run directory name (default: timestamp[_jobID]).")
    p.add_argument("--dry-run", action="store_true", help="Validate everything without importing torch or loading models.")
    p.add_argument("--require-env", action="store_true",
                   help="With --dry-run: treat missing Python modules / REFERENCE_ENCODER_URL as errors.")

    g = p.add_argument_group("model (same meaning as moshi.run_inference)")
    g.add_argument("--hf-repo", type=str, default="kyutai/moshika-rag-pytorch-bf16")
    g.add_argument("--moshi-weight", type=str, default=None)
    g.add_argument("--mimi-weight", type=str, default=None)
    g.add_argument("--tokenizer", type=str, default=None)
    g.add_argument("--config", type=str, default=None)
    g.add_argument("--device", type=str, default="cuda:0")
    g.add_argument("--half", action="store_true", help="float16 instead of bfloat16.")
    g.add_argument("--stt-wait-time", type=float, default=0.5)
    g.add_argument("--max-reference-tokens", type=int, default=64)
    g.add_argument("--vad-window-size", type=int, default=4)
    g.add_argument("--vad-threshold", type=float, default=0.5)
    g.add_argument("--power-threshold", type=int, default=-65)
    g.add_argument("--init-active-speaker", type=str, default="user", choices=["model", "user"])

    g = p.add_argument_group("run control")
    g.add_argument("--max-tail-silence-frames", type=int, default=40,
                   help="Stop after this many consecutive pad text tokens once no retrieval is pending (40 = 3.2 s).")
    g.add_argument("--max-response-seconds", type=float, default=30.0,
                   help="Hard cap on stream time generated after the input WAV ends.")
    g.add_argument("--sample-timeout", type=float, default=300.0,
                   help="Wall-clock seconds per run before it is recorded as a timeout and skipped.")
    g.add_argument("--max-consecutive-failures", type=int, default=3,
                   help="Abort the sweep after this many failed runs in a row (e.g. a broken GPU state).")
    g.add_argument("--speech-db", type=float, default=DEFAULT_SPEECH_DB, help="User speech RMS threshold (dBFS).")
    g.add_argument("--audible-db", type=float, default=DEFAULT_AUDIBLE_DB, help="Model audible RMS threshold (dBFS).")
    g.add_argument("--log-level", type=str, default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    args = p.parse_args(argv)
    args.retrieval_delay = [float(d) for d in args.retrieval_delay]
    return args


def load_manifest(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    errors: list[str] = []
    samples: list[dict[str, Any]] = []
    if not path.is_file():
        return [], [f"manifest not found: {path}"]
    seen: set[str] = set()
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as e:
            errors.append(f"{path}:{lineno}: invalid JSON ({e})")
            continue
        missing = [k for k in ("sample_id", "wav", "reference_text") if not obj.get(k)]
        if missing:
            errors.append(f"{path}:{lineno}: missing required field(s) {missing}")
            continue
        sid = str(obj["sample_id"])
        if sid in seen:
            errors.append(f"{path}:{lineno}: duplicate sample_id {sid!r}")
            continue
        if any(c in sid for c in "/\\ "):
            errors.append(f"{path}:{lineno}: sample_id {sid!r} must not contain '/', '\\' or spaces")
            continue
        seen.add(sid)
        wav = Path(obj["wav"])
        obj["sample_id"] = sid
        obj["wav_path"] = str(wav if wav.is_absolute() else (path.parent / wav).resolve())
        samples.append(obj)
    return samples, errors


def select_samples(samples: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    if args.sample_ids:
        wanted = set(args.sample_ids)
        samples = [s for s in samples if s["sample_id"] in wanted]
    if args.max_samples is not None:
        samples = samples[: args.max_samples]
    return samples


def inspect_wav(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    """Return (info, problem). Uses stdlib ``wave`` only."""
    if not path.is_file():
        return None, f"WAV not found: {path}"
    try:
        with wave.open(str(path), "rb") as wf:
            info = {
                "channels": wf.getnchannels(),
                "sample_rate": wf.getframerate(),
                "sample_width_bytes": wf.getsampwidth(),
                "duration_s": round(wf.getnframes() / float(wf.getframerate()), 3),
            }
        return info, None
    except (wave.Error, EOFError) as e:
        return None, f"could not parse {path} with stdlib wave ({e}); sphn may still read it (e.g. float WAV)"


def validate_config(args: argparse.Namespace, samples: list[dict[str, Any]]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not samples:
        errors.append("no samples selected")
    delays = args.retrieval_delay
    for d in delays:
        if not math.isfinite(d) or d < 0:
            errors.append(f"invalid retrieval delay {d}")
    if len(set(delays)) != len(delays):
        errors.append(f"duplicate retrieval delays: {delays}")
    if len(set(args.seeds)) != len(args.seeds):
        errors.append(f"duplicate seeds: {args.seeds}")
    if args.max_tail_silence_frames <= 0:
        errors.append("--max-tail-silence-frames must be > 0")
    if args.sample_timeout <= 0:
        errors.append("--sample-timeout must be > 0")
    if delays and all(math.isfinite(d) for d in delays):
        needed = max(delays) + args.stt_wait_time + 5.0
        if args.max_response_seconds < needed:
            warnings.append(
                f"--max-response-seconds={args.max_response_seconds} leaves < 5 s after the longest delay "
                f"({max(delays)} s + {args.stt_wait_time} s STT wait); post-RAG speech may be cut off"
            )
    return errors, warnings


# ----------------------------------------------------------------------
# Reproducibility metadata
# ----------------------------------------------------------------------


def _cmd(cmd: list[str], timeout: float = 10.0) -> str | None:
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, check=False)
        return r.stdout.strip() if r.returncode == 0 else None
    except (OSError, subprocess.SubprocessError):
        return None


def collect_metadata() -> dict[str, Any]:
    git = ["git", "-C", str(REPO_ROOT)]
    dirty = _cmd(git + ["status", "--porcelain"])
    versions = {}
    for pkg in ("torch", "numpy", "sphn", "sentencepiece", "transformers", "xformers", "safetensors",
                "huggingface-hub", "moshi"):
        try:
            versions[pkg] = importlib.metadata.version(pkg)
        except importlib.metadata.PackageNotFoundError:
            versions[pkg] = None
    return {
        "git_commit": _cmd(git + ["rev-parse", "HEAD"]),
        "git_branch": _cmd(git + ["rev-parse", "--abbrev-ref", "HEAD"]),
        "git_dirty_files": dirty.splitlines() if dirty else [],
        "command": " ".join(shlex.quote(a) for a in [sys.executable] + sys.argv),
        "cwd": os.getcwd(),
        "hostname": socket.gethostname(),
        "python_version": sys.version,
        "platform": platform.platform(),
        "started_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
        "slurm": {k: v for k, v in os.environ.items() if k.startswith("SLURM_")},
        "cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES"),
        "nvidia_smi": _cmd(["nvidia-smi", "--query-gpu=name,memory.total,driver_version,uuid",
                            "--format=csv,noheader"]),
        "env": {k: os.environ.get(k) for k in ("REFERENCE_ENCODER_URL", "HF_HOME", "HF_HUB_CACHE", "CONDA_DEFAULT_ENV")},
        "package_versions": versions,
    }


def delay_tag(d: float) -> str:
    return f"{d:g}".replace(".", "p") + "s"


def build_plan(samples: list[dict[str, Any]], args: argparse.Namespace) -> list[tuple[dict[str, Any], int, float]]:
    # Delay is the innermost loop, so all conditions of one sample/seed run back to back.
    return [(s, seed, d) for s in samples for seed in args.seeds for d in args.retrieval_delay]


def _delay_entry(d: float, frame_rate: float) -> dict[str, Any]:
    try:
        n = delay_to_steps(d, frame_rate)
    except ValueError:
        return {"condition_s": d, "steps": None, "effective_s": None}
    return {"condition_s": d, "steps": n, "effective_s": n / frame_rate}


def config_dict(args: argparse.Namespace, samples: list[dict[str, Any]], frame_rate: float) -> dict[str, Any]:
    a = {k: (str(v) if isinstance(v, Path) else v) for k, v in vars(args).items()}
    return {
        "experiment": "async_retrieval_latency",
        "independent_variable": "retrieval latency (stream seconds after the retrieval request)",
        "args": a,
        "frame_rate": frame_rate,
        "delays": [_delay_entry(d, frame_rate) for d in args.retrieval_delay],
        "samples": samples,
        "num_runs": len(build_plan(samples, args)),
    }


# ----------------------------------------------------------------------
# Dry run
# ----------------------------------------------------------------------


def _synthetic_trace(frame_rate: float) -> dict[str, Any]:
    """Tiny fake trace to smoke-test the metrics code."""
    text = ["<pad>"] * 10 + ["<0x04>"] + ["▁Let", "▁me", "▁check", "."] + ["<pad>"] * 5 + ["▁It", "'s", "▁Angel", "▁Falls", "."]
    rms = [-80.0] * 11 + [-25.0] * 4 + [-80.0] * 5 + [-25.0] * 5
    return {
        "experiment": {"sample_id": "synthetic", "delay_condition_s": 0.5, "effective_delay_s": 0.48,
                       "delay_steps": 6, "seed": 0, "frame_rate": frame_rate, "input_frames": 8},
        "model_text": text, "model_rms_db": rms, "user_rms_db": [-20.0] * 6 + [-80.0] * 2,
        "retrieval_events": [{"trigger_step": 10, "request_step": 12, "available_step": 18,
                              "injection_step": 18, "injection_num_steps": 4}],
        "answer": ["Angel Falls"], "reference_text": "Angel Falls ...",
    }


def dry_run(args: argparse.Namespace) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    print("=" * 78)
    print("DRY RUN: no torch import, no model loading, no GPU use, no inference")
    print("=" * 78)

    if sys.version_info < (3, 11):
        msg = f"Python {platform.python_version()} < 3.11 (the repo uses asyncio.TaskGroup); use the experiment env"
        (errors if args.require_env else warnings).append(msg)

    all_samples, manifest_errors = load_manifest(args.manifest)
    errors += manifest_errors
    samples = select_samples(all_samples, args)
    cfg_errors, cfg_warnings = validate_config(args, samples)
    errors += cfg_errors
    warnings += cfg_warnings

    print(f"\n[manifest] {args.manifest}  ({len(all_samples)} samples, {len(samples)} selected)")
    total_input_s = 0.0
    for s in samples:
        info, problem = inspect_wav(Path(s["wav_path"]))
        if problem and info is None and not Path(s["wav_path"]).is_file():
            errors.append(f"sample {s['sample_id']}: {problem}")
        elif problem:
            warnings.append(f"sample {s['sample_id']}: {problem}")
        if info:
            s["wav_info"] = info
            total_input_s += info["duration_s"]
            if info["sample_rate"] != 24000:
                warnings.append(f"sample {s['sample_id']}: {info['sample_rate']} Hz (will be resampled to 24 kHz)")
        ref = s["reference_text"]
        print(f"  - {s['sample_id']}: wav={s['wav_path']} {info or '(unreadable)'}")
        print(f"      question : {s.get('question')!r}")
        print(f"      reference: {ref[:100]!r}{'...' if len(ref) > 100 else ''}")
        print(f"      answer   : {s.get('answer')!r}")
        if not s.get("question"):
            warnings.append(f"sample {s['sample_id']}: no 'question' text (only used for logging/analysis)")

    print(f"\n[latency sweep] frame rate {DRY_RUN_FRAME_RATE} Hz, STT wait {args.stt_wait_time} s "
          f"= {int(args.stt_wait_time * DRY_RUN_FRAME_RATE)} steps between [RET] and the request")
    print(f"  {'condition (s)':>14} {'steps':>6} {'effective (s)':>14} {'[RET]->injection (s)':>21}")
    wait_steps = int(args.stt_wait_time * DRY_RUN_FRAME_RATE)
    for d in args.retrieval_delay:
        try:
            n = delay_to_steps(d, DRY_RUN_FRAME_RATE)
            print(f"  {d:>14g} {n:>6} {n / DRY_RUN_FRAME_RATE:>14.2f} {(n + wait_steps) / DRY_RUN_FRAME_RATE:>21.2f}")
        except ValueError as e:
            errors.append(str(e))
    print(f"  seeds: {args.seeds}")

    print("\n[mock retrieval] checking FixedReferenceBackend")
    for s in samples[:3]:
        try:
            backend = FixedReferenceBackend(s["reference_text"], max(args.retrieval_delay), DRY_RUN_FRAME_RATE)
            r1 = asyncio.run(backend.retrieve("user: dry run"))
            r2 = asyncio.run(backend.retrieve("user: different context"))
            assert r1.reference_text == r2.reference_text == s["reference_text"], "reference not fixed"
            assert r1.available_after_steps == backend.delay_steps
            print(f"  ok: {s['sample_id']} -> identical reference for 2 requests, "
                  f"available after {backend.delay_steps} steps")
        except Exception as e:  # noqa: BLE001
            errors.append(f"mock retrieval check failed for {s['sample_id']}: {e}")

    print("\n[analysis] metrics smoke test on a synthetic trace")
    try:
        m = compute_metrics(_synthetic_trace(DRY_RUN_FRAME_RATE))
        assert m["retrieval_trigger_time"] == 0.8 and m["reference_injection_time"] == 1.44, m
        assert m["first_informative_content_match"] == "angel falls", m
        print(f"  ok: pre_rag={m['pre_rag_transcript']!r} post_rag={m['post_rag_transcript']!r}")
    except Exception as e:  # noqa: BLE001
        errors.append(f"metrics smoke test failed: {e!r}")

    print(f"\n[output] root: {args.output_root}")
    try:
        args.output_root.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(dir=args.output_root, prefix=".write_test_"):
            pass
        print("  ok: writable (a new timestamped run directory is created per real run)")
        if args.run_name and (args.output_root / args.run_name / "results.jsonl").exists():
            errors.append(f"run directory {args.output_root / args.run_name} already has results.jsonl")
    except OSError as e:
        errors.append(f"output root not writable: {e}")

    print("\n[environment]")
    print(f"  python: {sys.executable} ({platform.python_version()})")
    print(f"  REFERENCE_ENCODER_URL={os.environ.get('REFERENCE_ENCODER_URL')!r} (set by the Slurm script)")
    print(f"  HF_HOME={os.environ.get('HF_HOME')!r}")
    if not (MOSHI_PKG_PARENT / "moshi" / "__init__.py").is_file():
        errors.append(f"moshi package not found under {MOSHI_PKG_PARENT}")
    missing = [m for m in REQUIRED_MODULES if importlib.util.find_spec(m) is None]
    if missing:
        msg = f"modules not importable in this Python: {missing}"
        (errors if args.require_env else warnings).append(msg + ("" if args.require_env else
                                                                 " (expected on the login node)"))
    else:
        print("  ok: all required modules are installed")
    if args.require_env and not os.environ.get("REFERENCE_ENCODER_URL"):
        errors.append("REFERENCE_ENCODER_URL is not set")

    n_runs = len(build_plan(samples, args))
    per_run_upper = (total_input_s / max(len(samples), 1)) + args.max_response_seconds
    print(f"\n[plan] {len(samples)} samples x {len(args.seeds)} seeds x {len(args.retrieval_delay)} delays "
          f"= {n_runs} runs, model loaded once, runs sequential on 1 GPU")
    print(f"  upper bound on generated stream time: {n_runs * per_run_upper / 60:.1f} min "
          f"(wall time is lower if the GPU is faster than real time)")
    print("\n[config]")
    print(json.dumps(config_dict(args, samples, DRY_RUN_FRAME_RATE)["args"], indent=2))

    assert "torch" not in sys.modules, "dry run must not import torch"
    print("\n  confirmed: torch was not imported")

    for w in warnings:
        print(f"WARNING: {w}")
    for e in errors:
        print(f"ERROR: {e}")
    print(f"\nDRY RUN {'FAILED' if errors else 'PASSED'} ({len(errors)} errors, {len(warnings)} warnings)")
    return 1 if errors else 0


# ----------------------------------------------------------------------
# Real run (GPU)
# ----------------------------------------------------------------------


def make_run_dir(args: argparse.Namespace) -> Path:
    name = args.run_name
    if not name:
        name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        if os.environ.get("SLURM_JOB_ID"):
            name += f"_job{os.environ['SLURM_JOB_ID']}"
    run_dir = (args.output_root / name).resolve()
    if (run_dir / "results.jsonl").exists():
        raise SystemExit(f"refusing to overwrite existing results in {run_dir}")
    for sub in ("audio", "traces", "logs"):
        (run_dir / sub).mkdir(parents=True, exist_ok=True)
    return run_dir


def setup_logging(level: str, log_file: Path) -> None:
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s", datefmt="%H:%M:%S")
    root = logging.getLogger()
    root.handlers.clear()
    for h in (logging.StreamHandler(), logging.FileHandler(log_file, encoding="utf-8")):
        h.setFormatter(fmt)
        root.addHandler(h)
    root.setLevel(getattr(logging, level))


def append_jsonl(path: Path, record: dict[str, Any]) -> None:
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
        f.flush()
        os.fsync(f.fileno())


def write_json(path: Path, obj: Any) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(obj, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    tmp.replace(path)


def run_real(args: argparse.Namespace) -> int:
    all_samples, manifest_errors = load_manifest(args.manifest)
    samples = select_samples(all_samples, args)
    cfg_errors, _ = validate_config(args, samples)
    missing_wavs = [s["sample_id"] for s in samples if not Path(s["wav_path"]).is_file()]
    if manifest_errors or cfg_errors or missing_wavs:
        for e in manifest_errors + cfg_errors + [f"missing WAV for {m}" for m in missing_wavs]:
            print(f"ERROR: {e}", file=sys.stderr)
        return 2

    run_dir = make_run_dir(args)
    setup_logging(args.log_level, run_dir / "logs" / "runner.log")
    logger.info("run directory: %s", run_dir)
    config = config_dict(args, samples, DRY_RUN_FRAME_RATE)
    config["metadata"] = collect_metadata()
    write_json(run_dir / "config.json", config)

    # Heavy imports only from here on. Make sure this branch's moshi code is the one imported.
    sys.path.insert(0, str(MOSHI_PKG_PARENT))
    import torch

    import moshi
    import moshi.server as moshi_server
    from moshi.inference_utils import load_models
    from moshi.inference_utils.utils import get_conditioning_remote_async, get_reference_encoder_url, seed_all
    from moshi.stt.local_stt import LocalSpeechToText

    from latency_job import LatencyInferenceJob

    moshi_file = Path(moshi.__file__).resolve()
    if MOSHI_PKG_PARENT.resolve() not in moshi_file.parents:
        logger.warning("moshi imported from %s, not from this repository", moshi_file)

    class _NoLLMReferenceGenerator:
        """Stand-in for LLMReferenceGenerator: the fixed-reference backend replaces the LLM,
        so no LLM endpoint (LLM_BASE_URL) is needed and no warm-up request is sent."""

        def __init__(self, *a: Any, **k: Any) -> None:
            pass

        def warmup(self) -> None:
            pass

        async def generate_reference_text(self, *a: Any, **k: Any):
            raise RuntimeError("LLM retrieval is disabled in the latency experiment")

    moshi_server.LLMReferenceGenerator = _NoLLMReferenceGenerator  # type: ignore[assignment]

    encoder_url = get_reference_encoder_url()
    model_args = argparse.Namespace(
        hf_repo=args.hf_repo, moshi_weight=args.moshi_weight, mimi_weight=args.mimi_weight,
        tokenizer=args.tokenizer, config=args.config, device=args.device,
        dtype=torch.float16 if args.half else torch.bfloat16,
        cfg_coef=1.0,  # per-slot reference injection requires cfg_coef == 1
        batch_size=1, init_active_speaker=args.init_active_speaker,
    )
    seed_all(args.seeds[0])
    t0 = time.monotonic()
    mimi, text_tokenizer, lm_gen = load_models(model_args)
    stt =LocalSpeechToText(deepcopy(mimi))
    state = moshi_server.ServerState(
        mimi=mimi, text_tokenizer=text_tokenizer, lm_gen=lm_gen, reference_encoder_url=encoder_url,
        stt_wait_time=args.stt_wait_time, gradium_stt=False, device=args.device, rag_timeout=10.0,
        max_reference_tokens=args.max_reference_tokens, batch_size=1, vad_window_size=args.vad_window_size,
        vad_threshold=args.vad_threshold, init_active_speaker=args.init_active_speaker,
        power_threshold=args.power_threshold,
    )
    state.warmup()
    frame_rate = float(state.runner.mimi.frame_rate)
    if frame_rate != DRY_RUN_FRAME_RATE:
        logger.warning("model frame rate %s != %s; delay steps recomputed", frame_rate, DRY_RUN_FRAME_RATE)
    config.update(config_dict(args, samples, frame_rate))
    config["runtime"] = {
        "model_load_wall_s": round(time.monotonic() - t0, 1),
        "moshi_package": str(moshi_file),
        "torch": torch.__version__,
        "torch_cuda": torch.version.cuda,
        "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
        "sample_rate": int(state.runner.mimi.sample_rate),
        "stt_wait_steps": state.stt_wait_steps,
        "rag_token_id": lm_gen.lm_model.rag_token_id,
        "sampling": {k: getattr(lm_gen, k, None) for k in ("use_sampling", "temp", "temp_text", "top_k", "top_k_text")},
    }
    write_json(run_dir / "config.json", config)
    logger.info("models loaded in %.1fs", config["runtime"]["model_load_wall_s"])

    status = {"status": "running"}
    try:
        with torch.no_grad():
            status = asyncio.run(
                _sweep(state, stt, samples, args, run_dir, encoder_url, seed_all, get_conditioning_remote_async,
                       LatencyInferenceJob)
            )
    except KeyboardInterrupt:
        status = {"status": "interrupted"}
    status["finished_at"] = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    write_json(run_dir / "run_status.json", status)
    logger.info("sweep finished: %s", status)
    return 0 if status.get("status") == "finished" else 1


async def _sweep(state, stt, samples, args, run_dir, encoder_url, seed_all, encode_remote, job_cls) -> dict[str, Any]:
    main_task = asyncio.current_task()
    assert main_task is not None
    # Slurm (scancel / time limit) and `timeout` send SIGTERM: cancel cleanly so the
    # in-flight run is saved as "interrupted" and the process exits.
    asyncio.get_running_loop().add_signal_handler(signal.SIGTERM, main_task.cancel)

    results_path = run_dir / "results.jsonl"
    counts = {"ok": 0, "timeout": 0, "error": 0}
    step_task = asyncio.create_task(state._step_loop(), name="batched-step-loop")
    try:
        reference_tensors: dict[str, Any] = {}
        for s in samples:
            text = s["reference_text"]
            if text not in reference_tensors:
                t = await encode_remote(text=text, encoder_url=encoder_url)
                reference_tensors[text] = t.squeeze(0).cpu()
                logger.info("pre-encoded reference for %s: %s", s["sample_id"], tuple(t.shape))

        plan = build_plan(samples, args)
        consecutive_failures = 0
        for i, (sample, seed, delay) in enumerate(plan, 1):
            if step_task.done():
                raise RuntimeError(f"batched step loop stopped: {step_task.exception()!r}")
            run_id = f"{sample['sample_id']}__d{delay_tag(delay)}__s{seed}"
            logger.info("=== run %d/%d: %s ===", i, len(plan), run_id)
            record = await _run_one(state, stt, sample, seed, delay, run_id, args, run_dir, reference_tensors,
                                    seed_all, job_cls)
            record["run_index"] = i
            append_jsonl(results_path, record)
            counts[record["status"]] = counts.get(record["status"], 0) + 1
            logger.info("run %s: status=%s stop=%s trigger=%s injection=%s", run_id, record["status"],
                        record["stop_reason"], record["retrieval_trigger_time"], record["reference_injection_time"])
            consecutive_failures = 0 if record["status"] == "ok" else consecutive_failures + 1
            if consecutive_failures >= args.max_consecutive_failures:
                logger.error("aborting: %d consecutive failed runs", consecutive_failures)
                return {"status": "aborted", "counts": counts, "planned_runs": len(plan)}
        return {"status": "finished", "counts": counts, "planned_runs": len(plan)}
    except asyncio.CancelledError:
        logger.warning("sweep cancelled (SIGTERM / Ctrl-C)")
        return {"status": "interrupted", "counts": counts}
    finally:
        step_task.cancel()
        with contextlib.suppress(asyncio.CancelledError, Exception):
            await step_task


async def _run_one(state, stt, sample, seed, delay, run_id, args, run_dir, reference_tensors, seed_all, job_cls):
    # Re-seed before every run so that, for a given sample and seed, all delay conditions
    # start from the same RNG state (generation before the injection should then match).
    seed_all(seed)
    job = job_cls(
        state, sample=sample, run_id=run_id, run_dir=run_dir, delay_s=delay, seed=seed,
        reference_tensors=reference_tensors, max_tail_silence=args.max_tail_silence_frames,
        max_response_seconds=args.max_response_seconds, stt=stt,
    )
    await state.wait_acquire_slot(job)
    status, error = "ok", None

    async def _run_job() -> None:
        async with asyncio.TaskGroup() as tg:
            await job.run(tg)

    try:
        await asyncio.wait_for(_run_job(), timeout=args.sample_timeout)
    except TimeoutError:
        status, error = "timeout", f"exceeded --sample-timeout={args.sample_timeout}s"
        logger.error("run %s timed out; recording failure and continuing", run_id)
    except asyncio.CancelledError:
        job.write_outputs(status="interrupted", reason="cancelled")
        raise
    except Exception as e:  # noqa: BLE001 (includes ExceptionGroup from the TaskGroup)
        status, error = "error", "".join(traceback.format_exception(e))
        logger.error("run %s failed:\n%s", run_id, error)
    finally:
        await state.release_slot(job.slot_idx)

    if status != "ok":
        job.write_outputs(status=status, reason=status, error=error)
    record = compute_metrics(job.trace, speech_db=args.speech_db, audible_db=args.audible_db)
    record.update({"run_id": run_id, "status": status, "error": error})
    return record


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    args.manifest = args.manifest.resolve()
    args.output_root = args.output_root.resolve()
    if args.dry_run:
        return dry_run(args)
    return run_real(args)


if __name__ == "__main__":
    sys.exit(main())
