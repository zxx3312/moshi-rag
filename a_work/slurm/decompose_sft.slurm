#!/bin/bash
#SBATCH --job-name=b-decompose-sft
#SBATCH --partition=secondary,scavenger
#SBATCH --account=dilek-ic
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=64G
#SBATCH --gres=gpu:1
#SBATCH --constraint=H100|h100|A100|AE7763_100g_512G_A100|AE7763_100g_1T_L40S|h200|rtx6000b
#SBATCH --time=01:30:00
#SBATCH --output=a_work/slurm/logs/%x-%j.out
set -euo pipefail
cd "$SLURM_SUBMIT_DIR"
# Prefer the original JSON-constrained backend once the private install is complete.
if [[ -f .venv-decompose/.install-complete ]]; then
    export VLLM_ENV="$PWD/.venv-decompose" SCRIPT=a_work/decompose_sft.py
    export RESULT_GROUP=sft_decompose RUN_NAME=v1
    export EVAL_ARGS='--b-root /u/tianyu30/project/moshi-rag-b --export-dir a_work/sft_decomposed_v1'
    exec bash a_work/slurm/eval_judge.slurm
fi
export HF_HUB_OFFLINE=1 TOKENIZERS_PARALLELISM=false PYTHONUNBUFFERED=1
/u/tianyu30/.conda/envs/CS546/bin/python a_work/decompose_sft.py \
  --b-root /u/tianyu30/project/moshi-rag-b \
  --export-dir a_work/sft_decomposed_transformers_v1 \
  --out a_work/results/sft_decompose_transformers_v1 \
  --local-model /projects/illinois/eng/cs/dilek/xzhu81/hf_home/hub/models--Qwen--Qwen3-14B/snapshots/40c069824f4251a91eefaf281ebe4c544efd3e18
