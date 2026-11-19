"""Fictional offline WAV/queue tests; never invoke Windows speech or an LLM API."""
import asyncio
from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
import time
import unittest
import wave

EVAL_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EVAL_ROOT))
sys.path.insert(0, str(EVAL_ROOT.parent))

from cascadesystem.audio import AudioError, SpeechOutput
from cascadesystem.config import Settings
from eval_audio import merge_waves
from eval_common import digest, write_json, write_jsonl
from eval_replay import run_b_debug, run_trace
from eval_score import score_b_run
from test_debug20 import FixtureLLM, WatchingLLM, prepared, trace


def wav(path, *, rate=8000, frames=160):
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), 'wb') as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(rate)
        output.writeframes(b'\x01\0' * frames)


class FakeSpeech(SpeechOutput):
    def __init__(self, directory, *, mode, play, **kwargs):
        super().__init__(directory, mode='none', play=False, **kwargs)
        self.mode, self.play = mode, play

    def _synthesize(self, event):
        path = (self.directory / f"{event['sequence']}_{event['sentence_index']}.wav").resolve()
        wav(path)
        return path, .02, 'Fictional test voice'

    def _play_audio(self, path, event, loop):
        start = time.monotonic()
        loop.call_soon_threadsafe(self._notify, event, 'playback_started', start)
        time.sleep(.02)
        end = time.monotonic()
        loop.call_soon_threadsafe(self._notify, event, 'playback_finished', end)
        return {'played': True, 'playback_started_s': start - self.started_at,
                'playback_finished_s': end - self.started_at}


