# Revised Gold — batch 8

原始review保持不变。本文是依据原note生成的修订草稿；完整修改说明见[修改报告](../change_report.md)。

句子带有文档标题；允许使用标题解析该文档中的人名及代词。support_sets内为AND，组间为OR；presupposition_sets按现有评估器表示预设捷径。

## Q211 — `hotpotqa_5a8e276b5542995a26add468` (revised draft)

> Which band formed first, Swervedriver or Incubus?

Source answer: Swervedriver

Gold final answer: Swervedriver

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: formation year of Swervedriver | false | 1989 | — | [d4s0] | — |
| u2: formation year of Incubus | false | 1991 | — | [d3s1] | — |
| u3: Which band formed first, Swervedriver or Incubus? | true | Swervedriver | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d3s1` Incubus (band) [1]: The band was formed in 1991 by vocalist Brandon Boyd, lead guitarist Mike Einziger, and drummer Jose Pasillas while enrolled in Calabasas High School and later expanded to include bassist Alex "Dirk Lance" Katunich, and Gavin "DJ Lyfe" Koppell; both of whom were eventually replaced by bassist Ben Kenney and DJ Kilmore respectively.
- `d4s0` Swervedriver [0]: Swervedriver are an English alternative rock band formed in Oxford in 1989 around core members Adam Franklin and Jimmy Hartridge.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Cruelty's Heart [0]: Cruelty's Heart is a Danish/English Pagan Black Metal band formed in 2009.
- `d1s1` Cruelty's Heart [1]: The band was formed by Bloodletter, Jens Forsberg-Olesen, Mikael Dupont, and Mads Holm Jensen.
- `d1s2` Cruelty's Heart [2]: They are signed to the record company UKEM Records.
- `d1s3` Cruelty's Heart [3]: The band's lyrical themes are heavily influenced by English Germanic Tales, and Anglo-Saxon culture/history.
- `d1s4` Cruelty's Heart [4]: Their first demo, "Die for Woden" was released in 2011.
- `d1s5` Cruelty's Heart [5]: In 2012, the band released their first Full-Length album titled "Rex Anglorvm Saxonvm", mainly containing lyrics on Germanic history and Saxon culture of England.
- `d1s6` Cruelty's Heart [6]: In 2014, Cruelty's Heart did a split with the English Black Metal band, Frostwork.
- `d2s0` Time Lapse Consortium [0]: Time-Lapse Consortium is an American band formed in 2003.
- `d2s1` Time Lapse Consortium [1]: Their sound is described as Psychedelic, Jazz, and Funk.
- `d2s2` Time Lapse Consortium [2]: The group consists of current Incubus members Mike Einziger on Guitar, Jose Pasillas on drums, Ben Kenney on Bass (although he was not a member of Incubus at the time of joining Time Lapse Consortium), Neal Evans of Soulive on Organ, and Suzie Katayama contributing on string arrangements.
- `d3s0` Incubus (band) [0]: Incubus is an American rock band from Calabasas, California.
- `d3s1` Incubus (band) [1]: The band was formed in 1991 by vocalist Brandon Boyd, lead guitarist Mike Einziger, and drummer Jose Pasillas while enrolled in Calabasas High School and later expanded to include bassist Alex "Dirk Lance" Katunich, and Gavin "DJ Lyfe" Koppell; both of whom were eventually replaced by bassist Ben Kenney and DJ Kilmore respectively.
- `d4s0` Swervedriver [0]: Swervedriver are an English alternative rock band formed in Oxford in 1989 around core members Adam Franklin and Jimmy Hartridge.
- `d4s1` Swervedriver [1]: Between 1989 and 1998, the band released four studio albums and numerous EPs and singles despite a considerable flux of members, managers, and record labels.
- `d4s2` Swervedriver [2]: By 1993 the band’s lineup had settled with Franklin on vocals/guitar, Hartridge on guitar, Jez Hindmarsh on drums, and Steve George on bass.
- `d4s3` Swervedriver [3]: They had emerged with a heavier rock sound than their shoegaze contemporaries, and over the next five years it evolved to include elements of psychedelia, classic pop, and indie rock.
- `d4s4` Swervedriver [4]: In 2008, the band reunited for touring purposes.
- `d4s5` Swervedriver [5]: They released their first new single in fifteen years in September 2013, and their first full-length album in seventeen years in March 2015.
- `d5s0` The Zombie Kids [0]: The Zombie Kids is a band formed by Edgar Candel Kerri and Cumhur Jay, two disc jockeys and record producers who live in Spain.
- `d5s1` The Zombie Kids [1]: The newly formed band became popular with their debut in Rock in Rio (Lisbon 2010) and the release of their first single "Face" (2010), which was a great success.
- `d5s2` The Zombie Kids [2]: The song was chosen to be part of the O.S.T of the movie "Tengo ganas de ti" and the Mexican brewery advertisement of "Cerveza Indio".
- `d5s3` The Zombie Kids [3]: Its good acceptance made the record label Universal Music sign an agreement with the band to record its first album, "The Zombie Kids", which went on sale 27 July 2012.
- `d5s4` The Zombie Kids [4]: That same year, the band was awarded with the Best Spanish Artist of the "MTV European Music Awards".
- `d5s5` The Zombie Kids [5]: During the summer of 2013 The Zombie Kids was the musical band which had performed the most in public.
- `d5s6` The Zombie Kids [6]: They have also launched their first project "TZK Radio" with monthly sessions with which they have made public their new song "My House is Your House" feat.
- `d5s7` The Zombie Kids [7]: MC Ambush.
- `d6s0` Giants of Science [0]: Giants of Science is a band formed in Brisbane in Queensland.
- `d6s1` Giants of Science [1]: They refer to their music as "nerd-core" and have been influenced by Split Enz Swervedriver, Sparklehorse, Superchunk, Brisbane underground rock legends the KT26ers, and Sonic's Rendezvous Band.
- `d6s2` Giants of Science [2]: They have supported MC5, Rollins Band, A Perfect Circle, and Mudhoney and have toured in Canada.
- `d6s3` Giants of Science [3]: Their album "Here Is The Punishment" debuted at #4 on the national AIR independent albums chart.
- `d7s0` Kilburn and the High Roads [0]: Kilburn and the High Roads were a British pub rock band formed by Ian Dury in 1970, and the first band formed by Dury.
- `d7s1` Kilburn and the High Roads [1]: The band released one studio album in 1975 before disbanding the same year.
- `d7s2` Kilburn and the High Roads [2]: Allmusic credits the band with being "an undeniable influence on punk and new wave".
- `d8s0` Acrassicauda [0]: Acrassicauda is an American-based Iraqi heavy metal band formed in 2001.
- `d8s1` Acrassicauda [1]: It is often credited as being the first heavy metal group to emerge from Iraq.
- `d8s2` Acrassicauda [2]: The original band consisted of three Arab members and one Assyrian (Tony Aziz Yaqoo).
- `d8s3` Acrassicauda [3]: The band formed and played concerts under the regime of Saddam Hussein.
- `d8s4` Acrassicauda [4]: It became well known outside of the local Iraqi metal scene after Vice magazine did a profile of the band.
- `d8s5` Acrassicauda [5]: It received even greater coverage when it was profiled in a feature-length documentary about the band and its troubles in Iraq called "Heavy Metal in Baghdad".
- `d8s6` Acrassicauda [6]: The band's first album was released on March 9, 2010.
- `d9s0` The Vermin [0]: The Vermin is a punk rock band from Las Vegas, Nevada.
- `d9s1` The Vermin [1]: The band formed in 1984 (1986 in some sources)as Vermin From Venus by singer and guitarist Dirk Vermin, and was noted for releasing one of the first independent punk rock albums in Las Vegas, "Sex on Planet X".
- `d9s2` The Vermin [2]: In 1994, Vermin and bassist Rob Ruckus formed a punk cover band called Godboy, and in 1995 the bands merged, adopting the name The Vermin.
- `d9s3` The Vermin [3]: The band recorded their first album under their new name, "Hell or Las Vegas", in 1996 with drummer Anthony Hudak, but Hudak left the band soon after and was immediately replaced with current drummer Gerry "Turbo" Proctor.
- `d9s4` The Vermin [4]: The band was featured in the low-budget horror film "Trans-American Killer" in 2005.
- `d9s5` The Vermin [5]: Singer Dirk Vermin opened Pussykat Tattoo in 1999; the shop, Vermin, and bassist Ruckus are currently featured in the A&E program "Bad Ink".
- `d10s0` The Strap-Ons [0]: The Strap-Ons are a punk rock band formed by vocalist Brian "Idle" Diederich, guitarist Billy England, bassist Emmit Joe George and drummer Ruben Remulla.
- `d10s1` The Strap-Ons [1]: A few months later, guitarist Kate Grottenhaler joined the group.
- `d10s2` The Strap-Ons [2]: The band formed in late 1996 originally as The Pimps in Norfolk, Virginia, but due to legal disputes, were forced to change their name to The Strap-Ons.
- `d10s3` The Strap-Ons [3]: The band's first CD was put out by a cooperative of six labels around the world called The World Label Cooperative.

</details>

## Q212 — `hotpotqa_5a8e2ba05542995085b373b8` (revised draft)

> Are the libretto of Tristan und Isolde and Ariane et Barbe-bleue in the same language?

Source answer: no

Gold final answer: no

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: libretto language of Tristan und Isolde | false | German | — | [d7s0] | — |
| u2: libretto language of Ariane et Barbe-bleue | false | French | — | [d4s1] | — |
| u3: Are the libretto of Tristan und Isolde and Ariane et Barbe-bleue in the same language? | true | no | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d4s1` Ariane et Barbe-bleue [1]: The French libretto is adapted (with very few changes) from the symbolist play of the same name by Maurice Maeterlinck, itself loosely based on the French literary tale "La Barbe bleue" by Charles Perrault.
- `d7s0` Tristan und Isolde [0]: Tristan und Isolde ("Tristan and Isolde", or "Tristan and Isolda", or "Tristran and Ysolt") is an opera, or music drama, in three acts by Richard Wagner to a German libretto by the composer, based largely on the romance by Gottfried von Strassburg.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Gottfried von Strassburg [0]: Gottfried von Strassburg (died c. 1210) is the author of the Middle High German courtly romance "Tristan", an adaptation of the 12th-century "Tristan and Iseult" legend.
- `d1s1` Gottfried von Strassburg [1]: Gottfried's work is regarded, alongside Wolfram von Eschenbach's "Parzival" and the "Nibelungenlied", as one of the great narrative masterpieces of the German Middle Ages.
- `d1s2` Gottfried von Strassburg [2]: He is probably also the composer of a small number of surviving lyrics.
- `d1s3` Gottfried von Strassburg [3]: His work became a source of inspiration for Richard Wagner's opera "Tristan und Isolde" (1865).
- `d2s0` Johanna Meier [0]: Johanna Meier (born February 13, 1938) is an American operatic soprano.
- `d2s1` Johanna Meier [1]: She has been described as "one of the foremost Wagnerian sopranos of her era".
- `d2s2` Johanna Meier [2]: She had an international career, including fourteen years at the Metropolitan Opera and three summers singing the role of Isolde in Wagner's "Tristan und Isolde" for the Bayreuth Festival—the Festival's first American Isolde.
- `d3s0` Georgette Leblanc [0]: Georgette Leblanc (8 February 1869 Rouen, – 27 October 1941 Le Cannet, near Cannes) was a French operatic soprano, actress, author, and the sister of novelist Maurice Leblanc.
- `d3s1` Georgette Leblanc [1]: She became particularly associated with the works of Jules Massenet and was an admired interpreter of the title role in Bizet's "Carmen".
- `d3s2` Georgette Leblanc [2]: For many years Leblanc was the lover of Belgian playwright and writer Maurice Maeterlinck, and he wrote several parts for her within his stage plays.
- `d3s3` Georgette Leblanc [3]: She portrayed the role of Ariane in "Ariane et Barbe-bleue", both in the original 1899 stage play by Maeterlinck and in the 1907 opera adaptation by Paul Dukas.
- `d3s4` Georgette Leblanc [4]: Leblanc also appeared in a couple of French films, most notably "L'Inhumaine" in 1924.
- `d3s5` Georgette Leblanc [5]: In the last few decades of her life she turned to writing, producing two commercially successful autobiographies and several children's books and travelogues.
- `d4s0` Ariane et Barbe-bleue [0]: Ariane et Barbe-bleue ("Ariadne and Bluebeard") is an opera in three acts by Paul Dukas.
- `d4s1` Ariane et Barbe-bleue [1]: The French libretto is adapted (with very few changes) from the symbolist play of the same name by Maurice Maeterlinck, itself loosely based on the French literary tale "La Barbe bleue" by Charles Perrault.
- `d5s0` Yseult Island [0]: Yseult Island is a small rocky island 0.7 nmi east of Tristan Island and 0.4 nmi north of the east point on Cape Jules.
- `d5s1` Yseult Island [1]: Photographed from the air by U.S. Navy Operation Highjump, 1946-47.
- `d5s2` Yseult Island [2]: Charted by the French Antarctic Expedition under Barre, 1951–52, and so named because of its twin relationship with Tristan Island.
- `d5s3` Yseult Island [3]: Yseult is the French spelling of Isolde, legendary heroine incorporated into Arthurian legend and later popularized by Richard Wagner's opera "Tristan und Isolde".
- `d6s0` Paul Dukas [0]: Paul Abraham Dukas (] ; 1 October 1865 – 17 May 1935) was a French composer, critic, scholar and teacher.
- `d6s1` Paul Dukas [1]: A studious man, of retiring personality, he was intensely self-critical, and he abandoned and destroyed many of his compositions.
- `d6s2` Paul Dukas [2]: His best known work is the orchestral piece "The Sorcerer's Apprentice" ("L'apprenti sorcier"), the fame of which has eclipsed that of his other surviving works.
- `d6s3` Paul Dukas [3]: Among these are the opera "Ariane et Barbe-bleue", a symphony, two substantial works for solo piano, and a ballet, "La Péri".
- `d7s0` Tristan und Isolde [0]: Tristan und Isolde ("Tristan and Isolde", or "Tristan and Isolda", or "Tristran and Ysolt") is an opera, or music drama, in three acts by Richard Wagner to a German libretto by the composer, based largely on the romance by Gottfried von Strassburg.
- `d7s1` Tristan und Isolde [1]: It was composed between 1857 and 1859 and premiered at the Königliches Hof- und Nationaltheater in Munich on 10 June 1865 with Hans von Bülow conducting.
- `d7s2` Tristan und Isolde [2]: Wagner referred to the work not as an opera, but called it "eine Handlung" (literally "a drama", "a plot" or "an action"), which was the equivalent of the term used by the Spanish playwright Calderón for his dramas.
- `d8s0` Fire and Sword [0]: Fire and Sword ("Feuer und Schwert – Die Legende von Tristan und Isolde") is a 1982 German romance/adventure film, directed by .
- `d8s1` Fire and Sword [1]: It is based on the legend of Tristan and Iseult.
- `d9s0` Tristan chord [0]: The Tristan chord is a chord made up of the notes F, B, D♯ , and G♯ .
- `d9s1` Tristan chord [1]: More generally, it can be any chord that consists of these same intervals: augmented fourth, augmented sixth, and augmented ninth above a bass note.
- `d9s2` Tristan chord [2]: It is so named as it is heard in the opening phrase of Richard Wagner's opera "Tristan und Isolde" as part of the leitmotif relating to Tristan.
- `d10s0` Dalit Warshaw [0]: Dalit Hadass Warshaw (born August 6, 1974) is a New York-based composer, pianist, thereminist.
- `d10s1` Dalit Warshaw [1]: Previously on the composition and music theory faculty of Boston Conservatory, she currently serves on the composition faculty at CUNY-Brooklyn College.
- `d10s2` Dalit Warshaw [2]: Her works have been performed by dozens of orchestral ensembles, including the New York Philharmonic and Israel Philharmonic Orchestras (Zubin Mehta conducting), the Boston Symphony, the Cleveland Orchestra, the Houston Symphony, the Y Chamber Orchestra, the Colorado Symphony and the Albany Symphony Orchestra.
- `d10s3` Dalit Warshaw [3]: In April 2006, her piece "After the Victory" for orchestra and chorus, was premiered by the Grand Rapids Symphony and the North American Choral Company.
- `d10s4` Dalit Warshaw [4]: Her first recording, entitled "Invocations" was released by Albany Records in 2011.
- `d10s5` Dalit Warshaw [5]: Her first piano concerto, "Conjuring Tristan," was commissioned by the Grand Rapids Symphony in 2014.
- `d10s6` Dalit Warshaw [6]: The work was inspired by Richard Wagner's "Tristan und Isolde," as well as by Thomas Mann's novella "Tristan."
- `d10s7` Dalit Warshaw [7]: The piece received its world premiere in January 2015, with Warshaw as the soloist.

</details>

## Q213 — `hotpotqa_5a8e42d15542995a26add4a6` (revised draft)

> Zhangye and Nan'an, Fujian are both located where?

Source answer: People's Republic of China

