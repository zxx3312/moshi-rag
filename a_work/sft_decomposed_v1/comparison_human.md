# 拆题器与人工单元对比（AI 辅助审阅）

原则：**新旧单元都合理时，保留拆题器拆法，人工监督向新单元对齐。** 不以旧 gold 的粒度、顺序或取值形式作为唯一正确答案。

已逐题对比 300 道 SFT 题（train 243 / dev 57）的生成单元与人工单元；对疑似问题结合原始证据核查。以下为辅助审阅建议，尚未由人工验收。

| 审阅结论 | train | dev | 合计 |
|---|---:|---:|---:|
| 需改：生成拆解 | 28 | 6 | 34 |
| 保留新拆法｜重标人工标签 | 46 | 11 | 57 |
| 待确认：语义或标签口径 | 3 | 3 | 6 |
| 未发现需单独修改的问题 | 166 | 37 | 203 |

## 如何使用标注

- **保留新拆法**：保留生成的描述、粒度和合理的依赖关系，重建 expected_answer、support_sets 以及各证据时刻的标签。合并单元常需联合多跳证据；不能只复制最后一跳证据，也不能按相同 u1/u2 编号机械对应。
- **需改生成拆解**：仅修正实际错误。题型元数据错误与实体、关系、答案目标错误分别在逐题建议中说明。若后续人工修正训练单元，还需检查运行时拆题器能否稳定生成同类拆法。
- **待确认**：先澄清问题含义或允许的答案口径，再构建监督。
- **未标记**：本轮未发现需单独修改的问题，不等于可直接复制旧 SFT 标签；所有新单元仍应按新输入重新生成和检查快照。

本轮仅添加 Markdown 标记和审阅 JSON，未修改原始生成 JSON、B 组 gold、训练集或验证集，未生成最终训练标签。未使用预留评测集。

机械差异统计：题型不同 56 题，结构不同 52 题。这些不是错误率；文字不同也不等于语义错误。

## 需改：生成拆解（34 题）

### [train #5 · 2wikimultihopqa_0ae4bb72086111ebbd5dac1f6bf848b6](train.md#human-review-2wikimultihopqa_0ae4bb72086111ebbd5dac1f6bf848b6)

**问题：** Who died first, Maude Fealy or Lars Gustafsson?

**差异：** 3 → 3 单元；comparison → bridge_comparison。

**原因：** 单元本身是两个已点名对象的事实加一个比较/共同属性结论，没有寻找未知中间实体的桥接步骤，但 question_type 被写成 bridge_comparison。

**建议：** 只将 question_type 改为 comparison，保留当前单元关系；这属于题型元数据错误，不应为凑题型增加桥接单元。

### [train #13 · 2wikimultihopqa_2547e59c089b11ebbd78ac1f6bf848b6](train.md#human-review-2wikimultihopqa_2547e59c089b11ebbd78ac1f6bf848b6)

**问题：** Who died later, Landgravine Sophie Of Hesse-Kassel or Juan Riba?

**差异：** 3 → 3 单元；comparison → bridge_comparison。

**原因：** 单元本身是两个已点名对象的事实加一个比较/共同属性结论，没有寻找未知中间实体的桥接步骤，但 question_type 被写成 bridge_comparison。

**建议：** 只将 question_type 改为 comparison，保留当前单元关系；这属于题型元数据错误，不应为凑题型增加桥接单元。

### [train #20 · 2wikimultihopqa_32e5e2840bb011ebab90acde48001122](train.md#human-review-2wikimultihopqa_32e5e2840bb011ebab90acde48001122)

**问题：** Who is the father of Grand Duchess Elizabeth Mikhailovna Of Russia?

**差异：** 2 → 2 单元；bridge → bridge。

**原因：** 新 u1 是母亲，u2 却写 father of {u1}，实际变成了外祖父；原题问本人父亲。这是关系错误，不是合理的粒度差异。

**建议：** 必须把 u2 的“father of {u1}（母亲的父亲）”改回 Elizabeth 本人的父亲。可以保留两单元并写清“father of Elizabeth, given {u1} as her mother”，也可以利用 d4s1 的直接父女证据改成单单元；关键是修正亲属关系，不是强制某种粒度。

### [train #39 · 2wikimultihopqa_5f7ce04c099111ebbdb0ac1f6bf848b6](train.md#human-review-2wikimultihopqa_5f7ce04c099111ebbdb0ac1f6bf848b6)

**问题：** Are Mar, Isfahan and Anjir Bazuiyeh both located in the same country?

**差异：** 3 → 4 单元；comparison → comparison。

**原因：** 把完整地名“Mar, Isfahan”中的行政区限定词当成另一个被比较对象，导致本应比较两个地点却生成三个事实单元。源文档标题与首句确认这是一个地点。

**建议：** 将“Mar, Isfahan”作为不可拆开的实体；恢复两个国家事实单元和一个必要比较结论，删除多余行政区单元并重建依赖。

### [train #43 · 2wikimultihopqa_6a80c1d408de11ebbd9eac1f6bf848b6](train.md#human-review-2wikimultihopqa_6a80c1d408de11ebbd9eac1f6bf848b6)

**问题：** Who died first, François-René Tranchefort or Ernst Ludwig Von Aster?

**差异：** 3 → 3 单元；comparison → bridge_comparison。

**原因：** 单元本身是两个已点名对象的事实加一个比较/共同属性结论，没有寻找未知中间实体的桥接步骤，但 question_type 被写成 bridge_comparison。

**建议：** 只将 question_type 改为 comparison，保留当前单元关系；这属于题型元数据错误，不应为凑题型增加桥接单元。

### [train #51 · 2wikimultihopqa_75141b5d086911ebbd5eac1f6bf848b6](train.md#human-review-2wikimultihopqa_75141b5d086911ebbd5eac1f6bf848b6)

**问题：** Do both Americanizing Shelley and Road Agent (1952 film) films have the directors from the same country?

**差异：** 5 → 5 单元；bridge_comparison → comparison。

**原因：** 已有完整的两条“导演→国籍”链和比较结论，5 个单元结构正确，但 question_type 被写成 comparison。

**建议：** 将 question_type 改为 bridge_comparison；u2/u4 建议明确为 nationality，避免 country of origin 被理解为出生地。

### [train #60 · 2wikimultihopqa_8b1a578708a211ebbd7aac1f6bf848b6](train.md#human-review-2wikimultihopqa_8b1a578708a211ebbd7aac1f6bf848b6)

**问题：** Who lived longer, Sergio Tofano or Diego Cisneros?

**差异：** 3 → 3 单元；comparison → comparison。

**原因：** 问的是寿命长短，当前事实单元只取死亡日期；死亡更晚不等于活得更久。

**建议：** u1/u2 改为各人的寿命或出生与死亡日期，结论比较寿命；复用旧 gold 的生卒日期证据，重新确认取值格式和派生标签。

### [train #65 · 2wikimultihopqa_9040c5ab097511ebbdb0ac1f6bf848b6](train.md#human-review-2wikimultihopqa_9040c5ab097511ebbdb0ac1f6bf848b6)

**问题：** Are Bol, Mazandaran and Kozmodemyansk, Perm Krai located in the same country?

**差异：** 3 → 4 单元；comparison → comparison。

**原因：** 把完整地名“Bol, Mazandaran”中的行政区限定词当成另一个被比较对象，导致本应比较两个地点却生成三个事实单元。源文档标题与首句确认这是一个地点。

**建议：** 将“Bol, Mazandaran”作为不可拆开的实体；恢复两个国家事实单元和一个必要比较结论，删除多余行政区单元并重建依赖。

### [train #79 · 2wikimultihopqa_b14d20df097211ebbdb0ac1f6bf848b6](train.md#human-review-2wikimultihopqa_b14d20df097211ebbdb0ac1f6bf848b6)

**问题：** Are both Marzian, Lorestan and Vella located in the same country?

**差异：** 3 → 4 单元；comparison → comparison。

