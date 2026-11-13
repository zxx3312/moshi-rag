# Batch 6–10 修订报告

保留原始五份review以及原gold/annotations不变。共150题：原题调整63题，替换24题，核查后保留63题。仍保留每batch 30题及Q151–Q300编号。

## 交付与使用

- 各batch目录含新的 `samples.jsonl`、`annotations.json`、`gold.jsonl`、`review.md`、`checks.json`。
- [150题gold](gold.jsonl)和[samples](samples.jsonl)必须配套使用；替换题的ID和部分题干已变化。
- [changes.json](changes.json)保存150题逐题前后unit、原始note及处理结论；[manifest.json](manifest.json)记录源哈希、去重边界和局部约定。
- 后续重新抽取SFT候选时，必须把本目录samples.jsonl的ID及归一化题干加入排除集合；原Step2保留名单尚未切换到新版。
- 本次为修订草稿，不标作人工已批准，不修改原数据或生成训练样本。运行 `python b_work/test_set/revisions/batch06_10_v1/build_revision.py` 可重建本目录产物。

## 处理原则与核查结论

同一组证据内为AND，不同组为OR。真实依赖全部满足后才走普通support；命中presupposition_sets且至少一个父unit已支持时可走预设链路。证据句带原文档标题，可据标题解析代词/姓氏，不能据标题猜属性。

二选一题沿用SFT的两候选事实+结论格式；无法证明的另一候选保留UNRESOLVED，不能为了消除空support捏造否定。尤其Q166的old German herding dogs与目标变种不是同一实体；Q271的受圣职是事件，Q257未列国籍，均不满足旧note建议的omission条件。

Q230按用户明确认可使用获奖年份年龄下界；Q238按用户要求接受非洲分布归一化；Q240的小说作者捷径明确标成预设路径，不冒充系列作者的直接证据。这三项局部约定在gold review和manifest中单独说明。

没有找到A端拆词器实现，因此“符合规则”仅指本地guide/SFT结构及评估器验证，不声称完成线上模型输出对齐。

## 修改清单

