# 剩余工作计划

本文列出到论文初稿的工作、依赖、完成标准和运行记录。实验定义见 `experiment_spec.md`。
D 编号对应 spec 第 11 节。一次只做一步；只做部分就标“进行中”。

截止日期：待用户填写学期结束日期、目标会议截稿日期。
最后核对：2026-11-18。当前任务为 **按对应分支逐步完成论文所需验证**。
主实验冻结运行及原始评分已完成，R1 已有校验实现和专项 GPU 结果；评分独立复核、
公平消融、语音对齐和人评仍待验收。下方早期计划及历史记录保留其当时状态。
**用户自行提交。助手不 commit、不 push，不自行创建其他工作区或仓库副本。**

## 当前推进顺序及对应分支（2026-11-18）

用户要求一步一步推进，各项工作放在对应任务分支。按以下工作包推进，每次只实施当前一步。
新分支仅在轮到对应任务时创建，起点使用已同步、所需功能齐全的 A 集成版本。
本表是工作安排，不替代尚待讨论的指标或研究规则决定。

| 顺序 | 工作与对应分支 | 验收依据 | 当前状态 |
|---|---|---|---|
| 1 | A 证据路径校验在现有 `a-eval-refinement`；B gold/SFT 标注由 B 在 `b-data-eval` 处理 | 专项路径回归、新代码的 GPU 调用与完整策略回放、B 口径独立确认 | A 空答案候选修复已通过离线校验；新 GPU 验收 12549423 已提交，B 对齐及完整策略影响仍待验收 |
| 2 | A 评分诊断、论文指标对照和复核接口在 `a-eval-refinement`；B evaluator 与独立标注在 `b-data-eval` | debug 先验证一致规则，再对原冻结主实验输出复核；覆盖率、未知和统计区间完整报告 | 下一步；完整正文语义和映射选择效应优先处理 |
| 3 | 公平生成消融使用待创建的 `a-baseline-ablation`；参数实验使用待创建的 `a-dev-parameter-sweep` | 先确定 D9 与候选范围，用 debug/SFT 记录质量、延迟及额外成本 | 待前两步验收；是否训练更多模型依开发诊断决定 |
| 4 | A 语音 smoke、TTS 校准在现有 `a-cascade`；C MoshiRAG 同口径对照在 `c-external-baselines`，评分在 B 分支 | 链路成功、计时误差记录、对应音频与结构化分数 | 待修复语音 smoke 并对齐 C 时间定义 |
| 5 | 人评方案与交付索引由 C 在 `c-external-baselines` 整理；A 需改音频导出时在 `a-cascade` | 预先确定抽样、匿名配对与评分办法，再收真人评分及一致性 | 待链路验收和人员安排 |
| 6 | 已冻结主实验运行管理在 `a-main-experiments`；经确认的补充结果分析与论文材料使用待创建的 `a-paper-results` | 主表、配对统计、局限、版本与数据来源可复现 | 原主实验已完成；新规则与参数的最终验证需另确认版本和独立评测安排 |

A 功能经用户提交后按项目流程集成到 `a-method-integration`。
三组共享定义合入 `main` 的安排由用户和全组决定。真实检索扩展、多轮交互、更多 judge
或重新训练是否需要，由论文主张和当前失败分析决定，不把这些扩展默认列为第一轮必做任务。

第 1 步执行记录。GPU 作业 `12545106` 已 COMPLETED、退出 0、用时 9 分 26 秒，
H100、账号 `dilek-ic`，源码及输入以既有冻结 manifest 为准。Prompt/LoRA 各 59 次调用无错误，
7 个虚构用例原严格校验通过 7/7、6/7。已定位 LoRA 明确排除时结论值为空的缺口，
本分支做最小修复，并用保存的同一批回复离线重校验，均为 7/7。
每种模型 52 个 debug 快照相对旧校验各有 2 个路径变化、无标签变化。
GPU 原始结果与离线新校验结果分开记录，未把离线通过写成重跑 GPU 的结果。
本步尚不等于 B gold、独立语义评分或完整策略验收完成，细节见 A judge notes。
当前 `a-eval-refinement` @ `3c02ce8` + dirty 的 A 测试 99 项、控制实验测试 19 项均通过，
退出 0，diff 检查通过。代码与计划修改待用户提交。