**原因：** 把完整地名“Marzian, Lorestan”中的行政区限定词当成另一个被比较对象，导致本应比较两个地点却生成三个事实单元。源文档标题与首句确认这是一个地点。

**建议：** 将“Marzian, Lorestan”作为不可拆开的实体；恢复两个国家事实单元和一个必要比较结论，删除多余行政区单元并重建依赖。

### [train #130 · hotpotqa_5a736dc755429901807db04e](train.md#human-review-hotpotqa_5a736dc755429901807db04e)

**问题：** Out of the two members of Hi-Gate, which was voted the No. 1 DJ in the world in 1995?

**差异：** 2 → 3 单元；bridge → comparison。

**原因：** member 1/member 2 没有实体名称、来源单元或可解析的占位符，两个“成员”是谁没有定义。

**建议：** 先增加 Hi-Gate 成员识别单元，再选择其中在1995年获 No.1 DJ 的成员；采用旧 gold 的两阶段结构或定义清楚的候选集合，不能使用无绑定的 member 1/2。

### [train #137 · hotpotqa_5a7769ea55429966f1a36d2f](train.md#human-review-hotpotqa_5a7769ea55429966f1a36d2f)

**问题：** Who died first, Yuri Linnik or Georg Cantor?

**差异：** 3 → 3 单元；comparison → bridge_comparison。

**原因：** 单元本身是两个已点名对象的事实加一个比较/共同属性结论，没有寻找未知中间实体的桥接步骤，但 question_type 被写成 bridge_comparison。

**建议：** 只将 question_type 改为 comparison，保留当前单元关系；这属于题型元数据错误，不应为凑题型增加桥接单元。

### [train #139 · hotpotqa_5a78fb5955429970f5fffe09](train.md#human-review-hotpotqa_5a78fb5955429970f5fffe09)

**问题：** What festival celebrated by the people of Karnataka celebrates a philosopher who died in 1609?

**差异：** 2 → 2 单元；bridge → bridge。

**原因：** 必要单元变成了“节日所纪念且卒于1609年的哲学家”，会输出人物；原题要求节日名称。

**建议：** 恢复“卒于1609年的哲学家”非必要单元，再以“卡纳塔克邦纪念{u1}的节日”为 necessary 单元；对应 d10s0 与 d9s1。

### [train #151 · hotpotqa_5a7f66cb55429969796c1a32](train.md#human-review-hotpotqa_5a7f66cb55429969796c1a32)

**问题：** Between Cranium and Auf Achse, which game had more people involved in creating?

**差异：** 3 → 3 单元；comparison → bridge_comparison。

**原因：** 两个游戏均已点名，只需比较创作者人数，属于 comparison，当前却标成 bridge_comparison。人工值 2/1 统计的是文档明确列出的创作者/设计者人数。

**建议：** 题型改为 comparison；保留三单元，并明确人数口径为“证据明确列出的不同创作者/设计者人数”，不要把未列出的所有参与人员也计入。

### [train #165 · hotpotqa_5a8ad70d5542992d82986f94](train.md#human-review-hotpotqa_5a8ad70d5542992d82986f94)

**问题：** American producer K.E. on the Track worked with Fetty Wap on a song named after which shoemaker?

**差异：** 2 → 2 单元；bridge → bridge。

**原因：** 新 u1 的 song produced by K.E. on the Track and Fetty Wap 将两人都写成制作人。d4s0/d4s1 只支持 Fetty Wap 演唱、K.E. on the Track 制作。

**建议：** u1 改为“song by Fetty Wap produced by K.E. on the Track”；u2 保持该歌曲以哪位鞋匠命名。不要把演唱者和制作人角色混同。

### [train #181 · hotpotqa_5ab4da805542996a3a969fd8](train.md#human-review-hotpotqa_5ab4da805542996a3a969fd8)

**问题：** Until which year did this Polish professional boxer who lost to Joe Smith Jr. in 2016 in a knockout victory hold the IBO light heavyweight title?

**差异：** 2 → 2 单元；bridge → bridge。

**原因：** 新 u2 丢掉了 until，变成泛指持有头衔的年份；证据同时包含2012和2013，可能误取开始年份或整个区间。

**建议：** 明确为“year until which {u1} held the IBO light heavyweight title / end year”，对应2013；保留旧证据 d9s0。

### [train #183 · hotpotqa_5ab679e1554299110f219a16](train.md#human-review-hotpotqa_5ab679e1554299110f219a16)

**问题：** Graham Gold is a DJ who broadcasts live Friday nights on a radio station that also broadcasts on what around the UK?

**差异：** 2 → 2 单元；bridge → bridge。

**原因：** 新 u2 问 what the radio station broadcasts，易被理解为节目内容；原题问 broadcasts on what，即播出平台/制式。

**建议：** 改为“broadcast platform/system on which {u1} also broadcasts around the UK”；目标应是 DAB Digital Radio 类平台，不是节目名。

### [train #188 · hotpotqa_5ab95b28554299743d22eb09](train.md#human-review-hotpotqa_5ab95b28554299743d22eb09)

**问题：** Jack and Jill and Forbes are both what?

**差异：** 3 → 4 单元；comparison → comparison。

**原因：** “Jack and Jill”是一本杂志的完整名称，不是 Jack 和 Jill 两个对象；当前拆成了三个对象。

**建议：** 以 Jack and Jill 与 Forbes 为两个实体，各建一个类别单元，结论依赖二者。

### [train #196 · hotpotqa_5abdc7fb55429965af743e3a](train.md#human-review-hotpotqa_5abdc7fb55429965af743e3a)

**问题：** John William Maule Ramsay served as Secretary for Scotland in the administration of a British Liberal statesman and Britian's oldest what?

**差异：** 2 → 2 单元；bridge → bridge。

**原因：** “Britain's oldest {u1}”没有说明要找的属性，{u1} 已是人物；原题要的是他作为最年长任职者所担任的职务。

**建议：** u2 改成“office of which {u1} was Britain's oldest holder”，保持 necessary；答案类型为职位（Prime Minister），不是人物或年龄。

### [train #213 · hotpotqa_5ade07a95542997dc790712e](train.md#human-review-hotpotqa_5ade07a95542997dc790712e)

**问题：** Baleine, Nova Scotia is best known as the landing site for a pilot born in which year ?

**差异：** 2 → 2 单元；bridge → bridge。

**原因：** u1 的 pilot associated with Baleine 太宽泛，丢失了“该地因其降落地点而著名”的识别条件。

**建议：** u1 明确为“pilot for whom Baleine is best known as the landing site”；u2 保留其出生年，使用 d2s1 的限定关系识别人物。

### [train #214 · hotpotqa_5ade188e5542990dbb2f7f52](train.md#human-review-hotpotqa_5ade188e5542990dbb2f7f52)

**问题：** Who was the italian actor and screen writer from the 1950s, Marco Ferreri or Gordon Wiles?

**差异：** 3 → 3 单元；comparison → comparison。

**原因：** 事实单元只检查 Italian 和 worked in the 1950s，漏掉 actor 与 screenwriter；结论却需要这两个职业条件。

**建议：** u1/u2 都应检查完整谓词“Italian actor and screenwriter from the 1950s”，再选择候选，不能只凭国籍和活跃年代。

### [train #215 · hotpotqa_5ade1b7755429975fa854e55](train.md#human-review-hotpotqa_5ade1b7755429975fa854e55)

**问题：** Which band was founded in the 21st century, Foo Fighters or Goon Moon?

**差异：** 3 → 3 单元；comparison → comparison。

**原因：** 问题按“是否成立于21世纪”选候选，模型却要求精确 founding year。Goon Moon 的给定文本只写2005年发行作品，并未给成立年份；不能把发行年当成立年。

**建议：** 按 A 的候选属性选择规则改成两个 whether ... founded in the 21st century 单元；保留旧 gold 的预设/排除路径并重新验证，不能给 Goon Moon 编造成立年份。

### [train #216 · hotpotqa_5ade9914554299728e26c759](train.md#human-review-hotpotqa_5ade9914554299728e26c759)

