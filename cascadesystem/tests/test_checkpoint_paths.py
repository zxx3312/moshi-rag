"""SDK-style checkpoint paths with fictional IDs; no remote calls."""
from argparse import Namespace
import json
from pathlib import Path
import tempfile
import unittest

from cascadesystem.config import Settings
from cascadesystem.llm import TinkerLLM
from cascadesystem.tests.test_lora_training import FakeBackend, prepared
from cascadesystem.tests.test_system import FakeHTTP
from cascadesystem.training.__main__ import inference_command
from cascadesystem.training.engine import check_checkpoint, checkpoint_info, train


RUN_ID = '00000000-1111-2222-3333-444444444444:train:0'
PATH = f'tinker://{RUN_ID}/sampler_weights/epoch-0001'


class CheckpointPathTests(unittest.IsolatedAsyncioTestCase):
    def test_sdk_client_suffix_and_legacy_paths_are_preserved(self):
        for value in [PATH, 'tinker://fiction/sampler_weights/epoch-0001']:
            self.assertEqual(check_checkpoint(value), value)

    def test_non_sampler_and_malformed_paths_are_rejected(self):
        for value in [None, 123, [], PATH.replace('sampler_weights', 'weights'),
                      PATH.replace('tinker://', 'https://'), PATH + '?key=value',
                      PATH + '\n', PATH + '/extra', f'tinker://{RUN_ID}/sampler_weights/']:
            with self.subTest(value=value), self.assertRaises(ValueError):
                check_checkpoint(value)

    async def test_colon_run_id_survives_training_best_selection_and_inference_wrapper(self):
        class SDKPathBackend(FakeBackend):
            async def save(self, name):
                return {'state': f'tinker://{RUN_ID}/weights/{name}',
                        'checkpoint': f'tinker://{RUN_ID}/sampler_weights/{name}'}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); prepared(root / 'inputs')
            output = await train(SDKPathBackend(), inputs=root / 'inputs', output=root / 'run',
                                 epochs=1, batch_size=2)
            self.assertEqual(checkpoint_info(output)['checkpoint'], PATH)
            events = [json.loads(line) for line in (output / 'events.jsonl').read_text().splitlines()]
            self.assertEqual(next(e['checkpoint'] for e in events if e['type'] == 'checkpoint_saved'), PATH)
            _, env = inference_command(Namespace(run=output, debug20=False,
                                                inference_args=['--', '--question', 'Fiction?']))
            self.assertEqual(env['CASCADE_JUDGE_MODEL'], PATH)

    async def test_http_judge_request_keeps_sdk_checkpoint_string_intact(self):
        http = FakeHTTP({'choices': [{'finish_reason': 'stop', 'message': {'content': '{}'}}]})
        llm = TinkerLLM(Settings(api_key='fictional', judge_model=PATH), http)
        await llm.complete('judge', 'JSON', {})
        self.assertEqual(http.requests[0][1]['body']['model'], PATH)


if __name__ == '__main__':
    unittest.main()