用户指出离线校验不足以确认问题解决。当前状态据此明确为候选修复，等待新版本 GPU
及完整策略验收。作业 `12549423` 已提交，账号 `dilek-ic`、normal QoS、nice 0、
scavenger/secondary，申请 1 张 H100、60 分钟。快照为
`a_work/results/code_snapshots/judge_premise_paths_20261118_v2_live/`，父 `3c02ce8` + dirty，
提交记录和全部源码、debug 输入及 adapter 的 hash 位于该目录。
验收重新调用 Prompt/LoRA，分别检查 7 个虚构例子与 52 个 debug 快照，
运行真实 judge/生成器驱动的省略后直接确认和明确排除策略场景，再分别运行
20 题、60 条 debug trace、600 条策略运行，最后使用 B `ea39057` 固定评分器。
计划结果为 `a_work/results/judge/judge_premise_paths_20261118_v2_live/`。
作业结束、场景断言和评分验收结果需分别记录，提交成功不代表规则验收通过。
首次调度核对为 PENDING / Priority，数值 Priority 为 2000，开始时间 N/A。
当前可见 H100 均已分配，ccc0419 虽有两张 GPU 未占用，但 96 个 CPU 全部分配，
该观测不构成预计开始时间。新 GPU 结果尚未产生。

2026-11-20 更新：`12549423` 已在 H100 / ccc0424 COMPLETED、退出 0，耗时 15 分 54 秒。
Prompt 与 LoRA 各 7 个虚构专项判断通过，2 个真实模型驱动策略场景均通过；每种模型的
20 道 debug 题三档、各 600 个策略运行及固定 B `ea39057` 评分完成，校验问题 0。
各 52 个 debug 证据快照中各 2 个路径记录变化、支持标签未变。结果与源码快照见上方路径。
Prompt、LoRA 的实际模型拆题配置分别确认完整 37/60、41/60，未知 8/60、11/60；
Wait-All 40/60、未知 3/60。B gold 对齐与独立语义复核仍待完成；专项通过不等于整体准确率。

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
| R1 | 原 1；A4、D14/D15 | 研究 `by_omission` 与 `by_presupposition` 的组合 | 用户已确认这两种标记 | 组合情形表、反例和候选规则；A/B 确认语义后，A 实现与 B gold/evaluator 口径一致；适用回归通过 | 进行中：2026-11-13 已核对当前代码、复现虚构路径、解释影响并给出三种候选；规则与实现未变，详见 A judge notes 第 8 节 |
| R2 | 原 2；A2、B4、D6/D10/D11 | 阅读 Full-Duplex-Bench 和 TurnBench，制定适合自由回答的评分候选方案 | R1 的问题分类已梳理；两篇论文已确定 | 原文和官方 scorer 对照表；区分语义正确性、证据支持、交互检测和自然度；说明缺失、别名、矛盾、纠错与分母；经 A/B 确认后再改评分 | 待开始；只核对论文身份与摘要，未完成细读 |
| R3 | 原 6；A5/A6、D4/D9 | 与 Wait-All 做公平的配对诊断 | R1/R2 口径可用于开发评分，待复核映射有处理方案 | 相同 trace、硬件和计时下的质量/覆盖/TTFGI/TTCA 表；区分策略与生成差异；是否增加 Wait-All 先 judge 的消融由 D9 决定 | 进行中：已有 v7 开发配对表；映射复核、生成公平性与 D9 消融未完成 |
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

