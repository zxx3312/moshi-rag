#!/usr/bin/env python
"""Aggregate a latency-sweep run directory by delay condition. Stdlib only (login-node safe).

    python experiments/async_retrieval_latency/analysis/analyze_latency.py RUN_DIR [--recompute]

Writes RUN_DIR/analysis/{per_run.csv, summary_by_delay.csv, summary.json, prefix_consistency.json}.

--recompute re-derives metrics from traces/*.json (e.g. with other --audible-db / --speech-db)
instead of reading results.jsonl.

Premature-answer correctness, pre/post-RAG contradiction and naturalness are NOT computed
here; they need human or LLM-judge annotation of the saved transcripts and audio.
"""

from __future__ import annotations

import argparse
import csv
import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from analysis.metrics import DEFAULT_AUDIBLE_DB, DEFAULT_SPEECH_DB, compute_metrics  # noqa: E402

NUMERIC = [
    "trigger_to_injection_s",
    "retrieval_trigger_time",
    "response_onset_latency_s",
    "first_text_latency_s",
    "first_informative_latency_s",
    "longest_response_silence_s",
    "num_silences_ge_1s",
    "num_silences_ge_2s",
    "num_retrievals",
    "pre_rag.duration_s",
    "pre_rag.speech_s",
    "pre_rag.silence_s",
    "pre_rag.longest_silence_s",
    "pre_rag.num_words",
    "wait_window.speech_s",
    "wait_window.num_words",
    "post_rag.speech_s",
    "post_rag.num_words",
    "pre_rag_filler.filler_total",
    "pre_rag_filler.max_ngram_repeat",
]
BOOLEAN = [
    "rag_triggered",
    "answer_mentioned_before_injection",
    "trigger_before_user_end",
    "pre_rag_filler.repeated_filler",
]


def get(rec: dict[str, Any], dotted: str) -> Any:
    cur: Any = rec
    for part in dotted.split("."):
        if not isinstance(cur, dict):
            return None
        cur = cur.get(part)
    return cur


def load_records(run_dir: Path, recompute: bool, speech_db: float, audible_db: float) -> list[dict[str, Any]]:
    results = run_dir / "results.jsonl"
    records = [json.loads(line) for line in results.read_text(encoding="utf-8").splitlines() if line.strip()] \
        if results.is_file() else []
    if not recompute:
        return records
    by_id = {r.get("run_id"): r for r in records}
    out = []
    for trace_path in sorted((run_dir / "traces").glob("*.json")):
        trace = json.loads(trace_path.read_text(encoding="utf-8"))
        m = compute_metrics(trace, speech_db=speech_db, audible_db=audible_db)
        run_id = trace["experiment"].get("run_id", trace_path.stem)
        prev = by_id.get(run_id, {})
        m.update({"run_id": run_id, "status": prev.get("status", m["status"]), "error": prev.get("error")})
        out.append(m)
    return out


