"""Transcribe the question audio with Whisper: the ASR end of the cascade.

    VLLM_PY a_work/run_asr.py --audio DIR --out ASR.jsonl

DIR is what make_question_audio.py wrote (WAVs and index.jsonl). Needs torch and transformers, and the model
in the Hugging Face cache. Each row has the transcript and the time from the end of the question to the
transcript, which run_replay.py --asr charges to the clock. Whisper is not streaming, so that time is one
pass over the whole question; measure it on the GPU the cascade would run on, not on a login node.
"""
import argparse
import json
import re
import statistics
import time
import wave
from pathlib import Path

WHISPER_RATE = 16000


def read_wav(path) -> tuple:
    """(samples as floats in [-1, 1], sample rate) of a mono 16-bit WAV."""
    import numpy as np
    with wave.open(str(path), "rb") as f:
        if f.getsampwidth() != 2 or f.getnchannels() != 1:
            raise ValueError(f"{path}: expected mono 16-bit audio")
        return np.frombuffer(f.readframes(f.getnframes()), dtype="<i2").astype("float32") / 32768.0, f.getframerate()


def words(text: str) -> list:
    return re.sub(r"[^a-z0-9' ]", " ", text.lower()).split()


def word_error_rate(reference: str, heard: str) -> float:
    """Word edits needed to turn the transcript into the reference, per reference word."""
    ref, hyp = words(reference), words(heard)
    row = list(range(len(hyp) + 1))
    for i, r in enumerate(ref, 1):
        previous, row[0] = row[0], i
        for j, h in enumerate(hyp, 1):
            previous, row[j] = row[j], min(row[j] + 1, row[j - 1] + 1, previous + (r != h))
    return row[-1] / max(len(ref), 1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--audio", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--model", default="openai/whisper-large-v3-turbo")
    ap.add_argument("--device", default=None, help="cuda or cpu; default cuda when there is one.")
    args = ap.parse_args()

    import torch
    import torchaudio
    from transformers import WhisperForConditionalGeneration, WhisperProcessor

    device = args.device or ("cuda" if torch.cuda.is_available() else "cpu")
    dtype = torch.float16 if device == "cuda" else torch.float32
    processor = WhisperProcessor.from_pretrained(args.model)
    model = WhisperForConditionalGeneration.from_pretrained(args.model, torch_dtype=dtype).to(device).eval()
    language = {} if args.model.endswith(".en") else {"language": "en", "task": "transcribe"}

    def transcribe(samples, rate):
        t0 = time.monotonic()
        audio = torchaudio.functional.resample(torch.from_numpy(samples.copy()), rate, WHISPER_RATE).numpy()
        features = processor(audio, sampling_rate=WHISPER_RATE, return_tensors="pt").input_features.to(device, dtype)
        with torch.no_grad():
            ids = model.generate(features, **language)
        text = processor.batch_decode(ids, skip_special_tokens=True)[0].strip()
        return text, time.monotonic() - t0

    index = [json.loads(line) for line in open(args.audio / "index.jsonl", encoding="utf-8")]
    transcribe(*read_wav(args.audio / index[0]["file"]))  # warm-up: the first call pays for start-up
    rows = []
    for item in index:
        samples, rate = read_wav(args.audio / item["file"])
        text, latency = transcribe(samples, rate)
        rows.append({"sample_id": item["sample_id"], "text": text, "latency_s": round(latency, 3),
                     "reference": item["question"], "wer": round(word_error_rate(item["question"], text), 3),
                     "audio_duration_s": item["duration_s"], "model": args.model, "device": device})
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    wrong = [r for r in rows if r["wer"] > 0]
    print(f"{len(rows)} questions on {device}: latency median {statistics.median(r['latency_s'] for r in rows):.2f} s, "
          f"mean WER {statistics.mean(r['wer'] for r in rows):.3f}, {len(wrong)} with errors")
    for r in wrong:
        print(f"  {r['wer']:.2f}  heard: {r['text']}\n        asked: {r['reference']}")


if __name__ == "__main__":
    main()
