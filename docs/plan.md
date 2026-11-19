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


### 集群维护与后续提交（2026-11-11 12:21 CST）

用户要求：后续作业选择未受维护影响的分区和节点。本次只检查调度信息并更新规则，
没有提交真实作业，没有取消或修改既有任务，也没有改实验参数。
证据来自当前 `scontrol show reservation -o`、`sinfo`、`sinfo -R`、
`scontrol show job`、`sacctmgr show assoc` 和 `sbatch --test-only`，不是实验性能结果。
核对时代码基线为 `a-cascade` @ `3380a7b`，本次文档改动尚未提交。

| 项目 | 查询时状态 | 后续处理 |
|---|---|---|
| `gpu_troubleshooting` | ACTIVE，2026-11-10 09:00 至 2026-11-20 09:00，只覆盖 `ccc0436`（L40S，scavenger） | 当前不是全分区维护，避开该节点 |
| `2027_Jan_Maintenance` | INACTIVE，2027-01-13 06:00 至 2027-01-27 06:00，覆盖登录节点及大量计算节点 | 尚未生效；任务运行窗口涉及该日期时重新核对，不能假设换分区即可绕过 |
| `secondary` | UP，有 H100 候选节点，申请 1 卡 / 8 CPU / 64G / 2 小时的 test-only 验证通过 | H100 评估继续默认此分区；可接受申请不代表马上有空卡 |
| `IllinoisComputes-GPU` | UP，有 A100/H200，当前可见节点没有 H100；已有 A100 作业正在运行 | 不作为 H100 的替代目标；已有开发作业保持不动 |
| `scavenger` | UP，有 H100；存在抢占/重排队条件，需要额外核对 | 不自动启用为回退分区 |
| `ic-express` | 当前 H100 资源为 MIG 切片，且分区限制账号 | 不把它当作整卡 H100 的直接替代 |

现有作业 `12306379` 查询时 RUNNING，节点 `ccc0387`，A100；
`12306380`、`12308419` 查询时 PENDING，原因 Priority，不是维护。
这是时间点记录，之后每次提交仍需重查。GPU 结束状态和产物由对应运行的验收步骤补录。

后续规则已写入 `CLAUDE.md`，A README 增加提交前检查说明。
现有评估脚本已经默认 secondary/H100；训练和 smoke 的候选分区在本次检查时均未全区维护，
本次没有盲目缩小其候选列表或变更 GPU 约束，也没有修改已排队使用的冻结快照。
未知的共享存储/网络停机不能仅凭分区 UP 排除；如有额外维护公告需一起核对。

### 独立级联英文 README（2026-11-17）

按用户要求替换 `cascadesystem/README.md`，仅说明系统流程、安装/调用方式和逐文件职责。
旧版含实验历史的说明备份到该目录被忽略的 `artifacts/documentation/`，运行产物保留。
根 README 增加英文说明入口。本次只编辑文档，不改变代码、提示词、模型或实验定义，
不读取预留评测数据，不调用 API、录音、下载模型或提交 GPU 作业。
核对文档中的 12 条 CLI 命令可被当前参数解析器接受，31 个本地文件链接均存在；
`--help` 和 `git diff --check` 退出 0。仅文档变更，未重跑功能测试，未 commit/push。

### 独立级联 debug 评估（2026-11-17，用户新任务）

用户要求建立级联评估目录，并明确选择 B 的 debug 20 题加真实 Wikipedia 检索。
新增 `cascadeevaluation/`，复用现有 cascadesystem，不修改控制器、提示词或正式实验定义。
数据固定到 B commit `ea390574eadd301354d5de46f0d28d328cca5bad`，只定向读取
`step2/prepared/samples_debug.jsonl` 与 `step3/gold_debug.jsonl`，导出独立问题和评分参考。
运行器只读取问题，离线评分器才读取参考答案；没有读取任何预留题、gold、trace 或其派生内容。

这是应用开发诊断：报告必要答案值的 EM/F1、整题值覆盖、引用格式、状态和实测文本/墙钟时间。
不把实时网页 ID 当作 B 的 trace ID，不计算正式 UCR/TTFGI/TTCA，不宣称语音延迟或独立语义正确率。
结果保存在 `cascadeevaluation/artifacts/`，代码与数据哈希写入 manifest；不安装新依赖、不运行 GPU。
初版真实 20 题已运行：2 complete、14 incomplete、4 error，必要答案值 EM 0.10；
45 次搜索 HTTP 429 明显影响结果，另有 judge 单元缺失/拆题依赖错误各 2 题，原始记录保留于
`runs/debug-wikipedia-20261117-v1/`。不能把该数值直接当作模型能力结论。
批量传输层已增加串行间隔、maxlag 和 Retry-After 有界退避，普通应用源码不变；复跑结果待补。
新增评估测试 22 项通过、退出 0；现有 cascadesystem 测试 105 项通过、退出 0。

复跑已完成：`cascadeevaluation/artifacts/runs/debug-wikipedia-20261117-v2/`，20 题全部有运行记录。
系统状态 6 complete / 6 incomplete / 8 error；必要答案值 EM 0.225、F1 0.3042857，
全部必要值精确匹配 4/20；这些是字符串值诊断，不是独立语义正确率。
71 次 Wikipedia HTTP 请求全部成功，无搜索错误；8 个流程错误分别为 judge 单元返回不全 6 次、
拆题占位符/依赖不符 2 次，未修改生产提示词或隐藏失败。
18 条已输出声明的引用格式检查通过，不将其表述为事实正确率 100%。
每题墙钟中位数 11.347 秒，包含限速等待，不是语音/模型独立延迟；没有计算正式 UCR/TTFGI/TTCA。
记录 183 次模型调用（179 ok / 4 cancelled），其中已返回用量的 179 次合计 210391 token；
取消请求可能仍计费，不用日志用量推断最终账单。

运行代码为 `a-cascade`，父 `c23d6ae6e7250b793c026e7ec01ae9166728f5af` + dirty，
两个包的源码集合 SHA256 为 `34e3e2c3a02283a8d7fa277c8ef819baedeb9cf4f4d1c7df4226c2cca60e767b`；
运行开始后源码未改变，清单见该运行的 `source-manifest.json`。本地 Python 3.14.3，
远端 Tinker 硬件未知，无本地/集群 GPU 作业。执行退出码 1 表示已记录流程错误，并非缺失报告。
报告为 `summary.md`、`summary.json`、`scores.csv` 和 `scores.jsonl`，首轮及各题事件/证据/调用保留。
检查确认密钥未进入新代码和运行产物，输入/参考/输出均被忽略，`git diff --check` 退出 0。
评估目录与该开发诊断已完成；不代表正式评测步骤完成。没有 commit/push。

### 独立级联输出协议修复（2026-11-17，用户后续任务）

用户要求修复上述结构错误。仅修改 `cascadesystem`，没有调整旧 A/B 实验定义。
新增 `protocol.py`：已知占位符缺失的显式依赖可补全，但必须重新通过严格 DAG 校验；
其他无效计划最多重写一次。judge 明确接收全部 required_unit_ids，缺项/重复/额外 ID
与逐字引用错误共用每个可见证据快照一次修正机会；未通过仍拒绝，不填造旧判断或答案。
原始拆题/judge 输出先落日志再校验，记录具体缺失/重复/额外 ID 与修正是否耗尽。
修正不接触未来证据，不重试网络/鉴权错误。提示仅使用虚构示例，未读取预留评测数据。

新增 13 项协议回归，当前 cascadesystem 共 118 项通过、退出 0；级联评估 22 项通过、退出 0。
保持相同 debug 20 题、2 秒 Wikipedia 间隔、2 次限流重试和 180 秒问题预算，
新评估运行保存在 `cascadeevaluation/artifacts/runs/debug-wikipedia-20261117-v3-protocol/`。
旧 v1/v2 结果保留，不修改 gold、评分方法、模型选择或当前 API 配置，没有新增依赖或 GPU 作业。

该复跑已完成 20 题，退出 0：8 complete / 12 incomplete / 0 error；上一轮为 6 / 6 / 8。
3 份计划触发本地显式依赖补全并通过完整校验；没有触发模型修正，也没有修正耗尽。
93 次 Wikipedia HTTP 请求均成功，无搜索错误。旧 8 个报错样本本轮为 1 complete / 7 incomplete。
必要答案值 EM 0.325、F1 0.4261111，全部必要值精确匹配 6/20；上一轮为 0.225、0.3042857、4/20。
这些是一次 debug 值匹配对比，不是独立语义准确率，也不能把收益全部归因于协议修复。
系统 complete 只表示计划中的必要单元已支持，不保证计划完整、关系正确或与 gold 一致。
36/36 引用格式检查通过，不代表事实正确率；正式 UCR/TTFGI/TTCA 仍为 null。
首条事实文本中位数 10.514 秒（17 题有测量），最终文本 15.162 秒（20 题）；
上一轮分别为 9.551 秒（13 题）和 11.347 秒（20 题）。没有语音播放，不作为声学延迟。
记录 219 次模型调用（215 ok / 4 cancelled），215 次已返回用量共 282204 token，不推算账单。

