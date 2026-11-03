# SFT 抽样复核表（train，10 题）

由 `sample_review.py --split train --count 10 --seed 2026` 生成。前几题按特殊情况（presupposition、by_omission、unreachable）各抽一题，其余按数据集 × 题型轮流抽取。

| # | sample_id | 数据集 / 题型 | 划分 | 特殊情况 | 复核原因 |
|---|---|---|---|---|---|
| 1 | `hotpotqa_5addad5c5542995b365fab5c` | hotpotqa / bridge | train | presupposition | — |
| 2 | `hotpotqa_5ae0c1c25542993d6555ec43` | hotpotqa / comparison | train | by_omission | — |
| 3 | `hotpotqa_5a905fb455429916514e7496` | hotpotqa / comparison | train | unreachable | — |
| 4 | `2wikimultihopqa_ed17b36008b511ebbd88ac1f6bf848b6` | 2wikimultihopqa / bridge_comparison | train | — | — |
| 5 | `2wikimultihopqa_485a0492085911ebbd5bac1f6bf848b6` | 2wikimultihopqa / comparison | train | — | — |
| 6 | `2wikimultihopqa_533e994a0bdd11eba7f7acde48001122` | 2wikimultihopqa / compositional | train | — | — |
| 7 | `2wikimultihopqa_b6f259dc0baf11ebab90acde48001122` | 2wikimultihopqa / inference | train | — | — |
| 8 | `hotpotqa_5adfdcf5554299025d62a367` | hotpotqa / bridge | train | — | — |
| 9 | `hotpotqa_5a7565475542992d0ec05f84` | hotpotqa / comparison | train | presupposition | — |
| 10 | `2wikimultihopqa_015ccd41087711ebbd67ac1f6bf848b6` | 2wikimultihopqa / bridge_comparison | train | — | — |

---

## 第 1 题：`hotpotqa_5addad5c5542995b365fab5c`

- 数据集 / 题型：hotpotqa / bridge（unit 构造类型 bridge）
- 划分：train；特殊情况：presupposition
- 问题：In what year did the state-owned competitor of Air 26 gain flag carrier staus?
- 源答案：1975

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | state-owned competitor of Air 26 | false | TAAG Angola Airlines （TAAG; TAAG Linhas Aéreas de Angola） | — |
| u2 | year in which {u1} gained flag carrier status | true | 1975 | u1 |

**u1 证据**
- `[]`：原文没有明确陈述
- presupposition 第 1 组：
  - `d2s2` (Air 26) Along with all other Angolan airlines except for TAAG, Air 26 is banned from operating within the European Union.
  - `d4s0` (TAAG Angola Airlines) TAAG Angola Airlines E.P. (Portuguese: "TAAG Linhas Aéreas de Angola E.P." ) is the state-owned national airline of Angola.

**u2 证据**
- support 第 1 组：
  - `d4s2` (TAAG Angola Airlines) The airline was originally set up by the government as "DTADivisão dos Transportes Aéreos" in 1938, rechristened "TAAG Angola Airlines" in 1973, and gained flag carrier status in 1975.

**起草备注**

- Bridge: the competitor (optional) then the year (necessary).
- No explicit support for u1: no sentence calls TAAG a competitor of Air 26. Air 26 sentence 2 shows both are Angolan airlines and TAAG Angola Airlines sentence 0 says TAAG is state-owned; 'competitor' is the question's premise. u1 therefore uses presupposition_sets with that pair (extension of rule 7(b); see report).
- Air 26 sentence 0 (source supporting fact) is not needed: sentence 2 already names Air 26 as an Angolan airline.

### 全部文档（`*` = gold 引用的句子）

**d1：Air Nicaragua**
- `d1s0` Nicaragua Airways is the potential future national flag carrier of Nicaragua.
- `d1s1` Its main base is Augusto C. Sandino International Airport, Managua.
- `d1s2` It is the first time in 20 years that Nicaragua will have a national flag carrier, after Aeronica ceased operations in 1991.
- `d1s3` Since then, the flag carrier status was awarded to Nicaragüense de Aviación also known as NICA Airlines.
- `d1s4` Several airlines had tried to become the Nicaraguan flag carrier like CAAL (Central American Airlines), SANSA (Servicios Aereos Nicaraguenses S.A.) but none of these survived a year.
- `d1s5` Today even NICA Airlines (6Y) is registered as the national airline of Nicaragua, the only international flight it operated once (Managua to Miami) and is done under the TACA code (TA) as a full TACA Airlines flight.

**d2：Air 26**
- `d2s0` Air26 - Linhas Aéreas, S.A. is an airline based in Luanda, Angola.
- `d2s1` Founded in 2006, it operates domestic passenger and cargo flights out of the city's Quatro de Fevereiro Airport.
- *`d2s2` Along with all other Angolan airlines except for TAAG, Air 26 is banned from operating within the European Union.
- `d2s3` In 2010, the company had its licence revoked, but it was re-issued on 31 January 2011.

**d3：Air Botswana**
- `d3s0` Air Botswana Corporation is Botswana's state-owned national flag carrier, with its headquarters located in Gaborone.
- `d3s1` It operates scheduled domestic and regional flights from its main base at Sir Seretse Khama International Airport.
- `d3s2` Air Botswana has been loss-making for several years, and there have been various attempts to privatise the company, and frequent changes to the corporation's management and board, so far without reducing the losses.

**d4：TAAG Angola Airlines**
- *`d4s0` TAAG Angola Airlines E.P. (Portuguese: "TAAG Linhas Aéreas de Angola E.P." ) is the state-owned national airline of Angola.
- `d4s1` Based in Luanda, the airline operates an all-Boeing fleet on domestic services within Angola, medium-haul services in Africa and long-haul services to Brazil, Cuba, China and Portugal.
- *`d4s2` The airline was originally set up by the government as "DTADivisão dos Transportes Aéreos" in 1938, rechristened "TAAG Angola Airlines" in 1973, and gained flag carrier status in 1975.
- `d4s3` It is now a member of both the International Air Transport Association and the African Airlines Association.

**d5：Nordica (airline)**
- `d5s0` Nordica is the state-owned Estonian flag carrier headquartered in Tallinn and based at Lennart Meri Tallinn Airport.
- `d5s1` It is the largest air carrier at Lennart Meri Tallinn Airport.
- `d5s2` The airline was formed after the 2015 bankruptcy of the previous flag carrier Estonian Air.
- `d5s3` Since most of the flights are marketed by LOT Polish Airlines, which owns 49% of the shares and a member of the Star Alliance, Nordica also carries LOT's flight codes and callsign on most of its flights.
- `d5s4` Through its subsidiary Regional Jet in a partnership with Scandinavian Airlines, Regional Jet operates four ATR72-600s between Copenhagen, Aarhus, Aalborg, Billund, Goteborg, Hanover and other SK destinations.

**d6：Air Côte d'Ivoire**
- `d6s0` Air Côte d'Ivoire is the flag carrier of Ivory Coast, based in Abidjan.
- `d6s1` The company succeeded the country's former flag carrier Air Ivoire, which went bankrupt in 2011.
- `d6s2` It started operations on 12   2012 (2012--) .

**d7：Air Ukraine**
- `d7s0` Air Ukraine (Ukrainian: Авіалінії України "Avialiniyi Ukrayiny") was a state-owned airline from Ukraine, serving as flag carrier of the country from 1992 to 2002.
- `d7s1` Headquartered in Kiev, Air Ukraine operated scheduled passenger and cargo flights mostly on domestic routes or within the Commonwealth of Independent States, but also to other European cities and to North America.

**d8：Cameroon Airlines**
- `d8s0` Cameroon Airlines was an airline from Cameroon, serving as flag carrier of the country.
- `d8s1` Based in Douala, it operated scheduled services within Africa, as well as to Europe and the Middle East out of its hub at Douala International Airport, with a second network focus on Yaoundé Nsimalen International Airport.
- `d8s2` The company was 96.43 per cent state owned, with the remaining shares having been held by Air France.
- `d8s3` It ceased operations in March 2008; its role as Cameroon's flag carrier was taken over by Camair-Co.

**d9：AirBaltic**
- `d9s0` airBaltic, legally incorporated as AS Air Baltic Corporation, is a state-owned Latvian low-cost carrier and the country's flag carrier, with its head office on the grounds of Riga International Airport in Mārupe municipality near Riga.
- `d9s1` Its main hub is at Riga International Airport with further bases at Tallinn Airport and Vilnius Airport.

**d10：SriLankan Airlines**
- `d10s0` SriLankan Airlines (marketed as SriLankan) is the flag carrier of Sri Lanka.
- `d10s1` It was launched in 1979 as Air Lanka, following the termination of operations of the original Sri Lankan flag carrier Air Ceylon.
- `d10s2` Following its partial acquisition in 1998 by Emirates, it was re-branded and introduced the current livery.
- `d10s3` After ending the Emirates partnership, it has continued using its re-branded name and logo.

### 由这道题生成的 SFT 样本（4 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=4 | d5, d7, d6, d8 | u1 —; u2 — |
| sftorder1 t=10 | d5, d7, d6, d8, d2, d1, d10, d3, d9, d4 | u1 ✅ TAAG Angola Airlines ← d2s2,d4s0 [presup]; u2 ✅ 1975 ← d4s2 |
| sftorder2 t=3 | d1, d10, d5 | u1 —; u2 — |
| sftorder2 t=7 | d1, d10, d5, d9, d7, d3, d4 | u1 —; u2 — |

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

