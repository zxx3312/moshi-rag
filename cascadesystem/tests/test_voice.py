"""Local ASR boundaries, microphone lifetime, and optional dependency isolation."""
import asyncio
from array import array
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

from cascadesystem.__main__ import arguments, asr_backend, main, relaunch_voice_environment
from cascadesystem.audio import AudioError
from cascadesystem.conversation import session_command
from cascadesystem.whisper_input import EndpointDetector, FasterWhisperInput


def pcm(amplitude=0, length=100):
    return array('h', [amplitude] * length).tobytes()


def args_for(*options):
    with patch('sys.argv', ['cascadesystem', *options]):
        return arguments()


class EndpointTests(unittest.TestCase):
    def test_initial_silence_has_a_deadline(self):
        detector = EndpointDetector(1000, initial_silence_s=1)
        for _ in range(11):
            result = detector.push(pcm())
            if result:
                break
        self.assertEqual(result, 'no_speech')
        self.assertFalse(detector.frames)

    def test_preroll_is_bounded_and_end_silence_finishes_the_question(self):
        detector = EndpointDetector(1000, end_silence_s=0.3)
        for _ in range(20):
            self.assertIsNone(detector.push(pcm()))
        self.assertIsNone(detector.push(pcm(2000)))
        self.assertLessEqual(len(detector.frames), 4)
        self.assertIsNone(detector.push(pcm()))
        self.assertIsNone(detector.push(pcm(2000)))  # A short pause does not end speech.
        for _ in range(4):
            status = detector.push(pcm())
            if status:
                break
        self.assertEqual(status, 'captured')

    def test_long_utterance_is_explicitly_rejected(self):
        detector = EndpointDetector(1000, max_utterance_s=0.2)
        self.assertIsNone(detector.push(pcm(3000)))
        self.assertEqual(detector.push(pcm(3000)), 'too_long')