2026-11-13：用户要求先解释截图中的影响并给方案。代码核对发现：omission 的 no 可参与
presupposition 的提前结论，且 omission 来源不会自动传递到结论标记。
用 3 个虚构运行时情形及 2 个假想 gold 支持情形复现；不代表真实模型错误率或真实 gold 质量。
三种候选为保守限制组合、满足严格条件后允许、保留规则分组诊断；建议先讨论保守限制加分组诊断。
具体分析、权衡和需要 A/B 对齐的接口见 `a_work/judge_notes.md` 第 8 节。
本次只改说明，没有改变 spec、提示词、策略、gold、evaluator 或训练标签；R1 尚未验收完成。

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
| 异步检索诊断 | 已有历史实验记录，核对了四轮聚合分数 | runs 1–3 完成，run4 仅完成 31/72；字符串命中不是语义准确率，见 A evaluation notes 的 2026-11-16 节 |
| MoshiRAG 可控性 | Wait / Progress / Final 有开发结果，Partial 不可靠 | `a_work/moshirag_control/FINDINGS.md`；单种子、第二人复核未完成 |
| A 控制器与 judge | 四个规则 baseline、Evidence-Aware、prompt / LoRA / oracle、模型拆题与生成 | 当前 `a-eval-refinement` @ `2f74933`；没有未提交研究代码，不等于最终配置已冻结 |
| A v5 回放 | 已运行并经固定 B evaluator 评分；部分映射由助手辅助复核 | `a_work/evaluation_notes.md`；仍有待复核项，不能当整体 UCR 或独立人工复核 |
| A 后续优化 | v6 LoRA 与两轮 v7 已完成；2026-11-12 补齐固定 B evaluator 评分，均退出 0、校验问题 0 | v7 主方法已确认完整 Prompt 37/60、LoRA 42/60；待复核声明 8/10，整体 UCR 为 null；详见 A evaluation notes |
| A ASR / TTS | 本地有 Whisper、Piper、调用回放和 smoke 脚本；作业 12308419 已失败，退出 1 | A100；ASR 报 No CUDA GPUs are available；主时间轴仍模拟，S1 未完成，见后文结束状态记录 |
| B 数据 | debug gold / trace、SFT 已有；最新提交说明评测批次修订和完整上下文 trace | B `ea39057` 及前序提交的元数据；未读取任何预留题、gold、trace，未验收 B1 |
| B evaluator | 有结构化声明评分、校验、映射复核队列和测试；A 本地已接入真实回放 | B eval README、A evaluation notes；语义抽取、纠错和 CI 仍待做 |
| C 外部对照 | 三档延迟 debug 交付及新增 AI 文字初评 | C `8668d9f`：60 条初评为 4 正确 / 11 部分正确 / 45 错误；人工评分列全空，正式评分、音频对齐和听评待做 |
| 共享文档 | 共享定义与计划已在 A 分支提交；本轮盘点仍未提交 | 当前 `a-eval-refinement`；main 和各组同步尚未验收，旧规则分支入口有过时项 |
| Proposal | 仓库和当前工作目录未找到 PDF | 约定路径 `docs/proposal.pdf`；已向用户询问位置，不编造或替代 PDF |

本表只从获准的开发说明、接口、提交元数据核对进度。
原稿中“v5 尚无真实回放”“B 预留集只有题目”“C 尚未按三档延迟运行”已过时，
但相应步骤的全部验收标准仍未满足。

### 分支快照

远端引用已于 2026-11-16 通过 `git fetch --all --prune` 更新。
`main` 与 `origin/main` 一致；原目录当前分支为 `a-eval-refinement`，没有覆盖既有未提交修改。

| 分支 | 核对时 commit | 说明 |
|---|---|---|
| `origin/main` | `73b578a1df477dfa90476021e75adc41714bc891` | 共享文档尚未提交到此分支 |
| `origin/a-method-integration` | `bc412d5` | A 的 PR 集成目标；本轮未切换、合并或验收与当前分支的差异 |
| `origin/a-cascade` | `c23d6ae` | 先前工作分支；旧 `origin/a-answer-gen` 等远端引用已经删除 |
| 本地 / `origin/a-eval-refinement` | `2f74933aafa3d900acf415d5269a8c3946465bfd` | 当前分支；本轮及 R1 未提交内容为说明文档，研究源码无新增 diff |
| `origin/b-data-eval` | `ea390574eadd301354d5de46f0d28d328cca5bad` | 最新评测修订与 trace 提交；只查看元数据和 evaluator，不查看预留内容 |
| `origin/c-external-baselines` | `8668d9f` | 新增 60 条 debug 响应的 AI 内容初评 |

`cascade.py`、`eval_with_b.py`、ASR/Piper 脚本与测试等已有实现已在分支历史中。
当前没有新增未提交研究代码；这不代表它们的语音验收、正式评分或运行来源已全部补齐。

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
| B1 | 预留 gold 与三档 trace；独立 B 标注会话，A 开发不看 | B | P1 | 构建校验通过、人工复核、commit 和 hash 完整 | 进行中：最新 `ea39057` 等提交说明已有批次复核、修订与完整上下文 trace；仅核对元数据，最终验收未核 |
| B2 | multipart 评测集来源与规模（D5） | B | P1 | 人决定规模；校验、人工复核、版本与 hash 同 B1 | 未开始 |
| B3 | judge 验证集（D8），决定另建约 200 条还是用预留 gold | A+B | B1 | 决定入 spec；若另建则标注并复核；沿用预留仍不解除禁读规则 | 未开始 |
| B4 | 按题目配对 bootstrap、完整回答事实抽取、冲突和纠错计分 | B | — | 测试通过，示例能出 CI，D6/D10 确认 | 未开始，已有结构化 evaluator 不等于这些能力齐全 |
| B5 | 可选：小规模 `retrieved` trace，检查延迟方案现实依据 | B | P1 | trace 校验通过，系统与延迟来源可追溯 | 未开始 |

### 阶段 3：语音与外部对照

