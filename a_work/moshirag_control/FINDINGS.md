# MoshiRAG 可控性实验：结果

2026-10-22，H100 80GB，bf16，种子 42424242，每个条件 1 次。
14 题：12 道 SimpleQA 难题（证据在问题结束后 8 s 到达）+ 2 道两段证据题（3 s、8 s）。
原始结果在 `results/full_v1/`（作业 11726985）和 `results/full_v2/`（作业 11727274），已 gitignore。
下表为人工阅读 `analysis/review.md` 后的判读，待组内第二人复核。
可复现性：两轮中的 `free` 条件 14/14 逐字相同，条件之间的差异来自控制而非随机性。

## 结论

不训练模型、只在推理时控制文字流、音频流和证据注入时间，可以在 MoshiRAG 上实现
Wait、Backchannel/Progress、Final Answer 三类动作。Partial Answer 在 v2 的做法下不可行（0/2），
"单元感知注入"（ours_v3）也没有改善，见文末。

| 动作 | 实现方式 | 结果 |
|---|---|---|
| Wait | 文字强制 PAD + 音频 token 替换为静音编码（`wait_av`） | 14/14 文字和声音都沉默（v1 只控制文字时，7/14 仍在出声） |
| Backchannel / Progress | 回放模型自己说过的片段（`progress_clip`） | 14/14 说出片段，证据前 0 条事实声明 |
| Final Answer | 证据到齐后回放 "Oh," 再放开（release cue） | 14/14 立即开口；严格匹配 10/14 答对，计入拼写近似 13/14 |
| Partial Answer | 第一段证据到达后让它说一句再按住（`ours_v2`） | 0/2：只拿到第一段证据，仍然回答整个问题（Caroline 把父亲说成祖父，Alpha 编造发布年份） |

## 各条件结果

| 轮次 | 条件 | 证据到达前 | 证据到达后答对（严格 / 计入拼写近似） |
|---|---|---|---|
| v1 | free | 14/14 给出具体错误答案 | 0/14 |
| v1 | wait（只控制文字） | 文字沉默，声音 7/14 仍在说话 | 4/14 |
| v1 | progress（文字强制短语） | 文字有短语，声音不跟随 | 1/14 |
| v1 | notready（注入"还没查到"） | 12/14 说"还在查"，2/14 说错 | 0/14 |
| v2 | wait_av | 14/14 静音 | 8/14；4/14 放开后不开口 |
| v2 | wait_av_kick | 14/14 静音 | 10/14 / 13/14；14/14 开口 |
| v2 | progress_clip | 14/14 说出片段，无事实声明 | 10/14 / 13/14；Caroline 只答出父亲 |
| v2 | progress_inj | 同 v1 notready | 3/14：多数改说 "should I keep looking?" |
| v2 | ours_v2 | 说出片段 | 0/2 部分回答正确 |

"拼写近似"指模型文本流拼写与 gold 不同但明显指同一实体：Corsans/Couranc（Coursan）、Ji Chun-ho（Ji Chung-ho）、Katha（Kathua）。是否算对需要听录音确认。

## 实现要点

1. 文字和音频是两条流。只改文字既不能让模型出声，也不能让它闭嘴；必须在 `on_audio_hook` 里同时替换音频 token。替换后的 token 也进入模型自己的历史，所以它"记得"自己是安静的。
2. 说话类动作用模型自己的录音片段（`configs/clips/`，由 `make_clips.py` 从 full_v1 剪出），文字 token 和音频编码逐帧回放。
3. 长时间沉默后模型不会主动开口（`wait_av` 4/14 不开口），放开时需要一个短的开场片段。
4. 用证据注入实现 Progress 会污染后续回答：注入"还没查到"后，真证据到达时多数仍说找不到。

## 对项目的含义

- 目标是 5 个动作在同一环境中评估。若 ours_v3 能实现 Partial Answer，端到端实验在 MoshiRAG 上运行全部 5 个动作；
  若不能，按 proposal 预案整体退回级联方案（ASR → LLM → TTS），所有策略在级联环境中比较，MoshiRAG 作为外部系统对照。
- release cue 固定为 "Oh, that's a good question."一类开场，自然度需要人评确认（静默数秒后再说 "that's a good question" 可能显得突兀）。

## 局限

- 每个条件 1 个种子；正确率需要多种子重复。
- SimpleQA 证据就是答案原句，"答对"主要反映模型是否开口并使用了证据。
- 自动统计用字符串匹配，漏判拼写差异，也检测不到错误答案；以本文件人工判读为准。
- 片段的音频编码是从录音重新编码得到，与原始生成的编码不完全相同；音质需听录音确认。

## Partial Answer 的单元感知注入（partial_v3，作业 11729084）

控制器知道每个答案单元是否已有证据支持，因此在部分证据到达时，注入的参考文本除证据外还写明缺失的部分
（单元的 `pending` 句，例如 "Where Fernando Di Leo was born is still being searched."）；最后一次注入追加
"The search is complete."，以抵消前面的缺失说明（progress_inj 显示"未就绪"注入会污染后续回答）。

数据：`configs/multipart_debug.json`，从 B 组 20 道 debug 题中选出 16 道可拆成两段证据的题
（bridge 5、comparison 5、bridge_comparison 2、NASA 多部分 4），加上 Caroline、Alpha，共 18 题；
证据句做了最小改写以便独立成句，来源记录在每条证据的 `source` 中。pending 句为手写，真实系统中应由 controller 根据单元描述生成。
条件：free、wait_av_kick、progress_clip、ours_v2、ours_v3，共 90 次。

### 结果（人工判读 3–8 s 之间的话，18 题）

| 条件 | 好的部分回答（只说第一段证据支持的内容） | 只说进度、无事实 | 越界（对缺失部分下结论或说错） |
|---|---|---|---|
| ours_v2（只注入证据） | 9/18 | 2/18 | 7/18 |
| ours_v3（证据 + 缺失说明） | 6/18 | 4/18 | 8/18 |

- 缺失说明没有让模型守住边界：它有时说对了缺失说明（Brian Part："Brian Part is from the United States, but I don't know yet where John Mosca is from"），
  有时把缺失的对象弄反（Alpha："Alpha's leader is currently unknown"），有时仍然直接给出结论（Gordonia："aren't in the same family"）。
- 缺失说明会延续到最后：最后一次注入写了 "The search is complete."，仍有 4 题在证据齐全后说"还在找"（Caroline、Nightmare、Margaret、Theal）。
- 证据齐全后多跳题本身答得不好：progress_clip 在两段证据都到达后，约 6–8/18 给出完整正确答案，常见问题是只复述其中一句证据或比较结论说反。
  这说明 MoshiRAG 用注入证据做两步推理的能力有限，与控制方式无关。
- 实现问题：模型在 8 s 时可能还在说话，此时回放 "Oh," 会打断句子（如 "launched on July sixteenth, nineteen | Oh, nineteen sixty-nine"）。
  release cue 应只在模型安静时回放。

### 结论

免训练控制能决定 MoshiRAG 什么时候说，但不能决定它说哪一部分。Partial Answer 在 MoshiRAG 上不可靠（两种做法越界率都约 40%）。
按既定预案，5 个动作需要在同一环境中评估，因此端到端实验应改用级联方案（ASR → LLM → TTS）；
MoshiRAG 作为外部系统对照，本实验的 Wait / Progress / Final Answer 控制结果作为"端到端模型可控性"的分析结论写入报告。
单种子；待组内确认后执行。
