"""Build the control-experiment manifest: one line per question with its spoken WAV,
gold answers, and a progressive evidence trace (times in seconds after the question ends).

  * 12 hard SimpleQA questions from the diagnosis pilot: one reference at --delay seconds.
  * configs/multihop.json: two-hop questions with two evidence arrivals.

Question audio is synthesized with Piper (same voice as the pilot) when missing:

    python3 a_work/moshirag_control/build_manifest.py \
        --tts-python /projects/illinois/eng/cs/dilek/xzhu81/envs/tts/bin/python \
        --voice /projects/illinois/eng/cs/dilek/xzhu81/piper_voices/en_US-lessac-medium.onnx
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
PILOT = REPO / "experiments/async_retrieval_latency/configs/samples_hard_pilot.jsonl"
TTS_SCRIPT = REPO / "experiments/async_retrieval_latency/scripts/make_tts_question.py"


def simpleqa_samples(delay_s):
    with open(PILOT, encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            yield {
                "sample_id": r["sample_id"],
                "question": r["question"],
                "events": [{"evidence_id": "ref", "visible_time_s": delay_s, "text": r["reference_text"]}],
                "units": [{"unit_id": "u1", "necessary": True, "answer": r["answer"], "support": ["ref"]}],
                "source": r.get("source"),
            }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--delay", type=float, default=8.0, help="Reference arrival for SimpleQA questions.")
    ap.add_argument("--out", type=Path, default=HERE / "configs/control_manifest.jsonl")
    ap.add_argument("--tts-python", type=Path, required=True)
    ap.add_argument("--voice", type=Path, required=True)
    args = ap.parse_args()

    samples = list(simpleqa_samples(args.delay))
    samples += json.loads((HERE / "configs/multihop.json").read_text(encoding="utf-8"))

    audio_dir = args.out.parent / "audio"
    for s in samples:
        wav = audio_dir / f"{s['sample_id']}.wav"
        if not wav.exists():
            subprocess.run([str(args.tts_python), str(TTS_SCRIPT), "--voice", str(args.voice),
                            "--text", s["question"], "--out", str(wav)], check=True)
        s["wav"] = str(wav.relative_to(args.out.parent))
        s["answer"] = [a for u in s["units"] if u["necessary"] for a in u["answer"]]

    with open(args.out, "w", encoding="utf-8") as f:
        for s in samples:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    print(f"wrote {len(samples)} samples to {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