Gold final answer: People's Republic of China

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: country containing Zhangye | false | People's Republic of China | — | [d10s0] | — |
| u2: country containing Nan'an, Fujian | false | People's Republic of China | — | [d8s0] | — |
| u3: Zhangye and Nan'an, Fujian are both located where? | true | People's Republic of China | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d8s0` Nan'an, Fujian [0]: Nan'an () is a county-level city of southern Fujian province, People's Republic of China.
- `d10s0` Zhangye [0]: Zhangye, formerly romanized as Changyeh or known as Kanchow, is a prefecture-level city in central Gansu Province in the People's Republic of China.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Zhangye Railway Station [0]: Zhangye Railway Station is located 6.4 km north east of Zhangye, Gansu.
- `d1s1` Zhangye Railway Station [1]: It handles about 49 passenger services per day along the Lanzhou–Xinjiang Railway as well as being a major freight depot.
- `d2s0` Zhangye West Railway Station [0]: Zhangye West Railway Station () is a railway station located in China's Gansu Province, Zhangye City, Ganzhou District.
- `d2s1` Zhangye West Railway Station [1]: It was put into operation on December 26, 2014.
- `d2s2` Zhangye West Railway Station [2]: It serves the Lanzhou–Xinjiang High-Speed Railway with High Speed services between Lanzhou and Urumqi and conventional services connecting Urumqi to various cities in Eastern and South Western China.
- `d2s3` Zhangye West Railway Station [3]: It is the second railway station serving Zhangye, with Zhangye Railway Station which serves the conventional LanXin Railway.
- `d3s0` Zhangye Ganzhou Airport [0]: Zhangye Ganzhou Airport (IATA: YZY, ICAO: ZLZY) , or Zhangye Southeast Air Base, is a dual-use military and civil airport serving the city of Zhangye in Gansu Province, China.
- `d3s1` Zhangye Ganzhou Airport [1]: It is located 24 kilometers from the city center.
- `d3s2` Zhangye Ganzhou Airport [2]: Construction began in May 2010 to convert the air base to a dual-use airport, at an estimated cost of 313 million yuan.
- `d3s3` Zhangye Ganzhou Airport [3]: The airport was opened on 1 November 2011.
- `d4s0` Zhangye National Geopark [0]: The Gansu Zhangye National Geopark (, herein, the ″Zhangye National Geopark″), is located in Sunan and Linze counties within the prefecture-level city of Zhangye.
- `d4s1` Zhangye National Geopark [1]: It covers an area of 322 km2 .
- `d4s2` Zhangye National Geopark [2]: The site became a quasi-national geopark on April 23, 2012 (provisional name: Gansu Zhangye Danxia Geopark).
- `d4s3` Zhangye National Geopark [3]: It was formally designated as ″Gansu Zhangye National Geopark″ by the Ministry of Land and Resources on June 16, 2016 after it has passed the on-site acceptance test.
- `d4s4` Zhangye National Geopark [4]: Known for its colorful rock formations, it has been voted by Chinese media outlets as one of the most beautiful landforms in China.
- `d5s0` The Nan'ao General Headquarters [0]: The Nan'ao General Headquarters (南澳总兵府) is located in Nan'ao County, Shantou, Guangdong province, China.
- `d5s1` The Nan'ao General Headquarters [1]: It served as a military center for coastal defense of Guangdong, Fujian province, and Taiwan.
- `d5s2` The Nan'ao General Headquarters [2]: Now the Headquarters is used as a museum of coast defense.
- `d6s0` Rally China [0]: The Rally China (中國拉力賽) is the largest rally racing event held in China.
- `d6s1` Rally China [1]: The first event was run as the "China Rally" in 1997 in the province of Guangdong, as a replacement to the Hong Kong - Beijing Rally, and was an event on the World Rally Championship (WRC) calendar in 1999.
- `d6s2` Rally China [2]: However it was replaced by the Cyprus Rally the following year.
- `d6s3` Rally China [3]: From 2000 to 2015, it has been part of the Asia Pacific Rally Championship (APRC), moving initially to Shaoguan, Fujian province. "
- `d6s4` Rally China [4]: "Force majeure because of government"", according to the organisers, led to the cancellation of the event in 2003.
- `d6s5` Rally China [5]: The event moved for a single year to Huizhou, Guangdong in 2004 before reverting to Shaoguan.
- `d6s6` Rally China [6]: From 2009 until 2015, the event was hosted in Longyou, Zhejiang province.
- `d6s7` Rally China [7]: The event will return to the WRC calendar in 2016 after moving to Huairou, Beijing.
- `d6s8` Rally China [8]: China will continue to host a round of the Asia-Pacific Rally Championship in Zhangye, Gansu in 2016 too, while Longyou will continue to host a round of the Chinese Rally Championship.
- `d7s0` Nan, Thailand [0]: Nan (Thai: น่าน ,  ] ) is a town in northern Thailand.
- `d7s1` Nan, Thailand [1]: It is 668 km north of Bangkok.
- `d7s2` Nan, Thailand [2]: It is in the centre of Nan Province which bears its name, and of which it is the former administrative capital.
- `d7s3` Nan, Thailand [3]: It covers the whole "tambon" Nai Wiang and parts of "tambon" Pha Sing of Mueang Nan district, an area of 7.60 km².
- `d7s4` Nan, Thailand [4]: In 2010 it had a population of 21,333.
- `d7s5` Nan, Thailand [5]: It is subdivided into 30 "chumchon".
- `d7s6` Nan, Thailand [6]: It is spread along the Nan River's right bank.
- `d7s7` Nan, Thailand [7]: Nan is a small city, primarily devoted to commercial, administrative, educational, and hospital activities.
- `d7s8` Nan, Thailand [8]: The old heart of the city, where Wat Phumin, the national museum and other tourist attractions are located, is being restored.
- `d7s9` Nan, Thailand [9]: The city's industrial and tourist development remains limited until now, but should be improved by the complete opening of the border towards Laos and beyond towards China.
- `d8s0` Nan'an, Fujian [0]: Nan'an () is a county-level city of southern Fujian province, People's Republic of China.
- `d8s1` Nan'an, Fujian [1]: It is under the administration of Quanzhou City and as of 2010, had a total population of 1,500,000.
- `d8s2` Nan'an, Fujian [2]: More than 3,000,000 overseas Chinese trace their ancestry to Nan'an.
- `d9s0` Fujian Medical University [0]: Fujian Medical University () is a university located in Fuzhou, Fujian, China.
- `d9s1` Fujian Medical University [1]: Fujian Medical University was founded in1937, named Fujian Provincial Medical Vocational School at that time.
- `d9s2` Fujian Medical University [2]: The name of the school was changed to Fujian Provincial Medical College in 1939 and was called Fujian Medical College in 1949.
- `d9s3` Fujian Medical University [3]: In 1969, after merging with Fujian Chinese Traditional Medical College and the medical department of Huaqiao University, Fujian Medical University was founded and moved to Quanzhou, Fujian.
- `d9s4` Fujian Medical University [4]: It was moved back to Fuzhou in 1978.
- `d9s5` Fujian Medical University [5]: The name of the school was changed back to Fujian Medical College in 1982 and then changed back to the present name in April 1996.
- `d10s0` Zhangye [0]: Zhangye, formerly romanized as Changyeh or known as Kanchow, is a prefecture-level city in central Gansu Province in the People's Republic of China.
- `d10s1` Zhangye [1]: It borders Inner Mongolia on the north and Qinghai on the south.
- `d10s2` Zhangye [2]: Its central district is Ganzhou, formerly a city of the Western Xia and one of the most important outposts of western China.

</details>

## Q214 — `hotpotqa_5a8f64e0554299458435d60b` (revised draft)

> Which documentary film was released first, Chicken Ranch or The End of Suburbia?

Source answer: Chicken Ranch

Gold final answer: Chicken Ranch

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: film year of Chicken Ranch | false | 1983 | — | [d7s0] | — |
| u2: film year of The End of Suburbia | false | 2004 | — | [d8s0] | — |
| u3: Which documentary film was released first, Chicken Ranch or The End of Suburbia? | true | Chicken Ranch | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d7s0` Chicken Ranch (film) [0]: Chicken Ranch is a 1983 documentary film by Nick Broomfield about the famous legalised brothel, the Chicken Ranch, in Pahrump, Nevada.
- `d8s0` The End of Suburbia [0]: The End of Suburbia: Oil Depletion and the Collapse of The American Dream is a 2004 documentary film concerning peak oil and its implications for the suburban lifestyle, written and directed by Toronto-based filmmaker Gregory Greene.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Single Video Theory [0]: Single Video Theory is a music documentary directed by Mark Pellington that follows the making of "Yield", the fifth album by the American alternative rock band Pearl Jam.
- `d1s1` Single Video Theory [1]: It was released first on VHS on August 4, 1998, and then on DVD on November 24, 1998.
- `d2s0` Chicken Ranch (Texas) [0]: The Chicken Ranch was an illegal but tolerated brothel in the U.S. state of Texas that operated from 1905 until 1973.
- `d2s1` Chicken Ranch (Texas) [1]: It was located in Fayette County about 2.5 mi east of downtown La Grange.
- `d2s2` Chicken Ranch (Texas) [2]: The business was established by Miss Jessie Williams, and was the basis for the 1973 ZZ Top song, "La Grange", the 1978 Broadway musical "The Best Little Whorehouse in Texas", and its 1982 film adaptation.
- `d3s0` Exterminate! (song) [0]: "Exterminate!"
- `d3s1` Exterminate! (song) [1]: is a song recorded by the German band Snap!
- `d3s2` Exterminate! (song) [2]: featuring Niki Haris.
- `d3s3` Exterminate! (song) [3]: The song is based on the track "Ex-Terminator" from their 1992 album "The Madman's Return" and was included in later editions of the album.
- `d3s4` Exterminate! (song) [4]: Released first at the end of 1992, it was a hit in several countries, particularly in France, Switzerland, the Netherlands, Norway, Austria and the United Kingdom, where it climbed to number two, and spent 15 weeks on the charts.
- `d4s0` Snegithiye [0]: Snegithiye (English:Oh Friend! "
- `d4s1` Snegithiye [1]: (female)" ) is a 2000 Tamil mystery thriller film directed by Priyadarshan.
- `d4s2` Snegithiye [2]: The story is loosely based on the 1999 Marathi film "Bindhaast" written by Chandrakant Kulkarni.
- `d4s3` Snegithiye [3]: The film notably features only female characters in the lead roles, played by Jyothika, Sharbani Mukherjee, Tabu and Ishita Arun.
- `d4s4` Snegithiye [4]: Music was composed by Vidyasagar.
- `d4s5` Snegithiye [5]: The film, released in 2000, proved to be an average grosser at the box office but bagged positive reviews from critics.
- `d4s6` Snegithiye [6]: Today, it is considered a cult classic that was underrated at the time of its release.
- `d4s7` Snegithiye [7]: Originally planned to be made as a bilingual, in Tamil and in Malayalam, the film released first in Tamil only, while the Malayalam dubbed version, "Raakilipattu", as well as the dubbed Hindi version, "Friendship", released seven years later.
- `d5s0` List of songs in Guitar Hero II [0]: "Guitar Hero II" is a music video game developed by Harmonix and distributed by RedOctane, and is a sequel to "Guitar Hero".
- `d5s1` List of songs in Guitar Hero II [1]: The game was released first to PlayStation 2 in 2006 , but later released for the Xbox 360 in 2007 .
- `d5s2` List of songs in Guitar Hero II [2]: "Guitar Hero II" challenges players to recreate the lead guitar portions of many rock music songs using a specially designed guitar-shaped controller, based on either a Gibson SG for the PlayStation 2 version, a Gibson Explorer for the Xbox 360 version, or else a standard console controller.
- `d5s3` List of songs in Guitar Hero II [3]: As notes scroll down the screen towards the player, the player must hit both the fret buttons on the guitar controller and the strum bar at the same time in order to successfully hit the notes.
- `d5s4` List of songs in Guitar Hero II [4]: Successfully hitting notes improves the player's performance in the game and also raises their score, while missing notes will reduce the player's performance, and a poor performance may end the song prematurely.
- `d5s5` List of songs in Guitar Hero II [5]: Each song can be played at one of four difficulty levels: Easy, Medium, Hard and Expert.
- `d5s6` List of songs in Guitar Hero II [6]: These levels reflect the number of fret buttons used and the number and frequency of the notes to be performed.
- `d6s0` 1950s in jazz [0]: By the end of the 1940s, the nervous energy and tension of bebop was replaced with a tendency towards calm and smoothness, with the sounds of cool jazz, which favoured long, linear melodic lines.
- `d6s1` 1950s in jazz [1]: It emerged in New York City, as a result of the mixture of the styles of predominantly white swing jazz musicians and predominantly black bebop musicians, and it dominated jazz in the first half of the 1950s.
- `d6s2` 1950s in jazz [2]: The starting point were a series of singles on Capitol Records in 1949 and 1950 of a nonet led by trumpeter Miles Davis, collected and released first on a ten-inch and later a twelve-inch as the "Birth of the Cool".
- `d6s3` 1950s in jazz [3]: Cool jazz recordings by Chet Baker, Dave Brubeck, Bill Evans, Gil Evans, Stan Getz and the Modern Jazz Quartet usually have a "lighter" sound which avoided the aggressive tempos and harmonic abstraction of bebop.
- `d6s4` 1950s in jazz [4]: Cool jazz later became strongly identified with the West Coast jazz scene, but also had a particular resonance in Europe, especially Scandinavia, with emergence of such major figures as baritone saxophonist Lars Gullin and pianist Bengt Hallberg.
- `d6s5` 1950s in jazz [5]: The theoretical underpinnings of cool jazz were set out by the blind Chicago pianist Lennie Tristano, and its influence stretches into such later developments as Bossa nova, modal jazz, and even free jazz.
- `d6s6` 1950s in jazz [6]: See also the list of cool jazz and West Coast musicians for further detail.
- `d7s0` Chicken Ranch (film) [0]: Chicken Ranch is a 1983 documentary film by Nick Broomfield about the famous legalised brothel, the Chicken Ranch, in Pahrump, Nevada.
- `d7s1` Chicken Ranch (film) [1]: Photographed by Sandi Sissel.
- `d8s0` The End of Suburbia [0]: The End of Suburbia: Oil Depletion and the Collapse of The American Dream is a 2004 documentary film concerning peak oil and its implications for the suburban lifestyle, written and directed by Toronto-based filmmaker Gregory Greene.
- `d9s0` Escape from Suburbia [0]: Escape from Suburbia: Beyond the American Dream is a 2007 Canadian documentary film written and directed by Gregory Greene, as a sequel to Greene's film "The End of Suburbia", and set to address what is termed "the upcoming energy crisis".
- `d9s1` Escape from Suburbia [1]: Through interviews with individuals, Gregory Greene outlines potential solutions to the coming energy crisis.
- `d10s0` La Grange (song) [0]: La Grange is a song by the American rock group ZZ Top, from their 1973 album "Tres Hombres".
- `d10s1` La Grange (song) [1]: One of ZZ Top's most successful songs, it was released as a single in 1973 and received extensive radio play, rising to No. 41 on the "Billboard" Hot 100 in 1974.
- `d10s2` La Grange (song) [2]: The song refers to a brothel on the outskirts of La Grange, Texas (later called the "Chicken Ranch").
- `d10s3` La Grange (song) [3]: The brothel is also the subject of the Broadway play and film "The Best Little Whorehouse in Texas", the latter starring Dolly Parton and Burt Reynolds.

</details>

## Q215 — `hotpotqa_5a902d5155429933b8a2048d` (revised draft)

> Where is the transmitter of the television station licensed to Topeka, KS, located?

Source answer: on Windy Hill Road in Maple Hill

Gold final answer: on Windy Hill Road in Maple Hill

Question type: `single` (source type `bridge`)

Original question: Where is a television transmitter located in Topeka, KS?

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: Where is the transmitter of the television station licensed to Topeka, KS, located? | true | on Windy Hill Road in Maple Hill | — | [d5s0, d5s2] OR [d1s0, d1s2] | — |

Evidence:

- `d1s0` WIBW-DT2 [0]: WIBW-DT2 is a primary MyNetworkTV- and secondary MeTV-affiliated television station located in Topeka, Kansas, United States.
- `d1s2` WIBW-DT2 [2]: Over-the-air, it broadcasts a standard definition digital signal on VHF channel 13.2 from a transmitter located on Windy Hill Road in Maple Hill.
- `d5s0` WIBW-TV [0]: WIBW-TV, virtual and VHF digital channel 13, is a CBS-affiliated television station licensed to Topeka, Kansas, United States.
- `d5s2` WIBW-TV [2]: WIBW-TV maintains studio facilities located on Commerce Place (next to the interchange of I-70, I-470, US 40, US 75 and K-4) in southwestern Topeka, and its transmitter is located on Windy Hill Road in Maple Hill.

Notes:

- 题干澄清：区分电视台许可城市Topeka与发射机所在地Maple Hill；证据和答案不变。

<details><summary>All source context</summary>

- `d1s0` WIBW-DT2 [0]: WIBW-DT2 is a primary MyNetworkTV- and secondary MeTV-affiliated television station located in Topeka, Kansas, United States.
- `d1s1` WIBW-DT2 [1]: It operates as a second digital subchannel of CBS affiliate WIBW-TV (channel 13), which is owned by Gray Television.
- `d1s2` WIBW-DT2 [2]: Over-the-air, it broadcasts a standard definition digital signal on VHF channel 13.2 from a transmitter located on Windy Hill Road in Maple Hill.
- `d1s3` WIBW-DT2 [3]: WIBW-TV maintains studio facilities located on Commerce Place (next to the interchange of I-70, I-470, US 40, US 75 and K-4) in southwestern Topeka.
- `d2s0` Broadcast transmitter [0]: A broadcast transmitter refers to an installation used for broadcasting, including radio transmitter or television transmitter equipment, the antenna, and often the location of the broadcasting station.
- `d3s0` North Hessary Tor transmitting station [0]: Situated on the summit of North Hessary Tor in Devon, England is an FM radio and television transmitter which uses as aerial a 196 m high guyed mast.
- `d3s1` North Hessary Tor transmitting station [1]: It was built by the BBC in 1955 when a transmitter was needed to introduce 405 line television into Devon.
- `d3s2` North Hessary Tor transmitting station [2]: It now carries a small UHF TV transmitter which serves Princetown and Dartmoor.
- `d3s3` North Hessary Tor transmitting station [3]: FM radio transmissions began in 1956 and cover most of Devon and eastern parts of Cornwall.
- `d3s4` North Hessary Tor transmitting station [4]: It is owned and operated by Arqiva.
- `d4s0` Transmitter/studio link [0]: The transmitter/studio link (or TSL) of a radio station or television station is a return link which sends telemetry data from the remotely located radio transmitter or television transmitter back to the studio for monitoring purposes.
- `d4s1` Transmitter/studio link [1]: The TSL may return the same way as the studio/transmitter link (STL), or it can be embedded in the station's regular broadcast signal as a subcarrier (for analog stations) or a separate data channel (for digital stations).
- `d5s0` WIBW-TV [0]: WIBW-TV, virtual and VHF digital channel 13, is a CBS-affiliated television station licensed to Topeka, Kansas, United States.
- `d5s1` WIBW-TV [1]: The station is owned by Gray Television.
- `d5s2` WIBW-TV [2]: WIBW-TV maintains studio facilities located on Commerce Place (next to the interchange of I-70, I-470, US 40, US 75 and K-4) in southwestern Topeka, and its transmitter is located on Windy Hill Road in Maple Hill.
- `d5s3` WIBW-TV [3]: To serve portions of the market that cannot adequately receive the main signal, WIBW-TV operates a digital fill-in translator in Topeka, WIBW-LD, which broadcasts on UHF channel 44.
- `d6s0` KTVF [0]: KTVF is an NBC-affiliated television station located in Fairbanks, Alaska, United States.
- `d6s1` KTVF [1]: KTVF is owned by Gray Television, as the sister stations of Fox affiliate KFXF-LD and CBS affiliate KXDF-CD.
- `d6s2` KTVF [2]: The station broadcasts a high definition digital signal on UHF channel 26 (or virtual channel 11 via PSIP) from a transmitter located on the Ester Dome.
- `d6s3` KTVF [3]: KTVF maintains separate studios located on International Drive in downtown Fairbanks.
- `d6s4` KTVF [4]: KTVF operates a digital fill-in translator on VHF channel 11 from a transmitter located at KFXF and KXDF-CD's studios on Braddock Street in downtown Fairbanks.
- `d6s5` KTVF [5]: This station is also used to provide full-market over-the-air high definition coverage of the low-powered Fox-affiliated KFXF-LD (simulcast over KTVF-DT2), as well as the low-powered CBS-affiliated KXDF-CD (simulcast over KTVF-DT3).
- `d7s0` KIH54 [0]: KIH54 (sometimes referred to as Birmingham All Hazards) is a NOAA Weather Radio station that serves the Birmingham-Hoover-Cullman Combined Statistical Area and surrounding cities.
- `d7s1` KIH54 [1]: It is programmed from the National Weather Service forecast office in Calera, Alabama with its transmitter located in the same city, side-mounted on the transmitter tower of Birmingham local television station WTTO.
- `d7s2` KIH54 [2]: It broadcasts weather and hazard information for the following counties: Bibb, Blount, Chilton, Coosa, Jefferson, Shelby, St. Clair, Tuscaloosa, and Walker.
- `d7s3` KIH54 [3]: On April 23, 2014, it was reported that the transmitter had stopped operating, a cause for concern because central Alabama is predicted to be impacted by severe thunderstorms between approximately April 27 and April 30, and no NOAA Weather Radios in the broadcast area of KIH54 will sound for watches and warnings issued by the National Weather Service until the transmitter is repaired.
- `d7s4` KIH54 [4]: On April 24, it was announced that a temporary, but much weaker, transmitter had been activated on the site of the main, inoperative transmitter.
- `d7s5` KIH54 [5]: It is currently operating on the broadcast signal of KIH54, using the same call sign.
- `d7s6` KIH54 [6]: The main transmitter has since been repaired and is fully operational.
- `d8s0` KHMY [0]: KHMY, known as "My 93-1" is an FM radio station based in Hutchinson, KS, broadcasting a Hot AC/Adult Top 40 format.
- `d8s1` KHMY [1]: Licensed to Pratt, Kansas, United States, the station serves the Hutchinson/Wichita area.
- `d8s2` KHMY [2]: The station is currently owned by Eagle Communications, Inc.
- `d8s3` KHMY [3]: The station has a transmitter located south of Plevna, Kansas.
- `d9s0` KTMJ-CD [0]: KTMJ-CD, virtual and UHF digital channel 43, is a low-powered Fox-affiliated television station licensed to Topeka, Kansas, United States.
- `d9s1` KTMJ-CD [1]: The Class A-licensed station is owned by Nexstar Media Group, and is a sister station to NBC affiliate KSNT (channel 27); Nexstar also operates ABC affiliate KTKA-TV (channel 49) under shared services and joint sales agreements with owner Vaughan Media, LLC.
- `d9s2` KTMJ-CD [2]: All three stations share studio facilities located on Northwest 25th Street (US 24), near the Kiro section of Topeka; KTMJ-CD maintains transmitter facilities located between the Kansas River and I-70/US 40/US 75/KS 4 in Topeka.
- `d10s0` Spur Hill [0]: This broadcast transmission site is located to the south of the city of Cork, Ireland, just North West of Cork airport, it has a cable-stayed mast 60m tall on an elevation of 137m ASL.
- `d10s1` Spur Hill [1]: The transmitter was initially opened in 1965 as a VHF relay of the main Mullaghanish television transmitter in County Cork.
- `d10s2` Spur Hill [2]: Later, FM radio transmitters were also added providing a relay of the national radio channels, and more recently, digital radio broadcasting (DAB) was started from the site.
- `d10s3` Spur Hill [3]: On its conversion to UHF television transmission in 1996, it became the main transmitter serving Cork city, carrying the four Irish analogue channels, RTÉ One (Ch53), RTÉ Two (Ch57), TV3 (Ch60), and TG4 (Ch63) at an effective radiated power of 20 kW.
- `d10s4` Spur Hill [4]: On 24 October 2012 all analogue television transmission ended in Ireland, and the station now provides the Irish DTT service Saorview to Cork city and environs.
- `d10s5` Spur Hill [5]: It is owned and operated by 2RN, a subsidiary of the Irish national broadcaster RTÉ.

</details>

## Q216 — `hotpotqa_5a90503755429916514e7470` (revised draft)

> What title did the Queen of the United Kingdom of Great Britain and Ireland give to Jeremiah Meyer?

Source answer: Painter in Miniatures

Gold final answer: Painter in Miniatures

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: queen described as Queen of the United Kingdom of Great Britain and Ireland | false | Queen Charlotte | — | [d1s0] | — |
| u2: title Jeremiah Meyer held for {u1} | true | Painter in Miniatures | u1 | [d8s1] | — |

Evidence:

- `d1s0` Charlotte of Mecklenburg-Strelitz [0]: Charlotte of Mecklenburg-Strelitz (Sophia Charlotte; 19 May 1744 – 17 November 1818) was by marriage to King George III the Queen of Great Britain and Ireland from her wedding in 1761 until the union of the two kingdoms in 1801, after which she was Queen of the United Kingdom of Great Britain and Ireland until her death in 1818.
- `d8s1` Jeremiah Meyer [1]: He was Painter in Miniatures to Queen Charlotte, Painter in Enamels to King George III and was one of the founder members of the Royal Academy.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Charlotte of Mecklenburg-Strelitz [0]: Charlotte of Mecklenburg-Strelitz (Sophia Charlotte; 19 May 1744 – 17 November 1818) was by marriage to King George III the Queen of Great Britain and Ireland from her wedding in 1761 until the union of the two kingdoms in 1801, after which she was Queen of the United Kingdom of Great Britain and Ireland until her death in 1818.
- `d1s1` Charlotte of Mecklenburg-Strelitz [1]: She was also the Electress of Hanover in the Holy Roman Empire until the promotion of her husband to King of Hanover on 12 October 1814, after which she was also queen consort of Hanover.
- `d2s0` Irish migration to Great Britain [0]: Irish migration to Great Britain has occurred from the earliest recorded history to the present.
- `d2s1` Irish migration to Great Britain [1]: There has been a continuous movement of people between the islands of Ireland and Great Britain due to their proximity.
- `d2s2` Irish migration to Great Britain [2]: This tide has ebbed and flowed in response to politics, economics and social conditions of both places.
- `d2s3` Irish migration to Great Britain [3]: Ireland was a feudal Lordship of the Kings of England between 1171 and 1541; a Kingdom in personal union with the Kingdom of England and Kingdom of Great Britain between 1542 and 1801; and politically united with Great Britain as the United Kingdom of Great Britain and Ireland between 1801 and 1922.
- `d2s4` Irish migration to Great Britain [4]: Today, Ireland is divided between the independent Republic of Ireland and Northern Ireland.
- `d3s0` United Kingdom of Great Britain and Ireland [0]: The United Kingdom of Great Britain and Ireland was established as a sovereign state on 1 January 1801 by the Acts of Union 1800, which merged the kingdoms of Great Britain and Ireland.
- `d3s1` United Kingdom of Great Britain and Ireland [1]: The growing desire for an Irish Republic led to the Irish War of Independence, which resulted in Ireland seceding from the Union and forming the Irish Free State in 1922.
- `d3s2` United Kingdom of Great Britain and Ireland [2]: Northern Ireland remained part of the United Kingdom, and the state was consequently renamed the "United Kingdom of Great Britain and Northern Ireland".
- `d4s0` Great Britain at the 2008 Summer Olympics [0]: The United Kingdom of Great Britain and Northern Ireland competed as Great Britain at the 2008 Summer Olympics in Beijing, China.
- `d4s1` Great Britain at the 2008 Summer Olympics [1]: The United Kingdom was represented by the British Olympic Association (BOA), and the team of selected athletes was officially known as Team GB.
- `d4s2` Great Britain at the 2008 Summer Olympics [2]: Britain is one of only five NOCs to have competed in every modern Summer Olympic Games since 1896.
- `d4s3` Great Britain at the 2008 Summer Olympics [3]: The delegation of 547 people included 311 competitors – 168 men, 143 women – and 236 officials.
- `d4s4` Great Britain at the 2008 Summer Olympics [4]: The team was made up of athletes from the whole United Kingdom including Northern Ireland (whose people may elect to hold Irish citizenship and are able to be selected to represent either Great Britain or Ireland at the Olympics).
- `d4s5` Great Britain at the 2008 Summer Olympics [5]: Additionally some British overseas territories compete separately from Britain in Olympic competition.
- `d5s0` List of British monarchs [0]: There have been 12 monarchs of the Kingdom of Great Britain and the United Kingdom (see Monarchy of the United Kingdom) since the merger of the Kingdom of England and the Kingdom of Scotland on 1 May 1707.
- `d5s1` List of British monarchs [1]: England and Scotland had been in personal union under the House of Stuart since 24 March 1603.
- `d5s2` List of British monarchs [2]: On 1 January 1801, Great Britain merged with the Kingdom of Ireland (also previously in personal union with Great Britain) to form the United Kingdom of Great Britain and Ireland.
- `d5s3` List of British monarchs [3]: After most of Ireland left the union on 6 December 1922, its name was amended on 12 April 1927 to the United Kingdom of Great Britain and Northern Ireland.
- `d6s0` Governance of England [0]: There has not been a government of England since 1707 when the Kingdom of England ceased to exist as a sovereign state, as it merged with the Kingdom of Scotland to form the Kingdom of Great Britain.
- `d6s1` Governance of England [1]: Kingdom of Great Britain continued from 1707 until 1801 when it merged with the Kingdom of Ireland to form the United Kingdom of Great Britain and Ireland, which itself became the United Kingdom of Great Britain and Northern Ireland (UK) in 1922 (in reality; in name in 1927) upon independence for most of the island of Ireland.
- `d6s2` Governance of England [2]: The UK since then has gone through significant change to its system of government, with devolved parliaments, assemblies and governments in Scotland, Wales and Northern Ireland.
- `d6s3` Governance of England [3]: England, however, remains under the full jurisdiction, on all matters, of the Parliament of the United Kingdom of Great Britain and Northern Ireland and the UK government as no devolved administration has been created for England within the new structure.
- `d6s4` Governance of England [4]: This situation has led to the anomaly, known as the West Lothian question, which is that Scottish Members of Parliament (MPs) are able to vote on legislation that affects only England whereas English MPs can not vote on certain Scottish matters due to devolution.
- `d6s5` Governance of England [5]: In some cases, such as top-up university tuition fees and foundation hospitals, the votes of Scottish MPs have been crucial in helping pass legislation for England that the majority of English MPs have opposed.
- `d7s0` Great Britain at the 2016 Summer Olympics [0]: The United Kingdom of Great Britain and Northern Ireland competed as Great Britain at the 2016 Summer Olympics in Rio de Janeiro, Brazil, from 5 to 21 August 2016.
- `d7s1` Great Britain at the 2016 Summer Olympics [1]: The United Kingdom was represented by the British Olympic Association (BOA), and the team of selected athletes was also known as Team GB.
- `d7s2` Great Britain at the 2016 Summer Olympics [2]: British athletes have appeared in every Summer Olympic Games of the modern era, alongside Australia, France, Greece, and Switzerland, though Great Britain is the only country to have won at least one gold medal at all of them.
- `d7s3` Great Britain at the 2016 Summer Olympics [3]: Although the British Olympic Association is the National Olympic Committee (NOC) for Great Britain and Northern Ireland, Northern Irish athletes can choose whether to compete for Great Britain or for the Republic of Ireland, as they are entitled to citizenship of either nation under the Good Friday Agreement.
- `d7s4` Great Britain at the 2016 Summer Olympics [4]: In 2016 Northern Ireland born representatives in Team GB included returning rowers Alan Campbell, Peter Chambers and Richard Chambers, archer Patrick Huston and four members of the men's field hockey team: David Ames, Mark Gleghorne, Iain Lewers and Ian Sloan.
- `d7s5` Great Britain at the 2016 Summer Olympics [5]: The team also represents, and included representation from, the Crown dependencies, among which were Guernsey's Heather Watson and Carl Hester, and from the ten of the thirteen British Overseas Territories represented by the BOA rather than their own NOC, whose representatives include Turks and Caicos-born sprinter Delano Williams and Anguillan-born long jumper Shara Proctor
- `d8s0` Jeremiah Meyer [0]: Jeremiah Meyer {'1': ", '2': ", '3': ", '4': "} (born "Jeremias Majer"; 18 January 1735 – 20 January 1789) was an 18th-century English miniature painter.
- `d8s1` Jeremiah Meyer [1]: He was Painter in Miniatures to Queen Charlotte, Painter in Enamels to King George III and was one of the founder members of the Royal Academy.
- `d9s0` United Kingdom [0]: The United Kingdom of Great Britain and Northern Ireland, commonly known as the United Kingdom (UK) and colloquially Great Britain (GB) or simply Britain, is a sovereign country in western Europe.
- `d9s1` United Kingdom [1]: Lying off the north-western coast of the European mainland, the United Kingdom includes the island of Great Britain, the north-eastern part of the island of Ireland and many smaller islands.
- `d9s2` United Kingdom [2]: Northern Ireland is the only part of the United Kingdom that shares a land border with another sovereign statethe Republic of Ireland.
- `d9s3` United Kingdom [3]: Apart from this land border, the United Kingdom is surrounded by the Atlantic Ocean, with the North Sea to its east, the English Channel to its south and the Celtic Sea to its south-south-west, giving it the 12th-longest coastline in the world.
- `d9s4` United Kingdom [4]: The Irish Sea lies between Great Britain and Ireland.
- `d9s5` United Kingdom [5]: With an area of 242500 km2 , the United Kingdom is the 78th-largest sovereign state in the world and the 11th-largest in Europe.
- `d9s6` United Kingdom [6]: It is also the 21st-most populous country, with an estimated 65.1 million inhabitants.
- `d9s7` United Kingdom [7]: Together, this makes it the fourth-most densely populated country in the European Union (EU).
- `d10s0` Monarchy of Ireland [0]: A monarchical system of government existed in Ireland from ancient times until, for what became the Republic of Ireland, the mid-twentieth century.
- `d10s1` Monarchy of Ireland [1]: Northern Ireland, as part of the United Kingdom, remains under a monarchical system of government.
- `d10s2` Monarchy of Ireland [2]: The Gaelic kingdoms of Ireland ended with the Norman invasion of Ireland, when the kingdom became a fief of the Holy See under the Lordship of the King of England.
- `d10s3` Monarchy of Ireland [3]: This lasted until the Parliament of Ireland conferred the crown of Ireland upon King Henry VIII of England during the English Reformation.
- `d10s4` Monarchy of Ireland [4]: The monarch of England held the crowns of England and Ireland in a personal union.
- `d10s5` Monarchy of Ireland [5]: The Union of the Crowns in 1603 expanded the personal union to include Scotland.
- `d10s6` Monarchy of Ireland [6]: The personal union between England and Scotland became a political union with the enactments of the Acts of Union 1707, which created the Kingdom of Great Britain.
- `d10s7` Monarchy of Ireland [7]: The crowns of Great Britain and Ireland remained in personal union until it was ended by the Acts of Union 1800, which united Ireland and Great Britain into the United Kingdom of Great Britain and Ireland from January 1801 until December 1922.

</details>

## Q217 — `hotpotqa_5a90970d5542995651fb51a5` (revised draft)

> Rainforest Ecological Train runs through a national park with an area of how many Kilometers ?

Source answer: 672 km2

Gold final answer: 672 km2

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: national park traversed by the Rainforest Ecological Train | false | Iguazú National Park | — | [d2s0] | — |
| u2: area of {u1} | true | 672 km2 | u1 | [d1s1] | — |

Evidence:

- `d1s1` Iguazú National Park [1]: It has an area of 672 km2 .
- `d2s0` Rainforest Ecological Train [0]: The Rainforest Ecological Train or Waterfalls Train ("Tren Ecológico de la Selva" or "Tren de las Cataratas") is an environmentally friendly, narrow gauge train that runs through the forest inside Iguazú National Park in the north of the province of Misiones of Argentina.

Notes:

- The answer is an area in square kilometers, not a length.
- 复核后保留原标注；原note为说明或未发现需要修改的证据/依赖问题。

<details><summary>All source context</summary>

- `d1s0` Iguazú National Park [0]: The Iguazú National Park (Spanish: "Parque Nacional Iguazú" ) is a national park of Argentina, located in the Iguazú Department, in the north of the province of Misiones, Argentine Mesopotamia.
- `d1s1` Iguazú National Park [1]: It has an area of 672 km2 .
- `d2s0` Rainforest Ecological Train [0]: The Rainforest Ecological Train or Waterfalls Train ("Tren Ecológico de la Selva" or "Tren de las Cataratas") is an environmentally friendly, narrow gauge train that runs through the forest inside Iguazú National Park in the north of the province of Misiones of Argentina.
- `d3s0` Sajama National Park [0]: Sajama National Park is a national park located in the Oruro Department, Bolivia.
- `d3s1` Sajama National Park [1]: It borders Lauca National Park in Chile.
- `d3s2` Sajama National Park [2]: The park is home to indigenous people, known as the Aymara, whose influential ancient culture can be seen in various aspects throughout the park.
- `d3s3` Sajama National Park [3]: The park contains unique cultural artifacts and ecological wonders, making it an exemplary location for ecotourism.
- `d3s4` Sajama National Park [4]: Many different indigenous plants and animals are exclusive to this area; therefore, its continued conservation is of great ecological importance.
- `d3s5` Sajama National Park [5]: Management of the park operates under a co-administrative approach, with local people and park conservationists engaging in a constant dialogue regarding park upkeep and policy.
- `d4s0` Biak-na-Bato National Park [0]: Biak-na-Bato National Park is a protected area of the Philippines located almost entirely within Barangay Biak-na-Bato in San Miguel, Bulacan from where it derives its name.
- `d4s1` Biak-na-Bato National Park [1]: The park also extends to the nearby municipalities of San Ildefonso and Doña Remedios Trinidad covering a total area of 2,117 hectares.
- `d4s2` Biak-na-Bato National Park [2]: It was declared a national park in 1937 by President Manuel Luis Quezon by virtue of its association with the history and site of the Biak-na-Bato Republic.
- `d4s3` Biak-na-Bato National Park [3]: The park consists of a cave network and a system of rivers and trails of both historical and ecological importance.
- `d4s4` Biak-na-Bato National Park [4]: Situated only 80 kilometers northeast from Manila, it is fast becoming a popular weekend eco-adventure destination for the city dwellers.
- `d5s0` Concinnia spinosa [0]: Concinnia spinosa, the Nangur spiny skink or Nangur skink, is a lizard known from two patches of dry-rainforest in South East Queensland, Australia.
- `d5s1` Concinnia spinosa [1]: It was formerly placed in the monotypic genus "Nangura" but was moved to "Concinnia" following the molecular phylogenetic studies of O'Connor & Moritz (2003) and Skinner and co-authors (2013).
- `d5s2` Concinnia spinosa [2]: This species is known only from two localities; the type locality, now in Nangura National Park, and a much smaller isolated population in Oakview National Park and adjacent Oakview State Forest.
- `d5s3` Concinnia spinosa [3]: The total distribution spans just 42 square kilometers, within which this species occupies less than 4 square kilometers, with an estimated population size of less than 200 individuals.
- `d5s4` Concinnia spinosa [4]: It is threatened by invasive species including cats, pigs, dogs, foxes and Cane Toads, by the invasive plant species Lantana camara, which increases fire risk and changes forest structure, and in some sites by logging and road maintenance.
- `d5s5` Concinnia spinosa [5]: Consequently, it is listed as Critically Endangered under the Australian Environment Protection and Biodiversity Conservation Act 1999 It resembles "Concinnia queenslandiae" in its spiny scales and like that species it is live bearing.
- `d5s6` Concinnia spinosa [6]: Along with minor differences in scalation, the Nangur Spiny Skink differs from other Australian Sphenomorphid skinks in its karyotype of 2n=28 chromosomes, where most others have 2n=30.
- `d5s7` Concinnia spinosa [7]: It is also unlike related species in that it lives in burrows, which occur in small colonies through the dry rainforest habitat.
- `d5s8` Concinnia spinosa [8]: There is some indication of parental care in this species, with adults sharing burrows with juveniles.
- `d6s0` IND Fulton Street Line [0]: The IND Fulton Street Line is a rapid transit line of the IND Division of the New York City Subway, running from the Cranberry Street Tunnel under the East River through all of central Brooklyn to a terminus in Ozone Park, Queens.
- `d6s1` IND Fulton Street Line [1]: The IND Rockaway Line branches from it just east of Rockaway Boulevard.
- `d6s2` IND Fulton Street Line [2]: The A train runs express during daytime hours and local at night on the underground portion of the line; it runs local on the elevated portion of the line at all times.
- `d6s3` IND Fulton Street Line [3]: The C train runs local on the underground portion of the line at all times except late nights.
- `d7s0` Playa cativo [0]: Playa Cativo is located in the Golfo Dulce, in Costa Ricas' south Pacific.
- `d7s1` Playa cativo [1]: Its name, Cativo, comes from a tree: Prioria Copaifera.
- `d7s2` Playa cativo [2]: The surrounding waters are part of the Piedras Blancas National Park to protect the needle-fish spawning grounds.
- `d7s3` Playa cativo [3]: A former extension of Corcovado National Park, Piedras Blancas National Park has over 35,000 acres of rainforest that surrounds Playa Cativo and was created in 1993 to protect the lowland tropical rainforest in the Golfo Dulce.
- `d7s4` Playa cativo [4]: Accessible only by boat, Playa Cativo was awarded the Ecologic Blue Flag for its cleanliness and sustainability practices.
- `d7s5` Playa cativo [5]: Because of the variety of micro climates, including wetlands, and the fact that is a gathered point for birds from North and South America, this area is considered a bird watcher's paradise.
- `d7s6` Playa cativo [6]: The four species of monkeys of Costa Rica has been seen there and about three families of hauler monkeys stay year round near the shore.
- `d7s7` Playa cativo [7]: The beach was originally a family farm and in the early 70's was sold.
- `d7s8` Playa cativo [8]: In 1980 was built the Rainbow Lodge in Playa Cativo, followed by the Buenavista Lodge.
- `d7s9` Playa cativo [9]: In July 2014 Playa Cativo Lodge (former Rainbow Lodge) opened after a full renovation.
- `d7s10` Playa cativo [10]: Playa Cativo's residents are committed to preserve the area as untouched as possible, and have established many sustainable practices and was recently awarded the Ecologic Blue Flag by the Costa Rica government.
- `d7s11` Playa cativo [11]: Among other actions, was created a recycle hub center as a free service for the people from the nearby beaches and communities.
- `d7s12` Playa cativo [12]: The electric power at Cativo is 100% clean and comes from an hydroelectric micro-generator and solar panels.
- `d7s13` Playa cativo [13]: The water source comes from a spring in the mountains behind Cativo beach and is clean and clear.
- `d7s14` Playa cativo [14]: Some of the all fruit trees still in the property, providing fresh organic fruits to visitors.
- `d7s15` Playa cativo [15]: Its tranquil waters are perfect for sea kayaking, stand up paddle boarding, swimming and snorkeling.
- `d7s16` Playa cativo [16]: As there are no roads to Playa Cativo, a 30 minutes scenic boat ride will take residents to Golfito or Puerto Jimenez, and often are seen dolphins and the seasonal humpback whales.
- `d7s17` Playa cativo [17]: Golfo Dulce, also known as Gulf of Dulce, is in the inner side of Osa Peninsula and across from Corcovado National Park.
- `d8s0` Tropical Rainforest Heritage of Sumatra [0]: The Tropical Rainforest Heritage of Sumatra site was inscribed as a UNESCO World Heritage site in 2004.
- `d8s1` Tropical Rainforest Heritage of Sumatra [1]: It comprises three Indonesian national parks on the island of Sumatra: Gunung Leuser National Park, Kerinci Seblat National Park and the Bukit Barisan Selatan National Park.
- `d8s2` Tropical Rainforest Heritage of Sumatra [2]: The site is listed under Criteria vii - outstanding scenic beauty; ix- an outstanding example representing significant on-going ecological and biological processes; and x- contains the most important and significant natural habitats for in-situ conservation.
- `d9s0` Kavir National Park [0]: Kavir National Park is a protected ecological zone in northern Iran.
- `d9s1` Kavir National Park [1]: It has an area of 4,000 square kilometers (1,500 mile²).
- `d9s2` Kavir National Park [2]: The park is located 120 kilometers south of Tehran and 100 kilometers east of Qom, and it sits on the western end of one of Iran's two major deserts, the Dasht-e Kavir (Great Salt Desert).
- `d9s3` Kavir National Park [3]: Siahkuh (Black Mountain), a large, semi-circular rock outcropping sits in roughly the park's center.
- `d10s0` Guanacaste National Park (Costa Rica) [0]: Guanacaste National Park, in Spanish Parque Nacional Guanacaste , is part of the Area de Conservación Guanacaste World Heritage Site, is a National Park in the northern part of Costa Rica, from the slopes of the Orosí and Cacao volcanoes west to the Interamerican Highway where it is adjacent to the Santa Rosa National Park.
- `d10s1` Guanacaste National Park (Costa Rica) [1]: It was created in 1989, partially due to the campaigning and fund-raising of Dr. Daniel Janzen to allow a corridor between the dry forest and rain forest areas which many species migrate between seasonally.
- `d10s2` Guanacaste National Park (Costa Rica) [2]: The park covers an area of approximately 340 square kilometers, and includes 140 species of mammals, over 300 birds, 100 amphibians and reptiles, and over 10,000 species of insects that have been identified.
- `d10s3` Guanacaste National Park (Costa Rica) [3]: It was this high density of bio-diversity that encouraged the Costa Rican government to protect this area.
- `d10s4` Guanacaste National Park (Costa Rica) [4]: The Guanacaste National Park weaves the neighboring Santa Rosa National Park with the high altitude forests of the two volcanoes, Orosi and Cacao, and the rainforest of the Caribbean in the country's north.

</details>

## Q218 — `hotpotqa_5a90b7f355429916514e752d` (revised draft)

> In which city has the Salon d'Automne been held since its first exhibition in 1903?

Source answer: Paris

Gold final answer: Paris

Question type: `single` (source type `bridge`)

Original question: In which city did he painter and printmaker associated with "Les Nabis" found Salon d'Automne?

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: city where the Salon d'Automne was first held | true | Paris | — | [d8s0] | — |

Evidence:

- `d8s0` Salon d'Automne [0]: The Salon d'Automne (Autumn Salon), or Société du Salon d'automne, is an annual art exhibition held in Paris, France since 1903; it is currently held on the Champs-Élysées, between the Grand Palais and the Petit Palais, in mid October .

Notes:

- 题干澄清：删除不唯一的画家筛选，将founding location明确为1903年开始的展览举办城市。
- single直接使用d8s0；不再事后挑选Vallotton，也不将创办者住所当作展览地点。

<details><summary>All source context</summary>

- `d1s0` Félix Vallotton [0]: Félix Edouard Vallotton (December 28, 1865December 29, 1925) was a Swiss/French painter and printmaker associated with "Les Nabis".
- `d1s1` Félix Vallotton [1]: He was an important figure in the development of the modern woodcut.
- `d2s0` Ker-Xavier Roussel [0]: Ker-Xavier Roussel (10 December 1867 – 6 June 1944) was a French painter associated with Les Nabis.
- `d3s0` Groupe de femmes [0]: Groupe de femmes, also called Groupe de trois femmes, or Groupe de trois personnages, is an early Cubist sculpture created circa 1911 by the Hungarian avant-garde, sculptor, and graphic artist Joseph Csaky (1888–1971).
- `d3s1` Groupe de femmes [1]: This sculpture formerly known from a black and white photograph (Galerie René Reichard) had been erroneously entitled "Deux Femmes (Two Women)", as the image captured on an angle showed only two figures.
- `d3s2` Groupe de femmes [2]: An additional photograph found in the Csaky family archives shows a frontal view of the work, revealing three figures rather than two.
- `d3s3` Groupe de femmes [3]: Csaky's sculpture was exhibited at the 1912 Salon d'Automne, and the 1913 Salon des Indépendants, Paris.
- `d3s4` Groupe de femmes [4]: A photograph taken of Salle XI "in sitiu" at the 1912 Salon d'Automne and published in "L'Illustration", 12 October 1912, p. 47, shows "Groupe de femmes" exhibited alongside the works of Jean Metzinger, František Kupka, Francis Picabia, Amedeo Modigliani and Henri Le Fauconnier.
- `d4s0` Louis Valtat [0]: Louis Valtat (] ; 8 August 1869 – 2 January 1952) was a French painter and printmaker associated with the Fauves ("the wild beasts", so named for their wild use of color), who first exhibited together in 1905 at the Salon d'Automne.
- `d5s0` Édouard Vuillard [0]: Jean-Édouard Vuillard (] ; 11 November 186821 June 1940) was a French painter and printmaker associated with the Nabis.
- `d6s0` 20th-century art [0]: 20th-century art—and what it became as modern art—began with modernism in the late 19th century.
- `d6s1` 20th-century art [1]: Nineteenth-century movements of Post-Impressionism (Les Nabis), Art Nouveau and Symbolism led to the first twentieth-century art movements of Fauvism in France and Die Brücke ("The Bridge") in Germany.
- `d6s2` 20th-century art [2]: Fauvism in Paris introduced heightened non-representational colour into figurative painting.
- `d6s3` 20th-century art [3]: Die Brücke strove for emotional Expressionism.
- `d6s4` 20th-century art [4]: Another German group was Der Blaue Reiter ("The Blue Rider"), led by Kandinsky in Munich, who associated the "blue rider" image with a spiritual non-figurative mystical art of the future.
- `d6s5` 20th-century art [5]: Kandinsky, Kupka, R. Delaunay and Picabia were pioneers of abstract (or non-representational) art.
- `d6s6` 20th-century art [6]: Cubism, generated by Picasso, Braque, Metzinger, Gleizes and others rejected the plastic norms of the Renaissance by introducing multiple perspectives into a two-dimensional image.
- `d6s7` 20th-century art [7]: Futurism incorporated the depiction of movement and machine age imagery.
- `d6s8` 20th-century art [8]: Dadaism, with its most notable exponents, Marcel Duchamp, who rejected conventional art styles altogether by exhibiting found objects, notably a urinal, and too Francis Picabia, with his "Portraits Mécaniques".
- `d7s0` Maurice Denis [0]: Maurice Denis (] ; 25 November 1870 – 13 November 1943) was a French painter and writer, and a member of the Symbolist and Les Nabis movements.
- `d7s1` Maurice Denis [1]: His theories contributed to the foundations of cubism, fauvism, and abstract art.
- `d8s0` Salon d'Automne [0]: The Salon d'Automne (Autumn Salon), or Société du Salon d'automne, is an annual art exhibition held in Paris, France since 1903; it is currently held on the Champs-Élysées, between the Grand Palais and the Petit Palais, in mid October .
- `d8s1` Salon d'Automne [1]: The first Salon d'Automne was created under the initiative of the Belgian architect, literary man and art collector Frantz Jourdain, along with the architect Hector Guimard, the painters Georges Desvallières, Eugène Carrière, Félix Vallotton, Édouard Vuillard and the Maison Jansen, a Paris-based interior decoration office (the first truly global design firm) founded in 1880 by Dutch-born Jean-Henri Jansen.
- `d9s0` Pierre Bonnard [0]: Pierre Bonnard (] ; 3 October 1867 — 23 January 1947) was a French painter and printmaker, as well as a founding member of the Post-Impressionist group of avant-garde painters Les Nabis.
- `d9s1` Pierre Bonnard [1]: Bonnard preferred to work from memory, using drawings as a reference, and his paintings are often characterized by a dreamlike quality.
- `d9s2` Pierre Bonnard [2]: The intimate domestic scenes, for which he is perhaps best known, often include his wife Marthe de Meligny.
- `d10s0` Dancer in a Café [0]: Danseuse au café (also known as Dancer in a Café or Au Café Concert and Danseuse) is a large oil painting created in 1912 by the French artist and theorist Jean Metzinger (1883–1956).
- `d10s1` Dancer in a Café [1]: The work was exhibited in Paris at the Salon d'Automne of 1912, entitled "Danseuse".
- `d10s2` Dancer in a Café [2]: The Cubist contribution to the 1912 Salon d'Automne created a controversy in the Municipal Council of Paris, leading to a debate in the Chambre des Députés about the use of public funds to provide the venue for such 'barbaric' art.
- `d10s3` Dancer in a Café [3]: The Cubists were defended by the Socialist deputy, Marcel Sembat.
- `d10s4` Dancer in a Café [4]: This painting was realized as Albert Gleizes and Jean Metzinger, in preparation for the Salon de la Section d'Or, published a major defence of Cubism, resulting in the first theoretical essay on the new movement, "Du «Cubisme»".
- `d10s5` Dancer in a Café [5]: "Danseuse au café" was first reproduced in a photograph published in an article entitled "Au Salon d'Automne "Les Indépendants"" in the French newspaper "", 2 Octobre 1912.
- `d10s6` Dancer in a Café [6]: The painting is now located at the Albright-Knox Art Gallery, Buffalo New York.

