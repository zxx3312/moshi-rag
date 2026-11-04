# B Evaluation

## Completed

- Reads policy logs from A's replay runner.
- Checks record IDs, versions, times, evidence snapshots, citations, and gold
  dependencies.
- Maps supplied structured claims to gold units through reviewed mappings or
  known gold-aligned policy IDs.
- Scores declared values with unit EM/F1 and cited gold support rules.
- Computes TTFR, TTFGI, and TTCA when the required times and claim scores are known.
- Saves run scores, claim scores, review items, validation issues, summaries,
  input hashes, and scoring options.
- Includes fictional examples and 31 passing tests.
- Checked 300 offline runs from 20 debug questions and 60 traces. These runs
  used A's placeholder text and made no model calls.

## Rules

Use Python 3. No extra packages are needed. Run commands from the repository root.
Use A's runner to make policy logs. This evaluator reads the supplied claim spans.

- Trace, gold, and log records use schema version `1.0`. Their sample IDs and
  data versions must match.
- Each snapshot ID must be visible at decision time. Each cited ID must be in
  that snapshot. Evidence arriving later cannot support the earlier decision.
- Known claim times must fit output times. Missing times and excluded scores
  stay `null`.
- A supported claim needs a matching gold value, a full cited support set, and
  supported dependencies. Gold aliases are accepted.
- Comparison units with `[[]]` use their parents' evidence. Question-premise
  support uses `presupposition_sets`. Omission and premise cases have separate counts.
- A Final Answer action records an attempt. Completion requires all necessary
  gold units to have correct values and cited support.
- Retrieval misses, invalid logs, errors, and expected missing runs stay in the reports.
- Placeholder runs get no scores by default. `--allow-placeholder` enables
  diagnostic scores for code checks.

A's claim names `start`, `end`, and `cited_evidence_ids` work directly.
The aliases `start_time_s`, `end_time_s`, and `evidence_ids` also work.
Conflicting values under both names are rejected.

Gold unit IDs and A's question-only unit IDs are separate. Claims with unclear
mappings go to `review_queue.jsonl`. A claim needs a declared `value` for scoring.
Use `--reviews` to load checked mappings. Both indexes below start at 0.
`record_index` counts rows within a run in file order; `claim_index` counts
claims within that row. Keep the source log unchanged after review.

```json
{"run_id":"custom_alpha_long__example_policy__s0","record_index":1,"claim_index":0,"gold_unit_id":"u1","reviewer":"example"}
```

Use `--aligned-policy` only when the policy's unit IDs are known to match gold,
such as `evidence_aware+oracle`. A final claim with ID `answer` can map directly
when the question has exactly one necessary gold unit. `--allow-value-match`
allows an approximate mapping when exactly one gold unit matches the value.
The output counts these approximate mappings separately.

| Metric | Current rule |
|---|---|
| Unit EM | Mean exact value match over necessary gold units. Missing units score 0. |
| Unit F1 | Mean word-overlap score over necessary gold units. |
| Structured UCR | Wrong-value or unsupported/uncited claims divided by supplied claims. Null when there are no claims or any claim needs review. |
| TTFR | First output starts, including an acknowledgment or progress message. Wait is excluded. |
| TTFGI | First supported structured claim starts. |
| TTCA | Earliest time when all necessary supported claims have finished. Conflicting values require review. |

Value matching uses lowercase text and removes accents, punctuation, articles,
and extra spaces. Unit scores measure the supplied values against gold units.
Unclear mappings and conflicting answers make completion scores null.

Timing is `unknown` by default. Use `--timing-kind estimated` for A's current
runner. Use `observed` for measured speech times with an `audio_stream` trace.
Different clocks, data versions, and timing kinds stay in separate groups.
Score means use scored runs only. Time medians include their sample counts.

The default inputs are `step3/traces_debug.jsonl` and `step3/gold_debug.jsonl`.
Set `--traces` and `--gold` for another data set. `--runner-commit` records the
code version that made the log. `--expected-policies` lists policies expected
on every input trace; a run with no rows gets status `missing`. The expected
seed is 0, or the value passed with `--expected-seed`.

Run the fictional example with checked mappings:

```bash
python3 -m b_work.eval.run_eval \
  --logs b_work/eval/examples/policy_log.jsonl \
  --traces b_work/eval/examples/trace.jsonl \
  --gold b_work/eval/examples/gold.jsonl \
  --reviews b_work/eval/examples/claim_reviews.jsonl \
  --timing-kind estimated \
  --out b_work/eval/output/example
```

Outputs are `run_scores.jsonl`, `claim_scores.jsonl`, `review_queue.jsonl`,
`validation_issues.jsonl`, `summary.json`, `summary.md`, and
`evaluation_config.json`. Run-level review reasons are in `run_scores.jsonl`.
The `output/` folder is ignored by Git.

Exit code 1 means invalid log rows were found. Exit code 2 means an input could
not be read or checked. Pending reviews do not cause a nonzero exit code.

Run the tests with:

```bash
python3 -m unittest discover -s b_work/eval/tests -v
```

## Next steps

- Extract all atomic facts from full replies, keeping negation and corrections.
- Add independent semantic support checks, including facts outside the gold list.
- Score final short answers with the official dataset rules.
- Add useful-information checks and full-fact timing.
- Track valid corrections when computing answer completion and TTCA.
- Add C's audio log conversion and speech alignment.
- Add no-claim rate, timeout and observation-window reports, and a full run manifest.
- Add paired confidence intervals and prepare the main evaluation gold and traces.

## Needs review

- Claim-to-gold mappings, especially multipart answers and approximate value matches.
- Gold support sets, dependencies, omission cases, and question-premise cases.
- Shared time definitions and the accuracy of estimated speech times.
- Expected run lists and errors recorded in separate model logs. A's policy log
  omits Wait calls and some model errors.
- Real model outputs and their facts before using the scores in final results.
