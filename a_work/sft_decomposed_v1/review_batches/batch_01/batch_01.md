# batch_01：人工审查（30 题）

全局题号 1–30；train 30 题 / dev 0 题。原训练/验证归属保持不变。

[返回分配索引](../README.md) · [完整对比报告](../../comparison_human.md)

**原则：新旧单元都合理时保留拆题器拆法，人工监督向新单元对齐。** 未标记的题目也需要核对答案和证据。现有标记是 AI 辅助审阅意见，不是人工验收结论。

审查人：________　完成日期：________

## 1. 2wikimultihopqa_015ccd41087711ebbd67ac1f6bf848b6 【保留新拆法｜重标人工标签】

原位置：`train` 第 1 题 · 全局第 1 题 · `sample_id: 2wikimultihopqa_015ccd41087711ebbd67ac1f6bf848b6`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_015ccd41087711ebbd67ac1f6bf848b6"></a>

> **审阅结论：保留新拆法｜重标人工标签**
>
> **差异与原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。
>
> **处理建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。
>
> **证据定位：** d3s0, d3s1, d6s0, d4s0, d1s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Are director of film The Enigma Of The Folies-Bergere and director of film Deep Soul (Film) from the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of director of The Enigma Of The Folies-Bergere | False | () |
| u2 | country of director of Deep Soul (Film) | False | () |
| u3 | whether directors are from the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of The Enigma of the Folies-Bergere | False | [] | Jean Mitry | [['d3s0', 'd3s1']] |
| u2 | nationality of {u1} | False | ['u1'] | French | [['d6s0']] |
| u3 | director of Deep Soul (film) | False | [] | Pantelis Voulgaris | [['d4s0']] |
| u4 | nationality of {u3} | False | ['u3'] | Greek | [['d1s0']] |
| u5 | whether the directors of The Enigma of the Folies-Bergere and Deep Soul (film) are from the same country | True | ['u2', 'u4'] | no | [[]] |

### Source documents (reference only)

**d1: Pantelis Voulgaris**

- [d1s0] Pantelis Voulgaris( born 23 October 1940) is a Greek film director and screenwriter.
- [d1s1] His first feature film" To proxenio tis Annas" in 1972 won the first prize in Thessaloniki International Film Festival.
- [d1s2] His 1989 film" The Striker with Number 9" was entered into the 39th Berlin International Film Festival.
- [d1s3] Two years later, his film" Quiet Days in August" was entered into the 41st Berlin International Film Festival.
- [d1s4] In 2005 his film" Brides" was entered into the 27th Moscow International Film Festival.

**d2: Jason Moore (director)**

- [d2s0] Jason Moore( born October 22, 1970) is an American director of film, theatre and television.

**d3: The Enigma of the Folies-Bergere**

- [d3s0] The Enigma of the Folies-Bergere (French:
- [d3s1] Enigme aux Folies-Bergère) is a 1959 French crime film directed by Jean Mitry and starring Bella Darvi, Frank Villard and Dora Doll.
- [d3s2] The police investigate a series of murders at the Folies-Bergère.

**d4: Deep Soul (film)**

- [d4s0] Deep Soul is a 2009 Greek drama film directed by Pantelis Voulgaris, on the 1946– 49 Greek Civil War.

**d5: Brian Johnson (special effects artist)**

- [d5s0] Brian Johnson( born 1939 or 1940) is a British designer and director of film and television special effects.

**d6: Jean Mitry**

- [d6s0] Jean Mitry (7 November 1904, Soissons, Aisne – 18 January 1988, La Garenne-Colombes) was a French film theorist, critic and filmmaker, a co-founder of France's first film society, and, in 1938, of the Cinémathèque Française.

**d7: Peter Levin**

- [d7s0] Peter Levin is an American director of film, television and theatre.

**d8: Ian Barry (director)**

- [d8s0] Ian Barry is an Australian director of film and TV.

**d9: Hanro Smitsman**

- [d9s0] Hanro Smitsman, born in 1967 in Breda( Netherlands), is a writer and director of film and television.

**d10: Ben Cura**

- [d10s0] Ben Cura( born 30 September 1988) is a British- Argentine actor and director of film, television and theatre.

## 2. 2wikimultihopqa_057dd7de0bdd11eba7f7acde48001122

原位置：`train` 第 2 题 · 全局第 2 题 · `sample_id: 2wikimultihopqa_057dd7de0bdd11eba7f7acde48001122`

Question: Where was the director of film Two Against The World (1936 Film) born?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of Two Against The World (1936 Film) | False | () |
| u2 | birthplace of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Two Against the World (1936 film) | False | [] | William C. McGann | [['d10s0']] |
| u2 | place of birth of {u1} | True | ['u1'] | Pittsburgh, Pennsylvania | [['d5s2']] |

### Source documents (reference only)

**d1: Peter Levin**

- [d1s0] Peter Levin is an American director of film, television and theatre.

**d2: Olav Aaraas**

- [d2s0] Olav Aaraas( born 10 July 1950) is a Norwegian historian and museum director.
- [d2s1] He was born in Fredrikstad.
- [d2s2] From 1982 to 1993 he was the director of Sogn Folk Museum, from 1993 to 2010 he was the director of Maihaugen and from 2001 he has been the director of the Norwegian Museum of Cultural History.
- [d2s3] In 2010 he was decorated with the Royal Norwegian Order of St. Olav.

**d3: Two Men in Town (1973 film)**

- [d3s0] Two Men in Town( a.k.a." Two Against the Law") is a 1973 Franco- Italian film directed by José Giovanni.
- [d3s1] The film was remade in 2014.

**d4: Ian Barry (director)**

- [d4s0] Ian Barry is an Australian director of film and TV.

**d5: William C. McGann**

- [d5s0] William C. McGann( April 15, 1893 – November 15, 1977) was an American film director.
- [d5s1] He directed 52 films between 1930 and 1942.
- [d5s2] He was born in Pittsburgh, Pennsylvania and died in Los Angeles, California.

**d6: Jesse E. Hobson**

- [d6s0] Jesse Edward Hobson( May 2, 1911 – November 5, 1970) was the director of SRI International from 1947 to 1955.
- [d6s1] Prior to SRI, he was the director of the Armour Research Foundation.

**d7: Dana Blankstein**

- [d7s0] Dana Blankstein- Cohen( born March 3, 1981) is the director of the Israeli Academy of Film and Television.
- [d7s1] She is a film director, and an Israeli culture entrepreneur.

**d8: Brian Kennedy (gallery director)**

- [d8s0] Brian Patrick Kennedy( born 5 November 1961) is an Irish- born art museum director who has worked in Ireland and Australia, and now lives and works in the United States.
- [d8s1] He is currently the director of the Peabody Essex Museum.
- [d8s2] He was the director of the Toledo Museum of Art in Ohio from 2010 to 2019.
- [d8s3] He was the director of the Hood Museum of Art from 2005 to 2010, and the National Gallery of Australia( Canberra) from 1997- 2004.

**d9: S. N. Mathur**

- [d9s0] S.N. Mathur was the Director of the Indian Intelligence Bureau between September 1975 and February 1980.
- [d9s1] He was also the Director General of Police in Punjab.

**d10: Two Against the World (1936 film)**

- [d10s0] Two Against the World, also known as One Fatal Hour, is a 1936 drama film directed by William C. McGann and starring Humphrey Bogart, Beverly Roberts, and Linda Perry.
- [d10s1] The film is based on the play "Five Star Final" by Louis Weitzenkorn and is a remake of the film "Five Star Final" starring Edward G. Robinson, although the setting has been moved from a newspaper office to a radio station which revives the memory of a twenty-year-old murder case, resulting in tragic consequences.

## 3. 2wikimultihopqa_085f772608c411ebbd8eac1f6bf848b6

原位置：`train` 第 3 题 · 全局第 3 题 · `sample_id: 2wikimultihopqa_085f772608c411ebbd8eac1f6bf848b6`

Question: Were K. Alex Müller and Christian Rocca of the same nationality?

Note:

Type: comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | nationality of K. Alex Müller | False | () |
| u2 | nationality of Christian Rocca | False | () |
| u3 | whether K. Alex Müller and Christian Rocca were of the same nationality | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | nationality of K. Alex Müller | False | [] | Swiss | [['d5s0']] |
| u2 | nationality of Christian Rocca | False | [] | Italian | [['d8s0']] |
| u3 | whether K. Alex Müller and Christian Rocca are of the same nationality | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: John Davidson (British writer)**

- [d1s0] John Davidson( born 1944) is an English writer on mysticism and Christian origins.

**d2: Michael Hulse**

- [d2s0] Michael Hulse( born 1955) is an English translator, critic and poet, notable especially for his translations of German novels by W. G. Sebald, Herta Müller, and Elfriede Jelinek.

**d3: Georg Bednorz**

- [d3s0] Johannes Georg Bednorz( born 16 May 1950) is a German physicist who, together with K. Alex Müller, discovered high- temperature superconductivity in ceramics, for which they shared the 1987 Nobel Prize in Physics.

**d4: Marinus of Caesarea**

- [d4s0] Marinus of Caesarea was a Roman soldier and a Christian martyr.

**d5: K. Alex Müller**

- [d5s0] Karl Alexander Müller( born April 20, 1927) is a Swiss physicist and Nobel laureate.
- [d5s1] He received the Nobel Prize in Physics in 1987 with Georg Bednorz for their work in superconductivity in ceramic materials.

**d6: Alex Craig**

- [d6s0] Alex Craig( born 2 April 1886) was a football player who played for Rangers, Greenock Morton and Ireland.
- [d6s1] He is one of only four players born in what is now the Republic of Ireland to play for Rangers.
- [d6s2] The others were Alex Stevenson, Jon Daly and James Lowry McAuley.

**d7: John Thornton (philanthropist)**

- [d7s0] John Thornton( 1720–1790) was a British merchant and Christian philanthropist.

**d8: Christian Rocca**

- [d8s0] Christian Rocca( born 23 January 1968) is an Italian newspaper journalist and blogger.

**d9: Tainá Müller**

- [d9s0] Tainá Müller( born June 1, 1982) is a Brazilian actress.
- [d9s1] She is the oldest of three sisters, actress Taiure Müller and MTV VJ Titi Müller.

**d10: Gervasio Gatti**

- [d10s0] Gervasio Gatti( c. 1550 in either Cremona, Vercelli or Pavia – c. 1631) was an Italian painter during the late- Renaissance, active in Parma, Piacenza, and Cremona.
- [d10s1] He was also known as Il Soiaro( or" Sojaro")
- [d10s2] Gatti trained with his uncle Bernardino Gatti.
- [d10s3] He helped decorate the salons in the Rocca of San Secondo Parmense.
- [d10s4] He also studied with Correggio.

## 4. 2wikimultihopqa_08d7167e084b11ebbd56ac1f6bf848b6

原位置：`train` 第 4 题 · 全局第 4 题 · `sample_id: 2wikimultihopqa_08d7167e084b11ebbd56ac1f6bf848b6`

Question: Which film has the director who was born earlier, They Came To Cordura or The Unknown Known?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of They Came To Cordura | False | () |
| u2 | birth date of {u1} | False | ('u1',) |
| u3 | director of The Unknown Known | False | () |
| u4 | birth date of {u3} | False | ('u3',) |
| u5 | which film's director was born earlier | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film They Came to Cordura | False | [] | Robert Rossen | [['d4s0']] |
| u2 | date of birth of {u1} | False | ['u1'] | March 16, 1908 | [['d8s0']] |
| u3 | director of film The Unknown Known | False | [] | Errol Morris | [['d1s0']] |
| u4 | date of birth of {u3} | False | ['u3'] | February 5, 1948 | [['d2s0']] |
| u5 | which of They Came to Cordura and The Unknown Known has the director born earlier | True | ['u2', 'u4'] | They Came to Cordura | [[]] |

### Source documents (reference only)

**d1: The Unknown Known**

- [d1s0] The Unknown Known( also known as The Unknown Known: The Life and Times of Donald Rumsfeld) is a 2013 American documentary film about the political career of former U.S. Secretary of Defense and congressman Donald Rumsfeld, directed by Academy Award winning documentarian and filmmaker Errol Morris.
- [d1s1] The film is a summary of 33 hours of interviews that Morris conducted with Rumsfeld over eleven separate sessions during visits to Newton, Massachusetts.
- [d1s2] It is dedicated to the memory of Roger Ebert.
- [d1s3] The film was released on April 4, 2014, by Radius- TWC.

**d2: Errol Morris**

- [d2s0] Errol Mark Morris( born February 5, 1948) is an American film director primarily of documentaries examining and investigating, among other things, authorities and eccentrics.
- [d2s1] His 1988 documentary" The Thin Blue Line" is cited among the best and most influential documentaries ever made.
- [d2s2] In 2003, his documentary film" The Fog of War: Eleven Lessons from the Life of Robert S. McNamara" won the Oscar for Best Documentary Feature.

**d3: Ben Palmer**

- [d3s0] Ben Palmer is a British film and television director who is known for being the director of" Bo' Selecta" and" The Inbetweeners".

**d4: They Came to Cordura**

- [d4s0] They Came to Cordura is a 1959 American CinemaScope Eastmancolor Western film co-written and directed by Robert Rossen and starring Gary Cooper, Rita Hayworth, Van Heflin and Tab Hunter.
- [d4s1] It was based on a 1958 novel by Glendon Swarthout.

**d5: Edward Yates**

- [d5s0] Edward J. Yates( September 16, 1918 – June 2, 2006) was an American television director who was the director of the ABC television program" American Bandstand" from 1952 until 1969.

**d6: Abhishek Saxena**

- [d6s0] Abhishek Saxena is an Indian Bollywood and Punjabi film director who directed the movie Phullu.
- [d6s1] The Phullu movie was released in theaters on 16 June 2017, in which film Sharib Hashmi is the lead role.
- [d6s2] Apart from these, he has also directed Patiala Dreamz, this is a Punjabi film.
- [d6s3] This film was screened in cinemas in 2014.

**d7: Rumbi Katedza**

- [d7s0] Rumbi Katedza is a Zimbabwean Film Producer and Director who was born on 17 January 1974.

**d8: Robert Rossen**

- [d8s0] Robert Rossen (March 16, 1908 – February 18, 1966) was an American screenwriter, film director, and producer whose film career spanned almost three decades.
- [d8s1] His 1949 film "All the King's Men" won Oscars for Best Picture, Best Actor and Best Supporting Actress, while Rossen was nominated for an Oscar as Best Director.
- [d8s2] He won the Golden Globe for Best Director and the film won the Golden Globe Award for Best Picture.
- [d8s3] In 1961, he directed "The Hustler", which was nominated for nine Oscars and won two.
- [d8s4] After directing and writing for the stage in New York, Rossen moved to Hollywood in 1937.
- [d8s5] From there, he worked as a screenwriter for Warner Bros. until 1941, and then interrupted his career to serve until 1944 as the chairman of the Hollywood Writers Mobilization, a body to organize writers for the effort in World War II.
- [d8s6] In 1945, he joined a picket line against Warner Bros.
- [d8s7] After making one film for Hal B. Wallis's newly formed production company, Rossen made one for Columbia Pictures, another for Wallis and most of his later films for his own companies, usually in collaboration with Columbia.
- [d8s8] Rossen was a member of the American Communist Party from 1937 to about 1947, and believed the Party was "dedicated to social causes of the sort that we as poor Jews from New York were interested in."
- [d8s9] He ended all relations with the Party in 1949.
- [d8s10] Rossen was twice called before the House Un-American Activities Committee (HUAC), in 1951 and in 1953.
- [d8s11] He exercised his Fifth Amendment rights at his first appearance, refusing to state whether he had ever been a Communist.
- [d8s12] As a result, he found himself blacklisted by Hollywood studios as well as unable to renew his passport.
- [d8s13] At his second appearance he named 57 people as current or former Communists and his blacklisting ended.
- [d8s14] In order to repair finances he produced his next film, "Mambo", in Italy in 1954.
- [d8s15] While "The Hustler" in 1961 was a great success, conflicts on the set of "Lilith" so disillusioned him that it was his last film.

**d9: Dick Power**

- [d9s0] Richard John Power( 13 December 1903 – unknown), known as Dick Power, was a Welsh professional heavyweight boxer.
- [d9s1] Born in Crumlin in Monmouthshire, Power became the Welsh heavyweight champion in 1926.

**d10: Hassan Zee**

- [d10s0] Hassan Zee is a Pakistani- American film director who was born in Chakwal, Pakistan.

## 5. 2wikimultihopqa_0ae4bb72086111ebbd5dac1f6bf848b6 【需改：生成拆解】

原位置：`train` 第 5 题 · 全局第 5 题 · `sample_id: 2wikimultihopqa_0ae4bb72086111ebbd5dac1f6bf848b6`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_0ae4bb72086111ebbd5dac1f6bf848b6"></a>

> **审阅结论：需改：生成拆解**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 单元本身是两个已点名对象的事实加一个比较/共同属性结论，没有寻找未知中间实体的桥接步骤，但 question_type 被写成 bridge_comparison。
>
> **处理建议：** 只将 question_type 改为 comparison，保留当前单元关系；这属于题型元数据错误，不应为凑题型增加桥接单元。
>
> **证据定位：** d9s0, d7s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Who died first, Maude Fealy or Lars Gustafsson?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 7

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | death date of Maude Fealy | False | () |
| u2 | death date of Lars Gustafsson | False | () |
| u3 | who died first | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | date of death of Maude Fealy | False | [] | November 9, 1971 | [['d9s0']] |
| u2 | date of death of Lars Gustafsson | False | [] | 3 April 2016 | [['d7s0']] |
| u3 | who died first, Maude Fealy or Lars Gustafsson | True | ['u1', 'u2'] | Maude Fealy | [[]] |

### Source documents (reference only)

**d1: Lars Gustafsson (wrestler)**

- [d1s0] Lars Gustafsson( born 21 April 1966) is a Swedish wrestler.
- [d1s1] He competed in the men's freestyle 74 kg at the 1988 Summer Olympics.

**d2: Lars H. Gustafsson**

- [d2s0] Lars H. Gustafsson was born on May 10, 1942 in Uppsala.
- [d2s1] His full name is Lars Hugo Elias Lindkvist Gustafsson.
- [d2s2] He is a pediatrician, author, and social commentator in Sweden.

