# batch_05：人工审查（30 题）

全局题号 121–150；train 30 题 / dev 0 题。原训练/验证归属保持不变。

[返回分配索引](../README.md) · [完整对比报告](../../comparison_human.md)

**原则：新旧单元都合理时保留拆题器拆法，人工监督向新单元对齐。** 未标记的题目也需要核对答案和证据。现有标记是 AI 辅助审阅意见，不是人工验收结论。

审查人：________　完成日期：________

## 1. 2wikimultihopqa_f52b042e0baf11ebab90acde48001122

原位置：`train` 第 121 题 · 全局第 121 题 · `sample_id: 2wikimultihopqa_f52b042e0baf11ebab90acde48001122`

Question: Who is the paternal grandmother of Charles Of Artois, Count Of Eu?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Charles Of Artois, Count Of Eu | False | () |
| u2 | mother of {u1}, Charles Of Artois, Count Of Eu's paternal grandmother | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Charles of Artois, Count of Eu | False | [] | Philip of Artois, Count of Eu | [['d6s0']] |
| u2 | mother of {u1}, Charles of Artois's paternal grandmother | True | ['u1'] | Isabeau of Melun | [['d3s0']] |

### Source documents (reference only)

**d1: Joan of Valois, Countess of Beaumont**

- [d1s0] Joan of Valois (1304–1363) was the daughter of Charles of Valois and his second wife Catherine I of Courtenay, titular empress of Constantinople.
- [d1s1] Half sister to Philip VI of Valois, in around 1320 she married Robert III of Artois, Count of Beaumont-le-Roger and seigneur of Conches.
- [d1s2] They had five known children:
Robert III of Artois had attempted to recover the title of count of Artois, which had been taken from him by his aunt Mahaut of Artois, but was condemned and exiled in 1331 for making and presenting forged documents in the process of filing against her.
- [d1s3] Joan of Valois and their children were therefore imprisoned by order of her half-brother Philip VI.

**d2: Louis, Count of Évreux**

- [d2s0] Louis of Évreux( 3 May 1276 – 19 May 1319, Paris) was a prince, the only son of King Philip III of France and his second wife Maria of Brabant, and thus a half- brother of King Philip IV of France.
- [d2s1] Louis had a quiet and reflective personality and was politically opposed to the scheming of his half- brother Charles of Valois.
- [d2s2] He was, however, close with his nephew Philip V of France.
- [d2s3] He married Margaret of Artois, daughter of Philip of Artois and sister of Robert III of Artois, and had five children:

**d3: Philip of Artois, Count of Eu**

- [d3s0] Philip of Artois (1358 – 16 June 1397, Micalizo), son of John of Artois, Count of Eu, and Isabeau of Melun, was Count of Eu from 1387 until his death, succeeding his brother Robert.
- [d3s1] Philip was a gallant and energetic soldier.
- [d3s2] In 1383, he captured the town of Bourbourg from the English.
- [d3s3] He went on a pilgrimage to the Holy Land, and was imprisoned there by Barquq, the Sultan of Egypt, being released through the mediation of Jean Boucicaut and the Venetians.
- [d3s4] In 1390, he joined the unsuccessful expedition of Louis II, Duke of Bourbon, against Mahdia.
- [d3s5] In 1392, he was created Constable of France.
- [d3s6] On 27 January 1393 he married Marie (1367–1434), daughter of John, Duke of Berry.
- [d3s7] They had four children:
- [d3s8] As a prominent Crusader, he was one of the French contingent sent to take part in the Battle of Nicopolis.
- [d3s9] He was captured in the battle, and subsequently died in captivity.

**d4: Tjuyu**

- [d4s0] Tjuyu( sometimes transliterated as Thuya or Thuyu) was an Egyptian noblewoman and the mother of queen Tiye, and the wife of Yuya.
- [d4s1] She is the grandmother of Akhenaten, and great grandmother of Tutankhamun.

**d5: Mona Hopton Bell**

- [d5s0] Mona Hopton Bell( 1867- 1940) was a British artist, best known for her portraits of civic figures.
- [d5s1] She was the grandmother of the painter Jean H. Bell.

**d6: Charles of Artois, Count of Eu**

- [d6s0] Charles of Artois (1394 – 25 July 1472), son of Philip of Artois, Count of Eu and Marie of Berry, was Count of Eu from December 1397 until his death 74 years later.
- [d6s1] He was taken prisoner by the English at the Battle of Agincourt on 25 October 1415, and was not released until 1438.
- [d6s2] In 1448, he married Jeanne of Saveuse (died 1449) and on 23 September 1454, Helene of Melun (d. 1473), but he had no children.
- [d6s3] He was appointed Lieutenant of the King in Normandy and Guyenne, as well as Governor of Paris, during the War of the Public Weal in 1465.
- [d6s4] He was succeeded by his nephew John II, Count of Nevers.

**d7: Thierry Larchier d'Hirson**

- [d7s0] Thierry Larchier d' Hirson or d' Hireçon, or de Hérisson,( 1270 in Bourbonnais – 23 August 1328) was a French cleric under Robert II, Count of Artois.
- [d7s1] Hirson was employed by Philip IV of France on several occasions.
- [d7s2] He became a canon of Arras in 1299; chancellor of Mahaut, Countess of Artois in 1303; provost of Aire- sur- la- Lys in 1309; and was appointed Bishop of Arras in April 1328.
- [d7s3] He died on 23 August 1328.
- [d7s4] Hirson was involved with Jeanne de Divion, who, in revenge for what she did not inherit upon the bishop's death, procured false documents for Robert III of Artois so that he could recover the County of Artois, which had been bestowed upon his great aunt Mahaut, Countess of Artois, in a legal dispute.

**d8: Hubba bint Hulail**

- [d8s0] Hubba bint Hulail was the grandmother of Hashim ibn' Abd Manaf, thus the great- great- great- grandmother of the Islamic" Nabī"( Prophet) Muhammad ibn Abdullah.

**d9: Hannah Arnold**

- [d9s0] Hannah Arnold, also known as Hannah Waterman King, was the grandmother of Benedict Arnolds children.

**d10: Margaret of Artois**

- [d10s0] Margaret of Artois( 1285–1311) was the eldest child of Philip of Artois and his wife, Blanche of Brittany.
- [d10s1] She was a member of the House of Artois.
- [d10s2] She was married to Louis d'Évreux.
- [d10s3] By her marriage, Margaret was Countess consort of Évreux.

## 2. 2wikimultihopqa_f5a1f18c088b11ebbd6fac1f6bf848b6

原位置：`train` 第 122 题 · 全局第 122 题 · `sample_id: 2wikimultihopqa_f5a1f18c088b11ebbd6fac1f6bf848b6`

Question: Which film has the director died first, Maravil Thirivu Sookshikkuka or Beloved Liar?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of Maravil Thirivu Sookshikkuka | False | () |
| u2 | death date of {u1} | False | ('u1',) |
| u3 | director of Beloved Liar | False | () |
| u4 | death date of {u3} | False | ('u3',) |
| u5 | which film's director died first | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Maravil Thirivu Sookshikkuka | False | [] | J. Sasikumar | [['d5s0']] |
| u2 | date of death of {u1} | False | ['u1'] | 17 July 2014 | [['d4s0']] |
| u3 | director of film Beloved Liar | False | [] | Hans Schweikart | [['d6s0']] |
| u4 | date of death of {u3} | False | ['u3'] | 1 December 1975 | [['d7s0']] |
| u5 | which of the two films has the director who died first | True | ['u2', 'u4'] | Beloved Liar | [[]] |

### Source documents (reference only)

**d1: Le Masque de la Méduse**

- [d1s0] Le masque de la Méduse is a 2009 fantasy horror film directed by Jean Rollin.
- [d1s1] The film is a modern-day telling of the Greek mythological tale of the Gorgon and was inspired by the 1964 classic Hammer Horror film of the same name and the 1981 cult classic" Clash of the Titans".
- [d1s2] It was Rollin's final film, as the director died in 2010.

**d2: Thulasi (1987 film)**

- [d2s0] Thulasi is a 1987 Tamil romantic drama film directed by Ameerjan.
- [d2s1] The film features Murali and Seetha in lead roles.
- [d2s2] The film, produced by P. S. V. Hariharan, had musical score by Sampath Selvam and was released on 27 November 1987.
- [d2s3] The music director died before the release of the film.

**d3: Little Turkey**

- [d3s0] Little Turkey( 1758–1801) was First Beloved Man of the Cherokee people, becoming, in 1794, the first Principal Chief of the original Cherokee Nation.

**d4: J. Sasikumar**

- [d4s0] Nambiathusseril Varkey John( 14 October 1927 – 17 July 2014), better known by his screen name Sasikumar, was an Indian film director who worked in Malayalam cinema.
- [d4s1] One of the most prolific directors in world cinema, he has directed more than 141 films in his career which began in the mid-1960s.
- [d4s2] He is often referred to as Hitmaker Sasikumar due to the commercial success of his films.
- [d4s3] Sasikumar holds three world records: the records for most films( 141), most films having the same actor as hero( Prem Nazir in 84 films) and the most films directed in a year( 15 films in 1977).
- [d4s4] He died in 2014 at the age of 86.

**d5: Maravil Thirivu Sookshikkuka**

- [d5s0] Maravil Thirivu Sookshikkuka is a 1972 Indian Malayalam crime thriller film, directed by J. Sasikumar and produced by R. S. Rajan.
- [d5s1] The film stars Prem Nazir, Vijayasree, Adoor Bhasi and Thikkurissi Sukumaran Nair in the lead roles.
- [d5s2] The film had musical score by G. Devarajan.

**d6: Beloved Liar**

- [d6s0] Beloved Liar  is a 1950 West German romantic comedy film directed by Hans Schweikart and starring Elfie Mayerhofer, Hans Söhnker and Gustav Knuth.
- [d6s1] It was made at the Bavaria Studios in Munich and on location at Lake Starnberg.
- [d6s2] The film's sets were designed by Robert Herlth.

**d7: Hans Schweikart**

- [d7s0] Hans Schweikart (1 October 1895 – 1 December 1975) was a German film director, actor and screenwriter.
- [d7s1] He directed 28 films between 1938 and 1968.
- [d7s2] He wrote for the film "The Marriage of Mr. Mississippi", which was entered into the 11th Berlin International Film Festival.

**d8: Mohsen Eslamzadeh**

- [d8s0] Mohsen Eslamzadeh is an Iranian documentary filmmaker.
- [d8s1] He is the director of" Alone Among The Taliban".
- [d8s2] This film has won the best documentary award at the 44th Athens International Film and Video Festival in the United States.
- [d8s3] This film has won the best documentary award at the 12th Marbella International Film Festival in Spain.
- [d8s4] This film has won the Shahid Avini Award offers.

**d9: Oconostota**

- [d9s0] Oconostota( c. 1710–1783)( also" Stalking Turkey") was a" skiagusta" of Chota and the First Beloved Man of the Cherokee from 1775 to 1781.

**d10: Querelle**

- [d10s0] Querelle is a 1982 West German- French English- language drama film directed by Rainer Werner Fassbinder and starring Brad Davis, adapted from French author Jean Genet's 1947 novel" Querelle of Brest".
- [d10s1] It marked Fassbinder's final film as a writer/ director; it was posthumously released just months after the director died of a drug overdose in June 1982.

## 3. 2wikimultihopqa_f96c965908dd11ebbd9eac1f6bf848b6

原位置：`train` 第 123 题 · 全局第 123 题 · `sample_id: 2wikimultihopqa_f96c965908dd11ebbd9eac1f6bf848b6`

Question: Which film has the director who was born earlier, Wives On Strike or Sporting Goods?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of Wives On Strike | False | () |
| u2 | birth date of {u1} | False | ('u1',) |
| u3 | director of Sporting Goods | False | () |
| u4 | birth date of {u3} | False | ('u3',) |
| u5 | which film's director was born earlier | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of Wives on Strike | False | [] | Omoni Oboli | [['d8s0']] |
| u2 | date of birth of {u1} | False | ['u1'] | 22 April 1978 | [['d3s0']] |
| u3 | director of Sporting Goods | False | [] | Malcolm St. Clair | [['d7s0']] |
| u4 | date of birth of {u3} | False | ['u3'] | May 17, 1897 | [['d9s0']] |
| u5 | which of the two films has the director born earlier | True | ['u2', 'u4'] | Sporting Goods | [[]] |

### Source documents (reference only)

**d1: Abhishek Saxena**

- [d1s0] Abhishek Saxena is an Indian Bollywood and Punjabi film director who directed the movie Phullu.
- [d1s1] The Phullu movie was released in theaters on 16 June 2017, in which film Sharib Hashmi is the lead role.
- [d1s2] Apart from these, he has also directed Patiala Dreamz, this is a Punjabi film.
- [d1s3] This film was screened in cinemas in 2014.

**d2: Hassan Zee**

- [d2s0] Hassan Zee is a Pakistani- American film director who was born in Chakwal, Pakistan.

**d3: Omoni Oboli**

- [d3s0] Omoni Oboli( born 22 April 1978) is a Nigerian actress, scriptwriter, film director, producer and a trained digital filmmaker.
- [d3s1] She studied at the New York Film Academy, and has written several screenplays such as; The figurine( 2009), Anchor baby( 2010)," Fatal Imagination Being Mrs Elliott The First Lady", and" Wives on Strike( 2016)".

**d4: Edward Yates**

- [d4s0] Edward J. Yates( September 16, 1918 – June 2, 2006) was an American television director who was the director of the ABC television program" American Bandstand" from 1952 until 1969.

**d5: Ben Palmer**

- [d5s0] Ben Palmer is a British film and television director who is known for being the director of" Bo' Selecta" and" The Inbetweeners".

**d6: Emilie of Saxony**

- [d6s0] Emilie of Saxony (27 July 1516 – 9 April 1591) was the third wife of Margrave George the Pious of Brandenburg-Ansbach.
- [d6s1] Since his two earlier wives died before his accession, she was the only one to enjoy the title Margravine.

**d7: Sporting Goods**

- [d7s0] Sporting Goods is a lost 1928 American comedy silent film directed by Malcolm St. Clair, written by George Marion Jr., Ray Harris and Thomas J. Crizer, and starring Richard Dix, Ford Sterling, Gertrude Olmstead, Philip Strange, Myrtle Stedman, Wade Boteler and Claude King.
- [d7s1] It was released on February 11, 1928, by Paramount Pictures.

**d8: Wives on Strike**

- [d8s0] Wives on Strike is a 2016 Nigerian film produced and directed by Omoni Oboli and starring Uche Jombo, Chioma Akpotha, Ufuoma McDermott, and Kehinde Bankole.

**d9: Malcolm St. Clair (filmmaker)**

- [d9s0] Malcolm St. Clair( May 17, 1897 – June 1, 1952) was a Hollywood film director, writer, producer and actor.

**d10: Rumbi Katedza**

- [d10s0] Rumbi Katedza is a Zimbabwean Film Producer and Director who was born on 17 January 1974.

## 4. 2wikimultihopqa_fbad88760bdc11eba7f7acde48001122

原位置：`train` 第 124 题 · 全局第 124 题 · `sample_id: 2wikimultihopqa_fbad88760bdc11eba7f7acde48001122`

Question: What is the place of birth of Julian Marley's father?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Julian Marley | False | () |
| u2 | place of birth of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Julian Marley | False | [] | Bob Marley | [['d7s1']] |
| u2 | place of birth of {u1} | True | ['u1'] | Nine Mile | [['d1s5']] |

### Source documents (reference only)

**d1: Bob Marley**

- [d1s0] Robert Nesta Marley, (6 February 1945 – 11 May 1981) was a Jamaican singer and songwriter.
- [d1s1] Considered one of the pioneers of reggae, his musical career was marked by blending elements of reggae, ska, and rocksteady, as well as forging a smooth and distinctive vocal and songwriting style.
- [d1s2] Marley's contributions to music increased the visibility of Jamaican music worldwide, and made him a global figure in popular culture for over a decade.
- [d1s3] Over the course of his career Marley became known as a Rastafari icon, and the singer sought to infuse his music with a sense of spirituality.
- [d1s4] He is also considered a global symbol of Jamaican culture and identity, and was controversial in his outspoken support for the legalization of marijuana, while he also advocated for Pan-Africanism.
- [d1s5] Born in Nine Mile, British Jamaica, Marley began his professional musical career in 1963, after forming Bob Marley and the Wailers.
- [d1s6] The group released its debut studio album "The Wailing Wailers" in 1965, which contained the single "One Love/People Get Ready"; the song was immensely popular, peaking in the top five on worldwide music charts, and established the group as a rising figure in reggae.
- [d1s7] The Wailers subsequently released eleven further studio albums; while initially employing louder instrumentation and singing, the group began engaging in rhythmic-based song construction in the late 1960s and early 1970s, which coincided with the singer's conversion to Rastafarianism.
- [d1s8] During this period Marley relocated to London, and the group typified their musical shift with the release of the album "The Best of The Wailers" (1971).
- [d1s9] The group attained international success after the release of the albums "Catch a Fire" and "Burnin'" (both 1973), and forged a reputation as touring artists.
- [d1s10] A year later the Wailers disbanded, and Marley went on to release his solo material under the band's name.
- [d1s11] His debut studio album "Natty Dread" (1974) received positive reception, as did its follow-up "Rastaman Vibration" (1976).
- [d1s12] A few months after the album's release Marley survived an assassination attempt at his home in Jamaica, which prompted him to permanently relocate to London soon afterward.
- [d1s13] There he recorded the album "Exodus" (1977); it incorporated elements of blues, soul, and British rock, enjoyed widespread commercial success, and is widely considered one of the best albums of all time.
- [d1s14] In 1977, Marley was diagnosed with acral lentiginous melanoma; he died as a result of the illness in 1981.
- [d1s15] His fans around the world expressed their grief, and he received a state funeral in Jamaica.
- [d1s16] The greatest hits album "Legend" was released in 1984, and subsequently became the best-selling reggae album of all-time.
- [d1s17] Marley also ranks as one of the best-selling music artists of all-time, with estimated sales of more than 75 million records worldwide, while his sound and style have influenced artists of various genres.
- [d1s18] He was posthumously honored by Jamaica soon after his death, as he was designated the nation's Order of Merit award.

**d2: Allan Marley**

- [d2s0] Allan Marley( born 29 February 1956) is an English professional footballer who played as a full- back.

**d3: Obata Toramori**

- [d3s0] He was the father of Obata Masamori.

**d4: Skip Marley**

- [d4s0] Skip Marley( born 4 June 1996) is a Jamaican singer- songwriter.
- [d4s1] He is the son of Cedella Marley, and grandson of Bob Marley.

**d5: Bert Marley**

- [d5s0] Bert C. Marley( born May 1, 1948) is an American politician.
- [d5s1] He was the chair of the Idaho Democratic Party from August 2015 to March 16, 2019.
- [d5s2] He was a member of the Idaho Senate and Idaho House of Representatives.

**d6: Cleomenes II**

- [d6s0] Cleomenes II( died 309 BC) was Agiad King of Sparta from 369 to 309 BC.
- [d6s1] The son of Cleombrotus I, he succeeded his brother Agesipolis II.
- [d6s2] He was the father of Acrotatus I, the father of Areus I, and of Cleonymus, the father of Leonidas II.

**d7: Julian Marley**

- [d7s0] Julian Ricardo Marley (born 4 June 1975) is a British Jamaican reggae musician.
- [d7s1] He is the son of reggae artist and performer Bob Marley, and Lucy Pounder.
- [d7s2] Marley is a Grammy award nominated, reggae singer, musician, songwriter, producer and humanitarian.
- [d7s3] He follows in his father's footsteps and is a devout Rastafarian who uses his music to inspire his life and spirituality.

**d8: Bambaata Marley**

- [d8s0] Bambaata Marley( born 12 July 1989) is a Jamaican singer- songwriter.
- [d8s1] He is the eldest son of Ziggy Marley, and eldest grandson of Bob Marley.

**d9: John Templeton (botanist)**

- [d9s0] John Templeton( 1766–1825) was an early Irish naturalist and botanist.
- [d9s1] He is often referred to as the" Father of Irish Botany".
- [d9s2] He was the father of naturalist, artist and entomologist Robert Templeton.

**d10: Arthur Beauchamp**

- [d10s0] Arthur Beauchamp( 1827 – 28 April 1910) was a Member of Parliament from New Zealand.
- [d10s1] He is remembered as the father of Harold Beauchamp, who rose to fame as chairman of the Bank of New Zealand and was the father of writer Katherine Mansfield.

## 5. 2wikimultihopqa_fc76b898099011ebbdb0ac1f6bf848b6

原位置：`train` 第 125 题 · 全局第 125 题 · `sample_id: 2wikimultihopqa_fc76b898099011ebbdb0ac1f6bf848b6`

Question: Are both villages, Boneh-Ye Khiraleh and Askaru, located in the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of Boneh-Ye Khiraleh | False | () |
| u2 | country of Askaru | False | () |
| u3 | whether Boneh-Ye Khiraleh and Askaru are in the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country of Boneh-ye Khiraleh | False | [] | Iran | [['d9s0']] |
| u2 | country of Askaru | False | [] | Iran | [['d10s0']] |
| u3 | whether Boneh-ye Khiraleh and Askaru are located in the same country | True | ['u1', 'u2'] | yes | [[]] |

### Source documents (reference only)

**d1: Boneh-ye Chahar**

- [d1s0] Boneh- ye Chahar( also Romanized as Boneh- ye Chahār; also known as Boneh- ye Chāreh) is a village in Garmsar Rural District, Jebalbarez- e Jonubi District, Anbarabad County, Kerman Province, Iran.
- [d1s1] At the 2006 census, its population was 91, in 21 families.

**d2: Boneh-ye Cheragh, Soltanabad**

- [d2s0] Boneh- ye Cheragh( also Romanized as Boneh- ye Cherāgh; also known as Boneh- ye Ḩājjī Cherāgh and Cherāgh) is a village in Soltanabad Rural District, in the Central District of Ramhormoz County, Khuzestan Province, Iran.
- [d2s1] At the 2006 census, its population was 125, in 29 families.

**d3: Boneh-ye Sukhteh Char**

- [d3s0] Boneh- ye Sukhteh Char( also Romanized as Boneh- ye Sūkhteh Chār; also known as Boneh- ye Sūkhteh and Boneh- ye Sūkhteh Chāl) is a village in Howmeh Rural District, in the Central District of Bam County, Kerman Province, Iran.
- [d3s1] At the 2006 census, its population was 63, in 13 families.

**d4: Boneh-ye Karim**

- [d4s0] Boneh- ye Karim( also Romanized as Boneh- ye Karīm; also known as Boneh- ye Karīmī and Karīmī) is a village in Howmeh- ye Gharbi Rural District, in the Central District of Ramhormoz County, Khuzestan Province, Iran.
- [d4s1] At the 2006 census, its population was 279, in 61 families.

**d5: Boneh-ye Abbas, Bushehr**

- [d5s0] Boneh- ye Abbas( also Romanized as Boneh- ye ‘ Abbās; also known as Boneh- ye ‘ Abbāsī) is a village in Shabankareh Rural District, Shabankareh District, Dashtestan County, Bushehr Province, Iran.
- [d5s1] At the 2006 census, its population was 103, in 20 families.

**d6: Boneh-ye Mirza**

- [d6s0] Boneh- ye Mirza( also Romanized as Boneh- ye Mīrzā) is a village in Shahi Rural District, Sardasht District, Dezful County, Khuzestan Province, Iran.
- [d6s1] At the 2006 census, its population was 36, in 7 families.

**d7: Boneh-ye Sorkhi**

