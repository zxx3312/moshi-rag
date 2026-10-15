# Existing Log Analysis

## 1. Purpose and execution

This step checks that the existing pilot logs can be analyzed and that their timing fields can be interpreted. No new model inference was performed in this step.

The existing pilot logs were successfully analyzed. Both the 0-second and 8-second delay conditions contain 12 successful runs. A successful run indicates that execution completed without errors; it does not imply that the answer was correct.

| Item | Description |
|---|---|
| Repository commit | 021927e39e40cad2c42fa0541d8631375c236543 |
| Python version | Python 3.11.11 |
| Repository branch used for the guide | `exp/async-retrieval-latency` |
| Analysis script | `experiments/async_retrieval_latency/analysis/analyze_latency.py` |
| Working data directory | `b_work/pilot_review` |
| Summary output | `b_work/pilot_review/analysis/summary_by_delay.csv` |
| Inspected sample | `sqa_1009`, 8-second delay condition |
| Delay mechanism | Fixed reference text with injection delayed on the model-step clock |

The analysis command was run from the repository root:

```bash
python3 experiments/async_retrieval_latency/analysis/analyze_latency.py b_work/pilot_review
```

Record the actual working environment using:

```bash
git rev-parse HEAD
python3 --version
```

The original pilot was generated on a Tesla T4 using the `t4_low_memory` variant. Those settings describe the original inference run, not the environment used to analyze its logs.

## 2. Summary observations

Each row in the summary CSV represents one delay condition. The `.n` suffix gives the number of valid observations for a metric, `.mean` gives its mean, `.median` gives its median, and `.rate` gives a proportion.

| Metric | 0-second condition | 8-second condition |
|---|---:|---:|
| Runs / successful executions | 12 / 12 | 12 / 12 |
| Mean trigger-to-injection time | 0.48 s | 8.48 s |
| Mean response-onset latency | 0.20 s | 0.20 s |
| Mean speech duration between trigger and injection | 0.40 s | 6.7067 s |
| Mean word count between trigger and injection | 1 | 20 |
| Repeated-filler heuristic rate | 0% | 25% |
| Runs with a detected answer-string match | 9 / 12 | 0 / 12 |

The model started speaking quickly in both conditions. With the longer delay, it produced more speech before reference injection. Whether that speech was useful or supported requires inspection beyond these aggregate metrics.

The complete pilot contains 31 runs, including small intermediate-delay groups. These are not 31 independent questions. The 1-, 2-, 3-, and 5-second groups contain only one or two runs each and should not be treated as equally sized comparisons.

## 3. Timing definitions

The model processes 12.5 steps per second, so each step represents 0.08 seconds:

```text
Time in seconds = step / 12.5
```

Raw event timestamps are measured from the beginning of the audio stream. Response latencies are calculated relative to the estimated end of user speech. In the inspected sample, the user-speech end was estimated from audio energy.

| Field | Meaning | Inspected value |
|---|---|---:|
| `user_end_time` | Estimated end of user speech | 3.44 s |
| `input_end_time` | End of the input audio, including any trailing silence | 4.56 s |
| `trigger_step` | Step at which retrieval was triggered | 46 → 3.68 s |
| `request_step` | Step at which the request was issued | 52 → 4.16 s |
| `reference_received_step` | Step at which the experiment program received the reference | 52 → 4.16 s |
| `available_step` | Scheduled step at which reference injection became eligible | 152 → 12.16 s |
| `injection_step` | Actual start of reference injection | 152 → 12.16 s |
| `injection_num_steps` | Number of steps used for injection | 4 → 0.32 s |
| `reference_ingestion_end_time` | End of reference injection | 12.48 s |

The reference was received by the experiment program before it was injected into the model. Holding the reference in the scheduler does not mean the model already has access to it.

```text
Trigger to request:
(52 - 46) / 12.5 = 0.48 seconds

Request to scheduled availability:
(152 - 52) / 12.5 = 8.00 seconds

Retrieval trigger to injection:
12.16 - 3.68 = 8.48 seconds

End of user speech to injection:
12.16 - 3.44 = 8.72 seconds

End of injection:
(152 + 4) / 12.5 = 12.48 seconds
```

`stt_wait_steps=6` accounts for the six-step interval between trigger and request. `latency_clock="model_steps"` indicates that the controlled delay follows the model-step clock. `backend_wait_wall_s=0.0` means no additional backend wait was recorded at injection; it does not mean the configured delay was zero.

## 4. Inspected case: sqa_1009

**Question:** Which commune in France is The Pont Serme located in?

**Reference:** The Pont Serme is located in the French commune of Coursan.

**Expected answer:** Coursan.

**Model transcript:**

> Oh, that's a good question. It's in the south of France, nestled in the Pyrenees mountains. Is there anything else I can help with?

| Event | Stream time | Time relative to user-speech end |
|---|---:|---:|
| User finished speaking | 3.44 s | 0.00 s |
| Assistant first audible output | 3.68 s | 0.24 s |
| Assistant first text | 3.76 s | 0.32 s |
| Last audible output ended | 11.68 s | 8.24 s |
| Reference injection started | 12.16 s | 8.72 s |
| Reference injection ended | 12.48 s | 9.04 s |

The model started speaking 0.24 seconds after the user finished. It produced a general location description and a closing question, but did not mention Coursan. Its last audible output ended 0.48 seconds before reference injection began. No additional text or audible speech was recorded after injection.

The geographic statements were produced before the current reference was injected. The log therefore does not establish retrieval support for those statements. Their factual correctness would require a separate check.

This case illustrates that a fast response onset can occur without a useful, evidence-grounded answer. It also motivates inspecting whether a system continues or updates its answer after delayed evidence arrives.

Related files, relative to `b_work/pilot_review`:

- Trace: `traces/sqa_1009__d8s__s42424242.json`
- Model audio: `audio/sqa_1009__d8s__s42424242_model.wav`
- Stereo audio: `audio/sqa_1009__d8s__s42424242_stereo.wav`

## 5. Interpretation limits

- The 8-second condition simulates delayed reference availability. It is not a measurement of a real search service's latency.
- `status="ok"` describes successful execution, not answer correctness. `stop_reason="tail_silence"` identifies the stopping condition, not task success.
- `first_informative_latency_s` uses answer-string matching. A missing value means no answer match was detected; it does not represent a latency of zero.
- `answer_mentioned_before_injection=null` is undefined when no answer match is detected. It should not be converted silently to `false`.
- The answer-string heuristic cannot directly replace evidence-grounded claim evaluation or the proposed time-to-first-grounded-information metric.
- `response_end_time` records the end of audible output, not the time at which a correct, complete answer was delivered.
- Filler-pattern matches may overlap. For example, `good question` and `that s a good question` can match the same phrase, so the total does not necessarily count distinct filler expressions.
- `wall_elapsed_s` is computation time in the original run environment. It should not be substituted for stream-time response latency.
- This single case supports a diagnostic observation, not a conclusion about all samples or the effectiveness of the proposed policy.