**问题：**  Burying the Ex is a comedy horror film starring an American actress known for playing Alice Cullen in the film adaptations of what novels?

**差异：** 2 → 2 单元；bridge → bridge。

**原因：** u1 只写 Burying the Ex 的美国女演员，漏掉“以 Alice Cullen 一角著称”的辨识条件；演员表 d5s1 含多名候选。

**建议：** u1 补上 known for playing Alice Cullen，或显式先保留演员候选再筛选；u2 再问该角色所在电影改编的小说系列。

### [train #219 · hotpotqa_5adf9e59554299025d62a2e9](train.md#human-review-hotpotqa_5adf9e59554299025d62a2e9)

**问题：** Was the Pixies a rock band when Pierre Bouvier was a child?

**差异：** 3 → 3 单元；comparison → bridge_comparison。

**原因：** 题型误写为 bridge_comparison；此外新 u1 是出生日期、u2 是乐队成立年份，与旧 gold 的 u1/u2 正好相反。

**建议：** 题型改为 comparison。若保留新顺序，必须交换旧事实单元对应的答案、证据和标签：新u1←旧u2，新u2←旧u1；结论仍依赖两者。

### [train #233 · hotpotqa_5ae340c45542992f92d82273](train.md#human-review-hotpotqa_5ae340c45542992f92d82273)

**问题：** The tour that Taylor Swift completed in Singapore on June 12, 2014 grossed how much?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 把“在新加坡于某日结束的整场巡演”改成了 Singapore tour/on that date 的收入，既合并巡演识别步骤，又可能误解为单场收入。

**建议：** 可以保留 single，只将描述明确为“total gross revenue of the Taylor Swift tour that concluded in Singapore on June 12, 2014”。用巡演识别和总收入证据联合支持；不要求恢复旧两单元，不把总收入变成新加坡单场收入。

### [train #236 · hotpotqa_5ae533495542992663a4f159](train.md#human-review-hotpotqa_5ae533495542992663a4f159)

**问题：** Barbara Linares is a model for what parent company of Aerie?

**差异：** 2 → 2 单元；bridge → bridge。

**原因：** 新必要单元“model Barbara Linares for {u1}”不清楚是在问人、真假还是公司，不能保证输出原题要求的母公司名称；这是目标表述问题，不是单元数量问题。

**建议：** 保留新查找方向也可以，但必要单元必须明确问“parent company of Aerie for which Barbara Linares models, given {u1}”。也可合并为一个完整公司查询；不强制恢复旧“先识别Aerie”的步骤。

### [train #238 · hotpotqa_5ae5397d55429960a22e0276](train.md#human-review-hotpotqa_5ae5397d55429960a22e0276)

**问题：** Eliot Teltscher and Anastasia Myskina both played what sport?

**差异：** 3 → 3 单元；comparison → bridge_comparison。

**原因：** 单元本身是两个已点名对象的事实加一个比较/共同属性结论，没有寻找未知中间实体的桥接步骤，但 question_type 被写成 bridge_comparison。

**建议：** 只将 question_type 改为 comparison，保留当前单元关系；这属于题型元数据错误，不应为凑题型增加桥接单元。

### [train #241 · hotpotqa_5ae71f455542996d980e7ca9](train.md#human-review-hotpotqa_5ae71f455542996d980e7ca9)

**问题：** Soul Axiom included a port for the Microsoft game console announced in what month?

**差异：** 2 → 2 单元；bridge → bridge。

**原因：** u1 写“console included in Soul Axiom”，容易指游戏中的设备；原题说游戏移植到的微软游戏平台。

**建议：** 改为“Microsoft game console for which Soul Axiom included a port”；u2 询问 {u1} 的公布月份，并保留证据中的年份（May 2013）。

### [train #242 · hotpotqa_5ae74ae95542997b22f6a688](train.md#human-review-hotpotqa_5ae74ae95542997b22f6a688)

**问题：** Rani Velu Nachiyar was a famous queen before which queen that was a leading figure of the Indian Rebellion of 1857?

**差异：** 2 → 2 单元；bridge → bridge。

**原因：** 最终单元是陈述句“Rani Velu Nachiyar was ... before {u1}”，没有明确要求输出那位女王，容易变成真假验证。

**建议：** 将必要单元明确写成“queen who was a leading figure of the 1857 rebellion and whom Rani Velu Nachiyar preceded, given {u1}”；如果保留反向查找，重映射两步证据，不输出 yes/no。

### [dev #31 · hotpotqa_5a7755e05542993735360237](dev.md#human-review-hotpotqa_5a7755e05542993735360237)

**问题：** Which computer animated film was released first, Khan Kluay or A Christmas Carol starring Jim Carrey?

**差异：** 3 → 3 单元；comparison → bridge_comparison。

**原因：** 单元本身是两个已点名对象的事实加一个比较/共同属性结论，没有寻找未知中间实体的桥接步骤，但 question_type 被写成 bridge_comparison。

**建议：** 只将 question_type 改为 comparison，保留当前单元关系；这属于题型元数据错误，不应为凑题型增加桥接单元。

### [dev #34 · hotpotqa_5a7a51485542990783324f0e](dev.md#human-review-hotpotqa_5a7a51485542990783324f0e)

**问题：** Under the Yum Yum Tree starred this actress who was born in April, 1927?

**差异：** 2 → 2 单元；bridge → bridge。

**原因：** 原题要女演员姓名，最终必要单元却是 birth date of {u1}，会把日期当最终答案。

**建议：** u1 识别演员候选，u2 明确为“actress among {u1} born in April 1927”；出生日期只是筛选证据，必要单元的值应为演员姓名。

### [dev #42 · hotpotqa_5a9060f05542990a98493604](dev.md#human-review-hotpotqa_5a9060f05542990a98493604)

**问题：** What novel written by an American novelist born in 1804 was adapted into a British silent drama film?

**差异：** 2 → 3 单元；bridge → bridge。

**原因：** 最终 necessary 单元问的是 British silent drama film adaptation，原题要求小说名；改编电影和原著即使同名也不是同一对象。

**建议：** 最后的 necessary 单元必须是“novel by {u1} adapted into a British silent drama film”；可保留旧 gold 的作者→小说两单元结构，电影仅作筛选条件/证据。

### [dev #43 · hotpotqa_5ab2585855429970612095e6](dev.md#human-review-hotpotqa_5ab2585855429970612095e6)

**问题：** Between the Akita and Boykin Spaniel, which dog breed is larger?

**差异：** 3 → 3 单元；comparison → comparison。

**原因：** 模型把 larger 限定成 weight，但给定证据只有 large 与 medium-sized 的体型分类，没有体重数值。

**建议：** u1/u2 改为 size classification/size of the breed，并比较体型；不要把大/中型标签当成体重或凭外部知识填公斤数。

### [dev #48 · hotpotqa_5ab7eff35542993667794059](dev.md#human-review-hotpotqa_5ab7eff35542993667794059)

**问题：** What kind of musician does Neil Hannon and Stephen Malkmus have in common?

**差异：** 3 → 3 单元；comparison → bridge_comparison。

**原因：** kind of musician 被错解成 music genre，原题及证据说的是歌手等音乐人角色；同时题型误标为 bridge_comparison。

**建议：** 题型改为 comparison；两方单元询问 musician role/kind of musician，结论输出共同角色（如 singer），而不是摇滚等音乐风格。

### [dev #56 · hotpotqa_5ae29b615542992decbdcd4f](dev.md#human-review-hotpotqa_5ae29b615542992decbdcd4f)

**问题：** Huainan and Wuzhishan City, in in which country?

**差异：** 3 → 3 单元；comparison → bridge_comparison。

**原因：** 原题问两城市在哪个国家，模型的必要结论却问是否在同一国家，答案类型由国家名变成 yes/no；题型也误写 bridge_comparison。

**建议：** 题型改为 comparison，u3 改为“country containing both Huainan and Wuzhishan City”，仍依赖两方国家事实，输出国家名称。

## 保留新拆法｜重标人工标签（57 题）

