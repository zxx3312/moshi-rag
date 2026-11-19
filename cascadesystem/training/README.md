# GPT-OSS-120B evidence-judge LoRA

For the revised final 300-question/900-trace set, use the separate
[GPT+LoRA final runner](<../../eval gpt900/README.md>). It selects the saved judge
checkpoint, retains this application's prompts/controller and original B scoring,
and requires explicit `--final-run`. The Debug20 entry remains development-only.

Train a LoRA adapter on Tinker for the **evidence judgment** stage. It learns
supported/unknown units, answer values, visible citations, literal quotes and
short reasons. A snapshot can support one part while another stays unresolved.

Decomposition, plan review, natural answer wording, verification and progress
messages still use the configured base model. Search, dependency checks, quote
validation and partial-answer scheduling remain application code. This does not
train the whole spoken pipeline or change the research specification.

Training and dev prediction use Tinker's remote service and your existing
`TINKER_API_KEY` in `cascadesystem/.env`. Your PC downloads packages and the
tokenizer, not 120B model weights. Ordinary checkpoint inference uses the
application's OpenAI-compatible HTTP client.

## Commands

Use the repository on `a-cascade`. Steps 1-5 train in **WSL Ubuntu/Linux**;
step 6 runs the application in Windows PowerShell. Choose new output names if
the example directories already exist; old results are preserved.

