"""Build full-context controlled mock traces (standard library only).

Every context sentence becomes one event with evidence ID "d<N>s<M>" (same convention as
build_gold.py). Documents arrive whole, in batches. The documents cited by supporting_facts
are split in citation order: the first half arrives with batch 1, the rest with batch 2.
A document cited only as normal or premise support in gold arrives with the
supporting_facts document of the same unit. Other distractors alternate between the batches
in document order. Traces carry no gold fields; the scheduler may read gold, the model may not.
"""

import argparse
import json
import math
from pathlib import Path
import re

if __package__:
    from .build_gold import source_texts, validate as validate_gold
else:
    from build_gold import source_texts, validate as validate_gold


SCHEMA_VERSION = "1.0"
DATA_VERSION = "debug-v0"
HERE = Path(__file__).resolve().parent
# Provisional batch times in seconds after question end. Delay schedules are not frozen yet
# (experiment_config.json, pending_decisions); anchors follow the existing 0-8 s pilot sweep.
SCHEDULES = {
    "immediate": [0.0],
    "short": [1.0, 3.0],
    "long": [2.0, 8.0],
}
TRACE_KEYS = ["schema_version", "data_version", "sample_id", "trace_id", "question", "time_origin",
              "clock", "trace_type", "events", "retrieval_complete_time_s"]
EVENT_KEYS = {"evidence_id", "scheduled_time_s", "visible_time_s", "text", "source"}
SOURCE_KEYS = {"dataset", "document_id", "document_index", "sentence_index"}
SUPPORT_FIELDS = ("support_sets", "presupposition_sets")


#-------------#
# Added: use both support paths when scheduling and checking evidence.
def support_ids(record):
    """Read evidence IDs only. Gold answers never become trace fields."""
    return {eid for unit in record["units"] for field in SUPPORT_FIELDS
            for group in unit.get(field, []) for eid in group}


def number(value):
    """Accept finite times, but reject booleans and missing values."""
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def validate_schedules(schedules):
    """This scheduler supports one arrival batch or two ordered arrival batches."""
    if not isinstance(schedules, dict) or not schedules:
        raise ValueError("Schedules must be a nonempty object")
    for name, times in schedules.items():
        if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z0-9_-]+", name):
            raise ValueError("Schedule names may use letters, numbers, underscores, and hyphens")
        if not isinstance(times, list) or len(times) not in (1, 2):
            raise ValueError(name + ": use one or two arrival times")
        if not all(number(t) and t >= 0 for t in times) or times != sorted(times):
            raise ValueError(name + ": arrival times must be finite, ordered, and nonnegative")


def validate_pair(sample, record):
    """Check versions, gold structure, and every evidence reference before writing."""
    sid = sample["sample_id"]
    if record.get("sample_id") != sid:
        raise ValueError(sid + ": sample and gold IDs differ")
    for row in (sample, record):
        if row.get("schema_version") != SCHEMA_VERSION:
            raise ValueError(sid + ": unknown schema_version")
    version = record.get("data_version")
    if not isinstance(version, str) or not version.strip() or sample.get("data_version") != version:
        raise ValueError(sid + ": sample and gold data versions differ")
    if record.get("source_type") != sample.get("type"):
        raise ValueError(sid + ": sample and gold source types differ")
    if not isinstance(sample.get("question"), str) or not sample["question"].strip():
        raise ValueError(sid + ": question must be nonempty text")
    titles = [title for title, _ in sample["context"]]
    if len(titles) != len(set(titles)):
        raise ValueError(sid + ": duplicate document titles")
    available = source_texts(sample)
    if not available:
        raise ValueError(sid + ": no source sentences")
    for title, index in sample.get("supporting_facts", []):
        if title not in titles or type(index) is not int or not 0 <= index < len(sample["context"][titles.index(title)][1]):
            raise ValueError(sid + ": invalid supporting fact")
    validate_gold(record)
    missing = support_ids(record) - available.keys()
    if missing:
        raise ValueError(sid + ": unknown gold evidence ID: " + ", ".join(sorted(missing)))
#-------------#


def gold_documents(sample, record=None):
    """Keep source citation order, or use gold documents when source facts are absent."""
    titles = [title for title, _ in sample["context"]]
    order = []
    for title, _ in sample.get("supporting_facts", []):
        number = titles.index(title) + 1
        if number not in order:
            order.append(number)
    # Older debug ordering stays unchanged when supporting facts are available.
    if not order and record is not None:
        for unit in record["units"]:
            cited = {document_number(e) for field in SUPPORT_FIELDS for group in unit.get(field, []) for e in group}
            for number in sorted(cited):
                if number not in order:
                    order.append(number)
    return order


