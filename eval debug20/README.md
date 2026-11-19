# Debug20: CascadeSystem with B evidence and scoring

Replay B Group's 20 debug questions through the existing `cascadesystem`, using
Tinker `openai/gpt-oss-120b` and B's unchanged scoring code. There is no live
Wikipedia search, ASR, or conversation history. Local Windows TTS and playback
are optional; they do not enable formal speech-claim timing scores.

## Workflow

```text
traces_debug.jsonl -> scheduler retains future evidence
                         |
question -> model decomposition -> only due evidence -> evidence judgment
                         |
              partial/final answer -> B-format policy log
                         |
gold_debug.jsonl -> B original scorer -> scores and mapping review queue
```

The model creates its own answer units from the question. It never receives gold
answers, gold units, support sets, or future evidence. Evidence keeps B's sentence
IDs and document titles. The scheduler waits for the original arrival times and
delivers all batches already due when the controller requests more evidence.
Model calls use an immutable ingested snapshot, including during repairs.

The cascade now verifies selected partial/final output units with their visible
dependency context. After evidence is exhausted it can make one additional judge
call for necessary unresolved units. This review can change the answer and add
latency; its input is still gold-free. Verification and semantic-review events
are saved in the original logs. Previous run directories keep their original
results. Start a fresh run to compare changed code; `--resume` rejects a changed
source hash. B scoring and its mapping-review requirements remain unchanged.

Tinker also reviews its question-only plan once before evidence processing.
Its final semantic review can repair a rejected quote contract once on the same
visible snapshot, without changing supported values or promoting unresolved
facts. The extra checks can add API latency; use a fresh run to assess them.

A trained GPT-OSS judge can be selected through the
[LoRA training guide](../cascadesystem/training/README.md). Its `--debug20`
wrapper keeps this replay/scorer and changes only judgment/repair API calls.
Public run settings record the judge checkpoint and reasoning effort. Use a new
output directory when switching models. SFT dev metrics in that guide measure
snapshot judgments separately from these debug runs.

## Run from the repository root

The standard library is sufficient. The existing API configuration is read from
`cascadesystem/.env`. No additional key file or package installation is needed.

On a fresh checkout, prepare the debug inputs once:

```powershell
python ".\eval debug20\run.py" prepare --ref origin/b-data-eval
```

Preparation freezes the resolved Git commit and exports only these debug files:

- `b_work/step3/traces_debug.jsonl`
- `b_work/step3/gold_debug.jsonl`

It also reads four original evaluator source files from `b_work/eval/` at the
same commit. These are cached without modifications under `artifacts/evaluators/`.
No branch switch, reserved/test data, or network access is needed for preparation.
Existing input directories are retained; skip preparation when already prepared.

Run the 20 questions under B's existing short-delay condition:

```powershell
python ".\eval debug20\run.py" run --schedule short
```

This is the default: 20 separate question runs. The existing B conditions are:

| Schedule | First batch | Second batch |
|---|---:|---:|
| `immediate` | All evidence at 0 seconds | None |
| `short` | 1 second | 3 seconds |
| `long` | 2 seconds | 8 seconds |

These are earliest evidence availability times, not promised speaking times.
Select a different condition without changing its times:

```powershell
python ".\eval debug20\run.py" run --schedule immediate
python ".\eval debug20\run.py" run --schedule long
python ".\eval debug20\run.py" run --schedule all
```

`all` runs the same 20 questions under all three
conditions: 60 runs, not 60 different questions. Actual API calls, processing,
and evidence waits contribute to elapsed wall time. Each model/controller run
has a 180-second timeout; use `--timeout SECONDS` to change it. Finishing its
audio queue afterward can extend total wall time beyond that limit.

### Generate audio directly

Run the first question under the long condition, synthesizing and playing each
sentence as the controller produces it:

```powershell
python ".\eval debug20\run.py" run --schedule long --limit 1 --tts windows --play
```

Synthesis and playback run alongside model processing and evidence arrival.
The next question starts after the current question's audio queue finishes.
Opening, progress, partial answers, final answers, and corrections are spoken in
output order. This is audio from the new run, not a later rewrite of saved text.