### [train #1 · 2wikimultihopqa_015ccd41087711ebbd67ac1f6bf848b6](train.md#human-review-2wikimultihopqa_015ccd41087711ebbd67ac1f6bf848b6)

**问题：** Are director of film The Enigma Of The Folies-Bergere and director of film Deep Soul (Film) from the same country?

**差异：** 5 → 3 单元；bridge_comparison → comparison。

**原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。

**建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。

### [train #19 · 2wikimultihopqa_31756c8e085511ebbd59ac1f6bf848b6](train.md#human-review-2wikimultihopqa_31756c8e085511ebbd59ac1f6bf848b6)

**问题：** Do both Opium (1919 Film) and Monna Vanna (1915 Film) films have the directors from the same country?

**差异：** 5 → 3 单元；bridge_comparison → comparison。

**原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。

**建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。

### [train #33 · 2wikimultihopqa_55627704089111ebbd73ac1f6bf848b6](train.md#human-review-2wikimultihopqa_55627704089111ebbd73ac1f6bf848b6)

**问题：** Do both directors of films Jack'S The Boy and Autumn Sun share the same nationality?

**差异：** 5 → 3 单元；bridge_comparison → comparison。

**原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。

**建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。

### [train #42 · 2wikimultihopqa_6670d044088d11ebbd70ac1f6bf848b6](train.md#human-review-2wikimultihopqa_6670d044088d11ebbd70ac1f6bf848b6)

**问题：** Do both Secret Obsession and Descente Aux Enfers films have the directors from the same country?

**差异：** 5 → 3 单元；bridge_comparison → comparison。

**原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。

**建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。

### [train #44 · 2wikimultihopqa_6b702cbe0baf11ebab90acde48001122](train.md#human-review-2wikimultihopqa_6b702cbe0baf11ebab90acde48001122)

**问题：** Who is the uncle of Elisabeth Raiser?

**差异：** 2 → 2 单元；bridge → bridge。

**原因：** parent 比旧 father 更宽，但题目只问 uncle，未限定父系或母系；新父母→兄弟链并非错误，旧标注的父系链可以作为有证据的实例。

**建议：** 保留生成的 parent 描述；按源证据将实际父系关系映射到新单元。不要仅因 gold 写 father 就改写拆题器；如存在多条亲属候选，再补充候选/别名监督。

### [train #62 · 2wikimultihopqa_8e43ba54087c11ebbd6aac1f6bf848b6](train.md#human-review-2wikimultihopqa_8e43ba54087c11ebbd6aac1f6bf848b6)

**问题：** Which film was released more recently, Let's Be Famous or The Dilemma?

**差异：** 3 → 3 单元；comparison → comparison。

**原因：** 两版事实含义一致，但两个被比较对象的 u1/u2 顺序交换；不属于拆题语义错误。

**建议：** 保留新拆法，按对象交换旧 u1/u2 的答案、引用、特殊标记和快照标签；结论 u3 的证据引用也需随之核对。不要按编号直接拷贝。

### [train #72 · 2wikimultihopqa_a1ef2dee085311ebbd59ac1f6bf848b6](train.md#human-review-2wikimultihopqa_a1ef2dee085311ebbd59ac1f6bf848b6)

**问题：** Are director of film A Woman's War and director of film The New Klondike from the same country?

**差异：** 5 → 3 单元；bridge_comparison → comparison。

**原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。

**建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。

### [train #81 · 2wikimultihopqa_b3a5431b08cc11ebbd93ac1f6bf848b6](train.md#human-review-2wikimultihopqa_b3a5431b08cc11ebbd93ac1f6bf848b6)

**问题：** Do both directors of films One On One (1977 Film) and Ready Money (Film) share the same nationality?

**差异：** 5 → 3 单元；bridge_comparison → comparison。

**原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。

**建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。

### [train #98 · 2wikimultihopqa_cdd42e23087c11ebbd6aac1f6bf848b6](train.md#human-review-2wikimultihopqa_cdd42e23087c11ebbd6aac1f6bf848b6)

**问题：** Do both films: A Doll's House (1917 film) and Circles (film) have the directors from the same country?

**差异：** 5 → 3 单元；bridge_comparison → comparison。

**原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。

**建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。

### [train #104 · 2wikimultihopqa_df25d98608e111ebbda3ac1f6bf848b6](train.md#human-review-2wikimultihopqa_df25d98608e111ebbda3ac1f6bf848b6)

**问题：** Do director of film She Fell Among Thieves and director of film Ernest Rides Again have the same nationality?

**差异：** 5 → 3 单元；bridge_comparison → comparison。

**原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。

**建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。

### [train #115 · 2wikimultihopqa_ef3a400a087811ebbd67ac1f6bf848b6](train.md#human-review-2wikimultihopqa_ef3a400a087811ebbd67ac1f6bf848b6)

**问题：** Do both Itty Bitty Titty Committee and Desperate Journey films have the directors from the same country?

**差异：** 5 → 3 单元；bridge_comparison → comparison。

**原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。

**建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。

### [train #126 · hotpotqa_5a730a5555429901807daf72](train.md#human-review-hotpotqa_5a730a5555429901807daf72)

**问题：** You Can't Run Away from It starred which eight time Academy Award nominee?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 新单元完整限定电影演员和八次奥斯卡提名条件，旧版分候选识别和筛选。两种都能回答同一演员；不因隐式桥接而判新单元错误。

**建议：** 保留 single；新目标值对应旧末单元，支持集合联合 d5s0 的演员关系和 d9s1 的提名条件，重建证据快照。

### [train #132 · hotpotqa_5a752d375542996c70cfaea4](train.md#human-review-hotpotqa_5a752d375542996c70cfaea4)

**问题：** American Hairless Terrier and Old Danish Pointer, are breeds of which animal?

**差异：** 3 → 1 单元；comparison → single。

**原因：** 新单元直接询问两对象的共同类别，旧单元分别查类别再合并。新单元包含两个对象且要求共同类别，联合两方证据即可支持；单元更少本身不是错误。

**建议：** 保留 single。将旧共同类别结论的值迁移到新u1，并为它建立覆盖两方事实的联合支持集合。只看到一方时仍应 UNRESOLVED；不为恢复旧粒度新增单元。

### [train #144 · hotpotqa_5a7a22d45542990783324e80](train.md#human-review-hotpotqa_5a7a22d45542990783324e80)

**问题：** Tom Choi, born in Taegu, South Korea, is a Korean-American actor best known for "Teen Wolf", Teen Wolf is an American television series developed by Jeff Davis, for which channel?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 问题已明确给出 Teen Wolf 和开发者，旧 gold 再设“Tom Choi 以哪部剧著称”作为必须先满足的依赖，重复验证已给信息。

**建议：** 保留 single 拆法，按 d7s0 标注一个频道单元；描述最好使用“channel for which Teen Wolf was developed”，与问题精确对应。移除旧 u1 依赖及多余快照标签。

### [train #145 · hotpotqa_5a7a46785542990783324ee5](train.md#human-review-hotpotqa_5a7a46785542990783324ee5)

**问题：** What type of publication is Popular Mechanics and Sojourners?

**差异：** 3 → 2 单元；comparison → multipart。

**原因：** 旧拆法用两方事实+共同结论，新 multipart 分别要求回答两个对象的同一属性，两方都是 necessary。两种都能覆盖题目要求；没有显式共同结论不等于漏答。按用户要求保留生成的两个必要单元。

**建议：** 保持 multipart 和两个 necessary=true。分别映射旧u1/u2的属性值和证据，删除旧u3作为独立训练目标；只有两方都支持才是完整。若旧共同答案词过窄，按各方实际描述设置值/别名，不改变新拆法。

### [train #147 · hotpotqa_5a7a572e5542990783324f1c](train.md#human-review-hotpotqa_5a7a572e5542990783324f1c)

