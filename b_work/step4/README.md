# Step 4 — Judge SFT Data (300 Training Questions)

Plan and open decisions: `sft_plan.md`. Rules: `b_work/step1/schema.md` v1.3 Section 4, `b_work/step1/labeling_guide.md` v1.2 Section 1.1, and A's `a_work/unit_schema.md` 5.5–5.6 (branch `a-prompt-judge`).

Status: **human review is complete.** After replacing 31 disputed questions, the annotation pool has 300 `reviewed` records and 41 `reject` records. The selected gold contains all 300 reviewed questions (153 2Wiki / 147 Hotpot; 243 train / 57 dev). `sft-v0` remains the data-version identifier and no longer denotes draft review status.

## Files

| File | Edit by hand? | Content |
|---|---|---|
| `convert_hotpot_parquet.py` | — | HotpotQA train parquet (Hugging Face) → original JSON layout. Needs `pyarrow`. |
| `prepare_sft.py` | — | Samples 180 candidates per dataset from official train (150 primary + 30 reserve), excluding all debug and reserved evaluation questions. |
| `prepared/samples_sft_candidates.jsonl`, `prepared/sft_manifest.json` | No (generated) | Candidates with `project_split` (train/dev), `candidate_rank`, `candidate_role`; seed, hashes, counts. |
| `make_batches.py` | — | Annotation worksheets, 30 questions each. |
| `drafts/batch_*.md` | No (generated) | Worksheets: question, answer, supporting facts, 2Wiki triples, all documents with sentence numbers. |
| `drafts/annotations_batch_*.json` | Yes | Unit annotations per worksheet, in the step3 format plus the extensions below. |
| `build_gold_sft.py` | — | Validates annotations and selects the final 300. Explicit replacements must preserve train/dev split; they normally preserve dataset/type, but may cross them when all remaining same-category candidates fail review. Otherwise the next reserve is used in rank order. |
| `gold_sft.jsonl`, `gold_sft_review.md` | No (generated) | Gold records (`data_version: sft-v0`) and a review copy with the cited sentences. |
| `build_sft.py` | — | Training traces, snapshots, judge inputs (A's `judge_messages()`), and targets. |
| `sft/sft_train.jsonl`, `sft/sft_dev.jsonl`, `sft/sft_stats.json` | No (generated) | Chat-format SFT examples with metadata; label statistics and cross-checks. |

## Run

From the repository root. Raw files go to `b_work/step2/raw/` and stay out of Git.

```bash
# 1. Data (see b_work/step2/README.md for the 2Wiki archive)
curl -L -o b_work/step2/raw/hotpot_train_parquet/train-00000-of-00002.parquet \
  https://huggingface.co/datasets/hotpotqa/hotpot_qa/resolve/main/distractor/train-00000-of-00002.parquet
curl -L -o b_work/step2/raw/hotpot_train_parquet/train-00001-of-00002.parquet \
  https://huggingface.co/datasets/hotpotqa/hotpot_qa/resolve/main/distractor/train-00001-of-00002.parquet
python3 b_work/step4/convert_hotpot_parquet.py b_work/step2/raw/hotpot_train_parquet/*.parquet \
  --out b_work/step2/raw/hotpot_train_v1.1_hf.json

# 2. Candidates and worksheets (existing outputs are never overwritten)
python3 b_work/step4/prepare_sft.py --hotpot b_work/step2/raw/hotpot_train_v1.1_hf.json \
  --twowiki b_work/step2/raw/data_ids_april7.zip
python3 b_work/step4/make_batches.py

# 3. Gold, after annotating the worksheets
python3 b_work/step4/build_gold_sft.py --annotations b_work/step4/drafts/annotations_batch_*.json

# 4. SFT examples (reads A's judge code from origin/a-prompt-judge; run `git fetch` first)
python3 b_work/step4/build_sft.py
```

Source hashes (SHA256): HotpotQA parquet `76d3bb30…e68` and `71366162…63f` (Hugging Face LFS IDs); converted JSON `09bddf49…cf75`; `data_ids_april7.zip` `95df2bf5…eef` (same file as step2). Full hashes are in `prepared/sft_manifest.json`.

## SFT-only presupposition support sets

Schema v1.3 standardizes the gold-side `by_presupposition` flag. The SFT builder additionally uses the following support-set representation to decide at which snapshot that flag becomes active:

- `presupposition_sets`: support sets that support the unit only when the question's premise is taken as given. Every such gold unit also carries static `by_presupposition: true`. It becomes SUPPORTED with the dynamic flag when one set is visible and at least one dependency is SUPPORTED (or it has no dependencies).
- The approved rule also covers exactly two named candidates with one unique answer: evidence explicitly ruling out one identifies the other. This extends A's current `derive_conclusion`, which only implements direct positive confirmation; the SFT builder appends this rule to the system prompt and exempts only this known extension from the A-code cross-check.
- `support_sets: []` on a unit whose value no sentence states explicitly (e.g. the losing candidate in "which of A and B won X", or a Wikidata triple the text does not state). The unit is never SUPPORTED except through `presupposition_sets`.

## SFT examples

- **Training traces:** 3 random document orders per question, one document per second. These are training-only schedules, never used for latency results.
- **Snapshots kept:** a label changes; a unit becomes blocked (its own evidence visible, a dependency not yet supported); up to 2 distractor-only snapshots; and the snapshot with all evidence. At most 10 per question, deduplicated by visible set.
- **Input:** A's `judge_messages()` at the commit recorded in `sft_stats.json` (system prompt + 3 few-shot examples + request), plus the documented system-prompt sentence for two-candidate elimination by presupposition; `--no-examples` drops the few-shot pairs. Units are gold descriptions and `depends_on` without answers.
- **Target:** A's `JUDGE_SCHEMA` reply. `value` is the gold `expected_answer`; citations are the first visible support set (a conclusion cites its dependencies' evidence).
- **Checks** (the build fails on any): no overlap with debug or reserved evaluation questions; no question in both splits; citations visible in the request; UNRESOLVED targets carry no value or citations. `sft_stats.json` also lists disagreements with A's `OracleJudge` + `resolve_dependencies` and `derive_conclusion`.

## Known limits

- **No `CONTRADICTED` targets.** Questions with conflicting evidence are rejected.
- **Gold descriptions, not decomposer units.** Runtime units come from A's decomposer and may be worded differently.
- **All selected questions are reachable.** Every necessary unit in the current Gold becomes supported when all evidence is visible; the builder validates this count on every rebuild.
