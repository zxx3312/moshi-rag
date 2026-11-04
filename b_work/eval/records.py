"""Read shared data and check A's policy logs. Uses the standard library only."""

from copy import deepcopy
import json
import math
from pathlib import Path


ACTIONS = {"Wait", "Backchannel", "Progress", "Partial Answer", "Final Answer"}
LOG_FIELDS = {"schema_version", "data_version", "sample_id", "trace_id", "run_id", "policy", "seed",
              "time_origin", "clock", "decision_time_s", "action", "text", "evidence_snapshot_ids",
              "output_start_time_s", "output_end_time_s", "claim_spans", "status"}


def require(condition, message):
    """Stop on bad input with a short reason."""
    if not condition:
        raise ValueError(message)


def number(value):
    """Reject booleans and non-finite numbers used as times."""
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def read_jsonl(path):
    """Read objects and report the file and line for bad JSON."""
    rows = []
    with Path(path).open(encoding="utf-8") as file:
        for index, line in enumerate(file, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
                require(isinstance(row, dict), "Each row must be an object")
            except ValueError as error:
                raise ValueError(f"{path}:{index}: {error}") from error
            rows.append(row)
    return rows


def write_jsonl(path, rows):
    """Write generated rows as UTF-8 JSONL."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False, allow_nan=False) + "\n")


def unique_index(rows, key):
    """Index records without silently replacing duplicate IDs."""
    result = {}
    for row in rows:
        require(isinstance(row, dict), "Indexed records must be objects")
        value = row.get(key)
        require(isinstance(value, str) and value.strip(), "Missing " + key)
        require(value not in result, "Duplicate " + key + ": " + value)
        result[value] = row
    return result


def check_gold(record):
    """Check unit fields and dependencies before any recursive scoring."""
    units = record.get("units")
    require(isinstance(units, list) and units, "Gold needs a nonempty units list")
    by_id = unique_index(units, "unit_id")
    require(any(unit.get("necessary") is True for unit in units), "Gold has no necessary unit")
    for unit in units:
        uid = unit["unit_id"]
        require(type(unit.get("necessary")) is bool, uid + ": invalid necessary flag")
        require(isinstance(unit.get("expected_answer"), str) and unit["expected_answer"].strip(), uid + ": missing expected answer")
        deps = unit.get("depends_on")
        require(isinstance(deps, list) and all(isinstance(d, str) and d in by_id and d != uid for d in deps), uid + ": invalid dependencies")
        require(len(deps) == len(set(deps)), uid + ": duplicate dependency")
        aliases = unit.get("aliases", [])
        require(isinstance(aliases, list) and all(isinstance(a, str) and a.strip() for a in aliases), uid + ": invalid aliases")
        for flag in ["by_omission", "by_presupposition"]:
            require(type(unit.get(flag, False)) is bool, uid + ": invalid " + flag)
        for field in ["support_sets", "presupposition_sets"]:
            sets = unit.get(field, [] if field == "presupposition_sets" else None)
            require(isinstance(sets, list), uid + ": invalid " + field)
            for inner in sets:
                require(isinstance(inner, list) and all(isinstance(e, str) and e for e in inner), uid + ": invalid support set")
                if not inner:
                    require(field == "support_sets" and sets == [[]] and bool(deps), uid + ": invalid empty support set")
        if unit.get("presupposition_sets"):
            require(unit.get("by_presupposition") is True, uid + ": presupposition sets need the flag")
    visited, active = set(), set()

    def visit(uid):
        """Detect a cycle rather than treating it as unsupported evidence."""
        require(uid not in active, "Gold dependency cycle at " + uid)
        if uid not in visited:
            active.add(uid)
            for parent in by_id[uid]["depends_on"]:
                visit(parent)
            active.remove(uid)
            visited.add(uid)

    for uid in by_id:
        visit(uid)


def prepare_inputs(traces, gold):
    """Check trace/gold identity. A retrieval miss is valid and stays visible in reports."""
    require(bool(traces) and bool(gold), "Trace and gold files must not be empty")
    trace_by_id = unique_index(traces, "trace_id")
    gold_by_id = unique_index(gold, "sample_id")
    for record in gold:
        require(record.get("schema_version") == "1.0", "Unknown gold schema version")
        check_gold(record)
    questions = {}
    for trace in traces:
        tid = trace["trace_id"]
        sid = trace.get("sample_id")
        require(sid in gold_by_id, tid + ": no matching gold record")
        require(trace.get("schema_version") == "1.0", tid + ": unknown trace schema version")
        require(trace.get("data_version") == gold_by_id[sid].get("data_version") and isinstance(trace.get("data_version"), str), tid + ": trace/gold data version mismatch")
        require(trace.get("time_origin") == "question_end", tid + ": unknown time origin")
        require(trace.get("clock") in {"simulated", "audio_stream"}, tid + ": unknown clock")
        require(isinstance(trace.get("question"), str), tid + ": missing question")
        require(sid not in questions or questions[sid] == trace["question"], sid + ": question differs between traces")
        questions[sid] = trace["question"]
        events = trace.get("events")
        require(isinstance(events, list), tid + ": events must be a list")
        known = set()
        last = -math.inf
        for event in events:
            require(isinstance(event, dict), tid + ": event must be an object")
            eid = event.get("evidence_id")
            require(isinstance(eid, str) and eid and eid not in known, tid + ": invalid/duplicate evidence ID")
            known.add(eid)
            time_s = event.get("visible_time_s")
            require(number(time_s) and time_s >= last, tid + ": invalid event order or time")
            last = time_s
        # Do not require all gold evidence in retrieval output. A miss is a real outcome.
    return trace_by_id, gold_by_id


def choose_field(claim, old_name, new_name):
    """Accept A's names and the shared aliases, but reject conflicting values."""
    require(old_name in claim or new_name in claim, "Missing claim field: " + old_name)
    if old_name in claim and new_name in claim:
        require(claim[old_name] == claim[new_name], "Conflicting claim fields: " + old_name)
    return claim[old_name] if old_name in claim else claim[new_name]


def ordered(start, end, message):
    """Check known time bounds; tolerate a small float rounding error."""
    if start is not None and end is not None:
        require(end + 1e-9 >= start, message)


def normalize_log(row, trace):
    """Check one decision and copy A claim names into the evaluator's internal form."""
    require(LOG_FIELDS <= set(row), "Missing policy log fields: " + ", ".join(sorted(LOG_FIELDS - set(row))))
    for key in ["schema_version", "data_version", "sample_id", "trace_id", "time_origin", "clock"]:
        require(row[key] == trace[key], "Trace/log mismatch: " + key)
    for key in ["run_id", "policy"]:
        require(isinstance(row[key], str) and row[key].strip(), "Missing " + key)
    require(type(row["seed"]) is int, "Invalid seed")
    require(row["action"] in ACTIONS, "Unknown action")
    require(row["status"] in {"ok", "error"}, "Unknown log status")
    require(isinstance(row["text"], str), "Log text must be a string")
    decision = row["decision_time_s"]
    require(number(decision), "Invalid decision time")
    times = {event["evidence_id"]: event["visible_time_s"] for event in trace["events"]}
    snapshot = row["evidence_snapshot_ids"]
    require(isinstance(snapshot, list) and all(isinstance(e, str) and e in times for e in snapshot), "Snapshot has unknown evidence")
    require(len(snapshot) == len(set(snapshot)), "Snapshot has duplicate IDs")
    require(all(times[e] <= decision + 1e-9 for e in snapshot), "Future evidence in decision snapshot")
    for key in ["output_start_time_s", "output_end_time_s"]:
        require(row[key] is None or number(row[key]), "Invalid " + key)
    ordered(decision, row["output_start_time_s"], "Output starts before decision")
    ordered(row["output_start_time_s"], row["output_end_time_s"], "Output ends before start")
    ordered(decision, row["output_end_time_s"], "Output ends before decision")
    for key in ["decision_cost_s", "generation_cost_s"]:
        if key in row:
            require(number(row[key]) and row[key] >= 0, "Invalid " + key)
    require(isinstance(row["claim_spans"], list), "claim_spans must be a list")
    result = deepcopy(row)
    result["claim_spans"] = []
    for claim in row["claim_spans"]:
        require(isinstance(claim, dict), "Claim must be an object")
        text = claim.get("text")
        require(isinstance(text, str) and text.strip() and text in row["text"], "Claim text is not part of the reply")
        cites = choose_field(claim, "cited_evidence_ids", "evidence_ids")
        require(isinstance(cites, list) and all(isinstance(e, str) and e in snapshot for e in cites), "Claim cites evidence outside decision snapshot")
        start = choose_field(claim, "start", "start_time_s")
        end = choose_field(claim, "end", "end_time_s")
        require(all(t is None or number(t) for t in [start, end]), "Invalid claim time")
        ordered(decision, start, "Claim starts before decision")
        ordered(decision, end, "Claim ends before decision")
        ordered(start, end, "Claim ends before start")
        ordered(row["output_start_time_s"], start, "Claim starts before output")
        ordered(end, row["output_end_time_s"], "Claim ends after output")
        ordered(start, row["output_end_time_s"], "Claim starts after output")
        ordered(row["output_start_time_s"], end, "Claim ends before output")
        require(claim.get("value") is None or isinstance(claim["value"], str), "Claim value must be a string or null")
        normalized = deepcopy(claim)
        normalized.update(text=text, cited_evidence_ids=list(cites), start=start, end=end)
        result["claim_spans"].append(normalized)
    if row["action"] == "Wait":
        require(not row["text"] and not row["claim_spans"] and row["output_start_time_s"] is None and row["output_end_time_s"] is None,
                "Wait needs empty text/claims and null output times")
    return result


def load_reviews(rows):
    """Index human or external claim-to-gold mappings by their stable log location."""
    result = {}
    for row in rows:
        require(isinstance(row.get("run_id"), str) and row["run_id"], "Review needs run_id")
        require(all(type(row.get(k)) is int and row[k] >= 0 for k in ["record_index", "claim_index"]), "Invalid review index")
        require(isinstance(row.get("gold_unit_id"), str) and row["gold_unit_id"], "Review needs gold_unit_id")
        key = (row["run_id"], row["record_index"], row["claim_index"])
        require(key not in result, "Duplicate claim review: " + str(key))
        result[key] = row
    return result
