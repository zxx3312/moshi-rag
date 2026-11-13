# Revised Gold — batch 9

原始review保持不变。本文是依据原note生成的修订草稿；完整修改说明见[修改报告](../change_report.md)。

句子带有文档标题；允许使用标题解析该文档中的人名及代词。support_sets内为AND，组间为OR；presupposition_sets按现有评估器表示预设捷径。

## Q241 — `hotpotqa_5a7906f55542990784727792` (revised draft)

> When was Fannie Lee Chaney's son born?

Source answer: May 30, 1943

Gold final answer: May 30, 1943

Question type: `bridge` (source type `bridge`)

Replaces: `hotpotqa_5ab8723c55429934fafe6dbc`

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: son of Fannie Lee Chaney | false | James Chaney | — | [d10s0] | — |
| u2: date of birth of {u1} | true | May 30, 1943 | u1 | [d6s0] | — |

Evidence:

- `d6s0` James Chaney [0]: James Earl Chaney (May 30, 1943 – June 21, 1964), from Meridian, Mississippi, was one of three American civil rights workers who were murdered during Freedom Summer by members of the Ku Klux Klan near Philadelphia, Mississippi.
- `d10s0` Fannie Lee Chaney [0]: Fannie Lee Chaney (September 4, 1921 – May 22, 2007) was an American baker turned civil rights activist after her son James Chaney was murdered by the Ku Klux Klan during the 1964 Freedom Summer rides in Mississippi.

Notes:

- 替换：四名回归球员，题干没有唯一定位条件。 新题保留原source type，人工核对两条显式事实及答案。

<details><summary>All source context</summary>

- `d1s0` Darrel Chaney [0]: Darrel Lee Chaney (born March 9, 1948, in Hammond, Indiana) is an American former player/announcer in Major League Baseball who played for the Cincinnati Reds and Atlanta Braves from 1969 to 1979.
- `d1s1` Darrel Chaney [1]: In the early 1980s he worked for the Braves as an announcer along with Ernie Johnson, Skip Caray and Pete Van Wieren.
- `d1s2` Darrel Chaney [2]: He was on the Atlanta Braves Radio Network as well as WTBS-TV.
- `d2s0` Abraham's family tree [0]: Abraham is known as the patriarch of the Jewish people through Isaac, the son born to him and Sarah in their old age and the patriarch of Islam through his son Ishmael, born to Abraham and his wife’s servant Hagar.
- `d3s0` The Minotaur in House of Leaves [0]: The Minotaur or Minotauros was the son born of lust to Queen Pasiphae of Crete and a bull.
- `d3s1` The Minotaur in House of Leaves [1]: He had the body of a man and the head of a bull and was more beast than human.
- `d3s2` The Minotaur in House of Leaves [2]: The creature was banished by King Minos to reside in the centre of a labyrinth in Knossos built by the ingenious architect Daedalus and his son Icarus.
- `d3s3` The Minotaur in House of Leaves [3]: The Minotaur was nursed by Queen Pasiphae as a child but grew to devour humans, so he was safely put away in the maze contrived so carefully and trickily that it was impossible for anyone that entered to navigate or escape it.
- `d3s4` The Minotaur in House of Leaves [4]: The Athenians were forced to pay a tribute to King Minos by sacrificing seven of their maidens and seven of their men, unarmed, to the Minotaur every nine years.
- `d3s5` The Minotaur in House of Leaves [5]: The Minotaur eventually fell prey to the sword of Theseus.
- `d3s6` The Minotaur in House of Leaves [6]: It is also rumoured that the Minotaur was in fact the offspring of King Minos but his unsightly and grotesque appearance was shameful to King Minos and was the reason why the Minotaur was banished under the pretext of inspiring fear and cannibalistic capabilities.
- `d4s0` Sunsum [0]: In the mythology of the Ashanti people and Akan people, the Sunsum is one's Spirit.
- `d4s1` Sunsum [1]: The Sunsum is what connects the body (honam) to the soul (Kra).
- `d4s2` Sunsum [2]: The Sunsum can be transmitted in a variety of ways, including from father to son during conception.
- `d4s3` Sunsum [3]: This power is used to protect the carriers of this spirit.
- `d4s4` Sunsum [4]: When a man dies, the Sunsum returns to the metaphorical house of the father in wait to be reincarnated in the next son born of the men of that family.
- `d5s0` Mithridates IV of Parthia [0]: Mithridates IV of Parthia (flourished 1st century & 2nd century) was a Prince of Iranian and Greek ancestry.
- `d5s1` Mithridates IV of Parthia [1]: He ruled as King of the Parthian Empire from 129 to 140.
- `d5s2` Mithridates IV of Parthia [2]: Mithridates IV was the youngest son born to Vonones II from a Greek concubine and was one of the brothers of Osroes I of Parthia (109–129).
- `d5s3` Mithridates IV of Parthia [3]: During the invasion of Mesopotamia by the Roman emperor Trajan (98–117) in 116, he and his son Sanatruces II of Parthia, took up the diadem but were defeated.
- `d5s4` Mithridates IV of Parthia [4]: After the death of Osroes I in 129 he assumed the throne and continued the struggle with the rival King Vologases III of Parthia (105–147).
- `d5s5` Mithridates IV of Parthia [5]: He died in an attack on Commagene in 140.
- `d5s6` Mithridates IV of Parthia [6]: Mithridates IV had appointed his son Sanatruces II as his successor, but Sanatruces II fell in a battle with the Romans.
- `d5s7` Mithridates IV of Parthia [7]: Another son, Vologases IV of Parthia (147–191), took the throne after the death of Vologases III in 147.
- `d6s0` James Chaney [0]: James Earl Chaney (May 30, 1943 – June 21, 1964), from Meridian, Mississippi, was one of three American civil rights workers who were murdered during Freedom Summer by members of the Ku Klux Klan near Philadelphia, Mississippi.
- `d6s1` James Chaney [1]: The others were Andrew Goodman and Michael Schwerner from New York City.
- `d7s0` Nijō Kanemoto [0]: Nijō Kanemoto (二条 兼基 , 1268–1334) , son of regent Nijō Yoshizane and adopted son of Nijō Morotada, was a Japanese "kugyō" (court noble) of the Kamakura period (1185–1333) of Japan.
- `d7s1` Nijō Kanemoto [1]: He held regent positions sesshō in 1298 and kampaku from 1300 to 1305.
- `d7s2` Nijō Kanemoto [2]: Regent Nijō Michihira was his son born by a concubine.
- `d7s3` Nijō Kanemoto [3]: His wife was a daughter of regent Kujō Tadanori; she gave birth to a son who was adopted by Imakōji family and became known as Imakōji Yoshifuyu, and a daughter who later married Kujō Fusazane.
- `d8s0` Savarni Manu [0]: According to Hindu mythology, there are 14 Manus specified.
- `d8s1` Savarni Manu [1]: As per Hindu texts present Manvantara runs on the name of seventh Manu i.e. Vaivasvata Manu.
- `d8s2` Savarni Manu [2]: Next coming Manu i.e. eighth Manu name is Savarni Manu or Surya Savarnika Manu.
- `d8s3` Savarni Manu [3]: Surya Savarnika means resemblance of Sun.
- `d8s4` Savarni Manu [4]: He is the son born to the sun-god Surya and wife named Chhaya.
- `d8s5` Savarni Manu [5]: Savarni's sons would be headed by Nirmoka, and among the demigods are the Sutapas.
- `d8s6` Savarni Manu [6]: Bali, the son of Virochana, is Indra, and Galava and Parashurama are among the seven sages.
- `d8s7` Savarni Manu [7]: In this age of Manu, the incarnation of the Supreme Personality of Godhead appears as Sarvabhauma, the son of Devaguhya and Sarasvati.
- `d8s8` Savarni Manu [8]: On the name of this Manu the only Ashram i.e. S S M Ashramam i.e Surya Savarnika Manavu Ashramam has been established at Garlavoddu, in India.
- `d9s0` Payne baronets [0]: The Payne Baronetcy, of St Christopher's in the West Indies, was a title in the Baronetage of Great Britain.
- `d9s1` Payne baronets [1]: It was created on 31 October 1737 for Charles Payne.
- `d9s2` Payne baronets [2]: According to some sources that title became extinct on the death of the second Baronet, Sir Gillis Payne, in 1801.
- `d9s3` Payne baronets [3]: Sir Gillis was in a relationship with a farmer's daughter, Maria Keeling.
- `d9s4` Payne baronets [4]: They apparently married in 1761 although several children had been born before this date.
- `d9s5` Payne baronets [5]: Peter Payne was the eldest son born after the marriage and would normally have succeeded in the title.
- `d9s6` Payne baronets [6]: However, he allowed his eldest brother John Payne to assume the title, although John was illegitimate.
- `d9s7` Payne baronets [7]: John died in 1803 when his son Charles assumed the title.
- `d9s8` Payne baronets [8]: However, in 1828 Peter Payne raised the question in the courts over who was the rightful baronet.
- `d9s9` Payne baronets [9]: The Court of Chancery declared that he was the rightful heir to his father, but this was overturned by the Lord Chancellor in 1829.
- `d9s10` Payne baronets [10]: Nonetheless, during his lifetime Sir Peter was universally acknowledged as a baronet.
- `d9s11` Payne baronets [11]: Most reference books on the British nobility and baronetage include the title, although they describe it as being in dispute between rival branches of the family.
- `d9s12` Payne baronets [12]: Charles Robert Salusbury Payne, the supposed sixth Baronet, appears to have discontinued the claim around 1900.
- `d10s0` Fannie Lee Chaney [0]: Fannie Lee Chaney (September 4, 1921 – May 22, 2007) was an American baker turned civil rights activist after her son James Chaney was murdered by the Ku Klux Klan during the 1964 Freedom Summer rides in Mississippi.

</details>

## Q242 — `hotpotqa_5ab8756755429934fafe6dd3` (revised draft)

> When was the American writer of the a series of four vampire-themed fantasy romance novels born?

Source answer: December 24, 1973

Gold final answer: December 24, 1973

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: American author of a series of four vampire-themed fantasy romance novels | false | Stephenie Meyer | — | [d10s0] | — |
| u2: date of birth of {u1} | true | December 24, 1973 | u1 | [d9s0] | — |

Evidence:

- `d9s0` Stephenie Meyer [0]: Stephenie Meyer (née Morgan; ; born December 24, 1973) is an American young adult fiction writer and film producer, best known for her vampire romance series "Twilight".
- `d10s0` Twilight (novel series) [0]: Twilight is a series of four vampire-themed fantasy romance novels by American author Stephenie Meyer.

Notes:

- 删除题干未给出的Twilight，避免描述提前泄漏中间信息。

<details><summary>All source context</summary>

- `d1s0` Eilis Flynn [0]: Eilis Flynn (b. Elizabeth Myrtle Smith, on a May 12 in Tacoma, Washington, United States), is an American author of four fantasy romance novels for the publisher, Cerridwen Press.
- `d1s1` Eilis Flynn [1]: She also has written for DC Comics using the name Elizabeth M. Smith.
- `d2s0` House of Night [0]: House of Night is a series of young adult vampire-themed fantasy novels by American author P. C. Cast and her daughter Kristin Cast.
- `d2s1` House of Night [1]: It follows the adventures of Zoey Redbird, a sixteen-year-old girl who has just become a "fledgling vampyre" and is required to attend the House of Night boarding school in Tulsa, Oklahoma.
- `d2s2` House of Night [2]: Books in the series have been on the "New York Times" Best Seller list for 63 weeks and have sold over seven million copies in North America, and more than ten million books worldwide, in 39 countries.
- `d2s3` House of Night [3]: The series, published by St Martin's Press, is planned to include thirteen books.
- `d3s0` Jane Feather [0]: Jane Feather, née "Jane Robotham" (born 1945 in Cairo, Egypt) is a popular British–American writer of historical romance novels.
- `d3s1` Jane Feather [1]: In 1984 she wrote five contemporary romances under the pseudonym Claudia Bishop.
- `d3s2` Jane Feather [2]: She now is a New York Times bestselling, award–winning writer and she has more than ten million romance novels in print.
- `d4s0` The Dark Heroine [0]: The Dark Heroine is a series of vampire-themed fantasy romance novels written by English author Abigail Gibbs, published by HarperCollins in 2012.
- `d4s1` The Dark Heroine [1]: The first novel in the series, "Dinner with a Vampire," revolves around London-born Violet Lee, who is kidnapped and held hostage by a Royal Family of vampires known as the Varns.
- `d4s2` The Dark Heroine [2]: The series is told from both Violet Lee and Kaspar Varn's perspective, the latter being heir to the Vamperic Throne in the novel.
- `d5s0` Harper Allen [0]: Harper Allen is a Canadian writer of contemporary and fantasy romance novels since 1998.
- `d6s0` Night Huntress [0]: Night Huntress is a series of "New York Times" bestselling urban fantasy romance novels by author Jeaniene Frost.
- `d6s1` Night Huntress [1]: The first novel was published in 2007 by Avon and takes place in a world where supernatural creatures exist but are not known to the general public at large.
- `d6s2` Night Huntress [2]: The series initially focused around the character of half-vampire Catherine "Cat" Crawfield and her full-vampire lover Bones, but eventually shifted focus to other characters such as Vlad Tepesh, a character that Frost had initially not planned to include.
- `d7s0` Sarah MacLean [0]: Sarah MacLean (born December 17, 1978) is a New York Times bestselling American author of young adult novels and romance novels.
- `d7s1` Sarah MacLean [1]: Her first adult romance novel, "Nine Rules to Break When Romancing a Rake" debuted on the New York Times Bestseller List, where it stayed for four weeks.
- `d7s2` Sarah MacLean [2]: Since then, all of her adult romance novels have been on the New York Times and USA Today bestseller lists.
- `d7s3` Sarah MacLean [3]: Since February 2014, MacLean has written a monthly romance novel review column for The Washington Post.
- `d7s4` Sarah MacLean [4]: She is a two-time winner of the Romance Writers of America RITA Award for Best Historical Romance for "A Rogue by Any Other Name" in 2013 and "No Good Duke Goes Unpunished" in 2014.
- `d8s0` Tagalog pocketbooks [0]: According to Tatin Yang in the article "Romansang Pinoy: A day with Tagalog romance novels", Tagalog romance paperbacks were thin Philippine versions of romance novel books that could be found at the bottom shelves of the romance section of bookstores, wrapped and bound with book covers that are decorated with Philippine comics-styled illustrations, such as "a barrio landscape with a badly dressed guy and girl locked in an embrace".
- `d8s1` Tagalog pocketbooks [1]: As a form of "escapist fiction" (escapism) and "commercial literature", Tagalog romance novels generally follow a "strict romance formula", meaning the narratives have happy endings (a factor influencing the salability of the novel), the protagonists are wealthy, good-looking, smart, and characters that cannot die.
- `d8s2` Tagalog pocketbooks [2]: Normally, the hero or heroine of the story falls in love and "goes crazy" over the admired person.
- `d8s3` Tagalog pocketbooks [3]: However, later authors of Tagalog romance novels deviated from portraying so-called "damsel-in-distress and knight-in-shining-armor characters".
- `d8s4` Tagalog pocketbooks [4]: Contemporary writers also turned away from writing "rags-to-riches plots".
- `d8s5` Tagalog pocketbooks [5]: The stereotypical norm had been replaced by the incorporation of storylines with "interesting scenes, characters [who are ready to face challenges or to sacrifice themselves for the benefit of other people], dialogues, and new angles to old plots".
- `d8s6` Tagalog pocketbooks [6]: Authors such as Maria Teresa Cruz San Diego, who used the pen names Maia Jose and Tisha Nicole, ventured into the fantasy romance genre, and into topics that are related to politics, ecology, gender issues, prostitution, mail-order bride syndicates, white slavery, non-governmental organizations, and breastfeeding programs.
- `d8s7` Tagalog pocketbooks [7]: Apart from writing about ideal lovers (men and women) and ideal situations, other novelists wrote about true-to-life settings, or at least based the stories from personal experiences.
- `d8s8` Tagalog pocketbooks [8]: Thus, Tagalog romance novels came to mirror or replicate the "roles that women and men play" in Philippine society.
- `d9s0` Stephenie Meyer [0]: Stephenie Meyer (née Morgan; ; born December 24, 1973) is an American young adult fiction writer and film producer, best known for her vampire romance series "Twilight".
- `d9s1` Stephenie Meyer [1]: The "Twilight" novels have gained worldwide recognition and sold over 100 million copies, with translations into 37 different languages.
- `d9s2` Stephenie Meyer [2]: Meyer was the bestselling author of 2008 and 2009 in America, having sold over 29 million books in 2008, and 26.5 million books in 2009.
- `d9s3` Stephenie Meyer [3]: "Twilight" was the best-selling book of 2008 in US bookstores.
- `d10s0` Twilight (novel series) [0]: Twilight is a series of four vampire-themed fantasy romance novels by American author Stephenie Meyer.
- `d10s1` Twilight (novel series) [1]: Released annually from 2005 through 2008, the four books chart the later teen years of Isabella "Bella" Swan, a girl who moves to Forks, Washington, and falls in love with a 104-year-old vampire named Edward Cullen.
- `d10s2` Twilight (novel series) [2]: The series is told primarily from Bella's point of view, with the epilogue of "Eclipse" and Part II of "Breaking Dawn" being told from the viewpoint of character Jacob Black, a werewolf.
- `d10s3` Twilight (novel series) [3]: The unpublished "Midnight Sun" is a retelling of the first book, "Twilight", from Edward Cullen's point of view.
- `d10s4` Twilight (novel series) [4]: The novella "The Short Second Life of Bree Tanner", which tells the story of a newborn vampire who appeared in "Eclipse", was published on June 5, 2010, as a hardcover book and on June 7 as a free online ebook. ""
- `d10s5` Twilight (novel series) [5]: , a definitive encyclopedic reference with nearly 100 full color illustrations, was released in bookstores on April 12, 2011.

</details>

## Q243 — `hotpotqa_5ab8b02d5542991b5579efdb` (revised draft)

> Are both, Boise State University and Syracuse University, public colleges?

Source answer: no

Gold final answer: no

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: institutional funding classification of Boise State University | false | public | — | [d1s0] | — |
| u2: institutional funding classification of Syracuse University | false | private | — | [d5s0] | — |
| u3: Are both, Boise State University and Syracuse University, public colleges? | true | no | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d1s0` Boise State University [0]: Boise State University (BSU) is a public college in Boise, Idaho.
- `d5s0` Syracuse University [0]: Syracuse University (commonly referred to as Syracuse, 'Cuse, or SU) is a private research university in Syracuse, New York, United States.

Notes:

- 将public or private答案选项从unit描述移至属性名institutional funding classification，避免SFT描述泄漏校验误判。
- 将public or private答案选项从unit描述移至属性名institutional funding classification，避免SFT描述泄漏校验误判。

<details><summary>All source context</summary>

- `d1s0` Boise State University [0]: Boise State University (BSU) is a public college in Boise, Idaho.
- `d1s1` Boise State University [1]: Founded in 1932 by the Episcopal Church, it became an independent junior college in 1934, and has been awarding baccalaureate and master's degrees since 1965.
- `d2s0` 2002 Boise State Broncos football team [0]: The 2002 Boise State Broncos football team represented Boise State University in the 2002 NCAA Division I-A football season.
- `d2s1` 2002 Boise State Broncos football team [1]: Boise State competed as a member of the Western Athletic Conference (WAC), and played their home games at Bronco Stadium in Boise, Idaho.
- `d2s2` 2002 Boise State Broncos football team [2]: The Broncos were led by second-year head coach Dan Hawkins.
- `d2s3` 2002 Boise State Broncos football team [3]: The Broncos finished the season 12–1 and 8–0 in conference to win their first WAC title and played in the Humanitarian Bowl, where they defeated Iowa State, 34–16.
- `d2s4` 2002 Boise State Broncos football team [4]: The 2002 marked the first season that Boise State was ranked in the top 25 since moving to Division I-A in 1996.
- `d3s0` Daryl Gross [0]: Daryl James Gross (born June 20, 1961) is currently the Executive Director of Intercollegiate Athletics at California State University, Los Angeles.
- `d3s1` Daryl Gross [1]: Prior to serving in this position, he was the Vice President and Special Assistant to the Chancellor at Syracuse University, in Syracuse, New York.
- `d3s2` Daryl Gross [2]: Previously, he was the school's athletic director.
- `d3s3` Daryl Gross [3]: In June 2015, the university announced that Mark Coyle, of Boise State, was hired to succeed Gross as athletic director.
- `d4s0` 2009–10 Boise State Broncos men's basketball team [0]: The 2009–10 Boise State Broncos men's basketball team represented Boise State University in the 2009–10 college basketball season.
- `d4s1` 2009–10 Boise State Broncos men's basketball team [1]: This was head coach Greg Graham's eighth and final season at Boise State as he was fired at the end of the season.
- `d4s2` 2009–10 Boise State Broncos men's basketball team [2]: The Broncos competed in the Western Athletic Conference and played their home games at the Taco Bell Arena.
- `d4s3` 2009–10 Boise State Broncos men's basketball team [3]: Boise State finished the season 15–17, 5–11 in WAC play and lost in the quarterfinals of the 2010 WAC Men's Basketball Tournament to Utah State.
- `d5s0` Syracuse University [0]: Syracuse University (commonly referred to as Syracuse, 'Cuse, or SU) is a private research university in Syracuse, New York, United States.
- `d5s1` Syracuse University [1]: The institution's roots can be traced to the Genesee Wesleyan Seminary (later becoming Genesee College), founded in 1831 by the Methodist Episcopal Church in Lima, New York.
- `d5s2` Syracuse University [2]: After several years of debate over relocating the college to Syracuse, the university was established in 1870, independent of the college.
- `d5s3` Syracuse University [3]: Since 1920, the university has identified itself as nonsectarian, although it maintains a relationship with The United Methodist Church.
- `d6s0` List of Boise State Broncos bowl games [0]: The Boise State Broncos college football team competes as part of the National Collegiate Athletic Association (NCAA) Division I Football Bowl Subdivision (FBS), representing Boise State University as members of the Mountain West Conference.
- `d6s1` List of Boise State Broncos bowl games [1]: Since the establishment of the team in 1932 (although joined Division I in 1971 and FBS in 1996), Boise State has appeared in 17 bowl games.
- `d6s2` List of Boise State Broncos bowl games [2]: The Broncos have appeared in eight different bowl games, with multiple appearances in the Humanitarian/MPC Computers Bowl (4), the Maaco Bowl Las Vegas (3), the Fiesta Bowl (3) (which was part of the Bowl Championship Series (BCS) and now part of the New Year's Six), the Hawaii Bowl (2), and the Poinsettia Bowl (2).
- `d6s3` List of Boise State Broncos bowl games [3]: Boise State was the only school from a non automatic qualifying conference to receive an at-large bid into a BCS game during the 2009 NCAA Division I FBS football season.
- `d6s4` List of Boise State Broncos bowl games [4]: They went to the 2010 Fiesta Bowl that season (all other appearances by non-AQ schools are actually automatic bids under BCS rules).
- `d6s5` List of Boise State Broncos bowl games [5]: With their most recent loss in the 2016 Cactus Bowl, Boise State has an overall bowl record of 11–6.
- `d7s0` Leon Rice (basketball) [0]: Leon Paul Rice (born November 25, 1963) is an American college basketball coach, and the head men's basketball coach at Boise State University.
- `d7s1` Leon Rice (basketball) [1]: Rice replaced Greg Graham as head coach of the Broncos on March 26, 2010.
- `d7s2` Leon Rice (basketball) [2]: In his first season as head coach, he led Boise State to the finals of the 2011 WAC Men's Basketball Tournament and to the semifinals of the 2011 College Basketball Invitational.
- `d7s3` Leon Rice (basketball) [3]: He is the first Boise State head coach to win 20 games in two of his first three seasons and has 20 or more wins in six of his first seven seasons.
- `d7s4` Leon Rice (basketball) [4]: In 2013, he guided the Broncos to their first ever at-large bid to the NCAA Tournament.
- `d7s5` Leon Rice (basketball) [5]: In 2015, he led the Broncos to their first ever Mountain West regular season championship, and first conference title for Boise State since 2008, and was named the Mountain West coach of the year.
- `d8s0` Greg Patton [0]: Greg Patton (born 1952) is a tennis coach, both nationally and at a collegiate level.
- `d8s1` Greg Patton [1]: He currently leads the nationally ranked Boise State Broncos of men's tennis program of Boise State University as their head coach.
- `d8s2` Greg Patton [2]: His career record at Boise State is 203-67.
- `d8s3` Greg Patton [3]: At Boise State, he has won seven conference championships in nine seasons in four different conferences (Big Sky, Big West, Western Athletic Conference, Mountain West).
- `d9s0` Boise State–Nevada football rivalry [0]: The Boise State–Nevada football rivalry is a college football rivalry between the Boise State Broncos football team of Boise State University and Nevada Wolf Pack football team of University of Nevada, Reno.
- `d9s1` Boise State–Nevada football rivalry [1]: The game has been played every year since 1971 with the exception of 1978, 1992, 1995, 2000, 2015 and 2016.
- `d9s2` Boise State–Nevada football rivalry [2]: The game was also played twice in 1990 as the second game was a Division I-AA semifinal playoff game, and to date has been the only post-season game played between the two programs.
- `d9s3` Boise State–Nevada football rivalry [3]: The series has mostly been a conference match-up, with the exception of the first seven games as well as the 1993, 1994, and 2011 games.
- `d9s4` Boise State–Nevada football rivalry [4]: Boise State and Nevada have faced each other as conference rivals in four separate conferences - the Big Sky Conference, Big West Conference, Western Athletic Conference and the Mountain West Conference.
- `d9s5` Boise State–Nevada football rivalry [5]: The two teams have played each other from the NCAA Division II level all the way up to the highest level of college football, NCAA Division I FBS.
- `d10s0` List of state universities in the United States [0]: In the United States, a state college or state university is one of the public colleges or universities funded by or associated with the state government.
- `d10s1` List of state universities in the United States [1]: In some cases, these institutions of higher learning are part of a state university system, while in other cases they are not.
- `d10s2` List of state universities in the United States [2]: Several U.S. territories also administer public colleges and universities.
- `d10s3` List of state universities in the United States [3]: The U.S. federal government does not run colleges or universities except for the service academies, the Community College of the Air Force, the Naval Postgraduate School, the Air Force Institute of Technology, the Uniformed Services University of the Health Sciences, military war colleges and staff colleges, and Haskell Indian Nations University.
- `d10s4` List of state universities in the United States [4]: Additionally, Georgetown University, Gallaudet University, Howard University, and American University are private universities that are federally chartered.
- `d10s5` List of state universities in the United States [5]: However, the federal government does make grants to state universities.

</details>

## Q244 — `hotpotqa_5ab9b4a555429970cfb8eb75` (revised draft)

> Is Rick Husband Amarillo International Airport or Grand Forks International Airport closer to the town it is near?

Source answer: Grand Forks International Airport

Gold final answer: Grand Forks International Airport

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: distance from Rick Husband Amarillo International Airport to downtown Amarillo | false | 6 miles | — | [d8s0] | — |
| u2: distance from Grand Forks International Airport to Grand Forks | false | 5 miles | — | [d7s0] | — |
| u3: Is Rick Husband Amarillo International Airport or Grand Forks International Airport closer to the town it is near? | true | Grand Forks International Airport | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d7s0` Grand Forks International Airport [0]: Grand Forks International Airport (IATA: GFK, ICAO: KGFK, FAA LID: GFK) is a public airport five miles (8 km) northwest of Grand Forks, in Grand Forks County, North Dakota.
- `d8s0` Rick Husband Amarillo International Airport [0]: Rick Husband Amarillo International Airport (IATA: AMA, ICAO: KAMA, FAA LID: AMA) is a public airport six miles (10 km) east of downtown Amarillo, in Potter and Randall Counties, Texas, United States.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Downtown Grand Forks [0]: Downtown Grand Forks is the original commercial center of Grand Forks, North Dakota.
- `d1s1` Downtown Grand Forks [1]: Located on the western bank of the Red River of the North, the downtown neighborhood is situated near the fork of the Red River and the Red Lake River.
- `d1s2` Downtown Grand Forks [2]: While downtown is no longer the dominant commercial area of the Greater Grand Forks community, it remains the historic center of Grand Forks.
- `d1s3` Downtown Grand Forks [3]: An 80.4 acre portion was listed on the National Register of Historic Places in 2005, as Downtown Grand Forks Historic District.
- `d1s4` Downtown Grand Forks [4]: Today, downtown Grand Forks is home to many offices, stores, restaurants, and bars.
- `d2s0` Red Lake River [0]: The Red Lake River (French: "Rivière du Lac Rouge"; Ojibwe: "Miskwaagamiiwi-zaaga'iganiiwi-ziibi") is a river located in northwestern Minnesota.
- `d2s1` Red Lake River [1]: The river begins on the western side of the Lower Red Lake and flows westward.
- `d2s2` Red Lake River [2]: After passing through Thief River Falls, Red Lake Falls, and Crookston, the river merges with the Red River of the North in East Grand Forks.
- `d2s3` Red Lake River [3]: The total length of the river is 193 miles (310.6 km).
- `d2s4` Red Lake River [4]: The term "Forks" in Grand Forks comes from this forking (confluence) of the Red and Red Lake rivers near downtown Grand Forks.
- `d3s0` Texas Air &amp; Space Museum [0]: The Texas Air & Space Museum is an aviation museum located near Rick Husband Amarillo International Airport in Amarillo, Texas.
- `d3s1` Texas Air &amp; Space Museum [1]: The museum displays civilian and military aircraft as well as a wide range of air and space artifacts.
- `d4s0` Grand Forks International [0]: The Grand Forks International (GFI) is an annual international invitational baseball tournament hosted at James Donaldson Park in Grand Forks, British Columbia.
- `d4s1` Grand Forks International [1]: The GFI is the largest invitational baseball tournament in Canada and is a large part of the culture in Grand Forks.
- `d4s2` Grand Forks International [2]: The tournament is also notable for being run entirely by volunteers.
- `d5s0` Grand Sky [0]: Grand Sky is an UAS (unmanned aerial systems)-specific business and aviation park located at Grand Forks Air Force Base near Grand Forks, North Dakota.
- `d5s1` Grand Sky [1]: A groundbreaking for the development was held in September 2015, making it the first UAS business and aviation park in the U.S.
- `d5s2` Grand Sky [2]: The park consists of 217 acres and includes access to the Grand Forks Air Force Base runway for large UAS flights.
- `d6s0` Grand Forks Municipal Airport [0]: Grand Forks Municipal Airport is a former airport, located within current city limits approximately 3 mi west-northwest of central Grand Forks, North Dakota.
- `d6s1` Grand Forks Municipal Airport [1]: It was closed shortly after World War II and is now redeveloped as part of the urban area of Grand Forks.
- `d7s0` Grand Forks International Airport [0]: Grand Forks International Airport (IATA: GFK, ICAO: KGFK, FAA LID: GFK) is a public airport five miles (8 km) northwest of Grand Forks, in Grand Forks County, North Dakota.
- `d7s1` Grand Forks International Airport [1]: GFK has no scheduled passenger flights out of the country but has an "international" title (like many other airports) because it has customs service for arrivals from Canada and other countries.
- `d8s0` Rick Husband Amarillo International Airport [0]: Rick Husband Amarillo International Airport (IATA: AMA, ICAO: KAMA, FAA LID: AMA) is a public airport six miles (10 km) east of downtown Amarillo, in Potter and Randall Counties, Texas, United States.
- `d8s1` Rick Husband Amarillo International Airport [1]: The airport was renamed in 2003 after NASA astronaut and Amarillo native Rick Husband, who died in the Space Shuttle "Columbia" disaster in February of that year.
- `d9s0` Emerado, North Dakota [0]: Emerado is a city in Grand Forks County, North Dakota, United States located near Grand Forks Air Force Base.
- `d9s1` Emerado, North Dakota [1]: It is part of the "Grand Forks, ND-MN Metropolitan Statistical Area" or "Greater Grand Forks".
- `d9s2` Emerado, North Dakota [2]: The population was 414 at the 2010 census.
- `d9s3` Emerado, North Dakota [3]: Grand Forks Air Force Base is located near Emerado.
- `d10s0` John D. Odegard School of Aerospace Sciences [0]: The John D. Odegard School of Aerospace Sciences (UND Aerospace) is a multidisciplinary college within the University of North Dakota (UND) in Grand Forks, North Dakota.
- `d10s1` John D. Odegard School of Aerospace Sciences [1]: The school was formed in 1968.
- `d10s2` John D. Odegard School of Aerospace Sciences [2]: The majority of the school's fleet of over 120 aircraft is based at nearby Grand Forks International Airport and is the largest fleet of civilian flight training aircraft in North America.
- `d10s3` John D. Odegard School of Aerospace Sciences [3]: UND Aerospace also operates flight training centers in Crookston, Minnesota, and Phoenix, Arizona.
- `d10s4` John D. Odegard School of Aerospace Sciences [4]: Today, the school has many aerospace-related programs including commercial aviation (fixed wing and rotorcraft), air traffic control, airport management, Space Studies, Computer Science, Atmospheric Sciences, and Earth System Science & Policy.
- `d10s5` John D. Odegard School of Aerospace Sciences [5]: Currently, the school has over 500 faculty and 1,900 students making it the second largest of UND’s degree-granting colleges.
- `d10s6` John D. Odegard School of Aerospace Sciences [6]: The present dean of the school is Dr. Paul Lindseth.

