"""SDK boundary checks with fictional tokens and futures; no optional imports/API."""
from types import SimpleNamespace as NS
import unittest
from unittest.mock import patch

from cascadesystem.training.sdk import BASE_MODEL, CloudBackend


class Vector(list):
    def tolist(self):
        return list(self)


class Tokens(Vector):
    def to_ints(self):
        return list(self)


class Ready:
    def __init__(self, value, log=None, label=''):
        self.value, self.log, self.label = value, log, label
    def __await__(self):
        async def resolve():
            if self.log is not None:
                self.log.append('await ' + self.label)
            return self.value
        return resolve().__await__()


def backend():
    obj = CloudBackend.__new__(CloudBackend)
    obj.tinker = NS(Datum=lambda **kw: NS(**kw), ModelInput=NS(from_ints=lambda t: t),
                    AdamParams=lambda **kw: kw, SamplingParams=lambda **kw: kw)
    obj.api_key, obj.service, obj.client = 'fictional', None, None
    return obj


class SDKTests(unittest.IsolatedAsyncioTestCase):
    def test_native_windows_training_fails_early_with_wsl_instructions(self):
        with patch('cascadesystem.training.sdk.sys.platform', 'win32'):
            with self.assertRaisesRegex(ValueError, 'WSL/Linux'):
                CloudBackend('fictional')

    def test_official_renderer_mask_is_shifted_with_the_next_token_target(self):
        obj = backend(); obj.train_on = 'last-assistant'
        seen = []
        def build(conversation, train_on_what):
            seen.append((conversation, train_on_what))
            return Tokens([10, 11, 12, 13]), Vector([0, 0, 1, 1])
        obj.renderer = NS(build_supervised_example=build)
        encoded = obj.encode({'payload': {'question': 'Fiction?'}, 'target': {'judgments': []}})
        datum = obj.datum(encoded)
        self.assertEqual(datum.model_input, [10, 11, 12])
        self.assertEqual(datum.loss_fn_inputs, {'target_tokens': [11, 12, 13], 'weights': [0, 1, 1]})
        self.assertEqual(seen[0][1], 'last-assistant')
        self.assertEqual([m['role'] for m in seen[0][0]], ['system', 'user', 'assistant'])
        self.assertNotIn('judgments', seen[0][0][1]['content'])

    async def test_optimizer_submits_before_waiting_and_loss_ignores_prompt_tokens(self):
        obj = backend(); log = []
        result = NS(loss_fn_outputs=[{'logprobs': Vector([-100, -0.2, -0.4])}])
        def submit(label, value):
            log.append('submit ' + label)
            return Ready(value, log, label)
        obj.client = NS(forward_backward=lambda data, loss: submit('backward', result),
                        optim_step=lambda params: submit('optimizer', None))
        numerator, denominator = await obj.train_batch([{'tokens': [1, 2, 3, 4], 'weights': [0, 0, 1, 1]}], 1e-4)
        self.assertEqual(log, ['submit backward', 'submit optimizer', 'await backward', 'await optimizer'])
        self.assertAlmostEqual(numerator, 0.6)
        self.assertEqual(denominator, 2)

    async def test_resume_restores_optimizer_and_close_awaits_explicit_status(self):
        obj = backend(); log = []
        service = NS(create_training_client_from_state_with_optimizer=lambda state: Ready(state),
                     close=lambda status: Ready(None, log, status))
        obj.tinker.ServiceClient = lambda **kw: service
        await obj.start(16, state='tinker://fiction/weights/epoch-0001')
        self.assertEqual(obj.client, 'tinker://fiction/weights/epoch-0001')
        await obj.close('errored')
        self.assertEqual(log, ['await errored'])

    async def test_new_adapter_receives_rank_and_initialization_seed(self):
        obj = backend(); seen = []
        def create(**kw):
            seen.append(kw)
            return Ready('client')
        obj.tinker.ServiceClient = lambda **kw: NS(create_lora_training_client=create)
        await obj.start(16, seed=37)
        self.assertEqual(seen, [{'base_model': BASE_MODEL, 'rank': 16, 'seed': 37}])

    async def test_dev_sampling_uses_final_text_and_rejects_truncation(self):
        obj = backend(); response = NS(sequences=[NS(tokens=[7], stop_reason='stop')]); seen = []
        def sample(**kw):
            seen.append(kw)
            return Ready(response)
        obj.sampler = NS(sample=sample)
        obj.renderer = NS(build_generation_prompt=lambda messages: messages,
                          get_stop_sequences=lambda: [999],
                          parse_response=lambda tokens: ({'content': [
                              {'type': 'thinking', 'text': 'private fictional reasoning'},
                              {'type': 'text', 'text': '{"judgments": []}'}]}, NS(is_clean=True)))
        self.assertEqual(await obj.sample({'question': 'Fiction?'}), {'judgments': []})
        self.assertEqual(seen[0]['sampling_params']['stop'], [999])
        self.assertEqual(len(seen[0]['prompt']), 2)
        response.sequences[0].stop_reason = 'length'
        with self.assertRaisesRegex(ValueError, 'token limit'):
            await obj.sample({'question': 'Fiction?'})

    def test_misaligned_logprobs_are_rejected(self):
        with self.assertRaisesRegex(ValueError, 'alignment'):
            CloudBackend.weighted_loss(NS(loss_fn_outputs=[{'logprobs': Vector([-1])}]),
                                       [{'weights': [0, 1, 1]}])


if __name__ == '__main__':
    unittest.main()
