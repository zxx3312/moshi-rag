"""Check that saved draft reviews never write gold or hide invalid inputs."""

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from b_work.step3.build_gold import validate


SCRIPT = Path(__file__).resolve().parents[1] / "build_gold.py"


class SavedReviewTests(unittest.TestCase):
    def setUp(self):
        """Use fictional data and separate input/output paths for every test."""
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.folder = Path(temporary.name)
        self.samples = self.folder / "samples.jsonl"
        self.annotations = self.folder / "annotations.json"
        self.gold = self.folder / "gold.jsonl"
        self.review = self.folder / "review.md"
        self.unused_output = self.folder / "unused_gold.jsonl"
        sample = {"sample_id": "fictional_1", "dataset": "custom", "type": "comparison",
                  "question": "Which of Alice and Bob is a director?", "answer": "Alice",
                  "context": [["Alice", ["Alice is a director."]],
                              ["Bob", ["Bob is an engineer."]],
                              ["Other", ["Unused context stays visible."]]]}
        self.record = {"schema_version": "1.0", "data_version": "review-draft",
                       "sample_id": sample["sample_id"], "question_type": "comparison",
                       "source_type": "comparison", "units": [
                           {"unit_id": "u1", "description": "whether Alice is a director",
                            "expected_answer": "yes", "necessary": False,
                            "depends_on": [], "support_sets": [["d1s0"]]},
                           {"unit_id": "u2", "description": "whether Bob is a director",
                            "expected_answer": "no", "necessary": False,
                            "depends_on": [], "support_sets": [], "by_omission": True},
                           {"unit_id": "u3", "description": "director among the two candidates",
                            "expected_answer": "Alice", "aliases": ["Alice A."], "necessary": True,
                            "depends_on": ["u1"], "support_sets": [[]],
                            "by_presupposition": True}]}
        self.annotation = {"schema_version": "1.0", "data_version": "review-draft", "records": [
            {"sample_id": sample["sample_id"], "status": "draft", "question_type": "comparison",
             "units": deepcopy(self.record["units"]), "notes": ["Keep the draft facts open."],
             "review_flags": ["existing_source_issue"]}]}
        self.samples.write_text(json.dumps(sample) + "\n")
        self.gold.write_text(json.dumps(self.record) + "\n")
        self.annotations.write_text(json.dumps(self.annotation))
        self.review.write_text("Previous review comments.\n")
        self.unused_output.write_text("Do not write gold in review mode.\n")

    def run_review(self, review_path=None):
        """Run the real CLI, including an output file that must remain untouched."""
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--samples", str(self.samples),
             "--annotations", str(self.annotations), "--review-from-gold", str(self.gold),
             "--review", str(review_path or self.review), "--out", str(self.unused_output)],
            capture_output=True, text=True)

    def test_saved_review_keeps_gold_and_shows_all_review_fields(self):
        inputs = [self.samples, self.annotations, self.gold, self.unused_output]
        before = {path: path.read_bytes() for path in inputs}
        result = self.run_review()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(before, {path: path.read_bytes() for path in inputs})
        text = self.review.read_text()
        for value in ("Alice A.", "**[by_omission]**", "**[by_presupposition]**",
                      "`[]`: no accepted support", "Question type:",
                      "Unused context stays visible.", "existing_source_issue"):
            self.assertIn(value, text)
        self.assertNotIn("Premise support sets", text)

    def test_unknown_gold_field_keeps_previous_review(self):
        self.record["units"][2]["extra_support"] = [["d1s0"]]
        self.gold.write_text(json.dumps(self.record) + "\n")
        before = self.review.read_bytes()
        result = self.run_review()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unsupported gold unit fields", result.stderr)
        self.assertEqual(self.review.read_bytes(), before)

    def test_stale_annotation_keeps_previous_review(self):
        self.annotation["records"][0]["units"][0]["expected_answer"] = "different"
        self.annotations.write_text(json.dumps(self.annotation))
        before = self.review.read_bytes()
        result = self.run_review()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("gold units differ from annotations", result.stderr)
        self.assertEqual(self.review.read_bytes(), before)

    def test_unknown_evidence_keeps_previous_review(self):
        for units in (self.record["units"], self.annotation["records"][0]["units"]):
            units[0]["support_sets"] = [["d99s0"]]
        self.gold.write_text(json.dumps(self.record) + "\n")
        self.annotations.write_text(json.dumps(self.annotation))
        before = self.review.read_bytes()
        result = self.run_review()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unknown evidence ID", result.stderr)
        self.assertEqual(self.review.read_bytes(), before)

    def test_review_cannot_overwrite_gold_input(self):
        before = self.gold.read_bytes()
        result = self.run_review(self.gold)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("must not overwrite an input file", result.stderr)
        self.assertEqual(self.gold.read_bytes(), before)

    def test_normal_gold_validation_still_rejects_empty_support(self):
        with self.assertRaisesRegex(ValueError, "support_sets"):
            validate(self.record)


if __name__ == "__main__":
    unittest.main()