- [d7s0] Boneh- ye Sorkhi( also Romanized as Boneh- ye Sorkhī; also known as Boneh- ye Sorkh and Shīrīn Āb) is a village in Dasht -e Lali Rural District, in the Central District of Lali County, Khuzestan Province, Iran.
- [d7s1] At the 2006 census, its population was 615, in 108 families.

**d8: Boneh-ye Amir Asgar**

- [d8s0] Boneh- ye Amir Asgar( also Romanized as Boneh- ye Āmīr ‘ Asgar; also known as Boneh- ye ‘ Asgar) is a village in Howmeh- ye Sharqi Rural District, in the Central District of Ramhormoz County, Khuzestan Province, Iran.
- [d8s1] At the 2006 census, its population was 170, in 34 families.

**d9: Boneh-ye Khiraleh**

- [d9s0] Boneh- ye Khiraleh( also Romanized as Boneh- ye Khīrāleh) is a village in Howmeh Rural District, in the Central District of Haftgel County, Khuzestan Province, Iran.
- [d9s1] At the 2006 census, its population was 33, in 7 families.

**d10: Askaru**

- [d10s0] Askaru( also Romanized as ʿ Askarū) is a village in Rayen Rural District, Rayen District, Kerman County, Kerman Province, Iran.
- [d10s1] At the 2006 census, its existence was noted, but its population was not reported.

## 6. hotpotqa_5a730a5555429901807daf72 【保留新拆法｜重标人工标签】

原位置：`train` 第 126 题 · 全局第 126 题 · `sample_id: hotpotqa_5a730a5555429901807daf72`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5a730a5555429901807daf72"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新单元完整限定电影演员和八次奥斯卡提名条件，旧版分候选识别和筛选。两种都能回答同一演员；不因隐式桥接而判新单元错误。
>
> **处理建议：** 保留 single；新目标值对应旧末单元，支持集合联合 d5s0 的演员关系和 d9s1 的提名条件，重建证据快照。
>
> **证据定位：** d5s0, d9s1；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: You Can't Run Away from It starred which eight time Academy Award nominee?

Note:

Type: single · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | eight time Academy Award nominee who starred in You Can't Run Away from It | True | () |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | stars of You Can't Run Away from It | False | [] | June Allyson and Jack Lemmon | [['d5s0']] |
| u2 | which of {u1} was an eight-time Academy Award nominee | True | ['u1'] | Jack Lemmon | [['d9s1']] |

### Source documents (reference only)

**d1: Rehearsing a Dream**

- [d1s0] Rehearsing a Dream is a short documentary directed and produced by four time Academy Award nominees Karen Goodman and Kirk Simon.
- [d1s1]  Cinematography by Buddy Squires and Steve McCarthy, edited by Nancy Baker and a Production of Simon & Goodman Picture Company.
- [d1s2]  The film premiered on HBO in August 2007 and was nominated for an Academy Award for Best Documentary Short.

**d2: Shea Kerry**

- [d2s0] Shea Kerry is an American writer and producer.
- [d2s1]  He played the role of "Steve" in the thriller "Dark Honeymoon" (2008), starring Academy Award nominee Roy Scheider ("All That Jazz", "The French Connection"), Academy Award nominee Eric Roberts ("Runaway Train"), Steve Wilder, and Daryl Hannah.

**d3: Amy Ryan**

- [d3s0] Amy Ryan (born Amy Beth Dziewiontkowski; May 3, 1969) is an American actress of stage and screen.
- [d3s1]  A graduate of New York's High School of Performing Arts, she is an Academy Award nominee and two-time Tony Award nominee.

**d4: Kyle Townsend**

- [d4s0] Kyle Townsend (born September 21, 1978) is an American record producer, musician and composer.
- [d4s1]  He has produced songs for such acclaimed recording artists as 5-time GRAMMY Award winner Celine Dion, 8-time Academy Award nominated songwriter Diane Warren, as well as Mary J Blige, Lady Gaga, Jessie J, and Academy Award winner Jennifer Hudson among others.
- [d4s2]  He has produced songs for five feature film releases including the 2012 Academy Award nominee for Best Picture, and he produced and arranged music for the 2015 Academy Awards Ceremony.
- [d4s3]  His contributions have earned 2 GRAMMY Award Nominations.

**d5: You Can't Run Away from It**

- [d5s0] You Can't Run Away from It is a 1956 Technicolor and CinemaScope musical comedy starring June Allyson and Jack Lemmon.
- [d5s1]  Directed and produced by Dick Powell, the film is a remake of the 1934 Academy Award-winning film "It Happened One Night".
- [d5s2]  The supporting cast features Charles Bickford, Jim Backus, Stubby Kaye, Jack Albertson and Howard McNear.
- [d5s3]  "It Happened One Night" had also been remade as a musical comedy in 1945 as "Eve Knew Her Apples".

**d6: Jonathan Tammuz**

- [d6s0] Jonathan Tammuz is a British-Canadian film director, best known for directing the short film "The Childeater" and the feature film "Rupert's Land".
- [d6s1]  "The Childeater" was a shortlisted Academy Award nominee for Best Live Action Short Film at the 62nd Academy Awards, and "Rupert's Land" which was a Genie Award nominee for Best Picture at the 19th Genie Awards, with Tammuz also nominated for Best Director.

**d7: Resurrection: The J.R. Richard Story**

- [d7s0] Resurrection: The J.R. Richard Story is a 2005 American independent film, directed by Greg Carter and Benjamin O. Jimerson-Phillips, Executive Producers Charlie Bellinger, J.R. Richard & Larry Johnson; and Produced by Benjamin O. Jimerson-Phillips, and Bruce Dalton, starring David Ramsey and Charles Durning two time Academy Award Nominee.
- [d7s1]  The film is a biopic tale of the Houston Astros baseball Pitcher J. R. Richard, his life high points struggles.
- [d7s2]  It was shot by Bellinger-7 Films, which is owned by Ms. Charlie Bellinger-Bethea, former wife of NFL Hall of Fame Inductee Elvin Bethea, and done in association with Nexus Films & Adept Films Inc.

**d8: Lesley Ann Warren**

- [d8s0] Lesley Ann Warren (born August 16, 1946) is an American actress and singer.
- [d8s1]  She was nominated for the Academy Award for Best Supporting Actress for the 1982 film "Victor/Victoria".
- [d8s2]  She is also an Emmy Award nominee and five-time Golden Globe Award nominee, winning the Golden Globe for Best Actress in a Drama Series for the 1977 NBC miniseries "Harold Robbins' 79 Park Avenue".

**d9: Jack Lemmon**

- [d9s0] John Uhler "Jack" Lemmon III (February 8, 1925 – June 27, 2001) was an American actor and musician.
- [d9s1]  Lemmon was an eight time Academy Award nominee, with two wins.
- [d9s2]  He starred in over 60 films, such as "Some Like It Hot", "The Apartment", "Mister Roberts" (for which he won the 1955 Academy Award for Best Supporting Actor), "Days of Wine and Roses", "The Great Race", "Irma la Douce", "The Odd Couple" and its sequel 30 years later, "The Odd Couple II", (and other frequent collaborations with "Odd Couple" co-star Walter Matthau), "Save the Tiger" (for which he won the 1973 Academy Award for Best Actor), "The Out-of-Towners", "The China Syndrome", "Missing" (for which he won Best Actor at the 1982 Cannes Film Festival), "Glengarry Glen Ross", "Tuesdays with Morrie", "Grumpy Old Men", and "Grumpier Old Men".

**d10: Michael Flessas**

- [d10s0] Michael C. Flessas (born June 2, 1959 in Miami, Florida), is the birth name of American actor Michael Flessas, who is of Greek ancestry.
- [d10s1]  Flessas' most notable film role was "Angry Man" in the Cannes Film Festival 2000 Palme d'Or winning film "Dancer in the Dark" directed by Danish film director Lars von Trier.
- [d10s2]  Originally, the director himself considered playing the role but, instead, the role was given to Flessas.
- [d10s3]  "Dancer in the Dark" starred Icelandic singer/actress Björk who won the Best Actress award at Cannes for her role.
- [d10s4]  French film icon, César Award winner, and Academy Award nominee Catherine Deneuve, and other noteworthy artists such as Academy Award and Tony Award winner Joel Grey, Peter Stormare, David Morse, and Stellan Skarsgård also performed in the multiple prize winning film.
- [d10s5]  One of Björk's songs for the film received an Academy Award nomination for Best Song.

## 7. hotpotqa_5a7329c65542992359bc3256

原位置：`train` 第 127 题 · 全局第 127 题 · `sample_id: hotpotqa_5a7329c65542992359bc3256`

Question: What is situated in the City of Timmins, Ontario, Canada,  Dome Mine or Con Mine?

Note:

Type: comparison · fallback: False · SFT snapshots: 6

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | whether Dome Mine is situated in the City of Timmins, Ontario, Canada | False | () |
| u2 | whether Con Mine is situated in the City of Timmins, Ontario, Canada | False | () |
| u3 | which mine is situated in the City of Timmins, Ontario, Canada | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Dome Mine is situated in the City of Timmins, Ontario, Canada | False | [] | yes | [['d6s0']] |
| u2 | whether Con Mine is situated in the City of Timmins, Ontario, Canada | False | [] | no | [] |
| u3 | which of Dome Mine and Con Mine is situated in the City of Timmins, Ontario, Canada | True | ['u1', 'u2'] | Dome Mine | [[]] |

### Source documents (reference only)

**d1: Kidd Mine**

- [d1s0] Kidd Mine is an underground base metal mine in the city of Timmins, Ontario, Canada.
- [d1s1]  It is owned by Glencore Inc., and operated by Kidd Operations, a Glencore subsidiary.
- [d1s2]  The mine was formerly owned by Xstrata Copper, Falconbridge Ltd., and Texas Gulf Sulphur.
- [d1s3]  Ore from the Kidd Mine is processed into concentrate at the Kidd Metallurgical Site, located 27 km southeast of the mine, which until 2010 also smelted the ore and refined the metal produced.
- [d1s4]  Following the closure of the majority of the Met Site, concentrate is now shipped to Quebec for processing.
- [d1s5]  Kidd Mine is the world's deepest copper/zinc mine.

**d2: Ida Dome mine**

- [d2s0] The Ida Dome mine is a large mine located in the western part of Namibia in Erongo Region.
- [d2s1]  Ida Dome represents one of the largest uranium reserves in Namibia, with estimated reserves of 53 million tonnes of ore grading 0.018% uranium.

**d3: Jamie Lim**

- [d3s0] Jamie Lim (born February 23, 1959 in Timmins, Ontario) was Mayor of Timmins from 2000 to 2003.
- [d3s1]  She was educated at the University of Western Ontario; she holds a Bachelor of Arts and Bachelor of Education degree.
- [d3s2]  Lim was an elected school board trustee and city councillor (1997) for Timmins City Council before being elected mayor in 2000, succeeding veteran mayor Victor M. Power on his retirement.
- [d3s3]  She was Timmins' first female mayor.
- [d3s4]  During her tenure as mayor, she was elected third vice-president of the Federation of Canadian Municipalities.

**d4: Negus Mine**

- [d4s0] Negus Mine was a gold producer at Yellowknife, Northwest Territories, Canada, from 1939 to 1952.
- [d4s1]  It produced 255,807 troy ounces (7956 kg) of gold from 490,808 tons of ore milled.
- [d4s2]  The underground workings were acquired by adjacent Con Mine in 1953 and were used for ventilation purposes until Con Mine closed in 2003.

**d5: Con Mine**

- [d5s0] The Con Mine (1938-2003) was the first gold mine developed in the Northwest Territories, Canada, just south of Yellowknife.
- [d5s1]  The property was staked by Consolidated Mining and Smelting Company of Canada (Cominco) in September 1935 in response to the discovery of visible gold nearby; the name "Con" is an abbreviation of "Consolidated".
- [d5s2]  The advent of winter prevented any prospecting from being conducted, but work in the summer of 1936 led to the discovery of numerous gold veins.
- [d5s3]  The Con Mine entered production in 1938 and ceased operations in 2003.
- [d5s4]  It has produced over 5000000 ozt of gold from 12,195,585 tons of ore processed.
- [d5s5]  The mine was over 6000 ft deep.

**d6: Dome Mine**

- [d6s0] Dome Mine is situated in the City of Timmins, Ontario, Canada; and was developed during the Porcupine Gold Rush.

**d7: Brigus Gold**

- [d7s0] Brigus Gold Corporation was a Canadian mining company.
- [d7s1]  The company was based in Halifax, Nova Scotia Canada and operated Black Fox Mine and Mill in the Timmins Gold District of Ontario.
- [d7s2]  The Black Fox Complex encompasses the Black Fox Mine, the new Grey Fox property and adjoining properties in the Township of Black River-Matheson, Ontario, Canada.
- [d7s3]  The Black Fox Mine is in production and the Grey Fox Mine, located four kilometres from Black Fox is in development.

**d8: Hollinger Mines**

- [d8s0] The Hollinger Gold Mine was founded by Benny Hollinger in Timmins, Ontario, and in 1910 the company was incorporated by Noah Timmins and partners.
- [d8s1]  The main Hollinger Mine operated from 1910 until 1968.
- [d8s2]  During that period 65,778,234 tons were milled, producing 19,327,691 ounces of gold, indicating an overall grade of 0.29.
- [d8s3]  The value of the gold produced is placed at $564.7 million.

**d9: Copperfields Mine**

- [d9s0] Copperfields Mine, originally known as Temagami Mine, is an abandoned copper and silver mine on Temagami Island in Lake Temagami, Ontario, Canada.
- [d9s1]  The mine opened in 1955 and comprises both underground and surface workings within a sulfide ore body.
- [d9s2]  Situated in Phyllis Township, the mine produced 34,000,000 dollars Canadian with 80 million pounds of copper, 230,028 ounces of silver and 13,271 ounces of gold.
- [d9s3]  It was considered to be the largest deposit of nearly pure chalcopyrite ever discovered in Canada.
- [d9s4]  A mill was not initially needed because the ore was 28% copper.
- [d9s5]  The mine closed in 1972 and is now flooded by water.
- [d9s6]  Ruins of the Copperfields mill are present as foundations.
- [d9s7]  It is possible to find mineral specimens in the spoil heaps of the old mine, such as chalcopyrite, pyrite, bornite, malachite, dolomite, hessite, merenskyite, millerite, palladium, quartz and others.
- [d9s8]  The Lake Temagami Access Road was created to ship ore from the mine site.

**d10: Timmins Transit**

- [d10s0] Timmins Transit provides public transportation services to the City of Timmins in north eastern Ontario, Canada.
- [d10s1]  The system is operated as a department of the City of Timmins, which also owns and operates the Timmins/Victor M. Power Airport.
- [d10s2]  Over the past few years, after a decade of decline, Timmins Transit has experienced some of the fastest ridership growth in the country.

## 8. hotpotqa_5a73301e55429901807dafad

原位置：`train` 第 128 题 · 全局第 128 题 · `sample_id: hotpotqa_5a73301e55429901807dafad`

Question: Pixie Geldof's mother died of what cause?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | mother of Pixie Geldof | False | () |
| u2 | cause of death of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | mother of Pixie Geldof | False | [] | Paula Yates | [['d9s1']] |
| u2 | cause of death of {u1} | True | ['u1'] | heroin overdose | [['d10s2']] |

### Source documents (reference only)

**d1: Kwanumsa (Kaesong)**

- [d1s0] Kwanŭm-sa is a Korean Buddhist temple located within Taehung Castle on Mt. Chonma near Kaesong, North Korea.
- [d1s1]  The site is one of the National Treasures of North Korea.
- [d1s2]  Named after Guanyin, the buddhist bodhisattva of compassion, this small temple is located in the beautiful valley between Mts.
- [d1s3]  Chonma and Songgo.
- [d1s4]  The temple was founded in 970 when a monk deposited two marble statues of the goddess in a cave behind the temple's current location.
- [d1s5]  The temple itself was constructed in 1393 under the Koryo Dynasty, and later renovated in 1646 under the Joseon.
- [d1s6]  The site contains many ancient relics, including a seven-story pagoda from the Koryo dynasty and the ancient Guanyin statues in Kwanum Cave.
- [d1s7]  The doors of the main shrine, known as the Taeung Hall, are decorated with carved flowers and leaves; an old legend relays why the decorations on one door are unfinished.
- [d1s8]  During the reconstruction of the temple during the Joseon dynasty, one of the main carvers was a twelve-year-old boy named Unna, famed for his skill in carving.
- [d1s9]  One day, while working on the temple, he heard his mother was seriously ill, and asked to be allowed to visit her.
- [d1s10]  He was refused, and his mother died shortly after.
- [d1s11]  He blamed himself and his skillful hands for his mother's death, and so out of grief used his carving axe to chop off his hand.
- [d1s12]  He then disappeared into the forest, never to be seen again.
- [d1s13]  Today, a carving of a boy with one hand ascending to heaven on the back of a white tiger can still be seen on the unfinished door.

**d2: Yo Hitoto**

- [d2s0] Yo Hitoto (一青 窈 , Hitoto Yō , born September 20, 1976) is a Japanese pop singer.
- [d2s1]  Her mother is Japanese and her father is Taiwanese.
- [d2s2]  She can speak three languages: Japanese, English, and Mandarin.
- [d2s3]  Tae Hitoto is her older sister.
- [d2s4]  Her name Hitoto is not her real surname, it is her mother's maiden name.
- [d2s5]  She changed her name when she came to Japan.
- [d2s6]  Her father died when she was very young, and her mother died when she was 16.

**d3: On Our Own (film)**

- [d3s0] The film starts with Peggy Williams's mother talking to her on the phone asking her to start from the beginning of the story.
- [d3s1]  An ambulance rushes to the hospital with the mother of four children.
- [d3s2]  It then goes by the children's apartment to tell them their mother died.
- [d3s3]  The four children, Mitch, Kate, Travis, and Lori go to the Los Angeles Courthouse with their neighbor, Mrs. Forsythe.
- [d3s4]  She tells the judge they have no family and that she is unable to take them in.
- [d3s5]  Kate tells the judge and Mr. Arnold that they have an Uncle Jack, but they don't believe Kate and the Judge decides to put them in a foster home until they get adopted.
- [d3s6]  In the foster home a grumpy nurse yells at Travis and Lori for jumping on a bed when Mr. Arnold comes in and tells them that Lori is going to be adopted.
- [d3s7]  Mitch is angry that he didn't tell them they would be split up and makes a plan to run away.
- [d3s8]  They escape to their old home where Mitch collects all the money he can find, (9 dollars), and his Uncle Jack's address, knowing Jack will know where their father is.
- [d3s9]  They also manage to get their dog back.
- [d3s10]  They then get into their mother's old car and drive away, with neighbors spotting them.

**d4: Ruth Rappaport**

- [d4s0] Ruth Rappaport (May 27, 1923 – November 17, 2010) was a Jewish-American librarian.
- [d4s1]  Her mother's cousin was Helena Rubinstein.
- [d4s2]  Rappaport was born in Leipzig, in Saxony; her family moved to Switzerland in 1938.
- [d4s3]  She later came to America.
- [d4s4]  Her parents returned to Germany, and in 1943 her father died in Buchenwald and her mother died in Ravensbrueck.

**d5: 1962 Mexico City radiation accident**

- [d5s0] In March–August 1962, a radiation incident in Mexico City occurred when a ten-year-old boy took home an unprotected industrial radiography source.
- [d5s1]  Four people died from overexposure to radiation from a 5-Ci cobalt-60 capsule, an industrial radiography orphaned source that was not contained in its proper shielding.
- [d5s2]  For several days, the boy kept the capsule in his pocket, then placed it in the kitchen cabinet of his home in Mexico City.
- [d5s3]  Having obtained the source on March 21, the boy died 38 days later on April 29.
- [d5s4]  Subsequently, his mother died on July 10; his 2-year-old sister died on August 18, and his grandmother died on October 15 of that year.
- [d5s5]  The boy's father also received a significant dose of radiation, however he survived.
- [d5s6]  Five other individuals also received significant overdoses of radiation.

**d6: Rose Porter**

- [d6s0] Rose Porter (6 December 1845 - 10 September 1906) was an American religious novelist.
- [d6s1]  She was born in New York, New York.
- [d6s2]  Her father, David Collins Porter, was a wealthy New Yorker.
- [d6s3]  He died in 1845, while Rose was an infant.
- [d6s4]  Her mother, Rose Anne Hardy, was the daughter of an English army officer.
- [d6s5]  Porter's early years were spent in New York and in the family's summer home in Catskills-on-the-Hudson.
- [d6s6]  She was educated in New York, with the exception of a year abroad.
- [d6s7]  After completing her education, she and her mother made their home in New Haven, Connecticut.
- [d6s8]  After the mother died, Porter kept her home in New Haven, where she lived with her servants.
- [d6s9]  Her first success was "Summer Drift-Wood for the Winter Fire".
- [d6s10]  Notwithstanding the fact that she was an invalid for years, Porter was a writer of quiet religious romance, publishing or editing 70 volumes.

**d7: List of The Saddle Club characters**

- [d7s0] Carole is a bright African American girl with a natural riding ability.
- [d7s1]  She became devastated when her mother died of cancer, and when Cobalt died, she almost gave up riding.
- [d7s2]  But her father, U.S. Marine Colonel Mitch Hanson, reminded Carole that her mother would have wanted her to follow her passion.
- [d7s3]  With money left by her mother, she bought a buckskin gelding, Starlight.
- [d7s4]  Carole knows her future lies with horses, but there are many paths to follow and she does not know which road to take.
- [d7s5]  Her grades are high enough for her to become a veterinarian but she would also love to breed and train Thoroughbreds.
- [d7s6]  She would not mind being a professional steeplechase jockey, or maybe traveling the world teaching dressage clinics.
- [d7s7]  Whatever career she chooses, her most immediate goal is to be the very best rider she can be.
- [d7s8]  Carole has little time for boys; therefore, she has never understood why anyone would prefer the company of a boy to that of a horse.
- [d7s9]  This is when the pressures of family, friends, school and competition cannot touch her.
- [d7s10]  Anyone who catches a glimpse of horse and rider moving as one along the lush creek cannot help but be in awe.
- [d7s11]  Like the other Saddle Club girls, Carole is becoming a young woman.
- [d7s12]  In "Moving On, Part 1", Carole's dad got re-deployed and she almost left Pine Hollow, The Saddle Club, and Starlight behind forever when it was decided that she'd live with her Aunt Penny.
- [d7s13]  Thanks to Mrs. Reg, however, Carole becomes the first live in boarder at Pine Hollow Stables as of "Moving On, Part 2" which allowed her to stay at Pine Hollow, continue to be in The Saddle Club, and keep Starlight.
- [d7s14]  Carole has never forgiven Veronica for killing Cobalt.
- [d7s15]  In "Itchy", Carole thought that she was allergic to horses, but after a visit to the doctor it was revealed that she is allergic to camels as the saddle blanket that her father sent her is made out of camel hair.
- [d7s16]  When Carole suggests naming Samson after "Samson and Delilah", it was a hinted indication that Carole is a Christian.
- [d7s17]  Whenever Carole's sad, to cheer herself up she'll ride Starlight or play her guitar.
- [d7s18]  Carole is focused, determined, stubborn, and passionate just like her mother was.
- [d7s19]  In the books, Carole and Lisa go to Willow Creek Junior High School together and Carole and Stevie are the same age.
- [d7s20]  in the "Pine Hollow" series Carole goes to Willow Creek High School with Lisa.
- [d7s21]  Carole's favorite color is Purple.

**d8: Yogamaharishi Swami Gitananda**

