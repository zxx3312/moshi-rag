"""Build gold unit records from hand annotations and validate them (standard library only).

Evidence IDs are "d<N>s<M>": N is the 1-based document position in the sample's context
(the "Document N" numbering in samples_debug_readable.md) and M is the 0-based sentence index.
Traces must use the same IDs.
"""

import argparse
import json
from pathlib import Path


SCHEMA_VERSION = "1.0"
DATA_VERSION = "debug-v0"
HERE = Path(__file__).resolve().parent
# Source dataset type -> unit-construction type (schema.md 4.3), using the names in A's
# decompose.py QUESTION_TYPES so that gold and controller decompositions can be compared.
QUESTION_TYPES = {
    "bridge": "bridge",
    "compositional": "bridge",
    "inference": "bridge",
    "comparison": "comparison",
    "bridge_comparison": "bridge_comparison",
    "custom_multipart": "multipart",
}


def evidence_id(doc_number, sentence_index):
    return "d" + str(doc_number) + "s" + str(sentence_index)


def resolve(sample, title, sentence_index):
    matches = [n for n, (name, _) in enumerate(sample["context"], start=1) if name == title]
    if len(matches) != 1:
        raise ValueError(sample["sample_id"] + ": title must match exactly one document: " + title)
    sentences = sample["context"][matches[0] - 1][1]
    if not isinstance(sentence_index, int) or not 0 <= sentence_index < len(sentences):
        raise ValueError(sample["sample_id"] + ": sentence index out of range: " + title + " " + str(sentence_index))
    return evidence_id(matches[0], sentence_index), sentences[sentence_index].strip()


def has_cycle(units):
    graph = {unit["unit_id"]: unit["depends_on"] for unit in units}
    state = {}

    def visit(node):
        if state.get(node) == "active":
            return True
        if state.get(node) == "done":
            return False
        state[node] = "active"
        found = any(visit(parent) for parent in graph[node])
        state[node] = "done"
        return found

    return any(visit(node) for node in graph)


def validate(record):
    sample_id = record["sample_id"]
    units = record["units"]
    ids = [unit["unit_id"] for unit in units]
    if len(ids) != len(set(ids)):
        raise ValueError(sample_id + ": duplicate unit_id")
    if not any(unit["necessary"] is True for unit in units):
        raise ValueError(sample_id + ": no necessary unit")
    for unit in units:
        where = sample_id + " " + unit["unit_id"]
        if not isinstance(unit.get("expected_answer"), str) or not unit["expected_answer"].strip():
            raise ValueError(where + ": empty expected_answer")
        if not isinstance(unit.get("necessary"), bool):
            raise ValueError(where + ": necessary must be boolean")
        if not isinstance(unit.get("by_omission", False), bool):
            raise ValueError(where + ": by_omission must be boolean")
        aliases = unit.get("aliases", [])
        if not isinstance(aliases, list) or not all(isinstance(a, str) and a.strip() for a in aliases):
            raise ValueError(where + ": aliases must be nonempty strings")
        for parent in unit["depends_on"]:
            if parent not in ids or parent == unit["unit_id"]:
                raise ValueError(where + ": invalid dependency " + parent)
        sets = unit["support_sets"]
        if sets == []:
            raise ValueError(where + ": support_sets [] is not allowed on an answerable unit")
        if any(len(inner) == 0 for inner in sets):
            if sets != [[]]:
                raise ValueError(where + ": an empty support set must be the only set, written [[]]")
            if not unit["depends_on"]:
                raise ValueError(where + ": [[]] requires a nonempty depends_on")
    if has_cycle(units):
        raise ValueError(sample_id + ": dependency cycle")
    necessary = [unit for unit in units if unit["necessary"]]
    kind = record["question_type"]
    if kind == "multipart" and (len(necessary) != len(units) or any(unit["depends_on"] for unit in units)):
        raise ValueError(sample_id + ": multipart units must all be necessary with no dependencies")
    if kind in ("single", "bridge", "comparison", "bridge_comparison") and len(necessary) != 1:
        raise ValueError(sample_id + ": " + kind + " needs exactly one necessary unit")
    if kind == "bridge" and len(units) > 1 and not necessary[0]["depends_on"]:
        raise ValueError(sample_id + ": the final bridge hop must depend on an earlier hop")
    if kind in ("comparison", "bridge_comparison") and necessary[0]["support_sets"] != [[]]:
        raise ValueError(sample_id + ": the comparison conclusion must have support_sets [[]]")


