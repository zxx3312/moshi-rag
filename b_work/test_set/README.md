# Main Evaluation Test Set

## Completed

- Saves 300 draft gold records in ten batches of 30 questions.
- Keeps the reserved question IDs, source answers, and source text from Step2.
- Each batch has editable annotations, draft gold, checks, and a review copy.
- Review copies include the support quotes and all source context.
- Uses the Step3 formatter to show aliases, special flags, and support sets.
- Gold draft checks are in [validation_report.json](validation_report.json).

| Batch | Questions | Source | Review |
|---|---|---|---|
| 01 | Q001–Q030 | 2Wiki | [Review](batches/batch_01/review.md) |
| 02 | Q031–Q060 | 2Wiki | [Review](batches/batch_02/review.md) |
| 03 | Q061–Q090 | 2Wiki | [Review](batches/batch_03/review.md) |
| 04 | Q091–Q120 | 2Wiki | [Review](batches/batch_04/review.md) |
| 05 | Q121–Q150 | 2Wiki | [Review](batches/batch_05/review.md) |
| 06 | Q151–Q180 | HotpotQA | [Review](batches/batch_06/review.md) |
| 07 | Q181–Q210 | HotpotQA | [Review](batches/batch_07/review.md) |
| 08 | Q211–Q240 | HotpotQA | [Review](batches/batch_08/review.md) |
| 09 | Q241–Q270 | HotpotQA | [Review](batches/batch_09/review.md) |
| 10 | Q271–Q300 | HotpotQA | [Review](batches/batch_10/review.md) |

## Rules

- All 300 annotations are drafts. Human review is needed before final evaluation.
- Review and edit `batches/batch_NN/annotations.json` first.
- Keep each unit's value, dependencies, and support sets clear.
- Evidence IDs use the source document position and sentence index: `d1s0`.
- Empty `support_sets: []` marks support that still needs review. It does not
  establish an answer or a negative fact.
- A unique-choice answer may use `by_presupposition: true`. Its `depends_on`
  lists only the needed facts, with evidence in their `support_sets`.
- Generate traces only after the gold review is complete.
- Reuse [Step3's trace script](../step3/build_traces.py).
- Traces must include every context sentence. Use the supporting facts and gold
  support to arrange whole documents into arrival batches, as Step3 does.
- Keep all test questions out of training, prompt tuning, and model selection.

To rebuild a review from its saved gold, run this from the repository root:

```bash
python3 b_work/step3/build_gold.py \
  --samples b_work/step2/prepared/samples_eval_reserved.jsonl \
  --annotations b_work/test_set/batches/batch_01/annotations.json \
  --review-from-gold b_work/test_set/batches/batch_01/gold.jsonl \
  --review b_work/test_set/batches/batch_01/review.md
```

For another batch, replace `batch_01` in the three paths. This mode writes only
the review. The saved gold units must match the annotations. Notes may change.

## Next steps

- Review each batch's units, support sets, and notes.
- Resolve source issues and confirm the accepted gold answers.
- After review, update gold outputs and review copies using the Step3 scripts.
- Then use Step3's trace script to make and check the full-context traces.

## Needs review

- All 300 draft answers and their necessary support chains.
- 82 questions have review flags. Of all 300 questions, 52 lack complete
  accepted gold support even with all source context.
- Source entity links, weak supporting facts, missing support, and question premises.
- Trace generation is pending gold review.
