"""Barge-in session orchestration: invalidate, cancel, listen, resolve, research again."""
import asyncio
import json
import math
import time

from .audio import AudioError
from .conversation import Conversation, session_command
from .live_audio import LiveMicrophone


async def interruptible_session(args, settings, llm_factory, search_factory, output, run_turn, *, recognizer=None, event_source=None):
    for value, lower, upper, label in [(args.barge_onset_seconds, 0.04, 1, 'barge onset'),
                                       (args.continuation_seconds, 0, 5, 'continuation delay')]:
        if not math.isfinite(value) or not lower <= value <= upper:
            raise ValueError(f'Invalid {label}: expected {lower}..{upper} seconds')
    source = event_source or LiveMicrophone(recognizer, output / 'input', onset_s=args.barge_onset_seconds)
    memory = Conversation(max_turns=args.history_turns)
    running = event_task = None
    turn_number, ignored_through = 0, 0
    current, pending, fragments = {}, set(), {}
    ready_at = None
    with (output / 'session.jsonl').open('x', encoding='utf-8') as journal:
        def log(kind, **data):
            journal.write(json.dumps({'type': kind, 'time_monotonic': time.monotonic(), **data}, ensure_ascii=False) + '\n')
            journal.flush()

        async def settle_turn(*, interrupt=False):
            nonlocal running, current
            if running is None:
                return
            task, metadata = running, current
            running, current = None, {}
            was_running = not task.done()
            if interrupt and was_running:
                metadata['state']['accept_output'] = False
                speech = metadata['state'].get('speech')
                if speech is not None and speech.player is not None:
                    speech.player.abort()
                task.cancel()
            await asyncio.gather(task, return_exceptions=True)
            if not task.cancelled():
                error = task.exception()
                if error is not None:
                    raise error
                result = task.result()
            else:
                result = metadata['state'].get('result', {
                    'question': metadata['question'], 'status': 'interrupted', 'events': [], 'audible_response': ''})
            memory.add(result)
            log('turn_interrupted' if result['status'] == 'interrupted' else 'turn_finished',
                turn=turn_number, status=result['status'], question=metadata['question'])

        try:
            print('打断模式：请戴耳机，麦克风持续收音 / Barge-in: use a headset; microphone stays active.', flush=True)
            await source.start()
            event_task = asyncio.create_task(source.next_event())
            while True:
                timeout = max(0, ready_at - asyncio.get_running_loop().time()) if ready_at is not None else None
                watched = {event_task}
                if running is not None:
                    watched.add(running)
                done, _ = await asyncio.wait(watched, timeout=timeout, return_when=asyncio.FIRST_COMPLETED)
                # Process speech onset first when onset and task completion arrive together.
                if event_task in done:
                    event = event_task.result()
                    event_task = asyncio.create_task(source.next_event())
                    log('input_event', event=event)
                    kind = event['type']
                    if kind == 'error':
                        raise AudioError(event['error'])
                    if kind == 'ready':
                        print('[麦克风 / Listening] 可以提问，回答中也可直接补充。', flush=True)
                    elif kind == 'speech_started':
                        pending.add(event['segment_id'])
                        ready_at = None
                        if running is not None:
                            active = not running.done()
                            await settle_turn(interrupt=True)
                            if active:
                                print('[已打断 / Interrupted] 请继续说。', flush=True)
                    elif kind == 'transcript':
                        sid, result = event['segment_id'], event['result']
                        pending.discard(sid)
                        if sid <= ignored_through:
                            continue
                        if result.get('status') != 'recognized':
                            print('[请重说 / Please repeat] ' + result.get('status', 'unknown'), flush=True)
                            # Keep earlier accepted fragments, but never start an answer from a truncated request.
                            fragments.clear()
                            ready_at = None
                            ignored_through = sid
                            continue
                        text = result['text'].strip()
                        print('[识别 / Heard] ' + text, flush=True)
                        command = session_command(text)
                        if command:
                            action, value = command
                            log('command', command=action, value=value)
                            fragments.clear()
                            ignored_through, ready_at = sid, None
                            await settle_turn(interrupt=True)
                            if action == 'exit':
                                break
                            if action == 'reset':
                                memory.reset()
                                print('上下文已清空 / History cleared.', flush=True)
                            elif action == 'pause':
                                print('已停下，补充后继续说 / Paused; continue when ready.', flush=True)
                            elif action == 'language':
                                args.language = value
                                if recognizer is not None:
                                    recognizer.language = value
                            elif action == 'history':
                                for turn in memory.context():
                                    print(f"[{turn['turn_id']}] {turn['question']}\n  {turn['assistant_response']}", flush=True)
                            elif action == 'help':
                                print('退出对话 / goodbye; 清空上下文; 等一下 / stop; 切换英文 / switch to Chinese', flush=True)
                        else:
                            fragments[sid] = result
                            if not pending:
                                ready_at = asyncio.get_running_loop().time() + args.continuation_seconds
                if running is not None and running.done():
                    await settle_turn()
                if ready_at is not None and asyncio.get_running_loop().time() >= ready_at and not pending and fragments:
                    # A newer onset queued during this loop gets priority over starting an outdated turn.
                    if event_task.done():
                        continue
                    ordered = [fragments[sid] for sid in sorted(fragments)]
                    question = '\n'.join(r['text'] for r in ordered)
                    if len(question) > 4000:
                        print('问题过长，请分开提问 / Combined question is too long.', flush=True)
                        fragments.clear()
                        ready_at = None
                        continue
                    turn_number += 1
                    turn_output = output / f'turn-{turn_number:04d}'
                    turn_output.mkdir(exist_ok=False)
                    state = {'accept_output': True}
                    current = {'state': state, 'question': question}
                    log('turn_started', turn=turn_number, question=question, segments=len(ordered))
                    running = asyncio.create_task(run_turn(args, settings, llm_factory(), search_factory(), turn_output,
                                                          question, asr={'segments': ordered, 'backend': 'live-faster-whisper'},
                                                          history=memory.context(), turn_state=state))
                    fragments, ready_at = {}, None
        finally:
            try:
                if running is not None:
                    await settle_turn(interrupt=True)
            finally:
                if event_task is not None:
                    event_task.cancel()
                    await asyncio.gather(event_task, return_exceptions=True)
                try:
                    await source.finish()
                finally:
                    (output / 'history.json').write_text(json.dumps(memory.context(), ensure_ascii=False, indent=2), encoding='utf-8')
                    log('session_finished', turns=turn_number)
    print('对话结束 / Conversation ended. ' + str(output.resolve()), flush=True)
    return 0
