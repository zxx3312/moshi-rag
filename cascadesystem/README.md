# CascadeSystem

A conversational retrieval system that combines local speech recognition, Tinker
`openai/gpt-oss-120b`, Wikipedia search, evidence checks, and optional speech output.
It runs independently of `a_work`, Moshi, and the repository's evaluation datasets.

For a separate development evaluation on B Group's debug questions, see
[Debug20 evaluation](<../eval debug20/README.md>). It uses fixed B debug evidence
and B's unchanged scorer, keeping reference answers out of model input. The
runner also supports `--tts windows --play` for speech during the evaluation.

For targeted GPT-OSS-120B LoRA training, see [Judge training](training/README.md).
It adapts B's SFT train/dev data to this application's evidence contract and
routes only judgment/repair calls to a saved Tinker checkpoint. Other stages
use the configured base model; training is optional.

## 1. How it works

```text
Text / recording / microphone
             |
      Speech-to-text, if needed
             |
      Resolve follow-ups and corrections
             |
      Split the question into answer units and dependencies
             |
      Search Wikipedia for the relevant entities and facts
             |
      Check evidence, citations, exact quotes, and dependencies
             |
      Generate and verify an answer from supported facts
             |
      Display complete sentences -> optional TTS -> playback
```

The controller processes evidence as it arrives:

| Current state | Response |
|---|---|
| Work has started | Generate a short opening based on the question. |
| Search or verification is still running | Generate a progress message from the actual execution state. |
| Some answer units are supported | Answer those parts without waiting for every search. |
| All necessary units are supported | Complete the answer without repeating earlier parts. |
| Retrieval ends with unresolved necessary units and some evidence | Recheck them and their dependencies once, then answer supported parts and state any remaining gaps. |

Opening and progress generation run alongside the main pipeline. If generation
times out or fails its checks, the system uses a short fallback message.
Factual answers require retrieved evidence; missing facts do not fall back to model
knowledge. Verification uses the same LLM and can still make mistakes.

### Model input at each stage

| Stage | Input |
|---|---|
| Decomposition | The resolved question; no reference answers or evidence. |
| Plan review | The question and proposed plan, before retrieval; checks requested relations and unnecessary dependencies. |
| Evidence judgment | The question, generated units, and currently ingested evidence. |
| Answer generation | The selected, approved facts for this output. |
| Answer verification | Selected facts, their transitive dependencies, and cited visible evidence. |
| Opening/progress | The question and actual execution state; no permission to invent answers. |

The model does not receive every document at the start. In live mode, searches
finish asynchronously. In Debug20, the scheduler withholds future evidence.
Generation is scoped to selected facts rather than a new unrestricted answer
from every document.

Tinker opts into one additional question-only plan review. It checks ancestor
depth, missing comparison conclusions, unnecessary negative prerequisites for
named-candidate choices, and invented conditions such as "immediately before."
The returned plan must pass the strict schema and graph checks; an invalid
review is rejected. Legacy custom providers can opt in with
`requires_plan_review=True`. This adds one API call per turn and can increase
latency; it does not guarantee a semantically correct plan.

### Opening acknowledgments and progress

The controller decides when an opening or progress message is allowed; the API
generates and checks the wording alongside the main pipeline. `Backchannel` is
the code label for the opening acknowledgment. In ordinary conversation,
backchannels usually mean brief listener responses such as "uh-huh"; the
application's opening is closer to "I'll check that."

Progress becomes eligible after three seconds without output, subject to state
and output limits. It is not a phrase repeated automatically every three seconds.
Generation and verification share a six-second budget. The controller rechecks
state before release and discards stale messages. Failed or late drafts can use
short state-based fallback phrases. Events record `feedback_source` as `model`
or `fallback`, so a familiar phrase alone does not identify how it was produced.

| Setting | Default | Purpose |
|---|---:|---|
| `CASCADE_PROGRESS_S` | `3` | Idle interval before progress is eligible. |
| `CASCADE_FEEDBACK_TIMEOUT_S` | `6` | Combined feedback generation/checking budget. |

### Evidence and output validation

Model outputs are validated before use. Dependencies explicitly named by known
placeholders can be added locally only if the resulting plan passes all graph
checks. Other invalid plans get at most one model rewrite. Missing, duplicate, or
extra judgment IDs and invalid quotes share a single repair attempt per evidence
snapshot. Failed repairs remain rejected; citations, exact quotes, and dependency
requirements are not relaxed. Raw replies and validation details are logged before
rejection so malformed outputs remain diagnosable.

