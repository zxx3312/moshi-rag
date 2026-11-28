# batch_03：人工审查（30 题）

全局题号 61–90；train 30 题 / dev 0 题。原训练/验证归属保持不变。

[返回分配索引](../README.md) · [完整对比报告](../../comparison_human.md)

**原则：新旧单元都合理时保留拆题器拆法，人工监督向新单元对齐。** 未标记的题目也需要核对答案和证据。现有标记是 AI 辅助审阅意见，不是人工验收结论。

审查人：________　完成日期：________

## 1. 2wikimultihopqa_8d777f1a095911ebbdaeac1f6bf848b6

原位置：`train` 第 61 题 · 全局第 61 题 · `sample_id: 2wikimultihopqa_8d777f1a095911ebbdaeac1f6bf848b6`

Question: Do the movies Melancholia (2008 Film) and Lost Battalion (1960 Film), originate from the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of origin of Melancholia (2008 Film) | False | () |
| u2 | country of origin of Lost Battalion (1960 Film) | False | () |
| u3 | whether Melancholia (2008 Film) and Lost Battalion (1960 Film) originate from the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country of origin of Melancholia (2008 film) | False | [] | Philippines | [['d4s0']] |
| u2 | country of origin of Lost Battalion (1960 film) | False | [] | Philippines | [['d5s0']] |
| u3 | whether Melancholia (2008 film) and Lost Battalion (1960 film) are from the same country | True | ['u1', 'u2'] | yes | [[]] |

### Source documents (reference only)

**d1: If You Only Knew (film)**

- [d1s0] If You Only Knew is a 2008 film.

**d2: Française (film)**

- [d2s0] Française is a 2008 film.

**d3: La Femme invisible**

- [d3s0] La Femme invisible is a 2008 film.

**d4: Melancholia (2008 film)**

- [d4s0] Melancholia is a 2008 Philippine film directed by Lav Diaz.
- [d4s1] It won the Horizons prize at the 65th Venice International Film Festival.

**d5: Lost Battalion (1960 film)**

- [d5s0] Lost Battalion( aka Escape to Paradise) is a 1960 black- and- white Filipino war film and love story produced and directed by Eddie Romero, and co-produced by Romero and Kane W. Lynn.
- [d5s1] Set during World War II, it stars Leopoldo Salcedo, Johnny Monteiro and Diane Jergens.
- [d5s2] It was later released in the US by American International Pictures as" Lost Batallion", on a double feature with" Guns of the Black Witch" in 1962.
- [d5s3] The film's ad line read" 200 Men and One Girl Trapped in a Ring of Steel!"

**d6: The Lost Battalion (1919 film)**

- [d6s0] The Lost Battalion is a 1919 American silent war film about units of the 77th Infantry Division( the" Lost Battalion") penetrating deep into the Argonne Forest of France during World War I.
- [d6s1] The film was directed by Burton L. King and features Major Charles W. Whittlesey and a number of actual soldiers from the 77th who portrayed themselves in the film.
- [d6s2] It was released July 2, 1919 in North America.
- [d6s3] The film was remade in 2001 by Russell Mulcahy.

**d7: Arugba**

- [d7s0] Arugba is a 2008 film.

**d8: Les Oreilles**

- [d8s0] Les Oreilles is a 2008 film.

**d9: C'est dimanche!**

- [d9s0] C'est dimanche!
- [d9s1] is a 2008 film.

**d10: Khamsa (film)**

- [d10s0] Khamsa is a 2008 film.

## 2. 2wikimultihopqa_8e43ba54087c11ebbd6aac1f6bf848b6 【保留新拆法｜重标人工标签】

原位置：`train` 第 62 题 · 全局第 62 题 · `sample_id: 2wikimultihopqa_8e43ba54087c11ebbd6aac1f6bf848b6`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_8e43ba54087c11ebbd6aac1f6bf848b6"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 两版事实含义一致，但两个被比较对象的 u1/u2 顺序交换；不属于拆题语义错误。
>
> **处理建议：** 保留新拆法，按对象交换旧 u1/u2 的答案、引用、特殊标记和快照标签；结论 u3 的证据引用也需随之核对。不要按编号直接拷贝。
>
> **证据定位：** d4s0, d10s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Which film was released more recently, Let's Be Famous or The Dilemma?

Note:

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | release year of Let's Be Famous | False | () |
| u2 | release year of The Dilemma | False | () |
| u3 | which film was released more recently | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | release year of The Dilemma | False | [] | 2011 | [['d4s0'], ['d4s6']] |
| u2 | release year of Let's Be Famous | False | [] | 1939 | [['d10s0']] |
| u3 | which of Let's Be Famous and The Dilemma was released more recently | True | ['u1', 'u2'] | The Dilemma | [[]] |

### Source documents (reference only)

**d1: Susuk (film)**

- [d1s0] Susuk is a 2008 Malaysian horror film which was released on 7 August 2008 in Malaysia.
- [d1s1] The film is directed by Amir Muhammad and Naeim Ghalili.
- [d1s2] The story concerns Soraya, who uses the forbidden practice of susuk to be famous.

**d2: The Dilemma (1914 film)**

- [d2s0] The Dilemma is a 1914 short written and directed by George Morgan and featuring William Russell.

**d3: Coney Island Baby (film)**

- [d3s0] Coney Island Baby is a 2003 comedy- drama in which film producer Amy Hobby made her directorial debut.
- [d3s1] Karl Geary wrote the film and Tanya Ryno was the film's producer.
- [d3s2] The music was composed by Ryan Shore.
- [d3s3] The film was shot in Sligo, Ireland, which is known locally as" Coney Island".
- [d3s4] The film was screened at the Newport International Film Festival.
- [d3s5] Hobby won the Jury Award for" Best First Time Director".
- [d3s6] The film made its premiere television broadcast on the Sundance Channel.

**d4: The Dilemma**

- [d4s0] The Dilemma is a 2011 American dark comedy film directed by Ron Howard, written by Allan Loeb and starring Vince Vaughn and Kevin James.
- [d4s1] The film follows savvy businessman Ronny( Vaughn) and genius engineer Nick( James) who are best friends and partners in an auto design firm.
- [d4s2] They are pursuing a project to make their firm famous.
- [d4s3] Ronny sees Nick's wife Geneva( Winona Ryder) kissing another man( Channing Tatum).
- [d4s4] Ronny seeks out answers and has to figure out how to tell Nick about what he saw while working with him to complete their critical presentation.
- [d4s5] It was filmed entirely in Chicago, Illinois.
- [d4s6] " The Dilemma" was released by Universal Pictures in the United States and Canada on January 14, 2011, to poor reviews and performed poorly at the box office, failing to recoup its$ 70 million production budget.

**d5: The Wonderful World of Captain Kuhio**

- [d5s0] The film was released in Japan on 10 October 2009.

**d6: Questa volta parliamo di uomini**

- [d6s0] Questa volta parliamo
- [d6s1] di uomini
- [d6s2] ( This Time Let's Talk about Men or Let's Talk About Men) is a 1965 Italian tragicomedy film directed by Lina Wertmüller and starring Nino Manfredi.
- [d6s3] The film was shot in black and white and in 35 mm and lasted 91 minutes.

**d7: Let**

- [d7s0] Let or LET may refer to:

**d8: It's Tough to Be Famous**

- [d8s0] It's Tough to Be Famous is a 1932 American pre-Code comedy film directed by Alfred E. Green and written by Robert Lord.
- [d8s1] The film stars Douglas Fairbanks, Jr., Mary Brian, Emma Dunn, Walter Catlett and David Landau.
- [d8s2] The film was released by Warner Bros. on April 2, 1932.

**d9: Let's Be Friends (film)**

- [d9s0] Let's Be Friends is a 2005 French film directed and written by Olivier Nakache& Éric Toledano.

**d10: Let's Be Famous**

- [d10s0] Let's Be Famous is a 1939 British comedy film directed by Walter Forde and starring Jimmy O' Dea, Betty Driver and Sonnie Hale.
- [d10s1] It was made by Associated Talking Pictures, with shooting beginning in November 1938.
- [d10s2] The film's art direction was by the Austrian Oscar Werndorff, in his final production.

## 3. 2wikimultihopqa_8f3c6e140baf11ebab90acde48001122

原位置：`train` 第 63 题 · 全局第 63 题 · `sample_id: 2wikimultihopqa_8f3c6e140baf11ebab90acde48001122`

Question: Who is the paternal grandfather of Edward Montagu, Viscount Hinchingbrooke?

Note:

Type: bridge · fallback: False · SFT snapshots: 7

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Edward Montagu, Viscount Hinchingbrooke | False | () |
| u2 | father of {u1}, Edward Montagu's paternal grandfather | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Edward Montagu, Viscount Hinchingbrooke | False | [] | Edward Montagu, 3rd Earl of Sandwich | [['d4s1'], ['d2s2', 'd2s3']] |
| u2 | father of {u1}, Edward Montagu, Viscount Hinchingbrooke's paternal grandfather | True | ['u1'] | Edward Montagu, 2nd Earl of Sandwich | [['d2s0']] |

### Source documents (reference only)

**d1: Alexander Popham (died 1705)**

- [d1s0] Alexander Popham( c. 1670 – 1705), of Littlecote House, Littlecote, Wiltshire, and St. James's Square, London, was an English politician.
- [d1s1] He was the only son of Sir Francis Popham of Littlecote Park.
- [d1s2] Popham was a Member( MP) of the Parliament of England for Chippenham in 1690 – 1698 and for Bath in the period 1698 – 16 June 1705.
- [d1s3] He married Anne Montagu, daughter of Ralph Montagu, 1st Duke of Montagu.
- [d1s4] Their daughter, Elizabeth( died 20 March 1761), married firstly Edward Montagu, Viscount Hinchingbrooke, and secondly Francis Seymour, of Sherborne, Dorset.

**d2: Edward Montagu, 3rd Earl of Sandwich**

- [d2s0] Edward Montagu, 3rd Earl of Sandwich (10 April 1670 – 20 October 1729) was born in Burlington House, London, England to Edward Montagu, 2nd Earl of Sandwich and Lady Ann Boyle.
- [d2s1] He was styled Viscount Hinchingbrooke from 1672 until his accession to the earldom in 1688.
- [d2s2] On 8 July 1689 he married Elizabeth Wilmot, daughter of John Wilmot, 2nd Earl of Rochester and Elizabeth Malet.
- [d2s3] They had two children, Elizabeth, who died as an infant, and Edward Richard Montagu, Viscount Hinchingbrooke (7 July 1692 – 3 October 1722), who predeceased his father.
- [d2s4] On the accession of Queen Anne, Sandwich was appointed Master of the Horse to her husband, Prince George of Denmark, despite strong objections from the royal favourite Sarah Churchill, who wanted the office for one of her own family.
- [d2s5] Sandwich was generally regarded by his contemporaries as insane:
- [d2s6] his wife so far as possible kept him "close confined" at Hinchingbrooke, and entrusted the management of the family estates to their son, as soon as he was old enough to take charge.
- [d2s7] From 1704 at the latest the Queen came under intense pressure to dismiss him; she followed her frequent policy of temporising, writing that she thought that "he was not as ill as he was said to be".
- [d2s8] In 1705 however Sandwich's mental illness became so obvious that he was obliged to resign his office, and lived for more than twenty years in retirement until his death in 1729.

**d3: Lyon Cohen**

- [d3s0] Lyon Cohen( 1868–1937) was a Polish- born Canadian businessman and a philanthropist.
- [d3s1] He was the grandfather of singer/ poet Leonard Cohen.

**d4: Edward Montagu, Viscount Hinchingbrooke**

- [d4s0] Edward Richard Montagu, Viscount Hinchingbrooke (7 July 1692 – 3 October 1722) was a British Army officer and politician who sat in the House of Commons from 1713 to 1722.
- [d4s1] Hinchingbrooke was the eldest son of Edward Montagu, 3rd Earl of Sandwich and his wife Elizabeth, daughter of the Earl of Rochester.
- [d4s2] His mother kept his father, who was generally believed to be insane, much confined, leaving Hinchingbrooke to carry out the public business of his family.
- [d4s3] On 12 April 1707, at the age of 14, Hinchingbrooke married Elizabeth Popham (died 20 March 1761), the daughter of Alexander Popham of Littlecote, Wiltshire (a grandson of Alexander Popham).
- [d4s4] After a tour of the continent in 1708, he was given command of a troop in Sir Richard Temple's Regiment of Horse for the 1709 campaign in Flanders.
- [d4s5] During this time, Hinchingbrooke was one of the infamous Mohocks, and was arrested for assaulting a watchman in 1712.
- [d4s6] In 1713, Hinchingbrooke was elected as Member of Parliament for Huntingdon, for which he served until 1722.
- [d4s7] Hinchingbrooke became colonel of the 37th Regiment of Foot in 1717.
- [d4s8] In March 1722, he was named Lord Lieutenant of Huntingdonshire and in April was returned as MP for Huntingdonshire.
- [d4s9] However, he died in October 1722, predeceasing his father.
- [d4s10] He left five children:
- [d4s11] His widow later married Francis Seymour.

**d5: Fred Le Deux**

- [d5s0] Frederick" Fred" Le Deux( born 4 December 1934) was an Australian rules footballer who played with Geelong in the Victorian Football League( VFL).
- [d5s1] He is the grandfather of Tom Hawkins.

**d6: Kaya Alp**

- [d6s0] Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

**d7: Henry Krause**

- [d7s0] Henry J." Red" Krause, Jr.( August 28, 1913 – February 20, 1987) was an American football offensive lineman in the National Football League for the Brooklyn Dodgers and the Washington Redskins.
- [d7s1] He played college football at St. Louis University.
- [d7s2] He is the grandfather of Jennifer Krause
- [d7s3] He is the great grandfather of Payton Hoeing

**d8: Abd al-Muttalib**

- [d8s0] Abd al- Muttalib Shaybah ibn Hashim( c. 497 – 578) was the grandfather of Islamic prophet Muhammad.

**d9: Edward Montagu Butler**

- [d9s0] Edward Montagu Butler( 3 December 1866 – 11 February 1948) was an English first- class cricketer and schoolmaster.

**d10: Edward Montagu (judge)**

- [d10s0] Sir Edward Montagu( c. 1485 – 10 February 1557) was an English lawyer and judge.

## 4. 2wikimultihopqa_8f49c34c089011ebbd72ac1f6bf848b6

原位置：`train` 第 64 题 · 全局第 64 题 · `sample_id: 2wikimultihopqa_8f49c34c089011ebbd72ac1f6bf848b6`

Question: Are The Patriots (Film) and Kungajakt both from the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of The Patriots (Film) | False | () |
| u2 | country of Kungajakt | False | () |
| u3 | whether The Patriots (Film) and Kungajakt are from the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country of origin of The Patriots (film) | False | [] | France | [['d7s0']] |
| u2 | country of origin of Kungajakt | False | [] | Sweden | [['d5s0']] |
| u3 | whether The Patriots (film) and Kungajakt are from the same country | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: 2003 New England Patriots season**

- [d1s0] The 2003 New England Patriots season was the franchise's 34th season in the National Football League, the 44th overall and the 4th under head coach Bill Belichick.
- [d1s1] They finished with a league- best 14 – 2 record before advancing to and winning Super Bowl XXXVIII.
- [d1s2] Two seasons after winning Super Bowl XXXVI, the Patriots went into 2003 after missing the playoffs in 2002.
- [d1s3] In a salary cap- related move, captain and Pro Bowl safety Lawyer Milloy was released five days before the start of the regular season, prompting second- guessing of head coach Bill Belichick among fans and a report by ESPN analyst Tom Jackson that Patriots players" hated their coach", an accusation later denied by players.
- [d1s4] Milloy signed with the Buffalo Bills, who defeated the Patriots, 31 – 0, in the season opener.
- [d1s5] The Patriots would rebound though, not losing another game after starting with a 2 – 2 record.
- [d1s6] Due to multiple injuries, the Patriots started 42 different players during the season, an NFL record for a division winner until the Patriots started 45 different players in 2005.
- [d1s7] Undefeated at home, nose tackle Ted Washington coined the phrase" Homeland Defense" for a Patriots' defense, boosted by the acquisitions of Washington and San Diego Chargers castoff safety Rodney Harrison in the offseason, that gave up a league- low 14.9 points per game en route to a 14 – 2 regular season record.
- [d1s8] The regular season was bookended with a 31 – 0 victory over the Bills at home in Week 17, a score reversed from the Patriots' shutout loss to the Bills in Week 1.
- [d1s9] The win gave the Patriots a perfect 8 – 0 record at home in the regular season and the 14 – 2 season was a club record and the first time the Patriots ever won more than 11 games in a season.
- [d1s10] After a first- round bye in the AFC playoffs, the Patriots faced the Tennessee Titans at home in one of the coldest games in NFL history and won, setting up an AFC Championship Game matchup with the Indianapolis Colts.
- [d1s11] The top- seeded Patriots intercepted Colts quarterback Peyton Manning, the league's co- MVP, four times, winning 24 – 14 and advancing to Super Bowl XXXVIII against the Carolina Panthers.
- [d1s12] With a tied game late in the fourth quarter, Adam Vinatieri kicked the game- winning field goal with seconds remaining, giving the Patriots their second Super Bowl victory in three seasons.

**d2: 2011 New England Patriots season**

- [d2s0] The 2011 New England Patriots season was the 42nd season for the team in the National Football League and 52nd season overall.
- [d2s1] The Patriots finished the regular season at 13 – 3, and represented the AFC in Super Bowl XLVI.
- [d2s2] It was the seventh Super Bowl trip in franchise history, and the fifth for head coach Bill Belichick and quarterback Tom Brady.
- [d2s3] The Patriots dedicated their 2011 season to the memory of Myra Kraft, the wife of owner Robert Kraft, who died on July 20, 2011 after a long fight against cancer.
- [d2s4] At both home and away games, the Patriots wore patches bearing Kraft's initials, MHK, on their uniforms.
- [d2s5] The Patriots elected to wear their Super Bowl patches on the right side of their uniforms, so that they could keep the MHK patch on the left as it had been all season.
- [d2s6] The Patriots were the only 2011 division winner that won their division the previous season.
- [d2s7] The Patriots lost in the Super Bowl to the New York Giants by a score of 21– 17.
- [d2s8] The Patriots, as was the case in their previous appearance against these same Giants in Super Bowl XLII, had a chance to join the San Francisco 49ers, the Dallas Cowboys, the Pittsburgh Steelers, and the Green Bay Packers as the only teams to win at least four Super Bowls( the Packers, who had entered the 2011 season as the defending champions, had not yet won a fourth Super Bowl when the Patriots had last appeared).
- [d2s9] Instead, the Patriots tied a then- NFL record for most losses in a Super Bowl that had been set by the Minnesota Vikings and tied by the Denver Broncos and Buffalo Bills, each of whom had lost four.
- [d2s10] With the loss, along with losses in 1985, 1996, and 2007, the Patriots tied with the Denver Broncos, Buffalo Bills and Minnesota Vikings for most Super Bowl losses at four( although the Broncos would lose their fifth against the Seattle Seahawks two years later, and the Patriots would lose their fifth six years later).

**d3: 2018 New England Patriots season**

- [d3s0] The 2018 New England Patriots season was the franchise's 49th season in the National Football League, the 59th overall, and the 19th under head coach Bill Belichick.
- [d3s1] The Patriots entered the season as two- time defending AFC champions.
- [d3s2] The Patriots' losses to the Jacksonville Jaguars and Detroit Lions in Week 2 and 3 marked the franchise's first back- to- back double- digit losses since 2002.
- [d3s3] After this slow start, the Patriots improved to 7–3 after Week 10.
- [d3s4] Following a notable Week 14 loss to the Miami Dolphins, the Patriots could not match their 13 – 3 record from 2017.
- [d3s5] A defeat to the Pittsburgh Steelers in Week 15 meant the Patriots had lost five games for the first time since 2009.
- [d3s6] After a win over the Buffalo Bills in Week 16, the Patriots clinched the AFC East for the tenth consecutive season, surpassing the Dallas Cowboys( 1975- 1983) and the Indianapolis Colts( 2002- 2010) for the most consecutive division titles.
- [d3s7] New England went undefeated at home with a Week 17 win over the New York Jets in which they clinched a first- round bye, and wrapped up the regular season with an 11 –5 record that gave them the AFC's 2nd seed in the postseason.
- [d3s8] Despite their five losses, the team achieved the rare distinction of going unbeaten against teams that qualified for the playoffs.
- [d3s9] The 2018 Patriots became the second team ever in the four major American sports leagues to win at least 10 straight division titles, joining Major League Baseball's Atlanta Braves( 1991 – 2005, excluding the strike- shortened 1994 season).
- [d3s10] The Patriots also secured their 16th- straight 10- win season, tying the San Francisco 49ers' league record streak, set from 1983 – 98.
- [d3s11] Notable records set during the season include QB Tom Brady achieving the record for most career passing touchdowns( including playoffs).
- [d3s12] In the playoffs, the Patriots defeated the Los Angeles Chargers in the Divisional round, 41 – 28, to advance to the AFC Championship game for a record eighth straight season.
- [d3s13] The Patriots defeated the Chiefs, 37–31 in overtime, to advance to the Super Bowl for a third straight year, becoming only the third team in NFL history to appear in three consecutive Super Bowls( joining the 1971 – 73 Miami Dolphins and 1990–93 Buffalo Bills).
- [d3s14] In Super Bowl LIII, they faced the Los Angeles Rams in a rematch of Super Bowl XXXVI, in which the Patriots defeated the then- St. Louis Rams 20 – 17.
- [d3s15] The Patriots won on this occasion by a score of 13– 3 to win their sixth Super Bowl, tying the Pittsburgh Steelers for most Super Bowl championships in NFL history.
- [d3s16] The victory also made them the first team since the 1972 Miami Dolphins to win the Super Bowl the season after losing the game.

**d4: 2004 New England Patriots season**

