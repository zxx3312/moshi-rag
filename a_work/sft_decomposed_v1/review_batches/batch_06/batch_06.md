# batch_06：人工审查（30 题）

全局题号 151–180；train 30 题 / dev 0 题。原训练/验证归属保持不变。

[返回分配索引](../README.md) · [完整对比报告](../../comparison_human.md)

**原则：新旧单元都合理时保留拆题器拆法，人工监督向新单元对齐。** 
审查人：________　完成日期：________

本批已依据人工 Note 调整；原始拆题保存在 JSON 的 `raw_decomposition`。下方 Adjusted units 为当前标注，旧 gold 仅供参照。标注已更新；逐时刻 SFT 快照尚未重建。

## 1. hotpotqa_5a7f66cb55429969796c1a32

原位置：`train` 第 151 题 · 全局第 151 题 · `sample_id: hotpotqa_5a7f66cb55429969796c1a32`

Question: Between Cranium and Auf Achse, which game had more people involved in creating?

Note: 题型应该是comparison，保留三单元，跟拆词器结构一致，证据跟旧的一样

Type: comparison · fallback: False · SFT snapshots: 7

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。 题型修正为 comparison。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | number of people involved in creating Cranium | False | [] | 2 | [["d7s0"], ["d4s1", "d4s2"]] | context |
| u2 | number of people involved in creating Auf Achse | False | [] | 1 | [["d10s0"]] | context |
| u3 | which game had more people involved in creating | True | ["u1", "u2"] | Cranium | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | number of creator/designer people explicitly named for the game Cranium | False | [] | 2 | [['d7s0'], ['d4s1', 'd4s2']] |
| u2 | number of creator/designer people explicitly named for the game Auf Achse | False | [] | 1 | [['d10s0']] |
| u3 | which of Cranium and Auf Achse has more creator/designer people explicitly named by the documents | True | ['u1', 'u2'] | Cranium | [[]] |

### Source documents (reference only)

**d1: Zigity**

- [d1s0] Zigity is a card game from the makers of Cranium that combines the play of games such as "Uno" with typical Cranium elements.

**d2: Garish**

- [d2s0] garish, formed in February 1997, is an Austrian alternative rock band.
- [d2s1]  After having asserted themselves in the alternative scene inside and outside Austria's borders with their first two records "amaurose pur."
- [d2s2]  and "wo die nacht erzaehlt vom tag", their third album "Absender auf Achse" gained favorable press and fan reaction.
- [d2s3]  Despite German lyrics, it is said that their emotional style of music is their "real language".

**d3: Suicide mission**

- [d3s0] A suicide mission is a task which is so dangerous for the people involved that they are not expected to survive.
- [d3s1]  The term is sometimes extended to include suicide attacks such as kamikaze and suicide bombings, where the people involved actively commit suicide during execution of the mission.
- [d3s2]  The risks involved with suicide missions are not always apparent to those participating in them or to those who plan them.
- [d3s3]  However, for an action to be considered a suicide mission someone involved must be aware of the risks.
- [d3s4]  A mission that goes horribly wrong is not a suicide mission.
- [d3s5]  An individual or group taking part in a mission may perceive the risks involved to be far greater than what they believe to be acceptable, while those planning or commanding the mission may think otherwise.
- [d3s6]  These situations can often lead to refusals to participate in missions on the basis that they are "suicide missions".
- [d3s7]  Similarly, planners or commanders may be well aware of the risks involved with missions while those participating in them may not.

**d4: Cranium, Inc.**

- [d4s0] Cranium, Inc. was a toy and board game developer.
- [d4s1]  The company was founded in 1998 by two former Microsoft executives, Richard Tait and Whit Alexander.
- [d4s2]  They co-developed the "Cranium" board game.

**d5: Visual guide**

- [d5s0] When applied to building block a website or similar work product, a Visual Guide can be an intermediate step toward the end goal of a complete website.
- [d5s1]  By creating a visual guide along the way, the designer or developer can get input from the other people involved in the website such as the customer, their manager, and other members of the team.
- [d5s2]  The visual guide will provide a view to the customer of what their website or project will end up looking like.
- [d5s3]  It ensures that they are kept up to date on any developments and changes made to the structure or visuals.
- [d5s4]  Visual guides also allow you to define the information hierarchy of the design.

**d6: Body Positive Movement**

- [d6s0] The Body Positive Movement is a movement that encourages people to adopt more forgiving and affirming attitudes towards their bodies, with the goal of improving overall health and well-being.
- [d6s1]  Whether people are nurturing their bodies and maintaining their weight, or finding a place in life where they are comfortable through working out, or changing their lifestyles to find a better attitude, the body positive movement focuses on building self-esteem through improving one's self-image.
- [d6s2]  The body positive movement targets all body shapes and sizes.
- [d6s3]  The movement is not only about working out and striving to be positive and creating a better lifestyle for oneself, but deals with health as well.
- [d6s4]  A debate within the movement surrounds the question of whether social media sites, including Instagram, Facebook, and blogs, are helping or harming people's perceptions of their bodies.
- [d6s5]  People involved with this movement challenge themselves daily to learn how to grow and love themselves to the fullest.

**d7: Cranium (board game)**

- [d7s0] Cranium is a party game created by Whit Alexander and Richard Tait in 1998, after Richard spent a weekend playing games with another family and recognized the need for a game involving a variety of skills.
- [d7s1]  He left his job at Microsoft, convincing his friend and co-worker Whit Alexander to join him in the creation of "Cranium".
- [d7s2]  "Cranium", manufactured by Hasbro subsidiary Cranium, Inc., is billed as "The Game for Your Whole Brain".
- [d7s3]  Unlike many other party games, "Cranium" includes a wide variety of activities.
- [d7s4]  Giorgio Davanzo handles packaging and branding for the game, and the artwork is done by Gary Baseman, creator of the animated television series "Teacher's Pet".

**d8: Auf Achse (TV series)**

- [d8s0] Auf Achse (a German expression meaning "on the road", the literal translation would be "on the axle") was a German television series on the ARD channel.
- [d8s1]  The series ran from 1977 until 1996 and 86 episodes were produced altogether.

**d9: Cranium Whoonu**

- [d9s0] Cranium Whoonu is a party game manufactured by Cranium, Inc. Whoonu is billed as "the fun-filled 'what's your favorite thing?'
- [d9s1]  game".

**d10: Auf Achse**

- [d10s0] Auf Achse (literally "on the axle"; figuratively "on the road") is a logistics-themed board game designed by Wolfgang Kramer and published in 1987 by FX Schmid.
- [d10s1]  The game won the Spiel des Jahres award.
- [d10s2]  In 1992, a junior edition was released; and in 1994 a rummy-like card game spinoff was released.
- [d10s3]  In 2007 a revised edition was published by Schmidt Spiele.

## 2. hotpotqa_5a7fc61155429969796c1b57

原位置：`train` 第 152 题 · 全局第 152 题 · `sample_id: hotpotqa_5a7fc61155429969796c1b57`

Question: The catalyst for the Peekskill riots was a concert annouced by a black singer that played football at what college?

