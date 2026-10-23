# Shared Data and Log Interface — B Group v1.1

Status: B GROUP INTERFACE v1.1 FOR INTEGRATION. B defines this common interface for data preparation and evaluation. A and C should use it for integration and report specific incompatibilities. Their feedback is not a prerequisite for B to start the debug data pipeline. This document does not claim that A/C have reviewed it or that the interface is already implemented in the repository.

v1.1 adds answer-unit construction rules from A's feedback (`a_work/unit_schema.md` v0.1 draft, branch `a-prompt-judge`) and two optional gold fields. The changes are backward compatible, so `schema_version` remains `1.0`. See Section 7 for the change log.

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

### 4.1 Optional gold fields (v1.1)

| Field | Type | Meaning |
|---|---|---|
| `aliases` | list of strings | Other accepted surface forms of `expected_answer`, e.g. `["Roger Thomas Staubach"]`. Defaults to `[]`. |
| `by_omission` | boolean | `true` when the unit is a negative claim supported only by omission from a defining description (Exception 2 in `labeling_guide.md` Section 1.1). Defaults to `false`. Evaluation reports these units separately. |

### 4.2 Support-set semantics

- `support_sets` lists only evidence that directly supports this unit. Support for earlier hops is expressed through `depends_on`, not repeated.
- A unit is supported at time `t` when at least one inner set is fully visible and every unit in `depends_on` is supported.
- `[[]]` means no additional evidence is needed: the unit is supported as soon as all its dependencies are supported. Use it only for comparison conclusion units (Section 4.3), which must have a nonempty `depends_on`.
- `[]` means no evidence can support the unit. Do not use it for answerable units.
- Alternative evidence found during review, including distractor sentences, is added as extra inner sets.

### 4.3 Unit construction by question type

Each unit is one fact that can be stated in one sentence and supported by one or a few evidence sentences. Usually 1–5 units per question.

| Question type | Units | `necessary` | `depends_on` |
|---|---|---|---|
| Single answer | One unit | `true` | none |
| Bridge / compositional / inference | One unit per hop | Intermediate hops `false`; final hop `true` | Each hop depends on the previous hop |
| Comparison (including yes/no) | One fact unit per compared entity, plus one conclusion unit | Fact units `false`; conclusion `true` | Conclusion depends on all fact units; conclusion `support_sets` is `[[]]` |
| Bridge comparison | Bridge hops per entity, then one conclusion unit | Conclusion `true`; all others `false` | As above |
| Multipart | One unit per part the user asked | All `true` | none |

- If the question explicitly asks for an intermediate hop ("Who directed X, and where was he born?"), treat it as multipart: that hop is `necessary: true`.
- `necessary` only decides completion (Section 6). Every unit, including `necessary: false`, counts as useful grounded information when it is stated correctly with visible support. This affects time-to-first-grounded-information metrics.

Comparison example (2Wiki Q05):

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "sample_id": "2wikimultihopqa_39751c8a08d811ebbd9aac1f6bf848b6",
  "units": [
    {"unit_id": "u1", "description": "birth date of Mark Gurr", "necessary": false,
     "expected_answer": "February 18, 1966", "depends_on": [], "support_sets": [["e1"]]},
    {"unit_id": "u2", "description": "birth date of William Eythe", "necessary": false,
     "expected_answer": "April 7, 1918", "depends_on": [], "support_sets": [["e2"]]},
    {"unit_id": "u3", "description": "who was born later", "necessary": true,
     "expected_answer": "Mark Gurr", "depends_on": ["u1", "u2"], "support_sets": [[]]}
  ]
}
```

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
7. `support_sets` equal to `[[]]` appears only on units with a nonempty `depends_on`; `[]` does not appear on answerable units.
8. Every question has at least one `necessary: true` unit.
9. `by_omission: true` units are reported separately in evaluation.

B owns the interface and can proceed with debug data under v1. A provides feedback on policy inputs/actions; C provides feedback on baseline/audio logging. Resolve concrete integration failures as they arise and version incompatible changes. A/C adoption must be recorded only after it is observed. Unmeasurable times remain null; a null measurement cannot be used to report a timing metric.

## 7. Change log

| Version | Date | Change |
|---|---|---|
| v1 | 2026-10-15 | Initial interface. |
| v1.1 | 2026-10-23 | Added optional gold fields `aliases` and `by_omission` (4.1), support-set semantics including `[[]]` (4.2), unit construction rules by question type from A's `unit_schema.md` v0.1 draft (4.3), and validation checks 7–9. No required field changed. |