运行名 `debug-wikipedia-20261117-v3-protocol`，分支 `a-cascade`，父 commit
`c23d6ae6e7250b793c026e7ec01ae9166728f5af` + dirty；源文件集合 SHA256
`8442fa7e83f37224f7067811b66c6f5b4978e634e067679cc96cf54672db119f`。
B debug 来源仍为 `ea390574eadd301354d5de46f0d28d328cca5bad`、`debug-v0`。
本地 Python 3.14.3，远程 Tinker 硬件未知，无本地/集群 GPU 作业。
汇总见运行目录的 `summary.md`/`summary.json`，协议诊断见 `protocol-analysis.json`；
源码与清单一致。118 项系统测试和 22 项评估测试通过、退出 0；没有 commit/push。
协议报错修复完成；12 题 incomplete 及答案值未匹配属于后续检索/拆题/语义支持问题，未宣称解决。

### 独立级联接入 B debug 回放评分（2026-11-17，用户后续任务）

用户要求按 B 标准评估现有 cascadesystem。新增独立的 B debug 固定证据回放入口，
保留原实时 Wikipedia 路径；只把证据提供方切换为调度器，拆题/判断/生成/校验逻辑保持现有实现。
只定向提取 B commit `ea390574eadd301354d5de46f0d28d328cca5bad` 的 debug gold、debug trace，
及 `eval` 中 4 个评分源码文件；不读取预留题或其派生内容，不修改 B 代码、gold 或正式实验定义。
模型仅接收题目与已到达证据，保留 B 原始证据 ID 和标题。普通运行器不读取 gold。
沿用 B 的 immediate/short/long 三种条件，20 道题共 60 次运行；真实 Tinker，关闭外部搜索与音频。
回放以墙钟等待已有证据日程，未测语音时间保持 null，B timing_kind 为 unknown。
默认调用 B 原评分函数，不假定控制器单元与 gold 对齐；未映射声明进入 B 复核队列，分数保持 null。
另可显式运行 B 的唯一精确值近似映射诊断，但不作为独立语义复核或正式整体 UCR。
若发生撤回，保留原输出且将该次运行排除评分为 error，因为 B 当前没有实现撤回规则。

进度：118 项系统测试通过；新增回放/实际 B 评分器回归 14 项，评估测试总计 36 项通过，退出均为 0。
新测试最初使用的中文 fixture 不适用 B 的英文整词定位；改用虚构英文 fixture，断言未放宽。
数据输入为 `cascadeevaluation/artifacts/inputs/b-debug-traces-v0/`（20 题、60 trace）。
独立运行目录拟为 `cascadeevaluation/artifacts/runs/b-debug-20261117-v1/`，结果待补。
无新增依赖，无 GPU 作业，无 commit/push。共享文档在当前分支，待用户提交后同步。

### 重建独立 eval debug20（2026-11-17，用户最新要求）

用户明确要求删除旧评估，创建 `eval debug20` 并自行执行真实运行。
已停止旧后台 `b-debug-20261117-v1`，中断前控制台记录 46/60 次完成；不作为完整评测结果。
按用户要求删除整个未跟踪 `cascadeevaluation/`，包含旧输入、日志、报告和缓存；
此删除覆盖此前失败产物保留约定，历史段落中的旧产物路径不再可用。
未删除 B 分支原始 `b_work/eval/`，没有切换分支，也没有改 B 的评分器或 gold。

新目录为 `eval debug20/`：独立 CLI、debug 输入准备、证据调度、B 日志适配和原评分器调用。
默认选择已有 short 条件（1/3 秒），运行 20 道题；all 为三种既有条件合计 60 次。
调度器在每次交付时合并全部已到达批次，未来句子仍不进入当前模型调用或修正调用。
保留 cascadesystem 的 question-only 拆题、判断、回答、校验以及可选 evidence_stream 接口。
模型与参数、B 标签和证据支持规则不变；普通运行器不读 gold，不调用实时搜索、ASR 或 TTS。
默认 B 未映射声明进入复核，null 不补零；可另存 B 自带的唯一值近似映射诊断。
未测语音时间保持 null；B 当前不支持的撤回被保留并标记适配错误，不伪造正常得分。

已仅离线准备 B `ea390574eadd301354d5de46f0d28d328cca5bad` 的 debug-v0（20 题、60 trace），
位于 `eval debug20/artifacts/inputs/b-debug-v0/`，输入和 B 源码哈希写入 manifest。
没有读取预留题或其派生内容。当前分支 `a-cascade`，父 `c23d6ae6e7250b793c026e7ec01ae9166728f5af` + dirty。
新回归 15 项及系统 118 项通过，退出码均 0；CLI 帮助与输入准备退出 0。
本地 Python 3.14.3，无新增依赖和 GPU 作业；本次重建后未调用真实模型 API，真实运行交给用户。
新目录说明和命令见 `eval debug20/README.md`。无 commit/push，共享文档待用户提交后同步。

最终检查：从同一固定 B commit 提取的 31 项原评分器测试也通过、退出 0。
两个包源文件集合 SHA256 为 `fa14fad487732b5afbdea12605146abccad69a338fdddf348ba1fb7d46846340`。
确认旧目录不存在，新目录尚无真实 runs 产物，README 本地链接有效，密钥扫描无泄露，
输入、缓存原评分器和本地密钥均被忽略；`git diff --check` 退出 0。

### 用户完成 Debug20 后的离线分析（2026-11-17）

用户运行 `eval debug20` 的 all 条件，运行名 `20261118T021730Z-fff3ebf9`，60/60 次记录齐全。
系统自判 complete 40、incomplete 20，无运行级错误/超时/缺失；三个条件 complete 为 immediate 14/20、
short 15/20、long 11/20。B 报告 ok 58 / error 2，两个 error 为 0006/0012 的撤回计分不兼容。
B 有 106 条声明待映射复核，0 条声明完成评分；只有三次无事实输出得到数值 Unit EM/F1=0，
不能把该 0 当作整体准确率。整体 UCR 和语音时间仍 null。

离线分析发现 VERIFY 把部分事实是否回答整个问题混作有效性判断；19 次运行有 facts_rejected，
其中 6 次最终 incomplete。4 道 NASA 题 × 3 条件共 12 次全部自判 complete，却无任何 Partial Answer；
short/long 的 8 次均曾以缺少第二部分为由拒绝第一部分。
验证输入还遗漏当前输出单元的依赖证据，0003/0009 出现因此拒绝桥接结论的理由。
另有 judge 漏判、否定结论误标 CONTRADICTED、0049–0051 拆题误解二选一问题，
以及 0046–0048 与 B by_omission 规则不同等问题。0057 正文结论、声明元数据和最终状态不一致。
本次没有修改代码、提示词、B gold 或评分规则，没有调用真实 API 或访问预留数据。

产物在该运行目录：`analysis.md`、`analysis.json`、`analysis_runs.csv`；原报告与日志保留。
用 B 原评分器离线重算默认汇总与保存值一致，60 个 trace ID、政策日志哈希、当前源码清单均核对通过。
代码为 a-cascade、父 `c23d6ae6e7250b793c026e7ec01ae9166728f5af` + dirty；
源码 SHA256 `fa14fad487732b5afbdea12605146abccad69a338fdddf348ba1fb7d46846340`。
B commit `ea390574eadd301354d5de46f0d28d328cca5bad`，debug-v0；本地 Python 3.14.3，
远程 Tinker 硬件未知，无 GPU 作业。墙钟中位数 9.065 秒，各次之和 576.740 秒，不是语音延迟。
日志共 575 模型调用（547 ok / 28 cancelled），已返回用量 692207 token，不推算账单。
本次为只读代码的结果分析，未重跑功能测试；没有 commit/push。后续先修验证范围和依赖上下文，再评估重试。

### 独立级联的输出验证与末尾复核修复（2026-11-17，用户后续要求）

按用户要求修复独立 cascadesystem，不修改旧 A 控制器、B gold/评分器、预留集或正式实验定义。
新增 `grounding.py`，为当前输出补齐已可见的传递依赖事实和引用；依赖仅供核验，不授权额外输出。
VERIFY 按本次 action/output_unit_ids 检查所选事实，不再把未回答其余部分当作部分事实无效。
Tinker 要求 facts_valid=true，且 expressed_unit_ids 恰好覆盖本次允许的输出；措辞/单元声明失败退回事实模板，
生成草稿失败后的模板也必须经过事实校验，ProviderError 不再退回未经复核的事实播放。
旧自定义 provider 保留原回复接口，显式提供的新单元声明仍校验；Tinker 启用严格契约。
最终事实被拒绝时，重新传播依赖阻塞，避免父单元失效而子单元仍标为支持。

检索耗尽、已有证据、仍有必要 UNRESOLVED 时最多增加一次 judge 语义复核；只重看该单元及依赖闭包，
相同证据快照，完整 ID、引用、逐字引文和依赖规则不变。格式不合格则拒绝，不额外修复或循环重试。
复核得到充分支持后可完成回答；仍无证据继续 incomplete；真实冲突不被强行转成否定答案。
PLAN 加强原问题意图、必要单元和候选选择约束；JUDGE 明确有依据的否定应 SUPPORTED，
增加标题/代词/显式关系链的核对指引。不自动启用 B 的 by_omission 职业否定规则。
拆题语义和正文是否存在额外事实仍依赖模型，不能把提示改动宣称为已消除语义错误。
新增 verification_reply、draft_rejected、semantic_review_* 日志；核验事件不用 action 字段冒充输出事件。