The pinned official Cookbook requires `tml-renderers`, whose
[supported platforms are Linux and macOS](https://tinker-docs.thinkingmachines.ai/cookbook/inkling/tml-renderers/).
Native Windows `train`/`evaluate` therefore stop early with WSL instructions.
Windows `prepare`, `inspect`, checkpoint `run` and speech modes do not need it.

### 1. Install a separate training environment

If WSL Ubuntu is not installed, run this yourself in administrator PowerShell,
restart if Windows requests it, then complete Ubuntu's username setup:

```powershell
wsl --install -d Ubuntu-24.04
wsl
```

If Ubuntu is already installed, open it with `wsl` instead. In the **Ubuntu
terminal**, use its Python 3.12 and keep the Windows speech environment separate:

```bash
cd /mnt/d/UIUC/CS546/moshi-rag
sudo apt update
sudo apt install -y python3.12-venv python3-pip-whl git
/usr/bin/python3.12 -m venv ~/.venvs/moshi-cascade-312
~/.venvs/moshi-cascade-312/bin/python -m pip --version
~/.venvs/moshi-cascade-312/bin/python -m pip install -r cascadesystem/training/requirements.txt
```

Keep this environment on WSL's Linux filesystem, while source code and run
outputs stay in the existing repository. Microsoft recommends the Linux
filesystem for Linux-tool workloads, especially dependency installation:
[WSL filesystems](https://learn.microsoft.com/en-us/windows/wsl/filesystems).
Do not copy an existing Windows environment into WSL.

If environment creation fails at `ensurepip`, the short exception alone does
not identify the underlying cause. On Ubuntu 24.04 with `/usr/bin/python3.12`,
repair its venv/wheel packages and retry the Linux-home environment:

```bash
sudo apt update
sudo apt install --reinstall -y python3.12-venv python3-pip-whl
/usr/bin/python3.12 -m venv ~/.venvs/moshi-cascade-312
~/.venvs/moshi-cascade-312/bin/python -m pip --version
```

If that still fails, expose the actual pip bootstrap error with:

```bash
~/.venvs/moshi-cascade-312/bin/python -m ensurepip --upgrade --default-pip
```

Retain its complete output for diagnosis. A failed earlier environment under
`cascadesystem/training/.venv` can stay in place; the commands below do not use it.
The assistant has not executed these repair/install commands in your WSL session.

Requirements pin Tinker 0.39.1 and an official cookbook commit for the GPT-OSS
Harmony renderer. No SDK is required for `prepare`, `inspect`, or `run`.
The first `train`/`evaluate` command can download the tokenizer.

### 2. Prepare and inspect the data

Data is already prepared in the current workspace. This guard also works on a
fresh checkout whose Git database contains the fixed B commit:

```bash
if [ ! -f cascadesystem/artifacts/training/data/manifest.json ]; then
    ~/.venvs/moshi-cascade-312/bin/python -m cascadesystem.training prepare
fi
~/.venvs/moshi-cascade-312/bin/python -m cascadesystem.training inspect
```

Preparation reads five explicit SFT paths from B commit
`ea390574eadd301354d5de46f0d28d328cca5bad`; it never checks out B's tree.
If this commit is unavailable locally, run `git fetch origin b-data-eval` first.

### 3. Check remote training with a small run

```bash
~/.venvs/moshi-cascade-312/bin/python -m cascadesystem.training train --smoke --output cascadesystem/artifacts/training/runs/smoke-v1
```

Smoke uses at most two batches of eight train snapshots, four dev snapshots and
one epoch, saving both training state and a sampling checkpoint. It checks
remote setup/saving, not quality. Keep it separate from the full training run.

An earlier version rejected valid SDK paths whose run IDs contain `:train:0`
with `Expected a Tinker sampler_weights checkpoint path`. This local validation
bug is fixed. If `smoke-v1` failed this way, keep that directory and run a new
`--smoke --output cascadesystem/artifacts/training/runs/smoke-v2` instead.
Do not resume across this code change: resume intentionally requires the same
source hash. A successful smoke ends with an epoch dev loss and `Best checkpoint:`.
Two printed step losses alone do not establish successful saving or inference.

Per-epoch optimizer steps equal `ceil(kept_train_snapshots / batch_size)`.
Smoke normally keeps 16 snapshots at batch size 8, giving 2 steps. Full training
has at most `ceil(1900 / 8) = 238` steps per epoch with this prepared dataset;
token-length exclusions can reduce that count. Dev forward batches do not
increment the printed optimizer-step counter.

### 4. Train

```bash
~/.venvs/moshi-cascade-312/bin/python -m cascadesystem.training train --epochs 3 --batch-size 8 --rank 16 --lr 0.0001 --output cascadesystem/artifacts/training/runs/gpt120-judge-v1
```

Defaults: `openai/gpt-oss-120b`, seed 42, low reasoning renderer, at most 24,576
tokens per full example and 4,096 supervised target tokens. Only the last
assistant answer contributes to loss. Overlong examples are excluded with
counts/indices recorded; never silently truncated. These are prototype starting
parameters, not a tuned or formally approved research recipe.

Each completed epoch saves dev token loss and two checkpoint paths. The lowest
dev loss selects `best.json`; that does not prove higher factual accuracy.
After a failure with saved state, explicitly resume using the same options:

```bash
~/.venvs/moshi-cascade-312/bin/python -m cascadesystem.training train --epochs 3 --batch-size 8 --rank 16 --lr 0.0001 --output cascadesystem/artifacts/training/runs/gpt120-judge-v1 --resume
```

Resume restores weights **and optimizer state** from the last completed epoch;
any partial epoch is repeated. Code, SDK versions, data and settings must match.
Failed attempts/logs are retained. An epoch-zero state permits restarting a
failed first epoch. If no state was saved, choose a new output directory.

### 5. Compare base and LoRA on the same SFT dev snapshots

```bash
~/.venvs/moshi-cascade-312/bin/python -m cascadesystem.training evaluate --base --output cascadesystem/artifacts/training/dev-base-v1
~/.venvs/moshi-cascade-312/bin/python -m cascadesystem.training evaluate --run cascadesystem/artifacts/training/runs/gpt120-judge-v1 --output cascadesystem/artifacts/training/dev-lora-v1
```

For a smaller check, add the same `--limit 20` to both commands. This selects
20 snapshots, not 20 independent questions or the B debug20 dataset.
`summary.md`/`summary.json` report unit label agreement, false support on
unsupported targets, missed supported units, and value exact match when both
labels are supported. Invalid replies count as invalid/missed predictions;
fatal SDK errors stop the command and retain predictions already saved.

Unprefixed metrics use judgments after application validation. The report also
includes raw label agreement/false support and counts rejected supported units,
so citation/dependency rejection does not hide the model's original mistakes.
Raw and validated predictions, generation settings and provenance are retained.

These are SFT dev diagnostics, not B's UCR or whole-answer accuracy. Value exact
match uses case-folded/trimmed text, not embeddings. Compare identical data,
limits and token budgets across both models.

### 6. Run the application with the trained judge

Return to **Windows PowerShell** in `D:\UIUC\CS546\moshi-rag`. Ordinary
inference uses your normal Python environment, not the WSL training environment:

```powershell
python -m cascadesystem.training run --run cascadesystem/artifacts/training/runs/gpt120-judge-v1 -- --question "Which city is the Eiffel Tower in, and when did it open?" --tts windows --play
python -m cascadesystem.training run --run cascadesystem/artifacts/training/runs/gpt120-judge-v1 -- --chat --tts windows --play
```

With the existing speech environment prepared:

```powershell
python -m cascadesystem.training run --run cascadesystem/artifacts/training/runs/gpt120-judge-v1 -- --listen --barge-in --tts windows --play
```

The wrapper reads `best.json`, checks its base model/prompt hash and sets
`CASCADE_JUDGE_MODEL` plus low judge reasoning in the child environment only.
It never edits `.env`. Only `judge`/`judge_repair` calls use the adapter; other
stages use `CASCADE_MODEL`. Normal commands without this wrapper use the
configured base judge unless you explicitly set `CASCADE_JUDGE_MODEL` yourself.

To replay the existing 20 debug questions with this judge and save WAVs:

```powershell
python -m cascadesystem.training run --run cascadesystem/artifacts/training/runs/gpt120-judge-v1 --debug20 -- run --schedule all --tts windows
```

This creates a new debug run using fixed timed evidence and B's unchanged
scorer, including its mapping-review requirements. Debug questions are never
training input. See [Debug20](<../../eval debug20/README.md>) for input preparation,
scoring and playback. Public run settings record the selected judge checkpoint.

## Data and limitations

B's original 300 SFT questions are split into 243 train and 57 dev questions.
Multiple evidence orders/times create 1,991 train and 486 dev snapshots.
Conversion retains **1,900 snapshots from 235 train questions** and **463
snapshots from 54 dev questions**, before tokenizer length filtering.

Conversion preserves B's labels. It uses the current judge prompt/JSON schema,
copies only currently visible sentences into model input, and attaches those
literal sentences to supported targets. It excludes omission-based questions
and snapshots whose old dependency exceptions conflict with current validation,
recording every exclusion. B's gold, scorer and experimental definitions stay
unchanged. Train/dev are separated by question ID and normalized question text.
Targets stay separate from prediction input; reserved data/debug answers are
not exported. Raw sources, hashes, conversions and exclusions stay under the
ignored `cascadesystem/artifacts/training/data/` directory.

The data has no `CONTRADICTED` targets and no dedicated single-answer/multipart
coverage. Units use B's annotated descriptions rather than current model
decompositions; subjects are unspecified. Quotes are copied full visible
sentences, not independently reviewed minimal spans. This is a starting dataset;
LoRA may not fix decomposition errors or generalize to every current failure.
Natural final sentences still come from the base model.

## Outputs and files

| File | Purpose |
|---|---|
| [`__main__.py`](__main__.py) | `prepare`, `inspect`, `train`, `evaluate`, and checkpoint inference wrapper. |
| [`data.py`](data.py) | Fixed SFT-only Git export, conversion, exclusions and hash/split checks. |
| [`sdk.py`](sdk.py) | Lazy SDK imports, official Harmony rendering, assistant-only shifted loss and remote operations. |
| [`engine.py`](engine.py) | Epochs, deterministic ordering, dev-loss selection, saved states, resume and dev metrics. |
| [`requirements.txt`](requirements.txt) | Separate optional training dependencies. |
| [`__init__.py`](__init__.py) | Package marker with no remote work on import. |
| [`test_lora_training.py`](../tests/test_lora_training.py) | Fictional data isolation, lifecycle, routing and checkpoint tests. |
| [`test_lora_sdk.py`](../tests/test_lora_sdk.py) | Fake SDK mask, optimizer, resume, cleanup and final-channel tests. |
| [`test_checkpoint_paths.py`](../tests/test_checkpoint_paths.py) | SDK run-ID suffixes, path rejection, save/selection/wrapper integration and HTTP model routing. |

Each run saves `config.json` (settings/hashes), `provenance.json` (parent commit
and dirty state), `tokenization.json` (kept/excluded rows), `events.jsonl`
(attempts/losses), and `epoch-*.json` (losses/checkpoint paths). `resume.json`
contains a `weights` state path for training; `best.json` contains a
`sampler_weights` path for inference. These path types are not interchangeable.
Weights remain hosted on Tinker; local files are metadata. Keys/artifacts are ignored.

Offline validation:

```powershell
python -m unittest cascadesystem.tests.test_lora_training cascadesystem.tests.test_lora_sdk -v
```

Fictional offline tests passed. The assistant has not installed the real SDK,
started remote training or verified account/model access, checkpoint inference
or resulting accuracy.

Official references: [SFT quickstart](https://tinker-docs.thinkingmachines.ai/tinker/quickstart/),
[checkpoint inference](https://tinker-docs.thinkingmachines.ai/inference/openai/overview/),
[state restoration and cleanup](https://tinker-docs.thinkingmachines.ai/tinker/api-reference/serviceclient/).
