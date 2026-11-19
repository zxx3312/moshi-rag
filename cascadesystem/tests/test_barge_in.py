"""Concurrent capture, task invalidation, and stale speech must respect interruption."""
import asyncio
from array import array
import contextlib
import io
import json
from pathlib import Path
import tempfile
import threading
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch
import wave

from cascadesystem.__main__ import arguments, run_turn
from cascadesystem.audio import AudioError
from cascadesystem.config import Settings
from cascadesystem.conversation import Conversation, resolve_context, session_command
from cascadesystem.duplex import interruptible_session
from cascadesystem.live_audio import InterruptiblePlayer, LiveMicrophone
from cascadesystem.whisper_input import EndpointDetector
from cascadesystem.llm import TinkerLLM
from dataclasses import replace


def args_for(*extra):
    with patch('sys.argv', ['cascadesystem', '--listen', '--barge-in', '--continuation-seconds', '0', *extra]):
        return arguments()


def fixture_result(question, status='complete'):
    return {'question': question, 'status': status, 'events': [], 'speech_status': 'disabled'}


class EventSource:
    def __init__(self):
        self.events, self.closed = asyncio.Queue(), False
    async def start(self):
        pass
    async def next_event(self):
        return await self.events.get()
    async def finish(self):
        self.closed = True
    async def onset(self, sid):
        await self.events.put({'type': 'speech_started', 'segment_id': sid})
    async def transcript(self, sid, text, status='recognized'):
        await self.events.put({'type': 'transcript', 'segment_id': sid, 'result': {'status': status, 'text': text}})
    async def say(self, sid, text):
        await self.onset(sid)
        await self.transcript(sid, text)


class SessionTests(unittest.IsolatedAsyncioTestCase):
    async def test_correction_cancels_old_task_and_preserves_the_interrupted_request(self):
        source, started, restarted = EventSource(), asyncio.Event(), asyncio.Event()
        calls, states = [], []
        async def runner(args, settings, llm, search, output, question, *, history, turn_state, asr):
            calls.append((question, history))
            states.append(turn_state)
            if len(calls) == 1:
                started.set()
                try:
                    await asyncio.Future()
                except asyncio.CancelledError:
                    turn_state['result'] = {**fixture_result(question, 'interrupted'), 'audible_response': ''}
                    raise
            restarted.set()
            return fixture_result(question)
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            root = Path(folder)
            task = asyncio.create_task(interruptible_session(args_for(), Settings(), object, object, root, runner, event_source=source))
            await source.say(1, 'When did the Silver Tower open?')
            await asyncio.wait_for(started.wait(), 2)
            await source.onset(2)
            await source.transcript(2, 'No, I meant the Golden Tower.')
            await asyncio.wait_for(restarted.wait(), 2)
            await source.say(3, 'goodbye')
            self.assertEqual(await asyncio.wait_for(task, 2), 0)
            self.assertEqual(calls[1][1][-1]['status'], 'interrupted')
            self.assertEqual(calls[1][1][-1]['question'], calls[0][0])
            self.assertFalse(states[0]['accept_output'])
            logs = [json.loads(line) for line in (root / 'session.jsonl').read_text(encoding='utf-8').splitlines()]
            self.assertEqual(sum(r['type'] == 'turn_interrupted' for r in logs), 1)
        self.assertTrue(source.closed)

    async def test_continuation_while_asr_is_pending_is_joined_before_starting(self):
        source, answered = EventSource(), asyncio.Event()
        calls = []
        async def runner(*args, **kwargs):
            calls.append(args[5])
            answered.set()
            return fixture_result(args[5])
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            task = asyncio.create_task(interruptible_session(args_for(), Settings(), object, object, Path(folder), runner, event_source=source))
            await source.onset(1)
            await source.onset(2)  # User resumes before segment 1 finishes transcribing.
            await source.transcript(1, 'Where is the Silver Tower')
            await asyncio.sleep(0.03)
            self.assertFalse(calls)
            await source.transcript(2, 'and when did it open?')
            await asyncio.wait_for(answered.wait(), 2)
            await source.say(3, 'goodbye')
            await asyncio.wait_for(task, 2)
        self.assertEqual(calls, ['Where is the Silver Tower\nand when did it open?'])

    async def test_pause_does_not_start_a_new_api_turn(self):
        source, started, cancelled = EventSource(), asyncio.Event(), asyncio.Event()
        calls = []
        async def runner(*args, **kwargs):
            calls.append(args[5])
            started.set()
            try:
                await asyncio.Future()
            finally:
                cancelled.set()
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            task = asyncio.create_task(interruptible_session(args_for(), Settings(), object, object, Path(folder), runner, event_source=source))
            await source.say(1, 'A fictional question?')
            await asyncio.wait_for(started.wait(), 2)
            await source.say(2, '等一下')
            await asyncio.wait_for(cancelled.wait(), 2)
            await source.say(3, '退出對話')
            await asyncio.wait_for(task, 2)
        self.assertEqual(len(calls), 1)

    async def test_input_failure_closes_capture_and_cancels_the_active_task(self):
        source, started, cancelled = EventSource(), asyncio.Event(), asyncio.Event()
        async def runner(*args, **kwargs):
            started.set()
            try:
                await asyncio.Future()
            finally:
                cancelled.set()
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            task = asyncio.create_task(interruptible_session(args_for(), Settings(), object, object, Path(folder), runner, event_source=source))
            await source.say(1, 'A fictional question?')
            await asyncio.wait_for(started.wait(), 2)
            await source.events.put({'type': 'error', 'error': 'fixture device disconnected'})
            with self.assertRaises(AudioError):
                await asyncio.wait_for(task, 2)
        self.assertTrue(source.closed)
        self.assertTrue(cancelled.is_set())

    async def test_reset_discards_history_and_late_older_transcripts(self):
        source, started, restarted = EventSource(), asyncio.Event(), asyncio.Event()
        histories = []
        async def runner(*args, **kwargs):
            histories.append(kwargs['history'])
            (started if len(histories) == 1 else restarted).set()
            return fixture_result(args[5])
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            task = asyncio.create_task(interruptible_session(args_for(), Settings(), object, object, Path(folder), runner, event_source=source))
            await source.say(1, 'First question?')
            await asyncio.wait_for(started.wait(), 2)
            await source.say(3, '清空上下文')
            await source.transcript(2, 'A late obsolete transcription')
            await source.say(4, 'New question?')
            await asyncio.wait_for(restarted.wait(), 2)
            await source.say(5, 'goodbye')
            await asyncio.wait_for(task, 2)
        self.assertEqual(histories, [[], []])


