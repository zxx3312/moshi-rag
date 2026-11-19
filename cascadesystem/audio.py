"""Optional existing Whisper/Piper executables, plus Windows system TTS.

No SDKs are imported or installed. Commands use argument arrays, never a shell.
"""
import asyncio
import json
import os
from pathlib import Path
import subprocess
import threading
import time
import wave

from .presentation import detect_language, sentence_events


class AudioError(RuntimeError):
    pass


def _run(args, *, text=None, timeout=180):
    try:
        options = {"creationflags": subprocess.CREATE_NO_WINDOW} if os.name == "nt" else {}
        result = subprocess.run(args, input=text, text=True, encoding="utf-8", errors="replace", capture_output=True,
                                timeout=timeout, check=False, **options)
    except (OSError, subprocess.TimeoutExpired):
        raise AudioError("Speech command failed to start or timed out") from None
    if result.returncode:
        if result.returncode == 12:
            raise AudioError("No enabled Windows voice for the answer language; install its speech voice in Windows settings")
        raise AudioError(f"Speech command exited with code {result.returncode}")
    return result.stdout.strip()


def transcribe(audio_path, output_dir, executable="whisper", model="turbo", language=None):
    audio_path, output_dir = Path(audio_path).resolve(), Path(output_dir).resolve()
    if not audio_path.is_file():
        raise AudioError("Input audio file does not exist")
    output_dir.mkdir(parents=True, exist_ok=False)
    args = [executable, str(audio_path), "--model", model, "--output_dir", str(output_dir), "--output_format", "json"]
    if language:
        args += ["--language", language]
    begin = time.monotonic()
    _run(args, timeout=600)
    try:
        text = json.loads((output_dir / (audio_path.stem + ".json")).read_text(encoding="utf-8"))["text"]
        if not isinstance(text, str) or not text.strip():
            raise ValueError()
    except (OSError, ValueError, KeyError, TypeError):
        raise AudioError("Whisper did not produce a nonempty transcript") from None
    return {"text": text.strip(), "latency_s": time.monotonic() - begin,
            "input_audio": str(audio_path), "model": model}


