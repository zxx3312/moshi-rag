# Step 1: B Group Interface v1

B group interface v1 for data preparation and evaluation. B can start the debug data pipeline using v1 while A/C integrate and provide feedback. We do not implement a retriever, controller, replay engine, or scorer, and we do not claim A/C approval or completed adoption.

## Files

- `schema.md`: trace, gold, timing, evidence visibility, and output log conventions.
- `labeling_guide.md`: three claim-level labels, five actions, and annotation examples.
- `experiment_config.json`: v1 common settings and explicit pending decisions.

The Alpha example is fictional and only checks shared understanding. It is not experimental evidence.

## What to do now

1. Read `schema.md`, especially evidence visibility and data isolation.
2. Ask A to review policy inputs, labels, action names, and output fields.
3. Ask C to review audio timestamps and baseline logging compatibility.
4. B checks that the proposed fields can support independent scoring.
5. Walk through the Alpha sample: no evidence at 0 s; only e1 at 2 s; e1 and e2 at 8 s. Ordinary model input must exclude future events and gold answers.
6. Start B debug data preparation under v1. Record A/C integration feedback when it arrives; do not invent confirmation. Fix specific compatibility issues and increment the schema version for incompatible changes.
7. Expand to 20 debug questions using the v1 format. Resolve methodological decisions before the affected evaluation: simulated cost assumptions before timing comparisons, audio alignment before audio timing metrics, and conflict handling before automatic scoring of conflicting cases.

No GPU or model training is required for this interface step. Update them when concrete integration feedback requires a change.

## References already used for the guide

- The pilot trace and analysis inspected in this session, especially `sqa_1009__d8s__s42424242`.
- [Checked pilot metric implementation](https://github.com/zxx3312/moshi-rag/blob/021927e39e40cad2c42fa0541d8631375c236543/experiments/async_retrieval_latency/analysis/metrics.py).
- [Checked delay scheduler](https://github.com/zxx3312/moshi-rag/blob/021927e39e40cad2c42fa0541d8631375c236543/experiments/async_retrieval_latency/scripts/latency_job.py).

The field names define the B group v1 interface; implementation and integration are subsequent work. Do not describe them as features already present in the repository. The 20-question composition remains a debug-data suggestion, not an original proposal requirement.
