"""Write a review sheet for a sample of SFT questions (standard library only).

The sample first takes one question per special case (presupposition_sets, by_omission, a necessary
unit no evidence supports), then fills the rest round-robin over dataset x source type, all with a
fixed seed. With --flagged it instead takes every question, in either split, whose annotation notes
ask for review (REVIEW_NOTE). For each question the sheet shows the gold units with their cited
sentences, every context document, and the SFT examples built from it, followed by a review checklist.
"""

import argparse
from collections import defaultdict
import json
from pathlib import Path
import random
import re
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from build_gold_sft import supported_when_all_visible  # noqa: E402

# Note wording that asks a reviewer to decide something (sft_issues_zh.md, Appendix A).
REVIEW_NOTE = re.compile(r"review|flag for|borderline|open point|caveat|unclear|weakest|may prefer|mismatch|may decide",
                         re.IGNORECASE)
CHECKLIST = [
    "结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确",
    "描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）",
    "答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里",
    "证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）",
    "备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子",
    "例外规则：by_omission / presupposition_sets 只用在规则允许的情况",
    "SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致",
]


def evidence_text(sample, evidence_id):
    document, sentence = evidence_id[1:].split("s")
    title, sentences = sample["context"][int(document) - 1]
    return title, sentences[int(sentence)].strip()


def flags(gold):
    units = gold["units"]
    result = []
    if any(u.get("presupposition_sets") for u in units):
        result.append("presupposition")
    if any(u.get("by_omission") for u in units):
        result.append("by_omission")
    if not {u["unit_id"] for u in units if u["necessary"]} <= supported_when_all_visible(units):
        result.append("unreachable")
    return result


def choose(golds, samples, count, split, seed):
    rng = random.Random(seed)
    pool = [g for g in golds if samples[g["sample_id"]]["project_split"] == split]
    rng.shuffle(pool)
    chosen = []
    for flag in ["presupposition", "by_omission", "unreachable"]:
        match = next((g for g in pool if flag in flags(g) and g not in chosen), None)
        if match and len(chosen) < count:
            chosen.append(match)
    groups = defaultdict(list)
    for gold in pool:
        if gold not in chosen:
            sample = samples[gold["sample_id"]]
            groups[(sample["dataset"], sample["type"])].append(gold)
    while len(chosen) < count and any(groups.values()):
        for key in sorted(groups):
            if groups[key] and len(chosen) < count:
                chosen.append(groups[key].pop())
    return chosen


