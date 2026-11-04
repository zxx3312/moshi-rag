# 原待复核题目（28 题，历史记录）

由 `sample_review.py --flagged` 生成的替换前复核材料。2026-11-03 的替换审计已从最终 gold 中移除其中 21 题；保留的 7 题为 `2wikimultihopqa_3a2fe93e…`、`hotpotqa_5ade1b77…`、`hotpotqa_5a7f66cb…`、`hotpotqa_5ac25035…`、`hotpotqa_5adde708…`、`hotpotqa_5a745a87…`、`2wikimultihopqa_f48d9c60…`。下文主体保留原始证据和历史争议说明；当前裁决以源 annotation 和下面的决议摘要为准。

## 2026-11-03 最终决议摘要

1. `2wikimultihopqa_3a2fe93e…`：English/British 视为等价，English 作为 British 的 alias，并用 Mavis Batey 句 0 显式支持。
2. `hotpotqa_5ade1b77…`：允许“两个点名候选且预设唯一答案”时由证据排除一方确定另一方；结论使用 `presupposition_sets` 和静态 `by_presupposition: true`。
3. `hotpotqa_5a7f66cb…`：事实 unit 改为文档明确点名的 creator/designer 数量，Cranium 2、Auf Achse 1。
4. `hotpotqa_5ac25035…`：事实和结论统一为文档明确列出的不同电影职务数量，Charles Burnett 7、Patricio Guzmán 1。
5. `hotpotqa_5adde708…`：正式名或 common name 中明确含 `plant` 可作为显式类别证据，保留。
6. `hotpotqa_5a745a87…`：两篇定义句都明确含 `private`，共享属性限定清楚，保留。
7. `2wikimultihopqa_f48d9c60…`：u2 明确定义为 Emilio 的 U.S. theatrical release date。

此外，原附录 C 的 5 道单-unit bridge/inference 题均已统一为两跳结构；当前 15 个带 `presupposition_sets` 的 Gold unit 均有静态 `by_presupposition: true`。

| # | sample_id | 数据集 / 题型 | 划分 | 特殊情况 | 复核原因 |
|---|---|---|---|---|---|
| 1 | `2wikimultihopqa_972b911e087f11ebbd6cac1f6bf848b6` | 2wikimultihopqa / bridge_comparison | train | — | 1 原数据可能连错实体：Bharathan 1998 年去世，却被当作 2007 年电影的导演 |
| 2 | `2wikimultihopqa_3118082408e011ebbda1ac1f6bf848b6` | 2wikimultihopqa / bridge_comparison | train | — | 1 原数据可能连错实体：文档里的 Maurice Campbell 是 1919 年出生的冰壶运动员，不可能导演 1921 年的电影 |
| 3 | `2wikimultihopqa_a73a3fc80bdc11eba7f7acde48001122` | 2wikimultihopqa / compositional | train | unreachable | 1 原数据可能连错实体：文档里的 Michael Simon 是 DJ，没说他导过电影；“from Hamburg”是否算出生地也待定 |
| 4 | `hotpotqa_5ab298ff554299340b52552a` | hotpotqa / comparison | dev | unreachable | 2 规则待定：Saroyan 的国籍只能从成长地推断，结论永远答不完，是否保留 |
| 5 | `hotpotqa_5a8af03c55429950cd6afc19` | hotpotqa / comparison | train | unreachable | 2 规则待定：Strayer 的族裔原文没写，结论永远答不完，是否保留 |
| 6 | `hotpotqa_5a7fab3a5542995d8a8ddeea` | hotpotqa / comparison | dev | unreachable | 2 规则待定：unit 定义成乐队成员的国籍还是乐队的国籍 |
| 7 | `hotpotqa_5a8661f85542991e7718162b` | hotpotqa / comparison | train | unreachable | 2 规则待定：“Which, or both”算不算点名候选 |
| 8 | `hotpotqa_5a75b40f5542992d0ec05fe6` | hotpotqa / comparison | train | unreachable | 2 规则待定：“both … what type”这类问题能否用预设 |
| 9 | `2wikimultihopqa_2f75b4620bb011ebab90acde48001122` | 2wikimultihopqa / inference | dev | unreachable | 2 规则待定：“son or nephew”不算明确陈述，结论永远答不完，起草者建议退回 |
| 10 | `2wikimultihopqa_3a2fe93e0bda11eba7f7acde48001122` | 2wikimultihopqa / compositional | dev | unreachable | 2 规则待定：原文写 English，源答案是 British，两者算不算同一个值 |
| 11 | `hotpotqa_5ade1b7755429975fa854e55` | hotpotqa / comparison | train | unreachable | 2 规则待定：输家的事实明确、赢家的不明确时，能否用排除法 |
| 12 | `hotpotqa_5a7f66cb55429969796c1a32` | hotpotqa / comparison | train | — | 3 靠数列表项来比较（哪款游戏的创作者更多） |
| 13 | `hotpotqa_5a84fd2a5542994c784ddabb` | hotpotqa / comparison | train | by_omission | 3 靠数列表项来比较（谁演奏的乐器更多），和已退回的 2Wiki 同类题标准不一致；“演奏乐器”算不算职业也待定 |
| 14 | `hotpotqa_5ac250355542992f1f2b384b` | hotpotqa / comparison | train | — | 3 靠数列表项来比较（谁的电影职务更多样），把定义句当作完整列表 |
| 15 | `hotpotqa_5adde7085542990dbb2f7f01` | hotpotqa / comparison | train | — | 4 证据偏弱：只靠俗名“radiator plant”认定 Peperomia 是植物 |
| 16 | `hotpotqa_5ae0c1c25542993d6555ec43` | hotpotqa / comparison | train | by_omission | 4 证据偏弱：由“all-Finnish line-up”推出 Kotipelto 是芬兰人 |
| 17 | `2wikimultihopqa_b87b12700bdd11eba7f7acde48001122` | 2wikimultihopqa / compositional | train | — | 4 证据偏弱：由“in Chinese history”推出 Huo Guang 是中国人 |
| 18 | `hotpotqa_5adcdfe05542992c1e3a2448` | hotpotqa / bridge | train | — | 4 证据偏弱：赛道在 Ogilvie“附近”，而且问题把赛车称为“爱好” |
| 19 | `hotpotqa_5ae1fe0b5542997283cd2317` | hotpotqa / bridge | train | — | 5 问题有瑕疵：Huntsville 跨 Madison 和 Limestone 两个县 |
| 20 | `hotpotqa_5a745a8755429979e288291e` | hotpotqa / comparison | dev | — | 5 问题有瑕疵：“both what”指代不明 |
| 21 | `hotpotqa_5ab5b95d554299637185c5f8` | hotpotqa / bridge | train | — | 5 问题有瑕疵：“got her start”可以理解成电影出道，也可以理解成拍广告起步 |
| 22 | `hotpotqa_5ab6a56d554299110f219a46` | hotpotqa / comparison | train | — | 5 问题有瑕疵：“产品是否相似”需要主观判断 |
| 23 | `2wikimultihopqa_4f103f2e0bdb11eba7f7acde48001122` | 2wikimultihopqa / compositional | dev | — | 5 问题有瑕疵：乐队还得过其他奖项，可能有别的正确答案 |
| 24 | `hotpotqa_5ac561725542993e66e823ad` | hotpotqa / bridge | train | — | 5 问题有瑕疵：问题把原文的两件事合成了一句 |
| 25 | `hotpotqa_5a72253f55429971e9dc92e5` | hotpotqa / comparison | train | — | 5 问题有瑕疵：问题说“六次大满贯”，但文档里的次数对不上，也没有 unit 检查这个前提 |
| 26 | `2wikimultihopqa_f48d9c60093011ebbdaeac1f6bf848b6` | 2wikimultihopqa / comparison | dev | — | 6 证据有多种解读：Emilio 原文写的是 2008 年的电影、2016 年上映 |
| 27 | `2wikimultihopqa_3addeb19089411ebbd75ac1f6bf848b6` | 2wikimultihopqa / bridge_comparison | train | — | 6 证据有多种解读：电影有两位导演，只按其中一位计算 |
| 28 | `2wikimultihopqa_812e515c0baf11ebab90acde48001122` | 2wikimultihopqa / inference | dev | unreachable | 7 已处理：“probably the son of”已改为没有证据，请确认 |

---

## 第 1 题：`2wikimultihopqa_972b911e087f11ebbd6cac1f6bf848b6`

- 数据集 / 题型：2wikimultihopqa / bridge_comparison（unit 构造类型 bridge_comparison）
- 划分：train；特殊情况：无
- 问题：Are both director of film Irish For Luck and director of film Azhagiya Tamil Magan from the same country?
- 源答案：no

### 复核原因

**1 原数据可能连错实体：Bharathan 1998 年去世，却被当作 2007 年电影的导演**

> Possible entity mismatch: Azhagiya Tamil Magan is a 2007 film, but the Bharathan document says he died in 1998. 2Wiki links the name; kept as draft for human review.

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | director of film Irish for Luck | false | Arthur B. Woods （Arthur Bickerstaffe Woods） | — |
| u2 | country descriptor of {u1} | false | British （English） | u1 |
| u3 | director of film Azhagiya Tamil Magan | false | Bharathan | — |
| u4 | country descriptor of {u3} | false | Indian （India） | u3 |
| u5 | whether the directors of Irish for Luck and Azhagiya Tamil Magan are from the same country | true | no | u2, u4 |

**u1 证据**
- support 第 1 组：
  - `d5s1` (Irish for Luck) Made at Teddington Studios by the British subsidiary of Warner Brothers, it was directed by Arthur B. Woods and starred Athene Seyler, Margaret Lockwood and Patric Knowles.

**u2 证据**
- support 第 1 组：
  - `d10s3` (Arthur B. Woods) By the end of the 1930s Woods was gaining a reputation as one of Britain's most promising and versatile young directors, but put his career on hold to volunteer for war service in the Royal Air Force, the only British film director to do so.
- support 第 2 组：
  - `d10s0` (Arthur B. Woods) Arthur Bickerstaffe Woods( 17 August 1904 – 8 February 1944) was an English film director with 27 credits between 1933 and 1940.

**u3 证据**
- support 第 1 组：
  - `d6s0` (Azhagiya Tamil Magan) Azhagiya Tamil Magan( Handsome Tamil son) is a 2007 Indian Tamil- language action film directed by Bharathan, written by S. K. Jeeva and produced by Swargachitra Appachan.

**u4 证据**
- support 第 1 组：
  - `d4s0` (Bharathan) Bharathan( 14 November 1946 – 30 July 1998) was an Indian film maker, artist, and art director.

**u5 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Bridge comparison (yes/no): director and country descriptor per film, then a conclusion unit.
- u2: Arthur B. Woods sentence 3 ('the only British film director to do so') states British; sentence 0 says 'English film director'. Both accepted (English as alias); either differs from Indian.
- u4: Bharathan sentence 0 'Indian film maker'; sentence 5 (born in Kerala, India) is a birthplace and not used. Source triple form 'India' kept as alias.
- Possible entity mismatch: Azhagiya Tamil Magan is a 2007 film, but the Bharathan document says he died in 1998. 2Wiki links the name; kept as draft for human review.

### 全部文档（`*` = gold 引用的句子）

**d1：Peter Levin**
- `d1s0` Peter Levin is an American director of film, television and theatre.

**d2：Ben Cura**
- `d2s0` Ben Cura( born 30 September 1988) is a British- Argentine actor and director of film, television and theatre.

**d3：Ian Barry (director)**
- `d3s0` Ian Barry is an Australian director of film and TV.

**d4：Bharathan**
- *`d4s0` Bharathan( 14 November 1946 – 30 July 1998) was an Indian film maker, artist, and art director.
- `d4s1` Bharathan is noted for being the founder of a new school of film making in Malayalam cinema, along with Padmarajan and K. G. George, in the 1980s, which created films that were widely received while also being critically acclaimed.
- `d4s2` Known for his unconventional works, he is widely regarded as one of the greatest film makers in the Indian Film Industry of all time.
- `d4s3` Bharathan is among one of the directors who revolutionised Malayalam Cinema.
- `d4s4` A train of directors, and screenwriters followed this school onto the 1990s including Sibi Malayil, Kamal, Lohithadas and Jayaraj.
- `d4s5` He was born at Engakkadu near Wadakkancherry, in present- day Thrissur district of Kerala, India.

**d5：Irish for Luck**
- `d5s0` Irish for Luck is a 1936 British comedy film, also known as Meet the Duchess.
- *`d5s1` Made at Teddington Studios by the British subsidiary of Warner Brothers, it was directed by Arthur B. Woods and starred Athene Seyler, Margaret Lockwood and Patric Knowles.
- `d5s2` Adapted from a novel by L.A.G. Strong, in the film an impoverished Irish Duchess tries to survive on her small income.

**d6：Azhagiya Tamil Magan**
- *`d6s0` Azhagiya Tamil Magan( Handsome Tamil son) is a 2007 Indian Tamil- language action film directed by Bharathan, written by S. K. Jeeva and produced by Swargachitra Appachan.
- `d6s1` The film stars actor Vijay in a dual role for the first time in his career as the hero and villain, while Shriya Saran, Namitha Vankawala, and N. Santhanam play in supporting roles.
- `d6s2` With cinematography by K. Balasubramaniam and editing by Anthony, the film's score and soundtrack is composed by A. R. Rahman.
- `d6s3` The film was dubbed in Malayalam with the same title, in Hindi as" Sabse Bada Khiladi", and in Telugu as" Maha Muduru".
- `d6s4` The film revolves around an excelling athlete who has the ability to predict future events.
- `d6s5` With his unique ability, he identifies several future events, including the attempted murder of his lover by a look- alike.
- `d6s6` The film was released on 8 November 2007 and distributed worldwide by Pyramid Saimira.
- `d6s7` The film collected$ 1,043,064 at the overseas box office in 2007.
- `d6s8` The film's financial performance was above average.

**d7：Hanro Smitsman**
- `d7s0` Hanro Smitsman, born in 1967 in Breda( Netherlands), is a writer and director of film and television.

**d8：Brian Johnson (special effects artist)**
- `d8s0` Brian Johnson( born 1939 or 1940) is a British designer and director of film and television special effects.

**d9：Jason Moore (director)**
- `d9s0` Jason Moore( born October 22, 1970) is an American director of film, theatre and television.

**d10：Arthur B. Woods**
- *`d10s0` Arthur Bickerstaffe Woods( 17 August 1904 – 8 February 1944) was an English film director with 27 credits between 1933 and 1940.
- `d10s1` Woods' films were mainly quota quickies but were diverse in style, from light comedy and musicals to dark crime thrillers.
- `d10s2` His most acclaimed film is 1938's" They Drive by Night".
- *`d10s3` By the end of the 1930s Woods was gaining a reputation as one of Britain's most promising and versatile young directors, but put his career on hold to volunteer for war service in the Royal Air Force, the only British film director to do so.
- `d10s4` He was killed while on active service in February 1944, leaving his potential largely unfulfilled.

### 由这道题生成的 SFT 样本（10 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=2 | d1, d6 | u1 —; u2 —; u3 ✅ Bharathan ← d6s0; u4 —; u5 — |
| sftorder1 t=3 | d1, d6, d5 | u1 ✅ Arthur B. Woods ← d5s1; u2 —; u3 ✅ Bharathan ← d6s0; u4 —; u5 — |
| sftorder1 t=5 | d1, d6, d5, d7, d2 | u1 ✅ Arthur B. Woods ← d5s1; u2 —; u3 ✅ Bharathan ← d6s0; u4 —; u5 — |
| sftorder1 t=7 | d1, d6, d5, d7, d2, d8, d4 | u1 ✅ Arthur B. Woods ← d5s1; u2 —; u3 ✅ Bharathan ← d6s0; u4 ✅ Indian ← d4s0; u5 — |
| sftorder1 t=10 | d1, d6, d5, d7, d2, d8, d4, d9, d10, d3 | u1 ✅ Arthur B. Woods ← d5s1; u2 ✅ British ← d10s3; u3 ✅ Bharathan ← d6s0; u4 ✅ Indian ← d4s0; u5 ✅ no ← d10s3,d4s0 |
| sftorder2 t=4 | d7, d4, d2, d6 | u1 —; u2 —; u3 ✅ Bharathan ← d6s0; u4 ✅ Indian ← d4s0; u5 — |
| sftorder2 t=5 | d7, d4, d2, d6, d3 | u1 —; u2 —; u3 ✅ Bharathan ← d6s0; u4 ✅ Indian ← d4s0; u5 — |
| sftorder2 t=9 | d7, d4, d2, d6, d3, d5, d9, d8, d10 | u1 ✅ Arthur B. Woods ← d5s1; u2 ✅ British ← d10s3; u3 ✅ Bharathan ← d6s0; u4 ✅ Indian ← d4s0; u5 ✅ no ← d10s3,d4s0 |
| sftorder3 t=3 | d5, d7, d6 | u1 ✅ Arthur B. Woods ← d5s1; u2 —; u3 ✅ Bharathan ← d6s0; u4 —; u5 — |
| sftorder3 t=6 | d5, d7, d6, d9, d3, d4 | u1 ✅ Arthur B. Woods ← d5s1; u2 —; u3 ✅ Bharathan ← d6s0; u4 ✅ Indian ← d4s0; u5 — |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 2 题：`2wikimultihopqa_3118082408e011ebbda1ac1f6bf848b6`

- 数据集 / 题型：2wikimultihopqa / bridge_comparison（unit 构造类型 bridge_comparison）
- 划分：train；特殊情况：无
- 问题：Which film has the director who was born first, Two Weeks with Pay or Woman-Wise?
- 源答案：Woman-Wise

### 复核原因

**1 原数据可能连错实体：文档里的 Maurice Campbell 是 1919 年出生的冰壶运动员，不可能导演 1921 年的电影**

> Possible entity mismatch: the Maurice Campbell document is a Canadian curler born 1919, who cannot have directed a 1921 film. 2Wiki links the name; per the documents the answer Woman-Wise holds (1885 vs 1919). If the real director was born before April 1885, the source answer would be wrong. Kept as draft for human review.

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | director of film Two Weeks with Pay | false | Maurice Campbell | — |
| u2 | date of birth of {u1} | false | November 28, 1919 | u1 |
| u3 | director of film Woman-Wise | false | Allan Dwan | — |
| u4 | date of birth of {u3} | false | 3 April 1885 | u3 |
| u5 | which of the two films has the director born first, Two Weeks with Pay or Woman-Wise | true | Woman-Wise | u2, u4 |

**u1 证据**
- support 第 1 组：
  - `d9s0` (Two Weeks with Pay) Two Weeks with Pay is a lost 1921 American silent comedy romance film starring Bebe Daniels and directed by Maurice Campbell.

**u2 证据**
- support 第 1 组：
  - `d4s0` (Maurice Campbell) Maurice Campbell( November 28, 1919 – July 4, 2014) was a Canadian curler from Trois- Rivières, Quebec.
- support 第 2 组：
  - `d4s1` (Maurice Campbell) Campbell was born November 28, 1919 in Saint- Hyacinthe, Quebec.

**u3 证据**
- support 第 1 组：
  - `d1s0` (Woman-Wise) Woman- Wise is a 1937 American crime film directed by Allan Dwan and written by Ben Markson.

**u4 证据**
- support 第 1 组：
  - `d5s0` (Allan Dwan) Allan Dwan (3 April 1885 – 28 December 1981) was a pioneering Canadian-born American motion picture director, producer, and screenwriter.

**u5 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Bridge comparison: director and birth date per film, then a conclusion comparing the birth dates.
- u2: Maurice Campbell sentence 1 ('Campbell was born November 28, 1919') added as alternative support.
- Possible entity mismatch: the Maurice Campbell document is a Canadian curler born 1919, who cannot have directed a 1921 film. 2Wiki links the name; per the documents the answer Woman-Wise holds (1885 vs 1919). If the real director was born before April 1885, the source answer would be wrong. Kept as draft for human review.
- Woman Wise (1928 film, directed by Albert Ray) is a different film from Woman-Wise (1937); not used and not an alias.

### 全部文档（`*` = gold 引用的句子）

**d1：Woman-Wise**
- *`d1s0` Woman- Wise is a 1937 American crime film directed by Allan Dwan and written by Ben Markson.
- `d1s1` The film stars Rochelle Hudson, Michael Whalen, Thomas Beck, Alan Dinehart, Douglas Fowley and George Hassell.
- `d1s2` The film was released on January 22, 1937, by 20th Century Fox.

**d2：Wale Adebanwi**
- `d2s0` Wale Adebanwi( born 1969) is a Nigerian- born first Black Rhodes Professor at St Antony's College, Oxford.

**d3：Henry Moore (cricketer)**
- `d3s0` Henry Walter Moore( 1849 – 20 August 1916) was an English- born first- class cricketer who spent most of his life in New Zealand.

**d4：Maurice Campbell**
- *`d4s0` Maurice Campbell( November 28, 1919 – July 4, 2014) was a Canadian curler from Trois- Rivières, Quebec.
- *`d4s1` Campbell was born November 28, 1919 in Saint- Hyacinthe, Quebec.
- `d4s2` Educated at the University of Montreal, he joined the Royal Canadian Army Medical Corps in 1943 and completed his medical degree in 1945 and was subsequently posted in Halifax, Nova Scotia.
- `d4s3` He was a specialist in rheumatology and internal medicine and practiced in Cap- de- la- Madeleine, Quebec.
- `d4s4` Campbell played in the 1958 Macdonald Brier, playing lead for the Quebec team, skipped by Bob Lahaie.
- `d4s5` The team finished 9th, with a 3- 7 record.
- `d4s6` He was President of the Quebec Curling Association for the 1963- 64 season.
- `d4s7` He served as president of the Canadian Curling Association for the 1970- 71 season and was named to the Canadian Curling Hall of Fame.
- `d4s8` Campbell died in Trois- Rivières on July 4, 2014.

**d5：Allan Dwan**
- *`d5s0` Allan Dwan (3 April 1885 – 28 December 1981) was a pioneering Canadian-born American motion picture director, producer, and screenwriter.

**d6：Rumbi Katedza**
- `d6s0` Rumbi Katedza is a Zimbabwean Film Producer and Director who was born on 17 January 1974.

**d7：Woman Wise**
- `d7s0` Woman Wise is a 1928 American silent comedy drama film directed by Albert Ray and starring William Russell, June Collyer and Walter Pidgeon.

**d8：Hartley Lobban**
- `d8s0` Hartley W Lobban (9 May 1926 – 15 October 2004) was a Jamaican-born first-class cricketer who played 17 matches for Worcestershire in the early 1950s.

**d9：Two Weeks with Pay**
- *`d9s0` Two Weeks with Pay is a lost 1921 American silent comedy romance film starring Bebe Daniels and directed by Maurice Campbell.

**d10：Hassan Zee**
- `d10s0` Hassan Zee is a Pakistani- American film director who was born in Chakwal, Pakistan.

### 由这道题生成的 SFT 样本（10 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=1 | d4 | u1 —; u2 —; u3 —; u4 —; u5 — |
| sftorder1 t=5 | d4, d8, d3, d2, d1 | u1 —; u2 —; u3 ✅ Allan Dwan ← d1s0; u4 —; u5 — |
| sftorder1 t=6 | d4, d8, d3, d2, d1, d5 | u1 —; u2 —; u3 ✅ Allan Dwan ← d1s0; u4 ✅ 3 April 1885 ← d5s0; u5 — |
| sftorder1 t=10 | d4, d8, d3, d2, d1, d5, d9, d6, d10, d7 | u1 ✅ Maurice Campbell ← d9s0; u2 ✅ November 28, 1919 ← d4s0; u3 ✅ Allan Dwan ← d1s0; u4 ✅ 3 April 1885 ← d5s0; u5 ✅ Woman-Wise ← d4s0,d5s0 |
| sftorder2 t=7 | d8, d5, d7, d10, d2, d1, d3 | u1 —; u2 —; u3 ✅ Allan Dwan ← d1s0; u4 ✅ 3 April 1885 ← d5s0; u5 — |
| sftorder2 t=8 | d8, d5, d7, d10, d2, d1, d3, d9 | u1 ✅ Maurice Campbell ← d9s0; u2 —; u3 ✅ Allan Dwan ← d1s0; u4 ✅ 3 April 1885 ← d5s0; u5 — |
| sftorder3 t=2 | d3, d9 | u1 ✅ Maurice Campbell ← d9s0; u2 —; u3 —; u4 —; u5 — |
| sftorder3 t=5 | d3, d9, d6, d10, d1 | u1 ✅ Maurice Campbell ← d9s0; u2 —; u3 ✅ Allan Dwan ← d1s0; u4 —; u5 — |
| sftorder3 t=6 | d3, d9, d6, d10, d1, d5 | u1 ✅ Maurice Campbell ← d9s0; u2 —; u3 ✅ Allan Dwan ← d1s0; u4 ✅ 3 April 1885 ← d5s0; u5 — |
| sftorder3 t=7 | d3, d9, d6, d10, d1, d5, d4 | u1 ✅ Maurice Campbell ← d9s0; u2 ✅ November 28, 1919 ← d4s0; u3 ✅ Allan Dwan ← d1s0; u4 ✅ 3 April 1885 ← d5s0; u5 ✅ Woman-Wise ← d4s0,d5s0 |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 3 题：`2wikimultihopqa_a73a3fc80bdc11eba7f7acde48001122`

- 数据集 / 题型：2wikimultihopqa / compositional（unit 构造类型 bridge）
- 划分：train；特殊情况：unreachable
- 问题：Where was the director of film The Love Patient born?
- 源答案：Hamburg

### 复核原因

**1 原数据可能连错实体：文档里的 Michael Simon 是 DJ，没说他导过电影；“from Hamburg”是否算出生地也待定**

> Further caveat: the DJ article does not say he directed films; linking it to The Love Patient's director rests on the shared name only (as in the source triples).

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | director of film The Love Patient | false | Michael Simon | — |
| u2 | place of birth of {u1} | true | Hamburg | u1 |

**u1 证据**
- support 第 1 组：
  - `d10s0` (The Love Patient) The Love Patient is a 2011 gay-themed romantic comedy written and directed by Michael Simon, released to festivals in 2011, and on DVD in 2012.

**u2 证据**
- `[]`：原文没有明确陈述

**起草备注**

- Bridge: director (optional) then birthplace (necessary).
- no explicit support: Michael Simon (DJ) 0 says he is 'a German DJ and musician from Hamburg'; 'from Hamburg' does not state the birthplace, so u2 has support_sets [].
- Further caveat: the DJ article does not say he directed films; linking it to The Love Patient's director rests on the shared name only (as in the source triples).

### 全部文档（`*` = gold 引用的句子）

**d1：Olav Aaraas**
- `d1s0` Olav Aaraas( born 10 July 1950) is a Norwegian historian and museum director.
- `d1s1` He was born in Fredrikstad.
- `d1s2` From 1982 to 1993 he was the director of Sogn Folk Museum, from 1993 to 2010 he was the director of Maihaugen and from 2001 he has been the director of the Norwegian Museum of Cultural History.
- `d1s3` In 2010 he was decorated with the Royal Norwegian Order of St. Olav.

**d2：Brian Kennedy (gallery director)**
- `d2s0` Brian Patrick Kennedy( born 5 November 1961) is an Irish- born art museum director who has worked in Ireland and Australia, and now lives and works in the United States.
- `d2s1` He is currently the director of the Peabody Essex Museum.
- `d2s2` He was the director of the Toledo Museum of Art in Ohio from 2010 to 2019.
- `d2s3` He was the director of the Hood Museum of Art from 2005 to 2010, and the National Gallery of Australia( Canberra) from 1997- 2004.

**d3：Michael Simon (DJ)**
- `d3s0` Michael Simon( born August 29, 1972) is a German DJ and musician from Hamburg, and a member of the band Scooter.

**d4：Georges Patient**
- `d4s0` Georges Patient( born 1 April 1949) is a member of the Senate of France, representing the territory of French Guiana.
- `d4s1` He is a member of the Socialist Party.

**d5：Dana Blankstein**
- `d5s0` Dana Blankstein- Cohen( born March 3, 1981) is the director of the Israeli Academy of Film and Television.
- `d5s1` She is a film director, and an Israeli culture entrepreneur.

**d6：Jesse E. Hobson**
- `d6s0` Jesse Edward Hobson( May 2, 1911 – November 5, 1970) was the director of SRI International from 1947 to 1955.
- `d6s1` Prior to SRI, he was the director of the Armour Research Foundation.

**d7：Ian Barry (director)**
- `d7s0` Ian Barry is an Australian director of film and TV.

**d8：S. N. Mathur**
- `d8s0` S.N. Mathur was the Director of the Indian Intelligence Bureau between September 1975 and February 1980.
- `d8s1` He was also the Director General of Police in Punjab.

**d9：Peter Levin**
- `d9s0` Peter Levin is an American director of film, television and theatre.

**d10：The Love Patient**
- *`d10s0` The Love Patient is a 2011 gay-themed romantic comedy written and directed by Michael Simon, released to festivals in 2011, and on DVD in 2012.

### 由这道题生成的 SFT 样本（5 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=4 | d8, d6, d4, d10 | u1 ✅ Michael Simon ← d10s0; u2 — |
| sftorder1 t=10 | d8, d6, d4, d10, d3, d1, d2, d5, d9, d7 | u1 ✅ Michael Simon ← d10s0; u2 — |
| sftorder2 t=3 | d1, d9, d10 | u1 ✅ Michael Simon ← d10s0; u2 — |
| sftorder3 t=1 | d6 | u1 —; u2 — |
| sftorder3 t=3 | d6, d2, d9 | u1 —; u2 — |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 4 题：`hotpotqa_5ab298ff554299340b52552a`

- 数据集 / 题型：hotpotqa / comparison（unit 构造类型 comparison）
- 划分：dev；特殊情况：unreachable
- 问题：Peter Boghossian and Strawberry Saroyan, are of which mutual nationality?
- 源答案：American

### 复核原因

**2 规则待定：Saroyan 的国籍只能从成长地推断，结论永远答不完，是否保留**

> No explicit support for u2: Strawberry Saroyan sentence 1 says she spent her childhood in Bolinas, California; nationality from a childhood place is an inference. Sentence 0 ('journalist and author') lists no nationality. The conclusion therefore can never be SUPPORTED (open point).

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | nationality of Peter Boghossian | false | American | — |
| u2 | nationality of Strawberry Saroyan | false | American | — |
| u3 | nationality shared by Peter Boghossian and Strawberry Saroyan | true | American | u1, u2 |

