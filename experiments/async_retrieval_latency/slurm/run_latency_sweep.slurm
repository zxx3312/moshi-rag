#!/bin/bash
# Controlled retrieval-latency sweep for MoshiRAG on ONE A100, all conditions sequential.
#
# Submit FROM THE REPOSITORY ROOT (the --output path below is relative to it):
#     sbatch experiments/async_retrieval_latency/slurm/run_latency_sweep.slurm
#
# Optional overrides (environment variables), e.g. a minimal first test:
#     DELAYS="3" MAX_SAMPLES=1 sbatch experiments/async_retrieval_latency/slurm/run_latency_sweep.slurm
#
#   CONDA_ENV / VENV_PATH   Python env with moshi deps (Python >= 3.11). VENV_PATH wins if set.
#   MANIFEST                sample manifest (default configs/samples.jsonl)
#   DELAYS                  space-separated delays in seconds (default "0 0.5 1 2 3 5 8")
#   SEEDS                   space-separated seeds (default "42424242")
#   MAX_SAMPLES, SAMPLE_IDS optional sample selection
#   EXTRA_ARGS              extra flags for run_latency_sweep.py
#
# The job ends as soon as the sweep finishes (no infinite loops, no sleep infinity,
# no tail -f). The reference-encoder server started below is always stopped by the
# EXIT trap: on success, on errors, on scancel and on the time limit.
#
#SBATCH --job-name=moshirag-latency
#SBATCH --partition=IllinoisComputes-GPU
#SBATCH --account=dilek-ic
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --gres=gpu:A100:1
#SBATCH --time=02:00:00
#SBATCH --signal=B:TERM@120
#SBATCH --output=experiments/async_retrieval_latency/slurm/logs/%x-%j.out

set -euo pipefail

# ---------------------------------------------------------------- settings
CONDA_MODULE="${CONDA_MODULE:-anaconda3/2024.10}"
CONDA_ENV="${CONDA_ENV:-moshirag}"
VENV_PATH="${VENV_PATH:-}"
EXP_REL="experiments/async_retrieval_latency"
MANIFEST="${MANIFEST:-$EXP_REL/configs/samples.jsonl}"
DELAYS="${DELAYS:-0 0.5 1 2 3 5 8}"
SEEDS="${SEEDS:-42424242}"
MAX_SAMPLES="${MAX_SAMPLES:-}"
SAMPLE_IDS="${SAMPLE_IDS:-}"
EXTRA_ARGS="${EXTRA_ARGS:-}"
HF_RAG_REPO="${HF_RAG_REPO:-kyutai/moshika-rag-pytorch-bf16}"
JOB_LIMIT_S="${JOB_LIMIT_S:-7200}"                                # keep in sync with --time
CONDITIONER_STARTUP_TIMEOUT="${CONDITIONER_STARTUP_TIMEOUT:-1800}" # first run may download weights
CONDITIONER_PORT="${CONDITIONER_PORT:-$((20000 + ${SLURM_JOB_ID:-0} % 20000))}"

# ---------------------------------------------------------------- cleanup
CHILD_PIDS=()

cleanup() {
    local rc=$?
    trap - EXIT INT TERM
    set +e
    for pid in "${CHILD_PIDS[@]}"; do
        if kill -0 "$pid" 2>/dev/null; then
            echo "[cleanup] sending TERM to pid $pid"
            kill -TERM "$pid" 2>/dev/null
        fi
    done
    # Give children up to 30 s to exit cleanly, then force-kill (bounded loop).
    for _ in $(seq 1 30); do
        local alive=0
        for pid in "${CHILD_PIDS[@]}"; do
            kill -0 "$pid" 2>/dev/null && alive=1
        done
        [[ $alive -eq 0 ]] && break
        sleep 1
    done
    for pid in "${CHILD_PIDS[@]}"; do
        if kill -0 "$pid" 2>/dev/null; then
            echo "[cleanup] pid $pid still alive, sending KILL"
            kill -KILL "$pid" 2>/dev/null
        fi
    done
    wait 2>/dev/null
    echo "[cleanup] done at $(date -Is), exit code $rc"
    exit "$rc"
}
trap cleanup EXIT
trap 'echo "[signal] received INT/TERM at $(date -Is), stopping"; exit 143' INT TERM

# ---------------------------------------------------------------- setup
REPO_ROOT="${SLURM_SUBMIT_DIR:-$(pwd)}"
cd "$REPO_ROOT"
if [[ ! -f moshi/moshi/run_inference.py || ! -d "$EXP_REL" ]]; then
    echo "ERROR: submit this job from the moshi-rag repository root (got $REPO_ROOT)" >&2
    exit 2
fi

echo "job ${SLURM_JOB_ID:-local} on $(hostname) at $(date -Is)"
echo "repo $REPO_ROOT @ $(git rev-parse --abbrev-ref HEAD) $(git rev-parse --short HEAD)"
nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv || true

if [[ -n "$VENV_PATH" ]]; then
    # shellcheck disable=SC1091
    source "$VENV_PATH/bin/activate"
