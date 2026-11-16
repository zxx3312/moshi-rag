"""Fictional checks that incomplete or duplicate smoke runs cannot unlock main experiments."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from eval_main_smoke import execution_inputs


class SmokeGateTest(unittest.TestCase):
    def setup_fixture(self, folder):
        def write(path, data, lines=False):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("".join(json.dumps(r) + "\n" for r in data) if lines else json.dumps(data))
        write(folder / "questions.jsonl", [{"trace_id": "fictional_immediate"}], True)
        root = folder / "results/shard_000"
        write(root / "gpu.json", {"gpu": "H100 (fictional test metadata)"})
        for phase in ("main", "oracle"):
            write(root / "q000" / (phase + "_worker.json"), {"state": "completed"})
            worker = root / "q000" / phase
            write(worker / "status.json", {"state": "completed"})
            write(worker / "execution.jsonl", [{"trace_id": "fictional_immediate", "policy": phase, "state": "completed"}], True)
            write(worker / "policy_log.jsonl", [{"trace_id": "fictional_immediate", "policy": phase}], True)
        return {"results": str(folder / "results"), "shards": [[0]],
                "questions": [str(folder / "questions.jsonl")], "policies": ["main", "oracle"]}

    def test_complete_fixture_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest = self.setup_fixture(Path(tmp))
            traces, logs, _ = execution_inputs(manifest, 0)
            self.assertEqual((len(traces), len(logs)), (1, 2))

    def test_failed_worker_cannot_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            manifest = self.setup_fixture(folder)
            (folder / "results/shard_000/q000/main_worker.json").write_text('{"state":"failed"}')
            with self.assertRaisesRegex(ValueError, "worker failed"):
                execution_inputs(manifest, 0)

    def test_duplicate_execution_cannot_replace_missing_one(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            manifest = self.setup_fixture(folder)
            path = folder / "results/shard_000/q000/main/execution.jsonl"
            path.write_text(path.read_text() * 2)
            with self.assertRaisesRegex(ValueError, "Missing or duplicate"):
                execution_inputs(manifest, 0)

    def test_empty_policy_log_cannot_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            manifest = self.setup_fixture(folder)
            (folder / "results/shard_000/q000/main/policy_log.jsonl").write_text("")
            with self.assertRaisesRegex(ValueError, "no log output"):
                execution_inputs(manifest, 0)


if __name__ == "__main__":
    unittest.main()