| 题号 | 处理 | 修改方法 |
|---|---|---|
| [Q152](batch_06/review.md) | 调整 | 题干已点名美术馆，删除画作桥接；新增d10s0、d3s2备选。 题干澄清：Washington, D.C.不是州，改问城市，保留原题及源答案供追溯。 |
| [Q153](batch_06/review.md) | 替换 | 替换：u1不唯一且d10s3未给SexyBack第一名；这是桥接定位和关键排名缺证据，不能据源答案补造。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q155](batch_06/review.md) | 调整 | 按用户明确口径，用d4s1的1861支持u2；u3继续按年份比较。 本题局部约定：按用户note，本题将founding year作为opening date；不推广到其他题。 |
| [Q156](batch_06/review.md) | 替换 | 替换：山峰被错标为subrange；按用户要求替换。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q158](batch_06/review.md) | 调整 | d1s3写的是Khan Kluay，因此补入u2而非u1；另补u2的d6s2与u1的d10s1。 |
| [Q159](batch_06/review.md) | 调整 | 题干澄清：将creator改为popularly attributed，避免把原文明确存疑的归属写成事实。 将人名答案改为Betsy Ross flag；用d9s0+d9s2支持旗帜及13颗星，保留桥梁人物定位。 |
| [Q161](batch_06/review.md) | 调整 | 每个候选各建一个非necessary事实unit；Qwirkle的定义支持类别排除，结论支持确认和排除两条预设链路。 |
| [Q162](batch_06/review.md) | 调整 | 先按题干姓氏定位女演员，再验证出演Arul；删除提前泄漏Jyothika的描述。 |
| [Q164](batch_06/review.md) | 调整 | Alex the Dog已在题干出现，删除Spuds MacKenzie桥接；d9s0直接定位品牌。 |
| [Q165](batch_06/review.md) | 调整 | d9s0单独没有magic主题，不能独自定位电影；增加d9s0+d9s1链路，并补d7s2的2006作为年份备选。 |
| [Q166](batch_06/review.md) | 调整 | 补建两候选事实unit，保留由Black Mouth Cur的美国起源排除得到答案的链路。d5s0是另一种传统牧羊犬群体，d2s0是German Shepherd，均不强行作为目标变种的直接起源证据；u1仍UNRESOLVED但不阻塞结论。 |
| [Q167](batch_06/review.md) | 调整 | 出生日期比较符合规则；补齐题干艺名Teru及全名别名，避免只接受Teruhiko。 |
| [Q170](batch_06/review.md) | 调整 | 补建Kir事实unit，定义未记载饮用习惯，不能by_omission；Hot toddy正向证据独立完成结论。 |
| [Q174](batch_06/review.md) | 替换 | 替换：只有城市，无南北方位或纬度；当前guide不允许隐含地理知识。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q179](batch_06/review.md) | 调整 | 补充d3s5和d10s0：均联系Neiman Marcus、Dallas及1907；不使用只说明现在总部的d8s0。 |
| [Q180](batch_06/review.md) | 调整 | 题干澄清：限定为文档列出的阵容，避免比较当前阵容与历史全体成员。 |
| [Q181](batch_07/review.md) | 调整 | u1已给出完整答案，移除黑猫定义的重复桥接。 |
| [Q183](batch_07/review.md) | 调整 | 保留正向确认链路；补题干短名Joe Orton为答案别名，不从Henry James的职业介绍推断作品命名关系。 |
| [Q186](batch_07/review.md) | 调整 | 合并为single，移除全名转换；d3s0仅介绍角色，按标题可解析He时不单独要求该句；补d5s1、d4s1备选。 |
| [Q188](batch_07/review.md) | 调整 | 删除题干没有的新体育场限定new，其余链路由d3s2和d4s2明确支持。 |
| [Q189](batch_07/review.md) | 替换 | 替换：美国到非欧洲需要额外地理映射，当前guide明确不允许。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q190](batch_07/review.md) | 替换 | 替换：Hole的两个创办者不是完整阵容；未找到可比较的成员总数。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q191](batch_07/review.md) | 调整 | Flicker已在题干中，删除演员/歌手桥接；保留来源当时的计划发行日期。 |
| [Q192](batch_07/review.md) | 调整 | 题干澄清：限定为文档列举的笔名数量，不断言终身总数。 继续比较1与4，新增题干短名Nelson DeMille。 |
| [Q195](batch_07/review.md) | 替换 | 替换：创建奖项不等于赞助奖项；上下文没有明确赞助关系。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q196](batch_07/review.md) | 替换 | 替换：French Air Force任职不等于法国来源/国籍；没有其他支持u2的句子。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q200](batch_07/review.md) | 调整 | d7s1本来已支持u1，同时直接说明辞职后任Secretary of the Interior，补作u2备选；无需等d3s0扩展官职名称。 |
| [Q201](batch_07/review.md) | 替换 | 替换：没有县与镇的政府层级规则，不能从两地所有者直接推出higher。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q203](batch_07/review.md) | 调整 | 按SFT两候选格式补建Bogosian的职业排除unit；确认与排除各自可完成结论，补短名别名。 |
| [Q205](batch_07/review.md) | 替换 | 替换：bimonthly在上下文未消歧，无法确定比monthly多还是少。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q206](batch_07/review.md) | 调整 | 题干澄清：将含混的was at限定为原文记载的2014年竞选宣布，不暗示实际参加或出席2016年选举。 删除全名桥接，d9s2即可回答；保留完整选举名称为别名。 |
| [Q208](batch_07/review.md) | 调整 | 已检查d10s0–d10s3的Waugh介绍，没有逃离纳粹的信息；历史事件不能用职业遗漏排除。补候选unit但仅启用Freud正向链路。 |
| [Q210](batch_07/review.md) | 替换 | 替换：producer不能直接等同impresario；按用户要求替换。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q215](batch_08/review.md) | 调整 | 题干澄清：区分电视台许可城市Topeka与发射机所在地Maple Hill；证据和答案不变。 |
| [Q218](batch_08/review.md) | 调整 | 题干澄清：删除不唯一的画家筛选，将founding location明确为1903年开始的展览举办城市。 single直接使用d8s0；不再事后挑选Vallotton，也不将创办者住所当作展览地点。 |
| [Q221](batch_08/review.md) | 调整 | d10s0与d9s0均列lemon juice，修正no→yes，u3由两组成分交集推出。源答案no留在来源记录。 |
| [Q222](batch_08/review.md) | 调整 | 按题干去掉north bank额外限定，补d7s3备选。 |
| [Q223](batch_08/review.md) | 调整 | 题干已给电影名，移除Vinessa Shaw桥接。 |
| [Q224](batch_08/review.md) | 调整 | 事实unit保留原文4、1、2，不把7冒充原文值；u3按确定性算术4+1+2=7<39比较。 |
| [Q226](batch_08/review.md) | 替换 | 替换：乐队成员关系不唯一且用户明确要求换题。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q228](batch_08/review.md) | 调整 | 补两候选结构。另一乐队的创办者信息不能证明Valli从未加入，关系属性不按遗漏排除；仅启用Four Seasons确认链路。 |
| [Q230](batch_08/review.md) | 调整 | 补d3s0+d3s3。按用户接受的获奖年龄下界，2007年最早也已72年10个月，超过Glasgow约72年7个月，u3可比较；不使用今天日期。 本题局部约定：按用户明确认可，将2007年获奖记载视为在世年龄下界；这是本题获准的推断，不宣称来源明确写出寿命或普遍证明奖项只能颁给在世者。 |
| [Q231](batch_08/review.md) | 调整 | 补两个明确two species的备选证据。 |
| [Q232](batch_08/review.md) | 调整 | 题干澄清：限定系列中有作品被学校采用，不把个别作品的教学使用扩大为全部三本。 |
| [Q235](batch_08/review.md) | 调整 | 题干澄清：将four divisions改为four named business areas，并限定来源2017年榜单；不把other businesses删除。 |
| [Q236](batch_08/review.md) | 调整 | 补两条明确说明Toussaint Louverture领导Haitian Revolution的备选。 |
| [Q237](batch_08/review.md) | 调整 | 补两候选结构，城市所有权不是运营者证据；保留正向确认链路，不臆造另一机场运营关系。 |
| [Q238](batch_08/review.md) | 调整 | 将origin描述改为distribution，按用户要求补d5s0备选；d5s1使用的是center of distribution部分，u3以两种植物的非洲分布交集推出。 本题局部约定：按用户note接受Afrotropics及South Africa到Africa的地域归一化，仅用于本题分布证据；不推广到无证据的经纬度比较。 |
| [Q239](batch_08/review.md) | 替换 | 替换：WPX没有部门数量，不能将沉默算成0。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q240](batch_08/review.md) | 调整 | 保留两条路径：d2s0为预设捷径；d2s1+d7s0为完整系列桥接证据。合并到一个必要unit，避免无条件依赖u1挡住捷径。 本题局部约定：按用户要求，单本小说作者捷径依赖本题同作者系列的预设；明确放在presupposition_sets，不当作“书作者必等于系列作者”的普遍证据。 |
| [Q241](batch_09/review.md) | 替换 | 替换：四名回归球员，题干没有唯一定位条件。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q242](batch_09/review.md) | 调整 | 删除题干未给出的Twilight，避免描述提前泄漏中间信息。 |
| [Q243](batch_09/review.md) | 调整 | 将public or private答案选项从unit描述移至属性名institutional funding classification，避免SFT描述泄漏校验误判。 将public or private答案选项从unit描述移至属性名institutional funding classification，避免SFT描述泄漏校验误判。 |
| [Q246](batch_09/review.md) | 调整 | 补齐四条Brooklyn属于New York City的明确备选证据。 |
| [Q247](batch_09/review.md) | 替换 | 替换：Ural上下文未说明公立性质；前身名称不能补出合并后性质。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q249](batch_09/review.md) | 替换 | 替换：缺少原始阵容及保持原阵容录制的专辑数，不能由主唱离队倒推。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q250](batch_09/review.md) | 调整 | 保留至少3的下界，精确3也支持该下界；补Laurus和Liriodendron备选。 |
| [Q252](batch_09/review.md) | 调整 | 电影written by已支持编剧职业；另收录全名与screenwriter Mutrux的组合，避免单靠姓氏对应。 |
| [Q253](batch_09/review.md) | 调整 | 标题The Simpsons (season 10)提供季名，d4s1同时说明首集和集数，可独立替代d1s0。 |
| [Q254](batch_09/review.md) | 调整 | 题干澄清：改为历史领地，不把1920年的Hawaii称为当时的州；Territory of Hawaii与Hawaii作为名称归一化。 删除领地升州的额外桥接，用d8s0直接回答。 |
| [Q255](batch_09/review.md) | 调整 | 题干澄清：限定为原文提供的两个网络口径，不推断同一时点全球网点总量。 u1采用共同上界773：78+622=700及2011年的773都满足；与UniCredit的>8500比较，避免把两个不同值当作同一个精确值。 |
| [Q256](batch_09/review.md) | 调整 | 补博物馆位于Winter Park的备选d2s1。 |
| [Q257](batch_09/review.md) | 调整 | 补另一候选unit。d6s0列PBS和作者而未列国籍，不满足“已列出该属性其他值”的omission条件，故仅保留正向确认。 |
| [Q260](batch_09/review.md) | 调整 | 删除全名桥接，按标题可解析Goward，补d3s3备选；接受Pru和全名以及源短名。 |
| [Q261](batch_09/review.md) | 替换 | 替换：third after A and B未明确两者顺序，不能支持紧邻的next smaller关系。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q264](batch_09/review.md) | 调整 | 同句给出冠名人物及公司，合并为公司定位unit，保留公司到所在地的真正第二跳。 |
| [Q266](batch_09/review.md) | 替换 | 替换：Ainslee文档未给出版频率。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q268](batch_09/review.md) | 调整 | 每句都同时满足两个条件，合并为single且两句互为备选。 |
| [Q269](batch_09/review.md) | 调整 | 民军两用且主要服务居住于美国东部的波多黎各人，组合明确描述民用旅客服务；补u2并使u3可推导。d8s1只说charter，未区分客运货运，不单独接受。 |
| [Q270](batch_09/review.md) | 替换 | 替换：缺少东西相对方位或经度。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q271](batch_10/review.md) | 调整 | 补两候选结构。按当前guide，ordination是事件而非职业，d9s0的作家职业介绍不能证明未受圣职；纠正旧note，保留Merton正向链路。 |
| [Q273](batch_10/review.md) | 调整 | 先确定Ira Lewis戏剧的电影，再用演员表及完整姓名验证Jerome Bernard；不从部分姓名任意选Orbach。Karabel也不被误称为演员。 |
| [Q274](batch_10/review.md) | 调整 | 删除全名转换用途；先核对1935年成立，再验证通缉名单，补d4s0。两项筛选都保留，不能因回答出FBI就忽略年份。 |
| [Q276](batch_10/review.md) | 调整 | 是非题答案改为yes，类型和年份片段保留在来源中。 |
| [Q277](batch_10/review.md) | 调整 | 反转筛选顺序，先所有权条件再播出关系；去掉Canadian额外限定，不从CBS/CTV中事后选答案。 |
| [Q279](batch_10/review.md) | 替换 | 替换：缺少东西相对方位或经度。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q280](batch_10/review.md) | 调整 | d2s2明确说明影片发布于BBC iPlayer，可支持题干所指BBC发布机构，补作u1备选。 |
| [Q282](batch_10/review.md) | 调整 | 题干只问共同职业，screenwriter及film director都成立，加入其他有效答案；此处aliases承载可接受答案集合，不声称两种职业语义等同。 |
| [Q287](batch_10/review.md) | 替换 | 替换：母公司创始人不能直接当作电视网络创始人。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q288](batch_10/review.md) | 替换 | 替换：Fred Taylor及Corey Dillon均满足条件，答案不唯一。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q289](batch_10/review.md) | 调整 | 补齐主唱身份六条备选及公司创办d9s2；d9文档可独立完成两跳。 |
| [Q290](batch_10/review.md) | 调整 | 补1396 ft的独立备选，保持建成高度口径。 |
| [Q291](batch_10/review.md) | 调整 | 先按电影条件定位角色，再核验球员昵称；补人物条目路径，避免先输出两个候选昵称。 |
| [Q292](batch_10/review.md) | 替换 | 替换：上下文只给London；当前规则未允许city→country常识映射。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q295](batch_10/review.md) | 替换 | 替换：district与province层级不一致，且没有可用的行政层级推理规则。 新题保留原source type，人工核对两条显式事实及答案。 |
| [Q299](batch_10/review.md) | 调整 | 补题干姓名别名。 题干澄清：将主观wider scope明确为文档列举职业数量，按6与2比较。 |
| [Q300](batch_10/review.md) | 替换 | 替换：Jim Cummings配音的是Dr. Robotnik，作品名Sonic不是刺猬角色配音证据。 新题保留原source type，人工核对两条显式事实及答案。 |

