"""Replay traces under the rule baselines and the evidence-aware policy, with real judge latency on the clock.

    python3 a_work/run_replay.py --base-url http://127.0.0.1:8000/v1 --model Qwen/Qwen3-14B \
        --trace TRACE.jsonl --gold GOLD.jsonl --out DIR

Evidence-aware runs: `+oracle` (gold labels, the upper bound), `+prompt` (prompt judge on gold unit
descriptions, so the gap to oracle is the judge's) and `+prompt_real` (the real system: the question is
decomposed by the LLM, that time delays the first judgment, and claims are scored by value).

To change only the judge, serve it separately: --judge-base-url URL --judge-model judge --judge-name lora
--no-examples. Decomposition and generation stay on --model, unless --grounded-model names a smaller model
on the judge's server to phrase the evidence-aware sentences (the baselines' answers stay on --model).

With --generate the LLM writes real sentences and every policy states a value: a baseline's best answer is
scored against gold by value, so it can be wrong. Without it, claims are placeholders, baselines state no
value, and their unsupported counts are a lower bound.

--concurrent adds a `+concurrent` copy of each evidence-aware policy, which judges and generates while the
agent speaks. Both copies share the judge's and the generator's outputs, so they differ only in timing.

Every model call is written to OUT/llm_calls.jsonl. --tape FILE... answers from such files instead of a
server, so a finished GPU run can be replayed anywhere with other timing settings (--tts, --concurrent, --asr
with the same transcripts). A request the tape lacks stops the run; --allow-tape-misses turns it into an
unusable reply and reports the count.

The cascade's speech ends (turntaking/cascade.py): --tts piper:VOICE.onnx times every utterance by its audio
and needs a Python with piper-tts; --asr FILE gives each question as the ASR heard it (run_asr.py).
"""
import argparse
import hashlib
import json
import statistics
import sys
import wave
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from turntaking.cascade import Heard, load_tts  # noqa: E402
from turntaking.decompose import decompose  # noqa: E402
from turntaking.generate import Generator  # noqa: E402
from turntaking.judge import OracleJudge, PromptJudge  # noqa: E402
from turntaking.llm import ChatClient, load_tape  # noqa: E402
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
                  "| policy | traces | TTFR | TTFGI (traces with any) | TTCA (completed) | unsupported / claims | asked answer correct | judge s per trace | generation s per trace | TTS s per trace | values not in text |",
                  "|---|---|---|---|---|---|---|---|---|---|---|"]
        for policy in dict.fromkeys(r["policy"] for r in rows):
            rs = [r for r in groups[group] if r["policy"] == policy]
            if rs:
                n = len(rs)
                lines.append(
                    f"| {policy} | {n} | {fmt([r['ttfr'] for r in rs])} | {fmt([r['ttfgi'] for r in rs], n)} "
                    f"| {fmt([r['ttca'] for r in rs], n)} | {sum(r['unsupported'] for r in rs)}/{sum(r['claims'] for r in rs)} "
                    f"| {sum(r['final_correct'] for r in rs)}/{n} | {statistics.mean(r['judge_cost_s'] for r in rs):.2f} "
                    f"| {statistics.mean(r['generation_cost_s'] for r in rs):.2f} "
                    f"| {statistics.mean(r['tts_cost_s'] for r in rs):.2f} | {sum(r['value_not_in_text'] for r in rs)} |")
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