新增 21 项虚构回归，全部系统测试 139 项通过、退出 0；Debug20 评估测试 15 项通过、退出 0。
保持已有测试和断言不变。检查覆盖：部分先答且最终不重复、三级依赖引用、未知/额外单元退回模板、
严格验证缺字段、生成/核验故障不输出事实、父事实拒绝后阻塞子事实、一次复核恢复/不恢复/假引用/鉴权失败。
本次只做离线测试，没有调用真实 API，没有新依赖或 GPU 作业。原 60 次结果原样保留，真实收益和延迟待用户新运行。
分支 a-cascade、父 c23d6ae6e7250b793c026e7ec01ae9166728f5af + dirty，无 commit/push。

复核闭包中的前置实体改变时，闭包外依赖该实体的旧支持结论也会失效；真正无关事实保持原状态。
测试过程发现新核验日志复用了 action 字段，会被既有消费者当作语音动作；已改为 output_action，
保留原有输出事件接口，没有修改既有测试。

最终源码集合 SHA256：`5b8935423ee4c493d6ad172329a762645150a81618214343bc6781c57c1029c6`，
37 个源文件的清单另存于忽略的 `cascadesystem/artifacts/changes/verification-20261117/source-manifest.json`。
旧运行政策日志哈希未变，README 链接有效，密钥未进入修改源码/文档，`git diff --check` 退出 0。
CLI 参数帮助退出 0；后续应新建运行而不是用改动后的源码 resume 原快照。

### 最新运行回答汇总（2026-11-17，用户要求）

按用户要求整理最新运行 `20261118T030106Z-03595158`：20 道 debug 题、60 次条件运行，均有 Final Answer。
在原运行目录新建 `final_answers.md`（按题和条件汇总最后回答）、`full_responses.md`（保留部分回答/撤回/最终回答顺序）、
`final_answers.csv`（可筛选的全量记录）和 `final_answers_manifest.json`（来源哈希及运行版本）。
源状态为 48 complete / 12 incomplete，仅照录系统状态，不作为正确率。未重写回答或合并消除撤回提示。
60 行 CSV 回读与原始回答一致，60 个源 run.json 哈希未改变；输入仅为该 debug 运行，无预留数据或 gold 评分。
无代码或提示词变更，无 API 调用，未重跑功能测试；产物均在 Git 忽略目录，无 commit/push。

### 第一题 long 语音回放示例（2026-11-17，用户要求）

用户要求听最新运行第一题 long 的完整输出。提取 `20261118T030106Z-03595158/samples/0003/run.json`，
保留原始 Backchannel、Partial Answer、Final Answer 三段英文文字，使用本机 Microsoft Zira Desktop 重合成。
沙箱内 System.Speech 初始化失败；获准在沙箱外调用本地 TTS 并播放成功。无模型/搜索 API 或新增依赖。
音频在该运行 `audio_0003_long_replay/question1_long_replay.wav`，长 20.757 秒，另存 transcript/replay/synthesis 元数据。
按日志文本就绪时间安排：3.362 秒开始确认，8.875 秒开始部分回答；最终文本原在 13.530 秒就绪，
因前段合成语音直到 14.538 秒结束，串行回放在 14.538 秒开始最终答案。
这是新合成的回放，不是原评估录音或原始声学时间。WAV 可读、时长与记录一致，播放进程退出 0。
生产代码/原运行结果不变；失败合成记录保留，音频及辅助回放脚本均在忽略目录。

### 对最新结果进行 B 离线值匹配诊断（2026-11-17，用户要求）

对 `20261118T030106Z-03595158` 调用 B 原版 scorer，显式启用 allow_value_match，另存
`b_eval_value_diagnostic/`，原严格报告保留。没有调用 API、修改代码/提示词/gold 或读取预留数据。
60 次运行，B 为 56 ok / 4 error（撤回适配限制）；数值 Unit EM/F1 覆盖 36/60，子集均值 0.75/0.75。
113 条可处理声明中 85 条唯一精确值近似映射，80 满足支持规则、5 未满足，28 条仍待复核。
整体 UCR 仍 null，不能把子集 0.75 报告为整体准确率，也不把近似映射当作独立人工复核。
第一题 long 两个声明均匹配 expected_answer 和支持证据，必要单元 EM/F1=1、grounded_complete=true。
该次映射来源保留 value_guess；详细限制另存 `b_eval_value_diagnostic/interpretation.md`。
报告已生成；CLI 退出 1 是因为包含 4 次适配错误，不表示离线评分运行失败。
运行版本/原日志哈希见该目录 evaluation_config.json；代码来源为 a-cascade/c23d6ae + dirty，
源码 SHA256 5b8935423ee4c493d6ad172329a762645150a81618214343bc6781c57c1029c6，
B ea390574eadd301354d5de46f0d28d328cca5bad、debug-v0；本地 Python 3.14.3，无新 GPU 作业。
本次只执行真实离线评分，不重跑功能测试或模型。无 commit/push。

### 自然完整句子的输出表达（2026-11-17，用户后续要求）

用户询问当前问题并希望回答更自然完整。按“有主语、像对话”处理，不加入未经证据支持的个人意见。
最新真实运行仍为 48 complete / 12 incomplete，剩余 12 次集中在出生地、职业否定、候选题误解及此前职业四道题。
原日志有 82 条事实 utterance，19 条使用回退模板；实际调用的生成和判断仍有语义错误，不能靠润色消除。
本次只改独立 cascadesystem 的表达层：GENERATE 明确主语/谓语、自然陈述、不得朗读内部任务或字段表；
VERIFY 将这种表达缺陷视为措辞问题，不据此推翻有证据的事实。新增 wording.py，Tinker 严格契约下
字段式生成草稿退回完整事实句，删除描述开头的任务动词，未知信息用第一人称说明。
保留所有 approved value 原文；冒号位于真实时间或片名时不一律禁止。不增加单独润色 API 调用。
旧自定义 provider 的模板格式保持兼容；不改变选择哪些事实、依赖、标签、引用、复核预算或 B 的评分规则。
新增 generation_fallback 诊断原因，旧运行和合成音频均不重写；需要新运行观察真实表达效果。

新增 5 项虚构回归。系统 144 项测试通过、退出 0，Debug20 15 项测试通过、退出 0；原测试未修改。
没有调用真实 API，没有新增依赖、预留数据访问或 GPU 作业。
版本 a-cascade、父 c23d6ae6e7250b793c026e7ec01ae9166728f5af + dirty，未 commit/push。

本次最终源码集合 SHA256 `21227f829eae6eff34c2977b9301774e17e51debe91606fb74690420530274f5`，
39 文件清单保存在忽略的 `cascadesystem/artifacts/changes/natural-wording-20261117/source-manifest.json`。
旧运行 policy_log 哈希未变，源码/文档密钥扫描无泄露，README 链接有效，git diff --check 退出 0。

### Debug20 直接生成和播放音频（2026-11-17，用户后续要求）

用户要求新运行直接输出可听音频。Debug20 run 新增 --tts windows / --play，以及按独立题目计数的 --limit。
模型每次发出 utterance 即进入原 SpeechOutput 的分句 TTS 队列，与证据接收和模型计算并发；不是跑完后重写文本。
每题保存 audio/segments 的逐句 WAV、audio/response.wav 合并音频、responses.txt、音频事件和索引。
有播放时合并 WAV 参考实际播放开始时间；仅合成时按语音可用时间生成预览，两者均不伪称原始声学声明对齐。
题目之间等待当前音频队列完成，批次 audio_summary.json 列出每题音频。控制台改为普通文本和路径，JSON 日志留作评分。
语音失败保留模型结果和已合成片段，停止余下题目并使 CLI 非零退出；取消时停止播放/合成并保存带 trace ID 的中断结果。
恢复运行须同时满足音频配置一致。默认不启用 TTS，原文字运行可继续使用。

B trace/gold/原评分器和指标规则未改。audio_enabled 仅作附加信息，原子声明时间仍 null，timing_kind=unknown。
新增 text_pipeline_wall_s（不含模型结束后的音频排空），total_wall_s 含 TTS 排空，不能混作原文字墙钟或正式语音指标。
新增 eval_audio.py 和 9 项虚构合成音频回归。系统 144 项、Debug20 24 项测试均通过，退出 0；现有测试未改。
验证了生成过程中已有音频、顺序播放和排空、缺失片段不冒充完整 WAV、音频失败停批次、取消清理、
limit 保留所选题的条件、无 TTS 不允许 play、音频运行仍不向 B 注入未知的原子声明时间。
本次没有调用真实模型/搜索 API、没有新增依赖、没有启动 GPU 作业；Windows 本地语音先前已验过组件，
本次新集成用虚构 WAV/播放器离线测试，未宣称做过真实 API 加 TTS 的整体验收。
用户可先执行 run --schedule long --limit 1 --tts windows --play，再选 all 批量保存。
分支 a-cascade，父 c23d6ae6e7250b793c026e7ec01ae9166728f5af + dirty，无 commit/push。