else
    module load "$CONDA_MODULE"
    eval "$(conda shell.bash hook)"
    set +u  # conda activation scripts reference unset variables
    conda activate "$CONDA_ENV"
    set -u
fi
echo "python: $(command -v python) ($(python --version 2>&1))"

export PYTHONUNBUFFERED=1
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-8}"
export REFERENCE_ENCODER_URL="http://127.0.0.1:${CONDITIONER_PORT}"
unset MOSHI_RETRIEVAL_LLMS_JSON  # retrieval is the in-process fixed-reference mock
echo "HF_HOME=${HF_HOME:-<unset, default ~/.cache/huggingface>}"

RUN_NAME="${RUN_NAME:-$(date +%Y%m%d_%H%M%S)_job${SLURM_JOB_ID:-local}}"
OUTPUT_ROOT="$REPO_ROOT/$EXP_REL/results"
RUN_DIR="$OUTPUT_ROOT/$RUN_NAME"
mkdir -p "$RUN_DIR/logs"
echo "run directory: $RUN_DIR"

read -r -a DELAY_ARR <<< "$DELAYS"
read -r -a SEED_ARR <<< "$SEEDS"
read -r -a EXTRA_ARR <<< "$EXTRA_ARGS"
RUN_ARGS=(
    --manifest "$MANIFEST"
    --retrieval-delay "${DELAY_ARR[@]}"
    --seeds "${SEED_ARR[@]}"
    --output-root "$OUTPUT_ROOT"
    --run-name "$RUN_NAME"
    --hf-repo "$HF_RAG_REPO"
)
if [[ -n "$MAX_SAMPLES" ]]; then
    RUN_ARGS+=(--max-samples "$MAX_SAMPLES")
fi
if [[ -n "$SAMPLE_IDS" ]]; then
    read -r -a SAMPLE_ID_ARR <<< "$SAMPLE_IDS"
    RUN_ARGS+=(--sample-ids "${SAMPLE_ID_ARR[@]}")
fi
RUN_ARGS+=("${EXTRA_ARR[@]}")

# ---------------------------------------------------------------- preflight (no GPU work)
echo "== preflight dry run =="
python "$EXP_REL/scripts/run_latency_sweep.py" "${RUN_ARGS[@]}" --dry-run --require-env

# ---------------------------------------------------------------- reference encoder service
echo "== starting reference encoder on port $CONDITIONER_PORT =="
COND_LOG="$RUN_DIR/logs/conditioner.log"
(
    cd moshi
    exec python -m moshi.server_conditioner \
        --config "hf://$HF_RAG_REPO/config.json" \
        --moshi-weight "hf://$HF_RAG_REPO/model.safetensors" \
        --cuda-device 0 \
        --conditioner reference_with_time \
        --host 127.0.0.1 \
        --port "$CONDITIONER_PORT"
) > "$COND_LOG" 2>&1 &
COND_PID=$!
CHILD_PIDS+=("$COND_PID")

deadline=$((SECONDS + CONDITIONER_STARTUP_TIMEOUT))
until python -c "import sys, urllib.request; urllib.request.urlopen(sys.argv[1], timeout=5)" \
        "$REFERENCE_ENCODER_URL/health" 2>/dev/null; do
    if ! kill -0 "$COND_PID" 2>/dev/null; then
        echo "ERROR: reference encoder exited during startup; last log lines:" >&2
        tail -n 40 "$COND_LOG" >&2 || true
        exit 3
    fi
    if (( SECONDS >= deadline )); then
        echo "ERROR: reference encoder not healthy after ${CONDITIONER_STARTUP_TIMEOUT}s" >&2
        tail -n 40 "$COND_LOG" >&2 || true
        exit 3
    fi
    sleep 10
done
echo "reference encoder healthy after ${SECONDS}s (job time)"

# ---------------------------------------------------------------- sweep
RUNNER_TIMEOUT=$((JOB_LIMIT_S - SECONDS - 300))
if (( RUNNER_TIMEOUT < 600 )); then
    echo "ERROR: only ${RUNNER_TIMEOUT}s left for the sweep" >&2
    exit 4
fi
echo "== running sweep (timeout ${RUNNER_TIMEOUT}s) =="
# Background + wait so the TERM trap runs immediately on scancel / time limit.
timeout --signal=TERM --kill-after=60 "$RUNNER_TIMEOUT" \
    python "$EXP_REL/scripts/run_latency_sweep.py" "${RUN_ARGS[@]}" &
RUN_PID=$!
CHILD_PIDS+=("$RUN_PID")
RC=0
wait "$RUN_PID" || RC=$?
echo "sweep exited with code $RC"

# Release the GPU-side encoder before the (CPU-only) summary.
kill -TERM "$COND_PID" 2>/dev/null || true
wait "$COND_PID" 2>/dev/null || true

if [[ -f "$RUN_DIR/results.jsonl" ]]; then
    echo "== summary =="
    cat "$RUN_DIR/run_status.json" 2>/dev/null || true
    python "$EXP_REL/analysis/analyze_latency.py" "$RUN_DIR" || echo "analysis failed (non-fatal)"
fi
exit "$RC"
