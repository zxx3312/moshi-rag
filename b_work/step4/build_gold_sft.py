"""Build judge-SFT gold records from annotations and validate them (standard library only).

Same annotation format and evidence IDs as b_work/step3/build_gold.py, plus the support-set representation
needed to schedule the schema v1.3 `by_presupposition` rule (a_work/unit_schema.md 5.6):

- presupposition_sets: support sets, in the same [title, index] form, that support the unit only
  when the question's premise is taken as given. Such a unit is SUPPORTED by_presupposition when one of
  these sets is visible and at least one of its depends_on units is SUPPORTED (or it has none). Every
  unit using this representation must also carry the static gold flag by_presupposition: true.
- support_sets []: no context sentence states the unit's value (e.g. Nin's non-win). The unit can
  only be SUPPORTED through presupposition_sets, or never.

Records with status "reject" are skipped. The final question list takes each dataset's primary
candidates that are not rejected and fills each rejected slot with the next annotated reserve.
"""

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "step3"))
from build_gold import QUESTION_TYPES, SCHEMA_VERSION, has_cycle, resolve  # noqa: E402

DATA_VERSION = "sft-v0"
STATUSES = ("draft", "reviewed", "reject")
UNIT_KEYS = {"unit_id", "description", "necessary", "expected_answer", "aliases", "depends_on",
             "support_sets", "presupposition_sets", "by_omission", "by_presupposition"}


def norm(text):
    return " ".join(re.findall(r"\w+", (text or "").casefold()))


def check(condition, where, message):
    if not condition:
        raise ValueError(where + ": " + message)


def resolve_sets(sample, sets, texts):
    result = []
    for inner in sets:
        ids = []
        for title, index in inner:
            eid, text = resolve(sample, title, index)
            ids.append(eid)
            texts[eid] = (title, index, text)
        result.append(ids)
    return result


def supported_when_all_visible(units):
    """Unit IDs that become SUPPORTED once every context sentence is visible."""
    by_id = {u["unit_id"]: u for u in units}
    done = {}

    def visit(uid):
        if uid not in done:
            unit = by_id[uid]
            parents = [visit(p) for p in unit["depends_on"]]
            explicit = bool(unit["support_sets"]) and all(parents)
            presupposed = bool(unit.get("presupposition_sets")) and (any(parents) or not parents)
            done[uid] = explicit or presupposed
        return done[uid]

    return {uid for uid in by_id if visit(uid)}


def validate(record, question):
    sample_id = record["sample_id"]
    units = record["units"]
    ids = [u["unit_id"] for u in units]
    check(len(ids) == len(set(ids)), sample_id, "duplicate unit_id")
    check(any(u["necessary"] is True for u in units), sample_id, "no necessary unit")
    question_norm = norm(question)
    for unit in units:
        where = sample_id + " " + unit["unit_id"]
        check(not set(unit) - UNIT_KEYS, where, "unknown fields " + str(sorted(set(unit) - UNIT_KEYS)))
        check(isinstance(unit.get("description"), str) and unit["description"].strip(), where, "empty description")
        check(isinstance(unit.get("expected_answer"), str) and unit["expected_answer"].strip(), where, "empty expected_answer")
        check(isinstance(unit.get("necessary"), bool), where, "necessary must be boolean")
        check(isinstance(unit.get("by_omission", False), bool), where, "by_omission must be boolean")
        check(isinstance(unit.get("by_presupposition", False), bool), where,
              "by_presupposition must be boolean")
        aliases = unit.get("aliases", [])
        check(isinstance(aliases, list) and all(isinstance(a, str) and a.strip() for a in aliases), where, "bad aliases")
        for parent in unit["depends_on"]:
            check(parent in ids and parent != unit["unit_id"], where, "invalid dependency " + parent)
        for placeholder in re.findall(r"\{(u\d+)\}", unit["description"]):
            check(placeholder in unit["depends_on"], where, "placeholder {" + placeholder + "} is not in depends_on")
        # The description is judge input: it may not reveal an answer the question does not contain.
        answer = norm(unit["expected_answer"])
        if answer not in ("yes", "no") and len(answer) > 2 and answer not in question_norm:
            check(answer not in norm(unit["description"]), where, "description reveals the expected answer")
        sets = unit["support_sets"]
        if any(len(inner) == 0 for inner in sets):
            check(sets == [[]], where, "an empty support set must be the only set, written [[]]")
            check(bool(unit["depends_on"]), where, "[[]] requires a nonempty depends_on")
        presupposed = unit.get("presupposition_sets", [])
        check(isinstance(presupposed, list) and all(inner for inner in presupposed), where,
              "presupposition_sets must be a list of nonempty sets")
        check(not presupposed or unit.get("by_presupposition") is True, where,
              "presupposition_sets requires by_presupposition true")
        check(not (unit.get("by_omission") and not sets), where, "by_omission needs a support set")
    check(not has_cycle(units), sample_id, "dependency cycle")
    necessary = [u for u in units if u["necessary"]]
    kind = record["question_type"]
    if kind in ("bridge", "comparison", "bridge_comparison"):
        check(len(necessary) == 1, sample_id, kind + " needs exactly one necessary unit")
    if kind == "bridge" and len(units) > 1:
        check(bool(necessary[0]["depends_on"]), sample_id, "the final bridge hop must depend on an earlier hop")
    if kind in ("comparison", "bridge_comparison"):
        check(necessary[0]["support_sets"] == [[]], sample_id, "the comparison conclusion must have support_sets [[]]")


