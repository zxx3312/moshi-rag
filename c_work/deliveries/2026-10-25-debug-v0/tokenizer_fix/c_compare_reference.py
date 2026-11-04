import gc
import json
import os
import random
import runpy
import wave
from pathlib import Path

import numpy as np
import torch
from safetensors.torch import save_file
from moshi.server_conditioner import EncoderService
from moshi.models import LMGen
from moshi.conditioners.base import ConditionAttributes

root = Path.home() / "projects/moshi-rag"
data = root / "c_work/debug-v0"

records = [
    json.loads(line)
    for line in (data / "questions_only.jsonl").read_text().splitlines()
    if line.strip()
]
record = next(
    row for row in records
    if row["sample_id"] == "custom_nasa_apollo11"
)
audio_path = data / "audio" / (record["sample_id"] + ".wav")

with wave.open(str(audio_path), "rb") as wav:
    assert wav.getframerate() == 24000
    assert wav.getnchannels() == 1 and wav.getsampwidth() == 2
    question_audio = np.frombuffer(
        wav.readframes(wav.getnframes()), dtype="<i2"
    ).astype(np.float32) / 32768.0

assert torch.cuda.is_available(), "请通过 sbatch 在 GPU 上运行"

job_id = os.environ["SLURM_JOB_ID"]
out = data / "runs" / ("reference-compare-" + job_id)
out.mkdir(parents=True, exist_ok=False)

reference = (
    "Apollo 11 launched on July 16, 1969. "
    "The mission ended with splashdown on July 24, 1969."
)

print("问题：", record["question"], flush=True)
print("参考资料：", reference, flush=True)
print("正在编码参考资料……", flush=True)

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
    reference_tensor = service.encode(reference).detach().cpu().contiguous()
    assert torch.isfinite(reference_tensor).all().item()

save_file({"tensor": reference_tensor}, str(out / "reference.safetensors"))

del service
gc.collect()
torch.cuda.empty_cache()

# 复用之前已成功的 Moshi 和 Mimi 加载程序。
loaded = runpy.run_path(str(root / "scripts/c_smoke_load.py"))
model = loaded["model"]
mimi = loaded["mimi"]
tokenizer = loaded["checkpoint"].get_text_tokenizer()
model.eval()

frame_size = int(mimi.sample_rate / mimi.frame_rate)
injection_step = (
    len(question_audio) + frame_size - 1
) // frame_size

# 问题音频结束后继续输入 20 秒静音，给模型回答时间。
audio = np.concatenate([
    question_audio, np.zeros(20 * 24000, dtype=np.float32)
])
audio = np.pad(audio, (0, (-len(audio)) % frame_size))
frames = torch.from_numpy(audio).to("cuda").reshape(1, 1, -1)

results = []

with torch.inference_mode():
    attrs = [ConditionAttributes(
        text={"first_speaker": "SPEAKER_OTHER"}
    )]
    prepared = model.condition_provider.prepare(attrs)
    conditions = model.condition_provider(prepared)

    for variant in ("no_reference", "with_reference"):
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
        applied = 0
        exec_mask = torch.tensor([True], dtype=torch.bool)

        print("开始运行：", variant, flush=True)

        with mimi.streaming(1), generator.streaming(1):
            for index, frame in enumerate(frames.split(frame_size, dim=-1)):
                if variant == "with_reference" and index == injection_step:
                    generator.update_streaming_sum_tensors(
                        [reference_tensor[0]]
                    )
                    print("已开始送入参考资料", flush=True)

                generator.apply_pending_streaming_sum_condition(exec_mask)

                if (
                    variant == "with_reference"
                    and injection_step <= index
                    < injection_step + reference_tensor.shape[1]
                ):
                    applied += 1

                tokens = generator.step(mimi.encode(frame))
                if tokens is not None:
                    pcm = mimi.decode(tokens[:, 1:, :])
                    chunks.append(pcm[0, 0].float().cpu().numpy())
                    token = int(tokens[0, 0, 0])
                    if token not in (0, 3, model.rag_token_id):
                        text_ids.append(token)

                if index % 100 == 0:
                    print("已处理帧数：", index, flush=True)

        assert chunks, "没有生成回答音频"
        if variant == "with_reference":
            assert applied == reference_tensor.shape[1]

        answer = tokenizer.decode(text_ids).replace("\x00", "")
        pcm = np.concatenate(chunks)
        wav_path = out / (variant + ".wav")

        with wave.open(str(wav_path), "wb") as wav:
            wav.setnchannels(1)
            wav.setsampwidth(2)
            wav.setframerate(int(mimi.sample_rate))
            wav.writeframes(
                (np.clip(pcm, -1, 1) * 32767).astype("<i2").tobytes()
            )

        result = {
            "variant": variant,
            "sample_id": record["sample_id"],
            "question": record["question"],
            "seed": 42,
            "reference_text": reference if variant == "with_reference" else None,
            "injection_basis": "end_of_question_audio_file",
            "injection_step": injection_step if applied else None,
            "reference_frames_applied": applied,
            "tail_silence_s": 20,
            "generated_text": answer,
            "response_wav": str(wav_path),
        }
        results.append(result)
        (out / "results.json").write_text(
            json.dumps(results, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(variant + " 回答：", answer, flush=True)

print("结果目录：", out, flush=True)
print("COMPARISON COMPLETED", flush=True)
