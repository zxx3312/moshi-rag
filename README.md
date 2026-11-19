# CascadeSystem: Evidence-Aware Spoken Retrieval

This fork contains a standalone conversational retrieval prototype for
**Computation-Aware Turn-Taking for Full-Duplex Spoken Agents**.

The current application uses Tinker `openai/gpt-oss-120b`, Wikipedia retrieval,
evidence checks, and optional local speech recognition and synthesis. A controller
decides when to acknowledge a question, wait, give a partial answer, finish, or
state that information could not be confirmed.

The application runs independently of Moshi. Original MoshiRAG code remains in
`moshi/`, `rust/`, and `client/`; its instructions are preserved in
[Original MoshiRAG documentation](docs/upstream_moshirag_README.md).

## Guides

| Guide | Contents |
|---|---|
| [CascadeSystem](cascadesystem/README.md) | Application flow, configuration, text/voice conversations, interruption, outputs, and file reference. |
| [Debug20 evaluation](<eval debug20/README.md>) | B's fixed debug evidence, original B scoring, direct WAV generation, and playback. |
| [GPT+LoRA final 900](<eval gpt900/README.md>) | Explicit final-run entry for the revised 300-question/900-trace set, with the saved GPT judge checkpoint and B scorer. |
| [GPT-OSS judge LoRA](cascadesystem/training/README.md) | SFT data preparation, Tinker training/dev comparison, and running a saved judge checkpoint. |
| [Experiment specification](docs/experiment_spec.md) | Research definitions and pending decisions, separate from prototype features. |
| [Work plan](docs/plan.md) | Progress, validation, source versions, and run records. |
| [Repository rules](CLAUDE.md) / [agent entry](AGENTS.md) | Data isolation and contribution instructions. |

## Quick start

Run commands from the **repository root**. The core requires Python 3.10+.
The Windows examples use installed system voices. Microphone recognition has
separate optional dependencies described in the application guide.

Try a fictional example without API calls:

```powershell
python -m cascadesystem --demo
```

Create the local API configuration only if it does not already exist:

```powershell
if (!(Test-Path cascadesystem/.env)) {
    Copy-Item cascadesystem/.env.example cascadesystem/.env
}
```

Set `TINKER_API_KEY` in `cascadesystem/.env`. The default model is
`openai/gpt-oss-120b`. Keep the key local; the file is ignored by Git.
Existing environment variables override the local file.

Ask a question using live Wikipedia and hear the reply:

```powershell
python -m cascadesystem --question "Which city is the Eiffel Tower in, and when did it open?" --tts windows --play --show-sources
```

Continuous text conversation with spoken replies:

```powershell
python -m cascadesystem --chat --tts windows --play
```

After installing the optional local ASR environment, use a microphone:

```powershell
python -m cascadesystem --listen --tts windows --play
python -m cascadesystem --listen --barge-in --tts windows --play
```

Use a headset for interruption mode; there is no acoustic echo cancellation.
See the [application guide](cascadesystem/README.md) for setup, device selection,
Chinese/English recognition, recordings, and session commands.

## What happens to a question

```text
Text / microphone / recording
        |
Optional ASR -> resolve follow-ups -> question-only decomposition + plan review
        |
Visible evidence -> judge support, citations, quotes, and dependencies
        |
Select supported facts not already output
        |
Generate natural sentences -> verify the selected facts and dependency context
        |
Text output -> optional sentence TTS and playback
```

When retrieval ends with necessary units still unresolved, the controller can
make one final evidence-only recheck. A failed recheck does not authorize an
answer from model memory. Correctly supported negative answers use
`SUPPORTED`; `CONTRADICTED` is not the ordinary label for an answer of "No."

Each API stage has a different input:

| Stage | Input |
|---|---|
| Decomposition | The question, without gold answers or evidence. |
| Plan review | The question and proposed units; checks relation depth, dependencies, and coverage before retrieval. |
| Evidence judgment | The question, generated units, and currently ingested evidence. |
| Answer generation | The selected, approved facts for this output. |
| Answer verification | Those facts plus their visible dependency evidence. |
| Waiting response | The question and the current execution state. |

Reading evidence does not guarantee that the model interprets it correctly.
The system validates structure, visible citations, exact quotes, and dependencies,
but semantic support and question interpretation still depend on model judgment.
Tinker performs one extra question-only plan review per turn. The final semantic
recheck can also repair a rejected quote once using the same visible sources,
without changing supported values or adding new facts. These checks add API
latency; their effect on real answers needs a fresh run.

### Waiting responses

The controller decides **when** to request a response and **what kind** is allowed.
The API supplies the wording.

- `Backchannel` is the code label for an opening acknowledgment, such as
  "I'll look up the launch and return dates." In conversation terminology this
  is closer to an acknowledgment than a listener's brief "uh-huh."
- `Progress` describes the actual processing state. It can be requested after
  about three seconds without output; it is not spoken automatically every
  three seconds.
- Generation and checking run alongside the main pipeline, with a default
  six-second combined budget. Unsafe, stale, failed, or late drafts are rejected
  or replaced with short state-based fallback phrases.

Waiting responses cannot announce unconfirmed answers or invented discoveries.
See [feedback.py](cascadesystem/feedback.py) and
[controller.py](cascadesystem/controller.py).