**问题：** In literary criticism, stream of consciousness is a narrative mode or method, that attempts to depict the multitudinous thoughts and feelings which pass through the mind, the term was coined by William James in 1890 in his "The Principles of Psychology", and in 1918 the novelist May Sinclair, Sinclair was the pseudonym of Mary Amelia St. Clair (24 August 1863 – 14 November 1946), a popular British writer who wrote about how many novels, short stories and poetry?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 问题已明示 May Sinclair 与 Mary Amelia St. Clair 的身份关系，旧 gold 却把识别该作家作为第一跳。

**建议：** 保留 single，直接询问该作家的作品数量；用 d10s0 支持。旧人物识别单元不应继续阻塞数量单元。

### [train #150 · hotpotqa_5a7f47d05542992e7d278ce2](train.md#human-review-hotpotqa_5a7f47d05542992e7d278ce2)

**问题：** When as the DVD box set of the simposon's season that included the episode that Mr. Burns starts to miss his childhood teddy bear released in region 1 ?

**差异：** 3 → 3 单元；bridge → bridge。

**原因：** 旧版按剧集→季→发行日期拆；新版按季（含剧情限定）→该季Region 1 DVD→日期拆。新描述仍保留剧情、季和Region 1，虽有冗余命名但目标未改变。

**建议：** 保留新3单元。新u1应取 season 5，需联合剧情定位和所属季的证据（d1s2/d1s0），不能复制旧u1的 Rosebud；新u2标注该季Region 1 DVD对象，新u3标注其日期，两者依 d7s6 和相应上下文/依赖重标。

### [train #154 · hotpotqa_5a809152554299485f598658](train.md#human-review-hotpotqa_5a809152554299485f598658)

**问题：** What is  Lauri Ylönen and Kim Jong-hyun's main occupation?

**差异：** 3 → 2 单元；comparison → multipart。

**原因：** 旧拆法用两方事实+共同结论，新 multipart 分别要求回答两个对象的同一属性，两方都是 necessary。两种都能覆盖题目要求；没有显式共同结论不等于漏答。按用户要求保留生成的两个必要单元。

**建议：** 保持 multipart 和两个 necessary=true。分别映射旧u1/u2的属性值和证据，删除旧u3作为独立训练目标；只有两方都支持才是完整。若旧共同答案词过窄，按各方实际描述设置值/别名，不改变新拆法。

### [train #157 · hotpotqa_5a83a5df5542992ef85e233f](train.md#human-review-hotpotqa_5a83a5df5542992ef85e233f)

**问题：** Chad Michaels was a runner up on the fourth season of RuPaul's Drag Race and is known for impersonating which singer?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 问题直接点名 Chad Michaels，并给出比赛背景，旧 gold 却再次把比赛亚军身份当作需检索的第一跳。

**建议：** 保留一个 necessary 单元“singer impersonated by Chad Michaels”，以 d4s0 支持；删除重复身份依赖并重建标签。

### [train #159 · hotpotqa_5a8492b65542997b5ce3fec5](train.md#human-review-hotpotqa_5a8492b65542997b5ce3fec5)

**问题：** Pylon and Bullet for My Valentine, is what type of musical organization?

**差异：** 3 → 1 单元；comparison → single。

**原因：** 新单元直接询问两对象的共同类别，旧单元分别查类别再合并。新单元包含两个对象且要求共同类别，联合两方证据即可支持；单元更少本身不是错误。

**建议：** 保留 single。将旧共同类别结论的值迁移到新u1，并为它建立覆盖两方事实的联合支持集合。只看到一方时仍应 UNRESOLVED；不为恢复旧粒度新增单元。

### [train #160 · hotpotqa_5a84b72b5542991dd0999dab](train.md#human-review-hotpotqa_5a84b72b5542991dd0999dab)

**问题：** What genre, usually involving a mysterious death, is exhibited by a book who features detective Sir Henry Merrivale?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 新单元直接问带有 Sir Henry Merrivale 的作品属于什么 genre；旧版用 mystery novel 再映射 mystery fiction。两种合理表达指向同一类作品，不能因为少一步就判错。

**建议：** 保留 single；以 d1s0/d1s1 的作品类型和人物关系标注值，核对 mystery novel/mystery fiction 的接受别名。若采用后者作为规范值，可用 d3s0 补充类别定义；重建支持路径而不恢复旧依赖。

### [train #163 · hotpotqa_5a88ec08554299206df2b3ad](train.md#human-review-hotpotqa_5a88ec08554299206df2b3ad)

**问题：** What are are commonly known as milkworts or snakeroots, Nothofagus or Polygala ?

**差异：** 3 → 3 单元；comparison → comparison。

**原因：** 新单元取两个候选的 common names，旧版取是否具有指定名称的 yes/no。两种取值均可回答题目；源文档确有 Nothofagus 的 southern beeches 和 Polygala 的 milkworts/snakeroots。

**建议：** 保留新 common-name 单元及对象顺序。新u1应标名称 southern beeches（d4s0），新u2应标 milkworts/snakeroots（d8s0/d8s1），不复制旧 yes/no。重新标注引用和快照；最终候选仍是 Polygala。

### [train #168 · hotpotqa_5a8b85f355429971feec4731](train.md#human-review-hotpotqa_5a8b85f355429971feec4731)

**问题：** Jean-Baptiste Andrea wrote and directed what 2003 French horror drama that was remade in 2014?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 旧 u1 直接写了问题未给出的电影名 Mumbai 125 KM，属于从标注/证据提前注入中间实体；新单元没有这项提示。

**建议：** 修改旧输入描述，不能把 Mumbai 125 KM 预先写入 question-only units。可以保留新单元并联合验证导演、年份和重拍条件，或拆成不含已知答案提示的两阶段候选筛选；重新标注支持集合。

### [train #169 · hotpotqa_5a8dd9b8554299068b959e06](train.md#human-review-hotpotqa_5a8dd9b8554299068b959e06)

**问题：** What islands are home to Rhinosolea microlepidota and are known in Japanese as the "Nansei" Islands?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 新单元完整保留栖息岛屿及 Nansei 别名条件，旧版显式分两步验证；两种粒度都合理。

**建议：** 保留 single；使用覆盖两条件的联合证据 d9s0 与 d4s0，重建支持集合和快照。不能仅因旧版存在依赖而增加新单元。

### [train #170 · hotpotqa_5a8e28ba5542990e94052a80](train.md#human-review-hotpotqa_5a8e28ba5542990e94052a80)

**问题：** Destiny and A Village Romeo and Juliet, is what type of play?

**差异：** 3 → 2 单元；comparison → multipart。

**原因：** 旧拆法用两方事实+共同结论，新 multipart 分别要求回答两个对象的同一属性，两方都是 necessary。两种都能覆盖题目要求；没有显式共同结论不等于漏答。按用户要求保留生成的两个必要单元。

**建议：** 保持 multipart 和两个 necessary=true。分别映射旧u1/u2的属性值和证据，删除旧u3作为独立训练目标；只有两方都支持才是完整。若旧共同答案词过窄，按各方实际描述设置值/别名，不改变新拆法。

### [train #172 · hotpotqa_5a908d1f55429916514e74f1](train.md#human-review-hotpotqa_5a908d1f55429916514e74f1)

**问题：** Rachel Carson and Walter Mosley, are which nationality?

**差异：** 3 → 2 单元；comparison → multipart。

**原因：** 旧拆法用两方事实+共同结论，新 multipart 分别要求回答两个对象的同一属性，两方都是 necessary。两种都能覆盖题目要求；没有显式共同结论不等于漏答。按用户要求保留生成的两个必要单元。

**建议：** 保持 multipart 和两个 necessary=true。分别映射旧u1/u2的属性值和证据，删除旧u3作为独立训练目标；只有两方都支持才是完整。若旧共同答案词过窄，按各方实际描述设置值/别名，不改变新拆法。

### [train #174 · hotpotqa_5ab292b4554299449642c901](train.md#human-review-hotpotqa_5ab292b4554299449642c901)

**问题：** The top brand of beer in North Korea is brewed by which company ?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 新单元在描述中保留“朝鲜顶级啤酒品牌的酿造公司”这一完整关系，旧版把品牌识别单独列出。两种粒度均可支持同一公司答案。