最终源码集合 SHA256 `57ffb38b36215a3ebfe0b1f8f416da0a57d1b5aef060c0aa38672a55ab208020`，
41 文件清单存于忽略的 `cascadesystem/artifacts/changes/debug20-audio-20261117/source-manifest.json`。
原运行 policy_log 哈希未变，源码/文档密钥扫描无泄露，README 链接有效，git diff --check 退出 0。

### 更新当前级联系统的英文 README（2026-11-17，用户要求）

本次只完成 P0 中当前应用入口和使用说明的文档更新，不推进模型评估或变更研究定义。
根 README 改为独立 CascadeSystem 入口，包含流程、API 各阶段输入、运行命令、语音和打断、
动态等待回应、complete/incomplete 与增量 Final 的含义、Debug20 固定证据和评分限制。
原上游说明保留到 docs/upstream_moshirag_README.md，修复迁移后的相对链接，并保留许可入口。
同步 cascadesystem/README.md 与 eval debug20/README.md，说明音频文件、完整对话转录、
每题超时与音频排空的区别，以及近似值映射子集分数不能当作整体准确率。
既有手动导出的 final_answers/full_responses 不写成每次运行的自动功能。

文档验证：61 个本地文件链接均存在；仅参数解析检查 17 条应用命令和 13 条评估命令，退出 0。
git diff --check 退出 0。运行源码 41 文件集合哈希仍为上述 57ffb38b...，没有修改实现或测试。
本次未重跑功能测试、未调用真实 API、未合成音频、未读取预留集，也未启动 GPU 作业。
分支 a-cascade，父 c23d6ae6e7250b793c026e7ec01ae9166728f5af + dirty；无 commit/push。
共享文档当前仍在本分支，待用户提交后安排同步 main 和其他组分支。

### 最新 Debug20 回答的离线逐题核对（2026-11-17，用户要求）

本次对应 A2 的开发评分和错误分析，仅处理用户已完成的 debug 运行，不启动新模型实验或冻结指标。
运行 `20261118T042104Z-af3cd283`，20 道 debug 题 × immediate/short/long，共 60 次；
Tinker openai/gpt-oss-120b，源码集合 SHA256 `57ffb38b36215a3ebfe0b1f8f416da0a57d1b5aef060c0aa38672a55ab208020`，
父 c23d6ae6e7250b793c026e7ec01ae9166728f5af + dirty；本地 Python，无 GPU 作业。
B 固定 `ea390574eadd301354d5de46f0d28d328cca5bad`，debug-v0，gold 哈希 29629fa9...，trace 哈希 3b50bd41...。
原 policy_log SHA256 `7ce860ccdf62e4e4334f0570d7af4990f2b7901a85878c17b3fe966988c945ab`。

产物另存该运行 `answer_audit_20261117/`：中文 report.md、20 题三条件 by_question.csv、
60 次完整输出 full_responses.md、逐次/逐声明审阅、103 条带理由和源日志哈希的关系映射，
以及原 B scorer 的辅助映射报告、独立唯一值近似诊断和来源清单。
这是 Codex 辅助核对，不是独立人工标注。无法确认的关系和错误定位的正文不强行映射，
没有改预测值、claim text、引用、B gold/scorer 或正式实验定义。

完整文本阅读分类：41 次明确说出所问核心答案，4 次说过答案信息又以混乱的不确定说明结束，
14 次缺少核心答案，1 次只列比较依据。11 道独立题在三条件都明确答出；这不是新增正式准确率。
系统自报仍为 42 complete / 18 incomplete。四道 NASA 题的 12 次回答均给出两个必要日期。
36 次含 Partial（immediate 4、short 15、long 17），19 次含事实输出使用回退措辞；未试听 WAV。

辅助映射后的 B 评分：57 ok / 3 error（0003、0044、0052 撤回不兼容）。
45/60 有数值 Unit EM/F1，子集均值 0.600 / 0.659259，不能当整体准确率。
已确认有依据完成 27/60，18 未完成、15 未知/不兼容；109 条可处理声明中 97 已评分，
85 满足支持、12 不满足（9 值格式/粒度匹配，3 引用支持），12 仍待复核，整体 UCR 仍 null。
唯一值诊断只覆盖 41/60，子集 EM/F1 0.658537、22 声明待复核；覆盖变化不能当性能改善。

实际问题包括：祖父题多查一代；Nobel 选择题受另一候选未知状态阻塞；Jamaican-born 被漏判；
Jake Zyrus/Charice 已有原始模型判断却遭身份校验拒绝；已有 Bay of Fundy 候选因省略号引文被拒；
职业否定与 B omission 口径不同；prior job 被误读或漏掉；7 个结构声明截取了错误关系的句子。
日期/城市附带国家的严格匹配、No 与 not 的正文对应、物种证据推属级关系也分别保留限制。
不修改实现，也未宣称通过润色或更大模型解决这些问题。

离线分析与复算均退出 0：60 次 B 分数/109 条声明在内存中重算与另存报告一致，
131 个原始文件哈希不变、20 行题目表与 60 行审阅记录齐全、14 个报告链接有效；源码哈希未变。
只对分析产物做校验，本次没有重跑功能测试、没有真实 API/搜索/音频合成、没有预留数据访问。
A2 独立复核、完整语义评分和整体 UCR 仍未完成。a-cascade 工作区无 commit/push，共享记录待用户同步。

### 修复独立级联的 Debug20 诊断问题（2026-11-18，用户要求）

本次只修独立 cascadesystem 与其 Debug20 适配，属于已授权开发修复；不推进正式运行或改研究定义。
在 2026-11-17 开始核对，跨日完成。旧 A 的 Qwen3-14B / Qwen3-4B LoRA、B 原评分器和 gold 均不修改。

落实内容：

- Tinker 拆题后新增一次只看原问题和候选计划的语义复核，检查祖先深度、必要比较结论、多余否定依赖、
  身份重复任务和擅加时间条件。review 返回计划仍严格验证图结构，失败不执行，也没有无限重试。
- 判断提示明确 X-born、候选选择与数值比较的不同依赖要求、此前角色、最短值、保留源日期格式，
  不把 species 级事实直接当 genus 级事实。普通模型仍不采用“没写职业就是否定”的新推断。
- 引用身份检查可接受有原文自述类型的冗余 album 等括号；人物角色限定还需本单元/祖先的角色上下文。
  地理/年份限定、不同显式类型和歧义页不放开；实时搜索自己的实体解析规则不改。
- 只在空白不同且源文本唯一匹配时恢复逐字原文，保留原始回复与变更日志。省略号/换词/大小写不自动补。
  修复请求附同快照原句；Tinker 的末尾复核允许一次引用契约修复，不能改支持值、引用ID、提升未知或新增冲突。
- 判定请求加入先前状态供措辞稳定参考，明确它不是证据；自然回退保留字面 Yes/No，并防 not-both 变成 neither。
- B 日志适配不再盲取第一个含值句。只有唯一且不共享其他声明值的句子才单独选择，
  否则保留原 utterance 作为未对齐上下文并标 span_basis；原子语音时间仍 null，不冒充语义/声学对齐。

离线回查此前诊断的 7 个错误句定位案例，新适配均保留完整原话，不改任何值/引用；
这只是旧输出的适配预览，不是新模型回答或准确率提升。原 131 个文件哈希未变。
虚构回归：系统新增 16 项、总 160 项通过；评估新增 4 项、总 28 项通过；退出均 0。
原已有测试文件哈希全部未改。覆盖只看问题的计划复核、坏计划拒绝、类型/同名边界、引文可见性和有限修复、
禁止引文修复更换事实、负向 both 语义、共享值/比较句上下文和未知语音时间。
三个 README 同步流程、预算、限制和文件表，55 个本地文档链接有效；git diff --check 退出 0。

源版本 a-cascade，父 `c23d6ae6e7250b793c026e7ec01ae9166728f5af` + dirty，
最终 43 文件集合 SHA256 `905240ebaa0ab0997fc1df72fd567bd2fa84aaa96f0d69689ae5f6365f5d41b9`。
清单与验证在忽略的 `cascadesystem/artifacts/changes/debug20-review-fixes-20261117/`：
`source-manifest-final.json`、`validation.json`、`adapter_preview.json`；保留早先中间源码清单。
Tinker 每题多一次计划 API 复核，末尾失败引文可能多一次修复；可能增加延迟，真实收益尚未确认。
没有真实模型/搜索 API、原生语音合成、GPU 作业、新依赖或预留数据访问。用户可新建 all 音频运行自行比较，不能 resume 旧源码结果。
旧真实分数、音频和辅助评分报告不重写。本次不宣称所有语义错误均已解决。无 commit/push，共享记录待用户同步。

### 最新一轮 Debug20 中文分析报告（2026-11-18，用户要求）

用户要求对最新 `20261118T052754Z-eebc4a69` 提供类似上一轮 report.md 的逐题分析。
本次仅做 A2 开发错误分析与离线评分，不修生产代码或启动新实验。产物在该运行 `answer_audit_20261118/`：
report.md、by_question.csv、full_responses.md、run/claim_audit.jsonl、comparison.jsonl、
99 条带理由与日志哈希的辅助映射、辅助 B 报告、独立近似值诊断、分析脚本及来源清单。