## 第 2 题：`hotpotqa_5ae0c1c25542993d6555ec43`

- 数据集 / 题型：hotpotqa / comparison（unit 构造类型 comparison）
- 划分：train；特殊情况：by_omission
- 问题：Timo Kotipelto and John Waite, are Finnish?
- 源答案：no

### 复核原因

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

## 第 3 题：`hotpotqa_5a905fb455429916514e7496`

- 数据集 / 题型：hotpotqa / comparison（unit 构造类型 comparison）
- 划分：train；特殊情况：unreachable
- 问题：Gin pahit and Springbokkie, have gin in them?
- 源答案：no

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | whether Gin pahit has gin in it | false | yes | — |
| u2 | whether Springbokkie has gin in it | false | no | — |
| u3 | whether Gin pahit and Springbokkie both have gin in them | true | no | u1, u2 |

**u1 证据**
- support 第 1 组：
  - `d3s0` (Gin pahit) Gin Pahit is an alcoholic drink made with gin and bitters, as enjoyed in colonial Malaya.

**u2 证据**
- `[]`：原文没有明确陈述

**u3 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Comparison (yes/no 'both'): two fact units plus a conclusion unit.
- Gin pahit sentence 1 ('bitter gin') is a name translation, not an ingredient statement; not used.
- No explicit support for u2: Springbokkie sentence 0 lists creme de menthe ('or substitutes') and Amarula, but ingredients are not an Exception 2 attribute (occupation, nationality, category), and '(or substitutes)' leaves the recipe open. So no by_omission and the conclusion is unreachable; see report.

### 全部文档（`*` = gold 引用的句子）

**d1：Kemp Cotton Gin Historic District**
- `d1s0` The Kemp Cotton Gin Historic District encompasses the only cotton gin extant in the Rohwer area of Desha County, Arkansas.
- `d1s1` The gin was built in 1950 by O. O. Kemp, a few years after the closure of the Rohwer War Relocation Center, where as many as 10,000 Japanese-Americans were interned during the Second World War.
- `d1s2` After the center's closure much of its land was returned to agricultural use, and Kemp built this gin near the Missouri Pacific Railroad line that ran through Rohwer.
- `d1s3` In addition to the gin, the complex Kemp built includes a pump house, scale house, and office.
- `d1s4` This entire complex was listed on the National Register of Historic Places in 2005.

**d2：Judd Hill Cotton Gin**
- `d2s0` The Judd Hill Cotton Gin is a historic cotton gin in Judd Hill, Arkansas.
- `d2s1` The gin was part of the Judd Hill Plantation, which was established by businessman Orange Judd Hill in the 1920s and sold to Hill's daughter and her husband, Esther and Samuel Chapin, in 1933.
- `d2s2` The cotton gin was built on the plantation circa 1930; its brick construction, designed to prevent fires, makes it a rarity among extant cotton gins.
- `d2s3` The plantation was successful throughout the 1940s and became one of the largest farms in Poinsett County.
- `d2s4` The cotton gin ceased operations in the 1970s or 1980s, but the plantation is still operated by the Judd Hill Foundation established by Esther Chapin.
- `d2s5` On September 28, 2005, the cotton gin was added to the National Register of Historic Places.

**d3：Gin pahit**
- *`d3s0` Gin Pahit is an alcoholic drink made with gin and bitters, as enjoyed in colonial Malaya.
- `d3s1` The name means "bitter gin" in Malay.

**d4：Konig's Westphalian Gin**
- `d4s0` Konig's Westphalian Gin was a "Steinhäger" gin produced up to the early part of the twentieth century from mineral water at H. C. König's "model distillery" in Steinhagen, Westphalia, Germany, said at the time to be the largest and the oldest gin distillery in the world.
- `d4s1` The gin was first produced in 1640.

**d5：Gimlet (cocktail)**
- `d5s0` The gimlet (pronounced with a hard 'g') is a cocktail made of gin and lime juice.
- `d5s1` A 1928 description of the drink was: "gin, a spot of lime, and soda".
- `d5s2` The description in the 1953 Raymond Chandler novel "The Long Goodbye" stated that "a real gimlet is half gin and half Rose's lime juice and nothing else".
- `d5s3` This is in line with the proportions suggested by "The Savoy Cocktail Book" (1930) which specifies one half Plymouth Gin and one half Rose's Lime Juice Cordial.
- `d5s4` However, modern tastes are less sweet, and generally provide for at least two parts gin to one part of the lime and other non alcoholic elements (see recipes below).

**d6：Gin Gin railway station**
- `d6s0` Gin Gin railway station is a heritage-listed railway station at Mulgrave Street, Gin Gin, Bundaberg Region, Queensland, Australia.
- `d6s1` It was built from 1888 to  1928 .
- `d6s2` It is also known as Gin Gin Railway Station, Goods Shed & Refreshment Rooms.
- `d6s3` It was added to the Queensland Heritage Register on 28 July 2000.

**d7：Gin Act 1736**
- `d7s0` The Spirit Duties Act 1735 (commonly known as the Gin Act of 1736) was an Act of the Parliament of Great Britain establishing a retail tax on gin and annual licenses for gin sellers.
- `d7s1` Designed to curb gin consumption, the law was widely disobeyed and repealed in 1743.

**d8：Sloe gin**
- `d8s0` Sloe gin is a red liqueur made with gin and sloe (blackthorn) drupes, which are a small fruit relative of the plum.
- `d8s1` Sloe gin has an alcohol content between 15 and 30 percent by volume.
- `d8s2` However, the European Union has established a minimum of 25% ABV for sloe gin to be named as such.
- `d8s3` The traditional way of making sloe gin is to soak the sloes in gin.
- `d8s4` Sugar is required to ensure the sloe juice is extracted from the fruit.

**d9：Cork Dry Gin**
- `d9s0` Cork Dry Gin is an Irish gin.
- `d9s1` First produced in Cork in the Watercourse Distillery circa 1793.
- `d9s2` Since 1975, Cork Dry Gin has been manufactured by Irish Distillers, a subsidiary of Pernod Ricard, at their Midleton Distillery.
- `d9s3` Cork Dry Gin is the largest selling gin brand in Ireland.

**d10：Springbokkie**
- `d10s0` The Springbokkie ("little Springbok" in the Afrikaans language), composed of creme de menthe ("or substitutes") and Amarula, is a cocktail shooter that is popular in South Africa.
- `d10s1` The drink derives its name from the team jersey colours (green and gold) of the South Africa national rugby union team, which is known as "The Springboks."
- `d10s2` The ratio of Amarula to creme de menthe can vary substantially between recipes.

### 由这道题生成的 SFT 样本（6 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=2 | d1, d3 | u1 ✅ yes ← d3s0; u2 —; u3 — |
| sftorder1 t=9 | d1, d3, d2, d7, d8, d4, d6, d5, d9 | u1 ✅ yes ← d3s0; u2 —; u3 — |
| sftorder1 t=10 | d1, d3, d2, d7, d8, d4, d6, d5, d9, d10 | u1 ✅ yes ← d3s0; u2 —; u3 — |
| sftorder2 t=4 | d8, d10, d2, d3 | u1 ✅ yes ← d3s0; u2 —; u3 — |
| sftorder3 t=3 | d4, d7, d3 | u1 ✅ yes ← d3s0; u2 —; u3 — |
| sftorder3 t=5 | d4, d7, d3, d6, d2 | u1 ✅ yes ← d3s0; u2 —; u3 — |

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

## 第 4 题：`2wikimultihopqa_ed17b36008b511ebbd88ac1f6bf848b6`

- 数据集 / 题型：2wikimultihopqa / bridge_comparison（unit 构造类型 bridge_comparison）
- 划分：train；特殊情况：无
- 问题：Which film whose director was born first, Desperado City or Dhanak?
- 源答案：Desperado City

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | director of film Desperado City | false | Vadim Glowna | — |
| u2 | date of birth of {u1} | false | 26 September 1941 | u1 |
| u3 | director of film Dhanak | false | Nagesh Kukunoor | — |
| u4 | date of birth of {u3} | false | 30 March 1967 | u3 |
| u5 | which of the two films has the director born first | true | Desperado City | u2, u4 |

**u1 证据**
- support 第 1 组：
  - `d9s0` (Desperado City) Desperado City is a 1981 West German drama film written and directed by Vadim Glowna.

**u2 证据**
- support 第 1 组：
  - `d8s0` (Vadim Glowna) Vadim Glowna( 26 September 1941 – 24 January 2012) was a German actor and film director.

**u3 证据**
- support 第 1 组：
  - `d7s0` (Dhanak) Dhanak is a 2015 Indian Hindi film written and directed by Nagesh Kukunoor.
- support 第 2 组：
  - `d2s9` (Nagesh Kukunoor) In 2015 he directed the road movie, "Dhanak", which won the Crystal Bear Grand Prix for Best Children's Film, and Special Mention for the Best Feature Film by The Children's Jury for Generation Kplus at the 65th Berlin International Film Festival.

**u4 证据**
- support 第 1 组：
  - `d2s0` (Nagesh Kukunoor) Nagesh Kukunoor (born 30 March 1967) is an Indian film director, producer, screenwriter and actor known for his works predominantly in Bollywood.

