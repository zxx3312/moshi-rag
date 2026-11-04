# LoRA judge

状态：训练脚本已写好，正在试跑，还没有准确率结果。

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
