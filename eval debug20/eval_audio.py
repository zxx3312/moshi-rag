"""Optional local speech output during replay, plus one playable WAV per trace."""
import asyncio
from pathlib import Path
import wave

from cascadesystem.audio import AudioError, SpeechOutput

from eval_common import write_json, write_jsonl


def merge_waves(records, destination):
    """Keep measured playback gaps, or preview the speech at synthesis-ready times."""
    if not records or any(not row.get('path') for row in records):
        raise AudioError('Some speech segments were not synthesized')
    chunks, cursor, fmt, timeline = [], 0, None, []
    for row in records:
        with wave.open(row['path'], 'rb') as stream:
            current = stream.getnchannels(), stream.getsampwidth(), stream.getframerate(), stream.getcomptype()
            if fmt is None:
                fmt = current
            if current != fmt or current[3] != 'NONE':
                raise AudioError('Speech segments must use the same PCM WAV format')
            frames = stream.getnframes()
            data = stream.readframes(frames)
        ready = row.get('playback_started_s')
        if ready is None:
            ready = row['synthesis_finished_s']
        start = max(cursor, round(max(0, ready) * fmt[2]))
        silence = bytes([128]) if fmt[1] == 1 else b'\0'
        chunks.extend([silence * ((start - cursor) * fmt[0] * fmt[1]), data])
        timeline.append({'event_sequence': row['event_sequence'], 'sentence_index': row['sentence_index'],
                         'action': row['action'], 'text': row['text'],
                         'wave_start_s': start / fmt[2], 'wave_end_s': (start + frames) / fmt[2]})
        cursor = start + frames
    with wave.open(str(destination), 'wb') as output:
        output.setnchannels(fmt[0])
        output.setsampwidth(fmt[1])
        output.setframerate(fmt[2])
        output.writeframes(b''.join(chunks))
    return {'path': str(Path(destination).resolve()), 'duration_s': cursor / fmt[2], 'timeline': timeline}


class TraceAudio:
    def __init__(self, directory, *, mode='none', play=False, started_at=None, speech_factory=SpeechOutput):
        if mode not in {'none', 'windows'} or play and mode == 'none':
            raise ValueError('--play requires --tts windows')
        self.directory, self.mode, self.play = Path(directory), mode, play
        self.events, self.texts, self.speech, self.worker = [], [], None, None
        self.result = {'enabled': mode != 'none', 'mode': mode, 'play': play, 'status': 'disabled'}
        if mode != 'none':
            self.directory.mkdir(parents=True, exist_ok=False)
            self.speech = speech_factory(self.directory / 'segments', mode=mode, play=play,
                                         started_at=started_at, on_event=self.on_audio_event)
            self.worker = asyncio.create_task(self.speech.worker())

    def on_audio_event(self, event):
        self.events.append(event)
        # Persist progress even if playback is cancelled before finishing the trace.
        write_jsonl(self.directory / 'audio_events.jsonl', self.events)

    async def submit(self, event):
        if self.speech is not None and event.get('type') == 'utterance':
            self.texts.append(event)
            (self.directory / 'responses.txt').write_text('\n\n'.join(
                f"[{e['time_s']:.3f}s | {e['action']}]\n{e['text']}" for e in self.texts) + '\n', encoding='utf-8')
            print(f"[Text {event['time_s']:.2f}s | {event['action']}] {event['text']}", flush=True)
            await self.speech.submit(event)

    async def finish(self, *, cancelled=False):
        if self.speech is None:
            return self.result
        error = None
        try:
            if cancelled:
                await self.speech.abort(self.worker)
            else:
                await self.speech.finish(self.worker)
        except Exception as exc:
            error = type(exc).__name__
            await self.speech.abort(self.worker)
        records = self.speech.records
        self.result.update(status='cancelled' if cancelled else 'error' if error or any(r['status'] != 'ok' for r in records) else 'ok',
                           errors=[r.get('error', r['status']) for r in records if r['status'] != 'ok'], records=records)
        if error:
            self.result['errors'].append(error)
        if not cancelled:
            try:
                self.result['wave'] = merge_waves(records, self.directory / 'response.wav')
            except (AudioError, OSError, wave.Error, KeyError) as exc:
                self.result['status'] = 'error'
                self.result['errors'].append(str(exc))
        write_json(self.directory / 'audio_index.json', self.result)
        if self.result.get('wave'):
            print('Audio: ' + self.result['wave']['path'], flush=True)
        return self.result
