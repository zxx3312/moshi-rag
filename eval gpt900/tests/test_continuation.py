"""Fictional operational recovery; no final questions, model calls or real speech."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from test_final import runner, trace, FixtureLLM
from cascadesystem.config import Settings
from eval_common import digest, public_settings, write_json


def result(row, audio_error=False, authentication=False):
    events = [{'type': 'utterance', 'sequence': 1, 'time_s': 0, 'action': 'Final Answer',
               'text': 'Fictional output.', 'claims': [], 'evidence_snapshot_ids': []}]
    if authentication:
        events.append({'type': 'failure', 'error': 'HTTP 401 Unauthorized'})
    return {'status': 'error' if authentication else 'complete', 'events': events,
            'audio': {'enabled': True, 'status': 'error' if audio_error else 'ok',
                      'errors': ['Speech command exited with code 1'] if audio_error else []},
            'evaluation': {'mode': runner.MODE, 'trace_id': row['trace_id']}}


def parent_fixture(root, rows=None):
    rows = rows or [trace(0), trace(1)]
    current = runner.source_manifest()
    old_source = deepcopy(current)
    old_source['files']['eval gpt900/run.py'] = '0' * 64
    old_source['sha256'] = hashlib.sha256(json.dumps(old_source['files'], sort_keys=True).encode()).hexdigest()
    settings = Settings()
    identity = {'mode': runner.MODE, 'split': 'eval_reserved', 'b_commit': runner.B_COMMIT,
        'traces_sha256': 'fictional-input-hash', 'trace_ids': [t['trace_id'] for t in rows],
        'policy': runner.POLICY, 'settings': public_settings(settings), 'source_sha256': current['sha256'],
        'timeout_s': 180, 'timing_kind': 'unknown', 'audio': {'tts': 'none', 'play': False},
        'audio_error_policy': 'continue'}
    parent = root / 'parent'
    sample = parent / 'samples/0001'
    sample.mkdir(parents=True)
    write_json(sample / 'run.json', result(rows[0], audio_error=True))
    (sample / 'preserved-audio-error.txt').write_text('Fictional prior error, retain verbatim.')
    write_json(parent / 'source-manifest.json', old_source)
    previous = {k: v for k, v in identity.items() if k != 'audio_error_policy'}
    previous['source_sha256'] = old_source['sha256']
    write_json(parent / 'manifest.json', previous)
    return parent, identity, current, rows, settings


class StopTests(unittest.TestCase):
    def test_new_audio_failure_stops_by_default_with_precise_message(self):
        with patch('builtins.print') as output:
            self.assertTrue(runner.stop_after_result(result(trace(), audio_error=True)))
        text = ' '.join(str(c.args) for c in output.call_args_list)
        self.assertIn('Speech command exited with code 1', text)
        self.assertNotIn('authentication failure', text)

    def test_saved_audio_failure_does_not_block_resume(self):
        saved = result(trace(), audio_error=True)
        before = deepcopy(saved)
        with patch('builtins.print'):
            self.assertFalse(runner.stop_after_result(saved, reused=True))
        self.assertEqual(saved, before)

    def test_explicit_audio_continue_retains_error_and_goes_on(self):
        saved = result(trace(), audio_error=True)
        with patch('builtins.print'):
            self.assertFalse(runner.stop_after_result(saved, continue_on_audio_error=True))
        self.assertEqual(saved['audio']['status'], 'error')

    def test_authentication_still_stops_when_audio_continue_is_enabled(self):
        with patch('builtins.print'):
            self.assertTrue(runner.stop_after_result(result(trace(), authentication=True),
                                                     continue_on_audio_error=True))


class ParentTests(unittest.TestCase):
    def test_accepts_recorded_runner_update_with_unchanged_method_and_checkpoint(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            parent, identity, current, _, _ = parent_fixture(root)
            plan = runner.continuation_plan(parent, root / 'child', identity, current)
            self.assertTrue(plan['shared_method_source_unchanged'])
            self.assertEqual(len(plan['inherited_samples']), 1)
            self.assertNotEqual(plan['parent_source_sha256'], plan['current_source_sha256'])
            self.assertFalse((root / 'child').exists())

    def test_changed_checkpoint_is_rejected_before_copying(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            parent, identity, current, _, _ = parent_fixture(root)
            identity['settings'] = {**identity['settings'], 'judge_model': 'different'}
            with self.assertRaisesRegex(ValueError, 'settings differ'):
                runner.continuation_plan(parent, root / 'child', identity, current)
            self.assertFalse((root / 'child').exists())

    def test_changed_controller_or_prompt_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            parent, identity, current, _, _ = parent_fixture(root)
            current['files']['cascadesystem/llm.py'] = 'changed-method'
            with self.assertRaisesRegex(ValueError, 'shared model/controller/prompt/scorer'):
                runner.continuation_plan(parent, root / 'child', identity, current)

    def test_parent_and_child_cannot_overlap(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            parent, identity, current, _, _ = parent_fixture(root)
            for output in [parent, parent / 'child', root]:
                with self.assertRaisesRegex(ValueError, 'separate new directory'):
                    runner.continuation_plan(parent, output, identity, current)

    def test_inconsistent_source_manifest_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            parent, identity, current, _, _ = parent_fixture(root)
            previous = json.loads((parent / 'source-manifest.json').read_text())
            previous['sha256'] = 'tampered'
            write_json(parent / 'source-manifest.json', previous)
            with self.assertRaisesRegex(ValueError, 'inconsistent'):
                runner.continuation_plan(parent, root / 'child', identity, current)

    def test_unfinished_parent_attempt_is_preserved_and_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            parent, identity, current, _, _ = parent_fixture(root)
            (parent / 'samples/0002').mkdir()
            with self.assertRaisesRegex(ValueError, 'unfinished'):
                runner.continuation_plan(parent, root / 'child', identity, current)
            self.assertTrue((parent / 'samples/0002').exists())


class ContinuationTests(unittest.IsolatedAsyncioTestCase):
    async def test_copy_preserves_parent_and_calls_only_unsaved_trace(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            parent, identity, current, rows, settings = parent_fixture(root)
            original = (parent / 'samples/0001/run.json').read_bytes()
            async def fake_new(row, config, directory, timeout, factory, tts, play):
                directory.mkdir(parents=True)
                saved = result(row)
                write_json(directory / 'run.json', saved)
                return saved
            data = {'b_commit': runner.B_COMMIT, 'files_sha256': {'public/traces.jsonl': 'fictional-input-hash'}}
            with patch.object(runner, 'load_public', return_value=(rows, data)), \
                    patch.object(runner, 'one_trace', side_effect=fake_new) as execute, patch('builtins.print'):
                child = await runner.run_final('fictional', root / 'child', settings, final_run=True,
                    continue_from=parent, continue_on_audio_error=True, factory=lambda _: FixtureLLM())
            self.assertEqual(execute.call_count, 1)
            self.assertEqual(execute.call_args.args[0]['trace_id'], rows[1]['trace_id'])
            self.assertEqual((parent / 'samples/0001/run.json').read_bytes(), original)
            self.assertEqual((child / 'samples/0001/run.json').read_bytes(), original)
            self.assertTrue((child / 'samples/0001/preserved-audio-error.txt').exists())
            self.assertEqual(json.loads((child / 'samples/0001/run.json').read_text())['audio']['status'], 'error')
            self.assertTrue((child / 'continuation.json').is_file())
            self.assertEqual(len(runner.read_jsonl(child / 'policy_log.jsonl')), 2)

    async def test_resume_and_continue_from_are_mutually_exclusive_before_data_read(self):
        with patch.object(runner, 'load_public') as loader:
            with self.assertRaisesRegex(ValueError, 'either --resume or --continue-from'):
                await runner.run_final('missing', 'missing', Settings(), final_run=True,
                                       resume=True, continue_from='parent')
            loader.assert_not_called()


if __name__ == '__main__':
    unittest.main()
