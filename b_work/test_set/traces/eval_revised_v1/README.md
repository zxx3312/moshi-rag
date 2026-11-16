# Revised Evaluation Traces

## Completed

- Saves 900 controlled mock traces for 300 revised questions and 817 gold units.
- Uses the original [Step3 trace builder](../../../step3/build_traces.py).
- Reads paired samples and gold from
  [Batches 1–5](../../revisions/batch01_05_v1/README.md) and
  [Batches 6–10](../../revisions/batch06_10_v1/README.md).
- Keeps all context sentences and document titles, including distractors.
- Checks 2,100 evidence snapshots and 5,719 unit judgments against A's Oracle
  and B's evaluator. Support states and first support times agree.
- Checks 3,086 supported citations. Every final answer has support by the last
  arrival. Seven optional units remain unresolved, as allowed by their gold.
- All 62 Step3 and B evaluation tests pass. The three generated output files
  rebuild exactly. Debug trace and review exports match the earlier script.

| File | Use |
|---|---|
| [traces.jsonl](traces.jsonl) | Questions, source evidence, and arrival times. |
| [review.md](review.md) | Private document batches and unit support times, Q1–Q300. |
| [validation_report.json](validation_report.json) | Builder checks and support times for each trace. |
| [integration_report.json](integration_report.json) | A/B checks, test counts, and fixed A code version. |
| [schedules.json](schedules.json) | Provisional arrival times used by the builder. |
| [manifest.json](manifest.json) | Input paths, versions, counts, and output paths. |

## Rules

- `schema_version` is `1.0`. `data_version` is `eval-revised-v1`.
- A controlled mock trace uses set arrival times. These are simulated times,
  not measured retrieval times or model results.
- Whole documents arrive together. Scheduled and visible times are equal.
- Source supporting-fact documents are split in citation order. Alternative
  normal and premise evidence arrives with its matching support document.
  Other documents alternate between batches in source order.
- Gold is used to arrange and check evidence. Gold answers, units, support sets,
  and special flags are not copied into public traces. Source evidence may state
  an answer; that source text stays intact.
- The review and reports use gold. Do not give them to an ordinary model.
  Only the separate Oracle check may read gold.
- Use both revisions' samples and gold together. Do not pair these traces with
  the original `batches/` gold or the frozen Step2 question text.
- Each question has these three provisional schedules:

| Schedule | First batch | Second batch |
|---|---|---|
| `immediate` | All documents at 0 seconds | None |
| `short` | 1 second | 3 seconds |
| `long` | 2 seconds | 8 seconds |

Run from the repository root to rebuild the traces, review, and builder report:

```bash
python3 b_work/step3/build_traces.py \
  --samples b_work/test_set/revisions/batch01_05_v1/samples.jsonl \
    b_work/test_set/revisions/batch06_10_v1/samples.jsonl \
  --gold b_work/test_set/revisions/batch01_05_v1/gold.jsonl \
    b_work/test_set/revisions/batch06_10_v1/gold.jsonl \
  --schedule-config b_work/test_set/traces/eval_revised_v1/schedules.json \
  --out b_work/test_set/traces/eval_revised_v1/traces.jsonl \
  --review b_work/test_set/traces/eval_revised_v1/review.md \
  --report b_work/test_set/traces/eval_revised_v1/validation_report.json
```

This command does not rebuild the manifest or the independent integration
report. Repeat the A/B checks and refresh those files after input, code, or delay
changes. The integration report names the fixed A commit used by these checks.

## Next steps

- Review arrival batches and support times in `review.md`.
- Agree with the team on final paired inputs and delays.
- Rebuild traces and repeat checks after accepted changes.
- Use A's runner for policy and model experiments with the agreed inputs.

## Needs review

- Final approval of both paired gold revisions.
- Final delay settings for the main experiment.
- Trace generation and offline checks do not replace human gold review.
