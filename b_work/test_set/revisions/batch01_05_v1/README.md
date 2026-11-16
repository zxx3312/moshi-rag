# Revised Evaluation Data — Batches 1–5

## Completed

- Applies the accepted Q1–Q150 review decisions to paired samples and annotations.
- Saves 150 revised questions and 453 gold units. Forty question texts changed.
- Uses the original [Step3 gold builder](../../../step3/build_gold.py).
- Keeps every source sentence and evidence ID. No question was replaced.
- Saves English Notes, original questions, source answers, and copyable unit JSON.
- Q55 uses `presupposition_sets` for the same d9s0 evidence already accepted.
  Its answer and support times are unchanged. Other units use normal support.
- Checks 900 evidence snapshots against A's Oracle and B's evaluator, with no
  support disagreements. Checks 1,743 supported citations too.
- Five batch rebuilds produce identical gold and review files.
- Keeps the original Step2 samples and original batch data unchanged.
- Includes these 150 questions in the shared
  [900-trace set](../../traces/eval_revised_v1/README.md). It uses paired samples
  and gold from both revision folders and keeps all source context.

| Batch | Questions | Units | Review |
|---|---|---:|---|
| 01 | Q1–Q30 | 79 | [Review](batch_01/review.md) |
| 02 | Q31–Q60 | 95 | [Review](batch_02/review.md) |
| 03 | Q61–Q90 | 92 | [Review](batch_03/review.md) |
| 04 | Q91–Q120 | 98 | [Review](batch_04/review.md) |
| 05 | Q121–Q150 | 89 | [Review](batch_05/review.md) |

Each batch has editable `annotations.json`, paired `samples.jsonl`, generated
`gold.jsonl`, `review.md`, and `checks.json`. The combined
[samples](samples.jsonl) and [gold](gold.jsonl) contain all 150 questions.
[manifest.json](manifest.json) records the source and applied review decisions.
[validation_report.json](validation_report.json) records the checks.

## Rules

- Use samples and gold from the same revision together.
- `schema_version` is `1.0`. `data_version` is `eval-revised-v1`.
- In samples, `answer` keeps the original source answer. `gold_answer` is the
  revised final answer. Use gold units to score the revised question.
- Keep the source `type` as a source label. Use gold `question_type` for the
  actual unit structure of the revised question.
- Edit annotations for unit or Notes changes. Keep sample questions and
  `gold_answer` in step with accepted answer changes.
- Normal support needs every dependency. A premise path needs at least one
  supported dependency, or no dependencies.
- Nonempty `presupposition_sets` requires `by_presupposition: true` and real
  evidence IDs. The field is used only when the question gives the needed premise.
- Keep this set out of training, prompt tuning, and model selection.
- Keep Q7's possible-family-tree wording and Q52's own-biography wording.
  These limits are part of the accepted questions.

Rebuild one batch from the repository root:

```bash
python3 b_work/step3/build_gold.py \
  --samples b_work/test_set/revisions/batch01_05_v1/batch_01/samples.jsonl \
  --annotations b_work/test_set/revisions/batch01_05_v1/batch_01/annotations.json \
  --out b_work/test_set/revisions/batch01_05_v1/batch_01/gold.jsonl \
  --review b_work/test_set/revisions/batch01_05_v1/batch_01/review.md \
  --include-unit-json
```

Change `batch_01` in all four paths to rebuild another batch. After changing a
batch, refresh the combined samples, gold, and check reports before using them.
The combined files are copies of the five batch outputs, not separate inputs.

## Next steps

- Agree with the team on the final paired 300-question revision.
- Review the shared trace batches and support times.
- Rebuild the shared traces after any accepted input or delay changes.

## Needs review

- Final experiment inputs and delay schedules.
- Traces use provisional times. Policy and model experiments have not been run.
