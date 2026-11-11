# AI 助手工作规则

本仓库是 `kyutai-labs/moshi-rag` 的 fork，用于课程研究项目
**Computation-Aware Turn-Taking for Full-Duplex Spoken Agents**。
研究问题：证据陆续到达时，语音助手什么时候该等、说进度、说部分答案、说完整答案。
Proposal 的约定位置是 `docs/proposal.pdf`。缺失时报告，不要猜测其内容。

本文件适用于整个仓库。`AGENTS.md` 链接本文件，让使用这两种入口的助手读取同一套规则。
实验定义见 `docs/experiment_spec.md`；步骤、进度、运行记录见 `docs/plan.md`。

## 开始任何任务之前

1. 先读 `docs/experiment_spec.md` 和 `docs/plan.md`。
2. 检查 `git status --short --branch`，保留已有的未提交改动。需要同步代码时，先
   `git fetch --all --prune`，确认分支关系后才做安全的快进；不要自动 stash、reset 或覆盖文件。
3. 读任务所在组的说明：
   - A（策略 / 控制器）：`a_work/README.md`、`a_work/unit_schema.md`、
     `a_work/judge_notes.md`、`a_work/lora_judge.md`。
   - B（数据 / 评估）：`b_work/step1/schema.md`、`b_work/eval/README.md`。
   - C（MoshiRAG 对照 / 人评）：`c_work/deliveries/*/README.md`。
   各组文件合并前可能只在自己的分支。A 的远端开发分支为 `a-answer-gen`，
   B 为 `b-data-eval`，C 为 `c-external-baselines`。先检查实际分支，
   不切换分支时用 `git show origin/<branch>:<path>`。本地 `a-cascade` 的未提交内容
   不等于远端已交付内容。
4. 用自己的话复述任务，说明对应的 plan 步骤、完成标准和不清楚的地方。
   研究决定（测什么、规则怎么定、阈值多少）问人，不要自己定。
   已获授权的实现和文档整理可以继续做。
5. 一次只做 `docs/plan.md` 中的一个步骤。任务超出当前步骤时先说明，
   不要顺手推进实验或消耗预留评测集。

## 数据

- **不得打开、读取、打印或使用** `b_work/step2/prepared/samples_eval_reserved.jsonl`，
  以及以后由它生成的 gold、trace 或其他包含题目、答案和证据的派生文件。
  不要通过全仓库内容搜索、打包整个 B 分支、批量读取结果等方式间接访问。
  只有两种例外，而且都需要用户明确说明：
  1. B1：给预留集标注 gold。这样的会话不得修改 A 组代码和提示词。
  2. F1：用户明确说“这是最终运行”。
- 可以通过提交元数据确认预留集工作是否有新提交；这不代表检查过标注质量或验收完成。
- 调提示词、改规则、选阈值、选模型只用 debug（20 题）和 SFT。
  SFT train 用于训练，dev 用于选择。改完在 `a_work/judge_notes.md` 记一行。
- 提示词示例必须是虚构内容，不得复制 debug、SFT 或评测题。
- 普通策略不得读取 gold。只有 `OracleJudge` 可以通过单独输入路径读 gold。
  evaluator 的 gold 输入与策略输入分开。历史的 gold 单元诊断配置不代表主方法可以读 gold。
- 时刻 t 的策略只能看到 `visible_time_s <= t` 的证据。
  完整 trace 和未来到达内容由调度器保管，不得交给普通模型。

## 实验定义与分工

- 指标、数据划分、延迟方案、时间成本、baseline 参数、标签规则以
  `docs/experiment_spec.md` 为准。要改其中任何一项，先停下，说明改什么、为什么，
  得到用户同意后再改，并在 spec 变更记录记一行。
- “已定”项的变更需要三组同意；助手不能代替任何组同意。
- 文档与代码不一致时，报告两边的路径和差异，先由人决定改哪一边。
- A 分支不改 B 的 evaluator 和 gold。发现问题，记录并交给 B。
- 不把草稿、排队、接口验收、助手辅助复核写成正式结果或独立人工标注。

## 测试

不得为了让测试通过而修改或删除测试。认为测试错了时，说明原因并问用户。
说“完成”前运行适用测试并报告实际数量、退出码、分支和代码版本。
历史数量是参考值，不得为了对齐数量改测试。

```bash
python3 -m unittest discover -s a_work/tests           # 原记录 73 项；以当前实际输出为准
python3 a_work/moshirag_control/tests/test_control.py  # 原记录 19 项
python3 -m unittest discover -s b_work/eval/tests      # B 分支，原记录 31 项
```

不要为运行测试而检出整个含预留数据的 B 工作树。可以只从固定的 B commit 提取
`b_work/eval/` 到临时目录再测试。`main` 缺少各组代码时，在对应组工作区验证，
并明确测试覆盖的是哪一份代码。

## 结果与运行记录

- 文档中的实验结果数字必须来自真实运行。一起记录运行名、代码 commit、数据来源和版本、
  显卡、结果路径；GPU 作业还要记录作业号。设计参数和数据规模不是性能结果，需说明用途。
- 未提交代码要标明父 commit 加 dirty，并保留源文件 hash 或快照清单。
- 不编造、估算或补齐缺失结果。离线估算必须写“估算”，不能冒充实测。
- 失败运行和不好的结果也保留。旧记录缺少元数据时写“待补”，不猜。
- 每次提交 GPU 作业先记录运行名和作业号；结束后在 `docs/plan.md` 的运行记录补全状态和结果。
  排队不算完成。本次新运行每个独立运行一行，旧的汇总记录后续逐项核实。
