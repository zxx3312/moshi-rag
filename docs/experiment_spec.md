# 实验定义（Experiment Spec）

本文是全组共用的实验定义：数据、计时、策略和指标。代码、gold、评估都以本文为准。
文档与代码不一致时先报告，由人决定改哪一边。

- **已定**：用户提供草稿中已明确的约定；变更需要三组同意，并记入变更记录。
- **暂定**：当前实现或原计划的设置，正式运行前冻结。
- **待定**：尚未决定，负责人见第 11 节。整理文档不构成研究决策或全组批准。

本版依据：用户提供的 2026-11-09 草稿；A 远端 `a-answer-gen` @ `9fb9adc`；
B 接口 `schema.md` v1.3、evaluator @ `638027b`；C debug 交付 @ `10d2394`；
2026-11-11 检查到的本地 `a-cascade` 未提交说明。
原草稿另引 `labeling_guide.md` v1.2、`experiment_config.json` 和 `a_work/unit_schema.md`。
**`docs/proposal.pdf` 当前缺失，尚未独立核对 proposal。**
性能结果放 plan 和各组原始记录，不在此补造。下文数字主要是实验设计参数或数据规模。

## 1. 研究问题与假设

证据陆续到达时，助手应该等待、给出非信息性回应、给出有依据的部分答案，还是给出最终答案？

| 编号 | 假设 | 主要指标 | 状态 |
|---|---|---|---|
| H1 | Evidence-Aware 比 Wait-All 更早给出有依据信息 | TTFGI，与 Wait-All 配对比较 | 已定（原草稿引 proposal，PDF 待核） |
| H2 | Evidence-Aware 的无依据声明少于 Time-Only、First-Evidence、MoshiRAG | Structured UCR | 已定；MoshiRAG 部分等 C1 |
| H3 | Evidence-Aware 最终答对率不明显低于 Wait-All | Unit EM、完成率 | 差距待定（D4） |
| H4 | 当前免训练推理控制可让 MoshiRAG 执行 Wait / Progress / Final，但 Partial 不可靠 | 人工判读 | 有开发结果，待第二人复核；不推广为普遍不可能 |

H1、H2 一起看。主图建议用 TTFGI–UCR 权衡图，多阈值 baseline 画曲线。
H1 在 `short`、`long` 检验；`immediate` 主要报告判断成本。
MoshiRAG 音频与文字回放的时间先对齐（D7）。

## 2. 环境与范围

| 项目 | 定义 | 状态 |
|---|---|---|
| 主实验 | 文字回放，模拟 ASR → LLM → TTS 中的 LLM 部分；问题直接用文本，说话时长估算 | 暂定（D2） |
| 采用级联方案的依据 | 当前 MoshiRAG Partial 控制不可靠，见 A 的 FINDINGS | 已定，结果仍需复核 |
| MoshiRAG | 外部系统对照和可控性分析 | 已定 |
| 对话 | 单轮问题，不使用 proposal 中的对话上下文 H_t | 已定，写入局限 |

本地已有 ASR/Piper 实现与 smoke 提交记录，见 `a_work/cascade.md`。
这不等于主实验已切换为真实语音，也不等于在线全双工验收完成。改变主实验口径先确认 D2。

## 3. 数据与隔离

| 集合 | 规模与组成 | 用途 | 状态 |
|---|---|---|---|
| `debug-v0` | 20 题：HotpotQA 8（bridge 4、comparison 4）；2Wiki 8（每类 2）；自建 multipart 4 | 开发、提示词、错误分析 | 已定，已有 gold、trace |
| `sft-v0` | 300 题：243 train / 57 dev；2Wiki 153、HotpotQA 147；官方 train | 训练 LoRA、选择 checkpoint | 已定，已有 gold、SFT |
| 预留评测集 | 300 题：HotpotQA 150（bridge 75、comparison 75）；2Wiki 150（bridge_comparison 38、comparison 38、compositional 37、inference 37）；官方 dev | 全部冻结后最终评估一次 | 原抽样 seed 42，规模/划分冻结待 D13；B 新增 gold 草稿提交，未验收 |
| 多部分评测集 | 来源、题数待定 | 检验 Partial 主要场景 | D5；预留集原设计无 multipart |
| MoshiRAG 控制集 | 初版 14 题（SimpleQA 12 + 两段证据 2）；扩展版 18 道两段证据题 | H4 | 开发结果见 FINDINGS，不是主评测 |

文件位于 B 分支：

