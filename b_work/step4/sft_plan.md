# Step 4 — Judge SFT Dataset (300 Questions): Execution Plan

Status (2026-11-03): Steps 2–4 and 6–8 are implemented (see `README.md`), and the selected 300 gold questions have completed human review. After the 31-question replacement audit, 300 annotation records are `reviewed` and 41 are `reject`; all 300 reviewed records are selected. The planned double-review agreement record in Step 5 is still open.

Goal: build supervised fine-tuning data for A's LoRA judge (W3, `a_work/turntaking/judge.py` on branch `a-prompt-judge`). One training example is one judge call: the question, the answer units (without answers), and the evidence visible at time `t`, mapped to a label, value, and citations for each unit.

## 0. Ground rules

- **Source: official train splits only.** The 300 reserved questions in `b_work/step2/prepared/samples_eval_reserved.jsonl` are final evaluation data and must not be used for training, prompt tuning, or model selection (`b_work/step2/README.md`). The 20 debug questions are not used either.
- **No overlap.** Exclude every debug and reserved `sample_id`, and every exact normalized question text (same normalization as `prepare_step2.py`), including overlap between the two source datasets.
- **One question, one split.** All schedules and snapshots of a question go to the same split (train or dev).
- **Same input format as the runtime judge.** The SFT prompt is produced by A's `judge_messages()` code. B appends one documented sentence for the approved two-candidate elimination form of `by_presupposition`; A's runtime prompt must adopt the same rule before evaluation.
- **No conflict cases.** Examples with both supporting and conflicting evidence are excluded until a conflict rule is frozen (`labeling_guide.md` Section 1; `unit_schema.md` 5.6).
- **Data version:** `sft-v0` on every generated record.

## 1. Freeze the open rules first

Mass annotation multiplies every unresolved rule by 300. Agree on these and record them in `labeling_guide.md` (v1.2) before Step 4:

