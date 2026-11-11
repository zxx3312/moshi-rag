"""The speech ends of the cascade: ASR -> controller -> LLM -> TTS.

The controller and the LLM are the replay's policy and generator. This module adds what the user said
(Heard) and what the agent's words sound like (Speech), so the replay clock can charge the time the speech
components take and use the real length of each utterance.

RateTTS and the question text stand in when no speech models are loaded; they reproduce the text-only replay.
"""
from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Callable, Dict, Optional


@dataclass(frozen=True)
class Heard:
    """What the ASR made of the question, and how long after the question ended it was ready."""
    text: str
    latency_s: float = 0.0


@dataclass(frozen=True)
class Speech:
    duration_s: float
    latency_s: float  # from text to first audio
    time_at: Callable[[int], float]  # seconds into the audio at which the character at this offset is spoken
    audio: Optional[bytes] = None  # mono 16-bit PCM
    sample_rate: Optional[int] = None


class RateTTS:
    """No audio: every word takes the same time. Dates and numbers come out too short, since "1969" is one
    word here and four when spoken."""
    name = "rate"

    def __init__(self, words_per_s: float = 2.5, min_s: float = 1.0):
        self.words_per_s, self.min_s = words_per_s, min_s

    def synthesize(self, text: str) -> Speech:
        duration = max(self.min_s, len(text.split()) / self.words_per_s)
        return Speech(duration, 0.0, lambda i: duration * i / max(len(text), 1))


class PiperTTS:
    """Piper on the CPU. An utterance lasts as long as its audio, and its latency is the time to the first
    sentence's audio: later sentences are synthesised while the first one plays.

    This voice gives no alignment, so the time of a character is estimated from the phonemes before it.
    A repeated text is synthesised once and reports the first call's latency again, like the generator.
    """
    name = "piper"

    def __init__(self, voice_path):
        from piper import PiperVoice  # only in the TTS environment
        self.voice = PiperVoice.load(str(voice_path))
        self.spoken: Dict[str, Speech] = {}

    def _phonemes(self, text: str) -> int:
        return sum(len(sentence) for sentence in self.voice.phonemize(text)) if text.strip() else 0

    def synthesize(self, text: str) -> Speech:
        if text not in self.spoken:
            t0, first, pcm = time.monotonic(), None, []
            for chunk in self.voice.synthesize(text):
                first = first if first is not None else time.monotonic() - t0
                pcm.append(chunk.audio_int16_bytes)
            audio, rate = b"".join(pcm), self.voice.config.sample_rate
            duration, total = len(audio) / 2 / rate, self._phonemes(text)

            def time_at(i: int) -> float:
                return duration * min(1.0, self._phonemes(text[:i]) / total) if total else 0.0

            self.spoken[text] = Speech(duration, first or 0.0, time_at, audio, rate)
        return self.spoken[text]


def load_tts(spec: Optional[str]):
    """"rate" or None for the stand-in, "piper:VOICE.onnx" for Piper."""
    if not spec or spec == "rate":
        return RateTTS()
    kind, _, arg = spec.partition(":")
    if kind == "piper" and arg:
        return PiperTTS(arg)
    raise ValueError(f"unknown TTS {spec!r}: use rate or piper:VOICE.onnx")
