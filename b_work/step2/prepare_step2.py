"""Prepare debug data and a separate reserved evaluation subset (standard library only)."""

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import random
import re
import unicodedata
from zipfile import ZipFile


SCHEMA_VERSION = "1.0"
DATA_VERSION = "debug-v0"


def question_key(text):
    text = unicodedata.normalize("NFKC", text).casefold()
    return " ".join(re.findall(r"\w+", text))


def file_sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for block in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_source(path, is_zip=False):
    member = None
    aliases_member = None
    if is_zip:
        with ZipFile(path) as archive:
            matches = []
            for name in archive.namelist():
                if not name.startswith("__MACOSX/") and Path(name).name == "dev.json":
                    matches.append(name)
                if Path(name).name == "id_aliases.json":
                    aliases_member = name
            if len(matches) != 1:
                raise ValueError("Expected exactly one dev.json in the 2Wiki archive: " + str(matches))
            member = matches[0]
            with archive.open(member) as file:
                rows = json.load(file)
    else:
        with path.open("r", encoding="utf-8") as file:
            rows = json.load(file)
    if not isinstance(rows, list):
        raise ValueError("Expected a top-level JSON array: " + str(path))
    return rows, member, aliases_member


def validate_record(row):
    if not isinstance(row, dict):
        return "record_not_object"
    for key in ["_id", "question", "answer", "context", "supporting_facts"]:
        if key not in row:
            return "missing_" + key
    if not isinstance(row["_id"], str) or not row["_id"].strip():
        return "invalid_id"
    if not isinstance(row["question"], str) or not row["question"].strip():
        return "empty_question"
    if not isinstance(row["answer"], str) or not row["answer"].strip():
        return "empty_or_nonstring_answer"
    if not isinstance(row["context"], list):
        return "invalid_context"
    titles = {}
    for paragraph in row["context"]:
        if not isinstance(paragraph, list) or len(paragraph) != 2:
            return "invalid_context_item"
        title, sentences = paragraph
        if not isinstance(title, str) or not isinstance(sentences, list):
            return "invalid_title_or_sentences"
        if title in titles:
            return "ambiguous_duplicate_title"
        if not all(isinstance(sentence, str) for sentence in sentences):
            return "invalid_sentence"
        titles[title] = sentences
    facts = row["supporting_facts"]
    if not isinstance(facts, list) or not facts:
        return "empty_supporting_facts"
    for fact in facts:
        if not isinstance(fact, list) or len(fact) != 2:
            return "invalid_support_item"
        title, index = fact
        if title not in titles:
            return "support_title_missing"
        if type(index) is not int or index < 0 or index >= len(titles[title]):
            return "support_index_out_of_range"
    return None


def select_stratified(rows, count, rng, used_questions):
    groups = defaultdict(list)
    for row in rows:
        group = str(row.get("type", "unspecified"))
        groups[group].append(row)
    for group in sorted(groups):
        groups[group].sort(key=lambda row: row["_id"])
        rng.shuffle(groups[group])
    selected = []
    while len(selected) < count:
        progress = False
        for group in sorted(groups):
            if len(selected) == count:
                break
            while groups[group]:
                row = groups[group].pop()
                key = question_key(row["question"])
                if key in used_questions:
                    continue
                used_questions.add(key)
                selected.append(row)
                progress = True
                break
        if not progress:
            raise ValueError("Not enough unique valid questions for requested split size")
    return selected


def normalize(row, dataset, split, source_split):
    result = {
        "schema_version": SCHEMA_VERSION,
        "data_version": DATA_VERSION,
        "sample_id": dataset + "_" + row["_id"],
        "dataset": dataset,
        "source_split": source_split,
        "source_id": row["_id"],
        "project_split": split,
        "question": row["question"],
        "answer": row["answer"],
        "context": row["context"],
        "supporting_facts": row["supporting_facts"],
        "type": row.get("type", "unspecified"),
        "annotation_review_status": "pending_human_review"
    }
    for key in ["evidences", "answer_id", "evidences_id", "entity_ids", "level", "source_records", "context_origin"]:
        if key in row:
            result[key] = row[key]
    return result