def build(sample, annotation):
    texts = {}
    units = []
    for unit in annotation["units"]:
        result = {key: unit[key] for key in ["unit_id", "description", "necessary", "expected_answer", "depends_on"]}
        result["support_sets"] = resolve_sets(sample, unit["support_sets"], texts)
        if unit.get("aliases"):
            result["aliases"] = unit["aliases"]
        if unit.get("by_omission"):
            result["by_omission"] = True
        if unit.get("by_presupposition"):
            result["by_presupposition"] = True
        if unit.get("presupposition_sets"):
            result["presupposition_sets"] = resolve_sets(sample, unit["presupposition_sets"], texts)
        units.append(result)
    check(sample["type"] in QUESTION_TYPES, sample["sample_id"], "no question_type for " + sample["type"])
    record = {"schema_version": SCHEMA_VERSION, "data_version": DATA_VERSION, "sample_id": sample["sample_id"],
              "question_type": QUESTION_TYPES[sample["type"]], "source_type": sample["type"], "units": units}
    validate(record, sample["question"])
    return record, texts


def select(candidates, annotations):
    """Primary questions that are not rejected, with rejected slots filled by reserves.

    A rejected primary may name an explicit ``replacement_sample_id`` in its annotation.  The
    replacement must be an accepted reserve from the same project split. Dataset and source type are
    normally preserved, but an explicit mapping may cross them when the remaining same-category
    candidates fail review; the final composition is reported by the build.
    Remaining rejected slots are filled by annotated reserves in rank order, as before.
    """
    chosen, missing = [], Counter()
    explicit_ids_global = set()
    by_id = {c["sample_id"]: c for c in candidates}
    for dataset in sorted({c["dataset"] for c in candidates}):
        rows = sorted((c for c in candidates if c["dataset"] == dataset), key=lambda c: c["candidate_rank"])
        primary = [c for c in rows if c["candidate_role"] == "primary"]
        reserves = [c for c in rows if c["candidate_role"] == "reserve"]
        accepted = [c for c in primary if c["sample_id"] in annotations and annotations[c["sample_id"]]["status"] != "reject"]
        unannotated = [c for c in primary if c["sample_id"] not in annotations]
        explicit = []
        for source in primary:
            annotation = annotations.get(source["sample_id"], {})
            replacement_id = annotation.get("replacement_sample_id")
            if replacement_id is None:
                continue
            check(annotation.get("status") == "reject", source["sample_id"],
                  "only a rejected question may name replacement_sample_id")
            check(replacement_id in by_id, source["sample_id"], "unknown replacement " + replacement_id)
            replacement = by_id[replacement_id]
            check(replacement["candidate_role"] == "reserve", source["sample_id"],
                  "replacement must be a reserve question")
            check(replacement["project_split"] == source["project_split"], source["sample_id"],
                  "replacement must keep project_split")
            replacement_annotation = annotations.get(replacement_id)
            check(replacement_annotation is not None and replacement_annotation["status"] != "reject",
                  source["sample_id"], "replacement is unannotated or rejected: " + replacement_id)
            check(replacement_id not in explicit_ids_global, source["sample_id"],
                  "replacement selected twice: " + replacement_id)
            explicit.append(replacement)
            explicit_ids_global.add(replacement_id)
        accepted += explicit
        explicit_ids = {c["sample_id"] for c in explicit}
        needed = len(primary) - len(accepted) - len(unannotated)
        for reserve in reserves:
            if needed == 0:
                break
            if reserve["sample_id"] in explicit_ids:
                continue
            annotation = annotations.get(reserve["sample_id"])
            if annotation is None:
                break  # reserves are used strictly in rank order
            if annotation["status"] != "reject":
                accepted.append(reserve)
                needed -= 1
        missing[dataset] = needed + len(unannotated)
        chosen += accepted
    return chosen, missing


