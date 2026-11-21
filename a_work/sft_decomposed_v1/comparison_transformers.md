# vLLM 拆题结果与 Transformers 版本对比

共 300 道题：train 243、dev 57。模型仅接收问题；新单元待复核，不含新答案和证据标签。

| 检查项 | 数量 |
|---|---|
| vLLM fallback | 0 |
| 拆解字段完全相同 | 292 |
| 存在差异的题目 | 8 |
| 题型不同 | 3 |
| 单元数量不同 | 4 |
| necessary/depends_on 结构不同 | 4 |

统计可能重叠。文字不同不一定代表语义不同；相同结构也不代表语义等价。差异同时涉及推理后端、JSON 约束和 GPU，不能单独归因于某一个因素。

B 源文件哈希、train/dev 归属、300 个 ID 以及问题提示词对应的模型调用记录均已检查。

| Split | Sample ID | Transformers → vLLM 题型 | 单元数 | 依赖/necessary结构变化 |
|---|---|---|---|---|
| train | 2wikimultihopqa_75141b5d086911ebbd5eac1f6bf848b6 | comparison → comparison | 3 → 5 | True |
| train | 2wikimultihopqa_8b1a578708a211ebbd7aac1f6bf848b6 | bridge_comparison → comparison | 5 → 3 | True |
| train | hotpotqa_5ab3c3b155429969a97a81b6 | comparison → comparison | 3 → 3 | False |
| train | hotpotqa_5ab8292c55429934fafe6cfe | bridge → single | 2 → 1 | True |
| train | hotpotqa_5ac16e3055429964131be1f3 | comparison → comparison | 3 → 3 | False |
| dev | 2wikimultihopqa_75be1186086711ebbd5eac1f6bf848b6 | comparison → comparison | 3 → 3 | False |
| dev | hotpotqa_5a7aa8565542995eb53be88b | bridge → single | 2 → 1 | True |
| dev | hotpotqa_5ab7eff35542993667794059 | bridge_comparison → bridge_comparison | 3 → 3 | False |
