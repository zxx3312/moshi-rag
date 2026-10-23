#!/bin/bash
# Serve the judge LLM with vLLM on one GPU and run a_work/eval_judge.py against it.
#
# Submit FROM THE REPOSITORY ROOT:
#     sbatch a_work/slurm/eval_judge.slurm
# Overrides: MODEL, RUN_NAME, EVAL_ARGS (e.g. "--thinking"), VLLM_ENV, HF_HOME.
#
#SBATCH --job-name=a-eval-judge
#SBATCH --partition=secondary
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --gres=gpu:1
#SBATCH --constraint=A100|H100|h100|A40|RTXA6000
#SBATCH --time=01:00:00
#SBATCH --output=a_work/slurm/logs/%x-%j.out

set -euo pipefail

MODEL="${MODEL:-Qwen/Qwen3-14B}"
VLLM_ENV="${VLLM_ENV:-/projects/illinois/eng/cs/dilek/xzhu81/envs/vllm}"
RUN_NAME="${RUN_NAME:-$(date +%Y%m%d_%H%M%S)_job${SLURM_JOB_ID:-local}}"
EVAL_ARGS="${EVAL_ARGS:-}"
export HF_HOME="${HF_HOME:-/projects/illinois/eng/cs/dilek/xzhu81/hf_home}"
export HF_HUB_OFFLINE=1
PORT="$((20000 + ${SLURM_JOB_ID:-0} % 20000))"
OUT="a_work/results/judge/$RUN_NAME"

cd "${SLURM_SUBMIT_DIR:-$(pwd)}"
[[ -f a_work/eval_judge.py ]] || { echo "submit from the repository root" >&2; exit 2; }
mkdir -p "$OUT"
echo "job ${SLURM_JOB_ID:-local} on $(hostname); repo @ $(git rev-parse --abbrev-ref HEAD) $(git rev-parse --short HEAD)"
nvidia-smi --query-gpu=name,memory.total --format=csv || true

SERVER_PID=""
cleanup() {
    local rc=$?
    trap - EXIT INT TERM
    if [[ -n "$SERVER_PID" ]] && kill -0 "$SERVER_PID" 2>/dev/null; then
        kill -TERM "$SERVER_PID"; sleep 5; kill -KILL "$SERVER_PID" 2>/dev/null || true
    fi
    echo "[cleanup] exit code $rc at $(date -Is)"
    exit "$rc"
}
trap cleanup EXIT
trap 'exit 143' INT TERM

"$VLLM_ENV/bin/vllm" serve "$MODEL" --port "$PORT" --max-model-len 8192 \
    --gpu-memory-utilization 0.90 > "$OUT/vllm.log" 2>&1 &
SERVER_PID=$!

deadline=$((SECONDS + 1200))
until curl -sf "http://127.0.0.1:$PORT/v1/models" > /dev/null; do
    kill -0 "$SERVER_PID" 2>/dev/null || { echo "vLLM exited:" >&2; tail -n 40 "$OUT/vllm.log" >&2; exit 3; }
    (( SECONDS < deadline )) || { echo "vLLM not ready after 1200 s" >&2; tail -n 40 "$OUT/vllm.log" >&2; exit 3; }
    sleep 10
done
echo "vLLM ready after ${SECONDS}s"

read -r -a EXTRA <<< "$EVAL_ARGS"
"$VLLM_ENV/bin/python" a_work/eval_judge.py --base-url "http://127.0.0.1:$PORT/v1" --model "$MODEL" \
    --out "$OUT" "${EXTRA[@]}"