To generate audio for all 60 condition runs without automatically playing them:

```powershell
python ".\eval debug20\run.py" run --schedule all --tts windows
```

Each trace saves `samples/0001/audio/response.wav`, a combined playable recording,
plus individual WAV segments and `responses.txt`. The WAV retains measured
playback gaps with `--play`; without playback it is a preview arranged at
synthesis-ready times. `audio_summary.json` lists the audio paths for the batch.
The terminal shows plain sentences and file paths, not model-response JSON.
JSON logs remain on disk for reproducibility and B scoring.

The transcript and combined WAV contain all spoken actions, including waiting
responses, partial answers, corrections, and the final action. A `Final Answer`
may contain only the last part of a multi-part answer. It is not automatically
a standalone summary of everything said. Earlier manually exported files named
`final_answers.md` or `full_responses.md` are not generated by every new run;
use the current run's transcript and ordered utterance events.

`--limit N` selects N unique questions. With `--schedule all --limit 1`, the
first question runs in three conditions; with `--schedule long --limit 1`, it
runs once. `--play` requires `--tts windows`. Use normal Windows PowerShell with
an installed voice for the question's language. No new TTS package is required.
Audio failure stops the remaining questions and reports an error instead of
silently returning only JSON. Synthesized segments and model results are kept.

By default, every invocation creates a new timestamped output directory under
`artifacts/runs/`. Use `--output PATH` to choose a new directory. `--resume`
requires an existing `--output PATH` with identical code, selected traces, and
settings; existing completed results and failures are retained.
Audio mode/playback settings must also match when resuming. Different optional
audio configurations are recorded in each new run's manifest.

## B scoring rules and limits

The code invokes B's actual `evaluate_corpus()` and `summarize()` functions. It
does not replace them with embeddings, an LLM grader, or a custom value scorer.
B checks normalized expected answers/aliases, cited support sets, dependencies,
and evidence visibility. Missing measurements remain null.

Controller unit IDs are independent from gold IDs. The default scorer does not
assume that `u1` means the same fact in both. Unmapped claims enter
`b_eval/review_queue.jsonl`; affected scores stay null until mappings are checked.
A `complete` controller status does not mean the answer is correct.

`complete` and `incomplete` describe whether the controller fulfilled its own
necessary answer units. B's separate `ok`/`error` status describes whether the
record can be evaluated, not whether its answer is right. For example, B cannot
score the current correction/retraction behavior and marks those records as
adapter errors even when the controller finished.

Rescore checked claim-to-gold mappings without API calls:

```powershell
python ".\eval debug20\run.py" score --run "RUN_DIRECTORY" --reviews "CHECKED_REVIEWS.jsonl" --output "RUN_DIRECTORY\b_eval_reviewed"
```

Review rows use B's `run_id`, zero-based `record_index`, `claim_index`, and
`gold_unit_id`, plus `source_log_sha256` for the unchanged `policy_log.jsonl`.
Reviews do not change predicted values, citations, or evidence.

B also supports a separate approximate diagnostic that maps unique exact values:

```powershell
python ".\eval debug20\run.py" score --run "RUN_DIRECTORY" --allow-value-match --output "RUN_DIRECTORY\b_eval_value_diagnostic"
```

Approximate mappings are counted separately and do not establish relation
correctness or independent semantic review. Do not report their UCR as a fully
reviewed project result. Scores may cover only a subset of runs; their mean is
not overall accuracy. Incorrect unmatched values must not disappear from the
interpretation of results. Keep the strict report and inspect coverage/reviews.

Only declared structured facts are scored; the original reply is retained for
inspection. B's current scorer does not implement retractions. A run containing
a correction is retained and marked as an adapter error for B scoring rather
than silently counted as correct. Claim times stay null and `timing_kind=unknown`,
so TTFR/TTFGI/TTCA are not reported as speech measurements. Optional local TTS
records sentence synthesis and playback times separately; it does not align every
atomic claim or change B's simulated trace clock. `text_pipeline_wall_s` excludes
draining the audio queue, while `total_wall_s` includes it when TTS is enabled.
Internal `trace.invalid` URLs identify evidence and are never fetched.

