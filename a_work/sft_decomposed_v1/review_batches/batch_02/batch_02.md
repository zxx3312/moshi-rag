# batch_02：人工审查（30 题）

全局题号 31–60；train 30 题 / dev 0 题。原训练/验证归属保持不变。

[返回分配索引](../README.md) · [完整对比报告](../../comparison_human.md)

**原则：新旧单元都合理时保留拆题器拆法，人工监督向新单元对齐。** 未标记的题目也需要核对答案和证据。现有标记是 AI 辅助审阅意见，不是人工验收结论。

审查人：________　完成日期：________

## 1. 2wikimultihopqa_4ef665780bda11eba7f7acde48001122

原位置：`train` 第 31 题 · 全局第 31 题 · `sample_id: 2wikimultihopqa_4ef665780bda11eba7f7acde48001122`

Question: When did the director of film Toto In Paris die?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of film Toto In Paris | False | () |
| u2 | death date of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Toto in Paris | False | [] | Camillo Mastrocinque | [['d1s0']] |
| u2 | date of death of {u1} | True | ['u1'] | 23 April 1969 | [['d10s0']] |

### Source documents (reference only)

**d1: Toto in Paris**

- [d1s0] Toto in Paris( also known as" Totò innamorato") is a 1958 Italian- French comedy film directed by Camillo Mastrocinque.

**d2: Sandrine Blancke**

- [d2s0] Sandrine Blancke( born 6 November 1978) is a Belgium French actress.
- [d2s1] She started her acting career as a child actor at the age of 13 in the 1991 film" Toto le héros".
- [d2s2] She was nominated for Best Supporting Actress at the 1st Magritte Awards.

**d3: Peter Levin**

- [d3s0] Peter Levin is an American director of film, television and theatre.

**d4: Theodred II (Bishop of Elmham)**

- [d4s0] Theodred II was a medieval Bishop of Elmham.
- [d4s1] The date of Theodred's consecration unknown, but the date of his death was sometime between 995 and 997.

**d5: Bill Smith (footballer, born 1897)**

- [d5s0] William Thomas Smith( born 9 April 1897, date of death unknown) was an English professional footballer.

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

**d7: Thomas Scott (diver)**

- [d7s0] Thomas Scott( 1907- date of death unknown) was an English diver.

**d8: Ian Barry (director)**

- [d8s0] Ian Barry is an Australian director of film and TV.

**d9: Toto in Madrid**

- [d9s0] Toto in Madrid is an Italian comedy film from 1959, directed by Steno, written by Vittorio Metz, starring Totò and Louis de Funès.
- [d9s1] The film is known under the titles:" Toto in Madrid"( English title)," Totò a MadridUn coup fumant"( France)," La culpa fue de Eva"( Spain).

**d10: Camillo Mastrocinque**

- [d10s0] Camillo Mastrocinque( 11 May 1901 – 23 April 1969) was an Italian film director and screenwriter.
- [d10s1] He directed 63 films between 1937 and 1968.
- [d10s2] He is known to horror film fans for directing" Terror in the Crypt"( 1964) starring Christopher Lee, and" An Angel for Satan"( 1966) starring Barbara Steele.

## 2. 2wikimultihopqa_533e994a0bdd11eba7f7acde48001122

原位置：`train` 第 32 题 · 全局第 32 题 · `sample_id: 2wikimultihopqa_533e994a0bdd11eba7f7acde48001122`

Question: What is the date of death of the director of film Muhammad Bin Tughluq (Film)?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of film Muhammad Bin Tughluq (Film) | False | () |
| u2 | date of death of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Muhammad bin Tughluq | False | [] | Cho Ramaswamy | [['d4s0'], ['d4s2']] |
| u2 | date of death of {u1} | True | ['u1'] | 7 December 2016 | [['d5s0']] |

### Source documents (reference only)

**d1: Ian Barry (director)**

- [d1s0] Ian Barry is an Australian director of film and TV.

**d2: Etan Boritzer**

- [d2s0] Etan Boritzer( born 1950) is an American writer of children ’s literature who is best known for his book" What is God?" first published in 1989.
- [d2s1] His best selling" What is?" illustrated children's book series on character education and difficult subjects for children is a popular teaching guide for parents, teachers and child- life professionals.
- [d2s2] Boritzer gained national critical acclaim after" What is God?" was published in 1989 although the book has caused controversy from religious fundamentalists for its universalist views.
- [d2s3] The other current books in the" What is?" series include
- [d2s4] What is Love?,
- [d2s5] What is Death?,
- [d2s6] What is Beautiful?,
- [d2s7] What is Funny?,
- [d2s8] What is Right?,
- [d2s9] What is Peace?,
- [d2s10] What is Money?,
- [d2s11] What is Dreaming?,
- [d2s12] What is a Friend?,
- [d2s13] What is True?,
- [d2s14] What is a Family?,
- [d2s15] What is a Feeling?"
- [d2s16] The series is now also translated into 15 languages.
- [d2s17] Boritzer was first published in 1963 at the age of 13 when he wrote an essay in his English class at Wade Junior High School in the Bronx, New York on the assassination of John F. Kennedy.
- [d2s18] His essay was included in a special anthology by New York City public school children compiled and published by the New York City Department of Education.
- [d2s19] Boritzer now lives in Venice, California and maintains his publishing office there also.
- [d2s20] He has helped numerous other authors to get published through" How to Get Your Book Published!" programs.
- [d2s21] Boritzer is also a yoga teacher who teaches regular classes locally and guest- teaches nationally.
- [d2s22] He is also recognized nationally as an erudite speaker on" The Teachings of the Buddha."

**d3: Abdul-Aziz bin Muhammad**

- [d3s0] Imam Abdul Aziz bin Muhammad bin Saud  (d. 1803) was the second ruler of the First Saudi State and son of Muhammad bin Saud.
- [d3s1] He was also the son-in-law of Muhammad bin Abdul Wahhab.
- [d3s2] He ruled from 1765 until 1803.

**d4: Muhammad bin Tughluq (film)**

- [d4s0] Muhammad bin Thughluq is a 1971 Indian Tamil-language comedy film directed and written by Cho Ramaswamy.
- [d4s1] It is the film version of the play of the same name.
- [d4s2] Both the play and the film were conceptualised, written and directed by Cho who also stars as the title character.
- [d4s3] The film is a satirical take on the then political and social affairs of India and is considered a fine portrayal of the political attitude existent till today.
- [d4s4] The title character's name is an allusion to the present day politics in India that can be compared with those of Tughluq's.
- [d4s5] It is believed in India that Tughluq, the sultan of Delhi in 14th century, was an unintelligent ruler especially for some of his decisions during his reign, including those of relocation of capital and experiments with coins.
- [d4s6] Thus, Cho found it to be a correct allusion to the present day political happenings.
- [d4s7] There are several dialogues in the film that mention these facts.

**d5: Cho Ramaswamy**

- [d5s0] Srinivasa Iyer Ramaswamy, better known as Cho Ramaswamy (5 October 1934 – 7 December 2016), was an Indian actor, comedian, character actor, editor, political satirist, playwright, dialogue writer, film director and lawyer in Tamil Nadu.

**d6: Bill Smith (footballer, born 1897)**

- [d6s0] William Thomas Smith( born 9 April 1897, date of death unknown) was an English professional footballer.

**d7: Muhammad bin Jamil Zeno**

- [d7s0] Muhammad bin Jamil Zeno( 1925 – Oct 2010) was an Islamic scholar and author.
- [d7s1] His name has also been transliterated differently in the English speaking world.
- [d7s2] Whilst his publishers Dar- Us- Salam in Riyadh translate it as' Muhammad bin Jamil Zeno', it is also rendered as Muhammad Bin/ Ibn Jamal/ Jamaal/ Jameel Zeeno/ Zaino/Zayno/Zaynoo/Zeenoo/Zino/Zainu.

**d8: Thomas Scott (diver)**

- [d8s0] Thomas Scott( 1907- date of death unknown) was an English diver.

**d9: Theodred II (Bishop of Elmham)**

- [d9s0] Theodred II was a medieval Bishop of Elmham.
- [d9s1] The date of Theodred's consecration unknown, but the date of his death was sometime between 995 and 997.

**d10: Abu Bakr Ibn Sayyid al-Nās**

- [d10s0] Muhammad bin Ahmad bin Abdullah bin Muhammad bin Yahya bin Muhammad bin Muhammad bin Sayyid al- Nas al- Ya'mari, better known as Abu Bakr Ibn Sayyid al- Nās, was a Medieval Muslim theologian.
- [d10s1] He was the grandfather of Fatḥ al- Din Ibn Sayyid al- Nās, though he died before ever meeting his grandson.

## 3. 2wikimultihopqa_55627704089111ebbd73ac1f6bf848b6 【保留新拆法｜重标人工标签】

原位置：`train` 第 33 题 · 全局第 33 题 · `sample_id: 2wikimultihopqa_55627704089111ebbd73ac1f6bf848b6`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_55627704089111ebbd73ac1f6bf848b6"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。
>
> **处理建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。
>
> **证据定位：** d7s0, d3s0, d1s0, d8s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Do both directors of films Jack'S The Boy and Autumn Sun share the same nationality?

Note:

Type: comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | nationality of director of Jack'S The Boy | False | () |
| u2 | nationality of director of Autumn Sun | False | () |
| u3 | whether both directors share the same nationality | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of Jack's the Boy | False | [] | Walter Forde | [['d7s0']] |
| u2 | nationality of {u1} | False | ['u1'] | British | [['d3s0']] |
| u3 | director of Autumn Sun | False | [] | Eduardo Mignogna | [['d1s0']] |
| u4 | nationality of {u3} | False | ['u3'] | Argentinian | [['d8s0']] |
| u5 | whether the directors of Jack's the Boy and Autumn Sun share the same nationality | True | ['u2', 'u4'] | no | [[]] |

### Source documents (reference only)

**d1: Autumn Sun**

- [d1s0] Autumn Sun is a 1996 Argentine drama film directed by Eduardo Mignogna and starring Norma Aleandro and Federico Luppi.
- [d1s1] It was written by Mignogna and Santiago Carlos Oves.
- [d1s2] Lita Stantic was the executive producer.

**d2: The Boy and the Dove**

- [d2s0] The Boy and the Dove is a 1961 Soviet short film directed by Andrey Konchalovsky.

**d3: Walter Forde**

- [d3s0] Walter Forde( born Thomas Seymour Woolford, 21 April 1898 – 7 January 1984) was a British actor, screenwriter and director.
- [d3s1] Born in Lambeth, South London in 1898, he directed over fifty films between 1919 from the silent era through to 1949 in the sound era He died in Los Angeles, California in 1984.

**d4: The Legend of the Boy and the Eagle**

- [d4s0] The Legend of the Boy and the Eagle is a 1967 American live- action Walt Disney film.

**d5: The Boy and the Fog**

- [d5s0] The Boy and the Fog is a 1953 Mexican drama film directed by Roberto Gavaldón.
- [d5s1] It was entered into the 1954 Cannes Film Festival.

**d6: Philip Sugden (historian)**

- [d6s0] Philip Sugden( January 27, 1947 – found dead April 26, 2014) was an English historian, best known for his comprehensive study of Jack the Ripper case, including the books" The Complete History of Jack the Ripper", first published in 1994, and" The Life and Times of Jack the Ripper"( 1996).
- [d6s1] He was the first academic historian to work on the case.

**d7: Jack's the Boy**

- [d7s0] Jack's the Boy is a 1932 British comedy film directed by Walter Forde and starring Jack Hulbert, Cicely Courtneidge, Francis Lister and Peter Gawthorne.
- [d7s1] It became well known for its song
- [d7s2] "The Flies Crawled Up the Window", sung by Hulbert, which was released as a record and proved a major hit.
- [d7s3] The film was released in the U.S. as Night and Day.

**d8: Eduardo Mignogna**

- [d8s0] Eduardo Mignogna (August 17, 1940 – October 6, 2006) was an Argentinian film director and screenwriter.

**d9: Mr. Right (2009 film)**

- [d9s0] Mr. Right is a 2009 British film directed by David Morris and Jacqui Morris.
- [d9s1] The jointly- made gay- themed film is the debut for both directors.

**d10: Lee Boardman**

- [d10s0] Lee Boardman( born 2 July 1972) is an English actor and narrator.
- [d10s1] He has appeared in the films" Jack the Giant Slayer" and" Love's Kitchen", and the television series" Rome".

## 4. 2wikimultihopqa_5637d4a60bdb11eba7f7acde48001122

原位置：`train` 第 34 题 · 全局第 34 题 · `sample_id: 2wikimultihopqa_5637d4a60bdb11eba7f7acde48001122`

Question: Where was the director of film Happy Easter born?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of film Happy Easter | False | () |
| u2 | birthplace of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Happy Easter | False | [] | Georges Lautner | [['d2s0']] |
| u2 | place of birth of {u1} | True | ['u1'] | Nice | [['d1s2']] |

### Source documents (reference only)

**d1: Georges Lautner**

- [d1s0] Georges Lautner( 24 January 1926 – 22 November 2013) was a French film director and screenwriter, known primarily for his comedies created in collaboration with screenwriter Michel Audiard.
- [d1s1] Lautner's ventures into other genres were less successful though the thriller Le Professionnel starring Jean- Paul Belmondo was a big commercial hit in France in 1981.
- [d1s2] He was born in Nice, the son of actress Renée Saint- Cyr.

**d2: Happy Easter**

- [d2s0] Happy Easter  is a 1984 French comedy film directed by Georges Lautner.

**d3: Jamal Easter**

- [d3s0] Derwain Jamal Easter( born 15 November 1987) is a Welsh footballer who is currently playing for Bridgend Town.
- [d3s1] He is also a former Wales Under- 21 international.

**d4: Ian Barry (director)**

- [d4s0] Ian Barry is an Australian director of film and TV.

**d5: Griffin Easter**

- [d5s0] Griffin Easter( born November 6, 1991) is an American professional cyclist, who currently rides for 303 Project.

**d6: Graham Easter**

- [d6s0] Graham Easter( born 26 September 1969) is an English former professional footballer who played as a winger.

**d7: Jermaine Easter**

- [d7s0] Jermaine Maurice Easter( born 15 January 1982 in Cardiff) is a former Welsh international footballer who played as a striker most recently for English club Bristol Rovers.

**d8: Wayne Easter**

- [d8s0] Wayne Easter( born June 22, 1949) is a Canadian politician who has been the elected member of parliament for the riding of Malpeque since 1993.

**d9: Peter Levin**

- [d9s0] Peter Levin is an American director of film, television and theatre.

**d10: Paul Easter**

- [d10s0] Paul Robert Easter( born 14 May 1963) is a former competitive swimmer who represented Great Britain in the Olympics, and competed for Scotland in the Commonwealth Games.

## 5. 2wikimultihopqa_565e3072087711ebbd67ac1f6bf848b6

原位置：`train` 第 35 题 · 全局第 35 题 · `sample_id: 2wikimultihopqa_565e3072087711ebbd67ac1f6bf848b6`

Question: Which film whose director is younger, Cross Shot or Germany, Year Zero?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of Cross Shot | False | () |
| u2 | birth date of {u1} | False | ('u1',) |
| u3 | director of Germany, Year Zero | False | () |
| u4 | birth date of {u3} | False | ('u3',) |
| u5 | which film's director is younger | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Cross Shot | False | [] | Stelvio Massi | [['d4s0']] |
| u2 | date of birth of {u1} | False | ['u1'] | 26 March 1929 | [['d7s0']] |
| u3 | director of film Germany, Year Zero | False | [] | Roberto Rossellini | [['d5s0']] |
| u4 | date of birth of {u3} | False | ['u3'] | 8 May 1906 | [['d6s0']] |
| u5 | which of the two films has the younger director | True | ['u2', 'u4'] | Cross Shot | [[]] |

### Source documents (reference only)

**d1: Year Zero (disambiguation)**

- [d1s0] Year zero is the year before 1 AD used in astronomical calculations.
- [d1s1] Year Zero may also refer to:

