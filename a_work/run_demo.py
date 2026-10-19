"""Replay the demo traces under every policy and print timelines plus preview metrics.

    python3 a_work/run_demo.py [--trace ...] [--gold ...] [--out ...]
"""
import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from turntaking.judge import OracleJudge  # noqa: E402
from turntaking.policies import EvidenceAware, FirstEvidence, FixedProgress, TimeOnly, WaitAll  # noqa: E402
from turntaking.preview import claim_supported, preview_metrics  # noqa: E402
from turntaking.replay import load_jsonl, replay, units_without_gold, write_jsonl  # noqa: E402


def fmt(x):
    return "-" if x is None else f"{x:.1f}s"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--trace", default=HERE / "demo/trace.jsonl")
    ap.add_argument("--gold", default=HERE / "demo/gold.jsonl")
    ap.add_argument("--out", default=HERE / "demo/out/policy_log.jsonl")
    args = ap.parse_args()

    traces = load_jsonl(args.trace)
    golds = {g["sample_id"]: g for g in load_jsonl(args.gold)}
    policies = [WaitAll(), FixedProgress(), TimeOnly(), FirstEvidence(), EvidenceAware(OracleJudge(golds.values()))]

    all_records, rows = [], []
    for trace in traces:
        gold = golds[trace["sample_id"]]
        gold_units = {u["unit_id"]: u for u in gold["units"]}
        units = units_without_gold(gold)
        print(f"\n=== {trace['question']}")
        for e in trace["events"]:
            print(f"    {e['visible_time_s']:>4.1f}s  {e['evidence_id']} arrives: {e['text'][:70]}")
        for policy in policies:
            records = replay(trace, units, policy)
            all_records += records
            print(f"  [{policy.name}]")
            for r in records:
                marks = " ".join(
                    f"{c['controller_unit_id']}={'ok' if claim_supported(c, gold_units, trace) else 'UNSUPPORTED'}"
                    for c in r["claim_spans"]
                )
                print(f"    {r['output_start_time_s']:>4.1f}s  {r['action']:<14} {r['text']}  {marks}")
            rows.append((trace["sample_id"][:24], policy.name, preview_metrics(records, trace, gold)))

    write_jsonl(args.out, all_records)
    print(f"\nWrote {len(all_records)} records to {args.out}")
    print("\nPreview metrics (A self-check only; B's evaluator is authoritative)")
    print(f"{'sample':<26}{'policy':<24}{'TTFR':>7}{'TTFGI':>7}{'TTCA':>7}  unsupported/claims")
    for sample, name, m in rows:
        print(f"{sample:<26}{name:<24}{fmt(m['ttfr']):>7}{fmt(m['ttfgi']):>7}{fmt(m['ttca']):>7}  {m['unsupported']}/{m['claims']}")


if __name__ == "__main__":
    main()
