"""Write annotation worksheets for the SFT candidates, one Markdown file per batch (standard library only).

Each question lists its source answer, supporting facts, 2Wiki evidence triples, and every context
document with numbered sentences; supporting-fact sentences are marked with *. Batches hold one
dataset each, in candidate_rank order, so reserves come after all primary questions.
"""

import argparse
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def worksheet(sample):
    support = {(title, index) for title, index in sample["supporting_facts"]}
    lines = ["## " + sample["sample_id"] + " (rank " + str(sample["candidate_rank"]) + ", " + sample["candidate_role"]
             + ", type " + sample["type"] + ")", "",
             "Question: " + sample["question"], "Source answer: " + sample["answer"],
             "Supporting facts: " + json.dumps(sample["supporting_facts"], ensure_ascii=False)]
    if sample.get("evidences"):
        lines.append("Evidence triples: " + json.dumps(sample["evidences"], ensure_ascii=False))
    lines.append("")
    for number, (title, sentences) in enumerate(sample["context"], start=1):
        lines.append("Document " + str(number) + ": " + title)
        for index, text in enumerate(sentences):
            lines.append(("* " if (title, index) in support else "  ") + str(index) + ": " + text.strip())
    return lines + [""]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates", type=Path, default=HERE / "prepared" / "samples_sft_candidates.jsonl")
    parser.add_argument("--out", type=Path, default=HERE / "drafts")
    parser.add_argument("--size", type=int, default=30)
    args = parser.parse_args()
    samples = [json.loads(line) for line in args.candidates.read_text(encoding="utf-8").splitlines()]
    args.out.mkdir(parents=True, exist_ok=True)
    count = 0
    for dataset in ["hotpotqa", "2wikimultihopqa"]:
        rows = sorted((s for s in samples if s["dataset"] == dataset), key=lambda s: s["candidate_rank"])
        for start in range(0, len(rows), args.size):
            batch = rows[start:start + args.size]
            name = "batch_" + dataset[:5] + "_" + str(start // args.size + 1).zfill(2)
            lines = ["# Worksheet " + name, "", "Ranks " + str(batch[0]["candidate_rank"]) + "–"
                     + str(batch[-1]["candidate_rank"]) + " of " + dataset + ".", ""]
            for sample in batch:
                lines += worksheet(sample)
            (args.out / (name + ".md")).write_text("\n".join(lines), encoding="utf-8")
            count += 1
    print(str(count) + " worksheets written to " + str(args.out))


if __name__ == "__main__":
    main()
