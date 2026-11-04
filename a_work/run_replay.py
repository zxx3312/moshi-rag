"""Replay traces under the rule baselines and the evidence-aware policy, with real judge latency on the clock.

    python3 a_work/run_replay.py --base-url http://127.0.0.1:8000/v1 --model Qwen/Qwen3-14B \
        --trace TRACE.jsonl --gold GOLD.jsonl --out DIR

Evidence-aware runs: `+oracle` (gold labels, the upper bound), `+prompt` (prompt judge on gold unit
descriptions, so the gap to oracle is the judge's) and `+prompt_real` (the real system: the question is
decomposed by the LLM, that time delays the first judgment, and claims are scored by value).

To change only the judge, serve it separately: --judge-base-url URL --judge-model judge --judge-name lora
--no-examples. Decomposition and generation stay on --model.

With --generate the LLM writes real sentences and every policy states a value: a baseline's best answer is
scored against gold by value, so it can be wrong. Without it, claims are placeholders, baselines state no
value, and their unsupported counts are a lower bound.
"""
import argparse
import statistics
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from turntaking.decompose import decompose  # noqa: E402
from turntaking.generate import Generator  # noqa: E402
from turntaking.judge import OracleJudge, PromptJudge  # noqa: E402
from turntaking.llm import ChatClient  # noqa: E402
from turntaking.policies import EvidenceAware, FirstEvidence, FixedProgress, TimeOnly, WaitAll  # noqa: E402
from turntaking.preview import preview_metrics  # noqa: E402
from turntaking.replay import load_jsonl, replay, units_without_gold, write_jsonl  # noqa: E402

def fmt(values, total=None):
    present = [v for v in values if v is not None]
    if not present:
        return "-" if total is None else f"- (0/{total})"
    text = f"{statistics.median(present):.1f}"
    return text if total is None else f"{text} ({len(present)}/{total})"


def table(rows, group_key):
    groups = defaultdict(list)
    for r in rows:
        groups[r[group_key]].append(r)
    lines = []
    for group in sorted(groups):
        lines += [f"### {group_key} = {group}", "",
                  "| policy | traces | TTFR | TTFGI (traces with any) | TTCA (completed) | unsupported / claims | asked answer correct | judge s per trace | generation s per trace | values not in text |",
                  "|---|---|---|---|---|---|---|---|---|---|"]
        for policy in dict.fromkeys(r["policy"] for r in rows):
            rs = [r for r in groups[group] if r["policy"] == policy]
            if rs:
                n = len(rs)
                lines.append(
                    f"| {policy} | {n} | {fmt([r['ttfr'] for r in rs])} | {fmt([r['ttfgi'] for r in rs], n)} "
                    f"| {fmt([r['ttca'] for r in rs], n)} | {sum(r['unsupported'] for r in rs)}/{sum(r['claims'] for r in rs)} "
                    f"| {sum(r['final_correct'] for r in rs)}/{n} | {statistics.mean(r['judge_cost_s'] for r in rs):.2f} "
                    f"| {statistics.mean(r['generation_cost_s'] for r in rs):.2f} | {sum(r['value_not_in_text'] for r in rs)} |")
        lines.append("")
    return lines


