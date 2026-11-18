# A Group: Evidence-Aware Turn-Taking Controller

Trace replay for the evidence-aware policy and four rule baselines, with a real judge, real sentences and,
optionally, real speech timing. The core (`turntaking/`, `run_replay.py`) needs Python 3.9+ and the standard
library only; models are reached over an OpenAI-compatible endpoint (vLLM).

```bash
python3 -m unittest discover -s a_work/tests    # all tests run on fake models, no GPU
python3 a_work/run_demo.py                      # two hand-made traces with placeholder sentences
```

## Layout

| File | Role |
|---|---|
| `turntaking/schema.py` | Action and label names from B's interface v1; observation and decision types |
| `turntaking/decompose.py` | Splits a question into answer units (sees the question only) |
| `turntaking/judge.py` | `OracleJudge` (gold support sets), `PromptJudge` (few-shot LLM, or a LoRA adapter without examples), dependency resolution, sufficiency state |
| `turntaking/premise.py` | Conservative checks for the candidate-selection evidence and an explicit uniqueness premise |
| `turntaking/policies.py` | `EvidenceAware` (ours), `WaitAll`, `FixedProgress`, `TimeOnly`, `FirstEvidence` |
| `turntaking/generate.py` | Writes what the agent says; guards that replace a sentence that drops a value or adds facts |
| `turntaking/cascade.py` | Speech ends of the cascade: `Heard` (ASR result), `Speech`, `RateTTS`, `PiperTTS` |
| `turntaking/replay.py` | Simulated clock, evidence visibility, `policy_log` records |
| `turntaking/preview.py` | Self-check TTFR/TTFGI/TTCA, unsupported claims, asked answer correct; B's evaluator is authoritative |
| `turntaking/llm.py` | Chat client that times every call and keeps a tape of calls for offline replay |
| `run_replay.py` | All policies over a trace file; writes `summary.md`, `policy_log.jsonl`, `trace_metrics.jsonl`, `llm_calls.jsonl` |
| `main_experiments.py` | Prepare and verify pinned public/private inputs, code, checkpoint and evaluator; print/test a Slurm command; collect B scores and paired latency |
| `run_main_experiments.py` | Run a main-experiment shard with question-only ordinary policies, a separate Oracle process, per-question checkpoints and timeout accounting |
| `slurm/main_experiments.slurm` | H100 array on authorized `dilek-ic`, normal QoS, nice 0; higher-tier scavenger with secondary fallback |
| `eval_main_smoke.py`, `slurm/validate_main_smoke.slurm` | CPU-only execution/log gate between the debug GPU smoke and the main array; checks all expected runs with the pinned B evaluator |
| `tests/test_main_experiments.py` | Fictional tests for input isolation, cross-schedule consistency, snapshot integrity and failure retention |
| `tests/test_main_smoke_gate.py` | Fictional tests that missing, duplicate or failed smoke work cannot pass the gate |
| `eval_with_b.py` | Scores a run with B's evaluator (unpacked from B's branch) next to the self-check |
| `make_question_audio.py`, `run_asr.py` | Speak the questions with Piper; transcribe them with Whisper |
| `eval_judge.py`, `eval_sft.py`, `train_lora_judge.py` | Judge evaluation on traces, on B's SFT dev set, and LoRA training |
| `eval_premise_paths.py` | Compare candidate validation on identical saved or live judge outputs using debug traces and fictional controls |
| `slurm/` | `eval_judge.slurm` serves the models and runs a script; `train_lora.slurm` |
| `unit_schema.md`, `judge_notes.md`, `lora_judge.md`, `cascade.md`, `evaluation_notes.md` | Rules, speech setup, and development/evaluation notes; `evaluation_notes.md` includes the 2026-11-18 main result analysis, coverage, mapping bias, bounded claim errors and paired latency (Chinese) |

## Data flow

```
question audio ─► ASR ─► question text ─► decompose ─► units
trace.jsonl ─► replay (only evidence with visible_time_s <= t) ─► policy.decide(obs)
                                              EvidenceAware: judge → dependencies → sufficiency state → action
                                              action ─► generator (LLM) ─► TTS ─► policy_log.jsonl ─► B eval
gold.jsonl ─► OracleJudge and self-check metrics only
```

Without `--asr` the question text comes from the trace; without `--tts piper:...` speech is timed at a fixed
2.5 words per second.

## Running a replay

