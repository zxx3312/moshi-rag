"""Lazy Tinker SDK boundary. Importing this module performs no network action."""
import importlib.metadata
import inspect
import math
import sys

from ..llm import JUDGE, parse_object

BASE_MODEL = 'openai/gpt-oss-120b'
RENDERER = 'gpt_oss_low_reasoning'


def messages(record):
    import json
    return [{'role': 'system', 'content': JUDGE},
            {'role': 'user', 'content': json.dumps(record['payload'], ensure_ascii=False)}]


class CloudBackend:
    def __init__(self, api_key):
        if sys.platform == 'win32':
            raise ValueError('Use WSL/Linux for train/evaluate: the pinned official Cookbook requires '
                             'tml-renderers, which supports Linux/macOS. Checkpoint run still works on Windows.')
        try:
            import tinker
            from tinker_cookbook.renderers import get_renderer, TrainOnWhat
            from tinker_cookbook.tokenizer_utils import get_tokenizer
        except ImportError as error:
            raise ValueError('Install cascadesystem/training/requirements.txt in the training environment') from error
        self.tinker = tinker
        self.api_key = api_key
        self.tokenizer = get_tokenizer(BASE_MODEL)  # Tokenizer download, not 120B weights.
        self.renderer = get_renderer(RENDERER, self.tokenizer)
        self.train_on = TrainOnWhat.LAST_ASSISTANT_MESSAGE
        self.versions = {name: importlib.metadata.version(name) for name in ['tinker', 'tinker-cookbook']}
        self.client = self.service = None

    def encode(self, record):
        import json
        conversation = messages(record) + [{'role': 'assistant', 'content': json.dumps(record['target'], ensure_ascii=False)}]
        model_input, weights = self.renderer.build_supervised_example(conversation, train_on_what=self.train_on)
        tokens, values = model_input.to_ints(), weights.tolist()
        return {'tokens': tokens, 'weights': values}

    def datum(self, encoded):
        return self.tinker.Datum(model_input=self.tinker.ModelInput.from_ints(encoded['tokens'][:-1]),
            loss_fn_inputs={'target_tokens': encoded['tokens'][1:], 'weights': encoded['weights'][1:]})

    async def start(self, rank, state=None, seed=42):
        self.service = self.tinker.ServiceClient(api_key=self.api_key, display_name='cascade-evidence-judge')
        if state:
            self.client = await self.service.create_training_client_from_state_with_optimizer(state)
        else:
            self.client = await self.service.create_lora_training_client(base_model=BASE_MODEL, rank=rank, seed=seed)

    @staticmethod
    def weighted_loss(result, encoded):
        numerator, denominator = 0.0, 0.0
        if len(result.loss_fn_outputs) != len(encoded):
            raise ValueError('Training result does not match batch')
        for output, item in zip(result.loss_fn_outputs, encoded):
            logprobs = output['logprobs'].tolist()
            weights = item['weights'][1:]
            if len(logprobs) != len(weights):
                raise ValueError('Training token/logprob alignment mismatch')
            numerator -= sum(float(p) * w for p, w in zip(logprobs, weights))
            denominator += sum(weights)
        if denominator <= 0 or not math.isfinite(numerator):
            raise ValueError('Non-finite or empty supervised loss')
        return numerator, denominator

    async def train_batch(self, encoded, learning_rate):
        backward = self.client.forward_backward([self.datum(row) for row in encoded], 'cross_entropy')
        optimizer = self.client.optim_step(self.tinker.AdamParams(learning_rate=learning_rate))
        result = await backward
        await optimizer
        return self.weighted_loss(result, encoded)

    async def loss_batch(self, encoded):
        result = await self.client.forward([self.datum(row) for row in encoded], 'cross_entropy')
        return self.weighted_loss(result, encoded)

    async def save(self, name):
        state = await self.client.save_state(name=name)
        sample = await self.client.save_weights_for_sampler(name=name)
        return {'state': state.path, 'checkpoint': sample.path}

    async def sample(self, payload, checkpoint=None, max_tokens=4096):
        # Used for dev evaluation with exactly the same renderer as training.
        if not hasattr(self, 'sampler'):
            self.service = self.tinker.ServiceClient(api_key=self.api_key, display_name='cascade-judge-dev')
            self.sampler = await self.service.create_sampling_client(
                **({'model_path': checkpoint} if checkpoint else {'base_model': BASE_MODEL}))
        record = {'payload': payload}
        prompt = self.renderer.build_generation_prompt(messages(record))
        result = await self.sampler.sample(prompt=prompt, num_samples=1,
            sampling_params=self.tinker.SamplingParams(max_tokens=max_tokens, temperature=0,
                                                       stop=self.renderer.get_stop_sequences()))
        sequence = result.sequences[0]
        if sequence.stop_reason == 'length':
            raise ValueError('Judge sample reached its token limit')
        message, termination = self.renderer.parse_response(sequence.tokens)
        if not termination.is_clean or message.get('tool_calls') or message.get('unparsed_tool_calls'):
            raise ValueError('Malformed judge completion')
        content = message['content']
        text = content if isinstance(content, str) else ''.join(p['text'] for p in content if p['type'] == 'text')
        return parse_object(text)

    async def close(self, status='success'):
        if self.service is not None:
            # Finish the session while retaining its explicitly saved checkpoints.
            close = getattr(self.service, 'close', None)
            if close:
                result = close(status)
                if inspect.isawaitable(result):
                    await result
