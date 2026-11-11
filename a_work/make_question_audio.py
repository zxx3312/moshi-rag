"""Speak each question with Piper, as input for the ASR end of the cascade.

    TTS_PY a_work/make_question_audio.py --trace TRACE.jsonl --voice VOICE.onnx --out DIR

TTS_PY is a Python with piper-tts (kept apart from the vLLM environment). Writes DIR/SAMPLE_ID.wav, mono
16-bit at the voice's rate with no padding, and DIR/index.jsonl. Synthetic questions are easier for an
ASR than recorded ones; C's question audio should replace them once it is shared.
"""
import argparse
import sys
import wave
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from turntaking.cascade import PiperTTS  # noqa: E402
from turntaking.replay import load_jsonl, write_jsonl  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--trace", type=Path, required=True)
    ap.add_argument("--voice", type=Path, required=True, help="Piper .onnx voice with its .onnx.json next to it.")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    questions = {t["sample_id"]: t["question"] for t in load_jsonl(args.trace)}  # one per question, not per trace
    tts = PiperTTS(args.voice)
    args.out.mkdir(parents=True, exist_ok=True)
    index = []
    for sample_id, question in questions.items():
        speech = tts.synthesize(question)
        with wave.open(str(args.out / f"{sample_id}.wav"), "wb") as f:
            f.setnchannels(1)
            f.setsampwidth(2)
            f.setframerate(speech.sample_rate)
            f.writeframes(speech.audio)
        index.append({"sample_id": sample_id, "question": question, "file": f"{sample_id}.wav",
                      "duration_s": round(speech.duration_s, 3), "voice": args.voice.name})
    write_jsonl(args.out / "index.jsonl", index)
    print(f"{len(index)} questions, {sum(r['duration_s'] for r in index):.1f} s of audio in {args.out}")


if __name__ == "__main__":
    main()
