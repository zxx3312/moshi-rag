#!/usr/bin/env python3
"""Render curated SFT review notes without changing model outputs or human gold."""
import argparse
from collections import Counter
import json
import hashlib
from pathlib import Path
import re

LABELS = {
    "modify_generated": "需改：生成拆解",
    "keep_generated_relabel": "保留新拆法｜重标人工标签",
    "review": "待确认：语义或标签口径",
    "no_change": "未发现需单独修改的问题",
}
BLOCK = re.compile(r"<!-- SFT_REVIEW_(?:GUIDE|NOTE)_BEGIN -->\n.*?<!-- SFT_REVIEW_(?:GUIDE|NOTE)_END -->\n\n", re.S)
HEADING = re.compile(r"^## (\d+)\. (\S+?)(?: 【[^\n]*】)?$", re.M)

def strip_notes(text):
    text = BLOCK.sub("", text)
    return HEADING.sub(lambda m: f"## {m[1]}. {m[2]}", text)

def render(text, records):
    base = strip_notes(text)
    found = [(int(m[1]), m[2]) for m in HEADING.finditer(base)]
    expected = [(r["number"], r["sample_id"]) for r in records]
    if found != expected:
        raise ValueError("Question membership/order does not match reviewed records")
    by_id = {r["sample_id"]: r for r in records}
    def annotate(m):
        r = by_id[m[2]]
        if r["status"] == "no_change":
            return m[0]
        label = LABELS[r["status"]]
        evidence = ", ".join(dict.fromkeys(e["evidence_id"] for e in r["evidence"]))
        block = (
            "<!-- SFT_REVIEW_NOTE_BEGIN -->\n"
            f'<a id="human-review-{r["sample_id"]}"></a>\n\n'
            f'> **审阅结论：{label}**（AI 辅助审阅，待人工确认）\n>\n'
            f'> **差异与原因：** {r["reason"]}\n>\n'
            f'> **处理建议：** {r["recommendation"]}\n>\n'
            f'> **证据定位：** {evidence}；原句见本题 Source documents。\n'
            "<!-- SFT_REVIEW_NOTE_END -->\n\n"
        )
        return f"{m[0]} 【{label}】\n\n" + block.rstrip("\n")
    out = HEADING.sub(annotate, base)
    guide = (
        "<!-- SFT_REVIEW_GUIDE_BEGIN -->\n"
        "**审阅原则：新旧单元都合理时，跟拆题器对齐。** 合理的合并、顺序或取值形式变化不要求恢复旧拆法；人工答案、证据集合、依赖标签与逐时刻 SFT 快照需按新单元重新标注。\n\n"
        "题目旁标记：**需改：生成拆解**＝发现题意、关系、目标或题型问题；"
        "**保留新拆法｜重标人工标签**＝生成单元保留，调整监督；"
        "**待确认**＝问题或答案口径需人工裁定。未标记不代表旧标签可以直接复制。\n\n"
        "本页是 AI 辅助审阅建议，不是人工验收或已重建的训练数据。原始生成 JSON、人工 gold 和 B 组文件未修改。"
        "统计与逐题索引见 [comparison_human.md](comparison_human.md)。\n"
        "<!-- SFT_REVIEW_GUIDE_END -->\n\n"
    )
    first = out.index("\n\n") + 2
    out = out[:first] + guide + out[first:]
    if strip_notes(out) != base:
        raise AssertionError("Annotation changed original Markdown content")
    return out