**d2: Fear (1954 film)**

- [d2s0] Fear  is a 1954 drama film directed by Roberto Rossellini and starring his wife Ingrid Bergman.
- [d2s1] It has also been released as Angst in the English-speaking world.
- [d2s2] It is loosely based on the Stefan Zweig novel "Fear".
- [d2s3] It was filmed in Munich and was shot simultaneously in German and English.
- [d2s4] Rossellini created it because he wanted to explore the reconstruction of Germany from both a material and moral standpoint ten years after making his previous German film "Germany Year Zero".
- [d2s5] The film is noirish with aspects reminiscent of Hitchcock and German Expressionism.

**d3: Homeland: Iraq Year Zero**

- [d3s0] Homeland: Iraq
- [d3s1] Year Zero is a 2015 documentary film written and directed by the Iraqi- French film director Abbas Fahdel.

**d4: Cross Shot**

- [d4s0] Cross Shot( originally titled La legge violenta della squadra anticrimine) is a 1976 Italian" poliziottesco" film directed by Stelvio Massi.
- [d4s1] It was filmed in Apulia, between Bari and Trani.

**d5: Germany, Year Zero**

- [d5s0] Germany, Year Zero is a 1948 film directed by Roberto Rossellini, and is the final film in Rossellini's unofficial war film trilogy, following" Rome, Open City" and" Pais à Germany Year Zero" takes place in Allied- occupied Germany, unlike the others, which take place in German- occupied Rome and during the Allied invasion of Italy, respectively.
- [d5s1] As in many neorealist films, Rossellini used mainly local, non-professional actors.
- [d5s2] He filmed on locations in Berlin and intended to convey the reality in Germany the year after its near total destruction in World War II.
- [d5s3] It contains dramatic images of bombed out Berlin and of the human struggle for survival following the destruction of Nazi Germany.
- [d5s4] When explaining his ideas about realism in an interview, he said," realism is nothing other than the artistic form of truth."

**d6: Roberto Rossellini**

- [d6s0] Roberto Gastone Zeffiro Rossellini( 8 May 1906 – 3 June 1977) was an Italian film director, screenwriter, and producer.
- [d6s1] Rossellini was one of the directors of the Italian neorealist cinema, contributing to the movement with films such as" Rome, Open City"( 1945)," Paisan"( 1946)," Germany, Year Zero"( 1948), and" General Della Rovere"( 1959).

**d7: Stelvio Massi**

- [d7s0] Stelvio Massi( 26 March 1929 – 26 March 2004), sometimes credited" Max Steel", was an Italian director known for his poliziotteschi films.

**d8: 0Q**

- [d8s0] 0Q( zero Q) or 0- Q may refer to:

**d9: La Bestia humana**

- [d9s0] La Bestia humana is a 1957 Argentine film whose story is based on the novel" La Bête Humaine" by the French writer Émile Zola.

**d10: Germany Year 90 Nine Zero**

- [d10s0] Germany Year 90 Nine Zero( French:" Allemagne année 90 neuf zéro") is a French film directed by Jean- Luc Godard and starring Eddie Constantine in his signature role as detective Lemmy Caution.
- [d10s1] This is the second film in which Godard and Constantine collaborated with the Lemmy Caution character, although it is not officially a sequel to" Alphaville".
- [d10s2] It was also the 15th and final time that Constantine would play his signature role in 40 years.
- [d10s3] The film was screened in competition at the 48th Venice International Film Festival, in which it won the President of the Italian Senate's Gold Medal.
- [d10s4] The title is a reference to the 1948 Roberto Rossellini film Germany, Year Zero

## 6. 2wikimultihopqa_595c742308ac11ebbd82ac1f6bf848b6

原位置：`train` 第 36 题 · 全局第 36 题 · `sample_id: 2wikimultihopqa_595c742308ac11ebbd82ac1f6bf848b6`

Question: Are both movies, Tragedy Of Love and Descente Du Mont Serrat, from the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of Tragedy Of Love | False | () |
| u2 | country of Descente Du Mont Serrat | False | () |
| u3 | whether both movies are from the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country of origin of Tragedy of Love | False | [] | Germany | [['d1s0', 'd1s1']] |
| u2 | country of origin of Descente du Mont Serrat | False | [] | France | [['d8s0']] |
| u3 | whether Tragedy of Love and Descente du Mont Serrat are from the same country | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Tragedy of Love**

- [d1s0] Tragedy of Love (German:
- [d1s1] Tragödie der Liebe) is a 1923 German silent film directed by Joe May and starring Mia May, Emil Jannings and Marlene Dietrich.
- [d1s2] The film's sets were designed by the art directors Erich Kettelhut, Paul Leni and Erich Zander.

**d2: Face of Love**

- [d2s0] Face of Love, Faces of Love, The Face of Love, etc., may refer to:

**d3: Neven du Mont**

- [d3s0] Neven du Mont may refer to:

**d4: Sky du Mont**

- [d4s0] Sky du Mont( born Cayetano Neven du Mont; 20 May 1947) is a German actor.

**d5: Konjiki no Gash Bell!! Movie 2: Attack of the Mecha-Vulcan**

- [d5s0] Discotek Media released both movies on Blu-ray and DVD for the first time in North America on March 27, 2018.

**d6: Manual of Love 2**

- [d6s0] Manual of Love 2 is a 2007 Italian romantic comedy film in four quartets directed by Giovanni Veronesi.
- [d6s1] It is the sequel of" Manual of Love" and was followed by" Manual of Love 3".

**d7: Season of Love**

- [d7s0] Season of Love or Seasons of Love may refer to:

**d8: Descente du Mont Serrat**

- [d8s0] Descente du Mont Serrat is a 1901 French short black- and- white silent documentary film directed by Segundo de Chomón.

**d9: The Game of Love**

- [d9s0] Game of Love or The Game of Love may refer to:

**d10: Mont'Serrat, Porto Alegre**

- [d10s0] Mont' Serrat is a neighbourhood(" bairro") in the city of Porto Alegre, the state capital of Rio Grande do Sul, in Brazil.
- [d10s1] It was created by Law 2022 from December 7, 1959.
- [d10s2] Located on a hill, Mont'Serrat was named after the famous mountain in Catalonia.
- [d10s3] It embraces people from upper middle class to upper class.

## 7. 2wikimultihopqa_5c23b3b20bdb11eba7f7acde48001122

原位置：`train` 第 37 题 · 全局第 37 题 · `sample_id: 2wikimultihopqa_5c23b3b20bdb11eba7f7acde48001122`

Question: What is the date of death of the director of film The Accidental Honeymoon?

Note:

Type: bridge · fallback: False · SFT snapshots: 7

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of film The Accidental Honeymoon | False | () |
| u2 | date of death of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film The Accidental Honeymoon | False | [] | Léonce Perret | [['d7s0']] |
| u2 | date of death of {u1} | True | ['u1'] | 12 August 1935 | [['d3s0']] |

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

**d2: Harry Wainwright (footballer)**

- [d2s0] Harry Wainwright( born 1899; date of death unknown) was an English footballer.

**d3: Léonce Perret**

- [d3s0] Léonce Joseph Perret (14 March 1880 – 12 August 1935) was a prolific and innovative French film actor, director and producer.
- [d3s1] He also worked as a stage actor and director.
- [d3s2] Often described as avant-garde for his unorthodox directing methods, Léonce Perret introduced innovative camera, lighting and film scoring techniques to French cinema.
- [d3s3] Léonce Perret began his career as a relatively undistinguished stage actor.
- [d3s4] He was recruited to the film industry by the Gaumont Film Company.
- [d3s5] His numerous short films gained significant accolade in French cinematography.
- [d3s6] Until his emigration to the United States in 1917, he was a fixture of the Gaumont Film Company.
- [d3s7] On American soil, he produced several popular films, the most notable being "Lest We ForgetN'oublions jamais") in 1918.
- [d3s8] After returning to France, he directed the successful "Koenigsmark" in 1923.
- [d3s9] His film "Madame Sans-Gêne" (1925), starring Gloria Swanson, was the first joint Franco-American film production.
- [d3s10] In addition, Léonce Perret collaborated with many of the French and American idols of his generation such as Abel Gance, Gloria Swanson, Gaby Morlay, René Cresté, Arletty, Suzanne Grandais, Mae Murray, and Huguette Duflos.

**d4: Theodred II (Bishop of Elmham)**

- [d4s0] Theodred II was a medieval Bishop of Elmham.
- [d4s1] The date of Theodred's consecration unknown, but the date of his death was sometime between 995 and 997.

**d5: The Accidental Detective 2: In Action**

- [d5s0] The Accidental Detective 2: In Action is a 2018 South Korean crime comedy film and sequel to Kim Jung- hoon's 2015 film" The Accidental Detective".
- [d5s1] The film is directed by Lee Eon-hee, starring Kwon Sang- woo, Sung Dong- il and Lee Kwang- soo.
- [d5s2] The film was released on June 13, 2018.

**d6: Thomas Scott (diver)**

- [d6s0] Thomas Scott( 1907- date of death unknown) was an English diver.

**d7: The Accidental Honeymoon**

- [d7s0] The Accidental Honeymoon is a 1918 American silent comedy drama film directed by Léonce Perret and starring Robert Warwick.
- [d7s1] A fragment of the film remains with only a single reel of the 5 reel film existing at the Library of Congress.

**d8: Bill Smith (footballer, born 1897)**

- [d8s0] William Thomas Smith( born 9 April 1897, date of death unknown) was an English professional footballer.

**d9: Ian Barry (director)**

- [d9s0] Ian Barry is an Australian director of film and TV.

**d10: Peter Levin**

- [d10s0] Peter Levin is an American director of film, television and theatre.

## 8. 2wikimultihopqa_5d3e9f4a0baf11ebab90acde48001122

原位置：`train` 第 38 题 · 全局第 38 题 · `sample_id: 2wikimultihopqa_5d3e9f4a0baf11ebab90acde48001122`

Question: Who is the paternal grandmother of Elizabeth Of Hungary, Queen Of Serbia?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Elizabeth Of Hungary, Queen Of Serbia | False | () |
| u2 | mother of {u1}, Elizabeth Of Hungary, Queen Of Serbia's paternal grandmother | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Elizabeth of Hungary, Queen of Serbia | False | [] | Stephen V of Hungary | [['d2s0']] |
| u2 | mother of {u1}, paternal grandmother of Elizabeth of Hungary, Queen of Serbia | True | ['u1'] | Maria Laskarina | [['d10s1']] |

### Source documents (reference only)

**d1: Elizabeth of Celje**

- [d1s0] Elizabeth of Celje( 1441 – 1455), also Elizabeth of Cilli, was the first wife of Matthias Corvinus, the future King of Hungary.

**d2: Elizabeth of Hungary, Queen of Serbia**

- [d2s0] Elizabeth of Hungary the widow("/ Jelisaveta"; c. 1255–1313) was one of the daughters of King Stephen V of Hungary and his wife Elizabeth the Cuman.
- [d2s1] She was a member of the House of Arpad and later became Queen consort of Serbia by her marriage to Stefan Uroš II Milutin of Serbia.

**d3: Louisa Cavendish-Bentinck**

- [d3s0] Caroline Louisa Cavendish- Bentinck( née Burnaby; 5 December 1832 – 6 July 1918) was the maternal grandmother of Queen Elizabeth The Queen Mother and the great- grandmother of Elizabeth II.

**d4: Mona Hopton Bell**

- [d4s0] Mona Hopton Bell( 1867- 1940) was a British artist, best known for her portraits of civic figures.
- [d4s1] She was the grandmother of the painter Jean H. Bell.

**d5: Kaoru Hatoyama**

- [d5s0] After the elections of 2009, she became more widely known as the grandmother of Prime Minister Yukio Hatoyama and his politician brother Kunio Hatoyama.

**d6: Hubba bint Hulail**

- [d6s0] Hubba bint Hulail was the grandmother of Hashim ibn' Abd Manaf, thus the great- great- great- grandmother of the Islamic" Nabī"( Prophet) Muhammad ibn Abdullah.

**d7: Yolanda of Poland**

- [d7s0] Yolanda of Poland( also known as Helen; 1235 – 11 June 1298) was the daughter of King Béla IV of Hungary and Maria Laskarina.
- [d7s1] She was the sister of Margaret of Hungary and Kinga of Poland( Cunegunda).
- [d7s2] One of her paternal aunts was the Franciscan Elizabeth of Hungary.

**d8: Tjuyu**

- [d8s0] Tjuyu( sometimes transliterated as Thuya or Thuyu) was an Egyptian noblewoman and the mother of queen Tiye, and the wife of Yuya.
- [d8s1] She is the grandmother of Akhenaten, and great grandmother of Tutankhamun.

**d9: Hannah Arnold**

- [d9s0] Hannah Arnold, also known as Hannah Waterman King, was the grandmother of Benedict Arnolds children.

**d10: Stephen V of Hungary**

- [d10s0] Stephen V (before 18 October 1239 – 6 August 1272, Csepel Island) was King of Hungary and Croatia between 1270 and 1272, and Duke of Styria from 1258 to 1260.
- [d10s1] He was the oldest son of King Béla IV and Maria Laskarina.
- [d10s2] King Béla had his son crowned king at the age of six and appointed him Duke of Slavonia.
- [d10s3] Still a child, Stephen married Elizabeth, a daughter of a chieftain of the Cumans whom his father settled in the Great Hungarian Plain.
- [d10s4] King Béla appointed Stephen Duke of Transylvania in 1257 and Duke of Styria in 1258.
- [d10s5] The local noblemen in Styria, which had been annexed four years before, opposed his rule.
- [d10s6] Assisted by King Ottokar II of Bohemia, they rebelled and expelled Stephen's troops from most parts of Styria.
- [d10s7] After Ottokar II routed the united army of Stephen and his father in the Battle of Kressenbrunn on 12 July 1260, Stephen left Styria and returned to Transylvania.
- [d10s8] Stephen forced his father to cede all the lands of the Kingdom of Hungary to the east of the Danube to him and adopted the title of junior king in 1262.
- [d10s9] In two years, a civil war broke out between father and son, because Stephen accused Béla of planning to disinherit him.
- [d10s10] They concluded a peace treaty in 1266, but confidence was never restored between them.
- [d10s11] Stephen succeeded his father, who died on 3 May 1270, without difficulties, but his sister Anna and his father's closest advisors fled to the Kingdom of Bohemia.
- [d10s12] Ottokar II invaded Hungary in the spring of 1271, but Stephen routed him.
- [d10s13] In next summer, a rebellious lord captured and imprisoned Stephen's son, Ladislaus.
- [d10s14] Shortly thereafter, Stephen unexpectedly fell ill and died.

## 9. 2wikimultihopqa_5f7ce04c099111ebbdb0ac1f6bf848b6 【需改：生成拆解】

原位置：`train` 第 39 题 · 全局第 39 题 · `sample_id: 2wikimultihopqa_5f7ce04c099111ebbdb0ac1f6bf848b6`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_5f7ce04c099111ebbdb0ac1f6bf848b6"></a>

> **审阅结论：需改：生成拆解**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 把完整地名“Mar, Isfahan”中的行政区限定词当成另一个被比较对象，导致本应比较两个地点却生成三个事实单元。源文档标题与首句确认这是一个地点。
>
> **处理建议：** 将“Mar, Isfahan”作为不可拆开的实体；恢复两个国家事实单元和一个必要比较结论，删除多余行政区单元并重建依赖。
>
> **证据定位：** d8s0, d3s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Are Mar, Isfahan and Anjir Bazuiyeh both located in the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of Mar | False | () |
| u2 | country of Isfahan | False | () |
| u3 | country of Anjir Bazuiyeh | False | () |
| u4 | whether Mar, Isfahan and Anjir Bazuiyeh are located in the same country | True | ('u1', 'u2', 'u3') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country of Mar, Isfahan | False | [] | Iran | [['d8s0']] |
| u2 | country of Anjir Bazuiyeh | False | [] | Iran | [['d3s0']] |
| u3 | whether Mar, Isfahan and Anjir Bazuiyeh are located in the same country | True | ['u1', 'u2'] | yes | [[]] |

