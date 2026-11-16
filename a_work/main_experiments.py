"""Prepare, verify and score a frozen experiment bundle. No model calls or live job submissions.

    python3 a_work/main_experiments.py prepare --name main_eval_revised_v1
    python3 a_work/main_experiments.py command --bundle BUNDLE --test-only
    python3 a_work/main_experiments.py collect --bundle BUNDLE --out ANALYSIS_DIR

The command subcommand prints the live sbatch command; --test-only asks Slurm to validate it without
creating a job. Preparing eval data requires explicit user authorization; use debug for development.
"""
import argparse
from collections import Counter, defaultdict
import hashlib
import importlib.util
import io
import json
import math
from pathlib import Path
import re
import shlex
import statistics
import subprocess
import sys
import tarfile
import tempfile

from run_main_experiments import POLICIES, save_json, verify_bundle

REPO = Path(__file__).resolve().parents[1]
TRACE_DIR = "b_work/test_set/traces/eval_revised_v1"
REVISIONS = ["batch01_05_v1", "batch06_10_v1"]
SCHEDULES = {"immediate": [0.0], "short": [1.0, 3.0], "long": [2.0, 8.0]}
TRACE_KEYS = {"schema_version", "data_version", "sample_id", "trace_id", "trace_type", "time_origin",
              "clock", "question", "events", "retrieval_complete_time_s"}
EVENT_KEYS = {"evidence_id", "scheduled_time_s", "visible_time_s", "source", "text"}


def git(*args):
    return subprocess.check_output(["git", *args], cwd=REPO)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def jsonl(data):
    return [json.loads(line) for line in data.splitlines() if line.strip()]


def check(condition, message):
    if not condition:
        raise ValueError(message)


def inspect_data(traces, golds, schedules, records_module):
    """Structural checks only. Never print or use question content to change model behavior."""
    trace_index, gold_index = records_module.prepare_inputs(traces, golds)
    check(set(gold_index) == {t["sample_id"] for t in traces}, "Gold/trace coverage differs")
    check(schedules == SCHEDULES, "Schedules differ from current experiment spec")
    groups = defaultdict(dict)
    for trace in traces:
        check(set(trace) == TRACE_KEYS, "Unexpected trace fields; reject possible gold leakage")
        check(trace["trace_type"] == "controlled_mock" and trace["clock"] == "simulated", "Unexpected trace clock/type")
        schedule = trace["trace_id"].rsplit("_", 1)[-1]
        check(schedule in schedules, "Unknown schedule")
        sid = trace["sample_id"]
        check(schedule not in groups[sid], "Duplicate schedule for a question")
        groups[sid][schedule] = trace
        document_times = {}
        last = 0.0
        for event in trace["events"]:
            check(set(event) == EVENT_KEYS, "Unexpected evidence fields")
            # The builder preserves every source sentence, including blank ones. Count them, never trim them.
            check(isinstance(event["text"], str), "Evidence text is not a string")
            when = event["visible_time_s"]
            check(type(when) in (int, float) and math.isfinite(when) and when in schedules[schedule], "Invalid arrival time")
            check(event["scheduled_time_s"] == when, "Scheduled/visible times differ")
            source = event["source"]
            check(isinstance(source, dict) and isinstance(source.get("document_id"), str), "Missing document title")
            check(set(source) == {"dataset", "document_id", "document_index", "sentence_index"},
                  "Unexpected source fields; reject possible gold leakage")
            document = (source.get("dataset"), source.get("document_index"), source["document_id"])
            check(document_times.setdefault(document, when) == when, "Document split across arrivals")
            last = max(last, when)
        check(trace["events"] and trace["retrieval_complete_time_s"] == last, "Invalid retrieval completion")
    for by_schedule in groups.values():
        check(set(by_schedule) == set(schedules), "Question does not have all three schedules")
        content = []
        for trace in by_schedule.values():
            content.append({e["evidence_id"]: (e["text"], e["source"]) for e in trace["events"]})
        check(all(value == content[0] for value in content), "Evidence content differs across schedules")
    units = [u for g in golds for u in g["units"]]
    return {"passed": True, "questions": len(groups), "traces": len(trace_index), "gold_units": len(units),
            "events": sum(len(t["events"]) for t in traces),
            "by_schedule": dict(Counter(t["trace_id"].rsplit("_", 1)[-1] for t in traces)),
            "question_types": dict(Counter(g.get("question_type", "unknown") for g in golds)),
            "source_types": dict(Counter(g.get("source_type", "unknown") for g in golds)),
            "omission_units": sum(u.get("by_omission", False) for u in units),
            "presupposition_units": sum(u.get("by_presupposition", False) for u in units),
            "presupposition_path_units": sum(bool(u.get("presupposition_sets")) for u in units),
            "both_flags_units": sum(u.get("by_omission", False) and u.get("by_presupposition", False) for u in units),
            "event_count_min": min(len(t["events"]) for t in traces),
            "event_count_max": max(len(t["events"]) for t in traces),
            "blank_evidence_events": sum(not e["text"].strip() for t in traces for e in t["events"]),
            "schedules": schedules, "cross_schedule_content_identical": True,
            "whole_document_arrivals": True, "no_gold_fields_in_public_trace": True}


