# Judge SFT 数据集（sft-v0）问题清单

检查日期：2026-11-03
检查对象：`b_work/step4/` 下的 `gold_sft.jsonl`（300 题）、`sft/sft_train.jsonl`（1,991 条）、`sft/sft_dev.jsonl`（486 条），以及生成它们的脚本和文档。
对照的要求：`sft_plan.md`、`b_work/step1/schema.md` 第 4 节、`b_work/step1/labeling_guide.md` 1.1 节、`b_work/step2/README.md`，以及 A 组 `a_work/unit_schema.md` 5.5–5.6（`a-prompt-judge` 分支，提交 `806e410`）。
审核进度（2026-11-03 更新）：31 道明确问题题已从最终 gold 移除并用现有候选替换。当前标注池共 341 条记录，其中 300 条为 `reviewed`、41 条为 `reject`；全部 300 条通过记录进入最终 gold。最终来源为 153 道 2Wiki、147 道 Hotpot，split 仍为 243 train / 57 dev。

## 结论

脚本层面的硬性要求都满足：

- 题目只来自官方 train 集，和 debug 的 20 题、预留评测的 300 题在 ID 和归一化问题文本上都没有重叠。
- 每道题的所有样本都只在 train 或 dev 其中一边。
- 输入 prompt 由 A 组的 `judge_messages()` 生成，目标格式符合 `JUDGE_SCHEMA`。
- 和 A 组 `OracleJudge`、`derive_conclusion` 的交叉检查为 0 处不一致。
- 引用的证据在当时都已经可见，UNRESOLVED 的目标都不带取值和引用。

人工审核状态问题已经解决；正式训练前仍需处理或明确接受以下主要风险：

1. few-shot 示例里的回复会被反复当作训练目标（问题 2）。
2. 不同批次之间仍存在标注标准一致性风险（问题 3）。

严重程度说明：

- **P0**：训练前必须解决。
- **P1**：会影响训练或评测结果的可信度，应在正式版本之前解决。
- **P2**：文档、可复现性和小的偏差。

---

## P0：训练前必须解决

### 问题 1（已解决）：原 28 道进一步审核题

- **处理**：原 28 道复核题中，21 道明确问题题已经替换；另外 10 道不在旧清单中的明确问题题也已替换，共替换 31 道。原清单剩余 7 道规则/措辞边界题继续保留。当前为 300 条 `reviewed`、41 条 `reject`；附录 A 和 `review/flagged_review_28.md` 仅作为历史复核材料。
- **原 28 题按复核原因分类**（复核表 `review/flagged_review_28.md`，每题的原因在 `review/flagged_reasons.json`）：

  | 分类 | 题数 | 需要做的决定 |
  |---|---|---|
  | 原数据可能连错了实体 | 3 | 核实源答案是否可信，不可信就退回 |
  | 规则待定 | 8 | 先在组内定规则（见问题 3），定完后标签可能翻转 |
  | 靠数列表项来比较 | 3 | 和已退回的 2Wiki 同类题统一：都退回或都保留 |
  | 证据偏弱 | 4 | 逐题判断这些句子算不算明确陈述 |
  | 问题本身有瑕疵 | 7 | 逐题决定保留、修改或退回 |
  | 证据有多种解读 | 2 | 确认现在的解读可以接受 |
  | 已处理，待确认 | 1 | 确认 “probably the son of” 改为没有证据 |

- **验证**：31 道旧题均不在新 gold，31 道指定替换全部入选；`gold_sft_review.md` 中 300 题均显示 `reviewed`。`sft_train.jsonl` 的 243 题和 `sft_dev.jsonl` 的 57 题与 gold split 完全一致，A 组代码交叉检查为 0 处不一致。
- **仍缺少的记录**：没有找到双人独立标注和一致率统计（`sft_plan.md` 第 5 步）。若实际做过，应补充记录；若没做，这仍是一项独立质检任务，但不再影响当前 `reviewed` 状态。

### 问题 2：few-shot 示例的回复会被当作训练目标重复训练

- **现象**：每条样本的 `messages` 里有 4 个 assistant 回复，结构是 system + 3 组 few-shot 问答 + 本题的 user 和 assistant。前 3 个 assistant 回复就是 A 组 prompt 里固定的虚构示例，2,419 条样本完全相同。
- **影响**：常见的 SFT 训练要么对所有 assistant 回复计算损失，要么对整段序列计算损失。无论哪种，同样的 3 个示例回复都会被训练 2,419 次，模型容易记住示例而不是学会判断。此外每条样本要多出约 2.5k 字符（约 600 token）。
- **建议**（需要和 A 组商定）：
  - 如果 LoRA judge 推理时不带 few-shot：用 `build_sft.py --no-examples` 重新生成。
  - 如果推理时要带 few-shot：训练时只对最后一个 assistant 回复计算损失，并在数据说明里写清楚。

