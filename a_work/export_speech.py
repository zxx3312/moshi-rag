"""Synthesize saved policy output into ordered sentence and per-run WAV files."""
import argparse
from collections import Counter, OrderedDict
import hashlib
import json
import math
from pathlib import Path
import re
import sys
import time
import wave

from turntaking.cascade import PiperTTS
from turntaking.replay import load_jsonl


def split_sentences(text):
    """Retain decimal points, initials and abbreviations within a sentence.

    Adapted from cascadesystem/presentation.py on a-cascade, commit d337547.
    """
    abbreviations = {"mr", "mrs", "ms", "dr", "prof", "sr", "jr", "st", "vs", "etc",
                     "e.g", "i.e", "a.m", "p.m"}
    closers = "\"'”’」』)]}"
    sentences, start, index = [], 0, 0
    while index < len(text):
        char = text[index]
        boundary = char in "。！？!?"
        if char == ".":
            token = re.search(r"([A-Za-z.]+)\.$", text[:index + 1])
            word = token.group(1) if token else ""
            decimal = index > 0 and index + 1 < len(text) and text[index - 1].isdigit() and text[index + 1].isdigit()
            abbreviated = (word.lower() in abbreviations or len(word) == 1
                           or bool(re.fullmatch(r"(?:[A-Za-z]\.){2,}", word + ".")))
            boundary = (not decimal and not abbreviated
                        and (index + 1 == len(text) or text[index + 1].isspace() or text[index + 1] in closers))
        if boundary:
            end = index + 1
            while end < len(text) and text[end] in "。！？!?" + closers:
                end += 1
            sentence = text[start:end].strip()
            if sentence:
                sentences.append(sentence)
            start = index = end
        else:
            index += 1
    if text[start:].strip():
        sentences.append(text[start:].strip())
    return sentences


def digest(path):
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def select_runs(records, policies=None, max_runs=None):
    """Group log rows in source order, keeping every spoken action."""
    groups = OrderedDict()
    indexes = Counter()
    for row in records:
        if policies and row["policy"] not in policies:
            continue
        run_id = row["run_id"]
        source_index = indexes[run_id]
        indexes[run_id] += 1
        if row["action"] == "Wait" or not row["text"].strip():
            continue
        if run_id not in groups:
            if max_runs is not None and len(groups) >= max_runs:
                continue
            groups[run_id] = []
        group = groups[run_id]
        if group:
            previous = group[-1]
            if any(row[k] != previous[k] for k in ("trace_id", "sample_id", "policy")):
                raise ValueError(f"Inconsistent run identity: {run_id}")
            current_start = row.get("output_start_time_s")
            previous_start = previous.get("output_start_time_s")
            if (isinstance(current_start, (int, float)) and isinstance(previous_start, (int, float))
                    and current_start < previous_start):
                raise ValueError(f"Speech records are out of order: {run_id}")
        group.append(dict(row, source_record_index=source_index))
    if not groups:
        raise ValueError("No spoken records matched the requested policies")
    return groups