| ID | 任务 | 负责 | 依赖 | 完成标准 | 状态 |
|---|---|---|---|---|---|
| S1 | 用现有开源 TTS 测回答时长、校准 2.5 词/秒；验收现有 ASR/Piper smoke | A或C | A1 | 估算与实测误差表；必要时经同意更新 D2；保留音频供人评 | 进行中：组件已有；smoke 12308419 失败，校准与链路未验收 |
| C1 | 相同延迟下跑 MoshiRAG，转 B 接口评分；先 debug，冻结后最终评估 | C+B | P1 | 时间定义 D7/D11 对齐；debug 正式评分通过 | 进行中：三档 60 条已交付且有 AI 文字初评；正式同口径评分和音频事实时间仍缺 |
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

### 全项目任务与分数盘点（2026-11-16）

本轮根据用户要求核对代码状态、全部可定位的获准开发汇总和远端进展。
当前 `a-eval-refinement` @ `2f74933`；保留 R1 的未提交文档，没有新增研究代码、GPU 作业或评分规则。
详细解释见 `a_work/evaluation_notes.md` 的 2026-11-16 节；逐轮原值、来源 hash 和可重现脚本在
ignored 的 `a_work/results/analysis/project_audit_20261116/`。该目录盘点 17 份 judge/dev、
12 份 replay 自查、2 份训练日志、4 轮 T4 汇总、4 个控制作业与 C 的 60 条 debug 初评。
本次只核对既有评分，没有新增模型调用或语义改判。

- 五轮既有 B 评分的日志/分数 hash 未变；v7 已确认完整仍为 Prompt 37/60、LoRA 42/60、Wait-All 40/60。
  主方法待定运行 8/10，整体 UCR 仍 null；LoRA 的 Unit EM 92% 只覆盖 50 个可评分运行。
- LoRA dev 单元标签一致为 1269/1352（93.9%），不是回答准确率；独立 dev 题仅 57 道。
- long 的配对 TTFGI 有提前信号，short 不稳定，TTCA 没有总体提前；计时仍为文字/rate 模拟。
- C @ `8668d9f` 的逐行 AI 文字初评为 4 正确、11 部分正确、45 错误，人工评分列全空。
  与 B 的结构化单元评分口径不同，不能据此宣布系统间准确率胜负。
- 控制作业 `partial_v3` 已补核为 RTX A6000、11729084、90/90 完成；单种子行为结果仍待第二人复核。
  T4 run4 是 31/72 中断，不是完整扫描；答案字符串命中不能替代语义评分。
- 旧运行表的 PENDING / 无 B 评分均为当时记录，由后续记录与本次盘点更新：
  12306379、12307492、12307493 均 COMPLETED 0；12306380 FAILED 3；12308419 FAILED 1。
  当前队列为空，2026-11-12 以来未查询到用户新作业；失败任务未重跑。
- 当前 A 测试 91 项、控制测试 19 项、B evaluator @ `ea390574eadd301354d5de46f0d28d328cca5bad`
  测试 31 项，均通过、退出 0；共 141 项 CPU fixtures 测试，不代表真实语音或语义评测通过。
  最新 B evaluator 与原固定评分 commit 的源码无差异；没有读取预留题/gold/trace 内容。

仍未解决的实现边界是持续 Wait 的终止、失败调用的耗时/tape 记录、R1 组合依据传播和时间规范不一致。
R1/R2、映射独立复核与公平对照仍优先于参数扫描和最终全量运行；语音 smoke 修复与校准优先于音频人评。
未选择新规则、阈值或胜出模型，未作最终冻结、上传或提交。

### 作业进度核对（2026-11-16 17:31 CST）

Smoke `12490825_0` 在 16:47:22–16:55:09 完成，用时 7 分 47 秒、退出 0，
GPU 为 NVIDIA H100 80GB HBM3 / ccc0421。自动校验 `12490921` 于 16:55:42–16:55:48
完成、退出 0；30 条预期策略运行和 B 日志校验通过，无待复核声明。
`gate_passed.json` 的通过范围仅为执行/格式，不代表语义质量已获批准。
主实验随后按已建立依赖自动开始，没有改输入、方法或模型。

以下主实验分片均执行同一 v3 冻结包、B `ea39057` 输入；每片 10 题、三档、十配置。
结果位于 `a_work/results/replay/main_eval_revised_v1_20261116_v3/shard_NNN/`。

