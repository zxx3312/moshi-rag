# batch_04：人工审查（30 题）

全局题号 91–120；train 30 题 / dev 0 题。原训练/验证归属保持不变。

[返回分配索引](../README.md) · [完整对比报告](../../comparison_human.md)

**原则：新旧单元都合理时保留拆题器拆法，人工监督向新单元对齐。** 未标记的题目也需要核对答案和证据。现有标记是 AI 辅助审阅意见，不是人工验收结论。

审查人：________　完成日期：________

## 1. 2wikimultihopqa_c3c1a5a00baf11ebab90acde48001122

原位置：`train` 第 91 题 · 全局第 91 题 · `sample_id: 2wikimultihopqa_c3c1a5a00baf11ebab90acde48001122`

Question: Who is Hipparete's father-in-law?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | husband of Hipparete | False | () |
| u2 | father of {u1}, Hipparete's father-in-law | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | husband of Hipparete | False | [] | Alcibiades | [['d1s1']] |
| u2 | father of {u1}, Hipparete's father-in-law | True | ['u1'] | Cleinias | [['d10s0']] |

### Source documents (reference only)

**d1: Hipparete**

- [d1s0] Hipparete  was the daughter of Hipponicus III, a wealthy Athenian.
- [d1s1] She was married c. 424 BC or earlier to the prominent Athenian statesman and general Alcibiades.

**d2: James Armour (Master mason)**

- [d2s0] James Armour (15 January 1730 – 20 September 1798) was a master mason and father of Jean Armour, and therefore the father-in-law of the poet Robert Burns.

**d3: Bill Dundee**

- [d3s0] William" Bill" Cruickshanks( born 24 October 1943) is a Scottish born- Australian professional wrestler and author better known by his stage name Bill Dundee.
- [d3s1] Cruickshanks is the father of Jamie Dundee and the father- in- law of wrestler Bobby Eaton.

**d4: John Adams (merchant)**

- [d4s0] John Adams( 1672 or 1673 – 1745) was an American- born Canadian merchant and member of the Nova Scotia Council.
- [d4s1] He was the father- in- law of Henry Newton( politician).

**d5: Ogawa Mataji**

- [d5s0] Viscount was a general in the early Imperial Japanese Army.
- [d5s1] He was also the father- in- law of Field Marshal Gen Sugiyama.

**d6: Peter Burroughs**

- [d6s0] Peter Burroughs( born 27 January 1947) is a British television and film actor, the director of Willow Management.
- [d6s1] He is the father- in- law of actor and TV presenter Warwick Davis.

**d7: Ludwig von Westphalen**

- [d7s0] Johann Ludwig von Westphalen( 11 July 1770 – 3 March 1842) was a liberal Prussian civil servant and the father- in- law of Karl Marx.

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

**d9: Mohammad Ilyas (cricketer)**

- [d9s0] Mohammad Ilyas Mahmood( born March 19, 1946, Lahore, Punjab) is a former Pakistani cricketer who played in ten Tests from 1964 to 1969.
- [d9s1] He is the father- in- law of Imran Farhat.

**d10: Alcibiades**

- [d10s0] Alcibiades, son of Cleinias (450–404 BC), from the deme of Scambonidae, was a prominent Athenian statesman, orator, and general.
- [d10s1] He was the last famous member of his mother's aristocratic family, the Alcmaeonidae, which fell from prominence after the Peloponnesian War.
- [d10s2] He played a major role in the second half of that conflict as a strategic advisor, military commander, and politician.
- [d10s3] During the course of the Peloponnesian War, Alcibiades changed his political allegiance several times.
- [d10s4] In his native Athens in the early 410s BC, he advocated an aggressive foreign policy and was a prominent proponent of the Sicilian Expedition, but he fled to Sparta after his political enemies brought charges of sacrilege against him.
- [d10s5] In Sparta, he served as a strategic adviser, proposing or supervising several major campaigns against Athens.
- [d10s6] In Sparta too, however, Alcibiades soon made powerful enemies and felt forced to defect to Persia.
- [d10s7] There he served as an adviser to the satrap Tissaphernes until his Athenian political allies brought about his recall.
- [d10s8] He then served as an Athenian general (Strategos) for several years, but his enemies eventually succeeded in exiling him a second time.
- [d10s9] Scholars have argued that had the Sicilian expedition been under Alcibiades's command instead of that of Nicias, the expedition might not have met its eventual disastrous fate.
- [d10s10] In the years when he served Sparta, Alcibiades played a significant role in Athens's undoing; the capture of Decelea and the revolts of several critical Athenian subjects occurred either at his suggestion or under his supervision.
- [d10s11] Once restored to his native city, however, he played a crucial role in a string of Athenian victories that eventually brought Sparta to seek a peace with Athens.
- [d10s12] He favored unconventional tactics, frequently winning cities over by treachery or negotiation rather than by siege.
- [d10s13] Alcibiades's military and political talents frequently proved valuable to whichever state currently held his allegiance, but his propensity for making powerful enemies ensured that he never remained in one place for long; and by the end of the war that he had helped to rekindle in the early 410s, his days of political relevance were a bygone memory.

## 2. 2wikimultihopqa_c3c8e96e0baf11ebab90acde48001122

原位置：`train` 第 92 题 · 全局第 92 题 · `sample_id: 2wikimultihopqa_c3c8e96e0baf11ebab90acde48001122`

Question: Who is the paternal grandmother of John De Southeray?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of John De Southeray | False | () |
| u2 | mother of {u1}, John De Southeray's paternal grandmother | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of John de Southeray | False | [] | Edward III of England | [['d5s0']] |
| u2 | mother of {u1}, John de Southeray's paternal grandmother | True | ['u1'] | Isabella of France | [['d9s3']] |

### Source documents (reference only)

**d1: Hannah Arnold**

- [d1s0] Hannah Arnold, also known as Hannah Waterman King, was the grandmother of Benedict Arnolds children.

**d2: Tjuyu**

- [d2s0] Tjuyu( sometimes transliterated as Thuya or Thuyu) was an Egyptian noblewoman and the mother of queen Tiye, and the wife of Yuya.
- [d2s1] She is the grandmother of Akhenaten, and great grandmother of Tutankhamun.

**d3: Mona Hopton Bell**

- [d3s0] Mona Hopton Bell( 1867- 1940) was a British artist, best known for her portraits of civic figures.
- [d3s1] She was the grandmother of the painter Jean H. Bell.

**d4: Gülbahar Hatun (wife of Mehmed II)**

- [d4s0] Gülbahar Hatun( 1432 – 1492) was the consort of Sultan Mehmed II, and mother of Sultan Bayezid II of the Ottoman Empire and the grandmother of Selim I.

**d5: John de Southeray**

- [d5s0] John de Southeray( 1364- 1383) was an illegitimate son of King Edward III of England by his mistress Alice Perrers.
- [d5s1] He was the oldest of Perrers' three acknowledged illegitimate children by her royal lover.
- [d5s2] He was knighted in April 1377, alongside the future King Richard II.
- [d5s3] That same year, he was married to Maud Percy, a daughter of Henry de Percy, 3rd Baron Percy; she divorced him in 1380, claiming she had not consented to the marriage.
- [d5s4] During the abortive Castilian campaign led by his half- brother the Earl of Cambridge in 1381, John led a contingent of English soldiers.
- [d5s5] After his troops went unpaid, John led them in a mutiny; he may have been only a figurehead for the mutineers, though, as he( unlike the other conspirators) went unpunished afterwards.

**d6: Hubba bint Hulail**

- [d6s0] Hubba bint Hulail was the grandmother of Hashim ibn' Abd Manaf, thus the great- great- great- grandmother of the Islamic" Nabī"( Prophet) Muhammad ibn Abdullah.

**d7: Kaoru Hatoyama**

- [d7s0] After the elections of 2009, she became more widely known as the grandmother of Prime Minister Yukio Hatoyama and his politician brother Kunio Hatoyama.

**d8: Hüma Hatun**

- [d8s0] Hüma Hatun (1410 ‒ September 1449) was the fourth wife of Ottoman Sultan Murad II and mother of Mehmed II and the grandmother of Bayezid II.

**d9: Edward III of England**

- [d9s0] Edward III (13 November 1312 – 21 June 1377) was king of England and Lord of Ireland from January 1327 until his death; he is noted for his military success and for restoring royal authority after the disastrous and unorthodox reign of his father, Edward II.
- [d9s1] Edward III transformed the Kingdom of England into one of the most formidable military powers in Europe.
- [d9s2] His long reign of 50 years was the second-longest in medieval England (after that of his great-grandfather Henry III) and saw vital developments in legislation and government, in particular the evolution of the English Parliament, as well as the ravages of the Black Death.
- [d9s3] Edward was crowned at age fourteen after his father was deposed by his mother, Isabella of France, and her lover Roger Mortimer.
- [d9s4] At age seventeen he led a successful coup d'état against Mortimer, the de facto ruler of the country, and began his personal reign.
- [d9s5] After a successful campaign in Scotland he declared himself rightful heir to the French throne in 1337.
- [d9s6] This started what became known as the Hundred Years' War.
- [d9s7] Following some initial setbacks, this first phase of the war went exceptionally well for England; victories at Crécy and Poitiers led to the highly favourable Treaty of Brétigny, in which England made territorial gains, and Edward renounced his claim to the French throne.
- [d9s8] This phase would become known as the Edwardian War.
- [d9s9] Edward's later years were marked by international failure and domestic strife, largely as a result of his inactivity and poor health.
- [d9s10] Edward III was a temperamental man but capable of unusual clemency.
- [d9s11] He was in many ways a conventional king whose main interest was warfare.
- [d9s12] Admired in his own time and for centuries after, Edward was denounced as an irresponsible adventurer by later Whig historians such as William Stubbs, but modern historians credit him with some significant achievements.

**d10: Anne Denman**

- [d10s0] Anne Denman( 1587–1661) was born in Olde Hall, Retford, Nottinghamshire.
- [d10s1] Through a fortunate second marriage with Thomas Aylesbury, she became the grandmother of Lady Anne Hyde, Duchess of York and great- grandmother of Queen Mary II and Queen Anne.

## 3. 2wikimultihopqa_c526bfac0baf11ebab90acde48001122

原位置：`train` 第 93 题 · 全局第 93 题 · `sample_id: 2wikimultihopqa_c526bfac0baf11ebab90acde48001122`

Question: Who is the paternal grandmother of Drusus Caesar?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Drusus Caesar | False | () |
| u2 | mother of {u1}, Drusus Caesar's paternal grandmother | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Drusus Caesar | False | [] | Germanicus | [['d7s1']] |
| u2 | mother of {u1}, Drusus Caesar's paternal grandmother | True | ['u1'] | Antonia Minor | [['d9s1']] |

### Source documents (reference only)

**d1: Diana Guardato**

- [d1s0] Diana Guardato was a member of the aristocratic Patrician Guardato family, and had three children with King Ferdinand I: Diana Guardato is the 16th- Great Grandmother of His Royal Highness Albert II of Belgium, 15th- Great Grandmother of His Majesty Juan Carlos
- [d1s1] I of Spain, 17th- Great Grandmother of Philippe of Belgium, 14th- Great Grandmother of His Majesty Manuel II of Portugal, 16th- Great Grandmother of Grand Duke Henri, as well as many others.

**d2: Mona Hopton Bell**

- [d2s0] Mona Hopton Bell( 1867- 1940) was a British artist, best known for her portraits of civic figures.
- [d2s1] She was the grandmother of the painter Jean H. Bell.

**d3: Julia Livia**

- [d3s0] Julia Livia (c.7–43 AD), sometimes referred to as Julia Drusi Caesaris filia (Julia, daughter of Drusus Caesar), was the daughter of Drusus Julius Caesar and Livilla, and granddaughter of the Roman Emperor Tiberius.
- [d3s1] She was also a first cousin of the emperor Caligula, and niece of the emperor Claudius.

**d4: Hannah Arnold**

- [d4s0] Hannah Arnold, also known as Hannah Waterman King, was the grandmother of Benedict Arnolds children.

**d5: Kaoru Hatoyama**

- [d5s0] After the elections of 2009, she became more widely known as the grandmother of Prime Minister Yukio Hatoyama and his politician brother Kunio Hatoyama.

**d6: Anne Denman**

- [d6s0] Anne Denman( 1587–1661) was born in Olde Hall, Retford, Nottinghamshire.
- [d6s1] Through a fortunate second marriage with Thomas Aylesbury, she became the grandmother of Lady Anne Hyde, Duchess of York and great- grandmother of Queen Mary II and Queen Anne.

**d7: Drusus Caesar**

- [d7s0] Drusus Caesar (AD 8 – AD 33) was the adopted grandson and heir of the Roman Emperor Tiberius, alongside his brother Nero.
- [d7s1] Born into the prominent Julio Claudian dynasty, Drusus was the son of Tiberius' general and heir, Germanicus.
- [d7s2] After the deaths of his father and of Tiberius' son, Drusus the Younger, Drusus and his brother Nero Julius Caesar were adopted together by Tiberius in September AD 23.
- [d7s3] As a result of being heirs of the emperor, he and his brother enjoyed accelerated political careers.
- [d7s4] Sejanus, the prefect of the Praetorian Guard, had become powerful in Rome and is believed by ancient writers such as Suetonius and Tacitus to have been responsible for the downfall of Drusus the younger.
- [d7s5] As Sejanus' power grew, other members of the imperial family began to fall as well.
- [d7s6] In AD 29, Tiberius wrote a letter to the Senate attacking Nero and his mother, and the Senate had them both exiled.
- [d7s7] Two years later, Nero died in exile on the island of Ponza.
- [d7s8] Drusus was later imprisoned following similar charges as his brother, and remained in prison from AD 30 until his death three years later.
- [d7s9] Their deaths allowed for the adoption and ascension of their third brother, Gaius Caligula, following the death of Tiberius in AD 37.

**d8: Tjuyu**

- [d8s0] Tjuyu( sometimes transliterated as Thuya or Thuyu) was an Egyptian noblewoman and the mother of queen Tiye, and the wife of Yuya.
- [d8s1] She is the grandmother of Akhenaten, and great grandmother of Tutankhamun.

**d9: Germanicus**

- [d9s0] Germanicus (Latin: "Germanicus Julius Caesar"; 24 May 15 BC – 10 October AD 19) was a member of the Julio-Claudian dynasty and a prominent general of the Roman Empire, who was known for his campaigns in Germania.
- [d9s1] The son of Nero Claudius Drusus and Antonia Minor, Germanicus was born into an influential branch of the patrician "gens Claudia".
- [d9s2] The agnomen "Germanicus" was added to his full name in 9 BC when it was posthumously awarded to his father in honor of his victories in Germania.
- [d9s3] In AD 4, he was adopted by his paternal uncle, Tiberius, who succeeded Augustus as Roman emperor a decade later.
- [d9s4] As a result, Germanicus became an official member of the "gens Julia", another prominent family which he was related to on his mother's side.
- [d9s5] His connection to the Julii was further consolidated through a marriage between himself and Agrippina the Elder, a granddaughter of Augustus.
- [d9s6] He was also the nephew of Tiberius, the older brother of Claudius, the father of Caligula, and the maternal grandfather of Nero.
- [d9s7] During the reign of Augustus, Germanicus enjoyed an accelerated political career as the heir of the emperor's heir, entering the office of quaestor five years before the legal age in AD 7.
- [d9s8] He held that office until AD 11, and was elected consul for the first time in AD 12.
- [d9s9] The year after, he was made proconsul of Germania Inferior, Germania Superior, and all of Gaul.
- [d9s10] From there he commanded eight legions, about one-third of the entire Roman army, which he led against the Germanic tribes in his campaigns from AD 14 to 16.
- [d9s11] He avenged the Roman Empire's defeat in the Teutoburg Forest and retrieved two of the three legionary eagles that had been lost during the battle.
- [d9s12] In AD 17 he returned to Rome where he received a triumph before leaving to reorganize the provinces of Asia Minor, whereby he incorporated the provinces of Cappadocia and Commagene in AD 18.
- [d9s13] While in the eastern provinces, he came into conflict with the governor of Syria, Gnaeus Calpurnius Piso.
- [d9s14] During their feud, Germanicus became ill in Antioch, where he died on 10 October AD 19.
- [d9s15] His death has been attributed to poison by ancient sources, but that was never proven.
- [d9s16] As a famous general, he was widely popular and regarded as the ideal Roman long after his death.
- [d9s17] To the Roman people, Germanicus was the Roman equivalent of Alexander the Great due to the nature of his death at a young age, his virtuous character, his dashing physique, and his military renown.

**d10: Hubba bint Hulail**

- [d10s0] Hubba bint Hulail was the grandmother of Hashim ibn' Abd Manaf, thus the great- great- great- grandmother of the Islamic" Nabī"( Prophet) Muhammad ibn Abdullah.

## 4. 2wikimultihopqa_c751b94c088211ebbd6dac1f6bf848b6

原位置：`train` 第 94 题 · 全局第 94 题 · `sample_id: 2wikimultihopqa_c751b94c088211ebbd6dac1f6bf848b6`

