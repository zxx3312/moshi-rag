# GPT-OSS-120B + judge LoRA on the revised final 900 traces

This independent entry uses the existing Cascade on **300 questions × three
arrival schedules = 900 traces**. It runs one GPT+LoRA configuration, not all the
strategies in A's comparison table. Planner, plan review, answer generation,
verification and feedback use `openai/gpt-oss-120b`. Only judgment/repair calls
(including completion review) use the checkpoint selected by
`cascadesystem/artifacts/training/runs/gpt120-judge-v1/best.json`.

It reuses the current `.env` and needs no additional dependencies or local model.
It does not rewrite `.env`, change existing prompts or modify the Debug20 entry.
Prediction calls the actual API; the implementation tests do not.

## Explicit final-run acknowledgment

The revised 900 traces are reserved evaluation data. `CLAUDE.md` permits F1 after
the user explicitly declares the final run. **Execute the following commands only
when declaring this the final evaluation of the frozen current configuration.**
`--final-run` is the explicit acknowledgment for this entry. Without it, prepare,
prediction and scoring reject before input/credential/checkpoint access or writes.
Use Debug20/SFT dev for development, model selection and parameter changes.

No reserved questions, gold or traces were read while implementing this entry.
The code was verified with fictional data only; actual final data and model/API
performance remain untested. Failed final attempts must be retained.

## PowerShell commands

```powershell
cd D:\UIUC\CS546\moshi-rag

# Once only: export the fixed revised inputs, without model calls.
python ".\eval gpt900\run.py" prepare --final-run

# Run all 900 traces using GPT+LoRA and save Windows speech.
python ".\eval gpt900\run.py" run --final-run --tts windows --allow-value-match --output "eval gpt900/artifacts/runs/gpt120-lora-v1"
```

`--allow-value-match` enables B's existing **approximate unique-value mapping
diagnostic**, also used by A's main collector. It helps produce a scorable-subset
table without equating model unit IDs with gold unit IDs. This is not embedding
matching or independent human review. Some claims/scores can remain unknown.
Omit the flag for strict checked-mapping-only scoring. This changes scoring only;
gold and mappings never enter model input. Disclose the scoring mode in comparisons.

Omit `--tts windows` for text-only evaluation; add `--play` to hear each utterance.
Windows speech requires native Windows. Real API requests use your existing account.

If inputs already exist, skip `prepare`. Output directories are never overwritten
as a new run. Resume with the same options:

```powershell
python ".\eval gpt900\run.py" run --final-run --tts windows --allow-value-match --output "eval gpt900/artifacts/runs/gpt120-lora-v1" --resume
```

Resume preserves every saved attempt, including errors/timeouts/cancellations; it
does not silently retry them. Input hashes, source, selected checkpoint, timeout
and audio settings must match. Continuing training can change `best.json`, which
will cause a different checkpoint to be refused on resume. Freeze training/code
before running. Ctrl+C normally saves the current attempt; abruptly killing the
process can leave an unfinished sample directory. Preserve failed artifacts.

### Continue an older run after the audio-stop fix

An audio synthesis error is separate from text-answer completion. By default a
new audio failure stops further inference. `--continue-on-audio-error` retains
that failure and continues text evaluation; API authentication errors still stop.
Audio failures remain in the sample and `audio_summary.json`, and can still make
the final process exit nonzero after all traces have been attempted.

The earlier runner also stopped again on a saved audio failure during `--resume`.
That behavior is fixed: saved attempts are retained and do not block unsaved ones.
Because this operational fix changes the runner source hash, an older frozen run
needs an explicit **new continuation directory**, rather than bypassing its resume
source check:

```powershell
python ".\eval gpt900\run.py" run --final-run --tts windows --allow-value-match --continue-on-audio-error --continue-from "eval gpt900/artifacts/runs/gpt120-lora-v1" --output "eval gpt900/artifacts/runs/gpt120-lora-v1-continued"
```

This verifies the same input, checkpoint, public settings and unchanged shared
model/controller/prompt/scorer code. It copies **all** saved attempts, successful
or failed, into the new directory and calls the model only for unsaved traces.
The original run, failed audio and failed model calls are not edited, retried or
removed. Copying existing audio can take time and needs additional disk space.
Parent/current source identities and inherited sample hashes are recorded in
`continuation.json`, with copies of the parent manifests. Overlapping parent/child
paths, existing child outputs and incomplete parent sample directories are refused.

To resume that new directory after another interruption, drop `--continue-from`
and retain the same audio-error policy:

```powershell
python ".\eval gpt900\run.py" run --final-run --tts windows --allow-value-match --continue-on-audio-error --output "eval gpt900/artifacts/runs/gpt120-lora-v1-continued" --resume
```

