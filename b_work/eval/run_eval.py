"""Check and score A policy logs with B gold and traces. No model calls are made."""

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import statistics
import sys

from .records import LOG_FIELDS, load_reviews, prepare_inputs, read_jsonl, require, write_jsonl
from .score import empty_metrics, score_run


HERE = Path(__file__).resolve().parent


def evaluate_corpus(traces, gold, logs, review_rows=(), aligned_policies=(),
                    allow_value_match=False, allow_placeholder=False, timing_kind="unknown",
                    expected_policies=(), expected_seed=0):
    """Keep each run, including bad or missing runs, and return claim audit records."""
    trace_by_id, gold_by_id = prepare_inputs(traces, gold)
    reviews = load_reviews(review_rows)
    runs = defaultdict(list)
    for index, row in enumerate(logs):
        require(LOG_FIELDS <= set(row), f"Log row {index}: missing required fields")
        require(isinstance(row["run_id"], str) and row["run_id"], f"Log row {index}: missing run_id")
        require(isinstance(row["trace_id"], str) and row["trace_id"] in trace_by_id, f"Log row {index}: unknown trace_id")
        require(isinstance(row["policy"], str) and row["policy"], f"Log row {index}: invalid policy")
        require(type(row["seed"]) is int, f"Log row {index}: invalid seed")
        runs[row["run_id"]].append(row)
    for run_id, record_index, claim_index in reviews:
        require(run_id in runs and record_index < len(runs[run_id]), "Review refers to an unknown run or record")
        claims = runs[run_id][record_index]["claim_spans"]
        require(isinstance(claims, list) and claim_index < len(claims), "Review refers to an unknown claim")
    scores, claims = [], []
    observed = set()
    for run_id, rows in runs.items():
        trace = trace_by_id[rows[0]["trace_id"]]
        record = gold_by_id[trace["sample_id"]]
        score, audit = score_run(rows, trace, record, reviews, aligned_policies,
                                 allow_value_match, allow_placeholder, timing_kind)
        score["question_type"] = record.get("question_type", "unknown")
        scores.append(score)
        for claim in audit:
            claims.append({"sample_id": trace["sample_id"], "policy": score["policy"], **claim})
        observed.add((score["trace_id"], score["policy"], score["seed"]))
    # A run with no output leaves no rows. An explicit expected-policy list makes it countable.
    for trace in traces:
        for policy in expected_policies:
            if (trace["trace_id"], policy, expected_seed) in observed:
                continue
            missing = {key: trace[key] for key in ["trace_id", "sample_id", "data_version", "clock"]}
            missing.update(run_id=trace["trace_id"] + "__" + policy + "__s" + str(expected_seed),
                           policy=policy, seed=expected_seed, timing_kind=timing_kind, status="missing",
                           question_type=gold_by_id[trace["sample_id"]].get("question_type", "unknown"),
                           final_answer_attempted=False, records=0, claims_total=0, claims_scored=0,
                           claims_needing_review=0, supported_claims=0, unsupported_claims=0,
                           approximate_mapping_claims=0, by_omission_supported=0, by_presupposition_supported=0,
                           validation_issues=[], review_reasons=["No rows for this expected run."], **empty_metrics())
            scores.append(missing)
    return scores, claims


