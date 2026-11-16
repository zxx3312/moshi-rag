#!/bin/bash
# Frozen 900-trace main experiment. Submit the command printed by main_experiments.py command.
# Both partitions admit normal QoS. scavenger has PriorityTier=3; secondary is the H100 fallback.
# FairShare currently has weight 0. Account choice alone does not create a priority bonus.
#SBATCH --job-name=a-main-experiments
#SBATCH --account=dilek-ic
#SBATCH --partition=scavenger,secondary
#SBATCH --qos=normal
#SBATCH --nice=0
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --gres=gpu:H100:1
#SBATCH --constraint=H100|h100
#SBATCH --time=04:00:00
#SBATCH --output=a_work/slurm/logs/%x-%A_%a.out
#SBATCH --no-requeue

set -euo pipefail
cd "${SLURM_SUBMIT_DIR:?Submit from the repository root}"
BUNDLE="${1:?Pass the frozen bundle directory}"
VLLM_ENV="${VLLM_ENV:-/projects/illinois/eng/cs/dilek/xzhu81/envs/vllm}"
export HF_HOME="${HF_HOME:-/projects/illinois/eng/cs/dilek/xzhu81/hf_home}"
export HF_HUB_OFFLINE=1
export VLLM_USE_FLASHINFER_SAMPLER=0
export PATH="$VLLM_ENV/bin:$PATH"
PYTHON="$VLLM_ENV/bin/python"
SHARD="${SLURM_ARRAY_TASK_ID:?Submit as a Slurm array}"
"$PYTHON" "$BUNDLE/runner/main_experiments.py" verify --bundle "$BUNDLE"
RESULT_ROOT="$("$PYTHON" -c 'import json,sys; print(json.load(open(sys.argv[1]))["results"])' "$BUNDLE/manifest.json")"
OUT="$RESULT_ROOT/$(printf 'shard_%03d' "$SHARD")"
mkdir -p "$OUT"
"$PYTHON" - "$OUT/gpu.json" <<'PY'
import importlib.metadata,json,os,subprocess,sys
command=['nvidia-smi','--query-gpu=name,memory.total','--format=csv,noheader,nounits']
visible=os.environ.get('CUDA_VISIBLE_DEVICES')
if visible:
    command.extend(['--id',visible])
gpu = subprocess.check_output(command,text=True).strip()
rows = gpu.splitlines()
if len(rows) != 1 or 'H100' not in rows[0] or not 75000 <= float(rows[0].rsplit(',',1)[1]) <= 85000:
    raise SystemExit('Expected one full H100 80GB; received: ' + gpu)
json.dump({'gpu':gpu, 'job_id':os.environ['SLURM_JOB_ID'],
           'array_job_id':os.environ.get('SLURM_ARRAY_JOB_ID'),
           'array_task_id':os.environ.get('SLURM_ARRAY_TASK_ID'),
           'partition':os.environ.get('SLURM_JOB_PARTITION'),
           'vllm_version':importlib.metadata.version('vllm'),
           'torch_version':importlib.metadata.version('torch')},open(sys.argv[1],'w'),indent=2)
PY
scontrol show job "$SLURM_JOB_ID" > "$OUT/slurm_job.txt"
scontrol show config | awk '/PriorityType|PriorityWeight/' > "$OUT/priority_config.txt"
PORT=$((20000 + SLURM_JOB_ID % 20000))
LORA_PORT=$((PORT + 1))
SERVER_PID=""
LORA_PID=""
cleanup() {
    local rc=$?
    trap - EXIT INT TERM
    for pid in "$SERVER_PID" "$LORA_PID"; do
        if [[ -n "$pid" ]]; then kill -TERM "$pid" 2>/dev/null || true; fi
    done
    echo "[exit] code=$rc job=$SLURM_JOB_ID shard=$SHARD"
    exit "$rc"
}
trap cleanup EXIT
trap 'exit 143' INT TERM
wait_ready() {
    local port="$1" pid="$2" log="$3" deadline=$((SECONDS + 1200))
    until curl -sf "http://127.0.0.1:$port/v1/models" >/dev/null; do
        kill -0 "$pid" 2>/dev/null || { tail -n 40 "$log" >&2; exit 3; }
        (( SECONDS < deadline )) || { echo "vLLM readiness timeout" >&2; exit 3; }
        sleep 5
    done
}
"$VLLM_ENV/bin/vllm" serve Qwen/Qwen3-14B --host 127.0.0.1 --port "$PORT" \
    --max-model-len 16384 --reasoning-parser qwen3 --gpu-memory-utilization 0.55 > "$OUT/vllm_14b.log" 2>&1 &
SERVER_PID=$!
wait_ready "$PORT" "$SERVER_PID" "$OUT/vllm_14b.log"
"$VLLM_ENV/bin/vllm" serve Qwen/Qwen3-4B --host 127.0.0.1 --port "$LORA_PORT" \
    --max-model-len 16384 --reasoning-parser qwen3 --gpu-memory-utilization 0.30 \
    --enable-lora --lora-modules "judge=$BUNDLE/adapter" > "$OUT/vllm_4b.log" 2>&1 &
LORA_PID=$!
wait_ready "$LORA_PORT" "$LORA_PID" "$OUT/vllm_4b.log"
"$PYTHON" "$BUNDLE/runner/run_main_experiments.py" --bundle "$BUNDLE" --shard "$SHARD" --out "$OUT" \
    --base-url "http://127.0.0.1:$PORT/v1" --lora-base-url "http://127.0.0.1:$LORA_PORT/v1" --resume
