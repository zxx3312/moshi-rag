# GPT-OSS-120B＋LoRA：900次最终运行分析

本报告分析`gpt120-lora-v1-continued`中的全部900条已保存尝试，覆盖300道独立问题和三种证据到达条件。
没有缺失记录。结果保留37条流程错误和1条音频失败，没有重试或剔除这些失败。
本报告沿用B的**近似值映射诊断评分**，不是独立人工语义评审；下面的“有据完整”均指当前B评分器的判定。

## 1. 主要结果

| 指标 | 结果 | 含义 |
| --- | --- | --- |
| 已保存运行 | 900/900；300题×3档 | 三个条件重复同一批问题，不是900道独立题 |
| 系统complete | 695/900（77.22%） | 系统认为自己规划的必要单元已完成 |
| 系统incomplete | 168/900（18.67%） | 系统结束但仍有未确认/未回答的必要部分 |
| 系统error | 37/900（4.11%） | JSON或结构化输出契约等流程错误 |
| B暂计完整且有据 | 394/900（43.78%） | 所有必要gold单元都有B认可的支持声明 |
| B不满足完整且有据 | 135/900（15.00%） | 可判定，但必要答案或支持引用不满足 |
| B完成情况未知 | 371/900（41.22%） | 待映射/复核或流程错误 |
| B必要答案值覆盖完整 | 418/900（46.44%） | 值覆盖满足参考要求，不代表引用支持也满足 |
| Unit EM / F1 | 79.02% / 79.02% | 仅在529条可评分记录上计算 |
| 运行级评分覆盖 | 529/900（58.78%） | 其余记录没有Unit EM数值 |

**结论：系统多数情况下能完成自己的处理流程，但不能将77.22%的complete或79.02%的子集Unit EM称为全900条准确率。**
当前暂计394条完整且有据，另371条未知。需要补齐独立映射/语义复核，才能更可靠地解释整体表现。
只有这一套GPT＋LoRA配置，不能据此证明它优于原GPT、Qwen或Wait-All，也不能把不同方法/覆盖的截图数字直接排成模型优劣。

## 2. 运行配置与来源

| 项目 | 设置 |
|---|---|
| 主模型 | `openai/gpt-oss-120b` |
| 判断模型 | GPT-OSS-120B＋训练的epoch-0001 LoRA |
| 判断checkpoint | `tinker://f9e9a6c1-e203-5c2c-acdd-68fe67378ca4:train:0/sampler_weights/epoch-0001` |
| LoRA作用范围 | judge、judge_repair及末尾判断复核；其他API阶段仍是原始120B |
| 数据 | B修订版eval-revised-v1；300题、三档共900trace |
| B固定commit | `ea390574eadd301354d5de46f0d28d328cca5bad` |
| 证据日程 | immediate=0秒；short=1/3秒；long=2/8秒；固定模拟检索到达 |
| 普通模型输入 | 问题、自行拆分的单元、当时已交付证据；不接收gold或未来证据 |
| 音频 | Windows TTS；play=false；音频失败记录后继续文字评估 |
| 问题超时 | 180秒 |
| B映射 | allow_value_match=true；没有把控制器unit ID直接当gold ID |
| 时序评分 | unknown；无正式语音声明起止对齐 |
| 运行版本 | a-cascade；父`c23d6ae6e7250b793c026e7ec01ae9166728f5af`＋dirty |
| 运行器源码身份 | `b652f87e3116f16619d16ba6fecc74acd36cf191b6e85e100f6a178739568af9` |

父目录`gpt120-lora-v1`在第312条因Windows TTS退出1中止。
续跑目录原样继承前312次，包括其中11次流程错误和1次音频失败；随后新增588次尝试，总计900次。
父子记录不相加成1212次，不将同一尝试重复当样本。检查了312份继承run.json与父目录字节哈希一致。
全部API调用的模型路由已核对，无判断器/主模型路由错用。Tinker远端GPU型号和作业号未提供，不能据此报告H100性能。

## 3. 系统complete与B判定为什么不同

| 系统状态 | B暂计有据完整 | B不满足 | B未知 |
| --- | --- | --- | --- |
| complete | 394 | 30 | 271 |
| incomplete | 0 | 105 | 63 |
| error | 0 | 0 | 37 |

