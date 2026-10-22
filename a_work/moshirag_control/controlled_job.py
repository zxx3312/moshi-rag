"""GPU job: run MoshiRAG on one spoken question under a control plan.

Subclasses the diagnosis experiment's LatencyInferenceJob and keeps its feed loop,
STT loop, per-step recording and output files. Differences:

1. Two LMGen hooks drive a TextController. Before each text token is sampled the
   disallowed logits are set to -inf; after sampling the token is reported back.
2. Evidence is injected on the trace schedule (seconds after the question ends),
   not when the model emits [RET]. The hand-over happens inside the logits hook at
   step k, so the reference is consumed from step k+1 on: exact to the step.
3. [RET] tokens are only recorded; they start no retrieval.

Step clock: hook step k == input frame k == output step k (text sampled at step k is
delivered with output k), 12.5 steps per second.
"""
from __future__ import annotations

import logging
from typing import Any

import torch

from latency_job import PAD, LatencyInferenceJob, _rms_db

from control import Plan, TextController, TokenIds

logger = logging.getLogger(__name__)


def question_end_step(user_rms_db: list, speech_db: float, input_frames: int) -> int:
    """Same rule as analysis/metrics.py: one past the last input frame above speech_db."""
    speech = [i for i, db in enumerate(user_rms_db) if db is not None and db > speech_db]
    return speech[-1] + 1 if speech else input_frames


class ControlledJob(LatencyInferenceJob):
    def __init__(self, server, *, sample: dict[str, Any], plan: Plan, run_id: str, run_dir, seed: int,
                 reference_tensors: dict[str, Any], max_tail_silence: int, max_response_seconds: float,
                 speech_db: float, stt):
        base = dict(sample, reference_text=plan.injections[0].text)  # parent needs one; its backend is unused
        super().__init__(server, sample=base, run_id=run_id, run_dir=run_dir, delay_s=0.0, seed=seed,
                         reference_tensors=reference_tensors, max_tail_silence=max_tail_silence,
                         max_response_seconds=max_response_seconds, stt=stt)
        lm = server.runner.lm_gen.lm_model
        self.ids = TokenIds(pad=lm.text_padding_token_id, epad=lm.end_of_text_padding_id, ret=lm.rag_token_id)
        self.q_end = question_end_step(self.trace["user_rms_db"], speech_db, self.input_frames)
        self.ctrl = TextController(plan, question_end_step=self.q_end, frame_rate=self.frame_rate, ids=self.ids,
                                   encode=lambda s: server.text_tokenizer.encode(s))
        self.plan = plan
        self.sample = sample
        self._lm_step = 0
        self._restricted = False
        self.injections: list[dict[str, Any]] = []
        self.ret_steps: list[int] = []
        exp = self.trace["experiment"]
        exp.update(condition=plan.condition, delay_condition_s=None, delay_steps=None, effective_delay_s=None)
        # Tail-silence stop only after everything scheduled has happened.
        self._tail_anchor_step = max(self.input_frames, self.ctrl.last_scheduled_step + 1)

    # ------------------------------------------------------------------ hooks (step loop)

    def _on_logits(self, logits: torch.Tensor) -> None:
        k = self._lm_step
        for i, inj in self.ctrl.injections_due(k):
            tensor = self.reference_tensors[inj.text]
            per_slot: list[Any] = [None] * self.server.batch_size
            per_slot[self.slot_idx] = tensor
            self.server.runner.lm_gen.update_streaming_sum_tensors(per_slot)
            self.injections.append({
                "label": inj.label, "text": inj.text, "scheduled_step": self.ctrl.injection_steps[i],
                "handover_step": k, "num_steps": int(tensor.shape[0]),
            })
            logger.info("[Control] step %d: injected %s (%d steps)", k, inj.label, tensor.shape[0])
        allowed = self.ctrl.allowed(k)
        self._restricted = allowed is not None
        if allowed is not None:
            row = logits[self.slot_idx, 0, 0]
            idx = torch.tensor(allowed, device=row.device)
            keep = row.index_select(0, idx)
            row.fill_(float("-inf"))
            row.index_copy_(0, idx, keep)

    def _on_text(self, tokens: torch.Tensor) -> None:
        self.ctrl.on_sampled(self._lm_step, int(tokens[self.slot_idx].item()), self._restricted)
        self._lm_step += 1

    async def run(self, rag_task_group) -> None:
        lm_gen = self.server.runner.lm_gen
        lm_gen.on_text_logits_hook, lm_gen.on_text_hook = self._on_logits, self._on_text
        try:
            await super().run(rag_task_group)
        finally:
            lm_gen.on_text_logits_hook, lm_gen.on_text_hook = None, None

    # ------------------------------------------------------------------ output loop

    async def _output_loop(self) -> None:
        rag_token_id = self.server.runner.lm_gen.lm_model.rag_token_id
        while not self._shutdown_event.is_set():
            out = await self.output_queue.get()
            step = self.step_index

            pcm = None
            if out.pcm is not None:
                pcm = out.pcm.detach().cpu().float().numpy().reshape(-1)
                self._model_pcm_chunks.append(pcm)
            self._pcm_by_step.append(pcm)
            self.model_rms_db.append(_rms_db(pcm))

            text_token = out.text_token
            if text_token == rag_token_id:
                self.ret_steps.append(step)
                self.model_text.append("[RET]")
            else:
                decoded = self._decode_text_token(text_token)
                self.turn_manager.handle_spoken_text(model_text=decoded)
                self.model_text.append(PAD if decoded is None else self.server.text_tokenizer.id_to_piece(text_token))

            if self._user_id_buffer:
                self.user_text.append(self.stt.text_tokenizer.id_to_piece(self._user_id_buffer.popleft()))
            else:
                self.user_text.append(PAD)

            async with self._pcm_one_step_cv:
                self.step_index += 1
                self._pcm_one_step_cv.notify_all()

            reason = self._stop_reason(step)
            if reason is not None:
                await self._finalize_run("completed", reason)
                return

    def write_outputs(self, status: str, reason: str | None, error: str | None = None) -> None:
        self.trace["control"] = {
            "condition": self.plan.condition,
            "question_end_step": self.q_end,
            "segments": [{"start_step": s, "mode": seg.mode, "phrase": seg.phrase}
                         for s, seg in zip(self.ctrl.segment_steps, self.plan.segments)],
            "injections": self.injections,
            "ret_steps": self.ret_steps,
            "lm_steps": self._lm_step,
            "rows": self.ctrl.rows,
            "token_ids": {"pad": self.ids.pad, "epad": self.ids.epad, "ret": self.ids.ret},
            "events": self.sample["events"],
            "units": self.sample["units"],
        }
        super().write_outputs(status, reason, error)