- [d8s0] Yogamaharishi Dr Swami Gitananda Giri Guru Maharaj was born on 24 July 1907, in Maharajganj, northern India, to an Irish mother and a Sindhi father.
- [d8s1]  His father, Sukraj Bhavanani, was a High court Advocate in the Patna High Court and an extensive landowner.
- [d8s2]  His mother Leelavathi was converted to Hinduism through the Arya Samaj rites.
- [d8s3]  Yogamaharishi received his early schooling at home from his mother.
- [d8s4]  Tragically, his mother died when he was but eight years of age.
- [d8s5]  When he was ten years, his Guru, the great Siddha and Master, Yogamaharishi Swami Kanakananda Bhrigu, (Ram Gopal Majumdar) entered his life.
- [d8s6]  For six years, he studied in the Guru Kula of his Master, imbibing not only the traditional education, but also the great mystic sciences of Yoga, Tantra and Yantra.

**d9: Pixie Geldof**

- [d9s0] Little Pixie Geldof (born 17 September 1990) is an English model and singer.
- [d9s1]  She is the third daughter of Bob Geldof and Paula Yates.

**d10: Paula Yates**

- [d10s0] Paula Elizabeth Yates (24 April 1959 – 17 September 2000) was an English television presenter and writer, best known for her work on two television programmes, "The Tube" and "The Big Breakfast".
- [d10s1]  She was in a relationship with musician Bob Geldof from 1976 to 1996.
- [d10s2]  She died of a heroin overdose in 2000.

## 9. hotpotqa_5a733a2e5542994cef4bc4df

原位置：`train` 第 129 题 · 全局第 129 题 · `sample_id: hotpotqa_5a733a2e5542994cef4bc4df`

Question: Which of these two men worked as a professor at New York University, Frankie Kazarian or Paul Boghossian?

Note:

Type: comparison · fallback: False · SFT snapshots: 7

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | whether Frankie Kazarian worked as a professor at New York University | False | () |
| u2 | whether Paul Boghossian worked as a professor at New York University | False | () |
| u3 | which of them worked as a professor at New York University | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Frankie Kazarian worked as a professor at New York University | False | [] | no | [['d3s0']] |
| u2 | whether Paul Boghossian worked as a professor at New York University | False | [] | yes | [['d8s0']] |
| u3 | which of Frankie Kazarian and Paul Boghossian worked as a professor at New York University | True | ['u1', 'u2'] | Paul Boghossian | [[]] |

### Source documents (reference only)

**d1: Kurt Herlth**

- [d1s0] Kurt Herlth (1896–1966) was a German art director known for his designs of film sets. His brother Robert Herlth was also an art director active in the German film industry, and the two men worked together a number of times.

**d2: Inside Burma: Land of Fear**

- [d2s0] Inside Burma: Land of Fear is a 1996 Central Independent Television documentary, written and presented by John Pilger, which was directed by David Munro.
- [d2s1]  The two men worked undercover in order to investigate the use of slave labour in Burma.

**d3: Frankie Kazarian**

- [d3s0] Frank Benedict Gerdelman (born August 4, 1977) is an American professional wrestler.
- [d3s1]  He is signed with Ring of Honor (ROH) under the ring name Frankie Kazarian and is a two-time ROH World Tag Team Champion with Christopher Daniels.
- [d3s2]  He is best known for his work with Total Nonstop Action Wrestling (TNA), under the ring names Kazarian and Kaz, he also wrestled under the gimmick of Suicide.

**d4: K. R. Sreenivasan**

- [d4s0] Katepalli R. Sreenivasan is an engineer whose research includes physics and applied mathematics.
- [d4s1]  He studies turbulence, nonlinear and statistical physics, astrophysical fluid mechanics, and cryogenic helium.
- [d4s2]  He is the dean of engineering and executive vice provost for science and technology of New York University.
- [d4s3]  Sreenivasan is also the Eugene Kleiner Professor for Innovation in Mechanical Engineering at New York University Tandon School of Engineering, and a professor of physics and mathematics professor at the New York University Graduate School of Arts and Science and Courant Institute of Mathematical Sciences.

**d5: JAPW New Jersey State Championship**

- [d5s0] The JAPW New Jersey State Championship was a title in the Jersey All Pro Wrestling professional wrestling promotion.
- [d5s1]  Being a professional wrestling championship, it is not won via direct competition; it is instead won via a predetermined ending to a match or awarded to a wrestler because of a wrestling angle.
- [d5s2]  It became an official title on September 25, 1998 with Flash Wheeler becoming the first champion.
- [d5s3]  It was retired on June 7, 2002.
- [d5s4]  On September 15, 2006; Frankie Kazarian was declared the New Jersey State Champion after the Light Heavyweight Championship was retired.
- [d5s5]  The current champion is Brodie Lee and he is in his first reign as champion.
- [d5s6]  There have been 17 reigns by 15 wrestlers with two vacancies.
- [d5s7]  One of the vacancies came when Reckless Youth was injured and vacated the title himself.

**d6: Nasir Memon**

- [d6s0] Nasir Memon is a computer scientist based in Brooklyn, New York.
- [d6s1]  Memon is a professor and chair of the New York University Tandon School of Engineering computer science and engineering department and affiliate faculty at the computer science department in the Courant Institute of Mathematical Sciences at New York University.
- [d6s2]  He is also the Department Head of NYU Tandon Online, the online learning unit of the school.
- [d6s3]  He introduced cyber security studies to New York University Tandon School of Engineering, making it one of the first schools to implement the program at the undergraduate level.
- [d6s4]  Memon holds twelve patents in image compression and security.
- [d6s5]  He is the founding director of the Center for Interdisciplinary Studies in Security and Privacy (CRISSP) and CRISSP Abu Dhabi.
- [d6s6]  In 2002, Memon founded Cyber Security Awareness Week (CSAW), an annual conference where tens of thousands of students compete in events and learn skills in cyber security Memon is also co-founder of Digital Assembly, a software company that develops digital forensics and data recovery and Vivic, a company that produces malware detection software.
- [d6s7]  Memon has published over 250 articles in journals and conferences and has contributed to articles regarding cyber security in magazines such as "Crain’s New York Business", "Fortune", and "USA Today".
- [d6s8]  His research has been featured in "NBC Nightly News", "The New York Times", "MIT Review", "Wired.Com", and "New Science Magazine".

**d7: Myles Jackson**

- [d7s0] Myles W. Jackson (born Paterson, New Jersey on 25 November 1964) is currently the Albert Gallatin Research Excellence Professor of the History of Science at New York University-Gallatin, Professor of History of the Faculty of Arts and Science of New York University, Professor of the Division of Medical Bioethics of NYU-Langone School of Medicine, Faculty Affiliate of the Engelberg Center on Innovation Law and Policy, NYU School of Law, and Director of Science and Society of the College of Arts and Science at NYU.
- [d7s1]  He was the inaugural Dibner Family Professor of the History and Philosophy of Science and Technology at Polytechnic Institute of New York University from 2007 to 2012.
- [d7s2]  The chair is named after Bern Dibner (1897 – 1988), an electrical engineer, industrialist, historian of science and technology and alumnus of Polytechnic Institute of Brooklyn.

**d8: Paul Boghossian**

- [d8s0] Paul Boghossian is Silver professor of philosophy at New York University in the NYU Department of Philosophy, where he was Chair of the Department for ten years (1994–2004) and responsible for building it into one of the top philosophy programs in the world.
- [d8s1]  His research interests include epistemology, the philosophy of mind, and the philosophy of language.
- [d8s2]  He is Director of the New York Institute of Philosophy and Distinguished Research Professor of Philosophy at the University of Birmingham.

**d9: Sackets Harbor Battlefield State Historic Site**

- [d9s0] Sackets Harbor Battlefield State Historic Site is a historically important location in Jefferson County, New York, United States.
- [d9s1]  The historic site is south of the Village of Sackets Harbor, bordering Lake Ontario in the Town of Hounsfield.
- [d9s2]  Two battles were fought near this location during the War of 1812.
- [d9s3]  Some 3,000 men worked at the shipyard building warships, and the village was fortified and garrisoned with thousands of troops.

**d10: Lawrence Schiffman**

- [d10s0] Lawrence H. Schiffman (born 1948) is a professor at New York University (as of 2014); he was formerly Vice-Provost of Undergraduate Education at Yeshiva University and Professor of Jewish Studies (from early 2011 to 2014).
- [d10s1]  He had previously been Chair of New York University’s Skirball Department of Hebrew and Judaic Studies and served as the Ethel and Irvin A. Edelman Professor in Hebrew and Judaic Studies at New York University (NYU).
- [d10s2]  He is a specialist in the Dead Sea Scrolls, Judaism in Late Antiquity, the history of Jewish law, and Talmudic literature.

## 10. hotpotqa_5a736dc755429901807db04e 【需改：生成拆解】

原位置：`train` 第 130 题 · 全局第 130 题 · `sample_id: hotpotqa_5a736dc755429901807db04e`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5a736dc755429901807db04e"></a>

> **审阅结论：需改：生成拆解**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** member 1/member 2 没有实体名称、来源单元或可解析的占位符，两个“成员”是谁没有定义。
>
> **处理建议：** 先增加 Hi-Gate 成员识别单元，再选择其中在1995年获 No.1 DJ 的成员；采用旧 gold 的两阶段结构或定义清楚的候选集合，不能使用无绑定的 member 1/2。
>
> **证据定位：** d4s0, d5s2；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Out of the two members of Hi-Gate, which was voted the No. 1 DJ in the world in 1995?

Note:

Type: comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | whether member 1 of Hi-Gate was voted No. 1 DJ in the world in 1995 | False | () |
| u2 | whether member 2 of Hi-Gate was voted No. 1 DJ in the world in 1995 | False | () |
| u3 | which member of Hi-Gate was voted No. 1 DJ in the world in 1995 | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | two members of Hi-Gate | False | [] | Judge Jules and Paul Masterson | [['d4s0']] |
| u2 | which of {u1} was voted the No. 1 DJ in the world in 1995 | True | ['u1'] | Judge Jules | [['d5s2']] |

### Source documents (reference only)

**d1: Assfactor 4**

- [d1s0] Assfactor 4 was a hardcore punk band from Columbia, South Carolina formed by two members of Tonka (Jay and Alex) and two members of Unherd (Eric and Kevin).
- [d1s1]  They formed in the fall of 1992 and broke up in late 1997.
- [d1s2]  Assfactor 4's sonic approach drew heavily from San Diego's early-1990s group Heroin, but their song structure was notably more akin to 1980's thrash and hardcore, placing Assfactor 4 in a unique position within the DIY hardcore scene of the era.
- [d1s3]  Their contemporaries in the southeast U.S. included Columbia's In/Humanity and Premonition, Raleigh, NC's Rights Reserved; and Richmond, VA's Action Patrol.
- [d1s4]  HeartattaCkzine readers voted Assfactor 4 "Coolest Band to Hang Out With" in 1995.
- [d1s5]  Assorted Porkchops has planned on releasing a discography in the near future.

**d2: Paul Oakenfold**

- [d2s0] Paul Mark Oakenfold (born 30 August 1963) is an English record producer and trance DJ.
- [d2s1]  He is a two time Grammy Award and two time World Music Awards nominee.
- [d2s2]  He was voted the No. 1 DJ in the World twice in 1998 and 1999 by DJ Magazine.
- [d2s3]  Paul has provided over 100 remixes for over 100 artists including U2, Moby, Madonna, Massive Attack, New Order, The Rolling Stones, The Stone Roses etc.

**d3: Hardwell**

- [d3s0] Robbert van de Corput (born 7 January 1988), who performs under the stage name Hardwell, is a Dutch electro house DJ, record producer and remixer.
- [d3s1]  He was voted the World's No. 1 DJ on "DJ Mag" in 2013, and again in 2014.
- [d3s2]  He was ranked at No. 3 on "DJ Mag" Top 100 DJs 2016 poll.
- [d3s3]  Hardwell is best known for his sets at music festivals, including Ultra Music Festival, Sunburn and Tomorrowland.

**d4: Hi-Gate**

- [d4s0] Hi-Gate is the dance music pairing of BBC Radio 1 DJ Judge Jules, and Paul Masterson.

**d5: Judge Jules**

- [d5s0] Judge Jules (born Julius O'Riordan, 26 October 1966) is a British dance music DJ, producer and entertainment lawyer.
- [d5s1]  Known for his DJ activities, music production and popular radio show which achieved global success.
- [d5s2]  He was voted the No. 1 DJ in the World by DJ Magazine in 1995.

**d6: Aba Shanti-I**

- [d6s0] Aba Shanti-I (real name Joseph Smith) is a sound system operator and dub producer from the UK.
- [d6s1]  Aba and his sound system have been playing through UK and Europe for over 30 years.
- [d6s2]  He has been a resident sound system at Notting Hill Carnival since 1993 and was voted the No. 1 DJ in the World by DJ Magazine in the same year.

**d7: Sasha (Welsh DJ)**

- [d7s0] Sasha (born Alexander Paul Coe on 4 September 1969 in Bangor, Gwynedd, Wales) is a Welsh DJ, record producer and Grammy Award nominee.
- [d7s1]  He was voted World No. 1 DJ in 2000 in a poll conducted by DJ Magazine.
- [d7s2]  He is a four-time International Dance Music Awards winner and four-time DJ Awards winner.

**d8: Shaun David Barker**

- [d8s0] Shaun David Barker is an Australian born talent manager, marketing executive and executive music producer.
- [d8s1]  He manages and markets Australian DJ’s including Timmy Trumpet, Stafford Brothers and tyDi, who have all been voted the number 1 DJ’s in Australia at the ITM Awards.

**d9: John Digweed**

- [d9s0] John Digweed (born 1 January 1967 in Hastings, England) is an English DJ, record producer and actor.
- [d9s1]  DJ Magazine voted him World No 1 DJ in 2001.

**d10: DJ Khushi**

- [d10s0] DJ Khushi is a disc jockey in India and has been awarded the Most Popular Bollywood DJ award.
- [d10s1]  Because of his frequent appearances, Khushi is also known as the official DJ of Shahrukh Khan.
- [d10s2]  He was the opening DJ during Tiesto's Delhi Gig.
- [d10s3]  In 2016, he headlined the Sunburn Music Festival with Hardwell, the world's No.1 DJ.
- [d10s4]  In Dec'16, Ellie Goulding and Nervo performed alongside DJ Khushi.
- [d10s5]  Khushi has also performed with LMFAO, Edward Maya and Akcent.

## 11. hotpotqa_5a74797655429929fddd843f

原位置：`train` 第 131 题 · 全局第 131 题 · `sample_id: hotpotqa_5a74797655429929fddd843f`

Question: Which pizza shop was created by a company merger, Papa Murphy's or Hungry Howie's Pizza?

Note:

Type: comparison · fallback: False · SFT snapshots: 5

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | whether Papa Murphy's was created by a company merger | False | () |
| u2 | whether Hungry Howie's Pizza was created by a company merger | False | () |
| u3 | which pizza shop was created by a company merger | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Papa Murphy's was created by a company merger | False | [] | yes | [['d6s1']] |
| u2 | whether Hungry Howie's Pizza was created by a company merger | False | [] | no | [] |
| u3 | which of Papa Murphy's and Hungry Howie's Pizza was created by a company merger | True | ['u1', 'u2'] | Papa Murphy's | [[]] |

### Source documents (reference only)

**d1: Gem Saloon**

- [d1s0] The Gem Saloon, at 808 Main St. in Thompson Falls, Montana, was built in 1914.
- [d1s1]  It is a historic building listed on the U.S. National Register of Historic Places.
- [d1s2]  It has also been used by, and known as, Napa Auto Parts, and has served as a restaurant, too.
- [d1s3]  When photographed in 2013 it held a pizza shop.

**d2: Papa Murphy's Park**

- [d2s0] Papa Murphy's Park (formerly known as the Cal Expo Multi-Use Sports Field Facility and Bonney Field) is a sports venue located on the grounds of Cal Expo in Sacramento, California.
- [d2s1]  The soccer-specific stadium has a capacity of 11,569 and includes a full-sized (120 x 80 yard) soccer field.
- [d2s2]  Papa Murphy's Park is the current home of Sacramento Republic FC soccer team and former home of PRO Rugby team, Sacramento Express.

**d3: Peter Gregg (musician)**

- [d3s0] Peter Gregg (born March 6, 1951, Kent, Ohio) is a producer and musician.
- [d3s1]  Gregg played lead guitar on the earliest recordings of the prototype predecessor to the musical group Devo, under his nom de guitar, Coupe de Ville.
- [d3s2]  In 1971, Gregg, along with Devo co-founders Gerald Casale and Bob Lewis recorded three songs: "I Been Refused", "I Need a Chick" and "Auto Mowdown" on primitive recording equipment located over Guido's Pizza Shop in Kent, Ohio

**d4: Jeff LaBar**

- [d4s0] Jeffrey Philip LaBar (born March 18, 1963, in Darby, Pennsylvania) is an American guitarist most famous for playing in the band Cinderella, in which he replaced original guitarist Michael Smerick, also known as Michael Kelly Smith.
- [d4s1]  LaBar also has a side band with Cinderella bandmate Eric Brittingham called Naked Beggars.
- [d4s2]  During Cinderella's temporary break-up in the mid-1990s, LaBar supported himself by running a pizza shop with his brother and by doing assorted construction jobs.
- [d4s3]  LaBar and Cinderella recently completed their 20th anniversary tour with fellow rock veterans Poison, who were also celebrating 20 years in the business.

**d5: Fresno, Ohio**

- [d5s0] Fresno is a census-designated place in eastern White Eyes Township, Coshocton County, Ohio, United States.
- [d5s1]  As of the 2010 census it had a population of 140.
- [d5s2]  Although it is unincorporated, it has a post office, with the ZIP code of 43824, gas station, White Eyes Carryout/Drive Thru and Pizza Shop.
- [d5s3]  It lies along State Route 93 between West Lafayette and Baltic.

**d6: Papa Murphy's**

- [d6s0] Papa Murphy's, a business based in Vancouver, Washington, United States, is a take-and-bake pizza company.
- [d6s1]  It began in 1995 as the merger of two take-and-bake pizza companies: Papa Aldo's Pizza (founded in 1981) and Murphy's Pizza (founded in 1981).
- [d6s2]  The company and its franchisees operate more than 1,300 outlets in the United States and Canada.
- [d6s3]  Papa Murphy's is the fifth-largest pizza chain in the United States.

**d7: Pictou County pizza**

- [d7s0] Pictou County Pizza is a regional variant of pizza found in Pictou County, Nova Scotia.
- [d7s1]  The style of pizza is unique, owing to its "brown sauce" and Halifax-made pepperoni.
- [d7s2]  The pizza can be shipped frozen across Canada via an arrangement between a local pizza shop and the local UPS agent.
- [d7s3]  The most common destination being Fort McMurray, Alberta with a two-day delivery time.
- [d7s4]  Since 2014 an annual competition between pizza makers in Pictou County has been held, with awards being given under a People's Choice category and as selected by a panel of judges.

**d8: Hungry Howie's Pizza**

- [d8s0] Hungry Howie's Pizza & Subs, Inc., also known as Hungry Howie's Pizza, is a franchise and the 11th largest pizza chain in the United States, with over 550 locations.
- [d8s1]  Hungry Howie's products include pizza, calzone-style subs, chicken wings and tenders, bread, salads, and brownies. Its headquarters are located in Madison Heights, Michigan in Metro Detroit.

**d9: WWE Slam City**

- [d9s0] WWE Slam City was an animated show produced by WWE, which aired on the WWE Network and Wednesday evenings on Nicktoons.
- [d9s1]  WWE Slam City was based on the Mattel action figure series starring toyetic versions of the WWE roster circa 2013.
- [d9s2]  The series, filmed in the next generation of stop-motion animation, features a new WWE animated character The Finisher, who fires all of the WWE wrestlers and sends them to Slam City to find day jobs.
- [d9s3]  The wrestlers are plunged into new career challenges as they pack every street corner with work to do and scores to settle.
- [d9s4]  With John Cena as an auto mechanic, Rey Mysterio as a traffic guard, Alberto Del Rio as a coffee house barista, Mark Henry as a pizza shop mascot, CM Punk as an ice-cream man, Dolph Ziggler as an industry leader, Randy Orton as a zookeeper, Kane as a chef and Sheamus as a theater usher.
- [d9s5]  Daniel Bryan, The Miz, Big Show, Brock Lesnar, Santino Marella and Damien Sandow are still jobless but Santino and Sandow are the most desperate to find one.
- [d9s6]  WWE Legends Stone Cold and The Rock are also featured in Slam City.
- [d9s7]  The 'Stretch Move' feature of Slam City characters is highlighted in WWE Slam City.

**d10: Mr. Football Award (Michigan)**

- [d10s0] The Michigan Mr. Football Award is an honor accorded to a high school football player from Michigan.
- [d10s1]  It is sponsored by Hungry Howie's, and is awarded based on a combination of player performance and fan voting.

## 12. hotpotqa_5a752d375542996c70cfaea4 【保留新拆法｜重标人工标签】

原位置：`train` 第 132 题 · 全局第 132 题 · `sample_id: hotpotqa_5a752d375542996c70cfaea4`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5a752d375542996c70cfaea4"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新单元直接询问两对象的共同类别，旧单元分别查类别再合并。新单元包含两个对象且要求共同类别，联合两方证据即可支持；单元更少本身不是错误。
>
> **处理建议：** 保留 single。将旧共同类别结论的值迁移到新u1，并为它建立覆盖两方事实的联合支持集合。只看到一方时仍应 UNRESOLVED；不为恢复旧粒度新增单元。
>
> **证据定位：** d6s0, d8s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: American Hairless Terrier and Old Danish Pointer, are breeds of which animal?

Note:

Type: single · fallback: False · SFT snapshots: 7

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | animal breed for American Hairless Terrier and Old Danish Pointer | True | () |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | animal of which the American Hairless Terrier is a breed | False | [] | dog | [['d6s0']] |
| u2 | animal of which the Old Danish Pointer is a breed | False | [] | dog | [['d8s0']] |
| u3 | animal of which both the American Hairless Terrier and Old Danish Pointer are breeds | True | ['u1', 'u2'] | dog | [[]] |

### Source documents (reference only)

**d1: Russkiy Toy**

- [d1s0] The Russian Toy (also known as the Russian Toy Terrier, and in Russia as the Russkiy Toy, Toychik,Russian: Русский той, Тойчик ) is a very small breed of dog originally bred in Russia from the English Toy Terrier which is known today as the Manchester Terrier.
- [d1s1]  There are two types of coats in the breed: smooth coat and long coat.
- [d1s2]  The smooth-coated variety was previously known as the Russian Toy Terrier and long-coated as the Moscow Long Haired Toy Terrier.
- [d1s3]  Both were brought together under the same Russian Toy Terrier name in 1988 and the "Terrier" was dropped from the name when the breed was added in 2006 to the official list of breeds registered with the Fédération Cynologique Internationale and has been registered in the Foundation Stock Service of the American Kennel Club since 2008, allowed to compete in AKC companion events since 2010.
- [d1s4]  The first official breed standard of the two varieties was written in 1966 in Russia.

**d2: Teddy Roosevelt Terrier**

- [d2s0] The Teddy Roosevelt Terrier is a small to medium-sized American hunting terrier.
- [d2s1]  Lower-set with shorter legs, more muscular, and heavier bone density than its cousin the American Rat Terrier.
- [d2s2]  There is much diversity in the history of the Teddy Roosevelt Terrier breed and it shares a common early history with the American Rat Terrier, Fox Paulistinha and Tenterfield Terrier.
- [d2s3]  It is said the Rat Terrier background stems from the terriers or other dogs that were brought over by early English and other working class immigrants.
- [d2s4]  Since the breed was a farm, hunting and utility dog there was little to no planned breeding other than breeding dogs with agreeable traits to each other in order to produce the desired work ethic in the dog.
- [d2s5]  It is assumed that the Feist (dog), Bull Terrier, Smooth Fox Terrier, Manchester Terrier, Whippet, Italian Greyhound, the now extinct English White Terrier, Turnspit dog and or Wry Legged Terrier all share in the Teddy Roosevelt Terrier's ancestry.
- [d2s6]  These early Ratting Terriers were then most likely bred to the Beagle or Beagle cross bred dogs (for increased scenting ability) and other dogs.
- [d2s7]  Maximizing the influences from these various breeds provides the modern Teddy Roosevelt Terrier with a keen sense of awareness and prey drive, an acute sense of smell and a very high intellect.
- [d2s8]  Although they tend to be aloof with strangers they are devoted companion dogs with a strong desire to please and be near their owners side at all times.

**d3: Rare breed (dog)**

- [d3s0] Rare breed (dog) is any breed of dog that is small in number and is used to refer to both old established breeds such as the Stabyhoun and Glen of Imaal Terrier or newer creations.
- [d3s1]  Since dogs have greater genetic variability than other domesticated animals the number of possible breeds is vast with new crosses constantly occurring, from these both selected and random crosses may come new breeds should offspring reliably breed true to type.
- [d3s2]  New breeds from the wild such as the Carolina Dog are quite rare compared to attempts at breed creation from man as found in the American Hairless Terrier which sought to exploit a mutation.

**d4: Old Jock**

- [d4s0] Old Jock (1859–1871), was a Fox Terrier famous during the late 19th and early 20th centuries.
- [d4s1]  A mostly white dog, he ran briefly with a hunting kennel before becoming a show dog, most notably with a victory at the show which popularised the Fox Terrier.
- [d4s2]  His main show rivalry was with a dog named Tartar, and along with a dog named Trap, the three were popular sires of the Fox Terrier breed.
- [d4s3]  He was also involved in the early formation of the Jack Russell Terrier and the Dandie Dinmont Terrier breeds.

**d5: Scanian dialect**

- [d5s0] Scanian (   ) is a closely related group of South Swedish dialects spoken in the province of Scania in southern Sweden.
- [d5s1]  Scanian formed part of the old Scandinavian dialect continuum and are by most historical linguists considered to be an East Danish dialect group, but due to the modern-era influence from Standard Swedish in the region and because traditional dialectology in the Scandinavian countries normally has not considered isoglosses that cut across state borders, the Scanian dialects have normally been treated as a South Swedish dialect group in Swedish dialect research.
- [d5s2]  However, many of the early Scandinavian linguists, including Adolf Noreen and G. Sjöstedt, classified it as "South Scandinavian", and some linguists, such as Elias Wessén, also considered Old Scanian a separate language, classified apart from both Old Danish and Old Swedish.

**d6: American Hairless Terrier**

- [d6s0] The American Hairless Terrier is a rare breed of dog that was derived as a variant of Rat Terrier.
- [d6s1]  As of January 1, 2004, the United Kennel Club deemed the AHT a separate terrier breed, granting it full UKC recognition.
- [d6s2]  An intelligent, social and energetic working breed, the American Hairless Terrier is often listed as a potential good breed choice for allergy sufferers.

**d7: Malte**

- [d7s0] Malte is a male given name that is mainly used in Denmark, Sweden and Germany, which is from Old Danish "Malti".
- [d7s1]  It originated from "Helmhold / Helmwald" ("helmet-govern") or from former Low German and Old Danish short form of Old German names beginning with "Mahal-" "assembly".
- [d7s2]  It described the advisor of the Thing (assembly).

**d8: Old Danish Pointer**

- [d8s0] The Old Danish Pointer is a medium-sized breed of dog, white with brown markings, originally used as a pointing dog in Denmark.

**d9: Yorkshire Terrier**

- [d9s0] The Yorkshire Terrier is a small dog breed of terrier type, developed during the 19th century in Yorkshire, England, to catch rats in clothing mills.
- [d9s1]  The defining feature of the breed is its maximum size of 7 lb , although some may exceed this and grow up to 15 lb .
- [d9s2]  It is placed in the Toy Terrier section of the Terrier Group by the Fédération Cynologique Internationale and in the Toy Group or Companion Group by other kennel clubs, including the American Kennel Club.
- [d9s3]  A popular companion dog, the Yorkshire Terrier has also been part of the development of other breeds, such as the Australian Silky Terrier.
- [d9s4]  It has a grey, black, and tan coat, and the breed's nickname is "Yorkie".

**d10: Airedale Terrier**

- [d10s0] The Airedale Terrier (often shortened to "Airedale"), also called Bingley Terrier and Waterside Terrier, is a dog breed of the terrier type that originated in the valley ("dale") of the River Aire, in the West Riding of Yorkshire, England.
- [d10s1]  It is traditionally called the "King of Terriers" because it is the largest of the terrier breeds.
- [d10s2]  The Airedale was bred from the Old English Black and Tan Terrier (now extinct), the Bull Terrier, the Otterhound and probably some other Terrier breeds, originally to serve as an all around working farm dog.
- [d10s3]  In Britain this breed has also been used as a war dog, guide dog and police dog.
- [d10s4]  In the United States, this breed has been used to hunt big game, upland birds, and water fowl, and serve in many other working capacities.

## 13. hotpotqa_5a7565475542992d0ec05f84

原位置：`train` 第 133 题 · 全局第 133 题 · `sample_id: hotpotqa_5a7565475542992d0ec05f84`

Question: Which park, Picos de Europa National Park or Caldera de Taburiente National Park is on an island?

Note:

Type: comparison · fallback: False · SFT snapshots: 6

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | whether Picos de Europa National Park is on an island | False | () |
| u2 | whether Caldera de Taburiente National Park is on an island | False | () |
| u3 | which park is on an island | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Picos de Europa National Park is on an island | False | [] | no | [] |
| u2 | whether Caldera de Taburiente National Park is on an island | False | [] | yes | [['d4s0'], ['d6s0']] |
| u3 | which of Picos de Europa National Park and Caldera de Taburiente National Park is on an island | True | ['u1', 'u2'] | Caldera de Taburiente National Park | [[]] |

### Source documents (reference only)

**d1: Tobes**

- [d1s0] Tobes is one of eight parishes (administrative divisions) in Peñamellera Baja, a municipality within the province and autonomous community of Asturias, in northern Spain.
- [d1s1]  It is located in the Picos de Europa National Park.

**d2: Oceño**

- [d2s0] Oceño is one of eight parishes (administrative divisions) in Peñamellera Alta, a municipality within the province and autonomous community of Asturias, in northern Spain.
- [d2s1]  It is located in the Picos de Europa National Park.

**d3: Lake Ercina**

- [d3s0] Lake Ercina is a small highland lake in Asturias, Spain.
- [d3s1]  It is located in the Picos de Europa, in the Cantabrian Mountains.
- [d3s2]  Situated next to Lake Enol, together, they forms the group known as Lakes of Covadonga within the Picos de Europa National Park.
- [d3s3]  Lake Ercina is smaller than Lake Enol.
- [d3s4]  It is situated at an altitude of 1108 m and its maximum depth is just over 2 m .
- [d3s5]  The eutrophic lake, covers approximately eight hectares.
- [d3s6]  Its characteristics are tied to its glacier origin and geographic location.

**d4: Caldera de Taburiente National Park**

- [d4s0] Caldera de Taburiente National Park (Spanish: "Parque Nacional de la Caldera de Taburiente" ) is large geological feature on the island of La Palma, Canary Islands, Spain.
- [d4s1]  It contains the enormous expanse of the Caldera de Taburiente which dominates the northern part of the island, and was designated as a national park in 1954.
- [d4s2]  The telescopes of the Roque de los Muchachos Observatory are situated very close to the summit.

**d5: Picos de Europa National Park**

- [d5s0] The Picos de Europa National Park (Spanish: "Parque Nacional de Picos de Europa" ) is a National Park in the Picos de Europa mountain range, in northern Spain.
- [d5s1]  It is within the boundaries of three autonomous communities, Asturias, Cantabria and Castile and León, which are represented on the body which runs the park.

**d6: Idafe Rock**

- [d6s0] Idafe Rock is a natural stone pillar located in Caldera de Taburiente National Park on the island of La Palma in the Canary Islands.

**d7: Lake Enol**

- [d7s0] Lake Enol is a small highland lake in the Principality of Asturias, Spain.
- [d7s1]  It is located in the Picos de Europa Western Massif, Cantabrian Mountains.
- [d7s2]  It is next to Lake Ercina and together, they form the group known as Lakes of Covadonga, inside the Picos de Europa National Park.
- [d7s3]  Lake Enol is the larger of the two.
- [d7s4]  It is situated approximately 10 km from Covadonga and 25 km from Cangas de Onís.
- [d7s5]  A curving road is available from Arriondas to the lake.
- [d7s6]  Measuring 0.1 km2 , it is one of the biggest lakes in the area.
- [d7s7]  Lake Enol is situated 1070 m above sea level, in the Picos de Europa).
- [d7s8]  It was formed by the withdrawal of a front glacier.