def prepare(args):
    check(bool(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", args.name)), "Unsafe run name")
    check(args.shards > 0, "Shard count must be positive")
    source_commit = git("rev-parse", args.ref).decode().strip()
    code_commit = git("rev-parse", "HEAD").decode().strip()
    inputs = REPO / "a_work/results/inputs" / args.name
    bundle = REPO / "a_work/results/code_snapshots" / args.name
    check(not inputs.exists() and not bundle.exists(), "Bundle/input name already exists; use a new name")
    check(args.adapter.is_dir(), "LoRA adapter directory does not exist")
    source_paths = ([TRACE_DIR + "/traces.jsonl"] +
                    ["b_work/test_set/revisions/" + r + "/gold.jsonl" for r in REVISIONS]
                    if args.dataset == "eval-revised-v1" else
                    ["b_work/step3/traces_debug.jsonl", "b_work/step3/gold_debug.jsonl"])
    raw = {p: git("show", source_commit + ":" + p) for p in source_paths}
    traces = jsonl(raw[source_paths[0]])
    golds = [row for p in source_paths[1:] for row in jsonl(raw[p])]
    schedules = (json.loads(git("show", source_commit + ":" + TRACE_DIR + "/schedules.json"))
                 if args.dataset == "eval-revised-v1" else SCHEDULES)
    # Import just B's stdlib validator; never check out B's dataset tree.
    with tempfile.TemporaryDirectory() as temporary:
        path = Path(temporary) / "records.py"
        path.write_bytes(git("show", source_commit + ":b_work/eval/records.py"))
        spec = importlib.util.spec_from_file_location("frozen_b_records", path)
        records_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(records_module)
        report = inspect_data(traces, golds, schedules, records_module)
    if args.dataset == "eval-revised-v1":
        check((report["questions"], report["traces"], report["gold_units"]) == (300, 900, 817), "Revised data counts changed")
        upstream = json.loads(git("show", source_commit + ":" + TRACE_DIR + "/manifest.json"))
    else:
        check((report["questions"], report["traces"]) == (20, 60), "Debug counts changed")
        upstream = {"status": "debug_only"}
    inputs.mkdir(parents=True)
    bundle.mkdir(parents=True)
    files = []

    def record(path, data, source=None):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        files.append({"path": str(path), "sha256": digest(data), **({"source": source} if source else {})})

    public_trace = inputs / "public/traces.jsonl"
    record(public_trace, raw[source_paths[0]], source_paths[0])
    for n, path in enumerate(source_paths[1:]):
        record(inputs / f"private/source_gold_{n}.jsonl", raw[path], path)
    gold_path = inputs / "private/gold.jsonl"
    record(gold_path, b"".join(raw[p].rstrip() + b"\n" for p in source_paths[1:]))
    grouped = defaultdict(list)
    for trace in traces:
        grouped[trace["sample_id"]].append(trace)
    questions = []
    for n, rows in enumerate(grouped.values()):
        path = inputs / f"public/questions/{n:03d}.jsonl"
        record(path, b"".join((json.dumps(r, ensure_ascii=False) + "\n").encode() for r in rows))
        questions.append(str(path))
    n_shards = min(args.shards, len(questions))
    shards = [list(range(i, len(questions), n_shards)) for i in range(n_shards)]
    sources = [REPO / "a_work" / f for f in ["run_main_experiments.py", "main_experiments.py"]]
    sources += sorted((REPO / "a_work/turntaking").glob("*.py"))
    sources += [REPO / "a_work/slurm/main_experiments.slurm"]
    for path in sources:
        record(bundle / "runner" / path.relative_to(REPO / "a_work"), path.read_bytes(), str(path.relative_to(REPO)))
    adapter_files = [args.adapter / "adapter_config.json", args.adapter / "adapter_model.safetensors"]
    for path in adapter_files:
        record(bundle / "adapter" / path.name, path.read_bytes(), str(path.resolve()))
    archive = git("archive", source_commit, "b_work/eval")
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        for member in tar.getmembers():
            if member.isfile():
                record(bundle / "evaluator" / member.name, tar.extractfile(member).read(), member.name)
    # Recheck the current A implementation against the pinned B support rules without any model call.
    oracle_check = '''
import json,sys
from b_work.eval.records import prepare_inputs,read_jsonl
from b_work.eval.score import supported_units,citation_support
sys.path.insert(0,sys.argv[3])
from turntaking.judge import OracleJudge
from turntaking.schema import Evidence,Observation,SUPPORTED
from turntaking.replay import units_without_gold
traces,golds=read_jsonl(sys.argv[1]),read_jsonl(sys.argv[2])
_,by_id=prepare_inputs(traces,golds)
judge=OracleJudge(golds)
counts=dict(snapshots=0,unit_comparisons=0,supported_citations=0,unresolved_optional_trace_units_at_full=0)
unresolved_optional=set()
for trace in traces:
    gold=by_id[trace['sample_id']]
    units={u['unit_id']:u for u in gold['units']}
    times=sorted({0.0}|{e['visible_time_s'] for e in trace['events']})
    for t in times:
        evidence=tuple(Evidence(e['evidence_id'],e['text'],e['visible_time_s'],e['source'])
                       for e in trace['events'] if e['visible_time_s']<=t)
        obs=Observation(trace['sample_id'],trace['question'],t,evidence,tuple(units_without_gold(gold)),
                        t>=trace['retrieval_complete_time_s'])
        labels=judge.judge(obs)
        visible={e.evidence_id for e in evidence}
        supported=supported_units(units,visible)
        if supported!={uid for uid,j in labels.items() if j.label==SUPPORTED}:
            raise ValueError('A/B support disagreement')
        counts['snapshots']+=1
        counts['unit_comparisons']+=len(units)
        for uid in supported:
            if not citation_support(uid,units,visible,set(labels[uid].citations)):
                raise ValueError('Oracle citation disagreement')
            counts['supported_citations']+=1
    if not all(uid in supported for uid,u in units.items() if u['necessary']):
        raise ValueError('Necessary unit unsupported at full context')
    counts['unresolved_optional_trace_units_at_full']+=sum(uid not in supported and not u['necessary'] for uid,u in units.items())
    unresolved_optional.update((trace['sample_id'],uid) for uid,u in units.items() if uid not in supported and not u['necessary'])
counts['unresolved_optional_units_at_full']=len(unresolved_optional)
counts['passed']=True
print(json.dumps(counts))
'''
    compatibility = subprocess.check_output([sys.executable, "-c", oracle_check, str(public_trace),
                                            str(gold_path), str(bundle / "runner")],
                                           cwd=bundle / "evaluator", text=True)
    report["oracle_compatibility"] = json.loads(compatibility)
    record(inputs / "audit.json", (json.dumps(report, indent=2) + "\n").encode())
    manifest = {"name": args.name, "dataset": args.dataset, "state": "prepared_not_submitted",
                "source_commit": source_commit, "runner_parent_commit": code_commit,
                "runner_branch": git("branch", "--show-current").decode().strip(),
                "runner_dirty": bool(git("status", "--porcelain")),
                "trace": str(public_trace), "gold": str(gold_path), "questions": questions,
                "shards": shards, "policies": POLICIES, "expected_policy_runs": len(traces) * len(POLICIES),
                "timing_kind": "estimated", "seed": 0,
                "results": str(REPO / "a_work/results/replay" / args.name),
                "audit": report, "upstream_status": upstream,
                "files": files}
    save_json(bundle / "manifest.json", manifest)
    verify_bundle(bundle)
    print(json.dumps({"bundle": str(bundle), "audit": report, "shards": n_shards,
                      "expected_policy_runs": manifest["expected_policy_runs"], "state": manifest["state"]}, indent=2))


def submission_command(bundle, manifest, concurrency):
    check(concurrency > 0, "Array concurrency must be positive")
    return ["sbatch", "--parsable", "--account=dilek-ic", "--qos=normal", "--nice=0",
            "--partition=scavenger,secondary", "--gres=gpu:H100:1", "--constraint=H100|h100",
            f"--array=0-{len(manifest['shards']) - 1}%{concurrency}",
            str(bundle / "runner/slurm/main_experiments.slurm"), str(bundle)]


def command(args):
    manifest = verify_bundle(args.bundle)
    cmd = submission_command(args.bundle, manifest, args.concurrency)
    (REPO / "a_work/slurm/logs").mkdir(parents=True, exist_ok=True)
    print(shlex.join(cmd), flush=True)
    if args.test_only:
        test_command = [cmd[0], "--test-only", *[arg for arg in cmd[1:] if arg != "--parsable"]]
        done = subprocess.run(test_command, cwd=REPO, capture_output=True, text=True)
        save_json(args.bundle / "slurm_test.json", {"mode": "test_only_no_submission", "command": test_command, "exit_code": done.returncode,
                                                  "stdout": done.stdout, "stderr": done.stderr})
        print(done.stdout + done.stderr)
        return done.returncode
    return 0


def paired_times(scores):
    by_key = {(r["trace_id"], r["policy"]): r for r in scores}
    result = []
    for policy in POLICIES:
        if policy == "wait_all":
            continue
        for schedule in SCHEDULES:
            rows = [r for r in scores if r["policy"] == policy and r["trace_id"].endswith("_" + schedule)]
            for metric in ("ttfgi_s", "ttca_s"):
                diffs = []
                for row in rows:
                    wait = by_key.get((row["trace_id"], "wait_all"))
                    if wait and row["status"] == "ok" and wait["status"] == "ok":
                        if row.get(metric) is not None and wait.get(metric) is not None:
                            diffs.append(wait[metric] - row[metric])
                result.append({"policy": policy, "schedule": schedule, "metric": metric,
                               "expected_traces": len(rows), "pairs": len(diffs),
                               "median_earlier_s": statistics.median(diffs) if diffs else None,
                               "earlier_pairs": sum(d > 0 for d in diffs)})
    return result


def collect(args):
    manifest = verify_bundle(args.bundle)
    check(not args.out.exists(), "Analysis output exists; use a new --out to preserve old scores")
    logs, workers, hardware = [], [], []
    for shard in range(len(manifest["shards"])):
        folder = Path(manifest["results"]) / f"shard_{shard:03d}"
        gpu = folder / "gpu.json"
        if gpu.exists():
            hardware.append(json.loads(gpu.read_text()))
        for index in manifest["shards"][shard]:
            for phase in ("main", "oracle"):
                out = folder / f"q{index:03d}" / phase
                marker = out.parent / (phase + "_worker.json")
                row = {"shard": shard, "question_index": index, "phase": phase,
                       "state": "interrupted" if out.exists() else "missing"}
                if marker.exists():
                    row.update(json.loads(marker.read_text()))
                workers.append(row)
                if (out / "policy_log.jsonl").exists():
                    logs.extend(jsonl((out / "policy_log.jsonl").read_bytes()))
    signatures = {json.dumps(g.get("gpu"), sort_keys=True) for g in hardware}
    check(len(signatures) <= 1, "Different GPU variants detected; score hardware strata separately")
    run_ids = defaultdict(set)
    for row in logs:
        run_ids[(row["trace_id"], row["policy"])].add(row["run_id"])
    check(all(len(ids) == 1 for ids in run_ids.values()), "Multiple attempts found for one trace/policy")
    args.out.mkdir(parents=True)
    merged = args.out / "policy_log.jsonl"
    merged.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in logs), encoding="utf-8")
    b_out = args.out / "b_eval"
    cmd = [sys.executable, "-m", "b_work.eval.run_eval", "--logs", str(merged),
           "--traces", manifest["trace"], "--gold", manifest["gold"], "--timing-kind", "estimated",
           "--runner-commit", manifest["runner_parent_commit"], "--allow-value-match",
           "--aligned-policy", "evidence_aware+oracle", "--aligned-policy", "evidence_aware+oracle+concurrent",
           "--expected-policies", *POLICIES, "--out", str(b_out)]
    done = subprocess.run(cmd, cwd=args.bundle / "evaluator", capture_output=True, text=True)
    (args.out / "evaluator.log").write_text(done.stdout + done.stderr, encoding="utf-8")
    if done.returncode not in (0, 1):
        raise RuntimeError("B scoring failed; see evaluator.log")
    scores = jsonl((b_out / "run_scores.jsonl").read_bytes())
    check(len(scores) == manifest["expected_policy_runs"], "Missing expected run accounting")
    save_json(args.out / "paired_latency.json", paired_times(scores))
    save_json(args.out / "execution_inventory.json", workers)
    save_json(args.out / "manifest.json", {"bundle": str(args.bundle),
        "bundle_sha256": digest((args.bundle / "manifest.json").read_bytes()),
        "source_commit": manifest["source_commit"], "runner_parent_commit": manifest["runner_parent_commit"],
        "evaluator_exit_code": done.returncode, "worker_statuses": dict(Counter(r["state"] for r in workers)),
        "policy_log_sha256": digest(merged.read_bytes()), "expected_policy_runs": len(scores), "hardware": hardware})
    print(json.dumps({"out": str(args.out), "scored_or_missing_runs": len(scores),
                      "worker_statuses": dict(Counter(r["state"] for r in workers)),
                      "evaluator_exit_code": done.returncode}, indent=2))
    return done.returncode


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="action", required=True)
    p = sub.add_parser("prepare")
    p.add_argument("--name", required=True)
    p.add_argument("--dataset", choices=["eval-revised-v1", "debug"], default="eval-revised-v1")
    p.add_argument("--ref", default="origin/b-data-eval")
    p.add_argument("--shards", type=int, default=30)
    p.add_argument("--adapter", type=Path, default=REPO / "a_work/results/lora/qwen3_4b_v1/best")
    p = sub.add_parser("verify")
    p.add_argument("--bundle", type=Path, required=True)
    p = sub.add_parser("command")
    p.add_argument("--bundle", type=Path, required=True)
    p.add_argument("--concurrency", type=int, default=2)
    p.add_argument("--test-only", action="store_true")
    p = sub.add_parser("collect")
    p.add_argument("--bundle", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if getattr(args, "bundle", None):
        args.bundle = args.bundle.resolve()
    if getattr(args, "out", None):
        args.out = args.out.resolve()
    if args.action == "verify":
        manifest = verify_bundle(args.bundle)
        print(json.dumps({"verified": True, "name": manifest["name"], "files": len(manifest["files"])}))
        return 0
    return {"prepare": prepare, "command": command, "collect": collect}[args.action](args) or 0


if __name__ == "__main__":
    sys.exit(main())
