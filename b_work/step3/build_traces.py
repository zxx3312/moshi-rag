"""Build controlled mock traces for the debug set and validate them (standard library only).

Every context sentence becomes one event with evidence ID "d<N>s<M>" (same convention as
build_gold.py). Documents arrive whole, in batches. The documents cited by supporting_facts
are split in citation order: the first half arrives with batch 1, the rest with batch 2.
A document cited only as alternative support in gold_debug.jsonl arrives with the
supporting_facts document of the same unit. Other distractors alternate between the batches
in document order. Traces carry no gold fields; the scheduler may read gold, the model may not.
"""

import argparse
import json
from pathlib import Path


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


def gold_documents(sample):
    titles = [title for title, _ in sample["context"]]
    order = []
    for title, _ in sample["supporting_facts"]:
        number = titles.index(title) + 1
        if number not in order:
            order.append(number)
    return order


def document_number(evidence_id):
    return int(evidence_id[1:].split("s")[0])


def alternative_documents(gold, record):
    """Map each document cited only by a gold support set to the supporting_facts document
    of the same unit, so that the alternative arrives together with what it substitutes for."""
    result = {}
    if record is None:
        return result
    for unit in record["units"]:
        cited = sorted({document_number(e) for inner in unit["support_sets"] for e in inner})
        anchors = [n for n in gold if n in cited]
        for number in cited:
            if number not in gold and number not in result:
                result[number] = anchors[0] if anchors else gold[-1]
    return result


def document_batches(sample, batch_count, record=None):
    gold = gold_documents(sample)
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
    return {
        "schema_version": SCHEMA_VERSION,
        "data_version": DATA_VERSION,
        "sample_id": sample["sample_id"],
        "trace_id": sample["sample_id"] + "_" + schedule,
        "question": sample["question"],
        "time_origin": "question_end",
        "clock": "simulated",
        "trace_type": "controlled_mock",
        "events": events,
        "retrieval_complete_time_s": max(times),
    }


def validate(trace, sample):
    where = trace["trace_id"]
    if list(trace) != TRACE_KEYS:
        raise ValueError(where + ": unexpected trace fields")
    ids = [event["evidence_id"] for event in trace["events"]]
    if len(ids) != len(set(ids)):
        raise ValueError(where + ": duplicate evidence ID")
    if len(ids) != sum(len(sentences) for _, sentences in sample["context"]):
        raise ValueError(where + ": not every context sentence is an event")
    times = [event["visible_time_s"] for event in trace["events"]]
    if times != sorted(times) or min(times) < 0:
        raise ValueError(where + ": visibility times are not ordered and nonnegative")
    if any(event["scheduled_time_s"] > event["visible_time_s"] for event in trace["events"]):
        raise ValueError(where + ": evidence visible before its scheduled time")
    if trace["retrieval_complete_time_s"] != max(times):
        raise ValueError(where + ": retrieval_complete_time_s is not the last arrival")


def supported_times(gold, trace):
    """Earliest time each gold unit is supported, or None (schema.md 4.2)."""
    visible = {event["evidence_id"]: event["visible_time_s"] for event in trace["events"]}
    units = {unit["unit_id"]: unit for unit in gold["units"]}
    result = {}

    def time_of(unit_id):
        if unit_id not in result:
            unit = units[unit_id]
            options = [max([visible[e] for e in inner], default=0.0) for inner in unit["support_sets"]]
            own = min(options) if options else None
            parents = [time_of(parent) for parent in unit["depends_on"]]
            result[unit_id] = None if own is None or None in parents else max([own] + parents)
        return result[unit_id]

    for unit_id in units:
        time_of(unit_id)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--samples", type=Path, default=HERE.parent / "step2" / "prepared" / "samples_debug.jsonl")
    parser.add_argument("--gold", type=Path, default=HERE / "gold_debug.jsonl")
    parser.add_argument("--out", type=Path, default=HERE / "traces_debug.jsonl")
    parser.add_argument("--review", type=Path, default=HERE / "traces_review.md")
    args = parser.parse_args()

    with args.samples.open("r", encoding="utf-8") as file:
        samples = [json.loads(line) for line in file]
    # Traces are built only for questions that already have gold units.
    gold = {}
    with args.gold.open("r", encoding="utf-8") as file:
        for line in file:
            record = json.loads(line)
            gold[record["sample_id"]] = record
    if not gold:
        raise ValueError("No gold records in " + str(args.gold))

    traces = []
    review = ["# Traces — Review Copy", "",
              "Generated by `build_traces.py`. Do not edit by hand. Batch times (s): "
              + "; ".join(name + " " + str(times) for name, times in SCHEDULES.items())
              + ". Documents marked * are cited by supporting_facts.", ""]
    for number, sample in enumerate(samples, start=1):
        if sample["sample_id"] not in gold:
            continue
        cited = set(gold_documents(sample))
        review += ["## Q" + str(number) + " — `" + sample["sample_id"] + "`", ""]
        for schedule, times in SCHEDULES.items():
            trace = build_trace(sample, schedule, times, gold.get(sample["sample_id"]))
            validate(trace, sample)
            traces.append(trace)
            batches = document_batches(sample, len(times), gold.get(sample["sample_id"]))
            parts = [str(time) + " s: " + ", ".join("d" + str(n) + ("*" if n in cited else "") for n in batch)
                     for time, batch in zip(times, batches)]
            record = gold[sample["sample_id"]]
            known = {event["evidence_id"] for event in trace["events"]}
            missing = {e for unit in record["units"] for inner in unit["support_sets"] for e in inner} - known
            if missing:
                raise ValueError(trace["trace_id"] + ": gold evidence missing from trace: " + ", ".join(sorted(missing)))
            found = supported_times(record, trace)
            review.append("- `" + schedule + "` — " + " | ".join(parts) + " — supported at: " + ", ".join(
                unit["unit_id"] + ("★" if unit["necessary"] else "") + "=" + str(found[unit["unit_id"]])
                for unit in record["units"]))
        review.append("")

    with args.out.open("w", encoding="utf-8") as file:
        for trace in traces:
            file.write(json.dumps(trace, ensure_ascii=False) + "\n")
    args.review.write_text("\n".join(review), encoding="utf-8")
    built = len(traces) // len(SCHEDULES)
    print("Wrote " + str(len(traces)) + " traces (" + str(built) + " samples with gold x "
          + str(len(SCHEDULES)) + " schedules) to " + str(args.out))
    print("Skipped " + str(len(samples) - built) + " samples without gold")


if __name__ == "__main__":
    main()