**d8: Naranjo de Bulnes**

- [d8s0] The Naranjo de Bulnes (known as Picu Urriellu in Asturian) is a limestone peak dating from the paleozoic era, located in the Macizo Central region of the Picos de Europa, Asturias (Spain).
- [d8s1]  Its name "Picu Urriellu" is believed to be derived from the term "Los Urrieles" which is used to describe the Macizo Central.
- [d8s2]  Naranjo de Bulnes is part of the Cabrales region of Asturias, and lies within the Picos de Europa National Park.

**d9: Trescares**

- [d9s0] Trescares is one of eight parishes (administrative divisions) in Peñamellera Alta, a municipality within the province and autonomous community of Asturias, in northern Spain.
- [d9s1]  It is located in the Picos de Europa National Park.

**d10: Lakes of Covadonga**

- [d10s0] The Lakes of Covadonga (el.
- [d10s1]  1134 m.) are composed of two glacial lakes located on the region of Asturias, Spain.
- [d10s2]  These lakes, often also called Lakes of Enol or simply Los Lagos, are Lake Enol and Lake Ercina located in the Picos de Europa range and they are the original center of the Picos de Europa National Park, created in 1918.

## 14. hotpotqa_5a75d0325542992db94736d2

原位置：`train` 第 134 题 · 全局第 134 题 · `sample_id: hotpotqa_5a75d0325542992db94736d2`

Question: Who was the 1907 football team captain for the oldest Catholic university in the Commonwealth of Pennsylvania?

Note:

Type: bridge · fallback: False · SFT snapshots: 6

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | oldest Catholic university in the Commonwealth of Pennsylvania | False | () |
| u2 | 1907 football team captain of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | oldest Catholic university in the Commonwealth of Pennsylvania | False | [] | Villanova University | [['d10s1']] |
| u2 | 1907 football team captain for {u1} | True | ['u1'] | Joseph Slavin | [['d9s1']] |

### Source documents (reference only)

**d1: St. Mary's University School of Law**

- [d1s0] St. Mary's University School of Law is one of the professional graduate schools of St. Mary's University.
- [d1s1]  The law school is located in San Antonio, Texas, USA and is the oldest Catholic law school in the American Southwest.
- [d1s2]  The University is a private Catholic university.
- [d1s3]  The School of Law has an enrollment of about 860 students, pursuing either Juris Doctor (J.D.), Master of Laws (LL.M.)
- [d1s4] , or Master of Jurisprudence (M.Jur.)
- [d1s5] .
- [d1s6]  degrees.
- [d1s7]  St. Mary's is the first law school in Texas to offer the M.Jur., the graduate degree in the study of law for students not seeking to enter the practice of law.

**d2: Immaculate Conception Seminary School of Theology**

- [d2s0] The Immaculate Conception Seminary School of Theology (ICSST) is the major seminary for the Roman Catholic Archdiocese of Newark and is part of Seton Hall University, a Roman Catholic university in New Jersey, and is located in South Orange, within the Archdiocese of Newark.
- [d2s1]  ICSST is one of the oldest Catholic seminaries in the United States.
- [d2s2]  Seton Hall is the oldest diocesan university in the country.
- [d2s3]  ICSST admits both students to study as seminarians and lay persons as well.
- [d2s4]  In addition to a Seminary Formation Program to prepare men for priesthood, ICSST has a renowned graduate program offering the following degrees:

**d3: Wesley Englehorn**

- [d3s0] Wesley Theodore "Moose" Englehorn (January 21, 1890 – September 3, 1993) was an American football player and coach.
- [d3s1]  Born in Helena, Montana, Englehorn first gained fame as a football player for Spokane High School.
- [d3s2]  While he was a junior in high school, he was reportedly recruited by Princeton University to come east to play football for the school.
- [d3s3]  A newspaper account in 1907 reported: "It is expected that Wesley Englehorn, the giant left tackle of the high school team, will also enter the Eastern college.
- [d3s4]  If this materializes the Spokane high school will be weakened next year by the loss of two of its greatest players.
- [d3s5]  ... Englehorn is also a strong basket ball player and track athlete."
- [d3s6]  Englehorn did not enroll at Princeton and instead played for two years on the All Star Pacific Northwest football and basketball teams.
- [d3s7]  He began his collegiate career at Washington State College.
- [d3s8]  After playing one year of football at Washington State, Englehorn enrolled at Dartmouth College, where he played two years at the tackle position.
- [d3s9]  He was elected team captain for the 1913 season, but he was declared ineligible under "the so-called three-year rule" because of his year at Washington State.
- [d3s10]  Though ineligible to play, Englehorn served as the team's assistant coach in 1913 and was elected class president.
- [d3s11]  He was selected as a first-team All-American in 1912.
- [d3s12]  He graduated from Dartmouth in 1914 and worked as a football coach for several years thereafter.
- [d3s13]  From 1914 to 1916, he was the football coach at Case School of Applied Science in Cleveland, Ohio.
- [d3s14]  In 1917, he was hired as the line coach and first assistant football coach at Colgate University.
- [d3s15]  In 1920, he was an assistant coach under Frank Cavanaugh at Boston College.
- [d3s16]  In 1921, he was hired as the head football coach at Amherst College.
- [d3s17]  In January 1922, Englehorn announced his retirement from coaching.
- [d3s18]  Shortly before his death at age 103, Englehorn said, "It's the football I remember best ... the teammates .
- [d3s19] .
- [d3s20]  the teamwork."
- [d3s21]  Prior to his death in 1993, he was living at Stapeley Hall, a home for the elderly in the Germantown section of Philadelphia, Pennsylvania, and was the oldest living All-American football player.

**d4: Charles Keinath**

- [d4s0] Charles "Kid" Keinath (November 13, 1885 – April 1966) was an American college athlete who was a four-time All-American in basketball while at the University of Pennsylvania.
- [d4s1]  He also won national championships in both basketball (1907–08) and football (1908) at Penn.
- [d4s2]  In 1907–08, the basketball team finished 24–4 and was retroactively named the national champions by the Helms Athletic Foundation.
- [d4s3]  Then, in 1908, the football team finished 11–0–1 and was named co-national champions with Harvard and LSU with Keinath leading the team as quarterback.
- [d4s4]  He was team captain as a senior for the basketball team and led the Quakers to a 22-game winning streak that spanned between the 1907–08 and 1908–09 seasons.

**d5: Catholic University Cardinals football**

- [d5s0] The Catholic University Cardinals football team represents The Catholic University of America in National Collegiate Athletic Association (NCAA) Division III college football competition as a member of the New England Women's and Men's Athletic Conference.
- [d5s1]  The team played its first game in 1895 and was a major college team in the first half of the 20th century, into the 1940s.
- [d5s2]  The football program was put on hiatus during World War II, and then discontinued shortly afterwards.
- [d5s3]  In 1965, football returned to the university at the club level, and, in 1977, re-entered NCAA competition as part of Division III.
- [d5s4]  The Cardinals have participated in the Division III playoffs three times in the late 1990s and have secured two ODAC championships.
- [d5s5]  The head coach is Mike Gutelius.

**d6: 1907 Washington football team**

- [d6s0] The 1907 Washington football team was an American football team that represented the University of Washington during the 1907 college football season.
- [d6s1]  In its second season under coach Victor M. Place, the team compiled a 4–4–2 record and outscored its opponents by a combined total of 96 to 48.
- [d6s2]  Enoch Bagshaw was the team captain.

**d7: Fordham University Press**

- [d7s0] The Fordham University Press is a publishing house, a division of Fordham University, that publishes primarily in the humanities and the social sciences.
- [d7s1]  Fordham University Press was established in 1907 and is headquartered at the university's Lincoln Center campus.
- [d7s2]  It is the oldest Catholic university press in the United States, and the seventh-oldest in the nation.

**d8: 1907 Central Michigan Normalites football team**

- [d8s0] The 1907 Central Michigan Normalites football team represented Central Michigan Normal School, later renamed Central Michigan University, as an independent during the 1907 college football season.
- [d8s1]  Football was reinstated after one year's absence, and Ralph Thacker, who had played fullback for Olivet College the prior year, was named coach of the football team.
- [d8s2]  Bruce Stickles was selected as the team captain.
- [d8s3]  Although the Central Michigan football media guide reports that the 1907 football team compiled a 2–4 record, including a loss to Alma College, the contemporaneous newspaper report on the Alma game reports it as a victory for Central by a 13 to 0 score.
- [d8s4]  Accordingly, it appears that the correct record of the 1907 football team was 3–3.

**d9: 1907 Villanova Wildcats football team**

- [d9s0] The 1907 Villanova Wildcats football team represented Villanova University during the 1907 college football season.
- [d9s1]  The Wildcats team captain was Joseph Slavin.

**d10: Villanova University**

- [d10s0] Villanova University is a private research university located in Radnor Township, a suburb northwest of Philadelphia, Pennsylvania, within the Archdiocese of Philadelphia in the United States.
- [d10s1]  Named after Saint Thomas of Villanova, the school is the oldest Catholic university in the Commonwealth of Pennsylvania.

## 15. hotpotqa_5a75ebe6554299109176e5d2

原位置：`train` 第 135 题 · 全局第 135 题 · `sample_id: hotpotqa_5a75ebe6554299109176e5d2`

Question: Which Walt Disney movie came out first, Tarzan or Honey, I Shrunk the Kids

Note:

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | release year of Tarzan | False | () |
| u2 | release year of Honey, I Shrunk the Kids | False | () |
| u3 | which Walt Disney movie came out first | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | release year of the Walt Disney movie Tarzan | False | [] | 1999 | [['d5s0']] |
| u2 | release year of the Walt Disney movie Honey, I Shrunk the Kids | False | [] | 1989 | [['d8s0'], ['d2s1'], ['d3s1'], ['d4s0'], ['d6s0'], ['d9s0']] |
| u3 | which Walt Disney movie came out first, Tarzan or Honey, I Shrunk the Kids | True | ['u1', 'u2'] | Honey, I Shrunk the Kids | [[]] |

### Source documents (reference only)

**d1: Honey, We Shrunk Ourselves**

- [d1s0] Honey, We Shrunk Ourselves is a 1997 live-action direct-to-video sequel to "Honey, I Shrunk the Kids" and "Honey, I Blew Up the Kid".
- [d1s1]  It is the third and final installment in the "Honey, I Shrunk the Kids" trilogy.
- [d1s2]  The directorial debut of cinematographer Dean Cundey and released through Walt Disney Home Video, it tells the story of inventor Wayne Szalinski as he accidentally shrinks his wife, brother, sister-in-law, and himself with his electromagnetic shrink ray.

**d2: Honey, I Shrunk the Kids: Movie Set Adventure**

- [d2s0] Honey, I Shrunk the Kids: Movie Set Adventure was a playground at Disney's Hollywood Studios in Orlando, Florida.
- [d2s1]  It was located in the Streets of America area and was based on Disney's 1989 film, "Honey, I Shrunk the Kids".
- [d2s2]  The playground, which opened almost a year after the film, featured 30 ft blades of grass, and was themed as a movie set for the giant backyard scenes from the film.
- [d2s3]  It was closed in April 2016 to make room for the construction of on the same site.

**d3: Robert Oliveri**

- [d3s0] Robert Dane Oliveri (born April 28, 1978) is a former American actor.
- [d3s1]  He is best known for his portrayal of Nick Szalinski in the 1989 Disney film, "Honey, I Shrunk the Kids", for which he was nominated for a Young Artist Award and a Saturn Award.
- [d3s2]  He reprised the role in the 1992 sequel, "Honey, I Blew Up the Kid" and the 3D film, "Honey, I Shrunk the Audience".
- [d3s3]  He is also known as Kevin, Winona Ryder's little brother, in Tim Burton's "Edward Scissorhands".

**d4: Marcia Strassman**

- [d4s0] Marcia Ann Strassman (April 28, 1948 – October 24, 2014) was an American actress and singer, best known for her roles as Nurse Margie Cutler on "M*A*S*H", as Julie Kotter on "Welcome Back, Kotter" and as Diane Szalinski in the feature film "Honey, I Shrunk the Kids" (1989); its sequel "Honey, I Blew Up the Kid" (1992); and the 3-D film spin-off "Honey, I Shrunk the Audience!
- [d4s1] " (1994), which was shown at several Disney theme parks through mid-2010.

**d5: Tarzan (1999 film)**

- [d5s0] Tarzan is a 1999 American animated drama adventure film produced by Walt Disney Feature Animation for Walt Disney Pictures.
- [d5s1]  The 37th Disney animated feature film and the last film produced during the Disney Renaissance era, it is based on the story "Tarzan of the Apes" by Edgar Rice Burroughs, and is the first animated major motion picture version of the "Tarzan" story.
- [d5s2]  Directed by Chris Buck and Kevin Lima with a screenplay by Tab Murphy, Bob Tzudiker, and Noni White, "Tarzan" features the voices of Tony Goldwyn, Minnie Driver, Glenn Close, and Rosie O'Donnell with Brian Blessed, Lance Henriksen, Wayne Knight, and Nigel Hawthorne.

**d6: Honey, I Shrunk the Kids: The TV Show**