- [d4s0] The 2004 New England Patriots season was the franchise's 35th season in the National Football League, the 45th overall and the 5th under head coach Bill Belichick.
- [d4s1] They finished with their second straight 14 – 2 record before advancing to and winning Super Bowl XXXIX, their third Super Bowl victory in four years, and their last one until 2014, when they went through a whole decade of postseason disappointments.
- [d4s2] They are, as of the present, the last team to repeat as NFL Champions and only the second to win 3 Super Bowls in a 4- year span( the other being the Dallas Cowboys from the 1992 to 1995 seasons).
- [d4s3] Following a Super Bowl win in 2003, the Patriots looked to improve their running game in the offseason.
- [d4s4] Replacing Antowain Smith with longtime but disgruntled Cincinnati Bengals running back Corey Dillon, who was acquired in a trade days before the 2004 NFL Draft; Dillon would rush for a career- high 1,635 yards in 2004.
- [d4s5] Winning their first six games of the season, the Patriots set the NFL record for consecutive regular season victories( 18), which was later broken by the 2006–2008 Patriots( 21), and consecutive regular season and playoff victories( 21) before losing to the Pittsburgh Steelers on October 31.
- [d4s6] In that game, Pro Bowl cornerback Ty Law was lost for the season with a foot injury.
- [d4s7] Combined with the loss of other starting cornerback Tyrone Poole two weeks earlier, the Patriots were forced to complete the regular season and playoffs by using second- year cornerback Asante Samuel, undrafted free agent Randall Gay, and longtime Patriots wide receiver Troy Brown at cornerback, among others.
- [d4s8] With a 14 – 2 record and the second seed in the AFC playoffs, the Patriots defeated the Indianapolis Colts at home in the playoffs for the second- straight year, holding the Colts' top offense to three points.
- [d4s9] The Patriots then defeated the Pittsburgh Steelers on the road, 41 – 27, in the AFC Championship Game.
- [d4s10] Prior to the Patriots' matchup with the Philadelphia Eagles in Super Bowl XXXIX, Eagles wide receiver Freddie Mitchell said he did not know the names of the Patriots' defensive backs, which was taken as a sign of disrespect by the Patriots'" replacement" secondary.
- [d4s11] The Patriots would go on to defeat the Eagles 24–21 in their second straight Super Bowl victory and third championship in four seasons, leading to some labeling the Patriots of the era a sports dynasty.

**d5: Kungajakt**

- [d5s0] Kungajakt is a 1944 Swedish drama film directed by Alf Sjöberg.

**d6: List of New England Patriots starting quarterbacks**

- [d6s0] The New England Patriots are a professional American football team based in Foxborough, Massachusetts.
- [d6s1] They are a member of the East Division of the American Football Conference( AFC).
- [d6s2] The team began as the Boston Patriots in the American Football League, a league that merged with the National Football League before the start of the 1970 season.
- [d6s3] In 1971, the team relocated to Foxborough, where they then became the New England Patriots.
- [d6s4] Between 1971 and 2001, the Patriots played their home games at Foxboro Stadium.
- [d6s5] Since 2002, the Patriots have played their home games at Gillette Stadium( formerly CMGI Field), which was built adjacent to Foxboro Stadium( which was then demolished, and the site was turned into a parking lot for Gillette Stadium).
- [d6s6] There have been 28 starting quarterbacks in the history of the franchise.
- [d6s7] The most starting quarterbacks the Patriots have had in one season is five quarterbacks, in 1987.
- [d6s8] Past quarterbacks for the Patriots include Patriots Hall of Fame inductees Babe Parilli, Steve Grogan, and Drew Bledsoe.
- [d6s9] Butch Songin became the first starting quarterback for the Patriots in 1960, when the franchise was first established.
- [d6s10] He was replaced by Tom Greene for the final two games of the season.
- [d6s11] Hall of Famer Parilli was the next starting quarterback for the Patriots, from 1961 to 1967.
- [d6s12] As of the 2018 season, New England's starting quarterback is Tom Brady, whom the Patriots selected in the 6th round( 199th pick overall) of the 2000 NFL Draft.
- [d6s13] He is the only quarterback to have led the Patriots to a Super Bowl victory.

**d7: The Patriots (film)**

- [d7s0] The Patriots is a 1994 French film by director Éric Rochant which focuses on certain activities carried out by the Mossad, as well as describing some of their operational tactics.
- [d7s1] It is a fictionalized account of two separate missions undertaken by the Israeli secret services.
- [d7s2] The first part relates the acquisition of the plans of the nuclear power plant which was later bombed by the Israeli Air Force( the Osirak nuclear site in Iraq).
- [d7s3] The second part of the movie is an interpretation of the Jonathan Pollard spy scandal.
- [d7s4] The film was entered into the 1994 Cannes Film Festival.

**d8: Colts–Patriots rivalry**

