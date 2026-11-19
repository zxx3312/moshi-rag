"""Fictional-only training, checkpoint, routing and data-isolation regressions."""
from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest

from cascadesystem.config import Settings
from cascadesystem.llm import TinkerLLM
from cascadesystem.protocol import decompose
from cascadesystem.tests.test_protocol import Recorder, Replies
from cascadesystem.tests.test_system import FakeHTTP
from cascadesystem.training.data import convert_record, load_prepared, prompt_hash, sha, write_json, write_rows
from cascadesystem.training.engine import checkpoint_info, encoded_rows, evaluate, train
from cascadesystem.training.__main__ import inference_command


def fixture(sid='fiction_train', split='train', ship='Silver Ship'):
    question = f'When did the {ship} launch and return?'
    texts = [f'The {ship} launched in 2044.', f'The {ship} returned in 2045.']
    descriptions = ['launch year of ' + ship, 'return year of ' + ship]
    units = [{'unit_id': f'u{i}', 'description': description, 'depends_on': []}
             for i, description in enumerate(descriptions, 1)]
    sample = {'sample_id': sid, 'source_split': 'train', 'project_split': split,
              'question': question, 'context': [[ship, texts]]}
    gold = {'sample_id': sid, 'units': [dict(u, necessary=True) for u in units]}
    target = {'units': [{'unit_id': 'u1', 'label': 'SUPPORTED', 'value': '2044',
                          'citations': ['d1s0'], 'by_omission': False},
                         {'unit_id': 'u2', 'label': 'UNRESOLVED', 'value': None,
                          'citations': [], 'by_omission': False}]}
    request = ('Question: ' + question + '\n\nUnits:\n' + json.dumps(units)
               + '\n\nEvidence received so far:\n[d1s0] (' + ship + ') ' + texts[0])
    record = {'messages': [{'role': 'system', 'content': 'Old schema'},
                          {'role': 'user', 'content': request},
                          {'role': 'assistant', 'content': json.dumps(target)}],
              'metadata': {'data_version': 'sft-v0', 'sample_id': sid, 'split': split,
                           'trace_id': sid + '_order1', 'time_s': 1, 'question_type': 'multipart'}}
    return record, sample, gold


def prepared(folder):
    folder.mkdir()
    rows = {}
    for split, ship in [('train', 'Silver Ship'), ('dev', 'Moon Ship')]:
        row, reason = convert_record(*fixture('fiction_' + split, split, ship))
        assert reason is None
        rows[split] = [deepcopy(row) for _ in range(4)]
        write_rows(folder / (split + '.jsonl'), rows[split])
    meta = {'mode': 'cascade_judge_sft', 'data_version': 'sft-v0', 'b_commit': '0' * 40,
            'judge_prompt_sha256': prompt_hash(),
            'files_sha256': {s + '.jsonl': sha((folder / (s + '.jsonl')).read_bytes()) for s in rows}}
    write_json(folder / 'manifest.json', meta)
    return rows


class DataTests(unittest.TestCase):
    def test_partial_snapshot_keeps_unknown_unit_and_only_visible_evidence(self):
        record, sample, gold = fixture()
        before = deepcopy(record)
        converted, reason = convert_record(record, sample, gold)
        self.assertIsNone(reason)
        self.assertEqual(converted['payload']['visible_evidence_ids'], ['d1s0'])
        self.assertEqual(converted['target']['judgments'][1]['label'], 'UNRESOLVED')
        self.assertEqual(converted['target']['judgments'][0]['quotes'][0]['text'], sample['context'][0][1][0])
        self.assertNotIn('target', converted['payload'])
        self.assertNotIn('expected_answer', json.dumps(converted['payload']))
        self.assertNotIn('2045', json.dumps(converted['payload']))
        self.assertEqual(record, before)

    def test_future_target_citation_is_rejected(self):
        record, sample, gold = fixture()
        targets = json.loads(record['messages'][-1]['content'])
        targets['units'][0]['citations'] = ['d1s1']
        record['messages'][-1]['content'] = json.dumps(targets)
        with self.assertRaisesRegex(ValueError, 'future'):
            convert_record(record, sample, gold)

    def test_omission_question_is_excluded_instead_of_relabeling(self):
        record, sample, gold = fixture()
        gold['units'][0]['by_omission'] = True
        result, reason = convert_record(record, sample, gold)
        self.assertIsNone(result)
        self.assertEqual(reason, 'question_uses_omission_rule')

    def test_old_dependency_exception_is_not_silently_accepted(self):
        record, sample, gold = fixture()
        units = json.loads(record['messages'][-2]['content'].split('Units:\n')[1].split('\n\nEvidence')[0])
        units[0]['depends_on'] = ['u2']
        start, rest = record['messages'][-2]['content'].split('Units:\n')
        evidence = rest.split('\n\nEvidence')[1]
        record['messages'][-2]['content'] = start + 'Units:\n' + json.dumps(units) + '\n\nEvidence' + evidence
        gold['units'][0]['depends_on'] = ['u2']
        result, reason = convert_record(record, sample, gold)
        self.assertIsNone(result)
        self.assertIn('dependency', reason)

    def test_non_training_source_and_split_are_rejected(self):
        record, sample, gold = fixture()
        sample['source_split'] = 'dev'
        with self.assertRaises(ValueError):
            convert_record(record, sample, gold)
        record['metadata']['split'] = 'reserved'
        with self.assertRaises(ValueError):
            convert_record(record, sample, gold)

    def test_changed_data_and_prompt_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / 'inputs'
            prepared(folder)
            load_prepared(folder)
            (folder / 'train.jsonl').write_text('{}\n', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'hash'):
                load_prepared(folder)