### Source documents (reference only)

**d1: Shah Mansur (Muzaffarid)**

- [d1s0] Shah Mansur was the last of the Muzaffarid rulers of Southern Iran.
- [d1s1] He ruled from Isfahan and was killed by the forces of Timurlane in 1393.

**d2: Road 62 (Iran)**

- [d2s0] Road 62 is a road connecting the province of Loristan to Isfahan and Mashhad, in Iran.

**d3: Anjir Bazuiyeh**

- [d3s0] Anjir Bazuiyeh( also Romanized as Anjīr Bāzū’īyeh and Anjīr -e Bāzū’īyeh) is a village in Dalfard Rural District, Sarduiyeh District, Jiroft County, Kerman Province, Iran.
- [d3s1] At the 2006 census, its population was 84, in 23 families.

**d4: Mohammad-Hassan Malekmadani**

- [d4s0] Mohammad- Hassan Malekmadani is an Iranian politician who served as the mayor in Isfahan and Tehran.

**d5: Radzice**

- [d5s0] Radzice is part of the name of two villages, both located in Gmina Drzewica, within Opoczno County, Łódź Voivodeship, Poland:

**d6: Road 55 (Iran)**

- [d6s0] Road 55 connects Persian Gulf and Bushehr to Isfahan and central Iran to Road 65.
- [d6s1] The road is of a national importance with regard to transit, as it is the shortest and fastest link connecting Isfahan and places north of it with Bushehr and Asaluyeh on the coast of Persian Gulf

**d7: Jawty**

- [d7s0] Jawty is part of the name of two villages, both located in Gmina Susz, within Iława County, Warmian- Masurian Voivodeship, Poland:

**d8: Mar, Isfahan**

- [d8s0] Mar( also Romanized as Mār) is a village in Barzavand Rural District, in the Central District of Ardestan County, Isfahan Province, Iran.
- [d8s1] At the 2006 census, its population was 61, in 26 families.

**d9: Lubnowy**

- [d9s0] Lubnowy is part of the name of two villages, both located in Gmina Susz, within Iława County, Warmian- Masurian Voivodeship, Poland:

**d10: Mehran Alighadr**

- [d10s0] Mehran Alighadr( born 24 May 1989) is an Iranian futsal player.
- [d10s1] He is a Left Winger, and currently a player of Giti Pasand Isfahan and Iran national futsal team.

## 10. 2wikimultihopqa_600955300baf11ebab90acde48001122

原位置：`train` 第 40 题 · 全局第 40 题 · `sample_id: 2wikimultihopqa_600955300baf11ebab90acde48001122`

Question: Who is George Iii Dadiani's paternal grandfather?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of George Iii Dadiani | False | () |
| u2 | father of {u1}, George Iii Dadiani's paternal grandfather | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of George III Dadiani | False | [] | Levan I Dadiani | [['d3s1']] |
| u2 | father of {u1}, George III Dadiani's paternal grandfather | True | ['u1'] | Mamia III Dadiani | [['d9s1']] |

### Source documents (reference only)

**d1: Prithvipati Shah**

- [d1s0] Prithvipati Shah( ?–1716) was the king of the Gorkha Kingdom in the Indian subcontinent, present- day Nepal.
- [d1s1] He was the grandfather of Nara Bhupal Shah.

**d2: Lyon Cohen**

- [d2s0] Lyon Cohen( 1868–1937) was a Polish- born Canadian businessman and a philanthropist.
- [d2s1] He was the grandfather of singer/ poet Leonard Cohen.

**d3: George III Dadiani**

- [d3s0] Giorgi III Dadiani (died 1582) was Prince of Mingrelia, of the House of Dadiani, from 1572 to 1573 and again from 1578 until his death.
- [d3s1] He was a son and successor of Levan I Dadiani.
- [d3s2] Giorgi Dadiani's hold of power in Mingrelia, one of those states that had emerged after the disintegration of the Kingdom of Georgia in the 15th century, was challenged by the neighboring ruler, Giorgi Gurieli, Prince of Guria, and his own younger brother, Mamia IV.
- [d3s3] In 1573, they succeeded in ousting Giorgi, who was only able to resume the throne through the intercession of King George II of Imereti and at the price of territorial and financial concessions in 1578.
- [d3s4] Thenceforth, Mingrelia experienced a relative peace until Giorgi's death in 1582.
- [d3s5] The historian Cyril Toumanoff, frequently cited in modern Western literature, disagreed with this traditional chronology, established by the early 18th-century scholar Prince Vakhushti, and dated Giorgi's rule to the years 1546–1574 and 1574–1582.

**d4: Abd al-Muttalib**

- [d4s0] Abd al- Muttalib Shaybah ibn Hashim( c. 497 – 578) was the grandfather of Islamic prophet Muhammad.

**d5: Guillaume Wittouck**

- [d5s0] Guillaume Wittouck( 1749- 1829) was a Belgian lawyer and High Magistrate.
- [d5s1] He was the Grandfather of industrialist Paul Wittouck.

**d6: Tamar of Mukhrani**

- [d6s0] Tamar( died 1683) was a Georgian princess of the House of Mukhrani who was married, successively, to three sovereigns of western Georgia — Levan III Dadiani, Prince of Mingrelia, then King Bagrat V of Imereti, and finally, Giorgi III Gurieli, Prince of Guria.
- [d6s1] Tamar's marriages were part of political intrigues and accompanying wife swaps characteristic for the Georgian history of that century.

**d7: Mamia IV Dadiani**

- [d7s0] Mamia IV Dadiani (died 1590) was Prince of Mingrelia, of the House of Dadiani, from 1573 to 1578 and again from 1582 until his death.
- [d7s1] He was a younger son of Levan I Dadiani.
- [d7s2] Mamia Dadiani's career unfolded against the background of an increasingly destructive civil unrest in the successor states of the Kingdom of Georgia in which the rulers of Mingrelia, in the former kingdom's west, played a critical role.
- [d7s3] His first accession to power was the result of a coup against his own brother, Giorgi III Dadiani, with whom he eventually reconciled in exchange of new estates.
- [d7s4] His second term, after succeeding on the death of Giorgi III Dadiani, was consumed by wars with his in-laws, the prince of Guria and king of Imereti.
- [d7s5] The latter, Levan of Imereti, fell in Mamia's hands and died in captivity.
- [d7s6] Dadiani himself died without seeing his protégé firmly established on the throne of Imereti.
- [d7s7] He was succeeded by his younger brother, Manuchar I Dadiani.

**d8: John Westley**

- [d8s0] Rev. John Westley( 1636 – 78) was an English nonconformist minister.
- [d8s1] He was the grandfather of John Wesley( founder of Methodism).

**d9: Levan I Dadiani**

- [d9s0] Levan I Dadiani (also Leon; ; died 1572) was a member of the House of Dadiani and ruler of Odishi, that is, Mingrelia, in western Georgia.
- [d9s1] He succeeded on the death of his father, Mamia III Dadiani, as "eristaviduke") of Odishi and ex officio "mandaturt-ukhutsesiLord High Steward") of Imereti in 1533.
- [d9s2] Dadiani's break with the king of Imereti brought about his downfall and imprisonment in 1546.
- [d9s3] He was able to escape and regain his possessions, securing Ottoman support for his independence from Imereti.

**d10: Kaya Alp**

- [d10s0] Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

## 11. 2wikimultihopqa_604b9ce208bc11ebbd88ac1f6bf848b6

原位置：`train` 第 41 题 · 全局第 41 题 · `sample_id: 2wikimultihopqa_604b9ce208bc11ebbd88ac1f6bf848b6`

Question: Which film has the director died first, The Gaunt Stranger or Dead Man'S Bluff?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of The Gaunt Stranger | False | () |
| u2 | death date of {u1} | False | ('u1',) |
| u3 | director of Dead Man'S Bluff | False | () |
| u4 | death date of {u3} | False | ('u3',) |
| u5 | which film's director died first | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film The Gaunt Stranger | False | [] | Walter Forde | [['d1s0']] |
| u2 | date of death of {u1} | False | ['u1'] | 7 January 1984 | [['d7s0']] |
| u3 | director of film Dead Man's Bluff | False | [] | Aleksei Balabanov | [['d5s1']] |
| u4 | date of death of {u3} | False | ['u3'] | 18 May 2013 | [['d2s0']] |
| u5 | which of The Gaunt Stranger and Dead Man's Bluff has the director who died first | True | ['u2', 'u4'] | The Gaunt Stranger | [[]] |

### Source documents (reference only)

**d1: The Gaunt Stranger**

- [d1s0] The Gaunt Stranger (released as The Phantom Strikes in the US) is a 1938 British mystery thriller film directed by Walter Forde.
- [d1s1] It stars Sonnie Hale, Wilfrid Lawson and Alexander Knox.

**d2: Aleksei Balabanov**

- [d2s0] Aleksei Oktyabrinovich Balabanov (25 February 1959 – 18 May 2013) was a Russian film director, screenwriter, and producer, who shot mostly arthouse pictures but gained mainstream popularity with the crime drama "Brother" (1997) and its more action-oriented sequel, "Brother 2" (2000), both of which starred Sergei Bodrov, Jr. as Danila Bagrov.
- [d2s1] "
- [d2s2] Brother" was successful both at the box office and in video copies, achieving wide popularity in Russia.
- [d2s3] Later, however, Balabanov became better known for his films "Cargo 200" (2007) and "Morphine" (2008).
- [d2s4] A hugely controversial figure, Balabanov was often accused of both Russian nationalism "(Brother 2, War)" and Russophobia "(Cargo 200, The Stoker)", as well as general misanthropy.
- [d2s5] Due to his personal and political controversy, grotesque style, dark humour, shocking naturalism, genre deconstruction, and balancing between art cinema and mainstream
- [d2s6] he was often compared to Lars von Trier, Rainer Werner Fassbinder, Coen brothers, and Takeshi Kitano.

**d3: The Ringer (1931 film)**

- [d3s0] The Ringer is a 1931 British crime film directed by Walter Forde and starring Patric Curwen, Esmond Knight, John Longden and Carol Goodner.
- [d3s1] Scotland Yard detectives hunt for a dangerous criminal who has recently returned to England.
- [d3s2] The film was based on an Edgar Wallace story" The Gaunt Stranger", which is the basis for his play" The Ringer".
- [d3s3] Forde remade the same story in 1938 as" The Gaunt Stranger".
- [d3s4] There was also a silent film of" The Ringer" in 1928, and a 1952 version starring Donald Wolfit.
- [d3s5] It was made at Beaconsfield Studios.

**d4: Blind Man's Bluff (1952 film)**

- [d4s0] Blind Man's Bluff is a 1952 British crime film directed by Charles Saunders and starring Zena Marshall, Sydney Tafler and Anthony Pendrell.

**d5: Dead Man's Bluff**

- [d5s0] Dead Man's Bluff, or Zhmurki  is a 2005 Russian black comedy/crime film.
- [d5s1] Director Aleksei Balabanov, who directed "Brother" and "Brother 2", uses "uniformly ace" (Variety) cameo performances, by Russia's most prominent actors.
- [d5s2] The film suggests that in the mean free-market streets of Russia in the beginning of 90s, the only real liberty was the freedom to kill.

**d6: Der Hexer (1964 film)**

- [d6s0] Der Hexer( aka The Ringer," The Wizard" or" The Mysterious Magician") is a 1964 West German black and white mystery film directed by Alfred Vohrer and starring Joachim Fuchsberger.
- [d6s1] It was part of a very successful series of German films based on the writings of Edgar Wallace and adapted from the 1925 novel titled" The Ringer"( originally:" The Gaunt Stranger").
- [d6s2] In 1965, a sequel" Neues vom HexerAgain the Ringer") was released.

**d7: Walter Forde**

- [d7s0] Walter Forde( born Thomas Seymour Woolford, 21 April 1898 – 7 January 1984) was a British actor, screenwriter and director.
- [d7s1] Born in Lambeth, South London in 1898, he directed over fifty films between 1919 from the silent era through to 1949 in the sound era He died in Los Angeles, California in 1984.

**d8: Dead Man's Hand (2007 film)**

- [d8s0] Dead Man's Hand is a 2007 film directed by Charles Band.

**d9: Elsa Barker**

- [d9s0] Elsa Barker( 1869 – 1954) was an American novelist, short- story writer and poet.
- [d9s1] She became known for three books" Letters from a Living Dead Man"( 1914)," War Letters from the Living Dead Man"( 1915), and" Last Letters From the Living Dead Man"( 1919), that she said were messages from a dead man produced through automatic writing.

**d10: The Ringer (1928 film)**

- [d10s0] The Ringer is a 1928 British silent crime film directed by Arthur Maude and starring Leslie Faber, Annette Benson and Hayford Hobbs.
- [d10s1] It was based on the Edgar Wallace novel" The Gaunt Stranger".
- [d10s2] Scotland Yard hunt for a dangerous criminal who has returned to Britain after many years away.
- [d10s3] A talkie version of" The Ringer" followed in 1931.

## 12. 2wikimultihopqa_6670d044088d11ebbd70ac1f6bf848b6 【保留新拆法｜重标人工标签】

原位置：`train` 第 42 题 · 全局第 42 题 · `sample_id: 2wikimultihopqa_6670d044088d11ebbd70ac1f6bf848b6`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_6670d044088d11ebbd70ac1f6bf848b6"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。
>
> **处理建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。
>
> **证据定位：** d2s0, d6s0, d9s0, d3s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Do both Secret Obsession and Descente Aux Enfers films have the directors from the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of director of Secret Obsession | False | () |
| u2 | country of director of Descente Aux Enfers | False | () |
| u3 | whether directors of Secret Obsession and Descente Aux Enfers are from the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of Secret Obsession | False | [] | Peter Sullivan | [['d2s0'], ['d6s13']] |
| u2 | nationality of {u1} | False | ['u1'] | American | [['d6s0']] |
| u3 | director of Descente aux enfers | False | [] | Francis Girod | [['d9s0']] |
| u4 | nationality of {u3} | False | ['u3'] | French | [['d3s0']] |
| u5 | whether the directors of Secret Obsession and Descente aux enfers are from the same country | True | ['u2', 'u4'] | no | [[]] |

### Source documents (reference only)

**d1: Charles K. Gifford**

- [d1s0] Charles K. Gifford is an American banker and businessman.
- [d1s1] He is the chairman emeritus of Bank of America having served on its board of directors from 2004 to 2016.

**d2: Secret Obsession**

- [d2s0] Secret Obsession is a 2019 American psychological thriller film directed by Peter Sullivan, who co-wrote the screenplay with Kraig Wenman.
- [d2s1] It stars Brenda Song, Mike Vogel and Dennis Haysbert.
- [d2s2] It was released on July 18, 2019, by Netflix.

**d3: Francis Girod**

- [d3s0] Francis Girod (9 October 1944 – 19 November 2006) was a French film director, actor, and screenwriter.
- [d3s1] He directed 20 films between 1974 and 2006.
- [d3s2] His film "L'enfance de l'art" was entered into the 1988 Cannes Film Festival.
- [d3s3] In 1994 he was a member of the jury at the 44th Berlin International Film Festival.

**d4: Constance aux enfers**

- [d4s0] Constance aux enfers( US title: Web of Fear) is a 1963 French language motion picture crime thriller directed by François Villiers.
- [d4s1] It was based on novel" Constance aux enfers" by Jean- Pierre Ferrière, who co-wrote screenplay with Jacques Sigurd.
- [d4s2] The film stars Michèle Morgan, Dany Saval.

**d5: Hector-Jonathan Crémieux**

- [d5s0] Hector-Jonathan Crémieux( 10 November 1828 – 30 September 1893) was a French librettist and playwright.
- [d5s1] His best- known work is his collaboration with Ludovic Halévy for Jacques Offenbach's" Orphée aux Enfers", known in English as" Orpheus in the Underworld".