def aggregate_group(runs):
    """Show metric coverage so missing results cannot look like zero latency or perfect scores."""
    status = Counter(run["status"] for run in runs)
    valid = [run for run in runs if run["status"] in {"ok", "diagnostic"}]
    scored_runs = [run for run in valid if run["unit_em"] is not None]
    claims = sum(run["claims_total"] for run in valid)
    scored_claims = sum(run["claims_scored"] for run in valid)
    pending = sum(run["claims_needing_review"] for run in valid)
    unsupported = sum(run["unsupported_claims"] for run in valid)
    result = {"runs": len(runs), "questions": len({run["sample_id"] for run in runs}),
              "status_counts": dict(status), "unit_scored_runs": len(scored_runs),
              "unit_score_coverage": len(scored_runs) / len(runs),
              "mean_unit_em_on_scored_runs": statistics.mean(run["unit_em"] for run in scored_runs) if scored_runs else None,
              "mean_unit_f1_on_scored_runs": statistics.mean(run["unit_f1"] for run in scored_runs) if scored_runs else None,
              "claims": claims, "scored_claims": scored_claims, "claims_needing_review": pending,
              "claim_coverage": scored_claims / claims if claims else None,
              "unsupported_claims": unsupported,
              "unsupported_rate_on_scored_claims": unsupported / scored_claims if scored_claims else None,
              "unsupported_claim_rate": unsupported / claims if claims and not pending else None,
              "approximate_mapping_claims": sum(run["approximate_mapping_claims"] for run in valid),
              "by_omission_supported": sum(run["by_omission_supported"] for run in valid),
              "by_presupposition_supported": sum(run["by_presupposition_supported"] for run in valid),
              "recorded_grounded_completions": sum(run["grounded_complete"] is True for run in runs),
              "recorded_grounded_completion_rate": sum(run["grounded_complete"] is True for run in runs) / len(runs),
              "completion_unknown_runs": sum(run["grounded_complete"] is None for run in runs)}
    for field in ["ttfr_s", "ttfgi_s", "ttca_s"]:
        measured = [run[field] for run in valid if run[field] is not None]
        result[field] = {"median": statistics.median(measured) if measured else None,
                         "count": len(measured), "runs": len(runs)}
    return result


def summarize(scores, traces):
    """Keep clock modes and data versions separate, and split results by schedule and type."""
    require(bool(scores), "No runs to evaluate; provide logs or --expected-policies")
    trace_by_id = {trace["trace_id"]: trace for trace in traces}

    def grouped(extra=None):
        """Build comparable groups without mixing audio timing with simulated timing."""
        groups = defaultdict(list)
        fields = ["policy", "data_version", "clock", "timing_kind"]
        if extra:
            fields.append(extra)
        for run in scores:
            row = dict(run)
            if extra == "schedule":
                trace = trace_by_id[run["trace_id"]]
                suffix = trace["trace_id"].rsplit("_", 1)[-1]
                row["schedule"] = trace.get("schedule", suffix if suffix in {"immediate", "short", "long"} else "unknown")
            groups[tuple(row[field] for field in fields)].append(run)
        return [{**dict(zip(fields, key)), **aggregate_group(rows)} for key, rows in sorted(groups.items())]

    return {"runs": len(scores), "questions": len({run["sample_id"] for run in scores}),
            "status_counts": dict(Counter(run["status"] for run in scores)),
            "groups": grouped(), "by_schedule": grouped("schedule"),
            "by_question_type": grouped("question_type"),
            "limits": [
                "Scores cover only supplied structured claims, not all facts in the full reply.",
                "Claim extraction and LLM-based semantic scoring are not implemented here.",
                "Unclear mappings are sent to review; they are not guessed as right or wrong.",
                "Unit EM/F1 score necessary gold units, not whole-answer benchmark EM/F1.",
                "No paired bootstrap intervals are computed in this first version.",
                "A omits Wait calls. Empty runs can be found only with an expected-run list.",
                "A's speech times are estimates. Use --timing-kind estimated for those logs.",
            ]}


def display(value):
    """Show missing metrics as a dash, while keeping true zeros visible."""
    return "-" if value is None else f"{value:.3f}"


def make_report(summary):
    """Write a short report with coverage beside every score."""
    lines = ["# Structured Claim Evaluation", "",
             "These scores use supplied claim spans and gold units. They are not a full semantic evaluation.", "",
             f"Runs: {summary['runs']}. Questions: {summary['questions']}.", "",
             "| Policy | Data version | Status counts | Runs | Unit-scored runs | Unit EM | Unit F1 | Claim coverage | Structured UCR | Review claims |",
             "|---|---|---|---:|---:|---:|---:|---:|---:|---:|"]
    for group in summary["groups"]:
        statuses = ", ".join(f"{key}: {count}" for key, count in sorted(group["status_counts"].items()))
        lines.append(f"| {group['policy']} | {group['data_version']} | {statuses} | {group['runs']} | {group['unit_scored_runs']} | "
                     f"{display(group['mean_unit_em_on_scored_runs'])} | {display(group['mean_unit_f1_on_scored_runs'])} | "
                     f"{display(group['claim_coverage'])} | {display(group['unsupported_claim_rate'])} | {group['claims_needing_review']} |")
    lines += ["", "| Policy | Clock | Timing kind | TTFR median (n) | TTFGI median (n) | TTCA median (n) | Recorded completions |",
              "|---|---|---|---:|---:|---:|---:|"]
    for group in summary["groups"]:
        times = [display(group[field]["median"]) + " (" + str(group[field]["count"]) + ")"
                 for field in ["ttfr_s", "ttfgi_s", "ttca_s"]]
        lines.append(f"| {group['policy']} | {group['clock']} | {group['timing_kind']} | "
                     + " | ".join(times) + f" | {group['recorded_grounded_completions']}/{group['runs']} |")
    lines += ["", "## Limits", ""] + ["- " + limit for limit in summary["limits"]]
    return "\n".join(lines) + "\n"


