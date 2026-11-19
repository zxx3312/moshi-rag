"""Optional local multilingual ASR; imports stay isolated from the stdlib core."""
from array import array
from collections import deque
import importlib.metadata
import json
import math
from pathlib import Path
import sys
import threading
import time
import wave

from .audio import AudioError


VOICE_ENV = Path(__file__).parent / ".venv"
MODEL_CACHE = Path(__file__).parent / "artifacts" / "models"


def voice_python():
    return VOICE_ENV / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")


class EndpointDetector:
    """Bound one utterance using RMS onset/end silence and a small pre-roll."""
    def __init__(self, rate, *, initial_silence_s=10, end_silence_s=1, max_utterance_s=30, threshold=0.015, onset_s=0):
        self.rate, self.threshold = rate, threshold
        self.wait_limit, self.end_limit, self.max_limit = initial_silence_s, end_silence_s, max_utterance_s
        self.waited = self.elapsed = self.quiet = 0.0
        self.started = False
        self.frames = []
        self.preroll = deque()
        self.preroll_s = 0.0
        self.onset_s, self.candidate_s = onset_s, 0.0

    def push(self, pcm):
        samples = array('h', pcm)
        duration = len(samples) / self.rate
        if not samples:
            raise AudioError("Microphone returned an empty audio buffer")
        rms = math.sqrt(sum(int(s) ** 2 for s in samples) / len(samples)) / 32768
        active = rms >= self.threshold
        self.candidate_s = self.candidate_s + duration if active else 0.0
        if not self.started:
            self.waited += duration
            self.preroll.append(pcm)
            self.preroll_s += duration
            while self.preroll_s > max(0.3, self.onset_s + 0.1) + duration:
                self.preroll_s -= len(self.preroll.popleft()) / 2 / self.rate
            if not active or self.candidate_s + 1e-9 < self.onset_s:
                return 'no_speech' if self.waited >= self.wait_limit else None
            self.started = True
            self.frames.extend(self.preroll)
            self.preroll.clear()
        else:
            self.frames.append(pcm)
        self.elapsed += duration
        self.quiet = 0.0 if active else self.quiet + duration
        if self.quiet >= self.end_limit:
            return 'captured'
        if self.elapsed >= self.max_limit:
            return 'too_long'
        return None