class FakeBackend:
    versions = {'fictional-sdk': '1'}
    def __init__(self, fail_step=None):
        self.started, self.trained, self.saved = [], [], []
        self.closed = False
        self.fail_step = fail_step
    def encode(self, record):
        return {'tokens': [10, 11, 12, 13], 'weights': [0.0, 0.0, 1.0, 1.0]}
    async def start(self, rank, state=None, seed=42):
        self.started.append((rank, state))
    async def train_batch(self, batch, lr):
        if self.fail_step == len(self.trained) + 1:
            raise RuntimeError('fictional provider failure')
        self.trained.append((deepcopy(batch), lr))
        return 2.0, 4.0
    async def loss_batch(self, batch):
        epoch = len(self.trained) // 2
        loss = {1: 0.8, 2: 0.2, 3: 0.4}.get(epoch, 0.6)
        return loss * 4, 4
    async def save(self, name):
        self.saved.append(name)
        return {'state': 'tinker://fiction/weights/' + name,
                'checkpoint': 'tinker://fiction/sampler_weights/' + name}
    async def close(self, status='success'):
        self.closed = True
    async def sample(self, payload, checkpoint, max_tokens):
        return {'judgments': [{'unit_id': u['unit_id'], 'label': 'UNRESOLVED',
                              'value': '', 'citations': [], 'quotes': []} for u in payload['units']]}


class TrainingTests(unittest.IsolatedAsyncioTestCase):
    async def test_best_checkpoint_uses_dev_loss_and_partial_batches_keep_masks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); prepared(root / 'inputs')
            backend = FakeBackend()
            output = await train(backend, inputs=root / 'inputs', output=root / 'run', epochs=3, batch_size=2)
            best = checkpoint_info(output)
            self.assertEqual(best['epoch'], 2)
            self.assertEqual(len(backend.trained), 6)
            self.assertEqual(backend.trained[0][0][0]['weights'], [0, 0, 1, 1])
            self.assertTrue(backend.closed)
            resume = FakeBackend()
            await train(resume, inputs=root / 'inputs', output=output, epochs=3, batch_size=2, resume=True)
            self.assertEqual(resume.started, [])

    async def test_smoke_is_bounded_and_marked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); prepared(root / 'inputs')
            backend = FakeBackend()
            output = await train(backend, inputs=root / 'inputs', output=root / 'run', smoke=True, batch_size=1)
            self.assertEqual(len(backend.trained), 2)
            self.assertTrue(checkpoint_info(output)['smoke'])

    async def test_failed_epoch_can_resume_from_last_completed_state_without_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); prepared(root / 'inputs')
            backend = FakeBackend(fail_step=3)
            with self.assertRaises(RuntimeError):
                await train(backend, inputs=root / 'inputs', output=root / 'run', epochs=3, batch_size=2)
            state = json.loads((root / 'run/resume.json').read_text(encoding='utf-8'))
            self.assertEqual(state['completed_epoch'], 1)
            previous = (root / 'run/events.jsonl').read_text(encoding='utf-8')
            retry = FakeBackend()
            await train(retry, inputs=root / 'inputs', output=root / 'run', epochs=3, batch_size=2, resume=True)
            self.assertEqual(retry.started[0][1], state['state'])
            self.assertEqual(len(retry.trained), 4)
            self.assertTrue((root / 'run/events.jsonl').read_text(encoding='utf-8').startswith(previous))

    async def test_invalid_data_fails_before_remote_training_model_is_created(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); prepared(root / 'inputs')
            backend = FakeBackend()
            backend.encode = lambda r: {'tokens': [1] * 10, 'weights': [0] * 5 + [1] * 5}
            with self.assertRaisesRegex(ValueError, 'No usable'):
                await train(backend, inputs=root / 'inputs', output=root / 'run', max_length=4)
            self.assertFalse(backend.started)

    async def test_dev_evaluation_measures_missed_support_without_using_targets_as_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); prepared(root / 'inputs')
            summary = await evaluate(FakeBackend(), inputs=root / 'inputs', output=root / 'eval', limit=2)
            self.assertEqual(summary['records'], 2)
            self.assertEqual(summary['label_agreement'], 0.5)
            self.assertEqual(summary['missed_supported_rate'], 1)
            self.assertEqual(summary['false_supported_rate'], 0)

    async def test_dev_report_distinguishes_raw_false_support_from_rejected_quotes(self):
        class BadQuoteBackend(FakeBackend):
            async def sample(self, payload, checkpoint, max_tokens):
                return {'judgments': [{'unit_id': u['unit_id'], 'label': 'SUPPORTED',
                    'value': '2044', 'citations': ['d1s0'], 'quotes': [
                        {'evidence_id': 'd1s0', 'text': 'A fabricated quote.'}]} for u in payload['units']]}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); prepared(root / 'inputs')
            summary = await evaluate(BadQuoteBackend(), inputs=root / 'inputs', output=root / 'eval', limit=1)
            self.assertEqual(summary['raw_false_supported_rate'], 1)
            self.assertEqual(summary['false_supported_rate'], 0)
            self.assertEqual(summary['counts']['rejected_supported_units'], 2)
            self.assertTrue((root / 'eval/provenance.json').is_file())

    def test_overlong_targets_are_excluded_not_truncated(self):
        backend = FakeBackend()
        with self.assertRaisesRegex(ValueError, 'No usable'):
            encoded_rows(backend, [{}], 100, 1)


