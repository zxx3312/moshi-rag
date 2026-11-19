# Structured Claim Evaluation

These scores use supplied claim spans and gold units. They are not a full semantic evaluation.

Runs: 60. Questions: 20.

| Policy | Data version | Status counts | Runs | Unit-scored runs | Unit EM | Unit F1 | Claim coverage | Structured UCR | Review claims |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| cascadesystem_question_only | debug-v0 | error: 4, ok: 56 | 60 | 2 | 0.000 | 0.000 | 0.000 | - | 104 |

| Policy | Clock | Timing kind | TTFR median (n) | TTFGI median (n) | TTCA median (n) | Recorded completions |
|---|---|---|---:|---:|---:|---:|
| cascadesystem_question_only | simulated | unknown | - (0) | - (0) | - (0) | 0/60 |

## Limits

- Scores cover only supplied structured claims, not all facts in the full reply.
- Claim extraction and LLM-based semantic scoring are not implemented here.
- Unclear mappings are sent to review; they are not guessed as right or wrong.
- Unit EM/F1 score necessary gold units, not whole-answer benchmark EM/F1.
- No paired bootstrap intervals are computed in this first version.
- A omits Wait calls. Empty runs can be found only with an expected-run list.
- A's speech times are estimates. Use --timing-kind estimated for those logs.
