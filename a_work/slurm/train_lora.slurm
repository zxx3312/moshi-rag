#!/bin/bash
# Train the LoRA judge on one GPU (Qwen3-4B by default).
#
# Submit FROM THE REPOSITORY ROOT:
#     RUN_NAME=qwen3_4b_v1 sbatch a_work/slurm/train_lora.slurm
# Smoke test:
#     RUN_NAME=smoke TRAIN_ARGS="--max-train 40 --max-dev 20 --epochs 1" sbatch a_work/slurm/train_lora.slurm
# Overrides: RUN_NAME, TRAIN_ARGS, SCRIPT, SFT_DIR, VLLM_ENV, LORA_EXTRA, HF_HOME.
#
#SBATCH --job-name=a-train-lora
#SBATCH --partition=IllinoisComputes-GPU,secondary
#SBATCH --account=dilek-ic
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --gres=gpu:1
#SBATCH --constraint=AE7763_100g_512G_A100|A100|H100|h100
#SBATCH --time=03:00:00
#SBATCH --output=a_work/slurm/logs/%x-%j.out

set -euo pipefail

P=/projects/illinois/eng/cs/dilek/xzhu81
VLLM_ENV="${VLLM_ENV:-$P/envs/vllm}"
export PYTHONPATH="${LORA_EXTRA:-$P/envs/lora_extra}"  # peft and accelerate, kept apart from the vLLM env
export HF_HOME="${HF_HOME:-$P/hf_home}"
export HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1
RUN_NAME="${RUN_NAME:-$(date +%Y%m%d_%H%M%S)_job${SLURM_JOB_ID:-local}}"
SCRIPT="${SCRIPT:-a_work/train_lora_judge.py}"
SFT_DIR="${SFT_DIR:-a_work/results/inputs/sft_v0}"
OUT="a_work/results/lora/$RUN_NAME"

cd "${SLURM_SUBMIT_DIR:-$(pwd)}"
[[ -f "$SCRIPT" ]] || { echo "submit from the repository root" >&2; exit 2; }
echo "job ${SLURM_JOB_ID:-local} on $(hostname); repo @ $(git rev-parse --abbrev-ref HEAD) $(git rev-parse --short HEAD)"
nvidia-smi --query-gpu=name,memory.total --format=csv || true

read -r -a EXTRA <<< "${TRAIN_ARGS:-}"
"$VLLM_ENV/bin/python" "$SCRIPT" --train "$SFT_DIR/sft_train.jsonl" --dev "$SFT_DIR/sft_dev.jsonl" --out "$OUT" "${EXTRA[@]}"
