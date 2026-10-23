#!/usr/bin/env python
"""Pick a reproducible pilot set of hard questions from OpenAI's SimpleQA test set (MIT license).

SimpleQA questions are short factual questions most models cannot answer from memory, which is
the case where MoshiRAG must rely on retrieval. Selection is rule-based plus a fixed-seed sample
(no hand-picking):

- answer_type Person or Place: the "first informative content" heuristic matches the gold
  answer string in the transcript, which works for names but not for dates/numbers that the
  model speaks as words. (This narrows the question types; note it when reporting.)
- question <= 16 words, ASCII, only letters/digits/spaces and , . ' - ? (speakable by TTS)
- answer <= 4 words, only letters/spaces and . ' - (a single short name)

Output: one JSON object per line with the question, gold answer, row index and source URLs.
References are written separately (see configs/samples_hard_pilot.jsonl).

    python experiments/async_retrieval_latency/scripts/build_simpleqa_pilot.py OUT.jsonl
"""

from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import json
import random
import re
import sys
import urllib.request
from pathlib import Path

URL = "https://openaipublic.blob.core.windows.net/simple-evals/simple_qa_test_set.csv"
SHA256_PREFIX = "feee3f7e7db3617e"  # version used for the pilot (4326 rows)
QUESTION_OK = re.compile(r"^[A-Za-z0-9 ,.'\-?]+$")
ANSWER_OK = re.compile(r"^[A-Za-z .'\-]+$")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("output", type=Path)
    p.add_argument("--csv", type=Path, default=None, help="Local copy of simple_qa_test_set.csv (else downloaded).")
    p.add_argument("-n", type=int, default=12)
    p.add_argument("--seed", type=int, default=20261006)
    p.add_argument("--max-question-words", type=int, default=16)
    p.add_argument("--max-answer-words", type=int, default=4)
    args = p.parse_args()

    raw = args.csv.read_bytes() if args.csv else urllib.request.urlopen(URL, timeout=60).read()
    digest = hashlib.sha256(raw).hexdigest()
    if not digest.startswith(SHA256_PREFIX):
        print(f"WARNING: SimpleQA file hash {digest[:16]} differs from the pilot's {SHA256_PREFIX}", file=sys.stderr)
    rows = list(csv.DictReader(raw.decode("utf-8").splitlines()))

    eligible = []
    for idx, r in enumerate(rows):
        meta = ast.literal_eval(r["metadata"])
        q, a = r["problem"].strip(), r["answer"].strip()
        if meta.get("answer_type") not in ("Person", "Place"):
            continue
        if not (QUESTION_OK.match(q) and q.endswith("?") and len(q.split()) <= args.max_question_words):
            continue
        if not (ANSWER_OK.match(a) and len(a.split()) <= args.max_answer_words):
            continue
        eligible.append({"row": idx, "question": q, "answer": a, "answer_type": meta.get("answer_type"),
                         "topic": meta.get("topic"), "urls": meta.get("urls", [])})

    random.Random(args.seed).shuffle(eligible)
    picked = sorted(eligible[: args.n], key=lambda x: x["row"])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in picked), encoding="utf-8")
    print(f"{len(rows)} rows, {len(eligible)} eligible, wrote {len(picked)} to {args.output} "
          f"(seed {args.seed}, file sha256 {digest[:16]})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
