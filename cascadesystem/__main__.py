"""Run from repository root: python -m cascadesystem --demo."""
import argparse
import asyncio
from dataclasses import replace
from datetime import datetime, timezone
import json
import importlib.util
from pathlib import Path
import subprocess
import sys
import time
import uuid

from .audio import AudioError, SpeechOutput, transcribe
from .config import Settings
from .controller import Cascade
from .demo import DemoLLM, DemoSearch, QUESTION
from .llm import TinkerLLM
from .search import WikipediaSearch
from .presentation import detect_language, ready_line, sentence_events
from .conversation import Conversation, session_command
from .speech_input import WindowsSpeechInput
from .whisper_input import FasterWhisperInput, VOICE_ENV, voice_python
from .live_audio import InterruptiblePlayer


def arguments():
    parser = argparse.ArgumentParser(description="Independent Tinker + Wikipedia evidence-aware speech cascade")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--question", help="One text question")
    source.add_argument("--audio", type=Path, help="Recorded question; transcribe locally, then research and answer")
    source.add_argument("--demo", action="store_true", help="Fictional offline example, no API calls")
    source.add_argument("--chat", action="store_true", help="Continuous text conversation with bounded history")
    source.add_argument("--listen", action="store_true", help="Continuous turn-by-turn microphone conversation")
    source.add_argument("--speech-info", action="store_true", help="List input devices/recognizers without opening the microphone")
    source.add_argument("--prepare-asr", action="store_true", help="Download and load the optional faster-whisper model; no microphone/API calls")
    source.add_argument("--transcribe", type=Path, help="Transcribe an existing recording only; no LLM/search/TTS")
    parser.add_argument("--output", type=Path, help="New run directory; existing directories are never overwritten")
    parser.add_argument("--tts", choices=["none", "windows", "piper"], default="none")
    parser.add_argument("--play", action="store_true", help="Play generated WAVs sequentially on Windows")
    parser.add_argument("--piper", default="piper", help="Existing Piper executable path")
    parser.add_argument("--voice", help="Existing Piper ONNX voice path")
    parser.add_argument("--whisper", default="whisper", help="Existing Whisper CLI executable path")
    parser.add_argument("--asr-model", default=None, help="Default: small for faster-whisper; turbo for Whisper CLI")
    parser.add_argument("--asr-language", default=None)
    parser.add_argument("--asr-backend", choices=["auto", "faster-whisper", "whisper", "windows"], default="auto", help="Auto prefers the installed local faster-whisper environment; otherwise Windows")
    parser.add_argument("--listen-timeout", type=float, default=10, help="Seconds to wait for speech before listening again")
    parser.add_argument("--silence-seconds", type=float, default=1, help="Silence that ends a spoken question")
    parser.add_argument("--min-confidence", type=float, default=0.3, help="Windows ASR confidence threshold only")
    parser.add_argument("--input-device", help="sounddevice input device ID or name; default is the system input device")
    parser.add_argument("--energy-threshold", type=float, default=0.015, help="Normalized RMS threshold for microphone onset/end detection")
    parser.add_argument("--max-utterance-seconds", type=float, default=30, help="Reject longer microphone questions instead of sending truncated text")
    parser.add_argument("--history-turns", type=int, default=6)
    parser.add_argument("--barge-in", action="store_true", help="Keep listening during answers; requires faster-whisper and a headset (no echo cancellation)")
    parser.add_argument("--barge-onset-seconds", type=float, default=0.18, help="Sustained voice energy needed to trigger interruption")
    parser.add_argument("--continuation-seconds", type=float, default=0.6, help="Additional quiet time to collect a continuation before starting an answer")
    parser.add_argument("--output-device", help="sounddevice output device ID/name for interruptible playback")
    parser.add_argument("--language", choices=["auto", "zh", "en"], default="auto", help="Answer language; auto follows the question")
    parser.add_argument("--show-sources", action="store_true", help="Print search queries, resolved subjects, and returned page titles")
    return parser.parse_args()


def asr_backend(args):
    if args.asr_backend != 'auto':
        return args.asr_backend
    if args.prepare_asr or voice_python().is_file() or importlib.util.find_spec('faster_whisper') is not None:
        return 'faster-whisper'
    return 'windows'