**建议：** 保留 single，值对应旧最终公司单元；支持集合必须覆盖品牌地位 d2s1 和酿造关系 d1s0，不能只有公司关系而跳过 top brand 限定。

### [train #175 · hotpotqa_5ab2989b554299194fa93423](train.md#human-review-hotpotqa_5ab2989b554299194fa93423)

**问题：** What American professional mixed martial artist who is currently fighting in the Middleweight division of the Ultimate Fighting Championship was trained by Matt Hume?

**差异：** 2 → 2 单元；bridge → bridge。

**原因：** 新版先从职业/国籍/级别找到候选，再验证 Matt Hume 训练关系；旧版先列学员再筛选。两种查找方向都可由给定文本支持。

**建议：** 保留新方向及两单元。新u1按 d2s0 标注符合职业条件的候选，新u2依赖新u1并按 d1s1 验证训练关系；不能复制旧u1的全部学员列表。出现多个候选时使用候选监督，不能凭未来证据提前选择。

### [train #178 · hotpotqa_5ab42d235542991751b4d6d1](train.md#human-review-hotpotqa_5ab42d235542991751b4d6d1)

**问题：** Who directed the Walt Disney Television movie that John William Minton was a cast member of?

**差异：** 3 → 2 单元；bridge → bridge。

**原因：** 新单元把演员别名解析并入电影识别，旧版把 John William Minton→Big John Studd 单列。只要身份链接有证据，新两单元仍然合理。

**建议：** 保留新2单元。电影识别需联合 d6s0 的别名证据与 d3s2 的演员表；导演单元用 d3s0 并依赖新u1。不能把演员表中的 Big John Studd 无依据地当成另一人，也不需要为旧粒度恢复单独别名单元。

### [train #179 · hotpotqa_5ab443ca5542991779162c43](train.md#human-review-hotpotqa_5ab443ca5542991779162c43)

**问题：** What do Lindsay Anderson and Aaron Kozak have in common?

**差异：** 3 → 1 单元；comparison → single。

**原因：** 新单元直接问共同点，旧版先按职业分两方再给结论。新问法更贴近原问题，并非必须改成职业三单元。

**建议：** 保留 single；用两方职业证据联合标注 filmmaker 等有支持的共同点及别名。不要只用一方职业作为完整支持；对其他合理共同点的接受范围由人工标签复核，不通过改写新单元强制只问 occupation。

### [train #186 · hotpotqa_5ab8292c55429934fafe6cfe](train.md#human-review-hotpotqa_5ab8292c55429934fafe6cfe)

**问题：** Anna Ranch Heritage Center is a former cattle ranch in a census-designated place with a population of what in 2010?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 新单元保留牧场所在地、人口和2010年三个限定，旧版把所在地显式拆出。合并没有改变询问对象或年份。

**建议：** 保留 single；以 d3s0 的所在地关系及 d7s1 的2010年人口联合支持，值仍为9,212；按新单元重新计算可见证据标签。

### [train #187 · hotpotqa_5ab8f1ae55429916710eb0c8](train.md#human-review-hotpotqa_5ab8f1ae55429916710eb0c8)

**问题：** Banks are subject to minimum capital requiremets based on what banking regulation recommendations issued by the Basel COmmittee on Banking Supervision? 

**差异：** 2 → 1 单元；bridge → single。

**原因：** 新单元同时限定最低资本要求与 Basel 委员会发布的建议，旧版把同一身份分两步验证。合并在语义上合理。

**建议：** 保留 single；联合 d1s3 与 d8s0 建立新支持集合和快照，不复用旧第二跳的单独引用，也不恢复旧两单元。

### [train #198 · hotpotqa_5ac119595542992a796dede5](train.md#human-review-hotpotqa_5ac119595542992a796dede5)

**问题：** Cherokee Lake is a reservoir formed by theimpoundment of what river flowing from Kingsport to Knoxville, Tennessee?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 新单元直接找形成 Cherokee Lake 的河流，旧版还把流向作为第二阶段核验。两种都指向同一河流，单单元不应因粒度不同被改回。

**建议：** 保留新 single。根据原问题是否仍要求核验流向，联合 d1s0/d8s0 建立完整支持，或明确记录题设已知的处理口径；不要悄悄把原有流向条件当成可忽略信息。

### [train #200 · hotpotqa_5ac1334b55429964131be184](train.md#human-review-hotpotqa_5ac1334b55429964131be184)

**问题：** What American author known for the Outlander series of novels, created her sixth novel, from the same series, called A Breath of Snow?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 新单元直接定位符合作者、系列和作品条件的人，旧版分两步验证相同身份；两种均合理。

**建议：** 保留 single；以作品署名及作者身份/系列信息重建支持路径，规范 A Breath of Snow 与 A Breath of Snow and Ashes 的别名。不能复制旧末单元的孤立支持。

### [train #202 · hotpotqa_5ac250355542992f1f2b384b](train.md#human-review-hotpotqa_5ac250355542992f1f2b384b)

**问题：** Who had more diverse credits in films, Charles Burnett or Patricio Guzmán?

**差异：** 3 → 3 单元；comparison → comparison。

**原因：** 旧单元取文档列出的角色数量，新单元取 film credits 文本/列表再比较多样性；角色列表足以表达这些事实，两种取值方式都合理。

**建议：** 保留生成的 credits 单元。人工目标改为文档支持的角色/credits 列表（而非机械复制7/1），明确结论依据不同角色的多样性。若存在“作品数量/角色种类”的歧义，在标签口径中说明，不强制将新单元改成旧计数。

### [train #205 · hotpotqa_5ac445975542995c82c4ad16](train.md#human-review-hotpotqa_5ac445975542995c82c4ad16)

**问题：** Which historic edifice has been a focal point of global and national activism since its inception, 1 Wall Street or Riverside Church?

**差异：** 3 → 3 单元；comparison → comparison。

**原因：** 两版事实含义一致，但两个被比较对象的 u1/u2 顺序交换；不属于拆题语义错误。

**建议：** 保留新拆法，按对象交换旧 u1/u2 的答案、引用、特殊标记和快照标签；结论 u3 的证据引用也需随之核对。不要按编号直接拷贝。

### [train #208 · hotpotqa_5adc0b3a5542996e685252b8](train.md#human-review-hotpotqa_5adc0b3a5542996e685252b8)

**问题：** What live-action television series was produced for Adult Swim and had Kristen Joy Schaal as an actor?

**差异：** 2 → 3 单元；bridge → bridge。

**原因：** 新拆法分别寻找满足 Adult Swim/live-action 条件和演员条件的剧集，再取共同剧集；旧版使用顺序桥接。两种查找方向都合理，不能仅因图形不同要求恢复旧版。

**建议：** 保留新3单元。按各自条件重标候选/剧集值；u2 的 live-action 也需相应来源支持，u3 只接受两方交集中符合全部条件的剧集。新u1/u2不是旧同编号单元，需重标支持集合；多个候选时不能提前硬填最终答案。

### [train #212 · hotpotqa_5adde7085542990dbb2f7f01](train.md#human-review-hotpotqa_5adde7085542990dbb2f7f01)

**问题：** What are both Dichondra and Peperomia?

**差异：** 3 → 2 单元；comparison → multipart。

**原因：** 旧拆法用两方事实+共同结论，新 multipart 分别要求回答两个对象的同一属性，两方都是 necessary。两种都能覆盖题目要求；没有显式共同结论不等于漏答。按用户要求保留生成的两个必要单元。

**建议：** 保持 multipart 和两个 necessary=true。分别映射旧u1/u2的属性值和证据，删除旧u3作为独立训练目标；只有两方都支持才是完整。若旧共同答案词过窄，按各方实际描述设置值/别名，不改变新拆法。

### [train #222 · hotpotqa_5ae0b79355429945ae95943c](train.md#human-review-hotpotqa_5ae0b79355429945ae95943c)

**问题：** Which star of The move The Founder was born on June 26, 1970 ?

**差异：** 2 → 2 单元；bridge → bridge。

