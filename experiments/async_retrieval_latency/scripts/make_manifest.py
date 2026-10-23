#!/usr/bin/env python
"""Build a manifest from a folder in the ``moshi.run_inference`` input format.

That format is ``NAME.wav`` plus an optional sidecar ``NAME.json`` with ``topic`` (question),
``gt_reference_text`` and ``answer``. Samples without a reference are skipped, unless
``--default-reference`` is given.

    python experiments/async_retrieval_latency/scripts/make_manifest.py INPUT_DIR OUT.jsonl
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("input_dir", type=Path)
    p.add_argument("output", type=Path)
    p.add_argument("--default-reference", type=str, default=None)
    args = p.parse_args()

    if args.output.exists():
        print(f"refusing to overwrite {args.output}", file=sys.stderr)
        return 1
    rows, skipped = [], []
    for wav in sorted(args.input_dir.glob("*.wav"), key=lambda x: str(x).lower()):
        side = wav.with_suffix(".json")
        meta = json.loads(side.read_text(encoding="utf-8")) if side.is_file() else {}
        ref = meta.get("gt_reference_text") or args.default_reference
        if not ref:
            skipped.append(wav.name)
            continue
        rows.append({
            "sample_id": wav.stem.replace(" ", "_"),
            "wav": str(wav.resolve()),
            "question": meta.get("topic"),
            "reference_text": ref,
            "answer": meta.get("answer"),
        })
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    print(f"wrote {len(rows)} samples to {args.output}; skipped {len(skipped)} without a reference")
    return 0


if __name__ == "__main__":
    sys.exit(main())