- debug：`b_work/step2/prepared/samples_debug.jsonl`、`b_work/step3/gold_debug.jsonl`、`b_work/step3/traces_debug.jsonl`。
- SFT：`b_work/step4/gold_sft.jsonl`、`b_work/step4/sft/sft_train.jsonl`、`b_work/step4/sft/sft_dev.jsonl`。
- 预留题：`b_work/step2/prepared/samples_eval_reserved.jsonl`，**开发期间禁止读取**，其派生 gold、trace 同样禁止。
- 划分清单：`b_work/step2/prepared/split_manifest.json`、`b_work/step4/prepared/sft_manifest.json`。

三个集合不重复，由 B 构建脚本检查。train 用于训练、dev 用于选择。
提示词示例必须虚构。预留集只允许 B1 标注会话或用户明确说“这是最终运行”的 F1 会话访问；
B1 会话不能修改 A 代码和提示词。最终运行前把冻结 commit 写入变更记录。
debug 数字只能用于开发过程、错误分析，不作为主结果。
B 的最新预留 gold 草稿状态仅从提交元数据确认，未查看内容。

## 4. Trace 与时间

| 项目 | 定义 | 状态 |
|---|---|---|
| 时间原点 | 用户问题结束，`time_origin: question_end`，秒 | 已定 |
| 可见性 | t 时只给策略 `visible_time_s <= t` 的证据 | 已定 |
| 证据粒度 | 每句一个事件，包括干扰句；同文档句子同时到达，带文档标题 | 已定 |
| trace 类型 | 当前 A/B 回放使用 `controlled_mock`；真实检索 `retrieved` 尚待 B5 | 暂定 |
| 决策间隔 | `tick_s=0.5` 秒 | 暂定 |
| 观察窗口 | 检索结束后 `max_extra_s=5.0` 秒 | 暂定 |

| 延迟方案 | 第一批 | 第二批 | 状态 |
|---|---|---|---|
| `immediate` | 全文档 0.0 秒 | — | 暂定（D1） |
| `short` | 1.0 秒 | 3.0 秒 | 暂定（D1） |
| `long` | 2.0 秒 | 8.0 秒 | 暂定（D1） |

B 的 `build_traces.py` 按 supporting facts 引用顺序把支持文档分成两半，桥接第一跳在第一批。
干扰文档轮流放入两批。细节见 B 的 step3 README。
延迟方案代表的真实场景需用诊断记录与可选 B5 支撑。
原草稿引用 MoshiRAG 论文的检索延迟数字，因本次未核对论文，不在此重述为事实。

## 5. 时间成本模型

文字回放时钟由 `a_work/turntaking/replay.py` 实现，未经过真实 ASR/TTS。

| 成本 | 当前约定 | 状态 |
|---|---|---|
| judge | 实测调用时间计入时钟，同一组可见证据只计一次 | 暂定 |
| 拆题 | 实测 `setup_cost_s`，推迟首次判断，仅 `_real` | 暂定 |
| 生成 | 实测调用时间；缓存命中仍按原调用时间计 | 暂定 |
| 固定决策 | `decision_cost_s=0.0` | D2 |
| Partial / Final 说话 | 词数 ÷ 2.5 词/秒，最短 1.0 秒 | 暂定，S1 校准 |
| Progress | `--generate` 时同上，固定短语 5 词对应 2.0 秒；否则 1.0 秒 | 暂定 |
| Backchannel | 固定 1.0 秒，不随 `--generate` 改变 | 暂定，与 Progress 算法不一致（D2） |
| 无 `--generate` 的声明 | 每声明 `CLAIM_S=2.0` 秒 | 仅调试 |
| 声明位置 | 按值在文本的位置占比估算 | D11；本地 Piper 分支另有估计方式，需核对 |
| 并发 | `--concurrent` 让说话时继续判断、生成，不模拟模型竞争拖慢 | D2 |
| 显卡 | 延迟只在同型号比较；正式结果 H100 | 已定 |

Piper 音频总长度实测不代表声明位置或整个时间轴已经实测。
当前级联分支仍使用模拟证据日程；不得把其回放称为真实在线全双工结果。

## 6. 动作与策略

### 6.1 动作

`Wait`、`Backchannel`、`Progress`、`Partial Answer`、`Final Answer`。
字符串与 B 的 `experiment_config.json` 一致，已定。

### 6.2 Evidence-Aware

judge 给单元打标签，`policies.py` 依次应用以下规则。“新单元”指 SUPPORTED 且尚未说过。