**u5 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Bridge comparison: director and birth date per film, then a conclusion comparing the birth dates.
- Nagesh Kukunoor sentence 9 ('In 2015 he directed the road movie, Dhanak') added as alternative support for u3; sentence 1 ('known for his works ... Dhanak') excluded.

### 全部文档（`*` = gold 引用的句子）

**d1：Henry Moore (cricketer)**
- `d1s0` Henry Walter Moore( 1849 – 20 August 1916) was an English- born first- class cricketer who spent most of his life in New Zealand.

**d2：Nagesh Kukunoor**
- *`d2s0` Nagesh Kukunoor (born 30 March 1967) is an Indian film director, producer, screenwriter and actor known for his works predominantly in Bollywood.
- `d2s1` He is known for his works in parallel cinema, such as "Hyderabad Blues" (1998), "Rockford" (1999), "Iqbal" (2005), "Dor" (2006), "Aashayein" (2010), "Lakshmi" (2014), and "Dhanak" (2016).
- `d2s2` Kukunoor has received seven International Awards, and two National Film Awards for his works.
- `d2s3` In 2003, he directed "3 Deewarein", which was showcased among the Indian panorama section, at the 2003 International Film Festival of India.
- `d2s4` The film was also premiered at the Kolkata Film Festival.
- `d2s5` After having been screened at the Indian Film Festival of Los Angeles, where it was well received, the film was screened at the Commonwealth Festival at Manchester, it was nominated as one of the top five films, at the gala presentation.
- `d2s6` Nagesh Kukunoor has also received the Filmfare Award for Best Story.
- `d2s7` In 2006, he garnered the National Film Award for Best Film on Other Social Issues, for directing "Iqbal".
- `d2s8` In 2014, he received the Mercedes Benz Audience Award, for Best Narrative at the Palm Springs International Film Festival for "Lakshmi".
- *`d2s9` In 2015 he directed the road movie, "Dhanak", which won the Crystal Bear Grand Prix for Best Children's Film, and Special Mention for the Best Feature Film by The Children's Jury for Generation Kplus at the 65th Berlin International Film Festival.
- `d2s10` The film has also garnered the Best Film Award in the main category-Children's Feature Film Competition-Cinema in Sneakers (film festival), and the Best Film Award - at the Montreal International Children's Film Festival (FIFEM).
- `d2s11` The film has garnered the National Film Award for Best Children's Film for 2016.

**d3：Ringo-en no shōjo**
- `d3s0` The art director was Tomoo Shimogawara.

**d4：Wale Adebanwi**
- `d4s0` Wale Adebanwi( born 1969) is a Nigerian- born first Black Rhodes Professor at St Antony's College, Oxford.

**d5：Deepak Sareen**
- `d5s0` Deepak Sareen is a Bollywood film director and assistant director.
- `d5s1` His first film as director was" Ranbhoomi" and last film as director was" Albela".

**d6：John McMahon (Surrey and Somerset cricketer)**
- `d6s0` John William Joseph McMahon( 28 December 1917 – 8 May 2001) was an Australian- born first- class cricketer who played for Surrey and Somerset in England from 1947 to 1957.

**d7：Dhanak**
- *`d7s0` Dhanak is a 2015 Indian Hindi film written and directed by Nagesh Kukunoor.
- `d7s1` Produced by Manish Mundra, Nagesh Kukunoor, and Elahe Hiptoola, the film features Hetal Gada and Krrish Chhabria as the two children, playing brother and sister, in the leading roles, with supporting performances from Chet Dixon, Vipin Sharma, Gulfam Khan, Vibha Chibber, Flora Saini, and Vijay Maurya.
- `d7s2` The film was released nationwide in India on 17 June 2016.
- `d7s3` The film was premiered at the 65th Berlin International Film Festival where it won the" Crystal Bear Grand Prix" for Best Children's Film, and Special Mention for the Best Feature Film by The Children's Jury for Generation Kplus.
- `d7s4` The film has also garnered the Best Film Award in the main category- Children's Feature Film Competition- Cinema in Sneakers( film festival), and the Best Film Award- at the Montreal International Children's Film Festival( FIFEM).
- `d7s5` Dhanak was also screened at the Indian Film Festival of Los Angeles, and the Toronto International Film Festival.
- `d7s6` The film has garnered Best Children's Film at the 64th National Film Awards.

**d8：Vadim Glowna**
- *`d8s0` Vadim Glowna( 26 September 1941 – 24 January 2012) was a German actor and film director.
- `d8s1` Since 1964 he appeared in more than 150 films and television shows.
- `d8s2` He directed the 1983 film" Dies rigorose Leben", which won an Honourable Mention at the 33rd Berlin International Film Festival.
- `d8s3` In 1989, he was a member of the jury at the 39th Berlin International Film Festival.
- `d8s4` Three years later, his film" Rising to the Bait" was entered into the 42nd Berlin International Film Festival.

**d9：Desperado City**
- *`d9s0` Desperado City is a 1981 West German drama film written and directed by Vadim Glowna.
- `d9s1` It won the Caméra d'Or at the 1981 Cannes Film Festival.

**d10：Hartley Lobban**
- `d10s0` Hartley W Lobban (9 May 1926 – 15 October 2004) was a Jamaican-born first-class cricketer who played 17 matches for Worcestershire in the early 1950s.

### 由这道题生成的 SFT 样本（10 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=5 | d3, d4, d6, d10, d7 | u1 —; u2 —; u3 ✅ Nagesh Kukunoor ← d7s0; u4 —; u5 — |
| sftorder1 t=6 | d3, d4, d6, d10, d7, d8 | u1 —; u2 —; u3 ✅ Nagesh Kukunoor ← d7s0; u4 —; u5 — |
| sftorder1 t=8 | d3, d4, d6, d10, d7, d8, d9, d2 | u1 ✅ Vadim Glowna ← d9s0; u2 ✅ 26 September 1941 ← d8s0; u3 ✅ Nagesh Kukunoor ← d7s0; u4 ✅ 30 March 1967 ← d2s0; u5 ✅ Desperado City ← d8s0,d2s0 |
| sftorder1 t=10 | d3, d4, d6, d10, d7, d8, d9, d2, d5, d1 | u1 ✅ Vadim Glowna ← d9s0; u2 ✅ 26 September 1941 ← d8s0; u3 ✅ Nagesh Kukunoor ← d7s0; u4 ✅ 30 March 1967 ← d2s0; u5 ✅ Desperado City ← d8s0,d2s0 |
| sftorder2 t=1 | d2 | u1 —; u2 —; u3 ✅ Nagesh Kukunoor ← d2s9; u4 ✅ 30 March 1967 ← d2s0; u5 — |
| sftorder2 t=2 | d2, d8 | u1 —; u2 —; u3 ✅ Nagesh Kukunoor ← d2s9; u4 ✅ 30 March 1967 ← d2s0; u5 — |
| sftorder2 t=3 | d2, d8, d4 | u1 —; u2 —; u3 ✅ Nagesh Kukunoor ← d2s9; u4 ✅ 30 March 1967 ← d2s0; u5 — |
| sftorder2 t=9 | d2, d8, d4, d3, d7, d10, d6, d9, d1 | u1 ✅ Vadim Glowna ← d9s0; u2 ✅ 26 September 1941 ← d8s0; u3 ✅ Nagesh Kukunoor ← d7s0; u4 ✅ 30 March 1967 ← d2s0; u5 ✅ Desperado City ← d8s0,d2s0 |
| sftorder3 t=4 | d7, d3, d5, d8 | u1 —; u2 —; u3 ✅ Nagesh Kukunoor ← d7s0; u4 —; u5 — |
| sftorder3 t=6 | d7, d3, d5, d8, d6, d9 | u1 ✅ Vadim Glowna ← d9s0; u2 ✅ 26 September 1941 ← d8s0; u3 ✅ Nagesh Kukunoor ← d7s0; u4 —; u5 — |

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

## 第 5 题：`2wikimultihopqa_485a0492085911ebbd5bac1f6bf848b6`

- 数据集 / 题型：2wikimultihopqa / comparison（unit 构造类型 comparison）
- 划分：train；特殊情况：无
- 问题：Were Glenn Walker (footballer, born 1998) and Eddie Deezen from the same country?
- 源答案：no

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | nationality of Glenn Walker (footballer, born 1998) | false | Norwegian （Norway） | — |
| u2 | nationality of Eddie Deezen | false | American （United States） | — |
| u3 | whether Glenn Walker (footballer, born 1998) and Eddie Deezen are from the same country | true | no | u1, u2 |

**u1 证据**
- support 第 1 组：
  - `d3s0` (Glenn Walker (footballer, born 1998)) Glenn Daniel Rogstad Walker( born 17 June 1998) is a Norwegian professional footballer who plays for Hødd on loan from Ranheim, as a defender.

**u2 证据**
- support 第 1 组：
  - `d4s0` (Eddie Deezen) Edward Harry Deezen( born March 6, 1957) is an American actor, voice actor and comedian best known for his bit parts as nerd characters in 1970s and 1980s films such as" GreaseGrease 2 Midnight Madness I Wanna Hold Your Hand 1941" and" War Games", as well as for larger and starring roles in a number of independent cult films, including" Surf II: The End of the Trilogy Mob BossBeverly Hills Vamp" and" Teenage Exorcist".

**u3 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Comparison (yes/no): two fact units plus a conclusion unit.
- Both biographies state the nationality explicitly. Glenn D. Walker (a US Army general) is a distractor with a similar name.

### 全部文档（`*` = gold 引用的句子）

