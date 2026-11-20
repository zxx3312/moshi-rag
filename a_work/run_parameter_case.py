"""Run and score one frozen development-set parameter configuration."""
import argparse
import json
from pathlib import Path
import subprocess
import sys


CASES = (
    ("baseline", 3.0, 1.0, 3.0),
    ("time_1", 1.0, 1.0, 3.0),
    ("time_5", 5.0, 1.0, 3.0),
    ("fixed_3", 3.0, 3.0, 3.0),
    ("fixed_5", 3.0, 5.0, 3.0),
    ("evidence_1", 3.0, 1.0, 1.0),
    ("evidence_5", 3.0, 1.0, 5.0),
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--judge-base-url", required=True)
    parser.add_argument("--case", type=int, choices=range(len(CASES)), required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    snapshot = Path(__file__).resolve().parent
    repo = snapshot.parents[3]
    name, time_only, fixed_progress, evidence_progress = CASES[args.case]
    replay_dir = args.out / "replay"
    args.out.mkdir(parents=True, exist_ok=True)
    case_config = dict(name=name, case=args.case, time_only_at_s=time_only,
                       fixed_progress_at_s=fixed_progress, evidence_progress_after_s=evidence_progress)
    (args.out / "case.json").write_text(json.dumps(case_config, indent=2) + "\n")

    command = [sys.executable, str(snapshot / "run_replay.py"),
               "--trace", str(snapshot / "inputs" / "traces_debug.jsonl"),
               "--gold", str(snapshot / "inputs" / "gold_debug.jsonl"),
               "--base-url", args.base_url, "--model", args.model, "--judge-base-url", args.judge_base_url,
               "--judge-model", "judge", "--judge-name", "lora", "--no-examples", "--generate", "--concurrent",
               "--time-only-at-s", str(time_only), "--fixed-progress-at-s", str(fixed_progress),
               "--evidence-progress-after-s", str(evidence_progress), "--out", str(replay_dir)]
    with (args.out / "replay.log").open("w") as log:
        subprocess.run(command, stdout=log, stderr=subprocess.STDOUT, check=True)

    rows = [json.loads(line) for line in (replay_dir / "trace_metrics.jsonl").read_text().splitlines()]
    if len(rows) != 600 or len({(r["trace_id"], r["policy"]) for r in rows}) != 600:
        raise ValueError(f"Expected 600 unique trace-policy runs, got {len(rows)}")
    calls = [json.loads(line) for line in (replay_dir / "judge_calls.jsonl").read_text().splitlines()]
    errors = [row for row in calls if row.get("error")]
    if errors:
        raise ValueError(f"{len(errors)} judge calls failed; see judge_calls.jsonl")
    score = [sys.executable, str(snapshot / "eval_with_b.py"), str(replay_dir), "--repo", str(repo),
             "--ref", "ea390574eadd301354d5de46f0d28d328cca5bad"]
    with (args.out / "b_eval.log").open("w") as log:
        subprocess.run(score, stdout=log, stderr=subprocess.STDOUT, check=True)
    scores = [json.loads(line) for line in (replay_dir / "b_eval" / "run_scores.jsonl").read_text().splitlines()]
    if len(scores) != 600 or any(row["status"] != "ok" for row in scores):
        raise ValueError("B evaluator did not return 600 valid scored runs")
    (args.out / "complete.json").write_text(json.dumps(dict(case_config, runs=len(rows),
                                                            judge_calls=len(calls), judge_errors=0,
                                                            b_eval_exit=0), indent=2) + "\n")


if __name__ == "__main__":
    main()