</details>

## Q219 — `hotpotqa_5ab1c693554299722f9b4c66` (revised draft)

> Which team based in South Wales participated in a final game of 1980 Welsh Cup Final?

Source answer: Newport County

Gold final answer: Newport County

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: teams contesting the 1980 Welsh Cup Final | false | Newport County and Shrewsbury Town | — | [d3s1] | — |
| u2: team among {u1} based in South Wales | true | Newport County | u1 | [d5s0] | — |

Evidence:

- `d3s1` 1980 Welsh Cup Final [1]: The final was contested between Newport County and Shrewsbury Town over two legs.
- `d5s0` Newport County A.F.C. [0]: Newport County Association Football Club (Welsh: "Clwb Pêl-droed Sir Casnewydd" ) is a professional association football club based in the city of Newport, South Wales.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` 2000 Welsh Cup Final [0]: The 2000 Welsh Cup Final saw Bangor City win the Welsh Cup after beating Cwmbran Town 1–0 at Racecourse Ground in the 113th Welsh Cup Final.
- `d2s0` Welsh League Cup [0]: The Welsh League Cup (also known as the League of Wales Cup, Welsh Premier League Cup or The Word Cup) is a cup competition in Welsh football organised by the Welsh Premier League.
- `d2s1` Welsh League Cup [1]: The competition was established in 1992 and is considered to be the second-most important domestic cup competition for Welsh football clubs, after the older and more prestigious Welsh Cup.
- `d2s2` Welsh League Cup [2]: Unlike the Welsh Cup, where 135 teams entered in 2008–09, the competition is only open to the members of the Welsh Premier League and a very select few other clubs.
- `d2s3` Welsh League Cup [3]: It should not be confused with the Welsh Football League Cup, which is for the clubs in the Welsh Football League, which despite its name only covers the south and centre of Wales.
- `d3s0` 1980 Welsh Cup Final [0]: The 1980 Welsh Cup Final was the final of the 93rd season of the main domestic football cup competition in Wales, the Welsh Cup.
- `d3s1` 1980 Welsh Cup Final [1]: The final was contested between Newport County and Shrewsbury Town over two legs.
- `d3s2` 1980 Welsh Cup Final [2]: Newport County won 5–1 on aggregate, winning both legs.
- `d4s0` 1991 Welsh Cup Final [0]: The 1991 Welsh Cup Final saw Swansea City win the Welsh Cup for the tenth time, by beating Wrexham 2–0 at National Stadium in the 104th Welsh Cup Final.
- `d5s0` Newport County A.F.C. [0]: Newport County Association Football Club (Welsh: "Clwb Pêl-droed Sir Casnewydd" ) is a professional association football club based in the city of Newport, South Wales.
- `d5s1` Newport County A.F.C. [1]: The team play in League Two, the fourth tier of the English football league system.
- `d5s2` Newport County A.F.C. [2]: Most recently reformed in 1989, the club is a continuation of the Newport County club which was founded in 1912 and was a founder member of the Football League's new Third Division in 1920.
- `d6s0` Richard Johnson (rugby) [0]: Richard Johnston, born (26-02-1980) in Neath, Wales, first started his career at Neath RFC in 1998 where he gained representative honours for Wales under 18/19's.
- `d6s1` Richard Johnson (rugby) [1]: In 2000 Richard signed for Pontypridd RFC where he spent three years.
- `d6s2` Richard Johnson (rugby) [2]: In his time at Ponty, Richard was selected for Wales U21's and Wales 7's and was involved in the squad that won the Welsh Cup in 2002 and narrowly lost to Sale in the Parker Pen European Shield Final.
- `d6s3` Richard Johnson (rugby) [3]: After regional rugby was formed he returned to Neath RFC winning the league twice and Welsh Cup in a three-year stint.
- `d6s4` Richard Johnson (rugby) [4]: Richard then changed codes, signing for Crusader RL and won 4 caps for Wales.
- `d6s5` Richard Johnson (rugby) [5]: He also played on the 7's circuit playing for Samurai 7's, White Hart Marauders, Crusaders and Scorpions.
- `d6s6` Richard Johnson (rugby) [6]: In 2007 Richard left rugby to pursue a career outside sport but continues to play on the 7's circuit and now vets competitions.
- `d7s0` 2010 Welsh Cup Final [0]: The 2010 Welsh Cup Final was the final of the 124th season of the main domestic football cup competition in Wales, the Welsh Cup.
- `d7s1` 2010 Welsh Cup Final [1]: The final was played at Parc y Scarlets in Llanelli on 1 May 2010 and marked the second time the final has been staged at the stadium.
- `d7s2` 2010 Welsh Cup Final [2]: The match was contested by Port Talbot Town, who beat Bala Town 1–0 in their semi-final, and Bangor City who beat Prestatyn Town 2–0 in their semi-final.
- `d8s0` 2011 Welsh Cup Final [0]: The 2011 Welsh Cup Final was the final of the 125th season of the main domestic football cup competition in Wales, the Welsh Cup.
- `d8s1` 2011 Welsh Cup Final [1]: The final was played at Parc y Scarlets in Llanelli on 8 May 2011 and marked the third time the final has been staged at the stadium.
- `d8s2` 2011 Welsh Cup Final [2]: The match was contested by Bangor City, who beat Gap Connah's Quay 1-0 in their semi-final, and Llanelli who beat The New Saints 1-0 in their semi-final.
- `d9s0` 1889 Welsh Cup Final [0]: The 1889 Welsh Cup Final, the 12th in the competition, was contested by Bangor and Northwich Victoria at the Racecourse Ground.
- `d9s1` 1889 Welsh Cup Final [1]: Bangor, in their first Welsh Cup final, won 2–1 in a match that would mark the first time these two teams, future founders and rivals of the Northern Premier League and Alliance Premier League would meet in a major final.
- `d9s2` 1889 Welsh Cup Final [2]: The most recent was the 1984 FA Trophy Final.
- `d10s0` 1979–80 Welsh Cup [0]: The 1979–80 Welsh Cup was the final of the 93rd season of the main domestic football cup competition in Wales, the Welsh Cup.

</details>

## Q220 — `hotpotqa_5ab2a01d5542992953946778` (revised draft)

> What kind of novelists were both Robert Stone and Truman Capote?

Source answer: American

Gold final answer: American

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: nationality descriptor of Robert Stone | false | American | — | [d1s0] | — |
| u2: nationality descriptor of Truman Capote | false | American | — | [d2s0] | — |
| u3: What kind of novelists were both Robert Stone and Truman Capote? | true | American | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d1s0` Robert Stone (novelist) [0]: Robert Stone (August 21, 1937 – January 10, 2015) was an American novelist.
- `d2s0` Truman Capote [0]: Truman Garcia Capote ( ; born Truman Streckfus Persons, September 30, 1924 – August 25, 1984) was an American novelist, screenwriter, playwright, and actor.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Robert Stone (novelist) [0]: Robert Stone (August 21, 1937 – January 10, 2015) was an American novelist.
- `d2s0` Truman Capote [0]: Truman Garcia Capote ( ; born Truman Streckfus Persons, September 30, 1924 – August 25, 1984) was an American novelist, screenwriter, playwright, and actor.
- `d2s1` Truman Capote [1]: Many of Capote's short stories, novels, plays, and nonfiction are recognized as literary classics, including the novella "Breakfast at Tiffany's" (1958) and the true crime novel "In Cold Blood" (1966), which he labeled a "nonfiction novel".
- `d2s2` Truman Capote [2]: At least 20 films and television dramas have been produced of Capote novels, stories, and plays.
- `d3s0` Dallas John Baker [0]: Dallas John Baker (born Dallas John Angguish Baker on 19 February 1968) is an Australian writer and academic noted for poetry, short stories and travel writing whose work deals with themes of alienation, otherness and sexuality.
- `d3s1` Dallas John Baker [1]: He is also known as Dallas Angguish, the name he used as a performance poet beginning in the 1980s.
- `d3s2` Dallas John Baker [2]: He has been repeatedly compared to Truman Capote and to David Sedaris.
- `d3s3` Dallas John Baker [3]: Angguish, who is openly gay, has also written plays and screenplays some of which have been produced.
- `d3s4` Dallas John Baker [4]: He is known for a lyrical style that foregrounds feeling and the use of powerful descriptive passages.
- `d3s5` Dallas John Baker [5]: Due to his evocative short stories, he has been variously described as Truman Capote's literary heir and as reminiscent of Carson McCullers, the much lauded Southern Gothic writer.
- `d3s6` Dallas John Baker [6]: His prose poetry has appeared in the journals Text, Lodestar Quarterly, Retort Magazine and Polari journal.
- `d3s7` Dallas John Baker [7]: His short stories have appeared in the book anthologies ""Dumped"", ""Bend, Don't Shatter"",""Sensual Travels"" and others.
- `d3s8` Dallas John Baker [8]: His collection of memoir and travel writing ""Anywhere But Here"", released in February 2006, received very strong reviews.
- `d3s9` Dallas John Baker [9]: In particular Graeme Aitken of Australian gay magazine DNA wrote:
- `d4s0` Capote (film) [0]: Capote is a 2005 biographical film about Truman Capote, following the events during the writing of Capote's non-fiction book "In Cold Blood".
- `d4s1` Capote (film) [1]: Philip Seymour Hoffman won several awards, including the Academy Award for Best Actor, for his critically acclaimed portrayal of the title character.
- `d4s2` Capote (film) [2]: The film was based on Gerald Clarke's biography "Capote" and was directed by Bennett Miller.
- `d4s3` Capote (film) [3]: It was filmed mostly in Manitoba in the autumn of 2004.
- `d4s4` Capote (film) [4]: It was released September 30, 2005, to coincide with Truman Capote's birthday.
- `d5s0` Truman Capote Award for Literary Criticism [0]: The Truman Capote Award for Literary Criticism is awarded for literary criticism by the University of Iowa on behalf of the Truman Capote Literary Trust.
- `d5s1` Truman Capote Award for Literary Criticism [1]: The value of the award is $30,000 (USD), and is said to be the largest annual cash prize for literary criticism in the English language.
- `d5s2` Truman Capote Award for Literary Criticism [2]: The formal name of the prize is the Truman Capote Award for Literary Criticism in Memory of Newton Arvin, commemorating both Capote and his friend Newton Arvin, who was a distinguished critic and Smith College professor until he lost his job in 1960 after his homosexuality was publicly exposed.
- `d6s0` Truman Capote Literary Trust [0]: The Truman Capote Literary Trust is an American charitable trust established in 1994 by Truman Capote's literary executor, Alan U. Schwartz, pursuant to Capote's will.
- `d7s0` Trilogy (film) [0]: Trilogy (also released as Truman Capote's Trilogy) is a 1969 American anthology drama film directed by Frank Perry and written by Truman Capote.
- `d7s1` Trilogy (film) [1]: It was listed to compete at the 1968 Cannes Film Festival, but the festival was cancelled due to the events of May 1968 in France.
- `d8s0` A Christmas Memory [0]: "A Christmas Memory" is a short story by Truman Capote.
- `d8s1` A Christmas Memory [1]: Originally published in "Mademoiselle" magazine in December 1956, it was reprinted in "The Selected Writings of Truman Capote" in 1963.
- `d8s2` A Christmas Memory [2]: It was issued in a stand-alone hardcover edition by Random House in 1966, and it has been published in many editions and anthologies since.
- `d9s0` One Christmas [0]: "One Christmas" is an autobiographical short story by Truman Capote, portions of which were originally published in a 1982 issue of the "Ladies’ Home Journal" magazine.
- `d9s1` One Christmas [1]: It was shortly thereafter published in 1983 as a book by Random House, Inc and was the final work published by Capote before his death in 1984.
- `d9s2` One Christmas [2]: The story is an emotional childhood tale about the nature of deception and alcoholism.
- `d9s3` One Christmas [3]: It is Capote’s last short story and a sequel to "The Thanksgiving Visitor".
- `d10s0` Infamous (film) [0]: Infamous is a 2006 American drama film based on the 1997 book by George Plimpton "Truman Capote: In Which Various Friends, Enemies, Acquaintances, and Detractors Recall His Turbulent Career".
- `d10s1` Infamous (film) [1]: It covers the period from the late 1950s through the mid-1960s, during which Truman Capote researched and wrote his bestseller "In Cold Blood".

</details>

## Q221 — `hotpotqa_5ab344fc55429969a97a811e` (revised draft)

> Do Bloody Mary and Sidecar share any ingredients in common?

Source answer: no

Gold final answer: yes

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: listed ingredients of Bloody Mary | false | vodka, tomato juice, spices and flavorings including lemon juice | — | [d10s0] | — |
| u2: listed ingredients of Sidecar | false | cognac, orange liqueur, lemon juice | — | [d9s0] | — |
| u3: Do Bloody Mary and Sidecar share any ingredients in common? | true | yes | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d9s0` Sidecar (cocktail) [0]: The sidecar is a cocktail traditionally made with cognac, orange liqueur (Cointreau, Grand Marnier, Grand Gala or another triple sec), and lemon juice.
- `d10s0` Bloody Mary (cocktail) [0]: A Bloody Mary is a cocktail containing vodka, tomato juice, and combinations of other spices and flavorings including Worcestershire sauce, Hot Sauce, piri piri sauce, beef consommé or bouillon, horseradish, celery, olives, salt, black pepper, cayenne pepper, lemon juice, lime juice and/or celery salt.

Notes:

- d10s0与d9s0均列lemon juice，修正no→yes，u3由两组成分交集推出。源答案no留在来源记录。

<details><summary>All source context</summary>

- `d1s0` Agent 077: Mission Bloody Mary [0]: Agent 077: Mission Bloody Mary or Agente 077: Missione Bloody Mary is a 1965 Italian action spy adventure film.
- `d1s1` Agent 077: Mission Bloody Mary [1]: The first of the Secret Agent 077 film series directed by Sergio Grieco.
- `d2s0` Bacon martini [0]: A Bacon Martini, also known as bacontini, pig on the tocks or a bloody bacon martini, is a cocktail that consists of bacon-infused vodka served with a garnish that can include strips of bacon, bacon bits, or olives.
- `d2s1` Bacon martini [1]: Variants may include the addition of Bloody Mary mix.
- `d2s2` Bacon martini [2]: Although not a vodka martini, which consists of vodka and vermouth, the term "bacon martini" is consistent with the trend of calling any straight liquor in a martini glass a "martini," such as the saketini or other variations.
- `d3s0` Bloody Mary (Nerve Endings) [0]: "Bloody Mary (Nerve Endings)", often referred to as just "Bloody Mary", is an indie rock song performed by American alternative rock music group Silversun Pickups.
- `d3s1` Bloody Mary (Nerve Endings) [1]: The song was written by Silversun Pickups, and produced by Jacknife Lee.
- `d3s2` Bloody Mary (Nerve Endings) [2]: It serves as the lead-off single to their third studio album, "Neck of the Woods", which was released on May 8, 2012.
- `d3s3` Bloody Mary (Nerve Endings) [3]: The song reached the top ten of the "Billboard" Alternative Songs chart in May 2012, peaking at number seven in June.
- `d4s0` Bloody Mary Morning [0]: "Bloody Mary Morning" is a song written by American country music singer-songwriter Willie Nelson.
- `d4s1` Bloody Mary Morning [1]: Nelson wrote the song inspired by his struggles to become a "better parent".
- `d4s2` Bloody Mary Morning [2]: It was originally released in the 1970 RCA Records release "Both Sides Now" with the title "Bloody Merry Morning".
- `d5s0` Caesar (cocktail) [0]: A Caesar is a cocktail created and primarily consumed in Canada.
- `d5s1` Caesar (cocktail) [1]: It typically contains vodka, a caesar mix (a blend of tomato juice and clam broth), hot sauce, and Worcestershire sauce, and is served with ice in a large, celery salt-rimmed glass, typically garnished with a stalk of celery and wedge of lime.
- `d5s2` Caesar (cocktail) [2]: What distinguishes it from a Bloody Mary is the inclusion of clam broth.
- `d5s3` Caesar (cocktail) [3]: The cocktail may also be contrasted with the Michelada, which has similar flavouring ingredients but uses beer instead of vodka.
- `d6s0` Bloody Mary (folklore) [0]: Bloody Mary is a folklore legend consisting of a ghost, phantom, or spirit conjured to reveal the future.
- `d6s1` Bloody Mary (folklore) [1]: She is said to appear in a mirror when her name is called three times.
- `d6s2` Bloody Mary (folklore) [2]: The Bloody Mary apparition may be benign or malevolent, depending on historic variations of the legend.
- `d6s3` Bloody Mary (folklore) [3]: The Bloody Mary appearances are mostly "witnessed" in group participation play.
- `d7s0` The Bloody Mary Show [0]: The Bloody Mary Show is a multi-award-winning British comedy web series produced and written by director Darren Chadwick-Hussein.
- `d7s1` The Bloody Mary Show [1]: The series is broadcast on the internet and premiered on September 7, 2012.
- `d7s2` The Bloody Mary Show [2]: So far, seven episodes of season one have been made, with season two currently under development.
- `d7s3` The Bloody Mary Show [3]: The show can be found distributed across the web including on Blip and YouTube.
- `d7s4` The Bloody Mary Show [4]: The Bloody Mary Show follows a group of unconventional ghouls, who can be summoned from the afterlife by the living or are sent to haunt them.
- `d7s5` The Bloody Mary Show [5]: The show focuses on main character Bloody Mary and her friends, Abdabs, Malevolent and Viscera, as they spend their days haunting the living, sharing their experiences and drinking at an underworld bar called Hemingway's, which was filmed in the oldest pub on the River Thames, 'The Mayflower.'
- `d8s0` Typhoon Mary (1960) [0]: Typhoon Mary, also nicknamed "Bloody Mary" by the Joint Typhoon Warning Center (JTWC), was an extremely damaging storm that was part of the 1960 Pacific typhoon season.
- `d8s1` Typhoon Mary (1960) [1]: It began as a circulation in a trough in the South China Sea.
- `d8s2` Typhoon Mary (1960) [2]: A tropical depression formed on June 2, as it was traveling clockwise.
- `d8s3` Typhoon Mary (1960) [3]: It became a tropical storm on the next day, and received the name "Mary".
- `d8s4` Typhoon Mary (1960) [4]: It slowly moved across the sea, strengthening to a typhoon.
- `d8s5` Typhoon Mary (1960) [5]: Mary made landfall in Hong Kong on June 8, and moved through Guangdong and Fujian.
- `d8s6` Typhoon Mary (1960) [6]: It reemerged back to the Pacific Ocean, and restrengthened into a typhoon temporarily.
- `d8s7` Typhoon Mary (1960) [7]: It then traveled east, weakening and becoming extratropical on June 12.
- `d9s0` Sidecar (cocktail) [0]: The sidecar is a cocktail traditionally made with cognac, orange liqueur (Cointreau, Grand Marnier, Grand Gala or another triple sec), and lemon juice.
- `d9s1` Sidecar (cocktail) [1]: In its ingredients, the drink is perhaps most closely related to the older brandy crusta, which differs both in presentation and in proportions of its components.
- `d10s0` Bloody Mary (cocktail) [0]: A Bloody Mary is a cocktail containing vodka, tomato juice, and combinations of other spices and flavorings including Worcestershire sauce, Hot Sauce, piri piri sauce, beef consommé or bouillon, horseradish, celery, olives, salt, black pepper, cayenne pepper, lemon juice, lime juice and/or celery salt.

</details>

## Q222 — `hotpotqa_5ab42f3c55429942dd415ebc` (revised draft)

> What is the translation of the name of the river on which Widnes is located ?

Source answer: boundary river

Gold final answer: boundary river

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: river on which Widnes is located | false | River Mersey | — | [d8s0] OR [d7s3] | — |
| u2: translation of the name of {u1} | true | boundary river | u1 | [d2s1] | — |

Evidence:

- `d2s1` River Mersey [1]: Its name is derived from the Anglo-Saxon language and translates as "boundary river".
- `d7s3` Runcorn [3]: Directly to the north across the River Mersey is the town of Widnes.
- `d8s0` Listed buildings in Widnes [0]: Widnes is an industrial town in the Borough of Halton, Cheshire, England, on the north bank of the River Mersey where it narrows at Runcorn Gap.

Notes:

- 按题干去掉north bank额外限定，补d7s3备选。

<details><summary>All source context</summary>

- `d1s0` Silver Jubilee Bridge [0]: The Silver Jubilee Bridge, "Widnes-Runcorn Bridge" or Runcorn Bridge crosses the River Mersey and the Manchester Ship Canal at Runcorn Gap between Runcorn and Widnes in Halton, England.
- `d1s1` Silver Jubilee Bridge [1]: It is a through arch bridge with a main arch span of 361 yards (330 m).
- `d1s2` Silver Jubilee Bridge [2]: It was opened in 1961 as a replacement for the Widnes-Runcorn Transporter Bridge, and was initially known simply as the Runcorn Bridge or Runcorn–Widnes Bridge.
- `d1s3` Silver Jubilee Bridge [3]: In 1975–77 it was widened, after which it was given its official name in honour of the Queen's Silver Jubilee.
- `d1s4` Silver Jubilee Bridge [4]: It carries the A533 road and a cantilevered footway.
- `d1s5` Silver Jubilee Bridge [5]: The bridge is recorded in the National Heritage List for England as a designated Grade II listed building.
- `d2s0` River Mersey [0]: The River Mersey is a river in the North West of England.
- `d2s1` River Mersey [1]: Its name is derived from the Anglo-Saxon language and translates as "boundary river".
- `d2s2` River Mersey [2]: The river may have been the border between the ancient kingdoms of Mercia and Northumbria and for centuries it formed part of the boundary between the historic counties of Lancashire and Cheshire.
- `d3s0` Deschutes River (Washington) [0]: The Deschutes River is a 50 mi river in Washington, United States.
- `d3s1` Deschutes River (Washington) [1]: Its source is in the Gifford Pinchot National Forest in Lewis County, and it empties into Budd Inlet of Puget Sound at Olympia in Thurston County.
- `d3s2` Deschutes River (Washington) [2]: It was given its name by French fur traders, who called it Rivière des Chutes, or "River of the Falls", a translation of the First Nations name for the site.
- `d3s3` Deschutes River (Washington) [3]: (The city of Tumwater, founded in the same location, takes its name from another translation for "waterfall", this one in Chinook Jargon.)
- `d4s0` Catalyst Science Discovery Centre [0]: The Catalyst Science Discovery Centre (originally known as The Museum of the Chemical Industry) is a science centre and museum focusing on chemistry and the history of the chemical industry.
- `d4s1` Catalyst Science Discovery Centre [1]: It is located near Spike Island in Widnes, Cheshire, and next to the River Mersey.
- `d4s2` Catalyst Science Discovery Centre [2]: The museum is accredited by the Arts Council England.
- `d5s0` Fiddlers Ferry power station [0]: Fiddlers Ferry Power Station is a coal fired power station located in Warrington, Cheshire, in North West England, which is capable of co-firing biomass.
- `d5s1` Fiddlers Ferry power station [1]: It is situated on the north bank of the River Mersey between the towns of Widnes and Warrington.
- `d5s2` Fiddlers Ferry power station [2]: Opened in 1971, the station has a generating capacity of 1,989 megawatts (MW).
- `d5s3` Fiddlers Ferry power station [3]: In a bid to combine efforts at the design and construction stages the Boiler and Turbo-generator plant were replicated at West Burton power station located between Retford and Gainsborough in North Nottinghamshire.
- `d6s0` Mersey Gateway [0]: The Mersey Gateway is a multi-million pound transport scheme between Runcorn and Widnes in Cheshire, England.
- `d6s1` Mersey Gateway [1]: The main part of the project is the construction of the "Mersey Gateway" toll bridge that will span the River Mersey and the Manchester Ship Canal.
- `d6s2` Mersey Gateway [2]: The crossing, which will have three traffic lanes in each direction, will be located approximately 1.5 km to the east of the existing Silver Jubilee Bridge.
- `d6s3` Mersey Gateway [3]: Apart from the new bridge, the project also includes major civil engineering work realigning the existing road network, constructing new interchanges and landscaping 9 km of highway.
- `d7s0` Runcorn [0]: Runcorn is an industrial town and cargo port in Cheshire, England, located within the Borough of Halton.
- `d7s1` Runcorn [1]: In 2010, Runcorn's population was estimated to be 61,000.
- `d7s2` Runcorn [2]: The town is on the southern bank of the River Mersey, where the estuary narrows to form the Runcorn Gap.
- `d7s3` Runcorn [3]: Directly to the north across the River Mersey is the town of Widnes.
- `d7s4` Runcorn [4]: Upstream and 8 mi to the northeast is the town of Warrington, and downstream 16 mi to the west is the city of Liverpool.
- `d8s0` Listed buildings in Widnes [0]: Widnes is an industrial town in the Borough of Halton, Cheshire, England, on the north bank of the River Mersey where it narrows at Runcorn Gap.
- `d8s1` Listed buildings in Widnes [1]: The town contains 21 buildings that are recorded in the National Heritage List for England as designated listed buildings. Of these, 5 are classified at Grade II*, and 16 at Grade II; Widnes has no Grade I listed buildings.
- `d8s2` Listed buildings in Widnes [2]: In the United Kingdom, the term "listed building" refers to a building or other structure officially designated as being of special architectural, historical, or cultural significance.
- `d8s3` Listed buildings in Widnes [3]: Listed buildings are categorised in three grades: Grade I consists of buildings of outstanding architectural or historical interest; Grade II* includes particularly significant buildings of more than local interest; Grade II consists of buildings of special architectural or historical interest.
- `d8s4` Listed buildings in Widnes [4]: Buildings in England are listed by the Secretary of State for Culture, Media and Sport on recommendations provided by English Heritage, which also determines the grading.
- `d9s0` Lac qui Parle River [0]: The Lac qui Parle River is a tributary of the Minnesota River, 118 miles (190 km) long, in southwestern Minnesota in the United States.
- `d9s1` Lac qui Parle River [1]: A number of tributaries of the river, including its largest, the West Branch Lac qui Parle River, also flow in eastern South Dakota.
- `d9s2` Lac qui Parle River [2]: Via the Minnesota River, the Lac qui Parle River is part of the watershed of the Mississippi River, draining an area of 1,156 sqmi in an agricultural region.
- `d9s3` Lac qui Parle River [3]: Slightly more than two-thirds of the Lac qui Parle watershed is in Minnesota.
- `d9s4` Lac qui Parle River [4]: "Lac qui parle" means "the lake which speaks" in the French language, and was a translation of the Sioux name for Lac qui Parle, a lake on the Minnesota River upstream of the mouth of the Lac qui Parle River.
- `d10s0` Cuerdley railway station [0]: One source gives Cuerdley railway station as being on what is now the southeastern edge of Widnes, England, stating that it was located near the then bone works which the 1849 OS Map shows as at the convergence of Moss Lane, the railway, the Sankey Canal, a creek and the north bank of the tidal River Mersey.
- `d10s1` Cuerdley railway station [1]: Of these only Moss Lane is no longer readily identifiable on a modern OS Map.
- `d10s2` Cuerdley railway station [2]: The authoritative "Disused Stations" website does not include an article on Cuerdley station, however, it does repeatedly use a map which places Cuerdley station some distance nearer Warrington.
- `d10s3` Cuerdley railway station [3]: This is corroborated by the Engineer's Line Reference (ELR) database which gives Cuerdley station as 1 mile 10 chains from Fiddlers Ferry and Penketh station and 1 mile 31 chains from Carterhouse Junction.
- `d10s4` Cuerdley railway station [4]: Furthermore, the ELR data gives the station site as only 31 chains west of the modern-day junction for Fiddlers Ferry Power station.

</details>

## Q223 — `hotpotqa_5ab4355555429942dd415ee3` (revised draft)

> What novella was "Eyes Wide Shut," starring Vinessa Elizabeth Shaw, based on?

Source answer: "Traumnovelle" ("Dream Story")

Gold final answer: "Traumnovelle" ("Dream Story")

Question type: `single` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: novella on which Eyes Wide Shut is based | true | "Traumnovelle" ("Dream Story") (accepted alternatives: Traumnovelle; Dream Story) | — | [d3s1] | — |

Evidence:

- `d3s1` Eyes Wide Shut [1]: Based on Arthur Schnitzler's 1926 novella "Traumnovelle" ("Dream Story"), the story is transferred from early 20th century Vienna to 1990s New York City.

Notes:

- 题干已给电影名，移除Vinessa Shaw桥接。

<details><summary>All source context</summary>

- `d1s0` Garden Party (film) [0]: Garden Party is a 2008 American drama film directed by Jason Freeland, starring Vinessa Shaw, Willa Holland and Oscar winner Jennifer Lawrence in her film debut.
- `d1s1` Garden Party (film) [1]: The film was shot in Los Angeles, California and was released on July 11, 2008 in the United States.
- `d2s0` Elizabeth Shaw (confectionery company) [0]: Elizabeth Shaw is the trading name of a Bristol based company that markets chocolate-based confectionery, including the well-known brands Famous Names chocolate liqueurs and Elizabeth Shaw after dinner mints.
- `d2s1` Elizabeth Shaw (confectionery company) [1]: The company has recently extended its range to include Flutes, and a Crisp Collection gift box, featuring products based on its unique honeycomb crisp inclusion.
- `d2s2` Elizabeth Shaw (confectionery company) [2]: It also markets a range of 100g bars, featuring its best loved flavours.
- `d3s0` Eyes Wide Shut [0]: Eyes Wide Shut is a 1999 erotic drama film directed, produced, and co-written by Stanley Kubrick.
- `d3s1` Eyes Wide Shut [1]: Based on Arthur Schnitzler's 1926 novella "Traumnovelle" ("Dream Story"), the story is transferred from early 20th century Vienna to 1990s New York City.
- `d3s2` Eyes Wide Shut [2]: The film follows the sexually-charged adventures of Dr. Bill Harford, who is shocked when his wife, Alice, reveals that she had contemplated having an affair a year earlier.
- `d3s3` Eyes Wide Shut [3]: He embarks on a night-long adventure, during which he infiltrates a massive masked orgy of an unnamed secret society.
- `d4s0` Rudolf Sieczyński [0]: Rudolf Sieczyński (1879, Vienna – 1952, Vienna) was an Austrian composer of Polish ancestry.
- `d4s1` Rudolf Sieczyński [1]: His fame today rests almost exclusively on the nostalgic Viennese song "Wien, du Stadt meiner Träume" ("Vienna, City of My Dreams"), whose melody and lyrics he wrote in 1914.
- `d4s2` Rudolf Sieczyński [2]: A well-known recording was made in 1957 by Elisabeth Schwarzkopf with Otto Ackermann conducting the Philharmonia Orchestra.
- `d4s3` Rudolf Sieczyński [3]: The song was featured in the soundtrack of the Stanley Kubrick film "Eyes Wide Shut".
- `d5s0` Tom Cruise: Unauthorized [0]: Tom Cruise: Unauthorized is a non-fiction biographical book about Tom Cruise, written by Wensley Clarkson.
- `d5s1` Tom Cruise: Unauthorized [1]: The book was published by Hastings House in 1998.
- `d5s2` Tom Cruise: Unauthorized [2]: The book discusses Tom Cruise's early life, his rise as an actor, involvement with Scientology, and past relationships with Mimi Rogers and Nicole Kidman.
- `d5s3` Tom Cruise: Unauthorized [3]: The book ended during the filming of "Eyes Wide Shut".
- `d6s0` Forever Blue (Chris Isaak album) [0]: Forever Blue is the fifth album by American rock and roll musician Chris Isaak, released in 1995.
- `d6s1` Forever Blue (Chris Isaak album) [1]: The album included three singles: the Grammy-nominated "Somebody's Crying"; "Baby Did a Bad Bad Thing," which was featured in Stanley Kubrick's final film, "Eyes Wide Shut"; and "Graduation Day," featured in the 1996 film "Beautiful Girls".
- `d6s2` Forever Blue (Chris Isaak album) [2]: In 1996, Forever Blue was also nominated for Best Rock Album.
- `d7s0` Filmography and awards of Stanley Kubrick [0]: Stanley Kubrick directed 13 feature films and three short documentaries over the course of his career, from "Day of the Fight" in 1951 to "Eyes Wide Shut" in 1999.
- `d7s1` Filmography and awards of Stanley Kubrick [1]: Many of Kubrick's films were nominated for Academy Awards or Golden Globes, but his only personal win of an Academy Award was for his work as director of special effects on "".
- `d8s0` Adam Bond [0]: Adam Richardson Bond is a multi-ethnic, British-American actor and stage director.
- `d8s1` Adam Bond [1]: He began his career as a teenager as a film extra in Stanley Kubrick's final film, "Eyes Wide Shut".
- `d8s2` Adam Bond [2]: He has had minor roles in films such as "Green Zone", "Legally Blonde", "" and "Inkheart".
- `d8s3` Adam Bond [3]: His heritage can be traced back to Jewish, Polish, Scottish, French, Irish, and Lakota Sioux ancestry.
- `d8s4` Adam Bond [4]: During spring 2016 and 2017, he has portrayed Jesus Christ for the U.S.-based cable news giant CNN's continuing docudrama series "Finding Jesus: Faith, Fact, Forgery", in tandem with the Christian faith's observance of the Passion of Christ and Easter.
- `d9s0` Vinessa Shaw [0]: Vinessa Elizabeth Shaw (born July 19, 1976) is an American film actress and model.
- `d9s1` Vinessa Shaw [1]: Shaw has starred in numerous motion pictures since the early 1990s and was a supporting cast member in the Showtime Drama "Ray Donovan".
- `d9s2` Vinessa Shaw [2]: Her breakout role was in Disney's 1993 Halloween comedy-fantasy hit film "Hocus Pocus".
- `d9s3` Vinessa Shaw [3]: She also was in "Ladybugs" (1992), Stanley Kubrick's "Eyes Wide Shut" (1999), the 2006 remake of Wes Craven's horror picture "The Hills Have Eyes", and "40 Days and 40 Nights", as Josh Hartnett's character's sadistic ex-girlfriend.
- `d9s4` Vinessa Shaw [4]: She stars as Dr. Jane Mathis in the 2017 Netflix original "Clinical".
- `d10s0` Influence of Stanley Kubrick [0]: Stanley Kubrick is regarded by film critics and historians as one of the most influential directors of all time.
- `d10s1` Influence of Stanley Kubrick [1]: Leading directors, including Martin Scorsese, Steven Spielberg, George Lucas, James Cameron, Woody Allen, Terry Gilliam, the Coen Brothers, Ridley Scott, Paul Thomas Anderson, Christopher Nolan, David Lynch, and George A. Romero, have cited Kubrick as a source of inspiration, and in the case of Spielberg, collaboration.
- `d10s2` Influence of Stanley Kubrick [2]: In an interview for the "Eyes Wide Shut" DVD release, Steven Spielberg comments that "nobody could shoot a picture better in history", and that Kubrick told stories in a way "antithetical to the way we are accustomed to receiving stories".
- `d10s3` Influence of Stanley Kubrick [3]: Writing in the introduction to a recent edition of Michel Ciment's "Kubrick", film director Martin Scorsese notes most of Kubrick's films were misunderstood and under-appreciated when first released, only to be considered masterpieces later on.

</details>

## Q224 — `hotpotqa_5ab439bd55429942dd415eee` (revised draft)

> Who won more Grand Slam Titles, Liezel Huber or Billie Jean King?

Source answer: Billie Jean King

Gold final answer: Billie Jean King

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: Grand Slam title counts listed for Liezel Huber | false | 4 women's doubles with Cara Black; 1 with Lisa Raymond; 2 mixed doubles with Bob Bryan | — | [d6s1] | — |
| u2: Grand Slam title count of Billie Jean King | false | 39 | — | [d5s1] | — |
| u3: Who won more Grand Slam Titles, Liezel Huber or Billie Jean King? | true | Billie Jean King | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d5s1` Billie Jean King [1]: King won 39 Grand Slam titles: 12 in singles, 16 in women's doubles, and 11 in mixed doubles.
- `d6s1` Liezel Huber [1]: Huber has won four Grand Slam titles in women's doubles with partner Cara Black, one with Lisa Raymond, and two mixed doubles titles with Bob Bryan.

Notes:

- 事实unit保留原文4、1、2，不把7冒充原文值；u3按确定性算术4+1+2=7<39比较。

<details><summary>All source context</summary>

- `d1s0` 1968 Australian Championships [0]: The 1968 Australian Championships was a tennis tournament that took place in the outdoor Kooyong Stadium in Melbourne, Australia from 19 to 29 January.
- `d1s1` 1968 Australian Championships [1]: It was the 56th edition of the Australian Championships (now known as Australian Open), the 16th held in Melbourne, and the first Grand Slam tournament of the year.
- `d1s2` 1968 Australian Championships [2]: It was also the last Grand Slam tournament to be restricted to amateurs.
- `d1s3` 1968 Australian Championships [3]: The singles titles were won by Australian William Bowrey and American Billie Jean King.
- `d2s0` 1983 Australian Open – Women's Singles [0]: First-seeded Martina Navratilova defeated ninth-seeded Kathy Jordan 6–2, 7–6 in the final to win the Women's Singles title at the 1983 Australian Open tennis tournament.
- `d2s1` 1983 Australian Open – Women's Singles [1]: The tournament was played on grass courts at the Kooyong Stadium in Melbourne from 29 November through 11 December 1983.
- `d2s2` 1983 Australian Open – Women's Singles [2]: Navratilova earned $75,000 prize money for winning the title, her 8th career Grand Slam singles title and her 2nd title at the Australian Open after 1981.
- `d2s3` 1983 Australian Open – Women's Singles [3]: She improved her year record to 86 wins and 1 loss.
- `d2s4` 1983 Australian Open – Women's Singles [4]: This tournament was also notable for being the first Australian Open in which Steffi Graf appeared in the main draw, and the last time that Billie Jean King appeared in the main singles draw of a grand slam.
- `d3s0` Ken Rosewall [0]: Kenneth Robert Rosewall {'1': ", '2': ", '3': 'AM, MBE', '4': "} (born 2 November 1934) is a former world top-ranking amateur and professional tennis player from Australia.
- `d3s1` Ken Rosewall [1]: He won a record 23 tennis Majors including 8 Grand Slam singles titles and before the Open Era a record 15 Pro Slam titles and a record 35 Major finals overall.
- `d3s2` Ken Rosewall [2]: He won the Pro Grand Slam in 1963.
- `d3s3` Ken Rosewall [3]: Rosewall won 9 slams in doubles with a career double grand slam.
- `d3s4` Ken Rosewall [4]: He is considered to be one of the greatest tennis players of all time.
- `d3s5` Ken Rosewall [5]: He had a renowned backhand and enjoyed a long career at the highest levels from the early 1950s to the early 1970s.
- `d3s6` Ken Rosewall [6]: Rosewall was one of the two best male players for about nine years and was the World No. 1 player for a number of years in the early 1960s.
- `d3s7` Ken Rosewall [7]: He was ranked among the top 20 players, amateur or professional, every year from 1952 through 1977.
- `d3s8` Ken Rosewall [8]: Rosewall is the only player to have simultaneously held Pro Grand Slam titles on three different surfaces (1962–1963).
- `d3s9` Ken Rosewall [9]: At the 1971 Australian Open he became the first male player during the open era to win a Grand Slam tournament without dropping a set.
- `d4s0` 2013 New Haven Open at Yale – Doubles [0]: Liezel Huber and Lisa Raymond were the defending champions, but decided not to defend their title together.
- `d4s1` 2013 New Haven Open at Yale – Doubles [1]: Huber partnered up with Nuria Llagostera Vives, while Raymond played alongside Flavia Pennetta.
- `d4s2` 2013 New Haven Open at Yale – Doubles [2]: Huber and Llagostera Vives defeated Pennetta and Raymond in the first round, but lost to Anabel Medina Garrigues and Katarina Srebotnik in the semifinals.
- `d4s3` 2013 New Haven Open at Yale – Doubles [3]: <br>
- `d5s0` Billie Jean King [0]: Billie Jean King ("née" Moffitt; born November 22, 1943) is an American former World No. 1 professional tennis player.
- `d5s1` Billie Jean King [1]: King won 39 Grand Slam titles: 12 in singles, 16 in women's doubles, and 11 in mixed doubles.
- `d5s2` Billie Jean King [2]: King won the singles title at the inaugural WTA Tour Championships.
- `d5s3` Billie Jean King [3]: King often represented the United States in the Federation Cup and the Wightman Cup.
- `d5s4` Billie Jean King [4]: She was a member of the victorious United States team in seven Federation Cups and nine Wightman Cups.
- `d5s5` Billie Jean King [5]: For three years, King was the United States' captain in the Federation Cup.
- `d6s0` Liezel Huber [0]: Liezel Huber (née Horn; born 21 August 1976) is a South African-American retired tennis player who represents the United States internationally.
- `d6s1` Liezel Huber [1]: Huber has won four Grand Slam titles in women's doubles with partner Cara Black, one with Lisa Raymond, and two mixed doubles titles with Bob Bryan.
- `d6s2` Liezel Huber [2]: On 12 November 2007, she became the co-World No. 1 in doubles with Cara Black.
- `d6s3` Liezel Huber [3]: On 19 April 2010, Huber became the sole No. 1 for the first time in her career.
- `d7s0` Tennis at the 2012 Summer Olympics [0]: The tennis tournaments at the 2012 Summer Olympics in London were staged at the All England Club in Wimbledon, from 28 July to 5 August.
- `d7s1` Tennis at the 2012 Summer Olympics [1]: This was the first Olympic grass court tournament since tennis was reintroduced as an Olympic sport and the first to be held at a Grand Slam venue in the Open era.
- `d7s2` Tennis at the 2012 Summer Olympics [2]: (Two other 2012 Summer Olympic bid finalists had also offered Grand Slam venues – second-place finisher Paris offered the French Open venue, the Stade Roland Garros, while fourth-place finisher New York offered the US Open venue, the USTA Billie Jean King National Tennis Center in Flushing Meadows-Corona Park, Queens.)
- `d8s0` 2010 Aegon Classic – Doubles [0]: Cara Black and Liezel Huber were the two-time defending champions but did not compete together.
- `d8s1` 2010 Aegon Classic – Doubles [1]: Black partnered up with Lisa Raymond and Huber with Bethanie Mattek-Sands.
- `d8s2` 2010 Aegon Classic – Doubles [2]: Black and Raymond won in the final after Huber and Mattek-Sands retired.
- `d9s0` 1983 Wimbledon Championships – Women's Singles [0]: Martina Navratilova defeated Andrea Jaeger 6–0, 6–3 in the final to win the Ladies' Singles tennis title at the 1983 Wimbledon Championships.
- `d9s1` 1983 Wimbledon Championships – Women's Singles [1]: Billie Jean King became the oldest semi-finalist at a Grand Slam event at 39 years, 7 months and 9 days old, an Open Era record.
- `d9s2` 1983 Wimbledon Championships – Women's Singles [2]: Chris Evert's loss in the 3rd round, snapped a streak of 34 consecutive Grand Slam semi-finals, she had made the semi-finals in her first 34 Grand Slam appearances between the US Open 1971 and the French Open 1983.
- `d10s0` 2005 French Open – Women's Doubles [0]: First-seeded defending champions Virginia Ruano Pascual and Paola Suárez defeated second-seeded Cara Black and Liezel Huber to win the title for the fourth time (after 2001, 2002 and 2004).
- `d10s1` 2005 French Open – Women's Doubles [1]: It was their 29th doubles title together, of which eight were won at Grand Slam tournaments.

</details>

## Q225 — `hotpotqa_5ab439f055429942dd415eef` (revised draft)

> Which airport Albany International Airport and Dane County Regional Airport is nearer its local town ?

Source answer: Dane County Regional Airport

Gold final answer: Dane County Regional Airport

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: distance from Albany International Airport to Albany | false | 7 miles | — | [d7s0] | — |
| u2: distance from Dane County Regional Airport to downtown Madison | false | 6 miles | — | [d8s0] | — |
| u3: Which airport Albany International Airport and Dane County Regional Airport is nearer its local town ? | true | Dane County Regional Airport | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d7s0` Albany International Airport [0]: Albany International Airport (IATA: ALB, ICAO: KALB, FAA LID: ALB) is a public airport seven miles (11 km) northwest of Albany, in Albany County, New York, United States.
- `d8s0` Dane County Regional Airport [0]: Dane County Regional Airport (DCRA) (IATA: MSN, ICAO: KMSN, FAA LID: MSN) (Truax Field) is a civil-military airport located six miles northeast of downtown Madison, the capital of Wisconsin.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Raleigh Executive Jetport [0]: Raleigh Exec: The Raleigh Executive Jetport @ Sanford-Lee County or Raleigh Exec Jetport at Sanford-Lee CountyFAA Airport Master Record for TTA (Form 5010 ) (ICAO: KTTA, FAA LID: TTA) is a public use airport located seven nautical miles (8 mi, 13 km) northeast of the central business district of Sanford, a city in Lee County, North Carolina, United States.
- `d1s1` Raleigh Executive Jetport [1]: It is owned by the Sanford-Lee County Regional Airport Authority and was previously known as Sanford-Lee County Regional Airport.
- `d1s2` Raleigh Executive Jetport [2]: This airport is included in the National Plan of Integrated Airport Systems for 2011–2015, which categorized it as a "reliever airport" for Raleigh-Durham International Airport.
- `d2s0` Pensacola International Airport [0]: Pensacola International Airport (IATA: PNS, ICAO: KPNS, FAA LID: PNS) , formerly Pensacola Gulf Coast Regional Airport and Pensacola Regional Airport (Hagler Field), is a public use airport three nautical miles (6 km) northeast of the central business district of Pensacola, in Escambia County, Florida, United States.
- `d2s1` Pensacola International Airport [1]: It is owned by the City of Pensacola.
- `d2s2` Pensacola International Airport [2]: Despite the name, this airport does not offer direct international flights.
- `d2s3` Pensacola International Airport [3]: This airport is one of the five major airports in North Florida, others being: Northwest Florida Beaches International Airport, Destin-Fort Walton Beach Airport Tallahassee International Airport, and Jacksonville International Airport.
- `d3s0` Elizabeth City Regional Airport [0]: Elizabeth City Regional Airport (IATA: ECG, ICAO: KECG, FAA LID: ECG) is a joint civil-military public and military use airport located three nautical miles (6 km) southeast of the central business district of Elizabeth City, in Pasquotank County, North Carolina, United States.
- `d3s1` Elizabeth City Regional Airport [1]: The airport, on the shore of the Pasquotank River, is also known as Elizabeth City-Pasquotank County Regional Airport or ECG Regional Airport.
- `d3s2` Elizabeth City Regional Airport [2]: It is included in the National Plan of Integrated Airport Systems for 2011–2015, which categorized it as a "general aviation" facility.
- `d4s0` Lea County Regional Airport [0]: Lea County Regional Airport (IATA: HOB, ICAO: KHOB) (Lea County-Hobbs Airport) is four miles (6.4 km) west of Hobbs, in Lea County, New Mexico.
- `d4s1` Lea County Regional Airport [1]: The airport covers 898 acre and has three runways.
- `d4s2` Lea County Regional Airport [2]: It is an FAA certified commercial airport served by United Airlines' affiliate with daily regional flights.
- `d4s3` Lea County Regional Airport [3]: Lea County Regional Airport is the largest of the three airports owned and operated by Lea County Government.
- `d4s4` Lea County Regional Airport [4]: Lea County also owns and operated two general aviation airports in Lovington and Jal, New Mexico.
- `d5s0` Susquehanna Area Regional Airport Authority [0]: The Susquehanna Area Regional Airport Authority (SARAA) is the governing authority of Harrisburg International Airport, Capital City Airport, Franklin County Regional Airport and Gettysburg Regional Airport in south-central Pennsylvania.
- `d5s1` Susquehanna Area Regional Airport Authority [1]: SARAA was incorporated on September 9, 1997, and officially took over control of HIA and CXY airports from the Commonwealth of Pennsylvania on January 1, 1998.
- `d6s0` Sharp County Regional Airport [0]: Sharp County Regional Airport (IATA: CKK, ICAO: KCVK, FAA LID: CVK) is a public-use airport in Sharp County, Arkansas, United States.
- `d6s1` Sharp County Regional Airport [1]: It is located three nautical miles (4 mi, 6 km) northeast of the central business district of Ash Flat, Arkansas.
- `d6s2` Sharp County Regional Airport [2]: The airport is owned by the Sharp County Regional Airport Authority.
- `d7s0` Albany International Airport [0]: Albany International Airport (IATA: ALB, ICAO: KALB, FAA LID: ALB) is a public airport seven miles (11 km) northwest of Albany, in Albany County, New York, United States.
- `d7s1` Albany International Airport [1]: It is owned by the Albany County Airport Authority.
- `d8s0` Dane County Regional Airport [0]: Dane County Regional Airport (DCRA) (IATA: MSN, ICAO: KMSN, FAA LID: MSN) (Truax Field) is a civil-military airport located six miles northeast of downtown Madison, the capital of Wisconsin.
- `d8s1` Dane County Regional Airport [1]: In the Federal Aviation Administration (FAA) National Plan of Integrated Airport Systems for 2017–2021, it is categorized as a small-hub primary commercial service facility.
- `d9s0` Truax Field Air National Guard Base [0]: Truax Field Air National Guard Base (IATA: MSN, ICAO: KMSN, FAA LID: MSN) , also known as Truax Field, is a military facility located at Dane County Regional Airport.
- `d9s1` Truax Field Air National Guard Base [1]: It is located five miles (8 km) northeast of the center of Madison, a city in Dane County, Wisconsin, United States.
- `d10s0` Eagle County Regional Airport [0]: Eagle County Regional Airport (IATA: EGE, ICAO: KEGE, FAA LID: EGE) (Vail/Eagle Airport or the Eagle Vail Airport) is four miles (6 km) west of Eagle, Colorado.
- `d10s1` Eagle County Regional Airport [1]: The airport serves its namesake Eagle County, which includes visitors to the nearby Vail and Beaver Creek ski resorts.
- `d10s2` Eagle County Regional Airport [2]: It covers 632 acre and has one runway.
- `d10s3` Eagle County Regional Airport [3]: The History Channel rated Eagle County Regional Airport as #8 on its list of Most Extreme Airports in July, 2010 due to the elevation, weather variability, an approach through mountainous terrain and challenging departure procedures.
- `d10s4` Eagle County Regional Airport [4]: In 2008–2009, the Airport completed a runway repaving and extension project, increasing the runway length to 9,000 feet.

</details>

## Q226 — `hotpotqa_5a7a0d665542990783324e14` (revised draft)

> Who was born first, Joe Manganiello or Kirk Kerkorian?

Source answer: Kerkor "Kirk" Kerkorian

Gold final answer: Kirk Kerkorian

Question type: `comparison` (source type `comparison`)

Replaces: `hotpotqa_5ab4da5b55429942dd415f96`

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: birth year of Joe Manganiello | false | 1976 | — | [d3s0] | — |
| u2: birth year of Kirk Kerkorian | false | 1917 | — | [d10s0] | — |
| u3: Who was born first, Joe Manganiello or Kirk Kerkorian? | true | Kirk Kerkorian (accepted alternatives: Kerkor "Kirk" Kerkorian) | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d3s0` Joe Manganiello [0]: Joseph Michael Manganiello ( ; ] ; born December 28, 1976) is an American actor.
- `d10s0` Kirk Kerkorian [0]: Kerkor "Kirk" Kerkorian (June 6, 1917 – June 15, 2015) was an Armenian-American businessman, investor, and philanthropist.

Notes:

- 替换：乐队成员关系不唯一且用户明确要求换题。 新题保留原source type，人工核对两条显式事实及答案。

<details><summary>All source context</summary>

- `d1s0` Frank Rosenfelt [0]: Frank E. Rosenfelt (November 15, 1921 – August 2, 2007) was an American executive who served as CEO of Metro-Goldwyn-Mayer (MGM) studio under MGM owner Kirk Kerkorian from 1972 until 1982.
- `d1s1` Frank Rosenfelt [1]: Additionally, Rosenfelt spearheaded the acquisition of United Artists by MGM in 1981.
- `d2s0` Paul Steelman [0]: Paul Curtis Steelman, a native of Atlantic City, is an American architect that is recognized as a visionary designer of global entertainment, hospitality, and gaming architecture based in Las Vegas, Nevada and Macau.
- `d2s1` Paul Steelman [1]: Paul has designed buildings for the mavericks of the gaming industry, including Kirk Kerkorian, Steve Wynn, Sheldon Adelson, Francis Lui, Lawrence Ho, Tan Sri Dato' Lim Kok Thay, Tan Sri Dr Chen Lip Keong, Prince Albert of Monaco, Bob Stupak, Frank Modica, Phil Satre, Derek Stevens and Stanley Ho.
- `d3s0` Joe Manganiello [0]: Joseph Michael Manganiello ( ; ] ; born December 28, 1976) is an American actor.
- `d3s1` Joe Manganiello [1]: He played Flash Thompson in Sam Raimi's "Spider-Man" trilogy and had various recurring roles in television on "ER", "How I Met Your Mother", and "One Tree Hill", before landing his breakout role as werewolf Alcide Herveaux on the HBO television series "True Blood".
- `d3s2` Joe Manganiello [2]: In 2011, he was voted "Favorite Pop-Culture Werewolf of All Time" by the readers of "Entertainment Weekly", and one of "Men's Health"'s "100 Fittest Men of All Time".
- `d4s0` Greg Bautzer [0]: Gregson Edward Bautzer (April 3, 1911 – October 26, 1987) was an American attorney, representing such stars as Ginger Rogers, Ingrid Bergman and Joan Crawford, Kirk Kerkorian, Howard Hughes and William R. Wilkerson.
- `d5s0` Fade Out: The Calamitous Final Days of MGM [0]: Fade Out: The Calamitous Final Days of MGM is a 1990 non-fiction book by Peter Bart which covers the history of MGM since 1969, when it was bought by Kirk Kerkorian.
- `d5s1` Fade Out: The Calamitous Final Days of MGM [1]: Bart was an executive at MGM in 1983 and 1984.
- `d6s0` Tracinda [0]: Tracinda Corporation is an American private investment corporation that was owned by the late Kirk Kerkorian.
- `d6s1` Tracinda [1]: Its major investments include a minority interest of MGM Resorts International.
- `d6s2` Tracinda [2]: Tracinda is headquartered in Las Vegas, Nevada.
- `d6s3` Tracinda [3]: The company was named after Kerkorian's daughters, Tracy and Linda.
- `d7s0` Tumbledown (2015 film) [0]: Tumbledown is a 2015 American romantic comedy film directed by Sean Mewshaw and written by Desiree Van Til.
- `d7s1` Tumbledown (2015 film) [1]: The film stars Jason Sudeikis, Rebecca Hall, Dianna Agron, and Joe Manganiello.
- `d7s2` Tumbledown (2015 film) [2]: The film was released on February 5, 2016, by Starz Digital.
- `d8s0` Smurfs: The Lost Village [0]: Smurfs: The Lost Village is a 2017 American 3D computer-animated comedy-adventure film produced by Sony Pictures Animation and The Kerner Entertainment Company, with animation by Sony Pictures Imageworks, for Columbia Pictures.
- `d8s1` Smurfs: The Lost Village [1]: Sony, LStar Capital and Wanda Pictures co-financed the film.
- `d8s2` Smurfs: The Lost Village [2]: It is based on "The Smurfs" comic book series created by the Belgian comics artist Peyo, and is a reboot unrelated to Sony's previous live-action/animated films based on the series.
- `d8s3` Smurfs: The Lost Village [3]: It was written by Stacey Harman and Pamela Ribon and directed by Kelly Asbury, and stars the voices of Demi Lovato, Rainn Wilson, Joe Manganiello, Mandy Patinkin, Jack McBrayer, Danny Pudi, Michelle Rodriguez, Ellie Kemper, Ariel Winter, Meghan Trainor, Jake Johnson and Julia Roberts.
- `d8s4` Smurfs: The Lost Village [4]: In the film, a mysterious map prompts Smurfette, Brainy, Clumsy and Hefty to find a lost village before Gargamel does.
- `d9s0` Jerry York (businessman) [0]: Jerome Bailey York (June 22, 1938 – March 18, 2010), commonly known as Jerry York, was an American businessman, and the Chairman, President and CEO of Harwinton Capital.
- `d9s1` Jerry York (businessman) [1]: He was the former CFO of IBM and Chrysler, and was CEO of Micro Warehouse.
- `d9s2` Jerry York (businessman) [2]: He was a chief aide to Kirk Kerkorian and his Tracinda investment company.
- `d9s3` Jerry York (businessman) [3]: In February 2006, Kerkorian helped elect York to the board of directors of General Motors, from which he had previously resigned.
- `d10s0` Kirk Kerkorian [0]: Kerkor "Kirk" Kerkorian (June 6, 1917 – June 15, 2015) was an Armenian-American businessman, investor, and philanthropist.
- `d10s1` Kirk Kerkorian [1]: He was the president and CEO of Tracinda Corporation, his private holding company based in Beverly Hills, California.
- `d10s2` Kirk Kerkorian [2]: Kerkorian is known for having been one of the important figures in the shaping of Las Vegas and, with architect Martin Stern, Jr. described as the "father of the mega-resort".
- `d10s3` Kirk Kerkorian [3]: He built the world's largest hotel in Las Vegas three times: the International Hotel (opened in 1969), the MGM Grand Hotel (1973) and the MGM Grand (1993).
- `d10s4` Kirk Kerkorian [4]: He purchased the Metro-Goldwyn-Mayer movie studio in 1969.