**d1：Khalid Mohammed (footballer)**
- `d1s0` Khalid Abdi Mohammed( born 1998) is an English footballer who played for Bury as a midfielder.

**d2：Ruairidh Campbell**
- `d2s0` Ruairidh Campbell( born 1998) is a Scottish professional rugby union referee who represents the Scottish Rugby Union.

**d3：Glenn Walker (footballer, born 1998)**
- *`d3s0` Glenn Daniel Rogstad Walker( born 17 June 1998) is a Norwegian professional footballer who plays for Hødd on loan from Ranheim, as a defender.
- `d3s1` He played youth football for Stjørdals- Blink and Rosenborg.
- `d3s2` Done with his junior years, he joined the city's number two team Ranheim ahead of the 2018 season.
- `d3s3` Facing scarce first- team action, he was loaned to his childhood club Stjørdals- Blink in the summer transfer window of 2018.

**d4：Eddie Deezen**
- *`d4s0` Edward Harry Deezen( born March 6, 1957) is an American actor, voice actor and comedian best known for his bit parts as nerd characters in 1970s and 1980s films such as" GreaseGrease 2 Midnight Madness I Wanna Hold Your Hand 1941" and" War Games", as well as for larger and starring roles in a number of independent cult films, including" Surf II: The End of the Trilogy Mob BossBeverly Hills Vamp" and" Teenage Exorcist".
- `d4s1` As a voice actor, he is recognized for his distinctively high- pitched and nasal voice, which has been used for the characters of Mandark in the Cartoon Network series" Dexter's Laboratory", Snipes the Magpie in" Rock- a- Doodle", Ned in" Kim Possible", and the Know- It- All Kid in" The Polar Express".

**d5：Glenn D. Walker**
- `d5s0` Glenn D. Walker( January 21, 1916 — May 3, 2002) was a lieutenant general in the United States Army.
- `d5s1` He was notable as commander of the 4th Infantry Division, First United States Army, I Corps, and adjutant general of the Mississippi National Guard.

**d6：Stella Kunkat**
- `d6s0` Stella Kunkat( born 1998) is a German actress.

**d7：Liza Jane (singer)**
- `d7s0` Liza Jane( born 1998) is an American singer- songwriter.
- `d7s1` Her first album is titled" We can start a fire".

**d8：Breana Geering**
- `d8s0` Breana Geering( born 1998) is a goofy- footed Canadian skateboarder.

**d9：Karin Kei Nagano**
- `d9s0` Karin Kei Nagano( born 1998) is an American pianist.

**d10：Tyler French**
- `d10s0` Tyler Jay French( born 1998/1999) is an English professional footballer who plays for Bradford City, as a central defender.

### 由这道题生成的 SFT 样本（9 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=1 | d4 | u1 —; u2 ✅ American ← d4s0; u3 — |
| sftorder1 t=5 | d4, d9, d8, d1, d6 | u1 —; u2 ✅ American ← d4s0; u3 — |
| sftorder1 t=8 | d4, d9, d8, d1, d6, d10, d5, d3 | u1 ✅ Norwegian ← d3s0; u2 ✅ American ← d4s0; u3 ✅ no ← d3s0,d4s0 |
| sftorder1 t=10 | d4, d9, d8, d1, d6, d10, d5, d3, d2, d7 | u1 ✅ Norwegian ← d3s0; u2 ✅ American ← d4s0; u3 ✅ no ← d3s0,d4s0 |
| sftorder2 t=1 | d3 | u1 ✅ Norwegian ← d3s0; u2 —; u3 — |
| sftorder2 t=5 | d3, d7, d1, d10, d4 | u1 ✅ Norwegian ← d3s0; u2 ✅ American ← d4s0; u3 ✅ no ← d3s0,d4s0 |
| sftorder2 t=9 | d3, d7, d1, d10, d4, d2, d8, d5, d6 | u1 ✅ Norwegian ← d3s0; u2 ✅ American ← d4s0; u3 ✅ no ← d3s0,d4s0 |
| sftorder3 t=2 | d6, d4 | u1 —; u2 ✅ American ← d4s0; u3 — |
| sftorder3 t=7 | d6, d4, d10, d1, d2, d8, d3 | u1 ✅ Norwegian ← d3s0; u2 ✅ American ← d4s0; u3 ✅ no ← d3s0,d4s0 |

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

## 第 6 题：`2wikimultihopqa_533e994a0bdd11eba7f7acde48001122`

- 数据集 / 题型：2wikimultihopqa / compositional（unit 构造类型 bridge）
- 划分：train；特殊情况：无
- 问题：What is the date of death of the director of film Muhammad Bin Tughluq (Film)?
- 源答案：7 December 2016

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | director of film Muhammad bin Tughluq | false | Cho Ramaswamy （Cho; Srinivasa Iyer Ramaswamy） | — |
| u2 | date of death of {u1} | true | 7 December 2016 （December 7, 2016） | u1 |

**u1 证据**
- support 第 1 组：
  - `d4s0` (Muhammad bin Tughluq (film)) Muhammad bin Thughluq is a 1971 Indian Tamil-language comedy film directed and written by Cho Ramaswamy.
- support 第 2 组：
  - `d4s2` (Muhammad bin Tughluq (film)) Both the play and the film were conceptualised, written and directed by Cho who also stars as the title character.

**u2 证据**
- support 第 1 组：
  - `d5s0` (Cho Ramaswamy) Srinivasa Iyer Ramaswamy, better known as Cho Ramaswamy (5 October 1934 – 7 December 2016), was an Indian actor, comedian, character actor, editor, political satirist, playwright, dialogue writer, film director and lawyer in Tamil Nadu.

**起草备注**

- Bridge: director (optional) then date of death (necessary).
- Film sentence 0 spells the title 'Muhammad bin Thughluq'; the document title identifies the film.
- Film sentence 2 ('Both the play and the film were ... directed by Cho') added as alternative support for u1; 'Cho' is in aliases, and Cho Ramaswamy sentence 0 ('better known as Cho Ramaswamy') links the name.

### 全部文档（`*` = gold 引用的句子）

**d1：Ian Barry (director)**
- `d1s0` Ian Barry is an Australian director of film and TV.

**d2：Etan Boritzer**
- `d2s0` Etan Boritzer( born 1950) is an American writer of children ’s literature who is best known for his book" What is God?" first published in 1989.
- `d2s1` His best selling" What is?" illustrated children's book series on character education and difficult subjects for children is a popular teaching guide for parents, teachers and child- life professionals.
- `d2s2` Boritzer gained national critical acclaim after" What is God?" was published in 1989 although the book has caused controversy from religious fundamentalists for its universalist views.
- `d2s3` The other current books in the" What is?" series include
- `d2s4` What is Love?,
- `d2s5` What is Death?,
- `d2s6` What is Beautiful?,
- `d2s7` What is Funny?,
- `d2s8` What is Right?,
- `d2s9` What is Peace?,
- `d2s10` What is Money?,
- `d2s11` What is Dreaming?,
- `d2s12` What is a Friend?,
- `d2s13` What is True?,
- `d2s14` What is a Family?,
- `d2s15` What is a Feeling?"
- `d2s16` The series is now also translated into 15 languages.
- `d2s17` Boritzer was first published in 1963 at the age of 13 when he wrote an essay in his English class at Wade Junior High School in the Bronx, New York on the assassination of John F. Kennedy.
- `d2s18` His essay was included in a special anthology by New York City public school children compiled and published by the New York City Department of Education.
- `d2s19` Boritzer now lives in Venice, California and maintains his publishing office there also.
- `d2s20` He has helped numerous other authors to get published through" How to Get Your Book Published!" programs.
- `d2s21` Boritzer is also a yoga teacher who teaches regular classes locally and guest- teaches nationally.
- `d2s22` He is also recognized nationally as an erudite speaker on" The Teachings of the Buddha."

**d3：Abdul-Aziz bin Muhammad**
- `d3s0` Imam Abdul Aziz bin Muhammad bin Saud  (d. 1803) was the second ruler of the First Saudi State and son of Muhammad bin Saud.
- `d3s1` He was also the son-in-law of Muhammad bin Abdul Wahhab.
- `d3s2` He ruled from 1765 until 1803.

**d4：Muhammad bin Tughluq (film)**
- *`d4s0` Muhammad bin Thughluq is a 1971 Indian Tamil-language comedy film directed and written by Cho Ramaswamy.
- `d4s1` It is the film version of the play of the same name.
- *`d4s2` Both the play and the film were conceptualised, written and directed by Cho who also stars as the title character.
- `d4s3` The film is a satirical take on the then political and social affairs of India and is considered a fine portrayal of the political attitude existent till today.
- `d4s4` The title character's name is an allusion to the present day politics in India that can be compared with those of Tughluq's.
- `d4s5` It is believed in India that Tughluq, the sultan of Delhi in 14th century, was an unintelligent ruler especially for some of his decisions during his reign, including those of relocation of capital and experiments with coins.
- `d4s6` Thus, Cho found it to be a correct allusion to the present day political happenings.
- `d4s7` There are several dialogues in the film that mention these facts.

**d5：Cho Ramaswamy**
- *`d5s0` Srinivasa Iyer Ramaswamy, better known as Cho Ramaswamy (5 October 1934 – 7 December 2016), was an Indian actor, comedian, character actor, editor, political satirist, playwright, dialogue writer, film director and lawyer in Tamil Nadu.