def document_number(evidence_id):
    """Read the original document position from a sentence ID."""
    return int(evidence_id[1:].split("s")[0])


def alternative_documents(gold, record):
    """Map each document cited only by a normal or premise set to a supporting-fact document
    of the same unit, so that the alternative arrives together with what it substitutes for."""
    result = {}
    if record is None:
        return result
    for unit in record["units"]:
        cited = sorted({document_number(e) for field in SUPPORT_FIELDS for inner in unit.get(field, []) for e in inner})
        anchors = [n for n in gold if n in cited]
        for number in cited:
            if number not in gold and number not in result:
                result[number] = anchors[0] if anchors else (gold[-1] if gold else cited[0])
    return result


def document_batches(sample, batch_count, record=None):
    """Keep each whole document in one batch, including alternate premise evidence."""
    if batch_count not in (1, 2):
        raise ValueError("Use one or two document batches")
    gold = gold_documents(sample, record)
    if batch_count == 1:
        return [list(range(1, len(sample["context"]) + 1))]
    first = (len(gold) + 1) // 2
    batches = [gold[:first], gold[first:]]
    alternatives = alternative_documents(gold, record)
    for number, anchor in alternatives.items():
        batches[0 if anchor in batches[0] else 1].append(number)
    distractors = [n for n in range(1, len(sample["context"]) + 1) if n not in gold and n not in alternatives]
    for position, number in enumerate(distractors):
        batches[position % 2].append(number)
    return [sorted(batch) for batch in batches]


def build_trace(sample, schedule, times, record=None):
    """Copy original evidence into a fixed public trace format, without gold fields."""
    validate_schedules({schedule: times})
    events = []
    for time, documents in zip(times, document_batches(sample, len(times), record)):
        for number in documents:
            title, sentences = sample["context"][number - 1]
            for index, text in enumerate(sentences):
                events.append({
                    "evidence_id": "d" + str(number) + "s" + str(index),
                    "scheduled_time_s": time,
                    "visible_time_s": time,
                    "text": text.strip(),
                    "source": {"dataset": sample["dataset"], "document_id": title,
                               "document_index": number, "sentence_index": index},
                })
    if not events:
        raise ValueError(sample["sample_id"] + ": no source sentences")
    return {
        "schema_version": SCHEMA_VERSION,
        "data_version": record["data_version"] if record is not None else sample.get("data_version", DATA_VERSION),
        "sample_id": sample["sample_id"],
        "trace_id": sample["sample_id"] + "_" + schedule,
        "question": sample["question"],
        "time_origin": "question_end",
        "clock": "simulated",
        "trace_type": "controlled_mock",
        "events": events,
        "retrieval_complete_time_s": max(event["visible_time_s"] for event in events),
    }


def validate(trace, sample):
    """Check the exact public fields, full source text, and whole-document timing."""
    where = trace["trace_id"]
    if list(trace) != TRACE_KEYS:
        raise ValueError(where + ": unexpected trace fields")
    if trace["sample_id"] != sample["sample_id"] or trace["question"] != sample["question"]:
        raise ValueError(where + ": sample ID or question differs")
    if trace["schema_version"] != SCHEMA_VERSION or trace["data_version"] != sample.get("data_version", DATA_VERSION):
        raise ValueError(where + ": trace version differs from sample")
    if trace["time_origin"] != "question_end" or trace["clock"] != "simulated" or trace["trace_type"] != "controlled_mock":
        raise ValueError(where + ": unexpected controlled trace settings")
    if not isinstance(trace["events"], list) or any(
            not isinstance(event, dict) or set(event) != EVENT_KEYS or
            not isinstance(event["source"], dict) or set(event["source"]) != SOURCE_KEYS
            for event in trace["events"]):
        raise ValueError(where + ": unexpected evidence or source fields")
    ids = [event["evidence_id"] for event in trace["events"]]
    if len(ids) != len(set(ids)):
        raise ValueError(where + ": duplicate evidence ID")
    available = source_texts(sample)
    if not ids or set(ids) != set(available):
        raise ValueError(where + ": not every context sentence is an event")
    times = [event["visible_time_s"] for event in trace["events"]]
    if not all(number(t) and t >= 0 for t in times) or times != sorted(times):
        raise ValueError(where + ": visibility times are not ordered and nonnegative")
    document_times = {}
    for event in trace["events"]:
        scheduled = event["scheduled_time_s"]
        if not number(scheduled) or scheduled < 0 or scheduled != event["visible_time_s"]:
            raise ValueError(where + ": controlled schedule and visible time must match")
        eid = event["evidence_id"]
        title, index, text = available[eid]
        document = document_number(eid)
        expected = {"dataset": sample["dataset"], "document_id": title,
                    "document_index": document, "sentence_index": index}
        if event["text"] != text or event["source"] != expected:
            raise ValueError(where + ": evidence text or source differs from the sample")
        timing = (scheduled, event["visible_time_s"])
        if document in document_times and document_times[document] != timing:
            raise ValueError(where + ": a document was split across arrival times")
        document_times[document] = timing
    if trace["retrieval_complete_time_s"] != max(times):
        raise ValueError(where + ": retrieval_complete_time_s is not the last arrival")