本轮 20 题 × 三条件，共 60 次；系统 45 complete / 11 incomplete / 4 error。
完整文本辅助阅读：45 次明确核心答案，3 次已说相关获奖信息却以错误区间问题的不确定说明结束，
8 次缺少核心答案，4 次流程错误；13 道题三条件均明确答出。这是 Codex 辅助阅读，不是独立人评或整体准确率。
上一轮明确核心答案 41，本轮新增 8 次、退步 4 次，另有原来末尾混乱的一次转成流程错误；改善和失败均保留。
Partial 25 次（immediate 4、short 6、long 15），回退事实输出 3 次、Correction 0；audio_summary 为 60 ok，未试听。

按关系映射 99/104 声明后调用 B 原 scorer：56 ok / 4 error，51/60 有数值 Unit EM/F1，
子集均值 0.823529 / 0.875817。必要值完整匹配 42；有依据完整 40、未满足 11、未知/错误 9。
88 条声明满足支持、11 不满足（8 值口径、3 引用），5 条仍待复核，整体 UCR 保持 null。
未映射的 3 个获奖年份、2 个制片人事实与 gold 的关系不同，不硬对齐。
唯一值近似诊断覆盖 42/60，子集 EM/F1 0.857143、16 声明待复核；不同覆盖不能作准确率高低结论。

新增失败明确定位到 plan_review：0004/0016/0017 的比较查询引用 u1/u3，而直接依赖只有 u2/u4；
0012 含自引用 subject。初始 decompose 的显式依赖补全未复用于 review，四次均在严格验证时报错。
0011 仍有无具体事实的身份单元，阻塞祖父链；Nobel 三次仍误读为获奖时间区间，question-only 查询还预填 1979。
出生地 immediate 仍漏已到达 Jamaican-born，prior job 三次仍漏 former Speaker，职业否定 omission 口径仍不同。
属/种证据与 long Charice 的 mononym 引用仍不充分。报告记录后续建议，本次未借分析继续改代码。

实际运行源码 SHA256 `d44911a9bf1fa85c309045e541877ecbff0d942f5246f8d728f94b5a9c4e93f0`，
父 c23d6ae6e7250b793c026e7ec01ae9166728f5af + dirty，不能替换为分析时工作区 905240eb...。
B 固定 ea390574eadd301354d5de46f0d28d328cca5bad / debug-v0，输入哈希与上一轮一致。
本轮原日志 SHA256 `b5dfdf32f8a01a6821adea1160f1b9e23a1cca9638f4d21a9d45ccd7961c9fea`。
60 次 plan_review 单次调用耗时中位数 1.958 秒；60 次全运行文字流水线中位数 11.692 秒，含音频排空总墙钟 13.096 秒。
这些不是正式声学时间指标或与 Wait-All 的配对收益，不能用两轮各自总体中位数证明变快。

离线分析与 B 分数/104 条声明重算一致，退出 0；20 行题表、60 条审阅和 16 个报告链接核验通过。
本轮 133 个原始文件、上一轮 131 个原始文件与运行代码均未变。只验证分析产物，没有重跑功能测试。
无真实模型/搜索/语音调用、新依赖、GPU 作业、预留集访问或 commit/push；a-cascade，共享记录待用户提交同步。

### GPT-OSS-120B 判断器 LoRA 与运行入口（2026-11-18，用户要求）

状态：实现与离线验证完成；真实远程训练、checkpoint 调用和效果比较尚未运行，交用户自行执行。
用户要求为当前 120B 准备训练及训练后运行指令。本次授权仅用于独立 cascadesystem 原型，
不改变旧 A Qwen 方法、B gold/scorer、职业 omission 规则或正式实验定义。

新增 `cascadesystem/training/`：固定 SFT 导出/适配、官方 Harmony renderer、Tinker LoRA 训练、
验证损失选择 checkpoint、恢复权重和优化器、SFT dev 原始/校验后判断对比，以及应用/Debug20 包装。
SDK 固定 0.39.1；cookbook 固定 28de41edfcdd07ba3e7980f35d53a586024a2184；使用 WSL Ubuntu/Linux 独立 Python 3.12 环境。
官方必装 tml-renderers 仅支持 Linux/macOS，原生 Windows train/evaluate 提前报明确错误；
prepare/inspect/run 及现有 Windows 语音不受影响。README 提供 WSL 安装及跨系统 checkpoint 使用步骤。
依赖仅列入可选安装指令，本次没有安装或下载 tokenizer/权重。实际 GPU 由 Tinker 管理，不能冒充正式 H100 实验。

只从固定 B commit ea390574eadd301354d5de46f0d28d328cca5bad 提取五个明确 SFT train/dev 源路径，
不检出 B 工作树、不读取预留集。原 243/57 题、1991/486 快照，经当前契约兼容过滤保留
train 235 题/1900 快照、dev 54 题/463 快照，尚未做真实 tokenizer 长度筛选。
训练排除 57 条依赖契约不兼容、34 条 omission；验证分别排除 6 和 17 条。
保持 B 标签，补当前可见原句引用，排除不兼容数据而非重写 gold；按问题 ID 和规范化问题文本隔离 train/dev。
输入只含当前快照可见证据，监督目标另存；有部分证据可支持对应单元，其余保持 UNRESOLVED。
没有 CONTRADICTED 目标、无专门 single-answer/multipart 覆盖；标注单元与当前拆题存在分布差异。
完整原句引用未作独立语义复核，因此这些数量和低 dev loss 均不是准确率提升证明。

运行时仅 judge/judge_repair 使用 `CASCADE_JUDGE_MODEL`，其余阶段沿用当前基础模型。
包装器校验 best.json 的基础模型/提示哈希，不写 .env；调用记录和 B 公开设置保留实际模型/判断推理强度。
训练日志、失败尝试、逐轮 state/sampler 路径、源码/数据/SDK 版本均保留；显式 resume 重复未完成的一轮。
dev 报告区分原始错误支持与引用/依赖过滤后的支持，避免把拦截成功当成模型判断正确；不宣称 B UCR。
计划复核复用已有安全依赖补全，仅增加已知占位符明确引用并重新严格校验，不增加 API 次数。
自引用、循环、未知单元及其他坏计划继续拒绝，不能声称此前四个错误全部解决。

虚构离线测试：系统 183 项（新增 23 项）、Debug20 28 项，退出均 0；原 15 个测试文件哈希未改。
五个子命令 help、prepared inspect、76 个文档链接、git diff --check 通过。
最新历史运行的 133 个原文件哈希均保持不变。没有模型/搜索/语音 API、新 GPU 作业或 commit/push。
分支 a-cascade，父 c23d6ae6e7250b793c026e7ec01ae9166728f5af + dirty；
本次 50 个源码文件集合 SHA256 001c43705c0b2f7c5bce577f108808d30726b84ed00e8eb1a67e223f68ee398e。
验证日志、源码清单在忽略的 `cascadesystem/artifacts/changes/gpt120-judge-lora-20261118/`；
原始/转换数据在忽略的 `cascadesystem/artifacts/training/data/`。四份英文 README 同步入口、文件表与限制。
后续由用户依次安装可选环境、smoke、完整训练、同份 dev 基础/LoRA 对比，再新建 Debug20 运行；共享记录待提交同步。

### WSL ensurepip 环境创建失败排查（2026-11-18，用户反馈）

用户在 /mnt/d 项目路径创建训练 venv 时，ensurepip 返回非零。部分 pyvenv.cfg 确认为 /usr/bin/python3.12、
3.12.3；当前只有包装异常，尚无 ensurepip 的底层错误，不能断定是缺包、权限或跨文件系统问题。
更新训练 README：Ubuntu 24.04 使用对应 python3.12-venv/python3-pip-whl，环境建在 WSL 主目录
~/.venvs/moshi-cascade-312，并提供直接运行 ensurepip 显示原始错误的命令。全部训练/验证命令同步路径，
代码、数据和 checkpoint 元数据仍使用原项目。失败环境不删除，不改变运行逻辑或实验规则。
仅核验文档/命令路径一致性与 diff；没有执行 apt/pip、创建 WSL 环境、调用模型或训练。
实际修复结果等待用户运行。a-cascade，父 c23d6ae6e7250b793c026e7ec01ae9166728f5af + dirty；无 commit/push。

### 修复 Tinker checkpoint 冒号运行 ID（2026-11-18，用户真实 smoke 反馈）

用户执行 smoke-v1：16 个训练快照、4 个 dev 快照、batch8、1epoch，完成 2 个优化 step；
日志 loss 分别为 3.3188521543636873、0.931456977041106。Tinker 0.39.1 / cookbook 0.7.0。
08:43:30Z 启动，08:44:25Z 记录 ValueError；这不是训练完成或准确率结果。
训练目录 `cascadesystem/artifacts/training/runs/smoke-v1/`，config 记录 app 源码身份
69730031992512ce7307e43cc4c1c734a2bae60a9d3e07c08777389e3d867118，不能替换为本次修复源码。
Tinker 管理远端 GPU，型号/作业号本地未提供，不作正式硬件或延迟结果。