class CancellationTests(unittest.IsolatedAsyncioTestCase):
    async def test_late_http_reply_after_cancellation_is_never_returned(self):
        entered, release = threading.Event(), threading.Event()
        class HTTP:
            def json(self, *args, **kwargs):
                entered.set()
                release.wait(2)
                return {'choices': [{'message': {'content': '{"stale":true}'}}]}
        client = TinkerLLM(replace(Settings(), api_key='fixture-key'), http=HTTP())
        task = asyncio.create_task(client.complete('fixture', 'fixture', {}))
        try:
            self.assertTrue(await asyncio.to_thread(entered.wait, 2))
            task.cancel()
            with self.assertRaises(asyncio.CancelledError):
                await task
            self.assertEqual(client.calls[0]['status'], 'cancelled')
        finally:
            release.set()
        self.assertTrue(task.cancelled())

    async def test_cancelled_turn_is_saved_without_treating_queued_speech_as_heard(self):
        started = asyncio.Event()
        async def cascade(question, callback, **kwargs):
            await callback({'type': 'utterance', 'sequence': 1, 'language': 'en', 'time_s': 0,
                            'action': 'Final Answer', 'text': 'This was queued but never heard.'})
            started.set()
            await asyncio.Future()
        args = args_for()
        args.play = True  # mode none ensures no actual device is opened in this test.
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            state = {}
            with patch('cascadesystem.__main__.Cascade') as factory:
                factory.return_value.run = cascade
                task = asyncio.create_task(run_turn(args, Settings(), object(), object(), Path(folder), 'A question?', turn_state=state))
                await asyncio.wait_for(started.wait(), 2)
                task.cancel()
                with self.assertRaises(asyncio.CancelledError):
                    await task
            result = json.loads((Path(folder) / 'run.json').read_text(encoding='utf-8'))
            self.assertEqual(result['status'], 'interrupted')
            self.assertEqual(result['audible_response'], '')
            memory = Conversation()
            memory.add(result)
            self.assertEqual(memory.context()[0]['assistant_response'], '')

    async def test_player_abort_unblocks_playback_and_prevents_stale_restart(self):
        entered, stopped = threading.Event(), threading.Event()
        class Stream:
            def start(self):
                pass
            def write(self, data):
                entered.set()
                stopped.wait(2)
            def abort(self):
                stopped.set()
            def stop(self):
                pass
            def close(self):
                pass
        output = Mock(return_value=Stream())
        player = InterruptiblePlayer(0)
        with tempfile.TemporaryDirectory() as folder, patch.dict('sys.modules', {'sounddevice': SimpleNamespace(RawOutputStream=output)}):
            path = Path(folder) / 'test.wav'
            with wave.open(str(path), 'wb') as audio:
                audio.setnchannels(1); audio.setsampwidth(2); audio.setframerate(16000); audio.writeframes(b'\0' * 32000)
            task = asyncio.create_task(asyncio.to_thread(player.play, path, {}, asyncio.get_running_loop(), Mock()))
            self.assertTrue(await asyncio.to_thread(entered.wait, 2))
            player.abort()
            with self.assertRaises(AudioError):
                await asyncio.wait_for(task, 2)
            with self.assertRaises(AudioError):
                player.play(path, {}, asyncio.get_running_loop(), Mock())
        self.assertEqual(output.call_count, 1)


