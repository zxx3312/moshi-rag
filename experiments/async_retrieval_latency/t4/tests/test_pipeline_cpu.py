"""CPU end-to-end check of one sweep run, with the real Mimi codec and a *tiny random* q8 LM.

Exercises the same code the T4 sweep runs: q8 loader -> LMGen -> ServerState batched step loop ->
LatencyInferenceJob (feed loop, NullSTT, frame-scheduled injection, outputs) -> _run_one -> metrics.
The tiny model's text logits get one forced [RET] at a fixed step, so the injection schedule can be
checked exactly. This says nothing about MoshiRAG's real behaviour, speed or GPU memory.

Needs the cached kyutai/moshika-rag-pytorch-bf16 files (Mimi + text tokenizer) and
configs/audio/tallest_waterfall.wav.

    HF_HUB_OFFLINE=1 python experiments/async_retrieval_latency/t4/tests/test_pipeline_cpu.py
"""

from __future__ import annotations

import argparse
import asyncio
import copy
import json
import sys
import tempfile
from pathlib import Path

import torch

HERE = Path(__file__).resolve()
T4_DIR = HERE.parents[1]
EXP_DIR = T4_DIR.parent
REPO = HERE.parents[4]
sys.path[:0] = [str(REPO / "moshi"), str(T4_DIR), str(EXP_DIR / "scripts"), str(EXP_DIR), str(HERE.parent)]

import moshi.server as moshi_server  # noqa: E402
from moshi.inference_utils.utils import seed_all  # noqa: E402
from moshi.models import loaders  # noqa: E402

import run_latency_sweep as base  # noqa: E402
from latency_job import LatencyInferenceJob  # noqa: E402
from q8_moshirag import build_lm_gen, load_q8_lm  # noqa: E402
from run_latency_sweep_t4 import NullSTT  # noqa: E402
from test_q8_cpu import TINY, make_checkpoint  # noqa: E402

FORCED_RET_CALL = 55  # forward_text call index (per run) at which [RET] is forced
WAV = EXP_DIR / "configs" / "audio" / "tallest_waterfall.wav"


class _NoLLM:
    def __init__(self, *a, **k):
        pass

    def warmup(self):
        pass


def main() -> int:
    torch.set_grad_enabled(False)
    if not WAV.is_file():
        print(f"SKIP: {WAV} not found")
        return 0
    moshi_server.LLMReferenceGenerator = _NoLLM
    real = loaders.CheckpointInfo.from_hf_repo("kyutai/moshika-rag-pytorch-bf16")
    mimi = real.get_mimi(device="cpu")
    tokenizer = real.get_text_tokenizer()

    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        tiny_cfg = copy.deepcopy(TINY) | {"card": 2048}  # must match Mimi's codebook size
        info = make_checkpoint(tmp, cfg=tiny_cfg)
        lm = load_q8_lm(info, device="cpu", dtype=torch.float16, quantize=True)

        calls = {"n": 0}

        def force_ret(module, inputs, output):
            # Exactly one [RET] per run: forced at FORCED_RET_CALL, suppressed everywhere else
            # (the random tiny model would otherwise sample it ~1% of steps).
            calls["n"] += 1
            output = output.clone()
            output[..., lm.rag_token_id] = 1e4 if calls["n"] == FORCED_RET_CALL else -1e4
            return output

        lm.text_linear.register_forward_hook(force_ret)

        def seed_and_reset(seed: int) -> None:
            calls["n"] = 0
            seed_all(seed)

        lm_gen = build_lm_gen(lm, info, init_active_speaker="user")
        state = moshi_server.ServerState(
            mimi=mimi, text_tokenizer=tokenizer, lm_gen=lm_gen, reference_encoder_url="disabled://test",
            stt_wait_time=0.5, device="cpu", batch_size=1, init_active_speaker="user", power_threshold=-65,
        )
        state.warmup()
        reference = "Fixed reference."
        sample = {"sample_id": "tiny", "wav_path": str(WAV), "reference_text": reference,
                  "question": "q", "answer": None}
        args = argparse.Namespace(max_tail_silence_frames=40, max_response_seconds=8.0, sample_timeout=600.0,
                                  speech_db=-45.0, audible_db=-45.0)
        run_dir = tmp / "run"
        for sub in ("audio", "traces", "logs"):
            (run_dir / sub).mkdir(parents=True)

        async def sweep() -> list[dict]:
            step_task = asyncio.create_task(state._step_loop())
            out = []
            try:
                for delay in (0.0, 1.0):
                    run_id = f"tiny__d{base.delay_tag(delay)}__s1"
                    out.append(await base._run_one(state, NullSTT(), sample, 1, delay, run_id, args, run_dir,
                                                   {reference: torch.randn(5, TINY["dim"])}, seed_and_reset,
                                                   LatencyInferenceJob))
            finally:
                step_task.cancel()
            return out

        records = asyncio.run(sweep())
        traces = [json.loads((run_dir / r["trace_path"]).read_text()) for r in records]
        for r, t, delay_steps in zip(records, traces, (0, 13)):
            assert r["status"] == "ok", r.get("error")
            ev = t["retrieval_events"]
            assert len(ev) == 1, ev
            ev = ev[0]
            assert ev["request_step"] - ev["trigger_step"] == 6, ev
            assert ev["injection_step"] - ev["request_step"] == delay_steps, ev
            assert ev["injection_num_steps"] == 5, ev
            assert (run_dir / r["output_audio_path"]).is_file() and (run_dir / r["stereo_audio_path"]).is_file()
            print(f"  ok: delay {r['retrieval_delay_condition']}s: [RET] step {ev['trigger_step']}, request "
                  f"{ev['request_step']}, injection {ev['injection_step']} (+{delay_steps}), stop={r['stop_reason']}, "
                  f"trigger_to_injection={r['trigger_to_injection_s']}s")
        k = min(t["retrieval_events"][0]["injection_step"] for t in traces)
        same = traces[0]["model_text"][:k] == traces[1]["model_text"][:k]
        diff_after = traces[0]["model_text"][k:k + 40] != traces[1]["model_text"][k:k + 40]
        assert same, "pre-injection tokens differ across delays on CPU"
        print(f"  ok: first {k} text tokens identical across delays; differ after injection: {diff_after}")
    print("CPU PIPELINE CHECK PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