Note: 跟新版本对齐

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留两单元及当前修正描述：Paul Robeson 是已宣布音乐会的演出者；不要求证明他本人发布公告。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | black singer whose announced concert was the catalyst for the Peekskill riots | False | [] | Paul Robeson | [["d2s1"]] | context |
| u2 | college where {u1} played football | True | ["u1"] | Rutgers College | [["d10s1"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | black singer whose announced concert was the catalyst for the Peekskill riots | False | [] | Paul Robeson | [['d2s1']] |
| u2 | college at which {u1} played football | True | ['u1'] | Rutgers College | [['d10s1']] |

### Source documents (reference only)

**d1: Vic Hanson**

- [d1s0] Victor A. Hanson (July 30, 1903 – April 10, 1982) was an American football player and coach, basketball player, and baseball player.
- [d1s1]  A three-sport college athlete, he played football, basketball, and baseball at Syracuse University in the 1920s, serving as team captain in all three sports.
- [d1s2]  The Watertown, New York native was named an Basketball All-American three times—in 1925, 1926, and 1927—by the Helms Athletic Foundation and was a consensus selection to the 1926 College Football All-America Team.
- [d1s3]  Following his college career he played briefly with the Cleveland Rosenblums in the American Basketball League and then formed a basketball team, the Syracuse All-Americans.
- [d1s4]  He was also signed by the New York Yankees of Major League Baseball upon graduation from Syracuse in 1927 and played one year in their farm system.
- [d1s5]  Hanson served as the head football coach at his alma mater from 1930 to 1936, compiling a record of 33–21–5.
- [d1s6]  He is only player inducted into both the Naismith Memorial Basketball Hall of Fame and the College Football Hall of Fame.

**d2: Peekskill riots**

- [d2s0] The Peekskill riots were anti-communist riots with anti-black and anti-Semitic undertones that took place at Cortlandt Manor, Westchester County, New York, in 1949.
- [d2s1]  The catalyst for the rioting was an announced concert by black singer Paul Robeson, who was well known for his strong pro-trade union stance, civil rights activism, communist affiliations, and anti-colonialism.
- [d2s2]  The concert, organized as a benefit for the Civil Rights Congress, was scheduled to take place on August 27 in Lakeland Acres, just north of Peekskill.

**d3: Floyd Gass**

- [d3s0] Floyd Gass (January 31, 1927 – March 3, 2006) was an American football and basketball player, coach, and college athletics administrator.
- [d3s1]  He served as the head football coach at Austin College from 1961 to 1968, having previously been offensive coordinator, and at Oklahoma State University–Stillwater from 1969 to 1971, compiling a career college football record of 56–46–2.
- [d3s2]  He was voted the Big Eight Conference Coach of the Year in 1969.
- [d3s3]  His record was 13–18–1 in his three seasons at Oklahoma State.
- [d3s4]  Gass was also the head basketball coach at Austin College from 1955 to 1962, tallying a mark of 71–80, and served as athletic director.
- [d3s5]  He was an alumnus of Oklahoma State, and played football and basketball while attending the university.
- [d3s6]  Gass was one of three head football coaches at Oklahoma State to have played for Oklahoma State, along with Jim Lookabaugh and current head coach Mike Gundy.
- [d3s7]  Gass served as athletics director at OSU from 1971 through 1978, when he left OSU to pursue other business opportunities.
- [d3s8]  Gass died on March 3, 2006, at the age of 79.

**d4: George Pyne II**

- [d4s0] George Francis Pyne, Jr. (October 17, 1909 – June 3, 1974) was an American football tackle who played one season with the Providence Steam Roller of the National Football League.
- [d4s1]  He played college football at the College of the Holy Cross and attended Milford High School in Milford, Massachusetts.
- [d4s2]  His son George Pyne III played in the AFL and his grandson Jim Pyne played in the NFL.
- [d4s3]  The Pynes were the first family to have three generations play professional football.
- [d4s4]  His grandson George played football at Brown University and is a businessman.

**d5: Harry W. Ewing**

- [d5s0] Harry Walter "Buck" Ewing (July 18, 1886 – March 11, 1962) was an American football player, coach of football, basketball and baseball, and college athletics administrator.
- [d5s1]  He was a 1909 graduate of University of Nebraska where he played football.
- [d5s2]  Ewing served as the head football coach at Morningside College (1911), South Dakota State College (1912–1917), Ohio Wesleyan University (1919–1921), Miami University (1922–1923), and Otterbein College (1935–1938, 1942–1945, 1951–1954), compiling a career college football record of 82–82–10.
- [d5s3]  He was also the head basketball coach at South Dakota State (1912–1913, 1914–1917), Ohio Wesleyan (1919–1920), Miami (1922–1924), and Otterbein (1942–1952), tallying a career college basketball mark of 117–111–1.

**d6: Tre' Johnson**

- [d6s0] Edward Stanton Johnson, III (born August 30, 1971 in Manhattan, New York) is a former American football Offensive tackle in the National Football League who played for the Washington Redskins and the Cleveland Browns.
- [d6s1]  He attended Peekskill High School, played college football at Temple University and was drafted in the second round of the 1994 NFL Draft.
- [d6s2]  He was selected to the 1999 Pro Bowl.

**d7: Adrien Robinson**

- [d7s0] Adrien Robinson (born September 23, 1988) is an American football tight end who is currently a free agent He was drafted in the 4th round (127th overall) in the 2012 NFL Draft by the New York Giants.
- [d7s1]  Born in Indianapolis, Indiana, Robinson played football at Warren Central High School, winning the state championship in all of his four seasons, and played football in college for the Cincinnati Bearcats from 2008 to 2011.

**d8: Mel Taube**

- [d8s0] Melvin Henry "Mel" Taube (December 20, 1904 – June 15, 1979) was an American football, basketball, and baseball player, coach, and college athletics administrator.
- [d8s1]  He served as the head football coach at Massachusetts State College, from 1931 to 1935 and at Carleton College from 1960 to 1969, compiling a career college football record of 62–58–5.
- [d8s2]  Taube was also the head basketball coach at Massachusetts State College (1933–1936), Purdue University (1945–1950), and Carleton (1950–1960), amassing a career college basketball mark of 201–142 and winning four Midwest Conference championships.
- [d8s3]  He was the head baseball coach at Massachusetts State (1932–1935), Purdue (1947–1950), and Carleton (1951–1970), tallying a career college baseball record of 93–74–3.
- [d8s4]  A three-sport letterman, Taube played football, basketball, and baseball at Purdue.

**d9: James C. Donnelly**

- [d9s0] James Corcoran Donnelly (December 9, 1881 – March 24, 1952) was an American football player and coach in the early 1900s.
- [d9s1]  He played football at Worcester's Classical High School then went on to Dartmouth where he played football.
- [d9s2]  After graduation in 1905 he went to Harvard Law School and was admitted to the bar in 1908.
- [d9s3]  He practiced law and served as head football coach at Worcester Polytechnic Institute (1909, 1911, 1915), Howard College in Birmingham, Alabama (1910), and Miami University in Oxford, Ohio (1912–1914), compiling a career college football record of 22–32–4.
- [d9s4]  In 1931, he was appointed a Superior Court judge.
- [d9s5]  His younger brother, Charley Donnelly also coached football at the high school and college level.
- [d9s6]  His youngest brother, Ralph E. Donnelly, was also a standout football player and war hero.

**d10: Paul Robeson**

- [d10s0] Paul Leroy Robeson (pronounced ; April 9, 1898 – January 23, 1976) was an American bass singer and actor who became involved with the Civil Rights Movement.
- [d10s1]  At Rutgers College, he was an outstanding American football player, and then had an international career in singing, with a distinctive, powerful, deep bass voice, as well as acting in theater and movies.
- [d10s2]  He became politically involved in response to the Spanish Civil War, fascism, and social injustices.
- [d10s3]  His advocacy of anti-imperialism, affiliation with communism, and criticism of the United States government caused him to be blacklisted during the McCarthy era.

## 3. hotpotqa_5a8009885542992e7d278deb

原位置：`train` 第 153 题 · 全局第 153 题 · `sample_id: hotpotqa_5a8009885542992e7d278deb`

Question: Who is best known as the vocalist of indie rock band Florence and the Machine, Florence Welch or Floor Jansen ?

Note: 

Type: comparison · fallback: False · SFT snapshots: 6

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | whether Florence Welch is best known as the vocalist of Florence and the Machine | False | [] | yes | [["d6s0"], ["d2s0", "d2s1"], ["d8s0", "d8s1"], ["d9s0", "d9s1"]] | context |
| u2 | whether Floor Jansen is best known as the vocalist of Florence and the Machine | False | [] | no | [] | no_direct_support |
| u3 | who is best known as the vocalist of Florence and the Machine | True | ["u1", "u2"] | Florence Welch | [[]] | question_presupposition |

- u2：无直接支持集合；不能仅由 expected_answer 将本单元标为 SUPPORTED。候选题结论可按独立的 presupposition_sets 路径判断。

- u3：`by_presupposition=true`，预设路径 `[["d6s0"], ["d2s0", "d2s1"], ["d8s0", "d8s1"], ["d9s0", "d9s1"]]`；不是直接证据。

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Florence Welch is the vocalist of indie rock band Florence and the Machine | False | [] | yes | [['d6s0'], ['d2s0', 'd2s1'], ['d8s0', 'd8s1'], ['d9s0', 'd9s1']] |
| u2 | whether Floor Jansen is the vocalist of indie rock band Florence and the Machine | False | [] | no | [] |
| u3 | which of Florence Welch and Floor Jansen is best known as the vocalist of indie rock band Florence and the Machine | True | ['u1', 'u2'] | Florence Welch | [[]] |

### Source documents (reference only)

**d1: Wish That You Were Here**

- [d1s0] "Wish That You Were Here" is a song by the English indie rock band Florence and the Machine, written by Florence Welch, Andrew Wyatt, and Emilie Haynie, and was released on Island Records on 26 August 2016.
- [d1s1]  The song was made available via digital download, and is featured on the soundtrack of the film "Miss Peregrine's Home for Peculiar Children" which was directed by Tim Burton.
- [d1s2]  Welch — a long-time fan of Burton's work — had expressed interest in collaborating with him long before the recording of "Wish That You Were Here" as they shared similar artistic themes.
- [d1s3]  Upon release, the composition was positively received by music critics and reached number 128 on the UK Singles Chart.

**d2: What the Water Gave Me (song)**

- [d2s0] "What the Water Gave Me" is a song by English indie rock band Florence and the Machine from their second studio album "Ceremonials" (2011).
- [d2s1]  The song was written by lead singer Florence Welch and Francis "Eg" White, and produced by Paul Epworth.
- [d2s2]  It was released on 23 August 2011 as the first promotional single from "Ceremonials".
- [d2s3]  After the band performed the song in Berkeley, California on 12 June 2011, the studio version premiered on Florence and the Machine's official website.
- [d2s4]  Welch decided to name the song "What the Water Gave Me" after seeing a Frida Kahlo painting of the same name.
- [d2s5]  During an interview, she confirmed that the song was inspired by English writer Virginia Woolf.

**d3: No Light, No Light**

- [d3s0] No Light, No Light is a song by English indie rock band Florence and the Machine from their second studio album, "Ceremonials" (2011).
- [d3s1]  The song was written by band members Florence Welch and Isabella Summers while the production was handled by Paul Epworth.
- [d3s2]  Island Records released the song as the second single from the album on 16 January 2012.
- [d3s3]  The song was the first one written for the album in the band's tour bus in Amsterdam.
- [d3s4]  Lyrically, in the song, Welch is expressing frustration about the state of her fragile relationship and she further tries to keep it together.
- [d3s5]  "No Light, No Light" received positive reviews by music critics who generally praised Welch's vocals and the drum-led instrumentation.
- [d3s6]  It was also placed on several critics' year-end lists of best singles.
- [d3s7]  The song peaked at number fifty on the UK Singles Chart, the Irish Singles Chart and number thirty nine on the US "Billboard" Alternative Songs chart.

**d4: Floor Jansen**

- [d4s0] Floor Jansen (] ; born 21 February 1981 in Goirle) is a Dutch singer, songwriter, and vocal coach.
- [d4s1]  She is the lead vocalist of Finnish symphonic metal band Nightwish.

**d5: Shake It Out**

- [d5s0] "Shake It Out" is a song by English indie rock band Florence and the Machine, released as the first official single from their second studio album, "Ceremonials" (2011).
- [d5s1]  It was written by Florence Welch and Paul Epworth, while production was handled by Epworth.
- [d5s2]  The song was digitally released in Australia on 14 September 2011, and it was available in the United States on 19 October.
- [d5s3]  It had its radio debut on XFM on 14 September 2011 in the United Kingdom.
- [d5s4]  Welch revealed that the song was written within an hour and according to her it talked about shaking the regrets and the things that were haunting her.

**d6: Florence Welch**

- [d6s0] Florence Leontine Mary Welch (born 28 August 1986) is an English musician, singer and songwriter, best known as the vocalist of indie rock band Florence and the Machine.

**d7: Lungs (album)**

- [d7s0] Lungs is the debut studio album by English indie rock band Florence and the Machine, released on 3 July 2009 on Island Records.
- [d7s1]  Frontwoman Florence Welch experimented with and honed the album's sound with bandmate Isabella Summers, while also collaborating with five record producers including James Ford, Paul Epworth, Steve Mackey.
- [d7s2]  The music on "Lungs" established Florence and the Machine as an internationally successful rock act, and also featured the group's successful mix of string arrangements centered around Welch's vocal prowess.

**d8: Spectrum (Say My Name)**

- [d8s0] "Spectrum" is a song by English indie rock band Florence and the Machine from their second studio album "Ceremonials" (2011).
- [d8s1]  It was written by lead singer Florence Welch and Paul Epworth with production being handled by Epworth.
- [d8s2]  The band premiered the song during a concert at Brooklyn's Creators Project on 15 October 2011, prior to the release of the album.
- [d8s3]  The album version of "Spectrum" is a downtempo orchestral pop, R&B, krautrock and disco song.
- [d8s4]  The accompanying music video for the song premiered on 30 May 2012.
- [d8s5]  It was directed by David LaChapelle and John Byrne.

**d9: Ceremonials Tour**

- [d9s0] The Ceremonials Tour was the second concert tour by English indie rock band Florence and the Machine.
- [d9s1]  The tour included performances at Music festivals because it is lead singer Florence Welch's favourite way to perform live.
- [d9s2]  Welch had originally planned to spend over one year touring for "Ceremonials" (their previous tour lasted almost three and a half years) before announcing that the December 2012 dates would be the final performances of the tour.
- [d9s3]  On 25 February 2013 it was announced that Florence and the Machine would be playing at the Coke Live Music Festival in Poland on 10 August 2013, and on 26 March 2013 it was announced that the band would be playing at Chime for Change's "The Sound of Change Live" concert at London's Twickenham Stadium alongside Beyoncé, Ellie Goulding and Haim, amongst others.

**d10: What Kind of Man (Florence and the Machine song)**

- [d10s0] "What Kind of Man" is a song by English indie rock band Florence and the Machine from their third studio album, "How Big, How Blue, How Beautiful" (2015).
- [d10s1]  It was written by Florence Welch, Kid Harpoon and John Hill, produced by Markus Dravs and co-produced by Hill.
- [d10s2]  The song was released on 12 February 2015 as the album's lead single.
- [d10s3]  "What Kind of Man" received Grammy Award nominations for Best Rock Performance and Best Rock Song.

## 4. hotpotqa_5a809152554299485f598658

原位置：`train` 第 154 题 · 全局第 154 题 · `sample_id: hotpotqa_5a809152554299485f598658`

Question: What is  Lauri Ylönen and Kim Jong-hyun's main occupation?

Note: 如果新拆分的两个necessary单元足以得到答案，就取消u3，之后对于这种类型的题目，也这样处理

Type: multipart · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | main occupation of Lauri Ylönen | True | [] | singer-songwriter | [["d7s0"], ["d3s1"]] | context |
| u2 | main occupation of Kim Jong-hyun | True | [] | singer-songwriter | [["d5s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | main occupation of Lauri Ylönen | False | [] | singer-songwriter | [['d7s0'], ['d3s1']] |
| u2 | main occupation of Kim Jong-hyun | False | [] | singer-songwriter | [['d5s0']] |
| u3 | main occupation shared by Lauri Ylönen and Kim Jong-hyun | True | ['u1', 'u2'] | singer-songwriter | [[]] |

### Source documents (reference only)

**d1: Heavy (Lauri Ylönen song)**

- [d1s0] "Heavy" is the first single of Lauri Ylönen from his first solo album "New World".
- [d1s1]  The world premiere of the song was on 26 February 2011 with a digital release on 25 February.

**d2: Keep Your Heart Broken**

- [d2s0] "Keep Your Heart Broken" is a song by the Finnish alternative rock band The Rasmus, and the ninth track of their 2005 album "Hide from the Sun".
- [d2s1]  It was written by lead-singer Lauri Ylönen.

**d3: The Rasmus**

- [d3s0] The Rasmus are a Finnish rock band that formed in 1994 in Helsinki while the band members were still in upper comprehensive school.
- [d3s1]  The original band members were Lauri Ylönen (lead singer/songwriter), Eero Heinonen (bass), Pauli Rantasalmi (guitar) and Jarno Lahti (drums).
- [d3s2]  Jarno Lahti left the year after and was replaced by Janne Heiskanen in 1995.
- [d3s3]  Heiskanen quit the band in 1998 and was soon replaced by Aki Hakala.
- [d3s4]  The Rasmus has sold 4 million albums worldwide, 310,000 copies in their native Finland alone.
- [d3s5]  They have won numerous awards, both domestic and international.

**d4: New World (Lauri Ylönen album)**

- [d4s0] New World is the first solo album from Lauri Ylönen, lead singer of Finnish band The Rasmus.
- [d4s1]  The album was released on 30 March 2011.
- [d4s2]  This album contains songs by Lauri that didn't fit The Rasmus' style, and decided to be released as a solo album.
- [d4s3]  The first single released was "Heavy" and the second was "In the City".

**d5: Kim Jong-hyun (singer)**

- [d5s0] Kim Jong-hyun (born April 8, 1990), better known by the mononym Jonghyun, is a South Korean singer-songwriter, and radio host.
- [d5s1]  He is a vocalist of the South Korean boy group Shinee, and has further participated in S.M. Entertainment's project group S.M.
- [d5s2]  The Ballad.
- [d5s3]  Jonghyun debuted as a solo artist on January 12, 2015, with his first EP, titled "Base".
- [d5s4]  In the same year, on September 17, Jonghyun released a compilation album, "Story Op.1".
- [d5s5]  On May 24, 2016, Jonghyun released his first studio album, "She Is", followed by his second compilation album, "Story Op.2" on April 24, 2017.

**d6: Kim Jong-hyun**

- [d6s0] Kim Jong-hyun () is a Korean name consisting of the family name Kim and the given name Jong-hyun, and may also refer to:

**d7: Lauri Ylönen**

- [d7s0] Lauri Ylönen (born 23 April 1979) is a Finnish singer-songwriter, best known as the frontman of the Finnish alternative rock band The Rasmus.

**d8: Ghost of Love (The Rasmus song)**

- [d8s0] "Ghost of Love" is a radio single released exclusively in Finland by Finnish alternative rock band The Rasmus, and the third track on their 2008 studio album "Black Roses".
- [d8s1]  It was written by lead-singer Lauri Ylönen.

**d9: Bittersweet (Apocalyptica song)**

- [d9s0] "Bittersweet" is a single by the cello rock band Apocalyptica in collaboration with Ville Valo (of HIM) and Lauri Ylönen (of The Rasmus).
- [d9s1]  The music is by Apocalyptica, the lyrics by Ville Valo and the vocals by Ville Valo and Lauri Ylönen.
- [d9s2]  The song is written for four cellos (quartet) and voice, but there are versions for just the cello quartet.
- [d9s3]  The lyrics are about a love triangle, in which a woman loves a man, who does not love her back, and another man which is in love with the woman, while she does not love him back.

**d10: Sail Away (The Rasmus song)**

- [d10s0] "Sail Away" is a song by the Finnish rock band The Rasmus, originally released on the band's sixth studio album "Hide from the Sun" on September 2, 2005.
- [d10s1]  The song was written by the lead singer Lauri Ylönen.
- [d10s2]  Sail away was 2nd on the United States singles list in 2005.

## 5. hotpotqa_5a825f5955429954d2e2eb1c

原位置：`train` 第 155 题 · 全局第 155 题 · `sample_id: hotpotqa_5a825f5955429954d2e2eb1c`

Question: Do theflowering plants Hypoxis and Monarda belong to the same family?

Note: 

Type: comparison · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | family of Hypoxis | False | [] | Hypoxidaceae | [["d3s0"], ["d3s5"]] | context |
| u2 | family of Monarda | False | [] | Lamiaceae | [["d10s0"]] | context |
| u3 | whether Hypoxis and Monarda belong to the same family | True | ["u1", "u2"] | no | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | family of the genus Hypoxis | False | [] | Hypoxidaceae | [['d3s0'], ['d3s5']] |
| u2 | family of the genus Monarda | False | [] | Lamiaceae | [['d10s0']] |
| u3 | whether Hypoxis and Monarda belong to the same family | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Trilliaceae**

- [d1s0] Trilliaceae is the botanical name of a family of flowering plants.
- [d1s1]  The family has been recognised as distinct since 1846 when it was recognized; this table  for a summarizes the placement of these taxa.
- [d1s2]  The family has been recognized by taxonomists such as Takhtajan, Dahlgren, Thorne, and Watson & Dallwitz; other taxonomists have considered these plants to belong to the family Liliaceae.
- [d1s3]  The APG II system, of 2003 (unchanged from the APG system, of 1998), does not recognize such a family either and assigns the plants involved to family Melanthiaceae.
- [d1s4]  One problem with this recognition is the lack of morphological synapomorphies for the family Melanthiaceae; this chart  provides a summary of the characters in each of the major groups.

**d2: Genoplesium**

- [d2s0] Genoplesium commonly known as midge orchids, is a genus of about 50 species of flowering plants in the orchid family, Orchidaceae and is found in Australia, New Zealand and New Caledonia.
- [d2s1]  Midge orchids are terrestrial herbs with a single leaf at the base of the plant.
- [d2s2]  They are similar to orchids in the genus "Prasophyllum" in that plants without flowers have a hollow, onion-like leaf.
- [d2s3]  The flowers are small but often scented and attractive to their insect pollinators.
- [d2s4]  There is disagreement about which species belong to this genus and some taxonomists suggest that most belong in the genus "Corunastylis".

**d3: Hypoxis**

- [d3s0] Hypoxis is a genus of flowering plants belonging to the family Hypoxidaceae.
- [d3s1]  The genus has an "almost cosmopolitan" distribution, occurring in Africa, the Americas, Asia, and Australia.
- [d3s2]  Europe lacks native species.
- [d3s3]  Most species are in the Southern Hemisphere, especially in southern Africa.
- [d3s4]  Common names for the genus include star-grass, star lily, yellow stars, African potato, and stars.
- [d3s5]  The genus is the largest of the Hypoxidaceae family and has its centre of variation in South Africa, where it occurs in open undisturbed grasslands.
- [d3s6]  The name "Hypoxis" was taken over by Linnaeus in 1759 from a name coined by Paul Reneaulme in 1611 for a superficially similar species of "Gagea" and meaning "a little sour", referring to the taste of that plant's leaves.

**d4: Cassava brown streak virus disease**

- [d4s0] Cassava brown streak virus disease (CBSD) is a damaging disease of cassava plants, and is especially troublesome in East Africa.
- [d4s1]  It was first identified in 1936 in Tanzania, and has spread to other coastal areas of East Africa, from Kenya to Mozambique.
- [d4s2]  Recently, it was found that two distinct viruses are responsible for the disease: cassava brown streak virus (CBSV) and Ugandan cassava brown streak virus (UCBSV).
- [d4s3]  Both have (+)ss RNA genomes, belong to the genus "Ipomovirus" in the family "Potyviridae," and produce generally similar symptoms in infected plants.
- [d4s4]  Root rot renders the cassava tuber inedible, resulting in severe loss of economic value; therefore, current research focuses on achieving cultivars that do not develop the necrotic rot.
- [d4s5]  This disease is considered to be the biggest threat to food security in coastal East Africa and around the eastern lakes.

**d5: Molluginaceae**

- [d5s0] Molluginaceae are a family of flowering plants recognized by several taxonomists.
- [d5s1]  It was previously included in the larger family Aizoaceae.
- [d5s2]  The APG III system of 2009 made no change in the status of the family as compared to the APG II system of 2003 and the APG system of 1998, apart from a reassignment of several genera, such as the placement of "Corrigiola" and "Telephium" into Caryophyllaceae, "Corbichonia" in Lophiocarpaceae, "Microtea" into Microteaceae and "Limeum" in Limeaceae, because the family was found to be widely polyphyletic in Caryophyllales.
- [d5s3]  In addition "Macarthuria" was found not to be related to "Limeum" as previously thought and thus it was placed in Macarthuriaceae, and similarly species formerly placed in "Hypertelis", apart from type species "Hypertelis spergulacea", a true Molluginaceae, were found to belong elsewhere and were described as "Kewa" in the family Kewaceae, named for the Royal Botanic Gardens Kew.
- [d5s4]  Molluginaceae is still assigned to the order Caryophyllales in the clade core eudicots, although the generic circumscription is difficult because "Mollugo" is not monophyletic.

**d6: Zeltnera**

- [d6s0] Zeltnera is a genus of flowering plants in the gentian family.
- [d6s1]  It was erected in 2004 when the genus "Centaurium" (the centauries) was split.
- [d6s2]  Genetic analysis revealed that "Centaurium" was polyphyletic, made up of plants that could be grouped into four clades. Each became a genus.
- [d6s3]  "Centaurium" remained, but it is now limited to the Eurasian species.
- [d6s4]  The Mexican species now belong to genus "Gyrandra", and the Mediterranean and Australian plants are in genus "Schenkia".
- [d6s5]  The new name "Zeltnera" was given to this genus, which contains most of the North American centauries.
- [d6s6]  There are about 25 species.

**d7: Bunyaviridae**

- [d7s0] Bunyaviridae is a defunct family of virus (see "").
- [d7s1]  The modern ICTV classifies the viruses in this former family as members of the family "Peribunyaviridae".
- [d7s2]  In 2017, the ICTV reclassified the family "Bunyaviridae" as "Bunyvirales," a taxonomic shift from a family of viruses to an order of viruses.
- [d7s3]  The body made these decisions in a 2016 convening in Budapest.
- [d7s4]  Primary reasons for this alteration revolve around these observations: approximately half of viruses in the former "Bunyaviridae" were at the time unassigned to a genus; novel viruses discovered that were characteristic of and clustered around "Bunyaviridae" based on phylogenetic analyses had bi-segmented genomes (as opposed to "Bunyaviridae's" tri-segmentation); and plant viruses also lacking tri-segmentation were previously known to be "bunya-like" yet were not properly assigned to the family "Bunyaviridae" based upon the past taxanomic classifications.
- [d7s5]  All five genera formerly in the family "Bunyaviridae" ("Hantavirus, Nairovirus, Orthobunyavirus, Phlebovirus, Tospovirus") are now novel viral families, some of which have been combined.
- [d7s6]  These new families include: "Hantaviridae, Feraviridae, Fimoviridae, Jonviridae, Nairoviridae, Peribunyaviridae, Phasmaviridae, Phenuiviridae," and "Tospoviridae".
- [d7s7]  This order of viruses belong to the fifth group of the Baltimore classification, the so called negative-sense single stranded ribonucleic acid (-)ssRNA.
- [d7s8]  They are enveloped RNA viruses.
- [d7s9]  Though generally found in arthropods or rodents, certain viruses in this order occasionally infect humans.
- [d7s10]  Some of them also infect plants.

**d8: Primulaceae**

- [d8s0] The Primulaceae are a family of herbaceous and woody flowering plants with about 53 genera with 2790 species, including some favorite garden plants and wildflowers, commonly known as the primrose family.
- [d8s1]  Most Primulaceae are perennial though some species, such as scarlet pimpernel, are annuals.
- [d8s2]  The family has been variously circumscribed, but it is now accepted in the broad sense including the former families Myrsinaceae and Theophrastaceae, because many genera traditionally placed in Primulaceae were found to belong to those other families and when united their circumscription remains intact.

**d9: Conophytum**

- [d9s0] Conophytum is a genus of South African and Namibian succulent plants that belong to the Aizoaceae family.
- [d9s1]  The name is derived from the Latin “conus” (cone) and Greek “phytum” (plant).
- [d9s2]  The plants are also known as knopies (buttons), waterblasies (water blisters), sphaeroids, conos, cone plants, dumplings, or button plants.

**d10: Monarda**

- [d10s0] Monarda is a genus of flowering plants in the mint family, Lamiaceae.
- [d10s1]  The genus is endemic to North America.
- [d10s2]  Common names include bee balm, horsemint, oswego tea, and bergamot, the latter inspired by the fragrance of the leaves, which is reminiscent of bergamot orange ("Citrus bergamia").
- [d10s3]  The genus was named for the Spanish botanist Nicolás Monardes, who wrote a book in 1574 describing plants of the New World.

## 6. hotpotqa_5a82f8e955429966c78a6abf

原位置：`train` 第 156 题 · 全局第 156 题 · `sample_id: hotpotqa_5a82f8e955429966c78a6abf`

Question: Are Mark Wystrach and Doc Neeson of the same nationality?

Note: 

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | nationality of Mark Wystrach | False | [] | American | [["d4s0"]] | context |
| u2 | nationality of Doc Neeson | False | [] | Australian | [["d9s0"]] | context |
| u3 | whether Mark Wystrach and Doc Neeson are of the same nationality | True | ["u1", "u2"] | no | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | nationality of Mark Wystrach | False | [] | American | [['d4s0']] |
| u2 | nationality of Doc Neeson | False | [] | Australian | [['d9s0']] |
| u3 | whether Mark Wystrach and Doc Neeson are of the same nationality | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: The Angels (Australian band)**

- [d1s0] The Angels are an Australian rock band which formed in Adelaide in 1974 as The Keystone Angels by John Brewster on rhythm guitar and vocals, his brother Rick Brewster on lead guitar and vocals, and Bernard "Doc" Neeson on lead vocals and guitar.
- [d1s1]  They were later joined by Graham "Buzz" Bidstrup on drums and vocals, and Chris Bailey on bass guitar and vocals.
- [d1s2]  In 1981 Bidstrup was replaced on drums by Brent Eccles.
- [d1s3]  Their studio albums on the Kent Music Report Albums Chart top 10 are "No Exit" (July 1979), "Dark Room" (June 1980), "Night Attack" (November 1981), "Two Minute Warning" (November 1984), "Howling" (October 1986) and "Beyond Salvation" (February 1990).
- [d1s4]  Their top 20 singles are "No Secrets" (1980), "Into the Heat" (1981), "We Gotta Get out of This Place" (1987), "Am I Ever Gonna See Your Face Again" (live, 1988), "Let the Night Roll On" and "Dogs Are Talking" (both 1990).

**d2: Midland (band)**

- [d2s0] Midland is an American country music group consisting of Mark Wystrach (lead vocals), Cameron Duddy (bass guitar, background vocals), and Jess Carson (lead guitar, background vocals).
- [d2s1]  Their debut single, "Drinkin' Problem", reached the top 5 on the "Billboard" Country Airplay chart.
- [d2s2]  The album's second single, "Make a Little" released to country radio on September 25, 2017.

**d3: The Angels discography**

- [d3s0] The Australian hard rock band, the Angels, have released thirteen studio albums, three live albums, six extended plays and forty-seven singles.
- [d3s1]  The Angels were formed in Adelaide in 1974 by the Brewster brothers, John and Rick, together with Bernard "Doc" Neeson.
- [d3s2]  The line-up of the band has since gone through numerous changes with Rick as the mainstay member.
- [d3s3]  They are known as Angel City internationally (to avoid confusion with now defunct 70's glamsters Angel) and later albums were released as The Angels from Angel City.
- [d3s4]  The Band always hated the international names.
- [d3s5]  Not all albums are available internationally and the ones that have been released generally have a different track listing and often an altered album cover from the original Australian releases.

**d4: Mark Wystrach**

- [d4s0] Mark Wystrach (born December 17, 1979) is an American actor and country music singer.

**d5: No Secrets (song)**

- [d5s0] "No Secrets" is a song by Australian hard rock group, The Angels, released in May 1980 from their album, "Dark Room".
- [d5s1]  "No Secrets" peaked at number 8 on the Kent Music Report Singles Chart.
- [d5s2]  It was co-written by band members, Graham "Buzz" Bidstrup and Bernard "Doc" Neeson.

**d6: Comin' Down (The Angels song)**

- [d6s0] "Comin' Down" is the third single by Australian hard rock band the Angels, released in March 1978.
- [d6s1]  The song was released from their album, "Face to Face".
- [d6s2]  The song first peaked on 8 May 1978 where it peaked at number 80 on the Kent Music Report Singles Chart and stayed in the charts for five weeks.
- [d6s3]  It was co-written by band members, Doc Neeson, John Brewster and Richard Brewster.

**d7: Tour of Duty – Concert for the Troops**

- [d7s0] Tour of Duty – Concert for the Troops was a concert in 1999 in Dili for the Australian troops serving with the International Force for East Timor.
- [d7s1]  This concert featured John Farnham, Kylie Minogue, Doc Neeson, Gina Jeffreys, James Blundell, The Living End, Dili Allstars and the RMC Band.

**d8: Am I Ever Gonna See Your Face Again**

- [d8s0] "Am I Ever Gonna See Your Face Again" is an Australian rock song written by Doc Neeson, John Brewster and Rick Brewster, and performed by their group, the Angels.
- [d8s1]  The song was initially recorded as a ballad in March 1976 but subsequently re-released as a rock song.
- [d8s2]  The song is best known for the expletive-laden audience response, "No Way, Get Fucked, Fuck Off", to the live version, which was issued in March 1988.
- [d8s3]  This chant has been described by "The Guardian"' s Darryl Mason as "one of the most famous in Australian rock history".

**d9: Doc Neeson**

- [d9s0] Bernard Patrick "Doc" Neeson OAM (4 January 1947 – 4 June 2014) was an Australian singer-songwriter and musician.
- [d9s1]  He was the front man for the hard rock band The Angels from its formation in February 1976 to their disbandment in December 1999.
- [d9s2]  For the group Neeson was the main lyricist with brothers, John and Rick Brewster, as the music composers.
- [d9s3]  Their top 20 studio albums on the Australian Kent Music Report Albums Chart are "Face to Face" (June 1978), "No Exit" (June 1979), "Dark Room" (June 1980), "Night Attack" (November 1981), "Watch the Red" (May 1983), "Two Minute Warning" (November 1984) and "Howling" (October 1986).
- [d9s4]  Their number-one album, "Beyond Salvation", on the ARIA Albums Chart appeared in February 1990 and was followed by another top 20 album, "Red Back Fever" (November 1991).
- [d9s5]  The group's top 20 singles on the related Australian charts are "No Secrets" (1980), "Into the Heat" (1981), "Never so Live" (1981), "We Gotta Get out of This Place" (1987), "Am I Ever Gonna See Your Face Again" (live, 1988), "Let the Night Roll On" (1990) and "Dogs Are Talking" (1990).

**d10: Fox Crane**

- [d10s0] Fox Crane is a fictional character on the NBC/DirecTV soap opera "Passions" and was portrayed by Justin Hartley from December 17, 2002—February 10, 2006, and Mark Cameron Wystrach from February 14, 2006—September 7, 2007.
- [d10s1]  Actor Nick Stabile took over the role temporarily following the 2004 Summer Olympic Games (which preempted Passions for a few weeks), while Hartley's wife, fellow Passions star Lindsay Hartley was on maternity leave.
- [d10s2]  Fox, as played by Hartley, was a fan favorite amongst "Passions" viewers.

## 7. hotpotqa_5a83a5df5542992ef85e233f

原位置：`train` 第 157 题 · 全局第 157 题 · `sample_id: hotpotqa_5a83a5df5542992ef85e233f`

Question: Chad Michaels was a runner up on the fourth season of RuPaul's Drag Race and is known for impersonating which singer?

Note: 对于问题中显性包含已知信息的题目，不需要再去context里找证据，按照新的拆分方法拆分，是否合理

Type: single · fallback: False · SFT snapshots: 6

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | singer impersonated by Chad Michaels | True | [] | Cher | [["d4s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | runner-up of the fourth season of RuPaul's Drag Race | False | [] | Chad Michaels | [['d4s1']] |
| u2 | singer whom {u1} is known for impersonating | True | ['u1'] | Cher | [['d4s0']] |

### Source documents (reference only)

**d1: RuPaul's Drag Race**

- [d1s0] RuPaul's Drag Race is an American reality competition television series produced by World of Wonder for Logo TV and, beginning with the ninth season, VH1.
- [d1s1]  The show documents RuPaul in the search for "America's next drag superstar."
- [d1s2]  RuPaul plays the role of host, mentor, and head judge for this series, as contestants are given different challenges each week.
- [d1s3]  "RuPaul's Drag Race" employs a panel of judges, including RuPaul, Michelle Visage, Ross Mathews, Carson Kressley, and a host of other guest judges, who critique contestants' progress throughout the competition.
- [d1s4]  The title of the show is a play on drag queen and drag racing, and the title sequence and song "Drag Race" both have a drag-racing theme.

**d2: RuPaul's Drag Race (season 7)**

- [d2s0] The seventh season of RuPaul's Drag Race began airing on March 2, 2015.
- [d2s1]  Returning judges include RuPaul and Michelle Visage, while the space previously occupied by Santino Rice has been filled by new additions Ross Mathews and Carson Kressley.
- [d2s2]  Matthews and Kressley are only both present for the season premiere and will take turns sharing judging responsibilities.
- [d2s3]  Shawn Morales, a member of the Pit Crew since the third season and Simon Sherry-Wood, a member in the sixth season, do not appear this season and were replaced by Bryce Eilenberg.
- [d2s4]  Like the previous two seasons of "RuPaul's Drag Race", the season featured 14 contestants competing for the title of "America's Next Drag Superstar", a one-year supply of Anastasia Beverly Hills cosmetics and a cash prize of 100,000 dollars.
- [d2s5]  The premiere of season, the show debuted with a live and same-day viewership of 350,000, a 20% increase from the previous season.
- [d2s6]  On March 20, 2015, it was announced that LogoTV had given the series an early renewal for an eighth season.

**d3: Carmen Carrera**

- [d3s0] Carmen Roman (born Christopher Roman; April 13, 1985), better known by her stage name Carmen Carrera, is an American reality television personality, model, burlesque performer, and actress, known for appearing on the third season of the Logo reality television series "RuPaul's Drag Race", as well as its spin-off series "RuPaul's Drag U".
- [d3s1]  Although she presented as male during the third season of "RuPaul's Drag Race", on May 1, 2012, ABC News reported that Carrera is a transgender woman.

**d4: Chad Michaels**

- [d4s0] Chad Michaels is an American drag performer and Cher impersonator.
- [d4s1]  He was the runner up of the fourth season of "RuPaul's Drag Race" and was the winner of "" season one.

**d5: List of RuPaul's Drag Race episodes**

- [d5s0] "RuPaul's Drag Race" is an American reality competition television series produced by World of Wonder for Logo TV.
- [d5s1]  The show documents RuPaul in his search for "America's next drag superstar."
- [d5s2]  Queen RuPaul plays the roles of host, mentor, and source of inspiration for this series, as contestants are given different challenges each week.
- [d5s3]  "RuPaul's Drag Race" employs a panel of judges, including RuPaul, Michelle Visage and a host of other guest judges, who critique contestants' progress throughout the competition.
- [d5s4]  The title of the show is a play on drag queen and drag racing, and the title sequence and song "Drag Race" both have a drag-racing theme.

**d6: List of RuPaul's Drag Race contestants**

- [d6s0] This is a list of contestants who have appeared on the American television show "RuPaul's Drag Race".
- [d6s1]  Contestants compete against each other and are progressively eliminated, until just a winner remains, who is crowned "next drag superstar".
- [d6s2]  They are judged by drag queen RuPaul and her panel of judges.
- [d6s3]  The series first aired in 2009 and as of 2017, there have been nine seasons of the show.
- [d6s4]  A total of 113 different participants have been selected as finalists in the show in its eight years running, with nine drag queens — BeBe Zahara Benet, Tyra Sanchez, Raja, Sharon Needles, Jinkx Monsoon, Bianca Del Rio, Violet Chachki, Bob the Drag Queen, and Sasha Velour being crowned so far as "America's Next Drag Superstar".
- [d6s5]  In addition, an season aired in 2012 featuring twelve returning contestants from the first four seasons, each competing for a place in the "Drag Race Hall of Fame".
- [d6s6]  The season was won by Chad Michaels, previously a runner-up in season four.
- [d6s7]  In 2015, it was announced "All Stars" had been renewed and a premiered on August 25, 2016.
- [d6s8]  The second season was won by Alaska, who was previously a runner-up in season 5.

**d7: RuPaul's Drag U**

- [d7s0] RuPaul's Drag U (as in "Drag University") is an American reality television series that debuted July 19, 2010, on Logo TV.
- [d7s1]  Its final episode aired in August 2012.
- [d7s2]  It was hosted by RuPaul and a team of drag queen "professors".
- [d7s3]  "Drag U" was a spin-off of "RuPaul's Drag Race".
- [d7s4]  RuPaul confirmed on May 8, 2013 via Twitter that the series had been cancelled.

**d8: Raven (drag queen)**

- [d8s0] David Petruschin (Russian: Дэвид Петрушин, born April 8, 1979), better known by his stage name Raven, is an American drag queen and make-up artist from Riverside, California.
- [d8s1]  He was the runner-up of the second season of "RuPaul's Drag Race" and also the runner-up of the of "".
- [d8s2]  He also made regular appearances on all three seasons of "RuPaul's Drag U".
- [d8s3]  Through these shows, he has collected one of the largest followings among all contestants.
- [d8s4]  He's well known as a fixture in the Southern California nightclub-scene and for his weekly webseries with Raja, where they critique the clothing of celebrities and other "Drag Race" alumnae.

**d9: RuPaul's Drag Race (season 1)**

- [d9s0] The first season of "RuPaul's Drag Race", later referred to as "The Lost Season", premiered in the United States on February 2, 2009, on VH-1.
- [d9s1]  Nine contestants were selected to compete in the running of becoming "America's Next Drag Superstar."
- [d9s2]  The first season was filmed during the summer of 2008.
- [d9s3]  The winner of the first season won a lifetime supply of MAC Cosmetics, was featured in an LA Eyeworks campaign, joined the Logo Drag Race tour, and won a cash prize of $20,000.
- [d9s4]  One of the nine contestants to compete on "RuPaul's Drag Race" was determined by an audience vote via the show's official website.
- [d9s5]  The results were announced in early September 2008.
- [d9s6]  The theme song playing during the runway every episode was "Cover Girl" from RuPaul's album "Champion".
- [d9s7]  This season and season one of All-Stars are the only seasons to not feature the "Snatch Game."

**d10: RuPaul's Drag Race: All Stars**

- [d10s0] RuPaul's Drag Race All Stars is an American reality competition television series produced by World of Wonder for Logo TV.
- [d10s1]  The show is a spin-off of "RuPaul's Drag Race" where RuPaul allows past contestants to come back and compete for a spot in the Drag Race Hall of Fame.
- [d10s2]  RuPaul plays the roles of host, mentor, and source of inspiration for this series, as contestants are given different challenges each week.
- [d10s3]  "RuPaul's Drag Race" employs a panel of judges, including RuPaul, Michelle Visage and a host of other guest judges, who critique contestants' progress throughout the competition.

## 8. hotpotqa_5a83c3a95542996488c2e4c1

原位置：`train` 第 158 题 · 全局第 158 题 · `sample_id: hotpotqa_5a83c3a95542996488c2e4c1`

Question: Which court case, Gonzales v. Carhart or Lawrence v. Texas, struck down the sodomy law?

Note: 

Type: comparison · fallback: False · SFT snapshots: 5

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | whether Gonzales v. Carhart struck down the sodomy law | False | [] | no | [] | no_direct_support |
| u2 | whether Lawrence v. Texas struck down the sodomy law | False | [] | yes | [["d10s1"]] | context |
| u3 | which court case struck down the sodomy law | True | ["u1", "u2"] | Lawrence v. Texas | [[]] | question_presupposition |

- u1：无直接支持集合；不能仅由 expected_answer 将本单元标为 SUPPORTED。候选题结论可按独立的 presupposition_sets 路径判断。

- u3：`by_presupposition=true`，预设路径 `[["d10s1"]]`；不是直接证据。

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Gonzales v. Carhart struck down the sodomy law | False | [] | no | [] |
| u2 | whether Lawrence v. Texas struck down the sodomy law | False | [] | yes | [['d10s1']] |
| u3 | which of Gonzales v. Carhart and Lawrence v. Texas struck down the sodomy law | True | ['u1', 'u2'] | Lawrence v. Texas | [[]] |

### Source documents (reference only)

**d1: State v. Limon**

- [d1s0] State v. Limon (280 Kan. 275, 122 P.3d 22) is a 2005 Kansas Supreme Court case in which a state law allowing for lesser punishment for statutory rape convictions if the partners were of different sexes than if they were of the same sex was found unconstitutional under both the federal and Kansas state constitutions.
- [d1s1]  It was among the first cases to cite the United States Supreme Court decision "Lawrence v. Texas" as precedent, months after the Virginia Supreme Court did similarly in "Martin v. Ziherl".

**d2: Isabel González**

- [d2s0] Isabel González (May 2, 1882 – June 11, 1971) was a Puerto Rican activist who helped pave the way for Puerto Ricans to be given United States citizenship.
- [d2s1]  As a young unwed pregnant woman, González had her plans to find and marry the father of her unborn child derailed by the United States Treasury Department when she was excluded as an alien "likely to become a public charge" upon her arrival in New York City.
- [d2s2]  González challenged the Government of the United States in the groundbreaking case "Gonzales v. Williams" (192 U.S. 1 (1904)).
- [d2s3]  Officially the case was known as "Isabella Gonzales, Appellant, v. William Williams, United States Commissioner of Immigration at the Port of New York" No. 225, argued December 4, 7, 1903, and decided January 4, 1904.
- [d2s4]  Her case was an appeal from the Circuit Court of the United States for the Southern District of New York, filed February 27, 1903, after also having her Writ of Habeas Corpus (HC.
- [d2s5]  1-187) dismissed.
- [d2s6]  Her Supreme Court case is the first time that the Court confronted the citizenship status of inhabitants of territories acquired by the United States.
- [d2s7]  González actively pursued the cause of U.S. citizenship for all Puerto Ricans by writing letters published in "The New York Times".

**d3: Partial-Birth Abortion Ban Act**

- [d3s0] The Partial-Birth Abortion Ban Act of 2003 (Pub.L.
- [d3s1]  108–105 , 117 Stat.
- [d3s2]  1201 , enacted  05, 2003 , , PBA Ban) is a United States law prohibiting a form of late termination of pregnancy called "partial-birth abortion," referred to in medical literature by as intact dilation and extraction.
- [d3s3]  Under this law, "Any physician who, in or affecting interstate or foreign commerce, knowingly performs a partial-birth abortion and thereby kills a human fetus shall be fined under this title or imprisoned not more than 2 years, or both."
- [d3s4]  The law was enacted in 2003, and in 2007 its constitutionality was upheld by the U.S. Supreme Court, in the case of "Gonzales v. Carhart".

**d4: LeRoy Carhart**

- [d4s0] LeRoy Harrison Carhart (born 1941) is an American physician from New Jersey best known for performing abortions late in pregnancy.
- [d4s1]  He became famous for his participation in the Supreme Court cases "Stenberg v. Carhart" and "Gonzales v. Carhart", both of which dealt with intact dilation and extraction (colloquially known as "partial-birth abortion").
- [d4s2]  He was one of the four subjects of the 2013 documentary "After Tiller".

**d5: Franklin v. State**

- [d5s0] Franklin v. State, (Fla. 1971), was a case in which the Florida Supreme Court struck down Florida's sodomy law as being "unconstitutional for vagueness and uncertainty in its language, violating constitutional due process to the defendants."
- [d5s1]  The court retained the state's prohibition on sodomy by ruling that anal and oral sex could still be prosecuted under the lesser charge of "unnatural and lascivious" conduct, thus reducing the crime from a felony to a misdemeanor.

**d6: Bowers v. Hardwick**

- [d6s0] Bowers v. Hardwick, 478 U.S. 186 (1986) , is a United States Supreme Court decision, overturned in 2003, that upheld, in a 5–4 ruling, the constitutionality of a Georgia sodomy law criminalizing oral and anal sex in private between consenting adults, in this case with respect to homosexual sodomy, though the law did not differentiate between homosexual sodomy and heterosexual sodomy.

**d7: State v. Whitmarsh**

- [d7s0] State v. Whitmarsh was a South Dakota Supreme Court case decided on November 18, 1910, which asked whether or not fellatio, or oral sex, should be classified as sodomy.
- [d7s1]  The contemporary federal common law definition of sodomy did not include fellatio.
- [d7s2]  The court ruled that fellatio was an "abominable and disgusting" crime against nature and outlawed it between any two persons, regardless of marital status, sexual orientation or age.
- [d7s3]  The case set a precedent for other states' laws and remained in effect in South Dakota for the next 66 years, until all sodomy laws, including the "crime against nature" statute, were abolished by the South Dakota Legislature in 1976.

**d8: Taylor v. United States (2016)**

- [d8s0] Taylor v. United States, 579 U.S. ___ (2016) , was a United States Supreme Court case in which the Court held that in a federal criminal prosecution under the Hobbs Act, the government is not required to prove an interstate commerce element beyond a reasonable doubt.
- [d8s1]  The Court relied on the decision in "Gonzales v. Raich" which held that Congress has the authority to regulate the marijuana market given that even local activities can have a "substantial effect" on interstate commerce.

**d9: Gonzales v. Carhart**

- [d9s0] Gonzales v. Carhart, 550 U.S. 124 (2007), is a United States Supreme Court case that upheld the Partial-Birth Abortion Ban Act of 2003.
- [d9s1]  The case reached the high court after U.S. Attorney General Alberto Gonzales appealed a ruling of the United States Court of Appeals for the Eighth Circuit in favor of LeRoy Carhart that struck down the Partial-Birth Abortion Ban Act.
- [d9s2]  Also before the Supreme Court was the consolidated appeal of Gonzales v. Planned Parenthood from the United States Court of Appeals for the Ninth Circuit, which had struck down the Partial-Birth Abortion Ban Act.

**d10: Lawrence v. Texas**

- [d10s0] Lawrence v. Texas, 539 U.S. 558 (2003) is a landmark decision by the United States Supreme Court.
- [d10s1]  The Court struck down the sodomy law in Texas in a 6-3 decision and, by extension, invalidated sodomy laws in 13 other states, making same-sex sexual activity legal in every U.S. state and territory.
- [d10s2]  The Court, with a five-justice majority, overturned its previous ruling on the same issue in the 1986 case "Bowers v. Hardwick", where it upheld a challenged Georgia statute and did not find a constitutional protection of sexual privacy.

## 9. hotpotqa_5a8492b65542997b5ce3fec5

原位置：`train` 第 159 题 · 全局第 159 题 · `sample_id: hotpotqa_5a8492b65542997b5ce3fec5`

Question: Pylon and Bullet for My Valentine, is what type of musical organization?

Note: 保留single，同时验证一下对应原来旧gold中的u1u2的证据是否都需要，保留需要的证据集合。

Type: single · fallback: False · SFT snapshots: 7

### Adjusted units and annotation

**执行结果：** 保留用户指定 single；共同属性必须联合两方证据，不允许由一方推另一方。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | type of musical organization for Pylon and Bullet for My Valentine | True | [] | band | [["d2s0", "d9s0"], ["d2s0", "d9s1"], ["d2s0", "d9s6"], ["d2s0", "d9s7"], ["d2s0", "d9s8"], ["d2s0", "d3s1"], ["d2s0", "d3s2"], ["d2s0", "d4s0"], ["d2s0", "d1s0"], ["d2s1", "d9s0"], ["d2s1", "d9s1"], ["d2s1", "d9s6"], ["d2s1", "d9s7"], ["d2s1", "d9s8"], ["d2s1", "d3s1"], ["d2s1", "d3s2"], ["d2s1", "d4s0"], ["d2s1", "d1s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | type of musical organization Pylon is | False | [] | band | [['d2s0'], ['d2s1']] |
| u2 | type of musical organization Bullet for My Valentine is | False | [] | band | [['d9s0'], ['d9s1'], ['d9s6'], ['d9s7'], ['d9s8'], ['d3s1'], ['d3s2'], ['d4s0'], ['d1s0']] |
| u3 | type of musical organization that Pylon and Bullet for My Valentine both are | True | ['u1', 'u2'] | band | [[]] |

### Source documents (reference only)

**d1: Jeff Killed John (EP)**

- [d1s0] Jeff Killed John is the last EP by Welsh nu metal band Jeff Killed John, before changing their name to Bullet for My Valentine.
- [d1s1]  This EP also marks the last recorded material with bassist Nick Crandle, before Jason James replaced him.
- [d1s2]  Many song elements from this EP would be reworked into later tracks for Bullet for My Valentine music: "Routine Unhappiness" contains riff elements that would later become "Tears Don't Fall," with lyrical content that would appear on "10 Years Today;" "Nation2Nation" would eventually become the bonus track "Turn to Despair" on the Japanese edition of "Hand of Blood;" and "All These Things I Hate (Revolve Around Me)" is an early demo of the song of the same name that would eventually appear on Bullet for My Valentine's debut album "The Poison."

**d2: Pylon (band)**

- [d2s0] Pylon were an American rock band from Athens, Georgia.
- [d2s1]  The band's danceable sound, a blend of new wave, post-punk, jangle pop, alternative rock and funk rock, influenced the Athens music scene and the 1980s American pop underground.
- [d2s2]  AllMusic wrote that Pylon's "role as elder statesmen of the alternative rock explosion is unassailable".

**d3: Matthew Tuck**

- [d3s0] Matthew "Matt" Tuck (born 20 January 1980) is a Welsh musician.
- [d3s1]  He is the lead vocalist and rhythm guitarist in the Welsh heavy metal band Bullet for My Valentine.
- [d3s2]  He and the other 3 members of his old band founded "Jeff Killed John" in 1998, but after bassist Nick Crandle left in 2003, the band was renamed to Bullet for My Valentine.
- [d3s3]  He is also a singer and guitarist in the supergroup AxeWound, which was formed in 2012.
- [d3s4]  He also plays piano, drums, keyboard, and harmonica.
- [d3s5]  He did a collaboration with Max Cavalera (Soulfly, Cavalera Conspiracy, ex-Sepultura) and with Apocalyptica in the song "Repressed".

**d4: Rare Cuts (EP)**

- [d4s0] Rare Cuts is an EP by Welsh metalcore band Bullet for My Valentine, released in Japan only.
- [d4s1]  "Rare Cuts" contains bonus tracks from Bullet for My Valentine's album "The Poison".
- [d4s2]  It includes an acoustic version of the band's song "Tears Don't Fall".

**d5: Argonotes**

- [d5s0] Argonotes, the unofficial band of the Toronto Argonauts is an all volunteer organization committed to bringing quality musical entertainment and a "traditional football atmosphere" to all Argonauts home football games.
- [d5s1]  Comprising more than 50 musicians on most game days, Argonotes is the largest musical organization associated with the CFL.

**d6: David W. Tucker**

- [d6s0] David W. Tucker (1929–2003) was a jazz trombonist, music educator, composer of band and orchestral music, record producer, and marching band arranger, most renowned as the director of the University of California Jazz Ensembles from 1969 until 1985.
- [d6s1]  Under his direction, the organization expanded to become the largest musical organization on the campus of the University of California, Berkeley, had an international reputation resulting from foreign tours, and sponsored the Pacific Coast Collegiate Jazz Festival.
- [d6s2]  Numerous student members of the organization have become renowned jazz musicians, composers, and music educators.

**d7: Pylon station**

- [d7s0] The pylon station is a type of deep underground subway station.
- [d7s1]  The basic distinguishing characteristic of the pylon station is the manner of division of the central hall from the station tunnels

**d8: Handel and Haydn Society**

- [d8s0] The Handel and Haydn Society, familiarly known as H+H, is an American chorus and period instrument orchestra based in Boston, Massachusetts.
- [d8s1]  Founded in 1815, it is the third oldest musical organization in the United States after the Stoughton Musical Society (founded in 1786) and the U.S. Marine Band (founded 1798), and the oldest continually performing arts organization in the United States.

**d9: Bullet for My Valentine**

- [d9s0] Bullet for My Valentine, often abbreviated as BFMV or B4MV, are a Welsh heavy metal band from Bridgend, formed in 1998.
- [d9s1]  The band is composed of Matthew Tuck (lead vocals, rhythm guitar), Michael Paget (lead guitar, backing vocals), Michael Thomas (drums) and Jamie Mathias (bass guitar).
- [d9s2]  Former members include Nick Crandle and Jason James; both were on bass.
- [d9s3]  They were formed under the name Jeff Killed John and started their music career by covering songs by Metallica and Nirvana.
- [d9s4]  Jeff Killed John recorded six songs which were not released; two of these tracks were reworked later in their career as Bullet for My Valentine.
- [d9s5]  Financial difficulties dictated the name change, which was followed by a change in music direction.
- [d9s6]  In 2002, the band secured a five-album deal with Sony BMG.
- [d9s7]  The band has stated that their music is influenced by classic metal acts such as Metallica, Iron Maiden and Slayer.
- [d9s8]  The band is part of the Cardiff music scene.

**d10: League of American Orchestras**

- [d10s0] The League of American Orchestras, formerly the American Symphony Orchestra League, is a North American Musical Organization consisting of a network of approximately 800 orchestras.
- [d10s1]  “Dedicated to helping orchestras meet the challenges of the twenty-first century,” the League consists of leading symphony and philharmonic orchestras, collegiate orchestras, community ensembles, and youth and student ensembles.
- [d10s2]  The only national organization devoted and focused on elevating the orchestra industry, the League was founded in 1942 and later chartered by Congress in 1962.
- [d10s3]  The League creates a network of all facets of the industry, including administrators, managers, board members, business partners, volunteers, and musicians.
- [d10s4]  Each year this organization presents two awards: the Gold Baton Award and the Helen M. Thompson Award.
- [d10s5]  The League affects the orchestral world through several outreach experiences, dedicated advocacy to music education and especially orchestral education, and maintaining and communicating a breadth of information and pertinent topics in publications.
- [d10s6]  It has also developed detailed antitrust policy and guidelines in order to comply with the landscape of the industry.
- [d10s7]  The League is a leading force in work on legislation regarding orchestras and support for the arts.

## 10. hotpotqa_5a84b72b5542991dd0999dab

原位置：`train` 第 160 题 · 全局第 160 题 · `sample_id: hotpotqa_5a84b72b5542991dd0999dab`

Question: What genre, usually involving a mysterious death, is exhibited by a book who features detective Sir Henry Merrivale?

Note: 我觉得这种题目并不属于题干中包含已知信息，应该按照旧gold的结构拆分

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | genre of a book featuring detective Sir Henry Merrivale | False | [] | mystery novel | [["d1s0", "d1s1"], ["d2s0", "d2s1"], ["d4s0", "d4s1"], ["d5s0", "d5s1"], ["d6s0", "d6s1"], ["d7s0", "d7s1"], ["d8s0", "d8s1"], ["d9s0", "d9s1"], ["d10s0", "d10s1"]] | context |
| u2 | genre usually involving a mysterious death to which {u1} belongs | True | ["u1"] | mystery fiction | [["d3s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | genre of a book featuring detective Sir Henry Merrivale | False | [] | mystery novel | [['d1s0', 'd1s1'], ['d2s0', 'd2s1'], ['d4s0', 'd4s1'], ['d5s0', 'd5s1'], ['d6s0', 'd6s1'], ['d7s0', 'd7s1'], ['d8s0', 'd8s1'], ['d9s0', 'd9s1'], ['d10s0', 'd10s1']] |
| u2 | genre usually involving a mysterious death to which {u1} belongs | True | ['u1'] | mystery fiction | [['d3s0']] |

### Source documents (reference only)

**d1: The Reader is Warned**

- [d1s0] The Reader is Warned is a mystery novel by the American writer John Dickson Carr (1906–1977), who published it under the name of Carter Dickson.
- [d1s1]  It is a whodunit and features the series detective Sir Henry Merrivale.

**d2: He Wouldn't Kill Patience**

- [d2s0] He Wouldn't Kill Patience is a mystery novel by the American writer John Dickson Carr (1906–1977), who published it under the name of Carter Dickson.
- [d2s1]  It is a locked room mystery and features the series detective Sir Henry Merrivale and his long-time associate, Scotland Yard's Chief Inspector Humphrey Masters.

**d3: Mystery fiction**

- [d3s0] Mystery fiction is a genre of fiction usually involving a mysterious death or a crime to be solved.
- [d3s1]  In a closed circle of suspects, each suspect must have a credible motive and a reasonable opportunity for committing the crime.
- [d3s2]  The central character must be a detective who eventually solves the mystery by logical deduction from facts fairly presented to the reader.
- [d3s3]  Sometimes mystery books are nonfictional.
- [d3s4]  "Mystery fiction" can be detective stories in which the emphasis is on the puzzle or suspense element and its logical solution such as a whodunit.
- [d3s5]  Mystery fiction can be contrasted with hardboiled detective stories, which focus on action and gritty realism.

**d4: Night at the Mocking Widow**

- [d4s0] Night at the Mocking Widow is a mystery novel by the American writer John Dickson Carr (1906–1977), who published it under the name of Carter Dickson .
- [d4s1]  It is a whodunnit and features the series detective Sir Henry Merrivale.

**d5: Murder in the Submarine Zone**

- [d5s0] Murder in the Submarine Zone (also published as "Nine—And Death Makes Ten" and "Murder in the Atlantic") is a mystery novel by the American writer John Dickson Carr (1906–1977), who published it under the name of Carter Dickson.
- [d5s1]  It is a whodunnit and features the series detective Sir Henry Merrivale.

**d6: And So to Murder**

- [d6s0] And So to Murder is a mystery novel by the American writer John Dickson Carr (1906–1977), who published it under the name of Carter Dickson.
- [d6s1]  It is a whodunnit and features the series detective Sir Henry Merrivale and Scotland Yard Chief Inspector Humphrey Masters.

**d7: The Gilded Man**

- [d7s0] The Gilded Man (also published as "Death and the Gilded Man") is a mystery novel by the American writer John Dickson Carr (1906–1977), who published it under the name of Carter Dickson.
- [d7s1]  It is a whodunnit and features the series detective Sir Henry Merrivale.

**d8: The Curse of the Bronze Lamp**

- [d8s0] The Curse of the Bronze Lamp (also published as "Lord of the Sorcerers") is a mystery novel by the American writer John Dickson Carr (1906–1977), who published it under the name of Carter Dickson.
- [d8s1]  It is a locked room mystery or, more properly, a subset of that category known as an "impossible crime", and features the series detective Sir Henry Merrivale.
- [d8s2]  Carr considered this one of his best impossible crime novels.

**d9: My Late Wives**

- [d9s0] My Late Wives is a mystery novel by the American writer John Dickson Carr (1906–1977), who published it under the name of Carter Dickson.
- [d9s1]  It is a whodunnit and features the series detective Sir Henry Merrivale and his long-time associate, Scotland Yard's Chief Inspector Humphrey Masters.

**d10: Death in Five Boxes**

- [d10s0] Death in Five Boxes is a mystery novel by the American writer John Dickson Carr (1906–1977), who published it under the name of Carter Dickson.
- [d10s1]  It is a whodunnit and features the series detective Sir Henry Merrivale and his associate, Scotland Yard's Chief Inspector Humphrey Masters.

## 11. hotpotqa_5a84f8b65542997b5ce3ff94

原位置：`train` 第 161 题 · 全局第 161 题 · `sample_id: hotpotqa_5a84f8b65542997b5ce3ff94`

Question: Which is a flowering plant the tolerates sandy soil and low rainfall: Luma or Cowpea?

Note: 

Type: comparison · fallback: False · SFT snapshots: 5

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | whether Luma tolerates sandy soil and low rainfall | False | [] | no | [] | no_direct_support |
| u2 | whether Cowpea tolerates sandy soil and low rainfall | False | [] | yes | [["d5s1"]] | context |
| u3 | which is a flowering plant that tolerates sandy soil and low rainfall | True | ["u1", "u2"] | cowpea | [[]] | question_presupposition |

- u1：无直接支持集合；不能仅由 expected_answer 将本单元标为 SUPPORTED。候选题结论可按独立的 presupposition_sets 路径判断。

- u3：`by_presupposition=true`，预设路径 `[["d5s1"]]`；不是直接证据。

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Luma tolerates sandy soil and low rainfall | False | [] | no | [] |
| u2 | whether cowpea tolerates sandy soil and low rainfall | False | [] | yes | [['d5s1']] |
| u3 | which of Luma and cowpea is a flowering plant that tolerates sandy soil and low rainfall | True | ['u1', 'u2'] | cowpea | [[]] |

### Source documents (reference only)

**d1: Spinney Hills, East Quogue**

- [d1s0] Spinney Hills is in East Quogue, New York on the eastern end of the Long Island Central Pine Barrens region.
- [d1s1]  It is often used as a hiking, hunting, and off-roading area for dirt bikers, quadders, paintballers, and four-wheelers that includes miles of trails with near beach sand consistency.
- [d1s2]  Spinney hills gets its name because of Spinney Road, which used to connect the East Quogue side of the hills to Sears Bellows County Park and Flanders (home of the Big Duck) to the north prior to the construction of the Sunrise Highway New York State Route 27.
- [d1s3]  This region was created by glacial deposits of rock and sand during the last ice age.
- [d1s4]  The sandy soil also absorbs most rainfall so there are few ponds or rivers in the area.
- [d1s5]  There is a shallow glacial well in Spinney Hills known as an aquifer, which is where most of the rainfall in the region is stored.
- [d1s6]  These hills are the continuation of a long east west ridge of hills known as the Ronkonkoma Moraine, which form the 'backbone' of Long Island.
- [d1s7]  Much of this region is undeveloped other than a sand mine to the west and Southampton Pines to the east.
- [d1s8]  There have been large scale legal battles between private real estate companies and the Town of Southampton over the future of the area, being it is one of the last expanses of wilderness left on Long Island.
- [d1s9]  There is a very large native population of white-tailed deer in the region due to lack of natural predators.
- [d1s10]  In the higher elevations small sections of the hills have an almost alpine-desert look, with sandy open plateaus and extremely dwarfed vegetation .
- [d1s11]  The Dwarf Pitch Pine which dominate the region grow not much taller than twenty feet in height due to dry, nutrient-poor soil.
- [d1s12]  There is a desert effect in the Pine Barrens, with relatively higher daytime temperatures and cooler nighttime temperatures than the coast, only a few miles away.
- [d1s13]  There are spectacular views of the Atlantic Ocean and Peconic Bay from certain peaks in this region if one knows where to hike.
- [d1s14]  The consistent ocean breeze at the higher elevations passing through the long brushy needles of the Dwarf Pitch Pines creates a gentle whisping sound, or white noise, adding a peaceful ambience to the big skies and expansiveness one feels in this region.

**d2: Cucurbita digitata**

- [d2s0] Cucurbita digitata is a species of flowering plant in the squash family known by the common names fingerleaf gourd and bitter squash.
- [d2s1]  It is similar to "Cucurbita californica", "Cucurbita cordata", "Cucurbita cylindrata", and "Cucurbita palmata" and all these species hybridize readily.
- [d2s2]  These species form the only restricted xerophyte species group in the genus "Cucurbita".
- [d2s3]  Each member of this species group is native to the Southwestern United States and Northwestern Mexico where they are relatively uncommon.
- [d2s4]  Each group member is found in hot, arid regions with low rainfall.
- [d2s5]  They prefer soil that is loose, gravelly, and well-drained.
- [d2s6]  "C. digitata" is native to northern Baja California at higher elevations, northern Sonora, Mexico, southern Arizona, and southwestern New Mexico.
- [d2s7]  The juvenile leaves of "C. cylindrata", "C. cordata", "C. digitata", and "C. palmata" show a high degree of similarity, but their mature leaves are visibly different, as are their root structures.
- [d2s8]  "C. palmata" and "C. digitata" are sympatric, with "C. palmata" separating the ranges of "C. digitata" at the juncture of Baja California, California, and Arizona.
- [d2s9]  "C. digitata" fruits are clear green mottle that turns yellow at maturity, striped, and round.

**d3: Cucurbita palmata**

- [d3s0] Cucurbita palmata is a species of flowering plant in the squash family known by the common names coyote melon and coyote gourd.
- [d3s1]  It is similar to "Cucurbita californica", "Cucurbita cordata", "Cucurbita cylindrata", and "Cucurbita digitata" and all these species hybridize readily.
- [d3s2]  It was first identified by Sereno Watson in 1876.
- [d3s3]  These species form the only restricted xerophyte species group in the genus "Cucurbita".
- [d3s4]  Each member of this species group is native to the Southwestern United States and Northwestern Mexico where they are relatively uncommon.
- [d3s5]  Each group member is found in hot, arid regions with low rainfall.
- [d3s6]  They prefer soil that is loose, gravelly, and well-drained.
- [d3s7]  "C. palmata" is native to northeastern Baja California, southeastern California, and southwestern Arizona to a point near the Colorado River.
- [d3s8]  The juvenile leaves of "C. cylindrata", "C. cordata", "C. digitata", and "C. palmata" show a high degree of similarity, but their mature leaves are visibly different, as are their root structures.
- [d3s9]  "C. palmata" and "C. digitata" are sympatric, with "C. palmata" separating the ranges of "C. digitata" at the juncture of Baja California, California, and Arizona.
- [d3s10]  "C. palmata" fruits are diffuse green mottle that turns yellow at maturity, striped, and round.

**d4: Cucurbita cylindrata**

- [d4s0] Cucurbita cylindrata is a species of flowering plant in the squash family.
- [d4s1]  It is similar to "Cucurbita californica", "Cucurbita cordata", "Cucurbita digitata", and "Cucurbita palmata" and all these species hybridize readily.
- [d4s2]  These species form the only restricted xerophyte species group in the genus "Cucurbita".
- [d4s3]  Each member of this species group is native to the Southwestern United States and Northwestern Mexico where they are relatively uncommon.
- [d4s4]  Each group member is found in hot, arid regions with low rainfall.
- [d4s5]  They prefer soil that is loose, gravelly, and well-drained.
- [d4s6]  "C. cylindrata" is found only in the middle portion of Baja California, mostly in Baja California Sur.
- [d4s7]  Botanists Bemis and Whitaker suggest that "C. cordata" and "C. cylindrata" may be a case of sympatric speciation.
- [d4s8]  The juvenile leaves of "C. cylindrata", "C. cordata", "C. digitata", and "C. palmata" show a high degree of similarity, but their mature leaves are visibly different, as are their root structures.
- [d4s9]  "C. cylindrata" fruits are dark green, striped, and round.

**d5: Cowpea**

- [d5s0] The cowpea, "Vigna unguiculata", is an annual herbaceous legume from the genus "Vigna".
- [d5s1]  Due to its tolerance for sandy soil and low rainfall it is an important crop in the semi-arid regions across Africa and other countries.
- [d5s2]  It requires very few inputs, as the plants root nodules are able to fix atmospheric nitrogen, making it a valuable crop for resource poor farmers and well-suited to intercropping with other crops.
- [d5s3]  The whole plant is used as forage for animals, with its use as cattle feed likely responsible for its name.

**d6: Cucurbita cordata**

- [d6s0] Cucurbita cordata is a species of flowering plant in the squash family.
- [d6s1]  It is similar to "Cucurbita californica", "Cucurbita cylindrata", "Cucurbita digitata", and "Cucurbita palmata" and all these species hybridize readily.
- [d6s2]  These species form the only restricted xerophyte species group in the genus "Cucurbita".
- [d6s3]  Each member of this species group is native to the Southwestern United States and Northwestern Mexico where they are relatively uncommon.
- [d6s4]  Each group member is found in hot, arid regions with low rainfall.
- [d6s5]  They prefer soil that is loose, gravelly, and well-drained.
- [d6s6]  "C. cordata" is found only in the vicinity of Bahía de los Ángeles, Baja California.
- [d6s7]  Botanists Bemis and Whitaker suggest that "C. cordata" and "C. cylindrata" may be a case of sympatric speciation.
- [d6s8]  The juvenile leaves of "C. cylindrata", "C. cordata", "C. digitata", and "C. palmata" show a high degree of similarity, but their mature leaves are visibly different, as are their root structures.
- [d6s9]  "C. cordata" fruits are gray green, striped, and round.

**d7: Limnophila aromatica**

- [d7s0] Limnophila aromatica (synonym: Limnophila chinensis var.
- [d7s1]  aromatica; also called rice paddy herb) is a tropical flowering plant in the plantain family, Plantaginaceae.
- [d7s2]  It is native to Southeast Asia, where it flourishes in hot temperatures and grows most often in watery environments, particularly in flooded rice fields.
- [d7s3]  It is called "Ngò ôm" or "ngò om" or "ngổ" in Vietnam and used as an herb and also cultivated for use as an aquarium plant.
- [d7s4]  The plant was introduced to North America in the 1970s due to Vietnamese immigration following the Vietnam War.
- [d7s5]  It is called "ma om" (ម្អម) in Khmer.
- [d7s6]  It is used in traditional Cambodian soup dishes and Southern Vietnamese cuisine.
- [d7s7]  It can grow in flooded rice paddies during wet season but it grows best on drained but still wet sandy soil of harvested rice paddies for a few months after the rainy season ended.
- [d7s8]  It dies out soon after it flowers.
- [d7s9]  Rural Cambodians often harvest them and put them on the roof of their houses to dry for later use.

**d8: Luma (plant)**

- [d8s0] Luma is a genus of flowering plants in the myrtle family Myrtaceae, described as a genus in 1853.
- [d8s1]  It is native to the Valdivian temperate rain forests of Chile and Argentina.

**d9: Salvia chamelaeagnea**

- [d9s0] Salvia chamelaeagnea is a species of flowering plant in genus "Salvia", known as sages.
- [d9s1]  It is endemic to South Africa, where it grows on the western coastline of the Cape of Good Hope.
- [d9s2]  It is a shrubby perennial herb up to 6 ft tall and 4 ft wide.
- [d9s3]  It bears 3/4 in light violet-blue flowers with pale lower lips and white throats.
- [d9s4]  The small, green leaves release a slight medicinal odor when brushed.
- [d9s5]  In the wild, the plant grows in sandy soil in streambeds, open fields, and roadsides.
- [d9s6]  It is cultivated for gardens.

**d10: High marsh**

- [d10s0] High marsh is a tidal marsh zone located above the Mean Highwater Mark (MHW) which, in contrast to the low marsh zone, is inundated infrequently during periods of extreme high tide and storm surge associated with coastal storms.
- [d10s1]  The high marsh is the intermittent zone between the low marsh and the uplands, an entirely terrestrial area rarely flooded during events of extreme tidal action caused by severe coastal storms.
- [d10s2]  The high marsh is distinguished from the low marsh by its sandy soil and higher elevation.
- [d10s3]  The elevation of the high marsh allows this zone to be covered by the high tide for no more than an hour a day.
- [d10s4]  With the soil exposed to air for long periods of time, evaporation occurs, leading to high salinity levels, up to four times that of sea water.
- [d10s5]  Areas of extremely high salinity prohibit plant growth altogether.
- [d10s6]  These barren sandy areas are known as "salt pans".
- [d10s7]  Some cordgrass plants do survive here, but are stunted and do not reach their full size.

## 12. hotpotqa_5a861e86554299211dda2a72

原位置：`train` 第 162 题 · 全局第 162 题 · `sample_id: hotpotqa_5a861e86554299211dda2a72`

Question: Do Michel Butor and Joanne Harris share the same nationality?

Note: 

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | nationality of Michel Butor | False | [] | French | [["d5s0"], ["d1s1"]] | context |
| u2 | nationality of Joanne Harris | False | [] | English | [["d8s0"]] | context |
| u3 | whether Michel Butor and Joanne Harris share the same nationality | True | ["u1", "u2"] | no | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | nationality of Michel Butor | False | [] | French | [['d5s0'], ['d1s1']] |
| u2 | nationality of Joanne Harris | False | [] | English | [['d8s0']] |
| u3 | whether Michel Butor and Joanne Harris share the same nationality | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Votre Faust**

- [d1s0] Votre Faust (Your Faust) is an opera (or, more precisely, a "variable fantasy in the style of an opera") in two acts by the Belgian composer Henri Pousseur, for five actors, four singers, twelve instrumentalists, and tape.
- [d1s1]  The text is by the French author Michel Butor.
- [d1s2]  Originally written between 1960 and 1968, it was premiered on 15 January 1969 at the in Milan, and revised in 1981.
- [d1s3]  Although about seven hours of performable material exists, the variable structure does not permit use of it all in a single version, and performances to date have been between three and three-and-a-half hours.

**d2: Gentlemen &amp; Players**

- [d2s0] Gentlemen & Players is a novel by Joanne Harris first published in 2005.
- [d2s1]  A dark psychological thriller, some of the themes may be partly based on Harris' experiences as a teacher at Leeds Grammar School.
- [d2s2]  Set in the present day during Michaelmas term at St Oswald's, a grammar school for boys somewhere in the North of England, the book is a psychological thriller about class distinctions, damaged childhood, secrets, identity and revenge.

**d3: Runemarks**

- [d3s0] Runemarks is a 2007 children's fantasy novel by Joanne Harris.
- [d3s1]  The book was published on 2 August 2007 by Doubleday Publishing and is set in a world where the Norse gods still survive as outlaws, their powers diminished, while a new and more powerful religion, the Order, tries to wipe out magic from the world.
- [d3s2]  Harris has stated that she was inspired to write the book due to her love of Norse mythology as a child, with the book being loosely based on a novel she wrote in her late teens.

**d4: Choi Suchol**

- [d4s0] Choi Suchol was born on May 13, 1958 in Chuncheon, Gangwon-do.
- [d4s1]  After attending Chuncheon High School, Choi received undergraduate and graduate degrees in French Literature from Seoul National University.
- [d4s2]  His doctoral dissertation was on the writings of Michel Butor.
- [d4s3]  He debuted in 1981 by winning the New Spring Literary Contest sponsored by the Chosun Ilbo with his story “Blindspot” (Maengjeom).
- [d4s4]  He has also taught Creative Writing at Hanshin University.

**d5: Michel Butor**

- [d5s0] Michel Butor (] ; 14 September 1926 – 24 August 2016) was a French writer.

**d6: Malbry**

- [d6s0] Malbry ("pronounced ""Mawbry"") is the fictional village that serves as the setting for Joanne Harris' Yorkshire-based thrillers, notably Blueeyedboy, Gentlemen and Players and Different Class .
- [d6s1]  It is also the setting for a number of Harris' short stories.

**d7: Runelight**

- [d7s0] Runelight is a 2011 children's fantasy novel by Joanne Harris and is the second in her RUNE series, following her previous novel, "Runemarks".
- [d7s1]  The book centers on Maddy Smith, and her twin sister, Maggie Rede, both on opposing sides of a war between the new gods and the old, who must both face powerful forces in order to save everything they hold dear.
- [d7s2]  Harris began working on the sequel due to feeling "that it wasn't finished as a story, that there was one chapter in the story that might continue".

**d8: Joanne Harris**

- [d8s0] Joanne Michèle Sylvie Harris, {'1': ", '2': ", '3': ", '4': "} (born 3 July 1964) is an English author, known for her award-winning novel "Chocolat".
- [d8s1]  It was later turned into the 2000 film "Chocolat".

**d9: Second Thoughts (Butor novel)**

- [d9s0] Second Thoughts (French: "La Modification" , 1957) is a novel by Michel Butor.
- [d9s1]  It is the author's most famous work.

**d10: Alain Robbe-Grillet**

- [d10s0] Alain Robbe-Grillet (] ; 18 August 1922 – 18 February 2008) was a French writer and filmmaker.
- [d10s1]  He was one of the figures most associated with the "Nouveau Roman" (new novel) trend of the 1960s, along with Nathalie Sarraute, Michel Butor and Claude Simon.
- [d10s2]  Alain Robbe-Grillet was elected a member of the Académie française on 25 March 2004, succeeding Maurice Rheims at seat No. 32.
- [d10s3]  He was married to Catherine Robbe-Grillet (née Rstakian).

## 13. hotpotqa_5a88ec08554299206df2b3ad

原位置：`train` 第 163 题 · 全局第 163 题 · `sample_id: hotpotqa_5a88ec08554299206df2b3ad`

Question: What are are commonly known as milkworts or snakeroots, Nothofagus or Polygala ?

Note: 保留新拆法

Type: comparison · fallback: False · SFT snapshots: 6

### Adjusted units and annotation

**执行结果：** 保留新顺序及 common name 查询；改为名称值而非旧 yes/no，结论依赖两方。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | common name of Nothofagus | False | [] | southern beeches | [["d4s0"]] | context |
| u2 | common name of Polygala | False | [] | milkworts or snakeroots | [["d8s0", "d8s1"]] | context |
| u3 | which of them are commonly known as milkworts or snakeroots | True | ["u1", "u2"] | Polygala | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Polygala is commonly known as milkworts or snakeroots | False | [] | yes | [['d8s1']] |
| u2 | whether Nothofagus is commonly known as milkworts or snakeroots | False | [] | no | [] |
| u3 | which of Nothofagus and Polygala is commonly known as milkworts or snakeroots | True | ['u1', 'u2'] | Polygala | [[]] |

### Source documents (reference only)

**d1: Polygala lutea**

- [d1s0] Polygala lutea, commonly known as orange- or yellow milkwort, is a herbaceous plant native to the United States.

**d2: Ulmus parvifolia**

- [d2s0] Ulmus parvifolia, commonly known as the Chinese elm or lacebark elm, is a species native to eastern Asia, including China, India, Taiwan, Japan, North Korea, and Vietnam.
- [d2s1]  It has been described as "one of the most splendid elms, having the poise of a graceful "Nothofagus"".

**d3: Polygala nana**

- [d3s0] Polygala nana, commonly known as candyroot or low bachelors' buttons, is a very small herbaceous plant which is native to the southeastern United States.
- [d3s1]  The root has a sweet liquorice flavor when it is chewed, but it is usually hidden underground until the plant flowers.
- [d3s2]  The seeds of candyroot are dispersed by ants.

**d4: Nothofagus**

- [d4s0] Nothofagus, also known as the southern beeches, is a genus of 43 species of trees and shrubs native to the Southern Hemisphere in southern South America (Chile, Argentina) and Australasia (east and southeast Australia, New Zealand, New Guinea and New Caledonia).
- [d4s1]  The species are ecological dominants in many temperate forests in these regions.
- [d4s2]  Some species are reportedly naturalised in Germany and Great Britain.
- [d4s3]  The genus has a rich fossil record of leaves, cupules and pollen, with fossils extending into the late Cretaceous and occurring in Australia, New Zealand, Antarctica and South America.
- [d4s4]  In the past, they were included in the family Fagaceae, but genetic tests revealed them to be genetically distinct, and they are now included in their own family, the Nothofagaceae (literally meaning "false beeches" or "bastard beeches").

**d5: Polygala amarella**

- [d5s0] Polygala amarella (or "P. amara"), commonly known as dwarf milkwort, is a plant of the family Polygalaceae.
- [d5s1]  A European native it grows on chalky grass land and limestone mountain pastures.

**d6: Chalciporus piperatus**

- [d6s0] Chalciporus piperatus, commonly known as the peppery bolete, is a small pored mushroom of the family Boletaceae found in mixed woodland in Europe and North America.
- [d6s1]  It has been recorded under introduced trees in Brazil, and has become naturalised in Tasmania and spread under native "Nothofagus cunninghamii" trees.
- [d6s2]  A small bolete, the fruit body has a 1.6 – orange-fawn cap with cinnamon to brown pores underneath, and a 4 – high by 0.6 – thick stipe.
- [d6s3]  The rare variety "hypochryseus", found only in Europe, has yellow pores and tubes.

**d7: Fuscospora alessandri**

- [d7s0] Fuscospora alessandrii (ruil) is a species of plant in the family Nothofagaceae, commonly known as the southern beeches.
- [d7s1]  It is endemic to Chile, occurring chiefly in the Chilean matorral ecoregion.
- [d7s2]  It is threatened by habitat loss.
- [d7s3]  The species is protected within Los Ruiles National Reserve.
- [d7s4]  It was known as "Nothofagus alessandrii" prior to 2013.

**d8: Polygala**

- [d8s0] Polygala is a large genus of flowering plants belonging to the family Polygalaceae.
- [d8s1]  They are commonly known as milkworts or snakeroots.
- [d8s2]  The genus is distributed widely throughout much of the world in temperate zones and the tropics.
- [d8s3]  The genus name "Polygala" comes from the ancient Greek "much milk", as the plant was thought to increase milk yields in cattle.

**d9: Fuscospora fusca**

- [d9s0] Fuscospora fusca, commonly known as red beech (Māori: tawhai raunui) is a species of southern beech, endemic to New Zealand, where it occurs on both the North Island and South Island.
- [d9s1]  Generally it is found on lower hills and inland valley floors where soil is fertile and well drained.
- [d9s2]  It was known as "Nothofagus fusca" prior to 2013.

**d10: Cyttaria gunnii**

- [d10s0] Cyttaria gunnii, commonly known as the myrtle orange or beech orange, is an orange-white coloured and edible ascomycete fungus native to Australasia.
- [d10s1]  It is a specific parasite of myrtle beech ("Nothofagus cunninghamii") trees.

## 14. hotpotqa_5a899d165542993b751ca961

原位置：`train` 第 164 题 · 全局第 164 题 · `sample_id: hotpotqa_5a899d165542993b751ca961`

Question: Which case is cited as the business purpose doctrine: Gregory v. Helvering or Ableman v. Booth?

Note: 

Type: comparison · fallback: False · SFT snapshots: 4

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | whether Gregory v. Helvering is cited as the business purpose doctrine | False | [] | yes | [["d10s1"]] | context |
| u2 | whether Ableman v. Booth is cited as the business purpose doctrine | False | [] | no | [] | no_direct_support |
| u3 | which case is cited as the business purpose doctrine | True | ["u1", "u2"] | Gregory v. Helvering | [[]] | question_presupposition |

- u2：无直接支持集合；不能仅由 expected_answer 将本单元标为 SUPPORTED。候选题结论可按独立的 presupposition_sets 路径判断。

- u3：`by_presupposition=true`，预设路径 `[["d10s1"]]`；不是直接证据。

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Gregory v. Helvering is cited as the business purpose doctrine | False | [] | yes | [['d10s1']] |
| u2 | whether Ableman v. Booth is cited as the business purpose doctrine | False | [] | no | [] |
| u3 | which of Gregory v. Helvering and Ableman v. Booth is cited as the business purpose doctrine | True | ['u1', 'u2'] | Gregory v. Helvering | [[]] |

### Source documents (reference only)

**d1: Criminal law in the Taney Court**

- [d1s0] The Taney Court (1836–1864) heard thirty criminal law cases, approximately one per year.
- [d1s1]  Notable cases include "Prigg v. Pennsylvania" (1842), "United States v. Rogers" (1846), "Ableman v. Booth" (1858), "Ex parte Vallandigham" (1861), and "United States v. Jackalow" (1862).

**d2: Organizational intelligence**

- [d2s0] Organizational Intelligence (OI) is the capability of an organization to comprehend and conclude knowledge relevant to its business purpose.
- [d2s1]  In other words, it is the intellectual capacity of the entire organizations.
- [d2s2]  With relevant organizational intelligence comes great potential value for companies and therefore organizations find study where their strengths and weaknesses lie in responding to change and complexity.
- [d2s3]  Organizational Intelligence embraces both knowledge management and organizational learning, as it is the application of knowledge management concepts to a business environment, additionally including learning mechanisms, comprehension models and business value network models, such as the balanced scorecard concept.
- [d2s4]  Organizational Intelligence consists of the ability to make sense of complex situations and act effectively, to interpret and act upon relevant events and signals in the environment.
- [d2s5]  It also includes the ability to develop, share and use knowledge relevant to its business purpose as well as the ability to reflect and learn from experience

**d3: Hoffman v. Jones**

- [d3s0] Hoffman v. Jones, (Fla. 1973), was a case decided by the Supreme Court of Florida that was the first adoption of the comparative negligence rule in negligence law through judicial decision as opposed to adoption through statute.
- [d3s1]  In the wrongful death case of Hoffman v. Jones, attorney Sammy Cacciatore Jr. was instrumental in causing the Florida Supreme Court to adopt for the first time the comparative negligence rule in negligence law.William Harrison Jones Jr. was killed by a Pav-A-Way Corporation truck driven by Philip Francis Hoffman Jr.
- [d3s2]  It was the first case in the nation in which a state supreme court abandoned the almost-150-year-old doctrine of contributory negligence, which precluded an injured victim from recovery if the victim had contributed to the incident to any degree.
- [d3s3]  The Florida Supreme Court adopted the concept of “pure” comparative negligence, which allows a victim to be compensated for the percentage of harm caused by the at-fault person.
- [d3s4]  The decision of the court in Hoffman v. Jones has been cited in law school textbooks, and now the concept of comparative negligence is the prevailing doctrine.

**d4: Gregory V of Constantinople**

- [d4s0] Gregory V (Γρηγόριος Ε΄, born "Georgios Angelopoulos") was Ecumenical Patriarch of Constantinople from 1797 to 1798, from 1806 to 1808 and from 1818 to 1821.
- [d4s1]  He was responsible for much restoration work to the Patriarchal Cathedral of St George, which had been badly damaged by fire in 1738.
- [d4s2]  At the onset of the Greek War of Independence, as Ethnarch of the Orthodox Millet Gregory V was blamed by Ottoman Sultan Mahmud II for his inability to suppress the Greek uprising, even though he had actually condemned the Greek revolutionary activities so as to protect the Greeks of Constantinople from reprisals by the Ottoman Turks.
- [d4s3]  The reprisals did come during Holy Week in April 1821, after the Greek rebels scored several successes against the Ottoman forces in the Peloponnese.

**d5: Ableman v. Booth**

- [d5s0] Ableman v. Booth, 62 U.S. 506 (1859) , was a United States Supreme Court case in which the Court held that State courts cannot issue rulings on federal law that contradict the decisions of federal courts, overturning a decision by the Supreme Court of Wisconsin.
- [d5s1]  The Supreme Court held that under the Constitution, the federal courts have the final power to decide cases arising under the Constitution and federal statutes, and that the States do not have the power to overturn those decisions.
- [d5s2]  Thus, Wisconsin did not have the authority to nullify federal judgments or statutes.

**d6: Gregory v. Hartley**

- [d6s0] Gregory v. Hartley, 113 U.S. 742 (1885) , was a case in error to the Supreme Court of the State of Nebraska where it was decided and reaffirmed that the words "term at which said cause could be first tried and before the trial thereof," Act of March 3, 1875, c. 137, § 3, 18 Stat.
- [d6s1]  471, mean the first term at which the cause is in law triable, i.e., in which it would stand for trial if the parties had taken the usual steps as to pleadings and other preparations.
- [d6s2]  Babbitt v. Clark, 103 U. S. 808, and "Pullman Palace Car Co. v. Speck", ante, 113 U. S. 87.

**d7: Step transaction doctrine**

- [d7s0] The step transaction doctrine is a judicial doctrine in the United States that combines a series of formally separate steps, resulting in tax treatment as a single integrated event.
- [d7s1]  The doctrine is often used in combination with other doctrines, such as substance over form.
- [d7s2]  The doctrine is applied to prevent tax abuse, such as tax shelters or bailing assets out of a corporation.
- [d7s3]  The step transaction doctrine originated from a common law principle in "Gregory v. Helvering", 293 U.S. 465 (1935), which allowed the court to recharacterize a tax-motivated transaction.

**d8: Helvering v. Horst**

- [d8s0] Helvering v. Horst, 311 U.S. 112 (1940) , is an opinion of the United States Supreme Court which further developed the “fruit-and-tree” metaphor established in "Lucas v. Earl", 281 U.S. 111 (1930) .
- [d8s1]  "Horst" is the leading case that applies the assignment of income doctrine to income from property.

**d9: Gregory v Rangitikei**

- [d9s0] Gregory v Rangitikei [1995] 2 NZLR 208, (1994) 6 TCLR 199 is a cited case in New Zealand regarding the sale of property by tender, confirming that an offer inviting tenders to be submitted for the purchase of something did not amount to an offer capable of acceptance to sell that property, but instead merely amounted to an invitation to treat.
- [d9s1]  It reinforces the English case of Spencer v Harding (1870) LR 5 CP 561.
- [d9s2]  However the Court also ruled that there was a breach of the Fair Trading Act (1986).

**d10: Gregory v. Helvering**

- [d10s0] Gregory v. Helvering, 293 U.S. 465 (1935), was a landmark decision by the United States Supreme Court concerned with U.S. income tax law.
- [d10s1]  The case is cited as part of the basis for two legal doctrines: the business purpose doctrine and the doctrine of substance over form.
- [d10s2]  The business purpose doctrine is essentially that where a transaction has no substantial business purpose other than the tax avoidance and tax evasion|avoidance or reduction]] of Federal tax, the tax law will not regard the transaction.
- [d10s3]  The doctrine of substance over form is essentially that, for Federal tax purposes, a taxpayer is bound by the economic substance of a transaction where the economic substance varies from its legal form.

## 15. hotpotqa_5a8ad70d5542992d82986f94

原位置：`train` 第 165 题 · 全局第 165 题 · `sample_id: hotpotqa_5a8ad70d5542992d82986f94`

Question: American producer K.E. on the Track worked with Fetty Wap on a song named after which shoemaker?

Note: 题目预设“以某位鞋匠命名”，并不足以单独证明那位鞋匠就与歌名完全同名，标签应该依据context

Type: bridge · fallback: False · SFT snapshots: 5

### Adjusted units and annotation

**执行结果：** 按 Note 严格依据 context。u1 为歌曲 Jimmy Choo；u2 无命名关系直接证据，取消预设路径，答案留空，完整 context 下仍为 UNRESOLVED。旧 gold 的 Jimmy Choo 仅作历史参考。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | song by Fetty Wap produced by K.E. on the Track | False | [] | Jimmy Choo | [["d4s0", "d4s1"]] | context |
| u2 | shoemaker after whom the song is named, given {u1} | True | ["u1"] | null（证据不足） | [] | no_direct_support |

- u2：context 不支持鞋匠身份及命名关系；答案留空，不能标为 SUPPORTED，也不能标为 CONTRADICTED。

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | song by Fetty Wap produced by K.E. on the Track | False | [] | Jimmy Choo | [['d4s0', 'd4s1']] |
| u2 | shoemaker after whom {u1} is named | True | ['u1'] | Jimmy Choo | [] |

### Source documents (reference only)

**d1: Fetty Wap (album)**

- [d1s0] Fetty Wap is the eponymous debut studio album by American rapper Fetty Wap.
- [d1s1]  It was released on September 25, 2015, by RGF Productions, distributed by Because Music and 300 Entertainment.
- [d1s2]  The album features guest appearances from Remy Boyz, Monty and M80.
- [d1s3]  Both Monty and M80, who were members of the Remy Boyz, contributed as featured guest artists on the album.

**d2: The One (Tamar Braxton song)**

- [d2s0] "The One" is a song by American R&B recording artist Tamar Braxton.
- [d2s1]  Written by Braxton, Yung Berg, Shaunice Lasha Jones, LaShawn Daniels, and its producer K.E. on the Track, the song contains samples from Juicy Fruit by Mtume.
- [d2s2]  The song also contains re-sung lyrics from The Notorious B.I.G.'s "Juicy", which also sampled Juicy Fruit.
- [d2s3]  It was released as the second single on May 7, 2013 from her second studio album "Love and War" (2013).

**d3: My Way (Fetty Wap song)**

- [d3s0] "My Way" is the third single by American rapper Fetty Wap, featuring Remy Boyz's RGF Productions' member Monty, from Wap's self-titled debut album.
- [d3s1]  It peaked at number seven on the "Billboard" Hot 100.

**d4: Jimmy Choo (song)**

- [d4s0] "Jimmy Choo" is a song by American rapper Fetty Wap for his upcoming album "King Zoo".
- [d4s1]  It was released on February 5, 2016 and was produced by K.E. on the Track.

**d5: Fetty Wap**

- [d5s0] Willie Maxwell II (born June 7, 1991) is an American rapper better known by his stage name Fetty Wap.
- [d5s1]  He rose to prominence after his debut single "Trap Queen", reached number two on the U.S. "Billboard" Hot 100 chart in May 2015.
- [d5s2]  This helped Fetty Wap secure a record deal with 300 Entertainment, a record label distributed by Atlantic Records.
- [d5s3]  He subsequently released two Top 10 singles in the U.S., "679" and "My Way".
- [d5s4]  Fetty Wap's eponymously titled debut album was released in September 2015 and reached number one on the U.S. "Billboard" 200 chart.

**d6: Wake Up (Fetty Wap song)**

- [d6s0] "Wake Up" is a song by American hip hop recording artist Fetty Wap for his upcoming of the album King Zoo.
- [d6s1]  The song was released on April 20, 2016 by RGF Productions and 300 Entertainment.
- [d6s2]  The track was produced by Frenzy.
- [d6s3]  It was certified Gold by the RIAA on November 14, 2016.

**d7: Westside (Fetty Wap song)**

- [d7s0] "Westside" is a song by American rapper Fetty Wap featuring Snoop Dogg for his upcoming of the album King Zoo.
- [d7s1]  The song was released on June 3, 2016 by RGF Productions and 300 Entertainment.
- [d7s2]  The track was produced by London on da Track.

**d8: Asking 4 It**

- [d8s0] "Asking 4 It" is a song by American singer and songwriter Gwen Stefani from her third studio album, "This Is What the Truth Feels Like" (2016).
- [d8s1]  The song features guest vocals from American rapper Fetty Wap.
- [d8s2]  It was released on March 18, 2016, as the ninth track on "This Is What the Truth Feels Like" by Interscope Records.
- [d8s3]  The track was written by Stefani, Justin Tranter, Julia Michaels, Tor Hermansen, Mikkel Eriksen, and Fetty Wap.
- [d8s4]  The track's production was handled by Stargate, while additional production was made by Tim Blacksmith and Danny D.

**d9: Bang My Head**

- [d9s0] "Bang My Head" is a song by French DJ and music producer David Guetta, featuring vocals from Australian singer Sia and American rapper Fetty Wap.
- [d9s1]  It was released as the second single from the re-release of Guetta's sixth studio album, "Listen".
- [d9s2]  "Bang My Head" tallies as the album's seventh single overall.
- [d9s3]  It was released via digital download on 30 October 2015.
- [d9s4]  The original album version of the song only featured Sia's vocals, but the second verse was later replaced with vocals from Fetty Wap for the reworked single release.

**d10: K.E. on the Track**

- [d10s0] Kevin Erondu, better known as K.E. on the Track, is an American record producer.

## 16. hotpotqa_5a8ad7ae5542992d82986f97

原位置：`train` 第 166 题 · 全局第 166 题 · `sample_id: hotpotqa_5a8ad7ae5542992d82986f97`

Question: Are Friedman Memorial Airport and Watertown International Airport in the same state?

Note: 

Type: comparison · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | state of Friedman Memorial Airport | False | [] | Idaho | [["d3s0"], ["d8s2"]] | context |
| u2 | state of Watertown International Airport | False | [] | New York | [["d7s0"]] | context |
| u3 | whether Friedman Memorial Airport and Watertown International Airport are in the same state | True | ["u1", "u2"] | no | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | state in which Friedman Memorial Airport is located | False | [] | Idaho | [['d3s0'], ['d8s2']] |
| u2 | state in which Watertown International Airport is located | False | [] | New York | [['d7s0']] |
| u3 | whether Friedman Memorial Airport and Watertown International Airport are in the same state | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Wiley Post–Will Rogers Memorial Airport**

- [d1s0] Wiley Post–Will Rogers Memorial Airport, (IATA: BRW, ICAO: PABR, FAA LID: BRW) often referred to as Post/Rogers Memorial is a public airport located in Utqiaġvik, a city in the North Slope Borough of the U.S. state of Alaska.
- [d1s1]  The airport is owned by the state.
- [d1s2]  Situated on the Chukchi Sea at a latitude of 71.29°N, the airport is the farthest north of any in US territory.
- [d1s3]  The airport is named after American humorist Will Rogers and aviator Wiley Post, both of whom died about 9 mi away at Point Barrow in a 1935 airplane crash.

**d2: Ketchum, Idaho**

- [d2s0] Ketchum is a city in Blaine County, Idaho, United States, in the central part of the state.
- [d2s1]  The population was 2,689 at the 2010 census, down from 3,003 in 2000.
- [d2s2]  Located in the Wood River Valley, Ketchum is adjacent to Sun Valley and the communities share many resources; both sit in the same valley beneath Bald Mountain, with its world-famous skiing.
- [d2s3]  The city also draws tourists from around the world to enjoy its fishing, hiking, trail riding, tennis, shopping, art galleries, and more.
- [d2s4]  The airport for Ketchum, Friedman Memorial Airport, is approximately 15 mi south in Hailey.

**d3: Friedman Memorial Airport**

- [d3s0] Friedman Memorial Airport (IATA: SUN, ICAO: KSUN, FAA LID: SUN) is a city-owned public-use airport in the northwest United States, located one nautical mile (2 km) southeast of the central business district of Hailey, the county seat of Blaine County, Idaho.
- [d3s1]  The airport is operated by the Friedman Memorial Airport Authority under a Joint Powers Agreement between the city of Hailey and Blaine County.
- [d3s2]  It serves the resort communities of Sun Valley and Ketchum, and the surrounding areas in the Wood River Valley.

**d4: Peach State Airport**

- [d4s0] Alexander Memorial Airport (FAA LID: GA2) , also known as Peach State Aerodrome or Candler Field, is a public grass strip located 1 mile (1.6 km) west of Williamson, Georgia, in the United States.
- [d4s1]  Alexander Memorial Airport is located in picturesque rural Pike County, 27 nautical miles (50 km) south of Hartsfield-Jackson Atlanta International Airport.

**d5: Sun Valley, Idaho**

- [d5s0] Sun Valley is a resort city in Blaine County in central Idaho, in the western United States.
- [d5s1]  The resort is adjacent to the city of Ketchum and within the greater Wood River valley.
- [d5s2]  The population was 1,406 at the 2010 census, down from 1,427 in 2000.
- [d5s3]  The elevation of Sun Valley (at the Lodge) is 5920 ft above sea level.
- [d5s4]  The area is served by Friedman Memorial Airport in Hailey, approximately 15 mi south.
- [d5s5]  Visitors to Sun Valley are relatively close to the Sawtooth National Recreation Area, accessed over Galena Summit on Highway 75, the "Sawtooth Scenic Byway."

**d6: New York State Route 12F**

- [d6s0] New York State Route 12F (NY 12F) is an east–west state highway in Jefferson County, New York, in the United States.
- [d6s1]  It extends for 6.89 mi from an intersection with NY 180 in the town of Hounsfield to a junction with U.S. Route 11 (US 11) and NY 12 in the city of Watertown.
- [d6s2]  The route follows a parallel routing to that of NY 12E between the vicinity of the village of Dexter and the city of Watertown.
- [d6s3]  While NY 12E runs along the north side of the Black River through this area, NY 12F follows the southern bank.
- [d6s4]  Just east of NY 180, NY 12F serves Watertown International Airport.

**d7: Watertown International Airport**

- [d7s0] Watertown International Airport (IATA: ART, ICAO: KART, FAA LID: ART) is a county owned, public use airport located in Jefferson County, New York, United States.
- [d7s1]  It is located five nautical miles (6 mi, 9 km) west of the central business district of Watertown.
- [d7s2]  The airport is mostly used for general aviation, but has scheduled passenger service provided by one commercial airline and subsidized by the Essential Air Service program.
- [d7s3]  The airport does not provide any scheduled international passenger flights, but is available as an international port of entry for private aircraft on two hours advance notice to customs from pilots.

**d8: Hailey, Idaho**

- [d8s0] Hailey is a city in and the county seat of Blaine County, in the Wood River Valley of the central part of the U.S. state of Idaho.
- [d8s1]  The population was 7,960 at the 2010 census, up from 6,200 in 2000.
- [d8s2]  Hailey is the site of Friedman Memorial Airport (SUN), the airport for the resort area of Sun Valley/Ketchum, 12 mi north.
- [d8s3]  The town of Bellevue is a few miles south.
- [d8s4]  From 1882 to 1895, Hailey was the county seat of now-defunct Alturas County.

**d9: Waukegan National Airport**

- [d9s0] Waukegan National Airport (IATA: UGN, ICAO: KUGN, FAA LID: UGN) is a public use airport located in Waukegan, a city in Lake County, Illinois, United States.
- [d9s1]  The airport is 35 nmi north of the central business district of Chicago.
- [d9s2]  It was originally named Waukegan Memorial Airport.
- [d9s3]  It has been operated by the Waukegan Port District since 1956 and is the second busiest airport in Illinois for international arrivals.
- [d9s4]  In January 2014 under a FAA reclassification of the airport and many others smaller airports across the United States, the airport was renamed Waukegan National Airport

**d10: Nantucket Memorial Airport**

- [d10s0] Nantucket Memorial Airport (IATA: ACK, ICAO: KACK, FAA LID: ACK) is a public airport on the south side of the island of Nantucket in the U.S. state of Massachusetts.
- [d10s1]  The airport is owned by the Town of Nantucket and is located three miles (5 km) southeast of the town center.
- [d10s2]  It is the second-busiest airport in the state, after Logan International Airport due to intense corporate travel to and from the island in the busy summer months.

## 17. hotpotqa_5a8b848d5542997f31a41d5c

原位置：`train` 第 167 题 · 全局第 167 题 · `sample_id: hotpotqa_5a8b848d5542997f31a41d5c`

Question: Are Haig P. Manoogian and Luther George Simjian both professors?

Note: 

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | whether Haig P. Manoogian is a professor | False | [] | yes | [["d2s0"]] | context |
| u2 | whether Luther George Simjian is a professor | False | [] | no | [["d9s0"]] | definition_omission |
| u3 | whether both Haig P. Manoogian and Luther George Simjian are professors | True | ["u1", "u2"] | no | [[]] | derived_from_dependencies |

- u2：`by_omission=true`，沿用定义性介绍省略规则，不是文中明确否定。

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Haig P. Manoogian is a professor | False | [] | yes | [['d2s0']] |
| u2 | whether Luther George Simjian is a professor | False | [] | no | [['d9s0']] |
| u3 | whether Haig P. Manoogian and Luther George Simjian are both professors | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Lawrence D. Reddick**

- [d1s0] Lawrence Dunbar Reddick (March 3, 1910 – August 2, 1995) was an African-American historian and professor who wrote the first biography of Martin Luther King Jr., strengthened major archives of African-American history resources at Atlanta University Center and the New York Public Library, and was fired by Alabama’s state board of education for his support for student sit-ins at Alabama State College—an event that earned him honor for his courage and brought Alabama State College censure by the American Association of University Professors.

**d2: Haig P. Manoogian**

- [d2s0] Haig Manoogian (May 23, 1916 – May 26, 1980) was an Armenian-American professor of film at New York University and a major early influence for many filmmakers such as Martin Scorsese, who was a student of his.

**d3: Venkat Rangan**

- [d3s0] P. Venkat Rangan is an Indian computer scientist.
- [d3s1]  He is the current vice chancellor of Amrita University.
- [d3s2]  A pioneer of research in Multimedia Systems, he was the founder and director of the Multimedia Laboratory at the University of California, San Diego, where he served as a Professor of Computer Science and Engineering.
- [d3s3]  By the age of 33 he was one of the youngest full professors at University of California, San Diego.
- [d3s4]  Dr. Rangan also founded Yodlee Inc. and served as its CEO, for which in 2000, he was selected as one of the 25 best entrepreneurs by the President of the US and featured on the July 2000 cover of Internet World Magazine.

**d4: George von Kunheim**

- [d4s0] George von Kunheim (July 1523 – 18 October 1611), born in the Prussian city of Wehlau (modern Znamensk) and died in Mühlhausen (modern Gvardeyskoye), married Margaretha Luther, daughter and child of Paul Luther and grandchild of Martin Luther on August 5, 1555.

**d5: Clubscene**

- [d5s0] Clubscene is a short film by Italian-Canadian filmmaker Adriano Valentini and features Mystery Hunters star Christina Broccolini.
- [d5s1]  Shot in April 2008, "Clubscene"was Valentini's Advanced Film Project while studying under director Susan Seidelman at NYU's Tisch School of the Arts.
- [d5s2]  In 2009, the film was awarded the Wasserman/King Finalist Award as well as the Craft Award in Screenwriting at NYU's First Run Film Festival.
- [d5s3]  The film was then invited to be screened at the prestigious 2009 Haig P. Manoogian Screenings at the Directors Guild of America Theater in Los Angeles.
- [d5s4]  Following its success, the films creators have begun adapting the concept into a web series, further exploring the world and characters.

**d6: The Dungeonmaster**

- [d6s0] The Dungeonmaster (originally Ragewar: The Challenges of Excalibrate and Digital Knights) is a 1984 low-budget science fiction/fantasy film, rated PG-13, starring Jeffrey Byron, Richard Moll and Leslie Wing.
- [d6s1]  The film is produced by Charles Band, and is split up into seven distinct story segments, each written and directed by a different person: Dave Allen, Charles Band, John Carl Buechler, Steven Ford, Peter Manoogian, Ted Nicolaou, and Rosemarie Turko.
- [d6s2]  The film's theme was influenced by the popularity of Disney's 1982 film "Tron" and the roleplaying game Dungeons and Dragons.
- [d6s3]  Principal filming began in 1983 but the film was not completed until 1984.
- [d6s4]  The film features an appearance by the heavy metal band W.A.S.P..
- [d6s5]  A sequel segment was planned for the anthology "Pulse Pounders", but the unfinished film was never released due to the collapse of Empire Pictures.

**d7: Leipzig Debate**

- [d7s0] The Leipzig Debate (German: "Leipziger Disputation" ) was a theological disputation originally between Andreas Karlstadt, Martin Luther, Philipp Melanchthon, and Johann Eck.
- [d7s1]  Eck, a defender of Catholic doctrine and a highly respected Dominican friar, had challenged Karlstadt, a Christian theologian, to a public debate concerning the doctrines of free will and grace.
- [d7s2]  The Leipzig Debate took place in June and July 1519 at Pleissenburg Castle in Leipzig, Germany.
- [d7s3]  Its purpose was to discuss Martin Luther's teachings, and was initiated and conducted in the presence of George, Duke of Saxony, an opponent of Luther.
- [d7s4]  Eck, considered the master debater in Germany, was concerned about clerical abuses, but his life's work had been dedicated to the defence of Catholic teachings and combating heresy.

**d8: Pressure (play)**

- [d8s0] Pressure is a play written by David Haig.
- [d8s1]  It made its world premiere at the Royal Lyceum Theatre, Edinburgh in May 2014, a year later than originally planned, before transferring to the Chichester Festival at the end of the same month.
- [d8s2]  The play centres on the true story of James Stagg and Operation Overlord, in particular the weather-forecasting for the D-Day landings and the resultant tensions between Dwight D. Eisenhower, James Stagg and Irving P. Krick.

**d9: Luther George Simjian**

- [d9s0] Luther George Simjian (Armenian: Լութեր Ճորճ (Կարապետ) Սիմճեան ) (January 28, 1905 – October 23, 1997) was an Armenian-American inventor of numerous devices and owner of over 200 patents.

**d10: George Haig, 2nd Earl Haig**

- [d10s0] George Alexander Eugene Douglas Haig, 2nd Earl Haig (15 March 1918 – 9 July 2009) was a British artist and peer who succeeded to the Earldom of Haig on 29 January 1928, at the age of nine, upon the death of his father, Field Marshal the 1st Earl Haig.
- [d10s1]  Until then he was styled Viscount Dawick.
- [d10s2]  Throughout his life, he was usually known to his family and friends as Dawyck Haig.

## 18. hotpotqa_5a8b85f355429971feec4731

原位置：`train` 第 168 题 · 全局第 168 题 · `sample_id: hotpotqa_5a8b85f355429971feec4731`

Question: Jean-Baptiste Andrea wrote and directed what 2003 French horror drama that was remade in 2014?

Note: 我觉得旧gold的拆分结构是合理的，你再检查一下

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 采用用户要求的两单元结构；去掉旧描述泄露的 Mumbai 125 KM，第一步验证 2014 年翻拍与 2003 年原作，第二步验证编导。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | 2003 film that was remade in 2014 | False | [] | Dead End | [["d2s0", "d2s1"]] | context |
| u2 | film written and directed by Jean-Baptiste Andrea, given {u1} | True | ["u1"] | Dead End | [["d8s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | 2003 film of which Mumbai 125 KM is a remake | False | [] | Dead End | [['d2s1']] |
| u2 | film written and directed by Jean-Baptiste Andrea, given {u1} | True | ['u1'] | Dead End | [['d8s0']] |

### Source documents (reference only)

**d1: Among the Living (2014 film)**

- [d1s0] Among the Living (French: Aux yeux des vivants ) is a 2014 French horror film written and directed by Julien Maury and Alexandre Bustillo.
- [d1s1]  The film had its world premiere on 10 March 2014 at South by Southwest and follows three young boys who discover that the seemingly banal exterior of their town hides a horrific inner secret.

**d2: Mumbai 125 KM**

- [d2s0] Mumbai 125 KM is a 2014 Indian horror film directed by Hemant Madhukar and starring Karanvir Bohra, Vedita Pratap Singh, Joey Debroy, Vije Bhatia in leads whilst Veena Malik played the main antagonist.
- [d2s1]  It is a remake of 2003 movie "Dead End".

**d3: Jean-Baptiste Andrea**

- [d3s0] Jean-Baptiste Andrea is a French film director and screenwriter.
- [d3s1]  He grew up in Cannes, where he started making short films.
- [d3s2]  He later moved to Paris and graduated in political science and economics.
- [d3s3]  In Paris, he met Fabrice Canepa, and the two of them began writing films together.
- [d3s4]  Together, they wrote and directed "Dead End".

**d4: The Awful Dr. Orloff**

- [d4s0] The Awful Dr. Orloff (Spanish: Gritos en la noche ) is a 1962 Spanish–French horror film directed by Jesús Franco.
- [d4s1]  It stars Howard Vernon as the mad Dr. Orloff (or sometimes Orlof) who wants to repair his disfigured daughter's face with skin grafts from others, with the aid of a slavish blind henchman named Morpho.
- [d4s2]  The film is considered to be the earliest Spanish horror film.
- [d4s3]  Howard Vernon continued to appear in a number of Franco's horror films up until his death.
- [d4s4]  Franco would later feature a number of blind or disfigured henchmen named Morpho in many of his later horror films, such as "Vampyos Lesbos" and "Revenge in the House of Usher".

**d5: High Tension**

- [d5s0] High Tension (French: Haute Tension, ] ; released in the United Kingdom as Switchblade Romance) is a 2003 French horror film directed by Alexandre Aja, stars Cécile de France, Maïwenn, and Philippe Nahon.

**d6: Big Nothing**

- [d6s0] Big Nothing is a 2006 British-Canadian black comedy crime film directed by Jean-Baptiste Andrea starring David Schwimmer and Simon Pegg.
- [d6s1]  It was released in December 2006, and had its premiere at Cardiff Film Festival in November 2006.

**d7: Playing 'In the Company of Men'**

- [d7s0] Playing <nowiki>'In the Company of Men'</nowiki> (French: "En jouant <nowiki>'Dans la compagnie des hommes'</nowiki>" or French: "Léo, en jouant <nowiki>'Dans la compagnie des hommes'</nowiki>" ) is a 2003 French drama film directed by Arnaud Desplechin.
- [d7s1]  It was screened in the Un Certain Regard section at the 2003 Cannes Film Festival.

**d8: Dead End (2003 film)**

- [d8s0] Dead End is a 2003 French horror drama film written and directed by Jean-Baptiste Andrea and Fabrice Canepa.
- [d8s1]  Although "Dead End" only had a budget of $900,000 it made a total of $77 million from DVD sales.

**d9: Tender Dracula**

- [d9s0] Tender Dracula, or Confessions of a Blood Drinker (French: Tendre Dracula ) is a 1974 French horror film directed by Pierre Grunstein.
- [d9s1]  The film stars Peter Cushing, Alida Valli and Miou-Miou.
- [d9s2]  The film involves two scriptwriters and two girls who are ordered by their director to visit the castle home of a horror actor (Peter Cushing) and to talk him out of his intention to change from horror films to romantic ones.
- [d9s3]  The longer they stay in the castle, the more likely it seems that the actor is an actual vampire.

**d10: Inside (2007 film)**

- [d10s0] Inside (French: "À l'intérieur" ) is a 2007 French home invasion horror film directed by Julien Maury and Alexandre Bustillo, starring Alysson Paradis and Béatrice Dalle.
- [d10s1]  It was written by co-director Bustillo, and is the first feature film from either director.
- [d10s2]  It concerns the attack and home invasion of a young pregnant woman by a mysterious stranger who seeks to take her unborn baby.
- [d10s3]  The film received generally positive reviews from mainstream critics upon its release and was particularly well received among horror film critics, noting it for being a genuinely scary and brutally violent example of the new wave of French horror.

## 19. hotpotqa_5a8dd9b8554299068b959e06

原位置：`train` 第 169 题 · 全局第 169 题 · `sample_id: hotpotqa_5a8dd9b8554299068b959e06`

Question: What islands are home to Rhinosolea microlepidota and are known in Japanese as the "Nansei" Islands?

Note: 应该拆分成两个unit，是否合理

Type: bridge · fallback: False · SFT snapshots: 7

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | islands around which Rhinosolea microlepidota is native | False | [] | Ryukyu Islands | [["d9s0"]] | context |
| u2 | islands home to Rhinosolea microlepidota that are known in Japanese as the "Nansei" Islands, given {u1} | True | ["u1"] | Ryukyu Islands | [["d4s0"], ["d6s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | islands around which Rhinosolea microlepidota is native | False | [] | Ryukyu Islands | [['d9s0']] |
| u2 | islands home to Rhinosolea microlepidota that are known in Japanese as the "Nansei" Islands, given {u1} | True | ['u1'] | Ryukyu Islands | [['d4s0'], ['d6s0']] |

### Source documents (reference only)

**d1: Faroe Islands women's national football team**

- [d1s0] The Faroe Islands women's national football team represents the Faroe Islands in women's association football and is controlled by the Faroe Islands Football Association (FSF), the governing body of all football in the Faroe Islands.
- [d1s1]  The FSF became a member of International Federation of Association Football (FIFA) in 1988 and Union of European Football Associations (UEFA) in 1990.
- [d1s2]  By population it remains the fourth smallest member of UEFA, which encompasses the countries of Europe.
- [d1s3]  The women's team played their first FIFA-sanctioned international match in 1995 and have never advanced to the finals of the FIFA Women's World Cup or UEFA Women's Championship.
- [d1s4]  They took part in the Island Games in 2001, 2003 and 2005 and won all three tournaments, as well as appearing at the 2010 edition of the Algarve Cup.
- [d1s5]  In the Faroe Islands the team is known as the "Kvinnulandsliðið".
- [d1s6]  As the Faroe Islands has no national stadium, the women's team have staged their home matches at different grounds throughout the country.

**d2: Yaeyama language**

- [d2s0] The Yaeyama language (八重山物言/ヤイマムニ , "Yaimamuni") is a Southern Ryukyuan language spoken in the Yaeyama Islands, the southernmost inhabited island group in Japan, with a combined population of about 53,000.
- [d2s1]  The Yaeyama Islands are situated in the Southern Ryukyu Islands, southwest of the Miyako Islands and to the east of Taiwan.
- [d2s2]  Yaeyama ("Yaimamunii") is most closely related to Miyako.
- [d2s3]  The number of competent native speakers is not known; as a consequence of Japanese language policy which refers to the language as the Yaeyama dialect (八重山方言 , Yaeyama hōgen ) , reflected in the education system, people below the age of 60 tend to not use the language except in songs and rituals, and the younger generation exclusively uses Japanese as their first language.
- [d2s4]  As compared to the Japanese "kokugo," or Japanese national language, other Ryukyuan languages such as Okinawan and Amami have also been referred to as dialects of Japanese.
- [d2s5]  Yaeyama is noted as having a comparatively lower "language vitality" among neighboring Ryukyuan languages.

**d3: Governor of the South Pacific Mandate**

- [d3s0] The Governor of the South Pacific Mandate (officially known as the Director of the South Sea Agency) was an official who ruled the Japanese South Pacific Mandate, a League of Nations mandate in the Pacific Ocean under the administration of the Empire of Japan, between 1922 and 1944.
- [d3s1]  The territory consisted of islands awarded to Japan by the League of Nations after World War I, prior to which they had been part of the German colonial empire.
- [d3s2]  During World War II, the United States captured the islands from Japan.
- [d3s3]  After World War II, the United Nations placed the territory under the United States trusteeship as the Trust Territory of the Pacific Islands.
- [d3s4]  The islands are now part of Palau, Northern Mariana Islands, Federated States of Micronesia, and Marshall Islands.

**d4: Ryukyu Islands**

- [d4s0] The Ryukyu Islands (琉球諸島 , Ryūkyū-shotō ) , more commonly known in Japanese as the "Nansei" Islands (南西諸島 , Nansei-shotō , lit.
- [d4s1]  "Southwest Islands") and also known as the Ryukyu Arc (琉球弧 , Ryūkyū-ko ) , are a chain of Japanese islands that stretch southwest from Kyushu to Taiwan: the Ōsumi, Tokara, Amami, Okinawa, and Sakishima Islands (further divided into the Miyako and Yaeyama Islands), with Yonaguni the southernmost.
- [d4s2]  The larger are mostly high islands and the smaller ones are mostly coral islands.
- [d4s3]  The largest of the islands is Okinawa.

**d5: Shortland Islands**

- [d5s0] The Shortland Islands are group of islands belonging to the Western Province of the Solomon Islands, at .
- [d5s1]  Named by John Shortland, they lie in the extreme northwest of the country's territory, close to the island of Bougainville, Papua New Guinea.
- [d5s2]  The largest island is Shortland Island.
- [d5s3]  Other islands include Ovau Island, Pirumeri Island, Magusaiai Island, Fauro Island, and Ballale Island (which was occupied by the Japanese in World War II, and is home to many abandoned World War II aircraft).

**d6: Okinawa Island**

- [d6s0] Okinawa Island (沖縄本島 , Okinawa-hontō ) is the largest of the Okinawa Islands and the Ryukyu ("Nansei") Islands of Japan.
- [d6s1]  The island is approximately 70 miles long and an average 7 miles wide, and has an area of 1,206.98 km2 .
- [d6s2]  It is roughly 640 km south of the rest of Japan, roughly the same distance off the coast of China, and 500 km north of Taiwan.
- [d6s3]  The Greater Naha area, home to the prefectural seat of Okinawa Prefecture on the southwestern part of Okinawa Island, has roughly 800,000 of the island's 1.3 million residents, while the city itself is home to about 320,000.

**d7: Toronto Islands**

- [d7s0] The Toronto Islands (formerly known as Island of Hiawatha and also known as Menecing, meaning "On the Island" in the Ojibwa language) are a chain of small islands in Lake Ontario, south of mainland Toronto, Ontario, Canada.
- [d7s1]  Comprising the only group of islands in the western part of Lake Ontario, the Toronto Islands are located just offshore from the city centre, and provide shelter for Toronto Harbour.
- [d7s2]  The islands are home to parkland, the Billy Bishop Toronto City Airport, several yacht clubs, Centreville Amusement Park, and Hanlan's Beach.
- [d7s3]  The island community is considered to be the largest urban car-free community in North America, although some service vehicles are permitted.
- [d7s4]  Access to the Islands is by ferry, including the City of Toronto ferries operating from Jack Layton Ferry Terminal at the foot of Bay Street, or by water taxis.

**d8: Tokara Islands**

- [d8s0] The Tokara Islands (吐噶喇列島 , Tokara-rettō ) is an archipelago in the Nansei Islands, and are part of the Satsunan Islands, which is in turn part of the Ryukyu Archipelago.
- [d8s1]  The 150 km chain consists of twelve small islands located between Yakushima and Amami-Oshima.
- [d8s2]  The islands have a total area of 101.35 sqkm .
- [d8s3]  Administratively, the whole group belongs to Toshima Village, Kagoshima Prefecture, Japan.
- [d8s4]  Only seven of the islands are permanently inhabited.
- [d8s5]  The islands, especially Takarajima, are home to the Tokara Pony.

**d9: Rhinosolea microlepidota**

- [d9s0] Rhinosolea microlepidota is a species of sole native to the Pacific Ocean from around the Ryukyu Islands.
- [d9s1]  This species grows to a length of 2.4 cm SL.
- [d9s2]  This species is the only known member of its genus.

**d10: Bonin Islands**

- [d10s0] The Bonin Islands, also known as the Ogasawara Islands (小笠原群島 , "Ogasawara Guntō" ) , are an archipelago of over 30 subtropical and tropical islands, some 1000 km directly south of Tokyo, Japan.
- [d10s1]  The name "Bonin Islands" comes from the Japanese word "bunin" (an archaic reading of 無人 "mujin"), meaning "no people" or "uninhabited".
- [d10s2]  The only inhabited islands of the group are Chichijima (父島 ), the seat of the municipal government, and Hahajima (母島 ), which includes Ogasawara Village.

## 20. hotpotqa_5a8e28ba5542990e94052a80

原位置：`train` 第 170 题 · 全局第 170 题 · `sample_id: hotpotqa_5a8e28ba5542990e94052a80`

Question: Destiny and A Village Romeo and Juliet, is what type of play?

Note: 我觉得u3是有必要的，不能默认题干中的两个对象一定是同一个类别

Type: comparison · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | type of work Destiny is | False | [] | opera | [["d1s0"]] | context |
| u2 | type of work A Village Romeo and Juliet is | False | [] | opera | [["d9s0"]] | context |
| u3 | type of play that Destiny and A Village Romeo and Juliet both are | True | ["u1", "u2"] | opera | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | type of work Destiny is | False | [] | opera | [['d1s0']] |
| u2 | type of work A Village Romeo and Juliet is | False | [] | opera | [['d9s0']] |
| u3 | type of play that Destiny and A Village Romeo and Juliet both are | True | ['u1', 'u2'] | opera | [[]] |

### Source documents (reference only)

**d1: Destiny (Janáček)**

- [d1s0] Destiny (also known as "Fate", Czech: "Osud" ) is an opera in three acts by Leoš Janáček to a Czech libretto by the composer and Fedora Bartošová.
- [d1s1]  Janáček began the work in 1903 and completed it in 1907.
- [d1s2]  The inspiration for the opera came from a visit by Janáček in the summer of 1903, after the death of his daughter Olga, to the spa at Luhačovice.
- [d1s3]  There, Janáček met Kamila Urválková, who had been the subject of an opera by Ludvík Čelanský, "Kamila", where she felt that Čelanský had falsely depicted her personality.
- [d1s4]  After learning that Janáček was a composer, Urválková persuaded Janáček to write another opera to counteract Čelanský's portrait of her.

**d2: Romeo**

- [d2s0] Romeo Montague (Italian: "Romeo Montecchi" ) is the protagonist of William Shakespeare's tragedy "Romeo and Juliet".
- [d2s1]  The son of Montague and his wife, he secretly loves and marries Juliet, a member of the rival House of Capulet.
- [d2s2]  Forced into exile after slaying Juliet's cousin, Tybalt, in a duel, Romeo commits suicide upon hearing falsely of Juliet's death.

**d3: Dorothy Bond**

- [d3s0] Dorothy Bond (1921 20 November 1952) was an English coloratura soprano whose star shone brightly but briefly.
- [d3s1]  She was noted for the purity of her tone and the accuracy of her intonation.
- [d3s2]  She became a favourite singer of Sir Thomas Beecham's, recording the voice of Olympia for the Powell and Pressburger film of Offenbach's "The Tales of Hoffmann" in 1950.
- [d3s3]  She also recorded Delius's "A Village Romeo and Juliet" under Beecham, and Ernest Bloch's "Sacred Service" under the composer.
- [d3s4]  She was killed in a road accident at the age of 31.

**d4: Romeo and Juliet Windmill**

- [d4s0] The Romeo and Juliet Windmill, is a wooden structure designed by architect Frank Lloyd Wright in the town of Wyoming, Wisconsin (Wyoming is south of the town of Spring Green).
- [d4s1]  It was designed in 1896 after being commissioned by Wright's aunts, Jane and Ellen Lloyd Jones, who needed the windmill to provide water for their school, the Hillside Home School.
- [d4s2]  The diamond-shaped portion of the windmill intersects the portion with the balcony that sits on an octagonal structure.
- [d4s3]  The balcony is accessible through an interior stairway.
- [d4s4]  Wright named these two parts of the building "Romeo" and "Juliet".
- [d4s5]  "Romeo" is the lozenge and Juliet, the octagon.
- [d4s6]  Architectural historian, Neil Levine explained the principles behind the lozenge and octagon: [Wright] gave the tower a bold geometric form as a structural solution to the expression of the tower's role as a landmark.
- [d4s7]  The pump rod and support for the wheel are carried up within an acutely angled lozenge shape pointed southeast to deflect blasts of wind like a "storm prow".
- [d4s8]  This angular element is inserted halfway into a larger octagonal volume that contains and supports it throughout nearly its full height.
- [d4s9]  Wright called the composition Romeo and Juliet, likening its conjugate geometry to an amorous union.

**d5: Romeo + Juliet**

- [d5s0] William Shakespeare's Romeo + Juliet (shortened to Romeo + Juliet) is a 1996 American romantic drama film directed, co-produced, and co-written by Baz Luhrmann, co-produced by Gabriella Martinelli, and co-written by Craig Pearce, being an adaptation and modernization of William Shakespeare's tragedy "Romeo and Juliet".
- [d5s1]  The film stars Leonardo DiCaprio and Claire Danes in the leading roles of Romeo and Juliet, who instantly fall in love when Romeo crashes a party and meets her, despite their being members of the Montague and Capulet family; Brian Dennehy, John Leguizamo, Pete Postlethwaite, Paul Sorvino, and Diane Venora star in supporting roles.

**d6: Romeo and Juliet on screen**

- [d6s0] William Shakespeare's Romeo and Juliet may be one of the most-screened plays of all time.
- [d6s1]  The most notable theatrical releases were George Cukor's multi-Oscar-nominated 1936 production "Romeo and Juliet", Franco Zeffirelli's 1968 film "Romeo and Juliet", and Baz Luhrmann's 1996 MTV-inspired "Romeo + Juliet".
- [d6s2]  The latter two were both, at the time, the highest-grossing Shakespeare films.
- [d6s3]  Cukor featured the mature actors Norma Shearer and Leslie Howard as the teenage lovers while Zeffirelli populated his film with beautiful young people, and Baz Luhrmann produced a heavily cut fast-paced version aimed at teenage audiences.

**d7: A rose by any other name would smell as sweet**

- [d7s0] "A rose by any other name would smell as sweet" is a popular reference to William Shakespeare's play "Romeo and Juliet", in which Juliet seems to argue that it does not matter that Romeo is from her rival's house of Montague, that is, that he is named "Montague."
- [d7s1]  The reference is often used to imply that the names of things do not affect what they really are.
- [d7s2]  This formulation is, however, a paraphrase of Shakespeare's actual language, seen underlined below.
- [d7s3]  This scene is called the balcony scene by many people.
- [d7s4]  Juliet not only makes the statement above but compares Romeo to a rose saying that if he wasn't named Romeo he would still be handsome and be Juliet's Love.
- [d7s5]  Also as said before this states that if he wasn't Romeo, then he wouldn't be a Montague and she would be able to get married with no problem at all.

**d8: Romeo × Juliet**

- [d8s0] Romeo × Juliet (ロミオ×ジュリエット , Romio to Jurietto ) is an anime television series, loosely based on William Shakespeare's classical play, "Romeo and Juliet", along with numerous references and characters from other Shakespearean plays.
- [d8s1]  Though the anime borrows mostly from Shakespeare's story, the manga adaptation differs extensively from the original.
- [d8s2]  "Romeo × Juliet" was broadcast in Japan on Chubu-Nippon, broadcasting from April 4, 2007 to September 26, 2007.
- [d8s3]  In 2009, "Romeo × Juliet" was dubbed into English and released by Funimation Entertainment.

**d9: A Village Romeo and Juliet**

- [d9s0] A Village Romeo and Juliet is an opera by Frederick Delius, the fourth of six operas.
- [d9s1]  The composer himself, with his wife Jelka, wrote the English-language libretto based on the short story "Romeo und Julia auf dem Dorfe" by the Swiss author Gottfried Keller.
- [d9s2]  The first performance was at the Komische Oper Berlin on 21 February 1907, as Romeo und Julia auf dem Dorfe.
- [d9s3]  Thomas Beecham conducted the British premiere at the Royal Opera House, Covent Garden in London on 22 February 1910.
- [d9s4]  The US premiere was on 26 April 1972 in Washington, D.C.

**d10: Characters in Romeo and Juliet**

- [d10s0] Prince Escalus, the Prince of Verona, is the desperate resolver of the feuding families.
- [d10s1]  He is based on the actual Scaligeri family which ruled Verona, possibly on Bartolomeo I.
- [d10s2]  Escalus is the voice of authority in Verona.
- [d10s3]  He appears only three times within the text and only to administer justice following major events in the feud between the Capulet and Montague families.
- [d10s4]  He first punishes Capulet and Montague for the quarrel between Tybalt, Benvolio, and a handful of servants.
- [d10s5]  He returns too late to stop the fatal brawls between Tybalt and Mercutio and, subsequently, Tybalt and Romeo.
- [d10s6]  Escalus is prepared to execute Romeo for his offence—Romeo's killing Tybalt—but lightens the sentence to lifetime banishment from Verona, when Benvolio insists that Tybalt started the quarrel by murdering Mercutio, a kinsman to the Prince.
- [d10s7]  He yells at Lord Montague for engaging in the feud, which really is the root cause which led to Tybalt killing Mercutio.
- [d10s8]  So, according to him, he lost his dear kinsman because of Lord Montague, so by exiling Romeo, Escalus gives him a 'taste of Montague's own medicine', to see how Montague feels when he loses a loved one.
- [d10s9]  Prince Escalus returns in the final scene—V.iii—following the double suicide of Romeo and Juliet, and at last declares the Lords Montague and Capulet guilty of Romeo and Juliet's death, and angrily tells them that their totally useless feud resulted in the deaths of not only their own loved ones (Lady Montague, Romeo, Juliet, and Tybalt), but also in the deaths of Escalus' loved ones (Mercutio and Paris).
- [d10s10]  He curses the feud that kills Romeo and Juliet whom he really feels sad for, just before the Lords come to peace with each other.
- [d10s11]  In the end, Prince Escalus becomes very happy that the feud has finally ended, even if with a heavy price, since it ended late.

## 21. hotpotqa_5a8e88875542990e94052b36

原位置：`train` 第 171 题 · 全局第 171 题 · `sample_id: hotpotqa_5a8e88875542990e94052b36`

Question: The head coach for the 2004-05 Florida Gators men's college basketball team is currently the head coach for what National Basketball Association team?

Note: 

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | head coach for the 2004-05 Florida Gators men's college basketball team | False | [] | Billy Donovan | [["d8s2"]] | context |
| u2 | current head coach team of {u1} in the National Basketball Association | True | ["u1"] | Oklahoma City Thunder | [["d9s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | head coach of the 2004-05 Florida Gators men's basketball team | False | [] | Billy Donovan | [['d8s2']] |
| u2 | National Basketball Association team for which {u1} is currently head coach | True | ['u1'] | Oklahoma City Thunder | [['d9s0']] |

### Source documents (reference only)

**d1: List of Florida Gators head football coaches**

- [d1s0] This list of Florida Gators head football coaches includes those coaches who have led the Florida Gators football team that represents the University of Florida in the sport of American football.
- [d1s1]  The Florida Gators currently compete in the Division I Football Bowl Subdivision (FBS) of the National Collegiate Athletic Association (NCAA), and the Eastern Division of the Southeastern Conference (SEC).
- [d1s2]  Twenty-four men have served as the Gators' head coach, including three who served as interim head coach, since the Gators began play in the fall of 1906.
- [d1s3]  In December 2014, Jim McElwain was hired as the Gators' latest head coach after his predecessor, Will Muschamp, coached the Gators in their final regular season game of 2014.

**d2: List of Florida Gators in the NBA**

- [d2s0] This List of Florida Gators men's basketball players in the NBA includes those former Florida Gators who have played in one or more regular season games of the National Basketball Association (NBA).
- [d2s1]  The Florida Gators men's basketball team represents the University of Florida was founded in 1915, and represents the university in intercollegiate competition.
- [d2s2]  The University of Florida is a member of the National Collegiate Athletic Association (NCAA) and Southeastern Conference (SEC).
- [d2s3]  The Gators have won two NCAA Men's Division I Basketball Championships in 2006 and 2007.
- [d2s4]  After their college careers, several former Gators have played professionally in the NBA.
- [d2s5]  As of the 2011–12 NBA season, 26 former Florida players have played in the NBA.
- [d2s6]  During the 2011–2012 NBA season, 10 former Gators were active players in the NBA.

**d3: 2012–13 Florida Gators men's basketball team**

- [d3s0] The 2012–13 Florida Gators men's basketball team represented the University of Florida in the sport of basketball during the 2012–13 college basketball season.
- [d3s1]  The Gators competed in Division I of the National Collegiate Athletic Association (NCAA) and the Southeastern Conference (SEC).
- [d3s2]  They were led by head coach Billy Donovan, and played their home games in the O'Connell Center on the university's Gainesville, Florida campus.

**d4: C. J. McCoy**

- [d4s0] Charles J. McCoy was an American college football and basketball coach.
- [d4s1]  McCoy was the third head coach of the Florida Gators football team and the first head coach of the Florida Gators men's basketball team that represent the University of Florida in Gainesville, Florida.

**d5: 2009–10 Florida Gators men's basketball team**

- [d5s0] The 2009–10 Florida Gators men's basketball team represented the University of Florida in the sport of basketball during the 2009–10 college basketball season.
- [d5s1]  The Gators competed in Division I of the National Collegiate Athletic Association (NCAA) and the Eastern Division of the Southeastern Conference (SEC).
- [d5s2]  They were led by head coach Billy Donovan, and played their home games in the O'Connell Center on the university's Gainesville, Florida campus.

**d6: Florida Gators men's tennis**

- [d6s0] The Florida Gators men's tennis team represents the University of Florida in the sport of tennis.
- [d6s1]  The Gators compete in Division I of the National Collegiate Athletics Association (NCAA) and the Southeastern Conference (SEC).
- [d6s2]  The team hosts its home matches in Linder Stadium on the university's Gainesville, Florida campus, led by head coach Bryan Shelton.
- [d6s3]  In the eighty-five-year history of the Gators men's tennis program, the Gators have won nine SEC team championships, two NCAA singles championships and one NCAA doubles championship.

**d7: 2010–11 Florida Gators men's basketball team**

- [d7s0] The 2010–11 Florida Gators men's basketball team represented the University of Florida in the sport of basketball during the 2010–11 college basketball season.
- [d7s1]  The Gators competed in Division I of the National Collegiate Athletic Association (NCAA) and the Eastern Division of the Southeastern Conference (SEC).
- [d7s2]  They were led by head coach Billy Donovan, and played their home games in the O'Connell Center on the university's Gainesville, Florida campus.

**d8: 2004–05 Florida Gators men's basketball team**

- [d8s0] The 2004–05 Florida Gators men's basketball team represented the University of Florida in the sport of basketball during the 2004–05 college basketball season.
- [d8s1]  The Gators competed in Division I of the National Collegiate Athletic Association (NCAA) and the Eastern Division of the Southeastern Conference (SEC).
- [d8s2]  They were led by head coach Billy Donovan, and played their home games in the O'Connell Center on the university's Gainesville, Florida campus.

**d9: Billy Donovan**

- [d9s0] William John Donovan Jr. (born May 30, 1965) is an American professional basketball coach who is currently the head coach for the Oklahoma City Thunder of the National Basketball Association (NBA).
- [d9s1]  He previously spent 19 seasons at the University of Florida, where his Florida Gators teams won back-to-back NCAA championships in 2006 and 2007.
- [d9s2]  Donovan has more wins than any other coach in the history of the Florida basketball program, and he coached the Gators to more NCAA tournament appearances, NCAA tournament wins, and Southeastern Conference (SEC) championships than all other Florida coaches combined.

**d10: 2011–12 Florida Gators men's basketball team**

- [d10s0] The 2011–12 Florida Gators men's basketball team represented the University of Florida in the sport of basketball during the 2011–12 college basketball season.
- [d10s1]  The Gators competed in Division I of the National Collegiate Athletic Association (NCAA) and the Southeastern Conference (SEC).
- [d10s2]  They were led by head coach Billy Donovan, and played their home games in the O'Connell Center on the university's Gainesville, Florida campus.

## 22. hotpotqa_5a908d1f55429916514e74f1

原位置：`train` 第 172 题 · 全局第 172 题 · `sample_id: hotpotqa_5a908d1f55429916514e74f1`

Question: Rachel Carson and Walter Mosley, are which nationality?

Note: 保留新版两个必要单元，分别使用 d8s0、d4s0 支持各自国籍。不根据题干预设两人国籍相同，不通过一人的证据推断另一人；两方均有支持才判为完整回答。

Type: multipart · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | nationality of Rachel Carson | True | [] | American | [["d8s0"]] | context |
| u2 | nationality of Walter Mosley | True | [] | American | [["d4s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | nationality of Rachel Carson | False | [] | American | [['d8s0']] |
| u2 | nationality of Walter Mosley | False | [] | American | [['d4s0']] |
| u3 | nationality shared by Rachel Carson and Walter Mosley | True | ['u1', 'u2'] | American | [[]] |

### Source documents (reference only)

**d1: RV Rachel Carson (2008)**

- [d1s0] RV "Rachel Carson" is a research vessel owned and operated by the University of Maryland's Center for Environmental Science, named in honor of the marine biologist and writer Rachel Carson.

**d2: Walter T. Mosley**

- [d2s0] Walter T. Mosley (born Walter Mosley III in Brooklyn, New York) is an American Democratic politician that represents the 57th district of the New York State Assembly.
- [d2s1]  He serves the neighborhoods of Fort Greene, Clinton Hill, Prospect Heights, and parts of Crown Heights and Bedford Stuyvesant.

**d3: Rachel Carson National Wildlife Refuge**

- [d3s0] The Rachel Carson National Wildlife Refuge is a 9125 acre National Wildlife Refuge made up of several parcels of land along 50 mi of Maine's southern coast.
- [d3s1]  Created in 1966, it is named for environmentalist and author Rachel Carson, whose book "Silent Spring" raised public awareness of the effects of DDT on migratory songbirds, and of other environmental issues.

**d4: Walter Mosley**

- [d4s0] Walter Ellis Mosley (born January 12, 1952) is an American novelist, most widely recognized for his crime fiction.
- [d4s1]  He has written a series of best-selling historical mysteries featuring the hard-boiled detective Easy Rawlins, a black private investigator and World War II veteran living in the Watts neighborhood of Los Angeles; they are perhaps his most popular works.

**d5: Rachel Carson Prize**

- [d5s0] Rachel Carson Prize may refer to any of three prizes and awards named after environmentalist Rachel Carson:

**d6: Ruth Jury Scott**

- [d6s0] Ruth Jury Scott (27 March 1909 – 18 June 2003) was a lifelong environmental activist, naturalist, and conservationist.
- [d6s1]  Scott was a close friend and colleague to Rachel Carson due to their shared passion for educating others about the environment as well as the deadly effects of chemical pesticides.
- [d6s2]  She later served on the executive committee of the Rachel Carson Trust for the Living Environment, Inc.

**d7: Rachel Carson Prize (environmentalist award)**

- [d7s0] The Rachel Carson Prize ("Rachel Carson-prisen") is an international environmental award, established in Stavanger, Norway in 1991 to commemorate the achievements of environmentalist Rachel Carson and to award efforts in her spirit.
- [d7s1]  The prize is awarded to a woman who has distinguished herself in outstanding work for the environment in Norway or internationally.

**d8: Rachel Carson**

- [d8s0] Rachel Louise Carson (May 27, 1907 – April 14, 1964) was an American marine biologist, author, and conservationist whose book "Silent Spring" and other writings are credited with advancing the global environmental movement.

**d9: Rachel Carson Run**

- [d9s0] Rachel Carson Run is a 1.4 mi long tributary of the Allegheny River located in Allegheny County in the U.S. state of Pennsylvania.
- [d9s1]  The stream is named after ecologist Rachel Carson.

**d10: Rachel Carson House (Colesville, Maryland)**

- [d10s0] The Rachel Carson House is a historic house at 11701 Berwick Road in Colesville, Maryland, an unincorporated area near Silver Spring, Maryland.
- [d10s1]  Built in 1956, this typical suburban ranch-style house was where writer Rachel Carson wrote her classic work "Silent Spring" in 1962.
- [d10s2]  The house was designated a National Historic Landmark in 1991 for its association with Carson.

## 23. hotpotqa_5ab25a9d5542993be8fa98df

原位置：`train` 第 173 题 · 全局第 173 题 · `sample_id: hotpotqa_5ab25a9d5542993be8fa98df`

Question: The American fashion designer for Bjork's Greatest Hits Tour is the director of what fashion house?

Note: 

Type: bridge · fallback: False · SFT snapshots: 7

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | American fashion designer for Bjork's Greatest Hits Tour | False | [] | Jeremy Scott | [["d4s6", "d5s0"]] | context |
| u2 | fashion house directed by {u1} | True | ["u1"] | Moschino | [["d5s1"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | American fashion designer for Björk's Greatest Hits Tour | False | [] | Jeremy Scott | [['d4s6', 'd5s0']] |
| u2 | fashion house of which {u1} is the director | True | ['u1'] | Moschino | [['d5s1']] |

### Source documents (reference only)

**d1: Norman Norell**

- [d1s0] Norman David Levinson (April 20, 1900 – October 25, 1972) known professionally as Norman Norell, was an American fashion designer famed for his elegant gowns, suits, and tailored silhouettes.
- [d1s1]  His designs for the Traina-Norell and Norell fashion houses became famous for their detailing, simple, timeless designs, and tailored construction.
- [d1s2]  By the mid-twentieth century Norell dominated the American fashion industry and in 1968 he became the first American fashion designer to launch his own brand of perfume.

**d2: Showgirl: The Greatest Hits Tour**

- [d2s0] Showgirl: The Greatest Hits Tour was the eighth concert tour by Australian singer Kylie Minogue.
- [d2s1]  The tour was launched in support of her ninth greatest hits compilation, "Ultimate Kylie".
- [d2s2]  Beginning March 2005, over 30 concerts were performed in Europe.

**d3: Diffusion line**

- [d3s0] A diffusion line (also known as a bridge line) is a secondary line of merchandise created by a high-end fashion house or fashion designer that retails at lower prices.
- [d3s1]  These ranges are separate from a fashion house's "signature line", or principal artistic line, that typically retail at much higher prices.
- [d3s2]  Diffusion products may be on sale alongside designers' signature line but they can also be made available at concession outlets and certain chain stores.
- [d3s3]  The use of a diffusion line is a part of the strategy of Massification where luxury brands attempt to reach a broader market in order to increase revenue and brand recognition.

**d4: Greatest Hits Tour (Björk)**

- [d4s0] The Greatest Hits Tour was the fifth worldwide concert tour by Icelandic musician Björk.
- [d4s1]  It was launched in support of the release of her "Greatest Hits" album, her box set "Family Tree", and to coincide with the release of her "Live Box" collection.
- [d4s2]  The tour was supposed to take place one year earlier, but it was delayed as Björk gave birth to her daughter.
- [d4s3]  The first dates of the tour were announced just two months after the birth.
- [d4s4]  The tour kicked off with two shows in London on May 24, 2003, and ended with a rescheduled performance in Toronto on September 3, 2003.
- [d4s5]  The tour visited Europe, Asia and North America with 28 shows in total.
- [d4s6]  Björk wore outfits and creations from Jeremy Scott, Alexander McQueen and Shoplifter.

**d5: Jeremy Scott**

- [d5s0] Jeremy Scott (born August 8, 1975) is an American fashion designer.
- [d5s1]  He is the creative director of the fashion house Moschino and the sole owner of his namesake label.
- [d5s2]  Since launching his brand in Paris in 1997, Scott has built a reputation as "pop culture’s most irreverent designer", and "fashion's last rebel".

**d6: Ultimate Collection Tour**

- [d6s0] The Ultimate Collection Tour (also known as Ultimate Collection Live) is the fourth headlining tour and first greatest hits tour by American recording artist, Anastacia.
- [d6s1]  The tour supports her second greatest hits complication, "Ultimate Collection" The tour began April 2016 in Italy and performed in 17 European countries and nearly 100 shows.

**d7: Oleg Cassini, Inc.**

- [d7s0] Oleg Cassini, Inc. is an American fashion house founded by American fashion designer Oleg Cassini.
- [d7s1]  The company is based in Oyster Bay Cove, New York, and was established in 1951.

**d8: The Greatest Hits Tour (Girls Aloud)**

- [d8s0] The Greatest Hits Tour was the third concert tour by Irish and British girl group Girls Aloud, in support of their first greatest hits album "".
- [d8s1]  Girls Aloud returned to Northern Ireland and the Republic of Ireland, having not performed there on 2006's Chemistry Tour.
- [d8s2]  The band performed sixteen dates in various arenas across the United Kingdom and Ireland, making it their second arena tour.
- [d8s3]  The Sound of Girls Aloud: The Greatest Hits Tour kicked off in Cheryl Cole's hometown of Newcastle on 14 May 2007 and concluding in near Nadine Coyle's home in Belfast on 2 June 2007.

**d9: Greatest Hits Tour (Westlife)**

- [d9s0] The Greatest Hits Tour (also known as The Farewell Tour) was the twelfth and final concert tour by Irish boy band, Westlife.
- [d9s1]  The tour, visited the Europe and Asia and supported the group's compilation album, "Greatest Hits".
- [d9s2]  After the tour finished, the group disbanded after performing for 14 years.

**d10: Patrick Kelly (fashion designer)**

- [d10s0] Patrick Kelly (September 24, 1954 – January 1, 1990) was an American fashion designer.
- [d10s1]  Born in Vicksburg, Mississippi, Kelly studied art at Jackson State University and then attended Parsons School of Design.
- [d10s2]  While in New York Kelly Struggled to find steady employment.
- [d10s3]  To support himself he had many jobs that included a part time job at Baskin Robbins while continuing to sell his own designs.
- [d10s4]  After receiving advice from his friend and super model Pat Cleveland and an anonymous one-way ticket he moved to Paris in 1979.
- [d10s5]  Once there Kelly was promptly hired as a costume designer for a nightclub called Le Palace.
- [d10s6]  In a small apartment which he shared with a model he continued to sell his own creations and even homemade chicken dinners to make ends meet.
- [d10s7]  While living in Atlanta at age 18 Kelly sold reworked, recycled clothes and served as an unpaid window-dresser at Yves Saint Laurent.
- [d10s8]  YSL chairman Pierre Bergé personally sponsored Kelly in 1988 to form the Paris-based womenswear fashion house Patrick Kelly Paris.
- [d10s9]  Kelly achieved his greatest commercial success in the late 1980s and in 1988 Kelly became both the first American and the first person of color to be admitted as a member of the Chambre syndicale du prêt-à-porter des couturiers et des créateurs de mode.
- [d10s10]  Kelly died at age 35 on New Year's Day, 1990.
- [d10s11]  Originally Kelly's causes of death were reported to be bone marrow disease and a brain tumor, but the actual cause of death is now acknowledged to be complications of AIDS.

## 24. hotpotqa_5ab292b4554299449642c901

原位置：`train` 第 174 题 · 全局第 174 题 · `sample_id: hotpotqa_5ab292b4554299449642c901`

Question: The top brand of beer in North Korea is brewed by which company ?

Note: 旧的gold结构是正确的

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | top brand of beer in North Korea | False | [] | Taedonggang | [["d2s1"]] | context |
| u2 | company that brews {u1} | True | ["u1"] | Taedonggang Brewing Company | [["d1s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | top brand of beer in North Korea | False | [] | Taedonggang | [['d2s1']] |
| u2 | company that brews {u1} | True | ['u1'] | Taedonggang Brewing Company | [['d1s0']] |

### Source documents (reference only)

**d1: Taedonggang**

- [d1s0] Taedonggang is a brand of North Korean beer brewed by the state-owned Taedonggang Brewing Company based in Pyongyang.
- [d1s1]  There are four brands of beer marketed as Taedonggang, though the brand known simply as "Taedonggang Beer" is that described below.

**d2: Beer in North Korea**

- [d2s0] North Korea has at least ten major breweries and many microbreweries that supply a wide range of beer products.
- [d2s1]  The top brand is the light lager Taedonggang which is internationally known for its quality.

**d3: New Zealand–North Korea relations**

- [d3s0] New Zealand–North Korea relations (Korean:뉴질랜드-조선민주주의인민공화국 관계) refers to international relations between New Zealand and North Korea.
- [d3s1]  Relations between the two countries have been almost non-existent since the division of Korea.
- [d3s2]  During the Korean War in the 1950s, New Zealand troops fought as part of the United Nations force that repelled the North Korean invasion of South Korea.
- [d3s3]  Since then, New Zealand and North Korea have had little contact, until July 2000 when North Korean Foreign Minister Paek Nam-sun and New Zealand Minister of Foreign Affairs Phil Goff met in Bangkok, leading to the establishment of diplomatic relations in March 2001.
- [d3s4]  The New Zealand ambassador to South Korea based in Seoul is also cross-accredited to North Korea.
- [d3s5]  In 2006, North Korea tested its first nuclear weapon, drawing criticism and suspension of relations by the New Zealand government, which holds a staunch anti-nuclear policy.
- [d3s6]  New Zealand began re-establishing formal relations in 2007, when the New Zealand Minister of Foreign Affairs Winston Peters visited Pyongyang on November 20 to discuss possible political and economic deals with North Korea, on the basis that it start dismantling its nuclear weapons facilities.

**d4: A&amp;W Cream Soda**

- [d4s0] A&W Cream Soda is a cream soda carbonated soft drink introduced by A&W Root Beer in 1986.
- [d4s1]  A&W Root Beer was first sold at a Veterans Day parade in Lodi, California in 1919 and the company established in 1922 by Frank Wright and Roy Allen.
- [d4s2]  The first product they created was A & W Root Beer.
- [d4s3]  It was not until 1986 that A&W Brands, headquartered in White Plains, N.Y. introduced A&W Cream Soda and A&W Diet Cream Soda through its network of franchised bottlers and distributors.
- [d4s4]  Although cream soda had been created in 1852 by E.M. Sheldon, A&W Brands was one of the first American companies to make it commercially.
- [d4s5]  In 1993, A&W Brands was purchased by Cadbury/Schweppes, and in 1995 Cadbury/Schweppes purchased the Dr. Pepper/Seven-Up Company, which made A&W a part of the Dr. Pepper/Seven Up, Inc.
- [d4s6]  In 2001, DPSU purchased the Snapple Beverage Group (formally TriArc Beverages), and moved the New York-based company operations to its new headquarters in Plano, Texas.
- [d4s7]  This acquisition put A&W within the same company as the top soda brand companies and made A&W Cream Soda the top brand in cream sodas.

**d5: North Korea Strategy Center**

- [d5s0] North Korea Strategy Center (NKSC) is a defector-led NGO that was established in Seoul, South Korea in 2007 to raise awareness about North Korea's human rights conditions, and advocate for freedom and unification in Korea.
- [d5s1]  Understanding the power of media and information to open minds and bring change, NKSC seeks to bring free press and media into North Korea by working with North and South Koreans, as well as the international community, raising awareness, with emphasis on the need for freedom of information and expression in North Korea.
- [d5s2]  Since its inception, NKSC has worked with over 150 North Korean defectors and sent over 40,000 DVDs, 400 radio sets, and 4,000 USBs into North Korea.

**d6: Communism in Korea**

- [d6s0] The Communist movement in Korea emerged as a political movement in the early 20th century.
- [d6s1]  Although the movement had a minor role in pre-war politics, the division between the communist North Korea and the anti-communist South Korea came to dominate Korean political life in the post-World War II era.
- [d6s2]  North Korea, officially the Democratic People's Republic of Korea, continues to be a Juche "socialist" state under the rule of the Workers Party of Korea.
- [d6s3]  In South Korea, communism remains illegal through the National Security Law.
- [d6s4]  Due to end of economic aid from Soviet Union after Dissolution of the Soviet Union in 1991 and impractical ideological application of Communist economy in North Korea over years of economic slowdown in 1980s and receding during 1990s, North Korea replaced Communism with Juche ideology in its 1992 and 1998 Constitutional revision for the personal cult of Kim's family dictatorship and (albeit reluctanly) opening of North Korean market economy reform, though it still remains a centrally planned economy with complete control of the state and agriculture with collectivized farms and state-funded education and healthcare.

**d7: Germany–North Korea relations**

- [d7s0] Germany–North Korea relations (Korean: 독일-조선민주주의인민공화국 관계 ) are the bilateral relations between Germany and North Korea.
- [d7s1]  During the Cold War, East Germany maintained diplomatic relations only with North Korea, while West Germany maintained diplomatic relations only with South Korea.
- [d7s2]  East Germany ceased to exist upon German reunification, which meant that diplomatic relations no longer existed between Germany and North Korea.
- [d7s3]  The two countries appointed protecting powers to represent their interests in the other country, Sweden being the protecting power for Germany, and China being the protecting power for North Korea.

**d8: United States in the Korean War**

- [d8s0] At the conclusion of World War II the Allied nations began the process of disarmament of Axis controlled regions.
- [d8s1]  Japan occupied Korea at this time and had been in control since 1910.
- [d8s2]  In 1945, the decision was made to have American Marines forces oversee Japanese surrender and disarmament south of the 38th parallel and the Soviet Union would facilitate the change of power to the north.
- [d8s3]  At the time there was no political motivation and seemed to be a logical and convenient plan of action.
- [d8s4]  The original agreement and intent was to create a unified and independent Korea out of the post Japanese occupation era.
- [d8s5]  Instead each side of the 38th parallel established its own government under the influence of the occupational country; the United States in South Korea and the Soviet Union in North Korea.
- [d8s6]  Both new Korean governments discredited the other and claimed to be the only legitimate political system.
- [d8s7]  Tensions between the North and South escalated and each side began to petition foreign powers for resources and support.
- [d8s8]  South Korea wanted weapons and supplies from Truman and the United States government while North Korea sought help from Stalin and the Soviet Union.
- [d8s9]  The United States was still war weary from the disruptive World War II campaign and refused South Korea's request for weapons and troops.
- [d8s10]  North Korea convinced the Soviet Union to supply them with the weapons and support they requested.
- [d8s11]  This decision coincided with the United States withdrawing the last remaining combat troops from South Korea.
- [d8s12]  North Korea saw its opportunity and attacked South Korean forces at the 38th parallel on June 25, 1950 and thus initiating the Korean War.

**d9: Iran–North Korea relations**

- [d9s0] Iran–North Korea relations (Korean: 이란-조선민주주의인민공화국 관계 ; Persian: روابط ایران و کره‌ی شمالی‎ ‎ ) are described as being positive by official news agencies of the two countries.
- [d9s1]  Diplomatic relations picked up following the Iranian Revolution in 1979 and the establishment of an Islamic Republic.
- [d9s2]  Iran and North Korea pledge cooperation in educational, scientific, and cultural spheres.
- [d9s3]  Some media reports claim this cooperation extends to nuclear cooperation, though official U.S. government publications and academic studies have disputed this.
- [d9s4]  The United States has been greatly concerned by North Korea's arms deals with Iran, which started during the 1980s with North Korea acting as a third party in arms deals between the Communist bloc and Iran, as well as selling domestically produced weapons to Iran, and North Korea continues selling missile to Iran.
- [d9s5]  North Korea and Iran are the remaining two members of George W. Bush's "Axis of evil", which has led to many of the concerns regarding Iran–North Korea relations.

**d10: University of Natural Science**

- [d10s0] Institute of Natural Science (INS) is a university located inside the region of the National Academy of Science in Pyongyang, North Korea.
- [d10s1]  As Kim Il-sung, a former leader of North Korea, emphasized the significance of education for gifted and talented students, INS originally started as a branch of Kim Il-sung University on January 17, 1962.
- [d10s2]  It was separated from Kim Il-sung University in 1985.
- [d10s3]  In South Korean mass media, this university is called "KAIST of North Korea".
- [d10s4]  Top students of natural sciences or engineering in North Korea study at this university supported totally by North Korean government.
- [d10s5]  Eighty percent of them is graduated from No.1 Middle Schools, which are science high schools for gifted and talented students in North Korea, and the rest thirty percent are medal winners in the national science (math, physics, chemistry, and biology) olympiads or national science quiz contests.

## 25. hotpotqa_5ab2989b554299194fa93423

原位置：`train` 第 175 题 · 全局第 175 题 · `sample_id: hotpotqa_5ab2989b554299194fa93423`

Question: What American professional mixed martial artist who is currently fighting in the Middleweight division of the Ultimate Fighting Championship was trained by Matt Hume?

Note: 与新版对齐

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新查找顺序，先职业/级别、再训练者；重映射证据，最终返回人物。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | American professional mixed martial artist fighting in the Middleweight division of the Ultimate Fighting Championship | False | [] | Tim Boetsch | [["d2s0"]] | context |
| u2 | fighter among {u1} trained by Matt Hume | True | ["u1"] | Tim Boetsch | [["d1s1"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | fighters trained by Matt Hume | False | [] | Josh Barnett, Tim Boetsch, Bob Sapp, Chris Leben, Hayato Sakurai, Akira Shoji, Matt Brown, Rich Franklin, Mario Miranda and Caros Fodor | [['d1s1']] |
| u2 | which of {u1} is an American professional mixed martial artist currently fighting in the UFC Middleweight division | True | ['u1'] | Tim Boetsch | [['d2s0']] |

### Source documents (reference only)

**d1: Matt Hume**

- [d1s0] Matt Hume (born July 14, 1966) is an American mixed martial artist.
- [d1s1]  He is the founder and head trainer at AMC Pankration in Kirkland, WA, which is home to UFC flyweight champion Demetrious Johnson, ONE bantamweight champion Bibiano Fernandes and he has trained numerous world class fighters including Josh Barnett, Tim Boetsch Bob Sapp, Chris Leben, Hayato Sakurai, Akira Shoji, Matt Brown, Rich Franklin, Mario Miranda and Caros Fodor.

**d2: Tim Boetsch**

- [d2s0] Timothy A. Boetsch ( ; born January 28, 1981) is an American professional mixed martial artist currently fighting in the Middleweight division of the Ultimate Fighting Championship.
- [d2s1]  In addition to the UFC, Boetsch has formerly competed as an alternate for the New York Pitbulls in the International Fight League and King of the Cage.
- [d2s2]  He holds victories over former UFC Champion Johny Hendricks and former bellator middleweight champion Hector Lombard.
- [d2s3]  As of July 21, 2017, he is ranked #13 in official UFC Middleweight rankings.

**d3: B.J. Penn**

- [d3s0] Jay Dee "B.J." Penn (born December 13, 1978) is an American professional mixed martial artist and Brazilian Jiu-Jitsu practitioner.
- [d3s1]  Penn debuted and competed in the Ultimate Fighting Championship (UFC), and later in K-1.
- [d3s2]  Prior to fighting for the UFC, he became the first American Gold medalist of the World Jiu-Jitsu Championship.
- [d3s3]  In mixed martial arts, Penn has competed in the Featherweight, Lightweight, Welterweight, and Middleweight divisions.
- [d3s4]  As a former UFC Lightweight Champion and UFC Welterweight Champion, he is one of only three fighters in UFC history to win titles in multiple weight classes.
- [d3s5]  Penn was also a Co-champion in the UFC 41 Lightweight Tournament, due to an eventual draw opposite Caol Uno in the tournament finale.
- [d3s6]  Through his tenures as champion, Penn unofficially unified the UFC Lightweight Championship (against Sean Sherk) and broke the all-time lightweight title defense record.
- [d3s7]  Penn was inducted into the UFC Hall of Fame, as the inaugural inductee in the Modern-Era Wing by career-long rival Matt Hughes, during "International Fight Week" in July 2015.

**d4: Luke Zachrich**

- [d4s0] Luke Zachrich (born October 1, 1981) is an American mixed martial artist and former professional boxer who formerly competed in the Middleweight division of the Ultimate Fighting Championship A professional mixed martial arts competitor since 2006, Zachrich was a member of Team Forrest on the seventh season of The Ultimate Fighter, and has also fought for King of the Cage, Xtreme Fighting Organization, Bellator, and Ultimate Victory Challenge, the latter of which he was the inaugural Middleweight Champion.

**d5: Rory Markham**

- [d5s0] Rory Markham (born March 25, 1982) is an American professional mixed martial artist, stuntman and actor who most recently competed in the Welterweight division of the Ultimate Fighting Championship.
- [d5s1]  A professional competitor since 2003, currently fighting in XFO MMA.
- [d5s2]  Markham has also formerly competed for the IFL, representing the Quad Cities Silverbacks.

**d6: Dan Henderson**

- [d6s0] Daniel Jeffery Henderson (born August 24, 1970) is an American former mixed martial artist and Olympic wrestler, who last competed as a middleweight in the Ultimate Fighting Championship.
- [d6s1]  He was the last Strikeforce Light Heavyweight Champion and was the last Welterweight (80 kg ) and Middleweight (95 kg ) champion of Pride Fighting Championships.
- [d6s2]  Additionally, Henderson was the Brazil Open '97 Tournament Champion, the UFC 17 Middleweight Tournament Champion, the Rings: King of Kings 1999 Tournament Champion and the Pride Weltwerweight Grand Prix Tournament Champion.
- [d6s3]  During his career, Henderson also challenged for the UFC Middleweight Championship (2x), the UFC Light Heavyweight Championship and the Strikeforce Middleweight Championship.
- [d6s4]  He was the first mixed martial artist to concurrently hold two titles in two different weight classes in a major MMA promotion.
- [d6s5]  At the time of his retirement after UFC 204, he was the oldest fighter on the UFC roster.
- [d6s6]  Known to be one of the greatest mixed martial artists of all time having defeated a total of seventeen MMA world champions across four major MMA promotions (UFC, PRIDE FC, Strikeforce, and RINGS).

**d7: Jordan Radev**

- [d7s0] Jordan Radev (Bulgarian: Йордан Радев ; born March 4, 1976) is a Bulgarian wrestler and professional mixed martial artist.
- [d7s1]  He was the first Bulgarian mixed martial artist to fight in the Ultimate Fighting Championship in its middleweight division.

**d8: Alan Jouban**

- [d8s0] Alan Michael Jouban (born November 25, 1981) is an American professional mixed martial artist currently fighting in the Welterweight division of the Ultimate Fighting Championship.
- [d8s1]  A professional competitor since 2010, Jouban has also formerly competed for Shark Fights, the RFA, Tachi Palace Fights, and Tuff-N-Uff.

**d9: Tamdan McCrory**

- [d9s0] Tamdan Wade McCrory (born November 5, 1986) is an American professional mixed martial artist who formerly competed in the Middleweight division of the Ultimate Fighting Championship.
- [d9s1]  A professional competitor since 2006, McCrory has also formerly competed for Bellator MMA and the Cage Fury Fighting Championships.

**d10: Jake Collier**

- [d10s0] Jake Collier (born October 23, 1988) is an American mixed martial artist currently fighting in the middleweight division of the Ultimate Fighting Championship (UFC).

## 26. hotpotqa_5ab2ad8b554299340b525544

原位置：`train` 第 176 题 · 全局第 176 题 · `sample_id: hotpotqa_5ab2ad8b554299340b525544`

Question: Who wrote the 1953 novel about a postliterate society?

Note: 

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | 1953 novel about a postliterate society | False | [] | Fahrenheit 451 | [["d3s2", "d5s0"], ["d3s2", "d1s1"]] | context |
| u2 | author of {u1} | True | ["u1"] | Ray Bradbury | [["d5s0"], ["d1s1"], ["d3s2"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | 1953 novel about a postliterate society | False | [] | Fahrenheit 451 | [['d3s2', 'd5s0'], ['d3s2', 'd1s1']] |
| u2 | author of {u1} | True | ['u1'] | Ray Bradbury | [['d5s0'], ['d1s1'], ['d3s2']] |

### Source documents (reference only)

**d1: Fahrenheit 451 (film)**

- [d1s0] Fahrenheit 451 is a 1966 British Dystopian science fiction drama film directed by François Truffaut and starring Oskar Werner, Julie Christie, and Cyril Cusack.
- [d1s1]  Based on the 1953 novel of the same name by Ray Bradbury, the film takes place in a controlled society in an oppressive future in which a fireman, whose duty it is to burn all literature, becomes a fugitive for reading.
- [d1s2]  This was Truffaut's first colour film as well as his only English-language film.
- [d1s3]  At the 1966 Venice Film Festival, "Fahrenheit 451" was nominated for the Golden Lion.

**d2: Against the Fall of Night**

- [d2s0] Against the Fall of Night is a science fiction novel by British writer Arthur C. Clarke.
- [d2s1]  Originally appearing as a novella in the November, 1948 issue of the magazine "Startling Stories", it was revised and expanded in 1951 and published in book form in 1953 by Gnome Press.
- [d2s2]  It was later expanded and revised again and published in 1956 as "The City and the Stars".
- [d2s3]  A later edition includes another of Clarke's early works and is titled "The Lion of Comarre and Against the Fall of Night".
- [d2s4]  In 1990, with Clarke's approval, Gregory Benford wrote a sequel titled "Beyond the Fall of Night", which continues the story arc of the 1953 novel.
- [d2s5]  It is generally printed with the original novel as a single volume.

**d3: Postliterate society**

- [d3s0] A postliterate society is a hypothetical society in which multimedia technology has advanced to the point where literacy, the ability to read or write, is no longer necessary or common.
- [d3s1]  The term appears as early as 1962 in Marshall McLuhan's "The Gutenberg Galaxy".
- [d3s2]  Many science-fiction societies are postliterate, as in Ray Bradbury's "Fahrenheit 451", Dan Simmons' novel "Ilium", and Gary Shteyngart's "Super Sad True Love Story".

**d4: John Harris (novelist)**

- [d4s0] John Harris (18 October 1916 – 7 March 1991) was a British author.
- [d4s1]  He published a series of crime novels featuring the character Inspector Pel, and war books.
- [d4s2]  He wrote with his own name, and also with the pseudonyms of Mark Hebden and Max Hennessy.
- [d4s3]  His 1953 novel "The Sea Shall Not Have Them" was the basis for a feature film of the same name in 1954.
- [d4s4]  He was the father of Juliet Harris, who published more Inspector Pel books under the name of Juliet Hebden.

**d5: Fahrenheit 451**

- [d5s0] Fahrenheit 451 is a dystopian novel by American writer Ray Bradbury, published in 1953.
- [d5s1]  It is regarded as one of his best works.
- [d5s2]  The novel presents a future American society where books are outlawed and "firemen" burn any that are found.
- [d5s3]  The book's tagline explains the title: "Fahrenheit 451 – the temperature at which book paper catches fire, and burns..."

**d6: The Burglar**

- [d6s0] The Burglar is a 1957 crime thriller film noir released by Columbia Pictures, based on the 1953 novel of the same name by David Goodis (who also wrote the script).
- [d6s1]  The picture stars Dan Duryea in the titular role and Jayne Mansfield.

**d7: The Unconquered (novel)**

- [d7s0] The Unconquered was a 1953 novel by Ben Ames Williams.
- [d7s1]  It was Williams' final novel, completed in January 1953 less than a month before his death.
- [d7s2]  It is a sequel to his "House Divided".

**d8: Cross Damon**

- [d8s0] Cross Damon was a fictional character from Richard Wright's 1953 novel "The Outsider".
- [d8s1]  Cross Damon was viewed as an "outsider" who did not attempt to become a product of the established culture of American society.
- [d8s2]  Cross was considered a complete opposite to Bigger Thomas, another character created by Richard Wright in his novel "Native Son".
- [d8s3]  He also ridicules Communist techniques and lives according to the principles of free choice.
- [d8s4]  Cross Damon committed murder in a completely different spirit than Bigger Thomas.
- [d8s5]  He acts as an individual who is free to do whatever his habits and desires lead him to do.
- [d8s6]  His is not a victim of social and environmental pressures outside his control.
- [d8s7]  In many ways, Cross Damon resembles Meursault, the hero of Albert Camus novel "The Stranger".
- [d8s8]  Both men lived outside of any involvement with common humanity and paid no attention to social mores.

**d9: The Deep Six (novel)**

- [d9s0] The Deep Six is a 1953 novel by Martin Dibner (1911-1992) describing the experiences of a group of U.S. Navy sailors fighting in the Aleutian Islands Campaign in 1943 during World War II.
- [d9s1]  The novel, based on the author's experiences serving in the light cruiser USS "Richmond" during the same campaign, is written in a terse Hemingwayesque style and was a contemporary of Nicholas Monsarrat's novel "The Cruel Sea" and "The Caine Mutiny" by Herman Wouk.
- [d9s2]  The novel reached the "New York Times" Bestseller List for the week of September 6, 1953, ranked 16th in sales, and appeared six times on the list until October 18, fluctuating between 14th and 16th.

**d10: The Golden Spiders: A Nero Wolfe Mystery**

- [d10s0] The Golden Spiders: A Nero Wolfe Mystery is a 2000 made-for-television film based on the 1953 novel by Rex Stout.
- [d10s1]  Set in 1950s Manhattan, the A&E Network production stars Maury Chaykin as the heavyweight detective genius Nero Wolfe, and Timothy Hutton as Wolfe's assistant, Archie Goodwin, narrator of the Nero Wolfe stories.
- [d10s2]  Veteran screenwriter Paul Monash adapted the 1953 novel by Rex Stout; Bill Duke directed.
- [d10s3]  When it first aired on the A&E Network March 5, 2000, "The Golden Spiders" was seen in 3.2 million homes, making it the fourth most-watched A&E original movie ever.
- [d10s4]  Its success led to the A&E original series, "A Nero Wolfe Mystery" (2001–2002).

## 27. hotpotqa_5ab3c3b155429969a97a81b6

原位置：`train` 第 177 题 · 全局第 177 题 · `sample_id: hotpotqa_5ab3c3b155429969a97a81b6`

Question: Which film was released first, Big Hero 6 or Muppet Treasure Island?

Note: 

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | release year of Big Hero 6 | False | [] | 2014 | [["d1s0"], ["d2s2"], ["d4s1"], ["d5s1"]] | context |
| u2 | release year of Muppet Treasure Island | False | [] | 1996 | [["d6s0"], ["d10s3"]] | context |
| u3 | which film was released first | True | ["u1", "u2"] | Muppet Treasure Island | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | release year of the film Big Hero 6 | False | [] | 2014 | [['d1s0'], ['d2s2'], ['d4s1'], ['d5s1']] |
| u2 | release year of the film Muppet Treasure Island | False | [] | 1996 | [['d6s0'], ['d10s3']] |
| u3 | which of Big Hero 6 and Muppet Treasure Island was released first | True | ['u1', 'u2'] | Muppet Treasure Island | [[]] |

### Source documents (reference only)

**d1: Big Hero 6 (film)**

- [d1s0] Big Hero 6 is a 2014 American 3D computer-animated superhero-comedy film produced by Walt Disney Animation Studios and released by Walt Disney Pictures.
- [d1s1]  Loosely based on the superhero team of the same name by Marvel Comics, the film is the 54th Disney animated feature film.
- [d1s2]  Directed by Don Hall and Chris Williams, the film tells the story of Hiro Hamada, a young robotics prodigy who forms a superhero team to combat a masked villain.
- [d1s3]  The film features the voices of Scott Adsit, Ryan Potter, Daniel Henney, T.J. Miller, Jamie Chung, Damon Wayans, Jr., Genesis Rodriguez, Alan Tudyk, James Cromwell, and Maya Rudolph.

**d2: Fredzilla**

- [d2s0] Fred (nicknamed Fredzilla) is a fictional character appearing in American comic books published by Marvel Comics.
- [d2s1]  The character appears in particular in "Big Hero 6", which features a team of superheroes of which he is a member.
- [d2s2]  He also appeared in the 2014 Disney animated film "Big Hero 6", which is based on the book.

**d3: Baymax**

- [d3s0] Baymax is a fictional character, a superhero appearing in American comic books published by Marvel Comics.
- [d3s1]  Created by Steven T. Seagle and Duncan Rouleau, Baymax first appeared in "Sunfire & Big Hero 6" #1 (September 1998).
- [d3s2]  Baymax begins his existence as Hiro Takachiho's science project.
- [d3s3]  Originally designed to be a hydro-powered robotic synthformer programmed to serve as Hiro's personal bodyguard, butler, and chauffeur, Baymax becomes Hiro's best friend and father figure when the young inventor programs his recently deceased father's brain engrams into Baymax's artificial intelligence.
- [d3s4]  When the Giri recruits Hiro into the fledgling super-team Big Hero 6, Baymax also joins the team, where his phenomenal strength, and amazing surveillance and data analysis capabilities have proven useful.

**d4: Big Hero 6 (TV series)**

- [d4s0] Big Hero 6: The Series is an upcoming American animated series, produced by Disney Television Animation and currently being developed by "Kim Possible" creators Mark McCorkle and Bob Schooley.
- [d4s1]  The series is based on Disney's 2014 film "Big Hero 6", which itself is loosely based on the comic book series, Big Hero 6 published by Marvel Comics.
- [d4s2]  Scheduled to premiere on Disney XD in November 2017, the series will take place after the events of the film and will use traditional 2D animation.

**d5: Don Hall (filmmaker)**

- [d5s0] Don Hall is an American film director and writer at Walt Disney Animation Studios.
- [d5s1]  He is known for co-directing "Winnie the Pooh" (2011), "Big Hero 6" (2014), which was inspired by the Marvel Comics of the same name and "Moana" (2016), along with Ron Clements and John Musker.
- [d5s2]  "Big Hero 6" won the Oscar for Best Animated Feature in 2015.

**d6: Muppet Treasure Island**

- [d6s0] Muppet Treasure Island is a 1996 American musical adventure comedy film based on Robert Louis Stevenson's "Treasure Island".
- [d6s1]  It is the fifth feature film to star The Muppets, and was directed by Brian Henson.

**d7: Honey Lemon**

- [d7s0] Honey Lemon (Aiko Miyazaki) is a fictional superhero appearing in American comic books published by Marvel Comics.
- [d7s1]  The character is commonly associated with the Japanese team known as Big Hero 6.
- [d7s2]  She was created by Steven T. Seagle and Duncan Rouleau, and first appeared in "Sunfire & Big Hero 6" #1 (September 1998).

**d8: Sam Eagle**

- [d8s0] Sam Eagle is a Muppet character originating from the television show "The Muppet Show", where he was performed by Frank Oz.
- [d8s1]  Sam has appeared in every Muppet film; as himself in "The Muppet Movie", "The Great Muppet Caper", "The Muppets Take Manhattan", "Muppets from Space", and "The Muppets", as well as the Head Schoolmaster in "The Muppet Christmas Carol," Samuel Arrow in "Muppet Treasure Island" and a CIA agent in "Muppets Most Wanted."
- [d8s2]  He also appears in the television series, "The Muppets."

**d9: List of The Muppets productions**

- [d9s0] This is a list of productions based on The Muppets characters and franchise, including films, television series and specials, and other media.
- [d9s1]  The franchise's main work is "The Muppet Show", a syndicated television series which ran from 1976 to 1981.
- [d9s2]  The franchise includes eight feature films; "The Muppet Movie", "The Great Muppet Caper", "The Muppets Take Manhattan", "The Muppet Christmas Carol", "Muppet Treasure Island", "Muppets from Space", "The Muppets", and "Muppets Most Wanted".
- [d9s3]  The franchise also includes other series such as "Muppets Tonight" and "The Muppets".

**d10: Bill Barretta**

- [d10s0] William Paul "Bill" Barretta (born June 19, 1964) is an American puppeteer and producer who has been performing with The Muppets since 1991, when he puppeteered the body of Sinclair family patriarch, Earl Sinclair on "Dinosaurs".
- [d10s1]  He later developed several new characters on "Muppets Tonight", including Pepe the King Prawn, Johnny Fiama, Big Mean Carl and Bobo the Bear.
- [d10s2]  Along with having his own Muppet characters, Barretta has taken over several of Jim Henson's roles, such as Dr. Teeth, Rowlf the Dog, Mahna Mahna and Swedish Chef, and briefly took over Jerry Nelson's role of Lew Zealand.
- [d10s3]  His film debut as a principal puppeteer was in 1996's "Muppet Treasure Island" as Clueless Morgan.
- [d10s4]  In addition, Barretta has produced two of the Muppets' television films, "It's a Very Merry Muppet Christmas Movie" (2002) and "The Muppets' Wizard of Oz" (2005).
- [d10s5]  Barretta also provides additional voices on "Kim Possible".
- [d10s6]  His most recent film performance was in Disney's "Muppets Most Wanted", where he also served as a co-producer.
- [d10s7]  Barretta also served as an executive producer on the ABC series, "The Muppets".

## 28. hotpotqa_5ab42d235542991751b4d6d1

原位置：`train` 第 178 题 · 全局第 178 题 · `sample_id: hotpotqa_5ab42d235542991751b4d6d1`

Question: Who directed the Walt Disney Television movie that John William Minton was a cast member of?

Note: 按照新拆法，检查一下标签

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新两单元，第一单元联合本名—艺名—演员表证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | Walt Disney Television movie that John William Minton was a cast member of | False | [] | Double Agent | [["d6s0", "d3s0", "d3s2"]] | context |
| u2 | director of {u1} | True | ["u1"] | Michael Vejar | [["d3s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | name by which John William Minton is better known | False | [] | Big John Studd | [['d6s0']] |
| u2 | Walt Disney Television movie in which {u1} was a cast member | False | ['u1'] | Double Agent | [['d3s0', 'd3s2']] |
| u3 | director of {u2} | True | ['u2'] | Michael Vejar | [['d3s0']] |

### Source documents (reference only)

**d1: General Hospital cast members**

- [d1s0] "General Hospital" is the longest running American television serial drama, airing on ABC.
- [d1s1]  Created by Frank and Doris Hursley, the series premiered on April 1, 1963.
- [d1s2]  The longest-running cast member is Leslie Charleson, who has portrayed Dr. Monica Quartermaine since August 17, 1977, also making her one of the longest-tenured actors in American soap operas.
- [d1s3]  Former cast member Rachel Ames was previously the series' longest-running cast member, portraying Audrey Hardy from 1964 to 2007, and making guest appearances in 2009 and 2013, the latter for the series' fiftieth anniversary.
- [d1s4]  Ames made a special appearance on October 30, 2015.
- [d1s5]  Actors Genie Francis and Kin Shriner, who portray Laura Spencer and Scott Baldwin, are the second and third longest-running cast members, having joined "General Hospital" in February and August 1977, respectively.
- [d1s6]  Actress Jacklyn Zeman — who portrays Bobbie Spencer — is the fourth longest-running cast member, joining the serial in December 1977.
- [d1s7]  Actress Jane Elliot, who joined the serial in June 1978 as Tracy Quartermaine, is the fifth longest-running cast member, joining "General Hospital" in June 1978 until her departure in May 2017.
- [d1s8]  Former cast member Anthony Geary, who portrayed Luke Spencer, was the sixth longest-running cast member, having joined "General Hospital" in November 1978.
- [d1s9]  The following list is of cast members who are currently on the show: the main and recurring cast members, or those who are debuting, departing or returning to the series.

**d2: Goof Troop**

- [d2s0] Goof Troop is an American animated comedy television series produced by Walt Disney Television Animation.
- [d2s1]  The series focuses on the relationship between single father Goofy and his son, Max; as well as their neighbors Pete and his family.
- [d2s2]  Created by Peter Montgomery, the main series of 65 episodes aired in first-run syndication from 1992 to 1993 on "The Disney Afternoon" programming block, while an additional thirteen episodes aired on Saturday mornings on ABC.
- [d2s3]  A Christmas special was also produced, which aired in syndication on November 1, 1992.
- [d2s4]  Walt Disney Pictures released two films based on the television series: the theatrical "A Goofy Movie", released on April 7, 1995; as well as the direct-to-video sequel and television series finale "An Extremely Goofy Movie", released on February 29, 2000.

**d3: Double Agent (1987 film)**

- [d3s0] Double Agent was a made for TV film from Walt Disney Television directed by Michael Vejar.
- [d3s1]  It starred Michael McKean, Susan Walden, Christopher Burton, Judith Jones, and Lloyd Bochner.
- [d3s2]  Additional cast included Del Zamora, John Putch, Alexa Hamilton, Jane A. Johnston, Lois January, Saveli Kramarov, Allan Kolman, and Big John Studd.
- [d3s3]  Double Agent was first telecast March 29, 1987, on The Disney Sunday Movie series.

**d4: Winnie the Pooh and Christmas Too**

- [d4s0] Winnie the Pooh and Christmas Too is a 1991 Christmas television special based on the Disney television series "The New Adventures of Winnie the Pooh", originally broadcast on Saturday, December 14, 1991 on ABC and produced by Walt Disney Animation (France), S.A. and Walt Disney Television Animation.

**d5: Return to Never Land**

- [d5s0] Return to Never Land (also known as Peter Pan 2 or Peter Pan In: Return to Never Land) is a 2002 American animated musical fantasy-adventure film produced by Walt Disney Television Animation, and released by Walt Disney Pictures and distributed by Walt Disney Studios Motion Pictures.
- [d5s1]  The film is a sequel to Walt Disney Feature Animation 1953 film "Peter Pan", It is based on J. M. Barrie's novel "Peter and Wendy", and had a worldwide gross of $109 million.

**d6: Big John Studd**

- [d6s0] John William Minton (February 19, 1948 – March 20, 1995) was an American professional wrestler and actor, better known by his ring name, Big John Studd.
- [d6s1]  Studd is best known for his appearances with the World Wide Wrestling Federation/World Wrestling Federation in the 1970s and 1980s.

**d7: The 100 Lives of Black Jack Savage**

- [d7s0] Disney Presents The 100 Lives of Black Jack Savage is a television series broadcast in the United States by NBC and produced by Stephen J. Cannell Productions in association with Walt Disney Television.
- [d7s1]  This show originated as a television movie.
- [d7s2]  The program originally aired in 1991, but lasted less than one season.

**d8: Acting Sheriff**

- [d8s0] Acting Sheriff is an unsold, half-hour television pilot created by Walt Disney Television for television network CBS that aired across the United States on Saturday, August 17, 1991.
- [d8s1]  Identified as episode number 895 in Walt Disney Television season number 35, the 30-minute comedy drama featured Robert Goulet as B movie actor Brent McCord who is elected to the unlikely job of sheriff in a small Northern California town.
- [d8s2]  With only an actor's knowledge and experience of what a sheriff does, the McCord character clashes with the local district attorney, character Donna Singer, and eventually lets a bank robber-prisoner escape.
- [d8s3]  Character Mike Swanson, a deputy who is loyal to McCord, captures the escaped prisoner and helps cover for McCord's mistake by informing news reporters that McCord made the capture.

**d9: Recess: School's Out**

- [d9s0] Recess: School's Out is a 2001 American animated comedy film based on the Disney television series "Recess".
- [d9s1]  It was produced by Walt Disney Pictures, Walt Disney Television Animation and Walt Disney Television Animation Digital Production with animation done by Sunwoo Animation and Sunwoo Digital International.
- [d9s2]  The film was distributed by Buena Vista Pictures Distribution, and released theatrically in the United States on February 16, 2001.

**d10: Mickey's House of Villains**

- [d10s0] Mickey's House of Villains (also known as House of Mouse: The Villains) is a 2002 direct-to-video animated film produced by The Walt Disney Company (Walt Disney Television Animation and Toon City Animation, with animation coordination by Walt Disney Feature Animation Florida.
- [d10s1]  It is based on the Disney Channel animated television series "Disney's House of Mouse" and a sequel to the direct-to-video animated film "", starring Mickey Mouse, Donald Duck, Minnie Mouse, Goofy, Daisy Duck and Disney Villains that have appeared in past Disney productions.
- [d10s2]  It was released on both VHS and DVD by Walt Disney Home Video on September 3, 2002.
- [d10s3]  It was followed by a 2004 direct-to-video animated film, "", produced by DisneyToon Studios, on August 17, 2004.

## 29. hotpotqa_5ab443ca5542991779162c43

原位置：`train` 第 179 题 · 全局第 179 题 · `sample_id: hotpotqa_5ab443ca5542991779162c43`

Question: What do Lindsay Anderson and Aaron Kozak have in common?

Note: 保留single

Type: single · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留用户指定 single；共同属性必须联合两方证据，不允许由一方推另一方。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | commonality between Lindsay Anderson and Aaron Kozak | True | [] | filmmaker | [["d5s0", "d3s0"], ["d7s4", "d3s0"], ["d4s0", "d3s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | occupation of Lindsay Anderson | False | [] | filmmaker | [['d5s0'], ['d7s4'], ['d4s0']] |
| u2 | occupation of Aaron Kozak | False | [] | filmmaker | [['d3s0']] |
| u3 | what Lindsay Anderson and Aaron Kozak have in common | True | ['u1', 'u2'] | filmmaker | [[]] |

### Source documents (reference only)

**d1: O Lucky Man!**

- [d1s0] O Lucky Man!
- [d1s1]  is a 1973 British comedy-drama fantasy film, intended as an allegory on life in a capitalist society.
- [d1s2]  Directed by Lindsay Anderson, it stars Malcolm McDowell as Mick Travis, whom McDowell had first played as a disaffected public schoolboy in his first film performance in Anderson's film "if..." (1968).
- [d1s3]  The film was entered into the 1973 Cannes Film Festival.

**d2: Hecate (musician)**

- [d2s0] Rachael Kozak (born May 26, 1976), better known by her stage name Hecate, is an American-Austrian experimental industrial and breakcore musician based in Berlin, Germany.
- [d2s1]  Her stage name originates from Hecate, the Greek goddess of sorcery.
- [d2s2]  Kozak uses sexuality as a major topic in her music (such as in the tracks "Hecate Jacks Off The Jackal" and "The Magick Of Female Ejaculation"), and has a heavy focus on death and the occult.
- [d2s3]  With over thirty releases, she has become a notable producer in the harsher genres of electronic music.
- [d2s4]  Kozak is also known for her collaborations with prolific electronic artist Venetian Snares (Aaron Funk), creating the album "Nymphomatriarch" entirely from recordings of she and Funk having sex, during a two-week tour in 2003.
- [d2s5]  She is also involved with video production, graphic arts and writing.
- [d2s6]  Since 1996, Kozak has managed her own record label Zhark International, has traveled the world extensively to perform, and became involved in the extreme metal scene, particularly industrial black metal.
- [d2s7]  She eventually formed Treachery, a black metal group.

**d3: Aaron Kozak**

- [d3s0] Aaron Kozak (born August 23, 1983) is an American playwright and filmmaker.

**d4: The White Bus**

- [d4s0] The White Bus is a 1967 short film by British director Lindsay Anderson.
- [d4s1]  The screenplay was jointly adapted with Shelagh Delaney from a short story in her collection "Sweetly Sings the Donkey" (1963).

**d5: Lindsay Anderson**

- [d5s0] Lindsay Gordon Anderson (17 April 1923 – 30 August 1994) was a British feature film, theatre and documentary director, film critic, and leading light of the Free Cinema movement and the British New Wave.
- [d5s1]  He is most widely remembered for his 1968 film "if...", which won the "Palme d'Or" at Cannes Film Festival and was Malcolm McDowell's cinematic debut.
- [d5s2]  He is also notable, though not a professional actor, for playing a minor role in the Academy Award winning film "Chariots of Fire".
- [d5s3]  Malcolm McDowell produced a 2007 documentary about his experiences with Lindsay Anderson, "Never Apologize".

**d6: The Long and the Short and the Tall (play)**

- [d6s0] The Long and the Short and the Tall is a play written by British playwright Willis Hall.
- [d6s1]  Set in the Second World War, the play premiered at the Royal Court Theatre in London in January 1959; it was directed by Lindsay Anderson and starred Peter O'Toole and Robert Shaw.
- [d6s2]  It was Anderson's first major production for the Royal Court, transferring to London's West End in April 1959.

**d7: Thursday's Children**

- [d7s0] Thursday's Children is a 1954 British short documentary film directed by Lindsay Anderson about The Royal School for the Deaf in Margate, Kent, UK.
- [d7s1]  The film is nearly silent, apart from music and narration.
- [d7s2]  It focuses on the faces and gestures of the little boys and girls.
- [d7s3]  As a residential school teaching lip reading, rather than a sign language, it features methods and goals not now used, and notes that only one child in three will achieve true speech.
- [d7s4]  Filmmakers Lindsay Anderson and Guy Brenton were unable to gain distribution for the film until it won an Academy Award in 1955 for Documentary Short Subject.

**d8: The Changing Room**

- [d8s0] The Changing Room is a 1971 play by David Storey, set in a men's changing room before, during and after a rugby league football game.
- [d8s1]  It premiered at the Royal Court Theatre on 9 November 1971, directed by Lindsay Anderson.
- [d8s2]  The 1973 Broadway production, directed by Michael Rudman, won several awards including the New York Drama Critics' Circle award for Best Play and the Tony Award for Best Featured Actor for John Lithgow.

**d9: Free Cinema**

- [d9s0] Free Cinema was a documentary film movement that emerged in the United Kingdom in the mid-1950s.
- [d9s1]  The term referred to an absence of propagandised intent or deliberate box office appeal.
- [d9s2]  Co-founded by Lindsay Anderson, though he later disdained the 'movement' tag, with Karel Reisz, Tony Richardson and Lorenza Mazzetti.
- [d9s3]  The movement began with a programme of three short films at the National Film Theatre, London, on 5 February 1956.
- [d9s4]  The programme was such a success that five more programmes appeared under the Free Cinema banner before the founders decided to end the series.
- [d9s5]  The last event was held in March 1959.
- [d9s6]  Three of the screenings consisted of work from overseas film makers.

**d10: In Celebration**

- [d10s0] In Celebration is a 1975 film directed by Lindsay Anderson.
- [d10s1]  It is based in the 1969 stage production of the same name by David Storey which was also directed by Anderson.
- [d10s2]  The movie was produced and released as part of the American Film Theatre, which adapted theatrical works for a subscription-driven cinema series.
- [d10s3]  It was meant to be shown theatrically with tickets sold in advance.

## 30. hotpotqa_5ab461c25542991751b4d754

原位置：`train` 第 180 题 · 全局第 180 题 · `sample_id: hotpotqa_5ab461c25542991751b4d754`

Question: In between Pizza Inn and Extreme Pizza which one was founded in 1994?

Note: 

Type: comparison · fallback: False · SFT snapshots: 5

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | whether Pizza Inn was founded in 1994 | False | [] | no | [] | no_direct_support |
| u2 | whether Extreme Pizza was founded in 1994 | False | [] | yes | [["d7s0"]] | context |
| u3 | which pizza chain was founded in 1994 | True | ["u1", "u2"] | Extreme Pizza | [[]] | question_presupposition |

- u1：无直接支持集合；不能仅由 expected_answer 将本单元标为 SUPPORTED。候选题结论可按独立的 presupposition_sets 路径判断。

- u3：`by_presupposition=true`，预设路径 `[["d7s0"]]`；不是直接证据。

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Pizza Inn was founded in 1994 | False | [] | no | [] |
| u2 | whether Extreme Pizza was founded in 1994 | False | [] | yes | [['d7s0']] |
| u3 | which of Pizza Inn and Extreme Pizza was founded in 1994 | True | ['u1', 'u2'] | Extreme Pizza | [[]] |

### Source documents (reference only)

**d1: California-style pizza**

- [d1s0] California-style pizza (also known as California pizza or Gourmet pizza) is a style of single-serving pizza that combines New York and Italian thin crust with toppings from the California cuisine cooking style.
- [d1s1]  Its invention is generally attributed to chef Ed LaDou, and Chez Panisse, in Berkeley, California.
- [d1s2]  Wolfgang Puck, after meeting LaDou, popularized the style of pizza in the rest of the country.
- [d1s3]  It is served in a number of California Cuisine restaurants.
- [d1s4]  Such restaurant chains as California Pizza Kitchen, Extreme Pizza, and Sammy's Woodfired Pizza are three major pizza franchises associated with California-style pizza.
- [d1s5]  Nancy Silverton's Pizzeria Mozza is also a popular California-style pizza restaurant in Los Angeles.

**d2: Robert L. Brock**

- [d2s0] Robert L. Brock (c. 1924 – June 7, 1998) was an American businessman.
- [d2s1]  He was born in Pawnee Rock, Kansas and graduated from Sterling High School and Kansas University.
- [d2s2]  he started "Inn Operations" with a friend and sold it to Holiday Inns, Inc to manage "Topeka Inn Management".
- [d2s3]  As chairman of TIM (later renamed Brock Hotel Corporation), the first and at the time largest franchisee of Holiday Inns, he founded ShowBiz Pizza Place in 1980 in Topeka, Kansas after becoming a Pizza Time Theatre franchisee.
- [d2s4]  He also started The Residence line of hotels with Jack DeBoer.
- [d2s5]  Marriott later bought the brand and renamed all locations "Residence Inn by Marriott".

**d3: Pizza Inn**

- [d3s0] Pizza Inn is an American restaurant chain and international food franchise, specializing in American-style pan pizza and side dishes.
- [d3s1]  The company is based in the Dallas suburb of The Colony, Texas.

**d4: El Cuartito**

- [d4s0] El Cuartito is a pizza restaurant in Buenos Aires, Argentina founded in September 1934.
- [d4s1]  It is located on Talcahuano 937.
- [d4s2]  El Cuartito's slogan is "The Good Pizza" (Spanish: "La Buena Pizza" ).
- [d4s3]  It has been declared cultural heritage of Buenos Aires.
- [d4s4]  El Cuartito is one of the oldest pizza restaurants in Buenos Aires.
- [d4s5]  The restaurant also specializes in empanadas.

**d5: Peppes Pizza**

- [d5s0] Peppes Pizza is a Norwegian pizza chain that serves American style and Italian style pizza.
- [d5s1]  Peppes is the largest pizza chain in Scandinavia.
- [d5s2]  The restaurant was founded by two Americans, Louis Jordan and his wife Anne from Hartford, Connecticut.
- [d5s3]  The restaurant chain is part of Umoe Catering As which consists of restaurants such as Burger King, TGI Fridays, La Baguette and Cafe Opus.
- [d5s4]  Peppes Pizza is one of the first restaurants that brought foreign food to Norway.
- [d5s5]  9 million pizzas are served by Peppes each year with deliveries in 11 cities in Norway.
- [d5s6]  Their menu was first put online in March 1995.
- [d5s7]  The servings have been described as enough for two people and that the pizza chain is "a cut above the rest".

**d6: Rabbe Grönblom**

- [d6s0] Rabbe Anders Grönblom (May 3, 1950 Helsinki, Finland – June 29, 2015) was a Finland-Swedish businessman who started a successful pizza business in Vaasa, Finland.
- [d6s1]  His first company—a pizzeria—was called "O sole mio" and it was founded in 1976 in the center of Vaasa.
- [d6s2]  From there he expanded to a pizza franchise chain first called "Pizzeria N:o 1".
- [d6s3]  He was known as the "Pizza-emperor" (Pizzakeisari in Finnish), because he was the founder of a well known pizza franchise chain called Kotipizza which was the new name of "Pizzeria N:o 1" which expanded fast outside of Vaasa.
- [d6s4]  The chain is said to be the biggest one in the Nordic countries.
- [d6s5]  He was also the founder of a shipping company called RG Line, a hotel chain called Omenahotelli and another pizza chain called Golden Rax Pizzabuffet.
- [d6s6]  Most of his companies are subsidiaries of Grönblom International LTD, where Rabbe Grönblom acted as director.
- [d6s7]  Golden Rax Pizzabuffet however is nowadays a part of Finland's largest hotel & restaurant company Restel Oy Ltd, where Rabbe Grönblom sat on the board.
- [d6s8]  He was also on the board of the Finnish tyre company Nokian Renkaat (since 2003).

**d7: Extreme Pizza**

- [d7s0] Extreme Pizza is a privately held restaurant franchise chain specializing in conventional and California-style pizza, founded by Todd Parent and Michael Pastor in 1994 in San Francisco, California.
- [d7s1]  The chain currently includes over 30 locations in the United States, and one in Ireland.
- [d7s2]  Most franchises are located in Northern California, as well as other states including Colorado, Texas, Virginia, Washington, Oregon, Idaho, and Michigan.

**d8: Pie Five**

- [d8s0] Pie Five Pizza Co. is a fast casual restaurant chain specializing in handcrafted personal pizza made in less than 5 minutes.
- [d8s1]  The brand is owned by Rave Restaurant Group, which also owns Pizza Inn.
- [d8s2]  As of December 2016, Pie Five has 98 restaurants in the following locations: Alabama, Arkansas, Florida, Georgia, Illinois, Indiana, Kansas, Maryland, Minnesota, Missouri, Nebraska, North Carolina, Oklahoma, Tennessee, Texas, Utah, Kentucky, Virginia and Washington, D.C. with more than 400 additional company-owned and franchise units anticipated.

**d9: Pizza Haven (United States)**

- [d9s0] Pizza Haven was an American Seattle-based pizzeria and pizza delivery chain, known as dial-a-pizza, founded in 1958 and opening its first location in the University District, Seattle near the University of Washington.
- [d9s1]  Pizza Haven was one of the first pizza companies to make deliveries.
- [d9s2]  Restaurant employees used radio phones to relay orders to roving drivers who carried stacks of pizzas in warming ovens in the back of their jeeps and pickup trucks.

**d10: Fox's Pizza Den**

- [d10s0] Fox's Pizza Den is a pizzeria chain based in Murrysville, Pennsylvania, United States.
- [d10s1]  It was founded in 1971 by Jim Fox in Pitcairn, Pennsylvania, and currently has more than 250 locations in 28 U.S. states, all franchise-owned.
- [d10s2]  Fox's Pizza Den has consistently ranked among the Top 25 pizza chains in the world.
- [d10s3]  The Small Business Administration named Jim Fox as one of the country's top entrepreneurs during National Small Business Week, May 5–11, 2002.
- [d10s4]  Since that time, many Fox's Franchises have closed due to a poor business model.
- [d10s5]  The alarming rate of failure lead to the SBA discontinuing the lending of money for Fox's Franchises.
- [d10s6]  Fox's Pizza was ranked "Best Pizza Franchise" in 2007.