- [d6s0] Honey, I Shrunk the Kids: The TV Show (truncated to Honey, I Shrunk the Kids in the show's title sequence) is an American syndicated comic science fiction sitcom based on the 1989 film, "Honey, I Shrunk the Kids".
- [d6s1]  It expands upon the original film's concept of a shrinking experiment gone wrong to include a myriad of experiments gone awry.
- [d6s2]  It debuted in syndication on September 1, 1997 and ran for three consecutive seasons, concluding with the 66th episode on May 20, 2000.

**d7: Cinderella (sports)**

- [d7s0] In sports, the terms Cinderella, "Cinderella story", and Cinderella team are used to refer to situations in which competitors achieve far greater success than would reasonably have been expected.
- [d7s1]  Cinderella stories tend to gain much media and fan attention as they move closer to the championship game at the end of the tournament.
- [d7s2]  The term comes from "Cinderella", a well-known European folk tale embodying a myth-element of unjust oppression/triumphant reward.
- [d7s3]  The title character is a woman living in unfortunate circumstances that are suddenly changed to remarkable fortune.
- [d7s4]  In a sporting context the term has been used at least since 1939, but came into widespread usage in 1950, when the Disney movie came out that year, and in reference to City College of New York, the unexpected winners of the NCAA Men's Basketball championship also that year.
- [d7s5]  The term was used by Bill Murray in the 1980 hit movie "Caddyshack" where he pretends as the announcer to his own golf fantasy: "Cinderella story.
- [d7s6]  Outta nowhere.
- [d7s7]  A former greenskeeper, now, about to become the Masters champion."

**d8: Honey, I Shrunk the Kids**

- [d8s0] Honey, I Shrunk the Kids is a 1989 American comic science fiction film.
- [d8s1]  The directorial debut of Joe Johnston and produced by Walt Disney Pictures, it tells the story of an inventor who accidentally shrinks his and his neighbor's kids to a quarter of an inch with his electromagnetic shrinking machine and throws them out into the backyard with the trash, where they must venture into their backyard to return home while fending off insects and other obstacles.

**d9: Honey, I Blew Up the Kid**

- [d9s0] Honey, I Blew Up the Kid is a 1992 American comedy science fiction film and the sequel to the 1989 film "Honey, I Shrunk the Kids".
- [d9s1]  Directed by Randal Kleiser and released by Walt Disney Pictures, the film stars Rick Moranis, Marcia Strassman, Robert Oliveri and Amy O'Neill, who reprise their roles as Wayne, Diane, Nick, and Amy Szalinski respectively, as well as newcomer Keri Russell as Mandy Park, Nick's love interest and babysitter of Adam, the Szalinskis' new two-year-old son, whose accidental exposure to Wayne's new industrial-sized growth machine causes him to gradually grow to enormous size.
- [d9s2]  Made only three years after "Honey, I Shrunk the Kids", this film is set five years after the events depicted in the previous film.
- [d9s3]  It was filmed in 1991.

**d10: Walt Disney Treasures: Wave Nine**

- [d10s0] The ninth wave of the "Walt Disney Treasures" series of DVDs was released on November 3, 2009.
- [d10s1]  This wave comprises two releases, each containing one season of the 1957–1959 "Zorro" TV series.
- [d10s2]  Note that these episodes were previously released exclusively through the Disney Movie Club, but those releases were colorized whereas these releases are the original black-and-white format.
- [d10s3]  Each release also includes two of the four hour-long "Zorro" episodes originally aired on "Walt Disney Presents" in 1960 and 1961.
- [d10s4]  This wave is the first wave to not include any animated sets, and the last wave that has been released to date.
- [d10s5]  Despite being the last wave, this was the only wave to feature standard size DVD cases, while the tin size remained the same.
- [d10s6]  For the first time also, the tins were colored black, and was the second time featuring another colored tin since "".
- [d10s7]  This wave also brought back the side straps, now colored yellow instead of blue.
- [d10s8]  This was also the first wave where no original animated set came out.
- [d10s9]  It was speculated on Disney fan forums that animated set would contain animated left overs from Disney era, including animated shorts not released on previous sets, including the Chip'n'Dale solo cartoons, and Educational shorts form mid-1960s, as well as the animated episodes from the anthology series some of them hosted by Ludwig Von Drake.

## 16. hotpotqa_5a77287a55429972597f1452

原位置：`train` 第 136 题 · 全局第 136 题 · `sample_id: hotpotqa_5a77287a55429972597f1452`

Question: Who is older, Speedy Keen or Shaun Ryder?

Note:

Type: comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | birth date of Speedy Keen | False | () |
| u2 | birth date of Shaun Ryder | False | () |
| u3 | who is older | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | birth date of Speedy Keen | False | [] | 29 March 1945 | [['d7s0']] |
| u2 | birth date of Shaun Ryder | False | [] | 23 August 1962 | [['d3s0']] |
| u3 | who is older, Speedy Keen or Shaun Ryder | True | ['u1', 'u2'] | Speedy Keen | [[]] |

### Source documents (reference only)

**d1: Kav Sandhu**

- [d1s0] KAV (Kav Sandhu) is a British musician from Leicester UK, based in Los Angeles.
- [d1s1]  KAV played guitar with British band Happy Mondays for 4 years after helping reform the band with frontman Shaun Ryder in 2004.
- [d1s2]  He launched his solo project under moniker "KAV" in 2008 with long-time friend and drummer Jim (James) Portas.
- [d1s3]  His solo material has been compared by the media to everyone from Iggy & The Stooges, Black Rebel Motorcycle Club, Primal Scream, Kasabian, The Rolling Stones & Bob Dylan.
- [d1s4]  He plays live with a full live band, which sometimes features guest musicians from various bands.

**d2: Keen's myotis**

- [d2s0] Keen's myotis ("Myotis keenii") is a species of vesper bat.
- [d2s1]  It is found in British Columbia in Canada and in Washington and Alaska in the United States.
- [d2s2]  It is named after the Rev. John Henry Keen, who collected the specimen that formed the basis for the first scientific description of the species.
- [d2s3]  Classification for Keen's myotis formerly included the Northern long-eared Myotis ("Myotis septentrionalis"), resulting in older studies confusing the species for one another.

**d3: Shaun Ryder**

- [d3s0] Shaun William George Ryder (born 23 August 1962) is an English musician and singer-songwriter.
- [d3s1]  He is best known as the lead singer of the Happy Mondays and Black Grape.
- [d3s2]  He was the runner-up of the tenth series of "I'm a Celebrity...Get Me Out of Here!
- [d3s3] ".

**d4: Amateur Night in the Big Top**

- [d4s0] Amateur Night in the Big Top is the first official solo album by Shaun Ryder, of Happy Mondays and Black Grape.
- [d4s1]  The album is subtitled "Clowns and Pet Sounds".
- [d4s2]  It was released in September, 2003 and co-produced by Pete Carroll, Shane Norton and Cabaret Voltaire's Stephen Mallinder.
- [d4s3]  It was recorded in Perth, Australia and released on the Offworld Sounds record label run by Ryder's cousin Pete Carroll and Mallinder.

**d5: All the Aces**

- [d5s0] All The Aces is a compilation album by the band Motörhead, released in 1993.
- [d5s1]  It includes 14 of their most popular songs, 2 enhanced multimedia sections and 8 previously unreleased live songs by The Muggers (a band formed by "Fast" Eddie Clarke and Phil "Philthy Animal" Taylor of Motörhead with John "Speedy" Keen and Billy Rath).

**d6: Dare (song)**

- [d6s0] "Dare" (styled as "挑戦 (DARE)") is a song by British virtual band Gorillaz, taken as the second single from their second studio album, "Demon Days".
- [d6s1]  The track is sung by Rosie Wilson (also known as Roses Gabor) with backing vocals from Damon Albarn and features vocals by Happy Mondays frontman Shaun Ryder.
- [d6s2]  It peaked at No. 1 in the UK Singles Chart in September 2005, becoming the band's only UK No. 1.
- [d6s3]  In 2016, vocals of the song were interpolated in Friction's song "Dare (Hold It Down)".
- [d6s4]  In 2017 the song was featured in an episode of the British soap-opera ￼￼EastEnders.

**d7: Speedy Keen**

- [d7s0] John David Percy "Speedy" Keen (29 March 1945 – 12 March 2002), was a songwriter, vocalist, drummer and keyboard player, best known for his association with the rock band Thunderclap Newman.
- [d7s1]  He wrote "Something in the Air" (1969) for the band, which reached No. 1 in the UK Singles Chart and released two solo albums.

**d8: Demon Days**

- [d8s0] Demon Days is the second studio album by British virtual band Gorillaz, released on 11 May 2005 in Japan and on 23 May internationally by Parlophone Records and in the United States by Virgin Records.
- [d8s1]  The album features contributions from De La Soul, Neneh Cherry, Martina Topley-Bird, Roots Manuva, MF DOOM, Ike Turner, Bootie Brown of the Pharcyde, Shaun Ryder, Dennis Hopper, the London Community Gospel Choir, and a children's choir.
- [d8s2]  Frontman Damon Albarn brought in Danger Mouse as producer.

**d9: Happy Mondays**

- [d9s0] Happy Mondays are an English alternative rock band from Salford, Greater Manchester.
- [d9s1]  Formed in 1980, the band's original line-up was Shaun Ryder (vocals), his brother Paul Ryder (bass), Mark Day (guitar), Paul Davis (keyboard), and Gary Whelan (drums).
- [d9s2]  Mark "Bez" Berry later joined the band onstage as a dancer/percussionist.
- [d9s3]  Rowetta joined the band as a guest vocalist in 1990.

**d10: Something in the Air**

- [d10s0] "Something in the Air" is a song recorded by Thunderclap Newman, written by Speedy Keen who also sang the song.
- [d10s1]  It was a number 1 single for three weeks in the UK Singles Chart in July 1969.
- [d10s2]  The song has been used for films, television and adverts, and has been covered by several artists.
- [d10s3]  The track was also included on Thunderclap Newman's only album release "Hollywood Dream" over a year later.

## 17. hotpotqa_5a7769ea55429966f1a36d2f 【需改：生成拆解】

原位置：`train` 第 137 题 · 全局第 137 题 · `sample_id: hotpotqa_5a7769ea55429966f1a36d2f`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5a7769ea55429966f1a36d2f"></a>

> **审阅结论：需改：生成拆解**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 单元本身是两个已点名对象的事实加一个比较/共同属性结论，没有寻找未知中间实体的桥接步骤，但 question_type 被写成 bridge_comparison。
>
> **处理建议：** 只将 question_type 改为 comparison，保留当前单元关系；这属于题型元数据错误，不应为凑题型增加桥接单元。
>
> **证据定位：** d7s0, d8s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Who died first, Yuri Linnik or Georg Cantor?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | death date of Yuri Linnik | False | () |
| u2 | death date of Georg Cantor | False | () |
| u3 | who died first | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | death date of Yuri Linnik | False | [] | June 30, 1972 | [['d7s0']] |
| u2 | death date of Georg Cantor | False | [] | January 6, 1918 | [['d8s0']] |
| u3 | who died first, Yuri Linnik or Georg Cantor | True | ['u1', 'u2'] | Georg Cantor | [[]] |

### Source documents (reference only)

**d1: Cantor space**

- [d1s0] In mathematics, a Cantor space, named for Georg Cantor, is a topological abstraction of the classical Cantor set: a topological space is a Cantor space if it is homeomorphic to the Cantor set.
- [d1s1]  In set theory, the topological space 2 is called "the" Cantor space.
- [d1s2]  Note that, commonly, 2 is referred to simply as the Cantor set, while the term Cantor space is reserved for the more general construction of "D" for a finite set "D" and a set "S" which might be finite, countable or possibly uncountable.

**d2: Georg Cantor's first set theory article**

- [d2s0] Georg Cantor's first set theory article was published in 1874 and contains the first theorems of transfinite set theory, which studies infinite sets and their properties.
- [d2s1]  One of these theorems is "Cantor's revolutionary discovery" that the set of all real numbers is uncountably, rather than countably, infinite.
- [d2s2]  This theorem is proved using Cantor's first uncountability proof, which differs from the more familiar proof using his diagonal argument.
- [d2s3]  The title of the article, "On a Property of the Collection of All Real Algebraic Numbers" ("Ueber eine Eigenschaft des Inbegriffes aller reellen algebraischen Zahlen "), refers to its first theorem: the set of real algebraic numbers is countable.

**d3: Tav (number)**

- [d3s0] In his work on set theory, Georg Cantor denoted the collection of all cardinal numbers by the last letter of the Hebrew alphabet, ת (transliterated as Taf, Tav, or Taw.)
- [d3s1]  As Cantor realized, this collection could not itself have a cardinality, as this would lead to a paradox of the Burali-Forti type.
- [d3s2]  Cantor instead said that it was an "inconsistent" collection which was absolutely infinite.

**d4: Cantor–Bernstein theorem**

- [d4s0] In set theory and order theory, the Cantor–Bernstein theorem states that the cardinality of the second type class, the class of countable order types, equals the cardinality of the continuum.
- [d4s1]  It was used by Felix Hausdorff and named by him after Georg Cantor and Felix Bernstein.
- [d4s2]  Cantor constructed a family of countable order types with the cardinality of the continuum, and in his 1901 inaugural dissertation Bernstein proved that such a family can have no higher cardinality.

**d5: Jónsson–Tarski algebra**

- [d5s0] In mathematics, a Jónsson–Tarski algebra or Cantor algebra is an algebraic structure encoding a bijection from an infinite set "X" onto the product "X"×"X".
- [d5s1]  They were introduced by .
- [d5s2]  , named them after Georg Cantor because of Cantor's pairing function and Cantor's theorem that an infinite set "X" has the same number of elements as "X"×"X"; the term "Cantor algebra" is also occasionally used to mean the Boolean algebra of all clopen subsets of the Cantor set, or the Boolean algebra of Borel subsets of the reals modulo meager sets (sometimes called the Cohen algebra).

**d6: Limitation of size**

- [d6s0] In the philosophy of mathematics, specifically the philosophical foundations of set theory, limitation of size is a concept developed by Philip Jourdain and/or Georg Cantor to avoid Cantor's paradox.
- [d6s1]  It identifies certain "inconsistent multiplicities", in Cantor's terminology, that cannot be sets because they are "too large".
- [d6s2]  In modern terminology these are called proper classes.

**d7: Yuri Linnik**

- [d7s0] Yuri Vladimirovich Linnik (Russian: Ю́рий Влади́мирович Ли́нник ; January 8, 1915 – June 30, 1972) was a Soviet mathematician active in number theory, probability theory and mathematical statistics.

**d8: Georg Cantor**

- [d8s0] Georg Ferdinand Ludwig Philipp Cantor ( ; ] ; March 3 [O.S. February 19] 1845  – January 6, 1918) was a German mathematician.
- [d8s1]  He invented set theory, which has become a fundamental theory in mathematics.
- [d8s2]  Cantor established the importance of one-to-one correspondence between the members of two sets, defined infinite and well-ordered sets, and proved that the real numbers are more numerous than the natural numbers.
- [d8s3]  In fact, Cantor's method of proof of this theorem implies the existence of an "infinity of infinities".
- [d8s4]  He defined the cardinal and ordinal numbers and their arithmetic.
- [d8s5]  Cantor's work is of great philosophical interest, a fact of which he was well aware.

**d9: Schröder–Bernstein theorem**

- [d9s0] In set theory, the Schröder–Bernstein theorem (named after Felix Bernstein and Ernst Schröder, also known as Cantor–Bernstein theorem, or Cantor–Schröder–Bernstein after Georg Cantor who first published it without proof) states that, if there exist injective functions "f" : "A" → "B" and "g" : "B" → "A" between the sets "A" and "B" , then there exists a bijective function "h" : "A" → "B" .
- [d9s1]  In terms of the cardinality of the two sets, this means that if |"A"| ≤ |"B"| and |"B"| ≤ |"A"| , then |"A"| = |"B"| ; that is, "A" and "B" are equipollent.
- [d9s2]  This is a useful feature in the ordering of cardinal numbers.

**d10: Smith–Volterra–Cantor set**

- [d10s0] In mathematics, the Smith–Volterra–Cantor set (SVC), fat Cantor set, or ε-Cantor set is an example of a set of points on the real line ℝ that is nowhere dense (in particular it contains no intervals), yet has positive measure.
- [d10s1]  The Smith–Volterra–Cantor set is named after the mathematicians Henry Smith, Vito Volterra and Georg Cantor.
- [d10s2]  The Smith-Volterra-Cantor set is topologically equivalent to the middle-thirds Cantor set.

## 18. hotpotqa_5a78aee6554299148911f91f

原位置：`train` 第 138 题 · 全局第 138 题 · `sample_id: hotpotqa_5a78aee6554299148911f91f`

Question: What is the full name of the Portuguese footballer who kicked the winning goal in the 2004 Coupe de France Final?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | Portuguese footballer who kicked the winning goal in the 2004 Coupe de France Final | False | () |
| u2 | full name of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | Portuguese footballer who scored the winning goal in the 2004 Coupe de France Final | False | [] | Pauleta | [['d10s0']] |
| u2 | full name of {u1} | True | ['u1'] | Pedro Miguel Carreiro Resendes | [['d7s0']] |

### Source documents (reference only)

**d1: 2013 Coupe de France Final**

- [d1s0] The 2013 Coupe de France Final was the 95th final of France's most prestigious football cup competition.
- [d1s1]  The final took place on 31 May 2013 at the Stade de France in Saint-Denis and was contested between Bordeaux and Evian.
- [d1s2]  The winner of the Coupe de France was guaranteed a place in the group stage of the UEFA Europa League with the club's appearance being dependent on whether it qualifies for the 2013–14 UEFA Champions League.
- [d1s3]  The final was broadcast live on France 2.

**d2: 2012 Coupe de France Final**

- [d2s0] The 2012 Coupe de France Final was the 94th final of France's most prestigious football cup competition.
- [d2s1]  The final took place on 28 April 2012 at the Stade de France in Saint-Denis and was contested between Lyon and Quevilly.
- [d2s2]  The winner of the Coupe de France is guaranteed a place in the group stage of the UEFA Europa League with the club's appearance being dependent on whether it qualifies for the 2012–13 UEFA Champions League.
- [d2s3]  The final was broadcast live on France 2.

**d3: 2015 Coupe de France Final**

- [d3s0] The 2015 Coupe de France Final decided the winner of the 2014–15 Coupe de France, the 98th season of France's premier football cup.
- [d3s1]  It was played on 30 May at the Stade de France in Saint-Denis, Paris, between Ligue 2 club Auxerre and Paris Saint-Germain of Ligue 1.
- [d3s2]  Paris Saint-Germain won the match 1–0 with a goal by Edinson Cavani, thus achieving their ninth title.

**d4: 2012 Coupe de la Ligue Final**

- [d4s0] The 2012 Coupe de la Ligue Final was the 18th final of France's football league cup competition, the Coupe de la Ligue, a football competition for the 42 teams that the Ligue de Football Professionnel (LFP) manages.
- [d4s1]  The final took place on 14 April 2012 at the Stade de France in Saint-Denis and was contested between Lyon and Marseille.
- [d4s2]  The latter club entered the match as the two-time defending champions of the competition and sought to become the first club in French football history to win the competition three consecutive years after previously becoming the first club to win the competition in back-to-back seasons.
- [d4s3]  Lyon made its first finals appearance since the 2008 Coupe de France Final and played at the Stade de France for the first time in nearly three years.
- [d4s4]  The final was broadcast live on public network broadcaster France Télévisions.

**d5: 2011 Coupe de France Final**

- [d5s0] The 2011 Coupe de France Final was the 93rd final of France's most prestigious football cup competition.
- [d5s1]  The final took place on 14 May 2011 at the Stade de France in Saint-Denis and was contested between Paris Saint-Germain and Lille.
- [d5s2]  Paris Saint-Germain were the defending champions of the competition and it was the third time in the club's history that it had appeared in back-to-back finals.
- [d5s3]  The winner of the Coupe de France is guaranteed a place in the playoff round of the UEFA Europa League with the club's appearance being dependent on whether it qualifies for the 2011–12 UEFA Champions League.
- [d5s4]  The final was broadcast live on France 2.

**d6: 2007–08 Coupe de France**

- [d6s0] The 2007–2008 Coupe de France was the 91st edition of the prestigious tournament and is open to all clubs in French football, as well as the 4 overseas departments if they qualify.
- [d6s1]  The defending champions were FC Sochaux-Montbéliard who defeated Olympique Marseille 5-4 on penalties to claim their 2nd Coupe de France trophy.
- [d6s2]  The final was held on May 24, 2008 at the Stade de France.
- [d6s3]  The 2008 Coupe de France champions are Olympique Lyonnais, who defeated Paris Saint-Germain 1-0 to claim their 4th Coupe de France trophy.

**d7: Pauleta**

- [d7s0] Pedro Miguel Carreiro Resendes, (born 28 April 1973), known as Pauleta (] ), is a retired Portuguese footballer who played as a striker.

**d8: 2008 Coupe de France Final**

- [d8s0] The 2008 Coupe de France Final was a football match that was held at the Stade de France in Saint-Denis, France on 24 May 2008.
- [d8s1]  It was the 90th final in the Coupe de France's history.
- [d8s2]  The final was contested between Paris Saint-Germain FC and Olympique Lyonnais.
- [d8s3]  This was PSG's 10th appearance in the Coupe de France final, having won the cup in 1982, 1983, 1993, 1995, 1998, 2004, and 2006.
- [d8s4]  They also lost in the final twice in 1985 and 2003.
- [d8s5]  With a win in this year's final, PSG would have been granted the rare cup double with their last double coming in 1998.
- [d8s6]  This was Olympique Lyonnais's 7th appearance in the final having won in 1964, 1967, and 1973.
- [d8s7]  They lost in the final three times in 1963, 1971, and 1976.

**d9: 2009 Coupe de France Final**

- [d9s0] The 2009 Coupe de France Final was the 91st final of France's most prestigious cup competition, the Coupe de France.
- [d9s1]  The final was played at the Stade de France in the Paris suburb of Saint-Denis on 9 May 2009 and was contested between Rennes of Ligue 1 and Guingamp of Ligue 2.
- [d9s2]  Guingamp earned its first Coupe de France trophy after defeating Rennes 2–1 through two second-half goals from Eduardo.

**d10: 2004 Coupe de France Final**

- [d10s0] The Coupe de France Final 2004 was a football match held at Stade de France, Saint-Denis on 29 May 2004, that saw Paris SG defeat LB Châteauroux 1-0 thanks to a goal by Pauleta.

## 19. hotpotqa_5a78fb5955429970f5fffe09 【需改：生成拆解】

原位置：`train` 第 139 题 · 全局第 139 题 · `sample_id: hotpotqa_5a78fb5955429970f5fffe09`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5a78fb5955429970f5fffe09"></a>

> **审阅结论：需改：生成拆解**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 必要单元变成了“节日所纪念且卒于1609年的哲学家”，会输出人物；原题要求节日名称。
>
> **处理建议：** 恢复“卒于1609年的哲学家”非必要单元，再以“卡纳塔克邦纪念{u1}的节日”为 necessary 单元；对应 d10s0 与 d9s1。
>
> **证据定位：** d10s0, d9s1；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: What festival celebrated by the people of Karnataka celebrates a philosopher who died in 1609?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | festival celebrated by the people of Karnataka | False | () |
| u2 | philosopher celebrated by {u1} who died in 1609 | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | philosopher who died in 1609 | False | [] | Kanaka Dasa | [['d10s0']] |
| u2 | festival celebrated by the people of Karnataka that celebrates {u1} | True | ['u1'] | Kanakadasa Jayanthi | [['d9s1']] |

### Source documents (reference only)

**d1: Chewidden Thursday**

- [d1s0] Chewidden Thursday (also known as White Thursday, Chewidden Day or Jew-whidn) was a festival celebrated by the tin miners of West Cornwall on the last clear Thursday before (i.e. at least one week before) Christmas.
- [d1s1]  The festival celebrated the discovery of 'white tin' or smelted tin by St Chiwidden, a little-known Cornish saint who in legend was an associate of St Piran.

**d2: Asogli Yam Festival**

- [d2s0] Asogli Yam Festival is an annual festival celebrated by the people of Asogli in the Volta Region of Ghana.
- [d2s1]  It is celebrated in the month of September every year to celebrate the cultivation of yam that was started by a hunter who found the tuber in the forest during his hunting expedition.
- [d2s2]  According to history, the cultivation of yam among the people of Asogli started when the yam that the hunter hid during his hunting expedition to come for it later germinated and grew bigger.
- [d2s3]  The celebration was brought into Ghana by the Ewe people of Ghana when they migrated from Notse in the Republic of Togo; where it is still celebrated.

**d3: Tirumala Shanivaralu**

