"""Multi-turn state is bounded and never substituted for retrieval evidence."""
import asyncio
import contextlib
from dataclasses import replace
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from cascadesystem.__main__ import arguments, conversation_loop, run_turn
from cascadesystem.audio import AudioError, SpeechOutput
from cascadesystem.config import Settings
from cascadesystem.controller import Cascade
from cascadesystem.conversation import ClarificationNeeded, Conversation, resolve_context, session_command
from cascadesystem.speech_input import WindowsSpeechInput


class MemoryTests(unittest.TestCase):
    def result(self, question, reply):
        return {'question': question, 'status': 'complete', 'events': [
            {'type': 'utterance', 'action': 'Backchannel', 'text': 'Do not remember this filler.'},
            {'type': 'utterance', 'action': 'Final Answer', 'text': reply}]}

    def test_history_is_bounded_and_feedback_is_excluded(self):
        memory = Conversation(max_turns=2)
        for i in range(3):
            memory.add(self.result(str(i), 'An unverified old answer.'))
        self.assertEqual([t['turn_id'] for t in memory.context()], [2, 3])
        self.assertNotIn('filler', json.dumps(memory.context()))
        self.assertIn('not current evidence', memory.context()[0]['trust'])

    def test_reset_and_context_copy(self):
        memory = Conversation()
        memory.add(self.result('A question', 'A reply'))
        copy = memory.context()
        copy[0]['question'] = 'modified'
        self.assertEqual(memory.context()[0]['question'], 'A question')
        memory.reset()
        self.assertFalse(memory.context())

    def test_commands_require_whole_utterance(self):
        self.assertEqual(session_command('退出对话。'), ('exit', None))
        self.assertEqual(session_command('/language en'), ('language', 'en'))
        self.assertEqual(session_command('switch to Chinese'), ('language', 'zh'))
        self.assertIsNone(session_command('How do I exit a game?'))


class HistoryLLM:
    def __init__(self, clarify=False):
        self.calls, self.requests = [], []
        self.clarify = clarify

    async def complete(self, purpose, system, payload):
        self.calls.append({'purpose': purpose, 'status': 'fixture', 'latency_s': 0})
        self.requests.append((purpose, payload))
        chinese = payload.get('output_language') == 'zh'
        if purpose == 'context':
            return {'standalone_question': '银塔什么时候开放？' if chinese else 'When did the Silver Tower open?',
                    'needs_clarification': self.clarify, 'clarification': 'Which tower?',
                    'used_turn_ids': [payload['conversation_history'][-1]['turn_id']]}
        if purpose == 'decompose':
            return {'units': [{'unit_id': 'u1', 'description': '银塔开放年份' if chinese else 'Silver Tower opening year',
                               'necessary': True, 'depends_on': [], 'queries': ['Silver Tower opening']}]}
        if purpose == 'judge':
            return {'judgments': [{'unit_id': 'u1', 'label': 'SUPPORTED', 'value': '2044', 'citations': ['e1'],
                                   'quotes': [{'evidence_id': 'e1', 'text': 'It opened in 2044.'}]}]}
        if purpose == 'generate':
            return {'text': '银塔于2044年开放。' if chinese else 'The Silver Tower opened in 2044.'}
        if purpose == 'verify':
            return {'approved': True, 'facts_valid': True}
        raise AssertionError(purpose)


class FreshSearch:
    async def search(self, query):
        return [{'title': 'Silver Tower', 'url': 'https://example.invalid/tower', 'text': 'It opened in 2044.'}]


def history():
    return [{'turn_id': 1, 'question': 'What is the Silver Tower?', 'resolved_question': 'What is the Silver Tower?',
             'assistant_response': 'An earlier unverified claim mentioning a SECRET_OLD_VALUE.', 'status': 'complete'}]


class ResolutionTests(unittest.IsolatedAsyncioTestCase):
    async def test_followup_is_resolved_and_then_independently_searched(self):
        llm = HistoryLLM()
        result = await Cascade(llm, FreshSearch(), Settings()).run('When did it open?', history=history())
        self.assertEqual(result['question'], 'When did it open?')
        self.assertEqual(result['resolved_question'], 'When did the Silver Tower open?')
        self.assertEqual(result['used_history_turn_ids'], [1])
        self.assertEqual(result['status'], 'complete')
        for purpose, payload in llm.requests:
            if purpose != 'context':
                self.assertNotIn('SECRET_OLD_VALUE', json.dumps(payload))
        self.assertEqual(result['evidence'][0]['evidence_id'], 'e1')

    async def test_history_does_not_supply_missing_evidence(self):
        class EmptySearch:
            async def search(self, query):
                return []
        result = await Cascade(HistoryLLM(), EmptySearch(), Settings()).run('When did it open?', history=history())
        self.assertEqual(result['status'], 'incomplete')
        self.assertFalse(result['output_enqueued_units'])

    async def test_ambiguous_reference_requests_clarification_without_search(self):
        result = await Cascade(HistoryLLM(clarify=True), FreshSearch(), Settings()).run('When did it open?', history=history())
        self.assertEqual(result['status'], 'needs_clarification')
        self.assertFalse(result['searches'])
        self.assertTrue(any(e.get('clarification') for e in result['events']))

    async def test_unknown_history_id_is_rejected(self):
        class WrongID:
            async def complete(self, *args):
                return {'needs_clarification': False, 'standalone_question': 'A question?', 'used_turn_ids': [99]}
        with self.assertRaises(ValueError):
            await resolve_context(WrongID(), 'What about it?', 'en', history())

    async def test_api_records_are_per_turn_when_client_is_reused(self):
        llm, cascade = HistoryLLM(), None
        cascade = Cascade(llm, FreshSearch(), Settings())
        first = await cascade.run('When did the Silver Tower open?')
        second = await cascade.run('When did it open?', history=history())
        self.assertEqual(len(first['llm_calls']), 4)
        self.assertEqual(len(second['llm_calls']), 5)


