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
| `turntaking/policies.py` | `EvidenceAware` (ours), `WaitAll`, `FixedProgress`, `TimeOnly`, `FirstEvidence` |
| `turntaking/generate.py` | Writes what the agent says; guards that replace a sentence that drops a value or adds facts |
| `turntaking/cascade.py` | Speech ends of the cascade: `Heard` (ASR result), `Speech`, `RateTTS`, `PiperTTS` |
| `turntaking/replay.py` | Simulated clock, evidence visibility, `policy_log` records |
| `turntaking/preview.py` | Self-check TTFR/TTFGI/TTCA, unsupported claims, asked answer correct; B's evaluator is authoritative |
| `turntaking/llm.py` | Chat client that times every call and keeps a tape of calls for offline replay |
| `run_replay.py` | All policies over a trace file; writes `summary.md`, `policy_log.jsonl`, `trace_metrics.jsonl`, `llm_calls.jsonl` |
| `eval_with_b.py` | Scores a run with B's evaluator (unpacked from B's branch) next to the self-check |
| `make_question_audio.py`, `run_asr.py` | Speak the questions with Piper; transcribe them with Whisper |
| `eval_judge.py`, `eval_sft.py`, `train_lora_judge.py` | Judge evaluation on traces, on B's SFT dev set, and LoRA training |
| `slurm/` | Model serving, LoRA training, and cascade smoke submission scripts; check maintenance and resource eligibility before each submission |
| `unit_schema.md`, `judge_notes.md`, `lora_judge.md`, `cascade.md`, `evaluation_notes.md` | Rules, speech setup, and development/evaluation notes (Chinese) |

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
- The cascade: add `PYTHON=$TTS_ENV/bin/python` and `--tts piper:VOICE.onnx --save-audio`; for ASR also
  `PRE_CMD="$VLLM_ENV/bin/python $S/run_asr.py --audio $I/question_audio --out OUT/asr.jsonl"` and
  `--asr OUT/asr.jsonl`. See `cascade.md`.

The A100 command above is a development example. Formal results require H100 under
`docs/experiment_spec.md`. Latency is only comparable between runs on the same GPU type.

Before each submission, check `scontrol show reservation -o`, `sinfo -R`, the candidate nodes,
account access, and the requested wall time. Select unaffected resources with the required GPU type;
`UP` does not mean idle, and `Priority` is not a maintenance reason. The H100 evaluation default is
`secondary`; recheck availability each time. Validate with `sbatch --test-only` when useful.
Do not automatically move to a different GPU type, MIG slice, or preemptible partition.
See `../CLAUDE.md` for the submission rule and `../docs/plan.md` for the dated cluster check.


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
