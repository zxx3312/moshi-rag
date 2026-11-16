"""Run a frozen main-experiment shard, with ordinary and Oracle work in separate processes.

Only --worker --phase oracle accepts --gold. Ordinary policies receive public traces and question-only
units. Existing prompts, policy thresholds and replay timing are reused without modification.
Each question is checkpointed; a watchdog records failures instead of hanging an entire Slurm shard.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from turntaking.decompose import decompose
from turntaking.generate import Generator
from turntaking.judge import OracleJudge, PromptJudge
from turntaking.llm import ChatClient
from turntaking.policies import EvidenceAware, FirstEvidence, FixedProgress, TimeOnly, WaitAll
from turntaking.replay import load_jsonl, replay, units_without_gold, write_jsonl

MAIN_POLICIES = ["wait_all", "fixed_progress", "time_only", "first_evidence",
                 "evidence_aware+prompt_real", "evidence_aware+prompt_real+concurrent",
                 "evidence_aware+lora_real", "evidence_aware+lora_real+concurrent"]
ORACLE_POLICIES = ["evidence_aware+oracle", "evidence_aware+oracle+concurrent"]
POLICIES = MAIN_POLICIES + ORACLE_POLICIES


def save_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    temporary.replace(path)


def verify_bundle(bundle):
    manifest = json.loads((bundle / "manifest.json").read_text(encoding="utf-8"))
    for item in manifest["files"]:
        path = Path(item["path"])
        if hashlib.sha256(path.read_bytes()).hexdigest() != item["sha256"]:
            raise ValueError("Frozen input/code/checkpoint changed: " + str(path))
    return manifest


def worker(args):
    if args.phase == "main" and args.gold is not None:
        raise ValueError("Ordinary policy workers must not receive --gold")
    if args.phase == "oracle" and args.gold is None:
        raise ValueError("Oracle requires its separate --gold input")
    traces = load_jsonl(args.trace)
    if not traces or len({t["sample_id"] for t in traces}) != 1:
        raise ValueError("A worker needs all schedules of exactly one question")
    args.out.mkdir(parents=True, exist_ok=False)
    shared = dict(max_tokens=1024, extra_body={"chat_template_kwargs": {"enable_thinking": False}})
    client = ChatClient(args.base_url, "Qwen/Qwen3-14B", **shared)
    clients, judges = [client], []
    generator = Generator(client)
    ledger, logs = [], []
    started = time.time()
    status = {"phase": args.phase, "sample_id": traces[0]["sample_id"], "state": "running"}
    save_json(args.out / "status.json", status)
    try:
        if args.phase == "main":
            _, units, fallback = decompose(traces[0]["question"], client)
            setup = sum(call.latency_s for call in client.calls)
            save_json(args.out / "decomposition.json", {
                "latency_s": setup, "fell_back": fallback,
                "units": [vars(unit) for unit in units]})
            lora_client = ChatClient(args.lora_base_url, "judge", **shared)
            clients.append(lora_client)
            prompt = PromptJudge(client, with_examples=True, name="prompt")
            lora = PromptJudge(lora_client, with_examples=False, name="lora")
            judges = [prompt, lora]
            # Baselines have no gold units. Generator.free reads only question and visible evidence.
            runs = [(policy, [], 0.0, False) for policy in
                    [WaitAll(), FixedProgress(), TimeOnly(), FirstEvidence()]]
            for name, judge in [("prompt", prompt), ("lora", lora)]:
                base = "evidence_aware+" + name + "_real"
                runs.extend((EvidenceAware(judge, name=base + suffix), units, setup, concurrent)
                            for suffix, concurrent in [("", False), ("+concurrent", True)])
        else:
            golds = {g["sample_id"]: g for g in load_jsonl(args.gold)}
            gold = golds[traces[0]["sample_id"]]
            judge = OracleJudge([gold])
            runs = [(EvidenceAware(judge, name=name), units_without_gold(gold), 0.0, name.endswith("+concurrent"))
                    for name in ORACLE_POLICIES]
        for trace in traces:
            for policy, policy_units, setup_cost, concurrent in runs:
                current = {"trace_id": trace["trace_id"], "policy": policy.name, "state": "running"}
                ledger.append(current)
                write_jsonl(args.out / "execution.jsonl", ledger)
                tick_started = time.monotonic()
                records = replay(trace, policy_units, policy, setup_cost_s=setup_cost,
                                 generator=generator, concurrent=concurrent)
                logs.extend(records)
                write_jsonl(args.out / "policy_log.jsonl", logs)
                current.update(state="completed", records=len(records), wall_s=time.monotonic() - tick_started)
                write_jsonl(args.out / "execution.jsonl", ledger)
                # A completed policy remains auditable if a later request or worker times out.
                write_jsonl(args.out / "llm_calls.jsonl", [row for c in clients for row in c.tape])
        status["state"] = "completed"
    except Exception as error:
        status.update(state="failed", error_type=type(error).__name__)
        (args.out / "error.txt").write_text(traceback.format_exc(), encoding="utf-8")
        raise
    finally:
        write_jsonl(args.out / "llm_calls.jsonl", [row for c in clients for row in c.tape])
        write_jsonl(args.out / "generate_calls.jsonl", generator.log)
        write_jsonl(args.out / "judge_calls.jsonl", [row for j in judges for row in j.log])
        status.update(wall_s=time.time() - started, finished_runs=sum(r["state"] == "completed" for r in ledger))
        save_json(args.out / "status.json", status)


def run_shard(args):
    manifest = verify_bundle(args.bundle)
    if not 0 <= args.shard < len(manifest["shards"]):
        raise ValueError("Shard index out of range")
    if args.out.exists() and not args.resume:
        raise ValueError("Output exists; use --resume to retain completed/failed attempts")
    args.out.mkdir(parents=True, exist_ok=True)
    manifest_hash = hashlib.sha256((args.bundle / "manifest.json").read_bytes()).hexdigest()
    identity_path = args.out / "run_config.json"
    if identity_path.exists():
        prior = json.loads(identity_path.read_text(encoding="utf-8"))
        if (prior["bundle_sha256"], prior["shard"]) != (manifest_hash, args.shard):
            raise ValueError("Resume output belongs to another bundle or shard")
    save_json(identity_path, {"bundle": str(args.bundle), "bundle_sha256": manifest_hash,
                             "shard": args.shard, "policies": POLICIES, "timing_kind": "estimated",
                             "job_id": os.environ.get("SLURM_JOB_ID"), "seed": 0})
    counts = {"completed": 0, "failed": 0}
    for index in manifest["shards"][args.shard]:
        for phase in ("main", "oracle"):
            out = args.out / f"q{index:03d}" / phase
            marker = out.parent / (phase + "_worker.json")
            # A failed attempt is preserved and counted, not silently rerun until it succeeds.
            if marker.exists():
                state = json.loads(marker.read_text(encoding="utf-8"))["state"]
                counts["completed" if state == "completed" else "failed"] += 1
                continue
            if out.exists():
                save_json(marker, {"state": "interrupted", "reason": "Previous worker has no completion marker"})
                counts["failed"] += 1
                continue
            command = [sys.executable, str(Path(__file__).resolve()), "--worker", "--phase", phase,
                       "--trace", manifest["questions"][index], "--out", str(out),
                       "--base-url", args.base_url, "--lora-base-url", args.lora_base_url]
            if phase == "oracle":
                command.extend(["--gold", manifest["gold"]])
            out.parent.mkdir(parents=True, exist_ok=True)
            start = time.time()
            with (out.parent / (phase + "_worker.log")).open("w", encoding="utf-8") as log:
                try:
                    done = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT, timeout=args.worker_timeout_s)
                    result = {"state": "completed" if done.returncode == 0 else "failed", "exit_code": done.returncode}
                except subprocess.TimeoutExpired:
                    result = {"state": "timeout", "exit_code": None}
            result.update(wall_s=time.time() - start, question_index=index, phase=phase)
            save_json(marker, result)
            counts["completed" if result["state"] == "completed" else "failed"] += 1
            print(json.dumps({"question_index": index, "phase": phase, **result}), flush=True)
    save_json(args.out / "shard_status.json", counts)
    return int(counts["failed"] > 0)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path)
    parser.add_argument("--shard", type=int)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--base-url", default="http://127.0.0.1:8000/v1")
    parser.add_argument("--lora-base-url", default="http://127.0.0.1:8001/v1")
    parser.add_argument("--worker-timeout-s", type=float, default=1800.0)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--worker", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--phase", choices=["main", "oracle"])
    parser.add_argument("--trace", type=Path)
    parser.add_argument("--gold", type=Path)
    args = parser.parse_args()
    if args.worker:
        if not args.phase or not args.trace:
            parser.error("Worker requires --phase and --trace")
        worker(args)
        return 0
    if args.bundle is None or args.shard is None or args.gold is not None:
        parser.error("A shard needs --bundle and --shard; --gold is Oracle-worker only")
    if args.worker_timeout_s <= 0:
        parser.error("--worker-timeout-s must be positive")
    return run_shard(args)


if __name__ == "__main__":
    sys.exit(main())