def session_args(mode):
    with patch('sys.argv', ['cascadesystem', mode]):
        return arguments()


class LoopTests(unittest.IsolatedAsyncioTestCase):
    async def test_cancellation_while_finishing_output_aborts_the_worker(self):
        class InterruptedSpeech(SpeechOutput):
            async def finish(self, worker):
                raise asyncio.CancelledError()

        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            speech = InterruptedSpeech(Path(folder) / 'audio')
            with patch('cascadesystem.__main__.SpeechOutput', return_value=speech):
                with self.assertRaises(asyncio.CancelledError):
                    await run_turn(session_args('--chat'), Settings(), HistoryLLM(), FreshSearch(),
                                   Path(folder), 'When did the Silver Tower open?')
            self.assertTrue(speech._aborted)
            self.assertTrue(speech.queue.empty())

    async def test_text_session_runs_two_turns_and_resets_history(self):
        values = iter(['What is the Silver Tower?', 'When did it open?', '/reset', 'A new question?', '/exit'])
        llm = HistoryLLM()
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            await conversation_loop(session_args('--chat'), Settings(), llm, FreshSearch, Path(folder), read_text=lambda: next(values))
            rows = [json.loads(line) for line in (Path(folder) / 'session.jsonl').read_text(encoding='utf-8').splitlines()]
            self.assertEqual(sum(r['type'] == 'turn_finished' for r in rows), 3)
            saved = json.loads((Path(folder) / 'history.json').read_text(encoding='utf-8'))
            self.assertEqual(len(saved), 1)
            self.assertEqual(saved[0]['question'], 'A new question?')
        self.assertEqual(sum(p == 'context' for p, _ in llm.requests), 1)

    async def test_voice_loop_ignores_unclear_audio_and_handles_language_commands(self):
        class Input:
            language, closed = 'zh', False
            def __init__(self):
                self.rows = iter([{'status': 'no_speech'}, {'status': 'low_confidence', 'text': 'bad input'},
                                  {'status': 'recognized', 'text': '银塔是什么？'},
                                  {'status': 'recognized', 'text': '切换英文'},
                                  {'status': 'recognized', 'text': 'When did it open?'},
                                  {'status': 'recognized', 'text': 'goodbye'}])
            def info(self):
                return {'recognizers': [{'language': 'zh-CN'}, {'language': 'en-US'}]}
            def listen(self, directory):
                return next(self.rows)
            def close(self):
                self.closed = True

        microphone, llm = Input(), HistoryLLM()
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            await conversation_loop(session_args('--listen'), Settings(), llm, FreshSearch, Path(folder), speech_input=microphone)
            self.assertTrue((Path(folder) / 'turn-0002' / 'run.json').is_file())
            self.assertFalse((Path(folder) / 'turn-0003').exists())
        self.assertTrue(microphone.closed)
        self.assertEqual(microphone.language, 'en')
        self.assertEqual(sum(p == 'decompose' for p, _ in llm.requests), 2)


class NativeInputTests(unittest.TestCase):
    def test_low_confidence_audio_is_marked_for_repetition(self):
        listener = WindowsSpeechInput('zh', min_confidence=0.3)
        listener._execute = lambda args: {'status': 'recognized', 'text': 'low confidence words', 'confidence': 0.1}
        with tempfile.TemporaryDirectory() as folder:
            result = listener.listen(Path(folder) / 'input')
            self.assertEqual(result['status'], 'low_confidence')
            self.assertTrue((Path(folder) / 'input' / 'recognition.json').exists())

    def test_invalid_confidence_is_rejected(self):
        listener = WindowsSpeechInput('en')
        listener._execute = lambda args: {'status': 'recognized', 'text': 'words', 'confidence': float('nan')}
        with tempfile.TemporaryDirectory() as folder, self.assertRaises(AudioError):
            listener.listen(Path(folder) / 'input')

    def test_invalid_listener_parameters_are_rejected(self):
        for kwargs in [{'language': 'xx'}, {'initial_silence_s': 0}, {'end_silence_s': 0}, {'min_confidence': 2}]:
            with self.assertRaises(ValueError):
                WindowsSpeechInput(**kwargs)


if __name__ == '__main__':
    unittest.main()