class SpeechOutput:
    def __init__(self, directory, *, mode="none", piper="piper", voice=None, play=False, started_at=None, on_event=None, player=None):
        if mode not in {"none", "windows", "piper"}:
            raise ValueError("Unknown TTS mode")
        if mode == "windows" and os.name != "nt":
            raise AudioError("Windows TTS is available only on Windows")
        if mode == "piper" and (not voice or not Path(voice).is_file()):
            raise AudioError("--voice must point to an existing Piper ONNX voice")
        if play and os.name != "nt":
            raise AudioError("Built-in playback is Windows-only; use saved WAV files on this platform")
        self.directory, self.mode = Path(directory), mode
        self.piper, self.voice, self.play = piper, voice, play
        self.started_at = time.monotonic() if started_at is None else started_at
        self.on_event = on_event
        self.records = []
        self.queue = asyncio.Queue()
        self._aborted = False
        self.player = player
        self._process_lock, self._synth_process = threading.Lock(), None
        self.active_record = None

    def _run_tts(self, args, *, text=None):
        """Allow an interrupted turn to kill its own synthesizer, without a shell."""
        options = {"creationflags": subprocess.CREATE_NO_WINDOW} if os.name == "nt" else {}
        process = None
        try:
            with self._process_lock:
                if self._aborted:
                    raise AudioError("Speech output cancelled")
                process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                           text=True, encoding='utf-8', errors='replace', **options)
                self._synth_process = process
            stdout, _ = process.communicate(input=text, timeout=180)
            if self._aborted:
                raise AudioError("Speech output cancelled")
            if process.returncode == 12:
                raise AudioError("No enabled Windows voice for the answer language; install its speech voice in Windows settings")
            if process.returncode:
                raise AudioError(f"Speech command exited with code {process.returncode}")
            return stdout.strip()
        except subprocess.TimeoutExpired:
            process.kill()
            process.communicate()
            raise AudioError("Speech command timed out") from None
        except OSError:
            raise AudioError("Speech command failed to start") from None
        finally:
            with self._process_lock:
                if self._synth_process is process:
                    self._synth_process = None

    async def submit(self, event):
        if self.mode != "none":
            for sentence in sentence_events(event):
                sentence.setdefault("language", detect_language(sentence["text"]))
                await self.queue.put(sentence)

    def _notify(self, event, kind, at=None, **data):
        if self._aborted:
            return
        if self.active_record is not None and self.active_record['event_sequence'] == event['sequence'] and self.active_record['sentence_index'] == event['sentence_index']:
            elapsed = (time.monotonic() if at is None else at) - self.started_at
            if kind == 'playback_started':
                self.active_record['playback_started_s'] = elapsed
            elif kind == 'playback_finished':
                self.active_record['playback_finished_s'] = elapsed
        if not self._aborted and self.on_event is not None:
            self.on_event({"type": kind, "time_s": round((time.monotonic() if at is None else at) - self.started_at, 6),
                           "event_sequence": event["sequence"], "sentence_index": event["sentence_index"],
                           "sentence_count": event["sentence_count"], "language": event["language"],
                           "text": event["text"], **data})

    async def worker(self):
        loop = asyncio.get_running_loop()
        while True:
            event = await self.queue.get()
            try:
                if event is None:
                    return
                record = {"event_sequence": event["sequence"], "sentence_index": event["sentence_index"],
                          "sentence_count": event["sentence_count"], "language": event["language"],
                          "text": event["text"], "action": event["action"], "status": "error",
                          "played": False, "playback_started_s": None, "playback_finished_s": None}
                self.active_record = record
                begin = time.monotonic()
                record["synthesis_started_s"] = begin - self.started_at
                try:
                    path, duration, voice_name = await asyncio.to_thread(self._synthesize, event)
                    record.update(status="ok", path=str(path), duration_s=duration, voice=voice_name,
                                  synthesis_finished_s=time.monotonic() - self.started_at)
                    self._notify(event, "audio_ready", path=str(path), duration_s=duration, voice=voice_name)
                    if self.play:
                        if self.player is not None:
                            playback = await asyncio.to_thread(self.player.play, path, event, loop, self._notify)
                        else:
                            playback = await asyncio.to_thread(self._play_audio, path, event, loop)
                        record.update(**playback)
                except AudioError as exc:
                    record["status"] = "error"
                    record["error"] = str(exc)
                    self._notify(event, "audio_error", error=str(exc))
                record["synthesis_and_playback_s"] = time.monotonic() - begin
                self.records.append(record)
                self.active_record = None
            finally:
                self.queue.task_done()

    def _synthesize(self, event):
        self.directory.mkdir(parents=True, exist_ok=True)
        path = (self.directory / f"{event['sequence']:04d}_{event['sentence_index']:02d}.wav").resolve()
        text = event["text"]
        if self.mode == "piper":
            self._run_tts([self.piper, "--model", str(Path(self.voice).resolve()), "--output_file", str(path)], text=text)
            voice_name = Path(self.voice).name
        else:
            # Only file paths are sent in arguments. Text is read from a UTF-8 file, never interpolated into code.
            text_path = path.with_suffix(".txt")
            text_path.write_text(text, encoding="utf-8")
            script = Path(__file__).with_name("windows_tts.ps1")
            voice_name = self._run_tts(["powershell.exe", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
                               "-File", str(script), "-TextPath", str(text_path), "-WavePath", str(path),
                               "-Language", event["language"]])
        try:
            with wave.open(str(path), "rb") as audio:
                duration = audio.getnframes() / audio.getframerate()
                if duration <= 0:
                    raise AudioError("TTS produced an empty WAV file")
        except (OSError, wave.Error):
            raise AudioError("TTS output is not a readable WAV file") from None
        return path, duration, voice_name

    def _play_audio(self, path, event, loop):
        import winsound
        if self._aborted:
            raise AudioError("Speech output cancelled")
        start = time.monotonic()
        loop.call_soon_threadsafe(self._notify, event, "playback_started", start)
        try:
            winsound.PlaySound(str(path), winsound.SND_FILENAME)
        except RuntimeError:
            raise AudioError("WAV playback failed") from None
        end = time.monotonic()
        loop.call_soon_threadsafe(self._notify, event, "playback_finished", end)
        return {"played": True, "playback_started_monotonic": start, "playback_finished_monotonic": end,
                "playback_started_s": start - self.started_at, "playback_finished_s": end - self.started_at}

    async def finish(self, worker):
        await self.queue.join()
        await self.queue.put(None)
        await worker

    async def abort(self, worker):
        self._aborted = True
        with self._process_lock:
            process = self._synth_process
            if process is not None and process.poll() is None:
                try:
                    process.kill()
                except OSError:
                    pass
        if self.player is not None:
            self.player.abort()
        elif self.play and os.name == "nt":
            import winsound
            try:
                winsound.PlaySound(None, 0)
            except RuntimeError:
                pass
        worker.cancel()
        await asyncio.gather(worker, return_exceptions=True)
        if self.active_record is not None:
            self.active_record.update(status='interrupted', played=False)
            self.records.append(self.active_record)
            self.active_record = None
        while not self.queue.empty():
            self.queue.get_nowait()
            self.queue.task_done()
