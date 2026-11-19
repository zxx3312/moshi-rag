"""Windows dictation from the default microphone or a WAV file, without Python dependencies."""
import json
import math
import os
from pathlib import Path
import subprocess
import threading
import time

from .audio import AudioError


class WindowsSpeechInput:
    def __init__(self, language="auto", initial_silence_s=10.0, end_silence_s=1.0, min_confidence=0.3):
        aliases = {None: "auto", "auto": "auto", "zh": "zh", "chinese": "zh", "en": "en", "english": "en"}
        language = language.lower() if isinstance(language, str) else language
        if language not in aliases:
            raise ValueError("Windows ASR language must be auto, zh, or en")
        self.language = aliases[language]
        if not math.isfinite(initial_silence_s) or not 1 <= initial_silence_s <= 60:
            raise ValueError("Initial silence must be 1..60 seconds")
        if not math.isfinite(end_silence_s) or not 0.2 <= end_silence_s <= 5:
            raise ValueError("End silence must be 0.2..5 seconds")
        if not math.isfinite(min_confidence) or not 0 <= min_confidence <= 1:
            raise ValueError("ASR confidence must be 0..1")
        self.initial_silence_s, self.end_silence_s = initial_silence_s, end_silence_s
        self.min_confidence = min_confidence
        self._process, self._closed = None, False
        self._lock = threading.Lock()

    def close(self):
        with self._lock:
            self._closed = True
            process = self._process
        if process is not None and process.poll() is None:
            try:
                process.kill()
            except OSError:
                pass

    def _execute(self, arguments):
        if os.name != "nt":
            raise AudioError("Native microphone recognition requires Windows")
        script = Path(__file__).with_name("windows_asr.ps1")
        command = ["powershell.exe", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass", "-File", str(script), *arguments]
        process = None
        try:
            with self._lock:
                if self._closed:
                    raise AudioError("Speech input has been closed")
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                           text=True, encoding="utf-8", errors="replace", creationflags=subprocess.CREATE_NO_WINDOW)
                self._process = process
            stdout, _ = process.communicate(timeout=self.initial_silence_s + 55)
        except (KeyboardInterrupt, subprocess.TimeoutExpired):
            if process is not None:
                process.kill()
                process.communicate()
            raise
        except OSError:
            raise AudioError("Could not start Windows speech recognition") from None
        finally:
            with self._lock:
                if self._process is process:
                    self._process = None
        if process.returncode:
            message = {13: "No Windows recognizer for this language; install the Windows speech language pack",
                       14: "Microphone unavailable; check your default input device and Windows microphone privacy settings"}
            raise AudioError(message.get(process.returncode, f"Windows recognition exited with code {process.returncode}"))
        try:
            raw = json.loads(stdout.lstrip("\ufeff"))
        except ValueError:
            raise AudioError("Windows recognizer returned invalid JSON") from None
        if not isinstance(raw, dict):
            raise AudioError("Windows recognizer returned an invalid result")
        return raw

    def info(self):
        return self._execute(["-InfoOnly"])

    def listen(self, directory, input_wave=None):
        directory = Path(directory).resolve()
        directory.mkdir(parents=True, exist_ok=False)
        arguments = ["-Language", self.language, "-InitialSilenceSeconds", str(self.initial_silence_s),
                     "-EndSilenceSeconds", str(self.end_silence_s), "-WavePath", str(directory / "question.wav")]
        if input_wave is not None:
            input_wave = Path(input_wave).resolve()
            if not input_wave.is_file():
                raise AudioError("Recognition input WAV does not exist")
            arguments += ["-InputWave", str(input_wave)]
        begin = time.monotonic()
        try:
            result = self._execute(arguments)
        except subprocess.TimeoutExpired:
            result = {"status": "timeout", "text": "", "confidence": 0.0}
        result["latency_s"] = time.monotonic() - begin
        result["backend"] = "windows"
        if result.get("status") not in {"recognized", "no_speech", "timeout"}:
            raise AudioError("Windows recognizer returned an unknown status")
        if result.get("status") == "recognized":
            text, confidence = result.get("text"), result.get("confidence")
            if not isinstance(text, str) or not text.strip() or type(confidence) not in {int, float} or not math.isfinite(confidence) or not 0 <= confidence <= 1:
                raise AudioError("Windows recognizer produced invalid text/confidence")
            result["text"] = text.strip()
            if confidence < self.min_confidence:
                result["status"] = "low_confidence"
        (directory / "recognition.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        return result