</details>

## Q227 — `hotpotqa_5ab4ec2755429942dd415fa6` (revised draft)

> Nelson Chai is the former president of what financial holding company that was founded in 1908, and is headquartered in New York City?

Source answer: CIT Group Inc.

Gold final answer: CIT Group Inc.

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: company of which Nelson Chai was former president | false | CIT Group | — | [d9s2] | — |
| u2: financial holding company {u1}, founded in 1908 and based in New York City | true | CIT Group Inc. | u1 | [d3s0] | — |

Evidence:

- `d3s0` CIT Group [0]: CIT Group Inc. is a financial holding company founded in 1908 headquartered in New York City.
- `d9s2` Nelson Chai [2]: He is the former president of CIT Group and reported directly to then CEO John Thain.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` BBVA Compass [0]: BBVA Compass Bancshares, Inc. (formerly Compass Bancshares) is a United States-based financial holding company headquartered in Birmingham, Alabama.
- `d1s1` BBVA Compass [1]: It has been a subsidiary of the Spanish multinational Banco Bilbao Vizcaya Argentaria since 2007 and operates chiefly in Alabama, Arizona, California, Colorado, Florida, New Mexico, and Texas.
- `d2s0` New York Private Bank &amp; Trust [0]: New York Private Bank & Trust Corporation is a bank holding company headquartered in New York City, United States.
- `d2s1` New York Private Bank &amp; Trust [1]: Howard Milstein is the Chairman, President & Chief Executive Officer.
- `d2s2` New York Private Bank &amp; Trust [2]: As of early 2007, it had $17.3 billion in assets and was the 50th largest bank holding company in the United States.
- `d2s3` New York Private Bank &amp; Trust [3]: The company has over 1211 employees.
- `d3s0` CIT Group [0]: CIT Group Inc. is a financial holding company founded in 1908 headquartered in New York City.
- `d3s1` CIT Group [1]: The company's name is an abbreviation of an early corporate name, Commercial Investment Trust.
- `d3s2` CIT Group [2]: It provides financing and leasing capital to customers in over 30 industries.
- `d3s3` CIT Group [3]: CIT also operates CIT Bank, an FDIC insured bank, its primary bank subsidiary.
- `d4s0` Katherine Oliver [0]: Katherine Oliver is an American media and entertainment executive based in New York City.
- `d4s1` Katherine Oliver [1]: Oliver is currently a Principal at Bloomberg Associates, a philanthropic consultancy firm founded by Michael Bloomberg to provide advice and long-term solutions to cities worldwide.
- `d4s2` Katherine Oliver [2]: On August 1, 2002, she was appointed by New York City Mayor Michael Bloomberg as the Commissioner of The New York City Mayor's Office of Film, Theatre and Broadcasting, which facilitates all aspects of film, television and commercial production in New York City, coordinating on-location filming, liaising with the community and promoting the City as an entertainment capital.
- `d4s3` Katherine Oliver [3]: Oliver was the main liaison between the Mayor's Office and Hollywood and aimed "to make filmmakers and production companies happy to return to New York."
- `d4s4` Katherine Oliver [4]: In 2013, Oliver and Mayor Bloomberg were featured on the cover of Variety and were credited for their role in "revitalizing the city's entertainment sector."
- `d4s5` Katherine Oliver [5]: An economic impact study released by the Boston Consulting Group in 2012 found that New York City's entertainment industry during Oliver's tenure as film commissioner had grown to account for a $7.1 billion annual direct spend in New York City, an increase of $2 billion since 2002, and that the local industry created 30,000 jobs in New York City since 2004, growing to employ 130,000 people.
- `d4s6` Katherine Oliver [6]: AM New York noted that: "New York's film and TV industry is stronger than it has ever been, pumping $7.1 billion into the local economy in 2011 and bringing in some $60 billion over the last decade."
- `d4s7` Katherine Oliver [7]: After Bloomberg announced that former president and co-founder of NYC Media Group Arick Wierson was returning to the private sector, Bloomberg named Oliver as the incoming president of NYC Media and general manager of NYCTV.
- `d4s8` Katherine Oliver [8]: In July 2010, Oliver became the commissioner of the Mayor's Office of Media and Entertainment, the city agency that includes the Mayor's Office of Film, Theatre and Broadcasting, NYC Media, and NYC Digital.
- `d5s0` Astoria Bank [0]: Astoria Bank (formerly Astoria Federal Savings & Loan Association) is a bank based in Long Island City, New York.
- `d5s1` Astoria Bank [1]: Astoria Financial Corporation is the holding company formed in 1993 to facilitate the conversion of Astoria Federal Savings and Loan Association from a mutual form of ownership to stock ownership.
- `d5s2` Astoria Bank [2]: Astoria Financial Corporation, with assets of $16.5 billion, is the holding company for Astoria Federal Savings and Loan Association.
- `d5s3` Astoria Bank [3]: Established in 1888, Astoria Federal, with deposits in New York totaling $10.4 billion, is the largest thrift depository in New York.
- `d6s0` Roman Sledziejowski [0]: Roman J. Sledziejowski (pronounced sleh-jay-YOV-ski) is a Polish-born investment manager widely recognized on Wall Street as an alleged criminal, liar, and thief, allegedly.
- `d6s1` Roman Sledziejowski [1]: After graduating from high school as class valedictorian, he attended Columbia University in New York City.
- `d6s2` Roman Sledziejowski [2]: In late 1990s Sledziejowski became one of the youngest licensed stockbrokers on Wall Street.
- `d6s3` Roman Sledziejowski [3]: He began his professional career at Salomon Smith Barney as an investment consultant in 1998, where he remained until 2002.
- `d6s4` Roman Sledziejowski [4]: From 2002 until 2004 he held the positions of Vice President and First Vice President for Prudential Financial, Inc. From 2004 until 2006, Sledziejowski served as a Senior Vice President of Investments and Firm's Investment Officer at Wachovia Securities.
- `d6s5` Roman Sledziejowski [5]: In 2006 he became the Chief Executive Officer of Innovest Holdings, a New York City–based financial services holding company with several subsidiary entities.
- `d6s6` Roman Sledziejowski [6]: Among them was an SEC registered Broker/Dealer catering mostly to Latin American Financial Market, TWS Financial, LLC.
- `d7s0` IberiaBank [0]: IberiaBank Corporation, stylized as IBERIABANK, is an American financial holding company headquartered in Lafayette, LA and the largest bank based in Louisiana.
- `d7s1` IberiaBank [1]: Founded in 1887, it now has over 250 combined offices in 10 states primarily throughout the South.
- `d7s2` IberiaBank [2]: The company has eight locations with representatives of IBERIA Wealth Advisors in four states, and one IBERIA Capital Partners, L.L.C. office in New Orleans.
- `d8s0` General Mediterranean Holding [0]: The General Mediterranean Holding (GMH) is a financial holding company established in 1979 in Luxembourg City, in southern Luxembourg, founded by Anglo-Iraqi businessman Nadhmi Auchi.
- `d9s0` Nelson Chai [0]: Nelson Joosuk Chai (born 1965) is an American investment banker and financial executive.
- `d9s1` Nelson Chai [1]: He formerly served as the chief financial officer of American financial services company Merrill Lynch and briefly as Bank of America's president for the Asia-Pacific region.
- `d9s2` Nelson Chai [2]: He is the former president of CIT Group and reported directly to then CEO John Thain.
- `d10s0` The Bank of New York Mellon [0]: The Bank of New York Mellon Corporation, which does business as BNY Mellon, is an American worldwide banking and financial services holding company headquartered in New York City.
- `d10s1` The Bank of New York Mellon [1]: It was formed on July 1, 2007, as a result of the merger of The Bank of New York and Mellon Financial Corporation.
- `d10s2` The Bank of New York Mellon [2]: The merger made the company one of the world's largest custodian banks and asset servicing companies.

</details>

## Q228 — `hotpotqa_5ab5b6c1554299637185c5e5` (revised draft)

> Did Franki Valli sing with Hellogoodbye or The Four Seasons?

Source answer: The Four Seasons

Gold final answer: The Four Seasons

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: whether Frankie Valli sang with Hellogoodbye | false | no | — | `[]`：无直接支持 | — |
| u2: whether Frankie Valli sang with The Four Seasons | false | yes | — | [d4s3] | — |
| u3: Did Franki Valli sing with Hellogoodbye or The Four Seasons? | true | The Four Seasons **[by_presupposition]** | u1, u2 | `[[]]`：由全部依赖推出 | [d4s3] |

Evidence:

- `d4s3` The Four Seasons (band) [3]: In 1960, the group known as the Four Lovers evolved into the Four Seasons, with Frankie Valli as the lead singer, Bob Gaudio (formerly of the Royal Teens) on keyboards and tenor vocals, Tommy DeVito on lead guitar and baritone vocals, and Nick Massi on electric bass and bass vocals.

Notes:

- 补两候选结构。另一乐队的创办者信息不能证明Valli从未加入，关系属性不按遗漏排除；仅启用Four Seasons确认链路。

<details><summary>All source context</summary>

- `d1s0` Roy Roman [0]: Roy Roman is a high note trumpet player who has performed lead with Lionel Hampton, the Benny Goodman Orchestra, Count Basie, Duke Ellington, Bob Hope, Sammy Davis, Jr. and Franki Valli, among others.
- `d1s1` Roy Roman [1]: Roman began playing the trumpet at age 19.
- `d1s2` Roy Roman [2]: After an injury to one of his front teeth, he was introduced to Roy Stevens, the teacher of a scientific method of embouchure development pioneered by William Costello.
- `d1s3` Roy Roman [3]: Today, Roman is the world's leading expert on the Stevens/Costello Method, a technique that allows the player to increase range, endurance and control.
- `d2s0` Can't Take My Eyes Off You [0]: "Can't Take My Eyes Off You" is a 1967 single credited to Frankie Valli.
- `d2s1` Can't Take My Eyes Off You [1]: The song was among his biggest hits, earning a gold record and reaching No. 2 on the "Billboard" Hot 100 for a week, stuck behind "Windy" by The Association.
- `d2s2` Can't Take My Eyes Off You [2]: It was co-written by Bob Gaudio, a bandmate of Valli's in The Four Seasons.
- `d2s3` Can't Take My Eyes Off You [3]: It was Valli's biggest solo hit until he hit #1 in 1974 with "My Eyes Adored You".
- `d3s0` Valli (album) [0]: Valli was the sixth solo LP album by Frankie Valli of The Four Seasons, released by Private Stock under catalog number PS-2017 as a stereo recording in 1976.
- `d3s1` Valli (album) [1]: It was reissued on compact disc in 2008, paired with his first solo effort from Private Stock, "Close Up", by Collector's Choice.
- `d4s0` The Four Seasons (band) [0]: The Four Seasons is an American rock and pop band that became internationally successful in the 1960s and 1970s.
- `d4s1` The Four Seasons (band) [1]: The Vocal Group Hall of Fame has stated that the group was the most popular rock band before the Beatles.
- `d4s2` The Four Seasons (band) [2]: Since 1970, they have also been known at times as Frankie Valli and the Four Seasons.
- `d4s3` The Four Seasons (band) [3]: In 1960, the group known as the Four Lovers evolved into the Four Seasons, with Frankie Valli as the lead singer, Bob Gaudio (formerly of the Royal Teens) on keyboards and tenor vocals, Tommy DeVito on lead guitar and baritone vocals, and Nick Massi on electric bass and bass vocals.
- `d5s0` Bobby Fox [0]: Bobby Fox is an Irish born Australian actor who originated the role of Franki Valli in the Australian production of "Jersey Boys".
- `d5s1` Bobby Fox [1]: He is a former 4 times World Irish Dance Champion and toured with dance productions "Riverdance", "Dancing on Dangerous Ground" (principal understudy), "To Dance on the Moon" (principal dancer) and starred in the revival of Australian musical "Hot Shoe Shuffle" as Spring.
- `d5s2` Bobby Fox [2]: Fox has also had roles in "Ladies in Black", "Blood Brothers", "Mamma Mia!
- `d5s3` Bobby Fox [3]: ", "Leader of the Pack", "Dusty – The Original Pop Diva", "We Will Rock You", "Spamalot" and The Production Company’s "Sweet Charity" and "Damn Yankees".
- `d6s0` Dean Valli [0]: Dean Valli (born October 5, 1983 in North Vancouver, British Columbia) is an offensive lineman with the Canadian Football League's British Columbia Lions.
- `d6s1` Dean Valli [1]: Valli attended Simon Fraser University and played for their football team, the Simon Fraser Clan.
- `d6s2` Dean Valli [2]: He played four full seasons with the Clan from 2002 to 2005.
- `d6s3` Dean Valli [3]: Dean graduated with a bachelor of arts from Simon Fraser University in 2006.
- `d6s4` Dean Valli [4]: In 2005, Valli was named to the Canada West Universities Athletic Association all-star team.
- `d6s5` Dean Valli [5]: He also represented SFU at the 2005 East West Bowl held in Waterloo, Ontario.
- `d6s6` Dean Valli [6]: Valli was selected in the 1st round, 6th overall, by the Lions in the 2006 CFL draft.
- `d6s7` Dean Valli [7]: 2006 was his first year playing professional football.
- `d7s0` Jersey Boys: Original Broadway Cast Recording [0]: Jersey Boys: Original Broadway Cast Recording is the Grammy-winning cast album for the Broadway musical "Jersey Boys", the story of Frankie Valli and The Four Seasons.
- `d7s1` Jersey Boys: Original Broadway Cast Recording [1]: The album was produced by original Four Season, Bob Gaudio.
- `d7s2` Jersey Boys: Original Broadway Cast Recording [2]: Principal vocals include Christian Hoff as "Tommy DeVito," Daniel Reichard as "Bob Gaudio," J. Robert Spencer as "Nick Massi" and John Lloyd Young as lead-singer "Frankie Valli."
- `d7s3` Jersey Boys: Original Broadway Cast Recording [3]: It was released November 1, 2005 by Rhino Entertainment and reached number eighty-five on the "Billboard" 200.
- `d7s4` Jersey Boys: Original Broadway Cast Recording [4]: In February 2008, the album was certified Gold by the RIAA.
- `d7s5` Jersey Boys: Original Broadway Cast Recording [5]: As of December 2014, the album has sold 1.4 million copies in the US.
- `d8s0` Hellogoodbye [0]: Hellogoodbye (sometimes styled as hellogoodbye) is a pop rock band that was formed in Huntington Beach, California in 2001 by singer Forrest Kline.
- `d8s1` Hellogoodbye [1]: They were signed to Drive-Thru Records and released their first full-length album "Zombies!
- `d8s2` Hellogoodbye [2]: Aliens!
- `d8s3` Hellogoodbye [3]: Vampires!
- `d8s4` Hellogoodbye [4]: Dinosaurs!
- `d8s5` Hellogoodbye [5]: " in 2006, in addition to their previously released EP "Hellogoodbye" and DVD "OMG HGB DVD ROTFL".
- `d8s6` Hellogoodbye [6]: In 2010, the band released "Would It Kill You?
- `d8s7` Hellogoodbye [7]: " on their label Wasted Summer Records.
- `d8s8` Hellogoodbye [8]: The album was released in the United Kingdom and Europe by LAB Records on the 14 March 2011.
- `d8s9` Hellogoodbye [9]: Hellogoodbye released their third album, Everything is Debatable, on October 29, 2013, while touring as the opening act for Paramore's The Self-Titled Tour.
- `d9s0` My Eyes Adored You [0]: "My Eyes Adored You" is a 1974 song written by Bob Crewe and Kenny Nolan.
- `d9s1` My Eyes Adored You [1]: It was originally recorded by The Four Seasons in early 1974.
- `d9s2` My Eyes Adored You [2]: After the Motown label balked at the idea of releasing it, the recording was sold to lead singer Frankie Valli for $4000.
- `d9s3` My Eyes Adored You [3]: After rejections by Capitol and Atlantic Records, Valli succeeded in getting the recording released on Private Stock Records, but the owner/founder of the label wanted only Valli's name on the label.
- `d9s4` My Eyes Adored You [4]: The single was released in the US in November 1974 and topped the "Billboard" Hot 100 in March 1975.
- `d9s5` My Eyes Adored You [5]: "My Eyes Adored You" also went to number 2 on the Easy Listening chart.
- `d9s6` My Eyes Adored You [6]: "Billboard" ranked it as the No. 5 song for 1975.
- `d10s0` The Wonder Who? [0]: The Wonder Who?
- `d10s1` The Wonder Who? [1]: was a "nom de disque" of The Four Seasons for four single records released from 1965 to 1967.
- `d10s2` The Wonder Who? [2]: It was one of a handful of "names" used by the group at that time, including Frankie Valli (as a "solo" artist even though the Four Seasons were present on the record) and The Valli Boys.
- `d10s3` The Wonder Who? [3]: Wonder Who?
- `d10s4` The Wonder Who? [4]: recordings generally feature the falsetto singing by Valli, but with a softer falsetto than on "typical" Four Seasons recordings.

</details>

## Q229 — `hotpotqa_5ab5e13c5542992aa134a3bf` (revised draft)

> What type of musician does Beau Bokan and Jason Scheff have in common?

Source answer: singer

Gold final answer: singer

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: musician roles of Beau Bokan | false | musician, singer | — | [d5s0] | — |
| u2: musician roles of Jason Scheff | false | bassist, singer, songwriter | — | [d2s0] | — |
| u3: What type of musician does Beau Bokan and Jason Scheff have in common? | true | singer | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d2s0` Jason Scheff [0]: Jason Randolph Scheff (born April 16, 1962, in San Diego) is an American bassist, singer, and songwriter.
- `d5s0` Beau Bokan [0]: Beau Mark Bokan (born November 30, 1981) is an American musician and singer.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` His Last Walk [0]: His Last Walk is the debut full-length album by American post-hardcore band Blessthefall, released April 10, 2007.
- `d1s1` His Last Walk [1]: It is the only release by the band to feature original vocalist, Craig Mabbitt, who would later be replaced by Beau Bokan.
- `d1s2` His Last Walk [2]: The album was released before Blessthefall started to play on the Taste of Chaos tour.
- `d1s3` His Last Walk [3]: Four singles were released for the album: "Higinia", "Guys Like You Make Us Look Bad", "A Message to the Unknown", and "Rise Up."
- `d1s4` His Last Walk [4]: The last song, "His Last Walk", features a bonus song (at the end of the same track) called "Purple Dog", which is a joke song made by the band members in which all members sing the song and clap their hands.
- `d2s0` Jason Scheff [0]: Jason Randolph Scheff (born April 16, 1962, in San Diego) is an American bassist, singer, and songwriter.
- `d2s1` Jason Scheff [1]: From 1985 to 2016 he was the bassist and singer for the veteran pop-rock band Chicago.
- `d3s0` Hollow Bodies [0]: Hollow Bodies is the fourth studio album by American metalcore band Blessthefall.
- `d3s1` Hollow Bodies [1]: It was released on August 20, 2013 through Fearless Records and produced by Joey Sturgis.
- `d3s2` Hollow Bodies [2]: It is the third album to include lead singer Beau Bokan, second album to include rhythm guitarist, Elliott Gruenberg and the first to include the same members in consecutive albums.
- `d4s0` Blessthefall [0]: Blessthefall (stylized as blessthefall or BLESSTHEFALL prior to 2013) is an American metalcore band from Scottsdale, Arizona, signed to Fearless Records.
- `d4s1` Blessthefall [1]: The band was founded in 2004 by guitarist Mike Frisby, drummer Matt Traynor, and bassist Jared Warth.
- `d4s2` Blessthefall [2]: Their debut album, "His Last Walk", with original vocalist Craig Mabbitt, was released April 10, 2007.
- `d4s3` Blessthefall [3]: Their second studio album, "Witness", with current vocalist Beau Bokan, was released October 6, 2009.
- `d4s4` Blessthefall [4]: Their third studio album, "Awakening", was released on October 4, 2011.
- `d4s5` Blessthefall [5]: Their fourth studio album, "Hollow Bodies", was released on August 20, 2013. "
- `d4s6` Blessthefall [6]: To Those Left Behind" is the band's fifth full-length album, released on September 18, 2015.
- `d5s0` Beau Bokan [0]: Beau Mark Bokan (born November 30, 1981) is an American musician and singer.
- `d5s1` Beau Bokan [1]: He is best known as the lead vocalist and keyboardist of Blessthefall, and the former vocalist of Take the Crown.
- `d5s2` Beau Bokan [2]: Bokan runs his own clothing line titled "Golden Hearts Shine Forever" which was launched in March 2011.
- `d5s3` Beau Bokan [3]: Bokan is Roman Catholic.
- `d6s0` Chauncy (album) [0]: Chauncy is the 1996 debut solo album by singer/songwriter/bassist Jason Scheff.
- `d6s1` Chauncy (album) [1]: Scheff is probably best known as a member of the band Chicago, where he has been the bassist and a lead singer since 1985.
- `d6s2` Chauncy (album) [2]: It also featured the only officially available recording of his 1993 co-composition "Mah Jongg" prior to the release of the original Chicago recording in 2008.
- `d7s0` What Kind of Man Would I Be? [0]: "What Kind of Man Would I Be?"
- `d7s1` What Kind of Man Would I Be? [1]: is a song written by Jason Scheff, Chas Sandford and Bobby Caldwell and recorded by the band Chicago for their 1988 album "Chicago 19" and 1989 album "Greatest Hits 1982–1989".
- `d7s2` What Kind of Man Would I Be? [2]: Scheff sang the lead vocals.
- `d8s0` Awakening (Blessthefall album) [0]: Awakening is the third full-length studio album by Blessthefall.
- `d8s1` Awakening (Blessthefall album) [1]: It was released on October 4, 2011, through Fearless Records.
- `d8s2` Awakening (Blessthefall album) [2]: It is the band's second album with singer Beau Bokan and first album with rhythm guitarist Elliott Gruenberg after the departure of Mike Frisby.
- `d8s3` Awakening (Blessthefall album) [3]: The album was produced by Michael "Elvis" Baskette, producer of the second album, "Witness".
- `d8s4` Awakening (Blessthefall album) [4]: On September 12, the song "40 Days..." was released on the IGN site.
- `d8s5` Awakening (Blessthefall album) [5]: It debuted at No. 32 on the "Billboard" 200, selling over 11,290 copies in its first week.
- `d8s6` Awakening (Blessthefall album) [6]: In Canada, the album debuted at No. 88 on the Canadian Albums Chart.
- `d8s7` Awakening (Blessthefall album) [7]: Like "Witness", the album features a few songs "without" harsh screaming or death growls.
- `d9s0` Take the Crown (band) [0]: Take the Crown was a post-hardcore band from Huntington Beach, California.
- `d9s1` Take the Crown (band) [1]: The original lineup included vocalist Beau Bokan, guitarist Nick Coffey, guitarist Tony Gonzalez, bassist James Campbell, and keyboardist Ryan Wilson.
- `d9s2` Take the Crown (band) [2]: The band began recording demos in 2004 with friend Chris Sorenson of Saosin; he would later produce their self-released debut EP, "Let the Games Begin", in 2006.
- `d9s3` Take the Crown (band) [3]: The band signed to Rise in 2007 and released their follow up full-length album, "Relapse React", May 13, 2008.
- `d9s4` Take the Crown (band) [4]: They announced their disbandment on September 25, 2008, which was due to the departure of James Campbell and Tony Gonzalez, lack of management, and financial burdens.
- `d10s0` Witness (Blessthefall album) [0]: Witness is the second full-length studio album by Blessthefall.
- `d10s1` Witness (Blessthefall album) [1]: It was released on October 6, 2009, through Fearless Records.
- `d10s2` Witness (Blessthefall album) [2]: It is the band's first album with Beau Bokan on lead vocals and final album with original guitarist Mike Frisby.
- `d10s3` Witness (Blessthefall album) [3]: The album was co-produced with There for Tomorrow drummer, Christopher Kamrada.
- `d10s4` Witness (Blessthefall album) [4]: This album includes a post-metal entrance, 2.0, and some songs without any screams or death growls.

</details>

## Q230 — `hotpotqa_5ab64cfa55429953192ad2b7` (revised draft)

> Who lived longer Ellen Glasgow or N. Scott Momaday ?

Source answer: N. Scott Momaday

Gold final answer: N. Scott Momaday

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: lifespan of Ellen Glasgow | false | 22 April 1873 to 21 November 1945 | — | [d6s0] | — |
| u2: completed lifespan or dated living-age bound of N. Scott Momaday | false | born 27 February 1934; alive in 2007 under the accepted award-based bound | — | [d3s0, d3s3] | — |
| u3: Who lived longer Ellen Glasgow or N. Scott Momaday ? | true | N. Scott Momaday | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d3s0` N. Scott Momaday [0]: Navarre Scott Momaday (born February 27, 1934) — known as N. Scott Momaday — is a Kiowa novelist, short story writer, essayist, and poet.
- `d3s3` N. Scott Momaday [3]: Momaday received the National Medal of Arts in 2007 for his work's celebration and preservation of indigenous oral and art tradition.
- `d6s0` Ellen Glasgow [0]: Ellen Anderson Gholson Glasgow (April 22, 1873 – November 21, 1945) was an American novelist who portrayed the changing world of the contemporary South.