Question: Which film has the director born first, Island Of The Blue Dolphins (Film) or House Of Women?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of Island Of The Blue Dolphins (Film) | False | () |
| u2 | birth date of {u1} | False | ('u1',) |
| u3 | director of House Of Women | False | () |
| u4 | birth date of {u3} | False | ('u3',) |
| u5 | which film's director was born first | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of Island of the Blue Dolphins (film) | False | [] | James B. Clark | [['d8s0'], ['d2s4']] |
| u2 | date of birth of {u1} | False | ['u1'] | May 14, 1908 | [['d2s0']] |
| u3 | director of House of Women | False | [] | Crane Wilbur | [['d3s0'], ['d3s1']] |
| u4 | date of birth of {u3} | False | ['u3'] | November 17, 1886 | [['d4s0']] |
| u5 | which of Island of the Blue Dolphins (film) and House of Women has the director born first | True | ['u2', 'u4'] | House of Women | [[]] |

### Source documents (reference only)

**d1: Hartley Lobban**

- [d1s0] Hartley W Lobban (9 May 1926 – 15 October 2004) was a Jamaican-born first-class cricketer who played 17 matches for Worcestershire in the early 1950s.

**d2: James B. Clark (director)**

- [d2s0] James B. Clark Jr.( May 14, 1908 – July 19, 2000) was an American film director, film editor, and television director.
- [d2s1] His career as a film editor began in 1937, and he was nominated for the Academy Award for Best Film Editing in 1941 for" How Green Was My Valley".
- [d2s2] He continued to work as a film editor until 1960, but in 1955 also began a career as a film and television director.
- [d2s3] He tended to focus on works involving people's relationships with animals.
- [d2s4] Among the more popular and notable projects he directed were the films" A Dog of Flanders"( 1959)," The Sad Horse"( 1959)," Misty"( 1961)," Flipper"( 1963)," Island of the Blue Dolphins"( 1964), and" My Side of the Mountain"( 1969), and episodes of the television series" My Friend Flicka"( 1955- 1956)," Batman"( 1966- 1967), and" Lassie"( 1969- 1971).

**d3: House of Women**

- [d3s0] House of Women is a 1962 American crime drama film directed by Crane Wilbur, starring Shirley Knight and Andrew Duggan.
- [d3s1] Walter Doniger who had been initially hired to direct the film was fired and replaced by Crane Wilbur ten days into the shooting.

**d4: Crane Wilbur**

- [d4s0] Crane Wilbur (November 17, 1886 – October 18, 1973) was an American writer, actor and director for stage, radio and screen.
- [d4s1] He was born in Athens, New York.
- [d4s2] Wilbur is best remembered for playing Harry Marvin in "The Perils of Pauline".
- [d4s3] He died in Toluca Lake, California.
- [d4s4] He was a prolific writer and director of at least 67 films from the silent era into the sound era, but it was as an actor that he found lasting recognition, particularly playing opposite Pearl White in the iconoclastic serial "The Perils of Pauline".
- [d4s5] He brought to the first motion pictures
- [d4s6] merry eyes, a great, thick crop of wavy, black hair and an athlete's interest in swimming and horseback riding.
- [d4s7] Twelve years of stage experience prepared him for his venture into the new art of silent motion pictures.

**d5: Claude Weisz**

- [d5s0] Claude Weisz is a French film director born in Paris.

**d6: John McMahon (Surrey and Somerset cricketer)**

- [d6s0] John William Joseph McMahon( 28 December 1917 – 8 May 2001) was an Australian- born first- class cricketer who played for Surrey and Somerset in England from 1947 to 1957.

**d7: Sepideh Farsi**

- [d7s0] Sepideh Farsi is an Iranian film director, born in Tehran in 1965.

**d8: Island of the Blue Dolphins (film)**

- [d8s0] Island of the Blue Dolphins is a 1964 American drama film directed by James B. Clark and written by Jane Klove and Ted Sherdeman.
- [d8s1] It is based on the 1960 novel" Island of the Blue Dolphins" by Scott O' Dell.
- [d8s2] The film stars Celia Kaye, Larry Domasin, Ann Daniel, Carlos Romero, George Kennedy and Hal John Norman.
- [d8s3] The film was released on July 3, 1964, by Universal Pictures.
- [d8s4] The producer and director had previously collaborated on" A Dog of Flanders" and" Misty".
- [d8s5] The film was shot in Gualala, California.

**d9: Wale Adebanwi**

- [d9s0] Wale Adebanwi( born 1969) is a Nigerian- born first Black Rhodes Professor at St Antony's College, Oxford.

**d10: Henry Moore (cricketer)**

- [d10s0] Henry Walter Moore( 1849 – 20 August 1916) was an English- born first- class cricketer who spent most of his life in New Zealand.

## 5. 2wikimultihopqa_c99c2b3d086f11ebbd62ac1f6bf848b6

原位置：`train` 第 95 题 · 全局第 95 题 · `sample_id: 2wikimultihopqa_c99c2b3d086f11ebbd62ac1f6bf848b6`

Question: Are both bands, Kreyson and Menace Clan, from the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 7

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of Kreyson | False | () |
| u2 | country of Menace Clan | False | () |
| u3 | whether Kreyson and Menace Clan are from the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country of origin of Kreyson | False | [] | Czech | [['d3s0']] |
| u2 | country of origin of Menace Clan | False | [] | American | [['d1s0']] |
| u3 | whether Kreyson and Menace Clan are from the same country | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Menace Clan**

- [d1s0] Menace Clan was an American hip- hop duo composed of Dante" Dee" Miller and Walter" Assassin" Adams formally signed to Rap- a- Lot Records.
- [d1s1] After signing with Rap- a- Lot, the duo appeared on Poppa LQ's" Your Entertainment, My Reality" and Bushwick Bill's" Phantom of the Rapra", and contributed a verse to the All- Star track," The Points".
- [d1s2] The duo's debut album" Da Hood" was released on October 10, 1995, but it failed to sell a significant number of copies and only reached number 44 on the" Billboard" Top R&B/ Hip- Hop Albums.
- [d1s3] After the release of" Da Hood", Menace Clan remained with Rap- a- Lot, appearing on the Geto Boys" The Resurrection" and Scarface's" My Homies", before leaving the label in 1998.
- [d1s4] The duo's last appearance was in 2000 on D-Red's" Smokin'& Lean'n 2000".
- [d1s5] Dante also appeared on the track," My Block", featured on Houston rapper Lil Flip's 2000 underground debut album" The Leprechaun".

**d2: Across the Great Divide tour**

- [d2s0] The Across the Great Divide tour was a concert tour by Australian alternative rock bands Powderfinger and Silverchair in 2007.
- [d2s1] The tour featured concerts in 26 towns across Australia and multiple shows in New Zealand.
- [d2s2] According to Powderfinger frontman Bernard Fanning, the aim of the tour was to" show[ that] both bands are behind the idea of reconciliation."
- [d2s3] Both bands aimed to increase awareness of the efforts of Reconciliation Australia to reduce the current 17- year gap in life expectancy between the average Australian life and that of Indigenous Australians.
- [d2s4] A triple DVD set was released with the same title as the tour on 1 December 2007 with the Melbourne performances for both bands and backstage occurrences from the tour.

**d3: Kreyson**

- [d3s0] Kreyson is a Czech metal band founded in Prague in 1989 by Ladislav Křížek( Vitacit, Citron, Damiens) after leaving the band Citron.
- [d3s1] He was joined by Jaroslav Bartoň, also from Citron, Daniel Krob( Arakain), Robert Vondrovic( Arakain), and Karel Adam( Moped).

**d4: Clan Forbes**

- [d4s0] Clan Forbes is a Highland Scottish clan from Aberdeenshire, Scotland.

**d5: Thampan**

- [d5s0] Thampan is the name of Nair clan from the state of Kerala in India.

**d6: Clan Pringle**

- [d6s0] Clan Pringle is an Armigerous clan from the Scottish Borders.

**d7: Sō Yoshiyori**

- [d7s0] Yoshinori was the head of the Sō clan from 1842 through 1862.

**d8: Young and Menace**

- [d8s0] " Young and Menace" is a song by American rock band Fall Out Boy, released on April 27, 2017, through Island Records and DCD2.
- [d8s1] It was released as the lead single from the band's seventh studio album," Mania".
- [d8s2] The music video was released simultaneously with the single.

**d9: Johnny Foreigner / Stagecoach**

- [d9s0] Johnny Foreigner/ Stagecoach is a split EP between Johnny Foreigner and Stagecoach.
- [d9s1] Released on November 15, 2010 through Alcopop!
- [d9s2] Records it features an original track from both bands as well as another track in which both bands perform a cover song of each other's songs and was limited to 500 copies.

**d10: Clan Agnew**

- [d10s0] Clan Agnew is a Scottish clan from Galloway in the Scottish Lowlands.

## 6. 2wikimultihopqa_cb2146660baf11ebab90acde48001122

原位置：`train` 第 96 题 · 全局第 96 题 · `sample_id: 2wikimultihopqa_cb2146660baf11ebab90acde48001122`

Question: Who is Thorvald Eiriksson's paternal grandfather?

Note:

Type: bridge · fallback: False · SFT snapshots: 7

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Thorvald Eiriksson | False | () |
| u2 | father of {u1}, Thorvald Eiriksson's paternal grandfather | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Thorvald Eiriksson | False | [] | Erik the Red | [['d7s0']] |
| u2 | father of {u1}, Thorvald Eiriksson's paternal grandfather | True | ['u1'] | Thorvald Asvaldsson | [['d5s1']] |

### Source documents (reference only)

**d1: Fred Le Deux**

- [d1s0] Frederick" Fred" Le Deux( born 4 December 1934) was an Australian rules footballer who played with Geelong in the Victorian Football League( VFL).
- [d1s1] He is the grandfather of Tom Hawkins.

**d2: John Mackay (poet)**

- [d2s0] John Mackay( 1656–1754), known as( The Blind Piper), was a Scottish Gaelic poet and composer, and the grandfather of William Ross.

**d3: Henry Krause**

- [d3s0] Henry J." Red" Krause, Jr.( August 28, 1913 – February 20, 1987) was an American football offensive lineman in the National Football League for the Brooklyn Dodgers and the Washington Redskins.
- [d3s1] He played college football at St. Louis University.
- [d3s2] He is the grandfather of Jennifer Krause
- [d3s3] He is the great grandfather of Payton Hoeing

**d4: Lyon Cohen**

- [d4s0] Lyon Cohen( 1868–1937) was a Polish- born Canadian businessman and a philanthropist.
- [d4s1] He was the grandfather of singer/ poet Leonard Cohen.

**d5: Erik the Red**

- [d5s0] Erik Thorvaldsson (950 – 1003), known as Erik the Red, was a Norse explorer, described in medieval and Icelandic saga sources as having founded the first settlement in Greenland.
- [d5s1] According to Icelandic sagas, he was born in the Jæren district of Rogaland, Norway, as the son of Thorvald Asvaldsson.
- [d5s2] He therefore also appears, patronymically, as Erik Thorvaldsson.
- [d5s3] The appellation "the Red" most likely refers to the color of his hair and beard.
- [d5s4] Icelandic explorer Leif Erikson was Erik's son.

**d6: Zhao Shoushan**

- [d6s0] Zhao Shoushan( 12 November 1894 – 20 June 1965) was a KMT general and later Chinese Communist Party politician.
- [d6s1] He is the grandfather of Zhao Leji.

**d7: Thorvald Eiriksson**

- [d7s0] Thorvald Eiriksson  was the son of Erik the Red and brother of Leif Erikson.
- [d7s1] The only Medieval Period source material available regarding Thorvald Eiriksson are the two "Vinland sagas"; the "Greenland Saga" and the "Saga of Erik the Red".
- [d7s2] Although differing in various detail, according to both sagas
- [d7s3] Thorvald was part of an expedition for the exploration of Vinland and became the first European to die in North America.
- [d7s4] The "Greenland Saga" describes a voyage made by Bjarni Herjolfsson, and the subsequent voyages of Leif Eriksson, his brother Thorvald Eiriksson, his sister Freydís Eiríksdóttir, and the Icelandic merchant Thorfinn Karsefni.
- [d7s5] The Saga describes hostilities with skraelings, the Norse term for the native peoples they met in the lands visited south and west of Greenland which they called Vinland and Markland.
- [d7s6] The "Saga of Erik the Red" tells the story as a single expedition led by Thorfinn Karsefni.
- [d7s7] The voyage of Thorvald Eriksson is told here as part of the Karsefni expedition.

**d8: Abd al-Muttalib**

- [d8s0] Abd al- Muttalib Shaybah ibn Hashim( c. 497 – 578) was the grandfather of Islamic prophet Muhammad.

**d9: John Westley**

- [d9s0] Rev. John Westley( 1636 – 78) was an English nonconformist minister.
- [d9s1] He was the grandfather of John Wesley( founder of Methodism).

**d10: Kaya Alp**

- [d10s0] Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

## 7. 2wikimultihopqa_cbcd85f00bd911eba7f7acde48001122

原位置：`train` 第 97 题 · 全局第 97 题 · `sample_id: 2wikimultihopqa_cbcd85f00bd911eba7f7acde48001122`

Question: Which country the performer of song Backwater Blues is from?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | performer of song Backwater Blues | False | () |
| u2 | country of origin of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | performer of song Backwater Blues | False | [] | Bessie Smith | [['d7s1']] |
| u2 | country of {u1} | True | ['u1'] | United States | [['d2s0']] |

### Source documents (reference only)

**d1: Bernie Bonvoisin**

- [d1s0] Bernard Bonvoisin, known as Bernie Bonvoisin( born 9 July 1956 in Nanterre, Hauts- de- Seine), is a French hard rock singer and film director.
- [d1s1] He is best known for having been the singer of Trust.
- [d1s2] He was one of the best friends of Bon Scott the singer of AC/ DC and together they recorded the song" Ride On" which was one of the last songs by Bon Scott.

**d2: Bessie Smith**

- [d2s0] Bessie Smith (April 15, 1894 – September 26, 1937) was an American blues singer.
- [d2s1] Nicknamed the Empress of the Blues, she was the most popular female blues singer of the 1920s and 1930s.
- [d2s2] She is often regarded as one of the greatest singers of her era and was a major influence on fellow blues singers, as well as jazz vocalists.

**d3: O Valencia!**

