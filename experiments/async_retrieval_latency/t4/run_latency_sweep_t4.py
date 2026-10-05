#!/usr/bin/env python
"""Low-memory version of the controlled retrieval-latency sweep, for one 16 GB GPU (Colab T4).

Same experiment as ../scripts/run_latency_sweep.py: same ``LatencyInferenceJob`` (frame-based
injection at request_step + round(delay * 12.5)), same per-run function, same metrics. Differences,
all about memory or runtime robustness:

- MoshiRAG's LM is int8-quantized while loading (``q8_moshirag.py``); the rest runs in float16
  (T4 has no bf16). ``--no-q8`` / ``--dtype`` exist for comparisons on larger GPUs.
- No reference encoder: embeddings come from ``precompute_reference_embeddings.py``'s cache.
- No STT and no retrieval LLM. The model's input is the raw audio; in this experiment the STT only
  produced transcripts/VAD for the LLM retrieval context, which a fixed reference does not use.
  The 0.5 s wait between [RET] and the retrieval request is kept, so the latency is defined the same way.
- GPU memory is logged per load stage and per run (logs/gpu_memory.jsonl, and fields in results.jsonl).
- ``--resume`` continues a run directory: completed runs are skipped, settings must match.

    python experiments/async_retrieval_latency/t4/run_latency_sweep_t4.py \
        --manifest experiments/async_retrieval_latency/configs/samples.jsonl \
        --reference-cache REF_CACHE --run-name t4_smoke --retrieval-delay 3 --resume [--dry-run]
"""

from __future__ import annotations

import argparse
import asyncio
import contextlib
import datetime
import gc
import hashlib
import importlib.util
import json
import logging
import os
import platform
import signal
import sys
import time
from pathlib import Path
from typing import Any

T4_DIR = Path(__file__).resolve().parent
EXP_DIR = T4_DIR.parent
REPO_ROOT = EXP_DIR.parents[1]
MOSHI_PKG_PARENT = REPO_ROOT / "moshi"
sys.path[:0] = [str(T4_DIR), str(EXP_DIR / "scripts"), str(EXP_DIR)]

import run_latency_sweep as base  # noqa: E402  (A100 runner; its helpers are stdlib-only)
from mock_retrieval import delay_to_steps  # noqa: E402
from reference_cache import cache_path, read_cache_header, reference_sha256  # noqa: E402

T4_DEFAULT_DELAYS = [0.0, 1.0, 2.0, 3.0, 5.0, 8.0]
FRAME_RATE = base.DRY_RUN_FRAME_RATE
REQUIRED_MODULES = ["torch", "numpy", "sphn", "sentencepiece", "safetensors", "huggingface_hub", "einops",
                    "bitsandbytes", "aiohttp", "httpx", "openai", "websockets", "gradium"]
# Settings that change model behaviour: a resumed run must use the same values.
RESUME_CRITICAL = ["hf_repo", "dtype", "no_q8", "stt_wait_time", "power_threshold", "init_active_speaker",
                   "max_tail_silence_frames", "max_response_seconds"]

