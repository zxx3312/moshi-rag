"""GPU-side job for the controlled retrieval-latency experiment.

Imports torch and moshi: only ``run_latency_sweep.py`` in non-dry-run mode may import it.

``LatencyInferenceJob`` subclasses the repo's offline ``InferenceJob`` and reuses its
feed loop (user WAV -> Mimi frames), STT loop and the shared batched step loop
unchanged. Only the output loop is overridden, with these differences from the parent:

1. Retrieval goes to ``FixedReferenceBackend`` (via ``FixedReferenceRAGManager``),
   which returns the same reference for every request. No LLM is called.
2. Latency is imposed on the model stream clock. The parent pauses the model while
   the retrieval is in flight and then converts the measured wall-clock time into
   ``floor(elapsed * frame_rate)`` model steps. Here the reference is injected at
   ``request_step + delay_steps`` directly, where ``request_step`` is the parent's
   ``retrieval_step`` (the [RET] step + STT wait steps).
3. The reference embedding is pre-encoded once per distinct reference by the
   reference-encoder service. In the parent the encoder call also pauses the
   model, so this does not change what the model sees.
4. The tail-silence stop is not applied while a retrieval is pending, and it counts
   silence from the last injection. A hard cap (``max_response_seconds``) bounds every run.
   Otherwise a long delay could end the run before the reference is ever injected.
5. Per-step data is recorded: text piece, model audio RMS, and the retrieval events.
"""

from __future__ import annotations

import asyncio
import json
import logging
import math
import time
import wave
from pathlib import Path
from typing import Any

import numpy as np

from moshi.inference_utils.inference_job import InferenceJob, _load_audio_mono_float32
from moshi.inference_utils.rag_manager import RAGManager
from moshi.inference_utils.utils import get_conditioning_remote_async

from mock_retrieval import FixedReferenceBackend

logger = logging.getLogger(__name__)

PAD = "<pad>"


def _rms_db(pcm: np.ndarray | None) -> float | None:
    if pcm is None or pcm.size == 0:
        return None
    rms = float(np.sqrt(np.mean(np.square(pcm.astype(np.float64)))))
    return round(20.0 * math.log10(rms + 1e-12), 1)


def _write_wav_int16(path: Path, channels: list[np.ndarray], sample_rate: int) -> None:
    n = max(len(c) for c in channels)
    data = np.zeros((n, len(channels)), dtype=np.float32)
    for i, c in enumerate(channels):
        data[: len(c), i] = c
    pcm_i16 = (np.clip(data, -1.0, 1.0) * 32767.0).astype(np.int16)
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "wb") as wf:
        wf.setnchannels(len(channels))
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(pcm_i16.tobytes())


class FixedReferenceRAGManager(RAGManager):
    """``RAGManager`` whose backend is a ``FixedReferenceBackend`` instead of an LLM."""

    def __init__(self, backend: FixedReferenceBackend, rag_timeout: float, max_tokens: int):
        super().__init__(reference_generator=None, rag_timeout=rag_timeout, max_tokens=max_tokens)  # type: ignore[arg-type]
        self.backend = backend

    async def get_reference_text(self, context: str) -> tuple[str, str, float, str]:
        result = await self.backend.retrieve(context)
        logger.info(
            "[MockRetrieval] request #%d -> fixed reference (available after %d steps)",
            result.request_index,
            result.available_after_steps,
        )
        return "", result.reference_text, 0.0, "fixed_reference"

    def warmup(self):
        pass