- [d3s0] " O Valencia!" is the fifth single by the indie rock band
- [d3s1] The Decemberists, and the first released from their fourth studio album," The Crane Wife".
- [d3s2] The music was written by The Decemberists and the lyrics by Colin Meloy.
- [d3s3] It tells a story of two star- crossed lovers.
- [d3s4] The singer falls in love with a person who belongs to an opposing gang.
- [d3s5] At the end of the song, the singer's lover jumps in to defend the singer, who is confronting his lover's brother( the singer's" sworn enemy") and is killed by the bullet intended for the singer.

**d4: Kristian Leontiou**

- [d4s0] Kristian Leontiou (born February 1982) is a British singer of Greek Cypriot descent, and is the singer for the indie rock band One eskimO.

**d5: Panda (Astro song)**

- [d5s0] " Panda" is a song of the Chilean band Astro and is the fifth song of the homonymous album of the year 2011.
- [d5s1] The song was composed and produced by the singer of the band Andrés Nusser and released like third single of the album on February 1, 2013.

**d6: Back from the Edge (disambiguation)**

- [d6s0] Back from the Edge is a 2016 album by James Arthur, and it s title song.
- [d6s1] Back from the Edge may also refer to:

**d7: Backwater Blues**

- [d7s0] The song "Backwater Blues" is a blues and jazz standard.
- [d7s1] It was written by Bessie Smith, and recorded (under the title "Back-water Blues") by her (vocals) and James P. Johnson (piano) on February 17, 1927.
- [d7s2] The song has long been associated with the Great Mississippi Flood of 1927.
- [d7s3] However, that flood was at its worst some two months after the song was written.
- [d7s4] Study of Smith's touring itinerary, of testimony of fellow entertainers who toured with her, and of contemporary reports indicates that the song was written in response to the flood that struck Nashville, Tennessee on Christmas Day 1926.
- [d7s5] The Cumberland River, which flows through the city, rose above its normal level, still a record .
- [d7s6] The lyrics are in the often-used AAB blues format.
- [d7s7] The words vary from one performer to another; this opening verse is representative:
- [d7s8] The song is quoted in the poem, "Ma Rainey" by Sterling A. Brown.

**d8: Dáithí Sproule**

- [d8s0] Dáithí Sproule( born 23 May 1950) is a guitarist and singer of traditional Irish music.
- [d8s1] His niece is the singer Claire Sproule.

**d9: Billy Milano**

- [d9s0] Billy Milano is a Bronx- born heavy metal musician now based in Austin, Texas.
- [d9s1] He is the singer and- occasionally- guitarist and bassist of crossover thrash band M.O.D., and he was also the singer of its predecessor, Stormtroopers of Death.
- [d9s2] He was also the singer of United Forces, which also featured his Stormtroopers of Death bandmate Dan Lilker.

**d10: Caspar Babypants**

- [d10s0] Caspar Babypants is the stage name of children's music artist Chris Ballew, who is also widely known as the singer of The Presidents of the United States of America.

## 8. 2wikimultihopqa_cdd42e23087c11ebbd6aac1f6bf848b6 【保留新拆法｜重标人工标签】

原位置：`train` 第 98 题 · 全局第 98 题 · `sample_id: 2wikimultihopqa_cdd42e23087c11ebbd6aac1f6bf848b6`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_cdd42e23087c11ebbd6aac1f6bf848b6"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。
>
> **处理建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。
>
> **证据定位：** d3s1, d10s0, d7s0, d5s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Do both films: A Doll's House (1917 film) and Circles (film) have the directors from the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of director of A Doll's House (1917 film) | False | () |
| u2 | country of director of Circles (film) | False | () |
| u3 | whether the directors of A Doll's House (1917 film) and Circles (film) are from the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of A Doll's House (1917 film) | False | [] | Joe De Grasse | [['d3s1']] |
| u2 | nationality of {u1} | False | ['u1'] | Canadian | [['d10s0']] |
| u3 | director of Circles (film) | False | [] | Srdan Golubović | [['d7s0']] |
| u4 | nationality of {u3} | False | ['u3'] | Serbian | [['d5s0']] |
| u5 | whether the directors of A Doll's House (1917 film) and Circles (film) are from the same country | True | ['u2', 'u4'] | no | [[]] |

### Source documents (reference only)

**d1: A Doll's House (1959 film)**

- [d1s0] A Doll's House is a 1959 live telecast based on Henrik Ibsen's 1879 play" A Doll's House" directed by George Schaefer which was broadcast on 15 November 1959 and is preserved as a kinescope.

**d2: A Doll's House (1973 Garland film)**

- [d2s0] A Doll's House is a 1973 British film, directed by Patrick Garland.
- [d2s1] It is based on Henrik Ibsen's play" A Doll's House"( 1879).

**d3: A Doll's House (1917 film)**

- [d3s0] A Doll's House is a 1917 American silent drama film based upon the play by Henrik Ibsen.
- [d3s1] It was directed by Joe De Grasse and stars Lon Chaney.

**d4: Ruth Eleanor Newton**

- [d4s0] Ruth Eleanor Newton( March 6, 1884 – May 27, 1972) was an American illustrator and doll designer.

**d5: Srdan Golubović**

- [d5s0] Srdan Golubović( born August 24, 1972) is a Serbian film director.

**d6: A Doll's House (1943 film)**

- [d6s0] A Doll's House is a 1943 Argentine drama film directed by Ernesto Arancibia and starring Delia Garcés and George Rigaud.
- [d6s1] It is based on the play" A Doll's House" by Henrik Ibsen.
- [d6s2] At the 1944 Argentine Film Critics Association Awards, Alberto López won the Best Sound for the film.

**d7: Circles (film)**

- [d7s0] Circles(/ Krugovi) is a 2013 Serbian drama film directed by Srdan Golubović.
- [d7s1] The film was selected as the Serbian entry for the Best Foreign Language Film at the 86th Academy Awards, but it was not nominated.
- [d7s2] The film won the Prize of the Ecumenical Jury at the 63rd Berlin International Film Festival and the Grand Prix, Golden Apricot at the 2013 Yerevan International Film Festival, Armenia, for Best Feature Film as well as the Grand Prix at 2013 CinEast Festival.

**d8: Anjana Vasan**

- [d8s0] Anjana Vasan is a Singaporean actor and singer- songwriter.
- [d8s1] She moved to the UK where she studied acting at the Royal Welsh College of Music& Drama.
- [d8s2] She has appeared in numerous productions on stage and screen, and has won acclaim for her roles in plays such as" Summer and Smoke"( Almeida Theatre)," Rutherford and Son"( National Theatre) and" A Doll's House"( Lyric Hammersmith).

**d9: The Flame of the Yukon (1926 film)**

- [d9s0] The Flame of the Yukon( 1926) is a silent Northwoods adventure- drama film starring Seena Owen and directed by George Melford.
- [d9s1] The film is based on a story by Monte Katterjohn and was distributed by Cecil DeMille's PDC( Producers Distributing Corporation).
- [d9s2] The film is a remake of a 1917 film that had starred Dorothy Dalton.
- [d9s3] The 1917 film survives at the Library of Congress.
- [d9s4] The 1926 film, once thought to be lost, is preserved at the UCLA Film and Television Archive.

**d10: Joseph De Grasse**

- [d10s0] Joseph Louis De Grasse( May 4, 1873 – May 25, 1940) was a Canadian film director.
- [d10s1] Born in Bathurst, New Brunswick, he was the elder brother of actor Sam De Grasse.

## 9. 2wikimultihopqa_d09d82000bda11eba7f7acde48001122

原位置：`train` 第 99 题 · 全局第 99 题 · `sample_id: 2wikimultihopqa_d09d82000bda11eba7f7acde48001122`

Question: What is the date of birth of the performer of song Down To The Honkytonk?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | performer of song Down To The Honkytonk | False | () |
| u2 | date of birth of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | performer of song Down to the Honkytonk | False | [] | Jake Owen | [['d5s0']] |
| u2 | date of birth of {u1} | True | ['u1'] | August 28, 1981 | [['d7s0']] |

### Source documents (reference only)

**d1: Bernie Bonvoisin**

- [d1s0] Bernard Bonvoisin, known as Bernie Bonvoisin( born 9 July 1956 in Nanterre, Hauts- de- Seine), is a French hard rock singer and film director.
- [d1s1] He is best known for having been the singer of Trust.
- [d1s2] He was one of the best friends of Bon Scott the singer of AC/ DC and together they recorded the song" Ride On" which was one of the last songs by Bon Scott.

**d2: Billy Milano**

- [d2s0] Billy Milano is a Bronx- born heavy metal musician now based in Austin, Texas.
- [d2s1] He is the singer and- occasionally- guitarist and bassist of crossover thrash band M.O.D., and he was also the singer of its predecessor, Stormtroopers of Death.
- [d2s2] He was also the singer of United Forces, which also featured his Stormtroopers of Death bandmate Dan Lilker.

**d3: Etan Boritzer**

- [d3s0] Etan Boritzer( born 1950) is an American writer of children ’s literature who is best known for his book" What is God?" first published in 1989.
- [d3s1] His best selling" What is?" illustrated children's book series on character education and difficult subjects for children is a popular teaching guide for parents, teachers and child- life professionals.
- [d3s2] Boritzer gained national critical acclaim after" What is God?" was published in 1989 although the book has caused controversy from religious fundamentalists for its universalist views.
- [d3s3] The other current books in the" What is?" series include
- [d3s4] What is Love?,
- [d3s5] What is Death?,
- [d3s6] What is Beautiful?,
- [d3s7] What is Funny?,
- [d3s8] What is Right?,
- [d3s9] What is Peace?,
- [d3s10] What is Money?,
- [d3s11] What is Dreaming?,
- [d3s12] What is a Friend?,
- [d3s13] What is True?,
- [d3s14] What is a Family?,
- [d3s15] What is a Feeling?"
- [d3s16] The series is now also translated into 15 languages.
- [d3s17] Boritzer was first published in 1963 at the age of 13 when he wrote an essay in his English class at Wade Junior High School in the Bronx, New York on the assassination of John F. Kennedy.
- [d3s18] His essay was included in a special anthology by New York City public school children compiled and published by the New York City Department of Education.
- [d3s19] Boritzer now lives in Venice, California and maintains his publishing office there also.
- [d3s20] He has helped numerous other authors to get published through" How to Get Your Book Published!" programs.
- [d3s21] Boritzer is also a yoga teacher who teaches regular classes locally and guest- teaches nationally.
- [d3s22] He is also recognized nationally as an erudite speaker on" The Teachings of the Buddha."

**d4: Caspar Babypants**

- [d4s0] Caspar Babypants is the stage name of children's music artist Chris Ballew, who is also widely known as the singer of The Presidents of the United States of America.

**d5: Down to the Honkytonk**

- [d5s0] "Down to the Honkytonk" is a song recorded by American country music singer Jake Owen.
- [d5s1] It is the second single from his sixth studio album "Greetings from... Jake".
- [d5s2] The song was written by Rodney Clawson, Luke Laird, and Shane McAnally, and produced by Big Loud Records co-owner Joey Moi.

**d6: Terence Robinson**

- [d6s0] Terence D. Robinson( date of birth and death unknown) was a male wrestler who competed for England.

**d7: Jake Owen**

- [d7s0] Joshua Ryan Owen (born August 28, 1981), known professionally as Jake Owen, is an American country music singer and songwriter and actor.
- [d7s1] Signed to RCA Nashville in 2006, he released his debut studio album, "Startin' with Me", that year.
- [d7s2] This album produced three singles, all of which reached top 20 on the "Billboard" Hot Country Songs chart: his debut single "Yee HawStartin' with Me", and "Something About a Woman".
- [d7s3] His second studio album, 2009's "Easy Does It", accounted for three more singles: "Don't Think I Can't Love YouEight Second Ride", and "Tell Me".
- [d7s4] In September 2011, Owen achieved his first number one hit on the country charts with the title track to his third studio album "Barefoot Blue Jean Night", as did with "Alone with YouThe One That Got Away", and "Anywhere with You".
- [d7s5] His fourth studio album, "Days of Gold", produced two singles with its title track, which broke the top 20 in 2014, and the number one single "Beachin'".
- [d7s6] Owen has also toured as an opening act for several other country artists, including Kenny Chesney, Brad Paisley, Little Big Town, Sugarland, Keith Urban, and Jason Aldean.

**d8: Brian Saunders (weightlifter)**

- [d8s0] Brian Saunders( date of birth and death unknown) was a male weightlifter who competed for England.

**d9: Theodred II (Bishop of Elmham)**

- [d9s0] Theodred II was a medieval Bishop of Elmham.
- [d9s1] The date of Theodred's consecration unknown, but the date of his death was sometime between 995 and 997.

**d10: O Valencia!**

- [d10s0] " O Valencia!" is the fifth single by the indie rock band
- [d10s1] The Decemberists, and the first released from their fourth studio album," The Crane Wife".
- [d10s2] The music was written by The Decemberists and the lyrics by Colin Meloy.
- [d10s3] It tells a story of two star- crossed lovers.
- [d10s4] The singer falls in love with a person who belongs to an opposing gang.
- [d10s5] At the end of the song, the singer's lover jumps in to defend the singer, who is confronting his lover's brother( the singer's" sworn enemy") and is killed by the bullet intended for the singer.

## 10. 2wikimultihopqa_d2e0be5a08b611ebbd88ac1f6bf848b6

原位置：`train` 第 100 题 · 全局第 100 题 · `sample_id: 2wikimultihopqa_d2e0be5a08b611ebbd88ac1f6bf848b6`

Question: Which film has the director died later, Panam Paduthum Padu or Taxi!?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of Panam Paduthum Padu | False | () |
| u2 | death date of {u1} | False | ('u1',) |
| u3 | director of Taxi! | False | () |
| u4 | death date of {u3} | False | ('u3',) |
| u5 | which film's director died later | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Panam Paduthum Padu | False | [] | Y. R. Swamy | [['d1s0']] |
| u2 | date of death of {u1} | False | ['u1'] | 21 October 2002 | [['d4s0']] |
| u3 | director of film Taxi! | False | [] | Roy Del Ruth | [['d6s0']] |
| u4 | date of death of {u3} | False | ['u3'] | April 27, 1961 | [['d5s0']] |
| u5 | which of Panam Paduthum Padu and Taxi! has the director who died later | True | ['u2', 'u4'] | Panam Paduthum Padu | [[]] |

### Source documents (reference only)

**d1: Panam Paduthum Padu**

- [d1s0] Panam Paduthum Padu is a 1954 Indian Tamil- language film directed by Y. R. Swamy.
- [d1s1] The film stars N. T. Rama Rao and Sowcar Janaki.

**d2: Thulasi (1987 film)**

- [d2s0] Thulasi is a 1987 Tamil romantic drama film directed by Ameerjan.
- [d2s1] The film features Murali and Seetha in lead roles.
- [d2s2] The film, produced by P. S. V. Hariharan, had musical score by Sampath Selvam and was released on 27 November 1987.
- [d2s3] The music director died before the release of the film.

**d3: Kathal Paduthum Padu**

- [d3s0] Kathal Paduthum Padu  is a 1966 Indian Tamil-language film directed by Joseph Thaliath Jr and produced under Citadel Studios.
- [d3s1] The film stars Jaishankar, Vanisri and Jayanthi in the lead roles.
- [d3s2] It was released on 7 October 1966 and became a commercial success.

**d4: Y. R. Swamy**

- [d4s0] Y. R. Swamy( c. 1927 – 21 October 2002) was an Indian film director and screenwriter who worked primarily Kannada cinema.
- [d4s1] He directed over 35 films in his career, 17 of which came in films that stars Rajkumar in the lead role.
- [d4s2] He also holds the record for directing Rajkumar for the highest no. of times- seventeen.
- [d4s3] His first film as a director came in the 1953 Tamil film," Pratigna".
- [d4s4] Since then, Swamy directed films in the Kannada language and mostly in the mythological genre and with a social connect.
- [d4s5] His popular films include" Bhakta Kanakadasa"( 1960)," Katari Veera"( 1966)," Paropakari"( 1970)," Sipayi Ramu"( 1972) and" Bhale Huchcha"( 1972).
- [d4s6] Recognizing his contribution to Kannada cinema, he was awarded the 1990 – 91 Puttanna Kanagal Award.

**d5: Roy Del Ruth**

- [d5s0] Roy Del Ruth( October 18, 1893, Delaware – April 27, 1961) was an American film director.

**d6: Taxi!**

- [d6s0] Taxi! is a 1932 American pre-Code gangster film directed by Roy Del Ruth and starring James Cagney and Loretta Young.
- [d6s1] The film includes two famous Cagney dialogues, one of which features Cagney conducting a conversation with a passenger in Yiddish, and the other when Cagney is speaking to his brother's killer through a locked closet, Come out and take it, you dirty yellow- bellied rat, or I'll give it to you through the door!
- [d6s2] The provenance of this sequence led to Cagney being famously misquoted as saying, You dirty rat, you killed my brother.
- [d6s3] To play his competitor in a ballroom dance contest, Cagney recommended his pal, fellow tough- guy- dancer George Raft, who was uncredited in the film.
- [d6s4] In a lengthy and memorable sequence, the scene culminates with Raft and his partner winning the dance contest against Cagney and Young, after which Cagney slugs Raft and knocks him down.
- [d6s5] As in" The Public Enemy"( 1931), several scenes in" Taxi!" involved the use of live machine gun bullets.
- [d6s6] After a few of the bullets narrowly missed Cagney's head, he outlawed the practice in his future films.
- [d6s7] In the film they see a fictitious Warner Bros.
- [d6s8] movie at the cinema called" Her Hour of Love" in which Cagney cracks a joke about the film's leading man's appearance( an unbilled cameo by Warners contract player Donald Cook, who had played Cagney's brother in" The Public Enemy") saying," his ears are too big".
- [d6s9] Also advertised in the cinema lobby in the film is" The Mad Genius", an actual film starring John Barrymore which was released the previous year by Warners and is a plug by them.

**d7: Querelle**

- [d7s0] Querelle is a 1982 West German- French English- language drama film directed by Rainer Werner Fassbinder and starring Brad Davis, adapted from French author Jean Genet's 1947 novel" Querelle of Brest".
- [d7s1] It marked Fassbinder's final film as a writer/ director; it was posthumously released just months after the director died of a drug overdose in June 1982.

**d8: Mohsen Eslamzadeh**

- [d8s0] Mohsen Eslamzadeh is an Iranian documentary filmmaker.
- [d8s1] He is the director of" Alone Among The Taliban".
- [d8s2] This film has won the best documentary award at the 44th Athens International Film and Video Festival in the United States.
- [d8s3] This film has won the best documentary award at the 12th Marbella International Film Festival in Spain.
- [d8s4] This film has won the Shahid Avini Award offers.

**d9: Ravina (actress)**

- [d9s0] Ravina is an Indian actress who acted in Dhallywood movies.
- [d9s1] She acted in" Praner Cheye Priyo" which film is considered as turning point of the career of Riaz.

**d10: Le Masque de la Méduse**

- [d10s0] Le masque de la Méduse is a 2009 fantasy horror film directed by Jean Rollin.
- [d10s1] The film is a modern-day telling of the Greek mythological tale of the Gorgon and was inspired by the 1964 classic Hammer Horror film of the same name and the 1981 cult classic" Clash of the Titans".
- [d10s2] It was Rollin's final film, as the director died in 2010.

## 11. 2wikimultihopqa_d49e4dfd089311ebbd75ac1f6bf848b6

原位置：`train` 第 101 题 · 全局第 101 题 · `sample_id: 2wikimultihopqa_d49e4dfd089311ebbd75ac1f6bf848b6`

Question: Are both Pass Island, Newfoundland And Labrador and Elvalandet located in the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 7

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of Pass Island, Newfoundland And Labrador | False | () |
| u2 | country of Elvalandet | False | () |
| u3 | whether both are located in the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country of Pass Island, Newfoundland and Labrador | False | [] | Canada | [['d7s0']] |
| u2 | country of Elvalandet | False | [] | Norway | [['d8s0']] |
| u3 | whether Pass Island, Newfoundland and Labrador and Elvalandet are located in the same country | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Pilley's Island**

- [d1s0] Pilley's Island is a town in Newfoundland and Labrador.
- [d1s1] It is located in Division No. 8, Newfoundland and Labrador.

**d2: Shannie Duff**

- [d2s0] Suzanne" Shannie" Duff, is a Canadian politician, who has served as mayor of St. John's, Newfoundland and Labrador and as a member of the Newfoundland and Labrador House of Assembly.

**d3: Keith Russell (politician)**

- [d3s0] Keith Russell is a Canadian politician in Newfoundland and Labrador and former Minister of Labrador and Aboriginal Affairs.
- [d3s1] He was elected to the Newfoundland and Labrador House of Assembly in the 2011 provincial election.
- [d3s2] A member of the Progressive Conservative Party of Newfoundland and Labrador, he represented the Labrador district of Lake Melville until his 2015 election defeat.
- [d3s3] Before entering provincial politics Russell was an Ordinary Member for Upper Lake Melville in the Nunatsiavut Government.

**d4: Bell Island Airport**

- [d4s0] Bell Island Airport, is located on Bell Island, Newfoundland and Labrador, Canada.

**d5: Puffin Island, Newfoundland and Labrador**

- [d5s0] Puffin Island, Newfoundland and Labrador may refer to:

**d6: Cottlesville**

- [d6s0] Cottlesville is a rural community just outside Summerford on New World Island, Newfoundland and Labrador.

**d7: Pass Island, Newfoundland and Labrador**

- [d7s0] Pass Island is a resettled community located on the Southern Shore of Newfoundland and Labrador, Canada.
- [d7s1] Many remnants from previous settlements are still visible across the ocean separating it from the community of Seal Cove, Fortune Bay.
- [d7s2] Many of the settlers from previously existent insular communities of Pass Island, were resettled to the communities of Hermitage- Sandyville and Harbour Breton.

**d8: Elvalandet**

- [d8s0] Elvalandet is an island in Trøndelag county, Norway.
- [d8s1] The island is located in the municipalities of Namsos and Fosnes.
- [d8s2] It is located in the Lauvøyfjorden, just south of the island of Jøa, east of the island of Otterøya, and west of the mainland.
- [d8s3] The town of Namsos lies about south of the island.
- [d8s4] The island is connected to the mainland by a bridge on the Norwegian County Road 769.
- [d8s5] There is a ferry connection on the north side of the island to the nearby island of Jøa.
- [d8s6] Most of the island is forested.
- [d8s7] The island is the 82nd largest island in Norway.

**d9: General Assembly of Newfoundland and Labrador**

- [d9s0] The General Assembly of Newfoundland and Labrador( known as the General Assembly of Newfoundland until 6 December 2001) is the legislature of the province of Newfoundland and Labrador, Canada.
- [d9s1] Today, the legislature is made of two elements: the monarch of Canada, represented by the Lieutenant Governor of Newfoundland and Labrador, and the unicameral assembly called the Newfoundland and Labrador House of Assembly.
- [d9s2] The legislature was first established in 1832.
- [d9s3] Like the Canadian federal government, Newfoundland and Labrador uses a Westminster- style parliamentary government, in which members are sent to the House of Assembly after general elections.
- [d9s4] The leader of the party with the most seats is called upon by the Lieutenant Governor of Newfoundland and Labrador to form a government and assume the position of premier Premier of Newfoundland and Labrador and Executive Council of Newfoundland and Labrador.
- [d9s5] The premier acts as Newfoundland and Labrador's head of government, while the Queen of Canada is head of state.
- [d9s6] The legislature was originally bicameral.
- [d9s7] From 1832 to 1934, it had an upper house called the Legislative Council of Newfoundland.
- [d9s8] That house was abolished in 1934.
- [d9s9] Between 1934 and Newfoundland's entry into Canadian Confederation in 1949, Newfoundland was under Commission of Government, and the General Assembly was suspended.

**d10: Newfoundland and Labrador Tankard**

- [d10s0] The Newfoundland and Labrador Tankard is the Newfoundland and Labrador provincial championship for men's curling.
- [d10s1] The tournament is run by the Newfoundland and Labrador Curling Association.
- [d10s2] The winner represents Team Newfoundland and Labrador at the Tim Hortons Brier.

## 12. 2wikimultihopqa_d764e9480bda11eba7f7acde48001122

原位置：`train` 第 102 题 · 全局第 102 题 · `sample_id: 2wikimultihopqa_d764e9480bda11eba7f7acde48001122`

Question: What is the date of death of the director of film More Deadly Than The Male?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of film More Deadly Than The Male | False | () |
| u2 | date of death of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film More Deadly Than the Male | False | [] | Robert G. Vignola | [['d8s1']] |
| u2 | date of death of {u1} | True | ['u1'] | October 25, 1953 | [['d5s0']] |

### Source documents (reference only)

**d1: Albert Thompson (footballer, born 1912)**

- [d1s0] Albert Thompson( born 1912, date of death unknown) was a Welsh footballer.

**d2: Thomas Scott (diver)**

- [d2s0] Thomas Scott( 1907- date of death unknown) was an English diver.

**d3: Theodred II (Bishop of Elmham)**

- [d3s0] Theodred II was a medieval Bishop of Elmham.
- [d3s1] The date of Theodred's consecration unknown, but the date of his death was sometime between 995 and 997.

**d4: Harry Wainwright (footballer)**

- [d4s0] Harry Wainwright( born 1899; date of death unknown) was an English footballer.

**d5: Robert G. Vignola**

- [d5s0] Robert G. Vignola( born Rocco Giuseppe Vignola, August 5, 1882 – October 25, 1953) was an Italian- born American actor, screenwriter and film director.
- [d5s1] A former stage actor, he appeared in many motion pictures produced by Kalem Company and later moved to directing, becoming one of the silent screen's most prolific directors.
- [d5s2] He also directed a handful of films in the early years of talkies but his career essentially ended in the silent era.

**d6: Peter Levin**

- [d6s0] Peter Levin is an American director of film, television and theatre.

**d7: Bill Smith (footballer, born 1897)**

- [d7s0] William Thomas Smith( born 9 April 1897, date of death unknown) was an English professional footballer.

**d8: More Deadly Than the Male**

- [d8s0] More Deadly Than The Male is a 1919 silent film comedy adventure produced by Famous Players-Lasky and released by Paramount Pictures.
- [d8s1] Robert G. Vignola directed and Ethel Clayton stars.

**d9: Ian Barry (director)**

- [d9s0] Ian Barry is an Australian director of film and TV.

**d10: Etan Boritzer**

- [d10s0] Etan Boritzer( born 1950) is an American writer of children ’s literature who is best known for his book" What is God?" first published in 1989.
- [d10s1] His best selling" What is?" illustrated children's book series on character education and difficult subjects for children is a popular teaching guide for parents, teachers and child- life professionals.
- [d10s2] Boritzer gained national critical acclaim after" What is God?" was published in 1989 although the book has caused controversy from religious fundamentalists for its universalist views.
- [d10s3] The other current books in the" What is?" series include
- [d10s4] What is Love?,
- [d10s5] What is Death?,
- [d10s6] What is Beautiful?,
- [d10s7] What is Funny?,
- [d10s8] What is Right?,
- [d10s9] What is Peace?,
- [d10s10] What is Money?,
- [d10s11] What is Dreaming?,
- [d10s12] What is a Friend?,
- [d10s13] What is True?,
- [d10s14] What is a Family?,
- [d10s15] What is a Feeling?"
- [d10s16] The series is now also translated into 15 languages.
- [d10s17] Boritzer was first published in 1963 at the age of 13 when he wrote an essay in his English class at Wade Junior High School in the Bronx, New York on the assassination of John F. Kennedy.
- [d10s18] His essay was included in a special anthology by New York City public school children compiled and published by the New York City Department of Education.
- [d10s19] Boritzer now lives in Venice, California and maintains his publishing office there also.
- [d10s20] He has helped numerous other authors to get published through" How to Get Your Book Published!" programs.
- [d10s21] Boritzer is also a yoga teacher who teaches regular classes locally and guest- teaches nationally.
- [d10s22] He is also recognized nationally as an erudite speaker on" The Teachings of the Buddha."

## 13. 2wikimultihopqa_d976e9ba085c11ebbd5cac1f6bf848b6

原位置：`train` 第 103 题 · 全局第 103 题 · `sample_id: 2wikimultihopqa_d976e9ba085c11ebbd5cac1f6bf848b6`

Question: Which film whose director is younger, The Countess Of Parma or Hold 'Em Yale (1928 Film)?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of The Countess Of Parma | False | () |
| u2 | birth date of {u1} | False | ('u1',) |
| u3 | director of Hold 'Em Yale (1928 Film) | False | () |
| u4 | birth date of {u3} | False | ('u3',) |
| u5 | which film's director is younger | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of The Countess of Parma | False | [] | Alessandro Blasetti | [['d1s0']] |
| u2 | date of birth of {u1} | False | ['u1'] | 3 July 1900 | [['d5s0']] |
| u3 | director of Hold 'Em Yale (1928 film) | False | [] | Edward H. Griffith | [['d2s0']] |
| u4 | date of birth of {u3} | False | ['u3'] | August 23, 1888 | [['d6s0']] |
| u5 | which of The Countess of Parma and Hold 'Em Yale (1928 film) has the younger director | True | ['u2', 'u4'] | The Countess of Parma | [[]] |

### Source documents (reference only)

**d1: The Countess of Parma**

- [d1s0] The Countess of Parma( Italian: La contessa di Parma) is a 1936 Italian comedy film directed by Alessandro Blasetti and starring Elisa Cegani, Antonio Centa and María Denis.
- [d1s1] Marcella, a mannequin working in a fashion store in Turin, falls in love with an Italian International football player whose aunt has just acquired the store intending to replace its reliance on French fashions with Italian designs.
- [d1s2] Blasetti later described it as his only" white telephone" film.

**d2: Hold 'Em Yale (1928 film)**

- [d2s0] Hold' Em Yale, alternately known as At Yale, is a 1928 American silent comedy film directed by Edward H. Griffith and starring Rod La Rocque, Jeanette Loff, and Hugh Allan.
- [d2s1] It was adapted from the Owen Davis play of the same name, and executive- produced by Cecil B. DeMille.

**d3: The Bride of the Colorado**

- [d3s0] The Bride of the Colorado is a 1928 film starring John Boles.

**d4: Catherine of Clermont**

- [d4s0] Catherine of Clermont (French: "Catherine de Clermont"; ? – 19/20 September 1212/1213) was a medieval noble lady; the Countess of Clermont-en-Beauvaisis in her own right, whilst she was also the Countess of Blois by marriage.

**d5: Alessandro Blasetti**

- [d5s0] Alessandro Blasetti (3 July 1900 – 1 February 1987) was an Italian film director and screenwriter who influenced Italian neorealism with the film "Quattro passi fra le nuvole".
- [d5s1] Blasetti was one of the leading figures in Italian cinema during the Fascist era.
- [d5s2] He is sometimes known as the "father of Italian cinema" because of his role in reviving the struggling industry in the late 1920s.

**d6: Edward H. Griffith**

- [d6s0] Edward H. Griffith( August 23, 1888 – March 3, 1975)( also known as E H Griffith, Lieut.
- [d6s1] Edward H. Griffith, Edward Griffith, and E. H. Griffith) was an American motion picture director, screenwriter, and producer.

**d7: The Countess of Baton Rouge**

- [d7s0] The Countess of Baton Rouge is a romantic comedy film by Canadian director André Forcier, released in 1997.

**d8: The Countess of Monte Cristo (1934 film)**

- [d8s0] The Countess of Monte Cristo is a 1934 American comedy film directed by Karl Freund and starring Fay Wray, Paul Lukas and Reginald Owen.
- [d8s1] The film was a remake of a 1932 German film" The Countess of Monte Cristo".
- [d8s2] It was remade in 1948 under the same title.

**d9: Hold 'Em Jail**

- [d9s0] Hold' Em Jail is a 1932 American pre-Code comedy film starring Wheeler and Woolsey.
- [d9s1] They play a couple of boobs who are wrongfully convicted for firearm possession and sent to prison, where they somehow end up playing on the warden's football team.
- [d9s2] Rare for the duo, it's a straight comedy with no musical numbers.
- [d9s3] The title is a pun on the then- popular college cheer," Hold'em, Yale."

**d10: Antonio Fratacci**

- [d10s0] Antonio Fratacci( Parma or Bologna) was an Italian painter of the first half of the 18th century.

## 14. 2wikimultihopqa_df25d98608e111ebbda3ac1f6bf848b6 【保留新拆法｜重标人工标签】

原位置：`train` 第 104 题 · 全局第 104 题 · `sample_id: 2wikimultihopqa_df25d98608e111ebbda3ac1f6bf848b6`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_df25d98608e111ebbda3ac1f6bf848b6"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。
>
> **处理建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。
>
> **证据定位：** d3s2, d2s0, d7s0, d8s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Do director of film She Fell Among Thieves and director of film Ernest Rides Again have the same nationality?

Note:

Type: comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | nationality of director of She Fell Among Thieves | False | () |
| u2 | nationality of director of Ernest Rides Again | False | () |
| u3 | whether the directors have the same nationality | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film She Fell Among Thieves | False | [] | Clive Donner | [['d3s2']] |
| u2 | nationality of {u1} | False | ['u1'] | British | [['d2s0']] |
| u3 | director of film Ernest Rides Again | False | [] | John R. Cherry III | [['d7s0']] |
| u4 | nationality of {u3} | False | ['u3'] | American | [['d8s0']] |
| u5 | whether the directors of She Fell Among Thieves and Ernest Rides Again have the same nationality | True | ['u2', 'u4'] | no | [[]] |

### Source documents (reference only)

**d1: Hanro Smitsman**

- [d1s0] Hanro Smitsman, born in 1967 in Breda( Netherlands), is a writer and director of film and television.

**d2: Clive Donner**

- [d2s0] Clive Stanley Donner( 21 January 1926 – 6 September 2010) was a British film director who was part of the British New Wave, directing films such as" The Caretaker Nothing But the BestWhat's New Pussycat?
- [d2s1] Here We Go Round the Mulberry Bush".
- [d2s2] He also directed television movies and commercials through the mid-1990s.

**d3: She Fell Among Thieves**

- [d3s0] She Fell Among
- [d3s1] Thieves is a 1978 British television film based on the novel by Dornford Yates.
- [d3s2] It stars Malcolm McDowell and Eileen Atkins and was directed by Clive Donner.
- [d3s3] It was one of a series of television films made by the BBC and Donner which focused on British heroes between the wars, others including" Rogue Male" and" The Three Hostages".

**d4: Brian Johnson (special effects artist)**

- [d4s0] Brian Johnson( born 1939 or 1940) is a British designer and director of film and television special effects.

**d5: Ian Barry (director)**

- [d5s0] Ian Barry is an Australian director of film and TV.

**d6: Peter Levin**

- [d6s0] Peter Levin is an American director of film, television and theatre.

**d7: Ernest Rides Again**

- [d7s0] Ernest Rides Again is a 1993 American comedy film written and directed by John R. Cherry III and starring Jim Varney.
- [d7s1] It opens with the song" There Once Was A Man Named Worrell".
- [d7s2] It is the sixth film to feature the character Ernest P. Worrell, the fifth film in the Ernest series, and the last to be released theatrically.
- [d7s3] Its gross was$ 1,433,496.
- [d7s4] In this movie, Ernest and a history professor discover a long- lost Revolutionary
- [d7s5] War cannon and must protect it from others who want the precious jewels hidden inside.
- [d7s6] Its budget was$ 7,000,000.
- [d7s7] It was the first" Ernest" movie to be filmed in Vancouver, British Columbia.

**d8: John R. Cherry III**

- [d8s0] John R. Cherry III is an American film director and screenwriter, most notable for creating the character of Ernest P. Worrell.

**d9: Jason Moore (director)**

- [d9s0] Jason Moore( born October 22, 1970) is an American director of film, theatre and television.

**d10: Ben Cura**

- [d10s0] Ben Cura( born 30 September 1988) is a British- Argentine actor and director of film, television and theatre.

## 15. 2wikimultihopqa_e092ab3c0bd911eba7f7acde48001122

原位置：`train` 第 105 题 · 全局第 105 题 · `sample_id: 2wikimultihopqa_e092ab3c0bd911eba7f7acde48001122`

Question: What nationality is the performer of song Revolver (Lewis Black Ep)?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | performer of song Revolver (Lewis Black Ep) | False | () |
| u2 | nationality of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | performer of song Revolver (Lewis Black EP) | False | [] | Lewis Black | [['d5s0']] |
| u2 | nationality of {u1} | True | ['u1'] | American | [['d4s0']] |

### Source documents (reference only)

**d1: Mike Williams (singer)**

- [d1s0] Michael IX Williams is the singer of American sludge metal band Eyehategod and the former associate editor of "Metal Maniacs".
- [d1s1] He has also worked on other projects.

**d2: Bernie Bonvoisin**

- [d2s0] Bernard Bonvoisin, known as Bernie Bonvoisin( born 9 July 1956 in Nanterre, Hauts- de- Seine), is a French hard rock singer and film director.
- [d2s1] He is best known for having been the singer of Trust.
- [d2s2] He was one of the best friends of Bon Scott the singer of AC/ DC and together they recorded the song" Ride On" which was one of the last songs by Bon Scott.

**d3: Billy Milano**

- [d3s0] Billy Milano is a Bronx- born heavy metal musician now based in Austin, Texas.
- [d3s1] He is the singer and- occasionally- guitarist and bassist of crossover thrash band M.O.D., and he was also the singer of its predecessor, Stormtroopers of Death.
- [d3s2] He was also the singer of United Forces, which also featured his Stormtroopers of Death bandmate Dan Lilker.

**d4: Lewis Black**

- [d4s0] Lewis Niles Black (born August 30, 1948) is an American stand-up comedian, author, playwright, social critic and actor.
- [d4s1] He is best known for his angry demeanour and belligerent comedic style, in which he often simulates having a mental breakdown.
- [d4s2] His comedy routines often escalate into angry rants about history, politics, religion, or any other cultural trends.
- [d4s3] He hosted the Comedy Central series "Lewis Black's Root of All Evil" and makes regular appearances on "The Daily Show with Trevor Noah" delivering his "Back in Black" commentary segment, which he has been doing since "
- [d4s4] The Daily Show" was hosted by Craig Kilborn.
- [d4s5] When not on the road performing, Black resides in Manhattan, but also maintains a residence in Chapel Hill, North Carolina.
- [d4s6] He is also a spokesman for the Aruba Tourism Authority, appearing in television ads that first aired in late 2009 and 2010, as well as the voice of Anger in 2015's Pixar film, "Inside Out".
- [d4s7] He was voted 51st of the 100 greatest stand-up comedians of all time by Comedy Central in 2004; he was voted 5th in Comedy Central's Stand Up Showdown in 2008 and 11th in 2010.
- [d4s8] Black has served as an "ambassador for voting rights" for the American Civil Liberties Union, since 2013.

**d5: Revolver (Lewis Black EP)**

- [d5s0] Revolver is an EP of outtakes made during the recording sessions of Lewis Black's first album, "The White Album".
- [d5s1] The title is a reference to the album Revolver by the Beatles.
- [d5s2] This was done to acknowledge the fact that these were outtakes and different edits from the sessions of Black's earlier release.

**d6: Astrid North**

- [d6s0] Astrid North( Astrid Karina North Radmann; 24 August 1973, Berlin – 25 June 2019, Berlin) was a German soul singer and songwriter.
- [d6s1] She was the singer of the German band, with whom she released five Albums.
- [d6s2] As guest singer of the band she published three albums.

**d7: Chris Robinson (singer)**

- [d7s0] Christopher Mark Robinson( born December 20, 1966) is an American musician.
- [d7s1] He is the singer of the rock and roll band
- [d7s2] The Black Crowes, is the brother of its guitarist Rich Robinson, and is the vocalist and rhythm guitarist for the Chris Robinson Brotherhood

**d8: Dáithí Sproule**

- [d8s0] Dáithí Sproule( born 23 May 1950) is a guitarist and singer of traditional Irish music.
- [d8s1] His niece is the singer Claire Sproule.

**d9: Caspar Babypants**

- [d9s0] Caspar Babypants is the stage name of children's music artist Chris Ballew, who is also widely known as the singer of The Presidents of the United States of America.

**d10: Kristian Leontiou**

- [d10s0] Kristian Leontiou (born February 1982) is a British singer of Greek Cypriot descent, and is the singer for the indie rock band One eskimO.

## 16. 2wikimultihopqa_e1675412087411ebbd67ac1f6bf848b6

原位置：`train` 第 106 题 · 全局第 106 题 · `sample_id: 2wikimultihopqa_e1675412087411ebbd67ac1f6bf848b6`

Question: Are both movies, Balala The Fairies: The Movie and Swedenhielms, from the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of Balala The Fairies: The Movie | False | () |
| u2 | country of Swedenhielms | False | () |
| u3 | whether both movies are from the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country of origin of Balala the Fairies: The Movie | False | [] | China | [['d10s0']] |
| u2 | country of origin of Swedenhielms | False | [] | Sweden | [['d7s0']] |
| u3 | whether Balala the Fairies: The Movie and Swedenhielms are from the same country | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Kumari (1977 film)**

- [d1s0] Kumari was the first Eastman color Nepali film released in 1977.
- [d1s1] The movie was made on the story of the popular author Bijaya Bahadur Malla.
- [d1s2] Prem Bahadur Basnet wrote the script of the movie and Pradip Rimal wrote the dialogues.
- [d1s3] The subject of the movie is based up on indigenous Newar community.

**d2: Konjiki no Gash Bell!! Movie 2: Attack of the Mecha-Vulcan**

- [d2s0] Discotek Media released both movies on Blu-ray and DVD for the first time in North America on March 27, 2018.

**d3: Pokémon the Movie: Genesect and the Legend Awakened**

- [d3s0] Pokémon the Movie: Genesect and the Legend Awakened, originally released in Japan as is a 2013 Japanese anime film directed by Kunihiko Yuyama.
- [d3s1] It is the 16th" Pokémon" anime movie and the third and the final arc of the Best Wishes series.
- [d3s2] The movie premiered in theaters on July 13, 2013.
- [d3s3] The movie features Genesect, the Paleozoic and final Pokémon in the fifth generation, as well as Mewtwo.
- [d3s4] The events of the film take place during the 16th season of.
- [d3s5] The film was shown on Cartoon Network in the United States on October 19, 2013.
- [d3s6] It was also shown on CITV in the United Kingdom on October 19, 2013 after Media Factory's retirement of the" Pokémon" products on October 1, 2013.
- [d3s7] The film was also shown in the Philippines starting on November 13, 2013, exclusively in SM Cinemas.
- [d3s8] On December 3, 2013, Viz Media released the movie on DVD in the U.S before the movie released on DVD and Blu-ray in Japan on December 18, 2013.

**d4: Balala the Fairies: Princess Camellia**

- [d4s0] Balala the Fairies: Princess Camellia is a 2015 Chinese fantasy adventure film directed by Chen Cheng and starring Zhao Yue and Dai Meng of SNH48, Zhao Jinmai, Daisy Waite and Xinel Simpson.
- [d4s1] It's the third film in the" Balala the Fairies" film series, following 2014's.
- [d4s2] It was released in China on October 1, 2015.

**d5: Balala the Fairies: The Magic Trial**

- [d5s0] Balala the Fairies: The Magic Trial( Chinese: 巴啦啦小魔仙之魔法的考驗), is a 2014 Chinese children's fantasy adventure film directed by Ren Yu and Hao Lui.
- [d5s1] It was released in China on 23 January.
- [d5s2] It is a live- action film adaptation of an animated magical girl series of the same name created by Guangzhou Toy company Auldey.
- [d5s3] It's the second film in the" Balala the Fairies" film series, following 2013's.
- [d5s4] It was followed by 2015's.

**d6: Allez, Eddy**

- [d6s0] Allez, Eddy!, translated as" Go, Eddy!", is a Belgian movie and long feature film debut of director Gert Embrechts.
- [d6s1] The movie was released in 2012.

**d7: Swedenhielms**

- [d7s0] Swedenhielms is a 1935 Swedish comedy-drama film directed by Gustaf Molander.
- [d7s1] The film is based on the play by Hjalmar Bergman from 1923 and starrs Gösta Ekman, Karin Swanström, and Tutta Rolf.

**d8: The Canary Effect**

- [d8s0] The Canary Effect is a 2006 documentary film that looks into the effects that the United States and its policies have on the Indigenous peoples (Native Americans) who are residents.
- [d8s1] It premiered at the Tribeca Film Festival and won the Stanley Kubrick Award at the 2006 Traverse City Film Festival (Michael Moore hosts).
- [d8s2] The movie was directed by Robin Davey and Yellow Thunder Woman, who are both members of LA Based alternative pop group The Bastard Fairies.
- [d8s3] The documentary was released on DVD in 2008.

**d9: Rustum (2019 film)**

- [d9s0] Rustum is a 2019 Indian Kannada- language action crime thriller film directed by Ravi Varma in his directorial debut.
- [d9s1] It was produced by Jayanna and Bhogendra under the banner of Jayanna Combines.
- [d9s2] The film features Shiva Rajkumar, Vivek Oberoi, Shraddha Srinath, Rachita Ram and Mayuri Kyatari in the lead roles.
- [d9s3] The movie was the Kannada debut of Vivek Oberoi, J. Mahendran and Harish Uthaman.
- [d9s4] This is the first Kannada movie to be set in Bihar for a large part of the movie.
- [d9s5] The movie was also noted to have a large portion of the second half of the movie in Hindi.
- [d9s6] A sequel to the movie was announced after the movie became a success.

**d10: Balala the Fairies: the Movie**

- [d10s0] Balala the Fairies: the Movie is a 2013 Chinese adventure film produced by Guangdong Alpha Animation and Culture Co., Ltd.
- [d10s1] It is a live- action film adaptation of Balala the Fairies, an animated magical girl series of the same name created by Guangzhou toy company Alpha Group Co., Ltd..
- [d10s2] It was followed by 2014's and 2015's.

## 17. 2wikimultihopqa_e43338b108aa11ebbd80ac1f6bf848b6

原位置：`train` 第 107 题 · 全局第 107 题 · `sample_id: 2wikimultihopqa_e43338b108aa11ebbd80ac1f6bf848b6`

Question: Are both schools, Sri Jayawardenepura Maha Vidyalaya and V Gymnasium, located in the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of Sri Jayawardenepura Maha Vidyalaya | False | () |
| u2 | country of V Gymnasium | False | () |
| u3 | whether both schools are located in the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country where Sri Jayawardenepura Maha Vidyalaya is located | False | [] | Sri Lanka | [['d5s0']] |
| u2 | country where V Gymnasium is located | False | [] | Croatia | [['d7s0']] |
| u3 | whether Sri Jayawardenepura Maha Vidyalaya and V Gymnasium are located in the same country | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Yasodara Devi Balika Maha Vidyalaya**

- [d1s0] Yasodara Devi Balika Maha Vidyalaya is a girls' school located in Gampaha district in Sri Lanka.

**d2: Gymnázium Andreja Vrábla Levice**

- [d2s0] Gymnázium Andreja Vrábla Levice is a gymnasium located in Levice, Slovakia.
- [d2s1] It was named after Andrej Vrábel( 1910 – 1991), a Slovak math teacher.

**d3: Gymnazium Andreja Vrabla**

- [d3s0] Gymnazium Andreja Vrabla is a gymnasium located in Levice, Slovakia.
- [d3s1] It was named after Andrej Vrábel( 1910 – 1991), a Slovak math teacher.

**d4: Hewavitharana Maha Vidyalaya**

- [d4s0] Hewavitharana Maha Vidyalaya is a mixed school in Sri Lanka, located in Rajagiriya.
- [d4s1] Hewavitharana Maha Vidyalaya has two sections: the Primary section, serving students from Grade 1 to Grade 5, and the Secondary section, serving students from Grade 6 to Grade 13.

**d5: Sri Jayawardenepura Maha Vidyalaya**

- [d5s0] Sri Jayawardenepura Maha Vidyalaya is a government school in Kotte, Sri Lanka.

**d6: Akuressa Maha Vidyalaya**

- [d6s0] Akuressa Maha Vidyalaya is a mix school in Sri Lanka, located in Matara district.
- [d6s1] Though it was originally a Buddhist school, now it is run by the Government of Sri Lanka as a Provincial School.
- [d6s2] Akuressa Maha Vidyalaya has two sections- the Primary section, serves students from Grade 1 to Grade 5 and the Secondary section, serves students from Grade 6 to Grade 13.

**d7: V Gymnasium**

- [d7s0] The Fifth Gymnasium is a high school in Zagreb, Croatia specialising in science and mathematics.
- [d7s1] It opened its doors on 7 November 1938.
- [d7s2] Today it has about 900 students in 28 classes.
- [d7s3] Students have taken part in the International Mathematical Olympiad and the International Chemistry Olympiad, where they have received various medals, and also the International Physics Olympiad.

**d8: Vigneshwara Maha Vidyalaya**

- [d8s0] Vigneshwara Maha Vidyalaya is a school in Trincomalee, founded in 1823 as a primary school by the Methodist church.
- [d8s1] It was upgraded to a Maha Vidiyalayam in 1979 and 1C grade school in 1981.
- [d8s2] Vikneshwara Maha Vidyalaya is located on the main street of the town of Trincomalee.

**d9: Jamaliya Muslim Maha Vidyalaya**

- [d9s0] Jamaliya Muslim Maha Vidyalaya is a school in Batagolladeniya in the district of Kandy in Sri Lanka.

**d10: Kularathna Maha Vidyalaya**

- [d10s0] Kulrathna Maha Vidyalaya also known as P. De S. Kularathna Vidyalaya is a mixed school in Ambalangoda, Sri Lanka.
- [d10s1] The school was established in 1986 by Dayawansha Ginige who was the founder principal of the school.
- [d10s2] The school is named after the famous Sri Lankan educationist Patrick de Silva Kularatne.
- [d10s3] Presently Kulrathna Maha Vidyalaya provides primary and secondary education to a student population of over 3000.

## 18. 2wikimultihopqa_e436d0220bdb11eba7f7acde48001122

原位置：`train` 第 108 题 · 全局第 108 题 · `sample_id: 2wikimultihopqa_e436d0220bdb11eba7f7acde48001122`

Question: Who is the spouse of the director of film Lord Of The Manor (Film)?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of film Lord Of The Manor (Film) | False | () |
| u2 | spouse of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Lord of the Manor | False | [] | Henry Edwards | [['d3s0']] |
| u2 | spouse of {u1} | True | ['u1'] | Chrissie White | [['d1s3']] |

### Source documents (reference only)

**d1: Henry Edwards (actor)**

- [d1s0] Henry Edwards (18 September 1882 – 2 November 1952) was an English actor and film director.
- [d1s1] He appeared in 81 films between 1915 and 1952.
- [d1s2] He also directed 67 films between 1915 and 1937.
- [d1s3] Edwards was married to actress Chrissie White, who co-starred in a number of his films.
- [d1s4] He was born in Weston-super-Mare, Somerset and died in Chobham, Surrey.

**d2: Gertrude of Bavaria**

- [d2s0] Gertrude of Saxony and Bavaria( 1152/55–1197) was Duchess of Swabia as the spouse of Duke Frederick IV, and Queen of Denmark as the spouse of King Canute VI.

**d3: Lord of the Manor (film)**

- [d3s0] Lord of the Manor is a 1933 British comedy film directed by Henry Edwards and starring Betty Stockfeld, Frederick Kerr and Henry Wilcoxon.
- [d3s1] It was based on a play by John Hastings Turner.
- [d3s2] It was made at Elstree Studios as a quota film for release by Paramount Pictures.
- [d3s3] The film's sets were designed by Wilfred Arnold.

**d4: Maria Teresa, Grand Duchess of Luxembourg**

- [d4s0] Maria Teresa, Grand Duchess of Luxembourg( born María Teresa Mestre y Batista; on 22 March 1956), is the spouse of Grand Duke Henri.

**d5: Adib Kheir**

- [d5s0] Adib Kheir was a leading Syrian nationalist of the 1920s.
- [d5s1] He was the owner of the Librairie Universelle in Damascus.
- [d5s2] His granddaughter is the spouse of Manaf Tlass.

**d6: Marie-Louise Coidavid**

- [d6s0] Marie Louise Coidavid( 1778 – March 11, 1851), was the Queen of the Kingdom of Haiti 1811 – 20 as the spouse of Henri I of Haiti.

**d7: Mehdi Abrishamchi**

- [d7s0] Mehdi Abrishamchi is an Iranian People's Mujahedin of Iran( MEK) politician who has been described as" the right hand man of Massoud Rajavi".
- [d7s1] He is the former spouse of the group's current leader, Maryam Rajavi, whom he divorced so that she could become the spouse of Massoud Rajavi.

**d8: Jamie Scott Gordon**

- [d8s0] Jamie Scott Gordon is a Scottish actor and writer known for the 2013 horror film" Lord of Tears".
- [d8s1] He is active with the theater project The Village Pub Theatre.

**d9: Sophia Magdalena of Denmark**

- [d9s0] Sophia Magdalena of Denmark (3 July 1746 – 21 August 1813) was Queen of Sweden as the spouse of King Gustav III.

**d10: Robert Basset**

- [d10s0] Sir Robert Basset( 1573- 1641), lord of the manor of Umberleigh and lord of the manor of Heanton Punchardon in Devon, England, was MP for Plymouth in 1593.

## 19. 2wikimultihopqa_e450a7ca08c211ebbd8cac1f6bf848b6

原位置：`train` 第 109 题 · 全局第 109 题 · `sample_id: 2wikimultihopqa_e450a7ca08c211ebbd8cac1f6bf848b6`

Question: Which film has the director who died first, Flirting With Love or Strait-Jacket?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of Flirting With Love | False | () |
| u2 | death date of {u1} | False | ('u1',) |
| u3 | director of Strait-Jacket | False | () |
| u4 | death date of {u3} | False | ('u3',) |
| u5 | which film's director died first | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of Flirting with Love | False | [] | John Francis Dillon | [['d6s0']] |
| u2 | date of death of {u1} | False | ['u1'] | April 4, 1934 | [['d10s0']] |
| u3 | director of Strait-Jacket | False | [] | William Castle | [['d1s1']] |
| u4 | date of death of {u3} | False | ['u3'] | May 31, 1977 | [['d9s0']] |
| u5 | which of Flirting with Love and Strait-Jacket has the director who died first | True | ['u2', 'u4'] | Flirting with Love | [[]] |

### Source documents (reference only)

**d1: Strait-Jacket**

- [d1s0] Strait- Jacket is a 1964 American horror- thriller film starring Joan Crawford and Diane Baker in a macabre mother and daughter tale about a series of axe-murders.
- [d1s1] Released by Columbia Pictures, the film was directed and produced by William Castle, and co-produced by Dona Holloway.
- [d1s2] The screenplay was the first of two written for Castle by Robert Bloch, the second being" The Night Walker"( 1964).
- [d1s3] " Strait- Jacket" marks the first big- screen appearance of Lee Majors in the uncredited role of Crawford's husband.
- [d1s4] The film's plot makes use of the psychological abuse method known as gaslighting.

**d2: Ben Palmer**

- [d2s0] Ben Palmer is a British film and television director who is known for being the director of" Bo' Selecta" and" The Inbetweeners".

**d3: G. Marthandan**

- [d3s0] G. Marthandan is an Indian film director who works in Malayalam cinema.

**d4: Drew Esocoff**

- [d4s0] Drew Esocoff( born c. 1957) is an American television sports director, who as of 2006 has been the director of NBC Sunday Night Football.

**d5: Abhishek Saxena**

- [d5s0] Abhishek Saxena is an Indian Bollywood and Punjabi film director who directed the movie Phullu.
- [d5s1] The Phullu movie was released in theaters on 16 June 2017, in which film Sharib Hashmi is the lead role.
- [d5s2] Apart from these, he has also directed Patiala Dreamz, this is a Punjabi film.
- [d5s3] This film was screened in cinemas in 2014.

**d6: Flirting with Love**

- [d6s0] Flirting with Love is a 1924 American silent drama film directed by John Francis Dillon and starring Colleen Moore, Conway Tearle and Winifred Bryson.

**d7: At War with Love**

- [d7s0] At War with Love is a 2016 Italian comedy film directed by Pif.

**d8: Flirting with Anthony**

- [d8s0] Flirting with Anthony is a 2005 released film written and directed by Christian Calson.

**d9: William Castle**

- [d9s0] William Castle( April 24, 1914 – May 31, 1977) was an American film director, producer, screenwriter, and actor.
- [d9s1] Orphaned at 11, Castle dropped out of high school at 15 to work in the theater.
- [d9s2] He came to the attention of Columbia Pictures for his talent for promotion and was hired.
- [d9s3] He learned the trade of filmmaking and became a director, acquiring a reputation for the ability to churn out competent B-movies quickly and on budget.
- [d9s4] He eventually struck out on his own, producing and directing thrillers, which, despite their low budgets, were effectively promoted with gimmicks, a trademark for which he is best known.
- [d9s5] He was also the producer for" Rosemary's Baby".

**d10: John Francis Dillon (director)**

- [d10s0] John Francis Dillon (July 13, 1884 – April 4, 1934) was an American film director and actor of the silent era.
- [d10s1] He directed 130 films between 1914 and 1934.
- [d10s2] He also appeared in 74 films between 1914 and 1931.
- [d10s3] He was born in New York, New York, was a brother of Robert A. Dillon, and died in Los Angeles, California from a heart attack.

## 20. 2wikimultihopqa_e4e452ca087411ebbd67ac1f6bf848b6

原位置：`train` 第 110 题 · 全局第 110 题 · `sample_id: 2wikimultihopqa_e4e452ca087411ebbd67ac1f6bf848b6`

Question: Which film whose director is younger, The Right Connections or Stocks And Blondes?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of The Right Connections | False | () |
| u2 | birth date of {u1} | False | ('u1',) |
| u3 | director of Stocks And Blondes | False | () |
| u4 | birth date of {u3} | False | ('u3',) |
| u5 | which film's director is younger | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film The Right Connections | False | [] | Chuck Vinson | [['d2s0']] |
| u2 | date of birth of {u1} | False | ['u1'] | July 14, 1956 | [['d4s0']] |
| u3 | director of film Stocks and Blondes | False | [] | Dudley Murphy | [['d8s0']] |
| u4 | date of birth of {u3} | False | ['u3'] | July 10, 1897 | [['d5s0'], ['d5s1']] |
| u5 | which of The Right Connections and Stocks and Blondes has the younger director | True | ['u2', 'u4'] | The Right Connections | [[]] |

### Source documents (reference only)

**d1: Miloš Zličić**

- [d1s0] Miloš Zličić( born 29 December 1999) is a Serbian football forward.
- [d1s1] He is a younger brother of Lazar Zličić.

**d2: The Right Connections**

- [d2s0] The Right Connections is a 1997 television film directed by Chuck Vinson and starring Melissa Joan Hart and her four real life siblings.

**d3: La Bestia humana**

- [d3s0] La Bestia humana is a 1957 Argentine film whose story is based on the novel" La Bête Humaine" by the French writer Émile Zola.

**d4: Chuck Vinson**

- [d4s0] Chuck Rallen Vinson( born July 14, 1956 in Elkhart, Indiana) is an American television director and producer.

**d5: Dudley Murphy**

- [d5s0] Dudley Murphy( July 10, 1897 – February 22, 1968) was an American film director.
- [d5s1] Murphy was born on July 10, 1897 in Winchester, Massachusetts, to the artists Caroline Hutchinson( Bowles) Murphy( 1868- 1923) and Hermann Dudley Murphy( 1867- 1945, and whom his son was named for), both accomplished Modernist landscape painters.
- [d5s2] After first finding work as a journalist, Dudley Murphy began making films in the early 1920s.
- [d5s3] In his first short film," Soul of the Cypress"( 1921), a variation on the Orpheus myth, the film's protagonist falls in love with a dryad( a wood nymph whose soul dwells in an ancient tree) and throws himself into the sea to become immortal and spend eternity with her.
- [d5s4] Murphy's then- wife Chase Harringdine played the dryad.
- [d5s5] Murphy followed this with" Danse Macabre"( 1922) featuring Adolph Bolm, Olin Howland, and Ruth Page.
- [d5s6] Both of these early films are in the DVD collection issued in October 2005( see link below).
- [d5s7] Murphy's eighth film," Ballet mécanique", which he co-directed with the French artist Fernand Léger, premiered on 24 September 1924 at the Internationale Ausstellung neuer Theatertechnik( International Exposition for New Theater Technique) in Vienna.
- [d5s8] Considered one of the masterpieces of early experimental filmmaking," Ballet mécanique" also included creative input from Man Ray and Ezra Pound, and was presented at the exposition by Frederick Kiesler.
- [d5s9] The film was scheduled to be screened with George Antheil's masterpiece of the same name.
- [d5s10] However, the music ran close to 30 minutes, while the film was 17 minutes long.
- [d5s11] In 2000, Paul Lehrman produced a married print of the film.
- [d5s12] In her book" Dudley Murphy: Hollywood Wild Card", film historian Susan Delson argues persuasively that Murphy was the film's driving force but that Léger was more successful at promoting the film as his own creation.
- [d5s13] " Ballet mécanique", with the George Antheil music originally written for the film, was included in the DVD collection released in October 2005.
- [d5s14] In addition to" Ballet mécanique", Murphy is best remembered for" St. Louis Blues"( 1929) with Bessie Smith and Jimmy Mordecai," Black and Tan"( 1929) with Duke Ellington and His Orchestra," Confessions of a Co- Ed"( 1931)," The Sport Parade"( 1932) with Joel McCrea, and" The Emperor Jones"( 1933), starring Paul Robeson.
- [d5s15] In 1932, Murphy helped introduce the Mexican artist David Alfaro Siqueiros to prominent people in the Los Angeles community.
- [d5s16] To show his gratitude, Siqueiros painted a mural on a wall in Murphy's Pacific Palisades home.
- [d5s17] The only intact mural by Siqueiros in the United States," Portrait of Mexico Today" was donated anonymously to the Santa Barbara Museum of Art in 1999.
- [d5s18] From the late 1940s through the 1960s Murphy and his fourth wife, Virginia, owned and operated Holiday House, an exclusive Malibu hotel designed by Richard Neutra and favored by the Hollywood elite.

**d6: Vadim Vlasov**

- [d6s0] Vadim Nikolayevich Vlasov( born 19 December 1980) is a former Russian football player.
- [d6s1] He is a younger brother of Dmitri Vlasov.

**d7: Dmitri Varfolomeyev (footballer, born 1978)**

- [d7s0] Dmitri Nikolayevich Varfolomeyev( born 15 March 1978 in Leningrad) is a former Russian football player.
- [d7s1] He is a younger brother of Sergei Varfolomeyev.

**d8: Stocks and Blondes**

- [d8s0] Stocks and Blondes is a 1928 American silent comedy film directed by Dudley Murphy and starring Gertrude Astor, Jacqueline Logan and Richard' Skeets' Gallagher.
- [d8s1] It is also known by the alternative title of Blondes and Bonds.

**d9: Wanda Whips Wall Street**

- [d9s0] Wanda Whips Wall Street( also known as Stocks and Blondes) is a 1982 pornographic film directed by Larry Revene and starring Veronica Hart.

**d10: A Fig Leaf for Eve**

- [d10s0] A Fig Leaf for Eve is a 1944 American film directed by Don Brodie.
- [d10s1] The film is also known as Desirable Lady, Flaming Girls, Hollywood Nights, Not Enough Clothes, Reckless Youth, Room for Love, and Strips and Blondes as American reissue titles.

## 21. 2wikimultihopqa_e4fbf9c1088311ebbd6dac1f6bf848b6 【待确认：语义或标签口径】

原位置：`train` 第 111 题 · 全局第 111 题 · `sample_id: 2wikimultihopqa_e4fbf9c1088311ebbd6dac1f6bf848b6`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_e4fbf9c1088311ebbd6dac1f6bf848b6"></a>

> **审阅结论：待确认：语义或标签口径**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新事实写 country of origin，旧 gold 使用国籍/国别描述。Robert G. Vignola 的证据明确是 Italian-born American，出生地与国籍口径会得出不同结论。
>
> **处理建议：** 明确本题采用 nationality/country descriptor 还是 birthplace。沿用现有 gold 时应写 nationality/country descriptor，并以 American 为值；不要把 Italian-born 当成国籍。
>
> **证据定位：** d9s0, d2s0, d1s0, d6s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Are director of film One Exciting Week and director of film The Woman God Changed both from the same country?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of film One Exciting Week | False | () |
| u2 | country of origin of {u1} | False | ('u1',) |
| u3 | director of film The Woman God Changed | False | () |
| u4 | country of origin of {u3} | False | ('u3',) |
| u5 | whether {u2} and {u4} are the same | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film One Exciting Week | False | [] | William Beaudine | [['d9s0']] |
| u2 | country descriptor of {u1} | False | ['u1'] | American | [['d2s0']] |
| u3 | director of film The Woman God Changed | False | [] | Robert G. Vignola | [['d1s0']] |
| u4 | country descriptor of {u3} | False | ['u3'] | American | [['d6s0']] |
| u5 | whether the directors of One Exciting Week and The Woman God Changed are from the same country | True | ['u2', 'u4'] | yes | [[]] |

### Source documents (reference only)

**d1: The Woman God Changed**

- [d1s0] The Woman God Changed is a 1921 American silent drama film directed by Robert G. Vignola and written by Brian Oswald Donn- Byrne and Doty Hobart.
- [d1s1] The film stars Seena Owen, E.K. Lincoln, Henry Sedley, Lillian Walker, H. Cooper Cliffe and Paul Nicholson.
- [d1s2] The film was released on July 3, 1921, by Paramount Pictures.

**d2: William Beaudine**

- [d2s0] William Washington Beaudine (January 15, 1892 – March 18, 1970) was an American film actor and director.
- [d2s1] He was one of Hollywood's most prolific directors, turning out films in remarkable numbers and in a wide variety of genres.

**d3: Jason Moore (director)**

- [d3s0] Jason Moore( born October 22, 1970) is an American director of film, theatre and television.

**d4: Ian Barry (director)**

- [d4s0] Ian Barry is an Australian director of film and TV.

**d5: Peter Levin**

- [d5s0] Peter Levin is an American director of film, television and theatre.

**d6: Robert G. Vignola**

- [d6s0] Robert G. Vignola( born Rocco Giuseppe Vignola, August 5, 1882 – October 25, 1953) was an Italian- born American actor, screenwriter and film director.
- [d6s1] A former stage actor, he appeared in many motion pictures produced by Kalem Company and later moved to directing, becoming one of the silent screen's most prolific directors.
- [d6s2] He also directed a handful of films in the early years of talkies but his career essentially ended in the silent era.

**d7: Brian Johnson (special effects artist)**

- [d7s0] Brian Johnson( born 1939 or 1940) is a British designer and director of film and television special effects.

**d8: Hanro Smitsman**

- [d8s0] Hanro Smitsman, born in 1967 in Breda( Netherlands), is a writer and director of film and television.

**d9: One Exciting Week**

- [d9s0] One Exciting Week is a 1946 American comedy film directed by William Beaudine and written by Jack Townley and John K. Butler.
- [d9s1] The film stars Al Pearce, Pinky Lee, Jerome Cowan, Shemp Howard, Arlene Harris and Mary Treen.
- [d9s2] The film was released on June 8, 1946, by Republic Pictures.

**d10: Ben Cura**

- [d10s0] Ben Cura( born 30 September 1988) is a British- Argentine actor and director of film, television and theatre.

## 22. 2wikimultihopqa_ec01ce8b08f711ebbdaaac1f6bf848b6

原位置：`train` 第 112 题 · 全局第 112 题 · `sample_id: 2wikimultihopqa_ec01ce8b08f711ebbdaaac1f6bf848b6`

Question: Who was born earlier, Faizal Yusof or Lenore Glen Offord?

Note:

Type: comparison · fallback: False · SFT snapshots: 5

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | birth date of Faizal Yusof | False | () |
| u2 | birth date of Lenore Glen Offord | False | () |
| u3 | who was born earlier | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | birth date of Faizal Yusof | False | [] | 13 June 1978 | [['d10s0']] |
| u2 | birth date of Lenore Glen Offord | False | [] | October 24, 1905 | [['d6s0']] |
| u3 | which of Faizal Yusof and Lenore Glen Offord was born earlier | True | ['u1', 'u2'] | Lenore Glen Offord | [[]] |

### Source documents (reference only)

**d1: Jeff Barlow**

- [d1s0] Jeff Barlow was a British actor who was born in Lancashire in 1871.

**d2: Huc-Mazelet Luquiens**

- [d2s0] Huc- Mazelet Luquiens( 1881 — 1961) was an American printmaker, painter and art educator who was born June 30, 1881 in Massachusetts to Jules Luquiens a French- speaking Swiss and Emma Clark who was born in Ohio.

**d3: John Veltri**

- [d3s0] John Veltri is a photographer who was born in 1938 in New Jersey.

**d4: Joël Henry (journalist)**

- [d4s0] Joël Henry( born 1955) is a French journalist who was born in Strasbourg.

**d5: Pauline Delpech**

- [d5s0] Pauline Delpech is a writer and a French actress who was born in 1981.

**d6: Lenore Glen Offord**

- [d6s0] Lenore Glen Offord( October 24, 1905 – April 24, 1991) was an American author and reviewer of detective fiction.
- [d6s1] Offord was born in Spokane, Washington and attended Mills College in Oakland, California.
- [d6s2] She graduated in 1925 with a degree in English.
- [d6s3] She attended the University of California at Berkeley the following year.
- [d6s4] Offord authored twelve books, eight of which are mysteries set in the San Francisco area.
- [d6s5] Offord was the" San Francisco Chronicle"'s mystery critic for more than thirty years, initially taking over Anthony Boucher's column during World War II.
- [d6s6] She received the Edgar Award for Outstanding Criticism in 1952.
- [d6s7] A long- time devotée of the Sherlock Holmes stories, Offord was the first female member of the Baker Street Irregulars.

**d7: Shannah Trailor**

- [d7s0] Shannah Trailor( born 1983) is an African- American author who was born in Chicago.

**d8: Evan Crooks**

- [d8s0] Evan Crooks is an American actor who was born in Fresno County, California.

**d9: Zaven Paré**

- [d9s0] Zaven Paré is a French new media artist who was born in 1961.

**d10: Faizal Yusof**

- [d10s0] Faizal Yusof( born Mohd Faizal Yusup; 13 June 19781 January 2011) was a Malaysian actor.
- [d10s1] He appeared in some Malay television series, including" Jersi 9Adamaya Tiramisu" and" Manjalara".
- [d10s2] Faizal died on 1 January 2011.
- [d10s3] He is survived by his second wife Rosmunira Rashid who was five months pregnant at the time of his death.
- [d10s4] He was previously married to singer Siti Nordiana with whom he had a son, Mohd Rayyan Nakhaie.

## 23. 2wikimultihopqa_ed17b36008b511ebbd88ac1f6bf848b6

原位置：`train` 第 113 题 · 全局第 113 题 · `sample_id: 2wikimultihopqa_ed17b36008b511ebbd88ac1f6bf848b6`

Question: Which film whose director was born first, Desperado City or Dhanak?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of Desperado City | False | () |
| u2 | birth date of {u1} | False | ('u1',) |
| u3 | director of Dhanak | False | () |
| u4 | birth date of {u3} | False | ('u3',) |
| u5 | which film's director was born first | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Desperado City | False | [] | Vadim Glowna | [['d9s0']] |
| u2 | date of birth of {u1} | False | ['u1'] | 26 September 1941 | [['d8s0']] |
| u3 | director of film Dhanak | False | [] | Nagesh Kukunoor | [['d7s0'], ['d2s9']] |
| u4 | date of birth of {u3} | False | ['u3'] | 30 March 1967 | [['d2s0']] |
| u5 | which of the two films has the director born first | True | ['u2', 'u4'] | Desperado City | [[]] |

### Source documents (reference only)

**d1: Henry Moore (cricketer)**

- [d1s0] Henry Walter Moore( 1849 – 20 August 1916) was an English- born first- class cricketer who spent most of his life in New Zealand.

**d2: Nagesh Kukunoor**

- [d2s0] Nagesh Kukunoor (born 30 March 1967) is an Indian film director, producer, screenwriter and actor known for his works predominantly in Bollywood.
- [d2s1] He is known for his works in parallel cinema, such as "Hyderabad Blues" (1998), "Rockford" (1999), "Iqbal" (2005), "Dor" (2006), "Aashayein" (2010), "Lakshmi" (2014), and "Dhanak" (2016).
- [d2s2] Kukunoor has received seven International Awards, and two National Film Awards for his works.
- [d2s3] In 2003, he directed "3 Deewarein", which was showcased among the Indian panorama section, at the 2003 International Film Festival of India.
- [d2s4] The film was also premiered at the Kolkata Film Festival.
- [d2s5] After having been screened at the Indian Film Festival of Los Angeles, where it was well received, the film was screened at the Commonwealth Festival at Manchester, it was nominated as one of the top five films, at the gala presentation.
- [d2s6] Nagesh Kukunoor has also received the Filmfare Award for Best Story.
- [d2s7] In 2006, he garnered the National Film Award for Best Film on Other Social Issues, for directing "Iqbal".
- [d2s8] In 2014, he received the Mercedes Benz Audience Award, for Best Narrative at the Palm Springs International Film Festival for "Lakshmi".
- [d2s9] In 2015 he directed the road movie, "Dhanak", which won the Crystal Bear Grand Prix for Best Children's Film, and Special Mention for the Best Feature Film by The Children's Jury for Generation Kplus at the 65th Berlin International Film Festival.
- [d2s10] The film has also garnered the Best Film Award in the main category-Children's Feature Film Competition-Cinema in Sneakers (film festival), and the Best Film Award - at the Montreal International Children's Film Festival (FIFEM).
- [d2s11] The film has garnered the National Film Award for Best Children's Film for 2016.

**d3: Ringo-en no shōjo**

- [d3s0] The art director was Tomoo Shimogawara.

**d4: Wale Adebanwi**

- [d4s0] Wale Adebanwi( born 1969) is a Nigerian- born first Black Rhodes Professor at St Antony's College, Oxford.

**d5: Deepak Sareen**

- [d5s0] Deepak Sareen is a Bollywood film director and assistant director.
- [d5s1] His first film as director was" Ranbhoomi" and last film as director was" Albela".

**d6: John McMahon (Surrey and Somerset cricketer)**

- [d6s0] John William Joseph McMahon( 28 December 1917 – 8 May 2001) was an Australian- born first- class cricketer who played for Surrey and Somerset in England from 1947 to 1957.

**d7: Dhanak**

- [d7s0] Dhanak is a 2015 Indian Hindi film written and directed by Nagesh Kukunoor.
- [d7s1] Produced by Manish Mundra, Nagesh Kukunoor, and Elahe Hiptoola, the film features Hetal Gada and Krrish Chhabria as the two children, playing brother and sister, in the leading roles, with supporting performances from Chet Dixon, Vipin Sharma, Gulfam Khan, Vibha Chibber, Flora Saini, and Vijay Maurya.
- [d7s2] The film was released nationwide in India on 17 June 2016.
- [d7s3] The film was premiered at the 65th Berlin International Film Festival where it won the" Crystal Bear Grand Prix" for Best Children's Film, and Special Mention for the Best Feature Film by The Children's Jury for Generation Kplus.
- [d7s4] The film has also garnered the Best Film Award in the main category- Children's Feature Film Competition- Cinema in Sneakers( film festival), and the Best Film Award- at the Montreal International Children's Film Festival( FIFEM).
- [d7s5] Dhanak was also screened at the Indian Film Festival of Los Angeles, and the Toronto International Film Festival.
- [d7s6] The film has garnered Best Children's Film at the 64th National Film Awards.

**d8: Vadim Glowna**

- [d8s0] Vadim Glowna( 26 September 1941 – 24 January 2012) was a German actor and film director.
- [d8s1] Since 1964 he appeared in more than 150 films and television shows.
- [d8s2] He directed the 1983 film" Dies rigorose Leben", which won an Honourable Mention at the 33rd Berlin International Film Festival.
- [d8s3] In 1989, he was a member of the jury at the 39th Berlin International Film Festival.
- [d8s4] Three years later, his film" Rising to the Bait" was entered into the 42nd Berlin International Film Festival.

**d9: Desperado City**

- [d9s0] Desperado City is a 1981 West German drama film written and directed by Vadim Glowna.
- [d9s1] It won the Caméra d'Or at the 1981 Cannes Film Festival.

**d10: Hartley Lobban**

- [d10s0] Hartley W Lobban (9 May 1926 – 15 October 2004) was a Jamaican-born first-class cricketer who played 17 matches for Worcestershire in the early 1950s.

## 24. 2wikimultihopqa_ed90d08c0bdb11eba7f7acde48001122

原位置：`train` 第 114 题 · 全局第 114 题 · `sample_id: 2wikimultihopqa_ed90d08c0bdb11eba7f7acde48001122`

Question: What is the date of birth of the director of film Fiend (Film)?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of film Fiend (Film) | False | () |
| u2 | date of birth of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Fiend | False | [] | Don Dohler | [['d2s0']] |
| u2 | date of birth of {u1} | True | ['u1'] | January 27, 1946 | [['d10s0']] |

### Source documents (reference only)

**d1: Les Richards**

- [d1s0] Les Richards( date of birth unknown) was an Australian rules footballer who played with North Melbourne in the Victorian Football League( VFL).

**d2: Fiend (film)**

- [d2s0] Fiend is a 1980 American B movie science fiction horror film directed and written by low-budget filmmaker Don Dohler, shot in Perry Hall, Maryland and starring Don Leifert, Elaine White, Richard Nelson, and George Stover.
- [d2s1] The film had U.S. theatrical release in September 1980.

**d3: Terence Robinson**

- [d3s0] Terence D. Robinson( date of birth and death unknown) was a male wrestler who competed for England.

**d4: Peter Levin**

- [d4s0] Peter Levin is an American director of film, television and theatre.

**d5: Pamela Jain**

- [d5s0] Pamela Jain is an Indian playback singer.
- [d5s1] Date of Birth:16th March.

**d6: Theodred II (Bishop of Elmham)**

- [d6s0] Theodred II was a medieval Bishop of Elmham.
- [d6s1] The date of Theodred's consecration unknown, but the date of his death was sometime between 995 and 997.

**d7: Ian Barry (director)**

- [d7s0] Ian Barry is an Australian director of film and TV.

**d8: Brian Saunders (weightlifter)**

- [d8s0] Brian Saunders( date of birth and death unknown) was a male weightlifter who competed for England.

**d9: Etan Boritzer**

- [d9s0] Etan Boritzer( born 1950) is an American writer of children ’s literature who is best known for his book" What is God?" first published in 1989.
- [d9s1] His best selling" What is?" illustrated children's book series on character education and difficult subjects for children is a popular teaching guide for parents, teachers and child- life professionals.
- [d9s2] Boritzer gained national critical acclaim after" What is God?" was published in 1989 although the book has caused controversy from religious fundamentalists for its universalist views.
- [d9s3] The other current books in the" What is?" series include
- [d9s4] What is Love?,
- [d9s5] What is Death?,
- [d9s6] What is Beautiful?,
- [d9s7] What is Funny?,
- [d9s8] What is Right?,
- [d9s9] What is Peace?,
- [d9s10] What is Money?,
- [d9s11] What is Dreaming?,
- [d9s12] What is a Friend?,
- [d9s13] What is True?,
- [d9s14] What is a Family?,
- [d9s15] What is a Feeling?"
- [d9s16] The series is now also translated into 15 languages.
- [d9s17] Boritzer was first published in 1963 at the age of 13 when he wrote an essay in his English class at Wade Junior High School in the Bronx, New York on the assassination of John F. Kennedy.
- [d9s18] His essay was included in a special anthology by New York City public school children compiled and published by the New York City Department of Education.
- [d9s19] Boritzer now lives in Venice, California and maintains his publishing office there also.
- [d9s20] He has helped numerous other authors to get published through" How to Get Your Book Published!" programs.
- [d9s21] Boritzer is also a yoga teacher who teaches regular classes locally and guest- teaches nationally.
- [d9s22] He is also recognized nationally as an erudite speaker on" The Teachings of the Buddha."

**d10: Don Dohler**

- [d10s0] Donald Michael "Don" Dohler (January 27, 1946 – December 2, 2006) was an American film director known for making low-budget science fiction and horror films, as well as work in underground comix and publishing.

## 25. 2wikimultihopqa_ef3a400a087811ebbd67ac1f6bf848b6 【保留新拆法｜重标人工标签】

原位置：`train` 第 115 题 · 全局第 115 题 · `sample_id: 2wikimultihopqa_ef3a400a087811ebbd67ac1f6bf848b6`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_ef3a400a087811ebbd67ac1f6bf848b6"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。
>
> **处理建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。
>
> **证据定位：** d6s0, d2s0, d9s0, d8s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Do both Itty Bitty Titty Committee and Desperate Journey films have the directors from the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of director of Itty Bitty Titty Committee | False | () |
| u2 | country of director of Desperate Journey | False | () |
| u3 | whether directors of Itty Bitty Titty Committee and Desperate Journey are from the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Itty Bitty Titty Committee | False | [] | Jamie Babbit | [['d6s0']] |
| u2 | nationality of {u1} | False | ['u1'] | American | [['d2s0']] |
| u3 | director of film Desperate Journey | False | [] | Raoul Walsh | [['d9s0']] |
| u4 | nationality of {u3} | False | ['u3'] | American | [['d8s0']] |
| u5 | whether the directors of Itty Bitty Titty Committee and Desperate Journey share the same nationality | True | ['u2', 'u4'] | yes | [[]] |

### Source documents (reference only)

**d1: Charles K. Gifford**

- [d1s0] Charles K. Gifford is an American banker and businessman.
- [d1s1] He is the chairman emeritus of Bank of America having served on its board of directors from 2004 to 2016.

**d2: Jamie Babbit**

- [d2s0] Jamie Merill Babbit( born November 16, 1970) is an American film director, producer and screenwriter.
- [d2s1] She directed the films" But I'm a Cheerleader The Quiet" and" Itty Bitty Titty Committee".
- [d2s2] She has also directed episodes of television programs including" Russian DollGilmore GirlsMalcolm in the MiddleUnited States of TaraLooking Nip/ Tuck The L WordSilicon Valley", and" The Marvelous Mrs. Maisel".

**d3: Montana (1950 film)**

- [d3s0] Montana is a 1950 American Technicolor Western film directed by Ray Enright and starring Errol Flynn.
- [d3s1] It was only the second time Flynn played an Australian on screen, the first time being" Desperate Journey"( 1942).
- [d3s2] The film was Flynn's fourth and final pairing with frequent co-star Alexis Smith.

**d4: Andrea Sperling**

- [d4s0] Andrea Sperling( born c. 1968/69) is an independent film producer based in Los Angeles.
- [d4s1] The films she has produced include" Totally Fucked Up But I'm a CheerleaderD.E.B.S." and" Itty Bitty Titty Committee" and the Sundance Top Prize winning" Like Crazy".

**d5: Deak Evgenikos**

- [d5s0] Deak Evgenikos is an American actress originally from New Jersey.
- [d5s1] date of birth December 13, 1977.
- [d5s2] She is best known for her role in Jamie Babbit's film Itty Bitty Titty Committee, a girl- powered romantic comedy that explores themes such as lesbianism and female empowerment.
- [d5s3] Evgenikos graduated from Sarah Lawrence College before beginning her acting career, starring in Guinevere Turner's short film" Hummer" in 2003.
- [d5s4] She appeared in the films" Frozen Smile" and" Hung" in 2005 before being cast in the role of Meat in Itty Bitty Titty Committee.
- [d5s5] Go Magazine listed her as one of its" 100 Women We Love."

**d6: Itty Bitty Titty Committee**

- [d6s0] Itty Bitty Titty Committee is a feminist, lesbian comedy film directed by Jamie Babbit.
- [d6s1] It was released on September 28, 2007.
- [d6s2] The film had its premiere at the international film festival Berlinale on February 9, 2007, where it was nominated for a Teddy Award for Best Feature.
- [d6s3] It had its American premiere at SXSW in March where it won the Jury Prize for Best Feature.
- [d6s4] The film was produced by non-profit organization POWER UP.

**d7: Robert Stone (director)**

- [d7s0] Robert Stone is a British- American documentary filmmaker.
- [d7s1] His work has been screened at dozens of film festivals and televised around the world, notably seven of his films have appeared on PBS's" American Experience" series and four of his films have premiered at the Sundance Film Festival( including Closing Night Film in 2009).

**d8: Raoul Walsh**

- [d8s0] Raoul A. Walsh( March 11, 1887 December 31, 1980) was an American film director, actor, founding member of the Academy of Motion Picture Arts and Sciences( AMPAS) and the brother of the silent screen actor George Walsh.
- [d8s1] He was known for portraying John Wilkes Booth in the silent classic" The Birth of a Nation"( 1915) and for directing such films as" The Big Trail"( 1930), starring John Wayne," High Sierra"( 1941), starring Ida Lupino and Humphrey Bogart; and" White Heat"( 1949), starring James Cagney and Edmond O'Brien.
- [d8s2] He directed his last film in 1964.

**d9: Desperate Journey**

- [d9s0] Desperate Journey is a 1942 American World War II action and aviation film directed by Raoul Walsh and starring Errol Flynn and Ronald Reagan.
- [d9s1] The supporting cast includes Raymond Massey, Alan Hale Sr., and Arthur Kennedy.
- [d9s2] The melodramatic film featured a group of downed Allied airmen making their way out of the Third Reich, often with their fists.
- [d9s3] Director Raoul Walsh called it "a war comedy spiced with enough tragedy to give it reality... beyond doubt the forerunner for "Hogan's Heroes

**d10: Joel Michaely**

- [d10s0] Joel Michaely is an American actor and film producer.
- [d10s1] He has appeared in such films as" Ca n't Hardly Wait But I'm a Cheerleader Ghost World The Rules of AttractionKiss Kiss Bang BangCruel WorldFactory Girl" and" Itty Bitty Titty Committee".
- [d10s2] On television, Michaely has appeared in" Unhappily Ever AfterSabrina the Teenage Witch" and" Popular".
- [d10s3] He produced the 2005 film" The Quiet".

## 26. 2wikimultihopqa_efbc380a0baf11ebab90acde48001122

原位置：`train` 第 116 题 · 全局第 116 题 · `sample_id: 2wikimultihopqa_efbc380a0baf11ebab90acde48001122`

Question: Who is the paternal grandmother of Sir Robert Long, 6Th Baronet?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Sir Robert Long, 6th Baronet | False | () |
| u2 | mother of {u1}, Sir Robert Long's paternal grandmother | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Sir Robert Long, 6th Baronet | False | [] | Sir James Long, 5th Baronet | [['d1s1']] |
| u2 | mother of {u1}, Sir Robert Long's paternal grandmother | True | ['u1'] | Susan Strangways | [['d9s1']] |

### Source documents (reference only)

**d1: Sir Robert Long, 6th Baronet**

- [d1s0] Sir Robert Long, 6th Baronet (1705 – 10 February 1767) was an English politician.
- [d1s1] The only surviving son of Sir James Long, 5th Baronet and his wife Henrietta Greville, Long was baptised on 8 November 1705 at St Martin in the Fields, Westminster, London.
- [d1s2] Educated at Balliol College, Oxford, he succeeded his father as 6th Baronet on 16 March 1729, and inherited the family estates, including the manors of Draycot and Athelhampton.
- [d1s3] He was elected Member of Parliament for the rotten borough of Wootton Bassett in 1734, and for Wiltshire in 1741.
- [d1s4] He married on 29 May 1735 at Woodford, Essex, Emma Child, the daughter of Richard Tylney, 1st Earl Tylney, of Wanstead (said to be possessed of 'almost revolting wealth'), and his wife Dorothy Glynn.
- [d1s5] Sir Robert and Emma had two daughters and four sons including:
- [d1s6] Many letters written by Sir Robert to his wife are held in the Wiltshire and Swindon Record Office, and furnish a picture of a happy marriage in the eighteenth century, illustrating a genuine affection for his wife, and fatherly love for his children, with nicknames such as 'Jemmy' and 'Dolly'.
- [d1s7] He had good-natured relationships with his dependants, even going so far as choosing material for a new dress for Lady Emma's companion.
- [d1s8] Sir Robert Long died on 10 February 1767 and was buried at Draycot.
- [d1s9] His wife died on 8 March 1758.

**d2: Anne Denman**

- [d2s0] Anne Denman( 1587–1661) was born in Olde Hall, Retford, Nottinghamshire.
- [d2s1] Through a fortunate second marriage with Thomas Aylesbury, she became the grandmother of Lady Anne Hyde, Duchess of York and great- grandmother of Queen Mary II and Queen Anne.

**d3: Kaoru Hatoyama**

- [d3s0] After the elections of 2009, she became more widely known as the grandmother of Prime Minister Yukio Hatoyama and his politician brother Kunio Hatoyama.

**d4: Tjuyu**

- [d4s0] Tjuyu( sometimes transliterated as Thuya or Thuyu) was an Egyptian noblewoman and the mother of queen Tiye, and the wife of Yuya.
- [d4s1] She is the grandmother of Akhenaten, and great grandmother of Tutankhamun.

**d5: Hubba bint Hulail**

- [d5s0] Hubba bint Hulail was the grandmother of Hashim ibn' Abd Manaf, thus the great- great- great- grandmother of the Islamic" Nabī"( Prophet) Muhammad ibn Abdullah.

**d6: Hannah Arnold**

- [d6s0] Hannah Arnold, also known as Hannah Waterman King, was the grandmother of Benedict Arnolds children.

**d7: Robert M. Long**

- [d7s0] Robert M. Long was a member of the Wisconsin State Assembly.

**d8: James Tylney-Long**

- [d8s0] Sir James Tylney- Long, 7th Baronet( 1736 – 28 November 1794) was an English politician who sat in the House of Commons for 32 years from 1762 to 1794.
- [d8s1] The eldest son of Sir Robert Long, 6th Baronet and his wife Emma Child, he succeeded his father as 7th Baronet on 10 February 1767, and inherited the family estates, including the manors of Draycot( Wiltshire) and Athelhampton( Dorset).

**d9: Sir James Long, 5th Baronet**

- [d9s0] Sir James Long, 5th Baronet (1682 – 16 March 1729) was an English landowner and Tory politician who sat in the English and British House of Commons between 1695 and 1729.
- [d9s1] The son of James Long and his wife Susan Strangways, he was born at Athelhampton and baptised at Melbury House, Dorchester, Dorset in 1682.
- [d9s2] He was the grandson of Sir James Long, 2nd Baronet and brother of the celebrated Kit-Cat Club beauty Anne Long (c. 1681 – 1711).
- [d9s3] He succeeded to the baronetcy on the death of his brother Sir Giles Long, 4th Baronet, in 1698.
- [d9s4] He married Henrietta Greville on 6 June 1702 at St Martin in the Fields, Westminster, London.
- [d9s5] She was the daughter of Fulke Greville, 5th Baron Brooke and his wife Sarah Dashwood, and a descendant of the Earl of Bedford.
- [d9s6] On the death of his grandmother Lady Dorothy Long in 1710, he inherited the Draycot Estate together with Athelhampton Manor, other land in Wiltshire and Dorset, and an estate near Ripon in Yorkshire.
- [d9s7] He used the inheritance to purchase more land in Dorset, adjacent to Athelhampton, in the manors of Burleston and Southover.
- [d9s8] Long was returned as Member of Parliament for Chippenham at the 1705 English general election and again in 1708 and 1710.
- [d9s9] At the 1715 British general election, he was returned as MP for Wootton Bassett.
- [d9s10] He did not stand at the 1722 British general election but was returned as MP for Wiltshire in 1727.
- [d9s11] Long died at his London residence in Jermyn Street on 16 March 1729 from apoplexy.
- [d9s12] There were four daughters and two sons from his marriage.
- [d9s13] Four of his six children survived him, including Robert who succeeded to the baronetcy.
- [d9s14] His daughter Susanna created a scandal by marrying her mother's gardener in 1732, as noted in his diary by Viscount Perceval, (related distantly by marriage to the Longs).
- [d9s15] Lady Henrietta Long died 19 May 1765 at Bath.

**d10: Walter Long (died 1610)**

- [d10s0] Sir Walter Long (1560 or 1565? – October 1610) was an English knight and landowner, born in Wiltshire, the son of Sir Robert Long and his wife Barbara Carne.

## 27. 2wikimultihopqa_f01f570a0baf11ebab90acde48001122

原位置：`train` 第 117 题 · 全局第 117 题 · `sample_id: 2wikimultihopqa_f01f570a0baf11ebab90acde48001122`

Question: Who is the paternal grandfather of Psusennes I?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Psusennes I | False | () |
| u2 | father of {u1}, Psusennes I's paternal grandfather | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Psusennes I | False | [] | Pinedjem I | [['d4s2']] |
| u2 | father of {u1}, Psusennes I's paternal grandfather | True | ['u1'] | Piankh | [['d8s1']] |

### Source documents (reference only)

**d1: John Mackay (poet)**

- [d1s0] John Mackay( 1656–1754), known as( The Blind Piper), was a Scottish Gaelic poet and composer, and the grandfather of William Ross.

**d2: Henry Krause**

- [d2s0] Henry J." Red" Krause, Jr.( August 28, 1913 – February 20, 1987) was an American football offensive lineman in the National Football League for the Brooklyn Dodgers and the Washington Redskins.
- [d2s1] He played college football at St. Louis University.
- [d2s2] He is the grandfather of Jennifer Krause
- [d2s3] He is the great grandfather of Payton Hoeing

**d3: Lyon Cohen**

- [d3s0] Lyon Cohen( 1868–1937) was a Polish- born Canadian businessman and a philanthropist.
- [d3s1] He was the grandfather of singer/ poet Leonard Cohen.

**d4: Psusennes I**

- [d4s0] Psusennes I (Greek Ψουσέννης) was the third pharaoh of the 21st Dynasty who ruled from Tanis between 1047–1001 BC. "
- [d4s1] Psusennes" is the Greek version of his original name Pasibkhanu or Pasebakhaenniut (in reconstructed Late Egyptian: /pəsiwʃeʕənneːʔə/), which means "The Star Appearing in the City" while his throne name, Akheperre Setepenamun, translates as "Great are the Manifestations of Ra, chosen of Amun.
- [d4s2] " He was the son of Pinedjem I and Henuttawy, Ramesses XI's daughter by Tentamun.
- [d4s3] He married his sister Mutnedjmet.

**d5: John Westley**

- [d5s0] Rev. John Westley( 1636 – 78) was an English nonconformist minister.
- [d5s1] He was the grandfather of John Wesley( founder of Methodism).

**d6: Abd al-Muttalib**

- [d6s0] Abd al- Muttalib Shaybah ibn Hashim( c. 497 – 578) was the grandfather of Islamic prophet Muhammad.

**d7: Fred Le Deux**

- [d7s0] Frederick" Fred" Le Deux( born 4 December 1934) was an Australian rules footballer who played with Geelong in the Victorian Football League( VFL).
- [d7s1] He is the grandfather of Tom Hawkins.

**d8: Pinedjem I**

- [d8s0] Pinedjem I was the High Priest of Amun at Thebes in Ancient Egypt from 1070 to 1032 BC and the "de facto" ruler of the south of the country from 1054 BC.
- [d8s1] He was the son of the High Priest Piankh.
- [d8s2] However, many Egyptologists today believe that the succession in the Amun priesthood actually ran from Piankh to Herihor to Pinedjem I.

**d9: Zhao Shoushan**

- [d9s0] Zhao Shoushan( 12 November 1894 – 20 June 1965) was a KMT general and later Chinese Communist Party politician.
- [d9s1] He is the grandfather of Zhao Leji.

**d10: Kaya Alp**

- [d10s0] Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

## 28. 2wikimultihopqa_f05c2009099111ebbdb0ac1f6bf848b6

原位置：`train` 第 118 题 · 全局第 118 题 · `sample_id: 2wikimultihopqa_f05c2009099111ebbdb0ac1f6bf848b6`

Question: Are both villages, Pociūnai (Prienai) and Zaandijk, located in the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country where Pociūnai (Prienai) is located | False | () |
| u2 | country where Zaandijk is located | False | () |
| u3 | whether Pociūnai (Prienai) and Zaandijk are in the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country where Pociūnai (Prienai) is located | False | [] | Lithuania | [['d10s0']] |
| u2 | country where Zaandijk is located | False | [] | Netherlands | [['d7s0'], ['d3s0']] |
| u3 | whether Pociūnai (Prienai) and Zaandijk are located in the same country | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Telephone numbers in Ascension Island**

- [d1s0] Country Code:+ 247< br> International Call Prefix: 00 Ascension Island does not share the same country code( +290) with the rest of St Helena.

**d2: Élise-Daucourt**

- [d2s0] Élise- Daucourt is a commune in the Marne department in north -eastern France.
- [d2s1] The commune consists of 2 villages, Élise and Daucourt, which are 1 mile apart.
- [d2s2] Both villages were separate communes until 1965, when they merged.
- [d2s3] Since the merger Élise is often called Élise- Daucourt.
- [d2s4] Both villages lie about 6 km south of Sainte- Menehould, the nearest regional town.

**d3: Zaandijk Zaanse Schans railway station**

- [d3s0] Zaandijk Zaanse Schans railway station, until 2016 Koog- Zaandijk railway station, is a railway station in Koog aan de Zaan and Zaandijk, both neighbourhoods of the municipality of Zaandam, Netherlands.
- [d3s1] It is also the closest railway station to Zaanse Schans.
- [d3s2] The station opened on 1 November 1869 and is located on the Den Helder – Amsterdam railway between Zaandam and Uitgeest.

**d4: A8 motorway (Netherlands)**

- [d4s0] The A8 motorway is a motorway in the Netherlands.
- [d4s1] It starts at the intersection with the Ring Amsterdam( the A10 motorway) at interchange Coenplein, and leads past Oostzaan, interchange Zaandam, and Zaandijk towards its terminus, not even 10 kilometers from its beginning at the Coenplein, near Assendelft.

**d5: Maylandsea**

- [d5s0] Maylandsea, and the adjacent Mayland, are villages on the Dengie peninsula in the English county of Essex.
- [d5s1] They are part of the Althorne ward of the Maldon district, and have a parish council that covers both villages.

**d6: Radisele**

- [d6s0] Radisele is a village in Central District of Botswana.
- [d6s1] The village is located along the road connecting Palapye and Mahalapye, approximately in the middle of both villages( about 37 km from either village).
- [d6s2] The population was 2,741 in 2001 census.

**d7: Zaandijk**

- [d7s0] Zaandijk is a town in the municipality of Zaanstad, province of North Holland, Netherlands.
- [d7s1] It lies about 11 kilometres( 6.8 miles) northwest of Amsterdam and had a population of 8,686 in 2017.

**d8: Allington, Salisbury**

- [d8s0] Allington is a village and civil parish in Wiltshire, England, about southeast of Amesbury and northeast of Salisbury.
- [d8s1] The parish includes the village of Boscombe; both villages are on the River Bourne and the A338 road.

**d9: Satellite tournament**

- [d9s0] A satellite tournament is either a minor tournament or event on a competitive sporting tour or one of a group of such tournaments that form a series played in the same country or region.

**d10: Pociūnai (Prienai)**

- [d10s0] Pociūnai is a village in the eldership or elderate of Ašmintos, in the Prienai district municipality in Kaunas County, Lithuania.
- [d10s1] According to the 2011 census, the village had 53 residents.

## 29. 2wikimultihopqa_f0864eb00bdc11eba7f7acde48001122

原位置：`train` 第 119 题 · 全局第 119 题 · `sample_id: 2wikimultihopqa_f0864eb00bdc11eba7f7acde48001122`

Question: What is the date of death of the director of film The Shadow Laughs (Film)?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of The Shadow Laughs (Film) | False | () |
| u2 | date of death of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film The Shadow Laughs | False | [] | Arthur Hoerl | [['d3s0']] |
| u2 | date of death of {u1} | True | ['u1'] | February 6, 1968 | [['d2s0']] |

### Source documents (reference only)

**d1: Thomas Scott (diver)**

- [d1s0] Thomas Scott( 1907- date of death unknown) was an English diver.

**d2: Arthur Hoerl**

- [d2s0] Arthur Hoerl (December 17, 1891 – February 6, 1968) was an American screenwriter and film director.
- [d2s1] Hoerl was born in New York, son of Louis Hoerl, a German immigrant silver polisher, and Teresa Hoerl.
- [d2s2] Arthur completed three years of high school, according to the 1940 US Census.
- [d2s3] He wrote for 150 films between 1921 and 1968.
- [d2s4] One of his most well known credits is co-writer for the film
- [d2s5] "Tell Your Children" (1936) which is now known as "Reefer Madness".
- [d2s6] For Broadway, 1932, he wrote the play "A Few Wild Oats."
- [d2s7] He also directed four films between 1932 and 1934.
- [d2s8] Hoerl died in Hollywood, California.

**d3: The Shadow Laughs (film)**

- [d3s0] The Shadow Laughs is a 1933 American Pre-Code mystery film directed by Arthur Hoerl and starring Hal Skelly, Rose Hobart and Harry T. Morey.

**d4: Theodred II (Bishop of Elmham)**

- [d4s0] Theodred II was a medieval Bishop of Elmham.
- [d4s1] The date of Theodred's consecration unknown, but the date of his death was sometime between 995 and 997.

**d5: Harry Wainwright (footballer)**

- [d5s0] Harry Wainwright( born 1899; date of death unknown) was an English footballer.

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

**d7: The Shadow of the Desert**

- [d7s0] The Shadow of the Desert( also released as The Shadow of the East) is a 1924 American silent horror film directed by George Archainbaud.
- [d7s1] The film is considered to be lost.

**d8: Ian Barry (director)**

- [d8s0] Ian Barry is an Australian director of film and TV.

**d9: Peter Levin**

- [d9s0] Peter Levin is an American director of film, television and theatre.

**d10: Bill Smith (footballer, born 1897)**

- [d10s0] William Thomas Smith( born 9 April 1897, date of death unknown) was an English professional footballer.

## 30. 2wikimultihopqa_f3d47a5d08b111ebbd85ac1f6bf848b6

原位置：`train` 第 120 题 · 全局第 120 题 · `sample_id: 2wikimultihopqa_f3d47a5d08b111ebbd85ac1f6bf848b6`

Question: Which film whose director was born first, A Man On The Road or Burnt Money?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of A Man On The Road | False | () |
| u2 | birth date of {u1} | False | ('u1',) |
| u3 | director of Burnt Money | False | () |
| u4 | birth date of {u3} | False | ('u3',) |
| u5 | which film's director was born first | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of A Man on the Road | False | [] | Manuel Mur Oti | [['d2s0']] |
| u2 | date of birth of {u1} | False | ['u1'] | 25 October 1908 | [['d5s0']] |
| u3 | director of Burnt Money | False | [] | Marcelo Piñeyro | [['d4s0']] |
| u4 | date of birth of {u3} | False | ['u3'] | March 5, 1953 | [['d3s0']] |
| u5 | which of A Man on the Road and Burnt Money has the director born first | True | ['u2', 'u4'] | A Man on the Road | [[]] |

### Source documents (reference only)

**d1: John McMahon (Surrey and Somerset cricketer)**

- [d1s0] John William Joseph McMahon( 28 December 1917 – 8 May 2001) was an Australian- born first- class cricketer who played for Surrey and Somerset in England from 1947 to 1957.

**d2: A Man on the Road**

- [d2s0] A Man on the Road( Spanish: Un hombre va por el camino) is a 1949 Spanish drama film directed by Manuel Mur Oti and starring Ana Mariscal, Fernando Nogueras and Pacita de Landa.

**d3: Marcelo Piñeyro**

- [d3s0] Marcelo Piñeyro( born March 5, 1953) is an Argentine award- winning film director, screenwriter, and film producer.

**d4: Burnt Money**

- [d4s0] Burnt Money is a 2001 Argentine action thriller directed by Marcelo Piñeyro and written by Piñeyro and Marcelo Figueras.
- [d4s1] Starring Leonardo Sbaraglia, Eduardo Noriega, Pablo Echarri, Leticia Brédice and Ricardo Bartis, it is based on Ricardo Piglia's 1997" Planeta" prize- winning novel of the same name.
- [d4s2] The novel was inspired by the true story of a notorious 1965 bank robbery in Buenos Aires.
- [d4s3] " Plata quemada" won, among other awards, the Goya Award for" Best Spanish Language Foreign Film" in 2002.
- [d4s4] It was partly funded by INCAA.

**d5: Manuel Mur Oti**

- [d5s0] Manuel Mur Oti( 25 October 1908 – 5 August 2003) was a Spanish screenwriter and film director.
- [d5s1] He also acted in one film, the neorealist" Segundo López"( 1953).

**d6: Wale Adebanwi**

- [d6s0] Wale Adebanwi( born 1969) is a Nigerian- born first Black Rhodes Professor at St Antony's College, Oxford.

**d7: Hartley Lobban**

- [d7s0] Hartley W Lobban (9 May 1926 – 15 October 2004) was a Jamaican-born first-class cricketer who played 17 matches for Worcestershire in the early 1950s.

**d8: Ringo-en no shōjo**

- [d8s0] The art director was Tomoo Shimogawara.

**d9: Deepak Sareen**

- [d9s0] Deepak Sareen is a Bollywood film director and assistant director.
- [d9s1] His first film as director was" Ranbhoomi" and last film as director was" Albela".

**d10: Henry Moore (cricketer)**

- [d10s0] Henry Walter Moore( 1849 – 20 August 1916) was an English- born first- class cricketer who spent most of his life in New Zealand.