Submit from the repository root. `I` is the input folder, `A` the LoRA adapter, `S` a code snapshot (a queued
job reads the code when it starts, so copy `run_replay.py`, `run_asr.py` and `turntaking/` somewhere stable).

```bash
BASE="--trace $I/traces_debug.jsonl --gold $I/gold_debug.jsonl --generate --concurrent"
LORA="--judge-model judge --judge-name lora --no-examples"
export RESULT_GROUP=replay SCRIPT=$S/run_replay.py
# LoRA judge on a second server; decomposition and the baselines' answers stay on Qwen3-14B
RUN_NAME=my_run GPU_UTIL=0.55 JUDGE_GPU_UTIL=0.30 JUDGE_BASE=Qwen/Qwen3-4B \
  JUDGE_VLLM_ARGS="--enable-lora --lora-modules judge=$A" EVAL_ARGS="$BASE $LORA" \
  sbatch --constraint="AE7763_100g_512G_A100|A100" a_work/slurm/eval_judge.slurm
```

- `--concurrent` adds a `+concurrent` copy of each evidence-aware policy that judges and generates while
  the agent speaks.
- `--grounded-model Qwen/Qwen3-4B` lets the judge's base model phrase the evidence-aware sentences.
- `--strict-candidate-paths` checks binary candidate decisions and records selected dependencies and citations in `judge_calls.jsonl`.
- The cascade: add `PYTHON=$TTS_ENV/bin/python` and `--tts piper:VOICE.onnx --save-audio`; for ASR also
  `PRE_CMD="$VLLM_ENV/bin/python $S/run_asr.py --audio $I/question_audio --out OUT/asr.jsonl"` and
  `--asr OUT/asr.jsonl`. See `cascade.md`.

The A100 command above is a development example. Formal results require H100 under
`docs/experiment_spec.md`. Latency is only comparable between runs on the same GPU type.

## Replaying a finished run without a GPU

Every run writes `llm_calls.jsonl`. Timing settings can then be changed and replayed anywhere:

```bash
python3 a_work/run_replay.py --trace ... --gold ... --generate --concurrent \
    --judge-model judge --judge-name lora --no-examples \
    --tape a_work/results/replay/my_run/llm_calls.jsonl --tts rate --out a_work/results/replay/my_run_again
```

The model names and prompts must match the recorded run. A request the tape lacks stops the replay;
`--allow-tape-misses` turns it into an unusable reply and reports the count.

## Scoring with B's evaluator

```bash
python3 a_work/eval_with_b.py a_work/results/replay/my_run     # writes my_run/b_eval/both.md
```

Pass `--reviews FILE --out OTHER_DIR` for a separate evaluation with reviewed mappings. The original
`b_eval/` is protected when reviews are supplied. See `evaluation_notes.md` for the v5 assisted review;
these mappings were reviewed by Codex and do not constitute independent human annotation.

## Not done yet

- The ASR/Piper smoke job is still pending as of 2026-11-11; the implementation is not yet GPU-validated.
- The two v7 text replay jobs completed on A100, but still need B evaluator scoring. See `lora_judge.md`.

- The formal three-judge comparison waits for B's judge validation set; the 300 reserved traces are run once at the end.
- The cascade uses synthetic question audio (Piper) until C's recordings are shared, and Whisper is not streaming.
- Models that share a GPU may slow each other when they run concurrently; the replay does not simulate that.
- Only non-Wait actions are logged.

## Main experiments on the revised 900 traces

Work branch: `a-main-experiments`, based on `origin/a-method-integration` at
`bc412d5911d79c7bb39a615b41cb8d2597738291`. The evaluation-refinement branch is separate.
The 2026-11-16 preparation and checks below supersede older status entries only for this new runner;
the historical replay and speech results above remain historical.

The designated B data are 300 revised questions, each with immediate/short/long arrivals, not 900
independent questions. Use both revised gold files named in B's trace manifest; original batch gold is
incompatible. These are controlled mock retrieval times, text input and estimated speech duration.
This data set has no multipart questions. Parameter selection stays on debug/dev.

The prepared matrix has four rule baselines; Prompt and LoRA question-only controllers, each serial and
concurrent; and two Oracle upper-bound configurations. That is 10 configurations and 9,000 expected
policy runs. Existing prompts, thresholds, generation guards and replay timing are unchanged. Historical
gold-description judge diagnostics are excluded from the ordinary main method. Oracle gets a separate
gold input in a separate worker; ordinary workers get only the public question/evidence file. The
parent scheduler retains future events, while policies and models receive visible snapshots only.