def review_section(sample, annotation, record, texts):
    lines = ["## `" + sample["sample_id"] + "` (" + annotation["status"] + ", " + sample["project_split"] + ")", "",
             "> " + sample["question"], "", "Source answer: " + sample["answer"] + " · type `" + sample["type"] + "`", ""]
    lines += ["| Unit | Necessary | Answer | Depends on | Support | Presupposition |", "|---|---|---|---|---|---|"]
    for unit in record["units"]:
        answer = unit["expected_answer"] + (" **[by_omission]**" if unit.get("by_omission") else "")
        lines.append("| " + unit["unit_id"] + ": " + unit["description"] + " | " + str(unit["necessary"]).lower() + " | "
                     + answer + " | " + (", ".join(unit["depends_on"]) or "—") + " | "
                     + " or ".join("[" + ", ".join(s) + "]" for s in unit["support_sets"]) + " | "
                     + " or ".join("[" + ", ".join(s) + "]" for s in unit.get("presupposition_sets", [])) + " |")
    lines += [""] + ["- `" + eid + "` (" + title + ", " + str(index) + "): " + text
                     for eid, (title, index, text) in sorted(texts.items())]
    lines += [""] + ["- Note: " + note for note in annotation.get("notes", [])] + [""]
    return lines


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates", type=Path, default=HERE / "prepared" / "samples_sft_candidates.jsonl")
    parser.add_argument("--annotations", type=Path, nargs="+", default=[HERE / "gold_annotations_sft.json"])
    parser.add_argument("--out", type=Path, default=HERE / "gold_sft.jsonl")
    parser.add_argument("--review", type=Path, default=HERE / "gold_sft_review.md")
    parser.add_argument("--check-only", action="store_true", help="validate the given annotations; write nothing")
    args = parser.parse_args()

    samples = {json.loads(line)["sample_id"]: json.loads(line)
               for line in args.candidates.read_text(encoding="utf-8").splitlines()}
    annotations = {}
    for path in args.annotations:
        for annotation in json.loads(path.read_text(encoding="utf-8"))["records"]:
            sample_id = annotation["sample_id"]
            check(sample_id in samples, sample_id, "not a candidate question")
            check(sample_id not in annotations, sample_id, "annotated twice")
            check(annotation.get("status") in STATUSES, sample_id, "status must be one of " + str(STATUSES))
            if annotation["status"] == "reject":
                check(bool(annotation.get("notes")), sample_id, "a rejected question needs a reason in notes")
            if "replacement_sample_id" in annotation:
                check(isinstance(annotation["replacement_sample_id"], str) and annotation["replacement_sample_id"],
                      sample_id, "replacement_sample_id must be a nonempty string")
            annotations[sample_id] = annotation

    built, errors = {}, []
    for sample_id, annotation in annotations.items():
        if annotation["status"] == "reject":
            continue
        try:
            built[sample_id] = build(samples[sample_id], annotation)
        except (ValueError, KeyError, TypeError) as error:
            errors.append(repr(error))
    statuses = Counter(a["status"] for a in annotations.values())
    unanswerable = [s for s, (r, _) in built.items()
                    if not {u["unit_id"] for u in r["units"] if u["necessary"]} <= supported_when_all_visible(r["units"])]
    print("annotations: " + json.dumps(dict(statuses)) + "; errors: " + str(len(errors))
          + "; necessary unit unreachable with all evidence: " + str(len(unanswerable)))
    for error in errors:
        print("  " + error)
    if errors:
        sys.exit(1)
    if args.check_only:
        return

    chosen, missing = select(list(samples.values()), annotations)
    if any(missing.values()):
        sys.exit("Not enough accepted questions; annotate more candidates: " + json.dumps(dict(missing)))
    chosen.sort(key=lambda c: c["sample_id"])
    with args.out.open("w", encoding="utf-8") as file:
        for sample in chosen:
            file.write(json.dumps(built[sample["sample_id"]][0], ensure_ascii=False) + "\n")
    lines = ["# Judge-SFT Gold Review", "",
             "Generated by `build_gold_sft.py`. Do not edit by hand. " + str(len(chosen)) + " questions; "
             + "necessary unit unreachable with all evidence: " + str(sum(c["sample_id"] in unanswerable for c in chosen)) + ".", ""]
    for sample in chosen:
        record, texts = built[sample["sample_id"]]
        lines += review_section(sample, annotations[sample["sample_id"]], record, texts)
    args.review.write_text("\n".join(lines), encoding="utf-8")
    print("wrote " + str(len(chosen)) + " gold records: " + json.dumps(dict(Counter(c["dataset"] + "/" + c["project_split"] for c in chosen))))


if __name__ == "__main__":
    main()