## 替换题映射

24道替代题来自本地HotpotQA train源；按ID和归一化题干排除原debug、原评估全集、SFT全部候选及已选gold。保留原source type（8 bridge、16 comparison），但比较子类型偏向可直接验证的日期/年份，未宣称细粒度难度分布不变。

| 原题号 | 新sample_id | 新问题 | 新答案 |
|---|---|---|---|
| 153 | `hotpotqa_5a879ab05542996e4f30887e` | The Oberoi family is part of a hotel company that has a head office in what city? | Delhi |
| 156 | `hotpotqa_5a7a02235542996c55b2dcd3` | Who was born first, Pablo Trapero or Aleksander Ford? | Aleksander Ford |
| 174 | `hotpotqa_5a736bfa5542991f29ee2e03` | Who is older Glenn Hughes or Ross Lynch? | Glenn Hughes |
| 189 | `hotpotqa_5a77bd595542995d83181291` | Between two tennis players Kim Clijsters and Mary Pierce, who is older? | Mary Pierce |
| 190 | `hotpotqa_5a769ac95542993569682c4f` | Who was born first, Odysseas Elytis or Cornel West? | Odysseas Elytis |
| 195 | `hotpotqa_5ac2c3545542990b17b1548b` | Chang Ucchin was born in korea during a time that ended with the conclusion of what?  | World War II |
| 196 | `hotpotqa_5ab808755542990e739ec7f2` | Which movie was released first, The Hunchback of Notre Dame or Saludos Amigos? | Saludos Amigos |
| 201 | `hotpotqa_5a7cbd7c554299452d57b9e6` | Who was born first Neil LaBute or H. Bruce Humberstone? | H. Bruce Humberstone |
| 205 | `hotpotqa_5a79f2185542996a35c1703d` | Who was born first George Marshall or Allan Dwan ? | Allan Dwan |
| 210 | `hotpotqa_5adf8d5b5542995534e8c7e1` | What year was the winner of the 2016 Marrakesh ePrix born? | 1988 |
| 226 | `hotpotqa_5a7a0d665542990783324e14` | Who was born first, Joe Manganiello or Kirk Kerkorian? | Kirk Kerkorian |
| 239 | `hotpotqa_5a7bb84d554299294a54aaa1` | Who is older, Vincent Walker or David Usher? | David Usher |
| 241 | `hotpotqa_5a7906f55542990784727792` | When was Fannie Lee Chaney's son born? | May 30, 1943 |
| 247 | `hotpotqa_5a89eca455429946c8d6ea11` | Was Beyond the Gates of Splendor or Jesus Camp released first? | Beyond the Gates of Splendor |
| 249 | `hotpotqa_5a793e77554299029c4b5f36` | Who was born first, Martin Heidegger or Lydia Davis? | Martin Heidegger |
| 261 | `hotpotqa_5ae65d055542996d980e7b14` | What was population of the city where the Dutch retired footballer Foeke Booy born? | 108,249 |
| 266 | `hotpotqa_5a7b5e55554299042af8f755` | Which author was born first, Lorraine Hansberry or Sandra Gulland? | Lorraine Hansberry |
| 270 | `hotpotqa_5a90b93f5542995651fb51ca` | Which documentary was released earlier, Almost Sunrise or 51 Birch Street? | 51 Birch Street |
| 279 | `hotpotqa_5a79e5a85542996c55b2dc94` | Who was born first, Tanya Donelly or Trace Cyrus? | Tanya Donelly |
| 287 | `hotpotqa_5ac3983a554299657fa290f5` | At the 2011 census, what was he population of the city where Kerry Saxby-Junna was born? | 6,960 |
| 288 | `hotpotqa_5ae1cab7554299492dc91b8a` | What nationality is the actress who played the role of Sam Sloan's wife Trudy in the sitcom The Single Guy ? | American |
| 292 | `hotpotqa_5a78b59d554299148911f958` | Which musician was born first, John Tardy or Tom Barman? | John Tardy |
| 295 | `hotpotqa_5a77431355429972597f14de` | Who is older, Rohan Bopanna or Sherwood Stewart? | Sherwood Stewart |
| 300 | `hotpotqa_5a90bd6555429933b8a205cf` | What is the nationality of the singer-songwriter who wrote the poetry collection Early Work ? | American |