### Partial, final, and complete

| Term | Meaning |
|---|---|
| `Partial Answer` | Speak newly supported facts while other information is pending. |
| `Final Answer` | The last output action; it can supply only the remaining part or state unresolved gaps. |
| `complete` | All necessary units in the system's own plan were supported and their output was accepted. |
| `incomplete` | Some necessary units remained unsupported or failed verification when processing ended. |
| `error` | An operational or provider failure prevented normal completion. |

A final action is not necessarily a standalone summary. Read partial answers,
corrections, and the final answer together to reconstruct the response.
A `complete` status is not an independently checked correctness score.

Natural sentences are produced during the run, using the existing generation
stage and conservative fallback wording. There is no extra post-run polishing
API call. The current draft must finish generation and verification before it
is emitted; this is not token-by-token audio streaming.

## Debug20: fixed evidence and direct audio

There are two distinct execution modes:

| Mode | Evidence source | Purpose |
|---|---|---|
| `python -m cascadesystem` | Live Wikipedia retrieval | Exercise the application, including external search. |
| `eval debug20/run.py` | B's frozen debug trace | Check behavior on controlled evidence and score with B's evaluator. |

Debug20 uses 20 unique questions with three existing evidence schedules:

| Schedule | First batch | Second batch |
|---|---:|---:|
| `immediate` | All at 0 seconds | None |
| `short` | 1 second | 3 seconds |
| `long` | 2 seconds | 8 seconds |

These are evidence availability times, not guaranteed speaking times.
Future evidence stays with the scheduler until it is due. B's reference answers
are used only for scoring.

On a fresh checkout, prepare the debug inputs once. Skip this if the default
input directory already exists:

```powershell
python ".\eval debug20\run.py" prepare --ref origin/b-data-eval
```

Run the first question in the long condition and hear each sentence as it is ready:

```powershell
python ".\eval debug20\run.py" run --schedule long --limit 1 --tts windows --play
```

Generate WAVs for all 20 questions in all three conditions, without automatic playback:

```powershell
python ".\eval debug20\run.py" run --schedule all --tts windows
```

Add `--play` to hear the batch. `--limit` counts unique questions:
`--schedule all --limit 1` selects three runs of the first question.

Each invocation creates a new directory under `eval debug20/artifacts/runs/`.
Per-question audio is saved as:

```text
RUN/
  samples/0001/audio/response.wav
  samples/0001/audio/responses.txt
  samples/0001/audio/audio_index.json
  audio_summary.json
  policy_log.jsonl
  b_eval/summary.md
```

Speech synthesis runs alongside model processing. Each question's audio queue
finishes before the next question starts. Without playback, the combined WAV is
a preview arranged at synthesis-ready times. JSON remains as background scoring
and provenance data; the console shows readable text and paths.

### Scoring saved results

The runner automatically applies B's unchanged scorer. Default scoring requires
checked claim-to-gold mappings; unmatched claims enter a review queue.

For a separate, approximate unique-value diagnostic without new API calls:

```powershell
python ".\eval debug20\run.py" score --run "RUN_DIRECTORY" --allow-value-match --output "NEW_SCORE_DIRECTORY"
```

The diagnostic checks expected values/aliases and B's support rules. It is not
embedding similarity or independent semantic grading. Means over a scored subset
are not overall accuracy. B currently cannot fully score retractions, and
unresolved mappings keep affected scores unknown. TTS files do not automatically
provide atomic claim alignment; formal speech-time metrics remain null.
See the [evaluation guide](<eval debug20/README.md>) for checked mappings and limits.

## Files and outputs

| Location | Role |
|---|---|
| [cascadesystem/](cascadesystem/README.md) | Controller, model prompts/client, live search, grounding, waiting responses, natural wording, conversation, ASR/TTS, and tests. |
| [eval debug20/](<eval debug20/README.md>) | Debug trace preparation, scheduling, audio generation, B log conversion, scoring, and tests. |
| [a_work/](a_work/README.md) | Separate research-method implementation and historical development notes. |
| [docs/](docs/plan.md) | Shared research specification, work plan, and preserved upstream guide. |
| `moshi/`, `rust/`, `client/` | Original MoshiRAG implementations and client. |

The two component guides include per-file responsibility tables.
The standalone application's `cascadesystem/artifacts/` contains run/session
logs and per-sentence WAVs. Debug20 additionally provides a combined
`audio/response.wav` per trace. Existing runs are retained; source changes require
a fresh run rather than resuming a different snapshot.

Development uses debug data. Reserved evaluation questions and their derived
answers/evidence are excluded from development. Runtime units and evidence
judgments never receive B's gold answers.

## Offline checks

```powershell
python -m unittest discover -s cascadesystem/tests
python -m unittest discover -s ".\eval debug20\tests"
```

These tests use fictional inputs and model/audio fixtures; they do not call
Tinker or access the reserved split. Passing them does not establish real-world
answer accuracy, microphone quality, or end-to-end spoken latency.

## Upstream licensing

See the preserved [MoshiRAG licensing information](docs/upstream_moshirag_README.md#license)
for the upstream code, model weights, and dependencies.