**d6：Bill Smith (footballer, born 1897)**
- `d6s0` William Thomas Smith( born 9 April 1897, date of death unknown) was an English professional footballer.

**d7：Muhammad bin Jamil Zeno**
- `d7s0` Muhammad bin Jamil Zeno( 1925 – Oct 2010) was an Islamic scholar and author.
- `d7s1` His name has also been transliterated differently in the English speaking world.
- `d7s2` Whilst his publishers Dar- Us- Salam in Riyadh translate it as' Muhammad bin Jamil Zeno', it is also rendered as Muhammad Bin/ Ibn Jamal/ Jamaal/ Jameel Zeeno/ Zaino/Zayno/Zaynoo/Zeenoo/Zino/Zainu.

**d8：Thomas Scott (diver)**
- `d8s0` Thomas Scott( 1907- date of death unknown) was an English diver.

**d9：Theodred II (Bishop of Elmham)**
- `d9s0` Theodred II was a medieval Bishop of Elmham.
- `d9s1` The date of Theodred's consecration unknown, but the date of his death was sometime between 995 and 997.

**d10：Abu Bakr Ibn Sayyid al-Nās**
- `d10s0` Muhammad bin Ahmad bin Abdullah bin Muhammad bin Yahya bin Muhammad bin Muhammad bin Sayyid al- Nas al- Ya'mari, better known as Abu Bakr Ibn Sayyid al- Nās, was a Medieval Muslim theologian.
- `d10s1` He was the grandfather of Fatḥ al- Din Ibn Sayyid al- Nās, though he died before ever meeting his grandson.

### 由这道题生成的 SFT 样本（8 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=1 | d4 | u1 ✅ Cho Ramaswamy ← d4s0; u2 — |
| sftorder1 t=2 | d4, d5 | u1 ✅ Cho Ramaswamy ← d4s0; u2 ✅ 7 December 2016 ← d5s0 |
| sftorder1 t=7 | d4, d5, d3, d2, d10, d6, d1 | u1 ✅ Cho Ramaswamy ← d4s0; u2 ✅ 7 December 2016 ← d5s0 |
| sftorder1 t=10 | d4, d5, d3, d2, d10, d6, d1, d9, d7, d8 | u1 ✅ Cho Ramaswamy ← d4s0; u2 ✅ 7 December 2016 ← d5s0 |
| sftorder2 t=6 | d4, d6, d7, d2, d8, d5 | u1 ✅ Cho Ramaswamy ← d4s0; u2 ✅ 7 December 2016 ← d5s0 |
| sftorder3 t=2 | d8, d4 | u1 ✅ Cho Ramaswamy ← d4s0; u2 — |
| sftorder3 t=3 | d8, d4, d5 | u1 ✅ Cho Ramaswamy ← d4s0; u2 ✅ 7 December 2016 ← d5s0 |
| sftorder3 t=6 | d8, d4, d5, d1, d10, d7 | u1 ✅ Cho Ramaswamy ← d4s0; u2 ✅ 7 December 2016 ← d5s0 |

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

## 第 7 题：`2wikimultihopqa_b6f259dc0baf11ebab90acde48001122`

- 数据集 / 题型：2wikimultihopqa / inference（unit 构造类型 bridge）
- 划分：train；特殊情况：无
- 问题：Who is the paternal grandmother of Ptolemy Viii Physcon?
- 源答案：Arsinoe III of Egypt

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | father of Ptolemy VIII Physcon | false | Ptolemy V Epiphanes （Ptolemy V） | — |
| u2 | mother of {u1}, Ptolemy VIII Physcon's paternal grandmother | true | Arsinoe III of Egypt （Arsinoe III） | u1 |

**u1 证据**
- support 第 1 组：
  - `d5s2` (Ptolemy VIII Physcon) He was the younger son of Ptolemy V Epiphanes and Cleopatra I Syra.

**u2 证据**
- support 第 1 组：
  - `d8s0` (Ptolemy V Epiphanes) Ptolemy V Epiphanes ("Ptolemaĩos Epiphanḗs EucharistosPtolemy the Manifest, the Beneficent"; 9 October 210–September 180 BC), son of the siblings Ptolemy IV Philopator and Arsinoe III of Egypt, was the fifth ruler of the Ptolemaic dynasty from July/August 204 to September 180 BC.

**起草备注**

- Bridge (inference): father (optional) then the father's mother, i.e. the paternal grandmother (necessary).
- Ptolemy V Epiphanes sentence 0 ('son of the siblings Ptolemy IV Philopator and Arsinoe III of Egypt') names the mother explicitly.
- Conall Collamrach, Titus Manlius Torquatus and Harsiesi mention Ptolemy VIII but not his parents.

### 全部文档（`*` = gold 引用的句子）

**d1：Conall Collamrach**
- `d1s0` Conall Collamrach, son of Eterscél Temrach, son of Eochaid Ailtlethan, was, according to medieval Irish legend and historical tradition, a High King of Ireland.
- `d1s1` He succeeded to the throne on the death of his uncle Óengus Tuirmech Temrach, and ruled for five years, until he was killed by Nia Segamain.
- `d1s2` The" Lebor Gabála" synchronises his reign with that of Ptolemy VIII Physcon in Egypt( 145 – 116 BC).
- `d1s3` The chronology of Geoffrey Keating's" Foras Feasa ar Éirinn" dates his reign to 232–226 BC, that of the" Annals of the Four Masters" to 326–320 BC.

**d2：Titus Manlius Torquatus (consul 165 BC)**
- `d2s0` Titus Manlius Torquatus( born before 208 – died after 133 BC) was a politician of the Roman Republic, who became consul in 165 BC.
- `d2s1` Born into a prominent family, he sought to emulate the legendary severity of his ancestors, notably by forcing his son to commit suicide after he had been accused of corruption.
- `d2s2` Titus had a long career and was a respected jurist.
- `d2s3` He was also active in diplomatic affairs; he notably served as ambassador to Egypt in 162 BC in a mission to support the claims of Ptolemy VIII Physcon over Cyprus.

**d3：Anne Denman**
- `d3s0` Anne Denman( 1587–1661) was born in Olde Hall, Retford, Nottinghamshire.
- `d3s1` Through a fortunate second marriage with Thomas Aylesbury, she became the grandmother of Lady Anne Hyde, Duchess of York and great- grandmother of Queen Mary II and Queen Anne.

**d4：Harsiesi**
- `d4s0` Harsiesi(? – 130 BC) was an ancient Egyptian rebel against the rule of Ptolemy VIII Physcon of the Ptolemaic Dynasty.

**d5：Ptolemy VIII Physcon**
- `d5s0` Ptolemy VIII Euergetes II Tryphon ("Ptolemaĩos Euergétēs TryphonPtolemy the Benefactor, the luxurious"; c. 184 BC – 28 June 116 BC),
- `d5s1` nicknamed Physcon ("Fatty"), was a king of the Ptolemaic dynasty in Egypt.
- *`d5s2` He was the younger son of Ptolemy V Epiphanes and Cleopatra I Syra.
- `d5s3` His reign was characterised by fierce political and military conflict with his older brother Ptolemy VI Philometor and his sister Cleopatra II.
- `d5s4` Ptolemy VIII was originally made co-ruler with his older siblings in the run-up to the Sixth Syrian War.
- `d5s5` In the course of that war, Ptolemy VI was captured and Ptolemy VIII became sole king of Egypt.
- `d5s6` When the war ended and Ptolemy VI was restored to the throne in 168 BC, the two brothers continued to quarrel.
- `d5s7` In 164 BC Ptolemy VIII drove out his brother and became sole king of the Ptolemaic empire, but he was expelled in turn in 163 BC.
- `d5s8` As a result of Roman intervention, Ptolemy VIII was awarded control of Cyrenaica.
- `d5s9` From there he repeatedly tried to capture Cyprus, which had also been promised to him by the Romans, from his brother.
- `d5s10` After Ptolemy VI's death in 145 BC, Ptolemy VIII returned to Egypt as co-ruler with his sister.
- `d5s11` His cruel treatment of opposition and his decision to marry his niece Cleopatra III and promote her to the status of co-regent led to a civil war from 132 to 126 BC, in which Cleopatra II controlled Alexandria and enjoyed the support of the Greek population of the country, while Ptolemy VIII and Cleopatra III controlled most of the rest of Egypt and were supported by the native Egyptians.
- `d5s12` During this war, native Egyptians were promoted to the highest echelons of the Ptolemaic government for the first time.
- `d5s13` Ptolemy was victorious and ruled alongside Cleopatra II and Cleopatra III until his death in 116 BC.
- `d5s14` The ancient Greek sources on Ptolemy VIII are extremely hostile, characterising him as cruel and mocking him as fat and degenerate, as part of a contrast with Ptolemy VI, whom they present extremely positively.
- `d5s15` The historian Günther Höbl calls him "one of the most brutal and at the same time one of the shrewdest politicians of the Hellenistic Age."

**d6：Kaoru Hatoyama**
- `d6s0` After the elections of 2009, she became more widely known as the grandmother of Prime Minister Yukio Hatoyama and his politician brother Kunio Hatoyama.

**d7：Hannah Arnold**
- `d7s0` Hannah Arnold, also known as Hannah Waterman King, was the grandmother of Benedict Arnolds children.

