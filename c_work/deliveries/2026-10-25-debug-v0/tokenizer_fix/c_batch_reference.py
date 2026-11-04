import gc
import json
import os
import random
import runpy
import sys
import wave
from pathlib import Path

root = Path.home() / "projects/moshi-rag"
data = root / "c_work/debug-v0"
source = (
    Path.home()
    / "projects/moshi-rag-b-data/b_work/step2/prepared/samples_debug.jsonl"
)

records = [
    json.loads(line)
    for line in source.read_text(encoding="utf-8").splitlines()
    if line.strip()
]
questions = {
    row["sample_id"]: row["question"]
    for row in (
        json.loads(line)
        for line in (data / "questions_only.jsonl").read_text(
            encoding="utf-8"
        ).splitlines()
        if line.strip()
    )
}

assert len(records) == 20, "Expected 20 samples"
assert len({row["sample_id"] for row in records}) == 20
assert set(questions) == {row["sample_id"] for row in records}

samples = []
for row in records:
    sample_id = row["sample_id"]
    assert row["question"] == questions[sample_id]
    audio_path = data / "audio" / (sample_id + ".wav")
    with wave.open(str(audio_path), "rb") as wav:
        assert wav.getframerate() == 24000
        assert wav.getnchannels() == 1
        assert wav.getsampwidth() == 2

    reference = "\n\n".join(
        str(title) + "\n" + " ".join(sentences)
        for title, sentences in row["context"]
    )
    assert reference.strip(), "Empty reference"
    samples.append({
        "schema_version": row["schema_version"],
        "data_version": row["data_version"],
        "sample_id": sample_id,
        "dataset": row["dataset"],
        "question": row["question"],
        "audio_path": str(audio_path),
        "reference_text": reference,
    })

if "--check-only" in sys.argv:
    print("INPUT CHECK PASSED: 20/20")
    raise SystemExit(0)

import numpy as np
import torch
from safetensors.torch import save_file
from moshi.server_conditioner import EncoderService
from moshi.models import LMGen
from moshi.conditioners.base import ConditionAttributes

assert torch.cuda.is_available(), "Run this script through a GPU job"
job_id = os.environ["SLURM_JOB_ID"]
out = data / "runs" / ("reference-batch-" + job_id)
out.mkdir(parents=True, exist_ok=False)

(out / "inputs.jsonl").write_text(
    "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in samples),
    encoding="utf-8",
)

references = {}
with torch.inference_mode():
    service = EncoderService(
        config=str(root / "tokenizer_fix/artifacts/moshirag.local.json"),
        moshi_weight=str(
            Path.home() / "models/moshika-rag-pytorch-bf16/model.safetensors"
        ),
        conditioner="reference_with_time",
        device="cuda:0",
    )
    service.condition_provider.eval()
    for index, sample in enumerate(samples, 1):
        print(f"ENCODING [{index}/20] {sample['sample_id']}", flush=True)
        tensor = service.encode(sample["reference_text"])
        assert torch.isfinite(tensor).all().item()
        tensor = tensor.detach().cpu().contiguous()
        references[sample["sample_id"]] = tensor
        folder = out / sample["sample_id"]
        folder.mkdir()
        save_file({"tensor": tensor}, str(folder / "reference.safetensors"))

del service
gc.collect()
torch.cuda.empty_cache()

loaded = runpy.run_path(str(root / "scripts/c_smoke_load.py"))
model = loaded["model"]
mimi = loaded["mimi"]
tokenizer = loaded["checkpoint"].get_text_tokenizer()
model.eval()
frame_rate = float(mimi.frame_rate)
frame_size = int(mimi.sample_rate / frame_rate)