class RoutingTests(unittest.IsolatedAsyncioTestCase):
    async def test_checkpoint_only_handles_judgment_calls(self):
        response = {'choices': [{'finish_reason': 'stop', 'message': {'content': '{}'}}]}
        http = FakeHTTP(response)
        settings = Settings(api_key='fictional', judge_model='tinker://fiction/sampler_weights/best')
        client = TinkerLLM(settings, http)
        for purpose in ['judge', 'judge_repair', 'decompose', 'plan_review', 'generate', 'verify', 'feedback']:
            await client.complete(purpose, 'JSON', {})
        models = [request[1]['body']['model'] for request in http.requests]
        self.assertEqual(models[:2], [settings.judge_model] * 2)
        self.assertEqual(models[2:], [settings.model] * 5)
        self.assertEqual([c['model'] for c in client.calls], models)

    async def test_plan_review_can_normalize_explicit_transitive_query_references(self):
        raw = {'units': [
            {'unit_id': 'u1', 'description': 'captain of Silver Ship', 'necessary': False,
             'depends_on': [], 'queries': ['Silver Ship captain']},
            {'unit_id': 'u2', 'description': 'birth year of {u1}', 'necessary': False,
             'depends_on': ['u1'], 'queries': ['{u1} birth year']},
            {'unit_id': 'u3', 'description': 'year comparison', 'necessary': True,
             'depends_on': ['u2'], 'queries': ['{u1} {u2} compare']}]}
        initial = deepcopy(raw); initial['units'][2]['depends_on'].append('u1')
        llm = Replies(initial, raw); llm.requires_plan_review = True
        units = await decompose(llm, 'A fictional comparison?', 'en', Settings(), Recorder())
        self.assertIn('u1', units[2].depends_on)
        self.assertEqual(len(llm.requests), 2)

    def test_run_wrapper_checks_checkpoint_and_does_not_modify_parent_environment(self):
        from argparse import Namespace
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            write_json(folder / 'best.json', {'base_model': 'openai/gpt-oss-120b',
                'judge_prompt_sha256': prompt_hash(), 'checkpoint': 'tinker://fiction/sampler_weights/best'})
            command, env = inference_command(Namespace(run=folder, debug20=False,
                                                       inference_args=['--', '--question', 'Fiction?']))
            self.assertEqual(command[-2:], ['--question', 'Fiction?'])
            self.assertEqual(env['CASCADE_JUDGE_MODEL'], 'tinker://fiction/sampler_weights/best')


if __name__ == '__main__':
    unittest.main()