- [d8s0] The Colts – Patriots rivalry is a National Football League( NFL) rivalry between the Indianapolis Colts and the New England Patriots.
- [d8s1] It is considered one of the most famous rivalries in the NFL.
- [d8s2] The two teams have combined for seven Super Bowl victories( six by the Patriots) and ten AFC Championships( eight by the Patriots) since 2001, while both are noted for their organizational excellence.
- [d8s3] The nature of this rivalry is somewhat ironic because while the Colts and Patriots were AFC East division rivals from 1970 – 2001( dating prior to the Colts' move from Baltimore to Indianapolis), their intensified enmity was not prevalent until Indianapolis was moved into the newly formed AFC South following the 2001 season as part of the NFL's realignment.
- [d8s4] Following New England's 43 – 22 win in the 2013 – 14 playoffs the Patriots lead the series with nine wins( three in the playoffs) versus five wins( one playoff) for the Colts, and the Patriots hold a lead in points scored, 411–351.
- [d8s5] The modern matchup spanning the period of 2001 – 2011 was usually headlined as a contest between quarterbacks Peyton Manning and Tom Brady, who together won six NFL MVP awards in eight years( 2003 – 10; four by Manning).
- [d8s6] In September 2001 Brady received his first start against the Colts after an injury to then- starter Drew Bledsoe, and proceeded to defeat the Colts in his first six games against them in the next years, including the 2003 AFC Championship Game and a 2004 AFC Divisional playoff game.
- [d8s7] The 2004 Divisional game was notable as the Patriots held a record breaking Colts offense to 3 points on snowy cold night in Foxborough.
- [d8s8] The Colts won the next three matches, notching two regular season victories and a win in the 2006 AFC Championship Game on the way to their win in Super Bowl XLI.
- [d8s9] Since then, the Patriots have won the six out of the next eight games from 2007 – 14.
- [d8s10] The quarterback angle of the rivalry changed in 2012 following Manning's release from the team, and with the surge to success of Colts rookie Andrew Luck.
- [d8s11] The rivalry gained momentum again in February 2018, when Patriots offensive coordinator Josh McDaniels, who had agreed to become the head coach of the Colts, went back on his word and decided to stay on as a coordinator in New England.
- [d8s12] The 1967 football season for both the NFL and the American Football League opened with the agreement for the pending merger of the two leagues already in place.
- [d8s13] On August 13, 1967 the Boston Patriots hosted the Baltimore Colts at Harvard Stadium.
- [d8s14] The Colts won 33- 3 as Tom Matte scored in the first quarter and the Colts got a safety when Jon Morris blew a snap and the ball flew out of the endzone.
- [d8s15] The Patriots and Colts met for the first time in NFL regular- season play at Harvard Stadium in week three of the 1970 season.
- [d8s16] The Colts jumped to a 7- 0 lead in the first quarter, but the Patriots closed to a 7- 6 fourth- quarter score on two Gino Cappelletti field goals.
- [d8s17] On following series, Johnny Unitas, who relieved starter Earl Morrall, finished off the Patriots with a 55- yard touchdown pass and a 14- 6 Colts win.
- [d8s18] Battling the Colts for the AFC East title, the Patriots traveled to Baltimore with a 6- 3 record( including a 27- 13 Colts victory in Foxborough in week one of the season).
- [d8s19] The Patriots picked off Bert Jones twice, leading to a 21- 14 win.
- [d8s20] The win accelerated a six- game winning streak for the Patriots and their first playoff berth since 1963.
- [d8s21] The Colts had been AFC East champs the previous three seasons, but were minus many of their best players due to trades and injuries, including Bert Jones and starting cornerbacks Nelson Munsey and Norm Thompson.
- [d8s22] They were 0- 2 and 18- point underdogs when they traveled to Foxboro to play the Patriots on" Monday Night Football".
- [d8s23] It was a sloppy game for three quarters, with New England leading 13- 7 heading into the final period.
- [d8s24] As it started raining hard, Baltimore came to life behind running back Joe Washington, making his first start with the team after an off- season trade from San Diego.
- [d8s25] First he threw a 54- yard touchdown pass on a halfback option to Roger Carr.
- [d8s26] Later he caught a 23- yard touchdown pass from Bill Troup.
- [d8s27] After Troup and Carr connected for a 67- yard score, the Colts led 27- 13 with eight minutes to play.
- [d8s28] The Patriots came back to score twice on runs by Steve Grogan and Sam Cunningham sandwiched around a successful onside kick to tie the game with 1:32 left.
- [d8s29] But Washington fielded the bouncing ensuing kickoff and darted 90 yards across the shimmering rain- soaked field for the touchdown to give Baltimore the stunning 34- 27 win, causing Howard Cosell to exclaim," What a football game this turned out to be!"
- [d8s30] The Patriots lost to the Baltimore Colts 12- 7 in Baltimore; it turned out to be the final meeting between the Patriots and the Baltimore Colts, as the team moved to Indianapolis for 1984.
- [d8s31] It was also New England's last game in Baltimore until the Baltimore Ravens debuted in 1996.
- [d8s32] In their first meeting at Indianapolis, the Patriots made their first trip to the Hoosier Dome and defeated the Colts 50- 17.
- [d8s33] The win was the second for new coach Raymond Berry, a former Colts receiver.
- [d8s34] The 4- 5 Colts hosted the 0-9 Patriots and the two teams lit up the Hoosier Dome scoreboard in an overtime thriller.
- [d8s35] The game lead tied or changed 10 times and the Patriots scored twice off Jeff George interceptions.
- [d8s36] Patriots kicker Charlie Baumann accounted for the Patriots' final nine points of a 37- 34 overtime triumph that came amid illness to coach Dick McPherson.
- [d8s37] Peyton Manning made his second career trip to Foxborough and led the Colts to a 28- 7 halftime lead.
- [d8s38] The Patriots, behind Drew Bledsoe, scored 17 unanswered points in the fourth off
- [d8s39] Colt turnovers and the game- winning Adam Vinatieri field goal came in the final thirty seconds.
- [d8s40] The Colts hosted the Patriots, holding a 10- 2 record to New England's 7- 5.
- [d8s41] The Colts earned a 20- 15 win despite 344 passing yards from Drew Bledsoe.
- [d8s42] It was the first for Manning over New England after three straight losses and the first win over the Patriots for the Manning family( Peyton's dad Archie was 0- 3 lifetime against the Patriots with the New Orleans Saints and Houston Oilers.)
- [d8s43] Week three of the 2001 season, Tom Brady made his first NFL start when the 2- 0 Colts came to Foxborough.
- [d8s44] The Colts were defeated 44- 13 as Peyton Manning threw three interceptions, two returned for touchdowns.
- [d8s45] On October 21, New England traveled to the RCA Dome and won 38- 17, where Patriot David Patten became the first player since Walter Payton in 1979 to score touchdowns three separate ways: throwing a 60- yard pass to Troy Brown, a 91- yard reception from Brady, and a rushing score.
- [d8s46] The first meeting since divisional realignment put the Colts into the now- second year AFC South, the two clubs sported 9- 2 records, the latest into a season two teams with such records had met.
- [d8s47] The Patriots erupted to a 31- 10 lead in the third quarter.
- [d8s48] Peyton Manning rallied the Colts back, throwing three touchdowns to tie the game, however the Patriots clawed back to a 38- 34 lead.
- [d8s49] The Colts drove to the Patriots' 2- yard line in the final minute, only to be stopped on four downs.
- [d8s50] Heading into the Monday Night fight between the Colts( 7- 0) and the two- time defending Super Bowl champion Patriots( 4- 3), QB Peyton Manning was winless against New England in Foxborough( 0- 7).
- [d8s51] The Colts beat the Patriots, 40- 21.
- [d8s52] In the game's closing minutes, veteran QB Doug Flutie replaced Brady, and Colts president Bill Polian was heard in the press box yelling" break his leg!"

**d9: Art Graham**

- [d9s0] Arthur William Graham III( born July 31, 1941) is a former American football player.
- [d9s1] He played professionally as a wide receiver in the American Football League( AFL) for six seasons with the Boston Patriots.
- [d9s2] He was named Patriots player of the year in 1963 after averaging 26.2 yards per catch and scoring five touchdowns.
- [d9s3] Drafted by both the Patriots and the Cleveland Browns, the Patriots offered him$ 10,000 to play for them.
- [d9s4] He played college football at Boston College.
- [d9s5] His father Art( Skinny) Graham II was an outfielder for 21 games for the Boston Red Sox during the 1934- 35 seasons.
- [d9s6] Art Graham III averaged 26.1 yards per reception during his rookie season with the Boston Patriots.
- [d9s7] Art had a career best 167 yards receiving in the Patriots thrilling 25- 24 last second victory over the Houston Oilers@ Fenway Park on 11-06 -64.
- [d9s8] He caught an 80- yard touchdowns pass from Babe Parilli in the Patriots 34- 17 win over the Houston Oilers on 11- 29- 64.
- [d9s9] Art made a game saving tackles on a long punt return by Hoot Gibson in the Patriots 17- 14 win over the Oakland Raiders on 09-13- 64.
- [d9s10] Art also made a game saving tackle on a long punt return by Lance Alworth in the Patriots 33- 28 win over the San Diego Chargers on 09-20- 64.
- [d9s11] Art held the Patriots Team Record for the most receptions in a game for 33 years.
- [d9s12] He had 11 receptions for 134 yards and 2 touchdowns in the Patriots 27- 27 tie with the Kansas City Chiefs on 11- 20- 66.
- [d9s13] He caught a 22- yard touchdown pass, even though he was only wearing one shoe, in the Patriots 20- 14 win over the Miami Dolphins on 11- 27- 66.
- [d9s14] ( It would take another 20 years before the Patriots would win another game played in Miami Florida) Graham is a member of the Patriots' All- 1960s( AFL) team.

**d10: 1976 New England Patriots season**

- [d10s0] The 1976 New England Patriots season was the franchise's 7th season in the National Football League and 17th overall.
- [d10s1] After a nine- year stretch in which they posted just one non-losing season amid eight losing years, the Patriots turned around their fortunes, going 11 – 3.
- [d10s2] It marked their first winning season as an NFL team( their last winning season came in 1966, when the team was still in the AFL).
- [d10s3] The team had gone just 3–11 the previous season, and was considered a" Cinderella team" in 1976.
- [d10s4] Coach Chuck Fairbanks was named NFL Coach of the Year, and cornerback Mike Haynes was named NFL Rookie of the Year.
- [d10s5] The 1976 Patriots rushed for a total of 2,957 yards( averaging five yards per carry) and scored 376 points, both second- best in the league.
- [d10s6] The 2,957 yards rushing were the fifth- highest total in NFL history at the time.
- [d10s7] The team's 5.0 yards per carry was the best in the NFL and remains higher than all Super Bowl champions except the 1973 Miami Dolphins whose own run game was 5.0 yards per carry.
- [d10s8] The Patriots also led the league in takeaways at 50; the Patriots finished third in the league in turnover differential at plus- 14.
- [d10s9] The Patriots made only their second playoff appearance in their history and first since 1963, but lost to the eventual Super Bowl champion Oakland Raiders in the first round of the playoffs.
- [d10s10] Earlier in the season, the Patriots handed the Raiders their only loss of the season with a final score of 48 – 17, but a controversial roughing the passer penalty on Ray Hamilton on a Raiders drive late in the playoff game dimmed the Patriots' hopes of defeating the Raiders again.
- [d10s11] Despite the playoff loss, the team has been considered one of the most talented in Patriots history; in 2004, Patriots head coach Bill Belichick, who was an assistant coach for the Detroit Lions in 1976, called this Patriots team" loaded", a" who's who team."
- [d10s12] The Patriots fell 30- 27 in a Monday Night preseason game; rookie cornerback Michael Haynes ran back a punt but began celebrating at the five- yard line and was hit and fumbled; Darryl Stingley grabbed the fumble and scored.
- [d10s13] Entering the season the Patriots had never scored on a punt return in any game.
- [d10s14] Four Steve Grogan interceptions and a fumble doomed the Patriots as the Colts ran roughshod at Schaefer Stadium 27 – 13, this despite the sacking of Colts quarterback Bert Jones for 40 yards and 179 rushing yards by the Patriots.
- [d10s15] The Pats rebounded with 278 rushing yards and four touchdowns( two rushing scores by Andy Johnson, a Grogan rushing score, and a four- yard toss to Russ Francis) in a 30 – 14 rout of Miami.
- [d10s16] Bob Griese had one touchdown throw and three interceptions.
- [d10s17] Forcing six Steeler fumbles in heavy rain, the Patriots wiped out a 20 – 9 third- quarter gap as Steve Grogan threw to Russ Francis and Darryl Stingley and ran in a touchdown for 21 second- half points.
- [d10s18] Don Calhoun's fumble in the final four minutes led to a Bradshaw touchdown, and after forcing another punt with 1:29 to go Bradshaw nearly fumbled away the ball but converted two first downs requiring 25 or more yards.
- [d10s19] With three seconds to go Roy Gerela missed a field goal and the Patriots had an upset 30 – 27 win.
- [d10s20] The Raiders suffered their only loss of the season in a 48 – 17 slaughter by the Patriots.
- [d10s21] Ken Stabler had a touchdown throw to Fred Biletnikoff but was sacked four times while Steve Grogan ran wild with three touchdown throws( to Darryl Stingley and Marlin Briscoe) and two rushing scores; Andy Johnson and Jess Phillips rushed in additional touchdowns.
- [d10s22] During the third quarter a Raiders touchdown was twice wiped out on penalties and the drive ended in a Stabler sack on third- and- 26.
- [d10s23] The Patriots never got on track as Grogan threw five picks and the Lions, led by running back Horace King and quarterback Greg Landry, stampeded the Patriots 30 – 10.
- [d10s24] One of the members of the Lions staff in this game was assistant special teams coach Bill Belichick, who introduced a two tight- end set on Detroit's offense that was rare for the NFL at the time.
- [d10s25] The Patriots despite ten penalties exploded to 330 rushing yards( 103 of them with a touchdown by Steve Grogan) as they annihilated the Jets 41- 7.
- [d10s26] Alex Karras( whose grandnephew would be drafted by the Patriots in 2016) was working the ABC Sports booth and read aloud Jets coach Lou Holtz's fight song for the team, a reworked version of the US Army's original march The Caissons Go Rolling Along.
- [d10s27] The Patriots posted their first win over the Bills since 1971 as the two teams combined for nine turnovers, 125 yards in penalties, and 586 yards of offense in the 26- 22 New England win.
- [d10s28] Sam Cunningham and OJ Simpson combined for 229 rushing yards.
- [d10s29] Despite 130 rushing yards from five Patriots backs New England fell at Miami 10- 3; all scoring took place in the second quarter as Jim Mandich accounted for the game's only touchdown.
- [d10s30] The Patriots were also penalized eleven times for 80 yards.
- [d10s31] Mike Haynes became the first Patriot to ever return a punt for a touchdown as he fielded a second- quarter punt at his 11 and stormed to the Buffalo endzone.
- [d10s32] The Patriots won 20–10 as Sam Cunningham rushed for 141 yards and a score while Joe Ferguson of the Bills threw four picks; the Bills also fumbled four times while the Patriots coughed up the ball fives times( three fumbles and two INTs).
- [d10s33] O. J. Simpson threw a punch at Mel Lunsford and both players were ejected after the ensuing fight.
- [d10s34] Battling for the division lead, the Colts and Patriots combined for 35 first- half points.
- [d10s35] In the first quarter Roger Carr caught a 22- yard pass from Bert Jones for the Colts while Al Chandler caught a two- yarder from Steve Grogan.
- [d10s36] Grogan ran in two second- quarter touchdowns and Don McCauley ran in a score for a 21–14 Patriots lead at the half.
- [d10s37] The two defenses then shut each other out, as Jones was picked off twice by Mike Haynes and sacked five times in total; Lydell Mitchell was limited to 52 rushing yards and the Patriots held on for the 21–14 win.
- [d10s38] The Jets hosted the Patriots at Shea Stadium and raced to a 10 – 0 lead in the first quarter behind a Pat Leahy field goal and a Greg Buttle fumble- return score, but the Patriots behind Steve Grogan throws to Andy Johnson and Darryl Stingley took a 14 – 10 lead entering the second quarter.
- [d10s39] From there the game collapsed for the 3 – 7 Jets as Joe Namath threw six interceptions; Mike Haynes grabbed three and Tim Fox had one, while Prentice McCray ran in two( totalling 118 yards) for touchdowns.
- [d10s40] With Sam Cunningham injured Don Calhoun became the workhorse back for New England, rushing for 109 yards.
- [d10s41] Namath was benched in the fourth quarter and Richard Todd took over; he threw a touchdown to Clark Gaines but was later picked off by Bob Howard.
- [d10s42] Grogan threw for just 83 yards and three scores as the Patriots routed the Jets 38 – 24.
- [d10s43] The Patriots amassed their highest rushing yardage of the year as Don Calhoun( 177 yards), Andy Johnson, and Ike Forte ground up 332 yards on the ground.
- [d10s44] Mike Haynes also returned a punt 62 yards for a touchdown as the Patriots sacked Denver's quarterbacks nine times, led 31–0 at the half, and cruised to a 38 – 14 final.
- [d10s45] With Archie Manning out for the year the Saints wound up using two quarterbacks( including ex-Bear Bobby Douglass) but managed only 236 total yards vs. 220 rushing yards from the Patriots led by Don Calhoun's 113 yards.
- [d10s46] In winning 27- 6 Steve Grogan completed only nine of 23 passes but two of them were touchdowns, one to Al Chandler, subbing for injured Russ Francis.
- [d10s47] The win was the 100th career victory in the franchise's history.
- [d10s48] Steve Grogan had his worst passing day of the season with just 40 yards in the air and a pick amid just four completions in 14 attempts.
- [d10s49] Six Patriots backs led by Andy Johnson rushed for 260 yards and three touchdowns while Sam Hunt picked off Steve Spurrier and ran back 68- yard touchdown.
- [d10s50] The game ended Tampa's winless first ever season.
- [d10s51] The 1976 AFC Divisional Playoffs.
- [d10s52] This would become the infamous" Ben Dreith Game" as officiating became a major controversy with numerous questionable penalties.
- [d10s53] Bill Lenkaitis had not been flagged for holding all season yet was flagged three times in this game.
- [d10s54] No penalty was called when George Atkinson of the Raiders hammered Russ Francis in the facemask and broke his nose; Steve Zabel popped Francis' nose back into place.
- [d10s55] There was also controversy over a Sam Cunningham run in the final five minutes of the fourth quarter where he went out of bounds; John Hannah claimed the sideline official moved the first down marker just before Cunningham went out of bounds, denying him a first down.
- [d10s56] On the play following this Cunningham run, on 3rd and 1 at the Raiders 28- yard line, Steve Grogan changed the snap count to draw the Raiders offsides, but the Raiders were barking out dummy snap counts themselves and Hannah, Leon Gray, and Pete Brock all jumped offsides(" I should have known better", Grogan said afterward).
- [d10s57] On the next play( 3rd and 6) Grogan threw to Russ Francis but Francis could not raise his arms because of holding by the Raiders Phil Villapiano, holding so blatant that according to Francis,"( he left) bruise marks on my arm ... when I saw Phil at the Pro Bowl that year, he came right out and told me he had done it."
- [d10s58] The Patriots missed the ensuing field goal attempt and the Raiders took possession.
- [d10s59] In the final minute of the fourth quarter Raymond Hamilton of the Patriots was flagged for roughing the passer against Ken Stabler of the Raiders on a 3rd- and- 18 play, even though replays showed no roughing; Dreith said the call was made because Hamilton had hit Stabler's helmet, but replays showed Stabler ducking away from Hamilton.
- [d10s60] Despite Patriot protests( Hamilton was flagged for unsportsmanlike conduct for his protests) the call stood.
- [d10s61] The Patriots stopped the Raiders on 3rd and 1 near the goal line but another personal foul penalty( this one on Prentice McCray) extended the Raiders drive, and on second and goal at the Patriot 1- yard line Stabler ran in the game- winning touchdown with ten seconds left in a 24 – 21 Raiders win.
- [d10s62] Patriot protests over Dreith's call were such that Dreith was not assigned to work any games involving the Patriots until 1987.

## 5. 2wikimultihopqa_9040c5ab097511ebbdb0ac1f6bf848b6 【需改：生成拆解】

原位置：`train` 第 65 题 · 全局第 65 题 · `sample_id: 2wikimultihopqa_9040c5ab097511ebbdb0ac1f6bf848b6`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_9040c5ab097511ebbdb0ac1f6bf848b6"></a>

> **审阅结论：需改：生成拆解**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 把完整地名“Bol, Mazandaran”中的行政区限定词当成另一个被比较对象，导致本应比较两个地点却生成三个事实单元。源文档标题与首句确认这是一个地点。
>
> **处理建议：** 将“Bol, Mazandaran”作为不可拆开的实体；恢复两个国家事实单元和一个必要比较结论，删除多余行政区单元并重建依赖。
>
> **证据定位：** d8s0, d1s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Are Bol, Mazandaran and Kozmodemyansk, Perm Krai located in the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of Bol | False | () |
| u2 | country of Mazandaran | False | () |
| u3 | country of Kozmodemyansk, Perm Krai | False | () |
| u4 | whether Bol, Mazandaran and Kozmodemyansk, Perm Krai are located in the same country | True | ('u1', 'u2', 'u3') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country of Bol, Mazandaran | False | [] | Iran | [['d8s0']] |
| u2 | country of Kozmodemyansk, Perm Krai | False | [] | Russia | [['d1s0']] |
| u3 | whether Bol, Mazandaran and Kozmodemyansk, Perm Krai are located in the same country | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Kozmodemyansk, Perm Krai**

- [d1s0] Kozmodemyansk is a rural locality( a selo) and the administrative center of Kozmodemyanskoye Rural Settlement, Karagaysky District, Perm Krai, Russia.
- [d1s1] The population was 602 as of 2010.
- [d1s2] There are 15 streets.

**d2: 2017 Perm Krai gubernatorial election**

- [d2s0] Gubernatorial Election in Perm Krai were held on 10 September 2017.

**d3: Habib Nafisi**

- [d3s0] Habib Nafisi is the founder of Tehran Polytechnic( Amirkabir University of Technology).
- [d3s1] He founded it in 1958 with five engineering departments.
- [d3s2] He also founded the University of Mazandaran and Iran University of Science and Technology.

**d4: Lake Chusovskoye**

- [d4s0] Chusovskoye is a lake in Perm Krai, Russia.
- [d4s1] Area is 19.1 km².
- [d4s2] Average depth is 1.5 – 2 m, maximal depth is 8 m.
- [d4s3] Is stretches from north to south for more than 15 km.
- [d4s4] It is largest lake in Perm Krai, located in the extreme north of Cherdynsky District, near the border with Komi Republic.
- [d4s5] There are Visherka River flows out of the lake and Beryozovka River, that flows into the lake in the north.

**d5: Borzinskiy district Museum**

- [d5s0] Municipal culture institution the Borzinskiy District Museum( Борзинскому краеведческому музею) is a historical museum in the town of Borzya in Zabaykalsky Krai.
- [d5s1] Located at the address: street Pushkin, 25.
- [d5s2] The museum opened on 2 December 1976.

**d6: Legislative Assembly of Perm Krai**

- [d6s0] The Legislative Assembly of Perm Krai is the supreme legislative power body of Perm Krai, a federal subject of Russia, which has existed since 2006.
- [d6s1] The Assembly is made up of sixty deputies who are directly elected by the population of Perm Krai for a five- year term.
- [d6s2] Voting is carried out using a mixed- member proportional representation system.

**d7: Afrasiyab dynasty**

- [d7s0] The Afrasiyab or Chalavi dynasty was a small Iranian Shia dynasty of Mazandaran and flourished in the late medieval, pre-Safavid period; it is also called the Kia dynasty.
- [d7s1] It was founded by Kiya Afrasiyab, who conquered the Bavand kingdom in 1349 and made himself king of the region.
- [d7s2] In 1504, Ismail I invaded Mazandaran and ended Afrasiyab rule of the region.

**d8: Bol, Mazandaran**

- [d8s0] Bol is a village in Sheykh Fazlolah- e Nuri Rural District, Baladeh District, Nur County, Mazandaran Province, Iran.
- [d8s1] At the 2006 census, its population was 48, in 17 families.

**d9: Arakhley**

- [d9s0] Arakhley is a rural locality( a" selo") in Chitinsky District of Zabaykalsky Krai, located on the southwest bank of Arakhley Lake, from Chita.
- [d9s1] Population: 306( 2002).
- [d9s2] There are many tourist bases nearby.
- [d9s3] A monument to the residents of Arakhley who died in Great Patriotic War is located in the village.

**d10: List of rural localities in Krasnodar Krai**

- [d10s0] This is a list of rural localities in Krasnodar Krai.
- [d10s1] Krasnodar Krai is a federal subject of Russia( a krai), located in the North Caucasus region in Southern Russia and administratively a part of the Southern Federal District.
- [d10s2] Its administrative center is the city of Krasnodar.
- [d10s3] The third most-populous federal subject, the krai had a population of 5,226,647 as of the 2010 Census.

## 6. 2wikimultihopqa_920f21380bda11eba7f7acde48001122

原位置：`train` 第 66 题 · 全局第 66 题 · `sample_id: 2wikimultihopqa_920f21380bda11eba7f7acde48001122`

Question: Who is the founder of the company that published The Friend (Lds Magazine)?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | company that published The Friend (Lds Magazine) | False | () |
| u2 | founder of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | publisher of The Friend (LDS magazine) | False | [] | The Church of Jesus Christ of Latter-day Saints | [['d1s0']] |
| u2 | founder of {u1} | True | ['u1'] | Joseph Smith | [['d10s4']] |

### Source documents (reference only)

**d1: The Friend (LDS magazine)**

- [d1s0] The Friend is the monthly English language children's magazine published by The Church of Jesus Christ of Latter-day Saints (LDS Church).
- [d1s1] It is aimed at those of Primary age,
- [d1s2] approximately ages 3 through 12.
- [d1s3] It includes messages from church leaders, stories, crafts, recipes, and artwork and poetry submitted by readers.
- [d1s4] "The Friend" is the successor to "The Children's Friend", the official magazine of the LDS Church for children between 1902 and 1970.
- [d1s5] "
- [d1s6] The Friend" has been published monthly since January 1971.
- [d1s7] The magazine contains no advertisements.
- [d1s8] Material from "The Friend" is translated into over 50 languages and published in various language editions of the "Liahona", the church's official international magazine.

**d2: The Friend (Quaker magazine)**

- [d2s0] The Friend is a weekly Quaker magazine published in London, UK.
- [d2s1] It is the only Quaker weekly in the world, and has been published continuously since 1843.
- [d2s2] It began as a monthly and in January 1892 became a weekly.
- [d2s3] It is one of the oldest continuously published publications in the world still in operation.
- [d2s4] Others( e.g." Punch") which began publication before" The Friend" have had lengthy interruptions in publication and/ or have closed down.

**d3: The Friend of China**

- [d3s0] The Friend of China, officially" The Friend of China and Hongkong Gazette" from 1842 to 1859, was an influential English- language newspaper in early British Hong Kong and among European residents of the Qing Empire.
- [d3s1] Its first issue was published, as" The Friend of China", on 17 March 1842.
- [d3s2] Upon the appearance of its second issue, 24 March 1842, the paper was amalgamated with the colonial government gazette, the" Hong Kong Gazette".
- [d3s3] In 1845 the paper lost its government connection but retained the title of the" Gazette".
- [d3s4] From this point the" Friend of China" adopted a generally antagonistic stance towards the colonial government, and spoke for the interests of the local European merchant community.
- [d3s5] A mainland edition of the paper, the" Overland Friend of China", was published separately for a time.
- [d3s6] The" Friend of China" s final owner and editor, William Tarrant, purchased the paper in 1850 and, after taking part in numerous political controversies, was imprisoned for libel in 1859.
- [d3s7] The" Friend of China" ceased publication, before resuming briefly at Canton following Tarrant's release in 1860 until 1861, and then at Shanghai from 1863 to 1869.
- [d3s8] Tarrant sold the paper in 1869, and the" Friend of China" folded permanently shortly thereafter.

**d4: Web enhancement**

- [d4s0] A web enhancement is a bonus expansion to a role- playing game product, that can be read and/ or downloaded from the website of the company that published the role- playing product it is associated with.

**d5: Cyrus Massoumi**

- [d5s0] Cyrus Massoumi is the founder of the investment fund humbition.
- [d5s1] He is also the founder of Zocdoc and was the company CEO for eight years.

**d6: Vennen**

- [d6s0] Vennen(" The Friend") was a Danish magazine for gay men published from 1949 to 1974.

**d7: Chappell & Co.**

- [d7s0] Chappell& Co. was an English company that published music and manufactured pianos.

**d8: Pink Pages**

- [d8s0] Pink Pages was an Indian LGBT magazine that published online and print issues from 2009 to 2017.

**d9: Pariah Press**

- [d9s0] Pariah Press was the company, funded by Mike Nystul, that published the first commercial edition of The Whispering Vault role- playing game.

**d10: The Church of Jesus Christ of Latter-day Saints**

- [d10s0] The Church of Jesus Christ of Latter-day Saints, often informally known as the LDS Church or Mormon Church, is a nontrinitarian, Christian restorationist church that considers itself to be the restoration of the original church founded by Jesus Christ.
- [d10s1] The church is headquartered in Salt Lake City, Utah, in the United States, and has established congregations and built temples worldwide.
- [d10s2] According to the church, it has over 16 million members and 65,000 full-time volunteer missionaries.
- [d10s3] In 2012, the National Council of Churches ranked the church as the fourth-largest Christian denomination in the United States, with over 6.5 million members there as of January 2018.
- [d10s4] It is the largest denomination in the Latter Day Saint movement founded by Joseph Smith during the early 19th century period of religious revival known as the Second Great Awakening.
- [d10s5] Adherents, often referred to as "Latter-day Saints" or, less formally, "Mormons", view faith in Jesus Christ and his atonement as fundamental principles of their religion.
- [d10s6] Church theology includes the Christian doctrine of salvation only through Jesus Christ, though LDS doctrines regarding the nature of God and the potential of mankind differ significantly from mainstream Christianity.
- [d10s7] The church has an open canon which includes four scriptural texts: the Bible (both Old and New Testaments), the Book of Mormon, the Doctrine and Covenants, and the Pearl of Great Price.
- [d10s8] Other than the Bible, the majority of the LDS canon constitutes revelation received by Joseph Smith and recorded by his scribes which includes commentary and exegesis about the Bible, texts described as lost parts of the Bible, and other works believed to be written by ancient prophets.
- [d10s9] Because of some of the doctrinal differences, Catholic, Orthodox, and several Protestant churches consider the church to be distinct and separate from mainstream Christianity.
- [d10s10] Under the doctrine of continuing revelation, Latter-day Saints believe that the church president is a modern-day "prophet, seer, and revelator" and that Jesus Christ, under the direction of God the Father, leads the church by revealing his will to its president.
- [d10s11] Individual members of the church believe that they can also receive personal revelation from God in conducting their lives.
- [d10s12] The president heads a hierarchical structure with various levels reaching down to local congregations.
- [d10s13] Bishops, drawn from the laity, lead local congregations.
- [d10s14] Male members, beginning in January of the year they reach age 12, may be ordained to the priesthood, provided they are living the standards of the church.
- [d10s15] Women are not ordained to the priesthood but do occupy leadership roles in some church organizations.
- [d10s16] Both men and women may serve as missionaries and the church maintains a large missionary program that proselytizes and conducts humanitarian services worldwide.
- [d10s17] Faithful members adhere to church laws of sexual purity, health, fasting, and Sabbath observance, and contribute ten percent of their income to the church in tithing.
- [d10s18] The church also teaches about sacred ordinances through which adherents make covenants with God, including baptism, confirmation, the sacrament (holy communion), priesthood ordination, endowment, and celestial marriage (marriage blessings which extend beyond mortality)—all of which are of great significance to church members.

## 7. 2wikimultihopqa_94e510f308c411ebbd8eac1f6bf848b6

原位置：`train` 第 67 题 · 全局第 67 题 · `sample_id: 2wikimultihopqa_94e510f308c411ebbd8eac1f6bf848b6`

Question: Which film was released more recently, Trafic or The River'S End (Film)?

Note:

Type: comparison · fallback: False · SFT snapshots: 7

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | release year of Trafic | False | () |
| u2 | release year of The River'S End (Film) | False | () |
| u3 | which film was released more recently | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | release year of Trafic | False | [] | 1971 | [['d3s0']] |
| u2 | release year of The River's End (film) | False | [] | 1920 | [['d6s0']] |
| u3 | which film was released more recently, Trafic or The River's End | True | ['u1', 'u2'] | Trafic | [[]] |

### Source documents (reference only)

**d1: River's End (1940 film)**

- [d1s0] River's End is a 1940 American western film directed by Ray Enright and starring Dennis Morgan, Elizabeth Inglis and George Tobias.
- [d1s1] It is an adaptation of the 1919 novel" The River's End" by James Oliver Curwood which had previously been made into 1920 and 1930 films.
- [d1s2] It is also known by the alternative title of Double Identity.
- [d1s3] The film is a Northern in which a Royal Canadian Mounted Police officer tracks an escaped convict, only to subsequently try to clear his name.
- [d1s4] The film's sets were designed by the art director Esdras Hartley.

**d2: London Unplugged**

- [d2s0] London Unplugged is a 2018 British drama anthology film which premiered at the East End Film Festival.
- [d2s1] The film consists of several segments directed by numerous directors and stars Juliet Stevenson, Poppy Miller, Imogen Stubbs, Ivanno Jeremiah, Ricky Nixon and Bruce Payne.

**d3: Trafic**

- [d3s0] Trafic(" Traffic") is a 1971 Italian- French comedy film directed by Jacques Tati." Trafic" was the last film to feature Tati's famous character of Monsieur Hulot, and followed the vein of earlier Tati films that lampooned modern society.
- [d3s1] Tati's use of the word" trafic" instead of the usual French word for car traffic(" la circulation") may derive from a desire to use the same franglais he used when he called his previous film" Play Time", and the primary meaning of" trafic" is" exchange of goods", rather than" traffic" per se.
- [d3s2] The word" Trafic" was subsequently used for a light utility vehicle model manufactured by Renault starting in 1981.

**d4: River's End (1930 film)**

- [d4s0] River's End is a 1930 American Pre-Code drama film directed by Michael Curtiz and starring Charles Bickford and Evalyn Knapp.
- [d4s1] Bickford plays two roles, a Royal Canadian Mounted Police( RCMP) sergeant and the man he is after.
- [d4s2] The film is the second of three adaptations of the bestselling novel" The River's End" by James Oliver Curwood, the others being released in 1920 and 1940.

**d5: Coney Island Baby (film)**

- [d5s0] Coney Island Baby is a 2003 comedy- drama in which film producer Amy Hobby made her directorial debut.
- [d5s1] Karl Geary wrote the film and Tanya Ryno was the film's producer.
- [d5s2] The music was composed by Ryan Shore.
- [d5s3] The film was shot in Sligo, Ireland, which is known locally as" Coney Island".
- [d5s4] The film was screened at the Newport International Film Festival.
- [d5s5] Hobby won the Jury Award for" Best First Time Director".
- [d5s6] The film made its premiere television broadcast on the Sundance Channel.

**d6: The River's End (film)**

- [d6s0] The River's End is a 1920 American silent western film directed by Victor Heerman and Marshall Neilan and starring Lewis Stone, Marjorie Daw, and Jane Novak.
- [d6s1] It is an adaptation of the 1919 novel of the same name by James Oliver Curwood.
- [d6s2] The film's sets were designed by the art director Ben Carré.

**d7: The Darkest Universe**

- [d7s0] The Darkest Universe is the second film from BAFTA- nominated directors Will Sharpe and Tom Kingsley.
- [d7s1] The film premiered at the London Comedy( LOCO) film festival in April 2016 and subsequently screened at the East End Film Festival.
- [d7s2] The film was written by Tiani Ghosh and Will Sharpe and was shot over a three- year period from 2013 to 2015.
- [d7s3] It is set on the canals of London and tells the story of the disappearance of a young couple on a narrow boat.

**d8: The Wonderful World of Captain Kuhio**

- [d8s0] The film was released in Japan on 10 October 2009.

**d9: Suspension of Disbelief (film)**

- [d9s0] Suspension of Disbelief is a 2012 English thriller film directed, edited, co-produced by Mike Figgis and starring Sebastian Koch, Lotte Verbeek, Emilia Fox, Rebecca Night, Eoin Macken, Lachlan Nieboer, Frances de la Tour, Julian Sands and Kenneth Cranham.
- [d9s1] It was premiered at the 7th Rome Film Festival in November 2012.
- [d9s2] It played in the 12th East End Film Festival on 6 July 2013 and in Rio de Janeiro International Film Festival on 26 September 2013.
- [d9s3] The film was released in the UK on 19 July 2013.

**d10: River's End (2005 film)**

- [d10s0] River's End is a 2005 American Western- drama film directed by William Katt and starring Barry Corbin, Sam Huntington, Caroline Goodall, William Katt, Charles Durning, Clint Howard, and Jackson Rathbone.

## 8. 2wikimultihopqa_97cea0b00baf11ebab90acde48001122

原位置：`train` 第 68 题 · 全局第 68 题 · `sample_id: 2wikimultihopqa_97cea0b00baf11ebab90acde48001122`

Question: Who is Ramesses-Meryamun-Nebweben's paternal grandfather?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Ramesses-Meryamun-Nebweben | False | () |
| u2 | father of {u1}, Ramesses-Meryamun-Nebweben's paternal grandfather | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Ramesses-Meryamun-Nebweben | False | [] | Ramesses II | [['d8s0']] |
| u2 | father of {u1}, Ramesses-Meryamun-Nebweben's paternal grandfather | True | ['u1'] | Seti I | [['d10s8']] |

### Source documents (reference only)

**d1: Lyon Cohen**

- [d1s0] Lyon Cohen( 1868–1937) was a Polish- born Canadian businessman and a philanthropist.
- [d1s1] He was the grandfather of singer/ poet Leonard Cohen.

**d2: Minmose (High Priest)**

- [d2s0] Minmose was the High Priest of Anhur during the reign of Ramesses II

**d3: Kaya Alp**

- [d3s0] Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

**d4: Prithvipati Shah**

- [d4s0] Prithvipati Shah( ?–1716) was the king of the Gorkha Kingdom in the Indian subcontinent, present- day Nepal.
- [d4s1] He was the grandfather of Nara Bhupal Shah.

**d5: John Westley**

- [d5s0] Rev. John Westley( 1636 – 78) was an English nonconformist minister.
- [d5s1] He was the grandfather of John Wesley( founder of Methodism).

**d6: Tyti**

- [d6s0] Tyti was an ancient Egyptian queen of the 20th dynasty.
- [d6s1] A wife and sister of Ramesses III and possibly the mother of Ramesses IV.

**d7: Montuherkhopshef (son of Ramesses III)**

- [d7s0] Montuherkhopshef or Montuhirkhopshef was a Prince of the 20th Dynasty of Egypt and one of the sons of Ramesses III and Iset Ta-Hemdjert.
- [d7s1] He was thus a brother of Ramesses IV, Ramesses VI, Ramesses VIII and an uncle of Ramesses V and Ramesses VII.
- [d7s2] He was the "First Charioteer of His Majesty", and married the lady Takhat who bears the prominent title of "King's Mother.
- [d7s3] " This development supports the hypothesis that they are most probably the parents of king Ramesses IX since no other Ramesside king had a mother by this name, also, Ramesses IX had a son named Montuherkhepeshef.
- [d7s4] Montuherkhepeshef is shown in the procession of princes in the Medinet Habu temple of Ramesses III.
- [d7s5] He is likely to be identical with the Prince Montuherkhepeshef buried in the tomb KV13 in the Valley of the Kings
Since Montuherkhopshef never became Pharaoh unlike his brothers and nephews, his date of death can be placed prior to Year 22 of Ramesses III (1164 BC) since his brother Ramesses IV is known to have been designated as Egypt's crown prince in this year.

**d8: Ramesses-Meryamun-Nebweben**

- [d8s0] Ramesses-Meryamun-Nebweben was an Ancient Egyptian prince, a son of Pharaoh Ramesses II.
- [d8s1] Since he is not shown or mentioned anywhere among the children of Ramesses, he is likely to have been one of the youngest of Ramesses' sons.
- [d8s2] He is known to us only from the inscriptions of his coffins.
- [d8s3] The identity of his mother is unknown.
- [d8s4] He spent his life in the Mer-wer harem, and was buried nearby after his death in his 30s.
- [d8s5] His body was found, and it is apparent that he had a deformed spine and was hunchbacked.
- [d8s6] It is likely that because of his deformity it was difficult to find an adequate coffin for him.
- [d8s7] He was buried in an unused outer coffin of his great-grandfather, which Ramesses I had had made when he was still a vizier.
- [d8s8] Although the inner coffin was also altered for Ramesses-Meryamun-Nebweben's burial, and the inscriptions were changed to his name instead of that of his great-grandfather, only the outer coffin was used, and the inner one was found by archeologists in a pit in Medinet Habu.
- [d8s9] Unlike several of his brothers, whose name also includes the name "Ramesses," in his name "Ramesses Meryamun" was enclosed in a cartouche, making it explicit that it is not used in its literal meaning ("Born of Rê, Beloved of Amun") but refers to the pharaoh.
- [d8s10] "Nebweben" means "lord of sunshine", the meaning of the prince's name is thus "Pharaoh Ramesses is the Lord of Sunshine".
- [d8s11] Such names, glorifying the pharaoh, are often found as names taken by high officials, but are relatively rare as given names within the royal family during the New Kingdom.

**d9: Abd al-Muttalib**

- [d9s0] Abd al- Muttalib Shaybah ibn Hashim( c. 497 – 578) was the grandfather of Islamic prophet Muhammad.

**d10: Ramesses II**

- [d10s0] Ramesses II (variously also spelt Rameses or Ramses ("Ra is the one who bore him" >); – July or August 1213; reigned 1279–1213 BC), also known as Ramesses the Great, was the third pharaoh of the Nineteenth Dynasty of Egypt.
- [d10s1] He is often regarded as the greatest, most celebrated, and most powerful pharaoh of the New Kingdom.
- [d10s2] His successors and later Egyptians called him the "Great Ancestor".
- [d10s3] He is known as Ozymandias in Greek sources ("Osymandýas"), from the first part of Ramesses' regnal name, , "The Maat of Ra is powerful, Chosen of Ra".
- [d10s4] Ramesses II led several military expeditions into the Levant, reasserting Egyptian control over Canaan.
- [d10s5] He also led expeditions to the south, into Nubia, commemorated in inscriptions at Beit el-Wali and Gerf Hussein.
- [d10s6] The early part of his reign was focused on building cities, temples, and monuments.
- [d10s7] He established the city of Pi-Ramesses in the Nile Delta as his new capital and used it as the main base for his campaigns in Syria.
- [d10s8] At fourteen, he was appointed prince regent by his father, Seti I.
- [d10s9] He is believed to have taken the throne in his late teens and is known to have ruled Egypt from 1279 to 1213 BC.
- [d10s10] Manetho attributes Ramesses II a reign of 66 years and 2 months; most Egyptologists today believe he assumed the throne on May 31, 1279 BC, based on his known accession date of III Season of the Harvest, day 27.
- [d10s11] Estimates of his age at death vary; 90 or 91 is considered most likely.
- [d10s12] Ramesses II celebrated an unprecedented thirteen or fourteen Sed festivals (the first held after 30 years of a pharaoh's reign, and then, every three years) during his reign—more than any other pharaoh.
- [d10s13] On his death, he was buried in a tomb in the Valley of the Kings; his body was later moved to a royal cache where it was discovered in 1881, and is now on display in the Egyptian Museum.

## 9. 2wikimultihopqa_9be7c0dc088f11ebbd72ac1f6bf848b6

原位置：`train` 第 69 题 · 全局第 69 题 · `sample_id: 2wikimultihopqa_9be7c0dc088f11ebbd72ac1f6bf848b6`

Question: Which film has the director who is older, They Came Back or Captain Scarlett?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of They Came Back | False | () |
| u2 | birth date of {u1} | False | ('u1',) |
| u3 | director of Captain Scarlett | False | () |
| u4 | birth date of {u3} | False | ('u3',) |
| u5 | which film's director is older | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film They Came Back | False | [] | Robin Campillo | [['d5s0']] |
| u2 | date of birth of {u1} | False | ['u1'] | 16 August 1962 | [['d6s0']] |
| u3 | director of film Captain Scarlett | False | [] | Thomas Carr | [['d2s0']] |
| u4 | date of birth of {u3} | False | ['u3'] | July 4, 1907 | [['d10s0']] |
| u5 | which of the two films has the older director | True | ['u2', 'u4'] | Captain Scarlett | [[]] |

### Source documents (reference only)

**d1: Dan Milne**

- [d1s0] Dan Milne is a British actor/ director who is possibly best known for his role in" EastEnders".

**d2: Captain Scarlett**

- [d2s0] Captain Scarlett is a 1953 American Technicolor Adventure film directed by Thomas Carr, that was shot in Mexico.
- [d2s1] The film is set in France following the fall of Napoleon, stars Richard Greene in the title role as a Robin Hood- type avenger and the Brazilian actress Leonora Amar in her final screen role.

**d3: Ben Palmer**

- [d3s0] Ben Palmer is a British film and television director who is known for being the director of" Bo' Selecta" and" The Inbetweeners".

**d4: Logan Sandler**

- [d4s0] Logan Sandler is an American writer and director who is best known for his first feature film" Live Cargo".

**d5: They Came Back**

- [d5s0] They Came Back, known in the UK as The Returned, is a 2004 French horror drama film directed by Robin Campillo in his directorial debut.
- [d5s1] The film was screened at the Hamburg Fantasy Filmfest in Germany, the Venice Film Festival in Italy, and the Toronto International Film Festival in Canada.
- [d5s2] Unlike the typical zombie film, in which the physically deformed undead compulsively feed on or otherwise harm the human population, the physically normal undead in" They Came Back" seek only to reintegrate themselves into the everyday life of the small French town where they formerly lived, or so it seems.

**d6: Robin Campillo**

- [d6s0] Robin Campillo (born 16 August 1962) is a Moroccan-born French screenwriter, editor and film director.
- [d6s1] He is known for his work on films such as "The Class" (2008), "Heading South" (2005), the French zombie film "They Came Back" (2004), "Eastern Boys" (2013), and "Time Out" (2001), the latter of which was placed at ninety-nine on Slant Magazine's best films of the 2000s, number nine of "The Guardian's" Best Films of the noughties, and number eleven at "The A.V. Club's" top fifty films of the 2000s.
- [d6s2] In 2017, he released "120 BPM (Beats per Minute)" which received mass acclaim and went on to garner many awards, including the Grand Prix and 2017
César Award for Best Film.

**d7: Charles Calvert (director)**

- [d7s0] Charles Calvert was a British, silent- era film director.
- [d7s1] He was sometimes credited as C.C. Calvert or Captain Charles Calvert.
- [d7s2] Calvert had a reputation as a journeyman director who produced old- fashioned films.

**d8: Scotty Fox**

- [d8s0] Scott Fox is a pornographic film director who is a member of the AVN Hall of Fame.

**d9: Elliot Silverstein**

- [d9s0] Elliot Silverstein( born August 3, 1927, in Boston, Massachusetts) is an American director, who is best known for being the director of the movie" Cat Ballou"( 1965).

**d10: Thomas Carr (director)**

- [d10s0] Thomas Carr( July 4, 1907 – April 23, 1997) was an American actor and film director of Hollywood movies and television programs.
- [d10s1] Often billed as" Tommy Carr", he later adopted his more formal" Thomas Carr" birth name as his billing name.

## 10. 2wikimultihopqa_9d785ec3097d11ebbdb0ac1f6bf848b6

原位置：`train` 第 70 题 · 全局第 70 题 · `sample_id: 2wikimultihopqa_9d785ec3097d11ebbdb0ac1f6bf848b6`

Question: Are both Tavakkolabad, Bam and Bardshelandan located in the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of Tavakkolabad, Bam | False | () |
| u2 | country of Bardshelandan | False | () |
| u3 | whether Tavakkolabad, Bam and Bardshelandan are located in the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country of Tavakkolabad, Bam | False | [] | Iran | [['d3s0']] |
| u2 | country of Bardshelandan | False | [] | Iran | [['d10s0']] |
| u3 | whether Tavakkolabad, Bam and Bardshelandan are located in the same country | True | ['u1', 'u2'] | yes | [[]] |

### Source documents (reference only)

**d1: Neyab, North Khorasan**

- [d1s0] Neyab( also Romanized as Neyāb) is a village in Safiabad Rural District, Bam and Safiabad District, Esfarayen County, North Khorasan Province, Iran.
- [d1s1] At the 2006 census, its population was 121, in 24 families.

**d2: Zali, North Khorasan**

- [d2s0] Zali( also Romanized as Zālī) is a village in Bam Rural District, Bam and Safiabad District, Esfarayen County, North Khorasan Province, Iran.
- [d2s1] At the 2006 census, its population was 81, in 18 families.

**d3: Tavakkolabad, Bam**

- [d3s0] Tavakkolabad( also Romanized as Tavakkolābād) is a village in Howmeh Rural District, in the Central District of Bam County, Kerman Province, Iran.
- [d3s1] At the 2006 census, its population was 50, in 18 families.

**d4: Fathabad, North Khorasan**

- [d4s0] Fathabad( also Romanized as Fatḩābād) is a village in Bam Rural District, Bam and Safiabad District, Esfarayen County, North Khorasan Province, Iran.
- [d4s1] At the 2006 census, its population was 237, in 63 families.

**d5: Dastjerd, North Khorasan**

- [d5s0] Dastjerd is a village in Bam Rural District, Bam and Safiabad District, Esfarayen County, North Khorasan Province, Iran.
- [d5s1] At the 2006 census, its population was 569, in 162 families.

**d6: Zanaft**

- [d6s0] Zanaft is a village in Safiabad Rural District, Bam and Safiabad District, Esfarayen County, North Khorasan Province, Iran.
- [d6s1] At the 2006 census, its population was 507, in 118 families.

**d7: Jahan, Iran**

- [d7s0] Jahan( also Romanized as Jahān) is a village in Bam Rural District, Bam and Safiabad District, Esfarayen County, North Khorasan Province, Iran.
- [d7s1] At the 2006 census, its population was 915, in 218 families.

**d8: Maqsudabad, North Khorasan**

- [d8s0] Maqsudabad( also Romanized as Maqşūdābād) is a village in Safiabad Rural District, Bam and Safiabad District, Esfarayen County, North Khorasan Province, Iran.
- [d8s1] At the 2006 census, its population was 416, in 105 families.

**d9: Mohammadabad, Esfarayen**

- [d9s0] Mohammadabad( also Romanized as Moḩammadābād) is a village in Safiabad Rural District, Bam and Safiabad District, Esfarayen County, North Khorasan Province, Iran.
- [d9s1] At the 2006 census, its existence was noted, but its population was not reported.

**d10: Bardshelandan**

- [d10s0] Bardshelandan( also Romanized as Bardshelāndān; also known as Bardshelāldān) is a village in Shalil Rural District, Miankuh District, Ardal County, Chaharmahal and Bakhtiari Province, Iran.
- [d10s1] At the 2006 census, its existence was noted, but its population was not reported.

## 11. 2wikimultihopqa_9e9948280bdc11eba7f7acde48001122

原位置：`train` 第 71 题 · 全局第 71 题 · `sample_id: 2wikimultihopqa_9e9948280bdc11eba7f7acde48001122`

Question: What is the date of death of Brien Cokayne, 1St Baron Cullen Of Ashbourne's father?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Brien Cokayne, 1st Baron Cullen Of Ashbourne | False | () |
| u2 | date of death of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Brien Cokayne, 1st Baron Cullen of Ashbourne | False | [] | George Cokayne | [['d8s1']] |
| u2 | date of death of {u1} | True | ['u1'] | 6 August 1911 | [['d10s0']] |

### Source documents (reference only)

**d1: Albert Thompson (footballer, born 1912)**

- [d1s0] Albert Thompson( born 1912, date of death unknown) was a Welsh footballer.

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

**d3: Harry Johnson (wrestler)**

- [d3s0] Harry Johnson( 1903- date of death unknown) was an English wrestler.

**d4: Bill Smith (footballer, born 1897)**

- [d4s0] William Thomas Smith( born 9 April 1897, date of death unknown) was an English professional footballer.

**d5: Harry Wainwright (footballer)**

- [d5s0] Harry Wainwright( born 1899; date of death unknown) was an English footballer.

**d6: William Cullen, Baron Cullen of Whitekirk**

- [d6s0] William Douglas Cullen, Baron Cullen of Whitekirk,( born 18 November 1935) is a former senior member of the Scottish judiciary.
- [d6s1] He formerly served as Lord Justice General and Lord President of the Court of Session, and was an additional Lord of Appeal in the House of Lords prior to the transfer of its judicial functions to the Supreme Court.

**d7: Thomas Scott (diver)**

- [d7s0] Thomas Scott( 1907- date of death unknown) was an English diver.

**d8: Brien Cokayne, 1st Baron Cullen of Ashbourne**

- [d8s0] Brien Ibrican Cokayne, 1st Baron Cullen of Ashbourne (12 July 1864 – 3 November 1932) was a British businessman and banker.
- [d8s1] Cokayne was the fourth son of George Cokayne (originally George Adams), author of "The Complete Peerage", the son of William Adams and his second wife Mary Anne, granddaughter of Charles Cokayne, 5th Viscount Cullen.
- [d8s2] His mother was Mary Dorothea, daughter of George Henry Gibbs and sister of Hucks Gibbs, 1st Baron Aldenham.
- [d8s3] He was educated at Charterhouse School.
- [d8s4] Cokayne was a partner in the firm of Anthony Gibbs and Sons, merchants and bankers, and also served as Deputy Governor from 1915 to 1918 and as Governor from 1918 to 1920 of the Bank of England.
- [d8s5] Appointed a Knight Commander of the Order of the British Empire in 1917, in 1920 he was raised to the peerage as Baron Cullen of Ashbourne, of Roehampton in the County of Surrey, a revival of the Cullen title held by his paternal ancestors.
- [d8s6] He was also appointed a Grand Cordon of the Order of the Sacred Treasure by Japan.
- [d8s7] Lord Cullen of Ashbourne married Grace Margaret, daughter of Reverend the Hon.
- [d8s8] John Marsham, in 1904.
- [d8s9] They had three sons and three daughters.
- [d8s10] He died in November 1932, aged 68, and was succeeded in the barony by his eldest son Charles.

**d9: Theodred II (Bishop of Elmham)**

- [d9s0] Theodred II was a medieval Bishop of Elmham.
- [d9s1] The date of Theodred's consecration unknown, but the date of his death was sometime between 995 and 997.

**d10: George Edward Cokayne**

- [d10s0] George Edward Cokayne, (29 April 1825 – 6 August 1911), was an English genealogist and long-serving herald at the College of Arms in London, who eventually rose to the rank of Clarenceux King of Arms.
- [d10s1] He wrote the authoritative and standard reference works "The Complete Peerage" and "The Complete Baronetage".

## 12. 2wikimultihopqa_a1ef2dee085311ebbd59ac1f6bf848b6 【保留新拆法｜重标人工标签】

原位置：`train` 第 72 题 · 全局第 72 题 · `sample_id: 2wikimultihopqa_a1ef2dee085311ebbd59ac1f6bf848b6`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_a1ef2dee085311ebbd59ac1f6bf848b6"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。
>
> **处理建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。
>
> **证据定位：** d3s0, d1s1, d4s0, d9s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Are director of film A Woman's War and director of film The New Klondike from the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of director of A Woman's War | False | () |
| u2 | country of director of The New Klondike | False | () |
| u3 | whether directors of A Woman's War and The New Klondike are from the same country | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film A Woman's War | False | [] | Kim Ki-young | [['d3s0']] |
| u2 | nationality of {u1} | False | ['u1'] | South Korean | [['d1s1']] |
| u3 | director of film The New Klondike | False | [] | Lewis Milestone | [['d4s0']] |
| u4 | nationality of {u3} | False | ['u3'] | American | [['d9s0']] |
| u5 | whether the directors of A Woman's War and The New Klondike are from the same country | True | ['u2', 'u4'] | no | [[]] |

### Source documents (reference only)

**d1: Kim Ki-young**

- [d1s0] Kim Ki-young
- [d1s1] ( October 10, 1919 – February 5, 1998) was a South Korean film director, known for his intensely psychosexual and melodramatic horror films, often focusing on the psychology of their female characters.
- [d1s2] Kim was born in Seoul during the colonial period, raised in Pyongyang, where he became interested in theater and cinema.
- [d1s3] In Korea after the end of World War II, he studied dentistry while becoming involved in the theater.
- [d1s4] During the Korean War, he made propaganda films for the United States Information Service.
- [d1s5] In 1955, he used discarded movie equipments to produce his first two films.
- [d1s6] With the success of these two films Kim formed his own production company and produced popular melodramas for the rest of the decade.
- [d1s7] Kim
- [d1s8] Ki-young's first expression of his mature style was in his" The Housemaid"( 1960), which featured a powerful" femme fatale" character.
- [d1s9] It is widely considered to be one of the best Korean films of all time.
- [d1s10] After a" Golden Age" during the 1960s, the 1970s were a low- point in the history of Korean cinema because of governmental censorship and a decrease in audience attendance.
- [d1s11] Nevertheless, working independently, Kim produced some of his most eccentric cinematic creations in this era.
- [d1s12] Films such as" Insect Woman"( 1972) and" Iodo"( 1977) were successful at the time and highly influential on the younger generations of South Korean filmmakers both at their time of release, and with their rediscovery years later.
- [d1s13] By the 1980s, Kim's popularity had gone into decline, and his output decreased in the second half of the decade.
- [d1s14] Neglected by the mainstream during much of the 1990s, Kim became a cult figure in South Korean film Internet forums in the early 1990s.
- [d1s15] Widespread international interest in his work was stimulated by a career retrospective at the 1997 Pusan International Film Festival.
- [d1s16] He was preparing a comeback film when he and his wife were killed in a house fire in 1998.
- [d1s17] The Berlin International Film Festival gave Kim a posthumous retrospective in 1998, and the French Cinémathèque screened 18 of Kim's films, some newly rediscovered and restored, in 2006.
- [d1s18] Through the efforts of the Korean Film Council( KOFIC), previously lost films by Kim Ki- young continue to be rediscovered and restored.
- [d1s19] Many current prominent South Korean filmmakers, including directors Im Sang- soo, Kim Ki-duk, Bong Joon- ho and Park Chan- wook, claim Kim Ki- young as an influence on their careers.

**d2: Ben Cura**

- [d2s0] Ben Cura( born 30 September 1988) is a British- Argentine actor and director of film, television and theatre.

**d3: A Woman's War**

- [d3s0] A Woman's War( 여성전선-" Yeoseon jeonseon") a.k.a. Women at the Front is a 1957 South Korean film directed by Kim Ki-young.

**d4: The New Klondike**

- [d4s0] The New Klondike is a 1926 black- and- white silent romantic comedy sports drama film directed by Lewis Milestone for Famous Players- Lasky.
- [d4s1] The film was set against the backdrop of the Florida land boom of the 1920s, and stands as Ben Hecht's first film assignment.

**d5: Ian Barry (director)**

- [d5s0] Ian Barry is an Australian director of film and TV.

**d6: Brian Johnson (special effects artist)**

- [d6s0] Brian Johnson( born 1939 or 1940) is a British designer and director of film and television special effects.

**d7: Jason Moore (director)**

- [d7s0] Jason Moore( born October 22, 1970) is an American director of film, theatre and television.

**d8: Hanro Smitsman**

- [d8s0] Hanro Smitsman, born in 1967 in Breda( Netherlands), is a writer and director of film and television.

**d9: Lewis Milestone**

- [d9s0] Lewis Milestone( born Leib Milstein; September 30, 1895 – September 25, 1980) was a Russian- born American motion picture director.
- [d9s1] He is known for directing" Two Arabian Knights"( 1927) and" All Quiet on the Western Front"( 1930), both of which received Academy Awards for Best Director.
- [d9s2] He also directed" The Front Page"( 1931 – nomination)," The General Died at Dawn"( 1936)," Of Mice and Men"( 1939)," Ocean's 11"( 1960), and received the directing credit for" Mutiny on the Bounty"( 1962), though Marlon Brando largely appropriated his responsibilities during its production.

**d10: Peter Levin**

- [d10s0] Peter Levin is an American director of film, television and theatre.

## 13. 2wikimultihopqa_a1f429840baf11ebab90acde48001122

原位置：`train` 第 73 题 · 全局第 73 题 · `sample_id: 2wikimultihopqa_a1f429840baf11ebab90acde48001122`

Question: Who is the paternal grandmother of Mechthild Of Bavaria?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Mechthild Of Bavaria | False | () |
| u2 | mother of {u1}, Mechthild Of Bavaria's paternal grandmother | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Mechthild of Bavaria | False | [] | William IV, Duke of Bavaria | [['d9s1']] |
| u2 | mother of {u1}, Mechthild of Bavaria's paternal grandmother | True | ['u1'] | Kunigunde of Austria | [['d1s1']] |

### Source documents (reference only)

**d1: William IV, Duke of Bavaria**

- [d1s0] William IV (13 November 1493 – 7 March 1550) was Duke of Bavaria from 1508 to 1550, until 1545 together with his younger brother Louis X, Duke of Bavaria.
- [d1s1] He was born in Munich to Albert IV and Kunigunde of Austria, a daughter of Emperor Frederick III.

**d2: Kaoru Hatoyama**

- [d2s0] After the elections of 2009, she became more widely known as the grandmother of Prime Minister Yukio Hatoyama and his politician brother Kunio Hatoyama.

**d3: Tjuyu**

- [d3s0] Tjuyu( sometimes transliterated as Thuya or Thuyu) was an Egyptian noblewoman and the mother of queen Tiye, and the wife of Yuya.
- [d3s1] She is the grandmother of Akhenaten, and great grandmother of Tutankhamun.

**d4: Anne Denman**

- [d4s0] Anne Denman( 1587–1661) was born in Olde Hall, Retford, Nottinghamshire.
- [d4s1] Through a fortunate second marriage with Thomas Aylesbury, she became the grandmother of Lady Anne Hyde, Duchess of York and great- grandmother of Queen Mary II and Queen Anne.

**d5: Mona Hopton Bell**

- [d5s0] Mona Hopton Bell( 1867- 1940) was a British artist, best known for her portraits of civic figures.
- [d5s1] She was the grandmother of the painter Jean H. Bell.

**d6: Hubba bint Hulail**

- [d6s0] Hubba bint Hulail was the grandmother of Hashim ibn' Abd Manaf, thus the great- great- great- grandmother of the Islamic" Nabī"( Prophet) Muhammad ibn Abdullah.

**d7: Hannah Arnold**

- [d7s0] Hannah Arnold, also known as Hannah Waterman King, was the grandmother of Benedict Arnolds children.

**d8: Diana Guardato**

- [d8s0] Diana Guardato was a member of the aristocratic Patrician Guardato family, and had three children with King Ferdinand I: Diana Guardato is the 16th- Great Grandmother of His Royal Highness Albert II of Belgium, 15th- Great Grandmother of His Majesty Juan Carlos
- [d8s1] I of Spain, 17th- Great Grandmother of Philippe of Belgium, 14th- Great Grandmother of His Majesty Manuel II of Portugal, 16th- Great Grandmother of Grand Duke Henri, as well as many others.

**d9: Mechthild of Bavaria**

- [d9s0] Mechthild of Bavaria (12 July 1532 – 2 November 1565 in Baden-Baden) was a German noblewoman.
- [d9s1] She was the daughter of William IV, Duke of Bavaria and his wife Marie.
- [d9s2] She was buried in the Stiftskirche at Baden-Baden.
- [d9s3] On 17 January 1557 she married Philibert, Margrave of Baden-Baden, and they had the following children:
- [d9s4] Mechthild is a German form of Matilde.

**d10: Mechthild of Sayn**

- [d10s0] Countess Mechthild of Sayn( c. 1203 – c. 1291), also called Mechthild of Landsberg, Mechtild, Mechtildis or Mathilde, was the wife of Henry III of Sayn.
- [d10s1] She was an important figure in the Late Middle Ages because of her religious foundations(" Stiftungen").

## 14. 2wikimultihopqa_a383cf200baf11ebab90acde48001122

原位置：`train` 第 74 题 · 全局第 74 题 · `sample_id: 2wikimultihopqa_a383cf200baf11ebab90acde48001122`

Question: Who is Theodora Of Khazaria's father-in-law?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | husband of Theodora Of Khazaria | False | () |
| u2 | father of {u1}, Theodora Of Khazaria's father-in-law | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | spouse of Theodora of Khazaria | False | [] | Justinian II | [['d9s1']] |
| u2 | father of {u1}, Theodora of Khazaria's father-in-law | True | ['u1'] | Constantine IV | [['d5s1']] |

### Source documents (reference only)

**d1: John Adams (merchant)**

- [d1s0] John Adams( 1672 or 1673 – 1745) was an American- born Canadian merchant and member of the Nova Scotia Council.
- [d1s1] He was the father- in- law of Henry Newton( politician).

**d2: Ogawa Mataji**

- [d2s0] Viscount was a general in the early Imperial Japanese Army.
- [d2s1] He was also the father- in- law of Field Marshal Gen Sugiyama.

**d3: Barthold A. Butenschøn Sr.**

- [d3s0] Hans Barthold Andresen Butenschøn( 27 December 1877 – 28 November 1971) was a Norwegian businessperson.
- [d3s1] He was born in Kristiania as a son of Nils August Andresen Butenschøn and Hanna Butenschøn, and grandson of Nicolay Andresen.
- [d3s2] Together with Mabel Anette Plahte( 1877 – 1973, a daughter of Frithjof M. Plahte) he had the son Hans Barthold Andresen Butenschøn Jr. and was through him the father- in- law of Ragnhild Butenschøn and grandfather of Peter Butenschøn.
- [d3s3] Through his daughter Marie Claudine he was the father- in- law of Joakim Lehmkuhl, through his daughter Mabel Anette he was the father- in- law of Harald Astrup( a son of Sigurd Astrup) and through his daughter Nini Augusta he was the father- in- law of Ernst Torp.
- [d3s4] He took commerce school and agricultural school.
- [d3s5] He was hired in the family company N. A. Andresen& Co, and became a co-owner in 1910.
- [d3s6] He eventually became chief executive officer.
- [d3s7] The bank changed its name to Andresens Bank in 1913 and merged with Bergens Kreditbank in 1920.
- [d3s8] The merger was dissolved later in the 1920s.
- [d3s9] He was also a landowner, owning Nedre Skøyen farm and a lot of land in Enebakk.
- [d3s10] He chaired the board of Nydalens Compagnie from 1926, having not been a board member before that.
- [d3s11] He also chaired the supervisory council of Forsikringsselskapet Viking and Nedre Glommen salgsforening, and was a supervisory council member of Filharmonisk Selskap.
- [d3s12] He was a member of the gentlemen's club SK Fram since 1890, and was proclaimed a lifetime member in 1964.
- [d3s13] He was buried in Enebakk.

**d4: John Vernou Bouvier III**

- [d4s0] John Vernou" Black Jack" Bouvier III( May 19, 1891 – August 3, 1957) was an American Wall Street stockbroker and socialite.
- [d4s1] He was the father of First Lady Jacqueline Kennedy Onassis and of socialite Lee Radziwill, and was the father- in- law of John F. Kennedy.

**d5: Justinian II**

- [d5s0] Justinian II (668 – 11 December 711), surnamed the Rhinotmetos or Rhinotmetus , was the last Byzantine Emperor of the Heraclian dynasty, reigning from 685 to 695 and again from 705 to 711.
- [d5s1] Justinian II was an ambitious and passionate ruler who was keen to restore the Roman Empire to its former glories, but he responded poorly to any opposition to his will and lacked the finesse of his father, Constantine IV.
- [d5s2] Consequently, he generated enormous opposition to his reign, resulting in his deposition in 695 in a popular uprising, and he only returned to the throne in 705 with the help of a Bulgar and Slav army.
- [d5s3] His second reign was even more despotic than the first, and it too saw his eventual overthrow in 711, abandoned by his army who turned on him before killing him.

**d6: James Armour (Master mason)**

- [d6s0] James Armour (15 January 1730 – 20 September 1798) was a master mason and father of Jean Armour, and therefore the father-in-law of the poet Robert Burns.

**d7: Theodora of Alexandria**

- [d7s0] Theodora of Alexandria was a saint and Desert Mother who was married to a prefect of Egypt.
- [d7s1] In order to perform penance for a sin she committed, she disguised herself as a man and joined a monastery in Thebaid.
- [d7s2] Her true identity as a woman was discovered only after her death.
- [d7s3] A rare image of Theodora in Western art is a print by Bernardino Capitelli, made in 1627 for Theodora Costa dal Pozzo, showing St Theodora of Alexandria disguised as a monk and caring for the child that she was accused of fathering( Vienna: Graphische Sammlung Albertina).

**d8: Ludwig von Westphalen**

- [d8s0] Johann Ludwig von Westphalen( 11 July 1770 – 3 March 1842) was a liberal Prussian civil servant and the father- in- law of Karl Marx.

**d9: Theodora of Khazaria**

- [d9s0] Theodora of Khazaria (Greek:
- [d9s1] Θεοδώρα των Χαζάρων) was Byzantine empress as the second wife of Justinian II.
- [d9s2] She was a sister of Busir, khagan of the Khazars, but their relation to other Khazar rulers such as Bihar, father of the future Empress Tzitzak, is unknown.

**d10: Peter Burroughs**

- [d10s0] Peter Burroughs( born 27 January 1947) is a British television and film actor, the director of Willow Management.
- [d10s1] He is the father- in- law of actor and TV presenter Warwick Davis.

## 15. 2wikimultihopqa_a8e8237408a211ebbd7bac1f6bf848b6

原位置：`train` 第 75 题 · 全局第 75 题 · `sample_id: 2wikimultihopqa_a8e8237408a211ebbd7bac1f6bf848b6`

Question: Was Eric Newby or Raymond Griffith born first?

Note:

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | birth date of Eric Newby | False | () |
| u2 | birth date of Raymond Griffith | False | () |
| u3 | who was born first | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | birth date of Eric Newby | False | [] | 6 December 1919 | [['d6s0']] |
| u2 | birth date of Raymond Griffith | False | [] | January 23, 1895 | [['d7s0']] |
| u3 | which of Eric Newby and Raymond Griffith was born first | True | ['u1', 'u2'] | Raymond Griffith | [[]] |

### Source documents (reference only)

**d1: Paul Martin Newby**

- [d1s0] Paul Martin Newby( born May 5, 1955) is an American judge, who was first elected to a seat on the North Carolina Supreme Court in 2004.
- [d1s1] He is currently the sole Republican in the Supreme Court.

**d2: Joey Newby**

- [d2s0] Joseph Eric Newby( born March 8, 1982 in Soldotna, Alaska) is a professional baseball pitcher who is currently with the Amarillo Sox.
- [d2s1] Newby attended Colorado State University – Pueblo.

**d3: Wale Adebanwi**

- [d3s0] Wale Adebanwi( born 1969) is a Nigerian- born first Black Rhodes Professor at St Antony's College, Oxford.

**d4: Henry Moore (cricketer)**

- [d4s0] Henry Walter Moore( 1849 – 20 August 1916) was an English- born first- class cricketer who spent most of his life in New Zealand.

**d5: John Griffith (monk)**

- [d5s0] John Griffith or Griffin( fl. 1553) was a Welsh præmonstratensian and a monk of the order of Cistercians in Halesowen Abbey, Worcestershire.

**d6: Eric Newby**

- [d6s0] George Eric Newby (6 December 1919 – 20 October 2006) was an English travel author.
- [d6s1] Newby's best known works include "A Short Walk in the Hindu KushThe Last Grain Race", and "Round Ireland in Low Gear".

**d7: Raymond Griffith**

- [d7s0] Raymond Griffith( January 23, 1895 – November 25, 1957) was a silent movie comedian.
- [d7s1] Later in his career, he worked behind the camera as writer and producer.

**d8: Kate Newby**

- [d8s0] Kate Newby( born 1979) is an artist from New Zealand.

**d9: Jon Newby**

- [d9s0] Jonathan Philip Robert Newby( born 28 November 1978) is an English footballer, who played as a striker, and manager.

**d10: Maurice Griffith**

- [d10s0] Maurice Griffith( or Griffin; c. 1507 – 20 November 1558) was a Welshman who became Bishop of Rochester.

## 16. 2wikimultihopqa_aaf6d2540bda11eba7f7acde48001122

原位置：`train` 第 76 题 · 全局第 76 题 · `sample_id: 2wikimultihopqa_aaf6d2540bda11eba7f7acde48001122`

Question: Where was the place of death of the director of film The Island Of Desire?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of film The Island Of Desire | False | () |
| u2 | place of death of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film The Island of Desire | False | [] | Otis Turner | [['d1s0']] |
| u2 | place of death of {u1} | True | ['u1'] | Los Angeles | [['d9s2']] |

### Source documents (reference only)

**d1: The Island of Desire**

- [d1s0] The Island of Desire is a lost 1917 silent film adventure directed by Otis Turner, produced and distributed by Fox Film Corporation and starring George Walsh.

**d2: Olav Aaraas**

- [d2s0] Olav Aaraas( born 10 July 1950) is a Norwegian historian and museum director.
- [d2s1] He was born in Fredrikstad.
- [d2s2] From 1982 to 1993 he was the director of Sogn Folk Museum, from 1993 to 2010 he was the director of Maihaugen and from 2001 he has been the director of the Norwegian Museum of Cultural History.
- [d2s3] In 2010 he was decorated with the Royal Norwegian Order of St. Olav.

**d3: Peter Levin**

- [d3s0] Peter Levin is an American director of film, television and theatre.

**d4: Where Was I**

- [d4s0] " Where Was I?" may refer to:

**d5: Jesse E. Hobson**

- [d5s0] Jesse Edward Hobson( May 2, 1911 – November 5, 1970) was the director of SRI International from 1947 to 1955.
- [d5s1] Prior to SRI, he was the director of the Armour Research Foundation.

**d6: Brian Kennedy (gallery director)**

- [d6s0] Brian Patrick Kennedy( born 5 November 1961) is an Irish- born art museum director who has worked in Ireland and Australia, and now lives and works in the United States.
- [d6s1] He is currently the director of the Peabody Essex Museum.
- [d6s2] He was the director of the Toledo Museum of Art in Ohio from 2010 to 2019.
- [d6s3] He was the director of the Hood Museum of Art from 2005 to 2010, and the National Gallery of Australia( Canberra) from 1997- 2004.

**d7: Motherland (disambiguation)**

- [d7s0] Motherland is the place of one's birth, the place of one's ancestors, or the place of origin of an ethnic group.
- [d7s1] Motherland may also refer to:

**d8: Law of Desire**

- [d8s0] Law of Desire or La ley del deseo( in original Spanish) is a 1987 film written and directed by Pedro Almodóvar.
- [d8s1] Starring Eusebio Poncela as Pablo, Carmen Maura as Tina and Antonio Banderas as Antonio.
- [d8s2] It was the first film Almodóvar made independently with his own production company" El Deseo".
- [d8s3] The story focuses on a complex love triangle between two men and a trans woman.
- [d8s4] Pablo, a successful gay film director, disappointed in his relationship with his young lover, Juan, concentrates in a new project, a monologue starring his transsexual sister, Tina.
- [d8s5] Antonio, an uptight young man, falls possessively in love with the director and in his passion would stop at nothing to obtain the object of his desire.
- [d8s6] The relationship between Pablo and Antonio is at the core of the film, however, the story and own drama of Pablo's sister, Tina, plays a strong role in the plot.
- [d8s7] Shot in the later part of 1986," Law of Desire" was Almodóvar's first work centered in homosexual relationships.
- [d8s8] He considers" Law of Desire" the key film in his life and career.
- [d8s9] It follows the more serious tone set by Almodóvar's previous film," Matador", exploring the unrestrained force of desire.
- [d8s10] It s themes are: love, loss, gender, family, sexuality and the close link between life and art.
- [d8s11] " Law of Desire" was met with general positive reactions from film critics, and it was a hit with audiences becoming Almodóvar's most successful film up to that point.
- [d8s12] It toured many international film festival, winning the Teddy Award in Berlin and it made Almodóvar known internationally.
- [d8s13] Elements from" Law of Desire" grew into the basis for two later films: Carmen Maura appears in a stage production of Cocteau's" The Human Voice", which inspired Almodóvar's next film," Women on the Verge of a Nervous Breakdown"; and Tina's confrontation scene with an abusive priest formed a partial genesis for" Bad Education".

**d9: Otis Turner**

- [d9s0] Otis Turner( November 29, 1862 – March 28, 1918) was an American director, screenwriter and producer.
- [d9s1] Between 1908 and 1917, he directed 133 films and wrote 40 scenarios.
- [d9s2] He was born in Fairfield, Indiana, and died in Los Angeles.
- [d9s3] The producer/ director Otis Werner in L. Frank Baum's" Aunt Jane's Nieces Out West" is a send- up of Turner, who had adapted Baum's works into films, first in collaboration with Baum, then legally but without Baum's approval.

**d10: Ian Barry (director)**

- [d10s0] Ian Barry is an Australian director of film and TV.

## 17. 2wikimultihopqa_afd5796e0bdb11eba7f7acde48001122

原位置：`train` 第 77 题 · 全局第 77 题 · `sample_id: 2wikimultihopqa_afd5796e0bdb11eba7f7acde48001122`

Question: What is the date of death of the director of film For You I Have Sinned?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of film For You I Have Sinned | False | () |
| u2 | date of death of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film For You I Have Sinned | False | [] | Mario Costa | [['d2s0']] |
| u2 | date of death of {u1} | True | ['u1'] | 22 October 1995 | [['d3s0']] |

### Source documents (reference only)

**d1: Ian Barry (director)**

- [d1s0] Ian Barry is an Australian director of film and TV.

**d2: For You I Have Sinned**

- [d2s0] For You I Have Sinned is a 1953 Italian melodrama film directed by Mario Costa and starring Pierre Cressoy, Milly Vitale and Frank Latimore.

**d3: Mario Costa (director)**

- [d3s0] Mario Costa( Rome, 30 May 1904 – Rome, 22 October 1995) was an Italian actor, director and screenwriter, active from 1934 to 1971.

**d4: Made for You**

- [d4s0] " Made for You" may refer to:

**d5: Theodred II (Bishop of Elmham)**

- [d5s0] Theodred II was a medieval Bishop of Elmham.
- [d5s1] The date of Theodred's consecration unknown, but the date of his death was sometime between 995 and 997.

**d6: Only for You**

- [d6s0] Only for You may refer to:

**d7: I Care for You**

- [d7s0] " I Care for You" may refer to:

**d8: Fallin' for You**

- [d8s0] Fallin' for You or Falling for You may refer to:

**d9: For You**

- [d9s0] For You may refer to:

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

## 18. 2wikimultihopqa_b063b1ae0bd911eba7f7acde48001122

原位置：`train` 第 78 题 · 全局第 78 题 · `sample_id: 2wikimultihopqa_b063b1ae0bd911eba7f7acde48001122`

Question: What is the place of birth of the director of film Keystone Hotel (Film)?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of film Keystone Hotel (Film) | False | () |
| u2 | place of birth of {u1} | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Keystone Hotel | False | [] | Ralph Staub | [['d1s0']] |
| u2 | place of birth of {u1} | True | ['u1'] | Chicago | [['d4s0']] |

### Source documents (reference only)

**d1: Keystone Hotel (film)**

- [d1s0] Keystone Hotel (1935) is a two-reel comedy short subject, directed by Ralph Staub and released by the Vitaphone Corporation through Warner Bros. Pictures.
- [d1s1] Inspired by the silent comedies produced by Mack Sennett, the film reunites many of Sennett's former stars.

**d2: Peter Levin**

- [d2s0] Peter Levin is an American director of film, television and theatre.

**d3: Brian Kennedy (gallery director)**

- [d3s0] Brian Patrick Kennedy( born 5 November 1961) is an Irish- born art museum director who has worked in Ireland and Australia, and now lives and works in the United States.
- [d3s1] He is currently the director of the Peabody Essex Museum.
- [d3s2] He was the director of the Toledo Museum of Art in Ohio from 2010 to 2019.
- [d3s3] He was the director of the Hood Museum of Art from 2005 to 2010, and the National Gallery of Australia( Canberra) from 1997- 2004.

**d4: Ralph Staub**

- [d4s0] Ralph Staub( July 21, 1899 in Chicago, Illinois – October 22, 1969, Los Angeles, California) was a movie director, writer and producer.
- [d4s1] Three of his short subjects in the" Screen Snapshots" series have been nominated for the Academy Award and he was awarded a star on the Hollywood Walk of Fame at 1752 Vine Street in Hollywood, California, USA.

**d5: Jesse E. Hobson**

- [d5s0] Jesse Edward Hobson( May 2, 1911 – November 5, 1970) was the director of SRI International from 1947 to 1955.
- [d5s1] Prior to SRI, he was the director of the Armour Research Foundation.

**d6: Dana Blankstein**

- [d6s0] Dana Blankstein- Cohen( born March 3, 1981) is the director of the Israeli Academy of Film and Television.
- [d6s1] She is a film director, and an Israeli culture entrepreneur.

**d7: Jason Moore (director)**

- [d7s0] Jason Moore( born October 22, 1970) is an American director of film, theatre and television.

**d8: S. N. Mathur**

- [d8s0] S.N. Mathur was the Director of the Indian Intelligence Bureau between September 1975 and February 1980.
- [d8s1] He was also the Director General of Police in Punjab.

**d9: Ian Barry (director)**

- [d9s0] Ian Barry is an Australian director of film and TV.

**d10: Olav Aaraas**

- [d10s0] Olav Aaraas( born 10 July 1950) is a Norwegian historian and museum director.
- [d10s1] He was born in Fredrikstad.
- [d10s2] From 1982 to 1993 he was the director of Sogn Folk Museum, from 1993 to 2010 he was the director of Maihaugen and from 2001 he has been the director of the Norwegian Museum of Cultural History.
- [d10s3] In 2010 he was decorated with the Royal Norwegian Order of St. Olav.

## 19. 2wikimultihopqa_b14d20df097211ebbdb0ac1f6bf848b6 【需改：生成拆解】

原位置：`train` 第 79 题 · 全局第 79 题 · `sample_id: 2wikimultihopqa_b14d20df097211ebbdb0ac1f6bf848b6`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_b14d20df097211ebbdb0ac1f6bf848b6"></a>

> **审阅结论：需改：生成拆解**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 把完整地名“Marzian, Lorestan”中的行政区限定词当成另一个被比较对象，导致本应比较两个地点却生成三个事实单元。源文档标题与首句确认这是一个地点。
>
> **处理建议：** 将“Marzian, Lorestan”作为不可拆开的实体；恢复两个国家事实单元和一个必要比较结论，删除多余行政区单元并重建依赖。
>
> **证据定位：** d7s0, d3s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Are both Marzian, Lorestan and Vella located in the same country?

Note:

Type: comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | country of Marzian | False | () |
| u2 | country of Lorestan | False | () |
| u3 | country of Vella | False | () |
| u4 | whether Marzian, Lorestan and Vella are located in the same country | True | ('u1', 'u2', 'u3') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country where Marzian, Lorestan is located | False | [] | Iran | [['d7s0']] |
| u2 | country where Vella is located | False | [] | Switzerland | [['d3s0']] |
| u3 | whether Marzian, Lorestan and Vella are located in the same country | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Vignogn**

- [d1s0] Vignogn is a former municipality in the district of Surselva in the canton of Graubünden in Switzerland.
- [d1s1] The municipalities of Cumbel, Degen, Lumbrein, Morissen, Suraua, Vignogn, Vella, and Vrin merged on 1 January 2013 into the new municipality of Lumnezia.

**d2: Cumbel**

- [d2s0] Cumbel is a former municipality in the district of Surselva in the Swiss canton of Graubünden.
- [d2s1] The municipalities of Cumbel, Degen, Lumbrein, Morissen, Suraua, Vignogn, Vella, and Vrin merged on 1 January 2013 into the new municipality of Lumnezia.

**d3: Vella**

- [d3s0] Vella is a village and a former municipality in the district of Surselva in the canton of Graubünden in Switzerland.
- [d3s1] The municipalities of Cumbel, Degen, Lumbrein, Morissen, Suraua, Vignogn, Vella, and Vrin merged on 1 January 2013 into the new municipality of Lumnezia.

**d4: Morissen**

- [d4s0] Morissen is a former municipality in the district of Surselva in the Swiss canton of Graubünden.
- [d4s1] The municipalities of Cumbel, Degen, Lumbrein, Morissen, Suraua, Vignogn, Vella, and Vrin merged on 1 January 2013 into the new municipality of Lumnezia.

**d5: Animae Gospel Choir**

- [d5s0] The Animae Gospel Choir is a vocal ensemble based in Malta.
- [d5s1] It was founded in 2008 by Glen Vella and it has since grown into a 23 gospel singer- troupe.

**d6: Lumbrein**

- [d6s0] Lumbrein is a former municipality in the district of Surselva in the Swiss canton of Graubünden.
- [d6s1] The municipalities of Cumbel, Degen, Lumbrein, Morissen, Suraua, Vignogn, Vella, and Vrin merged on 1 January 2013 into the new municipality of Lumnezia.

**d7: Marzian, Lorestan**

- [d7s0] Marzian( also Romanized as Marzīān, Marzeyān, and Marzīyan) is a village in Japelaq -e Sharqi Rural District, Japelaq District, Azna County, Lorestan Province, Iran.
- [d7s1] At the 2006 census, its population was 738, in 178 families.

**d8: Vrin**

- [d8s0] Vrin is a village and a former municipality in the Lumnezia.
- [d8s1] It belonged to the circle of Lugnez/ Lumnezia in the district of Surselva in the canton of Graubünden in Switzerland.
- [d8s2] The municipalities of Cumbel, Degen, Lumbrein, Morissen, Suraua, Vignogn, Vella, and Vrin merged on 1 January 2013 into the new municipality of Lumnezia.
- [d8s3] In 1998, the village was awarded the Wakker Prize for the preservation of its architectural heritage.

**d9: Suraua**

- [d9s0] Suraua is a former municipality in the district of Surselva in the canton of Graubünden in Switzerland.
- [d9s1] The former municipality was formed on January 1, 2002 through the union of Camuns, Surcasti, Tersnaus, and Uors-Peiden.
- [d9s2] The municipalities of Cumbel, Degen, Lumbrein, Morissen, Suraua, Vignogn, Vella, and Vrin merged on 1 January 2013 into the new municipality of Lumnezia.

**d10: Degen, Switzerland**

- [d10s0] Degen is a former municipality in the district of Surselva in the Swiss canton of Graubünden.
- [d10s1] Until 1983, it was officially known as Igels.
- [d10s2] The municipalities of Cumbel, Degen, Lumbrein, Morissen, Suraua, Vignogn, Vella, and Vrin merged on 1 January 2013 into the new municipality of Lumnezia.

## 20. 2wikimultihopqa_b2fd9eb4089d11ebbd78ac1f6bf848b6

原位置：`train` 第 80 题 · 全局第 80 题 · `sample_id: 2wikimultihopqa_b2fd9eb4089d11ebbd78ac1f6bf848b6`

Question: Which film has the director who was born later, Ferocious Pal or My Sweet Little Village?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of Ferocious Pal | False | () |
| u2 | birth date of {u1} | False | ('u1',) |
| u3 | director of My Sweet Little Village | False | () |
| u4 | birth date of {u3} | False | ('u3',) |
| u5 | which film's director was born later | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of Ferocious Pal | False | [] | Spencer Gordon Bennet | [['d1s0']] |
| u2 | date of birth of {u1} | False | ['u1'] | January 5, 1893 | [['d7s0']] |
| u3 | director of My Sweet Little Village | False | [] | Jiří Menzel | [['d2s0']] |
| u4 | date of birth of {u3} | False | ['u3'] | 23 February 1938 | [['d8s0']] |
| u5 | which of the two films has the director born later | True | ['u2', 'u4'] | My Sweet Little Village | [[]] |

### Source documents (reference only)

**d1: Ferocious Pal**

- [d1s0] Ferocious Pal is a 1934 American adventure film directed by Spencer Gordon Bennet and written by Joseph Anthony Roach.
- [d1s1] The film stars Kazan the Wonder Dog, Ruth Sullivan, Gene Toler, Robert Seiter, Tom London and Harry Dunkinson.
- [d1s2] The film was released on February 2, 1934, by Principal Distributing.

**d2: My Sweet Little Village**

- [d2s0] My Sweet Little Village is a 1985 Czechoslovak film directed by Jiří Menzel.
- [d2s1] In 1987 it was nominated for an Academy Award for Best Foreign Language Film.
- [d2s2] At the 1986 Montreal World Film Festival, it won the" Special Jury Award" and" Prize of the Ecumenical Jury".
- [d2s3] At the Paris Film Festival in 1987 Hungarian actor János Bán received the" best actor" award.
- [d2s4] In a public survey conducted in January 2007 by the online news server Novinky.cz this movie was chosen by 22, 4% of voters( approximately 66,000 people) as the most popular Czech comedy in history.

**d3: Rumbi Katedza**

- [d3s0] Rumbi Katedza is a Zimbabwean Film Producer and Director who was born on 17 January 1974.

**d4: Sweet Little Lies (2012 film)**

- [d4s0] Sweet Little Lies is a 2012 Romanian comedy film directed by Iura Luncasu.

**d5: Hassan Zee**

- [d5s0] Hassan Zee is a Pakistani- American film director who was born in Chakwal, Pakistan.

**d6: W. Augustus Barratt**

- [d6s0] W. Augustus Barratt( 1873- 1947) was a Scottish- born, later American, songwriter and musician.

**d7: Spencer Gordon Bennet**

- [d7s0] Spencer Gordon Bennet( January 5, 1893 – October 8, 1987) was an American film producer and director.
- [d7s1] Known as the" King of Serial Directors", he directed more film serials than any other director.

**d8: Jiří Menzel**

- [d8s0] Jiří Menzel( born 23 February 1938, Prague) is a Czech film director, theatre director, actor, and screenwriter.
- [d8s1] His films often combine a humanistic view of the world with sarcasm and provocative cinematography.
- [d8s2] Some of these films are adapted from works by Czech writers such as Bohumil Hrabal and Vladislav Vančura.
- [d8s3] Menzel, a member of the Czech New Wave, became internationally famous in 1967, when his first feature film," Closely Watched Trains", won the Academy Award for Best Foreign Language Film.
- [d8s4] His controversial film" Larks on a String" was filmed in 1969, but was initially banned by the Czechoslovakian government.
- [d8s5] It was finally released in 1990 after the fall of the Communist regime.
- [d8s6] The film won the Golden Bear at the 40th Berlin International Film Festival.
- [d8s7] Menzel was nominated for an Academy Award for Best Foreign Language Film again in 1986 with his dark comedy" My Sweet Little Village".
- [d8s8] In 1987, he was a member of the jury at the 37th Berlin International Film Festival.
- [d8s9] In 1989 he was a member of the jury at the 16th Moscow International Film Festival.
- [d8s10] In 1995 he was a member of the jury at the 19th Moscow International Film Festival.
- [d8s11] He was awarded a IIFA Lifetime Achievement Award in November 2013.

**d9: Ben Palmer**

- [d9s0] Ben Palmer is a British film and television director who is known for being the director of" Bo' Selecta" and" The Inbetweeners".

**d10: Edward Yates**

- [d10s0] Edward J. Yates( September 16, 1918 – June 2, 2006) was an American television director who was the director of the ABC television program" American Bandstand" from 1952 until 1969.

## 21. 2wikimultihopqa_b3a5431b08cc11ebbd93ac1f6bf848b6 【保留新拆法｜重标人工标签】

原位置：`train` 第 81 题 · 全局第 81 题 · `sample_id: 2wikimultihopqa_b3a5431b08cc11ebbd93ac1f6bf848b6`

<!-- SFT_REVIEW_NOTE_BEGIN -->
<a id="human-review-2wikimultihopqa_b3a5431b08cc11ebbd93ac1f6bf848b6"></a>

> **审阅结论：保留新拆法｜重标人工标签**（AI 辅助审阅，待人工确认）
>
> **差异与原因：** 新拆法将每部电影的“导演身份+国籍”合在一个事实单元，旧拆法显式分开每一跳。新描述仍指向同一导演及其国籍，并未把电影国别当成导演国籍；在联合证据支持下两种粒度都合理。按用户要求保留新3单元，不恢复旧5单元。
>
> **处理建议：** 保持生成的3单元和 comparison。新u1的值对应旧u2，支持须同时覆盖旧u1的导演关系与旧u2的国籍；新u2对应旧u4，支持须覆盖旧u3与旧u4；新u3对应旧u5并依赖新u1/u2。按完整支持路径重建快照，不能只复制旧国籍单元的直接证据。
>
> **证据定位：** d6s1, d9s0, d8s0, d2s0；原句见本题 Source documents。
<!-- SFT_REVIEW_NOTE_END -->

Question: Do both directors of films One On One (1977 Film) and Ready Money (Film) share the same nationality?

Note:

Type: comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | nationality of director of One On One (1977 Film) | False | () |
| u2 | nationality of director of Ready Money (Film) | False | () |
| u3 | whether both directors share the same nationality | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film One on One (1977 film) | False | [] | Lamont Johnson | [['d6s1']] |
| u2 | nationality of {u1} | False | ['u1'] | American | [['d9s0']] |
| u3 | director of film Ready Money | False | [] | Oscar Apfel | [['d8s0']] |
| u4 | nationality of {u3} | False | ['u3'] | American | [['d2s0']] |
| u5 | whether the directors of One on One and Ready Money share the same nationality | True | ['u2', 'u4'] | yes | [[]] |

### Source documents (reference only)

**d1: Robby Benson**

- [d1s0] Robby Benson( born Robin David Segal; January 21, 1956), is an American actor, singer, musician, educator, director, producer, writer and composer.
- [d1s1] He rose to prominence as a teen idol in the late 1970s, appearing in the sports films" One on One"( 1977) and" Ice Castles"( 1978).
- [d1s2] He subsequently garnered fame for portraying the voice of Beast in the Disney animated film" Beauty and the Beast"( 1991) and its numerous sequels and spin- offs.
- [d1s3] He later forged a career in directing television, including six episodes of the sitcom" Friends".
- [d1s4] In addition to acting and directing, Benson is an activist in the field of heart research, having undergone four open- heart surgeries since age 28 to correct congenital aortic valve defects and related damage.
- [d1s5] In 2012, he published a memoir recounting his medical journey and numerous surgeries.

**d2: Oscar Apfel**

- [d2s0] Oscar C. Apfel( January 17, 1878 – March 21, 1938) was an American film actor, director, screenwriter and producer.
- [d2s1] He appeared in 167 films between 1913 and 1939, and also directed 94 films between 1911 and 1927.

**d3: One on One**

- [d3s0] One on One may refer to:

**d4: Journey Among Women**

- [d4s0] Journey Among Women is a 1977 film directed by Tom Cowan.

**d5: William Robinson (runholder)**

- [d5s0] William Robinson( 4 May 1814 – 9 September 1889), also known as Ready Money Robinson, was a New Zealand runholder and member of the New Zealand Legislative Council.

**d6: One on One (1977 film)**

- [d6s0] One on One is a 1977 sports drama film starring Robby Benson and Annette O'Toole.
- [d6s1] It was written by Benson and his father Jerry Segal, directed by Lamont Johnson, and features a soundtrack performed by Seals and Crofts.

**d7: Cheering Section**

- [d7s0] Cheering Section is a 1977 film.

**d8: Ready Money (film)**

- [d8s0] Ready Money is a 1914 American comedy silent film directed by Oscar Apfel adapted by James Montgomery from his play of the same name.
- [d8s1] The film stars Edward Abeles, Monroe Salisbury, Jode Mullally, Jane Darwell, Bessie Barriscale and Florence Dagmar.
- [d8s2] The film was released on November 5, 1914, by Paramount Pictures.

**d9: Lamont Johnson**

- [d9s0] Ernest Lamont Johnson Jr.( September 30, 1922 – October 24, 2010) was an American actor and film director who has appeared in and directed many television shows and movies.
- [d9s1] He won two Emmy Awards.

**d10: Mr. Right (2009 film)**

- [d10s0] Mr. Right is a 2009 British film directed by David Morris and Jacqui Morris.
- [d10s1] The jointly- made gay- themed film is the debut for both directors.

## 22. 2wikimultihopqa_b69ced00089911ebbd77ac1f6bf848b6

原位置：`train` 第 82 题 · 全局第 82 题 · `sample_id: 2wikimultihopqa_b69ced00089911ebbd77ac1f6bf848b6`

Question: Were Susan Howatch and Hans Coper of the same nationality?

Note:

Type: comparison · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | nationality of Susan Howatch | False | () |
| u2 | nationality of Hans Coper | False | () |
| u3 | whether Susan Howatch and Hans Coper were of the same nationality | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | nationality of Susan Howatch | False | [] | British | [['d7s0']] |
| u2 | nationality of Hans Coper | False | [] | British | [['d3s0']] |
| u3 | whether Susan Howatch and Hans Coper are of the same nationality | True | ['u1', 'u2'] | yes | [[]] |

### Source documents (reference only)

**d1: The Weather Station (1923 film)**

- [d1s0] The Weather Station( German: Der Wetterwart) is a 1923 German silent film directed by Carl Froelich and starring Mady Christians, Albert Steinrück and Hans Brausewetter.
- [d1s1] The film's sets were designed by the art directors Otto Erdmann and Hans Sohnle.

**d2: Helene Thimig**

- [d2s0] Helene Thimig (5 June 1889 – 7 November 1974) was an Austrian stage and film actress.
- [d2s1] She was the daughter of the actor Hugo Thimig and the sister of Hermann Thimig and Hans Thimig.

**d3: Hans Coper**

- [d3s0] Hans Coper( 8 April 1920 – 16 June 1981), was an influential German- born British studio potter.
- [d3s1] His work is often coupled with that of Lucie
- [d3s2] Rie due to their close association, even though their best known work differs dramatically, with Rie's being less sculptural, while Coper's was much more abstract, but also always functional.
- [d3s3] The latter point was noted by M. S. Thomas in his recent book" The Essential Potness."
- [d3s4] Coper always made functional vessels, principally containers for flowers( vases), fruit( bowls), candles( candle holders) including work for Coventry Cathedral and Sussex University meeting house.
- [d3s5] He made a small group of Figures in the fifties, which were not vessels and were never put on sale(" see" Tony Birks).

**d4: The Wheel of Fortune (novel)**

- [d4s0] " The Wheel of Fortune"( 1984) is a novel by Susan Howatch and recounts the trials and tribulations of a fictitious British family, the Godwins, who appear to be part of the minor aristocracy.
- [d4s1] As the title of the novel and Boethius' comments on Fortune as printed on the first page of the very first part suggest, defying the ravages of time and fate forms a central theme to this novel, where the six primary characters seek to challenge fate or to make their own destinies regardless of the social norms or circumstances of the time.

**d5: John of Sweden**

- [d5s0] John of Sweden- Swedish:" JohanJon" and" Hans"- may refer to:

**d6: A Hoax**

- [d6s0] A Hoax is a 1936 German comedy film directed by E.W. Emo and starring Paul Hörbiger, Trude Marlen and Hans Moser.
- [d6s1] The film's sets were designed by Otto Erdmann and Hans Sohnle.

**d7: Susan Howatch**

- [d7s0] Susan Howatch( born 14 July 1940) is a British author.
- [d7s1] Her writing career has been distinguished by family saga- type novels which describe the lives of related characters for long periods of time.
- [d7s2] Her later books have also become known for their religious and philosophical themes.

**d8: David Ji**

- [d8s0] David Longfen Ji is an American businessman who co-founded Apex Digital, an electronics manufacturer.
- [d8s1] In 2004, he was arrested in China following a dispute with Sichuan Changhong Electric, a supplier owned by the city of Mianyang and the province of Sichuan.
- [d8s2] Changhong accused him of defrauding them through bad checks.
- [d8s3] Ji was taken, according to an account by his lawyer, to the senior management and told, "I decide whether you live or die."
- [d8s4] He has been held in China without charges.
- [d8s5] Ji's case highlighted an "implicit racism" in dealings with American businessmen.
- [d8s6] As a U.S. citizen he was not granted the same treatment by authorities as non-ethnically Chinese businessmen sharing the same nationality.

**d9: Come Back (film)**

- [d9s0] Come Back is a 1953 West German drama film directed by Alfred Braun and starring Winnie Markus, Rudolf Prack and Hans Stüwe.
- [d9s1] The film's sets were designed by the art directors Hans Ledersteger, Ernst Richter and Hans Richter.

**d10: William Alfred Ismay**

- [d10s0] William Alfred Ismay or Bill Ismay( 10 April 1910 – 13 January 2001) was a librarian, writer and collector in Wakefield, West Yorkshire known for his significant collection of post -war studio pottery.
- [d10s1] The collection called the W.A. Ismay Collection was bequeathed to the Yorkshire Museum and is one of the world's largest collections of 20th- century studio pottery.
- [d10s2] It includes work by Bernard Leach, Hans Coper, Shoji Hamada, Takeshi Yasuda, David Leach Dan Arbeid and Lucie Rie.

## 23. 2wikimultihopqa_b6f259dc0baf11ebab90acde48001122

原位置：`train` 第 83 题 · 全局第 83 题 · `sample_id: 2wikimultihopqa_b6f259dc0baf11ebab90acde48001122`

Question: Who is the paternal grandmother of Ptolemy Viii Physcon?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Ptolemy Viii Physcon | False | () |
| u2 | mother of {u1}, Ptolemy Viii Physcon's paternal grandmother | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Ptolemy VIII Physcon | False | [] | Ptolemy V Epiphanes | [['d5s2']] |
| u2 | mother of {u1}, Ptolemy VIII Physcon's paternal grandmother | True | ['u1'] | Arsinoe III of Egypt | [['d8s0']] |

### Source documents (reference only)

**d1: Conall Collamrach**

- [d1s0] Conall Collamrach, son of Eterscél Temrach, son of Eochaid Ailtlethan, was, according to medieval Irish legend and historical tradition, a High King of Ireland.
- [d1s1] He succeeded to the throne on the death of his uncle Óengus Tuirmech Temrach, and ruled for five years, until he was killed by Nia Segamain.
- [d1s2] The" Lebor Gabála" synchronises his reign with that of Ptolemy VIII Physcon in Egypt( 145 – 116 BC).
- [d1s3] The chronology of Geoffrey Keating's" Foras Feasa ar Éirinn" dates his reign to 232–226 BC, that of the" Annals of the Four Masters" to 326–320 BC.

**d2: Titus Manlius Torquatus (consul 165 BC)**

- [d2s0] Titus Manlius Torquatus( born before 208 – died after 133 BC) was a politician of the Roman Republic, who became consul in 165 BC.
- [d2s1] Born into a prominent family, he sought to emulate the legendary severity of his ancestors, notably by forcing his son to commit suicide after he had been accused of corruption.
- [d2s2] Titus had a long career and was a respected jurist.
- [d2s3] He was also active in diplomatic affairs; he notably served as ambassador to Egypt in 162 BC in a mission to support the claims of Ptolemy VIII Physcon over Cyprus.

**d3: Anne Denman**

- [d3s0] Anne Denman( 1587–1661) was born in Olde Hall, Retford, Nottinghamshire.
- [d3s1] Through a fortunate second marriage with Thomas Aylesbury, she became the grandmother of Lady Anne Hyde, Duchess of York and great- grandmother of Queen Mary II and Queen Anne.

**d4: Harsiesi**

- [d4s0] Harsiesi(? – 130 BC) was an ancient Egyptian rebel against the rule of Ptolemy VIII Physcon of the Ptolemaic Dynasty.

**d5: Ptolemy VIII Physcon**

- [d5s0] Ptolemy VIII Euergetes II Tryphon ("Ptolemaĩos Euergétēs TryphonPtolemy the Benefactor, the luxurious"; c. 184 BC – 28 June 116 BC),
- [d5s1] nicknamed Physcon ("Fatty"), was a king of the Ptolemaic dynasty in Egypt.
- [d5s2] He was the younger son of Ptolemy V Epiphanes and Cleopatra I Syra.
- [d5s3] His reign was characterised by fierce political and military conflict with his older brother Ptolemy VI Philometor and his sister Cleopatra II.
- [d5s4] Ptolemy VIII was originally made co-ruler with his older siblings in the run-up to the Sixth Syrian War.
- [d5s5] In the course of that war, Ptolemy VI was captured and Ptolemy VIII became sole king of Egypt.
- [d5s6] When the war ended and Ptolemy VI was restored to the throne in 168 BC, the two brothers continued to quarrel.
- [d5s7] In 164 BC Ptolemy VIII drove out his brother and became sole king of the Ptolemaic empire, but he was expelled in turn in 163 BC.
- [d5s8] As a result of Roman intervention, Ptolemy VIII was awarded control of Cyrenaica.
- [d5s9] From there he repeatedly tried to capture Cyprus, which had also been promised to him by the Romans, from his brother.
- [d5s10] After Ptolemy VI's death in 145 BC, Ptolemy VIII returned to Egypt as co-ruler with his sister.
- [d5s11] His cruel treatment of opposition and his decision to marry his niece Cleopatra III and promote her to the status of co-regent led to a civil war from 132 to 126 BC, in which Cleopatra II controlled Alexandria and enjoyed the support of the Greek population of the country, while Ptolemy VIII and Cleopatra III controlled most of the rest of Egypt and were supported by the native Egyptians.
- [d5s12] During this war, native Egyptians were promoted to the highest echelons of the Ptolemaic government for the first time.
- [d5s13] Ptolemy was victorious and ruled alongside Cleopatra II and Cleopatra III until his death in 116 BC.
- [d5s14] The ancient Greek sources on Ptolemy VIII are extremely hostile, characterising him as cruel and mocking him as fat and degenerate, as part of a contrast with Ptolemy VI, whom they present extremely positively.
- [d5s15] The historian Günther Höbl calls him "one of the most brutal and at the same time one of the shrewdest politicians of the Hellenistic Age."

**d6: Kaoru Hatoyama**

- [d6s0] After the elections of 2009, she became more widely known as the grandmother of Prime Minister Yukio Hatoyama and his politician brother Kunio Hatoyama.

**d7: Hannah Arnold**

- [d7s0] Hannah Arnold, also known as Hannah Waterman King, was the grandmother of Benedict Arnolds children.

**d8: Ptolemy V Epiphanes**

- [d8s0] Ptolemy V Epiphanes ("Ptolemaĩos Epiphanḗs EucharistosPtolemy the Manifest, the Beneficent"; 9 October 210–September 180 BC), son of the siblings Ptolemy IV Philopator and Arsinoe III of Egypt, was the fifth ruler of the Ptolemaic dynasty from July/August 204 to September 180 BC.
- [d8s1] Ptolemy inherited the throne at the age of five, when his parents died in suspicious circumstances.
- [d8s2] The new regent, Agathocles was widely reviled and was toppled by a revolution in 202 BC, but the series of regents who followed proved incompetent and the kingdom was paralysed.
- [d8s3] The Seleucid king Antiochus III and the Antigonid king Philip V took advantage of the kingdom's weakness to begin the Fifth Syrian War (202-196 BC), in which the Ptolemies lost all their territories in Asia Minor and the Levant, as well as most of their influence in the Aegean Sea.
- [d8s4] Simultaneously, Ptolemy V faced a widespread Egyptian revolt (206-185 BC) led by self-proclaimed Pharaohs, which resulted in the loss of most of Upper Egypt and parts of Lower Egypt as well.
- [d8s5] Ptolemy V came of age in 196 BC and was crowned as Pharaoh in Memphis, an occasion commemorated by the creation of the Rosetta Stone.
- [d8s6] After this, he made peace with Antiochus III and married his daughter Cleopatra I in 194/3 BC.
- [d8s7] This disgusted the Romans who had entered into hostilities with Antiochus partially on Ptolemy's behalf - after their victory, they distributed the old Ptolemaic territories in Asia Minor to Pergamum and Rhodes rather than returning them to Egypt.
- [d8s8] However, Ptolemaic forces steadily reconquered the south of the country, bringing all of Upper Egypt back under Ptolemaic control in 186 BC.
- [d8s9] In his last years, Ptolemy began manoeuvring for renewed warfare with the Seleucid empire, but these plans were cut short by his sudden death in September 180 BC, allegedly poisoned by courtiers worried about the cost of the war.
- [d8s10] Ptolemy's reign saw greatly increased prominence of courtiers and the Egyptian priestly elite in Ptolemaic political life - a pattern that would continue for most of the rest of the kingdom's existence.
- [d8s11] It also marked the collapse of Ptolemaic power in the wider Mediterranean region.
- [d8s12] Arthur Eckstein has argued that this collapse sparked the 'power transition crisis' which led to the Roman conquest of the eastern Mediterranean.

**d9: Hubba bint Hulail**

- [d9s0] Hubba bint Hulail was the grandmother of Hashim ibn' Abd Manaf, thus the great- great- great- grandmother of the Islamic" Nabī"( Prophet) Muhammad ibn Abdullah.

**d10: Tjuyu**

- [d10s0] Tjuyu( sometimes transliterated as Thuya or Thuyu) was an Egyptian noblewoman and the mother of queen Tiye, and the wife of Yuya.
- [d10s1] She is the grandmother of Akhenaten, and great grandmother of Tutankhamun.

## 24. 2wikimultihopqa_b902985208d411ebbd97ac1f6bf848b6

原位置：`train` 第 84 题 · 全局第 84 题 · `sample_id: 2wikimultihopqa_b902985208d411ebbd97ac1f6bf848b6`

Question: Were Sami Yli-Sirniö and Torger Nergård of the same nationality?

Note:

Type: comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | nationality of Sami Yli-Sirniö | False | () |
| u2 | nationality of Torger Nergård | False | () |
| u3 | whether Sami Yli-Sirniö and Torger Nergård were of the same nationality | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | nationality of Sami Yli-Sirniö | False | [] | Finnish | [['d1s0']] |
| u2 | nationality of Torger Nergård | False | [] | Norwegian | [['d9s0']] |
| u3 | whether Sami Yli-Sirniö and Torger Nergård have the same nationality | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Sami Yli-Sirniö**

- [d1s0] Sami Yli- Sirniö( born April 10, 1972) is a Finnish musician.
- [d1s1] He is currently the lead guitarist of Finnish metal band Waltari, and German metal band Kreator.
- [d1s2] He spent part of his life in Germany and thus has strong ties with the German metal scene.
- [d1s3] German" Rock Hard" magazine featured him in 2007 as" forgotten guitar hero".

**d2: Kreator**

- [d2s0] Kreator( pronounced" creator") is a German thrash metal band from Essen, formed in 1982.
- [d2s1] Their current lineup consists of lead vocalist, lead and rhythm guitarist Mille Petrozza, drummer Jürgen" Ventor" Reil, lead guitarist Sami Yli- Sirniö, and bassist Frédéric Leclercq.
- [d2s2] The band's lineup has changed multiple times over its- year career, most noticeably with their bassists and lead guitarists.
- [d2s3] Petrozza and Reil are the only two original members left in Kreator, though the latter had one hiatus from the band, from 1994 to 1996.
- [d2s4] Kreator's musical style is similar to that of their compatriots Destruction, Sodom and Tankard, which is usually more complex and, since" Violent Revolution"( 2001), more melodic.
- [d2s5] Along with those three bands, Kreator has been referred to as one of the" Big Four" of Teutonic thrash metal, and they are often credited with helping pioneer death metal and black metal by containing several elements of what was to become those genres.
- [d2s6] The band's style has changed several times over the years, from a Venom- inspired speed metal sound, later moving into thrash metal, and including a period of transitioning from thrash to industrial metal and gothic metal throughout the 1990s.
- [d2s7] In the early 2000s, Kreator returned to their classic thrash sound, which has continued to the present.
- [d2s8] To date, Kreator has released fourteen studio albums, two EPs, two live albums and three compilation albums.
- [d2s9] They gained a large underground fanbase in the international thrash metal community, with their second studio album" Pleasure to Kill"( 1986) regarded as an influential album of the genre.
- [d2s10] Many of their subsequent albums – including" Terrible Certainty"( 1987)," Extreme Aggression"( 1989) and" Coma of Souls"( 1990) – were also highly acclaimed.
- [d2s11] Despite being an influential band, as well as one of the first European thrash metal acts to sign to a major label( signing to Epic Records in 1988), Kreator would not achieve mainstream popularity until later albums, including their thirteenth studio album" Phantom Antichrist"( 2012) and its follow- up" Gods of Violence"( 2017), both of which peaked at higher chart positions in many countries, with the latter reaching number one on the German charts.
- [d2s12] The band has achieved worldwide sales of over ten million units for combined sales of all their albums, making them one of the best- selling German thrash metal bands of all time.

**d3: Endorama**

- [d3s0] Endorama is the ninth studio album by German thrash metal band Kreator released in 1999 by Drakkar Records.
- [d3s1] The gothic metal influences were the most prominent on this release, and Lacrimosa frontman Tilo Wolff provided guest vocals on the title song.
- [d3s2] This is the last Kreator album to feature Tommy Vetterli, who was replaced by current guitarist Sami Yli- Sirniö shortly before the recording of their next album" Violent Revolution".

**d4: Marianne Rørvik**

- [d4s0] Marianne Rørvik (born August 2, 1983) is a Norwegian curler.
- [d4s1] She is the skip of the Norwegian national women's team.
- [d4s2] Rørvik has played in nine straight (1997–2005) World Junior Curling Championships, winning gold in 2004 playing third for Linn Githmark.
- [d4s3] In 2002, she was added as an alternate player on the Dordi Nordby rink.
- [d4s4] In 2005, she played second for the team, which included a trip to the 2006 Winter Olympics and a fourth-place finish.
- [d4s5] In 2006, she was promoted as the team's third, and finally with the retirement of Nordby in 2008, she got to skip the national team.
- [d4s6] Rørvik is in a relationship with fellow curler Torger Nergård and Mother of two children Karine (b. 2010) & Thale (b. 2013).

**d5: David Ji**

- [d5s0] David Longfen Ji is an American businessman who co-founded Apex Digital, an electronics manufacturer.
- [d5s1] In 2004, he was arrested in China following a dispute with Sichuan Changhong Electric, a supplier owned by the city of Mianyang and the province of Sichuan.
- [d5s2] Changhong accused him of defrauding them through bad checks.
- [d5s3] Ji was taken, according to an account by his lawyer, to the senior management and told, "I decide whether you live or die."
- [d5s4] He has been held in China without charges.
- [d5s5] Ji's case highlighted an "implicit racism" in dealings with American businessmen.
- [d5s6] As a U.S. citizen he was not granted the same treatment by authorities as non-ethnically Chinese businessmen sharing the same nationality.

**d6: Mathias Soggemoen**

- [d6s0] Mathias Soggemoen
- [d6s1] ( 5 October 1847 – 1929) was a Norwegian railway worker, mountain climbing pioneer and guide.
- [d6s2] Mathias Johnsen Soggemoen was born the oldest of seven siblings in Rauma in Møre og Romsdal, Norway.
- [d6s3] In 1875, he married Ingeborg Olsdatter Sogge Brekken and settled at the village of Veblungsnes.
- [d6s4] They were the parents of nine children.
- [d6s5] Later in life, Mathias and Ingeborg Soggemoen emigrated to America with several of their children.
- [d6s6] Soggemoen is known for a number of first ascents of Norwegian mountains.
- [d6s7] Among his first ascents are Store Austanbotntind( 1883, with Carl Hall), Store Styggedalstinden( 1883, with Hall), Midtre Skagastølstind( 1884, with Hall), Hjelledalstind( 1884, with Hall), Storebjørn( 1884, with Hall), and Sentraltind( 1885, with Hall and Torger S. Sulheim).
- [d6s8] He also climbed Romsdalshornet in 1881.
- [d6s9] In 1886 Soggemoen and Hall made the first known ascent of Saksi( 2,189 m.a.s.l.).

**d7: Thomas Løvold**

- [d7s0] Thomas Løvold( born 27 January 1981) is a Norwegian curler.
- [d7s1] At Junior level, Løvold competed as skip and won gold medals at the 2002 and 2003 World Junior Curling Championships" B" tournaments.
- [d7s2] He has gained worldwide attention for having played as the alternate for Team Thomas Ulsrud at the 2010 Vancouver Winter Olympics and played third for Team Torger Nergård at the 2010 World Curling Championship in Cortina d' Ampezzo, Italy, winning the silver medal at both tournaments.
- [d7s3] Thomas Løvold also skips his own team on World Curling Tour events.
- [d7s4] His most successful tournament was the 2009 Lucerne Curling Trophy where his team made it to the semi-finals but lost to Team Ralph Stöckli of Switzerland.

**d8: Violent Revolution**

- [d8s0] Violent Revolution is the tenth studio album by the German thrash metal band Kreator.
- [d8s1] It was released on September 25, 2001.
- [d8s2] After almost a decade of musical experimentation with their metal sound( starting with" Renewal"), with this album the band returned to their 1980s thrash metal style, although it does make use of Gothenburg metal elements.
- [d8s3] " Violent Revolution" is also the first Kreator album to feature lead guitarist Sami Yli- Sirniö.

**d9: Torger Nergård**

- [d9s0] Torger Nergård, also spelled Nergaard( born 12 December 1974 in Trondheim) is a Norwegian curler from Oslo.

**d10: Petri Hiltunen**

- [d10s0] Petri Hiltunen( born 13 October 1967) is a Finnish cartoonist and illustrator.
- [d10s1] Hiltunen has produced work in a variety of genres, but is most notable for his fantasy and horror work.
- [d10s2] He has won the prestigious Puupäähattu award in 2002, which is regarded as the highest honour for Finnish comic artists.
- [d10s3] He is also a well- known figure in Finnish science fiction fandom and a regular panelist and guest of honour at conventions, such as Finncon.
- [d10s4] His own comic albums include the horror/ fantasy tale" Laulu yön lapsistaSong of the children of the night"), exploring the vampire folklore of 1562 Russia during the reign of Ivan the Terrible, and a graphic novel version of" Macbeth".
- [d10s5] The fantasy world of Jaconia, created for his" Praedor" comics, has been adapted into a role- playing game of the same name.
- [d10s6] His work has also been featured in the science fiction magazine" Tähtivaeltaja", the Finnish" Conan" magazine and twice in the war comics magazine" Korkeajännitys": a western story and one story set in the Finnish War.
- [d10s7] His drawing style is quite detailed, particularly with his characters, and features heavy lines.
- [d10s8] Hiltunen is best known in the Finnish popular consciousness from his much lighter, humorous newspaper comic strip" Väinämöisen paluu The Return of Väinämöinen"), published in many major newspapers and as comic books.
- [d10s9] In it, the Eternal Sage of" Kalevala" ends his self- imposed exile to find that he might have been gone for too long.
- [d10s10] He must try to adjust to modern Finland( e.g. finding out that these newfangled" potatoes" are now considered a traditional food) as modern Finland must try to adjust to him( e.g. a group of neo-nazis coming to greet him and introducing themselves as indigenous
- [d10s11] Finns; they are nonplussed when he starts apologizing and it turns out he thought they were Sami.)
- [d10s12] As the culture shock gradually faded, the strip became a more character- based comedy but eventually faded in turn.

## 25. 2wikimultihopqa_b99cad180baf11ebab90acde48001122

原位置：`train` 第 85 题 · 全局第 85 题 · `sample_id: 2wikimultihopqa_b99cad180baf11ebab90acde48001122`

Question: Who is Scholastique Of Champagne's paternal grandmother?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | father of Scholastique Of Champagne | False | () |
| u2 | mother of {u1}, Scholastique Of Champagne's paternal grandmother | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Scholastique of Champagne | False | [] | Henry I, Count of Champagne | [['d8s0']] |
| u2 | mother of {u1}, Scholastique of Champagne's paternal grandmother | True | ['u1'] | Matilda of Carinthia | [['d1s1']] |

### Source documents (reference only)

**d1: Henry I, Count of Champagne**

- [d1s0] Henry I (December 1127 – March 16, 1181), known as the Liberal, was count of Champagne from 1152 to 1181.
- [d1s1] He was the eldest son of Count Thibaut II of Champagne (who was also Count Thibaut IV of Blois) and his wife, Matilda of Carinthia.
- [d1s2] Henry took part in the Second Crusade under the leadership of Louis VII of France.
- [d1s3] He carried a letter of recommendation from Bernard of Clairvaux addressed to Manuel I Komnenos, Byzantine Emperor; he is listed among the notables present at the assembly held by Baldwin III of Jerusalem at Acre on 24 June 1148.
- [d1s4] On his father's death, Henry chose to take Champagne, leaving the family's older holdings (including Blois, Chartres, Sancerre, and Châteaudun) to his younger brothers.
- [d1s5] At the time this may have been surprising, for the other territories were richer and better developed.
- [d1s6] Henry must have foreseen the economic possibilities of Champagne, and it is during his rule that the county achieved its high place as one of the richest and strongest of the French principalities.
- [d1s7] Henry established orderly rule over the nobles of Champagne, and could fairly reliably count on the aid of some 2,000 vassals, which just by itself made him a power few in France could equal.
- [d1s8] This order in turn made Champagne a safe place for merchants to gather, and under the count's protection the Champagne Fairs became a central part of long-distance trade and finance in medieval Europe.
- [d1s9] In addition, the count's court in Troyes became a renowned literary center.
- [d1s10] Walter Map was among those who found hospitality there.
- [d1s11] The scholar Stephen of Alinerre was among Henry's courtiers, becoming chancellor of the county in 1176.
- [d1s12] In 1179 Henry went to Jerusalem again with a party of French knights including his relatives Peter of Courtenay (brother of Louis VII) and Philip of Dreux, bishop of Beauvais.
- [d1s13] Henry returned towards Europe by the land route across Asia Minor, and was captured and held to ransom by Kilij Arslan II, Seljuk sultan of Rüm.
- [d1s14] The ransom was paid by the Byzantine Emperor.
- [d1s15] Henry died on 16 March 1181.
- [d1s16] In 1164, Henry married Marie of France, daughter of Louis VII of France and Eleanor of Aquitaine.
- [d1s17] They had four children:
- [d1s18] Henry built the collegiate church of Saint-Étienne in Troyes between 1157 and 1171, which he planned as a necropolis for the House of Blois.
- [d1s19] He was buried there, as was his son Theobald III, but most of his descendants were buried elsewhere.
- [d1s20] He died in 1181 and was succeeded by their eldest son Henry.
- [d1s21] After Henry became king of Jerusalem, the younger son Theobald became count.

**d2: Anne Denman**

- [d2s0] Anne Denman( 1587–1661) was born in Olde Hall, Retford, Nottinghamshire.
- [d2s1] Through a fortunate second marriage with Thomas Aylesbury, she became the grandmother of Lady Anne Hyde, Duchess of York and great- grandmother of Queen Mary II and Queen Anne.

**d3: Kaoru Hatoyama**

- [d3s0] After the elections of 2009, she became more widely known as the grandmother of Prime Minister Yukio Hatoyama and his politician brother Kunio Hatoyama.

**d4: Hannah Arnold**

- [d4s0] Hannah Arnold, also known as Hannah Waterman King, was the grandmother of Benedict Arnolds children.

**d5: Hubba bint Hulail**

- [d5s0] Hubba bint Hulail was the grandmother of Hashim ibn' Abd Manaf, thus the great- great- great- grandmother of the Islamic" Nabī"( Prophet) Muhammad ibn Abdullah.

**d6: Purnima (Hindi actress)**

- [d6s0] Purnima Das Verma( born Meherbhano Mohammad Ali) was an Indian film actress who worked predominantly in Hindi language films.
- [d6s1] She is the grandmother of actor Emraan Hashmi.

**d7: Diana Guardato**

- [d7s0] Diana Guardato was a member of the aristocratic Patrician Guardato family, and had three children with King Ferdinand I: Diana Guardato is the 16th- Great Grandmother of His Royal Highness Albert II of Belgium, 15th- Great Grandmother of His Majesty Juan Carlos
- [d7s1] I of Spain, 17th- Great Grandmother of Philippe of Belgium, 14th- Great Grandmother of His Majesty Manuel II of Portugal, 16th- Great Grandmother of Grand Duke Henri, as well as many others.

**d8: Scholastique of Champagne**

- [d8s0] Scholastique of Champagne( 1172–1219) was the daughter of Marie, Countess of Champagne and Henry I, Count of Champagne.

**d9: Mona Hopton Bell**

- [d9s0] Mona Hopton Bell( 1867- 1940) was a British artist, best known for her portraits of civic figures.
- [d9s1] She was the grandmother of the painter Jean H. Bell.

**d10: Tjuyu**

- [d10s0] Tjuyu( sometimes transliterated as Thuya or Thuyu) was an Egyptian noblewoman and the mother of queen Tiye, and the wife of Yuya.
- [d10s1] She is the grandmother of Akhenaten, and great grandmother of Tutankhamun.

## 26. 2wikimultihopqa_ba94e15808c211ebbd8cac1f6bf848b6

原位置：`train` 第 86 题 · 全局第 86 题 · `sample_id: 2wikimultihopqa_ba94e15808c211ebbd8cac1f6bf848b6`

Question: Who was born earlier, Suzy Mckee Charnas or Tariq Anam Khan?

Note:

Type: comparison · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | birth date of Suzy Mckee Charnas | False | () |
| u2 | birth date of Tariq Anam Khan | False | () |
| u3 | who was born earlier | True | ('u1', 'u2') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | date of birth of Suzy McKee Charnas | False | [] | 22 October 1939 | [['d1s0']] |
| u2 | date of birth of Tariq Anam Khan | False | [] | 10 May 1953 | [['d8s0']] |
| u3 | who was born earlier, Suzy McKee Charnas or Tariq Anam Khan | True | ['u1', 'u2'] | Suzy McKee Charnas | [[]] |

### Source documents (reference only)

**d1: Suzy McKee Charnas**

- [d1s0] Suzy McKee Charnas( born 22 October 1939) is an American novelist and short story writer, writing primarily in the genres of science fiction and fantasy.
- [d1s1] She has won several awards for her fiction, including the Hugo Award, the Nebula Award and the James Tiptree Jr. Award.
- [d1s2] A selection of her short fiction was collected in" Stagestruck Vampires and Other Phantasms" in 2004.
- [d1s3] " The Holdfast Chronicles", a four- volume story written over the course of almost thirty years( the first installment," Walk to the End of the World" was published in 1974, and the last installment," The Conqueror's Child" was published in 1999) is considered to be her major accomplishment in writing.
- [d1s4] The series addresses the topics of feminist dystopia, separatist societies, war, and reintegration.
- [d1s5] Another of her major works," The Vampire Tapestry", has been adapted( by Charnas herself) into a play called" Vampire Dreams".
- [d1s6] She lives in New Mexico.

**d2: Joël Henry (journalist)**

- [d2s0] Joël Henry( born 1955) is a French journalist who was born in Strasbourg.

**d3: Jeff Barlow**

- [d3s0] Jeff Barlow was a British actor who was born in Lancashire in 1871.

**d4: John Veltri**

- [d4s0] John Veltri is a photographer who was born in 1938 in New Jersey.

**d5: Evan Crooks**

- [d5s0] Evan Crooks is an American actor who was born in Fresno County, California.

**d6: Shannah Trailor**

- [d6s0] Shannah Trailor( born 1983) is an African- American author who was born in Chicago.

**d7: Huc-Mazelet Luquiens**

- [d7s0] Huc- Mazelet Luquiens( 1881 — 1961) was an American printmaker, painter and art educator who was born June 30, 1881 in Massachusetts to Jules Luquiens a French- speaking Swiss and Emma Clark who was born in Ohio.

**d8: Tariq Anam Khan**

- [d8s0] Tariq Anam Khan( born 10 May 1953) is a Bangladeshi actor, director, writer and producer in theatre, television, and film.
- [d8s1] He was awarded the Bangladesh National Film Award for Best Actor in negative role for the film in 2014.
- [d8s2] He is founding member and leader of prominent Bangladeshi theatre group, Natyakendra, where he holds the position of Principal Secretary.
- [d8s3] Khan was a freedom fighter in the liberation war of Bangladesh in 1971.

**d9: Zaven Paré**

- [d9s0] Zaven Paré is a French new media artist who was born in 1961.

**d10: Pauline Delpech**

- [d10s0] Pauline Delpech is a writer and a French actress who was born in 1981.

## 27. 2wikimultihopqa_bd95c40f08bc11ebbd89ac1f6bf848b6

原位置：`train` 第 87 题 · 全局第 87 题 · `sample_id: 2wikimultihopqa_bd95c40f08bc11ebbd89ac1f6bf848b6`

Question: Do both films, Bad Men Of The Hills and Desert Thieves, have the directors who are from the same country?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of Bad Men Of The Hills | False | () |
| u2 | country of origin of {u1} | False | ('u1',) |
| u3 | director of Desert Thieves | False | () |
| u4 | country of origin of {u3} | False | ('u3',) |
| u5 | whether {u2} and {u4} are the same | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Bad Men of the Hills | False | [] | William Berke | [['d6s0']] |
| u2 | country descriptor of {u1} | False | ['u1'] | American | [['d7s0']] |
| u3 | director of film Desert Thieves | False | [] | Scott Sidney | [['d10s0']] |
| u4 | country descriptor of {u3} | False | ['u3'] | American | [['d3s0']] |
| u5 | whether the directors of Bad Men of the Hills and Desert Thieves are from the same country | True | ['u2', 'u4'] | yes | [[]] |

### Source documents (reference only)

**d1: Bad Men of Missouri**

- [d1s0] Bad Men of Missouri is a 1941 American Western film directed by Ray Enright and written by Charles Grayson.
- [d1s1] The film stars Dennis Morgan, Jane Wyman, Wayne Morris and Arthur Kennedy.
- [d1s2] The film was released by Warner Bros. on July 26, 1941.

**d2: City of Bad Men**

- [d2s0] City of Bad Men is a 1953 Technicolor Western film directed by Harmon Jones and starring Jeanne Crain and Dale Robertson.

**d3: Scott Sidney**

- [d3s0] Scott Sidney (1872 – 20 July 1928), born Harry Wilbur Siggins, was an American film director.
- [d3s1] He directed 117 films between 1913 and 1927.
- [d3s2] He died in London, England, United Kingdom.

**d4: 3 Bad Men**

- [d4s0] 3 Bad Men is a 1926 American Western film directed by John Ford.
- [d4s1] Bob Mastrangelo has called it "One of John Ford's greatest silent epics.
- [d4s2] " The film had inspired the title for Akira Kurosawa's 1958 film "Three Bad Men in a Hidden Fortress", simply known as "The Hidden Fortress" in the rest of the world.

**d5: The Arizona Raiders**

- [d5s0] The Arizona Raiders is a 1936 American western film directed by James P. Hogan and starring Buster Crabbe and Marsha Hunt.
- [d5s1] It was based on a Zane Grey novel and released by Paramount Pictures.
- [d5s2] The film is also known as Bad Men of Arizona( American reissue title).

**d6: Bad Men of the Hills**

- [d6s0] Bad Men of the Hills is a 1942 American Western film directed by William Berke and written by Luci Ward.
- [d6s1] The film stars Charles Starrett, Russell Hayden, Cliff Edwards, Luana Walters, Alan Bridge and Guy Usher.
- [d6s2] The film was released on August 13, 1942, by Columbia Pictures.

**d7: William Berke**

- [d7s0] William A. Berke( October 3, 1903 – February 15, 1958) was an American film director, producer and screenwriter.
- [d7s1] He directed nearly 90 films between 1934 and 1958.
- [d7s2] He also produced nearly 80 films between 1933 and 1958.
- [d7s3] He was born in Milwaukee, Wisconsin and died in Los Angeles, California.
- [d7s4] Richard Fleischer later recalled Berke" was known as King of the B's.
- [d7s5] For years and years he had made nothing but pictures with ten or twelve day shooting schedules, minuscule budgets of about$ 100,000 and no stars.
- [d7s6] Without bothering with editing or any postproduction chores and with short shooting schedules, he was able to squeeze in eight or ten pictures a year.
- [d7s7] And he was going nuts".
- [d7s8] According to Fleischer, Berke eventually pestered RKO executives enough to be assigned an A picture with a long shooting schedule and stars and he still shot it in twelve days.

**d8: Bad Men of the Border**

- [d8s0] Bad Men of the Border is a 1945 American Western film directed by Wallace Fox and written by Adele Buffington.
- [d8s1] The film stars Kirby Grant, Fuzzy Knight, Armida, John Eldredge, Barbara Sears and Edward Howard.
- [d8s2] The film was released on September 28, 1945, by Universal Pictures.

**d9: Bar-Z Bad Men**

- [d9s0] Bar-Z Bad Men is a 1937 American Western film directed by Sam Newfield and starring Johnny Mack Brown.

**d10: Desert Thieves**

- [d10s0] Desert Thieves is a 1914 American silent short western film directed by Scott Sidney and featuring Charles Ray, Gretchen Lederer, Tsuru Aoki, Frank Keenan and Ernest Swallow in lead roles.

## 28. 2wikimultihopqa_c09bb4380baf11ebab90acde48001122

原位置：`train` 第 88 题 · 全局第 88 题 · `sample_id: 2wikimultihopqa_c09bb4380baf11ebab90acde48001122`

Question: Who is Ultragotha's father-in-law?

Note:

Type: bridge · fallback: False · SFT snapshots: 8

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | spouse of Ultragotha | False | () |
| u2 | father of {u1}, Ultragotha's father-in-law | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | spouse of Ultragotha | False | [] | Childebert I | [['d5s0']] |
| u2 | father of {u1}, Ultragotha's father-in-law | True | ['u1'] | Clovis I | [['d6s0']] |

### Source documents (reference only)

**d1: Peter Burroughs**

- [d1s0] Peter Burroughs( born 27 January 1947) is a British television and film actor, the director of Willow Management.
- [d1s1] He is the father- in- law of actor and TV presenter Warwick Davis.

**d2: Harry Smith (athlete)**

- [d2s0] Harry James Smith( July 30, 1888 – November 20, 1962) was an American long- distance runner.
- [d2s1] He was most notable for competing in the 1912 Olympics in Stockholm.
- [d2s2] He was also the father of Hart wrestling family matriarch Helen Hart and the father- in- law of Stu Hart.

**d3: Ogawa Mataji**

- [d3s0] Viscount was a general in the early Imperial Japanese Army.
- [d3s1] He was also the father- in- law of Field Marshal Gen Sugiyama.

**d4: John Adams (merchant)**

- [d4s0] John Adams( 1672 or 1673 – 1745) was an American- born Canadian merchant and member of the Nova Scotia Council.
- [d4s1] He was the father- in- law of Henry Newton( politician).

**d5: Ultragotha**

- [d5s0] Ultragotha (or Ultrogothe), 510 - after 566/567, was a Frankish queen of the Merovingian dynasty via her marriage to Childebert I, reigning from c.541-558.
- [d5s1] They had two daughters, possibly named "Chrodoberge" et "Chrodesinde".
- [d5s2] When Childebert died in 558, his brother Clotaire I seized his kingdom and took control of the Palais de la Cité in Paris, where the royal treasures and the family of the deceased were.
- [d5s3] According to Gregory of Tours, he then condemned Ultrogotha and the two daughters to prison.
- [d5s4] Upon reuniting the kingdom of Clovis, Clotaire I freed them; the daughters likely became nuns.
- [d5s5] She died in around 567 and was buried in the St-Germain-des-Prés along with Childebert.
- [d5s6] The two daughters are also buried there.
- [d5s7] In 580, again according to Gregory of Tours, Ultrogotha's former Chancellor, , was chosen by Maurilio, bishop of Cahors, as his successor..

**d6: Childebert I**

- [d6s0] Childebert I (c. 496 – 13 December 558) was a Frankish King of the Merovingian dynasty, as third of the four sons of Clovis I who shared the kingdom of the Franks upon their father's death in 511.
- [d6s1] He was one of the sons of Saint Clotilda, born at Reims.
- [d6s2] He reigned as King of Paris from 511 to 558 and Orléans from 524 to 558.

**d7: Ludwig von Westphalen**

- [d7s0] Johann Ludwig von Westphalen( 11 July 1770 – 3 March 1842) was a liberal Prussian civil servant and the father- in- law of Karl Marx.

**d8: John Vernou Bouvier III**

- [d8s0] John Vernou" Black Jack" Bouvier III( May 19, 1891 – August 3, 1957) was an American Wall Street stockbroker and socialite.
- [d8s1] He was the father of First Lady Jacqueline Kennedy Onassis and of socialite Lee Radziwill, and was the father- in- law of John F. Kennedy.

**d9: Barthold A. Butenschøn Sr.**

- [d9s0] Hans Barthold Andresen Butenschøn( 27 December 1877 – 28 November 1971) was a Norwegian businessperson.
- [d9s1] He was born in Kristiania as a son of Nils August Andresen Butenschøn and Hanna Butenschøn, and grandson of Nicolay Andresen.
- [d9s2] Together with Mabel Anette Plahte( 1877 – 1973, a daughter of Frithjof M. Plahte) he had the son Hans Barthold Andresen Butenschøn Jr. and was through him the father- in- law of Ragnhild Butenschøn and grandfather of Peter Butenschøn.
- [d9s3] Through his daughter Marie Claudine he was the father- in- law of Joakim Lehmkuhl, through his daughter Mabel Anette he was the father- in- law of Harald Astrup( a son of Sigurd Astrup) and through his daughter Nini Augusta he was the father- in- law of Ernst Torp.
- [d9s4] He took commerce school and agricultural school.
- [d9s5] He was hired in the family company N. A. Andresen& Co, and became a co-owner in 1910.
- [d9s6] He eventually became chief executive officer.
- [d9s7] The bank changed its name to Andresens Bank in 1913 and merged with Bergens Kreditbank in 1920.
- [d9s8] The merger was dissolved later in the 1920s.
- [d9s9] He was also a landowner, owning Nedre Skøyen farm and a lot of land in Enebakk.
- [d9s10] He chaired the board of Nydalens Compagnie from 1926, having not been a board member before that.
- [d9s11] He also chaired the supervisory council of Forsikringsselskapet Viking and Nedre Glommen salgsforening, and was a supervisory council member of Filharmonisk Selskap.
- [d9s12] He was a member of the gentlemen's club SK Fram since 1890, and was proclaimed a lifetime member in 1964.
- [d9s13] He was buried in Enebakk.

**d10: James Armour (Master mason)**

- [d10s0] James Armour (15 January 1730 – 20 September 1798) was a master mason and father of Jean Armour, and therefore the father-in-law of the poet Robert Burns.

## 29. 2wikimultihopqa_c16ac4b4088311ebbd6dac1f6bf848b6

原位置：`train` 第 89 题 · 全局第 89 题 · `sample_id: 2wikimultihopqa_c16ac4b4088311ebbd6dac1f6bf848b6`

Question: Which film has the director who died first, Brewster Mccloud or The Crimson Curtain (1953 Film)?

Note:

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | director of Brewster Mccloud | False | () |
| u2 | death date of {u1} | False | ('u1',) |
| u3 | director of The Crimson Curtain (1953 Film) | False | () |
| u4 | death date of {u3} | False | ('u3',) |
| u5 | which film's director died first | True | ('u2', 'u4') |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of Brewster McCloud | False | [] | Robert Altman | [['d9s0']] |
| u2 | date of death of {u1} | False | ['u1'] | November 20, 2006 | [['d7s0']] |
| u3 | director of The Crimson Curtain (1953 film) | False | [] | Alexandre Astruc | [['d6s0']] |
| u4 | date of death of {u3} | False | ['u3'] | 19 May 2016 | [['d2s0']] |
| u5 | which of the two films has the director who died first | True | ['u2', 'u4'] | Brewster McCloud | [[]] |

### Source documents (reference only)

**d1: Ben Palmer**

- [d1s0] Ben Palmer is a British film and television director who is known for being the director of" Bo' Selecta" and" The Inbetweeners".

**d2: Alexandre Astruc**

- [d2s0] Alexandre Astruc( 13 July 1923 – 19 May 2016) was a French film critic and film director.

**d3: Katutu, the Blind**

- [d3s0] Katutu, the Blind is a 1953 film.

**d4: The Crimson Stain Mystery**

- [d4s0] The Crimson Stain Mystery is a 1916 American horror film serial directed by T. Hayes Hunter.
- [d4s1] " The Crimson Stain Mystery" was poorly received upon release.

**d5: Geoffrey Hoppe**

- [d5s0] Geoffrey Hoppe( born Geoffrey Alan Hoppe on August 26, 1955, in Appleton, Wisconsin United States) is the founder and CEO of the Crimson Circle Energy Company, Inc.
- [d5s1] Hoppe claims that in 1997 on an airplane flight a non-physical entity he calls" Tobias of the Crimson Council" presented himself and began conversing with him.
- [d5s2] Hoppe contends that since then he has been able to channel Tobias, as well as the ascended masters Adamus Saint- Germain and Kuthumi.
- [d5s3] He claims to do so by going through the process of making his consciousness and physical body available and allowing Tobias, Saint- Germain or Kuthumi to speak through him.
- [d5s4] In 1999 Hoppe, together with his wife and partner Linda Benyo, founded the Crimson Circle as a means to bring Tobias ’ messages to a wider audience.
- [d5s5] In 2006 the Crimson Circle was incorporated as the Crimson Circle Energy Company, Inc., based in Incline Village, Nevada USA.

**d6: The Crimson Curtain (1953 film)**

- [d6s0] The Crimson Curtain is a 1953 French short film directed by Alexandre Astruc.
- [d6s1] It was screened at the 1952 Cannes Film Festival, but not entered into the competition.

**d7: Robert Altman**

- [d7s0] Robert Bernard Altman (February 20, 1925 – November 20, 2006) was an American film director, screenwriter, and producer.
- [d7s1] A five-time nominee of the Academy Award for Best Director and an enduring figure from the New Hollywood era, Altman was considered a "maverick" in making films with a highly naturalistic but stylized and satirical aesthetic, unlike most Hollywood films.
- [d7s2] He is consistently ranked as one of the greatest and most influential filmmakers in American cinema.
- [d7s3] His style of filmmaking covered many genres, but usually with a "subversive" twist which typically relied on satire and humor to express his personal views.
- [d7s4] Altman developed a reputation for being "anti-Hollywood" and non-conformist in both his themes and directing style.
- [d7s5] However, actors especially enjoyed working under his direction because he encouraged them to improvise, thereby inspiring their own creativity.
- [d7s6] He preferred large ensemble casts for his films, and developed a multitrack recording technique which produced overlapping dialogue from multiple actors.
- [d7s7] This produced a more natural, more dynamic, and more complex experience for the viewer.
- [d7s8] He also used highly mobile camera work and zoom lenses to enhance the activity taking place on the screen.
- [d7s9] Critic Pauline Kael, writing about his directing style, said that Altman could "make film fireworks out of next to nothing."
- [d7s10] In 2006, the Academy of Motion Picture Arts and Sciences recognized Altman's body of work with an Academy Honorary Award.
- [d7s11] He never won a competitive Oscar despite seven nominations.
- [d7s12] His films "MASH" (1970), "McCabe & Mrs. Miller" (1971), and "Nashville" (1975) have been selected for the United States National Film Registry.
- [d7s13] Altman is one of the few filmmakers whose films have won the Golden Bear at Berlin, the Golden Lion at Venice, and the Golden Palm at Cannes.

**d8: The Crimson Circle (1922 film)**

- [d8s0] The Crimson Circle is a 1922 British silent crime film directed by George Ridgwell and starring Clifton Boyne, Fred Groves and Robert English.
- [d8s1] The film was an adaptation of the novel" The Crimson Circle" by Edgar Wallace.
- [d8s2] A German/ UK version of" The Crimson Circle Die rote Kreis"( 1929), was filmed in both a silent and Phonofilm sound- on- film version.

**d9: Brewster McCloud**

- [d9s0] Brewster McCloud is a 1970 American experimental comedy film directed by Robert Altman.
- [d9s1] It concerns a young recluse( Bud Cort, as the title character) who lives in a fallout shelter of the Houston Astrodome, where he is building a pair of wings so he can fly.
- [d9s2] He is helped by his comely and enigmatic" fairy godmother", played by Sally Kellerman, as he becomes a suspect in a series of murders.
- [d9s3] The film was shot on location in Houston, Texas.
- [d9s4] During the opening credits, shots of the downtown Houston skyline( with One Shell Plaza under construction) zoom toward the Houston Astrodome and Astrohall, with the emerging Texas Medical Center in the background.
- [d9s5] It was the first film shot inside the Astrodome.

**d10: Crimson Curtain (1952 film)**

- [d10s0] Crimson Curtain
- [d10s1] ( French: Le rideau rouge) is a 1952 French drama film directed by André Barsacq and starring Michel Simon, Pierre Brasseur and Jean Brochard.

## 30. 2wikimultihopqa_c1c9fc7a0baf11ebab90acde48001122

原位置：`train` 第 90 题 · 全局第 90 题 · `sample_id: 2wikimultihopqa_c1c9fc7a0baf11ebab90acde48001122`

Question: Who is the father-in-law of Aishwarya R. Dhanush?

Note:

Type: bridge · fallback: False · SFT snapshots: 9

### New decomposer units

| ID | Description | Necessary | Depends on |
|---|---|---|---|
| u1 | husband of Aishwarya R. Dhanush | False | () |
| u2 | father of {u1}, Aishwarya R. Dhanush's father-in-law | True | ('u1',) |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | spouse of Aishwarya R. Dhanush | False | [] | Dhanush | [['d4s2']] |
| u2 | father of {u1}, Aishwarya R. Dhanush's father-in-law | True | ['u1'] | Kasthuri Raja | [['d1s1']] |

### Source documents (reference only)

**d1: Dhanush**

- [d1s0] Venkatesh Prabhu (born 28 July 1983), better known by his stage name Dhanush, is an Indian film actor, producer, director, writer, lyricist, screenwriter and playback singer who predominantly works in Tamil cinema.
- [d1s1] Dhanush's first film was "Thulluvadho Ilamai", a 2002 coming-of-age film directed by his father, Kasthuri Raja.
- [d1s2] Over the last 15 years, Dhanush has starred in over 25 films.
- [d1s3] Dhanush won the Best Actor award at the 58th National Film Awards for his performance in "Aadukalam" (2010).
- [d1s4] In 2011, Dhanush's popular song "Why this Kolaveri Di" became the first Indian music video to cross 100 million views on YouTube.
- [d1s5] Dhanush produces films through his production company, Wunderbar Films.
- [d1s6] In addition to his best actor award, he has a national award for a movie he produced, "Visaranai".
- [d1s7] He has also won seven Filmfare Awards.

**d2: Peter Burroughs**

- [d2s0] Peter Burroughs( born 27 January 1947) is a British television and film actor, the director of Willow Management.
- [d2s1] He is the father- in- law of actor and TV presenter Warwick Davis.

**d3: John Vernou Bouvier III**

- [d3s0] John Vernou" Black Jack" Bouvier III( May 19, 1891 – August 3, 1957) was an American Wall Street stockbroker and socialite.
- [d3s1] He was the father of First Lady Jacqueline Kennedy Onassis and of socialite Lee Radziwill, and was the father- in- law of John F. Kennedy.

**d4: Aishwarya R. Dhanush**

- [d4s0] Aishwarya Rajinikanth Dhanush (born 1 January 1982) is an Indian film director.
- [d4s1] She is the elder daughter of actor Rajinikanth.
- [d4s2] She made her feature film debut with "3" (2012) starring her husband Dhanush.
- [d4s3] She has occasionally done playback singing.
- [d4s4] In August 2016, Aishwarya was selected as India's goodwill ambassador for the UN Women organization.

**d5: Harry Smith (athlete)**

- [d5s0] Harry James Smith( July 30, 1888 – November 20, 1962) was an American long- distance runner.
- [d5s1] He was most notable for competing in the 1912 Olympics in Stockholm.
- [d5s2] He was also the father of Hart wrestling family matriarch Helen Hart and the father- in- law of Stu Hart.

**d6: Barthold A. Butenschøn Sr.**

- [d6s0] Hans Barthold Andresen Butenschøn( 27 December 1877 – 28 November 1971) was a Norwegian businessperson.
- [d6s1] He was born in Kristiania as a son of Nils August Andresen Butenschøn and Hanna Butenschøn, and grandson of Nicolay Andresen.
- [d6s2] Together with Mabel Anette Plahte( 1877 – 1973, a daughter of Frithjof M. Plahte) he had the son Hans Barthold Andresen Butenschøn Jr. and was through him the father- in- law of Ragnhild Butenschøn and grandfather of Peter Butenschøn.
- [d6s3] Through his daughter Marie Claudine he was the father- in- law of Joakim Lehmkuhl, through his daughter Mabel Anette he was the father- in- law of Harald Astrup( a son of Sigurd Astrup) and through his daughter Nini Augusta he was the father- in- law of Ernst Torp.
- [d6s4] He took commerce school and agricultural school.
- [d6s5] He was hired in the family company N. A. Andresen& Co, and became a co-owner in 1910.
- [d6s6] He eventually became chief executive officer.
- [d6s7] The bank changed its name to Andresens Bank in 1913 and merged with Bergens Kreditbank in 1920.
- [d6s8] The merger was dissolved later in the 1920s.
- [d6s9] He was also a landowner, owning Nedre Skøyen farm and a lot of land in Enebakk.
- [d6s10] He chaired the board of Nydalens Compagnie from 1926, having not been a board member before that.
- [d6s11] He also chaired the supervisory council of Forsikringsselskapet Viking and Nedre Glommen salgsforening, and was a supervisory council member of Filharmonisk Selskap.
- [d6s12] He was a member of the gentlemen's club SK Fram since 1890, and was proclaimed a lifetime member in 1964.
- [d6s13] He was buried in Enebakk.

**d7: Ogawa Mataji**

- [d7s0] Viscount was a general in the early Imperial Japanese Army.
- [d7s1] He was also the father- in- law of Field Marshal Gen Sugiyama.

**d8: Ludwig von Westphalen**

- [d8s0] Johann Ludwig von Westphalen( 11 July 1770 – 3 March 1842) was a liberal Prussian civil servant and the father- in- law of Karl Marx.

**d9: John Adams (merchant)**

- [d9s0] John Adams( 1672 or 1673 – 1745) was an American- born Canadian merchant and member of the Nova Scotia Council.
- [d9s1] He was the father- in- law of Henry Newton( politician).

**d10: James Armour (Master mason)**

- [d10s0] James Armour (15 January 1730 – 20 September 1798) was a master mason and father of Jean Armour, and therefore the father-in-law of the poet Robert Burns.