def paired_with_wait_all(rows):
    """Each policy against Wait-All on the same traces. Medians alone hide who answered at all: TTCA compares only
    traces both completed, so the last two columns count the traces where just one side got the asked answer."""
    wait_all = {r["trace_id"]: r for r in rows if r["policy"] == "wait_all"}
    lines = ["| schedule | policy | TTFGI earlier by (earlier in / pairs) | TTCA earlier by (earlier in / pairs) | only this correct | only Wait-All correct |",
             "|---|---|---|---|---|---|"]

    def earlier(pairs, metric):
        diffs = [w[metric] - r[metric] for r, w in pairs if r[metric] is not None and w[metric] is not None]
        if not diffs:
            return "-"
        return f"{statistics.median(diffs):+.1f} ({sum(d > 0 for d in diffs)}/{len(diffs)})"

    for schedule in sorted({r["schedule"] for r in rows}):
        for policy in dict.fromkeys(r["policy"] for r in rows):
            if policy == "wait_all":
                continue
            pairs = [(r, wait_all[r["trace_id"]]) for r in rows if r["policy"] == policy and r["schedule"] == schedule]
            lines.append(f"| {schedule} | {policy} | {earlier(pairs, 'ttfgi')} | {earlier(pairs, 'ttca')} "
                         f"| {sum(r['final_correct'] and not w['final_correct'] for r, w in pairs)} "
                         f"| {sum(w['final_correct'] and not r['final_correct'] for r, w in pairs)} |")
    return lines + [""]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--trace", type=Path, default=HERE / "mock/trace.jsonl")
    ap.add_argument("--gold", type=Path, default=HERE / "mock/gold.jsonl")
    ap.add_argument("--base-url", default="http://127.0.0.1:8000/v1")
    ap.add_argument("--model", default="Qwen/Qwen3-14B")
    ap.add_argument("--judge-base-url", default=None, help="Server of the judge; default --base-url.")
    ap.add_argument("--judge-model", default=None, help="Served name of the judge; default --model.")
    ap.add_argument("--judge-name", default="prompt", help="Name in the policy column.")
    ap.add_argument("--no-examples", action="store_true", help="Judge without few-shot examples (LoRA).")
    ap.add_argument("--thinking", action="store_true")
    ap.add_argument("--generate", action="store_true", help="Write real sentences with the LLM.")
    ap.add_argument("--concurrent", action="store_true", help="Judge and generate while the agent speaks.")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    traces = load_jsonl(args.trace)
    golds = {g["sample_id"]: g for g in load_jsonl(args.gold)}
    client = ChatClient(args.base_url, args.model, max_tokens=8192 if args.thinking else 1024,
                        extra_body={"chat_template_kwargs": {"enable_thinking": args.thinking}})
    judge_client = ChatClient(args.judge_base_url or args.base_url, args.judge_model or args.model,
                              max_tokens=8192 if args.thinking else 1024,
                              extra_body={"chat_template_kwargs": {"enable_thinking": args.thinking}})
    judge = PromptJudge(judge_client, with_examples=not args.no_examples, name=args.judge_name)
    generator = Generator(client) if args.generate else None
    rules = [WaitAll(), FixedProgress(), TimeOnly(), FirstEvidence()]
    oracle = EvidenceAware(OracleJudge(golds.values()))
    prompt = EvidenceAware(judge, name=f"evidence_aware+{args.judge_name}")
    prompt_real = EvidenceAware(judge, name=f"evidence_aware+{args.judge_name}_real")

    decomposed, logs, rows = {}, [], []
    for trace in traces:
        sid = trace["sample_id"]
        if sid not in golds:
            continue
        gold = golds[sid]
        if sid not in decomposed:  # sees only the question, so once per question
            n_calls = len(client.calls)
            _, units, fell_back = decompose(trace["question"], client)
            decomposed[sid] = (units, sum(c.latency_s for c in client.calls[n_calls:]), fell_back)
        real_units, setup_cost, _ = decomposed[sid]
        gold_units = units_without_gold(gold)
        runs = [(p, gold_units, 0.0, args.generate) for p in rules]
        runs += [(p, gold_units, 0.0, False) for p in (oracle, prompt)]
        runs.append((prompt_real, real_units, setup_cost, True))
        for policy, units, setup, by_value in runs:
            records = replay(trace, units, policy, setup_cost_s=setup, generator=generator, concurrent=args.concurrent)
            logs += records
            metrics = preview_metrics(records, trace, gold, by_value=by_value)
            rows.append({"trace_id": trace["trace_id"], "sample_id": sid, "policy": policy.name,
                         "schedule": trace["trace_id"].rsplit("_", 1)[-1],
                         "question_type": gold.get("question_type", "unknown"), "setup_cost_s": setup, **metrics})

    args.out.mkdir(parents=True, exist_ok=True)
    write_jsonl(args.out / "policy_log.jsonl", logs)
    write_jsonl(args.out / "trace_metrics.jsonl", rows)
    write_jsonl(args.out / "judge_calls.jsonl", judge.log)
    if generator is not None:
        write_jsonl(args.out / "generate_calls.jsonl", generator.log)
        print(f"generation: {len(generator.log)} calls, {generator.fallbacks} replaced by plain facts")
    report = ["# Replay with real judge latency", "",
              f"model `{args.model}`, judge `{args.judge_model or args.model}` ({args.judge_name}), "
              f"thinking={args.thinking}, generate={args.generate}, concurrent={args.concurrent}, "
              f"traces `{args.trace}`, gold `{args.gold}`", "",
              "Times are medians in seconds after the question ends. Self-check metrics: B's evaluator is authoritative.", "",
              "## All traces", ""]
    report += table([dict(r, scope="all") for r in rows], "scope")
    report += ["## Paired with Wait-All", "", "Positive means earlier than Wait-All.", ""] + paired_with_wait_all(rows)
    report += ["## By delay schedule", ""] + table(rows, "schedule")
    report += ["## By question type", ""] + table(rows, "question_type")
    text = "\n".join(report) + "\n"
    (args.out / "summary.md").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
