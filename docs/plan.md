# 剩余工作计划

本文列出到论文初稿的工作、依赖、完成标准和运行记录。实验定义见 `experiment_spec.md`。
D 编号对应 spec 第 11 节。一次只做一步；只做部分就标“进行中”。

截止日期：待用户填写学期结束日期、目标会议截稿日期。
最后核对：2026-11-11。当前任务只处理 **P0 的文档整理和进度核对**。
**用户自行提交。助手不 commit、不 push，不自行创建其他工作区或仓库副本。**

## 现状与证据

| 部分 | 当前状态 | 依据与限制 |
|---|---|---|
| 异步检索诊断 | 已有历史实验记录 | `experiments/async_retrieval_latency/`；旧数字需补齐运行元数据后引用 |
| MoshiRAG 可控性 | Wait / Progress / Final 有开发结果，Partial 不可靠 | `a_work/moshirag_control/FINDINGS.md`；单种子、第二人复核未完成 |
| A 控制器与 judge | 四个规则 baseline、Evidence-Aware、prompt / LoRA / oracle、模型拆题与生成 | 远端 `a-answer-gen` @ `9fb9adc`；不等于最终配置已冻结 |
| A v5 回放 | 本地记录显示已运行并经固定 B evaluator 评分；部分映射由助手辅助复核 | `a_work/evaluation_notes.md`（未提交）；仍有待复核项，不能当整体 UCR 或独立人工复核 |
| A 后续优化 | 两轮 v7 在 2026-11-11 完成，退出 0；仍未经过 B evaluator | 作业 12307492 / 12307493，A100，text/rate；当前代码与运行快照不同，不能算整分支验收 |
| A ASR / TTS | 本地有 Whisper、Piper、调用回放和 smoke 脚本；作业 12308419 查询仍排队 | 2026-11-11，PENDING / Priority，申请 A100；主时间轴仍模拟，smoke 未验收，S1 未完成 |
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
| A2 | 用固定 B evaluator 评分真实回放；复核 claim 映射；确认 Wait 日志要求 | A+B | A1 | run_eval 退出 0；全部 review queue 复核；自查差异有解释，不能仅凭退出 0 宣告通过 | 进行中：有原始与辅助评分，待独立复核；不是整体正式分数 |
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