</details>

## Q245 — `hotpotqa_5ab9df1f554299232ef4a239` (revised draft)

> Jasmin Geljo is known for his role in a 2005 post-apocalyptic horror film written and directed by who?

Source answer: George A. Romero

Gold final answer: George A. Romero

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: 2005 post-apocalyptic horror film featuring Jasmin Geljo | false | Land of the Dead | — | [d9s1, d2s0] | — |
| u2: writer and director of {u1} | true | George A. Romero | u1 | [d2s0] | — |

Evidence:

- `d2s0` Land of the Dead [0]: Land of the Dead (also known as George A. Romero's Land of the Dead) is a 2005 post-apocalyptic horror film written and directed by George A. Romero; the fourth of Romero's six "Living Dead" movies, it is preceded by "Night of the Living Dead", "Dawn of the Dead" and "Day of the Dead", and succeeded by "Diary of the Dead" and "Survival of the Dead".
- `d9s1` Jasmin Geljo [1]: He is best known for his roles on Cube Zero as Ryjkin and in the films "Land of the Dead", "Assault on Precinct 13" and "The Sentinel".

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Maggie (film) [0]: Maggie is a 2015 post-apocalyptic horror drama film directed by Henry Hobson, in his directorial debut, written by John Scott 3, and starring Arnold Schwarzenegger, Abigail Breslin and Joely Richardson.
- `d1s1` Maggie (film) [1]: "Maggie" is a dramatic departure for Schwarzenegger, who is better known for his action film roles.
- `d2s0` Land of the Dead [0]: Land of the Dead (also known as George A. Romero's Land of the Dead) is a 2005 post-apocalyptic horror film written and directed by George A. Romero; the fourth of Romero's six "Living Dead" movies, it is preceded by "Night of the Living Dead", "Dawn of the Dead" and "Day of the Dead", and succeeded by "Diary of the Dead" and "Survival of the Dead".
- `d2s1` Land of the Dead [1]: It was released in 2005, with a budget of $15–19 million, the highest in the series, and became a success, grossing over $46 million.
- `d3s0` Viman [0]: Viman (Tamil: விமான்) is an upcoming Malaysian Tamil supernatural film written & directed by A.M. Kishok, produced by Avaraa Creationz, co-produced by Garuda Utama Production, had musical score by Daddy Shaq and choreographed by Vassan Kumaran.
- `d3s1` Viman [1]: Starring Kishok in the lead role with Jasmin Michael.The film revolves around a middle-aged man and the mysterious happenings in him with one objective, one mission and vision.
- `d3s2` Viman [2]: The film was set to release on 2016.
- `d4s0` Remains (film) [0]: Remains, also billed as Steve Niles' Remains, is a 2011 post-apocalyptic horror film.
- `d4s1` Remains (film) [1]: It depicts a small group of people in a Reno, Nevada casino who have survived a nuclear disaster while the rest of humanity has been turned into flesh eating zombies.
- `d4s2` Remains (film) [2]: It was produced by the Chiller Network and is based on the comic book series of the same name.
- `d5s0` Extinction (2015 film) [0]: Extinction (formerly known as Welcome to Harmony) is a 2015 post-apocalyptic horror film directed by Miguel Ángel Vivas who also co-wrote the screenplay with Alberto Marini from the novel "Y pese a todo" by Juan de Dios Garduño.
- `d5s1` Extinction (2015 film) [1]: The film stars Matthew Fox, Jeffrey Donovan and Quinn McColgan.
- `d5s2` Extinction (2015 film) [2]: In a post-apocalypse future, three survivors confront issues from their past, as well as a race of crazed zombies.
- `d5s3` Extinction (2015 film) [3]: The film was released on July 31, 2015 in the United States.
- `d6s0` The Divide (2011 film) [0]: The Divide is a post-apocalyptic horror film directed by Xavier Gens and written by Karl Mueller and Eron Sheean.
- `d6s1` The Divide (2011 film) [1]: It stars Michael Biehn, Lauren German, Milo Ventimiglia and Rosanna Arquette.
- `d6s2` The Divide (2011 film) [2]: "The Divide" was first screened at the SXSW festival in March 2011, then released in theaters in the United States on January 13, 2012 to negative reviews.
- `d6s3` The Divide (2011 film) [3]: It was released on DVD in the United States on April 17, 2012.
- `d7s0` Andrew Lincoln [0]: Andrew James Clutterbuck (born 14 September 1973), better known by his stage name Andrew Lincoln, is an English actor.
- `d7s1` Andrew Lincoln [1]: He is most recognised for his portrayal of Rick Grimes, the lead character in the AMC post-apocalyptic horror television series—based on the eponymous comic book series of the same name—"The Walking Dead".
- `d7s2` Andrew Lincoln [2]: His first major role was in the BBC drama "This Life", followed by roles such as Simon Casey in the Channel 4 sitcom "Teachers" and Mark in the Christmas-themed romantic comedy film "Love Actually" (2003).
- `d8s0` 28 Days Later [0]: 28 Days Later is a 2002 British post-apocalyptic horror film directed by Danny Boyle, written by Alex Garland, and starring Cillian Murphy, Naomie Harris, Brendan Gleeson, Megan Burns, and Christopher Eccleston.
- `d8s1` 28 Days Later [1]: The plot depicts the breakdown of society following the accidental release of a highly contagious virus and focuses upon the struggle of four survivors to cope with the destruction of the life they once knew.
- `d9s0` Jasmin Geljo [0]: Jasmin Geljo (born September 18, 1959) is a Bosnian-Canadian actor.
- `d9s1` Jasmin Geljo [1]: He is best known for his roles on Cube Zero as Ryjkin and in the films "Land of the Dead", "Assault on Precinct 13" and "The Sentinel".
- `d10s0` The Walking Dead (season 1) [0]: The first season of "The Walking Dead", an American post-apocalyptic horror television series on AMC, premiered on October 31, 2010, and concluded on December 5, 2010, consisting of 6 episodes.
- `d10s1` The Walking Dead (season 1) [1]: Developed for television by Frank Darabont, who wrote or co-wrote four of the season's six episodes and directed the pilot episode, "Days Gone Bye", the series is based on the eponymous series of comic books by Robert Kirkman, Tony Moore, and Charlie Adlard.
- `d10s2` The Walking Dead (season 1) [2]: It was executive produced by Darabont, Kirkman, David Alpert, Charles H. Eglee, and Gale Anne Hurd, with Darabont assuming the role of showrunner.

</details>

## Q246 — `hotpotqa_5aba637a55429939ce03dcbb` (revised draft)

> Are Brooklyn and Tower 49 both part of New York City?

Source answer: yes

Gold final answer: yes

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: city containing Brooklyn | false | New York City | — | [d7s0] OR [d2s0] OR [d4s0] OR [d5s0] OR [d10s0] | — |
| u2: city containing Tower 49 | false | New York City | — | [d3s0] | — |
| u3: Are Brooklyn and Tower 49 both part of New York City? | true | yes | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d2s0` Brooklyn Heights [0]: Brooklyn Heights is an affluent residential neighborhood within the New York City borough of Brooklyn.
- `d3s0` Tower 49 [0]: Tower 49 is an office skyscraper in the Midtown Manhattan district of New York City.
- `d4s0` Fulton Street Line (elevated) [0]: The Fulton Street Line, also called the Fulton Street Elevated or Kings County Line, was an elevated rail line mostly in Brooklyn, New York City, United States.
- `d5s0` East New York, Brooklyn [0]: East New York is a residential neighborhood in the eastern section of the borough of Brooklyn in New York City, United States.
- `d7s0` Brooklyn [0]: Brooklyn ( ) is the most populous borough of New York City, with a Census-estimated 2,629,150 residents in 2016.
- `d10s0` Fort Greene, Brooklyn [0]: Fort Greene is a neighborhood in the New York City borough of Brooklyn.

Notes:

- 补齐四条Brooklyn属于New York City的明确备选证据。

<details><summary>All source context</summary>

- `d1s0` List of bus routes in Brooklyn [0]: The Metropolitan Transportation Authority (MTA) operates a number of bus routes in Brooklyn, New York, United States; one minor route is privately operated under a city franchise.
- `d1s1` List of bus routes in Brooklyn [1]: Many of them are the direct descendants of streetcar lines (see list of streetcar lines in Brooklyn); the ones that started out as bus routes were almost all operated by the Brooklyn Bus Corporation, a subsidiary of the Brooklyn–Manhattan Transit Corporation, until the New York City Board of Transportation took over on June 5, 1940.
- `d1s2` List of bus routes in Brooklyn [2]: Of the 55 local Brooklyn routes operated by the New York City Transit Authority, roughly 35 are the direct descendants of one or more streetcar lines, and most of the others were introduced in full or in part as new bus routes by the 1930s.
- `d1s3` List of bus routes in Brooklyn [3]: Only the eastern section of the B82 (then the B50), the B83, and the B84 were created by New York City Transit from scratch, in 1978, 1966, and 2013, respectively.
- `d2s0` Brooklyn Heights [0]: Brooklyn Heights is an affluent residential neighborhood within the New York City borough of Brooklyn.
- `d2s1` Brooklyn Heights [1]: Originally referred to as Brooklyn Village, it has been a prominent area of Brooklyn since 1834.
- `d2s2` Brooklyn Heights [2]: The neighborhood is noted for its low-rise architecture and its many brownstone rowhouses, most of them built prior to the Civil War.
- `d2s3` Brooklyn Heights [3]: It also has an abundance of notable churches and other religious institutions.
- `d2s4` Brooklyn Heights [4]: Brooklyn's first art gallery, the Brooklyn Arts Gallery, was opened in Brooklyn Heights in 1958.
- `d2s5` Brooklyn Heights [5]: In 1965, a large part of Brooklyn Heights was protected from unchecked development by the creation of the Brooklyn Heights Historic District, the first such district in New York City.
- `d2s6` Brooklyn Heights [6]: The district was added to the National Register of Historic Places in 1966.
- `d3s0` Tower 49 [0]: Tower 49 is an office skyscraper in the Midtown Manhattan district of New York City.
- `d3s1` Tower 49 [1]: The lot is fronted on both 48th Street and 49th Street between 5th Avenue and Madison Avenue.
- `d3s2` Tower 49 [2]: The street frontages were offset by about the width of an NYC brownstone lot on both sides.
- `d4s0` Fulton Street Line (elevated) [0]: The Fulton Street Line, also called the Fulton Street Elevated or Kings County Line, was an elevated rail line mostly in Brooklyn, New York City, United States.
- `d4s1` Fulton Street Line (elevated) [1]: It ran above Fulton Street from Fulton Ferry, Brooklyn in Downtown Brooklyn east to East New York, and then south on Van Sinderen Avenue (southbound) and Snediker Avenue (northbound), east on Pitkin Avenue, north on Euclid Avenue, and east on Liberty Avenue to Ozone Park, Queens.
- `d4s2` Fulton Street Line (elevated) [2]: The portion in Brooklyn has been torn down, but most of the line in Queens has been connected to the New York City Subway and is now part of the IND Fulton Street Line (a portion of the A and C), an underground line that replaced the elevated line in Brooklyn.
- `d4s3` Fulton Street Line (elevated) [3]: The structure was the main line of the Kings County Elevated Railway, first opened in 1888.
- `d5s0` East New York, Brooklyn [0]: East New York is a residential neighborhood in the eastern section of the borough of Brooklyn in New York City, United States.
- `d5s1` East New York, Brooklyn [1]: The neighborhood is part of Brooklyn Community District 5, covered by Brooklyn Community Board 5.
- `d5s2` East New York, Brooklyn [2]: Its boundaries, starting from the north and moving clockwise are: Cypress Hills Cemetery to the north, the Borough of Queens to the east, Jamaica Bay to the south, and the Bay Ridge Branch railway tracks next to Van Sinderen Avenue to the west.
- `d5s3` East New York, Brooklyn [3]: Linden Boulevard and Atlantic Avenue are the primary thoroughfares through East New York.
- `d5s4` East New York, Brooklyn [4]: Its ZIP Codes include 11207, 11208, and 11239.
- `d5s5` East New York, Brooklyn [5]: The area is patrolled by the 75th Precinct located at 1000 Sutter Avenue.
- `d5s6` East New York, Brooklyn [6]: New York City Housing Authority (NYCHA) property in the area is patrolled by P.S.A. 2.
- `d5s7` East New York, Brooklyn [7]: During the latter part of the twentieth century, East New York came to be predominantly inhabited by African Americans and Latinos.
- `d6s0` One Worldwide Plaza [0]: One Worldwide Plaza is the largest tower of a three-building, mixed-use commercial and residential complex completed in 1989, in the New York City borough of Manhattan, known collectively as Worldwide Plaza.
- `d6s1` One Worldwide Plaza [1]: One Worldwide Plaza is a commercial office tower on Eighth Avenue.
- `d6s2` One Worldwide Plaza [2]: Two Worldwide Plaza is a residential condominium tower west of the center of the block, and Three Worldwide Plaza is a low-rise condominium residential building with street level stores on Ninth Avenue, to the west of the towers.
- `d6s3` One Worldwide Plaza [3]: Skidmore, Owings & Merrill was the designer for the office complex, and the residential complex was designed by Frank Williams.
- `d6s4` One Worldwide Plaza [4]: The complex, whose component skyscrapers are among the list of tallest buildings in New York City, occupies an entire city block, bounded by Eighth Avenue, Ninth Avenue, 49th Street, and 50th Street.
- `d6s5` One Worldwide Plaza [5]: Located on the west side of Eighth Avenue, One Worldwide Plaza is built on the site of New York City's third Madison Square Garden.
- `d7s0` Brooklyn [0]: Brooklyn ( ) is the most populous borough of New York City, with a Census-estimated 2,629,150 residents in 2016.
- `d7s1` Brooklyn [1]: It borders the borough of Queens at the southwestern end of Long Island, and has several bridge connections to the nearby boroughs of Staten Island and Manhattan.
- `d7s2` Brooklyn [2]: Since 1896, Brooklyn has had the same boundaries as Kings County, the most populous county in the U.S. state of New York and the second-most densely populated county in the United States, after the county of New York (which is coextensive with the borough of Manhattan).
- `d8s0` Queens [0]: Queens is the easternmost and largest in area of the five boroughs of New York City.
- `d8s1` Queens [1]: It is geographically adjacent to the borough of Brooklyn at the southwestern end of Long Island, and to Nassau County farther east on Long Island; in addition, Queens shares water borders with the boroughs of Manhattan and the Bronx.
- `d8s2` Queens [2]: Coterminous with Queens County since 1899, the borough of Queens is the second-largest in population (after Brooklyn), with a census-estimated 2,333,054 residents in 2016, approximately 48% of them foreign-born.
- `d8s3` Queens [3]: Queens County also is the second-most populous county in the U.S. state of New York, behind the neighboring borough of Brooklyn, which is coterminous with Kings County.
- `d8s4` Queens [4]: Queens is the fourth-most densely populated county among New York City's boroughs, as well as in the United States.
- `d8s5` Queens [5]: If each of New York City's boroughs were an independent city, Queens also would be the nation's fourth most populous, after Los Angeles, Chicago, and Brooklyn.
- `d8s6` Queens [6]: Queens is the most ethnically diverse urban area in the world.
- `d9s0` John W. Hunter [0]: John Ward Hunter (October 15, 1807 – April 16, 1900) was a United States Representative from New York.
- `d9s1` John W. Hunter [1]: Born in Bedford (now known as Bedford Stuyvesant), New York (now part of Brooklyn), he received a liberal schooling and was a clerk in a wholesale grocery store in New York City in 1824.
- `d9s2` John W. Hunter [2]: He was a clerk in the U.S. Custom House at New York City from 1831 to 1836, and was assistant auditor of the customhouse from 1836 to 1865.
- `d9s3` John W. Hunter [3]: He engaged in banking as treasurer of the Dime Savings Bank in Brooklyn, and was elected as a Democrat to the Thirty-ninth Congress to fill the vacancy caused by the death of James Humphrey.
- `d9s4` John W. Hunter [4]: Hunter held office from December 4, 1866 to March 3, 1867; while in Congress, he was censured by the House of Representatives on January 26, 1867 for the use of unparliamentary language.
- `d9s5` John W. Hunter [5]: He was not a candidate for renomination in 1866; in 1875 and 1876 he was mayor of Brooklyn.
- `d9s6` John W. Hunter [6]: His successor as mayor was Frederick A. Schroeder, a Republican.
- `d9s7` John W. Hunter [7]: Hunter was elected the first President of the Society of Old" "Brooklynites.
- `d9s8` John W. Hunter [8]: The prestigious civic organization which was founded in 1880, still holds monthly public meetings in the Brooklyn Surrogate's Courtroom.
- `d10s0` Fort Greene, Brooklyn [0]: Fort Greene is a neighborhood in the New York City borough of Brooklyn.
- `d10s1` Fort Greene, Brooklyn [1]: Part of Brooklyn Community Board 2 and served by the New York City Police Department's 88th Precinct, Fort Greene is listed on the New York State Registry and on the National Register of Historic Places, and is a New York City–designated Historic District.
- `d10s2` Fort Greene, Brooklyn [2]: It is located in northwest Brooklyn in the area known as South Brooklyn, just across from Lower Manhattan and north of Prospect Park.

</details>

## Q247 — `hotpotqa_5a89eca455429946c8d6ea11` (revised draft)

> Was Beyond the Gates of Splendor or Jesus Camp released first?

Source answer: Beyond the Gates of Splendor

Gold final answer: Beyond the Gates of Splendor

Question type: `comparison` (source type `comparison`)

Replaces: `hotpotqa_5aba74ad55429955dce3ee35`

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: film year of Beyond the Gates of Splendor | false | 2004 | — | [d6s0] | — |
| u2: film year of Jesus Camp | false | 2006 | — | [d8s0] | — |
| u3: Was Beyond the Gates of Splendor or Jesus Camp released first? | true | Beyond the Gates of Splendor | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d6s0` Beyond the Gates of Splendor [0]: Beyond the Gates of Splendor (also Beyond the Gates) is a feature-length documentary film that was released in 2004.
- `d8s0` Jesus Camp [0]: Jesus Camp is a 2006 American documentary film directed by Rachel Grady and Heidi Ewing about a Charismatic Christian summer camp, where children spend their summers being taught that they have "prophetic gifts" and can "take back America for Christ".

Notes:

- 替换：Ural上下文未说明公立性质；前身名称不能补出合并后性质。 新题保留原source type，人工核对两条显式事实及答案。

<details><summary>All source context</summary>

- `d1s0` Abandoned to God [0]: Abandoned to God is a Contemporary Christian music album released by Steve Camp in 1999.
- `d1s1` Abandoned to God [1]: This was the only album Camp released on the small Ministry Music label, and was released a year after Camp publicized his "107 Theses" that he felt were needed for reformation in the contemporary Christian music industry.
- `d1s2` Abandoned to God [2]: This album also features a then-little known Natalie Grant as a background vocalist.
- `d1s3` Abandoned to God [3]: This is also the first album since Consider the Cost in 1991 that did not feature a remake of an earlier song.
- `d1s4` Abandoned to God [4]: "Pledge My Head To Heaven" is a song originally performed by Keith Green, written for his 1980 album, So You Wanna Go Back To Egypt.
- `d2s0` Becky Fischer [0]: Becky Fischer (born May 31, 1951) is a Pentecostal children's pastor best known for her role in the 2006 documentary "Jesus Camp".
- `d3s0` Kids on Fire School of Ministry [0]: Kids on Fire School of Ministry was a Pentecostal summer camp at Devils Lake, North Dakota, United States.
- `d3s1` Kids on Fire School of Ministry [1]: It is the setting of the Academy Award nominated documentary "Jesus Camp".
- `d3s2` Kids on Fire School of Ministry [2]: The camp was run by the Reverend Becky Fischer.
- `d4s0` Through Gates of Splendor [0]: Through Gates of Splendor is a 1957 best selling book written by Elisabeth Elliot.
- `d4s1` Through Gates of Splendor [1]: The book tells the story of Operation Auca, an attempt by five American missionaries – Jim Elliot (the author's husband), Pete Fleming, Ed McCully, Nate Saint, and Roger Youderian – to reach the Huaorani tribe of eastern Ecuador.
- `d4s2` Through Gates of Splendor [2]: All five of the men were killed by the tribe.
- `d4s3` Through Gates of Splendor [3]: The book is Elliot's first book, and arguably her most well known work.
- `d5s0` Miss HIV [0]: Miss HIV is a feature-length documentary by Ethnographic Media, released to DVD on August 26, 2008.
- `d5s1` Miss HIV [1]: Written and directed by Jim Hanon (Beyond the Gates of Splendor, End of the Spear), and produced by Mart Green, the film explores the international collision of HIV/AIDS policies while following the journey of two HIV-positive women who enter a pageant in Botswana.
- `d5s2` Miss HIV [2]: What is happening in Botswana, where half of all pregnant women are HIV positive, is set contrasted with the past successes of Uganda, which has experienced one of the largest reductions in HIV infections ever recorded.
- `d6s0` Beyond the Gates of Splendor [0]: Beyond the Gates of Splendor (also Beyond the Gates) is a feature-length documentary film that was released in 2004.
- `d6s1` Beyond the Gates of Splendor [1]: It chronicles the events leading up to and following Operation Auca, an attempt to contact the Huaorani tribe of Ecuador in which five American missionaries were killed.
- `d6s2` Beyond the Gates of Splendor [2]: The film was produced by Bearing Fruit Productions and distributed by Every Tribe Entertainment.
- `d7s0` It's a Dying World [0]: It's a Dying World is a Contemporary Christian Music album by Steve Camp and was released by Myrrh Records in 1984.
- `d7s1` It's a Dying World [1]: This was Camp's final album for Myrrh Records, but was not released until after Camp released "Fire and Ice" with Sparrow in late 1983.
- `d8s0` Jesus Camp [0]: Jesus Camp is a 2006 American documentary film directed by Rachel Grady and Heidi Ewing about a Charismatic Christian summer camp, where children spend their summers being taught that they have "prophetic gifts" and can "take back America for Christ".
- `d8s1` Jesus Camp [1]: According to the distributor, it "doesn't come with any prepackaged point of view" and attempts to be "an honest and impartial depiction of one faction of the evangelical Christian community".
- `d9s0` Beyond the Gates (Possessed album) [0]: Beyond the Gates is the second and final album by death metal band Possessed.
- `d9s1` Beyond the Gates (Possessed album) [1]: It took a different direction from their debut, "Seven Churches".
- `d9s2` Beyond the Gates (Possessed album) [2]: Compared to "Seven Churches", "Beyond the Gates" has a more technical feeling and, due to poor production, a muddy sound.
- `d9s3` Beyond the Gates (Possessed album) [3]: Reception was mixed, with some very disappointed by the album for the sound and production, while others were happy with the new direction of the band.
- `d9s4` Beyond the Gates (Possessed album) [4]: "Beyond the Gates" became a sign of Possessed's decline, as they only released the EP "The Eyes of Horror" before they officially disbanded.
- `d10s0` Heidi Ewing [0]: Heidi Ewing is a director, producer, and writer of documentary films.
- `d10s1` Heidi Ewing [1]: She and Rachel Grady founded Loki Films in 2001, and have collaborated on several documentaries together.
- `d10s2` Heidi Ewing [2]: She is best known as the co-director of "Jesus Camp", which was nominated for an Academy Award for best documentary in 2006.
- `d10s3` Heidi Ewing [3]: Next came"12th & Delaware" (HBO), which premiered at the 2010 Sundance Film Festival.
- `d10s4` Heidi Ewing [4]: The film "casts a heart-rending light on the abortion divide" (LA Times) and was honored with a Peabody Award.
- `d10s5` Heidi Ewing [5]: "Detropia", a poetic look at Ewing's home town, also won several awards, including Best Editing at Sundance 2012, Outstanding Direction and Outstanding Original Score, at the 2013 Cinema Eye Honors for Nonfiction Filmmaking and a News and Documentary Emmy for editing.
- `d10s6` Heidi Ewing [6]: "Norman Lear: Just Another Version of You" was the opening night selection of the 2016 Sundance Film Festival and premiered on PBS American Masters on October 25, 2016.
- `d10s7` Heidi Ewing [7]: Other films as a director include "The Boys of Baraka", "Freakonomics", and "The Education of Mohammed Hussein".

</details>

## Q248 — `hotpotqa_5abaee4f5542996cc5e49f15` (revised draft)

> Were Cinderella and The Emperor's New Groove released by the same picture company?

Source answer: no

Gold final answer: no

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: original releasing company of Cinderella | false | RKO Radio Pictures | — | [d4s0] | — |
| u2: releasing company of The Emperor's New Groove | false | Walt Disney Pictures | — | [d7s0] | — |
| u3: Were Cinderella and The Emperor's New Groove released by the same picture company? | true | no | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d4s0` Cinderella (1950 film) [0]: Cinderella is a 1950 American animated musical fantasy film produced by Walt Disney and originally released by RKO Radio Pictures.
- `d7s0` The Emperor's New Groove [0]: The Emperor's New Groove is a 2000 American animated buddy comedy film created by Walt Disney Feature Animation and released by Walt Disney Pictures.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Man's Heart [0]: Man's Heart () is a tragedy silent film about the overseas Chinese community in tin mining industry, which was produced and released in 1928, presented by the "Kwong Kwong Motion Picture Company ()", which was located in Seremban, Negeri Sembilan state.
- `d1s1` Man's Heart [1]: its film crew and shooting equipments are coming from the past "Nanyang Low Pui-kim's Self-made "Motion Picture Company ()" in Singapore.
- `d2s0` The Emperor's New Groove (soundtrack) [0]: The Emperor's New Groove is the soundtrack to the 2000 Disney film "The Emperor's New Groove".
- `d2s1` The Emperor's New Groove (soundtrack) [1]: It features vocal performances by Shawn Colvin, Tom Jones, Eartha Kitt, Rascal Flatts, and Sting.
- `d2s2` The Emperor's New Groove (soundtrack) [2]: The album was released in 2000 by Walt Disney Records.
- `d2s3` The Emperor's New Groove (soundtrack) [3]: The music is by Sting and David Hartley, and the score is by John Debney.
- `d2s4` The Emperor's New Groove (soundtrack) [4]: The album included many songs that were written for "Kingdom of the Sun", the original incarnation for the project.
- `d2s5` The Emperor's New Groove (soundtrack) [5]: It also included Spanish and Italian versions of "My Funny Friend and Me".
- `d3s0` My Funny Friend and Me [0]: "My Funny Friend and Me" is a song by English musician Sting.
- `d3s1` My Funny Friend and Me [1]: It was written by Sting and David Hartley for Walt Disney Pictures' 40th animated feature film "The Emperor's New Groove".
- `d3s2` My Funny Friend and Me [2]: When the film began development in 1994 under the title "Kingdom of the Sun", Sting was hired to write the film's songs.
- `d3s3` My Funny Friend and Me [3]: Released in November 2000, the track reached 24 on the American "Billboard" Adult Contemporary Singles chart, and was nominated for the Academy Award for Best Original Song at the 73rd Academy Awards in 2001.
- `d4s0` Cinderella (1950 film) [0]: Cinderella is a 1950 American animated musical fantasy film produced by Walt Disney and originally released by RKO Radio Pictures.
- `d4s1` Cinderella (1950 film) [1]: Based on the fairy tale "Cinderella" by Charles Perrault, it is the twelfth Disney animated feature film.
- `d4s2` Cinderella (1950 film) [2]: Directing credits go to Clyde Geronimi, Hamilton Luske, and Wilfred Jackson.
- `d4s3` Cinderella (1950 film) [3]: Songs were written by Mack David, Jerry Livingston, and Al Hoffman.
- `d4s4` Cinderella (1950 film) [4]: Songs in the film include "Cinderella", "A Dream is a Wish Your Heart Makes", "Sing Sweet Nightingale", "The Work Song", "Bibbidi-Bobbidi-Boo", and "So This is Love".
- `d4s5` Cinderella (1950 film) [5]: It features the voices of Ilene Woods, Eleanor Audley, Verna Felton, Rhoda Williams, James MacDonald, Luis van Rooten, Don Barclay, Mike Douglas, and Lucille Bliss.
- `d5s0` List of The Emperor's New Groove characters [0]: The following are fictional characters from Disney's 2000 film "The Emperor's New Groove", its direct-to-video sequel "Kronk's New Groove", and the spin-off television series "The Emperor's New School".
- `d6s0` The Emperor's New School [0]: The Emperor's New School is an American animated television series on Disney Channel, based on the 2000 film "The Emperor's New Groove".
- `d6s1` The Emperor's New School [1]: It follows the adventures of a temporarily-dethroned Kuzco as he completes his education in order to return to the throne, while Yzma, as the school's principal, will stop at nothing to prevent Kuzco from passing all of his classes.
- `d7s0` The Emperor's New Groove [0]: The Emperor's New Groove is a 2000 American animated buddy comedy film created by Walt Disney Feature Animation and released by Walt Disney Pictures.
- `d7s1` The Emperor's New Groove [1]: It is the 40th Disney animated feature film.
- `d7s2` The Emperor's New Groove [2]: It was directed by Mark Dindal, produced by Randy Fullmer, written by David Reynolds, and stars David Spade, John Goodman, Eartha Kitt, Patrick Warburton and Wendie Malick.
- `d8s0` Kronk's New Groove [0]: Kronk's New Groove (also known as The Emperor's New Groove 2: Kronk's New Groove) is a 2005 American direct-to-video animated musical comedy film released by The Walt Disney Company on December 13, 2005.
- `d8s1` Kronk's New Groove [1]: The film is the sequel and spin-off to the 2000 animated film "The Emperor's New Groove", and features reprises of the roles of David Spade, John Goodman, Eartha Kitt, Patrick Warburton and Wendie Malick from the original film, with new voices by John Mahoney and Tracey Ullman.
- `d8s2` Kronk's New Groove [2]: It was also the last film to feature the voice of John Fiedler, who died six months before the movie was released.
- `d9s0` Restrung [0]: Restrung is an American-Canadian independent documentary film directed, shot, and edited by Mike Enns and produced by Enns and Randy Fullmer.
- `d9s1` Restrung [1]: The film chronicles Fullmer's life and career from making guitars at a young age, to work on Disney films such as "The Emperor's New Groove," "Who Framed Roger Rabbit," and "The Lion King," to ultimately resign from the company and establishing a guitar-making business.
- `d9s2` Restrung [2]: The film made its world premier on July 1, 2014.
- `d10s0` The Sweatbox [0]: The Sweatbox is a 2002 documentary designed to show behind the scenes footage of "Kingdom of the Sun" (the original working title of "The Emperor's New Groove").
- `d10s1` The Sweatbox [1]: It illustrated the slow and painful transformation from "Kingdom of the Sun" to "The Emperor's New Groove", including the director, musician Sting (whose wife created the documentary), artists, and voice cast being dismayed by the new direction.
- `d10s2` The Sweatbox [2]: A major theme is creative-executive conflicts.

</details>

## Q249 — `hotpotqa_5a793e77554299029c4b5f36` (revised draft)

> Who was born first, Martin Heidegger or Lydia Davis?

Source answer: Martin Heidegger

Gold final answer: Martin Heidegger

Question type: `comparison` (source type `comparison`)

Replaces: `hotpotqa_5abc25b6554299700f9d77f9`

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: birth year of Martin Heidegger | false | 1889 | — | [d8s0] | — |
| u2: birth year of Lydia Davis | false | 1947 | — | [d10s0] | — |
| u3: Who was born first, Martin Heidegger or Lydia Davis? | true | Martin Heidegger | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d8s0` Martin Heidegger [0]: Martin Heidegger ( ; ] ; 26 September 188926 May 1976) was a German philosopher and a seminal thinker in the Continental tradition and philosophical hermeneutics.
- `d10s0` Lydia Davis [0]: Lydia Davis (born July 15, 1947) is an American writer noted for literary works of extreme brevity (commonly called "flash fiction").

Notes:

- 替换：缺少原始阵容及保持原阵容录制的专辑数，不能由主唱离队倒推。 新题保留原source type，人工核对两条显式事实及答案。

<details><summary>All source context</summary>

- `d1s0` Martin Heidegger and Nazism [0]: Philosopher Martin Heidegger joined the Nazi Party (NSDAP) on May 1, 1933, ten days after being elected Rector of the University of Freiburg.
- `d1s1` Martin Heidegger and Nazism [1]: A year later, in April 1934, he resigned the Rectorship and stopped taking part in Nazi Party meetings, but remained a member of the Nazi Party until its dismantling at the end of World War II.
- `d1s2` Martin Heidegger and Nazism [2]: The denazification hearings immediately after World War II led to Heidegger's dismissal from Freiburg, banning him from teaching.
- `d1s3` Martin Heidegger and Nazism [3]: In 1949, after several years of investigation, the French military finally classified Heidegger as a "Mitläufer" or "Nazi follower".
- `d1s4` Martin Heidegger and Nazism [4]: The teaching ban was lifted in 1951 and Heidegger was granted "emeritus" status in 1953, but he was never allowed to resume his philosophy chair.
- `d2s0` Mark Wrathall [0]: Mark Wrathall (born 1965) is professor of Philosophy at the University of California, Riverside.
- `d2s1` Mark Wrathall [1]: His main interests include phenomenology, existentialism, the phenomenology of religion, the philosophy of popular culture, and the philosophy of law.
- `d2s2` Mark Wrathall [2]: He is considered a leading interpreter of the philosophy of Martin Heidegger.
- `d2s3` Mark Wrathall [3]: Wrathall is featured in Tao Ruspoli's film "Being in the World".
- `d2s4` Mark Wrathall [4]: According to a recent reviewer of Wrathall's latest book, "Wrathall's writing is clear and comprehensive, ranging across virtually all of Heidegger's collected works... Wrathall's overall interpretation of Heidegger's work is crystal clear, compelling, and relevant."
- `d3s0` The Origin of the Work of Art [0]: The Origin of the Work of Art (German: "Der Ursprung des Kunstwerkes" ) is an essay by the German philosopher Martin Heidegger.
- `d3s1` The Origin of the Work of Art [1]: Heidegger drafted the text between 1935 and 1937, reworking it for publication in 1950 and again in 1960.
- `d3s2` The Origin of the Work of Art [2]: Heidegger based his essay on a series of lectures he had previously delivered in Zurich and Frankfurt during the 1930s, first on the essence of the work of art and then on the question of the meaning of a "thing," marking the philosopher's first lectures on the notion of art.
- `d4s0` William J. Richardson [0]: William John Richardson, S.J. (2 November 1920 – 10 December 2016) was an American philosopher, who was among the very first to write a comprehensive study of the philosophy of Martin Heidegger, featuring an important preface by Heidegger himself.
- `d4s1` William J. Richardson [1]: In addition to his specialization in Heidegger, Richardson was also, as a trained psychoanalyst, a specialist in the thought of Jacques Lacan.
- `d4s2` William J. Richardson [2]: He was a Jesuit priest (entering the order on 14 August 1941, he was ordained a priest on 15 August 1953).
- `d4s3` William J. Richardson [3]: He taught philosophy at Fordham University and since 1981, at Boston College, where he was, at the time of his death, emeritus professor of philosophy.
- `d4s4` William J. Richardson [4]: He died in December 2016 in Weston, Massachusetts at the age of 96.
- `d5s0` Otto Pöggeler [0]: Otto Pöggeler (12 December 1928 in Attendorn – 10 December 2014) was a German philosopher.
- `d5s1` Otto Pöggeler [1]: He specialized in phenomenology and commenting on Heidegger.
- `d5s2` Otto Pöggeler [2]: In 1963 he authored the acclaimed "Martin Heidegger’s Path of Thinking", one of the first rigorous attempts at tracing the development of Heidegger’s thought.
- `d5s3` Otto Pöggeler [3]: He also published a study of poetry of Paul Celan, and was director of the Hegel Archive at the Ruhr University in Bochum.
- `d6s0` Richard M. Capobianco [0]: Richard M. Capobianco is an American philosophy professor and one of the leading commentators on the thought of the 20th century German philosopher Martin Heidegger.
- `d6s1` Richard M. Capobianco [1]: His two books, "Engaging Heidegger" and "Heidegger's Way of Being", have led the way to a renewed appreciation of Heidegger's core concern with Being as temporal radiant emergence or manifestation.
- `d6s2` Richard M. Capobianco [2]: He has also brought Heidegger into closer proximity with American authors such as Walt Whitman, Henry David Thoreau, Ralph Waldo Emerson, John Muir, and E. E. Cummings, and with English poets such as William Wordsworth and Gerard Manley Hopkins.
- `d7s0` Black Notebooks [0]: The Black Notebooks (German: "Schwarze Hefte" ) are a set of notebooks written by German philosopher Martin Heidegger (1889–1976), which were first published in 2014.
- `d7s1` Black Notebooks [1]: They were edited by Peter Trawny.
- `d7s2` Black Notebooks [2]: Originally a set of small notebooks with black covers in which Heidegger jotted observations, they have been collated into a 1000-page transcript.
- `d7s3` Black Notebooks [3]: The first notebook is missing.
- `d7s4` Black Notebooks [4]: The subsequent notebooks will be published in the Gesamtausgabe.
- `d7s5` Black Notebooks [5]: So far fourteen notebooks have been published encompassing the years 1931–1941 ("GA" 94–96).
- `d7s6` Black Notebooks [6]: The notebooks from 1942-1945 are in private possession but they have already been prepared for publication.
- `d7s7` Black Notebooks [7]: The notebooks contain more explicitly anti-Semitic content than Heidegger's previously published writings, reigniting the debate about Heidegger's Nazism and its relationship to his philosophical project.
- `d8s0` Martin Heidegger [0]: Martin Heidegger ( ; ] ; 26 September 188926 May 1976) was a German philosopher and a seminal thinker in the Continental tradition and philosophical hermeneutics.
- `d8s1` Martin Heidegger [1]: According to the "Internet Encyclopedia of Philosophy", he is "widely acknowledged to be one of the most original and important philosophers of the 20th century".
- `d8s2` Martin Heidegger [2]: Heidegger is best known for his contributions to phenomenology and existentialism, though as the "Stanford Encyclopedia of Philosophy" cautions, "his thinking should be identified as part of such philosophical movements only with extreme care and qualification".
- `d9s0` La sombra de Heidegger [0]: La sombra de Heidegger (English: The Shadow of Heidegger) is a 2005 thriller written by the Argentine philosopher José Pablo Feinmann.
- `d9s1` La sombra de Heidegger [1]: It depicts an exiled Nazi professor called Dieter Müller who writes a letter to his son, in which he describes the philosophy of Martin Heidegger as the spiritual guidance of the Nazi Party.
- `d9s2` La sombra de Heidegger [2]: Besides, "La sombra de Heidegger" has some elements that would enable it to be included in the category of historical novel.
- `d9s3` La sombra de Heidegger [3]: Although there are fictional characters, most of the people involved in the novel are public—and often controversial—figures, such as Adolf Hitler, Ernst Röhm, Jean-Paul Sartre and so on.The novel also covers topics of Argentine political life.
- `d9s4` La sombra de Heidegger [4]: More than once Müller satirizes the situation of peronism in Argentina.
- `d10s0` Lydia Davis [0]: Lydia Davis (born July 15, 1947) is an American writer noted for literary works of extreme brevity (commonly called "flash fiction").
- `d10s1` Lydia Davis [1]: Davis is also a short story writer, novelist, essayist, and translator from French and other languages, and has produced several new translations of French literary classics, including "Swann’s Way" by Marcel Proust and "Madame Bovary" by Gustave Flaubert.

</details>

## Q250 — `hotpotqa_5abc7bf75542993a06baf8f0` (revised draft)

> Which has more species Laurus or Liriodendron?

Source answer: Laurus

Gold final answer: Laurus

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: species count lower bound of Laurus | false | 3 or more | — | [d2s1] OR [d1s1, d1s2] | — |
| u2: species count of Liriodendron | false | 2 | — | [d9s0] OR [d10s0] | — |
| u3: Which has more species Laurus or Liriodendron? | true | Laurus | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d1s1` Laurus novocanariensis [1]: belonging to "Laurus" genus of evergreen trees belonging to the Laurel family, Lauraceae.
- `d1s2` Laurus novocanariensis [2]: The genus includes three species, whose diagnostic key characters often overlap.
- `d2s1` Laurus [1]: The genus includes three or more species.
- `d9s0` Liriodendron [0]: Liriodendron is a genus of two species of characteristically large deciduous trees in the magnolia family (Magnoliaceae).
- `d10s0` Liriodendron tulipifera [0]: Liriodendron tulipifera—known as the tulip tree, American tulip tree, tuliptree, tulip poplar, whitewood, fiddletree, and yellow-poplar—is the Western Hemisphere representative of the two-species genus "Liriodendron," and the tallest eastern hardwood.

Notes:

- 保留至少3的下界，精确3也支持该下界；补Laurus和Liriodendron备选。

<details><summary>All source context</summary>

- `d1s0` Laurus novocanariensis [0]: Laurus novocanariensis is an evergreen large shrub or tree with aromatic, shiny dark-green foliage.
- `d1s1` Laurus novocanariensis [1]: belonging to "Laurus" genus of evergreen trees belonging to the Laurel family, Lauraceae.
- `d1s2` Laurus novocanariensis [2]: The genus includes three species, whose diagnostic key characters often overlap.
- `d1s3` Laurus novocanariensis [3]: Under favorable conditions it is an impressive tree of 3 to 20 m. tall.
- `d1s4` Laurus novocanariensis [4]: It is native of rich soils in the cloud zone of always moist spots in subtropical climate with a high air-humidity, on the Canary and Madeira islands.
- `d2s0` Laurus [0]: Laurus is a genus of evergreen trees belonging to the Laurel family, Lauraceae.
- `d2s1` Laurus [1]: The genus includes three or more species.
- `d3s0` Phytophthora kernoviae [0]: Phytophthora kernoviae is a plant pathogen that mainly infects European beech ("Fagus sylvatica") and "Rhododendron ponticum".
- `d3s1` Phytophthora kernoviae [1]: It was first identified in 2003 in Cornwall, UK when scientists were surveying for the presence of "Phytophthora ramorum".
- `d3s2` Phytophthora kernoviae [2]: This made it the third new "Phytophthora" species to be found in the UK in a decade.
- `d3s3` Phytophthora kernoviae [3]: It was named "Phytophthora kernoviae", after the ancient name for Cornwall, Kernow.
- `d3s4` Phytophthora kernoviae [4]: It causes large stem lesions on beech and necrosis of stems and leaves of "Rhododendron ponticum".
- `d3s5` Phytophthora kernoviae [5]: It is self-fertile.
- `d3s6` Phytophthora kernoviae [6]: It has also been isolated from "Quercus robur" and "Liriodendron tulipifera".
- `d3s7` Phytophthora kernoviae [7]: The original paper describing the species, stated it can infect "Magnolia" and "Camellia" species, "Pieris formosa", "Gevuina avellana", "Michelia doltsopa" and "Quercus ilex".
- `d3s8` Phytophthora kernoviae [8]: Since then many other plants have been identified as natural hosts of the pathogen.
- `d3s9` Phytophthora kernoviae [9]: Molecular analysis has revealed that an infection on "Pinus radiata", recorded in New Zealand in 1950, was caused by "P. kernoviae".
- `d4s0` Morchella ulmaria [0]: Morchella ulmaria is a species of fungus in the family Morchellaceae.
- `d4s1` Morchella ulmaria [1]: It was described as new to science in 2012 by Philippe Clowez.
- `d4s2` Morchella ulmaria [2]: Later in the same year, Michael Kuo and colleagues described "Morchella cryptica", which is a junior synonym of "M. ulmaria".
- `d4s3` Morchella ulmaria [3]: The species occurs in the forests of Midwestern North America, often associated with white ash ("Fraxinus americana"), the American tulip tree ("Liriodendron tulipifera") or species of maple or elm.
- `d4s4` Morchella ulmaria [4]: It is closely related to "M. castanea" and 2 unnamed species from Asia.
- `d5s0` Mezilaurus [0]: Mezilaurus is a genus of plant in the family Lauraceae.
- `d5s1` Mezilaurus [1]: It is a neotropical genus consisting of 18-27 species, mostly hardwood evergreen trees, occurring from Costa Rica to the southeast of Brazil (Werff 1987).
- `d5s2` Mezilaurus [2]: 13 species have been identified in Brazil, distributed mostly in the Amazon region.
- `d5s3` Mezilaurus [3]: In Rio de Janeiro state only "M. navalium" (Allemão) Taub.
- `d5s4` Mezilaurus [4]: ex Mez has been recorded.
- `d5s5` Mezilaurus [5]: Some species have been reported within the Cerrado and in semideciduous forest surrounding the Pantanal Matogrossense.
- `d5s6` Mezilaurus [6]: The name "Mezilaurus" (half laurel) refers to its similar appearance to the genus "Laurus".
- `d6s0` Hakea laurina [0]: Hakea laurina is a plant of Southwest Australia that is widely cultivated and admired.
- `d6s1` Hakea laurina [1]: The species is often referred to as Kodjet, Pincushion Hakea, and Emu Bush.
- `d6s2` Hakea laurina [2]: The specific epithet, derived from the Latin "laurus", is given for the resemblance to the leaves of laurel.
- `d6s3` Hakea laurina [3]: The Noongar name for the plant is Kodjet or Kojet.
- `d7s0` Liriodendron chinense [0]: Liriodendron chinense (commonly known as the Chinese tulip poplar, Chinese tulip tree or Chinese whitewood) is Asia's native species in the "Liriodendron" genus.
- `d7s1` Liriodendron chinense [1]: This native of central and southern China grows in the provinces of Anhui, Guangxi, Jiangsu, Fujian, Guizhou, Hubei, Hunan, Jiangxi, Shaanxi, Zhejiang, Sichuan and Yunnan, and also locally in northern Vietnam.
- `d7s2` Liriodendron chinense [2]: Protected populations occur in the Tianmushan National Reserve, Huangshan, Wuyi Shan, and Badagongshan Nature Reserve.
- `d8s0` Laurus azorica [0]: Laurus azorica (also called Azores laurel or Macaronesian laurel) is a species of plant in the Lauraceae family, related to "Laurus nobilis".
- `d8s1` Laurus azorica [1]: It is a small aromatic tree.
- `d8s2` Laurus azorica [2]: A recent study found considerable genetic diversity within "L. nobilis", and that "L. azorica" is not genetically or morphologically distinct.
- `d9s0` Liriodendron [0]: Liriodendron is a genus of two species of characteristically large deciduous trees in the magnolia family (Magnoliaceae).
- `d10s0` Liriodendron tulipifera [0]: Liriodendron tulipifera—known as the tulip tree, American tulip tree, tuliptree, tulip poplar, whitewood, fiddletree, and yellow-poplar—is the Western Hemisphere representative of the two-species genus "Liriodendron," and the tallest eastern hardwood.
- `d10s1` Liriodendron tulipifera [1]: It is native to eastern North America from Southern Ontario and Illinois eastward to southeastern Massachusetts and Rhode Island, and south to central Florida and Louisiana.
- `d10s2` Liriodendron tulipifera [2]: It can grow to more than 50 m in virgin cove forests of the Appalachian Mountains, often with no limbs until it reaches 25 – in height, making it a very valuable timber tree.
- `d10s3` Liriodendron tulipifera [3]: It is fast-growing, without the common problems of weak wood strength and short lifespan often seen in fast-growing species.
- `d10s4` Liriodendron tulipifera [4]: April marks the start of the flowering period in the southern USA (except as noted below); trees at the northern limit of cultivation begin to flower in June.
- `d10s5` Liriodendron tulipifera [5]: The flowers are pale green or yellow (rarely white), with an orange band on the tepals; they yield large quantities of nectar.
- `d10s6` Liriodendron tulipifera [6]: The tulip tree is the state tree of Indiana, Kentucky, and Tennessee.

</details>

## Q251 — `hotpotqa_5abd6cb955429933744ab7cd` (revised draft)

> The creature HNoMS Draug is named after comes from what kind of mythology?

Source answer: Norse

Gold final answer: Norse

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: mythical creature after which HNoMS Draug was named | false | Draugr | — | [d3s0] | — |
| u2: mythology of {u1} | true | Norse | u1 | [d5s0] | — |

Evidence:

- `d3s0` HNoMS Draug [0]: Two ships of the Royal Norwegian Navy have borne the name HNoMS "Draug", after the sea revenant Draugr:
- `d5s0` Draugr [0]: The draugr or draug (Old Norse: "draugr" , plural draugar ; modern Icelandic: "draugur" , Faroese: "dreygur" and Danish, Swedish, and Norwegian: "draug" ), also called aptrganga or aptrgangr , literally "again-walker" (Icelandic: "afturganga" ) is an undead creature from Norse mythology.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` HNoMS Valkyrien [0]: HNoMS Valkyrien, HNoMS Valkyrjen (in Norwegian the prefix KNM is used) has been the name of several ships in the Royal Norwegian Navy.
- `d1s1` HNoMS Valkyrien [1]: Most of them have been in some way connected to the Royal Norwegian Navy's torpedo boats.
- `d1s2` HNoMS Valkyrien [2]: The name honours the valkyries of Norse mythology.
- `d1s3` HNoMS Valkyrien [3]: It has also been said that the ships have been given this name in honour of all women.
- `d1s4` HNoMS Valkyrien [4]: Some of the ships:
- `d2s0` Wight [0]: Wight is an English word, from Old English "wiht", and used to describe a creature or living sentient being.
- `d2s1` Wight [1]: It is akin to Old High German "wiht", meaning a creature or thing.
- `d2s2` Wight [2]: In its original usage the word "wight" described a living human being.
- `d2s3` Wight [3]: More recently, the word has been used within the fantasy genre of literature to describe undead: corpses with a part of their decayed soul still in residence, often draining life from their victims.
- `d2s4` Wight [4]: The earliest example of this usage in English is in William Morris's translation of the Grettis Saga, where draug is translated as "barrow wight".
- `d2s5` Wight [5]: Notable later examples include the undead Barrow-wights from the works of J. R. R. Tolkien, the reanimated creatures killed by the Others from the works of George R. R. Martin and in the HBO adaption of A Song of Ice and Fire, and the level-draining wights of "Dungeons & Dragons" role-playing game franchise.
- `d3s0` HNoMS Draug [0]: Two ships of the Royal Norwegian Navy have borne the name HNoMS "Draug", after the sea revenant Draugr:
- `d4s0` HNoMS Troll [0]: Two ships of the Royal Norwegian Navy have borne the name HNoMS "Troll", after the Norse mythological creature Troll:
- `d5s0` Draugr [0]: The draugr or draug (Old Norse: "draugr" , plural draugar ; modern Icelandic: "draugur" , Faroese: "dreygur" and Danish, Swedish, and Norwegian: "draug" ), also called aptrganga or aptrgangr , literally "again-walker" (Icelandic: "afturganga" ) is an undead creature from Norse mythology.
- `d6s0` HNoMS Vidar (N52) [0]: HNoMS "Vidar" (N52) was a Royal Norwegian Navy minelayer and command vessel.
- `d6s1` HNoMS Vidar (N52) [1]: "Vidar" was built by Mjellem & Karlsen in Bergen in 1977, and named after Odin's son Vidar from Norse mythology.
- `d6s2` HNoMS Vidar (N52) [2]: The vessel was the command ship for NATO's "Mine Counter Measures Force North" (MCMFORNORTH) in 2004 and 2005.
- `d6s3` HNoMS Vidar (N52) [3]: In 2006 she was sold to Lithuania and given the name "Jotvingis".
- `d6s4` HNoMS Vidar (N52) [4]: The Lithuanian Navy uses her as a command and support ship.
- `d7s0` HNoMS Nordkapp [0]: HNoMS "Nordkapp" was the lead ship of the "Nordkapp" class of fishery protection vessels.
- `d7s1` HNoMS Nordkapp [1]: She was launched 18 August 1937 at Horten naval shipyard, with yard number 123.
- `d7s2` HNoMS Nordkapp [2]: She had one sister ship, HNoMS "Senja".
- `d7s3` HNoMS Nordkapp [3]: "Nordkapp" was named after the North Cape in Finnmark.
- `d7s4` HNoMS Nordkapp [4]: As was typical of her class, "Nordkapp" was very unstable in rough seas and was viewed from the beginning as a second-rate vessel.
- `d7s5` HNoMS Nordkapp [5]: "Nordkapp" sailed throughout the Second World War and saw service in several theatres.
- `d8s0` HNoMS Troll (1910) [0]: The destroyer HNoMS "Troll, known locally as "Torpedojager Troll (litt.: "torpedo hunter"), was the second destroyer built for the Royal Norwegian Navy, as the second ship of the "Draug"-class destroyers.
- `d8s1` HNoMS Troll (1910) [1]: She was built at the naval shipyard in Horten, with yard number 104.
- `d8s2` HNoMS Troll (1910) [2]: She was kept in service long after she was obsolete, and took part in the defence of Norway after the German invasion in 1940.
- `d9s0` HNoMS Draug (1908) [0]: HNoMS "Draug" was the lead ship of the three-ship "Draug" class of destroyers built for the Royal Norwegian Navy in the years 1908–1913.
- `d9s1` HNoMS Draug (1908) [1]: The four-stacked destroyer was kept in service long after she was obsolete, and took part in the defence of Norway during the German invasion in 1940.
- `d10s0` HNoMS Garm (1913) [0]: HNoMS "Garm" was the third destroyer built for the Royal Norwegian Navy, and was a "Draug" class destroyer.
- `d10s1` HNoMS Garm (1913) [1]: "Garm" was constructed several years after her two sister ships, but to the same plans.
- `d10s2` HNoMS Garm (1913) [2]: She was built at the naval shipyard in Horten, with yard number 107.

</details>

## Q252 — `hotpotqa_5abd848455429924427fd03a` (revised draft)

> Are Edward F. Cline and Floyd Mutrux both screenwriters?

Source answer: yes

Gold final answer: yes

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: whether Edward F. Cline is a screenwriter | false | yes | — | [d4s0] | — |
| u2: whether Floyd Mutrux is a screenwriter | false | yes | — | [d9s0] OR [d10s0] OR [d10s0, d10s2] | — |
| u3: Are Edward F. Cline and Floyd Mutrux both screenwriters? | true | yes | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d4s0` Edward F. Cline [0]: Edward Francis Cline (November 4, 1891 – May 22, 1961) was an American screenwriter, actor, writer and director best known for his work with comedians W. C. Fields and Buster Keaton.
- `d9s0` Floyd Mutrux [0]: Floyd Mutrux (born June 21, 1941) is an American stage and film director, writer, producer, and screenwriter.
- `d10s0` American Me [0]: American Me is a 1992 biographical crime drama film produced and directed by Edward James Olmos, his first film as a director, and written by Floyd Mutrux and Desmond Nakano.
- `d10s2` American Me [2]: Executive producers included record producer Lou Adler, screenwriter Mutrux, and Irwin Young.

Notes:

- 电影written by已支持编剧职业；另收录全名与screenwriter Mutrux的组合，避免单靠姓氏对应。

<details><summary>All source context</summary>

- `d1s0` Edward F. Wente [0]: Edward F. Wente (born 1930) is an American professor emeritus of Egyptology and the Department of Near Eastern Languages and Civilizations at the University of Chicago.
- `d1s1` Edward F. Wente [1]: He received his Ph.D from the University of Chicago in 1959 and lectured there from 1963 to 1996.
- `d1s2` Edward F. Wente [2]: He is also a longstanding member of the Oriental Institute, Chicago.
- `d1s3` Edward F. Wente [3]: One of his major works is "Letters from Ancient Egypt" (1990), published by the Scholarly Press.
- `d1s4` Edward F. Wente [4]: In 1999 the Oriental Institute published a collection of essays by Egyptologists in honor of Edward Wente" "Gold of Praise: Studies on Ancient Egypt in Honor of Edward F. Wente"".
- `d2s0` There Goes My Baby (film) [0]: There Goes My Baby (also released as The Last Days of Paradise) is a 1994 American coming-of-age comedy-drama film written and directed by Floyd Mutrux and starring Dermot Mulroney, Rick Schroder, Noah Wyle, Lucy Deakins, and Kelli Williams.
- `d3s0` Sun Records (TV series) [0]: Sun Records is an American drama television series based on the musical "Million Dollar Quartet" written by Colin Escott and Floyd Mutrux.
- `d3s1` Sun Records (TV series) [1]: It takes place at the Sun Studio in Memphis.
- `d3s2` Sun Records (TV series) [2]: The series stars Drake Milligan, Trevor Donovan, Kevin Fonteyne, Christian Lees, Dustin Ingram, Billy Gardell, Jonah Lees, Chad Michael Murray and Jennifer Holland.
- `d3s3` Sun Records (TV series) [3]: The series premiered on CMT on February 23, 2017 and concluded on April 13, 2017.
- `d3s4` Sun Records (TV series) [4]: While originally intended to be a three-night event, CMT extended the show to an eight episode miniseries and hinted that future episodes could be a possibility due to the show's success.
- `d4s0` Edward F. Cline [0]: Edward Francis Cline (November 4, 1891 – May 22, 1961) was an American screenwriter, actor, writer and director best known for his work with comedians W. C. Fields and Buster Keaton.
- `d4s1` Edward F. Cline [1]: He was born in Kenosha, Wisconsin and died in Hollywood, California.
- `d5s0` Edward F. Caldwell &amp; Co. [0]: Edward F. Caldwell & Co., of New York City, was one of the premier designers and manufacturers of electric light fixtures and decorative metalwork from the late 19th to the mid-20th centuries.
- `d5s1` Edward F. Caldwell &amp; Co. [1]: Founded in 1895 by Edward F. Caldwell (1851–1914) and Victor F. von Lossberg (1853–1942), the firm left a legacy of custom designed and finely-made, metal gates, lanterns, chandeliers, ceiling and wall fixtures, floor and table lamps, and other decorative objects that can be found today in many metropolitan area churches, public buildings, offices, clubs, and residences including, the White House (1902 renovation), St. Patrick's Cathedral, New York, New York Public Library, and Rockefeller Center.
- `d6s0` Aloha, Bobby and Rose [0]: Aloha, Bobby and Rose is a 1975 American road drama film about a young working-class couple who accidentally cause the death of a store clerk during their first date, and go on the run from the law.
- `d6s1` Aloha, Bobby and Rose [1]: The film was written and directed by Floyd Mutrux, and starred Paul Le Mat and Dianne Hull, in addition to Robert Carradine in an early role.
- `d7s0` The Frozen North [0]: The Frozen North is a 1922 American short comedy film directed by and starring Buster Keaton.
- `d7s1` The Frozen North [1]: The film is a parody of early western films, especially those of William S. Hart.
- `d7s2` The Frozen North [2]: The film was written by Keaton and Edward F. Cline (credited as Eddie Cline).
- `d7s3` The Frozen North [3]: The film runs for around 17 minutes.
- `d7s4` The Frozen North [4]: Sybil Seely and Bonnie Hill co-star in the film.
- `d8s0` Gen. Edward F. Jones House [0]: Gen. Edward F. Jones House is a historic home located at Binghamton in Broome County, New York.
- `d8s1` Gen. Edward F. Jones House [1]: It was constructed in 1872 and is a large 2 ⁄ -story, irregularly shaped building built of an eclectic combination of materials and textures.
- `d8s2` Gen. Edward F. Jones House [2]: It was part of a large estate assembled by General Edward F. Jones (1828–1913) by 1883.
- `d8s3` Gen. Edward F. Jones House [3]: The foundation and first floor are constructed of brick while the upper stories are of wood with shingle, beaded board, and clapboard siding.
- `d8s4` Gen. Edward F. Jones House [4]: It is an exceptional example of the Queen Anne style.
- `d9s0` Floyd Mutrux [0]: Floyd Mutrux (born June 21, 1941) is an American stage and film director, writer, producer, and screenwriter.
- `d10s0` American Me [0]: American Me is a 1992 biographical crime drama film produced and directed by Edward James Olmos, his first film as a director, and written by Floyd Mutrux and Desmond Nakano.
- `d10s1` American Me [1]: Olmos also stars as the film's protagonist, Montoya Santana.
- `d10s2` American Me [2]: Executive producers included record producer Lou Adler, screenwriter Mutrux, and Irwin Young.
- `d10s3` American Me [3]: It depicts a fictionalized account of the founding and rise to power of the Mexican Mafia in the California prison system from the 1950s into the 1980s.

</details>

## Q253 — `hotpotqa_5abdd8d95542991f6610606a` (revised draft)

> How many episodes did the season of The Simpsons which featured the voice of Lisa Kudrow contain?

Source answer: It contains twenty-three episodes

Gold final answer: It contains twenty-three episodes

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: episode featuring Lisa Kudrow's voice | false | Lard of the Dance | — | [d1s3] | — |
| u2: season containing {u1} | false | The Simpsons season 10 | u1 | [d1s0] OR [d4s1] | — |
| u3: number of episodes in {u2} | true | It contains twenty-three episodes (accepted alternatives: 23; twenty-three; 23 episodes) | u2 | [d4s1] | — |

Evidence:

- `d1s0` Lard of the Dance [0]: "Lard of the Dance" is the first episode of "The Simpsons"' tenth season.
- `d1s3` Lard of the Dance [3]: Meanwhile, Lisa becomes jealous that a new student (voiced by Lisa Kudrow) is distracting all her friends by using her fashionable personality.
- `d4s1` The Simpsons (season 10) [1]: It contains twenty-three episodes, starting with "Lard of the Dance".

Notes:

- 标题The Simpsons (season 10)提供季名，d4s1同时说明首集和集数，可独立替代d1s0。

<details><summary>All source context</summary>

- `d1s0` Lard of the Dance [0]: "Lard of the Dance" is the first episode of "The Simpsons"' tenth season.
- `d1s1` Lard of the Dance [1]: It originally aired on the Fox network in the United States on August 23, 1998.
- `d1s2` Lard of the Dance [2]: Homer discovers he can make money by stealing and reselling grease, but eventually stops after negative encounters with Groundskeeper Willie and the Springfield Grease Company.
- `d1s3` Lard of the Dance [3]: Meanwhile, Lisa becomes jealous that a new student (voiced by Lisa Kudrow) is distracting all her friends by using her fashionable personality.
- `d1s4` Lard of the Dance [4]: The episode was written by Jane O'Brien and directed by Dominic Polcino.
- `d2s0` The Comeback (TV series) [0]: The Comeback is an American television comedy-drama series produced by HBO that stars actress Lisa Kudrow as sitcom actress Valerie Cherish in modern-day Los Angeles.
- `d2s1` The Comeback (TV series) [1]: It was created by Kudrow and Michael Patrick King, a former executive producer of "Sex and the City".
- `d2s2` The Comeback (TV series) [2]: Kudrow and King are also screenwriters and executive producers of the series, with King also serving as the director of some episodes.
- `d2s3` The Comeback (TV series) [3]: The series premiered on HBO on June 5, 2005 and aired for a single, 13-episode season before being canceled.
- `d2s4` The Comeback (TV series) [4]: The series was revived nine years later and an eight-episode second season aired on HBO beginning on November 9, 2014.
- `d3s0` List of Web Therapy webisodes [0]: "Web Therapy" is a web series of Lstudio.com mainly based on improvisation.
- `d3s1` List of Web Therapy webisodes [1]: Lisa Kudrow appears as the self-absorbed therapist Fiona Wallice who offers three-minute therapy sessions via webcam over the internet.
- `d3s2` List of Web Therapy webisodes [2]: Each webisode stars Kudrow video chatting with one or more guest stars.
- `d4s0` The Simpsons (season 10) [0]: "The Simpsons"' tenth season was originally broadcast on the Fox network in the United States between August 23, 1998, and May 16, 1999.
- `d4s1` The Simpsons (season 10) [1]: It contains twenty-three episodes, starting with "Lard of the Dance".
- `d4s2` The Simpsons (season 10) [2]: "The Simpsons" is a satire of a middle class American lifestyle epitomized by its family of the same name, which consists of Homer, Marge, Bart, Lisa and Maggie.
- `d4s3` The Simpsons (season 10) [3]: Set in the fictional city of Springfield, the show lampoons American culture, society, television, and many aspects of the human condition.
- `d5s0` List of Friends characters [0]: Various characters appeared in the sitcom "Friends", which aired for ten seasons on NBC from 1994 to 2004.
- `d5s1` List of Friends characters [1]: It featured six main cast members: Rachel Green (Jennifer Aniston), Phoebe Buffay (Lisa Kudrow), Joey Tribbiani (Matt LeBlanc), Chandler Bing (Matthew Perry), Ross Geller (David Schwimmer) and Monica Geller (Courteney Cox).
- `d5s2` List of Friends characters [2]: Many celebrities guest starred on the series throughout its ten-year run.
- `d6s0` Hopeless Pictures [0]: Hopeless Pictures is an American animated comedy series starring the voice of "Friends" actress Lisa Kudrow, "Seinfeld" guest actor Bob Balaban, and produced and broadcast by the IFC.
- `d6s1` Hopeless Pictures [1]: The cartoon follows fictional film producer Mel Wax, voiced by Michael McKean, in a spoof of the Hollywood movie industry.
- `d6s2` Hopeless Pictures [2]: Stylistically the show makes use of the audio from scripted telephone conversations combined with on-screen gags surrounding the cartoon characters speaking.
- `d7s0` Phoebe Buffay [0]: Phoebe Buffay-Hannigan is a fictional character, portrayed by Lisa Kudrow, one of the six main characters from the American sitcom "Friends".
- `d7s1` Phoebe Buffay [1]: Created by David Crane and Marta Kauffman, the show's creators, she appeared in each of the show's 236 episodes, from its premiere on September 24, 1994 to its finale on May 6, 2004.
- `d7s2` Phoebe Buffay [2]: A masseuse and musician, notable for her offbeat and sometimes ditzy behavior.
- `d7s3` Phoebe Buffay [3]: She was Monica's roommate before Rachel.
- `d7s4` Phoebe Buffay [4]: She plays guitar and sings at Central Perk.
- `d7s5` Phoebe Buffay [5]: During the show's ninth season, Phoebe is introduced to Mike Hannigan, played by actor Paul Rudd, by Joey, and the two begin a romantic relationship.
- `d7s6` Phoebe Buffay [6]: The two later get engaged, then married.
- `d8s0` List of The Comeback episodes [0]: The Comeback is an American television comedy-drama series produced by HBO that stars actress Lisa Kudrow as sitcom actress Valerie Cherish in modern-day Los Angeles.
- `d8s1` List of The Comeback episodes [1]: It was created by Kudrow and Michael Patrick King, a former executive producer of "Sex and the City".
- `d8s2` List of The Comeback episodes [2]: Kudrow and King are also screenwriters and executive producers of the series, with King also serving as the director of some episodes.
- `d8s3` List of The Comeback episodes [3]: The series premiered on HBO on June 5, 2005 and aired for a single, 13-episode season before being canceled.
- `d8s4` List of The Comeback episodes [4]: The series was revived nine years later and an eight-episode second season started airing on HBO on November 9, 2014.
- `d9s0` Laura Silverman [0]: Laura Jane Silverman (born June 10, 1966) is an American actress and voice actress, and the older sister of comedian Sarah Silverman.
- `d9s1` Laura Silverman [1]: She is best known for portraying a fictionalized version of herself alongside her sister in "" and "The Sarah Silverman Program".
- `d9s2` Laura Silverman [2]: She also stars as Jane Benson on "The Comeback" with Lisa Kudrow and voiced Laura, the sarcastic receptionist on the animated comedy television series "Dr. Katz, Professional Therapist".
- `d10s0` Romy and Michele's High School Reunion [0]: Romy and Michele's High School Reunion is a 1997 American comedy film directed by David Mirkin and starring Lisa Kudrow, Mira Sorvino, Janeane Garofalo, Camryn Manheim and Alan Cumming.
- `d10s1` Romy and Michele's High School Reunion [1]: The plot revolves around two 28-year-old women who appear to have not achieved much success in life, and decide to invent fake careers to impress former classmates at their 10-year high school reunion.
- `d10s2` Romy and Michele's High School Reunion [2]: The characters are taken from the stage play "Ladies Room", which also featured Kudrow.

</details>

## Q254 — `hotpotqa_5abec90a5542994516f45438` (revised draft)

> In what U.S. territory did the 1920 Politics strategy operate?

Source answer: Hawaii

Gold final answer: Hawaii

Question type: `single` (source type `bridge`)

Original question: 1920 Politics was a Republican political strategy to reassert the authority of the white race in which US state?

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: location where the 1920 Politics strategy operated | true | Hawaii (accepted alternatives: Territory of Hawaii) | — | [d8s0] | — |

Evidence:

- `d8s0` 1920 Politics (Hawaii) [0]: 1920 Politics also referred to as “Jim Crow” circa 1930, was a Republican political strategy to reassert the authority of the white race and promote American Anglo-Saxon values, in what was then the US Territory of Hawaii.

Notes:

- 题干澄清：改为历史领地，不把1920年的Hawaii称为当时的州；Territory of Hawaii与Hawaii作为名称归一化。
- 删除领地升州的额外桥接，用d8s0直接回答。

<details><summary>All source context</summary>

- `d1s0` Cloward–Piven strategy [0]: The Cloward–Piven strategy is a political strategy outlined in 1966 by American sociologists and political activists Richard Cloward and Frances Fox Piven that called for overloading the U.S. public welfare system in order to precipitate a crisis that would lead to a replacement of the welfare system with a national system of "a guaranteed annual income and thus an end to poverty".
- `d2s0` Southern strategy [0]: In American politics, the southern strategy was a Republican Party electoral strategy to increase political support among white voters in the South by appealing to racism against African Americans.
- `d2s1` Southern strategy [1]: As the Civil Rights Movement and dismantling of Jim Crow laws in the 1950s and 1960s visibly deepened existing racial tensions in much of the Southern United States, Republican politicians such as presidential candidate Richard Nixon and Senator Barry Goldwater developed strategies that successfully contributed to the political realignment of many white, conservative voters in the South to the Republican Party that had traditionally supported the Democratic Party.
- `d2s2` Southern strategy [2]: It also helped push the Republican Party much more to the right.
- `d3s0` Fifty-state strategy [0]: A fifty-state strategy is a political strategy which aims for progress in all states of the United States of America, rather than conceding certain states as "unwinnable."
- `d3s1` Fifty-state strategy [1]: In a presidential campaign, it is usually implemented as an appeal to a broad base of the American public in an attempt to win, even if marginally, every state, since even a marginal victory is effectively total victory for electoral purposes.
- `d3s2` Fifty-state strategy [2]: It can also refer to an overall long-term strategy for a political movement such as a political party.
- `d4s0` Angela McGlowan [0]: Angela McGlowan is an American political commentator, best selling author, and CEO of Political Strategies & Insights (PSI), a government affairs, political strategy, public relations, and advocacy consulting firm based in Oxford, Mississippi, with an office in Washington, D.C. In 2010, she placed third in the Republican primary for a Congressional seat in Mississippi.
- `d5s0` Territory of Hawaii [0]: The Territory of Hawaii or Hawaii Territory was an organized incorporated territory of the United States that existed from August 12, 1898, until August 21, 1959, when its territory was admitted to the Union as the fiftieth U.S. state, the State of Hawaii.
- `d5s1` Territory of Hawaii [1]: The Hawaii Admission Act specified that the State of Hawaii would not include Palmyra Atoll, the Midway Islands, Kingman Reef, and Johnston Atoll, which includes Johnston (or Kalama) Island and Sand Island.
- `d6s0` Uneven and combined development [0]: Uneven and combined development (or unequal and combined development) is a Marxist concept to describe the overall dynamics of human history.
- `d6s1` Uneven and combined development [1]: It was originally used by the Russian revolutionary Leon Trotsky around the turn of the 20th century, when he was analyzing the developmental possibilities that existed for the economy and civilization in the Russian empire, and the likely future of the Tsarist regime in Russia.
- `d6s2` Uneven and combined development [2]: It was the basis of his political strategy of permanent revolution, which implied a rejection of the idea that a human society inevitably developed through a uni-linear sequence of necessary "stages".
- `d6s3` Uneven and combined development [3]: Trotsky's ideas matured under the influence of Georg Vollmar's study of a possibility of socialism in one country, as well as John Hobson, Rudolf Hilferding and Vladimir Lenin's studies of imperialism.
- `d6s4` Uneven and combined development [4]: Also before Trotsky, Nikolay Chernyshevsky and Vasily Vorontsov proposed a similar idea.
- `d6s5` Uneven and combined development [5]: The concept is still used today by Trotskyists and other Marxists concerned with world politics.
- `d7s0` Theodore W. Allen [0]: Theodore William "Ted" Allen (August 23, 1919January 19, 2005) was an American intellectual, writer, and activist, best known for his pioneering writings since the 1960s on "white skin privilege" and the "invention" of the "white race," particularly his seminal "Class Struggle and the Origin of Racial Slavery: The Invention of the White Race," published as a pamphlet in 1975, and published the next year in expanded form.
- `d7s1` Theodore W. Allen [1]: He stressed that the "white race" was invented as "a ruling class social control formation."
- `d8s0` 1920 Politics (Hawaii) [0]: 1920 Politics also referred to as “Jim Crow” circa 1930, was a Republican political strategy to reassert the authority of the white race and promote American Anglo-Saxon values, in what was then the US Territory of Hawaii.
- `d9s0` White nationalism [0]: White nationalism is a type of nationalism or pan-nationalism which holds the belief that white people are a race and seeks to develop and maintain a white national identity.
- `d9s1` White nationalism [1]: Its proponents identify with and are attached to the concept of a white nation.
- `d9s2` White nationalism [2]: White nationalists say they seek to ensure the survival of the white race, and the cultures of historically white states.
- `d9s3` White nationalism [3]: They hold that white people should maintain their majority in majority-white countries, maintain their political and economic dominance, and that their cultures should be foremost.
- `d9s4` White nationalism [4]: Many white nationalists believe that miscegenation, multiculturalism, immigration of nonwhites and low birth rates among whites are threatening the white race, and some argue that it amounts to white genocide.
- `d10s0` Republican National Committee [0]: The Republican National Committee (RNC) is a U.S. political committee that provides national leadership for the Republican Party of the United States.
- `d10s1` Republican National Committee [1]: It is responsible for developing and promoting the Republican political platform, as well as coordinating fundraising and election strategy.
- `d10s2` Republican National Committee [2]: It is also responsible for organizing and running the Republican National Convention.
- `d10s3` Republican National Committee [3]: Similar committees exist in every U.S. state and most U.S. counties, although in some states party organization is structured by congressional district, allied campaign organizations being governed by a national committee.
- `d10s4` Republican National Committee [4]: Ronna Romney McDaniel is the current committee chairwoman.

</details>

## Q255 — `hotpotqa_5ac047a3554299294b218f70` (revised draft)

> Using the branch counts stated in the context, which is larger: China CITIC Bank's mainland branch network or UniCredit's network?

Source answer: UniCredit

Gold final answer: UniCredit

Question type: `comparison` (source type `comparison`)

Original question: Which bank has more branches, China CITIC Bank or UniCredit?

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: upper bound on the mainland branch-office counts reported for China CITIC Bank | false | at most 773 | — | [d2s4] OR [d2s5] | — |
| u2: number of UniCredit network branches | false | more than 8,500 | — | [d6s1] | — |
| u3: Using the branch counts stated in the context, which is larger: China CITIC Bank's mainland branch network or UniCredit's network? | true | UniCredit | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d2s4` China CITIC Bank [4]: The bank operates 78 branches in the mainland, and 622 sub-branches, located in economically developed regions of China.
- `d2s5` China CITIC Bank [5]: In total, there are 773 branch offices in China, as of Q4 2011.
- `d6s1` UniCredit [1]: Its network spans 50 markets in 17 countries, with more than 8,500 branches and over 147,000 employees.

Notes:

- 题干澄清：限定为原文提供的两个网络口径，不推断同一时点全球网点总量。
- u1采用共同上界773：78+622=700及2011年的773都满足；与UniCredit的>8500比较，避免把两个不同值当作同一个精确值。

<details><summary>All source context</summary>

- `d1s0` Kong Dan [0]: Kong Dan (Simplified Chinese: 孔丹) (born 1947 in Beijing, China with family roots in Pingxiang, Jiangxi, China) is a Chinese entrepreneur and economist.
- `d1s1` Kong Dan [1]: He is the chairman of the CITIC Group.
- `d1s2` Kong Dan [2]: He is also the chairman of CITIC International Financial Holdings, China CITIC Bank and CITIC Resources Holdings.
- `d2s0` China CITIC Bank [0]: China CITIC Bank () is China’s seventh-largest lender in terms of total assets.
- `d2s1` China CITIC Bank [1]: It was known as CITIC Industrial Bank until it changed its name in August 2005.
- `d2s2` China CITIC Bank [2]: China CITIC Bank, established in 1987, is a nationally comprehensive and internationally oriented commercial bank.
- `d2s3` China CITIC Bank [3]: The bank operates in almost 130 countries, and maintains a strong foothold on the mainland banking industry.
- `d2s4` China CITIC Bank [4]: The bank operates 78 branches in the mainland, and 622 sub-branches, located in economically developed regions of China.
- `d2s5` China CITIC Bank [5]: In total, there are 773 branch offices in China, as of Q4 2011.
- `d3s0` UniCredit Bank Slovakia [0]: UniCredit Bank Slovakia was a Slovak bank, formed by the merger of HVB Bank Slovakia and UniBanka in 2007, both owned by Italy-based UniCredit Group.
- `d3s1` UniCredit Bank Slovakia [1]: In 2013 it was absorbed by UniCredit Bank Czech Republic, forming UniCredit Bank Czech Republic and Slovakia.
- `d4s0` Ka Wah Bank [0]: Ka Wah Bank Limited (Traditional Chinese: 嘉華銀行有限公司) (Former stock code: ) was a bank in Hong Kong.
- `d4s1` Ka Wah Bank [1]: It was acquired by CITIC International Financial Holdings and renamed as CITIC Ka Wah Bank Limited (Traditional Chinese: 中信嘉華銀行有限公司)(In May 2010, CITIC Ka Wah Bank Limited was renamed as CITIC Bank International Limited(Traditional Chinese: 中信銀行國際有限公司)).
- `d5s0` China Investment Bank [0]: China Investment Bank () was a defunct bank of China.
- `d5s1` China Investment Bank [1]: It was became a subsidiary of China Construction Bank in 1994.
- `d5s2` China Investment Bank [2]: In 1998 it was absorbed by China Development Bank, with some business was received by China CITIC Bank.
- `d6s0` UniCredit [0]: UniCredit S.p.A. is an Italian global banking and financial services company.
- `d6s1` UniCredit [1]: Its network spans 50 markets in 17 countries, with more than 8,500 branches and over 147,000 employees.
- `d6s2` UniCredit [2]: Its strategic position in Western and Eastern Europe gives the group one of the region's highest market shares.
- `d6s3` UniCredit [3]: The company is a component of the Euro Stoxx 50 stock market index.
- `d7s0` Zhong Tian Plaza [0]: China CITIC Bank Mansion (), formerly Zhong Tian Plaza () is a 59-floor/229-meter tall skyscraper in Urumqi, Xinjiang, People's Republic of China.
- `d7s1` Zhong Tian Plaza [1]: It is the tallest building in Northwestern China and Central Asia.
- `d8s0` Bank Austria [0]: UniCredit Bank Austria AG, better known as Bank Austria, is an Austria bank, 96.35% owned by UniCredit Group.
- `d8s1` Bank Austria [1]: The bank maintains an extensive network in Austria, with about 7,700 employees serving customers in some 300 branches.
- `d8s2` Bank Austria [2]: Bank Austria also served as UniCredit's intermediate holding company for the banking network in Central and Eastern Europe (until September 2016), a region where the Group is the clear market leader with about 3,900 branches in 19 countries.
- `d8s3` Bank Austria [3]: However, all the CEE subsidiaries were transferred to the parent company in September 2016.
- `d8s4` Bank Austria [4]: As per 2008, 85% of Bank Austria's total workforce is employed out of Austria.
- `d9s0` CITIC Publishing Group [0]: CITIC Publishing Group () is a publishing company under CITIC Group based in Beijing, China.
- `d9s1` CITIC Publishing Group [1]: It was established on in 1988 as China CITIC Press and was reorganized to CITIC Publishing Group in 2008.
- `d10s0` CITIC Bank International [0]: CITIC Bank International () (Former stock code: ) ("formerly" known as CITIC Ka Wah Bank () and Ka Wah Bank) is a Hong Kong bank majority owned by CITIC.
- `d10s1` CITIC Bank International [1]: It is a subsidiary of CITIC International Financial Holdings.

</details>

## Q256 — `hotpotqa_5ac0cfb45542997d64295a58` (revised draft)

> What statistical area is the suburban city that houses the Charles Hosmer Morse Museum of American Art?

Source answer: Orlando–Kissimmee–Sanford

Gold final answer: Orlando–Kissimmee–Sanford

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: city containing the Charles Hosmer Morse Museum of American Art | false | Winter Park | — | [d5s1] OR [d2s1] | — |
| u2: metropolitan statistical area containing {u1} | true | Orlando–Kissimmee–Sanford | u1 | [d9s2] | — |

Evidence:

- `d2s1` Tiffany Chapel [1]: First installed for the 1893 World's Columbian Exposition in Chicago, the chapel is again on public display, more than a century later, at the Charles Hosmer Morse Museum of American Art in Winter Park, Florida since April 1999.
- `d5s1` Charles Hosmer Morse Museum of American Art [1]: It is located in Winter Park, Florida, USA.
- `d9s2` Winter Park, Florida [2]: It is part of the Orlando–Kissimmee–Sanford, Florida Metropolitan Statistical Area.

Notes:

- 补博物馆位于Winter Park的备选d2s1。

<details><summary>All source context</summary>

- `d1s0` Edmund C. Tarbell [0]: Edmund Charles Tarbell (April 26, 1862 – August 1, 1938) was an American Impressionist painter.
- `d1s1` Edmund C. Tarbell [1]: A member of the Ten American Painters, his work hangs in the Boston Museum of Fine Arts, Metropolitan Museum of Art, National Gallery of Art, Smithsonian American Art Museum, Corcoran Gallery of Art, DeYoung Museum, National Academy Museum and School, New Britain Museum of American Art, Worcester Art Museum, and numerous other collections.
- `d1s2` Edmund C. Tarbell [2]: He was a leading member of a group of painters which came to be known as the Boston School.
- `d2s0` Tiffany Chapel [0]: The Tiffany Chapel is a chapel interior designed by Louis Comfort Tiffany and created by the Tiffany Glass and Decorating Company.
- `d2s1` Tiffany Chapel [1]: First installed for the 1893 World's Columbian Exposition in Chicago, the chapel is again on public display, more than a century later, at the Charles Hosmer Morse Museum of American Art in Winter Park, Florida since April 1999.
- `d3s0` Association Residence Nursing Home [0]: The Association Residence Nursing Home, also called the Association for the Relief of Respectable, Aged and Indigent Females, is an historic building in New York City built from 1881–1883 to the design of Richard Morris Hunt in the Victorian Gothic style.
- `d3s1` Association Residence Nursing Home [1]: It is located on Amsterdam Avenue between 103rd and 104th Streets in Manhattan, and is now a youth hostel run by Hostelling International.
- `d3s2` Association Residence Nursing Home [2]: The Association was founded in 1814 to help the widows of soldiers of the American Revolutionary War and the War of 1812.
- `d3s3` Association Residence Nursing Home [3]: An addition to the building was constructed on the south end of the property in 1907, which contained seven Tiffany windows which are now in the collection of the Morse Museum of American Art.
- `d3s4` Association Residence Nursing Home [4]: The building was placed on the National Register of Historic Places in 1975.
- `d4s0` Charles Hosmer Morse [0]: Charles Hosmer Morse (September 23, 1833 – May 5, 1921) was an American businessman and philanthropist.
- `d4s1` Charles Hosmer Morse [1]: Morse was born at St. Johnsbury, Vermont.
- `d4s2` Charles Hosmer Morse [2]: He graduated from St. Johnsbury Academy in 1850.
- `d4s3` Charles Hosmer Morse [3]: Shortly after graduation he joined his uncle, Zelotus Hosmer, in the Boston office of E. & T. Fairbanks, marketing platform scales.
- `d4s4` Charles Hosmer Morse [4]: He was promoted to the New York office, and then to Chicago, eventually establishing a branch that would go on to be known as Fairbanks-Morse corporation.
- `d4s5` Charles Hosmer Morse [5]: He was also an early resident of and influential figure in the city of Winter Park, Florida.
- `d5s0` Charles Hosmer Morse Museum of American Art [0]: The Charles Hosmer Morse Museum of American Art houses the most comprehensive collection of the works of Louis Comfort Tiffany found anywhere, a major collection of American art pottery, and fine collections of late-19th- and early-20th-century American paintings, graphics and the decorative arts.
- `d5s1` Charles Hosmer Morse Museum of American Art [1]: It is located in Winter Park, Florida, USA.
- `d6s0` Ethel Scull 36 Times [0]: Ethel Scull 36 Times is a 1963 painting by American artist Andy Warhol, is currently on view at the Whitney Museum of American Art and is part of the collections of both the Metropolitan Museum of Art and the Whitney Museum of American Art.
- `d6s1` Ethel Scull 36 Times [1]: It was Warhol's first commissioned work.
- `d6s2` Ethel Scull 36 Times [2]: The work consists of four rows of nine equal columns, depicting Ethel Redner Scull, a well-known collector of modern art.
- `d6s3` Ethel Scull 36 Times [3]: The artwork is jointly owned by the Metropolitan Museum of Art and the Whitney Museum of American Art.
- `d7s0` Shreveport-Bossier City-Minden CSA [0]: The Shreveport-Bossier City-Minden Combined Statistical Area was made up of four parishes in northwestern Louisiana.
- `d7s1` Shreveport-Bossier City-Minden CSA [1]: The statistical area consisted of then-Shreveport-Bossier City Metropolitan Statistical Area and then-Minden Micropolitan Statistical Area.
- `d7s2` Shreveport-Bossier City-Minden CSA [2]: As of the 2010 census, the CSA had a population of 439,000 (though a July 1, 2011 estimate placed the population at 444,000).
- `d7s3` Shreveport-Bossier City-Minden CSA [3]: On February 28, 2013, OMB changed definitions of census statistical areas, and all four parishes in this combined statistical area were redefined as Shreveport-Bossier City Metropolitan Statistical Area.
- `d8s0` Anthony Waichulis [0]: Anthony Waichulis (born 1972) is a contemporary Trompe L'Oeil painter from rural Northeastern Pennsylvania.
- `d8s1` Anthony Waichulis [1]: Celebrated by critics and collectors alike, Waichulis' works have been published in nearly every major art publication including The Artist's Magazine, Fine Art Connoisseur, American Artist, American Art Review, American Art Collector, Art News, and Art-Talk.
- `d8s2` Anthony Waichulis [2]: Anthony, represented by The John Pence Gallery in San Francisco, has exhibited in numerous key venues across the country including the Smithsonian Institution, National Arts Club, Butler Institute of American Art, Orlando Museum of Art, Arnot Art Museum, and the Beijing World Art Museum among others.
- `d8s3` Anthony Waichulis [3]: Waichulis has also achieved top honors in nearly every prestigious national and international competition held today including The Artist's Magazine's Annual Competition and the Art Renewal Center's International Salon Competition.
- `d8s4` Anthony Waichulis [4]: In January 2006, Anthony became the first Trompe L'Oeil painter to be granted Living Master status with The Art Renewal Center.
- `d9s0` Winter Park, Florida [0]: Winter Park is a suburban city in Orange County, Florida, United States.
- `d9s1` Winter Park, Florida [1]: The population was 27,852 at the 2010 United States Census.
- `d9s2` Winter Park, Florida [2]: It is part of the Orlando–Kissimmee–Sanford, Florida Metropolitan Statistical Area.
- `d10s0` Lisa Hoke [0]: Lisa Hoke (born 1952 in Virginia) is an American installation artist and sculptor living and working in New York.
- `d10s1` Lisa Hoke [1]: She received a BFA from Virginia Commonwealth University in Richmond, Virginia and was awarded the Edwin Austin Abbey Fellowship from the National Academy Museum, New York and a Joan Mitchell Foundation Grant.
- `d10s2` Lisa Hoke [2]: Her work has exhibited nationally notably at the Sarasota Museum of Art, Oklahoma City Museum of Art, New Britain Museum of American Art, MASS MoCA, Aldrich Museum, The Hudson Valley Center for Contemporary Art, Cleveland Institute of Art, Serpentine Gallery, Corcoran Gallery of Art and the New Museum.
- `d10s3` Lisa Hoke [3]: Her work is in numerous public and private collations including the Whitney Museum of American Art, Johnson Museum of Art, Cornell University, and New Orleans Museum of Art, among others.
- `d10s4` Lisa Hoke [4]: Jennifer Coates reviewed her most recent solo exhibition at Pavel Zoubok Gallery in "Time Out":

</details>

## Q257 — `hotpotqa_5ac11a8d5542992a796dedee` (revised draft)

> Which is a French documentary, The Seine Meets Paris and Great Old Amusement Parks?

Source answer: The Seine Meets Paris

Gold final answer: The Seine Meets Paris

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: whether The Seine Meets Paris is a French documentary | false | yes | — | [d8s0] | — |
| u2: whether Great Old Amusement Parks is a French documentary | false | no | — | `[]`：无直接支持 | — |
| u3: Which is a French documentary, The Seine Meets Paris and Great Old Amusement Parks? | true | The Seine Meets Paris **[by_presupposition]** | u1, u2 | `[[]]`：由全部依赖推出 | [d8s0] |

Evidence:

- `d8s0` The Seine Meets Paris [0]: The Seine Meets Paris (French: La Seine a rencontré Paris ) is a 1957 French short documentary film directed by Joris Ivens from a screenplay by Jacques Prévert.

Notes:

- 补另一候选unit。d6s0列PBS和作者而未列国籍，不满足“已列出该属性其他值”的omission条件，故仅保留正向确认。

<details><summary>All source context</summary>

- `d1s0` Trolley park [0]: In the United States, trolley parks, which started in the 19th century, were picnic and recreation areas along or at the ends of streetcar lines in most of the larger cities.
- `d1s1` Trolley park [1]: These were precursors to amusement parks.
- `d1s2` Trolley park [2]: These trolley parks were created by the streetcar companies to give people a reason to use their services on weekends.
- `d1s3` Trolley park [3]: These parks originally consisted of picnic groves and pavilions, and often held events such as dances, concerts and fireworks.
- `d1s4` Trolley park [4]: Many eventually added features such as swimming pools, carousels, Ferris wheels, roller coasters, sports fields, boats rides, restaurants and other resort facilities to become amusement parks. Various sources report the existence of between 1,500 and 2,000 amusement parks in the United States by 1919.
- `d2s0` Knoebels Amusement Resort [0]: Knoebels Amusement Resort ( ) is a family-owned and operated amusement park, picnic grove, and campground in Elysburg, Pennsylvania.
- `d2s1` Knoebels Amusement Resort [1]: It is and has been America's largest free-admission park for 90 years of operation.
- `d2s2` Knoebels Amusement Resort [2]: Opened in 1926, the park has more than 60 rides, three wooden roller coasters, one steel roller coaster, a 1913 carousel, and a haunted house dark ride that was featured on the Discovery Channel.
- `d2s3` Knoebels Amusement Resort [3]: The park and its rides have won awards from organizations such as "Amusement Today", American Coaster Enthusiasts, and the International Association of Amusement Parks and Attractions.
- `d2s4` Knoebels Amusement Resort [4]: In 2014, Travel Channel rated Knoebels one of their Top 10 Family Friendly Amusement Parks in the United States.
- `d2s5` Knoebels Amusement Resort [5]: America's Number One Amusement Park
- `d3s0` Amusement park [0]: An amusement park is a park that features various attractions, such as rides and games, as well as other events for entertainment purposes.
- `d3s1` Amusement park [1]: A theme park is a type of amusement park that bases its structures and attractions around a central theme, often featuring multiple areas with different themes.
- `d3s2` Amusement park [2]: Unlike temporary and mobile funfairs and carnivals, amusement parks are stationary and built for long-lasting operation.
- `d3s3` Amusement park [3]: They are more elaborate than city parks and playgrounds, usually providing attractions that cater to a variety of age groups.
- `d3s4` Amusement park [4]: While amusement parks often contain themed areas, theme parks place a heavier focus with more intricately-designed themes that revolve around a particular subject or group of subjects.
- `d4s0` Joris Ivens [0]: Georg Henri Anton "Joris" Ivens (18 November 1898 – 28 June 1989) was a Dutch documentary filmmaker.
- `d4s1` Joris Ivens [1]: Among the notable films he directed or co-directed are "A Tale of the Wind", "The Spanish Earth", "Rain", "...A Valparaiso", "Misère au Borinage" ("Borinage"), "", "The Seine Meets Paris", "Far from Vietnam", "Pour le Mistral" and "How Yukong Moved the Mountains".
- `d5s0` Gay World Amusement Park [0]: Located between Geylang Road and Grove Road (now Mountbatten Road), Gay World was one of the famous trio of "World" amusement parks in Singapore.
- `d5s1` Gay World Amusement Park [1]: Together with the other two "Worlds", Great World Amusement Park (1930s–1978) at Kim Seng Road and New World Amusement Park (1923–1987) at Jalan Besar, Gay World Park was hustling and bustling with nightlife during the 1930s to 1960s.
- `d5s2` Gay World Amusement Park [2]: These amusement parks were especially popular among Singaporeans as it was the locals only form of entertainment, before television or shopping malls were introduced.
- `d5s3` Gay World Amusement Park [3]: Gay World Park was an all-in-one complex, where visitors were offered a wide range of entertainment, from movies to shopping and games.
- `d5s4` Gay World Amusement Park [4]: However, as its popularity began to dip in the 1970s, Gay World Park was eventually demolished in 2000 to make way for residential estates.
- `d5s5` Gay World Amusement Park [5]: This officially marked the end of Gay World Park and its journey in the entertainment industry.
- `d6s0` Great Old Amusement Parks [0]: Great Old Amusement Parks is a 1999 PBS television documentary VHS by Rick Sebak of WQED Pittsburgh.
- `d7s0` North Point State Park [0]: North Point State Park is a public recreation area located on Chesapeake Bay in Edgemere, Baltimore County, Maryland.
- `d7s1` North Point State Park [1]: The state park includes the site of the former Bay Shore Park, which was one of the state's premiere amusement parks during the first half of the 20th century.
- `d7s2` North Point State Park [2]: The park features restored remnants of the old amusement park as well as facilities for swimming, picnicking, bicycling, and hiking.
- `d7s3` North Point State Park [3]: Black Marsh, a 667 acre state wildlands area, makes up half the park's area.
- `d7s4` North Point State Park [4]: The park is administered by the Maryland Department of Natural Resources.
- `d8s0` The Seine Meets Paris [0]: The Seine Meets Paris (French: La Seine a rencontré Paris ) is a 1957 French short documentary film directed by Joris Ivens from a screenplay by Jacques Prévert.
- `d8s1` The Seine Meets Paris [1]: Told from the perspective of a boat trip through the city, it features scenes of daily life along the river.
- `d8s2` The Seine Meets Paris [2]: The film won the short film Palme d'Or at the 1958 Cannes Film Festival.
- `d9s0` List of amusement park rankings [0]: Amusement parks and theme parks are terms for a group of entertainment attractions, rides, and other events in a location for the enjoyment of large numbers of people.
- `d9s1` List of amusement park rankings [1]: Amusement parks are located all around the world with millions of people visiting them every year.
- `d9s2` List of amusement park rankings [2]: This list of amusement park rankings summarizes the attendance records, park rankings and the results of public polls of amusement parks around the world.
- `d10s0` Family entertainment center [0]: A family entertainment center (or centre), often abbreviated FEC in the entertainment industry, (also known as indoor amusement park or indoor theme park) is a small amusement park marketed towards families with small children to teenagers, and often entirely indoors or associated with a larger operation such as a theme park.
- `d10s1` Family entertainment center [1]: They usually cater to "sub-regional markets of larger metropolitan areas."
- `d10s2` Family entertainment center [2]: FECs are generally small compared to full-scale amusement parks, with fewer attractions, a lower per-person per-hour cost to consumers than a traditional amusement park, and not usually major tourist attractions, but sustained by an area customer base.
- `d10s3` Family entertainment center [3]: Many are locally owned and operated, although there are a number of chains and franchises in the field.
- `d10s4` Family entertainment center [4]: FECs are sometimes called family amusement centers, play zones, family fun centers, or simply fun centers.
- `d10s5` Family entertainment center [5]: Some non-traditional FECs, called urban entertainment centers (UECs), with more customized and branded attractions and retail outlets, are associated with major entertainment companies and may be tourist destinations.
- `d10s6` Family entertainment center [6]: Others, sometimes operated by Non-Profit organizations as Children's Museums or Science Centers, tend to be geared toward edutainment experiences rather than simply amusement.
- `d10s7` Family entertainment center [7]: FECs may also be adjuncts to full-scale amusement parks.

</details>

## Q258 — `hotpotqa_5ac1a6a85542994ab5c67db6` (revised draft)

> Where are the offices of the weather service that serves the Kansas city which was named after an agreement between European Americans and the Osage Nation?

Source answer: near Philip Billard Municipal Airport

Gold final answer: near Philip Billard Municipal Airport

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: Kansas city named after the stated agreement | false | Council Grove | — | [d7s2] | — |
| u2: weather office serving {u1} | false | National Weather Service Topeka, Kansas | u1 | [d1s3] | — |
| u3: office location of {u2} | true | near Philip Billard Municipal Airport | u2 | [d1s1] | — |

Evidence:

- `d1s1` National Weather Service Topeka, Kansas [1]: Its offices are located near Philip Billard Municipal Airport.
- `d1s3` National Weather Service Topeka, Kansas [3]: Communities that rely on the Topeka Weather Office for forecasts and severe storm warnings include Abilene, Clay Center, Concordia, Council Grove, Emporia, Hiawatha, Junction City, Lawrence, Manhattan, Marysville, Ottawa, and Topeka.
- `d7s2` Council Grove, Kansas [2]: It was named after an agreement between European Americans and the Osage Nation about allowing settlers' wagon trains to pass through the area and proceed to the West.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` National Weather Service Topeka, Kansas [0]: National Weather Service – Topeka, Kansas (Abbreviation TOP) is a local National Weather Service forecast office based in Topeka, the state capital of Kansas.
- `d1s1` National Weather Service Topeka, Kansas [1]: Its offices are located near Philip Billard Municipal Airport.
- `d1s2` National Weather Service Topeka, Kansas [2]: It provides weather and emergency information to 23 counties in north-central, northeast, and east-central Kansas.
- `d1s3` National Weather Service Topeka, Kansas [3]: Communities that rely on the Topeka Weather Office for forecasts and severe storm warnings include Abilene, Clay Center, Concordia, Council Grove, Emporia, Hiawatha, Junction City, Lawrence, Manhattan, Marysville, Ottawa, and Topeka.
- `d2s0` Treaty of Fort Clark [0]: The Treaty of Fort Clark (also known as the Treaty with the Osage or the Osage Treaty) was signed at Fort Osage (then called Fort Clark) on November 10, 1808 (ratified on April 28, 1810) in which the Osage Nation ceded all the land east of the fort in Missouri and Arkansas north of the Arkansas River to the United States.
- `d2s1` Treaty of Fort Clark [1]: The Fort Clark treaty and the Treaty of St. Louis in which the Sac (tribe) and Fox (tribe) ceded northeastern Missouri along with northern Illinois and southern Wisconsin were the first two major treaties in the newly acquired Louisiana Purchase.
- `d2s2` Treaty of Fort Clark [2]: The affected tribes, upset with the terms, were to side with the British in the War of 1812.
- `d2s3` Treaty of Fort Clark [3]: Following the settlement of that war, John C. Sullivan for the United States was to survey the ceded land in 1816 (adjusting it 23 miles westward to the mouth of the Kansas River to create the Indian Boundary Line west of which and south of which virtually all tribes were to be removed in the Indian Removal Act in 1830.
- `d3s0` Osage County, Oklahoma [0]: Osage County is the largest county by area in the state of Oklahoma in the United States.
- `d3s1` Osage County, Oklahoma [1]: Created in 1907 when Oklahoma was admitted as a state, the county is named for and is home to the federally recognized Osage Nation.
- `d3s2` Osage County, Oklahoma [2]: The county is coextensive with the Osage Nation Reservation, established by treaty in the 19th century when the Osage relocated there from Kansas.
- `d3s3` Osage County, Oklahoma [3]: The county seat is in Pawhuska, Oklahoma, one of the first three towns established in the county.
- `d3s4` Osage County, Oklahoma [4]: The total population of the county is 47,987.
- `d4s0` National Weather Service Lincoln, Illinois [0]: National Weather Service Lincoln, Illinois also known as National Weather Service Central Illinois is a weather forecast office responsible for monitoring weather conditions for 35 counties in Central and Southeastern Illinois.
- `d4s1` National Weather Service Lincoln, Illinois [1]: The Central Illinois office initially consisted of two forecast offices in Peoria and Springfield until the current location in Lincoln became the sole local forecast office in 1995.
- `d4s2` National Weather Service Lincoln, Illinois [2]: Federal meteorology offices and stations in the region date back to the 19th century when the Army Signal Service began taking weather observations using weather equipment at the Springer Building in Springfield.
- `d4s3` National Weather Service Lincoln, Illinois [3]: Since that time the presence of the National Weather Service greatly increased with the instillation of new weather radars, stations and forecast offices.
- `d4s4` National Weather Service Lincoln, Illinois [4]: The current office in Lincoln maintains a WSR-88D (NEXRAD) radar system, and Advanced Weather Interactive Processing System (AWIPS) that greatly improve forecasting in the region.
- `d4s5` National Weather Service Lincoln, Illinois [5]: Lincoln is in charge of weather forecasts, warnings and local statements as well as aviation weather.
- `d5s0` National Weather Service Chicago, Illinois [0]: National Weather Service Chicago, currently based in Romeoville, Illinois, is a weather forecast office responsible for monitoring weather conditions for 23 counties in Northern Illinois, the Chicago metropolitan area and Northwest Indiana.
- `d5s1` National Weather Service Chicago, Illinois [1]: The Army Signal Service established the first federal weather office in the region in Chicago on October 15, 1870.
- `d5s2` National Weather Service Chicago, Illinois [2]: During May 1894 the Chicago Weather Bureau was given a new forecast area extending from the Great Lakes region all the way to the Rocky Mountains.
- `d5s3` National Weather Service Chicago, Illinois [3]: The current National Weather Service Chicago is located in Romeoville and is in charge of issuing local forecasts and weather warnings for the Chicago area.
- `d5s4` National Weather Service Chicago, Illinois [4]: It is one of only two National Weather Service offices in Illinois, the other being National Weather Service Central Illinois in Lincoln, Illinois.
- `d5s5` National Weather Service Chicago, Illinois [5]: The National Weather Service Chicago forecast office is located adjacent to the Lewis University Airport in Romeoville, Illinois.
- `d6s0` Osage Treaty (1825) [0]: The Osage Treaty (also known as the Treaty with the Osage) was signed in what became Council Grove, Kansas, on June 2, 1825 between William Clark on behalf of the United States and members of the Osage Nation.
- `d6s1` Osage Treaty (1825) [1]: The accord contained fourteen articles.
- `d6s2` Osage Treaty (1825) [2]: Based on the most important terms of the accord, the Osage ceded multiple territories to the United States government.
- `d6s3` Osage Treaty (1825) [3]: According to the first article of the treaty, the territories ceded entailed lands lying within and west of both the State of Missouri and the Territory of Arkansas, lands lying north and west of the Red River, all territories south and east of the Kansas River, and all lands located through the Rock Saline.
- `d6s4` Osage Treaty (1825) [4]: The accord was proclaimed on December 30, 1825.
- `d7s0` Council Grove, Kansas [0]: Council Grove is a city and county seat in Morris County, Kansas, United States.
- `d7s1` Council Grove, Kansas [1]: This city is fifty-five miles southwest of Topeka.
- `d7s2` Council Grove, Kansas [2]: It was named after an agreement between European Americans and the Osage Nation about allowing settlers' wagon trains to pass through the area and proceed to the West.
- `d7s3` Council Grove, Kansas [3]: Pioneers gathered at a grove of trees so that wagons could band together for their trip west.
- `d7s4` Council Grove, Kansas [4]: As of the 2010 census, the city population was 2,182.
- `d8s0` KID77 [0]: KID77 (sometimes referred to as Kansas City All Hazards) is a NOAA Weather Radio station that serves the Kansas City metropolitan area and surrounding cities.
- `d8s1` KID77 [1]: It is programmed from the National Weather Service forecast office in Pleasant Hill, Missouri with its transmitter located in Independence.
- `d8s2` KID77 [2]: It broadcasts weather and hazard information for the following Counties and Cities
- `d9s0` Fort Osage [0]: Fort Osage (also known as Fort Clark or Fort Sibley) was an early 19th-century factory trading post system ran by the United States, being located in present-day Sibley, Missouri.
- `d9s1` Fort Osage [1]: The Treaty of Fort Clark was signed with certain members of the Osage Nation in 1808 calling for the creation of Fort Osage.
- `d9s2` Fort Osage [2]: It was one of three forts established by the U.S. Army to establish control over the newly acquired Louisiana Purchase territories.
- `d9s3` Fort Osage [3]: Fort Madison in SE Iowa was built to control trade and pacify Native Americans in the Upper Mississippi River region.
- `d9s4` Fort Osage [4]: Fort Belle Fontaine near St. Louis controlled the mouth of the Missouri.
- `d9s5` Fort Osage [5]: The fort ceased operations in the 1820s as the Osage in subsequent treaties ceded the rest of their land in Missouri.
- `d9s6` Fort Osage [6]: A replica of the fort was rebuilt on the site between 1948 and 1961.
- `d9s7` Fort Osage [7]: The Fort Osage school district (including Fort Osage High School), which serves northeast Independence and the surrounding area, was named after it.
- `d10s0` National Weather Service Boise, Idaho [0]: The National Weather Service Boise, Idaho is a weather forecast office responsible for weather forecasts, warnings and local statements as well as aviation weather forecasts and fire weather forecasts for 3 counties in Southeast Oregon and 14 counties in Southwest and South central Idaho.
- `d10s1` National Weather Service Boise, Idaho [1]: The U.S. Weather Bureau established an office in the Sonna Building on December 1, 1898.
- `d10s2` National Weather Service Boise, Idaho [2]: Since then, the U.S Weather Bureau office, now known as the National Weather Service forecast office gained forecast responsibility of Southern Idaho on June 22, 1970 which was expanded to the entire state of Idaho in 1973.
- `d10s3` National Weather Service Boise, Idaho [3]: After modernization in 1993, the forecast responsibility was changed to Southeast Oregon and Southwest Idaho.
- `d10s4` National Weather Service Boise, Idaho [4]: The current office in Boise maintains a WSR-88D (NEXRAD) radar system, 8 Automated airport weather station (ASOS) systems and Advanced Weather Interactive Processing System (AWIPS) that greatly improve forecasting in the region.
- `d10s5` National Weather Service Boise, Idaho [5]: Continuous weather observations have been maintained for the city of Boise since February 1, 1964 about 5 months after the U.S. Army established Fort Boise.
- `d10s6` National Weather Service Boise, Idaho [6]: The post surgeon for the U.S. Army took observations until July 1, 1877 when the U.S. Signal Service, established an office downtown.
- `d10s7` National Weather Service Boise, Idaho [7]: The Signal Office was discontinued on July 1, 1890.

</details>

## Q259 — `hotpotqa_5ac294b955429921a00aafd0` (revised draft)

> Which magazine was created first, Macworld or Soaps In Depth?

Source answer: Macworld

Gold final answer: Macworld

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: start year of Macworld as a print magazine | false | 1984 | — | [d10s1] | — |
| u2: creation year of Soaps In Depth | false | 1997 | — | [d6s0] | — |
| u3: Which magazine was created first, Macworld or Soaps In Depth? | true | Macworld | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d6s0` Soaps In Depth [0]: Soaps In Depth is a series of magazines created in 1997 by Bauer Publications to give American soap opera viewers more variety in their soap-related magazine purchases.
- `d10s1` Macworld [1]: It started life as a print magazine in 1984 and had the largest audited circulation (both total and newsstand) of Macintosh-focused magazines in North America, more than double its nearest competitor, "MacLife" (formerly "MacAddict").

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` United States Peace Index [0]: The United States Peace Index (USPI) is a measurement of American States and cities by their peacefulness.
- `d1s1` United States Peace Index [1]: Created by the Institute for Economics and Peace, the creators of the Global Peace Index, it is said to be the first in a series of National sub-divisions by their peacefulness.
- `d1s2` United States Peace Index [2]: The USPI was created first due to plentiful data and a large amount of diversity between states for level of peace.
- `d1s3` United States Peace Index [3]: The United States ranked 88/158 on the Global Peace index for 2012.
- `d1s4` United States Peace Index [4]: The U.S. index was released on 6 April 2011, at 00:01 Eastern Time and the second edition released on 24 April 2012.
- `d2s0` Viscount Powerscourt [0]: Viscount Powerscourt ( ) is a title that has been created three times in the Peerage of Ireland, each time for members of the Wingfield family.
- `d2s1` Viscount Powerscourt [1]: It was created first in 1618 for the Chief Governor of Ireland, Richard Wingfield.
- `d2s2` Viscount Powerscourt [2]: However, this creation became extinct on his death in 1634.
- `d2s3` Viscount Powerscourt [3]: It was created a second time in 1665 for Folliott Wingfield.
- `d2s4` Viscount Powerscourt [4]: He was the great-great-grandson of George Wingfield, uncle of the first Viscount of the 1618 creation.
- `d2s5` Viscount Powerscourt [5]: However, the 1665 creation also became extinct on the death of its first holder in 1717.
- `d3s0` Transition scenario [0]: Transition scenarios are descriptions of future states which combine a future image with an account of the changes that would need to occur to reach that future.
- `d3s1` Transition scenario [1]: These two elements are often created in a two-step process where the future image is created first (envisioning) followed by an exploration of the alternative pathways available to reach the future goal (backcasting).
- `d3s2` Transition scenario [2]: Both these processes can use participatory techniques (Raskin et al., 2002) where participants of varying backgrounds and interests are provided with an open and supportive group environment to discuss different contributing elements and actions.
- `d4s0` Baron Trevor [0]: Baron Trevor is a title that has been created three times.
- `d4s1` Baron Trevor [1]: It was created first in 1662 in the Peerage of Ireland along with the viscountcy of Dungannon.
- `d4s2` Baron Trevor [2]: For information on this creation, which became extinct in 1706, see Viscount Dungannon.
- `d5s0` CJ the DJ [0]: CJ the DJ is an Australian animated TV series created first broadcast on ABC3.
- `d5s1` CJ the DJ [1]: The show was created by Mark Gravas of "Yakkity Yak" fame and writer Stu Connolly.
- `d6s0` Soaps In Depth [0]: Soaps In Depth is a series of magazines created in 1997 by Bauer Publications to give American soap opera viewers more variety in their soap-related magazine purchases.
- `d6s1` Soaps In Depth [1]: Instead of buying a magazine like "Soap Opera Digest", in which all soap operas are covered, "Soaps In Depth" gave the soap viewer and potential shopper individual choices from the "Big Three" networks: ABC Soaps In Depth, CBS Soaps In Depth, and NBC Soaps In Depth.
- `d6s2` Soaps In Depth [2]: Each magazine is devoted to only the shows on the network the edition covers and is published biweekly.
- `d7s0` Soap Opera Update [0]: Soap Opera Update was a magazine dedicated to the coverage of soap operas, co-founded by Angela Shapiro in 1988.
- `d7s1` Soap Opera Update [1]: The magazine was published every three week.
- `d7s2` Soap Opera Update [2]: It was purchased by Bauer Media Group in 1992.
- `d7s3` Soap Opera Update [3]: The magazine became popular on newsstands in the mid-1990s.
- `d7s4` Soap Opera Update [4]: However, due to a lack of subscriptions and promotion, and criticisms for mediocre content and "lazy" press coverage, the magazine was discontinued in late 2002.
- `d7s5` Soap Opera Update [5]: In 2006, the "Update" began issuing "Soaps In Depth" and releasing an annual issue to review the soaps of the past year and preview soaps for the new year.
- `d8s0` Valentine Browne, 1st Earl of Kenmare [0]: Valentine Browne, 1st Earl of Kenmare (January 1754 – 3 October 1812) was the Seventh Baronet Browne.
- `d8s1` Valentine Browne, 1st Earl of Kenmare [1]: He was created First Baron Castlerosse and First Viscount Kenmare on 12 February 1798, with the earlier peerages not being recognised.
- `d8s2` Valentine Browne, 1st Earl of Kenmare [2]: He was created First Earl of Kenmare on 3 January 1801.
- `d9s0` Thomas Browne, 4th Viscount Kenmare [0]: Thomas Browne, 6th Baronet & 4th Viscount Kenmare (April 1726 – 11 September 1795) was an Irish landowner and politician.
- `d9s1` Thomas Browne, 4th Viscount Kenmare [1]: He was probably born at Killarney, County Kerry, the second of four children of Valentine Browne, fifth Baronet, third Viscount Kenmare (1695–1736), one of the few remaining great Roman Catholic landowners in Ireland, and his first wife, Honoria Butler (?
- `d9s2` Thomas Browne, 4th Viscount Kenmare [2]: -1730).
- `d9s3` Thomas Browne, 4th Viscount Kenmare [3]: Thomas Browne's great-grandfather, Sir Valentine Browne, third Baronet, had been created first Viscount Kenmare by James II in March 1689.
- `d9s4` Thomas Browne, 4th Viscount Kenmare [4]: This was an Irish peerage created after the removal of James II from the English throne, but during the period when James was de facto king of Ireland, before the conquest of Ireland by William III.
- `d9s5` Thomas Browne, 4th Viscount Kenmare [5]: The first and second viscounts had fought for James II but seem never to have been formally attainted under William.
- `d9s6` Thomas Browne, 4th Viscount Kenmare [6]: Consequently, the peerage remained on the Irish patent roll in a constitutionally ambiguous position, but was not formally recognised by the Protestant political establishment.
- `d10s0` Macworld [0]: Macworld is a web site dedicated to products and software of Apple Inc., published by Mac Publishing, which is headquartered in San Francisco, California.
- `d10s1` Macworld [1]: It started life as a print magazine in 1984 and had the largest audited circulation (both total and newsstand) of Macintosh-focused magazines in North America, more than double its nearest competitor, "MacLife" (formerly "MacAddict").
- `d10s2` Macworld [2]: "Macworld" was founded by David Bunnell (publisher) and Andrew Fluegelman (editor).
- `d10s3` Macworld [3]: It was the oldest Macintosh magazine still in publication, until September 10, 2014, when IDG, its parent company, announced it was discontinuing the print edition and laid off most of the staff, while continuing an online version.

</details>

## Q260 — `hotpotqa_5ac2ae4155429921a00ab030` (revised draft)

> which  Australian politician represented  Electoral district of Goulburn

Source answer: Jane Goward

Gold final answer: Pru Goward

Question type: `single` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: Australian politician representing Goulburn in the source | true | Pru Goward (accepted alternatives: Prudence Jane Goward; Jane Goward) | — | [d9s1] OR [d3s3] | — |

Evidence:

- `d3s3` Pru Goward [3]: Goward is a member of the New South Wales Legislative Assembly representing Goulburn for the Liberal Party of Australia since 2007.
- `d9s1` Electoral district of Goulburn [1]: It is represented by Pru Goward of the Liberal Party of Australia.

Notes:

- 删除全名桥接，按标题可解析Goward，补d3s3备选；接受Pru和全名以及源短名。

<details><summary>All source context</summary>

- `d1s0` Electoral district of Broken Hill [0]: Broken Hill was an electoral district of the Legislative Assembly in the Australian state of New South Wales.
- `d1s1` Electoral district of Broken Hill [1]: From 1894 to 1913, the Broken Hill district was covered by the electoral districts of "Broken Hill", Willyama and Sturt.
- `d1s2` Electoral district of Broken Hill [2]: In the 1912 redistribution, the electoral district of "Broken Hill" was abolished and absorbed into "Willyama" and "Sturt".
- `d1s3` Electoral district of Broken Hill [3]: In 1920, "Willyama", "Sturt" and the electoral district of Cobar were combined to create a three-member "Sturt".
- `d1s4` Electoral district of Broken Hill [4]: In 1927, single-member electorates were recreated and the city of Broken Hill was split between "Sturt" and Murray.
- `d1s5` Electoral district of Broken Hill [5]: From 1932, the city of Broken Hill was split between "Sturt" and Cobar.
- `d1s6` Electoral district of Broken Hill [6]: In 1968 "Sturt" was renamed Broken Hill and included all of the city of Broken Hill.
- `d1s7` Electoral district of Broken Hill [7]: In 1999, it was merged with part of "Murray" and renamed the electoral district of Murray-Darling.
- `d2s0` Joshua Arthur [0]: Joshua George Arthur (27 January 1906 – 20 May 1974) was an Australian politician who represented the Electoral district of Hamilton (1935–50) and the Electoral district of Kahibah (1950–53) for the Australian Labor Party.
- `d3s0` Pru Goward [0]: Prudence Jane Goward (born 2 September 1952 in Adelaide), an Australian politician, is the New South Wales Minister for Family and Community Services and Minister for Social Housing, since January 2017 in the Berejiklian government, and the Minister for Prevention of Domestic Violence and Sexual Assault, since 2015.
- `d3s1` Pru Goward [1]: She has previously served as the Minister for Mental Health, Minister for Medical Research, and Assistant Minister for Health between April 2015 and January 2017, and the Minister for Women between 2011 and January 2017, in the second Baird government and the Minister for Planning during 2014 and 2015.
- `d3s2` Pru Goward [2]: With the first Berejiklian government she returned to Community Services portfolio which she previously held between 2011 and 2014, in the O'Farrell and first Baird governments.
- `d3s3` Pru Goward [3]: Goward is a member of the New South Wales Legislative Assembly representing Goulburn for the Liberal Party of Australia since 2007.
- `d4s0` Electoral district of Southern Boroughs [0]: Southern Boroughs was a former electoral district for the Legislative Assembly in the Australian state of New South Wales created in 1856.
- `d4s1` Electoral district of Southern Boroughs [1]: It included the towns of Goulburn, Braidwood, Yass and Queanbeyan, while the surrounding rural area were in the electoral districts of Argyle, United Counties of Murray and St Vincent and King and Georgiana.
- `d4s2` Electoral district of Southern Boroughs [2]: It was replaced by Goulburn, Braidwood, Queanbeyan and Yass in 1859.
- `d5s0` Electoral district of Queanbeyan [0]: Queanbeyan was an electoral district of the Legislative Assembly in the Australian state of New South Wales from 1859 to 1913, in the Queanbeyan area.
- `d5s1` Electoral district of Queanbeyan [1]: It replaced parts of the electoral district of United Counties of Murray and St Vincent and the electoral district of Southern Boroughs.
- `d5s2` Electoral district of Queanbeyan [2]: It was merged with the electoral district of Monaro in 1913, when much of its former territory had been absorbed in the Australian Capital Territory.
- `d6s0` Electoral district of Argyle [0]: Argyle was an electoral district for the Legislative Assembly in the Australian State of New South Wales from 1856 to 1904, including Argyle County surrounding Goulburn.
- `d6s1` Electoral district of Argyle [1]: The town of Goulburn was in Southern Boroughs from 1856 to 1859 and then Goulburn.
- `d7s0` Buttala Electoral District [0]: Buttala electoral district was an electoral district of Sri Lanka between August 1947 and March 1960.
- `d7s1` Buttala Electoral District [1]: The district was named after the town of Buttala in Moneragala District, Uva Province.
- `d7s2` Buttala Electoral District [2]: The 1978 Constitution of Sri Lanka introduced the proportional representation electoral system for electing members of Parliament.
- `d7s3` Buttala Electoral District [3]: The existing 160 mainly single-member electoral districts were replaced with 22 multi-member electoral districts. Buttala electoral district is now represented by the Monaragala multi-member electoral district.
- `d8s0` Electoral district of Goulburn (Victoria) [0]: Electoral district of Goulburn was an electoral district of the Legislative Assembly in the Australian state of Victoria.
- `d8s1` Electoral district of Goulburn (Victoria) [1]: It was preceded by the Electoral district of Goulburn Valley, which was abolished in 1945.
- `d9s0` Electoral district of Goulburn [0]: Goulburn is an electoral district of the Legislative Assembly in the Australian state of New South Wales.
- `d9s1` Electoral district of Goulburn [1]: It is represented by Pru Goward of the Liberal Party of Australia.
- `d10s0` Electoral district of Goulburn Valley [0]: The Electoral district of Goulburn Valley was an electoral district of the Victorian Legislative Assembly.
- `d10s1` Electoral district of Goulburn Valley [1]: The district was replaced by the district of Goulburn in 1945.

</details>

## Q261 — `hotpotqa_5ae65d055542996d980e7b14` (revised draft)

> What was population of the city where the Dutch retired footballer Foeke Booy born?

Source answer: 108,249

Gold final answer: 108,249

Question type: `bridge` (source type `bridge`)

Replaces: `hotpotqa_5ac2cb3e5542996773102627`

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: city where Foeke Booy was born | false | Leeuwarden | — | [d5s0] | — |
| u2: population of {u1} in the source | true | 108,249 | u1 | [d1s0] | — |

Evidence:

- `d1s0` Leeuwarden [0]: Leeuwarden (] , ] ), Stadsfries: "Liwwadden") is a city and municipality with a population of 108,249 in Friesland in the Netherlands.
- `d5s0` Foeke Booy [0]: Foeke Booy (born 25 April 1962 in Leeuwarden) is a Dutch retired footballer and football manager.

Notes:

- 替换：third after A and B未明确两者顺序，不能支持紧邻的next smaller关系。 新题保留原source type，人工核对两条显式事实及答案。

<details><summary>All source context</summary>

- `d1s0` Leeuwarden [0]: Leeuwarden (] , ] ), Stadsfries: "Liwwadden") is a city and municipality with a population of 108,249 in Friesland in the Netherlands.
- `d1s1` Leeuwarden [1]: It is the provincial capital of the States of Friesland.
- `d2s0` Ivo den Bieman [0]: Ivo den Bieman (born 4 February 1967 in Wamel, Gelderland) is a Dutch retired footballer who played the majority of his career in Scotland.
- `d2s1` Ivo den Bieman [1]: He moved to Scotland in 1990 to attend Aberdeen University having previously played for Dutch amateur side SV Leones.
- `d3s0` Mitchell Elshot [0]: Mitchell Elshot (born 14 April 1995, Amsterdam) is a Dutch retired footballer who played for Eerste Divisie club Almere City FC during the 2012-2013 football season.
- `d4s0` Arturo ten Heuvel [0]: Arturo ten Heuvel (born 20 December 1978) is a Dutch retired footballer who played for HFC Haarlem, FC Volendam, FC Den Bosch, KSV Roeselare, Katwijk and Ajax Zaterdag during the span of his playing career.
- `d4s1` Arturo ten Heuvel [1]: He is currently a youth coach, managing the D2 squad (under-13) at Almere City FC.
- `d5s0` Foeke Booy [0]: Foeke Booy (born 25 April 1962 in Leeuwarden) is a Dutch retired footballer and football manager.
- `d6s0` Gerard Kerkum [0]: Gerard Kerkum (born 17 December 1930) is a Dutch retired footballer and was twice chairman of Dutch football team Feyenoord Rotterdam.
- `d7s0` Michel Kuipers [0]: Michel Kuipers (born 26 June 1974) is a Dutch retired footballer who played as a goalkeeper.
- `d7s1` Michel Kuipers [1]: Prior to football he served with the Dutch Marine Corps.
- `d7s2` Michel Kuipers [2]: He became a football agent after finishing his playing career.
- `d8s0` Reginald Faria [0]: Reginald Faria (born November 1981 in Amsterdam, Netherlands) is a Dutch retired footballer who played for Dutch Eredivisie Club FC Volendam during 2003-2004 season.
- `d9s0` Jeffrey Hoogervorst [0]: Jeffrey Hoogervorst (born 23 October 1984) is a Dutch retired footballer who plays as a central defender.
- `d10s0` Adilson Dos Santos [0]: Adilson Ben David Dos Santos (born 15 May 1974) is a Dutch retired footballer.