logger = logging.getLogger("latency_sweep_t4")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--manifest", type=Path, required=True)
    p.add_argument("--reference-cache", type=Path, required=True, help="Directory written by precompute_reference_embeddings.py.")
    p.add_argument("--retrieval-delay", type=float, nargs="+", default=T4_DEFAULT_DELAYS)
    p.add_argument("--seeds", type=int, nargs="+", default=[base.DEFAULT_SEED])
    p.add_argument("--sample-ids", nargs="+", default=None)
    p.add_argument("--max-samples", type=int, default=None)
    p.add_argument("--output-root", type=Path, default=T4_DIR / "results")
    p.add_argument("--run-name", type=str, default=None, help="Run directory name (use a fixed name to resume).")
    p.add_argument("--resume", action="store_true",
                   help="Continue --run-name if it exists (skip completed runs); start it otherwise.")
    p.add_argument("--retry-failed", action="store_true", help="With --resume: rerun runs recorded as timeout/error.")
    p.add_argument("--dry-run", action="store_true", help="Validate everything without importing torch.")
    p.add_argument("--require-env", action="store_true", help="With --dry-run: missing modules are errors.")

    g = p.add_argument_group("model / memory")
    g.add_argument("--hf-repo", type=str, default="kyutai/moshika-rag-pytorch-bf16")
    g.add_argument("--device", type=str, default="cuda:0")
    g.add_argument("--dtype", choices=["float16", "bfloat16"], default="float16",
                   help="Non-quantized parts of the LM. T4 needs float16.")
    g.add_argument("--no-q8", action="store_true", help="Do not quantize (needs >= 24 GB; for comparisons).")
    g.add_argument("--cuda-graphs", choices=["off", "on"], default="off",
                   help="CUDA graphs only change speed. Off by default: not verified with int8 layers.")
    g.add_argument("--gpu-mem-cap-gb", type=float, default=None,
                   help="Cap PyTorch's allocator (e.g. 15 to emulate a T4 on a larger GPU).")
    g.add_argument("--stt-wait-time", type=float, default=0.5)
    g.add_argument("--max-reference-tokens", type=int, default=64)
    g.add_argument("--vad-window-size", type=int, default=4)
    g.add_argument("--vad-threshold", type=float, default=0.5)
    g.add_argument("--power-threshold", type=int, default=-65)
    g.add_argument("--init-active-speaker", type=str, default="user", choices=["model", "user"])

    g = p.add_argument_group("run control")
    g.add_argument("--max-tail-silence-frames", type=int, default=40)
    g.add_argument("--max-response-seconds", type=float, default=30.0)
    g.add_argument("--sample-timeout", type=float, default=1200.0, help="Wall seconds per run (T4 is slow).")
    g.add_argument("--max-consecutive-failures", type=int, default=3)
    g.add_argument("--speech-db", type=float, default=base.DEFAULT_SPEECH_DB)
    g.add_argument("--audible-db", type=float, default=base.DEFAULT_AUDIBLE_DB)
    g.add_argument("--log-level", type=str, default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    args = p.parse_args(argv)
    args.retrieval_delay = [float(d) for d in args.retrieval_delay]
    args.manifest = args.manifest.resolve()
    args.reference_cache = args.reference_cache.resolve()
    args.output_root = args.output_root.resolve()
    if args.retry_failed and not args.resume:
        p.error("--retry-failed requires --resume")
    return args


# ----------------------------------------------------------------------
# Run directory, resume bookkeeping
# ----------------------------------------------------------------------


def file_sha256(path: str | Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def fingerprint(args: argparse.Namespace, samples: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "args": {k: getattr(args, k) for k in RESUME_CRITICAL},
        "samples": {s["sample_id"]: {"wav_sha256": file_sha256(s["wav_path"]),
                                     "reference_sha256": reference_sha256(s["reference_text"])} for s in samples},
    }


def check_fingerprint(old: dict[str, Any], new: dict[str, Any]) -> list[str]:
    problems = [f"setting {k!r} was {old['args'].get(k)!r}, now {v!r}"
                for k, v in new["args"].items() if old["args"].get(k) != v]
    for sid, h in new["samples"].items():
        if sid in old["samples"] and old["samples"][sid] != h:
            problems.append(f"sample {sid!r}: WAV or reference text changed")
    return problems


def run_dir_for(args: argparse.Namespace) -> Path:
    name = args.run_name or datetime.datetime.now().strftime("t4_%Y%m%d_%H%M%S")
    return args.output_root / name


def read_results(path: Path) -> tuple[list[dict[str, Any]], int]:
    """Records from results.jsonl, tolerating a truncated last line (e.g. a Colab disconnect)."""
    if not path.is_file():
        return [], 0
    records, bad = [], 0
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            bad += 1
    return records, bad


def rewrite_results(path: Path, records: list[dict[str, Any]]) -> None:
    tmp = path.with_suffix(".jsonl.tmp")
    tmp.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records), encoding="utf-8")
    tmp.replace(path)