**d6: Peter Sullivan (screenwriter)**

- [d6s0] Peter Sullivan( born November 30, 1976) is an American screenwriter, film director and film producer.
- [d6s1] Peter Sullivan was born in Shrewsbury, Massachusetts and graduated from New York University's Tisch School of the Arts with a degree in Film and Television.
- [d6s2] He directed the Hallmark original movie" Christmas Under WrapsChristmas Under Wraps" was the highest rated telecast in Hallmark Channel history and the second highest rated cable movie in 2014.
- [d6s3] His directing credits include the Lionsgate release" Summoned, High School Possession," a horror thriller," Dear Secret SantaHidden Away", a Lifetime thriller, the Lifetime original Christmas movie," All About Christmas Eve" and" Christmas Twister 12 Wishes of Christmas," and" The Dog Who Saved Halloween", the short" Stephen King Night Surf", and the comedy web- series" Everyone Counts," about the 2010 Census featuring French Stewart.
- [d6s4] In the summer of 2007, he directed a series of behind- the- scenes segments for the web- series" In the Motherhood,".
- [d6s5] His writing credits include:" Abandoned", the Hallmark film" Christmas Wedding TailA Valentine Date,StolenObsessionSeduced by LiesEve's Christmas", one of the highest rated Christmas movies in Lifetime history," His and Her Christmas", the New Line Cinema release, the Syfy original" Killer Mountain The Perfect StudentA Christmas ProposalTermination PointBlind Injustice Cave InSecret Lives His and Her ChristmasTrapped, HydraPast Lies, Encounter With DangerFaultline".
- [d6s6] He also co-wrote the airline disaster film" Turbulent Skies" with director Fred Olen Ray.
- [d6s7] He has also written a remake of the B-movie classic" Invasion of the Bee Girls" for producer Fred Weintraub," Final Sanction," an action film, and" The Tower," a horror feature for Cinetel Films.
- [d6s8] In 2008, Peter became vice- president of producer Jeffrey Schenck's production company ARO Entertainment.
- [d6s9] His credits include:" Jersey Shore Shark AttackWyatt Earp's Revenge,", he co-produced ABC Family's hit family film" The Dog Who Saved Christmas" and its sequels" The Dog Who Saved Christmas Vacation" and" The Dog Who Saved the Holidays", the submarine feature" Silent Venom", Syfy Channel originals" Phantom Racer", and" Ice Road TerrorAmerican Bandits: Frank and Jesse The Boy Next DoorChristmas Town The Christmas ClauseDesperate EscapeTrace of DangerA Nanny For Christmas", and" Nightfall".
- [d6s10] He was also a co-producer on the web series" Woke Up Dead".
- [d6s11] In addition to his film work, Peter has written for the internet site Latino Review, and he has also co-written the horror graphic novel" Burning Man" with comic book author Stephen Stern(" Zen the Intergalactic Ninja") and Kenneth Ceballos.
- [d6s12] It is available to download on Amazon.
- [d6s13] In 2018, Sullivan directed the Netflix psychological thriller" Secret Obsession".
- [d6s14] The film was released on July 18, 2019.

**d7: Kyōen Kobanzame**

- [d7s0] There are two parts of the film: the first part and the second part.
- [d7s1] Both parts have the same staff and the same actors.

**d8: Beneath the Surface (1997 film)**

- [d8s0] Under ytan
- [d8s1] ( French title: Descente aux Enfers, English title: Beneath the Surface) is a 1997 Swedish film directed by Daniel Fridell.
- [d8s2] The film won Guldbagge Awards in 1998 for best lead actress Johanna Sällström and best cinematography.

**d9: Descente aux enfers**

- [d9s0] Descente aux enfers(" Descent into Hell") is a 1986 French film directed by Francis Girod.
- [d9s1] Based on the 1955 novel' The Wounded and the Slain' by David Goodis, it is a psychological thriller set under the sun and heat of the Caribbean.
- [d9s2] A married couple, she( Sophie Marceau) with a dark secret in her past and he( Claude Brasseur), an author suffering from both writer's block and alcoholism, undergo experiences which strain their relationship to breaking point but in the end, though each will have to live with the consequences, they are reunited.

**d10: Robert Stone (director)**

- [d10s0] Robert Stone is a British- American documentary filmmaker.
- [d10s1] His work has been screened at dozens of film festivals and televised around the world, notably seven of his films have appeared on PBS's" American Experience" series and four of his films have premiered at the Sundance Film Festival( including Closing Night Film in 2009).

## 13. 2wikimultihopqa_6a80c1d408de11ebbd9eac1f6bf848b6 【需改：生成拆解】

原位置：`train` 第 43 题 · 全局第 43 题 · `sample_id: 2wikimultihopqa_6a80c1d408de11ebbd9eac1f6bf848b6`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_6a80c1d408de11ebbd9eac1f6bf848b6"></a>

> **审阅结论：需改：生成拆解**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 单元本身是两个已点名对象的事实加一个比较/共同属性结论，没有寻找未知中间实体的桥接步骤，但 question_type 被写成 bridge_comparison。
>
> **处理建议：** 只将 question_type 改为 comparison，保留当前单元关系；这属于题型元数据错误，不应为凑题型增加桥接单元。
>
> **证据定位：** d8s0, d6s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Who died first, François-René Tranchefort or Ernst Ludwig Von Aster?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | death date of François-René Tranchefort | False | () |
| u2 | death date of Ernst Ludwig Von Aster | False | () |
| u3 | who died first | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | date of death of François-René Tranchefort | False | [] | 22 May 2019 | [['d8s0']] |
| u2 | date of death of Ernst Ludwig von Aster | False | [] | February 10, 1855 | [['d6s0']] |
| u3 | which of François-René Tranchefort and Ernst Ludwig von Aster died first | True | ['u1', 'u2'] | Ernst Ludwig von Aster | [[]] |

### Source documents (reference only)

**d1: Ernest Friedrich Gilg**

- [d1s0] Ernest( or Ernst) Friedrich Gilg( January 12, 1867 in Baden- Württemberg, Germany – October 11, 1933 in Berlin) was a German botanist.

**d2: François-René de La Tour du Pin Chambly, marquis de La Charce**

- [d2s0] François René de La Tour du Pin, Marquis de la Charce, was a French Military Officer, Politician and Social Reformer.

**d3: Ernst Ludwig II, Duke of Saxe-Meiningen**

- [d3s0] Ernst Ludwig II, Duke of Saxe- Meiningen( Coburg, 8 August 1709 – Meiningen, 24 February 1729), was a duke of Saxe- Meiningen.
- [d3s1] He was the third but second surviving son of Ernst Ludwig I, Duke of Saxe- Meiningen and his first wife, Dorothea Marie of Saxe- Gotha.
- [d3s2] The death of his older brother Josef Bernhard( 22 March 1724) made him the heir to the duchy of Saxe- Meiningen.
- [d3s3] When his father died seven months later( 24 November 1724), Ernst Ludwig- fifteen years old- inherited the duchy along with his younger brother Karl Frederick.
- [d3s4] Because the two princes were under age when their father died, their uncles Frederik Wilhelm and Anton Ulrich served as their guardians until 1733.
- [d3s5] Ernst Ludwig died after reigning five years, only twenty years old and unmarried.
- [d3s6] He was succeeded by his younger brother, Karl Frederick.

**d4: Marc Vignal**

- [d4s0] Marc Vignal( born 21 December 1933 in Nogent- sur- Marne) is a noted French musicologist, writer and radio producer for France Musique and program manager at Radio France( 1975 – 99), a journalist for" Harmony"( 1964 – 84)," Le Monde de la musique"( 1985–2009) and" Classica"( 2009 –).
- [d4s1] He collaborated in the writing of" Fayard Guides: symphonic, sacred, chamber and piano" under the direction of François- René Tranchefort, including French and translated" The Classical Style" by Charles Rosen( Gallimard, 1978, repr. 2000), and" Bach Interpretation" by Paul Badura- Skoda( Buchet- Chastel 1999).
- [d4s2] Vignal is the author of numerous lectures, articles and books on music and musicians.

**d5: Jean-François Pontal**

- [d5s0] Jean- François René Pontal( born 17 April 1943) is a French businessman, and a former Chief Executive of Orange S.A ..

**d6: Ernst Ludwig von Aster**

- [d6s0] Ernst Ludwig von Aster( October 5, 1778- February 10, 1855) was a German officer and a highly decorated Prussian, Saxon and Russian general of the German Campaign of 1813 and the War of the Seventh Coalition.
- [d6s1] He took part in fortifying several fortresses, including in Cologne, Poznań and Königsberg.
- [d6s2] In his honor, in the Poznań Fortress and Koblenz Fortress have been given for forts names from surname" Aster".

**d7: Ernst Dümmler**

- [d7s0] Ernst Ludwig Dümmler( 2 January 183011 September 1902) was a German historian.

**d8: François-René Tranchefort**

- [d8s0] François- René Tranchefort(? – 22 May 2019) was a contemporary French musicologist.

**d9: Ernst-Ludwig von Thadden**

- [d9s0] Ernst- Ludwig von Thadden( born 9 July 1959, in Göttingen, Lower Saxony, Germany) is a German economist, professor at the Department of Economics of the University of Mannheim, and has been president( Rektor) of Mannheim University since October 2012.
- [d9s1] Previously he was professor of Economics at the Département d' Econométrie et Economie Politique at the University of Lausanne.

**d10: Arnošt Kreuz**

- [d10s0] Arnošt Kreuz( or Ernst Kreuz, 9 May 1912 – 9 February 1974), was a Czech football forward of German ethnicity who played for Czechoslovakia in the 1938 FIFA World Cup.

## 14. 2wikimultihopqa_6b702cbe0baf11ebab90acde48001122 【保留新拆法｜重标人工标签】

原位置：`train` 第 44 题 · 全局第 44 题 · `sample_id: 2wikimultihopqa_6b702cbe0baf11ebab90acde48001122`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_6b702cbe0baf11ebab90acde48001122"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** parent 比旧 father 更宽，但题目只问 uncle，未限定父系或母系；新父母→兄弟链并非错误，旧标注的父系链可以作为有证据的实例。
>
> **处理建议：** 保留生成的 parent 描述；按源证据将实际父系关系映射到新单元。不要仅因 gold 写 father 就改写拆题器；如存在多条亲属候选，再补充候选/别名监督。
>
> **证据定位：** d1s0, d7s3；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Who is the uncle of Elisabeth Raiser?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | parent of Elisabeth Raiser | False | () |
| u2 | brother of {u1}, Elisabeth Raiser's uncle | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Elisabeth Raiser | False | [] | Carl Friedrich von Weizsäcker | [['d1s0']] |
| u2 | brother of {u1}, Elisabeth Raiser's uncle | True | ['u1'] | Richard von Weizsäcker | [['d7s3']] |

### Source documents (reference only)

**d1: Elisabeth Raiser**

- [d1s0] Elisabeth Raiser (née Bertha Elisabeth Freiin von Weizsäcker) is a 21st-century historian, former President of the German Evangelical Church Assembly, and daughter of Carl Friedrich von Weizsäcker.

**d2: Giuseppe Bonizzoni**

- [d2s0] Giuseppe Bonizzoni( 22 April 1908 – 21 July 1976) was an Italian professional footballer who played as a defender.
- [d2s1] He was the uncle of former footballer and manager Luigi Bonizzoni.

**d3: Hysen Hoxha**

- [d3s0] Hysen Efendi Hoxha( 1861–1934) was an Albanian politician, mayor of Gjirokastër, and the uncle of Enver Hoxha.

**d4: Enrichetta d'Este**

- [d4s0] Enrichetta d' Este( Enrichetta Maria; 27 May 1702 – 30 January 1777) was a Duchess of Parma by marriage to Antonio Farnese, Duke of Parma, who was her first cousin as well as an uncle of Elisabeth Farnese, Queen of Spain.

**d5: John Montgomery Glover**

- [d5s0] John Montgomery Glover( September 4, 1822 – November 15, 1891) was a North American politician, who served as a U.S. Representative from Missouri, he was the uncle of John Milton Glover.

**d6: Ivan Novoseltsev**

- [d6s0] Ivan Petrovich Novoseltsev( born January 23, 1979) is a Russian former professional ice hockey winger.
- [d6s1] He is the uncle of Vladislav Namestnikov.

**d7: Carl Friedrich von Weizsäcker**

- [d7s0] Carl Friedrich Freiherr von Weizsäcker (28 June 1912 – 28 April 2007) was a German physicist and philosopher.
- [d7s1] He was the longest-living member of the team which performed nuclear research in Germany during the Second World War, under Werner Heisenberg's leadership.
- [d7s2] There is ongoing debate as to whether or not he and the other members of the team actively and willingly pursued the development of a nuclear bomb for Germany during this time.
- [d7s3] A member of the prominent Weizsäcker family, he was son of the diplomat Ernst von Weizsäcker, elder brother of the former German President Richard von Weizsäcker, father of the physicist and environmental researcher Ernst Ulrich von Weizsäcker and father-in-law of the former General Secretary of the World Council of Churches, Konrad Raiser.
- [d7s4] Weizsäcker made important theoretical discoveries regarding energy production in stars from nuclear fusion processes.
- [d7s5] He also did influential theoretical work on planetary formation in the early Solar System.
- [d7s6] In his late career, he focused more on philosophical and ethical issues, and was awarded several international honors for his work in those areas.

**d8: Bradley Orr**

- [d8s0] Bradley James Orr( born 1 November 1982) is an English retired footballer.
- [d8s1] He is the uncle of Rangers defender Jon Flanagan.

**d9: Bonifazio Bevilacqua Aldobrandini**

- [d9s0] Bonifazio Bevilacqua Aldobrandini (1571 – April 7, 1627) was an Italian Cardinal.
- [d9s1] He was the uncle of Pope Gregory XIV.

**d10: Christopher H. Clark**

- [d10s0] Christopher Henderson Clark (1767 – November 21, 1828) was a congressman and lawyer from Virginia.
- [d10s1] He was the brother of James Clark, the uncle of John Bullock Clark, Sr. and the great-uncle of John Bullock Clark, Jr..

## 15. 2wikimultihopqa_6d9e710e0bdb11eba7f7acde48001122

原位置：`train` 第 45 题 · 全局第 45 题 · `sample_id: 2wikimultihopqa_6d9e710e0bdb11eba7f7acde48001122`

Question: Where did the director of film Crooked Straight die?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of film Crooked Straight | False | () |
| u2 | place of death of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Crooked Straight | False | [] | Jerome Storm | [['d7s0']] |
| u2 | place of death of {u1} | True | ['u1'] | Desert Hot Springs | [['d3s2']] |

### Source documents (reference only)

**d1: Jesse E. Hobson**

- [d1s0] Jesse Edward Hobson( May 2, 1911 – November 5, 1970) was the director of SRI International from 1947 to 1955.
- [d1s1] Prior to SRI, he was the director of the Armour Research Foundation.

**d2: Olav Aaraas**

- [d2s0] Olav Aaraas( born 10 July 1950) is a Norwegian historian and museum director.
- [d2s1] He was born in Fredrikstad.
- [d2s2] From 1982 to 1993 he was the director of Sogn Folk Museum, from 1993 to 2010 he was the director of Maihaugen and from 2001 he has been the director of the Norwegian Museum of Cultural History.
- [d2s3] In 2010 he was decorated with the Royal Norwegian Order of St. Olav.

**d3: Jerome Storm**

- [d3s0] Jerome Storm( November 11, 1890 – July 10, 1958) was an American film director, actor and writer.
- [d3s1] He acted in 48 films between 1914 and 1941 and directed 47 films between 1918 and 1932.
- [d3s2] He was born in Denver, Colorado, and died in Desert Hot Springs, California.

**d4: Peter Levin**

- [d4s0] Peter Levin is an American director of film, television and theatre.

**d5: S. N. Mathur**