**d3: Verena Reichel**

- [d3s0] Verena Reichel( born in Grimma, Saxony, 21 March 1945) is a German literary translator.
- [d3s1] Bilingual from childhood, she later studied Scandinavian literature, German literature, and theater.
- [d3s2] Since 1972, she has worked as a freelance translator from Swedish, Norwegian, and Danish.
- [d3s3] She has published more than 60 volumes of translations from Swedish, including three by Ingmar Bergman, six by Henning Mankell, and four each by Märta Tikkanen and Torgny Lindgren.
- [d3s4] Especially notable are her translations of Lars Gustafsson: eighteen novels, three co-authored works, and poems gathered in" Ein Vormittag in Schweden"( 1998; co-translators were Hans Magnus Enzensberger and Hanns Grössel; Reichel edited the volume and wrote an afterword) and in" Jahrhunderte und Minuten"( 2009; with the same co-translators).
- [d3s5] Verena Reichel is a member of the Association of German- speaking Translators of Literary and Scientific Works( Verband deutschsprachiger Übersetzer literarischer und wissenschaftlicher Werke, VdÜ) within the Association of German Writers( Verband Deutscher Schriftsteller).
- [d3s6] Among her awards are: the 1987 Translation Prize of the Swedish Academy, the Helmut M. Braem Prize in 1992, the Petrarca Prize in 1995, also in 1995 the Nossack Academy Award of the Academy of Sciences and Literature in Mainz( together with Lars Gustafsson), in 1998 the Jane Scatcherd Prize, and in 2008 the Johann Heinrich Voss Prize for translation.
- [d3s7] The Petrarca Prize was awarded in particular for Reichel's translations of novels by Lars Gustafsson and the poetry of Katarina Frostenson, Lars Gustafsson, Johannes Edfelt, and Madeleine Gustafsson.

**d4: Lars Gustafsson Vasa**

- [d4s0] Lars Gustafsson Vasa( born 1 September 1586 in Silesia died 1660)- fictional son of Prince Gustav of Sweden with his supposed wife Brita Karth.
- [d4s1] According to the legend, in 1621 he married Brita Törnros.
- [d4s2] They were earlier thought to be the parents of Lars Eldstjerna and Samuel Stjerneld, founders of the Swedish noble families of Eldstierna and Stierneld respectively.
- [d4s3] Modern scholars have however refuted this myth and Lars and Samuel are nowadays identified as the sons of a vogt at Händelö named Lars( died 1657), whose possible patronym might have been Björnsson.

**d5: Sergio Badilla Castillo**

- [d5s0] Sergio Badilla Castillo( born November 30, 1947 in Valparaiso, Chile) is a Chilean poet and the founder of poetic transrealism in contemporary poetry.
- [d5s1] He is considered the Latin American poet with the broadest Nordic influence, from the Finnish poets, Edith Södergran, Elmer Diktonius, Paavo Haavikko, Pentti Saarikoski and the Swedes Gunnar Ekelöf, Tomas Tranströmer and Lars Gustafsson.

**d6: Lars Gustafsson (politician)**

- [d6s0] Lars Gustafsson( born 1951) is a Swedish Christian democratic politician and member of the Riksdag since 1998.

**d7: Lars Gustafsson**

- [d7s0] Lars Erik Einar Gustavsson( 17 May 1936 – 3 April 2016) was a Swedish poet, novelist, and scholar.

**d8: Samuel Larsson Stjerneld**

- [d8s0] Samuel Larsson Stjerneld (1637–1716) was son of Lars Gustafsson Vasa and Brita Törnros.
- [d8s1] In unknown year Samuel espoused an Englishwoman, Brita Ratskin (her mother a Sydney), a learned woman, who spoke Latin, understood Greek, and died in childbirth.
- [d8s2] They had daughter Catharina Stjerneld.
- [d8s3] In 1682 he married Margaretha Bethzen, daughter of Dutch merchant Mathias.

**d9: Maude Fealy**

- [d9s0] Maude Fealy( born Maude Mary Hawk, March 4, 1883 – November 9, 1971) was an American stage and silent film actress whose career survived into the sound era.

**d10: Hélène Grenier**

- [d10s0] Hélène Grenier was a Canadian librarian born in 1900 who died in 1992.

## 6. 2wikimultihopqa_0b4d4cb20bdd11eba7f7acde48001122

原位置：`train` 第 6 题 · 全局第 6 题 · `sample_id: 2wikimultihopqa_0b4d4cb20bdd11eba7f7acde48001122`

Question: Where was the place of death of the director of film Under The Cherry Moon?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of film Under The Cherry Moon | False | () |
| u2 | place of death of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Under the Cherry Moon | False | [] | Prince | [['d1s0']] |
| u2 | place of death of {u1} | True | ['u1'] | Chanhassen, Minnesota | [['d10s19']] |

### Source documents (reference only)

**d1: Under the Cherry Moon**

- [d1s0] Under the Cherry Moon is a 1986 American musical film directed by and starring Prince in his directorial debut.
- [d1s1] The film also stars former The Time member Jerome Benton, Steven Berkoff, Kristin Scott Thomas( in her feature film debut), and Francesca Annis.
- [d1s2] The film was a critical and commercial failure, winning five Golden Raspberry Awards, including Worst Picture, tying with" Howard the Duck".
- [d1s3] But, despite that, its soundtrack album, entitled" Parade", went platinum, selling over a million copies.

**d2: Olav Aaraas**

- [d2s0] Olav Aaraas( born 10 July 1950) is a Norwegian historian and museum director.
- [d2s1] He was born in Fredrikstad.
- [d2s2] From 1982 to 1993 he was the director of Sogn Folk Museum, from 1993 to 2010 he was the director of Maihaugen and from 2001 he has been the director of the Norwegian Museum of Cultural History.
- [d2s3] In 2010 he was decorated with the Royal Norwegian Order of St. Olav.

**d3: Dana Blankstein**

- [d3s0] Dana Blankstein- Cohen( born March 3, 1981) is the director of the Israeli Academy of Film and Television.
- [d3s1] She is a film director, and an Israeli culture entrepreneur.

**d4: S. N. Mathur**

- [d4s0] S.N. Mathur was the Director of the Indian Intelligence Bureau between September 1975 and February 1980.
- [d4s1] He was also the Director General of Police in Punjab.

**d5: Ian Barry (director)**

- [d5s0] Ian Barry is an Australian director of film and TV.

**d6: Jesse E. Hobson**

- [d6s0] Jesse Edward Hobson( May 2, 1911 – November 5, 1970) was the director of SRI International from 1947 to 1955.
- [d6s1] Prior to SRI, he was the director of the Armour Research Foundation.

**d7: Mountains (Prince song)**

- [d7s0] " Mountains" is a 1986 song by Prince and The Revolution, from the album" Parade", the soundtrack to the film" Under the Cherry Moon".
- [d7s1] It was written by The Revolution members Wendy& Lisa together with Prince.
- [d7s2] The extended 12" single version of the song runs nearly ten minutes.
- [d7s3] It reached number 23 in the US but only 45 in the UK.
- [d7s4] The B-side was the instrumental" Alexa de Paris", one of the few tracks from this project featuring a guitar solo.
- [d7s5] Both songs appear in the film" Under the Cherry Moon", with the video for" Mountains" playing as the credits roll.
- [d7s6] The version shown on MTV to promote the single was in color as opposed to the film's black- and- white version.
- [d7s7] " Mountains" was often performed in his live concerts.
- [d7s8] A music video, directed by Prince was released in April 1986.

**d8: Brian Kennedy (gallery director)**

- [d8s0] Brian Patrick Kennedy( born 5 November 1961) is an Irish- born art museum director who has worked in Ireland and Australia, and now lives and works in the United States.
- [d8s1] He is currently the director of the Peabody Essex Museum.
- [d8s2] He was the director of the Toledo Museum of Art in Ohio from 2010 to 2019.
- [d8s3] He was the director of the Hood Museum of Art from 2005 to 2010, and the National Gallery of Australia( Canberra) from 1997- 2004.

**d9: Peter Levin**

- [d9s0] Peter Levin is an American director of film, television and theatre.

**d10: Prince (musician)**

- [d10s0] Prince Rogers Nelson (June 7, 1958 – April 21, 2016) was an American singer, songwriter, musician, record producer, dancer, actor, and filmmaker.
- [d10s1] A guitar virtuoso known for his genre-crossing work, falsetto singing voice and flamboyant stage appearances, Prince is regarded as one of the greatest musicians of all time.
- [d10s2] His innovative music integrated a wide variety of styles, including funk, rock, R&B, new wave, soul, psychedelia, and pop.
- [d10s3] Prince pioneered the late 1970s Minneapolis sound, a funk rock subgenre drawing from synth-pop and new wave.
- [d10s4] Born and raised in Minneapolis, Minnesota, Prince developed an interest in music as a young child and wrote his first song, "Funk Machine", at the age of seven.
- [d10s5] He signed a recording contract with Warner Bros. Records at the age of 19, and released his debut album "
- [d10s6] For You" in 1978.
- [d10s7] Followed with his next four albums — "Prince" (1979), "Dirty Mind" (1980), "Controversy" (1981), and "1999" (1982)—Prince gained critical success, prominently showcasing his explicit lyrics as well as blending of funk, dance, and rock music.
- [d10s8] In 1984, he began referring to his backup band as The Revolution and released "Purple Rain", the soundtrack album to his successful film debut of the same name.
- [d10s9] It quickly became his most critically and commercially successful record, spending 24 consecutive weeks atop the "Billboard" 200.
- [d10s10] The film also won the Academy Award for Best Original Song Score, the last to receive the award.
- [d10s11] Following the disbandment of The Revolution, Prince released the critically acclaimed double album "Sign o' the Times" (1987).
- [d10s12] He released three more solo albums before debuting The New Power Generation band in 1991.
- [d10s13] In 1993, in the midst of a contractual dispute with Warner Bros., Prince changed his stage name to an unpronounceable symbol , also known as the "Love Symbol", and began releasing new albums at a faster rate in order to quickly meet a contractually required quota and therefore release himself from further obligations to the record label.
- [d10s14] He released five records between 1994 and 1996 before he signed with Arista Records in 1998.
- [d10s15] In 2000, he began referring to himself as "Prince" again.
- [d10s16] He subsequently released 16 albums, including "Musicology" (2004), which was his most successful album of the 2000s.
- [d10s17] His final album, "Hit n
- [d10s18] Run Phase Two", was first released on the Tidal streaming service in 2015.
- [d10s19] In April 2016, at the age of 57, Prince died of an accidental fentanyl overdose at his Paisley Park home and recording studio in Chanhassen, Minnesota.
- [d10s20] Prince sold over 130 million records worldwide, making him one of the best-selling music artists of all time.
- [d10s21] He won seven Grammy Awards, seven Brit Awards, six American Music Awards, four MTV Video Music Awards, an Academy Award, and a Golden Globe Award.
- [d10s22] He was also honored with special awards including the Grammy President's Merit Award, the American Music Award for Achievement and of Merit, and the "Billboard" Icon Award.
- [d10s23] He was inducted into the Rock and Roll Hall of Fame in 2004 and the Rhythm and Blues Music Hall of Fame in 2016.
- [d10s24] "
- [d10s25] Rolling Stone" ranked Prince at No. 27 on its list of the 100 Greatest Artists of All Time.

## 7. 2wikimultihopqa_11f7f17c0bdb11eba7f7acde48001122

原位置：`train` 第 7 题 · 全局第 7 题 · `sample_id: 2wikimultihopqa_11f7f17c0bdb11eba7f7acde48001122`

Question: What nationality is the director of film Higher Than A Kite?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of film Higher Than A Kite | False | () |
| u2 | nationality of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Higher Than a Kite | False | [] | Del Lord | [['d10s1']] |
| u2 | nationality of {u1} | True | ['u1'] | Canadian | [['d9s0']] |

### Source documents (reference only)

**d1: John Donatich**

- [d1s0] John Donatich is the Director of Yale University Press.

**d2: Dana Blankstein**

- [d2s0] Dana Blankstein- Cohen( born March 3, 1981) is the director of the Israeli Academy of Film and Television.
- [d2s1] She is a film director, and an Israeli culture entrepreneur.

**d3: Peter Levin**

- [d3s0] Peter Levin is an American director of film, television and theatre.

**d4: John Farrell (businessman)**

- [d4s0] John Farrell is the director of YouTube in Latin America.

**d5: Michael Govan**

- [d5s0] Michael Govan( born 1963) is the director of the Los Angeles County Museum of Art since 2006.
- [d5s1] Prior to this, Govan worked as the director of the Dia Art Foundation in New York City.

**d6: Ian Barry (director)**

- [d6s0] Ian Barry is an Australian director of film and TV.

**d7: Brian Kennedy (gallery director)**

- [d7s0] Brian Patrick Kennedy( born 5 November 1961) is an Irish- born art museum director who has worked in Ireland and Australia, and now lives and works in the United States.
- [d7s1] He is currently the director of the Peabody Essex Museum.
- [d7s2] He was the director of the Toledo Museum of Art in Ohio from 2010 to 2019.
- [d7s3] He was the director of the Hood Museum of Art from 2005 to 2010, and the National Gallery of Australia( Canberra) from 1997- 2004.

**d8: Olav Aaraas**

- [d8s0] Olav Aaraas( born 10 July 1950) is a Norwegian historian and museum director.
- [d8s1] He was born in Fredrikstad.
- [d8s2] From 1982 to 1993 he was the director of Sogn Folk Museum, from 1993 to 2010 he was the director of Maihaugen and from 2001 he has been the director of the Norwegian Museum of Cultural History.
- [d8s3] In 2010 he was decorated with the Royal Norwegian Order of St. Olav.

**d9: Del Lord**

- [d9s0] Delmar" Del" Lord( October 7, 1894 March 23, 1970) was a Canadian film director and actor best known as a director of Three Stooges films.

**d10: Higher Than a Kite**

- [d10s0] Higher
- [d10s1] Than a Kite is a 1943 short subject directed by Del Lord starring American slapstick comedy team The Three Stooges( Moe Howard, Larry Fine and Curly Howard).
- [d10s2] It is the 72nd entry in the series released by Columbia Pictures starring the comedians, who released 190 shorts for the studio between 1934 and 1959.

## 8. 2wikimultihopqa_137cbd01098c11ebbdb0ac1f6bf848b6

原位置：`train` 第 8 题 · 全局第 8 题 · `sample_id: 2wikimultihopqa_137cbd01098c11ebbdb0ac1f6bf848b6`

Question: Are both villages, Damvant and Gusheh-Ye Mohammad Malek, located in the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of Damvant | False | () |
| u2 | country of Gusheh-Ye Mohammad Malek | False | () |
| u3 | whether Damvant and Gusheh-Ye Mohammad Malek are in the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country where Damvant is located | False | [] | Switzerland | [['d1s0']] |
| u2 | country where Gusheh-ye Mohammad Malek is located | False | [] | Iran | [['d3s0']] |
| u3 | whether Damvant and Gusheh-ye Mohammad Malek are located in the same country | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Damvant**

- [d1s0] Damvant is a village and former municipality in the district of Porrentruy in the canton of Jura in Switzerland.
- [d1s1] Since 1 January 2009 it has been part of the new municipality Haute- Ajoie.

**d2: Gusheh-ye Olya, Markazi**

- [d2s0] Gusheh- ye Olya( also Romanized as Gūsheh- ye ‘ Olyā; also known as Gūsheh Bālā and Gūsheh- ye Bālā) is a village in Enaj Rural District, Qareh Chay District, Khondab County, Markazi Province, Iran.
- [d2s1] At the 2006 census, its population was 661, in 152 families.

**d3: Gusheh-ye Mohammad Malek**

- [d3s0] Gusheh- ye Mohammad Malek( also Romanized as Gūsheh- ye Moḩammad Mālek, Goosheh Mohammad Malek, and Gūsheh- ye Moḩammad -e Malek) is a village in Rostaq Rural District, in the Central District of Khomeyn County, Markazi Province, Iran.
- [d3s1] At the 2006 census, its population was 398, in 101 families.

**d4: Boneh-ye Mohammad Ali**

- [d4s0] Boneh- ye Mohammad Ali( also Romanized as Boneh- ye Moḩammad ʿ Alī) is a village in Chelo Rural District, Chelo District, Andika County, Khuzestan Province, Iran.
- [d4s1] At the 2006 census, its population was 29, in 5 families.

**d5: Gusheh-ye Kasavand**

- [d5s0] Gusheh- ye Kasavand( also Romanized as Gūsheh- ye Kasāvand; also known as Gūsheh) is a village in Kamazan -e Olya Rural District, Zand District, Malayer County, Hamadan Province, Iran.
- [d5s1] At the 2006 census, its population was 374, in 103 families.

**d6: Gusheh-ye Olya, Kohgiluyeh and Boyer-Ahmad**

- [d6s0] Gusheh- ye Olya( also Romanized as Gūsheh- ye ‘ Olyā; also known as Gūsheh and Gūsheh- ye Bālā) is a village in Poshteh- ye Zilayi Rural District, Sarfaryab District, Charam County, Kohgiluyeh and Boyer- Ahmad Province, Iran.
- [d6s1] At the 2006 census, its population was 113, in 19 families.

**d7: Gusheh-ye Sofla, Kohgiluyeh and Boyer-Ahmad**

- [d7s0] Gusheh- ye Sofla( also Romanized as Gūsheh- ye Soflá and Gūsheh -e Soflá; also known as Gūsheh) is a village in Poshteh- ye Zilayi Rural District, Sarfaryab District, Charam County, Kohgiluyeh and Boyer- Ahmad Province, Iran.
- [d7s1] At the 2006 census, its population was 118, in 21 families.

**d8: Kalateh-ye Mohammad Jan**

- [d8s0] Kalateh- ye Mohammad Jan( also Romanized as Kalāteh- ye Moḩammad Jān) is a village in Binalud Rural District, in the Central District of Nishapur County, Razavi Khorasan Province, Iran.
- [d8s1] At the 2006 census, its population was 202, in 60 families.

**d9: Gusheh-ye Pol**

- [d9s0] Gusheh- ye Pol( also Romanized as Gūsheh- ye Pol, Gūshehpal, and Gūsheh Pol) is a village in Dorud Rural District, in the Central District of Dorud County, Lorestan Province, Iran.
- [d9s1] At the 2006 census, its population was 397, in 90 families.

