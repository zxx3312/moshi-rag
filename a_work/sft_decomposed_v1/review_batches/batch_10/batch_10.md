# batch_10：人工审查（30 题）

全局题号 271–300；train 0 题 / dev 30 题。原训练/验证归属保持不变。

[返回分配索引](../README.md) · [完整对比报告](../../comparison_human.md)

**原则：新旧单元都合理时保留拆题器拆法，人工监督向新单元对齐。** 本批已由用户审核，按最新 Note 完成调整。

审查人：________　完成日期：________

本批已依据人工 Note 调整；原始拆题保存在 JSON 的 `raw_decomposition`。下方 Adjusted units 为当前标注，旧 gold 仅供参照。标注已更新；逐时刻 SFT 快照尚未重建。

## 1. 2wikimultihopqa_f618d408084c11ebbd56ac1f6bf848b6

原位置：`dev` 第 28 题 · 全局第 271 题 · `sample_id: 2wikimultihopqa_f618d408084c11ebbd56ac1f6bf848b6`

Question: Were both Andreas (Comics) and Albert Üksip, born in the same place?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | birthplace of Andreas (Comics) | False | [] | Weißenfels | [["d7s0"]] | context |
| u2 | birthplace of Albert Üksip | False | [] | Narva | [["d4s0"]] | context |
| u3 | whether Andreas (Comics) and Albert Üksip were born in the same place | True | ["u1", "u2"] | no | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | place of birth of Andreas (comics) | False | [] | Weißenfels | [['d7s0']] |
| u2 | place of birth of Albert Üksip | False | [] | Narva | [['d4s0']] |
| u3 | whether Andreas (comics) and Albert Üksip were born in the same place | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Andy Lanning**

- [d1s0] Andy Lanning( born 21 November 1963) is a British comic book writer and inker, known for his work for Marvel Comics and DC Comics, and for his collaboration with Dan Abnett.

**d2: Greg Rucka**

- [d2s0] Gregory Rucka is an American comic book writer and novelist, known for his work on such comics as" Action ComicsBatwomanDetective Comics", and the miniseries" Superman: World of New Krypton" for DC Comics, and for novels such as his" Atticus Kodiak" series.

**d3: Hieronymus Payer**

- [d3s0] Hieronymus Payer( 13 February 1787 in Vienna- Meidling; died 17 August 1845 in the same place) was an Austrian composer and pianist.

**d4: Albert Üksip**

- [d4s0] Albert Üksip( 8 December 1886 in Narva – 10 August 1966 in Tallinn) was an Estonian actor, botanist and translator.

**d5: Alfred Oppenheim (chemist)**

- [d5s0] Alfred Oppenheim( 3 November 1878 in Berlin – 14 May 1943 at the same place) was a German chemist and gas mantle manufacturer.

**d6: Klaus Janson**

- [d6s0] Klaus Janson( born January 23, 1952) is a German- born American comics artist, working regularly for Marvel Comics and DC Comics and sporadically for independent companies.
- [d6s1] While he is best known as an inker, Janson has frequently worked as a penciller and colorist.

**d7: Andreas (comics)**

- [d7s0] Andreas, pen name for" Andreas Martens", born January 3, 1951 in Weißenfels( Germany).
- [d7s1] Martens studied in Düsseldorf at the Academy of Fine Arts and at the St. Luc comics school in Belgium, assisting Eddy Paape on Udolfo, before relocating to France.
- [d7s2] He made his debut in the magazines( À suivre), Le Journal de Tintin and Heavy Metal.
- [d7s3] In 2001 he won de Prix Bonnet d’âne at the comic festival Quai des Bulles in Saint- Malo( France) for his entire oeuvre.
- [d7s4] This includes that he may draw the poster for the next festival.
- [d7s5] His genre series include Arq, Cromwell Stone, Cyrrus, Rork and its spin- off, Capricorne, as well as a number of single works such as La Caverne du Souvenir( The Cave of Memory), Coutoo, Dérives( Adrift), Aztèques, and Révélations Posthumes( Posthumous Revelations).

**d8: André Roche**

- [d8s0] André Roche, born in 1952 in France, is an artist, an illustrator and an author of comics and children's books.

**d9: Peter Dirck Keyser**

- [d9s0] Peter Dirck Keyser( born in Philadelphia, Pennsylvania, 8 February 1835; died same place, 8 March 1897) was a United States ophthalmologist.

**d10: Arvell Jones**

- [d10s0] Arvell Jones( whose earliest work is billed Arvell Malcolm Jones) is an American comics artist best known for his work for Marvel Comics, and for DC Comics and its imprint Milestone Media.

## 2. hotpotqa_5a745a8755429979e288291e

原位置：`dev` 第 29 题 · 全局第 272 题 · `sample_id: hotpotqa_5a745a8755429979e288291e`

Question: Wellesley College and Vanderbilt University are both what?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。如果没有其他明确相同的类别，保留旧答案 private 及别名，并要求两方证据。

Type: comparison · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 按 Note 保留 private 及已有别名作为标注目标，结论必须由两方类别证据支持；不声称这是自然语言中唯一可能的共同类别。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | type of Wellesley College | False | [] | private women's liberal arts college | [["d10s0"]] | context |
| u2 | type of Vanderbilt University | False | [] | private research university | [["d7s0"]] | context |
| u3 | common classification of Wellesley College and Vanderbilt University | True | ["u1", "u2"] | private | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | type of institution Wellesley College is | False | [] | private women's liberal arts college | [['d10s0']] |
| u2 | type of institution Vanderbilt University is | False | [] | private research university | [['d7s0']] |
| u3 | what Wellesley College and Vanderbilt University both are | True | ['u1', 'u2'] | private | [[]] |

### Source documents (reference only)

**d1: Wellesley College Botanic Gardens**

- [d1s0] The Wellesley College Botanic Gardens (22 acres) are botanical gardens located on the campus of Wellesley College in Wellesley, Massachusetts.
- [d1s1]  They are open daily without charge.

**d2: Vanderbilt University School of Nursing**

- [d2s0] Vanderbilt University School of Nursing (VUSN) is one of the graduate schools of Vanderbilt University, located in Nashville, Tennessee.
- [d2s1]  VUSN enjoys a close relationship with its university parent and with the separate nonprofit Vanderbilt University Medical Center, known for its highly acclaimed teaching hospital and groundbreaking efforts in electronic medical records.
- [d2s2]  The School of Nursing is ranked, along with the Vanderbilt University School of Medicine, in the top 20 in the U.S. News & World Report rankings.

**d3: Whitin Observatory**

- [d3s0] Whitin Observatory is an astronomical observatory owned and operated by Wellesley College.
- [d3s1]  Built in 1900, with additions in 1906, 1967, and 20102011, it is located in Wellesley, Massachusetts and named after Wellesley College trustee Mrs. John Crane Whitin (Sarah Elizabeth Whitin) of Whitinsville, who donated the funds for the observatory.
- [d3s2]  Astronomer Sarah Frances Whiting was the first director of the new Wellesley College Astronomy Department.

**d4: 2011 Vanderbilt Commodores football team**

- [d4s0] The 2011 Vanderbilt Commodores football team represented Vanderbilt University during the 2011 NCAA Division I FBS football season.
- [d4s1]  The Commodores played their seven home games at Vanderbilt Stadium at Dudley Field in Nashville, Tennessee, which has been Vanderbilt football's home stadium since 1922.
- [d4s2]  The team's head coach was James Franklin, who was in his first year at Vanderbilt.
- [d4s3]  Hired at Vanderbilt on December 17, 2010, he was previously the offensive coordinator and "head coach in waiting" at the University of Maryland.
- [d4s4]  Vanderbilt has been a member of the Southeastern Conference (SEC) since the league's inception in 1932, and has participated in the conference's Eastern Division since its formation for the 1992 season.
- [d4s5]  Vanderbilt completed the 2011 regular season with an overall record of 6–6 and a mark of 2–6 in conference play, finishing in a tie with Kentucky for fourth place in the SEC East.
- [d4s6]  They were invited to the Liberty Bowl where they were defeated by Cincinnati 24–31 to finish the season 6–7.
- [d4s7]  2011.
- [d4s8]  The seniors of the 2011 Vanderbilt football team became the first class in program history to qualify for two bowl game's while at the school.
- [d4s9]  Vanderbilt had only been to bowls in 1955 VS Auburn, 1974 VS Texas Tech, 1982 VS Air Force, and 2008 VS Boston College.

**d5: 2012 Vanderbilt Commodores football team**

- [d5s0] The 2012 Vanderbilt Commodores football team represented Vanderbilt University during the 2012 NCAA Division I FBS football season.
- [d5s1]  (variously "VU" "Vandy" Vanderbilt "Dores") The Commodores played their six home games at Vanderbilt Stadium at Dudley Field in Nashville, Tennessee, which has been Vanderbilt football's home stadium since 1922.
- [d5s2]  The team's head coach was James Franklin, who is in his second year at Vanderbilt.
- [d5s3]  Vanderbilt has been a member of the Southeastern Conference (SEC) since the league's inception in 1932, and has participated in the conference's Eastern Division since its formation for the 1992 season.
- [d5s4]  On November 11, 2012 Vandy became bowl eligible in back to back years for the first time in its 123-year football history.
- [d5s5]  This was the first time since 1935 that Vandy won five SEC games in a year and the first time in 30 years that they won at home against Tennessee.
- [d5s6]  Vanderbilt finished the year with the longest current SEC winning streak.
- [d5s7]  For the first time since 1948, Vanderbilt finished the season with a top 25 ranking.

**d6: Vanderbilt University School of Medicine**

- [d6s0] Vanderbilt University School of Medicine is a medical school located in Nashville, Tennessee.
- [d6s1]  Located in the Vanderbilt University Medical Center on the southeastern side of the Vanderbilt University campus, the School of Medicine claims two Nobel laureates: Earl Wilbur Sutherland, Jr., in 1971, for his discovery of the metabolic regulating compound cyclic AMP, and Stanley Cohen, in 1986, for his discovery with a colleague of epidermal growth factor.

**d7: Vanderbilt University**

- [d7s0] Vanderbilt University (also known informally as Vandy) is a private research university located in Nashville, Tennessee.
- [d7s1]  Founded in 1873, it was named in honor of shipping and rail magnate Cornelius Vanderbilt, who provided the school its initial $1 million endowment despite having never been to the South.
- [d7s2]  Vanderbilt hoped that his gift and the greater work of the university would help to heal the sectional wounds inflicted by the Civil War.

**d8: Vanderbilt University Law School**

- [d8s0] Vanderbilt University Law School (also known as Vanderbilt Law School or VLS) is a graduate school of Vanderbilt University.
- [d8s1]  Established in 1874, it is one of the oldest law schools in the southern United States.
- [d8s2]  Vanderbilt Law has consistently ranked among the top 20 law schools in the nation, and is currently ranked 17th in the 2018 edition of "U.S. News & World Report".
- [d8s3]  Vanderbilt Law School enrolls approximately 640 students, with each entering Juris Doctor class consisting of approximately 175 students.

**d9: Alan Schechter**

- [d9s0] Alan Schechter (born 1936) is a Professor Emeritus of Political Science at Wellesley College in Massachusetts.
- [d9s1]  He was educated at Amherst College, where he received his AB, and at Columbia University, where he earned his PhD.
- [d9s2]  He is a distinguished and award-winning political scientist.
- [d9s3]  He was also Hillary Rodham's advisor during her years at Wellesley College and supervised her senior thesis; Susan Estrich's book "The Case for Hillary Clinton" mentions her experience also writing an honors thesis for Professor Schechter (at a different time).
- [d9s4]  He remains involved with the college, running the Wellesley in Washington internship program, in which Rodham participated as a student and which continues to send approximately twenty women to Washington for internships each summer.
- [d9s5]  Professor Schechter is the former Chairman, Vice-Chairman, and member of the J. William Fulbright Foreign Scholarship Board (Fulbright Program), a Presidential appointment.

**d10: Wellesley College**

- [d10s0] Wellesley College is a private women's liberal arts college located west of Boston in the town of Wellesley, Massachusetts, United States.
- [d10s1]  Founded in 1870 by Henry and Pauline Durant, it is a member of the original Seven Sisters Colleges.
- [d10s2]  Wellesley is home to 56 departmental and interdepartmental majors spanning the liberal arts, as well as over 150 student clubs and organizations.
- [d10s3]  The college is also known for allowing its students to cross-register at Massachusetts Institute of Technology, Brandeis University, Babson College and Franklin W. Olin College of Engineering.
- [d10s4]  Wellesley athletes compete in the NCAA Division III New England Women's and Men's Athletic Conference.

## 3. hotpotqa_5a75dc7a5542992d0ec06004

原位置：`dev` 第 30 题 · 全局第 273 题 · `sample_id: hotpotqa_5a75dc7a5542992d0ec06004`

Question: What is the term for the service provided by HCL Technologies involving discovery, interpretation, and communication of patterns in data?