## Fixed inputs and visibility

Default B commit: `ea390574eadd301354d5de46f0d28d328cca5bad`.
The source paths come from the existing A main-experiment preparation code:

```text
b_work/test_set/traces/eval_revised_v1/traces.jsonl
b_work/test_set/revisions/batch01_05_v1/gold.jsonl
b_work/test_set/revisions/batch06_10_v1/gold.jsonl
```

Prepare exports only those named inputs and the source trace manifest, without
checking out the full B tree. It checks 300 questions, 900 traces, 817 gold units,
the fixed arrival schedules and B's original schema/support contracts. Original
batch gold cannot replace these revised gold files.

Frozen data live under `artifacts/inputs/eval-revised-v1/public/` and `private/`.
Prediction reads only the public traces and their hash manifest. The scheduler
retains future evidence; ordinary models see question/state and already delivered
evidence only. Gold is read by prepare's schema validation and the separate scorer.

The revised builder preserves blank evidence sentences. Frozen inputs and scorer
inputs retain them. Runtime skips blank sources, consistent with the existing
Cascade's empty-source rejection, while retaining all nonblank source IDs/text/times
and the original retrieval-completion time. The skipped count is recorded.

Each trace reuses `eval debug20/eval_replay.py`, the original controller, literal
quote/dependency checks, bounded repairs and optional audio. New outputs are labeled
`b_final_revised_trace`; reserved data are not relabeled as debug or passed through
the Debug20 loader. The source manifest records original shared Python/PowerShell
hashes and the new entry's Python files, and enforces that identity on resume.

## Outputs and scoring

For the commands above, results are under
`eval gpt900/artifacts/runs/gpt120-lora-v1/`:

| File | Function |
|---|---|
| `manifest.json`, `source-manifest.json` | Frozen checkpoint, public settings, input/source hashes and all 900 expected trace IDs |
| `samples/0001/run.json` | Full trace state, judgments, events and API call timings |
| `samples/0001/events.jsonl` | Controller events in order |
| `samples/0001/audio/responses.txt` | Spoken opening/progress/partial/final text, with TTS enabled |
| `samples/0001/audio/response.wav` | Combined speech, with TTS enabled |
| `policy_log.jsonl` | All predictions in the B scoring interface |
| `audio_summary.json` | Audio status for saved traces, with TTS enabled |
| `b_eval/summary.md` | Original B score table and unknown coverage |
| `b_eval/run_scores.jsonl` | Per-trace B scores |
| `b_eval/review_queue.jsonl` | Claims needing checked mappings |

Read partial and final utterances together: the final utterance may add only
previously unsaid facts. System `complete` does not itself establish B correctness.
Scoring automatically includes all 900 expected traces, retaining missing/failed
coverage. A resumed run writes a fresh `b_eval-*` report if an old report exists.
For independent re-scoring without API calls:

```powershell
python ".\eval gpt900\run.py" score --final-run --run "eval gpt900/artifacts/runs/gpt120-lora-v1" --output "eval gpt900/artifacts/scores/gpt120-lora-v1-reviewed" --reviews "PATH_TO_CHECKED_REVIEWS.jsonl"
```

Review records must bind the exact policy-log SHA256. High Unit EM on a smaller
scorable subset is not full-set whole-answer accuracy. This entry supplies one
GPT+LoRA row; it does not reproduce A's baselines, controller, omission exceptions,
vLLM serving or simulated speech clock. B timing remains `unknown` because formal
speech-claim alignment is absent. Sharing inputs alone does not make timings comparable.

## File map and offline checks

| File | Function |
|---|---|
| `run.py` | Final gate, fixed input export/validation, GPT+LoRA replay/resume and B scoring |
| `tests/test_final.py` | Fictional gating, schema, blank sources, gold isolation, 900-attempt inventory, resume and scoring tests |
| `tests/test_continuation.py` | Operational parent/child lineage, unchanged-method checks, saved-error recovery and audio/authentication separation |
| `.gitignore` | Keeps inputs, outputs and cache out of Git |

```powershell
python -m unittest discover -s "eval gpt900/tests"
```

Validation: 18 new tests, 187 original application tests and 28 original Debug20
tests passed, exit 0. All test questions/documents are fictional. Branch
`a-cascade`, parent `c23d6ae6e7250b793c026e7ec01ae9166728f5af` + dirty.

After the audio-stop recovery change, all 30 final-run tests passed, exit 0,
including the original 18 unchanged tests. No API/TTS calls or new final inference
were made to validate this fix. Only the existing failed run's operational
audio/error and provenance metadata were inspected; no answers were tuned.