def summary(review):
    records = review["records"]
    lines = ["# 拆题器与人工单元对比（AI 辅助审阅）", "",
        "原则：**新旧单元都合理时，保留拆题器拆法，人工监督向新单元对齐。** 不以旧 gold 的粒度、顺序或取值形式作为唯一正确答案。", "",
        "已逐题对比 300 道 SFT 题（train 243 / dev 57）的生成单元与人工单元；对疑似问题结合原始证据核查。以下为辅助审阅建议，尚未由人工验收。", "",
        "| 审阅结论 | train | dev | 合计 |", "|---|---:|---:|---:|"]
    for status,label in LABELS.items():
        counts=Counter(r["split"] for r in records if r["status"]==status)
        lines.append(f'| {label} | {counts["train"]} | {counts["dev"]} | {sum(counts.values())} |')
    lines += ["", "## 如何使用标注", "",
        "- **保留新拆法**：保留生成的描述、粒度和合理的依赖关系，重建 expected_answer、support_sets 以及各证据时刻的标签。合并单元常需联合多跳证据；不能只复制最后一跳证据，也不能按相同 u1/u2 编号机械对应。",
        "- **需改生成拆解**：仅修正实际错误。题型元数据错误与实体、关系、答案目标错误分别在逐题建议中说明。若后续人工修正训练单元，还需检查运行时拆题器能否稳定生成同类拆法。",
        "- **待确认**：先澄清问题含义或允许的答案口径，再构建监督。",
        "- **未标记**：本轮未发现需单独修改的问题，不等于可直接复制旧 SFT 标签；所有新单元仍应按新输入重新生成和检查快照。", "",
        "本轮仅添加 Markdown 标记和审阅 JSON，未修改原始生成 JSON、B 组 gold、训练集或验证集，未生成最终训练标签。未使用预留评测集。", "",
        f'机械差异统计：题型不同 {sum(r["type_changed"] for r in records)} 题，结构不同 {sum(r["structure_changed"] for r in records)} 题。这些不是错误率；文字不同也不等于语义错误。', ""]
    for status in ("modify_generated", "keep_generated_relabel", "review"):
        selected=[r for r in records if r["status"]==status]
        lines += [f"## {LABELS[status]}（{len(selected)} 题）", ""]
        for r in selected:
            link=f'{r["split"]}.md#human-review-{r["sample_id"]}'
            lines += [f'### [{r["split"]} #{r["number"]} · {r["sample_id"]}]({link})', "",
                f'**问题：** {r["question"]}', "",
                f'**差异：** {r["old_unit_count"]} → {r["new_unit_count"]} 单元；{r["old_question_type"]} → {r["new_question_type"]}。', "",
                f'**原因：** {r["reason"]}', "", f'**建议：** {r["recommendation"]}', ""]
    lines += ["## 复现标注", "", "逐题判断保存在 `human_comparison_review.json`，其中也记录参考证据原文。重新导出 train.md/dev.md 会覆盖标记，可从仓库根目录运行：", "", "```bash", "python3 a_work/annotate_sft_review.py", "```", "", "脚本仅重放已审阅意见，不运行模型、不自动判定正确性、不修改 JSON 生成结果。若数据内容或模型运行变更，应重新审阅，不应沿用本报告。", ""]
    return "\n".join(lines)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, default=Path(__file__).resolve().parent / "sft_decomposed_v1")
    args=parser.parse_args()
    review=json.loads((args.directory / "human_comparison_review.json").read_text())
    for name in ("train.json", "dev.json", "decompositions.jsonl"):
        key = "a_work/sft_decomposed_v1/" + name
        expected = review["source_sha256"][key]
        if hashlib.sha256((args.directory / name).read_bytes()).hexdigest() != expected:
            raise ValueError("Raw output changed; review must be updated: " + name)
    outputs={}
    for split in ("train", "dev"):
        p=args.directory / f"{split}.md"
        base = strip_notes(p.read_text())
        if hashlib.sha256(base.encode()).hexdigest() != review["base_markdown_sha256"][split]:
            raise ValueError("Markdown content changed; review must be updated: " + split)
        outputs[p]=render(p.read_text(), [r for r in review["records"] if r["split"]==split])
    outputs[args.directory / "comparison_human.md"]=summary(review)
    for p,content in outputs.items():
        p.write_text(content)
    print(json.dumps(Counter(r["status"] for r in review["records"]), ensure_ascii=False))

if __name__ == "__main__":
    main()