class ContinuousInputTests(unittest.IsolatedAsyncioTestCase):
    async def test_capture_continues_while_previous_audio_is_being_transcribed(self):
        release, listening, stop = threading.Event(), threading.Event(), threading.Event()
        buffers = iter([array('h', [3000] * 100).tobytes()] * 2 + [b'\0' * 200] * 3
                       + [array('h', [3000] * 100).tobytes()] * 2 + [b'\0' * 200] * 3)
        class Stream:
            def __enter__(self):
                return self
            def __exit__(self, *args):
                pass
            def read(self, frames):
                try:
                    return next(buffers), False
                except StopIteration:
                    stop.wait(3)
                    raise RuntimeError('fixture stream stopped')
            def abort(self):
                stop.set()
        class Recognizer:
            device, end_silence_s, max_utterance_s, threshold = None, 0.2, 30, 0.015
            def prepare(self):
                pass
            def listen(self, directory, path):
                listening.set()
                release.wait(3)
                return {'status': 'recognized', 'text': path.stem}
            def close(self):
                release.set()
        sd = SimpleNamespace(query_devices=lambda *a: {'default_samplerate': 1000}, RawInputStream=lambda **kw: Stream())
        with tempfile.TemporaryDirectory() as folder, patch.dict('sys.modules', {'sounddevice': sd}):
            source = LiveMicrophone(Recognizer(), Path(folder) / 'input', onset_s=0.18)
            try:
                await source.start()
                onsets = []
                while len(onsets) < 2:
                    event = await asyncio.wait_for(source.next_event(), 2)
                    if event['type'] == 'speech_started':
                        onsets.append(event['segment_id'])
                self.assertFalse(release.is_set())
                self.assertEqual(onsets, [1, 2])
                release.set()
                texts = []
                while len(texts) < 2:
                    event = await asyncio.wait_for(source.next_event(), 2)
                    if event['type'] == 'transcript':
                        texts.append(event['result']['text'])
                self.assertEqual(texts, ['segment-0001', 'segment-0002'])
            finally:
                await source.finish()


class CommandAndOnsetTests(unittest.TestCase):
    def test_brief_noise_does_not_trigger_an_onset(self):
        detector = EndpointDetector(1000, onset_s=0.18)
        detector.push(array('h', [3000] * 100).tobytes())
        detector.push(b'\0' * 200)
        self.assertFalse(detector.started)
        detector.push(array('h', [3000] * 100).tobytes())
        detector.push(array('h', [3000] * 100).tobytes())
        self.assertTrue(detector.started)

    def test_pause_is_a_whole_utterance_command(self):
        self.assertEqual(session_command('等一下！'), ('pause', None))
        self.assertEqual(session_command('Stop.'), ('pause', None))
        self.assertIsNone(session_command('Why did the engine stop?'))


class InterruptedContextTests(unittest.IsolatedAsyncioTestCase):
    async def test_latest_interrupted_request_is_explicitly_supplied_for_merging(self):
        payloads = []
        class Resolver:
            async def complete(self, purpose, system, payload):
                payloads.append(payload)
                return {'needs_clarification': False, 'standalone_question': 'Where is Amber Tower and when did it open?', 'used_turn_ids': [1]}
        history = [{'turn_id': 1, 'question': 'Where is it?', 'resolved_question': 'Where is Amber Tower?', 'status': 'interrupted'}]
        await resolve_context(Resolver(), 'And when did it open?', 'en', history)
        self.assertEqual(payloads[0]['interrupted_request']['question'], 'Where is Amber Tower?')

    async def test_old_interruption_is_not_merged_after_a_completed_topic_change(self):
        payloads = []
        class Resolver:
            async def complete(self, purpose, system, payload):
                payloads.append(payload)
                return {'needs_clarification': False, 'standalone_question': 'When did Copper Tower open?', 'used_turn_ids': [2]}
        history = [{'turn_id': 1, 'question': 'Where is Amber Tower?', 'status': 'interrupted'},
                   {'turn_id': 2, 'question': 'Where is Copper Tower?', 'status': 'complete'}]
        await resolve_context(Resolver(), 'When did it open?', 'en', history)
        self.assertIsNone(payloads[0]['interrupted_request'])


if __name__ == '__main__':
    unittest.main()
