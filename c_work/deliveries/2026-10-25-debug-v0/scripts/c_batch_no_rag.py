import json
import os
import runpy
import time
import wave
from pathlib import Path

import numpy as np
import torch
from moshi.models import LMGen
from moshi.conditioners.base import ConditionAttributes

root = Path.home() / "projects/moshi-rag"
data = root / "c_work/debug-v0"

records = [
    json.loads(line)
    for line in (data / "questions_only.jsonl").read_text(
        encoding="utf-8"
    ).splitlines()
    if line.strip()
]
assert len(records) == 20
assert len({r["sample_id"] for r in records}) == 20
for record in records:
    assert (data / "audio" / (record["sample_id"] + ".wav")).is_file()

job = os.environ.get("SLURM_JOB_ID", str(time.time_ns()))
run_dir = data / "runs" / ("no-rag-batch-" + job)
run_dir.mkdir(parents=True, exist_ok=False)
print("批量结果目录：", run_dir, flush=True)
loaded = runpy.run_path(str(root / "scripts/c_smoke_load.py"))
model = loaded["model"]
mimi = loaded["mimi"]
tokenizer = loaded["checkpoint"].get_text_tokenizer()


for index, record in enumerate(records, 1):
    print(f"[{index}/20] {record['sample_id']}", flush=True)
    output = run_dir / record["sample_id"]
    output.mkdir(exist_ok=False)
    source = data / "audio" / (record["sample_id"] + ".wav")

    with wave.open(str(source), "rb") as wav:
        assert wav.getframerate() == 24000
        assert wav.getnchannels() == 1 and wav.getsampwidth() == 2
        audio = np.frombuffer(
            wav.readframes(wav.getnframes()), dtype="<i2"
        ).astype(np.float32) / 32768.0

    # 复用此前已经通过的本地模型加载测试。
    with torch.inference_mode():
        torch.manual_seed(42)
        conditions = None
        if model.condition_provider is not None:
            attributes = [ConditionAttributes(
                text={"first_speaker": "SPEAKER_OTHER"}
            )]
            prepared = model.condition_provider.prepare(attributes)
            conditions = model.condition_provider(prepared)

        generator = LMGen(
            model, condition_tensors=conditions, profile=True
        )
        frame_size = int(mimi.sample_rate / mimi.frame_rate)

        # 播完问题后继续输入 15 秒静音，给模型回答时间。
        audio = np.concatenate([audio, np.zeros(15 * 24000, np.float32)])
        audio = np.pad(audio, (0, (-len(audio)) % frame_size))
        frames = torch.from_numpy(audio).to("cuda").reshape(1, 1, -1)

        chunks = []
        text_ids = []
        print("开始生成回答……", flush=True)
        with mimi.streaming(1), generator.streaming(1):
            for index, frame in enumerate(frames.split(frame_size, dim=-1)):
                codes = mimi.encode(frame)
                tokens = generator.step(codes)
                if tokens is not None:
                    pcm = mimi.decode(tokens[:, 1:, :])
                    chunks.append(pcm[0, 0].float().cpu())
                    token = int(tokens[0, 0, 0])
                    if token not in (0, 3):
                        text_ids.append(token)
                if index % 50 == 0:
                    print(f"已处理 {index} 帧", flush=True)

        assert chunks, "模型没有生成音频"
        response = torch.cat(chunks).numpy()
        text = tokenizer.decode(text_ids)

    with wave.open(str(output / "response.wav"), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(24000)
        wav.writeframes(
            (np.clip(response, -1, 1) * 32767).astype("<i2").tobytes()
        )

    result = {
        "sample_id": record["sample_id"],
        "question": record["question"],
        "variant": "reference_conditioner_removed_smoke_test",
        "retrieval_enabled": False,
        "seed": 42,
        "tail_silence_s": 15,
        "generated_text": text,
    }
    (output / "result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("模型生成文字：", text, flush=True)
    print("结果目录：", output, flush=True)
    print("QUESTION COMPLETED", flush=True)

    with (run_dir / "results.jsonl").open("a", encoding="utf-8") as file:
        file.write(json.dumps(result, ensure_ascii=False) + "\n")

print("BATCH GENERATION COMPLETED: 20/20", flush=True)
