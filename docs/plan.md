# 剩余工作计划

本文列出到论文初稿的工作、依赖、完成标准和运行记录。实验定义见 `experiment_spec.md`。
D 编号对应 spec 第 11 节。一次只做一步；只做部分就标“进行中”。

截止日期：待用户填写学期结束日期、目标会议截稿日期。
最后核对：2026-11-16。当前任务是 **F1 的主实验运行准备**，尚未启动最终模型运行。
下方历史状态表保留当时记录；本分支的当前进展见文末“900 条修订 trace 的主实验准备”。
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

## 900 条修订 trace 的主实验准备（2026-11-16）

用户指定 `b_work/test_set/traces/eval_revised_v1/traces.jsonl`，要求检查用途、起草主实验代码、
使用账号优先级并隔离分支。已在原目录创建 `a-main-experiments`，父 commit 为
`bc412d5911d79c7bb39a615b41cb8d2597738291`（`origin/a-method-integration`）。
`a-eval-refinement` 保持独立；没有合并评分规则讨论、commit/push 或新建工作树。
授权覆盖指定数据的结构检查、匹配 gold 接口核对和运行准备；没有用预留内容训练、
改提示词、选参数或选模型。F1 只完成运行准备，最终模型运行未开始。

### 数据核对

固定 B commit：`ea390574eadd301354d5de46f0d28d328cca5bad`。
trace SHA256：`34da9ee54e0d494f1c6701d7332febf0088f22d925c4f6543b48a3af58ae30ac`。
必须配对以下修订 gold，不能用原 `batches/` gold：

| 输入 | 题数 | SHA256 |
|---|---|---|
| `b_work/test_set/revisions/batch01_05_v1/gold.jsonl` | 150 | `c6936dd4068bb52a949285bb92465c3b95f9d086b54bacd8a37f31be89a74a72` |
| `b_work/test_set/revisions/batch06_10_v1/gold.jsonl` | 150 | `742970f46b9b753ca7ec0a28c6ef52061ce2a924ef9a9dd71756939985e82108` |

实际核对：300 题、900 条 trace、817 个 gold 单元、30,384 个证据事件。
HotpotQA / 2Wiki 各 150 题；三档各 300 条，分别为 0 秒、1/3 秒、2/8 秒。
修订后的单元题型为 bridge 129、comparison 116、bridge_comparison 35、single 20；没有 multipart。
`source_type` 保留原数据集分类，与单元题型不同。数据用于控制检索到达时间的策略比较，
不是 900 道独立问题，也不是实测检索时间。

同题三档的问题和完整证据一致，文档同时到达，没有 gold 字段混入公开 trace；
trace/gold ID 与版本对应。每条 11–73 个事件；原文空白句对应 3 个空事件，原样保留并计数。
与 debug 20 题、SFT 300 题的 sample ID 交集均为 0，仅证明 ID 不重叠。
omission 标志 3 个，presupposition 标志 13 个，其中 11 个有 presupposition_sets；
同单元双标志为 0，不排除依赖路径组合，也不代替 R1 规则研究。

用当前 A 代码重做离线兼容性检查：2,100 个证据快照、5,719 次单元支持比较、
3,086 次有效引用均与固定 B 规则一致；全部必要单元在完整证据后获支持。
7 个不同 optional 单元最终未解决，对应三档 21 个 trace-unit 对，符合可选单元定义。
这属于代码/数据校验，不是模型正确率。

B manifest 仍为 `controlled_mock_ready_for_review`，gold 人工批准和主实验延迟冻结未记录。
此次检查不替代三组最终批准；缺少的 multipart、语义评分与人评也没有自动完成。

### 矩阵、脚本与产物

| 配置 | 数量 | 用途 |
|---|---|---|
| Wait-All、Fixed Progress、Time-Only、First-Evidence | 4 | 现有规则对照 |
| Prompt `_real`：串行、并发 | 2 | 只看问题拆题的主方法 |
| LoRA `_real`：串行、并发 | 2 | 相同 14B 拆题/生成，替换 judge |
| Oracle：串行、并发 | 2 | 独立 gold 输入上界 |

共 10 个配置、预期 9,000 条 policy runs；这是设计规模，没有新模型性能结果。
普通进程不接收 gold，Oracle 另起子进程并接收单独 gold 路径。
模型只看到问题、问题拆解和当前可见证据；历史 gold 描述诊断不进入普通主方法。
保留现有模型、提示词、阈值、生成保护和 RateTTS/并发模拟，没有改变研究定义。
D9 消融、参数网格与新语义 scorer 仍需各自的决定，不擅自加入默认主表。

- `a_work/main_experiments.py`：固定数据/代码/adapter/evaluator，核验 hash，打印/试检调度命令，收集评分。
- `a_work/run_main_experiments.py`：按题分进程，保存进度、调用记录、失败与超时。
- `a_work/slurm/main_experiments.slurm`：H100 Slurm array；不在登录节点运行模型。
- `a_work/tests/test_main_experiments.py`：13 项虚构测试，检查隔离、一致性、快照、失败和试检命令。