Note: 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | term for the discovery, interpretation, and communication of patterns in data | False | [] | Analytics | [["d2s0"]] | context |
| u2 | service provided by HCL Technologies involving the discovery, interpretation, and communication of patterns in data, given {u1} | True | ["u1"] | Analytics | [["d9s4"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | term for the discovery, interpretation, and communication of patterns in data | False | [] | Analytics | [['d2s0']] |
| u2 | service provided by HCL Technologies involving the discovery, interpretation, and communication of patterns in data, given {u1} | True | ['u1'] | Analytics | [['d9s4']] |

### Source documents (reference only)

**d1: C Vijayakumar**

- [d1s0] C Vijayakumar (CVK or Vijay) is the President & Chief Executive Officer of HCL Technologies, a US$ 7 billion global IT services company.

**d2: Analytics**

- [d2s0] Analytics is the discovery, interpretation, and communication of meaningful patterns in data.
- [d2s1]  Especially valuable in areas rich with recorded information, analytics relies on the simultaneous application of statistics, computer programming and operations research to quantify performance.

**d3: Data mining**

- [d3s0] Data mining is the computing process of discovering patterns in large data sets involving methods at the intersection of machine learning, statistics, and database systems.
- [d3s1]  An essential process where intelligent methods are applied to extract data patterns.
- [d3s2]  It is an interdisciplinary subfield of computer science.
- [d3s3]  The overall goal of the data mining process is to extract information from a data set and transform it into an understandable structure for further use.
- [d3s4]  Aside from the raw analysis step, it involves database and data management aspects, data pre-processing, model and inference considerations, interestingness metrics, complexity considerations, post-processing of discovered structures, visualization, and online updating.
- [d3s5]  Data mining is the analysis step of the "knowledge discovery in databases" process, or KDD.

**d4: Content analysis**

- [d4s0] Content analysis is a research method for studying communication artifacts.
- [d4s1]  Social scientists use content analysis to quantify patterns in communication.
- [d4s2]  Practices and philosophies of content analysis vary between scholarly communities.
- [d4s3]  They all involve systematic reading or observation of texts or artifacts which are assigned labels (sometimes called codes) to indicate the presence of interesting, meaningful patterns .
- [d4s4]  After labeling a large set of texts, a researcher is able to statistically estimate the proportions of patterns in the texts, as well as correlations between patterns.
- [d4s5]  Computers are increasingly used in content analysis.
- [d4s6]  Popular qualitative data analysis programs provide efficient work-flow and data management tools for labeling.
- [d4s7]  Simple computational techniques can provide descriptive data such as word frequencies and document lengths.
- [d4s8]  Machine learning classifiers can greatly increase the number of texts which can be labeled, but the scientific utility of doing so is a matter of debate.

**d5: HCL ISD**

- [d5s0] HCL Technologies Infrastructure Services Division (HCL ISD) is a global IT infrastructure management services company.
- [d5s1]  It is a line of business of HCL Technologies.

**d6: Carbon nanotubes for water transport**

- [d6s0] Water shortages have become an increasingly pressing concern recently and with recent predictions of a high probability of the current drought turning into a megadrought occurring in the western United States, technologies involving water treatment and processing need to improve.
- [d6s1]  Carbon nanotubes (CNT) have been the subject of extensive studies because they demonstrate a range of unique properties that existing technologies lack.
- [d6s2]  For example, carbon nanotube membranes can demonstrate higher water flux with lower energy than current membranes.
- [d6s3]  These membranes can also filter out particles that are too small for conventional systems which can lead to better water purification techniques and less waste.
- [d6s4]  The largest obstacle facing CNT is processing as it is difficult to produce them in the large quantities that most of these technologies will require.

**d7: HCL Axon**

- [d7s0] HCL AXON is a UK-based business transformation consultancy which sells its services to customers using SAP and Oracle as their Enterprise Resource Planning system modeling tools.
- [d7s1]  Previously listed on the London Stock Exchange, and a FTSE 250 Index constituent, the company has been a subsidiary of Indian outsourcing firm HCL Technologies since December 2008, after the reverse merger of Axon Group plc and HCL SAP practice.

**d8: IT City, Lucknow**

- [d8s0] The Single City, Lucknow is part of the mega CG City project envisioned by the government of Uttar Pradesh and is conceptualized as a sustainable technology hub with clean power and balanced environment.
- [d8s1]  It is being built on a PPP model in partnership with HCL Technologies.
- [d8s2]  It is the second major investment by an IT Company in Lucknow, the first being Tata Consultancy Services which has its TCS Awadh Campus present in the city in which thousands of engineers are already working.
- [d8s3]  HCL has begun its operations in the city and training for the first batch of engineers has already been completed.
- [d8s4]  The project will be commissioned by October 2016.
- [d8s5]  Uttar Pradesh government has established Rs 1,500-crore Information Technology (IT) city over 100 acres in Lucknow with the concept of “Walk to Work” on Lucknow-Sultanpur Road.
- [d8s6]  About 100 acres of CG city was allotted to IT and ITeS companies which will also include a hi-tech skill development centre which can train more than 5000 people.
- [d8s7]  The remaining 400 acres is intended for Indian Institute of Information Technology (IIIT) and Medanta-Avadh super speciality hospital.

**d9: HCL Technologies**

- [d9s0] HCL Technologies Limited is an Indian multinational IT services company, headquartered in Noida, Uttar Pradesh, India.
- [d9s1]  It is a subsidiary of HCL Enterprise.
- [d9s2]  Originally a research and development division of HCL, it emerged as an independent company in 1991 when HCL ventured into the software services business.
- [d9s3]  HCL Technologies (the abbreviation of Hindustan Computers Limited) offers services including IT consulting, enterprise transformation, remote infrastructure management, engineering and R&D, and business process outsourcing (BPO).
- [d9s4]  HCL also provides services such as DRYiCE, Cybersecurity and Digital & Analytics.

**d10: Kiran Nadar**

- [d10s0] Kiran Shiv Nadar is an Indian art collector and philanthropist.
- [d10s1]  She is the wife of Shiv Nadar, the founder of HCL Technologies, and is a trustee of the Shiv Nadar Foundation and the founder of Kiran Nadar Museum of Art.

## 4. hotpotqa_5a7755e05542993735360237

原位置：`dev` 第 31 题 · 全局第 274 题 · `sample_id: hotpotqa_5a7755e05542993735360237`

Question: Which computer animated film was released first, Khan Kluay or A Christmas Carol starring Jim Carrey?

Note: 改 comparison，context 只给年份，统一为 release year，保留三单元。

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 改 comparison，context 只给年份，统一为 release year，保留三单元。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | release year of Khan Kluay | False | [] | 2006 | [["d7s0"], ["d4s2"], ["d10s3"]] | context |
| u2 | release year of A Christmas Carol starring Jim Carrey | False | [] | 2009 | [["d6s0", "d6s1"]] | context |
| u3 | which film was released first | True | ["u1", "u2"] | Khan Kluay | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | release year of the film Khan Kluay | False | [] | 2006 | [['d7s0'], ['d4s2'], ['d10s3']] |
| u2 | release year of the film A Christmas Carol starring Jim Carrey | False | [] | 2009 | [['d6s0', 'd6s1']] |
| u3 | which of Khan Kluay and A Christmas Carol starring Jim Carrey was released first | True | ['u1', 'u2'] | Khan Kluay | [[]] |

### Source documents (reference only)

**d1: Ace Ventura: Pet Detective**

- [d1s0] Ace Ventura: Pet Detective (or simply Ace Ventura, or also simply Pet Detective) is a 1994 American comedy film directed by Tom Shadyac, and co-written by and starring Jim Carrey.
- [d1s1]  It was developed by the film's original writer, Jack Bernstein, and co-producer, Bob Israel, for almost six years.
- [d1s2]  The film co-stars Courteney Cox, Tone Lōc, Sean Young and former Miami Dolphins quarterback Dan Marino.
- [d1s3]  In the film, Carrey plays Ace Ventura, an animal detective who is tasked with finding the Miami Dolphins' mascot that was abducted.
- [d1s4]  The film features a cameo appearance from death metal band Cannibal Corpse.

**d2: Khan Kluay (franchise)**

- [d2s0] Khan Kluay (Thai: ก้านกล้วย ; rtgs: Kan Kluai ;  ] ) is a Thai computer-animated feature film set during Ayutthaya-era Siam about an elephant who wanders away from his mother and eventually becomes the war elephant for King Naresuan.
- [d2s1]  It is based on "Chao Praya Prab Hongsawadee" by Ariya Jintapanichkarn.
- [d2s2]  A PC game called Khankluay:The Adventure has also been released in Thailand.

**d3: Khan Kluay 2**

- [d3s0] Khan Kluay 2 is a three-dimensional animated movie from Thailand, directed by Taweelap Srivuthivong and released in 2009.
- [d3s1]  It is the sequel to "Khan Kluay" and follows the further adventures of the war elephant of King Naresuan the Great.
- [d3s2]  It is set during the war between Ayutthaya and Bago.
- [d3s3]  Its theme is the need to protect family and country.
- [d3s4]  The movie grossed 79 million baht.

**d4: Jumbo (film)**

- [d4s0] Jumbo is a 2008 Bollywood animation film directed by Kompin Kemgumnird, produced by Percept Picture Company and features the voices of Akshay Kumar, Lara Dutta, Dimple Kapadia, Rajpal Yadav, Asrani, Gulshan Grover, and Yuvraj Singh.
- [d4s1] It has Yashveer Bains as lead role of Jumbo.
- [d4s2]  The film is an official remake/redubbing of the 2006 Thai film "Khan Kluay".
- [d4s3]  The film was dubbed and released in Hindi and the creative direction on the Hindi film was by Mayur Puri.
- [d4s4]  "Jumbo" released worldwide on Christmas Day 2008, but was met with poor critical reviews and turned out to be one of the biggest box office disasters of the year.
- [d4s5]  In 2011 A direct to DVD sequel titled Jumbo 2: The Return of the Big Elephant was released.

**d5: Rubberface**

- [d5s0] Rubberface is a 1981 television film made for CBC television starring Jim Carrey.
- [d5s1]  Originally titled "Introducing Janet", it was changed to "Rubberface" for the video release after Carrey's success.

**d6: A Christmas Carol (2009 film)**

- [d6s0] A Christmas Carol is a 2009 American 3D computer animated motion-capture fantasy film written and directed by Robert Zemeckis.
- [d6s1]  It is an adaptation of the Charles Dickens story of the same name and stars Jim Carrey in a multitude of roles, including Ebenezer Scrooge as a young, middle-aged, and old man, and the three ghosts who haunt Scrooge.
- [d6s2]  The film also features supporting roles done by Gary Oldman, Colin Firth, Bob Hoskins, Robin Wright, and Cary Elwes.

**d7: Khan Kluay**

- [d7s0] Khan Kluay (Thai: ก้านกล้วย) is a 2006 Thai 3D computer-animated Action adventure comedy family feature film set during Ayutthaya-era Siam about a Thai elephant who wanders away from his mother and eventually becomes the war elephant for King Naresuan.
- [d7s1]  It is based on "Chao Praya Prab Hongsawadee" by Ariya Jintapanichkarn.
- [d7s2]  It was officially released as Jumbo in India and The Blue Elephant in the United States.
- [d7s3]  There is a sequel to this movie, known as "Khan Kluay 2".
- [d7s4]  This movie is about Khan Kluay's two elephant children, another attack by the Hongsawadi (Burmese), and struggling whether to live with his wife or fight the Burmese.

**d8: God Tussi Great Ho**

- [d8s0] God Tussi Great Ho (English: "God you are Great" ) is a 2008 Indian fantasy comedy film, written and directed by Rumi Jaffery and starring Salman Khan, Priyanka Chopra, Sohail Khan and Amitabh Bachchan in a friendly appearance.
- [d8s1]  It was released on 15 August 2008.
- [d8s2]  According to director Rohit Dhawan, the film is inspired from a village folk tale about a Brahmin, though most reviewers noted that the film's story-line has similarities with the 2003 Hollywood comedy "Bruce Almighty", starring Jim Carrey and Jennifer Aniston.
- [d8s3]  However the film bombed at the box office.

**d9: Me, Myself &amp; Irene**

- [d9s0] Me, Myself & Irene is a 2000 American black comedy film directed by the Farrelly brothers, and starring Jim Carrey and Renée Zellweger.
- [d9s1]  Chris Cooper, Robert Forster, Richard Jenkins, Daniel Greene, Anthony Anderson, Jerod Mixon and Mongo Brownlee co-star.
- [d9s2]  The film is about a Rhode Island state trooper named Charlie who, after years of continuously suppressing his rage and feelings, suffers a psychotic breakdown which results in a second personality, Hank.
- [d9s3]  This was also Carrey's first role in a 20th Century Fox film.

**d10: Kantana Group**

- [d10s0] Kantana Group Public Company Limited (Thai: บริษัท กันตนา กรุ๊ป จำกัด "bor-rí-sàt gan-dtà-năa gróop jam-gàt ") is a film and television production company based in Bangkok, Thailand.
- [d10s1]  It is one of Thailand's oldest and largest film studios.
- [d10s2]  The company's post-production facilities, including the joint-venture Oriental Post, are a major Asian hub for film processing and editing.
- [d10s3]  The company is also known for its animation work, which includes the 2006 feature film "Khan Kluay".

## 5. hotpotqa_5a77a8365542995d83181250

原位置：`dev` 第 32 题 · 全局第 275 题 · `sample_id: hotpotqa_5a77a8365542995d83181250`

Question: Gândul Mâței and KMFDM, are what type of musical organization?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | type of musical organization Gândul Mâței is | False | [] | band | [["d4s0"]] | context |
| u2 | type of musical organization KMFDM is | False | [] | band | [["d9s0"]] | context |
| u3 | what type of musical organization they are | True | ["u1", "u2"] | band | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | type of musical organization Gândul Mâței is | False | [] | band | [['d4s0']] |
| u2 | type of musical organization KMFDM is | False | [] | band | [['d9s0']] |
| u3 | type of musical organization shared by Gândul Mâței and KMFDM | True | ['u1', 'u2'] | band | [[]] |

### Source documents (reference only)

**d1: Cheryl Wilson**

- [d1s0] Cheryl Wilson is a session singer who has had multiple No. 1 dance songs on the UK "Billboard" chart and has performed with many notable artists including Celine Dion, R. Kelly, Alice Peacock, Mavis Staples, The Smashing Pumpkins, Bertie Higgins, Michael Bolton, Bill Withers, Peabo Bryson, David Foster, Josh Grobin, Enrique Iglesias, Nick Carter, KMFDM, Cameo, Rod Stewart, Ray Charles, Natalie Cole, Mel Torme, Spike Lee, Tony Bennett, Peter Cetera, and Martha Wash.
- [d1s1]  She has also sung in commercials for companies such as McDonald's and is a member of the Jazz & Contemporary Studies Faculty at Roosevelt University in Chicago.
- [d1s2]  She contributes vocals to Jim Warner's Chicago musical project, Akalibrio.
- [d1s3]  Her performance on the KMFDM song "Power" was described as "soul-mama vamping".

**d2: League of American Orchestras**

- [d2s0] The League of American Orchestras, formerly the American Symphony Orchestra League, is a North American Musical Organization consisting of a network of approximately 800 orchestras.
- [d2s1]  “Dedicated to helping orchestras meet the challenges of the twenty-first century,” the League consists of leading symphony and philharmonic orchestras, collegiate orchestras, community ensembles, and youth and student ensembles.
- [d2s2]  The only national organization devoted and focused on elevating the orchestra industry, the League was founded in 1942 and later chartered by Congress in 1962.
- [d2s3]  The League creates a network of all facets of the industry, including administrators, managers, board members, business partners, volunteers, and musicians.
- [d2s4]  Each year this organization presents two awards: the Gold Baton Award and the Helen M. Thompson Award.
- [d2s5]  The League affects the orchestral world through several outreach experiences, dedicated advocacy to music education and especially orchestral education, and maintaining and communicating a breadth of information and pertinent topics in publications.
- [d2s6]  It has also developed detailed antitrust policy and guidelines in order to comply with the landscape of the industry.
- [d2s7]  The League is a leading force in work on legislation regarding orchestras and support for the arts.

**d3: David W. Tucker**

- [d3s0] David W. Tucker (1929–2003) was a jazz trombonist, music educator, composer of band and orchestral music, record producer, and marching band arranger, most renowned as the director of the University of California Jazz Ensembles from 1969 until 1985.
- [d3s1]  Under his direction, the organization expanded to become the largest musical organization on the campus of the University of California, Berkeley, had an international reputation resulting from foreign tours, and sponsored the Pacific Coast Collegiate Jazz Festival.
- [d3s2]  Numerous student members of the organization have become renowned jazz musicians, composers, and music educators.

**d4: Gândul Mâței**

- [d4s0] Gândul Mâței (] , Translation: The cat's thought) is a Moldovan alternative rock band from Chișinău, formed in 1996.

**d5: Moldova are talent**

- [d5s0] Moldova are talent (in English: "Moldova got Talent" ) is a TV show which first aired on 17 October 2013.
- [d5s1]  The project is a franchise of Got Talent, developed by Simco Limited.
- [d5s2]  The hosts of the show are Adrian Ursu and Mircea Marco.
- [d5s3]  The judges are the Moldovan singer Tania Cerga, a Moldovan singer (vocalist of Gândul Mâței band), Prime TV star and presenter Nicu Țărnă and a well known Moldovan opera singer, Mihai Muntean.
- [d5s4]  The grand prize of first serie is 500,000 MDL.

**d6: Nicu Țărnă**

- [d6s0] Nicu Țărnă (born July 25, 1977 in Chișinău, Moldova) is a musician, actor, songwriter, showman, and TV presenter from Moldova.
- [d6s1]  He is the lead vocalist for the Moldovan alternative rock band Gândul Mâței.

**d7: Argonotes**

- [d7s0] Argonotes, the unofficial band of the Toronto Argonauts is an all volunteer organization committed to bringing quality musical entertainment and a "traditional football atmosphere" to all Argonauts home football games.
- [d7s1]  Comprising more than 50 musicians on most game days, Argonotes is the largest musical organization associated with the CFL.

**d8: Handel and Haydn Society**

- [d8s0] The Handel and Haydn Society, familiarly known as H+H, is an American chorus and period instrument orchestra based in Boston, Massachusetts.
- [d8s1]  Founded in 1815, it is the third oldest musical organization in the United States after the Stoughton Musical Society (founded in 1786) and the U.S. Marine Band (founded 1798), and the oldest continually performing arts organization in the United States.

**d9: KMFDM**

- [d9s0] KMFDM (originally Kein Mehrheit Für Die Mitleid, loosely translated by the band as "no pity for the majority") is an industrial band led by German multi-instrumentalist Sascha Konietzko, who founded the group in 1984 as a performance art project.

**d10: Stoughton Musical Society**

- [d10s0] Organized in 1786, the Stoughton Musical Society is America's oldest performing musical organization.
- [d10s1]  For over two centuries it has had many distinguished accomplishments.
- [d10s2]  In 1908, when incorporated under the laws of the Commonwealth of Massachusetts, the name was changed to Old Stoughton Musical Society and it has retained that designation.

## 6. hotpotqa_5a78f57a554299148911f9bf

原位置：`dev` 第 33 题 · 全局第 276 题 · `sample_id: hotpotqa_5a78f57a554299148911f9bf`

Question: For which Minneapolis-St. Paul area sports team did Zenon Konopka play? 

Note: 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | teams Zenon Konopka played for | False | [] | Mighty Ducks of Anaheim, Columbus Blue Jackets, Tampa Bay Lightning, New York Islanders, Ottawa Senators, Minnesota Wild and Buffalo Sabres | [["d3s1"]] | context |
| u2 | which of {u1} is a Minneapolis-St. Paul area sports team | True | ["u1"] | Minnesota Wild | [["d8s2", "d8s3"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | teams Zenon Konopka played for | False | [] | Mighty Ducks of Anaheim, Columbus Blue Jackets, Tampa Bay Lightning, New York Islanders, Ottawa Senators, Minnesota Wild and Buffalo Sabres | [['d3s1']] |
| u2 | which of {u1} is a Minneapolis-St. Paul area sports team | True | ['u1'] | Minnesota Wild | [['d8s2', 'd8s3']] |

### Source documents (reference only)

**d1: Prescott Drawbridge**

- [d1s0] The Prescott Drawbridge, also called the Point Douglas Drawbridge, is a steel girder bridge with a double-leaf bascule drawbridge section.
- [d1s1]  The roadbed of the drawbridge span is a steel grate.
- [d1s2]  The bridge carries U.S. 10 across the St. Croix River and connects Prescott, Wisconsin, with the Point Douglas park area of Denmark Township, Minnesota.
- [d1s3]  This is the only drawbridge in the Minneapolis-St.
- [d1s4] Paul area.
- [d1s5]  It was completed in 1990 and replaced a rare regional example of a Waddell & Harrington vertical-lift bridge completed in 1922 that operated as a toll bridge from 1923 to 1946.

**d2: Tom Barnard**

- [d2s0] Thomas 'Tom' Mark Paul Barnard (born November 7, 1951) is an American talk radio host and former voice-over talent.
- [d2s1]  He is currently the host of "The KQ92 Morning Show" from 5:40am to 10:00am on 92 KQRS and Tom Barnard Show on 105 The Ticket from 6:00pm to 7:00pm both broadcast in the Minneapolis-St.
- [d2s2]  Paul area.
- [d2s3]  The show on 105 The Ticket makes up the third hour of the "The Tom Barnard Podcast" known as "The Ticket" where the first two hours of the podcast is known as "The Show".
- [d2s4]  As of February, 2014, the podcast was no longer broadcast on 105 The Ticket

**d3: Zenon Konopka**

- [d3s0] Zenon Konopka (born January 2, 1981) is a retired Canadian professional ice hockey player.
- [d3s1]  Konopka played for the Mighty Ducks of Anaheim, Columbus Blue Jackets, Tampa Bay Lightning, New York Islanders, Ottawa Senators, Minnesota Wild, and Buffalo Sabres during his NHL career.

**d4: History of the Hmong in Minneapolis–Saint Paul**

- [d4s0] The Hmong people are a major ethnic group in the Minneapolis–Saint Paul area.
- [d4s1]  As of 2000 there were 40,707 ethnic Hmong in the Minneapolis-St.
- [d4s2]  Paul area.
- [d4s3]  The 2010 U.S. Census stated there were 66,000 ethnic Hmong in Minneapolis-St.
- [d4s4]  Paul, giving it the largest urban Hmong population in the world.
- [d4s5]  Grit Grigoleit, author of "Coming Home?
- [d4s6]  The Integration of Hmong Refugees from Wat Tham Krabok, Thailand, into American Society," wrote that the Minneapolis-St.
- [d4s7]  Paul area "acted as the cultural and socio-political center of Hmong life in the U.S."

**d5: Sports in Los Angeles**

- [d5s0] The Los Angeles metropolitan area is home to several professional and collegiate sports teams.
- [d5s1]  The Greater Los Angeles Area has nine major league professional teams: the Anaheim Ducks, the Los Angeles Angels, the Los Angeles Chargers, the Los Angeles Clippers, the Los Angeles Dodgers, LA Galaxy, the Los Angeles Kings, the Los Angeles Lakers, and the Los Angeles Rams.
- [d5s2]  Los Angeles FC will begin play as the area's tenth major team in 2018.
- [d5s3]  USC Trojans football, UCLA Bruins men's basketball, USC Trojans baseball, USC Trojans track & field, and Cal State Fullerton Titans baseball are all historically premier organizations in college sports.
- [d5s4]  Other major sports teams include UCLA Bruins Football, Los Angeles Sparks, Pepperdine Waves baseball, and formerly the Los Angeles Raiders and Los Angeles Aztecs.
- [d5s5]  Between them, these Los Angeles area sports teams have won a combined 105 Championship Titles.
- [d5s6]  Los Angeles area colleges have produced upwards of 200 National Championship Teams, primarily from USC Trojans and UCLA Bruins of the Pac-12 Conference.
- [d5s7]  The 1932 and 1984 Summer Olympics were held in Los Angeles.
- [d5s8]  In 2028 the city will host the Olympics for a third time.

**d6: Sports team**

- [d6s0] A sports team is a group of individuals who play sports, usually team sports, on the same team.
- [d6s1]  Historically, sports teams and the people who play sports have been amateurs.
- [d6s2]  However, by the 20th century, some sports teams and their associated leagues became extremely valuable with net worth in the millions.
- [d6s3]  Real Madrid is rated by Forbes as the world most valuable sports team at $3.26 billion USD.
- [d6s4]  Some individual sports have modified rules that allow them to be played by teams.

**d7: Don Bleu**

- [d7s0] Don Bleu, real name Rick Kelleher, is an American former radio personality and former television host.
- [d7s1]  He grew up in East Grand Forks, Minnesota and began his career in 1966, when his friend Shadoe Stevens encouraged him to try radio.
- [d7s2]  He started at KILO (defunct) in Grand Forks, North Dakota, then moved to KQWB in Fargo, North Dakota.
- [d7s3]  He then moved to the Minneapolis-St.
- [d7s4]  Paul area in 1968 and worked at KDWB for nearly ten years.
- [d7s5]  His success at KDWB earned him a job at KHJ (AM) in Los Angeles.
- [d7s6]  In 1980, he moved to San Francisco and worked in the adult contemporary radio genre.
- [d7s7]  Most recently, he hosted the "Don Bleu Show" on KOSF, a music station in San Francisco, California.
- [d7s8]  He was named to the Pavek Museum of Broadcasting's Minnesota Broadcasting Hall of Fame in 2005, and in 2007 he was inducted into the "Bay Area Radio Hall of Fame".
- [d7s9]  Bleu initially worked at KIOI until 2011, when he moved to KOSF.
- [d7s10]  He was let go from the latter station and did his last broadcast on June 26, 2015.

**d8: Minnesota Wild**

- [d8s0] The Minnesota Wild are a professional ice hockey team based in St. Paul, Minnesota.
- [d8s1]  They are members of the Central Division of the Western Conference of the National Hockey League (NHL).
- [d8s2]  The Wild are the only Minneapolis-St.
- [d8s3]  Paul area major professional sports league franchises to play in St. Paul; the other three play in Minneapolis.

**d9: WDGY**

- [d9s0] WDGY (740 AM, "Wee-Gee") is a daytime-only oldies radio station serving the Minneapolis-St.
- [d9s1]  Paul area of Minnesota.
- [d9s2]  It is licensed to and transmits from Hudson, Wisconsin, three miles east of its studios in Lakeland, Minnesota.

**d10: Rod Trongard**

- [d10s0] Rodney Douglas "Rod" Trongard (February 16, 1933 – July 16, 2005) was a Minnesota-based sports broadcaster on both radio and television in the Minneapolis-St. Paul area for more than fifty years.

## 7. hotpotqa_5a7a51485542990783324f0e

原位置：`dev` 第 34 题 · 全局第 277 题 · `sample_id: hotpotqa_5a7a51485542990783324f0e`

Question: Under the Yum Yum Tree starred this actress who was born in April, 1927?

Note: 保留先演员后生日筛选；先列演员候选，最终输出女演员姓名而非生日，不提前泄露筛选结果。

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留先演员后生日筛选；先列演员候选，最终输出女演员姓名而非生日，不提前泄露筛选结果。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | lead cast of Under the Yum Yum Tree listed in the context | False | [] | Jack Lemmon; Carol Lynley; Dean Jones; Edie Adams | [["d4s0"]] | context |
| u2 | actress among {u1} born in April 1927 | True | ["u1"] | Edie Adams | [["d2s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | actress who starred in Under the Yum Yum Tree | False | [] | Edie Adams | [['d4s0']] |
| u2 | Under the Yum Yum Tree actress born in April 1927, given {u1} | True | ['u1'] | Edie Adams | [['d2s0']] |

### Source documents (reference only)

**d1: Jed Harris**

- [d1s0] Jed Harris (born Jacob Hirsch Horowitz; February 25, 1900 – November 15, 1979) was an Austrian-born American theatrical producer and director.
- [d1s1]  He was responsible for some of the most successful productions on the Broadway stage in the 1920s and 1930s, including "Broadway" (1926), "Coquette" (1927), "The Royal Family" (1927), "The Front Page" (1928), "Uncle Vanya" (1930), "The Green Bay Tree" (1933) and "Our Town" (1938).
- [d1s2]  He later directed the original Broadway productions of "The Heiress" (1947) and "The Crucible" (1953).

**d2: Edie Adams**

- [d2s0] Edie Adams (born Edith Elizabeth Enke, April 16, 1927 – October 15, 2008) was an American businesswoman, singer, actress and comedian.
- [d2s1]  Adams was an Emmy Award and Tony Award winner.

**d3: Frances Upton**

- [d3s0] Frances Upton (April 15, 1904 – November 27, 1975 in Philadelphia, Pennsylvania) was a Broadway actress and comedian.
- [d3s1]  She starred with Eddie Cantor in "Whoopee!
- [d3s2] " and the "Ziegfeld Follies of 1927".
- [d3s3]  She also had a featured role in the early talkie "Night Work".
- [d3s4]  In 1929, she performed on a network shortwave radio program specially broadcast to Richard Byrd's expedition to the South Pole.
- [d3s5]  In 1931, she starred in one of the first experimental television broadcasts in New York City, appearing with Gertrude Lawrence, Lionel Atwill, and boxer Primo Carnera.

**d4: Under the Yum Yum Tree**

- [d4s0] Under the Yum Yum Tree is a 1963 comedy film that stars Jack Lemmon, Carol Lynley, Dean Jones, and Edie Adams, with supporting roles by Imogene Coca and Paul Lynde.

**d5: Robert Lansing (actor)**

- [d5s0] Robert Lansing ( ; June 5, 1928 – October 23, 1994) was an American stage, film, and television actor.
- [d5s1]  Lansing's motion picture roles included "A Gathering of Eagles" with Rock Hudson and "Under the Yum Yum Tree" opposite Jack Lemmon.
- [d5s2]  On television, he appeared in episodes of such hits as "", "Alfred Hitchcock Presents", "The Twilight Zone" and "Murder, She Wrote".
- [d5s3]  Lansing is probably best remembered as the authoritarian Brig. Gen. Frank Savage in "12 O'Clock High" (1964), the television drama series about World War II bomber pilots.

**d6: Vanessa Cantave**

- [d6s0] Vanessa Cantave (born October 7, 1977) is an American chef.
- [d6s1]  She is the co-founder and executive chef of the catering company Yum Yum Catering and Events in DUMBO, Brooklyn.

**d7: Laura Marano**

- [d7s0] Laura Marie Marano (born November 29, 1995) is an American actress and singer.
- [d7s1]  She starred in the Disney Channel series "Austin & Ally" as Ally Dawson.
- [d7s2]  Marano was one of the five original classmates in "Are You Smarter than a 5th Grader?
- [d7s3] ".
- [d7s4]  She starred in "Without a Trace" for three seasons and also "Back to You", in both instances playing the daughter of the main characters.
- [d7s5]  Marano starred in the indie film "A Sort of Homecoming".
- [d7s6]  Marano also starred in the 2015 Disney Channel Original Movie "Bad Hair Day" along with "Good Luck Charlie" actress Leigh-Allyn Baker.
- [d7s7]  In 2015, she signed with Big Machine Records and released her debut single "Boombox" on March 11, 2016.
- [d7s8]  At the end of 2016, Big Machine Records made the decision to drop all of their pop artists.
- [d7s9]  Marano then signed to Warner Bros.
- [d7s10]  Records in 2017 and plans to release her debut album with the label.
- [d7s11]  She is also the younger sister of actress Vanessa Marano who starred in Freeform's "Switched at Birth".

**d8: Yum Jung-ah**

- [d8s0] Yum Jung-ah (born July 28, 1972) is a South Korean actress.
- [d8s1]  Her notable films include "A Tale of Two Sisters" (2003), "The Big Swindle" (2004), "The Old Garden" (2007), and "Cart" (2014), as well as the television series "Royal Family" (2011).

**d9: Huh Jung**

- [d9s0] Huh Jung (born 1981) is a South Korean film director and screenwriter.
- [d9s1]  Huh directorial debut - a low-budget horror-thriller "Hide and Seek" (2013) starring Son Hyun-joo, was an unexpected hit in 2013 with 5.6 million admissions.
- [d9s2]  His second feature - also a horror film, titled "The Mimic", stars actress Yum Jung-ah and is scheduled to release in 2017.

**d10: Sophia Bush**

- [d10s0] Sophia Anna Bush (born July 8, 1982) is an American actress, director, spokesperson, and activist.
- [d10s1]  She starred in The WB/CW drama series "One Tree Hill", where she played Brooke Davis from 2003 to 2012.
- [d10s2]  She is known for her film roles in "John Tucker Must Die" (2006), "The Hitcher" (2007), and "The Narrows" (2008).
- [d10s3]  From 2014 to 2017, she starred in the NBC police procedural drama series "Chicago P.D." as Det. Erin Lindsay.

## 8. hotpotqa_5a7aa8565542995eb53be88b

原位置：`dev` 第 35 题 · 全局第 278 题 · `sample_id: hotpotqa_5a7aa8565542995eb53be88b`

Question: What movie did Katy Mixon star in that was directed by Seth Gordon?

Note: 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | films in which Katy Mixon had roles | False | [] | The Quiet, Four Christmases, and State of Play | [["d9s1"]] | context |
| u2 | film among {u1} directed by Seth Gordon | True | ["u1"] | Four Christmases | [["d1s4"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | films in which Katy Mixon had roles | False | [] | The Quiet, Four Christmases, and State of Play | [['d9s1']] |
| u2 | film among {u1} directed by Seth Gordon | True | ['u1'] | Four Christmases | [['d1s4']] |

### Source documents (reference only)

**d1: Four Christmases**

- [d1s0] Four Christmases (Four Holidays in Australia and New Zealand, Anywhere But Home in the Netherlands, Norway, United Arab Emirates and in South Africa) is a Christmas-themed romantic comedy film about a couple visiting all four of their divorced parents' homes on Christmas Day.
- [d1s1]  The film is produced by Spyglass Entertainment released by New Line Cinema on November 26, 2008, the day before Thanksgiving, and distributed by Warner Bros.
- [d1s2]  Pictures.
- [d1s3]  It stars Vince Vaughn and Reese Witherspoon, with Sissy Spacek, Mary Steenburgen, Robert Duvall, Jon Voight, Jon Favreau, Tim McGraw, Dwight Yoakam, and Kristin Chenoweth as supporting cast.
- [d1s4]  The film is director Seth Gordon's first studio feature film.
- [d1s5]  The DVD and Blu-ray Disc was released on November 24, 2009.

**d2: Horrible Bosses**

- [d2s0] Horrible Bosses is a 2011 American black comedy film directed by Seth Gordon, written by Michael Markowitz, John Francis Daley and Jonathan Goldstein, based on a story by Markowitz.
- [d2s1]  It stars Jason Bateman, Charlie Day, Jason Sudeikis, Jennifer Aniston, Colin Farrell, Kevin Spacey and Jamie Foxx.
- [d2s2]  The plot follows three friends, played by Bateman, Day and Sudeikis, who decide to murder their respective overbearing, abusive bosses, portrayed by Spacey, Aniston and Farrell.

**d3: Sarah Dunn (author)**

- [d3s0] Sarah Dunn (born 1970) is an American author and television writer.
- [d3s1]  She is known for her novels 'The Big Love' and 'Secrets to Happiness', and the ABC sitcom "American Housewife", starring Katy Mixon.

**d4: Double Date (The Office)**

- [d4s0] "Double Date" is the 9th episode of the sixth season of the U.S. comedy series "The Office" and the show's 109th episode overall.
- [d4s1]  It was written by Charlie Grandy and directed by Seth Gordon.
- [d4s2]  It originally aired on NBC on November 5, 2009.

**d5: Identity Thief**

- [d5s0] Identity Thief is a 2013 American comedy film directed by Seth Gordon, written by Craig Mazin, and starring Jason Bateman and Melissa McCarthy.
- [d5s1]  The film tells a story about a man (Bateman) whose identity is stolen by a woman (McCarthy).

**d6: Bill Nye: Science Guy**

- [d6s0] "Bill Nye: Science Guy" is a 2017 biographical documentary film produced and directed by David Alvarado and Jason Sussberg of Structure Films ("The Immortalists," 2014), and produced by Seth Gordon and Kate McLean.
- [d6s1]  The documentary concept was pitched to the film's subject, Bill Nye, by Alvarado, Sussberg, and Gordon at a hotel bar in San Francisco in October 2014.

**d7: Travels with Scout**

- [d7s0] "Travels with Scout" is the twenty-first episode of "Modern Family" and the twenty-first episode of the series overall.
- [d7s1]  It originally aired on April 28, 2010 on ABC.
- [d7s2]  The episode was written by Paul Corrigan & Brad Walsh and directed by Seth Gordon.

**d8: Canvassing (Parks and Recreation)**

- [d8s0] "Canvassing" is the second episode of the first season of the American comedy television series "Parks and Recreation".
- [d8s1]  It originally aired on NBC in the United States on April 16, 2009.
- [d8s2]  The episode was written by Rachel Axler and directed by Seth Gordon.
- [d8s3]  In the episode, Deputy Director of Parks and Recreation Leslie and her staff canvas the neighborhood to seek support for an upcoming town meeting on their park proposal but end up drawing more critics than allies.

**d9: Katy Mixon**

- [d9s0] Katy Mixon (born March 30, 1981) is an American actress.
- [d9s1]  She began her career playing supporting roles in films such as "The Quiet" (2005), "Four Christmases" (2008), and "State of Play" (2009), before landing the female leading role in the HBO comedy series "Eastbound & Down" (2009–2013).

**d10: Dauphin Island Bridge**

- [d10s0] The Dauphin Island Bridge, formally the Gordon Persons Bridge, carries a 3 mi , two-lane section of Alabama State Route 193 from mainland Mobile County, Alabama across the Gulf Intracoastal Waterway to Dauphin Island.
- [d10s1]  The natural channel followed by the Gulf Intracoastal Waterway at this location is Pass Aux Herons.
- [d10s2]  The bridge separates the Mississippi Sound on the west from Mobile Bay on the east.
- [d10s3]  It was named in honor of Seth Gordon Persons, the 46th governor of Alabama.

## 9. hotpotqa_5a7cfdb755429909bec768e2

原位置：`dev` 第 36 题 · 全局第 279 题 · `sample_id: hotpotqa_5a7cfdb755429909bec768e2`

Question: The Frogman Corps is the maritime special operations force of the unified armed forces of what kingdom?

Note: 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

Type: bridge · fallback: False · SFT snapshots: 7

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | unified armed forces of which the Frogman Corps is the maritime special operations force | False | [] | Danish Defence | [["d10s0"]] | context |
| u2 | kingdom whose unified armed forces are {u1} | True | ["u1"] | Kingdom of Denmark | [["d3s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | unified armed forces of which the Frogman Corps is the maritime special operations force | False | [] | Danish Defence | [['d10s0']] |
| u2 | kingdom whose unified armed forces are {u1} | True | ['u1'] | Kingdom of Denmark | [['d3s0']] |

### Source documents (reference only)

**d1: Korps Commandotroepen**

- [d1s0] The Korps Commandotroepen (KCT) are the special forces of the Royal Netherlands Army.
- [d1s1]  It is one of the three principal units tasked with special operations in the Netherlands (the others being the "Maritime Special Operations Forces" (NL MARSOF) of the Netherlands Marine Corps and the "Brigade Speciale Beveiligingsopdrachten" (BSB) of the Royal Marechaussee), and it is deployable anywhere in the world under any circumstance, conducting all conceivable missions from the full spectrum of special operations, including counter-terrorism overseas.

**d2: Maritime Special Purpose Force**

- [d2s0] The United States Marine Corps' Maritime Special Purpose Force, or "MSPF", are a unique specialized sub-unit that are drawn from the Marine Expeditionary Units' (MEU) major subordinate elements.
- [d2s1]  They are special operations "capable" forces deployed to give the commanders low profile, two-platoon surgical emplacement in the accessible littoral regions.
- [d2s2]  The MSPF provides the enhanced operational capability and precision skills to complement, enable, and execute selected conventional, maritime special operations.
- [d2s3]  They can also perform operations not resident in traditional amphibious raid companies.

**d3: Danish Defence**

- [d3s0] The Danish Defence (Danish: "Forsvaret" , Faroese: "Danska verjan" ) is the unified armed forces of the Kingdom of Denmark, charged with the defence of Denmark and its constituent, self-governing nations Greenland and the Faroe Islands.

**d4: United States Pacific Command**

- [d4s0] United States Pacific Command (USPACOM) is a unified combatant command of the United States Armed Forces responsible for the Indo-Asia-Pacific region.
- [d4s1]  It is the oldest and largest of the unified combatant commands.
- [d4s2]  Its commander, the senior U.S. military officer in the Pacific, is responsible for military operations in an area which encompasses more than 100 e6sqmi , or roughly 52 percent of the Earth’s surface, stretching from the waters off the west coast of the United States to the west coast of India, and from the Arctic to the Antarctic.
- [d4s3]  The Commander reports to the President of the United States through the Secretary of Defense and is supported by Service component and subordinate unified commands, including U.S. Army Pacific, U.S. Pacific Fleet, U.S. Pacific Air Forces, U.S. Marine Forces Pacific, U.S. Forces Japan, U.S. Forces Korea, Special Operations Command Korea, and Special Operations Command Pacific.
- [d4s4]  USPACOM also has three direct reporting units (DRUs), including Daniel K. Inouye Asia-Pacific Center for Security Studies, U.S. Pacific Command Joint Intelligence Operations Center, Center for Excellence in Disaster Management and Humanitarian Assistance; and a Standing Joint Task Force, Joint Interagency Task Force West.
- [d4s5]  The USPACOM headquarters building, the Nimitz-MacArthur Pacific Command Center, is located on Camp H.M. Smith, Hawaii.

**d5: Unit Interventie Mariniers**

- [d5s0] M-Squadron, formerly the Unit Interventie Mariniers ("Marine Intervention Unit", UIM), and before that known as the Bijzondere Bijstands Eenheid ("Special Support Unit", BBE), is an elite Dutch special forces unit, which is specially trained for intervention missions.
- [d5s1]  It consists of a selection of specially trained marines of the Dutch Marine Corps, and it is part of the "Maritime Special Operations Forces" (MARSOF), which is the maritime counterpart of the Dutch Army's Korps Commandotroepen.
- [d5s2]  MARSOF is able to operate in and outside of the Netherlands, with emphasis on maritime special operations.
- [d5s3]  It currently consists of 3 SF units, C-Squadron (Mountain Leader Recon and Amphibian Recon) and M-Squadron (Counter-Terrorism).
- [d5s4]  M-Squadron consist of teams of 6 operators, each team and each operator with their own specialty.
- [d5s5]  Among those are diver and breach teams.

**d6: Lithuanian Special Operations Force**

- [d6s0] The Lithuanian Special Operations Force (LITHSOF) (Lithuanian: "Lietuvos Specialiųjų Operacijų Pajėgos" ) is a special operation unit of the Lithuanian Armed Forces, formed exclusively of carefully selected, motivated and specially trained professionals.
- [d6s1]  The main tasks of the Special Operations Force are counter terrorism, special reconnaissance, and hostage rescue.

**d7: Joint Task Force 2**

- [d7s0] Joint Task Force 2 (JTF2) (French: "Force opérationnelle interarmées 2, FOI 2" ) is an elite special operations force of the Canadian Armed Forces.
- [d7s1]  JTF2 serves alongside the Canadian Special Operations Regiment, the Canadian Joint Incident Response Unit and 427 Special Operations Aviation Squadron as part of the Canadian Special Operations Forces Command.
- [d7s2]  The unit is currently based at Dwyer Hill, near Ottawa, Ontario, and plans to move to a new facility to be built at CFB Trenton by 2019.

**d8: Namibian Special Forces**

- [d8s0] The Namibian Special Forces is a special operations command of the Namibian Defence Force responsible for special forces and special operations capable units.
- [d8s1]  The command consists of Army commandos, Army Airborne paratroopers and the Marine Corps amphibious special operations unit.
- [d8s2]  The Army commandos specialise in airborne and land borne insertion while the Marine Corps amphibious special operations unit specialise in small-unit maritime operations that originate from a river, ocean, swamp and delta.
- [d8s3]  The army units receive training assistance from former South African Special Forces (Recces) and the marine corps from the Brazilian Marine Corps.
- [d8s4]  The units regularly participate in Southern African Development Community (SADC) special forces exercises.

**d9: Special Operations Force (Singapore)**

- [d9s0] The Special Operations Force (SOF) is the Republic's Army Special Forces composed of highly trained elite soldiers within the Singapore Armed Forces Commando Formation and an essential component of the joint special forces unit Special Operations Task Force (SOTF).
- [d9s1]  According to the Principles of Special Forces, the Republic's special forces thrive on their exceptional qualities and advanced skills, consisting highly adaptive individuals who are independent and can operate independently, and the Republic's special forces soldiers cannot be mass-produced and must be managed carefully.

**d10: Frogman Corps (Denmark)**

- [d10s0] The Frogman Corps (Danish: "Frømandskorpset" ) is the maritime special operations force of the Danish Defence part of Special Operations Command.
- [d10s1]  On 1 July 2015, the Frogman Corps transferred from the Royal Danish Navy to the newly established Special Operations Command.

## 10. hotpotqa_5a7f359f55429930675136a9

原位置：`dev` 第 37 题 · 全局第 280 题 · `sample_id: hotpotqa_5a7f359f55429930675136a9`

Question: Who was a Canadian film producer, director, actor and screenwriter, Randal Kirk II or Sidney Olcott?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | whether Randal Kirk II was a Canadian film producer, director, actor and screenwriter | False | [] | no | [["d3s0"]] | definition_omission |
| u2 | whether Sidney Olcott was a Canadian film producer, director, actor and screenwriter | False | [] | yes | [["d1s0"]] | context |
| u3 | who was a Canadian film producer, director, actor and screenwriter | True | ["u1", "u2"] | Sidney Olcott | [[]] | derived_from_dependencies |

- u1：`by_omission=true`，沿用定义性介绍省略规则，不是文中明确否定。

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Randal Kirk II was a Canadian film producer, director, actor and screenwriter | False | [] | no | [['d3s0']] |
| u2 | whether Sidney Olcott was a Canadian film producer, director, actor and screenwriter | False | [] | yes | [['d1s0']] |
| u3 | which of Randal Kirk II and Sidney Olcott was a Canadian film producer, director, actor and screenwriter | True | ['u1', 'u2'] | Sidney Olcott | [[]] |

### Source documents (reference only)

**d1: Sidney Olcott**

- [d1s0] Sidney Olcott (September 20, 1872 – December 16, 1949) was a Canadian-born film producer, director, actor and screenwriter.

**d2: Carl Bessai**

- [d2s0] Carl Bessai (born 1966 in Edmonton, Alberta) is a Canadian film director and screenwriter.
- [d2s1]  Bessai studied at OCAD University and at York University in Toronto graduating with a Master of Fine Arts Degree.
- [d2s2]  He got his start directing documentary films before moving to Vancouver and directing his debut feature film "Johnny" in 1999.
- [d2s3]  Bessai has made a career working on low-budget independent features but has worked with A-List actors Ian McKellen and Deborah Kara Unger on his film "Emile" and Carrie-Anne Moss on his film "Normal".
- [d2s4]  He was nominated for the Genie Award for Best Achievement in Direction for the latter film.
- [d2s5]  Bessai is a member of the Director’s Guild of Canada, the Writer’s Guild of Canada, and the Canadian Film and Television Producer's Association.

**d3: Randal Kirk II**

- [d3s0] Randal Kirk II is an American film director, writer, producer, and cinematographer.

**d4: Timothy's Quest**

- [d4s0] Timothy's Quest is a 1922 American silent drama film produced by Dirigo Films and distributed by American Releasing.
- [d4s1]  It was directed by Sidney Olcott with the child actor Joseph Depew, based on a story written by Kate Douglas Wiggin.

**d5: Sidney J. Furie**

- [d5s0] Sidney J. Furie (born February 28, 1933) is a Canadian film director, screenwriter, and producer best known for his extensive work in both British and American cinema between the 1960s and early 1980s.
- [d5s1]  Like his contemporaries Norman Jewison and Ted Kotcheff, he was one of earliest Canadian directors to achieve mainstream critical and financial success outside their native country at a time when its film industry was virtually nonexistent.
- [d5s2]  He won a BAFTA Film Award and was nominated for a Palme d'Or for his work on the acclaimed spy thriller "The Ipcress File" starring Michael Caine.

**d6: Donald Shebib**

- [d6s0] Donald Shebib (born 17 January 1938, Toronto), often called Don Shebib, is a Canadian film director, writer, producer and editor.
- [d6s1]  A graduate of UCLA film school, Shebib gained prominence and critical acclaim in Canadian cinema for his seminal 1970 movie "Goin' Down the Road", which combined narrative storytelling with Canadian documentary tradition influenced by the British.
- [d6s2]  The low-budget film crew travelled around Toronto in a station wagon, supported by funding from the newly-formed Canadian Film Development Corporation.
- [d6s3]  The movie was screened in New York and hailed by Pauline Kael and Roger Ebert.
- [d6s4]  Kael wrote that the movie showed up the ostensibly forced sincerity and perceived honesty of the films of John Cassavetes.
- [d6s5]  Shebib is the father of Noah "40" Shebib.
- [d6s6]  Goin' Down the Road was digitally remastered as one of the key films in the Canadian film canon and was honoured with a screening at the Art Gallery of Ontario.
- [d6s7]  A sequel was shot in 2011, called "Goin' Down the Road Again," featuring some of the original cast members as well as a new generation of characters.

**d7: John Dunning (film producer)**

- [d7s0] John Dunning (April 27, 1927–September 19, 2011) was a pioneering Canadian film producer from Montreal who co-founded the Canadian film production company Cinépix and produced early works by notable Canadian directors David Cronenberg and Ivan Reitman.
- [d7s1]  Dunning launched Cinépix with partner André Link in Montreal in the early 1960s.
- [d7s2]  Their biggest commercial success—and the first Canadian box office hit—came with Reitman’s "Meatballs" (1979).

**d8: James W. Horne**

- [d8s0] James Wesley Horne (December 14, 1881June 29, 1942) was an early American actor, screenwriter and film director.
- [d8s1]  He began his career as an actor under director Sidney Olcott at Kalem Studios in 1913 and directed his first film for the company two years later.

**d9: The Lad from Old Ireland**

- [d9s0] The Lad from Old Ireland, also called A Lad from Old Ireland, is a one-reel 1910 American motion picture directed by and starring Sidney Olcott and written by and co-starring Gene Gauntier.
- [d9s1]  It was the first film appearance of prolific actor/director J.P. McGowan.

**d10: From the Manger to the Cross**

- [d10s0] From the Manger to the Cross or Jesus of Nazareth is a 1912 American motion picture that was filmed on location in Palestine.
- [d10s1]  It tells the story of Jesus' life.
- [d10s2]  Directed by Sidney Olcott who also appeared in the film, actress and screenwriter Gene Gauntier wrote the script and portrayed the Virgin Mary.

## 11. hotpotqa_5a81d03d55429903bc27b9c7

原位置：`dev` 第 38 题 · 全局第 281 题 · `sample_id: hotpotqa_5a81d03d55429903bc27b9c7`

Question: Are Gurinder Chadha and Hou Hsiao-hsien both from England?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: comparison · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | whether Gurinder Chadha is from England | False | [] | yes | [["d10s0"]] | context |
| u2 | whether Hou Hsiao-hsien is from England | False | [] | no | [["d4s0"]] | definition_omission |
| u3 | whether both Gurinder Chadha and Hou Hsiao-hsien are from England | True | ["u1", "u2"] | no | [[]] | derived_from_dependencies |

- u2：`by_omission=true`，沿用定义性介绍省略规则，不是文中明确否定。

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Gurinder Chadha is from England | False | [] | yes | [['d10s0']] |
| u2 | whether Hou Hsiao-hsien is from England | False | [] | no | [['d4s0']] |
| u3 | whether Gurinder Chadha and Hou Hsiao-hsien are both from England | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Flight of the Red Balloon**

- [d1s0] Flight of the Red Balloon (French: Le voyage du ballon rouge ) is a 2007 French-Taiwanese film directed by Hou Hsiao-hsien.
- [d1s1]  It is the first part in a new series of films produced by Musée d'Orsay, and tells the story of a French family as seen through the eyes of a Chinese student.
- [d1s2]  The film was shot in August and September 2006 on location in Paris.
- [d1s3]  This is Hou Hsiao-hsien's first non-Asian film.
- [d1s4]  It references the classic 1956 French short "The Red Balloon" directed by Albert Lamorisse.

**d2: Viceroy's House (film)**

- [d2s0] Viceroy's House is British-Indian historical drama film directed by Gurinder Chadha and written by Paul Mayeda Berges, Moira Buffini, and Chadha.
- [d2s1]  The film stars Hugh Bonneville, Gillian Anderson, Manish Dayal, Huma Qureshi, and Michael Gambon.
- [d2s2]  It has been selected to be screened out of competition at the 67th Berlin International Film Festival.

**d3: Dust in the Wind (film)**

- [d3s0] Dust in the Wind is a 1986 film by Taiwanese filmmaker Hou Hsiao-hsien.
- [d3s1]  It is based on co-screenwriter Wu Nien-jen's own experiences, and is the final part of Hou's coming-of-age trilogy, with the others being "A Summer at Grandpa's" (1984) and "The Time to Live and the Time to Die" (1985).

**d4: Hou Hsiao-hsien**

- [d4s0] Hou Hsiao-hsien (] born 8 April 1947) is a Taiwanese film director, screenwriter, producer and actor.
- [d4s1]  He is a leading figure in world cinema and in Taiwan's New Wave cinema movement, an auteur.
- [d4s2]  He won the Golden Lion at the Venice Film Festival in 1989 for his film "A City of Sadness" (1989), and the Best Director award at the Cannes Film Festival in 2015 for "The Assassin" (2015).
- [d4s3]  Other highly regarded works of his include "The Puppetmaster" (1993) and "Flowers of Shanghai" (1998).

**d5: The Assassin (2015 film)**

- [d5s0] The Assassin (; or: "The Assassin Niè Yǐnniáng") is a 2015 wuxia film directed by Taiwanese director Hou Hsiao-hsien.
- [d5s1]  A Taiwan/China/Hong Kong co-production, it was an official selection in the main competition section at the 2015 Cannes Film Festival.
- [d5s2]  At Cannes, Hou won the award for Best Director.
- [d5s3]  It was released in China and Hong Kong on 27 August, and a day later in Taiwan on 28 August 2015.
- [d5s4]  It was selected as the Taiwanese entry for the Best Foreign Language Film at the 88th Academy Awards but it was not nominated.

**d6: Cute Girl**

- [d6s0] Cute Girl, also known as Lovable You (), is a 1980 movie directed by Taiwanese director Hou Hsiao-hsien, starring Kenny Bee, Anthony Chan and Fong Fei Fei.
- [d6s1]  It was Hou Hsiao-hsien's first feature film.

**d7: Bride and Prejudice**

- [d7s0] Bride and Prejudice is a 2004 romantic drama film directed by Gurinder Chadha.
- [d7s1]  The screenplay by Chadha and Paul Mayeda Berges is a Bollywood-style adaptation of "Pride and Prejudice" by Jane Austen.
- [d7s2]  It was filmed primarily in English, with some Hindi and Punjabi dialogue.
- [d7s3]  The film released in the United States on 11 February 2005 and was well received by critics.

**d8: The Time to Live and the Time to Die**

- [d8s0] The Time to Live and the Time to Die, also known as A Time to Live, A Time to Die is a 1985 film directed by Hou Hsiao-hsien.
- [d8s1]  This film is inspired by screenwriter-turned-director Hou's own coming-of-age story.

**d9: It's a Wonderful Afterlife**

- [d9s0] It's a Wonderful Afterlife is a 2010 British comedy film directed by Gurinder Chadha.
- [d9s1]  The screenplay centres on an Indian mother whose obsession with marrying off her daughter leads her into the realm of serial murder.
- [d9s2]  It was filmed primarily in English, with some Hindi and Punjabi dialogue.
- [d9s3]  The title is a reference to Chadha's personal attachment to Frank Capra's film "It's a Wonderful Life."
- [d9s4]  Chadha also co-produced the film, and co-wrote the screenplay with her husband and producing partner, Paul Mayeda Berges.
- [d9s5]  The lead role is played by newcomer Goldy Notay, joining Shabana Azmi, Shaheen Khan, Sendhil Ramamurthy and Sally Hawkins in the cast.

**d10: Gurinder Chadha**

- [d10s0] Gurinder Chadha, {'1': ", '2': ", '3': ", '4': "} (born 10 January 1960) is an English film director of Kenyan Asian origin.
- [d10s1]  Most of her films explore the lives of Indians living in England.
- [d10s2]  This common theme among her work showcases the trials of Indian women living in England and how they must reconcile their converging traditional and modern cultures.
- [d10s3]  Although many of her films seem like simple quirky comedies about Indian women, they actually address many social and emotional issues, especially ones faced by immigrants caught between two worlds.

## 12. hotpotqa_5a8715fb5542991e771816bb

原位置：`dev` 第 39 题 · 全局第 282 题 · `sample_id: hotpotqa_5a8715fb5542991e771816bb`

Question:  A Time for Miracles chronicles the life story of America's first native born saint who was born in what year?

Note: 保留 single，d3s0 同时给出首位本土圣人身份和出生年，电影说明不是必需证据。

Type: single · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留 single，d3s0 同时给出首位本土圣人身份和出生年，电影说明不是必需证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | year America's first native born saint was born | True | [] | 1774 | [["d3s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | America's first native born saint whose life story A Time for Miracles chronicles | False | [] | Elizabeth Ann Seton | [['d4s0']] |
| u2 | birth year of {u1} | True | ['u1'] | 1774 | [['d3s0']] |

### Source documents (reference only)

**d1: Emmitsburg, Maryland**

- [d1s0] Emmitsburg is a town in Frederick County, Maryland, United States, just south of the Mason-Dixon line separating Maryland from Pennsylvania.
- [d1s1]  Founded in 1785, Emmitsburg is the home of Mount St. Mary's University.
- [d1s2]  The town has two Catholic pilgrimage sites: the National Shrine Grotto of Our Lady of Lourdes, which is on the campus of Mount St. Mary's, and the Basilica and National Shrine of St. Elizabeth Ann Seton, who was the first native born United States citizen to be canonized as a saint.
- [d1s3]  The Seton Shrine is one of the top eight Catholic pilgrimage destinations in the United States.

**d2: John Thayer (priest)**

- [d2s0] The Reverend John Thayer (1755–5 February 1815) was the first native of New England ordained to the Roman Catholic priesthood.
- [d2s1]  He was born in Boston, Massachusetts.
- [d2s2]  Thayer was educated at Yale College and was a Protestant in his early life.
- [d2s3]  He was ordained as a Congregationalist minister and served as a chaplain during the American Revolutionary War.
- [d2s4]  While visiting Rome in 1783, he converted to the Roman Catholic faith, an act which caused a sensation in New England at the time.
- [d2s5]  He credited his conversion to miracles attributed to the noted mendicant, Saint Benedict Joseph Labre, who lived and died there in that period.

**d3: Elizabeth Ann Seton**

- [d3s0] Elizabeth Ann Bayley Seton, S.C., (August 28, 1774 – January 4, 1821) was the first native-born citizen of the United States to be canonized by the Roman Catholic Church (September 14, 1975).
- [d3s1]  She established the first Catholic girls' school in the nation in Emmitsburg, Maryland, where she also founded the first American congregation of religious sisters, the Sisters of Charity.

**d4: A Time for Miracles**

- [d4s0] A Time For Miracles is a 1980 American made-for-television biographical drama film chronicling the life story of America's first native born saint, Elizabeth Ann Bayley Seton.
- [d4s1]  It was produced by ABC Circle Films for the American Broadcasting Company and telecast December 21, 1980, as a Christmas special.
- [d4s2]  The film was created by Beverlee Dean and directed by Michael O'Herlihy.
- [d4s3]  The script was written by Henry Denker with collaboration with Sister Mary Hilaire and filmed in Georgia.
- [d4s4]  "A Time For Miracles" starred "Ryan's Hope" and "" actress Kate Mulgrew as Elizabeth Seton.
- [d4s5]  John Forsythe and Lorne Greene also star.

**d5: John A. Winston**

- [d5s0] John Anthony Winston (September 4, 1812 – December 21, 1871) was the 15th Governor of the U.S. state of Alabama from 1853 to 1857.
- [d5s1]  He was born in 1812 in Madison County, Alabama Territory, and became the first native born governor of Alabama.
- [d5s2]  He was a son of William Winston and Mary Cooper of Tuscumbia Alabama.
- [d5s3]  William was a son of Anthony Winston and Keziah Jones former residents of Buckingham County Virginia.
- [d5s4]  John Anthony Winston married his first cousin, Mary Agness Jones, (born ca. 1819 and died ca. 1835) on August 7, 1832 in Madison County Alabama.
- [d5s5]  He died December 21, 1871 in Mobile, Alabama and is buried in the Winston Family Cemetery (privately owned) near Gainesville in Sumter County Alabama.
- [d5s6]  He had only one child, a daughter, Mary Agnes Winston.
- [d5s7]  In January 1867 he presented his credentials to the United States Senate as Senator-elect from Alabama for the term 1867–1873, but was not permitted to take his seat.

**d6: John David Merwin**

- [d6s0] John David Merwin (born September 26, 192117 March 2013) was a former politician of the United States Virgin Islands who served in that territory's Legislature, as Government Secretary (equivalent to Lieutenant Governor), and as the first native born Governor.
- [d6s1]  He was perhaps the first "politician" to be made Governor as previous appointees were primarily men of the military, industry, or non-elected government servants.

**d7: Josiah Winslow**

- [d7s0] Josiah Winslow was born in Plymouth Colony about 1628 and died in 1680 in Marshfield, Plymouth Colony.
- [d7s1]  In records of the time, historians also name him Josias Winslow, and modern writers have carried that name forward.
- [d7s2]  He was born one year after the Charter which founded the Massachusetts Bay Colony, bringing over 20,000 English immigrants to New England in the 1630s.
- [d7s3]  Josiah was the Harvard College-educated son of "Mayflower" passenger and Pilgrim leader Edward Winslow and was Governor from 1673 to 1680.
- [d7s4]  The most significant event during his term in office was King Philip's War, which created great havoc for both the English and Indian populations and changed New England forever.
- [d7s5]  Josiah was the first native born governor of an American Colony.

**d8: List of Argentine operas**

- [d8s0] This is a list of operas by Argentine composers.
- [d8s1]  Argentina's first native born opera composer was Francisco Hargreaves (1849-1900) who composed "La gatta bianca" (1875) and "Los estudiantes de Bologna" (1897), followed by Zenón Rolón (1856-1902) who composed several operas as well as operettas and zarzuelas.
- [d8s2]  The works of many of the composers from this generation were first performed outside Argentina.
- [d8s3]  Native Argentine opera was to develop much more with the massive European (mainly Italian) immigration in the late 19th century and even more with the opening of the Teatro Colón in 1908 where most of the 20th century operas listed here had their world premieres.
- [d8s4]  Some of the first operas to treat Argentine subjects or national themes were Arturo Berutti's "Pampa" (1897) based on the life of Juan Moreira and "Yupanki" (1899) based on the life of Inca warrior Manqu Inka Yupanki.
- [d8s5]  Also notable in this genre were Felipe Boero's "Tucumán" (1918) set during the Battle of Tucumán and "El matrero" (1929).
- [d8s6]  Considered by many to be the quintessential Argentine opera, "El matrero" had a libretto based on gaucho folk tradition and incorporated Argentine folk melodies and a traditional gaucho dance.
- [d8s7]  The Spanish playwright Federico García Lorca was also the inspiration for several Argentine operas.
- [d8s8]  His plays, "La zapatera prodigiosa" and "Bodas de sangre", were the basis of operas by Juan José Castro, while Osvaldo Golijov's 2003 opera "Ainadamar" is based on events in the playwright's life.

**d9: William Read Miller**

- [d9s0] William Read Miller (November 23, 1823November 29, 1887) was the 12th Governor of the State of Arkansas.
- [d9s1]  Born in Batesville, Arkansas; Miller was Arkansas's first native born Governor.
- [d9s2]  Serving two terms in the turbulent period after Reconstruction, Miller's four-year administration marked the beginnings of New Departure Democrats in Arkansas.
- [d9s3]  Running on a platform of economic growth via reconciliation between whites and freedmen, Miller often was opposed by members of his own party during the infancy of the Lost Cause ideology.
- [d9s4]  His plans to pay back a large state debt including the Holford Bonds, valued at $14 million ($ million today), were often interrupted by racial violence, and his support for public schools and universities was often combated by those in his own party.

**d10: Smokey Robinson &amp; The Miracles: 1957–1972**

- [d10s0] 1957-1972 is a 1972 double album by The Miracles on Motown Records' Tamla label.
- [d10s1]  This two-record set is noted as the group's final series of live concerts with original lead singer Smokey Robinson, recorded over a period of three days, July 14–16, during the 1972 National Parks Centennial, at the Carter Barron Amphitheater in Washington, D.C., and charted at #75 on the "Billboard" Top 200 Album chart, and at #14 on its R&B Album chart.
- [d10s2]  During the show, Smokey's wife, original Miracles member Claudette Rogers Robinson, who stopped touring with the group in 1964 (but continued recording with them), reunited with the Miracles on stage for the first time in eight years.
- [d10s3]  As a celebration of the group's fifteen years together, The Miracles made this an "all request" show, where audience members could choose which of the group's long string of hits they wanted performed.
- [d10s4]  Also, at the end of the concert, Miracles fans were introduced to the group's new lead singer, Billy Griffin.
- [d10s5]  According to Smokey's autobiography, "Smokey: Inside My Life", The Miracles' final concert was videotaped in movie form, but was never publicly released.
- [d10s6]  However, "1957-1972" was released on CD originally in 1990, and re-released again in 2004 along with The Miracles' 1969 "Live" album in the 2004 Motown/Hip-O Select release "Smokey Robinson and The Miracles: The Live Collection".

## 13. hotpotqa_5a87e93155429938390d3ea4

原位置：`dev` 第 40 题 · 全局第 283 题 · `sample_id: hotpotqa_5a87e93155429938390d3ea4`

Question: Are Purbanchal University and California State University, Northridge, both public universities?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | whether Purbanchal University is a public university | False | [] | yes | [["d6s0"]] | context |
| u2 | whether California State University, Northridge is a public university | False | [] | yes | [["d2s0"]] | context |
| u3 | whether both are public universities | True | ["u1", "u2"] | yes | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Purbanchal University is a public university | False | [] | yes | [['d6s0']] |
| u2 | whether California State University, Northridge is a public university | False | [] | yes | [['d2s0']] |
| u3 | whether Purbanchal University and California State University, Northridge are both public universities | True | ['u1', 'u2'] | yes | [[]] |

### Source documents (reference only)

**d1: S. K. Ramesh**

- [d1s0] S. K. Ramesh is presently the Dean of the College of Engineering and Computer Science at California State University, Northridge, United States.
- [d1s1]  Prior to joining California State University, Northridge he was the Professor of Electrical and Electronics Engineering at California State University, Sacramento and he served as the Department Chair since 1994.

**d2: California State University, Northridge**

- [d2s0] California State University, Northridge (also known as CSUN) is a public university in the Northridge neighborhood of Los Angeles, California, United States, in the San Fernando Valley.
- [d2s1]  With a total enrollment of 41,548 (as of Fall 2015) it has the largest student body of the 23-campus California State University system, and is one of the largest comprehensive universities in the State of California (behind UCLA) in terms of enrollment.
- [d2s2]  As of Fall 2014, the school had 2,096 faculty, of which between 745 and 784 (or about 40%) were on the tenure track.

**d3: California State University, San Bernardino**

- [d3s0] California State University, San Bernardino, (also known as Cal State San Bernardino or CSUSB), is a public university and one of the 23 general campuses of the California State University system.
- [d3s1]  The main campus sits on 441 acre in the University District of San Bernardino, California, United States, with a branch campus of 40 acre in Palm Desert, California, opened in 1986.
- [d3s2]  In 2013, California State University, San Bernardino was named a 2014 Best College in the Western Region by The Princeton Review for the tenth consecutive year, ranking CSUSB among the top 25 percent of universities across the nation.
- [d3s3]  Back in 2011, California State University, San Bernardino’s Jack H. Brown College of Business and Public Administration was recognized by "European CEO Magazine" as one of the top 20 schools of business in the world and one of the world's 18 most innovative business schools.

**d4: Ron Purcell**

- [d4s0] "Ronald Charles Purcell" (October 5, 1932 – September 7, 2011) was an American guitarist, with degrees from the Los Angeles Conservatory of Music, California State University, Northridge.
- [d4s1]  He was Professor Emeritus of the Department of Music at California State University, Northridge and Director of the International Guitar Research Archive.
- [d4s2]  His major teachers included Andrés Segovia, Emilio Pujol, Macario Santiago Kastner, Alirio Diaz and Mario Castelnuovo-Tedesco, whose "Hommage to Purcell", Op. 170, No. 38 is dedicated to him.

**d5: Scott Glasgow**

- [d5s0] Scott Glasgow is a Hollywood-based musical composer.
- [d5s1]  Has a Bachelor of Music from California State University, Northridge and a Master of Music from the San Francisco Conservatory of Music in 2001 where he was a student of Conrad Susa.
- [d5s2]  Scott studied with John Corigliano at the Aspen Music Festival 2002 and was in the ASACP Film Scoring program in 2004.
- [d5s3]  Since 2005 has made his career as a film composer with over 20+ studio features to date.
- [d5s4]  Scott also teaches at the university level, with classes in film scoring at CSUN California State University, Northridge and UCLA University of California, Los Angeles.
- [d5s5]  Scott has contributed addition music to films, TV and games including video games DC Universe Online, TV shows HBO Curb Your Enthusiasm and CBS 60 Minutes and feature films .

**d6: Purbanchal University**

- [d6s0] Purbanchal University (PU) is a public university in Biratnagar, the economic centre of Nepal.
- [d6s1]  It was established in 1993 by the government of Nepal.
- [d6s2]  It is on over 545 hectares.

**d7: Cal State Northridge Matadors football**

- [d7s0] The Cal State Northridge Matadors football team represented California State University, Northridge in the sport of American football from the 1962 through 2001 seasons.
- [d7s1]  Between 1962 through 1992, Cal State Northridge competed at the NCAA Division II level prior to moving to Division I-AA in 1993.
- [d7s2]  The Matadors played their home games at multiple stadiums throughout their history with the most recent being North Campus Stadium in Northridge, California.

**d8: Bill Kernen**

- [d8s0] Bill Kernen (born August 1, 1948 in Boise, Idaho) is the retired former head coach of the California State University, Bakersfield baseball team.
- [d8s1]  Prior to that position he was the head coach of the California State University, Northridge baseball team from 1989–1995, and the pitching coach for the California State University, Fullerton baseball team from 1978–1982 and 1986-87.
- [d8s2]  Following this he was the pitching coach at University of Illinois from 1987-88.
- [d8s3]  He was the pitching coach at North Carolina State from 2001-1003.
- [d8s4]  Before founding and building the program at CS Bakersfield, he was again an assistant at CS Fullerton in 2006-2007.
- [d8s5]  In addition to his baseball coaching achievements, Kernen is also an accomplished playwright, having been produced on the New York stage seven times.
- [d8s6]  He is the producer, writer and director of a short film made in 2006.
- [d8s7]  Kernen was a professional baseball player in the Baltimore Oriole organization from 1970-72.

**d9: Cal Poly Pomona College of Engineering**

- [d9s0] The Cal Poly Pomona College of Engineering is the engineering college at California State Polytechnic University, Pomona (Cal Poly Pomona or Cal Poly) located in Pomona, California, United States.
- [d9s1]  Well known for its "learn by doing" philosophy, the college's motto is: ""making imagination real"".
- [d9s2]  Cal Poly has one of the top engineering college among public schools in California and, with over 5,600 students (as of fall 2015), it is also the largest engineering college in Southern California, the second largest college of engineering in the California State University system, and the seventeenth largest engineering college in the United States.
- [d9s3]  In the 2017 "U.S. News & World Report" the College of Engineering is ranked the 5th best undergraduate program among public universities (11th overall) in the West for Master's-granting universities, and "has one of the top ranked engineering programs, and graduates roughly 1 of every 14 engineers in the state of California."

**d10: IRS Volunteer Income Tax Assistance Program**

- [d10s0] The Volunteer Income Tax Assistance (VITA) program is an initiative sponsored by the Internal Revenue Service.
- [d10s1]  Founded in 1971 by Gary Iskowitz at California State University, Northridge.
- [d10s2]  Since the 1970s the program has blossomed to several thousand sites nationwide partnering with non-profit organizations, city governments, and major public universities to file millions of returns every year.
- [d10s3]  In Tax Year 2015 3.7 million returns were filed with a 94% accuracy rate according to Frank Nolden, Director of Stakeholder Partnerships, Education, and Communication/SPEC.
- [d10s4]  The program is intended to service low to moderate-income tax payers, which the IRS has defined for the scope of the program as those individuals and families making less than $54,000 per year.

## 14. hotpotqa_5a88b15b5542994846c1ceba

原位置：`dev` 第 41 题 · 全局第 284 题 · `sample_id: hotpotqa_5a88b15b5542994846c1ceba`

Question: Chino Moreno and Needtobreathe, are of which nationality?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: multipart · fallback: False · SFT snapshots: 6

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | nationality of Chino Moreno | True | [] | American | [["d10s0"]] | context |
| u2 | nationality of Needtobreathe | True | [] | American | [["d1s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | nationality of Chino Moreno | False | [] | American | [['d10s0']] |
| u2 | nationality of Needtobreathe | False | [] | American | [['d1s0']] |
| u3 | nationality shared by Chino Moreno and Needtobreathe | True | ['u1', 'u2'] | American | [[]] |

### Source documents (reference only)

**d1: Needtobreathe**

- [d1s0] Needtobreathe (stylized as NEEDTOBREATHE) is an American Christian rock band from Seneca, South Carolina, United States.
- [d1s1]  The band is composed of Bear Rinehart (lead vocals, guitar, piano), Bo Rinehart (backing vocals, guitar), Seth Bolt (backing vocals, bass) and Josh Lovelace (backing vocals, keys).
- [d1s2]  To date they have released six studio albums: "Daylight" (2006), "The Heat" (2007), "The Outsiders" (2009), "The Reckoning" (2011), "Rivers in the Wasteland" (2014), and "Hard Love" (2016).

**d2: Palms (album)**

- [d2s0] Palms is the first studio album by the rock band Palms.
- [d2s1]  It was released in 2013 in CD digipack, limited edition vinyl, limited edition cassette and digital download formats by Ipecac Records.
- [d2s2]  The album was made available for streaming by "Spin" on June 18, 2013, one week before its release.
- [d2s3]  Upon its release, "Palms" debuted at No. 55 on the "Billboard" 200 and received positive reviews.
- [d2s4]  The album has been described as post-metal and alternative rock, much like singer Chino Moreno's main band, Deftones.

**d3: Team Sleep**

- [d3s0] Team Sleep is an American experimental alternative rock/post-rock group led by singer/guitarist Chino Moreno.
- [d3s1]  Moreno is better known for fronting the Sacramento-based alternative metal band Deftones.
- [d3s2]  Other current members include guitarist Todd Wilkinson, turntablist DJ Crook, bass guitarist/keyboardist Rick Verrett, drummer Gil Sharone and bassist Chuck Doom.

**d4: Droid (album)**

- [d4s0] Droid is the self-titled debut album from groove metal band Droid.
- [d4s1]  Released on James "Munky" Shaffer's independent record label Emotional Syphon Records it features guest vocals from Deftones frontman Chino Moreno.

**d5: The Raid: Redemption (soundtrack)**

- [d5s0] The Raid: Redemption is a soundtrack/score album composed by Joseph Trapanese and Linkin Park's co-vocalist Mike Shinoda, who also serves as producer for the album, which was originally inspired from the 2012 live-action film "".
- [d5s1]  The first official single from the album is "Razors Out" by Chino Moreno and Shinoda.
- [d5s2]  The second single released for the film is "Suicide Music" by Get Busy Committee and Shinoda.
- [d5s3]  The two singles were released as a double single on March 16, 2012.

**d6: Tempest (Deftones song)**

- [d6s0] "Tempest" is the second single by Sacramento, California-based alternative metal band Deftones, from their seventh studio album, "Koi No Yokan".
- [d6s1]  The song debuted on PureVolume's official website on October 3, 2012 along with a video featuring band members Chino Moreno and Sergio Vega giving some insight regarding the track.
- [d6s2]  The song's lyrical content is representative of the supposed end of the world that would have occurred on December 21, 2012, according to various myths related to the Mayan calendar.
- [d6s3]  It was featured in the trailer for the film "Jack the Giant Slayer" and an episode of "The Following".
- [d6s4]  An instrumental version made an appearance in the film "Furious 7".

**d7: Tried + True**

- [d7s0] Tried + True is the third and final studio album by Tinfed, released on August 22, 2000 by Hollywood Records.
- [d7s1]  It was produced by Ed Buller, known for his work with English groups such as Suede, Spiritualized and Slowdive.
- [d7s2]  The song "Dangergirl" features a guest appearance by Chino Moreno, lead vocalist of Deftones.
- [d7s3]  The album also contains "Immune", which was featured in the 2000 film "" and appeared on its .

**d8: Crosses (band)**

- [d8s0] Crosses (usually stylized as †††) is the musical side project of Deftones singer Chino Moreno, Far guitarist Shaun Lopez and Chuck Doom, based in Los Angeles, California, and formed in 2011.

**d9: Vices (Dead Poetic album)**

- [d9s0] Vices is the third full-length album by Christian hard rock band Dead Poetic.
- [d9s1]  The album was released on October 31, 2006 through Tooth & Nail Records.
- [d9s2]  Aaron Sprinkle once again produced the album, and Chino Moreno of Deftones contributed guest vocals to "Paralytic."
- [d9s3]  Lead vocalist Brandon Rike left the band shortly before the album's release and the band's remaining members opted not to continue with the band, although recently it has been stated that the band has not broken up, and will continue writing music.

**d10: Chino Moreno**

- [d10s0] Chino Moreno (born Camillo Wong Moreno; June 20, 1973) is an American musician.
- [d10s1]  He is best known as the lead vocalist and contributing guitarist of Deftones.
- [d10s2]  He is also a member of the side-project groups Team Sleep, Crosses, Saudade, and Palms.

## 15. hotpotqa_5a9060f05542990a98493604

原位置：`dev` 第 42 题 · 全局第 285 题 · `sample_id: hotpotqa_5a9060f05542990a98493604`

Question: What novel written by an American novelist born in 1804 was adapted into a British silent drama film?

Note: 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | American novelist born in 1804 | False | [] | Nathaniel Hawthorne | [["d7s0"]] | context |
| u2 | novel by {u1} adapted into a British silent drama film | True | ["u1"] | The Scarlet Letter | [["d2s0", "d2s1"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | American novelist born in 1804 | False | [] | Nathaniel Hawthorne | [['d7s0']] |
| u2 | novel by {u1} adapted into a British silent drama film | True | ['u1'] | The Scarlet Letter | [['d2s0', 'd2s1']] |

### Source documents (reference only)

**d1: Mumsie**

- [d1s0] Mumsie is a 1927 British silent drama film directed by Herbert Wilcox and starring Pauline Frederick, Nelson Keys and Herbert Marshall.
- [d1s1]  It was adapted from a play by Edward Knoblock about a favourite son of a family who proves to be a coward when war breaks out.
- [d1s2]  Pauline Frederick's last silent film.
- [d1s3]  "Mumsie" is a lost film.
- [d1s4]  It was made at Twickenham Studios.

**d2: The Scarlet Letter (1922 film)**

- [d2s0] The Scarlet Letter is a 1922 British silent drama film directed by Challis Sanderson and starring Sybil Thorndike, Tony Fraser and Dick Webb.
- [d2s1]  It is an adaptation of the novel "The Scarlett Letter" by Nathaniel Hawthorne.

**d3: Love in the Wilderness**

- [d3s0] Love in the Wilderness is a 1920 British silent drama film directed by Alexander Butler and starring Madge Titheradge, C.M. Hallard and Campbell Gullan.
- [d3s1]  It was adapted from Gertrude Page's novel of the same name.
- [d3s2]  The film is a romantic melodrama, set partly on a farm in Southern Rhodesia.
- [d3s3]  The film was shot in California.

**d4: God's Clay (1919 film)**

- [d4s0] God's Clay is a 1919 British silent drama film directed by Arthur Rooke and starring Janet Alexander, Humberston Wright and Maud Yates.
- [d4s1]  It is an adaptation of the novel "God's Clay" by Claude Askew and Alice Askew.
- [d4s2]  The story was adapted for a 1928 film "God's Clay" directed by Graham Cutts.

**d5: Far from the Madding Crowd (1915 film)**

- [d5s0] Far from the Madding Crowd is a 1915 British silent drama film produced and directed by Laurence Trimble and starring Florence Turner, Henry Edwards and Malcolm Cherry.
- [d5s1]  Trimble also adapted Thomas Hardy's 1874 novel for the screen.
- [d5s2]  "Far from the Madding Crowd" is a lost film.

**d6: The Manxman**

- [d6s0] The Manxman is a 1929 British silent drama film directed by Alfred Hitchcock and starring Anny Ondra, Carl Brisson and Malcolm Keen.
- [d6s1]  The film is based on a popular 1894 romantic novel "The Manxman" by Hall Caine, which had previously been made into a film 12 years earlier.
- [d6s2]  It was the last silent film that Hitchcock directed before he made the transition to sound film with his next film "Blackmail".

**d7: Nathaniel Hawthorne**

- [d7s0] Nathaniel Hawthorne ( ; born Nathaniel Hathorne; July 4, 1804 – May 19, 1864) was an American novelist, dark romantic, and short story writer.

**d8: The Manxman (1916 film)**

- [d8s0] The Manxman (also known as The Manx-Man) is a 1916 British silent drama film directed by George Loane Tucker and starring Henry Ainley, Adeline Hayden Coffin and Will Corrie.
- [d8s1]  It is based on the novel the 1894 novel of the same name by Hall Caine.
- [d8s2]  A second, silent adaptation was released in 1929; and directed by Alfred Hitchcock.

**d9: Lamp in the Desert**

- [d9s0] Lamp in the Desert is a 1922 British silent drama film directed by F. Martin Thornton and starring Gladys Jennings, Louis Willoughby and George K. Arthur.
- [d9s1]  It was adapted from a novel by Ethel M. Dell.

**d10: The Ever Open Door**

- [d10s0] The Ever Open Door is a 1920 British silent drama film directed by Fred Goodwins and starring Hayford Hobbs, Daphne Glenne and Margaret Hope.
- [d10s1]  It was based on the play "The Ever Open Door" by George R. Sims, a leading Victorian writer of stage melodramas.
- [d10s2]  It was one of a number of Sim's plays to be adapted for cinema during the Silent era.

## 16. hotpotqa_5ab2585855429970612095e6

原位置：`dev` 第 43 题 · 全局第 286 题 · `sample_id: hotpotqa_5ab2585855429970612095e6`

Question: Between the Akita and Boykin Spaniel, which dog breed is larger?

Note: 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | size of the Akita dog breed | False | [] | large | [["d8s0"]] | context |
| u2 | size of the Boykin Spaniel dog breed | False | [] | medium-sized | [["d5s0"]] | context |
| u3 | which of the Akita and the Boykin Spaniel is the larger dog breed | True | ["u1", "u2"] | Akita | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | size of the Akita dog breed | False | [] | large | [['d8s0']] |
| u2 | size of the Boykin Spaniel dog breed | False | [] | medium-sized | [['d5s0']] |
| u3 | which of the Akita and the Boykin Spaniel is the larger dog breed | True | ['u1', 'u2'] | Akita | [[]] |

### Source documents (reference only)

**d1: Picardy Spaniel**

- [d1s0] The Picardy Spaniel is a breed of dog developed in France for use as a gundog.
- [d1s1]  It is related to the Blue Picardy Spaniel, and still has many similarities, but the Picardy Spaniel is the older of the two breeds.
- [d1s2]  It is thought to be one of the two oldest continental spaniel breeds and was favoured by the French nobility, remaining popular for hunting after the French Revolution due to its weather resistant coat that enabled it to hunt in a variety of conditions and terrain.
- [d1s3]  However its popularity waned following the influx of English hunting breeds in the early 20th century.
- [d1s4]  Slightly smaller than an English Setter but larger than most of its spaniel cousins, it has no major health issues although as with many breeds with pendulous ears, it can be prone to ear infections.

**d2: Welsh Springer Spaniel**

- [d2s0] The Welsh Springer Spaniel is a breed of dog and a member of the spaniel family.
- [d2s1]  Thought to be comparable to the old Land Spaniel, they are similar to the English Springer Spaniel and historically have been referred to as both the Welsh Spaniel and the Welsh Cocker Spaniel.
- [d2s2]  They were relatively unknown until a succession of victories in dog trials by the breed increased its popularity.
- [d2s3]  Following recognition by The Kennel Club in 1902, the breed gained the modern name of Welsh Springer Spaniel.
- [d2s4]  The breed's coat only comes in a single colour combination of white with red markings, usually in a piebald pattern.
- [d2s5]  Loyal and affectionate, they can become very attached to family members and are wary of strangers.
- [d2s6]  Health conditions are limited to those common among many breeds of dog, although they are affected more than average by hip dysplasia and some eye conditions.
- [d2s7]  They are a working dog, bred for hunting, and while not as rare as some varieties of spaniel, they are rarer than the more widely known English Springer Spaniel with which they are sometimes confused.

**d3: Breed standard (dogs)**

- [d3s0] A breed standard (also called bench standard or the standard) in the dog fancy is a set of guidelines covering specific "externally observable" qualities such as "appearance", "movement", and "temperament" for that dog breed.
- [d3s1]  Breed standards are not scientific documents, but are written for each breed by clubs of hobbyists called breed clubs for their own specific requirements.
- [d3s2]  Details and definitions within breed standards for a specific dog breed may vary from breed club to breed club and from country to country.
- [d3s3]  Dog breed standards are similar in form and function to breed standards for other domesticated animals.

**d4: English Cocker Spaniel**

- [d4s0] The English Cocker Spaniel is a breed of gun dog.
- [d4s1]  The English Cocker Spaniel is an active, good-natured, sporting dog standing well up at the withers and compactly built.
- [d4s2]  There are "field" or "working" cockers and "show" cockers.
- [d4s3]  It is one of several varieties of spaniel and somewhat resembles its American cousin, the American Cocker Spaniel, although it is closer to the working-dog form of the Field Spaniel and the English Springer Spaniel.

**d5: Boykin Spaniel**

- [d5s0] The Boykin Spaniel is a medium-sized breed of dog, a Spaniel bred for hunting wild turkeys and ducks in the Wateree River Swamp of South Carolina, in the United States.
- [d5s1]  It is the state dog of South Carolina, where it was discovered and further developed by hunters in the 1900s.
- [d5s2]  1 September is Boykin Spaniel Day in South Carolina.

**d6: Alpine Spaniel**

- [d6s0] The Alpine Spaniel is an extinct breed of dog which was used in mountain rescues by the Augustinian Canons, who run hospices in the region around the Great St. Bernard Pass.
- [d6s1]  The spaniel was a large dog notable for its thick curly coat.
- [d6s2]  One of the most famous specimens of the Alpine Spaniel is Barry, however his preserved body has been modified on more than one occasion to fit with descriptions of the extinct breed from earlier time periods.
- [d6s3]  Due to the conditions in the Alps, and a series of accidents, extinction was discussed as a possibility by authors during the 1830s, and at some point prior to 1847 the entire breed was reduced to a single example due to disease.
- [d6s4]  Evidence held at the Natural History Museum in Bern show that two distinct breeds of dog were being used in the area during this time period.
- [d6s5]  The breed is thought to be the predecessor to the modern St. Bernard and the Clumber Spaniel.

**d7: King Charles Spaniel**

- [d7s0] The King Charles Spaniel (also known as the English Toy Spaniel) is a small dog breed of the spaniel type.
- [d7s1]  In 1903, the Kennel Club combined four separate toy spaniel breeds under this single title.
- [d7s2]  The other varieties merged into this breed were the Blenheim, Ruby and Prince Charles Spaniels, each of which contributed one of the four colours available in the breed.

**d8: Akita (dog)**

- [d8s0] The Akita (秋田犬 , Akita-inu, Akita-ken ) is a large breed of dog originating from the mountainous northern regions of Japan.
- [d8s1]  There are two separate varieties of Akita: a "Japanese" strain, commonly called "Akita Ken" in Japan, "Akita Inu" ("inu" means "dog" in Japanese), or "Japanese Akita"; and an "American" strain, known as the "Akita" or "American Akita".
- [d8s2]  The Japanese strain called the Akita Inu comes in a narrow palette of colors, with all other colors considered atypical of the breed, while the American strain known simply as the Akita comes in all dog colors.
- [d8s3]  The Akita has a short double-coat similar to that of many other northern spitz breeds such as the Siberian Husky, but long-coated dogs can be found in many litters due to a recessive gene.

**d9: American Cocker Spaniel**

- [d9s0] The American Cocker Spaniel is a breed of sporting dog.
- [d9s1]  It is a spaniel type dog that is closely related to the English Cocker Spaniel; the two breeds diverged during the 20th century due to differing breed standards in America and the UK.
- [d9s2]  In the United States, the breed is usually called the Cocker Spaniel, while elsewhere in the world, it is called the American Cocker Spaniel in order to differentiate between it and its English cousin, which was already known as "Cocker Spaniel" before the American variety was created.
- [d9s3]  The word "cocker" is commonly held to stem from their use to hunt woodcock in England, while "spaniel" is thought to be derived from the type's origins in Spain.

**d10: English Springer Spaniel**

- [d10s0] The English Springer Spaniel is a breed of gun dog in the Spaniel family traditionally used for flushing and retrieving game.
- [d10s1]  It is an affectionate, excitable breed with a typical lifespan of twelve to fourteen years.
- [d10s2]  They are very similar to the Welsh Springer Spaniel and are descended from the Norfolk or Shropshire Spaniels of the mid-19th century; the breed has diverged into separate show and working lines.
- [d10s3]  The breed suffers from average health complaints.
- [d10s4]  The show-bred version of the breed has been linked to "rage syndrome", although the disorder is very rare.
- [d10s5]  It is closely related to the Welsh Springer Spaniel and very closely to the English Cocker Spaniel; less than a century ago, springers and cockers would come from the same litter.
- [d10s6]  The smaller "cockers" hunted woodcock while the larger littermates were used to flush, or "spring," game.
- [d10s7]  In 1902, The Kennel Club recognized the English Springer Spaniel as a distinct breed.
- [d10s8]  They are used as sniffer dogs on a widespread basis.
- [d10s9]  The term "Springer" comes from the historic hunting role, where the dog would flush (spring) birds into the air.

## 17. hotpotqa_5ab27ea3554299340b5254e4

原位置：`dev` 第 44 题 · 全局第 287 题 · `sample_id: hotpotqa_5ab27ea3554299340b5254e4`

Question: are Meet the Patels and Arakimentari the same genre of film

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | genre of Meet the Patels | False | [] | documentary | [["d8s0"], ["d1s1"]] | context |
| u2 | genre of Arakimentari | False | [] | documentary | [["d9s1"]] | context |
| u3 | whether Meet the Patels and Arakimentari are the same genre of film | True | ["u1", "u2"] | yes | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | genre of the film Meet the Patels | False | [] | documentary | [['d8s0'], ['d1s1']] |
| u2 | genre of the film Arakimentari | False | [] | documentary | [['d9s1']] |
| u3 | whether Meet the Patels and Arakimentari are the same genre of film | True | ['u1', 'u2'] | yes | [[]] |

### Source documents (reference only)

**d1: Ravi Patel (actor)**

- [d1s0] Ravi Vasant Patel (born December 18, 1978) is an American television and film actor.
- [d1s1]  He has also written and directed, with his sister, an autobiographical documentary, "Meet the Patels".
- [d1s2]  He married fellow actor Mahaley Patel (nee Hessam) on May 7, 2015.

**d2: Alvin and the Chipmunks Meet the Wolfman**

- [d2s0] Alvin and the Chipmunks Meet the Wolfman is a 2000 animated horror musical comedy-themed direct-to-video film, produced by Bagdasarian Productions and Universal Cartoon Studios, distributed by Universal Studios Home Entertainment, and based on characters from "Alvin and the Chipmunks".
- [d2s1]  It was released on VHS in 2000 and DVD (as a "Monster Pack" with "Alvin and the Chipmunks Meet Frankenstein", "Monster Mash", and four episodes of "Archie's Weird Mysteries") in 2004 by Universal Studios Home Entertainment.
- [d2s2]  A Scare-riffic Double Feature DVD featuring "Alvin and the Chipmunks Meet Frankenstein" and this film was released on September 4, 2007.
- [d2s3]  Another Scare-riffic Double Feature DVD featuring "Alvin and the Chipmunks Meet Frankenstein" and this film was re-released on March 11, 2008.

**d3: Discourse types**

- [d3s0] The term discourse type is preferred to other labels which might be encountered in linguistics, such as "text-type" or "genre" since, for some, "text-type" implies work on written texts, whereas much of CADS has been carried out on spoken discourse , and "genre" is a term which is accompanied by huge baggage in literature, and some of the discourse types we may wish to examine might not meet everyone’s criteria of what constitutes a “genre”.
- [d3s1]  For instance, Parliamentary debates on the Iraq war, White House press briefings, or the speeches of Silvio Berlusconi, all objects of recent Corpus Assisted Discourse Studies (CADS) scrutiny , may not be classifiable as separate genres.

**d4: Genre criticism**

- [d4s0] Genre criticism is a method within rhetorical criticism for analyzing texts in terms of their genre: the set of generic expectations, conventions, and constraints that guide their production and interpretation.
- [d4s1]  In rhetoric, the theory of genre provides a means to classify and compare artifacts in terms of their formal, substantive and contextual features.
- [d4s2]  By grouping artifacts with others of similar formal features or rhetorical exigencies, rhetorical critics can shed light on how authors use or flout conventions in order to meet their needs.
- [d4s3]  Genre criticism has thus become one of the main methodologies within rhetorical criticism.

**d5: Biographical novel**

- [d5s0] The biographical novel is a genre of novel which provides a fictional account of a contemporary or historical person's life.
- [d5s1]  This kind of novel concentrates,on the experiences a person had during his lifetime, the people they meet and the incidents which occurred.
- [d5s2]  Like other forms of biographical fiction, details are often trimmed or reimagined to meet the artistic needs of the fictional genre, the novel.
- [d5s3]  These reimagined biographies are sometimes called semi-biographical novels, to distinguish the relative historicity of the work from other biographical novels

**d6: Solid Patels**

- [d6s0] Solid Patels is a 2015 Bollywood Hindi comedy film directed by Saurabh Varma and produced by Nitika thakur.
- [d6s1]  The film stars Shiv Pandit, Kettan Singh, Shazahn Padamsee, Vaishali Desai, and Ali Asgar.
- [d6s2]  The film is slated to release on 22 May 2015.
- [d6s3]  The first look of the film was released on 18 December 2014 and the trailer was launched on 18 March 2015.

**d7: Oye Hoye Pyar Ho Gaya**

- [d7s0] Oye Hoye Pyar Ho Gaya is a 2013 Punjabi film directed by Aditya Sood and starring Sharry Mann, Jimmy Sharma, Niharika Kareer as the main cast of the film and will release on 14 June 2013.
- [d7s1]  ‘Oye Hoye Pyar Ho Gaya’ is a story of two fun loving friends Sharry (Sharry Mann) and Harry (Rana Ranbir).
- [d7s2]  Sharry falls for Meet (Niharika Kareer), who is daughter of Police Commissioner Shamsher Singh (Yograj Singh).
- [d7s3] Chamkila (Binnu Dhillon) who is also trying his chances on Meet gets envy of Sharry and tries tarnishing his image in front of Meet’s family.
- [d7s4]  Kartar (Jimmy Sharma) son of Police Commissioner and elder brother of meet so he is the main hurdle whom sharry has to pass in the story and commissioner discuss everything with him before taking any decision.

**d8: Meet the Patels**

- [d8s0] Meet the Patels is a 2014 American romantic comedy documentary film directed by siblings Geeta V. Patel and Ravi V. Patel.
- [d8s1]  The film explores the expectations surrounding marriage in the Patels' first-generation Indian immigrant family and in wider American society.
- [d8s2]  It had its international premiere at Hot Docs in April 2014.

**d9: Arakimentari**

- [d9s0] Arakimentari is a 2004 American film directed by Travis Klose.
- [d9s1]  It is a documentary film about acclaimed and controversial Japanese photographer Nobuyoshi Araki.
- [d9s2]  The film looks at Araki's personal life as well as his art.

**d10: Kevi Rite Jaish**

- [d10s0] Kevi Rite Jaish is a 2012 Indian Gujarati-language drama film directed by Abhishek Jain and produced by Nayan Jain.
- [d10s1]  The film is a satire on the fascination and obsession of the Patels' - a Gujarati farmer community - migration to the U.S. Over the last half century, thousands of Patels have migrated to the U.S.A and have come to dominate its motel industry.
- [d10s2]  The film stars Divyang Thakkar, Veronica Kalpana-Gautam, Tejal Panchasara, Kenneth Desai, and Anang Desai.

## 18. hotpotqa_5ab2a4a7554299295394678b

原位置：`dev` 第 45 题 · 全局第 288 题 · `sample_id: hotpotqa_5ab2a4a7554299295394678b`

Question: What year was the founder of Mac Fisheries born?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | founder of Mac Fisheries | False | [] | William Lever, 1st Viscount Leverhulme | [["d5s0"]] | context |
| u2 | birth year of {u1} | True | ["u1"] | 1851 | [["d7s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | founder of Mac Fisheries | False | [] | William Lever, 1st Viscount Leverhulme | [['d5s0']] |
| u2 | birth year of {u1} | True | ['u1'] | 1851 | [['d7s0']] |

### Source documents (reference only)

**d1: Fin Donnelly**

- [d1s0] Fin Donnelly (born May 27, 1966) is a Canadian politician, who was elected to the House of Commons of Canada to represent the electoral district of Port Moody—Coquitlam.
- [d1s1]  He is a member of the New Democratic Party.
- [d1s2]  Donnelly was first elected as a member of parliament in a by-election on November 9, 2009, in the New Westminster—Coquitlam electoral district.
- [d1s3]  In the one year he spent in the 40th Canadian Parliament, he acted as the party's fisheries critic and introduced six private member bills.
- [d1s4]  He was re-elected in 2011 and in the ensuing 41st Parliament he re-introduced the same six bills, two of which, concerning the crime of luring a child were adopted, were adopted in the "Safe Streets and Communities Act".
- [d1s5]  He also introduced the bill titled "Ban on Shark Fin Importation Act" which was voted upon but defeated by the Conservative Party majority.
- [d1s6]  He acted was the official opposition's critic on Fisheries and Oceans until the 2012 leadership election after which Tom Mulcair moved him over to critic on Western Economic Diversification and then demoted him to role of deputy critic.
- [d1s7]  Donnelly again won re-election in the 2015 federal election and was promoted back to fisheries critic.
- [d1s8]  In the 42nd Parliament he re-introduced his previous bill to make closed containment facilities mandatory for commercial finfish aquaculture but the bill was defeated.

**d2: Charles Gordon (Canadian football)**

- [d2s0] Charles Gordon (born July 30, 1968 in Tampa, Florida) is a former American/Canadian FootballLeague player who attended Eastern Michigan University from 1986–1989 earning All-Mid American Conference (MAC) honors for three consecutive years including: 1986 Runner-Up for MAC Freshman of the Year and 1986 Sporting News Freshman All America Head of the Class (Special Mention); 1987 - 1st Team All Mid-American Conference (MAC) 1987- 3rd Team Football News Sophomore All America 1987 AP All America (Honorable Mention).
- [d2s1]  Helped lead Eastern Michigan University to its first and only MAC championship 10–2 overall record and 7–1 conference record.
- [d2s2]  Went to the 1987 California Bowl and upset 17½ point favorite San Jose State University for the only bowl game win in EMU history.

**d3: David George Stead**

- [d3s0] David George Stead (6 March 1877 – 2 August 1957) was an Australian marine biologist, ichthyologist, oceanographer, conservationist and writer.
- [d3s1]  He was born at St Leonards in Sydney, and educated at public schools and the Sydney Technical College.
- [d3s2]  In 1909 he was a founder of, and during its early years the main driving force behind, the Wildlife Preservation Society of Australia.
- [d3s3]  In December 1912 he became an inaugural committee member of the Eugenics Society of New South Wales.
- [d3s4]  His career included many government positions both in Australia and in Malaya.
- [d3s5]  He served as the Australian representative on international committees concerned with fisheries science, marine biology and oceanography.
- [d3s6]  He married three times, the third time to botanist and writer Thistle Yolette Harris in 1951.
- [d3s7]  He died at his home in Watsons Bay, Sydney.

**d4: Mahadev Jankar**

- [d4s0] Mahadev Jankar (Marathi: महादेव जानकर (Born on 19 April 1968) is senior Cabinate Minister in Government of Maharashtra as Minister for Animal Husbandry,Dairy Development and Fisheries Development.
- [d4s1]  He is Indian Politician and founder and National President of Rashtriya Samaj Paksha (Rashtriya Samaj Party) an Indian political party based in Maharashtra, founded in 2003.

**d5: Mac Fisheries**

- [d5s0] Mac Fisheries was a branded United Kingdom retail chain of fishmongers, founded by William Lever, 1st Viscount Leverhulme, the co-founder with his brother of Lever Brothers, which later merged to become Unilever.

**d6: Sidney Holt**

- [d6s0] Sidney J. Holt (born 28 February 1926) is a founder of fisheries science.
- [d6s1]  He is best known for the book "On the Dynamics of Exploited Fish Populations" which he published with Ray Beverton in 1957.
- [d6s2]  The book is a cornerstone of modern fisheries science and remains much used today.
- [d6s3]  Holt served with the FAO in 1953 and with other UN agencies for another 25 years.
- [d6s4]  After his retirement in 1979, Holt has remained active in work related to the International Whaling Commission and conservation of whales in general, also publishing his views about whaling and fisheries management in academic journals.

**d7: William Lever, 1st Viscount Leverhulme**

- [d7s0] William Hesketh Lever, 1st Viscount Leverhulme ( ; 19 September 1851 – 7 May 1925) was an English industrialist, philanthropist, and politician.
- [d7s1]  Having been educated at a small private school until the age of nine, then at church schools until he was fifteen; a somewhat privileged education for that time, he started work at his father's wholesale grocery business in Bolton.
- [d7s2]  Following an apprenticeship and a series of appointments in the family business, which he successfully expanded, he began manufacturing Sunlight Soap, building a substantial business empire with many well-known brands such as Lux and Lifebuoy.
- [d7s3]  In 1886, together with his brother, James, he established Lever Brothers, which was one of the first companies to manufacture soap from vegetable oils, and which is now part of the Anglo-Dutch transnational business Unilever.
- [d7s4]  In politics, Lever briefly sat as a Liberal MP for Wirral and later, as Lord Leverhulme, in the House of Lords as a Peer.
- [d7s5]  He was an advocate for expansion of the British Empire, particularly in Africa and Asia, which supplied palm oil, a key ingredient in Lever's product line.

**d8: Said bin Salim Al Shaksy**

- [d8s0] Said bin Salim Al Shaksy (Arabic: سعيد بن سالم الشقصي) (born Zanzibar in 1934 - 2015) was the founder and chairman of The Shaksy Group.
- [d8s1]  Al Shaksy has been a member and Managing Director of several Joint-Stock Companies, including Al Bank Al Ahli Al Omani SAOG, Oman Fisheries Co.
- [d8s2]  SAOG and Oman Hotels Co.
- [d8s3]  SAOG.

**d9: Pete Bethune**

- [d9s0] Captain Peter James "Pete" Bethune (born 4 April 1965) is a New Zealander, ship's captain with 500 ton master license, published author, producer of "The Operatives" TV Show, and public speaker.
- [d9s1]  He is the founder of "Earthrace Conservation" .
- [d9s2]  He works assisting countries in Asia, Central America and Africa with fisheries enforcement and anti-poaching.
- [d9s3]  He is the holder of the world record for circumnavigating the globe in his powerboat "Earthrace", a wavepiercing trimaran powered with biofuels.

**d10: Marc Rowell**

- [d10s0] Marcus Hosking "Marc" Rowell (born 5 April 1938) is a former Australian politician.
- [d10s1]  Born in Beecroft, New South Wales, he was a cane farmer and fruit grower in Queensland before entering politics.
- [d10s2]  In 1989, he was elected to the Legislative Assembly of Queensland as the National Party member for Hinchinbrook.
- [d10s3]  In 1998 he was appointed Minister for Primary Industries, Fisheries and Forestry, but lost the position when the Coalition was defeated at elections later that year.
- [d10s4]  Rowell held various posts in the shadow ministry, but retired at the 2006 state election.

## 19. hotpotqa_5ab33cec554299753aec595c

原位置：`dev` 第 46 题 · 全局第 289 题 · `sample_id: hotpotqa_5ab33cec554299753aec595c`

Question: When would be the album release in which "Too Much to Ask" is the third single song?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | album containing "Too Much to Ask" as the third single | False | [] | Flicker | [["d9s2"]] | context |
| u2 | release date of {u1} | True | ["u1"] | October 20, 2017 | [["d3s1"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | album for which Too Much to Ask was the third single | False | [] | Flicker | [['d9s2']] |
| u2 | release date of {u1} | True | ['u1'] | October 20, 2017 | [['d3s1']] |

### Source documents (reference only)

**d1: Re-Entry (Big Brovaz album)**

- [d1s0] Re-Entry is the second album released by UK R&B/hip-hop collective Big Brovaz.
- [d1s1]  After the album was delayed in May 2006, the band finally release the follow-up to "Nu Flow" on 9 April 2007.
- [d1s2]  Following the first single, "Yours Fatally" and the second single "Hangin' Around", the third single from the album, "Big Bro Thang", was received a staggared download only single release in February and March 2007.
- [d1s3]  The album release also contain the Booty Luv hit "Boogie 2nite" as a bonus track.

**d2: Have You Ever (S Club 7 song)**

- [d2s0] "Have You Ever" was a single released by UK pop group S Club 7 on 19 November 2001.
- [d2s1]  Following the success of the 2000 "Children in Need" track, "Never Had a Dream Come True", the BBC asked S Club 7 to perform the 2001 track for the charity too.
- [d2s2]  "Have You Ever" was co-written by Cathy Dennis, A. Frampton and Chris Braide.
- [d2s3]  The track is the penultimate ballad S Club 7 released as a single with lead vocals coming from singer Jo.
- [d2s4]  "Have You Ever" acted as an introduction to S Club 7's third album "Sunshine".
- [d2s5]  The single entered the UK Singles Chart at number one on 25 November 2001, and remained on the chart for 14 weeks (seven of which were in the top 10).
- [d2s6]  The Children in Need version of "Have You Ever" is listed in the "Guinness Book of World Records" as having the highest number of people's voices recorded in a single song; as recordings from children in schools across the UK were used in the chorus.
- [d2s7]  The song has sold 380,000 copies in the UK according to the Official UK Charts Company.
- [d2s8]  The photo for the cover of the single was shot in another major architectural landmark of the Los Angeles area - the Sheats Goldstein Residence near Beverly Hills.

**d3: Flicker (album)**

- [d3s0] Flicker is the upcoming debut studio album by Irish singer and songwriter Niall Horan.
- [d3s1]  It is scheduled for release on October 20, 2017, through Neon Haze Music and Capitol Records. "
- [d3s2] This Town" was released on 29 September 2016, as the album's lead single, followed by 2017 singles "Slow Hands" and "Too Much to Ask".

**d4: Glasgow Monday**

- [d4s0] Glasgow Monday is the 47th release, third live album, and second-ever double album release, from avant-folk/blues singer/songwriter Jandek.
- [d4s1]  It is his fifth release of the year (counting the DVD version of "Glasgow Sunday") and features "The Corwood Representative" on piano and vocals, along with the same rhythm section he performed with at the shows documented on "Glasgow Sunday" and "Newcastle Sunday", bassist Richard Youngs (playing upright bass) and drummer/percussionist Alex Neilson who accents the music with chimes and echoing percussion.
- [d4s2]  It was recorded live at the Center for Contemporary Arts in Glasgow, Scotland on May 23, 2005 and features a prelude and nine parts to a single song, "The Cell".

**d5: To the Metal!**

- [d5s0] To The Metal!
- [d5s1]  is the tenth full-length studio album by Gamma Ray.
- [d5s2]  It was released on 29 January 2010.
- [d5s3]  To promote the album, the band did a tour with Freedom Call and Secret Sphere.
- [d5s4]  The album was recorded in Kai's own studio in Hamburg in autumn 2009.
- [d5s5]  The band has recorded 12 songs.
- [d5s6]  Ten of them were featured on the regular album release, while the other two were bonus tracks appearing on the different editions of the album.
- [d5s7]  The band described some of the songs on the official website, revealing that there would be a full-throttle number called "Rise", a rhythmic and melodically diverse song called "Time To Live", and a multilayered anthem titled "All you need to know", featuring ex-Helloween frontman Michael Kiske.
- [d5s8]  Other songs mentioned are "No Need to Cry", a song written by Dirk Schlächter about the death of his father, "To The Metal", a song they played on various festivals before the album release and the atmospheric and dense "Empathy".
- [d5s9]  It is the last album featuring drummer Dan Zimmermann.

**d6: @Reverend Makers**

- [d6s0] @Reverend_Makers is the third album by English band Reverend and the Makers, released on 18 June 2012.
- [d6s1]  The album's first single was "Bassline" and was released on 13 February 2012, via free download from the band's Facebook page.
- [d6s2]  The band toured the UK following the album release, after a stint supporting Noel Gallagher's High Flying Birds in early Spring.
- [d6s3]  The second single, 'The Wrestler', was released on 14 May.
- [d6s4]  Upon release, the album went to #16 in the UK Chart, three places higher than the band's second album and the third single 'Out of the Shadows' was released in August.

**d7: This Too Shall Pass (OK Go song)**

- [d7s0] "This Too Shall Pass" is a song by American rock band OK Go.
- [d7s1]  It was released as the second single from their third studio album, "Of the Blue Colour of the Sky", in January 2010.
- [d7s2]  The band took the unorthodox route of creating two official music videos for the song, both of which premiered on YouTube.
- [d7s3]  The first features a live performance of the song in collaboration with the University of Notre Dame Marching Band.
- [d7s4]  The second features a giant Rube Goldberg machine, constructed to operate in time with the song.
- [d7s5]  The popularity of the second music video of the song has been compared to that of the band's video for "Here It Goes Again", helping to boost live performances and single song sales for the group but did not significantly improve sales of the "Colour" album.
- [d7s6]  Difficulties in marketing and distribution of the videos with their corporate label, EMI, led the band to form their own independent label shortly after the videos' releases.

**d8: Tru-Kvlt-Metal**

- [d8s0] "Tru-Kvlt-Metal" is the second non-official and third single song by American melodic metalcore band All That Remains from their seventh album, "The Order of Things".
- [d8s1]  It was released February 10, 2015.

**d9: Too Much to Ask**

- [d9s0] "Too Much to Ask" is a song recorded by Irish singer and songwriter Niall Horan.
- [d9s1]  It was written by Horan and Jamie Scott, with production handled by Greg Kurstin.
- [d9s2]  The song was released through Capitol Records on 15 September 2017, as the third single from Horan's forthcoming debut studio album, "Flicker" (2017).

**d10: Time Again**

- [d10s0] Time Again is a band from Hollywood, California which is represented in the band's songs and album art.
- [d10s1]  The band was formed in the summer of 2004 by Daniel Dart, Elijah Reyes.
- [d10s2]  Before they even had a full band or a single song written, they began printing stickers and flyers for Time Again to heavily promote their band, resulting in numerous shows being booked.
- [d10s3]  Time Again only came together as a full band a few days before their first show.
- [d10s4]  The band says all their musical influences are Rancid, The Clash, and Op Ivy.
- [d10s5]  In June 2005, Time Again released a self-titled EP on Rancid Records.
- [d10s6]  This EP would result in heavy radio play on several Los Angeles radio stations, including XM Fungus 53 which would name the EP as one of the top 25 albums of 2005, and the song "I Go Back" as one of the top 10 songs of 2005.
- [d10s7]  It included a cover of Rancid's song "Tattoo".
- [d10s8]  The band released their debut full-length, "The Stories are True", on April 25, 2006, on Hellcat Records.

## 20. hotpotqa_5ab406ce55429976abd1bd36

原位置：`dev` 第 47 题 · 全局第 290 题 · `sample_id: hotpotqa_5ab406ce55429976abd1bd36`

Question: Was Lev Kuleshov and Lo Wei work in the same country?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | country where Lev Kuleshov worked | False | [] | Soviet Union | [["d9s0"], ["d3s0"]] | context |
| u2 | country where Lo Wei worked | False | [] | Hong Kong | [["d5s0"]] | context |
| u3 | whether Lev Kuleshov and Lo Wei worked in the same country | True | ["u1", "u2"] | no | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country in which Lev Kuleshov worked | False | [] | Soviet Union | [['d9s0'], ['d3s0']] |
| u2 | country in which Lo Wei worked | False | [] | Hong Kong | [['d5s0']] |
| u3 | whether Lev Kuleshov and Lo Wei worked in the same country | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: On the Red Front**

- [d1s0] On the Red Front (Russian: На красном фронте , "Na krasnom fronte " ) is a 1920 Soviet silent adventure film directed by Lev Kuleshov.

**d2: We from the Urals**

- [d2s0] We from the Urals (Russian: Мы с Урала ) is a 1944 Soviet drama film directed by Lev Kuleshov and Aleksandra Khokhlova.

**d3: Kuleshov effect**

- [d3s0] The Kuleshov effect is a film editing (montage) effect demonstrated by Soviet filmmaker Lev Kuleshov in the 1910s and 1920s.
- [d3s1]  It is a mental phenomenon by which viewers derive more meaning from the interaction of two sequential shots than from a single shot in isolation.

**d4: The Death Ray (1925 film)**

- [d4s0] The Death Ray (Russian: Луч смерти , "Luch smerti " ) is a 1925 Soviet science fiction film directed by Lev Kuleshov.
- [d4s1]  The first and last reels of the film have been lost.
- [d4s2]  This film ran at 2 hours, 5 minutes, making this one of the earliest full length science fiction films.

**d5: Lo Wei**

- [d5s0] Lo Wei (sometimes spelled Lo Wai, 12 December 1918 – 20 January 1996) was a Hong Kong film director and film actor best known for launching the martial arts film careers of both Bruce Lee, in "The Big Boss" and "Fist of Fury", and Jackie Chan, in "New Fist of Fury".

**d6: The Happy Canary**

- [d6s0] The Happy Canary or The Gay Canary (Russian: Весёлая канарейка , "Vesyolaya kanareyka " ) is a 1929 Soviet silent adventure film directed by Lev Kuleshov and starring Galina Kravchenko, Andrey Fayt and Ada Vojtsik.

**d7: To Kill with Intrigue**

- [d7s0] To Kill with Intrigue (Chinese: 劍花煙雨江南) is a Kung Fu 1977 Hong Kong action film, directed by Lo Wei.
- [d7s1]  In the movie's plot, Chin Chang Yin (Feng Hsu) leads a gang known as the Killer Bees on a revenge mission to kill Cao Lei's (Jackie Chan) family.
- [d7s2]  However, she kills everyone but Cao Lei and falls in love with him.
- [d7s3]  Jackie mentions, in his book "I Am Jackie Chan", how much of the plot is confusing, and he was sure that even the director, Lo Wei, didn't even know what was going on.
- [d7s4]  He has also gone on to express that tensions between himself and the director along with the generally cold weather at the time of filming made for a frustrating experience.
- [d7s5]  The movie was filmed in Korea.

**d8: New Fist of Fury**

- [d8s0] New Fist of Fury is a 1976 Hong Kong martial arts film directed by Lo Wei and starring Jackie Chan.
- [d8s1]  It is the first of several films that Lo directed Chan in, and the first using Chan's stage name Sing Lung (literally meaning "becoming a dragon", by which Chan is still known today in Asia).
- [d8s2]  The film gave Chan his first starring role in a widely released film (his first starring role was in the "Little Tiger of Canton" which only had a limited release in 1973).
- [d8s3]  The film was a sequel to Bruce Lee's "Fist of Fury", one of Lo Wei's biggest successes.
- [d8s4]  "New Fist of Fury" was part of Lo's attempt to market Jackie Chan as the new Bruce Lee and did not contain any of the comedy elements that were to be Chan's career trademark later on.

**d9: Lev Kuleshov**

- [d9s0] Lev Vladimirovich Kuleshov (Russian: Лев Влади́мирович Кулешо́в ; 13 January [O.S. 1 January] 1899 – 29 March 1970) was a Russian and Soviet filmmaker and film theorist, one of the founders of the world's first film school, the Moscow Film School.
- [d9s1]  He was given the title People's Artist of the RSFSR in 1969.
- [d9s2]  He was intimately involved in development of the style of film making known as Soviet montage, especially it's psychological underpinning, including the use of editing and the cut to emotionally influence the audience, a principle known as the Kuleshov effect.
- [d9s3]  He also developed the theory of creative geography, which is the use of the action around a cut to connect otherwise disparate settings into a cohesive narrative.

**d10: Magnificent Bodyguards**

- [d10s0] Magnificent Bodyguards is a 1978 Hong Kong martial arts action film starring Jackie Chan and directed by Lo Wei.
- [d10s1]  Chan, along with Luk Chuen also worked as stunt coordinators.
- [d10s2]  This film was well received in Hong Kong, but Chan himself doesn't like it.
- [d10s3]  He puts it down to Lo Wei not giving him any creative freedom.
- [d10s4]  This was the first film in Hong Kong to be filmed using 3-D technology, and it features music from "Star Wars".

## 21. hotpotqa_5ab7eff35542993667794059

原位置：`dev` 第 48 题 · 全局第 291 题 · `sample_id: hotpotqa_5ab7eff35542993667794059`

Question: What kind of musician does Neil Hannon and Stephen Malkmus have in common?

Note: 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

Type: comparison · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | kind of musician Neil Hannon is | False | [] | singer | [["d4s0"]] | context |
| u2 | kind of musician Stephen Malkmus is | False | [] | singer | [["d10s0"], ["d5s1"], ["d7s1"], ["d6s2"]] | context |
| u3 | kind of musician that Neil Hannon and Stephen Malkmus have in common | True | ["u1", "u2"] | singer | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | kind of musician Neil Hannon is | False | [] | singer | [['d4s0']] |
| u2 | kind of musician Stephen Malkmus is | False | [] | singer | [['d10s0'], ['d5s1'], ['d7s1'], ['d6s2']] |
| u3 | kind of musician that Neil Hannon and Stephen Malkmus have in common | True | ['u1', 'u2'] | singer | [[]] |

### Source documents (reference only)

**d1: Mirror Traffic**

- [d1s0] Mirror Traffic is an album by Stephen Malkmus and the Jicks, released on August 23, 2011 by Matador Records.
- [d1s1]  It is the first collaboration between Stephen Malkmus and producer Beck and also the last album to feature drummer Janet Weiss, who moved on to become a member of Wild Flag.
- [d1s2]  As of November 2013, the album has sold 30,000 copies in the U.S. according to Nielsen SoundScan.

**d2: The Crust Brothers**

- [d2s0] The Crust Brothers, a band formed by Stephen Malkmus and members of Silkworm (Michael Dahlquist, Tim Midgett, and Andy Cohen), released one album, "Marquee Mark", a live recording of their December 5, 1997, show at the Crocodile Cafe in Seattle, Washington.
- [d2s1]  The show was a benefit for the Washington Wilderness Coalition.
- [d2s2]  The band stuck exclusively to covers (Malkmus sang lead on Silkworm's "Never met a man I didn't like"), refusing to play any Pavement songs—notably the requested "Summer Babe."
- [d2s3]  Of the 12 covers on "Marquee Mark", seven are from Bob Dylan & The Band's "The Basement Tapes".

**d3: Liberation (The Divine Comedy album)**

- [d3s0] Liberation is a 1993 album by The Divine Comedy, released on Setanta.
- [d3s1]  It was the second album to be released by The Divine Comedy, although the band's leader, Neil Hannon, often refers to it as the first due to the stylistic differences of the earlier album, "Fanfare for the Comic Muse".
- [d3s2]  The album was recorded over the space of twelve days in March, 1993 by Hannon and Darren Allison.
- [d3s3]  Hannon played most of the instruments on the album, while Allison was the recording engineer and drummer.

**d4: Neil Hannon**

- [d4s0] Edward Neil Anthony Hannon (born 7 November 1970) is a Northern Irish singer and songwriter.
- [d4s1]  He is the creator and front man of the chamber pop group The Divine Comedy, and is the band's sole constant member.
- [d4s2]  Hannon wrote the theme tunes for the sitcoms "Father Ted" and "The IT Crowd".

**d5: Stephen Malkmus and the Jicks**

- [d5s0] Stephen Malkmus and the Jicks is a rock band consisting of Stephen Malkmus, Mike Clark, Joanna Bolme, and Jake Morris.
- [d5s1]  Malkmus was the main singer and songwriter behind the influential 1990s indie rock band Pavement.

**d6: Crooked Rain, Crooked Rain: LA's Desert Origins**

- [d6s0] Crooked Rain, Crooked Rain: LA's Desert Origins is a double album by Pavement released on October 26, 2004.
- [d6s1]  It contains the band's second album, "Crooked Rain, Crooked Rain" (1994) in its entirety, as well as 37 of the band's other songs from that era, 25 of which (the entire second disc) were previously unreleased.
- [d6s2]  The album also contains a 62-page booklet of liner notes, which contain photographs, artwork, accounts from vocalist/guitarist Stephen Malkmus and guitarist Scott Kannberg (a.k.a. "Spiral Stairs"), and notes Malkmus wrote for "Melody Maker" about each of the songs on the original album.
- [d6s3]  The liner notes also feature a surreal and sensationalistic "interview" between Matador's Gerard Cosloy and the fictitious "Rob Jurkface".
- [d6s4]  According to Cosloy, he took questions by Pavement's biographer, Rob Jovanovic, changed them slightly, and wrote silly answers for them.

**d7: Cut Your Hair**

- [d7s0] "Cut Your Hair" is a song by American rock band Pavement from their second album, "Crooked Rain, Crooked Rain."
- [d7s1]  It was written by Pavement songwriter and lead singer Stephen Malkmus.
- [d7s2]  The song snidely attacks the importance of image in the music industry.
- [d7s3]  In one verse, Malkmus sarcastically recites a fictitious ad looking for a musician to join a band: "advertising looks and chops a must/ no big hair".

**d8: Stephen Malkmus (album)**

- [d8s0] Stephen Malkmus is the debut album by Stephen Malkmus, released on February 13, 2001 by Matador Records.
- [d8s1]  Malkmus had planned to create the record by himself, or through a smaller, local label, but eventually accepted the offer Matador asked, and he released it.
- [d8s2]  Pre-release promotional CDs of the album exist under the working titles "Jicks" and "Swedish Reggae".
- [d8s3]  Malkmus intended to release the album as The Jicks, but Matador insisted that the album be released under his own name.
- [d8s4]  The album peaked at #124 in the US and #49 in the UK.

**d9: Range Life (song)**

- [d9s0] "Range Life" is a song by Pavement, the third single from their 1994 album "Crooked Rain, Crooked Rain".
- [d9s1]  The song attracted attention with controversial lyrics that seemed to mock alternative rock superstars the Smashing Pumpkins and the Stone Temple Pilots; Pumpkins frontman Billy Corgan expressed his displeasure in magazine interviews, while songwriter Stephen Malkmus maintained that his words had been misinterpreted and no insult was intended.
- [d9s2]  Regardless, Pavement, which was due to tour for Lollapalooza in 1994, got kicked out when the Smashing Pumpkins, the headlining act, threatened to cancel their Lollapalooza dates if Pavement played.
- [d9s3]  Pavement would eventually play Lollapalooza the next year.
- [d9s4]  An early 1993 demo of the song did not feature this verse; guitarist Spiral Stairs recalled in 2004 that when Malkmus first revealed these new lyrics to his bandmates at the New York City recording sessions for "CRCR", "we almost lost our lunch from laughing so much."
- [d9s5]  The single was not commercially released in the USA; it was issued by the band's UK label at the time, Big Cat.
- [d9s6]  Both B-sides are outtakes from the "Crooked Rain, Crooked Rain" sessions and are included on the 2004 of that album.
- [d9s7]  This song was one of many to be included in the group's greatest hits album "".

**d10: Stephen Malkmus**

- [d10s0] Stephen Joseph Malkmus (born May 30, 1966) is an American musician best known as the lead singer and guitarist of the indie rock band Pavement.
- [d10s1]  He currently performs with Stephen Malkmus and the Jicks.

## 22. hotpotqa_5ab850d75542990e739ec8c0

原位置：`dev` 第 49 题 · 全局第 292 题 · `sample_id: hotpotqa_5ab850d75542990e739ec8c0`

Question: Which writter is known to have wrote Harry Potter, Mary Gordon or J. K. Rowling?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: comparison · fallback: False · SFT snapshots: 6

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | whether Mary Gordon wrote Harry Potter | False | [] | no | [] | no_direct_support |
| u2 | whether J. K. Rowling wrote Harry Potter | False | [] | yes | [["d5s0"], ["d2s1"], ["d3s0"], ["d4s0"], ["d6s0"], ["d9s0"], ["d9s4"], ["d10s1"], ["d1s1"]] | context |
| u3 | which writer is known to have written Harry Potter | True | ["u1", "u2"] | J. K. Rowling | [[]] | question_presupposition |

- u1：无直接支持集合；不能仅由 expected_answer 将本单元标为 SUPPORTED。候选题结论可按独立的 presupposition_sets 路径判断。

- u3：`by_presupposition=true`，预设路径 `[["d5s0"], ["d2s1"], ["d3s0"], ["d4s0"], ["d6s0"], ["d9s0"], ["d9s4"], ["d10s1"], ["d1s1"]]`；不是直接证据。

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Mary Gordon wrote Harry Potter | False | [] | no | [] |
| u2 | whether J. K. Rowling wrote Harry Potter | False | [] | yes | [['d5s0'], ['d2s1'], ['d3s0'], ['d4s0'], ['d6s0'], ['d9s0'], ['d9s4'], ['d10s1'], ['d1s1']] |
| u3 | which of Mary Gordon and J. K. Rowling wrote Harry Potter | True | ['u1', 'u2'] | J. K. Rowling | [[]] |

### Source documents (reference only)

**d1: The Magical Worlds of Harry Potter**

- [d1s0] The Magical Worlds of Harry Potter: A Treasury of Myths, Legends, and Fascinating Facts is a guide to the fictional "Harry Potter" universe, written by David Colbert.
- [d1s1]  It explores the references to history, legends, and literature in J.K. Rowling's "Harry Potter" novels.
- [d1s2]  Colbert conceived the idea for "The Magical Worlds of Harry Potter" while quizzing his nephew and nieces about the mythological references in the novels.
- [d1s3]  He later wrote the book while teaching a seminar on self-publishing to graduate students at the University of North Carolina.
- [d1s4]  The book was published in March 2001, without approval from Rowling, and has since received positive reviews from critics.
- [d1s5]  An updated version of "The Magical Worlds of Harry Potter" was published in 2004 by Berkley Books.

**d2: Warner Bros. Entertainment Inc. v. RDR Books**

- [d2s0] Warner Bros.
- [d2s1]  Entertainment, Inc. and J. K. Rowling v. RDR Books, 575 F.Supp.2d 513 (SDNY 2008) is a copyright lawsuit brought on 31 October 2007 by the media company Warner Bros. and "Harry Potter" author J. K. Rowling against RDR Books, an independent publishing company based in Muskegon, Michigan.
- [d2s2]  Lawyers for Rowling and Time Warner argued that RDR's attempt to publish for profit a print facsimile of "The Harry Potter Lexicon", a free online guide to the "Harry Potter" fictional universe, constituted an infringement of their copyright and was not protected by the affirmative defense of fair use.
- [d2s3]  The trial was held from 14–17 April 2008 in the United States District Court for the Southern District of New York.
- [d2s4]  In September 2008, the court ruled in Rowling's favor, and publication of the book was blocked.
- [d2s5]  In 2009, RDR Books released an edited volume, eliminating the problematic long quotes found to be infringing.

**d3: Harry Potter and the Deathly Hallows**

- [d3s0] Harry Potter and the Deathly Hallows is the seventh and final novel of the "Harry Potter" series, written by British author J. K. Rowling.
- [d3s1]  The book was released on 21 July 2007, ten years after publication of "Harry Potter and the Philosopher's Stone" (1997), by Bloomsbury Publishing in the United Kingdom, in the United States by Scholastic, and in Canada by Raincoast Books, ending the series that began in 1997 with the publication of "Harry Potter and the Philosopher's Stone".
- [d3s2]  The novel chronicles the events directly following "Harry Potter and the Half-Blood Prince" (2005), and the final confrontation between the wizards Harry Potter and Lord Voldemort, as well as revealing the previously concealed back story of several main characters.
- [d3s3]  The title of the book refers to three mythical objects featured in the story, collectively known as the "Deathly Hallows"—an unbeatable wand, a stone to bring the dead to life, and a cloak of invisibility.

**d4: Parodies of Harry Potter**

- [d4s0] The immense popularity and wide recognition of J. K. Rowling's Harry Potter fantasy series has led to its being extensively parodied, in works spanning nearly every medium.
- [d4s1]  The franchise holds the record for the most fan fiction parodies, at over 900.000 Some self-described parodies have been targeted by Rowling and her publishers as plagiarism, while others have sold hundreds of thousands of copies without any threat of legal sanction.
- [d4s2]  Misinterpretations of "Harry Potter" parodies have sparked at least two urban legends.
- [d4s3]  Many "Harry Potter" parodies are self-published; others are put out as part of major comic productions, such as "Mad", "The Simpsons", "South Park", "Saturday Night Live" and "Robot Chicken", all of which have parodied "Harry Potter" several times.
- [d4s4]  Rowling has also been parodied (and parodied herself) in a number of instances.

**d5: J. K. Rowling**

- [d5s0] Joanne Rowling, {'1': ", '2': ", '3': ", '4': "} ( ; born 31 July 1965), who writes under the pen names J. K. Rowling and Robert Galbraith, is a British novelist and screenwriter who wrote the "Harry Potter" fantasy series.
- [d5s1]  The books have won multiple awards, and sold more than 400 million copies.
- [d5s2]  They have become the best-selling book series in history and been the basis for a series of films, over which Rowling had overall approval on the scripts and was a producer on the final films in the series.

**d6: Harry Potter (film series)**

- [d6s0] Harry Potter is a British-American film series based on the "Harry Potter" novels by author J. K. Rowling.
- [d6s1]  The series is distributed by Warner Bros. and consists of eight fantasy films, beginning with "Harry Potter and the Philosopher's Stone" (2001) and culminating with "Harry Potter and the Deathly Hallows – Part 2" (2011).
- [d6s2]  A spin-off prequel series will consist of five films, starting with "Fantastic Beasts and Where to Find Them" (2016).
- [d6s3]  The "Fantastic Beasts" films mark the beginning of a shared media franchise known as J. K. Rowling's Wizarding World.

**d7: Fantastic Beasts and Where to Find Them**

- [d7s0] Fantastic Beasts and Where to Find Them is a 2001 book written by British author J. K. Rowling (under the pen name of the fictitious author Newt Scamander) about the magical creatures in the "Harry Potter" universe.
- [d7s1]  The original version purports to be Harry Potter's copy of the textbook of the same name mentioned in "Harry Potter and the Philosopher's Stone" (or "Harry Potter and the Sorcerer's Stone" in the US), the first novel of the "Harry Potter" series.
- [d7s2]  It includes several notes inside it supposedly handwritten by Harry, Ron Weasley, and Hermione Granger, detailing their own experiences with some of the beasts described, and including in-jokes relating to the original series.

**d8: Mary Gordon (writer)**

- [d8s0] Mary Catherine Gordon (born December 8, 1949) is an American writer and the McIntosh Professor of English at Barnard College.
- [d8s1]  She is best known for her novels, memoirs and literary criticism.

**d9: Religious debates over the Harry Potter series**

- [d9s0] Religious debates over the "Harry Potter" series of books by J. K. Rowling are based on claims that the novels contain occult or Satanic subtexts.
- [d9s1]  A number of Protestant, Catholic, and Orthodox Christians have argued against the series, as have some Shia and Sunni Muslims.
- [d9s2]  Supporters of the series have said that the magic in "Harry Potter" bears little resemblance to occultism, being more in the vein of fairy tales such as "Cinderella" and "Snow White", or to the works of C. S. Lewis and J. R. R. Tolkien, both of whom are known for writing fantasy novels with Christian subtexts.
- [d9s3]  Far from promoting a particular religion, some argue, the "Harry Potter" novels go out of their way to avoid discussing religion at all.
- [d9s4]  However, the author of the series, J. K. Rowling, describes herself as a practising Christian, and many have noted the Christian references which she includes in the final novel "Harry Potter and the Deathly Hallows".

**d10: A Very Potter Musical**

- [d10s0] A Very Potter Musical (originally titled Harry Potter: The Musical and often shortened to AVPM) is a musical with music and lyrics by Darren Criss and A. J. Holmes and a book by Matt Lang, Nick Lang and Brian Holden.
- [d10s1]  The story is a parody, based on several of the "Harry Potter" novels (particularly "Harry Potter and the Philosopher's Stone", "Harry Potter and the Goblet of Fire" and "Harry Potter and the Deathly Hallows") by J. K. Rowling, as well as their film counterparts.

## 23. hotpotqa_5ab9d4a9554299232ef4a21c

原位置：`dev` 第 50 题 · 全局第 293 题 · `sample_id: hotpotqa_5ab9d4a9554299232ef4a21c`

Question: The Pittsburgh Penguins 2003 first overall draft pick tied the franchise record for how many goalie wins?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | Pittsburgh Penguins 2003 first overall draft pick | False | [] | Marc-André Fleury | [["d1s1"]] | context |
| u2 | franchise record for goalie wins tied by {u1} | True | ["u1"] | 226 | [["d4s5"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | Pittsburgh Penguins' first overall pick in the 2003 NHL Entry Draft | False | [] | Marc-André Fleury | [['d1s1']] |
| u2 | number of goalie wins with which {u1} tied the Penguins franchise record | True | ['u1'] | 226 | [['d4s5']] |

### Source documents (reference only)

**d1: Marc-André Fleury**

- [d1s0] Marc-André Fleury (born November 28, 1984) is a French-Canadian professional ice hockey goaltender playing for the Vegas Golden Knights of the National Hockey League (NHL).
- [d1s1]  Drafted out of the Quebec Major Junior Hockey League (QMJHL) first overall by the Pittsburgh Penguins in the 2003 NHL Entry Draft, Fleury played major junior for four seasons with the Cape Breton Screaming Eagles, earning both the Mike Bossy Trophy as the league's top prospect and the Telus Cup as the top defensive player in 2003.
- [d1s2]  He joined the Penguins in 2003–04 and has won three Stanley Cup championships with the team in 2009, 2016, and 2017.
- [d1s3]  Internationally, Fleury has represented Canada twice as a junior, winning back-to-back silver medals at the World Junior Championships in 2003 and 2004.
- [d1s4]  He won a gold medal with Team Canada at the 2010 Winter Olympics in Vancouver.

**d2: Darcy Robinson**

- [d2s0] Darcy Robinson (May 3, 1981September 27, 2007) was an Italian/Canadian professional ice hockey defenseman who was a former Pittsburgh Penguins draft pick.
- [d2s1]  Robinson split five seasons between the AHL and ECHL, playing for both Pittsburgh Penguins' affiliates in Wilkes-Barre and Wheeling before joining HC Asiago in 2005.

**d3: Phil Kessel**

- [d3s0] Philip Joseph Kessel Jr. (born October 2, 1987) is an American professional ice hockey right winger currently playing for the Pittsburgh Penguins of the National Hockey League (NHL).
- [d3s1]  Kessel is a product of USA Hockey National Team Development Program and currently holds the program's career record for goals with 104.
- [d3s2]  He finished his amateur career playing collegiate hockey in the NCAA for the University of Minnesota in the Western Collegiate Hockey Association (WCHA) conference.
- [d3s3]  He was then selected fifth overall in the 2006 NHL Entry Draft by the Boston Bruins.
- [d3s4]  After his rookie season, 2006–07, he was awarded the Bill Masterton Memorial Trophy for overcoming testicular cancer while continuing his professional career.
- [d3s5]  In 2009, Kessel was traded from Boston to the Toronto Maple Leafs where he spent six seasons before being dealt to the Pittsburgh Penguins in 2015.
- [d3s6]  Kessel won his first and second Stanley Cup championships with the Pittsburgh Penguins in back to back seasons with wins over the San Jose Sharks and the Nashville Predators, respectively.
- [d3s7]  Kessel is known as a natural goal scorer and for his active iron man streak – he is one of four players in the NHL with an active streak (as of August 2017) of 600 or more consecutive games.

**d4: 2011–12 Pittsburgh Penguins season**

- [d4s0] The 2011–12 Pittsburgh Penguins season was the franchise’s 45th season in the National Hockey League (NHL).
- [d4s1]  The Penguins, led by head coach Dan Bylsma, would start the season without captain center Sidney Crosby.
- [d4s2]  The team still managed a 51–25–6 record, an East-best 29 home wins, and their 108 points second-best in the Eastern Conference.
- [d4s3]  In February, the team began the league's longest season winning streak and also saw the return of Crosby after missing more than 40 games with concussion like symptoms, before they saw the streak end in March at 11 games.
- [d4s4]  Center Evgeni Malkin was able to play in 75 games despite difficulties associated with recent knee surgery and recorded his greatest goal tally in a season (50) on the way to winning his second Art Ross Trophy.
- [d4s5]  Marc-Andre Fleury tied a franchise record for goalie wins (226) in a victory against the Atlantic division winning-New York Rangers.
- [d4s6]  The four-seed Penguins would see their playoff run end to the same team which halted their regular season winning streak, the Philadelphia Flyers, losing the first three games before perishing in Game 6 of the Eastern Conference Semifinals.

**d5: P. T. Ricci**

- [d5s0] Peter Thomas Ricci (born July 10, 1987), also found as "P. T." Ricci, is an American professional lacrosse player who plays for the Florida Launch of Major League Lacrosse.
- [d5s1]  Ricci played four years for Loyola College in Baltimore, Maryland and graduated from Conestoga High School in Berwyn, Pennsylvania in 2005, after starring in football and lacrosse and running track.
- [d5s2]  He finished his senior season at Loyola with a team leading 91 ground balls, and was the eleventh draft pick in the 2009 MLL Draft to the Chesapeake Bayhawks.
- [d5s3]  After two seasons with the Bayhawks he was traded to the Boston Cannons in May 2011.
- [d5s4]  He won consecutive championships in 2010 and 2011 with the Chesapeake Bayhawks and Boston Cannons respectively, attributing to the Cannons first Steinfield Trophy in MLL history.
- [d5s5]  He was also selected as an all-star in 2011 season.
- [d5s6]  He was traded by the Boston Cannons to the Florida Launch in November of 2013 along with Lee Coppersmith and the 12th overall draft prick in the 2014 draft for Brodie Merrill, Martin Cahill and the 37th overall draft pick in the 2014 draft.
- [d5s7]  He signed a 2 year deal with the Florida Launch in January 2017.

**d6: Matt Murray (ice hockey)**

- [d6s0] Matthew Murray (born May 25, 1994) is a Canadian professional ice hockey goaltender who plays with the Pittsburgh Penguins in the National Hockey League (NHL).
- [d6s1]  Murray was selected by the Penguins in the third round (83rd overall) of the 2012 NHL Entry Draft.
- [d6s2]  In 2016, Murray won his first Stanley Cup as the starting goalie for the Penguins during the playoffs.
- [d6s3]  In 2017, he won his second Stanley Cup, becoming the first goaltender in NHL history to win two Stanley Cups as a rookie, as well as setting the record for most playoff wins by a rookie goaltender with 22.

**d7: List of first overall MLS draft picks**

- [d7s0] The Major League Soccer SuperDraft's first overall pick is the player who is selected first among all eligible draftees by a team during the annual Major League Soccer (MLS) SuperDraft.
- [d7s1]  The first pick is awarded to the club with the poorest regular season record during the previous MLS campaign.
- [d7s2]  Exceptions are when there is an expansion franchise, where they expansion side has the opportunity to select the first overall draft pick.

**d8: Pittsburgh Penguins**

- [d8s0] The Pittsburgh Penguins are a professional ice hockey team based in Pittsburgh, Pennsylvania.
- [d8s1]  They are members of the Metropolitan Division of the Eastern Conference of the National Hockey League (NHL).
- [d8s2]  The franchise was founded in 1967 as one of the first expansion teams during the league's original expansion from six to twelve teams.
- [d8s3]  The Penguins played in the Civic Arena, also known to Pittsburgh fans as "The Igloo", from the time of their inception through the end of the 2009–10 season.
- [d8s4]  They moved into their new arena, PPG Paints Arena, to begin the 2010–11 season.
- [d8s5]  They have qualified for six Stanley Cup Finals, winning the Stanley Cup five times – in 1991, 1992, 2009, 2016, and 2017.
- [d8s6]  Along with the Edmonton Oilers, the Penguins are tied for the most Cup championships among non-Original Six teams.
- [d8s7]  With their Stanley Cup wins in 2016 and 2017, the Penguins became the first back-to-back champions in 19 years (since the 1997–98 Detroit Red Wings) and the first team to do so since the introduction of the salary cap.

**d9: 1991–92 Quebec Nordiques season**

- [d9s0] Quebec once again had the first overall draft pick heading into the 1991 NHL Entry Draft, as this marked the third consecutive season the Nordiques had the first overall selection.
- [d9s1]  With the pick, Quebec selected Eric Lindros of the Oshawa Generals.
- [d9s2]  Lindros scored 71 goals and 149 points with the Generals during the 1990–91 season, however, he let the Nordiques know that he was not interested in playing for Quebec.
- [d9s3]  Despite this, the Nordiques drafted him, however, the club was unable to sign Lindros.
- [d9s4]  Rather than playing for Quebec for the 1991–92 season, Lindros played for the Canadian national men's hockey team, and then returned to the Generals for the rest of the season.

**d10: List of first overall NBL Canada draft picks**

- [d10s0] The National Basketball League of Canada's first overall pick is the player who is selected first among all eligible draftees by a team during the annual National Basketball League of Canada (NBL Canada) Draft.
- [d10s1]  The first pick is, on most occasions, awarded to the team that finished with the worst record in the previous season.
- [d10s2]  Teams may be allowed to select earlier in the case that they make a trade during or prior to the event.
- [d10s3]  Only one first overall draft pick, Alex Johnson, previously played at an NCAA Division I school.
- [d10s4]  Johnson attended North Carolina State University.

## 24. hotpotqa_5abe97dc5542994516f453cf

原位置：`dev` 第 51 题 · 全局第 294 题 · `sample_id: hotpotqa_5abe97dc5542994516f453cf`

Question: What South East London-based post-punk/art rock group took their name from a American radical feminist that is best known for attempting to murder artist Andy Warhol?

Note: 【保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。 待题干称乐队得名于女权主义者，context 明确是她的 SCUM Manifesto。已给出人物→其宣言命名的乐队的两步修正，不需要改动原问题，需要这样的问题表述。

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 按 Note 保留原问题措辞，采用人物→以其宣言命名的乐队两步解释；最终 S.C.U.M 由 d4s0/d4s3 支持，不把它说成以 Valerie Solanas 本人姓名命名。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | American radical feminist best known for attempting to murder artist Andy Warhol | False | [] | Valerie Solanas | [["d8s0"]] | context |
| u2 | South East London-based post-punk/art rock group named after the manifesto written by {u1} | True | ["u1"] | S.C.U.M | [["d4s0", "d4s3"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | American radical feminist best known for attempting to murder artist Andy Warhol | False | [] | Valerie Solanas | [['d8s0']] |
| u2 | South East London-based post-punk/art rock group that took its name from {u1} | True | ['u1'] | S.C.U.M | [['d4s0', 'd4s3']] |

### Source documents (reference only)

**d1: Green Coca-Cola Bottles**

- [d1s0] Green Coca-Cola Bottles is a 1962 painting by Andy Warhol that depicts numerous Coca-Cola bottles.
- [d1s1]  Andy Warhol’s painting “Green Coca-Cola Bottles” attempted to take a mainstream item and converted it into a piece of art.
- [d1s2]  Warhol’s piece was a hybrid craft that is to say that he utilized a silkscreen technique, which mechanicalized some aspects of the painting, but also kept it so that he had to put in some of his individualized “unevenness” across the painting, to reel in the human aspect.
- [d1s3]  The painting engenders an optimistic message for the American public, which is best described in Warhol’s own words, “What’s grand about this country is that America started the tradition where the richest consumers buy essentially the same thing as the poorest... you can know that the President drinks Coke, Liz Taylor drinks Coke, and, just think, you can drink Coke, too.
- [d1s4]  A Coke is a Coke, and no amount of money can get you a better Coke.”
- [d1s5]  Here Warhol goes to show that the democratic equality, which allowed the birth of a uniformly governed consumerist mindset, has given them an equal satiating medium.
- [d1s6]  With respect to its artistic merits, Warhol’s painting utilizes repetitive imagery in the shape of hundred and twelve almost identical bottles, evoking a sense of mechanicalization which overlaps his former usage of mass culture objects.
- [d1s7]  The widespread display of advertisement flooded the American public during the sixties, and Warhol had been successful in mapping it onto his canvas, no wonder it is considered one of Warhol’s masterpieces.

**d2: Interview (magazine)**

- [d2s0] Interview is an American magazine founded in late 1969 by artist Andy Warhol and British journalist John Wilcock.
- [d2s1]  The magazine, nicknamed "The Crystal Ball of Pop," features intimate conversations between some of the world's biggest celebrities, artists, musicians, and creative thinkers.
- [d2s2]  Interviews are usually unedited or edited in the eccentric fashion of Warhol's books and "The Philosophy of Andy Warhol: From A to B and Back Again".

**d3: Anne Koedt**

- [d3s0] Anne Koedt (born 1941 in Denmark) is an American radical feminist and New York-based author of "The Myth of the Vaginal Orgasm", a classic feminist work on women's sexuality.
- [d3s1]  She was connected to the group New York Radical Women and was a founding member of New York Radical Feminists.

**d4: S.C.U.M (band)**

- [d4s0] S.C.U.M were a South East London-based post-punk/art rock group.
- [d4s1]  Its members were Thomas Cohen (vocals), Bradley Baker (machines, press), Samuel Kilcoyne (keyboards), Huw Webb (bass), and Melissa Rigby (drums).
- [d4s2]  The band previously included Ruaridh Connellan (drums) and Joseph Williams (bass, media).
- [d4s3]  S.C.U.M took their name from Valerie Solanas' manifesto, SCUM Manifesto, an ironic reference to the all-male band before Connellan's dismissal and replacement by Rigby.

**d5: Andy Warhol (song)**

- [d5s0] "Andy Warhol" is a song written by David Bowie in 1971 for the album "Hunky Dory".
- [d5s1]  It is an acoustic song about one of Bowie's early artist inspirations, the American pop artist Andy Warhol.

**d6: John Warhola**

- [d6s0] John Warhola (May 31, 1925 – December 24, 2010) played a pivotal role in maintaining the legacy of his younger brother, pop artist Andy Warhol, assigned responsibility by their father on his deathbed to ensure that Andy attended college and serving as a trustee of the Andy Warhol Foundation for the Visual Arts after his brother's death in 1987.
- [d6s1]  Warhola oversaw the establishment of The Andy Warhol Museum in Pittsburgh and the Andy Warhol Museum of Modern Art in Medzilaborce, Slovakia.

**d7: I Shot Andy Warhol**

- [d7s0] I Shot Andy Warhol is a 1996 American-British independent film about the life of Valerie Solanas and her relationship with the artist Andy Warhol.
- [d7s1]  The film marked the debut of Canadian director Mary Harron.
- [d7s2]  The film stars Lili Taylor as Valerie, Jared Harris as Andy Warhol, and Martha Plimpton as Valerie's friend Stevie.
- [d7s3]  Stephen Dorff plays Warhol superstar Candy Darling.
- [d7s4]  John Cale of The Velvet Underground wrote the film's score despite protests from former band member Lou Reed.
- [d7s5]  Yo La Tengo plays an anonymous band that is somewhat reminiscent of the group.

**d8: Valerie Solanas**

- [d8s0] Valerie Jean Solanas (April 9, 1936 – April 25, 1988) was an American radical feminist and author best known for writing the "SCUM Manifesto" and attempting to murder artist Andy Warhol in the late 1960s.

**d9: Andrea Dworkin**

- [d9s0] Andrea Rita Dworkin (September 26, 1946 – April 9, 2005) was an American radical feminist and writer best known for her criticism of pornography, which she argued was linked to rape and other forms of violence against women.
- [d9s1]  Her views were widely criticized by liberal feminists and others.
- [d9s2]  At the same time, she maintained a dialogue with political conservatives, and wrote a topically-related book, "Right-Wing Women".
- [d9s3]  After suffering abuse from her first husband, she was introduced to radical feminist literature, and began writing "Woman Hating".
- [d9s4]  Coming to New York, she became an activist on several issues and a writer, eventually publishing 10 books on feminism.

**d10: Andy Warhol Museum of Modern Art**

- [d10s0] The Andy Warhol Museum of Modern Art (Slovak: Múzeum Andyho Warhola Medzilaborce or Múzeum Moderného Umenia Andyho Warhola ) in Medzilaborce, Slovakia, was established in 1991 by the American family of the artist Andy Warhol and the Slovak Ministry of Culture.
- [d10s1]  Until 1996, AWMMA (the English-language acronym of the museum) was called The Warhol Family Museum of Modern Art.

## 25. hotpotqa_5ac149705542994d76dccdd0

原位置：`dev` 第 52 题 · 全局第 295 题 · `sample_id: hotpotqa_5ac149705542994d76dccdd0`

Question: Did Glamour or W come first?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: comparison · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | year Glamour was founded | False | [] | 1939 | [["d6s1"]] | context |
| u2 | year W was founded | False | [] | 1971 | [["d5s1"]] | context |
| u3 | which came first | True | ["u1", "u2"] | Glamour | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | year Glamour magazine was founded | False | [] | 1939 | [['d6s1']] |
| u2 | year W magazine was founded | False | [] | 1971 | [['d5s1']] |
| u3 | which of Glamour and W came first | True | ['u1', 'u2'] | Glamour | [[]] |

### Source documents (reference only)

**d1: Remembrance Project**

- [d1s0] The Remembrance Project is an anti-illegal immigration non-profit organization in the United States based in Houston, Texas.
- [d1s1]  In particular, it keeps a list of United States citizens killed by illegal aliens on U.S. soil.
- [d1s2]  It was praised by President Donald Trump.
- [d1s3]  The Remembrance Project was started to educate and raise awareness of the epidemic of killings of Americans by individuals who should not have been in the country in the first place.
- [d1s4]  Americans must come first in order to stop the permanent separation of families.

**d2: Federal Power Act**

- [d2s0] The Federal Power Act is a law appearing in Chapter 12 of Title 16 of the United States Code, entitled "Federal Regulation and Development of Power".
- [d2s1]  Enacted as the Federal Water Power Act on June 10, 1920, and amended many times since, its original purpose was to more effectively coordinate the development of hydroelectric projects in the United States.
- [d2s2]  Representative John J. Esch (R-Wisconsin) was the sponsor.
- [d2s3]  Prior to this time and despite federal control of navigable waters and the necessary congressional approval to construct such facilities, Congress had left the regulation of hydroelectric power to the individual states.
- [d2s4]  The first federal legislation broadly dealing with hydroelectric development regarded its competition with navigation usage; with the passage of the Rivers and Harbors Act of 1899 Congress made it illegal to dam navigable streams without a license (or permit) from them.
- [d2s5]  Until 1903, these congressional permits were given away on a 'first come first served' perpetual basis and controlled by the individual states.
- [d2s6]  This would lead to a long debate between competing private and public development interests, and culminate in the act's passage in 1920.

**d3: Swing (Australian politics)**

- [d3s0] The term swing refers to the extent of change in voter support, typically from one election or opinion poll to another, expressed as a positive or negative percentage point.
- [d3s1]  For the Australian House of Representatives and the lower houses of the parliaments of all the states and territories except Tasmania and the ACT, Australia employs preferential voting in single-member constituencies.
- [d3s2]  Under the full-preference instant-runoff voting system, in each seat the candidate with the lowest vote is eliminated and their preferences are distributed, which is repeated until only two candidates remain.
- [d3s3]  While every seat has a two-candidate preferred (TCP) result, seats where the major parties have come first and second are commonly referred to as having a two-party-preferred (TPP) result.
- [d3s4]  The concept of "swing" in Australian elections is not simply a function of the difference between the votes of the two leading candidates, as it is in Britain.
- [d3s5]  To know the majority of any seat, and therefore the swing necessary for it to change hands, it is necessary to know the preferences of all the voters, regardless of their first preference votes.
- [d3s6]  It is not uncommon in Australia for candidates who have comfortable leads on the first count to fail to win the seat, because "preference flows" go against them.

**d4: When Things of the Spirit Come First**

- [d4s0] When Things of the Spirit Come First is Simone de Beauvoir's 'first' work of fiction.
- [d4s1]  After a number of false starts, in 1937 she submitted this collection of interlinked stories to a publisher.
- [d4s2]  But it was turned down by both Gallimard and Grasset.
- [d4s3]  It consists of five short stories which are weaved together in such a way that it to structurally similar to a more traditional novel.
- [d4s4]  The first, "Maurcelle", tells the story of the oldest of three siblings.
- [d4s5]  She marries an abusive artist.
- [d4s6]  The second, "Chantal", tells the story of a lycee philosophy teacher (like de Beauvoir).
- [d4s7]  She idealizes her life and becomes involved in the lives of her students but ultimately refuses to help them.
- [d4s8]  "Lisa" is the third and shortest story, about a girl who struggles to live a spiritual life while existing in a physical body.
- [d4s9]  "Anne", the fourth story, is the result of many of de Beauvoir's earlier attempts at writing.
- [d4s10]  It parallels the story of her friend Elisabeth Mabille (Zaza) who died soon after her mother refused to allow her to marry Maurice Merleau-Ponty.
- [d4s11]  The final story, "Marguarite" expresses the existential views that de Beauvoir herself believed that life itself should be experienced, rather than spirituality.

**d5: W (magazine)**

- [d5s0] W is a monthly American fashion magazine published by Condé Nast, who purchased original owner Fairchild Publications in 1999.
- [d5s1]  It was created in 1971 by the publisher of sister magazine "Women's Wear Daily", James Brady.
- [d5s2]  The magazine is an oversize format – ten inches wide and thirteen inches tall.
- [d5s3]  Stefano Tonchi is the editor of "W"; Lucy Kriz is the vice president and publisher.
- [d5s4]  "W" magazine has a reader base of nearly half a million, 469,000 of which are annual subscribers.
- [d5s5]  80 % of the magazine's readers are female and have an average household income of $135,840.

**d6: Glamour (magazine)**

- [d6s0] Glamour is a women's magazine published by Condé Nast Publications.
- [d6s1]  Founded in 1939 and first published in April 1939 in the United States, it was originally called "Glamour of Hollywood".

**d7: Martin Ralph**

- [d7s0] Martin Ralph (born 18 January 1960) is an Australian sprint canoeist who competed in the mid-1980s.
- [d7s1]  At the 1984 Summer Olympics in Los Angeles, he was eliminated in the repechages of the K-2 500 m event.
- [d7s2]  Subsequently, he began to coach with the VIS(Victorian Institute of Sport) and independently.
- [d7s3]  Martin received the Australian Sports Medal from the Prime Minister and the Governor General for sporting achievement in the year 2000.
- [d7s4]  Often asked if he won a gold medal Martin replies, "I didn't come first and I didn't come last but I got a real good look at the bloke who did!"

**d8: California Fuel Cell Partnership**

- [d8s0] The California Fuel Cell Partnership is a public-private partnership to promote hydrogen vehicles (including cars and buses) in California.
- [d8s1]  It is notable as one of the first initiatives for that purpose undertaken in the United States.
- [d8s2]  The challenge is which come first, hydrogen cars or filling stations.

**d9: I Will Cure You**

- [d9s0] I Will Cure You is the only album by the comedian Vic Reeves.
- [d9s1]  It was released in 1991 by Island Records, produced by Steve Beresford, Andy Metcalfe and Philip Oakey and re-released in 1999 by Universal Music's Spectrum label.
- [d9s2]  The album peaked at #16 in the UK Albums Chart and featured the Number One single "Dizzy" which was a collaboration with The Wonder Stuff.
- [d9s3]  It included a mixture of covers and original songs in a variety of musical styles, many of which were originally introduced in Reeves’ debut Channel 4 comedy show "Vic Reeves Big Night Out".
- [d9s4]  Reeves’ comedy partner Bob Mortimer sings alongside Reeves on "Summer of ‘75", with Jonathan Ross providing whistling on "I Remember Punk Rock".
- [d9s5]  Reeves has said that he did not want to make a novelty or comedy album but something more serious, and that for him being a singer is secondary as his comedy will always come first.

**d10: St Philip Howard Catholic Voluntary Academy**

- [d10s0] St Philip Howard Catholic Voluntary Academy (formerly St Philip Howard Catholic School) is a Roman Catholic secondary school located in Glossop in northern Derbyshire.
- [d10s1]  It traditionally provides secondary education for Catholic school children in the Glossopdale and Longdendale valleys.
- [d10s2]  However, the school attracts applications from a wide variety of backgrounds and primary schools in Glossop.
- [d10s3]  The school has been established 52 years (as of 2013).
- [d10s4]  The current headteacher is Wendy Steciuk, who has held the post since September 2003.
- [d10s5]  The school attends a religious service at the nearby St Mary's Catholic Church at least once a term.
- [d10s6]  The school welcomes applications from all students, but makes clear that Catholic children come first in the selection process.
- [d10s7]  Traditionally, students come from Catholic primary schools around Glossop, Gamesley, Hadfield and Old Glossop.
- [d10s8]  However, students sometimes join the school from other non-religious schools in Glossop, Tintwistle and the Longdendale and Tameside areas.

## 26. hotpotqa_5adbf5d8554299438c868cec

原位置：`dev` 第 53 题 · 全局第 296 题 · `sample_id: hotpotqa_5adbf5d8554299438c868cec`

Question: Zota was a foe of the superhero appearing in comic books by which company?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | superhero that Zota was a foe of | False | [] | Doctor Strange | [["d4s1"]] | context |
| u2 | company that published comic books featuring {u1} | True | ["u1"] | Marvel Comics | [["d1s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | superhero of whom Zota was a foe | False | [] | Doctor Strange | [['d4s1']] |
| u2 | company publishing the comic books in which {u1} appears | True | ['u1'] | Marvel Comics | [['d1s0']] |

### Source documents (reference only)

**d1: Doctor Strange**

- [d1s0] Doctor Stephen Vincent Strange, M.D., is a fictional superhero appearing in American comic books published by Marvel Comics.
- [d1s1]  Created by artist Steve Ditko and writer Stan Lee, the character first appeared in "Strange Tales" #110 (cover-dated July 1963).
- [d1s2]  Doctor Strange serves as the Sorcerer Supreme, the primary protector of Earth against magical and mystical threats.
- [d1s3]  Inspired by stories of black magic and "Chandu the Magician", Strange was created during the Silver Age of Comic Books to bring a different kind of character and themes of mysticism to Marvel Comics.

**d2: Diamond (comics)**

- [d2s0] Diamond (Kent Chang) is a fictional character, a superhero appearing in American comic books published by Marvel Comics.
- [d2s1]  The character appears in the NEW-GEN comic books.
- [d2s2]  Created by Chris Matonti, J.D. Matonti, and Julia Coppola, he first appeared in NEW-GEN #1 (2010).
- [d2s3]  He was one of the children from the world of NEW-GEN granted extraordinary abilities by Deadalus' nanobot plague.
- [d2s4]  He is a founding member of the A.P.N.G.

**d3: Challenger (comics)**

- [d3s0] The Challenger is a fictional superhero appearing in American comic books published by Marvel Comics.
- [d3s1]  The character appeared beginning with the company's 1940s iteration as Timely Comics during the period fans and historians call the Golden Age of Comic Books.

**d4: Zota**

- [d4s0] Zota of Pergamum, usually referred to as Zota, is a fictional character, a super villain who appears in comics published by Marvel Comics.
- [d4s1]  The character, predominantly a foe of Doctor Strange, was created by writer-plotter Stan Lee and artist Steve Ditko.
- [d4s2]  He made his first appearance in "Strange Tales" #124 (September 1964).

**d5: Barbara Gordon**

- [d5s0] Barbara Gordon is a fictional superhero appearing in American comic books published by DC Comics, commonly in association with the superhero Batman.
- [d5s1]  The character was created by William Dozier, Julius Schwartz, and Carmine Infantino.
- [d5s2]  At the request of the producers of the 1960s "Batman" television series, DC editor Schwartz called for a new female counterpart to the superhero Batman that could be introduced into publication and the third season of the show simultaneously.
- [d5s3]  The character subsequently made her first comic book appearance as Batgirl in "Detective Comics" #359, titled "The Million Dollar Debut of Batgirl!"
- [d5s4]  (January 1967), by writer Gardner Fox and artist Carmine Infantino.

**d6: Feron**

- [d6s0] Feron is a fictional superhero appearing in American comic books published by Marvel Comics.
- [d6s1]  The character usually appears in comic books featuring the British superhero team Excalibur, of which he is a former member.
- [d6s2]  Created by writer/artist Alan Davis, he first appeared in "Excalibur" vol.
- [d6s3]  1 #48 (March 1992).

**d7: Roy Harper (comics)**

- [d7s0] Roy Harper is a fictional superhero appearing in American comic books published by DC Comics.
- [d7s1]  Roy is one of DC's most longstanding characters, originating in 1940s comics as Speedy, the teen sidekick of the superhero Green Arrow.
- [d7s2]  Like his mentor Green Arrow, Roy is a world-class archer and athlete who uses his exceptional marksmanship to fight crime.
- [d7s3]  Along with other prominent DC Comics superhero sidekicks, he goes on to become a core member of the superhero group the Teen Titans.
- [d7s4]  As an adult, Roy casts off his Speedy identity to establish himself as the superhero Arsenal, and for a time adopts the name Red Arrow to symbolise his having become an equal of Green Arrow.
- [d7s5]  As well as continuing to serve as one of the Titans at various times, Roy has had leading roles in the superhero groups the Seven Soldiers of Victory, the Outsiders, the Justice League, and the Outlaws.

**d8: Gazelle (New-Gen)**

- [d8s0] Gazelle (Elle) is a fictional character, a superhero appearing in American comic books published by Marvel Comics.
- [d8s1]  The character appears in the NEW-GEN comic books.
- [d8s2]  Created by Chris Matonti, J.D. Matonti, and Julia Coppola, she first appeared in NEW-GEN #1 (2010).
- [d8s3]  He was one of the children from the world of NEW-GEN granted extraordinary abilities by Deadalus' nanobot infestation.
- [d8s4]  She is a founding member of the A.P.N.G. superhero team.

**d9: Alan Scott**

- [d9s0] Alan Ladd Wellington Scott is a fictional superhero appearing in American comic books published by DC Comics, and the first superhero to bear the name Green Lantern.
- [d9s1]  He was created by Bill Finger and Martin Nodell first appearing in the comic book "All-American Comics #16", published in 1940.

**d10: Spider-Man**

- [d10s0] Spider-Man is a fictional superhero appearing in American comic books published by Marvel Comics.
- [d10s1]  The character was created by writer-editor Stan Lee and writer-artist Steve Ditko, and first appeared in the anthology comic book "Amazing Fantasy" #15 (August 1962) in the Silver Age of Comic Books.
- [d10s2]  Lee and Ditko conceived the character as an orphan being raised by his Aunt May and Uncle Ben in New York City after his parents Richard and Mary Parker were killed in a plane crash, and as a teenager, having to deal with the normal struggles of adolescence in addition to those of a costumed crime-fighter.
- [d10s3]  Spider-Man's creators gave him super strength and agility, the ability to cling to most surfaces, shoot spider-webs using wrist-mounted devices of his own invention, which he calls "web-shooters", and react to danger quickly with his "spider-sense", enabling him to combat his foes.

## 27. hotpotqa_5ade960d554299728e26c747

原位置：`dev` 第 54 题 · 全局第 297 题 · `sample_id: hotpotqa_5ade960d554299728e26c747`

Question: What is the nationality of the top scorer of the 2012–13 Primeira Liga?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | top scorer of the 2012–13 Primeira Liga | False | [] | Jackson Martínez | [["d5s4"]] | context |
| u2 | nationality of {u1} | True | ["u1"] | Colombian | [["d2s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | top scorer of the 2012–13 Primeira Liga | False | [] | Jackson Martínez | [['d5s4']] |
| u2 | nationality of {u1} | True | ['u1'] | Colombian | [['d2s0']] |

### Source documents (reference only)

**d1: 2013–14 Primeira Liga**

- [d1s0] The 2013–14 Primeira Liga (also known as Liga ZON Sagres for sponsorship reasons) was the 80th season of the Primeira Liga, the top professional league for Portuguese association football clubs.
- [d1s1]  It began on 18 August 2013 and concluded on 11 May 2014.
- [d1s2]  Sixteen teams contested the league, fourteen of which took part in the previous season and two of which were promoted from the Segunda Liga.
- [d1s3]  On 20 April 2014, Benfica won the Primeira Liga for a record 33rd time with a 2–0 victory over Olhanense, with two games to spare.

**d2: Jackson Martínez**

- [d2s0] Jackson Arley Martínez Valencia (] ; born 3 October 1986) is a Colombian professional footballer who plays as a striker for Chinese club Guangzhou Evergrande Taobao and the Colombian national team.

**d3: 2012–13 Taça da Liga (Third Round)**

- [d3s0] The 2012–13 Taça da Liga third round matches were played between December 2012 and January 2013.
- [d3s1]  The eight winners of the second round matches progressed to this round and were joined by the teams that finished in the top half of the 2012–13 Primeira Liga.
- [d3s2]  The 16 teams were seeded according to their league position in the previous season and drawn into four groups, where they played each other in a round-robin format.
- [d3s3]  The matchdays took place on 18–19 December, 29–30 December 2012 and 2 January 2013, and 9 January 2013.
- [d3s4]  The winners of each group progressed to the semi-finals to be played on 27 February 2013.

**d4: 2011–12 Primeira Liga**

- [d4s0] The 2011–12 Primeira Liga (also known as Liga ZON Sagres for sponsorship reasons) was the 78th season of the Primeira Liga, the top professional league for Portuguese association football clubs.
- [d4s1]  It began on 14 August 2011 and ended on 13 May 2012.
- [d4s2]  A total of 16 teams contested the league, 14 of which already took part in the previous season and two of which were promoted from the Liga de Honra.
- [d4s3]  Porto were the defending champions and secured their 26th and second consecutive league title.
- [d4s4]  Óscar Cardozo and Lima, respectively Benfica's and Braga's strikers, were the joint top scorers with 20 goals.

**d5: 2012–13 Primeira Liga**

- [d5s0] The 2012–13 Primeira Liga (also known as Liga ZON Sagres for sponsorship reasons) was the 79th season of the Primeira Liga, the top professional league for Portuguese association football clubs.
- [d5s1]  It began on 19 August 2012 and concluded on 19 May 2013.
- [d5s2]  Sixteen teams contested the league, fourteen of which took part in the previous season and two of which were promoted from the Liga de Honra.
- [d5s3]  Porto were the defending champions and secured their third consecutive and 27th overall title, after completing their second unbeaten season in three years.
- [d5s4]  Porto striker Jackson Martínez was the top scorer with 26 goals.

**d6: 2010–11 Primeira Liga**

- [d6s0] The 2010–11 Primeira Liga (also known as Liga ZON Sagres for sponsorship reasons) was the 77th season of the Primeira Liga, the top professional league for Portuguese association football clubs.
- [d6s1]  It began on 15 August 2010 and ended on 14 May 2011.
- [d6s2]  A total of 16 teams contested the league, 14 of which already took part in the previous season and two of which were promoted from the Liga de Honra.
- [d6s3]  Benfica were the defending champions but finished runners-up to Porto, who won their 25th league title in the club's first-ever unbeaten season.
- [d6s4]  Porto's forward Hulk was the top scorer with 23 goals.

**d7: 1999–2000 Primeira Liga**

- [d7s0] The 1999–2000 Primeira Liga was the 66th season of top-tier football in Portugal.
- [d7s1]  The competition was renamed Campeonato Nacional da Primeira Liga (National Championship of the First League), Primeira Liga for short, after the Portuguese League for Professional Football took control of the two top nationwide leagues in 1999.
- [d7s2]  It started on 20 August 1999 and ended on 14 May 2000.
- [d7s3]  The league was contested by 18 clubs with Porto as the defending champions.

**d8: 2012–13 Taça da Liga**

- [d8s0] The 2012–13 Taça da Liga was the sixth edition of the Taça da Liga, the Portuguese football league cup competition.
- [d8s1]  It was organized by the Portuguese League for Professional Football (LPFP) and contested between the 32 clubs competing in the 2012–13 Primeira Liga and 2012–13 Segunda Liga, the top two tiers of Portuguese football.
- [d8s2]  The first matches were played on 28 July 2012, and the final was played on Estádio Cidade de Coimbra in Coimbra, on 13 April 2013.

**d9: 2012–13 Segunda Liga**

- [d9s0] The 2012–13 Segunda Liga was the 23rd season of the second-tier of football in Portugal.
- [d9s1]  This season marked a series of changes in the league overall.
- [d9s2]  The league's name was changed back to Segunda Liga from the previous Liga de Honra.
- [d9s3]  A total of 22 teams contested the league, up from 16 in the previous season; 14 of which contested the 2011–12 season, two of which were promoted from the Portuguese Second Division (including a reserve team), one of which was relegated from the 2011–12 Primeira Liga, and five of which were new reserve teams of Primeira Liga clubs.
- [d9s4]  The reserve teams were not eligible for promotion to the Primeira Liga.

**d10: LPFP Primeira Liga Player of the Year**

- [d10s0] The Portuguese League for Professional Football Primeira Liga Player of the Year (often called the LPFP Primeira Liga Player of the Year, the Primeira Liga Player of the Year or simply the Player of the Year) is an annual award given to the player who is adjudged to have been the best of the year in Primeira Liga.
- [d10s1]  Between 2006 and 2010 the winner was chosen only by a vote amongst the members of Sports National Press Club (CNID).
- [d10s2]  Since 2011, thanks to new sponsorship agreements, all the awards related to football belong to Portuguese League for Professional Football (LPFP) and are chosen by a vote amongst their associated.

## 28. hotpotqa_5ae1e7275542997f29b3c18b

原位置：`dev` 第 55 题 · 全局第 298 题 · `sample_id: hotpotqa_5ae1e7275542997f29b3c18b`

Question: Paul Eiding has the role of the Vault Tec Rep from the video game developed by which company?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | video game featuring Paul Eiding as the Vault Tec Rep | False | [] | Fallout 4 | [["d6s1"]] | context |
| u2 | developer of {u1} | True | ["u1"] | Bethesda Game Studios | [["d10s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | video game in which Paul Eiding has the role of the Vault Tec Rep | False | [] | Fallout 4 | [['d6s1']] |
| u2 | company that developed {u1} | True | ['u1'] | Bethesda Game Studios | [['d10s0']] |

### Source documents (reference only)

**d1: Astro Warrior**

- [d1s0] Astro Warrior (アストロウォリアー , Asutoro Uoriā ) is a shoot 'em up video game developed and manufactured by Sega for the Master System in 1986.
- [d1s1]  Set in space, the player flies a spaceship shooting enemies and collecting power-ups to reach the mother ship of an invasion force.
- [d1s2]  Reception was mixed, with critics criticising the generic nature and lack of variety, and others praising the graphics.
- [d1s3]  The game was re-released on the "Hang-On / Astro" Warrior compilation in North America, and the "Astro Warrior / Pit Pot" compilation in Europe.
- [d1s4]  In 1996, Tec Toy re-released the game in Brazil as "Sapo Xulé: SOS Lagoa Poluída", and based it on a Brazilian 1980s toy.
- [d1s5]  This version was also released in Portugal.

**d2: Resident Evil 3: Nemesis**

- [d2s0] Resident Evil 3: Nemesis is a survival horror video game developed by Capcom and originally released for the PlayStation video game console in 1999.
- [d2s1]  It is the third installment in the "Resident Evil" video game series and takes place before and after the events of "Resident Evil 2".
- [d2s2]  The story of the game follows "Resident Evil" protagonist Jill Valentine and her efforts to escape from a city that has been infected with a new type of biological weapon secretly developed by the pharmaceutical company Umbrella.

**d3: Wonder Boy III: The Dragon's Trap**

- [d3s0] Wonder Boy III: The Dragon's Trap is a platforming and action-adventure video game developed by Westone as part of Sega's "Wonder Boy" series.
- [d3s1]  It was published by Sega and released for the Sega Master System in 1989 and for the Game Gear in 1992 as Wonder Boy: The Dragon's Trap.
- [d3s2]  It was ported by Hudson Soft in 1991(1990 in North America) and was released for the TurboGrafx-16/PC Engine under the name Dragon's Curse .
- [d3s3]  It was also ported in 1993 by Brazilian company Tec Toy under the title Turma da Mônica em o Resgate, with the game retooled to include characters from Brazilian comic book series "Monica's Gang" ("Turma da Mônica").
- [d3s4]  A remake developed by Lizardcube and published by DotEmu, titled "", was released in April 2017.

**d4: Fallout (video game)**

- [d4s0] Fallout: A Post Nuclear Role Playing Game is an open world role-playing video game developed and published by Interplay Productions in 1997.
- [d4s1]  The game has a post-apocalyptic and retro-futuristic setting, in the aftermath of a global nuclear war in an alternate history timeline mid-22nd century.
- [d4s2]  The protagonist of "Fallout" is an inhabitant of a Vault, long-term shelters, who is tasked to find the Water Chip to save other dwellers from water shortage.

**d5: Nightmare Circus**

- [d5s0] Nightmare Circus is a platform video game developed by Funcom and published by Tec Toy for the Sega Genesis video game console.
- [d5s1]  The game was released in Brazil in 1996, and eventually in North America via the Sega Channel in December 1996.

**d6: Paul Eiding**

- [d6s0] Paul Eiding (born March 28, 1957) is an American voice actor, voice instructor, and actor, perhaps best known as the voice actor behind Perceptor in the original Transformers cartoon, Colonel Roy Campbell in the "Metal Gear" series, the narrator in "Diablo", Judicator Aldaris in "StarCraft", and Max Tennyson in "Ben 10", "", "", and "Ben 10 Omniverse" where he also did the vocal effects for Zed, Liam and voices for several other characters.
- [d6s1]  He is also the Vault Tec Rep from "Fallout 4".

**d7: Game Dev Story**

- [d7s0] Game Dev Story is a simulation video game developed and published by Kairosoft for Microsoft Windows, iOS, and Android.
- [d7s1]  It was released for Windows in April of 1997 , for iOS and Android on October 9, 2010, and for Windows Phone on July 6, 2015.
- [d7s2]  The game follows a player-controlled video game company and its attempts to expand into a sales powerhouse over time.
- [d7s3]  As a simulation, the game and the direction of the company is controlled by the player, following a parallel timeline of the video game industry and its history.
- [d7s4]  The game was released to positive reviews, with many reviewers focusing on "Game Dev Story"' s addictive aspects and its witty references to video game pop culture.

**d8: Paperboy (video game)**

- [d8s0] Paperboy is a 1985 arcade game developed and published by Atari Games.
- [d8s1]  The player takes the role of a paperboy who delivers a fictional newspaper called "The Daily Sun" along a suburban street on his bicycle.
- [d8s2]  The game was ported to a wide range of video game consoles and personal computers.
- [d8s3]  The Nintendo Entertainment System version is the first NES game developed in the United States, and the Sega Master System version represented the first SMS game developed in the United Kingdom.
- [d8s4]  "Paperboy" is notable for its unusual theme, which extends to using bike handlebars as the controller.

**d9: Fallout Shelter**

- [d9s0] Fallout Shelter is a free-to-play simulation video game developed by Bethesda Game Studios, with assistance by Behaviour Interactive, and published by Bethesda Softworks.
- [d9s1]  Part of the "Fallout" series, it was released worldwide for iOS devices in June 2015, for Android devices in August 2015, for Microsoft Windows in July 2016, and Xbox One in February 2017.
- [d9s2]  The game tasks the player with building and managing their own Vault, a fallout shelter.

**d10: Fallout 4**

- [d10s0] Fallout 4 is an action role-playing video game developed by Bethesda Game Studios and published by Bethesda Softworks.
- [d10s1]  It is the fifth major installment in the "Fallout" series, and was released worldwide on November 10, 2015, for Microsoft Windows, PlayStation 4 and Xbox One.
- [d10s2]  The game is set within an open world post-apocalyptic environment that encompasses the city of Boston and the surrounding Massachusetts region known as "The Commonwealth".
- [d10s3]  The main story takes place in the year 2287, ten years after the events of "Fallout 3" and 210 years after "The Great War", which caused catastrophic nuclear devastation across the United States.

## 29. hotpotqa_5ae29b615542992decbdcd4f

原位置：`dev` 第 56 题 · 全局第 299 题 · `sample_id: hotpotqa_5ae29b615542992decbdcd4f`

Question: Huainan and Wuzhishan City, in in which country?

Note: 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

Type: comparison · fallback: False · SFT snapshots: 6

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | country containing Huainan | False | [] | People's Republic of China | [["d1s0"]] | context |
| u2 | country containing Wuzhishan City | False | [] | People's Republic of China | [["d2s0"]] | context |
| u3 | country containing both Huainan and Wuzhishan City | True | ["u1", "u2"] | People's Republic of China | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country containing Huainan | False | [] | People's Republic of China | [['d1s0']] |
| u2 | country containing Wuzhishan City | False | [] | People's Republic of China | [['d2s0']] |
| u3 | country containing both Huainan and Wuzhishan City | True | ['u1', 'u2'] | People's Republic of China | [[]] |

### Source documents (reference only)

**d1: Huainan**

- [d1s0] Huainan () is a prefecture-level city with 2,334,000 inhabitants in central Anhui Province, People’s Republic of China.
- [d1s1]  It borders the provincial capital of Hefei to the south, Lu'an to the southwest, Fuyang to the west, Bozhou to the northwest, Bengbu to the northeast and Chuzhou to the east.

**d2: Wuzhishan City**

- [d2s0] Wuzhishan () is a county-level city in the south-central part of Hainan, a province of the People's Republic of China.
- [d2s1]  Although called a "city", Wuzhishan refers to a large land area in Hainan - an area which was once a county.
- [d2s2]  Within this area is the main city, Wuzhishan City.
- [d2s3]  It was originally called Tōngzá () and is located beside Wuzhi Shan, the mountain.
- [d2s4]  The city's total area is 1129 square kilometres, and its population is 115,000 people.
- [d2s5]  Its postal code is 572200, and its district number is 0898.

**d3: Wuzhi Mountain**

- [d3s0] Wuzhi Mountain () is the highest mountain in Hainan, China, towering 1840 m above the center of Hainan Island.
- [d3s1]  The surrounding areas of Wuzhi Mountain are inhabited mainly by the Li ethnic group.
- [d3s2]  It is located adjacent to Wuzhishan City but is not part of that city's administrative area.

## 30. hotpotqa_5ae517665542990ba0bbb1b2

原位置：`dev` 第 57 题 · 全局第 300 题 · `sample_id: hotpotqa_5ae517665542990ba0bbb1b2`

Question: What singer did the Tiny Dancers support who was in The Verve?

Note: 保留新顺序，先列支持过的艺人/乐队集合，再筛选 The Verve 歌手；不能先验只写 Richard Ashcroft。

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新顺序，先列支持过的艺人/乐队集合，再筛选 The Verve 歌手；不能先验只写 Richard Ashcroft。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | acts supported by the Tiny Dancers listed in the context | False | [] | The Spinto Band; Babyshambles; Richard Ashcroft; Larrikin Love; Bob Dylan | [["d10s2"]] | context |
| u2 | singer among {u1} who was in The Verve | True | ["u1"] | Richard Ashcroft | [["d6s0", "d6s1"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | singer who was in the band The Verve | False | [] | Richard Ashcroft | [['d6s1']] |
| u2 | singer supported by the Tiny Dancers who was in The Verve, given {u1} | True | ['u1'] | Richard Ashcroft | [['d10s2']] |

### Source documents (reference only)

**d1: Natalie Duncan**

- [d1s0] Natalie Duncan (born Natalie Alexis Duncan 18 November 1988) is a British singer and songwriter from Nottingham, signed to Verve Records.
- [d1s1]  She released her debut EP "Natalie Alexis Duncan" on the Farmyard Records label in 2009 and then featured in BBC2's , broadcast in March and April 2011.
- [d1s2]  She released her debut album "Devil In Me" (recorded at Real World Studios and produced by Joe Henry) on the Verve label in July 2012.
- [d1s3]  She has been compared to the likes of Alicia Keys and Nina Simone.

**d2: Hopeless Romantic (Michelle Branch album)**

- [d2s0] Hopeless Romantic is the third studio album by American singer and songwriter Michelle Branch.
- [d2s1]  It was released on April 7, 2017, by Verve Records.
- [d2s2]  Co-written and co-produced by Patrick Carney, whom Branch is dating, the album is Branch's first release with Verve after leaving her previous label, Reprise Records, and having the original album material scrapped.
- [d2s3]  "Hopeless Romantic" is also Branch's first full-length album to be released since "Hotel Paper" (2003), and first overall release since the "Everything Comes and Goes" EP in 2010.

**d3: Free School Milk**

- [d3s0] Free School Milk is the first album by English band Tiny Dancers.
- [d3s1]  It was released on 11 June 2007 in the UK.

**d4: Jukebox Ella: The Complete Verve Singles, Vol. 1**

- [d4s0] Jukebox Ella: The Complete Verve Singles, Vol.
- [d4s1]  1 is a 2003 compilation album by the American jazz singer Ella Fitzgerald.
- [d4s2]  The album contains all the singles Fitzgerald recorded for Verve Records label between 1956 and 1965.

**d5: Fall into the Open**

- [d5s0] Fall Into The Open is the first studio album from American Recording Artist, Cris Gunther, released in 2007 on iTunes, CD Baby & Amazon.com.
- [d5s1]  Executived Produced by Cris Gunther, Terry Gunther, and Mary Ann Marchasella.
- [d5s2]  Produced by Tim K (Les Nubians, Tiny Hearts, Russell Taylor, Collette, and Esthero), and Fab Dupont (Shakira, Jennifer Lopez).
- [d5s3]  Written by Cris Gunther, Mic Murphy (The System), Tim K, Fab Dupont, and Richard Lynch.
- [d5s4]  The album features Mic Murphy (The System) on the track, "Black Doll", and, Verve/Universal Recording Artist, Lucy Woodward, on the tracks, "Gotta Give", "Sacred Sexuality", and the Kylie Minogue cover, "Turn It Into Love".
- [d5s5]  The album was mixed by Fab Dupont.
- [d5s6]  And, the track, "The Heat", was featured in a Songwriter's Hall Of Fame Showcase in New York City in 2002, which was featured in Billboard Magazine.
- [d5s7]  There are ten songs on this recording.

**d6: Richard Ashcroft**

- [d6s0] Richard Paul Ashcroft (born 11 September 1971) is an English singer and songwriter.
- [d6s1]  He was the lead singer and occasional rhythm guitarist of the alternative rock band The Verve from their formation in 1990 until their original split in 1999.
- [d6s2]  He became a successful solo artist in his own right, releasing three UK top three solo albums.
- [d6s3]  The Verve reformed in 2007 but again broke up by summer 2009.
- [d6s4]  Ashcroft then founded a new band, RPA & The United Nations of Sound, and released a new album on 19 July 2010.
- [d6s5]  On 22 February 2016 Ashcroft announced his fourth solo album, "These People", set for release 20 May 2016.
- [d6s6]  Chris Martin of Coldplay has described Ashcroft as "the best singer in the world".

**d7: Career Transition For Dancers**

- [d7s0] Career Transition For Dancers is a nonprofit organization with offices in New York, Los Angeles and Chicago dedicated to helping dancers establish new careers when they have retired from their performing careers.
- [d7s1]  Founded in 1985, the organization has provided over 46,000 hours of individual and group career counseling, with a dollar value of over $4 million, and awarded over $3 million in educational and entrepreneurial support.
- [d7s2]  The organization has 4,600 active dancer-clients and has helped thousands of dancers in 47 states with their transitions through mobile National Outreach Projects.
- [d7s3]  The organization helps dancers in all stages of their career whether they are students, pre-professional, or artists at the peak of their career.
- [d7s4]  Its vision is to help every dancer reach their full potential.

**d8: More Than a New Discovery**

- [d8s0] More Than a New Discovery is the debut album by Bronx-born singer, songwriter, and pianist Laura Nyro.
- [d8s1]  It was recorded during 1966 and released at the beginning of the following year on the Folkways imprint of the Verve label (this imprint was changed to Verve Forecast Records after Verve was threatened with legal action by Moses Asch who owned the Folkways label).
- [d8s2]  The album was reissued in 1969 as Laura Nyro, with a revised track order and slightly altered cover/back cover design—and again in 1973 as The First Songs, with an all-new cover design (featuring a rose illustration), and the song "Hands Off the Man" retitled to "Flim Flam Man".
- [d8s3]  It gave Nyro a chart entry at #97 on the "Billboard" 200, then known as the Pop Albums chart.

**d9: English Amateur Dancesport Association**

- [d9s0] The English Amateur Dancesport Association (EADA) Ltd is a volunteer-led organisation which represents the interests of Amateur Dancers (including Ballroom, Latin American, Sequence dancing and Freestyle) within England.
- [d9s1]  EADA provides support and training for Amateur dancers and acts as the voice of English Amateur dancers amongst other dance organisations both in the UK and overseas.
- [d9s2]  EADA also aims to get the younger audience involved and on the dance floor.
- [d9s3]  EADA hopes to increase the profile of dancesport.

**d10: Tiny Dancers**

- [d10s0] Tiny Dancers were an English band from South Elmsall, West Yorkshire.
- [d10s1]  They are David William Kay (vocals, acoustic guitar), Chris Etherington (lead guitar, keyboards), Dale Wathey (bass guitar), Duncan Morrison (drums) and David Glover (keyboards, glockenspiel, percussion, guitar).
- [d10s2]  Based in Sheffield, they signed to Parlophone in early 2006 and supported acts as diverse as The Spinto Band, Babyshambles, Richard Ashcroft, Larrikin Love, Bob Dylan, as well as a co-headlining tour with Ghosts and their own headline tour.