Unique whitespace-only quote differences can be restored to the original source
characters locally, with both forms logged. Omitted words, ellipses, case changes,
ambiguous repeated matches, and invisible sources are not repaired this way.
The strict exact-substring validator remains in force. Repair requests include
the already-visible cited sentences so the model can copy literal text.

Citation identity checks distinguish generic article types from different
namesakes: a redundant `(album)` suffix may match an unqualified article whose
lead explicitly identifies an album. A role-qualified person also needs role
context in the unit or its dependency chain. Geographic/year qualifiers,
different explicit qualifiers, and ambiguous pages remain blocked. Live search
keeps its separate strict entity resolution.

Output verification is scoped to the units selected for the current action.
A partial answer need not answer the whole question, and a final action need not
repeat facts already output. The verifier also receives the selected units'
transitive dependency facts and cited visible evidence. These are context only;
the generated draft may state only the selected facts. Tinker verification must
explicitly confirm `facts_valid` and account for exactly `output_unit_ids` via
`expressed_unit_ids`. A wording or unit-accounting failure uses a fact template;
the template still needs fact verification when generation itself was invalid.
Provider failures stop the run instead of releasing unchecked speech. Rejected
ancestors also invalidate their supported descendants. Verification replies and
draft/fact rejections are logged separately from spoken-output events.

After retrieval is exhausted, at most one additional judge call rechecks necessary
`UNRESOLVED` units and their dependency closure on the same ingested evidence.
It does not fetch more evidence or use model memory. A malformed review structure
is rejected. Tinker can repair an invalid quote contract once in the same snapshot;
this repair cannot change supported values/citations or promote unresolved units.
Custom providers opt in with `repairs_completion_quotes=True`. A genuine conflict
is not forced into an answer. Unrelated
units retain their validated state. This can add model latency and does not
guarantee a previously missed fact will be recovered. An evidence-backed negative
answer is `SUPPORTED` with a negative value; `CONTRADICTED` is not the label for
an ordinary "No" answer. Missing occupation information is not treated as proof
of a negative occupation.

Custom legacy model providers can retain the old verification reply contract.
Providers setting `requires_output_unit_ids=True` use the strict Tinker contract;
explicitly returned output-unit lists are checked for every provider.

Spoken answers use natural declarative sentences with a subject and a predicate.
Generation should not read internal tasks such as "Identify ..." or field/value
pairs aloud. For the strict Tinker contract, copied label/value drafts fall back
to complete fact sentences; missing information uses first-person uncertainty.
Approved values are preserved verbatim, without extra opinions, explanations,
or model-memory facts. The change adds no separate rewriting API call. Legacy
custom providers keep the original fallback format for compatibility. Formatting
cannot correct a wrongly decomposed relation or guarantee natural grammar for
every malformed description; grounding checks remain separate.

### Completion and the full response

`complete` means all necessary units in the system's own plan were supported and
their output accepted. `incomplete` means necessary units remained unresolved or
failed verification. `error` records an operational failure. These are internal
statuses, not independent comparisons with a reference answer.

`Partial Answer` speaks newly supported facts. `Final Answer` is the last output
action and may contain only the remaining facts or an uncertainty notice. Read
partial answers, corrections, and the final action in order for the full response.
Neither a final action nor `complete` guarantees correctness. A complete draft
is generated and verified before sentence output; LLM tokens are not streamed
directly to speech.

### Conversation and interruption

Conversation history helps resolve references such as "When did it open?" and
merge corrections or unfinished requests. Each new question is researched again;
previous answers are not treated as new evidence. Replies follow the question's
Chinese or English language unless `--language` overrides it.

Normal voice mode listens again after the answer finishes. With `--barge-in`,
capture continues during transcription, search, and playback. Speaking stops the
old answer, cancels its local task, and collects the correction or continuation
before starting a new evidence run. Only fully played sentences count as fully
heard in an interrupted turn. An HTTP request already sent may still finish remotely.

## 2. Setup and usage

Run every command below from the **repository root**, not from inside this folder.
The core requires Python 3.10+. Local faster-whisper uses a separate Python 3.12
environment. The playback examples below target Windows.

### Offline demo

```powershell
python -m cascadesystem --demo
```