| 独立分片 / 作业 | H100 节点 | 开始–结束 CST | 状态 / Slurm 用时 |
|---|---|---|---|
| 000 / 12490887_0 | ccc0419 | 17:04:34–17:12:16 | COMPLETED 0，7 分 42 秒 |
| 001 / 12490887_1 | ccc0419 | 17:12:33–17:17:25 | COMPLETED 0，4 分 52 秒 |
| 002 / 12490887_2 | ccc0419 | 17:17:49–17:23:08 | COMPLETED 0，5 分 19 秒 |
| 003 / 12490887_3 | ccc0419 | 17:23:36–17:28:31 | COMPLETED 0，4 分 55 秒 |
| 004 / 12490887_4 | ccc0419 | 17:29:02–运行中 | RUNNING；核对时 2 分 19 秒 |

本次四个已完成分片的 80 个 ordinary/Oracle worker 全部完成、无失败。
仍有 25 个分片排队，实际仅占 1 张卡；array 上限 4 不表示已分配 4 张。
主实验尚未结束，也尚未做全量 B 评分汇总。
按当前单卡每片约 5 分钟外推，剩余运行约 2–2.5 小时（估计，含通常分片间隔，
不保证新增排队时间）；增加可用卡会缩短，资源变化会延长。此估计取代之前无实测的时限预算作为当前进度参考。

### 主实验完成及结果分析（2026-11-18）

用户要求分析已完成主实验。本次只做固定 evaluator 评分与结果分析，不调参、不改规则、不启动模型。
保留本文件原有未提交的 11 月 16 日进度记录；以下为后续实际完成状态。

主实验 30/30 分片全部 COMPLETED、退出 0；600 个 worker、9,000 条不同策略运行全部完成。
所有分片均为 ccc0419 的 NVIDIA H100 80GB HBM3，实际峰值并行 1；
11 月 16 日 17:04:34–19:51:40 CST，墙钟 2:47:06，累计 GPU 分配 2:35:31。
沿用 v3 冻结包 `bc412d5911d79c7bb39a615b41cb8d2597738291` + dirty 和 B `ea390574eadd301354d5de46f0d28d328cca5bad`；
当前分支 HEAD `5a13686` 不冒充原运行代码。已重核 332 个冻结文件 hash。

各独立 GPU 作业记录如下；结果均位于 `a_work/results/replay/main_eval_revised_v1_20261116_v3/shard_NNN/`：

| 分片 | 作业号 | 节点 | 开始–结束 CST | Slurm 用时 | 状态 / 退出码 |
|---|---|---|---|---|---|
| 000 | 12490887_0 | ccc0419 | 17:04:34–17:12:16 | 7:42 | COMPLETED / 0:0 |
| 001 | 12490887_1 | ccc0419 | 17:12:33–17:17:25 | 4:52 | COMPLETED / 0:0 |
| 002 | 12490887_2 | ccc0419 | 17:17:49–17:23:08 | 5:19 | COMPLETED / 0:0 |
| 003 | 12490887_3 | ccc0419 | 17:23:36–17:28:31 | 4:55 | COMPLETED / 0:0 |
| 004 | 12490887_4 | ccc0419 | 17:29:02–17:34:13 | 5:11 | COMPLETED / 0:0 |
| 005 | 12490887_5 | ccc0419 | 17:34:39–17:39:43 | 5:04 | COMPLETED / 0:0 |
| 006 | 12490887_6 | ccc0419 | 17:40:10–17:45:26 | 5:16 | COMPLETED / 0:0 |
| 007 | 12490887_7 | ccc0419 | 17:45:35–17:50:39 | 5:04 | COMPLETED / 0:0 |
| 008 | 12490887_8 | ccc0419 | 17:50:59–17:56:15 | 5:16 | COMPLETED / 0:0 |
| 009 | 12490887_9 | ccc0419 | 17:56:50–18:02:04 | 5:14 | COMPLETED / 0:0 |
| 010 | 12490887_10 | ccc0419 | 18:02:29–18:07:22 | 4:53 | COMPLETED / 0:0 |
| 011 | 12490887_11 | ccc0419 | 18:07:40–18:12:48 | 5:08 | COMPLETED / 0:0 |
| 012 | 12490887_12 | ccc0419 | 18:13:05–18:18:29 | 5:24 | COMPLETED / 0:0 |
| 013 | 12490887_13 | ccc0419 | 18:19:03–18:23:57 | 4:54 | COMPLETED / 0:0 |
| 014 | 12490887_14 | ccc0419 | 18:24:31–18:29:41 | 5:10 | COMPLETED / 0:0 |
| 015 | 12490887_15 | ccc0419 | 18:30:12–18:35:30 | 5:18 | COMPLETED / 0:0 |
| 016 | 12490887_16 | ccc0419 | 18:36:04–18:40:52 | 4:48 | COMPLETED / 0:0 |
| 017 | 12490887_17 | ccc0419 | 18:41:00–18:45:59 | 4:59 | COMPLETED / 0:0 |
| 018 | 12490887_18 | ccc0419 | 18:46:18–18:51:32 | 5:14 | COMPLETED / 0:0 |
| 019 | 12490887_19 | ccc0419 | 18:51:44–18:57:14 | 5:30 | COMPLETED / 0:0 |
| 020 | 12490887_20 | ccc0419 | 18:57:35–19:02:45 | 5:10 | COMPLETED / 0:0 |
| 021 | 12490887_21 | ccc0419 | 19:02:57–19:08:00 | 5:03 | COMPLETED / 0:0 |
| 022 | 12490887_22 | ccc0419 | 19:08:24–19:13:16 | 4:52 | COMPLETED / 0:0 |
| 023 | 12490887_23 | ccc0419 | 19:13:44–19:18:44 | 5:00 | COMPLETED / 0:0 |
| 024 | 12490887_24 | ccc0419 | 19:19:01–19:24:22 | 5:21 | COMPLETED / 0:0 |
| 025 | 12490887_25 | ccc0419 | 19:25:00–19:29:39 | 4:39 | COMPLETED / 0:0 |
| 026 | 12490887_26 | ccc0419 | 19:30:18–19:35:34 | 5:16 | COMPLETED / 0:0 |
| 027 | 12490887_27 | ccc0419 | 19:36:13–19:41:23 | 5:10 | COMPLETED / 0:0 |
| 028 | 12490887_28 | ccc0419 | 19:41:36–19:46:37 | 5:01 | COMPLETED / 0:0 |
| 029 | 12490887_29 | ccc0419 | 19:46:52–19:51:40 | 4:48 | COMPLETED / 0:0 |

