# 答案单元规范（Unit Schema）v0.1 草稿

状态：草稿，待组内讨论后定稿。与接口 v1（`b_work/step1/schema.md`、`labeling_guide.md`）配套使用，字段名沿用 v1。

## 1. 什么是答案单元

答案单元（unit）是回答一个问题所需的**最小信息块**，满足三个条件：

1. 能用一句话单独说出来（例如"这部电影的导演是 Fernando Di Leo"）；
2. 能被一条或几条证据句直接支持；
3. 要么是用户直接问的，要么是得出答案必须经过的中间一步。

控制器在每个决策时刻判断每个单元有没有证据支持，再据此选择动作（第 6 节）。

## 2. 两种单元：控制器单元与 gold 单元

| | 控制器单元 | gold 单元 |
|---|---|---|
| 谁生成 | 控制器运行时根据**问题**生成（LLM 拆题） | 人工或脚本根据标准答案与 supporting facts 标注 |
| 是否含答案 | **不含**，只有描述 | 含 `expected_answer` 和 `support_sets` |
| 用途 | 决策 | 评估（Unsupported Claim Rate、TTFGI、TTCA） |
| 字段 | `unit_id`、`description`、`necessary`、`depends_on` | 再加 `expected_answer`、`support_sets` |

两者按同一套拆法（第 3 节）生成，但**相互独立**：评估时 B 组把回答里的声明独立映射到 gold 单元，不依赖控制器单元的编号。Oracle judge 是唯一可以直接使用 gold 单元的控制器（v1 第 4 节的单独输入路径）。

## 3. 拆法：按题型

### 3.1 单一答案（SimpleQA 类）

一个单元，`necessary: true`。

> "Which U.S. president was the last one to be born in the 18th century?"
> - u1：最后一位生于 18 世纪的美国总统 — necessary

### 3.2 桥接 / 组合 / 推理（bridge、compositional、inference）

每一跳一个单元。中间一跳 `necessary: false`，最后一跳 `necessary: true` 且 `depends_on` 中间一跳。

> "Where was the director of film Being Twenty born?"
> - u1：Being Twenty 的导演 — optional
> - u2：{u1} 的出生地 — necessary，depends_on [u1]

- 中间一跳设为 optional：用户没有直接问它，最终答案里可以不说。这与 HotpotQA / 2Wiki 的标准答案一致（只含最终实体），也不会因为 baseline 没提中间实体而判它不完整。
- 但它是**有用的部分答案**：在最后一跳的证据到达之前，说出"导演是 Fernando Di Leo，出生地还在查"就是 Partial Answer。说出 optional 单元计入 TTFGI（见 3.6 "necessary 与有用信息"）。
- `depends_on` 保证：中间一跳没有证据时，最后一跳不能算有证据（即使某句证据碰巧提到了出生地）。因此中间一跳说不说只影响完整性，不影响有没有依据。
- 例外：问题明确问了中间一跳（"Who directed Being Twenty, and where was he born?"），按多部分题处理，两个单元都是 necessary。

### 3.3 比较（comparison）

每个被比较对象的事实各一个单元（optional），再加一个**结论单元**（necessary），结论依赖所有事实单元。

> "Who was born later, Mark Gurr or William Eythe?"
> - u1：Mark Gurr 的出生日期 — optional
> - u2：William Eythe 的出生日期 — optional
> - u3：谁出生得更晚 — necessary，depends_on [u1, u2]

- 只有一边的事实有证据时，可以说这一边（Partial Answer），**不能**说结论。
- 是非题（"Are X and Y both …?"）同样处理，结论单元是"是 / 否"。

### 3.4 桥接比较（bridge_comparison）

先对每个对象做桥接，再比较。

> "Which film has the director who died later, Hotel Paradis or Devil's Doorway?"
> - u1：Hotel Paradis 的导演 — optional
> - u2：{u1} 的去世日期 — optional，depends_on [u1]
> - u3：Devil's Doorway 的导演 — optional
> - u4：{u3} 的去世日期 — optional，depends_on [u3]
> - u5：哪部电影的导演去世更晚 — necessary，depends_on [u2, u4]

### 3.5 多部分（multipart）

用户问了几件事就拆几个单元，全部 necessary，互不依赖。

> "On what date did Apollo 11 launch, and on what date did it splash down on Earth?"
> - u1：发射日期 — necessary
> - u2：溅落日期 — necessary

### 3.6 通用规则

- **粒度**：一个单元对应一个事实，通常就是一条证据句能支持的内容。不要把两个事实合成一个单元（例如"导演和他的出生地"）。
- **描述**：用名词短语或问句写清楚要找什么。控制器单元在拆题时还不知道桥接实体，用 `{u1}` 这样的占位符指代前一跳的结果。
- **依赖**：`depends_on` 只能指向同一题内的单元，不能有环。
- **数量**：一般 1–5 个。超过 5 个说明拆得太细，或者问题本身需要拆成多轮。
- **necessary 与有用信息**：`necessary` 只决定"回答是否完整"（TTCA、最终正确率）；**所有单元**（包括 optional）说出时都算"有依据的有用信息"（TTFGI）。只有用户真正问到的内容才设为 necessary。

## 4. 字段

```json
{
  "unit_id": "u2",
  "description": "birthplace of {u1}",
  "necessary": true,
  "depends_on": ["u1"]
}
```

gold 单元额外包含（v1 第 4 节）：

```json
{
  "expected_answer": "San Ferdinando di Puglia",
  "support_sets": [["e2"]]
}
```

