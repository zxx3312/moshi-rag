# Async retrieval latency stress test (MoshiRAG baseline)

Phase 1 of *Computation-Aware Turn-Taking for Full-Duplex Spoken Conversational Agents*:
an empirical baseline-failure analysis, not a new method.

## Research question

Does MoshiRAG's conversational behavior degrade when asynchronous retrieval takes longer?
Examples: long filler, uninformative speech, premature factual answers, pre/post-RAG
contradictions, abnormal silence.
The hypothesis may be wrong. If MoshiRAG stays natural at long latencies, that is a valid result and must be reported as such.

Note: the upstream README already says *"MoshiRAG is sensitive to retrieval delays over 3 seconds"*.
This experiment measures what that sensitivity looks like behaviorally.

## Design

| | |
|---|---|
| **Independent variable** | retrieval latency: stream-time seconds between the retrieval **request** and the moment the reference becomes available to the model |
| **Conditions** | `0, 0.5, 1, 2, 3, 5, 8` s (rounded to 80 ms frames: effective `0, 0.48, 1.04, 2.00, 3.04, 5.04, 8.00` s) |
| **Controlled** | same input WAV, same fixed reference text (and the same pre-computed reference embedding), same model weights, same decoding parameters (from the checkpoint's `lm_gen_config`), same seed: the RNG is re-seeded before every run |
| **Not controlled** | *whether* and *when* the model emits its retrieval token `[RET]`, because that is model behavior. Since this happens before any reference arrives, it should match across delays for a given sample and seed (see "prefix consistency") |

Pipeline per run:

```
user WAV -> MoshiRAG (offline, batch 1)
         -> model emits [RET] at step t
         -> STT wait (0.5 s = 6 steps, unchanged from the repo)    request_step = t + 6
         -> FixedReferenceBackend returns the SAME reference
         -> reference injected at request_step + round(delay * 12.5)
         -> model continues; run stops after 3.2 s of post-injection silence
            (or 30 s after the input ends)
```

### Where the latency is injected and why

In the repo's offline harness (`moshi/moshi/inference_utils/inference_job.py`), a pending retrieval
**pauses the model** (`_output_loop`, "Do not forward model until the retrieval is complete"). The measured
wall-clock retrieval time is then converted into a step offset (`floor(elapsed * frame_rate)`) after which the
reference is injected. So in offline mode, retrieval latency already exists only on the model's stream clock.

`scripts/latency_job.py` subclasses `InferenceJob` and sets that step offset directly, as
`round(delay * 12.5)`, instead of measuring a `sleep()`. This is what `sleep(N)` would emulate,
but deterministic: there is no 50 ms polling jitter and no dependence on GPU speed or event-loop timing.
No file under `moshi/` is modified. The feed loop, STT loop, batched GPU step loop, model, tokenizer and
weights are the repo's own.

The differences from the parent `_output_loop` are listed at the top of `scripts/latency_job.py`. The two that matter scientifically:
- The tail-silence stop is **not** applied while a retrieval is pending, and silence is counted from the
  injection. Otherwise, at 5–8 s delays, a silent model would end the run before the reference arrives
  and post-RAG behavior could not be observed. The long silence is still recorded.
- No LLM is called. `LLMReferenceGenerator` is replaced by a stub at runtime, so `LLM_BASE_URL` is not
  needed. The mock backend is `mock_retrieval/fixed_reference.py`.

The live server (`moshi.server` / `inference_utils/channel.py`) is truly wall-clock asynchronous: the model
keeps generating while the LLM runs. The offline emulation gives the model the same input it would see
there (it keeps generating for N seconds of stream time, then the reference arrives). It does not
reproduce real-time GPU load or jitter.

### What is measured and how precisely

All `*_time` fields are seconds on the **stream clock** (`step / 12.5`, step 0 = first input frame).
This is the time axis of the saved audio. Wall-clock time is not meaningful offline because inference runs
faster than real time.

| field | precision |
|---|---|
| `retrieval_request_time`, `retrieval_complete_time` | exact by construction |
| `retrieval_trigger_time` (`[RET]` text token) | exact to the frame (80 ms) |
| `reference_injection_time` | exact step of `update_streaming_sum_tensors`; takes effect on the next LM step(s) (≤ ~2 frames). The reference is consumed over `injection_num_steps` frames (`reference_ingestion_end_time`) |
| `user_end_time` | **approximate**: last input frame above `--speech-db` (energy); falls back to the end of the WAV |
| `assistant_first_audio_time`, `response_end_time`, silences | **approximate**: model audio RMS above `--audible-db` |
| `assistant_first_text_time` | exact to the frame (inner-monologue text is roughly, not exactly, aligned with audio) |
| `first_informative_content_time` | **heuristic**: first time the transcript contains a gold `answer` string. Needs `answer` in the manifest |
| `pre_rag_transcript` / `post_rag_transcript` | text tokens in `[trigger, injection)` / `[injection, end)` |
| premature *wrong* answer, contradiction, naturalness | **not computed**: transcripts and audio are saved for human or LLM-judge annotation |

## Files

```
configs/samples.example.jsonl   manifest format (one JSON object per line)
mock_retrieval/fixed_reference.py   deterministic backend (stdlib only)
scripts/run_latency_sweep.py    runner: --dry-run, model loaded once, sequential sweep
scripts/latency_job.py          GPU-side InferenceJob subclass (never imported by --dry-run)
scripts/make_manifest.py        builds a manifest from a moshi.run_inference-style folder (wav + sidecar json)
analysis/metrics.py             per-run metrics (stdlib; re-runnable with other thresholds)
analysis/analyze_latency.py     per-delay summary + prefix-consistency check (stdlib)
slurm/run_latency_sweep.slurm   1x A100 job: encoder service + sweep + summary, then exits
```

## Inputs

Create `configs/samples.jsonl` (the `configs/audio/` folder is gitignored):

```json
{"sample_id": "tallest_waterfall", "wav": "audio/tallest_waterfall.wav", "question": "What is the name of the tallest waterfall in the world?", "reference_text": "Angel Falls in Venezuela is ...", "answer": ["Angel Falls"]}
```

- `wav` is relative to the manifest (or absolute). It holds the spoken question; trailing silence is fine (after the WAV ends, silence keeps being fed).
- `reference_text` is the fixed "retrieved" reference, so it should be correct and concise.
- `answer` (string or list of aliases) is optional and enables the informative-content heuristic.
- Existing datasets in the `moshi.run_inference` format: `python experiments/async_retrieval_latency/scripts/make_manifest.py DIR configs/samples.jsonl`.

## Environment (one-time; not done yet)

The login node has no torch / moshi environment. The repo uses `asyncio.TaskGroup`, so it needs
**Python ≥ 3.11** (3.12 recommended). For example:

```bash
module load anaconda3/2024.10
conda create -n moshirag python=3.12 -y
conda activate moshirag
pip install -e moshi/ fastapi uvicorn httpx
```

Weights (~16 GB MoshiRAG, plus the STT model and ARC encoder) download from Hugging Face on first
use. Point `HF_HOME` at a location with enough quota (e.g. under `/projects`) before the first job.

## Dry run (login node safe)

```bash
python experiments/async_retrieval_latency/scripts/run_latency_sweep.py \
    --manifest experiments/async_retrieval_latency/configs/samples.jsonl --dry-run
```

This checks the manifest, the WAVs, the delay→step table, the mock backend, the metrics code, output
writability and installed modules, then prints the configuration. It never imports torch (asserted).
It works with the system `python3`; missing modules are only warnings unless `--require-env` is passed
(the Slurm preflight passes it).

## Submitting

From the **repository root** (`--output` in the script is relative to it):

```bash
# 1) smallest test: 1 sample x 1 delay
DELAYS="3" MAX_SAMPLES=1 sbatch experiments/async_retrieval_latency/slurm/run_latency_sweep.slurm
# 2) 1 sample x 7 delays
MAX_SAMPLES=1 sbatch experiments/async_retrieval_latency/slurm/run_latency_sweep.slurm
# 3) full manifest x 7 delays (add SEEDS="1 2 3" for repeated sampling)
sbatch experiments/async_retrieval_latency/slurm/run_latency_sweep.slurm
```

Other overrides: `CONDA_ENV`, `VENV_PATH`, `MANIFEST`, `SEEDS`, `SAMPLE_IDS`, `EXTRA_ARGS`.

The job requests 1 node, 1 A100 (`--gres=gpu:A100:1`, because `IllinoisComputes-GPU` also has H200 nodes),
8 CPUs, 64 GB RAM and 2 h. It runs a preflight dry run, starts the reference-encoder service on
`127.0.0.1:<20000 + jobid % 20000>`, waits for `/health` (bounded), runs the sweep under `timeout`,
stops the encoder, prints a summary and exits.

## Outputs

```
results/<YYYYmmdd_HHMMSS>_job<ID>/
  config.json        args, samples, delay table, git commit/branch/dirty files, command, hostname,
                     Slurm env, nvidia-smi, Python/torch/package versions, sampling params
  results.jsonl      one line per run (appended + fsynced as each run finishes)
  run_status.json    finished | aborted | interrupted, with per-status counts
  traces/<run>.json  full per-step trace: model/user text tokens, model & user RMS, retrieval events
  audio/<run>_model.wav    model output aligned to the stream clock
  audio/<run>_stereo.wav   left = user input, right = model (for listening)
  logs/runner.log, logs/conditioner.log
  analysis/          written by analyze_latency.py
slurm/logs/moshirag-latency-<jobid>.out   job stdout/stderr
```

`<run>` = `<sample_id>__d<delay>s__s<seed>`, e.g. `tallest_waterfall__d0p5s__s42424242`.

Re-analyze later with different thresholds (CPU only):

```bash
python experiments/async_retrieval_latency/analysis/analyze_latency.py RESULTS_DIR --recompute --audible-db -40
```

**Prefix consistency** (`analysis/prefix_consistency.json`): for each sample and seed, it checks
whether the model's tokens before the earliest injection are identical across delays. If they are, the
conditions differ only after the reference arrives. If not, GPU nondeterminism or RNG interleaving with
the STT model adds noise, and multiple seeds are needed.

## Monitoring and cancelling

```bash
squeue -u $USER                                   # PD = pending, R = running; gone = finished
tail -f experiments/async_retrieval_latency/slurm/logs/moshirag-latency-<JOBID>.out   # (in your own terminal)
wc -l experiments/async_retrieval_latency/results/<RUN>/results.jsonl             # runs completed so far
cat experiments/async_retrieval_latency/results/<RUN>/run_status.json             # exists once the sweep ended
sacct -j <JOBID> --format=JobID,State,Elapsed,ExitCode
scancel <JOBID>
```

## Failure handling

- **Per-run timeout** (`--sample-timeout`, default 300 s wall): the run is cancelled through asyncio, its
  partial trace and audio are saved with `status: timeout`, and the sweep continues.
- **Errors** in a run are recorded with a traceback (`status: error`). After 3 failed runs in a row
  (`--max-consecutive-failures`), the sweep aborts instead of burning GPU time.
- **Bounded runs**: each run is capped at `--max-response-seconds` (30 s) of stream time after the input.
- **scancel / time limit**: Slurm sends `TERM` 120 s before the limit (`--signal=B:TERM@120`), and the runner
  itself is wrapped in `timeout`. The Python runner cancels cleanly (the in-flight run is saved as
  `interrupted`), and the bash `EXIT` trap stops every child process (TERM, wait up to 30 s, then KILL).

## Limitations / confounds

- Offline emulation: model-time latency is exact, but real-time effects (GPU load, network jitter,
  audio buffering) are absent.
- `[RET]` timing is the model's decision and may vary across samples. Some samples may never trigger
  retrieval; for those, the delay has no effect (`rag_triggered: false`).
- With a fixed **correct** reference, the experiment isolates latency, not retrieval quality.
- Energy thresholds and the filler lexicon are heuristics. Validate them by listening to `*_stereo.wav`.
- Sampling is stochastic (`use_sampling`, temperatures from the checkpoint). Use several seeds before drawing conclusions.
- Synthetic or TTS questions may differ from real user speech. Note the voice and source per sample.
