"""Check log compatibility, gold support, uncertain mappings, and timing."""

from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest

from b_work.eval.records import load_reviews, normalize_log, prepare_inputs, read_jsonl
from b_work.eval.run_eval import evaluate_corpus, summarize
from b_work.eval.score import answer_scores, citation_support, contains_value, score_run, supported_units


def example_data():
    """Make a small A-format run with one partial answer and one final answer."""
    trace = {
        "schema_version": "1.0", "data_version": "debug-v0", "sample_id": "custom_alpha",
        "trace_id": "custom_alpha_long", "question": "Who leads Alpha, and when was it released?",
        "time_origin": "question_end", "clock": "simulated", "trace_type": "controlled_mock",
        "events": [
            {"evidence_id": "e1", "scheduled_time_s": 2.0, "visible_time_s": 2.0,
             "text": "Alpha is led by Alice.", "source": {"document_id": "Alpha leader", "sentence_index": 0}},
            {"evidence_id": "e2", "scheduled_time_s": 8.0, "visible_time_s": 8.0,
             "text": "Alpha was released on June 1.", "source": {"document_id": "Alpha release", "sentence_index": 0}},
        ], "retrieval_complete_time_s": 8.0,
    }
    gold = {"schema_version": "1.0", "data_version": "debug-v0", "sample_id": "custom_alpha",
            "question_type": "multipart", "units": [
                {"unit_id": "u1", "description": "leader of Alpha", "necessary": True,
                 "expected_answer": "Alice", "depends_on": [], "support_sets": [["e1"]]},
                {"unit_id": "u2", "description": "release date of Alpha", "necessary": True,
                 "expected_answer": "June 1", "depends_on": [], "support_sets": [["e2"]]},
            ]}
    base = {key: trace[key] for key in ["schema_version", "data_version", "sample_id", "trace_id", "time_origin", "clock"]}
    base.update(run_id="custom_alpha_long__example_policy__s0", policy="example_policy", seed=0, status="ok")
    logs = [
        {**base, "decision_time_s": 0.0, "action": "Backchannel", "text": "Let me check.",
         "evidence_snapshot_ids": [], "output_start_time_s": 0.0, "output_end_time_s": 1.0, "claim_spans": []},
        {**base, "decision_time_s": 2.0, "action": "Partial Answer", "text": "Alice leads Alpha.",
         "evidence_snapshot_ids": ["e1"], "output_start_time_s": 2.0, "output_end_time_s": 3.0,
         "claim_spans": [{"text": "Alice leads Alpha.", "controller_unit_id": "u1", "value": "Alice",
                          "cited_evidence_ids": ["e1"], "start": 2.0, "end": 3.0, "value_in_text": True}]},
        {**base, "decision_time_s": 8.0, "action": "Final Answer", "text": "It was released on June 1.",
         "evidence_snapshot_ids": ["e1", "e2"], "output_start_time_s": 8.0, "output_end_time_s": 9.0,
         "claim_spans": [{"text": "It was released on June 1.", "controller_unit_id": "u2", "value": "June 1",
                          "cited_evidence_ids": ["e2"], "start": 8.0, "end": 9.0, "value_in_text": True}]},
    ]
    return trace, gold, logs


def evaluate_example(logs=None, trace=None, gold=None, **options):
    """Use aligned IDs only because this fixture explicitly shares gold units."""
    default_trace, default_gold, default_logs = example_data()
    return score_run(default_logs if logs is None else logs,
                     default_trace if trace is None else trace,
                     default_gold if gold is None else gold,
                     aligned_policies=["example_policy"], **options)


class AnswerTests(unittest.TestCase):
    def test_normalization_aliases_and_partial_f1(self):
        self.assertEqual(answer_scores("The Emilio Sánchez!", ["Emilio Sanchez"]), (1.0, 1.0))
        self.assertEqual(answer_scores("Roger Staubach", ["Roger Thomas Staubach"]), (0.0, 0.8))
        self.assertEqual(answer_scores("", ["Alice"]), (0.0, 0.0))
        self.assertEqual(answer_scores("Bob", ["Alice"]), (0.0, 0.0))

    def test_whole_token_value_check(self):
        self.assertFalse(contains_value("Norman leads Alpha.", "no"))
        self.assertTrue(contains_value("No, it did not.", "no"))


