"""Compare observed policies and matched speech schedules on scored debug replay logs."""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from math import isclose
from pathlib import Path
from statistics import mean, median

from turntaking.replay import load_jsonl, write_jsonl


def speech_ready(record):
    return record["decision_time_s"] + sum(
        record[k] for k in ("decision_cost_s", "generation_cost_s", "tts_cost_s"))


def overlap(start, end, other_start, other_end):
    return max(0.0, min(end, other_end) - max(start, other_start))


def fixed_playback(records, scores, trace):
    """Replay intact factual utterances with a shared ready time and two release gates."""
    visible_at = {e["evidence_id"]: e["visible_time_s"] for e in trace["events"]}
    complete = trace["retrieval_complete_time_s"]
    segments = []
    skipped = Counter()
    early_end = delayed_end = 0.0
    for index, record in enumerate(records):
        claims = record["claim_spans"]
        if not claims:
            skipped["no_registered_claims"] += 1
            continue
        labels = []
        for number, claim in enumerate(claims):
            score = scores[index, number]
            if (score["value"] != claim["value"] or score["text"] != claim["text"]
                    or score["start"] != claim["start"] or score["end"] != claim["end"]):
                raise ValueError(f"Claim/score mismatch in {record['run_id']} at {index}/{number}")
            labels.append(score["label"])
        if any(label != "SUPPORTED" for label in labels):
            skipped["unsupported_or_unreviewed"] += 1
            continue
        if not all(c.get("value_in_text") is True for c in claims):
            skipped["value_not_located"] += 1
            continue

        start = record["output_start_time_s"]
        duration = record["output_end_time_s"] - start
        first_offset = min(c["start"] for c in claims) - start
        last_offset = max(c["end"] for c in claims) - start
        decision = record["decision_time_s"]
        if any(visible_at[cite] > decision + 1e-6 for c in claims for cite in c["cited_evidence_ids"]):
            raise ValueError(f"Future evidence in {record['run_id']}")
        # Keep the original computation timeline frozen. The only intervention is
        # when prepared speech may enter the single audio output channel.
        ready = speech_ready(record)
        if ready > start + 1e-6 or not (-1e-6 <= first_offset <= last_offset <= duration + 1e-6):
            raise ValueError(f"Inconsistent speech timing in {record['run_id']}")
        early_start = max(ready, early_end)
        delayed_start = max(ready, delayed_end, complete)
        early_end, delayed_end = early_start + duration, delayed_start + duration
        segments.append(dict(record_index=index, text=record["text"], action=record["action"],
                             ready_s=ready, duration_s=duration, first_fact_offset_s=first_offset,
                             incremental_start_s=early_start, delayed_start_s=delayed_start))

    result = dict(segments=segments, excluded_utterances=dict(skipped),
                  speech_s=sum(s["duration_s"] for s in segments),
                  words=sum(len(s["text"].split()) for s in segments))
    for arm in ("incremental", "delayed"):
        result[arm] = dict(first_fact_s=min((s[arm + "_start_s"] + s["first_fact_offset_s"]
                                             for s in segments), default=None),
                           finish_s=(early_end if arm == "incremental" else delayed_end) if segments else None)
    return result


def completion_timeline(records, ttca, retrieval_end):
    """Locate B's completion in the original audio timeline, including any earlier Partial."""
    if ttca is None:
        return None
    matches = [i for i, r in enumerate(records)
               if any(isclose(c["end"], ttca, rel_tol=0, abs_tol=1e-7) for c in r["claim_spans"])]
    if len(matches) != 1:
        raise ValueError(f"Cannot locate completion at {ttca} in {records[0]['run_id']}")
    index = matches[0]
    record = records[index]
    ready = speech_ready(record)
    start = record["output_start_time_s"]
    occupied = Counter()
    for earlier in records[:index]:
        occupied[earlier["action"]] += overlap(
            ready, start, earlier["output_start_time_s"], earlier["output_end_time_s"])
    idle = start - ready - sum(occupied.values())
    if idle < -1e-6 or ttca < start - 1e-6 or ttca > record["output_end_time_s"] + 1e-6:
        raise ValueError(f"Inconsistent completion timeline in {record['run_id']}")
    components = dict(decision_minus_retrieval_s=record["decision_time_s"] - retrieval_end,
                      decision_cost_s=record["decision_cost_s"], generation_cost_s=record["generation_cost_s"],
                      tts_cost_s=record["tts_cost_s"], waiting_for_partial_s=occupied["Partial Answer"],
                      waiting_for_other_speech_s=sum(occupied.values()) - occupied["Partial Answer"],
                      idle_after_ready_s=max(0.0, idle), speech_until_complete_s=ttca - start)
    if not isclose(retrieval_end + sum(components.values()), ttca, rel_tol=0, abs_tol=1e-6):
        raise ValueError(f"Timing components do not reproduce B's completion in {record['run_id']}")
    return dict(record_index=index, action=record["action"], ready_s=ready, start_s=start, components=components)