def supported_times(gold, trace):
    """Find earliest support through normal paths and question-premise paths."""
    visible = {event["evidence_id"]: event["visible_time_s"] for event in trace["events"]}
    units = {unit["unit_id"]: unit for unit in gold["units"]}
    result = {}

    def evidence_time(groups):
        """A whole group must arrive; any complete group is enough."""
        options = [max((visible[e] for e in group), default=0.0)
                   for group in groups if all(e in visible for e in group)]
        return min(options) if options else None

    def time_of(unit_id):
        """Normal paths wait for all parents; premise paths wait for any parent or none."""
        if unit_id not in result:
            unit = units[unit_id]
            own = evidence_time(unit["support_sets"])
            parents = [time_of(parent) for parent in unit["depends_on"]]
            options = []
            if own is not None and None not in parents:
                options.append(max([own] + parents))
            premise = evidence_time(unit.get("presupposition_sets", []))
            known_parents = [time for time in parents if time is not None]
            if premise is not None and (known_parents or not parents):
                options.append(max(premise, min(known_parents, default=0.0)))
            result[unit_id] = min(options) if options else None
        return result[unit_id]

    for unit_id in units:
        time_of(unit_id)
    return result


#-------------#
# Added: allow paired revision files without making another combined input copy.
def read_records(paths):
    """Read JSON objects and reject duplicate sample IDs across input files."""
    result = {}
    for path in paths:
        with path.open(encoding="utf-8") as file:
            for line_number, line in enumerate(file, 1):
                if not line.strip():
                    continue
                row = json.loads(line)
                if not isinstance(row, dict) or not isinstance(row.get("sample_id"), str) or not row["sample_id"].strip():
                    raise ValueError(str(path) + ":" + str(line_number) + ": missing sample_id")
                if row["sample_id"] in result:
                    raise ValueError("Duplicate sample ID: " + row["sample_id"])
                result[row["sample_id"]] = row
    return result
#-------------#


