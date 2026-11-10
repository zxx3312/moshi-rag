# Step 3 Gold and Reviews

## Completed

- Saves draft gold for all 20 debug questions.
- Saves 60 debug traces and their review copy.
- Builds reviews with units, aliases, special flags, support quotes, Notes,
  and all source context.
- Can rebuild a review from saved gold without writing gold files.

| File | Edit by hand? | Content |
|---|---|---|
| `gold_annotations.json` | Yes | Units, support references, and notes. |
| `build_gold.py` | Code | Builds debug gold or reviews of saved gold. |
| `gold_debug.jsonl` | No | The 20 debug gold records. |
| `gold_review.md` | Generated | The debug review copy. |
| `build_traces.py` | Code | Builds full-context controlled mock traces. |
| `traces_debug.jsonl` | No | The 60 debug traces. |
| `traces_review.md` | Generated | Arrival batches and support times. |

### New parts in build_gold.py

1. **Review-only mode.** `--review-from-gold` reads saved gold and writes only
   the review. It keeps gold files unchanged.
2. **Input checks.** Checks versions, sample IDs, and answer units. Review mode
   accepts both `d1s0` and `[document title, sentence index]` references.
3. **Draft support.** Shows unfinished units with `support_sets: []` for human
   review. This does not approve their answers. Normal gold generation stays strict.
4. **More review content.** Adds all source context and support that uses facts
   given by the question. Shows empty support clearly. Existing source issues stay
   in Notes. The table still shows aliases and special flags.
5. **File safety and table layout.** Stops the review from overwriting input
   files. Handles `|` and line breaks so table cells stay readable.

New and updated code blocks use `#-------------#` and simple English comments.

## Rules

- Follow `schema.md` v1.3 Section 4 and `labeling_guide.md` v1.2 Section 1.1.
- The record field `schema_version` remains `1.0`.
- Keep the frozen Step2 source files unchanged.
- Gold edits belong in annotations. Keep any review comments before rebuilding.
- Debug annotations use `[document title, sentence index]` support references.
- Review-only mode also accepts annotations with evidence IDs such as `d1s0`.
- The ordinary gold builder keeps strict support checks. Empty support lists
  are allowed only when displaying saved drafts for human review.
- Review-only mode checks versions, IDs, dependencies, and matching gold units.
  Invalid inputs leave the old review file unchanged.
- Reviews show `aliases`, `by_omission`, `by_presupposition`, and support sets.
  Existing source issues stay in Notes.
- For two named candidates with one unique answer, keep only the facts needed
  to confirm or rule out a candidate. The answer depends on those facts.
- Mark that answer with `by_presupposition: true`. Use `support_sets` and
  `depends_on` for its evidence. The flag does not replace evidence.
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
- Support test-set gold export after review. Keep the existing Step3 script.
- Generate test-set traces only after the user finishes gold review.

## Needs review

- Gold answers, dependencies, support sets, aliases, and special flags.
- Draft units with empty support and notes about source issues.
- Final delay settings before main experiments.
