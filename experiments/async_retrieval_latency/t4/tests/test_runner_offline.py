"""Stdlib-level checks of the T4 runner's bookkeeping (no torch, no GPU).

    python experiments/async_retrieval_latency/t4/tests/test_runner_offline.py
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
import tempfile
from pathlib import Path

T4_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(T4_DIR))

import run_latency_sweep_t4 as t4  # noqa: E402


def test_completed_and_repair() -> None:
    with tempfile.TemporaryDirectory() as d:
        run_dir = Path(d)
        path = run_dir / "results.jsonl"
        lines = [json.dumps({"run_id": "a", "status": "ok"}), json.dumps({"run_id": "b", "status": "timeout"}),
                 '{"run_id": "c", "stat']  # last line cut off by a disconnect
        path.write_text("\n".join(lines) + "\n")
        done, info = t4.completed(run_dir, retry_failed=False, apply=False)
        assert done == {"a", "b"} and info["corrupt_lines_dropped"] == 1, (done, info)
        assert path.read_text().count("\n") == 3, "apply=False must not touch the file"
        done, info = t4.completed(run_dir, retry_failed=True, apply=True)
        assert done == {"a"} and info["failed_to_retry"] == 1, (done, info)
        assert [json.loads(x)["run_id"] for x in path.read_text().splitlines()] == ["a"]
    print("  ok: resume skips completed runs, drops a truncated line, --retry-failed reruns failures")


def test_fingerprint_mismatch() -> None:
    old = {"args": {"dtype": "float16", "no_q8": False}, "samples": {"s1": {"wav_sha256": "x", "reference_sha256": "y"}}}
    same = {"args": {"dtype": "float16", "no_q8": False},
            "samples": {"s1": {"wav_sha256": "x", "reference_sha256": "y"}, "s2": {"wav_sha256": "z", "reference_sha256": "w"}}}
    changed = {"args": {"dtype": "float16", "no_q8": True}, "samples": {"s1": {"wav_sha256": "x", "reference_sha256": "CHANGED"}}}
    assert t4.check_fingerprint(old, same) == []
    problems = t4.check_fingerprint(old, changed)
    assert len(problems) == 2, problems
    print("  ok: resume accepts added samples/delays, rejects changed settings or changed sample content")


def test_null_stt() -> None:
    async def run() -> list:
        stt = t4.NullSTT()
        await stt.start_up()
        got = []

        async def consume():
            async for msg in stt:
                got.append(msg)

        task = asyncio.create_task(consume())
        await stt.send_audio(None)
        await stt.flush()
        await asyncio.sleep(0.01)
        assert not task.done()
        await stt.shutdown()
        await asyncio.wait_for(task, 1.0)
        return got

    assert asyncio.run(run()) == []
    print("  ok: NullSTT accepts audio, yields nothing, ends on shutdown")


def test_plan_ids() -> None:
    args = argparse.Namespace(seeds=[7], retrieval_delay=[0.0, 1.0])
    plan = t4.plan_runs([{"sample_id": "s"}], args)
    assert [r[3] for r in plan] == ["s__d0s__s7", "s__d1s__s7"], plan
    print("  ok: run ids match the A100 runner's naming")


if __name__ == "__main__":
    test_completed_and_repair()
    test_fingerprint_mismatch()
    test_null_stt()
    test_plan_ids()
    print("ALL OFFLINE RUNNER CHECKS PASSED")
