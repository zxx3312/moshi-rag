# A Group: Turn-Taking Controller (skeleton)

Text-level trace replay for the evidence-aware policy and the four rule baselines.
Python 3.9+, standard library only.

```bash
python3 a_work/run_demo.py                      # replay demo traces, print timelines + preview metrics
python3 -m unittest discover -s a_work/tests    # leakage and sanity checks
```

## Layout

| File | Role |
|---|---|
| `turntaking/schema.py` | Action/label strings from B's interface v1; observation and decision types |
| `turntaking/judge.py` | Judge API, `OracleJudge` (gold support sets), `PromptJudge` stub, dependency resolution, sufficiency state |
| `turntaking/policies.py` | `EvidenceAware` (ours), `WaitAll`, `FixedProgress`, `TimeOnly`, `FirstEvidence` |
| `turntaking/replay.py` | Simulated clock, evidence visibility filter, `policy_log` records |
| `turntaking/preview.py` | Rough TTFR/TTFGI/TTCA and unsupported-claim counts for self-checks; B's eval is authoritative |
| `demo/` | Two hand-made traces: one real 2Wiki debug question with a distractor, and B's fictional Alpha example |

## Data flow

```
trace.jsonl ──► replay (only evidence with visible_time_s <= t) ──► policy.decide(obs)
                                                                     │  EvidenceAware: judge → dependencies → sufficiency state → action
                                                                     ▼
                                                              policy_log.jsonl ──► B eval
gold.jsonl ──► OracleJudge only (separate input path)
```

## Not done yet

- `PromptJudge` (W2) and LoRA judge (W3).
- Controller-side unit decomposition: the demo copies units from gold with answers stripped, which is only valid for oracle runs.
- The generator is a placeholder: claims are rendered as `[unit: description <- citations]`.
- Simulated costs are placeholders: `decision_cost_s=0`, 1 s per short utterance, 2 s per claim. Pending agreement with B.
- Only non-Wait actions are logged.