Notes:

- 补d3s0+d3s3。按用户接受的获奖年龄下界，2007年最早也已72年10个月，超过Glasgow约72年7个月，u3可比较；不使用今天日期。
- 本题局部约定：按用户明确认可，将2007年获奖记载视为在世年龄下界；这是本题获准的推断，不宣称来源明确写出寿命或普遍证明奖项只能颁给在世者。

<details><summary>All source context</summary>

- `d1s0` Ari Berk [0]: Ari Berk is an American writer, folklorist, artist, and scholar of literature, iconography, and comparative myth.
- `d1s1` Ari Berk [1]: Berk holds degrees in Ancient History (B.A.), American Indian Studies (M.A.), and Comparative Literature and Culture (Ph.D.) from Humboldt State University and University of Arizona respectively.
- `d1s2` Ari Berk [2]: His dissertation was directed by Pulitzer Prize winner N. Scott Momaday and Berk was appointed to the committee that developed the first American Indian Studies doctoral program in the United States.
- `d2s0` The Way to Rainy Mountain [0]: The Way to Rainy Mountain (1969) is a book by Pulitzer Prize winning author N. Scott Momaday.
- `d2s1` The Way to Rainy Mountain [1]: It is about the journey of Momaday's Kiowa ancestors from their ancient beginnings in the Montana area to their final war and surrender to the United States Cavalry at Fort Sill, and subsequent resettlement near Rainy Mountain, Oklahoma.
- `d3s0` N. Scott Momaday [0]: Navarre Scott Momaday (born February 27, 1934) — known as N. Scott Momaday — is a Kiowa novelist, short story writer, essayist, and poet.
- `d3s1` N. Scott Momaday [1]: His novel "House Made of Dawn" was awarded the Pulitzer Prize for Fiction in 1969, and is considered the first major work of the Native American Renaissance.
- `d3s2` N. Scott Momaday [2]: His follow-up work "The Way to Rainy Mountain" blended folklore with memoir.
- `d3s3` N. Scott Momaday [3]: Momaday received the National Medal of Arts in 2007 for his work's celebration and preservation of indigenous oral and art tradition.
- `d3s4` N. Scott Momaday [4]: He holds twenty honorary degrees from colleges and universities, and is a fellow of the American Academy of Arts and Sciences.
- `d4s0` House Made of Dawn [0]: House Made of Dawn is a 1968 novel by N. Scott Momaday, widely credited as leading the way for the breakthrough of Native American literature into the mainstream.
- `d4s1` House Made of Dawn [1]: It was awarded the Pulitzer Prize for Fiction in 1969, and has also been noted for its significance in Native American Anthropology.
- `d5s0` Ellen Glasgow House [0]: The Ellen Glasgow House, also known as the Branch-Glascow House, is a historic house at 1 West Main Street in Richmond, Virginia.
- `d5s1` Ellen Glasgow House [1]: Built in 1841, it is nationally significant as the home of writer Ellen Glasgow (1873-1945) from 1887 until her death.
- `d5s2` Ellen Glasgow House [2]: It was declared a National Historic Landmark in 1971.
- `d6s0` Ellen Glasgow [0]: Ellen Anderson Gholson Glasgow (April 22, 1873 – November 21, 1945) was an American novelist who portrayed the changing world of the contemporary South.
- `d7s0` The Shadowy Third and Other Stories [0]: The Shadowy Third and Other Stories is a 1923 short story collection by Ellen Glasgow.
- `d7s1` The Shadowy Third and Other Stories [1]: Glasgow published only this one short story collection during her lifetime, which included seven stories.
- `d7s2` The Shadowy Third and Other Stories [2]: While Glasgow's novels receive more critical attention, scholarship on her stories continues into the twenty-first century.
- `d8s0` Virginia (novel) [0]: Virginia (1913) is a novel by Ellen Glasgow about a wife and mother who in vain seeks happiness by serving her family.
- `d8s1` Virginia (novel) [1]: This novel, her eleventh, marked a clear departure from Glasgow's previous work—she had written a series of bestsellers before publishing "Virginia"—in that it attacked, in a subtle yet unmistakable way, the very layer of society that constituted her readership.
- `d8s2` Virginia (novel) [2]: Also, as its heroine, though virtuous and god-fearing, is denied the happiness she is craving, its plot did not live up to readers' expectations as far as poetic justice is concerned and was bound to upset some of them.
- `d8s3` Virginia (novel) [3]: Today, "Virginia" is seen by many as an outstanding achievement in Glasgow's career, exactly because the author defied literary convention by questioning the foundations of American society around the dawn of the 20th century, be it capitalism, religion or racism.
- `d9s0` Robert Weil (editor) [0]: Robert Weil is the Editor-in-Chief and Publishing Director of Liveright, a newly relaunched division of W.W. Norton & Company.
- `d9s1` Robert Weil (editor) [1]: Over the course of his career, “Weil has published six National Book Award winners and three National Book Award finalists.
- `d9s2` Robert Weil (editor) [2]: He's published sixteen Pulitzer Prize winners (Michael Dirda, N. Scott Momaday, and Tina Rosenberg among them); seven Bancroft history prize winners; [and] seven MacArthur fellowship winners.”
- `d10s0` Native American Renaissance [0]: The Native American Renaissance is a term originally coined by critic Kenneth Lincoln in the 1983 book "Native American Renaissance" to categorise the significant increase in production of literary works by Native Americans in the United States in the late 1960s and onwards.
- `d10s1` Native American Renaissance [1]: A. Robert Lee and Alan Velie note that the book's title "quickly gained currency as a term to describe the efflorescence on literary works that followed the publication of N. Scott Momaday's "House Made of Dawn" in 1968".
- `d10s2` Native American Renaissance [2]: Momaday's novel garnered critical acclaim, including the Pulitzer Prize for Fiction in 1969.

