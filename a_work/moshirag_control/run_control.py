"""Run MoshiRAG under each control condition on every manifest question.

Dry run (login node, no torch): validates the manifest and prints every plan.

    python3 a_work/moshirag_control/run_control.py --manifest a_work/moshirag_control/configs/control_manifest.jsonl --dry-run

Real run: a_work/moshirag_control/run_control.slurm (needs REFERENCE_ENCODER_URL).
"""
from __future__ import annotations

import argparse
import asyncio
import contextlib
import datetime
import json
import signal
import sys
import time
import traceback
import wave
from copy import deepcopy
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
EXP_DIR = REPO / "experiments/async_retrieval_latency"
sys.path[:0] = [str(HERE), str(EXP_DIR), str(EXP_DIR / "scripts")]

from conditions import CLIPS, CONDITIONS, MULTI_EVIDENCE_ONLY, build_plan  # noqa: E402
from control import CLIP  # noqa: E402
from run_latency_sweep import (  # noqa: E402
    DEFAULT_SEED, DEFAULT_SPEECH_DB, MOSHI_PKG_PARENT, append_jsonl, collect_metadata, setup_logging, write_json,
)

import logging  # noqa: E402

logger = logging.getLogger("control_run")


def parse_args(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--manifest", type=Path, required=True)
    p.add_argument("--conditions", nargs="+", default=list(CONDITIONS), choices=CONDITIONS)
    p.add_argument("--seeds", type=int, nargs="+", default=[DEFAULT_SEED])
    p.add_argument("--sample-ids", nargs="+", default=None)
    p.add_argument("--multi-evidence-only", action="store_true")
    p.add_argument("--output-root", type=Path, default=HERE / "results")
    p.add_argument("--clip-dir", type=Path, default=HERE / "configs/clips")
    p.add_argument("--run-name", default=None)
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--hf-repo", default="kyutai/moshika-rag-pytorch-bf16")
    p.add_argument("--device", default="cuda:0")
    p.add_argument("--stt-wait-time", type=float, default=0.5)
    p.add_argument("--max-reference-tokens", type=int, default=64)
    p.add_argument("--max-tail-silence-frames", type=int, default=40)
    p.add_argument("--max-response-seconds", type=float, default=30.0)
    p.add_argument("--sample-timeout", type=float, default=300.0)
    p.add_argument("--speech-db", type=float, default=DEFAULT_SPEECH_DB)
    p.add_argument("--log-level", default="INFO")
    return p.parse_args(argv)


def load_samples(args) -> list[dict[str, Any]]:
    samples = []
    with open(args.manifest, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                s = json.loads(line)
                s["wav_path"] = str((args.manifest.parent / s["wav"]).resolve())
                samples.append(s)
    if args.sample_ids:
        samples = [s for s in samples if s["sample_id"] in set(args.sample_ids)]
    if args.multi_evidence_only:
        samples = [s for s in samples if len(s["events"]) >= 2]
    return samples


def build_runs(samples, args):
    """(sample, condition, seed, plan) for every run. The 'ours' conditions equal their progress
    counterparts with one evidence item, so they only run on multi-evidence samples."""
    runs = []
    for s in samples:
        for cond in args.conditions:
            if cond in MULTI_EVIDENCE_ONLY and len(s["events"]) < 2:
                continue
            for seed in args.seeds:
                runs.append((s, cond, seed, build_plan(cond, s["events"], s["units"])))
    return runs


def load_clips(clip_dir: Path) -> dict[str, tuple[dict, bytes]]:
    """Clip metadata and 16-bit PCM bytes, for every clip file present."""
    clips = {}
    for name in CLIPS:
        meta_path, wav_path = clip_dir / f"{name}.json", clip_dir / f"{name}.wav"
        if meta_path.is_file() and wav_path.is_file():
            with wave.open(str(wav_path), "rb") as wf:
                clips[name] = (json.loads(meta_path.read_text(encoding="utf-8")), wf.readframes(wf.getnframes()))
    return clips


def clips_needed(runs) -> set[str]:
    return {g.clip for _, _, _, plan in runs for g in plan.segments if g.mode == CLIP}


def dry_run(args) -> int:
    samples = load_samples(args)
    missing = [s["sample_id"] for s in samples if not Path(s["wav_path"]).is_file()]
    missing += [f"clip:{c}" for c in clips_needed(build_runs(samples, args)) - load_clips(args.clip_dir).keys()]
    for s, cond, seed, plan in build_runs(samples, args):
        segs = ", ".join(f"{g.start_s:g}s {g.mode}" + (f" '{g.phrase}'" if g.phrase else "")
                         + (f" {g.clip}->{g.after}" if g.clip else "") for g in plan.segments)
        injs = ", ".join(f"{i.time_s:g}s {i.label}" for i in plan.injections)
        print(f"{s['sample_id'][:28]:<30}{cond:<10} seed={seed}  segments=[{segs or 'none'}]  injections=[{injs}]")
    print(f"\n{len(build_runs(samples, args))} runs over {len(samples)} samples; missing inputs: {missing or 'none'}")
    return 1 if missing else 0


def run_real(args) -> int:
    samples = load_samples(args)
    runs = build_runs(samples, args)
    name = args.run_name or datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = args.output_root / name
    (run_dir / "logs").mkdir(parents=True, exist_ok=False)
    setup_logging(args.log_level, run_dir / "logs" / "runner.log")
    config = {"args": {k: str(v) for k, v in vars(args).items()}, "runs": len(runs), "metadata": collect_metadata()}
    write_json(run_dir / "config.json", config)

    sys.path.insert(0, str(MOSHI_PKG_PARENT))
    import torch
    import moshi.server as moshi_server
    from moshi.inference_utils import load_models
    from moshi.inference_utils.utils import get_conditioning_remote_async, get_reference_encoder_url, seed_all
    from moshi.stt.local_stt import LocalSpeechToText

    from controlled_job import ControlledJob

    class _NoLLM:
        def __init__(self, *a, **k): pass
        def warmup(self): pass
        async def generate_reference_text(self, *a, **k): raise RuntimeError("retrieval is scheduled by the trace")

    moshi_server.LLMReferenceGenerator = _NoLLM  # type: ignore[assignment]
    encoder_url = get_reference_encoder_url()
    model_args = argparse.Namespace(
        hf_repo=args.hf_repo, moshi_weight=None, mimi_weight=None, tokenizer=None, config=None, device=args.device,
        dtype=torch.bfloat16, cfg_coef=1.0, batch_size=1, init_active_speaker="user",
    )
    seed_all(args.seeds[0])
    t0 = time.monotonic()
    mimi, text_tokenizer, lm_gen = load_models(model_args)
    import numpy as np
    mimi_enc = deepcopy(mimi)  # fresh, non-streaming copy for encoding silence and clips
    dep_q = lm_gen.lm_model.dep_q
    frame = int(mimi.sample_rate / mimi.frame_rate)

    def encode_pcm(pcm: np.ndarray) -> torch.Tensor:
        with torch.no_grad():
            codes = mimi_enc.encode(torch.from_numpy(pcm)[None, None].to(args.device))
        return codes[0, :dep_q].to(args.device)

    audio_codes = {"silence": encode_pcm(np.zeros(12 * frame, dtype=np.float32))[:, 6]}
    clip_tokens = {}
    for name, (meta, raw) in load_clips(args.clip_dir).items():
        pcm = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
        codes = encode_pcm(pcm)
        if codes.shape[1] < meta["frames"]:
            raise RuntimeError(f"clip {name}: {codes.shape[1]} code frames < {meta['frames']} steps")
        audio_codes[name] = codes[:, :meta["frames"]]
        clip_tokens[name] = meta["text_tokens"]
    del mimi_enc
    stt = LocalSpeechToText(deepcopy(mimi))
    state = moshi_server.ServerState(
        mimi=mimi, text_tokenizer=text_tokenizer, lm_gen=lm_gen, reference_encoder_url=encoder_url,
        stt_wait_time=args.stt_wait_time, gradium_stt=False, device=args.device, rag_timeout=10.0,
        max_reference_tokens=args.max_reference_tokens, batch_size=1, vad_window_size=4, vad_threshold=0.5,
        init_active_speaker="user", power_threshold=-65,
    )
    state.warmup()
    config["runtime"] = {"model_load_wall_s": round(time.monotonic() - t0, 1), "torch": torch.__version__,
                         "gpu": torch.cuda.get_device_name(0)}
    write_json(run_dir / "config.json", config)

    async def sweep():
        asyncio.get_running_loop().add_signal_handler(signal.SIGTERM, asyncio.current_task().cancel)
        step_task = asyncio.create_task(state._step_loop())
        counts = {"ok": 0, "timeout": 0, "error": 0}
        try:
            tensors = {}
            for _, _, _, plan in runs:
                for inj in plan.injections:
                    if inj.text not in tensors:
                        t = await get_conditioning_remote_async(text=inj.text, encoder_url=encoder_url)
                        tensors[inj.text] = t.squeeze(0).cpu()
            logger.info("pre-encoded %d distinct references", len(tensors))
            for i, (sample, cond, seed, plan) in enumerate(runs, 1):
                run_id = f"{sample['sample_id']}__{cond}__s{seed}"
                logger.info("=== run %d/%d: %s ===", i, len(runs), run_id)
                seed_all(seed)
                job = ControlledJob(state, sample=sample, plan=plan, run_id=run_id, run_dir=run_dir, seed=seed,
                                    reference_tensors=tensors, max_tail_silence=args.max_tail_silence_frames,
                                    max_response_seconds=args.max_response_seconds, speech_db=args.speech_db, stt=stt,
                                    clip_tokens=clip_tokens, audio_codes=audio_codes)
                await state.wait_acquire_slot(job)
                status, error = "ok", None

                async def run_job():
                    async with asyncio.TaskGroup() as tg:
                        await job.run(tg)
                try:
                    await asyncio.wait_for(run_job(), timeout=args.sample_timeout)
                except TimeoutError:
                    status, error = "timeout", f"exceeded {args.sample_timeout}s"
                except asyncio.CancelledError:
                    job.write_outputs(status="interrupted", reason="cancelled")
                    raise
                except Exception as e:  # noqa: BLE001
                    status, error = "error", "".join(traceback.format_exception(e))
                    logger.error("run %s failed:\n%s", run_id, error)
                finally:
                    await state.release_slot(job.slot_idx)
                if status != "ok":
                    job.write_outputs(status=status, reason=status, error=error)
                counts[status] += 1
                append_jsonl(run_dir / "results.jsonl", {"run_id": run_id, "status": status, "error": error,
                                                         "lm_steps": job._lm_step, "output_steps": len(job.model_text)})
            return {"status": "finished", "counts": counts}
        except asyncio.CancelledError:
            return {"status": "interrupted", "counts": counts}
        finally:
            step_task.cancel()
            with contextlib.suppress(asyncio.CancelledError, Exception):
                await step_task

    with torch.no_grad():
        status = asyncio.run(sweep())
    write_json(run_dir / "run_status.json", status)
    logger.info("finished: %s", status)
    import summarize
    summarize.main(run_dir)
    return 0 if status["status"] == "finished" else 1


def main(argv=None) -> int:
    args = parse_args(argv)
    args.manifest = args.manifest.resolve()
    args.output_root = args.output_root.resolve()
    return dry_run(args) if args.dry_run else run_real(args)


if __name__ == "__main__":
    sys.exit(main())