根因已确认：实际 sampler 路径为 tinker://<uuid>:train:0/sampler_weights/epoch-0000 等；
本地 check_checkpoint 正则遗漏冒号，epoch1 保存返回后的校验拒绝了有效格式，best.json 尚未写出，
resume 仍标 completed_epoch=0。修复接受带冒号的运行 ID，同时拒绝非 sampler 类型、查询串和额外路径。
保存后先在 events 记录返回的 checkpoint/state，便于后续失败诊断。未修改旧 smoke 元数据或假造 best。
由于源码改变，严格 resume 不跨版本放行；README 提供新目录 smoke-v2，再执行完整训练的步骤。

系统 187 项、Debug20 28 项离线测试通过，退出均 0；新增 4 项虚构回归，已有测试未改。
覆盖新路径、坏路径、保存/最优轮选择/包装器和 HTTP model 字符串完整传递。78 个文档链接及 diff 检查通过。
本次 51 源文件集合 SHA256 26cfaa6b6d0b778909dd71449e8e4f6a63b1c44966bd9e2cc934558bc2ffbf7a，
a-cascade、父 c23d6ae6e7250b793c026e7ec01ae9166728f5af + dirty；验证记录及源码清单在
忽略的 `cascadesystem/artifacts/changes/checkpoint-path-fix-20261118/`。
助手没有调用真实训练/预测 API，没有改动历史结果、数据、提示或 B 评分；修复后远程 smoke 等用户自行运行。
用户同时问 step 数：每轮 ceil(长度过滤后训练快照数/batch)，smoke 为 2；完整 1900/batch8 上限 238，
三轮上限 714 个优化 step；dev forward 不计入该 step 数。无 commit/push，共享记录待用户提交同步。

### 原始 GPT-OSS-120B SFT dev baseline 分析（2026-11-18，用户运行结果）

只读核对 `cascadesystem/artifacts/training/dev-base-v1/`，checkpoint=null，确认是原模型加 JUDGE 提示，非 LoRA。
463 快照、54 个独立问题、1283 个单元；程序处理状态均 ok。参考 SUPPORTED734、UNRESOLVED549，无冲突目标。
原始标签正确 1200/1283=93.5308%；严格校验后 1139/1283=88.7763%。
原始错放支持 54/549=9.8361%，校验后 47/549=8.5610%；漏判由 29 增至 97/734=13.2153%。
双方 SUPPORTED 的637单元中值精确匹配567，即89.0110%；其余70次不匹配包括简称/全称等取值口径差异，
不能未经语义复核全当事实错误。参考可答单元中，标签和值同时吻合567/734=77.2480%，不称整题准确率。

75 个原始 SUPPORTED 被降为 UNRESOLVED：参考可答68（58引用/值契约，10依赖）、参考未知7（5契约，2依赖）。
68 个参考可答降级中，62 个原始值与参考精确吻合；因此下降不等于模型语义能力下降。
无效引文67处，其中57处含省略号拼接；仅空白规范化无法恢复这些单元。没有放宽校验或重写预测。
当前 evaluate 是单次判断加本地校验，没有运行在线 protocol 的一次引用修复，因此不能直接当完整系统效果。
LoRA 后续需在同份 dev 和同样评估方式比较，重点检查引文契约、错放支持与漏判，不能只看训练 loss。

原记录 app 源身份 1f653f8990aee7572316a96934daa3fbfa00eb471d277053cd6d6a20cc0d0e92，
父 c23d6ae6e7250b793c026e7ec01ae9166728f5af + dirty；B ea390574eadd301354d5de46f0d28d328cca5bad，
dev SHA256 2848720a8b86e461d0489af7571a20bedc3b51fe24b0a4b5374b22a90f1de615。
Tinker 远端 GPU 型号/作业号未提供；仅开发用 SFT 快照诊断，不是正式 H100 或 B UCR 结果。
离线逐条验证样本身份、数据哈希和原始/校验标签矩阵通过，退出0。未重跑模型或功能测试，无预留数据、训练或预测修改。
本次仅更新分析记录，a-cascade，无 commit/push；已有运行文件全部保留，共享记录待用户提交同步。

### LoRA Debug20 中文 report.md（2026-11-18，用户要求）

用户已完成 `20261118T175701Z-e9e7665c`：20题×immediate/short/long共60次，Windows TTS、未播放。
本次只离线分析，在该运行 `answer_audit_20261118/` 新建 report.md、60次完整原话、20行逐题CSV、
运行/声明审阅、110条辅助关系映射、B辅助评分/近似诊断、对比和诊断摘录、分析与验证脚本及哈希清单。
这些阅读与映射是Codex辅助核对，不是独立人评；不修改模型、提示词、训练数据、B gold/scorer或原运行。

实际运行源集合SHA256 26cfaa6b6d0b778909dd71449e8e4f6a63b1c44966bd9e2cc934558bc2ffbf7a，
父c23d6ae6e7250b793c026e7ec01ae9166728f5af + dirty；B固定ea390574eadd301354d5de46f0d28d328cca5bad/debug-v0。
只有判断阶段使用f9e9a6c1-e203-5c2c-acdd-68fe67378ca4:train:0的epoch-0001 LoRA，其余API阶段是原GPT-OSS-120B。
Tinker远端GPU型号/作业号未提供，不能作为正式H100结果。报告记录Chicago 11:57:01启动，对应UTC17:57:01。

系统48 complete /11 incomplete /1 error；辅助阅读48明确核心答案、3已说信息后仍混乱、8缺失/部分、1流程错误。
15道题三条件均明确答出。上一轮明确45，新增恢复5次、退步2次；结构错误减少，但不是单变量LoRA消融。
本轮30次发生Partial，合计31次输出；事实回退8次，Correction0，60个非空WAV有效但未试听。

原日志118声明、110条关系映射；B排除错误运行中的1条，因此有效117，109条已评分、8条待复核。
B辅助评分59ok/1error，51/60有数值Unit EM/F1，子集均值0.862745/0.872549；必要值完整44、未完整7、未知9。
完整且有依据39、不满足12、未知9；声明94支持、15不支持（10严格值口径、5引用/支持），整体UCR保持null。
上一轮完整有依据40，本轮39，不能因核心覆盖48/60就宣称整体准确率上升。
共同可评分47次的Unit EM为0.872340→0.893617，仅作开发子集描述。两轮源码、计划不同，不推定LoRA因果收益。

关键失败：0016–0018中LoRA把较晚去世电影选反，基础模型核验正确拦截，复核仍给相同错误值。
0046/0047把Jon误判电视编剧，批量拒绝又连带丢William正确事实；0048一次judge JSON解析失败终止。
Nobel三次仍错拆时间区间；0055的genus/plant身份限定造成拒绝，0057仍用物种支持属；short/long Charice引用不充分。
可解析judge/semantic-review的221处引文均连续匹配原文，说明格式改善不等于关系或比较推理正确。

B辅助评分原样重算一致、20行题表、60次运行、148个本地链接、60个WAV及模型路由检查通过，退出0。
本轮/上一轮及debug输入共1935个原文件哈希未变；原默认评分报告保持。未重跑功能测试，未调用真实模型、TTS或搜索。
仅新增报告与文档记录，无预留数据、新训练、commit/push。a-cascade，共享记录待用户提交同步。

### 导入用户提供的Qwen3-4B LoRA文件（2026-11-18，用户要求）

用户指定qwen3_4b_lora_judge.zip，已将其中两个文件原样导入
`cascadesystem/artifacts/models/qwen3_4b_lora_judge/`，没有读取或执行归档内的指令/代码。
归档SHA256为354f35c1dd8b671f08fd9623f82838719471f5549ec598681b90c7e633bc09ef，源文件保持不变。
adapter_config明确base_model_name_or_path=Qwen/Qwen3-4B，r16/alpha32，q/k/v/o投影；revision=null。
权重47,224,624字节，288个F32张量、36层、11,796,480个adapter参数；不含基础权重或tokenizer。
必须配对应的Qwen3-4B使用，14B不能替代。已提供使用现有Windows hf工具下载基础模型的命令，未实际下载。

验证：2文件CRC与SHA256一致、配置/rank和全部张量header、形状、数据偏移/大小通过，导入命令退出0。
配置与权重SHA256分别为6fe309e8d97a5da0ec2ffd40e29607d20bd814d894b3d418cedd290b5049b07d、
eb19af3a446e85f1793bf6789bca709cdb0128a300f9dc018e56905dd4e550e9。文件均在Git忽略目录。
import_manifest.json及局部README记录来源、检查范围与后续加载要求；检查脚本/记录在
`cascadesystem/artifacts/changes/import-qwen4b-lora-20261118/`。
只完成文件导入，未加载模型、注册服务、改变当前GPT判断器或旧A方法，未安装依赖、运行GPU或访问预留集。
归档未提供训练来源/提示/输出schema，不能宣称它必定对应旧A已报告成绩，或直接兼容当前judgments/原文引用契约。
仅文件与文档变动，不重跑功能测试；a-cascade，父c23d6ae6e7250b793c026e7ec01ae9166728f5af + dirty。
无commit/push，共享记录待用户提交同步。

### 独立Qwen Debug20后端（2026-11-18，用户要求，已完成代码与离线验证）