def write_jsonl(path, rows):
    with path.open("w", encoding="utf-8") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hotpot", type=Path, required=True)
    parser.add_argument("--twowiki", type=Path, required=True, help="Official April 7 archive, or its dev.json")
    parser.add_argument("--custom", type=Path, default=Path(__file__).with_name("custom_debug.json"))
    parser.add_argument("--out", type=Path, default=Path("b_work/step2/prepared"))
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--eval-per-dataset", type=int, default=150)
    args = parser.parse_args()
    if args.eval_per_dataset < 0:
        parser.error("--eval-per-dataset must be nonnegative")
    targets = ["samples_debug.jsonl", "samples_eval_reserved.jsonl", "split_manifest.json"]
    for name in targets:
        if (args.out / name).exists():
            parser.error("Output already exists; preserve frozen IDs and choose a new --out directory")

    with args.custom.open("r", encoding="utf-8") as file:
        custom = json.load(file)
    if not isinstance(custom, list) or len(custom) != 4:
        raise ValueError("Exactly four custom debug records are required")
    debug = []
    reserved = []
    used_questions = set()
    ids = set()
    for row in custom:
        reason = validate_record(row)
        if reason:
            raise ValueError("Invalid custom record: " + reason)
        if not row.get("source_records"):
            raise ValueError("Custom question is missing source provenance")
        key = question_key(row["question"])
        if key in used_questions or row["_id"] in ids:
            raise ValueError("Duplicate custom question or ID")
        ids.add(row["_id"])
        used_questions.add(key)
        debug.append(normalize(row, "custom", "debug", "custom_debug"))

    sources = []
    definitions = [
        ("hotpotqa", args.hotpot, "http://curtis.ml.cmu.edu/datasets/hotpot/hotpot_dev_distractor_v1.json", "dev_distractor_v1"),
        ("2wikimultihopqa", args.twowiki, "https://www.dropbox.com/s/ms2m13252h6xubs/data_ids_april7.zip?dl=1", "data_ids_april7")
    ]
    for dataset, path, url, version in definitions:
        rows, member, aliases = read_source(path, path.suffix.lower() == ".zip")
        valid = []
        rejected = Counter()
        seen_ids = set()
        missing_evidences = 0
        for row in rows:
            reason = validate_record(row)
            if reason:
                rejected[reason] += 1
                continue
            if row["_id"] in seen_ids:
                raise ValueError("Duplicate source ID in " + dataset + ": " + row["_id"])
            seen_ids.add(row["_id"])
            if dataset == "2wikimultihopqa" and "evidences" not in row:
                missing_evidences += 1
                rejected["missing_evidences"] += 1
                continue
            valid.append(row)
        rng = random.Random(str(args.seed) + ":" + dataset)
        chosen_debug = select_stratified(valid, 8, rng, used_questions)
        chosen_eval = select_stratified(valid, args.eval_per_dataset, rng, used_questions)
        for row in chosen_debug:
            debug.append(normalize(row, dataset, "debug", "dev"))
        for row in chosen_eval:
            reserved.append(normalize(row, dataset, "eval_reserved", "dev"))
        sources.append({
            "dataset": dataset,
            "expected_official_source_url": url,
            "declared_version": version,
            "source_filename": path.name,
            "source_sha256": file_sha256(path),
            "official_checksum_verified": False,
            "zip_dev_member": member,
            "zip_aliases_member": aliases,
            "total_records": len(rows),
            "valid_records_before_question_dedup": len(valid),
            "rejected_by_reason": dict(rejected),
            "debug_type_counts": dict(Counter(str(r.get("type", "unspecified")) for r in chosen_debug)),
            "eval_type_counts": dict(Counter(str(r.get("type", "unspecified")) for r in chosen_eval))
        })
        print(dataset + ": selected 8 debug and " + str(len(chosen_eval)) + " reserved evaluation questions")
        del valid, rows, chosen_debug, chosen_eval

    all_records = debug + reserved
    all_ids = [row["sample_id"] for row in all_records]
    if len(all_ids) != len(set(all_ids)):
        raise ValueError("Duplicate global sample IDs")
    debug.sort(key=lambda row: row["sample_id"])
    reserved.sort(key=lambda row: row["sample_id"])
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "data_version": DATA_VERSION,
        "stage": "W1_debug_and_eval_reservation",
        "seed": args.seed,
        "sampling": "round_robin_by_type_after_seeded_shuffle; custom-first then Hotpot then 2Wiki; excludes used normalized questions",
        "question_normalization": "Unicode NFKC, casefold, Unicode word tokens, collapsed spaces; exact normalized matches only",
        "sources": sources,
        "custom_file_sha256": file_sha256(args.custom),
        "splits": {
            "debug": {"count": len(debug), "sample_ids": [r["sample_id"] for r in debug]},
            "eval_reserved": {"count": len(reserved), "sample_ids": [r["sample_id"] for r in reserved]},
            "train": {"status": "pending_official_train_data"},
            "dev": {"status": "pending_heldout_partition_of_official_train"}
        },
        "notes": [
            "Reserved evaluation questions are from official dev, not hidden official test.",
            "Do not inspect reserved answers to tune prompts or thresholds.",
            "All snapshots, delays, and policy runs of a question must keep its project split.",
            "Future train/dev preparation must exclude both used IDs and normalized questions in this manifest.",
            "Source hashes identify downloaded bytes; no official checksum verification is claimed.",
            "Preserve the original 2Wiki archive and its alias table for later official evaluation.",
            "Structural validation is not human verification of semantic support.",
            "Custom examples are NASA-focused, source-derived debug questions, not a representative benchmark.",
            "No retrieval, model inference, evidence scheduling, or answer-unit annotation was performed."
        ]
    }
    args.out.mkdir(parents=True, exist_ok=True)
    write_jsonl(args.out / targets[0], debug)
    write_jsonl(args.out / targets[1], reserved)
    manifest["output_sha256"] = {name: file_sha256(args.out / name) for name in targets[:2]}
    (args.out / targets[2]).write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Debug total: " + str(len(debug)))
    print("Reserved evaluation total: " + str(len(reserved)))
    print("Output directory: " + str(args.out))
    print("Train/dev preparation is pending; review the debug questions before Step 3.")


if __name__ == "__main__":
    main()
