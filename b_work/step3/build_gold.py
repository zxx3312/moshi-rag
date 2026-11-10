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


#-------------#
# Updated: show unfinished support only when reviewing saved drafts.
# Normal gold generation still needs accepted support.
#-------------#
def validate(record, allow_unresolved=False):
    """Check gold structure. Only saved draft reviews may keep empty support."""
    sample_id = record["sample_id"]
    units = record["units"]
    # Keep Step3 units within the original support/dependency fields.
    allowed_fields = {"unit_id", "description", "necessary", "expected_answer", "depends_on",
                      "support_sets", "aliases", "by_omission", "by_presupposition"}
    ids = [unit["unit_id"] for unit in units]
    if len(ids) != len(set(ids)):
        raise ValueError(sample_id + ": duplicate unit_id")
    if not any(unit["necessary"] is True for unit in units):
        raise ValueError(sample_id + ": no necessary unit")
    for unit in units:
        where = sample_id + " " + unit["unit_id"]
        if set(unit) - allowed_fields:
            raise ValueError(where + ": unsupported gold unit fields")
        if not isinstance(unit.get("expected_answer"), str) or not unit["expected_answer"].strip():
            raise ValueError(where + ": empty expected_answer")
        if not isinstance(unit.get("necessary"), bool):
            raise ValueError(where + ": necessary must be boolean")
        if not isinstance(unit.get("by_omission", False), bool):
            raise ValueError(where + ": by_omission must be boolean")
        if not isinstance(unit.get("by_presupposition", False), bool):
            raise ValueError(where + ": by_presupposition must be boolean")
        aliases = unit.get("aliases", [])
        if not isinstance(aliases, list) or not all(isinstance(a, str) and a.strip() for a in aliases):
            raise ValueError(where + ": aliases must be nonempty strings")
        for parent in unit["depends_on"]:
            if parent not in ids or parent == unit["unit_id"]:
                raise ValueError(where + ": invalid dependency " + parent)
        sets = unit["support_sets"]
        # Empty support may stay in a draft review, but not in a normal gold build.
        if sets == [] and not allow_unresolved:
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
    # Only known question types have a defined unit structure.
    if kind not in {"single", "bridge", "comparison", "bridge_comparison", "multipart"}:
        raise ValueError(sample_id + ": unknown question type")
    if kind == "multipart" and (len(necessary) != len(units) or any(unit["depends_on"] for unit in units)):
        raise ValueError(sample_id + ": multipart units must all be necessary with no dependencies")
    if kind in ("single", "bridge", "comparison", "bridge_comparison") and len(necessary) != 1:
        raise ValueError(sample_id + ": " + kind + " needs exactly one necessary unit")
    if kind == "bridge" and len(units) > 1 and not necessary[0]["depends_on"]:
        raise ValueError(sample_id + ": the final bridge hop must depend on an earlier hop")
    # A saved draft may still have an unfinished comparison answer.
    allowed_sets = ([[]], []) if allow_unresolved else ([[]],)
    if kind in ("comparison", "bridge_comparison") and necessary[0]["support_sets"] not in allowed_sets:
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
        if unit.get("by_presupposition", False) is not False:
            result["by_presupposition"] = unit["by_presupposition"]
        units.append(result)
    if sample["type"] not in QUESTION_TYPES:
        raise ValueError(sample["sample_id"] + ": no question_type for source type " + sample["type"])
    record = {"schema_version": SCHEMA_VERSION, "data_version": DATA_VERSION,
              "sample_id": sample["sample_id"], "question_type": QUESTION_TYPES[sample["type"]],
              "source_type": sample["type"], "units": units}
    validate(record)
    return record, texts


#-------------#
# Added: collect source text for saved-gold reviews.
def source_texts(sample):
    """Keep every source sentence under its original evidence ID."""
    return {evidence_id(number, index): (title, index, text.strip())
            for number, (title, sentences) in enumerate(sample["context"], start=1)
            for index, text in enumerate(sentences)}
#-------------#


#-------------#
# Added: use the same evidence IDs when comparing the two files.
def normalized_units(sample, units, available):
    """Compare saved gold with annotations that use IDs or title/index pairs."""
    result = []
    for unit in units:
        # Work on a copy so the input annotation stays unchanged.
        item = dict(unit)
        sets = []
        for inner in item["support_sets"]:
            ids = []
            for reference in inner:
                if isinstance(reference, str):
                    # New annotations already use IDs such as d1s0.
                    eid = reference
                else:
                    # Older annotations use a document title and sentence number.
                    title, index = reference
                    eid, _ = resolve(sample, title, index)
                if eid not in available:
                    raise ValueError(sample["sample_id"] + ": unknown evidence ID " + eid)
                ids.append(eid)
            sets.append(ids)
        item["support_sets"] = sets
        # Treat missing and empty optional fields as the same value.
        for field in ("aliases", "by_omission", "by_presupposition"):
            if not item.get(field):
                item.pop(field, None)
        result.append(item)
    return result