### 问题 3：不同批次之间的标注标准不一致

同一类情况在不同批次里曾被标成不同标签。下表保留替换前的历史例子；其中多道明确问题题已在31题替换中移除，剩余边界仍需按最终规则统一回扫。

| 情况 | 不一致的地方 | 例子 |
|---|---|---|
| 作品列表里提到片名，算不算“导演”的证据 | 有的批次算，有的批次不算 | 算：Catherine Hardwicke 1（2Wiki 05）。不算：Robin Campillo 1 “known for his work on”（2Wiki 01）、Jiří Menzel 7 “his dark comedy”（2Wiki 03） |
| 国籍、国家取值写国名还是形容词 | 147 个国籍/国家类 unit 里，78 个写国名，69 个写形容词 | `2wikimultihopqa_254e9ee2…` 用 “Canada”，2Wiki 05 的 `ea80456…` 用形容词 |
| 同一种关系的描述措辞 | “nationality of” 52 个，“country descriptor of” 6 个 | 运行时 A 组的拆题器只会用其中一种写法 |
| English 和 British 算不算同一个值 | 已统一为可互作别名 | `2wikimultihopqa_972b911e…` 和 `2wikimultihopqa_3a2fe93e…` 均按等价值处理 |
| 预设规则的适用范围 | 已接受问题明确点名的候选/条件；恰好两个候选且预设唯一答案时，可由明确排除一方确定另一方 | `hotpotqa_5ade1b77…` 由 Foo Fighters 的 1994 年证据排除后确定 Goon Moon，并标 `by_presupposition` |
| “Which, or both” 这类问法算不算点名候选 | 起草者按 “both” 题处理，没有用预设 | `hotpotqa_5a8661f8…` |
| 从同一句的其他内容推出来的值 | 被当作明确陈述接受了 | `hotpotqa_5ae0c1c2…`：用 “all-Finnish line-up” 推出 Kotipelto 是芬兰人 |
| 推测语气（probably、son or nephew） | 2Wiki 05 原本算作证据，统筹审核时改成了不算；2Wiki 04 的 “son or nephew” 不算 | `2wikimultihopqa_812e515c…`、`2wikimultihopqa_2f75b462…` |
| 靠数列表项来比较的题 | 已限定为“文档明确列出的项目数量”，不声称完整枚举现实中的全部项目 | `hotpotqa_5ac25035…` 统一为电影职务数 7 比 1；`hotpotqa_5a7f66cb…` 统一为 creator/designer 数 2 比 1；原 `5a84fd2a…` 已替换 |

- **影响**：除了标签矛盾，取值写法不统一还会让模型输出的 `value` 格式不稳定。
- **与审核进度的关系**：`labeling_guide.md` v1.2 已经采纳了预设规则（Exception 3），原 28 道待审题现已完成人工审核。不过，上表各行的边界仍未全部写进 guide；若组内规则继续调整，仍应统一回扫相关记录。
- **建议**：
  - 先在组内（含 A 组）把上表每一行定成明确的规则，写进 `labeling_guide.md`（v1.3）。
  - 再按新规则统一修改相关记录。
  - 取值格式建议统一为：问“国家”给国名，问“国籍”给形容词，另一种写法放进 `aliases`。

---

## P1：影响可信度，正式版本前应解决

### 问题 4（已解决）：必要 unit 全证据不可达

- `2wikimultihopqa_3a2fe93e…` 已按 English/British 等价处理，Mavis Batey 句 0 成为显式支持。
- `hotpotqa_5ade1b77…` 已按“两个点名候选且预设唯一答案”规则处理：证据明确排除 Foo Fighters 后，结论 Goon Moon 以 `by_presupposition: true` 支持。
- 重建后 300 题的 necessary unit 在全证据下全部可达，不可达计数为 0。

### 问题 5：SFT 的预设支持集还没有被 A 组 Oracle 完整采纳

- **现象**：
  - `schema.md` v1.3 已加入 gold-side `by_presupposition` 标记；当前 15 个使用 `presupposition_sets` 的 Gold unit 均已静态标记 `by_presupposition: true`。
  - A 组的 `OracleJudge` 不读取 `presupposition_sets`。交叉检查只能跳过依赖预设的 unit，曾经因此出现过 1 处“不一致”（`hotpotqa_5addad5c…` 的 u2）。
  - A 组 `derive_conclusion` 只实现“直接确认赢家”，还未实现本轮批准的“明确排除两个候选中的输家”。SFT builder 已把新规则追加到 system prompt，并只对这一已知扩展跳过 A 代码交叉检查；其余交叉检查仍为 0。
- **影响**：
  - A 组用 `eval_judge.py` 和 OracleJudge 评估时，对预设类 unit 的判断会和 SFT 目标不一致。
  - debug 集和 SFT 集的规则不同，开发阶段的诊断结果会有偏差。
