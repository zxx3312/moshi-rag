# Shared Data and Log Interface — B Group v1

Status: B GROUP INTERFACE v1 FOR INTEGRATION. B defines this common interface for data preparation and evaluation. A and C should use it for integration and report specific incompatibilities. Their feedback is not a prerequisite for B to start the debug data pipeline. This document does not claim that A/C have reviewed it or that the interface is already implemented in the repository.

## 1. Shared conventions

| Item | Proposed convention |
|---|---|
| Schema version | `1.0`; incompatible versions must be rejected explicitly |
| Data version | `debug-v0`; required on traces, gold records, and output logs |
| Sample ID | `<dataset>_<source_id>`; unique across datasets |
| Trace ID | Identifies a question and a specific evidence schedule |
| Run ID | Identifies a trace, policy, seed, and attempt |
| Time origin | `question_end`: the end of user speech is zero |
| Time unit | Seconds, represented as numbers |
| Clock | `simulated` for text replay; `audio_stream` for speech runs |
| Missing values | JSON `null`, never silently replaced by zero |
| Evidence | Stable evidence IDs, text, and source location |
| Serialization | UTF-8 JSONL: one JSON object per line |

Keep simulated-clock and audio-clock results separate. For text replay, record how decision and generation costs advance the clock before claiming latency benefits. That cost model is still pending.

## 2. Evidence visibility

- `scheduled_time_s`: planned availability on the normalized clock.
- `visible_time_s`: when the evidence becomes usable under the agreed visibility convention.
- In controlled text replay, the two can be equal by construction.
- For the existing Moshi audio pipeline, propose using `reference_ingestion_end_time - user_end_time` as a conservative proxy. This is an approximation, not proof of complete semantic processing.
- Backend receipt is not model visibility. Preserve raw receipt and injection timestamps in an adapter when available.
- At a model call at time `t`, include only evidence with `visible_time_s <= t`.
- Preserve negative normalized times for events before the user finished; mark overlap instead of clipping them to zero.

For the inspected pilot sample, the normalized visibility proxy is `12.48 - 3.44 = 9.04` seconds, not 8 seconds.

## 3. Trace record: scheduler only

Required fields: `schema_version`, `data_version`, `sample_id`, `trace_id`, `question`, `time_origin`, `clock`, `trace_type`, `events`, `retrieval_complete_time_s`.

Each event requires `evidence_id`, `scheduled_time_s`, `visible_time_s`, `text`, and `source`. `source` preserves the dataset/document location. The retrieval-completion field may be null when unknown; completion does not guarantee sufficient evidence.

Fictional example, formatted across lines for readability:

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "sample_id": "custom_alpha001",
  "trace_id": "custom_alpha001_long",
  "question": "Who leads Alpha, and when was it released?",
  "time_origin": "question_end",
  "clock": "simulated",
  "trace_type": "controlled_mock",
  "events": [
    {"evidence_id": "e1", "scheduled_time_s": 2.0, "visible_time_s": 2.0,
     "text": "Alpha is led by Alice.", "source": {"document_id": "fictional_doc_1", "sentence_index": 0}},
    {"evidence_id": "e2", "scheduled_time_s": 8.0, "visible_time_s": 8.0,
     "text": "Alpha was released on June 1.", "source": {"document_id": "fictional_doc_2", "sentence_index": 0}}
  ],
  "retrieval_complete_time_s": 8.0
}
```

Do not pass the whole trace to an ordinary model. Its runtime input should contain only the question, current time, visible evidence, and permitted conversation history. At time 2 seconds, only e1 is visible. Future event times and e2's text remain private to the scheduler.

## 4. Gold record: evaluation only

Required fields: versions, `sample_id`, and `units`. Each gold unit contains `unit_id`, `description`, `necessary`, `expected_answer`, `depends_on`, and `support_sets`.

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "sample_id": "custom_alpha001",
  "units": [
    {"unit_id": "u1", "description": "Identify the leader", "necessary": true,
     "expected_answer": "Alice", "depends_on": [], "support_sets": [["e1"]]},
    {"unit_id": "u2", "description": "Identify the release date", "necessary": true,
     "expected_answer": "June 1", "depends_on": [], "support_sets": [["e2"]]}
  ]
}
```

Within each inner support list, all evidence items are needed. Across lists, any one complete set is sufficient. Evidence IDs are pointers: annotators must verify semantic support in the source text.

Gold answers, gold labels, and gold support mappings must never enter ordinary policy inputs. An oracle baseline must use a separate, explicitly named input path. Controller units generated from a question must not contain gold-derived answers or hints.

## 5. Output log: one record per action

Required fields: versions, `sample_id`, `trace_id`, `run_id`, `policy`, `seed`, `time_origin`, `clock`, `decision_time_s`, `action`, `text`, `evidence_snapshot_ids`, `output_start_time_s`, `output_end_time_s`, `claim_spans`, and `status`.

- `action` uses the five exact strings in `experiment_config.json`.
- `evidence_snapshot_ids` lists evidence supplied to the decision, not future arrivals.
- `Wait` uses an empty text string and null output times.
- `claim_spans` identifies atomic factual claims, their exact text, output times, and cited evidence IDs. It is empty when no factual claim is present. Generation need not supply gold unit matches; B's evaluator performs that mapping independently.
- Claim times can be null until alignment is available. Do not substitute decision times for spoken claim times.
- `status` is `ok` or `error`; preserve errors and incomplete runs.
- For audio, preserve raw stream timestamps as well as normalized timestamps in the adapter output.

The concrete claim-alignment method and simulated generation costs remain pending team decisions. Until agreed and implemented, log what is observed and leave unmeasured times null.

## 6. Completion and validation

An action named `Final Answer` does not by itself establish successful completion. Evaluation checks whether all necessary answer units have been correctly and supportably expressed, using evidence visible when each claim was output. Retractions and corrections must be retained for later scoring.

Minimum shared validation:

1. IDs and versions match across trace, gold, and output logs.
2. Evidence IDs resolve and event visibility times are ordered.
3. Every model snapshot excludes future evidence and all gold fields.
4. Gold dependencies reference valid units and contain no cycles.
5. Recorded claim times fall within output intervals when those intervals exist.
6. Unknown versions, malformed records, and missing measurements are reported explicitly.

B owns the interface and can proceed with debug data under v1. A provides feedback on policy inputs/actions; C provides feedback on baseline/audio logging. Resolve concrete integration failures as they arise and version incompatible changes. A/C adoption must be recorded only after it is observed. Unmeasurable times remain null; a null measurement cannot be used to report a timing metric.