</details>

## Q231 — `hotpotqa_5ab672165542995eadeeffe0` (revised draft)

> Which genus has more species, Azorina or Azadirachta?

Source answer: Azadirachta

Gold final answer: Azadirachta

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: species count of Azorina | false | 1 | — | [d1s0] | — |
| u2: species count of Azadirachta | false | 2 | — | [d3s0] OR [d2s1] OR [d3s1] | — |
| u3: Which genus has more species, Azorina or Azadirachta? | true | Azadirachta | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d1s0` Azorina [0]: Azorina is a monotypic genus of flowering plants within the family Campanulaceae, whose sole species, the Azorina vidalii, is endemic to the Azores.
- `d2s1` Azadirachta indica [1]: It is one of two species in the genus "Azadirachta", and is native to the Indian subcontinent, i.e. India, Nepal, Pakistan, Bangladesh, Sri Lanka, and Maldives.
- `d3s0` Azadirachta [0]: Azadirachta is a genus of two species of trees in the mahogany (Meliaceae) family.
- `d3s1` Azadirachta [1]: Numerous species have been proposed for the genus but only two are currently recognized, "Azadirachta excelsa" and the economically important tree "Azadirachta indica".

Notes:

- 补两个明确two species的备选证据。

<details><summary>All source context</summary>

- `d1s0` Azorina [0]: Azorina is a monotypic genus of flowering plants within the family Campanulaceae, whose sole species, the Azorina vidalii, is endemic to the Azores.
- `d1s1` Azorina [1]: Its fragmented population is made up of fewer than 1000 mature plants limited to the coastlines of several of the islands.
- `d2s0` Azadirachta indica [0]: Azadirachta indica (commonly known as neem, nimtree and Indian lilac) is a tree in the mahogany family Meliaceae.
- `d2s1` Azadirachta indica [1]: It is one of two species in the genus "Azadirachta", and is native to the Indian subcontinent, i.e. India, Nepal, Pakistan, Bangladesh, Sri Lanka, and Maldives.
- `d2s2` Azadirachta indica [2]: It typically is grown in tropical and semi-tropical regions.
- `d2s3` Azadirachta indica [3]: Neem trees now also grow in islands located in the southern part of Iran.
- `d2s4` Azadirachta indica [4]: Its fruits and seeds are the source of neem oil.
- `d3s0` Azadirachta [0]: Azadirachta is a genus of two species of trees in the mahogany (Meliaceae) family.
- `d3s1` Azadirachta [1]: Numerous species have been proposed for the genus but only two are currently recognized, "Azadirachta excelsa" and the economically important tree "Azadirachta indica".
- `d3s2` Azadirachta [2]: The latter is informally called the Neem tree; see also Neem oil.
- `d3s3` Azadirachta [3]: Both species are native to the Indomalaysian region, and "A. indica" is also widely cultivated and naturalized outside its native range.

</details>

## Q232 — `hotpotqa_5ab67c0055429954757d32f6` (revised draft)

> What author wrote a three-book memoir series whose books include works studied in school systems around the world?

Source answer: Homer Hickam, Jr.

Gold final answer: Homer Hickam, Jr.

Question type: `single` (source type `bridge`)

Original question: What author wrote a three book series of memoirs that are studied in school systems around the world?

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: What author wrote a three-book memoir series whose books include works studied in school systems around the world? | true | Homer Hickam, Jr. | — | [d10s0, d10s3] OR [d9s0, d9s3] | — |

Evidence:

- `d9s0` October Sky (novel) [0]: October Sky (originally published as Rocket Boys) is the first memoir in a series of three, by Homer Hickam, Jr. It is a story of growing up in a mining town, and a boy's pursuit of amateur rocketry in a coal mining town.
- `d9s3` October Sky (novel) [3]: It is also studied in many school systems around the world.
- `d10s0` The Coalwood Way [0]: The Coalwood Way (2000) is the second memoir in a series of three, by Homer Hickam, Jr. "The Coalwood Way" is a story of the Rocket Boys and Coalwood.
- `d10s3` The Coalwood Way [3]: It is also studied in many school systems around the world.

Notes:

- 题干澄清：限定系列中有作品被学校采用，不把个别作品的教学使用扩大为全部三本。

<details><summary>All source context</summary>

- `d1s0` The Mahabharata Quest: The Alexander Secret [0]: The Mahabharata Quest: The Alexander Secret is the second novel by Indian author Christopher C. Doyle and was released on 9 October 2014 by Westland Publishers.
- `d1s1` The Mahabharata Quest: The Alexander Secret [1]: The story follows Vijay and his friends as they embark on a quest to learn about Alexander the Great's secret mission in India while encountering bioterrorism.
- `d1s2` The Mahabharata Quest: The Alexander Secret [2]: Following his first novel, "The Mahabharata Secret", Doyle was signed for a three book series by Westland.
- `d1s3` The Mahabharata Quest: The Alexander Secret [3]: The author researched further on the "Mahabharata" and was also intrigued by Alexander's invasion of India and his sudden retreat.
- `d1s4` The Mahabharata Quest: The Alexander Secret [4]: Doyle combined secrets from the epic and created the story, stating that he consulted Sanskrit scholars and science experts regarding the theories he put in the book.
- `d1s5` The Mahabharata Quest: The Alexander Secret [5]: "The Mahabharata Quest: The Alexander Secret" was a commercial success and received positive critical reviews, which praised the storytelling and the theme.
- `d2s0` Yoshiki Tonogai [0]: Yoshiki Tonogai (外海良基 , Tonogai Yoshiki , born March 14) is a Japanese manga artist from Shiga, Japan.
- `d2s1` Yoshiki Tonogai [1]: He is notable as the illustrator of one of the "Higurashi When They Cry" manga adaptations: "Himatsubushi-hen", or Time Killing Arc.
- `d2s2` Yoshiki Tonogai [2]: He is also the artist and writer of "Doubt", which was completed in February 2009.
- `d2s3` Yoshiki Tonogai [3]: He followed up the "Doubt" series with two spiritual sequels, "Judge" and "Secret", all connected by the recurring appearance of the iconic Rabbit mask from "Doubt".
- `d2s4` Yoshiki Tonogai [4]: "Doubt" has been published in the US by Yen Press in its entirety in 2 volumes in April and July 2013, and the entire six book series of "Judge" and the three book series of "Secret" have been published by them as well.
- `d2s5` Yoshiki Tonogai [5]: They have also been published in various countries in Europe.
- `d3s0` One for the Morning Glory [0]: One For the Morning Glory is a fantasy novel by John Barnes, published 1996.
- `d3s1` One for the Morning Glory [1]: It is a fairy tale where the characters know that they are in a fairy tale.
- `d3s2` One for the Morning Glory [2]: The novel has a humorous tone similar to William Goldman's "The Princess Bride" — quite different from Barnes' usual science fiction.
- `d3s3` One for the Morning Glory [3]: It forms the second part of a three book series whose first and third parts are not yet written.
- `d4s0` The Catawbans (book series) [0]: The Catawbans is a series of three books by Gary Freeze on the history and genealogy of Catawba County in North Carolina.
- `d4s1` The Catawbans (book series) [1]: Freeze, a professor at Catawba College in Salisbury, was commissioned by the county to write its official history, and his three book series is the result of over twenty years of work on the project.
- `d4s2` The Catawbans (book series) [2]: The series includes the following three books:
- `d5s0` Bobbie Banda [0]: Barbara "Bobbie" Lucille Banda (c. 1947 – May 4, 2013) was an American Juaneño tribal elder, activist, and a member of the Juaneño Band of Mission Indians.
- `d5s1` Bobbie Banda [1]: Banda successfully championed efforts to introduction Native American curriculum, including Juaneño language courses, into the public school systems around San Juan Capistrano, California, during the 1970s.
- `d5s2` Bobbie Banda [2]: The curriculum is still taught in California public schools today.
- `d6s0` The Sea Beggars [0]: The Sea Beggars is an incomplete book series by Paul Kearney.
- `d6s1` The Sea Beggars [1]: It began with "The Mark of Ran" (2004) and tells the story of Rol Cortishane.
- `d6s2` The Sea Beggars [2]: It is based almost entirely around ocean-based adventures.
- `d6s3` The Sea Beggars [3]: A second volume, "This Forsaken Earth" (original working title "The Stars We Sail By") was published in July 2006.
- `d6s4` The Sea Beggars [4]: The series was expected to be four books long and the third had nearly been completed when the series was unexpectedly dropped by Bantam in May 2007.
- `d6s5` The Sea Beggars [5]: After signing a new contract with Solaris, Paul announced this would now be a three book series and that the last book in the series was due to be published as an omnibus in Autumn 2012.
- `d6s6` The Sea Beggars [6]: However, due to the US publishers never releasing the rights for the final book, this remains unpublished.
- `d7s0` Fire Study [0]: Fire Study is a 2008 fantasy novel written by Maria V. Snyder.
- `d7s1` Fire Study [1]: "Fire Study" is the third and final book in a three book series.
- `d8s0` Great American Bathroom Book [0]: The Great American Bathroom Book is the name of a three book series - Vol.
- `d8s1` Great American Bathroom Book [1]: 1, Vol.
- `d8s2` Great American Bathroom Book [2]: 2 and Vol.
- `d8s3` Great American Bathroom Book [3]: 3, published in 1992, 1993 and 1994, respectively.
- `d8s4` Great American Bathroom Book [4]: The books were published by Compact Classics, a small US publishing house.
- `d9s0` October Sky (novel) [0]: October Sky (originally published as Rocket Boys) is the first memoir in a series of three, by Homer Hickam, Jr. It is a story of growing up in a mining town, and a boy's pursuit of amateur rocketry in a coal mining town.
- `d9s1` October Sky (novel) [1]: It won the W.D. Weatherford Award in 1998, the year of its release.
- `d9s2` October Sky (novel) [2]: Today, it is one of the most often picked community/library reads in the United States.
- `d9s3` October Sky (novel) [3]: It is also studied in many school systems around the world.
- `d9s4` October Sky (novel) [4]: "October Sky" was followed by "The Coalwood Way" (2000) and "Sky of Stone" (2002).
- `d10s0` The Coalwood Way [0]: The Coalwood Way (2000) is the second memoir in a series of three, by Homer Hickam, Jr. "The Coalwood Way" is a story of the Rocket Boys and Coalwood.
- `d10s1` The Coalwood Way [1]: Homer calls it an "equal," rather than a sequel because the story happens during the same timeframe as the first book.
- `d10s2` The Coalwood Way [2]: Today, it is one of the most often picked community/library reads in the United States.
- `d10s3` The Coalwood Way [3]: It is also studied in many school systems around the world.
- `d10s4` The Coalwood Way [4]: The Coalwood Way (2000) is followed by "Sky of Stone" (2002), and preceded by "October Sky" (1998).

</details>

## Q233 — `hotpotqa_5ab6c47e55429954757d3368` (revised draft)

> Adam Fox was one of the first members of an informal literary discussion group associated with what University?

Source answer: University of Oxford, England

Gold final answer: University of Oxford, England

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: literary group Adam Fox joined as an early member | false | Inklings | — | [d7s1] | — |
| u2: university associated with {u1} | true | University of Oxford, England (accepted alternatives: University of Oxford; Oxford University) | u1 | [d1s0] | — |

Evidence:

- `d1s0` Inklings [0]: The Inklings was an informal literary discussion group associated with the University of Oxford, England, for nearly two decades between the early 1930s and late 1949.
- `d7s1` Adam Fox [1]: He was one of the first members of the "Inklings", a literary group which also included C.S. Lewis and J.R.R. Tolkien.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Inklings [0]: The Inklings was an informal literary discussion group associated with the University of Oxford, England, for nearly two decades between the early 1930s and late 1949.
- `d1s1` Inklings [1]: The Inklings were literary enthusiasts who praised the value of narrative in fiction and encouraged the writing of fantasy.
- `d2s0` Colin Hardie [0]: Colin Graham Hardie (16 February 1906 – 17 October 1998) was a British classicist and academic.
- `d2s1` Colin Hardie [1]: From 1933 to 1936, he was Director of the British School at Rome.
- `d2s2` Colin Hardie [2]: From 1936 to 1973, he was a Fellow of Magdalen College, Oxford, and a tutor in classics.
- `d2s3` Colin Hardie [3]: In addition, from 1967 to 1973, he was the Public Orator of the University of Oxford.
- `d2s4` Colin Hardie [4]: He was a member of the Inklings, an informal literary discussion group which included the likes of J. R. R. Tolkien and C. S. Lewis.
- `d3s0` Litbits [0]: Litbits is a literary discussion radio programme and podcast, hosted by academic Adam Smyth and literary journalist James Kidd.
- `d3s1` Litbits [1]: Guests on the programme have included Polly Russell, Paul Myerscough, Alex von Tunzelmann, Samantha Ellis, Jonathan Beckman, Hallie Rubenhold, Steve Rose, Joe Brooker, Dennis Duncan, Dinah Roe, Giles Milton and Liane Strauss.
- `d3s2` Litbits [2]: Subjects covered include Rooms and Procrastination.
- `d4s0` Eagle Street College [0]: The Eagle Street College was an informal literary society established in 1885 at the home of James William Wallace in Eagle Street, Bolton, to read and discuss literary works, particularly the poetry of Walt Whitman, (1819–91).
- `d4s1` Eagle Street College [1]: The group subsequently became known as the Bolton Whitman Fellowship or Whitmanites.
- `d4s2` Eagle Street College [2]: Its founder members were Wallace, Dr John Johnston and Fred Wild.
- `d4s3` Eagle Street College [3]: The group held an annual 'Whitman Day' celebration around the 31 May which was the poet's birthday.
- `d5s0` Petrashevsky Circle [0]: The Petrashevsky Circle was a Russian literary discussion group of progressive-minded commoner-intellectuals in St. Petersburg in the 1840s.
- `d5s1` Petrashevsky Circle [1]: It was organized by Mikhail Petrashevsky, a follower of the French utopian socialist Charles Fourier.
- `d5s2` Petrashevsky Circle [2]: Among the members were writers, teachers, students, minor government officials, and army officers.
- `d5s3` Petrashevsky Circle [3]: While differing in political views, most of them were opponents of the tsarist autocracy and Russian serfdom.
- `d5s4` Petrashevsky Circle [4]: Like that of the Lyubomudry group founded earlier in the century, the purpose of the circle was to discuss Western philosophy and literature that was officially banned by the Imperial government of Tsar Nicholas I.
- `d6s0` Charles Leslie Wrenn [0]: Charles Leslie Wrenn (1895–1969) was a British scholar.
- `d6s1` Charles Leslie Wrenn [1]: He became Rawlinson and Bosworth Professor of Anglo-Saxon at the University of Oxford in 1945, the successor in the chair of J.R.R. Tolkien, and held the position until 1963.
- `d6s2` Charles Leslie Wrenn [2]: Wrenn was a Fellow of Pembroke College, Oxford.
- `d6s3` Charles Leslie Wrenn [3]: He was also a member of the Oxford literary discussion group known as the "Inklings", which included C. S. Lewis and Tolkien.
- `d6s4` Charles Leslie Wrenn [4]: Some of the work published by Wrenn includes "The English Language" (1949), "A Study of Old English Literature" (1967)"," and "An Old English Grammar," written with Randolph Quirk (1955, rev. 1957).
- `d6s5` Charles Leslie Wrenn [5]: His literary interests were primarily comparative literature and later poets including T. S. Elliot.
- `d7s0` Adam Fox [0]: Adam Fox (1883 – 1977), Canon, was the Dean of Divinity at Magdalen College, Oxford.
- `d7s1` Adam Fox [1]: He was one of the first members of the "Inklings", a literary group which also included C.S. Lewis and J.R.R. Tolkien.
- `d7s2` Adam Fox [2]: Between 1938 and 1942 he was Professor of Poetry.
- `d7s3` Adam Fox [3]: Later he became Canon of Westminster Abbey and he is buried there in Poet's Corner.
- `d7s4` Adam Fox [4]: He was also Warden (Headmaster) of the famous Radley College.
- `d8s0` Nikolay Speshnev [0]: Nikolay Alexandrovich Speshnev (Russian: Николай Александрович Спе́шнев; 1821, Kursk - 1882, St. Petersburg) was a 19th-century Russian aristocrat and political activist, best known for his involvement with the pro-socialist literary discussion group the Petrashevsky Circle.
- `d8s1` Nikolay Speshnev [1]: He formed a secret revolutionary society from among the members of the circle, which included the young Fyodor Dostoevsky.
- `d8s2` Nikolay Speshnev [2]: After the government of Tsar Nicholas I arrested the members of the Petrashevsky Circle in 1849, Speshnev was interrogated, threatened with torture, and eventually sentenced, along with Dostoevsky, Petrashevsky and others, to execution by firing squad.
- `d8s3` Nikolay Speshnev [3]: The sentence was commuted to hard labour in Siberia, but the prisoners were only informed of this after enduring a mock execution.
- `d9s0` Roger Lancelyn Green [0]: Roger (Gilbert) Lancelyn Green (2 November 1918 – 8 October 1987) was a British biographer and children's writer.
- `d9s1` Roger Lancelyn Green [1]: He was an Oxford academic who formed part of the Inklings literary discussion group along with C. S. Lewis and J. R. R. Tolkien.
- `d10s0` Norma Guillard [0]: Norma Guillard Limonta is a Cuban social psychologist and adjunct lecturer at the University of Havana.
- `d10s1` Norma Guillard [1]: She is a co-founder of Grupo Oremi, a now defunct lesbian discussion group in Cuba.
- `d10s2` Norma Guillard [2]: Her academic works borders on gender, sexuality, race and identity.
- `d10s3` Norma Guillard [3]: Guillard is a foundation member of the Cuban branch of La Articulacion Regional de Afrodescendientes de Latinoamerica y el Caribe, a joint regional discussion group composed of individuals of African descent in Latin America and the Caribbean.

</details>

## Q234 — `hotpotqa_5ab7d12f55429928e1fe391f` (revised draft)

> Menindee Lakes are located near a town located on the banks of which river ?

Source answer: the Darling River

Gold final answer: the Darling River

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: town near Menindee Lakes | false | Menindee | — | [d6s1] | — |
| u2: river on whose banks {u1} lies | true | the Darling River (accepted alternatives: Darling River) | u1 | [d3s0] | — |

Evidence:

- `d3s0` Menindee, New South Wales [0]: Menindee, frequently but erroneously spelled "Menindie", is a small town in the far west of New South Wales, Australia, in Central Darling Shire, on the banks of the Darling River, with a sign-posted population of 980 and a 2011 census population of 449.
- `d6s1` Menindee Lakes [1]: The lakes lie in the far west region of New South Wales, Australia, near the town of Menindee.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Khowai [0]: Khowai is a town located in the Indian state of Tripura and a recent nagar panchayat forming into a Khowai Municipal Council in newly formed Khowai district in the Indian state of Tripura.
- `d1s1` Khowai [1]: The city lies on the banks of Khowai river and hence from the river the city gets its name.
- `d1s2` Khowai [2]: Located near the bangladesh border it has boundaries with it on its entire Southern part.
- `d2s0` Qayyarah [0]: Qayyarah or Qayara (Arabic: القيارة‎ ‎ ) is an Iraqi town located in southern Nineveh Governorate on the west bank of the Tigris river, and about 60 km (35 miles) south of Mosul.
- `d2s1` Qayyarah [1]: It is located in the Mosul District, and it is the seat of Qayyarah subdistrict.
- `d2s2` Qayyarah [2]: It has a population of 15,000.
- `d2s3` Qayyarah [3]: The town is located near the Qayyarah oil field and has an oil refinery on its south-western outskirts.
- `d2s4` Qayyarah [4]: The Qayyarah Airfield West is 20 kilometers west of the town.
- `d3s0` Menindee, New South Wales [0]: Menindee, frequently but erroneously spelled "Menindie", is a small town in the far west of New South Wales, Australia, in Central Darling Shire, on the banks of the Darling River, with a sign-posted population of 980 and a 2011 census population of 449.
- `d4s0` Boundary, Washington [0]: Boundary is a ghost town located in Stevens County, Washington, United States.
- `d4s1` Boundary, Washington [1]: The town was located near the Canada–US border and near the Columbia River.
- `d4s2` Boundary, Washington [2]: Boundary's peak years were during the 1890s.
- `d4s3` Boundary, Washington [3]: The population was around 900.
- `d4s4` Boundary, Washington [4]: The town started off as a railroad camp.
- `d4s5` Boundary, Washington [5]: When the railroad finally spanned the wild Pend Oreille with a bridge, the railroad workers quickly moved on leaving the town of Boundary deserted.
- `d4s6` Boundary, Washington [6]: The town contained the Boundary Hotel, post office, and general store.
- `d4s7` Boundary, Washington [7]: A town called "New Boundary" came into being south of the original townsite and the old town eventually vanished.
- `d5s0` Menindee County [0]: Menindee County is one of the 141 Cadastral divisions of New South Wales.
- `d5s1` Menindee County [1]: It is located between the Darling River and the South Australian border.
- `d5s2` Menindee County [2]: Menindee is at its north-eastern edge.
- `d5s3` Menindee County [3]: The Menindee Lakes are located there.
- `d6s0` Menindee Lakes [0]: The Menindee Lakes is a chain of shallow ephemeral freshwater lakes connected to the Darling River to form a storage system.
- `d6s1` Menindee Lakes [1]: The lakes lie in the far west region of New South Wales, Australia, near the town of Menindee.
- `d7s0` Gregory, Queensland [0]: Gregory is a small town located near the Gregory River in the Shire of Burke, Queensland, Australia.
- `d7s1` Gregory, Queensland [1]: The town had a population of 40 people in 2008 and is situated on the banks of the perennial Gregory River.
- `d7s2` Gregory, Queensland [2]: The Gregory River was named by explorer William Landsborough on 19 November 1861, after Augustus Charles Gregory explorer and first Surveyor General of Queensland.
- `d8s0` Volcanic City [0]: Volcanic City is a ghost town located in the Boundary Country region of British Columbia.
- `d8s1` Volcanic City [1]: It is located near the north fork of the Kettle River.
- `d8s2` Volcanic City [2]: A prospector named Volcanic Brown discovered an "iron cap" mountain near the north fork of the Kettle river.
- `d8s3` Volcanic City [3]: Volcanic Brown claimed the mountain was rich for mining.
- `d8s4` Volcanic City [4]: Brown tried to create a city in the vicinity of the mountain.
- `d8s5` Volcanic City [5]: He assumed miners would be attracted to the mountain and they would live in the city.
- `d9s0` Bridal Veil, Oregon [0]: Bridal Veil is a virtual ghost town located in Multnomah County, Oregon, United States.
- `d9s1` Bridal Veil, Oregon [1]: It was established in the 1880s during a logging boom by a logging company as it harvested timber on nearby Larch Mountain to be a company mill town around a sawmill.
- `d9s2` Bridal Veil, Oregon [2]: It had a close relationship with the logging town of Palmer for the first 50 years of its history.
- `d9s3` Bridal Veil, Oregon [3]: As of November 2011, all that remains of the town is a post office and a cemetery.
- `d9s4` Bridal Veil, Oregon [4]: The site is located near the west end of the Columbia River Gorge.
- `d10s0` Binnaway, New South Wales [0]: Binnaway is a small town located on the Castlereagh River in central western New South Wales near the larger centre of Coonabarabran, which is about 35 kilometres to the north.
- `d10s1` Binnaway, New South Wales [1]: In 2006, the town had a population of 495 people.
- `d10s2` Binnaway, New South Wales [2]: The road linking these two towns closely follows the meandering Castlereagh River.
- `d10s3` Binnaway, New South Wales [3]: There are many pleasant areas to stop beside the road and on the river banks to have a picnic.
- `d10s4` Binnaway, New South Wales [4]: Binnaway is also located near the similarly sized small town of Mendooran.
- `d10s5` Binnaway, New South Wales [5]: Following local government amalgamation, the town is now located in the Warrumbungle Shire Council area which is headquartered at Coonabarabran.

</details>

## Q235 — `hotpotqa_5ab7ece25542995dae37e9f3` (revised draft)

> Which four business areas are explicitly named for the company chaired by the wealthiest person in Georgia in the stated 2017 list?

Source answer: newspapers, television, radio, cable television

Gold final answer: newspapers, television, radio, cable television

Question type: `bridge` (source type `bridge`)

Original question: What 4 divisions make up the company of the wealthiest person in Georgia?

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: wealthiest person in Georgia in the stated 2017 list | false | James C. Kennedy | — | [d2s1] | — |
| u2: company chaired by {u1} | false | Cox Enterprises | u1 | [d2s0] | — |
| u3: four named business areas of {u2} | true | newspapers, television, radio, cable television | u2 | [d6s0] | — |

Evidence:

- `d2s0` James C. Kennedy [0]: James Cox Kennedy (born 1948) is an American media executive and the current chair of Cox Enterprises, the media conglomerate founded by his grandfather, James M. Cox.
- `d2s1` James C. Kennedy [1]: According to the Forbes billionaires list from 2017, he is the 105th richest person in the world, the thirty-seventh richest person in the United States, and the richest person in the state of Georgia, surpassing his aunt, Anne Cox Chambers, for the title.
- `d6s0` Anne Cox Chambers [0]: Anne Beau Cox Chambers (born December 1, 1919) is an American media proprietor, who has a stake of interest in Cox Enterprises, a privately held media empire that includes newspapers, television, radio, cable television, and other businesses.

Notes:

- 题干澄清：将four divisions改为four named business areas，并限定来源2017年榜单；不把other businesses删除。

<details><summary>All source context</summary>

- `d1s0` Richard DeVos [0]: Richard Marvin DeVos Sr. (born March 4, 1926) is an American businessman, co-founder of Amway along with Jay Van Andel (company restructured as Alticor in 2000), and owner of the Orlando Magic NBA basketball team.
- `d1s1` Richard DeVos [1]: In 2012, "Forbes" magazine listed him as the 60th wealthiest person in the United States, and the 205th richest in the world, with an estimated net worth of $5.1 billion.
- `d1s2` Richard DeVos [2]: At one point, he was one of the 10 wealthiest Americans.
- `d2s0` James C. Kennedy [0]: James Cox Kennedy (born 1948) is an American media executive and the current chair of Cox Enterprises, the media conglomerate founded by his grandfather, James M. Cox.
- `d2s1` James C. Kennedy [1]: According to the Forbes billionaires list from 2017, he is the 105th richest person in the world, the thirty-seventh richest person in the United States, and the richest person in the state of Georgia, surpassing his aunt, Anne Cox Chambers, for the title.
- `d2s2` James C. Kennedy [2]: He was featured in a Forbes article entitled "This Billionaire Knows The Secret To Saving A Family Business".
- `d3s0` Jean Coutu (pharmacist) [0]: Jean Coutu, {'1': ", '2': ", '3': ", '4': "} (born May 29, 1927) is a Canadian pharmacist and businessman.
- `d3s1` Jean Coutu (pharmacist) [1]: He is the founder and Chairman of the Jean Coutu Group which he started in 1969.
- `d3s2` Jean Coutu (pharmacist) [2]: With an estimated net worth of $US 1.6 billion (as of March 2012), Coutu was ranked by "Forbes" as the 22nd wealthiest Canadian and 938th wealthiest person in the world.
- `d4s0` Warren Buffett [0]: Warren Edward Buffett ( ; born August 30, 1930) is an American business magnate, investor, and philanthropist.
- `d4s1` Warren Buffett [1]: Buffett serves as the Chief Executive Officer and Chairman of Berkshire Hathaway.
- `d4s2` Warren Buffett [2]: He is considered by some to be one of the most successful investors in the world, and as of August 2017 is the second wealthiest person in the United States, and the fourth wealthiest in the world, with a total net worth of $76.9 billion.
- `d5s0` Nagpur division [0]: Nagpur Division is one of six administrative divisions of Maharashtra State in India.
- `d5s1` Nagpur division [1]: Nagpur is the most eastern division in the state, with an administrative headquarters in the city of Nagpur.
- `d5s2` Nagpur division [2]: It covers 51,336 km² (19,821 mi²).
- `d5s3` Nagpur division [3]: The Amravati and Nagpur divisions make up the region of Vidarbha.
- `d6s0` Anne Cox Chambers [0]: Anne Beau Cox Chambers (born December 1, 1919) is an American media proprietor, who has a stake of interest in Cox Enterprises, a privately held media empire that includes newspapers, television, radio, cable television, and other businesses.
- `d7s0` List of Catholic dioceses in Brazil [0]: The Catholic Church in Brazil comprises forty-four ecclesiastical provinces each headed by a Metropolitan archbishop.
- `d7s1` List of Catholic dioceses in Brazil [1]: The provinces are in turn subdivided into 215 dioceses (including 4 eparchies), 45 archdioceses and 12 territorial prelatures, each headed by a bishop or an archbishop.
- `d7s2` List of Catholic dioceses in Brazil [2]: These 272 divisions make the largest number of Catholic dioceses in any country.
- `d8s0` Middle office [0]: The middle office comprises departments of a financial services company that manage position-keeping (i.e. control representation of transactions within transaction-registering system of a company).
- `d8s1` Middle office [1]: These divisions make sure these transaction representations properly capture profit flows given the technological resources.
- `d8s2` Middle office [2]: The middle office is usually part of operations and finance divisions including product control, which normally is also in charge of settlement.
- `d8s3` Middle office [3]: It draws on the resources of both the front and the back offices. Due to their critical role, the middle office always acts in tandem with the front office work on open markets.
- `d8s4` Middle office [4]: Broadly speaking, middle office includes roles that affect either side (invest, finance, hedge, insure) of the balance sheet of the business.
- `d9s0` Iris Fontbona [0]: Iris Balbina Fontbona González (born 1942/1943) is a Chilean billionaire businesswoman, the widow of Andrónico Luksic Abaroa, from inheriting Antofagasta PLC.
- `d9s1` Iris Fontbona [1]: She is the wealthiest person in Chile, one of the fifth wealthiest in Latin America, and the 101st wealthiest person in the world.
- `d10s0` Paul Desmarais [0]: Paul Desmarais Sr., {'1': ", '2': ", '3': ", '4': "} (January 4, 1927 – October 8, 2013) was a Canadian financier and philanthropist, based in Montreal.
- `d10s1` Paul Desmarais [1]: With an estimated family net worth of US$ 4.5 billion (as of March 2011), Desmarais was ranked by "Forbes" as the fourth wealthiest person in Canada and 235th in the world in 2013.
- `d10s2` Paul Desmarais [2]: He was chairman and chief executive officer of Power Corporation of Canada until 1996 when he passed the reins of management of Power Corporation to his sons, Paul Jr. and André.
- `d10s3` Paul Desmarais [3]: He then continued to serve as a director and as chairman of the executive committee of the board, and remained the controlling shareholder.
- `d10s4` Paul Desmarais [4]: Power Corporation of Canada is a diversified international management and holding company with interests in companies in the financial services, renewable energy, communications and other business sectors.

</details>

## Q236 — `hotpotqa_5ab7f3285542992aa3b8c88f` (revised draft)

> Suzanne Simone Baptiste Louverture is the wife of the leader of which revolution?

Source answer: the Haitian Revolution

Gold final answer: the Haitian Revolution

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: husband of Suzanne Simone Baptiste Louverture | false | Toussaint Louverture | — | [d1s0] | — |
| u2: revolution led by {u1} | true | the Haitian Revolution (accepted alternatives: Haitian Revolution) | u1 | [d6s0] OR [d4s2] OR [d10s1] | — |

Evidence:

- `d1s0` Suzanne Simone Baptiste Louverture [0]: Suzanne Simone Baptiste Louverture (around 1742 – May 19, 1816 in Agen, France) was the wife of Toussaint Louverture and the "Dame-Consort" of the French colony of Saint-Domingue.
- `d4s2` Toussaint L'Overture County Cemetery [2]: It is named for Toussaint Louverture, the leader of the Haitian Revolution.
- `d6s0` Toussaint Louverture [0]: François-Dominique Toussaint Louverture (] 20 May 1743 – 7 April 1803), also known as Toussaint L'Ouverture or Toussaint Bréda, was the best-known leader of the Haitian Revolution.
- `d10s1` Joseph Saint-Rémy [1]: He is best known for his biography "La Vie de Toussaint Louverture" about the Haitian Revolution leader Toussaint L'Ouverture, and for his work "Pétion et Haïti", about another Revolutionary figure, Alexandre Pétion.

Notes:

- 补两条明确说明Toussaint Louverture领导Haitian Revolution的备选。

<details><summary>All source context</summary>

- `d1s0` Suzanne Simone Baptiste Louverture [0]: Suzanne Simone Baptiste Louverture (around 1742 – May 19, 1816 in Agen, France) was the wife of Toussaint Louverture and the "Dame-Consort" of the French colony of Saint-Domingue.
- `d2s0` War of Knives [0]: The War of Knives (French: "Guerre des couteaux"), also known as the War of the South, was a civil war from June 1799 to July 1800 between the Haitian revolutionary Toussaint Louverture, a black ex-slave who controlled the north of Saint-Domingue (modern-day Haiti), and his adversary André Rigaud, a free colored person of mixed race who controlled the south.
- `d2s1` War of Knives [1]: Louverture and Rigaud fought over de facto control of the French colony of Saint-Domingue during the war, which took place after the two men had successfully expelled foreign forces from the colony as part of the Haitian Revolution.
- `d2s2` War of Knives [2]: The war resulted in Toussaint taking control of the entirety of Saint-Domingue, and Rigaud fleeing into exile.
- `d3s0` Jean Baptiste Brunet [0]: Jean Baptiste Brunet (7 July 1763 – 21 September 1824) was a French general of division in the French Revolutionary Army.
- `d3s1` Jean Baptiste Brunet [1]: He was responsible for the arrest of Toussaint Louverture.
- `d3s2` Jean Baptiste Brunet [2]: He was promoted to command a light infantry demi-brigade at the Fleurus in 1794.
- `d3s3` Jean Baptiste Brunet [3]: He led the unit in François Joseph Lefebvre's division in the 1795, 1796 and 1799 campaigns.
- `d3s4` Jean Baptiste Brunet [4]: He was the son of French general Gaspard Jean-Baptiste Brunet who was guillotined in 1793.
- `d4s0` Toussaint L'Overture County Cemetery [0]: The Toussaint L'Ouverture County Cemetery is an historical African-American cemetery located in Franklin, Tennessee.
- `d4s1` Toussaint L'Overture County Cemetery [1]: It was listed on the National Register of Historic Places in 1995.
- `d4s2` Toussaint L'Overture County Cemetery [2]: It is named for Toussaint Louverture, the leader of the Haitian Revolution.
- `d4s3` Toussaint L'Overture County Cemetery [3]: The earliest recorded burials date from 1869, but it wasn't officially incorporated until 1884.
- `d4s4` Toussaint L'Overture County Cemetery [4]: It is "the oldest African American institution in continuous use" in Williamson County.
- `d5s0` Sanité Bélair [0]: Suzanne Bélair, called "Sanité Bélair", (1781 – 5 October 1802), was a Haitian Freedom fighter and revolutionary, lieutenant in the army of Toussaint Louverture.
- `d6s0` Toussaint Louverture [0]: François-Dominique Toussaint Louverture (] 20 May 1743 – 7 April 1803), also known as Toussaint L'Ouverture or Toussaint Bréda, was the best-known leader of the Haitian Revolution.
- `d6s1` Toussaint Louverture [1]: His military and political acumen saved the gains of the first Black insurrection in November 1791.
- `d6s2` Toussaint Louverture [2]: He first fought for the Spanish against the French; then for France against Spain and Great Britain; and finally, for Saint-Domingue against Napoleonic France.
- `d6s3` Toussaint Louverture [3]: He then helped transform the insurgency into a revolutionary movement, which by 1800 had turned Saint-Domingue, the most prosperous slave colony of the time, into the first free colonial society to have explicitly rejected race as the basis of social ranking.
- `d7s0` Revolution (Nina Simone song) [0]: "Revolution" is a 1969 song by American jazz musician Nina Simone and Weldon Irvine.
- `d7s1` Revolution (Nina Simone song) [1]: It was released as a single in 1969 and on the album "To Love Somebody" in 1969.
- `d7s2` Revolution (Nina Simone song) [2]: The single release was split over two sides of a 45 rpm disc and these two edits were used as separate tracks on the album.
- `d7s3` Revolution (Nina Simone song) [3]: The song was released the year after the Beatles' "Revolution", and is seen by some as a variation of that song.
- `d7s4` Revolution (Nina Simone song) [4]: "Revolution" didn't do as well as expected and Simone has expressed surprise and disappointment at its lack of success.
- `d8s0` Simone Torres [0]: Simone Torres arrives in the fictional town of Pine Valley, Pennsylvania in 2001 at the behest of Edmund Grey in order to aid his brother-in-law Mateo Santos uncover the identity of the drug lord "Proteus".
- `d8s1` Simone Torres [1]: An investigative reporter, Simone works to find Proteus's true identity while pretending to be engaged in an affair with Mateo, in order to protect the latter's wife and son from Proteus's wrath.
- `d8s2` Simone Torres [2]: Simone falls in love with Mateo, but it is clear his heart lies with his wife Hayley.
- `d8s3` Simone Torres [3]: Simone mistakenly believes that a legitimate book publisher is interested in her authoring a book on the investigation.
- `d8s4` Simone Torres [4]: Revealing inside information to the publisher, Simone is shocked when it turns out to be a front set up by "Vanessa Cortlandt", the real Proteus.
- `d8s5` Simone Torres [5]: As a result of Simone's leak, FBI agent "Chris Stamp" is almost killed.
- `d8s6` Simone Torres [6]: A furious Mateo distances himself from Simone.
- `d9s0` United States and the Haitian Revolution [0]: The Haitian Revolution provoked mixed reactions in the United States.
- `d9s1` United States and the Haitian Revolution [1]: In June 1793 when the Haitian people, led by Toussaint Louverture, overthrew the French colonial rule and declared themselves an independent colony, it made the neighboring United States uneasy.
- `d9s2` United States and the Haitian Revolution [2]: The slaves in Saint-Domingue’s were able to observe the growing disunity among the white colonists and themselves.
- `d9s3` United States and the Haitian Revolution [3]: They realized that they would need to seek an opportunity to stop the tyranny that was being placed upon them, thus they took a stand and revolted.
- `d9s4` United States and the Haitian Revolution [4]: The Haitian Revolution of 1804 impacted the United States of America, led by Thomas Jefferson, instilling fear of racial instability in the US, and the possible problematic effect the revolution could have on the early foreign relations and trade between the US and the new independent Haiti.
- `d9s5` United States and the Haitian Revolution [5]: Thomas Jefferson realized that the Haitian Revolution had the potential to cause an upheaval against slavery in the US not only by the slaves themselves, but by white abolitionists as well.
- `d9s6` United States and the Haitian Revolution [6]: Southern slaveholders feared that the revolt might spread from the island of Hispaniola to the slave plantations of the Southern United States.
- `d9s7` United States and the Haitian Revolution [7]: The primary goal of the US was to maintain social order in the country, so the United States attempted to suppress the Haitian Revolution.
- `d9s8` United States and the Haitian Revolution [8]: The US even went as far as to refuse acknowledgement of Haitian independence until 1862, which was during the heat of the North American civil war; coincidentally the main causal factor for the war between the states was slavery.
- `d9s9` United States and the Haitian Revolution [9]: The second major impact that the Haitian Revolution had on the United States was on early foreign relations and trade that had been conducted with Haiti.
- `d9s10` United States and the Haitian Revolution [10]: The United States had conducted trade and commerce with the Haitian island under French rule during the eighteenth century.
- `d9s11` United States and the Haitian Revolution [11]: Haiti was the main producer of the United States supply of sugar and coffee, and once the Haitian slave population had broken from slavery, the US was reluctant to continue trade with them in fear that they would upset the French and the Southern slaveholders.
- `d9s12` United States and the Haitian Revolution [12]: American merchants conducted a substantial trade with the plantations on Hispaniola (aka the French colony of Saint Domingue or Haiti).
- `d9s13` United States and the Haitian Revolution [13]: But there were anti-slavery advocates in northern cities who believed that consistency with the principles of the American Revolution — life, liberty and equality for all—demanded that the U.S. support the slave insurgents.
- `d9s14` United States and the Haitian Revolution [14]: An extremely beneficial aspect and real estate triumph that resulted from the Haitian Revolution and impacted the United States was the Louisiana Purchase.
- `d9s15` United States and the Haitian Revolution [15]: Once Napoleon had lost his control of the land holding in the Caribbean to the Haitian rebellion, he felt that the French territory in the southern part of the United States was useless to the French Empire.
- `d9s16` United States and the Haitian Revolution [16]: The US was only interested in the New Orleans area; however, the revolution enabled the sale of the entire territory west of the Mississippi River for around $15 million.
- `d9s17` United States and the Haitian Revolution [17]: This purchase more than doubled the United States’ territory.
- `d10s0` Joseph Saint-Rémy [0]: Joseph Saint-Rémy (1818 - 1856) was a Haitian historian.
- `d10s1` Joseph Saint-Rémy [1]: He is best known for his biography "La Vie de Toussaint Louverture" about the Haitian Revolution leader Toussaint L'Ouverture, and for his work "Pétion et Haïti", about another Revolutionary figure, Alexandre Pétion.
- `d10s2` Joseph Saint-Rémy [2]: Born in Guadeloupe, Saint-Rémy emigrated to Haiti as a young child and grew up in Les Cayes before leaving for school in France.

</details>

## Q237 — `hotpotqa_5ab80bbf5542991d32223818` (revised draft)

> Which airport is operated by the Coos Country Airport District, Southwest Oregon Regional Airport or Lawton–Fort Sill Regional Airport?

Source answer: Southwest Oregon Regional Airport

Gold final answer: Southwest Oregon Regional Airport

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: whether Southwest Oregon Regional Airport is operated by the Coos County Airport District | false | yes | — | [d4s1] | — |
| u2: whether Lawton–Fort Sill Regional Airport is operated by the Coos County Airport District | false | no | — | `[]`：无直接支持 | — |
| u3: Which airport is operated by the Coos Country Airport District, Southwest Oregon Regional Airport or Lawton–Fort Sill Regional Airport? | true | Southwest Oregon Regional Airport **[by_presupposition]** | u1, u2 | `[[]]`：由全部依赖推出 | [d4s1] |

Evidence:

- `d4s1` Southwest Oregon Regional Airport [1]: It is operated by the Coos County Airport District.

Notes:

- 补两候选结构，城市所有权不是运营者证据；保留正向确认链路，不臆造另一机场运营关系。

<details><summary>All source context</summary>

- `d1s0` Lawton–Fort Sill Regional Airport [0]: Lawton–Fort Sill Regional Airport (IATA: LAW, ICAO: KLAW, FAA LID: LAW) is a city owned airport two miles south of Lawton, in Comanche County, Oklahoma.
- `d1s1` Lawton–Fort Sill Regional Airport [1]: It is used for military aviation from nearby Fort Sill and Sheppard Air Force Base and is served by American Eagle.
- `d1s2` Lawton–Fort Sill Regional Airport [2]: Allegiant Air runs occasional charters to various destinations in the western United States.
- `d2s0` Elizabeth City Regional Airport [0]: Elizabeth City Regional Airport (IATA: ECG, ICAO: KECG, FAA LID: ECG) is a joint civil-military public and military use airport located three nautical miles (6 km) southeast of the central business district of Elizabeth City, in Pasquotank County, North Carolina, United States.
- `d2s1` Elizabeth City Regional Airport [1]: The airport, on the shore of the Pasquotank River, is also known as Elizabeth City-Pasquotank County Regional Airport or ECG Regional Airport.
- `d2s2` Elizabeth City Regional Airport [2]: It is included in the National Plan of Integrated Airport Systems for 2011–2015, which categorized it as a "general aviation" facility.
- `d3s0` Stafford Regional Airport [0]: Stafford Regional Airport (ICAO: KRMN, FAA LID: RMN) is a public airport located three miles (5 km) southwest of the central business district of Stafford, the county seat of Stafford County, Virginia, United States.
- `d3s1` Stafford Regional Airport [1]: The airport is southwest of the intersection of Route 630 and U.S. Route 1 near Interstate 95, approximately 40 mi south of Washington, D.C. and 60 mi north of Richmond.
- `d3s2` Stafford Regional Airport [2]: It is owned and operated by the Stafford Regional Airport Authority, an independent body of representatives from Stafford and Prince William Counties and the City of Fredericksburg.
- `d4s0` Southwest Oregon Regional Airport [0]: Southwest Oregon Regional Airport (IATA: OTH, ICAO: KOTH, FAA LID: OTH) , formerly North Bend Municipal Airport, is a public airport in North Bend, Coos County, Oregon.
- `d4s1` Southwest Oregon Regional Airport [1]: It is operated by the Coos County Airport District.
- `d5s0` History of Lawton, Oklahoma [0]: The History of Lawton, Oklahoma refers to the history of the southwestern Oklahoma city of Lawton, Oklahoma.
- `d5s1` History of Lawton, Oklahoma [1]: Lawton's history starts with opening of American Indian reservation lands in the early 1900s and has seen population and economic growth throughout the 20th Century due to its proximity with Fort Sill.
- `d6s0` Manassas Regional Airport [0]: Manassas Regional Airport (IATA: KHEF, ICAO: HEF) , also known as Harry P. Davis Field, is a city-owned public-use airport located four nautical miles (7 km) southwest of the central business district of Manassas, in a section of Manassas that was carved out of Prince William County specifically for the purpose of containing the airport.
- `d6s1` Manassas Regional Airport [1]: The largest regional airport in the state of Virginia, Manassas Regional Airport is located 30 miles from Washington, D.C.
- `d7s0` Coast Guard Air Station North Bend [0]: Coast Guard Air Station North Bend (CGAS North Bend) was established September 28, 1974 at Southwest Oregon Regional Airport in North Bend, Oregon, United States.
- `d7s1` Coast Guard Air Station North Bend [1]: The unit houses 153 active duty, nine reserve duty and five civilian personnel.
- `d7s2` Coast Guard Air Station North Bend [2]: The unit operates five Eurocopter HH-65 Dolphin helicopters.
- `d7s3` Coast Guard Air Station North Bend [3]: CGAS North Bend received its first upgraded HH-65C Dolphin in 2007 The unit functions include search and rescue, law enforcement, marine environmental protection, aids to navigation, and enforcement of federal treaties.
- `d8s0` Lawton High School (Oklahoma) [0]: Lawton High School (LHS) was the first high school built in Lawton, Oklahoma.
- `d8s1` Lawton High School (Oklahoma) [1]: Lawton High is located at 601 Northwest Fort Sill Boulevard in Lawton, Oklahoma.
- `d8s2` Lawton High School (Oklahoma) [2]: The school was originally housed in a building on 800 Southwest 'C' Avenue, which later came to be the Central Junior High building until the junior high was also moved to 1201 Northwest Fort Sill Boulevard.
- `d8s3` Lawton High School (Oklahoma) [3]: Old Lawton High School on C Avenue is listed on the National Register of Historic Places.
- `d9s0` Eastern Oregon Regional Airport [0]: Eastern Oregon Regional Airport (IATA: PDT, ICAO: KPDT, FAA LID: PDT) (Eastern Oregon Regional Airport at Pendleton) is a city-owned public airport three miles northwest of Pendleton, in Umatilla County, Oregon.
- `d9s1` Eastern Oregon Regional Airport [1]: It is used for general aviation and by one airline subsidized by the Essential Air Service program.
- `d10s0` Hammerfest Airport [0]: Hammerfest Airport (Norwegian: "Hammerfest lufthavn" ; IATA: HFT, ICAO: ENHF ) is a regional airport at Prærien in Hammerfest, Norway.
- `d10s1` Hammerfest Airport [1]: It is operated by the state-owned Avinor and handled 145,396 passengers in 2014, making it the third-busiest regional airport in the country.
- `d10s2` Hammerfest Airport [2]: The airport has a 880 m runway aligned 05/23.
- `d10s3` Hammerfest Airport [3]: Services are provided by Widerøe using the Dash 8-100.
- `d10s4` Hammerfest Airport [4]: Up to eight daily flights are provided to Tromsø and public service obligation flights are flown eastwards to other airports in Finnmark.
- `d10s5` Hammerfest Airport [5]: The airport is the base for offshore helicopter services operated by Bristow Norway and CHC Helikopter Service.
- `d10s6` Hammerfest Airport [6]: An estimated 40,000 people from Hammerfest Airport's catchment area annually use Alta Airport for flights to Oslo.

</details>

## Q238 — `hotpotqa_5ab811395542990e739ec80f` (revised draft)

> Which continent have a distribution of both the Ternstroemia and Cussonia genus of plants? 

Source answer: Africa

Gold final answer: Africa

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: listed distribution regions of Cussonia | false | Africa (South Africa and the Mascarene Islands; Afrotropics) | — | [d5s1] OR [d5s0] | — |
| u2: listed distribution regions of Ternstroemia | false | Africa, Asia, the Americas | — | [d7s1] | — |
| u3: Which continent have a distribution of both the Ternstroemia and Cussonia genus of plants?  | true | Africa | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d5s0` Cussonia [0]: Cussonia is a genus of plants of family Araliaceae, which is native to the Afrotropics.
- `d5s1` Cussonia [1]: It originated in Africa and has its center of distribution in South Africa and the Mascarene Islands.
- `d7s1` Ternstroemia [1]: It is distributed in tropical and subtropical regions in Africa, Asia, and the Americas.