This uses fictional data and scripted model/search providers, with no API calls.

### Configure Tinker

Create the local configuration file if it does not already exist:

```powershell
if (!(Test-Path cascadesystem/.env)) {
    Copy-Item cascadesystem/.env.example cascadesystem/.env
}
```

Edit `cascadesystem/.env` and set `TINKER_API_KEY`. The default connection is:

```dotenv
TINKER_API_KEY=your_key_here
CASCADE_BASE_URL=https://tinker.thinkingmachines.dev/services/tinker-prod/oai/api/v1
CASCADE_MODEL=openai/gpt-oss-120b
CASCADE_WIKI_LANGUAGE=en
```

Optional `CASCADE_JUDGE_MODEL=tinker://.../sampler_weights/...` selects a trained
judge; blank uses `CASCADE_MODEL`. `CASCADE_JUDGE_REASONING_EFFORT` defaults to
`low`. The training wrapper checks `best.json` without editing `.env`; per-call
logs record the actual model used.

The local `.env` is ignored by Git. Shell environment variables override its values.
Wikipedia search needs no API key. `CASCADE_WIKI_LANGUAGE` controls the source
language; it does not determine the language of the answer.

### Text questions and continuous chat

```powershell
# One question, with search queries and returned page titles.
python -m cascadesystem --question "Which city is the Eiffel Tower in?" --show-sources

# Continuous text input, with spoken replies.
python -m cascadesystem --chat --tts windows --play
```

Omit `--tts windows --play` for text-only output. With `--tts windows` alone,
the system saves WAV files without playing them. Windows TTS requires installed
voices for the requested language.

### Install local speech recognition

If `cascadesystem/.venv` is not already configured, create it with Python 3.12:

```powershell
py -3.12 -m venv cascadesystem/.venv
cascadesystem/.venv/Scripts/python.exe -m pip install -r cascadesystem/requirements-voice.lock.txt
python -m cascadesystem --prepare-asr --asr-model small
```

If `py -3.12` is unavailable, use the full path to a Python 3.12 executable instead.
The lock file contains the Windows/Python 3.12 dependency versions. Model files are
cached under `artifacts/models/`; normal recognition loads the local cache without
downloading. `--prepare-asr` explicitly downloads and loads the selected model.

The normal `python -m cascadesystem` command automatically launches the local voice
environment when needed. The multilingual `small` model runs on CPU with int8
computation and is reused across turns. Only transcribed text goes to Tinker.

### Microphone conversation and interruption

```powershell
# List input and output devices without opening the microphone.
python -m cascadesystem --speech-info

# Listen, answer, finish playback, then listen again.
python -m cascadesystem --listen --tts windows --play

# Keep listening and allow interruptions during an answer.
python -m cascadesystem --listen --barge-in --tts windows --play --show-sources
```

**Use a headset for barge-in.** There is no acoustic echo cancellation; speaker
output or sustained background noise can trigger an interruption. Barge-in requires
faster-whisper. Recognition still works on completed audio segments, rather than
streaming partial words directly into the LLM.

| Option | Purpose |
|---|---|
| `--language auto\|zh\|en` | Answer language; default follows the question. |
| `--asr-language zh` or `en` | Force recognition language; omit for automatic detection with faster-whisper. |
| `--input-device ID` | Select a microphone by the ID or name shown by `--speech-info`. |
| `--output-device ID` | Select the playback device in barge-in mode. |
| `--silence-seconds 1` | Silence that ends an utterance. |
| `--energy-threshold 0.015` | Audio energy threshold used to detect speech onset and silence. |
| `--barge-onset-seconds 0.18` | Sustained energy required to trigger an interruption. |
| `--continuation-seconds 0.6` | Extra time after transcription to collect a continuation. |
| `--max-utterance-seconds 30` | Maximum microphone utterance length; longer input is rejected. |
| `--history-turns 6` | Maximum conversation turns retained in context. |

### Session commands

| Action | Text command | Spoken command |
|---|---|---|
| Exit | `/exit` | `goodbye` or `退出对话` |
| Clear context | `/reset` | `清空上下文` |
| Show history | `/history` | — |
| Set language | `/language zh`, `/language en`, `/language auto` | `switch to Chinese`, `switch to English` |
| Pause an answer | — | `stop` or `等一下`, in barge-in mode |

