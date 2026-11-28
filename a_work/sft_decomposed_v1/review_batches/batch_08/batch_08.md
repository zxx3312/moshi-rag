# batch_08：人工审查（30 题）

全局题号 211–240；train 30 题 / dev 0 题。原训练/验证归属保持不变。

[返回分配索引](../README.md) · [完整对比报告](../../comparison_human.md)

**原则：新旧单元都合理时保留拆题器拆法，人工监督向新单元对齐。** 本批已由用户审核，按最新 Note 完成调整。

审查人：________　完成日期：________

本批已依据人工 Note 调整；原始拆题保存在 JSON 的 `raw_decomposition`。下方 Adjusted units 为当前标注，旧 gold 仅供参照。标注已更新；逐时刻 SFT 快照尚未重建。

## 1. hotpotqa_5addad5c5542995b365fab5c

原位置：`train` 第 211 题 · 全局第 211 题 · `sample_id: hotpotqa_5addad5c5542995b365fab5c`

Question: In what year did the state-owned competitor of Air 26 gain flag carrier staus?

Note: 用户确认：d2s2 与 d4s0 联合作为 u1 的 support。

Type: bridge · fallback: False · SFT snapshots: 4

### Adjusted units and annotation

**执行结果：** 按用户确认，将 d2s2 与 d4s0 的联合推断作为 u1 的 context 支持；两条证据必须同时到达。移除 by_presupposition 和 presupposition_sets，答案仍为 TAAG Angola Airlines。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | state-owned competitor of Air 26 | False | [] | TAAG Angola Airlines | [["d2s2", "d4s0"]] | context |
| u2 | year {u1} gained flag carrier status | True | ["u1"] | 1975 | [["d4s2"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | state-owned competitor of Air 26 | False | [] | TAAG Angola Airlines | [] |
| u2 | year in which {u1} gained flag carrier status | True | ['u1'] | 1975 | [['d4s2']] |

### Source documents (reference only)

**d1: Air Nicaragua**

- [d1s0] Nicaragua Airways is the potential future national flag carrier of Nicaragua.
- [d1s1]  Its main base is Augusto C. Sandino International Airport, Managua.
- [d1s2]  It is the first time in 20 years that Nicaragua will have a national flag carrier, after Aeronica ceased operations in 1991.
- [d1s3]  Since then, the flag carrier status was awarded to Nicaragüense de Aviación also known as NICA Airlines.
- [d1s4]  Several airlines had tried to become the Nicaraguan flag carrier like CAAL (Central American Airlines), SANSA (Servicios Aereos Nicaraguenses S.A.) but none of these survived a year.
- [d1s5]  Today even NICA Airlines (6Y) is registered as the national airline of Nicaragua, the only international flight it operated once (Managua to Miami) and is done under the TACA code (TA) as a full TACA Airlines flight.

**d2: Air 26**

- [d2s0] Air26 - Linhas Aéreas, S.A. is an airline based in Luanda, Angola.
- [d2s1]  Founded in 2006, it operates domestic passenger and cargo flights out of the city's Quatro de Fevereiro Airport.
- [d2s2]  Along with all other Angolan airlines except for TAAG, Air 26 is banned from operating within the European Union.
- [d2s3]  In 2010, the company had its licence revoked, but it was re-issued on 31 January 2011.

**d3: Air Botswana**

- [d3s0] Air Botswana Corporation is Botswana's state-owned national flag carrier, with its headquarters located in Gaborone.
- [d3s1]  It operates scheduled domestic and regional flights from its main base at Sir Seretse Khama International Airport.
- [d3s2]  Air Botswana has been loss-making for several years, and there have been various attempts to privatise the company, and frequent changes to the corporation's management and board, so far without reducing the losses.

**d4: TAAG Angola Airlines**

- [d4s0] TAAG Angola Airlines E.P. (Portuguese: "TAAG Linhas Aéreas de Angola E.P." ) is the state-owned national airline of Angola.
- [d4s1]  Based in Luanda, the airline operates an all-Boeing fleet on domestic services within Angola, medium-haul services in Africa and long-haul services to Brazil, Cuba, China and Portugal.
- [d4s2]  The airline was originally set up by the government as "DTADivisão dos Transportes Aéreos" in 1938, rechristened "TAAG Angola Airlines" in 1973, and gained flag carrier status in 1975.
- [d4s3]  It is now a member of both the International Air Transport Association and the African Airlines Association.

**d5: Nordica (airline)**

- [d5s0] Nordica is the state-owned Estonian flag carrier headquartered in Tallinn and based at Lennart Meri Tallinn Airport.
- [d5s1]  It is the largest air carrier at Lennart Meri Tallinn Airport.
- [d5s2]  The airline was formed after the 2015 bankruptcy of the previous flag carrier Estonian Air.
- [d5s3]  Since most of the flights are marketed by LOT Polish Airlines, which owns 49% of the shares and a member of the Star Alliance, Nordica also carries LOT's flight codes and callsign on most of its flights.
- [d5s4]  Through its subsidiary Regional Jet in a partnership with Scandinavian Airlines, Regional Jet operates four ATR72-600s between Copenhagen, Aarhus, Aalborg, Billund, Goteborg, Hanover and other SK destinations.

**d6: Air Côte d'Ivoire**

- [d6s0] Air Côte d'Ivoire is the flag carrier of Ivory Coast, based in Abidjan.
- [d6s1]  The company succeeded the country's former flag carrier Air Ivoire, which went bankrupt in 2011.
- [d6s2]  It started operations on 12   2012 (2012--) .

**d7: Air Ukraine**

- [d7s0] Air Ukraine (Ukrainian: Авіалінії України "Avialiniyi Ukrayiny") was a state-owned airline from Ukraine, serving as flag carrier of the country from 1992 to 2002.
- [d7s1]  Headquartered in Kiev, Air Ukraine operated scheduled passenger and cargo flights mostly on domestic routes or within the Commonwealth of Independent States, but also to other European cities and to North America.

**d8: Cameroon Airlines**

- [d8s0] Cameroon Airlines was an airline from Cameroon, serving as flag carrier of the country.
- [d8s1]  Based in Douala, it operated scheduled services within Africa, as well as to Europe and the Middle East out of its hub at Douala International Airport, with a second network focus on Yaoundé Nsimalen International Airport.
- [d8s2]  The company was 96.43 per cent state owned, with the remaining shares having been held by Air France.
- [d8s3]  It ceased operations in March 2008; its role as Cameroon's flag carrier was taken over by Camair-Co.

**d9: AirBaltic**

- [d9s0] airBaltic, legally incorporated as AS Air Baltic Corporation, is a state-owned Latvian low-cost carrier and the country's flag carrier, with its head office on the grounds of Riga International Airport in Mārupe municipality near Riga.
- [d9s1]  Its main hub is at Riga International Airport with further bases at Tallinn Airport and Vilnius Airport.

**d10: SriLankan Airlines**

- [d10s0] SriLankan Airlines (marketed as SriLankan) is the flag carrier of Sri Lanka.
- [d10s1]  It was launched in 1979 as Air Lanka, following the termination of operations of the original Sri Lankan flag carrier Air Ceylon.
- [d10s2]  Following its partial acquisition in 1998 by Emirates, it was re-branded and introduced the current livery.
- [d10s3]  After ending the Emirates partnership, it has continued using its re-branded name and logo.

## 2. hotpotqa_5adde7085542990dbb2f7f01

原位置：`train` 第 212 题 · 全局第 212 题 · `sample_id: hotpotqa_5adde7085542990dbb2f7f01`

Question: What are both Dichondra and Peperomia?

Note: 这种类型的题目(both, and)按照新的拆分方式拆分，两个对象都要有证据

Type: multipart · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | what Dichondra is | True | [] | plant | [["d3s0"], ["d3s1"]] | context |
| u2 | what Peperomia is | True | [] | plant | [["d5s0"], ["d2s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | what kind of organism Dichondra is | False | [] | plant | [['d3s0'], ['d3s1']] |
| u2 | what kind of organism Peperomia is | False | [] | plant | [['d5s0'], ['d2s0']] |
| u3 | what Dichondra and Peperomia both are | True | ['u1', 'u2'] | plants | [[]] |

### Source documents (reference only)

**d1: Peperomia argyreia**

- [d1s0] Peperomia argyreia, the watermelon peperomia or watermelon begonia, is a species of plant in the Piperaceae family.
- [d1s1]  Its native range is Bolivia, Brazil, Ecuador, and Venezuela.

**d2: List of Peperomia diseases**

- [d2s0] This is a list of diseases that affect the genus "Peperomia" which includes radiator plant, baby rubber tree ("Peperomia obtusifolia"), emerald ripple peperomia ("Peperomia caperata") and others.

**d3: Dichondra**

- [d3s0] Dichondra is a small genus of flowering plants in the morning glory family, Convolvulaceae.
- [d3s1]  They are prostrate, perennial, herbaceous plants, with creeping stems which take root readily at the leaf nodes.
- [d3s2]  The flowers are white, greenish or yellowish, 2–3 mm diameter.

**d4: Peperomia tetraphylla**

- [d4s0] Peperomia tetraphylla, known as the acorn peperomia or four-leaved peperomia, is a small plant in the pepper family that grows in Australia, Asia, Africa, New Zealand, Lord Howe Island, and other islands in the Pacific Ocean.
- [d4s1]  In New South Wales, it is often seen as an epiphyte or growing on rocks in rainforests. Tiny flowers form on a spike, at the end of the branchlets.
- [d4s2]  The specific epithet "tetraphylla" is from the Ancient Greek language, meaning "four leaves".

**d5: Peperomia**

- [d5s0] Peperomia (radiator plant) is one of the 2 large genera of the Piperaceae family, with more than 1000 recorded species.
- [d5s1]  Most of them are compact, small perennial epiphytes growing on rotten wood.
- [d5s2]  More than 1500 species have been recorded, occurring in all tropical and subtropical regions of the world, though concentrated in Central America and northern South America.
- [d5s3]  A limited number of species (around 17) are found in Africa.

**d6: Dichondra repens**

- [d6s0] Dichondra repens is a small, prostrate, herbaceous plant native to New Zealand and many parts of Australia.
- [d6s1]  It is occasionally known as kidney weed in Australia and as Mercury Bay weed in New Zealand.
- [d6s2]  Di (Latin) = two; chondros (Greek) = seed; repens (Latin) = creeping / crawling.
- [d6s3]  Most commonly called dichondra in Australia.

**d7: Peperomia blanda**

- [d7s0] Peperomia blanda, the arid-land peperomia, is a species of herb in the Piperaceae family.
- [d7s1]  The species has a natural pan-tropical distribution that encompasses Asia, Africa, Australasia, Polynesia and the Americas.
- [d7s2]  The species typically grows as a perennial, somewhat succulent herb to 30cm in height, though the form varies from prostrate and creeping to up to 60 cm tall depending on environment and genotype.
- [d7s3]  The typical habitat is damp rock crevices and steep stream banks.

**d8: Peperomia alata**

- [d8s0] Peperomia alata, the winged peperomia, is a plant species found growing in swamps in Florida, West Indies, Central America, South America.
- [d8s1]  In Florida, is apparently rare, known for certain only from Collier County.

**d9: Peperomia wheeleri**

- [d9s0] Peperomia wheeleri is a rare species of flowering plant in the pepper family known by the common name Wheeler's peperomia.
- [d9s1]  It is endemic to Puerto Rico, where it is known only from the island of Culebra.
- [d9s2]  It has been become rare because of deforestation and grazing by livestock.
- [d9s3]  It is a federally listed endangered species of the United States.

**d10: Peperomia caperata**

- [d10s0] Peperomia caperata, the emerald ripple peperomia, is a species of flowering plant in the Piperaceae family, native to Brazil.
- [d10s1]  It is a mound-forming evergreen perennial growing to 20 cm tall and wide, with corrugated heart-shaped leaves, and narrow spikes of white flowers 5 - long, in summer.

## 3. hotpotqa_5ade07a95542997dc790712e

原位置：`train` 第 213 题 · 全局第 213 题 · `sample_id: hotpotqa_5ade07a95542997dc790712e`

Question: Baleine, Nova Scotia is best known as the landing site for a pilot born in which year ?

Note: 保留原拆分

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | pilot for whom Baleine, Nova Scotia is best known as the landing site | False | [] | Beryl Markham | [["d2s1"]] | context |
| u2 | birth year of {u1} | True | ["u1"] | 1902 | [["d1s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | pilot for whom Baleine, Nova Scotia is best known as the landing site | False | [] | Beryl Markham | [['d2s1']] |
| u2 | birth year of {u1} | True | ['u1'] | 1902 | [['d1s0']] |

### Source documents (reference only)

**d1: Beryl Markham**

- [d1s0] Beryl Markham (née Clutterbuck, 26 October 1902 – 3 August 1986) was a British-born Kenyan aviator (one of the first bush pilots), adventurer, racehorse trainer and author.
- [d1s1]  She was the first woman to fly solo across the Atlantic from east to west.
- [d1s2]  She wrote about her adventures in her memoir, "West with the Night".

**d2: Baleine, Nova Scotia**

- [d2s0] Baleine (formerly Port aux Baleines) is a community in the Canadian province of Nova Scotia, located in the Cape Breton Regional Municipality on Cape Breton Island.
- [d2s1]  The community is perhaps best known as the landing site for pilot Beryl Markham's record flight across the Atlantic Ocean (See Memorial Plaque to Record Flight).

**d3: Charles Lawrence (British Army officer)**

- [d3s0] Brigadier-General Charles Lawrence (14 December 1709 – 19 October 1760) was a British military officer who, as lieutenant governor and subsequently governor of Nova Scotia.
- [d3s1]  He is perhaps best known for overseeing the Expulsion of the Acadians and settling the New England Planters in Nova Scotia.
- [d3s2]  He was born in Plymouth, England and died in Halifax, Nova Scotia.
- [d3s3]  According to historian Elizabeth Griffith, Lawrence was seen as a "competent", "efficient" officer with a "service record that had earned him fairly rapid promotion, a person of considerable administrative talent who was trusted by both Cornwallis and Hopson."
- [d3s4]  He is the namesake of Fort Lawrence, Nova Scotia and Lawrencetown, Nova Scotia.
- [d3s5]  He is buried in the crypt of St. Paul's Church (Halifax).

**d4: Mike Smith (actor)**

- [d4s0] Mike Smith (born August 27, 1972) is a Canadian actor and musician born in New Glasgow, Nova Scotia, and raised in Thorburn.
- [d4s1]  He is best known for his portrayal of "Bubbles" and co-writer of the ongoing cult classic television program, films and stage production "Trailer Park Boys".
- [d4s2]  He played hockey for the Pictou County Weeks of the Nova Scotia Midget AAA Hockey League when he was in high school.
- [d4s3]  Smith earned a degree in English from St. Francis Xavier University in Antigonish, Nova Scotia.
- [d4s4]  For a short time in 2006, he was engaged to actress Nichole Hiltz.

**d5: Laurie Swim**

- [d5s0] Laurie Swim, BFA, (born 27 February 1949 in Lockeport, Nova Scotia) is a Canadian visual artist, best known for her quilt art.
- [d5s1]  Her work can be found in the permanent collections of the New York Museum of Arts and Design, the Nova Scotia Art Bank, the Nova Scotia Designer Crafts Council, the Ontario Workers Arts and Heritage Centre, and in private collections.
- [d5s2]  She won the Portia White Prize in 2013.

**d6: Heather Rankin (curler)**

- [d6s0] Heather Rankin (born April 30, 1965) is a Canadian curler from Calgary.
- [d6s1]  While living in Nova Scotia, she won the provincial junior championships in 1984 and would skip the Nova Scotia team at the Canadian Junior Curling Championships.
- [d6s2]  In 1990 she won the Nova Scotia provincial championships sending her to that year's Tournament of Hearts.
- [d6s3]  She skipped the Nova Scotia team to a 9-2 record in her debut winning the all-star skip award, but lost the final to Ontario, skipped by Alison Goring.

**d7: Nova Scotia House of Assembly**

- [d7s0] The Nova Scotia Legislature, formally, known as the General Assembly, consists of the Queen of Canada in Right of Nova Scotia represented by the Lieutenant Governor of Nova Scotia and the House of Assembly, is the legislative branch of the provincial government of Nova Scotia, Canada.
- [d7s1]  The assembly is the oldest in Canada, having first sat in 1758, and in 1848 was the site of the first responsible government in the British Empire.

**d8: Elizabeth Bishop House**

- [d8s0] The Elizabeth Bishop House, also known as the Bulmer House, is an historic single-family house that today is used as an artists' retreat in Great Village, Nova Scotia.
- [d8s1]  The house is associated with Pulitzer Prize winning author Elizabeth Bishop who in her youth lived in the house each summer with her maternal grandparents, William Brown Bulmer and Elizabeth (Hutchinson) Bulmer.
- [d8s2]  Bishop based many of her stories (such as "In the Village") and poems (such as "Filling Station") on aspects of Great Village and Nova Scotia.
- [d8s3]  Although the Bulmers bought the property in 1874, it is not known when it was built.
- [d8s4]  On May 21, 1997, the Bulmer House was recognized as a Nova Scotia Provincially Recognized Heritage Site for its connection to Elizabeth Bishop and her writings as well as for its architectural significance; it is a good example of a typical 1 ⁄ -storey Classical Revival dwelling dating from between 1800 and 1850, a type common to rural Nova Scotia.

**d9: Clarence Gillis**

- [d9s0] Clarence (Clarie) Gillis, MP (October 3, 1895 – December 17, 1960) was a Canadian social democratic politician and trade unionist from Cape Breton Island, Nova Scotia.
- [d9s1]  He was born on Nova Scotia's mainland, but grew-up in Cape Breton.
- [d9s2]  He worked in the island's underground coal mines operated by the British Empire Steel and Coal Company (BESCO).
- [d9s3]  He also served as a member of the infantry in the Canadian Corps in Flanders during the First World War.
- [d9s4]  After the war he returned to the coal mines and became an official with the mine's United Mine Workers of America (UMW) union.
- [d9s5]  In 1938, he helped bring UMW Local 26 into the Co-operative Commonwealth Federation (CCF), becoming the first labour local to affiliate with the party.
- [d9s6]  In 1940, he became the first CCF member elected to the Canadian House of Commons, east of Manitoba.
- [d9s7]  While serving in the House, he was known as its leading voice championing labour issues.
- [d9s8]  He was also a main voice for social rights during his 17-years in Parliament.
- [d9s9]  His most notable achievement was securing the funding that allowed the building of a fixed-link between Nova Scotia's mainland and Cape Breton Island at the Strait of Canso: the Canso Causeway.
- [d9s10]  After winning four-straight elections, he was defeated in 1957 and died three-years later in Glace Bay, Nova Scotia.

**d10: Jonathan Eddy**

- [d10s0] Jonathan Eddy (c. 1726–1804) served for the British in the French and Indian War and for the American Patriots in the American Revolution.
- [d10s1]  After the French and Indian War he settled in Nova Scotia as a New England Planter, becoming a member of the General Assembly of Nova Scotia.
- [d10s2]  During the American Revolutionary War, he was strongly supportive of the rebellion against the Crown.
- [d10s3]  He encouraged the residents of Nova Scotia to join in open revolt against King George III and England.
- [d10s4]  He led a failed attempt to capture Fort Cumberland in 1776 and was forced to retreat to Massachusetts, the place of his birth.
- [d10s5]  The following year he led the defense of Machias, Maine during the Battle of Machias (1777).
- [d10s6]  After the war he established the community now known as Eddington, Maine in 1784, where he died.

## 4. hotpotqa_5ade188e5542990dbb2f7f52

原位置：`train` 第 214 题 · 全局第 214 题 · `sample_id: hotpotqa_5ade188e5542990dbb2f7f52`

Question: Who was the italian actor and screen writer from the 1950s, Marco Ferreri or Gordon Wiles?

Note: 对于这种题干中有需要求证的信息，按照旧拆分的方法

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | whether Marco Ferreri was an Italian actor and screenwriter from the 1950s | False | [] | yes | [["d4s0"]] | context |
| u2 | whether Gordon Wiles was an Italian actor and screenwriter from the 1950s | False | [] | no | [["d7s0"]] | definition_omission |
| u3 | which of Marco Ferreri and Gordon Wiles was the Italian actor and screenwriter from the 1950s | True | ["u1", "u2"] | Marco Ferreri | [[]] | derived_from_dependencies |

- u2：`by_omission=true`，沿用定义性介绍省略规则，不是文中明确否定。

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Marco Ferreri was an Italian actor and screenwriter from the 1950s | False | [] | yes | [['d4s0']] |
| u2 | whether Gordon Wiles was an Italian actor and screenwriter from the 1950s | False | [] | no | [['d7s0']] |
| u3 | which of Marco Ferreri and Gordon Wiles was the Italian actor and screenwriter from the 1950s | True | ['u1', 'u2'] | Marco Ferreri | [[]] |

### Source documents (reference only)

**d1: Kiss the Other Sheik**

- [d1s0] Kiss the Other Sheik (Italian: "Oggi, domani, dopodomani" , also known as The Man, the Woman and the Money) is a 1965 Italian comedy film in three segments, directed by Eduardo De Filippo, Marco Ferreri and Luciano Salce.
- [d1s1]  It stars Marcello Mastroianni, Virna Lisi, Catherine Spaak, Pamela Tiffin and Luciano Salce.

**d2: Break Up (1965 film)**

- [d2s0] Break Up (Italian: L'uomo dei cinque palloni and also known as "The Man with the Balloons") is a 1965 Italian comedy film directed by Marco Ferreri.

**d3: Countersex**

- [d3s0] Controsesso, internationally released as Countersex, is a 1964 Italian anthology comedy film directed by Franco Rossi, Marco Ferreri and Renato Castellani.
- [d3s1]  All the episodies have sex as main theme.
- [d3s2]  The episode of Ferreri is considered by several critics as the masterpiece of the first Italian period of the director.

**d4: Marco Ferreri**

- [d4s0] Marco Ferreri (11 May 1928 – 9 May 1997) was an Italian film director, screenwriter and actor, who began his career in the 1950s directing three films in Spain, followed by 24 Italian films before his death in 1997.

**d5: The House of Smiles**

- [d5s0] The House of Smiles (Italian: "La casa del sorriso" ) is a 1991 Italian film directed by Marco Ferreri.
- [d5s1]  It depicts a romance between an old man and an old woman inside a care home.

**d6: Diary of a Maniac**

- [d6s0] Diary of a Maniac (Italian: "Diario di un vizio" ) is a 1993 Italian drama film directed by Marco Ferreri.
- [d6s1]  It was entered into the 43rd Berlin International Film Festival.

**d7: Gordon Wiles**

- [d7s0] Gordon Wiles (October 10, 1904 – October 17, 1950) was an American art director and film director.
- [d7s1]  He won an Academy Award for Best Art Direction for the film "Transatlantic".
- [d7s2]  He was born in St. Louis, Missouri.
- [d7s3]  His father, Albert Wiles, was a doctor in Jerseyville, Illinois.

**d8: El Pisito**

- [d8s0] El Pisito is a 1959 Spanish comedy film directed by Marco Ferreri.
- [d8s1]  The Spanish Ministry of Culture forced the producers to sign the film as co-directed by Spaniard Isidoro M. Ferry.
- [d8s2]  It was co-written by famous Spanish screenwriter Rafael Azcona, who collaborated with Ferreri throughout his career.

**d9: Liza (1972 film)**

- [d9s0] Liza (Italian: "La cagna" , literally, "The Bitch") is a 1972 Italian drama film directed by Marco Ferreri.

**d10: El Cochecito**

- [d10s0] El Cochecito is a 1960 Spanish black comedy film directed by Marco Ferreri.
- [d10s1]  The film is based on Rafael Azcona's novel and Azcona co-wrote the script with Ferreri.
- [d10s2]  The film was a huge flop when it was released in Spain, but nowadays is a cult classic.
- [d10s3]  The film had troubles with Spanish censorship, that forced to change and cut the original ending.

## 5. hotpotqa_5ade1b7755429975fa854e55

原位置：`train` 第 215 题 · 全局第 215 题 · `sample_id: hotpotqa_5ade1b7755429975fa854e55`

Question: Which band was founded in the 21st century, Foo Fighters or Goon Moon?

Note: 按 A 的候选属性选择规则改成两个 whether ... founded in the 21st century 单元；保留旧 gold 的预设/排除路径并重新验证，不能给 Goon Moon 编造成立年份

Type: comparison · fallback: False · SFT snapshots: 6

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | whether Foo Fighters was founded in the 21st century | False | [] | no | [["d8s0"], ["d9s0"], ["d10s0"]] | context |
| u2 | whether Goon Moon was founded in the 21st century | False | [] | yes | [] | no_direct_support |
| u3 | which of Foo Fighters and Goon Moon was founded in the 21st century | True | ["u1", "u2"] | Goon Moon | [[]] | question_presupposition |

- u2：无直接支持集合；不能仅由 expected_answer 将本单元标为 SUPPORTED。候选题结论可按独立的 presupposition_sets 路径判断。

- u3：`by_presupposition=true`，预设路径 `[["d8s0"], ["d9s0"], ["d10s0"]]`；不是直接证据。

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Foo Fighters was founded in the 21st century | False | [] | no | [['d8s0'], ['d9s0'], ['d10s0']] |
| u2 | whether Goon Moon was founded in the 21st century | False | [] | yes | [] |
| u3 | which of Foo Fighters and Goon Moon was founded in the 21st century | True | ['u1', 'u2'] | Goon Moon | [[]] |

### Source documents (reference only)

**d1: Goon Moon**

- [d1s0] Goon Moon is an American rock band composed of Jeordie White (also known as Twiggy Ramirez) and Chris Goss.
- [d1s1]  The band released the mini-LP "I Got a Brand New Egg Layin' Machine" in 2005 and have since recorded a full-length album, "Licker's Last Leg", which was released on May 8, 2007.
- [d1s2]  The album features cameos from longtime Goss collaborators Josh Homme and Josh Freese, as well as desert rock mainstay Dave Catching.
- [d1s3]  Although Goss and White continue to work on other projects, they have both alluded to the possibility of future Goon Moon recordings on Twitter.

**d2: The Colour and the Shape**

- [d2s0] The Colour and the Shape is the second studio album by the American rock band Foo Fighters.
- [d2s1]  Produced by Gil Norton, it was released through Capitol Records and the group's own Roswell Records on May 20, 1997.
- [d2s2]  The record is the debut of the Foo Fighters as a group, as the band's previous record, "Foo Fighters" (1995), was primarily recorded by frontman Dave Grohl and friend Barrett Jones as a demo.
- [d2s3]  After the project ballooned and became an international success, the group convened for pre-production in the fall of 1996 and brought in producer Norton to establish a pop sensibility for the tracks.
- [d2s4]  The band strived to create a full-fledged rock record, although the music press predicted another grunge offshoot.

**d3: Socialism of the 21st century**

- [d3s0] Socialism of the 21st century (Spanish: "Socialismo del siglo XXI" ) is a political term used to describe the interpretation of socialist principles advocated first by Heinz Dieterich in 1996 and later by Latin American leaders like Hugo Chávez of Venezuela, Rafael Correa of Ecuador, Evo Morales of Bolivia, and Luiz Inácio Lula da Silva of Brazil.
- [d3s1]  Socialism of the 21st century argues that both free-market industrial capitalism and twentieth-century socialism have failed to solve urgent problems of humanity, like poverty, hunger, exploitation, economic oppression, sexism, racism, the destruction of natural resources, and the absence of a truly participative democracy.
- [d3s2]  Therefore, because of the local unique historical conditions, socialism of the 21st century is often contrasted with previous applications of socialism in other countries and aims for a more decentralized and participatory planning process.
- [d3s3]  Socialism of the 21st century has democratic socialist elements, but primarily resembles Marxist revisionism.

**d4: Songs from the Laundry Room**

- [d4s0] Songs from the Laundry Room is an EP by American rock band Foo Fighters, released exclusively for Record Store Day 2015.
- [d4s1]  This EP and the Foo Fighters album are the two Foo Fighters releases upon which Dave Grohl plays all the instruments.

**d5: Foo Fighters: Back and Forth**

- [d5s0] Foo Fighters: Back and Forth is a 2011 rockumentary about the American rock band Foo Fighters, directed by filmmaker James Moll.
- [d5s1]  The film documents the band's history, and gets its title from a track on the Foo Fighters' seventh studio album "Wasting Light".

**d6: 21st century in fiction**

- [d6s0] Many science fiction works have been set in the 21st century (years 2001 to 2100).
- [d6s1]  With humanity now in the 21st century, many of the predictions of these works have so far been proven obsolete.
- [d6s2]  This page lists only "predictions" regarding the 21st century, as opposed to contemporary accounts of the actual 21st century, which would be too numerous to list.

**d7: Sunny Day Real Estate**

- [d7s0] Sunny Day Real Estate was an American emo band from Seattle, Washington.
- [d7s1]  They were one of the early emo bands and helped establish the genre.
- [d7s2]  In 1994, the band released their debut album "Diary" on Sub Pop Records to critical acclaim.
- [d7s3]  However, shortly after releasing their second album "LP2", the band broke up, with members Nate Mendel and William Goldsmith joining Foo Fighters and Jeremy Enigk embarking on a solo career.
- [d7s4]  In 1997, they regrouped long enough to record two more studio albums and a live album but ultimately disbanded once again in 2001.
- [d7s5]  The band reunited again in 2009.
- [d7s6]  Bassist Nate Mendel, who chose to remain with Foo Fighters during the previous reunion in 1997, took part in this reunion.
- [d7s7]  In a 2013 interview with MusicRadar, Mendel said Sunny Day Real Estate was inactive.
- [d7s8]  According to Mendel, the band attempted to record a full-length album after the end of their reunion tour, but the sessions "just fell apart".
- [d7s9]  In 2014 the band released one song from those sessions, "Lipton Witch," on a split 7" vinyl with Circa Survive on Record Store Day.

**d8: Foo Fighters**

- [d8s0] Foo Fighters is an American rock band, formed in Seattle, Washington in 1994.
- [d8s1]  It was founded by Nirvana drummer Dave Grohl as a one-man project following the dissolution of Nirvana after the death of Kurt Cobain.
- [d8s2]  The group got its name from the UFOs and various aerial phenomena that were reported by Allied aircraft pilots in World War II, which were known collectively as "foo fighters".

**d9: List of Foo Fighters band members**

- [d9s0] Foo Fighters is an American alternative rock band formed by multi-instrumentalist and vocalist Dave Grohl in 1994.
- [d9s1]  After recording the album "Foo Fighters" alone, Grohl enlisted guitarist Pat Smear, bassist Nate Mendel and drummer William Goldsmith to join the band.
- [d9s2]  This lineup recorded the second Foo Fighters album, 1997's "The Colour and the Shape", although most of Goldsmith's drum recordings were removed and re-recorded by Grohl for the release, after he left the band due to creative tensions.
- [d9s3]  Goldsmith was replaced by Taylor Hawkins, and Franz Stahl replaced Smear after he also departed, although he only remained in the band for a short period and did not record an album with the group.
- [d9s4]  The group's third album, "There Is Nothing Left to Lose", featured Hawkins on drums and was released in 1999.

**d10: Foo Fighters live performances**

- [d10s0] Foo Fighters is an American alternative rock band, founded in 1994 by musician Dave Grohl.
- [d10s1]  After recording by himself what would become the album Foo Fighters, Grohl decided to recruit a full band with him as singer and guitarist.
- [d10s2]  The original line-up included bassist Nate Mendel, drummer William Goldsmith, and Pat Smear.

## 6. hotpotqa_5ade9914554299728e26c759

原位置：`train` 第 216 题 · 全局第 216 题 · `sample_id: hotpotqa_5ade9914554299728e26c759`

Question:  Burying the Ex is a comedy horror film starring an American actress known for playing Alice Cullen in the film adaptations of what novels?

Note: u1 补上 known for playing Alice Cullen，

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 按 Note 补 Alice Cullen 限定，联合演员表、美国女演员身份及角色证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | American actress starring in Burying the Ex known for playing Alice Cullen | False | [] | Ashley Greene | [["d5s1", "d1s0", "d1s1"]] | context |
| u2 | novels that feature Alice Cullen as played by {u1} | True | ["u1"] | Twilight | [["d1s1"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | actress starring in Burying the Ex who is known for playing Alice Cullen | False | [] | Ashley Greene | [['d5s1', 'd1s1']] |
| u2 | novels whose film adaptations featured {u1} as Alice Cullen | True | ['u1'] | Twilight | [['d1s1']] |

### Source documents (reference only)

**d1: Ashley Greene**

- [d1s0] Ashley Michele Greene (born February 21, 1987) is an American actress and model.
- [d1s1]  She is known for playing Alice Cullen in the film adaptations of Stephenie Meyer's "Twilight" novels.

**d2: The Uninvited (2009 film)**

- [d2s0] The Uninvited is a 2009 American psychological horror film directed by the Guard Brothers, and starring Emily Browning, Elizabeth Banks, Arielle Kebbel and David Strathairn.
- [d2s1]  It is a remake of the 2003 South Korean K-Horror film "A Tale of Two Sisters", which is in turn one of several film adaptations of the Korean folk tale Janghwa Hongryeon jeon.
- [d2s2]  The film received mixed reviews.

**d3: Peter Facinelli**

- [d3s0] Peter Facinelli (born November 26, 1973) is an American actor and producer.
- [d3s1]  He starred as Donovan "Van" Ray on the Fox series "Fastlane" from 2002 to 2003.
- [d3s2]  He played Dr. Carlisle Cullen in the film adaptations of the "Twilight" novel series, and is also known for his role as Mike Dexter in the 1998 film "Can't Hardly Wait".
- [d3s3]  Facinelli was a regular on the Showtime comedy-drama series "Nurse Jackie", portraying the role of Dr. Fitch "Coop" Cooper.
- [d3s4]  He portrayed Maxwell Lord on the first season of the TV series "Supergirl".

**d4: Suck (film)**

- [d4s0] Suck is a 2009 rock-and-roll vampire black comedy horror film starring, written and directed by Rob Stefaniuk.
- [d4s1]  Stefaniuk stars alongside Canadian actress Jessica Paré, Nicole de Boer (his castmate from the TV series "Catwalk"), Malcolm McDowell and rock legends Alice Cooper, Iggy Pop, Henry Rollins and Alex Lifeson of Rush.
- [d4s2]  Production took place in and around Toronto in late 2008.

**d5: Burying the Ex**

- [d5s0] Burying the Ex is a 2014 American comedy horror film directed by Joe Dante and written by Alan Trezza.
- [d5s1]  The film stars Anton Yelchin, Ashley Greene, Alexandra Daddario and Oliver Cooper.
- [d5s2]  It screened out of competition at the 71st Venice International Film Festival.
- [d5s3]  The film was released on June 19, 2015, by Image Entertainment.

**d6: Bloodbath at the House of Death**

- [d6s0] Bloodbath at the House of Death is a 1983 comedy horror film starring the British comedian Kenny Everett and featuring Vincent Price.
- [d6s1]  It is an over-the-top spoof loosely inspired by "The Amityville Horror" and other horror films from the same period.

**d7: Paloma Bernardi**

- [d7s0] Paloma Bernardi (born April 21, 1985) is a Brazilian actress.
- [d7s1]  She became known in Brazil when playing the character Mia in the telenovela Viver a Vida on Globo in which she won the Trophy Super Gold Cap 2010 (Troféu Super Cap de Ouro).
- [d7s2]  Paloma is also known for playing Alice in the novel Insensato Coração and also by interpret the villainess Rosângela in Salve Jorge which began as the victim Trafficking and in the course of the novel became a dealer.
- [d7s3]  Paloma is the daughter of businessman Nestor Bernardi gaucho, and visual artist and former dancer of the Ballet Popular do Recife, Dil Bernardi.
- [d7s4]  Born in the city of São Paulo in north of the city of São Paulo, where he maintains with his family Amarte Cultural Space.

**d8: Leisha Hailey**

- [d8s0] Leisha Hailey (born July 11, 1971) is an American actress and musician known for playing Alice Pieszecki in the Showtime Networks series "The L Word".
- [d8s1]  Hailey first came to the public's attention as a musician in the pop duo The Murmurs and has continued her music career as part of the band Uh Huh Her.

**d9: Kim Ostrenko**

- [d9s0] Kim Ostrenko is an American actress with roles in 16 movies and TV shows, most recently playing Alice Connellan in "Dolphin Tale" (2011).
- [d9s1]  She has also played a number of theater roles.

**d10: Megan Fox**

- [d10s0] Megan Denise Fox (born May 16, 1986) is an American actress and model.
- [d10s1]  She began her acting career in 2001, with several minor television and film roles, and played a regular role on the "Hope & Faith" television sitcom.
- [d10s2]  In 2004, she made her film debut with a role in the teen comedy "Confessions of a Teenage Drama Queen".
- [d10s3]  In 2007, she co-starred as Mikaela Banes, the love interest of Shia LaBeouf's character, in the blockbuster action film "Transformers", which became her breakout role.
- [d10s4]  Fox reprised her role in the 2009 sequel, "".
- [d10s5]  Later in 2009, she starred as the eponymous lead in the black comedy horror film "Jennifer's Body".

## 7. hotpotqa_5adea8a655429939a52fe92c

原位置：`train` 第 217 题 · 全局第 217 题 · `sample_id: hotpotqa_5adea8a655429939a52fe92c`

Question: Are both Andrei Platonov and Edward Albee a writer?

Note: 

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | whether Andrei Platonov is a writer | False | [] | yes | [["d7s0"], ["d8s2"]] | context |
| u2 | whether Edward Albee is a writer | False | [] | yes | [["d10s0"], ["d5s0"], ["d3s0"]] | context |
| u3 | whether both Andrei Platonov and Edward Albee are writers | True | ["u1", "u2"] | yes | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Andrei Platonov is a writer | False | [] | yes | [['d7s0'], ['d8s2']] |
| u2 | whether Edward Albee is a writer | False | [] | yes | [['d10s0'], ['d5s0'], ['d3s0']] |
| u3 | whether Andrei Platonov and Edward Albee are both writers | True | ['u1', 'u2'] | yes | [[]] |

### Source documents (reference only)

**d1: Edward Albee's At Home at the Zoo**

- [d1s0] Edward Albee's At Home at the Zoo (formerly titled "Peter & Jerry") is a play by Edward Albee which adds a first act to his 1959 play "The Zoo Story".
- [d1s1]  This first act, also called "Homelife", revolves around the marriage of Peter and Ann and ends with Peter leaving to go read a book in Central Park.

**d2: The Cow (1989 film)**

- [d2s0] The Cow (Russian: Корова Korova) is a 1989 Soviet animated short film directed by Aleksandr Petrov.
- [d2s1]  It tells the story of a boy who recalls how his family lost its cow.
- [d2s2]  The film is based on a short story by Andrei Platonov and was made using paint-on-glass animation.

**d3: Edward F. Albee Foundation**

- [d3s0] The Edward F. Albee Foundation was started by its namesake, playwright Edward Albee, in 1967, after revenue from his play Who's Afraid of Virginia Woolf?
- [d3s1]  proved abundant.

**d4: Three Brothers (1981 film)**

- [d4s0] Three Brothers (Italian: "Tre fratelli" ) is a 1981 Italian film based on a work by Andrei Platonov.
- [d4s1]  It was directed by Francesco Rosi and stars Philippe Noiret, Vittorio Mezzogiorno, Michele Placido and Charles Vanel.

**d5: The Zoo Story**

- [d5s0] The Zoo Story is a one-act play by American playwright Edward Albee.
- [d5s1]  His first play, it was written in 1958 and completed in just three weeks.
- [d5s2]  The play explores themes of isolation, loneliness, miscommunication as anathematization, social disparity and dehumanization in a commercial world.
- [d5s3]  Now, professional theatre companies can only produce "The Zoo Story" as a part of "Edward Albee's at Home at the Zoo" (originally titled "Peter and Jerry").

**d6: Natascha Drubek**

- [d6s0] Natascha Drubek (Drubek-Meyer) is a researcher, author and editor in the area of Central and East European literature, film and media.
- [d6s1]  Since 2012 she has been teaching Comparative Literature and Film and Media Studies at the Free University of Berlin.
- [d6s2]  She is one of the developers of Hyperkino and the editor-in-chief of the open access academic journal Apparatus.
- [d6s3]  From 2003 until 2014 she was the editor of the Film and Screen Media section ARTmargins, a journal for contemporary Central & Eastern European Visual Culture.
- [d6s4]  Between 2009 and 2015 Natascha Drubek was a Heisenberg Fellow of the Deutsche Forschungsgeminschaft at the University of Regensburg pursuing two projects: Soviet Antireligious Films and Campaigns and the film projects in the Theresienstadt Concentration Camp.
- [d6s5]  In 2014, during her Heisenberg fellowship she organized a conference on film propaganda in Theresienstadt Concentration Camp.
- [d6s6]  In 2016 Drubek published a selection of the conference proceedings as a double Special Issue of Apparatus.
- [d6s7]  She holds a PhD from Ludwig Maximilian University of Munich (with a thesis on Nikolai Gogol) where she was also habilitated with a monograph on the cultural history of early Russian film centering on the Russian pre-revolutionary director Evgenii Bauer ("Russisches Licht.
- [d6s8]  Von der Ikone zum frühen sowjetischen Kino", 2012).
- [d6s9]  Her other research interests include Fyodor Dostoyevsky, Andrei Platonov, Vladimir Sorokin, and Jana Černá, born Krejcarová.

**d7: Andrei Platonov**

- [d7s0] Andrei Platonov (Russian: Андре́й Плато́нов , ] ; August 28 [O.S. August 16] 1899 – January 5, 1951) was the pen name of Andrei Platonovich Klimentov (Russian: Андре́й Плато́нович Климе́нтов ), a Soviet Russian writer, playwright, and poet, whose works anticipate existentialism.
- [d7s1]  Although Platonov was a Communist, most of his works were banned in his own lifetime for their skeptical attitude toward collectivization and other Stalinist policies, as well as for its experimental, avant-garde form.
- [d7s2]  His famous works include the novels "The Foundation Pit" (Котлован) and "" (Чевенгур)

**d8: Alexander Vvedensky (poet)**

- [d8s0] Alexander Ivanovich Vvedensky (Russian: Алекса́ндр Ива́нович Введе́нский ; 1904–1941) was a Russian poet and dramatist with formidable influence on "unofficial" and avant-garde art during and after the times of the Soviet Union.
- [d8s1]  Vvedensky is widely considered (among contemporary Russian writers and literary scholars) as one of the most original and important authors to write in Russian in the early Soviet period.
- [d8s2]  He is placed on par with writers such as Andrei Platonov for innovation in the language.
- [d8s3]  Vvedensky considered his own poetry "a critique of reason more powerful than Kant's."

**d9: The Lonely Voice of Man**

- [d9s0] The Lonely Voice of Man (Russian: Одинокий голос человека ), also known as The Lonely Human Voice, is the first full-feature film by Alexander Sokurov.
- [d9s1]  It was originally filmed in 1978 and reconstructed in 1987 at the Lenfilm studios.
- [d9s2]  The film is largely based on Andrei Platonov's "River Potudan" and "Origin of the Master", although it is not a direct film adaptation in the traditional sense but rather a recreation of the spiritual nature of Platonov's prose.

**d10: Edward Albee**

- [d10s0] Edward Franklin Albee III ( ; March 12, 1928 – September 16, 2016) was an American playwright known for works such as "The Zoo Story" (1958), "The Sandbox" (1959), "Who's Afraid of Virginia Woolf?
- [d10s1] " (1962), and "A Delicate Balance" (1966).
- [d10s2]  Three of his plays won the Pulitzer Prize for Drama, and two of his other works won the Tony Award for Best Play.

## 8. hotpotqa_5adec3db55429975fa854f83

原位置：`train` 第 218 题 · 全局第 218 题 · `sample_id: hotpotqa_5adec3db55429975fa854f83`

Question: Are Blood Bowl and Afrikan tähti both games?

Note: 

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | whether Blood Bowl is a game | False | [] | yes | [["d7s0"], ["d7s1"], ["d5s0"], ["d4s0"], ["d6s1"], ["d9s1"]] | context |
| u2 | whether Afrikan tähti is a game | False | [] | yes | [["d8s0"], ["d8s1"], ["d3s1"], ["d10s0"]] | context |
| u3 | whether both Blood Bowl and Afrikan tähti are games | True | ["u1", "u2"] | yes | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Blood Bowl is a game | False | [] | yes | [['d7s0'], ['d7s1'], ['d5s0'], ['d4s0'], ['d6s1'], ['d9s1']] |
| u2 | whether Afrikan tähti is a game | False | [] | yes | [['d8s0'], ['d8s1'], ['d3s1'], ['d10s0']] |
| u3 | whether Blood Bowl and Afrikan tähti are both games | True | ['u1', 'u2'] | yes | [[]] |

### Source documents (reference only)

**d1: Online Blood Bowl League Manager**

- [d1s0] Online Blood Bowl League Manager (OBBLM) is an internet package mainly written in PHP & MySQL programming language and available under the terms of the GNU General Public License (GPL).
- [d1s1]  Online Blood Bowl League Manager allows you to easily manage your blood bowl leagues tournaments, games, teams, players, skills and much more.

**d2: Blood Bowl Sutra**

- [d2s0] The Blood Bowl Sutra (Chinese: 血盆經; pinyin: Xuèpénjīng, Japanese: Ketsubon Kyō) is an apocryphal Mahayana sutra of Chinese origin.
- [d2s1]  The earliest version of this text was likely composed around the end of the 12th century or the beginning of the 13th.

**d3: Kari Mannerla**

- [d3s0] Kari Mannerla (January 9, 1930, Helsinki, Finland – July 12, 2006, Helsinki, Finland) was a Finnish board and card game designer and advertising agency executive.
- [d3s1]  The most famous game designed by Mannerla is the board game "Afrikan tähti" ("The Star of Africa"), the idea of which he began to develop in 1949.
- [d3s2]  The game was published two years later.
- [d3s3]  Mannerla made up the name of the game when reading an article about the biggest diamond in the world, the Star of Africa, discovered in South Africa.

**d4: Blood Bowl (1995 video game)**

- [d4s0] Blood Bowl is the turn-based strategy video game adaptation of the popular Games Workshop miniatures game, originally developed for MS-DOS computers by MicroLeague.

**d5: Blood Bowl (2009 video game)**

- [d5s0] Blood Bowl is a fantasy football video game developed by Cyanide, loosely based on American football, and adapted from the board game of the same name, which is produced by Games Workshop, using the CRP ruleset.

**d6: Blood Bowl 2**

- [d6s0] Blood Bowl 2 is a turn-based fantasy sports video game developed by Cyanide Studios and published by Focus Home Interactive.
- [d6s1]  It is a sequel to the 2009 video game "Blood Bowl", based on the board game by Games Workshop.
- [d6s2]  The game was developed for Microsoft Windows, PlayStation 4, and Xbox One, and was released on 22 September 2015.
- [d6s3]  A Mac OS X version of the game was launched in May 2016.

**d7: Blood Bowl**

- [d7s0] Blood Bowl is a fantasy football game created by Jervis Johnson for the British games company Games Workshop as a parody of American Football.
- [d7s1]  The game was first released in 1986 and has been re-released in new editions since.
- [d7s2]  "Blood Bowl" is set in an alternate version of the "Warhammer Fantasy" setting, populated by traditional fantasy elements such as human warriors, goblins, dwarves, elves, orcs and trolls.

**d8: Afrikan tähti**

- [d8s0] Afrikan tähti (] ; Finnish: Star of Africa), known in Swedish as Den försvunna diamanten (The Missing Diamond) or Afrikas stjärna meaning ""the star of Africa"", is a Finnish board game designed by Kari Mannerla originally in 1951.
- [d8s1]  It has been one of the most popular board games in Scandinavia for decades.

**d9: Impact! Miniatures**

- [d9s0] Impact!
- [d9s1]  Miniatures is a company started in April 2006 by members of the Blood Bowl online community with the aim of producing figures suitable for use with Fantasy Football games such as Elfball, Blood Bowl, Street Brawl, Street Bowl and Deathball.

**d10: Inkan aarre**

- [d10s0] Inkan aarre (Finnish for "The treasure of the Inca") is a 2005 Finnish board game, designed by Kari Mannerla as a direct sequel to his 1951 board game "Afrikan tähti".

## 9. hotpotqa_5adf9e59554299025d62a2e9

原位置：`train` 第 219 题 · 全局第 219 题 · `sample_id: hotpotqa_5adf9e59554299025d62a2e9`

Question: Was the Pixies a rock band when Pierre Bouvier was a child?

Note: 题型改成comparison，保持新顺序

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。 题型修正为 comparison。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | birth date of Pierre Bouvier | False | [] | 9 May 1979 | [["d5s0"]] | context |
| u2 | year Pixies became a rock band | False | [] | 1986 | [["d3s0"]] | context |
| u3 | whether Pixies was a rock band when Pierre Bouvier was a child | True | ["u1", "u2"] | yes | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | year in which the Pixies formed as a rock band | False | [] | 1986 | [['d3s0']] |
| u2 | date of birth of Pierre Bouvier | False | [] | 9 May 1979 | [['d5s0']] |
| u3 | whether the Pixies was a rock band when Pierre Bouvier was a child | True | ['u1', 'u2'] | yes | [[]] |

### Source documents (reference only)

**d1: Kim Deal**

- [d1s0] Kimberley Ann "Kim" Deal (born June 10, 1961) is an American singer, songwriter and musician, best known as the former bassist and backup vocalist of the alternative rock band Pixies, and the lead vocalist and rhythm guitarist for The Breeders.
- [d1s1]  Deal joined Pixies in January 1986 as the band's bassist, adopting the stage name Mrs. John Murphy for the albums "Come on Pilgrim" and "Surfer Rosa".
- [d1s2]  Following "Doolittle" and Pixies' hiatus, she formed The Breeders with Tanya Donelly, Josephine Wiggs and later introduced her identical twin sister Kelley Deal.
- [d1s3]  Pixies broke up in early 1993.

**d2: The Breeders discography**

- [d2s0] The discography of American alternative rock band The Breeders consists of four studio albums, one live album, three extended plays, ten singles and twelve music videos. Kim Deal, then-bassist of American alternative rock band the Pixies, formed The Breeders as a side-project with Tanya Donelly, guitarist of American alternative rock band Throwing Muses.
- [d2s1]  After recording a demo tape, The Breeders signed to the English independent record label 4AD in 1989.
- [d2s2]  Their debut studio album "Pod" was released in May 1990, but was not commercially successful.
- [d2s3]  After the revival of the Pixies and Throwing Muses in 1990, The Breeders became mostly inactive until the Pixies' breakup in 1993.
- [d2s4]  With a new lineup, The Breeders released their "Safari" EP in 1992, followed by their second studio album "Last Splash" in 1993.
- [d2s5]  "Last Splash" was The Breeders' most successful album; it peaked at number 33 on the United States "Billboard" 200 and was certified platinum by the Recording Industry Association of America in 1994.
- [d2s6]  The album spawned the band's most successful single, "Cannonball".
- [d2s7]  The single peaked at number 44 on the US "Billboard" Hot 100 and at number two on the "Billboard" Alternative Songs chart.

**d3: Pixies**

- [d3s0] The Pixies are an American alternative rock band formed in 1986 in Boston, Massachusetts.
- [d3s1]  Until 2013, the band comprised Black Francis (lead vocals, rhythm guitar), Joey Santiago (lead guitar), Kim Deal (bass, backing vocals) and David Lovering (drums).
- [d3s2]  The band disbanded acrimoniously in 1993, but reunited in 2004.
- [d3s3]  After Deal left in 2013, the Pixies hired Kim Shattuck as a touring bassist; she was replaced the same year by Paz Lenchantin, who became a permanent member in 2016.

**d4: Bossanova (Pixies album)**

- [d4s0] Bossanova is the third studio album by American rock band Pixies.
- [d4s1]  It was released in August 13, 1990 on the English independent record label 4AD in the United Kingdom and by Elektra Records in the United States.
- [d4s2]  All of "Bossanova"<nowiki>'</nowiki>s original material was written by the band's frontman Black Francis; this was a first for a Pixies album, but he has written all of their songs since.
- [d4s3]  The album's sound, inspired by surf rock and space rock, complements its lyrical focus on outer space, which references subjects such as aliens and unidentified flying objects.

**d5: Pierre Bouvier**

- [d5s0] Pierre Charles Bouvier {'1': ", '2': ", '3': ", '4': "} (born 9 May 1979) is a Canadian singer, songwriter, musician, composer and actor who is best known as the lead singer and guitarist of the rock band Simple Plan.

**d6: List of Pixies tribute albums**

- [d6s0] A number of tribute albums to the Pixies, an American alternative rock band, have been recorded since the band's break-up in 1993.
- [d6s1]  Artists featured on the albums range from American rock bands, such as Weezer, OK Go and Eve 6, to lesser-known European bands.
- [d6s2]  The first widely released Pixies tribute album, "Death to the Pixies—We're Better!"
- [d6s3] , was released in February 1998 as the result of a Pixies cover contest in the Netherlands that was launched by the magazine Oor, the radio station VPRO and the record label Play It Again Sam.

**d7: History (Story Untold song)**

- [d7s0] "History" is the first single from Canadian band Story Untold.
- [d7s1]  The members of Story Untold are from Quebec, Canada, which is also home to Simple Plan.
- [d7s2]  Simple Plan has known the five-piece for a while, and the French Canadians teamed up to write Story Untold's newest single "History".
- [d7s3]  The song is about how the band is going to make it big, even if it seems like a crazy idea: "You can call me crazy/But when I close my eyes/I can see it clearly/I can see the shining lights."
- [d7s4]  The song was co-penned with Simple Plan's vocalist Pierre Bouvier and drummer Chuck Comeau.
- [d7s5]  The song is just one of seven songs on the band's self-titled EP.
- [d7s6]  History also has a music video where the band is a part of an underground fight club.
- [d7s7]  It features each boy taking on a different fighter, and it subtly introduces each band member for those who have never heard of Story Untold before.
- [d7s8]  An acoustic version of the song does appear on YouTube but is not featured on the Story Untold EP.

**d8: Chuck Comeau**

- [d8s0] Charles-André "Chuck" Comeau {'1': ", '2': ", '3': ", '4': "} (born 17 September 1979) is a Canadian musician and drummer, best known for being the drummer of the rock band Simple Plan.
- [d8s1]  He also founded the apparel company Role Model Clothing along with his bandmate Pierre Bouvier and the band's best friend, Patrick Langlois.
- [d8s2]  He is also former drummer for the punk rock band Reset from 1993 to 1999, which he quit to form Simple Plan with his Reset bandmate who also left Reset, Pierre Bouvier.

**d9: I'm Just a Kid**

- [d9s0] "I'm Just a Kid" is the debut single by the band Simple Plan, written by Pierre Bouvier.
- [d9s1]  It appeared on their debut album "No Pads, No Helmets... Just Balls".
- [d9s2]  It was featured in the films "Grind", "The New Guy", and "Cheaper by the Dozen".

**d10: Joey Santiago**

- [d10s0] Joseph Alberto "Joey" Santiago (born June 10, 1965) is a Filipino-American guitarist and composer.
- [d10s1]  Active since 1986, Santiago is best known as the lead guitarist for the American alternative rock band the Pixies.
- [d10s2]  After the band's breakup in 1993, Santiago produced musical scores for film and television documentaries, and he formed The Martinis with his wife, Linda Mallari.
- [d10s3]  He also contributed to albums by Charles Douglas and former Pixies band-mate Frank Black.
- [d10s4]  Santiago resumed his role as the Pixies' lead guitarist when they reunited in 2004.

## 10. hotpotqa_5adfdcf5554299025d62a367

原位置：`train` 第 220 题 · 全局第 220 题 · `sample_id: hotpotqa_5adfdcf5554299025d62a367`

Question:  Royal Air Force Valley provides fast-jet training using an advanced trainer aircraft first flown in what year?

Note: 

Type: bridge · fallback: False · SFT snapshots: 7

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | advanced trainer aircraft used by Royal Air Force Valley | False | [] | BAE Systems Hawk | [["d1s1"]] | context |
| u2 | year the aircraft in {u1} was first flown | True | ["u1"] | 1974 | [["d3s1"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | advanced trainer aircraft used by Royal Air Force Valley for fast-jet training | False | [] | BAE Systems Hawk | [['d1s1']] |
| u2 | year {u1} was first flown | True | ['u1'] | 1974 | [['d3s1']] |

### Source documents (reference only)

**d1: RAF Valley**

- [d1s0] Royal Air Force Valley or more simply RAF Valley (Welsh: "RAF y Fali" ) (IATA: VLY, ICAO: EGOV) is a Royal Air Force station on the island of Anglesey, Wales, and which is also used as Anglesey Airport.
- [d1s1]  It provides fast-jet training using the BAE Systems Hawk and provides training for aircrew working with search and rescue.

**d2: Muniz M-9**

- [d2s0] The Muniz M-9 was a two-seat training biplane with tandem open cockpit and powered by a 200 hp (149 kW) 130 hp (197 kW) de Havilland Gipsy Six engine.
- [d2s1]  Designed by Lieutenant-Colonel Antonio Muniz, a serving officer in the Brazilian Air Force, as an advanced trainer and was very similar to his earlier M-7 primary trainer.
- [d2s2]  It was first flown in 1937 and a small production run was built for the air force by Cia Nacional de Navegacao Costiera.

**d3: BAE Systems Hawk**

- [d3s0] The BAE Systems Hawk is a British single-engine, jet-powered advanced trainer aircraft.
- [d3s1]  It was first flown at Dunsfold, Surrey, in 1974 as the Hawker Siddeley Hawk, and subsequently produced by its successor companies, British Aerospace and BAE Systems, respectively.
- [d3s2]  It has been used in a training capacity and as a low-cost combat aircraft.

**d4: Royal Air Force Music Services**

- [d4s0] Royal Air Force Music Services is the organization which provides military musical support to the Royal Air Force.
- [d4s1]  Based at RAF Northolt (previously at RAF Uxbridge) and RAF Cranwell, it forms the central administration of one hundred and seventy musicians divided between the Central Band of the Royal Air Force, The Band of the Royal Air Force College, The Band of the Royal Air Force Regiment and Headquarters Music Services.
- [d4s2]  These main military bands contain within their ranks the Royal Air Force Squadronnaires, Royal Air Force Swing Wing, Royal Air Force Shades of Blue, and The Salon Orchestra of the Central Band of the Royal Air Force.

**d5: Beechcraft T-6 Texan II**

- [d5s0] The Beechcraft T-6 Texan II is a single-engine turboprop aircraft built by the Raytheon Aircraft Company (which became Hawker Beechcraft and later Beechcraft Defense Company, and was bought by Textron Aviation in 2014).
- [d5s1]  A trainer aircraft based on the Pilatus PC-9, the T-6 has replaced the Air Force's Cessna T-37B Tweet and the Navy's T-34C Turbo Mentor.
- [d5s2]  The T-6A is used by the United States Air Force for basic pilot training and Combat Systems Officer (CSO) training and by the United States Navy and United States Marine Corps for primary Naval Aviator training as well as primary and intermediate Naval Flight Officer (NFO) training.
- [d5s3]  The T-6A is also used as a basic trainer by the Royal Canadian Air Force (CT-156 Harvard II), the Greek Air Force, the Israeli Air Force ("Efroni"), and the Iraqi Air Force.
- [d5s4]  The T-6B is the primary trainer for U.S. student naval aviators.
- [d5s5]  The T-6C is used for training by the Mexican Air Force, Royal Air Force, Royal Moroccan Air Force, and the Royal New Zealand Air Force.

**d6: Yakovlev Yak-130**

- [d6s0] The Yakovlev Yak-130 (NATO reporting name: Mitten) is a subsonic two-seat advanced trainer aircraft originally developed by Yakovlev and Aermacchi.
- [d6s1]  It has also been marketed as a potential light attack aircraft.
- [d6s2]  Development of the plane began in 1991 and the maiden flight was conducted on 25 April 1996.
- [d6s3]  In 2002, it won a Russian government tender for training aircraft and in 2009 the aircraft entered service with the Russian Air Force.
- [d6s4]  As an advanced training aircraft, the Yak-130 is able to replicate the characteristics of several 4+ generation fighters as well as the fifth-generation Sukhoi Su-57.
- [d6s5]  It can also perform light-attack and reconnaissance duties, carrying a combat load of 3,000 kg.

**d7: Boulton Paul Balliol**

- [d7s0] The Boulton Paul Balliol and Sea Balliol were monoplane military advanced trainer aircraft built for the Royal Air Force (RAF) and the Royal Navy Fleet Air Arm (FAA) by Boulton Paul Aircraft.
- [d7s1]  Developed in the late 1940s the Balliol was designed to replace the North American Harvard trainer and used the Rolls-Royce Merlin engine, with the Sea Balliol a naval version for deck landing training.

**d8: Partenavia Mosquito**

- [d8s0] The Partenavia P.86 Mosquito was a two-seat civil trainer aircraft first flown in Italy on 27 April 1986.
- [d8s1]  It was a high-wing monoplane of pod-and-boom construction with tricycle undercarriage and a twin tail, that accommodated the student and instructor side-by-side.

**d9: Miles Magister**

- [d9s0] The Miles M.14 Magister is a British two-seat monoplane basic trainer aircraft built by the Miles Aircraft for the Royal Air Force and Fleet Air Arm.
- [d9s1]  Affectionately known as the Maggie, the Magister was based on Miles' civilian Hawk Major and Hawk Trainer and was the first monoplane designed specifically as a trainer for the RAF.
- [d9s2]  As a low-wing monoplane, it was an ideal introduction to the Spitfire and Hurricane for new pilots.
- [d9s3]  Its sister design, the Miles Master was an advanced trainer also built by Phillips & Powis at Woodley.

**d10: North American T-6 Texan**

- [d10s0] The North American Aviation T-6 Texan is an American single-engined advanced trainer aircraft used to train pilots of the United States Army Air Forces (USAAF), United States Navy, Royal Air Force, and other air forces of the British Commonwealth during World War II and into the 1970s.
- [d10s1]  Designed by North American Aviation, the T-6 is known by a variety of designations depending on the model and operating air force.
- [d10s2]  The United States Army Air Corps (USAAC) and USAAF designated it as the AT-6, the United States Navy the SNJ, and British Commonwealth air forces the Harvard, the name by which it is best known outside of the US.
- [d10s3]  Starting in 1948, the new United States Air Force (USAF) designated it the T-6, with the USN following in 1962.
- [d10s4]  It remains a popular warbird aircraft used for airshow demonstrations and static displays.
- [d10s5]  It has also been used many times to simulate various Japanese aircraft, including the Mitsubishi A6M Zero in movies depicting World War II in the Pacific.

## 11. hotpotqa_5ae05ae955429945ae959340

原位置：`train` 第 221 题 · 全局第 221 题 · `sample_id: hotpotqa_5ae05ae955429945ae959340`

Question: On what network did an American actress portray Shirley Partridge, along with David Cassidy, beginning in 1970?

Note: 

Type: bridge · fallback: False · SFT snapshots: 7

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | television show where Shirley Partridge was portrayed by an American actress along with David Cassidy | False | [] | The Partridge Family | [["d7s4"], ["d4s1"]] | context |
| u2 | network that aired {u1} | True | ["u1"] | ABC | [["d10s2"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | television series in which an American actress portrayed Shirley Partridge along with David Cassidy beginning in 1970 | False | [] | The Partridge Family | [['d7s4'], ['d4s1']] |
| u2 | network on which {u1} aired | True | ['u1'] | ABC | [['d10s2']] |

### Source documents (reference only)

**d1: The Partridge Family Album**

- [d1s0] The Partridge Family Album is The Partridge Family's first album.
- [d1s1]  It was released in 1970 and included their first recording, "I Think I Love You".
- [d1s2]  It has a picture of the whole family on the back and a small picture of David Cassidy and Shirley Jones.
- [d1s3]  The album cover is made to look like an old-fashioned photo album.
- [d1s4]  The original release of the album included a framed color photograph of the group.
- [d1s5]  The exterior label promoting the inclusion of the hit song was affixed to the jacket itself, not the shrink wrap.

**d2: David Cassidy: Man Undercover**

- [d2s0] David Cassidy: Man Undercover (the word "undercover" in the series title appeared at various times written as one word or two) was an American police drama starring David Cassidy, four years after his run starring in the "The Partridge Family", marking his first starring role since that series was cancelled.
- [d2s1]  The series was spun off after Cassidy starred in a special two-hour episode of "Police Story", titled "A Chance to Live," which aired in May 1978; this episode served as the pilot for "Man Undercover".

**d3: David Cassidy discography**

- [d3s0] The discography of David Cassidy, an American pop artist, consists of twelve studio albums, three live albums, six compilation albums, two soundtrack albums, and twenty-four singles.
- [d3s1]  David Cassidy has been recording albums since 1970.
- [d3s2]  His career is most notable for his solo music and his recordings with the Partridge Family.

**d4: David Cassidy**

- [d4s0] David Bruce Cassidy (born April 12, 1950) is a retired American actor, singer, songwriter, and guitarist.
- [d4s1]  He is known for his role as Keith Partridge, the son of Shirley Partridge (played by his stepmother Shirley Jones), in the 1970s musical-sitcom "The Partridge Family", which led to his becoming one of popular culture's teen idols and pop singers of the 1970s.
- [d4s2]  He later had a career in both acting and music.

**d5: Old Trick New Dog**

- [d5s0] Old Trick New Dog is a 1998 album from David Cassidy on his own Slamajama Records label.
- [d5s1]  In addition to new songs, it also features several remakes of songs from "The Partridge Family".
- [d5s2]  The single lifted from the album - "No Bridge I Wouldn't Cross" - was an Adult Contemporary Top 25 hit in the USA.
- [d5s3]  The track - "You Were The One" - was co-written by David Cassidy and Tony Romeo who wrote many of the most popular songs for Cassidy and The Partridge Family in the 1970s, including I Think I Love You, "Summer Days", "I Am A Clown" and "Sing Me".

**d6: I Think I Love You**

- [d6s0] "I Think I Love You" is a song composed by songwriter Tony Romeo in 1970.
- [d6s1]  It was released as the debut single by The Partridge Family pop group, featuring David Cassidy on lead vocals and Shirley Jones on background vocals.
- [d6s2]  The Partridge Family version was a number-one hit on the "Billboard" Hot 100 in November 1970.
- [d6s3]  The alternative rock band Voice of the Beehive scored a hit cover version of their own in 1991.
- [d6s4]  There have also been many other cover versions of this song, most notably, Perry Como, Kaci, Katie Cassidy, Paul Westerberg, Constantine Maroulis, and the new "In Search of the Partridge Family" cast on VH1.

**d7: Shirley Jones**

- [d7s0] Shirley Mae Jones (born March 31, 1934) is an American singer and actress of stage, film and television.
- [d7s1]  In her six decades of show business, she has starred as wholesome characters in a number of well-known musical films, such as "Oklahoma!
- [d7s2] " (1955), "Carousel" (1956), and "The Music Man" (1962).
- [d7s3]  She won the Academy Award for Best Supporting Actress for playing a vengeful prostitute in "Elmer Gantry" (1960).
- [d7s4]  She played the lead role of Shirley Partridge, the widowed mother of five children, in the musical situation-comedy television series "The Partridge Family" (1970–74), which co-starred her real-life stepson David Cassidy, son of Jack Cassidy.

**d8: A Partridge Family Christmas Card**

- [d8s0] A Partridge Family Christmas Card was originally released as a vinyl album of Christmas music in 1971.
- [d8s1]  The case of the album contains a reproduction of a Christmas card that was signed by the whole Partridge Family, the stars of a 1970s sitcom.
- [d8s2]  The song "My Christmas Card to You" was original, but the remainder of the tracks were standards.
- [d8s3]  Like most of the Partridge Family songs, the lead vocals are sung by David Cassidy, who played Keith Partridge in the show.
- [d8s4]  The album also features one of the few Partridge Family recordings featuring Shirley Jones as the lead singer ("The Christmas Song").

**d9: Greatest Hits (Partridge Family album)**

- [d9s0] The Partridge Family's Greatest Hits album was issued by Arista in 1989.
- [d9s1]  It was never released on vinyl, only on cassette and compact disc, and is the first Partridge Family album to ever be released on CD.
- [d9s2]  It contains 16 songs, including the TV show's second theme song, "Come on Get Happy" which was never featured on a Partridge family album, and two songs by David Cassidy as a solo act: "Cherish" and "Could It Be Forever".
- [d9s3]  It has liner notes by Danny Bonaduce and a Partridge Family trivia quiz.
- [d9s4]  The cover has a picture of a period lunchbox with a cartoon picture of the family in red velvet suits.

**d10: The Partridge Family**

- [d10s0] The Partridge Family is an American musical-sitcom starring Shirley Jones and featuring David Cassidy.
- [d10s1]  Jones played a widowed mother, and Cassidy played the oldest of her five children who embarked on a music career.
- [d10s2]  It ran from September 25, 1970, until March 23, 1974, on the ABC network as part of a Friday-night lineup, and had subsequent runs in syndication.
- [d10s3]  The family was loosely based on the real-life musical family The Cowsills, a popular band in the late 1960s and early 1970s.

## 12. hotpotqa_5ae0b79355429945ae95943c

原位置：`train` 第 222 题 · 全局第 222 题 · `sample_id: hotpotqa_5ae0b79355429945ae95943c`

Question: Which star of The move The Founder was born on June 26, 1970 ?

Note: 保留新拆法，重构标签

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留演员→出生日期筛选顺序；u1 标注候选演员集合，不在生日证据到达前只标 Nick Offerman。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | stars of The Founder listed in the context | False | [] | Michael Keaton; Nick Offerman; John Carroll Lynch | [["d3s1", "d3s2"]] | context |
| u2 | star of The Founder born on June 26, 1970 | True | ["u1"] | Nick Offerman | [["d6s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | person born on June 26, 1970 | False | [] | Nick Offerman | [['d6s0']] |
| u2 | star of the movie The Founder who was born on June 26, 1970, given {u1} | True | ['u1'] | Nick Offerman | [['d3s2']] |

### Source documents (reference only)

**d1: Mary Louise Rhodes**

- [d1s0] Mary Louise Rhodes (April 5, 1916 – June 26, 1987) was a petroleum geologist in the United States.
- [d1s1]  Rhodes was born April 5, 1916 in Clinton, Missouri.
- [d1s2]  She achieved a bachelor’s degree (1938) and a master’s degree (1939) in Geology at the University of Missouri.
- [d1s3]  In 1942, Rhodes started her professional career in the production department at the Standard Oil Company of Texas (SOTEX), where she examined well samples, constructed sample logs, and prepared subservience maps and cross-sections.
- [d1s4]  Later she transferred to the exploration department in 1946, she continued to work in this department for the rest of her career.
- [d1s5]  Her duties in this department mainly included travelling the world to collect soil samples and collect to find oil reserves.
- [d1s6]  Throughout her professional career, Rhodes became well-known as a carbonate stratigrapher and an expert on several of the Permian basin rock units.
- [d1s7]  Rhodes died in June 26, 1987 from cancer in Midland, Texas.

**d2: Coney Island Cyclone**

- [d2s0] The Coney Island Cyclone (better known as simply the Cyclone) is a historic wooden roller coaster that opened on June 26, 1927, in the Coney Island section of Brooklyn, New York City.
- [d2s1]  On June 18, 1975, Dewey and Jerome Albert – owners of Astroland Park – entered into an agreement with New York City to operate the ride.
- [d2s2]  Despite original plans by the city to scrap the ride in the early 1970s, the roller coaster was refurbished in the 1974 off-season and reopened on July 3, 1975.
- [d2s3]  Astroland Park continued to invest millions over the years in the upkeep of the Cyclone.
- [d2s4]  After Astroland closed in 2008, Carol Hill Albert, president of Cyclone Coasters, continued to operate it under a lease agreement with the city.
- [d2s5]  In 2011, Luna Park took over operation of the Cyclone.
- [d2s6]  It was declared a New York City landmark on July 12, 1988, and was placed on the National Register of Historic Places on June 26, 1991.

**d3: The Founder**

- [d3s0] The Founder is a 2016 American biographical drama film directed by John Lee Hancock and written by Robert Siegel.
- [d3s1]  The film stars Michael Keaton as businessman Ray Kroc, and portrays the story of his creation of the McDonald's fast food chain.
- [d3s2]  Nick Offerman and John Carroll Lynch co-star as McDonald's founders Richard and Maurice McDonald.

**d4: Frank Ronzio**

- [d4s0] Frank Ronzio (June 26, 1920 – January 19, 1989) was an American actor famous for playing 'Litmus' in the film "Escape from Alcatraz".
- [d4s1]  Ronzio was born in Rhode Island on June 26, 1920.
- [d4s2]  He played only ten roles in his life.
- [d4s3]  He also acted in "Hill Street Blues" and "Fear City".
- [d4s4]  He died in Los Angeles on January 19, 1989, at age 68.

**d5: Nick Coleman (columnist)**

- [d5s0] Nicholas J. (Nick) Coleman (born June 26, 1950 in Saint Paul, Minnesota) is a blogger and former Minnesota journalist and columnist for the "Star Tribune", the daily newspaper published in Minneapolis, Minnesota and the St. Paul Pioneer Press.
- [d5s1]  Coleman had two stints at the "Star Tribune", having begun his career there in 1973.
- [d5s2]  In 1986, Coleman left the "Star Tribune" and became a news columnist at the "St. Paul Pioneer Press".
- [d5s3]  Coleman was with the "Pioneer Press" until leaving in 2003, when he then returned to the "Star Tribune" in 2003 as a Metro News columnist, staying until 2009.

**d6: Nick Offerman**

- [d6s0] Nicholas "Nick" Offerman (born June 26, 1970) is an American actor, voice actor, producer, writer, comedian and carpenter widely known for his breakout role as Ron Swanson in the acclaimed NBC sitcom "Parks and Recreation", for which he received the Television Critics Association Award for Individual Achievement in Comedy.
- [d6s1]  His first major television role since the end of "Parks and Recreation" was his role as Karl Weathers in the FX series "Fargo", for which he received a Critics' Choice Television Award nomination for Best Supporting Actor in a Movie/Miniseries and Gavin in the Ice Age franchise.

**d7: Jeff Winkless**

- [d7s0] Jeffrey Alan Winkless (June 2, 1941 – June 26, 2006) was an American film and voice actor and music composer.
- [d7s1]  He was born in Springfield, Massachusetts.
- [d7s2]  Two of his younger brothers, Terence H. Winkless and Daniel Owen Winkless, worked with him on "The Banana Splits Adventure Hour".
- [d7s3]  He was also credited as Jeffrey Brock.
- [d7s4]  He has done voice-overs for several anime titles including "Doomed Megalopolis", "Space Adventure Cobra", "Vampire Hunter D", "Crying Freeman" and "Lily C.A.T.".
- [d7s5]  Winkless died of a brain tumor on June 26, 2006, 24 days after his 65th birthday.
- [d7s6]  He is survived by his three brothers and his wife Rayonelle Baldwin.

**d8: 4 Way Street**

- [d8s0] 4 Way Street is the third album by Crosby, Stills & Nash, their second as Crosby, Stills, Nash & Young, and their first live album.
- [d8s1]  It was originally released as Atlantic Records SD-2-902, shipping as a gold record and peaking at #1 on the "Billboard" 200.
- [d8s2]  A document of their tour from the previous year, the live recordings presented were taken from shows at the Fillmore East (New York, New York) on June 2 through June 7, 1970; The Forum (Los Angeles, California) on June 26 through June 28, 1970; and the Auditorium Theatre (Chicago, Illinois) on July 5, 1970.

**d9: William Apap**

- [d9s0] William "Willie" Apap (June 26, 1918 – February 3, 1970) was a Maltese artist.
- [d9s1]  He was born in Valletta, Malta, on the June 26, 1918.
- [d9s2]  He was the youngest member of a family that included the sculptor Vincent Apap and musician Joseph Apap.

**d10: Byron Looper**

- [d10s0] Byron (Low Tax) Looper, born Byron Anthony Looper (September 15, 1964 – June 26, 2013), was a Republican politician in Tennessee.
- [d10s1]  In order to advance his political career, he legally changed his middle name from "Anthony" to "(Low Tax)".
- [d10s2]  After being convicted for the October 1998 murder of his election opponent, incumbent Tennessee State Senator Tommy Burks, he was given a life sentence in prison.
- [d10s3]  He died in Morgan County Correctional Complex on June 26, 2013.

## 13. hotpotqa_5ae0bf2955429906c02dab1f

原位置：`train` 第 223 题 · 全局第 223 题 · `sample_id: hotpotqa_5ae0bf2955429906c02dab1f`

Question: Which band was formed first, Radiohead or My Morning Jacket?

Note: 

Type: comparison · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | year Radiohead was formed | False | [] | 1985 | [["d8s0"]] | context |
| u2 | year My Morning Jacket was formed | False | [] | 1998 | [["d3s0"]] | context |
| u3 | which band was formed first | True | ["u1", "u2"] | Radiohead | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | year Radiohead was formed | False | [] | 1985 | [['d8s0']] |
| u2 | year My Morning Jacket was formed | False | [] | 1998 | [['d3s0']] |
| u3 | which of Radiohead and My Morning Jacket was formed first | True | ['u1', 'u2'] | Radiohead | [[]] |

### Source documents (reference only)

**d1: Wayne Robbins and The Hellsayers**

- [d1s0] Wayne Robbins and The Hellsayers is a psychedelic-folk-rock band based in Asheville, North Carolina.
- [d1s1]  The band is Wayne Robbins (vocals and guitars, and principal songwriter), Jeff Whitworth (lap steel, guitars, banjo), Jonas Cole (guitars and keys), Erich Hubner (bass) and Josh Carpenter (drums).
- [d1s2]  Their first album, "The Lonesome Sea", was released on De'll Orso Records in London to critical acclaim ("Uncut" magazine gave it four stars), and it was independently released by the band in the U.S.
- [d1s3]  The band completed a successful tour of Europe in May 2007 in support of Band of Horses, playing gigs at such high-profile venues as Scala in London, Vera in Groningen, and Tivoli in Utrecht.
- [d1s4]  The Hellsayers have shared the stage with Band of Horses, My Morning Jacket, Smog, Magnolia Electric Company, Chris Robinson (Black Crowes), Tyler Ramsey, Apples in Stereo, The Long Winters, Oakley Hall, Dalek, Deerhunter, Bloodkin, Hopewell, The High Dials, Benji Hughes, Summer Hymns, The Houstons, Wooden Birds (American Analog Set), Drug Money, and many more.
- [d1s5]  In October 2009, the band recorded a 4 song EP (tentatively titled "Banana Shark") with producer Brent Rademaker (of Beachwood Sparks) at Rademaker's home studio in Tampa, FL.
- [d1s6]  The Hellsayers are currently shopping their finished second album, "All You Need To Sleep," (co-produced by Wayne Robbins and Morgan Kraft) to labels in the U.S.

**d2: My Morning Jacket Does Xmas Fiasco Style**

- [d2s0] My Morning Jacket Does Xmas Fiasco Style is a 2000 EP by the rock band My Morning Jacket, containing Christmas songs.
- [d2s1]  Its alternate title is We Wish You a Merry Christmas and a Happy New Year!

**d3: My Morning Jacket**

- [d3s0] My Morning Jacket is an American rock band formed in Louisville, Kentucky in 1998.
- [d3s1]  The band currently consists of vocalist/guitarist Jim James, bassist Tom Blankenship, drummer Patrick Hallahan, guitarist Carl Broemel, and keyboardist Bo Koster.
- [d3s2]  The band's sound, rooted in rock and country, is often experimental and psychedelic.
- [d3s3]  The group amassed a following beginning in the 2000s in part due to their live performances.

**d4: The Waterfall (album)**

- [d4s0] The Waterfall is the seventh studio album by American rock band My Morning Jacket.
- [d4s1]  Produced by Tucker Martine and group frontman Jim James, the album was released on May 4, 2015 by ATO Records and Capitol Records.
- [d4s2]  My Morning Jacket rose to prominence in the 2000s with a string of acclaimed albums and praised live performances.
- [d4s3]  Its sixth album, "Circuital" (2011), was equally well received.
- [d4s4]  The band toured in support of it for two years before taking a break.
- [d4s5]  They regrouped in late 2013 to begin work on "The Waterfall", a process which took eighteen months.

**d5: Dead Confederate**

- [d5s0] Dead Confederate is an American alternative rock band formed in Augusta, Georgia and based in Athens, Georgia.
- [d5s1]  The band's sound has been described as a mix of alternative country, psychedelic rock and grunge, and has drawn comparisons to Nirvana and My Morning Jacket.

**d6: Okonokos**

- [d6s0] Okonokos is a live album and concert film by the American band My Morning Jacket released on October 31, 2006.
- [d6s1]  The album was recorded during the band's fall 2005 Z Tour, over two nights at The Fillmore in San Francisco, California.
- [d6s2]  This is the first My Morning Jacket album for which frontman Jim James does not receive a production credit; he is credited for "concept/story".

**d7: My Morning Jacket discography**

- [d7s0] The discography of American indie rock band My Morning Jacket, consists of seven studio albums, 11 extended plays, 14 singles, four music videos, three compilation albums, four live albums and one video album.
- [d7s1]  The band signed with independent Darla Records in 1998 before moving to ATO in 2003.
- [d7s2]  James explained that "At the time, My Morning Jacket was just me and an acoustic guitar in my bedroom, I'd been sending cassette tapes out [and] our first record label, I wrote them a love letter, pretending Darla was a girl that I wanted to woo'.

**d8: Radiohead**

- [d8s0] Radiohead are an English rock band from Abingdon, Oxfordshire, formed in 1985.
- [d8s1]  The band consists of Thom Yorke (lead vocals, guitar, piano, keyboards), Jonny Greenwood (lead guitar, keyboards, other instruments), Ed O'Brien (guitar, backing vocals), Colin Greenwood (bass), and Phil Selway (drums, percussion, backing vocals).
- [d8s2]  They have worked with producer Nigel Godrich and cover artist Stanley Donwood since 1994.

**d9: The Romany Rye (band)**

- [d9s0] The Romany Rye is a band formed by Luke MacMaster, former guitarist of The Colour.
- [d9s1]  Their first album, "Highway 1, Looking Back Carefully", was released on October 5, 2009 with a track listing of eight songs.
- [d9s2]  The band could be categorized as indie folk-rock and draws comparisons to the likes of Neil Young, My Morning Jacket, Ryan Adams & The Cardinals, and many others.
- [d9s3]  Kings of Leon guitarist Matthew Followill, whose band has its early roots in country rock, dubbed them a band to watch in 2010.
- [d9s4]  On January 3, 2012, they released their second album, "Quicksilver Sunbeam".

**d10: Tom Blankenship**

- [d10s0] Tom Blankenship is an American rock musician.
- [d10s1]  He currently plays bass guitar for the Louisville, Kentucky band My Morning Jacket.
- [d10s2]  In 2012, Blankenship wrote an article on My Morning Jacket, discussing the band and growing up in Louisville, for the July issue of "Louisville Magazine".

## 14. hotpotqa_5ae130515542997b2ef7d121

原位置：`train` 第 224 题 · 全局第 224 题 · `sample_id: hotpotqa_5ae130515542997b2ef7d121`

Question: These happy Golden Years was written by what American writer known for her series of children's books that were released from 1932 to 1943?

Note: 

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | American writer known for her series of children's books released from 1932 to 1943 | False | [] | Laura Ingalls Wilder | [["d2s0"]] | context |
| u2 | author of "These happy Golden Years", given {u1} | True | ["u1"] | Laura Ingalls Wilder | [["d9s0"], ["d10s0", "d10s1"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | author of These Happy Golden Years | False | [] | Laura Ingalls Wilder | [['d9s0'], ['d10s0', 'd10s1']] |
| u2 | American writer known for a series of children's books released from 1932 to 1943, given {u1} | True | ['u1'] | Laura Ingalls Wilder | [['d2s0']] |

### Source documents (reference only)

**d1: Revue**

- [d1s0] A revue (from French 'magazine' or 'overview') is a type of multi-act popular theatrical entertainment that combines music, dance, and sketches.
- [d1s1]  The revue has its roots in 19th century popular entertainment and melodrama but grew into a substantial cultural presence of its own during its golden years from 1916 to 1932.
- [d1s2]  Though most famous for their visual spectacle, revues frequently satirized contemporary figures, news or literature.
- [d1s3]  Similar to the related subforms of operetta and musical theatre, the revue art form brings together music, dance and sketches to create a compelling show.
- [d1s4]  In contrast to these, however, revue does not have an overarching storyline.
- [d1s5]  Rather, a general theme serves as the motto for a loosely-related series of acts that alternate between solo performances and dance ensembles.

**d2: Laura Ingalls Wilder**

- [d2s0] Laura Ingalls Wilder ( ; February 7, 1867 – February 10, 1957) was an American writer known for the "Little House on the Prairie" series of children's books released from 1932 to 1943 which were based on her childhood in a settler and pioneer family.

**d3: Kate Klise**

- [d3s0] Catherine "Kate" Klise (born April 13 in 1963) is an American writer known for children's fiction.
- [d3s1]  Many of her books are illustrated by her sister, M. Sarah Klise.
- [d3s2]  Their popular "Regarding" series is presented in a scrapbook format, with letters, journal entries, and related ephemera telling the story.
- [d3s3]  She is also known for her picture books as well as the bestselling 43 Old Cemetery Road series.
- [d3s4]  Klise's first adult novel, "In the Bag", was released in 2012.
- [d3s5]  She is a contributor to "The Huffington Post".

**d4: Stephen R. Lawhead**

- [d4s0] Stephen R. Lawhead, born (1950--) 2 1950 (age 67 ) , is a UK–based American writer known for his works of fantasy, science fiction, and historical fiction, particularly Celtic historical fiction.
- [d4s1]  He has written over 28 novels and numerous children's and non-fiction books.

**d5: Jennifer Jones**

- [d5s0] Jennifer Jones (born Phylis Lee Isley; March 2, 1919 – December 17, 2009), also known as Jennifer Jones Simon, was an American actress during Hollywood's golden years.
- [d5s1]  Jones, who won the Academy Award for Best Actress for her performance in "The Song of Bernadette" (1943), was also Academy Award-nominated for her performances in four other films.
- [d5s2]  She was married three times, most notably to film producer David O. Selznick.

**d6: Debra Evans**

- [d6s0] Debra Evans (born 1953) is an American writer known for her books on issues related to contemporary Christian spirituality, reproductive health, women's wellness, and family relationships.
- [d6s1]  She has written over 22 non-fiction books.

**d7: Judy Blume**

- [d7s0] Judy Blume (born Judith Sussman; February 12, 1938) is an American writer known for children's and young adult (YA) fiction.
- [d7s1]  Some of her best known works are "Are You There God?
- [d7s2]  It's Me, Margaret" (1970), "Tales of a Fourth Grade Nothing" (1972), "Deenie" (1973), and "Blubber" (1974).
- [d7s3]  "The New Yorker" has called her books "talismans that, for a significant segment of the American female population, marked the passage from childhood to adolescence."

**d8: Victor Milan**

- [d8s0] Victor Woodward Milán (born 1954 in Tulsa, Oklahoma) is an American writer known for libertarian science fiction and an interest in cybernetics.
- [d8s1]  In 1986 he won the Prometheus Award for "Cybernetic Samurai".
- [d8s2]  He has also written several shared universe works for the Forgotten Realms, "Star Trek", and Wild Cards Universes.
- [d8s3]  He has also written books under the pseudonyms Richard Austin (Jove Books "The Guardians" series), Robert Baron (Jove Books "Stormrider" series), and S. L. Hunter ("Steele" series with Simon Hawke, who used the pen name J. D. Masters).
- [d8s4]  He also wrote at least 9 novels under the "house name" of James Axler for the Harlequin Press/Gold Eagle Books "Deathlands" and "Outlanders" series.
- [d8s5]  He has published almost 100 novels and numerous short stories.

**d9: These Happy Golden Years**

- [d9s0] These Happy Golden Years is an autobiographical children's novel written by Laura Ingalls Wilder and published in 1943, the eighth of nine books in her "Little House" series – although it originally ended it.
- [d9s1]  It is based on her later adolescence near De Smet, South Dakota, featuring her short time as a teacher, beginning at age 15, and her courtship with Almanzo Wilder.
- [d9s2]  It spans the time period from 1882 to 1885, when they marry.

**d10: List of Little House on the Prairie books**

- [d10s0] The original Little House books were a series of eight autobiographical children's novels written by Laura Ingalls Wilder and published by Harper & Brothers from 1932 to 1943.
- [d10s1]  The eighth book, "These Happy Golden Years", featured Laura Ingalls at ages 15 to 18 and was originally published with one page at the end containing the note, "The end of the Little House books."
- [d10s2]  The ninth and last novel written by Ingalls Wilder, "The First Four Years" was published posthumously and unfinished in 1971.
- [d10s3]  Although her intentions are unknown, it is commonly considered part of the Little House series and is included in the 9-volume paperback box set "Little House, Big Adventure" (Harper Trophy, May 1994).

## 15. hotpotqa_5ae13d9d55429920d523433d

原位置：`train` 第 225 题 · 全局第 225 题 · `sample_id: hotpotqa_5ae13d9d55429920d523433d`

Question: Are both Tangshan and Lanxi, Zhejiang from the same province in China?

Note: 

Type: comparison · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | province of Tangshan | False | [] | Hebei | [["d4s0"], ["d5s0"], ["d3s0"], ["d6s0"]] | context |
| u2 | province of Lanxi, Zhejiang | False | [] | Zhejiang | [["d9s0"]] | context |
| u3 | whether Tangshan and Lanxi, Zhejiang are from the same province | True | ["u1", "u2"] | no | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | province in which Tangshan is located | False | [] | Hebei | [['d4s0'], ['d5s0'], ['d3s0'], ['d6s0']] |
| u2 | province in which Lanxi, Zhejiang is located | False | [] | Zhejiang | [['d9s0']] |
| u3 | whether Tangshan and Lanxi, Zhejiang are in the same province of China | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Christianity in Zhejiang**

- [d1s0] Christianity is a minority in Zhejiang province of China.
- [d1s1]  Zhejiang has one of the largest Protestant populations of China.
- [d1s2]  Immaculate Conception Cathedral of Hangzhou is in Zhejiang.
- [d1s3]  Zhejiang has greater religious freedom of Christianity than other parts of the country.
- [d1s4]  There were more than 600 detentions of Christians in the province in 2006.
- [d1s5]  The Shouters are active in the province.

**d2: Tangshan NO.1 high school**

- [d2s0] Tangshan No.1 High School (, pinyin: Tángshān shì dìyī zhōngxué), commonly abbreviated as Tangshan Yizhong (), is a highly prestigious public in Hebei province, China.
- [d2s1]  It was established in 1902 by the Yong Ping Government (Tangshan Government) during the Qing Dynasty, known as the Yong Ping Zhongli High School.

**d3: North China University of Science and Technology**

- [d3s0] North China University of Science and Technology is a university in Tangshan City, Hebei Province, People's Republic of China.
- [d3s1] North China University of Science and Technology, located in Tangshan the most promising city at the center of Bohai Bay Rim, is one of the ten key universities of Hebei Province, China.
- [d3s2]  It is a comprehensive university taking engineering and medicine as the backbone and pursuing a harmonious development of engineering, medicine, sciences, economics, management, law and humanities.
- [d3s3]  Education programs are provided for masters, bachelors, international students and adult students.

**d4: Tangshan**

- [d4s0] Tangshan () is a largely industrial prefecture-level city in northeastern Hebei province, China.
- [d4s1]  It has become known for the 1976 Tangshan earthquake which measured 7.8 on the Richter scale, flattening much of the city and killing at least 255,000 residents according to official estimates.
- [d4s2]  The city has since been rebuilt, has become a tourist attraction and has among the 10 largest ports in China.

**d5: Tangshan Sannühe Airport**

- [d5s0] Tangshan Sannühe Airport () (IATA: TVS, ICAO: ZBTS) , or Tangshan Air Base, is a dual-use military and civil airport serving the city of Tangshan in Hebei Province, China.
- [d5s1]  It is located near the village of Sannühe, 20 kilometers from the city center in Fengrun District.
- [d5s2]  The airport was opened on 13 July 2010.

**d6: CRRC Tangshan**

- [d6s0] CRRC Tangshan Co., Ltd. (), is a manufacturer of rolling stock located in Tangshan, Hebei province, People's Republic of China.
- [d6s1]  While Datong built mainline steam locomotives until 1988, Tangshan built steam for industrial use until 1999, becoming the last works in the world to build steam for non-tourist use.

**d7: Jinhua**

- [d7s0]    , is a prefecture-level city in central Zhejiang province in eastern China.
- [d7s1]  It borders the provincial capital of Hangzhou to the northwest, Quzhou to the southwest, Lishui to the south, Taizhou to the east, and Shaoxing to the northeast.
- [d7s2]  Its population was 5,361,572 at the 2010 census including 1,077,245 in the built-up area made of two urban districts (not including the satellite city of Lanxi, which has become essentially a suburban offshoot of Jinhua's main urban area).

**d8: Yutian County, Hebei**

- [d8s0] Yutian () is a county of northeastern Hebei province, China, and is under the administration of the prefecture-level city of Tangshan, bordering Tianjin to the north and west.
- [d8s1]  It is located approximately 55 km northwest of Tangshan and 110 km east of Beijing, lying on China National Highway 102.
- [d8s2]  It has an area of 1,165 km² and a population of 650,000 .

**d9: Lanxi, Zhejiang**

- [d9s0] Lanxi also known as Lanchi () is a county-level city under the administration of the prefecture-level city Jinhua in Zhejiang Province, China.

**d10: Huangdian, Zhejiang**

- [d10s0] Huangdian () is a town under the administration of Lanxi City in western Zhejiang province, China, located 10 km northwest of downtown Lanxi.
- [d10s1]  , it has 46 villages under its administration.

## 16. hotpotqa_5ae143aa55429920d523435d

原位置：`train` 第 226 题 · 全局第 226 题 · `sample_id: hotpotqa_5ae143aa55429920d523435d`

Question: Are the bands Skunk Anansie and Anberlin from the same country?

Note: 

Type: comparison · fallback: False · SFT snapshots: 6

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | country of Skunk Anansie | False | [] | United Kingdom | [["d1s0"], ["d6s0"], ["d2s0"]] | context |
| u2 | country of Anberlin | False | [] | United States | [["d5s0"]] | context |
| u3 | whether Skunk Anansie and Anberlin are from the same country | True | ["u1", "u2"] | no | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country Skunk Anansie is from | False | [] | United Kingdom | [['d1s0'], ['d6s0'], ['d2s0']] |
| u2 | country Anberlin is from | False | [] | United States | [['d5s0']] |
| u3 | whether Skunk Anansie and Anberlin are from the same country | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Skunk Anansie**

- [d1s0] Skunk Anansie are a British rock band whose members include Skin (lead vocals, guitar), Cass (guitar, bass, backing vocals), Ace (guitar, backing vocals) and Mark Richardson (drums and percussion).

**d2: Skunk Anansie discography**

- [d2s0] The discography of Skunk Anansie, an English rock band, consists of six studio albums and twenty-four singles, including one re-issue.
- [d2s1]  The band's members include Skin (Deborah Dyer), Cass (Richard Lewis), Ace (Martin Kent) and Mark Richardson.
- [d2s2]  The group formed in 1994 and disbanded in 2001; they re-united in 2009.
- [d2s3]  Skunk Anansie are named after the West African folk tales of Anansi the Spider-man, with "Skunk" added to "make the name nastier".

**d3: Andy Wallace (producer)**

- [d3s0] Andy Wallace is an American music studio engineer with a long track record of successful productions, beginning with the 1986 production of the Run-DMC/Aerosmith collaboration on "Walk This Way" with Rick Rubin.
- [d3s1]  Following this breakout success, Wallace went on to work with Feeder, Sum 41, The Cult, Slayer, Prince, Bruce Springsteen, Sepultura, Soulfly, Nirvana, The Misfits, White Zombie, Jeff Buckley, Ben Folds Five, Faith No More, Rollins Band, Rush, Alice Cooper, Bernard Butler, Bad Religion, Sonic Youth, L7, Guns N' Roses, Rage Against the Machine, Front 242, Alabama 3, Linkin Park, Trapt, Foo Fighters, Silverchair, At the Drive-In, Staind, Sevendust, Blind Melon, System of a Down, Phish, Skunk Anansie, A Perfect Circle, Limp Bizkit, 3 Doors Down, Fuel, Chevelle, Disturbed, Paul McCartney, The Cribs, Atreyu, Young Astronauts Club, Avenged Sevenfold, Dream Theater, Ghost (Swedish band), A Day to Remember and many others.
- [d3s2]  As of October 2005, over 80 million album units had been sold worldwide that contained a credit to Andy Wallace.

**d4: Selling Jesus**

- [d4s0] "Selling Jesus" is a song by Skunk Anansie, released as their debut single.
- [d4s1]  Although Skunk Anansie previously released "Little Baby Swastikkka" as a limited release, it was not regarded as an actual single.
- [d4s2]  "Selling Jesus" is a song in protest of religion and politics, and in particular Christianity.
- [d4s3]  The single is taken from their debut album, "Paranoid & Sunburnt", and reached number 46 on the UK Singles Chart.
- [d4s4]  Three added B-Sides were included on the CD release, with track 4 'Skunk Song' being written by Ace, R. France, C. Lewis and Skin.
- [d4s5]  The title song was also included on the soundtrack to the motion picture "Strange Days".

**d5: Anberlin**

- [d5s0] Anberlin was an American alternative rock band formed in Winter Haven, Florida in 1998 and disbanded in 2014.
- [d5s1]  Since the beginning of 2007, the band consisted of lead vocalist Stephen Christian, guitarists Joseph Milligan and Christian McAlhaney, bassist Deon Rexroat, and drummer Nathan Young.

**d6: Hedonism (Just Because You Feel Good)**

- [d6s0] "Hedonism (Just Because You Feel Good)" is a song by British group Skunk Anansie.
- [d6s1]  It was released in January 1997 as a single from their second album, "Stoosh".
- [d6s2]  The song reached #14 in the UK singles chart.
- [d6s3]  It also proved to be a top 20 hit in several countries such as France, Sweden and Austria and a top 10 hit in other countries such as Norway and The Netherlands and a #2 hit in Switzerland.
- [d6s4]  It is regarded as one of Skunk Anansie's most known singles and was a popular choice at concerts.
- [d6s5]  Skin performs a version of the song at many of her solo gigs, and US R&B group Groove Theory covered the song for their second album, "The Answer".

**d7: Brazen (Weep)**

- [d7s0] "Brazen (Weep)" is the fourth and final single from Skunk Anansie's second album, "Stoosh".
- [d7s1]  It was released in June 1997 and reached #11 in the UK Singles Chart.
- [d7s2]  That made the song to the band's most successful song in their home country, even more successful than their commercially biggest hit Hedonism (Just Because You Feel Good), which reached #13.
- [d7s3]  Three versions of the single were released.
- [d7s4]  CD2 and CD3 were remix CDs.

**d8: Primary (band)**

- [d8s0] Primary were an Australian techno rock band which formed in 1995 the Fonti brothers: Jamie on keyboards and Sean on bass guitar (both ex-Caligula), and Connie Mitchell on lead vocals.
- [d8s1]  According to Australian musicologist, Ian McFarlane, the group were "Dominated by South African-born [Mitchell]'s hyperactive and full-frontal vocals, with thunderous electronic rock underpinning the music, Primary sounded like a techno Skunk Anansie.
- [d8s2]  Jamie Fonti coined the phrase 'Hybrid Electronica Rock' in order to describe the band's sound."
- [d8s3]  The group released two albums, "This Is the Sound" (June 1999) and "Watching the World" (28 May 2001).
- [d8s4]  They disbanded late in 2003.

**d9: Skin discography**

- [d9s0] Skin is the lead singer of Skunk Anansie and a solo artist.
- [d9s1]  She has released two albums as a solo artist and featured on several other artists albums.
- [d9s2]  For Skunk Anansie's full discography see Skunk Anansie discography.

**d10: Weak (Skunk Anansie song)**

- [d10s0] "Weak" is a song by Skunk Anansie, released as their fourth single.
- [d10s1]  It was the last release to be taken from their debut album "Paranoid & Sunburnt".
- [d10s2]  The song is one of Skunk Anansie's well known releases, and often a favourite at festivals.
- [d10s3]  Skin performs a slower, more ballad-like version at many of her solo gigs.
- [d10s4]  The song has also been covered by Rod Stewart on his 1998 album "When We Were the New Boys".

## 17. hotpotqa_5ae176ef5542990adbacf79d

原位置：`train` 第 227 题 · 全局第 227 题 · `sample_id: hotpotqa_5ae176ef5542990adbacf79d`

Question: Are Nagisa Oshima and David Hewlett of the same nationality?

Note: 

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | nationality of Nagisa Oshima | False | [] | Japanese | [["d4s0"]] | context |
| u2 | nationality of David Hewlett | False | [] | Canadian | [["d2s0"]] | context |
| u3 | whether Nagisa Oshima and David Hewlett are of the same nationality | True | ["u1", "u2"] | no | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | nationality of Nagisa Oshima | False | [] | Japanese | [['d4s0']] |
| u2 | nationality of David Hewlett | False | [] | Canadian | [['d2s0']] |
| u3 | whether Nagisa Oshima and David Hewlett are of the same nationality | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Tomoyo Oshima**

- [d1s0] Tomoyo Oshima (大島 ともよ , Ōshima Tomoyo , born 1949 Akita, Japan) is a Japanese film editor, known as editor of Nagisa Oshima's and Shuji Terayama's films in her young days.
- [d1s1]  She is the director of Tokyo Filmex, a film festival.

**d2: David Hewlett**

- [d2s0] David Ian Hewlett (born 18 April 1968) is an English-born Canadian actor, writer, director, and voice actor best known for his role as Dr. Rodney McKay on the Canadian-American science fiction TV shows "Stargate SG-1", "Stargate Atlantis" and "Stargate Universe".
- [d2s1]  Younger television viewers may know him best from his two 1993 guest appearances on "Shining Time Station", portraying nosy journalist Ted Typo.

**d3: Forbidden Colours**

- [d3s0] "Forbidden Colours" is a 1983 song by David Sylvian and Ryuichi Sakamoto.
- [d3s1]  The song is the vocal version of the theme from the Nagisa Oshima film "Merry Christmas, Mr. Lawrence" (in certain territories retitled "Furyo").
- [d3s2]  It appears on the film's soundtrack album and was released as a single on Virgin Records in 1983 (the second collaborative single release by Sylvian and Sakamoto, following 1982's "Bamboo Houses").

**d4: Nagisa Oshima**

- [d4s0] Nagisa Oshima (大島 渚 , Ōshima Nagisa , March 31, 1932 – January 15, 2013) was a Japanese film director and screenwriter.
- [d4s1]  His films include "In the Realm of the Senses" (1976), a sexually explicit film set in 1930's Japan, and "Merry Christmas, Mr. Lawrence" (1983), about Japanese WW2 prisoners of war.

**d5: Merry Christmas, Mr. Lawrence**

- [d5s0] Merry Christmas, Mr. Lawrence (Japanese: Senjō no Merī Kurisumasu (戦場のメリークリスマス , "Merry Christmas on the Battlefield") , also known in many European editions as Furyo (俘虜, Japanese for "prisoner of war"), is a 1983 British-Japanese drama film directed by Nagisa Oshima, produced by Jeremy Thomas and starring David Bowie, Tom Conti, Ryuichi Sakamoto, Takeshi Kitano and Jack Thompson.

**d6: Max, Mon Amour**

- [d6s0] Max, Mon Amour a.k.a. Max, My Love is a 1986 film directed by Nagisa Oshima, starring Charlotte Rampling, Anthony Higgins, Victoria Abril, Pierre Étaix and Milena Vukotic.
- [d6s1]  The screenplay was written by Oshima and Jean-Claude Carrière, and the film was produced by Serge Silberman.

**d7: Fumio Watanabe**

- [d7s0] Fumio Watanabe (渡辺文雄 , Watanabe Fumio , October 31, 1929 – August 4, 2004) was a Japanese actor most known for his work with Japanese New Wave director Nagisa Oshima.
- [d7s1]  He was born in Tokyo and graduated from the University of Tokyo before joining the Shōchiku studio in 1956.

**d8: The Seed and the Sower**

- [d8s0] The Seed and the Sower is a book by South African writer Laurens van der Post, consisting of three interrelated stories blended into a novel, first published in 1963.
- [d8s1]  The novel was filmed in 1983 as "Merry Christmas Mr. Lawrence", directed by Nagisa Oshima and starring David Bowie, Tom Conti, Ryuichi Sakamoto and Takeshi Kitano.

**d9: Kei Satō**

- [d9s0] Kei Satō (佐藤 慶 , Satō Kei ) was a Japanese character actor and narrator.
- [d9s1]  He was born in Aizu.
- [d9s2]  He is known for his work with Japanese New Wave director Nagisa Oshima, and for several films with Kaneto Shindo, such as "Onibaba" and "Kuroneko".
- [d9s3]  He won the best actor award from "Kinema Junpo" for the films "The Ceremony" and "Nihon no akuryō".
- [d9s4]  He also worked as a narrator for many documentaries, both on television and film.

**d10: Cruel Story of Youth**

- [d10s0] Cruel Story of Youth (青春残酷物語 , Seishun Zankoku Monogatari ) is a 1960 Japanese film directed by Nagisa Oshima, starring Yusuke Kawazu and Miyuki Kuwano as teenage delinquents and lovers.
- [d10s1]  It is Oshima's second feature film and is known for its elements of French "nouvelle vague".
- [d10s2]  The film won the 1960 Blue Ribbon Awards for Best Newcomer for Oshima.

## 18. hotpotqa_5ae1af93554299492dc91b69

原位置：`train` 第 228 题 · 全局第 228 题 · `sample_id: hotpotqa_5ae1af93554299492dc91b69`

Question: are Horia Tecău and Heinz Günthardt nationals of the same country ?

Note: 

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | nationality of Horia Tecău | False | [] | Romanian | [["d5s0"]] | context |
| u2 | nationality of Heinz Günthardt | False | [] | Swiss | [["d10s0"]] | context |
| u3 | whether Horia Tecău and Heinz Günthardt are nationals of the same country | True | ["u1", "u2"] | no | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | nationality of Horia Tecău | False | [] | Romanian | [['d5s0']] |
| u2 | nationality of Heinz Günthardt | False | [] | Swiss | [['d10s0']] |
| u3 | whether Horia Tecău and Heinz Günthardt are nationals of the same country | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: 2009 Zenith Tennis Cup – Doubles**

- [d1s0] Yves Allegro and Horia Tecău were the defending champions, however Tecău chose to not participate.

**d2: 2010 Pilot Pen Tennis – Men's Doubles**

- [d2s0] Julian Knowle and Jürgen Melzer were the defending champions, but Melzer chose not to participate this year.As a result, Knowle partnered with Andy Ram, but they lost to Robert Lindstedt and Horia Tecău in the semifinals.
- [d2s1]  Lindstedt and Tecău went on to win the tournament, after defeating Rohan Bopanna and Aisam-ul-Haq Qureshi in the final 6–4, 7–5.

**d3: 2009 Mamaia Challenger – Doubles**

- [d3s0] Florin Mergea and Horia Tecău were the defending champions.
- [d3s1]  Tecău didn't start this year.

**d4: 2012 PBZ Zagreb Indoors – Doubles**

- [d4s0] Dick Norman and Horia Tecău were the defending champions but Tecău chose not to compete and Norman teamed up with James Cerretani.
- [d4s1]  They lost in the first round to Benjamin Becker and Alexander Waske.
- [d4s2] <br>

**d5: Horia Tecău**

- [d5s0] Horia Tecău (] ; born January 19, 1985) is a Romanian tennis player currently ranked World No. 9 in doubles.
- [d5s1]  He turned pro in 2003 and reached the men's doubles finals of the 2010, 2011 and 2012 Wimbledon Championships with Robert Lindstedt before winning it in 2015 with Jean-Julien Rojer, with whom he also won the 2017 US Open.
- [d5s2]  Tecău also won the 2012 Australian Open mixed doubles title with Bethanie Mattek-Sands and the 2015 ATP World Tour Finals with Rojer.

**d6: 1981 Stockholm Open – Doubles**

- [d6s0] Heinz Günthardt and Paul McNamee were the defending champions, but McNamee did not participate this year.
- [d6s1]  Günthardt partnered Balázs Taróczy, losing in the first round.

**d7: 1980 Geneva Open – Doubles**

- [d7s0] Željko Franulović and Balázs Taróczy won the title, defeating Heinz Günthardt and Markus Günthardt 6–4, 4–6, 6–4 in the final.

**d8: 2014 Topshelf Open – Men's Doubles**

- [d8s0] Max Mirnyi and Horia Tecău were the defending champions, but Mirnyi chose not to participate.
- [d8s1]  Tecău played alongside Jean-Julien Rojer and successfully defended the title, defeating Santiago González and Scott Lipsky in the final, 6–3, 7–6.

**d9: 2010 UNICEF Open – Men's Doubles**

- [d9s0] Wesley Moodie and Dick Norman were defending champions, but they lost in the semifinals against Robert Lindstedt and Horia Tecău.
- [d9s1] Lindstedt and Tecău won the final 1–6, 7–5, [10–7] against Lukáš Dlouhý and Leander Paes.

**d10: Heinz Günthardt**

- [d10s0] Heinz Peter Günthardt (born 8 February 1959 in Zürich) is a former tennis player from Switzerland, who won five singles titles during his professional career, including the Rotterdam WCT in 1980.

## 19. hotpotqa_5ae1b052554299492dc91b6b

原位置：`train` 第 229 题 · 全局第 229 题 · `sample_id: hotpotqa_5ae1b052554299492dc91b6b`

Question: Which opera Ernani and Stiffelio.has more acts ?

Note: 

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | number of acts in Ernani | False | [] | four | [["d2s0"]] | context |
| u2 | number of acts in Stiffelio | False | [] | three | [["d8s0"]] | context |
| u3 | which opera has more acts | True | ["u1", "u2"] | Ernani | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | number of acts in the opera Ernani | False | [] | four | [['d2s0']] |
| u2 | number of acts in the opera Stiffelio | False | [] | three | [['d8s0']] |
| u3 | which of the operas Ernani and Stiffelio has more acts | True | ['u1', 'u2'] | Ernani | [[]] |

### Source documents (reference only)

**d1: Carlo Guasco**

- [d1s0] Carlo Guasco (16 March 1813 – 13 December 1876) was a celebrated Italian operatic tenor who sang in Italian and other European opera houses from 1837 to 1853.
- [d1s1]  Although he sang in many world premieres, he is most remembered today for having created the leading tenor roles in Verdi's "I Lombardi alla prima crociata", "Ernani", and "Attila".

**d2: Ernani**

- [d2s0] Ernani is an operatic "dramma lirico" in four acts by Giuseppe Verdi to an Italian libretto by Francesco Maria Piave, based on the play "Hernani" by Victor Hugo.

**d3: Ernani do Nascimento Germano**

- [d3s0] Ernani do Nascimento Germano, better known as Ernani (São João da Barra, 16 July 1982) is a Brazilian footballer, who acts as a steering wheel and side.
- [d3s1]  Currently playing for Juventude.

**d4: Corrado Zambelli**

- [d4s0] Corrado Zambelli (3 June 1897 - 1 September 1974) was an Italian classical bass who had an active international singing career in operas and concerts from the 1920s through the 1950s.
- [d4s1]  He appears on several complete opera recordings, including "Otello" and "Carmen" for His Master's Voice; and "Ernani", "Il trovatore", "La favorite", and "La Gioconda" for Columbia Records.

**d5: Repertoire of Plácido Domingo**

- [d5s0] Spanish tenor Plácido Domingo has officially sung 147 roles in Italian, French, German, English, Spanish and Russian.
- [d5s1]  His main repertoire however is Italian ("Otello", Cavaradossi in "Tosca", "Don Carlo", Des Grieux in "Manon Lescaut", Dick Johnson in "La fanciulla del West", Radames in "Aida"), French ("Faust", "Werther", Don José in "Carmen", Samson in "Samson et Dalila"), and German ("Lohengrin", "Parsifal", and Siegmund in "Die Walküre").
- [d5s2]  Domingo currently continues to add more operas to his repertoire.
- [d5s3]  Since 2009, he has moved substantially into the baritone repertoire, especially focusing on Verdi baritone roles.
- [d5s4]  In 2015, he made his most recent debuts as Macbeth at the Berliner Staatsoper, Don Carlo in "Ernani" at the Metropolitan Opera, and Gianni Schicchi at the Los Angeles Opera.
- [d5s5]  Tim Page, a Pulitzer Prize-winner for music criticism, described Domingo in a 1996 "Washington Post" article as "the most versatile, intelligent and altogether accomplished operatic tenor now before the public."

**d6: Gaetano Mares**

- [d6s0] Gaetano Mares (1793–1862) was an Italian conductor.
- [d6s1]  He notably conducted the world premieres of Giuseppe Verdi's "Ernani" (1844), "Attila (opera)" (1846), "Rigoletto" (1851) and "La traviata" (1853) at La Fenice in Venice.

**d7: Sondra Radvanovsky**

- [d7s0] Sondra Radvanovsky (born April 11, 1969) is an American-Canadian soprano.
- [d7s1]  Specializing in 19th-century Italian opera, Radvanovsky has been called one of the leading Verdi sopranos of her generation.
- [d7s2]  Her signature roles include Elvira in "Ernani", Leonora in "Il trovatore", Elena in "I vespri siciliani", Élisabeth in "Don Carlos", and the title role in "Norma".

**d8: Stiffelio**

- [d8s0] Stiffelio is an opera in three acts by Giuseppe Verdi, from an Italian libretto by Francesco Maria Piave.
- [d8s1]  The origin of this was the novel “Le pasteur d’hommes”, by Émile Souvestre, which was published in 1838.
- [d8s2]  This was adapted into the French play "Le pasteur, ou L'évangile et le foyer" by Émile Souvestre and Eugène Bourgeois.
- [d8s3]  That was in turn translated into Italian by Gaetano Vestri as "Stifellius"; this formed the basis of Piave's libretto.

**d9: Aroldo**

- [d9s0] Aroldo (] ) is an opera in four acts by Giuseppe Verdi to an Italian libretto by Francesco Maria Piave, based on and adapted from their earlier 1850 collaboration, "Stiffelio".
- [d9s1]  The first performance was given in the Teatro Nuovo Comunale in Rimini on 16 August 1857.

**d10: José Cura**

- [d10s0] José Cura (born December 5, 1962 in Rosario, Argentina) is an Argentine operatic tenor, conductor, director, scenographer and photographer known for intense and original interpretations of opera characters, notably "Otello" in Verdi’s "Otello", "Samson" in Saint-Saëns’ "Samson et Dalila", "Canio" in Ruggero Leoncavallo's "Pagliacci", "Stiffelio" in Giuseppe Verdi's "Stiffelio" and many others.

## 20. hotpotqa_5ae234405542992decbdcc5a

原位置：`train` 第 230 题 · 全局第 230 题 · `sample_id: hotpotqa_5ae234405542992decbdcc5a`

Question: In which city will you find the MTR or Mass Transit Railway which stops at Tin Yuet () which is located at ground level at the centre of Tin Shing Road and between Tin Yuet Estate and Tin Ching Estate?

Note: 如果题目信息可以算作已知条件，按single拆分

Type: single · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | city where the MTR or Mass Transit Railway which stops at Tin Yuet is located | True | [] | Hong Kong | [["d4s0"], ["d5s0"], ["d8s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | rail network that the Tin Yuet stop belongs to | False | [] | MTR Light Rail | [['d1s0']] |
| u2 | city served by {u1} | True | ['u1'] | Hong Kong | [['d4s0'], ['d5s0'], ['d8s0']] |

### Source documents (reference only)

**d1: Tin Yuet Stop**

- [d1s0] Tin Yuet () is an MTR Light Rail stop.
- [d1s1]  It is located at ground level at the centre of Tin Shing Road, between Tin Yuet Estate and Tin Ching Estate, in Tin Shui Wai, Yuen Long District.
- [d1s2]  It began service on 7 December 2003 and belongs to Zone 5A.
- [d1s3]  It serves Tin Yuet Estate and Tin Ching Estate.

**d2: Tin Wu Stop**

- [d2s0] Tin Wu () is an MTR Light Rail stop.
- [d2s1]  It is located at ground level at the junction of Tin Wu Road and Tin Shing Road in Tin Shui Wai, Yuen Long District.
- [d2s2]  It began service on 7 December 2003 and belongs to Zone 4.
- [d2s3]  It serves Tin Shui Wai Sports Ground and Tin Shui Wai Sports Centre.

**d3: Ginza Stop**

- [d3s0] Ginza () is an MTR Light Rail stop.
- [d3s1]  It is located at ground level in the centre of Tin Shing Road in Tin Shui Wai, Yuen Long District.
- [d3s2]  It began service on 7 December 2003 and belongs to Zone 4.
- [d3s3]  It is the only station on the MTR network with a Japanese name, and it is one of the two Light Rail stops with announcements in Mandarin Chinese.

**d4: MTR**

- [d4s0] The Mass Transit Railway (MTR; ) is a major public transport network serving Hong Kong.
- [d4s1]  Operated by the MTR Corporation Limited (MTRCL), it consists of heavy rail, light rail, and feeder bus service centred on an 11-line rapid transit network serving the urbanised areas of Hong Kong Island, Kowloon, the New Territories.
- [d4s2]  The system currently includes 218.2 km of rail with 159 stations, including 91 heavy rail stations and 68 light rail stops.
- [d4s3]  The MTR is one of the most profitable metro systems in the world, with a high farebox recovery ratio of 124% in 2016.

**d5: Sha Tin Station**

- [d5s0] Sha Tin () is a station on the East Rail Line of Hong Kong's Mass Transit Railway (MTR) system.
- [d5s1]  The station is located in the town centre of Sha Tin.

**d6: Tin Yiu Stop**

- [d6s0] Tin Yiu () is an MTR Light Rail stop.
- [d6s1]  It is located at ground level at Tin Shui Road near Tin Yiu Estate in Tin Shui Wai, Yuen Long District.
- [d6s2]  It began service on 10 January 1993 and belongs to Zone 4.
- [d6s3]  It serves Tin Yiu Estate and Tin Shing Court.

**d7: Tin Yat Stop**

- [d7s0] Tin Yat () is one of the MTR Light Rail stops.
- [d7s1]  It is located at ground level at the centre of Tin Shui Road and Tin Sau Road in Tin Shui Wai, Yuen Long District, Hong Kong.
- [d7s2]  It began service on 7 December 2003 and belongs to Zone 5A.

**d8: Fo Tan Station**

- [d8s0] Fo Tan () is a station on the East Rail Line of the Mass Transit Railway (MTR) system in Hong Kong.
- [d8s1]  It is located in the Fo Tan area of Sha Tin District, between Sha Tin and University stations on the East Rail Line's main branch.
- [d8s2]  The Racecourse station is located parallel to Fo Tan, on the line's Racecourse branch.

**d9: Tin Wing Stop**

- [d9s0] Tin Wing Stop () is an MTR Light Rail stop.
- [d9s1]  It is located at ground level at the centre of Tin Wing Road, Tin Shing Road, and Tin Yan Road in Tin Shui Wai Town Centre, Yuen Long District.
- [d9s2]  It began service on 26 March 1995 and belongs to Zone 4.

**d10: Tin Tsz Stop**

- [d10s0] Tin Tsz () is an MTR Light Rail stop.
- [d10s1]  It is located at ground level near the Tin Shing Road, near Tin Tsz Estate, in Tin Shui Wai, Yuen Long District, Hong Kong.
- [d10s2]  It began service on 7 December 2003 and belongs to Zone 4 of single-ride tickets.
- [d10s3]  It serves Tin Tsz Estate, Tin Lai Court, and Tin Yau Court.

## 21. hotpotqa_5ae266c35542996483e6499a

原位置：`train` 第 231 题 · 全局第 231 题 · `sample_id: hotpotqa_5ae266c35542996483e6499a`

Question: Which genus of plants has a larger range, Fritillaria or Teucrium?

Note: 

Type: comparison · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | range of Fritillaria | False | [] | Eurasia, North Africa, and North America | [["d6s0"]] | context |
| u2 | range of Teucrium | False | [] | worldwide | [["d7s5"]] | context |
| u3 | which genus has a larger range | True | ["u1", "u2"] | Teucrium | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | geographic range of the genus Fritillaria | False | [] | Eurasia, North Africa, and North America | [['d6s0']] |
| u2 | geographic range of the genus Teucrium | False | [] | worldwide | [['d7s5']] |
| u3 | which of Fritillaria and Teucrium has a larger range | True | ['u1', 'u2'] | Teucrium | [[]] |

### Source documents (reference only)

**d1: West Berkshire Museum**

- [d1s0] Berkshire Museum is located in Newbury, Berkshire.
- [d1s1]  Established in 1904, the museum houses various artworks and collections.
- [d1s2]  The museum is housed in two of Newbury's most historic buildings.
- [d1s3]  The Cloth Hall was built in 1627 by Richard Emmes, a master carpenter of Speenhamland for the Newbury Corporation as a cloth factory.
- [d1s4]  Originally part of a larger range of buildings with a courtyard in the centre, the building was subsequently used as a workhouse, hospital and school before being used for storing corn from 1829 until its conversion to a museum.

**d2: List of mountains in Poland**

- [d2s0] The Sudetes and Carpathian Mountains mountain ranges are located on either side of Poland's southern border.
- [d2s1]  Within Poland, neither of these ranges is forbidding enough to prevent substantial habitation; the Carpathians are especially densely populated.
- [d2s2]  The rugged form of the Sudeten range derives from the geological shifts that formed the later Carpathian uplift.
- [d2s3]  The Carpathians in Poland, formed as a discrete topographical unit in the relatively recent Tertiary Era, are the highest mountains in the country.
- [d2s4]  They are the northernmost edge of a much larger range that extends into the Czech Republic, Slovakia, Ukraine, Hungary, and Romania.

**d3: Elsinore Mountains**

- [d3s0] Elsinore Mountains, a ridge of mountains within the larger range of the Santa Ana Mountains, in the Cleveland National Forest, Riverside County, California, United States.
- [d3s1]  the tallest peaks within the range is the unofficially named San Mateo Peak at 3,591 ft. Second is officially named Elsinore Peak at 3536 feet.
- [d3s2]  The Elsinore Mountanins run in a ridge from just east of El Cariso, southeast to Elsinore Peak.
- [d3s3]  Beyond that peak the ridge begins to descend and curves to the east.
- [d3s4]  From Elsinore Peak, a ridge runs to the west and then northwest to San Mateo Peak, enclosing the Morrell Potrero on the south and west.

**d4: Proserpinus**

- [d4s0] Proserpinus is a genus of moths in the family Sphingidae, the sphinx moths or hawk moths.
- [d4s1]  Species of the genus are native to North America with the exception of "P. proserpinus", which has a much larger range extending from Asia to Africa.

**d5: Fujifilm X-series**

- [d5s0] The Fujifilm X-series range of digital cameras consists of Fujifilm's high-end digital cameras and is aimed at professional and keen enthusiast photographers.
- [d5s1]  It is part of the larger range of Fujifilm's digital cameras.
- [d5s2]  X-series itself is not characterized by a single common sensor size, technology or a lens format.
- [d5s3]  Rather, its main differentiating feature is emphasis on the controls needed by an advanced digital camera user.

**d6: Fritillaria**

- [d6s0] Fritillaria is a genus of Eurasian, North African, and North American plants in the lily family.

**d7: Teucrium**

- [d7s0] Teucrium is a genus of mostly perennial plants in the family Lamiaceae.
- [d7s1]  Some of the New World species are annuals.
- [d7s2]  The name is believed to refer to King Teucer of Troy.
- [d7s3]  Members of the genus are commonly known as germanders.
- [d7s4]  There are hundreds of species, including herbs, shrubs or subshrubs.
- [d7s5]  They are found all over the world but are most common in Mediterranean climates.

**d8: Cerro Catedral (Uruguay)**

- [d8s0] Cerro Catedral ("Cathedral Hill"), also known as Cerro Cordillera, is a peak and the highest point of Uruguay, with an altitude of 513.66 m .
- [d8s1]  It is located north of Maldonado Department, in the municipality of Aiguá, in a hill range named Sierra Carapé, which constitutes part of a larger range named Cuchilla Grande.
- [d8s2]  Its name derived from the curious forms of the rocky elevations of its summit, which are very common in the southern part of this country.

**d9: Granite Wash Mountains**

- [d9s0] The Granite Wash Mountains are a short, arid, low elevation mountain range of western-central Arizona, in the southeast of La Paz County.
- [d9s1]  The range borders a slightly larger range southeast, the Little Harquahala Mountains; both ranges form a section on the same water divide between two desert washes.
- [d9s2]  The washes flow in opposite directions, one northwest to the Colorado River, the other southeast to the Gila River.

**d10: International Harvester Light Line pickup**

- [d10s0] The International D-Series (1000–1500) replaced the C-Series as International's Light Line range of pickup trucks in early 1969, for a shortened model year.
- [d10s1]  The name started out as a simple continuation of the previous A-, B-, and C-series trucks.
- [d10s2]  It was largely a rebodied version of its predecessors, with a square-rigged look very similar to the period Scout utility vehicle.
- [d10s3]  The Travelall underwent parallel changes to the Light Line trucks.
- [d10s4]  The light line of trucks was marked by a larger range of transmission and wheelbase options than any of its competitors, and in general the lineup aimed to maximize adaptability.
- [d10s5]  The Light Line was also available as a bare chassis, for special purpose applications.
- [d10s6]  Production ended without replacement in late April 1975, as a hard-pressed International chose to focus on the Scout and on heavier machinery.

## 22. hotpotqa_5ae31f4455429928c423961b

原位置：`train` 第 232 题 · 全局第 232 题 · `sample_id: hotpotqa_5ae31f4455429928c423961b`

Question: Jordan Lussey is a midfielder for a football club that is based in Telford, Shropshire, England, and whose colours are what?

Note: 

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | football club that Jordan Lussey plays for | False | [] | A.F.C. Telford United | [["d6s0"]] | context |
| u2 | colours of {u1} | True | ["u1"] | white with navy blue and red trim | [["d2s3"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | football club for which Jordan Lussey plays as a midfielder | False | [] | A.F.C. Telford United | [['d6s0']] |
| u2 | colours of {u1} | True | ['u1'] | white with navy blue and red trim | [['d2s3']] |

### Source documents (reference only)

**d1: Oakengates Athletic F.C.**

- [d1s0] Oakengates Athletic Football Club (previously Oakengates Town) is a football club based in Telford, Shropshire.
- [d1s1]  The club plays 'home' games at Doseley Road, Dawley.
- [d1s2]  It is named for the town of Oakengates, now part of Telford.

**d2: A.F.C. Telford United**

- [d2s0] A.F.C. Telford United is a football club based in Telford, Shropshire, England.
- [d2s1]  The club were formed after Telford United folded due to financial problems.
- [d2s2]  Currently members of the National League North, the sixth tier of English football, they play home matches at the New Bucks Head in Wellington, part of the new town of Telford.
- [d2s3]  Their colours are white with navy blue and red trim.

**d3: New Bucks Head**

- [d3s0] New Bucks Head is a stadium in Telford, England and the home of Conference National football club A.F.C. Telford United.
- [d3s1]  It was originally built for Telford United to play at before they went bankrupt.
- [d3s2]  The stadium is on the same site as the original Bucks Head, which had been home to Telford United and Wellington Town for over a century.
- [d3s3]  The stadium was completed in 2003, and has a capacity of 6,300.
- [d3s4]  It is covered on three out of four sides.
- [d3s5]  The stadium lease and assets are currently held by Telford and Wrekin Council.

**d4: Allscott F.C.**

- [d4s0] Allscott Football Club is an English football club based in Telford, Shropshire.
- [d4s1]  The club participates in the West Midlands (Regional) League Division One the 11th tier of English football.

**d5: List of Shrewsbury Town F.C. seasons**

- [d5s0] Shrewsbury Town Football Club, a professional association football club based in Shrewsbury, Shropshire, England, was founded in 1886.
- [d5s1]  They first played league football in the inaugural Shropshire & District League for the 1890–91 season; they finished the season as runners-up and also won the Welsh Cup at the first attempt.
- [d5s2]  After five seasons in the Shropshire & District League, they were admitted to the Birmingham & District League in 1895; they won their first league championship in that league in 1923.
- [d5s3]  In 1937 they moved to the Midland Football League where they won the league three times out of the seven seasons they participated in.
- [d5s4]  In 1950 they joined The Football League competing in its Third Division North for one season before being transferred to the South equivalent for the rest of their time in the third division.
- [d5s5]  Shrewsbury played in the Third Division South until 1958–59, when they were placed in the Fourth Division on League reorganisation.
- [d5s6]  They gained their first promotion in the same season after finishing fourth.
- [d5s7]  They remained in The Football League, albeit in different divisions, until they were relegated to the Football Conference in 2003.
- [d5s8]  It was in the Conference where Shrewsbury achieved their first play-off success, when they beat Aldershot Town in a penalty shoot-out after a 1–1 draw after extra time at the Britannia Stadium to win promotion back into the newly renamed Football League Two.
- [d5s9]  Since then Shrewsbury have remained in the Football League.

**d6: Jordan Lussey**

- [d6s0] Jordan Lussey (born 2 November 1994) is an English semi-professional footballer who plays as a midfielder for National League North club A.F.C. Telford United.
- [d6s1]  He has played for Liverpool, Bolton Wanderers, York City and Southport.

**d7: Telford United F.C.**

- [d7s0] Telford United Football Club was an English football club based in Telford, Shropshire.

**d8: Telford Raiders**

- [d8s0] Telford Raiders ARLFC are a rugby league club based in the town of Telford in Shropshire, England.
- [d8s1]  Their first team plays in the Midlands Regional division of the Rugby League Conference and they have a development team in the Midlands Rugby League as well as an active junior development program.

**d9: Wellington Amateurs F.C.**

- [d9s0] Wellington Amateurs Football Club is an English football club located in Telford, in Shropshire.
- [d9s1]  The club plays in the West Midlands (Regional) League Premier Division .
- [d9s2]  After many years in the Wellington League, the team was promoted to the Shropshire County Football League.
- [d9s3]  They were promoted to the West Midlands (Regional) League in 2006.
- [d9s4]  Wellington won Division One three times in four seasons and gained promotion to the Premier Division for 2012–13.

**d10: Telford United**

- [d10s0] Telford United may refer to one of two an English association football club based in Telford, Shropshire:

## 23. hotpotqa_5ae340c45542992f92d82273

原位置：`train` 第 233 题 · 全局第 233 题 · `sample_id: hotpotqa_5ae340c45542992f92d82273`

Question: The tour that Taylor Swift completed in Singapore on June 12, 2014 grossed how much?

Note: 按照旧拆法拆分

Type: bridge · fallback: False · SFT snapshots: 7

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | Taylor Swift tour that concluded in Singapore on June 12, 2014 | False | [] | The Red Tour | [["d2s1"], ["d7s5"]] | context |
| u2 | amount grossed by {u1} | True | ["u1"] | over $150 million | [["d7s5"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | Taylor Swift tour that concluded in Singapore on June 12, 2014 | False | [] | The Red Tour | [['d2s1'], ['d7s5']] |
| u2 | amount grossed by {u1} | True | ['u1'] | over $150 million | [['d7s5']] |

### Source documents (reference only)

**d1: The 1989 World Tour**

- [d1s0] The 1989 World Tour was the fourth concert tour by American singer-songwriter Taylor Swift, in support of her fifth studio album, "1989" (2014).
- [d1s1]  The tour's European and North American dates, as well as two shows in Japan, were announced in November 2014, followed by the Oceania dates in December 2014.
- [d1s2]  Additional dates for Singapore and Shanghai were announced in June 2015 with a third and final Melbourne show announced in July 2015.
- [d1s3]  The tour began on May 5, 2015, in Tokyo, Japan and concluded on December 12, 2015 in Melbourne, Australia, the day before her 26th birthday.
- [d1s4]  The tour became Swift's highest grossing and most attended tour to date, mobilizing 2,278,647 fans and $250,733,097 revenue.
- [d1s5]  It was the highest grossing tour in the world in 2015.

**d2: The Red Tour**

- [d2s0] The Red Tour was the third concert tour by American singer-songwriter Taylor Swift.
- [d2s1]  Launched in support of Swift's fourth studio album, "Red" (2012), the tour began on March 13, 2013 in Omaha, Nebraska and concluded on June 12, 2014 in Singapore.

**d3: Taylor Swift (album)**

- [d3s0] Taylor Swift is the debut studio album by American singer-songwriter Taylor Swift, released on October 24, 2006, by Big Machine Records.
- [d3s1]  Swift was 16 years old at the time of the album's release and wrote its songs during her freshman year of high school.
- [d3s2]  Swift has writing credits on all of the album's songs, including those co-written with Liz Rose.
- [d3s3]  Swift experimented with several producers, ultimately choosing Nathan Chapman, who had produced her demo album.
- [d3s4]  Musically, the album is country music styled, and lyrically it speaks of romantic relationships, a couple of which Swift wrote from observing relationships before being in one.
- [d3s5]  Lyrics also touch on Swift's personal struggles in high school.

**d4: Our Song (Taylor Swift song)**

- [d4s0] "Our Song" is a country song performed by American singer-songwriter Taylor Swift.
- [d4s1]  The song was written by Swift and produced by Nathan Chapman.
- [d4s2]  It was released on September 9, 2007 by Big Machine Records as the third single from Swift's eponymous debut album, "Taylor Swift" (2006).
- [d4s3]  Swift solely composed "Our Song" for the talent show of her freshman year in high school, about a boyfriend who she did not have a song with.
- [d4s4]  It was included on "Taylor Swift" as she recalled its popularity with her classmates.
- [d4s5]  The uptempo track is musically driven mainly by banjo and lyrically describes a young couple who use the events in their lives in place of a regular song.

**d5: Beautiful Eyes**

- [d5s0] Beautiful Eyes is the second extended play (EP) by American singer-songwriter Taylor Swift.
- [d5s1]  The EP was released on July 15, 2008 by Big Machine Records exclusively to Walmart stores in the United States and online.
- [d5s2]  The limited release EP has a primarily country pop sound and features alternate versions of tracks from her debut album, "Taylor Swift" (2006), and two original tracks, "Beautiful Eyes" and "I Heart ?"
- [d5s3] , songs which she had previously written; a DVD, featuring music videos of singles from "Taylor Swift", is also included on the physical release of the EP.

**d6: Fearless (Taylor Swift song)**

- [d6s0] "Fearless" is a country pop song performed by American singer-songwriter Taylor Swift.
- [d6s1]  The song was co-written by Swift in collaboration with Liz Rose and Hillary Lindsey and produced by Nathan Chapman and Swift.
- [d6s2]  "Fearless" was released on January 3, 2010 by Big Machine Records as the fifth and final single from Swift's second studio album of the same name (2008).
- [d6s3]  Swift composed the song while traveling on tour to promote her eponymous debut album, "Taylor Swift" (2006).
- [d6s4]  She wrote "Fearless" in regard to the fearlessness of falling in love and eventually titled her second studio album after the song.
- [d6s5]  Musically, it contains qualities commonly found in country pop music and, lyrically, is about a perfect first date.

**d7: Red (Taylor Swift album)**

- [d7s0] Red is the fourth studio album by American singer-songwriter Taylor Swift.
- [d7s1]  It was released on October 22, 2012, by Big Machine Records, as the follow-up to her third studio album, "Speak Now".
- [d7s2]  The album title was inspired by the "semi-toxic relationships" that Swift experienced during the process of conceiving this album, which Swift described the emotions she felt as "red emotions" due to their intense and tumultuous nature.
- [d7s3]  "Red" touches on Swift's signature themes of love and heartbreak, however, from a more mature perspective while exploring other themes such as fame and the pressure of being in the limelight.
- [d7s4]  The album features collaborations with producers and guest artists such as Gary Lightbody of Snow Patrol and Ed Sheeran and is noted for Swift's experimentation with new musical genres.
- [d7s5]  Swift completed The Red Tour in support of the album on June 12, 2014, which became the highest-grossing tour of all time by a country artist, grossing over $150 million.

**d8: Fearless Tour**

- [d8s0] The Fearless Tour was the debut concert tour by American singer-songwriter Taylor Swift.
- [d8s1]  Also referred to as the Fearless Tour 2009 and the Fearless Tour 2010, it was launched in support of her second studio album ""Fearless"" (2008).
- [d8s2]  On the tour, she was joined by guests Kellie Pickler and Gloriana.
- [d8s3]  Teen singer Justin Bieber joined her as an opening act for the tour when she went to England in November 2009.
- [d8s4]  During the tour, Swift performed with guests such as John Mayer, Katy Perry, and Faith Hill.
- [d8s5]  It grossed $63,705,590 from 89 reported shows and an audience of 1,138,977.

**d9: Picture to Burn**

- [d9s0] "Picture to Burn" is a song recorded by American singer-songwriter Taylor Swift.
- [d9s1]  It was co-written by Swift and Liz Rose, and produced by Nathan Chapman.
- [d9s2]  It was released on February 3, 2008 by Big Machine Records as the fourth single from Swift's eponymous studio album, "Taylor Swift" (2006).
- [d9s3]  It was inspired by the narcissistic and cocky nature of her former high school classmate and ex-boyfriend Jordan Alford with whom Swift never established a formal relationship.
- [d9s4]  In retrospect, Swift has stated that she has evolved on a personal level and as a songwriter, claiming she processed emotions differently since "Picture to Burn".
- [d9s5]  The song was chosen as a single based on the audience's reaction to it in concert.
- [d9s6]  Musically, the track is of the country rock genre with prominent usage of guitar, banjo, and drums.
- [d9s7]  The lyrics concern setting fire to photographs of a former boyfriend.

**d10: The Taylor Swift Holiday Collection**

- [d10s0] The Taylor Swift Holiday Collection, originally titled Sounds of the Season: The Taylor Swift Holiday Collection, is a Christmas EP by American singer Taylor Swift.
- [d10s1]  The EP was first released on October 14, 2007 by Big Machine Records exclusively to Target stores in the United States and online.
- [d10s2]  The release was originally a limited release for the 2007 holiday season, but was re-released to iTunes and Amazon.com on December 2, 2008 and again in October 2009 to Target stores.
- [d10s3]  "The Taylor Swift Holiday Collection" features cover versions of Christmas songs and two original tracks written by Swift, "Christmases When You Were Mine" and "Christmas Must Be Something More", all of which have a country pop sound.

## 24. hotpotqa_5ae3f3cb5542995ad6573cd9

原位置：`train` 第 234 题 · 全局第 234 题 · `sample_id: hotpotqa_5ae3f3cb5542995ad6573cd9`

Question: Which company works with petroleum, Apache Corporation or Alexion Pharmaceuticals?

Note: 

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | whether Apache Corporation works with petroleum | False | [] | yes | [["d7s0"]] | context |
| u2 | whether Alexion Pharmaceuticals works with petroleum | False | [] | no | [["d3s0"]] | definition_omission |
| u3 | which company works with petroleum | True | ["u1", "u2"] | Apache Corporation | [[]] | derived_from_dependencies |

- u2：`by_omission=true`，沿用定义性介绍省略规则，不是文中明确否定。

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Apache Corporation works with petroleum | False | [] | yes | [['d7s0']] |
| u2 | whether Alexion Pharmaceuticals works with petroleum | False | [] | no | [['d3s0']] |
| u3 | which of Apache Corporation and Alexion Pharmaceuticals works with petroleum | True | ['u1', 'u2'] | Apache Corporation | [[]] |

### Source documents (reference only)

**d1: David L. Hallal**

- [d1s0] David L. Hallal is the former President and Chief Executive Officer (CEO) of Alexion Pharmaceuticals, the American pharmaceutical company best known for its development of Soliris, a drug used to treat the rare disorders atypical hemolytic uremic syndrome (aHUS) and paroxysmal nocturnal hemoglobinuria (PNH).

**d2: Raymond Plank**

- [d2s0] Raymond Plank (born May 29, 1922) is the founder and retired Chairman of Apache Corporation.
- [d2s1]  He led Apache from a small oil and gas concern to a conglomerate with interests in energy, commercial real estate, agriculture, manufacturing and telecommunications, then divested its non-energy assets to concentrate exclusively on oil and gas exploration and production.
- [d2s2]  Under Plank’s leadership Apache expanded its oil and gas operations internationally and built the company from its original $250,000 capitalization to a market capitalization of over $30 billion.

**d3: Alexion Pharmaceuticals**

- [d3s0] Alexion Pharmaceuticals Inc. is an American pharmaceutical company best known for its development of Soliris, a drug used to treat the rare disorders atypical hemolytic uremic syndrome (aHUS) and paroxysmal nocturnal hemoglobinuria (PNH).
- [d3s1]  The company is also involved in immune system research related to autoimmune diseases.
- [d3s2]  It employs around 2,400 people worldwide.
- [d3s3]  In February 2016, the company held the dedication ceremony for its new headquarters in New Haven, Connecticut, not far from the company's starting point in the same city.

**d4: Hendrickson International**

- [d4s0] Hendrickson Corporation is an American privately held company located in Itasca, Illinois with revenues in excess of $1 billion that designs and manufactures commercial full-size truck suspensions.
- [d4s1]  The company works with single, tandem, and tridem drive axles as well as front and trailer suspensions.
- [d4s2]  The Bumper & Trim division manufactures exactly that, and Hendrickson Spring manufactures mechanical springs for the Hendrickson suspensions.

**d5: Hunt Petroleum**

- [d5s0] Hunt Petroleum Corporation was an oil and gas exploration and production company formed in 1950.
- [d5s1]  The company was originally called Petrol Production Co. and was later renamed Hunt Petroleum Corporation.
- [d5s2]  The company was a Delaware corporation owned 52.84% by the Margaret Hunt Trust Estate and 47.16% by the Haroldson L. Hunt, Jr.
- [d5s3]  Trust Estate.
- [d5s4]  The primary beneficiaries of these two trusts are the two eldest children of the late H. L. Hunt and Lyda Bunker Hunt.
- [d5s5]  Hunt Petroleum Corporation had no common ownership and was not affiliated with any of the following entities: Hunt Oil Company; Petro-Hunt, LLC; Hunt Exploration; Unity Hunt; Hunt Properties; or Rosewood Resources.

**d6: Ludwig N. Hantson**

- [d6s0] Ludwig Norbert Michel Hantson (born August 1962) is a Belgium businessman, the CEO of Alexion Pharmaceuticals since March 2017.
- [d6s1]  He was the president and CEO of Baxalta, an American biopharmaceutical company, from 2015 to 2016.

**d7: Apache Corporation**

- [d7s0] Apache Corporation is an American petroleum and natural gas exploration and production company headquartered in Houston, Texas.

**d8: Oge Modie**

- [d8s0] Ogechukwu Olufunmilola Modie (born January 12, 1976) is a Nigerian public servant who works as the Chief of Staff (an unconstitutional office) to the Honorable Minister of State for Petroleum Resources.
- [d8s1]  She was the Chief of Staff (an unconstitutional office) to the former Group Managing Director (GMD) of Nigerian National Petroleum Corporation (NNPC), Nigeria's National Oil Corporation.
- [d8s2]  Subsequently, the GMD was named as the Chairman of the Board of the Corporation, as provided for under Section 1(2) of the Nigerian National Petroleum Corporation Act of 1997, as amended on 4th of July, 2016.
- [d8s3]  Her primary responsibility is the provision of administrative, organisational and advisory support to Dr. Emmanuel Ibe Kachikwu.
- [d8s4]  She assumed duty in August 2015.

**d9: Mekong Auto**

- [d9s0] Mekong Auto Corporation headquartered in Ho Chi Minh City, Vietnam, is a car manufacturer and assembler founded in 1991.
- [d9s1]  The first car was built at the Delta Auto Plant on May 20, 1992.
- [d9s2]  Japanese Saeilo Machinery Japan Inc. is the major shareholder of the company, owning 51%.
- [d9s3]  The company opened Co Loa Auto Plant in Ha Noi City in 1993.
- [d9s4]  The company works with Fiat S.p.A. (Fiat cars and Iveco trucks), Pyeonghwa Motors and SsangYong.

**d10: Forum Corporation**

- [d10s0] The Forum Corporation is a global learning and consulting company focused on leadership development and sales performance.
- [d10s1]  The company works with customers around the world and across a large variety of industries.
- [d10s2]  Founded in 1971, the company established itself as a pioneer in the corporate training and education space.
- [d10s3]  Forum has worked with over 480 companies, 130 of which are listed on the Fortune 500.

## 25. hotpotqa_5ae3fc835542995dadf24288

原位置：`train` 第 235 题 · 全局第 235 题 · `sample_id: hotpotqa_5ae3fc835542995dadf24288`

Question: In between Die schweigsame Frau and La straniera which one is an opera in three acts?

Note: 

Type: comparison · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新 whether 三幕查询，旧 three/two 改为 yes/no，支持证据不变。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | whether Die schweigsame Frau is an opera in three acts | False | [] | yes | [["d10s0"]] | context |
| u2 | whether La straniera is an opera in three acts | False | [] | no | [["d8s0"]] | context |
| u3 | which one is an opera in three acts | True | ["u1", "u2"] | Die schweigsame Frau | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | number of acts in the opera Die schweigsame Frau | False | [] | three | [['d10s0']] |
| u2 | number of acts in the opera La straniera | False | [] | two | [['d8s0']] |
| u3 | which of Die schweigsame Frau and La straniera is an opera in three acts | True | ['u1', 'u2'] | Die schweigsame Frau | [[]] |

### Source documents (reference only)

**d1: Die Frau ohne Schatten**

- [d1s0] Die Frau ohne Schatten (The Woman without a Shadow), Op. 65, is an opera in three acts by Richard Strauss with a libretto by his long-time collaborator, the poet Hugo von Hofmannsthal.
- [d1s1]  It was written between 1911 and either 1915 or 1917.
- [d1s2]  When it premiered in Vienna on 10 October 1919, critics and audiences were unenthusiastic.
- [d1s3]  Many cited problems with Hofmannsthal's complicated and heavily symbolic libretto.
- [d1s4]  However, it is now a standard part of the operatic repertoire.

**d2: The Singing Lesson**

- [d2s0] The Singing Lesson is a chamber opera in three acts with music and libretto by Matthew Davidson.
- [d2s1]  Based on three short stories ("The Garden Party", "The Singing Lesson", and "The Doll’s House") by New Zealand author Katherine Mansfield, the opera is very unusual in several respects.
- [d2s2]  For instance, the three acts are not connected by a conventional plot, but instead by literary themes.
- [d2s3]  Those themes are class conflict (Acts 1 and 3) and a marriage of convenience (Act 2).
- [d2s4]  However, the overall literary theme for all three acts is delusion.

**d3: Mark Delavan**

- [d3s0] Mark Delavan is an American operatic bass-baritone.
- [d3s1]  He made his professional debut in 1986 at the San Francisco Opera in a small role in Giuseppe Verdi's "Don Carlos".
- [d3s2]  He spent the next three years performing in numerous comprimario roles with the company.
- [d3s3]  He has since returned to that opera house to sing Scarpia in Giacomo Puccini's "Tosca" (2004, with Carol Vaness in the title role) and Wotan in Richard Wagner's "The Ring Cycle" (2008, 2010, and 2011).
- [d3s4]  In 2001 he made his debut at the Metropolitan Opera as Amonasro in Verdi's "Aida" with Deborah Voigt in the title role, Luciano Pavarotti as Radamès, Olga Borodina as Amneris, and James Levine conducting.
- [d3s5]  He has since been heard at the Met as Alfio in Pietro Mascagni's "Cavalleria rusticana", Carlo Gérard in "Andrea Chénier", Count Tomsky in "The Queen of Spades", Don Carlo in Verdi's "La Forza del Destino", the Messenger in Richard Strauss' "Die Frau ohne Schatten", Scarpia, and the title roles in Verdi's "Nabucco", Verdi's "Rigoletto", and Verdi's "Simon Boccanegra".

**d4: Titon et l'Aurore**

- [d4s0] Titon et l'Aurore (English: "Tithonus and Aurora") is an opera in three acts and a prologue by the French composer Jean-Joseph de Mondonville which was first performed at the Académie royale de musique, Paris on 9 January 1753.
- [d4s1]  The authorship of the libretto has been subject to debate; Mondonville's contemporaries ascribed the prologue to Antoine Houdar de la Motte and the three acts of the opera to the Abbé de La Marre.
- [d4s2]  "Titon et l'Aurore" belongs to the genre known as the "pastorale héroïque".
- [d4s3]  The work played an important role in the so-called Querelle des Bouffons, a dispute over the relative merits of the French and Italian operatic traditions which dominated the intellectual life of Paris in the early 1750s.
- [d4s4]  The tremendous success of Mondonville's opera at its premiere was an important victory for the French camp (although their Italian rivals claimed that this was because they had been excluded from their seats by members of the army).
- [d4s5]  "Titon" was one of Mondonville's most popular works and went on to enjoy several revivals during his lifetime.

**d5: Die geschiedene Frau**

- [d5s0] Die geschiedene Frau ("The Divorcée"), is an operetta in three acts by Leo Fall with a libretto by Victor Léon, after Victorien Sardou's "Divorçons!"
- [d5s1] .
- [d5s2]  Conducted by the composer, It opened to considerable success at the Carltheater in Vienna on 23 December 1908 with Hubert Marischka as Karel.

**d6: Ellen Shade**

- [d6s0] Ellen Shade is an American operatic soprano from New York.
- [d6s1]  Her repertoire includes the Kaiserin in "Die Frau ohne Schatten", the Marschallin "Der Rosenkavalier", Chrysothemis "Elektra", Ariadne "Ariadne auf Naxos", Arabella, Katya Kabanova, Aida, Desdemona "Otello", Amelia "Un ballo in Maschera", Amelia "Simon Boccanegra", Sieglinde "Die Walkure", Elsa "Lohengrin", Elisabeth "Tannhauser", Eva "Die Meistersinger von Nurnberg".
- [d6s2]  In Europe she has appeared at La Scala Milan, the Royal Opera House, Covent Garden, the Bastille and the Chatelet in Paris and in Vienna, Salzburg Festival, Berlin, Hamburg, Frankfurt [Article Reference], Stuttgart, Amsterdam, Brussels, Geneva and Athens.
- [d6s3]  In North America she has performed with virtually all the major opera companies, including the Metropolitan Opera New York, Chicago, San Francisco, Los Angeles, Houston, Dallas, Seattle, Santa Fe, and the Canadian Opera in Toronto.

**d7: Die Kluge**

- [d7s0] Die Kluge.
- [d7s1]  Die Geschichte von dem König und der klugen Frau ("The Wise [Girl].
- [d7s2]  The Story of the King and the Wise Woman") is an opera in 12 scenes written by Carl Orff.
- [d7s3]  It premiered in Frankfurt, Germany, on 20 February 1943.
- [d7s4]  Orff referred to this opera as a "Märchenoper " (fairy tale opera).
- [d7s5]  The composer also wrote the libretto, based on "Die Kluge Bauerntochter" ("The Peasant's Wise Daughter") from the Grimm's Fairy Tales.
- [d7s6]  A performance lasts for about 90 minutes and is often paired with Orff's "Der Mond".

**d8: La straniera**

- [d8s0] La straniera ("The Foreign Woman") is an opera in two acts with music by Vincenzo Bellini to an Italian libretto by Felice Romani, based on the novel "L'Étrangère" (2 vols, 1825) by Charles-Victor Prévot, vicomte d'Arlincourt, although writer Herbert Weinstock also adds that it is "more likely [based on] a dramatization of [that novel] in Italian by Giovan Carlo, barone di Cosenza" since he then quotes a letter from Bellini to his friend Francesco Florimo in which he says that Romani "certainly will not follow the play" [suggesting then that they were aware of its existence.]

**d9: Die Jagd**

- [d9s0] Die Jagd ("The Hunt") is an opera by the German composer Johann Adam Hiller.
- [d9s1]  It takes the form of a "Singspiel" in three acts.
- [d9s2]  The libretto by Christian Felix Weiße is based on the plays "La partie de chasse de Henri IV " by Charles Collé, "The King and the Miller of Mansfield" by Robert Dodsley, and the "opéra comique" by Michel-Jean Sedaine (originally set by Monsigny).
- [d9s3]  The opera was first performed at the Schlosstheater, Weimar on 29 January 1770.
- [d9s4]  "Die Jagd" is considered one of the most important early "Singspiele".
- [d9s5]  It was admired by Goethe and Wagner.

**d10: Die schweigsame Frau**

- [d10s0] Die schweigsame Frau ("The Silent Woman"), Op. 80, is a 1935 opera in three acts by Richard Strauss with libretto by Stefan Zweig after Ben Jonson's "Epicoene, or the Silent Woman".

## 26. hotpotqa_5ae533495542992663a4f159

原位置：`train` 第 236 题 · 全局第 236 题 · `sample_id: hotpotqa_5ae533495542992663a4f159`

Question: Barbara Linares is a model for what parent company of Aerie?

Note: 按照新的拆分顺序

Type: bridge · fallback: False · SFT snapshots: 7

### Adjusted units and annotation

**执行结果：** 按 Note 保留先母公司后模特关系的顺序，修正必要单元使答案明确为公司。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | parent company of Aerie | False | [] | American Eagle Outfitters | [["d7s3"], ["d4s1"]] | context |
| u2 | parent company {u1} whose Aerie brand Barbara Linares models for | True | ["u1"] | American Eagle Outfitters | [["d4s0", "d4s1"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | brand that Barbara Linares models for | False | [] | Aerie | [['d4s0', 'd4s1']] |
| u2 | parent company of {u1} | True | ['u1'] | American Eagle Outfitters | [['d7s3'], ['d4s1']] |

### Source documents (reference only)

**d1: Saab Automobile**

- [d1s0] Saab Automobile AB was a manufacturer of automobiles that was founded in Sweden in 1945 when its parent company, SAAB AB (soon to be Saab AB) (   ), began a project to design a small automobile.
- [d1s1]  The first production model, the Saab 92, was launched in 1949.
- [d1s2]  In 1968 the parent company merged with Scania-Vabis, and ten years later the Saab 900 was launched, in time becoming Saab's best-selling model.
- [d1s3]  In the mid-1980s the new Saab 9000 model also appeared.

**d2: Life-Like**

- [d2s0] Life-Like was a manufacturer of model trains and accessories that began as a division of parent company Life-Like Products, a manufacturer of extruded foam ice chests and coolers.
- [d2s1]  In 1960 the company purchased the assets of the defunct Varney Scale Models and began manufacturing model trains and accessories under the name Life-Like in 1970.
- [d2s2]  In 2005 the parent company, known as Lifoam Industries, LLC, chose to concentrate on their core products and sold their model railroad operations to hobby distributor Wm. K. Walthers.
- [d2s3]  Today, the Life-Like trademark is used by Walthers for its line of value-priced starter train sets.

**d3: Pivotal Games**

- [d3s0] Pivotal Games Limited was a British video game developer based in Corston, England, founded in March 2000 by fifteen ex-Pumpkin Studios employees, after it was shut down by its parent company, Eidos Interactive.
- [d3s1]  Led by Jim Bambra, Nick Cook and Alex McLean, of which Bambra and Cook had previously founded Pumpkin Studios in August 1996, the studio was formed under the Kaboom Studios umbrella, in order to establish a publishing relationship to Sales Curve Interactive (SCi, later renamed SCi Games).
- [d3s2]  Between 2002 and 2008, Pivotal Games developed all installments in the "Conflict" series, as well as "The Great Escape", based on the film of the same name.
- [d3s3]  In September 2003, after financial struggles of parent company Kaboom Studios, who had at that point had already closed down sister studios Attention to Detail and Silicon Dreams Studio, SCi showed interest in acquiring the company.
- [d3s4]  Kaboom Studios went into receivership on 9 September 2003, with all remaining assets, including still-active Pivotal Games, being transferred to Ernst & Young for sale.
- [d3s5]  On 29 September 2003, SCi acquired Pivotal Games from Ernst & Young for a total of GB£ .
- [d3s6]  In May 2005, SCi Games finalised its acquisition and merger with Eidos plc, the parent of Eidos Interactive, which would become in charge of SCi Games' subsidiaries.
- [d3s7]  In March 2008, SCi Games closed down fourteen operating projects to counter a GB£ net loss from the preceding fiscal year, leading to rumors that Pivotal Games was also to be closed.
- [d3s8]  On 14 July 2008, it was officially announced that the studio was to shut its doors, and 99 staff had already been made redundant, leaving only a team of 10–12 specialist personnel.
- [d3s9]  Pivotal Games was closed on 13 August 2008.

**d4: Barbie Ferreira**

- [d4s0] Barbara "Barbie" Linhares Ferreira (born December 14, 1996) is an American model.
- [d4s1]  She models for Aerie, a brand of clothing from American Eagle Outfitters.

**d5: HNA Infrastructure Investment Group**

- [d5s0] Hainan HNA Infrastructure Investment Group Co., Ltd. formerly Hainan Island Construction Co., Ltd. is a Chinese listed company based in Haikou.
- [d5s1]  in mid-2016 the company acquired HNA Infrastructure Group () in a reverse IPO from intermediate parent company HNA Infrastructure Holding Group (), which HNA Infrastructure Group is the parent company of HNA Real Estate and HNA Airport Group (, in turn HNA Airport Group is the parent company of HNA Airport Holdings (Group) () and HNA Airport Holdings is the parent company of Sanya Phoenix International Airport Co., Ltd.); HNA Airport Group is the largest shareholder of Haikou Meilan International Airport (19.58% as at October 2016), which in turn the largest shareholder of Hong Kong listed company HNA Infrastructure.
- [d5s2]  In December 2016 a proposed capital increase of the HK-listed company was announced.
- [d5s3]  HNA Infrastructure Investment Group would purchase a minority share directly.
- [d5s4]  Haikou Meilan International Airport was the second-largest shareholder of Hainan Airlines; Hainan Airlines, however, also owned a minority stake in Haikou Meilan International Airport.

**d6: Parent company guarantee**

- [d6s0] A parent company guarantee (PCG) is a guarantee by a parent company of a contractor’s performance under its contract with its client, where the contractor is a subsidiary of the parent company.

**d7: American Eagle Outfitters**

- [d7s0] American Eagle Outfitters, Inc. is an American clothing and accessories retailer, headquartered in the Southside Works Neighborhood of Pittsburgh, Pennsylvania.
- [d7s1]  It was founded in 1977 by brothers Jerry and Mark Silverman as a subsidiary of Retail Ventures, Inc., a company which also owned and operated Silverman's Menswear.
- [d7s2]  The Silvermans sold their ownership interests in 1991 to Jacob Price of Knoxville, Tennessee.
- [d7s3]  American Eagle Outfitters is also the parent company of Aerie.

**d8: Aerie Pharmaceuticals**

- [d8s0] Aerie Pharmaceuticals (NASDAQ: AERI ) is a publicly traded, clinical-stage pharmaceutical company focused on the discovery, development and commercialization of first-in-class therapies for the treatment of patients with glaucoma and other diseases of the eye.
- [d8s1]  Aerie's two lead product candidates are once-daily IOP-lowering therapies with novel mechanisms of action to treat patients with glaucoma or ocular hypertension.

**d9: SM-Chile**

- [d9s0] SM-Chile is a holding company for Banco de Chile.
- [d9s1]  Until 1996, when its Board of Shareholders agreed to become an investment company with exclusive turn, governed by Law No. 19,396, changing its name to Bank of Parent Company Chile SA' Simultaneously, the parent company of Banco de Chile SA created a commercial bank under the name Banco de Chile and was transferred all its assets and liabilities, excluding subordinated obligation call with the Central Bank of Chile, obligation undertaken following the banking crisis of the years 1982 - 1984 and the consequent bailout carried out by the Central Bank.
- [d9s2]  After this transformation, the sole shareholder of Banco de Chile was the parent company of Banco de Chile SA

**d10: Structural subordination**

- [d10s0] In corporate finance, Structural subordination is the concept that a lender to a company will not have access to the assets of the company's subsidiary until after all of the subsidiary's creditors have been paid and the remaining assets have been distributed up to the company as an equity holder.
- [d10s1]  For example, if a lender loans money to a parent company, that lender is structurally subordinated to a lender who loaned money to a subsidiary operating company which is lower down in the company organizational structure.
- [d10s2]  The operating company lender is structurally senior, and the parent company lender can only be repaid from the operating assets after the operating company lender has been repaid.

## 27. hotpotqa_5ae5394855429908b6326585

原位置：`train` 第 237 题 · 全局第 237 题 · `sample_id: hotpotqa_5ae5394855429908b6326585`

Question: Which device can air TVPlayer channels for free and allows users to play using a remote?

Note: 这种并列条件的题可以按照single拆分

Type: single · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留用户要求的 single，联合 TVPlayer 设备与遥控游戏能力证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | device that can air TVPlayer channels for free and allows users to play using a remote | True | [] | Amazon Fire TV | [["d1s0", "d3s2"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | smart devices through which TVPlayer's free-to-air channels can be watched | False | [] | Apple TV 4th Generation and Amazon Fire TV | [['d1s0']] |
| u2 | which of {u1} allows users to play using a remote | True | ['u1'] | Amazon Fire TV | [['d3s2']] |

### Source documents (reference only)

**d1: TVPlayer**

- [d1s0] TVPlayer is a live TV streaming service for users to watch free-to-air channels through their smart devices (Apple TV 4th Generation Only, Amazon Fire TV) desktops, smartphones and tablets.
- [d1s1]  The TV service allows television licence holders in the United Kingdom to stream 78 free live television channels, including BBC, ITV, Channel 4, Channel 5, Heart TV, Capital TV and The Box.
- [d1s2]  TVPlayer offers a "TVPlayer Plus" branded 'no contract, cancel anytime' monthly or yearly subscription service which allows consumers access to an additional 30 live streaming television channels, including Gold, Cartoon Network, Discovery Channel, Eurosport 1 and Eurosport 2.
- [d1s3]  TVPlayer Plus also allows users to catch up on programmes with their 7-day catch up service when using a "Plus" subscription.
- [d1s4]  Brazilian Channel Globo is available with an extra subscription.

**d2: PicDial**

- [d2s0] PicDial is a mobile service created by IQzone Inc. and based in Scottsdale, Arizona, United States.
- [d2s1]  PicDial provides users with the ability to automatically see their friends' Facebook and MySpace profile pictures and status messages as Full Screen Caller ID on their mobile phone.
- [d2s2]  The software automatically keeps contacts social networking information current, allowing the most recent profile pictures and status messages to be displayed on incoming and outgoing calls or texts.
- [d2s3]  The PicDial application provides users with a "Favorites Screen," a visual grid that allows users to call or text by selecting a friends social networking profile picture.
- [d2s4]  This Mobile social address book platform allows users to link multiple social networks.
- [d2s5]  The application also enables users to determine which picture will display when a call or text is made to a PicDial friend, giving the user control over the picture seen by friends.
- [d2s6]  This defined picture can either be taken from the users camera on the phone, or pulled from their profile pictures on Facebook or MySpace.
- [d2s7]  When a user changes their picture (and status message), this new image will be updated to their friends' phones.

**d3: Amazon Fire TV**

- [d3s0] Amazon Fire TV refers to two digital media players and microconsoles developed by Amazon.com.
- [d3s1]  It is a small network appliance and entertainment device designed to stream digital audio/video content to a high-definition television.
- [d3s2]  The device also allows users to play video games with the included remote, via a mobile app, or with an optional game controller.

**d4: Packet Tracer**

- [d4s0] Packet Tracer is a cross-platform visual simulation tool designed by Cisco Systems that allows users to create network topologies and imitate modern computer networks.
- [d4s1]  The software allows users to simulate the configuration of Cisco routers and switches using a simulated command line interface.
- [d4s2]  Packet Tracer makes use of a drag and drop user interface, allowing users to add and remove simulated network devices as they see fit.
- [d4s3]  The software is mainly focused towards Certified Cisco Network Associate Academy students as an educational tool for helping them learn fundamental CCNA concepts.
- [d4s4]  Students enrolled in a CCNA Academy program can freely download and use the tool free of charge for educational use.

**d5: WhosHere**

- [d5s0] WhosHere is a social proximity networking app created by WhosHere founders Bryant Harris and Stephen Smith launched in July 2008.
- [d5s1]  WhosHere utilizes GPS location capabilities combined with a social networking platform that allows users to interact with other people based on compatible geographical location.
- [d5s2]  The app allows users to find other users with similar interests and connect with them real-time via free text, image messages and free VoIP calls without disclosing any personal information.
- [d5s3]  It runs on Apple iOS devices including iPhone, iPod touch and iPad.

**d6: TermWiki**

- [d6s0] TermWiki.com (pronounced ) is a major social learning network that allows users to learn, discover, share, and store personal terms and glossaries in 1487 domains in 97 languages.
- [d6s1]  The site emphasizes collaboration, with a forum, a question/answer module, messaging features that encourage user interaction, and discussion pages on each term.
- [d6s2]  The personal profile page allows users to become fans of other users, add photos, and add links and post comments on other users recent activity.
- [d6s3]  TermWiki also allows companies to conduct international ad campaigns on keyword terms, for improved SEO performance.

**d7: Web chat**

- [d7s0] A web chat is a system that allows users to communicate in real time using easily accessible web interfaces.
- [d7s1]  It is a type of Internet online chat distinguished by its simplicity and accessibility to users who do not wish to take the time to install and learn to use specialized chat software.
- [d7s2]  This trait allows users instantaneous access and only a web browser is required to chat.
- [d7s3]  Users will always get the latest version of a chat service because no software installation or updates are required.

**d8: Splashtop Remote**

- [d8s0] Splashtop Remote remote-desktop software allows users to connect to and control computers from various devices, such as a personal computer, iPad, iPhone, or Android device.
- [d8s1]  Unlike products using the Remote Desktop Protocol, Splashtop Remote uses a proprietary protocol capable of delivering real-time video and audio to the remote user at 60+ frames per seconds and low latency.
- [d8s2]  Splashtop has over 30 million users, and many device makers such as Acer, Asus, Dell, Epson, HP, Lenovo, Panasonic, Sharp, Sony, Toshiba, and others are bundling Splashtop with their devices.

**d9: PrivacyStar**

- [d9s0] PrivacyStar is a service that identifies who is calling and why, and provides for call complaint filing which reports to the Federal Trade Commission.
- [d9s1]  The PrivacyStar service is available on the web and on mobile applications for Android and iOS.
- [d9s2]  On several applications powered by PrivacyStar, call and text blocking is available.
- [d9s3]  The applications, along with PrivacyStar’s iPhone Lookup+ application, enable users to file potential debt collector and telemarketer violations directly to the FTC.
- [d9s4]  The application captures detailed information about possible Fair Debt Collection Practices Act violations including date, time, number, and identity and allows users to easily provide this information to regulatory agencies so they may take action.
- [d9s5]  PrivacyStar has over 1.2 million users who have blocked over 120 million calls and filed over 300,000 complaints directly with the Federal Trade Commission as of September 2012.
- [d9s6]  In fact, PrivacyStar is the leading source of all call complaint data reported to the FTC.
- [d9s7]  In 2015, its users filed 31% of all call complaints.
- [d9s8]  On February 13, 2013, PrivacyStar launched a free SMS spam complaint filing feature for Android smartphones.
- [d9s9]  The application allows users to file text message spam complaints in addition to the existing ability to file call complaints directly to the Federal Trade Commission from their Android phones.

**d10: DeepArt**

- [d10s0] DeepArt or DeepArt.io is a website that allows users to create unique artistic images by using an algorithm to redraw one image using the stylistic elements of another image.
- [d10s1]  This uses "A Neural Algorithm of Artistic Style" that was developed by several of its creators to separate style elements from a piece of art.
- [d10s2]  The tool allows users to create imitation works of art using the style of famous artists.
- [d10s3]  The neural algorithm is used by the Deep Art website to create a representation of an image provided by the user by using the 'style' of another image provided by the user.
- [d10s4]  A similar program, Prisma, is an iOS and Android app that was based on the open source programming that underlies DeepArt.

## 28. hotpotqa_5ae5397d55429960a22e0276

原位置：`train` 第 238 题 · 全局第 238 题 · `sample_id: hotpotqa_5ae5397d55429960a22e0276`

Question: Eliot Teltscher and Anastasia Myskina both played what sport?

Note: 只将 question_type 改为 comparison，保留当前单元关系

Type: comparison · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。 题型修正为 comparison。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | sport played by Eliot Teltscher | False | [] | tennis | [["d10s0"], ["d6s0", "d6s3"], ["d2s0"]] | context |
| u2 | sport played by Anastasia Myskina | False | [] | tennis | [["d3s0"], ["d3s1"], ["d3s2"]] | context |
| u3 | common sport played by both | True | ["u1", "u2"] | tennis | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | sport Eliot Teltscher played | False | [] | tennis | [['d10s0'], ['d6s0', 'd6s3'], ['d2s0']] |
| u2 | sport Anastasia Myskina played | False | [] | tennis | [['d3s0'], ['d3s1'], ['d3s2']] |
| u3 | sport that both Eliot Teltscher and Anastasia Myskina played | True | ['u1', 'u2'] | tennis | [[]] |

### Source documents (reference only)

**d1: 1983 Congoleum Classic – Singles**

- [d1s0] Yannick Noah was the defending champion but lost in the semifinals to Eliot Teltscher.

**d2: 1981 Grand Marnier Tennis Games – Doubles**

- [d2s0] Bruce Manson and Brian Teacher won in the final 7–6, 6–2 against Terry Moor and Eliot Teltscher.

**d3: Anastasia Myskina**

- [d3s0] Anastasiya Andreyevna Myskina (Russian: Анастасия Андреевна Мыскина ; ] ; born 8 July 1981) is a Russian former tennis player.
- [d3s1]  She won the 2004 French Open singles title, becoming the first Russian female tennis player to win a Grand Slam singles title.
- [d3s2]  Subsequent to this victory, she rose to No. 3 in the WTA rankings, becoming the first Russian female tennis player to reach the top 3 in the history of the rankings.
- [d3s3]  In September 2004, she reached a career-high ranking of No. 2.
- [d3s4]  She has not officially retired, but has been inactive on the WTA Tour since May 2007.

**d4: 2005 Wismilak International – Doubles**

- [d4s0] Anastasia Myskina and Ai Sugiyama were the defending champions, but none competed this year, with Myskina competing at the Fed Cup final during the same week.

**d5: 1979 New Zealand Open – Singles**

- [d5s0] Tim Wilkison defeated Peter Feigl 6–3, 4–6, 6–4, 2–6, 6–2 to win the 1979 Heineken Open singles competition.
- [d5s1]  Eliot Teltscher was the champion but did not defend his title.

**d6: 1978 New Zealand Open**

- [d6s0] The 1978 New Zealand Open, also known by its sponsored name Benson & Hedges New Zealand Open, was a men's professional tennis tournament held in Auckland, New Zealand.
- [d6s1]  It was a non-tour event, i.e. not part of the 1978 Grand Prix circuit.
- [d6s2]  The tournament was played on outdoor hard courts and was held from 2 January through 8 January 1978.
- [d6s3]  Eliot Teltscher won the singles title.

**d7: 2007 J&amp;S Cup – Doubles**

- [d7s0] Elena Likhovtseva and Anastasia Myskina were the defending champions, but Myskina chose not to compete that year.
- [d7s1]  Likhovtseva partnered with Elena Vesnina.

**d8: 1983 French Open – Mixed Doubles**

- [d8s0] The Mixed Doubles tournament at the 1983 French Open was held from 23 May until 5 June 1983 on the outdoor clay courts at the Stade Roland Garros in Paris, France.
- [d8s1]  Barbara Jordan and Eliot Teltscher won the title, defeating Leslie Allen and Charles Strode in the final.

**d9: 1980 Birmingham Open – Singles**

- [d9s0] Jimmy Connors was the defending champion and successfully defended his title, defeating Eliot Teltscher in the final, 6–3, 6–2.

**d10: Eliot Teltscher**

- [d10s0] Eliot Teltscher (born March 15, 1959, in Rancho Palos Verdes, California) is a retired professional American tennis player.
- [d10s1]  He resides in Irvine, California.

## 29. hotpotqa_5ae60b0d554299546bf8302c

原位置：`train` 第 239 题 · 全局第 239 题 · `sample_id: hotpotqa_5ae60b0d554299546bf8302c`

Question: Which professional footballer who plays as a left-back for Los Angeles Galaxy did Cheryl Cole divorced 

Note: 保留新的顺序，重构标签

Type: bridge · fallback: False · SFT snapshots: 7

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | professional footballer who plays as a left-back for Los Angeles Galaxy | False | [] | Ashley Cole | [["d1s0"]] | context |
| u2 | person Cheryl Cole divorced, given {u1} | True | ["u1"] | Ashley Cole | [["d6s0", "d6s4"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | footballer whom Cheryl Cole divorced | False | [] | Ashley Cole | [['d6s0', 'd6s4']] |
| u2 | professional footballer who plays as a left-back for Los Angeles Galaxy whom Cheryl Cole divorced, given {u1} | True | ['u1'] | Ashley Cole | [['d1s0']] |

### Source documents (reference only)

**d1: Ashley Cole**

- [d1s0] Ashley Cole (born 20 December 1980) is an English professional footballer who plays as a left-back for Los Angeles Galaxy in Major League Soccer.
- [d1s1]  Cole is considered by many critics and fellow professional players as one of the best defenders of his generation, and by some, for the better part of his career, as the best left-back in the world.

**d2: Daniel Gonzalez (Argentine footballer)**

- [d2s0] Daniel González is a retired Argentine association football goalkeeper who played professionally in Argentina and the United States.
- [d2s1]  He is the goalkeeper coach for Los Angeles Galaxy II, the reserve team for Major League Soccer's Los Angeles Galaxy

**d3: MLS Cup 2005**

- [d3s0] MLS Cup 2005, the 10th edition of Major League Soccer's championship match, was played between the New England Revolution and the Los Angeles Galaxy to decide the champion of the 2005 season.
- [d3s1]  The game was played at Pizza Hut Park in Frisco, Texas on November 13, 2005.
- [d3s2]  In a rematch of MLS Cup 2002, the Los Angeles Galaxy again beat the New England Revolution 1–0 in overtime, this time on a goal from Guillermo Ramírez.

**d4: 2008 Colorado Rapids season**

- [d4s0] The 2008 Colorado Rapids season was the thirteenth season of the team's existence.
- [d4s1]  Colorado began their season with 4-0 victory over the Los Angeles Galaxy and ended a 1-1 draw against Real Salt Lake.
- [d4s2]  They finished 4th in the Western Conference and 9th overall, 1 point behind the New York Red Bulls for the final Wild Card Playoff spot.
- [d4s3]  In the US Open Cup Qualifying, Colorado defeated the Los Angeles Galaxy 1-0 before losing in Kansas City in a penalty shootout.

**d5: Puerto Rico MLS-USL Challenge**

- [d5s0] The Puerto Rico USL-MLS Challenge was a preseason invitational football tournament featuring the host club Puerto Rico Islanders, two clubs from Major League Soccer and a USL First Division club.
- [d5s1]  The tournament was played in Juan Ramón Loubriel Stadium in Bayamon, Puerto Rico.
- [d5s2]  The first edition features the MLS clubs: Los Angeles Galaxy and F.C. Dallas, and USL clubs: Puerto Rico Islanders and Rochester Rhinos.
- [d5s3]  Los Angeles Galaxy won the tournament after 2-1 win over the Puerto Rico Islanders.
- [d5s4]  The tournament was again celebrated in 2009 featuring only a match between MLS club D.C. United and the Puerto Rico Islanders.
- [d5s5]  D.C. United won the tournament after a 2-1 win.

**d6: Promise This**

- [d6s0] "Promise This" is a song by English recording artist Cheryl Cole, taken from her second studio album "Messy Little Raindrops".
- [d6s1]  It was released in the United Kingdom and Ireland as the album's lead single on 24 October 2010 by Fascination Records.
- [d6s2]  The up-tempo dance-pop song was written by American songwriter Priscilla Renea Hamilton, British music producer Wayne Wilkins, and Christopher Jackson and produced by Wilkins.
- [d6s3]  The lyrics to "Promise This" reference Cole's personal life and relationships, as well as incorporating the French language.
- [d6s4]  The single's release came in the aftermath of a public divorce from footballer Ashley Cole, as well as a life-threatening battle with malaria.

**d7: Sports in Los Angeles**

- [d7s0] The Los Angeles metropolitan area is home to several professional and collegiate sports teams.
- [d7s1]  The Greater Los Angeles Area has nine major league professional teams: the Anaheim Ducks, the Los Angeles Angels, the Los Angeles Chargers, the Los Angeles Clippers, the Los Angeles Dodgers, LA Galaxy, the Los Angeles Kings, the Los Angeles Lakers, and the Los Angeles Rams.
- [d7s2]  Los Angeles FC will begin play as the area's tenth major team in 2018.
- [d7s3]  USC Trojans football, UCLA Bruins men's basketball, USC Trojans baseball, USC Trojans track & field, and Cal State Fullerton Titans baseball are all historically premier organizations in college sports.
- [d7s4]  Other major sports teams include UCLA Bruins Football, Los Angeles Sparks, Pepperdine Waves baseball, and formerly the Los Angeles Raiders and Los Angeles Aztecs.
- [d7s5]  Between them, these Los Angeles area sports teams have won a combined 105 Championship Titles.
- [d7s6]  Los Angeles area colleges have produced upwards of 200 National Championship Teams, primarily from USC Trojans and UCLA Bruins of the Pac-12 Conference.
- [d7s7]  The 1932 and 1984 Summer Olympics were held in Los Angeles.
- [d7s8]  In 2028 the city will host the Olympics for a third time.

**d8: Harut Karapetyan**

- [d8s0] Harutyun Karapetyan (born 7 April 1972) is an Armenian former professional footballer who played as a forward in the MLS for Los Angeles Galaxy, San Jose Earthquakes and Tampa Bay Mutiny.
- [d8s1]  Karapetyan holds the record for the fastest hat-trick in MLS history, scoring one in five minutes in June 1998, while playing for the Los Angeles Galaxy against the Dallas Burn; the Galaxy eventually won the match 8–1.

**d9: Messy Little Raindrops**

- [d9s0] Messy Little Raindrops is the second studio album by British recording artist Cheryl Cole, released on 29 October 2010 by Fascination Records.
- [d9s1]  The project is the follow-up to Cole's multi-platinum debut solo album "3 Words" (2009), following seven successful years as a member of girl group Girls Aloud.
- [d9s2]  Recorded in Los Angeles and London, Cole mainly worked with Wayne Wilkins, who previously produced Cole's number one debut single "Fight for This Love".

**d10: Baggio Hušidić**

- [d10s0] Adis "Baggio" Hušidić (born 19 May 1987) is a Bosnian-American footballer who plays for Los Angeles Galaxy in Major League Soccer.
- [d10s1]  A dynamic, hard-working, intelligent, and versatile player, with good distribution and offensive capabilities, he is capable of playing in any midfield position, and has also been deployed as a left-back.

## 30. hotpotqa_5ae64a2155429908198fa575

原位置：`train` 第 240 题 · 全局第 240 题 · `sample_id: hotpotqa_5ae64a2155429908198fa575`

Question: What movie starring Ellen Page was directed by Jason Reitman and written by Diablo Cody, premiered at the 2007 Toronto International Film Festival?

Note: 条件过多，按照旧的拆分方式，让模型可以先回答部分答案

Type: bridge · fallback: False · SFT snapshots: 6

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | movie starring Ellen Page that was directed by Jason Reitman and written by Diablo Cody | False | [] | Juno | [["d10s0", "d10s1"], ["d10s0", "d5s3"]] | context |
| u2 | movie starring Ellen Page, directed by Jason Reitman and written by Diablo Cody, that premiered at the 2007 Toronto International Film Festival, given {u1} | True | ["u1"] | Juno | [["d10s4"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | movie starring Ellen Page that was directed by Jason Reitman and written by Diablo Cody | False | [] | Juno | [['d10s0', 'd10s1'], ['d10s0', 'd5s3']] |
| u2 | movie starring Ellen Page, directed by Jason Reitman and written by Diablo Cody, that premiered at the 2007 Toronto International Film Festival, given {u1} | True | ['u1'] | Juno | [['d10s4']] |

### Source documents (reference only)

**d1: Passenger Side**

- [d1s0] Passenger Side is a 2009 drama film written and directed by Matthew Bissonnette and produced by Corey Marr.
- [d1s1]  It stars Adam Scott, Joel Bissonnette and Robin Tunney.
- [d1s2]  The film premiered at the 2009 Los Angeles Film Festival before screening at numerous film festivals worldwide including the Toronto International Film Festival, BFI London Film Festival, and Whistler Film Festival.
- [d1s3]  The film won the Citytv Award for Best Canadian Feature at the Edmonton International Film Festival and was named to "Canada's Top Ten" films of 2009 by the Toronto International Film Festival.

**d2: Mouth to Mouth (2005 British film)**

- [d2s0] Mouth to Mouth is a 2005 drama starring Ellen Page.
- [d2s1]  The first feature film written and directed by Canadian-born Alison Murray, it won the Grand Chameleon award at the 2005 Brooklyn International Film Festival.
- [d2s2]  It was shot on location in England, France, Germany and Portugal.

**d3: Labor Day (film)**

- [d3s0] Labor Day is a 2013 American drama film based on the 2009 novel of the same name by Joyce Maynard.
- [d3s1]  Directed by Jason Reitman, the film stars Kate Winslet and Josh Brolin.
- [d3s2]  The film was co-produced by Paramount Pictures and Indian Paintbrush, premiering at the Telluride Film Festival on August 29, 2013, and was a Special Presentation at the 2013 Toronto International Film Festival.
- [d3s3]  The film was released in the United States on January 31, 2014.

**d4: Jennifer's Body**

- [d4s0] Jennifer's Body is a 2009 supernatural horror black comedy film written by Diablo Cody and directed by Karyn Kusama.
- [d4s1]  The film stars Megan Fox, Amanda Seyfried, Johnny Simmons, and Adam Brody.
- [d4s2]  Fox portrays a demonically possessed high school girl who kills her male classmates, with her best friend striving to stop her.
- [d4s3]  The film premiered at the 2009 Toronto International Film Festival and was released in the United States and Canada on September 18, 2009.
- [d4s4]  The title is a reference to the song of the same name by alternative rock band Hole on their album "Live Through This".
- [d4s5]  As a tie-in to the film, Boom!
- [d4s6]  Studios produced a "Jennifer's Body" graphic novel, released in August 2009.

**d5: Ellen Page**

- [d5s0] Ellen Grace Philpotts-Page (born February 21, 1987), known professionally as Ellen Page, is a Canadian actress.
- [d5s1]  Her career began with roles in Canadian television shows including "Pit Pony", "Trailer Park Boys", and "ReGenesis".
- [d5s2]  Page starred in the 2005 drama "Hard Candy", for which she won the Austin Film Critics Association's Award for Best Actress.
- [d5s3]  Her breakthrough role was the title character in Jason Reitman's comedy film "Juno" (2007), for which she received nominations for Academy Award, BAFTA, Golden Globe and Screen Actors Guild Award for Best Actress, and won awards including the Independent Spirit Award, MTV Movie Award and Teen Choice Award for Best Actress Comedy.

**d6: The Sun Also Rises (2007 film)**

- [d6s0] The Sun Also Rises () is a 2007 film directed, produced and co-written by Chinese director Jiang Wen starring Joan Chen, Anthony Wong, Jaycee Chan, and Jiang Wen himself.
- [d6s1]  This movie is the polyptych of interconnected stories in different time-zones, shifting between a Yunnan village, a campus, and the Gobi Desert.
- [d6s2]  This movie was screened in competition at the Venice International Film Festival and nominated for Golden Lion but lost to Ang Lee's historical thriller "Lust, Caution".
- [d6s3]  This film also premiered at the 2007 Toronto International Film Festival on September 9, and was nominated for Achievement in Cinematography at the 2007 Asia Pacific Screen Awards.

**d7: List of accolades received by Up in the Air**

- [d7s0] "Up in the Air" is a 2009 American comedy-drama film directed by Jason Reitman and co-written by Reitman and Sheldon Turner.
- [d7s1]  The film is an adaptation of the eponymous 2001 novel by Walter Kirn.
- [d7s2]  "Up in the Air" was screened as a "sneak preview" at the Telluride Film Festival on September 6, 2009, before its world premiere at the Toronto International Film Festival on September 12, 2009.
- [d7s3]  "Up in the Air" was released in the United States on December 4, 2009; playing on 15 screens in its first weekend, it grossed over $1.1 million.
- [d7s4]  The film opened nationwide on December 23, 2009, earning over $11 million its first weekend in wide release.
- [d7s5]  The film earned $79 million over 18 weeks in the United States and Canada, with an additional $83 million in overseas markets.

**d8: Tully (2018 film)**

- [d8s0] Tully is an upcoming American comedy-drama film directed by Jason Reitman and written by Diablo Cody.
- [d8s1]  The film stars Charlize Theron, Mackenzie Davis, Mark Duplass and Ron Livingston.
- [d8s2]  The film is scheduled to be released on April 20, 2018 by Focus Features.

**d9: Young Adult (film)**

- [d9s0] Young Adult is a 2011 American comedy-drama film directed by Jason Reitman, from a screenplay written by Diablo Cody, and starring Charlize Theron.
- [d9s1]  Reitman and Cody worked together previously on "Juno" (2007).
- [d9s2]  "Young Adult" began a limited release on December 9, 2011, before expanding to a wide release on December 16.
- [d9s3]  It received generally positive reviews.

**d10: Juno (film)**

- [d10s0] Juno is a 2007 American coming of age comedy-drama independent film directed by Jason Reitman and written by Diablo Cody.
- [d10s1]  Ellen Page stars as the title character, an independent-minded teenager confronting an unplanned pregnancy and the subsequent events that put pressures of adult life onto her.
- [d10s2]  Michael Cera, Jennifer Garner, Jason Bateman, Allison Janney and J. K. Simmons also star.
- [d10s3]  Filming spanned from early February to March 2007 in Vancouver, British Columbia.
- [d10s4]  It premiered on September 8 at the 2007 Toronto International Film Festival, receiving a standing ovation.