class FasterWhisperInput:
    def __init__(self, language=None, initial_silence_s=10, end_silence_s=1, *, model="small",
                 device=None, energy_threshold=0.015, max_utterance_s=30, cache_dir=MODEL_CACHE):
        aliases = {None: 'auto', 'auto': 'auto', 'zh': 'zh', 'chinese': 'zh', 'en': 'en', 'english': 'en'}
        normalized = language.lower() if isinstance(language, str) else language
        if normalized not in aliases:
            raise ValueError("ASR language must be auto, zh, or en")
        self.language = aliases[normalized]
        for value, lower, upper, label in [(initial_silence_s, 1, 60, 'initial silence'),
                                            (end_silence_s, 0.2, 5, 'end silence'),
                                            (max_utterance_s, 2, 120, 'maximum utterance'),
                                            (energy_threshold, 0.0001, 1, 'energy threshold')]:
            if not math.isfinite(value) or not lower <= value <= upper:
                raise ValueError(f"Invalid {label}: expected {lower}..{upper}")
        self.initial_silence_s, self.end_silence_s = initial_silence_s, end_silence_s
        self.max_utterance_s, self.threshold = max_utterance_s, energy_threshold
        self.device = int(device) if isinstance(device, str) and device.isdecimal() else device
        self.model_name, self.cache_dir = model, Path(cache_dir).resolve()
        self._model = None
        self._closed = threading.Event()
        self._lock, self._stream = threading.Lock(), None

    def prepare(self, *, download=False):
        if self._closed.is_set():
            raise AudioError("Speech input has been closed")
        if self._model is None:
            try:
                from faster_whisper import WhisperModel
                self.cache_dir.mkdir(parents=True, exist_ok=True)
                self._model = WhisperModel(self.model_name, device='cpu', compute_type='int8',
                                          cpu_threads=4, download_root=str(self.cache_dir),
                                          local_files_only=not download)
            except ImportError:
                raise AudioError("Install cascadesystem/requirements-voice.txt in cascadesystem/.venv first") from None
            except (OSError, RuntimeError, ValueError) as exc:
                raise AudioError(f"ASR model could not load ({type(exc).__name__}); run --prepare-asr to download it") from None
        return {'backend': 'faster-whisper', 'model': self.model_name, 'device': 'cpu',
                'compute_type': 'int8', 'cache_dir': str(self.cache_dir)}

    def info(self):
        try:
            import sounddevice as sd
            all_devices = sd.query_devices()
            devices = [{'id': i, 'name': d['name'], 'channels': d['max_input_channels'],
                        'sample_rate': d['default_samplerate']}
                       for i, d in enumerate(all_devices) if d['max_input_channels'] > 0]
            return {'backend': 'faster-whisper', 'model': self.model_name, 'input_devices': devices,
                    'default_input_device': int(sd.default.device[0]),
                    'output_devices': [{'id': i, 'name': d['name'], 'channels': d['max_output_channels'],
                                        'sample_rate': d['default_samplerate']}
                                       for i, d in enumerate(all_devices) if d['max_output_channels'] > 0],
                    'default_output_device': int(sd.default.device[1]),
                    'versions': {p: importlib.metadata.version(p) for p in ['faster-whisper', 'sounddevice', 'ctranslate2']}}
        except ImportError:
            raise AudioError("Voice dependencies are missing; install requirements-voice.txt in cascadesystem/.venv") from None
        except Exception as exc:
            raise AudioError(f"Could not enumerate microphone devices ({type(exc).__name__})") from None

    def close(self):
        self._closed.set()
        with self._lock:
            stream = self._stream
        if stream is not None:
            try:
                stream.abort()
            except Exception:
                pass

    def _capture(self, destination):
        import sounddevice as sd
        if self._closed.is_set():
            raise AudioError("Speech input has been closed")
        try:
            device = sd.query_devices(self.device, 'input')
            rate = int(device['default_samplerate'])
            detector = EndpointDetector(rate, initial_silence_s=self.initial_silence_s,
                                        end_silence_s=self.end_silence_s,
                                        max_utterance_s=self.max_utterance_s, threshold=self.threshold)
            overflowed = False
            with sd.RawInputStream(samplerate=rate, blocksize=max(1, rate // 50), device=self.device,
                                   channels=1, dtype='int16') as stream:
                with self._lock:
                    self._stream = stream
                while not self._closed.is_set():
                    data, overflow = stream.read(max(1, rate // 50))
                    overflowed |= overflow
                    status = detector.push(bytes(data))
                    if status:
                        break
                else:
                    raise AudioError("Speech input cancelled")
            if detector.frames:
                with wave.open(str(destination), 'wb') as output:
                    output.setnchannels(1)
                    output.setsampwidth(2)
                    output.setframerate(rate)
                    output.writeframes(b''.join(detector.frames))
            # Never send a truncated utterance or audio with dropped input frames to the LLM.
            if overflowed:
                status = 'input_overflow'
            return {'status': status, 'audio_duration_s': sum(map(len, detector.frames)) / 2 / rate,
                    'input_overflow': bool(overflowed), 'sample_rate': rate}
        except AudioError:
            raise
        except Exception as exc:
            raise AudioError(f"Microphone capture failed ({type(exc).__name__}); check --input-device and Windows microphone access") from None
        finally:
            with self._lock:
                self._stream = None

    def _transcribe(self, path):
        segments, info = self._model.transcribe(str(path), language=None if self.language == 'auto' else self.language,
                                                beam_size=5, vad_filter=True, condition_on_previous_text=False)
        rows = [{'text': s.text.strip(), 'start_s': s.start, 'end_s': s.end,
                 'avg_logprob': s.avg_logprob, 'no_speech_prob': s.no_speech_prob} for s in segments]
        text = ' '.join(s['text'] for s in rows).strip()
        status = 'recognized' if text else 'no_speech'
        # These are decoder scores, not calibrated recognition probabilities or Windows confidence.
        if rows and sum(s['avg_logprob'] for s in rows) / len(rows) < -1.0:
            status = 'low_confidence'
        return {'status': status, 'text': text, 'language': info.language,
                'language_probability': info.language_probability, 'segments': rows,
                'audio_duration_s': info.duration}

    def listen(self, directory, input_wave=None):
        self.prepare()
        directory = Path(directory).resolve()
        directory.mkdir(parents=True, exist_ok=False)
        started = time.monotonic()
        path = Path(input_wave).resolve() if input_wave is not None else directory / 'question.wav'
        if input_wave is not None and not path.is_file():
            raise AudioError("Recognition input file does not exist")
        capture = {'status': 'captured'} if input_wave is not None else self._capture(path)
        capture_s = time.monotonic() - started
        transcription_start = time.monotonic()
        if capture['status'] == 'captured':
            if self._closed.is_set():
                raise AudioError("Speech input cancelled")
            try:
                result = self._transcribe(path)
            except Exception as exc:
                raise AudioError(f"Audio transcription failed ({type(exc).__name__})") from None
        else:
            result = {**capture, 'text': ''}
        result.update(backend='faster-whisper', model=self.model_name, input_audio=str(path) if path.exists() else None,
                      capture_s=capture_s, transcription_s=time.monotonic() - transcription_start,
                      latency_s=time.monotonic() - started)
        (directory / 'recognition.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
        return result
