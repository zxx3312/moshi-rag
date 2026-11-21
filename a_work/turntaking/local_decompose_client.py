"""Local Transformers backend for A's unchanged decomposer prompts and validator.

Unlike the vLLM client this uses unconstrained greedy decoding; validate_units still
checks every reply. Intended for offline dataset construction when vLLM is unavailable.
"""
import time
from types import SimpleNamespace
from .decompose import build_messages
from .llm import parse_json_object


class LocalDecomposeClient:
    def __init__(self, model_path, questions, batch_size=8):
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
        self.torch = torch
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True, padding_side='left')
        if self.tokenizer.pad_token_id is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path, local_files_only=True, torch_dtype=torch.bfloat16,
            attn_implementation='sdpa').to('cuda').eval()
        self.questions = questions
        self.position = 0
        self.batch_size = batch_size
        self.pending = {}
        self.calls = []
        self.tape = []

    def chat_json(self, messages, *, purpose, schema=None):
        question = messages[-1]['content'][len('Question: '):]
        if question not in self.pending:
            batch = self.questions[self.position:self.position+self.batch_size]
            self.position += len(batch)
            assert question in batch
            prompts = [self.tokenizer.apply_chat_template(build_messages(q), tokenize=False,
                       add_generation_prompt=True, enable_thinking=False) for q in batch]
            inputs = self.tokenizer(prompts, return_tensors='pt', padding=True).to('cuda')
            start = time.monotonic()
            with self.torch.inference_mode():
                outputs = self.model.generate(**inputs, max_new_tokens=1024, do_sample=False,
                                              pad_token_id=self.tokenizer.pad_token_id)
            elapsed = time.monotonic()-start
            texts = self.tokenizer.batch_decode(outputs[:, inputs['input_ids'].shape[1]:], skip_special_tokens=True)
            self.pending.update({q: (text, elapsed/len(batch)) for q,text in zip(batch,texts)})
        raw, elapsed = self.pending.pop(question)
        self.calls.append(SimpleNamespace(latency_s=elapsed))
        self.tape.append(dict(purpose=purpose, raw_text=raw, latency_s=elapsed,
                              backend='transformers', latency_note='batch elapsed divided by batch size'))
        return parse_json_object(raw)