- [d5s0] S.N. Mathur was the Director of the Indian Intelligence Bureau between September 1975 and February 1980.
- [d5s1] He was also the Director General of Police in Punjab.

**d6: Ian Barry (director)**

- [d6s0] Ian Barry is an Australian director of film and TV.

**d7: Crooked Straight**

- [d7s0] Crooked Straight is a 1919 American silent drama film directed by Jerome Storm and written by Julien Josephson.
- [d7s1] The film stars Charles Ray, Wade Boteler, Margery Wilson, Gordon Mullen, and Otto Hoffman.
- [d7s2] The film was released on November 9, 1919, by Paramount Pictures.
- [d7s3] It is not known whether the film currently survives.

**d8: Brian Kennedy (gallery director)**

- [d8s0] Brian Patrick Kennedy( born 5 November 1961) is an Irish- born art museum director who has worked in Ireland and Australia, and now lives and works in the United States.
- [d8s1] He is currently the director of the Peabody Essex Museum.
- [d8s2] He was the director of the Toledo Museum of Art in Ohio from 2010 to 2019.
- [d8s3] He was the director of the Hood Museum of Art from 2005 to 2010, and the National Gallery of Australia( Canberra) from 1997- 2004.

**d9: Dana Blankstein**

- [d9s0] Dana Blankstein- Cohen( born March 3, 1981) is the director of the Israeli Academy of Film and Television.
- [d9s1] She is a film director, and an Israeli culture entrepreneur.

**d10: Michael Govan**

- [d10s0] Michael Govan( born 1963) is the director of the Los Angeles County Museum of Art since 2006.
- [d10s1] Prior to this, Govan worked as the director of the Dia Art Foundation in New York City.

## 16. 2wikimultihopqa_6dde19e80baf11ebab90acde48001122

原位置：`train` 第 46 题 · 全局第 46 题 · `sample_id: 2wikimultihopqa_6dde19e80baf11ebab90acde48001122`

Question: Who is the paternal grandfather of Albero I Of Louvain?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Albero I Of Louvain | False | () |
| u2 | father of {u1}, Albero I Of Louvain's paternal grandfather | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Albero I of Louvain | False | [] | Henry II, Count of Louvain | [['d10s1']] |
| u2 | father of {u1}, Albero I of Louvain's paternal grandfather | True | ['u1'] | Lambert II, Count of Louvain | [['d3s1']] |

### Source documents (reference only)

**d1: Henry III, Count of Louvain**

- [d1s0] Henry III of Louvain( German:" Heinrich", Dutch:" Hendrik", French:" Henri"; died 1095), was count of Louvain( Leuven) and landgrave of Brabant, son of Henry II( c. 1020 – 1078), count of Louvain and Brussels, and Adela of Orthen( or Betuwe), a daughter of Count Everard of Orthen.

**d2: Albero III of Kuenring**

- [d2s0] Albero III of Kuenring, born 1115/18 and died 15 August 1182, was a ministerialis from the noble house of Kuenring in Austria.
- [d2s1] He was the first- born son of Albero I of Kuenring, who died around 1118.

**d3: Henry II, Count of Louvain**

- [d3s0] Henry II( German:" Heinrich", Dutch:" Hendrik", French:" Henri") was Count of Louvain( Leuven) from 1054 through 1071.
- [d3s1] Henry II was the son of Lambert II, Count of Louvain and Oda of Verdun.
- [d3s2] His maternal uncles included Pope Stephen X and Godfrey the Bearded, Duke of Lorraine.

**d4: Lyon Cohen**

- [d4s0] Lyon Cohen( 1868–1937) was a Polish- born Canadian businessman and a philanthropist.
- [d4s1] He was the grandfather of singer/ poet Leonard Cohen.

**d5: John Westley**

- [d5s0] Rev. John Westley( 1636 – 78) was an English nonconformist minister.
- [d5s1] He was the grandfather of John Wesley( founder of Methodism).

**d6: Henry Krause**

- [d6s0] Henry J." Red" Krause, Jr.( August 28, 1913 – February 20, 1987) was an American football offensive lineman in the National Football League for the Brooklyn Dodgers and the Washington Redskins.
- [d6s1] He played college football at St. Louis University.
- [d6s2] He is the grandfather of Jennifer Krause
- [d6s3] He is the great grandfather of Payton Hoeing

**d7: Kaya Alp**

- [d7s0] Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

**d8: Fred Le Deux**

- [d8s0] Frederick" Fred" Le Deux( born 4 December 1934) was an Australian rules footballer who played with Geelong in the Victorian Football League( VFL).
- [d8s1] He is the grandfather of Tom Hawkins.

**d9: Abd al-Muttalib**

- [d9s0] Abd al- Muttalib Shaybah ibn Hashim( c. 497 – 578) was the grandfather of Islamic prophet Muhammad.

**d10: Albero I of Louvain**

- [d10s0] Albero I of Louvain (1070 – 1 January 1128) was the 57th Prince-Bishop of Liège from 1123 until his death.
- [d10s1] Albero was the third son of Henry II, Count of Leuven and Adela of Tweisterbant.
- [d10s2] After the suspicious death of Prince-Bishop Frederick of Liege in 1121, Holy Roman Emperor Henry V appointed Alexander of Jülich as his successor.
- [d10s3] But Friedrich von Schwarzenburg, Archbishop of Cologne refused to ordain Alexander, and the see remained vacant.
- [d10s4] The next year, the Concordat of Worms was signed between the Emperor and Pope Callixtus II.
- [d10s5] As a consequence, Albero of Leuven became the new Bishop of Liège in 1123.
- [d10s6] Albero restored order in the Bishopric with the support of his brother Godfrey I, Count of Leuven.

## 17. 2wikimultihopqa_700d51200baf11ebab90acde48001122

原位置：`train` 第 47 题 · 全局第 47 题 · `sample_id: 2wikimultihopqa_700d51200baf11ebab90acde48001122`

Question: Who is Isolde Beidler's maternal grandfather?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | mother of Isolde Beidler | False | () |
| u2 | father of {u1}, Isolde Beidler's maternal grandfather | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | mother of Isolde Beidler | False | [] | Cosima Wagner | [['d5s0']] |
| u2 | father of {u1}, Isolde Beidler's maternal grandfather | True | ['u1'] | Franz Liszt | [['d10s0']] |

### Source documents (reference only)

**d1: Fujiwara no Nagara**

- [d1s0] , also known as Fujiwara no Nagayoshi, was a Japanese statesman, courtier and politician of the early Heian period.
- [d1s1] He was the grandfather of Emperor Yōzei.

**d2: Lyon Cohen**

- [d2s0] Lyon Cohen( 1868–1937) was a Polish- born Canadian businessman and a philanthropist.
- [d2s1] He was the grandfather of singer/ poet Leonard Cohen.

**d3: Abd al-Muttalib**

- [d3s0] Abd al- Muttalib Shaybah ibn Hashim( c. 497 – 578) was the grandfather of Islamic prophet Muhammad.

**d4: Kaya Alp**

- [d4s0] Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

**d5: Isolde Beidler**

- [d5s0] Isolde Beidler (born Isolde von Bülow: 10 April 1865 – 7 February 1919) was the third of the five stepchildren and children of the composer Richard Wagner and his wife, who is generally known as Cosima Wagner (though the two of them married only in 1870).
- [d5s1] Isolde herself married the Swiss-born conductor (1872-1930) and was the mother of author (1901-1981), celebrated at his birth as "Richard Wagner's first grandchild".
- [d5s2] In view of the enduring interest in Richard Wagner's antisemitic opinions, it becomes intriguing that in 1923 Isolde Beidler posthumously acquired a Jewish daughter-in-law.

**d6: John Westley**

- [d6s0] Rev. John Westley( 1636 – 78) was an English nonconformist minister.
- [d6s1] He was the grandfather of John Wesley( founder of Methodism).

**d7: Guillaume Wittouck**

- [d7s0] Guillaume Wittouck( 1749- 1829) was a Belgian lawyer and High Magistrate.
- [d7s1] He was the Grandfather of industrialist Paul Wittouck.

**d8: Henry Bryant (naturalist)**

- [d8s0] Henry Bryant( May 12, 1820 – February 2, 1867) was an American physician and naturalist.
- [d8s1] He was the grandfather of Henry Bryant Bigelow.

**d9: Prithvipati Shah**

- [d9s0] Prithvipati Shah( ?–1716) was the king of the Gorkha Kingdom in the Indian subcontinent, present- day Nepal.
- [d9s1] He was the grandfather of Nara Bhupal Shah.

**d10: Cosima Wagner**

- [d10s0] Cosima Wagner (born Francesca Gaetana Cosima Liszt; 24 December 1837 – 1 April 1930) was the illegitimate daughter of the Hungarian pianist and composer Franz Liszt and Marie d'Agoult.
- [d10s1] She became the second wife of the German composer Richard Wagner, and with him founded the Bayreuth Festival as a showcase for his stage works; after his death she devoted the rest of her life to the promotion of his music and philosophy.
- [d10s2] Commentators have recognised Cosima as the principal inspiration for Wagner's later works, particularly "Parsifal".
- [d10s3] In 1857, after a childhood largely spent under the care of her grandmother and with governesses, Cosima married the conductor Hans von Bülow.
- [d10s4] Although the marriage produced two children, it was largely a loveless union, and in 1863 Cosima began a relationship with Wagner, who was 24 years her senior.
- [d10s5] She married him in 1870; after his death in 1883 she directed the Bayreuth Festival for more than 20 years, increasing its repertoire to form the Bayreuth canon of ten operas and establishing the festival as a major event in the world of musical theatre.
- [d10s6] During her directorship, Cosima opposed theatrical innovations and adhered closely to Wagner's original productions of his works, an approach continued by her successors long after her retirement in 1907.
- [d10s7] She shared Wagner's convictions of German cultural and racial superiority, and under her influence, Bayreuth became increasingly identified with antisemitism.
- [d10s8] This was a defining aspect of Bayreuth for decades, into the Nazi era which closely followed her death in 1930.
- [d10s9] Thus, although she is widely perceived as the saviour of the festival, her legacy remains controversial.

## 18. 2wikimultihopqa_71900dca0bdd11eba7f7acde48001122

原位置：`train` 第 48 题 · 全局第 48 题 · `sample_id: 2wikimultihopqa_71900dca0bdd11eba7f7acde48001122`

Question: What is the place of birth of the director of film A Simple Twist Of Fate?

Note:

Type: bridge · fallback: False · SFT snapshots: 6

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of film A Simple Twist Of Fate | False | () |
| u2 | place of birth of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film A Simple Twist of Fate | False | [] | Gillies MacKinnon | [['d10s0']] |
| u2 | place of birth of {u1} | True | ['u1'] | Glasgow | [['d9s0']] |

### Source documents (reference only)

**d1: Olav Aaraas**

- [d1s0] Olav Aaraas( born 10 July 1950) is a Norwegian historian and museum director.
- [d1s1] He was born in Fredrikstad.
- [d1s2] From 1982 to 1993 he was the director of Sogn Folk Museum, from 1993 to 2010 he was the director of Maihaugen and from 2001 he has been the director of the Norwegian Museum of Cultural History.
- [d1s3] In 2010 he was decorated with the Royal Norwegian Order of St. Olav.

**d2: The Irony of Fate 2**

- [d2s0] The Irony of Fate 2 or The Irony of Fate: Continuation(" Ironiya sud ’by.
- [d2s1] Prodolzheniye") is a 2007 Russian romantic comedy film directed by Timur Bekmambetov based on a screenplay by Aleksey Slapovsky produced by Channel One and released by Mosfilm.
- [d2s2] It is a direct sequel of the first" The Irony of Fate".
- [d2s3] It was originally rumored to be put in production in a press release, dedicated to the original movie's 30th anniversary in 2005.
- [d2s4] " Irony of Fate" earned$ 55,000,000 in total from its gross box- office release, with$ 49,000,000 coming from the Russian box- office alone.

**d3: Peter Levin**

- [d3s0] Peter Levin is an American director of film, television and theatre.

**d4: Ian Barry (director)**

- [d4s0] Ian Barry is an Australian director of film and TV.

**d5: General Hospital: Twist of Fate**

- [d5s0] General Hospital:
- [d5s1] Twist of Fate is the only primetime episode of the long- running ABC( ABC Daytime) soap opera" General Hospital".
- [d5s2] The primetime special aired on Saturday at 9 PM ET/ PT on December 14, 1996.

**d6: Hugh Fate**

- [d6s0] Hugh Berry" Bud" Fate( born December 4, 1929) is an American politician in the state of Alaska.
- [d6s1] He served in the Alaska House of Representatives from 2002 to 2005, representing Fairbanks as a Republican.
- [d6s2] He is a former dentist.
- [d6s3] From 1951 to 1953, he served in the United States Army Signal Corps.

**d7: Marion Laine**

- [d7s0] Marion Laine is a French actor, screenwriter and film director.
- [d7s1] Her 2008 film" A Simple Heart" was entered into the 30th Moscow International Film Festival where it won the Special Jury Prize.

**d8: Twist of Fate (film)**

- [d8s0] Twist of Fate, also known as Beautiful Stranger, is a 1954 British and American mystery film noir directed by David Miller and starring Ginger Rogers and Herbert Lom.

**d9: Gillies MacKinnon**

- [d9s0] Gillies MacKinnon (born 8 January 1948, Glasgow) is a Scottish film director, writer and painter.
- [d9s1] He attended the Glasgow School of Art where he studied mural painting.
- [d9s2] Following this he became an art teacher and cartoonist, and about this time he traveled with a nomadic tribe in the Sahara for six months.
- [d9s3] In the 1970s he studied at the Middlesex Polytechnic and in the 1980s in the National Film and Television School.
- [d9s4] He made a short film called "Passing Glory" as his graduation piece, a dour recreation of Glasgow in the 1950s and 1960s.
- [d9s5] It was premiered at the 1986 Edinburgh International Film Festival, where it won the first Scottish Film Prize.

**d10: A Simple Twist of Fate**

- [d10s0] A Simple Twist of Fate is a 1994 American comedy-drama film directed by Gillies MacKinnon.
- [d10s1] The screenplay by Steve Martin is loosely based on the 1861 novel "Silas Marner" by George Eliot.
- [d10s2] Martin stars, along with Gabriel Byrne, Laura Linney, Catherine O'Hara and Stephen Baldwin.

## 19. 2wikimultihopqa_74b339c40baf11ebab90acde48001122

原位置：`train` 第 49 题 · 全局第 49 题 · `sample_id: 2wikimultihopqa_74b339c40baf11ebab90acde48001122`

Question: Who is Cacamatzin's paternal grandfather?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Cacamatzin | False | () |
| u2 | father of {u1}, Cacamatzin's paternal grandfather | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Cacamatzin | False | [] | Nezahualpilli | [['d9s1'], ['d10s10', 'd9s0']] |
| u2 | father of {u1}, Cacamatzin's paternal grandfather | True | ['u1'] | Nezahualcoyotl | [['d10s0']] |

### Source documents (reference only)

**d1: John Westley**

- [d1s0] Rev. John Westley( 1636 – 78) was an English nonconformist minister.
- [d1s1] He was the grandfather of John Wesley( founder of Methodism).

**d2: Zhao Shoushan**

- [d2s0] Zhao Shoushan( 12 November 1894 – 20 June 1965) was a KMT general and later Chinese Communist Party politician.
- [d2s1] He is the grandfather of Zhao Leji.

**d3: John Mackay (poet)**

- [d3s0] John Mackay( 1656–1754), known as( The Blind Piper), was a Scottish Gaelic poet and composer, and the grandfather of William Ross.

**d4: Abd al-Muttalib**

- [d4s0] Abd al- Muttalib Shaybah ibn Hashim( c. 497 – 578) was the grandfather of Islamic prophet Muhammad.

**d5: Kaya Alp**

- [d5s0] Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

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

**d9: Cacamatzin**

- [d9s0] Cacamatzin (or Cacama) (1483–1520) was the tlatoani (ruler) of Texcoco, the second most important city of the Aztec Empire.
- [d9s1] Cacamatzin was a son of the previous king Nezahualpilli by one of his mistresses.
- [d9s2] Traditionally, the Texcocan kings were elected by the nobility from the most able of the royal family.
- [d9s3] Cacamatzin's election to the throne in 1515 was said to have been made under considerable pressure from Moctezuma II, lord of Tenochtitlán.
- [d9s4] Moctezuma II wished to lessen Texcoco's power in favor of greater centralization in Tenochtitlán.
- [d9s5] Cacamatzin wrote "Cacamatzin IcuicSong of Cacamatzin"), invoking his father and grandfather; he seems to protest against Pedro de Alvarado's attack during the festival of Tóxcatl.
- [d9s6] Moctezuma II, under orders from Cortés, had Cacamatzin arrested "in his own palace while discussing war-preparations".
- [d9s7] The "Caciques" of Coyoacan, Iztapalapa, and Tacuba were also arrested.
- [d9s8] Cacamatzin died during the retreat of Spanish conquistador Hernán Cortés, on the La Noche Triste.