**d8：Ptolemy V Epiphanes**
- *`d8s0` Ptolemy V Epiphanes ("Ptolemaĩos Epiphanḗs EucharistosPtolemy the Manifest, the Beneficent"; 9 October 210–September 180 BC), son of the siblings Ptolemy IV Philopator and Arsinoe III of Egypt, was the fifth ruler of the Ptolemaic dynasty from July/August 204 to September 180 BC.
- `d8s1` Ptolemy inherited the throne at the age of five, when his parents died in suspicious circumstances.
- `d8s2` The new regent, Agathocles was widely reviled and was toppled by a revolution in 202 BC, but the series of regents who followed proved incompetent and the kingdom was paralysed.
- `d8s3` The Seleucid king Antiochus III and the Antigonid king Philip V took advantage of the kingdom's weakness to begin the Fifth Syrian War (202-196 BC), in which the Ptolemies lost all their territories in Asia Minor and the Levant, as well as most of their influence in the Aegean Sea.
- `d8s4` Simultaneously, Ptolemy V faced a widespread Egyptian revolt (206-185 BC) led by self-proclaimed Pharaohs, which resulted in the loss of most of Upper Egypt and parts of Lower Egypt as well.
- `d8s5` Ptolemy V came of age in 196 BC and was crowned as Pharaoh in Memphis, an occasion commemorated by the creation of the Rosetta Stone.
- `d8s6` After this, he made peace with Antiochus III and married his daughter Cleopatra I in 194/3 BC.
- `d8s7` This disgusted the Romans who had entered into hostilities with Antiochus partially on Ptolemy's behalf - after their victory, they distributed the old Ptolemaic territories in Asia Minor to Pergamum and Rhodes rather than returning them to Egypt.
- `d8s8` However, Ptolemaic forces steadily reconquered the south of the country, bringing all of Upper Egypt back under Ptolemaic control in 186 BC.
- `d8s9` In his last years, Ptolemy began manoeuvring for renewed warfare with the Seleucid empire, but these plans were cut short by his sudden death in September 180 BC, allegedly poisoned by courtiers worried about the cost of the war.
- `d8s10` Ptolemy's reign saw greatly increased prominence of courtiers and the Egyptian priestly elite in Ptolemaic political life - a pattern that would continue for most of the rest of the kingdom's existence.
- `d8s11` It also marked the collapse of Ptolemaic power in the wider Mediterranean region.
- `d8s12` Arthur Eckstein has argued that this collapse sparked the 'power transition crisis' which led to the Roman conquest of the eastern Mediterranean.

**d9：Hubba bint Hulail**
- `d9s0` Hubba bint Hulail was the grandmother of Hashim ibn' Abd Manaf, thus the great- great- great- grandmother of the Islamic" Nabī"( Prophet) Muhammad ibn Abdullah.

**d10：Tjuyu**
- `d10s0` Tjuyu( sometimes transliterated as Thuya or Thuyu) was an Egyptian noblewoman and the mother of queen Tiye, and the wife of Yuya.
- `d10s1` She is the grandmother of Akhenaten, and great grandmother of Tutankhamun.

### 由这道题生成的 SFT 样本（8 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=2 | d4, d5 | u1 ✅ Ptolemy V Epiphanes ← d5s2; u2 — |
| sftorder1 t=9 | d4, d5, d1, d7, d3, d6, d10, d9, d8 | u1 ✅ Ptolemy V Epiphanes ← d5s2; u2 ✅ Arsinoe III of Egypt ← d8s0 |
| sftorder1 t=10 | d4, d5, d1, d7, d3, d6, d10, d9, d8, d2 | u1 ✅ Ptolemy V Epiphanes ← d5s2; u2 ✅ Arsinoe III of Egypt ← d8s0 |
| sftorder2 t=1 | d6 | u1 —; u2 — |
| sftorder2 t=3 | d6, d1, d5 | u1 ✅ Ptolemy V Epiphanes ← d5s2; u2 — |
| sftorder2 t=7 | d6, d1, d5, d2, d4, d3, d8 | u1 ✅ Ptolemy V Epiphanes ← d5s2; u2 ✅ Arsinoe III of Egypt ← d8s0 |
| sftorder3 t=2 | d7, d8 | u1 —; u2 — |
| sftorder3 t=5 | d7, d8, d6, d4, d9 | u1 —; u2 — |

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

## 第 8 题：`hotpotqa_5adfdcf5554299025d62a367`

- 数据集 / 题型：hotpotqa / bridge（unit 构造类型 bridge）
- 划分：train；特殊情况：无
- 问题： Royal Air Force Valley provides fast-jet training using an advanced trainer aircraft first flown in what year?
- 源答案：1974

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | advanced trainer aircraft used by Royal Air Force Valley for fast-jet training | false | BAE Systems Hawk （Hawk; Hawker Siddeley Hawk） | — |
| u2 | year {u1} was first flown | true | 1974 | u1 |

**u1 证据**
- support 第 1 组：
  - `d1s1` (RAF Valley) It provides fast-jet training using the BAE Systems Hawk and provides training for aircrew working with search and rescue.

**u2 证据**
- support 第 1 组：
  - `d3s1` (BAE Systems Hawk) It was first flown at Dunsfold, Surrey, in 1974 as the Hawker Siddeley Hawk, and subsequently produced by its successor companies, British Aerospace and BAE Systems, respectively.

**起草备注**

- Bridge: u1 identifies the trainer aircraft, u2 its first-flight year.
- RAF Valley sentence 0 and BAE Systems Hawk sentence 0 removed from support: they do not state the aircraft or the year (sentence 0 of the Hawk only confirms 'advanced trainer').

### 全部文档（`*` = gold 引用的句子）

**d1：RAF Valley**
- `d1s0` Royal Air Force Valley or more simply RAF Valley (Welsh: "RAF y Fali" ) (IATA: VLY, ICAO: EGOV) is a Royal Air Force station on the island of Anglesey, Wales, and which is also used as Anglesey Airport.
- *`d1s1` It provides fast-jet training using the BAE Systems Hawk and provides training for aircrew working with search and rescue.

**d2：Muniz M-9**
- `d2s0` The Muniz M-9 was a two-seat training biplane with tandem open cockpit and powered by a 200 hp (149 kW) 130 hp (197 kW) de Havilland Gipsy Six engine.
- `d2s1` Designed by Lieutenant-Colonel Antonio Muniz, a serving officer in the Brazilian Air Force, as an advanced trainer and was very similar to his earlier M-7 primary trainer.
- `d2s2` It was first flown in 1937 and a small production run was built for the air force by Cia Nacional de Navegacao Costiera.

**d3：BAE Systems Hawk**
- `d3s0` The BAE Systems Hawk is a British single-engine, jet-powered advanced trainer aircraft.
- *`d3s1` It was first flown at Dunsfold, Surrey, in 1974 as the Hawker Siddeley Hawk, and subsequently produced by its successor companies, British Aerospace and BAE Systems, respectively.
- `d3s2` It has been used in a training capacity and as a low-cost combat aircraft.

**d4：Royal Air Force Music Services**
- `d4s0` Royal Air Force Music Services is the organization which provides military musical support to the Royal Air Force.
- `d4s1` Based at RAF Northolt (previously at RAF Uxbridge) and RAF Cranwell, it forms the central administration of one hundred and seventy musicians divided between the Central Band of the Royal Air Force, The Band of the Royal Air Force College, The Band of the Royal Air Force Regiment and Headquarters Music Services.
- `d4s2` These main military bands contain within their ranks the Royal Air Force Squadronnaires, Royal Air Force Swing Wing, Royal Air Force Shades of Blue, and The Salon Orchestra of the Central Band of the Royal Air Force.

**d5：Beechcraft T-6 Texan II**
- `d5s0` The Beechcraft T-6 Texan II is a single-engine turboprop aircraft built by the Raytheon Aircraft Company (which became Hawker Beechcraft and later Beechcraft Defense Company, and was bought by Textron Aviation in 2014).
- `d5s1` A trainer aircraft based on the Pilatus PC-9, the T-6 has replaced the Air Force's Cessna T-37B Tweet and the Navy's T-34C Turbo Mentor.
- `d5s2` The T-6A is used by the United States Air Force for basic pilot training and Combat Systems Officer (CSO) training and by the United States Navy and United States Marine Corps for primary Naval Aviator training as well as primary and intermediate Naval Flight Officer (NFO) training.
- `d5s3` The T-6A is also used as a basic trainer by the Royal Canadian Air Force (CT-156 Harvard II), the Greek Air Force, the Israeli Air Force ("Efroni"), and the Iraqi Air Force.
- `d5s4` The T-6B is the primary trainer for U.S. student naval aviators.
- `d5s5` The T-6C is used for training by the Mexican Air Force, Royal Air Force, Royal Moroccan Air Force, and the Royal New Zealand Air Force.

**d6：Yakovlev Yak-130**
- `d6s0` The Yakovlev Yak-130 (NATO reporting name: Mitten) is a subsonic two-seat advanced trainer aircraft originally developed by Yakovlev and Aermacchi.
- `d6s1` It has also been marketed as a potential light attack aircraft.
- `d6s2` Development of the plane began in 1991 and the maiden flight was conducted on 25 April 1996.
- `d6s3` In 2002, it won a Russian government tender for training aircraft and in 2009 the aircraft entered service with the Russian Air Force.
- `d6s4` As an advanced training aircraft, the Yak-130 is able to replicate the characteristics of several 4+ generation fighters as well as the fifth-generation Sukhoi Su-57.
- `d6s5` It can also perform light-attack and reconnaissance duties, carrying a combat load of 3,000 kg.

