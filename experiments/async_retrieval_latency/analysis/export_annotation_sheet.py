#!/usr/bin/env python
"""Export one row per run for manual annotation of the behaviours the metrics cannot judge.

    python experiments/async_retrieval_latency/analysis/export_annotation_sheet.py RUN_DIR [--manifest M]

Writes RUN_DIR/analysis/annotation_sheet.csv (open in Excel / Google Sheets). Stdlib only.

Label columns (left empty, fill them in while reading the transcripts and listening to *_stereo.wav):
  premature_answer        before the reference arrived, the model stated an answer: none / correct / wrong
  contradiction           after the reference arrived, it contradicted what it said before: y / n
  wait_behaviour          main behaviour while waiting: silence / filler / progress / partial / answer / other
  naturalness_1to5        overall naturalness of the turn, 1 (very unnatural) to 5 (natural)
  notes                   free text
Label blind to the delay condition if you can (sort or hide the delay column first).
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

LABELS = ["premature_answer", "contradiction", "wait_behaviour", "naturalness_1to5", "notes"]


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("run_dir", type=Path)
    args = p.parse_args()

    records = []
    for line in (args.run_dir / "results.jsonl").read_text(encoding="utf-8").splitlines():
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    latest = {r["run_id"]: r for r in records}  # last record per run (a retried run replaces earlier ones)
    rows = []
    for r in sorted(latest.values(), key=lambda r: (r["sample_id"], r.get("seed", 0), r["retrieval_delay_condition"])):
        rows.append({
            "run_id": r["run_id"],
            "sample_id": r["sample_id"],
            "seed": r.get("seed"),
            "delay_s": r["retrieval_delay_condition"],
            "status": r.get("status"),
            "question": r.get("question"),
            "gold_answer": " | ".join(r.get("answer") or []) if isinstance(r.get("answer"), list) else r.get("answer"),
            "rag_triggered": r.get("rag_triggered"),
            "trigger_time": r.get("retrieval_trigger_time"),
            "injection_time": r.get("reference_injection_time"),
            "answer_in_transcript_before_injection (auto)": r.get("answer_mentioned_before_injection"),
            "pre_trigger_transcript": (r.get("pre_trigger") or {}).get("transcript"),
            "pre_rag_transcript": r.get("pre_rag_transcript"),
            "post_rag_transcript": r.get("post_rag_transcript"),
            "stereo_audio": r.get("stereo_audio_path"),
            **{k: "" for k in LABELS},
        })
    out = args.run_dir / "analysis" / "annotation_sheet.csv"
    out.parent.mkdir(exist_ok=True)
    with out.open("w", newline="", encoding="utf-8-sig") as f:  # utf-8-sig: Excel opens it correctly
        w = csv.DictWriter(f, fieldnames=list(rows[0]) if rows else ["run_id"])
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {out} ({len(rows)} runs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
