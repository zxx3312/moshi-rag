"""Evaluate the prompt judge and the question decomposer against gold units.

    python3 a_work/eval_judge.py --base-url http://127.0.0.1:8000/v1 --model Qwen/Qwen3-14B --out DIR

1. Decomposition: decomposer units vs gold units (question type, unit count, necessary flags, dependency shape).
2. Labels: the judge gets gold unit descriptions (no answers), so label errors are not mixed with
   decomposition errors. At t=0 and at every evidence arrival its labels (after dependency resolution)
   are compared with the Oracle's.
"""
import argparse
import json
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from turntaking.decompose import decompose  # noqa: E402
from turntaking.judge import OracleJudge, PromptJudge, resolve_dependencies, sufficiency_state  # noqa: E402
from turntaking.llm import ChatClient  # noqa: E402
from turntaking.replay import _parse_events, load_jsonl, units_without_gold, write_jsonl  # noqa: E402
from turntaking.schema import LABELS, SUPPORTED, UNRESOLVED, Observation  # noqa: E402


def norm(s):
    return re.sub(r"[^a-z0-9 ]", "", (s or "").lower()).strip()


def value_match(pred, answers):
    p = norm(pred)
    return bool(p) and any(g and (g in p or p in g) for g in map(norm, answers))


def question_type(gold):
    """Gold may carry question_type (A's mock); B's gold does not, so infer it from the unit structure."""
    if gold.get("question_type"):
        return gold["question_type"]
    units = gold["units"]
    if len(units) == 1:
        return "single"
    conclusions = [u for u in units if u["support_sets"] == [[]] and len(u["depends_on"]) >= 2]
    if conclusions:
        facts = [u for u in units if u not in conclusions]
        return "bridge_comparison" if any(u["depends_on"] for u in facts) else "comparison"
    if all(u["necessary"] and not u["depends_on"] for u in units):
        return "multipart"
    return "bridge"


def shape(units):
    return [(u.necessary, len(u.depends_on)) for u in units]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--trace", type=Path, default=HERE / "mock/trace.jsonl")
    ap.add_argument("--gold", type=Path, default=HERE / "mock/gold.jsonl")
    ap.add_argument("--base-url", default="http://127.0.0.1:8000/v1")
    ap.add_argument("--model", default="Qwen/Qwen3-14B")
    ap.add_argument("--thinking", action="store_true", help="Enable Qwen3 thinking mode (slower).")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    traces = load_jsonl(args.trace)  # B's data has several traces (delay schedules) per question
    golds = load_jsonl(args.gold)
    gold_by_id = {g["sample_id"]: g for g in golds}
    question_of = {t["sample_id"]: t["question"] for t in traces}
    extra = {"chat_template_kwargs": {"enable_thinking": args.thinking}}
    client = ChatClient(args.base_url, args.model, extra_body=extra)
    oracle, judge = OracleJudge(golds), PromptJudge(client)
    args.out.mkdir(parents=True, exist_ok=True)

    decomp_rows, step_rows = [], []
    for g in golds:  # decomposition sees only the question: once per question
        sid, qtype = g["sample_id"], question_type(g)
        if sid not in question_of:
            continue
        gold_units = tuple(units_without_gold(g))
        pred_type, pred_units, fell_back = decompose(question_of[sid], client)
        decomp_rows.append({
            "sample_id": sid, "question": question_of[sid], "gold_type": qtype, "pred_type": pred_type,
            "fell_back": fell_back, "type_ok": pred_type == qtype,
            "count_ok": len(pred_units) == len(gold_units), "shape_ok": shape(pred_units) == shape(gold_units),
            "pred_units": [vars(u) | {"depends_on": list(u.depends_on)} for u in pred_units],
            "gold_units": [{"unit_id": u.unit_id, "description": u.description, "necessary": u.necessary,
                            "depends_on": list(u.depends_on)} for u in gold_units],
        })

    for trace in traces:  # labels: every trace, so every delay schedule
        sid = trace["sample_id"]
        if sid not in gold_by_id:
            continue
        g = gold_by_id[sid]
        qtype, gold_units = question_type(g), tuple(units_without_gold(g))
        events = _parse_events(trace)
        expected = {u["unit_id"]: [u["expected_answer"]] + list(u.get("aliases", [])) for u in g["units"]}
        gold_omission = {u["unit_id"]: u.get("by_omission", False) for u in g["units"]}
        for t in sorted({0.0} | {e.visible_time_s for e in events}):
            visible = tuple(e for e in events if e.visible_time_s <= t)
            obs = Observation(sid, trace["question"], t, visible, gold_units, False)
            o = resolve_dependencies(gold_units, oracle.judge(obs))
            p = resolve_dependencies(gold_units, judge.judge(obs))
            for unit in gold_units:
                uid = unit.unit_id
                step_rows.append({
                    "sample_id": sid, "trace_id": trace["trace_id"], "question_type": qtype, "time_s": t, "unit_id": uid,
                    "necessary": unit.necessary, "oracle": o[uid].label, "prompt": p[uid].label,
                    "value": p[uid].value, "expected": expected[uid][0], "citations": list(p[uid].citations),
                    "by_omission": p[uid].by_omission, "gold_by_omission": bool(gold_omission[uid]),
                    "value_ok": value_match(p[uid].value, expected[uid]) if p[uid].label == SUPPORTED else None,
                    "state_oracle": sufficiency_state(gold_units, o), "state_prompt": sufficiency_state(gold_units, p),
                })

    write_jsonl(args.out / "decompositions.jsonl", decomp_rows)
    write_jsonl(args.out / "judge_steps.jsonl", step_rows)
    write_jsonl(args.out / "judge_calls.jsonl", judge.log)
    report = summarize(decomp_rows, step_rows, judge.log, client, args)
    (args.out / "summary.md").write_text(report, encoding="utf-8")
    print(report)