def actual_playback(records, score, retrieval_end):
    partial_s = partial_before_s = 0.0
    partial_count = partial_crossed_during_preparation = 0
    last_end = 0.0
    for r in records:
        start, end = r["output_start_time_s"], r["output_end_time_s"]
        if start < last_end - 1e-6 or end < start:
            raise ValueError(f"Overlapping or reversed speech times in {r['run_id']}")
        last_end = end
        if r["action"] == "Partial Answer":
            partial_count += 1
            if r["decision_time_s"] < retrieval_end <= start:
                partial_crossed_during_preparation += 1
            partial_s += end - start
            partial_before_s += overlap(start, end, 0, retrieval_end)
    return dict(first_fact_s=score["ttfgi_s"], complete_answer_s=score["ttca_s"],
                grounded_complete=score["grounded_complete"], review_claims=score["claims_needing_review"],
                speech_s=sum(r["output_end_time_s"] - r["output_start_time_s"] for r in records),
                words=sum(len(r["text"].split()) for r in records), partial_count=partial_count,
                partial_selected_before_but_started_after_retrieval=partial_crossed_during_preparation,
                partial_s=partial_s, partial_before_retrieval_end_s=partial_before_s,
                partial_after_retrieval_end_s=partial_s - partial_before_s,
                completion=completion_timeline(records, score["ttca_s"], retrieval_end))


def paired(early, late, metric):
    diffs = [b[metric] - a[metric] for a, b in zip(early, late)
             if a[metric] is not None and b[metric] is not None]
    return dict(pairs=len(diffs), median_s=median(diffs) if diffs else None,
                earlier=sum(d > 1e-6 for d in diffs), later=sum(d < -1e-6 for d in diffs))


def timing_breakdown(ours, wait):
    """Positive gaps here mean extra time in Evidence-Aware, using the same pairs for every term."""
    pairs = [(a, b) for a, b in zip(ours, wait) if a["completion"] and b["completion"]]
    partial = sum(r["partial_s"] for r in ours)
    before = sum(r["partial_before_retrieval_end_s"] for r in ours)
    delays = [a["complete_answer_s"] - b["complete_answer_s"] for a, b in pairs]
    blocked = [a["completion"]["components"]["waiting_for_partial_s"] for a, b in pairs]
    component_means = {}
    if pairs:
        for key in pairs[0][0]["completion"]["components"]:
            component_means[key] = mean(a["completion"]["components"][key] - b["completion"]["components"][key]
                                        for a, b in pairs)
        if not isclose(sum(component_means.values()), mean(delays), rel_tol=0, abs_tol=1e-6):
            raise ValueError("Paired completion time difference does not match component means")
    return dict(traces_with_partial=sum(r["partial_count"] > 0 for r in ours),
                partial_utterances=sum(r["partial_count"] for r in ours),
                partial_selected_before_but_started_after_retrieval=sum(
                    r["partial_selected_before_but_started_after_retrieval"] for r in ours),
                partial_s=partial,
                partial_before_retrieval_end_s=before, partial_after_retrieval_end_s=partial - before,
                fraction_of_partial_before_retrieval_end=before / partial if partial else None,
                completion_pairs=len(pairs), pairs_blocked_by_partial=sum(x > 1e-6 for x in blocked),
                later_pairs=sum(d > 1e-6 for d in delays),
                later_pairs_blocked_by_partial=sum(d > 1e-6 and x > 1e-6 for d, x in zip(delays, blocked)),
                mean_extra_completion_s=mean(delays) if pairs else None, mean_extra_components_s=component_means)