class LogTests(unittest.TestCase):
    def test_future_evidence_is_invalid_even_when_output_is_later(self):
        trace, gold, logs = example_data()
        logs[1]["evidence_snapshot_ids"].append("e2")
        logs[1]["output_end_time_s"] = 10.0
        score, _ = evaluate_example(logs[:2], trace, gold)
        self.assertEqual(score["status"], "invalid")
        self.assertIn("Future evidence", score["validation_issues"][0]["reason"])
        self.assertIsNone(score["unit_em"])

    def test_future_citations_do_not_borrow_later_evidence(self):
        trace, gold, logs = example_data()
        logs[1]["claim_spans"][0]["cited_evidence_ids"] = ["e2"]
        logs[1]["output_end_time_s"] = 10.0
        score, _ = evaluate_example(logs[:2], trace, gold)
        self.assertEqual(score["status"], "invalid")
        self.assertIn("outside decision snapshot", score["validation_issues"][0]["reason"])

    def test_both_claim_field_forms_are_accepted(self):
        trace, _, logs = example_data()
        claim = logs[1]["claim_spans"][0]
        for old, new in [("start", "start_time_s"), ("end", "end_time_s"), ("cited_evidence_ids", "evidence_ids")]:
            claim[new] = claim.pop(old)
        normalized = normalize_log(logs[1], trace)
        self.assertEqual(normalized["claim_spans"][0]["start"], 2.0)
        claim["start"] = 4.0
        with self.assertRaisesRegex(ValueError, "Conflicting claim fields"):
            normalize_log(logs[1], trace)

    def test_bad_times_and_wait_rows_are_invalid(self):
        for value in [True, float("nan"), -1.0]:
            trace, gold, logs = example_data()
            logs[1]["claim_spans"][0]["start"] = value
            score, _ = evaluate_example(logs, trace, gold)
            self.assertEqual(score["status"], "invalid")
        trace, _, logs = example_data()
        logs[0]["action"] = "Wait"
        with self.assertRaisesRegex(ValueError, "Wait needs"):
            normalize_log(logs[0], trace)

    def test_claim_must_fit_output_and_reply_text(self):
        trace, _, logs = example_data()
        logs[1]["claim_spans"][0]["end"] = 4.0
        with self.assertRaisesRegex(ValueError, "after output"):
            normalize_log(logs[1], trace)
        logs[1]["claim_spans"][0]["end"] = 3.0
        logs[1]["claim_spans"][0]["text"] = "A different reply."
        with self.assertRaisesRegex(ValueError, "not part"):
            normalize_log(logs[1], trace)

    def test_empty_wait_and_error_rows_are_kept(self):
        trace, gold, logs = example_data()
        logs[0].update(action="Wait", text="", output_start_time_s=None, output_end_time_s=None)
        score, _ = evaluate_example(logs, trace, gold)
        self.assertEqual(score["records"], 3)
        self.assertEqual(score["status"], "ok")
        logs[0]["status"] = "error"
        scores, _ = evaluate_corpus([trace], [gold], logs)
        summary = summarize(scores, [trace])
        self.assertEqual(summary["status_counts"], {"error": 1})
        self.assertIsNone(scores[0]["unit_em"])

    def test_unknown_versions_cycles_and_duplicate_ids_are_rejected(self):
        trace, gold, _ = example_data()
        for field, value in [("schema_version", "2.0"), ("data_version", "other")]:
            changed = dict(trace, **{field: value})
            with self.subTest(field=field), self.assertRaises(ValueError):
                prepare_inputs([changed], [gold])
        with self.assertRaisesRegex(ValueError, "Duplicate trace_id"):
            prepare_inputs([trace, trace], [gold])
        gold["units"][0]["depends_on"] = ["u2"]
        gold["units"][1]["depends_on"] = ["u1"]
        with self.assertRaisesRegex(ValueError, "cycle"):
            prepare_inputs([trace], [gold])

    def test_bad_json_has_a_line_number(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "bad.jsonl"
            path.write_text('{}\nnot json\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, r"bad.jsonl:2:"):
                read_jsonl(path)


class SupportTests(unittest.TestCase):
    def test_full_and_alternative_support_sets_are_needed(self):
        _, gold, _ = example_data()
        unit = dict(gold["units"][0], support_sets=[["e1", "e2"], ["e3"]])
        units = {"u1": unit}
        self.assertEqual(supported_units(units, {"e1"}), set())
        self.assertEqual(supported_units(units, {"e3"}), {"u1"})
        self.assertFalse(citation_support("u1", units, {"e1", "e2"}, {"e1"}))
        self.assertTrue(citation_support("u1", units, {"e1", "e2"}, {"e1", "e2"}))

    def test_dependencies_need_visible_support(self):
        trace, gold, logs = example_data()
        gold["units"][0]["necessary"] = False
        gold["units"][1]["depends_on"] = ["u1"]
        trace["events"][0]["visible_time_s"] = 8.0
        trace["events"][1]["visible_time_s"] = 2.0
        trace["events"].reverse()
        row = deepcopy(logs[-1])
        row.update(decision_time_s=2.0, output_start_time_s=2.0, output_end_time_s=3.0, evidence_snapshot_ids=["e2"])
        row["claim_spans"][0].update(start=2.0, end=3.0)
        score, claims = evaluate_example([row], trace, gold)
        self.assertEqual(claims[0]["label"], "UNSUPPORTED")
        self.assertFalse(score["grounded_complete"])

    def test_empty_outer_and_inner_sets_have_different_meanings(self):
        _, gold, _ = example_data()
        units = {u["unit_id"]: u for u in gold["units"]}
        units["u3"] = {"unit_id": "u3", "expected_answer": "Alpha", "necessary": True,
                       "depends_on": ["u1", "u2"], "support_sets": [[]]}
        self.assertNotIn("u3", supported_units(units, {"e1"}))
        self.assertIn("u3", supported_units(units, {"e1", "e2"}))
        self.assertFalse(citation_support("u3", units, {"e1", "e2"}, {"e1"}))
        self.assertTrue(citation_support("u3", units, {"e1", "e2"}, {"e1", "e2"}))
        units["u3"]["support_sets"] = []
        self.assertNotIn("u3", supported_units(units, {"e1", "e2"}))

    def test_presupposition_sets_can_use_one_known_branch(self):
        _, gold, _ = example_data()
        units = {u["unit_id"]: u for u in gold["units"]}
        units["u2"]["support_sets"] = []
        units["u3"] = {"unit_id": "u3", "necessary": True, "expected_answer": "Alice",
                       "depends_on": ["u1", "u2"], "support_sets": [[]],
                       "presupposition_sets": [["e1"]], "by_presupposition": True}
        self.assertIn("u3", supported_units(units, {"e1"}))
        self.assertTrue(citation_support("u3", units, {"e1"}, {"e1"}))
        self.assertNotIn("u3", supported_units(units, set()))

    def test_correct_value_without_citation_is_not_grounded(self):
        _, _, logs = example_data()
        logs[-1]["claim_spans"][0]["cited_evidence_ids"] = []
        score, claims = evaluate_example(logs)
        self.assertEqual(score["unit_em"], 1.0)
        self.assertTrue(score["answer_complete"])
        self.assertFalse(score["grounded_complete"])
        self.assertEqual(claims[-1]["label"], "UNSUPPORTED")

    def test_presupposition_flag_alone_does_not_replace_support(self):
        _, gold, _ = example_data()
        units = {u["unit_id"]: u for u in gold["units"]}
        units["u3"] = {"unit_id": "u3", "necessary": True, "expected_answer": "Alice",
                       "depends_on": ["u1", "u2"], "support_sets": [[]],
                       "by_presupposition": True}
        self.assertNotIn("u3", supported_units(units, {"e1"}))
        self.assertFalse(citation_support("u3", units, {"e1"}, {"e1"}))
        units["u3"]["presupposition_sets"] = [["e2"]]
        self.assertIn("u3", supported_units(units, {"e1", "e2"}))
        self.assertFalse(citation_support("u3", units, {"e1", "e2"}, {"e1"}))

    def test_premise_support_needs_its_own_citations(self):
        _, gold, _ = example_data()
        units = {u["unit_id"]: u for u in gold["units"]}
        units["u3"] = {"unit_id": "u3", "necessary": True, "expected_answer": "Alice",
                       "depends_on": ["u1", "u2"], "support_sets": [["e3"]],
                       "presupposition_sets": [["e1"]], "by_presupposition": True}
        self.assertIn("u3", supported_units(units, {"e1", "e3"}))
        self.assertFalse(citation_support("u3", units, {"e1", "e3"}, {"e3"}))
        self.assertTrue(citation_support("u3", units, {"e1", "e3"}, {"e1"}))

    def test_retrieval_miss_stays_in_the_data(self):
        trace, gold, logs = example_data()
        trace["events"] = trace["events"][:1]
        prepare_inputs([trace], [gold])
        score, _ = evaluate_example(logs[:1], trace, gold)
        self.assertEqual(score["status"], "ok")
        self.assertEqual(score["missing_gold_evidence_ids"], ["e2"])
        self.assertEqual(score["unreachable_necessary_units"], ["u2"])
        self.assertFalse(score["grounded_complete"])


class MappingAndTimingTests(unittest.TestCase):
    def test_good_multipart_run_and_time_metrics(self):
        score, claims = evaluate_example(timing_kind="estimated")
        self.assertEqual((score["unit_em"], score["unit_f1"]), (1.0, 1.0))
        self.assertTrue(score["grounded_complete"])
        self.assertEqual(score["unsupported_claim_rate"], 0.0)
        self.assertEqual((score["ttfr_s"], score["ttfgi_s"], score["ttca_s"]), (0.0, 2.0, 9.0))
        self.assertEqual(len(claims), 2)

    def test_unknown_times_never_become_zero(self):
        score, _ = evaluate_example()
        self.assertIsNone(score["ttfr_s"])
        self.assertIsNone(score["ttfgi_s"])
        self.assertIsNone(score["ttca_s"])
        _, _, logs = example_data()
        for row in logs:
            row.update(output_start_time_s=None, output_end_time_s=None)
            for claim in row["claim_spans"]:
                claim.update(start=None, end=None)
        score, _ = evaluate_example(logs, timing_kind="estimated")
        self.assertTrue(score["grounded_complete"])
        self.assertIsNone(score["ttca_s"])

    def test_final_answer_is_not_proof_of_completion(self):
        _, _, logs = example_data()
        logs[1]["action"] = "Final Answer"
        score, _ = evaluate_example(logs[:2], timing_kind="estimated")
        self.assertTrue(score["final_answer_attempted"])
        self.assertFalse(score["answer_complete"])
        self.assertEqual(score["unit_em"], 0.5)
        self.assertIsNone(score["ttca_s"])

    def test_unaligned_ids_are_not_assumed_to_be_gold_ids(self):
        trace, gold, logs = example_data()
        score, claims = score_run(logs, trace, gold)
        self.assertEqual(score["claims_needing_review"], 2)
        self.assertIsNone(score["unit_em"])
        self.assertIsNone(score["unsupported_claim_rate"])
        guessed, _ = score_run(logs, trace, gold, allow_value_match=True)
        self.assertEqual(guessed["approximate_mapping_claims"], 2)
        self.assertEqual(claims[0]["candidate_gold_unit_ids"], ["u1"])

    def test_ambiguous_values_need_review(self):
        trace, gold, logs = example_data()
        gold["units"][1]["expected_answer"] = "Alice"
        score, claims = score_run(logs[:2], trace, gold, allow_value_match=True)
        self.assertEqual(claims[0]["reason"], "ambiguous_gold_value")
        self.assertIsNone(score["unsupported_claim_rate"])

    def test_reviewed_mapping_uses_log_positions(self):
        trace, gold, logs = example_data()
        for row in logs:
            for claim in row["claim_spans"]:
                claim["controller_unit_id"] = "different"
        review_rows = [{"run_id": logs[0]["run_id"], "record_index": index, "claim_index": 0,
                        "gold_unit_id": uid, "reviewer": "test"} for index, uid in [(1, "u1"), (2, "u2")]]
        scores, claims = evaluate_corpus([trace], [gold], logs, review_rows=review_rows)
        self.assertTrue(scores[0]["grounded_complete"])
        self.assertEqual({c["mapping_source"] for c in claims}, {"review"})
        with self.assertRaisesRegex(ValueError, "Duplicate claim review"):
            load_reviews(review_rows + review_rows[:1])

    def test_one_answer_baseline_can_be_wrong(self):
        trace, gold, logs = example_data()
        gold["units"] = gold["units"][:1]
        row = deepcopy(logs[1])
        row.update(action="Final Answer", text="Bob leads Alpha.")
        row["claim_spans"][0].update(controller_unit_id="answer", text=row["text"], value="Bob")
        score, claims = score_run([row], trace, gold)
        self.assertEqual(score["unit_em"], 0.0)
        self.assertEqual(claims[0]["label"], "UNSUPPORTED")

    def test_metadata_value_must_occur_in_output(self):
        _, _, logs = example_data()
        logs[1]["text"] = "Bob leads Alpha."
        logs[1]["claim_spans"][0]["text"] = logs[1]["text"]
        score, claims = evaluate_example(logs)
        self.assertEqual(claims[0]["reason"], "value_not_found_in_claim_text")
        self.assertIsNone(score["unit_em"])

    def test_placeholder_runs_have_no_answer_score_by_default(self):
        _, _, logs = example_data()
        logs[1]["text"] = "[u1: leader = Alice <- e1]"
        logs[1]["claim_spans"][0]["text"] = logs[1]["text"]
        score, _ = evaluate_example(logs)
        self.assertEqual(score["status"], "placeholder")
        self.assertIsNone(score["unit_em"])
        diagnostic, _ = evaluate_example(logs, allow_placeholder=True)
        self.assertEqual(diagnostic["status"], "diagnostic")

    def test_conflicting_answers_are_not_silently_resolved(self):
        trace, gold, logs = example_data()
        wrong = deepcopy(logs[1])
        wrong["text"] = "Bob leads Alpha."
        wrong["claim_spans"][0].update(text=wrong["text"], value="Bob")
        score, _ = evaluate_example([logs[0], wrong, logs[1], logs[2]], trace, gold)
        self.assertIn("conflicting_values_for_unit:u1", score["review_reasons"])
        self.assertIsNone(score["grounded_complete"])

    def test_missing_expected_runs_are_preserved(self):
        trace, gold, _ = example_data()
        scores, claims = evaluate_corpus([trace], [gold], [], expected_policies=["wait_all"])
        self.assertEqual(scores[0]["status"], "missing")
        self.assertEqual(claims, [])
        summary = summarize(scores, [trace])
        self.assertEqual(summary["groups"][0]["runs"], 1)
        self.assertIsNone(summary["groups"][0]["ttfr_s"]["median"])

    def test_clock_groups_do_not_mix(self):
        trace, gold, logs = example_data()
        with self.assertRaisesRegex(ValueError, "audio_stream"):
            evaluate_example(timing_kind="observed")
        audio = dict(trace, clock="audio_stream", trace_id="custom_alpha_audio")
        audio_logs = deepcopy(logs)
        for row in audio_logs:
            row.update(clock="audio_stream", trace_id=audio["trace_id"], run_id="audio_run")
        scores, _ = evaluate_corpus([trace, audio], [gold], logs + audio_logs,
                                     aligned_policies=["example_policy"], timing_kind="estimated")
        self.assertEqual(len(summarize(scores, [trace, audio])["groups"]), 2)

    def test_inputs_are_not_mutated(self):
        trace, gold, logs = example_data()
        original = deepcopy((trace, gold, logs))
        evaluate_corpus([trace], [gold], logs, aligned_policies=["example_policy"])
        self.assertEqual((trace, gold, logs), original)


if __name__ == "__main__":
    unittest.main()