## 已核查并保留的note

| 题号 | 结论 |
|---|---|
| Q157 | 复核后保留原标注；原note为说明或未发现需要修改的证据/依赖问题。 |
| Q160 | 复核后保留原标注；原note为说明或未发现需要修改的证据/依赖问题。 |
| Q163 | 已检索完整上下文；d3s1只说明Hawking创办中心，不能替代Director of Research证据。保留d5s0及现有链路。 |
| Q169 | 复核后保留原标注；原note为说明或未发现需要修改的证据/依赖问题。 |
| Q173 | 问题意思是“James Tully于1928年当选代表的选区，以谁命名？”d4s4先定位Barton，d2s1再给出Sir Edmund Barton，现有两跳正确。 |
| Q182 | 复核后保留原标注；原note为说明或未发现需要修改的证据/依赖问题。 |
| Q193 | 保留。English→England是国别形容词归一化；题干问from而非公民身份，出生地与国别描述可用于本题。 |
| Q199 | 复核后保留原标注；原note为说明或未发现需要修改的证据/依赖问题。 |
| Q207 | 复核后保留原标注；原note为说明或未发现需要修改的证据/依赖问题。 |
| Q209 | 保留两跳。铁路名称含Bodie不等于题干明确给出终点；d5s0仍是确认ghost-town terminus所需证据，不能仅按名称跳过。 |
| Q217 | 复核后保留原标注；原note为说明或未发现需要修改的证据/依赖问题。 |
| Q265 | 保留d3s1→d5s0两跳。d3s1只说明来自Cradle of Filth，未说明创始成员；题干没有点名该乐队，也不能排除他在多个乐队任职，故不把一般成员关系直接升级为founder捷径。 |
| Q285 | 复核后保留原标注；原note为说明或未发现需要修改的证据/依赖问题。 |
| Q296 | 复核后保留原标注；原note为说明或未发现需要修改的证据/依赖问题。 |
| Q298 | 保留Chilopsis的明确单种正向链路和唯一候选预设。Cunninghamia的one or two不等于明确多于一种，不增设排除证据；在报告保留分类不确定性。 |

