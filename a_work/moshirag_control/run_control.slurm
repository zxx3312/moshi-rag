#!/bin/bash
# MoshiRAG control experiment on one A100: reference encoder + all (question, condition, seed) runs.
#
# Submit FROM THE REPOSITORY ROOT:
#     sbatch a_work/moshirag_control/run_control.slurm
# Smoke test first:
#     SAMPLE_IDS="sqa_3564" sbatch a_work/moshirag_control/run_control.slurm
#
# Overrides: MANIFEST, CONDITIONS, SEEDS, SAMPLE_IDS, RUN_NAME, CONDA_ENV, HF_HOME.
#
#SBATCH --job-name=moshirag-control
#SBATCH --partition=IllinoisComputes-GPU
#SBATCH --account=dilek-ic
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --gres=gpu:A100:1
#SBATCH --time=01:30:00
#SBATCH --signal=B:TERM@120
#SBATCH --output=a_work/moshirag_control/slurm_logs/%x-%j.out

set -euo pipefail

A_REL="a_work/moshirag_control"
MANIFEST="${MANIFEST:-$A_REL/configs/control_manifest.jsonl}"
CONDITIONS="${CONDITIONS:-free wait progress notready ours}"
SEEDS="${SEEDS:-42424242}"
SAMPLE_IDS="${SAMPLE_IDS:-}"
RUN_NAME="${RUN_NAME:-$(date +%Y%m%d_%H%M%S)_job${SLURM_JOB_ID:-local}}"
HF_RAG_REPO="kyutai/moshika-rag-pytorch-bf16"
export HF_HOME="${HF_HOME:-/projects/illinois/eng/cs/dilek/xzhu81/hf_home}"
export HF_HUB_OFFLINE=1
PORT="$((20000 + ${SLURM_JOB_ID:-0} % 20000))"
export REFERENCE_ENCODER_URL="http://127.0.0.1:${PORT}"

COND_PID=""
cleanup() {
    local rc=$?
    trap - EXIT INT TERM
    if [[ -n "$COND_PID" ]] && kill -0 "$COND_PID" 2>/dev/null; then
        kill -TERM "$COND_PID" 2>/dev/null
        for _ in $(seq 1 30); do kill -0 "$COND_PID" 2>/dev/null || break; sleep 1; done
        kill -KILL "$COND_PID" 2>/dev/null || true
    fi
    echo "[cleanup] exit code $rc at $(date -Is)"
    exit "$rc"
}
trap cleanup EXIT
trap 'echo "[signal] stopping"; exit 143' INT TERM

cd "${SLURM_SUBMIT_DIR:-$(pwd)}"
[[ -f "$A_REL/run_control.py" ]] || { echo "submit from the repository root" >&2; exit 2; }
echo "job ${SLURM_JOB_ID:-local} on $(hostname); repo @ $(git rev-parse --abbrev-ref HEAD) $(git rev-parse --short HEAD)"
nvidia-smi --query-gpu=name,memory.total --format=csv || true

module load anaconda3/2024.10
eval "$(conda shell.bash hook)"
set +u; conda activate "${CONDA_ENV:-moshirag}"; set -u
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-8}"

read -r -a COND_ARR <<< "$CONDITIONS"
read -r -a SEED_ARR <<< "$SEEDS"
ARGS=(--manifest "$MANIFEST" --conditions "${COND_ARR[@]}" --seeds "${SEED_ARR[@]}" --run-name "$RUN_NAME")
if [[ -n "$SAMPLE_IDS" ]]; then read -r -a ID_ARR <<< "$SAMPLE_IDS"; ARGS+=(--sample-ids "${ID_ARR[@]}"); fi

python "$A_REL/run_control.py" "${ARGS[@]}" --dry-run

RUN_DIR="$A_REL/results/$RUN_NAME"
mkdir -p "$A_REL/slurm_logs"
COND_LOG="$A_REL/slurm_logs/conditioner-${SLURM_JOB_ID:-local}.log"
(
    cd moshi
    exec python -m moshi.server_conditioner --config "hf://$HF_RAG_REPO/config.json" \
        --moshi-weight "hf://$HF_RAG_REPO/model.safetensors" --cuda-device 0 \
        --conditioner reference_with_time --host 127.0.0.1 --port "$PORT"
) > "$COND_LOG" 2>&1 &
COND_PID=$!

deadline=$((SECONDS + 900))
until python -c "import sys, urllib.request; urllib.request.urlopen(sys.argv[1], timeout=5)" "$REFERENCE_ENCODER_URL/health" 2>/dev/null; do
    kill -0 "$COND_PID" 2>/dev/null || { echo "encoder died:" >&2; tail -n 40 "$COND_LOG" >&2; exit 3; }
    (( SECONDS < deadline )) || { echo "encoder not healthy after 900 s" >&2; tail -n 40 "$COND_LOG" >&2; exit 3; }
    sleep 10
done
echo "reference encoder healthy after ${SECONDS}s"

python "$A_REL/run_control.py" "${ARGS[@]}" &
RUN_PID=$!
RC=0
wait "$RUN_PID" || RC=$?
echo "runner exited with code $RC; results in $RUN_DIR"
exit "$RC"