当前规范快照为 `main_eval_revised_v1_20261116_v3`：

| 类别 | 路径 |
|---|---|
| 公开 trace 与 private gold | `a_work/results/inputs/main_eval_revised_v1_20261116_v3/` |
| 冻结代码、evaluator、adapter 和 manifest | `a_work/results/code_snapshots/main_eval_revised_v1_20261116_v3/` |
| 预定 GPU 结果，当前尚无结果 | `a_work/results/replay/main_eval_revised_v1_20261116_v3/shard_NNN/` |
| ID 隔离检查 | `a_work/results/analysis/main_dataset_audit_20261116/overlap_check.json` |
| 虚构 HTTP 贯通检查 | `a_work/results/analysis/main_experiments_smoke_20261116/summary.json` |

v1/v2 为保留的准备历史，没有 GPU 运行；v2 虚构 HTTP 检查通过，v3 追加完整试检命令记录
和中断状态处理。输入/快照均 ignored；manifest 如实记录父 commit + dirty 和文件 hash。
用户提交后可另制干净 commit 快照，不能把当前快照冒充干净源码。
准备、验证、打印调度命令与收集用法见 A README 的 Main experiments 节。

默认 30 shard，每 shard 10 题及其全部三档、300 条策略运行，array 同时运行上限 2。
每任务 1 张完整 H100 80GB、8 CPU、64GB RAM、4 小时；已有 adapter 复制并 hash 固定。
14B 与 4B 的显存比例沿用 0.55/0.30；真实双服务启动尚未 GPU 验证。
每普通/Oracle 问题进程有 1,800 秒 watchdog；成功、失败和中断均保留，resume 不自动重试失败。
不改底层 Wait 终止和 HTTP 失败计时定义，以 worker 失败清单容纳这些限制；模拟并发不含同卡竞争。
收集时固定全部预期策略，不漏掉未跑和失败；B 映射待复核时 UCR 仍可能为 null。
配对延迟报告有效数与覆盖，不擅自选择 bootstrap 方法。

### 优先级与实际验证

本次实时核对：`xzhu81` 已授权 `dilek-ic`、normal QoS。
`scavenger` 提供完整 H100、PriorityTier 3；`secondary` 为 tier 1 的 H100 备选。
`IllinoisComputes-GPU` 当前只有 A100/H200，不满足正式 H100 约束。
脚本使用 `--partition=scavenger,secondary --account=dilek-ic --qos=normal --nice=0`；
不降低 nice 优先级，不用未经授权的 QoS。FairShare 权重当前为 0，账号不自动带来该项加分。
分区层级不保证开始时间；抢占和缺失保留。

当前父 `bc412d5` + dirty：A 共 104 项（原 91 + 新 13）、控制 19 项、固定 B evaluator 31 项
全部通过、退出 0，共 154 项 CPU 测试；shell 语法检查通过。
虚构 HTTP 端点贯通 runner 子进程与 B scorer：30 条策略运行、零校验问题，runner/scorer 均退出 0。
没有真实模型调用，这不是 debug 或 main 性能分数。

早期 v1 `sbatch --test-only` 返回 0；后续试检被自动审批拒绝，原因是把输出编号 12490525
解释为实际提交。没有重试调度。只读核对 squeue 无任务、sacct 无该作业；
本机 Slurm 手册说明 `--test-only` 不提交作业。原试检日志记的是待提交命令，漏记实际执行的
`--test-only`，已改为完整实际命令并加 mock 测试；旧日志保留。
v3 没有再次执行 Slurm 试检或实际提交，只有离线校验和命令打印。
当前没有 GPU 作业号、主实验分数或新的人评交付；最终批准与模型运行尚未完成。

已另备 `a_work/results/code_snapshots/main_debug_smoke_20261116/`，固定同版 debug 输入与代码。
`smoke_command.json` 保存实际待提交命令：仅 array task 0、首道 debug 题的三档 × 十配置，
共 30 条策略运行，1 张 H100、30 分钟上限；没有执行命令。
完整 debug bundle 共有 20 个 task，但本次 smoke 命令只选择一个，不隐式提交整套 debug。
建议先验收该 GPU smoke 的模型启动和日志，再决定正式提交主实验。

### 开发集 GPU smoke 提交（2026-11-16）

用户明确要求先提交已准备的开发集 smoke，并询问增加并行卡数。
本次提交范围是 `main_debug_smoke_20261116` 的 task 0：1 道 debug 题 × 三档 × 十配置，
共 30 条策略运行，1 张完整 H100、30 分钟，`dilek-ic`、normal、nice 0、scavenger/secondary。
提交前已核验冻结包 51 个文件 hash；没有使用预留题运行模型。
作业号与提交回执在实际提交后立即补录；目前这段是提交意图，不代表作业已创建或成功。

实际提交回执：2026-11-16 16:20 CST，作业 **12490825**（array task 0），sbatch 退出 0。
提交时工作区 HEAD 为 `7dd78302156ce206c5c0756d5fcb340e0d589c4c`；执行的是既有冻结包，
其父 commit 为 `bc412d5` + dirty，全部文件 hash 校验通过，不用工作区 HEAD 冒充运行源码。