def main():
    """Check paired inputs, then write public traces and separate review/check files."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--samples", type=Path, nargs="+",
                        default=[HERE.parent / "step2" / "prepared" / "samples_debug.jsonl"])
    parser.add_argument("--gold", type=Path, nargs="+", default=[HERE / "gold_debug.jsonl"])
    parser.add_argument("--out", type=Path, default=HERE / "traces_debug.jsonl")
    parser.add_argument("--review", type=Path, default=HERE / "traces_review.md")
    parser.add_argument("--report", type=Path, help="Write a separate check report; do not give it to ordinary models.")
    parser.add_argument("--schedule-config", type=Path, help="JSON object of schedule names and one or two arrival times.")
    args = parser.parse_args()

    # Check every path before writing anything, including a private check report.
    inputs = args.samples + args.gold + ([args.schedule_config] if args.schedule_config else [])
    outputs = [args.out, args.review] + ([args.report] if args.report else [])
    input_paths = {path.resolve() for path in inputs}
    output_paths = [path.resolve() for path in outputs]
    if len(output_paths) != len(set(output_paths)):
        parser.error("Trace, review, and report outputs must use different files")
    if input_paths & set(output_paths):
        parser.error("Trace outputs must not overwrite an input file")
    schedules = SCHEDULES
    if args.schedule_config:
        schedules = json.loads(args.schedule_config.read_text(encoding="utf-8"))
    validate_schedules(schedules)
    samples = read_records(args.samples)
    gold = read_records(args.gold)
    if not gold:
        raise ValueError("No gold records")
    unknown = set(gold) - set(samples)
    if unknown:
        raise ValueError("Gold has unknown samples: " + ", ".join(sorted(unknown)))
    for sid, record in gold.items():
        validate_pair(samples[sid], record)
    versions = {record["data_version"] for record in gold.values()}
    if len(versions) != 1:
        raise ValueError("Gold records must use one data version")
    version = next(iter(versions))
    if version != DATA_VERSION and (
            args.out.resolve() == (HERE / "traces_debug.jsonl").resolve() or
            args.review.resolve() == (HERE / "traces_review.md").resolve()):
        parser.error("Non-debug traces need separate --out and --review files")

    traces = []
    checks = []
    review = ["# Traces — Review Copy", "",
              "Generated by `build_traces.py`. Do not edit by hand. Batch times (s): "
              + "; ".join(name + " " + str(times) for name, times in schedules.items())
              + ". Documents marked * are cited by supporting_facts.", ""]
    if version != DATA_VERSION:
        review += ["Data version: `" + version + "`.", "",
                   "This review contains gold-based support times. It is not an ordinary model input.", ""]
    for number, sample in enumerate(samples.values(), start=1):
        if sample["sample_id"] not in gold:
            continue
        record = gold[sample["sample_id"]]
        question_number = sample.get("question_number", number)
        if type(question_number) is not int or question_number < 1:
            raise ValueError(sample["sample_id"] + ": invalid question_number")
        cited = set(gold_documents(sample))
        review += ["## Q" + str(question_number) + " — `" + sample["sample_id"] + "`", ""]
        for schedule, times in schedules.items():
            trace = build_trace(sample, schedule, times, record)
            validate(trace, sample)
            traces.append(trace)
            batches = document_batches(sample, len(times), record)
            parts = [str(time) + " s: " + ", ".join("d" + str(n) + ("*" if n in cited else "") for n in batch)
                     for time, batch in zip(times, batches)]
            known = {event["evidence_id"] for event in trace["events"]}
            missing = support_ids(record) - known
            if missing:
                raise ValueError(trace["trace_id"] + ": gold evidence missing from trace: " + ", ".join(sorted(missing)))
            found = supported_times(record, trace)
            required = [found[unit["unit_id"]] for unit in record["units"] if unit["necessary"]]
            if None in required:
                raise ValueError(trace["trace_id"] + ": a necessary answer has no support time")
            checks.append({"question_number": question_number, "sample_id": sample["sample_id"],
                           "trace_id": trace["trace_id"], "event_count": len(trace["events"]),
                           "supported_at": found, "final_supported_at": max(required)})
            review.append("- `" + schedule + "` — " + " | ".join(parts) + " — supported at: " + ", ".join(
                unit["unit_id"] + ("★" if unit["necessary"] else "") + "=" + str(found[unit["unit_id"]])
                for unit in record["units"]))
        review.append("")

    report = {"passed": True, "schema_version": SCHEMA_VERSION, "data_version": version,
              "input_samples": [str(path) for path in args.samples],
              "input_gold": [str(path) for path in args.gold], "schedules": schedules,
              "question_count": len(gold), "trace_count": len(traces),
              "gold_unit_count": sum(len(record["units"]) for record in gold.values()),
              "presupposition_units": sum(bool(unit.get("presupposition_sets"))
                                            for record in gold.values() for unit in record["units"]),
              "all_context_preserved": True, "gold_fields_in_trace": False,
              "total_events": sum(len(trace["events"]) for trace in traces), "records": checks}
    # Write only after all inputs, traces, and required support times pass checks.
    for output in outputs:
        output.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as file:
        for trace in traces:
            file.write(json.dumps(trace, ensure_ascii=False, allow_nan=False) + "\n")
    args.review.write_text("\n".join(review), encoding="utf-8")
    if args.report:
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    built = len(traces) // len(schedules)
    print("Wrote " + str(len(traces)) + " traces (" + str(built) + " samples with gold x "
          + str(len(schedules)) + " schedules) to " + str(args.out))
    print("Skipped " + str(len(samples) - built) + " samples without gold")


if __name__ == "__main__":
    main()
