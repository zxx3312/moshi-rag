# dev: A decomposer review

<!-- SFT_REVIEW_GUIDE_BEGIN -->
**审阅原则：新旧单元都合理时，跟拆题器对齐。** 合理的合并、顺序或取值形式变化不要求恢复旧拆法；人工答案、证据集合、依赖标签与逐时刻 SFT 快照需按新单元重新标注。

题目旁标记：**需改：生成拆解**＝发现题意、关系、目标或题型问题；**保留新拆法｜重标人工标签**＝生成单元保留，调整监督；**待确认**＝问题或答案口径需人工裁定。未标记不代表旧标签可以直接复制。

本页是 AI 辅助审阅建议，不是人工验收或已重建的训练数据。原始生成 JSON、人工 gold 和 B 组文件未修改。统计与逐题索引见 [comparison_human.md](comparison_human.md)。
<!-- SFT_REVIEW_GUIDE_END -->

模型仅看到问题。新单元未经人工复核；旧 gold 仅供对照，不作为新单元标签。

## 1. 2wikimultihopqa_008905100baf11ebab90acde48001122

Question: Who is Apama Iii's father-in-law?

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | spouse of Apama Iii | False | () |
| u2 | father of {u1}, Apama Iii's father-in-law | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | spouse of Apama III | False | [] | Prusias I of Bithynia | [['d7s8']] |
| u2 | father of {u1}, Apama III's father-in-law | True | ['u1'] | Ziaelas of Bithynia | [['d4s5']] |

### Source documents (reference only)

**d1: Harry Smith (athlete)**

- [d1s0] Harry James Smith( July 30, 1888 – November 20, 1962) was an American long- distance runner.
- [d1s1] He was most notable for competing in the 1912 Olympics in Stockholm.
- [d1s2] He was also the father of Hart wrestling family matriarch Helen Hart and the father- in- law of Stu Hart.

**d2: John Vernou Bouvier III**

- [d2s0] John Vernou" Black Jack" Bouvier III( May 19, 1891 – August 3, 1957) was an American Wall Street stockbroker and socialite.
- [d2s1] He was the father of First Lady Jacqueline Kennedy Onassis and of socialite Lee Radziwill, and was the father- in- law of John F. Kennedy.

**d3: Ogawa Mataji**

- [d3s0] Viscount was a general in the early Imperial Japanese Army.
- [d3s1] He was also the father- in- law of Field Marshal Gen Sugiyama.

**d4: Prusias I of Bithynia**

- [d4s0] Prusias I Cholus
- [d4s1] (Greek:
- [d4s2] Προυσίας
- [d4s3] ὁ Χωλός
- [d4s4] "the Lame")
- [d4s5] (lived c. 243 – 182 BC, reigned c. 228 – 182 BC) was a king of Bithynia, the son of Ziaelas of Bithynia.

**d5: Peter Burroughs**

- [d5s0] Peter Burroughs( born 27 January 1947) is a British television and film actor, the director of Willow Management.
- [d5s1] He is the father- in- law of actor and TV presenter Warwick Davis.

**d6: James Armour (Master mason)**

- [d6s0] James Armour (15 January 1730 – 20 September 1798) was a master mason and father of Jean Armour, and therefore the father-in-law of the poet Robert Burns.

**d7: Apama III**

- [d7s0] Apama III, sometimes known as Apame III( born c. 250 BC, flourished 3rd and 2nd century BC) was a Greek princess from the Antigonid dynasty.
- [d7s1] Apama was of Greek Macedonian and Persian descent.
- [d7s2] She was the child born to the King Demetrius II Aetolicus and Queen Stratonice of Macedon.
- [d7s3] Her paternal grandparents were the Antigonid Monarchs Antigonus II Gonatas and Phila, while her maternal grandparents were the Seleucid Monarchs Antiochus I Soter and Stratonice of Syria.
- [d7s4] From her father ’s second marriage, she had a younger paternal half- brother called Philip V of Macedon who would eventually succeed as king.
- [d7s5] Apama was the namesake of her maternal aunt Apama II, who was the wife of King Magas of Cyrene and mother of the Ptolemaic Queen Berenice II.
- [d7s6] Apama was born and raised in Macedonia.
- [d7s7] Her father formed an alliance with the Greek King of Anatolia Prusias I of Bithynia.
- [d7s8] Apama later married Prusias I and through her marriage, became Queen of Bithynia.
- [d7s9] Apama bore Prusias I, a son and his successor called Prusias II of Bithynia, sometimes known as" Prusias II CynegusCynegus" means" the Hunter".
- [d7s10] Her husband was also an ally to her half brother, Philip V. After Philip V, took the port city of Prusa, her husband rebuilt the city around 202 BC and renamed the city" Apamea Myrlea", which still bears her name.
- [d7s11] Her daughter- in- law was her niece and namesake Apame IV.
- [d7s12] Apame IV was one of the daughters of her half brother and later married her son.

**d8: Barthold A. Butenschøn Sr.**

- [d8s0] Hans Barthold Andresen Butenschøn( 27 December 1877 – 28 November 1971) was a Norwegian businessperson.
- [d8s1] He was born in Kristiania as a son of Nils August Andresen Butenschøn and Hanna Butenschøn, and grandson of Nicolay Andresen.
- [d8s2] Together with Mabel Anette Plahte( 1877 – 1973, a daughter of Frithjof M. Plahte) he had the son Hans Barthold Andresen Butenschøn Jr. and was through him the father- in- law of Ragnhild Butenschøn and grandfather of Peter Butenschøn.
- [d8s3] Through his daughter Marie Claudine he was the father- in- law of Joakim Lehmkuhl, through his daughter Mabel Anette he was the father- in- law of Harald Astrup( a son of Sigurd Astrup) and through his daughter Nini Augusta he was the father- in- law of Ernst Torp.
- [d8s4] He took commerce school and agricultural school.
- [d8s5] He was hired in the family company N. A. Andresen& Co, and became a co-owner in 1910.
- [d8s6] He eventually became chief executive officer.
- [d8s7] The bank changed its name to Andresens Bank in 1913 and merged with Bergens Kreditbank in 1920.
- [d8s8] The merger was dissolved later in the 1920s.
- [d8s9] He was also a landowner, owning Nedre Skøyen farm and a lot of land in Enebakk.
- [d8s10] He chaired the board of Nydalens Compagnie from 1926, having not been a board member before that.
- [d8s11] He also chaired the supervisory council of Forsikringsselskapet Viking and Nedre Glommen salgsforening, and was a supervisory council member of Filharmonisk Selskap.
- [d8s12] He was a member of the gentlemen's club SK Fram since 1890, and was proclaimed a lifetime member in 1964.
- [d8s13] He was buried in Enebakk.

**d9: John Adams (merchant)**

- [d9s0] John Adams( 1672 or 1673 – 1745) was an American- born Canadian merchant and member of the Nova Scotia Council.
- [d9s1] He was the father- in- law of Henry Newton( politician).

**d10: Ludwig von Westphalen**

- [d10s0] Johann Ludwig von Westphalen( 11 July 1770 – 3 March 1842) was a liberal Prussian civil servant and the father- in- law of Karl Marx.

## 2. 2wikimultihopqa_363145e20baf11ebab90acde48001122

Question: Who is the paternal grandfather of Helvis Of Cyprus?

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Helvis Of Cyprus | False | () |
| u2 | father of {u1}, Helvis Of Cyprus's paternal grandfather | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Helvis of Cyprus | False | [] | Amalric II of Jerusalem | [['d2s0']] |
| u2 | father of {u1}, Helvis of Cyprus's paternal grandfather | True | ['u1'] | Hugh VIII of Lusignan | [['d9s0', 'd9s2']] |

### Source documents (reference only)

**d1: Fred Le Deux**

- [d1s0] Frederick" Fred" Le Deux( born 4 December 1934) was an Australian rules footballer who played with Geelong in the Victorian Football League( VFL).
- [d1s1] He is the grandfather of Tom Hawkins.

**d2: Helvis of Cyprus**

- [d2s0] Helvis of Lusignan (c. 1190 – c. 1218) was the daughter of Amalric II of Jerusalem, King of Cyprus, and his wife, Eschive d'Ibelin.
- [d2s1] She was married twice.
- [d2s2] Firstly, she was given in marriage to Eudes de Dampierre, a French knight, in about 1205.
- [d2s3] With Eudes she had children, including eldest son
- [d2s4] The details of her second marriage are revealed in a letter from Pope Innocent III to the archbishop of Antioch, dated September 1211.
- [d2s5] Helvis had been taken from her husband (or fled him) by the young Raymond-Roupen of Antioch, designated heir to the Armenian throne, and although ecclesiastical authorities commanded the return to her husband Eudes de Dampierre, Helvis refused.
- [d2s6] The young couple seem to have been encouraged by Helvis' brother-in-law, Walter of Montbéliard, which infuriated Helvis' brother King Hugh.
- [d2s7] She and Raymond-Roupen had issue:

**d3: Phoebus of Lusignan**

- [d3s0] Phoebus of Lusignan( died after July, 1485 in Rome)( also called Febo or Febos in Portuguese) was a titular Marshal of Armenia and also titular Lord of Sidon, the illegitimate son of Peter of Lusignan, titular Count of Tripoli.

**d4: Kaya Alp**

- [d4s0] Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

**d5: Helvis of Brunswick-Grubenhagen**

- [d5s0] Helvis of Brunswick- Grubenhagen( 1353 – 15 January 1421), was the Queen consort of Cyprus and Queen consort of Armenia as the wife of King James I of Cyprus.
- [d5s1] He was also titular King of Jerusalem.
- [d5s2] She was styled Queen of Cyprus from 1382 to 1398; although at the time of his ascension to the Cypriot throne, he and Helvis were imprisoned in Genoa after they had been captured by the Genoese on the island of Rhodes.
- [d5s3] Almost all of Helvis' 12 children were born to her while she was held prisoner.
- [d5s4] In 1385, after negotiations and many ruinous concessions to the Genoese, they were released and James was crowned king.
- [d5s5] In 1393, she became Queen of Armenia.

**d6: John of Lusignan**

- [d6s0] John of Lusignan( or Jean de Lusignan)( c. 1329 or 1329/1330–1375), regent of the Kingdom of Cyprus and titular Prince of Antioch.
- [d6s1] He was son of King Hugh IV of Cyprus and his second wife, Alix of Ibelin.
- [d6s2] He was a member of the House of Lusignan.

**d7: Isabella of Lusignan**

- [d7s0] Isabella of Lusignan( c.1224 – 14 January 1300) was a daughter of Hugh X of Lusignan and his wife Isabella of Angoulême, Dowager Queen of England.
- [d7s1] Isabella was half- sister to King Henry III of England.
- [d7s2] She was Dame de Beauvoir- sur Mer et de Mercillac.

**d8: Henry Krause**

- [d8s0] Henry J." Red" Krause, Jr.( August 28, 1913 – February 20, 1987) was an American football offensive lineman in the National Football League for the Brooklyn Dodgers and the Washington Redskins.
- [d8s1] He played college football at St. Louis University.
- [d8s2] He is the grandfather of Jennifer Krause
- [d8s3] He is the great grandfather of Payton Hoeing

**d9: Aimery of Cyprus**

- [d9s0] Aimery of Lusignan ("Amorí"; before 11551 April 1205), erroneously referred to as Amalric or Amaury in earlier scholarship, was the first King of Cyprus, reigning from 1196 to his death.
- [d9s1] He also reigned as King of Jerusalem from his marriage to Isabella I in 1197 to his death.
- [d9s2] He was the younger son of Hugh VIII of Lusignan, a nobleman in Poitou.
- [d9s3] After participating in a rebellion against Henry II of England in 1168, he went to the Holy Land and settled in the Kingdom of Jerusalem.
- [d9s4] His marriage to Eschiva of Ibelin (whose father, Baldwin of Ibelin was an influential nobleman) strengthened his position in the kingdom.
- [d9s5] His younger brother, Guy, married Sibylla, the sister of and heir to Baldwin IV of Jerusalem.
- [d9s6] Baldwin made Aimery Constable of Jerusalem around 1180.
- [d9s7] He was one of the commanders of the Christian army in the Battle of Hattin, which ended with decisive defeat at the hands of the army of Saladin, the Ayyubid sultan of Egypt and Syria, on 4 July 1187.
- [d9s8] Aimery supported his brother, Guy, even after Guy had lost his claim to the Kingdom of Jerusalem according to most barons of the realm, because of the death of Sibylla and their two daughters.
- [d9s9] The new king of Jerusalem, Henry of Champagne, arrested him for a short period.
- [d9s10] After his release, he retired to Jaffa which was the fief of his elder brother, Geoffrey of Lusignan, who had left the Holy Land.
- [d9s11] After Guy died in May 1194, his vassals in Cyprus elected Aimery as their lord.
- [d9s12] He accepted the suzerainty of the Holy Roman Emperor, Henry VI.
- [d9s13] With the emperor's authorization, Aimery was crowned King of Cyprus in September 1197.
- [d9s14] He soon married Henry of Champagne's widow, Isabella I of Jerusalem.
- [d9s15] He and his wife were crowned king and queen of Jerusalem in January 1198.
- [d9s16] He signed a truce with Al-Adil I, the Ayyubid sultan of Egypt, which secured the Christian possession of the coastline from Acre to Antioch.
- [d9s17] His rule was a period of peace and stability in both of his realms.

**d10: Maria of Antioch-Armenia**