| 优先级 | 条件 | 动作 |
|---|---|---|
| 1 | 所有必要单元 SUPPORTED | Final，只说尚未说过的必要单元 |
| 2 | 检索结束但仍不完全充分 | Final，说新单元，说明其余未确认 |
| 3 | 有新单元 | Partial，只说新单元事实 |
| 4 | 上次 Partial 后没有新单元 | Progress，每次 Partial 后最多一次 |
| 5 | 尚未说 Backchannel | Backchannel，通常在 0 秒，拆题未完成也可说 |
| 6 | 已过 `progress_after_s=3.0`，未说过 Progress 或事实 | Progress |
| 7 | 其他 | Wait |

映射规则已定；3.0 秒暂定（D3）；检索结束仍不充分时的说法待 D10。
`unit_schema.md` 仍有 Partial 附带进度的旧描述，与此处 facts-only 有差异，先报告，不擅改研究规则。

### 6.3 Baseline

| 策略 | 规则 | 参数与状态 |
|---|---|---|
| Wait-All | 检索完成后回答 | 已定 |
| Fixed Progress | 固定时间说一次 Progress，之后同 Wait-All | `progress_at_s=1.0`，暂定（D3） |
| Time-Only | 到固定时间回答；检索提前完成也回答 | `answer_at_s=3.0`，暂定；正式结果扫描多个阈值（D3） |
| First-Evidence | 看到任何证据即回答 | 已定 |
| MoshiRAG | C 运行的原异步检索系统 | 待时间对齐与正式评分（D7） |

`--generate` 时，规则 baseline 的 `Generator.free` 用全部可见证据尽力回答，可能答错。

### 6.4 回放配置

| 配置 | 单元 | judge | gold 对应 | 用途 |
|---|---|---|---|---|
| 四个规则 baseline | 无 | 无 | 按值对应，需复核 | 对照 |
| `evidence_aware+oracle` | gold | gold 支持关系 | `--aligned-policy` | 上限 |
| `evidence_aware+<judge>` | gold 描述，去掉答案 | 真实 judge | 与 gold 编号相同 | 历史诊断，隔离 judge 差距 |
| `evidence_aware+<judge>_real` | 模型只看问题拆题 | 真实 judge | 按值对应，需复核 | **主方法** |

论文主表只用 `_real` 代表本方法。普通策略不得读取 gold。
历史诊断配置用 gold 描述的输入路径需与 B 接口的隔离要求核对，不得因此把 gold 交给主方法。

## 7. Judge 与模型

### 7.1 标签

已定规则详见 `a_work/unit_schema.md` 第 5 节：

- `SUPPORTED`：可见证据明确支持候选值，引用全可见，依赖全 SUPPORTED。
- `UNRESOLVED`：证据不足或依赖没有证据。
- `CONTRADICTED`：可见证据与候选值冲突。
- `by_omission`：定义性介绍未列出的职业、国籍、类别可按否定处理，单独统计。
  A 已采用；B 关于运行时使用仍待 D14，不能写成全组已冻结。
- `by_presupposition`：问题明确点名的候选或条件可作已知，包括二选一排除；单独统计。
- 比较结论的标签由代码从依赖推导，值由模型给出。引用写证据 ID，不写单元 ID。
- 支持和冲突并存、需要常识的否定、纠错计分等未定项见 D10、D14。

### 7.2 模型

LLM 全部开源，vLLM 部署，temperature 0。现有开源 ASR/TTS 是语音组件，不是 LLM 替换。

| 角色 | 模型 | 当前设置 | 状态 |
|---|---|---|---|
| 拆题 | Qwen3-14B | 不思考，只看问题 | 暂定 |
| 生成 | Qwen3-14B | 不思考，尽量短；超过 40 词、漏值或加未判断内容则退回直接念事实 | 暂定 |
| Prompt judge | Qwen3-14B | 不思考，few-shot | 暂定 |
| LoRA judge | Qwen3-4B + LoRA | r=16，lr=2e-4，batch 2 × 累积 4，仅 q/k/v/o，训练 3 epoch，dev 选择 checkpoint，推理不带 few-shot | 暂定 |
| Oracle | 无模型 | gold `support_sets`、`presupposition_sets` | 已定，仅独立 oracle 输入 |

已选 checkpoint 和开发比较详见 `lora_judge.md`，旧结果的 provenance 待 plan 核对。
思考模式不是默认，原因见 `judge_notes.md` 3.10；不在此重复缺少完整运行元数据的性能数字。
SFT 无 CONTRADICTED、单答案和 multipart；训练用 gold 描述，运行时用模型描述，需报告局限。

### 7.3 生成不对称（D9）

本方法生成器只拿 judge 判过的事实，baseline 生成器拿全部可见证据。
需决定是否让 Wait-All 也先 judge 再用相同生成方式，分离策略与生成方式影响。

## 8. 指标