class LatencyInferenceJob(InferenceJob):
    def __init__(
        self,
        server,
        *,
        sample: dict[str, Any],
        run_id: str,
        run_dir: Path,
        delay_s: float,
        seed: int,
        reference_tensors: dict[str, Any],
        max_tail_silence: int,
        max_response_seconds: float,
        stt,
    ):
        wav_path = Path(sample["wav_path"])
        self.run_dir = run_dir
        self.trace_path = run_dir / "traces" / f"{run_id}.json"
        self.audio_path = run_dir / "audio" / f"{run_id}_model.wav"
        self.stereo_path = run_dir / "audio" / f"{run_id}_stereo.wav"
        super().__init__(
            server,
            wav_path,
            self.trace_path,
            stop_on_end_of_input=False,
            use_gt_reference=False,
            max_tail_silence=max_tail_silence,
            sidecar={
                "gt_user_text": sample.get("question"),
                "gt_reference_text": sample["reference_text"],
                "answer": sample.get("answer"),
            },
            stt=stt,
        )
        mimi = server.runner.mimi
        self.frame_rate = float(mimi.frame_rate)
        self.sample_rate = int(mimi.sample_rate)
        self.frame_size = int(server.frame_size)

        self.backend = FixedReferenceBackend(sample["reference_text"], delay_s, self.frame_rate)
        self.rag_manager = FixedReferenceRAGManager(self.backend, server.rag_timeout, server.max_reference_tokens)
        self.reference_tensors = reference_tensors

        # Same loading/trimming as the parent's _feed_loop, to know where the input ends.
        user_pcm = _load_audio_mono_float32(wav_path, self.sample_rate)
        self.input_frames = len(user_pcm) // self.frame_size
        self.user_pcm = user_pcm[: self.input_frames * self.frame_size]
        self.max_response_steps = int(math.ceil(max_response_seconds * self.frame_rate))

        self.retrieval_events: list[dict[str, Any]] = []
        self._pending_event: dict[str, Any] | None = None
        self._ref_received = asyncio.Event()
        self._received_text: str | None = None
        self._pcm_by_step: list[np.ndarray | None] = []
        self.model_rms_db: list[float | None] = []
        self._tail_anchor_step = self.input_frames
        self._pad_run = 0
        self._wall_start = time.monotonic()

        self.trace["retrieval_events"] = self.retrieval_events
        self.trace["model_rms_db"] = self.model_rms_db
        self.trace["user_rms_db"] = [
            _rms_db(self.user_pcm[i * self.frame_size : (i + 1) * self.frame_size]) for i in range(self.input_frames)
        ]
        self.trace["experiment"] = {
            "run_id": run_id,
            "sample_id": sample["sample_id"],
            "question": sample.get("question"),
            "input_wav": str(wav_path),
            "delay_condition_s": float(delay_s),
            "delay_steps": self.backend.delay_steps,
            "effective_delay_s": self.backend.effective_delay_s,
            "seed": seed,
            "frame_rate": self.frame_rate,
            "sample_rate": self.sample_rate,
            "frame_size": self.frame_size,
            "stt_wait_steps": int(self.turn_manager.stt_wait_steps),
            "input_frames": self.input_frames,
            "max_tail_silence_frames": max_tail_silence,
            "max_response_steps": self.max_response_steps,
            "latency_clock": "model_steps",
            "status": "running",
            "stop_reason": None,
            "error": None,
            "trace_path": str(self.trace_path.relative_to(run_dir)),
            "output_audio_path": str(self.audio_path.relative_to(run_dir)),
            "stereo_audio_path": str(self.stereo_path.relative_to(run_dir)),
            "wall_elapsed_s": None,
        }

    # ------------------------------------------------------------------
    # Retrieval scheduling
    # ------------------------------------------------------------------

    def _on_trigger(self, step: int, wait_steps: int) -> None:
        if self._pending_event is not None:
            # Same as the parent: a new [RET] cancels the in-flight retrieval.
            self._pending_event["superseded_at_step"] = step
        request_step = step + wait_steps
        ev = {
            "index": len(self.retrieval_events),
            "trigger_step": step,
            "request_step": request_step,
            "available_step": request_step + self.backend.delay_steps,
            "reference_received_step": None,
            "injection_step": None,
            "injection_num_steps": None,
            "superseded_at_step": None,
            "backend_wait_wall_s": 0.0,
        }
        self._ref_received = asyncio.Event()
        self._received_text = None
        self._pending_event = ev
        self.retrieval_events.append(ev)
        if self.trace["rag_trigger_step"] == -1:
            self.trace["rag_trigger_step"] = step
            self.trace["retrieval_step"] = request_step
        logger.info(
            "[Latency] [RET] at step %d -> request step %d, reference available at step %d (+%d steps)",
            step,
            request_step,
            ev["available_step"],
            self.backend.delay_steps,
        )

    async def _on_reference(self, reference_text: str | None, lm_label: str = "") -> None:
        ev = self._pending_event
        if ev is None:
            return
        ev["reference_received_step"] = self.step_index
        self._received_text = reference_text or ""
        self._ref_received.set()

    async def _inject(self, ev: dict[str, Any], step: int) -> None:
        if not self._ref_received.is_set():
            # Practically never happens (the mock backend returns immediately), but if it
            # does, waiting here pauses the model, which keeps the stream-clock delay exact.
            t0 = time.monotonic()
            await asyncio.wait_for(self._ref_received.wait(), timeout=60.0)
            ev["backend_wait_wall_s"] = round(time.monotonic() - t0, 4)
        text = self._received_text or ""
        tensor = self.reference_tensors.get(text)
        if tensor is None:
            remote = await get_conditioning_remote_async(text=text, encoder_url=self.server.reference_encoder_url)
            tensor = remote.squeeze(0).cpu()
            self.reference_tensors[text] = tensor
        per_slot: list[Any] = [None] * self.server.batch_size
        per_slot[self.slot_idx] = tensor
        self.server.runner.lm_gen.update_streaming_sum_tensors(per_slot)

        ev["injection_step"] = step
        ev["injection_num_steps"] = int(tensor.shape[0])
        self._pending_event = None
        self.trace["reference_text"] = text
        if self.trace["conditioning_step"] == -1:
            self.trace["conditioning_step"] = step
        self._tail_anchor_step = max(self._tail_anchor_step, step + 1)
        self._pad_run = 0
        logger.info("[Latency] injected reference at step %d (%d conditioning steps)", step, tensor.shape[0])

    # ------------------------------------------------------------------
    # Output loop (overrides InferenceJob._output_loop)
    # ------------------------------------------------------------------

    def _stop_reason(self, step: int) -> str | None:
        if step < self.input_frames:
            return None
        if step >= self.input_frames + self.max_response_steps:
            return "max_response"
        if self._pending_event is not None:
            return None
        if step >= self._tail_anchor_step:
            self._pad_run = self._pad_run + 1 if self.model_text[-1] == PAD else 0
            if self.max_tail_silence is not None and self._pad_run > self.max_tail_silence:
                return "tail_silence"
        return None

    async def _output_loop(self) -> None:
        assert self._task_group is not None
        rag_token_id = self.server.runner.lm_gen.lm_model.rag_token_id
        wait_steps = int(self.turn_manager.stt_wait_steps)
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
                self._on_trigger(step, wait_steps)
                self.model_text.append(self.server.text_tokenizer.id_to_piece(text_token))  # type: ignore[arg-type]
                await self.rag_manager.trigger(
                    task_group=self._task_group,
                    wait_steps=wait_steps,
                    handle_reference_fn=self._on_reference,
                    context_provider=self.turn_manager.get_context,
                )
            else:
                decoded = self._decode_text_token(text_token)
                self.turn_manager.handle_spoken_text(model_text=decoded)
                if decoded is None:
                    self.model_text.append(PAD)
                else:
                    self.model_text.append(self.server.text_tokenizer.id_to_piece(text_token))  # type: ignore[arg-type]

            if self._user_id_buffer:
                uid = self._user_id_buffer.popleft()
                self.user_text.append(self.stt.text_tokenizer.id_to_piece(uid))  # type: ignore[arg-type]
            else:
                self.user_text.append(PAD)

            self.rag_manager.step()
            ev = self._pending_event
            if ev is not None and step >= ev["available_step"]:
                await self._inject(ev, step)

            async with self._pcm_one_step_cv:
                self.step_index += 1
                self._pcm_one_step_cv.notify_all()

            reason = self._stop_reason(step)
            if reason is not None:
                await self._finalize_run("completed", reason)
                return

    async def _finalize(self) -> None:
        await self._finalize_run("completed", "parent_finalize")

    async def _finalize_run(self, status: str, reason: str) -> None:
        self._shutdown_event.set()
        async with self._pcm_one_step_cv:
            self._pcm_one_step_cv.notify_all()
        self.rag_manager.cancel_pending()
        self.write_outputs(status=status, reason=reason)
        self._done.set()

    # ------------------------------------------------------------------
    # Outputs
    # ------------------------------------------------------------------

    def write_outputs(self, status: str, reason: str | None, error: str | None = None) -> None:
        """Write trace JSON and audio. Synchronous, so it is also safe after a timeout/cancel."""
        exp = self.trace["experiment"]
        exp["status"] = status
        exp["stop_reason"] = reason
        exp["error"] = error
        exp["wall_elapsed_s"] = round(time.monotonic() - self._wall_start, 3)
        exp["num_steps"] = len(self.model_text)
        exp["mock_backend_requests"] = len(self.backend.requests)
        self.trace["model_text"] = self.model_text
        self.trace["user_text"] = self.user_text

        self.trace_path.parent.mkdir(parents=True, exist_ok=True)
        self.trace_path.write_text(json.dumps(self.trace, indent=1), encoding="utf-8")

        # Model audio aligned to the step clock (zeros for steps without audio output).
        silence = np.zeros(self.frame_size, dtype=np.float32)
        model = np.concatenate([p if p is not None else silence for p in self._pcm_by_step]) \
            if self._pcm_by_step else np.zeros(0, dtype=np.float32)
        if model.size:
            _write_wav_int16(self.audio_path, [model], self.sample_rate)
            _write_wav_int16(self.stereo_path, [self.user_pcm, model], self.sample_rate)
