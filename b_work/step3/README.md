# Step 3 Gold and Reviews

## Completed

- Saves draft gold for all 20 debug questions.
- Saves 60 debug traces and their review copy.
- Builds reviews with units, aliases, special flags, support quotes, Notes,
  and all source context.
- Can rebuild a review from saved gold without writing gold files.
- Exports paired test-set gold using the annotation data version and reviewed
  question type. Debug export keeps its existing data format.
- Supports `presupposition_sets` in gold exports and saved-gold reviews.
- Rebuilt the revised Q1–Q150 data with this script: 150 questions and 453 units.

| File | Edit by hand? | Content |
|---|---|---|
| `gold_annotations.json` | Yes | Units, support references, and notes. |
| `build_gold.py` | Code | Builds gold from paired annotations and samples, or reviews saved gold. |
| `gold_debug.jsonl` | No | The 20 debug gold records. |
| `gold_review.md` | Generated | The debug review copy. |
| `build_traces.py` | Code | Builds full-context controlled mock traces. |
| `traces_debug.jsonl` | No | The 60 debug traces. |
| `traces_review.md` | Generated | Arrival batches and support times. |

### New parts in build_gold.py

1. **Review-only mode.** `--review-from-gold` reads saved gold and writes only
   the review. It keeps gold files unchanged.
2. **Input checks.** Checks versions, sample IDs, answer units, and evidence.
   Both modes accept `d1s0` and `[document title, sentence index]` references.
3. **Draft support.** Shows unfinished units with `support_sets: []` for human
   review. Normal exports require a complete support path for each final answer.
4. **More review content.** Adds all source context and support that uses facts
   given by the question. Shows empty support clearly. Existing source issues stay
   in Notes. The table still shows aliases and special flags.
5. **File safety and table layout.** Stops the review from overwriting input
   files. Handles `|` and line breaks so table cells stay readable.
6. **Premise paths.** Checks and keeps `presupposition_sets`. Shows a separate
   table column and quotes its evidence when a question uses this field.
7. **Revised data.** Keeps the annotation data version, reviewed question type,
   original question numbers, original questions, and revised final answers.
   `--include-unit-json` adds copyable answer units to a review.

New and updated code blocks use `#-------------#` and simple English comments.

## Rules

- Follow `schema.md` v1.3 Section 4 and `labeling_guide.md` v1.2 Section 1.1.
- The record field `schema_version` remains `1.0`.
- Keep the frozen Step2 source files unchanged.
- Gold edits belong in annotations. Keep any review comments before rebuilding.
- Debug annotations use `[document title, sentence index]` support references.
- Both modes accept evidence IDs such as `d1s0` in both support fields.
- A normal export needs the samples and annotations to use the same data version.
- A test-set export must use separate output paths, away from the debug files.
- An empty normal support list gives no direct support. A final answer still
  needs a complete normal or premise path. An unknown candidate may stay open
  only when a valid premise path can complete the answer.
- Review-only mode checks versions, IDs, dependencies, and matching gold units.
  Invalid inputs leave the old review file unchanged.
- Reviews show `aliases`, `by_omission`, `by_presupposition`, and both support fields.
  Existing source issues stay in Notes.
- Normal `support_sets` need all units in `depends_on` to be supported.
- `presupposition_sets` lists separate evidence paths that use a fact given by
  the question. Each group must contain evidence. Empty groups are rejected.
- A premise path needs at least one supported dependency, or no dependencies.
- Every unit with nonempty `presupposition_sets` needs `by_presupposition: true`.
  The flag alone does not skip dependencies or provide support.
- Do not use this shortcut for date comparisons or "both" and "same" questions.
- A sentence's document title identifies its subject. If titles will be hidden
  from the judge, check whether more source sentences are needed for pronouns.
- Generating a review does not mean that a person has approved the gold.

Run from the repository root to build debug gold and its review:

```bash
python3 b_work/step3/build_gold.py
```

To rebuild only a review of saved gold:

```bash
python3 b_work/step3/build_gold.py \
  --samples b_work/step2/prepared/samples_eval_reserved.jsonl \
  --annotations b_work/test_set/batches/batch_01/annotations.json \
  --review-from-gold b_work/test_set/batches/batch_01/gold.jsonl \
  --review b_work/test_set/batches/batch_01/review.md
```

This reads the saved gold and writes only the review. It does not write `--out`.
Saved gold units must match the annotations. Notes may change.

To rebuild revised Batch 1 gold and its review:

```bash
python3 b_work/step3/build_gold.py \
  --samples b_work/test_set/revisions/batch01_05_v1/batch_01/samples.jsonl \
  --annotations b_work/test_set/revisions/batch01_05_v1/batch_01/annotations.json \
  --out b_work/test_set/revisions/batch01_05_v1/batch_01/gold.jsonl \
  --review b_work/test_set/revisions/batch01_05_v1/batch_01/review.md \
  --include-unit-json
```

For Batches 2–5, change `batch_01` in all four paths. Keep reviewed Notes in
annotations before rebuilding. The original Step2 source stays unchanged.

The existing debug trace command is:

```bash
python3 b_work/step3/build_traces.py
```

- Each context sentence is an event, including distractors.
- Whole documents arrive together. Scheduled and visible times are equal.
- Supporting-fact documents are split in citation order across two batches.
- Alternative gold-support documents arrive with their matching support batch.
- Other documents alternate between batches in original document order.
- Trace IDs use `<sample_id>_<schedule>`.

Current debug schedules are provisional:

| Schedule | First batch | Second batch |
|---|---|---|
| `immediate` | All documents at 0 seconds | None |
| `short` | 1 second | 3 seconds |
| `long` | 2 seconds | 8 seconds |

## Next steps

- Review the 300 test-question gold drafts using their batch review copies.
- Apply any later accepted review edits to the matching revision annotations.
- Add data-version and premise-path support to `build_traces.py` before using
  it with revised test-set gold. The current trace script handles debug data.
- Generate test-set traces only after the user finishes gold review.

## Needs review

- Gold answers, dependencies, support sets, aliases, and special flags.
- Draft units with empty support and notes about source issues.
- Final delay settings before main experiments.
