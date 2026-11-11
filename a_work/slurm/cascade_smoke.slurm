#!/bin/bash
# Submit from the repository root with SNAPSHOT, INPUT_DIR and RUN_NAME set.
# INPUT_DIR contains only a small debug subset, its gold, and question_audio/index.jsonl.
# SNAPSHOT contains run_replay.py, run_asr.py, eval_with_b.py, eval_judge.slurm and turntaking/.
# This verifies real ASR and TTS inside a simulated evidence replay, not a live audio server.
#SBATCH --job-name=a-cascade-smoke
#SBATCH --partition=IllinoisComputes-GPU,secondary
#SBATCH --account=dilek-ic
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --gres=gpu:1
#SBATCH --constraint=AE7763_100g_512G_A100|A100
#SBATCH --time=00:30:00
#SBATCH --output=a_work/slurm/logs/%x-%j.out

set -euo pipefail
cd "${SLURM_SUBMIT_DIR:?submit from the repository root}"
: "${SNAPSHOT:?set an absolute code snapshot directory}"
: "${INPUT_DIR:?set an absolute debug input directory}"
: "${RUN_NAME:?set a unique output name}"

export VLLM_ENV="${VLLM_ENV:-/projects/illinois/eng/cs/dilek/xzhu81/envs/vllm}"
TTS_ENV="${TTS_ENV:-/projects/illinois/eng/cs/dilek/xzhu81/envs/tts}"
VOICE="${VOICE:-/projects/illinois/eng/cs/dilek/xzhu81/piper_voices/en_US-lessac-medium.onnx}"
ADAPTER="${ADAPTER:-$PWD/a_work/results/lora/qwen3_4b_v1/best}"
: "${B_EVAL_REF:?set the evaluator commit used for this experiment}"
export RESULT_GROUP=replay
OUT="$PWD/a_work/results/$RESULT_GROUP/$RUN_NAME"

[[ ! -e "$OUT" ]] || { echo "Output already exists: $OUT" >&2; exit 2; }
for file in "$SNAPSHOT/run_replay.py" "$SNAPSHOT/run_asr.py" "$SNAPSHOT/eval_with_b.py" \
            "$SNAPSHOT/eval_judge.slurm" "$SNAPSHOT/manifest.json" \
            "$INPUT_DIR/traces_debug.jsonl" "$INPUT_DIR/gold_debug.jsonl" \
            "$INPUT_DIR/question_audio/index.jsonl" "$VOICE" "$VOICE.json" \
            "$ADAPTER/adapter_config.json"; do
    [[ -s "$file" ]] || { echo "Missing prerequisite: $file" >&2; exit 2; }
done
"$VLLM_ENV/bin/python" - "$SNAPSHOT/manifest.json" <<'PY'
import hashlib
import json
import sys
from pathlib import Path
manifest = json.loads(Path(sys.argv[1]).read_text())
for item in manifest["files"]:
    path = Path(item["path"])
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != item["sha256"]:
        raise SystemExit(f"Snapshot/input changed or missing: {path}")
print(f"Verified {len(manifest['files'])} frozen code, input and model files", flush=True)
PY

export PYTHON="$TTS_ENV/bin/python"
export SCRIPT="$SNAPSHOT/run_replay.py"
export MODEL=Qwen/Qwen3-14B
export VLLM_ARGS=""
export GPU_UTIL=0.55 JUDGE_GPU_UTIL=0.30 JUDGE_BASE=Qwen/Qwen3-4B
export JUDGE_VLLM_ARGS="--enable-lora --lora-modules judge=$ADAPTER"
export OMP_NUM_THREADS=4 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=4
# shell-quote the pre-command because eval_judge.slurm executes it through bash.
printf -v PRE_CMD '%q ' "$VLLM_ENV/bin/python" "$SNAPSHOT/run_asr.py" \
    --audio "$INPUT_DIR/question_audio" --out "$OUT/asr.jsonl" --device cuda
export PRE_CMD
export EVAL_ARGS="--trace $INPUT_DIR/traces_debug.jsonl --gold $INPUT_DIR/gold_debug.jsonl --generate --concurrent --judge-model judge --judge-name lora --no-examples --asr $OUT/asr.jsonl --tts piper:$VOICE --save-audio"

bash "$SNAPSHOT/eval_judge.slurm"
"$VLLM_ENV/bin/python" "$SNAPSHOT/eval_with_b.py" "$OUT" --repo "$PWD" --ref "$B_EVAL_REF"
