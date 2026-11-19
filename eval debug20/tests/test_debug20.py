"""Fictional integration checks against B's unchanged scorer; no model/network calls."""
import asyncio
from copy import deepcopy
import json
from pathlib import Path
import tempfile
import time
import unittest
import sys

EVAL_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EVAL_ROOT))
sys.path.insert(0, str(EVAL_ROOT.parent))

from cascadesystem.config import Settings
from cascadesystem.demo import DemoLLM
from eval_data import load_b_traces, load_evaluator
from eval_score import score_b_run
from eval_replay import TraceEvidence, policy_rows, run_b_debug, run_trace
from eval_common import digest, write_json, write_jsonl


B_COMMIT = 'ea390574eadd301354d5de46f0d28d328cca5bad'


def trace():
    return {'schema_version': '1.0', 'data_version': 'debug-v0', 'sample_id': 'fictional_ship',
            'trace_id': 'fictional_ship_short', 'question': 'When did the Silver Ship launch and return?', 'time_origin': 'question_end',
            'clock': 'simulated', 'trace_type': 'controlled_mock', 'retrieval_complete_time_s': .06,
            'events': [{'evidence_id': 'd1s0', 'scheduled_time_s': 0, 'visible_time_s': 0,
                        'text': 'The Silver Ship launched on May 12, 2040.', 'source': {'document_id': 'Silver Ship'}},
                       {'evidence_id': 'd2s0', 'scheduled_time_s': .06, 'visible_time_s': .06,
                        'text': 'The Silver Ship returned on May 20, 2040.', 'source': {'document_id': 'Silver Ship'}}]}


def gold():
    return {'schema_version': '1.0', 'data_version': 'debug-v0', 'sample_id': 'fictional_ship',
            'question_type': 'multipart', 'units': [
                {'unit_id': 'gold_launch', 'description': 'launch date', 'necessary': True,
                 'expected_answer': 'May 12, 2040', 'aliases': [], 'depends_on': [], 'support_sets': [['d1s0']]},
                {'unit_id': 'gold_return', 'description': 'return date', 'necessary': True,
                 'expected_answer': 'May 20, 2040', 'aliases': [], 'depends_on': [], 'support_sets': [['d2s0']]}]}


def prepared(folder):
    folder.mkdir()
    write_jsonl(folder / 'traces.jsonl', [trace()])
    write_jsonl(folder / 'gold.jsonl', [gold()])
    write_json(folder / 'manifest.json', {'mode': 'b_debug_trace', 'split': 'debug', 'data_version': 'debug-v0',
                                         'b_commit': B_COMMIT, 'files_sha256': {
                                             name: digest(folder / name) for name in ['traces.jsonl', 'gold.jsonl']}})


class FixtureLLM(DemoLLM):
    async def complete(self, purpose, system, payload):
        if purpose == 'decompose':
            return {'units': [{'unit_id': 'u1', 'description': 'launch date', 'necessary': True,
                               'depends_on': [], 'queries': ['Silver Ship launch']},
                              {'unit_id': 'u2', 'description': 'return date', 'necessary': True,
                               'depends_on': [], 'queries': ['Silver Ship return']}]}
        if purpose.startswith('judge'):
            rows = []
            for uid, word, value in [('u1', 'launched', 'May 12, 2040'), ('u2', 'returned', 'May 20, 2040')]:
                source = next((e for e in payload['evidence'] if word in e['text']), None)
                rows.append({'unit_id': uid, 'label': 'SUPPORTED' if source else 'UNRESOLVED',
                             'value': value if source else '', 'citations': [source['evidence_id']] if source else [],
                             'quotes': [{'evidence_id': source['evidence_id'], 'text': source['text']}] if source else []})
            return {'judgments': rows}
        if purpose == 'generate':
            return {'text': ' '.join(f"The {f['description']} was {f['value']}." for f in payload['APPROVED_FACTS'])}
        return await super().complete(purpose, system, payload)


class WatchingLLM(FixtureLLM):
    def __init__(self):
        super().__init__()
        self.snapshots = []
    async def complete(self, purpose, system, payload):
        if purpose == 'judge':
            self.snapshots.append(deepcopy(payload))
            await asyncio.sleep(.08)  # The next evidence arrives during this call.
        return await super().complete(purpose, system, payload)