def build(sample, annotation):
    units = []
    texts = {}
    for unit in annotation["units"]:
        sets = []
        for inner in unit["support_sets"]:
            ids = []
            for title, index in inner:
                eid, text = resolve(sample, title, index)
                ids.append(eid)
                texts[eid] = (title, index, text)
            sets.append(ids)
        result = {
            "unit_id": unit["unit_id"],
            "description": unit["description"],
            "necessary": unit["necessary"],
            "expected_answer": unit["expected_answer"],
            "depends_on": unit["depends_on"],
            "support_sets": sets,
        }
        if unit.get("aliases", []) != []:
            result["aliases"] = unit["aliases"]
        if unit.get("by_omission", False) is not False:
            result["by_omission"] = unit["by_omission"]
        units.append(result)
    if sample["type"] not in QUESTION_TYPES:
        raise ValueError(sample["sample_id"] + ": no question_type for source type " + sample["type"])
    record = {"schema_version": SCHEMA_VERSION, "data_version": DATA_VERSION,
              "sample_id": sample["sample_id"], "question_type": QUESTION_TYPES[sample["type"]],
              "source_type": sample["type"], "units": units}
    validate(record)
    return record, texts


def review_section(number, sample, annotation, record, texts):
    lines = ["## Q" + str(number) + " — `" + sample["sample_id"] + "` (" + annotation["status"] + ")", "",
             "> " + sample["question"], "", "Source answer: " + sample["answer"], "",
             "Question type: `" + record["question_type"] + "` (source type `" + record["source_type"] + "`)", "",
             "| Unit | Necessary | Expected answer | Depends on | Support sets |", "|---|---|---|---|---|"]
    for unit in record["units"]:
        answer = unit["expected_answer"]
        if unit.get("aliases"):
            answer += " (aliases: " + "; ".join(unit["aliases"]) + ")"
        if unit.get("by_omission"):
            answer += " **[by_omission]**"
        if unit["support_sets"] == [[]]:
            sets = "`[[]]`: no extra evidence, supported when dependencies are"
        else:
            sets = " OR ".join("[" + ", ".join(inner) + "]" for inner in unit["support_sets"])
        lines.append("| " + unit["unit_id"] + ": " + unit["description"] + " | " + str(unit["necessary"]).lower()
                     + " | " + answer + " | " + (", ".join(unit["depends_on"]) or "—") + " | " + sets + " |")
    lines += ["", "Evidence:", ""]
    for eid in sorted(texts, key=lambda e: [int(x) for x in e[1:].split("s")]):
        title, index, text = texts[eid]
        lines.append("- `" + eid + "` " + title + " [" + str(index) + "]: " + text)
    lines += ["", "Notes:", ""] + ["- " + note for note in annotation["notes"]] + [""]
    return lines


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--samples", type=Path, default=HERE.parent / "step2" / "prepared" / "samples_debug.jsonl")
    parser.add_argument("--annotations", type=Path, default=HERE / "gold_annotations.json")
    parser.add_argument("--out", type=Path, default=HERE / "gold_debug.jsonl")
    parser.add_argument("--review", type=Path, default=HERE / "gold_review.md")
    args = parser.parse_args()

    with args.samples.open("r", encoding="utf-8") as file:
        samples = [json.loads(line) for line in file]
    with args.annotations.open("r", encoding="utf-8") as file:
        annotations = json.load(file)
    if annotations["data_version"] != DATA_VERSION or annotations["schema_version"] != SCHEMA_VERSION:
        raise ValueError("Annotation versions do not match " + SCHEMA_VERSION + " / " + DATA_VERSION)
    by_id = {}
    for annotation in annotations["records"]:
        if annotation["sample_id"] in by_id:
            raise ValueError("Duplicate annotation: " + annotation["sample_id"])
        by_id[annotation["sample_id"]] = annotation
    unknown = set(by_id) - {sample["sample_id"] for sample in samples}
    if unknown:
        raise ValueError("Annotations for unknown samples: " + ", ".join(sorted(unknown)))

    records = []
    sections = []
    for number, sample in enumerate(samples, start=1):
        annotation = by_id.get(sample["sample_id"])
        if annotation is None:
            continue
        record, texts = build(sample, annotation)
        records.append(record)
        sections += review_section(number, sample, annotation, record, texts)
    counts = {}
    for record in records:
        key = (record["question_type"], record["source_type"])
        counts[key] = counts.get(key, 0) + 1
    review = ["# Gold Units — Review Copy", "",
              "Generated by `build_gold.py` from `gold_annotations.json`. Do not edit by hand.", "",
              "| question_type | source_type | Questions |", "|---|---|---:|"]
    review += ["| " + kind + " | " + source + " | " + str(count) + " |" for (kind, source), count in sorted(counts.items())]
    review += ["| **Total** | | **" + str(len(records)) + "** |", ""] + sections

    with args.out.open("w", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False) + "\n")
    args.review.write_text("\n".join(review), encoding="utf-8")
    pending = [a["sample_id"] for a in annotations["records"] if a["status"] != "draft"]
    print("Annotated " + str(len(records)) + "/" + str(len(samples)) + " samples; wrote " + str(args.out))
    if pending:
        print("Not draft status: " + ", ".join(pending))


if __name__ == "__main__":
    main()