| 运行名 | 数据 / 配置 | 作业号 | GPU | 结果位置 | 当前状态 |
|---|---|---|---|---|---|
| `main_debug_smoke_20261116` task 0 | 固定 B `ea39057` 的第一道 debug 题、三档、十配置；30 条预期运行 | 12490825 | 请求 1 × H100 80GB，未分配 | `a_work/results/replay/main_debug_smoke_20261116/shard_000/` | PENDING / Priority；没有性能分数 |

已用 scontrol 核实 Account=dilek-ic、QOS=normal、Nice=0、Priority=2000、30 分钟、
scavenger/secondary、H100 约束。提交回执保存在冻结包的 `submission_20261116.json`。
用户同时询问更多卡：已提出把主实验 30 个分片一次入队、上限 4 张 H100；
当前仅 smoke 已授权并提交，主实验最终运行确认仍待回复，不自动提交或放行。

用户随后明确选择“先只提交开发集 smoke”。本轮范围据此限定为现有作业 12490825；
不提交、挂起排队或放行主实验，不再把此前的多卡询问解释为最终运行授权。

### 主实验批量提交（2026-11-16）

用户随后明确要求“主实验一起提交”，覆盖上一条仅 smoke 的范围限制。
本次以既有冻结包 `main_eval_revised_v1_20261116_v3` 提交全部 30 个分片，最多 4 张完整 H100
同时运行，预期 9,000 条策略运行。模型、标签、阈值、计时和评分配置保持冻结包原值。
先挂起主实验，待 smoke 执行及独立日志/评分校验通过后再允许启动；不改 gold 或用主实验调参。
作业号和依赖关系在实际提交后立即补录。此段为提交意图，不代表作业已创建或 smoke 已验收。

实际主实验提交于 2026-11-16 16:24 CST，作业 **12490887**，sbatch 退出 0。
已校验冻结包全部 332 个文件；最初加 user hold，在建立下述依赖后移除 hold。
新增 CPU 校验任务 **12490921** 于 16:27 CST 提交，1 CPU、2GB、5 分钟、无 GPU，
使用同一授权账号、QoS、nice 和分区。依赖链为：

`12490825` smoke 成功 → `12490921` 执行/日志校验成功 → `12490887` 主实验可开始调度。

校验任务确认普通/Oracle worker 完整、30 条策略执行均完成且不重复、日志有输出，
再用冻结 B evaluator 检查全部预期配置和记录有效性。允许语义映射待复核，不以分数高低筛选。
任一执行或校验失败则主实验不能启动；全部通过后由 Slurm 自动处理依赖，无需另一次人工 release。
主实验不再处于 user hold，当前等待的是尚未满足的成功依赖。

| 独立运行 | 作业号 | 资源 / 时限 | 来源和产物 | 16:28 CST 核对状态 |
|---|---|---|---|---|
| debug smoke task 0 | 12490825 | 1 H100 / 30 分钟 | 既有 debug 冻结包，`results/replay/main_debug_smoke_20261116/shard_000/` | PENDING / Priority，未分配 GPU |
| smoke 执行/评分校验 | 12490921 | 1 CPU、2GB / 5 分钟 | `results/code_snapshots/main_smoke_validation_20261116/`；输出 `results/analysis/main_debug_smoke_12490825_gate/` | PENDING / Dependency |
| 主实验全 30 分片 | 12490887 | 每片 1 H100 / 4 小时，最多 4 片并行 | `results/code_snapshots/main_eval_revised_v1_20261116_v3/`；`results/replay/main_eval_revised_v1_20261116_v3/` | PENDING，Dependency=afterok:12490921，未分配 GPU |

主实验回执在主冻结包 `submission_20261116.json`，含提交、依赖修改和 release 的实际命令及退出码。
校验脚本单独复制冻结并记录 SHA256，回执在 `main_smoke_validation_20261116/submission.json`。
主实验冻结包仍是原 v3，未将新校验脚本混入或修改已提交的模型/策略代码。
新增源码是 `eval_main_smoke.py`、`slurm/validate_main_smoke.slurm` 和 4 项虚构 gate 测试。
本轮 A 全部 108 项测试、shell 语法检查通过，退出 0；本轮不重复未变更的控制和 B 测试。

目前 `squeue --start` 对 smoke 和主实验均返回 N/A，不能承诺开始日期或固定队列名次。
16:26 CST 的快照中，适用分区有 27 条 H100 请求的数值 Priority 高于本任务 2000；
array 聚合、资源拟合、分区层级和回填不同，不能解释为“前面只有 27 个任务”。
smoke 未运行，故还没有可用于外推主实验墙钟耗时的实测。
在四卡持续满载且每片均用满四小时时，30 片需要 8 批、32 小时配置预算；
这是不含排队的上限预算，不是实际耗时预测；超时和失败仍按原规则保留。

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