- [d3s0] Purattasi Sani or Tirumala Shanivara (Telugu: తిరుమల శనివారాలు , Tamil: புரட்டாசி சனி ) is a Hindu festival celebrated in some parts of South India including Andhra Pradesh, Karnataka, Tamil Nadu and Kerala.
- [d3s1]  The Hindu deity, Venkateswara, is worshiped during this festival.
- [d3s2]  It is celebrated during the Tamil month of Purattasi, generally which falls in the months of September and October of Gregorian calendar.
- [d3s3]  Puratasi Masam is of great importance as it is believed that Lord Venkateswara appeared on the earth in this month.
- [d3s4]  Lord Vishnu devotees consider this as the ideal month for thanking Lord Vishnu for preserving the Universe at the end of Kali Yuga.
- [d3s5]  All the Saturdays of this month are treated as holy days and Devotees gather in large number at Lord Vishnu temples and special prayers are offered.
- [d3s6]  Particularly the Odd Saturdays 1st, 3rd, 5th are of more importance.
- [d3s7]  Tirumala Annual Navarathri Brahmotsavam were also observed during this month where Tirumala will be flooded with lakhs of devotees.
- [d3s8]  Some people will take only vegetarian food during this month.

**d4: Gologo festival**

- [d4s0] The Gologo Festival is among the major festivals in Ghana and is celebrated by the chiefs and peoples of Talensi, Tong-Zuf, in the Upper East Region of the country, serving "to reinforce the community belief in the Nnoo shrine or Golib god", which deity regulates Talensi agricultural life.
- [d4s1]  It is a pre-harvest festival celebrated in the months of March and April, with sacrifices offered to seek protection and ensure plentiful rain and a good harvest in the coming season from the earthly gods.
- [d4s2]  The festival has a three-day programme at three different villages.
- [d4s3]  The first part takes place at Gorogo, the second at Yinduri, and the final and biggest at Teng-Zug (Tong-Zuf).
- [d4s4]  Libation is poured at the Teng-Zug shrine to thank the gods for a successful occasion.
- [d4s5]  The one in March is called Gol-diema, which means tutorial.
- [d4s6]  The main Gologo festival is celebrated in the second week in April.
- [d4s7]  Traditional songs are composed by the elders of each community for the occasion and people dance to the composed songs.
- [d4s8]  During this period, noise-making is prohibited and no one mourns their dead.
- [d4s9]  There is a special dress code whereby men wear a short knicker and a towel on the chest.
- [d4s10]  Women are also expected to tie a long towel from their chest down to the feet and cover their heads with a special local-made cloth.

**d5: Gangamma Jatara**

- [d5s0] Gangamma Jatara or Jathra is a folk festival celebrated in several places across Southern India; including Karnataka, Rayalaseema and Andhra regions in Andhra Pradesh.
- [d5s1]  It is celebrated for eight days.

**d6: Bheemana Amavasya**

- [d6s0] Bheemana Amavasya is a festival celebrated in South India, most in parts of Karnataka, Andhra Pradesh and Tamil Nadu.
- [d6s1]  It is celebrated on the new moon day ("amavasya") of the "ashadha" month of the Hindu calendar.

**d7: Fetu Afahye**

- [d7s0] The Fetu Afahye is a festival celebrated by the chiefs and peoples of Cape Coast in the Central region of Ghana.
- [d7s1]  The festival is celebrated on the first Saturday in the month of September every year.
- [d7s2]  The Fetu Afahye is celebrated annually by the Oguaa people of Cape Coast because in the past there was an outbreak of disease among the people that killed many.
- [d7s3]  The people prayed to the gods to help them to get rid of the disease.
- [d7s4]  Thus the festival is celebrated to keep the town clean and to prevent another epidemic befalling the people.

**d8: Nandotsava**

- [d8s0] Nandotsav is a festival celebrated the day after the festival Janmashtami, which celebrates the Lord Krishna's birth.

**d9: Kanakadasa Jayanthi**

- [d9s0] Kanakadasa Jayanthi is a festival cerebrated by people of Karnataka in general and Kuruba Gowda community in particular.
- [d9s1]  It is celebrated every year on the birth anniversary of the great poet and saint shri Kanaka Dasa.
- [d9s2]  In tribute to the great saint, the Government of Karnataka has declared the birthday of Kanaka Dasa as a state holiday.
- [d9s3]  All the government offices, schools and colleges around the state celebrate the birth anniversary of Shri Kanaka Dasa as a tribute to one of the great social reformers of Karnataka.
- [d9s4]  The 521 anniversary celebrated in 2015.

**d10: Kanaka Dasa**

- [d10s0] Kanaka Dasa (Kannada: ಕನಕದಾಸ ) (1509 – 1609) was a poet, philosopher, musician and composer from modern Karnataka.
- [d10s1]  He is known for his Kirtanes and Ugabhoga, compositions in the Kannada language for Carnatic music.
- [d10s2]  Like other Haridasas, he used simple Kannada language and native metrical forms for his compositions.

## 20. hotpotqa_5a79188455429974737f7984

原位置：`train` 第 140 题 · 全局第 140 题 · `sample_id: hotpotqa_5a79188455429974737f7984`

Question: What is the birthday of the composer of the song "Cups" that wasn't Luisa Gerstein?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | composer of the song "Cups" that wasn't Luisa Gerstein | False | () |
| u2 | birthday of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | composer of the song "Cups" other than Luisa Gerstein | False | [] | A. P. Carter | [['d2s2']] |
| u2 | birth date of {u1} | True | ['u1'] | December 15, 1891 | [['d6s0']] |

### Source documents (reference only)

**d1: María Luisa Escobar**

- [d1s0] María Luisa González Gragirena de Escobar (née María Luisa González Gragirena; known artistically by her married name María Luisa Escobar; also credited as Maritza Graxirena; Valencia, 5 December 1903 - Caracas, 14 May 1985) was a Venezuelan musicologist, pianist, composer, and caricaturist, who founded the Caracas Athenaeum in 1931.
- [d1s1]  She also served as President of the Venezuelan Red Cross (Valencia, 1921; Caracas, 1922–23).

**d2: Cups (song)**

- [d2s0] "Cups" is a version of the 1931 Carter Family song "When I'm Gone", usually performed a cappella with a cup used to provide percussion, as in the cup game.
- [d2s1]  It was first performed this way in a YouTube video by Lulu and The Lampshades in 2009 (under the title "You're Gonna Miss Me").
- [d2s2]  Composition of the song is credited to A. P. Carter and Luisa Gerstein of Lulu and the Lampshades.

**d3: Happy Birthday (Birthday Party song)**

- [d3s0] "Happy Birthday" is a 1980 song and by The Boys Next Door.
- [d3s1]  It was released as a single on 16 February 1980 on Missing Link.
- [d3s2]  The song is not related to the popular birthday song "Happy Birthday to You".
- [d3s3]  The first album it appeared on was "The Birthday Party".
- [d3s4]  It was later included as track two on the 1992 compilation "Hits".

**d4: Iisalmen serkku ja muita kertomuksia**