用户要求新建`eval debug20 qwen/`，只替换模型，其余沿用现有独立cascadesystem流程。
用户已明确选择本机RTX 5080 16GB上的4-bit量化；本次落实这一实现步骤，不推进正式实验。
新增独立CLI、NF4运行时、模型文件检查、依赖/安装脚本、英文说明及虚构离线测试。
14B负责拆题、计划复核、生成、核验与反馈；4B加导入LoRA负责judge/judge_repair及其末尾复核。
使用NF4双重量化、BF16计算、greedy、关闭thinking、两个模型共享单GPU队列；加载位于题目计时之前。
保留原prompt、控制器、可见证据边界、引用/依赖检查、有限修复、B日志/评分与Windows TTS。
旧输出只兼容units根字段改名judgments，不补造原文、不改标签/值/引用，不启用omission例外。
新代码/共享源码hash、依赖版本、量化配置及模型身份写入单独manifest，并进入resume身份检查。
大基础权重只检查分片header/大小/mtime，非全文件内容校验；adapter完整SHA保持导入版本。

本地14B八分片、4B三分片的索引与张量范围、LoRA288张量形状/完整SHA检查通过，inspect退出0。
24项新虚构测试、187项原系统测试、28项原评估测试通过，退出码均0；旧测试未改。
新测试覆盖模型路由、原提示/输入保留、旧schema不放宽校验、并发取消、NF4/mock加载与生成、
上下文超限不截断、无gold预测、真实旧回放的partial/final、resume拒绝变更、CLI产物与评分委托。
仅mock使用加载/评分接口，未加载真实模型、安装包、调用API/TTS、跑B题目或训练；没有新准确率。
实际NF4显存/性能及该LoRA对当前prompt的适配仍须用户首题试跑；16GB并不保证所有上下文都够用。
安装指令用现有uv创建新的Python3.12环境，避开当前Python3.14和已失效的旧语音venv。
验证版本为a-cascade，父c23d6ae6e7250b793c026e7ec01ae9166728f5af加dirty。
原cascadesystem与旧eval debug20的.py/.ps1保持，原51文件集合SHA256仍为
26cfaa6b6d0b778909dd71449e8e4f6a63b1c44966bd9e2cc934558bc2ffbf7a；新目录另存源码身份。
新目录源码SHA256为1bce5699e204d4750a33344b8ae680774ef286d01dae2a8473046adbe73d8711；
离线验证记录在`eval debug20 qwen/artifacts/validation/20261118/manifest.json`及同目录日志/资产元数据。
没有访问预留数据、改B gold/scorer或旧A方法，无commit/push；共享文档待用户提交同步。

### 用户本机Qwen首轮失败诊断（2026-11-18，只读运行分析）

用户执行`eval debug20 qwen/artifacts/runs/20261118T191326Z-b1f076d9/`后取消；本次只检查其已保存0001—0004。
0001/0002/0003均为error，实际failure均为`Local Qwen judge timed out after 45s (including GPU queue)`；
judge调用实际墙钟87.984/84.438/63.609秒，最终错误输出在114.078/99.953/79.109秒。
三次均已收到22句、2057字符证据；14B拆题和计划复核成功，4B+LoRA未返回已完成的判断JSON。
运行时超时后会等待生成线程响应停止请求，因此45秒是触发取消的期限，非严格返回上限。
反馈生成均在6秒边界取消，所播放的opening/progress是现有安全回退，不是已成功生成的模型反馈。
0004为用户取消，非已完成答案评分。生成采样参数警告后拆题仍成功，该警告不是前三条失败异常。
加载后torch已分配11.801GiB，但无判断阶段峰值/部分token日志，不能据此认定OOM、CPU换页或输出循环。
另见14B将目标祖父拆为父亲再找父亲的祖父，计划复核仍保留此关系错误；它不同于当前运行终止原因。
后续先补判断阶段耗时/部分输出诊断并单题复测，再决定超时/资源调整；本次没有实现或试跑修改。
数据B debug-v0/ea390574eadd301354d5de46f0d28d328cca5bad；用户GPU RTX5080、torch2.8.0+cu128、NF4。
实际运行源码1bce5699e204d4750a33344b8ae680774ef286d01dae2a8473046adbe73d8711，父c23d6ae+dirty/a-cascade。
本次仅增加此诊断记录，原运行保留，无新模型/TTS/API调用或功能代码修改，故未重跑功能测试；无预留数据/commit/push。

### GPT+LoRA修订900条独立入口（2026-11-18，用户要求提供运行指令）

用户要求将当前GPT+LoRA用于截图同规模的数据。本次只落实运行准备，不将询问指令解释为助手读取预留题的授权。
从origin/a-main-experiments的README/main_experiments.py元数据确认：指定集为300题×三档900trace，
固定B来源ea390574eadd301354d5de46f0d28d328cca5bad，使用eval_revised_v1 trace及batch01_05_v1/batch06_10_v1两份修订gold。
没有打开这些题目/gold/trace或其内容派生输出；没有切换分支、checkout完整B树、训练或调用真实模型。

新建`eval gpt900/`，独立CLI支持prepare/run/score；三步均在任何数据/凭据/检查点访问前要求显式--final-run。
保留当前GPT120B planner/generator/verifier及训练judge checkpoint选择，复用原Cascade、单trace回放、B scorer和TTS。
输入严格区分public/private，预测不读gold；原gold与修订gold不能混用，导出后记录固定来源和全部输入hash。
准备入口检查300/900/817及三档/内容一致性；仅运行当前GPT+LoRA策略，不冒充A十配置矩阵或Oracle上限。
原A builder保留空证据句，原独立scheduler拒绝空句；新入口保留原始输入/评分文件，运行时仅跳过空句，
非空句ID/内容/时刻及原检索结束时刻不变，另记跳过数量。没有修改普通系统的证据支持规则。
评分默认严格映射，显式--allow-value-match只启用B现有近似值诊断，与A main collector参数一致但不当独立人评。
评分清单包含900预期项，不隐藏缺失/失败；resume对源码、模型、输入和设置校验，不重试已保存失败。
延迟仍为unknown，无真实语音声明对齐；不宣称复现A模拟时钟或H100延迟。

18项新虚构测试通过（其中900条虚构执行/恢复清单验证），187项原系统与28项原Debug20测试通过，退出均0。
仅mock运行准备/模型与新评分器委托测试；旧28测试使用冻结B标准库评分器和虚构数据。旧测试未改。
新增入口--help通过，不带--final-run拒绝；实际900内容/配套API可用性未验证，真实导出与模型评测由用户最终确认后执行。
原51个共享.py/.ps1不变，新目录另记源hash，README/训练指南补入口，旧运行全部保留。
完整源集合SHA256为9c2435691a6633d61ce619ece3157f2ffd922c8f0282b5f3faac82728fe08c73；
验证记录在`eval gpt900/artifacts/validation/20261118/manifest.json`，未带确认参数的子进程实际退出2。
a-cascade，父c23d6ae6e7250b793c026e7ec01ae9166728f5af+dirty；无commit/push，共享文档待用户同步。

### 修复900条运行被音频失败中断及恢复阻塞（2026-11-18）

用户报告gpt120-lora-v1在312/900停止，原B运行状态301 ok/11 error/588 missing。
只核查已生成0309—0312的运行/音频错误元数据，没有读取问题、证据、答案用于调整模型。
0312文本complete、模型调用成功，但audio.status=error：Speech command exited with code 1，合并语音又报Some speech segments were not synthesized。
不是API认证中断；0311另有独立的judge JSON解析失败。原停止消息混合音频/认证原因，且--resume会再次被旧音频失败阻塞。
本次只修运行恢复，不改模型、prompt、证据规则、时序或评分，不用预留回答调参。

新增--continue-on-audio-error，语音错误原样记账、可继续文字评估；新的认证/权限失败仍停止，打印具体原因。
恢复不再因已保存的失败反复停住；不重试或隐去这些失败。
新增显式--continue-from到独立新目录：校验同输入/模型/设置与不变的共享方法源码，复制全部已保存样本，
原目录不写入，父/子源码身份及继承run.json哈希写continuation.json和父manifest副本。
旧源码冻结检查不取消；父子路径重叠、已有子目录、方法/模型变化或未保存的父样本均拒绝。
未代用户执行复制或续跑，未增加任何真实API/TTS调用；Windows语音进程退出1的更底层原因当前日志未保留。
30项900入口测试通过、退出0，原18项测试未改，新增12项虚构回归覆盖保存失败后继续、认证仍停、复制不改原记录和拒绝方法变化。
共享51个.py/.ps1仍与26cfaa6b6d0b778909dd71449e8e4f6a63b1c44966bd9e2cc934558bc2ffbf7a一致。
新源码SHA256为b652f87e3116f16619d16ba6fecc74acd36cf191b6e85e100f6a178739568af9；验证记录在
`eval gpt900/artifacts/validation/audio-continuation-20261118/manifest.json`。当前配置/判断checkpoint与父运行元数据逐项一致。
a-cascade，父c23d6ae6e7250b793c026e7ec01ae9166728f5af+dirty；原运行与评分保留，无训练/commit/push。