</details>

## Q262 — `hotpotqa_5ac2ed41554299218029db96` (revised draft)

> Which genus has more species, Monstera or Cercis?

Source answer: Monstera

Gold final answer: Monstera

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: species count of Monstera | false | about 50 | — | [d1s0] | — |
| u2: species count of Cercis | false | about 10 | — | [d3s0] | — |
| u3: Which genus has more species, Monstera or Cercis? | true | Monstera | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d1s0` Monstera [0]: Monstera is a genus of about 50 species of flowering plants in the arum family, Araceae, native to tropical regions of the Americas.
- `d3s0` Cercis [0]: Cercis , is a genus of about 10 species in the subfamily Cercidoideae of the pea family Fabaceae, native to warm temperate regions.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Monstera [0]: Monstera is a genus of about 50 species of flowering plants in the arum family, Araceae, native to tropical regions of the Americas.
- `d1s1` Monstera [1]: The genus is named from the Latin word for "monstrous" or "abnormal", and refers to the unusual leaves with natural holes that members of the genus have.
- `d2s0` Rhaphidophora tetrasperma [0]: Rhaphidophora tetrasperma (common names: "Mini Monstera", Philodendron "Ginny", Philodendron "Piccolo") is a species of plant in the family Araceae, genus "Rhaphidophora".
- `d2s1` Rhaphidophora tetrasperma [1]: It is native to Southern Thailand and to Malaysia.
- `d3s0` Cercis [0]: Cercis , is a genus of about 10 species in the subfamily Cercidoideae of the pea family Fabaceae, native to warm temperate regions.
- `d3s1` Cercis [1]: It contains small deciduous trees or large shrubs commonly known as redbuds.
- `d3s2` Cercis [2]: They are characterised by simple, rounded to heart-shaped leaves and pinkish-red flowers borne in the early spring on bare leafless shoots, on both branches and trunk ("cauliflory").
- `d3s3` Cercis [3]: Cercis is derived from the Greek word κερκις ("kerkis") meaning "weaver's shuttle", which was applied by Theophrastus to "C. siliquastrum".
- `d4s0` Cercidiphyllum [0]: Cercidiphyllum is a genus containing two species of plants, both commonly called katsura.
- `d4s1` Cercidiphyllum [1]: They are the sole members of the monotypic family Cercidiphyllaceae.
- `d4s2` Cercidiphyllum [2]: The genus is native to Japan and China and unrelated to "Cercis" (redbuds).

</details>

## Q263 — `hotpotqa_5ac2f34455429921a00ab0b6` (revised draft)

> What university did Bill Daly graduate that Gary Bettman also graduated from?

Source answer: New York University School of Law

Gold final answer: New York University School of Law

Question type: `comparison` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: schools from which Bill Daly received degrees | false | Dartmouth College; New York University School of Law | — | [d10s3] | — |
| u2: schools from which Gary Bettman graduated | false | Cornell University; New York University School of Law | — | [d3s2] | — |
| u3: school common to {u1} and {u2} | true | New York University School of Law | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d3s2` Gary Bettman [2]: Bettman is a graduate of Cornell University and New York University School of Law.
- `d10s3` Bill Daly [3]: He received his bachelor's degree from Dartmouth College and his law degree from New York University School of Law.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` 2011–12 Winnipeg Jets season [0]: The 2011–12 Winnipeg Jets season was the 13th season for the National Hockey League franchise and the first in Winnipeg, Manitoba, after 12 seasons as the Atlanta Thrashers.
- `d1s1` 2011–12 Winnipeg Jets season [1]: The franchise played in Atlanta since the 1999–2000 NHL season, and relocated to Winnipeg following the conclusion of the 2010–11 NHL season.
- `d1s2` 2011–12 Winnipeg Jets season [2]: The relocation of the Thrashers to Winnipeg was confirmed by NHL Commissioner Gary Bettman on May 31, 2011, and approved by the NHL Board of Governors on June 21, 2011.
- `d1s3` 2011–12 Winnipeg Jets season [3]: The 2011 season also marks the first appearance of the Winnipeg Jets name in the NHL since the previous franchise moved from Winnipeg to Phoenix in 1996.
- `d1s4` 2011–12 Winnipeg Jets season [4]: At the end of the year, the team failed to qualify for a playoff spot.
- `d2s0` William Merrigan Daly [0]: William Merrigan Daly, Jr., known to friends and colleagues as Bill Daly (1 September 1887, in Cincinnati – 3 December 1936, in New York City), was a pianist, composer, songwriter, orchestrator, musical director and conductor.
- `d3s0` Gary Bettman [0]: Gary Bruce Bettman (born June 2, 1952) is the commissioner of the National Hockey League (NHL), a post he has held since February 1, 1993.
- `d3s1` Gary Bettman [1]: Previously, Bettman was a senior vice president and general counsel to the National Basketball Association (NBA).
- `d3s2` Gary Bettman [2]: Bettman is a graduate of Cornell University and New York University School of Law.
- `d4s0` Leinster Ladies Senior Club Football Championship [0]: The Leinster Ladies senior football club championship has been running since 1978.
- `d4s1` Leinster Ladies Senior Club Football Championship [1]: The trophy is named after the man who presented it, Bill Daly, a Cavanman who lived in Dublin and was involved with Ballyboden St Endas.
- `d4s2` Leinster Ladies Senior Club Football Championship [2]: Foxrock Cabinteely (Dublin) are the current holders having secured their second ever title and will represent Leinster in the All Ireland series, where they will face Carnacon of Mayo.
- `d5s0` 58th National Hockey League All-Star Game [0]: The 58th National Hockey League All-Star Game, also known as the 2011 National Hockey League All-Star Game presented by Discover, was the National Hockey League's (NHL) annual All-Star Game played on January 30, 2011.
- `d5s1` 58th National Hockey League All-Star Game [1]: The game took place during the 2010–11 NHL season at the RBC Center in Raleigh, North Carolina, home of the Carolina Hurricanes.
- `d5s2` 58th National Hockey League All-Star Game [2]: Originally, the Game was supposed to be hosted by the Phoenix Coyotes, but due to ownership issues, the NHL decided to move the game.
- `d5s3` 58th National Hockey League All-Star Game [3]: After bidding for the game reopened, it was awarded to Carolina and fulfilled a nine-year-old promise made to the franchise by NHL Commissioner Gary Bettman.
- `d6s0` Gil Stein (ice hockey) [0]: Gilbert Stein (born 1928) is an American lawyer, law instructor and former professional ice hockey executive.
- `d6s1` Gil Stein (ice hockey) [1]: Stein served with the National Hockey League (NHL) as vice-president and legal counsel for nearly 15 years before becoming the fifth and last president of the NHL in 1992.
- `d6s2` Gil Stein (ice hockey) [2]: Stein served in that role for a year until shortly after the owners appointed Gary Bettman to the newly created post of commissioner.
- `d6s3` Gil Stein (ice hockey) [3]: Stein was initially inducted into the Hockey Hall of Fame in 1993, but withdrew after allegations that he had improperly manipulated his own nomination.
- `d6s4` Gil Stein (ice hockey) [4]: Since leaving the NHL, Stein has served as a lawyer and taught sports law.
- `d7s0` Rick Howland [0]: Richard "Rick" Howland is a Canadian actor known for his role as Trick on "Lost Girl" and Harry Buttman (a parody of Gary Bettman) in "Bon Cop, Bad Cop".
- `d8s0` Toni Janke [0]: Toni Janke is a contemporary Indigenous female singer/songwriter.
- `d8s1` Toni Janke [1]: She is a mother of two and was one of Australia's youngest Indigenous university graduates.
- `d8s2` Toni Janke [2]: She graduated with a combined Bachelor of Arts/Law from the University of NSW in 1989.
- `d8s3` Toni Janke [3]: She won a Deadly in 2002 for Female Artist of The Year.
- `d8s4` Toni Janke [4]: Janke has Aboriginal, Torres Strait Islander, Malay and Filipino heritage.
- `d8s5` Toni Janke [5]: She also graduated from the Australian Catholic University School of Theology where she obtained a Graduate Certificate in Ministry in 2012 and has worked in government, Indigenous media, the arts, education and pastoral ministry.
- `d8s6` Toni Janke [6]: She lives in Brisbane and works in the community sector.
- `d9s0` Bill Daly (footballer) [0]: Bill Daly ( 7 November 1892 – 26 September 1980) was an Australian rules footballer who played with Melbourne and South Melbourne in the Victorian Football League (VFL).
- `d10s0` Bill Daly [0]: William "Bill" L. Daly III (born May 1, 1964) is an American attorney and the current deputy commissioner and chief legal officer of the National Hockey League (NHL) under commissioner, Gary Bettman.
- `d10s1` Bill Daly [1]: He is also a Hockey Hall of Fame board member and former NHL vice president and chief legal officer.
- `d10s2` Bill Daly [2]: Before joining the NHL front office he worked for the New York law firm of Skadden, Arps, Slate, Meagher & Flom, LLP.
- `d10s3` Bill Daly [3]: He received his bachelor's degree from Dartmouth College and his law degree from New York University School of Law.
- `d10s4` Bill Daly [4]: He is a big fan of the Miami Dolphins, and currently resides in Bethesda, Maryland.