def section(number, gold, sample, annotation, examples, reason=None):
    cited = set()
    lines = ["## 第 " + str(number) + " 题：`" + gold["sample_id"] + "`", "",
             "- 数据集 / 题型：" + sample["dataset"] + " / " + sample["type"] + "（unit 构造类型 " + gold["question_type"] + "）",
             "- 划分：" + sample["project_split"] + "；特殊情况：" + ("、".join(flags(gold)) or "无"),
             "- 问题：" + sample["question"], "- 源答案：" + sample["answer"], ""]
    review_notes = [note for note in annotation.get("notes", []) if REVIEW_NOTE.search(note)]
    if reason or review_notes:
        lines += ["### 复核原因", ""] + (["**" + reason + "**", ""] if reason else [])
        lines += ["> " + note for note in review_notes] + [""]
    lines += ["### Gold units", "",
             "| unit | 描述 | necessary | 答案（别名） | 依赖 |", "|---|---|---|---|---|"]
    for unit in gold["units"]:
        answer = unit["expected_answer"] + (" （" + "; ".join(unit["aliases"]) + "）" if unit.get("aliases") else "")
        answer += " **[by_omission]**" if unit.get("by_omission") else ""
        lines.append("| " + unit["unit_id"] + " | " + unit["description"] + " | " + str(unit["necessary"]).lower()
                     + " | " + answer + " | " + (", ".join(unit["depends_on"]) or "—") + " |")
    lines.append("")
    for unit in gold["units"]:
        lines.append("**" + unit["unit_id"] + " 证据**")
        if unit["support_sets"] == [[]]:
            lines.append("- `[[]]`：结论由依赖 unit 推出")
        elif not unit["support_sets"]:
            lines.append("- `[]`：原文没有明确陈述")
        for kind, sets in [("support", unit["support_sets"]), ("presupposition", unit.get("presupposition_sets", []))]:
            for index, inner in enumerate(s for s in sets if s):
                lines.append("- " + kind + " 第 " + str(index + 1) + " 组：")
                for evidence_id in inner:
                    cited.add(evidence_id)
                    title, text = evidence_text(sample, evidence_id)
                    lines.append("  - `" + evidence_id + "` (" + title + ") " + text)
        lines.append("")
    lines += ["**起草备注**", ""] + ["- " + note for note in annotation.get("notes", [])] + [""]
    lines += ["### 全部文档（`*` = gold 引用的句子）", ""]
    for document, (title, sentences) in enumerate(sample["context"], start=1):
        lines.append("**d" + str(document) + "：" + title + "**")
        for index, text in enumerate(sentences):
            evidence_id = "d" + str(document) + "s" + str(index)
            lines.append("- " + ("*" if evidence_id in cited else "") + "`" + evidence_id + "` " + text.strip())
        lines.append("")
    lines += ["### 由这道题生成的 SFT 样本（" + str(len(examples)) + " 条）", "",
              "| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |", "|---|---|---|"]
    for example in sorted(examples, key=lambda e: (e["metadata"]["trace_id"], e["metadata"]["time_s"])):
        reply = json.loads(example["messages"][-1]["content"])["units"]
        labels = "; ".join(u["unit_id"] + " " + ("✅ " + str(u["value"]) + " ← " + ",".join(u["citations"])
                                                 + (" [presup]" if u["by_presupposition"] else "")
                                                 if u["label"] == "SUPPORTED" else "—") for u in reply)
        lines.append("| " + example["metadata"]["trace_id"].rsplit("_", 1)[1] + " t=" + str(int(example["metadata"]["time_s"]))
                     + " | " + ", ".join("d" + str(n) for n in example["metadata"]["document_order"]) + " | " + labels + " |")
    lines += ["", "### 复核清单", ""] + ["- [ ] " + item for item in CHECKLIST]
    lines += ["", "复核结论（通过 / 修改 / 退回）：", "", "问题记录：", "", "---", ""]
    return lines


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates", type=Path, default=HERE / "prepared" / "samples_sft_candidates.jsonl")
    parser.add_argument("--gold", type=Path, default=HERE / "gold_sft.jsonl")
    parser.add_argument("--annotations", type=Path, nargs="+", default=sorted((HERE / "drafts").glob("annotations_batch_*.json")))
    parser.add_argument("--sft", type=Path, default=HERE / "sft")
    parser.add_argument("--split", default="train", choices=["train", "dev"])
    parser.add_argument("--count", type=int, default=10)
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument("--flagged", action="store_true",
                        help="every question (train and dev) whose notes ask for review; ignores --split/--count/--seed")
    parser.add_argument("--reasons", type=Path, help="optional JSON {sample_id: one-line reason} shown per question")
    parser.add_argument("--out", type=Path, default=HERE / "review" / "sample_review_train_10.md")
    args = parser.parse_args()

    samples = {json.loads(line)["sample_id"]: json.loads(line)
               for line in args.candidates.read_text(encoding="utf-8").splitlines()}
    golds = [json.loads(line) for line in args.gold.read_text(encoding="utf-8").splitlines()]
    annotations = {r["sample_id"]: r for path in args.annotations
                   for r in json.loads(path.read_text(encoding="utf-8"))["records"]}
    examples = defaultdict(list)
    for split in (["train", "dev"] if args.flagged else [args.split]):
        for line in (args.sft / ("sft_" + split + ".jsonl")).read_text(encoding="utf-8").splitlines():
            record = json.loads(line)
            examples[record["metadata"]["sample_id"]].append(record)
    reasons = json.loads(args.reasons.read_text(encoding="utf-8")) if args.reasons else {}

    if args.flagged:
        chosen = sorted((g for g in golds if any(REVIEW_NOTE.search(n) for n in annotations[g["sample_id"]].get("notes", []))),
                        key=lambda g: (reasons.get(g["sample_id"], "~"), g["sample_id"]))
        title = "# 待复核题目（" + str(len(chosen)) + " 题，train 和 dev）"
        intro = ("由 `sample_review.py --flagged` 生成：起草备注中要求复核的全部题目"
                 "（匹配 review、flag for、borderline、open point、caveat 等措辞），按复核原因分组排列。")
    else:
        chosen = choose(golds, samples, args.count, args.split, args.seed)
        title = "# SFT 抽样复核表（" + args.split + "，" + str(len(chosen)) + " 题）"
        intro = ("由 `sample_review.py --split " + args.split + " --count " + str(args.count) + " --seed " + str(args.seed)
                 + "` 生成。前几题按特殊情况（presupposition、by_omission、unreachable）各抽一题，其余按数据集 × 题型轮流抽取。")
    lines = [title, "", intro, "", "| # | sample_id | 数据集 / 题型 | 划分 | 特殊情况 | 复核原因 |", "|---|---|---|---|---|---|"]
    for number, gold in enumerate(chosen, start=1):
        sample = samples[gold["sample_id"]]
        lines.append("| " + str(number) + " | `" + gold["sample_id"] + "` | " + sample["dataset"] + " / " + sample["type"]
                     + " | " + sample["project_split"] + " | " + ("、".join(flags(gold)) or "—")
                     + " | " + reasons.get(gold["sample_id"], "—") + " |")
    lines += ["", "---", ""]
    for number, gold in enumerate(chosen, start=1):
        lines += section(number, gold, samples[gold["sample_id"]], annotations[gold["sample_id"]], examples[gold["sample_id"]],
                         reasons.get(gold["sample_id"]))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(lines), encoding="utf-8")
    print("wrote " + str(len(chosen)) + " questions to " + str(args.out))


if __name__ == "__main__":
    main()