def pct(n, d):
    return f"{n}/{d} ({100 * n / d:.0f}%)" if d else "-"


def summarize(decomp, steps, calls, client, args):
    lines = ["# Prompt judge evaluation", "",
             f"model `{args.model}`, thinking={args.thinking}, gold `{args.gold}`, traces `{args.trace}` "
             f"({len({s['trace_id'] for s in steps})} traces)", ""]

    lines += ["## Decomposition", "", "| question type | n | type ok | unit count ok | structure ok | fallback |",
              "|---|---|---|---|---|---|"]
    by_type = defaultdict(list)
    for d in decomp:
        by_type[d["gold_type"]].append(d)
    for qt, ds in sorted(by_type.items()) + [("all", decomp)]:
        n = len(ds)
        lines.append(f"| {qt} | {n} | {pct(sum(d['type_ok'] for d in ds), n)} | {pct(sum(d['count_ok'] for d in ds), n)} "
                     f"| {pct(sum(d['shape_ok'] for d in ds), n)} | {sum(d['fell_back'] for d in ds)} |")

    lines += ["", "## Unit labels vs Oracle (gold unit descriptions, after dependency resolution)", ""]
    conf = Counter((s["oracle"], s["prompt"]) for s in steps)
    lines += ["| oracle \\ prompt | " + " | ".join(LABELS) + " |", "|---" * (len(LABELS) + 1) + "|"]
    for o in LABELS:
        lines.append(f"| {o} | " + " | ".join(str(conf[(o, p)]) for p in LABELS) + " |")
    n = len(steps)
    agree = sum(s["oracle"] == s["prompt"] for s in steps)
    false_sup = [s for s in steps if s["prompt"] == SUPPORTED and s["oracle"] != SUPPORTED]
    missed = [s for s in steps if s["oracle"] == SUPPORTED and s["prompt"] != SUPPORTED]
    sup_ok = [s for s in steps if s["prompt"] == SUPPORTED and s["oracle"] == SUPPORTED]
    lines += ["", f"- label agreement: {pct(agree, n)}",
              f"- false SUPPORTED (would allow an unsupported claim): {pct(len(false_sup), sum(s['oracle'] != SUPPORTED for s in steps))} of oracle-unsupported unit-steps",
              f"- missed SUPPORTED (would delay grounded information): {pct(len(missed), sum(s['oracle'] == SUPPORTED for s in steps))} of oracle-supported unit-steps",
              f"- value correct when both say SUPPORTED: {pct(sum(bool(s['value_ok']) for s in sup_ok), len(sup_ok))}",
              f"- by_omission SUPPORTED: judge {sum(s['by_omission'] for s in steps)}, "
              f"of which gold also by_omission {sum(s['by_omission'] and s['gold_by_omission'] for s in steps)}; "
              f"gold by_omission unit-steps {sum(s['gold_by_omission'] and s['oracle'] == SUPPORTED for s in steps)}"]

    lines += ["", "| question type | unit-steps | agreement | false SUPPORTED | missed SUPPORTED |", "|---|---|---|---|---|"]
    by_qt = defaultdict(list)
    for s in steps:
        by_qt[s["question_type"]].append(s)
    for qt, ss in sorted(by_qt.items()):
        lines.append(f"| {qt} | {len(ss)} | {pct(sum(s['oracle'] == s['prompt'] for s in ss), len(ss))} "
                     f"| {sum(s['prompt'] == SUPPORTED and s['oracle'] != SUPPORTED for s in ss)} "
                     f"| {sum(s['oracle'] == SUPPORTED and s['prompt'] != SUPPORTED for s in ss)} |")

    states = {(s["trace_id"], s["time_s"]): (s["state_oracle"], s["state_prompt"]) for s in steps}
    lines += ["", f"- sufficiency state agreement (decides the action): "
                  f"{pct(sum(a == b for a, b in states.values()), len(states))} of decision points"]

    lat = [c["latency_s"] for c in calls]
    errors = sum(1 for c in calls if c["error"])
    downgraded = sum(len(c["downgraded"]) for c in calls)
    lines += ["", "## Judge calls", "",
              f"- calls: {len(calls)}, errors: {errors}, SUPPORTED labels downgraded for invalid citations: {downgraded}"]
    if lat:
        q = sorted(lat)
        lines.append(f"- latency per call: mean {statistics.mean(lat):.2f} s, median {statistics.median(lat):.2f} s, "
                     f"p90 {q[int(0.9 * (len(q) - 1))]:.2f} s, max {q[-1]:.2f} s")
    tokens = [c.completion_tokens for c in client.calls if c.purpose == "judge" and c.completion_tokens]
    if tokens:
        lines.append(f"- completion tokens per judge call: mean {statistics.mean(tokens):.0f}")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    main()
