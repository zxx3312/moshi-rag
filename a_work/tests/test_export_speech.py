"""Check ordered audio export without loading a model."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
import wave

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from export_speech import export, split_sentences
from turntaking.cascade import Speech


def row(run, action, text, start, policy="evidence_aware"):
    return dict(run_id=run, trace_id="trace_" + run, sample_id="sample_" + run,
                policy=policy, action=action, text=text, output_start_time_s=start, output_end_time_s=start + 1)


class FakePiper:
    def __init__(self, fail_on=None):
        self.spoken = {}
        self.fail_on = fail_on

    def synthesize(self, text):
        if text == self.fail_on:
            raise RuntimeError("fixture synthesis failure")
        speech = Speech(0.1, 0.0, lambda _: 0.0, b"\x01\x00" * 10, 100)
        self.spoken[text] = speech
        return speech


class UnexpectedFailurePiper(FakePiper):
    def synthesize(self, text):
        if text == "Bad.":
            raise TypeError("fixture unexpected failure")
        return super().synthesize(text)


class ExportSpeechTest(unittest.TestCase):
    def test_sentence_splitting_preserves_abbreviations_and_decimals(self):
        text = 'Dr. Vale measured 1.5 cm. It grew. Then Prof. Chen agreed!'
        self.assertEqual(split_sentences(text), ['Dr. Vale measured 1.5 cm.', 'It grew.', 'Then Prof. Chen agreed!'])

    def test_export_keeps_run_order_actual_audio_and_record_indices(self):
        rows = [row("a", "Wait", "", 0), row("a", "Partial Answer", "First fact. Another fact.", 1),
                row("b", "Final Answer", "Different run.", 2, policy="wait_all"),
                row("a", "Final Answer", "Final fact.", 3)]
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory) / "new"
            result = export(rows, FakePiper(), out, policies=["evidence_aware"], gap_s=0.2)
            self.assertEqual((result["total_runs"], result["successful_runs"], result["failed_runs"]), (1, 1, 0))
            item = result["runs"][0]
            folder = out / item["folder"]
            parts = json.loads((folder / "segments.json").read_text())
            self.assertEqual([p["text"] for p in parts], ["First fact.", "Another fact.", "Final fact."])
            self.assertEqual([p["source_record_index"] for p in parts], [1, 1, 2])
            self.assertEqual([p["action"] for p in parts], ["Partial Answer", "Partial Answer", "Final Answer"])
            self.assertEqual([p["source_output_start_s"] for p in parts], [1, 1, 3])
            self.assertAlmostEqual(item["duration_s"], 0.7)
            self.assertAlmostEqual(parts[1]["audio_start_s"], 0.3)
            with wave.open(str(folder / "response.wav"), "rb") as wav:
                self.assertEqual((wav.getnchannels(), wav.getsampwidth(), wav.getframerate()), (1, 2, 100))
                self.assertEqual(wav.getnframes(), 70)
            self.assertEqual(len(list((folder / "segments").glob("*.wav"))), 3)
            self.assertEqual(json.loads((out / "manifest.json").read_text()), result)
            with self.assertRaises(FileExistsError):
                export(rows, FakePiper(), out)

    def test_failed_run_is_recorded_and_other_runs_continue(self):
        rows = [row("a", "Final Answer", "Bad.", 1), row("b", "Final Answer", "Good.", 1)]
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory) / "new"
            result = export(rows, FakePiper("Bad."), out)
            self.assertEqual((result["successful_runs"], result["failed_runs"]), (1, 1))
            self.assertEqual([item["status"] for item in result["runs"]], ["error", "ok"])
            self.assertTrue((out / result["runs"][1]["folder"] / "response.wav").is_file())

    def test_interleaved_runs_do_not_exceed_max_runs(self):
        rows = [row("a", "Partial Answer", "A.", 1), row("b", "Final Answer", "B.", 1),
                row("a", "Final Answer", "A again.", 2)]
        with tempfile.TemporaryDirectory() as directory:
            result = export(rows, FakePiper(), Path(directory) / "new", max_runs=1)
            self.assertEqual(result["runs"][0]["segment_count"], 2)
            self.assertEqual(result["runs"][0]["run_id"], "a")

    def test_unexpected_synthesis_failure_preserves_other_runs(self):
        rows = [row("a", "Final Answer", "Bad.", 1), row("b", "Final Answer", "Good.", 1)]
        with tempfile.TemporaryDirectory() as directory:
            result = export(rows, UnexpectedFailurePiper(), Path(directory) / "new")
            self.assertEqual(result["runs"][0]["error_type"], "TypeError")
            self.assertEqual(result["runs"][1]["status"], "ok")

    def test_missing_source_times_keep_record_order_and_are_recorded_as_unknown(self):
        first = row("a", "Partial Answer", "First.", 1)
        first["output_start_time_s"] = None
        del first["output_end_time_s"]
        rows = [first, row("a", "Final Answer", "Second.", 2)]
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory) / "new"
            result = export(rows, FakePiper(), out)
            segments = json.loads((out / result["runs"][0]["folder"] / "segments.json").read_text())
            self.assertEqual([s["text"] for s in segments], ["First.", "Second."])
            self.assertIsNone(segments[0]["source_output_start_s"])
            self.assertIsNone(segments[0]["source_output_end_s"])