#-------------#


#-------------#
# Added: check saved gold before writing its review.
def saved_review_texts(sample, annotation, record, versions):
    """Check saved draft inputs without approving or rewriting their gold."""
    for field in ("schema_version", "data_version"):
        if record.get(field) != versions[field]:
            raise ValueError(sample["sample_id"] + ": saved gold version mismatch: " + field)
    if record.get("source_type") != sample["type"]:
        raise ValueError(sample["sample_id"] + ": saved gold source type mismatch")
    if annotation.get("question_type", record["question_type"]) != record["question_type"]:
        raise ValueError(sample["sample_id"] + ": saved gold question type mismatch")
    # Keep unfinished draft units visible. This does not approve their answers.
    validate(record, allow_unresolved=True)
    available = source_texts(sample)
    # Stop if annotations changed but the saved gold was not updated.
    if normalized_units(sample, annotation["units"], available) != normalized_units(sample, record["units"], available):
        raise ValueError(sample["sample_id"] + ": gold units differ from annotations; update gold before rebuilding its review")
    # Question-based reasoning uses the same support sets and required facts.
    cited = {eid for unit in record["units"] for inner in unit["support_sets"] for eid in inner}
    return {eid: available[eid] for eid in cited}
#-------------#


#-------------#
# Added: explain each support-list form in the review table.
def support_text(sets):
    """Show an empty draft support list clearly, rather than leaving a blank cell."""
    if sets == []:
        return "`[]`: no accepted support"
    if sets == [[]]:
        return "`[[]]`: no extra evidence, supported when dependencies are"
    return " OR ".join("[" + ", ".join(inner) + "]" for inner in sets)
#-------------#


#-------------#
# Added: keep special characters from breaking a table row.
def table_cell(value):
    """Keep a unit's text inside one readable Markdown table cell."""
    # A | must not start a new column. Show new lines with <br>.
    return value.replace("|", "\\|").replace("\n", "<br>")
#-------------#


def review_section(number, sample, annotation, record, texts):
    """Show units, cited evidence, notes, and every source sentence."""
    #-------------#
    # Updated: show all unit fields needed for a human review.
    lines = ["## Q" + str(number) + " — `" + sample["sample_id"] + "` (" + annotation["status"] + ")", "",
             "> " + sample["question"].rstrip(), "", "Source answer: " + sample["answer"], "",
             "Question type: `" + record["question_type"] + "` (source type `" + record["source_type"] + "`)", "",
             "| Unit | Necessary | Expected answer | Depends on | Support sets |",
             "|---|---|---|---|---|"]
    for unit in record["units"]:
        answer = unit["expected_answer"]
        if unit.get("aliases"):
            answer += " (aliases: " + "; ".join(unit["aliases"]) + ")"
        if unit.get("by_omission"):
            answer += " **[by_omission]**"
        if unit.get("by_presupposition"):
            answer += " **[by_presupposition]**"
        cells = [unit["unit_id"] + ": " + unit["description"], str(unit["necessary"]).lower(), answer,
                 ", ".join(unit["depends_on"]) or "—", support_text(unit["support_sets"])]
        lines.append("| " + " | ".join(table_cell(cell) for cell in cells) + " |")
    #-------------#
    lines += ["", "Evidence:", ""]
    for eid in sorted(texts, key=lambda e: [int(x) for x in e[1:].split("s")]):
        title, index, text = texts[eid]
        lines.append(("- `" + eid + "` " + title + " [" + str(index) + "]: " + text).rstrip())
    #-------------#
    # Added: keep existing source issues in Notes, without a second review stage.
    notes = list(annotation.get("notes", []))
    notes += ["Source check: `" + flag + "`." for flag in annotation.get("review_flags", [])]
    lines += ["", "Notes:", ""] + ["- " + note for note in notes] + [""]
    #-------------#

    #-------------#
    # Added: let the reader open the full context, including uncited sentences.
    lines += ["<details><summary>All source context</summary>", ""]
    # Keep original document positions so context IDs match the gold evidence IDs.
    for document_number, (title, sentences) in enumerate(sample["context"], start=1):
        for index, text in enumerate(sentences):
            eid = evidence_id(document_number, index)
            lines.append(("- `" + eid + "` " + title + " [" + str(index) + "]: " + text.strip()).rstrip())
    lines += ["", "</details>", ""]
    #-------------#
    return lines