def summarize(rows):
    early = [r["actual_evidence_aware"] for r in rows]
    wait = [r["actual_wait_all"] for r in rows]
    fixed = [r["fixed"] for r in rows]
    incremental = [f["incremental"] for f in fixed]
    delayed = [f["delayed"] for f in fixed]
    excluded = Counter()
    for f in fixed:
        excluded.update(f["excluded_utterances"])
    return dict(traces=len(rows), questions=len({r["sample_id"] for r in rows}),
                actual_first_fact=paired(early, wait, "first_fact_s"),
                actual_complete_answer=paired(early, wait, "complete_answer_s"),
                actual_timing_breakdown=timing_breakdown(early, wait),
                actual_speech=dict(evidence_aware_median_s=median(r["speech_s"] for r in early),
                                   wait_all_median_s=median(r["speech_s"] for r in wait)),
                actual_complete_counts={name: dict(confirmed=sum(r["grounded_complete"] is True for r in arm),
                                                   unknown=sum(r["grounded_complete"] is None for r in arm))
                                        for name, arm in (("evidence_aware", early), ("wait_all", wait))},
                fixed_first_fact=paired(incremental, delayed, "first_fact_s"),
                fixed_finish=paired(incremental, delayed, "finish_s"),
                fixed_segment_count=sum(len(f["segments"]) for f in fixed),
                fixed_multisegment_traces=sum(len(f["segments"]) >= 2 for f in fixed),
                excluded_utterances=dict(excluded))


def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", type=Path, required=True, help="A scored debug replay directory")
    parser.add_argument("--traces", type=Path, required=True, help="Debug traces used by that replay")
    parser.add_argument("--out", type=Path, required=True, help="New analysis directory")
    args = parser.parse_args()
    run, b_eval = args.run, args.run / "b_eval"
    config = json.loads((run / "run_config.json").read_text())
    policy = f"evidence_aware+{config['judge_name']}_real+concurrent"
    log_path = run / "policy_log.jsonl"
    evaluator = json.loads((b_eval / "evaluation_config.json").read_text())
    hashes = {item["sha256"] for item in evaluator["inputs"]}
    if any(file_hash(path) not in hashes for path in (args.traces, log_path)):
        raise ValueError("Trace or log differs from the input recorded by B's evaluator")
    logs = defaultdict(list)
    for row in load_jsonl(log_path):
        if row["policy"] in (policy, "wait_all"):
            logs[row["run_id"]].append(row)
    scored = {}
    for row in load_jsonl(b_eval / "run_scores.jsonl"):
        if row["policy"] in (policy, "wait_all"):
            key = row["trace_id"], row["policy"]
            if key in scored or row["status"] != "ok":
                raise ValueError(f"Duplicate or invalid scored run: {key}")
            scored[key] = row
    claims = defaultdict(dict)
    for row in load_jsonl(b_eval / "claim_scores.jsonl"):
        if row["policy"] == policy:
            claims[row["run_id"]][row["record_index"], row["claim_index"]] = row

    rows = []
    for trace in load_jsonl(args.traces):
        tid = trace["trace_id"]
        ours, wait = scored[tid, policy], scored[tid, "wait_all"]
        records = logs[ours["run_id"]]
        if len(records) != ours["records"] or len(logs[wait["run_id"]]) != wait["records"]:
            raise ValueError(f"Log/score record count mismatch for {tid}")
        rows.append(dict(trace_id=tid, sample_id=trace["sample_id"], schedule=tid.rsplit("_", 1)[1],
                         retrieval_complete_s=trace["retrieval_complete_time_s"],
                         actual_evidence_aware=actual_playback(records, ours, trace["retrieval_complete_time_s"]),
                         actual_wait_all=actual_playback(logs[wait["run_id"]], wait, trace["retrieval_complete_time_s"]),
                         fixed=fixed_playback(records, claims[ours["run_id"]], trace)))
    if len({r["trace_id"] for r in rows}) != len(rows) or len(scored) != 2 * len(rows):
        raise ValueError("Trace and scored-run populations differ")

    summary = {s: summarize([r for r in rows if r["schedule"] == s]) for s in sorted({r["schedule"] for r in rows})}
    sources = [args.traces, log_path, run / "run_config.json", b_eval / "evaluation_config.json",
               b_eval / "run_scores.jsonl", b_eval / "claim_scores.jsonl", Path(__file__)]
    report = dict(policy=policy, sources={str(path): file_hash(path) for path in sources},
                  all_traces=summarize(rows), by_schedule=summary)
    args.out.mkdir(parents=True, exist_ok=False)
    write_jsonl(args.out / "trace_pairs.jsonl", rows)
    (args.out / "summary.json").write_text(json.dumps(report, indent=2) + "\n")


if __name__ == "__main__":
    main()