| Decision | Proposed default | Where it is pending |
|---|---|---|
| Question presuppositions | Accepted as premises. Evidence may confirm the answer directly or, for exactly two named candidates with one unique answer, explicitly rule out the other candidate. Contradictory premises go to human review. Flag affected units `by_presupposition: true`. | `labeling_guide.md` v1.2 Section 1.1 |
| Negatives that need world knowledge | `UNRESOLVED` (current rule) | `labeling_guide.md` Section 5 |
| Deterministic comparison | The judge produces it (as in A's prompt) | `labeling_guide.md` Section 5 |
| Citation target when several support sets are complete | The first complete set in gold order | new |
| Split sizes | 240 train / 60 dev, stratified by question type | `experiment_config.json` |
| Composition | Mirror the reserved set: HotpotQA 75 bridge + 75 comparison; 2Wiki ~38 each of comparison, bridge_comparison, compositional, inference | new |

The debug gold Q13 and Q17 are updated to the agreed presupposition rule, so the debug set and SFT data follow the same rule.

## 2. Download the official train files

Same procedure as `b_work/step2/README.md`, recording SHA256 for each file:

- HotpotQA: `hotpot_train_v1.1.json`.
- 2WikiMultiHopQA: `train.json` inside the same `data_ids_april7.zip` already used for dev, plus its alias file.

Raw files stay outside Git.

## 3. Sample 300 questions — `prepare_sft.py`

1. Load train records and apply the same structural checks as `prepare_step2.py` (support indices in range, nonempty answer, supporting titles present).
2. Remove the overlaps listed in Section 0, using `split_manifest.json`.
3. Shuffle with a fixed seed and draw per question type to the composition in Section 1. **Draw about 20% extra candidates** (≈360) so that questions rejected in review can be replaced from the same ordered list without reseeding.
4. Assign train/dev per question, stratified by type.
5. Write `prepared/samples_sft_candidates.jsonl` and `prepared/sft_manifest.json` (seed, hashes, IDs, type counts, exclusions). Do not overwrite existing outputs.

## 4. Draft gold units automatically

Manual annotation at the debug-set level of detail (about 10 minutes per question) is too slow for 300 questions. Draft first, then review.

- **2Wiki:** build units from `type` + `evidences` triples (one triple per fact unit, then a conclusion unit for comparisons) following `schema.md` 4.3. Map each triple to its supporting sentence for `support_sets`. Take aliases from the alias table.
- **HotpotQA:** build units from `type` + `supporting_facts`. Bridge: one unit per supporting document in hop order. Comparison: one fact unit per entity, then a conclusion unit. An LLM may draft unit descriptions; every draft is reviewed.
- **Alternative support:** search the distractor sentences for other sentences that state the same value (string match on answer and aliases, plus an optional LLM check), and add them as candidate extra sets **marked for review**. Missing alternative support produces wrong `UNRESOLVED` targets, the main source of label noise.
- Output: `drafts/annotations_batch_*.json` in the same format as `b_work/step3/gold_annotations.json`. Drafts are changed to `status: "reviewed"` after human review; rejected candidates use `status: "reject"`.

## 5. Human review

- Generalize `b_work/step3/build_gold.py` to take input/output paths, and run its validation on the drafts. It already checks titles, sentence ranges, dependencies, support-set rules, and field types.
- Generate a review copy (as `gold_review.md`) with the cited sentence text, and split the questions among reviewers.
- Review checklist, taken from `b_work/step2/review_notes.md` and `labeling_guide.md` 1.1:
  1. Each cited sentence states the value explicitly (no inference).
  2. Pronouns resolve through the document title; otherwise cite the earlier sentence too.
  3. Distractor sentences that also support a unit are added as extra sets.
  4. `by_omission` is used only under Exception 2.
  5. Presupposition handling follows Section 1.
  6. The answer is normalized; surface variants go to `aliases`.
  7. Reject the question (with a reason) if it is ambiguous, wrongly answered by the source, or needs a conflict rule.
- **Double-review about 10%** (30 questions) independently and report agreement on units and support sets. Resolve disagreements against the source text and fix the guide if a rule was unclear.
- Replace rejected questions from the extra candidates, in order, until 300 pass. Set `status: "reviewed"`.

## 6. Build training traces

Reuse `b_work/step3/build_traces.py` (controlled text replay, whole documents arriving). The three evaluation schedules give only about two distinct non-empty evidence sets per question, which is too few for training. Add training-only schedules:

- `k` (e.g. 3) random document arrival orders per question, one document per step.
- Keep the `d<N>s<M>` evidence IDs so that gold support sets apply unchanged.

These schedules are a training augmentation and are never used to report latency results.

## 7. Generate SFT examples — `build_sft.py`

For each trace and each evidence arrival (the empty-evidence step is skipped, as in `PromptJudge`):

1. **Input:** build the message list with A's `judge_messages()`. Use gold unit descriptions and `depends_on` with answers stripped (the same input `eval_judge.py` uses), and evidence with document titles.
2. **Target:** compute it from gold with the oracle logic plus values:
   - A unit is `SUPPORTED` when a support set is fully visible and all its `depends_on` units are `SUPPORTED`. Otherwise `UNRESOLVED`, with value `null` and no citations.
   - `value` = `expected_answer`. `citations` = the support set chosen by the Section 1 rule; a conclusion unit cites its dependencies' evidence. `by_omission` comes from gold.
   - Serialize exactly in `JUDGE_SCHEMA` form.
3. **Deduplicate and balance:** keep every snapshot where some label changes; keep at most a few distractor-only snapshots per question, which teach the model not to over-claim. Cap at about 10 examples per question, roughly 2,500–3,000 in total.
4. Write `sft_train.jsonl` and `sft_dev.jsonl` as chat messages (`system` / `user` / `assistant`), each with `sample_id`, `trace_id`, `time_s`, and `data_version` metadata for tracing.

## 8. Quality checks

Automatic (the script fails on any violation):

- No `sample_id` or normalized question overlaps with debug or reserved data.
- No question appears in both train and dev.
- Every citation is visible at that snapshot; no `SUPPORTED` dependent unit has an unsupported dependency.
- Every target parses against `JUDGE_SCHEMA`; the prompt length fits the training context.
- Report label counts by question type, `by_omission`, and presupposition flags.

Manual:

- Read 50 random examples end to end.
- Run A's `OracleJudge` over the same traces and confirm its labels equal the SFT targets.
- Run the current `PromptJudge` on `sft_dev.jsonl` as a baseline. Its disagreements with the targets show both annotation errors and what SFT has to learn.

## 9. Hand-off

- Commit the scripts, manifests, `gold_annotations_sft.json`, and the generated JSONL files (if size permits; otherwise record their hashes).
- Write `b_work/step4/README.md` with the run commands and final counts.
- A trains the LoRA judge on `sft_train.jsonl` and selects checkpoints on `sft_dev.jsonl`. Error analysis uses the 20 debug questions; the final comparison uses `eval_judge.py` on the reserved 300, run once.

## Known limitations

- **No `CONTRADICTED` targets.** Gold has no contradiction annotations and conflict cases are excluded, so the SFT judge will rarely or never output `CONTRADICTED`. Adding synthetic conflicts needs a frozen conflict rule first.
- **Gold unit descriptions, not decomposer units.** At runtime the judge sees units from A's decomposer. Training on gold descriptions alone may not transfer if the decomposer's wording differs; consider adding decomposer-produced units, aligned to gold, as a later augmentation.
- **Controlled replay only.** Snapshots come from document-level text replay, not real retrieval or audio timing.

## Effort estimate

| Step | Who | Estimate |
|---|---|---|
| 1 Rule freeze | B with A | One meeting |
| 2–4 Download, sampling, auto-draft | B | 1–2 days of scripting |
| 5 Human review | B (split among reviewers) | ~3–5 min per question, ≈20–25 person-hours including double review |
| 6–8 Traces, SFT build, checks | B | 1–2 days |