### 最终运行前344条进度快照（2026-11-18，用户要求只读分析）

用户询问已完成344条表现，读取时续跑已保存345条。本次固定续跑gpt120-lora-v1-continued的0001—0344，
单独复制评分日志/身份到`eval gpt900/artifacts/analysis/progress-0344-20261118T220326Z/`，不改正在运行的目录。
覆盖115题：immediate115/short115/long114；旧312继承部分只计一次。模型/规则保持冻结，不据此调参。
系统271 complete/61 incomplete/12 error；音频343 ok/1 error，旧312音频失败保留。
错误为7次JSON解析、3次查询列表格式、2次占位符依赖契约；不将这些都算事实答案错误。
使用原B scorer与既有allow_value_match=True离线评分，900预期项中332 ok/12 error/556 missing。
就前344条：有据完整暂计168/344=48.84%，已知不满足51，未知125；必要答案值覆盖完整183。
219条有Unit EM/F1，子集均值0.835616；不是344条整题准确率，也不与截图全900条件直接排名。
774条纳入声明汇总，603已评/171待复核，47未获支持；已评分子集7.794%，整体UCR仍null。
complete271中B暂计有据完整168、不满足19、未知84，系统完成率78.78%不能当准确率。
计数/分母/900预期清单校验与离线评分退出0，344对run与policylog共688原文件哈希快照后未变。
报告report.md、progress.json、diagnostic_counts.json、validation.json及独立B报告保存在上述分析目录。
仅进度分析，无新模型/API/TTS/训练/搜索调用，无功能源码修改，未重跑功能测试。
沿用b652f87e3116f16619d16ba6fecc74acd36cf191b6e85e100f6a178739568af9，B固定ea390574eadd301354d5de46f0d28d328cca5bad。
Tinker远端GPU/作业号未提供，不声称H100正式时延。a-cascade/c23d6ae+dirty，无commit/push。

同一344条快照的完成状态解释补充：51个grounded_complete=False中36个必要答案值未完整覆盖，
15个答案值覆盖但支持/引用契约不满足（19条相关不支持声明均为missing_gold_support_or_citation）。
125个未知中12个为运行error，113个有待映射声明；对应171声明为155映射待定/14多义值/2正文无声明值。
B在有任何pending声明时冻结整条run完成指标；未知既可能含正确答案，也可能含未映射错误，不能当正确。
grounded_complete只检查必要单元均有SUPPORTED声明，不等于所有附带话语零无依据；UCR另计。
补充解释写同分析目录completion_explanation.md；仅核对冻结B源码和快照元数据，无模型/提示/代码/评分修改。

### GPT＋LoRA全部900次report.md（2026-11-18，用户要求）

确认gpt120-lora-v1-continued已保存900条、300题三档各300，未缺失；原312条继承只计一次。
生成该运行根目录`report.md`及`analysis_final900_20261119T000603Z/`的900行汇总CSV、聚合JSON、独立B复算及hash清单。
目录时间戳是UTC，报告记录对应Chicago 2026-11-18的最终运行分析。
系统695 complete/168 incomplete/37 error；音频899 ok/1 error，未掩盖第312条失败。
B为863 ok/37 error，无missing；有据完整暂计394/900=43.78%，不满足135，未知371。
必要答案值覆盖完整418；529条可评分记录的Unit EM/F1=79.0170%，覆盖58.78%，不称全体准确率。
1831声明中1322已评/509待评，106不满足B支持/引用条件；子集8.0182%，整体UCR仍null。
371未知为334映射待评与37流程error；135不满足中111必要答案未完整覆盖，24值匹配但证据契约不足。
近似值映射只接受唯一匹配候选，存在选择偏差；报告未对未知补分，不冒充独立语义复核。
三档有据完整138/136/120；按独立题三档全成功97题，0档成功130题（含未知/错误，非130题全错）。
报告附37流程错误索引、三档/数据来源/题型分组、系统与B交叉表、API阶段耗时和完整数据/源码身份。
运行有301条出现Partial；文本流程中位11.711秒，不作为B语音TTFR/TTFGI/TTCA，后者仍unknown。

复算原B运行评分、声明评分、待复核队列逐条一致，退出0；900清单/300题/路由校验、312继承run哈希一致。
899份WAV非空头部可读（未试听）；45个报告链接有效。8507份原预测/事件/文本/索引/评分文件hash检查未变，未对全部WAV做完整二进制hash。
report SHA256为2f9f7abfe520f1a52a6387851d6991dd625591355713d56c8b3cf727cd9c908e。
生成脚本在`eval gpt900/artifacts/reporting/final900_report.py`，仅派生分析，未改任何功能代码、模型、prompt、B gold/scorer或原运行。
未调用真实LLM/API/TTS、搜索或训练，未据预留结果选模型/调参；无功能代码变化，未重跑功能测试。
实际源码b652f87e3116f16619d16ba6fecc74acd36cf191b6e85e100f6a178739568af9（前312来自9c243569...），共享51代码身份保持26cfaa6b...。
B固定ea390574eadd301354d5de46f0d28d328cca5bad；TinkerGPU/作业号未提供，非H100延迟声明。
a-cascade/c23d6ae+dirty；无commit/push，共享文档待用户提交同步，生成报告与数据均在忽略目录。

### 删除独立系统中的可选Qwen内容（2026-11-18，用户明确要求）

用户要求删除cascadesystem中的Qwen内容及整个eval debug20 qwen目录；本次只做这项清理。
删除前逐一核验绝对路径均位于D:/UIUC/CS546/moshi-rag内，根和内部无重解析目录/符号链接，未跨shell组合删除。
已删除eval debug20 qwen整目录（源码、专用测试、.venv、运行/验证产物），以及
cascadesystem/artifacts/models/qwen3_4b_lora_judge和artifacts/changes/import-qwen4b-lora-20261118。
该特性专用测试随用户要求的特性删除，不是为让测试通过而删除；其余现有测试未改。
清理根README、cascadesystem README/file map、Debug20及900指南、A README里本可选后端的当前链接。
本文件及judge_notes较早的Qwen导入/实现/失败诊断段落仅为历史记录，其中已删除路径不再作为使用入口。

GPT应用与训练/Debug20/900入口及.env保留，默认仍openai/gpt-oss-120b，训练judge checkpoint元数据校验通过。
原51共享.py/.ps1身份仍为26cfaa6b6d0b778909dd71449e8e4f6a63b1c44966bd9e2cc934558bc2ffbf7a。
8507个GPT原结果相关文件hash及900次report.md的2f9f7abfe520f1a52a6387851d6991dd625591355713d56c8b3cf727cd9c908e均未变。
187项系统测试、28项Debug20测试、30项900测试通过，共245项，退出码均0，无真实API/TTS/模型/训练调用。
cascadesystem中无Qwen命名残留及当前说明引用；旧A方法、外层D:/UIUC/CS546/models里的Qwen3-14B/4B基础权重均未删除。
验证记录在eval gpt900/artifacts/maintenance/cleanup-local-backend-20261118/manifest.json。
a-cascade，父c23d6ae6e7250b793c026e7ec01ae9166728f5af+dirty；未读取预留题调参，无commit/push，共享记录待用户同步。

### 提交当前代码到GitHub分支，不merge（2026-11-18，用户明确授权）

用户明确要求上传GitHub但不merge，本次授权覆盖当前已完成改动的本地commit和分支push。
上传目标为origin/a-cascade（zxx3312/moshi-rag），远端fetch确认提交基点与本地一致，为c23d6ae。
提交范围为独立GPT系统、语音/打断、训练模块、Debug20与900入口及指南/开发记录；可选本地Qwen目录已按要求删除。
上传前检查70个候选代码/文档文件，无真实凭据、数据集、模型、音频或artifacts；仅.env.example模板进入版本控制。
187系统+28 Debug20+30最终入口共245项测试已通过、退出0，功能代码此后未改。
不创建PR、不执行merge、不推main、不强制覆盖分支；本次发布commit与远端状态以Git提交/推送记录为准。
本地.env、训练checkpoint记录、数据、运行结果和report.md均留在忽略目录，不随代码上传。

### 补传两个eval的运行产物（2026-11-18，用户明确授权）

用户确认此前代码提交未包含runs后，明确要求上传两个eval的运行内容；本次授权包括运行结果、报告、文字与音频的commit及push。
范围仅为eval debug20/artifacts/runs和eval gpt900/artifacts/runs，共5个运行目录；排除Python字节码缓存。
22596个运行文件，共2820868710字节；暂存区逐文件Git blob与原始文件一致，SHA256清单核对通过，退出0。
调整两个eval的忽略规则，继续忽略inputs、evaluator缓存和其他artifact目录；.gitattributes对runs禁用换行转换，保留原始字节。
发布前保存逐文件大小、SHA256及Git blob身份，仅做传输完整性核对，不查看评测题目、答案或证据，不改模型、提示词或评分结果。
本次不执行推理、训练或评分；无功能代码变化，以文件清单和blob核对验证上传完整性，不重复运行功能测试。
目标仍为origin/a-cascade，父提交d337547065bb71bd4bf439c919e62d8499dbb193；不merge、不推main。
上传完成状态及提交号以本次Git记录为准；共享文档尚未同步到main。
