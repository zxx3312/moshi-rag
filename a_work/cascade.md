# 级联语音实验

当前实现是 **真实 ASR / LLM / TTS + 模拟证据时间轴**。它还不是实时双工语音服务器。
`run_replay.py` 默认仍使用问题原文和每秒 2.5 个单词的语速；必须显式传入 `--asr`
和 `--tts piper:...` 才会使用语音组件。

## 已有组件

- `make_question_audio.py`：Piper 合成问题。当前 debug 的 20 条音频已在
  `results/inputs/b_debug_q1_20_gold13/question_audio/`，使用 `en_US-lessac-medium`。
- `run_asr.py`：Whisper `large-v3-turbo` 转写，保存转写文本、延迟和逐题 WER。
  它对完整问题做非流式识别；GPU 预热和模型加载不计入逐题延迟。
- `turntaking/cascade.py`：Piper 输出实际音频长度和首块合成耗时；固定反馈短语视为预合成。
- `run_replay.py --save-audio`：保存每个不同回答的 WAV 和索引。它不输出完整对话混音。
- `llm_calls.jsonl`：保存调用结果与延迟，供同样请求的离线回放使用。

## 首次 smoke test

使用 debug 输入中按原顺序出现的第一道 bridge 和第一道 multipart 题：Caroline 的祖父、
Apollo 11 的发射和溅落日期；各跑 immediate / short / long，共 6 条 trace。
这是接口验收，不用于选择模型或报告准确率。

2026-11-10 已提交作业 **12308419**，输出名 `cascade_smoke_20261110_v1`。
快照与提交参数位于 `results/code_snapshots/cascade_smoke_20261110_v1/`，
输入位于 `results/inputs/cascade_smoke_20261110_v1/`。2026-11-11 查询仍为 PENDING，
原因 Priority，申请 A100；尚未验收，不能写成链路已跑通。正式结果按 spec 使用 H100。

作业脚本：`slurm/cascade_smoke.slurm`。在仓库根目录提交，设置：

```bash
export SNAPSHOT=/absolute/path/to/frozen/code
export INPUT_DIR=/absolute/path/to/debug/subset
export RUN_NAME=unique_cascade_smoke_name
export B_EVAL_REF=15f0e0246cc91443bd74b477ccee941432794ef6
sbatch a_work/slurm/cascade_smoke.slurm
```

快照需包含 `run_replay.py`、`run_asr.py`、`eval_with_b.py`、`turntaking/`、
`eval_judge.slurm` 和记录文件哈希的 `manifest.json`。输入需含 `traces_debug.jsonl`、
`gold_debug.jsonl`、选中问题的 `question_audio/index.jsonl` 及 WAV。
输入、代码和模型文件的路径与哈希写入快照清单；不要编辑已经提交的快照。

作业先运行 ASR，退出 ASR 进程释放 GPU，再启动 Qwen3-14B 和 Qwen3-4B LoRA judge。
拆题和回答措辞使用 14B。Piper 在独立 TTS 环境的 CPU 上合成。
包括 4 个规则基线，以及 Oracle / LoRA gold 单元 / LoRA 模型拆题的串行和并发版本，
合计 10 个策略配置、60 个 policy runs。结束后自动调用固定版本的 B evaluator。

校园集群的现有依赖（可通过环境变量覆盖）：

| 资源 | 路径 |
|---|---|
| vLLM / Whisper Python | `/projects/illinois/eng/cs/dilek/xzhu81/envs/vllm/bin/python` |
| Piper Python | `/projects/illinois/eng/cs/dilek/xzhu81/envs/tts/bin/python` |
| Piper voice | `/projects/illinois/eng/cs/dilek/xzhu81/piper_voices/en_US-lessac-medium.onnx` |
| LoRA adapter | `a_work/results/lora/qwen3_4b_v1/best` |

验收时检查：

1. `asr.jsonl` 有 2 条有效转写，记录 WER 与延迟；错误转写同样保留。
2. `trace_metrics.jsonl` 有 60 条记录，`run_config.json` 明确启用了 ASR 和 Piper。
3. `audio/index.jsonl` 中音频长度与 WAV 一致；抽听数字、日期及专有名词。
4. B 评分的 `validation_issues.jsonl` 为空，缺失运行、未知映射和错误没有被隐去。
5. 所有结果仍标为模拟 / 估计时间；成功只证明链路跑通，不证明实时性能或策略优势。

## 时间口径与限制

- ASR 延迟会推迟依赖问题文本的工作；证据日程仍来自固定 trace。
  这不模拟真实检索如何受转写错误影响。
- Piper 的整段音频长度是实测的，声明在音频里的位置仍由音素比例估计，没有强制对齐。
- 并发版通过模拟时钟重叠判断、生成和播放；没有实测共享 GPU 的竞争和在线调度。
- 合成问题比真实录音容易。C 已共享早期**回答**音频；那并不是可直接替代本目录的用户问题录音。
- 无 ASR 的 gold 单元对照和使用 ASR 的模型拆题版本具有不同信息条件；Oracle 是上界。
- 不启用 `--allow-tape-misses` 来制造可报告结果；缺少调用记录的回放应失败。

smoke 通过后，再在同型号 GPU、相同输入和相同评估规则下做 text/rate、text/Piper、ASR/Piper
对照，并补充音频对齐与真实调度测量。v7 两轮文字回放已完成，没有启用真实语音；
作业及来源见 `lora_judge.md`。仍有两个 judge 作业排队，其完整运行参数待核。
