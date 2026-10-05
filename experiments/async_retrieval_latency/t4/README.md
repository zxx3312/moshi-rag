# Async retrieval latency — low-memory version (Colab T4, 16 GB)

Same experiment as the A100/Slurm version in the parent directory: same `LatencyInferenceJob`,
the same frame-based injection at `request_step + round(delay × 12.5)`, the same metrics and the
same `analysis/analyze_latency.py`. The A100 files are unchanged. The default delays here are
`0, 1, 2, 3, 5, 8` s (effective `0, 1.04, 2.00, 3.04, 5.04, 8.00` s after rounding to 80 ms frames).

**Read this first:** T4 results come from **int8-quantized MoshiRAG in float16**, not the
bf16 model. Treat them as their own condition; don't pool them with A100 bf16 runs unless
you have checked that the two agree.

## What is different from the A100 version, and why

| Change | Why | Effect on the experiment |
|---|---|---|
| LM quantized to int8 while loading (`q8_moshirag.py`) | bf16/fp16 weights alone are 15.4 GB; a T4 has ~15 GB | **Changes numerics** (see below) |
| float16 instead of bfloat16 | T4 (sm_75) has no bf16 | Changes numerics slightly |
| Reference embeddings precomputed once (`precompute_reference_embeddings.py`), encoder never loaded during the sweep | the ARC encoder alone is 12.1 GB | None if the cache is computed on an A100; T4-computed embeddings use fp16 autocast instead of bf16 |
| No STT | the model's input is raw audio; the STT only fed the retrieval-LLM context, which a fixed reference ignores | `user_transcript_stt` is empty; the 0.5 s wait between `[RET]` and the request is kept |
| No retrieval LLM | fixed reference, as in the A100 version | none |
| CUDA graphs off by default (`--cuda-graphs on` to try) | not verified with int8 layers | speed only |
| Spare Mimi copy freed | only used by the live web server | none |

Other runtime conditions are the same as the A100 version: batch size 1, runs in sequence, the model loaded once, and the RNG re-seeded before every run.

### The q8 situation (checked, not assumed)

- `kyutai/moshika-rag-pytorch-bf16` ships **no** q8 checkpoint. The repo's `scripts/export_quantized.py`
  would need ~28 GB of GPU memory to make one.
- The repo's q8 **load path is broken** in this fork. `models/loaders.get_moshi_lm` casts every
  `*.weight_scb` int8 scale to the model dtype, and `QLinear.forward` then raises. This is reproduced in `tests/test_q8_cpu.py`.
- `q8_moshirag.py` builds the LM on `meta`, streams the bf16 checkpoint one layer at a time, and
  quantizes each layer with the repo's own `replace_linear_with_qlinear`. On a tiny model it is
  **bit-identical** to quantizing the fully loaded model with the repo's function, and sampling gives identical tokens.
- **Unknown until run on a GPU:** whether int8 changes MoshiRAG's real behaviour (when `[RET]` fires, what it says).
  Before relying on T4 results, run the same sample and seed with and without q8 on a large GPU
  (`--no-q8 --dtype bfloat16` versus the default) and compare the transcripts.

### Expected memory (estimate from the checkpoint header, not measured)

| Part | Size |
|---|---|
| int8 Linear weights (7.38 B params) | ~7.4 GB |
| fp16 embeddings / norms / conditioner (0.31 B params) | ~0.6 GB |
| KV cache (context 3000, 32 layers, fp16) | ~1.6 GB |
| Mimi (fp32) + CUDA context + workspaces | ~1 GB |
| **Total** | **~10–11 GB of ~15 GB** |

Precompute (separate process): the ARC encoder in fp32 is ~12.1 GB (`--weights-dtype float16` halves it, at the cost of a deviation).

## Files

```
t4/
  run_latency_sweep_t4.py           sweep runner: q8 load, cached embeddings, GPU memory log, --resume, --dry-run
  precompute_reference_embeddings.py   one-time ARC encoding -> REF_CACHE/ref_<sha>.safetensors
  q8_moshirag.py                    streaming int8 loader for the MoshiRAG LM
  reference_cache.py, gpu_memory.py helpers
  configs/samples_small.jsonl       5 example questions for step 3 (pick your own evaluation set)
  requirements-colab.txt            pinned versions (as verified on the cluster, Python 3.12)
  colab_runner.ipynb                the notebook
  tests/                            CPU checks (see "What has been verified")
```

## Running on Colab