</details>

## Q264 — `hotpotqa_5ac2f6b8554299677310265f` (revised draft)

> Henry W. Bloch School of Management is named after the founder of an American tax preparation company that is based where?

Source answer: Kansas City

Gold final answer: Kansas City

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: company founded by the person after whom Henry W. Bloch School of Management is named | false | H&R Block | — | [d4s2] | — |
| u2: city where {u1} is based | true | Kansas City | u1 | [d9s1] | — |

Evidence:

- `d4s2` Henry W. Bloch School of Management [2]: It is named after Alumnus Henry W. Bloch, founder of H&R Block.
- `d9s1` H&amp;R Block [1]: The Kansas City-based company also offers payroll, and business consulting services.

Notes:

- 同句给出冠名人物及公司，合并为公司定位unit，保留公司到所在地的真正第二跳。

<details><summary>All source context</summary>

- `d1s0` David Renz [0]: David O. Renz is a professor of public policy and the director of the Midwest Center for Nonprofit Leadership at the Henry W. Bloch School of Management at the University of Missouri-Kansas City (UMKC).
- `d2s0` LibraTax [0]: LibraTax is a company that provides a tax preparation tool, attributed as the first to calculate tax obligations for bitcoin traders.
- `d2s1` LibraTax [1]: It is a standalone tool that creates a Schedule D for taxes owed to the Internal Revenue Service and not a complete suite of tax preparation tools.
- `d3s0` American Tax Funding [0]: American Tax Funding (ATF) is a private company based in Jupiter, Florida that engages in the purchasing and servicing of delinquent municipal real estate tax lien sales.
- `d3s1` American Tax Funding [1]: Originally formed in 1997 as Transamerica Municipal Finance (TMF), a division of Transamerica Corporation.
- `d3s2` American Tax Funding [2]: In August 2000 the founders completed a form of a management buyout of TMF, creating ATF.
- `d3s3` American Tax Funding [3]: ATF currently buys and services real estate tax liens in over 14 states and has provided over $1 billion in relief to local governments.
- `d3s4` American Tax Funding [4]: Many ATF tax liens are secured by either Wells Fargo Foot Hill or the Harris Nesbitt Corporation.
- `d3s5` American Tax Funding [5]: The process of privatizing the municipal tax foreclosures process and outsourcing to out of state third party, for-profit, private companies has drawn criticism from housing advocates who argue that a for-profit tax foreclosure process leads to more foreclosures, displacement and vacancy.
- `d3s6` American Tax Funding [6]: The other argument is that third party purchases of tax liens enables local governments to pay for essential services such as salaries for teachers, health care, police officers and firefighters.
- `d3s7` American Tax Funding [7]: To date, no study has shown that the sale of tax liens to third parties leads to any increase in foreclosure activity.
- `d3s8` American Tax Funding [8]: In fact, the sale of liens to third party purchasers often extends redemption periods and allows flexible repayment agreements for delinquent tax payers.
- `d4s0` Henry W. Bloch School of Management [0]: Henry W. Bloch School of Management (formerly known as Henry W. Bloch School of Business and Public Administration) is an AACSB accredited business school founded in 1952 at the University of Missouri-Kansas City in Kansas City, Missouri.
- `d4s1` Henry W. Bloch School of Management [1]: It offers undergraduate and graduate degrees in Business, Accounting and Public Administration.
- `d4s2` Henry W. Bloch School of Management [2]: It is named after Alumnus Henry W. Bloch, founder of H&R Block.
- `d4s3` Henry W. Bloch School of Management [3]: The Bloch School also offers NASPAA accredited degrees in Public administration.
- `d5s0` TurboTax [0]: TurboTax is an American tax preparation software package developed by Michael A. Chipman of Chipsoft in the mid-1980s.
- `d5s1` TurboTax [1]: Intuit acquired Chipsoft, based in San Diego, in 1993.
- `d5s2` TurboTax [2]: Chipsoft, now known as Intuit Consumer Tax Group, is still based in San Diego, having moved into a new office complex in 2007.
- `d5s3` TurboTax [3]: Intuit Corporation is headquartered in Mountain View, California.
- `d6s0` Free File Alliance [0]: The Free File Alliance is a group of tax preparation companies that have partnered with the Internal Revenue Service to provide free electronic tax filing services to U.S tax payers meeting certain guidelines.
- `d6s1` Free File Alliance [1]: The Free File Alliance claims that the program benefits American taxpayers by providing services that would cost the IRS money to provide if online tax filing were administered directly by the IRS.
- `d6s2` Free File Alliance [2]: The IRS stipulates filers must have an adjusted gross income (AGI) of $62,000 or less for tax year 2015, but participating companies have their own requirements and restrictions.
- `d7s0` TaxAct [0]: TaxAct is an American tax preparation software package.
- `d7s1` TaxAct [1]: It is a member of the Free File Alliance, a free federal tax preparation and electronic filing program for eligible individual taxpayers developed through a partnership between the IRS and a group of private sector tax software companies.
- `d8s0` Liberty Tax Service [0]: Liberty Tax Service is an American company specializing in the preparation of tax returns for individuals and small businesses.
- `d8s1` Liberty Tax Service [1]: It is the third largest tax preparation franchise in the United States.
- `d8s2` Liberty Tax Service [2]: The company began in Canada in 1997 when John Hewitt, co-founder of Jackson Hewitt, acquired a Canadian tax franchisor, U&R Tax Depot.
- `d8s3` Liberty Tax Service [3]: In 1998, the company became Liberty Tax Service and opened five offices in the United States.
- `d8s4` Liberty Tax Service [4]: Liberty Tax Service is the primary subsidiary of Liberty Tax, Inc., a NASDAQ-traded company.
- `d9s0` H&amp;R Block [0]: H&R Block is an American tax preparation company in North America, Australia, and India.
- `d9s1` H&amp;R Block [1]: The Kansas City-based company also offers payroll, and business consulting services.
- `d10s0` Nicholas Peroff [0]: Nicholas C. Peroff (born May 19, 1944) is an American political scientist, public administrator and professor in Native American studies and Complexity Theory at the Henry W. Bloch School of Management at the University of Missouri-Kansas City, he formerly held teaching positions in Taiwan, South Korea and South Africa.

