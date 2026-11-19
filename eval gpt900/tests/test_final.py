"""Synthetic-only final-run plumbing tests. Never inspect reserved B contents."""
import asyncio
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('gpt900_runner', ROOT / 'run.py')
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)
from cascadesystem.config import Settings
from eval_common import digest, write_json, write_jsonl


def trace(index=0, schedule='immediate', blank=False):
    times = {'immediate': [0, 0], 'short': [1, 3], 'long': [2, 8]}[schedule]
    events = [{'evidence_id': f'e{n+1}', 'scheduled_time_s': times[n], 'visible_time_s': times[n],
        'text': text, 'source': {'dataset': 'fictional', 'document_id': title,
                               'document_index': n, 'sentence_index': 0}}
        for n, (title, text) in enumerate([
            ('Silver Ship launch', 'The Silver Ship launched on May 12, 2040.'),
            ('Silver Ship return', '' if blank else 'The Silver Ship returned on May 20, 2040.')])]
    return {'schema_version': '1.0', 'data_version': 'eval-revised-v1', 'sample_id': f'fictional_ship_{index}',
        'trace_id': f'fictional_ship_{index}_{schedule}', 'question': f'When did fictional Silver Ship {index} launch?',
        'trace_type': 'controlled_mock', 'time_origin': 'question_end', 'clock': 'simulated',
        'events': events, 'retrieval_complete_time_s': max(times)}


def corpus(blank=False):
    return [trace(i, s, blank) for i in range(300) for s in ['immediate', 'short', 'long']]


def prepared(path):
    (path / 'public').mkdir(parents=True)
    write_jsonl(path / 'public/traces.jsonl', corpus())
    manifest = {'mode': runner.MODE, 'split': 'eval_reserved', 'b_commit': runner.B_COMMIT,
        'files_sha256': {'public/traces.jsonl': digest(path / 'public/traces.jsonl')}}
    write_json(path / 'manifest.json', manifest)
    return manifest


class FixtureLLM:
    def __init__(self):
        self.calls, self.payloads = [], []
    async def complete(self, purpose, system, payload):
        self.calls.append({'purpose': purpose, 'status': 'fictional'})
        self.payloads.append(deepcopy(payload))
        if purpose.startswith('decompose'):
            return {'units': [{'unit_id': 'u1', 'description': 'launch date', 'necessary': True,
                               'depends_on': [], 'queries': ['Silver Ship launch']}]}
        if purpose.startswith('judge'):
            source = next(e for e in payload['evidence'] if 'launched' in e['text'])
            return {'judgments': [{'unit_id': 'u1', 'label': 'SUPPORTED', 'value': 'May 12, 2040',
                'citations': [source['evidence_id']], 'quotes': [
                    {'evidence_id': source['evidence_id'], 'text': source['text']}]}]}
        if purpose == 'generate':
            return {'text': 'The Silver Ship launched on May 12, 2040.'}
        if purpose == 'verify':
            return {'approved': True, 'facts_valid': True, 'expressed_unit_ids': ['u1']}
        raise AssertionError(purpose)


