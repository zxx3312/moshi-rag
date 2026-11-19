# Structured Claim Evaluation

These scores use supplied claim spans and gold units. They are not a full semantic evaluation.

Runs: 900. Questions: 300.

| Policy | Data version | Status counts | Runs | Unit-scored runs | Unit EM | Unit F1 | Claim coverage | Structured UCR | Review claims |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| cascade_gpt120_lora_question_only | eval-revised-v1 | error: 11, missing: 588, ok: 301 | 900 | 198 | 0.838 | 0.838 | 0.778 | - | 154 |

| Policy | Clock | Timing kind | TTFR median (n) | TTFGI median (n) | TTCA median (n) | Recorded completions |
|---|---|---|---:|---:|---:|---:|
| cascade_gpt120_lora_question_only | simulated | unknown | - (0) | - (0) | - (0) | 152/900 |

## Limits

- Scores cover only supplied structured claims, not all facts in the full reply.
- Claim extraction and LLM-based semantic scoring are not implemented here.
- Unclear mappings are sent to review; they are not guessed as right or wrong.
- Unit EM/F1 score necessary gold units, not whole-answer benchmark EM/F1.
- No paired bootstrap intervals are computed in this first version.
- A omits Wait calls. Empty runs can be found only with an expected-run list.
- A's speech times are estimates. Use --timing-kind estimated for those logs.