def plan_runs(samples, args) -> list[tuple[dict[str, Any], int, float, str]]:
    return [(s, seed, d, f"{s['sample_id']}__d{base.delay_tag(d)}__s{seed}")
            for s, seed, d in base.build_plan(samples, args)]


def completed(run_dir: Path, retry_failed: bool, apply: bool) -> tuple[set[str], dict[str, int]]:
    """Run ids to skip. With ``apply``, also repairs/compacts results.jsonl on disk."""
    path = run_dir / "results.jsonl"
    records, bad = read_results(path)
    keep = [r for r in records if r.get("status") == "ok" or not retry_failed]
    if apply and (bad or len(keep) != len(records)):
        rewrite_results(path, keep)
    info = {"records": len(records), "corrupt_lines_dropped": bad, "failed_to_retry": len(records) - len(keep)}
    return {r["run_id"] for r in keep}, info


# ----------------------------------------------------------------------
# Dry run
# ----------------------------------------------------------------------


def dry_run(args: argparse.Namespace) -> int:
    errors, warnings = [], []
    print("=" * 78)
    print("T4 DRY RUN: no torch import, no model loading, no GPU use")
    print("=" * 78)
    all_samples, manifest_errors = base.load_manifest(args.manifest)
    errors += manifest_errors
    samples = base.select_samples(all_samples, args)
    e, w = base.validate_config(args, samples)
    errors += e
    warnings += w

    print(f"\n[manifest] {args.manifest} ({len(samples)}/{len(all_samples)} samples selected)")
    for s in samples:
        info, problem = base.inspect_wav(Path(s["wav_path"]))
        if problem:
            (errors if info is None and not Path(s["wav_path"]).is_file() else warnings).append(f"{s['sample_id']}: {problem}")
        try:
            meta = read_cache_header(cache_path(args.reference_cache, s["reference_text"]), s["reference_text"])
            cache = f"cached {meta['shape']} {meta['dtype']} autocast={meta.get('autocast_dtype')}"
        except (FileNotFoundError, ValueError) as ex:
            errors.append(f"{s['sample_id']}: {ex}")
            cache = "NOT CACHED"
        print(f"  - {s['sample_id']}: {info['duration_s'] if info else '?'} s audio | reference {cache}")

    print(f"\n[delays] {'condition':>9} {'steps':>6} {'effective':>9}")
    for d in args.retrieval_delay:
        with contextlib.suppress(ValueError):
            n = delay_to_steps(d, FRAME_RATE)
            print(f"         {d:>9g} {n:>6} {n / FRAME_RATE:>9.2f}")

    run_dir = run_dir_for(args)
    plan = plan_runs(samples, args)
    exists = (run_dir / "config.json").is_file()
    if exists and not args.resume:
        errors.append(f"{run_dir} already exists: add --resume to continue it")
    done = set()
    if exists and args.resume:
        done, info = completed(run_dir, args.retry_failed, apply=False)
        old = json.loads((run_dir / "config.json").read_text(encoding="utf-8")).get("fingerprint")
        if old and not errors:
            for prob in check_fingerprint(old, fingerprint(args, samples)):
                errors.append(f"resume mismatch: {prob}")
        print(f"\n[resume] {run_dir}: {info}")
    remaining = [r for r in plan if r[3] not in done]
    print(f"\n[plan] {len(plan)} runs ({len(samples)} samples x {len(args.seeds)} seeds x "
          f"{len(args.retrieval_delay)} delays), {len(plan) - len(remaining)} already done, {len(remaining)} to run")
    print(f"  run dir: {run_dir}")
    print(f"  model: {'int8 (q8) ' if not args.no_q8 else ''}{args.dtype}, CUDA graphs {args.cuda_graphs}, STT off, "
          f"retrieval LLM off, reference encoder off (cache)")

    try:
        args.output_root.mkdir(parents=True, exist_ok=True)
        probe = args.output_root / f".write_test_{os.getpid()}"
        probe.write_text("x")
        probe.unlink()
    except OSError as ex:
        errors.append(f"output root not writable: {ex}")
    missing = [m for m in REQUIRED_MODULES if importlib.util.find_spec(m) is None]
    if missing:
        (errors if args.require_env else warnings).append(f"modules not installed: {missing}")
    if sys.version_info < (3, 11):
        (errors if args.require_env else warnings).append(f"Python {platform.python_version()} < 3.11")

    assert "torch" not in sys.modules, "dry run must not import torch"
    print("\n  confirmed: torch was not imported")
    for x in warnings:
        print(f"WARNING: {x}")
    for x in errors:
        print(f"ERROR: {x}")
    print(f"\nT4 DRY RUN {'FAILED' if errors else 'PASSED'} ({len(errors)} errors, {len(warnings)} warnings)")
    return 1 if errors else 0


