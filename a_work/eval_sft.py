"""Score a judge on B's SFT dev set: every record's request against its target labels.

    python a_work/eval_sft.py --base-url URL --model NAME --dev sft_dev.jsonl --out DIR [--no-examples]

Used to select the LoRA judge and to baseline the prompt judge on data it was not tuned on.
Replies go through the same validation as at runtime (normalize_reply + resolve_dependencies).
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

from turntaking.judge import JUDGE_SCHEMA, normalize_reply, resolve_dependencies, sufficiency_state  # noqa: E402
from turntaking.llm import ChatClient  # noqa: E402
from turntaking.preview import norm  # noqa: E402
from turntaking.schema import LABELS, SUPPORTED, UnitJudgment, Unit  # noqa: E402


def parse_request(text):
    """(question, units without necessary flags, visible evidence ids) from a judge request."""
    question = text.split("\n", 1)[0].removeprefix("Question: ")
    raw_units = json.loads(re.search(r"Units:\n(\[.*?\])\n\nEvidence", text, re.S).group(1))
    units = [Unit(u["unit_id"], u["description"], False, tuple(u["depends_on"])) for u in raw_units]
    visible = re.findall(r"^\[([^\]]+)\]", text.split("Evidence received so far:\n", 1)[1], re.M)
    return question, units, visible


def score(rows, targets):
    """Per unit-step and per-record measures from (record metadata, predicted labels, target labels)."""
    conf = Counter()
    groups = defaultdict(list)
    for row in rows:
        for uid, want in row["target"].items():
            got = row["pred"].get(uid, "UNRESOLVED")
            conf[(want, got)] += 1
            groups[row["question_type"]].append((want, got))
    return conf, groups


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dev", type=Path, required=True)
    ap.add_argument("--base-url", default="http://127.0.0.1:8000/v1")
    ap.add_argument("--model", required=True)
    ap.add_argument("--judge-model", default=None, help="Served name of a LoRA adapter; default --model.")
    ap.add_argument("--no-examples", action="store_true")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    records = [json.loads(l) for l in args.dev.read_text(encoding="utf-8").splitlines() if l.strip()][:args.limit]
    client = ChatClient(args.base_url, args.judge_model or args.model,
                        extra_body={"chat_template_kwargs": {"enable_thinking": False}})
    rows, errors, omission, presupposition, values = [], 0, Counter(), Counter(), Counter()
    for rec in records:
        request = rec["messages"][:-1]
        if args.no_examples:
            request = request[:1] + request[-1:]
        question, units, visible = parse_request(request[-1]["content"])
        target_reply = {u["unit_id"]: u for u in json.loads(rec["messages"][-1]["content"])["units"]}
        try:
            raw = client.chat_json(request, purpose="judge", schema=JUDGE_SCHEMA)
        except (ValueError, OSError):
            raw, errors = {}, errors + 1
        out, _ = normalize_reply(raw, units, visible, question)
        out = resolve_dependencies(units, out)
        for uid, t in target_reply.items():
            if t["by_omission"]:
                omission[out[uid].by_omission] += 1
            if t["by_presupposition"]:
                presupposition[out[uid].label == SUPPORTED] += 1
            if t["label"] == SUPPORTED and out[uid].label == SUPPORTED:
                values[norm(out[uid].value) == norm(t["value"]) or norm(t["value"]) in norm(out[uid].value)] += 1
        # All necessary flags are unknown here, so states use the unit the question ends on (the last unit).
        rows.append({"sample_id": rec["metadata"]["sample_id"], "question_type": rec["metadata"]["question_type"],
                     "time_s": rec["metadata"]["time_s"], "target": {u: t["label"] for u, t in target_reply.items()},
                     "pred": {u: j.label for u, j in out.items()},
                     "values": {u: j.value for u, j in out.items()}})

    conf, groups = score(rows, None)
    total = sum(conf.values())
    agree = sum(n for (w, g), n in conf.items() if w == g)
    not_sup = sum(n for (w, _), n in conf.items() if w != SUPPORTED)
    sup = total - not_sup
    false_sup = sum(n for (w, g), n in conf.items() if w != SUPPORTED and g == SUPPORTED)
    missed = sum(n for (w, g), n in conf.items() if w == SUPPORTED and g != SUPPORTED)
    final = sum(r["pred"].get(max(r["target"]), "") == r["target"][max(r["target"])] for r in rows)
    lat = [c.latency_s for c in client.calls]
    lines = ["# SFT dev evaluation", "", f"model `{args.judge_model or args.model}`, few-shot={not args.no_examples}, "
             f"records {len(rows)}, errors {errors}", "",
             f"- label agreement: {agree}/{total} ({agree / total:.1%})",
             f"- false SUPPORTED: {false_sup}/{not_sup} ({false_sup / max(1, not_sup):.1%})",
             f"- missed SUPPORTED: {missed}/{sup} ({missed / max(1, sup):.1%})",
             f"- final unit label correct: {final}/{len(rows)} ({final / max(1, len(rows)):.1%})",
             f"- value matches when both SUPPORTED: {values[True]}/{sum(values.values())}",
             f"- by_omission found: {omission[True]}/{sum(omission.values())}; "
             f"by_presupposition units supported: {presupposition[True]}/{sum(presupposition.values())}",
             f"- latency per call: mean {statistics.mean(lat):.2f} s, median {statistics.median(lat):.2f} s, "
             f"p90 {sorted(lat)[int(0.9 * (len(lat) - 1))]:.2f} s", "",
             "| question type | unit-steps | agreement | false SUPPORTED | missed SUPPORTED |", "|---|---|---|---|---|"]
    for qt, pairs in sorted(groups.items()):
        n = len(pairs)
        lines.append(f"| {qt} | {n} | {sum(w == g for w, g in pairs) / n:.1%} "
                     f"| {sum(w != SUPPORTED and g == SUPPORTED for w, g in pairs)} "
                     f"| {sum(w == SUPPORTED and g != SUPPORTED for w, g in pairs)} |")
    report = "\n".join(lines) + "\n"
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "summary.md").write_text(report, encoding="utf-8")
    with open(args.out / "dev_rows.jsonl", "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(report)


if __name__ == "__main__":
    main()