原始评分汇总位于 `a_work/results/analysis/main_eval_revised_v1_20261118/`，不覆盖 GPU 原输出。
collector/evaluator 均退出 0；9,000 条日志 status=ok，validation issues 为 0，待复核声明记录 1,427。
固定 B evaluator 的 31 项测试全部通过；分析脚本对运行唯一性、缺失、计数、并发质量一致性等断言通过。
分析来源和派生表 hash 分别保存在 `manifest.json`、`analysis_manifest.json`；脚本为 `analyze.py`。

- 确认完整：Wait-All 551/900、Time-Only 391/900、First-Evidence 231/900、Prompt 415/900、LoRA 503/900、Oracle 900/900。
- 完成未知：Wait-All 63、Prompt 305、LoRA 294。主方法 value-match 只自动映射准确匹配值；高子集 EM 存在选择效应。
- LoRA 子集 Unit EM 94.9% 仅覆盖 606/900，Prompt 83.4% 覆盖 595/900，不能与 Wait-All 65.8%（837/900）直接比较整体正确率。
- 官方非 Oracle UCR 均保持 null；按既有 B 上下界定义汇总，LoRA 登记声明错误率范围 8.3%–32.0%，Prompt 9.5%–36.5%，Time-Only 53.6%–56.8%，First-Evidence 71.1%–74.5%。这是标签未知的范围，不是置信区间或完整正文错误率。
- long 配对 TTFGI 提前：Prompt 2.42 秒（105 对）、LoRA 3.64 秒（112 对）；short 分别晚 1.65、0.63 秒。long 串行 TTCA 仍分别晚 1.96、0.90 秒。
- 并发质量与串行一致；short 相对自身串行 TTCA 改善 Prompt 2.23 秒、LoRA 1.57 秒，long 均 0.50 秒，仍为模拟并发。
- LoRA judge 平均 0.85 秒，Prompt judge 1.57 秒；单答案组 LoRA 确认完整 37/60，Prompt 50/60，不能称所有题型都胜出。

详细表、指标解释和研究结论见 `a_work/evaluation_notes.md` 的 2026-11-18 节；A README 已增加结果入口。
F1 的冻结运行与原始结构化评分完成，独立映射、完整语义、语音对齐与 C 人评仍待验收。
本次没有补别名、自动改分、改 gold/evaluator、改提示词/阈值、模型调用、commit 或 push。

### B 评估进度核对与 A/B 接口对齐（2026-11-18）