def main():
    """Read A logs and write scores, review items, validation errors, and a summary."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--logs", type=Path, required=True)
    parser.add_argument("--traces", type=Path, default=HERE.parent / "step3/traces_debug.jsonl")
    parser.add_argument("--gold", type=Path, default=HERE.parent / "step3/gold_debug.jsonl")
    parser.add_argument("--reviews", type=Path, help="Reviewed claim-to-gold mappings in JSONL")
    parser.add_argument("--aligned-policy", action="append", default=[], help="A policy whose unit IDs are known to match gold")
    parser.add_argument("--allow-value-match", action="store_true", help="Allow approximate mapping by one exact gold value")
    parser.add_argument("--allow-placeholder", action="store_true", help="Diagnostic scores only; never use for final results")
    parser.add_argument("--timing-kind", choices=["unknown", "estimated", "observed"], default="unknown")
    parser.add_argument("--expected-policies", nargs="*", default=[], help="Count missing runs for these policies on every input trace")
    parser.add_argument("--expected-seed", type=int, default=0)
    parser.add_argument("--runner-commit", help="Record the commit that made the policy log")
    parser.add_argument("--out", type=Path, default=HERE / "output")
    args = parser.parse_args()
    names = ["run_scores.jsonl", "claim_scores.jsonl", "review_queue.jsonl", "validation_issues.jsonl",
             "summary.json", "summary.md", "evaluation_config.json"]
    inputs = [args.logs, args.traces, args.gold] + ([args.reviews] if args.reviews else [])
    require(not ({p.resolve() for p in inputs} & {(args.out / name).resolve() for name in names}),
            "Output files must not overwrite an input file")
    traces, gold, logs = [read_jsonl(path) for path in [args.traces, args.gold, args.logs]]
    review_rows = read_jsonl(args.reviews) if args.reviews else []
    scores, claims = evaluate_corpus(traces, gold, logs, review_rows, args.aligned_policy,
                                     args.allow_value_match, args.allow_placeholder, args.timing_kind,
                                     args.expected_policies, args.expected_seed)
    summary = summarize(scores, traces)
    config = {"schema_version": "1.0", "runner_commit": args.runner_commit,
              "timing_kind": args.timing_kind, "aligned_policies": args.aligned_policy,
              "allow_value_match": args.allow_value_match, "allow_placeholder": args.allow_placeholder,
              "expected_policies": args.expected_policies, "expected_seed": args.expected_seed,
              "scoring_scope": "supplied_structured_claims",
              "inputs": [{"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()} for path in inputs]}
    summary["config"] = config
    write_jsonl(args.out / "run_scores.jsonl", scores)
    write_jsonl(args.out / "claim_scores.jsonl", claims)
    write_jsonl(args.out / "review_queue.jsonl", [claim for claim in claims if claim["label"] == "NEEDS_REVIEW"])
    write_jsonl(args.out / "validation_issues.jsonl", [{"run_id": run["run_id"], **issue}
                                                    for run in scores for issue in run["validation_issues"]])
    for name, content in [("summary.json", summary), ("evaluation_config.json", config)]:
        (args.out / name).write_text(json.dumps(content, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    (args.out / "summary.md").write_text(make_report(summary), encoding="utf-8")
    print("Evaluated " + str(len(scores)) + " runs; statuses: " + str(summary["status_counts"]))
    print("Claims needing review: " + str(sum(run["claims_needing_review"] for run in scores)))
    print("Report: " + str(args.out / "summary.md"))
    return int(any(run["status"] == "invalid" for run in scores))


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError) as error:
        print("Input error: " + str(error), file=sys.stderr)
        raise SystemExit(2)