## 题干澄清（保留原文供追溯）

### Q152

- 原题：Lady Elizabeth Delmé and Her Children (1779) is a portrait given to the National Gallery of Art in 1937, which is located in which state?
- 新题：Lady Elizabeth Delmé and Her Children (1779) is a portrait given to the National Gallery of Art in 1937, which is located in which city?
- 原因：Washington, D.C.不是州，改问城市，保留原题及源答案供追溯。

### Q159

- 原题：What flag features 13 stars, and has a creator who also has a memorial bridge named after her connecting Pennsylvania and New Jersey?
- 新题：What flag features 13 stars and is popularly attributed to the woman after whom the memorial bridge connecting Pennsylvania and New Jersey is named?
- 原因：将creator改为popularly attributed，避免把原文明确存疑的归属写成事实。

### Q180

- 原题：Which band has more members, Chvrches or Goodbye Mr. Mackenzie?
- 新题：Comparing the lineups stated in the context, which band has more members, Chvrches or Goodbye Mr. Mackenzie?
- 原因：限定为文档列出的阵容，避免比较当前阵容与历史全体成员。

### Q192

- 原题：Who had more pen names, George Orwell or Nelson DeMille?
- 新题：Who has more pen names explicitly listed in the context, George Orwell or Nelson DeMille?
- 原因：限定为文档列举的笔名数量，不断言终身总数。