**原因：** 新拆法先查 The Founder 的演员候选，再按生日筛选；旧拆法先查生日匹配人物再验证电影。两种方向均合理。

**建议：** 保留新方向。按 d3s1/d3s2 标注实际演员候选，新u2再用生日证据筛选；不能在只见演员表时提前把新u1固定为 Nick Offerman。重建候选值、证据和时间快照。

### [train #224 · hotpotqa_5ae130515542997b2ef7d121](train.md#human-review-hotpotqa_5ae130515542997b2ef7d121)

**问题：** These happy Golden Years was written by what American writer known for her series of children's books that were released from 1932 to 1943?

**差异：** 2 → 2 单元；bridge → bridge。

**原因：** 新旧查找方向相反：两步验证的实体最终相同，但第一跳和第二跳所使用的条件/证据交换。仅看相同答案字符串会漏掉这种差异。

**建议：** 新方向可以保留。按新 description 重新建立每步支持集合及依赖生效时刻；旧预设路径、标签不能仅因 expected_answer 相同而直接复用。

### [train #230 · hotpotqa_5ae234405542992decbdcc5a](train.md#human-review-hotpotqa_5ae234405542992decbdcc5a)

**问题：** In which city will you find the MTR or Mass Transit Railway which stops at Tin Yuet () which is located at ground level at the centre of Tin Shing Road and between Tin Yuet Estate and Tin Ching Estate?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 题目已经明示 MTR / Mass Transit Railway，旧 gold 又通过 Tin Yuet 识别轨道网络。对于当前问题找城市，这一步不应是必要依赖。

**建议：** 保留 single，直接询问 MTR 所在/服务城市；d4s0 已支持 Hong Kong。Tin Yuet 停靠关系可作问题给定背景，不能无条件沿用旧桥接阻塞。

### [train #235 · hotpotqa_5ae3fc835542995dadf24288](train.md#human-review-hotpotqa_5ae3fc835542995dadf24288)

**问题：** In between Die schweigsame Frau and La straniera which one is an opera in three acts?

**差异：** 3 → 3 单元；comparison → comparison。

**原因：** 新单元按“是否三幕歌剧”取 yes/no，旧事实值为幕数 three/two。新方式符合 A 的定名候选属性选择规则，不应为了对齐旧数字而改回。

**建议：** 将新事实目标重标为 yes/no，并用原幕数证据验证；复核派生结论与预设路径。保留新拆解，只重建人工监督标签。

### [train #237 · hotpotqa_5ae5394855429908b6326585](train.md#human-review-hotpotqa_5ae5394855429908b6326585)

**问题：** Which device can air TVPlayer channels for free and allows users to play using a remote?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 新单元完整保留 TVPlayer 免费频道和遥控游玩条件；旧版分设备候选和筛选。两种都可通过联合证据给出设备身份。

**建议：** 保留 single。支持需联合 d1s0 的播放设备与 d3s2 的遥控游戏条件，重新计算快照；不要只复制旧末单元的遥控器证据。

### [train #239 · hotpotqa_5ae60b0d554299546bf8302c](train.md#human-review-hotpotqa_5ae60b0d554299546bf8302c)

**问题：** Which professional footballer who plays as a left-back for Los Angeles Galaxy did Cheryl Cole divorced 

**差异：** 2 → 2 单元；bridge → bridge。

**原因：** 新旧查找方向相反：两步验证的实体最终相同，但第一跳和第二跳所使用的条件/证据交换。仅看相同答案字符串会漏掉这种差异。

**建议：** 新方向可以保留。按新 description 重新建立每步支持集合及依赖生效时刻；旧预设路径、标签不能仅因 expected_answer 相同而直接复用。

### [train #240 · hotpotqa_5ae64a2155429908198fa575](train.md#human-review-hotpotqa_5ae64a2155429908198fa575)

**问题：** What movie starring Ellen Page was directed by Jason Reitman and written by Diablo Cody, premiered at the 2007 Toronto International Film Festival?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 新单元完整保留导演、编剧、主演和首映条件；旧版分阶段验证同一电影。两种粒度都合理。

**建议：** 保留 single；联合 d10s0/d10s1/d10s4 覆盖全部条件，重建新支持集合与快照，不为对齐旧版而增加单元。

### [train #243 · hotpotqa_5ae752255542995703ce8be5](train.md#human-review-hotpotqa_5ae752255542995703ce8be5)

**问题：** Which river that streams westward from Pittsburgh, Pennsylvania, to Cairo, Illinois is the northern boundary of Downtown Louisville?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 新单元完整保留河流流向和城市边界条件；旧版分两阶段确认同一河流。两种都可通过联合证据支持。

**建议：** 保留 single；联合 d6s0 与 d8s1 标注完整支持，并重建快照。不要仅引用流向或边界一方，也不要恢复旧两单元。

### [dev #9 · 2wikimultihopqa_75be1186086711ebbd5eac1f6bf848b6](dev.md#human-review-2wikimultihopqa_75be1186086711ebbd5eac1f6bf848b6)

**问题：** Are director of film Vivasaayi Magan and director of film When The Evening Bells Ring (1951 Film) both from the same country?

**差异：** 5 → 3 单元；bridge_comparison → comparison。

**原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。

**建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。

### [dev #14 · 2wikimultihopqa_8ec76c0808db11ebbd9cac1f6bf848b6](dev.md#human-review-2wikimultihopqa_8ec76c0808db11ebbd9cac1f6bf848b6)

**问题：** Do both films: All The Winners and Mano Po 6: A Mother'S Love have the directors from the same country?

**差异：** 5 → 3 单元；bridge_comparison → comparison。

**原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。

**建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。

### [dev #19 · 2wikimultihopqa_bc7761cc088511ebbd6dac1f6bf848b6](dev.md#human-review-2wikimultihopqa_bc7761cc088511ebbd6dac1f6bf848b6)

**问题：** Do both films, Joe Somebody and Figures of the Night, have the directors who are from the same country?

**差异：** 5 → 3 单元；bridge_comparison → comparison。

**原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。

**建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。

### [dev #22 · 2wikimultihopqa_d996cdce0baf11ebab90acde48001122](dev.md#human-review-2wikimultihopqa_d996cdce0baf11ebab90acde48001122)

**问题：** Who is the child of Uday Tikekar?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 旧 gold 经配偶再找女儿，既多绕一步，也不能仅凭配偶的孩子就断定父子关系。完整上下文 d4s1 已直接说 Swanandi 是 Uday 的女儿。

**建议：** 保留 single：child of Uday Tikekar。用 d4s0/d4s1 的直接亲子关系重标支持集合，删除 spouse 依赖；不是删除已有父女事实。

### [dev #30 · hotpotqa_5a75dc7a5542992d0ec06004](dev.md#human-review-hotpotqa_5a75dc7a5542992d0ec06004)

**问题：** What is the term for the service provided by HCL Technologies involving discovery, interpretation, and communication of patterns in data?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 新单元合并服务定义和 HCL 是否提供该服务，旧版分两步验证同一术语；目标与限定均保留，合并合理。

**建议：** 保留 single；联合 d2s0 的定义和 d9s4 的服务列表标注 Analytics，并重建快照。

### [dev #33 · hotpotqa_5a78f57a554299148911f9bf](dev.md#human-review-hotpotqa_5a78f57a554299148911f9bf)

**问题：** For which Minneapolis-St. Paul area sports team did Zenon Konopka play? 

**差异：** 2 → 2 单元；bridge → bridge。

**原因：** 新 u1 已同时限定效力关系和 Minneapolis–St. Paul 地区，u2 询问其名字，存在冗余但未改变最终实体。旧版先列出全部球队再筛选。

**建议：** 保留生成的两单元，不因冗余强行换回旧候选列表。新u1需联合 d3s1 与 d8s2/d8s3 标注球队，新u2沿用同一身份的名称及对应支持/依赖；不把旧u1的整串球队名单复制到新u1。

### [dev #35 · hotpotqa_5a7aa8565542995eb53be88b](dev.md#human-review-hotpotqa_5a7aa8565542995eb53be88b)