**d10: Nezahualpilli**

- [d10s0] Nezahualpilli (Nahuatl for "fasting prince"; 1464–1515) was ruler ("tlatoani") of the Mesoamerican city-state of Texcoco, elected by the city's nobility after the death of his father, Nezahualcoyotl, in 1472.
- [d10s1] Like his father, he was a poet, was considered a sage, and had the reputation of being a fair ruler.
- [d10s2] Only one of his poems survives: Icuic Nezahualpilli yc tlamato huexotzinco ("Song of Nezahualpilli during the war with Huexotzinco").
- [d10s3] His court was a haven for astronomers, engineers, and soothsayers.
- [d10s4] During his reign, he abolished capital punishment for a number of crimes and struggled to keep the political independence of Texcoco during the increasing centralization of Aztec power in Tenochtitlán.
- [d10s5] When he told Moctezuma II that the Texcocan wise men had foretold foreign dominion over the Valley of Mexico, the emperor challenged him to a ball game.
- [d10s6] Moctezuma considered the loss of the game a negative omen.
- [d10s7] He married a daughter of Ahuitzotl only to later have her executed.
- [d10s8] Her public improprieties and high social status qualified her for a punishment that would not have been applicable to someone of a lower status.
- [d10s9] He was said to have taken numerous consorts and fathered 144 children.
- [d10s10] Nezahualpilli was succeeded by his son Cacama.

## 20. 2wikimultihopqa_74c8e33c0baf11ebab90acde48001122

原位置：`train` 第 50 题 · 全局第 50 题 · `sample_id: 2wikimultihopqa_74c8e33c0baf11ebab90acde48001122`

Question: Who is the maternal grandmother of Edmund Mortimer (Died 1331)?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | mother of Edmund Mortimer | False | () |
| u2 | mother of {u1}, Edmund Mortimer's maternal grandmother | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | mother of Edmund Mortimer (died 1331) | False | [] | Joan de Geneville, 2nd Baroness Geneville | [['d4s0']] |
| u2 | mother of {u1}, Edmund Mortimer's maternal grandmother | True | ['u1'] | Joan of Lusignan | [['d1s0']] |

### Source documents (reference only)

**d1: Joan de Geneville, 2nd Baroness Geneville**

- [d1s0] Joan de Geneville, 2nd Baroness Geneville, Countess of March, Baroness Mortimer (2 February 1286 – 19 October 1356), also known as Jeanne de Joinville, was the daughter of Sir Piers de Geneville and Joan of Lusignan.
- [d1s1] She inherited the estates of her grandparents, Geoffrey de Geneville, 1st Baron Geneville, and Maud de Lacy, Baroness Geneville.
- [d1s2] She was one of the wealthiest heiresses in the Welsh Marches and County Meath, Ireland.
- [d1s3] She was the wife of Roger Mortimer, 1st Earl of March, the de facto ruler of England from 1327 to 1330.
- [d1s4] She succeeded as suo jure 2nd Baroness Geneville on 21 October 1314 upon the death of her grandfather, Geoffrey de Geneville.
- [d1s5] As a result of her husband's insurrection against King Edward II of England, she was imprisoned in Skipton Castle for two years.
- [d1s6] Following the execution of her husband in 1330 for usurping power in England, Joan was once more taken into custody.
- [d1s7] In 1336, her lands were restored to her after she received a full pardon for her late husband's crimes from Edward II's son and successor, Edward III of England.

**d2: Mona Hopton Bell**

- [d2s0] Mona Hopton Bell( 1867- 1940) was a British artist, best known for her portraits of civic figures.
- [d2s1] She was the grandmother of the painter Jean H. Bell.

**d3: Purnima (Hindi actress)**

- [d3s0] Purnima Das Verma( born Meherbhano Mohammad Ali) was an Indian film actress who worked predominantly in Hindi language films.
- [d3s1] She is the grandmother of actor Emraan Hashmi.

**d4: Edmund Mortimer (died 1331)**

- [d4s0] Sir Edmund Mortimer (1302/1303 – 16 December 1331) was the eldest son of Roger Mortimer, 1st Earl of March and Joan de Geneville, 2nd Baroness Geneville.
- [d4s1] By his wife Elizabeth de Badlesmere he was the father of Roger Mortimer, 2nd Earl of March.
- [d4s2] Though Edmund survived his father by one year, he did not inherit his father's lands and titles as they were forfeited to the Crown and his son only reacquired them gradually.

**d5: Hannah Arnold**

- [d5s0] Hannah Arnold, also known as Hannah Waterman King, was the grandmother of Benedict Arnolds children.

**d6: Anne Denman**

- [d6s0] Anne Denman( 1587–1661) was born in Olde Hall, Retford, Nottinghamshire.
- [d6s1] Through a fortunate second marriage with Thomas Aylesbury, she became the grandmother of Lady Anne Hyde, Duchess of York and great- grandmother of Queen Mary II and Queen Anne.

**d7: Kaoru Hatoyama**

- [d7s0] After the elections of 2009, she became more widely known as the grandmother of Prime Minister Yukio Hatoyama and his politician brother Kunio Hatoyama.

**d8: Tjuyu**

- [d8s0] Tjuyu( sometimes transliterated as Thuya or Thuyu) was an Egyptian noblewoman and the mother of queen Tiye, and the wife of Yuya.
- [d8s1] She is the grandmother of Akhenaten, and great grandmother of Tutankhamun.

**d9: Diana Guardato**

- [d9s0] Diana Guardato was a member of the aristocratic Patrician Guardato family, and had three children with King Ferdinand I: Diana Guardato is the 16th- Great Grandmother of His Royal Highness Albert II of Belgium, 15th- Great Grandmother of His Majesty Juan Carlos
- [d9s1] I of Spain, 17th- Great Grandmother of Philippe of Belgium, 14th- Great Grandmother of His Majesty Manuel II of Portugal, 16th- Great Grandmother of Grand Duke Henri, as well as many others.

**d10: Hubba bint Hulail**

- [d10s0] Hubba bint Hulail was the grandmother of Hashim ibn' Abd Manaf, thus the great- great- great- grandmother of the Islamic" Nabī"( Prophet) Muhammad ibn Abdullah.

## 21. 2wikimultihopqa_75141b5d086911ebbd5eac1f6bf848b6 【需改：生成拆解】

原位置：`train` 第 51 题 · 全局第 51 题 · `sample_id: 2wikimultihopqa_75141b5d086911ebbd5eac1f6bf848b6`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_75141b5d086911ebbd5eac1f6bf848b6"></a>

> **审阅结论：需改：生成拆解**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 已有完整的两条“导演→国籍”链和比较结论，5 个单元结构正确，但 question_type 被写成 comparison。
>
> **处理建议：** 将 question_type 改为 bridge_comparison；u2/u4 建议明确为 nationality，避免 country of origin 被理解为出生地。
>
> **证据定位：** d9s0, d6s0, d2s0, d5s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Do both Americanizing Shelley and Road Agent (1952 film) films have the directors from the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of Americanizing Shelley | False | () |
| u2 | country of origin of {u1} | False | ('u1',) |
| u3 | director of Road Agent (1952 film) | False | () |
| u4 | country of origin of {u3} | False | ('u3',) |
| u5 | whether {u2} and {u4} are the same | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of Americanizing Shelley | False | [] | Lorraine Senna | [['d9s0']] |
| u2 | nationality of {u1} | False | ['u1'] | American | [['d6s0']] |
| u3 | director of Road Agent (1952 film) | False | [] | Lesley Selander | [['d2s0']] |
| u4 | nationality of {u3} | False | ['u3'] | American | [['d5s0']] |
| u5 | whether the directors of Americanizing Shelley and Road Agent (1952 film) are from the same country | True | ['u2', 'u4'] | yes | [[]] |

### Source documents (reference only)

**d1: Trail Guide**

- [d1s0] Trail Guide is a 1952 film directed by Lesley Selander and starring Tim Holt.
- [d1s1] It lost$ 20,000.

**d2: Road Agent (1952 film)**

- [d2s0] Road Agent is a 1952 Western film directed by Lesley Selander and starring Tim Holt and Richard Martin.
- [d2s1] Principal supporting cast members included Noreen Nash and Mauritz Hugo.
- [d2s2] Mary Jo Traolta made her film debut as the romantic lead.

**d3: The First Time (1952 film)**

- [d3s0] The First Time is a 1952 film directed by Frank Tashlin, and starring Robert Cummings and Barbara Hale.

**d4: Dave Hebner**

- [d4s0] David Hebner( born May 17, 1949) is an American professional wrestling authority figure, promoter, road agent, and referee.

**d5: Lesley Selander**

- [d5s0] Lesley Selander( May 26, 1900 – December 5, 1979) was an American film director of Westerns and adventure movies.
- [d5s1] His career as director, spanning 127 feature films and dozens of TV episodes, lasted from 1936- 68.
- [d5s2] Before that, Selander was assistant director on films such as" The Cat and the Fiddle"( 1934)," A Night at the Opera"( 1935), and Fritz Lang's" Fury"( 1936).
- [d5s3] To this day Selander remains one of the most prolific directors of feature Westerns in cinema history, having taken the helm for 107 Westerns between his first directorial feature in 1936 and 1967.
- [d5s4] In 1956 he was nominated for the Directors Guild of America award for Outstanding Directorial Achievement in Television, for his work directing a 1954 episode of" Lassie".

**d6: Lorraine Senna**

- [d6s0] Lorraine Senna (sometimes credited as Lorraine Senna Ferrara) is an American film and television director.

**d7: No Time for Flowers**

- [d7s0] No Time for Flowers is a 1952 film directed by Don Siegel.

**d8: Something for the Birds**

- [d8s0] Something for the Birds is a 1952 film directed by Robert Wise and starring Victor Mature and Patricia Neal.

**d9: Americanizing Shelley**

- [d9s0] Americanizing Shelley is a 2007 Hollywood romantic comedy film directed by Lorraine Senna and starring Beau Bridges, Namrata Singh Gujral, Shaheen Khan, Wil Wheaton, Noureen DeWulf, Tony Yalda, and Ajay Mehta.

**d10: Lost in Alaska**

- [d10s0] Lost in Alaska is a 1952 film starring the comedy team of Abbott and Costello.

## 22. 2wikimultihopqa_75de80fc0bdb11eba7f7acde48001122

原位置：`train` 第 52 题 · 全局第 52 题 · `sample_id: 2wikimultihopqa_75de80fc0bdb11eba7f7acde48001122`

Question: Where was the director of film The Boy Who Stole A Million born?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of The Boy Who Stole A Million | False | () |
| u2 | birthplace of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film The Boy Who Stole a Million | False | [] | Charles Crichton | [['d2s0']] |
| u2 | place of birth of {u1} | True | ['u1'] | Wallasey | [['d3s1']] |

### Source documents (reference only)

**d1: The Boy Who Stole the Elephant**

- [d1s0] The Boy Who Stole the Elephant is a 1970 American TV movie starring Mark Lester.
- [d1s1] It was originally filmed as a two part episode of" The Wonderful World of Disney".
- [d1s2] It was filmed in December 1969.

**d2: The Boy Who Stole a Million**

- [d2s0] The Boy Who Stole a Million is a 1960 British comedy thriller film directed by Charles Crichton.
- [d2s1] The film was shot on location in the Spanish city of Valencia, with an international cast list.

**d3: Charles Crichton**