**u1 证据**
- support 第 1 组：
  - `d4s0` (Peter Boghossian) Peter Gregory Boghossian (born July 25, 1966) is an American philosopher and atheism advocate.

**u2 证据**
- `[]`：原文没有明确陈述

**u3 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Comparison (shared nationality): two fact units plus a conclusion unit; no presupposition (shared-value question).
- No explicit support for u2: Strawberry Saroyan sentence 1 says she spent her childhood in Bolinas, California; nationality from a childhood place is an inference. Sentence 0 ('journalist and author') lists no nationality. The conclusion therefore can never be SUPPORTED (open point).
- Strawberry Saroyan sentence 1 removed from support.

### 全部文档（`*` = gold 引用的句子）

**d1：Peter Scot**
- `d1s0` Peter Scot is a brand of Indian whisky, manufactured by Khoday India Limited (KIL), and launched in May 1968.
- `d1s1` It is a flagship brand of the company and is manufactured at their Bangalore facility.
- `d1s2` In "Khoday Distilleries Limited vs. The Scotch Whisky Association and Others", Peter Warren, an employee of Khoday, told the Supreme Court of India that the brand name Peter Scot was made up using his father's first name, "Peter", and his nationality, "Scot".
- `d1s3` Another factor in choosing the name was due to the British explorer, Captain Scott, and his son Peter Scott.
- `d1s4` Although the name "Scott" is spelt with two t's, it is phonetically the same as the word Scot.
- `d1s5` The brand's main competitors are Pernod Ricard's Blenders Pride and United Spirits Limited's Royal Challenge.

**d2：Fragmentation (sociology)**
- `d2s0` In urban sociology, fragmentation refers to the absence or the underdevelopment of connections between the society and the groupings of some members of that society on the lines of a common culture, nationality, race, language, occupation, religion, income level, or other common interests.
- `d2s1` This gap between the concerned group and the rest might be social, indicating poor interrelationships among each other; economical based on structural inequalities; institutional in terms of formal and specific political, occupational, educative or associative organizations and/or geographic implying regional or residential concentration.
- `d2s2` bell hooks coined the term when addressing the problem of 'hierarchy of oppression' within the feminist movement; where some felt experiencing more types of oppression gave greater validity to one's opinion and, therefore undermined group strength and solidarity within the movement as much as non-interscectional identity did in the 1970s [where female identity was seen predominantly through the lens of white, middle-class women and didn't take into consideration that identity could be made up of many more cultural influences such as race, gender, sexuality, spirituality etc. all intersecting across points of privilege and oppression].
- `d2s3` hooks argued for greater inclusivity, mutual support and an understanding of various types of feminism within the movement; each sharing the same equity goals, yet having different ideas on the methods to achieve such goals.

**d3：Peter C. Clapman**
- `d3s0` Peter C. Clapman is the current CEO of Governance for Owners USA Inc, previously served as Senior Vice President & Chief Counsel for TIAA-CREF for 32 years.
- `d3s1` He serves on multiple boards and committees, including the Committee on Capital Markets Regulation, the AARP Mutual Funds Board of Trustees, the Board of Directors at iPass and the Conference of Fund Leaders; a joint initiative of the Yale Center and Mutual Fund Directors Forum.

**d4：Peter Boghossian**
- *`d4s0` Peter Gregory Boghossian (born July 25, 1966) is an American philosopher and atheism advocate.
- `d4s1` He is Assistant Professor of Philosophy at Portland State University.
- `d4s2` His primary research areas are critical thinking, philosophy of education, and moral reasoning.
- `d4s3` Boghossian is a speaker for the Center for Inquiry, the Richard Dawkins Foundation for Reason and Science, and the Secular Student Alliance.
- `d4s4` He has been nominated as a member of the Global Secular Council.

**d5：Strawberry Jam Comics**
- `d5s0` Strawberry Jam Comics was a Canadian publisher of comic books during the black-and-white comics boom of the mid and late 1980s.
- `d5s1` Inspired by the creative success of Dave Sim's "Cerebus the Aardvark", founders Paul Stockton and Derek McCulloch launched Strawberry Jam with the publication of "To Be Announced" #1 in 1985.
- `d5s2` The commercial success of Kevin Eastman and Peter Laird's "Teenage Mutant Ninja Turtles" provided further inspiration.

**d6：Peter Lynch**
- `d6s0` Peter Lynch (born January 19, 1944) is an American investor, mutual fund manager, and philanthropist.
- `d6s1` As the manager of the Magellan Fund at Fidelity Investments between 1977 and 1990, Lynch averaged a 29.2% annual return, consistently more than doubling the S&P 500 market index and making it the best performing mutual fund in the world.
- `d6s2` During his tenure, assets under management increased from $18 million to $14 billion.

**d7：Mutual Aid: A Factor of Evolution**
- `d7s0` Mutual Aid: A Factor of Evolution is a 1902 essay collection by Russian anarchist philosopher Peter Kropotkin.
- `d7s1` The essays, initially published in the English periodical "The Nineteenth Century" between 1890 and 1896, explore the role of mutually-beneficial cooperation and reciprocity (or "mutual aid") in the animal kingdom and human societies both past and present.
- `d7s2` It is an argument against the competition-centred theories of so-called social Darwinism, as well as the romantic depictions of cooperation presented by writers such as Jean-Jacques Rousseau, who argued it was motivated by universal love rather than self-interest.
- `d7s3` "Mutual Aid" is considered a fundamental text in anarchist communism, presenting a scientific basis for communism alternative to the historical materialism of the Marxists.
- `d7s4` Many biologists also consider it an important catalyst in the scientific study of cooperation.

**d8：Strawberry Saroyan**
- `d8s0` Strawberry Saroyan (born 1970) is a journalist and author.
- `d8s1` The daughter of Aram Saroyan and granddaughter of playwright William Saroyan and actress Carol Matthau, she spent her childhood in Bolinas, California.
- `d8s2` She has a sister named Cream.
- `d8s3` She writes for the New York Times Style section and is the author of "".

**d9：Our Mutual Friend (1976 TV serial)**
- `d9s0` Our Mutual Friend is a 1976 British television serial adapted from the Charles Dickens novel "Our Mutual Friend".
- `d9s1` The series was made by the BBC and ran during 1976 for a total of seven episodes.
- `d9s2` It was directed by Peter Hammond.

**d10：Petrović**
- `d10s0` Petrović (or Petrovich) is a Slavic last and second name, found in countries with Slavic populations.
- `d10s1` Examples of such countries are: Croatia, Serbia, Montenegro, Bosnia and Herzegovina, Slovenia, Macedonia and Russia.
- `d10s2` This surname or last name is not tied to any nationality.
- `d10s3` It is normal Slavic surname deriving from "Petar", which is equivalent to Peter in English.
- `d10s4` The part "ov" designates possession: "Petrov" means "Peter's".
- `d10s5` The suffix "ić" is a diminutive designation, or descendant designation.
- `d10s6` So, the last name can be translated as "Peter's son", equivalent to the English last name of Peterson.

### 由这道题生成的 SFT 样本（6 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=3 | d9, d10, d3 | u1 —; u2 —; u3 — |
| sftorder1 t=4 | d9, d10, d3, d4 | u1 ✅ American ← d4s0; u2 —; u3 — |
| sftorder1 t=7 | d9, d10, d3, d4, d8, d7, d1 | u1 ✅ American ← d4s0; u2 —; u3 — |
| sftorder1 t=10 | d9, d10, d3, d4, d8, d7, d1, d5, d2, d6 | u1 ✅ American ← d4s0; u2 —; u3 — |
| sftorder2 t=4 | d6, d5, d7, d4 | u1 ✅ American ← d4s0; u2 —; u3 — |
| sftorder3 t=6 | d8, d9, d5, d10, d7, d4 | u1 ✅ American ← d4s0; u2 —; u3 — |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 5 题：`hotpotqa_5a8af03c55429950cd6afc19`

- 数据集 / 题型：hotpotqa / comparison（unit 构造类型 comparison）
- 划分：train；特殊情况：unreachable
- 问题：Are Charles Burnett and Frank R. Strayer both African-Americans?
- 源答案：no

### 复核原因

**2 规则待定：Strayer 的族裔原文没写，结论永远答不完，是否保留**

> No explicit support for u2: Frank R. Strayer sentence 0 ('an actor, film writer, director and producer') lists no nationality or ethnicity, so Exception 2 condition 3 fails. Film sentences call his films 'American', which says nothing about his ethnicity. The conclusion therefore can never be SUPPORTED (open point).

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | whether Charles Burnett is African-American | false | yes | — |
| u2 | whether Frank R. Strayer is African-American | false | no | — |
| u3 | whether Charles Burnett and Frank R. Strayer are both African-Americans | true | no | u1, u2 |

**u1 证据**
- support 第 1 组：
  - `d4s0` (Charles Burnett (director)) Charles Burnett (born April 13, 1944, in Vicksburg, Mississippi) is an African-American film director, film producer, writer, editor, actor, photographer, and cinematographer.

**u2 证据**
- `[]`：原文没有明确陈述

**u3 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Comparison (yes/no 'both'): two fact units plus a conclusion unit.
- No explicit support for u2: Frank R. Strayer sentence 0 ('an actor, film writer, director and producer') lists no nationality or ethnicity, so Exception 2 condition 3 fails. Film sentences call his films 'American', which says nothing about his ethnicity. The conclusion therefore can never be SUPPORTED (open point).
- Frank R. Strayer sentence 0 removed from support.

### 全部文档（`*` = gold 引用的句子）

**d1：Blondie in Society**
- `d1s0` Blondie in Society is a 1941 black and white comedy film, directed by Frank R. Strayer.
- `d1s1` It is the ninth of the 28 Blondie films.

**d2：Blondie Takes a Vacation**
- `d2s0` Blondie Takes a Vacation is a 1939 black-and-white comedy film, directed by Frank R. Strayer.
- `d2s1` The film is based on Chic Young's comic strip of the same name.

**d3：Blondie's Blessed Event**
- `d3s0` Blondie's Blessed Event is a 1942 black and white comedy film, directed by Frank R. Strayer.
- `d3s1` It is the eleventh of the Blondie films.

**d4：Charles Burnett (director)**
- *`d4s0` Charles Burnett (born April 13, 1944, in Vicksburg, Mississippi) is an African-American film director, film producer, writer, editor, actor, photographer, and cinematographer.
- `d4s1` His most popular films include "Killer of Sheep" (1978), "My Brother's Wedding" (1983), "To Sleep with Anger" (1990), "The Glass Shield" (1994), and "" (2007).
- `d4s2` He has been involved in other types of motion pictures including shorts, documentaries, and a TV series.

**d5：One in a Million (1934 film)**
- `d5s0` One in a Million is a 1934 American drama film directed by Frank R. Strayer and starring Dorothy Wilson, Charles Starrett and Guinn 'Big Boy' Williams.

**d6：Frank R. Strayer**
- `d6s0` Frank R. Strayer (September 21, 1891 – February 3, 1964) was an actor, film writer, director and producer.
- `d6s1` He was active from the mid-1920s until the early 1950s.

**d7：Just Married (1928 film)**
- `d7s0` Just Married is a 1928 American comedy silent film directed by Frank R. Strayer and written by Frank Butler, George Marion Jr., Adelaide Matthews, Anne Nichols and Gilbert Pratt.
- `d7s1` The film stars James Hall, Ruth Taylor, Harrison Ford, William Austin, Ivy Harris, Tom Ricketts and Maude Turner Gordon.
- `d7s2` The film was released on August 18, 1928, by Paramount Pictures.

**d8：Killer of Sheep**
- `d8s0` Killer of Sheep is a 1978 American drama film written, directed, produced, and shot by Charles Burnett.
- `d8s1` It features Henry G. Sanders, Kaycee Moore, and Charles Bracy, among others.
- `d8s2` The drama depicts the culture of urban African-Americans in Los Angeles' Watts district.
- `d8s3` The film's style is often likened to Italian neorealism.

**d9：Mama Loves Papa (1945 film)**
- `d9s0` Mama Loves Papa is a 1945 American black-and-white comedy film directed by Frank R. Strayer, and written by Monte Brice, with a story by Keene Thompson and a screenplay by Charles E. Roberts, as a loose remake of the 1933 film of the same name written by Douglas MacLean.
- `d9s1` The film was produced by RKO Radio Pictures and stars Leon Errol and Elizabeth Risdon.

**d10：Caught Cheating**
- `d10s0` Caught Cheating is a 1931 American comedy film directed by Frank R. Strayer from a screenplay by W. Scott Darling.
- `d10s1` The film stars Charles Murray, George Sidney, and Nita Martan, and it was released by Tiffany Productions on January 31, 1931.

### 由这道题生成的 SFT 样本（6 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=4 | d7, d8, d3, d4 | u1 ✅ yes ← d4s0; u2 —; u3 — |
| sftorder1 t=7 | d7, d8, d3, d4, d10, d1, d2 | u1 ✅ yes ← d4s0; u2 —; u3 — |
| sftorder1 t=10 | d7, d8, d3, d4, d10, d1, d2, d5, d6, d9 | u1 ✅ yes ← d4s0; u2 —; u3 — |
| sftorder2 t=3 | d10, d8, d4 | u1 ✅ yes ← d4s0; u2 —; u3 — |
| sftorder2 t=9 | d10, d8, d4, d2, d9, d5, d6, d7, d3 | u1 ✅ yes ← d4s0; u2 —; u3 — |
| sftorder3 t=8 | d2, d10, d7, d1, d9, d5, d3, d4 | u1 ✅ yes ← d4s0; u2 —; u3 — |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 6 题：`hotpotqa_5a7fab3a5542995d8a8ddeea`

- 数据集 / 题型：hotpotqa / comparison（unit 构造类型 comparison）
- 划分：dev；特殊情况：unreachable
- 问题：Do the bands The Telescopes and Ubiquitous Synergy Seeker have members of the same nationality?
- 源答案：no

### 复核原因

**2 规则待定：unit 定义成乐队成员的国籍还是乐队的国籍**

> Source supporting facts kept out for that reason. Reviewer may decide to reinterpret the units as the bands' nationality, which would give English vs Canadian with explicit support.

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | nationality of the members of The Telescopes | false | English （British） | — |
| u2 | nationality of the members of Ubiquitous Synergy Seeker | false | Canadian | — |
| u3 | whether The Telescopes and Ubiquitous Synergy Seeker have members of the same nationality | true | no | u1, u2 |

**u1 证据**
- `[]`：原文没有明确陈述

**u2 证据**
- `[]`：原文没有明确陈述

**u3 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Comparison (yes/no): two member-nationality fact units plus a conclusion unit.
- no explicit support: u1 and u2, the documents give only the bands' nationality (The Telescopes 0 'English band'; Ubiquitous Synergy Seeker 0 'Canadian duo', Questamation 0, New World Alphabet 0 'Canadian band'); members' nationality from the band's is inference (rule 4, cf. 'an American film').
- Source supporting facts kept out for that reason. Reviewer may decide to reinterpret the units as the bands' nationality, which would give English vs Canadian with explicit support.

### 全部文档（`*` = gold 引用的句子）

**d1：Advanced Basics**
- `d1s0` Advanced Basics is the third Extended play by Ubiquitous Synergy Seeker.
- `d1s1` The album was funded through crowdsourcing site PledgeMusic, the project was titled "#Letsgetweirdtogether".
- `d1s2` This EP is notable for being the first official USS release outside of Canada.

**d2：Approved (Ubiquitous Synergy Seeker album)**
- `d2s0` Approved is the second EP released by Ubiquitous Synergy Seeker.
- `d2s1` Music videos were released for tracks "Yo Hello Hooray (Everyday)" and "Damini".