**d7：Boulton Paul Balliol**
- `d7s0` The Boulton Paul Balliol and Sea Balliol were monoplane military advanced trainer aircraft built for the Royal Air Force (RAF) and the Royal Navy Fleet Air Arm (FAA) by Boulton Paul Aircraft.
- `d7s1` Developed in the late 1940s the Balliol was designed to replace the North American Harvard trainer and used the Rolls-Royce Merlin engine, with the Sea Balliol a naval version for deck landing training.

**d8：Partenavia Mosquito**
- `d8s0` The Partenavia P.86 Mosquito was a two-seat civil trainer aircraft first flown in Italy on 27 April 1986.
- `d8s1` It was a high-wing monoplane of pod-and-boom construction with tricycle undercarriage and a twin tail, that accommodated the student and instructor side-by-side.

**d9：Miles Magister**
- `d9s0` The Miles M.14 Magister is a British two-seat monoplane basic trainer aircraft built by the Miles Aircraft for the Royal Air Force and Fleet Air Arm.
- `d9s1` Affectionately known as the Maggie, the Magister was based on Miles' civilian Hawk Major and Hawk Trainer and was the first monoplane designed specifically as a trainer for the RAF.
- `d9s2` As a low-wing monoplane, it was an ideal introduction to the Spitfire and Hurricane for new pilots.
- `d9s3` Its sister design, the Miles Master was an advanced trainer also built by Phillips & Powis at Woodley.

**d10：North American T-6 Texan**
- `d10s0` The North American Aviation T-6 Texan is an American single-engined advanced trainer aircraft used to train pilots of the United States Army Air Forces (USAAF), United States Navy, Royal Air Force, and other air forces of the British Commonwealth during World War II and into the 1970s.
- `d10s1` Designed by North American Aviation, the T-6 is known by a variety of designations depending on the model and operating air force.
- `d10s2` The United States Army Air Corps (USAAC) and USAAF designated it as the AT-6, the United States Navy the SNJ, and British Commonwealth air forces the Harvard, the name by which it is best known outside of the US.
- `d10s3` Starting in 1948, the new United States Air Force (USAF) designated it the T-6, with the USN following in 1962.
- `d10s4` It remains a popular warbird aircraft used for airshow demonstrations and static displays.
- `d10s5` It has also been used many times to simulate various Japanese aircraft, including the Mitsubishi A6M Zero in movies depicting World War II in the Pacific.

### 由这道题生成的 SFT 样本（7 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=3 | d8, d6, d1 | u1 ✅ BAE Systems Hawk ← d1s1; u2 — |
| sftorder1 t=9 | d8, d6, d1, d4, d7, d10, d5, d2, d3 | u1 ✅ BAE Systems Hawk ← d1s1; u2 ✅ 1974 ← d3s1 |
| sftorder1 t=10 | d8, d6, d1, d4, d7, d10, d5, d2, d3, d9 | u1 ✅ BAE Systems Hawk ← d1s1; u2 ✅ 1974 ← d3s1 |
| sftorder2 t=1 | d1 | u1 ✅ BAE Systems Hawk ← d1s1; u2 — |
| sftorder2 t=6 | d1, d6, d9, d2, d10, d4 | u1 ✅ BAE Systems Hawk ← d1s1; u2 — |
| sftorder3 t=2 | d1, d3 | u1 ✅ BAE Systems Hawk ← d1s1; u2 ✅ 1974 ← d3s1 |
| sftorder3 t=7 | d1, d3, d2, d5, d8, d9, d10 | u1 ✅ BAE Systems Hawk ← d1s1; u2 ✅ 1974 ← d3s1 |

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

## 第 9 题：`hotpotqa_5a7565475542992d0ec05f84`

- 数据集 / 题型：hotpotqa / comparison（unit 构造类型 comparison）
- 划分：train；特殊情况：presupposition
- 问题：Which park, Picos de Europa National Park or Caldera de Taburiente National Park is on an island?
- 源答案：Caldera de Taburiente National Park

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | whether Picos de Europa National Park is on an island | false | no | — |
| u2 | whether Caldera de Taburiente National Park is on an island | false | yes | — |
| u3 | which of Picos de Europa National Park and Caldera de Taburiente National Park is on an island | true | Caldera de Taburiente National Park （Caldera de Taburiente; Parque Nacional de la Caldera de Taburiente） | u1, u2 |

**u1 证据**
- `[]`：原文没有明确陈述

**u2 证据**
- support 第 1 组：
  - `d4s0` (Caldera de Taburiente National Park) Caldera de Taburiente National Park (Spanish: "Parque Nacional de la Caldera de Taburiente" ) is large geological feature on the island of La Palma, Canary Islands, Spain.
- support 第 2 组：
  - `d6s0` (Idafe Rock) Idafe Rock is a natural stone pillar located in Caldera de Taburiente National Park on the island of La Palma in the Canary Islands.

**u3 证据**
- `[[]]`：结论由依赖 unit 推出
- presupposition 第 1 组：
  - `d4s0` (Caldera de Taburiente National Park) Caldera de Taburiente National Park (Spanish: "Parque Nacional de la Caldera de Taburiente" ) is large geological feature on the island of La Palma, Canary Islands, Spain.
- presupposition 第 2 组：
  - `d6s0` (Idafe Rock) Idafe Rock is a natural stone pillar located in Caldera de Taburiente National Park on the island of La Palma in the Canary Islands.

**起草备注**

- Comparison (selection between named candidates): two fact units plus a conclusion unit.
- No explicit support for u1: Picos de Europa sentences place it in a mountain range in northern Spain and in three autonomous communities; 'not on an island' needs world knowledge.
- Presupposition (unit_schema 5.6): conclusion gets presupposition_sets = u2's support sets.
- Idafe Rock sentence 0 ('Caldera de Taburiente National Park on the island of La Palma') is alternative support for u2.
- Picos de Europa National Park sentence 1 and Caldera de Taburiente sentence 1 removed from support (sentence 1 needs sentence 0 for the island, and sentence 0 alone suffices).

### 全部文档（`*` = gold 引用的句子）

**d1：Tobes**
- `d1s0` Tobes is one of eight parishes (administrative divisions) in Peñamellera Baja, a municipality within the province and autonomous community of Asturias, in northern Spain.
- `d1s1` It is located in the Picos de Europa National Park.

**d2：Oceño**
- `d2s0` Oceño is one of eight parishes (administrative divisions) in Peñamellera Alta, a municipality within the province and autonomous community of Asturias, in northern Spain.
- `d2s1` It is located in the Picos de Europa National Park.

**d3：Lake Ercina**
- `d3s0` Lake Ercina is a small highland lake in Asturias, Spain.
- `d3s1` It is located in the Picos de Europa, in the Cantabrian Mountains.
- `d3s2` Situated next to Lake Enol, together, they forms the group known as Lakes of Covadonga within the Picos de Europa National Park.
- `d3s3` Lake Ercina is smaller than Lake Enol.
- `d3s4` It is situated at an altitude of 1108 m and its maximum depth is just over 2 m .
- `d3s5` The eutrophic lake, covers approximately eight hectares.
- `d3s6` Its characteristics are tied to its glacier origin and geographic location.

**d4：Caldera de Taburiente National Park**
- *`d4s0` Caldera de Taburiente National Park (Spanish: "Parque Nacional de la Caldera de Taburiente" ) is large geological feature on the island of La Palma, Canary Islands, Spain.
- `d4s1` It contains the enormous expanse of the Caldera de Taburiente which dominates the northern part of the island, and was designated as a national park in 1954.
- `d4s2` The telescopes of the Roque de los Muchachos Observatory are situated very close to the summit.

**d5：Picos de Europa National Park**
- `d5s0` The Picos de Europa National Park (Spanish: "Parque Nacional de Picos de Europa" ) is a National Park in the Picos de Europa mountain range, in northern Spain.
- `d5s1` It is within the boundaries of three autonomous communities, Asturias, Cantabria and Castile and León, which are represented on the body which runs the park.

**d6：Idafe Rock**
- *`d6s0` Idafe Rock is a natural stone pillar located in Caldera de Taburiente National Park on the island of La Palma in the Canary Islands.

**d7：Lake Enol**
- `d7s0` Lake Enol is a small highland lake in the Principality of Asturias, Spain.
- `d7s1` It is located in the Picos de Europa Western Massif, Cantabrian Mountains.
- `d7s2` It is next to Lake Ercina and together, they form the group known as Lakes of Covadonga, inside the Picos de Europa National Park.
- `d7s3` Lake Enol is the larger of the two.
- `d7s4` It is situated approximately 10 km from Covadonga and 25 km from Cangas de Onís.
- `d7s5` A curving road is available from Arriondas to the lake.
- `d7s6` Measuring 0.1 km2 , it is one of the biggest lakes in the area.
- `d7s7` Lake Enol is situated 1070 m above sea level, in the Picos de Europa).
- `d7s8` It was formed by the withdrawal of a front glacier.

**d8：Naranjo de Bulnes**
- `d8s0` The Naranjo de Bulnes (known as Picu Urriellu in Asturian) is a limestone peak dating from the paleozoic era, located in the Macizo Central region of the Picos de Europa, Asturias (Spain).
- `d8s1` Its name "Picu Urriellu" is believed to be derived from the term "Los Urrieles" which is used to describe the Macizo Central.
- `d8s2` Naranjo de Bulnes is part of the Cabrales region of Asturias, and lies within the Picos de Europa National Park.

