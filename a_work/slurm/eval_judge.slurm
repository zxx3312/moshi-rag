#!/bin/bash
# Serve the judge LLM with vLLM on one GPU and run a script against it (a_work/eval_judge.py by default).
#
# Submit FROM THE REPOSITORY ROOT:
#     sbatch a_work/slurm/eval_judge.slurm
# Overrides: MODEL, RUN_NAME, EVAL_ARGS (e.g. "--thinking"), SCRIPT, RESULT_GROUP, VLLM_ARGS, VLLM_ENV, HF_HOME.
# A LoRA judge: VLLM_ARGS="--enable-lora --lora-modules judge=ADAPTER_DIR" with --judge-model judge in EVAL_ARGS.
# A second server on the same GPU, for run_replay.py: JUDGE_BASE=MODEL JUDGE_VLLM_ARGS=... with GPU_UTIL and
# JUDGE_GPU_UTIL summing under 1; --judge-base-url is added for you.
# The cascade: PYTHON=TTS_ENV/bin/python runs the script where piper-tts is installed (the script itself needs
# only the standard library), and PRE_CMD="..." runs first on the GPU, before the servers take it (run_asr.py).
#
#SBATCH --job-name=a-eval-judge
#SBATCH --partition=secondary
# Use the authorized project account; priority depends on partition tier and site policy.
#SBATCH --account=dilek-ic
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --gres=gpu:1
# H100 only, so judge latency is comparable across runs.
#SBATCH --constraint=H100|h100
#SBATCH --time=02:00:00
#SBATCH --output=a_work/slurm/logs/%x-%j.out

set -euo pipefail

MODEL="${MODEL:-Qwen/Qwen3-14B}"
VLLM_ENV="${VLLM_ENV:-/projects/illinois/eng/cs/dilek/xzhu81/envs/vllm}"
RUN_NAME="${RUN_NAME:-$(date +%Y%m%d_%H%M%S)_job${SLURM_JOB_ID:-local}}"
EVAL_ARGS="${EVAL_ARGS:-}"
export HF_HOME="${HF_HOME:-/projects/illinois/eng/cs/dilek/xzhu81/hf_home}"
export HF_HUB_OFFLINE=1
# The venv is not activated: put its tools (ninja) on PATH, and use PyTorch sampling instead of
# FlashInfer's JIT-built sampler (the judge decodes greedily, so the result is the same).
export PATH="$VLLM_ENV/bin:$PATH"
export VLLM_USE_FLASHINFER_SAMPLER=0
PORT="$((20000 + ${SLURM_JOB_ID:-0} % 20000))"
SCRIPT="${SCRIPT:-a_work/eval_judge.py}"
OUT="a_work/results/${RESULT_GROUP:-judge}/$RUN_NAME"
read -r -a VLLM_EXTRA <<< "${VLLM_ARGS:-}"
read -r -a JUDGE_EXTRA <<< "${JUDGE_VLLM_ARGS:-}"
JUDGE_BASE="${JUDGE_BASE:-}"
JUDGE_PORT="$((PORT + 1))"

PYTHON="${PYTHON:-$VLLM_ENV/bin/python}"

cd "${SLURM_SUBMIT_DIR:-$(pwd)}"
[[ -f "$SCRIPT" ]] || { echo "submit from the repository root" >&2; exit 2; }
mkdir -p "$OUT"
echo "job ${SLURM_JOB_ID:-local} on $(hostname); repo @ $(git rev-parse --abbrev-ref HEAD) $(git rev-parse --short HEAD)"
nvidia-smi --query-gpu=name,memory.total --format=csv || true
if [[ -n "${PRE_CMD:-}" ]]; then
    echo "[pre] $PRE_CMD"
    bash -c "$PRE_CMD"
fi

SERVER_PID=""
JUDGE_PID=""
cleanup() {
    local rc=$?
    trap - EXIT INT TERM
    for pid in "$SERVER_PID" "$JUDGE_PID"; do
        if [[ -n "$pid" ]] && kill -0 "$pid" 2>/dev/null; then
            kill -TERM "$pid"; sleep 5; kill -KILL "$pid" 2>/dev/null || true
        fi
    done
    echo "[cleanup] exit code $rc at $(date -Is)"
    exit "$rc"
}
trap cleanup EXIT
trap 'exit 143' INT TERM

# The reasoning parser keeps Qwen3's <think> part out of the JSON constraint, so thinking mode works;
# with thinking off it changes nothing.
"$VLLM_ENV/bin/vllm" serve "$MODEL" --port "$PORT" --max-model-len 16384 --reasoning-parser qwen3 \
    --gpu-memory-utilization "${GPU_UTIL:-0.90}" "${VLLM_EXTRA[@]}" > "$OUT/vllm.log" 2>&1 &
SERVER_PID=$!

wait_ready() {  # port pid log
    local deadline=$((SECONDS + 1200))
    until curl -sf "http://127.0.0.1:$1/v1/models" > /dev/null; do
        kill -0 "$2" 2>/dev/null || { echo "vLLM exited:" >&2; tail -n 40 "$3" >&2; exit 3; }
        (( SECONDS < deadline )) || { echo "vLLM not ready after 1200 s" >&2; tail -n 40 "$3" >&2; exit 3; }
        sleep 10
    done
    echo "vLLM on port $1 ready after ${SECONDS}s"
}
wait_ready "$PORT" "$SERVER_PID" "$OUT/vllm.log"

read -r -a EXTRA <<< "$EVAL_ARGS"
if [[ -n "$JUDGE_BASE" ]]; then  # started second: vLLM checks free GPU memory at startup
    "$VLLM_ENV/bin/vllm" serve "$JUDGE_BASE" --port "$JUDGE_PORT" --max-model-len 16384 --reasoning-parser qwen3 \
        --gpu-memory-utilization "${JUDGE_GPU_UTIL:-0.30}" "${JUDGE_EXTRA[@]}" > "$OUT/vllm_judge.log" 2>&1 &
    JUDGE_PID=$!
    wait_ready "$JUDGE_PORT" "$JUDGE_PID" "$OUT/vllm_judge.log"
    EXTRA+=(--judge-base-url "http://127.0.0.1:$JUDGE_PORT/v1")
fi
"$PYTHON" "$SCRIPT" --base-url "http://127.0.0.1:$PORT/v1" --model "$MODEL" \
    --out "$OUT" "${EXTRA[@]}"