From the repository root:

```bash
# Prepared locally; use a NEW name to make another immutable bundle.
python3 a_work/main_experiments.py prepare --name main_eval_revised_v1_20261116_v3 \
  --ref ea390574eadd301354d5de46f0d28d328cca5bad

B=a_work/results/code_snapshots/main_eval_revised_v1_20261116_v3
python3 a_work/main_experiments.py verify --bundle "$B"
python3 a_work/main_experiments.py command --bundle "$B" --test-only
# Without --test-only, command prints the sbatch invocation; it does not submit it.
python3 a_work/main_experiments.py command --bundle "$B"

# After the run, collect once into a NEW analysis directory. Missing/failed work is retained.
python3 a_work/main_experiments.py collect --bundle "$B" \
  --out a_work/results/analysis/main_eval_revised_v1_20261116_v3
```

Inputs are under `results/inputs/<name>/public/` and `private/`; frozen runner, evaluator and adapter are
under `results/code_snapshots/<name>/`; GPU outputs go under `results/replay/<name>/shard_NNN/`.
The manifest records full commits, source paths and SHA256 for all inputs, code and adapter files.
A pending job reads these frozen files, and detects edits before starting a server.

The default is 30 shards with 10 questions each, three schedules kept together, at most two array tasks
running at once. Each task reserves one full H100 80GB for up to four hours. Qwen3-14B generates and
serves the Prompt judge; Qwen3-4B serves the existing LoRA adapter on the same allocated GPU.
GPU memory fractions remain the earlier development settings 0.55/0.30; startup is not GPU-validated
by CPU tests. Co-resident-server costs and simulated concurrency remain limitations.

`scavenger` currently has PriorityTier 3 and full H100 nodes; `secondary` has tier 1 and is the fallback.
`IllinoisComputes-GPU` currently supplies A100/H200, so it cannot satisfy the H100 constraint.
Use authorized normal QoS and nice 0. FairShare currently has zero weight, and neither account selection
nor a successful `--test-only` guarantees a start time. No negative nice or unauthorized QoS is used.

Each ordinary/Oracle question worker has a 1,800-second watchdog. Results and tapes are saved after
each policy; errors and timeouts have separate markers and logs. `--resume` preserves completed and
failed attempts; it does not silently retry failed questions. Slurm requeue is disabled to avoid hidden
repetitions. To retry, prepare a distinct named run and retain both inventories. The legacy persistent
Wait termination and failed-HTTP timing limitations remain; this runner contains them as recorded worker
failures, without changing the underlying timing definition.

`collect` uses the frozen B evaluator and all ten expected policies on every trace, so missing output
does not disappear. Only Oracle is declared gold-aligned. Structured claims still need independent
mapping/semantic review; overall UCR may be null. Paired latency reports positive values for earlier
output, sample counts and missing coverage. No confidence interval method is silently selected.

The data manifest still says `controlled_mock_ready_for_review`, with gold approval and final delay
freeze unrecorded. Preparation is not a declaration of final approval, a GPU run or a result.
See `docs/plan.md` for the actual checks and pending work.

On 2026-11-16 the user authorized the main submission. Smoke job `12490825`, CPU validation job
`12490921` and main array `12490887` are submitted. Dependencies are smoke → successful validation →
main, so no manual release is needed after a passing gate. Failure keeps the main array blocked.
The gate checks execution completeness and B log validity; it does not require high semantic scores.
The submitted main array raises concurrency from the preparation default of two to four H100 GPUs;
all 30 shards retain the same frozen code and inputs. See the plan for current queue state.

As checked on 2026-11-18, all 30 main tasks finished on November 16 at 19:51:40 CST, with 600 completed
workers and 9,000 completed policy runs. Actual peak parallelism was one H100 task. The fixed B scorer
returned exit 0 with no invalid log rows, while 1,427 claim records still need review. Full results are in
`results/analysis/main_eval_revised_v1_20261118/`; `analyze.py` reproduces aggregate tables and hashes.
See [the main analysis](evaluation_notes.md#主实验结果分析2026-11-18). High conditional Unit EM is affected
by value-based mapping and does not establish whole-answer accuracy. Long-delay first information is
earlier on measurable pairs, while short-delay and complete-answer speed do not show a general win.
No main prompts, labels, values, aliases or thresholds were changed after these results.