def make_speech_input(args):
    backend = asr_backend(args)
    if backend == 'windows':
        return WindowsSpeechInput(args.asr_language, args.listen_timeout, args.silence_seconds, args.min_confidence)
    if backend == 'faster-whisper':
        return FasterWhisperInput(args.asr_language, args.listen_timeout, args.silence_seconds,
                                  model=args.asr_model or 'small', device=args.input_device,
                                  energy_threshold=args.energy_threshold, max_utterance_s=args.max_utterance_seconds)
    raise ValueError("Whisper CLI handles recordings only; use --asr-backend faster-whisper or windows for --listen")


def relaunch_voice_environment(args):
    """Keep the user's normal python command while isolating optional binary dependencies."""
    needs_voice = args.listen or args.audio or args.transcribe or args.speech_info or args.prepare_asr
    interpreter = voice_python()
    if not needs_voice or asr_backend(args) != 'faster-whisper' or not interpreter.is_file() or Path(sys.prefix).resolve() == VOICE_ENV.resolve():
        return None
    process = subprocess.Popen([str(interpreter), '-m', 'cascadesystem', *sys.argv[1:]])
    try:
        return process.wait()
    except KeyboardInterrupt:
        # Console Ctrl+C reaches both processes. Give the child time to close its microphone.
        try:
            process.wait(timeout=3)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()
        raise