def save_audio(folder: Path, tts) -> None:
    """One WAV per distinct utterance, named by the text's hash, with an index to find them."""
    folder.mkdir(parents=True, exist_ok=True)
    index = []
    for text, speech in tts.spoken.items():
        name = hashlib.sha1(text.encode("utf-8")).hexdigest()[:16] + ".wav"
        with wave.open(str(folder / name), "wb") as f:
            f.setnchannels(1)
            f.setsampwidth(2)
            f.setframerate(speech.sample_rate)
            f.writeframes(speech.audio)
        index.append({"text": text, "file": name, "duration_s": round(speech.duration_s, 3),
                      "latency_s": round(speech.latency_s, 3)})
    write_jsonl(folder / "index.jsonl", index)


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
    ap.add_argument("--grounded-model", default=None,
                    help="Model on the judge's server that phrases evidence-aware sentences; default --model.")
    ap.add_argument("--thinking", action="store_true")
    ap.add_argument("--generate", action="store_true", help="Write real sentences with the LLM.")
    ap.add_argument("--concurrent", action="store_true",
                    help="Also run each evidence-aware policy judging and generating while the agent speaks.")
    ap.add_argument("--tts", default="rate", help="rate (fixed words per second) or piper:VOICE.onnx.")
    ap.add_argument("--asr", type=Path, default=None, help="JSONL from run_asr.py: sample_id, text, latency_s.")
    ap.add_argument("--save-audio", action="store_true", help="Write the TTS audio of every utterance to OUT/audio.")
    ap.add_argument("--tape", type=Path, nargs="+", default=None,
                    help="llm_calls.jsonl of earlier runs: answer from them, no server needed.")
    ap.add_argument("--allow-tape-misses", action="store_true")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    traces = load_jsonl(args.trace)
    golds = {g["sample_id"]: g for g in load_jsonl(args.gold)}
    shared = dict(max_tokens=8192 if args.thinking else 1024,
                  extra_body={"chat_template_kwargs": {"enable_thinking": args.thinking}},
                  replay=load_tape(args.tape) if args.tape else None, allow_misses=args.allow_tape_misses)
    client = ChatClient(args.base_url, args.model, **shared)
    judge_client = ChatClient(args.judge_base_url or args.base_url, args.judge_model or args.model, **shared)
    judge = PromptJudge(judge_client, with_examples=not args.no_examples, name=args.judge_name)
    grounded_client = (ChatClient(args.judge_base_url or args.base_url, args.grounded_model, **shared)
                       if args.grounded_model else client)
    generator = Generator(client, grounded_client) if args.generate else None
    tts = load_tts(args.tts)
    heard = {r["sample_id"]: Heard(r["text"], float(r["latency_s"])) for r in load_jsonl(args.asr)} if args.asr else {}
    rules = [WaitAll(), FixedProgress(), TimeOnly(), FirstEvidence()]
    oracle_judge = OracleJudge(golds.values())
    # (policy, uses the model's own units, judges and generates while speaking)
    ours = [(EvidenceAware(oracle_judge), False), (EvidenceAware(judge, name=f"evidence_aware+{args.judge_name}"), False),
            (EvidenceAware(judge, name=f"evidence_aware+{args.judge_name}_real"), True)]
    ours = [(p, real, False) for p, real in ours]
    if args.concurrent:
        ours += [(EvidenceAware(p.judge, name=p.name + "+concurrent"), real, True) for p, real, _ in ours]

    decomposed, logs, rows = {}, [], []
    for trace in traces:
        sid = trace["sample_id"]
        if sid not in golds:
            continue
        gold = golds[sid]
        if args.asr and sid not in heard:
            sys.exit(f"--asr has no row for {sid}")
        if sid not in decomposed:  # sees only the question as heard, so once per question
            n_calls = len(client.calls)
            question = heard[sid].text if sid in heard else trace["question"]
            _, units, fell_back = decompose(question, client)
            decomposed[sid] = (units, sum(c.latency_s for c in client.calls[n_calls:]), fell_back)
        real_units, setup_cost, _ = decomposed[sid]
        gold_units = units_without_gold(gold)
        runs = [(p, gold_units, 0.0, args.generate, False) for p in rules]
        runs += [(p, real_units, setup_cost, True, conc) if real else (p, gold_units, 0.0, False, conc)
                 for p, real, conc in ours]
        for policy, units, setup, by_value, concurrent in runs:
            records = replay(trace, units, policy, setup_cost_s=setup, generator=generator, concurrent=concurrent,
                             tts=tts, heard=heard.get(sid))
            logs += records
            metrics = preview_metrics(records, trace, gold, by_value=by_value)
            rows.append({"trace_id": trace["trace_id"], "sample_id": sid, "policy": policy.name,
                         "schedule": trace["trace_id"].rsplit("_", 1)[-1],
                         "question_type": gold.get("question_type", "unknown"), "setup_cost_s": setup,
                         "asr_cost_s": heard[sid].latency_s if sid in heard else 0.0, **metrics})

    clients = list({id(c): c for c in (client, judge_client, grounded_client)}.values())
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "run_config.json").write_text(json.dumps({k: v if isinstance(v, (bool, type(None))) else
                                                          [str(x) for x in v] if isinstance(v, list) else str(v)
                                                          for k, v in vars(args).items()}, indent=2), encoding="utf-8")
    write_jsonl(args.out / "policy_log.jsonl", logs)
    write_jsonl(args.out / "trace_metrics.jsonl", rows)
    write_jsonl(args.out / "judge_calls.jsonl", judge.log)
    write_jsonl(args.out / "decompositions.jsonl", [
        {"sample_id": sid, "question": heard[sid].text if sid in heard else golds[sid].get("question"),
         "latency_s": round(latency, 3), "fell_back": fell_back,
         "units": [{"unit_id": u.unit_id, "description": u.description, "necessary": u.necessary,
                    "depends_on": list(u.depends_on)} for u in units]}
        for sid, (units, latency, fell_back) in decomposed.items()])
    write_jsonl(args.out / "llm_calls.jsonl", {row["key"]: row for c in clients for row in c.tape}.values())
    misses = sum(c.misses for c in clients)
    if generator is not None:
        write_jsonl(args.out / "generate_calls.jsonl", generator.log)
        print(f"generation: {len(generator.log)} calls, {generator.fallbacks} replaced by plain facts")
    if args.save_audio and hasattr(tts, "spoken"):
        save_audio(args.out / "audio", tts)
    report = ["# Replay with real judge latency", "",
              f"model `{args.model}`, judge `{args.judge_model or args.model}` ({args.judge_name}), "
              f"grounded sentences by `{args.grounded_model or args.model}`, "
              f"thinking={args.thinking}, generate={args.generate}, tts={args.tts}, asr={args.asr}, "
              f"traces `{args.trace}`, gold `{args.gold}`"
              + (f", replayed from tape with {misses} requests missing" if args.tape else ""), "",
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