**d10: Kalateh-ye Mohammad Baqer**

- [d10s0] Kalateh- ye Mohammad Baqer( also Romanized as Kalāteh- ye Moḩammad Bāqer) is a village in Bizaki Rural District, Golbajar District, Chenaran County, Razavi Khorasan Province, Iran.
- [d10s1] At the 2006 census, its existence was noted, but its population was not reported.

## 9. 2wikimultihopqa_16a707100bb011ebab90acde48001122

原位置：`train` 第 9 题 · 全局第 9 题 · `sample_id: 2wikimultihopqa_16a707100bb011ebab90acde48001122`

Question: Who is the paternal grandfather of Princess Mangkubumi?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Princess Mangkubumi | False | () |
| u2 | father of {u1}, Princess Mangkubumi's paternal grandfather | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Princess Mangkubumi | False | [] | Hamengkubuwono X | [['d8s1']] |
| u2 | father of {u1}, Princess Mangkubumi's paternal grandfather | True | ['u1'] | Hamengkubuwono IX | [['d2s2']] |

### Source documents (reference only)

**d1: Lyon Cohen**

- [d1s0] Lyon Cohen( 1868–1937) was a Polish- born Canadian businessman and a philanthropist.
- [d1s1] He was the grandfather of singer/ poet Leonard Cohen.

**d2: Hamengkubuwono X**

- [d2s0] Sri Sultan Hamengkubuwono X (also spelled as Hamengkubuwana X, often abbreviated as HB X)
- [d2s1] (born BRM Herjuno Darpito, 2 April 1946 in Yogyakarta) is the Sultan of the historic Yogyakarta Sultanate in Indonesia, and is currently also the Governor of the modern Yogyakarta Special Region ("Daerah Istimewa Yogyakarta").
- [d2s2] Hamengkubuwono X succeeded his father, Hamengkubuwono IX as the Sultan of Yogyakarta when Hamengkubuwono IX died on 3 October 1988.
- [d2s3] Hamengkubuwono X was formally installed as Sultan on 7 March 1989.
- [d2s4] However, the position of the Governor of the Yogyakarta Special Region did not go to Hamengkubuwono X. Vice Governor Sri Paku Alam VIII, prince of the subordinate enclave of Paku Alaman within Yogyakarta was instead controversially elevated to the position of governor.
- [d2s5] This was in contrary to the agreement made at the independence of Indonesia in recognition of Hamengkubuwono IX's support and role in the Indonesian War of Independence.
- [d2s6] Under the agreement, the Yogyakarta Sultan holds the position of governor in the Yogyakarta Special Region, and the Paku Alam holds the position of vice governor.
- [d2s7] After the fall of the Suharto regime in May 1998, and following the death of Sri Paku Alam VIII on 11 September 1998, the central government required an election be held for the post of Yogyakarta Governor.
- [d2s8] Hamengkubuwono X was democratically elected as the Governor on 3 October 1998.
- [d2s9] On 30 August 2012, following a decade of talks between Yogyakarta and the central government, the national legislature of Indonesia formally enshrined in law the convention that the Sultan inherits the position of governor.

**d3: Kaya Alp**

- [d3s0] Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

**d4: Abd al-Muttalib**

- [d4s0] Abd al- Muttalib Shaybah ibn Hashim( c. 497 – 578) was the grandfather of Islamic prophet Muhammad.

**d5: Fujiwara no Nagara**

- [d5s0] , also known as Fujiwara no Nagayoshi, was a Japanese statesman, courtier and politician of the early Heian period.
- [d5s1] He was the grandfather of Emperor Yōzei.

**d6: Henry Bryant (naturalist)**

- [d6s0] Henry Bryant( May 12, 1820 – February 2, 1867) was an American physician and naturalist.
- [d6s1] He was the grandfather of Henry Bryant Bigelow.

**d7: Guillaume Wittouck**

- [d7s0] Guillaume Wittouck( 1749- 1829) was a Belgian lawyer and High Magistrate.
- [d7s1] He was the Grandfather of industrialist Paul Wittouck.

**d8: Princess Mangkubumi**

- [d8s0] Princess Mangkubumi
- [d8s1] (Javanese: ꦩꦁꦑꦸꦨꦸꦩꦶ) is the first child and daughter of Sri Sultan Hamengkubuwono X of Yogyakarta and his consort, Ratu Hemas.
- [d8s2] On 5 May 2015 she was proclaimed Crown Princess by her father.
- [d8s3] She married Prince Wironegoro, a businessman and philanthropist.

**d9: Prithvipati Shah**

- [d9s0] Prithvipati Shah( ?–1716) was the king of the Gorkha Kingdom in the Indian subcontinent, present- day Nepal.
- [d9s1] He was the grandfather of Nara Bhupal Shah.

**d10: John Westley**

- [d10s0] Rev. John Westley( 1636 – 78) was an English nonconformist minister.
- [d10s1] He was the grandfather of John Wesley( founder of Methodism).

## 10. 2wikimultihopqa_1b5c5d6a0baf11ebab90acde48001122

原位置：`train` 第 10 题 · 全局第 10 题 · `sample_id: 2wikimultihopqa_1b5c5d6a0baf11ebab90acde48001122`

Question: Who is Tiberius (Son Of Justinian Ii)'s paternal grandfather?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Tiberius (Son Of Justinian Ii) | False | () |
| u2 | father of {u1}, Tiberius (Son Of Justinian Ii)'s paternal grandfather | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Tiberius (son of Justinian II) | False | [] | Justinian II | [['d7s0'], ['d7s1']] |
| u2 | father of {u1}, paternal grandfather of Tiberius (son of Justinian II) | True | ['u1'] | Constantine IV | [['d1s1']] |

### Source documents (reference only)

**d1: Justinian II**

- [d1s0] Justinian II (668 – 11 December 711), surnamed the Rhinotmetos or Rhinotmetus , was the last Byzantine Emperor of the Heraclian dynasty, reigning from 685 to 695 and again from 705 to 711.
- [d1s1] Justinian II was an ambitious and passionate ruler who was keen to restore the Roman Empire to its former glories, but he responded poorly to any opposition to his will and lacked the finesse of his father, Constantine IV.
- [d1s2] Consequently, he generated enormous opposition to his reign, resulting in his deposition in 695 in a popular uprising, and he only returned to the throne in 705 with the help of a Bulgar and Slav army.
- [d1s3] His second reign was even more despotic than the first, and it too saw his eventual overthrow in 711, abandoned by his army who turned on him before killing him.

**d2: Henry Bryant (naturalist)**

- [d2s0] Henry Bryant( May 12, 1820 – February 2, 1867) was an American physician and naturalist.
- [d2s1] He was the grandfather of Henry Bryant Bigelow.

**d3: Kaya Alp**

- [d3s0] Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

**d4: Prithvipati Shah**

- [d4s0] Prithvipati Shah( ?–1716) was the king of the Gorkha Kingdom in the Indian subcontinent, present- day Nepal.
- [d4s1] He was the grandfather of Nara Bhupal Shah.

**d5: John Westley**

- [d5s0] Rev. John Westley( 1636 – 78) was an English nonconformist minister.
- [d5s1] He was the grandfather of John Wesley( founder of Methodism).

**d6: Abd al-Muttalib**

- [d6s0] Abd al- Muttalib Shaybah ibn Hashim( c. 497 – 578) was the grandfather of Islamic prophet Muhammad.

**d7: Tiberius (son of Justinian II)**

- [d7s0] Tiberius ("Tiberios"; 705–711) was the son of Emperor Justinian II and Theodora of Khazaria.
- [d7s1] He served as co-emperor of the Byzantine Empire with his father Justinian II, from 706–711.
- [d7s2] Both were killed in 711, when Bardanes led a rebellion which marched on Constantinople.
- [d7s3] After Tiberius' death, two different individuals impersonated him, with one, named Bashir, going on to be hosted by Hisham ibn Abd al-Malik, the Umayyad Caliph, before his lie was discovered and he was crucified.

**d8: Guillaume Wittouck**

- [d8s0] Guillaume Wittouck( 1749- 1829) was a Belgian lawyer and High Magistrate.
- [d8s1] He was the Grandfather of industrialist Paul Wittouck.

**d9: Lyon Cohen**

- [d9s0] Lyon Cohen( 1868–1937) was a Polish- born Canadian businessman and a philanthropist.
- [d9s1] He was the grandfather of singer/ poet Leonard Cohen.

**d10: Fujiwara no Nagara**

- [d10s0] , also known as Fujiwara no Nagayoshi, was a Japanese statesman, courtier and politician of the early Heian period.
- [d10s1] He was the grandfather of Emperor Yōzei.

## 11. 2wikimultihopqa_1ec8b764099211ebbdb0ac1f6bf848b6

原位置：`train` 第 11 题 · 全局第 11 题 · `sample_id: 2wikimultihopqa_1ec8b764099211ebbdb0ac1f6bf848b6`

Question: Are both Ilyinskoye, Selivanovsky District, Vladimir Oblast and Chal Lal located in the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of Ilyinskoye, Selivanovsky District, Vladimir Oblast | False | () |
| u2 | country of Chal Lal | False | () |
| u3 | whether both locations are in the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country of Ilyinskoye, Selivanovsky District, Vladimir Oblast | False | [] | Russia | [['d2s0']] |
| u2 | country of Chal Lal | False | [] | Iran | [['d6s0']] |
| u3 | whether Ilyinskoye, Selivanovsky District, Vladimir Oblast and Chal Lal are located in the same country | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Tuchkovo, Vladimir Oblast**

- [d1s0] Tuchkovo is a rural locality( a selo) in Selivanovsky District, Vladimir Oblast, Russia.
- [d1s1] The population was 9 as of 2010.

**d2: Ilyinskoye, Selivanovsky District, Vladimir Oblast**

- [d2s0] Ilyinskoye is a rural locality( a selo) in Selivanovsky District, Vladimir Oblast, Russia.
- [d2s1] The population was 44 as of 2010.

**d3: Zaborye, Vladimir Oblast**

- [d3s0] Zaborye is a rural locality( a selo) in Selivanovsky District, Vladimir Oblast, Russia.
- [d3s1] The population was 3 as of 2010.

**d4: Nikulino, Selivanovsky District, Vladimir Oblast**

- [d4s0] Nikulino is a rural locality( a selo) in Selivanovsky District, Vladimir Oblast, Russia.
- [d4s1] The population was 2 as of 2010.

**d5: Andreyevskoye (Krasnoselskoye Rural Settlement), Yuryev-Polsky District, Vladimir Oblast**

- [d5s0] Andreyevskoye is a rural locality( a selo) in Selivanovsky District, Vladimir Oblast, Russia.
- [d5s1] The population was 4 as of 2010.

**d6: Chal Lal**

- [d6s0] Chal Lal( also Romanized as Chāl Lāl) is a village in Darreh Kayad Rural District, Sardasht District, Dezful County, Khuzestan Province, Iran.
- [d6s1] At the 2006 census, its existence was noted, but its population was not reported.

**d7: Peremilovo**

- [d7s0] Peremilovo is a rural locality( a selo) in Selivanovsky District, Vladimir Oblast, Russia.
- [d7s1] The population was 1 as of 2010.

**d8: Podlesny, Vladimir Oblast**

- [d8s0] Podlesny is a rural locality( a selo) in Selivanovsky District, Vladimir Oblast, Russia.
- [d8s1] The population was 1 as of 2010.

**d9: Ozyorny, Vladimir Oblast**

- [d9s0] Ozyorny is a rural locality( a selo) in Selivanovsky District, Vladimir Oblast, Russia.
- [d9s1] The population was 2 as of 2010.

**d10: Bogorodskoye, Yuryev-Polsky District, Vladimir Oblast**

- [d10s0] Bogorodskoye is a rural locality( a selo) in Selivanovsky District, Vladimir Oblast, Russia.
- [d10s1] The population was 2 as of 2010.

## 12. 2wikimultihopqa_218b92b40bdc11eba7f7acde48001122

原位置：`train` 第 12 题 · 全局第 12 题 · `sample_id: 2wikimultihopqa_218b92b40bdc11eba7f7acde48001122`

Question: Where was the director of film All By Myself (Film) born?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of All By Myself (Film) | False | () |
| u2 | birthplace of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film All by Myself | False | [] | Felix E. Feist | [['d1s0']] |
| u2 | place of birth of {u1} | True | ['u1'] | New York City | [['d5s0']] |

### Source documents (reference only)

**d1: All by Myself (film)**

- [d1s0] All by Myself is a 1943 American comedy film directed by Felix E. Feist and written by Hugh Wedlock Jr. and Howard Snyder.
- [d1s1] The film stars Rosemary Lane, Evelyn Ankers, Patric Knowles, Neil Hamilton, Grant Mitchell and Louise Beavers.
- [d1s2] The film was released on June 11, 1943, by Universal Pictures.

**d2: Peter Levin**

- [d2s0] Peter Levin is an American director of film, television and theatre.

**d3: Olav Aaraas**

- [d3s0] Olav Aaraas( born 10 July 1950) is a Norwegian historian and museum director.
- [d3s1] He was born in Fredrikstad.
- [d3s2] From 1982 to 1993 he was the director of Sogn Folk Museum, from 1993 to 2010 he was the director of Maihaugen and from 2001 he has been the director of the Norwegian Museum of Cultural History.
- [d3s3] In 2010 he was decorated with the Royal Norwegian Order of St. Olav.

**d4: I Can Do Bad All by Myself (film)**

- [d4s0] I Can Do Bad
- [d4s1] All by Myself is a 2009 American romantic musical comedy- drama film which was released on September 11, 2009.
- [d4s2] The film was directed, produced, and written by Tyler Perry, who also makes an appearance in the film as his signature character Madea.
- [d4s3] Although the film and play share the same title, the film is not an adaptation of Perry's play of the same name; the two works have different storylines.

**d5: Felix E. Feist**

- [d5s0] Felix Ellison Feist (February 28, 1910 – September 2, 1965) was an American film and television director and writer born in New York City.

**d6: Ian Barry (director)**

- [d6s0] Ian Barry is an Australian director of film and TV.

**d7: Jesse E. Hobson**

- [d7s0] Jesse Edward Hobson( May 2, 1911 – November 5, 1970) was the director of SRI International from 1947 to 1955.
- [d7s1] Prior to SRI, he was the director of the Armour Research Foundation.

**d8: Dana Blankstein**

- [d8s0] Dana Blankstein- Cohen( born March 3, 1981) is the director of the Israeli Academy of Film and Television.
- [d8s1] She is a film director, and an Israeli culture entrepreneur.

**d9: Brian Kennedy (gallery director)**

- [d9s0] Brian Patrick Kennedy( born 5 November 1961) is an Irish- born art museum director who has worked in Ireland and Australia, and now lives and works in the United States.
- [d9s1] He is currently the director of the Peabody Essex Museum.
- [d9s2] He was the director of the Toledo Museum of Art in Ohio from 2010 to 2019.
- [d9s3] He was the director of the Hood Museum of Art from 2005 to 2010, and the National Gallery of Australia( Canberra) from 1997- 2004.

**d10: S. N. Mathur**

- [d10s0] S.N. Mathur was the Director of the Indian Intelligence Bureau between September 1975 and February 1980.
- [d10s1] He was also the Director General of Police in Punjab.

## 13. 2wikimultihopqa_2547e59c089b11ebbd78ac1f6bf848b6 【需改：生成拆解】

原位置：`train` 第 13 题 · 全局第 13 题 · `sample_id: 2wikimultihopqa_2547e59c089b11ebbd78ac1f6bf848b6`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_2547e59c089b11ebbd78ac1f6bf848b6"></a>

> **审阅结论：需改：生成拆解**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 单元本身是两个已点名对象的事实加一个比较/共同属性结论，没有寻找未知中间实体的桥接步骤，但 question_type 被写成 bridge_comparison。
>
> **处理建议：** 只将 question_type 改为 comparison，保留当前单元关系；这属于题型元数据错误，不应为凑题型增加桥接单元。
>
> **证据定位：** d5s0, d4s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Who died later, Landgravine Sophie Of Hesse-Kassel or Juan Riba?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | death date of Landgravine Sophie Of Hesse-Kassel | False | () |
| u2 | death date of Juan Riba | False | () |
| u3 | who died later | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | date of death of Landgravine Sophie of Hesse-Kassel | False | [] | 22 November 1670 | [['d5s0']] |
| u2 | date of death of Juan Riba | False | [] | 20 April 1973 | [['d4s0']] |
| u3 | which of Landgravine Sophie of Hesse-Kassel and Juan Riba died later | True | ['u1', 'u2'] | Juan Riba | [[]] |

### Source documents (reference only)

**d1: William IV, Landgrave of Hesse-Kassel**

- [d1s0] William IV of Hesse- Kassel( 24 June 1532 – 25 August 1592), also called" William the Wise", was the first Landgrave of the Landgraviate of Hesse- Kassel( or Hesse- Cassel).
- [d1s1] He was the founder of the oldest line, which survives to this day.

**d2: Prince William of Hesse-Kassel**

- [d2s0] Prince William of Hesse-Kassel (24 December 1787 – 5 September 1867), was the first son of Prince Frederick of Hesse-Kassel and Princess Caroline of Nassau-Usingen.

**d3: Margravine Hedwig Sophie of Brandenburg**

- [d3s0] Hedwig Sophia of Brandenburg( 14 July 1623, Berlin- 26 June 1683, Schmalkalden) was Landgravine consort of Hesse- Kassel by marriage to William VI, Landgrave of Hesse- Kassel, and regent from 1663 until 1677 during the minority of her sons, William VII, Landgrave of Hesse- Kassel and Charles I, Landgrave of Hesse- Kassel.

**d4: Juan Riba**

- [d4s0] Juan Riba Guixà( 19 January 1900 – 20 April 1973) was a Spanish rower.
- [d4s1] He competed in the men's eight event at the 1924 Summer Olympics.

**d5: Landgravine Sophie of Hesse-Kassel**

- [d5s0] Sophie of Hesse- Kassel( 12 September 1615, in Kassel- 22 November 1670, in Bückeburg) was a princess of Hesse- Kassel by birth and by marriage Countess of Schaumburg- Lippe.