After pausing, add your correction or ask to continue the previous question.
Chinese voice commands accept simplified and traditional characters.
`Ctrl+C` cancels the session. Clearing context does not delete saved logs.

### Recordings and alternative backends

```powershell
# Transcribe a recording, search, and answer.
python -m cascadesystem --audio "question.wav" --tts windows --play

# Transcribe only: no Tinker, search, or speech output.
python -m cascadesystem --transcribe "question.wav"

# Windows built-in recognition, without faster-whisper; no barge-in.
python -m cascadesystem --listen --asr-backend windows --asr-language en --tts windows --play

# An existing Whisper CLI for recorded input.
python -m cascadesystem --audio "question.wav" --asr-backend whisper --whisper "C:\tools\whisper.exe" --asr-model turbo

# An existing Piper executable and matching voice for speech output.
python -m cascadesystem --question "Where is Paris?" --tts piper --piper "C:\tools\piper.exe" --voice "C:\voices\en_US-lessac-medium.onnx" --play
```

Windows recognition needs the corresponding Windows speech language pack. Its
`--asr-language auto` uses the Windows interface language, not audio language
detection. `--min-confidence` applies only to that backend.

`--speech-info`, `--transcribe`, and `--prepare-asr` do not need a Tinker key.
Use `python -m cascadesystem --help` for the complete option list.

### Output and checks

Runs create a unique directory under `cascadesystem/artifacts/`; `--output PATH`
selects a new directory explicitly. Existing output directories are not overwritten.

| Output | Contents |
|---|---|
| `run.json` | Question, plan, evidence, judgments, model calls, answer events, and audio status. |
| `events.jsonl` | Ordered controller events and relative timestamps. |
| `audio_events.jsonl` | Audio readiness and playback start/finish events. |
| `audio/` | Generated WAV files and TTS text files where applicable. |
| `session.jsonl`, `history.json` | Session events and retained conversation history. |
| `turn-0001/`, etc. | Separate run files for each conversation turn. |
| `input/` | Captured audio segments and recognition results. |

"Text ready" measures when checked text is available. "Playback start" measures
when the playback API starts, after synthesis and queue waiting; it is not an acoustic
measurement. Turn timestamps start when question text is ready; ASR time is recorded
separately. Logs and recordings remain local and are ignored by Git.

```powershell
python -m unittest discover -s cascadesystem/tests -v
```

## 3. Files and responsibilities