</details>

## Q265 — `hotpotqa_5ac300905542996773102682` (revised draft)

> Devilment finally found a stable vocalist in the founding member of which band?

Source answer: Cradle of Filth

Gold final answer: Cradle of Filth

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: stable vocalist who joined Devilment | false | Dani Filth | — | [d3s1] | — |
| u2: band of which {u1} is a founding member | true | Cradle of Filth | u1 | [d5s0] | — |

Evidence:

- `d3s1` Devilment [1]: The band experienced problems finding a stable vocalist until Dani Filth from the extreme metal band Cradle of Filth joined.
- `d5s0` Dani Filth [0]: Dani Filth (born Daniel Lloyd Davey) is the lyricist, vocalist and founding member of the metal band Cradle of Filth.

Notes:

- 保留d3s1→d5s0两跳。d3s1只说明来自Cradle of Filth，未说明创始成员；题干没有点名该乐队，也不能排除他在多个乐队任职，故不把一般成员关系直接升级为founder捷径。

<details><summary>All source context</summary>

- `d1s0` Ronnie Radke [0]: Ronald Joseph Radke (born December 15, 1983) is an American singer, songwriter, entertainer, and record producer born in Las Vegas, Nevada.
- `d1s1` Ronnie Radke [1]: He is the founding member and current lead vocalist, keyboardist, and recently guitarist for the rock band Falling in Reverse, and is the former vocalist and founding member of post-hardcore band Escape the Fate.
- `d2s0` I Finally Found My Way [0]: "I Finally Found My Way" is a song by the American hard rock band Kiss released on their 1998 album "Psycho Circus".
- `d3s0` Devilment [0]: Devilment are a British heavy metal band originally formed in late 2011.
- `d3s1` Devilment [1]: The band experienced problems finding a stable vocalist until Dani Filth from the extreme metal band Cradle of Filth joined.
- `d3s2` Devilment [2]: They released their first studio album, "The Great And Secret Show", on 3 November 2014.
- `d4s0` The Next Step (Kurt Rosenwinkel album) [0]: The Next Step is Kurt Rosenwinkel's fourth album as a band leader.
- `d4s1` The Next Step (Kurt Rosenwinkel album) [1]: It is his second release on Verve, and regarded as a major step in his creative evolution.
- `d4s2` The Next Step (Kurt Rosenwinkel album) [2]: Rosenwinkel himself, says of the album, "It represents the culmination of many life phases for me.
- `d4s3` The Next Step (Kurt Rosenwinkel album) [3]: Some of these phases started ten years ago and have finally found resolution in this record.
- `d4s4` The Next Step (Kurt Rosenwinkel album) [4]: It represents the next step in my music and in my life".
- `d4s5` The Next Step (Kurt Rosenwinkel album) [5]: The album debuts a number of Rosenwinkel compositions which would become staples of his live performances and would also be rerecorded on his albums, Deep Song and Star of Jupiter.
- `d4s6` The Next Step (Kurt Rosenwinkel album) [6]: This material was developed by the band during their frequent gigs at Smalls Jazz Club in New York City.
- `d4s7` The Next Step (Kurt Rosenwinkel album) [7]: Mitch Borden, the club's owner recalled that "Kurt Rosenwinkel's band played with such dramatic fire, that it would consume everyone present".
- `d4s8` The Next Step (Kurt Rosenwinkel album) [8]: The Next Step features several songs with alternate guitar tunings, as well as Kurt Rosenwinkel's piano playing on one tune.
- `d5s0` Dani Filth [0]: Dani Filth (born Daniel Lloyd Davey) is the lyricist, vocalist and founding member of the metal band Cradle of Filth.
- `d6s0` Dan Finch [0]: Daniel J Finch (born 21 December 1977) is a metal vocalist and guitarist.
- `d6s1` Dan Finch [1]: He is currently in The Dead Soul Communion and The Devils Music.
- `d6s2` Dan Finch [2]: Finch has also released a number of sample and loops packages.
- `d6s3` Dan Finch [3]: He grew up in Lowestoft, Suffolk.
- `d6s4` Dan Finch [4]: He has one daughter Alice Grace Finch who was born on 31 December 2011.
- `d6s5` Dan Finch [5]: Finch was the founding member of Devilment which he formed in 2011.
- `d6s6` Dan Finch [6]: But songs were written as far back as 2001, when the band was called Brutal Grooves Inc.
- `d7s0` Jonas Renkse [0]: Jonas Petter Renkse (born 19 May 1975) is a founding member, songwriter, lead vocalist (1991–1994, 1997-) and ex-drummer (1991–1994, 1996–1998) of the band Katatonia, founding member, songwriter, bassist, backing vocalist, ex-guitarist (2004) of the band Bloodbath.
- `d8s0` Cain Hoy Stable [0]: Cain Hoy Stable was a Thoroughbred racing stable and horse breeding operation with training facilities in Columbia, South Carolina and Kissimmee, Florida.
- `d8s1` Cain Hoy Stable [1]: It was owned by Harry Guggenheim who also raced horses in Europe.
- `d8s2` Cain Hoy Stable [2]: A founding member of the New York Racing Association, Guggenheim began racing in 1929 and originally raced as the Falaise Stable, the name of his Long Island, New York estate.
- `d8s3` Cain Hoy Stable [3]: In 1943 he renamed it the Cain Hoy Stable for his Cain Hoy Plantation, a 15000 acre timber and cattle plantation near Wando, South Carolina.
- `d9s0` Jeff Caxide [0]: Jeff Caxide is an American bassist, best known for his time with post-metal band Isis, of which he was a founding member and present until its dissolution in 2010.
- `d9s1` Jeff Caxide [1]: He was also a founding member of Red Sparowes, but left after the release of their first full-length.
- `d9s2` Jeff Caxide [2]: He also contributed to side-project Spylacopa.
- `d9s3` Jeff Caxide [3]: Prior to his time in Isis, he was a touring member of the Boston metalcore band 454 Big Block.
- `d9s4` Jeff Caxide [4]: He also helped found Connecticut-based metalcore band Cable, for whom he played bass.
- `d9s5` Jeff Caxide [5]: His stay with the band as a musician was brief, but he did return in order to produce 1999's "Gutter Queen".
- `d10s0` Los Guerreros del Infierno [0]: Los Guerreros del Infierno (Spanish for "The Warriors From Hell") is a "Lucha Libre" (Professional wrestling) stable based in Consejo Mundial de Lucha Libre (CMLL) in Mexico that has existed since 2000.
- `d10s1` Los Guerreros del Infierno [1]: The group was created as a splinter group of "Los Infernales" and initially used the name until they were forced to change their name in 2001 and then became Los Guerreros del Infierno.
- `d10s2` Los Guerreros del Infierno [2]: When Atlantis joined the group in 2005 they adopted the name "Los Guerreros de la Atlantida", which is used interchangeably with the "Guerreros del Infierno" name.
- `d10s3` Los Guerreros del Infierno [3]: The stable currently consists of founding member Último Guerrero as well as Gran Guerrero and Euforia.

