"""Replay traces under the rule baselines and the evidence-aware policy, with real judge latency on the clock.

    python3 a_work/run_replay.py --base-url http://127.0.0.1:8000/v1 --model Qwen/Qwen3-14B \
        --trace TRACE.jsonl --gold GOLD.jsonl --out DIR

Evidence-aware runs: `+oracle` (gold labels, the upper bound), `+prompt` (prompt judge on gold unit
descriptions, so the gap to oracle is the judge's) and `+prompt_real` (the real system: the question is
decomposed by the LLM, that time delays the first judgment, and claims are scored by value).

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

REAL = "evidence_aware+prompt_real"
ORDER = ["wait_all", "fixed_progress", "time_only", "first_evidence",
         "evidence_aware+oracle", "evidence_aware+prompt", REAL]


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
                  "| policy | traces | TTFR | TTFGI (traces with any) | TTCA (completed) | unsupported / claims | judge s per trace | generation s per trace | values not in text |",
                  "|---|---|---|---|---|---|---|---|---|"]
        for policy in ORDER:
            rs = [r for r in groups[group] if r["policy"] == policy]
            if rs:
                n = len(rs)
                lines.append(
                    f"| {policy} | {n} | {fmt([r['ttfr'] for r in rs])} | {fmt([r['ttfgi'] for r in rs], n)} "
                    f"| {fmt([r['ttca'] for r in rs], n)} | {sum(r['unsupported'] for r in rs)}/{sum(r['claims'] for r in rs)} "
                    f"| {statistics.mean(r['judge_cost_s'] for r in rs):.2f} "
                    f"| {statistics.mean(r['generation_cost_s'] for r in rs):.2f} | {sum(r['value_not_in_text'] for r in rs)} |")
        lines.append("")
    return lines


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--trace", type=Path, default=HERE / "mock/trace.jsonl")
    ap.add_argument("--gold", type=Path, default=HERE / "mock/gold.jsonl")
    ap.add_argument("--base-url", default="http://127.0.0.1:8000/v1")
    ap.add_argument("--model", default="Qwen/Qwen3-14B")
    ap.add_argument("--thinking", action="store_true")
    ap.add_argument("--generate", action="store_true", help="Write real sentences with the LLM.")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    traces = load_jsonl(args.trace)
    golds = {g["sample_id"]: g for g in load_jsonl(args.gold)}
    client = ChatClient(args.base_url, args.model, max_tokens=8192 if args.thinking else 1024,
                        extra_body={"chat_template_kwargs": {"enable_thinking": args.thinking}})
    judge = PromptJudge(client)
    generator = Generator(client) if args.generate else None
    rules = [WaitAll(), FixedProgress(), TimeOnly(), FirstEvidence()]
    oracle = EvidenceAware(OracleJudge(golds.values()))
    prompt = EvidenceAware(judge, name="evidence_aware+prompt")
    prompt_real = EvidenceAware(judge, name=REAL)

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
            records = replay(trace, units, policy, setup_cost_s=setup, generator=generator)
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
              f"model `{args.model}`, thinking={args.thinking}, generate={args.generate}, "
              f"traces `{args.trace}`, gold `{args.gold}`", "",
              "Times are medians in seconds after the question ends. Self-check metrics: B's evaluator is authoritative.", "",
              "## All traces", ""]
    report += table([dict(r, scope="all") for r in rows], "scope")
    report += ["## By delay schedule", ""] + table(rows, "schedule")
    report += ["## By question type", ""] + table(rows, "question_type")
    text = "\n".join(report) + "\n"
    (args.out / "summary.md").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