def main():
    """Build debug gold, or rebuild only a review from saved gold drafts."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--samples", type=Path, default=HERE.parent / "step2" / "prepared" / "samples_debug.jsonl")
    parser.add_argument("--annotations", type=Path, default=HERE / "gold_annotations.json")
    parser.add_argument("--out", type=Path, default=HERE / "gold_debug.jsonl")
    parser.add_argument("--review", type=Path, default=HERE / "gold_review.md")
    #-------------#
    # Added: choose saved gold when only the review needs to be rebuilt.
    parser.add_argument("--review-from-gold", type=Path,
                        help="Read existing gold and write only the review; do not write --out.")
    #-------------#
    args = parser.parse_args()

    #-------------#
    # Added: protect source, annotation, and gold files from being overwritten.
    inputs = [args.samples, args.annotations]
    if args.review_from_gold:
        inputs.append(args.review_from_gold)
    if args.review.resolve() in {path.resolve() for path in inputs}:
        parser.error("Review output must not overwrite an input file")
    #-------------#

    with args.samples.open("r", encoding="utf-8") as file:
        samples = [json.loads(line) for line in file]
    with args.annotations.open("r", encoding="utf-8") as file:
        annotations = json.load(file)
    #-------------#
    # Updated: saved reviews may use a data version other than debug-v0.
    # The saved gold must still match that version when each question is checked.
    if annotations["schema_version"] != SCHEMA_VERSION or (
            not args.review_from_gold and annotations["data_version"] != DATA_VERSION):
        raise ValueError("Annotation versions do not match " + SCHEMA_VERSION + " / " + DATA_VERSION)
    #-------------#
    by_id = {}
    for annotation in annotations["records"]:
        if annotation["sample_id"] in by_id:
            raise ValueError("Duplicate annotation: " + annotation["sample_id"])
        by_id[annotation["sample_id"]] = annotation
    unknown = set(by_id) - {sample["sample_id"] for sample in samples}
    if unknown:
        raise ValueError("Annotations for unknown samples: " + ", ".join(sorted(unknown)))

    #-------------#
    # Added: load saved gold as input. Do not change the file.
    saved_gold = {}
    if args.review_from_gold:
        with args.review_from_gold.open("r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue
                record = json.loads(line)
                sid = record["sample_id"]
                if sid in saved_gold:
                    raise ValueError("Duplicate saved gold: " + sid)
                saved_gold[sid] = record
        if set(saved_gold) != set(by_id):
            raise ValueError("Saved gold and annotations must have the same sample IDs")
    #-------------#

    records = []
    sections = []
    for number, sample in enumerate(samples, start=1):
        annotation = by_id.get(sample["sample_id"])
        if annotation is None:
            continue
        #-------------#
        # Added: reuse saved units, or run the normal gold build.
        if args.review_from_gold:
            record = saved_gold[sample["sample_id"]]
            texts = saved_review_texts(sample, annotation, record, annotations)
        else:
            record, texts = build(sample, annotation)
        #-------------#
        records.append(record)
        sections += review_section(number, sample, annotation, record, texts)
    counts = {}
    for record in records:
        key = (record["question_type"], record["source_type"])
        counts[key] = counts.get(key, 0) + 1
    #-------------#
    # Updated: tell the reader which inputs were used for this review.
    origin = ("saved gold and annotations" if args.review_from_gold else "annotations")
    review = ["# Gold Units — Review Copy", "",
              "Generated by `build_gold.py` from " + origin + ".", "",
              "Edit annotations for data changes. Keep review comments when rebuilding this file.", "",
              "| question_type | source_type | Questions |", "|---|---|---:|"]
    #-------------#
    review += ["| " + kind + " | " + source + " | " + str(count) + " |" for (kind, source), count in sorted(counts.items())]
    review += ["| **Total** | | **" + str(len(records)) + "** |", ""] + sections

    #-------------#
    # Added: write gold only in normal build mode. Review-only mode skips this.
    if not args.review_from_gold:
        with args.out.open("w", encoding="utf-8") as file:
            for record in records:
                file.write(json.dumps(record, ensure_ascii=False) + "\n")
    #-------------#
    # Write the review only after all input checks have passed.
    args.review.write_text("\n".join(review), encoding="utf-8")
    pending = [a["sample_id"] for a in annotations["records"] if a["status"] != "draft"]
    #-------------#
    # Added: show whether this run wrote only a review or also built gold.
    if args.review_from_gold:
        print("Review copy: " + str(len(records)) + " samples; wrote " + str(args.review) + "; gold unchanged")
    else:
        print("Annotated " + str(len(records)) + "/" + str(len(samples)) + " samples; wrote " + str(args.out))
    #-------------#
    if pending:
        print("Not draft status: " + ", ".join(pending))


if __name__ == "__main__":
    main()
