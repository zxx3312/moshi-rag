# 31 道问题题替换审计（2026-11-03）

本轮从最终 gold 移除 31 道明确存在实体错链、证据不足、主观比较或不当省略推断的题，并使用现有候选替换。所有替换题均为 `reviewed`，necessary unit 在全部证据到齐时可达；构建器、SFT schema、引用可见性和 A 组代码交叉检查均通过。

## 替换题审核结果

| replacement sample_id | split / source type | 逻辑依据 |
|---|---|---|
| `2wikimultihopqa_b3a5431b08cc11ebbd93ac1f6bf848b6` | train / bridge_comparison | 两位导演及其 American 国籍均直接陈述 |
| `2wikimultihopqa_ef3a400a087811ebbd67ac1f6bf848b6` | train / bridge_comparison | 两位导演及其 American 国籍均直接陈述 |
| `2wikimultihopqa_d2e0be5a08b611ebbd88ac1f6bf848b6` | train / bridge_comparison | 导演身份和死亡日期完整，2002 晚于 1961 |
| `2wikimultihopqa_9d785ec3097d11ebbdb0ac1f6bf848b6` | train / comparison | 两个村庄均明确位于 Iran |
| `2wikimultihopqa_fc76b898099011ebbdb0ac1f6bf848b6` | train / comparison | 两个村庄均明确位于 Iran |
| `2wikimultihopqa_0ae4bb72086111ebbd5dac1f6bf848b6` | train / comparison | 两个死亡日期直接陈述，可确定先后 |
| `2wikimultihopqa_b902985208d411ebbd97ac1f6bf848b6` | train / comparison | Finnish 与 Norwegian 直接陈述 |
| `2wikimultihopqa_794cefac08cb11ebbd92ac1f6bf848b6` | train / comparison | 两个出生日期直接陈述，可确定先后 |
| `2wikimultihopqa_254e9ee20bdb11eba7f7acde48001122` | train / compositional | 电影导演和 Canadian 国籍直接陈述 |
| `2wikimultihopqa_461f74380bdc11eba7f7acde48001122` | train / compositional | 电影导演和 Istanbul 出生地直接陈述 |
| `2wikimultihopqa_920f21380bda11eba7f7acde48001122` | train / compositional | 杂志出版方和该组织创办人直接陈述 |
| `2wikimultihopqa_cbcd85f00bd911eba7f7acde48001122` | train / compositional | Bessie Smith 的演唱和 American 国籍直接陈述 |
| `2wikimultihopqa_f01f570a0baf11ebab90acde48001122` | train / inference | 父亲和父亲的父亲两跳均直接陈述 |
| `2wikimultihopqa_16a707100bb011ebab90acde48001122` | train / inference | 父女和父子两跳均直接陈述 |
| `2wikimultihopqa_7b9cef6a0bdb11eba7f7acde48001122` | dev / compositional | 电影导演和 heart failure 死因直接陈述 |
| `2wikimultihopqa_008905100baf11ebab90acde48001122` | dev / inference | 配偶和配偶父亲两跳均直接陈述 |
| `2wikimultihopqa_e5f6937a0bae11ebab90acde48001122` | dev / inference | 母子和母亲的父亲两跳均直接陈述 |
| `hotpotqa_5a79188455429974737f7984` | train / bridge | 另一位作曲者和其出生日期直接陈述 |
| `hotpotqa_5add1b765542990d50227de3` | train / bridge | Nero Decree 的签发者及任总理年份直接陈述 |
| `hotpotqa_5a8b85f355429971feec4731` | train / bridge | 翻拍关系与 Jean-Baptiste Andrea 的编导关系直接陈述 |
| `hotpotqa_5ae752255542995703ce8be5` | train / bridge | 河流路线和 Downtown Louisville 北界直接陈述 |
| `hotpotqa_5ae340c45542992f92d82273` | train / bridge | 巡演结束地点/日期和 `over $150 million` 直接陈述 |
| `hotpotqa_5abc47d055429959677d6a70` | train / comparison | 两人使用电影媒介均有直接证据 |
| `hotpotqa_5ae3f3cb5542995ad6573cd9` | train / comparison | Apache 明确为 petroleum 公司；Alexion 的定义类别支持 `by_omission` |
| `hotpotqa_5a733a2e5542994cef4bc4df` | train / comparison | Paul 明确为 NYU 教授；Kazarian 的职业定义支持 `by_omission` |
| `hotpotqa_5a752d375542996c70cfaea4` | train / comparison | 两个实体均明确为 dog breed |
| `hotpotqa_5a908d1f55429916514e74f1` | train / comparison | 两人均明确为 American |
| `hotpotqa_5adf9e59554299025d62a2e9` | train / comparison | 1986 成团与 1979 出生可确定当时年龄为 7 岁 |
| `hotpotqa_5ab33cec554299753aec595c` | dev / bridge | 第三支单曲所属专辑和专辑发布日期直接陈述 |
| `hotpotqa_5a77a8365542995d83181250` | dev / comparison | 两个音乐组织均明确为 band |
| `hotpotqa_5a7f359f55429930675136a9` | dev / comparison | Sidney 完整满足国籍/职业条件；Randal 的定义句支持 `by_omission` |

## 未采用的同类候选

为避免用新争议替换旧争议，以下 Hotpot comparison/train 候选没有进入 gold：

- `hotpotqa_5a85b04f…`：只知道 Irwin Winkler 有 50 部作品，Jim Mendiola 的完整数量未知。
- `hotpotqa_5a7a6e33…`：The American Conservative 的文本没有显式给出所属国家，且“both”题不能用问题预设。
- `hotpotqa_5a7328d1…`：文档没有给出 Primus 的真正最近专辑日期，不能与 Built to Spill 做完整比较。

因此使用 3 道证据完整的 2Wiki comparison/train 候选补位。train/dev 和 comparison 数量保持不变；来源分布从 150/150 变为 153 2Wiki / 147 Hotpot。

## 构建结果

- Gold：300 题，243 train / 57 dev；31 道旧题全部移除，31 道替换全部入选。
- SFT：1,991 train examples / 486 dev examples。
- 必答 unit 全证据不可达：0 题。原两道规则边界题已按后续人工裁决修正。
- `unknown` 占位值：0。
- A 组交叉检查不一致：0。
- Gold SHA256：`d59ee38833a591899336c7e2a0badb13a8eb2677689f021eadcbc141b20e03c3`。
- SFT train SHA256：`e8ea558117c8ff87ce1f59f3f59b734e75b44e14bbca6c5b97dfcdcdf4d46994`。
- SFT dev SHA256：`57a04193841add510ad7835705e6c52d0661491f7dd189e84ba0dc52e0cadb27`。
