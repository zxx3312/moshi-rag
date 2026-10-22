"""Cut a short clip of MoshiRAG's own speech (audio + text tokens) out of a finished run,
so it can be replayed later as a deterministic Backchannel / Progress / release cue.

    python3 a_work/moshirag_control/make_clips.py RUN_DIR RUN_ID "Let me look it up for you. One moment." look_it_up

The model WAV and the per-step text tokens (control rows) share the 80 ms step clock,
so the clip is the same step range in both. Stdlib only.
"""
import argparse
import json
import wave
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKIP = ("<pad>", "[RET]")


def locate(model_text, phrase):
    """Step range [start, end) of the content pieces that spell `phrase` (case-insensitive)."""
    chars, owner = [], []
    for step, piece in enumerate(model_text):
        if piece in SKIP:
            continue
        for ch in piece.replace("▁", " "):
            chars.append(ch.lower())
            owner.append(step)
    text = "".join(chars)
    i = text.find(phrase.lower())
    if i < 0:
        raise SystemExit(f"phrase not found in transcript: {text!r}")
    return owner[i], owner[i + len(phrase) - 1] + 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run_dir", type=Path)
    ap.add_argument("run_id")
    ap.add_argument("phrase")
    ap.add_argument("name")
    ap.add_argument("--pad-after", type=int, default=2, help="Extra steps after the last piece (word tail).")
    ap.add_argument("--out-dir", type=Path, default=HERE / "configs/clips")
    args = ap.parse_args()

    trace = json.loads((args.run_dir / "traces" / f"{args.run_id}.json").read_text(encoding="utf-8"))
    exp = trace["experiment"]
    start, end = locate(trace["model_text"], args.phrase)
    end += args.pad_after
    tokens = {r["step"]: r["token"] for r in trace["control"]["rows"]}
    frame = int(exp["frame_size"])

    with wave.open(str(args.run_dir / exp["output_audio_path"]), "rb") as wf:
        sr, width = wf.getframerate(), wf.getsampwidth()
        wf.setpos(start * frame)
        pcm = wf.readframes((end - start) * frame)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    with wave.open(str(args.out_dir / f"{args.name}.wav"), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(width)
        wf.setframerate(sr)
        wf.writeframes(pcm)
    meta = {
        "name": args.name, "phrase": args.phrase, "source_run": args.run_id, "source_dir": args.run_dir.name,
        "start_step": start, "end_step": end, "frames": end - start,
        "text_tokens": [tokens[s] for s in range(start, end)],
        "pieces": trace["model_text"][start:end],
    }
    (args.out_dir / f"{args.name}.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{args.name}: steps {start}-{end} ({(end - start) / 12.5:.2f} s): {' '.join(meta['pieces'])}")


if __name__ == "__main__":
    main()