### Q206

- 原题：What election was Senator Harry Reid at in Nevada?
- 新题：In January 2014, what election did Bob Beers announce he would enter against Senator Harry Reid in Nevada?
- 原因：将含混的was at限定为原文记载的2014年竞选宣布，不暗示实际参加或出席2016年选举。

### Q215

- 原题：Where is a television transmitter located in Topeka, KS?
- 新题：Where is the transmitter of the television station licensed to Topeka, KS, located?
- 原因：区分电视台许可城市Topeka与发射机所在地Maple Hill；证据和答案不变。

### Q218

- 原题：In which city did he painter and printmaker associated with "Les Nabis" found Salon d'Automne?
- 新题：In which city has the Salon d'Automne been held since its first exhibition in 1903?
- 原因：删除不唯一的画家筛选，将founding location明确为1903年开始的展览举办城市。

### Q232

- 原题：What author wrote a three book series of memoirs that are studied in school systems around the world?
- 新题：What author wrote a three-book memoir series whose books include works studied in school systems around the world?
- 原因：限定系列中有作品被学校采用，不把个别作品的教学使用扩大为全部三本。

### Q235

- 原题：What 4 divisions make up the company of the wealthiest person in Georgia?
- 新题：Which four business areas are explicitly named for the company chaired by the wealthiest person in Georgia in the stated 2017 list?
- 原因：将four divisions改为four named business areas，并限定来源2017年榜单；不把other businesses删除。

