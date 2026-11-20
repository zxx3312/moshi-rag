"""Paired playback on a single channel with evidence arriving during speech."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from compare_wait_all import actual_playback, fixed_playback, timing_breakdown


def utterance(cite, ready, duration, offset):
    span = dict(value=cite, text=cite, cited_evidence_ids=[cite], value_in_text=True,
                start=ready + offset, end=ready + offset + 0.2)
    return dict(run_id="example", decision_time_s=ready - 1, decision_cost_s=0.5,
                generation_cost_s=0.5, tts_cost_s=0, output_start_time_s=ready,
                output_end_time_s=ready + duration, action="Partial Answer", text=cite, claim_spans=[span])


class WaitAllAblationTest(unittest.TestCase):
    def setUp(self):
        self.trace = dict(retrieval_complete_time_s=8, events=[
            dict(evidence_id="a", visible_time_s=1), dict(evidence_id="b", visible_time_s=8)])
        self.rows = [utterance("a", 2, 3, 1), utterance("b", 9, 2, 0.5)]
        self.scores = {(i, 0): dict(row["claim_spans"][0], label="SUPPORTED") for i, row in enumerate(self.rows)}

    def test_wait_overlaps_speech_and_delayed_arm_queues_identical_segments(self):
        result = fixed_playback(self.rows, self.scores, self.trace)
        self.assertEqual(result["incremental"], dict(first_fact_s=3, finish_s=11))
        self.assertEqual(result["delayed"], dict(first_fact_s=9, finish_s=13))
        self.assertEqual(result["speech_s"], 5)
        self.assertEqual([s["delayed_start_s"] for s in result["segments"]], [8, 11])

    def test_unknown_claim_excludes_whole_utterance_and_empty_scripts_have_no_times(self):
        extra = dict(self.rows[0]["claim_spans"][0], value="c")
        self.rows[0]["claim_spans"].append(extra)
        self.scores[0, 1] = dict(extra, label="NEEDS_REVIEW")
        self.scores[1, 0]["label"] = "UNSUPPORTED"
        result = fixed_playback(self.rows, self.scores, self.trace)
        self.assertEqual(result["segments"], [])
        self.assertEqual(result["incremental"], dict(first_fact_s=None, finish_s=None))
        self.assertEqual(result["excluded_utterances"], {"unsupported_or_unreviewed": 2})

    def test_cannot_release_claim_using_future_evidence(self):
        self.trace["events"][0]["visible_time_s"] = 8
        with self.assertRaisesRegex(ValueError, "Future evidence"):
            fixed_playback(self.rows, self.scores, self.trace)

    def test_partial_after_retrieval_only_blocks_speech_once_final_is_ready(self):
        partial = utterance("a", 2, 7, 1)  # Plays until 9, retrieval completes at 8.
        final = utterance("b", 9, 2, 0.5)
        final.update(action="Final Answer", decision_time_s=8, decision_cost_s=0.3, generation_cost_s=0.2)
        score = dict(ttfgi_s=None, ttca_s=9.7, grounded_complete=True, claims_needing_review=0)
        actual = actual_playback([partial, final], score, 8)
        self.assertEqual(actual["partial_before_retrieval_end_s"], 6)
        self.assertEqual(actual["partial_after_retrieval_end_s"], 1)
        self.assertEqual(actual["completion"]["components"]["waiting_for_partial_s"], 0.5)
        # The same final sentence, ready at the same time, with an idle output channel.
        wait = utterance("b", 8.5, 2, 0.5)
        wait.update(action="Final Answer", decision_time_s=8, decision_cost_s=0.3, generation_cost_s=0.2)
        reference = actual_playback([wait], dict(score, ttca_s=9.2), 8)
        breakdown = timing_breakdown([actual], [reference])
        self.assertEqual(breakdown["mean_extra_completion_s"], 0.5)
        self.assertEqual(breakdown["later_pairs_blocked_by_partial"], 1)

    def test_completion_can_occur_in_partial_and_unknown_stays_unpaired(self):
        self.rows[1]["action"] = "Final Answer"
        score = dict(ttfgi_s=3, ttca_s=3.2, grounded_complete=True, claims_needing_review=0)
        measured = actual_playback(self.rows, score, 8)
        self.assertEqual(measured["completion"]["action"], "Partial Answer")
        self.assertEqual(measured["completion"]["components"]["decision_minus_retrieval_s"], -7)
        unknown = actual_playback(self.rows, dict(score, ttca_s=None, grounded_complete=None), 8)
        self.assertIsNone(unknown["completion"])
        breakdown = timing_breakdown([measured], [unknown])
        self.assertEqual(breakdown["completion_pairs"], 0)
        self.assertIsNone(breakdown["mean_extra_completion_s"])

    def test_evidence_arrives_between_partial_decision_and_playback(self):
        row = utterance("a", 8, 3, 0.5)
        score = dict(ttfgi_s=None, ttca_s=None, grounded_complete=None, claims_needing_review=1)
        result = actual_playback([row], score, 8)
        self.assertEqual(result["partial_selected_before_but_started_after_retrieval"], 1)
        self.assertEqual(result["partial_before_retrieval_end_s"], 0)
        self.assertEqual(result["partial_after_retrieval_end_s"], 3)