系统按自己生成的必要单元判断完成；B按独立gold的必要单元、答案写法及标注证据集合评分。
系统complete的695条中，30条已被B判为不满足有据完整，271条未知；这些不能全部当答对。

135条已知不满足中：

- 111条必要答案值没有全部覆盖/匹配；可能是漏答、拆题目标偏差或取值不符，不能仅凭该字段区分。
- 24条必要答案值覆盖完整，但必要单元的支持/引用链未满足B条件。

371条未知中：

- 334条日志可评估，但存在尚未完成映射的声明，B暂不计算整条run的完成/Unit EM指标。
- 37条是流程错误，答案指标留空。

未知不是“模型仍在回答”，也不等于答案正确。即使核心答案看起来正确，附带声明无法映射也会让整条run待评。
反过来，错误答案若无法通过唯一值匹配，也可能进入未知。不能只凭这一表声称全部未知都来自评分程序。
grounded_complete只要求**所有必要单元**被SUPPORTED声明覆盖，并不要求每句附加话都正确；附加无依据声明另看UCR。

## 4. 声明、引用与评分覆盖

| 指标 | 结果 |
| --- | --- |
| 纳入汇总的声明 | 1831 |
| 已评分声明 | 1322（72.20%） |
| 待映射/复核声明 | 509（27.80%） |
| 已评分声明中未获支持 | 106/1322（8.02%） |
| 整体Structured UCR | null；不能用已评子集的8.02%代替 |

待评声明原因：

| 原因 | 声明数 |
| --- | --- |
| value_not_found_in_claim_text | 2 |
| claim_mapping_required | 441 |
| ambiguous_gold_value | 66 |

106条UNSUPPORTED声明的原因全部是`missing_gold_support_or_citation`。
这说明没有满足B标注的支持/引用集合，不能未经语义复核就断言106条自然语言内容全部事实错误。
与此同时，这也不能当作它们已有可靠依据；替代证据、链条遗漏或标注问题需要独立核对。

本轮所有1322条已评分声明都通过`value_guess`近似映射。
该机制主要在声明值与某一个gold单元答案/别名规范化精确匹配时才能自动对应。
因此，值不匹配或映射不明的声明可能被留在待评队列；**529条可评分子集可能存在选择偏差**，79.02%不是全面语义正确率。
没有使用embedding或另外的LLM为未知答案擅自补分，也没有修改gold别名或支持集合。

## 5. 三种证据到达条件

| 条件 | 运行 | 系统complete | incomplete | error | B有据完整 | B不满足 | B未知 | Unit可评分数 | 子集Unit EM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| immediate | 300 | 231 | 61 | 8 | 138 | 49 | 113 | 187 | 76.47% |
| short | 300 | 240 | 50 | 10 | 136 | 42 | 122 | 178 | 80.90% |
| long | 300 | 224 | 57 | 19 | 120 | 44 | 136 | 164 | 79.88% |

三档每档300次、同一批300道题。有据完整率分别为46.00%、45.33%、40.00%。
long有19次流程错误，高于immediate的8次、short的10次；这属于本次观察，不证明延迟本身导致模型能力下降。
各档Unit EM的分母不同，不宜只比较百分数。没有做置信区间或显著性推断。

## 6. 数据集与题型分组

| 数据来源 | 运行数 | B有据完整 | B不满足 | B未知 | 可评分数 | 子集Unit EM |
| --- | --- | --- | --- | --- | --- | --- |
| 2wikimultihopqa | 450 | 225 | 63 | 162 | 288 | 83.68% |
| hotpotqa | 450 | 169 | 72 | 209 | 241 | 73.44% |

| 题型（B元数据） | 运行数 | B有据完整 | B未知 | 可评分数 | 子集Unit EM |
| --- | --- | --- | --- | --- | --- |
| bridge | 387 | 199 | 141 | 246 | 85.37% |
| bridge_comparison | 105 | 36 | 46 | 59 | 69.49% |
| comparison | 348 | 125 | 170 | 178 | 73.60% |
| single | 60 | 34 | 14 | 46 | 78.26% |

## 7. 按独立问题看三档一致性

| 一个问题在几档被B暂计有据完整 | 独立问题数 |
| --- | --- |
| 0/3档 | 130 |
| 1/3档 | 43 |
| 2/3档 | 30 |
| 3/3档 | 97 |

有158道问题至少一档未知，30道问题至少一档流程错误。
“0/3档成功”不等于三档都答错，其中可能含未知或运行错误。
这些分组是重复条件下的描述，不能把900次当900个独立问题做统计。