- **建议**：
  - 通知 A 组让 `OracleJudge` 支持 `presupposition_sets`。
  - 评估时按 schema v1.3 对 `by_presupposition: true` 的 unit 单独统计。

### 问题 6：可能漏标的备选证据

- **现象**：替换前自动检查曾找出 127 个“疑似漏标”的 unit，分布在 108 题中。31 题替换后该旧统计已失效，需要重新运行启发式检查；当前硬校验和 A 组交叉检查均为 0 错误。
- **抽查结果**：抽查前 40 个，大多数是**正确地没有采用**的句子，例如用电影的国别推断导演国籍，或者句子里只是同时出现了这些名字。少数属于问题 3 里的边界情况，例如 Roberto Rossellini 1 “contributing … with films such as Germany, Year Zero”。
- **影响**：真正漏标的地方会产生“应为 SUPPORTED 却标成 UNRESOLVED”的错误标签，让 judge 变得过度保守。
- **建议**：确认人工审核是否逐一覆盖了这 127 个启发式候选；若没有，按名单补查。可以考虑把该检查加入 `build_sft.py` 的统计输出，方便导出完整名单。

### 问题 7（已解决）：expected_answer 中的占位值

- **原问题**：`hotpotqa_5add999a…` 和 `hotpotqa_5ae015e0…` 的 context 分别缺少 Glenn Danzig 的音乐生涯长度和 The World Without US 的片长，因此使用了错误的 `unknown` 占位值。
- **处理**：两题已标记为 `reject`，分别用同为 HotpotQA comparison/train 的 `hotpotqa_5ab3c3b1…`，以及 comparison/dev 的 `hotpotqa_5ae29b61…` 替换。新题的两个比较值都有显式证据，重建后 gold 中已无 `unknown`。
- **备注**：原先使用 `none` 的 `hotpotqa_5a84fd2a…` 已在本轮因不当 `by_omission` 被替换；当前 gold 中仍无 `unknown` 占位值。

### 问题 8：部分 prompt 过长

- **现象**：每条样本的总长度中位数约 8.1k 字符，P99 约 14.6k，最长 44.8k（约 11k token）。超过 16k 字符的有 15 条，其中 8 条来自同一题 `2wikimultihopqa_8f49c34c…`。
- **影响**：如果训练时 `max_seq_length` 设得比较小，这些样本会被截断，截掉的可能是证据甚至目标回复，标签就会和输入对不上。
- **建议**：确定训练用的最大长度。超长样本要么丢弃，要么换题，不要截断。可以在 `build_sft.py` 里加一个长度上限参数。

### 问题 9：计划中的几项质检没有做

- **现象**：`sft_plan.md` 第 8 步要求的“人工通读 50 条随机样本”和“用当前 PromptJudge 在 `sft_dev.jsonl` 上跑基线”都还没做。后者需要 GPU 和 A 组的模型服务。
- **建议**：人工审核完成后补做。PromptJudge 基线可以请 A 组用 `eval_judge.py` 跑一次。

---

## P2：文档、可复现性和小的偏差

### 问题 10：题型配比和 train/dev 比例略有偏差

- **现象**：替补是按候选顺序补位的，没有按题型补，所以：
  - 2Wiki 的 comparison 是 36 题（目标 38），compositional 和 inference 各 38 题（目标 37）。
  - HotpotQA 的 bridge 是 76 题、comparison 是 74 题（目标各 75）。
  - train/dev 是 243/57（计划 240/60）。
- **建议**：影响不大。如果要严格对齐评测集的配比，可以把 `build_gold_sft.py` 的替补规则改成“同数据集、同题型的下一道替补”。

### 问题 11（已解决）：单 unit bridge/inference 结构

- 原来剩余的 5 道单-unit 记录已全部按 schema 4.3 拆成两跳：中间 unit 为 `necessary: false`，最终 unit 为 `necessary: true` 并依赖中间 unit。
- 当前 Gold 中 bridge/inference 单-unit 记录为 0。

### 问题 12：README 里有不准确的地方

- **现象**：
  - README 说完整的哈希值在 `prepared/sft_manifest.json` 里，但 manifest 只记录了转换后 JSON 的哈希，没有两个 parquet 文件的哈希。
  - 下载步骤缺少创建 `hotpot_train_parquet/` 目录的命令。
- **建议**：把 parquet 的完整哈希写进 manifest 或 README，并补上 `mkdir -p`。

### 问题 13：A 组代码的版本没有固定

- **现象**：`build_sft.py` 默认读取 `origin/a-prompt-judge` 分支的最新提交。A 组一更新 prompt，重新构建出的数据就会悄悄变化。实际使用的提交号会记录在 `sft_stats.json` 里，但默认值本身不固定。
- **建议**：发布正式版本时用 `--a-ref 806e410…` 固定提交号，或者把默认值改成具体的提交号。

