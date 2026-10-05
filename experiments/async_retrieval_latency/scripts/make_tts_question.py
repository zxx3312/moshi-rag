#!/usr/bin/env python
"""Synthesize a spoken question WAV with Piper (local CPU TTS) for smoke tests.

Run with a Python that has ``piper-tts`` installed (kept separate from the experiment env):

    TTS_PY -m piper.download_voices en_US-lessac-medium --data-dir VOICE_DIR
    TTS_PY experiments/async_retrieval_latency/scripts/make_tts_question.py \
        --voice VOICE_DIR/en_US-lessac-medium.onnx \
        --text "What is the name of the tallest waterfall in the world?" \
        --out experiments/async_retrieval_latency/configs/audio/tallest_waterfall.wav

Output: mono 16-bit 24 kHz (Mimi's rate), with leading and trailing silence.
Synthetic speech is a limitation: note the voice used for each sample.
"""

from __future__ import annotations

import argparse
import io
import sys
import wave
from pathlib import Path

import numpy as np

TARGET_SR = 24000


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--voice", type=Path, required=True, help="Piper .onnx voice (its .onnx.json next to it).")
    p.add_argument("--text", type=str, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--lead-silence", type=float, default=0.5)
    p.add_argument("--tail-silence", type=float, default=1.0)
    args = p.parse_args()

    from piper import PiperVoice

    if args.out.exists():
        print(f"refusing to overwrite {args.out}", file=sys.stderr)
        return 1
    voice = PiperVoice.load(str(args.voice))
    buf = io.BytesIO()
    with wave.open(buf, "wb") as wf:
        voice.synthesize_wav(args.text, wf)
    buf.seek(0)
    with wave.open(buf, "rb") as wf:
        sr = wf.getframerate()
        assert wf.getsampwidth() == 2 and wf.getnchannels() == 1
        x = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0

    # Linear-interpolation resample to 24 kHz (sufficient for a speech smoke test).
    n_out = int(round(len(x) * TARGET_SR / sr))
    y = np.interp(np.linspace(0, len(x) - 1, n_out), np.arange(len(x)), x).astype(np.float32)
    y = np.concatenate([np.zeros(int(args.lead_silence * TARGET_SR), np.float32), y,
                        np.zeros(int(args.tail_silence * TARGET_SR), np.float32)])

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(args.out), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(TARGET_SR)
        wf.writeframes((np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes())
    print(f"wrote {args.out}: {len(y) / TARGET_SR:.2f} s at {TARGET_SR} Hz (source {sr} Hz, voice {args.voice.name})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