**d6: Maurice, Landgrave of Hesse-Kassel**

- [d6s0] Maurice of Hesse- Kassel( 25 May 1572 – 15 March 1632), also called Maurice the Learned, was the Landgrave of Hesse- Kassel( or Hesse- Cassel) in the Holy Roman Empire from 1592 to 1627.

**d7: Charles I, Landgrave of Hesse-Kassel**

- [d7s0] Charles of Hesse- Kassel( 3 August 1654 – 23 March 1730), of the House of Hesse, was the Landgrave of Hesse- Kassel from 1670 to 1730.

**d8: George Charles of Hesse-Kassel**

- [d8s0] George Charles of Hesse-Kassel (8 January 1691 – 5 March 1755) was a prince of Hesse-Kassel and a Prussian General.

**d9: William VII, Landgrave of Hesse-Kassel**

- [d9s0] William VII of Hesse- Kassel( 21 June 1651 – 21 November 1670) was Landgrave of Hesse- Kassel.

**d10: Prince Frederick of Hesse-Kassel**

- [d10s0] Prince Frederick of Hesse-Kassel (11 September 1747 – 20 May 1837) was a younger member of the dynasty that ruled the Landgraviate of Hesse-Kassel (or Hesse-Cassel) and a Danish general.
- [d10s1] He was born as the youngest son of Hereditary Prince Frederick of Hesse-Kassel (the future Landgrave Frederick II) and Princess Mary of Great Britain.
- [d10s2] He was the last surviving grandchild of George II of Great Britain, dying one month before Queen Victoria (granddaughter of his first cousin King George III) ascended to the throne.

## 14. 2wikimultihopqa_254e9ee20bdb11eba7f7acde48001122

原位置：`train` 第 14 题 · 全局第 14 题 · `sample_id: 2wikimultihopqa_254e9ee20bdb11eba7f7acde48001122`

Question: Which country the director of film Kelly Of The Secret Service is from?

Note:

Type: bridge · fallback: False · SFT snapshots: 7

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of film Kelly Of The Secret Service | False | () |
| u2 | country of origin of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Kelly of the Secret Service | False | [] | Robert F. Hill | [['d3s1']] |
| u2 | nationality of {u1} | True | ['u1'] | Canada | [['d7s0']] |

### Source documents (reference only)

**d1: No. 1 of the Secret Service**

- [d1s0] No. 1 of the Secret Service is a 1977 imitation James Bond film starring Nicky Henson as British secret agent Charles Bind.
- [d1s1] It was directed and written by Lindsay Shonteff and produced by his wife Elizabeth Gray.
- [d1s2] The film had the working title of 008 of the Secret Service.
- [d1s3] It was released on VHS under the title Her Majesty ’s Top Gun.

**d2: Holt of the Secret Service**

- [d2s0] Holt of the Secret Service( 1941) was the 16th serial released by Columbia Pictures.

**d3: Kelly of the Secret Service**

- [d3s0] Kelly of the Secret Service is a 1936 American mystery film produced by Sam Katzman.
- [d3s1] Directed by Robert F. Hill, it stars Lloyd Hughes, Jack Mulhall and Sheila Bromley.

**d4: Elmer Washburn**

- [d4s0] Elmer Washburn was the 3rd Director of the United States Secret Service.

**d5: The Secret Service Agent's Memories**

- [d5s0] The secret service agent's memories is a Russian historical film and TV series based on the novel by Oleg Ryaskov, who is also the director.

**d6: Charles Gittens**

- [d6s0] Charles LeRoy Gittens( August 31, 1928 – July 27, 2011) was an American United States Secret Service agent.
- [d6s1] Gittens joined the Secret Service in 1956, becoming the agency's first African American agent.
- [d6s2] Gittens was born in Cambridge, Massachusetts, on August 31, 1928, as one of his family's seven children.
- [d6s3] His father was a contractor who had immigrated to the United States from Barbados.
- [d6s4] He left his high school before graduation in order to enlist in the United States Army.
- [d6s5] He was promoted to lieutenant in the Army and was stationed in Japan during the Korean War.
- [d6s6] Gittens earned his GED while serving in the Army.
- [d6s7] Following the end of the war, Gittens earned a bachelor's degree from present- day North Carolina Central University.
- [d6s8] He completed the four year academic program in three years, and graduated Magna Cum Laude with a Bachelor of Arts degree in English and Spanish.
- [d6s9] As a result, he was bilingual.
- [d6s10] Gittens taught at a school in North Carolina for one year.
- [d6s11] He was encouraged to take the civil service exam, which resulted in his recruitment into the United States Secret Service.
- [d6s12] He began his career at the agency's office in Charlotte, North Carolina.
- [d6s13] He then became an investigator at the Secret Service's field office in New York City, where he served for ten years.
- [d6s14] He was assigned to a" special detail" Secret Service unit, which investigated bank fraud and counterfeiting.
- [d6s15] Gittens was then transferred to the Secret Service's field office in Puerto Rico, where he guarded New York Governor Nelson Rockefeller during his 1969 trip to the Caribbean and Latin America.
- [d6s16] Gittens was promoted to the head of the Secret Service's field office in Washington, D.C. in 1971.
- [d6s17] He retired from the agency in 1979.
- [d6s18] He then joined the United States Department of Justice, where he led investigations of Nazi war criminals who were residing in the United States at the Department's Office of Special Investigations.
- [d6s19] Charles Gittens died of complications from a heart attack at the Collington Episcopal Life Care Community, an assisted living facility in Mitchellville, Maryland, on July 27, 2011, at the age of 82.
- [d6s20] He had moved to the facility from Fort Washington, Maryland, in 2010.
- [d6s21] His first wife, Ruthie, with whom he had one daughter, died in 1991.
- [d6s22] He and his second wife, Maureen, divorced.

**d7: Robert F. Hill**

- [d7s0] Robert F. Hill( April 14, 1886 – March 18, 1966) was a Canadian film director, screenwriter, and actor during the silent film era.

**d8: Mark J. Sullivan**

- [d8s0] Mark J. Sullivan was the Director of the United States Secret Service from May 31, 2006 to March 27, 2013.
- [d8s1] Sullivan succeeded W. Ralph Basham and was sworn in as the 22nd Director of the Secret Service on May 31, 2006.
- [d8s2] He was succeeded by Julia Pierson on March 27, 2013.

**d9: Code of the Secret Service**

- [d9s0] Code of the Secret Service is a 1939 film directed by Noel M. Smith and starring Ronald Reagan.
- [d9s1] It is the second of four films in the U.S. Secret Service Agent Brass Bancroft series, having been preceded by" Secret Service of the Air"( 1939) and followed by" Smashing the Money Ring"( 1939) and" Murder in the Air"( 1940).
- [d9s2] The series was part of a late 1930s effort by Warner Bros. to produce films depicting law enforcement in a positive light under pressure from Homer Stille Cummings( Franklin D. Roosevelt's Attorney General) and Will H. Hays( creator of the Motion Picture Production Code, the movie industry's censorship guidelines), due to the studio's part in producing early 1930s films glamorizing gangsters.
- [d9s3] The series also enabled Warner Bros. to create Reagan's screen persona, with Reagan even showing up to the set of" Code of the Secret Service" and asking director Noel M. Smith," When do I fight and whom?"

**d10: U. E. Baughman**

- [d10s0] Urbanus Edmund Baughman( 21 May 1905 – 6 November 1978) was the chief of the United States Secret Service between 1948 and 1961, under Presidents Truman, Eisenhower, and Kennedy.
- [d10s1] Baughman was the first Secret Service Chief to pen a memoir concerning the office he held.
- [d10s2] Entitled" Secret Service Chief", it was a veritable tell- all on the intricacies and inner workings of the Secret Service and its evolution from a counterfeit detection department to the presidential protection unit.
- [d10s3] Baughman was appointed to head the Secret Service by President Harry S. Truman shortly after the 1948 election.
- [d10s4] According to the book" American Gunfight", by Stephen Hunter and John Bainbridge Jr., Truman dismissed Baughman's predecessor James J. Maloney in part because he had dispatched most of Truman's Secret Service detail to New York to prepare to guard New York Governor Thomas E. Dewey.
- [d10s5] Dewey was widely expected to be elected president but was beaten by Truman in one of the greatest upsets in presidential election history.

## 15. 2wikimultihopqa_2564e76e089e11ebbd78ac1f6bf848b6

原位置：`train` 第 15 题 · 全局第 15 题 · `sample_id: 2wikimultihopqa_2564e76e089e11ebbd78ac1f6bf848b6`

Question: Who was born first, Jaime Manuel Gómez or Lars Levi Laestadius?

Note:

Type: comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | birth date of Jaime Manuel Gómez | False | () |
| u2 | birth date of Lars Levi Laestadius | False | () |
| u3 | who was born first | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | date of birth of Jaime Manuel Gómez | False | [] | June 27, 1972 | [['d5s0']] |
| u2 | date of birth of Lars Levi Laestadius | False | [] | 10 January 1800 | [['d10s0']] |
| u3 | which of Jaime Manuel Gómez and Lars Levi Laestadius was born first | True | ['u1', 'u2'] | Lars Levi Laestadius | [[]] |

### Source documents (reference only)

**d1: Manuel Gómez Mora**

- [d1s0] Manuel Gómez Mora( born August 16, 1990 in Guadalajara, Jalisco), known as Manuel Gómez, is a Mexican professional association football( soccer) player who plays for Inter Playa del Carmen.

**d2: Henry Moore (cricketer)**

- [d2s0] Henry Walter Moore( 1849 – 20 August 1916) was an English- born first- class cricketer who spent most of his life in New Zealand.

**d3: Rodrigo Gómez (Argentine footballer)**

- [d3s0] Rodrigo Manuel Gómez born( 2 January 1993) is an Argentine football midfielder who currently plays for Huracán on loan from Toluca.

**d4: Milla Clementsdotter**

