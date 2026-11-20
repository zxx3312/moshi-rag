#!/bin/bash
#SBATCH --job-name=a-dev-sweep
#SBATCH --partition=scavenger,secondary
#SBATCH --account=dilek-ic
#SBATCH --qos=normal
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --gres=gpu:H100:1
#SBATCH --constraint=H100|h100
#SBATCH --time=00:45:00
#SBATCH --array=0-6%4
#SBATCH --output=a_work/slurm/logs/%x-%A_%a.out

set -euo pipefail
: "${SNAPSHOT_DIR:?Provide the absolute frozen snapshot directory}"
: "${SWEEP_RUN_NAME:?Provide a unique development run name}"
export RUN_NAME="${SWEEP_RUN_NAME}/case_${SLURM_ARRAY_TASK_ID}"
export RESULT_GROUP="parameter_sweeps"
export SCRIPT="${SNAPSHOT_DIR}/run_parameter_case.py"
export EVAL_ARGS="--case ${SLURM_ARRAY_TASK_ID}"
export GPU_UTIL=0.55 JUDGE_GPU_UTIL=0.30 JUDGE_BASE="Qwen/Qwen3-4B"
export JUDGE_VLLM_ARGS="--enable-lora --lora-modules judge=${SNAPSHOT_DIR}/adapter"
exec bash "${SNAPSHOT_DIR}/slurm/eval_judge.slurm"