**问题：** What movie did Katy Mixon star in that was directed by Seth Gordon?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 新单元完整询问 Katy Mixon 参演且由 Seth Gordon 执导的电影，旧版先列参演电影再筛选；两者目标一致。

**建议：** 保留 single，使用 d9s1 的参演关系和 d1s4 的导演关系联合支持；重建新目标和快照，而不是只迁移旧第二跳的直接引用。

### [dev #36 · hotpotqa_5a7cfdb755429909bec768e2](dev.md#human-review-hotpotqa_5a7cfdb755429909bec768e2)

**问题：** The Frogman Corps is the maritime special operations force of the unified armed forces of what kingdom?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 新单元保留 Frogman Corps→所属武装力量→王国的完整语义关系，只是不把中间军队单列。两种粒度都可由两段证据支持。

**建议：** 保留 single；支持集合覆盖 d10s0 与 d3s0，值为王国名；新单元不能在只看到军队名称时提前支持。

### [dev #39 · hotpotqa_5a8715fb5542991e771816bb](dev.md#human-review-hotpotqa_5a8715fb5542991e771816bb)

**问题：**  A Time for Miracles chronicles the life story of America's first native born saint who was born in what year?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 新单元以“America's first native born saint”作完整身份限定，直接问出生年；旧版另列电影→圣人。d3s0 在同一句中明确给出该唯一身份和出生日期，合并合理。

**建议：** 保留 single；直接以 d3s0 支持出生年1774。电影关系若被用作额外核验，可另保留相应支持路径，但不能强制继承旧电影身份依赖而忽视直接证据。

### [dev #41 · hotpotqa_5a88b15b5542994846c1ceba](dev.md#human-review-hotpotqa_5a88b15b5542994846c1ceba)

**问题：** Chino Moreno and Needtobreathe, are of which nationality?

**差异：** 3 → 2 单元；comparison → multipart。

**原因：** 旧拆法用两方事实+共同结论，新 multipart 分别要求回答两个对象的同一属性，两方都是 necessary。两种都能覆盖题目要求；没有显式共同结论不等于漏答。按用户要求保留生成的两个必要单元。

**建议：** 保持 multipart 和两个 necessary=true。分别映射旧u1/u2的属性值和证据，删除旧u3作为独立训练目标；只有两方都支持才是完整。若旧共同答案词过窄，按各方实际描述设置值/别名，不改变新拆法。

### [dev #57 · hotpotqa_5ae517665542990ba0bbb1b2](dev.md#human-review-hotpotqa_5ae517665542990ba0bbb1b2)

**问题：** What singer did the Tiny Dancers support who was in The Verve?

**差异：** 2 → 2 单元；bridge → bridge。

**原因：** 新拆法先查 Tiny Dancers 支持过的歌手，再核验 The Verve 身份；旧版反向查找。两种方向均合理，但新第一跳有多个候选。

**建议：** 保留新方向；按 d10s2 标注可支持的歌手候选，不在 The Verve 证据尚不可见时提前指定 Richard Ashcroft；新u2再结合 d6s1 及新u1依赖筛选。重新标注每一步证据与标签。

## 待确认：语义或标签口径（6 题）

### [train #111 · 2wikimultihopqa_e4fbf9c1088311ebbd6dac1f6bf848b6](train.md#human-review-2wikimultihopqa_e4fbf9c1088311ebbd6dac1f6bf848b6)

**问题：** Are director of film One Exciting Week and director of film The Woman God Changed both from the same country?

**差异：** 5 → 5 单元；bridge_comparison → bridge_comparison。

**原因：** 新事实写 country of origin，旧 gold 使用国籍/国别描述。Robert G. Vignola 的证据明确是 Italian-born American，出生地与国籍口径会得出不同结论。

**建议：** 明确本题采用 nationality/country descriptor 还是 birthplace。沿用现有 gold 时应写 nationality/country descriptor，并以 American 为值；不要把 Italian-born 当成国籍。

### [train #152 · hotpotqa_5a7fc61155429969796c1b57](train.md#human-review-hotpotqa_5a7fc61155429969796c1b57)

**问题：** The catalyst for the Peekskill riots was a concert annouced by a black singer that played football at what college?

**差异：** 2 → 2 单元；bridge → bridge。

**原因：** 原题“concert announced by a black singer”有修饰歧义；模型写成了歌手本人宣布音乐会，旧标注及 d2s1 只支持“已宣布的一场由该歌手演出的音乐会”。

**建议：** 澄清问题/单元为“black singer whose announced concert was the catalyst ...”；不要要求证据额外证明是谁发布公告。第二跳大学保持不变。

### [train #197 · hotpotqa_5ac04afa5542996f0d89cb80](train.md#human-review-hotpotqa_5ac04afa5542996f0d89cb80)

**问题：** Wells Cathedral School is a co-educational independent school located in Wells, Somerset, England, the school is one of the five specialist musical schools for school-age children in the United Kingdom, includes which specialist music school for children, located in the town of Bushey, in which south location?

**差异：** 2 → 2 单元；bridge → bridge。

**原因：** 题目原文本混有“哪所学校”和“在哪个 south location”，新旧 u2 都用模糊的 south location。源答案实际为 Hertfordshire。

**建议：** 新旧两单元先保持不变。需要确认原问题究竟只问地区，还是同时问学校与地区；此项是问题/监督范围待确认，不以旧 gold 为理由改拆题器。

### [dev #26 · 2wikimultihopqa_f48d9c60093011ebbdaeac1f6bf848b6](dev.md#human-review-2wikimultihopqa_f48d9c60093011ebbdaeac1f6bf848b6)

**问题：** Which film was released first, Upasane or Emilio (Film)?

**差异：** 3 → 3 单元；comparison → comparison。

**原因：** 新单元询问 release year，旧 u2 标注的是 U.S. theatrical release date（2016-11-04）。首映、国家上映及年份/日期的口径不同，不能原样复制。

**建议：** 保留新 release year 形式。人工需要确认发行口径：美国院线上映、世界首次发行还是文档年份；按确认口径把目标规范为年份，不能直接复制旧完整日期或擅自把美国上映年当全球首映年。

### [dev #29 · hotpotqa_5a745a8755429979e288291e](dev.md#human-review-hotpotqa_5a745a8755429979e288291e)

**问题：** Wellesley College and Vanderbilt University are both what?

**差异：** 3 → 3 单元；comparison → comparison。

**原因：** “both what”是开放的共同类别查询；旧答案只接受 private，而两方也可能共有其他机构类别。新 common classification 本身没有限定必须输出 private。

**建议：** 保留新 common classification 三单元。人工确认是否只接受 private 或也接受其他有证据的共同类别，并设置合适别名/接受范围；不为匹配旧唯一答案而改写拆题器。

### [dev #51 · hotpotqa_5abe97dc5542994516f453cf](dev.md#human-review-hotpotqa_5abe97dc5542994516f453cf)

**问题：** What South East London-based post-punk/art rock group took their name from a American radical feminist that is best known for attempting to murder artist Andy Warhol?

**差异：** 2 → 1 单元；bridge → single。

**原因：** 问题说乐队得名于女权主义者，旧 gold 也按人物描述；d4s3 实际说名称来自她写的 SCUM Manifesto。新单元还把人物/命名来源/乐队全部压在一起。

**建议：** 先修订问题与 gold 的命名关系，不把人物和作品混为一谈；可拆为人物→其宣言→以该宣言命名的乐队，最终必要值仍是乐队。没有这一步复核，不应将当前任一版作为已审核训练标签。

## 复现标注

逐题判断保存在 `human_comparison_review.json`，其中也记录参考证据原文。重新导出 train.md/dev.md 会覆盖标记，可从仓库根目录运行：

```bash
python3 a_work/annotate_sft_review.py
```

脚本仅重放已审阅意见，不运行模型、不自动判定正确性、不修改 JSON 生成结果。若数据内容或模型运行变更，应重新审阅，不应沿用本报告。