### 问题 14：Git 状态

- **现象**：
  - step1、step3 的规则更新已经在本地提交（`6f6665d`），`b_work/step2/raw/` 也已经不再出现在未跟踪文件里。
  - `b_work/step4/` 还没有提交，其中 `sft/` 有 23MB。
  - 本地分支相对远程领先 1 个提交、落后 1 个提交（远程是 Q1–10 的 gold），还没有 push。起草时有些子代理读的是远程版本的 `gold_annotations.json`，有些读的是本地版本，参考的风格示例不完全相同。
- **建议**：提交 step4，`git pull --rebase` 合并远程提交（`b_work/step3/README.md` 第 3 行会冲突，保留 v1.3/v1.2 那一行），重新生成 debug 集的 gold 和 trace，然后 push。

### 问题 15：已知的设计局限（不是错误，但要写进说明）

- **没有 `CONTRADICTED` 目标。** 证据有冲突的题都被退回了，所以训练出的 judge 几乎不会输出这个标签。
- **训练用的是 gold 的 unit 描述，不是拆题器生成的。** 运行时的措辞可能不同。
- **训练用的到达顺序和评测用的时间表不同。** 训练时每秒到达一篇文档，顺序随机；评测时文档分两批到达。这些训练用的时间表不能用来报告延迟结果。
- **原数据集里的错误关联被保留了下来。** 例如 Bharathan 1998 年去世，却被当作 2007 年电影的导演；Maurice Campbell 生于 1919 年，却被当作 1921 年电影的导演。judge 只根据文本判断，所以这不影响标签本身，但这些题不适合用来评估答案是否正确。

---

## 建议的处理顺序

1. 补上双人标注和一致率记录，或者补做（问题 1、9）。
2. 组内（含 A 组）继续确定问题 3 表格里尚未裁决的规则，并同步 A 组对“排除输家”预设的实现（问题 5）。
3. 按最终规则统一回扫全部 300 题中的取值格式、描述措辞和疑似漏标证据（问题 3、6；问题 4、7、11 已解决）。
4. 和 A 组确定 few-shot 和最大长度的处理方式，重新生成 SFT 数据（问题 2、8、13）。
5. 补做其余质检（问题 9），修正 README 的剩余可复现性说明（问题 12），合并远程提交后 push（问题 14）。

---

## 附录 A：已完成进一步审核的 28 题（历史名单）

这些题曾因 notes 中出现 review、flag for、borderline、open point、caveat、unclear、weakest、may prefer、mismatch、may decide 之一而被列入进一步复核。现已完成人工审核；逐题的原复核原因和材料仍见 `review/flagged_review_28.md`。

2wikimultihopqa_2f75b4620bb011ebab90acde48001122, 2wikimultihopqa_3118082408e011ebbda1ac1f6bf848b6, 2wikimultihopqa_3a2fe93e0bda11eba7f7acde48001122, 2wikimultihopqa_3addeb19089411ebbd75ac1f6bf848b6, 2wikimultihopqa_4f103f2e0bdb11eba7f7acde48001122, 2wikimultihopqa_812e515c0baf11ebab90acde48001122, 2wikimultihopqa_972b911e087f11ebbd6cac1f6bf848b6, 2wikimultihopqa_a73a3fc80bdc11eba7f7acde48001122, 2wikimultihopqa_b87b12700bdd11eba7f7acde48001122, 2wikimultihopqa_f48d9c60093011ebbdaeac1f6bf848b6, hotpotqa_5a72253f55429971e9dc92e5, hotpotqa_5a745a8755429979e288291e, hotpotqa_5a75b40f5542992d0ec05fe6, hotpotqa_5a7f66cb55429969796c1a32, hotpotqa_5a7fab3a5542995d8a8ddeea, hotpotqa_5a84fd2a5542994c784ddabb, hotpotqa_5a8661f85542991e7718162b, hotpotqa_5a8af03c55429950cd6afc19, hotpotqa_5ab298ff554299340b52552a, hotpotqa_5ab5b95d554299637185c5f8, hotpotqa_5ab6a56d554299110f219a46, hotpotqa_5ac250355542992f1f2b384b, hotpotqa_5ac561725542993e66e823ad, hotpotqa_5adcdfe05542992c1e3a2448, hotpotqa_5adde7085542990dbb2f7f01, hotpotqa_5ade1b7755429975fa854e55, hotpotqa_5ae0c1c25542993d6555ec43, hotpotqa_5ae1fe0b5542997283cd2317

## 附录 B：当前必答 unit 永远得不到支持的题（0 题）

无。

## 附录 C：单 unit bridge/inference 记录（0 题）

原有 5 题已统一为两跳结构。