class GateTests(unittest.TestCase):
    def test_prepare_refuses_before_git_or_writes_without_final_flag(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(runner, 'git') as git:
            output = Path(folder) / 'not-created'
            with self.assertRaisesRegex(ValueError, 'explicit --final-run'):
                runner.prepare(output)
            git.assert_not_called()
            self.assertFalse(output.exists())

    def test_load_and_score_refuse_before_opening_nonexistent_data(self):
        with self.assertRaisesRegex(ValueError, '--final-run'):
            runner.load_public(Path('does-not-exist'))
        with self.assertRaisesRegex(ValueError, '--final-run'):
            runner.score('does-not-exist', 'does-not-exist', 'does-not-exist')

    def test_cli_refuses_before_checkpoint_or_environment_access(self):
        with patch.object(runner, 'checkpoint_info') as checkpoint, patch.object(runner.Settings, 'from_env') as config:
            with self.assertRaisesRegex(ValueError, '--final-run'):
                runner.main(runner.arguments(['run']))
            checkpoint.assert_not_called()
            config.assert_not_called()

    def test_cli_has_explicit_final_acknowledgment_and_default_full_selection(self):
        args = runner.arguments(['run', '--final-run'])
        self.assertTrue(args.final_run)
        self.assertEqual(args.timeout, 180)
        self.assertFalse(args.allow_value_match)
        self.assertFalse(hasattr(args, 'limit'))


class DataTests(unittest.TestCase):
    def test_accepts_synthetic_300_questions_in_all_three_schedules(self):
        counts = runner.validate_public(corpus())
        self.assertEqual(counts, {'questions': 300, 'traces': 900,
                                 'schedules': {'immediate': 300, 'short': 300, 'long': 300}})

    def test_rejects_debug_sized_input(self):
        with self.assertRaisesRegex(ValueError, '300 revised questions and 900'):
            runner.validate_public([trace()])

    def test_future_or_gold_metadata_is_rejected(self):
        for level in ['trace', 'event', 'source']:
            rows = corpus()
            target = rows[0] if level == 'trace' else rows[0]['events'][0] if level == 'event' else rows[0]['events'][0]['source']
            target['expected_answer'] = 'FORBIDDEN_FICTIONAL_GOLD'
            with self.assertRaisesRegex(ValueError, 'shape|fields'):
                runner.validate_public(rows)

    def test_evidence_cannot_change_between_schedules(self):
        rows = corpus()
        rows[1]['events'][0]['text'] = 'Different fictional evidence'
        with self.assertRaisesRegex(ValueError, 'differs between schedules'):
            runner.validate_public(rows)

    def test_arrival_times_cannot_be_rewritten(self):
        rows = corpus()
        rows[1]['events'][0]['visible_time_s'] = 0
        with self.assertRaisesRegex(ValueError, 'arrival schedule'):
            runner.validate_public(rows)

    def test_blank_sentences_stay_in_input_and_do_not_shorten_completion_time(self):
        rows = corpus(blank=True)
        runner.validate_public(rows)
        raw = rows[2]
        runtime = runner.runtime_trace(raw)
        self.assertEqual(len(raw['events']), 2)
        self.assertEqual(len(runtime['events']), 1)
        self.assertEqual(runtime['retrieval_complete_time_s'], 8)
        self.assertEqual(runtime['events'][0], raw['events'][0])

    def test_prediction_loader_does_not_require_or_open_private_gold(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            prepared(root)
            traces, _ = runner.load_public(root, final_run=True)
            self.assertEqual(len(traces), 900)
            self.assertFalse((root / 'private').exists())

    def test_public_hash_changes_are_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            prepared(root)
            with (root / 'public/traces.jsonl').open('a') as stream:
                stream.write('\n')
            with self.assertRaisesRegex(ValueError, 'hash mismatch'):
                runner.load_public(root, final_run=True)

    def test_prepare_joins_only_revised_gold_and_freezes_source_paths(self):
        rows = corpus()
        gold = [{'sample_id': f'fictional_ship_{i}', 'units': [{}] * (3 if i < 217 else 2)} for i in range(300)]
        encode = lambda values: ''.join(json.dumps(r) + '\n' for r in values).encode()
        blobs = {runner.SOURCES['public/traces.jsonl']: encode(rows),
                 runner.SOURCES['private/source_gold_0.jsonl']: encode(gold[:150]),
                 runner.SOURCES['private/source_gold_1.jsonl']: encode(gold[150:]),
                 runner.TRACE_DIR + '/manifest.json': b'{"status":"fictional_only"}'}
        def fake_git(operation, source):
            self.assertEqual(operation, 'show')
            self.assertTrue(source.startswith(runner.B_COMMIT + ':'))
            return blobs[source.split(':', 1)[1]]
        evaluator = MagicMock()
        with tempfile.TemporaryDirectory() as folder, patch.object(runner, 'frozen_commit', return_value=runner.B_COMMIT), \
                patch.object(runner, 'git', side_effect=fake_git), \
                patch.object(runner, 'load_evaluator', return_value=(evaluator, {})):
            output = Path(folder) / 'input'
            result = runner.prepare(output, final_run=True)
            self.assertEqual(result['traces'], 900)
            saved_gold = runner.read_jsonl(output / 'private/gold.jsonl')
            self.assertEqual(sum(len(r['units']) for r in saved_gold), 817)
            self.assertEqual(result['source_paths'], runner.SOURCES)
            evaluator.prepare_inputs.assert_called_once()


class ReplayTests(unittest.IsolatedAsyncioTestCase):
    async def test_full_inventory_and_resume_preserve_all_900_synthetic_attempts(self):
        async def fake_trace(row, settings, folder, timeout, factory, tts, play):
            folder.mkdir(parents=True)
            result = {'status': 'complete', 'events': [{'type': 'utterance', 'sequence': 1,
                'time_s': 0, 'action': 'Final Answer', 'text': 'Fictional output.', 'claims': [],
                'evidence_snapshot_ids': []}], 'evaluation': {'trace_id': row['trace_id'], 'mode': runner.MODE}}
            write_json(folder / 'run.json', result)
            return result
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            prepared(root / 'input')
            settings = Settings()
            with patch.object(runner, 'one_trace', side_effect=fake_trace) as execute, patch('builtins.print'):
                output = await runner.run_final(root / 'input', root / 'output', settings, final_run=True,
                                               factory=lambda _: FixtureLLM())
                first = (output / 'samples/0001/run.json').read_bytes()
                self.assertEqual(execute.call_count, 900)
                self.assertEqual(len(runner.read_jsonl(output / 'policy_log.jsonl')), 900)
                execute.reset_mock()
                await runner.run_final(root / 'input', output, settings, final_run=True, resume=True,
                                       factory=lambda _: FixtureLLM())
                execute.assert_not_called()
                self.assertEqual(first, (output / 'samples/0001/run.json').read_bytes())
                self.assertEqual(len(runner.read_jsonl(output / 'policy_log.jsonl')), 900)

    async def test_one_trace_reuses_original_controller_without_gold(self):
        provider = FixtureLLM()
        with tempfile.TemporaryDirectory() as folder:
            directory = Path(folder) / 'sample'
            result = await runner.one_trace(trace(blank=True), Settings(), directory, 5,
                                            lambda _: provider, 'none', False)
            self.assertEqual(result['status'], 'complete')
            self.assertEqual(result['evaluation']['mode'], runner.MODE)
            self.assertEqual(result['evaluation']['empty_evidence_sentences_ignored'], 1)
            self.assertNotIn('expected_answer', json.dumps(provider.payloads))
            self.assertNotIn('support_sets', json.dumps(provider.payloads))
            self.assertEqual([e['text'] for e in result['evidence']], ['The Silver Ship launched on May 12, 2040.'])

    async def test_run_gate_refuses_before_provider_access(self):
        factory = MagicMock()
        with self.assertRaisesRegex(ValueError, '--final-run'):
            await runner.run_final('missing', 'missing', Settings(), factory=factory)
        factory.assert_not_called()

    async def test_checkpoint_change_refuses_resume_before_any_new_sample(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            prepared(root / 'input')
            output = root / 'output'
            output.mkdir()
            write_json(output / 'manifest.json', {'mode': runner.MODE, 'source_sha256': 'different'})
            with self.assertRaisesRegex(ValueError, 'resume refused'):
                await runner.run_final(root / 'input', output, Settings(), final_run=True, resume=True,
                                       factory=lambda _: FixtureLLM())
            self.assertFalse((output / 'samples').exists())


class ScoreTests(unittest.TestCase):
    def test_scorer_sees_gold_separately_and_retains_expected_missing_runs(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            inputs, run = root / 'input', root / 'run'
            data = prepared(inputs)
            (inputs / 'private').mkdir()
            write_jsonl(inputs / 'private/gold.jsonl', [{'sample_id': 'fictional_only', 'units': []}])
            data['files_sha256']['private/gold.jsonl'] = digest(inputs / 'private/gold.jsonl')
            write_json(inputs / 'manifest.json', data)
            run.mkdir()
            write_json(run / 'manifest.json', {'mode': runner.MODE, 'b_commit': runner.B_COMMIT,
                'traces_sha256': data['files_sha256']['public/traces.jsonl'],
                'trace_ids': [t['trace_id'] for t in corpus()], 'code_commit': 'fictional', 'source_sha256': 'fictional'})
            write_jsonl(run / 'policy_log.jsonl', [])
            evaluator = MagicMock()
            evaluator.evaluate_corpus.return_value = ([], [])
            evaluator.summarize.return_value = {'status_counts': {'missing': 900}, 'groups': []}
            evaluator.make_report.return_value = 'Fictional report only'
            with patch.object(runner, 'load_evaluator', return_value=(evaluator, {})):
                report = runner.score(inputs, run, root / 'score', final_run=True, allow_value_match=True)
            args = evaluator.evaluate_corpus.call_args
            self.assertEqual(len(args.args[0]), 900)
            self.assertEqual(args.args[1], [{'sample_id': 'fictional_only', 'units': []}])
            self.assertEqual(args.kwargs['expected_policies'], [runner.POLICY])
            self.assertEqual(args.kwargs['timing_kind'], 'unknown')
            self.assertTrue(args.kwargs['allow_value_match'])
            self.assertEqual(report['status_counts']['missing'], 900)
            self.assertTrue((root / 'score/summary.md').exists())


if __name__ == '__main__':
    unittest.main()