The adapter uses an individual sentence only when its value occurs in exactly
one sentence and that sentence contains no other declared claim value. Repeated
names, shared Yes/No values, and comparison names can make sentence assignment
ambiguous. In that case it keeps the original whole utterance as context, marked
`span_basis=utterance_context_unaligned`, instead of choosing the first matching
sentence. This does not establish atomic relation alignment or semantic review;
claim speech times remain null. B still checks the original declared value,
text and citations. Historical logs are not rewritten.

The current model can still misread a relation, miss a fact expressed indirectly,
or assign the wrong time context. Evidence validation and natural wording do
not establish semantic correctness. The standalone cascade also does not infer
a negative occupation solely from its absence in a description; this can leave
gaps against B's omission-based labels. These are development limitations,
not changes to B's reference answers or scoring rules.

## Outputs

- `artifacts/inputs/b-debug-v0/traces.jsonl`: unchanged bytes from B's `traces_debug.jsonl`.
- `artifacts/inputs/b-debug-v0/gold.jsonl`: unchanged bytes from B's `gold_debug.jsonl`, scoring only.
- `artifacts/inputs/b-debug-v0/manifest.json`: source paths, frozen B commit, and input hashes.
- `artifacts/runs/RUN/manifest.json`: model configuration without keys, B commit,
  source hashes, selected traces, and code provenance.
- `samples/0001/run.json` and `events.jsonl`: original result, evidence, and model calls.
- `samples/0001/adapter_issues.json`: limitations such as unsupported retractions.
- `policy_log.jsonl`: all actions and declared claims in B's required format.
- `samples/0001/audio/response.wav`: complete synthesized speech for one trace, when enabled.
- `samples/0001/audio/responses.txt`: readable output transcript in speech order.
- `samples/0001/audio/audio_index.json`: speech segments, voice, errors, timing and combined-WAV timeline.
- `audio_summary.json`: batch audio-file paths and audio failures, when enabled.
- `b_eval/summary.md` and `summary.json`: B's report with score coverage.
- `b_eval/run_scores.jsonl`, `claim_scores.jsonl`, `review_queue.jsonl`, and
  `validation_issues.jsonl`: score details and pending mappings.

All generated data, results, and cached evaluator files are ignored by Git.

An optional offline review, created separately when requested, can live under
`artifacts/runs/<run>/answer_audit_<date>/`: `report.md` explains the findings,
`full_responses.md` preserves all utterances, and `by_question.csv` compares
conditions. Assisted mapping reports stay separate from the original `b_eval/`.
Such reviews must identify their reviewer and score coverage; core-answer
reading, controller completion, and B grounded completion are different results.

Exit 0 means no operational/adapter errors or missing runs; pending mapping
reviews can still leave scores null. Exit 1 reports errors/invalid/missing runs.
Exit 2 reports setup/input failure; 130 is cancellation. A zero exit code does
not establish correct answers.

## Files

| File | Responsibility |
|---|---|
| `run.py` | `prepare`, `run`, and `score` commands; default short condition and unique output directories. |
| `eval_common.py` | Paths, Git access, JSON IO, source hashes, and public settings. |
| `eval_data.py` | Debug-only export/loading and unchanged B evaluator loading at one frozen commit. |
| `eval_replay.py` | Future-private evidence scheduling, existing Cascade execution, B log conversion, and retained failures. |
| `eval_audio.py` | Concurrent local TTS/playback, readable transcripts, per-trace combined WAVs, and retained audio errors. |
| `eval_score.py` | Original B scorer invocation, checked/explicitly approximate mappings, and report export. |
| `tests/test_debug20.py` | Fictional offline tests for isolation, arrival times, mappings, support, errors, and source integrity. |
| `tests/test_audio.py` | Offline synthetic-WAV tests for incremental speech, playback draining, cancellation, failures and question limits. |
| `tests/test_claim_context.py` | Fictional checks for shared values, comparison conclusions, conservative utterance context and unknown speech times. |
| `.gitignore` | Excludes generated inputs, results, cached code, and bytecode. |

Offline tests, without Tinker calls or benchmark-question access:

```powershell
python -m unittest discover -s ".\eval debug20\tests" -v
```
