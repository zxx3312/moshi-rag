# B SFT questions decomposed with A's vLLM configuration

This directory contains a separate vLLM run over the same 300 unique questions as the earlier Transformers export: 243 train and 57 dev. Membership and question text are checked against B's actual SFT files. B source files and the earlier Transformers results are not modified.

## Configuration

- Model: Qwen/Qwen3-14B, snapshot `40c069824f4251a91eefaf281ebe4c544efd3e18`.
- Independent environment: `.venv-decompose`, vLLM 0.32.0, PyTorch 2.13.0, Transformers 5.19.0. These three versions match A's default environment.
- A's unchanged `turntaking/decompose.py` and `turntaking/llm.py`: original rules, nine few-shot examples, output schema, validation and fallback.
- `temperature=0`, `max_tokens=1024`, `enable_thinking=false`, `response_format=json_schema`.
- A's original serving script: context limit 16384, Qwen3 reasoning parser, GPU memory utilization 0.90, FlashInfer sampler disabled.
- Hardware and complete provenance are recorded in `environment.json`. The GPU may differ from A's experiments; this is not a formal latency comparison and does not promise bitwise identical output.

Only the question enters the decomposer. Gold units and source documents appear in review files after inference, not in model input. All new units remain `needs_review`; no old expected answers or support labels are transferred to new units.

## Files

- `questions.json`: deduplicated input questions, split and SFT snapshot count.
- `decompositions.jsonl`: per-question checkpoint, including `fell_back`.
- `train.json`, `dev.json`: annotation-style `records` containing new units.
- `train.md`, `dev.md`: new units, original human gold and source sentences with evidence IDs.
- `manifest.json`: source hashes, generation settings and completion/fallback statistics. Check `completed` before treating the run as finished.
- `environment.json`: package versions, model revision, hardware, server arguments and code hashes.
- `comparison_transformers.json`, `comparison_transformers.md`: validated comparison with the earlier Transformers export, generated after completion. Exact text/structure differences are not semantic accuracy judgments.

## Run again

From the repository root:

```bash
mkdir -p a_work/slurm/logs
sbatch a_work/slurm/decompose_sft_vllm.slurm
```

The script uses vLLM only; it does not fall back to another backend. The same configuration resumes completed checkpoint records. For a new experiment with changed settings, use a fresh export directory.

After completion, compare the results using the corresponding call log:

```bash
python3 a_work/compare_sft_decompositions.py \
  --calls a_work/results/sft_decompose/vllm_v1/llm_calls.jsonl
```

The first run used job `12608904` and log directory `vllm_v1`. The reusable Slurm wrapper uses `vllm_<job_id>` for later runs. Do not commit or push automatically.

## 与人工单元对比

按用户确认的原则：新旧单元都合理时保留拆题器结果，人工监督向新单元对齐。

- `comparison_human.md`：300 题的审阅统计与问题索引。
- `human_comparison_review.json`：逐题审阅意见、原因、建议、参考证据及输入 SHA256；AI 辅助审阅，未人工验收。
- `train.md`、`dev.md`：题号旁标记需改生成拆解、保留新拆法并重标人工标签、或待确认语义/标签口径。
- `../annotate_sft_review.py`：重放审阅标记；校验原始内容哈希，可重复运行。

本轮 34 题需改生成拆解或题型、57 题保留新拆法并调整监督、6 题待确认、203 题未发现需单独修改的问题。
原始生成 JSON、B 组 gold 和 SFT 文件未修改；这些文件仍不是已重建监督的可训练数据。
重新导出 Markdown 后可运行 `python3 a_work/annotate_sft_review.py` 恢复标记。

## 人工审查分批

[review_batches/README.md](review_batches/README.md) 提供 10 个 batch 的分配索引，每批 30 题，各有 JSON 与 Markdown。
按 train 243 题、dev 57 题的原顺序分批：01–08 每批 30 道 train；09 为 train 3 + dev 27；10 为 dev 30。
每题保留原 split、sample_id 和原题号。分批仅为审查副本，不改变训练/验证划分，未读取预留测试集。
Markdown 保留所有原始证据和审阅标记，JSON 的 records 与原生成记录一致；manifest 保存源文件哈希和映射。
人工修改批次文件不会自动写回原文件；后续按 sample_id 回收，避免覆盖审查成果。

各批文件现位于独立的 `review_batches/batch_01/` 至 `batch_10/` 文件夹中，每个文件夹包含同名 JSON 和 Markdown。

人工 Note 调整后的 batch 6–10（150 题）已补答案、支持集合及特殊推理字段；参见 [标注报告](review_batches/annotation_report_batch06_10.md)。批次 JSON 为当前标注副本，原始推理保存在 raw_decomposition；原始 train/dev 导出未覆盖。

2026-11-28：batch 6–10 已由用户审核，并按最新 Note 完成修订；当前版本 note-aligned-v3。6-15 的鞋匠单元保留证据不足（答案 null）；逐时刻 SFT 尚未重建。历史审阅记录仅供追溯。
