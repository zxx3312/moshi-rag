#!/bin/bash
#SBATCH --job-name=a-tts-export
#SBATCH --partition=scavenger,secondary
#SBATCH --account=dilek-ic
#SBATCH --qos=normal
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=00:30:00
#SBATCH --output=a_work/slurm/logs/%x-%j.out

set -euo pipefail
: "${SNAPSHOT_DIR:?Provide the frozen source and policy log directory}"
: "${EXPORT_OUT:?Provide a new audio output directory}"
: "${VOICE_PATH:?Provide the Piper ONNX voice}"
PYTHON="${PYTHON:-/projects/illinois/eng/cs/dilek/xzhu81/envs/tts/bin/python}"
export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=4 OPENBLAS_NUM_THREADS=4
cd "${SLURM_SUBMIT_DIR:-$(pwd)}"
read -r -a EXTRA <<< "${EXPORT_ARGS:-}"
exec "$PYTHON" "${SNAPSHOT_DIR}/export_speech.py" \
    --logs "${SNAPSHOT_DIR}/policy_log.jsonl" --voice "$VOICE_PATH" \
    --out "$EXPORT_OUT" "${EXTRA[@]}"