class ReplayTests(unittest.IsolatedAsyncioTestCase):
    async def test_real_controller_preserves_ids_and_snapshot_isolation_and_partial_output(self):
        llm = WatchingLLM()
        with tempfile.TemporaryDirectory() as folder:
            result = await run_trace(trace(), Settings(), Path(folder) / 'sample', 2, lambda _: llm)
        self.assertEqual(result['status'], 'complete')
        self.assertEqual([e['evidence_id'] for e in result['evidence']], ['d1s0', 'd2s0'])
        self.assertEqual(llm.snapshots[0]['visible_evidence_ids'], ['d1s0'])
        self.assertEqual(llm.snapshots[1]['visible_evidence_ids'], ['d1s0', 'd2s0'])
        self.assertNotIn('gold_launch', json.dumps(llm.snapshots))
        self.assertNotIn('support_sets', json.dumps(llm.snapshots))
        answers = [e['action'] for e in result['events'] if e['type'] == 'utterance']
        self.assertIn('Partial Answer', answers)
        self.assertEqual(answers[-1], 'Final Answer')

    async def test_prediction_runs_when_gold_file_is_absent_and_resume_keeps_existing_result(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            prepared(root / 'input')
            (root / 'input/gold.jsonl').unlink()
            output = await run_b_debug(root / 'input', root / 'run', settings=Settings(), llm_factory=lambda _: FixtureLLM())
            original = (output / 'samples/0001/run.json').read_bytes()
            await run_b_debug(root / 'input', root / 'run', settings=Settings(), resume=True,
                              llm_factory=lambda _: FixtureLLM())
            self.assertEqual(original, (output / 'samples/0001/run.json').read_bytes())

    async def test_timeout_remains_error_in_b_log(self):
        slow = trace()
        slow['events'][0]['visible_time_s'] = 3
        slow['events'][1]['visible_time_s'] = 4
        slow['retrieval_complete_time_s'] = 4
        with tempfile.TemporaryDirectory() as folder:
            result = await run_trace(slow, Settings(), Path(folder) / 'sample', .01, lambda _: FixtureLLM())
        self.assertEqual(result['status'], 'timeout')
        logs, _ = policy_rows(result, slow)
        self.assertTrue(all(r['status'] == 'error' for r in logs))

    async def test_scheduler_waits_for_actual_arrival(self):
        iterator = TraceEvidence(trace(), time.monotonic()).__aiter__()
        await anext(iterator)
        started = time.monotonic()
        second = await anext(iterator)
        self.assertGreater(time.monotonic() - started, .04)
        self.assertEqual(second[0]['evidence_id'], 'd2s0')

    async def test_late_consumer_receives_all_due_evidence_without_artificial_extra_rounds(self):
        iterator = TraceEvidence(trace(), time.monotonic() - 1).__aiter__()
        batch = await anext(iterator)
        self.assertEqual([row['evidence_id'] for row in batch], ['d1s0', 'd2s0'])
        with self.assertRaises(StopAsyncIteration):
            await anext(iterator)


class InputAndAdapterTests(unittest.TestCase):
    def test_reserved_manifest_and_changed_trace_are_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            inputs = Path(folder) / 'inputs'
            prepared(inputs)
            (inputs / 'traces.jsonl').write_text('{}\n', encoding='utf-8')
            with self.assertRaises(ValueError):
                load_b_traces(inputs)
            manifest = json.loads((inputs / 'manifest.json').read_text())
            manifest['split'] = 'eval_reserved'
            write_json(inputs / 'manifest.json', manifest)
            with self.assertRaises(ValueError):
                load_b_traces(inputs)

    def test_duplicate_ids_and_invalid_times_are_rejected(self):
        for key, value in [('evidence_id', 'd1s0'), ('visible_time_s', float('nan'))]:
            bad = trace()
            bad['events'][1][key] = value
            with self.assertRaises(ValueError):
                TraceEvidence(bad, time.monotonic())

    def test_retraction_keeps_original_action_and_excludes_run_from_b_scoring(self):
        result = {'status': 'incomplete', 'events': [{'sequence': 4, 'type': 'utterance', 'time_s': 2,
                  'action': 'Correction', 'text': 'Please disregard that date.', 'claims': []}]}
        rows, issues = policy_rows(result, trace())
        self.assertEqual(rows[0]['cascade_action'], 'Correction')
        self.assertEqual(rows[0]['status'], 'error')
        self.assertEqual(len(issues), 1)


class BScorerTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)
        prepared(self.root / 'input')
        self.output = await run_b_debug(self.root / 'input', self.root / 'run', settings=Settings(),
                                        llm_factory=lambda _: FixtureLLM())

    def reviews(self):
        rows = []
        logs = [json.loads(line) for line in (self.output / 'policy_log.jsonl').read_text(encoding='utf-8').splitlines()]
        for i, record in enumerate(logs):
            for j, claim in enumerate(record['claim_spans']):
                rows.append({'run_id': record['run_id'], 'record_index': i, 'claim_index': j,
                             'gold_unit_id': 'gold_launch' if claim['controller_unit_id'] == 'u1' else 'gold_return',
                             'reviewer': 'fictional_test_fixture', 'source_log_sha256': digest(self.output / 'policy_log.jsonl')})
        path = self.root / 'reviews.jsonl'
        write_jsonl(path, rows)
        return path

    async def test_strict_b_default_does_not_assume_controller_ids_match_gold(self):
        summary = score_b_run(self.root / 'input', self.output, self.root / 'strict')
        group = summary['groups'][0]
        self.assertEqual(group['claims_needing_review'], 2)
        self.assertIsNone(group['mean_unit_em_on_scored_runs'])
        self.assertIsNone(group['unsupported_claim_rate'])
        self.assertEqual(group['ttfgi_s']['count'], 0)

    async def test_checked_mapping_scores_values_and_support_without_inventing_speech_times(self):
        summary = score_b_run(self.root / 'input', self.output, self.root / 'reviewed', reviews=self.reviews())
        group = summary['groups'][0]
        self.assertEqual(group['mean_unit_em_on_scored_runs'], 1)
        self.assertEqual(group['unsupported_claim_rate'], 0)
        self.assertEqual(group['recorded_grounded_completions'], 1)
        self.assertIsNone(group['ttca_s']['median'])
        self.assertEqual(summary['config']['aligned_policies'], [])

    async def test_correct_value_with_wrong_cited_support_is_unsupported(self):
        reviews = self.reviews()
        logs = [json.loads(line) for line in (self.output / 'policy_log.jsonl').read_text(encoding='utf-8').splitlines()]
        for row in logs:
            for claim in row['claim_spans']:
                if claim['controller_unit_id'] == 'u2':
                    claim['cited_evidence_ids'] = ['d1s0']
        write_jsonl(self.output / 'policy_log.jsonl', logs)
        reviews = self.reviews()
        summary = score_b_run(self.root / 'input', self.output, self.root / 'wrong_support', reviews=reviews)
        self.assertEqual(summary['groups'][0]['mean_unit_em_on_scored_runs'], 1)
        self.assertEqual(summary['groups'][0]['unsupported_claim_rate'], .5)
        self.assertEqual(summary['groups'][0]['recorded_grounded_completions'], 0)

    async def test_approximate_mapping_is_explicit_and_separate(self):
        summary = score_b_run(self.root / 'input', self.output, self.root / 'approx', allow_value_match=True)
        self.assertEqual(summary['groups'][0]['approximate_mapping_claims'], 2)
        self.assertTrue(summary['config']['allow_value_match'])

    async def test_future_evidence_is_invalid_even_when_answer_matches(self):
        reviews = self.reviews()
        logs = [json.loads(line) for line in (self.output / 'policy_log.jsonl').read_text(encoding='utf-8').splitlines()]
        for row in logs:
            if row['claim_spans']:
                row['evidence_snapshot_ids'] = ['d1s0', 'd2s0']
                row['decision_time_s'] = 0
        write_jsonl(self.output / 'policy_log.jsonl', logs)
        summary = score_b_run(self.root / 'input', self.output, self.root / 'invalid')
        self.assertEqual(summary['status_counts'], {'invalid': 1})

    async def test_review_for_changed_source_log_is_rejected(self):
        reviews = self.reviews()
        with (self.output / 'policy_log.jsonl').open('a', encoding='utf-8') as stream:
            stream.write('\n')
        with self.assertRaises(ValueError):
            score_b_run(self.root / 'input', self.output, self.root / 'changed', reviews=reviews)

    async def test_actual_b_source_hashes_are_preserved(self):
        _, hashes = load_evaluator(B_COMMIT)
        self.assertEqual(hashes['score.py'], 'b08979820496dff68ac15e5f2ff25367d1299bccd638c5b5e812e344725c4913')