## 8. 流程错误与控制器行为

| 终止错误 | 次数 |
| --- | --- |
| LLM did not return one valid JSON object | 24 |
| Each unit needs 1 or 2 short search queries | 3 |
| Placeholders must name explicit dependencies | 3 |
| Unit IDs must be u1, u2, ... | 4 |
| Judge must return judgments | 3 |

37次流程错误主要是JSON与结构化输出契约问题，不等同于37个已确认的事实错误。
API日志中的status=ok通常仅表示请求返回并解析为JSON，不代表后续plan/judgment schema或事实正确。
本报告不基于预留题修改prompt、训练数据、阈值或模型。

| 控制器动作 | 出现过该动作的trace数 | 动作总次数 |
| --- | --- | --- |
| Backchannel | 900 | 900 |
| Progress | 603 | 675 |
| Partial Answer | 301 | 310 |
| Final Answer | 900 | 900 |
| Correction | 0 | 0 |

| 运行事件 | 出现过的trace数 |
| --- | --- |
| facts_rejected | 67 |
| draft_rejected | 33 |
| generation_fallback | 100 |
| semantic_review_requested | 192 |
| protocol_validation_failed | 81 |

事实核验拒绝可能是在拦截错误，不能将每次拒绝直接算作新错误。
表达回退不一定改变事实。Partial出现次数也不证明它一定早于Wait-All或内容更可靠，需要配套时序/对照分析。
这些事件可在同一次运行共存，不能简单相加当失败数。

## 9. API耗时与音频

| 阶段 | 调用数 | 中位耗时（秒） | 状态计数 |
| --- | --- | --- | --- |
| decompose | 900 | 2.218 | ok=900 |
| plan_review | 900 | 2.422 | ok=900 |
| judge | 1343 | 2.110 | ok=1319, error=24 |
| judge_repair | 7 | 2.359 | ok=7 |
| generate | 1104 | 1.156 | ok=1104 |
| verify | 1104 | 1.546 | ok=1104 |
| feedback_generate | 2436 | 1.078 | ok=2348, cancelled=87, error=1 |
| feedback_verify | 1999 | 0.969 | ok=1719, cancelled=275, error=5 |

文本控制流程墙钟中位数为11.711秒，平均12.594秒。
它包含证据等待、API和控制器工作，测到最后音频队列排空之前；不是单独LLM推理时间，也不是完整声学回答时间。
反馈请求的cancelled经常来自对话结束/状态切换，不全部是接口故障。不同API调用可能并发，耗时不能相加当整题延迟。
B的TTFR、TTFGI、TTCA全部仍为unknown，没有用文本时间或WAV长度补造正式时序分数。

音频状态899成功、1失败。检查了899份非空WAV文件的头部/可读性，没有试听，不评价自然度或实际播报准确性。
第312条音频失败及文字complete状态均被保留；续跑继续策略没有把它改成音频成功。

## 10. 阅读结论与后续边界

1. 本次完成全部900次尝试，无missing；系统complete695次，但这只是系统内部完成状态。
2. B当前暂计394次完整且有据，135次不满足，371次未知；未知比例41.22%，评分覆盖仍是重要限制。
3. 529条可评分记录的Unit EM为79.02%，不能宣称“全900准确率79%”。
4. 已评分声明中106条不满足标注支持/引用条件；还有509条待复核，整体UCR保持null。
5. 37条结构化输出错误与168条系统incomplete应分别报告，不把流程完成、答案正确和证据支持混为一谈。
6. 当前只有GPT＋LoRA一套配置，没有同条件原始GPT或Wait-All对照；不能将效果归因于LoRA训练收益。
7. 本报告只分析冻结运行，不据此对预留集调参；额外映射/语义复核应单独记录身份、规则和源日志hash，并保留原评分。

## 11. 文件与可复现性

