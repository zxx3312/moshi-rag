# Step 3 — Gold Units for the Debug Set

Rules: `b_work/step1/schema.md` v1.1 Section 4 and `b_work/step1/labeling_guide.md` v1.1 Section 1.1. Source data: `b_work/step2/prepared/samples_debug.jsonl` (frozen; not modified here). Review decisions: `b_work/step2/review_notes.md`.

## Files

| File | Edit by hand? | Content |
|---|---|---|
| `gold_annotations.json` | Yes | Units per question, with evidence cited as `[document title, sentence index]` and annotation notes. |
| `build_gold.py` | — | Converts annotations to gold records and validates them. |
| `gold_debug.jsonl` | No (generated) | Gold records in the `schema.md` Section 4 format, one per line. |
| `gold_review.md` | No (generated) | Review copy: units, the cited sentence text, and notes for each question. |
| `build_traces.py` | — | Builds controlled mock traces for every question that has gold units, and validates them. |
| `traces_debug.jsonl` | No (generated) | Traces in the `schema.md` Section 3 format: currently questions 11–20 × 3 schedules. |
| `traces_review.md` | No (generated) | Review copy: which documents arrive in each batch, and when each gold unit becomes supported. |

Run from the repository root, gold first because the trace builder reads it:

```bash
python3 b_work/step3/build_gold.py
python3 b_work/step3/build_traces.py
```

## Trace schedules (provisional)

Delay schedules are not frozen yet (`experiment_config.json`, `pending_decisions`). The batch times are set in `SCHEDULES` at the top of `build_traces.py`, anchored on the existing 0–8 s pilot sweep:

| Schedule | Batch 1 | Batch 2 |
|---|---|---|
| `immediate` | all documents at 0.0 s | — |
| `short` | 1.0 s | 3.0 s |
| `long` | 2.0 s | 8.0 s |

- Every context sentence is an event, including distractors. Documents arrive whole; `visible_time_s` equals `scheduled_time_s` (controlled text replay).
- The documents cited by `supporting_facts` are split in citation order: the first half in batch 1, the rest in batch 2. In questions 11–20, citation order is hop order for every bridge question, so batch 1 holds the first hop; check this when adding other questions.
- A document cited only as alternative support in `gold_debug.jsonl` arrives with the `supporting_facts` document of the same unit. Other distractors alternate between batches in document order.
- `trace_id` is `<sample_id>_<schedule>`.
- Questions without gold units get no trace, because alternative-support documents can only be placed once gold exists. When gold for questions 1–10 is added to `gold_debug.jsonl`, rerunning `build_traces.py` also produces their traces.

The script stops with an error on unknown titles, sentence indices out of range, invalid or cyclic dependencies, `[]` support sets, `[[]]` without dependencies, questions with no necessary unit, and malformed `aliases` / `by_omission`.

## Conventions

- **Evidence IDs** are `d<N>s<M>`: `N` is the 1-based document position in the sample's context (the "Document N" numbering in `samples_debug_readable.md`), `M` is the 0-based sentence index. Traces must use the same IDs, which means traces should include every context sentence that a support set cites, including distractor sentences.
- **Document titles:** evidence is assumed to be shown together with its document title, as in HotpotQA. A sentence whose subject is the article's topic ("He won...", "The team was created...") then stands alone. Sentences that need an earlier sentence for other content ("The pair...", sentence fragments) are cited together with it. If traces or the judge input will not include titles, Q13, Q14 and Q17 need their opening sentences added to the support sets.
- **Status:** `draft` or `pending_decision`. Q17 is `pending_decision` until the presupposition rule in `labeling_guide.md` Section 5 is agreed.
