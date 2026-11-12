# 剩余工作计划

本文列出到论文初稿的工作、依赖、完成标准和运行记录。实验定义见 `experiment_spec.md`。
D 编号对应 spec 第 11 节。一次只做一步；只做部分就标“进行中”。

截止日期：待用户填写学期结束日期、目标会议截稿日期。
最后核对：2026-11-12。当前任务是**安排下述六项工作并建立对应分支**；
本次不执行模型实验、预留集最终评估或人评上传。
**用户自行提交。助手不 commit、不 push，不自行创建其他工作区或仓库副本。**

## 下一轮六项工作的执行顺序（2026-11-12）

用户列出六项工作；按依赖调整为 **原第 1 → 2 → 6 → 4 → 3 → 5 项**。
先处理标签与评分，再做 Wait-All 对照和开发参数比较，之后冻结并最终评估，最后交付人评音频。
参数选择在最终评估前完成；不能用预留集结果反向选阈值或修改方法。
这是一份实施排期，不代表新指标、标签规则或参数已经获全组批准。

本轮工作分支为 `a-eval-refinement`，从原工作区 `a-cascade` 的
`c23d6ae6e7250b793c026e7ec01ae9166728f5af` 创建并切换。
切换前后已核对暂存与未暂存 diff 指纹，既有修改完全保留；没有 stash、commit、push 或新建工作树。
后续代码按 A 的流程集成到 `a-method-integration`；共享计划仍待用户安排同步到 main。

| 执行序号 | 对应用户项 / 现有步骤 | 工作内容 | 开始条件 | 完成标准与产物 | 当前状态 |
|---|---|---|---|---|---|
| R1 | 原 1；A4、D14/D15 | 研究 `by_omission` 与 `by_presupposition` 的组合 | 用户已确认这两种标记 | 组合情形表、反例和候选规则；A/B 确认语义后，A 实现与 B gold/evaluator 口径一致；适用回归通过 | 待开始；本次只完成含义确认与排期 |
| R2 | 原 2；A2、B4、D6/D10/D11 | 阅读 Full-Duplex-Bench 和 TurnBench，制定适合自由回答的评分候选方案 | R1 的问题分类已梳理；两篇论文已确定 | 原文和官方 scorer 对照表；区分语义正确性、证据支持、交互检测和自然度；说明缺失、别名、矛盾、纠错与分母；经 A/B 确认后再改评分 | 待开始；只核对论文身份与摘要，未完成细读 |
| R3 | 原 6；A5/A6、D4/D9 | 与 Wait-All 做公平的配对诊断 | R1/R2 口径可用于开发评分，待复核映射有处理方案 | 相同 trace、硬件和计时下的质量/覆盖/TTFGI/TTCA 表；区分策略与生成差异；是否增加 Wait-All 先 judge 的消融由 D9 决定 | 待开始 |
| R4 | 原 4；A3、D2/D3 | 开发数据上的参数对比 | R3 的对照可比，计时和失败记录可靠 | 参数候选清单、扫描结果和成本；人确认选定配置并记录到 spec；调参只用获准开发数据 | 待开始；不预设扫描数值 |
| R5 | 原 3；P1、B1/B2/B4、F1 | 冻结后用约定的完整评测数据跑全部已定配置 | R1–R4 验收、相关 D 项冻结、数据验收、用户明确最终运行 | 冻结代码/数据/模型/配置及 hash；完整运行清单、失败和缺失记录；固定 evaluator 评分及配对汇总 | 未开始；完整数据范围尚待确认，不读取预留题 |
| R6 | 原 5；S1、C2 | 整理并上传语音文件，交 C 组人评 | 语音链路验收；正式交付采用冻结配置与预先约定的人评方案 | 配对音频、匿名编号、索引、版本/hash、评分表和上传链接；C 确认接收 | 待开始；上传位置与人评方案待 C 确认 |

### R1：特殊标记组合要回答的问题

用户已确认指 `by_omission` 和 `by_presupposition`。它们是判断依据标记，
不是在 SUPPORTED / UNRESOLVED / CONTRADICTED 之外新增两类标签。
先用虚构样例和获准 debug/SFT 分析，分别处理：

- 同一单元同时涉及两种依据，是否允许两个标记同时为 true，还是只记录实际采用的路径。
- 一个依赖单元按 omission 支持，结论再通过 presupposition 提前成立的情况。
- 二选一、双方是否都满足、共同属性和日期比较能否使用相同规则；不能把它们混为一类。
- 明确支持、缺省否定、问题预设和冲突证据相遇时如何处理；证据未到时不得提前推定。
- gold 的 `support_sets` / `presupposition_sets`、运行时 judge 与 evaluator 如何表达同一条依据。