- [d4s0] Milla Clementsdotter( also known as, Milla Clemensdotter, Maria of Lappland( Finnish language, Lapin Maija; November 1, 1812 – April 8, 1892) was a Swedish Southern Sami woman who is remembered for guiding Lars Levi Laestadius in questions of Christian faith.
- [d4s1] She belonged to a revival movement marked by Pietistic and Moravian influences, a member of a group known as" Readers", a background shared by Laestadius' mother.

**d5: Jaime Manuel Gómez**

- [d5s0] Jaime Manuel Gomez( born June 27, 1972 in Laredo, Texas) is a Mexican American professional boxer in the Light Middleweight division.

**d6: Hartley Lobban**

- [d6s0] Hartley W Lobban (9 May 1926 – 15 October 2004) was a Jamaican-born first-class cricketer who played 17 matches for Worcestershire in the early 1950s.

**d7: John McMahon (Surrey and Somerset cricketer)**

- [d7s0] John William Joseph McMahon( 28 December 1917 – 8 May 2001) was an Australian- born first- class cricketer who played for Surrey and Somerset in England from 1947 to 1957.

**d8: Wale Adebanwi**

- [d8s0] Wale Adebanwi( born 1969) is a Nigerian- born first Black Rhodes Professor at St Antony's College, Oxford.

**d9: Manuel Gómez-Moreno González**

- [d9s0] Manuel Gómez- Moreno González( 26 June 1834 – 20 December 1918) was a Spanish painter, amateur archaeologist and professor.
- [d9s1] His son was the noted historian and archaeologist, Manuel Gómez- Moreno Martínez.

**d10: Lars Levi Laestadius**

- [d10s0] Lars Levi Laestadius( 10 January 1800 – 21 February 1861) was a Swedish pastor and administrator of the Swedish state Lutheran church in Lapland who founded the Laestadian pietist revival movement to help his largely Sami congregations, who were being ravaged by alcoholism.
- [d10s1] Laestadius was also a noted botanist and an author.
- [d10s2] Laestadius himself became a teetotaller( except for his ongoing use of wine in holy Communion) in the 1840s, when he began successfully awakening his Sami parishioners to the misery and destruction alcohol was causing them.

## 16. 2wikimultihopqa_297ea8fb097011ebbdb0ac1f6bf848b6

原位置：`train` 第 16 题 · 全局第 16 题 · `sample_id: 2wikimultihopqa_297ea8fb097011ebbdb0ac1f6bf848b6`

Question: Are Aghol Beyk-E Olya and Bardiyeh-Ye Yek located in the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of Aghol Beyk-E Olya | False | () |
| u2 | country of Bardiyeh-Ye Yek | False | () |
| u3 | whether Aghol Beyk-E Olya and Bardiyeh-Ye Yek are located in the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country where Aghol Beyk-e Olya is located | False | [] | Iran | [['d2s0']] |
| u2 | country where Bardiyeh-ye Yek is located | False | [] | Iran | [['d5s0']] |
| u3 | whether Aghol Beyk-e Olya and Bardiyeh-ye Yek are located in the same country | True | ['u1', 'u2'] | yes | [[]] |

### Source documents (reference only)

**d1: Soveychti-ye Yek**

- [d1s0] Soveychti-ye Yek( also Romanized as Soveychtī- ye Yek; also known as Soveyḩetī- ye Yek) is a village in Gharb -e Karun Rural District, in the Central District of Khorramshahr County, Khuzestan Province, Iran.
- [d1s1] At the 2006 census, its population was 273, in 46 families.

**d2: Aghol Beyk-e Olya**

- [d2s0] Aghol Beyk -e Olya( also Romanized as Āghol Beyk- e ‘ Olyā; also known as Aghalbak, Aqalbak Bāla, Ogholbeyg- e Bālā, Ogholbeyk- e- ‘ Olyā, Oghūl Beyg- e Bālā, Oghulbeyn, Owghlī Beyg- e ‘ Olyā, and Owghol Beyg- e Bālā) is a village in Ijrud -e Bala Rural District, in the Central District of Ijrud County, Zanjan Province, Iran.
- [d2s1] At the 2006 census, its population was 949, in 232 families.

**d3: Taleqan-ye Yek**

- [d3s0] Taleqan- ye Yek( meaning" Taleqan 1", also Romanized as Ţāleqān- ye Yek and Ţāleghānī- ye Yek) is a village in Kashkan Rural District, Shahivand District, Dowreh County, Lorestan Province, Iran.
- [d3s1] At the 2006 census, its population was 229, in 46 families.

**d4: Tavileh-ye Yek**

- [d4s0] Tavileh- ye Yek( also Romanized as Ţavīleh- ye Yek) is a village in Hoveyzeh Rural District, in the Central District of Hoveyzeh County, Khuzestan Province, Iran.
- [d4s1] At the 2006 census, its population was 41, in 7 families.

**d5: Bardiyeh-ye Yek**

- [d5s0] Bardiyeh- ye Yek( also Romanized as Bardīyeh- ye Yek; also known as Bardīyeh and Sardīyeh) is a village in Howmeh- ye Gharbi Rural District, in the Central District of Dasht -e Azadegan County, Khuzestan Province, Iran.
- [d5s1] At the 2006 census, its population was 1,479, in 236 families.

**d6: Yekaviyeh-ye Yek**

- [d6s0] Yekaviyeh- ye Yek( also Romanized as Yekāvīyeh- ye Yek; also known as Lekāvīgeh- ye Yek) is a village in Anaqcheh Rural District, in the Central District of Ahvaz County, Khuzestan Province, Iran.
- [d6s1] At the 2006 census, its population was 774, in 86 families.

**d7: Chahshur-e Halvayi-ye Yek**

- [d7s0] Chahshur -e Halvayi -ye Yek( also Romanized as Chāhshūr -e Ḩalvāy ī- ye Yek; also known as Chāhshūr -e Ḩalvāee- ye Yek) is a village in Karian Rural District, in the Central District of Minab County, Hormozgan Province, Iran.
- [d7s1] At the 2006 census, its population was 64, in 12 families.

**d8: Mansuriyeh-ye Yek**

- [d8s0] Mansuriyeh- ye Yek( also Romanized as Manşūrīyeh- ye Yek) is a village in Anaqcheh Rural District, in the Central District of Ahvaz County, Khuzestan Province, Iran.
- [d8s1] At the 2006 census, its population was 305, in 63 families.

**d9: Maliheh-ye Yek, Hoveyzeh**

- [d9s0] Maliheh- ye Yek( also Romanized as Māliḥeh- ye Yek) is a village in Hoveyzeh Rural District, in the Central District of Hoveyzeh County, Khuzestan Province, Iran.
- [d9s1] At the 2006 census, its population was 284, in 45 families.

**d10: Abu Geraniyeh-ye Yek**

- [d10s0] Abu Geraniyeh- ye Yek( also Romanized as Abū Gerānīyeh- ye Yek; also known as Abū Gereyneh- ye Yek) is a village in Shoaybiyeh- ye Sharqi Rural District, Shadravan District, Shushtar County, Khuzestan Province, Iran.
- [d10s1] At the 2006 census, its population was 135, in 16 families.

## 17. 2wikimultihopqa_2ec600e40bb011ebab90acde48001122

原位置：`train` 第 17 题 · 全局第 17 题 · `sample_id: 2wikimultihopqa_2ec600e40bb011ebab90acde48001122`

Question: Who is the paternal grandfather of Milo (Bishop Of Trier)?

Note:

Type: bridge · fallback: False · SFT snapshots: 7

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Milo (Bishop Of Trier) | False | () |
| u2 | father of {u1}, Milo (Bishop Of Trier)'s paternal grandfather | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Milo (bishop of Trier) | False | [] | Leudwinus | [['d9s0']] |
| u2 | father of {u1}, Milo's paternal grandfather | True | ['u1'] | Saint Warinus | [['d1s5']] |

### Source documents (reference only)

**d1: Leudwinus**

- [d1s0] Saint Leudwinus, Count of Treves ("Leodewin, Liutwin, Ludwin")
- [d1s1] (c. 660 – 29 September 722 in Reims) founded an abbey in Mettlach.
- [d1s2] He was Archbishop of Treves and Laon.
- [d1s3] As patron saint of the Mettlach parish, his relics are carried through the town by procession at the annual Pentecost celebration.
- [d1s4] His feast day is September 23.
- [d1s5] He was the son of Saint Warinus, the paternal grandson of Saint Sigrada, and nephew of Saint Leodegarius.

**d2: Fujiwara no Nagara**

- [d2s0] , also known as Fujiwara no Nagayoshi, was a Japanese statesman, courtier and politician of the early Heian period.
- [d2s1] He was the grandfather of Emperor Yōzei.

**d3: Prithvipati Shah**

- [d3s0] Prithvipati Shah( ?–1716) was the king of the Gorkha Kingdom in the Indian subcontinent, present- day Nepal.
- [d3s1] He was the grandfather of Nara Bhupal Shah.

**d4: Abd al-Muttalib**

- [d4s0] Abd al- Muttalib Shaybah ibn Hashim( c. 497 – 578) was the grandfather of Islamic prophet Muhammad.

**d5: Kaya Alp**

- [d5s0] Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

**d6: Lyon Cohen**

- [d6s0] Lyon Cohen( 1868–1937) was a Polish- born Canadian businessman and a philanthropist.
- [d6s1] He was the grandfather of singer/ poet Leonard Cohen.

**d7: John Westley**

- [d7s0] Rev. John Westley( 1636 – 78) was an English nonconformist minister.
- [d7s1] He was the grandfather of John Wesley( founder of Methodism).

**d8: Henry Bryant (naturalist)**

- [d8s0] Henry Bryant( May 12, 1820 – February 2, 1867) was an American physician and naturalist.
- [d8s1] He was the grandfather of Henry Bryant Bigelow.

**d9: Milo (bishop of Trier)**

- [d9s0] Milo of Trier (d. 762 or 763) was the son of St. Leudwinus and his successor as Archbishop of Trier and Archbishop of Reims.
- [d9s1] His great-uncle Saint Basinus had preceded his father as Trier.
- [d9s2] He was the great-grandson of Saint Sigrada and Saint Leodegarius was his great uncle.

**d10: Guillaume Wittouck**

- [d10s0] Guillaume Wittouck( 1749- 1829) was a Belgian lawyer and High Magistrate.
- [d10s1] He was the Grandfather of industrialist Paul Wittouck.

## 18. 2wikimultihopqa_30f1c3da0bb011ebab90acde48001122

原位置：`train` 第 18 题 · 全局第 18 题 · `sample_id: 2wikimultihopqa_30f1c3da0bb011ebab90acde48001122`

Question: Who is the maternal grandfather of William D'Aubigny, 2Nd Earl Of Arundel?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | mother of William D'Aubigny, 2nd Earl Of Arundel | False | () |
| u2 | father of {u1}, William D'Aubigny's maternal grandfather | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | mother of William d'Aubigny, 2nd Earl of Arundel | False | [] | Adeliza of Louvain | [['d5s0']] |
| u2 | father of {u1}, maternal grandfather of William d'Aubigny, 2nd Earl of Arundel | True | ['u1'] | Godfrey I, Count of Louvain | [['d7s0']] |

### Source documents (reference only)

**d1: William Fitzalan, 9th Earl of Arundel**

- [d1s0] William Fitzalan, 9th Earl of Arundel, 6th Baron Maltravers( 23 November 1417 – 1487) was an English nobleman.
- [d1s1] Born on 23 November 1417, William was the second son of John Fitzalan, 6th Earl of Arundel( 1385 – 1421), and Eleanor Berkeley( d. 1455), daughter of John Berkeley of Beverston.
- [d1s2] His elder brother John Fitzalan, 7th Earl of Arundel, died on 12 June 1435.
- [d1s3] The title passed to William's nephew Humphrey Fitzalan, 8th Earl of Arundel, who was only a six- year- old with no descendants.
- [d1s4] William thus became the heir presumptive and, when Humphrey died three years later on 24 April 1438, he succeeded to the title.

**d2: Hugh d'Aubigny, 5th Earl of Arundel**

- [d2s0] Hugh d' Aubigny, 5th Earl of Arundel( died 7 May 1243) was the last in the Aubigny male line to hold the Arundel Castle.
- [d2s1] He was the son of William d'Aubigny, 3rd Earl of Arundel and younger brother of William d'Aubigny, 4th Earl of Arundel.
- [d2s2] He inherited his title on the death of his elder brother in 1224.
- [d2s3] He also inherited the position of hereditary Chief Butler of England for life.
- [d2s4] In 1242 he was one of the seven Earls who accompanied the King Henry in his expedition to Aquitaine.
- [d2s5] On his death he was buried at Wymondham Abbey and his large estates divided amongst his four sisters and their issue.
- [d2s6] His title of Earl of Arundel was inherited by his nephew John FitzAlan, 6th Earl of Arundel, son of his sister Isabel d'Aubigny.
- [d2s7] He had married Isabel de Warenne( c. 1228– 1282), daughter of William de Warenne, 5th Earl of Surrey and Maud Marshal( 1192 – 1248).
- [d2s8] They had no children.
- [d2s9] His widow never remarried but became an important countess who founded the Cistercian Abbey at Marham and may have been buried at Convent Church Marham.

**d3: William d'Aubigny, 4th Earl of Arundel**

- [d3s0] William d' Aubigny, 4th Earl of Arundel, also known as William de Albini V( b. 1203 – before 7 August 1224) was the eldest son of William d'Aubigny, 3rd Earl of Arundel and Mabel of Chester( born c. 1173), daughter of Hugh de Kevelioc, 3rd Earl of Chester and Bertrade de Montfort of Évreux.
- [d3s1] He became Earl of Arundel and Earl of Sussex on 30 March 1221.
- [d3s2] He was buried at Wymondham Abbey, Norfolk.
- [d3s3] There is no evidence that he married or had children.
- [d3s4] He was the Chief Butler of England and was succeeded by his brother, Hugh.

**d4: Thomas Bruce, 2nd Earl of Ailesbury**

- [d4s0] Thomas Bruce, 2nd Earl of Ailesbury( later styled Aylesbury) and 3rd Earl of Elgin( 1656 – 16 December 1741) was an English politician and memoirist.
- [d4s1] He was the son of Robert Bruce, 2nd Earl of Elgin, and Lady Diana Grey.
- [d4s2] His maternal grandparents were Henry Grey, 1st Earl of Stamford, and Lady Anne Cecil, daughter of William Cecil, 2nd Earl of Exeter.
- [d4s3] His" Memoirs", which were not published until long after his death, are a valuable source for English history in the last quarter of the seventeenth century.

**d5: William d'Aubigny, 2nd Earl of Arundel**

- [d5s0] William d' Aubigny, 2nd Earl of Arundel( b.[ 1138-1150], d. 24 December 1193), also called William de Albini III, was the son of William d'Aubigny, 1st Earl of Arundel and Adeliza of Louvain, widow of Henry I of England.
- [d5s1] He married Maud de St. Hilary and among their children was William d'Aubigny, 3rd Earl of Arundel.
- [d5s2] The Duke of Norfolk's Archives Assistant Librarian Sara Rodger wrote that William" did have three sons, William who succeeded him as Earl in 1196, and Alan and Geoffrey, of whom we know nothing."
- [d5s3] His daughter, Matilda d' Aubigny, married William de Warenne, 5th Earl of Surrey.
- [d5s4] In 1176/ 7 he was created Earl of Sussex and in 1190 he inherited the earldom of Arundel.
- [d5s5] He is buried at Wymondham Abbey, Norfolk, England.

**d6: Humphrey Fitzalan, 8th Earl of Arundel**

- [d6s0] Humphrey Fitzalan, 8th Earl of Arundel, 5th Baron Maltravers( 30 January 142924 April 1438).
- [d6s1] This Earl of Arundel was short lived.
- [d6s2] He was a son of John Fitzalan, 7th Earl of Arundel, and Maud Lovell.
- [d6s3] His father died on 12 June 1435, leaving 6- year- old Humphrey as the 15th Earl of Arundel.
- [d6s4] Humphrey died three years later, at age 9.
- [d6s5] The title then passed to his uncle William Fitzalan, 9th Earl of Arundel.
- [d6s6] His older half- sister Avice Stafford( 4 December 14233 June 1457) married James Butler, 1st Earl of Wiltshire.

**d7: Adeliza of Louvain**

- [d7s0] Adeliza of Louvain, sometimes known in England as Adelicia of Louvain, also called Adela and Aleidis; (c. 1103 – March/April 1151) was Queen of England from 1121 to 1135, as the second wife of King Henry I. She was the daughter of Godfrey I, Count of Louvain.
- [d7s1] Henry was some 35 years older than his bride, who was about 18 when they married.
- [d7s2] He already had children, though no surviving son, from his first marriage to Matilda of Scotland, as well as several illegitimate ones.
- [d7s3] As his second marriage produced no children, the decision was made to leave the throne to his daughter, the Empress Matilda; an oath was sworn by the clergy, members of the royal family, including Adeliza, as well as English nobles to recognise Matilda as Henry's heir upon his death.
- [d7s4] After his death Adeliza spent three years based in a convent, then married again and had seven children by William d'Aubigny, 1st Earl of Arundel.
- [d7s5] But a year before her death at the age of forty eight she left her husband to move to a monastery in Flanders, where at least one of her brothers also lived.
- [d7s6] Adeliza's royal marriage seems to have been successful, apart from the failure to produce a new heir.
- [d7s7] The flow of Henry's illegitimate children seems already to have ceased by the time of the marriage, and they spent most of their marriage together, which was by no means inevitable in royal marriages of the period.
- [d7s8] She seems to have been influential in the promotion of French poetry and other arts at court, but played little part in politics.

**d8: William d'Aubigny, 3rd Earl of Arundel**

- [d8s0] William d'Aubigny, 3rd Earl of Arundel, also called William de Albini IV, (before 1180 – 1 February 1221) was an English nobleman, a favourite of King John, and a participant in the Fifth Crusade.

**d9: William d'Aubigny, 1st Earl of Arundel**

- [d9s0] William d' Aubigny, 1st Earl of Lincoln and 1st Earl of Arundel( c. 110912 October 1176), also known as William d' Albini, William de Albini and William de Albini II, was an English nobleman.
- [d9s1] He was the son of William d'Aubigny" Pincerna" of Old Buckenham Castle in Norfolk, and Maud Bigod, daughter of Roger Bigod of Norfolk.

**d10: Thomas Fitzalan, 10th Earl of Arundel**

- [d10s0] Thomas Fitzalan otherwise Arundel, 10th Earl of Arundel, 7th Baron Maltravers( 145025 October 1524) was the son of William Fitzalan, 9th Earl of Arundel, and Joan Neville, eldest daughter of Richard Neville, 5th Earl of Salisbury, and Alice Montagu," suo jure" Countess of Salisbury.

## 19. 2wikimultihopqa_31756c8e085511ebbd59ac1f6bf848b6 【保留新拆法｜重标人工标签】

原位置：`train` 第 19 题 · 全局第 19 题 · `sample_id: 2wikimultihopqa_31756c8e085511ebbd59ac1f6bf848b6`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_31756c8e085511ebbd59ac1f6bf848b6"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。
>
> **处理建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。
>
> **证据定位：** d1s0, d4s0, d2s0, d7s1；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Do both Opium (1919 Film) and Monna Vanna (1915 Film) films have the directors from the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of director of Opium (1919 Film) | False | () |
| u2 | country of director of Monna Vanna (1915 Film) | False | () |
| u3 | whether directors of Opium (1919 Film) and Monna Vanna (1915 Film) are from the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of Opium (1919 film) | False | [] | Robert Reinert | [['d1s0'], ['d4s3']] |
| u2 | nationality of {u1} | False | ['u1'] | German | [['d4s0']] |
| u3 | director of Monna Vanna (1915 film) | False | [] | Mario Caserini | [['d2s0']] |
| u4 | nationality of {u3} | False | ['u3'] | Italian | [['d7s1']] |
| u5 | whether the directors of Opium (1919 film) and Monna Vanna (1915 film) are from the same country | True | ['u2', 'u4'] | no | [[]] |

### Source documents (reference only)

**d1: Opium (1919 film)**

- [d1s0] Opium is a 1919 German silent film directed by Robert Reinert and starring Eduard von Winterstein, Sybill Morel and Werner Krauss.

**d2: Monna Vanna (1915 film)**

- [d2s0] Monna Vanna is a 1915 Italian silent film directed by Mario Caserini and starring Madeleine Céliat, Hamilton Revelle and François-Paul Donadio.
- [d2s1] It was released in the United States by Universal Pictures in 1916.

**d3: J'accuse! (1938 film)**

- [d3s0] J'accuse! is a 1938 French war film directed by Abel Gance and starring Victor Francen.
- [d3s1] It is a remake of the 1919 film of the same name, which was also directed by Gance.

**d4: Robert Reinert**

- [d4s0] Robert Reinert (1872–1928) was a German film director and screenwriter.
- [d4s1] Born in Vienna, he moved to Munich around 1900.
- [d4s2] He wrote several novels, including "Der Weg zur Sonne" (1906) and "Krieg" (1907).
- [d4s3] His successful script for the film "Homunculus" (1916) led him to direct several films, most notably "Opium" and "NervenNerven" opened in Munich in 1919.
- [d4s4] People were hospitalized after watching the movie and one woman, after seeing it, woke up one night, went out on the street in her nightshirt and screamed "Now I am going to die!
- [d4s5] Now I am going to die!"
- [d4s6] About "Nerven", one recent critic wrote Nerven" is a disorienting, highly experimental work.
- [d4s7] Released in 1919, before "The Cabinet of Dr. Caligari" (early 1920), it might have become a prototype of German Expressionist cinema if it had been widely seen."
- [d4s8] Reinert married actress Thea Steinbrecher in 1921.
- [d4s9] Reinert's films were not a commercial success, and in 1925 he got a job with UFA, where he worked until his death of a heart attack in 1928.

**d5: Mark Lewis (filmmaker)**

- [d5s0] Mark Lewis( born 1958 in Mullumbimby, Australia) is an Australian documentary film and television producer, director and writer.
- [d5s1] He is famous for his film and for his body of work on animals.
- [d5s2] Unlike many other producers of nature films, his films do not attempt to document the animals in question or their behaviors but rather the complex relationships between people and society and the animals they interact with.
- [d5s3] His films have earned him many awards, including a British Academy Award nomination, a nomination from the Directors Guild of America, two Emmy ’s for Outstanding Direction in documentary film, and an Emmy Award for Outstanding Science Program on American Television.

**d6: The Grey Car**

- [d6s0] The Grey Car is a 1919 film directed by Enrique Rosas which is the number 98 in 100 Mexican best movies.

**d7: Mario Caserini**

- [d7s0] Mario Caserini( 26 February
- [d7s1] 1874 – 17 November 1920) was an Italian film director, as well as an actor, screenwriter, and early pioneer of film making in the early portion of the 20th century.
- [d7s2] Caserini was born in Rome, Italy, and was married to early 20th- century Italian actress Maria Caserini.
- [d7s3] His 1906 film Otello is believed to be the earliest film adaptation of the William Shakespeare play" Othello".

**d8: Monna Vanna (1922 film)**

- [d8s0] Monna Vanna is a 1922 German silent historical film directed by Richard Eichberg and starring Lee Parry, Paul Wegener and Hans Stürm.
- [d8s1] The film is based on the play" Monna Vanna" by Maurice Maeterlinck which itself drew on story by the sixteenth century writer Niccolò Machiavelli.
- [d8s2] It was made at the Emelka Studios near Munich as part of a deal Eichberg had struck with Bavaria Film.
- [d8s3] Some filming also took place at the Johannisthal Studios in Berlin.
- [d8s4] The film's sets were designed by the art directors Willy Reiber, Jacek Rotmil and Kurt Richter.

**d9: Bruce Gordon (actor/director)**

- [d9s0] Bruce Gordon was an actor who appeared in and directed the 1919 film" The First Men in the Moon".
- [d9s1] He was born in Johannesburg, South Africa.

**d10: The White Hope (1922 film)**

- [d10s0] The White Hope is a 1922 British silent sports film directed by Frank Wilson and starring Violet Hopson, Stuart Rome and John MacAndrews.
- [d10s1] It is a remake of Wilson's own 1915 film of the same name with many of the same cast members.

## 20. 2wikimultihopqa_32e5e2840bb011ebab90acde48001122 【需改：生成拆解】

原位置：`train` 第 20 题 · 全局第 20 题 · `sample_id: 2wikimultihopqa_32e5e2840bb011ebab90acde48001122`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_32e5e2840bb011ebab90acde48001122"></a>

> **审阅结论：需改：生成拆解**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新 u1 是母亲，u2 却写 father of {u1}，实际变成了外祖父；原题问本人父亲。这是关系错误，不是合理的粒度差异。
>
> **处理建议：** 必须把 u2 的“father of {u1}（母亲的父亲）”改回 Elizabeth 本人的父亲。可以保留两单元并写清“father of Elizabeth, given {u1} as her mother”，也可以利用 d4s1 的直接父女证据改成单单元；关键是修正亲属关系，不是强制某种粒度。
>
> **证据定位：** d4s0, d4s1, d9s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Who is the father of Grand Duchess Elizabeth Mikhailovna Of Russia?

Note:

Type: bridge · fallback: False · SFT snapshots: 7

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | mother of Grand Duchess Elizabeth Mikhailovna Of Russia | False | () |
| u2 | father of {u1}, Grand Duchess Elizabeth Mikhailovna Of Russia's father | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | mother of Grand Duchess Elizabeth Mikhailovna of Russia | False | [] | Princess Charlotte of Württemberg | [['d4s0', 'd4s1']] |
| u2 | father of Grand Duchess Elizabeth Mikhailovna of Russia, given {u1} as her mother | True | ['u1'] | Grand Duke Michael Pavlovich of Russia | [['d9s0'], ['d4s0', 'd4s1']] |

### Source documents (reference only)

**d1: Prince Dmitri Alexandrovich of Russia**

- [d1s0] Prince Dmitri Alexandrovich of Russia (15 August 1901 – 7 July 1980) was the fourth son and fifth child of Grand Duke Alexander Mikhailovich of Russia and Grand Duchess Xenia Alexandrovna of Russia.
- [d1s1] He was a nephew of Tsar Nicholas II of Russia.

**d2: Prince Gabriel Constantinovich of Russia**

- [d2s0] Prince Gabriel Constantinovich of Russia( 15 July
- [d2s1] 1887 – 28 February 1955) was the second son of Grand Duke Konstantin Konstantinovich of Russia and his wife, Grand Duchess Elizabeth Mavrikievna of Russia.
- [d2s2] A great- grandson of Tsar Nicholas I, he was born in Imperial Russia and served in the army during World War I.
- [d2s3] He lost much of his family during the war and the Russian Revolution.
- [d2s4] He narrowly escaped execution by the Bolsheviks and spent the rest of his life living in exile in France.

**d3: Héctor Barrantes**

- [d3s0] Héctor Barrantes Sansoni( 1939–1990) was an Argentine polo player.
- [d3s1] He was the stepfather of Sarah, Duchess of York.

**d4: Grand Duchess Elizabeth Mikhailovna of Russia**

- [d4s0] Grand Duchess Elizabeth Mikhailovna of Russia
- [d4s1] (Moscow, 26 May 1826 – Wiesbaden, 28 January 1845) was the second child and daughter of Grand Duke Mikhail Pavlovich of Russia and Princess Charlotte of Württemberg who took the name "Elena Pavlovna" upon her conversion to the Orthodox faith.
- [d4s2] Through her father, Elizabeth was a granddaughter of Tsar Paul I of Russia, and a niece of both Russian emperors
- [d4s3] Alexander I and Nicholas I.

**d5: Barbara (Yakovleva)**

- [d5s0] Varvara Alexeyevna Yakovleva( c. 1880- July 18, 1918), called Nun Barbara, was a Russian Orthodox nun in the convent of Grand Duchess Elizabeth Fyodorovna.
- [d5s1] She was killed by the Bolsheviks along with the grand duchess and Prince Ioann Konstantinovich of Russia, Prince Konstantin Konstantinovich of Russia, Prince Igor Konstantinovich of Russia, Grand Duke Sergei Mikhailovich of Russia, Fyodor Remez, Grand Duke Sergei's secretary, and Prince Vladimir Pavlovich Paley at Alapaevsk.
- [d5s2] She was later canonized as a martyr by both the Russian Orthodox Church Outside Russia and the Russian Orthodox Church within Russia.

**d6: Grand Duchess Catherine Mikhailovna of Russia**

- [d6s0] Grand Duchess Catherine Mikhailovna of Russia( 28 August 1827 – 12 May 1894), was the third of five daughters of Grand Duke Michael Pavlovich of Russia( youngest son of Emperor Paul I and Princess Sophie Dorothea of Württemberg) and Princess Charlotte of Württemberg( eldest child of Prince Paul of Württemberg and Princess Charlotte of Saxe- Hildburghausen).

**d7: Abdul-Vahed Niyazov**

- [d7s0] ' of Russia.

**d8: Grand Duchess Olga Pavlovna of Russia**

- [d8s0] Grand Duchess Olga Pavlovna of Russia  was a "Grand Duchess of Russia" as the second youngest daughter and seventh child of Emperor Paul I of Russia and his empress consort, Sophie Dorothea of Württemberg.

**d9: Princess Charlotte of Württemberg**

- [d9s0] Princess Charlotte of Württemberg (9 January 1807 – 2 February 1873) was later known as Grand Duchess Elena Pavlovna, the wife of Grand Duke Michael Pavlovich of Russia.
- [d9s1] He was the youngest son of Emperor Paul I of Russia and Duchess Sophie Dorothea of Württemberg.

**d10: Princess Vera Constantinovna of Russia**

- [d10s0] Princess Vera Constantinovna of Russia, also Vera Konstantinovna( 24 April 1906 – 11 January 2001), was the youngest child of Grand Duke Konstantine Konstantinovich of Russia and his wife, Grand Duchess Elizabeth Mavrikievna.
- [d10s1] A great- granddaughter of Tsar Nicholas
- [d10s2] I of Russia, she was born in the Russian Empire and was a childhood playmate of the younger children of Emperor Nicholas II of Russia.
- [d10s3] She lost much of her family during World War I and the Russian Revolution.
- [d10s4] At age twelve, she escaped revolutionary Russia, fleeing with her mother and brother George to Sweden.
- [d10s5] She spent the rest of her long life in exile, first in Western Europe and from the 1950s in the United States.

## 21. 2wikimultihopqa_36363b920baf11ebab90acde48001122

原位置：`train` 第 21 题 · 全局第 21 题 · `sample_id: 2wikimultihopqa_36363b920baf11ebab90acde48001122`

Question: Who is Abba Saga's paternal grandfather?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Abba Saga | False | () |
| u2 | father of {u1}, Abba Saga's paternal grandfather | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Abba Saga | False | [] | Zara Yaqob | [['d1s0']] |
| u2 | father of {u1}, Abba Saga's paternal grandfather | True | ['u1'] | Dawit I | [['d6s3']] |

### Source documents (reference only)

**d1: Abba Saga**

- [d1s0] Abba Saga was the son of the Ethiopian king Zara Yaqob, and a monk of Ethiopian Christianity.
- [d1s1] His teacher was Abba Sabra, a monk of Ethiopian Christianity.
- [d1s2] He converted to Judaism after Abba Sabra, himself converted.
- [d1s3] Later Abba Sabra and Abba Saga, established a separate kingdom in modern day Ethiopia in which Jews were not persecuted, unlike the kingdom, of his father, who was known as" the exterminator of the Jews" in which Jews were severely persecuted.

**d2: Abba Bok'a**

- [d2s0] Moti Abba Bok'a was a King of the Gibe Kingdom of Jimma( reigned 1859 – 1862).
- [d2s1] He was the son of Abba Magal, and brother of Abba Jifar I.

**d3: Abd al-Muttalib**

- [d3s0] Abd al- Muttalib Shaybah ibn Hashim( c. 497 – 578) was the grandfather of Islamic prophet Muhammad.

**d4: Guillaume Wittouck**

- [d4s0] Guillaume Wittouck( 1749- 1829) was a Belgian lawyer and High Magistrate.
- [d4s1] He was the Grandfather of industrialist Paul Wittouck.

**d5: Fujiwara no Nagara**

- [d5s0] , also known as Fujiwara no Nagayoshi, was a Japanese statesman, courtier and politician of the early Heian period.
- [d5s1] He was the grandfather of Emperor Yōzei.

**d6: Zara Yaqob**

- [d6s0] Zar'a Ya`qob or Zera Yacob
- [d6s1] (Ge'ez ዘርአ:ያዕቆብ "zar'ā yāʿiqōb", English: "Descendant of Jacob"; 1399 – 26 August 1468) was the Emperor ("nəgusä nägäst") of Ethiopia, and a member of the Solomonic dynasty who ruled under regnal name Kwestantinos
- [d6s2] I (Ge'ez ቈስታንቲኖስ "qʷastāntīnōs") or Constantine I, from the old province of Shewa, where the capital of the Amhara emperors was located before the post-16th-century Oromo migrations and the destructive war with Gran Ahmad.
- [d6s3] Born at Telq in the province of Fatajar (now part of the Oromia Region, near the Awash River), Zara Yaqob was the youngest son of Dawit I and his youngest wife, Igzi Kebra.
- [d6s4] The British expert on Ethiopia, Edward Ullendorff, stated that Zara Yaqob "was unquestionably the greatest ruler Ethiopia had seen since Ezana, during the heyday of Aksumite power, and none of his successors on the throne – excepted only the emperors Menelik II and Haile Selassie – can be compared to him."
- [d6s5] Paul B. Henze repeats the tradition that the jealousy of his older brother Tewodros I forced the courtiers to take Zara Yaqob to Tigray where he was brought up in secret, and educated in Axum and at the monastery of Debre Abbay.
- [d6s6] While admitting that this tradition "is invaluable as providing a religious background for Zar'a-Ya'iqob's career", Taddesse Tamrat dismisses this story as "very improbable in its details.
- [d6s7] " The professor notes that Zara Yaqob wrote in his "Mashafa Berhan" that "he was brought down from the royal prison of Mount Gishan only on the eve of his accession to the throne."

**d7: Kaya Alp**

- [d7s0] Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

**d8: John Westley**

- [d8s0] Rev. John Westley( 1636 – 78) was an English nonconformist minister.
- [d8s1] He was the grandfather of John Wesley( founder of Methodism).

**d9: Prithvipati Shah**

- [d9s0] Prithvipati Shah( ?–1716) was the king of the Gorkha Kingdom in the Indian subcontinent, present- day Nepal.
- [d9s1] He was the grandfather of Nara Bhupal Shah.

**d10: Lyon Cohen**

- [d10s0] Lyon Cohen( 1868–1937) was a Polish- born Canadian businessman and a philanthropist.
- [d10s1] He was the grandfather of singer/ poet Leonard Cohen.

## 22. 2wikimultihopqa_36df83c7084b11ebbd56ac1f6bf848b6

原位置：`train` 第 22 题 · 全局第 22 题 · `sample_id: 2wikimultihopqa_36df83c7084b11ebbd56ac1f6bf848b6`

Question: Who was born earlier, Eberhard Nestle or Zélia Cardoso De Mello?

Note:

Type: comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | birth date of Eberhard Nestle | False | () |
| u2 | birth date of Zélia Cardoso De Mello | False | () |
| u3 | who was born earlier | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | date of birth of Eberhard Nestle | False | [] | May 1, 1851 | [['d7s0']] |
| u2 | date of birth of Zélia Cardoso de Mello | False | [] | September 20, 1953 | [['d5s0']] |
| u3 | which of Eberhard Nestle and Zélia Cardoso de Mello was born earlier | True | ['u1', 'u2'] | Eberhard Nestle | [[]] |

### Source documents (reference only)

**d1: José Manuel de Mello**

- [d1s0] José Manuel de Mello( December 8, 1927 – September 16, 2009), was a Portuguese businessman who founded the conglomerate Grupo José de Mello.
- [d1s1] He was the heir of an older industrial conglomerate, Companhia União Fabril( CUF), which had been founded by his grandfather Alfredo da Silva.
- [d1s2] José Manuel started to work for CUF until the Carnation Revolution military coup in Lisbon, on April 24, 1974.
- [d1s3] With the pro-communist inspiration of the radical events that followed the coup, José Manuel de Mello had to leave the country in 1975.
- [d1s4] Some years later, as democracy and modern capitalism prevailed in post-revolutionary Portugal, Mello, like many other political refugees of the entrepreneurial class, returned to his country.
- [d1s5] He then resumed his business activities and ultimately built a business conglomerate- the Grupo José de Mello with strong interests on motorway infrastructure, healthcare and chemicals.
- [d1s6] He had 12 children.

**d2: Bernardo Alves**

- [d2s0] Bernardo Cardoso de Resende Alves( born November 20, 1974, Belo Horizonte) is a show jumping rider from Brazil.

**d3: Adriana Cardoso de Castro**

- [d3s0] Adriana Cardoso de Castro( born 29 October 1990) is a Brazilian handballer for BM Bera Bera and the Brazilian national team.

**d4: Estêvão Cardoso de Avellar**

- [d4s0] Estêvão Cardoso de Avellar( November 4, 1917 – December 3, 2009) was a Brazilian bishop of the Roman Catholic Church.

**d5: Zélia Cardoso de Mello**

- [d5s0] Zélia Maria Cardoso de Mello( born September 20, 1953 in São Paulo) served as Brazil's Minister of Economy from 1990 to 1991 under Fernando Collor de Mello( no relation).
- [d5s1] She was married to Brazilian comedian Chico Anysio, with whom she has two children, Rodrigo and Victoria.
- [d5s2] The couple divorced in 1998.
- [d5s3] Zélia Cardoso de Mello worked in the academic, public and private sectors in Brazil.
- [d5s4] She graduated from FEA- USP where she also got her PhD degree in Economics.
- [d5s5] She was a professor at the University of São Paulo for almost 20 years
- [d5s6] Her political career began in 1986 when Dilson Funaro, the Minister of Finance of Brazil, invited her to join his" Economic Advisory Team" as Director of the National Treasure Dept. In 1990 Cardoso de Mello was appointed the National Minister of Economy, Finance and Planning of Brazil under president Fernando Collor de Mello.
- [d5s7] After significant criticism, she resigned this position in May 1991.
- [d5s8] In 1991, she released a biography," Zelia, A Passion".
- [d5s9] It became a best- seller, perhaps because, according to a review," It says little about tax reform and inflation, but a lot about Cardoso's sexual exploits in office."
- [d5s10] In 1995 she moved to New York City and became a visiting scholar at the" Institute of Latin America and Iberian Studies" at Columbia University.
- [d5s11] Since 1998, Cardoso de Mello has served executive positions at several major financial advisory companies focused on Brazil, including Global Access Investments, Orix and Lily Pond Capital.
- [d5s12] Her academic career was entirely accomplished in the School of Business and Economics at the University of São Paulo, where she received her college degree, Doctorate, and served as university professor.
- [d5s13] She is currently a partner at New York- based Aquila Associates.

**d6: Anthony de Mello**

- [d6s0] Anthony de Mello, also known as Tony de Mello( 4 September 1931 – 2 June 1987), was an Indian Jesuit priest and psychotherapist.
- [d6s1] A spiritual teacher, writer, and public speaker, de Mello wrote several books on spirituality and hosted numerous spiritual retreats and conferences.
- [d6s2] He continues to be known for his storytelling which drew from the various mystical traditions of both East and West and for introducing many people in the West to mindfulness- based practices he sometimes called" awareness prayer."

**d7: Eberhard Nestle**

- [d7s0] Eberhard Nestle( May 1, 1851, Stuttgart – March 9, 1913, Stuttgart) was a German biblical scholar, textual critic, orientalist, editor of Novum Testamentum Graece, and the father of Erwin Nestle.

**d8: Luiz Alberto de Araújo**

- [d8s0] Luiz Alberto Cardoso de Araújo( born 27 June 1987) is a Brazilian decathlete.

**d9: Milton Thiago de Mello**

- [d9s0] Milton
- [d9s1] Thiago de Mello better known as Doctor Milton
- [d9s2] Thiago de Mello( born February 5, 1916, in Rio de Janeiro) é um Veterinarian Physician the dean of Brazilian primatology.
- [d9s3] He is a strong voice for biological conservation of Brazil's megadiverse flora and fauna, as well as en example of professional and personal probity.
- [d9s4] As a professional Veterinarian Physician and zoological researcher, the Doutor Thiago de Mello is world- famous and has received awards and distinctions from many governments and organizations, such as from the “ Comité Français de l’ Association Mondiale Vétérinaire ”, “ The World Veterinary Epidemiology Society ”, the “ Sociedad Colombiana de Primatologia ” and “ The John Guggenhiem Memorial ”.
- [d9s5] He is an honorary member of the Royal Academy of Veterinary Sciences of London, the American Academy of Microbiology, and the New York Academy of Sciences.
- [d9s6] He was awarded the Medal of Merit in Veterinary Medicine, as the highest level( Grã- Cruz).
- [d9s7] He is a consultant with the Pan-American Health Organization, and the Food and Agriculture Agency of the United Nations.
- [d9s8] He belongs to more than 30 Brazilian and international scientific societies, of which he has helped found 14 and served as an official of at least 12.
- [d9s9] He is the author of numerous books and over 150 scientific papers on primates, brucellosis, bubonic plague, medical mycology, the teaching of veterinary medicine, and the environmental crisis in Brazil and other countries.
- [d9s10] The recently founded Milton Thiago de Mello Environmental Institute, in Sobradinho, Distrito Federal, Brazil, is named after Thiago de Mello, also.
- [d9s11] Almost all Brazilian primatologists have, at one time or another, studied under Dr. Milton Thiago de Mello.
- [d9s12] He turned 100 in February 2016.

**d10: Jack de Mello**

- [d10s0] Jack de Mello( November 15, 1916 – April 27, 2019) was an American composer, arranger, producer, and recording artist from Hawaii.
- [d10s1] He was known for being a composer and advocate of Hawaiian music.
- [d10s2] Jack de Mello composed music for animated television series including" The Flintstones" and" The Jetsons."
- [d10s3] He was the father of Jon de Mello.

## 23. 2wikimultihopqa_36f59e640bdd11eba7f7acde48001122

原位置：`train` 第 23 题 · 全局第 23 题 · `sample_id: 2wikimultihopqa_36f59e640bdd11eba7f7acde48001122`

Question: When was the director of film Artists Under The Big Top: Perplexed born?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of film Artists Under The Big Top: Perplexed | False | () |
| u2 | birth date of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Artists Under the Big Top: Perplexed | False | [] | Alexander Kluge | [['d3s1']] |
| u2 | date of birth of {u1} | True | ['u1'] | 14 February 1932 | [['d8s0']] |

### Source documents (reference only)

**d1: Terence Robinson**

- [d1s0] Terence D. Robinson( date of birth and death unknown) was a male wrestler who competed for England.

**d2: Down Under the Big Top**

- [d2s0] Down Under the Big Top is a 1996 American movie.
- [d2s1] It is the Newsboys' first feature film and was released as a direct-to-video title.
- [d2s2] The film also represents the first screenplay ever written by director Steve Taylor.

**d3: Artists Under the Big Top: Perplexed**

- [d3s0] Artists in the Big Top:
- [d3s1] Perplexed is a 1968 West German film written and directed by Alexander Kluge.
- [d3s2] The film is made in a collage style, featuring newsreels and quotations from philosophers alongside the story of a failing circus whose owner, Leni( Hannelore Hoger), must decide whether her dream of a new kind of circus is too optimistic.
- [d3s3] The film is a symbolic representation of Kluge's own frustrations in trying to help stimulate the New German Cinema movement.

**d4: Ian Barry (director)**

- [d4s0] Ian Barry is an Australian director of film and TV.

**d5: Marko Kovač (director)**

- [d5s0] Marko Kovač( born 9 April 1981 in Belgrade, Yugoslavia, today Serbia) is Serbian architect and film director.
- [d5s1] In 2007. he graduated architecture at the University of Belgrade's School of Architecture.
- [d5s2] He is a member of Film Artists Association of Serbia.

**d6: Under the Big Top**

- [d6s0] Under the Big Top is a 1938 American film directed by Karl Brown.

**d7: Etan Boritzer**

- [d7s0] Etan Boritzer( born 1950) is an American writer of children ’s literature who is best known for his book" What is God?" first published in 1989.
- [d7s1] His best selling" What is?" illustrated children's book series on character education and difficult subjects for children is a popular teaching guide for parents, teachers and child- life professionals.
- [d7s2] Boritzer gained national critical acclaim after" What is God?" was published in 1989 although the book has caused controversy from religious fundamentalists for its universalist views.
- [d7s3] The other current books in the" What is?" series include
- [d7s4] What is Love?,
- [d7s5] What is Death?,
- [d7s6] What is Beautiful?,
- [d7s7] What is Funny?,
- [d7s8] What is Right?,
- [d7s9] What is Peace?,
- [d7s10] What is Money?,
- [d7s11] What is Dreaming?,
- [d7s12] What is a Friend?,
- [d7s13] What is True?,
- [d7s14] What is a Family?,
- [d7s15] What is a Feeling?"
- [d7s16] The series is now also translated into 15 languages.
- [d7s17] Boritzer was first published in 1963 at the age of 13 when he wrote an essay in his English class at Wade Junior High School in the Bronx, New York on the assassination of John F. Kennedy.
- [d7s18] His essay was included in a special anthology by New York City public school children compiled and published by the New York City Department of Education.
- [d7s19] Boritzer now lives in Venice, California and maintains his publishing office there also.
- [d7s20] He has helped numerous other authors to get published through" How to Get Your Book Published!" programs.
- [d7s21] Boritzer is also a yoga teacher who teaches regular classes locally and guest- teaches nationally.
- [d7s22] He is also recognized nationally as an erudite speaker on" The Teachings of the Buddha."

**d8: Alexander Kluge**

- [d8s0] Alexander Kluge( born 14 February 1932) is a German author, philosopher, academic and film director.

**d9: Brian Saunders (weightlifter)**

- [d9s0] Brian Saunders( date of birth and death unknown) was a male weightlifter who competed for England.

**d10: Theodred II (Bishop of Elmham)**

- [d10s0] Theodred II was a medieval Bishop of Elmham.
- [d10s1] The date of Theodred's consecration unknown, but the date of his death was sometime between 995 and 997.

## 24. 2wikimultihopqa_3ac87e2c0baf11ebab90acde48001122

原位置：`train` 第 24 题 · 全局第 24 题 · `sample_id: 2wikimultihopqa_3ac87e2c0baf11ebab90acde48001122`

Question: Who is Stephen Tomašević Of Bosnia's father-in-law?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | wife of Stephen Tomašević Of Bosnia | False | () |
| u2 | father of {u1}, Stephen Tomašević Of Bosnia's father-in-law | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | spouse of Stephen Tomašević of Bosnia | False | [] | Maria of Serbia | [['d1s2', 'd1s3'], ['d9s1'], ['d7s4'], ['d2s2']] |
| u2 | father of {u1}, Stephen Tomašević of Bosnia's father-in-law | True | ['u1'] | Lazar Branković | [['d9s1']] |

### Source documents (reference only)

**d1: Stephen Tomašević of Bosnia**

- [d1s0] Stephen Tomašević or Stephen II (Стјепан/Стефан Томашевић; died on 25 May 1463) was the last sovereign from the Bosnian Kotromanić dynasty, reigning as Despot of Serbia briefly in 1459 and as King of Bosnia from 1461 until 1463.
- [d1s1] Stephen's father, King Thomas, had great ambitions for him.
- [d1s2] An attempt to expand into Croatia proper by marrying Stephen to a wealthy noblewoman failed, and negotiations for a marital alliance with the Sforzas of Milan were abandoned when a more prestigious opportunity presented itself: marriage to the heiress Maria of Serbia.
- [d1s3] Celebrated in April 1459, it made Stephen the ruler of the remnants of the neighbouring country.
- [d1s4] The intent was to unite the Kingdom of Bosnia and the Serbian Despotate under Stephen to combat the expanding Ottoman Empire.
- [d1s5] Stephen's Catholicism made him unpopular in Orthodox Serbia.
- [d1s6] After ruling it for merely two months, he surrendered it to the encroaching Ottoman forces and fled back to his father's court, which earned him the contempt of the Hungarian king Matthias Corvinus and other Christian rulers in Europe.
- [d1s7] Stephen succeeded his father on the throne following the latter's death in July 1461 and became the first Bosnian king to receive a crown from the Holy See.
- [d1s8] The kingdom's existence, however, was increasingly threatened by the Ottomans.
- [d1s9] King Stephen had the unanimous support of his noblemen in resistance to the Ottomans, but not of the common people.
- [d1s10] He maintained an active correspondence with Pope Pius II, who forgave him for the loss of Serbia and worked with him to preserve Bosnia for Christendom.
- [d1s11] The Hungarian king was placated, but all Western monarchs contacted by Stephen refused to assist him.
- [d1s12] Confident that at least Matthias would come to his aid, Stephen refused to deliver the customary tribute to the Ottoman sultan
- [d1s13] Mehmed the Conqueror, which provoked an invasion.
- [d1s14] In May 1463, Mehmed marched into Bosnia, meeting little effective resistance, and captured Stephen, who was then beheaded.
- [d1s15] The execution marks the fall of the Kingdom of Bosnia to the Ottoman Empire.

**d2: Jerina Branković (wife of Gjon Kastrioti II)**

- [d2s0] Jerina Branković , or Irina (Ирина), was the wife of Gjon Kastrioti II.
- [d2s1] She was the third daughter of Lazar Branković and Helena Palaiologina.
- [d2s2] She had two sisters, Helen (Mary), wife of King Stephen Tomašević of Bosnia, and Milica, wife of Leonardo III Tocco of Epirus.
- [d2s3] Gjon Kastrioti II was the "conte di Spoleto" in 1485, and "duca di San Pietro" in Galatina in 1495.
- [d2s4] They had the following issue:

**d3: Catherine of Bosnia, Grand Princess of Hum**

- [d3s0] " For other people named Catherine of Bosnia, see Catherine of Bosnia( disambiguation)."
- [d3s1] Catherine of Bosnia( Bosnian:" Katarina Kotromanić Stjepanova")( b. 1294- d. 1355) was sister of Stephen II, Ban of Bosnia.

**d4: Peter Burroughs**

- [d4s0] Peter Burroughs( born 27 January 1947) is a British television and film actor, the director of Willow Management.
- [d4s1] He is the father- in- law of actor and TV presenter Warwick Davis.

**d5: Ludwig von Westphalen**

- [d5s0] Johann Ludwig von Westphalen( 11 July 1770 – 3 March 1842) was a liberal Prussian civil servant and the father- in- law of Karl Marx.

**d6: Ogawa Mataji**

- [d6s0] Viscount was a general in the early Imperial Japanese Army.
- [d6s1] He was also the father- in- law of Field Marshal Gen Sugiyama.

**d7: Milica Branković**

- [d7s0] Milica Branković (d. 1464) was Serbian princess and the first wife of Leonardo III Tocco, whom she married on 1 May 1463.
- [d7s1] She was a daughter of despot Lazar Branković of Serbia and Helena Palaiologina.
- [d7s2] Milica died in childbirth in 1464, while giving birth to Carlo III Tocco.
- [d7s3] Carlo III Tocco succeeded his father as titular ruler of Epirus (Arta) and Zakynthos.
- [d7s4] Her siblings were Maria, wife of King Stephen Tomašević of Bosnia and Jerina, wife of Gjon Kastrioti II.

**d8: John Adams (merchant)**

- [d8s0] John Adams( 1672 or 1673 – 1745) was an American- born Canadian merchant and member of the Nova Scotia Council.
- [d8s1] He was the father- in- law of Henry Newton( politician).

**d9: Maria of Serbia, Queen of Bosnia**

- [d9s0] Maria of Serbia (/Мара Бранковић; 1447 – 1500), christened Helena ("Jelena"/Јелена), was the last Queen of Bosnia and Despoina of Serbia.
- [d9s1] As the eldest daughter of the deceased Despot of Serbia Lazar Branković, the 12-year-old Helena was given in marriage to the Bosnian prince Stephen Tomašević in 1459.
- [d9s2] She then took the name Maria, while her husband obtained the title to Serbia through her.
- [d9s3] The country was lost to the Ottomans within a few months, and the couple fled to Bosnia.
- [d9s4] Maria's husband ascended the Bosnian throne in 1461, but two years later the kingdom too fell to the Ottomans and he was executed.
- [d9s5] The widowed queen avoided capture by fleeing to the coast.
- [d9s6] Having spent a few years in Venetian Dalmatia and possibly Hungary, Maria settled in Ottoman Greece at the court of her aunts Mara and Kantakouzene.
- [d9s7] Her string of conflicts and legal disputes with Kantakouzene, the Republic of Ragusa and Athonite monasteries earned her an ill reputation, with the monks describing her as an "evil woman".

**d10: Barthold A. Butenschøn Sr.**

- [d10s0] Hans Barthold Andresen Butenschøn( 27 December 1877 – 28 November 1971) was a Norwegian businessperson.
- [d10s1] He was born in Kristiania as a son of Nils August Andresen Butenschøn and Hanna Butenschøn, and grandson of Nicolay Andresen.
- [d10s2] Together with Mabel Anette Plahte( 1877 – 1973, a daughter of Frithjof M. Plahte) he had the son Hans Barthold Andresen Butenschøn Jr. and was through him the father- in- law of Ragnhild Butenschøn and grandfather of Peter Butenschøn.
- [d10s3] Through his daughter Marie Claudine he was the father- in- law of Joakim Lehmkuhl, through his daughter Mabel Anette he was the father- in- law of Harald Astrup( a son of Sigurd Astrup) and through his daughter Nini Augusta he was the father- in- law of Ernst Torp.
- [d10s4] He took commerce school and agricultural school.
- [d10s5] He was hired in the family company N. A. Andresen& Co, and became a co-owner in 1910.
- [d10s6] He eventually became chief executive officer.
- [d10s7] The bank changed its name to Andresens Bank in 1913 and merged with Bergens Kreditbank in 1920.
- [d10s8] The merger was dissolved later in the 1920s.
- [d10s9] He was also a landowner, owning Nedre Skøyen farm and a lot of land in Enebakk.
- [d10s10] He chaired the board of Nydalens Compagnie from 1926, having not been a board member before that.
- [d10s11] He also chaired the supervisory council of Forsikringsselskapet Viking and Nedre Glommen salgsforening, and was a supervisory council member of Filharmonisk Selskap.
- [d10s12] He was a member of the gentlemen's club SK Fram since 1890, and was proclaimed a lifetime member in 1964.
- [d10s13] He was buried in Enebakk.

## 25. 2wikimultihopqa_3d884fec0bdd11eba7f7acde48001122

原位置：`train` 第 25 题 · 全局第 25 题 · `sample_id: 2wikimultihopqa_3d884fec0bdd11eba7f7acde48001122`

Question: What is the place of birth of the director of film The Outsider (2018 Film)?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of The Outsider (2018 Film) | False | () |
| u2 | place of birth of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film The Outsider (2018 film) | False | [] | Martin Zandvliet | [['d4s0']] |
| u2 | place of birth of {u1} | True | ['u1'] | Fredericia | [['d2s0']] |

### Source documents (reference only)

**d1: Peter Levin**

- [d1s0] Peter Levin is an American director of film, television and theatre.

**d2: Martin Zandvliet**

- [d2s0] Martin Pieter Zandvliet( born 7 January 1971 in Fredericia) is a Danish film director and screenwriter.

**d3: Brian Kennedy (gallery director)**

- [d3s0] Brian Patrick Kennedy( born 5 November 1961) is an Irish- born art museum director who has worked in Ireland and Australia, and now lives and works in the United States.
- [d3s1] He is currently the director of the Peabody Essex Museum.
- [d3s2] He was the director of the Toledo Museum of Art in Ohio from 2010 to 2019.
- [d3s3] He was the director of the Hood Museum of Art from 2005 to 2010, and the National Gallery of Australia( Canberra) from 1997- 2004.

**d4: The Outsider (2018 film)**

- [d4s0] The Outsider is a 2018 Japanese-American crime drama thriller film directed by Martin Zandvliet and written by Andrew Baldwin.
- [d4s1] It stars Jared Leto, Tadanobu Asano, Kippei Shiina, Shiori Kutsuna, and Emile Hirsch and follows an American who becomes a member of the Japanese yakuza.
- [d4s2] The film was released by Netflix on March 9, 2018, and received generally unfavorable reviews from critics.

**d5: Barbara Blair**

- [d5s0] Barbara Blair was an American film actress.
- [d5s1] She played leading and supporting roles in several British films including" The Outsider"( 1939).

**d6: Jesse E. Hobson**

- [d6s0] Jesse Edward Hobson( May 2, 1911 – November 5, 1970) was the director of SRI International from 1947 to 1955.
- [d6s1] Prior to SRI, he was the director of the Armour Research Foundation.

**d7: The Outsider (1939 film)**

- [d7s0] The Outsider is a 1939 British drama film directed by Paul L. Stein and starring George Sanders, Mary Maguire and Barbara Blair.
- [d7s1] The screenplay concerns an osteopath who cures one of his patients with whom he has fallen in love.
- [d7s2] It is a remake of the 1931 film" The Outsider" and was based on the 1923 play of the same name by Dorothy Brandon.
- [d7s3] The film was shot at Elstree Studios with sets designed by the art director Cedric Dawe.

**d8: Olav Aaraas**

- [d8s0] Olav Aaraas( born 10 July 1950) is a Norwegian historian and museum director.
- [d8s1] He was born in Fredrikstad.
- [d8s2] From 1982 to 1993 he was the director of Sogn Folk Museum, from 1993 to 2010 he was the director of Maihaugen and from 2001 he has been the director of the Norwegian Museum of Cultural History.
- [d8s3] In 2010 he was decorated with the Royal Norwegian Order of St. Olav.

**d9: Ian Barry (director)**

- [d9s0] Ian Barry is an Australian director of film and TV.

**d10: The Outsider (1926 film)**

- [d10s0] The Outsider is a 1926 American 60- minute silent drama film directed by Rowland V. Lee and starring Jacqueline Logan, Lou Tellegen and Walter Pidgeon.
- [d10s1] It was based on the 1923 play" The Outsider" by Dorothy Brandon.
- [d10s2] The screenplay is set in London and concerns an unorthodox doctor who cures a patient with whom he is in love.
- [d10s3] The film was remade as a British sound film" The Outsider" in 1931 which was released by Metro Goldwyn Mayer.

## 26. 2wikimultihopqa_43110efa08a311ebbd7bac1f6bf848b6

原位置：`train` 第 26 题 · 全局第 26 题 · `sample_id: 2wikimultihopqa_43110efa08a311ebbd7bac1f6bf848b6`

Question: Which film has the director died earlier, The Son Of Dr. Jekyll or Man From Montana?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of The Son Of Dr. Jekyll | False | () |
| u2 | death date of {u1} | False | ('u1',) |
| u3 | director of Man From Montana | False | () |
| u4 | death date of {u3} | False | ('u3',) |
| u5 | which film's director died earlier | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film The Son of Dr. Jekyll | False | [] | Seymour Friedman | [['d7s0']] |
| u2 | date of death of {u1} | False | ['u1'] | April 2, 2003 | [['d5s0']] |
| u3 | director of film Man from Montana | False | [] | Ray Taylor | [['d3s0']] |
| u4 | date of death of {u3} | False | ['u3'] | 15 February 1952 | [['d2s0']] |
| u5 | which of The Son of Dr. Jekyll and Man from Montana has the director who died earlier | True | ['u2', 'u4'] | Man from Montana | [[]] |

### Source documents (reference only)

**d1: Dr. Pyckle and Mr. Pryde**

- [d1s0] Dr. Pyckle and Mr. Pryde is a 1925 silent, black- and- white comedy film, directed by Scott Pembroke and Joe Rock( also the producer).
- [d1s1] The film itself is both a spoof of the previous Dr. Jekyll and Mr. Hyde films( e.g." Dr. Jekyll and Mr. Hyde"( 1912) and" Dr. Jekyll and Mr. Hyde"( 1920)) and the well- famed novel by Robert Louis Stevenson" Strange Case of Dr Jekyll and Mr Hyde."
- [d1s2] The film stars Stan Laurel as the title characters.

**d2: Ray Taylor (director)**

- [d2s0] Ray Taylor (1 December 1888 – 15 February 1952) was an American film director.
- [d2s1] He directed 159 films between 1926 and 1949.
- [d2s2] His debut was the 1926 film serial "Fighting with Buffalo Bill".

**d3: Man from Montana**

- [d3s0] Man from Montana is a 1941 American Western film directed by Ray Taylor and written by Bennett Cohen.
- [d3s1] The film stars Johnny Mack Brown, Fuzzy Knight, Billy Lenhart, Kenneth Brown, Jean Brooks and Nell O' Day.
- [d3s2] The film was released on September 5, 1941, by Universal Pictures.

**d4: Dr. Jekyll y el Hombre Lobo**

- [d4s0] Dr. Jekyll y el Hombre Lobo( Dr. Jekyll and the Wolfman), also known as Dr. Jekyll and the Werewolf, is a 1971 Spanish horror film, the sixth in the series, about the werewolf Count Waldemar Daninsky, played by Paul Naschy.
- [d4s1] It was followed by a sequel," El Retorno de Walpurgis".

**d5: Seymour Friedman**

- [d5s0] Seymour Friedman( August 17, 1917 – April 2, 2003) was an American film director.
- [d5s1] He later worked as a production manager in television.
- [d5s2] Friedman began his career as an assistant director, before enlisting for military service following America's entry into World War II.
- [d5s3] He directed his first film," Trapped by Boston Blackie", in 1948.
- [d5s4] Like many of the other films he directed, it was a low- budget series film.
- [d5s5] In the early 1950s, Friedman went to Britain to make a couple of films, before returning to Hollywood.
- [d5s6] He directed his last film in 1956, and switched to working entirely in television.

**d6: Abbott and Costello Meet Dr. Jekyll and Mr. Hyde**

- [d6s0] Abbott and Costello Meet Dr. Jekyll and Mr. Hyde is a 1953 American horror comedy film directed by Charles Lamont and starring the comedy team of Abbott and Costello, and co-stars Boris Karloff.
- [d6s1] Inspired by the 1886 novella" The Strange Case of Dr. Jekyll and Mr. Hyde" by Robert Louis Stevenson, the film follows the story of two American detectives visiting Edwardian London who become involved with the hunt for Dr. Jekyll, who is responsible for a series of murders.

**d7: The Son of Dr. Jekyll**

- [d7s0] The Son of Dr. Jekyll is a 1951 American horror film directed by Seymour Friedman and starring Louis Hayward, Jody Lawrance and Alexander Knox.
- [d7s1] The film is a continuation of Robert Louis Stevenson's original classic 1886 novella" Strange Case of Dr. Jekyll and Mr. Hyde".
- [d7s2] Jack Pollexfen, the scriptwriter of this film, wrote and produced a sequel in the same vein," The Daughter of Dr. Jekyll"( 1957), starring Gloria Talbott.

**d8: Dr. Jekyll and Sister Hyde**

- [d8s0] Dr. Jekyll and Sister Hyde is a 1971 British horror film directed by Roy Ward Baker based on the novella "Strange Case of Dr Jekyll and Mr Hyde" by Robert Louis Stevenson.
- [d8s1] The film was made by British studio Hammer Film Productions and was their third adaptation of the story after "The Ugly Duckling" and "The Two Faces of Dr. Jekyll".
- [d8s2] The film is notable for showing Jekyll transform into a female Hyde; it also incorporates into the plot aspects of the historical Jack the Ripper and Burke and Hare cases.
- [d8s3] The two characters were played by the film's stars, Ralph Bates and Martine Beswick.

**d9: My Friend, Dr. Jekyll**

- [d9s0] My Friend, Dr. Jekyll, is a 1960 Italian comedy film directed by Marino Girolami.
- [d9s1] It is a parody of the Robert Louis Stevenson's novella" Strange Case of Dr Jekyll and Mr Hyde".

**d10: The Daughter of Dr. Jekyll**

- [d10s0] Daughter of Dr. Jekyll is a low- budget black- and- white 1957 American horror film produced by Jack Pollexfen, directed by Edgar G. Ulmer and released by Allied Artists.
- [d10s1] The film is a variation on the 1886 gothic novella" Strange Case of Dr. Jekyll and Mr. Hyde" by Robert Louis Stevenson.
- [d10s2] It stars Gloria Talbott, John Agar and Arthur Shields.
- [d10s3] In the film, Janet Smith( Gloria Talbott) learns that she is not only the daughter of the infamous Dr. Henry Jekyll, but is convinced by her guardian, Dr. Lomas( Arthur Shields), that she has inherited her father's transformative condition.
- [d10s4] Janet begins to believe that she turns into a monster after two local woman are found horribly killed and nearly takes her own life because of it.
- [d10s5] However, all is not what it seems.
- [d10s6] " Daughter of Dr. Jekyll" was released in theaters in the US on a double bill with" The Cyclops".

## 27. 2wikimultihopqa_461f74380bdc11eba7f7acde48001122

原位置：`train` 第 27 题 · 全局第 27 题 · `sample_id: 2wikimultihopqa_461f74380bdc11eba7f7acde48001122`

Question: Where was the director of film Jîn born?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of film Jîn | False | () |
| u2 | birthplace of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Jîn | False | [] | Reha Erdem | [['d6s0']] |
| u2 | place of birth of {u1} | True | ['u1'] | Istanbul | [['d1s0']] |

### Source documents (reference only)

**d1: Reha Erdem**

- [d1s0] Reha Erdem( born 1960 in Istanbul) is a Turkish film director and screenwriter.

**d2: Jason Moore (director)**

- [d2s0] Jason Moore( born October 22, 1970) is an American director of film, theatre and television.

**d3: Brian Kennedy (gallery director)**

- [d3s0] Brian Patrick Kennedy( born 5 November 1961) is an Irish- born art museum director who has worked in Ireland and Australia, and now lives and works in the United States.
- [d3s1] He is currently the director of the Peabody Essex Museum.
- [d3s2] He was the director of the Toledo Museum of Art in Ohio from 2010 to 2019.
- [d3s3] He was the director of the Hood Museum of Art from 2005 to 2010, and the National Gallery of Australia( Canberra) from 1997- 2004.

**d4: Peter Levin**

- [d4s0] Peter Levin is an American director of film, television and theatre.

**d5: Ian Barry (director)**

- [d5s0] Ian Barry is an Australian director of film and TV.

**d6: Jîn**

- [d6s0] Jîn (in Kurdish it means "Woman", Jin in English) is a 2013 Turkish-German movie directed by Reha Erdem.
- [d6s1] The movie is about a Kurdish guerilla fighter who deserted her military unit aiming at leaving the conflict region (Eastern Turkey) for the city of Izmir.

**d7: Jesse E. Hobson**

- [d7s0] Jesse Edward Hobson( May 2, 1911 – November 5, 1970) was the director of SRI International from 1947 to 1955.
- [d7s1] Prior to SRI, he was the director of the Armour Research Foundation.

**d8: Dana Blankstein**

- [d8s0] Dana Blankstein- Cohen( born March 3, 1981) is the director of the Israeli Academy of Film and Television.
- [d8s1] She is a film director, and an Israeli culture entrepreneur.

**d9: Olav Aaraas**

- [d9s0] Olav Aaraas( born 10 July 1950) is a Norwegian historian and museum director.
- [d9s1] He was born in Fredrikstad.
- [d9s2] From 1982 to 1993 he was the director of Sogn Folk Museum, from 1993 to 2010 he was the director of Maihaugen and from 2001 he has been the director of the Norwegian Museum of Cultural History.
- [d9s3] In 2010 he was decorated with the Royal Norwegian Order of St. Olav.

**d10: S. N. Mathur**

- [d10s0] S.N. Mathur was the Director of the Indian Intelligence Bureau between September 1975 and February 1980.
- [d10s1] He was also the Director General of Police in Punjab.

## 28. 2wikimultihopqa_481d8b620baf11ebab90acde48001122

原位置：`train` 第 28 题 · 全局第 28 题 · `sample_id: 2wikimultihopqa_481d8b620baf11ebab90acde48001122`

Question: Who is Catherine Of Hungary, Queen Of Serbia's mother-in-law?

Note:

Type: bridge · fallback: False · SFT snapshots: 7

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | husband of Catherine Of Hungary, Queen Of Serbia | False | () |
| u2 | mother of {u1}, Catherine Of Hungary, Queen Of Serbia's mother-in-law | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | spouse of Catherine of Hungary, Queen of Serbia | False | [] | Stefan Dragutin | [['d3s1'], ['d5s4']] |
| u2 | mother of {u1}, Catherine of Hungary's mother-in-law | True | ['u1'] | Helen of Anjou | [['d5s3']] |

### Source documents (reference only)

**d1: Eldon Howard**

- [d1s0] Eldon Howard was a British screenwriter.
- [d1s1] She was the mother- in- law of Edward J. Danziger and wrote a number of the screenplays for films by his company Danziger Productions.

**d2: Marian Shields Robinson**

- [d2s0] Marian Lois Robinson( née Shields; born July 29, 1937) is the mother of Michelle Obama, former First Lady of the United States, and Craig Robinson, a basketball executive, and the mother- in- law of former U.S. President Barack Obama.

**d3: Catherine of Hungary, Queen of Serbia**

- [d3s0] Catherine of Hungary("/ Katalina"; c. 1256 – after 1314) was the second daughter of Stephen V of Hungary and his wife Queen Elizabeth, daughter of Seyhan, chieftain of the Cumans.
- [d3s1] Catherine became Queen consort of Serbia by her marriage to Stephen Dragutin of Serbia.

**d4: Wilhelmine Amalia of Brunswick-Lüneburg**

- [d4s0] Wilhelmine Amalia of Brunswick- Lüneburg( 21 April 1673 – 10 April 1742) was Holy Roman Empress, Queen of the Germans, Queen of Hungary, Queen of Bohemia, Archduchess consort of Austria etc. as the spouse of Joseph I, Holy Roman Emperor.

**d5: Stefan Dragutin**

- [d5s0] "Stefan" Dragutin (1244 – 12 March 1316) was King of Serbia from 1276 to 1282.
- [d5s1] From 1282, he ruled a separate kingdom which included northern Serbia, and (from 1284)
- [d5s2] the neighboring Hungarian banates (or border provinces), for which he was unofficially styled as "King of Syrmia".
- [d5s3] He was the eldest son of King Stefan Uroš I of Serbia and Helen of Anjou.
- [d5s4] He received the title of "young king" in token of his right to succeed his father after a peace treaty between Uroš I and Béla IV of Hungary who was the grandfather of Dragutin's wife, Catherine, in 1268.
- [d5s5] He rebelled against his father and forced him to abdicate with Hungarian assistance in 1282.
- [d5s6] Dragutin abandoned
- [d5s7] Uroš
- [d5s8] I's centralizing policy and ceded large territories to his mother in appanage.
- [d5s9] After a riding accident, he abdicated in favor of his brother, Milutin in 1282, but he retained the northern regions of Serbia along the Hungarian border.
- [d5s10] Two years later, his brother-in-law, Ladislaus IV of Hungary, granted him three banatesMačva (or "Sirmia ulterior"), Usora and Solito him.
- [d5s11] He was the first Serbian monarch to rule Belgrade.
- [d5s12] With his brother's support, he also occupied the Banate of Braničevo in 1284 or 1285.
- [d5s13] Dragutin was in theory a vassal both to his brother (for his Serbian territories), and to the Hungarian monarchs (for the four banates), but he actually ruled his realm as an independent ruler from the 1290s.
- [d5s14] His conflicts with Milutin developed into an open war in 1301 and he made frequent raids against the neighboring Hungarian lords from 1307.
- [d5s15] Most of the Serbian noblemen supported Dragutin, but he was forced to make peace with Milutin after Milutin's mercenaries routed him in 1311 or 1312.
- [d5s16] Before his death, he entered into a monastery and died as the monk Teokist.
- [d5s17] In the list of Serbian saints, Dragutin is venerated on 12 November or 30 October (Old Style and New Style dates).

**d6: Slavica Đukić Dejanović**

- [d6s0] Slavica Đukić Dejanović( born 4 July 1951) is a Serbian politician, current Minister without portfolio in the Government of Serbia, and former Minister of Health in the Government of Serbia, acting Head of State of Serbia and President of the National Assembly of Serbia, and a long- time member of the Socialist Party of Serbia.
- [d6s1] Dejanović is the second woman at the head of the National Assembly of Serbia, after Nataša Mićić, who was President of Parliament 2001- 2004, and the first one in the independent Serbia.
- [d6s2] In that role she was also the Acting President of Serbia following the resignation of Boris Tadić in 2012 and was the first woman to hold the post of Head of State of Serbia since independence in 2006.

**d7: Priscilla Pointer**

- [d7s0] Priscilla Marie Pointer( born May 18, 1924) is an American stage, film and television character actress.
- [d7s1] She began her career in the theater, including productions on Broadway.
- [d7s2] Later, Pointer moved to Hollywood to act in films and on television.
- [d7s3] She is the mother of Amy Irving, therefore making her the former mother- in- law of filmmakers Steven Spielberg and Bruno Barreto and the mother- in- law of documentary filmmaker Kenneth Bowser, Jr.

**d8: Catherine of Hungary, Duchess of Świdnica**

- [d8s0] Catherine of Hungary( died 1355) was a daughter of King Charles I of Hungary.
- [d8s1] Her mother is uncertain.
- [d8s2] She was a member of the House of Anjou and was a Hungarian princess.

**d9: Maria Thins**

- [d9s0] Maria Thins( c. 1593 – 27 December 1680) was the mother- in- law of Johannes Vermeer and a member of the Gouda Thins family.

**d10: Vera Miletić**

- [d10s0] Vera Miletić (Serbian Cyrillic: Вера Милетић; 8 March 1920 – 7 September 1944) was a Serbian student and soldier.
- [d10s1] She was notable for being the mother of Mira Marković, posthumously making her the mother-in-law of Serbian president Slobodan Milošević.

## 29. 2wikimultihopqa_485a0492085911ebbd5bac1f6bf848b6

原位置：`train` 第 29 题 · 全局第 29 题 · `sample_id: 2wikimultihopqa_485a0492085911ebbd5bac1f6bf848b6`

Question: Were Glenn Walker (footballer, born 1998) and Eddie Deezen from the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of Glenn Walker (footballer, born 1998) | False | () |
| u2 | country of Eddie Deezen | False | () |
| u3 | whether Glenn Walker (footballer, born 1998) and Eddie Deezen are from the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | nationality of Glenn Walker (footballer, born 1998) | False | [] | Norwegian | [['d3s0']] |
| u2 | nationality of Eddie Deezen | False | [] | American | [['d4s0']] |
| u3 | whether Glenn Walker (footballer, born 1998) and Eddie Deezen are from the same country | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Khalid Mohammed (footballer)**

- [d1s0] Khalid Abdi Mohammed( born 1998) is an English footballer who played for Bury as a midfielder.

**d2: Ruairidh Campbell**

- [d2s0] Ruairidh Campbell( born 1998) is a Scottish professional rugby union referee who represents the Scottish Rugby Union.

**d3: Glenn Walker (footballer, born 1998)**

- [d3s0] Glenn Daniel Rogstad Walker( born 17 June 1998) is a Norwegian professional footballer who plays for Hødd on loan from Ranheim, as a defender.
- [d3s1] He played youth football for Stjørdals- Blink and Rosenborg.
- [d3s2] Done with his junior years, he joined the city's number two team Ranheim ahead of the 2018 season.
- [d3s3] Facing scarce first- team action, he was loaned to his childhood club Stjørdals- Blink in the summer transfer window of 2018.

**d4: Eddie Deezen**

- [d4s0] Edward Harry Deezen( born March 6, 1957) is an American actor, voice actor and comedian best known for his bit parts as nerd characters in 1970s and 1980s films such as" GreaseGrease 2 Midnight Madness I Wanna Hold Your Hand 1941" and" War Games", as well as for larger and starring roles in a number of independent cult films, including" Surf II: The End of the Trilogy Mob BossBeverly Hills Vamp" and" Teenage Exorcist".
- [d4s1] As a voice actor, he is recognized for his distinctively high- pitched and nasal voice, which has been used for the characters of Mandark in the Cartoon Network series" Dexter's Laboratory", Snipes the Magpie in" Rock- a- Doodle", Ned in" Kim Possible", and the Know- It- All Kid in" The Polar Express".

**d5: Glenn D. Walker**

- [d5s0] Glenn D. Walker( January 21, 1916 — May 3, 2002) was a lieutenant general in the United States Army.
- [d5s1] He was notable as commander of the 4th Infantry Division, First United States Army, I Corps, and adjutant general of the Mississippi National Guard.

**d6: Stella Kunkat**

- [d6s0] Stella Kunkat( born 1998) is a German actress.

**d7: Liza Jane (singer)**

- [d7s0] Liza Jane( born 1998) is an American singer- songwriter.
- [d7s1] Her first album is titled" We can start a fire".

**d8: Breana Geering**

- [d8s0] Breana Geering( born 1998) is a goofy- footed Canadian skateboarder.

**d9: Karin Kei Nagano**

- [d9s0] Karin Kei Nagano( born 1998) is an American pianist.

**d10: Tyler French**

- [d10s0] Tyler Jay French( born 1998/1999) is an English professional footballer who plays for Bradford City, as a central defender.

## 30. 2wikimultihopqa_4c0857900bda11eba7f7acde48001122

原位置：`train` 第 30 题 · 全局第 30 题 · `sample_id: 2wikimultihopqa_4c0857900bda11eba7f7acde48001122`

Question: Where was the place of death of the director of film Old Clothes?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of film Old Clothes | False | () |
| u2 | place of death of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Old Clothes | False | [] | Edward F. Cline | [['d2s0']] |
| u2 | place of death of {u1} | True | ['u1'] | Hollywood | [['d7s1']] |

### Source documents (reference only)

**d1: Too Fat Too Furious**

- [d1s0] Too Fat Too Furious is a 2005 Dutch action comedy film.
- [d1s1] It is a remake of the Danish film" Old Men in New Cars" and received a Golden Film for 100,000 visitors.

**d2: Old Clothes**

- [d2s0] Old Clothes is a 1925 American silent drama film directed by Edward F. Cline and starring Jackie Coogan and Joan Crawford.
- [d2s1] This was the first film in which Crawford was credited with her new name — Joan Crawford.
- [d2s2] She had been renamed by the studio, who deemed her birth name, Lucille LeSueur, as sounding unfit for a movie star.

**d3: Peter Levin**

- [d3s0] Peter Levin is an American director of film, television and theatre.

**d4: Olav Aaraas**

- [d4s0] Olav Aaraas( born 10 July 1950) is a Norwegian historian and museum director.
- [d4s1] He was born in Fredrikstad.
- [d4s2] From 1982 to 1993 he was the director of Sogn Folk Museum, from 1993 to 2010 he was the director of Maihaugen and from 2001 he has been the director of the Norwegian Museum of Cultural History.
- [d4s3] In 2010 he was decorated with the Royal Norwegian Order of St. Olav.

**d5: Brian Kennedy (gallery director)**

- [d5s0] Brian Patrick Kennedy( born 5 November 1961) is an Irish- born art museum director who has worked in Ireland and Australia, and now lives and works in the United States.
- [d5s1] He is currently the director of the Peabody Essex Museum.
- [d5s2] He was the director of the Toledo Museum of Art in Ohio from 2010 to 2019.
- [d5s3] He was the director of the Hood Museum of Art from 2005 to 2010, and the National Gallery of Australia( Canberra) from 1997- 2004.

**d6: Ian Barry (director)**

- [d6s0] Ian Barry is an Australian director of film and TV.

**d7: Edward F. Cline**

- [d7s0] Edward Francis Cline ("Eddie") (November 4, 1891 – May 22, 1961) was an American screenwriter, actor, writer and director best known for his work with comedians W. C. Fields and Buster Keaton.
- [d7s1] He was born in Kenosha, Wisconsin and died in Hollywood, California.

**d8: Jesse E. Hobson**

- [d8s0] Jesse Edward Hobson( May 2, 1911 – November 5, 1970) was the director of SRI International from 1947 to 1955.
- [d8s1] Prior to SRI, he was the director of the Armour Research Foundation.

**d9: Dana Blankstein**

- [d9s0] Dana Blankstein- Cohen( born March 3, 1981) is the director of the Israeli Academy of Film and Television.
- [d9s1] She is a film director, and an Israeli culture entrepreneur.

**d10: S. N. Mathur**

- [d10s0] S.N. Mathur was the Director of the Indian Intelligence Bureau between September 1975 and February 1980.
- [d10s1] He was also the Director General of Police in Punjab.