def write_wave(path, audio, sample_rate):
    with wave.open(str(path), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        wav.writeframes(audio)


def synthesize_run(records, tts, folder, gap_s):
    """Produce actual sequential audio; offsets are within this offline WAV."""
    folder.mkdir(parents=True)
    segments_dir = folder / "segments"
    segments_dir.mkdir()
    segments = []
    rate = None
    frames = 0
    combined = None
    try:
        for record in records:
            for sentence in split_sentences(record["text"]):
                started = time.monotonic()
                speech = tts.synthesize(sentence)
                elapsed = time.monotonic() - started
                if not speech.audio or not speech.sample_rate or len(speech.audio) % 2:
                    raise ValueError("Piper returned empty or invalid 16-bit audio")
                if rate is None:
                    rate = speech.sample_rate
                    combined = wave.open(str(folder / "response.wav"), "wb")
                    combined.setnchannels(1)
                    combined.setsampwidth(2)
                    combined.setframerate(rate)
                if speech.sample_rate != rate:
                    raise ValueError("Sample rate changed within one response")
                if segments:
                    silence_frames = round(gap_s * rate)
                    combined.writeframesraw(b"\x00\x00" * silence_frames)
                    frames += silence_frames
                start = frames / rate
                segment_file = f"{len(segments) + 1:04d}.wav"
                write_wave(segments_dir / segment_file, speech.audio, rate)
                combined.writeframesraw(speech.audio)
                frames += len(speech.audio) // 2
                segments.append(dict(index=len(segments) + 1, source_record_index=record["source_record_index"],
                                     action=record["action"], text=sentence, file="segments/" + segment_file,
                                     source_output_start_s=record.get("output_start_time_s"),
                                     source_output_end_s=record.get("output_end_time_s"),
                                     audio_start_s=start, audio_end_s=frames / rate,
                                     synthesis_wall_s=elapsed))
    finally:
        if combined is not None:
            combined.close()
    if not segments:
        raise ValueError("No sentences were synthesized")
    (folder / "transcript.txt").write_text("\n".join(segment["text"] for segment in segments) + "\n",
                                            encoding="utf-8")
    (folder / "segments.json").write_text(json.dumps(segments, ensure_ascii=False, indent=2) + "\n",
                                            encoding="utf-8")
    # Bound memory across a large export. Repeated phrases are still cached within a run.
    tts.spoken.clear()
    return dict(segment_count=len(segments), duration_s=frames / rate, sample_rate=rate,
                response_wav="response.wav", segments_file="segments.json", transcript="transcript.txt")


def save_manifest(output, manifest):
    temporary = output / "manifest.json.tmp"
    temporary.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(output / "manifest.json")


def export(records, tts, output, *, policies=None, max_runs=None, gap_s=0.25, metadata=None):
    if not math.isfinite(gap_s) or gap_s < 0:
        raise ValueError("Sentence gap must be finite and nonnegative")
    groups = select_runs(records, policies, max_runs)
    output.mkdir(parents=True, exist_ok=False)
    manifest = dict(metadata or {}, timing_kind="offline_sequential_audio", sentence_gap_s=gap_s,
                    total_runs=len(groups), successful_runs=0, failed_runs=0, runs=[])
    save_manifest(output, manifest)
    for run_id, rows in groups.items():
        folder_name = hashlib.sha256(run_id.encode("utf-8")).hexdigest()[:20]
        folder = output / "runs" / folder_name
        entry = dict(run_id=run_id, sample_id=rows[0]["sample_id"], trace_id=rows[0]["trace_id"],
                     policy=rows[0]["policy"], folder="runs/" + folder_name)
        try:
            entry.update(synthesize_run(rows, tts, folder, gap_s))
            entry["status"] = "ok"
            manifest["successful_runs"] += 1
        except Exception as error:
            entry.update(status="error", error_type=type(error).__name__, error=str(error))
            manifest["failed_runs"] += 1
            tts.spoken.clear()
        manifest["runs"].append(entry)
        save_manifest(output, manifest)
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--logs", type=Path, required=True, help="Existing A policy_log.jsonl")
    parser.add_argument("--voice", type=Path, required=True, help="Piper ONNX voice")
    parser.add_argument("--out", type=Path, required=True, help="New output directory")
    parser.add_argument("--policy", action="append", help="Exact policy name; repeat to select multiple")
    parser.add_argument("--max-runs", type=int, help="Limit the number of run IDs for a smoke test")
    parser.add_argument("--gap-s", type=float, default=0.25, help="Silence between sentences (default: 0.25)")
    args = parser.parse_args()
    if args.max_runs is not None and args.max_runs <= 0:
        parser.error("--max-runs must be positive")
    voice = args.voice.resolve()
    records = load_jsonl(args.logs)
    tts = PiperTTS(voice)
    summary = export(records, tts, args.out, policies=args.policy, max_runs=args.max_runs, gap_s=args.gap_s,
                     metadata={"source_log": str(args.logs.resolve()), "source_sha256": digest(args.logs),
                               "voice": str(voice), "voice_sha256": digest(voice)})
    print(f"Audio export: {summary['successful_runs']}/{summary['total_runs']} runs succeeded; "
          f"{summary['failed_runs']} failed. Output: {args.out}")
    return int(summary["failed_runs"] > 0)


if __name__ == "__main__":
    sys.exit(main())
