"""CPU-only execution/format gate for a completed debug smoke. Makes no model calls.

A passing gate means all expected policy runs executed and B can validate their logs. It does not
require high answer scores or resolve pending semantic mappings, and never selects a model/threshold.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def read_jsonl(path):
    return [json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def execution_inputs(manifest, shard):
    """Read only the selected smoke shard and require each planned policy to have executed once."""
    folder = Path(manifest["results"]) / f"shard_{shard:03d}"
    gpu = read_json(folder / "gpu.json")
    require("H100" in gpu.get("gpu", ""), "Smoke did not run on an H100")
    traces, logs = [], []
    policies = set(manifest["policies"])
    for index in manifest["shards"][shard]:
        selected = read_jsonl(manifest["questions"][index])
        expected = {(t["trace_id"], p) for t in selected for p in policies}
        executions = []
        question_logs = []
        for phase in ("main", "oracle"):
            parent = folder / f"q{index:03d}"
            require(read_json(parent / (phase + "_worker.json"))["state"] == "completed", "Smoke worker failed")
            require(read_json(parent / phase / "status.json")["state"] == "completed", "Worker output is incomplete")
            executions.extend(read_jsonl(parent / phase / "execution.jsonl"))
            question_logs.extend(read_jsonl(parent / phase / "policy_log.jsonl"))
        observed = [(r["trace_id"], r["policy"]) for r in executions]
        require(len(observed) == len(expected) and set(observed) == expected, "Missing or duplicate policy executions")
        require(all(r["state"] == "completed" for r in executions), "Policy execution did not complete")
        require({(r["trace_id"], r["policy"]) for r in question_logs} == expected, "Expected policy has no log output")
        traces.extend(selected)
        logs.extend(question_logs)
    return traces, logs, gpu


def evaluate(bundle, shard, out):
    manifest = read_json(bundle / "manifest.json")
    require(manifest["dataset"] == "debug", "Gate only accepts a debug bundle")
    for record in manifest["files"]:
        require(hashlib.sha256(Path(record["path"]).read_bytes()).hexdigest() == record["sha256"],
                "Frozen smoke input/code changed")
    traces, logs, gpu = execution_inputs(manifest, shard)
    out.mkdir(parents=True, exist_ok=False)
    trace_path, log_path = out / "traces.jsonl", out / "policy_log.jsonl"
    for path, rows in [(trace_path, traces), (log_path, logs)]:
        path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    command = [sys.executable, "-m", "b_work.eval.run_eval", "--traces", str(trace_path),
               "--gold", manifest["gold"], "--logs", str(log_path), "--timing-kind", "estimated",
               "--runner-commit", manifest["runner_parent_commit"], "--allow-value-match",
               "--aligned-policy", "evidence_aware+oracle", "--aligned-policy", "evidence_aware+oracle+concurrent",
               "--expected-policies", *manifest["policies"], "--out", str(out / "b_eval")]
    done = subprocess.run(command, cwd=bundle / "evaluator", capture_output=True, text=True)
    (out / "evaluator.log").write_text(done.stdout + done.stderr, encoding="utf-8")
    require(done.returncode == 0, "B log validation/scoring failed")
    require(not read_jsonl(out / "b_eval/validation_issues.jsonl"), "B found invalid log rows")
    scores = read_jsonl(out / "b_eval/run_scores.jsonl")
    expected = {(t["trace_id"], p) for t in traces for p in manifest["policies"]}
    require(len(scores) == len(expected) and {(r["trace_id"], r["policy"]) for r in scores} == expected,
            "B expected-run accounting differs")
    require(all(r["status"] == "ok" for r in scores), "Missing or invalid scored runs")
    summary = {"passed": True, "scope": "execution_and_log_validation_only", "trace_count": len(traces),
               "policy_runs": len(scores), "gpu": gpu, "semantic_quality_approved": False,
               "claims_pending_review": sum(r["claims_needing_review"] for r in scores),
               "bundle_sha256": hashlib.sha256((bundle / "manifest.json").read_bytes()).hexdigest()}
    (out / "gate_passed.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--shard", type=int, default=0)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    evaluate(args.bundle.resolve(), args.shard, args.out.resolve())


if __name__ == "__main__":
    main()