def summarize(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[float, list[dict[str, Any]]] = defaultdict(list)
    for r in records:
        groups[float(r["retrieval_delay_condition"])].append(r)
    rows = []
    for delay in sorted(groups):
        rs = groups[delay]
        ok = [r for r in rs if r.get("status") == "ok"]
        row: dict[str, Any] = {"delay_s": delay, "n_runs": len(rs), "n_ok": len(ok)}
        for key in NUMERIC:
            vals = [float(v) for v in (get(r, key) for r in ok) if isinstance(v, (int, float))]
            row[f"{key}.n"] = len(vals)
            row[f"{key}.mean"] = round(statistics.fmean(vals), 4) if vals else None
            row[f"{key}.median"] = round(statistics.median(vals), 4) if vals else None
        for key in BOOLEAN:
            vals = [v for v in (get(r, key) for r in ok) if isinstance(v, bool)]
            row[f"{key}.n"] = len(vals)
            row[f"{key}.rate"] = round(sum(vals) / len(vals), 4) if vals else None
        stops: dict[str, int] = defaultdict(int)
        for r in rs:
            stops[str(r.get("stop_reason"))] += 1
        row["stop_reasons"] = dict(stops)
        rows.append(row)
    return rows


def prefix_consistency(run_dir: Path, records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """For each (sample, seed): are the model tokens identical across delays before the earliest injection?

    If they are, the delay conditions differ only after the reference arrives, which is the intended control.
    If not, GPU nondeterminism or RNG interleaving with the STT model is adding noise.
    """
    groups: dict[tuple[str, int], list[dict[str, Any]]] = defaultdict(list)
    for r in records:
        if r.get("status") == "ok" and r.get("trace_path"):
            groups[(r["sample_id"], r["seed"])].append(r)
    out = []
    for (sid, seed), rs in sorted(groups.items()):
        traces = [json.loads((run_dir / r["trace_path"]).read_text(encoding="utf-8")) for r in rs]
        inj = [t["retrieval_events"][0]["injection_step"] for t in traces
               if t.get("retrieval_events") and t["retrieval_events"][0].get("injection_step") is not None]
        if len(traces) < 2 or not inj:
            out.append({"sample_id": sid, "seed": seed, "n_runs": len(traces), "comparable": False})
            continue
        k = min(inj)
        seqs = [t["model_text"][:k] for t in traces]
        first_div = next((i for i in range(k) if len({tuple(s[i:i + 1]) for s in seqs}) > 1), None)
        out.append({"sample_id": sid, "seed": seed, "n_runs": len(traces), "comparable": True,
                    "compared_steps": k, "identical_prefix": first_div is None, "first_divergence_step": first_div})
    return out


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    keys: list[str] = []
    for r in rows:
        for k in r:
            if k not in keys:
                keys.append(k)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        for r in rows:
            w.writerow({k: json.dumps(v) if isinstance(v, (dict, list)) else v for k, v in r.items()})


def flat_run_row(r: dict[str, Any]) -> dict[str, Any]:
    row = {k: r.get(k) for k in (
        "run_id", "sample_id", "seed", "retrieval_delay_condition", "effective_delay_s", "status", "stop_reason",
        "rag_triggered", "num_retrievals", "user_end_time", "retrieval_trigger_time", "retrieval_request_time",
        "retrieval_complete_time", "reference_injection_time", "assistant_first_audio_time",
        "first_informative_content_time", "response_end_time", "response_onset_latency_s",
        "first_informative_latency_s", "answer_mentioned_before_injection", "longest_response_silence_s",
        "pre_rag_transcript", "post_rag_transcript", "assistant_transcript", "output_audio_path")}
    for key in NUMERIC + BOOLEAN:
        if "." in key:
            row[key] = get(r, key)
    return row


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("run_dir", type=Path)
    p.add_argument("--recompute", action="store_true")
    p.add_argument("--speech-db", type=float, default=DEFAULT_SPEECH_DB)
    p.add_argument("--audible-db", type=float, default=DEFAULT_AUDIBLE_DB)
    args = p.parse_args()

    records = load_records(args.run_dir, args.recompute, args.speech_db, args.audible_db)
    if not records:
        print(f"no records in {args.run_dir}", file=sys.stderr)
        return 1
    out_dir = args.run_dir / "analysis"
    out_dir.mkdir(exist_ok=True)
    summary = summarize(records)
    prefix = prefix_consistency(args.run_dir, records)
    write_csv(out_dir / "per_run.csv", [flat_run_row(r) for r in records])
    write_csv(out_dir / "summary_by_delay.csv", summary)
    (out_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    (out_dir / "prefix_consistency.json").write_text(json.dumps(prefix, indent=2), encoding="utf-8")

    cols = [("delay_s", "delay"), ("n_ok", "ok"), ("rag_triggered.rate", "RET%"),
            ("trigger_to_injection_s.median", "ret->inj"), ("response_onset_latency_s.median", "onset"),
            ("first_informative_latency_s.median", "1st info"), ("pre_rag.speech_s.median", "preRAG speech"),
            ("pre_rag.num_words.median", "preRAG words"), ("longest_response_silence_s.median", "max gap"),
            ("answer_mentioned_before_injection.rate", "ans<inj%"), ("pre_rag_filler.repeated_filler.rate", "rep.fill%")]
    print("medians in seconds unless noted; rates over ok runs with a defined value")
    print("  ".join(f"{h:>13}" for _, h in cols))
    for row in summary:
        print("  ".join(f"{'-' if row.get(k) is None else row.get(k):>13}" for k, _ in cols))
    n_cmp = [x for x in prefix if x.get("comparable")]
    if n_cmp:
        same = sum(1 for x in n_cmp if x["identical_prefix"])
        print(f"\nprefix consistency (pre-injection tokens identical across delays): {same}/{len(n_cmp)} sample-seeds")
    print(f"\nwrote {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
