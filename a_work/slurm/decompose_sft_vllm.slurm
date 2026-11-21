#!/bin/bash
#SBATCH --job-name=b-decompose-vllm
#SBATCH --partition=secondary,scavenger
#SBATCH --account=dilek-ic
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=64G
#SBATCH --gres=gpu:1
#SBATCH --constraint=H100|h100|A100|AE7763_100g_512G_A100|h200|rtx6000b
#SBATCH --time=00:45:00
#SBATCH --output=a_work/slurm/logs/%x-%j.out
set -euo pipefail
cd "$SLURM_SUBMIT_DIR"
export VLLM_ENV="$PWD/.venv-decompose"
[[ -f "$VLLM_ENV/.install-complete" ]] || { echo 'Independent vLLM environment is not ready' >&2; exit 2; }
export SCRIPT=a_work/decompose_sft.py RESULT_GROUP=sft_decompose
export RUN_NAME="vllm_${SLURM_JOB_ID}"
export EVAL_ARGS='--b-root /u/tianyu30/project/moshi-rag-b --export-dir a_work/sft_decomposed_v1'
# No fallback backend: keep decoding and JSON constraints consistent with A.
exec bash a_work/slurm/eval_judge.slurm