- [d4s0] Iisalmen serkku ja muita kertomuksia (Finnish: "The Cousin from Iisalmi and Other Tales") is a collection of historical short novels Finnish author Kaari Utrio.
- [d4s1]  This book includes novels Iisalmen serkku, Luisa, Agneta rakastuu, Rakas Thea, Ihana köyhyys, Ruusukupit and Rautalilja (Finnish: "Cousin from Iisalmi", "Luisa", "Agneta Falls in Love", "Dear Thea", "Lovely Poorness", "Rose Cups" and "Iron Lily".

**d5: Maria Luisa De Crescenzo**

- [d5s0] Maria Luisa De Crescenzo (b. January 12, 1992) is an Italian actress.
- [d5s1]  Her credits include the television series "Rosso San Valentino" and the films "Young Europe", "David's Birthday" and "A Flat for Three".

**d6: A. P. Carter**

- [d6s0] Alvin Pleasant Delaney Carter (December 15, 1891 – November 7, 1960) professionally recording as A.P. Carter, was an American musician and founding member of The Carter Family, one of the most notable acts in the history of country music.

**d7: Happy Birthday to You**

- [d7s0] "Happy Birthday to You", more commonly known as simply "Happy Birthday", is a song that is traditionally sung to celebrate the anniversary of a person's birth.
- [d7s1]  According to the 1998 "Guinness World Records", "Happy Birthday to You" is the most recognized song in the English language, followed by "For He's a Jolly Good Fellow".
- [d7s2]  The song's base lyrics have been translated into at least 18 languages.
- [d7s3]  The melody of "Happy Birthday to You" comes from the song "Good Morning to All", which has traditionally been attributed to American sisters Patty and Mildred J. Hill in 1893, although the claim that the sisters composed the tune is disputed.

**d8: Garden (Totally Enormous Extinct Dinosaurs song)**

- [d8s0] "Garden" is a song by English electro producer and DJ Totally Enormous Extinct Dinosaurs featuring Vocals by Luisa Gerstein.
- [d8s1]  The track was released in the United Kingdom on October 14, 2011 as the second single from his debut studio album, Trouble.
- [d8s2]  The song was written by Orlando Higginbottom and produced by Totally Enormous Extinct Dinosaurs.

**d9: María Luisa Anido**

- [d9s0] María Luisa Anido (Isabel María Luisa Anido González) (26 January 1907 – 4 June 1996) was an Argentine classical guitarist and composer.

**d10: Landshapes**

- [d10s0] Landshapes is a British band known primarily for their effects-heavy psychedelic alternative rock.
- [d10s1]  They released their debut full-length album "Rambutan" on indie record label Bella Union in 2013 and their second, "Heyoon", in May 2015.
- [d10s2]  The band consists of Dan Blackett, Jemma Freeman, Heloise Tunstall-Behrens and Luisa Gerstein.
- [d10s3]  They were previously called Lulu and the Lampshades.

## 21. hotpotqa_5a79289d55429907847277cf

原位置：`train` 第 141 题 · 全局第 141 题 · `sample_id: hotpotqa_5a79289d55429907847277cf`

Question: What band was formed first, Weezer or Royal Blood?

Note:

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | year Weezer was formed | False | () |
| u2 | year Royal Blood was formed | False | () |
| u3 | which band was formed first | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | year Weezer was formed | False | [] | 1992 | [['d4s0']] |
| u2 | year Royal Blood was formed | False | [] | 2013 | [['d6s0'], ['d5s0']] |
| u3 | which of Weezer and Royal Blood was formed first | True | ['u1', 'u2'] | Weezer | [[]] |

### Source documents (reference only)

**d1: Come On Over (Royal Blood song)**

- [d1s0] "Come On Over" is a song written by Mike Kerr and Ben Thatcher of British rock duo Royal Blood.
- [d1s1]  The song was originally recorded by the duo for the band's debut single, "Out of the Black", where it appeared as the B-side.
- [d1s2]  The track later appeared as the third track on the band's debut extended play "Out of the Black", and as the second track on the band's eponymous debut studio album, "Royal Blood".
- [d1s3]  The track also appeared on the band's third single, released by Black Mammoth Records and Warner Bros.
- [d1s4]  Records on 21 April 2014.
- [d1s5]  "Come On Over" also appears on the soundtrack for "WWE 2K15" and "Guitar Hero Live".

**d2: Royal Blood (album)**

- [d2s0] Royal Blood is the eponymous debut studio album by British rock duo Royal Blood.
- [d2s1]  The album, produced by the band and Tom Dalgety, was released by Warner Bros.
- [d2s2]  Records on 22 August 2014 in Friday-release countries and on 25 August 2014 in the United Kingdom.

**d3: Figure It Out (Royal Blood song)**

- [d3s0] "Figure It Out" is a song written by Mike Kerr and Ben Thatcher of British rock duo Royal Blood.
- [d3s1]  The song was originally recorded by the duo for the band's eponymous debut studio album, "Royal Blood", where it appears as the third track on the album.
- [d3s2]  The track also appeared on the band's fourth single, released by Black Mammoth Records and Warner Bros.
- [d3s3]  Records on 18 August 2014 as the lead single promoting "Royal Blood".
- [d3s4]  "Figure It Out" also appears on the soundtrack for the video game "Pro Evolution Soccer 2016".

**d4: Weezer**

- [d4s0] Weezer is an American rock band formed in Los Angeles in 1992, consisting of Rivers Cuomo (lead vocals, guitar), Patrick Wilson (drums), Brian Bell (guitar, backing vocals, keyboards), and Scott Shriner (bass guitar, backing vocals).
- [d4s1]  Weezer has sold 9.2 million albums in the US and over 17 million worldwide.

**d5: Royal Blood discography**

- [d5s0] English hard rock band Royal Blood has released two studio albums, two extended plays (EPs), eight singles and nine music videos. Formed in Brighton in January 2013, Royal Blood is a duo consisting of bassist and vocalist Mike Kerr and drummer Ben Thatcher.
- [d5s1]  After signing with Warner Bros.
- [d5s2]  Records, the duo released their debut single "Out of the Black" in October 2013, which debuted at number 29 on the UK Rock & Metal Singles Chart.
- [d5s3]  In February 2014, "Little Monster" was issued as the band's second single, registering on the UK Singles Chart at number 95 and the UK Rock & Metal Singles Chart at number one.
- [d5s4]  Both singles were later issued alongside their B-sides on the EP "Out of the Black" in March. "
- [d5s5] Come On Over" – initially featured as the B-side to "Out of the Black" – was released as a single in April, reaching number 68 on the UK Singles Chart.
- [d5s6]  At the same time, "Little Monster" also returned to the charts, peaking at number 74 on the UK Singles Chart.

**d6: Royal Blood (band)**

- [d6s0] Royal Blood are an English rock duo formed in Brighton in 2013.
- [d6s1]  The band's sound is reminiscent of and rooted in modern blues rock, hard rock, garage rock, stoner rock and psychedelic rock.
- [d6s2]  Their first album "Royal Blood" was released in August 2014.

**d7: Out of the Black (song)**

- [d7s0] "Out of the Black" is a song written by Mike Kerr and Ben Thatcher of British rock duo Royal Blood.
- [d7s1]  The song was originally recorded by the duo for release as a single, appearing on the band's debut single of the same name, released by Black Mammoth Records on 11 November 2013.
- [d7s2]  The track later appeared as the opening track on the band's debut extended play "Out of the Black", and as the opening track on the band's eponymous debut studio album, "Royal Blood".
- [d7s3]  The track was also part of the soundtrack to the film "Who Am I – No System Is Safe", as well as the video games "Forza Horizon 2" and "EA Sports UFC".
- [d7s4]  It was also used in a featurette for the Netflix series "Daredevil" at the 2015 New York Comic Con.
- [d7s5]  The song was also the official theme song for the 2016 professional wrestling event "WWE Roadblock".
- [d7s6]  This song has also been covered by Billie Marten.

**d8: The Sword Stained with Royal Blood (film)**

- [d8s0] The Sword Stained with Royal Blood is a 1993 Hong Kong film based on Louis Cha's novel "Sword Stained with Royal Blood".
- [d8s1]  The film was written, produced and directed by Cheung Hoi-ching and stars Yuen Biao, Sharla Cheung, Danny Lee, Ng Man-tat and Anita Yuen

**d9: Little Monster (song)**

- [d9s0] "Little Monster" is a song written by Mike Kerr and Ben Thatcher of British rock duo Royal Blood.
- [d9s1]  The song was originally recorded by the duo for release as a single, appearing on the band's second single of the same name, released by Black Mammoth Records and Warner Bros.
- [d9s2]  Records on 10 February 2014.
- [d9s3]  The single marked the band's first release under Warner Bros.
- [d9s4]  Records after signing with the label in 2013.
- [d9s5]  The track later appeared as the second track on the band's debut extended play "Out of the Black", and as the sixth track on the band's eponymous debut studio album, "Royal Blood".
- [d9s6]  It is currently the duo's highest-charting single.
- [d9s7]  The song is included as a playable track in "Guitar Hero Live".

**d10: Gemfire**

- [d10s0] Gemfire (released in Japan as Royal Blood or ロイヤルブラッド "Roiyaru Buraddo", Super Royal Blood or スーパーロイヤルブラッド "Sūpā Roiyaru Buraddo" in its Super Famicom version) is a medieval war game for the MSX, Nintendo Entertainment System, Super NES, FM Towns, Mega Drive/Genesis, MS-DOS, and later Windows, developed by Koei.
- [d10s1]  The object in the game is to unify a fictional island by force.
- [d10s2]  Players use infantry, cavalry, and archers, as well as fantasy units such as magicians, dragons or gargoyles in order to capture the castle needed to control that particular territory.

## 22. hotpotqa_5a7a166f5542990783324e48

原位置：`train` 第 142 题 · 全局第 142 题 · `sample_id: hotpotqa_5a7a166f5542990783324e48`

Question: What American actor stars in the sixth installment in the "Saw" franchise?

Note:

Type: bridge · fallback: False · SFT snapshots: 7

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | sixth installment in the "Saw" franchise | False | () |
| u2 | American actor starring in {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | sixth installment in the Saw franchise | False | [] | Saw VI | [['d2s1']] |
| u2 | American actor who stars in {u1} | True | ['u1'] | Tobin Bell | [['d2s1', 'd6s0']] |

### Source documents (reference only)

**d1: Mission: Impossible 6**

- [d1s0] Mission: Impossible 6 is an upcoming American action spy film written, co-produced and directed by Christopher McQuarrie.
- [d1s1]  It is the sixth installment in the and stars Tom Cruise, Rebecca Ferguson, Ving Rhames, Simon Pegg, Michelle Monaghan, Alec Baldwin and Sean Harris all reprising their roles from previous films, with Henry Cavill, Vanessa Kirby, Sian Brooke and Angela Bassett joining the franchise.
- [d1s2]  The film will be released on July 27, 2018, by Paramount Pictures and will be the first film in the series to be released in 3D.

**d2: Saw VI**

- [d2s0] Saw VI is a 2009 American horror film directed by Kevin Greutert from a screenplay written by Patrick Melton and Marcus Dunstan.
- [d2s1]  It is the sixth installment in the "Saw" franchise and stars Tobin Bell, Costas Mandylor, Betsy Russell, Mark Rolston, Peter Outerbridge, and Shawnee Smith.
- [d2s2]  It was produced by Mark Burg and Oren Koules of Twisted Pictures and distributed by Lionsgate.

**d3: Curse of Chucky**

- [d3s0] Curse of Chucky is a 2013 American supernatural slasher film and the sixth installment of the "Child's Play" franchise.
- [d3s1]  The film was written and directed by Don Mancini, who created the franchise and wrote all films to date.
- [d3s2]  It stars Brad Dourif as Chucky and Fiona Dourif as Nica Pierce, as well as Danielle Bisutti, A Martinez and Brennan Elliott.
- [d3s3]  The film grossed $3.4 million in DVD sales.

**d4: The Texas Chainsaw Massacre: The Beginning**

- [d4s0] The Texas Chainsaw Massacre: The Beginning is a 2006 American slasher film and a prequel to the 2003 film "The Texas Chainsaw Massacre".
- [d4s1]  The sixth installment in "The Texas Chainsaw Massacre" franchise was directed by Jonathan Liebesman and co-produced by Kim Henkel and Tobe Hooper (co-creators of the original 1974 film).
- [d4s2]  The film went into release in North America on October 6, 2006.
- [d4s3]  The film's story takes place four years before the timeline of the 2003 film.
- [d4s4]  It stars Jordana Brewster, Diora Baird, Taylor Handley, Matt Bomer and R. Lee Ermey.

**d5: Magic to Win**

- [d5s0] Magic to Win (Chinese: 開心魔法, meaning "Happy Magic") is a 2011 Hong Kong film directed by Wilson Yip.
- [d5s1]  The film stars Wu Chun, Karena Ng, Raymond Wong, Wu Jing and Louis Koo.
- [d5s2]  It is a sixth installment of the "Happy Ghost" film franchise, but a completely different version of the story.

**d6: Tobin Bell**

- [d6s0] Tobin Bell (born Joseph Henry Tobin, Jr.; August 7, 1942) is an American actor.
- [d6s1]  He is best known for his portrayal of John Kramer / Jigsaw of the "Saw" film series.
- [d6s2]  After years of work doing stand-ins and background work on films, he got his first major acting job in "Mississippi Burning" (1988) and went on to star in made-for-television films and guest star in television shows throughout the 1990s.

**d7: Mortal Kombat: Deception**

- [d7s0] Mortal Kombat: Deception is a fighting video game developed and published by Midway as the sixth installment of the "Mortal Kombat" ("MK") video game franchise.
- [d7s1]  It was released for the PlayStation 2 and Xbox in October 2004, and for the Nintendo GameCube in March 2005.
- [d7s2]  "Mortal Kombat: Deception" follows the storyline from the fifth installment, "".
- [d7s3]  Its story centers on the revival of the Dragon King Onaga, who attempts to conquer the realms featured in the series after defeating the sorcerers Quan Chi and Shang Tsung, the main antagonists in the previous game, and the Thunder God Raiden, defender of Earthrealm.
- [d7s4]  The surviving warriors from the previous titles join forces to confront Onaga.

**d8: Fast &amp; Furious 6**

- [d8s0] Fast & Furious 6 (alternatively known as Furious 6 or Fast Six) is a 2013 American action film directed by Justin Lin and written by Chris Morgan.
- [d8s1]  It is the sixth installment in "The Fast and the Furious" franchise.
- [d8s2]  The film stars Vin Diesel, Paul Walker, Dwayne Johnson, Michelle Rodriguez, Jordana Brewster, Tyrese Gibson, Chris Bridges, Sung Kang, Luke Evans, Gina Carano, and John Ortiz.
- [d8s3]  "Fast & Furious 6" follows a professional criminal gang led by Dominic Toretto (Diesel) who have retired following their successful heist in "Fast Five" (2011), but remain wanted fugitives.
- [d8s4]  U.S. Diplomatic Security Service (DSS) agent Luke Hobbs (Johnson) offers to clear the group's criminal records and allow them to return home in exchange for helping him to take down a skilled mercenary organization led by Owen Shaw (Evans), one member of which is Toretto's presumed-dead lover Letty Ortiz (Rodriguez).

**d9: List of Lady Jewelpet episodes**

- [d9s0] Lady Jewelpet (レディ ジュエルペット , Redi Juerupetto ) is the sixth installment of the Jewelpet anime franchise created by Sanrio and Sega and animated by both Zexcs and Studio Comet.
- [d9s1]  It was first announced by Sanrio on their official Twitter page to coincide with the anime franchise's 5th anniversary.
- [d9s2]  The series aired on April 5, 2014 on TV Tokyo and TV Osaka and is directed by Itsuro Kawasaki and written by Natsuko Takahashi.
- [d9s3]  It is the first "Jewelpet" installment to be officially handled by Zexcs who co-produced the "Jewelpet Twinkle" Fan Discs and the OVA episode.

**d10: American Pie Presents: Beta House**

- [d10s0] American Pie Presents: Beta House is a 2007 American sex comedy film released by Universal Pictures.
- [d10s1]  It is the third installment in the "American Pie Presents" series and the sixth installment in the "American Pie" franchise.
- [d10s2]  The film concludes a story arc that begins with "" (2006).
- [d10s3]  John White stars as Erik Stifler, a college freshman who pledges the Beta House fraternity led by his cousin Dwight Stifler (Steve Talley).
- [d10s4]  Christopher McDonald co-stars as Erik's father and Eugene Levy plays Beta House alumnus Noah Levenstein.

## 23. hotpotqa_5a7a168a5542996a35c170c7

原位置：`train` 第 143 题 · 全局第 143 题 · `sample_id: hotpotqa_5a7a168a5542996a35c170c7`

Question: The mother of Archduchess Elisabeth Marie of Austria, was born on which day ?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | mother of Archduchess Elisabeth Marie of Austria | False | () |
| u2 | birth date of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | mother of Archduchess Elisabeth Marie of Austria | False | [] | Princess Stéphanie of Belgium | [['d7s0'], ['d2s0']] |
| u2 | birth date of {u1} | True | ['u1'] | 21 May 1864 | [['d3s0']] |

### Source documents (reference only)

**d1: Archduchess Elisabeth Franziska of Austria**

- [d1s0] Archduchess Elisabeth Franziska Maria of Austria (17 January 1831 – 14 February 1903) was born in Ofen (Buda), Hungary, the daughter of Palatine Joseph of Hungary (1776–1847) and his third wife Maria Dorothea of Württemberg (1797–1855).

**d2: Princess Stephanie of Windisch-Graetz**

- [d2s0] Princess Stéphanie of Windisch-Graetz (April 4, 1909 in Ploskovice, Bohemia – May 29, 2005 in Uccle, Belgium) was the daughter of Prince Otto Weriand of Windisch-Graetz (1873–1952) and Archduchess Elisabeth Marie of Austria (1883–1963), only child of Crown Prince Rudolf of Austria and Princess Stéphanie of Belgium.
- [d2s1]  She was the great-grandchild of Emperor Franz-Joseph and Empress Elisabeth ('Sissi') of Austria.
- [d2s2]  She was also the great-grandchild of King Leopold II of Belgium.

**d3: Princess Stéphanie of Belgium**

- [d3s0] Princess Stéphanie of Belgium (21 May 1864 – 23 August 1945) was a Belgian princess by birth and became Crown Princess of Austria through her marriage to the heir-apparent of the Habsburg dynasty, Archduke Rudolf.
- [d3s1]  She was famously widowed in 1889 when Rudolf and his mistress, Mary Vetsera, were found dead in an apparent murder-suicide pact at the Imperial hunting lodge at Mayerling in the Vienna Woods.

**d4: Maria Theresa of Austria-Este (1849–1919)**

- [d4s0] Maria Theresa of Austria-Este (Maria Theresa Henriette Dorothee; 2 July 1849 – 3 February 1919) was the last Queen of Bavaria.
- [d4s1]  She was the daughter and only child of Archduke Ferdinand of Austria-Este and his wife, Archduchess Elisabeth of Austria.

**d5: Prince Karl Alfred of Liechtenstein**

- [d5s0] Prince Karl Alfred of Liechtenstein (Karl Alfred Maria Johannes Baptista Heinrich Aloys Georg Hartmann Ignatius; 16 August 1910 – 17 November 1985) was a Liechtensteiner prince and brother of Franz Joseph II.
- [d5s1]  He was the third child and second son of Prince Aloys of Liechtenstein and Archduchess Elisabeth Amalie of Austria.

**d6: Archduchess Elisabeth of Austria (1922–1993)**

- [d6s0] Archduchess Elisabeth of Austria (31 May 1922 – 6 January 1993) was a member of the House of Habsburg-Lorraine.
- [d6s1]  She was the youngest daughter of Charles I, the last Emperor of Austria, and his wife Zita of Bourbon-Parma.

**d7: Archduchess Elisabeth Marie of Austria**

- [d7s0] Archduchess Elisabeth Marie of Austria (Elisabeth Maria Henriette Stephanie Gisela; 2 September 1883 – 16 March 1963) was the only child of Rudolf, Crown Prince of Austria and Princess Stéphanie of Belgium, and a granddaughter of Emperor Franz Joseph I of Austria and King Leopold II of the Belgians.
- [d7s1]  She was known to the family as "Erzsi", a diminutive of her name in Hungarian.
- [d7s2]  Later nicknamed "The Red Archduchess", she was famous for becoming a socialist and a member of the Austrian Social Democratic Party.

**d8: Stéphanie Windisch-Graetz**

- [d8s0] Stéphanie Windisch-Graetz (born 17 July 1939) is the daughter of Prince Franz Joseph zu Windisch-Graetz and granddaughter of Archduchess Elisabeth Marie of Austria.
- [d8s1]  Archduchess Elisabeth was the daughter of Rudolf, Crown Prince of Austria and granddaughter of Emperor Franz Joseph I of Austria.

**d9: Archduchess Elisabeth Amalie of Austria**

- [d9s0] Archduchess Elisabeth Amalie of Austria (7 July 1878 – 13 March 1960) was a daughter of Archduke Karl Ludwig of Austria and his third wife Infanta Maria Theresa of Portugal.
- [d9s1]  She was the mother of Franz Joseph II, Prince of Liechtenstein, and the paternal grandmother of Hans-Adam II, Prince of Liechtenstein.

**d10: Archduchess Elisabeth Franziska of Austria (1892–1930)**

- [d10s0] Archduchess Elisabeth Franziska of Austria (1892–1930)

## 24. hotpotqa_5a7a22d45542990783324e80 【保留新拆法｜重标人工标签】

原位置：`train` 第 144 题 · 全局第 144 题 · `sample_id: hotpotqa_5a7a22d45542990783324e80`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5a7a22d45542990783324e80"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 问题已明确给出 Teen Wolf 和开发者，旧 gold 再设“Tom Choi 以哪部剧著称”作为必须先满足的依赖，重复验证已给信息。
>
> **处理建议：** 保留 single 拆法，按 d7s0 标注一个频道单元；描述最好使用“channel for which Teen Wolf was developed”，与问题精确对应。移除旧 u1 依赖及多余快照标签。
>
> **证据定位：** d1s0, d7s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Tom Choi, born in Taegu, South Korea, is a Korean-American actor best known for "Teen Wolf", Teen Wolf is an American television series developed by Jeff Davis, for which channel?

Note:

Type: single · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | network that airs Teen Wolf | True | () |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | American television series for which Tom Choi is known | False | [] | Teen Wolf | [['d1s0']] |
| u2 | channel for which Jeff Davis developed {u1} | True | ['u1'] | MTV | [['d7s0'], ['d6s0'], ['d5s0'], ['d8s1'], ['d3s0']] |

### Source documents (reference only)

**d1: Tom Choi**

- [d1s0] Tom Choi, born in Taegu, South Korea, is a Korean-American actor best known for "Teen Wolf" and "Mortal Kombat".

**d2: Teen Wolf (1986 TV series)**

- [d2s0] Teen Wolf, known as The Cartoon Adventures of Teen Wolf in the United Kingdom, is an animated American television series broadcast from 1986 to 1987 that was produced by Southern Star Productions and Hanna-Barbera Australia in association with Clubhouse Pictures in the first season and Atlantic/Kushner-Locke in the second season.
- [d2s1]  It was based on the 1985 live-action film, "Teen Wolf".

**d3: List of Teen Wolf characters**

- [d3s0] "Teen Wolf" is an American television series that airs on MTV.
- [d3s1]  The series premiered on Sunday, June 5, 2011, following the 2011 MTV Movie Awards.
- [d3s2]  "Teen Wolf" is a supernatural drama series that follows Scott McCall (Tyler Posey), a high school student and social outcast who is bitten by a werewolf.
- [d3s3]  He tries to maintain a normal life while hiding his secret and dealing with supernatural dangers that plague the town of Beacon Hills.
- [d3s4]  He is aided by his best friend, Stiles Stilinski (Dylan O'Brien), and mysterious werewolf, Derek Hale (Tyler Hoechlin).

**d4: Teen Wolf (season 4)**

- [d4s0] The fourth season of "Teen Wolf", an American supernatural drama created by Jeff Davis and to some extent, based on the Teen Wolf 1985 film of the same name, premiered on June 23, 2014.
- [d4s1]  The series was renewed for a fourth season of 12 episodes on October 12, 2013.

**d5: Teen Wolf (season 1)**

- [d5s0] The first season of "Teen Wolf", an American supernatural drama, was developed by Jeff Davis based upon the 1985 film of the same name, premiered on June 5, 2011 and concluded on August 15, 2011 on the MTV network.
- [d5s1]  The season featured 12 episodes.

**d6: List of Teen Wolf episodes**

- [d6s0] "Teen Wolf" is an American supernatural drama developed by Jeff Davis loosely based upon the 1985 film of the same name and a screenplay by Jeph Loeb & Matthew Weisman, which premiered on June 5, 2011 on MTV.
- [d6s1]  The series stars Tyler Posey as Scott McCall, a teenager who transforms into a werewolf after being bitten by one.

**d7: Teen Wolf (2011 TV series)**

- [d7s0] Teen Wolf is an American television series developed by Jeff Davis for MTV.
- [d7s1]  It is loosely based on the 1985 film of the same name, and stars Tyler Posey as a teenager named Scott McCall, who is bitten by a werewolf and must cope with how it affects his life and the lives of those closest to him, and Dylan O'Brien as "Stiles" Stilinski, Scott's best friend.
- [d7s2]  The series has received generally positive reviews from critics and is a fan favorite on social media.

**d8: Jeff Davis (writer)**

- [d8s0] Jeff Davis (born June 13, 1975) is an American writer and television producer.
- [d8s1]  He is best known for creating the CBS crime drama "Criminal Minds" and MTV's "Teen Wolf", a television series reboot of the 1985 film of the same name.

**d9: Teen Wolf (season 3)**

- [d9s0] The third season of "Teen Wolf", an American supernatural drama created by Jeff Davis and to some extent, based on the 1985 film of the same name, premiered on June 3, 2013.
- [d9s1]  The series was renewed for a third season of 24 episodes on July 12, 2012.

**d10: List of Scream episodes**

- [d10s0] "Scream" is an American slasher horror television series developed by Jill Blotevogel, Dan Dworkin and Jay Beattie for MTV and is based on the slasher film series of the same name created by Kevin Williamson.
- [d10s1]  The series premiered of June 30, 2015, following the airing of the second episode of the fifth season of "Teen Wolf", to mixed reviews from critics, though it has slowly earned a strong fan base throughout its run.

## 25. hotpotqa_5a7a46785542990783324ee5 【保留新拆法｜重标人工标签】

原位置：`train` 第 145 题 · 全局第 145 题 · `sample_id: hotpotqa_5a7a46785542990783324ee5`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5a7a46785542990783324ee5"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 旧拆法用两方事实+共同结论，新 multipart 分别要求回答两个对象的同一属性，两方都是 necessary。两种都能覆盖题目要求；没有显式共同结论不等于漏答。按用户要求保留生成的两个必要单元。
>
> **处理建议：** 保持 multipart 和两个 necessary=true。分别映射旧u1/u2的属性值和证据，删除旧u3作为独立训练目标；只有两方都支持才是完整。若旧共同答案词过窄，按各方实际描述设置值/别名，不改变新拆法。
>
> **证据定位：** d5s0, d2s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: What type of publication is Popular Mechanics and Sojourners?

Note:

Type: multipart · fallback: False · SFT snapshots: 7

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | type of publication for Popular Mechanics | True | () |
| u2 | type of publication for Sojourners | True | () |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | type of publication Popular Mechanics is | False | [] | magazine | [['d5s0'], ['d1s2'], ['d9s0'], ['d8s1'], ['d10s2'], ['d7s0']] |
| u2 | type of publication Sojourners is | False | [] | magazine | [['d2s0'], ['d2s2'], ['d2s4']] |
| u3 | type of publication that Popular Mechanics and Sojourners both are | True | ['u1', 'u2'] | magazine | [[]] |

### Source documents (reference only)

**d1: Benjamin Chertoff**

- [d1s0] Benjamin Chertoff is a journalist, photographer and video producer.
- [d1s1]  He is most known for his work on the Popular Mechanics article .
- [d1s2]  He also created the Popular Mechanics Show, the weekly podcast of Popular Mechanics magazine.
- [d1s3]  He is currently a freelance photojournalist, writer and documentary producer.

**d2: Sojourners**

- [d2s0] Sojourners magazine is a progressive monthly publication of the American Christian social justice organization Sojourners, which arose out of the Sojourners Community.
- [d2s1]  It was first published in 1971 under the original title of "The Post-American".
- [d2s2]  The magazine publishes editorials and articles on Christianity and politics, the church and social issues, social justice, and Christian living.
- [d2s3]  Articles frequently feature coverage of fair trade, interfaith dialogue, peacemaking, and work to alleviate poverty.
- [d2s4]  The offices of the magazine are in Washington, D.C.

**d3: Atlas Press (tool company)**

- [d3s0] Atlas Press Co. was a tool company that manufactured popular brands of metalworking tools from 1920 to the mid-1970s.
- [d3s1]  Many of their products received wide coverage in "Popular Mechanics" and "Popular Science" at the time.

**d4: SpaceCub**

- [d4s0] SpaceCub was a design project for a homebuilt rocket.
- [d4s1]  Between 1993 and 1994, Geoffrey A. Landis proposed that a vehicle designed to launch to the edge of space might be a feasible project for a "personal" spaceship, the equivalent of a Piper Cub for space.
- [d4s2]  The insight was that a flight to "only" 100 km would reach the officially-defined edge of space, and even though this is much easier a challenge than an orbital flight, such a suborbital flight would be of excitement to the public, and the pilot would be officially qualified as an astronaut.
- [d4s3]  A small group of rocket enthusiasts, computer hobbyists, and science-fiction writers gathered together to do a preliminary design, with the ultimate goal of moving on to building a prototype, with (then) physics student David Burkhead leading the technical effort.
- [d4s4]  The vehicle design was discussed in many venues, and presentations on the design progress were given in several conferences, such as the 1995NSS International Space Development Conference, where it attracted considerable popular attention.
- [d4s5]  The design was featured in print in places including the December 1994 Popular Mechanics, and the Brazilian popular magazine Istoé.

**d5: Popular Mechanics**

- [d5s0] Popular Mechanics is a classic magazine of popular science and technology.

**d6: Michael Belfiore**

- [d6s0] Michael Belfiore is an author and journalist.
- [d6s1]  Some of his notable works include "", published by Smithsonian Books "Rocketeers", and "The Way People Live - Life Aboard a Space Station".
- [d6s2]  He has written numerous articles for "Popular Mechanics" and "Popular Science"

**d7: Mechanix Illustrated**

- [d7s0] Mechanix Illustrated was an American magazine founded in the first half of the 20th century to compete against the older "Popular Science" and "Popular Mechanics".
- [d7s1]  Billed as "The How-To-Do Magazine," "Mechanix Illustrated" ("MI") aimed to guide readers through various projects from home improvements and advice on repairs to "build-your-own (sports car, telescope, helicopter, etc)."
- [d7s2]  It was headquartered in New York City.

**d8: Parker Jeanie's Teenie**

- [d8s0] The Parker Jeanie's Teenie, or JT-1, is a single-seat, single-engine sport aircraft first built in the United States in 1967 and marketed for homebuilding.
- [d8s1]  It was featured on the cover of a Popular Mechanics magazine issue in May, 1968.
- [d8s2]  The caption on the cover read, "Build This 'Flying Volkswagen' For Less Than $600!
- [d8s3] ."
- [d8s4]  The cost of materials has increased since the article's publication but the initial popularity of Parker's Jeanie's Teenie was high.
- [d8s5]  The Teenie would be certified in the Experimental category in the US.
- [d8s6]  A pilot license is required to fly one, as it is not considered an ultralight aircraft in the United States.

**d9: Popular Mechanics for Kids**

- [d9s0] Popular Mechanics for Kids (sometimes abbreviated to PMK) is an educational Canadian television series based on "Popular Mechanics" magazine.
- [d9s1]  It was notable for starting the careers of Elisha Cuthbert, Jay Baruchel and Tyler Kyte.
- [d9s2]  The show's intent is to teach viewers how things work.
- [d9s3]  It was awarded the Parents Choice Award in 2003, and was nominated for the Gemini Awards.

**d10: William Gurstelle**

- [d10s0] William Gurstelle (born March 29, 1956) is an American nonfiction author, magazine writer, and inventor.
- [d10s1]  He is a feature columnist for "Make" magazine and a columnist and contributing editor at "Popular Science" magazine.
- [d10s2]  Previously, he was the Pyrotechnics and Ballistics Editor at "Popular Mechanics" magazine.

## 26. hotpotqa_5a7a4cba5542990198eaf114

原位置：`train` 第 146 题 · 全局第 146 题 · `sample_id: hotpotqa_5a7a4cba5542990198eaf114`

Question: Who is older, Shaun Ryder or Fish?

Note:

Type: comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | birth date of Shaun Ryder | False | () |
| u2 | birth date of Fish | False | () |
| u3 | who is older | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | birth date of Shaun Ryder | False | [] | 23 August 1962 | [['d8s0']] |
| u2 | birth date of Fish | False | [] | 25 April 1958 | [['d6s0']] |
| u3 | who is older, Shaun Ryder or Fish | True | ['u1', 'u2'] | Fish | [[]] |

### Source documents (reference only)

**d1: Gogoselachus**

- [d1s0] Gogoselachus ("shark from the Gogo formation") is an extinct genus of cartilaginous fish known from the late Devonian of Australia.
- [d1s1]  It is one of the earliest well-preserved Devonian chondrichthyans (20 million years older than "Cladoselache"), as much more of the fish than just teeth and scales were preserved.
- [d1s2]  This rare preservation reveals some unique discoveries about the evolution of the cartilage that was inside later cartilaginous fish such as sharks, rays, and chimaeras.

**d2: Dare (song)**

- [d2s0] "Dare" (styled as "挑戦 (DARE)") is a song by British virtual band Gorillaz, taken as the second single from their second studio album, "Demon Days".
- [d2s1]  The track is sung by Rosie Wilson (also known as Roses Gabor) with backing vocals from Damon Albarn and features vocals by Happy Mondays frontman Shaun Ryder.
- [d2s2]  It peaked at No. 1 in the UK Singles Chart in September 2005, becoming the band's only UK No. 1.
- [d2s3]  In 2016, vocals of the song were interpolated in Friction's song "Dare (Hold It Down)".
- [d2s4]  In 2017 the song was featured in an episode of the British soap-opera ￼￼EastEnders.

**d3: Amateur Night in the Big Top**

- [d3s0] Amateur Night in the Big Top is the first official solo album by Shaun Ryder, of Happy Mondays and Black Grape.
- [d3s1]  The album is subtitled "Clowns and Pet Sounds".
- [d3s2]  It was released in September, 2003 and co-produced by Pete Carroll, Shane Norton and Cabaret Voltaire's Stephen Mallinder.
- [d3s3]  It was recorded in Perth, Australia and released on the Offworld Sounds record label run by Ryder's cousin Pete Carroll and Mallinder.

**d4: Demon Days**

- [d4s0] Demon Days is the second studio album by British virtual band Gorillaz, released on 11 May 2005 in Japan and on 23 May internationally by Parlophone Records and in the United States by Virgin Records.
- [d4s1]  The album features contributions from De La Soul, Neneh Cherry, Martina Topley-Bird, Roots Manuva, MF DOOM, Ike Turner, Bootie Brown of the Pharcyde, Shaun Ryder, Dennis Hopper, the London Community Gospel Choir, and a children's choir.
- [d4s2]  Frontman Damon Albarn brought in Danger Mouse as producer.

**d5: Maine Avenue Fish Market**

- [d5s0] The Maine Avenue Fish Market is an open air seafood market located in Southwest Washington, D.C. Also known as the Fish Wharf, or simply, the Wharf, the Maine Avenue Fish Market is one of the few surviving open air seafood markets on the east coast of the United States.
- [d5s1]  A local landmark, the Maine Avenue Fish Market is the oldest continuously operating fish market in the United States, seventeen years older than New York City's Fulton Fish Market.

**d6: Fish (singer)**

- [d6s0] Derek William Dick (born 25 April 1958), better known by his stage name Fish, is a Scottish singer-songwriter and occasional actor.
- [d6s1]  He achieved prominence as the lead singer and lyricist of the neo-progressive rock band Marillion from 1981 until 1988.
- [d6s2]  In his solo career, Fish has explored contemporary pop and traditional folk.

**d7: Kav Sandhu**

- [d7s0] KAV (Kav Sandhu) is a British musician from Leicester UK, based in Los Angeles.
- [d7s1]  KAV played guitar with British band Happy Mondays for 4 years after helping reform the band with frontman Shaun Ryder in 2004.
- [d7s2]  He launched his solo project under moniker "KAV" in 2008 with long-time friend and drummer Jim (James) Portas.
- [d7s3]  His solo material has been compared by the media to everyone from Iggy & The Stooges, Black Rebel Motorcycle Club, Primal Scream, Kasabian, The Rolling Stones & Bob Dylan.
- [d7s4]  He plays live with a full live band, which sometimes features guest musicians from various bands.

**d8: Shaun Ryder**

- [d8s0] Shaun William George Ryder (born 23 August 1962) is an English musician and singer-songwriter.
- [d8s1]  He is best known as the lead singer of the Happy Mondays and Black Grape.
- [d8s2]  He was the runner-up of the tenth series of "I'm a Celebrity...Get Me Out of Here!
- [d8s3] ".

**d9: Central Station Design**

- [d9s0] Central Station Design is a Mancunian design company founded by Pat Carroll, Karen Jackson, and Matt Carroll.
- [d9s1]  It is usually associated with Factory Records and the Madchester scene of the early 1990s.
- [d9s2]  The company created album cover artwork and posters for Factory artists including The Happy Mondays, Black Grape, and James.
- [d9s3]  Their design for the Happy Mondays' "Madchester Rave On E.P." in late 1989 became the iconic logo for the movement.
- [d9s4]  The Carrolls are cousins of Shaun and Paul Ryder of the Happy Mondays.

**d10: Happy Mondays**

- [d10s0] Happy Mondays are an English alternative rock band from Salford, Greater Manchester.
- [d10s1]  Formed in 1980, the band's original line-up was Shaun Ryder (vocals), his brother Paul Ryder (bass), Mark Day (guitar), Paul Davis (keyboard), and Gary Whelan (drums).
- [d10s2]  Mark "Bez" Berry later joined the band onstage as a dancer/percussionist.
- [d10s3]  Rowetta joined the band as a guest vocalist in 1990.

## 27. hotpotqa_5a7a572e5542990783324f1c 【保留新拆法｜重标人工标签】

原位置：`train` 第 147 题 · 全局第 147 题 · `sample_id: hotpotqa_5a7a572e5542990783324f1c`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5a7a572e5542990783324f1c"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 问题已明示 May Sinclair 与 Mary Amelia St. Clair 的身份关系，旧 gold 却把识别该作家作为第一跳。
>
> **处理建议：** 保留 single，直接询问该作家的作品数量；用 d10s0 支持。旧人物识别单元不应继续阻塞数量单元。
>
> **证据定位：** d2s1, d10s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: In literary criticism, stream of consciousness is a narrative mode or method, that attempts to depict the multitudinous thoughts and feelings which pass through the mind, the term was coined by William James in 1890 in his "The Principles of Psychology", and in 1918 the novelist May Sinclair, Sinclair was the pseudonym of Mary Amelia St. Clair (24 August 1863 – 14 November 1946), a popular British writer who wrote about how many novels, short stories and poetry?

Note:

Type: single · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | number of novels, short stories, and poetry written by Mary Amelia St. Clair | True | () |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | novelist who first applied the term stream of consciousness in a literary context in 1918 | False | [] | May Sinclair | [['d2s1']] |
| u2 | number of novels, short stories and poetry written by {u1} | True | ['u1'] | two dozen | [['d10s0']] |

### Source documents (reference only)

**d1: Aidan Higgins**

- [d1s0] Aidan Higgins (3 March 1927 – 27 December 2015) was an Irish writer.
- [d1s1]  He wrote short stories, travel pieces, radio drama and novels.
- [d1s2]  Among his published works are "Langrishe, Go Down" (1966), "Balcony of Europe" (1972) and the biographical "Dog Days" (1998).
- [d1s3]  His writing is characterised by non-conventional foreign settings and a stream of consciousness narrative mode.
- [d1s4]  Most of his early fiction is autobiographical - "like slug trails, all the fiction happened."

**d2: Stream of consciousness (narrative mode)**

- [d2s0] In literary criticism, stream of consciousness is a narrative mode or method that attempts to depict the multitudinous thoughts and feelings which pass through the mind.
- [d2s1]  The term was coined by William James in 1890 in his "The Principles of Psychology", and in 1918 the novelist May Sinclair (1863–1946) first applied the term stream of consciousness, in a literary context, when discussing Dorothy Richardson's (1873–1957) novels. "
- [d2s2] Pointed Roofs" (1915), the first work in Richardson's series of 13 semi-autobiographical novels titled "Pilgrimage", is the first complete stream of consciousness novel published in English.
- [d2s3]  However, in 1934, Richardson comments that "Proust, James Joyce, Virginia Woolf & D.R. ... were all using 'the new method', though very differently, simultaneously".

**d3: Gladys Bronwyn Stern**

- [d3s0] Gladys Bronwyn Stern or GB Stern (17 June 1890 – 20 September 1973), born Gladys "Bertha" Stern in London, England, wrote many novels, short stories, plays, memoirs, biographies and literary criticism.

**d4: Stream of consciousness (psychology)**

- [d4s0] Stream of consciousness refers to the flow of thoughts in the conscious mind.
- [d4s1]  Research studies have shown that we only experience one mental event at a time as a fast-moving mind stream.
- [d4s2]  William James, often considered to be the father of American psychology, first coined the phrase "stream of consciousness".
- [d4s3]  The full range of thoughts—that one can be aware of—can form the content of this stream.

**d5: The Principles of Psychology**

- [d5s0] The Principles of Psychology is an 1890 book about psychology by William James, an American philosopher and psychologist who trained to be a physician before going into psychology.
- [d5s1]  There are four methods from James' book: stream of consciousness (James' most famous psychological metaphor); emotion (later known as the James–Lange theory); habit (human habits are constantly formed to achieve certain results); and will (through James' personal experiences in life).

**d6: Hubert Crackanthorpe**

- [d6s0] Hubert Montague Crackanthorpe born (12 May 1870 – c. November 1896) was a Victorian British writer who created works mainly in the genres of the essay, short story, and novella.
- [d6s1]  He also wrote limited amounts of literary criticism.
- [d6s2]  After dying early and under mysterious circumstances, his name is now little known and has all but vanished from conventional literary biographies of the period.
- [d6s3]  Crackanthorpe is usually associated with the literary movement of naturalism.
- [d6s4]  His literary legacy consists largely of three volumes of short stories he managed to publish during his lifetime; contemporary opinions of his talent as a writer varied widely, though one of his works was published with an appreciation by none other than Henry James.

**d7: Pointed Roofs**

- [d7s0] Pointed Roofs, published in 1915, is the first work (she called it a "chapter") in Dorothy Richardson's (1873 – 1957) series of 13 semi-autobiographical novels titled "Pilgrimage", and the first complete stream of consciousness novel published in English.
- [d7s1]  The novelist May Sinclair (1863 – 1946) first applied the term "stream of consciousness" In a review of "Pointed Roofs" ("The Egoist" April 1918).

**d8: Sciousness**

- [d8s0] Sciousness, a term coined by William James in "The Principles of Psychology", refers to consciousness separate from consciousness of self.
- [d8s1]  James wrote:

**d9: Stream of unconsciousness (narrative mode)**

- [d9s0] In literary criticism, stream of unconsciousness is a narrative mode that portrays an individual's point of view by transcribing the author's unconscious dialogue or "somniloquy" during sleep, in connection to his or her actions within a dream.

**d10: May Sinclair**

- [d10s0] May Sinclair was the pseudonym of Mary Amelia St. Clair (24 August 1863 – 14 November 1946), a popular British writer who wrote about two dozen novels, short stories and poetry.
- [d10s1]  She was an active suffragist, and member of the Woman Writers' Suffrage League.
- [d10s2]  May Sinclair was also a significant critic in the area of modernist poetry and prose, and she is attributed with first using the term stream of consciousness in a literary context, when reviewing the first volumes of Dorothy Richardson's novel sequence "Pilgrimage" (1915–67), in "The Egoist", April 1918.

## 28. hotpotqa_5a7aa2135542995eb53be882

原位置：`train` 第 148 题 · 全局第 148 题 · `sample_id: hotpotqa_5a7aa2135542995eb53be882`

Question: Who was born first, James Schuyler or Robert Lowell?

Note:

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | birth date of James Schuyler | False | () |
| u2 | birth date of Robert Lowell | False | () |
| u3 | who was born first | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | birth date of James Schuyler | False | [] | November 9, 1923 | [['d5s0']] |
| u2 | birth date of Robert Lowell | False | [] | March 1, 1917 | [['d4s0']] |
| u3 | which of James Schuyler and Robert Lowell was born first | True | ['u1', 'u2'] | Robert Lowell | [[]] |

### Source documents (reference only)

**d1: Waking in the Blue**

- [d1s0] 'Waking in the Blue' is a poem by Robert Lowell that was published in his book "Life Studies" and is a striking, early example of confessional poetry.
- [d1s1]  Of the handful of poems from "Life Studies" in which Lowell explored his struggles with mental illness, this poem was one of Lowell's most forthwright admissions that he was mentally ill.
- [d1s2]  Though he doesn't discuss the exact nature of his mental illness in the poem, he does describe his hospitalization in a mental institution.
- [d1s3]  Lowell's admission of having spent time in a mental institution was considered a brave one to make when he published the poem in 1959, when public disclosure about mental illness was a serious social taboo.

**d2: Trevor Winkfield**

- [d2s0] Trevor Winkfield (born 1944) is a British-born artist and writer.
- [d2s1]  Drawing upon his interest in both modernist literary movements and medieval architecture and pageantry, Winkfield has collaborated with many contemporary poets and writers, including John Ashbery, Harry Mathews, James Schuyler, and Ron Padgett.

**d3: Charles North (poet)**

- [d3s0] Charles North (born June 9, 1941) is an American poet, essayist and teacher.
- [d3s1]  Described by the poet James Schuyler as “the most stimulating poet of his generation,” he has received two National Endowment for the Arts Creative Writing Fellowships, an Individual Artist’s Grant from the Foundation for Contemporary Arts, four Fund for Poetry awards, and a Poets Foundation award.

**d4: Robert Lowell**

- [d4s0] Robert Traill Spence Lowell IV ( ; March 1, 1917 – September 12, 1977) was an American poet.
- [d4s1]  He was born into a Boston Brahmin family that could trace its origins back to the "Mayflower".
- [d4s2]  His family, past and present, were important subjects in his poetry.
- [d4s3]  Growing up in Boston also informed his poems, which were frequently set in Boston and the New England region.
- [d4s4]  The literary scholar Paula Hayes believes that Lowell mythologized New England, particularly in his early work.

**d5: James Schuyler**

- [d5s0] James Marcus Schuyler (November 9, 1923 – April 12, 1991) was an American poet.
- [d5s1]  His awards include the Pulitzer Prize for Poetry for his 1980 collection "The Morning of the Poem".
- [d5s2]  He was a central figure in the New York School and is often associated with fellow New York School poets John Ashbery, Frank O'Hara, Kenneth Koch, and Barbara Guest.

**d6: Life Studies**

- [d6s0] Life Studies is the fourth book of poems by Robert Lowell.
- [d6s1]  Most critics (including Helen Vendler, Steven Gould Axelrod, Adam Kirsch, and others) consider it one of Lowell's most important books, and the Academy of American Poets named it one of their "Groundbreaking Books."
- [d6s2]  Helen Vendler called "Life Studies" Lowell's "most original book."

**d7: Pierre Martory**

- [d7s0] Pierre Martory (December 1, 1920 – October 5, 1998) was a French poet whose influence on New York School poets was quiet but profound.
- [d7s1]  His work was admired by Frank O'Hara, James Schuyler, Harry Mathews, and others, and translated extensively by John Ashbery, with whom he shared his life in Paris for nearly a decade.
- [d7s2]  His work has appeared in many books in both England and the United States, as well as in "The New Yorker" and "Poetry".
- [d7s3]  Martory’s personal “charm,” the poet Ann Lauterbach once said, “devolved back to the original meaning of ‘spell.
- [d7s4] ’” However, as Ashbery has noted, “Both the humor and the sadness in his poems are always rendered with an unemphatic clarity that is certainly Mozartian.”

**d8: Locus Solus (journal)**

- [d8s0] Locus Solus was an American journal of experimental poetry and prose that published four issues in 1961 and 1962, one a double issue.
- [d8s1]  The magazine was edited by the poets John Ashbery, Kenneth Koch, and James Schuyler, all of whom contributed to its four issues.
- [d8s2]  The content was completely in English but the journal was published in France (in Lans-en-Vercors) by Harry Mathews.

**d9: Darragh Park**

- [d9s0] Darragh Park (July 24, 1939 – April 17, 2009) was an American Artist, and the literary executor of the estate of Pulitzer Prize–winning poet James Schuyler.
- [d9s1]  Perhaps best known for his book cover illustrations, Park painted landscapes as well as cityscapes in the style of Fairfield Porter.
- [d9s2]  He was based in Bridgehampton, NY and his works were on exhibit at the Parrish Art Museum.
- [d9s3]  and at the Guild Hall in East Hampton.

**d10: Lord Weary's Castle**

- [d10s0] Lord Weary's Castle, Robert Lowell's second book of poetry, won the Pulitzer Prize for Poetry in 1947 when Lowell was only thirty.
- [d10s1]  Robert Giroux, who was the publisher of Lowell's wife at the time, Jean Stafford, also became Lowell's publisher after he saw the manuscript for "Lord Weary's Castle" and was very impressed; he later stated that "Lord Weary's Castle" was the most successful book of poems that he ever published.

## 29. hotpotqa_5a7da4da5542997cc2c47468

原位置：`train` 第 149 题 · 全局第 149 题 · `sample_id: hotpotqa_5a7da4da5542997cc2c47468`

Question: Facing Sudan and Seal Island are both what genre of movie?

Note:

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | genre of Facing Sudan | False | () |
| u2 | genre of Seal Island | False | () |
| u3 | what genre both movies are | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | genre of the film Facing Sudan | False | [] | documentary film | [['d2s0']] |
| u2 | genre of the film Seal Island | False | [] | documentary film | [['d6s0'], ['d6s1']] |
| u3 | genre of movie that Facing Sudan and Seal Island both belong to | True | ['u1', 'u2'] | documentary film | [[]] |

### Source documents (reference only)

**d1: Prime Seal Island**

- [d1s0] Prime Seal Island is a long island, with a high central ridge and an area of 1220 ha, in south-eastern Australia.
- [d1s1]  It is part of Tasmania’s Prime Seal Island Group, lying in eastern Bass Strait west of Flinders in the Furneaux Group.
- [d1s2]  Geologically, it is limestone overlying granite and has notable karst features, including caves.
- [d1s3]  It is leased for farming and is extensively grazed by sheep and cattle as well as the native Tasmanian pademelons.

**d2: Facing Sudan**

- [d2s0] Facing Sudan is a documentary film released in 2007.
- [d2s1]  It chronicles the situation in Sudan from independence in 1956, through civil war and the current crisis in Darfur.
- [d2s2]  The narrative of Sudan is told through the eyes of activists from various segments of American society.
- [d2s3]  Brian Burns—a young custodian who traveled to South Sudan in order to effect change there—supplies the arc in the film, and links the various stories together.

**d3: Seal Island, Anguilla**

- [d3s0] Seal Island is a small island off the northwest coast of Anguilla.
- [d3s1]  It is located some two kilometres to the west of the Prickly Pear Cays at 18° 16' N, 63° 9' W, and lies at the centre of the Seal island Reef System Marine Park.
- [d3s2]  The area is popular with scuba divers.

**d4: Duiker Island**

- [d4s0] Duiker Island or Duikereiland ("Afrikaans"), also known as Seal Island (not to be confused with the nearby Seal Island), is an island off Hout Bay near Cape Town South Africa.
- [d4s1]  It is 77 by 95 metres in size, with an area of about 0.4 hectare.

**d5: Althorpe Islands Conservation Park**

- [d5s0] Althorpe Islands Conservation Park is a protected area in the Australian state of South Australia occupying the Althorpe Islands, Haystack Island and Seal Island in Investigator Strait near the town of Stenhouse Bay.
- [d5s1]  The conservation park was proclaimed in 1972 following the enactment of the "National Parks and Wildlife Act 1972" with the protection initially applying to the Western Islets in the Althorpe Islands, Haystack Island and Seal Island with Althorpe Island itself was not added until 1997.
- [d5s2]  The purpose of the conservation park is ‘to protect important wildlife habitat, particularly for sea-bird populations’.
- [d5s3]  It is classified as an IUCN Category Ia protected area.

**d6: Seal Island (film)**

- [d6s0] Seal Island is a 1948 American documentary film directed by James Algar.
- [d6s1]  Produced by Walt Disney, it was the first installment of the "True-Life Adventures" series of nature documentaries.
- [d6s2]  It won an Academy Award in 1949 for Best Short Subject (Two-Reel).

**d7: Seal Islands (South Shetland Islands)**

- [d7s0] The Seal Islands (also known as Îles des Phoques, Islas Foca, Islotes Foca and Seal Rocks) are a group of small islands and rocky islets lying about 7 km north and north-west of Elephant Island, in the South Shetland Islands of Antarctica.
- [d7s1]  They extend east–west for about 5 km, and are separated from Elephant Island by Sealers Passage.
- [d7s2]  The group takes its name from the largest island, which Captain William Smith named Seal Island in 1820 because of the number of seals killed there.

**d8: Seal Island (Nova Scotia)**

- [d8s0] Seal Island (also known as Great Seal Island) is an island on the outermost extreme of Southwestern Nova Scotia, Canada, in the Municipality of the District of Argyle in Yarmouth County.
- [d8s1]  It is approximately 4.3 km long and 0.8 km wide and is surrounded on its east, south and west sides by dangerous shoals.
- [d8s2]  It is surrounded by the Atlantic Ocean and is the biggest of a group of five islands which extend north for 12 km .
- [d8s3]  It is the second southernmost point of land of Nova Scotia.
- [d8s4]  The southern tip of nearby Cape Sable Island is 250 m farther south than the southern tip of land on Seal Island.

**d9: West Island Conservation Park**

- [d9s0] West Island Conservation Park is a protected area occupying both West Island and Seal Island in coastal waters near Victor Harbor in South Australia.
- [d9s1]  The park was proclaimed in 1972 following the enactment of the "National Parks and Wildlife Act 1972" with the protection initially applying to West Island only which itself previously had reserve status under the "Fauna Conservation Act 1964-1965".
- [d9s2]  Seal Island was added to the park in 1979.
- [d9s3]  The purpose of the park is to protect the breeding populations of bird species present on both islands such as little penguins, silver gulls, crested terns, Caspian terns and fairy terns.
- [d9s4]  The conservation park is classified as an IUCN Category Ia protected area.

**d10: Criehaven, Maine**

- [d10s0] Criehaven is an alternative name for Ragged Island, an unorganized territory in Knox County, Maine, United States.
- [d10s1]  Criehaven was formerly a plantation including Ragged Island just south of Matinicus Isle in outer Penobscot Bay, plus Matinicus Rock to its southeast, and Seal Island, the location of Seal Island National Wildlife Refuge, to its northeast.
- [d10s2]  Criehaven surrendered its organization and reverted to an unorganized territory in 1925, but the name persists.

## 30. hotpotqa_5a7f47d05542992e7d278ce2 【保留新拆法｜重标人工标签】

原位置：`train` 第 150 题 · 全局第 150 题 · `sample_id: hotpotqa_5a7f47d05542992e7d278ce2`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-hotpotqa_5a7f47d05542992e7d278ce2"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 旧版按剧集→季→发行日期拆；新版按季（含剧情限定）→该季Region 1 DVD→日期拆。新描述仍保留剧情、季和Region 1，虽有冗余命名但目标未改变。
>
> **处理建议：** 保留新3单元。新u1应取 season 5，需联合剧情定位和所属季的证据（d1s2/d1s0），不能复制旧u1的 Rosebud；新u2标注该季Region 1 DVD对象，新u3标注其日期，两者依 d7s6 和相应上下文/依赖重标。
>
> **证据定位：** d1s2, d1s0, d7s6；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: When as the DVD box set of the simposon's season that included the episode that Mr. Burns starts to miss his childhood teddy bear released in region 1 ?

Note:

Type: bridge · fallback: False · SFT snapshots: 6

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | season of The Simpsons that includes the episode where Mr. Burns starts to miss his childhood teddy bear | False | () |
| u2 | DVD box set of {u1} released in region 1 | False | ('u1',) |
| u3 | release date of {u2} | True | ('u2',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | episode of The Simpsons in which Mr. Burns starts to miss his childhood teddy bear | False | [] | Rosebud | [['d1s2']] |
| u2 | season of The Simpsons that includes {u1} | False | ['u1'] | season 5 | [['d1s0'], ['d7s3']] |
| u3 | Region 1 release date of the DVD box set of The Simpsons {u2} | True | ['u2'] | December 21, 2004 | [['d7s6']] |

### Source documents (reference only)

**d1: Rosebud (The Simpsons)**

- [d1s0] "Rosebud" is the fourth episode of "The Simpsons"<nowiki>'</nowiki> fifth season.
- [d1s1]  It first aired on the Fox network in the United States on October 21, 1993.
- [d1s2]  The episode begins by showing how on the eve of his birthday, Mr. Burns starts to miss his childhood teddy bear Bobo.
- [d1s3]  The bear ends up in the hands of Maggie Simpson and Burns does everything in his power to get Bobo returned to him.

**d2: There Is a Season**

- [d2s0] There Is a Season is a four-CD and one DVD box set by the American rock band The Byrds that was released on September 26, 2006 by Columbia/Legacy.
- [d2s1]  It comprises 99 tracks and includes material from every one of the band's twelve studio albums, presented in roughly chronological order.
- [d2s2]  The bonus DVD features ten clips of the Byrds lip-synching their hits on television programs between 1965 and 1967.
- [d2s3]  Upon release, the box set failed to reach the "Billboard" 200 chart or the UK Albums Chart.
- [d2s4]  "There Is a Season" supplants the band's earlier box set, "The Byrds", which was released in October 1990.

**d3: The Simpsons (season 2)**

- [d3s0] "The Simpsons"' second season originally aired on the Fox network between October 11, 1990 and May 9, 1991, and contained 22 episodes, beginning with "Bart Gets an "F"".
- [d3s1]  Another episode, "Blood Feud", aired during the summer after the official season finale.
- [d3s2]  The executive producers for the second production season were Matt Groening, James L. Brooks, and Sam Simon, who had also been EPs for the previous season.
- [d3s3]  The DVD box set was released on August 6, 2002 in Region 1, July 8, 2002 in Region 2 and in September, 2002 in Region 4.
- [d3s4]  The episode "Homer vs. Lisa and the 8th Commandment" won the Primetime Emmy Award for Outstanding Animated Program (for Programming Less Than One Hour), and was also nominated in the "Outstanding Sound Mixing for a Comedy Series or a Special" category.

**d4: The Life Collection**

- [d4s0] The Life Collection is a 24-disc DVD box set of eight titles from David Attenborough's 'Life' series of BBC natural history programmes.
- [d4s1]  It was released in the UK on 5 December 2005 and has also been made available on Region 4 DVD in Australia and New Zealand.
- [d4s2]  The Region 4 DVD contains four fewer discs as "Life on Earth" is not included.
- [d4s3]  It has not yet been issued in Region 1 encoding for the US.

**d5: Family Guy (season 4)**

- [d5s0] The fourth season of the animated comedy series "Family Guy" aired on Fox from May 1, 2005, to May 21, 2006, and consisted of thirty episodes, making it the longest season to date.
- [d5s1]  The first half of the season is included within the volume 3 DVD box set, which was released on November 29, 2005, and the second half is included within the volume 4 DVD box set, which was released on November 14, 2006.
- [d5s2]  Volume 4 was split into seasons 4 and 5 in regions outside the United States, leading to confusion over season numbers between U.S., Australian, and UK consumers.
- [d5s3]  The last three episodes of season 4 were the basis for the movie known as "", and are edited for content; Fox does not include these episodes in the official episode count.

**d6: American Dad! (season 6)**

- [d6s0] "American Dad!
- [d6s1] "<nowiki>'s</nowiki> sixth season premiered on Fox on September 27, 2009.
- [d6s2]  The season consists of nine episodes from production line four (4AJNxx) and nine from production line five (5AJNxx).
- [d6s3]  The entire season was released in the Volume Six DVD box set on April 19, 2011 in Region 1; on June 27, 2011 in Region 2; and July 13, 2011 and Region 4.
- [d6s4]  The season also marked the series move to airing in 16:9 high definition on January 3, 2010 with the episode "Don't Look a Smith Horse in the Mouth".

**d7: The Simpsons (season 5)**

- [d7s0] "The Simpsons"' fifth season originally aired on the Fox network between September 30, 1993 and May 19, 1994.
- [d7s1]  The showrunner for the fifth production season was David Mirkin who executive produced 20 episodes.
- [d7s2]  Al Jean and Mike Reiss executive produced the remaining two, which were both hold overs that were produced for the previous season.
- [d7s3]  The season contains some of the series' most acclaimed episodes, including "Cape Feare" and "Rosebud".
- [d7s4]  It also includes the 100th episode, "Sweet Seymour Skinner's Baadasssss Song".
- [d7s5]  The season was nominated for two Primetime Emmy Awards and won an Annie Award for Best Animated Television Program as well as an Environmental Media Award and a Genesis Award.
- [d7s6]  The DVD box set was released in Region 1 on December 21, 2004, Region 2 on March 21, 2005, and Region 4 on March 23, 2005.

**d8: List of Pani Poni Dash! episodes**

- [d8s0] This article lists the episodes from the anime series "Pani Poni Dash!
- [d8s1] " which aired in Japan on TV Tokyo between July 3, 2005 and December 25, 2005.
- [d8s2]  Each episode ends with a still image drawn by Japanese illustrators of anime, manga, and visual novels; these are listed below as endcards.
- [d8s3]  The anime has since been licensed by United States based company Funimation Entertainment in North America and ADV Films in the United Kingdom.
- [d8s4]  King Records subsidiary Starchild has the video and music rights for the anime.
- [d8s5]  A special OVA was released with DVD box set containing the anime series, on April 15, 2009.
- [d8s6]  Funimation released a complete DVD box set on March 10, 2009.
- [d8s7]  On October 26, 2010, Funimation re-released the complete series as a part of their Super Amazing Value Edition line-up.

**d9: Devil May Hare**

- [d9s0] Devil May Hare is a 1954 Warner Bros. "Looney Tunes" cartoon was released on June 19, 1954.
- [d9s1]  This theatrical cartoon was directed by Robert McKimson and starred Mel Blanc playing the voices of Bugs Bunny, the Tasmanian Devil, and the turtle.
- [d9s2]  This short is featured on the "" DVD box set, as well as the "" DVD box set.
- [d9s3]  It also appeared in the "" Blu-ray box set alongside "Bedevilled Rabbit", "Ducking the Devil", "Bill of Hare", and "Dr. Devil and Mr. Hare".

**d10: The Simpsons (season 7)**

- [d10s0] "The Simpsons"' seventh season originally aired on the Fox network between September 17, 1995 and May 19, 1996.
- [d10s1]  The show runners for the seventh production season were Bill Oakley and Josh Weinstein who would executive produce 21 episodes this season.
- [d10s2]  David Mirkin executive produced the remaining four, including two hold overs that were produced for the previous season.
- [d10s3]  The season was nominated for two Primetime Emmy Awards, including Outstanding Animated Program and won an Annie Award for Best Animated Television Program.
- [d10s4]  The DVD box set was released in Region 1 December 13, 2005, Region 2 January 30, 2006 and Region 4 on March 22, 2006.
- [d10s5]  The set was released in two different forms: a Marge-shaped box and also a standard rectangular-shaped box in which the theme is a movie premiere.
