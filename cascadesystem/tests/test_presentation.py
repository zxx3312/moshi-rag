import asyncio
from dataclasses import replace
from pathlib import Path
import tempfile
import time
import unittest

from cascadesystem.audio import SpeechOutput
from cascadesystem.config import Settings
from cascadesystem.controller import Cascade
from cascadesystem.presentation import detect_language, finish_sentence, ready_line, sentence_events, split_sentences


class PresentationTests(unittest.TestCase):
    def test_chinese_sentences_and_quotes(self):
        self.assertEqual(split_sentences('他说：“确认了！”日期是2044年。'), ['他说：“确认了！”', '日期是2044年。'])

    def test_english_abbreviations_and_decimals(self):
        self.assertEqual(split_sentences('Dr. Aster measured 3.14 units in U.S. labs. It worked!'),
                         ['Dr. Aster measured 3.14 units in U.S. labs.', 'It worked!'])

    def test_language_detection_and_override(self):
        self.assertEqual(detect_language('埃菲尔铁塔在哪个城市？'), 'zh')
        self.assertEqual(detect_language('Where is the Eiffel Tower?'), 'en')
        self.assertEqual(detect_language('Where is 北京?'), 'en')
        self.assertEqual(detect_language('Eiffel Tower 在哪？'), 'zh')
        self.assertEqual(detect_language('Where is it?', 'zh'), 'zh')

    def test_ready_time_is_explicitly_labelled(self):
        event = {'sequence': 1, 'language': 'zh', 'action': 'Final Answer', 'time_s': 2.5, 'text': '第一句。第二句。'}
        sentences = sentence_events(event)
        self.assertEqual(len(sentences), 2)
        self.assertIn('文本就绪 2.50秒', ready_line(sentences[0]))
        self.assertEqual(sentences[1]['sentence_index'], 2)
        self.assertEqual(finish_sentence('Paris', 'en'), 'Paris.')


class LocalSearch:
    async def search(self, query):
        return [{'title': 'Silver observatory', 'url': 'https://example.invalid/observatory',
                 'text': 'The silver observatory opened in 2044.'}]


class BilingualLLM:
    def __init__(self, wrong_language=False):
        self.languages = []
        self.wrong_language = wrong_language

    async def complete(self, purpose, system, payload):
        language = payload['output_language']
        self.languages.append(language)
        if purpose == 'decompose':
            return {'units': [{'unit_id': 'u1', 'description': '天文台开放年份' if language == 'zh' else 'The observatory opening year',
                               'necessary': True, 'depends_on': [], 'queries': ['silver observatory opening']}]}
        if purpose == 'judge':
            return {'judgments': [{'unit_id': 'u1', 'label': 'SUPPORTED', 'value': '2044', 'citations': ['e1'],
                                   'quotes': [{'evidence_id': 'e1', 'text': 'opened in 2044'}]}]}
        if purpose == 'generate':
            return {'text': 'The observatory opened in 2044.' if self.wrong_language or language == 'en' else '天文台于2044年开放。'}
        if purpose == 'verify':
            return {'approved': True}
        raise AssertionError('Unexpected stage')


class BilingualTests(unittest.IsolatedAsyncioTestCase):
    async def test_chinese_question_english_source_chinese_answer(self):
        llm = BilingualLLM()
        result = await Cascade(llm, LocalSearch(), Settings()).run('银色天文台是哪一年开放的？')
        self.assertEqual(result['response_language'], 'zh')
        self.assertEqual(set(llm.languages), {'zh'})
        final = next(e for e in result['events'] if e.get('action') == 'Final Answer')
        self.assertEqual(final['text'], '天文台于2044年开放。')

    async def test_english_question_english_answer(self):
        result = await Cascade(BilingualLLM(), LocalSearch(), Settings()).run('When did the silver observatory open?')
        self.assertEqual(result['response_language'], 'en')
        final = next(e for e in result['events'] if e.get('action') == 'Final Answer')
        self.assertEqual(final['text'], 'The observatory opened in 2044.')

    async def test_wrong_language_generation_uses_localized_fallback(self):
        result = await Cascade(BilingualLLM(wrong_language=True), LocalSearch(), Settings()).run('银色天文台是哪一年开放的？')
        final = next(e for e in result['events'] if e.get('action') == 'Final Answer')
        self.assertTrue(final['fallback'])
        self.assertEqual(final['text'], '天文台开放年份：2044。')


class SpeechQueueTests(unittest.IsolatedAsyncioTestCase):
    async def test_sentence_audio_is_sequential_with_real_queue_delay(self):
        notifications = []
        origin = time.monotonic() - 1
        with tempfile.TemporaryDirectory() as folder:
            voice = Path(folder) / 'fake.onnx'
            voice.write_bytes(b'fixture')
            speech = SpeechOutput(folder, mode='piper', voice=str(voice), started_at=origin, on_event=notifications.append)
            speech.play = True

            def synthesize(event):
                time.sleep(0.01)
                return Path(folder) / f"{event['sentence_index']}.wav", 0.05, 'fixture voice'

            def play(path, event, loop):
                start = time.monotonic()
                loop.call_soon_threadsafe(speech._notify, event, 'playback_started', start)
                time.sleep(0.05)
                end = time.monotonic()
                return {'played': True, 'playback_started_s': start - origin, 'playback_finished_s': end - origin}

            speech._synthesize, speech._play_audio = synthesize, play
            worker = asyncio.create_task(speech.worker())
            await speech.submit({'sequence': 7, 'time_s': 0.0, 'action': 'Final Answer', 'language': 'en', 'text': 'First sentence. Second sentence.'})
            await speech.finish(worker)
            self.assertEqual(len(speech.records), 2)
            self.assertGreater(speech.records[0]['playback_started_s'], 1)
            self.assertGreaterEqual(speech.records[1]['playback_started_s'], speech.records[0]['playback_finished_s'])
            starts = [n for n in notifications if n['type'] == 'playback_started']
            self.assertEqual([n['sentence_index'] for n in starts], [1, 2])
            self.assertEqual([r['language'] for r in speech.records], ['en', 'en'])

    async def test_synthesis_only_never_claims_playback(self):
        with tempfile.TemporaryDirectory() as folder:
            voice = Path(folder) / 'fake.onnx'
            voice.write_bytes(b'fixture')
            speech = SpeechOutput(folder, mode='piper', voice=str(voice))
            speech._synthesize = lambda event: (Path(folder) / 'fake.wav', 1.0, 'fixture voice')
            worker = asyncio.create_task(speech.worker())
            await speech.submit({'sequence': 1, 'action': 'Final Answer', 'text': 'Confirmed.', 'language': 'en'})
            await speech.finish(worker)
            self.assertFalse(speech.records[0]['played'])
            self.assertIsNone(speech.records[0]['playback_started_s'])


if __name__ == '__main__':
    unittest.main()