- [d3s0] Charles Ainslie Crichton (6 August 1910 – 14 September 1999) was an English film director and editor.
- [d3s1] Born in Wallasey, Cheshire, he became best known for directing many comedies produced at Ealing Studios and had a 40-year career editing and directing many films and television programmes.
- [d3s2] For the acclaimed comedy "A Fish Called Wanda" (1988), Crichton was nominated for both the Academy Award for Best Director and the Academy Award for Best Original Screenplay (along with the film's star John Cleese).

**d4: Boy Who Caught a Crook**

- [d4s0] The Boy Who Caught a Crook is a 1961 children's film about a young boy who tracks down a gangster.

**d5: Olav Aaraas**

- [d5s0] Olav Aaraas( born 10 July 1950) is a Norwegian historian and museum director.
- [d5s1] He was born in Fredrikstad.
- [d5s2] From 1982 to 1993 he was the director of Sogn Folk Museum, from 1993 to 2010 he was the director of Maihaugen and from 2001 he has been the director of the Norwegian Museum of Cultural History.
- [d5s3] In 2010 he was decorated with the Royal Norwegian Order of St. Olav.

**d6: Jared Breeze**

- [d6s0] Jared Breeze is an American child actor.
- [d6s1] He starred in the title role of the 2015 film" The Boy".

**d7: Ian Barry (director)**

- [d7s0] Ian Barry is an Australian director of film and TV.

**d8: Peter Levin**

- [d8s0] Peter Levin is an American director of film, television and theatre.

**d9: The Boy Mir**

- [d9s0] The Boy Mir is documentary film about ten years life of a Hazara boy in Afghanistan.
- [d9s1] This film was made after an international hit film" The Boy who Plays on the Buddhas of Bamiyan" by a British film maker Phil Grabsky.

**d10: René Million**

- [d10s0] René Million( born 23 March 1934) is a French former swimmer.
- [d10s1] He competed in the men's 400 metre freestyle at the 1952 Summer Olympics.

## 23. 2wikimultihopqa_77ee511408c111ebbd8bac1f6bf848b6

原位置：`train` 第 53 题 · 全局第 53 题 · `sample_id: 2wikimultihopqa_77ee511408c111ebbd8bac1f6bf848b6`

Question: Which film has the director who is older, Prairie Badmen or Jimmy, the Boy Wonder?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of Prairie Badmen | False | () |
| u2 | birth date of {u1} | False | ('u1',) |
| u3 | director of Jimmy, the Boy Wonder | False | () |
| u4 | birth date of {u3} | False | ('u3',) |
| u5 | which film's director is older | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of Prairie Badmen | False | [] | Sam Newfield | [['d1s0']] |
| u2 | date of birth of {u1} | False | ['u1'] | December 6, 1899 | [['d5s0']] |
| u3 | director of Jimmy, the Boy Wonder | False | [] | Herschell Gordon Lewis | [['d9s1']] |
| u4 | date of birth of {u3} | False | ['u3'] | June 15, 1926 | [['d4s0']] |
| u5 | which of Prairie Badmen and Jimmy, the Boy Wonder has the older director | True | ['u2', 'u4'] | Prairie Badmen | [[]] |

### Source documents (reference only)

**d1: Prairie Badmen**

- [d1s0] Prairie Badmen is a 1946 American Western film directed by Sam Newfield and written by Fred Myton.
- [d1s1] The film stars Buster Crabbe, Al St. John, Patricia Knox, Charles King, Ed Cassidy and Kermit Maynard.
- [d1s2] The film was released on July 17, 1946, by Producers Releasing Corporation.

**d2: Douglas Croft**

- [d2s0] Douglas Croft( August 12, 1926 – October 24, 1963), born Douglas Malcom Wheatcroft, was an American child actor who is best remembered for being the first person to portray the DC Comics character Robin, the Boy Wonder, as well as his secret identity Dick Grayson, in the 1943 serial" Batman" when he was 16 years old.

**d3: Scotty Fox**

- [d3s0] Scott Fox is a pornographic film director who is a member of the AVN Hall of Fame.

**d4: Herschell Gordon Lewis**

- [d4s0] Herschell Gordon Lewis( June 15, 1926 – September 26, 2016) was an American filmmaker, best known for creating the" splatter" subgenre of horror films.
- [d4s1] He is often called the" Godfather of Gore"( a title also given to Lucio Fulci), though his film career included works in a range of exploitation film genres including juvenile delinquent films, nudie-cuties, two children's films and at least one rural comedy.
- [d4s2] On Lewis' career, All Movie wrote," With his better- known gore films, Herschell Gordon Lewis was a pioneer, going farther than anyone else dared, probing the depths of disgust and discomfort onscreen with more bad taste and imagination than anyone of his era."

**d5: Sam Newfield**

- [d5s0] Sam Newfield, born Samuel Neufeld,( December 6, 1899- November 10, 1964), also known as Sherman Scott or Peter Stewart, was an American B-movie director, one of the most prolific in American film history —he is credited with directing over 250 feature films in a career which began during the silent era and ended in 1958.
- [d5s1] In addition to his staggering feature output, he also directed one- and two- reel comedy shorts, training films, industrial films, TV episodes and pretty much anything anyone would pay him for.
- [d5s2] Because of this massive output—he would sometimes direct more than 20 films in a single year —he has been called the most prolific director of the sound era.
- [d5s3] Many of Newfield's films were made for PRC Pictures.
- [d5s4] This was a film production company headed by his brother Sigmund Neufeld.
- [d5s5] The films PRC produced were low- budget productions, the majority being westerns, with an occasional horror film or crime drama.

**d6: Jimmy Flint**

- [d6s0] Jimmy' The Wapping Assassin' Flint( born 6 November 1952) is an English actor, playwright and retired boxer.

**d7: Elliot Silverstein**

- [d7s0] Elliot Silverstein( born August 3, 1927, in Boston, Massachusetts) is an American director, who is best known for being the director of the movie" Cat Ballou"( 1965).

**d8: Ben Palmer**

- [d8s0] Ben Palmer is a British film and television director who is known for being the director of" Bo' Selecta" and" The Inbetweeners".

**d9: Jimmy, the Boy Wonder**

- [d9s0] Jimmy, the Boy Wonder is a 1966 children's musical film about a boy, played by Dennis Jones, who successfully stops time.
- [d9s1] The film is one of two children's features directed by Herschell Gordon Lewis, the other being" The Magic Land of Mother Goose", who is better known for his gory splatter films.
- [d9s2] It was described as a" glorious bomb" by the" Scarecrow Video Movie Guide".

**d10: Justin Whitlock Dart Sr.**

- [d10s0] Justin Whitlock
- [d10s1] Dart, Sr.( August 17, 1907 – January 26, 1984) was an American businessman, considered the" boy wonder" of the drug store industry.
- [d10s2] In college Dart had played football for Northwestern University.

## 24. 2wikimultihopqa_794cefac08cb11ebbd92ac1f6bf848b6

原位置：`train` 第 54 题 · 全局第 54 题 · `sample_id: 2wikimultihopqa_794cefac08cb11ebbd92ac1f6bf848b6`

Question: Who was born first, Charles School Blakely or Mike Nickeas?

Note:

Type: comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | birth date of Charles School Blakely | False | () |
| u2 | birth date of Mike Nickeas | False | () |
| u3 | who was born first | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | date of birth of Charles School Blakely | False | [] | November 6, 1880 | [['d1s0']] |
| u2 | date of birth of Mike Nickeas | False | [] | February 13, 1983 | [['d8s0']] |
| u3 | who was born first, Charles School Blakely or Mike Nickeas | True | ['u1', 'u2'] | Charles School Blakely | [[]] |

### Source documents (reference only)

**d1: Charles School Blakely**

- [d1s0] Charles School Blakely( November 6, 1880 – January 11, 1975) was an American army officer and Brigadier general who served during World War I.

**d2: Michael Clark**

- [d2s0] Michael( or Mike)
- [d2s1] Clark may refer to:

**d3: Michael Jones**

- [d3s0] Michael or Mike Jones may refer to:

**d4: Michael Miller**

- [d4s0] Michael or Mike Miller may refer to:

**d5: Michael Davis**

- [d5s0] Michael or Mike Davis may refer to:

**d6: Michael Harris**

- [d6s0] Michael or Mike Harris may refer to:

**d7: Michael Brown**

- [d7s0] Michael or Mike Brown may refer to:

**d8: Mike Nickeas**

- [d8s0] Michael James Nickeas( born February 13, 1983) is a Canadian former professional baseball catcher.
- [d8s1] Nickeas played four seasons in Major League Baseball( MLB) with the New York Mets and Toronto Blue Jays.

**d9: St. Charles School District**

- [d9s0] St. Charles School District may refer to:

**d10: Michael White**

- [d10s0] Michael or Mike White may refer to:

## 25. 2wikimultihopqa_7c7bf9860bda11eba7f7acde48001122

原位置：`train` 第 55 题 · 全局第 55 题 · `sample_id: 2wikimultihopqa_7c7bf9860bda11eba7f7acde48001122`

Question: What is the date of birth of the director of film The Lost Language Of Cranes (Film)?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of The Lost Language Of Cranes (Film) | False | () |
| u2 | date of birth of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film The Lost Language of Cranes | False | [] | Nigel Finch | [['d4s0']] |
| u2 | date of birth of {u1} | True | ['u1'] | 1 August 1949 | [['d2s0']] |

### Source documents (reference only)

**d1: Theodred II (Bishop of Elmham)**

- [d1s0] Theodred II was a medieval Bishop of Elmham.
- [d1s1] The date of Theodred's consecration unknown, but the date of his death was sometime between 995 and 997.

**d2: Nigel Finch**

- [d2s0] Nigel Lucius Graeme Finch (1 August 1949 – 14 February 1995) was an English film director and filmmaker whose career influenced the growth of British gay cinema.

**d3: Terence Robinson**

- [d3s0] Terence D. Robinson( date of birth and death unknown) was a male wrestler who competed for England.

**d4: The Lost Language of Cranes (film)**

- [d4s0] The Lost Language of Cranes is a 1991 British television film directed by Nigel Finch.
- [d4s1] Made by the BBC for their "Screen Two" series; it is an adaptation of the 1986 novel of the same name by David Leavitt.
- [d4s2] Whereas the novel is set in New York with American characters, the film takes place in London.
- [d4s3] Though most of the characters in the film are British, the characters of Elliot, Geoffrey and Winston are American, and the story is essentially that of the novel.

**d5: Brian Saunders (weightlifter)**

- [d5s0] Brian Saunders( date of birth and death unknown) was a male weightlifter who competed for England.

**d6: Les Richards**

- [d6s0] Les Richards( date of birth unknown) was an Australian rules footballer who played with North Melbourne in the Victorian Football League( VFL).

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

**d8: Julian Wastall**

- [d8s0] Julian Wastall( 18 September 1958 – 11 January 1994) was a composer working in film and TV including the successful Granada TV series" Cracker"( 1993) and" The Lost Language of Cranes"( 1991).
- [d8s1] Other credits include" Clubland"( 1991)," GamesMaster"( 1992)," Revolver"( 1991) and" Angels"( 1992).
- [d8s2] As' Jules Wastall' he is credited with the theme music for Channel 4's gay and lesbian magazine show' Out On Tuesday' which launched in 1989.
- [d8s3] He was awarded a BAFTA in 1992 for Best Original Music with Daemion Barry for Friday On My Mind.
- [d8s4] The classical music composer Rachel Portman ’s work, ‘ For Julian, ’ was a memorial in solo piano for her friend.

**d9: Ian Barry (director)**

- [d9s0] Ian Barry is an Australian director of film and TV.

**d10: Peter Levin**

- [d10s0] Peter Levin is an American director of film, television and theatre.

## 26. 2wikimultihopqa_85ab0d88084e11ebbd56ac1f6bf848b6

原位置：`train` 第 56 题 · 全局第 56 题 · `sample_id: 2wikimultihopqa_85ab0d88084e11ebbd56ac1f6bf848b6`

Question: Which film has the director who was born first, Texas Masquerade or Jason Bourne (Film)?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of Texas Masquerade | False | () |
| u2 | birth date of {u1} | False | ('u1',) |
| u3 | director of Jason Bourne (Film) | False | () |
| u4 | birth date of {u3} | False | ('u3',) |
| u5 | which film's director was born first | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of Texas Masquerade | False | [] | George Archainbaud | [['d5s0']] |
| u2 | date of birth of {u1} | False | ['u1'] | May 7, 1890 | [['d9s0']] |
| u3 | director of Jason Bourne (film) | False | [] | Paul Greengrass | [['d8s0'], ['d8s4'], ['d1s3']] |
| u4 | date of birth of {u3} | False | ['u3'] | 13 August 1955 | [['d1s0']] |
| u5 | which of Texas Masquerade and Jason Bourne (film) has the director born first | True | ['u2', 'u4'] | Texas Masquerade | [[]] |

### Source documents (reference only)

**d1: Paul Greengrass**

- [d1s0] Paul Greengrass( born 13 August 1955) is an English film director, film producer, screenwriter, and former journalist.
- [d1s1] He specialises in dramatisations of real- life events and is known for his signature use of hand- held cameras.
- [d1s2] His early film" Bloody Sunday" won the Golden Bear at 52nd Berlin International Film Festival.
- [d1s3] Other films he has directed include three in the" Bourne" action/ thriller series:" The Bourne Supremacy"( 2004)," The Bourne Ultimatum"( 2007), and" Jason Bourne"( 2016);" United 93"( 2006), for which he won the BAFTA Award for Best Director and received an Academy Award for Best Director nomination;" Green Zone"( 2010); and" Captain Phillips"( 2013).
- [d1s4] In 2004, he co-wrote and produced the film" Omagh", which won British Academy Television Award.
- [d1s5] In 2007, Greengrass co-founded Directors UK, a professional organization of British filmmakers, and was its first President until 2014.
- [d1s6] In 2008," The Telegraph" named him among the most influential people in British culture.
- [d1s7] In 2017, Greengrass was honoured with a British Film Institute Fellowship.

**d2: Liu Chien-sin**

- [d2s0] Liu Chien- sin or Jason Liu( born 8 June 1968) is the Deputy Secretary- General to the President of the Republic of China since 21 April 2018.

**d3: Wale Adebanwi**

- [d3s0] Wale Adebanwi( born 1969) is a Nigerian- born first Black Rhodes Professor at St Antony's College, Oxford.

**d4: The Bourne Identity (2002 film)**

- [d4s0] The Bourne Identity is a 2002 action thriller film based on Robert Ludlum's novel of the same name.
- [d4s1] It stars Matt Damon as Jason Bourne, a man suffering from extreme memory loss and attempting to discover his true identity amidst a clandestine conspiracy within the Central Intelligence Agency( CIA).
- [d4s2] The film also features Franka Potente, Chris Cooper, Clive Owen, Julia Stiles, Brian Cox, and Adewale Akinnuoye- Agbaje.
- [d4s3] The first in the" Jason Bourne" film series, it was followed by" The Bourne Supremacy"( 2004)," The Bourne Ultimatum"( 2007)," The Bourne Legacy"( 2012), and" Jason Bourne"( 2016).
- [d4s4] The film was co-produced and directed by Doug Liman and adapted for the screen by Tony Gilroy and William Blake Herron.
- [d4s5] Although Robert Ludlum died in 2001, he is credited as an executive producer alongside Frank Marshall.
- [d4s6] Universal Pictures released the film to theatres in the United States on June 14, 2002, and it received a positive critical and public reaction.

**d5: Texas Masquerade**

- [d5s0] Texas Masquerade is a 1944 American Western film directed by George Archainbaud, written by Jack Lait Jr. and Norman Houston, and starring William Boyd, Andy Clyde, Jimmy Rogers, Don Costello, Mady Correll and Francis McDonald.
- [d5s1] It was released on February 8, 1944, by United Artists.

**d6: Henry Moore (cricketer)**

- [d6s0] Henry Walter Moore( 1849 – 20 August 1916) was an English- born first- class cricketer who spent most of his life in New Zealand.

**d7: The Bourne Supremacy (film)**

- [d7s0] The Bourne Supremacy is a 2004 action thriller film featuring Robert Ludlum's Jason Bourne character.
- [d7s1] Though it takes the name of the second Bourne novel, it s plot is entirely different.
- [d7s2] The film was directed by Paul Greengrass from a screenplay by Tony Gilroy.
- [d7s3] Universal Pictures released the film to theaters in the United States on July 23, 2004.
- [d7s4] It is the second in the" Jason Bourne" film series.
- [d7s5] It is preceded by" The Bourne Identity"( 2002) and followed by" The Bourne Ultimatum"( 2007)," The Bourne Legacy"( 2012), and" Jason Bourne"( 2016).
- [d7s6] " The Bourne Supremacy" continues the story of Jason Bourne, a former CIA assassin suffering from psychogenic amnesia.
- [d7s7] Bourne is portrayed by Matt Damon.
- [d7s8] The film focuses on his attempt to learn more of his past as he is once more enveloped in a conspiracy involving the CIA and Operation Treadstone.
- [d7s9] The film also stars Brian Cox as Ward Abbott, Joan Allen as Pamela Landy and Julia Stiles as Nicky Parsons.

**d8: Jason Bourne (film)**

- [d8s0] Jason Bourne is a 2016 American action thriller film directed by Paul Greengrass and written by Paul Greengrass and Christopher Rouse.
- [d8s1] It is the fifth and final installment of the" Bourne" film series and a direct sequel to" The Bourne Ultimatum"( 2007).
- [d8s2] Matt Damon reprises his role as the main character, former CIA assassin Jason Bourne.
- [d8s3] In addition, the film stars Tommy Lee Jones, Alicia Vikander, Julia Stiles, Vincent Cassel, Riz Ahmed, Ato Essandoh and Scott Shepherd.
- [d8s4] The character Aaron Cross, from" The Bourne Legacy"( 2012), does not appear in the film because director Greengrass wanted to focus on the title character, and because actor Jeremy Renner was unable to participate due to scheduling conflicts.
- [d8s5] In" Jason Bourne", Bourne remains on the run from CIA hit squads as he tries to uncover hidden truths about his father, while CIA director Robert Dewey( Jones) orders the head of cyber- security Heather Lee( Vikander) to hunt him down.
- [d8s6] Principal photography on the film commenced on September 8, 2015.
- [d8s7] " Jason Bourne" premiered in London on July 11, 2016, and was theatrically released in the United States by Universal Pictures on July 29, 2016.
- [d8s8] The film received mixed reviews upon release; critics praised Damon's and Vikander's performances and action but criticized the story; some critics also expressed disappointment in Jeremy Renner's absence and ignoring the events of" The Bourne Legacy".
- [d8s9] Despite mixed reviews, the film was a box office success, grossing$ 415 million worldwide.

**d9: George Archainbaud**

- [d9s0] George Archainbaud( May 7, 1890 – February 20, 1959) was a French- born American film and television director.

**d10: The Bourne Legacy (film)**

- [d10s0] The Bourne Legacy is a 2012 American action thriller film directed by Tony Gilroy, and is the fourth installment in the series of films adapted from the" Jason Bourne" novels originated by Robert Ludlum and continued by Eric Van Lustbader, being preceded by" The Bourne Identity"( 2002)," The Bourne Supremacy"( 2004), and" The Bourne Ultimatum"( 2007).
- [d10s1] Although this film has the same title as Van Lustbader's first" Bourne" novel," The Bourne Legacy", the actual screenplay bears little resemblance to the novel.
- [d10s2] Unlike the novel, which features Jason Bourne as the principal character, the film centers on black ops agent Aaron Cross( played by Jeremy Renner), an original character.
- [d10s3] In addition to Renner, the film stars Rachel Weisz and Edward Norton.
- [d10s4] The titular character Jason Bourne does not appear in" The Bourne Legacy", as actor Matt Damon chose not to return for the fourth film, due to Paul Greengrass not directing.
- [d10s5] Bourne is shown in pictures and mentioned by name several times throughout the film.
- [d10s6] Tony Gilroy, co-screenwriter of the first three films, sought to continue the story of the film series without changing its key events, and parts of" The Bourne Legacy" take place at the same time as the previous film," The Bourne Ultimatum"( 2007).
- [d10s7] Aaron Cross is a member of a black ops program called Operation Outcome whose subjects are genetically enhanced.
- [d10s8] He must run for his life once former CIA Treadstone agent Jason Bourne's actions lead to the public exposure of Operation Treadstone and its successor Operation Blackbriar.
- [d10s9] Filming was primarily in New York City, with some scenes shot in the Philippines, South Korea, Pakistan, and Canada.
- [d10s10] Released on, 2012, the film received mixed reviews, with critics praising the story, but expressing disappointment in Matt Damon's absence.
- [d10s11] The film was followed in 2016 by" Jason Bourne", in which Damon reprised his earlier role.

## 27. 2wikimultihopqa_864dbcc60bdd11eba7f7acde48001122

原位置：`train` 第 57 题 · 全局第 57 题 · `sample_id: 2wikimultihopqa_864dbcc60bdd11eba7f7acde48001122`

Question: What is the place of birth of the director of film The Black Diamond (1922 Film)?

Note:

Type: bridge · fallback: False · SFT snapshots: 7

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of The Black Diamond (1922 Film) | False | () |
| u2 | place of birth of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film The Black Diamond (1922 film) | False | [] | André Hugon | [['d1s0']] |
| u2 | place of birth of {u1} | True | ['u1'] | Algiers | [['d6s1']] |

### Source documents (reference only)

**d1: The Black Diamond (1922 film)**

- [d1s0] The Black Diamond  is a 1922 French silent mystery film directed by André Hugon and starring Claude Mérelle, Ginette Maddie and Armand Bernard.

**d2: Gustave Diamond**

- [d2s0] Gustave Diamond( born January 29, 1928) is a Senior United States District Judge of the United States District Court for the Western District of Pennsylvania.

**d3: Aleska Diamond**

- [d3s0] Aleska Diamond( born August 6, 1988) is a Hungarian acrobat, escort and former pornographic film actress.

**d4: Barry Diamond (footballer)**

- [d4s0] Barry Diamond( born 20 March 1960 in Dumbarton) is a Scottish former professional footballer who played in the Football League as a forward.

**d5: Nearly a Deserter**

- [d5s0] Nearly a Deserter is a 1916 American short silent comedy film produced by the United States Motion Picture Corporation under the Black Diamond Comedy name.
- [d5s1] The film was the first Black Diamond Comedy distributed by the Paramount Pictures.

**d6: André Hugon**

- [d6s0] André Hugon( 17 December 1886 – 22 August 1960) was a French film director, screenwriter and film producer best known for his silent films from 1913 onwards, particularly of the 1920s and into sound.
- [d6s1] Hugon was born in Algiers in 1886 which at the time was part of France.
- [d6s2] He directed some 90 films between 1913 and 1952.

**d7: Debi Diamond**

- [d7s0] Debi Diamond( born May 1, 1965 in San Fernando Valley, California) is an American adult actress and nude model.

**d8: Graham Diamond**

- [d8s0] Graham Diamond( born 18 August 1949, Manchester, England) is a speculative fiction, fantasy and science fiction author.

**d9: Andrew Diamond (professor)**

- [d9s0] Andrew Jay Diamond( born 1 November 1967) is an American academic and professor of American history and civilization at the Université Paris- Sorbonne and also the Director of the Histoire et dynamique des espaces Anglophones( HDEA).

**d10: Thomas Diamond**

- [d10s0] Thomas Nicklaus Diamond( born April 6, 1983) is an American former professional baseball pitcher.
- [d10s1] He played in Major League Baseball( MLB) for the Chicago Cubs.

## 28. 2wikimultihopqa_86790dc00bda11eba7f7acde48001122

原位置：`train` 第 58 题 · 全局第 58 题 · `sample_id: 2wikimultihopqa_86790dc00bda11eba7f7acde48001122`

Question: What is the date of death of Rose Vestris's husband?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | husband of Rose Vestris | False | () |
| u2 | date of death of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | husband of Rose Vestris | False | [] | Angiolo Vestris | [['d8s2']] |
| u2 | date of death of {u1} | True | ['u1'] | 10 June 1809 | [['d2s0']] |

### Source documents (reference only)

**d1: Harry Wainwright (footballer)**

- [d1s0] Harry Wainwright( born 1899; date of death unknown) was an English footballer.

**d2: Angiolo Vestris**

- [d2s0] Angiolo Maria Gasparo Vestris (19 November 1730, Florence - 10 June 1809, Paris) was a Franco-Italian ballet dancer.
- [d2s1] The younger brother of Gaétan Vestris and Thérèse Vestris, he studied dance with Louis Dupré and became a soloist of the Opéra de Paris in 1753.
- [d2s2] He then danced at Stuttgart under the direction of Noverre (also marrying Rose Gourgaud, daughter of the comic-actor Dugazon, in the town in 1766) before returning to Paris in 1767, where he was taken on as an actor at the Comédie-Italienne.

**d3: Bill Smith (footballer, born 1897)**

- [d3s0] William Thomas Smith( born 9 April 1897, date of death unknown) was an English professional footballer.

**d4: Thomas Scott (diver)**

- [d4s0] Thomas Scott( 1907- date of death unknown) was an English diver.

**d5: Fred Bradley (rower)**

- [d5s0] Frederick Bradley( 1908- date of death unknown) was an English rower.

**d6: Theodred II (Bishop of Elmham)**

- [d6s0] Theodred II was a medieval Bishop of Elmham.
- [d6s1] The date of Theodred's consecration unknown, but the date of his death was sometime between 995 and 997.

**d7: Albert Thompson (footballer, born 1912)**

- [d7s0] Albert Thompson( born 1912, date of death unknown) was a Welsh footballer.

**d8: Rose Vestris**

- [d8s0] Françoise-Rose Gourgaud (7 April 1743, in Marseille – 5 October 1804, in Paris), stage name Madame Vestris, was a French actress.
- [d8s1] She was the sister of Pierre-Antoine Gourgaud, stage name Dugazon.
- [d8s2] She married the ballet-dancer Angiolo Vestris (Florentine in origin and a younger brother of Gaétan Vestris).

**d9: Harry Johnson (wrestler)**

- [d9s0] Harry Johnson( 1903- date of death unknown) was an English wrestler.

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

## 29. 2wikimultihopqa_8971e3ec0baf11ebab90acde48001122

原位置：`train` 第 59 题 · 全局第 59 题 · `sample_id: 2wikimultihopqa_8971e3ec0baf11ebab90acde48001122`

Question: Who is Archduchess Marie Astrid Of Austria's father-in-law?

Note:

Type: bridge · fallback: False · SFT snapshots: 7

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | husband of Archduchess Marie Astrid Of Austria | False | () |
| u2 | father of {u1}, Archduchess Marie Astrid Of Austria's father-in-law | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | husband of Archduchess Marie Astrid of Austria | False | [] | Archduke Carl Christian of Austria | [['d6s0']] |
| u2 | father of {u1}, father-in-law of Archduchess Marie Astrid of Austria | True | ['u1'] | Archduke Carl Ludwig of Austria | [['d2s1']] |

### Source documents (reference only)

**d1: John Adams (merchant)**

- [d1s0] John Adams( 1672 or 1673 – 1745) was an American- born Canadian merchant and member of the Nova Scotia Council.
- [d1s1] He was the father- in- law of Henry Newton( politician).

**d2: Archduke Carl Christian of Austria**

- [d2s0] Archduke Carl Christian of Austria (born 26 August 1954 at Château de Belœil in Belœil, Belgium) is a Belgian aristocrat and a member of the formerly ruling Austro-Hungarian House of Habsburg-Lorraine.
- [d2s1] He is the third child of Archduke Carl Ludwig of Austria and his wife, Princess Yolande de Ligne.

**d3: Archduchess Marie Valerie of Austria**

- [d3s0] Archduchess Marie Valerie of Austria (22 April 1868 – 6 September 1924) was the third daughter and fourth and last child of Franz Joseph I of Austria and Elisabeth of Bavaria.
- [d3s1] Her given name was Marie Valerie Mathilde Amalie, but she was usually called Valerie.

**d4: Archduchess Elisabeth Franziska of Austria (1892–1930)**

- [d4s0] Archduchess Elisabeth Franziska Marie Karoline Ignatia Salvator (27 January 1892 – 29 January 1930) was the eldest daughter of Archduke Franz Salvator of Austria and Archduchess Marie Valerie of Austria.
- [d4s1] Through her mother, she was a granddaughter of Emperor Franz Joseph I of Austria.

**d5: Archduchess Maria Carolina of Austria (1740–1741)**

- [d5s0] Archduchess Maria Carolina of Austria (
- [d5s1] Maria Carolina Ernestina Antonia Johanna Josefa; 12 January 1740 – 25 January 1741), was the third child and daughter of Archduchess Maria Theresa of Austria, later Holy Roman Empress and Duke Francis of Lorraine.

**d6: Archduchess Marie Astrid of Austria**

- [d6s0] Archduchess Marie Astrid of Austria( née" Princess Marie Astrid of Luxembourg"; born 17 February 1954 at Castle Betzdorf) is the elder daughter and eldest child of Grand Duke Jean of Luxembourg and Joséphine- Charlotte of Belgium, and the wife of Archduke Carl Christian of Austria.

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

**d8: Archduke Otto of Austria (1865–1906)**

- [d8s0] Archduke Otto Franz Joseph Karl Ludwig Maria of Austria (21 April 1865 – 1 November 1906) was the second son of Archduke Karl Ludwig of Austria (younger brother of Emperor Franz Joseph I of Austria) and his second wife, Princess Maria Annunciata of Bourbon-Two Sicilies.
- [d8s1] He was the father of Charles I of Austria, the last Emperor of Austria.

**d9: Ogawa Mataji**

- [d9s0] Viscount was a general in the early Imperial Japanese Army.
- [d9s1] He was also the father- in- law of Field Marshal Gen Sugiyama.

**d10: Ludwig von Westphalen**

- [d10s0] Johann Ludwig von Westphalen( 11 July 1770 – 3 March 1842) was a liberal Prussian civil servant and the father- in- law of Karl Marx.

## 30. 2wikimultihopqa_8b1a578708a211ebbd7aac1f6bf848b6 【需改：生成拆解】

原位置：`train` 第 60 题 · 全局第 60 题 · `sample_id: 2wikimultihopqa_8b1a578708a211ebbd7aac1f6bf848b6`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_8b1a578708a211ebbd7aac1f6bf848b6"></a>

> **审阅结论：需改：生成拆解**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 问的是寿命长短，当前事实单元只取死亡日期；死亡更晚不等于活得更久。
>
> **处理建议：** u1/u2 改为各人的寿命或出生与死亡日期，结论比较寿命；复用旧 gold 的生卒日期证据，重新确认取值格式和派生标签。
>
> **证据定位：** d8s0, d4s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Who lived longer, Sergio Tofano or Diego Cisneros?

Note:

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | death date of Sergio Tofano | False | () |
| u2 | death date of Diego Cisneros | False | () |
| u3 | who lived longer | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | birth and death dates of Sergio Tofano | False | [] | 20 August 1886 – 28 October 1973 | [['d8s0']] |
| u2 | birth and death dates of Diego Cisneros | False | [] | September 27, 1911 – July 15, 1980 | [['d4s0']] |
| u3 | which of Sergio Tofano and Diego Cisneros lived longer | True | ['u1', 'u2'] | Sergio Tofano | [[]] |

### Source documents (reference only)

**d1: Diogo de Azambuja**

- [d1s0] Diogo de Azambuja or Diego de Azambuja( born Montemor- o- Velho, 1432; died 1518) was a Portuguese noble.

**d2: Giovanni Lopez de Andrade**

- [d2s0] Giovanni Lopez de Andrade, O.S.A. or Diego Lopez de Andrade( 1569 – 1628) was a Roman Catholic prelate who served as Archbishop of Otranto( 1623 – 1628).

**d3: Rosetta Tofano**

- [d3s0] Rosetta Tofano( 1902–1960) was an Italian costume designer and film star.
- [d3s1] She was a noted costumier for the stage and films.
- [d3s2] In 1923 she met and married Sergio Tofano.
- [d3s3] She made her film debut in the lead role in the 1932 film" Your Money or Your Life" and made several further appearances over the next decade.

**d4: Diego Cisneros**

- [d4s0] Diego Jesús Jiménez de Cisneros Bermúdez (September 27, 1911 – July 15, 1980) was a Cuban-Venezuelan businessman.
- [d4s1] He founded Grupo Cisneros.

**d5: Diego Maia**

- [d5s0] Diego Lopes da Silva Maia or Diego Maia( born 3 February 1990) is a Brazilian football defender.
- [d5s1] Diego Maia signed for Tupi Football Club in January 2014.

**d6: Diego Siloe**

- [d6s0] Diego Siloe( anglicized) or Diego de Siloé( c. 1495 – 1563) was a Spanish Renaissance architect and sculptor, progenitor of the Granadan school of sculpture.
- [d6s1] He developed the majority of his work in Andalusia.

**d7: Diego Silva Patriota**

- [d7s0] Diego Silva Patriota( born 22 August 1986), commonly known as Diego or Diego Patriota, is a Brazilian footballer who currently plays as a midfielder for Liga de Elite club Chao Pak Kei.

**d8: Sergio Tofano**

- [d8s0] Sergio Tòfano( 20 August 1886 – 28 October 1973) was an Italian actor, director, playwright, scene designer and illustrator.
- [d8s1] Tofano was born in Rome.
- [d8s2] In 1909, he made his first appearance on stage with Ermete Novelli, then joined Virgilio Talli's company( 1913 – 23).
- [d8s3] He soon specialized as a comic actor, giving his role a new elegance and complexity.
- [d8s4] He worked with other famous actors and directors: Dario Niccodemi( 1924 – 27); Luigi Almirante and Giuditta Rissone( 1927 – 30), Elsa Merlini, Vittorio De Sica, Evi Maltagliati, Gino Cervi etc.
- [d8s5] During those years, he made his famous performances as Doctor Knock in Jules Romains' play, and as Professor Toti in Luigi Pirandello's" Pensaci, Giacomino!".
- [d8s6] He also led important theatrical firms.
- [d8s7] After the Second World War, he worked with the most important directors, like Luchino Visconti and Giorgio Strehler.
- [d8s8] In 1917 Tofano invented, for a children's magazine," Il Corriere dei Piccoli", a famous character, Signor Bonaventura, whose adventures lasted for more than forty years.
- [d8s9] He used to sign as" Sto".

**d9: Maximus of Tyre**

- [d9s0] Maximus of Tyre( fl. late 2nd century AD), also known as Cassius Maximus Tyrius, was a Greek rhetorician and philosopher who lived in the time of the Antonines and Commodus, and who belongs to the trend of the Second Sophistic.
- [d9s1] His writings contain many allusions to the history of Greece, while there is little reference to Rome; hence it is inferred that he lived longer in Greece, perhaps as a professor at Athens.
- [d9s2] Although nominally a Platonist, he is really an Eclectic and one of the precursors of Neoplatonism.

**d10: Diego de Simancas**

- [d10s0] Diego de Simancas or Diego de Simancas Simancas( died 1583) was a Roman Catholic prelate who served as Bishop of Zamora( 1578 – 1583), Bishop of Badajoz( 1568 – 1578), and Bishop of Ciudad Rodrigo( 1564 – 1568).