B 分支最新为 `ea390574eadd301354d5de46f0d28d328cca5bad`。300 道修订题、两份配套 gold 和 900 条模拟检索 trace 已交付，并用于上面的主实验。B 数据 manifest 仍待记录人工 gold 验收和延迟方案定稿。
自 `15f0e02`（11 月 3 日）之后，`b_work/eval/` 无差异。冻结评分器与当前 B 的核心代码、测试一致，本次 31 项测试通过。评分器可以校验日志、评分已登记声明并接受人工关系映射。整段事实抽取、独立语义支持判断、纠错计分、C 音频对齐和配对置信区间仍列为后续工作。

当前优先处理 A2/B4 的声明映射。主实验中 LoRA、Prompt、Wait-All 分别有 294、305、63 条完成状态未知。用虚构数据复现同一个错误答案在 baseline 直接记为 `wrong_gold_value`，在主方法按值猜测映射时进入 `claim_mapping_required`，提供按关系复核的映射后同样记为 `wrong_gold_value`。

建议的交接与验收顺序如下。

1. A 先用同一批获准 debug 回放对齐 Prompt、LoRA、Wait-All。给 B 的例子同时包含待复核项和已自动评分项，特别覆盖关系/对象不符、同值歧义、等价改写、正文未表达的元数据值和 gold 外声明。
2. A/B 共同看同一批例子。先根据声明关系判断是否对应 gold 单元，再判值是否正确，最后用当时可见的引用判断是否有依据。保留正文未表达与 gold 外声明的原始分类，分别约定如何处理。
3. B 给出复核口径和独立映射。现有 `--reviews` 接受按 `run_id`、`record_index`、`claim_index` 定位的映射。A 绑定原日志 hash，用原输出离线重评到单独目录，比较覆盖率、完成状态和结论变化。
4. 开发集复核做通后，再按一致规则安排主实验的独立复核。串行、并发的声明可以核对重复后复用映射，各自保留时间。配对区间和正文语义评分分别记录进度。

当前完成了代码与产物核对及虚构复现。A2 仍待独立复核，B4 的语义、置信区间和音频计分未验收。

### R1 组合路径规则与训练判断（2026-11-18）

用户确认 A 侧采用以下规则。只有省略推得的否定时，必要结论保持 `UNRESOLVED`。有直接确认胜出候选的证据时可以作答。明确排除一个候选时，只有题目确实限定两个候选且恰有一个成立，才可通过问题预设推出另一候选。保留实际采用的证据路径，B 侧的 gold、评分和 SFT 标注口径待对齐。

这次决定改变结论采用证据的条件，现有 judge 输入、输出字段和 adapter 仍可使用。14B Prompt 和 4B LoRA 共用 `normalize_reply` / `derive_conclusion`，先验证运行时校验即可。需检查省略依赖经中间单元传递和全部依赖已支持的路径。题中出现候选名字、依赖数为二或模型没有打 omission 标记，都不足以独立确认明确排除和唯一性。

只汇总本地 `sft_v0` 的 1,991 条 train 和 486 条 dev 记录。标为受支持且使用 presupposition 的单元分别有 62 和 6 个，未发现它们直接依赖标为 omission 的 `no`。这是旧标签的直接依赖统计，真实模型误标和间接路径仍需验证。只有现有 judge 在获准开发题上仍经常混淆明确否定和省略，或无法提供校验所需的依据时，再请 B 核对 SFT 标注和补例，评估继续微调。

用四个虚构的已解析判断调用现有 `derive_conclusion`。仅省略、直接确认 B、明确排除 A 三种情形当前都返回 `SUPPORTED`。当 A 的省略否定和 B 的直接证据并存时，现有代码把两条都放入引用，并把结论的 presupposition 标志清为 false。直接可引用 B 的证据，应保留作答并记录真正采用的依据。对 v7 Prompt 和 LoRA 分别检查 101、99 个历史 debug judge 调用的原始标志，同一快照未见两种组合标记，因此需要专门的对照用例。

人工验收只需先用上述少量例子，确认题目是否保证恰有一个候选成立、每个时点的原句支持了什么、结论应引哪条证据。B 据此对齐 gold 支持路径和评估口径。四例是当前代码的 CPU 检查，尚未运行现有权重验证，也未实施新规则。

用户提供了与 B 组员对齐的例子。只见省略 `e1` 判 `UNRESOLVED`，见直接支持 `e2` 引 `e2`，见明确排除 `e3` 且二选一成立时引 `e3` 并记录用了题目预设，`e1` 和 `e2` 并存时只需引 `e2`。用虚构 gold 在现有 B evaluator 验证了四种支持结果和 `e1+e2` 时仅引 `e1` 的反例，五项断言通过。当前 B 远端仍为 `ea39057`，新版 gold 待交付。A 可并行做虚构用例和获准的 debug 诊断，新口径的正式评分使用对齐且版本匹配的 B 输入。路径级标记的统计另需核对。

