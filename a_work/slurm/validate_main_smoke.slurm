#!/bin/bash
# Submit with --dependency=afterok:SMOKE_JOB. An afterok dependency on this gate releases main work.
#SBATCH --job-name=a-validate-smoke
#SBATCH --account=dilek-ic
#SBATCH --partition=scavenger,secondary
#SBATCH --qos=normal
#SBATCH --nice=0
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --time=00:05:00
#SBATCH --output=a_work/slurm/logs/%x-%j.out
#SBATCH --no-requeue
set -euo pipefail
cd "${SLURM_SUBMIT_DIR:?Submit from repository root}"
GATE="${1:?Pass frozen gate Python file}"
BUNDLE="${2:?Pass debug bundle}"
OUT="${3:?Pass a new validation output directory}"
EXPECTED_HASH="${4:?Pass SHA256 of frozen gate Python file}"
python3 - "$GATE" "$EXPECTED_HASH" <<'PY'
import hashlib,pathlib,sys
if hashlib.sha256(pathlib.Path(sys.argv[1]).read_bytes()).hexdigest()!=sys.argv[2]:
    raise SystemExit('Frozen gate code changed')
PY
python3 "$GATE" --bundle "$BUNDLE" --shard 0 --out "$OUT"