Open `t4/colab_runner.ipynb` in Colab (File → Upload notebook, or open it from GitHub), select a T4
runtime, and run the cells in order. Outline:

1. `git clone --branch exp/async-retrieval-latency <your fork>` → `/content/moshi-rag`.
   The branch must be pushed first. For a private fork, put a GitHub token in the URL.
2. `pip install -r experiments/async_retrieval_latency/t4/requirements-colab.txt`
3. `huggingface_hub.login()` with a read token that has access to `meta-llama/Llama-3.2-3B-Instruct`
   (only its ~9 MB tokenizer is downloaded, and only by the precompute step).
4. Make the question WAVs with Piper (`scripts/make_tts_question.py`) in a separate venv.
5. Precompute embeddings once into Drive (`--cache-dir .../reference_cache`).
6. Then the three steps. Each is one command, and rerunning it after a disconnect resumes it:

```bash
EXP=experiments/async_retrieval_latency
ARGS="--reference-cache $CACHE --output-root $RESULTS --resume"

# 1) 1 sample x 1 delay
python $EXP/t4/run_latency_sweep_t4.py --manifest $EXP/configs/samples.jsonl --retrieval-delay 3 --run-name step1_1x1 $ARGS
# 2) 1 sample x all delays (0 1 2 3 5 8)
python $EXP/t4/run_latency_sweep_t4.py --manifest $EXP/configs/samples.jsonl --run-name step2_1xall $ARGS
# 3) small multi-sample sweep (5 x 6 = 30 runs)
python $EXP/t4/run_latency_sweep_t4.py --manifest $EXP/t4/configs/samples_small.jsonl --run-name step3_small $ARGS
# summary (CPU)
python $EXP/analysis/analyze_latency.py $RESULTS/step3_small
```

Add `--dry-run` to any of them first: it checks the WAVs, the embedding cache, the resume state and
the plan, without importing torch.

### Resume

- Results are appended to `results.jsonl` and fsynced after every run. A run cut off by a disconnect
  has no record, so it is simply rerun.
- `--resume` with the same `--run-name` skips completed runs. It refuses to continue if a
  behaviour-relevant setting changed (q8, dtype, STT wait, stop rules, ...) or if a sample's WAV or
  reference text changed. Adding samples, delays or seeds to an existing run is allowed.
- A last line half-written by a crash is dropped. `--retry-failed` reruns runs recorded as `timeout` or `error`.
- Each session (command, resume info, metadata) is appended to `logs/sessions.jsonl`.

## Outputs (per run directory, on Drive)

The same layout as the A100 version (`config.json`, `results.jsonl`, `run_status.json`, `traces/`,
`audio/*_model.wav` and `*_stereo.wav`, `logs/runner.log`), plus:

- `logs/gpu_memory.jsonl`: allocated, reserved and peak memory for PyTorch, and used/total for the
  whole device, after each load stage (`mimi_loaded`, `transformer_layers_loaded_q8`, ...,
  `warmup_done`) and after each run.
- In each `results.jsonl` record: `gpu_peak_allocated_mb`, `gpu_peak_reserved_mb`,
  `gpu_device_used_mb`, `run_wall_s`, `variant`, `q8`, `dtype` and `gpu`.

## Validating the T4 setup on the campus cluster (optional)

`--gpu-mem-cap-gb 15` caps PyTorch's allocator, which emulates a T4's memory budget on an A100.
It does not emulate the T4's speed or its lack of bf16.
`--no-q8 --dtype bfloat16` runs the same code unquantized, for the q8-vs-bf16 comparison.

## What has been verified

| Check | How | Result |
|---|---|---|
| repo q8 load path | `tests/test_q8_cpu.py`, tiny random model, CPU | fails: scales cast to fp16, forward raises |
| streaming q8 loader = repo quantizer | same | bit-identical weights; identical sampled tokens |
| unquantized streaming load = `get_moshi_lm` | same | identical |
| full per-run pipeline (real Mimi, tiny q8 LM, NullSTT, `LatencyInferenceJob`, `_run_one`, metrics) | `tests/test_pipeline_cpu.py`, CPU, `[RET]` forced at one step | injection exactly at +0 / +13 frames; pre-injection tokens identical across delays; outputs diverge after injection |
| resume bookkeeping, NullSTT | `tests/test_runner_offline.py` | pass |
| dry run, syntax, notebook JSON | login node | pass |
| **anything on a real GPU** (T4 or A100): memory, speed, bitsandbytes on sm_75, the real 7B model, the real ARC encoder precompute, CUDA graphs with int8 | — | **not run** |