Notes:

- 将origin描述改为distribution，按用户要求补d5s0备选；d5s1使用的是center of distribution部分，u3以两种植物的非洲分布交集推出。
- 本题局部约定：按用户note接受Afrotropics及South Africa到Africa的地域归一化，仅用于本题分布证据；不推广到无证据的经纬度比较。

<details><summary>All source context</summary>

- `d1s0` Festuca [0]: Festuca (fescue) is a genus of flowering plants belonging to the grass family, Poaceae (subfamily Pooideae).
- `d1s1` Festuca [1]: They are evergreen or herbaceous perennial tufted grasses with a height range of 10 - and a cosmopolitan distribution, occurring on every continent except Antarctica.
- `d1s2` Festuca [2]: The genus is closely related to ryegrass ("Lolium"), and recent evidence from phylogenetic studies using DNA sequencing of plant mitochondrial DNA shows that the genus lacks monophyly.
- `d1s3` Festuca [3]: As a result, plant taxonomists have moved several species, including the forage grasses tall fescue and meadow fescue, from the genus "Festuca" into the genus "Lolium".
- `d2s0` Myosotidium [0]: Myosotidium is a genus of plants belonging to the family Boraginaceae.
- `d2s1` Myosotidium [1]: This genus is represented by the single species Myosotidium hortensia, the giant forget-me-not or Chatham Islands forget-me-not, which is endemic to the Chatham Islands, New Zealand.
- `d2s2` Myosotidium [2]: The biogeography is yet unresolved, but its ancestors are likely from the American continent, as "Myosotidium hortensia" was found to be sister to the South American plant genus "Selkirkia" and both genera being sister to the North American genus "Mimophytum".
- `d3s0` Diocirea [0]: Diocirea is a genus of flowering plants in the figwort family, Scrophulariaceae.
- `d3s1` Diocirea [1]: The genus is endemic to a small area in the south-west of Western Australia and is intermediate in character between "Eremophila" and "Myoporum".
- `d3s2` Diocirea [2]: There are four members of the genus, all of which are small shrubs with stems and leaves which produce a resin making the plants appear bluish-green.
- `d3s3` Diocirea [3]: Neither the genus, nor any of the species had been described before 2007 although a few specimens had been collected as "Eremophila elachantha".
- `d3s4` Diocirea [4]: Despite their limited distribution, they often occur in populations of several thousand individual plants, forming a dense ground cover.
- `d4s0` Owenia (plant) [0]: Owenia is a genus of plants, mainly trees in the mahogany family Meliaceae.
- `d4s1` Owenia (plant) [1]: They are endemic to Australia and fairly widespread across the continent.
- `d4s2` Owenia (plant) [2]: There are five species in the genus, most from New South Wales and living in conditions ranging from wet rainforest to the verges of the desert.
- `d4s3` Owenia (plant) [3]: Like many plants, it plays its part in patch dynamics.
- `d5s0` Cussonia [0]: Cussonia is a genus of plants of family Araliaceae, which is native to the Afrotropics.
- `d5s1` Cussonia [1]: It originated in Africa and has its center of distribution in South Africa and the Mascarene Islands.
- `d5s2` Cussonia [2]: Due to their striking habit, they are a conspicuous and easily recognizable group of plants.
- `d5s3` Cussonia [3]: Their genus name commemorates the botanist Pierre Cusson.
- `d5s4` Cussonia [4]: The Afro-Malagasy and Asian "Schefflera", and Afrotropical "Seemannaralia" genera are related taxa that share several of its morphological characteristics, among which the leaves borne on the end of branches, inflorescences carried on terminal branches or stems, and reduced leaf complexity in developing inflorescences.
- `d6s0` Luzula [0]: Luzula is a genus of flowering plants the family Juncaceae, the rushes.
- `d6s1` Luzula [1]: The genus has a cosmopolitan distribution, with species occurring throughout the world, especially in temperate regions, the Arctic, and higher elevation areas in the tropics.
- `d6s2` Luzula [2]: Plants of the genus are known commonly as wood-rush, wood rush, or woodrush.
- `d6s3` Luzula [3]: Possible origins of the genus name include the Italian "lucciola" ("to shine, sparkle") or the Latin "luzulae" or "luxulae", from "lux" ("light"), inspired by the way the plants sparkle when wet with dew.
- `d6s4` Luzula [4]: Another etymology sometimes given is that it does derive from lucciola but that this meant a midsummerfield, or from the Latin luculus, meaning a small place; the same source also states that this name was applied by Luigi Anguillara (an Italian botanist) in 1561.
- `d7s0` Ternstroemia [0]: Ternstroemia is a genus of flowering plants in the family Pentaphylacaceae.
- `d7s1` Ternstroemia [1]: It is distributed in tropical and subtropical regions in Africa, Asia, and the Americas.
- `d8s0` Eugenia [0]: Eugenia is a genus of flowering plants in the myrtle family Myrtaceae.
- `d8s1` Eugenia [1]: It has a worldwide, although highly uneven, distribution in tropical and subtropical regions.
- `d8s2` Eugenia [2]: The bulk of the approximately 1,000 species occur in the New World tropics, especially in the northern Andes, the Caribbean, and the Atlantic Forest (coastal forests) of eastern Brazil.
- `d8s3` Eugenia [3]: Other centers of diversity include New Caledonia and Madagascar.
- `d8s4` Eugenia [4]: Many species new to science have been and are in the process of being described from these regions.
- `d8s5` Eugenia [5]: For example, 37 new species of "Eugenia" have been described from Mesoamerica in the past few years.
- `d8s6` Eugenia [6]: At least 20 new species are currently in the process of being described from New Caledonia, and approximately the same number of species new to science may occur in Madagascar.
- `d8s7` Eugenia [7]: Despite the enormous ecological importance of the myrtle family in Australia (e.g. "Eucalyptus", "Corymbia", "Angophora", "Melaleuca", "Callistemon", "Rhodamnia", "Gossia"), only one species of "Eugenia", "E. reinwardtiana", occurs on that continent.
- `d8s8` Eugenia [8]: The genus also is represented in Africa south of the Sahara, but it is relatively species-poor on that continent.
- `d8s9` Eugenia [9]: In the past some botanists included the morphologically similar Old World genus "Syzygium" in "Eugenia", but research by Rudolf Schmid in the early 1970s convinced most botanists that the genera are easily separable.
- `d8s10` Eugenia [10]: Research by van Wyk and colleagues in South Africa suggests the genus may comprise at least two major lineages, recognizable by anatomical and other features.
- `d9s0` Cerceris [0]: Cerceris is a genus of wasps in the family Crabronidae.
- `d9s1` Cerceris [1]: It is the largest genus in the family, with over 1030 described species.
- `d9s2` Cerceris [2]: The genus has a cosmopolitan distribution, with species on every continent.
- `d10s0` Nymphaea [0]: Nymphaea is a genus of hardy and tender aquatic plants in the family Nymphaeaceae.
- `d10s1` Nymphaea [1]: The genus has a cosmopolitan distribution.
- `d10s2` Nymphaea [2]: Many species are cultivated as ornamental plants, and many cultivars have been bred.
- `d10s3` Nymphaea [3]: Some taxa occur as introduced species where they are not native, and some are weeds. Plants of the genus are known commonly as water lilies.
- `d10s4` Nymphaea [4]: The genus name is from the Greek νυμφαια, "nymphaia" and the Latin "nymphaea", which mean "water lily" and were inspired by the nymphs of Greek and Latin mythology.