with torch.inference_mode(), (out / "results.jsonl").open(
    "x", encoding="utf-8"
) as log:
    attrs = [ConditionAttributes(
        text={"first_speaker": "SPEAKER_OTHER"}
    )]
    conditions = model.condition_provider(
        model.condition_provider.prepare(attrs)
    )

    for number, sample in enumerate(samples, 1):
        sample_id = sample["sample_id"]
        reference = references[sample_id]
        print(f"GENERATING [{number}/20] {sample_id}", flush=True)

        with wave.open(sample["audio_path"], "rb") as wav:
            audio = np.frombuffer(
                wav.readframes(wav.getnframes()), dtype="<i2"
            ).astype(np.float32) / 32768.0

        audio_duration = len(audio) / 24000
        injection_step = (len(audio) + frame_size - 1) // frame_size
        audio = np.pad(audio, (0, (-len(audio)) % frame_size))

        # Allow the entire reference plus 20 additional seconds.
        tail_frames = int(reference.shape[1]) + int(20 * frame_rate)
        audio = np.concatenate([
            audio,
            np.zeros(tail_frames * frame_size, dtype=np.float32),
        ])
        frames = torch.from_numpy(audio).to("cuda").reshape(1, 1, -1)

        random.seed(42)
        np.random.seed(42)
        torch.manual_seed(42)
        torch.cuda.manual_seed_all(42)

        generator = LMGen(
            model,
            condition_tensors=conditions,
            force_streaming_sum=True,
            profile=True,
        )
        chunks = []
        text_ids = []
        text_events = []
        applied = 0
        exec_mask = torch.tensor([True], dtype=torch.bool)

        with mimi.streaming(1), generator.streaming(1):
            for step, frame in enumerate(frames.split(frame_size, dim=-1)):
                if step == injection_step:
                    generator.update_streaming_sum_tensors([reference[0]])
                    print("REFERENCE INJECTION STARTED", flush=True)

                generator.apply_pending_streaming_sum_condition(exec_mask)

                if injection_step <= step < injection_step + reference.shape[1]:
                    applied += 1

                tokens = generator.step(mimi.encode(frame))
                if tokens is not None:
                    pcm = mimi.decode(tokens[:, 1:, :])
                    chunks.append(pcm[0, 0].float().cpu().numpy())
                    token = int(tokens[0, 0, 0])
                    text_events.append({"step": step, "token_id": token})
                    if token not in (0, 3, model.rag_token_id):
                        text_ids.append(token)

                if step % 200 == 0:
                    print(f"PROCESSED FRAMES: {step}", flush=True)

        assert chunks, "No response audio generated"
        assert applied == reference.shape[1], "Incomplete reference delivery"

        answer = tokenizer.decode(text_ids).replace("\x00", "")
        folder = out / sample_id
        wav_path = folder / "response.wav"
        pcm = np.concatenate(chunks)

        with wave.open(str(wav_path), "wb") as wav:
            wav.setnchannels(1)
            wav.setsampwidth(2)
            wav.setframerate(int(mimi.sample_rate))
            wav.writeframes(
                (np.clip(pcm, -1, 1) * 32767).astype("<i2").tobytes()
            )

        result = {
            **sample,
            "variant": "full_context_reference_debug",
            "seed": 42,
            "reference_selection": "all_context_documents_in_source_order",
            "injection_basis": "end_of_question_audio_file",
            "question_audio_duration_s": audio_duration,
            "injection_step": injection_step,
            "reference_frames_applied": applied,
            "frame_rate": frame_rate,
            "tail_silence_s": tail_frames / frame_rate,
            "generated_text": answer,
            "text_token_events": text_events,
            "response_wav": str(wav_path),
        }
        payload = json.dumps(result, ensure_ascii=False)
        (folder / "result.json").write_text(payload, encoding="utf-8")
        log.write(payload + "\n")
        log.flush()
        print("ANSWER:", answer, flush=True)
        print(f"COMPLETED [{number}/20]", flush=True)

print("RESULT DIRECTORY:", out, flush=True)
print("BATCH REFERENCE COMPLETED: 20/20", flush=True)
