"""Sample judge-SFT questions from the official train splits (standard library only).

Reuses the record checks, question normalization and round-robin type sampling of
b_work/step2/prepare_step2.py. Every debug and reserved evaluation question is excluded by
sample ID and by normalized question text. Each dataset contributes --per-dataset primary
questions plus --reserve-per-dataset ordered replacements for questions rejected in review.
Train/dev is assigned per question, stratified by source type.
"""

import argparse
from collections import Counter
import json
from pathlib import Path
import random
import sys
from zipfile import ZipFile

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "step2"))
from prepare_step2 import (  # noqa: E402
    SCHEMA_VERSION, file_sha256, normalize, question_key, select_stratified, validate_record, write_jsonl,
)

DATA_VERSION = "sft-v0"
DEV_EVERY = 5  # every fifth question of a source type, in sampling order, goes to dev


def read_rows(path):
    if path.suffix.lower() != ".zip":
        return json.loads(path.read_text(encoding="utf-8")), None
    with ZipFile(path) as archive:
        members = [n for n in archive.namelist() if not n.startswith("__MACOSX/") and Path(n).name == "train.json"]
        if len(members) != 1:
            raise ValueError("Expected exactly one train.json in the 2Wiki archive: " + str(members))
        with archive.open(members[0]) as file:
            return json.load(file), members[0]


def excluded(prepared):
    ids, questions = set(), set()
    for name in ["samples_debug.jsonl", "samples_eval_reserved.jsonl"]:
        for line in (prepared / name).read_text(encoding="utf-8").splitlines():
            row = json.loads(line)
            ids.add(row["sample_id"])
            questions.add(question_key(row["question"]))
    return ids, questions


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hotpot", type=Path, required=True, help="HotpotQA train JSON (convert_hotpot_parquet.py output)")
    parser.add_argument("--twowiki", type=Path, required=True, help="Official April 7 archive, or its train.json")
    parser.add_argument("--step2", type=Path, default=HERE.parent / "step2" / "prepared")
    parser.add_argument("--out", type=Path, default=HERE / "prepared")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--per-dataset", type=int, default=150)
    parser.add_argument("--reserve-per-dataset", type=int, default=30)
    args = parser.parse_args()
    targets = ["samples_sft_candidates.jsonl", "sft_manifest.json"]
    if any((args.out / name).exists() for name in targets):
        parser.error("Output already exists; keep the first valid candidate list or choose a new --out directory")

    used_ids, used_questions = excluded(args.step2)
    excluded_count = len(used_questions)
    candidates, sources = [], []
    definitions = [
        ("hotpotqa", args.hotpot, "https://huggingface.co/datasets/hotpotqa/hotpot_qa (distractor, train parquet)"),
        ("2wikimultihopqa", args.twowiki, "https://www.dropbox.com/s/ms2m13252h6xubs/data_ids_april7.zip?dl=1"),
    ]
    for dataset, path, url in definitions:
        rows, member = read_rows(path)
        valid, rejected = [], Counter()
        for row in rows:
            reason = validate_record(row)
            if not reason and dataset == "2wikimultihopqa" and not row.get("evidences"):
                reason = "missing_evidences"
            if not reason and dataset + "_" + row["_id"] in used_ids:
                reason = "debug_or_reserved_id"
            if reason:
                rejected[reason] += 1
            else:
                valid.append(row)
        rng = random.Random(str(args.seed) + ":sft:" + dataset)
        chosen = select_stratified(valid, args.per_dataset + args.reserve_per_dataset, rng, used_questions)
        rank_in_type = Counter()
        for rank, row in enumerate(chosen, start=1):
            group_rank = rank_in_type[row["type"]]
            rank_in_type[row["type"]] += 1
            record = normalize(row, dataset, "dev" if group_rank % DEV_EVERY == DEV_EVERY - 1 else "train", "train")
            record["data_version"] = DATA_VERSION
            record["candidate_rank"] = rank
            record["candidate_role"] = "primary" if rank <= args.per_dataset else "reserve"
            candidates.append(record)
        sources.append({
            "dataset": dataset,
            "source_url": url,
            "source_filename": path.name,
            "source_sha256": file_sha256(path),
            "zip_train_member": member,
            "total_records": len(rows),
            "valid_records_before_question_dedup": len(valid),
            "rejected_by_reason": dict(rejected),
            "primary_type_counts": dict(Counter(r["type"] for r in chosen[:args.per_dataset])),
            "reserve_type_counts": dict(Counter(r["type"] for r in chosen[args.per_dataset:])),
        })
        print(dataset + ": " + str(len(chosen)) + " candidates (" + str(args.per_dataset) + " primary)")
        del rows, valid

    ids = [r["sample_id"] for r in candidates]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate sample IDs")
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "data_version": DATA_VERSION,
        "stage": "W3_judge_sft_candidates",
        "seed": args.seed,
        "sampling": "round_robin_by_type_after_seeded_shuffle per dataset (prepare_step2.select_stratified); "
                    "Hotpot then 2Wiki; candidate_rank is the replacement order",
        "split_rule": "per source type in candidate order, every " + str(DEV_EVERY) + "th question is dev",
        "question_normalization": "same as step2 (prepare_step2.question_key)",
        "excluded": {"step2_manifest_dir": str(args.step2), "normalized_questions": excluded_count,
                     "sample_ids": len(used_ids)},
        "sources": sources,
        "counts": {
            "candidates": len(candidates),
            "by_role_and_split": dict(Counter(r["candidate_role"] + "/" + r["project_split"] for r in candidates)),
        },
        "notes": [
            "Candidates come from official train only; no debug or reserved evaluation question is included.",
            "Reserve candidates replace rejected primary questions of the same dataset in candidate_rank order.",
            "All snapshots and schedules of a question stay in its project_split.",
        ],
    }
    args.out.mkdir(parents=True, exist_ok=True)
    write_jsonl(args.out / targets[0], candidates)
    manifest["output_sha256"] = {targets[0]: file_sha256(args.out / targets[0])}
    (args.out / targets[1]).write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(manifest["counts"]))


if __name__ == "__main__":
    main()