</details>

## Q266 — `hotpotqa_5a7b5e55554299042af8f755` (revised draft)

> Which author was born first, Lorraine Hansberry or Sandra Gulland?

Source answer: Lorraine Vivian Hansberry

Gold final answer: Lorraine Hansberry

Question type: `comparison` (source type `comparison`)

Replaces: `hotpotqa_5ac31ad4554299741d48a1ee`

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: birth year of Lorraine Hansberry | false | 1930 | — | [d4s0] | — |
| u2: birth year of Sandra Gulland | false | 1944 | — | [d6s0] | — |
| u3: Which author was born first, Lorraine Hansberry or Sandra Gulland? | true | Lorraine Hansberry (accepted alternatives: Lorraine Vivian Hansberry) | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d4s0` Lorraine Hansberry [0]: Lorraine Vivian Hansberry (May 19, 1930 – January 12, 1965) was an African-American playwright and writer.
- `d6s0` Sandra Gulland [0]: Sandra Gulland (born November 3, 1944) is an American-born Canadian novelist.

Notes:

- 替换：Ainslee文档未给出版频率。 新题保留原source type，人工核对两条显式事实及答案。

<details><summary>All source context</summary>

- `d1s0` Lorraine Hansberry Hall [0]: Lorraine Hansberry Hall (built 1973) is a residence hall at Lincoln University, named for author and playwright Lorraine Hansberry.
- `d1s1` Lorraine Hansberry Hall [1]: Since its opening, Lorraine Hansberry Hall has been used to house freshmen women.
- `d1s2` Lorraine Hansberry Hall [2]: In January 2003 the Women’s Center was opened in the basement as a wellness resource directed for female students.
- `d1s3` Lorraine Hansberry Hall [3]: The basement of Lorraine Hansberry Hall is also the location for the large laundry area for the residents.
- `d2s0` Young, Black, and Determined [0]: Young, Black, and Determined: A Biography of Lorraine Hansberry is a 1998 book by Patricia and Fredrick McKissack.
- `d2s1` Young, Black, and Determined [1]: It is a biography of the playwright and activist, Lorraine Hansberry.
- `d3s0` The Lorraine Hansberry Theatre [0]: The Lorraine Hansberry Theatre is named after the acclaimed playwright of "A Raisin in the Sun".
- `d3s1` The Lorraine Hansberry Theatre [1]: She wrote the play while living in Bay Area.
- `d3s2` The Lorraine Hansberry Theatre [2]: Since being founded in 1981, The Lorraine Hansberry Theatre has mounted productions that have included performances by Ruby Dee, Ossie Davis, Danny Glover and Ntozake Shange.
- `d3s3` The Lorraine Hansberry Theatre [3]: The Lorraine Hansberry Theatre is the first African-American arts institution to be located in downtown San Francisco.
- `d4s0` Lorraine Hansberry [0]: Lorraine Vivian Hansberry (May 19, 1930 – January 12, 1965) was an African-American playwright and writer.
- `d5s0` To Be Young, Gifted and Black (play) [0]: "To Be Young, Gifted and Black: Lorraine Hansberry in her Own Words", was written by Lorraine Hansberry, an American writer best known for her 1957 play "A Raisin in the Sun", a play that made Hansberry the first black author of a show on Broadway.
- `d5s1` To Be Young, Gifted and Black (play) [1]: After her death in 1965, Hansberry's ex-husband and friend, songwriter and poet Robert Nemiroff, collated her unpublished writings and adapted them into a stage play that first ran from 1968 to 1969 off Broadway.
- `d5s2` To Be Young, Gifted and Black (play) [2]: It was then converted into an equally successful autobiography with the same title.
- `d6s0` Sandra Gulland [0]: Sandra Gulland (born November 3, 1944) is an American-born Canadian novelist.
- `d6s1` Sandra Gulland [1]: She is the author of "The Shadow Queen" and "Mistress of the Sun", novels set in the court of Louis XIV, The Sun King, and a trilogy of novels based on the life of Josephine Bonaparte: "The Many Lives & Secret Sorrows of Josephine B."; "Tales of Passion, Tales of Woe"; "The Last Great Dance on Earth".
- `d7s0` Carl Augustus Hansberry [0]: Carl Augustus Hansberry (April 30, 1895—March 17, 1946) was an American real estate broker, inventor and political activist.
- `d7s1` Carl Augustus Hansberry [1]: He was also the father of award-winning playwright Lorraine Hansberry and the great-grandfather of actress Taye Hansberry.
- `d8s0` William Leo Hansberry [0]: William Leo Hansberry (February 25, 1894 – November 3, 1965) was an American scholar and lecturer.
- `d8s1` William Leo Hansberry [1]: He was the older brother of real estate broker Carl Augustus Hansberry, uncle of award-winning playwright Lorraine Hansberry and great-granduncle of actress Taye Hansberry.
- `d9s0` Hansberry College Prep [0]: Hansberry College Prep, formerly known as "Noble Auburn Gresham College Prep", is a public four-year charter high school located in the Auburn Gresham in Chicago, Illinois.
- `d9s1` Hansberry College Prep [1]: It is a part of the Noble Network of Charter Schools.
- `d9s2` Hansberry College Prep [2]: Hansberry College Prep opened its doors in 2012 as Noble Auburn Gresham College Prep in recognition of the neighborhood in which the school resides.
- `d9s3` Hansberry College Prep [3]: In July 2013, the campus changed its name to Hansberry College Prep in honor of Lorraine Hansberry, an African-American writer and playwright who grew up on Chicago's south side and who worked to combat racial segregation in the 1950s and 1960s.
- `d9s4` Hansberry College Prep [4]: Hansberry College Prep currently serves grades nine through twelve and will graduate its first class in 2016.
- `d10s0` Les Blancs [0]: Les Blancs is a play written by Lorraine Hansberry.
- `d10s1` Les Blancs [1]: It debuted on Broadway on November 15, 1970 and ran until December 19 of that same year.
- `d10s2` Les Blancs [2]: It debuted to heavy criticism.
- `d10s3` Les Blancs [3]: It was Lorraine Hansberry’s final work and she considered it her most important, as it depicts the plights of colonialism in the late 19th and early 20th centuries.
- `d10s4` Les Blancs [4]: It is her only play that takes place in Africa, and it uses dance and music both as signifiers of black and African cultures; a concept called the Black Aesthetic.

</details>

## Q267 — `hotpotqa_5ac3295d5542995ef918c14d` (revised draft)

> What role in the TV show "Death in Paradise" was played by the man who performed with Alexander Armstrong in the podcast "Timeghost"?

Source answer: Richard Poole

Gold final answer: Richard Poole

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: performer with Alexander Armstrong in Timeghost | false | Ben Miller | — | [d3s0, d3s1] | — |
| u2: role played by {u1} in Death in Paradise | true | Richard Poole (accepted alternatives: DI Richard Poole) | u1 | [d8s3] | — |

Evidence:

- `d3s0` Armstrong and Miller [0]: Armstrong and Miller are an English stand-up comedy double act consisting of the actor-comedians Alexander Armstrong and Ben Miller.
- `d3s1` Armstrong and Miller [1]: They have performed in two eponymous television sketch shows, the satirical "Timeghost" podcast, and many individual television appearances.
- `d8s3` Ben Miller [3]: Miller is also known for playing the lead role of DI Richard Poole in the first 2 series of the BBC Crime Drama "Death in Paradise".

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` TLC (TV series) [0]: TLC is a darkly surreal farce-like sitcom set in a fictional NHS hospital called South Middlesex.
- `d1s1` TLC (TV series) [1]: Written by Fintan Coyle, co-creator of hit game show "Weakest Link", it was first broadcast on the BBC on 11 November 2002 and ran over six episodes until 16 December.
- `d1s2` TLC (TV series) [2]: There were some very mixed opinions on the show among both critics and viewers, but it achieved decent ratings and featured an excellent comedy cast including Richard Griffiths, Alexander Armstrong and "The League of Gentlemen's" Reece Shearsmith.
- `d1s3` TLC (TV series) [3]: The series was released on DVD in the UK on 29 October 2007.
- `d2s0` Alexander Armstrong's Big Ask [0]: Alexander Armstrong's Big Ask is a British comedy panel show hosted by Alexander Armstrong.
- `d2s1` Alexander Armstrong's Big Ask [1]: The pilot was shown on Dave on 30 May 2011.
- `d2s2` Alexander Armstrong's Big Ask [2]: The guests on the pilot were Robert Webb, Katy Brand and Griff Rhys Jones.
- `d2s3` Alexander Armstrong's Big Ask [3]: After a positive reaction to the pilot, Dave ordered a full series which was filmed in October 2011 and broadcast from 6 February 2012.
- `d2s4` Alexander Armstrong's Big Ask [4]: A second series began 26 February 2013.
- `d3s0` Armstrong and Miller [0]: Armstrong and Miller are an English stand-up comedy double act consisting of the actor-comedians Alexander Armstrong and Ben Miller.
- `d3s1` Armstrong and Miller [1]: They have performed in two eponymous television sketch shows, the satirical "Timeghost" podcast, and many individual television appearances.
- `d4s0` Don't Ask Me Ask Britain [0]: Don't Ask Me Ask Britain is a British television comedy panel game show that has aired on ITV since 18 April 2017 and is hosted by Alexander Armstrong with Frank Skinner and Jonathan Ross as the team captains.
- `d4s1` Don't Ask Me Ask Britain [1]: The series is produced by Chalkboard TV for ITV.
- `d4s2` Don't Ask Me Ask Britain [2]: The goal is for the two teams to second-guess what the viewers will vote for in various questions by using an app and voting along live.
- `d5s0` Micro Men [0]: Micro Men, working title Syntax Era is a one-off BBC drama television show set in the late 1970s and the early-mid 1980s, about the rise of the British home computer market.
- `d5s1` Micro Men [1]: It focuses on the rivalry between Sir Clive Sinclair (played by Alexander Armstrong), who developed the ZX Spectrum, and Chris Curry (played by Martin Freeman), the man behind the BBC Micro.
- `d6s0` Pointless [0]: Pointless is a British quiz show produced by Endemol UK for the BBC, hosted by Alexander Armstrong and Richard Osman.
- `d6s1` Pointless [1]: Each episode of the quiz features teams of two contestants attempting to find correct but obscure answers to general knowledge questions in order to score as few points as possible, and become eligible to compete for the show's cash jackpot.
- `d6s2` Pointless [2]: All questions used on the show are factual in nature, and are asked to a panel of 100 individuals in a pre-conducted public survey.
- `d6s3` Pointless [3]: Contestants seek to find correct answers that were given by as few participants as possible; those given by no participants are termed "pointless" and are the most desirable.
- `d6s4` Pointless [4]: Every pointless answer given during the main game increases the jackpot by £250, and one such answer must be given in the final round in order to win it.
- `d7s0` Combat Jack [0]: Reggie Ossé, also known as Combat Jack (born July 8, 1969 in Brooklyn, New York) is a former hip hop music attorney and executive, and also the former managing editor of "The Source".
- `d7s1` Combat Jack [1]: He is the host of the podcast "The Combat Jack Show" and founding partner of the Loud Speakers Podcast network.
- `d7s2` Combat Jack [2]: He was also the host of the Complex TV show version of the Combat Jack Show podcast.
- `d8s0` Ben Miller [0]: Bennet Evan "Ben" Miller (born 24 February 1966) is an English comedian, actor and director.
- `d8s1` Ben Miller [1]: He is best known as one half of comedy double act Armstrong and Miller, with Alexander Armstrong.
- `d8s2` Ben Miller [2]: Miller and Armstrong wrote and starred in the Channel 4 sketch show "Armstrong and Miller", as well as the BBC sketch show "The Armstrong & Miller Show".
- `d8s3` Ben Miller [3]: Miller is also known for playing the lead role of DI Richard Poole in the first 2 series of the BBC Crime Drama "Death in Paradise".
- `d9s0` Saurabh Pandey [0]: Saurabh Pandey(born 11 May 1988) is an Indian Television and Bollywood actor.
- `d9s1` Saurabh Pandey [1]: His debut TV show as lead was Siddharth Basu's first Fiction TV show Jiya Jale for 9X TV in (2007).
- `d9s2` Saurabh Pandey [2]: He later played the role of Shaurya in his second TV show titled "Shaurya aur Suhani" for Star Plus channel.
- `d9s3` Saurabh Pandey [3]: He also played the role of protagonist in shows like Tere Mere Sapne, Ganga Kii Dheej and Razia Sultan.
- `d10s0` Armstrong and Miller (TV series) [0]: Armstrong and Miller - later retitled The Armstrong and Miller Show - is a comedy sketch television show that aired between 1997 and 2001 featuring Alexander Armstrong and Ben Miller, known together as Armstrong and Miller.
- `d10s1` Armstrong and Miller (TV series) [1]: Following a series on the Paramount Comedy Channel in 1997, a further three were made for Channel 4.

