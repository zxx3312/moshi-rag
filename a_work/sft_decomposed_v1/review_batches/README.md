# 人工审查分批索引

共 300 题，额外分为 10 批，每批 30 题。按原 train 顺序，再按原 dev 顺序排列，不随机打乱、不改变训练/验证划分。这里的 dev 是验证集，不是预留测试集；本次未读取预留测试集。

**审阅原则：新旧单元都合理时，跟拆题器对齐。** 每批 Markdown 保留新单元、原人工 gold、完整证据及现有辅助审阅意见。JSON 保留原始生成记录，不自动补写答案或证据。

每题标明批内编号、原 split 与原题号；`sample_id` 是回收审阅结果时的稳定标识。第 09 批同时包含 train 与 dev，回收时必须按原 split 分开。

审查时确认单元正确性，再补 expected_answer、support_sets 等监督字段；证据编号仅在本题内部有效。当前意见属于 AI 辅助审阅，不代表已人工确认。

| Batch | 全局题号 | Train | Dev | Markdown | JSON | 审查人 | 状态 |
|---|---|---:|---:|---|---|---|---|
| 01 | 1–30 | 30 | 0 | [batch_01.md](batch_01/batch_01.md) | [batch_01.json](batch_01/batch_01.json) | 待分配 | 待审查 |
| 02 | 31–60 | 30 | 0 | [batch_02.md](batch_02/batch_02.md) | [batch_02.json](batch_02/batch_02.json) | 待分配 | 待审查 |
| 03 | 61–90 | 30 | 0 | [batch_03.md](batch_03/batch_03.md) | [batch_03.json](batch_03/batch_03.json) | 待分配 | 待审查 |
| 04 | 91–120 | 30 | 0 | [batch_04.md](batch_04/batch_04.md) | [batch_04.json](batch_04/batch_04.json) | 待分配 | 待审查 |
| 05 | 121–150 | 30 | 0 | [batch_05.md](batch_05/batch_05.md) | [batch_05.json](batch_05/batch_05.json) | 待分配 | 待审查 |
| 06 | 151–180 | 30 | 0 | [batch_06.md](batch_06/batch_06.md) | [batch_06.json](batch_06/batch_06.json) | 待分配 | 待审查 |
| 07 | 181–210 | 30 | 0 | [batch_07.md](batch_07/batch_07.md) | [batch_07.json](batch_07/batch_07.json) | 待分配 | 待审查 |
| 08 | 211–240 | 30 | 0 | [batch_08.md](batch_08/batch_08.md) | [batch_08.json](batch_08/batch_08.json) | 待分配 | 待审查 |
| 09 | 241–270 | 3 | 27 | [batch_09.md](batch_09/batch_09.md) | [batch_09.json](batch_09/batch_09.json) | 待分配 | 待审查 |
| 10 | 271–300 | 0 | 30 | [batch_10.md](batch_10/batch_10.md) | [batch_10.json](batch_10/batch_10.json) | 待分配 | 待审查 |

辅助审阅标记、题目内容与证据均来自父目录现有文件。分批是副本，不会自动同步回原 train/dev 文件。人工修改 batch 文件后应保存这些文件，不要直接重新生成覆盖；回收时按 sample_id 合并，并检查每题原 split。

`manifest.json` 保存源文件 SHA256、每批构成与逐题映射，便于核对遗漏、重复及原始位置。

每个 batch 使用独立文件夹，例如 `batch_05/batch_05.md` 与 `batch_05/batch_05.json`，可按文件夹分配给审查人。

每道题的 `Question:` 下方提供空白 `Note:` 行，可直接填写人工修改建议。

## Batch 6–10 当前标注版本

[调整报告与待确认题](annotation_report_batch06_10.md)：150 题已依据人工 Note 调整并补答案/证据，batch 9–10 已补写 60 条 Note。原 7 题已按最新 Note 落实，处理结果见报告。此五批的 JSON records 和 Markdown Adjusted units 是更新后的标注副本，已不再与父目录原始模型记录完全一致；原模型输出保存在 raw_decomposition。批次 1–5 不变。

原 Note、原 gold 及全部上下文均保留。逐时刻 SFT 快照尚未重建，用户已确认审核通过；单元证据不足状态仍按 context 保留。修改前文件和逐题决策见 annotation_audit/。

2026-11-28：batch 6–10 已由用户审核，并按最新 Note 完成修订；当前版本 note-aligned-v3。6-15 的鞋匠单元保留证据不足（答案 null）；逐时刻 SFT 尚未重建。历史审阅记录仅供追溯。