- `support_sets`：外层是"或"，内层是"且"。`[["e1", "e2"], ["e5"]]` 表示 e1 和 e2 同时可见，或 e5 可见，都算有证据。
- gold 单元的 `support_sets` 只列**直接**支持本单元的证据；依赖链上的证据由 `depends_on` 体现，不重复列。

## 5. 三种标签的判定标准

judge 在时刻 t 只看 `visible_time_s <= t` 的证据，对每个单元给出一个标签。被判断的对象是"单元 + 候选值"，例如"u1 = Fernando Di Leo"。

| 标签 | 判定标准 |
|---|---|
| `SUPPORTED` | 当前可见证据**明确写出**这个候选值；引用的证据 ID 都可见；`depends_on` 中的单元都是 SUPPORTED |
| `UNRESOLVED` | 证据不足，或依赖的单元还没有证据。没有证据不等于矛盾 |
| `CONTRADICTED` | 当前可见证据明确与候选值冲突 |

细则：

1. **只认明确陈述，不认推断。** "Being Twenty is an Italian film directed by Fernando Di Leo" 不支持"Di Leo 出生在意大利"。（MoshiRAG 实验里模型正是这样越界的。）
2. **结论单元允许确定性的比较。** u1、u2 都 SUPPORTED 时，比较两个日期得出 u3 算 SUPPORTED，引用 u1、u2 的证据。
3. **候选值从哪来。** 控制器单元没有预设答案，judge 从可见证据中抽取候选值并给出引用；没有可抽取的值就是 UNRESOLVED。候选值也可以是 agent 已经说出口的值：后来的证据与之冲突时标 CONTRADICTED，供控制器决定是否更正。
4. **引用必须指向已可见的证据。** 引用检查只确认证据 ID 存在且可见，不代表语义上一定支持；语义支持由 judge 判断，评估时由 B 组用 gold 独立核对。引用写证据编号（e1），不写单元编号；结论单元引用它所依赖单元的证据。
5. **定义性介绍中未列出的属性视为否定（by_omission）。** 这是细则 1 的唯一例外，与 HotpotQA / 2Wiki 标准答案的隐含假设一致：
   - 适用条件：证据是对该实体的定义性介绍（通常是百科首句，如 "Jon Turteltaub is an American film director and producer."），且被问的属性属于介绍会列出的类别（职业、国籍、所属类别等）。
   - 此时介绍里没有列出的属性可以判为"不是"，标签为 SUPPORTED，同时标记 `by_omission: true`。例如上句支持"Turteltaub 不是电视编剧"。
   - 不适用：需要常识或外部知识才能得出的否定（例如证据只说机场在明尼苏达州，推出"不在欧洲"）；非定义性的句子（只提到某个事件或作品的句子）。
   - 评估时 `by_omission` 的判断单独统计，便于区分"明确写出"和"按省略推出"。judge、gold 标注和 B 组的 Unsupported Claim 评估必须使用同一规则。
6. **同一单元同时有支持和冲突的证据**：按 v1 标注指南，先标记为需要人工复核，冲突处理规则定下来之前不进入自动评分和 SFT 数据。

## 6. 从单元标签到动作

| 状态 | 条件 | 默认动作 |
|---|---|---|
| Insufficient | 没有任何单元 SUPPORTED | Wait / Backchannel / Progress（按时间） |
| Partially Sufficient | 有单元 SUPPORTED 且尚未说过，但 necessary 单元没有全部 SUPPORTED | Partial Answer：只说新近 SUPPORTED 的单元，并说明其余还在查 |
| Fully Sufficient | 所有 necessary 单元 SUPPORTED | Final Answer |

- Partial Answer 只能说 SUPPORTED 的单元；比较题在结论单元 SUPPORTED 之前不能说结论。
- 检索已经结束但仍不 Fully Sufficient：说出已 SUPPORTED 的部分，并明确说明其余没有找到（这条待组内确认）。

## 7. 待讨论

1. ~~桥接题的中间一跳设为 optional 还是 necessary~~ 已定：optional，但计入 TTFGI（3.2、3.6）。需要 B 组在评估框架中按此计算 TTFGI。
1a. ~~证据没提到的属性能否当作否定~~ 已定：仅限定义性介绍，标记 by_omission（5.5）。需要 B 组在 gold 标注和评估中采用同一规则。
1b. 需要常识才能得出的否定（例如"不在欧洲"）怎么处理：未定。目前按细则 1 判为 UNRESOLVED。
2. 结论单元的确定性比较是否需要 judge 之外单独实现（例如日期比较写成规则）。
3. 检索结束仍不充分时的动作（第 6 节最后一条）。
4. 冲突证据的处理规则（v1 待定项）。
5. 控制器拆题用哪个 LLM、拆题结果与 gold 单元不一致时如何统计。

## 附：完整示例（gold 单元）

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "sample_id": "2wikimultihopqa_39751c8a08d811ebbd9aac1f6bf848b6",
  "units": [
    {"unit_id": "u1", "description": "birth date of Mark Gurr", "necessary": false,
     "expected_answer": "February 18, 1966", "depends_on": [], "support_sets": [["e1"]]},
    {"unit_id": "u2", "description": "birth date of William Eythe", "necessary": false,
     "expected_answer": "April 7, 1918", "depends_on": [], "support_sets": [["e2"]]},
    {"unit_id": "u3", "description": "who was born later", "necessary": true,
     "expected_answer": "Mark Gurr", "depends_on": ["u1", "u2"], "support_sets": [[]]}
  ]
}
```

`u3` 的 `support_sets` 为 `[[]]`：它不需要额外的证据句，只要依赖的 u1、u2 都 SUPPORTED 就成立。