**d9：Trescares**
- `d9s0` Trescares is one of eight parishes (administrative divisions) in Peñamellera Alta, a municipality within the province and autonomous community of Asturias, in northern Spain.
- `d9s1` It is located in the Picos de Europa National Park.

**d10：Lakes of Covadonga**
- `d10s0` The Lakes of Covadonga (el.
- `d10s1` 1134 m.) are composed of two glacial lakes located on the region of Asturias, Spain.
- `d10s2` These lakes, often also called Lakes of Enol or simply Los Lagos, are Lake Enol and Lake Ercina located in the Picos de Europa range and they are the original center of the Picos de Europa National Park, created in 1918.

### 由这道题生成的 SFT 样本（6 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=7 | d10, d7, d1, d5, d2, d9, d4 | u1 —; u2 ✅ yes ← d4s0; u3 ✅ Caldera de Taburiente National Park ← d4s0 [presup] |
| sftorder1 t=8 | d10, d7, d1, d5, d2, d9, d4, d3 | u1 —; u2 ✅ yes ← d4s0; u3 ✅ Caldera de Taburiente National Park ← d4s0 [presup] |
| sftorder1 t=9 | d10, d7, d1, d5, d2, d9, d4, d3, d8 | u1 —; u2 ✅ yes ← d4s0; u3 ✅ Caldera de Taburiente National Park ← d4s0 [presup] |
| sftorder1 t=10 | d10, d7, d1, d5, d2, d9, d4, d3, d8, d6 | u1 —; u2 ✅ yes ← d4s0; u3 ✅ Caldera de Taburiente National Park ← d4s0 [presup] |
| sftorder2 t=7 | d2, d1, d9, d3, d7, d8, d6 | u1 —; u2 ✅ yes ← d6s0; u3 ✅ Caldera de Taburiente National Park ← d6s0 [presup] |
| sftorder3 t=3 | d5, d3, d4 | u1 —; u2 ✅ yes ← d4s0; u3 ✅ Caldera de Taburiente National Park ← d4s0 [presup] |

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

## 第 10 题：`2wikimultihopqa_015ccd41087711ebbd67ac1f6bf848b6`

- 数据集 / 题型：2wikimultihopqa / bridge_comparison（unit 构造类型 bridge_comparison）
- 划分：train；特殊情况：无
- 问题：Are director of film The Enigma Of The Folies-Bergere and director of film Deep Soul (Film) from the same country?
- 源答案：no

### Gold units

| unit | 描述 | necessary | 答案（别名） | 依赖 |
|---|---|---|---|---|
| u1 | director of The Enigma of the Folies-Bergere | false | Jean Mitry | — |
| u2 | nationality of {u1} | false | French （France） | u1 |
| u3 | director of Deep Soul (film) | false | Pantelis Voulgaris | — |
| u4 | nationality of {u3} | false | Greek （Greece） | u3 |
| u5 | whether the directors of The Enigma of the Folies-Bergere and Deep Soul (film) are from the same country | true | no | u2, u4 |

**u1 证据**
- support 第 1 组：
  - `d3s0` (The Enigma of the Folies-Bergere) The Enigma of the Folies-Bergere (French:
  - `d3s1` (The Enigma of the Folies-Bergere) Enigme aux Folies-Bergère) is a 1959 French crime film directed by Jean Mitry and starring Bella Darvi, Frank Villard and Dora Doll.

**u2 证据**
- support 第 1 组：
  - `d6s0` (Jean Mitry) Jean Mitry (7 November 1904, Soissons, Aisne – 18 January 1988, La Garenne-Colombes) was a French film theorist, critic and filmmaker, a co-founder of France's first film society, and, in 1938, of the Cinémathèque Française.

**u3 证据**
- support 第 1 组：
  - `d4s0` (Deep Soul (film)) Deep Soul is a 2009 Greek drama film directed by Pantelis Voulgaris, on the 1946– 49 Greek Civil War.

**u4 证据**
- support 第 1 组：
  - `d1s0` (Pantelis Voulgaris) Pantelis Voulgaris( born 23 October 1940) is a Greek film director and screenwriter.

**u5 证据**
- `[[]]`：结论由依赖 unit 推出

**起草备注**

- Bridge comparison: director and nationality chain per film, then a same-country conclusion.
- The Enigma of the Folies-Bergere sentence 0 is a fragment ('(French:'); the director is in sentence 1, so u1 cites sentences 0 and 1 together. The source supporting fact lists only sentence 0.
- u2 uses 'a French film theorist, critic and filmmaker' (Jean Mitry 0); the Soissons birthplace is not used. The film's 'French' and 'Greek' descriptors are not used for the directors.

### 全部文档（`*` = gold 引用的句子）

**d1：Pantelis Voulgaris**
- *`d1s0` Pantelis Voulgaris( born 23 October 1940) is a Greek film director and screenwriter.
- `d1s1` His first feature film" To proxenio tis Annas" in 1972 won the first prize in Thessaloniki International Film Festival.
- `d1s2` His 1989 film" The Striker with Number 9" was entered into the 39th Berlin International Film Festival.
- `d1s3` Two years later, his film" Quiet Days in August" was entered into the 41st Berlin International Film Festival.
- `d1s4` In 2005 his film" Brides" was entered into the 27th Moscow International Film Festival.

**d2：Jason Moore (director)**
- `d2s0` Jason Moore( born October 22, 1970) is an American director of film, theatre and television.

**d3：The Enigma of the Folies-Bergere**
- *`d3s0` The Enigma of the Folies-Bergere (French:
- *`d3s1` Enigme aux Folies-Bergère) is a 1959 French crime film directed by Jean Mitry and starring Bella Darvi, Frank Villard and Dora Doll.
- `d3s2` The police investigate a series of murders at the Folies-Bergère.

**d4：Deep Soul (film)**
- *`d4s0` Deep Soul is a 2009 Greek drama film directed by Pantelis Voulgaris, on the 1946– 49 Greek Civil War.

**d5：Brian Johnson (special effects artist)**
- `d5s0` Brian Johnson( born 1939 or 1940) is a British designer and director of film and television special effects.

**d6：Jean Mitry**
- *`d6s0` Jean Mitry (7 November 1904, Soissons, Aisne – 18 January 1988, La Garenne-Colombes) was a French film theorist, critic and filmmaker, a co-founder of France's first film society, and, in 1938, of the Cinémathèque Française.

**d7：Peter Levin**
- `d7s0` Peter Levin is an American director of film, television and theatre.

**d8：Ian Barry (director)**
- `d8s0` Ian Barry is an Australian director of film and TV.

**d9：Hanro Smitsman**
- `d9s0` Hanro Smitsman, born in 1967 in Breda( Netherlands), is a writer and director of film and television.

**d10：Ben Cura**
- `d10s0` Ben Cura( born 30 September 1988) is a British- Argentine actor and director of film, television and theatre.

### 由这道题生成的 SFT 样本（10 条）

| 时刻 | 已到达的文档（按顺序） | 各 unit 标签（取值 / 引用） |
|---|---|---|
| sftorder1 t=1 | d3 | u1 ✅ Jean Mitry ← d3s0,d3s1; u2 —; u3 —; u4 —; u5 — |
| sftorder1 t=3 | d3, d7, d4 | u1 ✅ Jean Mitry ← d3s0,d3s1; u2 —; u3 ✅ Pantelis Voulgaris ← d4s0; u4 —; u5 — |
| sftorder1 t=5 | d3, d7, d4, d2, d6 | u1 ✅ Jean Mitry ← d3s0,d3s1; u2 ✅ French ← d6s0; u3 ✅ Pantelis Voulgaris ← d4s0; u4 —; u5 — |
| sftorder1 t=10 | d3, d7, d4, d2, d6, d9, d8, d10, d5, d1 | u1 ✅ Jean Mitry ← d3s0,d3s1; u2 ✅ French ← d6s0; u3 ✅ Pantelis Voulgaris ← d4s0; u4 ✅ Greek ← d1s0; u5 ✅ no ← d6s0,d1s0 |
| sftorder2 t=2 | d2, d3 | u1 ✅ Jean Mitry ← d3s0,d3s1; u2 —; u3 —; u4 —; u5 — |
| sftorder2 t=3 | d2, d3, d7 | u1 ✅ Jean Mitry ← d3s0,d3s1; u2 —; u3 —; u4 —; u5 — |
| sftorder2 t=6 | d2, d3, d7, d10, d1, d6 | u1 ✅ Jean Mitry ← d3s0,d3s1; u2 ✅ French ← d6s0; u3 —; u4 —; u5 — |
| sftorder2 t=7 | d2, d3, d7, d10, d1, d6, d8 | u1 ✅ Jean Mitry ← d3s0,d3s1; u2 ✅ French ← d6s0; u3 —; u4 —; u5 — |
| sftorder3 t=6 | d10, d5, d9, d3, d7, d4 | u1 ✅ Jean Mitry ← d3s0,d3s1; u2 —; u3 ✅ Pantelis Voulgaris ← d4s0; u4 —; u5 — |
| sftorder3 t=8 | d10, d5, d9, d3, d7, d4, d2, d6 | u1 ✅ Jean Mitry ← d3s0,d3s1; u2 ✅ French ← d6s0; u3 ✅ Pantelis Voulgaris ← d4s0; u4 —; u5 — |

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
