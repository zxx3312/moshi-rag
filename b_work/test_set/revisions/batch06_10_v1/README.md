# Batch 6–10 修订版

[逐题修改报告](change_report.md) · [新gold（150题）](gold.jsonl) · [配套samples](samples.jsonl) · [校验结果](validation_report.json)

原始batch目录不变。新样本和gold须配套使用。

| Batch | 调整原题 | 替换 | 保留 | 新review |
|---|---:|---:|---:|---|
| 6 | 13 | 3 | 14 | [review.md](batch_06/review.md) |
| 7 | 10 | 7 | 13 | [review.md](batch_07/review.md) |
| 8 | 15 | 2 | 13 | [review.md](batch_08/review.md) |
| 9 | 14 | 6 | 10 | [review.md](batch_09/review.md) |
| 10 | 11 | 6 | 13 | [review.md](batch_10/review.md) |

每个batch还提供独立gold、samples、annotations和checks。12题题干澄清的原文与新版对照见修改报告；所有原note与处理决定见changes.json。

重建：`python b_work/test_set/revisions/batch06_10_v1/build_revision.py`。替代题来源快照在replacement_sources.jsonl，构建时核对本地训练原始文件。

后续重采样训练候选时需加入新版samples的排除清单。没有修改原Step2/SFT抽样程序。