### Q254

- 原题：1920 Politics was a Republican political strategy to reassert the authority of the white race in which US state?
- 新题：In what U.S. territory did the 1920 Politics strategy operate?
- 原因：改为历史领地，不把1920年的Hawaii称为当时的州；Territory of Hawaii与Hawaii作为名称归一化。

### Q255

- 原题：Which bank has more branches, China CITIC Bank or UniCredit?
- 新题：Using the branch counts stated in the context, which is larger: China CITIC Bank's mainland branch network or UniCredit's network?
- 原因：限定为原文提供的两个网络口径，不推断同一时点全球网点总量。

### Q299

- 原题：Who has a wider scope of profession, Christopher Guest or  Roman Karmen?
- 新题：Who has more distinct professions explicitly listed in the context, Christopher Guest or Roman Karmen?
- 原因：将主观wider scope明确为文档列举职业数量，按6与2比较。

## 校验

- 150/150题结构、证据ID、依赖无环及最终答案在全上下文下可支持。
- 空上下文没有任何unit被错误支持；22个实际评估器最小证据场景通过。
- 24道替代题的题干、答案、context及supporting_facts与训练原始记录逐字段一致。
- 原五批20个review/gold/annotation/check文件SHA256前后相同。
- 另有非必要候选unit维持UNRESOLVED，属于未提供证据的事实，不阻塞已验证的预设最终路径。
