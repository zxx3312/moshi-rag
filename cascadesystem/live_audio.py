"""Continuous capture and cancellable playback using the optional voice environment.

No acoustic echo cancellation: use a headset with the barge-in mode.
"""
import asyncio
import queue
from pathlib import Path
import threading
import time
import wave

from .audio import AudioError
from .whisper_input import EndpointDetector


class InterruptiblePlayer:
    def __init__(self, started_at, device=None):
        self.started_at, self.device = started_at, device
        self.cancelled = threading.Event()
        self._lock, self._stream = threading.Lock(), None

    def abort(self):
        self.cancelled.set()
        with self._lock:
            if self._stream is not None:
                try:
                    self._stream.abort()
                except Exception:
                    pass

    def play(self, path, event, loop, notify):
        import sounddevice as sd
        stream = None
        try:
            with wave.open(str(path), 'rb') as audio:
                dtype = {1: 'uint8', 2: 'int16', 3: 'int24', 4: 'int32'}.get(audio.getsampwidth())
                if dtype is None:
                    raise AudioError("Unsupported playback WAV format")
                with self._lock:
                    if self.cancelled.is_set():
                        raise AudioError("Speech output cancelled")
                    stream = sd.RawOutputStream(samplerate=audio.getframerate(), channels=audio.getnchannels(),
                                                dtype=dtype, device=self.device)
                    self._stream = stream
                    stream.start()
                started = time.monotonic()
                loop.call_soon_threadsafe(notify, event, 'playback_started', started)
                while not self.cancelled.is_set():
                    data = audio.readframes(max(1, audio.getframerate() // 50))
                    if not data:
                        break
                    stream.write(data)
                if self.cancelled.is_set():
                    raise AudioError("Speech output cancelled")
                stream.stop()  # Drain buffered audio before declaring this sentence finished.
                if self.cancelled.is_set():
                    raise AudioError("Speech output cancelled")
                ended = time.monotonic()
                loop.call_soon_threadsafe(notify, event, 'playback_finished', ended)
                return {'played': True, 'playback_started_s': started - self.started_at,
                        'playback_finished_s': ended - self.started_at}
        except AudioError:
            raise
        except Exception as exc:
            raise AudioError(f"Audio playback failed ({type(exc).__name__})") from None
        finally:
            with self._lock:
                if stream is not None:
                    try:
                        stream.close()
                    except Exception:
                        pass
                self._stream = None


class LiveMicrophone:
    """Capture never waits for Whisper or a network request. One ASR worker preserves order."""
    def __init__(self, recognizer, directory, *, onset_s=0.18):
        self.recognizer, self.directory, self.onset_s = recognizer, Path(directory), onset_s
        self.events = asyncio.Queue(maxsize=128)
        self._audio = queue.Queue(maxsize=4)
        self._stop = threading.Event()
        self._lock, self._stream = threading.Lock(), None
        self._threads, self._loop = [], None

    def _publish(self, event):
        event.setdefault('time_monotonic', time.monotonic())
        def deliver():
            if self._stop.is_set():
                return
            try:
                self.events.put_nowait(event)
            except asyncio.QueueFull:
                self._stop.set()
                while not self.events.empty():
                    self.events.get_nowait()
                self.events.put_nowait({'type': 'error', 'error': 'Live input event backlog exceeded its limit'})
        if self._loop is not None and not self._loop.is_closed():
            self._loop.call_soon_threadsafe(deliver)

    async def start(self):
        await asyncio.to_thread(self.recognizer.prepare)
        self.directory.mkdir(parents=True, exist_ok=False)
        self._loop = asyncio.get_running_loop()
        for target in (self._transcribe_loop, self._capture_loop):
            thread = threading.Thread(target=target, daemon=True)
            self._threads.append(thread)
            thread.start()

    async def next_event(self):
        return await self.events.get()

    def _capture_loop(self):
        try:
            import sounddevice as sd
            rate = int(sd.query_devices(self.recognizer.device, 'input')['default_samplerate'])
            def detector():
                return EndpointDetector(rate, initial_silence_s=float('inf'), end_silence_s=self.recognizer.end_silence_s,
                                        max_utterance_s=self.recognizer.max_utterance_s,
                                        threshold=self.recognizer.threshold, onset_s=self.onset_s)
            endpoint, segment_id, overflowed, suppress, quiet = detector(), 0, False, False, 0.0
            with sd.RawInputStream(samplerate=rate, blocksize=max(1, rate // 50), device=self.recognizer.device,
                                   channels=1, dtype='int16') as stream:
                with self._lock:
                    self._stream = stream
                self._publish({'type': 'ready', 'sample_rate': rate})
                while not self._stop.is_set():
                    data, overflow = stream.read(max(1, rate // 50))
                    data = bytes(data)
                    before = endpoint.started
                    status = endpoint.push(data)
                    if suppress:
                        # Do not treat the tail of a rejected long utterance as a new question.
                        quiet = quiet + len(data) / 2 / rate if endpoint.candidate_s == 0 else 0
                        if quiet >= self.recognizer.end_silence_s:
                            endpoint, suppress, quiet = detector(), False, 0.0
                        continue
                    overflowed |= bool(overflow)
                    if endpoint.started and not before:
                        segment_id += 1
                        self._publish({'type': 'speech_started', 'segment_id': segment_id})
                    if status not in {'captured', 'too_long'}:
                        continue
                    path = self.directory / f'segment-{segment_id:04d}.wav'
                    with wave.open(str(path), 'wb') as output:
                        output.setnchannels(1)
                        output.setsampwidth(2)
                        output.setframerate(rate)
                        output.writeframes(b''.join(endpoint.frames))
                    rejection = 'too_long' if status == 'too_long' else 'input_overflow' if overflowed else None
                    if rejection is not None:
                        self._publish({'type': 'transcript', 'segment_id': segment_id,
                                       'result': {'status': rejection, 'text': '', 'input_audio': str(path)}})
                    else:
                        try:
                            self._audio.put_nowait((segment_id, path))
                        except queue.Full:
                            self._publish({'type': 'transcript', 'segment_id': segment_id,
                                           'result': {'status': 'input_backlog', 'text': '', 'input_audio': str(path)}})
                    suppress = status == 'too_long'
                    endpoint, overflowed = detector(), False
        except Exception as exc:
            if not self._stop.is_set():
                self._publish({'type': 'error', 'error': f'Microphone capture failed ({type(exc).__name__}); check input device and microphone access'})
        finally:
            with self._lock:
                self._stream = None

    def _transcribe_loop(self):
        while not self._stop.is_set():
            try:
                segment_id, path = self._audio.get(timeout=0.1)
            except queue.Empty:
                continue
            try:
                if not self._stop.is_set():
                    result = self.recognizer.listen(self.directory / f'asr-{segment_id:04d}', path)
                    self._publish({'type': 'transcript', 'segment_id': segment_id, 'result': result})
            except Exception as exc:
                self._publish({'type': 'error', 'error': f'Speech transcription failed ({type(exc).__name__})'})
            finally:
                self._audio.task_done()

    def close(self):
        self._stop.set()
        with self._lock:
            if self._stream is not None:
                try:
                    self._stream.abort()
                except Exception:
                    pass
        self.recognizer.close()

    async def finish(self):
        self.close()
        for thread in self._threads:
            await asyncio.to_thread(thread.join, 3)