- [原始B评分摘要](b_eval/summary.md)、[原始逐条评分](b_eval/run_scores.jsonl)、[原始待复核队列](b_eval/review_queue.jsonl)。
- [本次离线复算摘要](analysis_final900_20261119T000603Z/b_eval_recomputed/summary.md)：与原始运行级/声明级/待复核评分逐条一致。
- [900条逐次汇总CSV](analysis_final900_20261119T000603Z/per_run.csv)：含状态、指标、到达条件和错误信息，不含问题或答案正文。
- [聚合指标JSON](analysis_final900_20261119T000603Z/metrics.json)、[分析与原文件hash清单](analysis_final900_20261119T000603Z/manifest.json)。
- [全部文字/模型调用示例位置](samples/0001/run.json)；每个样本`audio/responses.txt`含当次全部说话文本，`audio/response.wav`为音频。
- 生成脚本位于`eval gpt900/artifacts/reporting/final900_report.py`，不会调用模型或改写原评分。

原运行器源码身份来自manifest，完整方法/数据身份保留在原`source-manifest.json`、`manifest.json`、`continuation.json`中。
对父子目录原始预测、事件、文本/音频索引和B评分文件保存SHA256，并在报告完成后复核未变；不对所有音频二进制做全文件哈希。
本次只生成派生报告/汇总/离线复算，不修改模型、prompt、控制器、B gold/scorer或原始结果，无新模型/API/TTS/训练调用。
离线复算与清单校验退出0；无功能代码修改，未重跑功能测试。共享文档待用户提交同步，无commit/push。

## 附录：37次流程错误位置

| 样本编号 | 到达条件 | 流程错误 |
| --- | --- | --- |
| [0003](samples/0003/run.json) | long | LLM did not return one valid JSON object |
| [0127](samples/0127/run.json) | immediate | Each unit needs 1 or 2 short search queries |
| [0128](samples/0128/run.json) | short | Each unit needs 1 or 2 short search queries |
| [0129](samples/0129/run.json) | long | Each unit needs 1 or 2 short search queries |
| [0183](samples/0183/run.json) | long | Placeholders must name explicit dependencies |
| [0192](samples/0192/run.json) | long | Placeholders must name explicit dependencies |
| [0201](samples/0201/run.json) | long | LLM did not return one valid JSON object |
| [0235](samples/0235/run.json) | immediate | LLM did not return one valid JSON object |
| [0286](samples/0286/run.json) | immediate | LLM did not return one valid JSON object |
| [0287](samples/0287/run.json) | short | LLM did not return one valid JSON object |
| [0311](samples/0311/run.json) | short | LLM did not return one valid JSON object |
| [0322](samples/0322/run.json) | immediate | LLM did not return one valid JSON object |
| [0350](samples/0350/run.json) | short | Unit IDs must be u1, u2, ... |
| [0352](samples/0352/run.json) | immediate | Unit IDs must be u1, u2, ... |
| [0384](samples/0384/run.json) | long | LLM did not return one valid JSON object |
| [0426](samples/0426/run.json) | long | Judge must return judgments |
| [0437](samples/0437/run.json) | short | LLM did not return one valid JSON object |
| [0464](samples/0464/run.json) | short | Unit IDs must be u1, u2, ... |
| [0465](samples/0465/run.json) | long | Unit IDs must be u1, u2, ... |
| [0466](samples/0466/run.json) | immediate | LLM did not return one valid JSON object |
| [0468](samples/0468/run.json) | long | LLM did not return one valid JSON object |
| [0492](samples/0492/run.json) | long | LLM did not return one valid JSON object |
| [0502](samples/0502/run.json) | immediate | LLM did not return one valid JSON object |
| [0509](samples/0509/run.json) | short | LLM did not return one valid JSON object |
| [0609](samples/0609/run.json) | long | LLM did not return one valid JSON object |
| [0613](samples/0613/run.json) | immediate | LLM did not return one valid JSON object |
| [0614](samples/0614/run.json) | short | LLM did not return one valid JSON object |
| [0621](samples/0621/run.json) | long | LLM did not return one valid JSON object |
| [0687](samples/0687/run.json) | long | LLM did not return one valid JSON object |
| [0831](samples/0831/run.json) | long | Judge must return judgments |
| [0843](samples/0843/run.json) | long | Judge must return judgments |
| [0878](samples/0878/run.json) | short | LLM did not return one valid JSON object |
| [0879](samples/0879/run.json) | long | LLM did not return one valid JSON object |
| [0881](samples/0881/run.json) | short | Placeholders must name explicit dependencies |
| [0891](samples/0891/run.json) | long | LLM did not return one valid JSON object |
| [0894](samples/0894/run.json) | long | LLM did not return one valid JSON object |
| [0897](samples/0897/run.json) | long | LLM did not return one valid JSON object |