class WaveTests(unittest.TestCase):
    def test_combined_wave_keeps_silence_and_sentence_order(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            wav(root / 'a.wav'); wav(root / 'b.wav')
            records = [{'path': str(root / 'a.wav'), 'synthesis_finished_s': .02, 'playback_started_s': None,
                        'event_sequence': 1, 'sentence_index': 1, 'action': 'Partial Answer', 'text': 'First.'},
                       {'path': str(root / 'b.wav'), 'synthesis_finished_s': .07, 'playback_started_s': None,
                        'event_sequence': 2, 'sentence_index': 1, 'action': 'Final Answer', 'text': 'Second.'}]
            result = merge_waves(records, root / 'response.wav')
            self.assertAlmostEqual(result['duration_s'], .09)
            with wave.open(str(root / 'response.wav'), 'rb') as audio:
                data = audio.readframes(audio.getnframes())
            self.assertEqual(data[:160 * 2], b'\0' * (160 * 2))
            self.assertEqual(data[160 * 2:320 * 2], b'\x01\0' * 160)
            self.assertEqual([r['text'] for r in result['timeline']], ['First.', 'Second.'])

    def test_missing_segment_does_not_create_a_complete_response_wave(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'response.wav'
            with self.assertRaises(AudioError):
                merge_waves([{'status': 'error'}], path)
            self.assertFalse(path.exists())


class AudioReplayTests(unittest.IsolatedAsyncioTestCase):
    async def test_speech_is_synthesized_before_pipeline_finishes(self):
        with tempfile.TemporaryDirectory() as folder:
            result = await run_trace(trace(), Settings(), Path(folder) / 'sample', 3,
                                     lambda _: WatchingLLM(), tts='windows', speech_factory=FakeSpeech)
            self.assertEqual(result['audio']['status'], 'ok')
            self.assertTrue(Path(result['audio']['wave']['path']).is_file())
            partial = next(e for e in result['events'] if e.get('type') == 'utterance' and e.get('action') == 'Partial Answer')
            audio_record = next(r for r in result['audio']['records'] if r['event_sequence'] == partial['sequence'])
            self.assertLess(audio_record['synthesis_finished_s'], result['evaluation']['text_pipeline_wall_s'])
            self.assertTrue(result['evaluation']['audio_enabled'])
            self.assertEqual(result['evaluation']['timing_kind'], 'unknown')

    async def test_playback_drains_before_trace_returns_and_has_actual_start_records(self):
        with tempfile.TemporaryDirectory() as folder:
            result = await run_trace(trace(), Settings(), Path(folder) / 'sample', 3,
                                     lambda _: FixtureLLM(), tts='windows', play=True, speech_factory=FakeSpeech)
            self.assertTrue(all(r['played'] for r in result['audio']['records']))
            self.assertTrue(all(r['playback_started_s'] is not None for r in result['audio']['records']))
            self.assertGreaterEqual(result['evaluation']['total_wall_s'], result['evaluation']['text_pipeline_wall_s'])

    async def test_audio_run_keeps_b_claim_timing_unknown(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            prepared(root / 'input')
            await run_b_debug(root / 'input', root / 'run', settings=Settings(), llm_factory=lambda _: FixtureLLM(),
                              tts='windows', play=True, speech_factory=FakeSpeech)
            summary = score_b_run(root / 'input', root / 'run', root / 'b_eval')
            self.assertEqual(summary['status_counts'], {'ok': 1})
            self.assertEqual(summary['groups'][0]['timing_kind'], 'unknown')
            self.assertIsNone(summary['groups'][0]['ttfr_s']['median'])
            logs = [json.loads(line) for line in (root / 'run/policy_log.jsonl').read_text().splitlines()]
            self.assertTrue(all(row['audio_enabled'] for row in logs))
            self.assertTrue(all(row['output_start_time_s'] is None for row in logs))

    async def test_speech_failure_stops_remaining_questions_and_is_not_hidden(self):
        class FailedSpeech(FakeSpeech):
            def _synthesize(self, event):
                raise AudioError('fictional missing voice')
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            prepared(root / 'input')
            second = deepcopy(trace())
            second['sample_id'], second['trace_id'] = 'fictional_other', 'fictional_other_short'
            write_jsonl(root / 'input/traces.jsonl', [trace(), second])
            meta = json.loads((root / 'input/manifest.json').read_text())
            meta['files_sha256']['traces.jsonl'] = digest(root / 'input/traces.jsonl')
            write_json(root / 'input/manifest.json', meta)
            await run_b_debug(root / 'input', root / 'run', settings=Settings(), llm_factory=lambda _: FixtureLLM(),
                              tts='windows', speech_factory=FailedSpeech)
            summary = json.loads((root / 'run/audio_summary.json').read_text())
            self.assertEqual(summary['failed_runs'], 1)
            self.assertFalse((root / 'run/samples/0002').exists())

    async def test_cancellation_stops_audio_and_saves_identified_partial_result(self):
        class Slow(FixtureLLM):
            async def complete(self, *args):
                await asyncio.sleep(5)
                return await super().complete(*args)
        with tempfile.TemporaryDirectory() as folder:
            sample = Path(folder) / 'sample'
            task = asyncio.create_task(run_trace(trace(), Settings(), sample, 10, lambda _: Slow(),
                                                  tts='windows', speech_factory=FakeSpeech))
            await asyncio.sleep(.03)
            task.cancel()
            with self.assertRaises(asyncio.CancelledError):
                await task
            saved = json.loads((sample / 'run.json').read_text())
            self.assertEqual(saved['status'], 'cancelled')
            self.assertEqual(saved['evaluation']['trace_id'], trace()['trace_id'])
            self.assertEqual(saved['audio']['status'], 'cancelled')

    async def test_limit_counts_questions_and_keeps_their_requested_conditions(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            prepared(root / 'input')
            traces = []
            for sid in ['fictional_ship', 'fictional_other']:
                for condition in ['immediate', 'short', 'long']:
                    record = deepcopy(trace())
                    record['sample_id'], record['trace_id'] = sid, sid + '_' + condition
                    traces.append(record)
            write_jsonl(root / 'input/traces.jsonl', traces)
            meta = json.loads((root / 'input/manifest.json').read_text())
            meta['files_sha256']['traces.jsonl'] = digest(root / 'input/traces.jsonl')
            write_json(root / 'input/manifest.json', meta)
            await run_b_debug(root / 'input', root / 'run', limit=1, settings=Settings(), llm_factory=lambda _: FixtureLLM())
            selected = json.loads((root / 'run/manifest.json').read_text())['trace_ids']
            self.assertEqual(selected, ['fictional_ship_immediate', 'fictional_ship_short', 'fictional_ship_long'])

    async def test_play_without_tts_fails_before_provider_is_constructed(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            prepared(root / 'input')
            def provider(_):
                raise AssertionError('Provider should not be constructed for invalid CLI configuration')
            with self.assertRaisesRegex(ValueError, '--play'):
                await run_b_debug(root / 'input', root / 'run', play=True, settings=Settings(), llm_factory=provider)


if __name__ == '__main__':
    unittest.main()