</details>

## Q239 — `hotpotqa_5a7bb84d554299294a54aaa1` (revised draft)

> Who is older, Vincent Walker or David Usher?

Source answer: David Usher

Gold final answer: David Usher

Question type: `comparison` (source type `comparison`)

Replaces: `hotpotqa_5ab868e755429919ba4e22e3`

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: birth year of Vincent Walker | false | 1980 | — | [d5s0] | — |
| u2: birth year of David Usher | false | 1966 | — | [d1s0] | — |
| u3: Who is older, Vincent Walker or David Usher? | true | David Usher | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d1s0` David Usher [0]: David Usher (born April 24, 1966) is an English-born Canadian musician, best-selling author, keynote speaker and activist, known as the lead singer of the alternative rock band Moist.
- `d5s0` Vincent Walker [0]: Vincent Francis Walker (born March 2, 1980), better known as Vince Walker, is an American multi-instrumentalist, best known as the lead singer of third-wave ska band Suburban Legends.

Notes:

- 替换：WPX没有部门数量，不能将沉默算成0。 新题保留原source type，人工核对两条显式事实及答案。

<details><summary>All source context</summary>

- `d1s0` David Usher [0]: David Usher (born April 24, 1966) is an English-born Canadian musician, best-selling author, keynote speaker and activist, known as the lead singer of the alternative rock band Moist.
- `d2s0` Let It Play [0]: Let It Play is the ninth studio album by Canadian solo artist David Usher.
- `d2s1` Let It Play [1]: It was released on October 21, 2016 via David Usher's own music label, Evil Empire Inc..
- `d2s2` Let It Play [2]: The album features English translations of French Canadian songs.
- `d3s0` Billy Bang [0]: Billy Bang (September 20, 1947 – April 11, 2011), born William Vincent Walker, was an American free jazz violinist and composer.
- `d4s0` Brian Robertson (trombonist) [0]: Brian Robertson (born October 19, 1979) is the trombone player for the Orange County-based third-wave ska band Suburban Legends and, along with Vincent Walker, is one of the two members to have played with the band since its origin as Bomb Squad.
- `d4s1` Brian Robertson (trombonist) [1]: He met other ex-Suburban Legends / Bomb Squad members, trumpet player Aaron Bertram and best friend and trombone player Ryan Dallas Cook through the Huntington Beach High School Marching Band.
- `d4s2` Brian Robertson (trombonist) [2]: In 2007, Robertson started to be known by the nickname 'Robot', most likely a reference to the dance moves he does onstage with the band, the first three letters of his last name, and/or to avoid confusion with the band's other Brian, Brian Klemm.
- `d5s0` Vincent Walker [0]: Vincent Francis Walker (born March 2, 1980), better known as Vince Walker, is an American multi-instrumentalist, best known as the lead singer of third-wave ska band Suburban Legends.
- `d5s1` Vincent Walker [1]: He was formerly the lead trumpet player, and left sometime after the release of "Rump Shaker", but returned to the band in September 2005 for the band's appearance on the Jerry Lewis MDA Telethon, which happened to be lead singer Tim Maurer's last performance.
- `d5s2` Vincent Walker [2]: He replaced Maurer as the singer in an odd switching of roles, and continues with the band as frontman.
- `d6s0` Vince Foster [0]: Vincent Walker "Vince" Foster Jr. (January 15, 1945 – July 20, 1993) was a Deputy White House Counsel during the first half-year of President Bill Clinton's administration.
- `d6s1` Vince Foster [1]: Prior to that, he was a partner at Rose Law Firm in Little Rock, Arkansas, where he was a colleague and friend of Hillary Rodham Clinton and where, as "The Washington Post" later wrote, he rose to "the pinnacle of the Arkansas legal establishment."
- `d6s2` Vince Foster [2]: At the White House he was unhappy with work in politics and spiraled into depression.
- `d6s3` Vince Foster [3]: His death by gunshot was attributed by five official or governmental investigations to suicide but several conspiracy theories emerged.
- `d7s0` Black Black Heart [0]: "Black Black Heart" is a song written by David Usher and Jeff Pearce and released as a second single off Usher's 2001 album "Morning Orbit".
- `d8s0` Day Job (Suburban Legends album) [0]: Day Job is Suburban Legends' fifth album, released on April 3, 2012.
- `d8s1` Day Job (Suburban Legends album) [1]: Aaron Bertram, Brian Robertson, Derek Rock, and Vincent Walker appeared on local online radio program "TNN Radio" to announce the album on February 18, 2012.
- `d9s0` Charles Vincent Walker [0]: Charles Vincent Walker FRS (20 March 1812 – 24 December 1882) was an English electrical engineer and publisher, a major influence on the development of railway telecommunications, he was also the first person to send a submarine telegraph signal.
- `d10s0` Tim Maurer [0]: Timothy Robert "Tim" Maurer (born October 10, 1980) is an American singer, best known as the former lead singer of third-wave ska band Suburban Legends.
- `d10s1` Tim Maurer [1]: He has left the band on two separate occasions.
- `d10s2` Tim Maurer [2]: The first was in 2000 after the recording of Origin Edition.
- `d10s3` Tim Maurer [3]: He rejoined the band in early 2002 after his replacement singer Chris Batstone left the band.
- `d10s4` Tim Maurer [4]: He officially left the band again in September 2005 after the band's third consecutive appearance on the Jerry Lewis MDA Telethon, performing a new song entitled "Moving Closer."
- `d10s5` Tim Maurer [5]: The band's former trumpet player, Vincent Walker, rejoined the band for the performance, then took over as lead singer afterward.
- `d10s6` Tim Maurer [6]: Maurer returned for a final performance with the band on November 29, 2005 at Huntington Beach High School for a benefit show for the Ryan Dallas Cook Memorial Fund, which was set up following the death of Suburban Legends' trombonist Dallas Cook.

</details>

## Q240 — `hotpotqa_5ab870ee5542990e739ec8f6` (revised draft)

> A Wind in the Door is part of a series written by who?

Source answer: Madeleine L'Engle

Gold final answer: Madeleine L'Engle

Question type: `single` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: author of the series containing A Wind in the Door | true | Madeleine L'Engle **[by_presupposition]** | — | [d2s1, d7s0] | [d2s0] |

Evidence:

- `d2s0` A Wind in the Door [0]: A Wind in the Door is a young adult science fantasy novel by Madeleine L'Engle.
- `d2s1` A Wind in the Door [1]: It is a companion book to "A Wrinkle in Time", and part of the Time Quintet.
- `d7s0` Time Quintet [0]: The Time Quintet is a fantasy/science fiction series of five young adult novels written by Madeleine L'Engle.

Notes:

- 保留两条路径：d2s0为预设捷径；d2s1+d7s0为完整系列桥接证据。合并到一个必要unit，避免无条件依赖u1挡住捷径。
- 本题局部约定：按用户要求，单本小说作者捷径依赖本题同作者系列的预设；明确放在presupposition_sets，不当作“书作者必等于系列作者”的普遍证据。

<details><summary>All source context</summary>

- `d1s0` Codename: Kids Next Door [0]: Codename: Kids Next Door, commonly abbreviated to Kids Next Door or KND, is an American animated television series created by Tom Warburton for Cartoon Network, and the 13th of the network's "Cartoon Cartoons".
- `d1s1` Codename: Kids Next Door [1]: The series centers on the adventures of five children who operate from a high-tech tree house, fighting against adult and teen villains with advanced 2×4 technology.
- `d1s2` Codename: Kids Next Door [2]: Using their codenames (Numbuh 1, Numbuh 2, Numbuh 3, Numbuh 4, and Numbuh 5), they are Sector V, part of a global organization called the Kids Next Door.
- `d2s0` A Wind in the Door [0]: A Wind in the Door is a young adult science fantasy novel by Madeleine L'Engle.
- `d2s1` A Wind in the Door [1]: It is a companion book to "A Wrinkle in Time", and part of the Time Quintet.
- `d3s0` The Four Winds of Love [0]: The Four Winds of Love is the overall title for a series of six novels written by Compton Mackenzie, "The East Wind of Love" (1937), "The South Wind of Love" (1938), "The West Wind of Love" (1940), "West to North" (1942), "The North Wind of Love, Book 1" (1944) and "The North Wind of Love, Book 2" (1945), which taken together constitute a major fictional chronicle of the first forty years of the twentieth century.
- `d3s1` The Four Winds of Love [1]: The main protagonist of the hexalogy is the semi-autobiographical character of John Ogilvie.
- `d4s0` Door to Door (Modern Family) [0]: "Door to Door" is the fourth episode of the third season of the American sitcom "Modern Family", and the series' 52nd episode overall.
- `d4s1` Door to Door (Modern Family) [1]: "Door to Door" first aired on October 5, 2011, on ABC.
- `d4s2` Door to Door (Modern Family) [2]: The episode was written by Bill Wrubel and directed by Chris Koch.
- `d5s0` Koi Kaze [0]: Koi Kaze (Japanese: 恋風 , lit.
- `d5s1` Koi Kaze [1]: "Love Wind") is a Japanese manga series written and illustrated by Motoi Yoshida.
- `d5s2` Koi Kaze [2]: It premiered in the September 2001 issue of "Evening" and ran for 29 chapters until its conclusion in the October 2004 issue.
- `d5s3` Koi Kaze [3]: The individual chapters were collected and published in five "tankōbon" volumes by Kodansha.
- `d5s4` Koi Kaze [4]: The series tells of the love affair that develops between 27-year-old Koshiro, and his 15-year-old sister, Nanoka.
- `d6s0` Kaze Hikaru [0]: Kaze Hikaru (Japanese: 風光る , lit.
- `d6s1` Kaze Hikaru [1]: "Shining Wind") is a Japanese manga series written and illustrated by Taeko Watanabe.
- `d6s2` Kaze Hikaru [2]: Set in the "bakumatsu" period, the series follows Tominaga Sei, a young girl who poses as a boy named Kamiya Seizaburo so she can join the Mibu-Roshi (Special Police; later known as the Shinsengumi).
- `d6s3` Kaze Hikaru [3]: She befriends her sensei, Okita Sōji, who discovers her secret.
- `d7s0` Time Quintet [0]: The Time Quintet is a fantasy/science fiction series of five young adult novels written by Madeleine L'Engle.
- `d8s0` Close the Last Door [0]: Close the Last Door (Japanese: 最後のドアを閉めろ!
- `d8s1` Close the Last Door [1]: , Hepburn: Saigo no Door wo Shimero! )
- `d8s2` Close the Last Door [2]: is a yaoi manga series written by Yugi Yamada.
- `d8s3` Close the Last Door [3]: It has been adapted into an OVA directed by Tama.
- `d8s4` Close the Last Door [4]: It is licensed in North America by Digital Manga Publishing, which published the first volume in 2006.
- `d9s0` Kaze no Stigma [0]: Stigma of the Wind or Kaze no Stigma (Japanese: 風の<ruby ><rb>聖痕</rb><rp> (</rp><rt >スティグマ</rt><rp>)</rp></ruby> , Hepburn: Kaze no Sutiguma , lit.
- `d9s1` Kaze no Stigma [1]: "Stigma of the Wind") is a Japanese light novel series written by Takahiro Yamato and illustrated by Hanamaru Nanto.
- `d9s2` Kaze no Stigma [2]: After the death of the author on July 20, 2009, the story remains incomplete at twelve chapters.
- `d9s3` Kaze no Stigma [3]: A 24-episode anime adaptation directed by Junichi Sakata and animated by Gonzo aired from April–September 2007.
- `d9s4` Kaze no Stigma [4]: It has been dubbed in English by Animax Asia under the title Stigma of the Wind and by Funimation as Kaze no Stigma.
- `d10s0` Dan Angel [0]: Dan Angel is an American film and television producer, screenwriter, story editor and showrunner.
- `d10s1` Dan Angel [1]: He has written and produced a number of television series and movies, often with his writing partner Billy Brown, including "The X-Files", "Goosebumps", "Animorphs", "", "Door to Door", "", "Christmas in Canaan", "" and "Dan Vs.".
- `d10s2` Dan Angel [2]: His work has won numerous awards, including a Primetime Emmy Award for Outstanding Made for Television Movie and Peabody Award recognizing his work executive producing "Door to Door".
- `d10s3` Dan Angel [3]: and another Emmy Award for Outstanding Children's Series in his work on .

</details>