- [d10s0] Maria of Antioch- Armenia( 1215–1257) was lady of Toron from 1229 to her death.
- [d10s1] She was the elder daughter of Raymond- Roupen, prince of Antioch, and of Helvis of Lusignan.
- [d10s2] She derived her title of Lady of Toron and claim to the throne of Armenia from her father.
- [d10s3] Maria's paternal grandmother Alice became lady of Toron when emperor Frederick II, at the end of the Sixth Crusade, negotiated the return of lands conquered by Saladin; Maria succeeded her as she was the closest surviving relative.
- [d10s4] In 1240 she married Philip of Montfort, Lord of Tyre, previously lord of Castres, and they had the following children:
- [d10s5] She was the great- granddaughter of Roupen III, prince of Armenia( Roupen III's daughter was Alice), who had been succeeded by his brother Leo I. Maria thus unsuccessfully claimed rights to the throne of Armenia, something her father and grandmother had previously attempted and failed.

## 3. 2wikimultihopqa_3a2fe93e0bda11eba7f7acde48001122

Question: What nationality is Keith Batey's wife?

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | wife of Keith Batey | False | () |
| u2 | nationality of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | wife of Keith Batey | False | [] | Mavis Batey | [['d2s0']] |
| u2 | nationality of {u1} | True | ['u1'] | British | [['d3s0']] |

### Source documents (reference only)

**d1: Iraqi nationality law**

- [d1s0] Iraqi nationality is transmitted by one's parents.

**d2: Keith Batey**

- [d2s0] Keith Batey( 4 July 1919 – 28 August 2010) was a codebreaker who, with his wife, Mavis Batey( 5 May 1921 – 12 November 2013), worked on the German Enigma machine at Bletchley Park during World War II.

**d3: Mavis Batey**

- [d3s0] Mavis Lilian Batey, MBE( née Lever; 5 May 1921 – 12 November 2013), was an English code- breaker during World War II.
- [d3s1] Her work at Bletchley Park was one of the keys to the success of D- Day.
- [d3s2] She later became an historian of gardening, who campaigned to save historic parks and gardens, and an author.
- [d3s3] Batey was awarded the Veitch Memorial Medal in 1985, and made a Member of the Order of the British Empire( MBE) in 1987, in both cases for her work on the conservation of gardens.

**d4: Nayelly Hernández**

- [d4s0] Nayelly Hernández( born 23 February 1986) is a former Mexican female professional squash player.
- [d4s1] She has represented Mexico internationally in several international competitions including the Central American and Caribbean Games, Pan American Games, Women's World Team Squash Championships.
- [d4s2] Nayelly achieved her highest career ranking of 57 in October 2011 during the 2011 PSA World Tour.
- [d4s3] Her husband Chris Walker whose nationality is English is also a professional squash player.
- [d4s4] She joined the Trinity College in 2008 as the first Mexican female to join a US college for squash and graduated in 2010.

**d5: Baglan Mailybayev**

- [d5s0] Baglan Mailybayev( in Kazakh Бағлан Асаубайұлы Майлыбаев) was born on 20 May 1975 in Zhambyl region, Kazakhstan.
- [d5s1] His nationality is Kazakh.
- [d5s2] He is a politician of the Republic of Kazakhstan, Deputy Head of the Presidential Administration of the Republic of Kazakhstan, Doctor of Law( 2002)( under the supervision of Professor Zimanov S.Z.- scientific advisor and academician of National Academy of Sciences of the Republic of Kazakhstan) and Ph.D. in Political Science( 1998).

**d6: Eleni Gabre-Madhin**

- [d6s0] Eleni Zaude Gabre- Madhin, an Ethiopian economist with Swiss nationality, is a former Chief Executive Officer of the Ethiopia Commodity Exchange( ECX).
- [d6s1] She has had many years of experience working on agricultural markets – particularly in Sub- Saharan Africa – and has held senior positions in the World Bank, the International Food Policy Research Institute( Washington), and United Nations( Geneva).

**d7: Mário Laginha**

- [d7s0] Mário João Laginha dos Santos,( born April 25, 1960 in Lisbon), a pianist and composer, is one of the most well- known Portuguese jazz musicians today.
- [d7s1] He is mostly recognized for his collaborations with Portuguese jazz singer Maria João, with whom he recorded over a dozen albums and toured worldwide extensively.
- [d7s2] Other acknowledged collaboration work includes four- handed piano sessions with Bernardo Sassetti and Pedro Burmester.
- [d7s3] Mário's main influence on piano is Keith Jarrett.

**d8: Ali Rahuma**

- [d8s0] Ali Khalifa Rahuma( born May 16, 1982) is a Libyan football midfielder who's nationality is Libyan.
- [d8s1] He currently plays for Al- Ittihad, and is a member of the Libya national football team.

**d9: Malcolm Sinclair (actor)**

- [d9s0] Malcolm Sinclair( born 5 June 1950) is a British stage and television actor and former President of Trade Union, Equity 2010 – 18 when he stood down after 4 terms and was replaced by Maureen Beattie.
- [d9s1] He is perhaps best known for his role as Assistant Chief Constable Freddy Fisher in the television series" Pie in the Sky"( 1994 – 1997), although he has an extensive number of film, television and theatre roles to his credit.
- [d9s2] His brother is Keith Sinclair, the Bishop of Birkenhead.

**d10: Rebirth (Keith Sweat album)**

- [d10s0] Rebirth is Keith Sweat's eighth studio album.

## 4. 2wikimultihopqa_4dc594f408cd11ebbd93ac1f6bf848b6

Question: Which film has the director died earlier, Schwarzwaldmelodie or Vacations in the Other World?

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of Schwarzwaldmelodie | False | () |
| u2 | death date of {u1} | False | ('u1',) |
| u3 | director of Vacations in the Other World | False | () |
| u4 | death date of {u3} | False | ('u3',) |
| u5 | which film's director died earlier | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Schwarzwaldmelodie | False | [] | Géza von Bolváry | [['d5s0']] |
| u2 | date of death of {u1} | False | ['u1'] | 10 August 1961 | [['d10s0']] |
| u3 | director of film Vacations in the Other World | False | [] | Mario Soffici | [['d2s0']] |
| u4 | date of death of {u3} | False | ['u3'] | 10 May 1977 | [['d7s0']] |
| u5 | which of the two films has the director who died earlier | True | ['u2', 'u4'] | Schwarzwaldmelodie | [[]] |

### Source documents (reference only)

**d1: Le Masque de la Méduse**

- [d1s0] Le masque de la Méduse is a 2009 fantasy horror film directed by Jean Rollin.
- [d1s1] The film is a modern-day telling of the Greek mythological tale of the Gorgon and was inspired by the 1964 classic Hammer Horror film of the same name and the 1981 cult classic" Clash of the Titans".
- [d1s2] It was Rollin's final film, as the director died in 2010.

**d2: Vacations in the Other World**

- [d2s0] Vacations in the Other World or Vacaciones en el otro mundo is a 1942 Argentine film directed by Mario Soffici.
- [d2s1] The film, a seriocomedy, explores the gap between the high- pressure world of business and the ambience of domestic living.

**d3: A Groom from the Other World**

- [d3s0] A Groom from the Other World or is a 1958 Soviet comedy film directed by Leonid Gaidai.

**d4: Thulasi (1987 film)**

- [d4s0] Thulasi is a 1987 Tamil romantic drama film directed by Ameerjan.
- [d4s1] The film features Murali and Seetha in lead roles.
- [d4s2] The film, produced by P. S. V. Hariharan, had musical score by Sampath Selvam and was released on 27 November 1987.
- [d4s3] The music director died before the release of the film.

**d5: Schwarzwaldmelodie**

- [d5s0] Schwarzwaldmelodie is a 1956 West German film directed by Géza von Bolváry.
- [d5s1] The film was produced in de Ufa-Studios Berlin and in the Circus Roland.

**d6: Vacations in Majorca**

- [d6s0] Vacations in Majorca is a 1959 Italian comedy film directed by Giorgio Bianchi.

**d7: Mario Soffici**

- [d7s0] Mario Soffici( 14 May 1900 – 10 May 1977) was an Argentine film director, actor and screenwriter of the classic era.
- [d7s1] A native of Florence, Soffici moved to Argentina in the 1920s and began acting in 1931 and directing in 1935 on the film" El Alma de Bandoneón", working with popular actors of the period such as Libertad Lamarque in tango- based musical films.
- [d7s2] He directed some 40 films between 1935 and 1962, most notably" Prisioneros de la tierra"( 1939)( often cited as one of the greatest in Argentine cinema)," El Curandero"( 1955)," El hombre que debía una muerte"( 1955) and" Rosaura a las 10"( 1958).
- [d7s3] He directed and co- wrote with Eduardo Boneo and Francisco Madrid" La cabalgata del circo," where Eva Duarte played a supporting role.
- [d7s4] He died in Buenos Aires in 1977.

**d8: Mohsen Eslamzadeh**

- [d8s0] Mohsen Eslamzadeh is an Iranian documentary filmmaker.
- [d8s1] He is the director of" Alone Among The Taliban".
- [d8s2] This film has won the best documentary award at the 44th Athens International Film and Video Festival in the United States.
- [d8s3] This film has won the best documentary award at the 12th Marbella International Film Festival in Spain.
- [d8s4] This film has won the Shahid Avini Award offers.

**d9: Querelle**

- [d9s0] Querelle is a 1982 West German- French English- language drama film directed by Rainer Werner Fassbinder and starring Brad Davis, adapted from French author Jean Genet's 1947 novel" Querelle of Brest".
- [d9s1] It marked Fassbinder's final film as a writer/ director; it was posthumously released just months after the director died of a drug overdose in June 1982.

**d10: Géza von Bolváry**

- [d10s0] Géza von Bolváry (full name Géza Maria von Bolváry-Zahn; 26 December 1897 – 10 August 1961) was a Hungarian actor, screenwriter and film director, who worked principally in Germany and Austria.

## 5. 2wikimultihopqa_5ea97157099411ebbdb0ac1f6bf848b6

Question: Are Rasas and Barakuh, Roshtkhar located in the same country?

Type: comparison · fallback: False · SFT snapshots: 7

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of Rasas | False | () |
| u2 | country of Barakuh, Roshtkhar | False | () |
| u3 | whether Rasas and Barakuh, Roshtkhar are in the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country of Rasas | False | [] | Syria | [['d9s0']] |
| u2 | country of Barakuh, Roshtkhar | False | [] | Iran | [['d10s0']] |
| u3 | whether Rasas and Barakuh, Roshtkhar are located in the same country | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Satellite tournament**

- [d1s0] A satellite tournament is either a minor tournament or event on a competitive sporting tour or one of a group of such tournaments that form a series played in the same country or region.

**d2: Language Management**

- [d2s0] Language management is a discipline that consists of satisfying the needs of people who speak multiple different languages.
- [d2s1] These may be in the same country, in companies, and in cultural or international institutions where one must use multiple languages.

**d3: Kumaradeva**

- [d3s0] Kumaradeva was an Indian sculptor from the 8th century.
- [d3s1] His works include" The Buddhist Goddess Shyama Tara( Green Tara) Attended by Sita Tara( White Tara) and Bhrikuti"
- [d3s2] He is also the author of the treatise" Silparatna", which provides an account of the Fresco- secco painting technology in detail.
- [d3s3] According to this text, a picture should be painted with appropriate colours along with proper forms and sentiments( rasas), and moods and actions( bhavas).

**d4: 1992 Copa Libertadores**

- [d4s0] The 1992 Copa Libertadores was the 33rd edition of the Copa Libertadores, CONMEBOL's annual international club tournament.
- [d4s1] São Paulo won the competition.
- [d4s2] The participating teams were divided into five groups, in which teams of the same country were placed in the same group.
- [d4s3] Each country was represented by two teams.
- [d4s4] The countries were paired as follows:

**d5: Telephone numbers in Ascension Island**

- [d5s0] Country Code:+ 247< br> International Call Prefix: 00 Ascension Island does not share the same country code( +290) with the rest of St Helena.

**d6: 2001–02 UEFA Champions League second group stage**

- [d6s0] Eight winners and eight runners- up from the first group stage were drawn into four groups of four teams, each containing two group winners and two runners- up.
- [d6s1] Teams from the same country or from the same first round group could not be drawn together.
- [d6s2] The top two teams in each group advanced to the quarter- finals.

**d7: 1993 Copa Libertadores**

- [d7s0] The Copa Libertadores 1993 was the 34th edition of the Copa Libertadores, CONMEBOL's annual international club tournament.
- [d7s1] São Paulo won the competition.
- [d7s2] The participating teams were divided into five groups, in which teams of the same country were placed in the same group.
- [d7s3] Each country was represented by two teams.
- [d7s4] The countries were paired as follows:

**d8: 1971 Copa Libertadores**

- [d8s0] The Copa Libertadores 1971 was the 12th edition of the Copa Libertadores, CONMEBOL's annual international club tournament.
- [d8s1] Nacional won the competition.
- [d8s2] The participating teams were divided into five groups, in which teams of the same country were placed in the same group.
- [d8s3] Each country was represented by two teams.
- [d8s4] The countries were paired as follows:

**d9: Rasas**

- [d9s0] Rasas( also spelled Rsas) is a village in southern Syria, administratively part of the al- Suwayda Governorate, located south of al- Suwayda.
- [d9s1] Nearby localities include' Ira to the southwest, Sahwat Bilata to the east, al- Ruha to the northeast and Umm Walad to the west.
- [d9s2] According to the Syria Central Bureau of Statistics( CBS), Rasas had a population of 3,332 in the 2004 census.

**d10: Barakuh, Roshtkhar**

- [d10s0] Barakuh( also Romanized as Barākūh) is a village in Roshtkhar Rural District, in the Central District of Roshtkhar County, Razavi Khorasan Province, Iran.
- [d10s1] At the 2006 census, its population was 872, in 221 families.

## 6. 2wikimultihopqa_640bede1095311ebbdaeac1f6bf848b6

Question: Are Daher-Socata and Dsf Refractories & Minerals Ltd both located in the same country?

Type: comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country where Daher-Socata is located | False | () |
| u2 | country where Dsf Refractories & Minerals Ltd is located | False | () |
| u3 | whether Daher-Socata and Dsf Refractories & Minerals Ltd are located in the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country of DAHER-SOCATA | False | [] | France | [['d6s1']] |
| u2 | country of DSF Refractories & Minerals Ltd | False | [] | United Kingdom | [['d4s0']] |
| u3 | whether Daher-Socata and DSF Refractories & Minerals Ltd are located in the same country | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Adam Sulzdorf-Liszkiewicz**

- [d1s0] Adam Sulzdorf- Liszkiewicz is a designer, scholar, and educator who teaches at Occidental College and is CEO of RUST LTD, both in Los Angeles.
- [d1s1] He is best known for his designs for popular virtual reality games and serious games.

**d2: Jawty**

- [d2s0] Jawty is part of the name of two villages, both located in Gmina Susz, within Iława County, Warmian- Masurian Voivodeship, Poland:

**d3: List of Capcom subsidiaries**

- [d3s0] Apart from the head office building and the R&D building of Capcom Co., Ltd., both located in Chūō -ku, Osaka, the Japanese parent company also has a branch office in the Shinjuku Mitsui Building in Nishi- Shinjuku, Shinjuku, Tokyo.
- [d3s1] It also has the Ueno Facility.
- [d3s2] a branch office in Iga, Mie Prefecture.
- [d3s3] The international Capcom Group currently encompasses 15 subsidiaries in Japan, North America, Europe, and East Asia.
- [d3s4] Affiliated companies include Koko Capcom Co., Ltd. in South Korea, Street Fighter Film, LLC in the United States, and Dellgamadas Co., Ltd.

**d4: DSF Refractories & Minerals Ltd**

- [d4s0] DSF Refractories and Minerals Limited (formerly Derbyshire Silica Firebrick Co Ltd) is the last major British producer of refractory products, both shaped and unshaped.
- [d4s1] DSF is located in Friden within the Derbyshire's Peak National Park.
- [d4s2] DSF also a processor and supplier of crushed and graded refractory raw materials for other applications such as coloured road-stone.
- [d4s3] By the 1960s, the business diversified into supplying other industries including steel, glass and cement.
- [d4s4] DSF was established in 1993 following the receivership of DSF Refractories Ltd and its parent company BH-F. British Hartford-Fairmont Ltd 'BH-F' had owned the company since 1987.
- [d4s5] They acquired DSF to support their business in the glass industry from West Group International 'WGI' who had as West Gas Improvement formed the company in 1892 as Derbyshire Silica Firebrick Ltd to support WGI's gas development business by the manufacture of refractories for use in the production of town gas.
- [d4s6] Nowadays the brickworks at Friden makes high-alumina refractory bricks and blocks which are exported worldwide for use by the heat containment industries, such as glass, cement, steel and petrochemical manufacturers.
- [d4s7] The company also supplies refractory minerals to other refractory manufacturers for use in the ceramics industries as well as in welding and road surface products.
- [d4s8] Despite the closure in the 1990s of the nearby silica pits which supplied raw materials, the company remains a major local employer.
- [d4s9] As at 2015, it employed approximately 115 people.

**d5: First Quantum Minerals**

- [d5s0] First Quantum Minerals Ltd. is a Canadian- based mining and metals company whose principal activities include mineral exploration, development and mining.
- [d5s1] Its main product is copper, which accounts for 80% of revenues as of 2016.
- [d5s2] First Quantum's common shares are listed for trading on the Toronto Stock Exchange in Canada( symbol" FM").
- [d5s3] Until 2016, First Quantum also maintained a secondary listing on the London Stock Exchange( symbol" FQM"), in the United Kingdom.

**d6: DAHER-SOCATA**

- [d6s0] DAHER- SOCATA( formerly SOCATA and EADS Socata) is a producer of general aviation aircraft propelled by piston engines and turboprops, including business planes, small personal or training aircraft, as well as the production of aircraft structures for other manufacturers such as Airbus, Dassault, Embraer, Eurocopter and Lockheed Martin.
- [d6s1] The company headquarters is currently located in Tarbes, France.
- [d6s2] In March 2015 the company name was again changed to just" Daher" as part of a rebranding to align the division with its parent company Daher.

**d7: Newhaven, Derbyshire**

- [d7s0] Newhaven is a hamlet in the county of Derbyshire, England, east of Hartington and west of Cromford.
- [d7s1] The principal employer in the area is DSF Refractories& Minerals Ltd.
- [d7s2] The hamlet is located within the Peak District National Park.

**d8: Lac Minerals Ltd v International Corona Resources Ltd**

- [d8s0] Lac Minerals Ltd v International Corona Resources Ltd is a leading Supreme Court of Canada decision on the nature of fiduciary and confidential relationships that can be created in the course of business, together with appropriate remedies for restitution when such relationships are breached.

**d9: Lubnowy**

- [d9s0] Lubnowy is part of the name of two villages, both located in Gmina Susz, within Iława County, Warmian- Masurian Voivodeship, Poland:

**d10: Radzice**

- [d10s0] Radzice is part of the name of two villages, both located in Gmina Drzewica, within Opoczno County, Łódź Voivodeship, Poland:

## 7. 2wikimultihopqa_6968dcf40bdc11eba7f7acde48001122

Question: When is Adele Khoury Graham's husband's birthday?

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | husband of Adele Khoury Graham | False | () |
| u2 | birthday of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | husband of Adele Khoury Graham | False | [] | Bob Graham | [['d7s1']] |
| u2 | date of birth of {u1} | True | ['u1'] | November 9, 1936 | [['d2s0']] |

### Source documents (reference only)

**d1: Theodred II (Bishop of Elmham)**

- [d1s0] Theodred II was a medieval Bishop of Elmham.
- [d1s1] The date of Theodred's consecration unknown, but the date of his death was sometime between 995 and 997.

**d2: Bob Graham**

- [d2s0] Daniel Robert Graham (born November 9, 1936) is an American politician and author who served as the 38th governor of Florida from 1979 to 1987 and a United States senator from Florida from 1987 to 2005.
- [d2s1] He is a member of the Democratic Party.
- [d2s2] Born in Coral Gables, Florida, Graham won election to the Florida Legislature after graduating from Harvard Law School.
- [d2s3] After serving in both houses of the Florida Legislature, Graham won the 1978 Florida gubernatorial election, and was reelected in 1982.
- [d2s4] In the 1986 Senate elections, Graham defeated incumbent Republican Senator Paula Hawkins.
- [d2s5] He helped found the Democratic Leadership Council and eventually became Chairman of the Senate Intelligence Committee.
- [d2s6] Graham ran for the 2004 Democratic presidential nomination, but dropped out before the first primaries.
- [d2s7] He declined to seek reelection in 2004 and retired from the Senate.
- [d2s8] Graham served as co-chair of the National Commission on the BP "Deepwater Horizon" Oil Spill and Offshore Drilling and as a member of the Financial Crisis Inquiry Commission and the CIA External Advisory Board.
- [d2s9] He works at the Bob Graham Center for Public Service at his undergraduate alma mater, the University of Florida.
- [d2s10] He also served as Chairman of the Commission on the Prevention of WMD proliferation and terrorism.
- [d2s11] Through the WMD policy center he advocates for the recommendations in the Commission's report, "World at Risk."
- [d2s12] In 2011, Graham published his first novel, the thriller "The Keys to the Kingdom".
- [d2s13] He has also written three nonfiction books: "
- [d2s14] Workdays: Finding Florida on the Job,Intelligence Matters", and "America: The Owner's Manual".

**d3: Pamela Jain**

- [d3s0] Pamela Jain is an Indian playback singer.
- [d3s1] Date of Birth:16th March.

**d4: Moffat Sinkala**

- [d4s0] Moffat Sinkala( date of birth unknown, died June 2004) was a Zambian footballer.
- [d4s1] He competed in the men's tournament at the 1980 Summer Olympics.

**d5: Etan Boritzer**

- [d5s0] Etan Boritzer( born 1950) is an American writer of children ’s literature who is best known for his book" What is God?" first published in 1989.
- [d5s1] His best selling" What is?" illustrated children's book series on character education and difficult subjects for children is a popular teaching guide for parents, teachers and child- life professionals.
- [d5s2] Boritzer gained national critical acclaim after" What is God?" was published in 1989 although the book has caused controversy from religious fundamentalists for its universalist views.
- [d5s3] The other current books in the" What is?" series include
- [d5s4] What is Love?,
- [d5s5] What is Death?,
- [d5s6] What is Beautiful?,
- [d5s7] What is Funny?,
- [d5s8] What is Right?,
- [d5s9] What is Peace?,
- [d5s10] What is Money?,
- [d5s11] What is Dreaming?,
- [d5s12] What is a Friend?,
- [d5s13] What is True?,
- [d5s14] What is a Family?,
- [d5s15] What is a Feeling?"
- [d5s16] The series is now also translated into 15 languages.
- [d5s17] Boritzer was first published in 1963 at the age of 13 when he wrote an essay in his English class at Wade Junior High School in the Bronx, New York on the assassination of John F. Kennedy.
- [d5s18] His essay was included in a special anthology by New York City public school children compiled and published by the New York City Department of Education.
- [d5s19] Boritzer now lives in Venice, California and maintains his publishing office there also.
- [d5s20] He has helped numerous other authors to get published through" How to Get Your Book Published!" programs.
- [d5s21] Boritzer is also a yoga teacher who teaches regular classes locally and guest- teaches nationally.
- [d5s22] He is also recognized nationally as an erudite speaker on" The Teachings of the Buddha."

**d6: Les Richards**

- [d6s0] Les Richards( date of birth unknown) was an Australian rules footballer who played with North Melbourne in the Victorian Football League( VFL).

**d7: Adele Khoury Graham**

- [d7s0] Adele Khoury Graham (born April 4, 1938) is an American educator and the former First Lady of Florida from 1979 to 1987.
- [d7s1] She is the wife of the 38th Governor of Florida and former United States Senator Bob Graham.
- [d7s2] Adele Graham was the First Lady of the state of Florida from 1979 to 1987.
- [d7s3] She spent her career as public school teacher in Massachusetts and Miami, Florida.
- [d7s4] In all, the Grahams have four children and 11 grandchildren.

**d8: Brian Saunders (weightlifter)**

- [d8s0] Brian Saunders( date of birth and death unknown) was a male weightlifter who competed for England.

**d9: Mark Kenneth Woods**

- [d9s0] Mark Kenneth Woods( date of birth unknown) is a Canadian comedy writer, actor, producer, director and TV host.

**d10: Terence Robinson**

- [d10s0] Terence D. Robinson( date of birth and death unknown) was a male wrestler who competed for England.

## 8. 2wikimultihopqa_6be60084088e11ebbd70ac1f6bf848b6

Question: Which film has the director born earlier, Two Can Play or The Faithful River (Film)?

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of Two Can Play | False | () |
| u2 | birth date of {u1} | False | ('u1',) |
| u3 | director of The Faithful River (Film) | False | () |
| u4 | birth date of {u3} | False | ('u3',) |
| u5 | which film's director was born earlier | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of Two Can Play | False | [] | Nat Ross | [['d3s0']] |
| u2 | date of birth of {u1} | False | ['u1'] | June 13, 1902 | [['d1s0']] |
| u3 | director of The Faithful River (film) | False | [] | Tadeusz Chmielewski | [['d10s0']] |
| u4 | date of birth of {u3} | False | ['u3'] | 7 June 1927 | [['d2s0']] |
| u5 | which of Two Can Play and The Faithful River has the director born earlier | True | ['u2', 'u4'] | Two Can Play | [[]] |

### Source documents (reference only)

**d1: Nat Ross**

- [d1s0] Nat Ross( June 13, 1902 – February 24, 1941) was an American film director and producer of the silent era.
- [d1s1] He directed 61 films between 1922 and 1931.
- [d1s2] He was born in San Francisco, California.
- [d1s3] He was shot dead in Los Angeles in 1941 by a disgruntled employee whom Ross had fired from the plant where Ross was working as foreman.
- [d1s4] He was the nephew of producer Carl Laemmle.

**d2: Tadeusz Chmielewski**

- [d2s0] Tadeusz Chmielewski (7 June 1927 – 4 December 2016) was a Polish film director, screenwriter and film producer, most notable for being one of the pioneers of popular Polish comedy.
- [d2s1] During World War II and until 1948, he was a soldier for the National Armed Forces and the Home Army.

**d3: Two Can Play**

- [d3s0] Two Can Play is a 1926 American silent drama film directed by Nat Ross and starring George Fawcett, Allan Forrest and Clara Bow.

**d4: Two Can Play That Game (film)**

- [d4s0] Two Can Play That Game is a 2001 romantic comedy film written and directed by Mark Brown and starring Vivica A. Fox and Morris Chestnut.

**d5: Fred Roy Krug**

- [d5s0] Fred R. Krug is an American film and television producer- director born in Bern, Switzerland.

**d6: Claude Weisz**

- [d6s0] Claude Weisz is a French film director born in Paris.

**d7: Three Can Play That Game**

- [d7s0] Three Can Play That Game is a 2007 romantic comedy film directed by Samad Davis and starring Jason George, Jazsmin Lewis, and Vivica A. Fox.
- [d7s1] It is a sequel to the 2001 film "Two Can Play That Game".

**d8: Jacques Décombe**

- [d8s0] Jacques Décombe is a French author, actor and director born in 1953.

**d9: Sepideh Farsi**

- [d9s0] Sepideh Farsi is an Iranian film director, born in Tehran in 1965.

**d10: The Faithful River (film)**

- [d10s0] The Faithful River is a Polish historical film directed by Tadeusz Chmielewski.
- [d10s1] It was produced in 1983 and released in 1987.

## 9. 2wikimultihopqa_75be1186086711ebbd5eac1f6bf848b6 【保留新拆法｜重标人工标签】

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_75be1186086711ebbd5eac1f6bf848b6"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。
>
> **处理建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。
>
> **证据定位：** d9s0, d1s0, d3s0, d4s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Are director of film Vivasaayi Magan and director of film When The Evening Bells Ring (1951 Film) both from the same country?

Type: comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of director of film Vivasaayi Magan | False | () |
| u2 | country of director of film When The Evening Bells Ring (1951 Film) | False | () |
| u3 | whether directors of Vivasaayi Magan and When The Evening Bells Ring (1951 Film) are from the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of Vivasaayi Magan | False | [] | Ramarajan | [['d9s0']] |
| u2 | nationality of {u1} | False | ['u1'] | Indian | [['d1s0']] |
| u3 | director of When the Evening Bells Ring (1951 film) | False | [] | Alfred Braun | [['d3s0']] |
| u4 | nationality of {u3} | False | ['u3'] | German | [['d4s0']] |
| u5 | whether the directors of Vivasaayi Magan and When the Evening Bells Ring (1951 film) are from the same country | True | ['u2', 'u4'] | no | [[]] |

### Source documents (reference only)

**d1: Ramarajan**

- [d1s0] Ramarajan is an Indian Tamil film Actor, Writer and Director who specialised in acting and directing films on village- based subjects.
- [d1s1] He is also known as" Makkal Nayagan".
- [d1s2] Many of his films were successful.
- [d1s3] He was called the rural box office emperor in the late 1980s.
- [d1s4] He is known for his colourful gaudy costumes and excessive makeup.
- [d1s5] His pairings with Rekha in Tamil cinema were his biggest hits.
- [d1s6] He has worked in more than 40 films and has directed more than 10 films.

**d2: When the Evening Bells Ring (1930 film)**

- [d2s0] When the Evening Bells Ring( German: Wenn die Abendglocken läuten) is a 1930 German silent drama film directed by Hanns Beck- Gaden and starring Josef Berger, Rosa Kirchner- Lang and Hanns Beck- Gaden.
- [d2s1] It is a heimatfilm set in Bavaria.

**d3: When the Evening Bells Ring (1951 film)**

- [d3s0] When the Evening Bells Ring is a 1951 West German drama film directed by Alfred Braun and starring Willy Birgel, Maria Holst and Paul Hörbiger.
- [d3s1] It is unrelated to the 1930 silent film of the same title.

**d4: Alfred Braun**

- [d4s0] Alfred Braun( 13 May 1888 – 3 January 1978) was a German screenwriter, actor and film director.

**d5: Ian Barry (director)**

- [d5s0] Ian Barry is an Australian director of film and TV.

**d6: Brian Johnson (special effects artist)**

- [d6s0] Brian Johnson( born 1939 or 1940) is a British designer and director of film and television special effects.

**d7: Ben Cura**

- [d7s0] Ben Cura( born 30 September 1988) is a British- Argentine actor and director of film, television and theatre.

**d8: Peter Levin**

- [d8s0] Peter Levin is an American director of film, television and theatre.

**d9: Vivasaayi Magan**

- [d9s0] Vivasaayi Magan is a 1997 Indian Tamil film, directed by Ramarajan and produced by Rani Azhakappan.
- [d9s1] The film stars Ramarajan, Devayani, K. R. Vijaya and Vadivelu in lead roles.
- [d9s2] The film had musical score by Sirpy.

**d10: Hanro Smitsman**

- [d10s0] Hanro Smitsman, born in 1967 in Breda( Netherlands), is a writer and director of film and television.

## 10. 2wikimultihopqa_7728ea720bb011ebab90acde48001122

Question: Who is Mariota, Countess Of Ross's father-in-law?

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | husband of Mariota, Countess Of Ross | False | () |
| u2 | father of {u1}, Mariota, Countess Of Ross's father-in-law | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | spouse of Mariota, Countess of Ross | False | [] | Domhnall of Islay, Lord of the Isles | [['d5s1']] |
| u2 | father of {u1}, Mariota's father-in-law | True | ['u1'] | John of Islay | [['d6s1']] |

### Source documents (reference only)

**d1: James Armour (Master mason)**

- [d1s0] James Armour (15 January 1730 – 20 September 1798) was a master mason and father of Jean Armour, and therefore the father-in-law of the poet Robert Burns.

**d2: Alexander Leslie, Earl of Ross**

- [d2s0] Alexander Leslie, Earl of Ross( died 1402) was a Scottish nobleman.
- [d2s1] Born between 1367 and 1382, he was the son of Walter Leslie, Lord of Ross and Euphemia I, Countess of Ross.
- [d2s2] In around 1394 he became Earl of Ross and sometime before 1398 he married Isabel Stewart, daughter of Robert Stewart, Duke of Albany.
- [d2s3] They had one child, Euphemia.
- [d2s4] He died at Dingwall, Scotland on 8 May 1402.

**d3: Ogawa Mataji**

- [d3s0] Viscount was a general in the early Imperial Japanese Army.
- [d3s1] He was also the father- in- law of Field Marshal Gen Sugiyama.

**d4: Ludwig von Westphalen**

- [d4s0] Johann Ludwig von Westphalen( 11 July 1770 – 3 March 1842) was a liberal Prussian civil servant and the father- in- law of Karl Marx.

**d5: Mariota, Countess of Ross**

- [d5s0] Mariota, Countess of Ross( Mairead, also called Mary and Margaret; died 1440) was the daughter of Euphemia I, Countess of Ross and her husband, the crusading war- hero Walter Leslie, Lord of Ross.
- [d5s1] Upon the death of her brother, Alexander Leslie, Earl of Ross, she became the heir- presumptive of her niece Euphemia II, Countess of Ross although her husband Domhnall of Islay, Lord of the Isles pressed Mariota's superior claim to the earldom.
- [d5s2] Domhnall attempted to gain control of the earldom, and sometime after 1405 but before 1411, Domhnall gained control of Dingwall Castle.
- [d5s3] In the year after the death of the nominal king Robert III of Scotland( 1406), in August 1407, Domhnall sent emissaries to England to the heir of the throne, the captive James Stewart.
- [d5s4] King Henry IV of England sent his own emissaries the following year to negotiate an alliance against Robert Stewart, Duke of Albany, the Guardian of Scotland who was controlling Euphemia and the earldom.
- [d5s5] With control over the principal seat of the earldom of Ross and support of the exiled heir to the Scottish throne, in 1411 Domhnall felt strong enough to march against Albany's main northern ally, Alexander Stewart, Earl of Mar.
- [d5s6] At the Battle of Harlaw Domhnall failed to inflict a decisive victory, and withdrew back to the western highlands.
- [d5s7] In the aftermath, Albany was able to retake Dingwall and seize control of Easter Ross.
- [d5s8] In 1415, Euphemia was persuaded by Albany to resign the earldom to his own second son, John Stewart, Earl of Buchan.
- [d5s9] This action was challenged by Domhnall of Islay, who continued to claim the earldom on behalf of Mariota.
- [d5s10] After the return of King James the latter destroyed the power of the Albany Stewarts, executing the Albany's son and successor Murdoch Stewart, Duke of Albany.
- [d5s11] Domhnall had died in 1423, but Mariota continued to enjoy the support of his successor and her own son, Alexander.
- [d5s12] Alexander took over her claims, and in 1437 her son was recognized as earl by the king.
- [d5s13] She died in 1440.
- [d5s14] She had two known children, Alexander and Mariota.

**d6: Donald of Islay, Lord of the Isles**

- [d6s0] Donald, Lord of the Isles
- [d6s1] (Gaelic: "Dómhnall"; died 1423), was the son and successor of John of Islay, Lord of the Isles and chief of Clan Donald.
- [d6s2] The Lordship of the Isles was based in and around the Scottish west-coast island of Islay, but under Donald's father had come to include many of the other islands off the west coast of Scotland, as well as Morvern, Garmoran, Lochaber, Kintyre and Knapdale on the mainland.
- [d6s3] Donald was the grandson of King Robert II of Scotland and first cousin of King Robert III; he took pride in his royal blood, even adopting the royal tressure to surround his coat of arms.
- [d6s4] While it is customary to portray the Lords of the Isles as divorced from the mainstream of Scottish political life, and as representatives of a brand of lordship distinct from the rest of Scotland, this view obscures the fact that Donald was only one of many magnates who held large lordships with little interference from the crown in late 14th and early 15th century Scotland.
- [d6s5] The Douglas kindred of southern Scotland and the Albany Stewarts had similar roles as Donald.

**d7: Barthold A. Butenschøn Sr.**

- [d7s0] Hans Barthold Andresen Butenschøn( 27 December 1877 – 28 November 1971) was a Norwegian businessperson.
- [d7s1] He was born in Kristiania as a son of Nils August Andresen Butenschøn and Hanna Butenschøn, and grandson of Nicolay Andresen.
- [d7s2] Together with Mabel Anette Plahte( 1877 – 1973, a daughter of Frithjof M. Plahte) he had the son Hans Barthold Andresen Butenschøn Jr. and was through him the father- in- law of Ragnhild Butenschøn and grandfather of Peter Butenschøn.
- [d7s3] Through his daughter Marie Claudine he was the father- in- law of Joakim Lehmkuhl, through his daughter Mabel Anette he was the father- in- law of Harald Astrup( a son of Sigurd Astrup) and through his daughter Nini Augusta he was the father- in- law of Ernst Torp.
- [d7s4] He took commerce school and agricultural school.
- [d7s5] He was hired in the family company N. A. Andresen& Co, and became a co-owner in 1910.
- [d7s6] He eventually became chief executive officer.
- [d7s7] The bank changed its name to Andresens Bank in 1913 and merged with Bergens Kreditbank in 1920.
- [d7s8] The merger was dissolved later in the 1920s.
- [d7s9] He was also a landowner, owning Nedre Skøyen farm and a lot of land in Enebakk.
- [d7s10] He chaired the board of Nydalens Compagnie from 1926, having not been a board member before that.
- [d7s11] He also chaired the supervisory council of Forsikringsselskapet Viking and Nedre Glommen salgsforening, and was a supervisory council member of Filharmonisk Selskap.
- [d7s12] He was a member of the gentlemen's club SK Fram since 1890, and was proclaimed a lifetime member in 1964.
- [d7s13] He was buried in Enebakk.

**d8: William III, Earl of Ross**

- [d8s0] William( or Uilleam) III, 5th Earl of Ross( d. 1372) was a fourteenth- century Scottish nobleman.
- [d8s1] He was the fifth O’ Beolan earl of Ross, descending from the founder of the line, Fearchar of Ross( or Fearchar MacTaggart).

**d9: John Adams (merchant)**

- [d9s0] John Adams( 1672 or 1673 – 1745) was an American- born Canadian merchant and member of the Nova Scotia Council.
- [d9s1] He was the father- in- law of Henry Newton( politician).

**d10: Peter Burroughs**

- [d10s0] Peter Burroughs( born 27 January 1947) is a British television and film actor, the director of Willow Management.
- [d10s1] He is the father- in- law of actor and TV presenter Warwick Davis.

## 11. 2wikimultihopqa_7b9cef6a0bdb11eba7f7acde48001122

Question: What is the cause of death of director of film The Magic Of Lassie?

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of film The Magic Of Lassie | False | () |
| u2 | cause of death of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film The Magic of Lassie | False | [] | Don Chaffey | [['d5s0']] |
| u2 | cause of death of {u1} | True | ['u1'] | heart failure | [['d1s2']] |

### Source documents (reference only)

**d1: Don Chaffey**

- [d1s0] Donald Chaffey (5 August 1917 – 13 November 1990) was a British film director, writer, producer, and art director.
- [d1s1] Chaffey's film career began as an art director in 1947, and his directorial debut was in 1953.
- [d1s2] He remained active in the industry until his death in 1990 from heart failure.
- [d1s3] His 1973 film "Charley One-Eye" was entered into the 24th Berlin International Film Festival
- [d1s4] He is chiefly known for his fantasy films, which include "Jason and the Argonauts" (1963), "The Three Lives of Thomasina" (1963), "One Million Years B.C." (1966), "The Viking Queen" (1967), "Creatures the World Forgot" (1971), "Pete's Dragon" (1977), and "C.H.O.M.P.S." (1979), his final feature film.
- [d1s5] Concurrent with his theatrically released films, Chaffey directed numerous British television series episodes, including several for "The PrisonerDanger Man", and "The Avengers".
- [d1s6] From the 1980s until his death, all of his work was in American made-for-TV movies, and in such TV series as "Fantasy IslandStingrayMacGyverVega$T. J. HookerMatt Houston" and "Charlie's Angels".

**d2: Josh Magette**

- [d2s0] Josh Magette( born November 28, 1989) is an American professional basketball player for the Orlando Magic of the National Basketball Association( NBA), on a two- way contract with the Lakeland Magic of the NBA G League.
- [d2s1] He played college basketball for the University of Alabama in Huntsville.

**d3: The Cutting Edge: The Magic of Movie Editing**

- [d3s0] The Cutting Edge: The Magic of Movie Editing is a 2004 documentary film directed by filmmaker Wendy Apple.
- [d3s1] The film is about the art of film editing.
- [d3s2] Clips are shown from many groundbreaking films with innovative editing styles.

**d4: Michael Sharrett**

- [d4s0] Stuart Michael Sharrett( born July 18, 1965) is an American actor.
- [d4s1] Best known for his role in the 1978 classic family movie" The Magic of Lassie" with James Stewart, Sharrett additionally co-starred in the 1985 action film" Savage Dawn" and in the 1986 Wes Craven horror film" Deadly Friend", for which he received a Young Artist Award nomination as the" Best Young Actor in a Horror Motion Picture".

**d5: The Magic of Lassie**

- [d5s0] The Magic of Lassie is a 1978 American family musical drama film directed by Don Chaffey, starring Lassie, James Stewart, Stephanie Zimbalist, Pernell Roberts, and Michael Sharrett, with cameo appearances by Mickey Rooney and Alice Faye (in her final film appearance).
- [d5s1] James Stewart is featured in one of only three musical film roles that he played
- [d5s2] : the first was "Born to Dance" (1936)
- [d5s3] in which he introduced the Cole Porter standard "Easy To Love" and the second was "Pot O' Gold" (1941).
- [d5s4] This was also his final onscreen appearance in a live-action film.
- [d5s5] The screenplay and song score are supplied by the prolific Sherman Brothers of "Mary Poppins" fame.
- [d5s6] Their song "
- [d5s7] When You're Loved" was nominated for an Academy Award for "Best Original Song" and was sung by Debby Boone.
- [d5s8] It is also the only musical film featuring Lassie.
- [d5s9] Released in the wake of "Star Wars", the film was panned as old-fashioned, and flopped at the box office.
- [d5s10] Critics expressed dismay at Stewart singing unmemorable songs as the grandfather.
- [d5s11] Following the film's failure, he semiretired from acting.

**d6: Ken Dancyger**

- [d6s0] Kennet Dancyger is a scriptwriting theoretician, film historian and expert on film editing and film production.
- [d6s1] He is professor of film and TV at Maurice Kanbar Institute of Film, Television,& New Media, Undergraduate.
- [d6s2] He has been the president of University Film and Video Association.
- [d6s3] He has taught film in the U.S. and Canada since 1968.
- [d6s4] His 2002 book contains a detailed comparison of screwball comedy and film noir.( p. 68) He has collaborated as historical consultant for the 2004 documentary" The Cutting Edge: The Magic of Movie Editing", about the art of film editing.

**d7: Courage of Lassie**

- [d7s0] Courage of Lassie is a 1946 Technicolor MGM feature film starring Elizabeth Taylor, Frank Morgan, and dog actor Pal in a story about a collie named Bill and his young companion, Kathie Merrick.
- [d7s1] When Bill is separated from Kathie following a vehicular accident, he is trained as a war dog, performs heroically, and, after many tribulations, is eventually reunited with his beloved Kathie.
- [d7s2] " Courage of Lassie" is the third of seven MGM films featuring a canine star called Lassie, based on Eric Knight's fictional character.
- [d7s3] Pal, a male Rough Collie, using the stage name Lassie, appeared as the title character in the first film," Lassie Come Home" and as Laddie in its sequel," Son of Lassie".
- [d7s4] Despite this film's title, the character Lassie does not appear in" Courage of Lassie"; Pal( credited as Lassie) portrays" Bill", also referred to as" Duke" for part of the movie.
- [d7s5] " Courage of Lassie" has been released to VHS and DVD.

**d8: Son of Lassie**

- [d8s0] Son of Lassie( also known as Laddie, Son of Lassie) is a 1945 Technicolor feature film produced by MGM based on characters created by Eric Knight, and starring Peter Lawford, Donald Crisp, June Lockhart and Pal( credited as Lassie).
- [d8s1] A sequel to" Lassie Come Home", the film focuses on the now adult Joe Carraclough after he joins the Royal Air Force during World War II and is shot down over Nazi-occupied Norway along with a stowaway, Lassie's son" Laddie" – played by Pal." Son of Lassie" was released theatrically on April 20, 1945, by Loew's.

**d9: Richard T. Jones**

- [d9s0] Richard Timothy Jones( born January 16, 1972) is an American actor.
- [d9s1] Jones is best known for his portrayals of Laveinio in the dramatic film" The Wood"( 1999) and Mike of the dramatic films" Why Did I Get Married?"( 2007) and" Why Did I Get Married Too?"( 2010).
- [d9s2] He is also well known for his role as Bruce Van Exel, court services officer on the CBS television series" Judging Amy" that aired from 1999 to 2005.

**d10: B. J. Johnson (basketball)**

- [d10s0] Robert" B. J." Johnson Jr.( born December 21, 1995) is an American professional basketball player for the Orlando Magic of the National Basketball Association( NBA), on a two- way contract with the Lakeland Magic of the NBA G League.
- [d10s1] He played college basketball for La Salle and Syracuse.

## 12. 2wikimultihopqa_874c55c20bda11eba7f7acde48001122

Question: What is the date of death of the director of film The Social Buccaneer (1916 Film)?

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of The Social Buccaneer (1916 Film) | False | () |
| u2 | date of death of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film The Social Buccaneer (1916 film) | False | [] | Jack Conway | [['d1s0']] |
| u2 | date of death of {u1} | True | ['u1'] | October 11, 1952 | [['d2s0']] |

### Source documents (reference only)

**d1: The Social Buccaneer (1916 film)**

- [d1s0] The Social Buccaneer is a 1916 American silent drama film directed by Jack Conway and starring J. Warren Kerrigan, Louise Lovely and Maude George.

**d2: Jack Conway (filmmaker)**

- [d2s0] Jack Ryan Conway (July 17, 1887 – October 11, 1952) was an American film director and film producer, as well as an actor of many films in the first half of the 20th century.

**d3: Peter Levin**

- [d3s0] Peter Levin is an American director of film, television and theatre.

**d4: Etan Boritzer**

- [d4s0] Etan Boritzer( born 1950) is an American writer of children ’s literature who is best known for his book" What is God?" first published in 1989.
- [d4s1] His best selling" What is?" illustrated children's book series on character education and difficult subjects for children is a popular teaching guide for parents, teachers and child- life professionals.
- [d4s2] Boritzer gained national critical acclaim after" What is God?" was published in 1989 although the book has caused controversy from religious fundamentalists for its universalist views.
- [d4s3] The other current books in the" What is?" series include
- [d4s4] What is Love?,
- [d4s5] What is Death?,
- [d4s6] What is Beautiful?,
- [d4s7] What is Funny?,
- [d4s8] What is Right?,
- [d4s9] What is Peace?,
- [d4s10] What is Money?,
- [d4s11] What is Dreaming?,
- [d4s12] What is a Friend?,
- [d4s13] What is True?,
- [d4s14] What is a Family?,
- [d4s15] What is a Feeling?"
- [d4s16] The series is now also translated into 15 languages.
- [d4s17] Boritzer was first published in 1963 at the age of 13 when he wrote an essay in his English class at Wade Junior High School in the Bronx, New York on the assassination of John F. Kennedy.
- [d4s18] His essay was included in a special anthology by New York City public school children compiled and published by the New York City Department of Education.
- [d4s19] Boritzer now lives in Venice, California and maintains his publishing office there also.
- [d4s20] He has helped numerous other authors to get published through" How to Get Your Book Published!" programs.
- [d4s21] Boritzer is also a yoga teacher who teaches regular classes locally and guest- teaches nationally.
- [d4s22] He is also recognized nationally as an erudite speaker on" The Teachings of the Buddha."

**d5: Ian Barry (director)**

- [d5s0] Ian Barry is an Australian director of film and TV.

**d6: Thomas Scott (diver)**

- [d6s0] Thomas Scott( 1907- date of death unknown) was an English diver.

**d7: Harry Wainwright (footballer)**

- [d7s0] Harry Wainwright( born 1899; date of death unknown) was an English footballer.

**d8: Bill Smith (footballer, born 1897)**

- [d8s0] William Thomas Smith( born 9 April 1897, date of death unknown) was an English professional footballer.

**d9: Albert Thompson (footballer, born 1912)**

- [d9s0] Albert Thompson( born 1912, date of death unknown) was a Welsh footballer.

**d10: Theodred II (Bishop of Elmham)**

- [d10s0] Theodred II was a medieval Bishop of Elmham.
- [d10s1] The date of Theodred's consecration unknown, but the date of his death was sometime between 995 and 997.

## 13. 2wikimultihopqa_8e463167086c11ebbd61ac1f6bf848b6

Question: Which film has the director who died later, The Purple Heart or How Mcdougall Topped The Score?

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of The Purple Heart | False | () |
| u2 | death date of {u1} | False | ('u1',) |
| u3 | director of How Mcdougall Topped The Score | False | () |
| u4 | death date of {u3} | False | ('u3',) |
| u5 | which film's director died later | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film The Purple Heart | False | [] | Lewis Milestone | [['d10s0']] |
| u2 | date of death of {u1} | False | ['u1'] | September 25, 1980 | [['d7s0']] |
| u3 | director of film How McDougall Topped the Score | False | [] | Victor Upton-Brown | [['d8s0']] |
| u4 | date of death of {u3} | False | ['u3'] | 23 May 1964 | [['d9s0']] |
| u5 | which of The Purple Heart and How McDougall Topped the Score has the director who died later | True | ['u2', 'u4'] | The Purple Heart | [[]] |

### Source documents (reference only)

**d1: Danny Dietz**

- [d1s0] Daniel Phillip Dietz Jr (January 26, 1980 – June 28, 2005) was a Navy SEAL who was awarded the U.S. Navy's second highest decoration, the Navy Cross, along with the Purple Heart, for his actions during the War in Afghanistan.

**d2: Don W. Sears**

- [d2s0] Don W. Sears was the eighth Dean and Professor Emeritus of Law at the University of Colorado Law School.
- [d2s1] Sears was also a two- time recipient of the Purple Heart and Bronze Star for his military service during World War II.

**d3: Tyler Ziegel**

- [d3s0] Tyler W." Ty" Ziegel( October 16, 1982 – December 26, 2012) was a United States Marine Corps sergeant who suffered severe burns during the Iraq War.
- [d3s1] He received the Purple Heart medal.

**d4: Joe Steffy**

- [d4s0] Joseph Benton" Joe" Steffy, Jr.( April 3, 1926 – May 22, 2011) was an American football player.
- [d4s1] He went to fight in the Korean War and received the Bronze Star Medal and the Purple Heart.
- [d4s2] Steffy was inducted into the College Football Hall of Fame.

**d5: Annie Fox (nurse)**

- [d5s0] Lt. Annie G. Fox( August 4, 1893 – January 20, 1987) was the first woman to receive the Purple Heart for combat.
- [d5s1] She served as the chief nurse in the Army Nurse Corps at Hickam Field during the Japanese attack on Pearl Harbor, on December 7, 1941.
- [d5s2] At that time the awarding of the Purple Heart did not require the service member to be injured.
- [d5s3] The requirements were changed after the attack of Pearl Harbor and Lt. Fox was awarded the Bronze Star because Fox was not wounded in the attack.

**d6: Needham Roberts**

- [d6s0] Needham Roberts( April 28, 1901 – April 18, 1949) was an American soldier in the Harlem Hellfighters and recipient of the Purple Heart and the Croix de Guerre for his valor during World War I.

**d7: Lewis Milestone**

- [d7s0] Lewis Milestone( born Leib Milstein; September 30, 1895 – September 25, 1980) was a Russian- born American motion picture director.
- [d7s1] He is known for directing" Two Arabian Knights"( 1927) and" All Quiet on the Western Front"( 1930), both of which received Academy Awards for Best Director.
- [d7s2] He also directed" The Front Page"( 1931 – nomination)," The General Died at Dawn"( 1936)," Of Mice and Men"( 1939)," Ocean's 11"( 1960), and received the directing credit for" Mutiny on the Bounty"( 1962), though Marlon Brando largely appropriated his responsibilities during its production.

**d8: How McDougall Topped the Score**

- [d8s0] How McDougall Topped the Score is a 1924 Australian silent film directed by Victor Upton-Brown.
- [d8s1] It is based on a famous poem by Thomas Edward Spencer about a cricket match won when a dog steals a ball, enabling the batting team to score plenty of runs.
- [d8s2] It is considered a lost film.

**d9: Victor Upton-Brown**

- [d9s0] Victor Upton-Brown (1 November 1880 – 23 May 1964) was an Australian rules football coach who coached University for a season while they were in the Victorian Football League (VFL).
- [d9s1] Upton-Brown coached University when Gerald Brosnan stepped aside for the 1913 season but couldn't steer the club to a single win from his 18 games in charge.
- [d9s2] When not coaching, Upton-Brown spent some time as a boundary and field umpire in the VFL.
- [d9s3] He was involved in the early Australian movie industry, writing and directing a movie based on the play 'How McDougall Topped the Score' which was released in 1924.
- [d9s4] He is also credited as having acted in the 1920 film: The Kelly Gang, which starred Godfrey Cass.
- [d9s5] He also taught at Wesley College in Melbourne and is credited as the lyricist of several school songs, including "Grey Towers".
- [d9s6] He was also the editor of the 1910 version of that school's songbook.
- [d9s7] He opened the South Yarra Cinema in the suburb of South Yarra, Melbourne, on 22 November 1915, where he lectured on movies.
- [d9s8] He was an occasional contributor to "The Argus" newspaper in Melbourne, Australia, during 1914 and 1915.

**d10: The Purple Heart**

- [d10s0] The Purple Heart is a 1944 American black- and- white war film, produced by Darryl F. Zanuck, directed by Lewis Milestone, and starring Dana Andrews, Richard Conte, Don" Red" Barry, Sam Levene and Trudy Marshall.
- [d10s1] Eighteen- year- old Farley Granger had a supporting role.
- [d10s2] The film is a dramatization of the" show trial" of a number of US airmen by the Japanese government during World War II.
- [d10s3] It is loosely based on the trial of eight US airmen who took part in the April 18, 1942, Doolittle Raid on Japan.
- [d10s4] Three were later executed and one died as a POW.
- [d10s5] This film was the first to deal directly with the Japanese treatment of POWs and ran into opposition from the US War Department, which was afraid that such films would provoke reprisals from the Japanese government.

## 14. 2wikimultihopqa_8ec76c0808db11ebbd9cac1f6bf848b6 【保留新拆法｜重标人工标签】

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_8ec76c0808db11ebbd9cac1f6bf848b6"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。
>
> **处理建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。
>
> **证据定位：** d7s0, d6s0, d10s4, d5s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Do both films: All The Winners and Mano Po 6: A Mother'S Love have the directors from the same country?

Type: comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of director of All The Winners | False | () |
| u2 | country of director of Mano Po 6: A Mother'S Love | False | () |
| u3 | whether both directors are from the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of All the Winners | False | [] | Geoffrey Malins | [['d7s0']] |
| u2 | nationality of {u1} | False | ['u1'] | British | [['d6s0']] |
| u3 | director of Mano Po 6: A Mother's Love | False | [] | Joel Lamangan | [['d10s4']] |
| u4 | nationality of {u3} | False | ['u3'] | Filipino | [['d5s0']] |
| u5 | whether the directors of All the Winners and Mano Po 6: A Mother's Love are from the same country | True | ['u2', 'u4'] | no | [[]] |

### Source documents (reference only)

**d1: Mano Po 5: Gua Ai Di**

- [d1s0] Mano Po 5: Gua Ai Di( also billed parenthetically as Mano Po 5: Gua Ai Di( I Love You)) is a 2006 Filipino film starring Filipino actors Angel Locsin as Charity and Richard Gutierrez as Nathan.
- [d1s1] Nathan is a veterinarian with playboy tendencies who falls in love with Charity, a Chinese Filipino who always follows tradition.
- [d1s2] In order to woo not only Charity but also her family, Nathan tries to follow and adapt Chinese culture, but with hilarious results.
- [d1s3] Unlike the other films in the series," Mano Po 5" is a romantic comedy- drama film.
- [d1s4] The film stars Lorna Tolentino, Angel Locsin and Richard Gutierrez, which already starred together in" Mano Po 2: My Home".
- [d1s5] Asia's Superstar and" Star In A Million" finalist Christian Bautista also appeared in his first film at the height of his successful musical career.

**d2: Mano Po III: My Love**

- [d2s0] Mano Po III: My Love is the third installment of the Mano Po anthology, following the success of" Mano Po" and" Mano Po 2: My Home".
- [d2s1] Produced by Regal Entertainment through MAQ Productions," Mano Po III" stars Vilma Santos in the leading role.

**d3: Ako Legal Wife**

- [d3s0] Mano Po 4: Ako Legal Wife is Regal Entertainment's entry for the 2005 Metro Manila Film Festival.
- [d3s1] The film focuses on the lives of the Chinese- Filipino community, but rather in a wackiest way unlike in the first 3 Mano Po installments which are used in a melodramatic way.
- [d3s2] It stars Jay Manalo, Zsa Zsa Padilla as Chona the Legal Wife, Cherry Pie Picache as Patty the Lucky Wife and Rufa Mae Quinto as Gloria the Latest Wife.
- [d3s3] The title is considered as the fourth installment of Mano Po and was based on the line of Zsa Zsa Padilla in the movie Mano Po 2: My Home," Ako Legal Wife!"
- [d3s4] Aside from the other Mano Po films this film is the first comedy from the series since three of the films in the beginning centered on perplex drama

**d4: Mano Po**

- [d4s0] Mano Po is Regal Entertainment's entry for the 2002 Metro Manila Film Festival.
- [d4s1] The film focuses on the lives of the Chinese Filipino community.
- [d4s2] " Mano Po" stars an all- star cast headed by Maricel Soriano, Richard Gomez, Kris Aquino and Ara Mina.
- [d4s3] Eddie Garcia and Boots Anson- Roa play the patriarch and matriarch of the Go clan respectively.
- [d4s4] The film won the most major awards in the film- awarding bodies, including 12 awards in the 28th Manila Film Festival in 2002.
- [d4s5] It was named Best Picture, Best Actor( for Eddie Garcia), Best Actress( for Ara Mina), Best Supporting Actress( for Kris Aquino) and Best Director( for Joel Lamangan).
- [d4s6] " Mano Po" was among the top- grossing films in time for the Metro Manila Filmfest.
- [d4s7] The film's success was followed by another episode," Mano Po 2: My Home" and a spin- off, that was released in 2007.

**d5: Joel Lamangan**

- [d5s0] Joel Lamangan( born September 21, 1952) is a Filipino film director, television director and actor.
- [d5s1] His award- winning films includes" The Flor Contemplacion StorySidhiDeathrowHubogAishte Imasu 1941 Blue Moon" and" Mano Po".
- [d5s2] On August 19, 2008, Lamangan directed his first indie movie" Walang Kawala" produced by DMV Entertainment.
- [d5s3] It stars Polo Ravales and Joseph Bitangcol, with the special participation of Jean Garcia.
- [d5s4] Joel also directs" Obra" and will soon start shooting Desperadas
- [d5s5] 2.
- [d5s6] He started production for the next Sine Novela:" Una Kang Naging Akin" starring Angelika dela Cruz, Wendell Ramos, and Maxene Magalona.
- [d5s7] In 2013 Elections he ran as congressman for Cavite's 1st District under the Lakas- CMD/ United Nationalist Alliance/ Partido Magdalo.
- [d5s8] However he backed out in the race.
- [d5s9] In 2013, Lamangan was named as the artistic director of Gantimpala Theater Foundation.
- [d5s10] Lamangan will direct an original musical titled" Katipunan: Mga Anak ng Bayan" and it will star actors Sandino Martin and Anna Fegi.
- [d5s11] The show toured in August and September 2013 around provinces of Manila to celebrate the 150th anniversary of the birth of Philippine hero, Andres Bonifacio.
- [d5s12] Lamangan is a member of the international Order of DeMolay from Baja Chapter, Cavite City.
- [d5s13] He was conferred with the highest honor being a DeMolay to the rank of Legion of Honor last November 14, 2015, by the Grand Master Victor Antonio T. Espejo of the Supreme Council Order of DeMolay Philippines for outstanding leadership in his field of endeavor, for service to humanity, for success in fraternal life, including adult service to the Order of DeMolay.
- [d5s14] The Supreme Council Order of DeMolay is an appendant body of Freemasonry.

**d6: Geoffrey Malins**

- [d6s0] Arthur" Geoffrey" Herbert Malins( 18 November 1886 – 1940) was a British film director most famous for camera and editing work on the 1916 war film" The Battle of the Somme", which combined documentary and propaganda, and reached an audience of over 20 million viewers.

**d7: All the Winners**

- [d7s0] All the Winners is a 1920 British silent sports film directed by Geoffrey Malins and starring Owen Nares, Maudie Dunham and Sam Livesey.
- [d7s1] It is set in the horse racing world.
- [d7s2] It was made at Isleworth Studios.

**d8: Mano Po 7: Tsinoy**

- [d8s0] Mano Po 7: Chinoy is a Filipino film starring Richard Yap, Jean Garcia and Enchong Dee.
- [d8s1] The film is the 7th installment of the Mano Po franchise from Regal Entertainment.
- [d8s2] It tells the story of a modern Chinese Filipino family.
- [d8s3] Beneath the facade of a typical well- off Chinese Filipino family, it also tackles the struggles of family life as well as how they managed to reunite themselves as one.
- [d8s4] The film was shown in theatres starting December 14, 2016.
- [d8s5] But was delayed due to insistent public demand that film was re-run in theatres starting February 8, 2017.
- [d8s6] The film starred Richard Yap making him the first male main protagonist in the entire Mano Po film series.
- [d8s7] It was also the second Mano Po movie that was not directed by Joel Lamangan who directed" Mano PoMano
- [d8s8] Po 4: Ako Legal Wife" and.

**d9: Mano Po 2: My Home**

- [d9s0] Mano
- [d9s1] Po 2: My Home is the second installment of the Mano Po franchise, after Mano Po( 2002).
- [d9s2] Produced by Regal Entertainment, Mano Po 2 stars Susan Roces in the leading role.
- [d9s3] This was also the first Mano Po movie that was not directed by Joel Lamangan, director of the first movie; rather it was directed by Erik Matti.
- [d9s4] It was one of the official entries in the 2003 Metro Manila Film Festival which garnered 5 awards alongside Filipinas.

**d10: Mano Po 6: A Mother's Love**

- [d10s0] Mano
- [d10s1] Po 6: A Mother's Love is the sixth installment in the Mano Po film franchise, following in 2006.
- [d10s2] Produced by Regal Entertainment," Mano Po 6" marks the first appearance of Sharon Cuneta in a Regal movie.
- [d10s3] Co- starring with Sharon are: Zsa Zsa Padilla( in her third Mano Po role), Christopher De Leon, Boots Anson- Roa( fourth appearance in the Mano Po series), Kris Aquino( in her third Mano Po role), Dennis Trillo( in another Mano Po appearance, last seen in), former ABS- CBN talent and GMA actress Heart Evangelista, and Ciara Sotto.
- [d10s4] Joel Lamangan, who had last worked with Sharon in Walang Kapalit, was at the helm, in his fifth Mano Po directorial job.
- [d10s5] The movie which was a 2009 Metro Manila Film Festival entry had its theater run from 25 December 2009 to January 2010.

## 15. 2wikimultihopqa_971f9d7a0bd911eba7f7acde48001122

Question: When was the director of film The Big Bang (1989 Film) born?

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of The Big Bang (1989 Film) | False | () |
| u2 | birth date of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film The Big Bang (1989 film) | False | [] | James Toback | [['d5s0']] |
| u2 | date of birth of {u1} | True | ['u1'] | November 23, 1944 | [['d4s0']] |

### Source documents (reference only)

**d1: Ian Barry (director)**

- [d1s0] Ian Barry is an Australian director of film and TV.

**d2: Kevin Sussman**

- [d2s0] Kevin Sussman( born December 4, 1970) is an American actor and comedian.
- [d2s1] He played Walter on the ABC comedy- drama" Ugly Betty" and Stuart Bloom on the CBS sitcom" The Big Bang Theory".
- [d2s2] Starting with the sixth season of" The Big Bang Theory", he was promoted to a series regular.

**d3: Ralph Asher Alpher**

- [d3s0] Ralph Asher Alpher( February 3, 1921 – August 12, 2007) was an American cosmologist, who carried out pioneering work in the early 1950s on the Big Bang model, including Big Bang nucleosynthesis and predictions of the cosmic microwave background radiation.

**d4: James Toback**

- [d4s0] James Toback (born November 23, 1944) is an American screenwriter and film director.
- [d4s1] He was nominated for the Academy Award for Best Original Screenplay in 1991 for "Bugsy".
- [d4s2] He has directed films including "The Pick-up ArtistTwo Girls and a Guy" and "Black and White".
- [d4s3] On October 22, 2017, the "Los Angeles Times" reported that 38 women have accused Toback of sexual harassment or assault.
- [d4s4] Since the article was published, 357 additional women contacted "Los Angeles Times" and said that Toback had sexually harassed them.
- [d4s5] The accounts stretch over a 40-year period.
- [d4s6] Toback has denied all the allegations.

**d5: The Big Bang (1989 film)**

- [d5s0] The Big Bang is a 1989 documentary film, directed by Academy Award- nominated screenwriter James Toback.
- [d5s1] The film addresses questions about life and existence.
- [d5s2] It was released to theaters May 11, 1990, and aired on PBS on August 6, 1991.

**d6: Etan Boritzer**

- [d6s0] Etan Boritzer( born 1950) is an American writer of children ’s literature who is best known for his book" What is God?" first published in 1989.
- [d6s1] His best selling" What is?" illustrated children's book series on character education and difficult subjects for children is a popular teaching guide for parents, teachers and child- life professionals.
- [d6s2] Boritzer gained national critical acclaim after" What is God?" was published in 1989 although the book has caused controversy from religious fundamentalists for its universalist views.
- [d6s3] The other current books in the" What is?" series include
- [d6s4] What is Love?,
- [d6s5] What is Death?,
- [d6s6] What is Beautiful?,
- [d6s7] What is Funny?,
- [d6s8] What is Right?,
- [d6s9] What is Peace?,
- [d6s10] What is Money?,
- [d6s11] What is Dreaming?,
- [d6s12] What is a Friend?,
- [d6s13] What is True?,
- [d6s14] What is a Family?,
- [d6s15] What is a Feeling?"
- [d6s16] The series is now also translated into 15 languages.
- [d6s17] Boritzer was first published in 1963 at the age of 13 when he wrote an essay in his English class at Wade Junior High School in the Bronx, New York on the assassination of John F. Kennedy.
- [d6s18] His essay was included in a special anthology by New York City public school children compiled and published by the New York City Department of Education.
- [d6s19] Boritzer now lives in Venice, California and maintains his publishing office there also.
- [d6s20] He has helped numerous other authors to get published through" How to Get Your Book Published!" programs.
- [d6s21] Boritzer is also a yoga teacher who teaches regular classes locally and guest- teaches nationally.
- [d6s22] He is also recognized nationally as an erudite speaker on" The Teachings of the Buddha."

**d7: Eric Lerner**

- [d7s0] Eric J. Lerner( born May 31, 1947) is an American popular science writer, and independent plasma researcher.
- [d7s1] He wrote the 1991 book" The Big Bang Never Happened", which advocates Hannes Alfvén's plasma cosmology instead of the Big Bang theory.
- [d7s2] He is founder, president, and chief scientist of Lawrenceville Plasma Physics, Inc.

**d8: Theodred II (Bishop of Elmham)**

- [d8s0] Theodred II was a medieval Bishop of Elmham.
- [d8s1] The date of Theodred's consecration unknown, but the date of his death was sometime between 995 and 997.

**d9: Brian Saunders (weightlifter)**

- [d9s0] Brian Saunders( date of birth and death unknown) was a male weightlifter who competed for England.

**d10: Terence Robinson**

- [d10s0] Terence D. Robinson( date of birth and death unknown) was a male wrestler who competed for England.

## 16. 2wikimultihopqa_9eb9f3480baf11ebab90acde48001122

Question: Who is the paternal grandfather of Princess Jeguk?

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Princess Jeguk | False | () |
| u2 | father of {u1}, Princess Jeguk's paternal grandfather | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Princess Jeguk | False | [] | Kublai Khan | [['d9s2']] |
| u2 | father of {u1}, Princess Jeguk's paternal grandfather | True | ['u1'] | Tolui | [['d4s3']] |

### Source documents (reference only)

**d1: Abd al-Muttalib**

- [d1s0] Abd al- Muttalib Shaybah ibn Hashim( c. 497 – 578) was the grandfather of Islamic prophet Muhammad.

**d2: Fred Le Deux**

- [d2s0] Frederick" Fred" Le Deux( born 4 December 1934) was an Australian rules footballer who played with Geelong in the Victorian Football League( VFL).
- [d2s1] He is the grandfather of Tom Hawkins.

**d3: John Westley**

- [d3s0] Rev. John Westley( 1636 – 78) was an English nonconformist minister.
- [d3s1] He was the grandfather of John Wesley( founder of Methodism).

**d4: Kublai Khan**

- [d4s0] Kublai  was the fifth Khagan (Great Khan) of the Mongol Empire ("Ikh Mongol Uls"), reigning from 1260 to 1294
- [d4s1] (although after the division of the empire this was a nominal position).
- [d4s2] He also founded the Yuan dynasty in China as a conquest dynasty in 1271, and ruled as the first Yuan emperor until his death in 1294.
- [d4s3] Kublai was the fourth son of Tolui (his second son with Sorghaghtani Beki) and a grandson of Genghis Khan.
- [d4s4] He succeeded his older brother Möngke as Khagan in 1260, but had to defeat his younger brother Ariq Böke in the Toluid Civil War lasting until 1264.
- [d4s5] This episode marked the beginning of disunity in the empire.
- [d4s6] Kublai's real power was limited to China and Mongolia, though as Khagan he still had influence in the Ilkhanate and, to a significantly lesser degree, in the Golden Horde.
- [d4s7] If one counts the Mongol Empire at that time as a whole, his realm reached from the Pacific Ocean to the Black Sea, from Siberia to what is now Afghanistan.
- [d4s8] In 1271, Kublai established the Yuan dynasty, which ruled over present-day Mongolia, China, Korea, and some adjacent areas, and assumed the role of Emperor of China.
- [d4s9] By 1279, the Mongol conquest of the Song dynasty was completed and Kublai became the first non-Han emperor to conquer all of China.
- [d4s10] The imperial portrait of Kublai was part of an album of the portraits of Yuan emperors and empresses, now in the collection of the National Palace Museum in Taipei.
- [d4s11] White, the color of the royal costume of Kublai, was the imperial color of the Yuan dynasty.

**d5: Lyon Cohen**

- [d5s0] Lyon Cohen( 1868–1937) was a Polish- born Canadian businessman and a philanthropist.
- [d5s1] He was the grandfather of singer/ poet Leonard Cohen.

**d6: Henry Krause**

- [d6s0] Henry J." Red" Krause, Jr.( August 28, 1913 – February 20, 1987) was an American football offensive lineman in the National Football League for the Brooklyn Dodgers and the Washington Redskins.
- [d6s1] He played college football at St. Louis University.
- [d6s2] He is the grandfather of Jennifer Krause
- [d6s3] He is the great grandfather of Payton Hoeing

**d7: Kaya Alp**

- [d7s0] Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

**d8: John Mackay (poet)**

- [d8s0] John Mackay( 1656–1754), known as( The Blind Piper), was a Scottish Gaelic poet and composer, and the grandfather of William Ross.

**d9: Princess Jeguk**

- [d9s0] "Daejang"-Princess Jeguk (28 June 1259 – 21 May 1297, "Princess-Aunt of the State of Je") or Empress Inmyeong was queen consort to king Chungnyeol of Goryeo and the mother of king Chungseon of Goryeo.
- [d9s1] She was the first Mongol queen of Korea, having gone to Goryeo from the Yuan dynasty.
- [d9s2] Her father was Kublai Khan.
- [d9s3] Princesses qualified as  were aunts of the emperor.
- [d9s4] She was the aunt of Temür Khan, who later succeeded her father as the Yuan emperor.

**d10: Zhao Shoushan**

- [d10s0] Zhao Shoushan( 12 November 1894 – 20 June 1965) was a KMT general and later Chinese Communist Party politician.
- [d10s1] He is the grandfather of Zhao Leji.

## 17. 2wikimultihopqa_b200fa00097e11ebbdb0ac1f6bf848b6

Question: Which film was released earlier, It'S Kind Of A Funny Story (Film) or The Education Of Nicky?

Type: comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | release year of It'S Kind Of A Funny Story (Film) | False | () |
| u2 | release year of The Education Of Nicky | False | () |
| u3 | which film was released earlier | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | release year of It's Kind of a Funny Story | False | [] | 2010 | [['d5s0'], ['d5s2'], ['d8s1']] |
| u2 | release year of The Education of Nicky | False | [] | 1921 | [['d4s0']] |
| u3 | which of It's Kind of a Funny Story and The Education of Nicky was released earlier | True | ['u1', 'u2'] | The Education of Nicky | [[]] |

### Source documents (reference only)

**d1: A Cinderella Story: Christmas Wish**

- [d1s0] A Cinderella Story: Christmas
- [d1s1] Wish is a 2019 American teen comedy musical film written and directed by Michelle Johnston and starring Laura Marano and Gregg Sulkin.
- [d1s2] It is the fifth installment of" A Cinderella Story" film series.
- [d1s3] The film was released digitally on October 15, 2019, and DVD on October 29, 2019.

**d2: The Education of Fairies**

- [d2s0] The Education of Fairies  is a 2006 international co-production drama film directed by José Luis Cuerda.

**d3: Hum Hai Raahi Car Ke**

- [d3s0] Hum Hai Raahi
- [d3s1] Car
- [d3s2] Ke is a comedy misadventure love story film directed by Jyotin Goel, that was released in India on 24 May 2013.

**d4: The Education of Nicky**

- [d4s0] The Education of Nicky is a 1921 British silent romance film directed by Arthur Rooke and starring James Knight, Marjorie Villis and Constance Worth.
- [d4s1] It was based on a novel by May Wynn.

**d5: It's Kind of a Funny Story (film)**

- [d5s0] It's Kind of a Funny Story is a 2010 American comedy- drama film written and directed by Anna Boden and Ryan Fleck, an adaptation of Ned Vizzini's 2006 novel of the same name.
- [d5s1] The film stars Keir Gilchrist, Zach Galifianakis, Emma Roberts, and Viola Davis.
- [d5s2] It was released in the United States on October 8, 2010, and received mixed to positive reviews.

**d6: The Wonderful World of Captain Kuhio**

- [d6s0] The film was released in Japan on 10 October 2009.

**d7: Hate Story**

- [d7s0] Hate Story is a 2012 Indian Hindi- language erotic thriller film directed by Vivek Agnihotri and produced by Vikram Bhatt.
- [d7s1] It stars Nikhil Dwivedi, Gulshan Devaiya and Paoli Dam in lead roles and the film was released on 20 April 2012.
- [d7s2] The first installment in the" Hate Story" film series the film was a commercial and critical success.
- [d7s3] The premise of the film chronicles a woman and her struggle to fight against the man that betrayed her.

**d8: Keir Gilchrist**

- [d8s0] Keir David Peters Gilchrist( born 28 September 1992) is an English- born Canadian actor.
- [d8s1] Gilchrist is known for playing Marshall Gregson on Showtime's original series" United States of Tara", Craig Gilner in the 2010 comedy- drama film" It's Kind of a Funny Story", Paul in" It Follows", and Sam Gardner in the Netflix original series" Atypical".

**d9: The Education of Sonny Carson**

- [d9s0] The Education of Sonny Carson is a 1974 film based on the best- selling autobiography of Sonny Carson.

**d10: Hate Story 3**

- [d10s0] Hate Story 3 is a 2015 Indian Hindi- language Bollywood erotic thriller film directed by Vishal Pandya.
- [d10s1] Produced by T- Series, it stars Sharman Joshi, Karan Singh Grover, Zareen Khan and Daisy Shah in lead roles, and Priyanshu Chatterjee in a pivotal role.
- [d10s2] Written by Vikram Bhatt and Madhuri Banerji, the film is part of the" Hate Story" film series.
- [d10s3] The film was released on 4 December 2015.
- [d10s4] The film was a box office success.

## 18. 2wikimultihopqa_ba5637db098c11ebbdb0ac1f6bf848b6

Question: Are Nahr-E Shahab and Bazm, Fars located in the same country?

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of Nahr-E Shahab | False | () |
| u2 | country of Bazm, Fars | False | () |
| u3 | whether Nahr-E Shahab and Bazm, Fars are located in the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country where Nahr-e Shahab is located | False | [] | Iran | [['d8s0']] |
| u2 | country where Bazm, Fars is located | False | [] | Iran | [['d10s0']] |
| u3 | whether Nahr-e Shahab and Bazm, Fars are located in the same country | True | ['u1', 'u2'] | yes | [[]] |

### Source documents (reference only)

**d1: Language Management**

- [d1s0] Language management is a discipline that consists of satisfying the needs of people who speak multiple different languages.
- [d1s1] These may be in the same country, in companies, and in cultural or international institutions where one must use multiple languages.

**d2: 2001–02 UEFA Champions League second group stage**

- [d2s0] Eight winners and eight runners- up from the first group stage were drawn into four groups of four teams, each containing two group winners and two runners- up.
- [d2s1] Teams from the same country or from the same first round group could not be drawn together.
- [d2s2] The top two teams in each group advanced to the quarter- finals.

**d3: 1971 Copa Libertadores**

- [d3s0] The Copa Libertadores 1971 was the 12th edition of the Copa Libertadores, CONMEBOL's annual international club tournament.
- [d3s1] Nacional won the competition.
- [d3s2] The participating teams were divided into five groups, in which teams of the same country were placed in the same group.
- [d3s3] Each country was represented by two teams.
- [d3s4] The countries were paired as follows:

**d4: 1992 Copa Libertadores**

- [d4s0] The 1992 Copa Libertadores was the 33rd edition of the Copa Libertadores, CONMEBOL's annual international club tournament.
- [d4s1] São Paulo won the competition.
- [d4s2] The participating teams were divided into five groups, in which teams of the same country were placed in the same group.
- [d4s3] Each country was represented by two teams.
- [d4s4] The countries were paired as follows:

**d5: Telephone numbers in Ascension Island**

- [d5s0] Country Code:+ 247< br> International Call Prefix: 00 Ascension Island does not share the same country code( +290) with the rest of St Helena.

**d6: 1993 Copa Libertadores**

- [d6s0] The Copa Libertadores 1993 was the 34th edition of the Copa Libertadores, CONMEBOL's annual international club tournament.
- [d6s1] São Paulo won the competition.
- [d6s2] The participating teams were divided into five groups, in which teams of the same country were placed in the same group.
- [d6s3] Each country was represented by two teams.
- [d6s4] The countries were paired as follows:

**d7: Zelzal**

- [d7s0] Zelzal( meaning" Earthquake") is a series of artillery rockets developed by Iran.
- [d7s1] The series consists of:
- [d7s2] These rockets were developed by SAHID Hassan Tehrani Moghaddam, after developed the Shahab- 1 and the Shahab- 2.

**d8: Nahr-e Shahab**

- [d8s0] Nahr -e Shahab( also Romanized as Nahr -e Shahāb; also known as Shahāb) is a village in Buzi Rural District, in the Central District of Shadegan County, Khuzestan Province, Iran.
- [d8s1] At the 2006 census, its existence was noted, but its population was not reported.

**d9: Satellite tournament**

- [d9s0] A satellite tournament is either a minor tournament or event on a competitive sporting tour or one of a group of such tournaments that form a series played in the same country or region.

**d10: Bazm, Fars**

- [d10s0] Bazm( also known as Bāz) is a village in Sarvestan Rural District, in the Central District of Bavanat County, Fars Province, Iran.
- [d10s1] At the 2006 census, its population was 422, in 111 families.

## 19. 2wikimultihopqa_bc7761cc088511ebbd6dac1f6bf848b6 【保留新拆法｜重标人工标签】

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_bc7761cc088511ebbd6dac1f6bf848b6"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。
>
> **处理建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。
>
> **证据定位：** d8s0, d3s0, d1s0, d10s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Do both films, Joe Somebody and Figures of the Night, have the directors who are from the same country?

Type: comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of director of Joe Somebody | False | () |
| u2 | country of director of Figures of the Night | False | () |
| u3 | whether the directors of Joe Somebody and Figures of the Night are from the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of Joe Somebody | False | [] | John Pasquin | [['d8s0']] |
| u2 | nationality of {u1} | False | ['u1'] | American | [['d3s0']] |
| u3 | director of Figures of the Night | False | [] | Richard Oswald | [['d1s0']] |
| u4 | nationality of {u3} | False | ['u3'] | Austrian | [['d10s0']] |
| u5 | whether the directors of Joe Somebody and Figures of the Night are from the same country | True | ['u2', 'u4'] | no | [[]] |

### Source documents (reference only)

**d1: Figures of the Night**

- [d1s0] Figures of the Night( German:Nachtgestalten) is a 1920 German silent horror film written, directed and produced by Richard Oswald and starring Paul Wegener, Conrad Veidt, Reinhold Schünzel and Erna Morena.
- [d1s1] It is based on the novel" Eleagabal Kuperus" by Karl Hans Strobl.
- [d1s2] Strobl was the editor of a German horror fiction magazine called" Der Orchideengarten" which was said to have been influenced by the works of Edgar Allan Poe.
- [d1s3] Strobl was an anti-Semitic and later willingly joined the Nazi Party, which may explain why he has become an obscure literary figure today.
- [d1s4] The film's art direction was by Hans Dreier, and Carl Hoffmann handled the cinematography.
- [d1s5] Hoffmann went on to collaborate with such noted German directors as Fritz Lang and F.W. Murnau.
- [d1s6] It was filmed at the Babelsberg Studio in Berlin.

**d2: The Night and You**

- [d2s0] The Night and You( Spanish: La Noche y tú) is a 1946 Mexican film.
- [d2s1] It was directed by Chano Urueta.

**d3: John Pasquin**

- [d3s0] John Pasquin( born November 30, 1944) is an American director of film, television and theatre.

**d4: You and the Night and the Music (Helen Merrill album)**

- [d4s0] You and The Night and The Music is a 1998 studio album by Helen Merrill.

**d5: After the Night and the Music**

- [d5s0] After the Night and the Music is a one- act play in three parts, written by Elaine May.
- [d5s1] It opened in 2005.
- [d5s2] May derived the name of the play from the Howard Dietz song" You and the Night and the Music".

**d6: Matt Corboy**

- [d6s0] Matt Corboy( born June 4, 1973) is an American actor.
- [d6s1] He has appeared in both films and television series.

**d7: Night and Day**

- [d7s0] Night and Day may refer to:

**d8: Joe Somebody**

- [d8s0] Joe Somebody is a 2001 American comedy-drama film written by John Scott Shepherd and directed by John Pasquin.
- [d8s1] The film stars Tim Allen as an ordinary man forced into violence by a workplace bully.
- [d8s2] The film also stars Julie Bowen, Kelly Lynch, Greg Germann, Hayden Panettiere, Patrick Warburton and Jim Belushi.
- [d8s3] Screenwriter John Scott Shepherd wrote the script based on his experiences working in advertising.
- [d8s4] Though originally offered to Jim Carrey, the role of Joe Scheffer would eventually be taken by Allen.
- [d8s5] The film marked Allen and Pasquin's third feature together, after 1994's "The Santa Clause" and 1997's "Jungle 2 Jungle".
- [d8s6] The entire film was shot over a nearly eight-week span in Minnesota.
- [d8s7] The film was released in the U.S. on December 21, 2001, to negative reviews.
- [d8s8] Produced on a $38 million budget, the film ended its theatrical run with $24.5 million worldwide, making it a financial failure.
- [d8s9] The film received one award nomination, which went to young Panettiere's performance as the title character's daughter.

**d9: Francis Gouldman**

- [d9s0] Francis Gouldman(" c." 1607–1688/89) was a Church of England clergyman and lexicographer whose Latin- English dictionary( 1664) went through several editions.
- [d9s1] Gouldman was also one of the directors who oversaw the publication of the monumental" Critici sacri", a major collection of Biblical criticism.

**d10: Richard Oswald**

- [d10s0] Richard Oswald (5 November 1880 – 11 September 1963) was an Austrian director, producer, and screenwriter.

## 20. 2wikimultihopqa_bf1ebaa80bda11eba7f7acde48001122

Question: What is the date of death of Lord Frederick Spencer Hamilton's mother?

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | mother of Lord Frederick Spencer Hamilton | False | () |
| u2 | date of death of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | mother of Lord Frederick Spencer Hamilton | False | [] | Lady Louisa Jane Russell | [['d7s0']] |
| u2 | date of death of {u1} | True | ['u1'] | 31 March 1905 | [['d5s0']] |

### Source documents (reference only)

**d1: Etan Boritzer**

- [d1s0] Etan Boritzer( born 1950) is an American writer of children ’s literature who is best known for his book" What is God?" first published in 1989.
- [d1s1] His best selling" What is?" illustrated children's book series on character education and difficult subjects for children is a popular teaching guide for parents, teachers and child- life professionals.
- [d1s2] Boritzer gained national critical acclaim after" What is God?" was published in 1989 although the book has caused controversy from religious fundamentalists for its universalist views.
- [d1s3] The other current books in the" What is?" series include
- [d1s4] What is Love?,
- [d1s5] What is Death?,
- [d1s6] What is Beautiful?,
- [d1s7] What is Funny?,
- [d1s8] What is Right?,
- [d1s9] What is Peace?,
- [d1s10] What is Money?,
- [d1s11] What is Dreaming?,
- [d1s12] What is a Friend?,
- [d1s13] What is True?,
- [d1s14] What is a Family?,
- [d1s15] What is a Feeling?"
- [d1s16] The series is now also translated into 15 languages.
- [d1s17] Boritzer was first published in 1963 at the age of 13 when he wrote an essay in his English class at Wade Junior High School in the Bronx, New York on the assassination of John F. Kennedy.
- [d1s18] His essay was included in a special anthology by New York City public school children compiled and published by the New York City Department of Education.
- [d1s19] Boritzer now lives in Venice, California and maintains his publishing office there also.
- [d1s20] He has helped numerous other authors to get published through" How to Get Your Book Published!" programs.
- [d1s21] Boritzer is also a yoga teacher who teaches regular classes locally and guest- teaches nationally.
- [d1s22] He is also recognized nationally as an erudite speaker on" The Teachings of the Buddha."

**d2: Sophie Winkleman**

- [d2s0] Sophie Lara Winkleman (born 5 August 1980) is an English actress.
- [d2s1] She is the wife of Lord Frederick Windsor, son of Queen Elizabeth II's first cousin Prince Michael of Kent, and as such is also known as Lady Frederick Windsor.

**d3: Thomas Scott (diver)**

- [d3s0] Thomas Scott( 1907- date of death unknown) was an English diver.

**d4: Lord Frederick Cavendish-Bentinck**

- [d4s0] Major-General Lord Frederick Cavendish-Bentinck (2 November 1781 – 10 February 1828) known as Lord Frederick Bentinck was a British soldier and politician.
- [d4s1] The youngest child and fourth son of William Cavendish-Bentinck, 3rd Duke of Portland and Lady Dorothy Cavendish, Cavendish-Bentinck attended Westminster School before joining the army.

**d5: Louisa Hamilton, Duchess of Abercorn**

- [d5s0] Louisa Jane Hamilton, Duchess of Abercorn, VA( née Lady Louisa Jane Russell)( 8 July 1812 – 31 March 1905) was a member of the British aristocracy.
- [d5s1] She was the sister of Prime Minister John Russell, 1st Earl Russell, and among her descendants are two British princesses( Diana and Sarah) and Prince Richard, Duke of Gloucester.

**d6: Frederick Robb**

- [d6s0] Major- General Sir Frederick Spencer Wilson Robb,( 8 October 1858 – 8 February 1948) was a senior British Army officer who went on to be Military Secretary.

**d7: Lord Frederick Spencer Hamilton**

- [d7s0] Lord Frederick Spencer Hamilton (13 October 1856 – 11 August 1928) was a Conservative Party politician in the United Kingdom, the sixth son of James Hamilton, 1st Duke of Abercorn and Lady Louisa Jane Russell.
- [d7s1] He was Second Secretary of the Diplomatic Service (1877–1884) and Member of Parliament (MP) for Manchester South West (1885–1886) and North Tyrone (1892–1895).
- [d7s2] Lord Frederick also wrote the books "
- [d7s3] Here, There and
- [d7s4] EverywhereThe Days Before Yesterday" and "Vanished Pomps of Yesterday" which was first published in 1920 by Hodder and Stoughton Ltd, London.
- [d7s5] These give vivid accounts of his life in the diplomatic service.
- [d7s6] While serving as aide-de-camp to Lord Lansdowne, then Governor-General of Canada, in Ottawa, Lord Frederick was the first person to introduce skiing to Canada.
- [d7s7] From 1896 to 1900, he was editor of the Pall Mall Magazine.
- [d7s8] He never married and died without children.

**d8: Lord Frederick Paulet**

- [d8s0] Lieutenant General Lord Frederick Paulet,( 12 May 1810 – 1 January 1871) was a senior British Army officer.

**d9: Bill Smith (footballer, born 1897)**

- [d9s0] William Thomas Smith( born 9 April 1897, date of death unknown) was an English professional footballer.

**d10: Theodred II (Bishop of Elmham)**

- [d10s0] Theodred II was a medieval Bishop of Elmham.
- [d10s1] The date of Theodred's consecration unknown, but the date of his death was sometime between 995 and 997.

## 21. 2wikimultihopqa_d690e9a809bc11ebbdb0ac1f6bf848b6

Question: Are both high schools, Warwick Valley High School and Yoncalla High School, located in the same country?

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country where Warwick Valley High School is located | False | () |
| u2 | country where Yoncalla High School is located | False | () |
| u3 | whether both high schools are located in the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country where Warwick Valley High School is located | False | [] | United States | [['d3s0']] |
| u2 | country where Yoncalla High School is located | False | [] | United States | [['d5s0']] |
| u3 | whether Warwick Valley High School and Yoncalla High School are located in the same country | True | ['u1', 'u2'] | yes | [[]] |

### Source documents (reference only)

**d1: North Valley High School**

- [d1s0] North Valley High School is a public high school located in Grants Pass, Oregon, United States.

**d2: Calloway County High School**

- [d2s0] Calloway County
- [d2s1] High School is a public high school located in Murray, Kentucky.
- [d2s2] The school was formed from the consolidation of six high schools from across the county: Hazel High School, Lynn Grove High School, Kirksey High School, Almo High School, New Concord High School, and Faxon High School.

**d3: Warwick Valley High School**

- [d3s0] Warwick Valley High School( WVHS) is located on Sanfordville Road outside the Village of Warwick, New York, United States.
- [d3s1] It educates students in grades 9 through 12 in the Warwick Valley Central School District, which covers most of the village and town of Warwick, including the hamlet of Pine Island.
- [d3s2] Students in those portions of the town near the village of Florida and the village of Greenwood Lake attend other high schools.
- [d3s3] A referendum to send students from the latter community to WVHS failed in 2007.

**d4: Metea Valley High School**

- [d4s0] Metea Valley High School is a high school in Aurora, Illinois that opened in August 2009 in DuPage County.
- [d4s1] The school is one of four high schools operated by the Indian Prairie School District.
- [d4s2] The others in Aurora are Waubonsie Valley High School and Indian Plains, while Neuqua Valley High School is in Naperville.

**d5: Yoncalla High School**

- [d5s0] Yoncalla High School is a public high school in Yoncalla, Oregon, United States.

**d6: Sioux Valley High School**

- [d6s0] Sioux Valley High School is a high school located in Volga, South Dakota, USA.

**d7: Midland High School (Midland, Michigan)**

- [d7s0] Midland High School is a three- story public high school located in Midland, Michigan.
- [d7s1] It is the older of two high schools in the Midland Public Schools district, and a member of the Saginaw Valley High School Association.

**d8: River Valley High School (Michigan)**

- [d8s0] River Valley High School is the high school for the River Valley School District located in Three Oaks, Michigan, United States.
- [d8s1] River Valley High School houses grades 6-12.

**d9: Eagle Valley High School**

- [d9s0] Eagle Valley High School( EVHS) is a high school located in Gypsum, Colorado.

**d10: Tippecanoe Valley High School**

- [d10s0] Tippecanoe Valley High School is a high school located in Akron, Indiana.
- [d10s1] Home of the Vikings.

## 22. 2wikimultihopqa_d996cdce0baf11ebab90acde48001122 【保留新拆法｜重标人工标签】

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_d996cdce0baf11ebab90acde48001122"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 旧 gold 经配偶再找女儿，既多绕一步，也不能仅凭配偶的孩子就断定父子关系。完整上下文 d4s1 已直接说 Swanandi 是 Uday 的女儿。
>
> **处理建议：** 保留 single：child of Uday Tikekar。用 d4s0/d4s1 的直接亲子关系重标支持集合，删除 spouse 依赖；不是删除已有父女事实。
>
> **证据定位：** d4s0, d4s1, d6s2, d1s4；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Who is the child of Uday Tikekar?

Type: single · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | child of Uday Tikekar | True | () |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | spouse of Uday Tikekar | False | [] | Arati Ankalikar-Tikekar | [['d6s2']] |
| u2 | child of Uday Tikekar, given {u1} as his spouse | True | ['u1'] | Swanandi Tikekar | [['d1s4'], ['d4s1']] |

### Source documents (reference only)

**d1: Arati Ankalikar-Tikekar**

- [d1s0] Arati Ankalikar-Tikekar (born January 27, 1963 in Vijayapura, Karnataka) is a two-time National Award-winning Indian classical singer who is active mostly in Marathi, Konkani and Hindi film Industry; known for high-pitch singing and style, earned in Agra as well as Gwalior and Jaipur.
- [d1s1] Arati has been credited by audio cassettes and CD recordings.
- [d1s2] She was the main playback singer for the Sham Benegal's film, "Sardari Begum".
- [d1s3] She is known for her albums "Tejomay NadbrahmRaag-Rang", and, playback for the movies "AntarnaadDe dhakkaSavlee", and the hit "Sardari BegumEk Hazarachi Note".
- [d1s4] Her daughter Swanandi Tikekar who is in her mid-twenties dabbles in acting as well.

**d2: Chakrabongse Bhuvanath**

- [d2s0] Field Marshal Chakrabongse Bhuvanath, the Prince of Bishnulok( 3 March 1883 – 13 June 1920), was the 40th child of King Chulalongkorn and the fourth child of Queen Sri Bajarindra.

**d3: Prince Hodong of Goguryeo**

- [d3s0] Hodong is a child of Daemusin of Goguryeo who was the third king of Goguryeo.

**d4: Swanandi Tikekar**

- [d4s0] Swanandi Tikekar(born 13 November) in a Marathi actress.
- [d4s1] She is daughter of Uday Tikekar and Aarti Ankalikar.
- [d4s2] She pursued a masters in law from ILS College.
- [d4s3] She is well known for her role as Minal in Dil Dosti Duniyadari and Mukta in Dil Dosti Dobara.
- [d4s4] She was also seen in the plays "Ek Shoonya Teen" and "Don't Worry Be Happy."

**d5: Ingegerd Birgersdotter of Bjelbo**

- [d5s0] Ingegerd( or" Ingegärd")
- [d5s1] Birgersdotter of Bjelbo( or" Bjälbo"; ca.
- [d5s2] 1180 – 7 April after 1210, possibly 1230) was a Swedish Queen Consort, second spouse of King Sverker II of Sweden.
- [d5s3] Ingegerd was born into one of Sweden's most powerful noble families, the Bjälbo family, as the child of the powerful Jarl Birger Brosa and the Queen Dowager Brigida Haraldsdotter; her mother was the child of King Harald Gille of Norway and had, in her first marriage, herself been the Queen of Sweden in 1160 – 1161.

**d6: Uday Tikekar**

- [d6s0] Uday Tikekar( Marathi: उदय टिकेकर) is an Indian film and television actor.
- [d6s1] He began his career in Marathi theatre, also putting up performances in Hindi theatre.
- [d6s2] He is married to classical singer Arati Ankalikar- Tikekar, who is a 2- time National Film Award winner.

**d7: U. R. Lalit**

- [d7s0] U. R. Lalit is a senior counsel practising at Supreme Court of India and a former additional judge of the Delhi High Court.
- [d7s1] He is father of Uday U. Lalit, judge of Supreme Court of India.

**d8: Princess Hyomyeong**

- [d8s0] Princess Hyomyeong/ Hyo-Myung( 1637- 1700), was the child of King Injo, the sixteenth king of the Joseon dynasty in Korea, and his Consort, Lady Gwi- in Jo.
- [d8s1] She was the only daughter of King Injo.

**d9: Benito di Paula**

- [d9s0] Benito di Paula, stage name of Uday Velloso( born 28 November 1941), is a Brazilian singer- songwriter and pianist.

**d10: Latif Yahia**

- [d10s0] Latif Yahia(" Laṭīf Yaḥīa"; born 14 June 1964) is an Iraqi- born author and former combatant in the Iran – Iraq War.
- [d10s1] Two journalists have disputed this and other claims made by Yahia.
- [d10s2] He is best known for being the alleged former body double of Uday Hussein, the son of Iraqi dictator Saddam Hussein.

## 23. 2wikimultihopqa_e5f6937a0bae11ebab90acde48001122

Question: Who is the maternal grandfather of Tiberius Gemellus?

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | mother of Tiberius Gemellus | False | () |
| u2 | father of {u1}, Tiberius Gemellus's maternal grandfather | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | mother of Tiberius Gemellus | False | [] | Livilla | [['d10s3']] |
| u2 | father of {u1}, Tiberius Gemellus's maternal grandfather | True | ['u1'] | Nero Claudius Drusus | [['d4s0']] |

### Source documents (reference only)

**d1: Kaya Alp**

- [d1s0] Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

**d2: John Westley**

- [d2s0] Rev. John Westley( 1636 – 78) was an English nonconformist minister.
- [d2s1] He was the grandfather of John Wesley( founder of Methodism).

**d3: Abd al-Muttalib**

- [d3s0] Abd al- Muttalib Shaybah ibn Hashim( c. 497 – 578) was the grandfather of Islamic prophet Muhammad.

**d4: Livilla**

- [d4s0] Claudia Livia Julia (Classical Latin: ; c. 13 BC – AD 31) was the only daughter of Nero Claudius Drusus and Antonia Minor and sister of the Roman Emperor Claudius and general Germanicus, and thus the paternal aunt of the emperor Caligula and maternal great-aunt of emperor Nero, as well as the niece and daughter-in-law of Tiberius.
- [d4s1] She was named after her grandmother, Augustus' wife Livia Drusilla, and commonly known by her family nickname Livilla ("little Livia").
- [d4s2] She was born after Germanicus and before Claudius.
- [d4s3] She was twice married to the potential successor in the Julio-Claudian dynasty, first to Augustus' grandson Gaius Caesar
- [d4s4] (died 4 AD) and later to Tiberius' son Drusus the Younger (died AD 23).
- [d4s5] Allegedly, she helped her lover Sejanus in poisoning her second husband and died shortly after Sejanus fell from power in AD 31.

**d5: Zhao Shoushan**

- [d5s0] Zhao Shoushan( 12 November 1894 – 20 June 1965) was a KMT general and later Chinese Communist Party politician.
- [d5s1] He is the grandfather of Zhao Leji.

**d6: Henry Krause**

- [d6s0] Henry J." Red" Krause, Jr.( August 28, 1913 – February 20, 1987) was an American football offensive lineman in the National Football League for the Brooklyn Dodgers and the Washington Redskins.
- [d6s1] He played college football at St. Louis University.
- [d6s2] He is the grandfather of Jennifer Krause
- [d6s3] He is the great grandfather of Payton Hoeing

**d7: Fred Le Deux**

- [d7s0] Frederick" Fred" Le Deux( born 4 December 1934) was an Australian rules footballer who played with Geelong in the Victorian Football League( VFL).
- [d7s1] He is the grandfather of Tom Hawkins.

**d8: Lyon Cohen**

- [d8s0] Lyon Cohen( 1868–1937) was a Polish- born Canadian businessman and a philanthropist.
- [d8s1] He was the grandfather of singer/ poet Leonard Cohen.

**d9: John Mackay (poet)**

- [d9s0] John Mackay( 1656–1754), known as( The Blind Piper), was a Scottish Gaelic poet and composer, and the grandfather of William Ross.

**d10: Tiberius Gemellus**

- [d10s0] Tiberius Julius Caesar Nero Gemellus, known as Tiberius Gemellus (Latin: "
- [d10s1] Tiberius Caesar Drusus filius
- [d10s2] Tiberius Augustus nepos divus
- [d10s3] Augustus pronepos"; 10 October AD 19–37/38) was the son of Drusus and Livilla, the grandson of the Emperor Tiberius, and the second cousin of the Emperor Caligula.
- [d10s4] "
- [d10s5] Gemellus" is a nickname meaning "the twin".
- [d10s6] His twin brother, Tiberius Claudius Caesar Germanicus II Gemellus, died while still an infant in 23.
- [d10s7] His father and older cousins died, and are suspected by contemporary sources as having been systematically eliminated by the powerful praetorian prefect Sejanus.
- [d10s8] Their removal allowed Gemellus and Caligula to be named joint-heirs by Tiberius in 35, a decision that ultimately resulted in Caligula assuming power and having Gemellus killed, or by forcing him to kill himself, in late 37 or early 38.

## 24. 2wikimultihopqa_e95cb5fc085d11ebbd5cac1f6bf848b6

Question: Which film whose director was born first, Zanjeer (1973 Film) or The Legend Of Lylah Clare?

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of Zanjeer (1973 Film) | False | () |
| u2 | birth date of {u1} | False | ('u1',) |
| u3 | director of The Legend Of Lylah Clare | False | () |
| u4 | birth date of {u3} | False | ('u3',) |
| u5 | which film's director was born first | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of Zanjeer (1973 film) | False | [] | Prakash Mehra | [['d8s0']] |
| u2 | date of birth of {u1} | False | ['u1'] | 13 July 1939 | [['d1s0']] |
| u3 | director of The Legend of Lylah Clare | False | [] | Robert Aldrich | [['d6s0']] |
| u4 | date of birth of {u3} | False | ['u3'] | August 9, 1918 | [['d5s0']] |
| u5 | which of Zanjeer (1973 film) and The Legend of Lylah Clare has the director born first | True | ['u2', 'u4'] | The Legend of Lylah Clare | [[]] |

### Source documents (reference only)

**d1: Prakash Mehra**

- [d1s0] Prakash Mehra( 13 July 1939 – 17 May 2009) was an Indian film director and producer known for his blockbuster Hindi films.
- [d1s1] He was one of the pioneers of masala films, along with Nasir Hussain, and Manmohan Desai.
- [d1s2] His collaborations with the actor Amitabh Bachchan resulted in several box office blockbusters and classics, due to which Mehra was considered among the' Golden Directors' of his time.

**d2: Henry Moore (cricketer)**

- [d2s0] Henry Walter Moore( 1849 – 20 August 1916) was an English- born first- class cricketer who spent most of his life in New Zealand.

**d3: The Legend of the Silver Fir**

- [d3s0] The Legend of the Silver Fir is a 1973 Czechoslovak film directed by František Vláčil.

**d4: Wale Adebanwi**

- [d4s0] Wale Adebanwi( born 1969) is a Nigerian- born first Black Rhodes Professor at St Antony's College, Oxford.

**d5: Robert Aldrich**

- [d5s0] Robert Burgess Aldrich( August 9, 1918 – December 5, 1983) was an American film director, producer, and screenwriter.
- [d5s1] His notable credits include" Vera Cruz"( 1954)," Kiss Me Deadly"( 1955)," The Big Knife"( 1955)," Autumn Leaves"( 1956)," Attack"( 1956)," What Ever Happened to Baby Jane?"( 1962)," Hush ... Hush, Sweet Charlotte"( 1964)," The Flight of the Phoenix"( 1965)," The Dirty Dozen"( 1967) and" The Longest Yard"( 1974).
- [d5s2] Aldrich was portrayed by Alfred Molina in the television miniseries" Feud"( 2017).

**d6: The Legend of Lylah Clare**

- [d6s0] The Legend of Lylah Clare is a 1968 American drama film released by Metro- Goldwyn- Mayer and directed by Robert Aldrich.
- [d6s1] The film stars Peter Finch, Kim Novak( in multiple roles), Ernest Borgnine, Michael Murphy, and Valentina Cortese.
- [d6s2] The film was based on a 1962" DuPont Show of the Week" TV drama co-written by" Wild in the Streets" creator Robert Thom.
- [d6s3] A satire on Hollywood, full of references to similar films, it recounts how an untalented beginner is hired to play the legendary Lylah Clare, a tempestuous actress who died mysteriously 20 years ago, and is herself consumed by the system.
- [d6s4] Although Aldrich's previous 1960s efforts were praised by critics," Lylah Clare" opened to negative reviews.

**d7: The Legend of Frank Woods**

- [d7s0] The Legend of Frank Woods is a 1977 western film.
- [d7s1] " The Legend of Frank Woods" is a re-edited version a 1972 film entitled" To Hell You Preach".

**d8: Zanjeer (1973 film)**

- [d8s0] Zanjeer is a 1973 Indian Hindi- language action film written by Salim- Javed( mostly by Salim Khan, with assistance from Javed Akhtar), directed and produced by Prakash Mehra, and starring Amitabh Bachchan, Jaya Bachchan, Pran, Ajit and Bindu.
- [d8s1] The film changed Hindi cinema's trend from romance films to action films, and pioneered Bachchan's new image of a brooding but explosive person who fights back when cornered, known as" The Angry Young Man."
- [d8s2] The film started a new wave in Bollywood.
- [d8s3] At a time when India was suffering from corruption and low economic growth, and the common man was left with frustration and anger over the system," Zanjeer" began shifting Hindi cinema in a violent and aggressive direction.
- [d8s4] Reflecting the anger of the masses, Amitabh Bachchan was seen as the new hero, who had the courage to fight against the wrongs while maintaining moral values at the same time.
- [d8s5] This film also ended the struggling period for Bachchan, and turned him into a rising star.
- [d8s6] The film was a blockbuster success, domestically in India and overseas in the Soviet Union.
- [d8s7] It was the first of many collaborations between screenwriter duo Salim- Javed and Amitabh Bachchan.
- [d8s8] Ever since" Zanjeer", Salim- Javed wrote many of their subsequent scripts with Bachchan in mind for the lead role, and insisted on him being cast for their later films, including blockbusters such as" Deewaar"( 1975) and" Sholay"( 1975), establishing Bachchan as a superstar.
- [d8s9] In addition to being a turning point for Bachchan's career and Hindi cinema," Zanjeer" was also a turning point for South Indian cinema, with Bachchan's acting inspiring future Tamil Superstar Rajinikanth.
- [d8s10] " Zanjeer" remains an important film in the history of Indian cinema and is regarded as a classic today.

**d9: The Legend of the Boy and the Eagle**

- [d9s0] The Legend of the Boy and the Eagle is a 1967 American live- action Walt Disney film.

**d10: The Legend of Ero of Armenteira**

- [d10s0] The legend of Saint Ero of Armenteira.
- [d10s1] The romanic monastery of Armenteira has always been related to the legend of its founder, the abbot Ero.

## 25. 2wikimultihopqa_ea8045620bdb11eba7f7acde48001122

Question: What nationality is the director of film Lorai: Play To Live?

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of film Lorai: Play To Live | False | () |
| u2 | nationality of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Lorai: Play to Live | False | [] | Parambrata Chatterjee | [['d2s0']] |
| u2 | nationality of {u1} | True | ['u1'] | Indian | [['d5s0']] |

### Source documents (reference only)

**d1: Peter Levin**

- [d1s0] Peter Levin is an American director of film, television and theatre.

**d2: Lorai: Play to Live**

- [d2s0] Lorai: Play to Live is an Indian Bengali sports drama film directed by Parambrata Chatterjee, which stars Prosenjit Chatterjee, Payel Sarkar and Indrasish Roy in lead roles.
- [d2s1] The film is produced by Shyam Sunder Dey under the "Greentouch Entertainment".
- [d2s2] The film was released on 9 January 2015.

**d3: Brian Kennedy (gallery director)**

- [d3s0] Brian Patrick Kennedy( born 5 November 1961) is an Irish- born art museum director who has worked in Ireland and Australia, and now lives and works in the United States.
- [d3s1] He is currently the director of the Peabody Essex Museum.
- [d3s2] He was the director of the Toledo Museum of Art in Ohio from 2010 to 2019.
- [d3s3] He was the director of the Hood Museum of Art from 2005 to 2010, and the National Gallery of Australia( Canberra) from 1997- 2004.

**d4: John Farrell (businessman)**

- [d4s0] John Farrell is the director of YouTube in Latin America.

**d5: Parambrata Chatterjee**

- [d5s0] Parambrata Chattopadhyay (born 27 June 1980) is an Indian film actor, director, producer, and television personality.
- [d5s1] He has a significant following in West Bengal, India.
- [d5s2] Parambrata started his career with Bengali television and films.
- [d5s3] He made his Hindi debut in Kahaani (2012), starring along with Vidya Balan and Nawazuddin Siddiqui.
- [d5s4] He also acted in "Bhalo Theko" (2003), which is Vidya Balan's debut film.
- [d5s5] He has a very good knowledge of world music and has sung for few Bengali films like Chaya Manush and Samantaral.

**d6: Dana Blankstein**

- [d6s0] Dana Blankstein- Cohen( born March 3, 1981) is the director of the Israeli Academy of Film and Television.
- [d6s1] She is a film director, and an Israeli culture entrepreneur.

**d7: Ian Barry (director)**

- [d7s0] Ian Barry is an Australian director of film and TV.

**d8: Michael Govan**

- [d8s0] Michael Govan( born 1963) is the director of the Los Angeles County Museum of Art since 2006.
- [d8s1] Prior to this, Govan worked as the director of the Dia Art Foundation in New York City.

**d9: John Donatich**

- [d9s0] John Donatich is the Director of Yale University Press.

**d10: Olav Aaraas**

- [d10s0] Olav Aaraas( born 10 July 1950) is a Norwegian historian and museum director.
- [d10s1] He was born in Fredrikstad.
- [d10s2] From 1982 to 1993 he was the director of Sogn Folk Museum, from 1993 to 2010 he was the director of Maihaugen and from 2001 he has been the director of the Norwegian Museum of Cultural History.
- [d10s3] In 2010 he was decorated with the Royal Norwegian Order of St. Olav.

## 26. 2wikimultihopqa_f48d9c60093011ebbdaeac1f6bf848b6 【待确认：语义或标签口径】

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_f48d9c60093011ebbdaeac1f6bf848b6"></a>

> **审阅结论：待确认：语义或标签口径**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新单元询问 release year，旧 u2 标注的是 U.S. theatrical release date（2016-11-04）。首映、国家上映及年份/日期的口径不同，不能原样复制。
>
> **处理建议：** 保留新 release year 形式。人工需要确认发行口径：美国院线上映、世界首次发行还是文档年份；按确认口径把目标规范为年份，不能直接复制旧完整日期或擅自把美国上映年当全球首映年。
>
> **证据定位：** d2s0, d10s1；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Which film was released first, Upasane or Emilio (Film)?

Type: comparison · fallback: False · SFT snapshots: 7

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | release year of Upasane | False | () |
| u2 | release year of Emilio (Film) | False | () |
| u3 | which film was released first | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | release date of Upasane | False | [] | 1974 | [['d2s0']] |
| u2 | U.S. theatrical release date of Emilio | False | [] | November 4, 2016 | [['d10s1']] |
| u3 | which of Upasane and Emilio was released first | True | ['u1', 'u2'] | Upasane | [[]] |

### Source documents (reference only)

**d1: Bommalattam (2008 film)**

- [d1s0] Bommalattam is a 2008 Indian Tamil film directed by Bharathiraja starring Arjun Sarja and Nana Patekar in the lead roles.
- [d1s1] Originally filmed in Hindi under the title" Cinema", the film was released first in Tamil.
- [d1s2] Hindi version retitled" Final Cut of Director" had a limited release in 2016.
- [d1s3] This marked Nana Patekar's Tamil film debut.

**d2: Upasane**

- [d2s0] Upasane( English: Worship) is a 1974 Kannada musical drama film, directed by Puttanna Kanagal.
- [d2s1] The film produced by Rashi brothers, is based on the novel of the same name, written by Devaki Murthy.
- [d2s2] The film mostly had women playing the lead roles, consisting of Aarathi, Leelavathi, M. N. Lakshmi Devi, G. V. Sharadha and Advani Lakshmi Devi. Dr. Govinda Mannur, K. S. Ashwath and Seetharam played the male supporting roles.
- [d2s3] Actor Seetharam was colloquially named as" Upasane" Seetharam for the rest of his career after the release of this film.
- [d2s4] The film dealt with the plight of Sharadha( Aarathi) who intends to pursue her career in classical music.
- [d2s5] The film went on to win multiple high- profile awards at the Karnataka State Film Awards for the year 1974- 75 including Best Film, Best Screenplay and Best Cinematography.
- [d2s6] Aarathi, who played the protagonist at the age of 19, won the Filmfare Best Actress award.

**d3: Lloyd (film)**

- [d3s0] Lloyd is a 2001 American comedy film.
- [d3s1] The film was released on May 4, 2001.

**d4: Single Video Theory**

- [d4s0] Single Video Theory is a music documentary directed by Mark Pellington that follows the making of "Yield", the fifth album by the American alternative rock band Pearl Jam.
- [d4s1] It was released first on VHS on August 4, 1998, and then on DVD on November 24, 1998.

**d5: Coney Island Baby (film)**

- [d5s0] Coney Island Baby is a 2003 comedy- drama in which film producer Amy Hobby made her directorial debut.
- [d5s1] Karl Geary wrote the film and Tanya Ryno was the film's producer.
- [d5s2] The music was composed by Ryan Shore.
- [d5s3] The film was shot in Sligo, Ireland, which is known locally as" Coney Island".
- [d5s4] The film was screened at the Newport International Film Festival.
- [d5s5] Hobby won the Jury Award for" Best First Time Director".
- [d5s6] The film made its premiere television broadcast on the Sundance Channel.

**d6: Empties**

- [d6s0] Empties is a 2007 film directed by Jan Svěrák and written by his father Zdeněk Svěrák, who also stars in the film.
- [d6s1] It was released first in the Czech Republic in March 2007.
- [d6s2] The film is a comedy from the same team which made Kolya.

**d7: Rakka (film)**

- [d7s0] The film was released on YouTube and Steam on 14 June 2017.

**d8: Invasion of the Neptune Men**

- [d8s0] The film was released in 1961 in Japan and was later released in the United States on television.
- [d8s1] In 1998, the film was featured on an episode of" Mystery Science Theater 3000".

**d9: The Wonderful World of Captain Kuhio**

- [d9s0] The film was released in Japan on 10 October 2009.

**d10: Emilio (film)**

- [d10s0] Emilio is a 2008 American drama film written and directed by Kim Jorgensen, starring Walter Perez, Danny Martinez, Alejandro Patino, Wendell Wright, Jesse Garcia, and Ryan McTavish.
- [d10s1] It was released theatrically in the U.S. on November 4, 2016.

## 27. 2wikimultihopqa_f5972e880baf11ebab90acde48001122

Question: Who is Erzsébet Thurzó's paternal grandfather?

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Erzsébet Thurzó | False | () |
| u2 | father of {u1}, Erzsébet Thurzó's paternal grandfather | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Erzsébet Thurzó | False | [] | Imre Thurzó | [['d10s0']] |
| u2 | father of {u1}, Erzsébet Thurzó's paternal grandfather | True | ['u1'] | György Thurzó | [['d8s0']] |

### Source documents (reference only)

**d1: John Westley**

- [d1s0] Rev. John Westley( 1636 – 78) was an English nonconformist minister.
- [d1s1] He was the grandfather of John Wesley( founder of Methodism).

**d2: Kaya Alp**

- [d2s0] Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

**d3: Lyon Cohen**

- [d3s0] Lyon Cohen( 1868–1937) was a Polish- born Canadian businessman and a philanthropist.
- [d3s1] He was the grandfather of singer/ poet Leonard Cohen.

**d4: Fred Le Deux**

- [d4s0] Frederick" Fred" Le Deux( born 4 December 1934) was an Australian rules footballer who played with Geelong in the Victorian Football League( VFL).
- [d4s1] He is the grandfather of Tom Hawkins.

**d5: Miklós Szilágyi**

- [d5s0] Miklós Szilágyi de Alsó- Baksán et Nagy- Dobán( was born at the end of the 14th century), was a Hungarian nobleman, member of the House of Szilágyi, grandfather of Erzsébet Szilágyi and Michael Szilágyi, maternal great- grandfather of King Matthias of Hungary

**d6: Henry Krause**

- [d6s0] Henry J." Red" Krause, Jr.( August 28, 1913 – February 20, 1987) was an American football offensive lineman in the National Football League for the Brooklyn Dodgers and the Washington Redskins.
- [d6s1] He played college football at St. Louis University.
- [d6s2] He is the grandfather of Jennifer Krause
- [d6s3] He is the great grandfather of Payton Hoeing

**d7: Abd al-Muttalib**

- [d7s0] Abd al- Muttalib Shaybah ibn Hashim( c. 497 – 578) was the grandfather of Islamic prophet Muhammad.

**d8: Imre Thurzó**

- [d8s0] Count Imre Thurzó de Bethlenfalva (11 September 1598 – 19 October 1621) was a Hungarian aristocrat, son of Palatine György Thurzó, who served as Perpetual Ispán (Count; "comes") of Árva County between 1616 and 1621.
- [d8s1] Count Imre also functioned as Rector of the University of Wittenberg from 1616 to 1621.
- [d8s2] He was the last male member of the prestigious Thurzó family.

**d9: Gergely Szilágyi**

- [d9s0] Count Gergely Szilágyi( was born at the end of the 14th century), was a Hungarian nobleman, member of the House of Szilágyi, uncle of Erzsébet Szilágyi and Michael Szilágyi.

**d10: Erzsébet Thurzó**

- [d10s0] Countess Erzsébet Thurzó de Bethlenfalva (20 February 1621 – 4 July 1642) was a Hungarian noblewoman, daughter of Count Imre Thurzó and Baroness Krisztina Nyáry.

## 28. 2wikimultihopqa_f618d408084c11ebbd56ac1f6bf848b6

Question: Were both Andreas (Comics) and Albert Üksip, born in the same place?

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | birthplace of Andreas (Comics) | False | () |
| u2 | birthplace of Albert Üksip | False | () |
| u3 | whether Andreas (Comics) and Albert Üksip were born in the same place | True | ('u1', 'u2') |

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

## 29. hotpotqa_5a745a8755429979e288291e 【待确认：语义或标签口径】

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5a745a8755429979e288291e"></a>

> **审阅结论：待确认：语义或标签口径**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** “both what”是开放的共同类别查询；旧答案只接受 private，而两方也可能共有其他机构类别。新 common classification 本身没有限定必须输出 private。
>
> **处理建议：** 保留新 common classification 三单元。人工确认是否只接受 private 或也接受其他有证据的共同类别，并设置合适别名/接受范围；不为匹配旧唯一答案而改写拆题器。
>
> **证据定位：** d10s0, d7s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Wellesley College and Vanderbilt University are both what?

Type: comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | type of Wellesley College | False | () |
| u2 | type of Vanderbilt University | False | () |
| u3 | common classification of Wellesley College and Vanderbilt University | True | ('u1', 'u2') |

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

## 30. hotpotqa_5a75dc7a5542992d0ec06004 【保留新拆法｜重标人工标签】

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5a75dc7a5542992d0ec06004"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新单元合并服务定义和 HCL 是否提供该服务，旧版分两步验证同一术语；目标与限定均保留，合并合理。
>
> **处理建议：** 保留 single；联合 d2s0 的定义和 d9s4 的服务列表标注 Analytics，并重建快照。
>
> **证据定位：** d2s0, d9s4；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: What is the term for the service provided by HCL Technologies involving discovery, interpretation, and communication of patterns in data?

Type: single · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | term for the service provided by HCL Technologies involving discovery, interpretation, and communication of patterns in data | True | () |

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

## 31. hotpotqa_5a7755e05542993735360237 【需改：生成拆解】

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5a7755e05542993735360237"></a>

> **审阅结论：需改：生成拆解**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 单元本身是两个已点名对象的事实加一个比较/共同属性结论，没有寻找未知中间实体的桥接步骤，但 question_type 被写成 bridge_comparison。
>
> **处理建议：** 只将 question_type 改为 comparison，保留当前单元关系；这属于题型元数据错误，不应为凑题型增加桥接单元。
>
> **证据定位：** d7s0, d6s0, d6s1；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Which computer animated film was released first, Khan Kluay or A Christmas Carol starring Jim Carrey?

Type: bridge_comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | release date of Khan Kluay | False | () |
| u2 | release date of A Christmas Carol starring Jim Carrey | False | () |
| u3 | which film was released first | True | ('u1', 'u2') |

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

## 32. hotpotqa_5a77a8365542995d83181250

Question: Gândul Mâței and KMFDM, are what type of musical organization?

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | type of musical organization Gândul Mâței is | False | () |
| u2 | type of musical organization KMFDM is | False | () |
| u3 | what type of musical organization they are | True | ('u1', 'u2') |

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

## 33. hotpotqa_5a78f57a554299148911f9bf 【保留新拆法｜重标人工标签】

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5a78f57a554299148911f9bf"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新 u1 已同时限定效力关系和 Minneapolis–St. Paul 地区，u2 询问其名字，存在冗余但未改变最终实体。旧版先列出全部球队再筛选。
>
> **处理建议：** 保留生成的两单元，不因冗余强行换回旧候选列表。新u1需联合 d3s1 与 d8s2/d8s3 标注球队，新u2沿用同一身份的名称及对应支持/依赖；不把旧u1的整串球队名单复制到新u1。
>
> **证据定位：** d3s1, d8s2, d8s3；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: For which Minneapolis-St. Paul area sports team did Zenon Konopka play? 

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | sports team Zenon Konopka played for in the Minneapolis-St. Paul area | False | () |
| u2 | name of the team {u1} | True | ('u1',) |

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

## 34. hotpotqa_5a7a51485542990783324f0e 【需改：生成拆解】

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5a7a51485542990783324f0e"></a>

> **审阅结论：需改：生成拆解**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 原题要女演员姓名，最终必要单元却是 birth date of {u1}，会把日期当最终答案。
>
> **处理建议：** u1 识别演员候选，u2 明确为“actress among {u1} born in April 1927”；出生日期只是筛选证据，必要单元的值应为演员姓名。
>
> **证据定位：** d4s0, d2s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Under the Yum Yum Tree starred this actress who was born in April, 1927?

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | actress who starred in Under the Yum Yum Tree | False | () |
| u2 | birth date of {u1}, given she was born in April, 1927 | True | ('u1',) |

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

## 35. hotpotqa_5a7aa8565542995eb53be88b 【保留新拆法｜重标人工标签】

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5a7aa8565542995eb53be88b"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新单元完整询问 Katy Mixon 参演且由 Seth Gordon 执导的电影，旧版先列参演电影再筛选；两者目标一致。
>
> **处理建议：** 保留 single，使用 d9s1 的参演关系和 d1s4 的导演关系联合支持；重建新目标和快照，而不是只迁移旧第二跳的直接引用。
>
> **证据定位：** d9s1, d1s4；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: What movie did Katy Mixon star in that was directed by Seth Gordon?

Type: single · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | movie directed by Seth Gordon that Katy Mixon starred in | True | () |

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

## 36. hotpotqa_5a7cfdb755429909bec768e2 【保留新拆法｜重标人工标签】

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5a7cfdb755429909bec768e2"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新单元保留 Frogman Corps→所属武装力量→王国的完整语义关系，只是不把中间军队单列。两种粒度都可由两段证据支持。
>
> **处理建议：** 保留 single；支持集合覆盖 d10s0 与 d3s0，值为王国名；新单元不能在只看到军队名称时提前支持。
>
> **证据定位：** d10s0, d3s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: The Frogman Corps is the maritime special operations force of the unified armed forces of what kingdom?

Type: single · fallback: False · SFT snapshots: 7

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | kingdom whose unified armed forces include the Frogman Corps | True | () |

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

## 37. hotpotqa_5a7f359f55429930675136a9

Question: Who was a Canadian film producer, director, actor and screenwriter, Randal Kirk II or Sidney Olcott?

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | whether Randal Kirk II was a Canadian film producer, director, actor and screenwriter | False | () |
| u2 | whether Sidney Olcott was a Canadian film producer, director, actor and screenwriter | False | () |
| u3 | who was a Canadian film producer, director, actor and screenwriter | True | ('u1', 'u2') |

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

## 38. hotpotqa_5a81d03d55429903bc27b9c7

Question: Are Gurinder Chadha and Hou Hsiao-hsien both from England?

Type: comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | whether Gurinder Chadha is from England | False | () |
| u2 | whether Hou Hsiao-hsien is from England | False | () |
| u3 | whether both Gurinder Chadha and Hou Hsiao-hsien are from England | True | ('u1', 'u2') |

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

## 39. hotpotqa_5a8715fb5542991e771816bb 【保留新拆法｜重标人工标签】

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5a8715fb5542991e771816bb"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新单元以“America's first native born saint”作完整身份限定，直接问出生年；旧版另列电影→圣人。d3s0 在同一句中明确给出该唯一身份和出生日期，合并合理。
>
> **处理建议：** 保留 single；直接以 d3s0 支持出生年1774。电影关系若被用作额外核验，可另保留相应支持路径，但不能强制继承旧电影身份依赖而忽视直接证据。
>
> **证据定位：** d4s0, d3s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question:  A Time for Miracles chronicles the life story of America's first native born saint who was born in what year?

Type: single · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | year America's first native born saint was born | True | () |

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

## 40. hotpotqa_5a87e93155429938390d3ea4

Question: Are Purbanchal University and California State University, Northridge, both public universities?

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | whether Purbanchal University is a public university | False | () |
| u2 | whether California State University, Northridge is a public university | False | () |
| u3 | whether both are public universities | True | ('u1', 'u2') |

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

## 41. hotpotqa_5a88b15b5542994846c1ceba 【保留新拆法｜重标人工标签】

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5a88b15b5542994846c1ceba"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 旧拆法用两方事实+共同结论，新 multipart 分别要求回答两个对象的同一属性，两方都是 necessary。两种都能覆盖题目要求；没有显式共同结论不等于漏答。按用户要求保留生成的两个必要单元。
>
> **处理建议：** 保持 multipart 和两个 necessary=true。分别映射旧u1/u2的属性值和证据，删除旧u3作为独立训练目标；只有两方都支持才是完整。若旧共同答案词过窄，按各方实际描述设置值/别名，不改变新拆法。
>
> **证据定位：** d10s0, d1s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Chino Moreno and Needtobreathe, are of which nationality?

Type: multipart · fallback: False · SFT snapshots: 6

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | nationality of Chino Moreno | True | () |
| u2 | nationality of Needtobreathe | True | () |

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

## 42. hotpotqa_5a9060f05542990a98493604 【需改：生成拆解】

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5a9060f05542990a98493604"></a>

> **审阅结论：需改：生成拆解**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 最终 necessary 单元问的是 British silent drama film adaptation，原题要求小说名；改编电影和原著即使同名也不是同一对象。
>
> **处理建议：** 最后的 necessary 单元必须是“novel by {u1} adapted into a British silent drama film”；可保留旧 gold 的作者→小说两单元结构，电影仅作筛选条件/证据。
>
> **证据定位：** d7s0, d2s0, d2s1；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: What novel written by an American novelist born in 1804 was adapted into a British silent drama film?

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | American novelist born in 1804 | False | () |
| u2 | novel written by {u1} | False | ('u1',) |
| u3 | British silent drama film adaptation of {u2} | True | ('u2',) |

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

## 43. hotpotqa_5ab2585855429970612095e6 【需改：生成拆解】

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5ab2585855429970612095e6"></a>

> **审阅结论：需改：生成拆解**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 模型把 larger 限定成 weight，但给定证据只有 large 与 medium-sized 的体型分类，没有体重数值。
>
> **处理建议：** u1/u2 改为 size classification/size of the breed，并比较体型；不要把大/中型标签当成体重或凭外部知识填公斤数。
>
> **证据定位：** d8s0, d5s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Between the Akita and Boykin Spaniel, which dog breed is larger?

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | weight of the Akita breed | False | () |
| u2 | weight of the Boykin Spaniel breed | False | () |
| u3 | which dog breed is larger | True | ('u1', 'u2') |

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

## 44. hotpotqa_5ab27ea3554299340b5254e4

Question: are Meet the Patels and Arakimentari the same genre of film

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | genre of Meet the Patels | False | () |
| u2 | genre of Arakimentari | False | () |
| u3 | whether Meet the Patels and Arakimentari are the same genre of film | True | ('u1', 'u2') |

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

## 45. hotpotqa_5ab2a4a7554299295394678b

Question: What year was the founder of Mac Fisheries born?

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | founder of Mac Fisheries | False | () |
| u2 | birth year of {u1} | True | ('u1',) |

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

## 46. hotpotqa_5ab33cec554299753aec595c

Question: When would be the album release in which "Too Much to Ask" is the third single song?

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | album containing "Too Much to Ask" as the third single | False | () |
| u2 | release date of {u1} | True | ('u1',) |

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

## 47. hotpotqa_5ab406ce55429976abd1bd36

Question: Was Lev Kuleshov and Lo Wei work in the same country?

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country where Lev Kuleshov worked | False | () |
| u2 | country where Lo Wei worked | False | () |
| u3 | whether Lev Kuleshov and Lo Wei worked in the same country | True | ('u1', 'u2') |

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

## 48. hotpotqa_5ab7eff35542993667794059 【需改：生成拆解】

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5ab7eff35542993667794059"></a>

> **审阅结论：需改：生成拆解**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** kind of musician 被错解成 music genre，原题及证据说的是歌手等音乐人角色；同时题型误标为 bridge_comparison。
>
> **处理建议：** 题型改为 comparison；两方单元询问 musician role/kind of musician，结论输出共同角色（如 singer），而不是摇滚等音乐风格。
>
> **证据定位：** d4s0, d10s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: What kind of musician does Neil Hannon and Stephen Malkmus have in common?

Type: bridge_comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | music genre of Neil Hannon | False | () |
| u2 | music genre of Stephen Malkmus | False | () |
| u3 | common music genre of Neil Hannon and Stephen Malkmus | True | ('u1', 'u2') |

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

## 49. hotpotqa_5ab850d75542990e739ec8c0

Question: Which writter is known to have wrote Harry Potter, Mary Gordon or J. K. Rowling?

Type: comparison · fallback: False · SFT snapshots: 6

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | whether Mary Gordon wrote Harry Potter | False | () |
| u2 | whether J. K. Rowling wrote Harry Potter | False | () |
| u3 | which writer is known to have written Harry Potter | True | ('u1', 'u2') |

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

## 50. hotpotqa_5ab9d4a9554299232ef4a21c

Question: The Pittsburgh Penguins 2003 first overall draft pick tied the franchise record for how many goalie wins?

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | Pittsburgh Penguins 2003 first overall draft pick | False | () |
| u2 | franchise record for goalie wins tied by {u1} | True | ('u1',) |

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

## 51. hotpotqa_5abe97dc5542994516f453cf 【待确认：语义或标签口径】

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5abe97dc5542994516f453cf"></a>

> **审阅结论：待确认：语义或标签口径**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 问题说乐队得名于女权主义者，旧 gold 也按人物描述；d4s3 实际说名称来自她写的 SCUM Manifesto。新单元还把人物/命名来源/乐队全部压在一起。
>
> **处理建议：** 先修订问题与 gold 的命名关系，不把人物和作品混为一谈；可拆为人物→其宣言→以该宣言命名的乐队，最终必要值仍是乐队。没有这一步复核，不应将当前任一版作为已审核训练标签。
>
> **证据定位：** d8s0, d4s0, d4s3；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: What South East London-based post-punk/art rock group took their name from a American radical feminist that is best known for attempting to murder artist Andy Warhol?

Type: single · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | South East London-based post-punk/art rock group named after an American radical feminist known for attempting to murder Andy Warhol | True | () |

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

## 52. hotpotqa_5ac149705542994d76dccdd0

Question: Did Glamour or W come first?

Type: comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | year Glamour was founded | False | () |
| u2 | year W was founded | False | () |
| u3 | which came first | True | ('u1', 'u2') |

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

## 53. hotpotqa_5adbf5d8554299438c868cec

Question: Zota was a foe of the superhero appearing in comic books by which company?

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | superhero that Zota was a foe of | False | () |
| u2 | company that published comic books featuring {u1} | True | ('u1',) |

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

## 54. hotpotqa_5ade960d554299728e26c747

Question: What is the nationality of the top scorer of the 2012–13 Primeira Liga?

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | top scorer of the 2012–13 Primeira Liga | False | () |
| u2 | nationality of {u1} | True | ('u1',) |

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

## 55. hotpotqa_5ae1e7275542997f29b3c18b

Question: Paul Eiding has the role of the Vault Tec Rep from the video game developed by which company?

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | video game featuring Paul Eiding as the Vault Tec Rep | False | () |
| u2 | developer of {u1} | True | ('u1',) |

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

## 56. hotpotqa_5ae29b615542992decbdcd4f 【需改：生成拆解】

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5ae29b615542992decbdcd4f"></a>

> **审阅结论：需改：生成拆解**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 原题问两城市在哪个国家，模型的必要结论却问是否在同一国家，答案类型由国家名变成 yes/no；题型也误写 bridge_comparison。
>
> **处理建议：** 题型改为 comparison，u3 改为“country containing both Huainan and Wuzhishan City”，仍依赖两方国家事实，输出国家名称。
>
> **证据定位：** d1s0, d2s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Huainan and Wuzhishan City, in in which country?

Type: bridge_comparison · fallback: False · SFT snapshots: 6

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of Huainan | False | () |
| u2 | country of Wuzhishan City | False | () |
| u3 | whether Huainan and Wuzhishan City are in the same country | True | ('u1', 'u2') |

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

## 57. hotpotqa_5ae517665542990ba0bbb1b2 【保留新拆法｜重标人工标签】

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5ae517665542990ba0bbb1b2"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新拆法先查 Tiny Dancers 支持过的歌手，再核验 The Verve 身份；旧版反向查找。两种方向均合理，但新第一跳有多个候选。
>
> **处理建议：** 保留新方向；按 d10s2 标注可支持的歌手候选，不在 The Verve 证据尚不可见时提前指定 Richard Ashcroft；新u2再结合 d6s1 及新u1依赖筛选。重新标注每一步证据与标签。
>
> **证据定位：** d6s1, d10s2；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: What singer did the Tiny Dancers support who was in The Verve?

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | singer supported by the Tiny Dancers | False | () |
| u2 | singer in The Verve who was supported by the Tiny Dancers | True | ('u1',) |

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