本轮先产出候选与反例，不直接决定优先级或更改“已定”规则。
A 不修改 B 的 gold 或 evaluator；需要的接口变化形成清单交 B 对齐。

### R2：论文对象与评分范围

用户指定的论文已核对为：

1. Lin et al. (2025), [Full-Duplex-Bench: A Benchmark to Evaluate Full-duplex Spoken Dialogue Models on Turn-taking Capabilities](https://arxiv.org/abs/2503.04721)，
   [官方代码](https://github.com/DanielLin94144/Full-Duplex-Bench)。按用户引用核对该论文对应版本，不能直接用仓库后续版本替代。
2. Jiang et al. (2026), [TurnBench: A Multi-Domain Benchmark for Turn-Taking Dynamics in Spoken Dialogue](https://arxiv.org/abs/2608.25218)，
   [官方代码](https://github.com/SesameAILabs/turnbench)。

从摘要看，两者分别关注全双工交互行为与 end-of-turn / interruption 检测。
本项目应借鉴它们的交互评价，但自由回答的事实正确性与“决策时有无证据”仍需单独适配。
不能把检测准确率直接当作回答正确率，也不能假定论文已经提供适用本任务的语义 scorer。

现有 B evaluator 已有规范化和 gold 别名匹配，并非未经处理的逐字比较；
当前不足包括等价改写、关系是否对应问题、正文未登记事实、纠错和 claim 映射。
下一步读原文指标定义、官方实现、判定窗口、分母和缺失规则，逐项列出可借鉴部分与不适用部分。
保留 EM/F1 作为可复现的参考，同时提出语义判定及人工复核方案；
若使用模型辅助判定，需核对人工一致性并遵守现有 Qwen3/本地部署约束。
任何评分规则变更先由人确认，不为了提高当前分数增加别名或改变 gold。

### R3–R6 的共同前置条件

- 开发诊断先复核 v7 待定映射，分别报告正确性、支持性、覆盖和延迟。
  原 Wait-All 保留；是否新增相同 judge/生成方式的消融仍属于 D9，不能偷偷替换 baseline。
- 参数比较前核对回放终止边界、失败调用耗时、声明时间估计和串行/并发成本。
  未修复或未验收的计时问题不能当作真实收益。候选阈值范围待人确认。
- ASR/Piper smoke 的故障修复、TTS 校准与音频对齐作为语音交付前置工作。
  可在方法开发阶段准备 debug 音频包供流程检查，但不当作正式人评结果。
- “完整数据”具体是否包括预留 300 题、额外 multipart 及 C 外部对照，需要先列清单。
  train/dev/debug 不合并为最终评测集。正式结果按现有 spec 用 H100。
- 按 `CLAUDE.md` 的数据条款，含预留集的 F1 必须在冻结后、用户明确表示“这是最终运行”时执行。
  当前排期不解除开发期间禁读要求，也不授权启动最终 GPU 作业。
- 在正式运行前约定人评题目选择、策略、维度、评分人数和匿名随机化办法，避免按结果挑音频。
  上传前准备可审阅的包与 manifest；目的地、C 的接收方式待确认，本次不发送文件或消息。

本次交付范围为上述排期、已创建分支和文档更新。六项研究工作均未被标为完成。
尚未提交新 GPU 作业、访问预留数据、改变实验定义或上传音频。

## 现状与证据

| 部分 | 当前状态 | 依据与限制 |
|---|---|---|
| 异步检索诊断 | 已有历史实验记录 | `experiments/async_retrieval_latency/`；旧数字需补齐运行元数据后引用 |
| MoshiRAG 可控性 | Wait / Progress / Final 有开发结果，Partial 不可靠 | `a_work/moshirag_control/FINDINGS.md`；单种子、第二人复核未完成 |
| A 控制器与 judge | 四个规则 baseline、Evidence-Aware、prompt / LoRA / oracle、模型拆题与生成 | 远端 `a-answer-gen` @ `9fb9adc`；不等于最终配置已冻结 |
| A v5 回放 | 本地记录显示已运行并经固定 B evaluator 评分；部分映射由助手辅助复核 | `a_work/evaluation_notes.md`（未提交）；仍有待复核项，不能当整体 UCR 或独立人工复核 |
| A 后续优化 | v6 LoRA 与两轮 v7 已完成；2026-11-12 补齐固定 B evaluator 评分，均退出 0、校验问题 0 | v7 主方法已确认完整 Prompt 37/60、LoRA 42/60；待复核声明 8/10，整体 UCR 为 null；详见 A evaluation notes |
| A ASR / TTS | 本地有 Whisper、Piper、调用回放和 smoke 脚本；作业 12308419 已失败，退出 1 | A100；ASR 报 No CUDA GPUs are available；主时间轴仍模拟，S1 未完成，见后文结束状态记录 |
| B 数据 | debug gold / trace、SFT 已有；预留 gold 有新增草稿提交 | B `638027b` 的提交元数据；未读取任何预留题、gold、trace，未验收 B1 |
| B evaluator | 有结构化声明评分、校验、映射复核队列和测试；A 本地已接入真实回放 | B eval README、A evaluation notes；语义抽取、纠错和 CI 仍待做 |
| C 外部对照 | 新增按三档延迟的 debug 交付 | C `10d2394` 的 `trace-v1-debug-12189299/README.md`；执行检查通过不等于正式评分，音频对齐和听评待做 |
| 共享文档 | 三份正文已在原仓库整理，AGENTS 与 CLAUDE 共用规则；等待用户提交和后续同步 | 当前 `a-cascade` 工作区；还没有在 main 或各组分支交付 |
| Proposal | 仓库和当前工作目录未找到 PDF | 约定路径 `docs/proposal.pdf`；已向用户询问位置，不编造或替代 PDF |

本表只从获准的开发说明、接口、提交元数据核对进度。
原稿中“v5 尚无真实回放”“B 预留集只有题目”“C 尚未按三档延迟运行”已过时，
但相应步骤的全部验收标准仍未满足。

### 分支快照

远端引用已通过 `git fetch --all --prune` 更新。
`main` 与 `origin/main` 一致；原工作区保留在 `a-cascade`，没有覆盖未提交修改。

| 分支 | 核对时 commit | 说明 |
|---|---|---|
| `origin/main` | `73b578a1df477dfa90476021e75adc41714bc891` | 共享文档尚未提交到此分支 |
| `origin/a-method-integration` | `5cc824f` | A 的 PR 集成目标，PR #1、#2、#4 已合并（原记录） |
| `origin/a-answer-gen` | `9fb9adc316d478362c5443948ef53a4645b8fae7` | 相对集成分支的后续 judge / LoRA / generation 工作尚待集成 |
| 本地 `a-cascade` | `9fb9adc` + dirty | 已有用户的级联、评估和测试改动；不得当作上述干净 commit 的行为 |
| `origin/b-data-eval` | `638027bf35c29428742c1e42aabf9243a08466d8` | 最新提交说明新增预留 gold 草稿；只查看提交元数据 |
| `origin/c-external-baselines` | `10d2394dd559b842bc5df01134536946038ddfa7` | 新 debug trace 交付 |

A 本地未提交代码包括 `cascade.py`、`eval_with_b.py`、ASR/Piper 脚本与测试等。
这些工作不是本次整理新增的实验实现，已有 README、unit schema 和代码差异均保留。

## 步骤

状态：未开始 / 进行中 / 完成。没有独立验收证据时不标完成。
plan 是分工，不是自动执行 commit、push、PR、合并、tag 或 GPU 运行的授权。

### 阶段 0：整理与冻结定义

| ID | 任务 | 负责 | 依赖 | 完成标准 | 状态 |
|---|---|---|---|---|---|
| P0 | 整理 CLAUDE/AGENTS、spec、plan 与 proposal；用户提交共享文档到 main，各组后续同步 main；A 后续将 answer-gen 工作经 PR 集成，核对 README | A | — | PDF 在位；三组看到共享文档；A 测试通过；分支/README 不再误报进度 | 进行中：文档已整理、测试已跑；PDF 缺失；未 commit、PR、合并或同步其他分支 |
| P1 | 三组复核 spec，优先 D1、D13、D14、D15；确认已有草稿是否遵守冻结顺序 | 全组 | P0 | 对应项冻结，变更记录写明同意者 | 未开始，未将任何研究决定写成新批准 |

### 阶段 1：开发集上的方法（只用 debug / SFT）

| ID | 任务 | 负责 | 依赖 | 完成标准 | 状态 |
|---|---|---|---|---|---|
| A1 | 核对 v4 / v5 显卡、代码、数据版本；H100 上补齐可比回放，保留旧结果 | A | P0 | v4/v5 summary 与逐次运行记录完整；写明 B 输入 commit；v5 TTCA 与旧离线估算对照，估算继续标注 | 进行中：v5 已有本地记录，H100 可比性和 provenance 未验收 |
| A2 | 用固定 B evaluator 评分真实回放；复核 claim 映射；确认 Wait 日志要求 | A+B | A1 | run_eval 退出 0；全部 review queue 复核；自查差异有解释，不能仅凭退出 0 宣告通过 | 进行中：2026-11-12 已补 v6/v7 原始评分与配对分析；映射、语义抽取和独立复核仍缺，不是整体正式分数 |
| A3 | 参数扫描 Time-Only、Fixed Progress、Evidence-Aware progress 阈值，画 TTFGI–UCR | A | A2 | 图表和选定参数；人确认后写入 D3 | 未开始 |
| A4 | by_presupposition GPU 验证；by_omission 只选对应标题再判断的候选改法；种到属的错误 | A | P0 | judge notes 新增真实运行行；错判 SUPPORTED 不增加；研究规则变更先确认 | 未开始，原 notes 仍写部分 GPU 验证待做 |
| A5 | 分析只有 Wait-All 答对的 trace，分拆题、judge、生成归因 | A | A2 | 逐条归因表；据此讨论 D4、D9 | 未开始 |
| A6 | 视 D9 做 Wait-All 先 judge 再生成的消融 | A | A5 + D9 | 真实回放和 spec 7.3 更新 | 未开始，不能先替人决定做消融 |
| A7 | 汇总听音表；第二人复核 FINDINGS；视需要多种子 | A | — | 汇总表、复核人和判断依据 | 未开始，已有单人判读不等于复核完成 |

### 阶段 2：最终评估数据

| ID | 任务 | 负责 | 依赖 | 完成标准 | 状态 |
|---|---|---|---|---|---|
| B1 | 预留 gold 与三档 trace；独立 B 标注会话，A 开发不看 | B | P1 | 构建校验通过、人工复核、commit 和 hash 完整 | 进行中：仅从 `638027b` 提交信息确认 gold 草稿存在；内容、trace、验收未核 |
| B2 | multipart 评测集来源与规模（D5） | B | P1 | 人决定规模；校验、人工复核、版本与 hash 同 B1 | 未开始 |
| B3 | judge 验证集（D8），决定另建约 200 条还是用预留 gold | A+B | B1 | 决定入 spec；若另建则标注并复核；沿用预留仍不解除禁读规则 | 未开始 |
| B4 | 按题目配对 bootstrap、完整回答事实抽取、冲突和纠错计分 | B | — | 测试通过，示例能出 CI，D6/D10 确认 | 未开始，已有结构化 evaluator 不等于这些能力齐全 |
| B5 | 可选：小规模 `retrieved` trace，检查延迟方案现实依据 | B | P1 | trace 校验通过，系统与延迟来源可追溯 | 未开始 |

### 阶段 3：语音与外部对照

| ID | 任务 | 负责 | 依赖 | 完成标准 | 状态 |
|---|---|---|---|---|---|
| S1 | 用现有开源 TTS 测回答时长、校准 2.5 词/秒；验收现有 ASR/Piper smoke | A或C | A1 | 估算与实测误差表；必要时经同意更新 D2；保留音频供人评 | 进行中：有本地组件和提交记录；smoke 结果和校准未验收 |
| C1 | 相同延迟下跑 MoshiRAG，转 B 接口评分；先 debug，冻结后最终评估 | C+B | P1 | 时间定义 D7/D11 对齐；debug 正式评分通过 | 进行中：新三档 debug 交付已到，正式评分和音频事实时间仍缺 |
| C2 | Pairwise 人评，确认及时性、自然度、可信度、策略、题数和评分人数 | C | S1 | 经人确认的方案和人评结果 | 未开始 |

### 阶段 4：最终运行与论文

| ID | 任务 | 负责 | 依赖 | 完成标准 | 状态 |
|---|---|---|---|---|---|
| F1 | 用户明确说“这是最终运行”后冻结代码/tag，在预留与 multipart 一次跑全配置并评分 | 全组 | A2、A3、B1、B2、B4，以及所有最晚需最终运行前确认的 D 项 | tag/commit 入 spec，输入 hash 与结果入运行记录；之后不再用预留调参 | 未开始，不能因已有 gold 草稿提前运行 |
| F2 | 论文主表、TTFGI–UCR 图、诊断、可控性、错误分析和局限 | 全组 | F1 | 初稿 | 未开始 |

依赖分两条：数据线 P0 → P1 → B1/B2 → F1；方法线 P0 → A1 → A2 → A3 → F1。
A2 的开发评分用 debug，不依赖预留 B1；不得为开发评分提前打开预留数据。
B4 也必须在 F1 前完成。S1 完成后再做 C2。时间安排由人确认，本次不启动这些步骤。

## 当前需要人确认或补交的内容

- `docs/proposal.pdf` 的真实文件位置；现有文档中关于 proposal 的内容只转录用户草稿，未独立核对。
- P1 的冻结决定与同意者，特别是 B 已有草稿后，D13–D15 是否已有未同步的决定。
- D2：默认文字回放与本地 ASR/Piper 分支采用什么正式口径。
- D3、D4、D6、D7、D9–D11 等仍是待定，不能从现有代码反推为已批准。
- `unit_schema.md` 的 Partial 附带进度描述与 facts-only 实现不一致。
- B 接口与 A 非 Wait 日志、gold 描述诊断输入路径存在需要共同核对的差异。

## 新同学从哪里开始

1. 读规则 `CLAUDE.md`（同源入口 `AGENTS.md`）。
2. 读 proposal；若 PDF 缺失，报告，不猜内容。再读 spec 第 1、2、6、8 节。
3. 在有 A 代码的原工作区读 `a_work/README.md`，运行 `python3 a_work/run_demo.py`。
4. 读 FINDINGS，理解当前改用级联方案的开发依据和判读局限。
5. 读 judge notes、LoRA notes；本地级联分支再读 cascade / evaluation notes。
6. 从依赖满足、尚未完成的一个步骤开始；用户有指定时以指定步骤为准。

## 运行记录

每次 GPU 运行单独一行，记录来源分支和完整 commit、数据 hash、代码或快照、显卡、作业号、状态和结果路径。
旧草稿有汇总行且缺元数据，暂保留为**历史索引，尚未验收**；不能直接据此引用性能数字。
“待补”表示没有核实，不代表不存在。没有结果不补造。本次只读文档和跑 CPU 测试，未提交 GPU 作业。

| 日期 | 运行名 | 数据来源和版本 | 代码 commit / 快照 | 显卡 | 作业号 | 结果路径 | 状态 / 元数据缺口 |
|---|---|---|---|---|---|---|---|
| 2026-10-06 | 异步检索延迟 runs 1–4（旧汇总） | 简单题 / SimpleQA；版本待补 | 待补 | Colab T4（原记录） | — | `experiments/async_retrieval_latency/t4/colab_results_2026-10-06/` | 旧诊断，逐次来源待核；proposal PDF 缺失 |
| 2026-10-22 | `full_v1` | 控制集；输入 commit/hash 待补 | 待补 | H100（FINDINGS） | 11726985 | `a_work/moshirag_control/results/full_v1/` | 旧结果，第二人复核待做 |
| 2026-10-22 | `full_v2` | 控制集；输入 commit/hash 待补 | 待补 | H100（FINDINGS） | 11727274 | `a_work/moshirag_control/results/full_v2/` | 旧结果，第二人复核待做 |
| 待补 | `partial_v3` | 两段证据扩展控制集；版本待补 | 待补 | 待补 | 11729084 | 见 FINDINGS；完整路径待补 | 已有人工判读记录，provenance 未齐 |
| 2026-10-25 前 | C 早期无参考 / 有参考（旧汇总） | `debug-v0`，版本见交付包 | 待从交付包核实 | 待补 | 11675327、11760936、11761507 | `c_work/deliveries/2026-10-25-debug-v0/` | 交付 README 可读；不构成匹配时间对照 |
| 待补 | Prompt judge mock v1–v6、B v1–v2（旧汇总） | mock / debug；版本待补 | 待补 | H100；mock v3 A6000（notes） | 待补 | `a_work/results/judge/` | 逐次记录、失败与元数据待核；不跨卡比延迟 |
| 待补 | `qwen3_4b_v1` 训练 | SFT train `sft-v0`；B 来源 commit 待补 | 待补 | 待补 | 待补 | `a_work/results/lora/qwen3_4b_v1/` | 已有训练记录，元数据待核 |
| 待补 | LoRA / Prompt SFT dev 评估（旧汇总） | SFT dev `sft-v0`；B commit 待补 | 待补 | A100（LoRA notes） | 待补 | `a_work/results/lora_eval/` | 开发比较；不与 H100 混报 |
| 待补 | 回放 v4 | debug 三档；B commit 待补 | 待补 | 待核，旧 notes 提及 A100 | 待补 | 完整目录待补，旧表见 `a_work/lora_judge.md` | A1 核对后补齐，离线估算继续标为估算 |
| 不晚于 2026-11-10 | `b_q1_20_gen_v5` | debug；本地输入版本与 B commit 待补 | 待补，不能以当前 HEAD 代替 | 待核 | 待补 | `a_work/results/replay/b_q1_20_gen_v5/` | 据本地 evaluation notes 已评分；原始 / assisted 分开，待独立复核 |
| 不晚于 2026-11-10 | `b_q1_20_gen_v5_lora` | debug；本地输入版本与 B commit 待补 | 待补 | 待核 | 待补 | `a_work/results/replay/b_q1_20_gen_v5_lora/` | 同上；evaluator 固定 `15f0e0246cc91443bd74b477ccee941432794ef6` |
| 不晚于 2026-11-10 | C `trace-v1-debug-12189299` | B debug 三档；trace SHA256 见交付 README | runner commit 待补；交付 commit `10d2394` 不等于 runner commit | 待补 | 12189299 | `c_work/deliveries/trace-v1-debug-12189299/` | README 报执行/产物检查通过；正式评分与对齐待做 |
| 2026-11-10 提交 | `cascade_smoke_20261110_v1` | debug 子集；输入 manifest 见本地快照 | `a_work/results/code_snapshots/cascade_smoke_20261110_v1/`；父 commit/hash 待核 | 申请 A100，尚未分配 | 12308419 | `a_work/results/` 下，精确输出待验收；说明见 `a_work/cascade.md` | 2026-11-11 查询 PENDING / Priority，未验收 |
| 2026-11-11 | `b_q1_20_gen_v7_lora` | `a_work/results/inputs/b_debug_q1_20_gold13/`；debug；B 来源 commit 待核 | 父 `9fb9adc` + dirty；`a_work/results/code_snapshots/replay_gen_q1_20_v7/` | A100-SXM4-80GB | 12307492 | `a_work/results/replay/b_q1_20_gen_v7_lora/` | COMPLETED，退出 0；rate、无 ASR；有自查产物，无 B 评分 |
| 2026-11-11 | `b_q1_20_gen_v7` | 同一 debug 输入；B 来源 commit 待核 | 同一 v7 开发快照，非当前整分支验收 | A100-SXM4-80GB | 12307493 | `a_work/results/replay/b_q1_20_gen_v7/` | COMPLETED，退出 0；prompt judge；rate、无 ASR；无 B 评分 |

另有 judge 作业 `12306379`、`12306380`，2026-11-11 查询仍为 PENDING / Priority，
均申请 A100，完整运行名与配置尚待核，不能仅按提交时间认定是 v6。
原先 `12306377`、`12306378` 已在未运行时取消，sacct 无分配节点；保留此记录，不冒充模型失败。
v7 快照 Python 文件集合 SHA256 为
`e0cd7bee8a6cf9dee8e6db1e26d6a6db5f7fd730711587e1f32dce686abdbefe`。
计算为相对快照目录的路径排序后拼接路径、NUL、内容、NUL，排除 pycache。
当前 `run_replay.py`、`generate.py` 与该快照不同，不把运行时 HEAD 当作完整源码版本。
以上状态来自 squeue/sacct、对应 Slurm 日志和已知 debug run_config，不是仅依据旧笔记。
旧失败与模型启动失败详见 judge notes；后续补档时保留失败，不删除历史记录。
本地结果目录不进 git。交付文档路径可以定位历史证据，不授权复制更多结果到版本库。

## 本次文档整理与验证（2026-11-11）

- 在原有 `/u/xzhu81/CS546/moshi-rag`、`a-cascade` 整理，无 commit/push。
- 用户要求只用原目录后，已迁回文档并移除助手先前新建的 main worktree。
- 远端 fetch 已完成；本地 `a-cascade` 父 commit 与 `origin/a-answer-gen` 一致。
  为保留 dirty 工作区，不切换分支或合并其他组。共享文档进 main 和组间同步仍待用户安排。
- 只读取 B/C 的接口、debug 交付说明和提交元数据；未读取预留题及派生 gold/trace。
- A 代码测试使用用户现有 dirty 工作区，不代表干净 `9fb9adc` 或 main 的测试结果。
- 结果来源为本会话真实 CPU 测试输出；没有模型调用、GPU 运行或性能新结果。

| 命令 | 被测代码 | 结果 | GPU / 数据 / 结果位置 |
|---|---|---|---|
| `python3 -m unittest discover -s a_work/tests` | `a-cascade`，父 `9fb9adc316d478362c5443948ef53a4645b8fae7` + dirty | 91 项，通过，退出 0 | 无 GPU；本地 fake models/fixtures；本会话终端输出 |
| `python3 a_work/moshirag_control/tests/test_control.py` | 同一 A 工作区 | 19 项，通过，退出 0 | 无 GPU；本地测试；本会话终端输出 |
| `python3 -m unittest discover -s b_work/eval/tests` | `638027bf35c29428742c1e42aabf9243a08466d8` 的 `b_work/eval/`，仅定向提取到临时目录 | 31 项，通过，退出 0 | 无 GPU；测试内 fixture；本会话终端输出；未检出 B 数据目录 |

A 被测 Python 源码集合的 SHA256：
`d06caf2663c4f2ee800022a7ae9ac2a655c114b5245b5123d063436600e3c4b0`。
计算方法：按路径排序，依次拼接 `a_work/` 下 `.py` 的相对路径、NUL、原始内容、NUL；
排除 results 与 `__pycache__`。这标识被测本地源文件集合，不替代正式运行的冻结快照。

### P0 尚未完成的部分

- 补 proposal PDF 并核对 proposal 引用。
- 用户选择提交范围并提交；给共享文档安排进入 main 的路径。
- 各组同步 main，A 的既有实验改动另按 PR 流程集成。
- 后续由相应负责人验收运行 provenance、映射和研究决定。本次不替代这些工作。


### 用户提交前整理（2026-11-11）

当前准备两个独立提交：A 组代码、测试与说明；共享文档和根 README。
助手只整理、验证并提供命令，由用户执行 commit。工作范围仍是 P0 交接，不启动新实验。
已修正 v7 完成和 smoke 排队状态，judge notes 补记已有提示词改动。
本次重新运行 A 测试：91 项通过；控制实验：19 项通过；均退出 0，不使用 GPU。
B evaluator 未改动，之前固定 B commit 的 31 项通过记录仍保留。
代码提交表示保存开发进度，不表示 S1 或最终评估验收完成。


### 账号权限与优先级核对（2026-11-11 12:26 CST）

用户要求检查现有权限是否生效。核对来源为 scontrol、squeue、sprio、sacctmgr、sshare。
核对开始时 HEAD 为 `3380a7b`，整理期间工作区 HEAD 已更新为 `c23d6ae`（维护规则记录提交）；
助手未执行 commit。本次只改说明和注释，不改运行参数、不改队列、不重新提交任务。

- `xzhu81` 的授权关联包含 `dilek-ic` 与 `campusclusterusers`，允许的 association QoS 为 normal。
  三个既有作业实际都是 `Account=dilek-ic`、`QOS=normal`，不是误用默认公共账号。
- 既有作业 scontrol 数值 Priority 为 2151–2154；同一时点 IllinoisComputes-GPU 的
  待运行作业数值范围为 0–3000，说明用户不是最低数值优先级。资源申请不同，不能据此给出精确候位排名。
- `IllinoisComputes-GPU` 的 `PriorityTier=3`，`secondary` 为 1；分区层级与数值 Priority 是两回事。
- Slurm 当前权重：Age=1000、Partition=2000，FairShare=0、Assoc=0、QOS=0、JobSize=0。
  虽然 sshare 显示组账号下的 FairShare 大于公共账号下的值，它目前不参与数值 Priority 加分。
  原 eval_judge.slurm 的“组账号带来更高 fair-share priority”注释不准确，已仅修正文案。
- 旧 judge 作业 `12306379`、`12306380` 的 Nice=5；smoke `12308419` 的 Nice=0。
  当前脚本与本会话 SBATCH 环境变量都没有设置 nice，旧值来源待核。正 nice 会降低数值优先级，
  后续不无故增加；不擅自改已结束任务或尝试未授权 QoS。
- Illinois Computes 的官方政策区分 Primary、De-prioritized Primary、Secondary；不能把
  normal QoS 直接解释为最低权限，也不能仅看一个 Priority 数字判断所有资源的调度先后。
  正式 H100 仍受型号约束，不能为了较高层级擅自换 A100/H200 或 MIG。

官方解释：[Campus Cluster 队列政策](https://campuscluster.illinois.edu/access/illinois-computes/)、
[Slurm 优先级和分区层级](https://slurm.schedmd.com/priority_multifactor.html)。

查询期间三个旧作业均已结束；之前 RUNNING / PENDING 的记录保留为当时状态：

| 日期 | 运行名 | 数据来源 | 代码 / 快照 | 显卡 / 节点 | 作业号 | 结果路径 | 状态与限制 |
|---|---|---|---|---|---|---|---|
| 2026-11-11 | `b_q1_20_gen_v6_lora` | `a_work/results/inputs/b_debug_q1_20_gold13/`，debug；B commit 待核 | 运行日志 HEAD `3380a7b`；v6 快照及其源码哈希待进一步核实，不能以 HEAD 代替 | A100-SXM4-80GB / ccc0387 | 12306379 | `a_work/results/replay/b_q1_20_gen_v6_lora/` | COMPLETED，退出 0；已有回放 summary，正式评分待验收 |
| 2026-11-11 | `b_q1_20_gen_v6_lora_conc` | 同一 debug 来源，提交时参数仍待核 | 日志 HEAD `3380a7b`；实际快照版本待核 | A100-SXM4-80GB / ccc0388 | 12306380 | `a_work/results/replay/b_q1_20_gen_v6_lora_conc/`；Slurm 日志 `a_work/slurm/logs/a-eval-judge-12306380.out` | FAILED，退出 3；vLLM Engine core initialization failed；不是排队或权限拒绝，根因待定位 |
| 2026-11-11 | `cascade_smoke_20261110_v1`（结束状态补录） | 已冻结 debug 子集，输入 manifest 见上方旧提交记录 | `a_work/results/code_snapshots/cascade_smoke_20261110_v1/`；日志 HEAD `3380a7b` | A100-SXM4-80GB / ccc0388 | 12308419 | `a_work/results/replay/cascade_smoke_20261110_v1/`；Slurm 日志 `a_work/slurm/logs/a-cascade-smoke-12308419.out` | FAILED，退出 1；ASR 启动报 No CUDA GPUs are available，尚未完成链路验收 |

以上是操作状态，未新增实验性能结果。两个失败保留原始日志，不作优先级问题处理；
本次只记录，不启动故障修复或重跑。当前用户队列查询为空，没有仍待调高优先级的现有作业。

### 新完成 debug 回放的评分整理（2026-11-12，A2）

用户要求整理新分数并分析报告。本次只补 CPU 评分和汇总，不启动 GPU 实验、不调参数。
基线 `a-cascade` @ `c23d6ae6e7250b793c026e7ec01ae9166728f5af` + dirty；保留原有暂存与工作区修改。
详细报告见 `a_work/evaluation_notes.md` 的 2026-11-12 节；汇总与 hash 清单在
`a_work/results/analysis/debug_scores_20261112/`，不进 Git。

| 原 GPU 运行 | 作业 / 显卡 | 原代码来源 | 本次评分输入与产物 | 本次结果 |
|---|---|---|---|---|
| `b_q1_20_gen_v6_lora` | 12306379 / A100-SXM4-80GB | 日志 HEAD `3380a7b`；候选 v6 快照存在，实际加载绑定待补 | `b_debug_q1_20_gold13/` debug；`results/replay/b_q1_20_gen_v6_lora/b_eval/` | 420 个 policy runs；退出 0；validation issues 0；全配置待复核声明 34；主方法已确认完整 38/60 |
| `b_q1_20_gen_v7` | 12307493 / A100-SXM4-80GB | `replay_gen_q1_20_v7/`；父 `9fb9adc` + dirty，快照 hash 见上文及 A notes | 同一 debug 输入；`results/replay/b_q1_20_gen_v7/b_eval/` | 600 个 policy runs；退出 0；validation issues 0；全配置待复核声明 40；主方法已确认完整 37/60 |
| `b_q1_20_gen_v7_lora` | 12307492 / A100-SXM4-80GB | 同一 v7 快照 | 同一 debug 输入；`results/replay/b_q1_20_gen_v7_lora/b_eval/` | 600 个 policy runs；退出 0；validation issues 0；全配置待复核声明 44；主方法已确认完整 42/60 |

固定 B evaluator `15f0e0246cc91443bd74b477ccee941432794ef6`，与 v5 原始评分一致；
31 项现有 evaluator 测试通过、退出 0。新运行输入 SOURCE 指向
`a2808f17558076291ec439d2ced8a00be8c52281`，已核对 debug trace/gold SHA256 一致；完整 hash 见 A notes。
五轮 B 评分配置所记录的实际输入 hash 相同；v5 旧 SOURCE 的 gold 版本不吻合，最初运行来源仍待补。

主方法待复核声明为 Prompt 8、LoRA 10，整体 Structured UCR 保留 null。
long 档有更早给出信息的开发信号，short 无稳定收益，TTCA 仍较 Wait-All 晚；
并发是模拟调度收益，不能当作真实共享 GPU 或 ASR/Piper 的实测。
A2 保持进行中：独立映射复核、完整语义抽取、别名规则和运行 provenance 尚未验收。
本次未改 gold、B evaluator 或提示词，未读取预留评测数据，未 commit/push。