**d3：Welding the C:/**
- `d3s0` Welding The C:/ is the first EP released by Ubiquitous Synergy Seeker.
- `d3s1` The album earned the band a fan base when the first single, "Hollow Point Sniper Hyperbole", became popular after being played on alternative radio stations across Ontario, particularly by Toronto's 102.1 The Edge.

**d4：Questamation**
- `d4s0` Questamation, released on Mar 9, 2009, is the first full-length semi-programmed album by Canadian band Ubiquitous Synergy Seeker, alias USS, consisting of Ashley Boo-Schultz on guitar and vocals, and Jason Parsons, aka Human Kebab, on turntables and programming.
- `d4s1` For the recording, USS teamed up with Matthew Wagner (Crystal Castles, Alpha Galates) for production and engineering, as well as with Chris Davies and Charles Topping who 'aided musically'.

**d5：Refugees and asylum in Russia**
- `d5s0` The Russian Federation's Law on Refugees defines who is a refugee for purposes of obtaining asylum in the country.
- `d5s1` The Law defines a refugee as a "person who is outside his/her country of nationality or habitual residence; has a well-founded fear of persecution because of his/her race, religion, nationality, membership in a particular social group or political opinion; and is unable or unwilling to avail himself/herself of the protection of that country, or to return there, for fear of persecution.
- `d5s2` Upon receiving an asylum seeker's application, the Russian Federal Migration Service ("FMS") determines whether the asylum seeker meets the legislative definition of a "refugee" and should be granted asylum.

**d6：The Telescopes**
- `d6s0` The Telescopes are an English noise, space rock, dream pop and psychedelic band, formed in 1987 by Stephen Lawrie, and drawing influence from artists such as Suicide, The Velvet Underground and The 13th Floor Elevators.
- `d6s1` They have a total of six released albums since their debut, "Taste", released in 1989.

**d7：Zoo Legacy**
- `d7s0` Zoo Legacy is a hip-hop/indie-rock band from Ottawa, Ontario, Canada.
- `d7s1` Formed in 2010, the band began as an outlet for brothers Samuel (keyboards, guitars, vocals) and Dominic Goss (guitars).
- `d7s2` After successfully recording a demo of material, the brothers enlisted the talents of friend and local rapper Nicholas Pouponneau in the summer of 2010, who began rapping verses over the instrumental tracks they had previously written.
- `d7s3` They obtained their name by combining the previous stage name of Pouponneau (Young Legacy) and a neighborhood park the Goss brothers spent time in visiting family in South Africa (Zoo Lake).
- `d7s4` Throughout the years, they have shared the stage with acts such as Lauryn Hill, Kardinal Offishall, Classified, Shad, Ubiquitous Synergy Seeker, SonReal and BADBADNOTGOOD.
- `d7s5` Their sound has been likened to acts like The Weeknd, The XX and Atmosphere.

**d8：List of space telescopes**
- `d8s0` This list of space telescopes (astronomical space observatories) is grouped by major frequency ranges: gamma ray, x-ray, ultraviolet, visible, infrared, microwave and radio.
- `d8s1` Telescopes that work in multiple frequency bands are included in all of the appropriate sections.
- `d8s2` Space telescopes that collect particles, such as cosmic ray nuclei and/or electrons, as well as instruments that aim to detect gravitational waves, are also listed.
- `d8s3` Missions with specific targets within the Solar System (e.g. our Sun and its planets), are excluded; see List of Solar System probes for these, and List of Earth observation satellites for missions targeting our planet.

**d9：New World Alphabet**
- `d9s0` New World Alphabet, released on January 13, 2017, is the second studio album by Canadian band Ubiquitous Synergy Seeker, also known as USS.
- `d9s1` It is the first studio album since their debut album Questamation, released in 2009, though they had two EPs released in between, which are Approved, released in 2011, and Advanced Basics, released in 2014.

**d10：Ubiquitous Synergy Seeker**
- `d10s0` USS (Ubiquitous Synergy Seeker) is a Canadian alternative rock musical duo that began working out of Parkdale, a neighbourhood situated in the west end of Toronto, Ontario, Canada.
- `d10s1` The band is composed of vocalist, guitarist, and erhu player Ashley Buchholz (aka Ash Boo-Schultz) and turntablist/hype man Jason "Human Kebab" Parsons.

### 由这道题生成的 SFT 样本（3 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=3 | d3, d9, d8 | u1 —; u2 —; u3 — |
| sftorder1 t=10 | d3, d9, d8, d6, d5, d4, d2, d10, d1, d7 | u1 —; u2 —; u3 — |
| sftorder2 t=2 | d3, d2 | u1 —; u2 —; u3 — |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 7 题：`hotpotqa_5a8661f85542991e7718162b`

- 数据集 / 题型：hotpotqa / comparison（unit 构造类型 comparison）
- 划分：train；特殊情况：unreachable
- 问题：Which, or both, originated in Turkey and Central Asia; Tulips or Virgilia trees?
- 源答案：Tulips

### 复核原因

**2 规则待定：“Which, or both”算不算点名候选**

> No presupposition: the question allows 'both', so it does not presuppose that exactly one candidate qualifies. The conclusion therefore can never be SUPPORTED under the current rules (open point).

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | whether tulips originated in Turkey and Central Asia | false | yes | — |
| u2 | whether Virgilia trees originated in Turkey and Central Asia | false | no | — |
| u3 | which of tulips and Virgilia trees, or both, originated in Turkey and Central Asia | true | tulips （Tulipa; tulip） | u1, u2 |

**u1 证据**
- support 第 1 组：
  - `d5s7` (Tulip) Tulips originally were found in a band stretching east from Turkey to Central Asia, but since the seventeenth century have become widely naturalised and cultivated ("see map").

**u2 证据**
- `[]`：原文没有明确陈述

**u3 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Comparison ('which, or both'): two fact units plus a conclusion unit.
- No explicit support for u2: Virgilia (plant) sentence 0 calls it a genus of Southern African trees; 'did not originate in Turkey and Central Asia' needs world knowledge.
- No presupposition: the question allows 'both', so it does not presuppose that exactly one candidate qualifies. The conclusion therefore can never be SUPPORTED under the current rules (open point).
- Virgilia (plant) sentence 0 removed from support.

### 全部文档（`*` = gold 引用的句子）

**d1：Demographics of Central Asia**
- `d1s0` Central Asia is a diverse land with many ethnic groups, languages, religions and tribes.
- `d1s1` The nations which make up Central Asia are five of the former Soviet republics: Kazakhstan, Kyrgyzstan, Turkmenistan, Tajikistan, and Uzbekistan, which have a total population of about /1e6 round 0 million.
- `d1s2` Afghanistan is not always considered part of the region, but when it is, Central Asia has a total population of about 122 million (2016).
- `d1s3` Additionally, Pakistan has a large population of central Asian peoples even though it is not categorized as a central Asian nation.
- `d1s4` Most central Asians belong to religions which were introduced to the area within the last 1,500 years, such as Sunni Islam, Shia Islam, Ismaili Islam, Tengriism, and Syriac Christianity.
- `d1s5` Buddhism, however, was introduced to Central Asia over 2,200 years ago, and Zoroastrianism, over 2,500 years ago.

**d2：Persian literature**
- `d2s0` Persian literature (Persian: ادبیات فارسی‎ ‎ "adabiyāt-e fārsi"), comprises oral compositions and written texts in the Persian language and it is one of the world's oldest literatures.
- `d2s1` It spans two-and-a-half millennia, though much of the pre-Islamic material has been lost.
- `d2s2` Its sources have been within Greater Iran including present-day Iran, Iraq, the Caucasus, and Turkey, regions of Central and South Asia where the Persian language has historically been either the native or official language.
- `d2s3` For instance, Mowlana Rumi, one of best-loved Persian poets, born in Balkh or Vakhsh (in what is now Afghanistan), wrote in Persian, and lived in Konya, then the capital of the Seljuks in Anatolia.
- `d2s4` The Ghaznavids conquered large territories in Central and South Asia and adopted Persian as their court language.
- `d2s5` There is thus Persian literature from Iran, Mesopotamia, Azerbaijan, the wider Caucasus, Turkey, western parts of Pakistan, India, Tajikistan and other parts of Central Asia.
- `d2s6` Not all Persian literature is written in Persian, as some consider works written by ethnic Persians in other languages, such as Greek and Arabic, to be included.
- `d2s7` At the same time, not all literature written in Persian is written by ethnic Persians or Iranians, as Turkic, Caucasian, and Indic poets and writers have also used the Persian language in the environment of Persianate cultures.

**d3：Selcuk Yorgancioglu**
- `d3s0` Selcuk Yorgancıoglu (born May 20, 1967) is a Turkish businessman in the finance sector.
- `d3s1` Yorgancıoglu currently is a Partner and Regional Head for Turkey and Central Asia, The Abraaj Group.
- `d3s2` The Abraaj Group (formerly known as Abraaj Capital) is the leading private equity investor operating in the growth markets of Africa, Latin America, Middle East, South Asia, South East Asia, Turkey and Central Asia.
- `d3s3` The Abraaj Group currently manages US$ 10.0 billion across 20+ sector and country-specific Funds, encompassing private equity and real estate investments.
- `d3s4` Yorgancıoglu is most notable within the Turkish investment community for The Abraaj Group's recent investment to Fibabanka partnering up with Özyeğin family and the prominent Turkish banker Hüsnü Özyeğin, Abraaj's investment in Turkey's largest e-commerce website Hepsiburada.com in partnership with Hanzade Doğan Boyner leading e-commerce entrepreneur in Turkey as well as Abraaj's multi billion dollar exit from Acıbadem Healthcare Group to Khazanah Nasional/IHH, the investment holding arm of the Government of Malaysia.
- `d3s5` As part of the deal, Abraaj got 50% cash and 50% shares in IHH.
- `d3s6` IHH was later floated jointly on Malaysia and Singapore stock exchanges.
- `d3s7` Year-to-date, it was the third biggest public offering in the world in 2012.
- `d3s8` This deal raised significant attention to Abraaj and the Founder Arif Naqvi and his Turkish business partner Selcuk Yorgancioglu.
- `d3s9` Under Yorgancioglu's lead, The Abraaj Group recently bought 80% of the Turkish Dairy Manufacturer, Yorsan.
- `d3s10` Yorsan deal was led by Yorgancioglu and his Turkish team, with another planned investment in horizon according to Bloomberg.

**d4：Black Death migration**
- `d4s0` The Black Death, caused by "Yersinia pestis", is enzootic (commonly present) in populations of ground rodents in Central Asia.
- `d4s1` Morelli et al. (2010) reported the origin of the plague bacillus to be in China.
- `d4s2` An older theory places the first cases in the steppes of Central Asia, and others, such as the historian Michael W. Dols, argue that the historical evidence concerning epidemics in the Mediterranean and specifically the Plague of Justinian point to a probability that the Black Death originated in Central Asia (not Africa - Asia (http://www.medicalnewstoday.com/articles/206309.php) where it then became entrenched among the rodent population.

**d5：Tulip**
- `d5s0` Tulips ("Tulipa") form a genus of spring-blooming perennial herbaceous bulbiferous geophytes (having bulbs as storage organs).
- `d5s1` The flowers are usually large, showy and brightly coloured, generally red yellow or white.
- `d5s2` They often have a different coloured blotch at the base of the tepals (petals), internally.
- `d5s3` because of a degree of variability within the populations, and a long history of cultivation, classification has been complex and controversial.
- `d5s4` The tulip is a member of the Liliaceae (lily) family, along with 14 other genera, where it is most closely related to "Amana", "Erythronium" and "Gagea" in the tribe Lilieae.
- `d5s5` There are about 75 species, and these are divided between four subgenera.
- `d5s6` The name "tulip" is thought to be derived from a Persian word for turban, which it may have been thought to resemble.
- *`d5s7` Tulips originally were found in a band stretching east from Turkey to Central Asia, but since the seventeenth century have become widely naturalised and cultivated ("see map").
- `d5s8` In their natural state they are adapted to mountainous areas with temperate climates.
- `d5s9` Flowering in the spring, they become dormant in the summer once the flowers and leaves die back, emerging above ground as a shoot from the underground bulb in early spring.

**d6：Islam in Central Asia**
- `d6s0` Islam in Central Asia has existed since the beginning of Islamic history.
- `d6s1` Islam is the most widely practiced religion in Central Asia.
- `d6s2` The Hanafi school of thought of Sunnism is the most popular, with Shiism of Imami and Ismaili denominations predominating in the Pamir plateau and the western Tian Shan mountains (almost exclusively Ismailis), while boasting to a large minority population in the Zarafshan river valley, from Samarkand to Bukhara (almost exclusively Imamis).
- `d6s3` Islam came to Central Asia in the early part of the 8th century as part of the Muslim conquest of the region.
- `d6s4` Many well-known Islamic scientists and philosophers came from Central Asia, and several major Muslim empires, including the Timurid Empire and the Mughal Empire, originated in Central Asia.
- `d6s5` In the 20th century, severe restrictions on religious practice were enacted by the Soviet Union in Soviet Central Asia and the People's Republic of China in Xinjiang.
- `d6s6` Concerns about Islamic radicalism and religious freedom in the region persist to this day.

**d7：Buddhism in Central Asia**
- `d7s0` Buddhism in Central Asia refers to the forms of Buddhism that existed in Central Asia, which were historically especially prevalent along the Silk Road.
- `d7s1` The history of Buddhism in Central Asia is closely related to the Silk Road transmission of Buddhism during the first millennium of the common era.

**d8：Virgilia (plant)**
- `d8s0` Virgilia is a genus of Southern African trees in the family Fabaceae, having shiny to hairy pinnate leaves and attractive mauve to pink pea-shaped flowers followed by leathery pods.
- `d8s1` They are valued as useful ornamental trees by gardeners, particularly the well-known species "Virgilia divaricata" ('Tree in a Hurry', 'Cape Lilac', 'Blossom Tree') and "Virgilia oroboides" ('Pink Blossom Tree'), despite having a comparatively short life (15 years).
- `d8s2` They prefer well drained soils; some will then grow 2m in the first season.
- `d8s3` They will tolerate wind and have dense foliage growing close to the ground, so they are useful as pioneer species for privacy and wind protection.
- `d8s4` The common name in South Africa (in Afrikaans) is keurboom, meaning 'choice tree'.

**d9：List of World Heritage Sites in Eastern Europe**
- `d9s0` The UNESCO (United Nations Educational, Scientific and Cultural Organization) has designated 77 World Heritage Sites in nine countries (also called "state parties") of Eastern Europe; defined here to mean the former Eastern Bloc countries not including the Baltic Countries (which are in Northern Europe) or former Yugoslavia and Albania (which are in Southern Europe) or the parts of Germany that once comprised East Germany (which are included in Western Europe): Russia, Belarus, Poland, Czech Republic, Slovakia, Hungary, Ukraine, Moldova, Romania and Bulgaria.
- `d9s1` Only the European part of Russia is included here; the Asian part is included in Central Asia.
- `d9s2` Although they have territory in Eastern Europe, uniquely positioned Turkey and the Caucasian countries of Armenia, Georgia, and Azerbaijan are not included here but in Western Asia, and Kazakhstan is included in Central Asia.

**d10：Soviet Central Asia**
- `d10s0` Soviet Central Asia refers to the section of Central Asia formerly controlled by the Soviet Union, as well as the time period of Soviet administration (1918–1991).
- `d10s1` Central Asian SSRs declared independence in 1991.
- `d10s2` In terms of area, it is nearly synonymous with Russian Turkestan, the name for the region during the Russian Empire.
- `d10s3` Soviet Central Asia went through many territorial divisions before the current borders were created in the 1920s and 1930s.

### 由这道题生成的 SFT 样本（6 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=7 | d6, d2, d7, d4, d9, d8, d5 | u1 ✅ yes ← d5s7; u2 —; u3 — |
| sftorder1 t=8 | d6, d2, d7, d4, d9, d8, d5, d3 | u1 ✅ yes ← d5s7; u2 —; u3 — |
| sftorder1 t=10 | d6, d2, d7, d4, d9, d8, d5, d3, d1, d10 | u1 ✅ yes ← d5s7; u2 —; u3 — |
| sftorder2 t=5 | d8, d7, d3, d10, d9 | u1 —; u2 —; u3 — |
| sftorder2 t=9 | d8, d7, d3, d10, d9, d2, d1, d6, d5 | u1 ✅ yes ← d5s7; u2 —; u3 — |
| sftorder3 t=1 | d5 | u1 ✅ yes ← d5s7; u2 —; u3 — |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 8 题：`hotpotqa_5a75b40f5542992d0ec05fe6`

- 数据集 / 题型：hotpotqa / comparison（unit 构造类型 comparison）
- 划分：train；特殊情况：unreachable
- 问题：Vania King and Cyril Suk III both specialize in what type of Tennis play?
- 源答案：doubles

### 复核原因

**2 规则待定：“both … what type”这类问题能否用预设**

> Open point: the question presupposes both share the specialty, so Suk's 'doubles specialist' alone would answer it, but rule 7 excludes 'both' questions from by_presupposition; the conclusion is therefore never supported.

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | type of tennis play Vania King specializes in | false | doubles | — |
| u2 | type of tennis play Cyril Suk III specializes in | false | doubles | — |
| u3 | type of tennis play that both Vania King and Cyril Suk III specialize in | true | doubles | u1, u2 |

**u1 证据**
- `[]`：原文没有明确陈述

**u2 证据**
- support 第 1 组：
  - `d10s1` (Cyril Suk) A doubles specialist, Suk won one Grand Slam men's doubles title and four Grand Slam mixed doubles titles during his career.

**u3 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Comparison (common attribute): one fact unit per player plus a conclusion unit.
- no explicit support: u1, Vania King 1 says she won two women's doubles titles, which does not state that she specializes in doubles.
- Vania King sentence 1 from the source supporting facts is therefore not used. The doubles tournament documents for Suk are co-occurrence only.
- Open point: the question presupposes both share the specialty, so Suk's 'doubles specialist' alone would answer it, but rule 7 excludes 'both' questions from by_presupposition; the conclusion is therefore never supported.

### 全部文档（`*` = gold 引用的句子）

**d1：1994 Gerry Weber Open – Doubles**
- `d1s0` Petr Korda and Cyril Suk were the defending champions, but Korda did not participate this year.
- `d1s1` Suk partnered Daniel Vacek, losing in the quarterfinals.

**d2：2005 Qatar Open – Doubles**
- `d2s0` Martin Damm and Cyril Suk were the defending champions.
- `d2s1` Damm partnered with Jared Palmer, losing in the first round.
- `d2s2` Suk partnered with Pavel Vízner, losing in the quarterfinals.

**d3：2001 Generali Open – Doubles**
- `d3s0` Pablo Albano and Cyril Suk were the defending champions but they competed with different partners that year, Albano with Lucas Arnold and Suk with Marius Barnard.

**d4：Vania King**
- `d4s0` Vania King (; born February 3, 1989) is an American tennis player.
- `d4s1` King won both the 2010 Wimbledon and 2010 US Open women's doubles titles with Kazakhstani partner Yaroslava Shvedova.

**d5：1996 Italian Open – Men's Doubles**
- `d5s0` Cyril Suk and Daniel Vacek were the defending champions but they competed with different partners that year, Suk with Hendrik Jan Davids and Vacek with Richey Reneberg.

**d6：2006 Ordina Open – Men's Doubles**
- `d6s0` Cyril Suk and Pavel Vízner were the defending champions, but did not play together this year.
- `d6s1` Suk partnered Robin Vik, losing in the first round.
- `d6s2` Vízner partnered Lukáš Dlouhý, losing in the semifinals.

**d7：1996 Davidoff Swiss Indoors – Doubles**
- `d7s0` Cyril Suk and Daniel Vacek were the defending champions but they competed with different partners that year, Suk with Petr Korda and Vacek with Yevgeny Kafelnikov.

**d8：1999 US Open – Men's Doubles**
- `d8s0` Sandon Stolle and Cyril Suk were the defending champions, but Stolle competed with Wayne Black, while Suk competed with Donald Johnson this year.
- `d8s1` Suk and Johnson were defeated by Stolle and Black in the third round, while Stolle and Black were defeated by Andrei Olhovskiy and David Prinosil in the quarterfinals.

**d9：1993 Volvo International – Doubles**
- `d9s0` The 1993 Volvo International was a tennis tournament played on outdoor hard courts at the Cullman-Heyman Tennis Center in New Haven, Connecticut, United States and was part of the Championship Series of the 1993 ATP Tour.
- `d9s1` The tournament ran from August 16 through August 23, 1993.
- `d9s2` Kelly Jones and Rick Leach were the defending champions but only Jones competed that year with Paul Annacone.
- `d9s3` Annacone and Jones lost in the semifinals to Cyril Suk and Daniel Vacek.
- `d9s4` Suk and Vacek won in the final 7–5, 6–4 against Steve DeVries and David Macpherson.

**d10：Cyril Suk**
- `d10s0` Cyril Suk III (born 29 January 1967) is a former professional tennis player.
- *`d10s1` A doubles specialist, Suk won one Grand Slam men's doubles title and four Grand Slam mixed doubles titles during his career.

### 由这道题生成的 SFT 样本（5 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=1 | d10 | u1 —; u2 ✅ doubles ← d10s1; u3 — |
| sftorder1 t=5 | d10, d9, d4, d8, d6 | u1 —; u2 ✅ doubles ← d10s1; u3 — |
| sftorder1 t=10 | d10, d9, d4, d8, d6, d2, d1, d5, d3, d7 | u1 —; u2 ✅ doubles ← d10s1; u3 — |
| sftorder2 t=7 | d1, d3, d4, d5, d6, d7, d10 | u1 —; u2 ✅ doubles ← d10s1; u3 — |
| sftorder3 t=7 | d8, d3, d1, d9, d6, d4, d7 | u1 —; u2 —; u3 — |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 9 题：`2wikimultihopqa_2f75b4620bb011ebab90acde48001122`

- 数据集 / 题型：2wikimultihopqa / inference（unit 构造类型 bridge）
- 划分：dev；特殊情况：unreachable
- 问题：Who is Manius Aemilius Lepidus (Consul 11)'s paternal grandmother?
- 源答案：Junia Secunda

### 复核原因

**2 规则待定：“son or nephew”不算明确陈述，结论永远答不完，起草者建议退回**

> no explicit support: Manius Aemilius Lepidus (consul 11) sentence 0 says he was 'the son or nephew of Marcus Aemilius Lepidus the Younger', which does not state the father. u1 has support_sets [], so u2 is never supported; the source answer depends on the 'son' reading. Reviewer may prefer reject.

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | father of Manius Aemilius Lepidus (consul 11) | false | Marcus Aemilius Lepidus the Younger （Marcus Aemilius Lepidus Minor） | — |
| u2 | mother of {u1}, Manius Aemilius Lepidus's paternal grandmother | true | Junia Secunda | u1 |

**u1 证据**
- `[]`：原文没有明确陈述

**u2 证据**
- support 第 1 组：
  - `d2s0` (Marcus Aemilius Lepidus Minor) Marcus Aemilius Lepidus the Younger or Marcus Aemilius Lepidus Minor( died 30 BC), was the only child of triumvir Marcus Aemilius Lepidus and his wife Junia Secunda, a half- sister to Brutus the Younger, one of Julius Caesar's assassins.

**起草备注**

- Bridge (inference): father (optional) then his mother (necessary).
- no explicit support: Manius Aemilius Lepidus (consul 11) sentence 0 says he was 'the son or nephew of Marcus Aemilius Lepidus the Younger', which does not state the father. u1 has support_sets [], so u2 is never supported; the source answer depends on the 'son' reading. Reviewer may prefer reject.
- Triple name 'Marcus Aemilius Lepidus the Younger' matches the document title 'Marcus Aemilius Lepidus Minor'; both kept.

### 全部文档（`*` = gold 引用的句子）

**d1：Quintus Aemilius Lepidus**
- `d1s0` Quintus Aemilius Lepidus( possibly Quintus Aemilius Lepidus Barbula)( fl. 1st century BC) was a Roman senator and military officer who was appointed consul in 21 BC.

**d2：Marcus Aemilius Lepidus Minor**
- *`d2s0` Marcus Aemilius Lepidus the Younger or Marcus Aemilius Lepidus Minor( died 30 BC), was the only child of triumvir Marcus Aemilius Lepidus and his wife Junia Secunda, a half- sister to Brutus the Younger, one of Julius Caesar's assassins.

**d3：Lucius Aemilius Lepidus Paullus (consul 34 BC)**
- `d3s0` Lucius Aemilius Lepidus Paullus also known as Paullus Aemilius Lepidus( c. 77 BC – after 11 BC) was a Roman Senator.
- `d3s1` Paullus was a member of the gens Aemilia.
- `d3s2` He was a grandson of Marcus Aemilius Lepidus and Appuleia through their son Lucius Aemilius Lepidus Paullus by his unnamed wife.
- `d3s3` His paternal uncle Marcus Aemilius Lepidus served as a member of the Second Triumvirate.
- `d3s4` Paullus served as consul in 34 BC and censor in 22.
- `d3s5` Paullus first married Cornelia( c. 54 BC- 16 BC).
- `d3s6` With Cornelia, Paullus had three children: Lucius Aemilius Paullus( c. 37 BC- 14 AD) the husband of Julia the Younger and consul in AD 1; Marcus Aemilius Lepidus( c. 30 BC- 33 AD), consul in AD 6; and a daughter Aemilia Paulla( c. 22 BC).
- `d3s7` Aemilia was married twice: first to Lucius Munatius Plancus, consul in AD 13; second to Publius Memmius Regulus.
- `d3s8` Paullus was widowed in 18 BC, the same year Cornelia's brother Publius Cornelius Lentulus Marcellinus was consul.
- `d3s9` Not long after Cornelia's death, he married Claudia Marcella Minor, one of the daughters of consul Gaius Claudius Marcellus Minor and Octavia the Younger, as her maternal uncle was the Roman emperor Augustus.
- `d3s10` The marriage of Marcella and Paullus linked two honored republican houses and tied them closely to the imperial circle.
- `d3s11` At some point after 11 BC, Marcella bore him a son, Paullus Aemilius Regulus, who later served as a quaestor during the rule of the Roman emperor Tiberius.

**d4：Manius Aemilius Lepidus (consul 66 BC)**
- `d4s0` Manius Aemilius Lepidus was a Roman politician who became consul in 66 BC alongside Lucius Volcatius Tullus.

**d5：Tjuyu**
- `d5s0` Tjuyu( sometimes transliterated as Thuya or Thuyu) was an Egyptian noblewoman and the mother of queen Tiye, and the wife of Yuya.
- `d5s1` She is the grandmother of Akhenaten, and great grandmother of Tutankhamun.

**d6：Lucius Volcatius Tullus (consul 66 BC)**
- `d6s0` Lucius Volcatius Tullus was a Roman politician who became consul in 66 BC alongside Manius Aemilius Lepidus.

**d7：Hannah Arnold**
- `d7s0` Hannah Arnold, also known as Hannah Waterman King, was the grandmother of Benedict Arnolds children.

**d8：Hubba bint Hulail**
- `d8s0` Hubba bint Hulail was the grandmother of Hashim ibn' Abd Manaf, thus the great- great- great- grandmother of the Islamic" Nabī"( Prophet) Muhammad ibn Abdullah.

**d9：Manius Aemilius Lepidus (consul 11)**
- `d9s0` Manius Aemilius Lepidus was the son or nephew of Marcus Aemilius Lepidus the Younger and consul of Rome in 11 AD.
- `d9s1` Tacitus reports that Augustus on his deathbed, while discussing possible rivals for the Roman Emperor Tiberius, described him as worthy of becoming emperor ("capax imperii"), but "disdainful" of supreme power.
- `d9s2` He defended his sister Aemilia Lepida at her trial in 20 AD.
- `d9s3` He had a daughter also called Aemilia Lepida.
- `d9s4` At the trial of Clutorius Priscus, he argued without success that the proposed death sentence was excessively harsh.
- `d9s5` After 5 BC, but prior to acceding to the consulship, Lepidus was coopted as an Augur.
- `d9s6` In 21 AD, Tiberius appointed him to the governorship of Asia.

**d10：Mona Hopton Bell**
- `d10s0` Mona Hopton Bell( 1867- 1940) was a British artist, best known for her portraits of civic figures.
- `d10s1` She was the grandmother of the painter Jean H. Bell.

### 由这道题生成的 SFT 样本（6 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=1 | d1 | u1 —; u2 — |
| sftorder1 t=4 | d1, d5, d7, d2 | u1 —; u2 — |
| sftorder1 t=10 | d1, d5, d7, d2, d10, d6, d4, d8, d3, d9 | u1 —; u2 — |
| sftorder2 t=6 | d3, d5, d7, d4, d8, d2 | u1 —; u2 — |
| sftorder3 t=4 | d4, d8, d1, d5 | u1 —; u2 — |
| sftorder3 t=6 | d4, d8, d1, d5, d10, d2 | u1 —; u2 — |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 10 题：`2wikimultihopqa_3a2fe93e0bda11eba7f7acde48001122`

- 数据集 / 题型：2wikimultihopqa / compositional（unit 构造类型 bridge）
- 划分：dev；特殊情况：unreachable
- 问题：What nationality is Keith Batey's wife?
- 源答案：British

### 复核原因

**2 规则待定：原文写 English，源答案是 British，两者算不算同一个值**

> Open point: 'English' is the explicitly stated descriptor; it is not added as an alias because it is a different value from the source answer. Reviewer may prefer expected_answer 'English' with support Mavis Batey 0.

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | wife of Keith Batey | false | Mavis Batey （Mavis Lilian Batey） | — |
| u2 | nationality of {u1} | true | British | u1 |

**u1 证据**
- support 第 1 组：
  - `d2s0` (Keith Batey) Keith Batey( 4 July 1919 – 28 August 2010) was a codebreaker who, with his wife, Mavis Batey( 5 May 1921 – 12 November 2013), worked on the German Enigma machine at Bletchley Park during World War II.

**u2 证据**
- `[]`：原文没有明确陈述

**起草备注**

- Bridge: wife (optional) then nationality (necessary).
- no explicit support: no sentence calls Mavis Batey British. Mavis Batey 0 says 'an English code-breaker'; English to British needs world knowledge. The supporting fact Mavis Batey 3 is an award (Member of the Order of the British Empire), not a nationality. u2 has support_sets [].
- Open point: 'English' is the explicitly stated descriptor; it is not added as an alias because it is a different value from the source answer. Reviewer may prefer expected_answer 'English' with support Mavis Batey 0.

### 全部文档（`*` = gold 引用的句子）

**d1：Iraqi nationality law**
- `d1s0` Iraqi nationality is transmitted by one's parents.

**d2：Keith Batey**
- *`d2s0` Keith Batey( 4 July 1919 – 28 August 2010) was a codebreaker who, with his wife, Mavis Batey( 5 May 1921 – 12 November 2013), worked on the German Enigma machine at Bletchley Park during World War II.

**d3：Mavis Batey**
- `d3s0` Mavis Lilian Batey, MBE( née Lever; 5 May 1921 – 12 November 2013), was an English code- breaker during World War II.
- `d3s1` Her work at Bletchley Park was one of the keys to the success of D- Day.
- `d3s2` She later became an historian of gardening, who campaigned to save historic parks and gardens, and an author.
- `d3s3` Batey was awarded the Veitch Memorial Medal in 1985, and made a Member of the Order of the British Empire( MBE) in 1987, in both cases for her work on the conservation of gardens.

**d4：Nayelly Hernández**
- `d4s0` Nayelly Hernández( born 23 February 1986) is a former Mexican female professional squash player.
- `d4s1` She has represented Mexico internationally in several international competitions including the Central American and Caribbean Games, Pan American Games, Women's World Team Squash Championships.
- `d4s2` Nayelly achieved her highest career ranking of 57 in October 2011 during the 2011 PSA World Tour.
- `d4s3` Her husband Chris Walker whose nationality is English is also a professional squash player.
- `d4s4` She joined the Trinity College in 2008 as the first Mexican female to join a US college for squash and graduated in 2010.

**d5：Baglan Mailybayev**
- `d5s0` Baglan Mailybayev( in Kazakh Бағлан Асаубайұлы Майлыбаев) was born on 20 May 1975 in Zhambyl region, Kazakhstan.
- `d5s1` His nationality is Kazakh.
- `d5s2` He is a politician of the Republic of Kazakhstan, Deputy Head of the Presidential Administration of the Republic of Kazakhstan, Doctor of Law( 2002)( under the supervision of Professor Zimanov S.Z.- scientific advisor and academician of National Academy of Sciences of the Republic of Kazakhstan) and Ph.D. in Political Science( 1998).

**d6：Eleni Gabre-Madhin**
- `d6s0` Eleni Zaude Gabre- Madhin, an Ethiopian economist with Swiss nationality, is a former Chief Executive Officer of the Ethiopia Commodity Exchange( ECX).
- `d6s1` She has had many years of experience working on agricultural markets – particularly in Sub- Saharan Africa – and has held senior positions in the World Bank, the International Food Policy Research Institute( Washington), and United Nations( Geneva).

**d7：Mário Laginha**
- `d7s0` Mário João Laginha dos Santos,( born April 25, 1960 in Lisbon), a pianist and composer, is one of the most well- known Portuguese jazz musicians today.
- `d7s1` He is mostly recognized for his collaborations with Portuguese jazz singer Maria João, with whom he recorded over a dozen albums and toured worldwide extensively.
- `d7s2` Other acknowledged collaboration work includes four- handed piano sessions with Bernardo Sassetti and Pedro Burmester.
- `d7s3` Mário's main influence on piano is Keith Jarrett.

**d8：Ali Rahuma**
- `d8s0` Ali Khalifa Rahuma( born May 16, 1982) is a Libyan football midfielder who's nationality is Libyan.
- `d8s1` He currently plays for Al- Ittihad, and is a member of the Libya national football team.

**d9：Malcolm Sinclair (actor)**
- `d9s0` Malcolm Sinclair( born 5 June 1950) is a British stage and television actor and former President of Trade Union, Equity 2010 – 18 when he stood down after 4 terms and was replaced by Maureen Beattie.
- `d9s1` He is perhaps best known for his role as Assistant Chief Constable Freddy Fisher in the television series" Pie in the Sky"( 1994 – 1997), although he has an extensive number of film, television and theatre roles to his credit.
- `d9s2` His brother is Keith Sinclair, the Bishop of Birkenhead.

**d10：Rebirth (Keith Sweat album)**
- `d10s0` Rebirth is Keith Sweat's eighth studio album.

### 由这道题生成的 SFT 样本（5 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=6 | d7, d4, d5, d1, d3, d6 | u1 —; u2 — |
| sftorder1 t=7 | d7, d4, d5, d1, d3, d6, d2 | u1 ✅ Mavis Batey ← d2s0; u2 — |
| sftorder1 t=10 | d7, d4, d5, d1, d3, d6, d2, d8, d10, d9 | u1 ✅ Mavis Batey ← d2s0; u2 — |
| sftorder2 t=5 | d7, d4, d10, d8, d2 | u1 ✅ Mavis Batey ← d2s0; u2 — |
| sftorder2 t=8 | d7, d4, d10, d8, d2, d9, d1, d5 | u1 ✅ Mavis Batey ← d2s0; u2 — |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 11 题：`hotpotqa_5ade1b7755429975fa854e55`

- 数据集 / 题型：hotpotqa / comparison（unit 构造类型 comparison）
- 划分：train；特殊情况：unreachable
- 问题：Which band was founded in the 21st century, Foo Fighters or Goon Moon?
- 源答案：Goon Moon

### 复核原因

**2 规则待定：输家的事实明确、赢家的不明确时，能否用排除法**

> No presupposition_sets: rule 7a needs the winner's fact to be explicit; here only the loser's is. The conclusion is therefore never supported. Open point: elimination by presupposition (loser confirmed 'no').

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | whether Foo Fighters was founded in the 21st century | false | no | — |
| u2 | whether Goon Moon was founded in the 21st century | false | yes | — |
| u3 | which of Foo Fighters and Goon Moon was founded in the 21st century | true | Goon Moon | u1, u2 |

**u1 证据**
- support 第 1 组：
  - `d8s0` (Foo Fighters) Foo Fighters is an American rock band, formed in Seattle, Washington in 1994.
- support 第 2 组：
  - `d9s0` (List of Foo Fighters band members) Foo Fighters is an American alternative rock band formed by multi-instrumentalist and vocalist Dave Grohl in 1994.
- support 第 3 组：
  - `d10s0` (Foo Fighters live performances) Foo Fighters is an American alternative rock band, founded in 1994 by musician Dave Grohl.

**u2 证据**
- `[]`：原文没有明确陈述

**u3 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Comparison (selection between named candidates): one fact unit per band plus a conclusion unit.
- u1 'no' follows from the stated year 1994 (Foo Fighters 0, List of Foo Fighters band members 0, Foo Fighters live performances 0).
- no explicit support: u2, no sentence gives Goon Moon's founding date; the 2005 mini-LP (Goon Moon 1) only implies it. Goon Moon 0, 1, 3 from the source supporting facts are not used.
- No presupposition_sets: rule 7a needs the winner's fact to be explicit; here only the loser's is. The conclusion is therefore never supported. Open point: elimination by presupposition (loser confirmed 'no').

### 全部文档（`*` = gold 引用的句子）

**d1：Goon Moon**
- `d1s0` Goon Moon is an American rock band composed of Jeordie White (also known as Twiggy Ramirez) and Chris Goss.
- `d1s1` The band released the mini-LP "I Got a Brand New Egg Layin' Machine" in 2005 and have since recorded a full-length album, "Licker's Last Leg", which was released on May 8, 2007.
- `d1s2` The album features cameos from longtime Goss collaborators Josh Homme and Josh Freese, as well as desert rock mainstay Dave Catching.
- `d1s3` Although Goss and White continue to work on other projects, they have both alluded to the possibility of future Goon Moon recordings on Twitter.

**d2：The Colour and the Shape**
- `d2s0` The Colour and the Shape is the second studio album by the American rock band Foo Fighters.
- `d2s1` Produced by Gil Norton, it was released through Capitol Records and the group's own Roswell Records on May 20, 1997.
- `d2s2` The record is the debut of the Foo Fighters as a group, as the band's previous record, "Foo Fighters" (1995), was primarily recorded by frontman Dave Grohl and friend Barrett Jones as a demo.
- `d2s3` After the project ballooned and became an international success, the group convened for pre-production in the fall of 1996 and brought in producer Norton to establish a pop sensibility for the tracks.
- `d2s4` The band strived to create a full-fledged rock record, although the music press predicted another grunge offshoot.

**d3：Socialism of the 21st century**
- `d3s0` Socialism of the 21st century (Spanish: "Socialismo del siglo XXI" ) is a political term used to describe the interpretation of socialist principles advocated first by Heinz Dieterich in 1996 and later by Latin American leaders like Hugo Chávez of Venezuela, Rafael Correa of Ecuador, Evo Morales of Bolivia, and Luiz Inácio Lula da Silva of Brazil.
- `d3s1` Socialism of the 21st century argues that both free-market industrial capitalism and twentieth-century socialism have failed to solve urgent problems of humanity, like poverty, hunger, exploitation, economic oppression, sexism, racism, the destruction of natural resources, and the absence of a truly participative democracy.
- `d3s2` Therefore, because of the local unique historical conditions, socialism of the 21st century is often contrasted with previous applications of socialism in other countries and aims for a more decentralized and participatory planning process.
- `d3s3` Socialism of the 21st century has democratic socialist elements, but primarily resembles Marxist revisionism.

**d4：Songs from the Laundry Room**
- `d4s0` Songs from the Laundry Room is an EP by American rock band Foo Fighters, released exclusively for Record Store Day 2015.
- `d4s1` This EP and the Foo Fighters album are the two Foo Fighters releases upon which Dave Grohl plays all the instruments.

**d5：Foo Fighters: Back and Forth**
- `d5s0` Foo Fighters: Back and Forth is a 2011 rockumentary about the American rock band Foo Fighters, directed by filmmaker James Moll.
- `d5s1` The film documents the band's history, and gets its title from a track on the Foo Fighters' seventh studio album "Wasting Light".

**d6：21st century in fiction**
- `d6s0` Many science fiction works have been set in the 21st century (years 2001 to 2100).
- `d6s1` With humanity now in the 21st century, many of the predictions of these works have so far been proven obsolete.
- `d6s2` This page lists only "predictions" regarding the 21st century, as opposed to contemporary accounts of the actual 21st century, which would be too numerous to list.

**d7：Sunny Day Real Estate**
- `d7s0` Sunny Day Real Estate was an American emo band from Seattle, Washington.
- `d7s1` They were one of the early emo bands and helped establish the genre.
- `d7s2` In 1994, the band released their debut album "Diary" on Sub Pop Records to critical acclaim.
- `d7s3` However, shortly after releasing their second album "LP2", the band broke up, with members Nate Mendel and William Goldsmith joining Foo Fighters and Jeremy Enigk embarking on a solo career.
- `d7s4` In 1997, they regrouped long enough to record two more studio albums and a live album but ultimately disbanded once again in 2001.
- `d7s5` The band reunited again in 2009.
- `d7s6` Bassist Nate Mendel, who chose to remain with Foo Fighters during the previous reunion in 1997, took part in this reunion.
- `d7s7` In a 2013 interview with MusicRadar, Mendel said Sunny Day Real Estate was inactive.
- `d7s8` According to Mendel, the band attempted to record a full-length album after the end of their reunion tour, but the sessions "just fell apart".
- `d7s9` In 2014 the band released one song from those sessions, "Lipton Witch," on a split 7" vinyl with Circa Survive on Record Store Day.

**d8：Foo Fighters**
- *`d8s0` Foo Fighters is an American rock band, formed in Seattle, Washington in 1994.
- `d8s1` It was founded by Nirvana drummer Dave Grohl as a one-man project following the dissolution of Nirvana after the death of Kurt Cobain.
- `d8s2` The group got its name from the UFOs and various aerial phenomena that were reported by Allied aircraft pilots in World War II, which were known collectively as "foo fighters".

**d9：List of Foo Fighters band members**
- *`d9s0` Foo Fighters is an American alternative rock band formed by multi-instrumentalist and vocalist Dave Grohl in 1994.
- `d9s1` After recording the album "Foo Fighters" alone, Grohl enlisted guitarist Pat Smear, bassist Nate Mendel and drummer William Goldsmith to join the band.
- `d9s2` This lineup recorded the second Foo Fighters album, 1997's "The Colour and the Shape", although most of Goldsmith's drum recordings were removed and re-recorded by Grohl for the release, after he left the band due to creative tensions.
- `d9s3` Goldsmith was replaced by Taylor Hawkins, and Franz Stahl replaced Smear after he also departed, although he only remained in the band for a short period and did not record an album with the group.
- `d9s4` The group's third album, "There Is Nothing Left to Lose", featured Hawkins on drums and was released in 1999.

**d10：Foo Fighters live performances**
- *`d10s0` Foo Fighters is an American alternative rock band, founded in 1994 by musician Dave Grohl.
- `d10s1` After recording by himself what would become the album Foo Fighters, Grohl decided to recruit a full band with him as singer and guitarist.
- `d10s2` The original line-up included bassist Nate Mendel, drummer William Goldsmith, and Pat Smear.

### 由这道题生成的 SFT 样本（6 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=2 | d4, d10 | u1 ✅ no ← d10s0; u2 —; u3 — |
| sftorder1 t=8 | d4, d10, d5, d6, d2, d1, d3, d8 | u1 ✅ no ← d8s0; u2 —; u3 — |
| sftorder1 t=10 | d4, d10, d5, d6, d2, d1, d3, d8, d7, d9 | u1 ✅ no ← d8s0; u2 —; u3 — |
| sftorder2 t=2 | d2, d9 | u1 ✅ no ← d9s0; u2 —; u3 — |
| sftorder2 t=9 | d2, d9, d1, d8, d6, d5, d10, d4, d7 | u1 ✅ no ← d8s0; u2 —; u3 — |
| sftorder3 t=5 | d7, d5, d2, d6, d10 | u1 ✅ no ← d10s0; u2 —; u3 — |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 12 题：`hotpotqa_5a7f66cb55429969796c1a32`

- 数据集 / 题型：hotpotqa / comparison（unit 构造类型 comparison）
- 划分：train；特殊情况：无
- 问题：Between Cranium and Auf Achse, which game had more people involved in creating?
- 源答案：Cranium

### 复核原因

**3 靠数列表项来比较（哪款游戏的创作者更多）**

> Caveat: Cranium sentence 4 also names packaging and artwork contributors; counting them only strengthens the answer.

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | people who created the game Cranium | false | Whit Alexander and Richard Tait | — |
| u2 | people who created the game Auf Achse | false | Wolfgang Kramer | — |
| u3 | which game had more people involved in creating it, Cranium or Auf Achse | true | Cranium | u1, u2 |

**u1 证据**
- support 第 1 组：
  - `d7s0` (Cranium (board game)) Cranium is a party game created by Whit Alexander and Richard Tait in 1998, after Richard spent a weekend playing games with another family and recognized the need for a game involving a variety of skills.
- support 第 2 组：
  - `d4s1` (Cranium, Inc.) The company was founded in 1998 by two former Microsoft executives, Richard Tait and Whit Alexander.
  - `d4s2` (Cranium, Inc.) They co-developed the "Cranium" board game.

**u2 证据**
- support 第 1 组：
  - `d10s0` (Auf Achse) Auf Achse (literally "on the axle"; figuratively "on the road") is a logistics-themed board game designed by Wolfgang Kramer and published in 1987 by FX Schmid.

**u3 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Comparison (count): creators of each game plus a conclusion unit; the conclusion compares the counts (two vs. one).
- Cranium, Inc. sentences 1-2 together state that Tait and Alexander co-developed the game; added as alternative support for u1.
- Auf Achse (TV series) is a distractor (a different work).
- Caveat: Cranium sentence 4 also names packaging and artwork contributors; counting them only strengthens the answer.

### 全部文档（`*` = gold 引用的句子）

**d1：Zigity**
- `d1s0` Zigity is a card game from the makers of Cranium that combines the play of games such as "Uno" with typical Cranium elements.

**d2：Garish**
- `d2s0` garish, formed in February 1997, is an Austrian alternative rock band.
- `d2s1` After having asserted themselves in the alternative scene inside and outside Austria's borders with their first two records "amaurose pur."
- `d2s2` and "wo die nacht erzaehlt vom tag", their third album "Absender auf Achse" gained favorable press and fan reaction.
- `d2s3` Despite German lyrics, it is said that their emotional style of music is their "real language".

**d3：Suicide mission**
- `d3s0` A suicide mission is a task which is so dangerous for the people involved that they are not expected to survive.
- `d3s1` The term is sometimes extended to include suicide attacks such as kamikaze and suicide bombings, where the people involved actively commit suicide during execution of the mission.
- `d3s2` The risks involved with suicide missions are not always apparent to those participating in them or to those who plan them.
- `d3s3` However, for an action to be considered a suicide mission someone involved must be aware of the risks.
- `d3s4` A mission that goes horribly wrong is not a suicide mission.
- `d3s5` An individual or group taking part in a mission may perceive the risks involved to be far greater than what they believe to be acceptable, while those planning or commanding the mission may think otherwise.
- `d3s6` These situations can often lead to refusals to participate in missions on the basis that they are "suicide missions".
- `d3s7` Similarly, planners or commanders may be well aware of the risks involved with missions while those participating in them may not.

**d4：Cranium, Inc.**
- `d4s0` Cranium, Inc. was a toy and board game developer.
- *`d4s1` The company was founded in 1998 by two former Microsoft executives, Richard Tait and Whit Alexander.
- *`d4s2` They co-developed the "Cranium" board game.

**d5：Visual guide**
- `d5s0` When applied to building block a website or similar work product, a Visual Guide can be an intermediate step toward the end goal of a complete website.
- `d5s1` By creating a visual guide along the way, the designer or developer can get input from the other people involved in the website such as the customer, their manager, and other members of the team.
- `d5s2` The visual guide will provide a view to the customer of what their website or project will end up looking like.
- `d5s3` It ensures that they are kept up to date on any developments and changes made to the structure or visuals.
- `d5s4` Visual guides also allow you to define the information hierarchy of the design.

**d6：Body Positive Movement**
- `d6s0` The Body Positive Movement is a movement that encourages people to adopt more forgiving and affirming attitudes towards their bodies, with the goal of improving overall health and well-being.
- `d6s1` Whether people are nurturing their bodies and maintaining their weight, or finding a place in life where they are comfortable through working out, or changing their lifestyles to find a better attitude, the body positive movement focuses on building self-esteem through improving one's self-image.
- `d6s2` The body positive movement targets all body shapes and sizes.
- `d6s3` The movement is not only about working out and striving to be positive and creating a better lifestyle for oneself, but deals with health as well.
- `d6s4` A debate within the movement surrounds the question of whether social media sites, including Instagram, Facebook, and blogs, are helping or harming people's perceptions of their bodies.
- `d6s5` People involved with this movement challenge themselves daily to learn how to grow and love themselves to the fullest.

**d7：Cranium (board game)**
- *`d7s0` Cranium is a party game created by Whit Alexander and Richard Tait in 1998, after Richard spent a weekend playing games with another family and recognized the need for a game involving a variety of skills.
- `d7s1` He left his job at Microsoft, convincing his friend and co-worker Whit Alexander to join him in the creation of "Cranium".
- `d7s2` "Cranium", manufactured by Hasbro subsidiary Cranium, Inc., is billed as "The Game for Your Whole Brain".
- `d7s3` Unlike many other party games, "Cranium" includes a wide variety of activities.
- `d7s4` Giorgio Davanzo handles packaging and branding for the game, and the artwork is done by Gary Baseman, creator of the animated television series "Teacher's Pet".

**d8：Auf Achse (TV series)**
- `d8s0` Auf Achse (a German expression meaning "on the road", the literal translation would be "on the axle") was a German television series on the ARD channel.
- `d8s1` The series ran from 1977 until 1996 and 86 episodes were produced altogether.

**d9：Cranium Whoonu**
- `d9s0` Cranium Whoonu is a party game manufactured by Cranium, Inc. Whoonu is billed as "the fun-filled 'what's your favorite thing?'
- `d9s1` game".

**d10：Auf Achse**
- *`d10s0` Auf Achse (literally "on the axle"; figuratively "on the road") is a logistics-themed board game designed by Wolfgang Kramer and published in 1987 by FX Schmid.
- `d10s1` The game won the Spiel des Jahres award.
- `d10s2` In 1992, a junior edition was released; and in 1994 a rummy-like card game spinoff was released.
- `d10s3` In 2007 a revised edition was published by Schmidt Spiele.

### 由这道题生成的 SFT 样本（7 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=1 | d7 | u1 ✅ Whit Alexander and Richard Tait ← d7s0; u2 —; u3 — |
| sftorder1 t=5 | d7, d3, d5, d4, d6 | u1 ✅ Whit Alexander and Richard Tait ← d7s0; u2 —; u3 — |
| sftorder1 t=6 | d7, d3, d5, d4, d6, d10 | u1 ✅ Whit Alexander and Richard Tait ← d7s0; u2 ✅ Wolfgang Kramer ← d10s0; u3 ✅ Cranium ← d7s0,d10s0 |
| sftorder1 t=7 | d7, d3, d5, d4, d6, d10, d9 | u1 ✅ Whit Alexander and Richard Tait ← d7s0; u2 ✅ Wolfgang Kramer ← d10s0; u3 ✅ Cranium ← d7s0,d10s0 |
| sftorder1 t=10 | d7, d3, d5, d4, d6, d10, d9, d8, d1, d2 | u1 ✅ Whit Alexander and Richard Tait ← d7s0; u2 ✅ Wolfgang Kramer ← d10s0; u3 ✅ Cranium ← d7s0,d10s0 |
| sftorder2 t=8 | d7, d1, d4, d6, d3, d5, d8, d10 | u1 ✅ Whit Alexander and Richard Tait ← d7s0; u2 ✅ Wolfgang Kramer ← d10s0; u3 ✅ Cranium ← d7s0,d10s0 |
| sftorder3 t=6 | d2, d6, d5, d8, d1, d7 | u1 ✅ Whit Alexander and Richard Tait ← d7s0; u2 —; u3 — |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 13 题：`hotpotqa_5a84fd2a5542994c784ddabb`

- 数据集 / 题型：hotpotqa / comparison（unit 构造类型 comparison）
- 划分：train；特殊情况：by_omission
- 问题：Which leader singer plays more musical instruments, Matt Shultz or Paul Roberts?
- 源答案：Matthew Ray "Matt" Shultz

### 复核原因

**3 靠数列表项来比较（谁演奏的乐器更多），和已退回的 2Wiki 同类题标准不一致；“演奏乐器”算不算职业也待定**

> Open point: treating 'plays an instrument' (instrumentalist) as an occupation attribute is a judgment call.

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | musical instruments Matt Shultz plays | false | guitar | — |
| u2 | musical instruments Paul Roberts plays | false | none （no instrument） **[by_omission]** | — |
| u3 | which of Matt Shultz and Paul Roberts plays more musical instruments | true | Matt Shultz （Matthew Ray "Matt" Shultz; Matthew Ray Shultz） | u1, u2 |

**u1 证据**
- support 第 1 组：
  - `d5s0` (Matt Shultz (singer)) Matthew Ray "Matt" Shultz (born October 23, 1983) is the lead singer and occasional guitarist for the American rock band Cage the Elephant.
- support 第 2 组：
  - `d5s1` (Matt Shultz (singer)) He also plays guitar on the bonus track "Cover Me Again" from their self-titled album.

**u2 证据**
- support 第 1 组：
  - `d2s0` (Paul Roberts (musician)) Paul Roberts (born 31 December 1959 in Chiswick, London) is an English singer who was the lead singer of The Stranglers between 1990 and 2006.

**u3 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Comparison (count of instruments): two fact units plus a conclusion unit; no presupposition (value comparison).
- u1: Matt Shultz sentence 0 ('occasional guitarist') and sentence 1 ('also plays guitar') each state guitar.
- u2 uses the omission exception: Paul Roberts (musician) sentence 0 is a defining description listing the occupation 'singer' (lead singer of The Stranglers) and no instrument. No document states that this Paul Roberts plays an instrument (Soulsec 0 calls him frontman; K-Klass and the 1942 song concern other people named Paul Roberts), so condition 4 holds.
- Open point: treating 'plays an instrument' (instrumentalist) as an occupation attribute is a judgment call.
- Cage the Elephant sentence 1 ('lead vocalist Matt Shultz') states no instrument and is not used.

### 全部文档（`*` = gold 引用的句子）

**d1：Cage the Elephant**
- `d1s0` Cage the Elephant is an American rock band from Bowling Green, Kentucky, that formed in 2006 and relocated to London, England in 2008 before their first album was released.
- `d1s1` The band currently consists of lead vocalist Matt Shultz, rhythm guitarist Brad Shultz, lead guitarist Nick Bockrath, guitarist and keyboardist Matthan Minster, bassist Daniel Tichenor, and drummer Jared Champion.
- `d1s2` Lincoln Parish served as the band's lead guitarist from their formation in 2006 until December 2013, when he left on good terms to pursue a career in producing.
- `d1s3` The band's first album, "Cage the Elephant", was released in 2008 to much success, spawning several successful radio singles and gained the band a large following in both the United States and the United Kingdom.

**d2：Paul Roberts (musician)**
- *`d2s0` Paul Roberts (born 31 December 1959 in Chiswick, London) is an English singer who was the lead singer of The Stranglers between 1990 and 2006.

**d3：C.G. Conn**
- `d3s0` C.G. Conn Ltd., sometimes called Conn Instruments or commonly just Conn, was a United States manufacturer of musical instrument incorporated in 1915.
- `d3s1` It bought the production facilities owned by Charles Gerard Conn, a major figure in early manufacture of brasswinds and saxophones in the USA.
- `d3s2` Its early business was based mainly on such instruments, which it manufactured in Elkhart, Indiana.
- `d3s3` During the 1950s the bulk of its sales revenue shifted to electric organs.
- `d3s4` In 1969 the company was sold under bankruptcy to the Crowell-Collier-MacMillan publishing company.
- `d3s5` Conn was divested of its Elkhart production facilities in 1970, leaving remaining production in satellite facilities and contractor sources.
- `d3s6` The company was sold in 1980 then again in 1985, reorganized under the parent corporation United Musical Instruments (UMI) in 1986.
- `d3s7` The assets of UMI were bought by Steinway Musical Instruments in 2000 and in January 2003 were merged with other Steinway properties into a subsidiary called Conn-Selmer.
- `d3s8` C.G. Conn is currently a brand of musical instruments manufactured by Conn-Selmer.

**d4：Jared Champion**
- `d4s0` In high school, Champion, with current bandmates Matt Shultz and Brad Shultz, were in a band called Liquid Twilight.
- `d4s1` It is unknown when they broke up.

**d5：Matt Shultz (singer)**
- *`d5s0` Matthew Ray "Matt" Shultz (born October 23, 1983) is the lead singer and occasional guitarist for the American rock band Cage the Elephant.
- *`d5s1` He also plays guitar on the bonus track "Cover Me Again" from their self-titled album.

**d6：Gesellschaft der Freunde alter Musikinstrumente**
- `d6s0` The Gesellschaft der Freunde alter Musikinstrumente (GEFAM) ("Society of friends of old musical instruments") was founded in 1951 in Zurich, Switzerland, by a number of music lovers and collectors of historical musical instruments.
- `d6s1` It is still the only society in the German speaking part of Europe (Germany, Austria, Switzerland, Lichtenstein) that is concerned mainly with old musical instruments.
- `d6s2` Thanks to its base in Switzerland it has a multicultural and multilanguage profile, visual in its international list of members.
- `d6s3` Today there are around 200 members (individuals and institutions), mainly in Europe, but also on other parts of the globe.
- `d6s4` The spectrum includes specialised museums and collections of old musical instruments, researchers and instrument makers as well as private collectors and enthusiasts.

**d7：Museum of Musical Instruments (Milan)**
- `d7s0` The Museum of Musical Instruments of Milan exhibits over 700 musical instruments from the fifteenth to twentieth centuries with particular attention to Lombard instruments.
- `d7s1` The collection contains plucked instruments, Lombard and Cremonese violins, hunting horns, numerous wood instruments (e.g. flutes, oboes, clarinets, English horns), bassoons, pianos and some ancient organs.
- `d7s2` In particular the Cremonese lutherie (from Cremona in low Lombardy) is appreciated all over the world for the high quality of its musical instruments.
- `d7s3` The museum also displays the equipment of the former Studio di fonologia musicale di Radio Milano.

**d8：K-Klass**
- `d8s0` K-Klass are a British electronic music group that originally recorded in Wrexham, North Wales, and are now based in Manchester, England.
- `d8s1` Its original members were Andy Williams, Carl Thomas, Russ Morgan and Paul Roberts.
- `d8s2` K-Klass signed with the label Deconstruction Records, and later to Parlophone.
- `d8s3` Since leaving Parlophone Andy Williams and Carl Thomas have both left K-Klass leaving just Paul Roberts and Russell Morgan alongside original vocalist Bobbi Depasois as K-Klass.
- `d8s4` Roberts and Morgan run their own record label Klass Action

**d9：There's a Star-Spangled Banner Waving Somewhere**
- `d9s0` "There's A Star-Spangled Banner Waving Somewhere" is a patriotic anthem written in 1942 by Paul Roberts and Shelby Darnell (a pseudonym for producer Bob Miller).
- `d9s1` The song was completed, along with other tunes, on Swan's Island, Maine, where Paul Roberts visited and performed with his soon to become wife, Annie Marrithew, during World War II.
- `d9s2` The song enjoyed its greatest popularity during the war years.
- `d9s3` The "somewhere" in the title of the song refers to an idealistic version of heaven reserved for the brave U.S. soldiers fighting the Axis Powers, somewhat akin to the concept of Valhalla.
- `d9s4` The verses are a narrative of a young man who is crippled, but still yearns to fight and earn his place in this patriotic afterlife.

**d10：Soulsec**
- `d10s0` The British band Soulsec (formerly known as The Faithband or the 'Paul Roberts Band') is the solo project of the ex Stranglers frontman Paul Roberts.

### 由这道题生成的 SFT 样本（9 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=1 | d2 | u1 —; u2 ✅ none ← d2s0; u3 — |
| sftorder1 t=3 | d2, d7, d3 | u1 —; u2 ✅ none ← d2s0; u3 — |
| sftorder1 t=9 | d2, d7, d3, d10, d8, d9, d1, d4, d5 | u1 ✅ guitar ← d5s0; u2 ✅ none ← d2s0; u3 ✅ Matt Shultz ← d5s0,d2s0 |
| sftorder1 t=10 | d2, d7, d3, d10, d8, d9, d1, d4, d5, d6 | u1 ✅ guitar ← d5s0; u2 ✅ none ← d2s0; u3 ✅ Matt Shultz ← d5s0,d2s0 |
| sftorder2 t=2 | d7, d5 | u1 ✅ guitar ← d5s0; u2 —; u3 — |
| sftorder2 t=6 | d7, d5, d6, d3, d10, d2 | u1 ✅ guitar ← d5s0; u2 ✅ none ← d2s0; u3 ✅ Matt Shultz ← d5s0,d2s0 |
| sftorder3 t=1 | d5 | u1 ✅ guitar ← d5s0; u2 —; u3 — |
| sftorder3 t=5 | d5, d9, d10, d8, d6 | u1 ✅ guitar ← d5s0; u2 —; u3 — |
| sftorder3 t=7 | d5, d9, d10, d8, d6, d1, d2 | u1 ✅ guitar ← d5s0; u2 ✅ none ← d2s0; u3 ✅ Matt Shultz ← d5s0,d2s0 |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 14 题：`hotpotqa_5ac250355542992f1f2b384b`

- 数据集 / 题型：hotpotqa / comparison（unit 构造类型 comparison）
- 划分：train；特殊情况：无
- 问题：Who had more diverse credits in films, Charles Burnett or Patricio Guzmán?
- 源答案：Charles Burnett

### 复核原因

**3 靠数列表项来比较（谁的电影职务更多样），把定义句当作完整列表**

> Caveat: the conclusion treats the defining descriptions as complete role lists, as the source gold does.

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | film credits (roles) of Charles Burnett | false | film director, film producer, writer, editor, actor, photographer, and cinematographer | — |
| u2 | film credits (roles) of Patricio Guzmán | false | documentary film director （film director; director） | — |
| u3 | which of Charles Burnett and Patricio Guzmán had more diverse credits in films | true | Charles Burnett （Burnett） | u1, u2 |

**u1 证据**
- support 第 1 组：
  - `d1s0` (Charles Burnett (director)) Charles Burnett (born April 13, 1944, in Vicksburg, Mississippi) is an African-American film director, film producer, writer, editor, actor, photographer, and cinematographer.

**u2 证据**
- support 第 1 组：
  - `d9s0` (Patricio Guzmán) Patricio Guzmán Lozanes (born August 11, 1941) is a Chilean documentary film director.

**u3 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Comparison (count of film credits): two fact units plus a conclusion unit; no presupposition (value comparison).
- u1 and u2 take the role lists from the defining descriptions: seven roles for Burnett, 'documentary film director' for Guzman. Nostalgia for the Light sentence 2 adds that Guzman narrated one documentary; the comparison holds either way.
- Killer of Sheep sentence 0 (written, directed, produced, shot) lists only part of Burnett's roles and is not alternative support for the full list.
- Caveat: the conclusion treats the defining descriptions as complete role lists, as the source gold does.

### 全部文档（`*` = gold 引用的句子）

**d1：Charles Burnett (director)**
- *`d1s0` Charles Burnett (born April 13, 1944, in Vicksburg, Mississippi) is an African-American film director, film producer, writer, editor, actor, photographer, and cinematographer.
- `d1s1` His most popular films include "Killer of Sheep" (1978), "My Brother's Wedding" (1983), "To Sleep with Anger" (1990), "The Glass Shield" (1994), and "" (2007).
- `d1s2` He has been involved in other types of motion pictures including shorts, documentaries, and a TV series.

**d2：Selma, Lord, Selma**
- `d2s0` Selma, Lord, Selma is a 1999 American film based on true events that happened in March 1965, known as Bloody Sunday in Selma, Alabama.
- `d2s1` The film tells the story through the eyes of an 11-year-old African-American girl named Sheyann Webb (Jurnee Smollett).
- `d2s2` It was directed by Charles Burnett, one of the pioneers of black American independent cinema.
- `d2s3` It premiered as a television movie on ABC on January 17, 1999.

**d3：Salvador Allende (film)**
- `d3s0` Salvador Allende is a 2004 documentary film about Chilean president Salvador Allende, from his election campaign to the "coup d'état" which ended his life.
- `d3s1` It was directed by Patricio Guzmán and screened out of competition at the 2004 Cannes Film Festival.

**d4：Nostalgia for the Light**
- `d4s0` Nostalgia for the Light (Spanish: "Nostalgia de la Luz" ) is a documentary released in 2010 by Patricio Guzmán to address the lasting impacts of Augusto Pinochet’s dictatorship.
- `d4s1` Guzmán focuses on the similarities between astronomers researching humanity’s past, in an astronomical sense, and the struggle of many Chilean women who still search, after decades, for the remnants of their relatives executed during the dictatorship.
- `d4s2` Patricio Guzmán narrates the documentary himself and the documentary includes interviews and commentary from those affected and from astronomers and archeologists.

**d5：Killer of Sheep**
- `d5s0` Killer of Sheep is a 1978 American drama film written, directed, produced, and shot by Charles Burnett.
- `d5s1` It features Henry G. Sanders, Kaycee Moore, and Charles Bracy, among others.
- `d5s2` The drama depicts the culture of urban African-Americans in Los Angeles' Watts district.
- `d5s3` The film's style is often likened to Italian neorealism.

**d6：Hey Joe**
- `d6s0` "Hey Joe" is an American popular song from the 1960s that has become a rock standard and has been performed in many musical styles by hundreds of different artists.
- `d6s1` "Hey Joe" tells the story of a man who is on the run and planning to head to Mexico after shooting his unfaithful wife.
- `d6s2` The song was registered for copyright in the U.S. in 1962 by Billy Roberts.
- `d6s3` However, diverse credits and claims have led to confusion about the song's authorship.
- `d6s4` The earliest known commercial recording of the song is the late-1965 single by the Los Angeles garage band The Leaves; the band then re-recorded the track and released it in 1966 as a follow-up single which became a hit.
- `d6s5` The best-known version is The Jimi Hendrix Experience's 1966 recording.
- `d6s6` The song title is sometimes given as "Hey Joe, Where You Gonna Go?"
- `d6s7` or similar variations.

**d7：Austin Film Society**
- `d7s0` The Austin Film Society (AFS) is a non-profit film society based in Austin, Texas.
- `d7s1` Founded in 1985 to exhibit independent, experimental, foreign and various other non-mainstream art films, the film society has grown from just film exhibition to fostering independent filmmaking in Texas and has served as a cornerstone in building the film industry in Austin.
- `d7s2` The film society also owns and maintains Austin Studios, hosts the annual Texas Film Awards gala, and oversees the Austin Film Society grant program.
- `d7s3` The film society was founded by film director Richard Linklater, who currently serves on the board as artistic director.
- `d7s4` Other notable members on the board and advisory board include Tim McCanlies, Robert Rodriguez, Charles Burnett, Guillermo del Toro, Jonathan Demme, Mike Judge, John Sayles, Steven Soderbergh, Paul Stekler and Quentin Tarantino.

**d8：The Compass Rose (film)**
- `d8s0` The Compass Rose (Spanish: "La rosa de los vientos" ) is a 1983 Spanish drama film directed by Patricio Guzmán.
- `d8s1` It was entered into the 13th Moscow International Film Festival.

**d9：Patricio Guzmán**
- *`d9s0` Patricio Guzmán Lozanes (born August 11, 1941) is a Chilean documentary film director.
- `d9s1` He is internationally renowned for films such as "The Battle of Chile" and "Salvador Allende".

**d10：The Pearl Button**
- `d10s0` The Pearl Button (Spanish: El botón de nácar ) is a 2015 Chilean documentary film directed by Patricio Guzmán.
- `d10s1` It was screened in the main competition section of the 65th Berlin International Film Festival where it won the Silver Bear for Best Script.
- `d10s2` It won the Lumières Award for Best Documentary at the 21st Lumières Awards.
- `d10s3` The filmmaker has described the work as part of a triptych with "Nostalgia for the Light" and potentially a third film focusing on the Andes.

### 由这道题生成的 SFT 样本（8 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=5 | d5, d2, d10, d8, d1 | u1 ✅ film director, film producer, writer, editor, actor, photographer, and cinematographer ← d1s0; u2 —; u3 — |
| sftorder1 t=7 | d5, d2, d10, d8, d1, d7, d9 | u1 ✅ film director, film producer, writer, editor, actor, photographer, and cinematographer ← d1s0; u2 ✅ documentary film director ← d9s0; u3 ✅ Charles Burnett ← d1s0,d9s0 |
| sftorder1 t=9 | d5, d2, d10, d8, d1, d7, d9, d6, d4 | u1 ✅ film director, film producer, writer, editor, actor, photographer, and cinematographer ← d1s0; u2 ✅ documentary film director ← d9s0; u3 ✅ Charles Burnett ← d1s0,d9s0 |
| sftorder1 t=10 | d5, d2, d10, d8, d1, d7, d9, d6, d4, d3 | u1 ✅ film director, film producer, writer, editor, actor, photographer, and cinematographer ← d1s0; u2 ✅ documentary film director ← d9s0; u3 ✅ Charles Burnett ← d1s0,d9s0 |
| sftorder2 t=1 | d9 | u1 —; u2 ✅ documentary film director ← d9s0; u3 — |
| sftorder2 t=2 | d9, d1 | u1 ✅ film director, film producer, writer, editor, actor, photographer, and cinematographer ← d1s0; u2 ✅ documentary film director ← d9s0; u3 ✅ Charles Burnett ← d1s0,d9s0 |
| sftorder2 t=6 | d9, d1, d10, d4, d3, d8 | u1 ✅ film director, film producer, writer, editor, actor, photographer, and cinematographer ← d1s0; u2 ✅ documentary film director ← d9s0; u3 ✅ Charles Burnett ← d1s0,d9s0 |
| sftorder3 t=1 | d1 | u1 ✅ film director, film producer, writer, editor, actor, photographer, and cinematographer ← d1s0; u2 —; u3 — |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 15 题：`hotpotqa_5adde7085542990dbb2f7f01`

- 数据集 / 题型：hotpotqa / comparison（unit 构造类型 comparison）
- 划分：train；特殊情况：无
- 问题：What are both Dichondra and Peperomia?
- 源答案：plants

### 复核原因

**4 证据偏弱：只靠俗名“radiator plant”认定 Peperomia 是植物**

> u2: Peperomia sentence 0 calls it 'radiator plant' and List of Peperomia diseases sentence 0 says the genus includes radiator plant, baby rubber tree, etc. Both rely on the common name; accepted as explicit, but this is the weakest evidence in the record. 'Genus of the Piperaceae family' alone would be an inference.

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | what kind of organism Dichondra is | false | plant （flowering plant; genus of flowering plants） | — |
| u2 | what kind of organism Peperomia is | false | plant （radiator plant; genus of plants） | — |
| u3 | what Dichondra and Peperomia both are | true | plants （plant; plant genera; genera of plants） | u1, u2 |

**u1 证据**
- support 第 1 组：
  - `d3s0` (Dichondra) Dichondra is a small genus of flowering plants in the morning glory family, Convolvulaceae.
- support 第 2 组：
  - `d3s1` (Dichondra) They are prostrate, perennial, herbaceous plants, with creeping stems which take root readily at the leaf nodes.

**u2 证据**
- support 第 1 组：
  - `d5s0` (Peperomia) Peperomia (radiator plant) is one of the 2 large genera of the Piperaceae family, with more than 1000 recorded species.
- support 第 2 组：
  - `d2s0` (List of Peperomia diseases) This is a list of diseases that affect the genus "Peperomia" which includes radiator plant, baby rubber tree ("Peperomia obtusifolia"), emerald ripple peperomia ("Peperomia caperata") and others.

**u3 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Comparison (shared category): two fact units plus a conclusion unit.
- u1: Dichondra sentence 0 ('genus of flowering plants') and sentence 1 ('They are ... herbaceous plants') each state it.
- u2: Peperomia sentence 0 calls it 'radiator plant' and List of Peperomia diseases sentence 0 says the genus includes radiator plant, baby rubber tree, etc. Both rely on the common name; accepted as explicit, but this is the weakest evidence in the record. 'Genus of the Piperaceae family' alone would be an inference.
- Species sentences (Peperomia caperata, wheeleri, argyreia, blanda, alata, tetraphylla) are not used: linking a species to its genus by name is an inference (step3 Osbeckia precedent).

### 全部文档（`*` = gold 引用的句子）

**d1：Peperomia argyreia**
- `d1s0` Peperomia argyreia, the watermelon peperomia or watermelon begonia, is a species of plant in the Piperaceae family.
- `d1s1` Its native range is Bolivia, Brazil, Ecuador, and Venezuela.

**d2：List of Peperomia diseases**
- *`d2s0` This is a list of diseases that affect the genus "Peperomia" which includes radiator plant, baby rubber tree ("Peperomia obtusifolia"), emerald ripple peperomia ("Peperomia caperata") and others.

**d3：Dichondra**
- *`d3s0` Dichondra is a small genus of flowering plants in the morning glory family, Convolvulaceae.
- *`d3s1` They are prostrate, perennial, herbaceous plants, with creeping stems which take root readily at the leaf nodes.
- `d3s2` The flowers are white, greenish or yellowish, 2–3 mm diameter.

**d4：Peperomia tetraphylla**
- `d4s0` Peperomia tetraphylla, known as the acorn peperomia or four-leaved peperomia, is a small plant in the pepper family that grows in Australia, Asia, Africa, New Zealand, Lord Howe Island, and other islands in the Pacific Ocean.
- `d4s1` In New South Wales, it is often seen as an epiphyte or growing on rocks in rainforests. Tiny flowers form on a spike, at the end of the branchlets.
- `d4s2` The specific epithet "tetraphylla" is from the Ancient Greek language, meaning "four leaves".

**d5：Peperomia**
- *`d5s0` Peperomia (radiator plant) is one of the 2 large genera of the Piperaceae family, with more than 1000 recorded species.
- `d5s1` Most of them are compact, small perennial epiphytes growing on rotten wood.
- `d5s2` More than 1500 species have been recorded, occurring in all tropical and subtropical regions of the world, though concentrated in Central America and northern South America.
- `d5s3` A limited number of species (around 17) are found in Africa.

**d6：Dichondra repens**
- `d6s0` Dichondra repens is a small, prostrate, herbaceous plant native to New Zealand and many parts of Australia.
- `d6s1` It is occasionally known as kidney weed in Australia and as Mercury Bay weed in New Zealand.
- `d6s2` Di (Latin) = two; chondros (Greek) = seed; repens (Latin) = creeping / crawling.
- `d6s3` Most commonly called dichondra in Australia.

**d7：Peperomia blanda**
- `d7s0` Peperomia blanda, the arid-land peperomia, is a species of herb in the Piperaceae family.
- `d7s1` The species has a natural pan-tropical distribution that encompasses Asia, Africa, Australasia, Polynesia and the Americas.
- `d7s2` The species typically grows as a perennial, somewhat succulent herb to 30cm in height, though the form varies from prostrate and creeping to up to 60 cm tall depending on environment and genotype.
- `d7s3` The typical habitat is damp rock crevices and steep stream banks.

**d8：Peperomia alata**
- `d8s0` Peperomia alata, the winged peperomia, is a plant species found growing in swamps in Florida, West Indies, Central America, South America.
- `d8s1` In Florida, is apparently rare, known for certain only from Collier County.

**d9：Peperomia wheeleri**
- `d9s0` Peperomia wheeleri is a rare species of flowering plant in the pepper family known by the common name Wheeler's peperomia.
- `d9s1` It is endemic to Puerto Rico, where it is known only from the island of Culebra.
- `d9s2` It has been become rare because of deforestation and grazing by livestock.
- `d9s3` It is a federally listed endangered species of the United States.

**d10：Peperomia caperata**
- `d10s0` Peperomia caperata, the emerald ripple peperomia, is a species of flowering plant in the Piperaceae family, native to Brazil.
- `d10s1` It is a mound-forming evergreen perennial growing to 20 cm tall and wide, with corrugated heart-shaped leaves, and narrow spikes of white flowers 5 - long, in summer.

### 由这道题生成的 SFT 样本（8 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=2 | d1, d2 | u1 —; u2 ✅ plant ← d2s0; u3 — |
| sftorder1 t=4 | d1, d2, d5, d7 | u1 —; u2 ✅ plant ← d5s0; u3 — |
| sftorder1 t=10 | d1, d2, d5, d7, d9, d4, d6, d8, d10, d3 | u1 ✅ plant ← d3s0; u2 ✅ plant ← d5s0; u3 ✅ plants ← d3s0,d5s0 |
| sftorder2 t=3 | d9, d7, d5 | u1 —; u2 ✅ plant ← d5s0; u3 — |
| sftorder2 t=5 | d9, d7, d5, d4, d3 | u1 ✅ plant ← d3s0; u2 ✅ plant ← d5s0; u3 ✅ plants ← d3s0,d5s0 |
| sftorder3 t=3 | d9, d10, d2 | u1 —; u2 ✅ plant ← d2s0; u3 — |
| sftorder3 t=7 | d9, d10, d2, d5, d8, d1, d3 | u1 ✅ plant ← d3s0; u2 ✅ plant ← d5s0; u3 ✅ plants ← d3s0,d5s0 |
| sftorder3 t=8 | d9, d10, d2, d5, d8, d1, d3, d6 | u1 ✅ plant ← d3s0; u2 ✅ plant ← d5s0; u3 ✅ plants ← d3s0,d5s0 |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 16 题：`hotpotqa_5ae0c1c25542993d6555ec43`

- 数据集 / 题型：hotpotqa / comparison（unit 构造类型 comparison）
- 划分：train；特殊情况：by_omission
- 问题：Timo Kotipelto and John Waite, are Finnish?
- 源答案：no

### 复核原因

**4 证据偏弱：由“all-Finnish line-up”推出 Kotipelto 是芬兰人**

> u1: Timo Kotipelto sentence 0 gives only a Finnish birthplace and a Finnish band, which is not support. Fourth Dimension (Stratovarius album) sentence 1 says the album features Kotipelto and is the last Stratovarius album 'featuring an all-Finnish line-up'; it is used as the only support. Flag for review: this is entailment within one sentence, not a direct statement of his nationality.

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | whether Timo Kotipelto is Finnish | false | yes | — |
| u2 | whether John Waite is Finnish | false | no **[by_omission]** | — |
| u3 | whether Timo Kotipelto and John Waite are both Finnish | true | no | u1, u2 |

**u1 证据**
- support 第 1 组：
  - `d4s1` (Fourth Dimension (Stratovarius album)) The album is the band's first to feature vocalist Timo Kotipelto as well as the last with keyboardist Antti Ikonen and drummer Tuomo Lassila, thus being the last Stratovarius album to date featuring an all-Finnish line-up.

**u2 证据**
- support 第 1 组：
  - `d5s0` (John Waite) John Charles Waite (born 4 July 1952) is an English musician.

**u3 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Comparison (yes/no): two fact units plus a conclusion unit.
- u1: Timo Kotipelto sentence 0 gives only a Finnish birthplace and a Finnish band, which is not support. Fourth Dimension (Stratovarius album) sentence 1 says the album features Kotipelto and is the last Stratovarius album 'featuring an all-Finnish line-up'; it is used as the only support. Flag for review: this is entailment within one sentence, not a direct statement of his nationality.
- Kotipelto sentence 1 ('their native Finland') is about the band, not the person, and is not used.
- u2 uses the omission exception (labeling_guide.md 1.1, Exception 2): John Waite sentence 0 is a defining description listing 'English'; no sentence calls him Finnish.
- Timo Kotipelto sentence 0 from the source supporting facts is dropped.

### 全部文档（`*` = gold 引用的句子）

**d1：For the Glory of Nothing**
- `d1s0` For The Glory Of Nothing is the fifth album by Finnish heavy metal band Tarot, released in 1998.
- `d1s1` The album includes a guest appearance from Timo Kotipelto of Stratovarius, who contributes backing vocals to the song "Warhead".

**d2：Stratovarius**
- `d2s0` Stratovarius is a Finnish power metal band that formed in 1984.
- `d2s1` Since their formation, they have released 16 studio albums, 4 DVD and 5 live albums.
- `d2s2` Along with German bands Helloween, Blind Guardian, and Gamma Ray, Stratovarius is considered one of the leading and most influential groups of the power metal genre.
- `d2s3` In its history, the band has gone through many chaotic lineup changes and since 1995 there are no founding members of the band that remain.
- `d2s4` Currently, the longest standing member is singer Timo Kotipelto, who joined in 1994.

**d3：Kotipelto**
- `d3s0` Kotipelto is a Finnish melodic power metal self-named band by Timo Kotipelto created during a hiatus in activity for power metal band Stratovarius.
- `d3s1` Kotipelto has been commercially well received in their native Finland, with a Top 10 single "Beginning" from his first release "Waiting for the Dawn", and lyrics often concentrating on ancient Egyptian themes.

**d4：Fourth Dimension (Stratovarius album)**
- `d4s0` Fourth Dimension is the fourth studio album by power metal band Stratovarius, released on 11 April 1995 through Noise Records.
- *`d4s1` The album is the band's first to feature vocalist Timo Kotipelto as well as the last with keyboardist Antti Ikonen and drummer Tuomo Lassila, thus being the last Stratovarius album to date featuring an all-Finnish line-up.
- `d4s2` Founding member and guitarist Timo Tolkki, who had served as the band's vocalist for their first three albums, still provided background vocals on "Fourth Dimension" before handing over lead singing duties to Kotipelto for all subsequent albums.

**d5：John Waite**
- *`d5s0` John Charles Waite (born 4 July 1952) is an English musician.
- `d5s1` He was lead vocalist for The Babys and Bad English.
- `d5s2` As a solo artist, 1984's "Missing You", was a No. 1 hit on the US "Billboard" Hot 100 and a top ten hit on the UK Singles Chart.

**d6：Jani Liimatainen**
- `d6s0` Jani Allan Kristian Liimatainen (born 9 September 1980 in Kemi, Finland) is a Finnish musician, songwriter and backing vocalist.
- `d6s1` He is the former guitarist and one of the founding members of the power metal band Sonata Arctica.
- `d6s2` He has also performed with Cain's Offering, Altaria and Stratovarius vocalist Timo Kotipelto (his band mate in Cain's Offering).

**d7：Silence (Sonata Arctica album)**
- `d7s0` Silence is the second full-length album by Finnish power metal band Sonata Arctica, released in 2001 through Spinefarm Records.
- `d7s1` It is the only studio album to feature keyboardist Mikko Härkin, and the first album with original member Marko Paasikoski, who returned to the band the previous year.
- `d7s2` Stratovarius lead singer Timo Kotipelto sang guest vocals on the album.

**d8：Blackoustic**
- `d8s0` Blackoustic is a collaborative acoustic album by Stratovarius and Cain's Offering vocalist Timo Kotipelto and ex-Sonata Arctica and Cain's Offering guitarist Jani Liimatainen (credited as Kotipelto & Liimatainen).
- `d8s1` The album was released on October 19, 2012, and entered the Finnish charts at #13 the first week.
- `d8s2` The album is self-financed.
- `d8s3` While initially only sold during performances, the album was eventually released through the Earmusic label, which had released the prior Stratovarius albums since "Polaris".

**d9：Timo Kotipelto**
- `d9s0` Timo Antero Kotipelto (born 15 March 1969 in Lappajärvi, Finland) is the vocalist of the Finnish power metal band Stratovarius and is the creator and vocalist of the power metal band Kotipelto.
- `d9s1` Kotipelto is currently the longest standing member of Stratovarius, after the departure of Timo Tolkki.

**d10：Dreamspace**
- `d10s0` Dreamspace is the third studio album by power metal band Stratovarius, released on 9 February 1994 through Noise Records.
- `d10s1` It is the last Stratovarius album to feature guitarist Timo Tolkki on vocals (after which Timo Kotipelto became the lead singer on 1995's "Fourth Dimension"), as well as the first to feature bassist Jari Kainulainen.

### 由这道题生成的 SFT 样本（9 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=4 | d8, d1, d6, d5 | u1 —; u2 ✅ no ← d5s0; u3 — |
| sftorder1 t=5 | d8, d1, d6, d5, d7 | u1 —; u2 ✅ no ← d5s0; u3 — |
| sftorder1 t=6 | d8, d1, d6, d5, d7, d4 | u1 ✅ yes ← d4s1; u2 ✅ no ← d5s0; u3 ✅ no ← d4s1,d5s0 |
| sftorder1 t=10 | d8, d1, d6, d5, d7, d4, d9, d2, d10, d3 | u1 ✅ yes ← d4s1; u2 ✅ no ← d5s0; u3 ✅ no ← d4s1,d5s0 |
| sftorder2 t=5 | d10, d6, d3, d7, d4 | u1 ✅ yes ← d4s1; u2 —; u3 — |
| sftorder2 t=8 | d10, d6, d3, d7, d4, d9, d1, d5 | u1 ✅ yes ← d4s1; u2 ✅ no ← d5s0; u3 ✅ no ← d4s1,d5s0 |
| sftorder3 t=1 | d5 | u1 —; u2 ✅ no ← d5s0; u3 — |
| sftorder3 t=2 | d5, d4 | u1 ✅ yes ← d4s1; u2 ✅ no ← d5s0; u3 ✅ no ← d4s1,d5s0 |
| sftorder3 t=3 | d5, d4, d10 | u1 ✅ yes ← d4s1; u2 ✅ no ← d5s0; u3 ✅ no ← d4s1,d5s0 |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 17 题：`2wikimultihopqa_b87b12700bdd11eba7f7acde48001122`

- 数据集 / 题型：2wikimultihopqa / compositional（unit 构造类型 bridge）
- 划分：train；特殊情况：无
- 问题：What nationality is Empress Huo Chengjun's father?
- 源答案：Chinese

### 复核原因

**4 证据偏弱：由“in Chinese history”推出 Huo Guang 是中国人**

> Borderline: Huo Guang sentence 0 ('a Western Han politician ... a rare example in Chinese history of a powerful official') and sentence 1 ('one of the most powerful consort kin in Chinese imperial history') are read as explicitly placing him as a Chinese official; no sentence says 'Chinese politician' directly. Reviewer should confirm.

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | father of Empress Huo Chengjun | false | Huo Guang | — |
| u2 | nationality of {u1} | true | Chinese （China） | u1 |

**u1 证据**
- support 第 1 组：
  - `d3s2` (Empress Huo Chengjun) Her father was the statesman Huo Guang, who served as regent for Emperor Zhao and who remained exceedingly powerful during Emperor Xuan's reign until his death in 68 BC.

**u2 证据**
- support 第 1 组：
  - `d2s0` (Huo Guang) Huo Guang (died 68 BC), courtesy name Zimeng (子孟), was a Western Han politician who was a rare example in Chinese history of a powerful official who deposed an emperor for the good of the state rather than to usurp the throne.
- support 第 2 组：
  - `d2s1` (Huo Guang) He was the half-brother of renowned Han general Huo Qubing, and one of the most powerful consort kin in Chinese imperial history.

**起草备注**

- Bridge (compositional): father (optional) then nationality (necessary).
- Borderline: Huo Guang sentence 0 ('a Western Han politician ... a rare example in Chinese history of a powerful official') and sentence 1 ('one of the most powerful consort kin in Chinese imperial history') are read as explicitly placing him as a Chinese official; no sentence says 'Chinese politician' directly. Reviewer should confirm.
- Empress Huo Chengjun sentence 0 ('empress during Han Dynasty') does not state the father's nationality and is not used.

### 全部文档（`*` = gold 引用的句子）

**d1：Eleni Gabre-Madhin**
- `d1s0` Eleni Zaude Gabre- Madhin, an Ethiopian economist with Swiss nationality, is a former Chief Executive Officer of the Ethiopia Commodity Exchange( ECX).
- `d1s1` She has had many years of experience working on agricultural markets – particularly in Sub- Saharan Africa – and has held senior positions in the World Bank, the International Food Policy Research Institute( Washington), and United Nations( Geneva).

**d2：Huo Guang**
- *`d2s0` Huo Guang (died 68 BC), courtesy name Zimeng (子孟), was a Western Han politician who was a rare example in Chinese history of a powerful official who deposed an emperor for the good of the state rather than to usurp the throne.
- *`d2s1` He was the half-brother of renowned Han general Huo Qubing, and one of the most powerful consort kin in Chinese imperial history.

**d3：Empress Huo Chengjun**
- `d3s0` Empress Huo Chengjun (霍成君) (died 54 BC) was an empress during Han Dynasty.
- `d3s1` She was the second wife of Emperor Xuan.
- *`d3s2` Her father was the statesman Huo Guang, who served as regent for Emperor Zhao and who remained exceedingly powerful during Emperor Xuan's reign until his death in 68 BC.
- `d3s3` Her mother's name was Xian (顯).

**d4：Rumbold of Mechelen**
- `d4s0` Saint Rumbold( or" RumoldRomuold") was an Irish or Scottish Christian missionary, although his true nationality is not known for certain.
- `d4s1` He was martyred near Mechelen by two men, whom he had denounced for their evil ways.
- `d4s2` Saint Rumbold's feast day is celebrated by the Roman Catholic Church, and Western Rite Orthodox Churches, on 24 June; and it is celebrated in Ireland on 3 July.
- `d4s3` He is the patron saint of Mechelen, where St. Rumbold's Cathedral possesses an elaborate golden shrine on its high altar, containing relics attributed to the saint.
- `d4s4` It is rumoured that his remains are buried inside the cathedral.
- `d4s5` Twenty- five paintings in the choir illustrate his life.

**d5：Ali Rahuma**
- `d5s0` Ali Khalifa Rahuma( born May 16, 1982) is a Libyan football midfielder who's nationality is Libyan.
- `d5s1` He currently plays for Al- Ittihad, and is a member of the Libya national football team.

**d6：Nayelly Hernández**
- `d6s0` Nayelly Hernández( born 23 February 1986) is a former Mexican female professional squash player.
- `d6s1` She has represented Mexico internationally in several international competitions including the Central American and Caribbean Games, Pan American Games, Women's World Team Squash Championships.
- `d6s2` Nayelly achieved her highest career ranking of 57 in October 2011 during the 2011 PSA World Tour.
- `d6s3` Her husband Chris Walker whose nationality is English is also a professional squash player.
- `d6s4` She joined the Trinity College in 2008 as the first Mexican female to join a US college for squash and graduated in 2010.

**d7：Baglan Mailybayev**
- `d7s0` Baglan Mailybayev( in Kazakh Бағлан Асаубайұлы Майлыбаев) was born on 20 May 1975 in Zhambyl region, Kazakhstan.
- `d7s1` His nationality is Kazakh.
- `d7s2` He is a politician of the Republic of Kazakhstan, Deputy Head of the Presidential Administration of the Republic of Kazakhstan, Doctor of Law( 2002)( under the supervision of Professor Zimanov S.Z.- scientific advisor and academician of National Academy of Sciences of the Republic of Kazakhstan) and Ph.D. in Political Science( 1998).

**d8：Fulco**
- `d8s0` Fulco was the first known missionary Bishop of Estonia.
- `d8s1` He was appointed in 1165 by Eskil, the Danish Archbishop of Lund.
- `d8s2` Before his appointment, Fulco was a Benedictine monk in the abbey of Moutier- la- Celle, near Troyes in France.
- `d8s3` His nationality is not known.
- `d8s4` After his appointment, Fulco appears in sources only once.
- `d8s5` In 1171, Pope Alexander III asked the Archbishop of Trondheim to assign an Estonian monk Nicolaus living in Stavanger to go to Fulco's assistance.
- `d8s6` No further information survives about Fulco's work in Estonia, or whether he ever even got there.

**d9：Khalid al-Habib**
- `d9s0` Khalid al- Habib also believed to use the nom de guerre Khalid al Harbi is an Al- Qaeda leader who has overseen Al- Qaeda operations in Afghanistan.
- `d9s1` In 2005 it was reported that al- Habib died in a US missile strike on the Pakistani village of Damadola though it is unclear whether this is the case as Pakistani officials have claimed that no Al- Qaeda leaders died in the attack.
- `d9s2` al- Habib's nationality is not clear with sources claiming he may be Egyptian or Moroccan.

**d10：Roberto Savio**
- `d10s0` Roberto Savio( born in Rome, Italy, but also holding Argentine nationality) is a journalist, communication expert, political commentator, activist for social and climate justice and advocate of global governance.
- `d10s1` He has spent most of his career with Inter Press Service( IPS), the news agency which he founded in 1964 along with Argentine journalist Pablo Piacentini.
- `d10s2` Savio studied Economics at the University of Parma, followed by post -graduate courses in Development Economics under Gunnar Myrdal, History of Art and International Law in Rome.
- `d10s3` He started his professional career as a research assistant in International Law at the University of Parma.

### 由这道题生成的 SFT 样本（9 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=4 | d5, d4, d6, d2 | u1 —; u2 — |
| sftorder1 t=5 | d5, d4, d6, d2, d3 | u1 ✅ Huo Guang ← d3s2; u2 ✅ Chinese ← d2s0 |
| sftorder1 t=10 | d5, d4, d6, d2, d3, d8, d7, d1, d10, d9 | u1 ✅ Huo Guang ← d3s2; u2 ✅ Chinese ← d2s0 |
| sftorder2 t=4 | d8, d1, d4, d2 | u1 —; u2 — |
| sftorder2 t=6 | d8, d1, d4, d2, d5, d3 | u1 ✅ Huo Guang ← d3s2; u2 ✅ Chinese ← d2s0 |
| sftorder3 t=3 | d6, d5, d3 | u1 ✅ Huo Guang ← d3s2; u2 — |
| sftorder3 t=4 | d6, d5, d3, d2 | u1 ✅ Huo Guang ← d3s2; u2 ✅ Chinese ← d2s0 |
| sftorder3 t=8 | d6, d5, d3, d2, d8, d1, d10, d9 | u1 ✅ Huo Guang ← d3s2; u2 ✅ Chinese ← d2s0 |
| sftorder3 t=9 | d6, d5, d3, d2, d8, d1, d10, d9, d7 | u1 ✅ Huo Guang ← d3s2; u2 ✅ Chinese ← d2s0 |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 18 题：`hotpotqa_5adcdfe05542992c1e3a2448`

- 数据集 / 题型：hotpotqa / bridge（unit 构造类型 bridge）
- 划分：train；特殊情况：无
- 问题：What town in Minnesota hosts a weekly event based on a pre-World War I hobby?
- 源答案：town Ogilvie

### 复核原因

**4 证据偏弱：赛道在 Ogilvie“附近”，而且问题把赛车称为“爱好”**

> Caveats: the question calls racing a 'hobby', and the track is 'near' the town rather than in it; a dirt oval track's racing program is read as dirt track racing. Follows the source gold. Flag for review.

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | pre-World War I hobby on which the weekly event is based | false | dirt track racing | — |
| u2 | town in Minnesota that hosts a weekly {u1} event | true | Ogilvie （Ogilvie, Minnesota; town Ogilvie） | u1 |

**u1 证据**
- support 第 1 组：
  - `d7s1` (Dirt track racing) It began in the United States before World War I and became widespread during the 1920s and 1930s.

**u2 证据**
- support 第 1 组：
  - `d2s0` (Ogilvie Raceway) Ogilvie Raceway, is a 4/10 mile Dirt clay oval race track located near Ogilvie, Minnesota.
  - `d2s1` (Ogilvie Raceway) Named after the nearby town Ogilvie.
  - `d2s2` (Ogilvie Raceway) It hosts a weekly Wissota racing program consisting of Modifieds, Super Stocks, Midwest Modifieds, Modified 4sStreet Stocks and Hornets.

**起草备注**

- Bridge: the pre-World War I hobby (optional) then the Minnesota town hosting a weekly event of it (necessary).
- u1 is identified jointly with u2: Dirt track racing sentence 1 says it began before World War I.
- u2 needs Ogilvie Raceway sentences 0 (dirt clay oval race track near Ogilvie, Minnesota), 1 (Ogilvie is a town) and 2 (weekly racing program) together.
- Caveats: the question calls racing a 'hobby', and the track is 'near' the town rather than in it; a dirt oval track's racing program is read as dirt track racing. Follows the source gold. Flag for review.
- Aliases include the source surface form 'town Ogilvie'.

### 全部文档（`*` = gold 引用的句子）

**d1：St. Peter Armory**
- `d1s0` The St. Peter Armory is a former National Guard Armory in St. Peter, Minnesota, United States.
- `d1s1` Built from 1912 to 1913, it is one of the oldest armories still standing in Minnesota and was the first one to be owned by the state upon its completion.
- `d1s2` It was designed in a restrained Gothic Revival style which captures a transition in Minnesota armory design from heavy, fortresslike buildings to the simpler designs of the 1920s.
- `d1s3` It was listed on the National Register of Historic Places in 1997 for having local significance in the themes of architecture, military history, and social history.
- `d1s4` It was nominated for being an excellent example of Minnesota's pre-World War I armories, as well as for its early status, transitional architecture, and role in St. Peter as a center not only of military affairs but also social and recreational events.

**d2：Ogilvie Raceway**
- *`d2s0` Ogilvie Raceway, is a 4/10 mile Dirt clay oval race track located near Ogilvie, Minnesota.
- *`d2s1` Named after the nearby town Ogilvie.
- *`d2s2` It hosts a weekly Wissota racing program consisting of Modifieds, Super Stocks, Midwest Modifieds, Modified 4sStreet Stocks and Hornets.

**d3：Lore Kruger**
- `d3s0` Lore Kruger (1914–2009) was a German-Jewish photographer and Nazi resistor, known most notably for the photographs taken in pre-World War II Europe.
- `d3s1` Born in Magdeburg, Germany, as Lore Heinemann on March 11, 1914, Kruger was part of a Jewish-German family.
- `d3s2` She grew up taking photographs for fun and soon it became her career.
- `d3s3` As her family fled from rising Nazi sentiment in Germany, Lore Kruger and her camera captured emigration and resistance in turbulent pre-World War II Europe.

**d4：Germany Olympic football team**
- `d4s0` The Germany Olympic football team represents Germany in international football competitions in Olympic Games.
- `d4s1` It has been active since 1908, and first competed in 1912.
- `d4s2` Olympic football was originally an amateur sport, and as the pre-World War II German national team was also amateur, it was able to send a full national team to the games.
- `d4s3` After the war, Germany was divided, but until 1964 East and West competed under the name of "United Team of Germany", although without a combined squad.
- `d4s4` From 1968 West Germany began to compete on its own, but were still forced to send an amateur team, who were not able to match the success of their professional counterparts in the World Cup and European Championship.
- `d4s5` The rules on amateurism were relaxed in the 1980s, which allowed West Germany some success, notably a bronze medal finish in 1988.
- `d4s6` Since 1992 the tournament has been competed by under-23 teams, making Germany's Olympic qualification dependent on the results of the under-21 team.
- `d4s7` Only in 2016 the Germans returned to the Olympic stage, with a silver medal after losing on a penalty shoot-out to hosts Brazil.
- `d4s8` Reunified Germany is now the only World Cup champion without the Olympic gold.

**d5：Dub Mission**
- `d5s0` Dub Mission is a dub, dubstep, roots, and dancehall party which occurs weekly on Sunday nights at San Francisco's Elbo Room club in the Mission district.
- `d5s1` Started by DJ Sep in 1996 as a monthly venue to fill a void in the Bay Area's dub scene, Dub Mission has grown into a weekly event with a loyal fan base, and regularly features prominent dub and reggae musicians as guests.
- `d5s2` Resident DJs of Dub Mission include J Boogie, Ludichris, Vinnie Esparza, and Maneesh the Twister.
- `d5s3` Prominent stars who have performed at Dub Mission events include the Mad Professor, Adrian Sherwood, DJ Collage, Mungo's Hi Fi, Scientist, Tippa Irie, Twilight Circus Dub Sound System, and Tino Corp.

**d6：USCGC Papaw (WLB-308)**
- `d6s0` USCGC "Papaw" (WLB-308) was a sea-going buoy tender whose design is based on the pre-World War II United States Lighthouse Service Tenders.
- `d6s1` The original design was modified to provide an armored cutter capable of wartime missions in addition to her primary mission of Aids to Navigation.
- `d6s2` "Papaw" was built in 1943 by the Marine Iron and Shipbuilding Company of Duluth, Minnesota.
- `d6s3` Commissioned 12 October 1943, she was assigned the home port of San Francisco, California.

**d7：Dirt track racing**
- `d7s0` Dirt track racing is a type of auto racing performed on clay or dirt surfaced oval tracks.
- *`d7s1` It began in the United States before World War I and became widespread during the 1920s and 1930s.
- `d7s2` Two different types of race cars dominated—open wheel racers in the Northeast and West and stock cars in the South.
- `d7s3` While open wheel race cars are purpose-built racing vehicles, stock cars (also known as fendered cars) can be either purpose-built race cars or street vehicles that have been modified to varying degrees.

**d8：Cowtown Rodeo**
- `d8s0` The Cowtown Rodeo is the longest running weekly rodeo in the United States, it was started in 1929.
- `d8s1` The show is at 7:30 on Saturday nights from May through September.
- `d8s2` In 1957 and 1958, Cowtown was syndicated on national television.
- `d8s3` It is located in Pilesgrove, New Jersey and Woodstown, New Jersey.
- `d8s4` Grant Harris and his family have been running the rodeo every Saturday night during the summer months since 1955, when it was first staged as a weekly event.

**d9：Midnight breakfast**
- `d9s0` Midnight breakfast is a generic term for a communal meal served at some American colleges and universities.
- `d9s1` Menu items that are generally considered breakfast foods are served in the school's dining hall late at night (hence "midnight") as a study break before or during final exams, or as a traditional community-building event.
- `d9s2` Midnight breakfast is usually at most a weekly event and at least an annual event, and should not be confused with school dining facilities that operate 24 hours a day on a regular basis.

**d10：De Lysle Ferree Cass**
- `d10s0` De Lysle Ferrée Cass (1887–1973) was a writer of fantasy short stories.
- `d10s1` He had at least six stories published pre-World War I in magazines from the Munsey pulp stable.
- `d10s2` These include: "Oahula the Carnivorous" ("The All-Story" March 1913); "Pilgrims in Love" ("The All-Story" Sep and Oct 1913); "The Love Caprice" ("The All-Story" November 1913); "Love Goes Blindly" ("The All-Story" Dec 1913); "The Man Who Could Not Die" ("All Story" March 1914 and "The All-Story" Mar 7, 1914); and "The White Spot" ("All-Story Cavalier Weekly", Oct 24 and 31, 1914).
- `d10s3` His stories for the Munsey pulps are marked by a frank eroticism unusual for its time, together with frequent settings in Oriental climes.

### 由这道题生成的 SFT 样本（9 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=1 | d2 | u1 —; u2 — |
| sftorder1 t=2 | d2, d7 | u1 ✅ dirt track racing ← d7s1; u2 ✅ Ogilvie ← d2s0,d2s1,d2s2 |
| sftorder1 t=10 | d2, d7, d3, d6, d10, d5, d8, d1, d4, d9 | u1 ✅ dirt track racing ← d7s1; u2 ✅ Ogilvie ← d2s0,d2s1,d2s2 |
| sftorder2 t=2 | d3, d7 | u1 ✅ dirt track racing ← d7s1; u2 — |
| sftorder2 t=5 | d3, d7, d10, d9, d5 | u1 ✅ dirt track racing ← d7s1; u2 — |
| sftorder2 t=7 | d3, d7, d10, d9, d5, d1, d4 | u1 ✅ dirt track racing ← d7s1; u2 — |
| sftorder2 t=8 | d3, d7, d10, d9, d5, d1, d4, d2 | u1 ✅ dirt track racing ← d7s1; u2 ✅ Ogilvie ← d2s0,d2s1,d2s2 |
| sftorder3 t=4 | d4, d3, d1, d7 | u1 ✅ dirt track racing ← d7s1; u2 — |
| sftorder3 t=8 | d4, d3, d1, d7, d10, d6, d9, d2 | u1 ✅ dirt track racing ← d7s1; u2 ✅ Ogilvie ← d2s0,d2s1,d2s2 |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 19 题：`hotpotqa_5ae1fe0b5542997283cd2317`

- 数据集 / 题型：hotpotqa / bridge（unit 构造类型 bridge）
- 划分：train；特殊情况：无
- 问题：University of Alabama in Huntsville is a college located in what county?
- 源答案：Madison

### 复核原因

**5 问题有瑕疵：Huntsville 跨 Madison 和 Limestone 两个县**

> Caveat: Huntsville sentence 2 says the city extends into Limestone County; the answer follows sentence 0 ('primarily in Madison County') and the source gold.

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | city in which the University of Alabama in Huntsville is located | false | Huntsville, Alabama （Huntsville） | — |
| u2 | county in which {u1} is located | true | Madison County （Madison） | u1 |

**u1 证据**
- support 第 1 组：
  - `d6s0` (University of Alabama in Huntsville) The University of Alabama in Huntsville (also known as UAHuntsville or UAH) is a state-supported, public, coeducational research university in Huntsville, Alabama, United States.
- support 第 2 组：
  - `d4s1` (David B. Williams (academic)) He was previously the fifth president of the University of Alabama in Huntsville in Huntsville, Alabama from March 2007 until April 2011, and Vice Provost for Research and Harold Chambers Senior Professor of Materials Science and Engineering at Lehigh University in Bethlehem, Pennsylvania.

**u2 证据**
- support 第 1 组：
  - `d7s0` (Huntsville, Alabama) Huntsville is a city located primarily in Madison County in the Appalachian region of northern Alabama.
- support 第 2 组：
  - `d7s1` (Huntsville, Alabama) Huntsville is the county seat of Madison County.

**起草备注**

- Bridge: the city (optional) then its county (necessary).
- David B. Williams (academic) sentence 1 ('the University of Alabama in Huntsville in Huntsville, Alabama') is alternative support for u1.
- Huntsville, Alabama sentence 1 ('county seat of Madison County') is alternative support for u2.
- Caveat: Huntsville sentence 2 says the city extends into Limestone County; the answer follows sentence 0 ('primarily in Madison County') and the source gold.
- Not used for u1: Cummings Research Park sentences (the park is in Huntsville and UAH is its anchor tenant), which needs an inference.

### 全部文档（`*` = gold 引用的句子）

**d1：ARMOR Doppler Weather Radar**
- `d1s0` ARMOR (Advanced Radar for Meteorological and Operational Research) Doppler weather radar is a C-Band, Dual-Polarimetric Doppler Weather Radar, located at the Huntsville International Airport in Huntsville, Alabama.
- `d1s1` The radar is a collaborative effort between WHNT-TV and the University of Alabama in Huntsville.
- `d1s2` Raw data for the radar is only available to a limited audience, such as UAH employees and NWS meteorologists.
- `d1s3` All ARMOR data is archived at the National Space Science and Technology Center located on the UAH campus.

**d2：AEgis Technologies**
- `d2s0` AEgis Technologies is a privately held small business headquartered in Huntsville, Alabama that specializes in modeling and simulation (M&S) technology and emerging training solutions for both military and commercial applications.
- `d2s1` Mr. Bill Waite and Mr. Steve Hill founded AEgis in 1989, and AEgis has steadily grown with revenues increasing to $60+ million in sales and employment of 325+ professionals.
- `d2s2` More than 30% of its employees have military experience with 50+ employees as Certified Modeling and Simulation Professionals (CMSP).
- `d2s3` For over 25 years, AEgis has been in the forefront of efforts to establish M&S as a stand-alone science and engineering discipline in industry, government and academia.
- `d2s4` AEgis has been involved in the creation of M&S standards and professional certification across the international M&S professional community-of-practice.
- `d2s5` AEgis has received several awards and the company was nominated as one of the Top 20 Best Places to Work in 2012 by the Huntsville/Madison County Chamber of Commerce.
- `d2s6` Corporate headquarters are located in Huntsville, Alabama, with additional offices in Orlando, FL, Albuquerque, New Mexico, Boston, Massachusetts, Washington D.C., and Newport, Rhode Island.

**d3：Huntsville Hospital Tram System**
- `d3s0` The Huntsville Hospital Tram System is an automated people mover system located as part of the Huntsville Hospital System complex in Huntsville, Alabama, United States.
- `d3s1` Operating on a 1890 ft concrete guideway, the trams serve to connect the Huntsville Hospital with the Huntsville Hospital for Women & Children.
- `d3s2` At the time of completion, this was the second hospital people mover system in the United States after the Duke University Medical Center Patient Rapid Transit.
- `d3s3` s of 2010 , this is the only automated people mover system completed in the state of Alabama.

**d4：David B. Williams (academic)**
- `d4s0` David B. Williams is the dean of the College of Engineering at the Ohio State University.
- *`d4s1` He was previously the fifth president of the University of Alabama in Huntsville in Huntsville, Alabama from March 2007 until April 2011, and Vice Provost for Research and Harold Chambers Senior Professor of Materials Science and Engineering at Lehigh University in Bethlehem, Pennsylvania.

**d5：Cummings Research Park**
- `d5s0` Cummings Research Park, located primarily in the city of Huntsville, Alabama is the second largest research park in the United States, and the fourth largest in the world.
- `d5s1` The Research Triangle Park (RTP) in North Carolina is the only research park in the United States that is larger.
- `d5s2` However, since RTP is spread over areas in three counties and intermingled with many non-research firms, and CRP is fully concentrated with strong restrictions to the type of occupants, there is justification to credit CRP as being the largest contiguous research park of its type in America.
- `d5s3` Cummings Research Park is a member of the Association of University Research Parks (AURP ).
- `d5s4` The University of Alabama in Huntsville serves as anchor tenant for the park.
- `d5s5` UAH is a comprehensive research university with more than 8,400 students.
- `d5s6` Half of the university's graduates earn a degree in science or engineering.

**d6：University of Alabama in Huntsville**
- *`d6s0` The University of Alabama in Huntsville (also known as UAHuntsville or UAH) is a state-supported, public, coeducational research university in Huntsville, Alabama, United States.
- `d6s1` The university is accredited by the Southern Association of Colleges and Schools to award baccalaureate, master's and doctoral degrees, and is organized in eight colleges: business administration, education, engineering, honors college, arts, humanities & social sciences, nursing, professional & continuing studies, science and graduate studies.

**d7：Huntsville, Alabama**
- *`d7s0` Huntsville is a city located primarily in Madison County in the Appalachian region of northern Alabama.
- *`d7s1` Huntsville is the county seat of Madison County.
- `d7s2` The city extends west into neighboring Limestone County.
- `d7s3` Huntsville's population was 180,105 as of the 2010 census.
- `d7s4` Huntsville is the third-largest city in Alabama and the largest city in the five-county Huntsville-Decatur-Albertville, AL Combined Statistical Area, which at the 2013 census estimate had a total population of 683,871.
- `d7s5` The Huntsville Metropolitan Area's population was 417,593 in 2010 to become the 2nd largest in Alabama.
- `d7s6` Huntsville metro's population reached 441,000 by 2014.

**d8：University of Alabama School of Medicine**
- `d8s0` The University of Alabama School of Medicine at UAB, or UAB School of Medicine as it is more commonly known, is a public medical school located in Birmingham, Alabama with branch campuses in Huntsville, Montgomery, and at the University of Alabama College of Community Health Sciences in Tuscaloosa.
- `d8s1` Residency programs are also located in Selma, Huntsville and Montgomery.

**d9：Katie Baldwin**
- `d9s0` Katie Baldwin is an American printmaker and book artist living in Huntsville, Alabama.
- `d9s1` She is currently an Assistant Professor at the University of Alabama in Huntsville.
- `d9s2` She received her Bachelor of Fine Arts from Evergreen State College in Olympia, Washington and her Master of Fine Arts from the University of the Arts (Philadelphia).
- `d9s3` She served as a Victor Hammer Fellow at Wells College from 2011-2013.
- `d9s4` Baldwin produced the book "Treasure" at Women's Studio Workshop.
- `d9s5` Baldwin maintains a blog at Queen Anne's Revenge Press with illustrations and discussions of her art.
- `d9s6` She has taught pochoir, woodcut, reductive woodcut, and book art classes at the Center for Book Arts.

**d10：Alabama–Huntsville Chargers men's ice hockey**
- `d10s0` The Alabama–Huntsville Chargers ice hockey (commonly referred to as the UAH Chargers) are an NCAA Division I college ice hockey program that represents the University of Alabama in Huntsville Chargers.

### 由这道题生成的 SFT 样本（8 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=1 | d4 | u1 ✅ Huntsville, Alabama ← d4s1; u2 — |
| sftorder1 t=10 | d4, d1, d5, d10, d8, d9, d6, d2, d3, d7 | u1 ✅ Huntsville, Alabama ← d6s0; u2 ✅ Madison County ← d7s0 |
| sftorder2 t=1 | d7 | u1 —; u2 — |
| sftorder2 t=2 | d7, d6 | u1 ✅ Huntsville, Alabama ← d6s0; u2 ✅ Madison County ← d7s0 |
| sftorder3 t=1 | d2 | u1 —; u2 — |
| sftorder3 t=3 | d2, d5, d4 | u1 ✅ Huntsville, Alabama ← d4s1; u2 — |
| sftorder3 t=7 | d2, d5, d4, d1, d8, d6, d7 | u1 ✅ Huntsville, Alabama ← d6s0; u2 ✅ Madison County ← d7s0 |
| sftorder3 t=8 | d2, d5, d4, d1, d8, d6, d7, d3 | u1 ✅ Huntsville, Alabama ← d6s0; u2 ✅ Madison County ← d7s0 |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 20 题：`hotpotqa_5a745a8755429979e288291e`

- 数据集 / 题型：hotpotqa / comparison（unit 构造类型 comparison）
- 划分：dev；特殊情况：无
- 问题：Wellesley College and Vanderbilt University are both what?
- 源答案：private

### 复核原因

**5 问题有瑕疵：“both what”指代不明**

> Open point: 'both what' is underspecified; 'private' is the only shared attribute the two defining sentences state (a college vs. a university).

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | type of institution Wellesley College is | false | private women's liberal arts college | — |
| u2 | type of institution Vanderbilt University is | false | private research university | — |
| u3 | what Wellesley College and Vanderbilt University both are | true | private （private institutions; private schools） | u1, u2 |

**u1 证据**
- support 第 1 组：
  - `d10s0` (Wellesley College) Wellesley College is a private women's liberal arts college located west of Boston in the town of Wellesley, Massachusetts, United States.

**u2 证据**
- support 第 1 组：
  - `d7s0` (Vanderbilt University) Vanderbilt University (also known informally as Vandy) is a private research university located in Nashville, Tennessee.

**u3 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Comparison ('both what'): one institution-type unit per school plus a conclusion unit; the shared attribute is 'private'.
- Open point: 'both what' is underspecified; 'private' is the only shared attribute the two defining sentences state (a college vs. a university).

### 全部文档（`*` = gold 引用的句子）

**d1：Wellesley College Botanic Gardens**
- `d1s0` The Wellesley College Botanic Gardens (22 acres) are botanical gardens located on the campus of Wellesley College in Wellesley, Massachusetts.
- `d1s1` They are open daily without charge.

**d2：Vanderbilt University School of Nursing**
- `d2s0` Vanderbilt University School of Nursing (VUSN) is one of the graduate schools of Vanderbilt University, located in Nashville, Tennessee.
- `d2s1` VUSN enjoys a close relationship with its university parent and with the separate nonprofit Vanderbilt University Medical Center, known for its highly acclaimed teaching hospital and groundbreaking efforts in electronic medical records.
- `d2s2` The School of Nursing is ranked, along with the Vanderbilt University School of Medicine, in the top 20 in the U.S. News & World Report rankings.

**d3：Whitin Observatory**
- `d3s0` Whitin Observatory is an astronomical observatory owned and operated by Wellesley College.
- `d3s1` Built in 1900, with additions in 1906, 1967, and 20102011, it is located in Wellesley, Massachusetts and named after Wellesley College trustee Mrs. John Crane Whitin (Sarah Elizabeth Whitin) of Whitinsville, who donated the funds for the observatory.
- `d3s2` Astronomer Sarah Frances Whiting was the first director of the new Wellesley College Astronomy Department.

**d4：2011 Vanderbilt Commodores football team**
- `d4s0` The 2011 Vanderbilt Commodores football team represented Vanderbilt University during the 2011 NCAA Division I FBS football season.
- `d4s1` The Commodores played their seven home games at Vanderbilt Stadium at Dudley Field in Nashville, Tennessee, which has been Vanderbilt football's home stadium since 1922.
- `d4s2` The team's head coach was James Franklin, who was in his first year at Vanderbilt.
- `d4s3` Hired at Vanderbilt on December 17, 2010, he was previously the offensive coordinator and "head coach in waiting" at the University of Maryland.
- `d4s4` Vanderbilt has been a member of the Southeastern Conference (SEC) since the league's inception in 1932, and has participated in the conference's Eastern Division since its formation for the 1992 season.
- `d4s5` Vanderbilt completed the 2011 regular season with an overall record of 6–6 and a mark of 2–6 in conference play, finishing in a tie with Kentucky for fourth place in the SEC East.
- `d4s6` They were invited to the Liberty Bowl where they were defeated by Cincinnati 24–31 to finish the season 6–7.
- `d4s7` 2011.
- `d4s8` The seniors of the 2011 Vanderbilt football team became the first class in program history to qualify for two bowl game's while at the school.
- `d4s9` Vanderbilt had only been to bowls in 1955 VS Auburn, 1974 VS Texas Tech, 1982 VS Air Force, and 2008 VS Boston College.

**d5：2012 Vanderbilt Commodores football team**
- `d5s0` The 2012 Vanderbilt Commodores football team represented Vanderbilt University during the 2012 NCAA Division I FBS football season.
- `d5s1` (variously "VU" "Vandy" Vanderbilt "Dores") The Commodores played their six home games at Vanderbilt Stadium at Dudley Field in Nashville, Tennessee, which has been Vanderbilt football's home stadium since 1922.
- `d5s2` The team's head coach was James Franklin, who is in his second year at Vanderbilt.
- `d5s3` Vanderbilt has been a member of the Southeastern Conference (SEC) since the league's inception in 1932, and has participated in the conference's Eastern Division since its formation for the 1992 season.
- `d5s4` On November 11, 2012 Vandy became bowl eligible in back to back years for the first time in its 123-year football history.
- `d5s5` This was the first time since 1935 that Vandy won five SEC games in a year and the first time in 30 years that they won at home against Tennessee.
- `d5s6` Vanderbilt finished the year with the longest current SEC winning streak.
- `d5s7` For the first time since 1948, Vanderbilt finished the season with a top 25 ranking.

**d6：Vanderbilt University School of Medicine**
- `d6s0` Vanderbilt University School of Medicine is a medical school located in Nashville, Tennessee.
- `d6s1` Located in the Vanderbilt University Medical Center on the southeastern side of the Vanderbilt University campus, the School of Medicine claims two Nobel laureates: Earl Wilbur Sutherland, Jr., in 1971, for his discovery of the metabolic regulating compound cyclic AMP, and Stanley Cohen, in 1986, for his discovery with a colleague of epidermal growth factor.

**d7：Vanderbilt University**
- *`d7s0` Vanderbilt University (also known informally as Vandy) is a private research university located in Nashville, Tennessee.
- `d7s1` Founded in 1873, it was named in honor of shipping and rail magnate Cornelius Vanderbilt, who provided the school its initial $1 million endowment despite having never been to the South.
- `d7s2` Vanderbilt hoped that his gift and the greater work of the university would help to heal the sectional wounds inflicted by the Civil War.

**d8：Vanderbilt University Law School**
- `d8s0` Vanderbilt University Law School (also known as Vanderbilt Law School or VLS) is a graduate school of Vanderbilt University.
- `d8s1` Established in 1874, it is one of the oldest law schools in the southern United States.
- `d8s2` Vanderbilt Law has consistently ranked among the top 20 law schools in the nation, and is currently ranked 17th in the 2018 edition of "U.S. News & World Report".
- `d8s3` Vanderbilt Law School enrolls approximately 640 students, with each entering Juris Doctor class consisting of approximately 175 students.

**d9：Alan Schechter**
- `d9s0` Alan Schechter (born 1936) is a Professor Emeritus of Political Science at Wellesley College in Massachusetts.
- `d9s1` He was educated at Amherst College, where he received his AB, and at Columbia University, where he earned his PhD.
- `d9s2` He is a distinguished and award-winning political scientist.
- `d9s3` He was also Hillary Rodham's advisor during her years at Wellesley College and supervised her senior thesis; Susan Estrich's book "The Case for Hillary Clinton" mentions her experience also writing an honors thesis for Professor Schechter (at a different time).
- `d9s4` He remains involved with the college, running the Wellesley in Washington internship program, in which Rodham participated as a student and which continues to send approximately twenty women to Washington for internships each summer.
- `d9s5` Professor Schechter is the former Chairman, Vice-Chairman, and member of the J. William Fulbright Foreign Scholarship Board (Fulbright Program), a Presidential appointment.

**d10：Wellesley College**
- *`d10s0` Wellesley College is a private women's liberal arts college located west of Boston in the town of Wellesley, Massachusetts, United States.
- `d10s1` Founded in 1870 by Henry and Pauline Durant, it is a member of the original Seven Sisters Colleges.
- `d10s2` Wellesley is home to 56 departmental and interdepartmental majors spanning the liberal arts, as well as over 150 student clubs and organizations.
- `d10s3` The college is also known for allowing its students to cross-register at Massachusetts Institute of Technology, Brandeis University, Babson College and Franklin W. Olin College of Engineering.
- `d10s4` Wellesley athletes compete in the NCAA Division III New England Women's and Men's Athletic Conference.

### 由这道题生成的 SFT 样本（8 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=5 | d5, d4, d6, d3, d10 | u1 ✅ private women's liberal arts college ← d10s0; u2 —; u3 — |
| sftorder1 t=9 | d5, d4, d6, d3, d10, d8, d9, d1, d2 | u1 ✅ private women's liberal arts college ← d10s0; u2 —; u3 — |
| sftorder1 t=10 | d5, d4, d6, d3, d10, d8, d9, d1, d2, d7 | u1 ✅ private women's liberal arts college ← d10s0; u2 ✅ private research university ← d7s0; u3 ✅ private ← d10s0,d7s0 |
| sftorder2 t=5 | d1, d9, d2, d5, d7 | u1 —; u2 ✅ private research university ← d7s0; u3 — |
| sftorder2 t=6 | d1, d9, d2, d5, d7, d10 | u1 ✅ private women's liberal arts college ← d10s0; u2 ✅ private research university ← d7s0; u3 ✅ private ← d10s0,d7s0 |
| sftorder2 t=9 | d1, d9, d2, d5, d7, d10, d3, d4, d6 | u1 ✅ private women's liberal arts college ← d10s0; u2 ✅ private research university ← d7s0; u3 ✅ private ← d10s0,d7s0 |
| sftorder3 t=7 | d3, d5, d6, d4, d8, d9, d7 | u1 —; u2 ✅ private research university ← d7s0; u3 — |
| sftorder3 t=8 | d3, d5, d6, d4, d8, d9, d7, d10 | u1 ✅ private women's liberal arts college ← d10s0; u2 ✅ private research university ← d7s0; u3 ✅ private ← d10s0,d7s0 |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 21 题：`hotpotqa_5ab5b95d554299637185c5f8`

- 数据集 / 题型：hotpotqa / bridge（unit 构造类型 bridge）
- 划分：train；特殊情况：无
- 问题：ICarly starred which actress who got her start in "School of Rock"?
- 源答案：Miranda Taylor Cosgrove

### 复核原因

**5 问题有瑕疵：“got her start”可以理解成电影出道，也可以理解成拍广告起步**

> Caveat: Miranda Cosgrove 2 states her film debut, while sentence 1 says her career began with commercials at 3; 'got her start' follows the source gold.

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | actress who got her start in "School of Rock" | false | Miranda Cosgrove （Miranda Taylor Cosgrove） | — |
| u2 | iCarly star who got her start in "School of Rock", given {u1} | true | Miranda Cosgrove （Miranda Taylor Cosgrove） | u1 |

**u1 证据**
- support 第 1 组：
  - `d7s2` (Miranda Cosgrove) Cosgrove's film debut came in 2003, when she appeared as Summer Hathaway in "School of Rock".

**u2 证据**
- support 第 1 组：
  - `d10s1` (ICarly (season 1)) The season introduces Carly Shay (Miranda Cosgrove), Sam Puckett (Jennette McCurdy), Freddie Benson (Nathan Kress), and Spencer Shay (Jerry Trainor).
- support 第 2 组：
  - `d7s4` (Miranda Cosgrove) In 2007, she landed the role of Carly Shay, the lead character on the Nickelodeon teen sitcom "iCarly", on which she starred until 2012.

**起草备注**

- Bridge: u1 finds the actress from School of Rock, u2 confirms the iCarly role.
- Answer normalized from 'Miranda Taylor Cosgrove' to 'Miranda Cosgrove'; full name kept as alias.
- Caveat: Miranda Cosgrove 2 states her film debut, while sentence 1 says her career began with commercials at 3; 'got her start' follows the source gold.
- Miranda Cosgrove 4 added as alternative support for u2. Miranda Cosgrove 0 (source supporting fact) does not state either unit's value.
- Distractors with iCarly roles: Jennette McCurdy, Abby Wilde, Shanley Caswell.

### 全部文档（`*` = gold 引用的句子）

**d1：Mandy Rain**
- `d1s0` Amanda Rose Moseley (born December 20, 1993) better known by her stage name Mandy Rain, is an American recording artist, dancer, and actress.
- `d1s1` Rain started her acting career at a young age.
- `d1s2` In 2007, Rain auditioned for Star Camp, a Nickelodeon television show that focuses on the making of a super star musical group.
- `d1s3` Rain was chosen along with seven other kids to join the show and The Giggle Club.
- `d1s4` The band disbanded shortly after the series' finale.
- `d1s5` Shortly afterwards, The Giggle Club's producer Nick Cannon decided to groom Rain for a solo career.
- `d1s6` Cannon started bringing Rain to recording studios to record songs while he was drafting a show for her called The Diaries of Mandy Rain.
- `d1s7` After hearing one of the tracks Rain had recorded, Cannon got inspired by it and decided to start drafting a different show about three private school girls.
- `d1s8` After several months, Canon formed School Gyrls.
- `d1s9` The original line up featured Rain, Monica Parales, and Jacque Pyles.
- `d1s10` In the summer of 2009, School Gyrls starred in a movie Canon had written called School Gyrls which premiered on Nickelodeon on February 21, 2010.
- `d1s11` Shortly afterwards, they released a self-titled album "School Gyrls".
- `d1s12` Later that year, they also released a holiday album titled "A Very School Gyrls Holla-Day".
- `d1s13` Rain and Pyles left the group shortly after the release of the holiday album to focus on their solo careers.

**d2：The Chardon Polka Band**
- `d2s0` The Chardon Polka Band is an American, Ohio-based, Cleveland-Style polka band.
- `d2s1` It was started by Jake Kouwe in 2003 when he recruited four other teenagers to form a polka band at Chardon High School, and the group was originally called "The Chardon High School Polka Band" and included an accordion, trumpet, saxophone, clarinet, electric guitar, and tuba.
- `d2s2` The group got their start in the school's music room and played at local senior centers and nursing homes in the Chardon area.
- `d2s3` Kouwe cites Weird Al Yankovic as his inspiration for playing the accordion as he started lessons on the accordion after seeing Yankovic in a VH1 special.
- `d2s4` The popular satirist remains a role model for The Chardon Polka Band.
- `d2s5` The band had slowly gained notoriety among Polka fans and in the Cleveland music scene in general, but got mainstream attention when they were featured in a reality show named "Polka Kings" on Reelz in 2015, even though the show was quickly cancelled.
- `d2s6` The band currently plays over 200 shows a year and has grown to be one of the Cleveland music scene's most recognizable performers but also tours nationally and headlines many of the nation's top folk festival and Oktoberfest celebrations, playing a mixture of original music, classic polkas, and covers of pop songs.The band has released five full-length albums, all independently, three of which were nominated for a Polka Hall of Fame award for either the album or one or more songs.

**d3：Abby Wilde**
- `d3s0` Abigail Miriam Dauermann (born February 25, 1989), better known by her stage name Abby Wilde, is an American actress and singer who rose to fame for her role as Stacey Dillsen on "Zoey 101", "iCarly" and "Sam & Cat".
- `d3s1` In 2009, Wilde starred in her first full-length feature film, "Family of Four", which is her only film role to date.

**d4：Anne Triola**
- `d4s0` Anne Triola (born 1924) is an American singer, musician, and actress of stage, film, and television.
- `d4s1` As a comedian and supporting actress, she got her start singing in Hollywood night clubs.
- `d4s2` Triola made her mark in the well known musical film "Lullaby Of Broadway" (1951) and received much praise for her effort in the motion picture "Without Reservations" (1946) that starred John Wayne.
- `d4s3` She participated in five Hollywood films, assisted with USO tours in the Pacific Theater during World War II, and caused audiences to lose themselves in laughter, but Triola may best be remembered for her work as a singer and comedian with the musical theatre that included performances in night clubs all over the country such as the Blue Angel in New York City.

**d5：Princeton Law School**
- `d5s0` The Law School at the College of New Jersey (now Princeton University) was a department of Princeton University from 1847 until 1852.
- `d5s1` It began instruction in 1847 as a modest effort consisting of three professors: Joseph Coerten Hornblower, Richard Stockton Field, and James S. Green.
- `d5s2` Only seven students obtained a law degree before the school closed in 1852.
- `d5s3` The short-lived experiment was the furthest the university got in a recurring ambition, marked by varying levels of effort, to establish a law school.
- `d5s4` Previously, in the 1820s, an attempt was made to organize teaching in law, but this plan ended with the death of the designated professor.
- `d5s5` In 1935, the university once again formed appreciable plans for the start of a law school but was unable to secure a faculty.
- `d5s6` The desire remained after these unsuccessful efforts but aspirations were relegated to thirsting words rather than material preparations.
- `d5s7` In 1974, then president of Princeton, William G. Bowen, selected a committee to investigate and advise on the achievability of a law school.
- `d5s8` The committee recommended plans for a law school be deferred after citing high construction costs.
- `d5s9` Princeton, Brown, and Dartmouth are the only Ivy League schools to lack a law school, and all Princeton graduates who are lawyers will have received their legal training elsewhere.

**d6：True Jackson, VP**
- `d6s0` True Jackson, VP is an American television sitcom that aired on Nickelodeon from November 8, 2008 to August 20, 2011.
- `d6s1` The series starred Keke Palmer, Ashley Argota, Matt Shively, Danielle Bisutti, Greg Proops, Robbie Amell, and Ron Butler.
- `d6s2` The theme song was written by Toby Gad and Keke Palmer and is performed by Palmer.
- `d6s3` The series was shot in front of a live studio audience, which is mentioned at the start of each episode (with the exception of the episode "Mission Gone Bad").
- `d6s4` On May 5, 2009, Nickelodeon renewed the show for a second season of 34 episodes, which premiered on November 14, 2009.
- `d6s5` In 2010, Nickelodeon cancelled the show after two seasons.
- `d6s6` It was then later split, making a third season.
- `d6s7` The pilot episode garnered 4.8 million viewers on its first airing and set network records among kids 6–11, adolescents 9–14 and several other demos, airing after the "iCarly" three-part episode "iGo to Japan".
- `d6s8` The show premiered on Nickelodeon (UK and Ireland) on May 25, 2009 and on Nickelodeon (Latin America) on August 3, 2009.
- `d6s9` The one-hour (two-part) episode entitled "Mystery in Peru" completed the 34 ordered episodes for season two (production wise), after it aired on August 20, 2011.
- `d6s10` Keke Palmer posted a video on her YouTube account and posted on her blog, confirming that "Mystery in Peru" is the series' finale.

**d7：Miranda Cosgrove**
- `d7s0` Miranda Taylor Cosgrove (born May 14, 1993) is an American actress, singer and songwriter.
- `d7s1` Her career began at the age of 3 with several television commercial appearances.
- *`d7s2` Cosgrove's film debut came in 2003, when she appeared as Summer Hathaway in "School of Rock".
- `d7s3` She appeared in a number of minor television roles over several years before coming to prominence as Megan Parker on the Nickelodeon television series "Drake & Josh".
- *`d7s4` In 2007, she landed the role of Carly Shay, the lead character on the Nickelodeon teen sitcom "iCarly", on which she starred until 2012.
- `d7s5` As of May 2010, Cosgrove earned $180,000 per episode of "iCarly", making her the second-highest-paid child star on television, and in 2012 was listed in the "Guinness World Records" as the highest paid child actress.
- `d7s6` Cosgrove also voiced Margo in the animated film "Despicable Me" (2010) and its sequels.
- `d7s7` In 2016, she starred as Shea Moore on the short-lived NBC sitcom "Crowded".

**d8：Shanley Caswell**
- `d8s0` Shanley Caswell (born December 3, 1991) is an American actress.
- `d8s1` She has guest starred in television series such as "", "Bones", "iCarly" and "The Middle".
- `d8s2` She is best known for her starring roles in "Detention" as Riley Jones and as Andrea Perron in "The Conjuring".
- `d8s3` She currently has a recurring role in "".

**d9：Jennette McCurdy**
- `d9s0` Jennette McCurdy (born June 26, 1992) is an American actress, producer, screenwriter, and singer.
- `d9s1` She is best known for her role as Sam Puckett on the Nickelodeon sitcom "iCarly" and its spin-off series "Sam & Cat".
- `d9s2` She has also appeared in a number of television series, including "Victorious", "Zoey 101", "True Jackson VP", "Malcolm in the Middle", and "Lincoln Heights", and has also produced, written, and starred in her own online series titled "What's Next for Sarah?
- `d9s3` ".
- `d9s4` Since May 2015, she has starred in the Netflix/City drama series "Between" as Wiley Day.

**d10：ICarly (season 1)**
- `d10s0` The first season of "iCarly" aired on Nickelodeon from September 8, 2007 to July 25, 2008.
- *`d10s1` The season introduces Carly Shay (Miranda Cosgrove), Sam Puckett (Jennette McCurdy), Freddie Benson (Nathan Kress), and Spencer Shay (Jerry Trainor).
- `d10s2` This is notably the only season without a 1 hour special.

### 由这道题生成的 SFT 样本（6 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=4 | d2, d9, d1, d7 | u1 ✅ Miranda Cosgrove ← d7s2; u2 ✅ Miranda Cosgrove ← d7s4 |
| sftorder1 t=6 | d2, d9, d1, d7, d10, d4 | u1 ✅ Miranda Cosgrove ← d7s2; u2 ✅ Miranda Cosgrove ← d10s1 |
| sftorder1 t=10 | d2, d9, d1, d7, d10, d4, d5, d3, d6, d8 | u1 ✅ Miranda Cosgrove ← d7s2; u2 ✅ Miranda Cosgrove ← d10s1 |
| sftorder2 t=1 | d3 | u1 —; u2 — |
| sftorder2 t=2 | d3, d10 | u1 —; u2 — |
| sftorder3 t=4 | d4, d3, d2, d7 | u1 ✅ Miranda Cosgrove ← d7s2; u2 ✅ Miranda Cosgrove ← d7s4 |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 22 题：`hotpotqa_5ab6a56d554299110f219a46`

- 数据集 / 题型：hotpotqa / comparison（unit 构造类型 comparison）
- 划分：train；特殊情况：无
- 问题：Do both Xylem Inc. and LKQ Corporation sell the similar products?
- 源答案：no

### 复核原因

**5 问题有瑕疵：“产品是否相似”需要主观判断**

> Caveat: 'similar' is a semantic judgment (water technology vs. auto parts), less strictly deterministic than comparing dates.

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | products sold by Xylem Inc. | false | water technology （water technology products） | — |
| u2 | products sold by LKQ Corporation | false | auto parts （used and refurbished auto parts; automotive products） | — |
| u3 | whether Xylem Inc. and LKQ Corporation both sell similar products | true | no | u1, u2 |

**u1 证据**
- support 第 1 组：
  - `d4s0` (Xylem Inc.) Xylem Inc. is a large American water technology provider, enabling customers worldwide to transport, treat, test and efficiently use water in public utility, residential, commercial, agricultural and industrial settings.

**u2 证据**
- support 第 1 组：
  - `d7s0` (LKQ Corporation) LKQ Corporation is an American auto parts company.
- support 第 2 组：
  - `d7s1` (LKQ Corporation) The company is focused on providing wholesale used and refurbished auto parts via its subsidiaries across the United States and the world.
- support 第 3 组：
  - `d7s3` (LKQ Corporation) The company also operates facilities selling recycled automotive products.

**u3 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Comparison (yes/no): one product unit per company plus a conclusion unit.
- LKQ Corporation sentences 0 and 3 are alternative support for u2. Euro Car Parts sentences 0-1 (LKQ bought a car parts distributor) are inference; not used.
- Caveat: 'similar' is a semantic judgment (water technology vs. auto parts), less strictly deterministic than comparing dates.

### 全部文档（`*` = gold 引用的句子）

**d1：Natural Products Association**
- `d1s0` The Natural Products Association or NPA (formerly the NNFA, or the National Nutritional Foods Association) is the largest and oldest nonprofit organization representing the interests of manufacturers and retailers of the natural products industry, which includes organic and health foods, dietary supplements, natural ingredient cosmetics, and other similar products.
- `d1s1` The organization includes more than 1,900 members accounting for more than 10,000 retailers, manufacturers, wholesalers and distributors of natural products.

**d2：Defensive strategy (marketing)**
- `d2s0` Defensive strategy is defined as a marketing tool that helps companies to retain valuable customers that can be taken away by competitors.
- `d2s1` Competitors can be defined as other firms that are located in the same market category or sell similar products to the same segment of people.
- `d2s2` When this rivalry exist, each company has the challenge to protect its brand, growth expectations and profitability in order to have a strong competitive advantage and an adequate reputation among other brands.
- `d2s3` In order to reduce the risk of money losses, firms have to take action and take their competition away from the industry.

**d3：Tobacco-Free Pharmacies**
- `d3s0` Tobacco-Free Pharmacies is a term used to refer to retail pharmacies where the sale of tobacco products is not available.
- `d3s1` Outside the United States, it is rare for pharmacy stores to sell cigarettes and similar products on the same premises as over-the-counter drugs and prescription medication.
- `d3s2` Anti-tobacco campaigners advocate the removal of tobacco from pharmacies due to the health risks associated with smoking and the apparent contradiction of selling cigarettes alongside smoking cessation products and asthma medication.
- `d3s3` Some pharmaceutical retailers counter this argument by reasoning that by selling tobacco, they are more readily able to offer to customers advice and products for quitting smoking.

**d4：Xylem Inc.**
- *`d4s0` Xylem Inc. is a large American water technology provider, enabling customers worldwide to transport, treat, test and efficiently use water in public utility, residential, commercial, agricultural and industrial settings.
- `d4s1` The company does business in more than 150 countries.
- `d4s2` Launched in 2011 from the spinoff of the water-related businesses of ITT Corporation, Xylem is headquartered in Rye Brook, N.Y., with 2015 revenues of $3.65 billion and 12,500 employees worldwide.

**d5：Competitive heterogeneity**
- `d5s0` Competitive heterogeneity is a concept from strategic management that examines why industries do not converge on one best way of doing things.
- `d5s1` In the view of strategic management scholars, the microeconomics of production and competition combine to predict that industries will be composed of identical firms offering identical products at identical prices.
- `d5s2` Deeper analyses of this topic were taken up in industrial organization economics by crossover economics/strategic-management scholars such as Harold Demsetz and Michael Porter.
- `d5s3` Demsetz argued that better-managed firms would make better products (or similar products at lower costs) than their competitors.
- `d5s4` Such firms would translate better products or lower prices (an optimal decision based on lower costs) into higher levels of demand, which would lead to revenue growth.
- `d5s5` These firms would then be larger than the more poorly managed competitors.
- `d5s6` Porter argued that firms in an industry would cluster into strategic groups.
- `d5s7` Each group would be similar and movement between groups would be difficult and costly (barriers to mobility).
- `d5s8` Richard Rumelt and Stephen Lippman demonstrated how firms could differ in an industry in partial equilibrium-like circumstances.
- `d5s9` Richard Nelson and Sidney G. Winter discussed how firms develop differing capabilities.
- `d5s10` During this time, industrial economics focused on industry characteristics, treated the differences among firms in an industry as trivial.
- `d5s11` This was a point of contention within strategy and between strategy and economics from about 1980 to the mid-1990s.

**d6：C3controls**
- `d6s0` c3controls, formerly known as Control Concepts Corporation, is a U.S. manufacturer of electric controls sold worldwide.
- `d6s1` The company manufactures its products to primarily be sold directly to its customers.
- `d6s2` Its line of products includes disconnect switches, contactors, overload relays, pilot lights, push buttons, terminal blocks, general purpose relays, and many other similar products.
- `d6s3` c3controls headquarters is in Beaver, Pennsylvania, where it was started in 1976 by Glenn Taylor.

**d7：LKQ Corporation**
- *`d7s0` LKQ Corporation is an American auto parts company.
- *`d7s1` The company is focused on providing wholesale used and refurbished auto parts via its subsidiaries across the United States and the world.
- `d7s2` As of 2014, it was a Fortune 500 corporation.
- *`d7s3` The company also operates facilities selling recycled automotive products.

**d8：Euro Car Parts**
- `d8s0` Euro Car Parts is a distributor based in the United Kingdom of car parts and accessories, with locations across the United Kingdom.
- `d8s1` The company was bought by LKQ Corporation in October 2011 for £255million.

**d9：Gretchen W. McClain**
- `d9s0` Gretchen W. McClain is an American business executive.
- `d9s1` She currently serves on the Board of Directors for Booz Allen Hamilton and Ametek.
- `d9s2` She served as the President and Chief Executive Officer of Xylem Inc. (), and as the former Chief Director of the International Space Station and Deputy Associate Administrator of Human Space Exploration at NASA.

**d10：Atari Age**
- `d10s0` Atari Age was a magazine distributed to Atari Club members from 1982 until 1984.
- `d10s1` It was published by The Atari Club, Inc., a subsidiary of Atari, Inc. The magazine only covered Atari products and events, offering exclusive deals to its readers, and serving as an advertising and merchandise outlet for the company.
- `d10s2` Atari used the magazine to build brand loyalty.
- `d10s3` The articles extolled Atari games and lavished them with praise, regardless of their comparison to similar products from competitors.
- `d10s4` The magazine was based in Philadelphia, Pennsylvania.

### 由这道题生成的 SFT 样本（8 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=1 | d5 | u1 —; u2 —; u3 — |
| sftorder1 t=2 | d5, d4 | u1 ✅ water technology ← d4s0; u2 —; u3 — |
| sftorder1 t=8 | d5, d4, d2, d10, d3, d8, d9, d1 | u1 ✅ water technology ← d4s0; u2 —; u3 — |
| sftorder1 t=10 | d5, d4, d2, d10, d3, d8, d9, d1, d6, d7 | u1 ✅ water technology ← d4s0; u2 ✅ auto parts ← d7s0; u3 ✅ no ← d4s0,d7s0 |
| sftorder2 t=7 | d3, d8, d1, d2, d10, d9, d7 | u1 —; u2 ✅ auto parts ← d7s0; u3 — |
| sftorder2 t=8 | d3, d8, d1, d2, d10, d9, d7, d4 | u1 ✅ water technology ← d4s0; u2 ✅ auto parts ← d7s0; u3 ✅ no ← d4s0,d7s0 |
| sftorder3 t=7 | d5, d9, d6, d2, d3, d1, d4 | u1 ✅ water technology ← d4s0; u2 —; u3 — |
| sftorder3 t=9 | d5, d9, d6, d2, d3, d1, d4, d10, d7 | u1 ✅ water technology ← d4s0; u2 ✅ auto parts ← d7s0; u3 ✅ no ← d4s0,d7s0 |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 23 题：`2wikimultihopqa_4f103f2e0bdb11eba7f7acde48001122`

- 数据集 / 题型：2wikimultihopqa / compositional（unit 构造类型 bridge）
- 划分：dev；特殊情况：无
- 问题：Which award the performer of song Don'T Bring Me Down got?
- 源答案：Rock and Roll Hall of Fame

### 复核原因

**5 问题有瑕疵：乐队还得过其他奖项，可能有别的正确答案**

> u2: Electric Light Orchestra sentence 14 (inducted into the Rock and Roll Hall of Fame). Open point: sentence 10 ('collected 19 CRIA, 21 RIAA, and 38 BPI awards') names other awards; these are not added as aliases.

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | performer of song Don't Bring Me Down | false | Electric Light Orchestra （ELO; The Electric Light Orchestra） | — |
| u2 | award received by {u1} | true | Rock and Roll Hall of Fame （induction into the Rock and Roll Hall of Fame） | u1 |

**u1 证据**
- support 第 1 组：
  - `d9s0` (Don't Bring Me Down) "Don't Bring Me Down" is the ninth and final track on the English rock band the Electric Light Orchestra's 1979 album "Discovery".
- support 第 2 组：
  - `d1s0` (Don't Bring Me Down (disambiguation)) " Do n't Bring Me Down" is a song by the Electric Light Orchestra.

**u2 证据**
- support 第 1 组：
  - `d3s14` (Electric Light Orchestra) In 2017 the ELO line-up of Wood, Lynne, Bevan and Tandy were inducted into the Rock and Roll Hall of Fame.

**起草备注**

- Bridge (compositional): performer (optional) then award (necessary).
- u1: Don't Bring Me Down (disambiguation) sentence 0 ('is a song by the Electric Light Orchestra') added as alternative support.
- Ambiguity: the context also has 'Don't Bring Me Down' songs by the Animals, the Pretty Things (Montells cover) and Spirits. The question title matches the undisambiguated document, which is the ELO song, as in the source gold; kept as draft.
- u2: Electric Light Orchestra sentence 14 (inducted into the Rock and Roll Hall of Fame). Open point: sentence 10 ('collected 19 CRIA, 21 RIAA, and 38 BPI awards') names other awards; these are not added as aliases.

### 全部文档（`*` = gold 引用的句子）

**d1：Don't Bring Me Down (disambiguation)**
- *`d1s0` " Do n't Bring Me Down" is a song by the Electric Light Orchestra.
- `d1s1` Do n't Bring Me Down may also refer to:

**d2：The Breakers (American band)**
- `d2s0` The Breakers were an American garage rock band from Memphis, Tennessee who were active in the 1960s.
- `d2s1` They became one of the most popular bands in the Memphis area and enjoyed considerable success with their regional hit" Do n't Bring Me No Flowers( I Ai n't Dead Yet)".
- `d2s2` There has been a resurgence of interest in the Breakers amongst garage rock collectors and enthusiasts in recent years.

**d3：Electric Light Orchestra**
- `d3s0` The Electric Light Orchestra (ELO) are an English rock band formed in Birmingham in 1970 by songwriters/multi-instrumentalists Jeff Lynne and Roy Wood with drummer Bev Bevan.
- `d3s1` Their music is characterised by a fusion of Beatlesque pop, classical arrangements and futuristic iconography.
- `d3s2` After Wood's departure in 1972, Lynne became the band's sole leader, arranging and producing every album while writing virtually all of their original material.
- `d3s3` For their initial tenure, Lynne, Bevan and keyboardist Richard Tandy were the group's only consistent members.
- `d3s4` ELO was formed out of Lynne's and Wood's desire to create modern rock and pop songs with classical overtones.
- `d3s5` It derived as an offshoot of Wood's previous band, The Move, of which Lynne and Bevan were also members.
- `d3s6` During the 1970s and 1980s, ELO released a string of top 10 albums and singles, including two LPs that reached the top of British charts: the disco-inspired "Discovery" (1979) and the science-fiction-themed concept album "Time" (1981).
- `d3s7` In 1986, Lynne lost interest in the band and disbanded the group.
- `d3s8` Bevan responded by forming his own band, ELO Part II, which later became the Orchestra.
- `d3s9` After a brief reunion from 2000–01, ELO remained largely inactive until 2014, when Lynne re-formed the band again with Tandy as Jeff Lynne's ELO.
- `d3s10` During ELO's original 14-year period of active recording and touring, they sold over 50 million records worldwide, and collected 19 CRIA, 21 RIAA, and 38 BPI awards.
- `d3s11` For a period in the mid 1970s, the band saw more success in the United States, where they were billed as "the English guys with the big fiddles".
- `d3s12` From 1972 to 1986, ELO accumulated twenty seven Top 40 songs on the UK Singles Chart, and fifteen Top 20 songs on the US "Billboard" Hot 100.
- `d3s13` The band also holds the record for having the most "Billboard" Hot 100 Top 40 hits (20) without a number one single of any band in US chart history.
- *`d3s14` In 2017 the ELO line-up of Wood, Lynne, Bevan and Tandy were inducted into the Rock and Roll Hall of Fame.

**d4：The Montells**
- `d4s0` The Montells were an American garage rock band from Miami, Florida who were active in the 1960s.
- `d4s1` They briefly operated under the name H.M. Subjects and recorded a version of the Pretty Things's" Do n't Bring Me Down," which while in the process of becoming a local hit, became embroiled in a controversy involving Morton Downey, Jr., then a disc jockey at Miami's WFUN and later of talk show fame.
- `d4s2` The song was criticized for its apparently sexually suggestive lyric and the contention that Downey allegedly took payola for the song, an allegation which was never proven.
- `d4s3` The band went on to record another single, once again as the Montells, featuring an A-side for which they are remembered," You Ca n't Make Me."
- `d4s4` They broke up in 1967, but reunited for a performance in 2008.

**d5：Bring Me Down**
- `d5s0` Bring Me Down may refer to:

**d6：Spirits (band)**
- `d6s0` Spirits is a male/ female dance music duo from England who scored two entries on the Hot Dance Music/ Club Play chart in 1995.
- `d6s1` Members are Osmond Wright and Beverly Thomas.
- `d6s2` Their debut single" Do n't Bring Me Down" spent two weeks at number one on the dance chart and it was followed by" Spirit Inside", which hit number twelve.

**d7：Don't Bring Me Down (The Animals song)**
- `d7s0` " Do n't Bring Me Down" is a song composed by Gerry Goffin and Carole King and recorded as a 1966 hit single by the Animals.

**d8：Bring Me Down (You Don't)**
- `d8s0` " Bring Me Down( You Don't)" is a song by British rock band Love Amongst Ruin, written by singer and guitarist Steve Hewitt.
- `d8s1` The song has frequently been performed live by the band.

**d9：Don't Bring Me Down**
- *`d9s0` "Don't Bring Me Down" is the ninth and final track on the English rock band the Electric Light Orchestra's 1979 album "Discovery".
- `d9s1` It is their highest-charting hit in the United States to date.

**d10：O Valencia!**
- `d10s0` " O Valencia!" is the fifth single by the indie rock band
- `d10s1` The Decemberists, and the first released from their fourth studio album," The Crane Wife".
- `d10s2` The music was written by The Decemberists and the lyrics by Colin Meloy.
- `d10s3` It tells a story of two star- crossed lovers.
- `d10s4` The singer falls in love with a person who belongs to an opposing gang.
- `d10s5` At the end of the song, the singer's lover jumps in to defend the singer, who is confronting his lover's brother( the singer's" sworn enemy") and is killed by the bullet intended for the singer.

### 由这道题生成的 SFT 样本（9 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=3 | d7, d10, d9 | u1 ✅ Electric Light Orchestra ← d9s0; u2 — |
| sftorder1 t=5 | d7, d10, d9, d8, d3 | u1 ✅ Electric Light Orchestra ← d9s0; u2 ✅ Rock and Roll Hall of Fame ← d3s14 |
| sftorder1 t=10 | d7, d10, d9, d8, d3, d4, d1, d2, d6, d5 | u1 ✅ Electric Light Orchestra ← d9s0; u2 ✅ Rock and Roll Hall of Fame ← d3s14 |
| sftorder2 t=1 | d3 | u1 —; u2 — |
| sftorder2 t=2 | d3, d6 | u1 —; u2 — |
| sftorder2 t=7 | d3, d6, d10, d5, d8, d2, d1 | u1 ✅ Electric Light Orchestra ← d1s0; u2 ✅ Rock and Roll Hall of Fame ← d3s14 |
| sftorder2 t=8 | d3, d6, d10, d5, d8, d2, d1, d7 | u1 ✅ Electric Light Orchestra ← d1s0; u2 ✅ Rock and Roll Hall of Fame ← d3s14 |
| sftorder3 t=4 | d2, d7, d6, d1 | u1 ✅ Electric Light Orchestra ← d1s0; u2 — |
| sftorder3 t=9 | d2, d7, d6, d1, d9, d5, d10, d4, d3 | u1 ✅ Electric Light Orchestra ← d9s0; u2 ✅ Rock and Roll Hall of Fame ← d3s14 |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 24 题：`hotpotqa_5ac561725542993e66e823ad`

- 数据集 / 题型：hotpotqa / bridge（unit 构造类型 bridge）
- 划分：train；特殊情况：无
- 问题：Which British fortification was a post of passage during a war launched in 1763 by a loose confederation of elements of Native American tribes, primarily from the Great Lakes region?
- 源答案：Fort Ligonier

### 复核原因

**5 问题有瑕疵：问题把原文的两件事合成了一句**

> Caveat: sentence 3 says it was a post of passage to Fort Pitt and, during Pontiac's War, a vital link; the question merges the two. Follows the source gold.

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | war launched in 1763 by a loose confederation of elements of Native American tribes, primarily from the Great Lakes region | false | Pontiac's War （Pontiac's Rebellion; Pontiac's Conspiracy） | — |
| u2 | British fortification that was a post of passage during {u1} | true | Fort Ligonier | u1 |

**u1 证据**
- support 第 1 组：
  - `d8s0` (Pontiac's War) Pontiac's War (also known as Pontiac's Conspiracy or Pontiac's Rebellion) was launched in 1763 by a loose confederation of elements of Native American tribes, primarily from the Great Lakes region, the Illinois Country, and Ohio Country who were dissatisfied with British postwar policies in the Great Lakes region after the British victory in the French and Indian War (1754–1763).

**u2 证据**
- support 第 1 组：
  - `d6s3` (Fort Ligonier) It served as a post of passage to the new Fort Pitt, and during Pontiac's War of 1763, was a vital link in the British communication and supply lines.

**起草备注**

- Bridge: the war (optional) then the fortification (necessary).
- Fort Ligonier sentence 0 (source supporting fact) says 'British fortification' but not the post-of-passage role or Pontiac's War; sentence 3 states both and mentions the British supply lines, so it alone supports u2.
- Caveat: sentence 3 says it was a post of passage to Fort Pitt and, during Pontiac's War, a vital link; the question merges the two. Follows the source gold.

### 全部文档（`*` = gold 引用的句子）

**d1：Battle of Fallen Timbers**
- `d1s0` The Battle of Fallen Timbers (August 20, 1794) was the final battle of the Northwest Indian War, a struggle between Native American tribes affiliated with the Western Confederacy, including support from the British led by Captain Alexander McKillop, against the United States for control of the Northwest Territory (an area north of the Ohio River, east of the Mississippi River, and southwest of the Great Lakes).
- `d1s1` This land had been ceded to the United States in accordance with the Treaty of Paris (1783), but the Native Americans (who had not been party to the treaty) refused to comply with the treaty and relinquish control.
- `d1s2` British army bases were maintained there to support their Native allies.
- `d1s3` This ultimately led to the American offensive and subsequent British-Indian withdrawal from the territory altogether following the Treaty of Greenville.
- `d1s4` The battle, which was a decisive victory for the United States, ended major hostilities in the region until Tecumseh's War and the Battle of Tippecanoe in 1811.

**d2：Northwest Indian War**
- `d2s0` The Northwest Indian War (1785–1795), also known as the Ohio War, Little Turtle's War, and by other names, was a war between the United States and a confederation of numerous Native American tribes, with support from the British, for control of the Northwest Territory.
- `d2s1` It followed centuries of conflict over this territory, first among Native American tribes, and then with the added shifting alliances among the tribes and the European powers of France and Great Britain, and their colonials.

**d3：Great Lakes**
- `d3s0` The Great Lakes (French: "les Grands-Lacs" ), also called the Laurentian Great Lakes and the Great Lakes of North America, are a series of interconnected freshwater lakes located primarily in the upper mid-east region of North America, on the Canada–United States border, which connect to the Atlantic Ocean through the Saint Lawrence River.
- `d3s1` Consisting of Lakes Superior, Michigan, Huron (or Michigan–Huron), Erie, and Ontario, they form the largest group of freshwater lakes on Earth by total area, and second largest by total volume containing 21% of the world's surface fresh water by volume.
- `d3s2` The total surface is 94250 sqmi , and the total volume (measured at the low water datum) is 5439 cumi .
- `d3s3` Due to their sea-like characteristics (rolling waves, sustained winds, strong currents, great depths, and distant horizons) the five Great Lakes have also long been referred to as "inland seas".
- `d3s4` Lake Superior is the second largest lake in the world by area, and Lake Michigan is the largest lake that is entirely within one country.
- `d3s5` The southern half of the Great Lakes is bordered by the Great Lakes Megalopolis.

**d4：Treaty of Saginaw**
- `d4s0` The Treaty of Saginaw, also known as the Treaty with the Chippewa, was made between Gen. Lewis Cass and Chief Mash Kee Yosh, Chief John Okemos, Chief Wasso and other Native American tribes of the Great Lakes region (principally the Ojibwe, but also the Ottawa and Potawatomi) in what is now the United States, on September 24, 1819, proclaimed by the President of the United States on March 25, 1820, and placed in law as 7 Stat.
- `d4s1` 203 .

**d5：Fort Winnebago**
- `d5s0` Fort Winnebago was a 19th-century fortification of the United States Army located on a hill overlooking the eastern end of the portage between the Fox and Wisconsin Rivers east of present-day Portage, Wisconsin.
- `d5s1` It was the middle one of three fortifications along the Fox-Wisconsin Waterway that also included Fort Howard in Green Bay, Wisconsin and Fort Crawford in Prairie du Chien, Wisconsin.
- `d5s2` Fort Winnebago was constructed in 1828 as part of an effort to maintain peace between white settlers and the region's Native American tribes following the Winnebago War of 1827.
- `d5s3` The fort's location was chosen not only because of its proximity to the site of Red Bird's surrender in the Winnebago War, but also because of the strategic importance of the portage on the Fox-Wisconsin Waterway, a heavily traveled connection between the Great Lakes and the Mississippi River.
- `d5s4` Fort Winnebago's location near the portage allowed it to regulate transportation between the lakes and the Mississippi.

**d6：Fort Ligonier**
- `d6s0` Fort Ligonier is a British fortification from the French and Indian War located in Ligonier, Pennsylvania, United States.
- `d6s1` The fort served as a staging area for the Forbes Expedition of 1758.
- `d6s2` During the eight years of its existence as a garrison, Fort Ligonier was never taken by an enemy.
- *`d6s3` It served as a post of passage to the new Fort Pitt, and during Pontiac's War of 1763, was a vital link in the British communication and supply lines.
- `d6s4` It was attacked twice and besieged by the Native Americans, prior to the decisive victory at Bushy Run in August of that year.
- `d6s5` The fort was decommissioned from active service in 1766.
- `d6s6` Today, there is a museum next to the reconstructed fort.
- `d6s7` Inside the museum there are artifacts from the battle.
- `d6s8` An individual can take a guided tour of the fort, and on Fort Ligonier Days, the fort's cannons are fired.

**d7：Indian barrier state**
- `d7s0` The Indian barrier state or buffer state was a British proposal to establish a Native American state in the portion of the Great Lakes region of North America west of the Appalachian Mountains, and bounded by the Ohio and Mississippi rivers and the Great Lakes.
- `d7s1` The concept of establishing such a state, first conceived in the late 1750s, was part of a long-term plan to reconcile the Indian tribes to British rule and diminish hostilities between the tribes and the British Army following its victory in the French and Indian War.
- `d7s2` After the region was assigned to the United States in the 1783 treaty ending the American Revolutionary War, British officials pursued efforts to organize the various tribes within it into a sort of Confederation that would form the basis of an Indian state, independent of the United States and under their tutelage, as a way to protect their fur trade ventures in the region and to block anticipated American attacks upon their remaining North American possessions.

**d8：Pontiac's War**
- *`d8s0` Pontiac's War (also known as Pontiac's Conspiracy or Pontiac's Rebellion) was launched in 1763 by a loose confederation of elements of Native American tribes, primarily from the Great Lakes region, the Illinois Country, and Ohio Country who were dissatisfied with British postwar policies in the Great Lakes region after the British victory in the French and Indian War (1754–1763).
- `d8s1` Warriors from numerous tribes joined the uprising in an effort to drive British soldiers and settlers out of the region.
- `d8s2` The war is named after the Odawa leader Pontiac, the most prominent of many native leaders in the conflict.

**d9：Barnes projectile point**
- `d9s0` Barnes' points are lanceolate Paleo-Indian projectile points distributed throughout the lower northeastern United States, from Missouri to the Great Lakes area, extending into Canada.
- `d9s1` Barnes points are associated with the Early Paleoindian Parkhill complex of the eastern Great Lakes region, with sites being especially common in southwestern Ontario.
- `d9s2` Barnes points have also been found in northeastern Indiana, which suggests affinities with the Great Lakes region during the early and middle portions of the Paleoindian period.
- `d9s3` It is a large, fluted spear point with "delicate ears" and a fishtail base.
- `d9s4` The fluting, or groove in the center of the point, tends to extend nearly the entire length of the point.
- `d9s5` It was first classified in 1963 by William Roosa.
- `d9s6` The Barnes site, in Midland County, Michigan, was first located by Mr. Wallace Hill, whose house was then a few hundred feet from the site.
- `d9s7` The staff of the University of Michigan Museum of Anthropology was informed of the site in 1959.
- `d9s8` William Roosa recognized that the fluting technique on the points, while similar to that of Folsom points, was otherwise unique.

**d10：History of Michigan**
- `d10s0` The history of human activity in Michigan, a U.S. state in the Midwest, began with settlement of the western Great Lakes region by Native Americans perhaps as early as 11,000 BCE.
- `d10s1` The first European to explore Michigan, Étienne Brûlé, came in about 1620.
- `d10s2` The area was part of Canada (New France) from 1668 to 1763.
- `d10s3` In 1701, the French officer Antoine de la Mothe Cadillac, along with fifty-one additional French-Canadians, founded a settlement called Fort Pontchartrain du Détroit, now the city of Detroit.
- `d10s4` When New France was defeated in the French and Indian War, it ceded the region to Britain in 1763.
- `d10s5` After the British defeat in the American Revolutionary War, the Treaty of Paris (1783) expanded the United States' boundaries to include nearly all land east of the Mississippi River and south of Canada.
- `d10s6` Michigan was then part of the "Old Northwest".
- `d10s7` From 1787 to 1800, it was part of the Northwest Territory.
- `d10s8` In 1800, the Indiana Territory was created, and most of the current state Michigan lay within it, with only the easternmost parts of the state remaining in the Northwest Territory.
- `d10s9` In 1802, when Ohio was admitted to the Union, the whole of Michigan was attached to the Territory of Indiana, and so remained until 1805, when the Territory of Michigan was established.

### 由这道题生成的 SFT 样本（8 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=1 | d8 | u1 ✅ Pontiac's War ← d8s0; u2 — |
| sftorder1 t=4 | d8, d7, d10, d2 | u1 ✅ Pontiac's War ← d8s0; u2 — |
| sftorder1 t=6 | d8, d7, d10, d2, d5, d6 | u1 ✅ Pontiac's War ← d8s0; u2 ✅ Fort Ligonier ← d6s3 |
| sftorder1 t=10 | d8, d7, d10, d2, d5, d6, d3, d9, d1, d4 | u1 ✅ Pontiac's War ← d8s0; u2 ✅ Fort Ligonier ← d6s3 |
| sftorder2 t=4 | d2, d3, d5, d6 | u1 —; u2 — |
| sftorder2 t=8 | d2, d3, d5, d6, d9, d7, d4, d8 | u1 ✅ Pontiac's War ← d8s0; u2 ✅ Fort Ligonier ← d6s3 |
| sftorder3 t=2 | d5, d7 | u1 —; u2 — |
| sftorder3 t=8 | d5, d7, d10, d2, d8, d3, d1, d6 | u1 ✅ Pontiac's War ← d8s0; u2 ✅ Fort Ligonier ← d6s3 |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 25 题：`hotpotqa_5a72253f55429971e9dc92e5`

- 数据集 / 题型：hotpotqa / comparison（unit 构造类型 comparison）
- 划分：train；特殊情况：无
- 问题： Liezel Huber and Arantxa Sánchez Vicario, are both six time Grand Slam title winners of what sport?
- 源答案：professional tennis player.

### 复核原因

**5 问题有瑕疵：问题说“六次大满贯”，但文档里的次数对不上，也没有 unit 检查这个前提**

> Caveat: the 'six time' premise is not checked by any unit and does not match the documents exactly (Huber: 5 women's doubles + 2 mixed; Sánchez Vicario: 6 women's doubles).

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | sport of Liezel Huber | false | tennis | — |
| u2 | sport of Arantxa Sánchez Vicario | false | tennis | — |
| u3 | sport in which Liezel Huber and Arantxa Sánchez Vicario are both six-time Grand Slam title winners | true | tennis （professional tennis; professional tennis player） | u1, u2 |

**u1 证据**
- support 第 1 组：
  - `d6s0` (Liezel Huber) Liezel Huber (née Horn; born 21 August 1976) is a South African-American retired tennis player who represents the United States internationally.

**u2 证据**
- support 第 1 组：
  - `d5s0` (Arantxa Sánchez Vicario) Aránzazu Isabel María "Arantxa" Sánchez Vicario (] ; born 18 December 1971) is a Spanish former World No. 1 professional tennis player.
- support 第 2 组：
  - `d4s1` (1995 Wimbledon Championships – Women's Singles) Steffi Graf defeated Sánchez Vicario 4–6, 6–1, 7–5 in the final to win the Ladies' Singles tennis title at the 1995 Wimbledon Championships, giving Graf the sixth Wimbledon title of her career.

**u3 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Comparison ('both ... what sport'): one sport unit per player plus a conclusion unit.
- Answer normalized from 'professional tennis player.' to 'tennis'.
- Liezel Huber sentence 1 (source supporting fact) lists titles but does not name the sport; replaced by sentence 0 ('retired tennis player').
- 1995 Wimbledon Championships – Women's Singles sentence 1 (Graf defeated Sánchez Vicario in the final for the tennis title) is alternative support for u2. Other tournament sentences do not name the sport.
- Caveat: the 'six time' premise is not checked by any unit and does not match the documents exactly (Huber: 5 women's doubles + 2 mixed; Sánchez Vicario: 6 women's doubles).

### 全部文档（`*` = gold 引用的句子）

**d1：Karina Habšudová**
- `d1s0` Karina Habšudová (born 2 August 1973) is a Slovak former professional tennis player.
- `d1s1` She has been ranked as high as 10 in the world (1997).
- `d1s2` Together with Karol Kučera she won the Hopman Cup in 1998.
- `d1s3` Her best performance at a Grand Slam came when she got to the quarter finals of the 1996 French Open, defeating Kristin Godridge, Nathalie Tauziat, Martina Hingis and Anke Huber before losing to Arantxa Sánchez Vicario.

**d2：1994 Australian Open – Mixed Doubles**
- `d2s0` Arantxa Sánchez Vicario and Todd Woodbridge were the defending champions but they competed with different partners that year, Sánchez Vicario with Emilio Sánchez and Woodbridge with Helena Suková.

**d3：1994 US Open – Women's Singles**
- `d3s0` Steffi Graf was the defending champion, but she was defeated in the final by Arantxa Sánchez Vicario, marking the last time Sánchez Vicario defeated Graf at any tournament.

**d4：1995 Wimbledon Championships – Women's Singles**
- `d4s0` Conchita Martínez was the defending champion, but she lost to Arantxa Sánchez Vicario in the semifinals.
- *`d4s1` Steffi Graf defeated Sánchez Vicario 4–6, 6–1, 7–5 in the final to win the Ladies' Singles tennis title at the 1995 Wimbledon Championships, giving Graf the sixth Wimbledon title of her career.

**d5：Arantxa Sánchez Vicario**
- *`d5s0` Aránzazu Isabel María "Arantxa" Sánchez Vicario (] ; born 18 December 1971) is a Spanish former World No. 1 professional tennis player.
- `d5s1` She won four Grand Slam singles titles, six Grand Slam women's doubles titles, and four Grand Slam mixed doubles titles.
- `d5s2` In 1994 she was crowned the ITF World Champion for the year.

**d6：Liezel Huber**
- *`d6s0` Liezel Huber (née Horn; born 21 August 1976) is a South African-American retired tennis player who represents the United States internationally.
- `d6s1` Huber has won four Grand Slam titles in women's doubles with partner Cara Black, one with Lisa Raymond, and two mixed doubles titles with Bob Bryan.
- `d6s2` On 12 November 2007, she became the co-World No. 1 in doubles with Cara Black.
- `d6s3` On 19 April 2010, Huber became the sole No. 1 for the first time in her career.

**d7：1996 US Open – Women's Doubles**
- `d7s0` Gigi Fernández and Natasha Zvereva were the defending champions and successfully defended their title, defeating Jana Novotná and Arantxa Sánchez Vicario 1–6, 6–1, 6–4 in the final.
- `d7s1` It was the 5th US Open, 15th Grand Slam and 66th overall title for Fernández, and the 4th US Open, 15th Grand Slam and 60th overall title, in their respective careers.

**d8：1997 Bausch &amp; Lomb Championships – Doubles**
- `d8s0` Chanda Rubin and Arantxa Sánchez Vicario were the defending champions but they competed with different partners that year, Rubin with Brenda Schultz-McCarthy and Sánchez Vicario with Larisa Savchenko.

**d9：1989 French Open – Women's Singles**
- `d9s0` Steffi Graf was the two-time defending champion, but lost in the final to 17-year-old Arantxa Sánchez Vicario, 7–6, 3–6, 7–5, ending her winning streak of Grand Slam singles titles at five.
- `d9s1` Graf served for the championship at 5–3 in the third set, but lost the game at love and won only three more points in the match from that point.
- `d9s2` It was the first of Sánchez Vicario's three French Open titles, which she also won in 1994 and 1998.

**d10：1996 Wimbledon Championships – Women's Singles**
- `d10s0` Steffi Graf was the defending champion, and she successfully defended her title, defeating Arantxa Sánchez Vicario in the final, in what was a rematch of last year's final.
- `d10s1` With the victory, Graf captured her seventh and final Wimbledon crown, while it marked Sánchez Vicario's last appearance in the ladies' championship match.

### 由这道题生成的 SFT 样本（9 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=1 | d4 | u1 —; u2 ✅ tennis ← d4s1; u3 — |
| sftorder1 t=2 | d4, d6 | u1 ✅ tennis ← d6s0; u2 ✅ tennis ← d4s1; u3 ✅ tennis ← d6s0,d4s1 |
| sftorder1 t=4 | d4, d6, d8, d10 | u1 ✅ tennis ← d6s0; u2 ✅ tennis ← d4s1; u3 ✅ tennis ← d6s0,d4s1 |
| sftorder1 t=10 | d4, d6, d8, d10, d7, d9, d2, d3, d5, d1 | u1 ✅ tennis ← d6s0; u2 ✅ tennis ← d5s0; u3 ✅ tennis ← d6s0,d5s0 |
| sftorder2 t=3 | d10, d1, d4 | u1 —; u2 ✅ tennis ← d4s1; u3 — |
| sftorder2 t=4 | d10, d1, d4, d6 | u1 ✅ tennis ← d6s0; u2 ✅ tennis ← d4s1; u3 ✅ tennis ← d6s0,d4s1 |
| sftorder3 t=2 | d2, d6 | u1 ✅ tennis ← d6s0; u2 —; u3 — |
| sftorder3 t=4 | d2, d6, d9, d7 | u1 ✅ tennis ← d6s0; u2 —; u3 — |
| sftorder3 t=5 | d2, d6, d9, d7, d5 | u1 ✅ tennis ← d6s0; u2 ✅ tennis ← d5s0; u3 ✅ tennis ← d6s0,d5s0 |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 26 题：`2wikimultihopqa_f48d9c60093011ebbdaeac1f6bf848b6`

- 数据集 / 题型：2wikimultihopqa / comparison（unit 构造类型 comparison）
- 划分：dev；特殊情况：无
- 问题：Which film was released first, Upasane or Emilio (Film)?
- 源答案：Upasane

### 复核原因

**6 证据有多种解读：Emilio 原文写的是 2008 年的电影、2016 年上映**

> Emilio (film) sentence 0 calls it 'a 2008 American drama film' while sentence 1 gives the U.S. theatrical release as November 4, 2016 (the triple's value). Treated as production year vs. theatrical release, not a conflict; the answer is Upasane either way. Flag for review.

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | release date of Upasane | false | 1974 | — |
| u2 | release date of Emilio | false | November 4, 2016 （2016） | — |
| u3 | which of Upasane and Emilio was released first | true | Upasane | u1, u2 |

**u1 证据**
- support 第 1 组：
  - `d2s0` (Upasane) Upasane( English: Worship) is a 1974 Kannada musical drama film, directed by Puttanna Kanagal.

**u2 证据**
- support 第 1 组：
  - `d10s1` (Emilio (film)) It was released theatrically in the U.S. on November 4, 2016.

**u3 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Comparison: two release-date units plus a conclusion unit.
- Upasane sentence 0 ('a 1974 Kannada ... film') is taken as stating the release year.
- Emilio (film) sentence 0 calls it 'a 2008 American drama film' while sentence 1 gives the U.S. theatrical release as November 4, 2016 (the triple's value). Treated as production year vs. theatrical release, not a conflict; the answer is Upasane either way. Flag for review.
- Answer capitalization: question writes 'Emilio (Film)'; document title is 'Emilio (film)'.

### 全部文档（`*` = gold 引用的句子）

**d1：Bommalattam (2008 film)**
- `d1s0` Bommalattam is a 2008 Indian Tamil film directed by Bharathiraja starring Arjun Sarja and Nana Patekar in the lead roles.
- `d1s1` Originally filmed in Hindi under the title" Cinema", the film was released first in Tamil.
- `d1s2` Hindi version retitled" Final Cut of Director" had a limited release in 2016.
- `d1s3` This marked Nana Patekar's Tamil film debut.

**d2：Upasane**
- *`d2s0` Upasane( English: Worship) is a 1974 Kannada musical drama film, directed by Puttanna Kanagal.
- `d2s1` The film produced by Rashi brothers, is based on the novel of the same name, written by Devaki Murthy.
- `d2s2` The film mostly had women playing the lead roles, consisting of Aarathi, Leelavathi, M. N. Lakshmi Devi, G. V. Sharadha and Advani Lakshmi Devi. Dr. Govinda Mannur, K. S. Ashwath and Seetharam played the male supporting roles.
- `d2s3` Actor Seetharam was colloquially named as" Upasane" Seetharam for the rest of his career after the release of this film.
- `d2s4` The film dealt with the plight of Sharadha( Aarathi) who intends to pursue her career in classical music.
- `d2s5` The film went on to win multiple high- profile awards at the Karnataka State Film Awards for the year 1974- 75 including Best Film, Best Screenplay and Best Cinematography.
- `d2s6` Aarathi, who played the protagonist at the age of 19, won the Filmfare Best Actress award.

**d3：Lloyd (film)**
- `d3s0` Lloyd is a 2001 American comedy film.
- `d3s1` The film was released on May 4, 2001.

**d4：Single Video Theory**
- `d4s0` Single Video Theory is a music documentary directed by Mark Pellington that follows the making of "Yield", the fifth album by the American alternative rock band Pearl Jam.
- `d4s1` It was released first on VHS on August 4, 1998, and then on DVD on November 24, 1998.

**d5：Coney Island Baby (film)**
- `d5s0` Coney Island Baby is a 2003 comedy- drama in which film producer Amy Hobby made her directorial debut.
- `d5s1` Karl Geary wrote the film and Tanya Ryno was the film's producer.
- `d5s2` The music was composed by Ryan Shore.
- `d5s3` The film was shot in Sligo, Ireland, which is known locally as" Coney Island".
- `d5s4` The film was screened at the Newport International Film Festival.
- `d5s5` Hobby won the Jury Award for" Best First Time Director".
- `d5s6` The film made its premiere television broadcast on the Sundance Channel.

**d6：Empties**
- `d6s0` Empties is a 2007 film directed by Jan Svěrák and written by his father Zdeněk Svěrák, who also stars in the film.
- `d6s1` It was released first in the Czech Republic in March 2007.
- `d6s2` The film is a comedy from the same team which made Kolya.

**d7：Rakka (film)**
- `d7s0` The film was released on YouTube and Steam on 14 June 2017.

**d8：Invasion of the Neptune Men**
- `d8s0` The film was released in 1961 in Japan and was later released in the United States on television.
- `d8s1` In 1998, the film was featured on an episode of" Mystery Science Theater 3000".

**d9：The Wonderful World of Captain Kuhio**
- `d9s0` The film was released in Japan on 10 October 2009.

**d10：Emilio (film)**
- `d10s0` Emilio is a 2008 American drama film written and directed by Kim Jorgensen, starring Walter Perez, Danny Martinez, Alejandro Patino, Wendell Wright, Jesse Garcia, and Ryan McTavish.
- *`d10s1` It was released theatrically in the U.S. on November 4, 2016.

### 由这道题生成的 SFT 样本（7 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=2 | d1, d10 | u1 —; u2 ✅ November 4, 2016 ← d10s1; u3 — |
| sftorder1 t=9 | d1, d10, d5, d4, d7, d8, d6, d9, d3 | u1 —; u2 ✅ November 4, 2016 ← d10s1; u3 — |
| sftorder1 t=10 | d1, d10, d5, d4, d7, d8, d6, d9, d3, d2 | u1 ✅ 1974 ← d2s0; u2 ✅ November 4, 2016 ← d10s1; u3 ✅ Upasane ← d2s0,d10s1 |
| sftorder2 t=7 | d8, d9, d3, d5, d4, d6, d2 | u1 ✅ 1974 ← d2s0; u2 —; u3 — |
| sftorder2 t=9 | d8, d9, d3, d5, d4, d6, d2, d7, d10 | u1 ✅ 1974 ← d2s0; u2 ✅ November 4, 2016 ← d10s1; u3 ✅ Upasane ← d2s0,d10s1 |
| sftorder3 t=5 | d4, d5, d8, d9, d1 | u1 —; u2 —; u3 — |
| sftorder3 t=9 | d4, d5, d8, d9, d1, d6, d7, d10, d2 | u1 ✅ 1974 ← d2s0; u2 ✅ November 4, 2016 ← d10s1; u3 ✅ Upasane ← d2s0,d10s1 |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 27 题：`2wikimultihopqa_3addeb19089411ebbd75ac1f6bf848b6`

- 数据集 / 题型：2wikimultihopqa / bridge_comparison（unit 构造类型 bridge_comparison）
- 划分：train；特殊情况：无
- 问题：Which film has the director born earlier, Six Hours To Lose or Red Riding Hood (2011 Film)?
- 源答案：Six Hours To Lose

### 复核原因

**6 证据有多种解读：电影有两位导演，只按其中一位计算**

> Six Hours to Lose sentence 0 names two directors, Alex Joffé and Jean Lévitte; u1 follows the triple (Alex Joffé). Lévitte's birth date is not in the documents. The answer holds through Joffé. Flag for review (co-directed film).

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | director of film Six Hours to Lose | false | Alex Joffé （Alexandre Joffé） | — |
| u2 | date of birth of {u1} | false | 18 November 1918 （November 18, 1918） | u1 |
| u3 | director of film Red Riding Hood (2011 film) | false | Catherine Hardwicke （Helen Catherine Hardwicke） | — |
| u4 | date of birth of {u3} | false | October 21, 1955 （21 October 1955） | u3 |
| u5 | which of Six Hours to Lose and Red Riding Hood (2011 film) has the director born earlier | true | Six Hours to Lose （Six Hours To Lose） | u2, u4 |

**u1 证据**
- support 第 1 组：
  - `d4s0` (Six Hours to Lose) Six Hours to Lose  is a 1947 French romance film directed by Alex Joffé and Jean Lévitte and starring André Luguet, Denise Grey and Pierre Larquey.

**u2 证据**
- support 第 1 组：
  - `d10s0` (Alex Joffé) Alex Joffé (18 November 1918 – 18 August 1995) was a French film director and screenwriter, known for "Les cracks" (1968), "Fortunat" (1960) and "La grosse caisse" (1965).
- support 第 2 组：
  - `d10s2` (Alex Joffé) Alex Joffé was born on 18 November 1918 in Alexandria, Egypt, as Alexandre Joffé.

**u3 证据**
- support 第 1 组：
  - `d2s0` (Red Riding Hood (2011 film)) Red Riding Hood is a 2011 American romance horror film directed by Catherine Hardwicke, and produced by Leonardo DiCaprio, from a screenplay by David Leslie Johnson.
- support 第 2 组：
  - `d6s1` (Catherine Hardwicke) Her directorial work includes" Thirteen"( 2003), which she co-wrote with Nikki Reed, the film's co-star," Lords of Dogtown"( 2005)," The Nativity Story"( 2006)," Twilight"( 2008)," Red Riding Hood"( 2011)," Plush"( 2013)," Miss You Already"( 2015), and" Miss Bala"( 2019).

**u4 证据**
- support 第 1 组：
  - `d6s0` (Catherine Hardwicke) Helen Catherine Hardwicke( born October 21, 1955) is an American film director, production designer, and screenwriter.

**u5 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Bridge comparison: director/birth-date chain per film plus a conclusion unit.
- Six Hours to Lose sentence 0 names two directors, Alex Joffé and Jean Lévitte; u1 follows the triple (Alex Joffé). Lévitte's birth date is not in the documents. The answer holds through Joffé. Flag for review (co-directed film).
- Alex Joffé sentence 2 added as alternative support for u2.
- Catherine Hardwicke sentence 1 ('Her directorial work includes ... Red Riding Hood (2011)') added as alternative support for u3.
- Answer capitalization normalized from 'Six Hours To Lose'; source form kept in aliases.
- Trap: Red Riding Hood (2003 film) has a different director.

### 全部文档（`*` = gold 引用的句子）

**d1：Red Riding Hood (2003 film)**
- `d1s0` Red Riding Hood is a 2003 Italian horror film loosely based on the story of Little Red Riding Hood, directed by Giacomo Cimini, the film stars Roberto Purvis as Tom Hunter, Justine Powell as Arianna and Kathleen Archebald as Rose McKenzie.

**d2：Red Riding Hood (2011 film)**
- *`d2s0` Red Riding Hood is a 2011 American romance horror film directed by Catherine Hardwicke, and produced by Leonardo DiCaprio, from a screenplay by David Leslie Johnson.
- `d2s1` The film is very loosely based on the folk tale "Little Red Riding Hood" collected by both Charles Perrault under the name "Le Petit Chaperon RougeLittle Red Riding Hood") and several decades later by the Brothers Grimm as "RotkäppchenLittle Red Cap").
- `d2s2` It stars Amanda Seyfried as the title role, with Gary Oldman, Billy Burke, Shiloh Fernandez, Max Irons, Virginia Madsen, Lukas Haas and Julie Christie in supporting roles.
- `d2s3` "Red Riding Hood" had its world premiere at Hollywood on March 7, 2011 and was theatrically released on March 11, 2011, by Warner Bros. Pictures.
- `d2s4` The film received generally negative reviews from critics, with praise for Seyfrield's performance and atmosphere but criticized its characters and story.
- `d2s5` It had grossed over $89 million worldwide against a $42 million budget.

**d3：Max Irons**
- `d3s0` Maximilian Paul Diarmuid Irons( born 17 October 1985) is an English- Irish actor and model.
- `d3s1` He is known for his roles in" Red Riding Hood"( 2011), his first leading role in" Bitter Harvest"( 2017 film)," The White Queen"( 2013)," The Host"( 2013)," Woman in Gold"( 2014)," The Riot Club"( 2014), and" The Wife"( 2018).

**d4：Six Hours to Lose**
- *`d4s0` Six Hours to Lose  is a 1947 French romance film directed by Alex Joffé and Jean Lévitte and starring André Luguet, Denise Grey and Pierre Larquey.
- `d4s1` The film was based on the novel of Robert Brasillach, with the same title "Six heures à perdre", edited posthumously in 1953.
- `d4s2` The film's sets were designed by the art director Paul-Louis Boutié and Guy de Gastyne.

**d5：Tom Thumb and Little Red Riding Hood**
- `d5s0` Tom Thumb and Little Red Riding Hood is a 1962 Mexican fantasy adventure film directed by Roberto Rodríguez.
- `d5s1` It is a sequel to two other imported films," Little Red Riding Hood"( 1960) and" Little Red Riding Hood and Friends"( 1961).
- `d5s2` The dubbed version of the film was theatrically released in United States by K. Gordon Murray in 1965.
- `d5s3` The film was also released on VHS by Something Weird Video in 2002.
- `d5s4` An uncut version of the film with English subtitles was released on DVD as Little Red Riding Hood and Tom Thumb vs. the Monsters.

**d6：Catherine Hardwicke**
- *`d6s0` Helen Catherine Hardwicke( born October 21, 1955) is an American film director, production designer, and screenwriter.
- *`d6s1` Her directorial work includes" Thirteen"( 2003), which she co-wrote with Nikki Reed, the film's co-star," Lords of Dogtown"( 2005)," The Nativity Story"( 2006)," Twilight"( 2008)," Red Riding Hood"( 2011)," Plush"( 2013)," Miss You Already"( 2015), and" Miss Bala"( 2019).

**d7：Little Red Riding Hood (1954 film)**
- `d7s0` Little Red Riding Hood is a German film, directed by Walter Janssen, based on the story of Little Red Riding Hood by the Brothers Grimm.
- `d7s1` It should not be confused with the 1953 German film" Little Red Riding Hood" which is also based on the fairy tale.

**d8：Little Red Riding Hood (1953 film)**
- `d8s0` Little Red Riding Hood is a 1953 West German family film directed by Fritz Genschow and starring Daniela Maris, Werner Stock and Rita- Maria Nowottnick.
- `d8s1` It is based on the fairy tale" Little Red Riding Hood".
- `d8s2` It should not be confused with another German adaptation" Little Red Riding Hood" directed by Walter Janssen, which was released the following year.

**d9：Little Red Riding Hood (1920 film)**
- `d9s0` Little Red Riding Hood is a 1920 Czechoslovak drama film directed by Svatopluk Innemann.

**d10：Alex Joffé**
- *`d10s0` Alex Joffé (18 November 1918 – 18 August 1995) was a French film director and screenwriter, known for "Les cracks" (1968), "Fortunat" (1960) and "La grosse caisse" (1965).
- `d10s1` He was the father of the director Arthur Joffé, as well as Marion (born 1952) and Nina (born 1956).
- *`d10s2` Alex Joffé was born on 18 November 1918 in Alexandria, Egypt, as Alexandre Joffé.
- `d10s3` He was married to Renée Asseo.
- `d10s4` He died on 18 August 1995 in Paris.

### 由这道题生成的 SFT 样本（10 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=7 | d6, d8, d5, d7, d2, d3, d10 | u1 —; u2 —; u3 ✅ Catherine Hardwicke ← d2s0; u4 ✅ October 21, 1955 ← d6s0; u5 — |
| sftorder1 t=8 | d6, d8, d5, d7, d2, d3, d10, d4 | u1 ✅ Alex Joffé ← d4s0; u2 ✅ 18 November 1918 ← d10s0; u3 ✅ Catherine Hardwicke ← d2s0; u4 ✅ October 21, 1955 ← d6s0; u5 ✅ Six Hours to Lose ← d10s0,d6s0 |
| sftorder1 t=10 | d6, d8, d5, d7, d2, d3, d10, d4, d9, d1 | u1 ✅ Alex Joffé ← d4s0; u2 ✅ 18 November 1918 ← d10s0; u3 ✅ Catherine Hardwicke ← d2s0; u4 ✅ October 21, 1955 ← d6s0; u5 ✅ Six Hours to Lose ← d10s0,d6s0 |
| sftorder2 t=1 | d1 | u1 —; u2 —; u3 —; u4 —; u5 — |
| sftorder2 t=4 | d1, d5, d9, d4 | u1 ✅ Alex Joffé ← d4s0; u2 —; u3 —; u4 —; u5 — |
| sftorder2 t=7 | d1, d5, d9, d4, d7, d3, d6 | u1 ✅ Alex Joffé ← d4s0; u2 —; u3 ✅ Catherine Hardwicke ← d6s1; u4 ✅ October 21, 1955 ← d6s0; u5 — |
| sftorder2 t=9 | d1, d5, d9, d4, d7, d3, d6, d2, d10 | u1 ✅ Alex Joffé ← d4s0; u2 ✅ 18 November 1918 ← d10s0; u3 ✅ Catherine Hardwicke ← d2s0; u4 ✅ October 21, 1955 ← d6s0; u5 ✅ Six Hours to Lose ← d10s0,d6s0 |
| sftorder3 t=2 | d3, d6 | u1 —; u2 —; u3 ✅ Catherine Hardwicke ← d6s1; u4 ✅ October 21, 1955 ← d6s0; u5 — |
| sftorder3 t=5 | d3, d6, d10, d1, d2 | u1 —; u2 —; u3 ✅ Catherine Hardwicke ← d2s0; u4 ✅ October 21, 1955 ← d6s0; u5 — |
| sftorder3 t=8 | d3, d6, d10, d1, d2, d7, d8, d4 | u1 ✅ Alex Joffé ← d4s0; u2 ✅ 18 November 1918 ← d10s0; u3 ✅ Catherine Hardwicke ← d2s0; u4 ✅ October 21, 1955 ← d6s0; u5 ✅ Six Hours to Lose ← d10s0,d6s0 |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---

## 第 28 题：`2wikimultihopqa_812e515c0baf11ebab90acde48001122`

- 数据集 / 题型：2wikimultihopqa / inference（unit 构造类型 bridge）
- 划分：dev；特殊情况：unreachable
- 问题：Who is the paternal grandfather of Kaemsekhem?
- 源答案：Khufu

### 复核原因

**7 已处理：“probably the son of”已改为没有证据，请确认**

> Kaemsekhem sentence 0 says he was 'probably the son of Crown Prince Kawab'. The hedge is kept as support because it is the only statement and the source gold relies on it. Flag for review.
> Lead review (2026-11-02): 'probably the son of' is hedged, not an explicit statement; u1 support_sets set to [], so u2 is unreachable.

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | father of Kaemsekhem | false | Kawab （Crown Prince Kawab） | — |
| u2 | father of {u1}, paternal grandfather of Kaemsekhem | true | Khufu （King Khufu） | u1 |

**u1 证据**
- `[]`：原文没有明确陈述

**u2 证据**
- support 第 1 组：
  - `d7s1` (Kawab) He was the eldest son of King Khufu and Queen Meritites I. Kawab served as vizier and was buried in the double mastaba G 7110 - 7120 in the east field which is part of the Giza Necropolis.

**起草备注**

- Inference: father (optional) then his father, the paternal grandfather (necessary).
- Kaemsekhem sentence 0 says he was 'probably the son of Crown Prince Kawab'. The hedge is kept as support because it is the only statement and the source gold relies on it. Flag for review.
- Kawab sentence 1 is cited alone; its extra content (vizier, burial) is not needed.
- Lead review (2026-11-02): 'probably the son of' is hedged, not an explicit statement; u1 support_sets set to [], so u2 is unreachable.

### 全部文档（`*` = gold 引用的句子）

**d1：Henry Krause**
- `d1s0` Henry J." Red" Krause, Jr.( August 28, 1913 – February 20, 1987) was an American football offensive lineman in the National Football League for the Brooklyn Dodgers and the Washington Redskins.
- `d1s1` He played college football at St. Louis University.
- `d1s2` He is the grandfather of Jennifer Krause
- `d1s3` He is the great grandfather of Payton Hoeing

**d2：Kaya Alp**
- `d2s0` Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

**d3：Abd al-Muttalib**
- `d3s0` Abd al- Muttalib Shaybah ibn Hashim( c. 497 – 578) was the grandfather of Islamic prophet Muhammad.

**d4：John Mackay (poet)**
- `d4s0` John Mackay( 1656–1754), known as( The Blind Piper), was a Scottish Gaelic poet and composer, and the grandfather of William Ross.

**d5：Lyon Cohen**
- `d5s0` Lyon Cohen( 1868–1937) was a Polish- born Canadian businessman and a philanthropist.
- `d5s1` He was the grandfather of singer/ poet Leonard Cohen.

**d6：John Westley**
- `d6s0` Rev. John Westley( 1636 – 78) was an English nonconformist minister.
- `d6s1` He was the grandfather of John Wesley( founder of Methodism).

**d7：Kawab**
- `d7s0` Kawab is the name of an ancient Egyptian prince of the 4th Dynasty.
- *`d7s1` He was the eldest son of King Khufu and Queen Meritites I. Kawab served as vizier and was buried in the double mastaba G 7110 - 7120 in the east field which is part of the Giza Necropolis.

**d8：Zhao Shoushan**
- `d8s0` Zhao Shoushan( 12 November 1894 – 20 June 1965) was a KMT general and later Chinese Communist Party politician.
- `d8s1` He is the grandfather of Zhao Leji.

**d9：Fred Le Deux**
- `d9s0` Frederick" Fred" Le Deux( born 4 December 1934) was an Australian rules footballer who played with Geelong in the Victorian Football League( VFL).
- `d9s1` He is the grandfather of Tom Hawkins.

**d10：Kaemsekhem**
- `d10s0` Kaemsekhem was an Ancient Egyptian nobleman and probably the son of Crown Prince Kawab and Hetepheres II.
- `d10s1` He later served as the director of the royal palace.
- `d10s2` He was buried in mastaba G 7660 in the east field, which is part of the Giza Necropolis.

### 由这道题生成的 SFT 样本（6 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=6 | d9, d3, d10, d1, d8, d4 | u1 —; u2 — |
| sftorder1 t=7 | d9, d3, d10, d1, d8, d4, d7 | u1 —; u2 — |
| sftorder1 t=8 | d9, d3, d10, d1, d8, d4, d7, d6 | u1 —; u2 — |
| sftorder1 t=10 | d9, d3, d10, d1, d8, d4, d7, d6, d5, d2 | u1 —; u2 — |
| sftorder2 t=4 | d2, d6, d10, d7 | u1 —; u2 — |
| sftorder3 t=7 | d8, d10, d4, d5, d2, d9, d7 | u1 —; u2 — |

### 复核清单

- [ ] 结构：按题型拆分正确（每跳一个 unit；比较题有事实 unit 和结论 unit），depends_on 正确
- [ ] 描述：只凭问题就能写出，不泄露答案（桥接实体用 {u1} 代替）
- [ ] 答案：expected_answer 写法规范，源答案的原样写法和其他变体在 aliases 里
- [ ] 证据：每个引用句都明确写出了这个值（不靠推断、不是推测语气）
- [ ] 备选证据：10 篇文档（包括干扰文档）里没有漏掉其他明确写出同一值的句子
- [ ] 例外规则：by_omission / presupposition_sets 只用在规则允许的情况
- [ ] SFT 标签：下方每个快照的 SUPPORTED / UNRESOLVED 与证据到达情况一致

复核结论（通过 / 修改 / 退回）：

问题记录：

---