# ----------------------------------------------------------------------
# Real run
# ----------------------------------------------------------------------


class NullSTT:
    """Stands in for LocalSpeechToText. The model's input is the raw audio; here the STT only fed
    transcripts/VAD into the retrieval-LLM context, which the fixed reference does not use."""

    text_tokenizer = None
    vad_callback = None

    def __init__(self) -> None:
        self._closed = asyncio.Event()

    async def start_up(self) -> None:
        self._closed = asyncio.Event()

    async def shutdown(self) -> None:
        self._closed.set()

    async def send_audio(self, audio) -> None:
        return None

    async def flush(self) -> None:
        return None

    async def __aiter__(self):
        await self._closed.wait()
        return
        yield  # makes this an async generator that yields nothing


def run_real(args: argparse.Namespace) -> int:
    all_samples, manifest_errors = base.load_manifest(args.manifest)
    samples = base.select_samples(all_samples, args)
    errors = manifest_errors + base.validate_config(args, samples)[0]
    errors += [f"missing WAV for {s['sample_id']}" for s in samples if not Path(s["wav_path"]).is_file()]
    for s in samples:
        try:
            read_cache_header(cache_path(args.reference_cache, s["reference_text"]), s["reference_text"])
        except (FileNotFoundError, ValueError) as ex:
            errors.append(f"{s['sample_id']}: {ex} (run precompute_reference_embeddings.py first)")
    run_dir = run_dir_for(args)
    resumed = (run_dir / "config.json").is_file()
    if resumed and not args.resume:
        errors.append(f"{run_dir} already exists: add --resume to continue it")
    fp = fingerprint(args, samples) if not errors else None
    if resumed and not errors:
        old = json.loads((run_dir / "config.json").read_text(encoding="utf-8")).get("fingerprint") or {}
        errors += [f"resume mismatch: {x}" for x in check_fingerprint(old, fp)] if old else []
    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        return 2

    for sub in ("audio", "traces", "logs"):
        (run_dir / sub).mkdir(parents=True, exist_ok=True)
    base.setup_logging(args.log_level, run_dir / "logs" / "runner.log")
    done, info = completed(run_dir, args.retry_failed, apply=True) if resumed else (set(), {})
    plan = plan_runs(samples, args)
    todo = [r for r in plan if r[3] not in done]
    logger.info("run directory %s (%s); %d planned, %d done, %d to run", run_dir,
                "resumed" if resumed else "new", len(plan), len(plan) - len(todo), len(todo))
    session = {"started_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
               "resumed": resumed, "resume_info": info, "metadata": base.collect_metadata(),
               "args": {k: (str(v) if isinstance(v, Path) else v) for k, v in vars(args).items()}}
    if not resumed:
        config = base.config_dict(args, samples, FRAME_RATE)
        config["variant"] = "t4_low_memory"
        config["fingerprint"] = fp
        config["metadata"] = session["metadata"]
        base.write_json(run_dir / "config.json", config)
    with (run_dir / "logs" / "sessions.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(session, default=str) + "\n")
    if not todo:
        logger.info("nothing to do: all planned runs are complete")
        write_status(run_dir, plan, "finished")
        return 0

    if args.cuda_graphs == "off":
        os.environ["NO_CUDA_GRAPH"] = "1"  # read by moshi.utils.compile on every call

    import torch

    if not torch.cuda.is_available():
        logger.error("CUDA is not available")
        return 2
    device = args.device
    major, minor = torch.cuda.get_device_capability(device)
    if args.dtype == "bfloat16" and major < 8:
        logger.error("bfloat16 needs sm_80+; this GPU is sm_%d%d (use --dtype float16)", major, minor)
        return 2
    total = torch.cuda.get_device_properties(device).total_memory
    if args.gpu_mem_cap_gb:
        torch.cuda.set_per_process_memory_fraction(min(1.0, args.gpu_mem_cap_gb * 1024**3 / total), device)
        logger.info("PyTorch allocator capped at %.1f GB", args.gpu_mem_cap_gb)

    from gpu_memory import GpuMemoryLog

    memlog = GpuMemoryLog(run_dir / "logs" / "gpu_memory.jsonl", device)
    memlog.log("process_start", gpu=torch.cuda.get_device_name(device), capability=f"sm_{major}{minor}")

    sys.path.insert(0, str(MOSHI_PKG_PARENT))
    import moshi.server as moshi_server
    from moshi.inference_utils.utils import seed_all
    from moshi.models import loaders
    from safetensors.torch import load_file

    from latency_job import LatencyInferenceJob
    from q8_moshirag import build_lm_gen, count_linear_types, load_q8_lm

    class _NoLLMReferenceGenerator:
        def __init__(self, *a: Any, **k: Any) -> None:
            pass

        def warmup(self) -> None:
            pass

        async def generate_reference_text(self, *a: Any, **k: Any):
            raise RuntimeError("LLM retrieval is disabled in the latency experiment")

    moshi_server.LLMReferenceGenerator = _NoLLMReferenceGenerator  # type: ignore[assignment]

    t0 = time.monotonic()
    seed_all(args.seeds[0])
    info_ckpt = loaders.CheckpointInfo.from_hf_repo(args.hf_repo)
    text_tokenizer = info_ckpt.get_text_tokenizer()
    mimi = info_ckpt.get_mimi(device=device)
    mimi.set_profile(False)
    memlog.log("mimi_loaded")
    lm = load_q8_lm(info_ckpt, device, dtype=getattr(torch, args.dtype), quantize=not args.no_q8,
                    on_stage=lambda stage: memlog.log(stage))
    lm_gen = build_lm_gen(lm, info_ckpt, args.init_active_speaker)
    memlog.log("lm_gen_built", linear_types=count_linear_types(lm))
    state = moshi_server.ServerState(
        mimi=mimi, text_tokenizer=text_tokenizer, lm_gen=lm_gen,
        reference_encoder_url="disabled://precomputed-reference-cache",
        stt_wait_time=args.stt_wait_time, gradium_stt=False, device=device, rag_timeout=10.0,
        max_reference_tokens=args.max_reference_tokens, batch_size=1, vad_window_size=args.vad_window_size,
        vad_threshold=args.vad_threshold, init_active_speaker=args.init_active_speaker,
        power_threshold=args.power_threshold,
    )
    state.mimi_copy = None  # spare Mimi copy is only used by the live web server
    gc.collect()
    torch.cuda.empty_cache()
    memlog.log("server_state_built")
    state.warmup()
    memlog.log("warmup_done", load_wall_s=round(time.monotonic() - t0, 1))

    reference_tensors: dict[str, Any] = {}
    for s in samples:
        text = s["reference_text"]
        if text not in reference_tensors:
            reference_tensors[text] = load_file(str(cache_path(args.reference_cache, text)))["embedding"]

    runtime = {"variant": "t4_low_memory", "gpu": torch.cuda.get_device_name(device),
               "capability": f"sm_{major}{minor}", "torch": torch.__version__, "q8": not args.no_q8,
               "dtype": args.dtype, "cuda_graphs": args.cuda_graphs, "stt": "disabled",
               "frame_rate": float(state.runner.mimi.frame_rate), "stt_wait_steps": state.stt_wait_steps,
               "rag_token_id": lm_gen.lm_model.rag_token_id,
               "sampling": {k: getattr(lm_gen, k, None) for k in ("use_sampling", "temp", "temp_text", "top_k", "top_k_text")},
               "linear_types": count_linear_types(lm), "load_wall_s": round(time.monotonic() - t0, 1)}
    with (run_dir / "logs" / "sessions.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps({"runtime": runtime}) + "\n")
    if not resumed:
        config = json.loads((run_dir / "config.json").read_text(encoding="utf-8"))
        config["runtime"] = runtime
        base.write_json(run_dir / "config.json", config)

    status = "running"
    try:
        with torch.no_grad():
            status = asyncio.run(_sweep(state, NullSTT(), todo, len(plan), args, run_dir, reference_tensors,
                                        memlog, seed_all, LatencyInferenceJob, runtime))
    except KeyboardInterrupt:
        status = "interrupted"
    memlog.log("sweep_end", status=status)
    write_status(run_dir, plan, status)
    return 0 if status == "finished" else 1


def write_status(run_dir: Path, plan, status: str) -> None:
    records, _ = read_results(run_dir / "results.jsonl")
    counts: dict[str, int] = {}
    for r in records:
        counts[r.get("status", "?")] = counts.get(r.get("status", "?"), 0) + 1
    ok_ids = {r["run_id"] for r in records if r.get("status") == "ok"}
    remaining = [run_id for *_, run_id in plan if run_id not in ok_ids]
    base.write_json(run_dir / "run_status.json", {
        "status": "finished" if status == "finished" and not remaining else status,
        "counts": counts, "planned_runs": len(plan), "remaining_runs": remaining,
        "updated_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
    })


async def _sweep(state, stt, todo, n_planned, args, run_dir, reference_tensors, memlog, seed_all, job_cls, runtime):
    import torch

    main_task = asyncio.current_task()
    assert main_task is not None
    asyncio.get_running_loop().add_signal_handler(signal.SIGTERM, main_task.cancel)
    results_path = run_dir / "results.jsonl"
    step_task = asyncio.create_task(state._step_loop(), name="batched-step-loop")
    consecutive_failures = 0
    try:
        for i, (sample, seed, delay, run_id) in enumerate(todo, 1):
            if step_task.done():
                raise RuntimeError(f"batched step loop stopped: {step_task.exception()!r}")
            logger.info("=== run %d/%d (of %d planned): %s ===", i, len(todo), n_planned, run_id)
            torch.cuda.reset_peak_memory_stats(args.device)
            t0 = time.monotonic()
            record = await base._run_one(state, stt, sample, seed, delay, run_id, args, run_dir,
                                         reference_tensors, seed_all, job_cls)
            mem = memlog.log("run_end", run_id=run_id, status=record["status"])
            record.update({
                "variant": "t4_low_memory", "q8": runtime["q8"], "dtype": runtime["dtype"], "gpu": runtime["gpu"],
                "run_wall_s": round(time.monotonic() - t0, 1),
                "gpu_peak_allocated_mb": mem.get("peak_allocated_mb"),
                "gpu_peak_reserved_mb": mem.get("peak_reserved_mb"),
                "gpu_device_used_mb": mem.get("device_used_mb"),
            })
            base.append_jsonl(results_path, record)
            logger.info("run %s: status=%s stop=%s [RET]=%s injection=%s wall=%.0fs peak=%.0f MB", run_id,
                        record["status"], record["stop_reason"], record["retrieval_trigger_time"],
                        record["reference_injection_time"], record["run_wall_s"], mem.get("peak_allocated_mb") or -1)
            consecutive_failures = 0 if record["status"] == "ok" else consecutive_failures + 1
            if consecutive_failures >= args.max_consecutive_failures:
                logger.error("aborting: %d consecutive failed runs", consecutive_failures)
                return "aborted"
        return "finished"
    except asyncio.CancelledError:
        logger.warning("sweep interrupted; rerun the same command with --resume to continue")
        return "interrupted"
    finally:
        step_task.cancel()
        with contextlib.suppress(asyncio.CancelledError, Exception):
            await step_task


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return dry_run(args) if args.dry_run else run_real(args)


if __name__ == "__main__":
    sys.exit(main())
