# Colab T4 results, 2026-10-06 (UTC)

Results of the controlled retrieval-latency experiment run on Google Colab (one Tesla T4) with
`t4/run_latency_sweep_t4.py`. MoshiRAG is **int8-quantized in float16** here, not the released
bf16 model. All runs use seed 42424242 and synthetic Piper TTS questions (voice `en_US-lessac-medium`).
"Delay" is the time between the retrieval request and the moment the fixed, correct reference is
injected. Injection always happens 0.48 s (STT wait) + delay after the model's `[RET]` token.

Only lightweight files are committed: metrics, per-step traces, analysis, logs and 4 example WAVs. The full audio
(model + stereo WAV for every run) and the runner logs stay on Google Drive
(`MyDrive/moshirag_t4/results/<original run name>/`).

## Runs

| Folder | Original run name | Questions | Delays (s) | Runs | Status |
|---|---|---|---|---|---|
| `run1_easy_1question_delay3s` | `step1_1x1` | 1 easy (tallest waterfall) | 3 | 1 | complete |
| `run2_easy_1question_6delays` | `step2_1xall` | 1 easy | 0, 1, 2, 3, 5, 8 | 6 | complete |
| `run3_easy_5questions_6delays` | `step3_small` | 5 easy (`t4/configs/samples_small.jsonl`) | 0, 1, 2, 3, 5, 8 | 30 | complete |
| `run4_hard_simpleqa_12questions_delays0s_8s` | `pilot_hard` | 12 hard SimpleQA (`configs/samples_hard_pilot.jsonl`) | **0 and 8 for all 12**; also 1, 2, 3 for sqa_1009 and sqa_1155, and 5 for sqa_1009 | 31 | 0 s and 8 s complete; the all-delays extension was stopped after 7 runs |

`run4/traces_interrupted/` holds the trace of the one run that was cancelled mid-way
(sqa_1155, 5 s). It has no record in `results.jsonl`, so the analysis does not use it.

## Files in each run folder

| File | What it is |
|---|---|
| `results.jsonl` | One line per completed run: timings (`retrieval_trigger_time`, `reference_injection_time`, ...), latencies, pre-RAG and post-RAG transcripts, silence and filler statistics, GPU memory, wall time |
| `config.json` | Arguments, sample list, delay table, git commit, package versions, GPU and sampling parameters |
| `run_status.json` | finished / interrupted, counts per status, runs not yet done |
| `traces/<sample>__d<delay>s__s<seed>.json` | Per-step record of one run: model and user text tokens, model audio RMS per 80 ms frame, retrieval events |
| `analysis/summary_by_delay.csv`, `summary.json` | Medians and rates per delay (printed tables below) |
| `analysis/per_run.csv` | One row per run with the main fields (spreadsheet friendly) |
| `analysis/prefix_consistency.json` | Whether the model's tokens before the earliest injection are identical across delays |
| `analysis/annotation_sheet.csv` | run4 only: transcripts with empty label columns for manual annotation |
| `logs/gpu_memory.jsonl` | GPU memory after each load stage and each run |
| `logs/sessions.jsonl` | One entry per Colab session (command, resume info, environment) |
| `audio_examples/*.wav` | run4 only: stereo WAV, **left = question, right = model**, for two questions at 0 s and 8 s |

Standard file names are kept on purpose: `analysis/analyze_latency.py`, `analysis/export_annotation_sheet.py`
and `--resume` read them. To recompute the analysis:

```bash
python experiments/async_retrieval_latency/analysis/analyze_latency.py \
    experiments/async_retrieval_latency/t4/colab_results_2026-10-06/run4_hard_simpleqa_12questions_delays0s_8s
```

## Notebooks

| File | What it is |
|---|---|
| `notebooks/session1_setup_and_easy_question_runs1-3_executed.ipynb` | Executed Colab session: environment setup, embedding precompute (including the OOM and fix), runs 1–3, with outputs |
| `notebooks/session2_hard_simpleqa_pilot_run4_executed.ipynb` | Executed Colab session: hard-question pilot (run 4), with outputs |

The clean, runnable notebook is `t4/colab_runner.ipynb`.

## Main observation (run 4, delays 0 s vs 8 s)

`prefix_consistency`: 12/12. Before the earliest injection, the model's output is token-identical across
delays, so differences come only from when the reference arrives.

Preliminary counts from reading the transcripts in `results.jsonl`. **They have not been checked by
manual annotation yet** (`analysis/annotation_sheet.csv` is still empty):

| | 0 s delay | 8 s delay |
|---|---|---|
| Correct answer given | 9/12 (the other 3: phonetically close misnames, e.g. "Carl Munck" for Carl Wunsch) | 0/12 |
| Specific wrong answer stated before the reference arrived | 0/12 | 11/12 |
| Closed the turn ("Is there anything else...") before the reference arrived | 0/12 | 6/12 |
| Corrected itself after the reference arrived | n/a | 0/12 |
| Response onset after the question (median) | 0.16 s | 0.16 s |

Example (sqa_3564, "Which U.S. president was the last one to be born in the 18th century?", gold: James Buchanan):
- 0 s: "That's a fun question! James Buchanan was the last president born in the eighteenth century."
- 8 s: "That's a good question! Adams was the last president born in the eighteenth century, born in
  seventeen thirty-five. Is there anything else?" The model stays silent after the correct reference arrives.

Even when it answers correctly at 0 s, the model sometimes adds details that are not in the reference
(e.g. Buchanan "born in seventeen eighty-five").

Limitations: one seed; int8/float16 model on a T4; synthetic questions; transcripts come from the model's
text stream (close to, but not a verbatim transcription of, its speech); intermediate delays cover only 1–2 questions.