class WhisperAdapterTests(unittest.TestCase):
    def model(self, rows=None):
        if rows is None:
            rows = [SimpleNamespace(text=' A fictional tower.', start=0, end=1, avg_logprob=-0.2, no_speech_prob=0.01)]
        return SimpleNamespace(transcribe=Mock(side_effect=lambda *a, **kw: (iter(rows), SimpleNamespace(language='en', language_probability=0.95, duration=1.0))))

    def test_model_is_reused_and_recording_auto_language_stays_local(self):
        model = self.model()
        loader = Mock(return_value=model)
        with tempfile.TemporaryDirectory() as folder, patch.dict(sys.modules, {'faster_whisper': SimpleNamespace(WhisperModel=loader)}):
            root = Path(folder)
            source = root / 'source.wav'
            source.write_bytes(b'fixture handled by a fake model')
            listener = FasterWhisperInput(cache_dir=root / 'models')
            result = listener.listen(root / 'one', source)
            listener.listen(root / 'two', source)
            self.assertEqual(loader.call_count, 1)
            self.assertTrue(loader.call_args.kwargs['local_files_only'])
            self.assertEqual(loader.call_args.kwargs['device'], 'cpu')
            self.assertEqual(result['status'], 'recognized')
            self.assertIsNone(model.transcribe.call_args.kwargs['language'])
            self.assertTrue(model.transcribe.call_args.kwargs['vad_filter'])
            self.assertFalse(model.transcribe.call_args.kwargs['condition_on_previous_text'])
            self.assertEqual(json.loads((root / 'one' / 'recognition.json').read_text())['text'], 'A fictional tower.')

    def test_downloading_requires_explicit_prepare_flag(self):
        loader = Mock(return_value=self.model())
        with tempfile.TemporaryDirectory() as folder, patch.dict(sys.modules, {'faster_whisper': SimpleNamespace(WhisperModel=loader)}):
            listener = FasterWhisperInput(cache_dir=folder)
            listener.prepare(download=True)
            self.assertFalse(loader.call_args.kwargs['local_files_only'])

    def test_low_decoder_score_and_empty_segments_are_not_accepted(self):
        listener = FasterWhisperInput()
        listener._model = self.model([SimpleNamespace(text='Uncertain.', start=0, end=1, avg_logprob=-1.2, no_speech_prob=0.1)])
        self.assertEqual(listener._transcribe(Path('fixture.wav'))['status'], 'low_confidence')
        listener._model = self.model([])
        self.assertEqual(listener._transcribe(Path('fixture.wav'))['status'], 'no_speech')

    def test_microphone_is_closed_before_transcription(self):
        state = {'open': False}
        buffers = iter([pcm(3000), pcm(), pcm(), pcm()])
        class Stream:
            def __enter__(self):
                state['open'] = True
                return self
            def __exit__(self, *args):
                state['open'] = False
            def read(self, frames):
                return next(buffers), False
        sounddevice = SimpleNamespace(query_devices=lambda *a: {'default_samplerate': 1000}, RawInputStream=lambda **kw: Stream())
        listener = FasterWhisperInput(end_silence_s=0.2)
        listener._model = self.model()
        original = listener._transcribe
        def transcribe(path):
            self.assertFalse(state['open'])
            self.assertTrue(path.is_file())
            return original(path)
        listener._transcribe = transcribe
        with tempfile.TemporaryDirectory() as folder, patch.dict(sys.modules, {'sounddevice': sounddevice}):
            result = listener.listen(Path(folder) / 'capture')
        self.assertEqual(result['status'], 'recognized')
        self.assertIsNone(listener._stream)

    def test_rejected_capture_never_reaches_the_model(self):
        listener = FasterWhisperInput()
        listener._model = self.model()
        for status in ['too_long', 'input_overflow', 'no_speech']:
            with self.subTest(status=status), tempfile.TemporaryDirectory() as folder:
                listener._capture = Mock(return_value={'status': status})
                self.assertEqual(listener.listen(Path(folder) / 'attempt')['status'], status)
        listener._model.transcribe.assert_not_called()

    def test_close_aborts_active_stream_and_prevents_reopening(self):
        listener = FasterWhisperInput()
        stream = Mock()
        listener._stream = stream
        listener.close()
        stream.abort.assert_called_once()
        with self.assertRaises(AudioError):
            listener.prepare()

    def test_invalid_capture_parameters_fail_early(self):
        for kwargs in [{'language': 'invalid'}, {'energy_threshold': 0}, {'max_utterance_s': 0}, {'end_silence_s': float('nan')}]:
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                FasterWhisperInput(**kwargs)


class VoiceRoutingTests(unittest.TestCase):
    def test_traditional_chinese_voice_commands_are_understood(self):
        self.assertEqual(session_command('退出對話。'), ('exit', None))
        self.assertEqual(session_command('切換英文。'), ('language', 'en'))
        self.assertEqual(session_command('重新開始。'), ('reset', None))

    def test_explicit_windows_stays_windows(self):
        self.assertEqual(asr_backend(args_for('--listen', '--asr-backend', 'windows')), 'windows')

    def test_text_modes_never_launch_an_optional_environment(self):
        with patch('cascadesystem.__main__.subprocess.Popen') as popen:
            self.assertIsNone(relaunch_voice_environment(args_for('--chat')))
            popen.assert_not_called()

    def test_transcription_only_does_not_load_api_settings(self):
        listener = Mock()
        listener.listen.return_value = {'status': 'recognized', 'text': 'A fictional question?'}
        with patch('cascadesystem.__main__.make_speech_input', return_value=listener), patch('cascadesystem.__main__.Settings.from_env', side_effect=AssertionError('API settings accessed')), contextlib.redirect_stdout(io.StringIO()):
            result = asyncio.run(main(args_for('--transcribe', 'fixture.wav', '--asr-backend', 'faster-whisper')))
        self.assertEqual(result, 0)
        listener.close.assert_called_once()


if __name__ == '__main__':
    unittest.main()