- 延迟只在同型号显卡之间比较，正式结果用 H100。
- debug 数字只能用于开发过程或错误分析，不能作为论文主结果。
- 有待复核的 Structured UCR 保留 null，不把已评分子集比例冒充整体 UCR。

## 代码和环境

- 不使用付费 API。LLM 只用开源 Qwen3 系列，在 Campus Cluster 用 vLLM 部署。
  MoshiRAG 对照、现有开源 ASR/TTS 组件按实验角色使用；它们不是新增 LLM 选择。
- `a_work/turntaking/`、`a_work/run_*.py`、`a_work/eval_*.py`、`b_work/eval/`
  只用 Python 标准库。训练、vLLM、MoshiRAG 相关脚本可用已有依赖。
  新增依赖前问用户。现有代码若违反约束，先报告，不借整理文档擅自重构。
- GPU 任务一律 `sbatch`，不在登录节点运行模型。
- 每次提交前实时检查 `scontrol show reservation -o`、`sinfo -R`、候选分区/节点状态和账号权限。
  优先选没有受维护影响、且满足 GPU 型号、显存与时限的分区；同分区部分节点维护时，
  使用未受影响的合格节点，不把整个分区都当作停机。检查运行时段是否与已公告维护窗口重叠。
  排队原因 `Priority` / `Resources` 不等于维护；分区 `UP` 也不保证立即有空卡。
- H100 评估目前默认 `secondary`；以后每次重查，不永久依赖本次状态。
  不为绕开维护擅自换显卡或账号，不使用不满足实验要求的 MIG 切片。
  备用分区需确认权限、时限及抢占/重排队条件；`scavenger` 不自动作为默认回退。
  无合格资源时说明原因并等待；用户只要求后续调度时，不取消、迁移或重复提交已有作业。
  可以先用 `sbatch --test-only` 验证资源申请；它不实际创建 GPU 运行。
- 结果写 `a_work/results/<category>/<run_name>/`，不进 git。
  跨分支复制输入放 `a_work/results/inputs/`，记录来源分支、完整 commit 和文件 hash。
- 不改上游代码 `moshi/`、`rust/`、`client/`，除非任务明确要求。
- 文件改动后，同步更新所在组 README 文件表。共享文档入口更新根 README。
- 集群账号 `dilek-ic`。环境和缓存路径以当前 `a_work/slurm/eval_judge.slurm` 为准。

## Git

- 共享文档（本文件、`AGENTS.md`、`docs/`）放 `main`，各组再把 `main` 合并到自己的分支。
  当前会话按用户要求只在原有 `moshi-rag` 目录整理；不要自行新建工作树、仓库副本或额外工作目录。
  共享文档目前若未在 main，写明待同步，由用户提交后安排；不能假装其他分支已同步。
- A 的 PR 合并到 `a-method-integration`；B、C 在各自分支工作。
  合并到 `main` 由全组决定，不直接推送 `main`。
- **不要自行 commit 或 push。每次完成工作后只提供建议的英文 commit message，由用户提交。**
  不因 plan 列了步骤就自动建 PR、合并或打 tag；需要用户明确要求。
- commit 信息用简短英文，说明改了什么和为什么。
- commit 和 PR 不加任何 AI 署名，不加 `Co-Authored-By: Claude ...` 或 `Generated with ...`。
- 不提交结果、音频、模型权重、原始数据集和密钥（包括 HF token）。

## 常用命令

以下命令在有 A 组代码的工作区、仓库根目录执行；阅读规则不代表授权运行 GPU 实验。

```bash
python3 a_work/run_demo.py
sbatch a_work/slurm/eval_judge.slurm

# 只复制 debug；先记录 origin/b-data-eval 的完整 commit。
mkdir -p a_work/results/inputs/debug_v0
git rev-parse origin/b-data-eval
git show origin/b-data-eval:b_work/step3/traces_debug.jsonl > a_work/results/inputs/debug_v0/traces_debug.jsonl
git show origin/b-data-eval:b_work/step3/gold_debug.jsonl > a_work/results/inputs/debug_v0/gold_debug.jsonl
D=a_work/results/inputs/debug_v0
SCRIPT=a_work/run_replay.py RESULT_GROUP=replay \
  EVAL_ARGS="--trace $D/traces_debug.jsonl --gold $D/gold_debug.jsonl --generate" \
  sbatch a_work/slurm/eval_judge.slurm

# B evaluator；LOG/TRACE/GOLD/COMMIT/OUT 换成获准数据和真实版本。
python3 -m b_work.eval.run_eval --logs LOG --traces TRACE --gold GOLD \
  --timing-kind estimated --runner-commit COMMIT --out OUT
```

## 每次任务结束时

1. 更新 plan 中当前一步的状态、产物和未解决问题。只做了一部分就写“进行中”。
2. GPU 运行更新运行记录；规则、提示词和模型选择更新 A 的 judge notes。
3. 更新相应 README 文件表，检查 diff 与未跟踪文件，确认没有数据、密钥或结果混入。
4. 报告改了什么、测试结果、尚缺什么，并给出简短英文 commit message。由用户提交，不自行 commit 或 push。

A 的笔记用中文，代码、字段名、命令用英文。用词简单，一句话说一件事。
记录“做了什么、结果怎样、为什么这样决定”，不写空泛总结。
