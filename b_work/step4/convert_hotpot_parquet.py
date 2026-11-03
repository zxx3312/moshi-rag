"""Convert the Hugging Face HotpotQA distractor train parquet files to the original JSON layout.

The original train URL (curtis.ml.cmu.edu) is unreachable and the RAGLAB mirror has no train file,
so train comes from the hotpotqa/hotpot_qa dataset on Hugging Face (distractor config). Each record is
rewritten to the field layout of hotpot_train_v1.1.json so that prepare_sft.py reads both datasets the
same way. Needs pyarrow (the only non-standard dependency in this step).
"""

import argparse
import json
from pathlib import Path

import pyarrow.parquet as pq


def convert(record):
    facts = record["supporting_facts"]
    context = record["context"]
    return {
        "_id": record["id"],
        "question": record["question"],
        "answer": record["answer"],
        "type": record["type"],
        "level": record["level"],
        "supporting_facts": [[title, index] for title, index in zip(facts["title"], facts["sent_id"])],
        "context": [[title, sentences] for title, sentences in zip(context["title"], context["sentences"])],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("parquet", type=Path, nargs="+")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        parser.error("Output already exists: " + str(args.out))
    rows = []
    for path in sorted(args.parquet):
        rows += [convert(record) for record in pq.read_table(path).to_pylist()]
    args.out.write_text(json.dumps(rows, ensure_ascii=False), encoding="utf-8")
    print(str(len(rows)) + " records written to " + str(args.out))


if __name__ == "__main__":
    main()