正式分数由 B 的 `b_work/eval/` 算；A 的 `preview.py` 只自查。

| 指标 | 定义 | 状态 |
|---|---|---|
| Unit EM / F1 | 必要 gold 单元的值匹配率 / 词重叠；缺失 0 | 已定 |
| Structured UCR | 值错误或无有效引用的声明数 / 声明总数；任一映射待复核则 null | 已定 |
| TTFR | 第一次非 Wait 输出开始，包括 Backchannel、Progress | 已定 |
| TTFGI | 第一个有依据声明开始；optional 桥接中间单元也算 | 已定 |
| TTCA | 所有必要单元被正确、有依据说完的最早时间 | 已定 |
| 完成 | 所有必要值正确，表达时支持证据可见 | 已定 |
| `final_correct` | 问题要的答案是否答对，目前 A 自查 | 是否正式使用待定 |
| omission / presupposition | 单独计数 | 已定 |

Backchannel 通常在 0 秒，因此主要看 TTFGI。
文字回放用 `--timing-kind estimated`；音频满足实测与接口条件后才用 `observed`，分开报告。
SFT 与 debug 的问题预设支持关系写法不同；evaluator 使用 `presupposition_sets`，需 D15 统一。
未知或未测时间留 null；不得用决策时间冒充说出声明的时间。

## 9. 统计与报告

| 项目 | 做法 | 状态 |
|---|---|---|
| 配对 | 同一 trace 与 Wait-All 比较，报告差值中位数和更早比例 | 已定 |
| 时间 | 中位数及有效样本数，不隐去缺失运行 | 已定 |
| 置信区间 | 按题目重采样的配对 bootstrap；同题多延迟不独立 | 待 D6 |
| 随机性 | temperature 0 仍可能受 vLLM 批处理影响 | 是否重复运行待定 |
| 分组 | 按延迟方案、题型报告 | 已定 |

助手辅助的 claim 映射不是独立人工复核。未完成复核不报告整体 UCR。
失败、不完整、无事实声明及无效时间都保留，不能通过排除坏结果提高表现。

## 10. 范围外的专门说明

- MoshiRAG 控制细节：`a_work/moshirag_control/FINDINGS.md`。
- ASR/Piper 实现和限制：本地 `a_work/cascade.md`，尚未提交。
- 人评流程：plan 的 A7、C2，尚未冻结。
- 运行与元数据缺口：`docs/plan.md`。

## 11. 待定决定

| ID | 决定 | 负责 | 最晚时间 |
|---|---|---|---|
| D1 | 冻结三种延迟 | B | 预留 trace 生成前 |
| D2 | TTS 校准、Backchannel/Progress 统一、decision cost、concurrent、主实验时间口径 | A+B | 最终运行前 |
| D3 | Time-Only 扫描范围、两个 progress 阈值 | A | 最终运行前 |
| D4 | H3 可接受的答对率差距 | 全组 | 写论文前 |
| D5 | multipart 评测来源、规模 | B | 预留标注时 |
| D6 | 置信区间方法 | B | 最终运行前 |
| D7 | MoshiRAG 与回放时间对齐；B 建议参考文本注入结束时间 | C+B | C 正式运行前 |
| D8 | judge 验证集另建约 200 条人工标注，还是用预留 gold | A+B | judge 正式比较前 |
| D9 | 是否做生成方式消融 | A | 最终运行前 |
| D10 | 检索结束不充分时的说法；冲突、更正、撤回计分 | A+B | 最终运行前 |
| D11 | 文字声明时间估算、音频对齐 | A+B+C | 最终运行前 |
| D12 | 引用口述还是仅日志记录 | A+B | 写论文前 |
| D13 | 冻结数据划分 seed、规模 | B | 预留标注前 |
| D14 | 运行时 omission、常识否定、My Inspiration d3s1、Gingrich 年份要求 | A+B | 预留标注前 |
| D15 | 统一问题预设 gold 写法 | B | 预留标注前 |

B 已有预留 gold 草稿提交，不等于 D13–D15 已获全组批准；需 B 独立核对冻结与标注的先后关系。
D8 若选择预留 gold，仍必须遵守保留集禁读要求，不能借 judge 开发提前访问。

## 变更记录

| 日期 | 改动 | 同意者 / 状态 |
|---|---|---|
| 2026-11-09 | 用户提供初稿，依据 A `9fb9adc` 和各组文档 | 原稿待确认 |
| 2026-11-11 | 按用户要求落库；同步 B gold 草稿、C debug 交付、A 本地级联状态；补充来源、隔离和不一致说明 | 用户授权整理；未冻结研究决定；PDF 待补 |
