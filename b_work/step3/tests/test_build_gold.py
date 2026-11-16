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


class GoldFixture(unittest.TestCase):
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


class SavedReviewTests(GoldFixture):
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


#-------------#
# Added: use fictional questions to check premise paths and normal test-set exports.
class GoldExportTests(GoldFixture):
    def setUp(self):
        """Pair revised samples with annotations that use both reference forms."""
        super().setUp()
        self.sample = json.loads(self.samples.read_text())
        self.sample.update(schema_version="1.0", data_version="review-draft", type="inference",
                           original_question="Who is the director?", gold_answer="Alice")
        self.annotation["records"][0]["question_number"] = 151
        final = self.annotation["records"][0]["units"][2]
        final["depends_on"] = ["u1", "u2"]
        final["presupposition_sets"] = [["d1s0"]]
        self.annotation["records"][0]["units"][0]["support_sets"] = [[["Alice", 0]]]
        self.samples.write_text(json.dumps(self.sample) + "\n")
        self.annotations.write_text(json.dumps(self.annotation))

    def run_export(self, output_path=None, review_path=None):
        """Run a normal export into temporary files only."""
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--samples", str(self.samples),
             "--annotations", str(self.annotations), "--out", str(output_path or self.gold),
             "--review", str(review_path or self.review), "--include-unit-json"],
            capture_output=True, text=True)

    def test_export_keeps_premise_paths_and_reviewed_type(self):
        before = {p: p.read_bytes() for p in (self.samples, self.annotations)}
        result = self.run_export()
        self.assertEqual(result.returncode, 0, result.stderr)
        gold = json.loads(self.gold.read_text())
        self.assertEqual(gold["data_version"], "review-draft")
        self.assertEqual(gold["source_type"], "inference")
        self.assertEqual(gold["question_type"], "comparison")
        self.assertEqual(gold["units"][0]["support_sets"], [["d1s0"]])
        self.assertEqual(gold["units"][2]["presupposition_sets"], [["d1s0"]])
        self.assertEqual(before, {p: p.read_bytes() for p in before})
        text = self.review.read_text()
        for expected in ("## Q151", "Original question: Who is the director?", "Gold final answer: Alice",
                         "Presupposition sets", '"presupposition_sets"', "Unused context stays visible."):
            self.assertIn(expected, text)

    def test_premise_only_single_quotes_its_evidence(self):
        unit = deepcopy(self.annotation["records"][0]["units"][2])
        unit.update(unit_id="u1", depends_on=[], support_sets=[],
                    presupposition_sets=[[["Alice", 0]]])
        self.annotation["records"][0].update(question_type="single", units=[unit])
        self.annotations.write_text(json.dumps(self.annotation))
        result = self.run_export()
        self.assertEqual(result.returncode, 0, result.stderr)
        gold = json.loads(self.gold.read_text())
        self.assertEqual(gold["units"][0]["support_sets"], [])
        self.assertEqual(gold["units"][0]["presupposition_sets"], [["d1s0"]])
        self.assertIn('`[]`: no direct support; use the premise path', self.review.read_text())
        self.assertIn('- `d1s0` Alice [0]: Alice is a director.', self.review.read_text().split('Notes:')[0])

    def test_invalid_premise_inputs_keep_both_outputs(self):
        cases = [
            ({"by_presupposition": False}, "requires by_presupposition"),
            ({"presupposition_sets": [[]]}, "empty presupposition set"),
            ({"presupposition_sets": [["d99s0"]]}, "unknown evidence ID"),
        ]
        original = deepcopy(self.annotation)
        for changes, error in cases:
            with self.subTest(changes=changes):
                self.annotation = deepcopy(original)
                self.annotation["records"][0]["units"][2].update(changes)
                self.annotations.write_text(json.dumps(self.annotation))
                before = {p: p.read_bytes() for p in (self.gold, self.review)}
                result = self.run_export()
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(error, result.stderr)
                self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_premise_path_still_needs_a_supported_parent(self):
        first, final = deepcopy(self.annotation["records"][0]["units"][:2])
        first["support_sets"] = []
        final.update(necessary=True, depends_on=["u1"], support_sets=[],
                     presupposition_sets=[["d1s0"]], by_presupposition=True)
        record = deepcopy(self.record)
        record.update(question_type="bridge", units=[first, final])
        with self.assertRaisesRegex(ValueError, "no complete"):
            validate(record)

    def test_export_checks_sample_version_before_writing(self):
        self.sample["data_version"] = "wrong-version"
        self.samples.write_text(json.dumps(self.sample) + "\n")
        before = {p: p.read_bytes() for p in (self.gold, self.review)}
        result = self.run_export()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("versions differ", result.stderr)
        self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_export_cannot_overwrite_an_input(self):
        before = {p: p.read_bytes() for p in (self.samples, self.annotations, self.review)}
        result = self.run_export(output_path=self.annotations)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("must not overwrite an input", result.stderr)
        self.assertEqual(before, {p: p.read_bytes() for p in before})


class PresuppositionReviewTests(GoldFixture):
    def setUp(self):
        """Keep matching gold and annotations with a separate premise path."""
        super().setUp()
        self.record["units"][2]["presupposition_sets"] = [["d1s0"]]
        self.annotation["records"][0]["units"][2]["presupposition_sets"] = [[["Alice", 0]]]
        self.gold.write_text(json.dumps(self.record) + "\n")
        self.annotations.write_text(json.dumps(self.annotation))

    def test_saved_review_accepts_both_premise_reference_forms(self):
        before = self.gold.read_bytes()
        result = self.run_review()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.gold.read_bytes(), before)
        self.assertIn("Presupposition sets", self.review.read_text())

    def test_changed_premise_keeps_the_previous_review(self):
        self.annotation["records"][0]["units"][2]["presupposition_sets"] = [["d2s0"]]
        self.annotations.write_text(json.dumps(self.annotation))
        before = self.review.read_bytes()
        result = self.run_review()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("gold units differ from annotations", result.stderr)
        self.assertEqual(self.review.read_bytes(), before)

    def test_unknown_saved_premise_evidence_keeps_previous_review(self):
        self.record["units"][2]["presupposition_sets"] = [["d99s0"]]
        self.gold.write_text(json.dumps(self.record) + "\n")
        before = self.review.read_bytes()
        result = self.run_review()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unknown evidence ID", result.stderr)
        self.assertEqual(self.review.read_bytes(), before)
#-------------#


if __name__ == "__main__":
    unittest.main()