async def run_turn(args, settings, llm, search, output, question, asr=None, history=None, *, turn_state=None):
    """One isolated evidence run; a session passes only bounded conversational context."""
    language = detect_language(question, args.language)
    started_at = time.monotonic()
    state = turn_state if turn_state is not None else {}
    state.setdefault('accept_output', True)
    recorded_events = []
    with (output / "events.jsonl").open("x", encoding="utf-8") as journal, (output / "audio_events.jsonl").open("x", encoding="utf-8") as audio_journal:
        def on_audio(event):
            audio_journal.write(json.dumps(event, ensure_ascii=False) + "\n")
            audio_journal.flush()
            if event["type"] == "playback_started":
                label = f"开始播放 {event['time_s']:.2f}秒" if language == "zh" else f"Playback start {event['time_s']:.2f}s"
                if state['accept_output']:
                    print(f"[{label} | {event['sentence_index']}/{event['sentence_count']}] {event['text']}", flush=True)
            elif event["type"] == "audio_error":
                print(("语音失败：" if language == "zh" else "Speech failed: ") + event["error"], file=sys.stderr)

        device = getattr(args, 'output_device', None)
        device = int(device) if isinstance(device, str) and device.isdecimal() else device
        player = InterruptiblePlayer(started_at, device=device) if getattr(args, 'barge_in', False) and args.play else None
        speech = SpeechOutput(output / "audio", mode=args.tts, piper=args.piper, voice=args.voice, play=args.play,
                              started_at=started_at, on_event=on_audio, player=player)
        state['speech'] = speech
        worker = asyncio.create_task(speech.worker())
        try:
            async def on_event(event):
                recorded_events.append(event)
                journal.write(json.dumps(event, ensure_ascii=False) + "\n")
                journal.flush()
                if not state['accept_output']:
                    return
                if event["type"] == "utterance":
                    for sentence in sentence_events(event):
                        print(ready_line(sentence), flush=True)
                    await speech.submit(event)
                elif event["type"] == "failure":
                    print("Operation failed: " + event["error"], file=sys.stderr)
                elif args.show_sources and event["type"] == "search_started":
                    label = "搜索" if language == "zh" else "Search"
                    print(f"[{label}] {event['query']} | subject={event.get('subject', '')}", flush=True)
                elif args.show_sources and event["type"] == "search_finished":
                    label = "返回页面" if language == "zh" else "Returned pages"
                    print(f"[{label}] " + "; ".join(p['title'] for p in event.get('returned_pages', [])), flush=True)
                elif event["type"] == "context_resolved":
                    print(("[本轮问题] " if language == "zh" else "[Resolved question] ") + event["standalone_question"], flush=True)

            result = await Cascade(llm, search, settings).run(question, on_event, language=language, started_at=started_at, history=history)
            await speech.finish(worker)
        except asyncio.CancelledError:
            state['accept_output'] = False
            await speech.abort(worker)
            resolved = next((e['standalone_question'] for e in recorded_events if e['type'] == 'context_resolved'), question)
            audible = [r['text'] for r in speech.records if r.get('played') and r['status'] == 'ok'] if args.play else [
                e['text'] for e in recorded_events if e['type'] == 'utterance' and e.get('action') in {'Partial Answer', 'Final Answer', 'Correction'}]
            interrupted = {'question': question, 'resolved_question': resolved, 'status': 'interrupted',
                           'events': recorded_events, 'audio': speech.records, 'asr': asr,
                           'audible_response': ' '.join(audible), 'llm_calls': list(getattr(llm, 'calls', [])),
                           'speech_status': 'interrupted', 'interrupted_at_s': time.monotonic() - started_at,
                           'note': 'Queued and partly played sentences are not treated as fully heard; in-flight HTTP may finish remotely.'}
            state['result'] = interrupted
            (output / 'run.json').write_text(json.dumps(interrupted, ensure_ascii=False, indent=2), encoding='utf-8')
            raise
        except BaseException:
            await speech.abort(worker)
            raise
    result.update(demo=args.demo, asr=asr, audio=speech.records,
                  speech_status="disabled" if args.tts == "none" else "ok" if all(r["status"] == "ok" for r in speech.records) else "error")
    (output / "run.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    state['result'] = result
    print(("运行记录：" if language == "zh" else "Run saved: ") + str(output.resolve()))
    return result


def exit_code(result):
    return 1 if result["status"] == "error" or result["speech_status"] == "error" else 0


async def conversation_loop(args, settings, llm, search_factory, output, *, read_text=None, speech_input=None):
    memory = Conversation(max_turns=args.history_turns)
    turn_number = attempt = 0
    if read_text is None:
        read_text = lambda: input("你 / You > ")
    if args.listen and speech_input is None:
        speech_input = make_speech_input(args)
    print("连续对话已开始 / Conversation started. /exit 退出, /reset 清空上下文, /history 查看历史。", flush=True)
    if args.listen:
        prepare = getattr(speech_input, 'prepare', None)
        if prepare is not None:
            print("正在加载本地语音模型 / Loading local speech model...", flush=True)
            await asyncio.to_thread(prepare)
        info = await asyncio.to_thread(speech_input.info)
        if info.get('backend') == 'faster-whisper':
            print(f"ASR: faster-whisper / {info['model']} / CPU int8 / language={speech_input.language}", flush=True)
            if not info.get('input_devices'):
                raise AudioError("No microphone input device is available")
        else:
            print("识别器 / Recognizers: " + ", ".join(r["language"] for r in info.get("recognizers", [])), flush=True)
        print("回答结束后继续收音；说‘退出对话’或 goodbye 结束，‘切换英文’/switch to Chinese 切换识别语言。", flush=True)
    with (output / "session.jsonl").open("x", encoding="utf-8") as session_log:
        def log(kind, **data):
            session_log.write(json.dumps({"type": kind, **data}, ensure_ascii=False) + "\n")
            session_log.flush()

        try:
            while True:
                asr = None
                if args.listen:
                    attempt += 1
                    print("[麦克风 / Listening] 请说话，说完停顿即可。", flush=True)
                    asr = await asyncio.to_thread(speech_input.listen, output / "input" / f"attempt-{attempt:04d}")
                    log("recognition", result=asr)
                    if asr.get("status") != "recognized":
                        reason = {
                            'too_long': '问题过长，请分成较短的问题 / Question too long; please ask a shorter question.',
                            'input_overflow': '采集丢帧，请检查音频设备后重说 / Audio input overflow; check your device and try again.',
                            'low_confidence': '识别不确定，请重说 / Uncertain recognition; please repeat.',
                        }.get(asr.get('status'), '未识别到清晰语音，请重说 / No clear speech; please try again.')
                        print(reason, flush=True)
                        continue
                    question = asr["text"]
                    print("[识别 / Heard] " + question, flush=True)
                else:
                    # Keep terminal input on the main thread so Ctrl+C does not leave a blocked input worker.
                    try:
                        question = read_text()
                    except EOFError:
                        break
                question = question.strip()
                if not question:
                    continue
                command = session_command(question)
                if command:
                    kind, value = command
                    log("command", command=kind, value=value)
                    if kind == "exit":
                        break
                    if kind == "reset":
                        memory.reset()
                        print("上下文已清空 / History cleared.", flush=True)
                    elif kind == "history":
                        for turn in memory.context():
                            print(f"[{turn['turn_id']}] {turn['question']}\n  {turn['assistant_response']}", flush=True)
                    elif kind == "language":
                        args.language = value
                        if speech_input is not None:
                            speech_input.language = value
                        print("语言 / Language: " + value, flush=True)
                    elif kind == "help":
                        print("/exit  /reset  /history  /language zh|en|auto", flush=True)
                    continue
                turn_number += 1
                turn_output = output / f"turn-{turn_number:04d}"
                turn_output.mkdir(exist_ok=False)
                log("turn_started", turn=turn_number, question=question, output=str(turn_output))
                result = await run_turn(args, settings, llm, search_factory(), turn_output, question, asr, memory.context())
                memory.add(result)
                log("turn_finished", turn=turn_number, status=result["status"], speech_status=result["speech_status"])
                # run_turn drains the playback queue before returning; the microphone is closed during answers.
        finally:
            close_input = getattr(speech_input, "close", None)
            if close_input is not None:
                close_input()
            (output / "history.json").write_text(json.dumps(memory.context(), ensure_ascii=False, indent=2), encoding="utf-8")
            log("session_finished", turns=turn_number)
    print("对话结束 / Conversation ended. " + str(output.resolve()), flush=True)
    return 0


async def main(args):
    if args.barge_in and (not args.listen or asr_backend(args) != 'faster-whisper'):
        raise ValueError("--barge-in requires --listen with faster-whisper")
    if args.speech_info:
        listener = make_speech_input(args)
        try:
            print(json.dumps(await asyncio.to_thread(listener.info), ensure_ascii=False, indent=2))
        finally:
            listener.close()
        return 0
    if args.prepare_asr:
        if asr_backend(args) != 'faster-whisper':
            raise ValueError("--prepare-asr requires --asr-backend faster-whisper")
        listener = make_speech_input(args)
        try:
            print("下载/加载语音模型 / Downloading/loading speech model...", flush=True)
            print(json.dumps(await asyncio.to_thread(listener.prepare, download=True), ensure_ascii=False, indent=2))
        finally:
            listener.close()
        return 0
    if args.transcribe:
        output = args.output or Path(__file__).parent / 'artifacts' / ('transcription-' + uuid.uuid4().hex[:8])
        if asr_backend(args) == 'whisper':
            result = await asyncio.to_thread(transcribe, args.transcribe, output, args.whisper, args.asr_model or 'turbo', args.asr_language)
        else:
            listener = make_speech_input(args)
            try:
                result = await asyncio.to_thread(listener.listen, output, args.transcribe)
            finally:
                listener.close()
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result.get('status', 'recognized') == 'recognized' else 1
    settings = Settings.from_env()
    if args.demo:
        settings = replace(settings, progress_s=0.1)
        llm, search = DemoLLM(), DemoSearch()
    else:
        llm, search = TinkerLLM(settings), WikipediaSearch(settings)
    if args.play and args.tts == "none":
        raise ValueError("--play requires --tts windows or --tts piper")
    if args.history_turns < 1:
        raise ValueError("--history-turns must be positive")
    output = args.output or Path(__file__).parent / "artifacts" / (datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8])
    output.mkdir(parents=True, exist_ok=False)
    if args.chat or args.listen:
        if args.barge_in:
            from .duplex import interruptible_session
            return await interruptible_session(args, settings, lambda: TinkerLLM(settings),
                                               lambda: WikipediaSearch(settings), output, run_turn,
                                               recognizer=make_speech_input(args))
        return await conversation_loop(args, settings, llm, lambda: WikipediaSearch(settings), output)
    asr = None
    if args.audio:
        if asr_backend(args) != "whisper":
            listener = make_speech_input(args)
            try:
                asr = await asyncio.to_thread(listener.listen, output / "asr", args.audio)
            finally:
                listener.close()
            if asr.get("status") != "recognized":
                raise AudioError("No clear speech recognized in the input WAV")
        else:
            asr = await asyncio.to_thread(transcribe, args.audio, output / "asr", args.whisper, args.asr_model or 'turbo', args.asr_language)
    question = QUESTION if args.demo else asr["text"] if asr else args.question
    return exit_code(await run_turn(args, settings, llm, search, output, question, asr))


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    try:
        args = arguments()
        relaunched = relaunch_voice_environment(args)
        raise SystemExit(relaunched if relaunched is not None else asyncio.run(main(args)))
    except (ValueError, AudioError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(2)
    except KeyboardInterrupt:
        print("Cancelled.", file=sys.stderr)
        raise SystemExit(130)