</details>

## Q268 — `hotpotqa_5ac3b04f55429939154138b7` (revised draft)

> Which railway is a part of Summerseat and also runs between Heywood and Rawtenstall?

Source answer: East Lancashire Railway

Gold final answer: East Lancashire Railway

Question type: `single` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: railway serving Summerseat and running between Heywood and Rawtenstall | true | East Lancashire Railway | — | [d5s1] OR [d6s0] | — |

Evidence:

- `d5s1` Summerseat railway station [1]: It is part of the Heritage East Lancashire Railway (which runs for 12 miles from Heywood-Rawtenstall).
- `d6s0` East Lancashire Railway [0]: The East Lancashire Railway is a 12+1/2 mi heritage railway line in north west England which runs between Heywood and Rawtenstall with intermediate stations at Bury Bolton Street, Burrs Country Park , Summerseat, Ramsbottom and Irwell Vale.

Notes:

- 每句都同时满足两个条件，合并为single且两句互为备选。

<details><summary>All source context</summary>

- `d1s0` Helsinki–Riihimäki railway [0]: Helsinki–Riihimäki railway is a railway running between the Helsinki Central railway station and the Riihimäki railway station in Finland.
- `d1s1` Helsinki–Riihimäki railway [1]: It was opened in 1862 as a part of the Finland's first railway between Helsinki and Hämeenlinna.
- `d1s2` Helsinki–Riihimäki railway [2]: The Helsinki commuter rail system also runs by the Helsinki–Riihimäki railway.
- `d2s0` Heywood railway station, Victoria [0]: Heywood railway station is a disused station on the Portland railway line in the town of Heywood, in the state of Victoria, Australia.
- `d2s1` Heywood railway station, Victoria [1]: The last passenger train between Ararat and Portland was on 12 September 1981, operated by a DRC railcar.
- `d2s2` Heywood railway station, Victoria [2]: The platform and station building are still in place at Heywood, although in a disused condition.
- `d2s3` Heywood railway station, Victoria [3]: Some of the former yard remains as unconnected broad gauge track, with power connections also provided to a work camp area.
- `d2s4` Heywood railway station, Victoria [4]: The former goods shed was removed by October 1983, and the through line was converted to standard gauge in 1995.
- `d3s0` The Wise Woman of Hoxton [0]: The Wise Woman of Hoxton is a city comedy by the early modern English playwright Thomas Heywood.
- `d3s1` The Wise Woman of Hoxton [1]: It was published under the title "The Wise-Woman of Hogsdon" in 1638, though it was probably first performed c. 1604 by the Queen's Men company (of which Heywood was a shareholder), either at The Curtain or perhaps The Red Bull.
- `d3s2` The Wise Woman of Hoxton [2]: The play is set in Hoxton, an area that at the time was outside the boundaries of the city of London and notorious for its entertainments and recreations.
- `d3s3` The Wise Woman of Hoxton [3]: The Victorian critic F. G. Fleay suggested that Heywood, who was also an actor, originally played the part of Sencer.
- `d3s4` The Wise Woman of Hoxton [4]: It has often been compared with Ben Jonson's comic masterpiece "The Alchemist" (1610)—the poet T. S. Eliot, for example, argued that with this play Heywood "succeeds with something not too far below Jonson to be comparable to that master's work".
- `d4s0` Swanage railway station [0]: Swanage railway station is a railway station located in Swanage, on the Isle of Purbeck in the English county of Dorset.
- `d4s1` Swanage railway station [1]: Originally the terminus of a London and South Western Railway (L&SWR) branch line from Wareham, the line and station were closed by British Rail in 1972.
- `d4s2` Swanage railway station [2]: It has since reopened as a station on the Swanage Railway, a heritage railway that currently runs from Norden station just north of Corfe Castle to Swanage station.
- `d4s3` Swanage railway station [3]: It now also runs to Wareham on certain services, but not on regular services due to signalling problems.
- `d5s0` Summerseat railway station [0]: Summerseat railway station is a preserved railway station that serves the village of Summerseat in Greater Manchester, England.
- `d5s1` Summerseat railway station [1]: It is part of the Heritage East Lancashire Railway (which runs for 12 miles from Heywood-Rawtenstall).
- `d6s0` East Lancashire Railway [0]: The East Lancashire Railway is a 12+1/2 mi heritage railway line in north west England which runs between Heywood and Rawtenstall with intermediate stations at Bury Bolton Street, Burrs Country Park , Summerseat, Ramsbottom and Irwell Vale.
- `d7s0` Rawtenstall to Bacup Line [0]: The Rawtenstall to Bacup railway line opened in two stages, from Rawtenstall to Waterfoot in 1848, and from Waterfoot to the Bacup terminus in 1852.
- `d7s1` Rawtenstall to Bacup Line [1]: There were stations at Rawtenstall, Cloughfold, Stacksteads and Bacup.
- `d7s2` Rawtenstall to Bacup Line [2]: The line was doubled in 1880, at the same time as the line from Bacup to Rochdale was also opened (closed 1947).
- `d7s3` Rawtenstall to Bacup Line [3]: Passenger and freight services operated until the Beeching cuts in 1966, the last passenger train running on December 5th 1966 and the track being lifted in 1969.
- `d8s0` South Coast Line [0]: The South Coast Line is an intercity rail service operated by NSW TrainLink that services the Illawarra region of New South Wales, Australia.
- `d8s1` South Coast Line [1]: The service runs from , and runs the entire length of the eponymous South Coast railway line to .
- `d8s2` South Coast Line [2]: The service also runs along the Eastern Suburbs railway line at peak hours and the Port Kembla railway line to .
- `d8s3` South Coast Line [3]: It is operated with NSW TrainLink H sets and Sydney Trains T sets, with Endeavour railcars operating the service on the non-electrified line between and Bomaderry.
- `d9s0` Don River Railway [0]: The Don River Railway is a volunteer run vintage railway and museum in Don, a suburb of Devonport, Tasmania.
- `d9s1` Don River Railway [1]: It runs a passenger train ride from Don to Coles Beach and return using part of the former Don River Line that ran between Don Junction and Paloona.
- `d9s2` Don River Railway [2]: The service is usually run Wednesday through to Sunday inclusive.
- `d9s3` Don River Railway [3]: Don River Railway is open every day except Good Friday and Christmas Day.
- `d9s4` Don River Railway [4]: On operating weekdays, customer can expect to ride in either a 1940s ex TGR rail car, or diesel locomotive pulling heritage carriages, whilst steam locomotives usually run on weekends.
- `d9s5` Don River Railway [5]: .
- `d9s6` Don River Railway [6]: The railway also runs a number of diesel locomotives numbered V2, X4, Y6 and 866.
- `d9s7` Don River Railway [7]: Numerous other locomotives and rolling stock are in the process of being restored at the on-site workshop.
- `d10s0` Southern Railway of British Columbia [0]: The Southern Railway of British Columbia, branded as SRY Rail Link (reporting mark SRY) is a Canadian short line railway operating in the southwestern British Columbia.
- `d10s1` Southern Railway of British Columbia [1]: The main facility is the port at Annacis Island with major import of cars, export of forestry products, and other shipments.
- `d10s2` Southern Railway of British Columbia [2]: The railway has interconnections with three Class I railroads, including Canadian Pacific (CP), Canadian National (CN) and Burlington Northern Santa Fe (BNSF).
- `d10s3` Southern Railway of British Columbia [3]: It operates a fleet of 29 locomotives, mostly consisting of EMD GP-9 & SW900 locomotives.
- `d10s4` Southern Railway of British Columbia [4]: It also rosters 5 unique Ex.
- `d10s5` Southern Railway of British Columbia [5]: Canadian National Railway GMD-1 locomotives, and also runs 3 SD38-2 locomotives, and 1 SD38AC.
- `d10s6` Southern Railway of British Columbia [6]: The railroad also operates a fleet 2,000 rail cars, SRY hauls approximately 70,000 carloads per year.
- `d10s7` Southern Railway of British Columbia [7]: It operates around 123 mi of track, 62 mi of which is mainline track.