| File | Contents and purpose |
|---|---|
| [`__init__.py`](__init__.py) | Package definition. |
| [`__main__.py`](__main__.py) | CLI modes, voice-environment launch, turn execution, session startup, and output files. |
| [`config.py`](config.py) | Defaults, allowed `.env` settings, model connection, timeouts, and resource budgets. |
| [`training/README.md`](training/README.md) | Commands, data limitations, dev comparison, checkpoints and detailed training file map. |
| [`training/data.py`](training/data.py) | Fixed B SFT-only conversion, visible quote targets and split/hash checks. |
| [`training/sdk.py`](training/sdk.py) | Optional SDK boundary and official GPT-OSS Harmony renderer. |
| [`training/engine.py`](training/engine.py) | LoRA epochs, dev-loss selection, optimizer-state resume and judge dev metrics. |
| [`training/__main__.py`](training/__main__.py) | Training CLI and child-process judge checkpoint wrapper. |
| [`training/__init__.py`](training/__init__.py) | Training package definition without import side effects. |
| [`training/requirements.txt`](training/requirements.txt) | Pinned SDK and cookbook for a separate environment. |
| [`tests/test_lora_training.py`](tests/test_lora_training.py) | Fictional data, resume, checkpoint selection and judge-only routing regressions. |
| [`tests/test_lora_sdk.py`](tests/test_lora_sdk.py) | Fake SDK masks, optimizer submission, restoration and completion parsing. |
| [`tests/test_checkpoint_paths.py`](tests/test_checkpoint_paths.py) | SDK checkpoint run-ID suffixes and save-to-inference regressions. |
| [`.env.example`](.env.example) | Template for local Tinker and Wikipedia settings. |
| `.env` | Local API key and overrides; not committed. |
| [`transport.py`](transport.py) | Bounded HTTP/JSON requests and error handling without logging authentication data. |
| [`llm.py`](llm.py) | Tinker client; decomposition, evidence judgment, answer generation, and verification prompts; call timing. |
| [`models.py`](models.py) | Answer-unit dependencies, evidence and judgment structures, citation checks, and exact-quote validation. |
| [`search.py`](search.py) | Replaceable search interface and Wikipedia implementation, including entity resolution and passage selection. |
| [`controller.py`](controller.py) | Concurrent searches or an optional scheduled-evidence stream, partial/final answers, missing-information handling, and corrections. |
| [`protocol.py`](protocol.py) | Explicit-placeholder dependency completion, one-attempt plan/judge repairs, strict revalidation, and raw-reply diagnostics. |
| [`tests/test_review_fixes.py`](tests/test_review_fixes.py) | Fictional regressions for question-only plan review, bounded quote repairs, entity types/namesakes, and literal Yes/No wording. |
| [`grounding.py`](grounding.py) | Transitive visible-dependency verification context and exact selected-output-unit accounting. |
| [`wording.py`](wording.py) | Complete fact-sentence fallbacks, copied-label detection, and natural missing-information notices without changing approved values. |
| [`feedback.py`](feedback.py) | Dynamic opening/progress messages, state checks, time budgets, and fallback phrases. |
| [`conversation.py`](conversation.py) | Bounded history, follow-up resolution, unfinished-request merging, and session commands. |
| [`presentation.py`](presentation.py) | Chinese/English detection, sentence splitting, and terminal time labels. |
| [`audio.py`](audio.py) | Sequential TTS queue, Windows/Piper synthesis, playback integration, cancellation, and Whisper CLI adapter. |
| [`whisper_input.py`](whisper_input.py) | Local faster-whisper model loading/reuse, microphone endpoint detection, and recording transcription. |
| [`speech_input.py`](speech_input.py) | Windows recognition wrapper, language selection, confidence checks, and process cleanup. |
| [`windows_asr.ps1`](windows_asr.ps1) | Windows dictation from a microphone or WAV file and installed-recognizer inspection. |
| [`windows_tts.ps1`](windows_tts.ps1) | Select an installed Chinese/English voice and synthesize a WAV file. |
| [`live_audio.py`](live_audio.py) | Continuous microphone capture, a separate ASR worker, and interruptible sounddevice playback. |
| [`duplex.py`](duplex.py) | Barge-in session loop, old-task invalidation, continuation collection, and interruption-aware history. |
| [`demo.py`](demo.py) | Fictional question and scripted model/search providers for the offline demo. |
| [`requirements-voice.txt`](requirements-voice.txt) | Direct optional ASR/audio dependencies with compatibility pins. |
| [`requirements-voice.lock.txt`](requirements-voice.lock.txt) | Full dependency versions for the Windows/Python 3.12 voice environment. |
| [`.gitignore`](.gitignore) | Excludes local keys, voice environment, generated artifacts, and bytecode. |
| [`tests/__init__.py`](tests/__init__.py) | Test package definition. |
| [`tests/test_system.py`](tests/test_system.py) | Core controller, provider adapters, configuration, citations, dependencies, and failure handling. |
| [`tests/test_entity.py`](tests/test_entity.py) | Entity identity, redirects/disambiguation, namesakes, and final fact rejection. |
| [`tests/test_feedback.py`](tests/test_feedback.py) | Dynamic feedback, state consistency, timeouts, and stale-message cancellation. |
| [`tests/test_presentation.py`](tests/test_presentation.py) | Bilingual replies, sentence splitting, speech queue ordering, and timing labels. |
| [`tests/test_conversation.py`](tests/test_conversation.py) | History limits, follow-ups, clarification, session loops, and language/exit commands. |
| [`tests/test_voice.py`](tests/test_voice.py) | Local ASR reuse, capture boundaries, silence/rejection cases, and optional-environment routing. |
| [`tests/test_barge_in.py`](tests/test_barge_in.py) | Concurrent capture, interruption, stale-result rejection, continuation merging, and playback cancellation. |
| [`tests/test_protocol.py`](tests/test_protocol.py) | Bounded structural repairs, preserved evidence snapshots, dependency safety, and refusal after an unsuccessful repair. |
| [`tests/test_grounding.py`](tests/test_grounding.py) | Fictional regressions for partial/final scope, bridge context, negative answers, draft accounting, failed verification, and a single completion recheck. |
| [`tests/test_wording.py`](tests/test_wording.py) | Bilingual sentence wording, preserved values, time/title punctuation, and verified natural fallback output. |