按题去重后，SFT 的 62 条 train 和 6 条 dev 预设支持判断分别来自 14 道和 1 道题。逐题核对均未写明“两个候选恰好一个成立”。标签中有 `yes` 支持依赖的为 train 51 条、跨 11 题，dev 6 条、跨 1 题；既无 `yes` 也无 `no` 的为 train 5 条、跨 2 题。只有 `no` 作为已支持的是非依赖且无 `yes` 的 6 条均来自同一道成立年份比较题。引用句明写被排除乐队成立于 1994 年，题干用 `Which ... A or B?`，需由 B 复核这一题的排除路径是否符合最终约定的候选唯一性要求。该统计仅覆盖 SFT，旧标签和代码未改。

按用户要求补齐全部 SFT 预设路径复核。逐条检查原来已标预设的 68 条判断，并递归追溯省略否定的依赖，额外查出 25 条未标预设的多依赖结论。共 93 条、21 道 SFT 题。A 的逐条建议如下。

- 68 条已有正面证据支撑候选。保留 `SUPPORTED`，用正面证据作为结论路径。其中 18 条来自额外查出的未标预设结论。
- 6 条排除 Foo Fighters 后直接推出 Goon Moon。按题干没有保证恰好一个的口径，建议先判 `UNRESOLVED`。某些快照已有 Goon Moon 的唱片发行年份，仍缺成立时间。
- 8 条的现有引用未完整支持所问关系。Cowpea 4 条缺开花植物分类的明确证据，Florence Welch 3 条只支撑主唱身份，TAAG 1 条缺与 Air 26 的竞争关系。按现有严格口径建议 `UNRESOLVED`，把原句与缺口交 B 确认。
- 4 条歌曲命名问题按题干给定的命名前提单列。7 条「两者是否都满足」按原口径单列，本次二选一规则不延伸到这两类。

完整建议记录在 `a_work/results/analysis/sft_premise_path_review_20261118/`。`question_review.csv` 按题汇总，`judgment_review.csv` 提供源行、证据、旧引用、建议和 B 复核列。脚本核验 93 条及其分组、证据可见性，并记录两份源 SFT 的 hash。此为 A 侧审阅建议，训练源文件和 B gold 保留原样。

用户随后授权实现 A 侧校验并运行开发实验。独立分支 `a-judge-premise-path` 从主实验分支的 `5a13686` 创建，继续保留已有未提交说明。`run_replay.py --strict-candidate-paths` 启用新校验并记录所选证据路径。直接确认优先，排除需明确的二选一前提及能核实的明确否定。同一份模型输出分别跑旧、新校验，不改 prompt、adapter 或 B 数据。排除分支按保守英文句式核对；未能核实的改写保持 `UNRESOLVED`。

开发运行 `judge_premise_paths_20261118_live` 计划使用现有 14B Prompt 和 4B LoRA，各运行 7 个虚构对照及 20 道 debug 题的已记录证据快照。不使用预留数据。回放先核验 113 项 A 测试和 19 项控制实验测试，全部通过。离线匹配 model-unit 请求得到 Prompt 52、LoRA 50 个快照；LoRA 另有 2 个缺少对应请求，未纳入同输入对照。两模型各 2 个快照由预设改记直接支持，标签均不变。详细输出在 `a_work/results/analysis/judge_premise_paths_20261118_offline/`。

H100 作业 `12545106` 已提交，提交退出 0，首次核对为 PENDING。账号 `dilek-ic`、normal QoS、nice 0，scavenger/secondary，1 张 H100、40 分钟。源码父 `5a13686a687394228a58c48b668b0592606e2715` + dirty，debug 来源 `a2808f17558076291ec439d2ced8a00be8c52281`。快照和输入 hash 位于 `a_work/results/code_snapshots/judge_premise_paths_20261118_live/manifest.json`，计划结果在 `a_work/results/judge/judge_premise_paths_20261118_live/`。

另跑了完整的虚构策略回放。`e1` 在 0 秒到达、`e2` 在 4 秒到达。相同模拟 judge 回复下，旧规则在 0 秒作出 Final Answer 决策并引 `e1`，新规则在 4 秒确认后才作出 Final Answer 决策并只引 `e2`。两项断言均通过，记录在离线目录的 `fictional_policy_check.json`。

按用户要求撤回临时分支，工作区切回原 `a-main-experiments`。切换前后已核对全部未提交改动及未跟踪文件内容一致，`a-judge-premise-path` 本地引用已删除。已提交作业保留原快照和记录，快照的分支名反映提交时状态。
