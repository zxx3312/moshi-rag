# LoRA judge

状态：`qwen3_4b_v1` 已训练并做过初步比较，正式对比要等 B 组的 judge 验证集。结果见文末。

用途：分工要求比较三种 judge：Oracle、prompt judge（Qwen3-14B）、LoRA SFT 小模型。LoRA judge 由 `train_lora_judge.py` 训练，推理时仍走 `PromptJudge`（换成 adapter 的模型名、不带 few-shot），所有校验逻辑相同。

## 为什么选 Qwen3-4B

1. **分工的定位**：分工要求"LoRA SFT 小模型"，与大模型的 prompt judge 形成对比。
2. **延迟是实际问题**：Qwen3-14B 在 A100 上平均每次判断 2.8 秒，最长 5.5 秒（B 组 20 题，60 条 trace）。在 `short` 延迟下，prompt 版首次给出有依据信息的中位时间（3.4 秒）比 Wait-All（3.0 秒）还晚。模型更小才有可能省下这段时间。
3. **任务窄**：judge 只读证据、输出固定格式的标签，B 组提供 1,991 条专用训练样本，可以检验小模型经过训练能否补上差距。
4. **资源占用小**：权重 8.0GB，Qwen3-14B 为 29.5GB，训练和部署对显存的要求更低。

**风险**：模型能力弱于 14B，可能更容易错判。延迟和准确率都待实测。准确率不够时换 8B 或 14B，只需改 `--base`。

## 数据

B 组 `b_work/step4/sft/`（sft-v0）：训练 1,991 条（243 题），验证 486 条（57 题），全部来自官方 train，与 debug 和预留评测题不重叠。本地副本在 `results/inputs/sft_v0/`。

| B 组列出的问题 | 处理 |
|---|---|
| few-shot 回复会被反复当作训练目标 | 训练脚本去掉示例，推理也不带 |
| 超长样本 | 超过 4096 token 的丢弃，不截断。用 Qwen3-4B 的分词器统计：训练集丢 10 条，验证集 0 条 |
| 只对最终回复计算损失 | 提示部分的 label 全部屏蔽 |
| "排除输家"规则 | 已加入 `JUDGE_SYSTEM` 和 `derive_conclusion`，提示词与 SFT 数据逐字一致 |
| `OracleJudge` 不读 `presupposition_sets` | 已按 `build_sft.py` 的规则实现 |
| 标注标准不一致（取值写法等） | 暂时接受，这一版视为试跑 |
| 没有 CONTRADICTED 样本 | 接受，写入局限：LoRA judge 基本不会输出这个标签 |
| 训练用 gold 单元描述，运行时用拆题器的单元 | 接受，需要用 `prompt_real` 对应的回放检验 |

局限：SFT 数据没有单一答案题和多部分题，这两类要在 debug 集上单独看。

## 流程

```bash
# 试跑
RUN_NAME=smoke TRAIN_ARGS="--max-train 40 --max-dev 20 --epochs 1" sbatch a_work/slurm/train_lora.slurm
# 完整训练
RUN_NAME=qwen3_4b_v1 sbatch a_work/slurm/train_lora.slurm
# 验证集评估（--judge-model 用 adapter；基线不加 VLLM_ARGS 和 --no-examples）
D=a_work/results/inputs/sft_v0/sft_dev.jsonl
MODEL=Qwen/Qwen3-4B RESULT_GROUP=lora_eval RUN_NAME=qwen3_4b_v1 SCRIPT=a_work/eval_sft.py \
  VLLM_ARGS="--enable-lora --lora-modules judge=a_work/results/lora/qwen3_4b_v1/best" \
  EVAL_ARGS="--dev $D --judge-model judge --no-examples" sbatch a_work/slurm/eval_judge.slurm
```

选模型用 `sft_dev`，错误分析用 20 道 debug 题。正式的三种 judge 对比要等 B 组的 judge 验证集；预留的 300 题只在最后跑一次。

默认参数：LoRA r=16，学习率 2e-4，3 个 epoch，batch 2 × 梯度累积 4，只训练 attention 的 q/k/v/o 投影层。这些是常用的初始值，还没有调过。

## 结果

### 训练

`results/lora/qwen3_4b_v1`：训练 1,981 条（丢弃 10 条），验证 486 条，用时 57 分钟。三个 epoch 的验证损失为 0.0130、0.0146、0.0187，`best/` 是第 1 个 epoch，之后开始过拟合。

### SFT 验证集（A100）

| 模型 | 单元一致率 | 错判 SUPPORTED | 漏判 SUPPORTED | 每条耗时 |
|---|---|---|---|---|
| LoRA 4B | 93.9% | 13.2%（76/574） | 0.9%（7/778） | 1.39 秒 |
| Prompt 4B | 72.0% | 53.3% | 9.1% | 1.31 秒 |
| Prompt 14B | 85.7% | 20.7% | 9.4% | 2.93 秒 |

- 这些数字来自 SFT 的标签，而错判样本里有些疑似标签问题，还在核对。全部 76 条见 `results/lora_eval/lora_false_supported.md`（不进 git）。
- 训练、验证和 debug 题没有重叠，也没有完全重复的样本。但 SFT 没有 CONTRADICTED 和多部分题。

### Debug 20 题

| 模型 | 单元一致率 | 错判 SUPPORTED | 漏判 SUPPORTED | 取值正确率 | 状态正确率 |
|---|---|---|---|---|---|
| LoRA 4B | 95% | 12/160 | 5/197 | 94% | 91% |
| Prompt 4B | 94% | 20/160 | 2/197 | 77% | 87% |
| Prompt 14B | 94% | 8/160 | 12/197 | 89% | 89% |

拆题暂时仍用 14B：结构正确率 90%，4B 只有 60%。

### 回放（v4，拆题和生成用 14B，只换 judge）

正数表示比 Wait-All 早，单位是秒，取配对中位数，依次为 immediate / short / long。

| judge | TTFGI | TTCA | 答对 | 无依据 / 声明数 | judge 秒/trace |
|---|---|---|---|---|---|
| Oracle | +0.4 / +2.4 / +6.4 | +0.4 / -4.4 / -1.2 | 60/60 | 0/104 | 0 |
| Prompt 14B | -2.3 / -2.1 / +1.9 | -2.3 / -8.3 / -4.3 | 48/60 | 7/92 | 4.26 |
| LoRA | -0.9 / +1.2 / +5.6 | -0.5 / -6.6 / -3.4 | 49/60 | 11/96 | 2.08 |
| LoRA（模型拆题） | -3.3 / +0.5 / +5.5 | -2.9 / -5.6 / -3.1 | 46/60 | 10/90 | 1.94 |

结论：LoRA 省下一半判断时间，第一条有效信息因此明显提前；答对数和 14B 差不多，无依据多 4 条，样本太小，分不出高下。Oracle 的 TTCA 也落后，说明完整答案变晚主要不是 judge 造成的，而是 Partial 占用说话时间、Final 重复内容。

### 针对 TTCA 的改动（待验证）

- Partial 只说事实。说完后如果证据还没齐，再由策略说一句 Progress；已齐就直接说 Final。
- Final 只说新内容。Wait-All 也用同样的简短要求，比较才公平。
- `--concurrent`：判断和生成在说话时继续运行。没有模拟模型之间互相拖慢，所以这部分收益可能偏乐观。

用 v4 日志离线估算，short 和 long 档的 LoRA TTCA 约为 +0.6 和 +5.4。这只是估算，而且没有按同样的简短要求缩短 Wait-All，要以真实回放为准。"Partial 前多等几秒"在估算中反而变差，暂不做。