</details>

## Q269 — `hotpotqa_5ac3b39e554299204fd21e09` (revised draft)

> Do Dillingham Airport and Rafael Hernández Airport both handle civilian (passenger) service?

Source answer: yes

Gold final answer: yes

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: whether Dillingham Airport handles passenger service | false | yes | — | [d9s1] | — |
| u2: whether Rafael Hernandez Airport handles passenger service | false | yes | — | [d3s0, d3s3] | — |
| u3: Do Dillingham Airport and Rafael Hernández Airport both handle civilian (passenger) service? | true | yes | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d3s0` Rafael Hernández Airport [0]: Rafael Hernández Airport (IATA: BQN, ICAO: TJBQ, FAA LID: BQN) is a joint civil-military airport located in Aguadilla, Puerto Rico.
- `d3s3` Rafael Hernández Airport [3]: Rafael Hernandez Airport mainly serves Puerto Rican westerners living in the Eastern Region of the United States.
- `d9s1` Dillingham Airport [1]: Scheduled passenger service is available at this airport.

Notes:

- 民军两用且主要服务居住于美国东部的波多黎各人，组合明确描述民用旅客服务；补u2并使u3可推导。d8s1只说charter，未区分客运货运，不单独接受。

<details><summary>All source context</summary>

- `d1s0` Koliganek Airport [0]: Koliganek Airport (IATA: KGK, ICAO: PAJZ, FAA LID: JZZ) is a state-owned, public-use airport located one nautical mile (1.85 km) east of the central business district of Koliganek, in the Dillingham Census Area of the U.S. state of Alaska.
- `d1s1` Koliganek Airport [1]: Scheduled airline service to Dillingham Airport is provided by Peninsula Airways (PenAir).
- `d2s0` Puerto Rico Firefighters Corps [0]: The Puerto Rico Firefighters Corps —Spanish: "Cuerpo de Bomberos de Puerto Rico" (CBPR)— is the statewide fire department that provides fire protection, rescue, and protection from other hazards in Puerto Rico.
- `d2s1` Puerto Rico Firefighters Corps [1]: It was established in 1942 under the Puerto Rico Fire Services.
- `d2s2` Puerto Rico Firefighters Corps [2]: In addition, it offers fire protection services to all the airports under the authority of the Puerto Rico Ports Authority, including the Luis Muñoz Marin International Airport, Rafael Hernández Airport, and Mercedita Airport and they serve as crash rescue divisions.
- `d2s3` Puerto Rico Firefighters Corps [3]: A separate agency, the Puerto Rico Medical Emergency Corps, provides emergency medical services to all Puerto Rico.
- `d3s0` Rafael Hernández Airport [0]: Rafael Hernández Airport (IATA: BQN, ICAO: TJBQ, FAA LID: BQN) is a joint civil-military airport located in Aguadilla, Puerto Rico.
- `d3s1` Rafael Hernández Airport [1]: It is named after the Puerto Rican composer Rafael Hernández Marín and is the second largest international airport in Puerto Rico in the region of Porta del Sol, Puerto Rico's west coast.
- `d3s2` Rafael Hernández Airport [2]: It is also home to Coast Guard Air Station Borinquen.
- `d3s3` Rafael Hernández Airport [3]: Rafael Hernandez Airport mainly serves Puerto Rican westerners living in the Eastern Region of the United States.
- `d3s4` Rafael Hernández Airport [4]: The airport previously served as a focus city for PAWA Dominicana.
- `d4s0` Hernandez Houses [0]: Rafael Hernandez Houses, also known as Hernandez Houses, is a public housing development built and maintained by the New York City Housing Authority (NYCHA) on the Lower East Side of Manhattan at .
- `d4s1` Hernandez Houses [1]: The development is named after Rafael Hernández Marín (1892-1965), a Puerto Rican music composer who served in the United States Armed Forces during World War I.
- `d4s2` Hernandez Houses [2]: After studying music in Puerto Rico and Mexico, Rafael Hernández Marín travelled to New York City, then to Latin America; after he returned to his homeland Puerto Rico, he became the director of the Puerto Rican Symphonic Orchestra.
- `d5s0` Curaçao International Airport [0]: Hato International Airport or Curaçao International Airport (formerly "Dr. Albert Plesman International Airport") (IATA: CUR, ICAO: TNCC) is the airport of Willemstad, Curaçao.
- `d5s1` Curaçao International Airport [1]: It has services to the Caribbean region, South America, North America and Europe.
- `d5s2` Curaçao International Airport [2]: Hato Airport is a fairly large facility, with the third longest commercial runway in the Caribbean region after Rafael Hernández Airport in Puerto Rico and Pointe-à-Pitre International Airport in Guadeloupe.
- `d5s3` Curaçao International Airport [3]: The airport serves as a main base for Insel Air.
- `d6s0` Shannons Pond Seaplane Base [0]: Shannons Pond Seaplane Base (FAA LID: 0Z3) is a public-use seaplane base located three nautical miles (6 km) west of the central business district of Dillingham, a city in the Dillingham Census Area of the U.S. state of Alaska.
- `d6s1` Shannons Pond Seaplane Base [1]: As per Federal Aviation Administration records, this facility had 1,000 passenger boardings (enplanements) in calendar year 2008.
- `d6s2` Shannons Pond Seaplane Base [2]: It is 3 mi west of Dillingham Airport.
- `d7s0` Punta Borinquen Radar Station [0]: Punta Borinquen Radar Station is a facility of the Puerto Rico Air National Guard home for the 141st Air Control Squadron.
- `d7s1` Punta Borinquen Radar Station [1]: Located adjacent to Rafael Hernández Airport (which operates at the old Ramey Air Force Base), the facility has operated since 1964 when the 140th Aircraft Control and Warning Squadron (ACWS) was created under the control of Air Defense Command (ADC).
- `d8s0` Fina Air [0]: Fina Air was an airline based in San Juan, Puerto Rico named after Josefina Canto who was the mother of Lazaro Canto.
- `d8s1` Fina Air [1]: It operated charter flights to the Dominican Republic from Luis Muñoz Marín International Airport in San Juan, Rafael Hernández Airport in Aguadilla and Eugenio María de Hostos Airport in Mayagüez.
- `d8s2` Fina Air [2]: The airline has now ceased operations.
- `d9s0` Dillingham Airport [0]: Dillingham Airport (IATA: DLG, ICAO: PADL, FAA LID: DLG) is a state owned, public use airport located two nautical miles (4 km) west of the central business district of Dillingham, a city in the Dillingham Census Area of the U.S. state of Alaska.
- `d9s1` Dillingham Airport [1]: Scheduled passenger service is available at this airport.
- `d10s0` Twin Hills Airport [0]: Twin Hills Airport (IATA: TWA, FAA LID: A63) is a state-owned, public-use airport serving Twin Hills, in the Dillingham Census Area of the U.S. state of Alaska.
- `d10s1` Twin Hills Airport [1]: Scheduled airline service to Dillingham Airport is provided by Peninsula Airways (PenAir).

</details>

## Q270 — `hotpotqa_5a90b93f5542995651fb51ca` (revised draft)

> Which documentary was released earlier, Almost Sunrise or 51 Birch Street?

Source answer: 51 Birch Street

Gold final answer: 51 Birch Street

Question type: `comparison` (source type `comparison`)

Replaces: `hotpotqa_5ac41f1d5542991943173924`

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: film year of Almost Sunrise | false | 2016 | — | [d5s0] | — |
| u2: film year of 51 Birch Street | false | 2005 | — | [d10s0] | — |
| u3: Which documentary was released earlier, Almost Sunrise or 51 Birch Street? | true | 51 Birch Street | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d5s0` Almost Sunrise [0]: Almost Sunrise is a 2016 American documentary film directed by Michael Collins.
- `d10s0` 51 Birch Street [0]: 51 Birch Street is a 2005 documentary film about the universal themes of love, marriage, fidelity, and the mystery of a suburban family, directed by Doug Block.

Notes:

- 替换：缺少东西相对方位或经度。 新题保留原source type，人工核对两条显式事实及答案。

<details><summary>All source context</summary>

- `d1s0` Isanti County Courthouse [0]: The former Isanti County Courthouse, located at 237 2nd Avenue, South West, corner of Birch Street, in Cambridge, Minnesota, United States, is an historic two-story redbrick county courthouse built in 1888.
- `d1s1` Isanti County Courthouse [1]: Today it is known as Court House Square and has been remodeled into a private office building.
- `d2s0` William Thomas Abington House [0]: The William Thomas Abington House is a historic house located on Center Street in Beebe, Arkansas, midway between East Mississippi Street and Birch Street.
- `d3s0` Galbraith Mountain [0]: Galbraith Mountain is the common name for North Lookout Mountain, located between the communities of Sudden Valley and Bellingham, Washington.
- `d3s1` Galbraith Mountain [1]: A 3125 acre area was owned by the Trillium Corporation until April 1, 2010, when the company surrendered the property to Polygon Financial Partners instead of defaulting on the loan held by Polygon.
- `d3s2` Galbraith Mountain [2]: Galbraith Mountain has two main summits, which are 1365 ft and 1785 ft high.
- `d3s3` Galbraith Mountain [3]: Though they are not either of the highest points on Lookout mountain, they are prominent from all over Western Whatcom County.
- `d3s4` Galbraith Mountain [4]: The Whatcom Independent Mountain Pedalers (WHIMPs) created and maintained a large trail system under a 2005 contract with Trillium.
- `d3s5` Galbraith Mountain [5]: The mountain has many access points; the two most popular are from Birch Street, off of Lakeway Drive, and Galbraith Lane, off of Samish Way.
- `d4s0` Mayfield Brewery [0]: The Mayfield Brewery was a brewery that operated in Mayfield, California between years 1868 and 1920.
- `d4s1` Mayfield Brewery [1]: The brewery was located at what is now the corner of California Avenue and Birch Street in Palo Alto, California.
- `d4s2` Mayfield Brewery [2]: The brewery produced Steam beer and sold it in kegs to local saloons.
- `d4s3` Mayfield Brewery [3]: The brewery was shut down by Prohibition.
- `d5s0` Almost Sunrise [0]: Almost Sunrise is a 2016 American documentary film directed by Michael Collins.
- `d5s1` Almost Sunrise [1]: It recounts the story of two Iraq veterans, Tom Voss and Anthony Anderson, who, in an attempt to put their combat experience behind them, embark on a 2,700-mile trek on foot across America.
- `d5s2` Almost Sunrise [2]: It made its world premiere on the opening night of the Telluride Mountainfilm Festival on 27 May, 2016.
- `d6s0` Jerome Cooperative Creamery [0]: The Jerome Cooperative Creamery is a cooperative creamery and also refers to historic lava rock structures used by the creamery on Birch Street in Jerome, Idaho, United States.
- `d6s1` Jerome Cooperative Creamery [1]: The structures were listed on the National Register of Historic Places in 1983.
- `d6s2` Jerome Cooperative Creamery [2]: They were built in 1915, 1924, and 1933 by master stonemason H.T. Pugh who popularized the use of lava rock in the Jerome area.
- `d7s0` John Davis (entrepreneur) [0]: John F. Davis III (born 1953) is an entrepreneur, educator, CEO of Room Key, and a member of the Texas Christian University Board of Trustees.
- `d7s1` John Davis (entrepreneur) [1]: He is a co-founder of 1-800-Flowers and former CEO of both Pegasus Solutions and Birch Street Systems.
- `d8s0` St. Joseph's School (Biddeford, Maine) [0]: St. Joseph's School is a historic former school building on Birch Street in Biddeford, Maine.
- `d8s1` St. Joseph's School (Biddeford, Maine) [1]: Built in 1887, it was one of the first large masonry schools to be built in the state, and became a focal point for the migration of French Canadians into the state.
- `d8s2` St. Joseph's School (Biddeford, Maine) [2]: It was listed on the National Register of Historic Places in 1983.
- `d8s3` St. Joseph's School (Biddeford, Maine) [3]: It has been converted to residential use.
- `d9s0` In Search of Sunrise 6: Ibiza [0]: In Search of Sunrise 6: Ibiza (also known as ISOS 6) is the sixth album in the "In Search of Sunrise" series mixed by trance DJ/producer Tiësto, released on September 7, 2007 in the Netherlands and October 16, 2007 in the United States as a double disc album.
- `d9s1` In Search of Sunrise 6: Ibiza [1]: This information was confirmed on July 31, 2007 on Tiësto's website.
- `d9s2` In Search of Sunrise 6: Ibiza [2]: Many file-sharing websites, earlier in 2007, released a fake torrent of In Search of Sunrise 6, labeled In Search of Sunrise 6 - London, which even included a CD cover.
- `d9s3` In Search of Sunrise 6: Ibiza [3]: This was quickly noted as a fake as information of the CD had not been released via Tiësto's website nor the In Search of Sunrise series website.
- `d9s4` In Search of Sunrise 6: Ibiza [4]: A special release party was held at the Heineken Music Hall in Amsterdam on November 3, 2007.
- `d9s5` In Search of Sunrise 6: Ibiza [5]: Like previous "In Search of Sunrise" albums, this album contains a special slipcase.
- `d9s6` In Search of Sunrise 6: Ibiza [6]: The album picture was taken by Stephanie Pistel.
- `d9s7` In Search of Sunrise 6: Ibiza [7]: The compilation was awarded in the 2008 WMC Awards in Miami, it won for "Best Full Length DJ Mix CD".
- `d10s0` 51 Birch Street [0]: 51 Birch Street is a 2005 documentary film about the universal themes of love, marriage, fidelity, and the mystery of a suburban family, directed by Doug Block.

</details>
