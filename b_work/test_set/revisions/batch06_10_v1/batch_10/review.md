# Revised Gold — batch 10

原始review保持不变。本文是依据原note生成的修订草稿；完整修改说明见[修改报告](../change_report.md)。

句子带有文档标题；允许使用标题解析该文档中的人名及代词。support_sets内为AND，组间为OR；presupposition_sets按现有评估器表示预设捷径。

## Q271 — `hotpotqa_5adbe0df554299438c868cc0` (revised draft)

> Which writer was ordained to priesthood, W. Somerset Maugham or Thomas Merton?

Source answer: Thomas Merton

Gold final answer: Thomas Merton

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: whether W. Somerset Maugham was ordained to the priesthood | false | no | — | `[]`：无直接支持 | — |
| u2: whether Thomas Merton was ordained to the priesthood | false | yes | — | [d8s2] | — |
| u3: Which writer was ordained to priesthood, W. Somerset Maugham or Thomas Merton? | true | Thomas Merton **[by_presupposition]** | u1, u2 | `[[]]`：由全部依赖推出 | [d8s2] |

Evidence:

- `d8s2` Thomas Merton [2]: In 1949, he was ordained to the priesthood and given the name Father Louis.

Notes:

- 补两候选结构。按当前guide，ordination是事件而非职业，d9s0的作家职业介绍不能证明未受圣职；纠正旧note，保留Merton正向链路。

<details><summary>All source context</summary>

- `d1s0` International Thomas Merton Society [0]: The International Thomas Merton Society, founded in 1987, is a learned society which studies the works of American Catholic writer and mystic Thomas Merton.
- `d1s1` International Thomas Merton Society [1]: It sponsors conferences and co-publishes a journal, "The Merton Seasonal".
- `d1s2` International Thomas Merton Society [2]: The society and the Thomas Merton Center are located at Bellarmine University in Louisville, Kentucky, U.S.A.
- `d2s0` Thomas Merton Award [0]: The Thomas Merton Award has been awarded since 1972 by the Thomas Merton Center for Peace and Social Justice in Pittsburgh, United States.
- `d2s1` Thomas Merton Award [1]: It is named after Thomas Merton and is given annually to "national and international individuals struggling for justice."
- `d3s0` Somerset Maugham Award [0]: The Somerset Maugham Award is a British literary prize given each May by the Society of Authors.
- `d3s1` Somerset Maugham Award [1]: It is awarded to the best writer or writers of a book published in the past year who is under the age of 35.
- `d3s2` Somerset Maugham Award [2]: The prize was instituted in 1947 by William Somerset Maugham and thus bears his name.
- `d3s3` Somerset Maugham Award [3]: The award is to be spent on foreign travel.
- `d3s4` Somerset Maugham Award [4]: The total fund for each year is £12,000.
- `d4s0` The Razor's Edge (1946 film) [0]: The Razor's Edge is the first film version of W. Somerset Maugham's 1944 novel of the same name.
- `d4s1` The Razor's Edge (1946 film) [1]: It was released in 1946 and stars Tyrone Power, Gene Tierney, John Payne, Anne Baxter, Clifton Webb, Herbert Marshall, with a supporting cast including Lucile Watson, Frank Latimore and Elsa Lanchester.
- `d4s2` The Razor's Edge (1946 film) [2]: Marshall plays Somerset Maugham.
- `d4s3` The Razor's Edge (1946 film) [3]: The film was directed by Edmund Goulding.
- `d5s0` List of works about Thomas Merton [0]: The following is a list of works about Thomas Merton, publications about Thomas Merton, the Trappist monk from Abbey of Gethsemani.
- `d5s1` List of works about Thomas Merton [1]: The bibliography is organized into categories.
- `d5s2` List of works about Thomas Merton [2]: A separate list of works by Thomas Merton is also available.
- `d6s0` Robert Calder (writer) [0]: Robert Lorin Calder, a Canadian writer and professor, won the Governor General's Award for English-language non-fiction in 1989 for his "Willie: The Life of W. Somerset Maugham", a biography based on extensive archival work and interviews with surviving associates of Maugham, in particular Alan Searle.
- `d6s1` Robert Calder (writer) [1]: Unlike Ted Morgan, who had obtained permission from Maugham's executors to publish from Maugham's letters in his biography (1980), Calder was refused permission to do so by the Royal Literary Fund and had to rely on paraphrase in referencing Maugham's unpublished correspondence.
- `d7s0` St. Joseph's Intermediate and Commercial School [0]: St. Joseph's Intermediate and Commercial School (St. Joseph's Commercial School, SJICS, or St. Joe's Sherbourne) is a former Catholic High school located in the Cabbagetown neighbourhood of Toronto, Ontario, Canada part of the Metropolitan Separate School Board (now the Toronto Catholic District School Board).
- `d7s1` St. Joseph's Intermediate and Commercial School [1]: The school was later renamed to Thomas Merton Academy (Thomas Merton, TMA, or Merton) in 1985 after the Anglo-American monk Thomas Merton.
- `d8s0` Thomas Merton [0]: Thomas Merton, O.C.S.O. (January 31, 1915 – December 10, 1968) was an American Catholic writer, theologian and mystic.
- `d8s1` Thomas Merton [1]: A Trappist monk of the Abbey of Gethsemani, Kentucky, he was a poet, social activist, and student of comparative religion.
- `d8s2` Thomas Merton [2]: In 1949, he was ordained to the priesthood and given the name Father Louis.
- `d9s0` W. Somerset Maugham [0]: William Somerset Maugham CH ( ; 25 January 1874 – 16 December 1965), better known as W. Somerset Maugham, was a British playwright, novelist and short story writer.
- `d9s1` W. Somerset Maugham [1]: He was among the most popular writers of his era and reputedly the highest-paid author during the 1930s.
- `d10s0` Trio (film) [0]: Trio (also known as W. Somerset Maugham's Trio) is a 1950 British anthology film based on three short stories by W. Somerset Maugham: "The Verger", "Mr. Know-All" and "Sanatorium".
- `d10s1` Trio (film) [1]: Ken Annakin directed "The Verger" and "Mr. Know-All", while Harold French was responsible for "Sanatorium".

</details>

## Q272 — `hotpotqa_5adbfffb5542994650320c39` (revised draft)

> The McKinley Tariff was framed by the representative who was later assassinated in what month?

Source answer: September 1901

Gold final answer: September 1901

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: representative who framed the McKinley Tariff | false | William McKinley | — | [d5s0] | — |
| u2: month and year of {u1}'s assassination | true | September 1901 | u1 | [d9s0] | — |

Evidence:

- `d5s0` McKinley Tariff [0]: The Tariff Act of 1890, commonly called the McKinley Tariff, was an act of the United States Congress framed by Representative William McKinley that became law on October 1, 1890.
- `d9s0` William McKinley [0]: William McKinley (January 29, 1843 – September 14, 1901) was the 25th President of the United States from March 4, 1897 until his assassination in September 1901, six months into his second term.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Sook-ja Kim [0]: Sook-ja "Sue" Kim (born 1941) is a Korean-born U.S. singer.
- `d1s1` Sook-ja Kim [1]: She started singing with her sisters in a group called The Kim Sisters at the age of 10 and played 13 different instruments.
- `d1s2` Sook-ja Kim [2]: In 1950, the Korean War broke out and Sue Kim's father, Kim Hae-song, who was a famous Korean symphony orchestra conductor was captured by the North Korean army and later assassinated.
- `d1s3` Sook-ja Kim [3]: Her mother, Lee Nan-young, was left with no home, no food and no money for her and her seven children.
- `d1s4` Sook-ja Kim [4]: Lee was a famous Korean singer who rose to stardom with the song "Mokpo Tears."
- `d1s5` Sook-ja Kim [5]: In 1953, Lee asked the children to perform with her in South Korea's military clubs to support their family.
- `d1s6` Sook-ja Kim [6]: The GIs donated rock and roll records for the sisters to memorize and sing, and in turn the sisters received chocolate bars and alcohol, which they exchanged for food.
- `d1s7` Sook-ja Kim [7]: The GIs that returned to the States spread the word about the talented trio and in 1958, Tom Ball (who later became The Kim Sisters’ manager) heard about the sisters from one of the returning GIs and went to Korea to recruit them for an Asian act that he was producing.
- `d2s0` Wilson–Gorman Tariff Act [0]: The Revenue Act or Wilson-Gorman Tariff of 1894 (ch.
- `d2s1` Wilson–Gorman Tariff Act [1]: 349, §73, 28 Stat.
- `d2s2` Wilson–Gorman Tariff Act [2]: 570 , August 27, 1894) slightly reduced the United States tariff rates from the numbers set in the 1890 McKinley tariff and imposed a 2% income tax.
- `d2s3` Wilson–Gorman Tariff Act [3]: It is named for William L. Wilson, Representative from West Virginia, chair of the U.S. House Ways and Means Committee, and Senator Arthur P. Gorman of Maryland, both Democrats.
- `d3s0` Smoot–Hawley Tariff Act [0]: The Tariff Act of 1930 (codified at ), otherwise known as the Smoot–Hawley Tariff or Hawley–Smoot Tariff, was an act implementing protectionist trade policies sponsored by Senator Reed Smoot and Representative Willis C. Hawley and signed into law on June 17, 1930.
- `d3s1` Smoot–Hawley Tariff Act [1]: The act raised U.S. tariffs on over 20,000 imported goods.
- `d4s0` István Tisza [0]: Count István Tisza de Borosjenő et Szeged (archaically English: Stephen Tisza; 22 April 1861 – 31 October 1918) was a Hungarian politician, prime minister, political scientist and member of Hungarian Academy of Sciences.
- `d4s1` István Tisza [1]: The prominent event in his life was Austria-Hungary's entry into the First World War when he was prime minister for the second time.
- `d4s2` István Tisza [2]: He was later assassinated during the Chrysanthemum Revolution on 31 October 1918 - the same day that Hungary terminated its political union with Austria.
- `d4s3` István Tisza [3]: Tisza supported the dual monarchy of Austria-Hungary and was representative of the then "liberal-conservative consent".
- `d5s0` McKinley Tariff [0]: The Tariff Act of 1890, commonly called the McKinley Tariff, was an act of the United States Congress framed by Representative William McKinley that became law on October 1, 1890.
- `d5s1` McKinley Tariff [1]: The tariff raised the average duty on imports to almost fifty percent, an act designed to protect domestic industries from foreign competition.
- `d5s2` McKinley Tariff [2]: Protectionism, a tactic supported by Republicans, was fiercely debated by politicians and condemned by Democrats.
- `d5s3` McKinley Tariff [3]: The McKinley Tariff was replaced with the Wilson–Gorman Tariff Act in 1894, which promptly lowered tariff rates.
- `d6s0` United States elections, 1890 [0]: The 1890 United States elections occurred in the middle of Republican President Benjamin Harrison's term.
- `d6s1` United States elections, 1890 [1]: Members of the 52nd United States Congress were chosen in this election.
- `d6s2` United States elections, 1890 [2]: The Republicans suffered major losses due to the Panic of 1890 and the unpopularity of the McKinley Tariff.
- `d6s3` United States elections, 1890 [3]: The Populist Party also emerged as an important third party.
- `d7s0` Revenue Act of 1913 [0]: The Revenue Act of 1913, also known as the Tariff Act, the Underwood Tariff, the Underwood Act, the Underwood Tariff Act, or the Underwood-Simmons Act (ch.
- `d7s1` Revenue Act of 1913 [1]: 16, 38 Stat.
- `d7s2` Revenue Act of 1913 [2]: 114 , October 3, 1913), re-imposed the federal income tax after the ratification of the Sixteenth Amendment and lowered basic tariff rates from 40% to 25%, well below the Payne-Aldrich Tariff Act of 1909.
- `d7s3` Revenue Act of 1913 [3]: It was signed into law by President Woodrow Wilson on October 3, 1913 and was sponsored by Alabama Representative Oscar Underwood.
- `d8s0` Dingley Act [0]: The Dingley Act of 1897 (ch.
- `d8s1` Dingley Act [1]: 11, 30 Stat.
- `d8s2` Dingley Act [2]: 151 , July 24, 1897), introduced by U.S. Representative Nelson Dingley, Jr., of Maine, raised tariffs in United States to counteract the Wilson–Gorman Tariff Act of 1894, which had lowered rates.
- `d8s3` Dingley Act [3]: Came into effect under William McKinley the first year that he was in office.
- `d8s4` Dingley Act [4]: The McKinley administration wanted to slowly bring back the protectionism that was proposed by the Tariff of 1890.
- `d9s0` William McKinley [0]: William McKinley (January 29, 1843 – September 14, 1901) was the 25th President of the United States from March 4, 1897 until his assassination in September 1901, six months into his second term.
- `d9s1` William McKinley [1]: McKinley led the nation to victory in the Spanish–American War, raised protective tariffs to promote American industry, and maintained the nation on the gold standard in a rejection of inflationary proposals.
- `d10s0` Thomas Bowman (Iowa politician) [0]: Thomas Bowman (May 25, 1848 – December 1, 1917) was a local official, newspaper publisher, and one-term Democratic U.S. Representative from Iowa's 9th congressional district.
- `d10s1` Thomas Bowman (Iowa politician) [1]: Benefiting from an electoral backlash in 1890 against Republicans for their support of the McKinley Tariff, Bowman's election was a rare nineteenth century Democratic win in traditionally Republican southwestern Iowa.

</details>

## Q273 — `hotpotqa_5adcdea85542992c1e3a2441` (revised draft)

> What film adaptation do both Jerome Bernard and Ira Lewis have in common?

Source answer: Chinese Coffee

Gold final answer: Chinese Coffee

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: film adaptation of a play by Ira Lewis | false | Chinese Coffee | — | [d4s1, d4s2] | — |
| u2: film {u1} starring an actor whose name includes Jerome Bernard | true | Chinese Coffee | u1 | [d4s2, d3s0] | — |

Evidence:

- `d3s0` Jerry Orbach [0]: Jerome Bernard "Jerry" Orbach (October 20, 1935 – December 28, 2004) was an American actor and singer, described at the time of his death as "one of the last" bona fide" leading men of the Broadway musical and global celebrity on television" and a "versatile stage and film actor".
- `d4s1` Ira Lewis [1]: Lewis was best known for his one-act play, "Chinese Coffee", which opened at the Circle in the Square Theatre in 1992, starring Al Pacino.
- `d4s2` Ira Lewis [2]: A film adaptation of "Chinese Coffee", also starring Pacino, as well as Jerry Orbach, was released in 2000.

Notes:

- 先确定Ira Lewis戏剧的电影，再用演员表及完整姓名验证Jerome Bernard；不从部分姓名任意选Orbach。Karabel也不被误称为演员。

<details><summary>All source context</summary>

- `d1s0` Gerome Ragni [0]: Gerome Ragni (born Jerome Bernard Ragni; September 11, 1935 – July 10, 1991) was an American actor, singer and songwriter, best known as the co-author of the groundbreaking 1960s musical "".
- `d2s0` Les Misérables (1934 film) [0]: Les Misérables is a 1934 film adaptation of Victor Hugo's novel of the same name.
- `d2s1` Les Misérables (1934 film) [1]: It was written and directed by Raymond Bernard and stars Harry Baur as Jean Valjean and Charles Vanel as Javert.
- `d2s2` Les Misérables (1934 film) [2]: The film lasts four and a half hours and is considered by critics to be the greatest adaptation of the novel, due to its in-depth development of the themes and characters in comparison with most shorter adaptations.
- `d3s0` Jerry Orbach [0]: Jerome Bernard "Jerry" Orbach (October 20, 1935 – December 28, 2004) was an American actor and singer, described at the time of his death as "one of the last" bona fide" leading men of the Broadway musical and global celebrity on television" and a "versatile stage and film actor".
- `d4s0` Ira Lewis [0]: Ira Lewis Metsky (27 August 1932 — 4 April 2015) was an American actor, writer, and playwright.
- `d4s1` Ira Lewis [1]: Lewis was best known for his one-act play, "Chinese Coffee", which opened at the Circle in the Square Theatre in 1992, starring Al Pacino.
- `d4s2` Ira Lewis [2]: A film adaptation of "Chinese Coffee", also starring Pacino, as well as Jerry Orbach, was released in 2000.
- `d4s3` Ira Lewis [3]: Ira Lewis wrote the film's screenplay, while Pacino directed the adaptation.
- `d5s0` Never Gonna Dance [0]: Never Gonna Dance is a Broadway musical featuring the music of Jerome Kern.
- `d5s1` Never Gonna Dance [1]: The musical was based on the 1936 Fred Astaire/Ginger Rogers film "Swing Time".
- `d5s2` Never Gonna Dance [2]: Lyricists include Oscar Hammerstein, Ira Gershwin, P. G. Wodehouse, Bernard Dougall, Johnny Mercer, Jimmy McHugh, Otto Harbach, and Dorothy Fields.
- `d6s0` Pride and Prejudice (1940 film) [0]: Pride and Prejudice is a 1940 American film adaptation of Jane Austen's novel "Pride and Prejudice", directed by Robert Z. Leonard and starring Greer Garson and Laurence Olivier.
- `d6s1` Pride and Prejudice (1940 film) [1]: The screenplay was written by Aldous Huxley and Jane Murfin, adapted specifically from the stage adaptation by Helen Jerome in addition to Jane Austen's novel.
- `d6s2` Pride and Prejudice (1940 film) [2]: The film is about five sisters from an English family of landed gentry who must deal with issues of marriage, morality, and misconceptions.
- `d6s3` Pride and Prejudice (1940 film) [3]: The film was released by MGM on July 26, 1940 in the United States, and was critically well received.
- `d6s4` Pride and Prejudice (1940 film) [4]: "The New York Times" film critic praised the film as "the most deliciously pert comedy of old manners, the most crisp and crackling satire in costume that we in this corner can remember ever having seen on the screen."
- `d7s0` Ira Deutchman [0]: Ira Deutchman is best known as a producer, distributor and marketer of independent films, but in 2000, he moved into film exhibition as Co-Founder and Managing Partner of Emerging Pictures—a New York-based digital exhibition company, which was sold in January, 2015 to Vancouver-based 20 Year Media He also served as Chair of the Film Program at Columbia University School of the Arts from 2011 to 2015, where he has been a Professor of Professional Practice for more than 25 years.
- `d7s1` Ira Deutchman [1]: Deutchman is a member of The Academy of Motion Picture Arts and Sciences.
- `d7s2` Ira Deutchman [2]: He was one of the original creative advisors to the Sundance Institute and formerly served on the Board of Advisors for the Sundance Film Festival.
- `d7s3` Ira Deutchman [3]: He has also served as a Board member and former Board chair for the Independent Feature Project, the Board of Advisors for the Los Angeles Independent Film Festival, the Williamstown Film Festival, IFP/West, and the Collective for Living Cinema, and was a member of the Board for Kartemquin Films.
- `d7s4` Ira Deutchman [4]: In 2015, he donated his personal archives to the University of Michigan's Screen Arts Mavericks and Makers Collection.
- `d7s5` Ira Deutchman [5]: Deutchman continues to produce films while consulting on the marketing and distribution of independent films, and teaching producing students in the MFA Film Program at Columbia University's School of the Arts.
- `d7s6` Ira Deutchman [6]: Current projects include a film adaptation of Barbara Ehrenreich's best-selling book "Nickel and Dimed," a theatrical adaptation of Joan Micklin Silver's 1976 independent film "Hester Street" and a documentary about art film maverick Donald Rugoff, which is in production.
- `d7s7` Ira Deutchman [7]: He consults for Luce Cinecitta on the marketing of Italian cinema in the United States.
- `d7s8` Ira Deutchman [8]: Deutchman was awarded the first annual Spotlight Lifetime Achievement Award at the 2017 Sundance Art House Convergence.
- `d8s0` Jerome Karabel [0]: Jerome Bernard Karabel (born 1950) is an American sociologist, political and social commentator, and Professor of Sociology at the University of California at Berkeley.
- `d8s1` Jerome Karabel [1]: He has written extensively on American institutions of higher education and on various aspects of social policy and history in the United States, often from a comparative perspective.
- `d9s0` Chinese Coffee [0]: Chinese Coffee is a one-act play, written by Ira Lewis.
- `d10s0` Rosemary's Baby (miniseries) [0]: Rosemary's Baby is a 2014 two-part, four-hour television miniseries adaptation of Ira Levin's best-selling horror novel of the same name.
- `d10s1` Rosemary's Baby (miniseries) [1]: Zoe Saldana stars in the NBC production that is directed by Agnieszka Holland.
- `d10s2` Rosemary's Baby (miniseries) [2]: Unlike earlier versions, it is set in Paris rather than New York.
- `d10s3` Rosemary's Baby (miniseries) [3]: The work was not well received by critics, many of whom said that it was stretched to fill two two-hour timeslots.
- `d10s4` Rosemary's Baby (miniseries) [4]: Although there are several notable changes, this miniseries is considered to be a fairly true updating of the original film adaptation.

</details>

## Q274 — `hotpotqa_5adcfdc555429947343537f4` (revised draft)

> What federal agency was founded in 1935 and maintains a list of wanted persons?

Source answer: the Federal Bureau of Investigation (FBI)

Gold final answer: FBI

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: federal agency founded in 1935 | false | FBI (accepted alternatives: Federal Bureau of Investigation) | — | [d2s1] | — |
| u2: agency {u1} that maintains the wanted-person list | true | FBI (accepted alternatives: Federal Bureau of Investigation; the Federal Bureau of Investigation (FBI)) | u1 | [d1s0] OR [d4s0] | — |

Evidence:

- `d1s0` FBI Ten Most Wanted Fugitives by year, 1960 [0]: In 1960, the United States FBI, under Director J. Edgar Hoover, continued for an eleventh year to maintain a public list of the people it regarded as the Ten Most Wanted Fugitives.
- `d2s1` J. Edgar Hoover [1]: He was appointed as the fifth director of the Bureau of Investigation — the FBI's predecessor — in 1924 and was instrumental in founding the FBI in 1935, where he remained director until his death in 1972 at the age of 77.
- `d4s0` Myloh Jaqory Mason [0]: Myloh Jaqory Mason (born June 28, 1990) is an American man who was listed by the Federal Bureau of Investigation (FBI) of the United States within the FBI list of the ten most wanted persons for crimes alleged committed.

Notes:

- 删除全名转换用途；先核对1935年成立，再验证通缉名单，补d4s0。两项筛选都保留，不能因回答出FBI就忽略年份。

<details><summary>All source context</summary>

- `d1s0` FBI Ten Most Wanted Fugitives by year, 1960 [0]: In 1960, the United States FBI, under Director J. Edgar Hoover, continued for an eleventh year to maintain a public list of the people it regarded as the Ten Most Wanted Fugitives.
- `d2s0` J. Edgar Hoover [0]: John Edgar Hoover (January 1, 1895 – May 2, 1972), better known as J. Edgar Hoover, was the first Director of the Federal Bureau of Investigation (FBI) of the United States.
- `d2s1` J. Edgar Hoover [1]: He was appointed as the fifth director of the Bureau of Investigation — the FBI's predecessor — in 1924 and was instrumental in founding the FBI in 1935, where he remained director until his death in 1972 at the age of 77.
- `d2s2` J. Edgar Hoover [2]: Hoover has been credited with building the FBI into a larger crime-fighting agency than it was at its inception and with instituting a number of modernizations to police technology, such as a centralized fingerprint file and forensic laboratories.
- `d3s0` Civil forfeiture in the United States [0]: Civil forfeiture in the United States, also called civil asset forfeiture or civil judicial forfeiture or occasionally civil seizure, is a controversial legal process in which law enforcement officers take assets from persons suspected of involvement with crime or illegal activity without necessarily charging the owners with wrongdoing.
- `d3s1` Civil forfeiture in the United States [1]: While civil procedure, as opposed to criminal procedure, generally involves a dispute between two private citizens, civil forfeiture involves a dispute between law enforcement and "property" such as a pile of cash or a house or a boat, such that the thing is suspected of being involved in a crime.
- `d3s2` Civil forfeiture in the United States [2]: To get back the seized property, owners must prove it was not involved in criminal activity.
- `d3s3` Civil forfeiture in the United States [3]: Sometimes it can mean a threat to seize property as well as the act of seizure itself.
- `d3s4` Civil forfeiture in the United States [4]: In 2015, Eric Holder ended 'adoptive forfeiture' which occurred "when a state or local law enforcement agency seizes property pursuant to state law and requests that a federal agency take the seized asset and forfeit it under federal law" due to abuse.
- `d3s5` Civil forfeiture in the United States [5]: States proceeded to curtail the powers of police to seize assets, actions by the justice department in July 2017 have sought to reinstate police seizure powers to raise funding for federal agencies and local law enforcement.
- `d4s0` Myloh Jaqory Mason [0]: Myloh Jaqory Mason (born June 28, 1990) is an American man who was listed by the Federal Bureau of Investigation (FBI) of the United States within the FBI list of the ten most wanted persons for crimes alleged committed.
- `d4s1` Myloh Jaqory Mason [1]: Mason is described by the FBI as a violent felon.
- `d5s0` Turner Broadcasting System, Inc. v. FCC [0]: Turner Broadcasting v. Federal Communications Commission, 512 U.S. 622 (1994), is the first of two United States Supreme Court cases dealing with the must carry rules imposed on cable television companies.
- `d5s1` Turner Broadcasting System, Inc. v. FCC [1]: "Turner Broadcasting v. Federal Communications Commission (II)", 520 U.S. 180 (1997) was the second.
- `d5s2` Turner Broadcasting System, Inc. v. FCC [2]: "Turner I" established that cable television companies were indeed First Amendment speakers but didn't decide whether the federal regulation of their speech infringed upon their speech rights.
- `d5s3` Turner Broadcasting System, Inc. v. FCC [3]: In "Turner II" the court decided that the must carry provisions were constitutional.
- `d5s4` Turner Broadcasting System, Inc. v. FCC [4]: Under the "Miami Herald v. Tornillo" case, it was unconstitutional to force a newspaper to run a story the editors would not have included absent a government statute because it was compelled speech which could not pass the strict scrutiny of a compelling state interest being achieved with the least restrictive means necessary to achieve the state interest.
- `d5s5` Turner Broadcasting System, Inc. v. FCC [5]: However, under the rule of "Red Lion Broadcasting Co. v. FCC" the High Court held that a federal agency could regulate broadcast stations (TV and Radio) with far greater discretion.
- `d5s6` Turner Broadcasting System, Inc. v. FCC [6]: In order for federal agency regulation of broadcast media to pass constitutional muster, it need only serve an important state interest and need not narrowly tailor its regulation to the least restrictive means.
- `d6s0` Abdul Rauf Asghar [0]: Abdul Rauf is a commander of the militant Pakistani group Jaish-e-Mohammed, based mainly in the Pakistan-administered portion of the state of Kashmir and also in Afghanistan.
- `d6s1` Abdul Rauf Asghar [1]: The younger brother of Jaish-e-Mohammad chief Masood Azhar, he was involved in the hijacking of an Indian Airlines Flight 814 and is one of the most wanted persons in India due to his history of militant activities.
- `d7s0` Federal Agency on Atomic Energy (Russia) [0]: Ministry for Atomic Energy of the Russian Federation and Federal Agency on Atomic Energy (or Rosatom), were a Russian federal executive body in 1992-2008 (as Federal Ministry in 1992-2004 and as Federal Agency in 2004-2008).
- `d8s0` Office of Thrift Supervision [0]: The Office of Thrift Supervision (OTS) was a United States federal agency under the Department of the Treasury that chartered, supervised, and regulated all federally chartered and state-chartered savings banks and savings and loans associations.
- `d8s1` Office of Thrift Supervision [1]: It was created in 1989 as a renamed version of another federal agency (that was faulted for its role in the savings and loan crisis).
- `d8s2` Office of Thrift Supervision [2]: Like other U.S. federal bank regulators, it was paid by the banks it regulated.
- `d8s3` Office of Thrift Supervision [3]: The OTS was initially seen as an aggressive regulator, but was later lax.
- `d8s4` Office of Thrift Supervision [4]: Declining revenues and staff led the OTS to market itself to companies as a lax regulator in order to get revenue.
- `d9s0` Federal Housing Finance Agency [0]: The Federal Housing Finance Agency (FHFA) is an independent federal agency created as the successor regulatory agency of the Federal Housing Finance Board (FHFB), the Office of Federal Housing Enterprise Oversight (OFHEO), and the U.S. Department of Housing and Urban Development government-sponsored enterprise mission team, absorbing the powers and regulatory authority of both entities, with expanded legal and regulatory authority, including the ability to place government sponsored enterprises (GSEs) into receivership or conservatorship.
- `d10s0` Executive Order 12148 [0]: Executive Order 12148 was an executive order enacted by President Jimmy Carter on July 20, 1979 to transfer and reassign duties to the newly formed agency, known as the Federal Emergency Management Agency (FEMA), created by Executive Order 12127.
- `d10s1` Executive Order 12148 [1]: The order combined several federal agencies tasked with emergency preparedness and civil defense spread across the executive departments into a unified entity that was established as an independent agency, free of Cabinet interference, with authority as the lead federal agency in a presidentially-declared disaster.

</details>

## Q275 — `hotpotqa_5add1e565542990d50227dea` (revised draft)

> Who was the writer of the graphic novel upon which the 2003 American superhero film, directed by Bryan Singer, is based?

Source answer: Chris Claremont

Gold final answer: Chris Claremont

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: 2003 American superhero film directed by Bryan Singer | false | X2 | — | [d9s0, d9s2] | — |
| u2: graphic novel on which {u1} was based | false | X-Men: God Loves, Man Kills | u1 | [d4s0, d4s2] | — |
| u3: writer of {u2} | true | Chris Claremont | u2 | [d4s1] | — |

Evidence:

- `d4s0` X-Men: God Loves, Man Kills [0]: X-Men: God Loves, Man Kills ("Marvel Graphic Novel" #5) is an original graphic novel published in 1982 by Marvel Comics, starring their popular superhero team the X-Men.
- `d4s1` X-Men: God Loves, Man Kills [1]: It was written by Chris Claremont and illustrated by Brent Anderson.
- `d4s2` X-Men: God Loves, Man Kills [2]: The book was the basis for the film "X2".
- `d9s0` X2 (film) [0]: X2 (often promoted as X2: X-Men United and internationally as X-Men 2) is a 2003 American superhero film based on the X-Men superhero team appearing in Marvel Comics.
- `d9s2` X2 (film) [2]: The film was directed by Bryan Singer, written by Michael Dougherty, Dan Harris, and David Hayter, and features an ensemble cast including Hugh Jackman, Patrick Stewart, Ian McKellen, Halle Berry, Famke Janssen, James Marsden, Rebecca Romijn-Stamos, Brian Cox, Alan Cumming, Bruce Davison, Shawn Ashmore, Aaron Stanford, Kelly Hu, and Anna Paquin.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Hellboy (2004 film) [0]: Hellboy is a 2004 American supernatural superhero film directed by Guillermo del Toro and starring Ron Perlman, loosely based on the Dark Horse Comics graphic novel "" by Mike Mignola.
- `d1s1` Hellboy (2004 film) [1]: In the film, a demonic beast-turned superhero known as Hellboy, secretly works to keep the world safe from paranormal threats with his team, the Bureau of Paranormal Research and Defense.
- `d2s0` Justice League: War [0]: Justice League: War is a direct-to-video animated superhero film featuring the DC Comics superhero team the Justice League, and an adaptation of the story "Justice League: Origin" by Geoff Johns and Jim Lee, the first story in DC's 2011 DC Universe relaunch.
- `d2s1` Justice League: War [1]: It was directed by Jay Oliva, scripted by Heath Corson.
- `d2s2` Justice League: War [2]: It is the first movie from the DC Universe Animated Original Movies series that is part of a new shared continuity, the DC Animated Movie Universe.
- `d2s3` Justice League: War [3]: The film was released for downloading on January 21, 2014<ref name="http://www.com"> </ref> and was released on Blu-ray and DVD formats on February 4, 2014.
- `d2s4` Justice League: War [4]: It had its world premiere at the Paley Center for Media on the same day.
- `d2s5` Justice League: War [5]: <ref name="http://www.bleedingcool.com"> </ref> On August 11, 2015, Warner Home Video re-released the film on a combo pack, which includes a DVD and Blu-Ray copy, a digital copy, and the graphic novel it's based on.
- `d3s0` X-Men: Days of Future Past [0]: X-Men: Days of Future Past is a 2014 American superhero film based on the fictional X-Men characters that appear in Marvel Comics.
- `d3s1` X-Men: Days of Future Past [1]: Directed by Bryan Singer, it is the seventh installment of the "X-Men" film series and acts as a sequel to both 2006's "" and 2011's "".
- `d3s2` X-Men: Days of Future Past [2]: The story, inspired by the 1981 "Uncanny X-Men" storyline "Days of Future Past" by Chris Claremont and John Byrne, focuses on two time periods, with Wolverine traveling back in time to 1973 to change history and prevent an event that results in doom for both humans and mutants.
- `d3s3` X-Men: Days of Future Past [3]: The film features an ensemble cast, including Hugh Jackman, James McAvoy, Michael Fassbender, Jennifer Lawrence, Halle Berry, Anna Paquin, Ellen Page, Peter Dinklage, Ian McKellen and Patrick Stewart.
- `d3s4` X-Men: Days of Future Past [4]: Simon Kinberg wrote the screenplay from a story conceived by Jane Goldman, himself, and Matthew Vaughn.
- `d4s0` X-Men: God Loves, Man Kills [0]: X-Men: God Loves, Man Kills ("Marvel Graphic Novel" #5) is an original graphic novel published in 1982 by Marvel Comics, starring their popular superhero team the X-Men.
- `d4s1` X-Men: God Loves, Man Kills [1]: It was written by Chris Claremont and illustrated by Brent Anderson.
- `d4s2` X-Men: God Loves, Man Kills [2]: The book was the basis for the film "X2".
- `d5s0` X-Men (film) [0]: X-Men is a 2000 American superhero film based on the Marvel Comics superhero team of the same name, distributed by 20th Century Fox.
- `d5s1` X-Men (film) [1]: The film, directed by Bryan Singer and written by David Hayter, features an ensemble cast that includes Hugh Jackman, Patrick Stewart, Ian McKellen, Halle Berry, Famke Janssen, James Marsden, Bruce Davison, Rebecca Romijn-Stamos, Ray Park, Tyler Mane, and Anna Paquin.
- `d5s2` X-Men (film) [2]: It depicts a world in which a small proportion of people are mutants, whose possession of superhuman powers makes them distrusted by normal humans.
- `d5s3` X-Men (film) [3]: The film focuses on the mutants Wolverine and Rogue as they are brought into a conflict between two groups that have radically different approaches to bringing about the acceptance of mutant-kind: Professor Xavier's X-Men, and the Brotherhood of Mutants, led by Magneto.
- `d6s0` X-Men (film series) [0]: X-Men is an American superhero film series based on the fictional superhero team of the same name, who originally appeared in a series of comic books created by Stan Lee and Jack Kirby and published by Marvel Comics.
- `d6s1` X-Men (film series) [1]: 20th Century Fox obtained the film rights to the characters in 1994, and after numerous drafts, Bryan Singer was hired to direct "X-Men" (2000) and its sequel, "X2" (2003), while Brett Ratner directed "" (2006).
- `d7s0` Superman Returns [0]: Superman Returns is a 2006 American superhero film directed and produced by Bryan Singer.
- `d7s1` Superman Returns [1]: It is based on the DC Comics character Superman and serves as an homage sequel to the motion pictures "Superman" (1978) and "Superman II" (1980), while ignoring the events of "Superman III" (1983) and "" (1987).
- `d7s2` Superman Returns [2]: The film stars Brandon Routh as Clark Kent/Superman, Kate Bosworth as Lois Lane, Kevin Spacey as Lex Luthor, with James Marsden, Frank Langella, and Parker Posey.
- `d7s3` Superman Returns [3]: The film tells the story of the title character returning to Earth after a five-year absence.
- `d7s4` Superman Returns [4]: He finds that his love interest Lois Lane has moved on with her life, and that his archenemy Lex Luthor is plotting a scheme that will destroy Superman and the world.
- `d8s0` X-Men: Apocalypse [0]: X-Men: Apocalypse is a 2016 American superhero film based on the fictional X-Men characters that appear in Marvel Comics.
- `d8s1` X-Men: Apocalypse [1]: It is the ninth installment in the "X-Men" film series and a sequel to "".
- `d8s2` X-Men: Apocalypse [2]: Directed by Bryan Singer, with a screenplay by Simon Kinberg from a story conceived by Singer, Kinberg, Michael Dougherty and Dan Harris, the film stars James McAvoy, Michael Fassbender, Jennifer Lawrence, Oscar Isaac, Nicholas Hoult, Rose Byrne, Tye Sheridan, Sophie Turner, Olivia Munn and Lucas Till.
- `d8s3` X-Men: Apocalypse [3]: The ancient mutant En Sabah Nur awakens in 1983 and plans to wipe out modern civilization and take over the world, leading the X-Men to try to stop him and defeat his team of renegade mutants.
- `d9s0` X2 (film) [0]: X2 (often promoted as X2: X-Men United and internationally as X-Men 2) is a 2003 American superhero film based on the X-Men superhero team appearing in Marvel Comics.
- `d9s1` X2 (film) [1]: It is the sequel to 2000's "X-Men", and the second installment in the "X-Men" film series.
- `d9s2` X2 (film) [2]: The film was directed by Bryan Singer, written by Michael Dougherty, Dan Harris, and David Hayter, and features an ensemble cast including Hugh Jackman, Patrick Stewart, Ian McKellen, Halle Berry, Famke Janssen, James Marsden, Rebecca Romijn-Stamos, Brian Cox, Alan Cumming, Bruce Davison, Shawn Ashmore, Aaron Stanford, Kelly Hu, and Anna Paquin.
- `d9s3` X2 (film) [3]: The plot, inspired by the graphic novel "", pits the X-Men and their enemies, the Brotherhood, against the genocidal Colonel William Stryker (Brian Cox).
- `d9s4` X2 (film) [4]: He leads an assault on Professor Xavier's school to build his own version of Xavier's mutant-tracking computer Cerebro, in order to destroy every mutant on Earth and to save the human race from them.
- `d10s0` X-Men: First Class [0]: X-Men: First Class (stylized onscreen as X: First Class) is a 2011 American superhero film, based on the X-Men characters appearing in Marvel Comics.
- `d10s1` X-Men: First Class [1]: It is the fifth installment in the "X-Men" film series.
- `d10s2` X-Men: First Class [2]: It is both a prequel and a soft reboot of the franchise, the film was directed by Matthew Vaughn and produced by Bryan Singer.
- `d10s3` X-Men: First Class [3]: The story is set primarily in 1962 during the Cuban Missile Crisis, and focuses on the relationship between Professor Charles Xavier (James McAvoy) and Erik Lehnsherr / Magneto (Michael Fassbender), and the origin of their groups—the X-Men and the Brotherhood of Mutants, respectively, as they deal with the Hellfire Club led by Sebastian Shaw (Kevin Bacon), who is bent on world domination.
- `d10s4` X-Men: First Class [4]: The film co-stars Rose Byrne, January Jones and Oliver Platt.
- `d10s5` X-Men: First Class [5]: The film also introduces new actors to the series including Nicholas Hoult and Jennifer Lawrence who, like McAvoy and Fassbender, reimagine popular characters from the franchise (Beast and Mystique) that have already been established in previous films, namely the original trilogy.

</details>

## Q276 — `hotpotqa_5add5f395542990dbb2f7e50` (revised draft)

>  the movie "A Cure for Wellness" was a science fiction?

Source answer: is a 2016 science fiction psychological horror

Gold final answer: yes

Question type: `single` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: whether A Cure for Wellness is science fiction | true | yes | — | [d3s0] | — |

Evidence:

- `d3s0` A Cure for Wellness [0]: A Cure for Wellness is a 2016 science fiction psychological horror

Notes:

- 是非题答案改为yes，类型和年份片段保留在来源中。

<details><summary>All source context</summary>

- `d1s0` Dane DeHaan [0]: Dane William DeHaan ( ; born February 6, 1986) is an American actor.
- `d1s1` Dane DeHaan [1]: His roles include Jesse on the HBO series "In Treatment", Andrew Detmer in "Chronicle" (2012), Jason Kancam in Derek Cianfrance's "The Place Beyond the Pines" (2012), Lucien Carr in "Kill Your Darlings" (2013), Harry Osborn in "The Amazing Spider-Man 2" (2014), James Dean in Anton Corbijn's "Life" (2015), Lockhart in Gore Verbinski's "A Cure for Wellness" (2016) and the title character in Luc Besson's "Valerian and the City of a Thousand Planets" (2017).
- `d1s2` Dane DeHaan [2]: He has also appeared in several advertisements for Prada.
- `d2s0` Severna Park (writer) [0]: Severna Park (born 1958) is a science fiction author and winner of the Nebula Award for Best Short Story (The Cure For Everything, 2001).
- `d2s1` Severna Park (writer) [1]: Her first novel, "Speaking Dreams" from 1992, was a Lambda Literary Award nominee.
- `d2s2` Severna Park (writer) [2]: She now writes mainstream fiction.
- `d2s3` Severna Park (writer) [3]: Employed as a teacher, she lives with her partner of twenty-five years in Maryland.
- `d3s0` A Cure for Wellness [0]: A Cure for Wellness is a 2016 science fiction psychological horror
- `d4s0` Starship Highlander [0]: Raumschiff Highlander (translated: Starship Highlander) is a fan-created science fiction film and novel series.
- `d4s1` Starship Highlander [1]: The series was initiated in 1993 by Robert Amper.
- `d4s2` Starship Highlander [2]: Originally, a fan club of science fiction, especially for "" (aka "ST:TOS" or just "TOS"), and the Star Wars movies, whose members met regularly.
- `d4s3` Starship Highlander [3]: Some members having experience in filmmaking, the idea spawned of creating material for a movie.
- `d4s4` Starship Highlander [4]: First episode of the series aired in 1995 on German TV Channel SAT.1.
- `d4s5` Starship Highlander [5]: Inspired by the success of their movie came four additional sequels at the rate of one per year.
- `d4s6` Starship Highlander [6]: The movies are a parody of Star Trek and other classics of the genre.
- `d5s0` The Philip K. Dick Reader [0]: The Philip K. Dick Reader is a collection of science fiction stories by American writer Philip K. Dick.
- `d5s1` The Philip K. Dick Reader [1]: It was first published by Citadel Twilight in 1997.
- `d5s2` The Philip K. Dick Reader [2]: Many of the stories had originally appeared in the magazines "If", "Science Fiction Adventures", "Science Fiction Stories", "Orbit", "Fantasy and Science Fiction", "Imagination", "Future", "Galaxy Science Fiction", "Beyond Fantasy Fiction", "Satellite", "Imaginative Tales", "Fantastic Universe" and "Space Science Fiction".
- `d5s3` The Philip K. Dick Reader [3]: It is identical in content and order to the edition of volume 3 of the Collected Stories of Philip K. Dick produced by the same publisher apart from the substitution of three stories in positions 21-23 of 24 and the omission of the end notes in the Collected Stories edition.
- `d5s4` The Philip K. Dick Reader [4]: At press time, stories 21 and 24 had already been made into successful movie adaptations and stories 22 and 23 had been optioned.
- `d6s0` I-CON [0]: I-CON (short for "Island CONvention") is a [roughly] annual fan convention, held on various college campuses in Suffolk County, Long Island, New York.
- `d6s1` I-CON [1]: First held in 1982 on the campus of Stony Brook University (then State University of New York at Stony Brook), I-CON became a very eclectic convention.
- `d6s2` I-CON [2]: The programming included things normally found at different types of convention, like speeches by and talks with science fiction authors, extensive gaming, anime fandom, comics fandom, furry fandom, multiple movie showings, and medieval programming, as well as live performances.
- `d6s3` I-CON [3]: There was also a science track discussing recent developments in various branches of science and exploring the real science behind science fiction technologies.
- `d6s4` I-CON [4]: I-CON was jointly held by ICON Science Fiction, Inc., a tax-exempt educational foundation, and the I-CON Campus Chapter of Stony Brook.
- `d7s0` The Death Cure [0]: The Death Cure is a 2011 young adult dystopian science fiction novel written by American writer James Dashner and the third book, fifth chronologically, in the "Maze Runner" series.
- `d7s1` The Death Cure [1]: It was published on October 11, 2011 by Delacorte Press and was preceded by "The Maze Runner" and "The Scorch Trials" and followed by the series prequels, "The Kill Order and The Fever Code."
- `d8s0` Science fiction films in India [0]: The genre of science fiction has been prevalent in the Indian film industry since the second half of the 20th century.
- `d8s1` Science fiction films in India [1]: Beginning in 1952, the film "Kaadu" was made, which was a Tamil-American co-production. "
- `d8s2` Science fiction films in India [2]: The Alien" was a science fiction film under production in the late 1960s which was eventually cancelled.
- `d8s3` Science fiction films in India [3]: The film was being directed by Bengali Indian director Satyajit Ray and produced by Hollywood studio Columbia Pictures.
- `d8s4` Science fiction films in India [4]: The script was written by Ray in 1967, based on "Bankubabur Bandhu", a Bengali story he had written in 1962 for "Sandesh", the Ray family magazine.
- `d8s5` Science fiction films in India [5]: In 1987, the superhero film "Mr. India" was a huge success which strengthened the hold of sci-fi films in India, especially Bollywood.
- `d8s6` Science fiction films in India [6]: "Indiatimes Movies" ranks the movie amongst the "Top 25 Must See Bollywood Films".
- `d8s7` Science fiction films in India [7]: "Mr. India" brought the idea of science fiction to the general people in India.
- `d8s8` Science fiction films in India [8]: In 2003, the blockbuster film "Koi... Mil Gaya" marked the beginning of the successful Krrish film series, which is the first sci-fi/superhero film series in Indian cinema.
- `d8s9` Science fiction films in India [9]: The 2010 Tamil film "Enthiran" starring Rajinikanth and Aishwarya Rai is the most expensive and most successful sci/fi film ever produced in India.
- `d9s0` Final Blackout [0]: Final Blackout is a dystopic science fiction novel by author L. Ron Hubbard.
- `d9s1` Final Blackout [1]: The novel is set in the future and follows a man known as "the Lieutenant" as he restores order to England after a world war.
- `d9s2` Final Blackout [2]: First published in serialized format in 1940 in the science fiction magazine "Astounding Science Fiction", "Final Blackout" was published in book form in 1948 by The Hadley Publishing Co..
- `d9s3` Final Blackout [3]: Author Services Inc. published a hardcover edition of the book in 1988, and in 1989 the Church of Scientology-affiliated organization Bridge Publications said that a film director named Christopher Cain had signed a contract to write and direct a movie version based on the book.
- `d10s0` Forrest J Ackerman [0]: Forrest J Ackerman (born Forrest James Ackerman; November 24, 1916 – December 4, 2008) was an American magazine editor, science fiction writer and literary agent, a founder of science fiction fandom, a leading expert on science fiction, horror, and fantasy films, and acknowledged as the world's most avid collector of genre books and movie memorabilia.
- `d10s1` Forrest J Ackerman [1]: He was based in Los Angeles, California.

</details>

## Q277 — `hotpotqa_5ade18df5542990dbb2f7f53` (revised draft)

> Which television network that aired Gameshow Marathon has been owned by the Bell Media division of BCE, Inc since 2000?

Source answer: CTV

Gold final answer: CTV

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: network owned by the Bell Media division of BCE since 2000 in the source | false | CTV | — | [d8s1] | — |
| u2: network {u1} that aired Gameshow Marathon | true | CTV | u1 | [d3s2] | — |

Evidence:

- `d3s2` Gameshow Marathon (U.S. TV series) [2]: It also aired in Canada on CTV.
- `d8s1` CTV Television Network [1]: Since 2000 it is owned by the Bell Media division of BCE, Inc. It is Canada's largest privately or commercially owned network, and has consistently been placed as Canada's top-rated network in total viewers and in key demographics since 2002, after several years trailing the rival Global Television Network in key markets.

Notes:

- 反转筛选顺序，先所有权条件再播出关系；去掉Canadian额外限定，不从CBS/CTV中事后选答案。

<details><summary>All source context</summary>

- `d1s0` 299 Queen Street West [0]: 299 Queen Street West, also known as Bell Media Queen Street, is the headquarters of the television/radio broadcast hub of Bell Canada's media unit, Bell Media located at the intersection of Queen Street West and John Street in Downtown Toronto, Ontario, Canada.
- `d1s1` 299 Queen Street West [1]: The building previously served as the headquarters of CTVglobemedia until Bell Canada acquired CTV again in 2011 as well as CHUM Television, a division of CHUM Limited, until CTV acquired CHUM in 2007, and was once known as the CHUM-City Building.
- `d1s2` 299 Queen Street West [2]: It is now head offices and downtown Toronto studios for Bell Media.
- `d2s0` Bell Media Radio [0]: Bell Media Radio is the Canadian radio broadcasting division of Bell Media which is owned by BCE Inc. The division owns the bulk of the radio properties owned by CHUM Limited in 2007 when it was purchased by CTVglobemedia (now Bell Media), and Astral Media when it was purchased by Bell in 2013.
- `d3s0` Gameshow Marathon (U.S. TV series) [0]: Game$how Marathon is an American television program which aired on CBS from May 31, 2006 to June 29, 2006.
- `d3s1` Gameshow Marathon (U.S. TV series) [1]: It is based on the United Kingdom series "Ant & Dec's Gameshow Marathon" which aired on ITV in 2005.
- `d3s2` Gameshow Marathon (U.S. TV series) [2]: It also aired in Canada on CTV.
- `d4s0` Card Sharks [0]: Card Sharks is an American television game show created by Chester Feldman for Mark Goodson-Bill Todman Productions.
- `d4s1` Card Sharks [1]: Based on the card game Acey Deucey, the game has two contestants compete for control of a row of oversized playing cards by answering questions posed by the host and then guessing if the next card is higher or lower in value than the previous one.
- `d4s2` Card Sharks [2]: The concept has been made into a series four separate times since its debut in 1978, and also appeared as part of CBS's "Gameshow Marathon".
- `d4s3` Card Sharks [3]: The show originally ran on NBC from 1978 to 1981 with Jim Perry hosting; a revival ran from 1986 to 1989 on CBS with Bob Eubanks as host, accompanied by another version in syndication with Bill Rafferty.
- `d4s4` Card Sharks [4]: Gene Wood was the announcer on these three versions.
- `d4s5` Card Sharks [5]: Another syndicated revival aired from 2001 to 2002 with Pat Bullard as host and Gary Kroeger as announcer.
- `d4s6` Card Sharks [6]: All versions of the show had various female assistants to handle the playing cards.
- `d5s0` List of assets owned by CTVglobemedia [0]: CTV Specialty Television Inc. is jointly owned by Bell Media and ESPN, with 80% owned by Bell Media and 20% owned by ESPN (itself 80% owned by The Walt Disney Company and 20% owned by Hearst Corporation).
- `d6s0` TSN Radio [0]: TSN Radio is a semi-national sports radio brand and part-time network in Canada carried on AM radio stations owned by Bell Media Radio.
- `d6s1` TSN Radio [1]: The TSN Radio brand, and some of the stations' content, is shared with Bell Media's television sports channel, The Sports Network.
- `d6s2` TSN Radio [2]: With the American sports media company ESPN being a minority shareholder in TSN, most of the stations also air some ESPN Radio programming, usually on weekends and/or overnight.
- `d7s0` The Sports Network [0]: The Sports Network (TSN) is a Canadian English language sports specialty service.
- `d7s1` The Sports Network [1]: Established by the Labatt Brewing Company in 1984 as part of the first group of Canadian specialty cable channels, since 2001, TSN has been majority-owned by communications conglomerate Bell Canada (presently through its broadcasting subsidiary Bell Media) with a minority stake held by ESPN Inc. via a 20% share in the Bell Media subsidiary CTV Specialty Television.
- `d7s2` The Sports Network [2]: TSN is the largest specialty channel in Canada in terms of gross revenue, with a total of $400.4 million in revenue in 2013.
- `d8s0` CTV Television Network [0]: CTV is an English-language broadcast television network in Canada launched in 1961.
- `d8s1` CTV Television Network [1]: Since 2000 it is owned by the Bell Media division of BCE, Inc. It is Canada's largest privately or commercially owned network, and has consistently been placed as Canada's top-rated network in total viewers and in key demographics since 2002, after several years trailing the rival Global Television Network in key markets.
- `d9s0` Bell Media [0]: Bell Media Inc. ("French": Bell Média) is the mass media subsidiary of BCE Inc. (also known as Bell Canada Enterprises, the parent company of the former telephone monopoly Bell Canada).
- `d9s1` Bell Media [1]: Its operations include television broadcasting and production (including the CTV and CTV Two television networks), radio broadcasting (through Bell Media Radio), digital media (including CraveTV) and Internet properties including Sympatico.
- `d9s2` Bell Media [2]: ca.
- `d10s0` Bell Media Tower [0]: The Bell Media Tower (Tour Bell Média) is a skyscraper in Montreal, Quebec, Canada.
- `d10s1` Bell Media Tower [1]: Located at 1800 McGill College Avenue, it was built for the Montreal Trust Company, and shared the name Place Montreal Trust with the adjoining mall.
- `d10s2` Bell Media Tower [2]: It stands 125 m (410 ft) and 30 storeys tall.
- `d10s3` Bell Media Tower [3]: It was originally owned by Cadillac Fairview but is now owned by Ivanhoe Cambridge.
- `d10s4` Bell Media Tower [4]: The main tenant was Astral Media, which had its corporate headquarters in the building along with several of its French-speaking television stations.
- `d10s5` Bell Media Tower [5]: In 2013, Bell acquired Astral Media, changing the tower's name to Bell Media Tower when it became regional offices for Bell Media.

</details>

## Q278 — `hotpotqa_5ade279e5542992fa25da6fa` (revised draft)

> Kent Dairy Round Barn is near the city in what Montana county?

Source answer: Carbon

Gold final answer: Carbon

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: Montana city near the Kent Dairy Round Barn | false | Red Lodge | — | [d3s0] | — |
| u2: county containing {u1} | true | Carbon (accepted alternatives: Carbon County) | u1 | [d7s0] | — |

Evidence:

- `d3s0` Kent Dairy Round Barn [0]: The Kent Dairy Round Barn near Red Lodge, Montana is a round barn that was built during 1939-1941 and is believed to be one of the last round dairy barns built in the United States.
- `d7s0` Red Lodge, Montana [0]: Red Lodge is a city in and the county seat of Carbon County, Montana, United States.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Robert Weber Round Barn [0]: The Robert Weber Round Barn is a round barn located east of Durand, Illinois, United States along Illinois Route 75 in Harrison Township.
- `d1s1` Robert Weber Round Barn [1]: The Weber barn was constructed in 1917 and features a roof designed and built by the Haas Brothers, who worked on other area round barns.
- `d1s2` Robert Weber Round Barn [2]: The barn is 55 ft in diameter and features a 24 ft diameter central silo.
- `d1s3` Robert Weber Round Barn [3]: The design of the Weber Round Barn stands out from other area round barns in its vitrified tile walls, a development used in later period American round barns.
- `d1s4` Robert Weber Round Barn [4]: The Robert Weber Round Barn was added to the U.S. National Register of Historic Places in 1984.
- `d2s0` Bert Leedy Round Barn [0]: The Bert Leedy Round Barn, also known as Paxton Round Barn and as Fulton County Historical Society Round Barn, is a round barn located in Richland Township near Rochester, Indiana, United States.
- `d2s1` Bert Leedy Round Barn [1]: Built in 1924, it was listed on the National Register of Historic Places in 1993.
- `d2s2` Bert Leedy Round Barn [2]: The listing was consistent with terms of a National Park Service "Multiple Property Documentation" study on "Round and Polygonal Barns of Indiana" that was prepared in 1991.
- `d2s3` Bert Leedy Round Barn [3]: The Round Barn was moved to its current site, an open-air museum, in 1989 after it was struck by a tornado.
- `d3s0` Kent Dairy Round Barn [0]: The Kent Dairy Round Barn near Red Lodge, Montana is a round barn that was built during 1939-1941 and is believed to be one of the last round dairy barns built in the United States.
- `d3s1` Kent Dairy Round Barn [1]: It has an adjoining rectangular milkhouse.
- `d3s2` Kent Dairy Round Barn [2]: The barn was built under supervision of master barn builder, Emery McNamee, by Ephraim Kent and sons Armas, Harry, James, Leo, and Waino.
- `d4s0` James Bruce Round Barn [0]: The James Bruce Round Barn is a round barn located near the Stephenson County, Illinois city of Freeport, United States.
- `d4s1` James Bruce Round Barn [1]: The barn was constructed in 1914 by the team of Jeremiah Shaffer and the Haas Brothers, who were responsible for at least a dozen round barns in the area.
- `d4s2` James Bruce Round Barn [2]: The barn features a single hip roof design which was probably influenced by the Agricultural Experiment Stations at the University of Illinois and the University of Wisconsin–Madison.
- `d4s3` James Bruce Round Barn [3]: The Bruce Round Barn was the last known round barn designed by the Shaffer–Haas team.
- `d4s4` James Bruce Round Barn [4]: The building was listed on the U.S. National Register of Historic Places as part of a multiple property submission in 1984.
- `d5s0` Thomas Ranck Round Barn [0]: The Thomas Ranck Round Barn is a round barn in Waterloo Township near the Fayette-Wayne County, Indiana county line.
- `d5s1` Thomas Ranck Round Barn [1]: It is one of many round barns built in Indiana during the late 19th and early 20th centuries.
- `d5s2` Thomas Ranck Round Barn [2]: Of the round barns built in eastern Indiana during this period the Ranck Round Barn stands out as one of the most elaborately designed structures.
- `d5s3` Thomas Ranck Round Barn [3]: The Thomas Ranck Round Barn was listed on the U.S. National Register of Historic Places in January 1983.
- `d6s0` Virginia Tillery Round Barn [0]: The Virginia Tillery Round Barn is a round barn located on County Route 738 west of White Hall in Greene County, Illinois.
- `d6s1` Virginia Tillery Round Barn [1]: The barn was built in the fall of 1912 for farmer Harry C. Price.
- `d6s2` Virginia Tillery Round Barn [2]: With a 36 ft diameter, the barn is relatively small for an Illinois round barn; the median diameter of Illinois round barns was 60 ft .
- `d6s3` Virginia Tillery Round Barn [3]: Its size suggests that it served as a general-purpose barn, not a dairy barn like the state's larger round barns.
- `d6s4` Virginia Tillery Round Barn [4]: Brown tile blocks were used to build the barn, which is topped by a wood shingle roof with a cupola.
- `d7s0` Red Lodge, Montana [0]: Red Lodge is a city in and the county seat of Carbon County, Montana, United States.
- `d7s1` Red Lodge, Montana [1]: It is part of the Billings Metropolitan Statistical Area.
- `d7s2` Red Lodge, Montana [2]: The population was 2,125 at the United States Census, 2010.
- `d8s0` University of Illinois round barns [0]: The three University of Illinois round barns played a special role in the promotion and popularity of the American round barn.
- `d8s1` University of Illinois round barns [1]: They are located in the U.S. city of Urbana, Illinois on the campus of the University of Illinois (U of I).
- `d8s2` University of Illinois round barns [2]: The University of Illinois was home to one of the Agricultural Experiment Stations, located at U.S. universities, which were at the heart of the promotion of the round barn.
- `d8s3` University of Illinois round barns [3]: At least one round barn in Illinois was built specifically after its owner viewed the barns at the university.
- `d8s4` University of Illinois round barns [4]: Though originally an experiment the three barns helped to lead the way for round barn construction throughout the Midwest, particularly in Illinois.
- `d8s5` University of Illinois round barns [5]: The barns were listed as contributing properties to the U of I Experimental Dairy Farm Historic District, which was listed on the U.S. National Register of Historic Places in 1994.
- `d9s0` Dennis Otte Round Barn [0]: The Dennis Otte Round Barn is a round barn in the U.S. state of Illinois near the unincorporated Stephenson County community of Eleroy.
- `d9s1` Dennis Otte Round Barn [1]: The barn was built in 1930 by Herman Altenbern and has a diameter of 54 feet (16.5 m).
- `d9s2` Dennis Otte Round Barn [2]: The barn is representative of the last round barn design variations that evolved.
- `d9s3` Dennis Otte Round Barn [3]: The Otte Round Barn was added to the U.S. National Register of Historic Places in 1984.
- `d10s0` Dammon Round Barn [0]: Dammon Round Barn is a round barn just southeast of Red Wing, Minnesota, United States, adjacent to U.S. Route 61.
- `d10s1` Dammon Round Barn [1]: The barn is listed on the National Register of Historic Places.
- `d10s2` Dammon Round Barn [2]: It was built in 1914, with a foundation of Mississippi River limestone, and is 60 ft in diameter and 60 ft high.
- `d10s3` Dammon Round Barn [3]: It was built during a time of agricultural growth in Goodhue County, when dairy cow herds were averaging 25 cows per farm and farmers were starting to build specialized barns.
- `d10s4` Dammon Round Barn [4]: The round barn design was built around a silo and provided insulation for the silage, as well as making feeding and cleaning easier.
- `d10s5` Dammon Round Barn [5]: Despite the efficiency, however, round barns were difficult to construct, and they were not widely adopted.
- `d10s6` Dammon Round Barn [6]: Later in its history the barn was used for honey production of the bee keeping owners of the farm.
- `d10s7` Dammon Round Barn [7]: In 2000 the Farm was purchased by Robin and Elaine Kleffman and the Dammon Barn underwent some significant restoration.
- `d10s8` Dammon Round Barn [8]: A straightening of the walls and replacement of the original pillars for the upper floor support and a leveling and new installation of a floor in the top level of the barn makes this one of the most premiere remaining round barns in Minnesota.

</details>

## Q279 — `hotpotqa_5a79e5a85542996c55b2dc94` (revised draft)

> Who was born first, Tanya Donelly or Trace Cyrus?

Source answer: Tanya Donelly

Gold final answer: Tanya Donelly

Question type: `comparison` (source type `comparison`)

Replaces: `hotpotqa_5ade45c75542992fa25da720`

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: birth year of Tanya Donelly | false | 1966 | — | [d6s0] | — |
| u2: birth year of Trace Cyrus | false | 1989 | — | [d2s0] | — |
| u3: Who was born first, Tanya Donelly or Trace Cyrus? | true | Tanya Donelly | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d2s0` Trace Cyrus [0]: Trace Dempsey Cyrus (born Neil Timothy Helson; February 24, 1989) is an American musician.
- `d6s0` Tanya Donelly [0]: Tanya Donelly (born July 14, 1966, in Newport, Rhode Island) is an American Grammy Award-nominated singer-songwriter and guitarist based in New England who co-founded Throwing Muses with her stepsister Kristin Hersh.

Notes:

- 替换：缺少东西相对方位或经度。 新题保留原source type，人工核对两条显式事实及答案。

<details><summary>All source context</summary>

- `d1s0` Ron Cyrus [0]: Ronald Ray "Ron" Cyrus (July 10, 1935 – February 28, 2006) was an American Democratic politician and public servant in Greenup County, Kentucky.
- `d1s1` Ron Cyrus [1]: He was the father of American country music singer/actor Billy Ray Cyrus and the paternal grandfather of Trace Cyrus, Miley Cyrus and Noah Cyrus.
- `d2s0` Trace Cyrus [0]: Trace Dempsey Cyrus (born Neil Timothy Helson; February 24, 1989) is an American musician.
- `d2s1` Trace Cyrus [1]: The son of country singer Billy Ray Cyrus and brother of recording artist Miley Cyrus, he is the backing vocalist and bassist of the band Metro Station.
- `d2s2` Trace Cyrus [2]: He left the band in 2010 but returned in 2014.
- `d2s3` Trace Cyrus [3]: In 2010, he began providing vocals and guitar in the pop rock band Ashland HIGH.
- `d2s4` Trace Cyrus [4]: He also owns the clothing company From Backseats to Bedrooms.
- `d3s0` The Blizzard of 78 [0]: The Blizzard of 78 is an American rock band from Boston and Providence.
- `d3s1` The Blizzard of 78 [1]: Consisting of ex-Delta Clutch members, they currently have two albums released; the first being the critically acclaimed "Where All Life Hangs".
- `d3s2` The Blizzard of 78 [2]: Tanya Donelly contributed a guest vocal to the album, and it won several Motif Magazine awards in 2007.
- `d3s3` The Blizzard of 78 [3]: The Blizzard of 78 have played with, or opened for, Coldplay, Alex Chilton, Ronnie Spector, Snow Patrol, Jim Carroll, Tanya Donelly, Guster, Remy Zero and Throwing Muses.
- `d3s4` The Blizzard of 78 [4]: The group once performed The Replacements' album "Tim" in its entirety.
- `d4s0` Brother Clyde (album) [0]: Brother Clyde is the debut studio album from alternative rock group Brother Clyde.
- `d4s1` Brother Clyde (album) [1]: It is the first side-project from country music singer Billy Ray Cyrus.
- `d4s2` Brother Clyde (album) [2]: The album features duets with Cyrus' son Trace Cyrus as well as Dolly Parton, who Cyrus said "wanted to rock."
- `d4s3` Brother Clyde (album) [3]: It was released on August 10, 2010.
- `d4s4` Brother Clyde (album) [4]: Its first single, "Lately", which features rapper King Phaze, was issued to digital retailers on June 29, 2010, and a music video, which was directed by Cyrus, was released for the song in July 2010.
- `d5s0` Whiskey Tango Ghosts [0]: Whiskey Tango Ghosts is the third solo album by Tanya Donelly, released in 2004.
- `d5s1` Whiskey Tango Ghosts [1]: The album marks a departure from Donelly's previous pop work in favor of a country and folk-influenced sound.
- `d5s2` Whiskey Tango Ghosts [2]: Donelly has described the album as influenced by "a horrible war, a horrible administration, (and) a bleak, mean winter."
- `d6s0` Tanya Donelly [0]: Tanya Donelly (born July 14, 1966, in Newport, Rhode Island) is an American Grammy Award-nominated singer-songwriter and guitarist based in New England who co-founded Throwing Muses with her stepsister Kristin Hersh.
- `d6s1` Tanya Donelly [1]: She then went on to work in The Breeders and Belly in the 1990s.
- `d6s2` Tanya Donelly [2]: In the late 1990s, she settled into a solo recording career, working largely with musicians connected to the Boston music scene.
- `d7s0` Throwing Muses [0]: Throwing Muses is an alternative rock band formed in 1981 in Newport, Rhode Island, that toured and recorded extensively until 1997, when its members began concentrating more on other projects.
- `d7s1` Throwing Muses [1]: The group was originally fronted by two lead singers, Kristin Hersh, and Tanya Donelly, who both wrote the group's songs.
- `d7s2` Throwing Muses [2]: Throwing Muses are known for performing music with shifting tempos, creative chord progressions, unorthodox song structures, and surreal lyrics.
- `d7s3` Throwing Muses [3]: The group was set apart from other contemporary acts by Hersh's stark, candid writing style; Donelly's pop stylings and vocal harmonies; and David Narcizo's unusual drumming techniques eschewing use of cymbals.
- `d7s4` Throwing Muses [4]: Hersh's hallucinatory, febrile songs occasionally touched on the subject of mental illness, more often drawing portraits of characters from daily life or addressing relationships.
- `d8s0` Belly (band) [0]: Belly is an alternative rock band formed in Boston, Massachusetts in 1991 by former Throwing Muses member Tanya Donelly (who was also in The Breeders).
- `d8s1` Belly (band) [1]: The original lineup consisted of Donelly on lead vocals and guitar, Fred Abong on bass, and brothers Tom and Chris Gorman on guitar and drums respectively.
- `d8s2` Belly (band) [2]: Although formed in Boston, the group's members are all from the Newport, Rhode Island area, and identify themselves as a Rhode Island band as opposed to a Boston one.
- `d9s0` Noah Cyrus [0]: Noah Lindsey Cyrus (born January 8, 2000) is an American actress and singer.
- `d9s1` Noah Cyrus [1]: She voiced the title role in the English version of the 2009 animated feature film "Ponyo".
- `d9s2` Noah Cyrus [2]: In 2016, she released her debut single "Make Me (Cry)", featuring vocals from Labrinth.
- `d9s3` Noah Cyrus [3]: Her debut album is set to be released in late 2017.
- `d9s4` Noah Cyrus [4]: She is the youngest daughter of Tish Cyrus and Billy Ray Cyrus and the younger sister of Miley Cyrus and Trace Cyrus.
- `d10s0` Lovesongs for Underdogs [0]: Lovesongs for Underdogs is the solo debut album by American singer Tanya Donelly, who had formerly recorded with Throwing Muses, The Breeders, and Belly.
- `d10s1` Lovesongs for Underdogs [1]: It was released on August 9, 1997.
- `d10s2` Lovesongs for Underdogs [2]: Two singles were released for promotion of the album.
- `d10s3` Lovesongs for Underdogs [3]: "Pretty Deep" was released in July 1997, while "The Bright Light" was released in October 1997.
- `d10s4` Lovesongs for Underdogs [4]: In the U.S both 4AD released singles were released in two parts, each including 2 newly released B-Sides.
- `d10s5` Lovesongs for Underdogs [5]: "Pretty Deep" featured "Spaghetti", "Morna", "These Days" and "Influenza".
- `d10s6` Lovesongs for Underdogs [6]: "The Bright Light" featured "Bury Me", "How Can You Sleep?"
- `d10s7` Lovesongs for Underdogs [7]: , "Life On Sirius" and "Moon Over Boston".
- `d10s8` Lovesongs for Underdogs [8]: A music video for each single was produced and aired on Vh1 and MTV2.
- `d10s9` Lovesongs for Underdogs [9]: Both videos differed highly in creative and artistic direction from previous Belly videos and exclusively featured Tanya solo, in movie like settings.
- `d10s10` Lovesongs for Underdogs [10]: "Pretty Deep" and "The Bright Light" enjoyed heavy airplay on Triple A radio stations in the U.S Northeast.
- `d10s11` Lovesongs for Underdogs [11]: "Lovesongs For Underdogs" peaked at #36 on the Official UK Albums Chart for 2 weeks upon its release.
- `d10s12` Lovesongs for Underdogs [12]: The singles, "Pretty Deep" and "The Bright Light" peaked at #55 and #65 (the latter) for 2 weeks each upon their 2 CD Single releases.

</details>

## Q280 — `hotpotqa_5adfa22655429942ec259ac4` (revised draft)

> How many total staff (including part-time, flexible, and fixed contract staff) does the broadcaster, who released HyperNormalisation, employ?

Source answer: 35,402

Gold final answer: 35,402

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: broadcaster of HyperNormalisation | false | BBC | — | [d2s0] OR [d2s2] | — |
| u2: total staff of {u1}, including part-time, flexible and fixed-contract staff | true | 35,402 | u1 | [d1s3] | — |

Evidence:

- `d1s3` BBC [3]: The total number of staff is 35,402 when part-time, flexible, and fixed contract staff are included.
- `d2s0` HyperNormalisation [0]: HyperNormalisation is a 2016 BBC documentary by British filmmaker Adam Curtis.
- `d2s2` HyperNormalisation [2]: The film was released on 16 October 2016 on the BBC iPlayer.

Notes:

- d2s2明确说明影片发布于BBC iPlayer，可支持题干所指BBC发布机构，补作u1备选。

<details><summary>All source context</summary>

- `d1s0` BBC [0]: The British Broadcasting Corporation (BBC) is a British public service broadcaster with its headquarters at Broadcasting House in London.
- `d1s1` BBC [1]: The BBC is the world's oldest national broadcasting organisation and the largest broadcaster in the world by number of employees.
- `d1s2` BBC [2]: It employs over 20,950 staff in total, 16,672 of whom are in public sector broadcasting.
- `d1s3` BBC [3]: The total number of staff is 35,402 when part-time, flexible, and fixed contract staff are included.
- `d2s0` HyperNormalisation [0]: HyperNormalisation is a 2016 BBC documentary by British filmmaker Adam Curtis.
- `d2s1` HyperNormalisation [1]: In the film, Curtis argues that since the 1970s, governments, financiers, and technological utopians have given up on the complex "real world" and built a simple "fake world" that is run by corporations and kept stable by politicians.
- `d2s2` HyperNormalisation [2]: The film was released on 16 October 2016 on the BBC iPlayer.
- `d3s0` The One (company) [0]: The One Total Home Experience, stylized THE One, is a furniture retail company founded by Swedish entrepreneur and philanthropist Thomas Lundgren.
- `d3s1` The One (company) [1]: As of December 2014, the home fashion brand has a total of 18 stores across the Middle East and North Africa in Bahrain, Iraq, Jordan, Kuwait, Lebanon, Qatar, Tunisia and the United Arab Emirates, with a total staff complement of over 700.
- `d4s0` Strafing [0]: Strafing is the military practice of attacking ground targets from low-flying aircraft using aircraft-mounted automatic weapons ranging from machine guns (5mm to 20mm) to autocannons or rotary cannons (typically 20mm to 37mm).
- `d4s1` Strafing [1]: This means that, although ground attack using automatic weapons fire is very often accompanied with bombing or rocket fire, the term "strafing" does not specifically include the last two.
- `d4s2` Strafing [2]: The term "strafing" can cover either fixed guns, or aimable (flexible) guns.
- `d4s3` Strafing [3]: Fixed guns firing directly ahead tend to be more predominant on fixed wing aircraft, while helicopters tend to use aimable weapons which can be fired in many different directions independent of the direction the aircraft is pointing in (in most cases, flexible guns on a fixed wing aircraft are for defense purposes only, although they can sometimes be used to fire on ground targets to limited effect).
- `d4s4` Strafing [4]: Some fixed wing aircraft, like fighter-bombers, are capable of flying either air-combat missions or ground attack missions (P-47 Thunderbolt), while others are dedicated ground-attack types (Il-2 Shturmovik).
- `d4s5` Strafing [5]: In cases where an aircraft is capable of both types of combat, when it is assigned to a ground attack role, and thus expected to be using the guns mostly for strafing, the fixed weapons are often mounted so that the convergence point is lower and at a greater range than would be used for air combat.
- `d4s6` Strafing [6]: This is helpful because it allows the pilot to aim at a target without having to dive towards the ground as steeply, decreasing the risk of collision with the ground and increasing the amount of firing time available before having to pull up, and it also increases the range from the target, helping avoid anti-aircraft fire and potential damage from exploding targets.
- `d4s7` Strafing [7]: Because of the low altitude and relatively low airspeed required for accurate strafing, it is very risky for the pilot, who is exposed not only to the risk of flight-into-terrain and obstacles such as power lines, but also to anti-aircraft weapons, including surface-to-air missiles (both vehicle mounted and hand-held), anti-aircraft artillery and small caliber weapons fire (such as machine guns and small arms).
- `d4s8` Strafing [8]: Planes purposely designed for ground attack may include additional armour around and underneath the cockpit and other vulnerable areas such as engines to protect the pilot and key flight components, while aircraft designed mostly for air combat tend to have most of their armor placed to protect directly ahead or to the rear, where fire from other aircraft is most likely, leaving them more vulnerable to fire from directly below or to the sides, where much ground fire often comes from.
- `d5s0` European Chemical Industry Council [0]: The European Chemical Industry Council or Cefic (from its former French name "Conseil Européen des Fédérations de l'Industrie Chimique") is the main European trade association for the chemical industry.
- `d5s1` European Chemical Industry Council [1]: It was founded in 1959, and its history follows through the creation of the European Union.
- `d5s2` European Chemical Industry Council [2]: Its headquarters are located in Brussels.
- `d5s3` European Chemical Industry Council [3]: Cefic represents 29,000 large, medium and small chemical companies in Europe, interacting on behalf of their members with international and EU institutions, non-governmental organisations, the international media, and other stakeholders.
- `d5s4` European Chemical Industry Council [4]: Chemicals companies in the European Union employ a total staff of about 1.2 million.
- `d6s0` St. Lucie County Public Schools [0]: St. Lucie County Public Schools is the branding for St. Lucie County School District, which is the school district that manages schools in St. Lucie County, Florida, USA.
- `d6s1` St. Lucie County Public Schools [1]: Whereas, the total staff in the district consists of over 6,500 teachers and 2,300 administration staff.
- `d7s0` Stour Valley Community School [0]: Stour Valley Community School is a coeducational free school for pupils aged 11 to 16 in Clare in the English county of Suffolk.
- `d7s1` Stour Valley Community School [1]: The school opened in September 2011 as one of the first 24 free schools in England.
- `d7s2` Stour Valley Community School [2]: The school opened with around 170 pupils and a total staff of 29, including non-teaching support staff.
- `d7s3` Stour Valley Community School [3]: The headteacher is Christine Inchley.
- `d8s0` The Daily Dot [0]: The Daily Dot is a digital media company covering Internet culture and life on the web.
- `d8s1` The Daily Dot [1]: Founded by Nicholas White in 2011, "The Daily Dot" is headquartered in Austin, Texas with offices in New York City and San Francisco.
- `d8s2` The Daily Dot [2]: It had a full-time staff of 76 in addition to 222 freelance contributors in early 2016 before laying off 40% of its total staff in September 2016.
- `d9s0` Loan modification in the United States [0]: Loan modification is the systematic alteration of mortgage loan agreements that help those having problems making the payments by reducing interest rates, monthly payments or principal balances.
- `d9s1` Loan modification in the United States [1]: Lending institutions could make one or more of these changes to relieve financial pressure on borrowers to prevent the condition of foreclosure.
- `d9s2` Loan modification in the United States [2]: Loan modifications have been practiced in the United States since The 2008 Crash Of The Housing Market from Washington Mutual, Chase Home Finance, Chase, JP Morgan & Chase, other contributors like MER's.
- `d9s3` Loan modification in the United States [3]: Crimes of Mortgage ad Real Estate Staff had long assisted nd finally the squeaky will could not continue as their deviant practices broke the state and crashed.
- `d9s4` Loan modification in the United States [4]: Modification owners either ordered by The United States Department of Housing, The United States IRS or President Obamas letters from Note Holders came to those various departments asking for the Democratic process to help them keep their homes and protection them from explosion.
- `d9s5` Loan modification in the United States [5]: Thus the birth of Modifications.
- `d9s6` Loan modification in the United States [6]: It is yet to date for clarity how theses enforcements came into existence and except b whom, but t is certain that note holders form the Midwest reached out in the Democratic Process for assistance.
- `d9s7` Loan modification in the United States [7]: FBI Mortgage Fraud Department came into existence.
- `d9s8` Loan modification in the United States [8]: Modifications HMAP HARP were also birthed to help note holders get Justice through reduced mortgage by making terms legal.
- `d9s9` Loan modification in the United States [9]: Modification of mortgage terms was introduced by IRS staff addressing the crisis called the HAMP TEAMS that went across the United States desiring the new products to assist homeowners that were victims of predatory lending practices, unethical staff, brokers, attorneys and lenders that contributed to the crash.
- `d9s10` Loan modification in the United States [10]: Modification were a fix to the crash as litigation has ensued as the lenders reorganized and renamed the lending institutions and government agencies are to closely monitor them.
- `d9s11` Loan modification in the United States [11]: Prior to modifications loan holders that experiences crisis would use Loan assumptions and Loan transfers to keep the note in the 1930s.
- `d9s12` Loan modification in the United States [12]: During the Great Depression, loan transfers, loan assumption, and loan bail out programs took place at the state level in an effort to reduce levels of loan foreclosures while the Federal Bureau of Investigation, Federal Trade Commission, Comptroller, the United States Government and State Government responded to lending institution violations of law in these arenas by setting public court records that are legal precedence of such illegal actions.
- `d9s13` Loan modification in the United States [13]: The legal precedents and reporting agencies were created to address the violations of laws to consumers while the Modifications were created to assist the consumers that are victims of predatory lending practices.
- `d9s14` Loan modification in the United States [14]: During the so-called "Great Recession" of the early 21st century, loan modification became a matter of national policy, with various actions taken to alter mortgage loan terms to prevent further economic destabilization.
- `d9s15` Loan modification in the United States [15]: Due to absorbent personal profits nothing has been done to educate Homeowners or Creditors that this money from equity, escrow is truly theirs the Loan Note Holder and it is their monetary rights as the real prize and reason for the Housing Crash was the profit n obtaining the mortgage holders Escrow.
- `d9s16` Loan modification in the United States [16]: The Escrow and Equity that is accursed form the Note Holders payments various staff through the United States claimed as recorded and cashed by all staff in real-estate from local residential Tax Assessing Staff, Real Estate Staff, Ordinance Staff, Police Staff, Brokers, attorneys, lending institutional staff but typically Attorneys who are also typically the owners or Rental properties that are trained through Bankruptcies'.
- `d9s17` Loan modification in the United States [17]: that collect the Escrow that is rightfully the Homeowners but because most Homeowners are unaware of what money is due them and how they can loose their escrow.
- `d9s18` Loan modification in the United States [18]: Most Creditors are unaware that as the note holder that the Note Holder are due a annual or semi annual equity check and again bank or other lending and or legal intuitions staff claim this monies instead.
- `d9s19` Loan modification in the United States [19]: This money Note Holders were unaware of is the prize of real estate and the cause of the Real Estate Crash of 2008 where Lending Institutions provided mortgages to people years prior they know they would eventually loose with Loan holders purchasing Balloon Mortgages lending product that is designed to make fast money off the note holder whom is always typically unaware of their escrow, equity and that are further victimized by conferences and books on HOW TO MAKE MONEY IN REAL STATE - when in fact the money is the Note Holder.
- `d9s20` Loan modification in the United States [20]: The key of the crash was not the House, but the loan product used and the interest and money that was accrued form the note holders that staff too immorally.
- `d9s21` Loan modification in the United States [21]: The immoral and illegal actions of predatory lending station and their staff began with the inception of balloon mortgages although illegal activity has always existed in the arena, yet the crash created "Watch Dog" like HAMP TEAM, IRS, COMPTROLLER< Federal Trade Commission Consumer Protection Bureau, FBI, CIA, Local Police Department, ICE ( The FBI online Computer crime division receives and investigates computer crimes that record keeping staff from title companies, lending institutional staff, legal staff and others created fraudulent documents to change payments and billing of note holders to obtain the money note holders are typically unaware of) and other watch dog agencies came into existence to examine if houses were purchased through a processed check at Government Debited office as many obtained free homes illegally.
- `d9s22` Loan modification in the United States [22]: Many were incarcerated for such illegal actions.
- `d9s23` Loan modification in the United States [23]: Modifications fixed the Notes to proper lower interest, escrow, tax fees that staff typically raised for no reason.
- `d9s24` Loan modification in the United States [24]: Many people from various arenas involved in reals estate have been incarcerated for these actions as well as other illegal actions like charging for a modification.
- `d9s25` Loan modification in the United States [25]: Additionally Modifications were also made to address the falsifications such as inappropriate mortgage charges, filing of fraudulently deeds, reporting of and at times filing of fraudulent mortgages that were already paid off that were fraudulently continued by lenders staff and attorneys or brokers or anyone in the Real Estate Chain through the issues of real estate terms to continue to violate United States Laws, contract law and legal precedence where collusion was often done again to defraud and steal from the Note Holder was such a common practice that was evidence as to why the Mortgage Crash in 2008 occurred for the purpose of wining the prize of stealing form Homeowners and those that foreclosed was actually often purposefully for these monies note holders were unaware of to be obtained which was why Balloon mortgages and loans were given to the staff in the Real Estate Market with the hoper and the expectation that the loan holders would default as it offered opportunity to commit illegal transactions of obtaining the homeowners funds.
- `d9s26` Loan modification in the United States [26]: While such scams were addressed through modifications in 2008.
- `d9s27` Loan modification in the United States [27]: The Market relied heavily on Consumers ignorance to prosper, ignorance of real estate terms, ignorance on what they were to be charged properly for unethical financial gain and while staff in real estates lending arenas mingled terms to deceive y deliberate confusion consumers out of cash and homes while the USA Government provided Justice through President Obamas Inception and IRS Inception of Modifications which addressed these unethical profits in Reals Estate.
- `d9s28` Loan modification in the United States [28]: It was in 2009 that HARP, HAMP and Modifications were introduced to stop the victimization of Note Holders.
- `d9s29` Loan modification in the United States [29]: Taking on the Banks that ran USA Government was a great and dangerous undertaking that made America Great Again as Justice for Consumers reigned.
- `d9s30` Loan modification in the United States [30]: Legal action taken against institutions that have such business practices can be viewed in State Code of Law and Federal Law on precedent cases that are available to the public.
- `d9s31` Loan modification in the United States [31]: Finally, It had been unlawful to be charged by an attorney to modify as well as fro banking staff to modify terms to increase a mortgage and or change lending product to a balloon in an concerted effort to make homeowner foreclose which is also illegal, computer fraud and not the governments intended purpose or definition of a modification.
- `d10s0` Flextime [0]: Flextime (also spelled flexitime [British English], flex-time) is a flexible hours schedule that allows workers to alter workday start and finish times.
- `d10s1` Flextime [1]: In contrast to traditional work arrangements that require employees to work a standard 9 a.m. to 5 p.m. day, flextime typically involves a "core" period of the day during which employees are required to be at work (e.g., between 11 a.m. and 3 p.m.), and a "bandwidth" period within which all required hours must be worked (e.g., between 5:30 a.m. and 7:30 p.m.).
- `d10s2` Flextime [2]: The working day outside of the "core" period is "flexible time", in which employees can choose when they work, subject to achieving total daily, weekly or monthly hours within the "bandwidth" period set by employers, and subject to the necessary work being done .
- `d10s3` Flextime [3]: The total working time required of employees on flextime schedules is the same as that required under traditional work schedules.
- `d10s4` Flextime [4]: A flextime policy allows staff to determine when they will work, while a flexplace policy allows staff to determine where they will work.
- `d10s5` Flextime [5]: Advantages include allowing employees to coordinate their work hours with public transport schedules, with the schedules of their children, and with daily traffic patterns to avoid high congestion times such as rush hour.
- `d10s6` Flextime [6]: Some claim that flexible working will change the nature of the way we work.

</details>

## Q281 — `hotpotqa_5adfb790554299603e418389` (revised draft)

> What do Eragrostis and Rhexia have in common?

Source answer: plant genus

Gold final answer: plant genus

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: classification of Eragrostis | false | plant genus | — | [d4s0] | — |
| u2: classification of Rhexia | false | plant genus | — | [d3s0] | — |
| u3: What do Eragrostis and Rhexia have in common? | true | plant genus | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d3s0` Rhexia [0]: Rhexia is a plant genus of Melastomataceae (ca. 4500 species in 150 genera) family.
- `d4s0` Eragrostis [0]: Eragrostis is a large and widespread genus of plants in the grass family, found in many countries on all inhabited continents and many islands.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Eragrostis intermedia [0]: Eragrostis intermedia is a species of grass known by the common name plains lovegrass.
- `d1s1` Eragrostis intermedia [1]: It is native to North and Central America, where it is distributed from the southeastern and southwestern United States south to Costa Rica.
- `d1s2` Eragrostis intermedia [2]: Its range may extend to South America.
- `d2s0` Eragrostis curvula [0]: Eragrostis curvula is a species of grass known by the common name weeping lovegrass.
- `d2s1` Eragrostis curvula [1]: Other common names include Boer lovegrass, curved lovegrass, Catalina lovegrass, and African lovegrass.
- `d3s0` Rhexia [0]: Rhexia is a plant genus of Melastomataceae (ca. 4500 species in 150 genera) family.
- `d3s1` Rhexia [1]: "Rhexia" species are commonly called “meadow beauty” and 11 to 13 species of "Rhexia" have been recognized depending on different taxonomic treatments.
- `d4s0` Eragrostis [0]: Eragrostis is a large and widespread genus of plants in the grass family, found in many countries on all inhabited continents and many islands.
- `d5s0` Cyperus eragrostis [0]: Cyperus eragrostis is a species of sedge known by several common names, including tall flatsedge, nutgrass, tall nutgrass, umbrella sedge, chufa, Earth almond, zula nuts, edible galingale and pale galingale.
- `d6s0` Hawaiian tropical low shrublands [0]: The Hawaiian tropical low shrublands are a tropical savanna ecoregion in the Hawaiian Islands.
- `d6s1` Hawaiian tropical low shrublands [1]: These shrublands cover an area of 1500 km2 in the leeward lowlands of the main islands and most of the smaller islands, including the Northwestern Hawaiian Islands.
- `d6s2` Hawaiian tropical low shrublands [2]: The ecoregion includes both grasslands and mixed shrublands.
- `d6s3` Hawaiian tropical low shrublands [3]: Kāwelu ("Eragrostis variabilis"), mauʻ u ʻ akiʻ aki ("Fimbristylis cymosa"), ʻ akiʻ aki ("Sporobolus virginicus"), and "Lepturus repens" are common grassland plants.
- `d6s4` Hawaiian tropical low shrublands [4]: Shrublands are dominated by ʻ ilima ("Sida fallax"), ʻ aʻ aliʻ i ("Dodonaea viscosa"), naupaka ("Scaevola" spp.)
- `d6s5` Hawaiian tropical low shrublands [5]: , hinahina kū kahakai ("Heliotropium anomalum" var.
- `d6s6` Hawaiian tropical low shrublands [6]: "argenteum"), kīpūkai ("Heliotropium curassavicum"), maʻ o ("Gossypium tomentosum"), ʻ akoko ("Euphorbia" spp.)
- `d6s7` Hawaiian tropical low shrublands [7]: , ʻ āheahea ("Chenopodium oahuense"), naio ("Myoporum sandwicense"), kolokolo kahakai ("Vitex rotundifolia"), and pūkiawe ("Styphelia tameiameiae").
- `d6s8` Hawaiian tropical low shrublands [8]: More than 90% of the plant species found in this ecoregion are endemic, including ʻ ōhai ("Sesbania tomentosa"), ʻ āwiwi ("Schenkia sebaeoides"), and wahine noho kula ("Isodendrion pyrifolium").
- `d7s0` Eragrostis variabilis [0]: Eragrostis variabilis is a species of grass known by the common names variable lovegrass, kawelu, emoloa, and kalamalo.
- `d7s1` Eragrostis variabilis [1]: It is endemic to Hawaii, where it occurs on all the main islands plus Kure Atoll, Midway Atoll, Pearl and Hermes Atoll, Lisianski Island, Laysan, and Nihoa.
- `d8s0` Rhexia aristosa [0]: Rhexia aristosa is a species of flowering plants in the Melastomataceae known by the common names awned meadowbeauty and awnpetal meadowbeauty.
- `d8s1` Rhexia aristosa [1]: It is native to the eastern United States, where it occurs on the coastal plain from New Jersey to Alabama.
- `d9s0` Eragrostis pilosa [0]: Eragrostis pilosa is a species of grass.
- `d9s1` Eragrostis pilosa [1]: It is native to Eurasia and Africa.
- `d9s2` Eragrostis pilosa [2]: It may or may not be native to North America.
- `d9s3` Eragrostis pilosa [3]: It is widely introduced, and it is a common weed in many areas.
- `d10s0` Eragrostis lehmanniana [0]: Eragrostis lehmanniana is a species of grass known by the common name Lehmann lovegrass.
- `d10s1` Eragrostis lehmanniana [1]: It is native to southern Africa.
- `d10s2` Eragrostis lehmanniana [2]: It is present elsewhere as an introduced species.
- `d10s3` Eragrostis lehmanniana [3]: It is well known as an invasive weed in some areas, such as Arizona in the United States.

</details>

## Q282 — `hotpotqa_5adfed45554299603e4183c5` (revised draft)

> What was the career that Sidney Lumet and Albert Ward share in common?

Source answer: screenwriter

Gold final answer: screenwriter

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: listed occupations of Sidney Lumet | false | director, producer, screenwriter | — | [d2s0] | — |
| u2: listed occupations of Albert Ward | false | screenwriter, film director | — | [d9s0] | — |
| u3: What was the career that Sidney Lumet and Albert Ward share in common? | true | screenwriter (accepted alternatives: director; film director; director and screenwriter; screenwriter and director) | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d2s0` Sidney Lumet [0]: Sidney Arthur Lumet ( ; June 25, 1924 – April 9, 2011) was an American director, producer and screenwriter with over 50 films to his credit.
- `d9s0` Albert Ward (film director) [0]: Albert Ward (1870-1956) was a British screenwriter and film director.

Notes:

- 题干只问共同职业，screenwriter及film director都成立，加入其他有效答案；此处aliases承载可接受答案集合，不声称两种职业语义等同。

<details><summary>All source context</summary>

- `d1s0` Gotham Independent Film Awards 1998 [0]: The 8th Annual Gotham Independent Film Awards were held on September 23, 1998 and were hosted by Stanley Tucci.
- `d1s1` Gotham Independent Film Awards 1998 [1]: At the ceremony, Sidney Lumet was honoured with a Career Tribute, Frances McDormand received the Actor Award, Richard LaGravenese was given the Writer Award and David V. Picker was awarded the Producer/Industry Executive Award.
- `d2s0` Sidney Lumet [0]: Sidney Arthur Lumet ( ; June 25, 1924 – April 9, 2011) was an American director, producer and screenwriter with over 50 films to his credit.
- `d2s1` Sidney Lumet [1]: He was nominated for the Academy Award for Best Director for "12 Angry Men" (1957), "Dog Day Afternoon" (1975), "Network" (1976), and "The Verdict" (1982).
- `d2s2` Sidney Lumet [2]: He did not win an individual Academy Award, but he did receive an Academy Honorary Award and 14 of his films were nominated for various Oscars, such as "Network", which was nominated for ten, winning four.
- `d3s0` Night Falls on Manhattan [0]: Night Falls on Manhattan is a 1997 American crime drama film directed by Sidney Lumet, set and filmed on location in New York City.
- `d3s1` Night Falls on Manhattan [1]: Its screenplay is by Lumet, based on a novel by Robert Daley entitled "Tainted Evidence".
- `d4s0` Strip Search (film) [0]: Strip Search is a drama film made for the HBO network, first aired on April 27, 2004.
- `d4s1` Strip Search (film) [1]: The film explores the status of individual liberties in the aftermath of the September 11, 2001 attacks and the approval of the USA PATRIOT Act.
- `d4s2` Strip Search (film) [2]: The film was directed by Sidney Lumet and written by "Oz" creator Tom Fontana.
- `d4s3` Strip Search (film) [3]: It stars Glenn Close, Maggie Gyllenhaal, Ken Leung, Bruno Lastra and Dean Winters.
- `d4s4` Strip Search (film) [4]: The film was first screened at the Monaco Film Premiere with Lumet in person presenting it, in the presence of Fontana.
- `d5s0` Critical Care (film) [0]: Critical Care is a 1997 film directed by Sidney Lumet.
- `d5s1` Critical Care (film) [1]: The film is a satire about American medicine.
- `d5s2` Critical Care (film) [2]: The screenplay by Steven Schwartz is based on the novel by Richard Dooling and stars James Spader, Kyra Sedgwick, Anne Bancroft, Helen Mirren, Jeffrey Wright, and Albert Brooks.
- `d5s3` Critical Care (film) [3]: Rick Baker provided special makeup effects.
- `d5s4` Critical Care (film) [4]: The film is about a doctor who finds himself involved in a fight with two half sisters over the care of their ailing father.
- `d6s0` A Stranger Among Us [0]: A Stranger Among Us is a 1992 film directed by Sidney Lumet and starring Melanie Griffith.
- `d6s1` A Stranger Among Us [1]: It tells the story of an undercover police officer's experiences in a Hasidic community.
- `d6s2` A Stranger Among Us [2]: It was entered into the 1992 Cannes Film Festival.
- `d6s3` A Stranger Among Us [3]: It is often cited as one of Lumet's two failures of the 1990s, the other being "Guilty as Sin" (1993).
- `d6s4` A Stranger Among Us [4]: Despite the poor reviews suffered by both these films, Lumet received the 1993 D. W. Griffith Award of the Directors Guild of America.
- `d6s5` A Stranger Among Us [5]: The film was also the first credited role for actor James Gandolfini.
- `d7s0` Jake Cannavale [0]: Jake Lumet Cannavale (born May 1, 1995) is an American musician and theatre and television actor.
- `d7s1` Jake Cannavale [1]: He appeared on Broadway in 2015 in the comedy "Fish in the Dark" by Larry David.
- `d7s2` Jake Cannavale [2]: He has also appeared on television's "Nurse Jackie".
- `d7s3` Jake Cannavale [3]: He is the son of actor Bobby Cannavale and screenwriter Jenny Lumet.
- `d7s4` Jake Cannavale [4]: He is the grandson of film director Sidney Lumet and a great-grandson of singer/actress Lena Horne.
- `d8s0` ...One Third of a Nation... [0]: ...One Third of a Nation... is a 1939 American drama film directed by Dudley Murphy and written by Oliver H.P. Garrett and Dudley Murphy.
- `d8s1` ...One Third of a Nation... [1]: The film stars Sylvia Sidney, Leif Erickson, Myron McCormick, Hiram Sherman, the future director Sidney Lumet and Muriel Hutchison.
- `d8s2` ...One Third of a Nation... [2]: The film was released on February 10, 1939, by Paramount Pictures.
- `d9s0` Albert Ward (film director) [0]: Albert Ward (1870-1956) was a British screenwriter and film director.
- `d9s1` Albert Ward (film director) [1]: He also play the role of William Shakespeare in the 1914 biopic of the playwright's career "The Life of Shakespeare".
- `d10s0` Jean Aurenche [0]: Jean Aurenche (1903–1992) was a French screenwriter.
- `d10s1` Jean Aurenche [1]: During his career, he wrote 80 films for directors such as René Clément, Bertrand Tavernier, Marcel Carné, Jean Delannoy, Sidney Lumet and Claude Autant Lara.
- `d10s2` Jean Aurenche [2]: He is often associated with the screenwriter Pierre Bost, with whom he had a fertile partnership from 1940 to 1975.

</details>

## Q283 — `hotpotqa_5ae048a255429924de1b708e` (revised draft)

> What movie did Pitof direct which had an action-adventure tie-in video game based off of it in 2004?

Source answer: Catwoman

Gold final answer: Catwoman

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: 2004 film with the same-name action-adventure tie-in game | false | Catwoman | — | [d6s0] | — |
| u2: film {u1} directed by Pitof | true | Catwoman | u1 | [d3s0] | — |

Evidence:

- `d3s0` Catwoman (film) [0]: Catwoman is a 2004 American action superhero film loosely based on the DC Comics character of the same name directed by Pitof, produced by Denise Di Novi and Edward McDonnell, and written by John Rogers, John Brancato and Michael Ferris, with music by Klaus Badelt.
- `d6s0` Catwoman (video game) [0]: Catwoman is an action-adventure tie-in video game based on the 2004 film of the same name based on the fictional character.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Tron: Evolution [0]: Tron: Evolution is a third-person action-adventure, tie-in video game for the film "" by Propaganda Games, published by Disney Interactive.
- `d1s1` Tron: Evolution [1]: It was officially announced at the Spike Video Game Awards and was released for the Microsoft Windows, PlayStation 3, PlayStation Portable and Xbox 360 platforms in 2010.
- `d2s0` Shrek Forever After (video game) [0]: Shrek Forever After (also known as Shrek 4, and Shrek Forever After: The Final Chapter) is an action-adventure video game based on the film of the same name.
- `d2s1` Shrek Forever After (video game) [1]: It was released on May 18, 2010, in North America.
- `d2s2` Shrek Forever After (video game) [2]: It is the fourth and final video game based on the movie series of "Shrek".
- `d2s3` Shrek Forever After (video game) [3]: This was also the last Shrek game to be developed by Activison.
- `d3s0` Catwoman (film) [0]: Catwoman is a 2004 American action superhero film loosely based on the DC Comics character of the same name directed by Pitof, produced by Denise Di Novi and Edward McDonnell, and written by John Rogers, John Brancato and Michael Ferris, with music by Klaus Badelt.
- `d3s1` Catwoman (film) [1]: It stars Halle Berry, Sharon Stone, Benjamin Bratt, Lambert Wilson, Frances Conroy, and Alex Borstein.
- `d4s0` Lego Star Wars: The Video Game [0]: Lego Star Wars: The Video Game is a Lego-themed, action-adventure video game based on the Lego Star Wars line of toys, and the first game in TT Games' Lego video game franchise.
- `d4s1` Lego Star Wars: The Video Game [1]: It was first released on 29 March 2005, and is a video game adaptation of the "Star Wars" prequel trilogy: "" (1999), "" (2002) and "" (2005), with a bonus segment from "A New Hope" (1977).
- `d5s0` X-Men: The Official Game [0]: X-Men: The Official Game (also known as X3: The Official Game) is Activision's tie-in video game to the 2006 film "".
- `d5s1` X-Men: The Official Game [1]: The game covers the events of the films "X2" and "", specifically following the characters of Wolverine, Iceman, and Nightcrawler.
- `d5s2` X-Men: The Official Game [2]: It also bridges the gap between the two films, explaining why Nightcrawler is not present for "The Last Stand", and also introduces new foes to the "X-Men" film canon, such as HYDRA.
- `d6s0` Catwoman (video game) [0]: Catwoman is an action-adventure tie-in video game based on the 2004 film of the same name based on the fictional character.
- `d6s1` Catwoman (video game) [1]: It features the likeness of the film's lead actress, Halle Berry, though the character's voice is provided by actress Jennifer Hale.
- `d7s0` Lego Knights' Kingdom [0]: Lego Knights' Kingdom is an action-adventure video game based on the Lego toy brand.
- `d7s1` Lego Knights' Kingdom [1]: It was developed by Razorback Developments and published in 2004 by THQ for the Game Boy Advance handheld system.
- `d7s2` Lego Knights' Kingdom [2]: It was the second game based on the Knights' Kingdom theme, after "".
- `d7s3` Lego Knights' Kingdom [3]: However, that game was based on the first version of Knights' Kingdom, while the GBA game is based on the second version.
- `d8s0` Mighty Max (toyline) [0]: Mighty Max was a series of toys that were manufactured by Bluebird Toys PLC in the UK in 1992, and designed by Big Monster Toys.
- `d8s1` Mighty Max (toyline) [1]: The toys were similar to the earlier Polly Pocket toyline; however, these toys were marketed primarily towards young boys.
- `d8s2` Mighty Max (toyline) [2]: In Canada and the USA, they were distributed by Irwin Toy Limited and Mattel Inc. respectively.
- `d8s3` Mighty Max (toyline) [3]: The original toyline consisted mainly of "Doom Zones" and "Horror Heads."
- `d8s4` Mighty Max (toyline) [4]: "Doom Zones" were small playsets with a horror theme and featured miniature figurines of menacing creatures and the hero Max, a young boy with blond hair, jeans, a white t-shirt with a red "M" on it, and a baseball cap (the color varied based on the playset purchased) which also always had an "M" on it.
- `d8s5` Mighty Max (toyline) [5]: The "Horror Heads" were smaller-sized playsets, also shaped like the heads of creatures and contained miniature figures.
- `d8s6` Mighty Max (toyline) [6]: It was later adapted into a TV series, as well as a tie-in video game produced by Ocean Software for the Super NES and Mega Drive/Genesis.
- `d9s0` Star Trek (2013 video game) [0]: Star Trek is a third-person action-adventure "Star Trek" video game.
- `d9s1` Star Trek (2013 video game) [1]: It was developed by Digital Extremes and co-published by Namco Bandai Games and Paramount Pictures in association with CBS Studios International.
- `d9s2` Star Trek (2013 video game) [2]: The game was first released in the United States on April 23, 2013, for PlayStation 3, Xbox 360, and Microsoft Windows platforms.
- `d9s3` Star Trek (2013 video game) [3]: It took three years to produce, and was the first in-house video game development by Paramount Studios, who opted not to license development to a third party.
- `d9s4` Star Trek (2013 video game) [4]: The production team aimed for it to be a collaboration with those working on the "Star Trek" films to avoid the typical pitfalls associated with film tie-in video games.
- `d9s5` Star Trek (2013 video game) [5]: Video games which influenced "Star Trek" included the "Mass Effect" series, "Uncharted" and "Metroid Prime", and certain elements of "Star Trek" reflected episodes of "" such as "" and "Amok Time".
- `d10s0` Tron Evolution: Battle Grids [0]: Tron Evolution: Battle Grids is a video game based on the 2010 film "" and the Wii and Nintendo DS version of the third-person action-adventure tie-in video game by the .
- `d10s1` Tron Evolution: Battle Grids [1]: Its storyline predates that of the other versions.
- `d10s2` Tron Evolution: Battle Grids [2]: The video game was developed by n-Space and published by Disney Interactive Studios.

</details>

## Q284 — `hotpotqa_5ae0575755429945ae95931f` (revised draft)

> The 1958 Pro Bowl was played at the California stadium that is the home for which college?

Source answer: University of Southern California

Gold final answer: University of Southern California

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: stadium that hosted the 1958 Pro Bowl | false | Los Angeles Memorial Coliseum | — | [d7s1] | — |
| u2: college whose football team uses {u1} as its home | true | University of Southern California (accepted alternatives: USC) | u1 | [d6s1] | — |

Evidence:

- `d6s1` Los Angeles Memorial Coliseum [1]: The stadium serves as the home to the University of Southern California (USC) Trojans football team, and as the temporary home of the Los Angeles Rams of the National Football League (NFL).
- `d7s1` 1958 Pro Bowl [1]: The game was played on January 12, 1958, at the Los Angeles Memorial Coliseum in Los Angeles, California in front of 66,634 fans.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Merlin Olsen [0]: Merlin Jay Olsen ( ; September 15, 1940 – March 11, 2010) was an American football player, announcer, and actor.
- `d1s1` Merlin Olsen [1]: He played his entire 15-year professional football career in National Football League (NFL) as a defensive tackle with the Los Angeles Rams.
- `d1s2` Merlin Olsen [2]: He was selected to the Pro Bowl a record 14 straight times, missing selection only in the last year of his career.
- `d1s3` Merlin Olsen [3]: This record of 14 seasons selected to play in the Pro Bowl, consecutive or otherwise, is current and shared with former offensive lineman Bruce Matthews, former tight end Tony Gonzalez, and former quarterback Peyton Manning.
- `d1s4` Merlin Olsen [4]: A recipient of the 1961 Outland Trophy as the best lineman in college football, Olsen is a member of the Pro Football Hall of Fame and the College Football Hall of Fame.
- `d1s5` Merlin Olsen [5]: As an actor, he portrayed farmer Jonathan Garvey on "Little House on the Prairie".
- `d1s6` Merlin Olsen [6]: After leaving that series, he starred in his own NBC drama, "Father Murphy".
- `d2s0` 1995 Pro Bowl [0]: The 1995 Pro Bowl was the NFL's all-star game for the 1994 season.
- `d2s1` 1995 Pro Bowl [1]: The game was played on February 5, 1995, at Aloha Stadium in Honolulu, Hawaii.
- `d2s2` 1995 Pro Bowl [2]: The final Score was AFC 41, NFC 13.
- `d2s3` 1995 Pro Bowl [3]: This was the AFC's largest margin of victory since the AFL-NFL merger.
- `d2s4` 1995 Pro Bowl [4]: Rookie Marshall Faulk of the Indianapolis Colts rushed for a Pro Bowl record 180 yards and was the game's MVP.
- `d2s5` 1995 Pro Bowl [5]: Chris Warren added 127 yards rushing as the AFC posted records for rushing yards (400) and total yards (552).
- `d2s6` 1995 Pro Bowl [6]: Both Warren and Faulk broke the Pro Bowl rushing record, formerly held by O.J. Simpson.
- `d3s0` DeSean Jackson [0]: DeSean William Jackson (born December 1, 1986) is an American football wide receiver for the Tampa Bay Buccaneers of the National Football League (NFL).
- `d3s1` DeSean Jackson [1]: He played college football for the University of California, Berkeley, where he was recognized as a consensus All-American.
- `d3s2` DeSean Jackson [2]: He was drafted by the Philadelphia Eagles in the second round of the 2008 NFL Draft, and played for the Washington Redskins for three seasons after his departure from the Eagles.
- `d3s3` DeSean Jackson [3]: Jackson has been selected to the Pro Bowl three times, and was the first player selected to the Pro Bowl at two different positions in the same year when he was named to the 2010 Pro Bowl as a wide receiver and return specialist.
- `d4s0` 2014 Trinidad and Tobago Pro Bowl [0]: The 2014 Trinidad and Tobago Pro Bowl is the tenth season of the "Digicel Pro Bowl", which is a knockout football tournament for Trinidad and Tobago teams competing in the TT Pro League.
- `d4s1` 2014 Trinidad and Tobago Pro Bowl [1]: For the fourth consecutive season, the Pro Bowl concluded the Pro League calendar.
- `d4s2` 2014 Trinidad and Tobago Pro Bowl [2]: Additionally, for the third year the winner of the Pro Bowl was invited to compete in the Digicel Charity Shield to open the 2014–15 Pro League season.
- `d4s3` 2014 Trinidad and Tobago Pro Bowl [3]: W Connection entered as the Pro Bowl holders having defeated North East Stars by a score of 4–3 in a penalty shootout after the match ended in 0–0 in regulation during the 2013 final in Hasely Crawford Stadium.
- `d4s4` 2014 Trinidad and Tobago Pro Bowl [4]: The competition commenced on 2 May with all nine Pro League teams competing in single elimination beginning with the qualifying round and concluded on 23 May with the final.
- `d5s0` Trinidad and Tobago Pro Bowl [0]: The Trinidad and Tobago Pro Bowl, or commonly known as the Digicel Pro Bowl for sponsorship reasons, is a knockout football tournament for teams in the TT Pro League.
- `d5s1` Trinidad and Tobago Pro Bowl [1]: The competition is played during May following the conclusion of the Pro League season.
- `d5s2` Trinidad and Tobago Pro Bowl [2]: The Pro Bowl began without a sponsor during the competitions's first two years.
- `d5s3` Trinidad and Tobago Pro Bowl [3]: It was not until 2006, when Courts began providing monetary prizes, that the tournament had its first sponsor.
- `d5s4` Trinidad and Tobago Pro Bowl [4]: Following a pullout by Courts after three years, Digicel became the new branding partner of the competition.
- `d5s5` Trinidad and Tobago Pro Bowl [5]: The prize money for the winner, as announced by TT Pro League CEO Dexter Skeene, is determined by the players, the clubs and the communities.
- `d5s6` Trinidad and Tobago Pro Bowl [6]: With this programme the communities are expected to adopt the clubs and pledge their support to them during the tournament.
- `d5s7` Trinidad and Tobago Pro Bowl [7]: The prize money will be the amount received from gate receipts and TT$100,000, courtesy of tournament sponsors Digicel.
- `d6s0` Los Angeles Memorial Coliseum [0]: The Los Angeles Memorial Coliseum is an American sports stadium located in the Exposition Park neighborhood of Los Angeles, California.
- `d6s1` Los Angeles Memorial Coliseum [1]: The stadium serves as the home to the University of Southern California (USC) Trojans football team, and as the temporary home of the Los Angeles Rams of the National Football League (NFL).
- `d6s2` Los Angeles Memorial Coliseum [2]: The Coliseum was home to the Rams from 1946 to 1979, when they moved to Anaheim Stadium in Anaheim, California, and is serving as their home stadium again until the completion of Los Angeles Stadium at Hollywood Park in Inglewood, California.
- `d6s3` Los Angeles Memorial Coliseum [3]: The facility has a permanent seating capacity of 93,607 for USC football games, making it the largest football stadium in the Pac-12 Conference.
- `d6s4` Los Angeles Memorial Coliseum [4]: For Rams games, capacity is at 93,607, giving it the largest capacity in the NFL.
- `d7s0` 1958 Pro Bowl [0]: The 1958 Pro Bowl was the NFL's eighth annual all-star game which featured the outstanding performers from the 1957 season.
- `d7s1` 1958 Pro Bowl [1]: The game was played on January 12, 1958, at the Los Angeles Memorial Coliseum in Los Angeles, California in front of 66,634 fans.
- `d7s2` 1958 Pro Bowl [2]: The West squad defeated the East by a score of 26–7.
- `d8s0` 2013 Trinidad and Tobago Pro Bowl [0]: The 2013 Trinidad and Tobago Pro Bowl was the ninth season of the "Digicel Pro Bowl", which is a knockout football tournament for Trinidad and Tobago teams competing in the TT Pro League.
- `d8s1` 2013 Trinidad and Tobago Pro Bowl [1]: For the third consecutive season, the Pro Bowl concluded the Pro League calendar.
- `d8s2` 2013 Trinidad and Tobago Pro Bowl [2]: Additionally, for the second year the winner of the Pro Bowl was invited to compete in the Digicel Charity Shield to open the 2013–14 Pro League season.
- `d8s3` 2013 Trinidad and Tobago Pro Bowl [3]: Defence Force entered as the Pro Bowl holders having defeated Caledonia AIA by a score of 5–2 in the 2012 final in Hasely Crawford Stadium.
- `d8s4` 2013 Trinidad and Tobago Pro Bowl [4]: The competition commenced on 17 May with all eight Pro League teams competing in single elimination beginning in the quarterfinals and concluded on 29 May with the final.
- `d9s0` 2012 Trinidad and Tobago Charity Shield [0]: The 2012 Trinidad and Tobago Charity Shield (known as the "Digicel Charity Shield" for sponsorship reasons) was the inaugural edition of the Charity Shield, which was a football match that opened the 2012–13 TT Pro League season.
- `d9s1` 2012 Trinidad and Tobago Charity Shield [1]: The match was played at Manny Ramjohn Stadium in Marabella on 8 September 2012, between the winners of the previous season's Pro League and Pro Bowl competitions.
- `d9s2` 2012 Trinidad and Tobago Charity Shield [2]: The match was contested by the 2012 Digicel Pro Bowl winners, Defence Force, and the champions of the 2011–12 Pro League, W Connection.
- `d9s3` 2012 Trinidad and Tobago Charity Shield [3]: The "Savonetta Boys" won the match 2–0 with goals from Shahdon Winchester and Joevin Jones, who was later named the "Man of the Match".
- `d10s0` 2017 Pro Bowl [0]: The 2017 Pro Bowl (branded as the 2017 Pro Bowl presented by Aquafina for sponsorship reasons) was the National Football League's all-star game for the 2016 season which was played at Camping World Stadium in Orlando, Florida on January 29, 2017.
- `d10s1` 2017 Pro Bowl [1]: The game was the first in a three-year deal to host the Pro Bowl in Orlando, which also included cross-promotional events (such as a newly-established skills competition) held at the Walt Disney World Resort (which is owned by the parent company of the game's broadcaster, ESPN).

</details>

## Q285 — `hotpotqa_5ae0a6ea5542993d6555ebe9` (revised draft)

> Are Waste Land and Shikashika both types of drinks?

Source answer: no

Gold final answer: no

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: whether Waste Land is a drink | false | no **[by_omission]** | — | [d8s0] | — |
| u2: whether Shikashika is a drink | false | yes | — | [d3s0] | — |
| u3: Are Waste Land and Shikashika both types of drinks? | true | no | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d3s0` Shikashika [0]: Shikashika is a shaved ice drink made from glacier ice in Peru and Bolivia.
- `d8s0` Waste Land (film) [0]: Waste Land is a 2010 British-Brazilian documentary film directed by Lucy Walker.

Notes:

- The negative uses the allowed entity-category omission exception from the defining film description.
- 复核后保留原标注；原note为说明或未发现需要修改的证据/依赖问题。

<details><summary>All source context</summary>

- `d1s0` Waste management law [0]: Waste management laws<section begin=overview /> govern the transport, treatment, storage, and disposal of all manner of waste, including municipal solid waste, hazardous waste, and nuclear waste, among many other types.
- `d1s1` Waste management law [1]: Waste laws are generally designed to minimize or eliminate the uncontrolled dispersal of waste materials into the environment in a manner that may cause ecological or biological harm, and include laws designed to reduce the generation of waste and promote or mandate waste recycling.
- `d1s2` Waste management law [2]: Regulatory efforts include identifying and categorizing waste types and mandating transport, treatment, storage, and disposal practices.
- `d1s3` Waste management law [3]: <section end=overview />
- `d2s0` Business waste [0]: Business (or commercial and industrial) waste – cover the commercial waste and industrial waste types .
- `d2s1` Business waste [1]: Generally, businesses are expected to make their own arrangements for the collection, treatment and disposal of their wastes.
- `d2s2` Business waste [2]: Waste from smaller shops and trading estates where local authority waste collection agreements are in place will generally be treated as municipal waste.
- `d3s0` Shikashika [0]: Shikashika is a shaved ice drink made from glacier ice in Peru and Bolivia.
- `d3s1` Shikashika [1]: In some rural communities, the extraction and sale of ice continues to be a primary natural resource for local economies.
- `d3s2` Shikashika [2]: Ice merchants extract the blocks with an axe by hand and transport them down from the mountains atop mules.
- `d3s3` Shikashika [3]: The unit of sale is usually an ice block weighing approximately 40 kilos which is sold to Shikashika vendors.
- `d3s4` Shikashika [4]: Each block sells for approximately 17 USD.
- `d3s5` Shikashika [5]: In turn, Shikashika is sold for approximately 15 cents in plastic bags with colorful sweet syrups at Andean festivals and on market day.
- `d3s6` Shikashika [6]: The word Shikashika is onomatopeia from the Amerindian language Quechua.
- `d3s7` Shikashika [7]: An alternative word for Shikashika in Spanish is "raspadilla."
- `d4s0` Composite liner [0]: Disposing trash on Earth mainly comes in three ways: littering, incinerating, and storing in it the many landfills we have around the world.
- `d4s1` Composite liner [1]: With today’s landfills, there are very constructed contaminate structures.
- `d4s2` Composite liner [2]: These systems are designed to help keep solid waste from becoming too uncontained and uncontrolled from the environment and the impact it could have on the health of humans.
- `d4s3` Composite liner [3]: The purpose of having a liner system within a landfill is mainly to isolate everything within the landfill from the environment and protect it from contaminating the contents of the soil and especially the water within the ground.
- `d4s4` Composite liner [4]: These liners are engineered to create a physical barrier between the garbage within the landfill, the ground, and the environment, in order to separate the liquid contaminate (leachate) so that it can go to a treatment facility.
- `d4s5` Composite liner [5]: There are different types of these landfill sites for the different types of solid wastes which society creates and leaves behind.
- `d4s6` Composite liner [6]: There are certain levels of harmfulness in which the different types of trash have; therefore, there are different types of liner systems which are required for these different types of disposal sites.
- `d4s7` Composite liner [7]: The first type is single liner-systems.
- `d4s8` Composite liner [8]: These systems usually are put within landfills which mostly hold construction rubble.
- `d4s9` Composite liner [9]: These landfills are not meant to hold the disposal of harmful liquid wastes such as paint, tar, or any other type of liquid garbage that can easily seep through a single liner system.
- `d4s10` Composite liner [10]: The second type is double-liner systems.
- `d4s11` Composite liner [11]: These systems are usually found in municipal solid waste landfills as well all hazardous waste landfills.
- `d4s12` Composite liner [12]: The first part is constructed to collect the leachate while the second layer is engineered to be a leak-detection system to ensure that no contaminates leak into the ground and contaminate everything.
- `d5s0` Gerontion [0]: "Gerontion" is a poem by T. S. Eliot that was first published in 1920.
- `d5s1` Gerontion [1]: The work relates the opinions and impressions of a gerontic, or elderly man, through a dramatic monologue which describes Europe after World War I through the eyes of a man who has lived the majority of his life in the 19th century.
- `d5s2` Gerontion [2]: Eliot considered using this already published poem as a preface to "The Waste Land", but decided to keep it as an independent poem.
- `d5s3` Gerontion [3]: Along with "The Love Song of J. Alfred Prufrock" and "The Waste Land", and other works published by Eliot in the early part of his career, '"Gerontion" discusses themes of religion, sexuality, and other general topics of modernist poetry.
- `d6s0` Household hazardous waste [0]: Household hazardous waste (HHW), sometimes called retail hazardous waste or "home generated special materials', is post-consumer waste which qualifies as hazardous waste when discarded.
- `d6s1` Household hazardous waste [1]: It includes household chemicals and other substances for which the owner no longer has a use, such as consumer products sold for home care, personal care, automotive care, pest control and other purposes.
- `d6s2` Household hazardous waste [2]: These products exhibit many of the same dangerous characteristics as fully regulated hazardous waste due to their potential for reactivity, ignitability, corrosivity, toxicity, or persistence.
- `d6s3` Household hazardous waste [3]: Examples include drain cleaners, oil paint, motor oil, antifreeze, fuel, poisons, pesticides, herbicides and rodenticides, fluorescent lamps, lamp ballasts, smoke detectors, medical waste, some types of cleaning chemicals, and consumer electronics (such as televisions, computers, and cell phones).
- `d7s0` Civic amenity site [0]: A civic amenity site (CA site) or household waste recycling centre (HWRC) is a facility where the public can dispose of household waste and also often containing recycling points.
- `d7s1` Civic amenity site [1]: Civic amenity sites are run by the local authority in a given area.
- `d7s2` Civic amenity site [2]: Collection points for recyclable waste such as green waste, metals, glass and other waste types (including WVO) are available.
- `d7s3` Civic amenity site [3]: Items that cannot be collected by local waste collection schemes such as bulky waste are also provided.
- `d8s0` Waste Land (film) [0]: Waste Land is a 2010 British-Brazilian documentary film directed by Lucy Walker.
- `d8s1` Waste Land (film) [1]: The film chronicles artist Vik Muniz, who travels to the world's largest landfill, Jardim Gramacho outside Rio de Janeiro, to collaborate with a lively group of catadores of recyclable materials, who find a way to the most prestigious auction house in London via the surprising transformation of refuse into contemporary art.
- `d8s2` Waste Land (film) [2]: The catadores work in a co-operative founded and led by Sebastião Carlos Dos Santos, the ACAMJG, or Association of Pickers of Jardim Gramacho, who dreamed of improving life for his community.
- `d8s3` Waste Land (film) [3]: The money created by the selling of the artworks was given back to the catadores and the ACAMJG, as well as the prize money from the film awards, to help the catadores and their community.
- `d9s0` Chemical waste [0]: Chemical waste is a waste that is made from harmful chemicals (mostly produced by large factories).
- `d9s1` Chemical waste [1]: Chemical waste may fall under regulations such as COSHH in the United Kingdom, or the Clean Water Act and Resource Conservation and Recovery Act in the United States.
- `d9s2` Chemical waste [2]: In the U.S., the Environmental Protection Agency (EPA) and the Occupational Safety and Health Administration (OSHA), as well as state and local regulations also regulate chemical use and disposal.
- `d9s3` Chemical waste [3]: Chemical waste may or may not be classed as hazardous waste.
- `d9s4` Chemical waste [4]: A chemical hazardous waste is a solid, liquid, or gaseous material that displays either a “Hazardous Characteristic” or is specifically “listed” by name as a hazardous waste.
- `d9s5` Chemical waste [5]: There are four characteristics chemical wastes may have to be considered as hazardous.
- `d9s6` Chemical waste [6]: These are Ignitability, Corrosivity, Reactivity, and Toxicity.
- `d9s7` Chemical waste [7]: This type of hazardous waste must be categorized as to its identity, constituents, and hazards so that it may be safely handled and managed.
- `d9s8` Chemical waste [8]: Chemical waste is a broad term and encompasses many types of materials.
- `d9s9` Chemical waste [9]: Consult the Material Safety Data Sheet (MSDS), Product Data Sheet or Label for a list of constituents.
- `d9s10` Chemical waste [10]: These sources should state whether this chemical waste is a waste that needs special disposal.
- `d10s0` Kulotunga Cinkaiariyan [0]: Kulotunga Cinkaiariyan (Tamil: குலோத்துங்க சிங்கையாரியன் ) was the third of the Aryacakravarti kings of Jaffna Kingdom.
- `d10s1` Kulotunga Cinkaiariyan [1]: Author of the book “Ancient Jaffna” C. Rasanayagam calculated that he has been ruled Jaffna from 1256 to 1279 (23 years).
- `d10s2` Kulotunga Cinkaiariyan [2]: Yalpana Vaipava Malai says he followed his ancestor and promoted agriculture, and he converted waste land into agriculture land.
- `d10s3` Kulotunga Cinkaiariyan [3]: Also the book added that during his rule the kingdom was peaceful and prosper.

</details>

## Q286 — `hotpotqa_5ae1af14554299234fd042c4` (revised draft)

> Are both William Beaudine and Richard Benjamin American actors?

Source answer: yes

Gold final answer: yes

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: occupation and nationality descriptor of William Beaudine | false | American film actor | — | [d1s0] | — |
| u2: occupation and nationality descriptor of Richard Benjamin | false | American actor | — | [d5s0] | — |
| u3: Are both William Beaudine and Richard Benjamin American actors? | true | yes | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d1s0` William Beaudine [0]: William Washington Beaudine (January 15, 1892 – March 18, 1970) was an American film actor and director.
- `d5s0` Richard Benjamin [0]: Richard Samuel Benjamin (born May 22, 1938) is an American actor and film director.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` William Beaudine [0]: William Washington Beaudine (January 15, 1892 – March 18, 1970) was an American film actor and director.
- `d1s1` William Beaudine [1]: He was one of Hollywood's most prolific directors, turning out films in remarkable numbers and in a wide variety of genres.
- `d2s0` Penrod and Sam (1931 film) [0]: Penrod and Sam is a 1931 American Pre-Code comedy film directed by William Beaudine and starring Leon Janney and Frank Coghlan Jr. It is an adaptation of the novel "Penrod and Sam" by Booth Tarkington.
- `d2s1` Penrod and Sam (1931 film) [1]: Beaudine had previously directed a 1923 silent version "Penrod and Sam", and was invited to remake his earlier success.
- `d3s0` Cornered (1924 film) [0]: Cornered is a 1924 American silent drama film directed by William Beaudine.
- `d3s1` Cornered (1924 film) [1]: It is considered to be a lost.
- `d3s2` Cornered (1924 film) [2]: The story was filmed again in 1930, this time as a talkie called "Road to Paradise".
- `d3s3` Cornered (1924 film) [3]: It was also directed by Beaudine.
- `d4s0` Adventures of Kitty O'Day [0]: Adventures of Kitty O'Day is a 1945 American comedy mystery film directed by William Beaudine and starring Jean Parker, Peter Cookson and Tim Ryan.
- `d4s1` Adventures of Kitty O'Day [1]: It was a sequel to the 1944 film "Detective Kitty O'Day".
- `d4s2` Adventures of Kitty O'Day [2]: The two films were an attempt to create a new detective series but no further films were made.
- `d4s3` Adventures of Kitty O'Day [3]: A third film, "Fashion Model", also directed by Beaudine, was made using a similar formula but with another actress playing a heroine with a different name.
- `d5s0` Richard Benjamin [0]: Richard Samuel Benjamin (born May 22, 1938) is an American actor and film director.
- `d6s0` Boy of Mine [0]: Boy of Mine is a 1923 American silent family drama film directed by William Beaudine.
- `d6s1` Boy of Mine [1]: It stars Ben Alexander, Rockliffe Fellowes, and Henry B. Walthall.
- `d6s2` Boy of Mine [2]: Wendy L. Marshall stated that "Beaudine had the Midas touch when it came to directing children" in films like this and "Penrod and Sam".
- `d7s0` Road to Paradise (film) [0]: Road to Paradise is a 1930 American pre-Code drama film produced and distributed by First National Pictures, and starring Loretta Young, Jack Mulhall and Raymond Hatton.
- `d7s1` Road to Paradise (film) [1]: It was directed by William Beaudine and is based on a 1920 play Dodson Mitchell by Zelda Sears called "Cornered".
- `d7s2` Road to Paradise (film) [2]: The film was a remake of a 1924 silent version, entitled "Cornered", which was also directed by William Beaudine.
- `d8s0` Men in Her Life [0]: Men in Her Life is a 1931 American Pre-Code drama film directed by William Beaudine and starring Lois Moran, Charles Bickford and Victor Varconi.
- `d8s1` Men in Her Life [1]: It was based on a novel by Warner Fabian (Samuel Hopkins Adams).
- `d8s2` Men in Her Life [2]: It was made during a brief spell Beaudine had working at Columbia Pictures.
- `d8s3` Men in Her Life [3]: Critics considered the film one of the studio's better B releases.
- `d8s4` Men in Her Life [4]: Part of the film was set in the Café de la Paix in Paris which was reconstructed authentically at the Columbia studios.
- `d8s5` Men in Her Life [5]: Columbia also made a Spanish-language version of this film, entitled "Hombres en mi vida".
- `d9s0` Clancy Street Boys [0]: Clancy Street Boys is a 1943 film directed by William Beaudine and starring the East Side Kids.
- `d9s1` Clancy Street Boys [1]: It is Beaudine's first film with the team; he would direct several more in the series and many in the Bowery Boys canon.
- `d9s2` Clancy Street Boys [2]: Leo Gorcey married the female lead Amelita Ward.
- `d9s3` Clancy Street Boys [3]: There is no mention of "Clancy Street" in the film, but a rival gang at Cherry Street appears at the beginning and climax of the film.
- `d10s0` Billy the Kid Versus Dracula [0]: Billy the Kid vs. Dracula is a 1966 American low-budget horror-Western film directed by William Beaudine.
- `d10s1` Billy the Kid Versus Dracula [1]: It was released theatrically as part of a double bill, along with "Jesse James Meets Frankenstein's Daughter".
- `d10s2` Billy the Kid Versus Dracula [2]: Both films were shot in eight days at Corriganville Movie Ranch and at Paramount Studios in mid 1965; both were the final feature films of director William Beaudine.
- `d10s3` Billy the Kid Versus Dracula [3]: The film revolves around Billy the Kid played by stuntman Chuck Courtney trying to save his fiancee from Dracula (John Carradine repeating his role from the low-budget Universal Studios movie sequels to the Bela Lugosi classic).
- `d10s4` Billy the Kid Versus Dracula [4]: The films were produced by television producer Carroll Case for Joseph E. Levine.

</details>

## Q287 — `hotpotqa_5ac3983a554299657fa290f5` (revised draft)

> At the 2011 census, what was he population of the city where Kerry Saxby-Junna was born?

Source answer: 6,960

Gold final answer: 6,960

Question type: `bridge` (source type `bridge`)

Replaces: `hotpotqa_5ae1afe9554299234fd042c6`

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: town where Kerry Saxby-Junna was born | false | Young, New South Wales | — | [d3s1] | — |
| u2: 2011 census population of {u1} | true | 6,960 | u1 | [d7s1] | — |

Evidence:

- `d3s1` Kerry Saxby-Junna [1]: She was born in Young, New South Wales and grew up in Ballina, New South Wales.
- `d7s1` Young, New South Wales [1]: At the 2011 census , Young had a population of 6,960.

Notes:

- 替换：母公司创始人不能直接当作电视网络创始人。 新题保留原source type，人工核对两条显式事实及答案。

<details><summary>All source context</summary>

- `d1s0` Demography of the United Kingdom [0]: According to the 2011 census, the total population of the United Kingdom was around 63,182,000.
- `d1s1` Demography of the United Kingdom [1]: <ref name="2http://www.ons.gov.uk/ons/dcp171778_292378.pdf |title=2011 Census: Population Estimates for the United Kingdom |publisher=Office for National Statistics |date=27 March 2011 |accessdate=18 December 2012 }}</ref> It is the 22nd-largest in the world.
- `d1s2` Demography of the United Kingdom [2]: Its overall population density is 259 people per square kilometre (671 people per sq mi), with England having a significantly higher population density than Wales, Scotland and Northern Ireland.
- `d1s3` Demography of the United Kingdom [3]: Almost one-third of the population lives in England's southeast, which is predominantly urban and suburban, with about 8 million in the capital city of London, the population density of which is just over 5,200 per square kilometre (13,468 per sq mi).
- `d2s0` Orleans, Ontario [0]: Orléans ( ; French: ] ) (officially Orléans), is a suburb of Ottawa, Ontario, Canada.
- `d2s1` Orleans, Ontario [1]: It is located in the eastern part of the city along the Ottawa River, about 16 km from downtown Ottawa.
- `d2s2` Orleans, Ontario [2]: The Canada 2011 Census determined that Orléans' population was 107,823.
- `d2s3` Orleans, Ontario [3]: Prior to being amalgamated into Ottawa in 2001, the community of Orléans was spread over two municipal jurisdictions, the eastern portion being in the pre-amalgamation City of Cumberland, the western portion in the City of Gloucester.
- `d2s4` Orleans, Ontario [4]: According to the 2011 census, 62,888 people lived in the Cumberland portion of Orléans, while 44,935 people lived in the Gloucester portion.
- `d2s5` Orleans, Ontario [5]: Today, Orléans spans the municipal wards of Orléans, Innes and Cumberland.
- `d2s6` Orleans, Ontario [6]: Orléans is one of 3 areas of the post-amalgamated City of Ottawa to contain a significant francophone population, hence the community's name.
- `d3s0` Kerry Saxby-Junna [0]: Kerry-Anne Saxby-Junna, born Kerry Saxby AM (born 2 June 1961) is a retired Australian race walker.
- `d3s1` Kerry Saxby-Junna [1]: She was born in Young, New South Wales and grew up in Ballina, New South Wales.
- `d4s0` Blennerville [0]: Blennerville (Irish: "Cathair Uí Mhóráin" , meaning "the seat/home of the Morans") is a small village and now a suburb of Tralee, County Kerry, Ireland.
- `d4s1` Blennerville [1]: It is approximately 1 mi west of the town centre on the N86 road to Dingle, where the River Lee enters Tralee Bay.
- `d4s2` Blennerville [2]: The village was formerly Tralee's port, and is connected to the town centre by the Tralee Ship Canal.
- `d4s3` Blennerville [3]: Part of Blennerville electoral division falls within the area of Tralee Town Council, and at the 2011 census had a population of 141.
- `d4s4` Blennerville [4]: The remaining portion, outside the urban boundaries, had a 2011 population of 556.
- `d5s0` Islam in West Bengal [0]: Since the partition of India in 1947, the majority of the Bengali Muslims have lived in Bangladesh.
- `d5s1` Islam in West Bengal [1]: Islam is the minority religion in West Bengal as of 2011.
- `d5s2` Islam in West Bengal [2]: However, Islam is also the second largest and the fastest growing religion in the Indian state of West Bengal.
- `d5s3` Islam in West Bengal [3]: According to 2011 Census of India, West Bengal has over 24.6 million Bengali Muslims, who form 27% of the state's population.
- `d5s4` Islam in West Bengal [4]: In West Bengal capital Kolkata Muslim's Population is 926,414 making up 20.6% of the city population as of 2011 census.
- `d5s5` Islam in West Bengal [5]: Bengali Muslims are minority in all districts of Bengal except Uttar Dinajpur (49.92%), Maldah (51.27%) and Murshidabad (66.28%) .
- `d5s6` Islam in West Bengal [6]: It is also said that this rise is due to proximity to Muslim-dominated districts of neighboring state of Bihar and illegal migration from Bangladesh cause demography change in the state.
- `d6s0` Korçë [0]: Korçë (] ; (definite Albanian form: "Korça" ), other names see below) is a city and municipality in southeastern Albania, and the seat of Korçë County.
- `d6s1` Korçë [1]: It was formed at the 2015 local government reform by the merger of the former municipalities Drenovë, Korçë, Lekas, Mollaj, Qendër Bulgarec, Vithkuq, Voskop and Voskopojë, that became municipal units.
- `d6s2` Korçë [2]: The seat of the municipality is the city Korçë.
- `d6s3` Korçë [3]: The total population is 75,994 (2011 census), in a total area of 805.99 km2 .
- `d6s4` Korçë [4]: The population of the former municipality at the 2011 census was 51,152.
- `d6s5` Korçë [5]: It is the sixth largest city in Albania.
- `d6s6` Korçë [6]: It stands on a plateau some 850 m above sea level, surrounded by the Morava Mountains.
- `d7s0` Young, New South Wales [0]: Young is a town in the South West Slopes region of New South Wales, Australia and the largest town in Hilltops Council.
- `d7s1` Young, New South Wales [1]: At the 2011 census , Young had a population of 6,960.
- `d8s0` Northern Region, Manitoba [0]: The Northern Region is a region in the Canadian province of Manitoba.
- `d8s1` Northern Region, Manitoba [1]: It is situated on the Canadian Shield and includes Manitoba's Hudson Bay coastline.
- `d8s2` Northern Region, Manitoba [2]: The major economic activities are mining and tourism.
- `d8s3` Northern Region, Manitoba [3]: The region is composed of four census divisions: 19 and 21–23 .
- `d8s4` Northern Region, Manitoba [4]: The land area of the region is 438,491.51 km² (169,302.52 mi²), which encompasses 67% of Manitoba's total land area.
- `d8s5` Northern Region, Manitoba [5]: The vast majority of the region is undeveloped wilderness.
- `d8s6` Northern Region, Manitoba [6]: Its total population at the 2011 census was 88,146, which was only 7.3% of Manitoba's total population in the 2011 census.
- `d8s7` Northern Region, Manitoba [7]: The largest municipality is the city of Thompson.
- `d8s8` Northern Region, Manitoba [8]: Other major population centers include the city of Flin Flon and the town of The Pas.
- `d8s9` Northern Region, Manitoba [9]: Indian reserves comprise more than 49% of the region's population.
- `d8s10` Northern Region, Manitoba [10]: There are 54 reserves with a total population of 40,572.
- `d8s11` Northern Region, Manitoba [11]: The largest of these are Norway House 17 and Peguis 1B.
- `d9s0` Warton, Lancaster [0]: Warton is a village, civil parish and electoral ward in the City of Lancaster in north Lancashire in the north-west of England, close to the boundary with Cumbria, with a population of around 2,000, measured at the 2011 Census to be 2,360.
- `d9s1` Warton, Lancaster [1]: It is a village steeped in history; its earliest recording as a settlement is made in Domesday Book written in 1086.
- `d9s2` Warton, Lancaster [2]: The nearest town to Warton is Carnforth, which was originally part of Warton parish.
- `d9s3` Warton, Lancaster [3]: It has connections to the first President of the United States, George Washington: Washington's ancestor of seven generations, Lawrence Washington, is rumoured to have helped build the village church of St Oswald.
- `d9s4` Warton, Lancaster [4]: The parish covers an area in excess of 11000 acre and is predominantly rural.
- `d9s5` Warton, Lancaster [5]: The parish of Warton had a population of 2315 recorded in the 2001 census, and 2,360 in the 2011 census.
- `d10s0` Ackworth, West Yorkshire [0]: Ackworth is a village and civil parish in the metropolitan borough of Wakefield, West Yorkshire, England, situated between Pontefract, Barnsley and Doncaster on the small River Went.
- `d10s1` Ackworth, West Yorkshire [1]: The village consists of four parts, High Ackworth, Low Ackworth, Ackworth Moor Top, and Brackenhill.
- `d10s2` Ackworth, West Yorkshire [2]: According to the 2001 census it had a population of 6,493, increasing to 7,049 at the 2011 Census.
- `d10s3` Ackworth, West Yorkshire [3]: There is also a City of Wakefield Ward called Ackworth, North Elmsall and Upton.
- `d10s4` Ackworth, West Yorkshire [4]: At the 2011 Census this ward had a population of 16,099.

</details>

## Q288 — `hotpotqa_5ae1cab7554299492dc91b8a` (revised draft)

> What nationality is the actress who played the role of Sam Sloan's wife Trudy in the sitcom The Single Guy ?

Source answer: American

Gold final answer: American

Question type: `bridge` (source type `bridge`)

Replaces: `hotpotqa_5ae1d5a3554299234fd04319`

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: actress playing Trudy, the wife of Sam Sloan, in The Single Guy | false | Ming-Na Wen | — | [d4s2] | — |
| u2: nationality of {u1} | true | American | u1 | [d8s0] | — |

Evidence:

- `d4s2` The Single Guy [2]: The series also starred Joey Slotnick as Eliot's best friend Sam Sloan, Ming-Na Wen as Sam's wife Trudy and Ernest Borgnine as doorman Manny, throughout its entire run.
- `d8s0` Ming-Na Wen [0]: Ming-Na Wen (; born November 20, 1963) is an American actress.

Notes:

- 替换：Fred Taylor及Corey Dillon均满足条件，答案不唯一。 新题保留原source type，人工核对两条显式事实及答案。

<details><summary>All source context</summary>

- `d1s0` Tom Stade [0]: Tom Stade is a Canadian comedian who currently lives in Edinburgh, Scotland with his wife Trudy and their two children.
- `d1s1` Tom Stade [1]: Stade was encouraged to move from his hometown of Vancouver to the UK in 2001 by his friend and fellow comedian, Craig Campbell.
- `d1s2` Tom Stade [2]: He has a distinctive "drunken Canadian" accent and is known for his appearances at the Edinburgh Festival, as well as appearing on British TV shows such as "Live at the Apollo", "The Comedy Store", "The Live Floor Show", "Stand Up for the Week", and "The World Stands Up".
- `d1s3` Tom Stade [3]: Other appearances include: "Mock the Week", the Birmingham leg of (whilst he lived in Wolverhampton) "Michael McIntyre's Comedy Roadshow", "Dave's One Night Stand", "Lee Mack's All Star Cast", and "Frankie Boyle's Tramadol Nights" (for which he also wrote).
- `d1s4` Tom Stade [4]: In March 2011 and December 2012, he appeared as a guest star on "Soccer AM".
- `d2s0` Adrian Monk [0]: Adrian Monk is a title character and the protagonist of the USA Network television series "Monk", portrayed by Tony Shalhoub.
- `d2s1` Adrian Monk [1]: He is a renowned former homicide detective for the San Francisco Police Department.
- `d2s2` Adrian Monk [2]: Monk has obsessive-compulsive disorder (OCD) and multiple phobias, all of which intensified after the murder of his wife Trudy, resulting in his suspension from the department.
- `d2s3` Adrian Monk [3]: He works as a private police homicide consultant and undergoes therapy with the ultimate goal of overcoming his grief, taking control of his phobias and disorder, and being reinstated as a police detective.
- `d3s0` Alison Brie [0]: Alison Brie Schermerhorn (born December 29, 1982 ) is an American actress and producer.
- `d3s1` Alison Brie [1]: She portrayed Annie Edison in the NBC/Yahoo! sitcom "Community" (2009–2015) and Trudy Campbell in the AMC drama "Mad Men" (2007–2015).
- `d3s2` Alison Brie [2]: Brie currently voices Diane Nguyen on the Netflix animated series "BoJack Horseman" (2014–present) and portrays Ruth Wilder on the Netflix comedy-drama series "GLOW" (2017).
- `d3s3` Alison Brie [3]: She has starred in several films, such as "Scream 4" (2011), "The Five-Year Engagement" (2012), "The Lego Movie" (2014), "Get Hard" (2015), "Sleeping with Other People" (2015), and "How to Be Single" (2016).
- `d4s0` The Single Guy [0]: The Single Guy is an American television sitcom that ran for two seasons on NBC, from September 1995 to April 1997.
- `d4s1` The Single Guy [1]: It stars Jonathan Silverman as struggling New York City writer Jonathan Eliot, and followed several of his close friends (some of whom came and left as the show was re-tooled between seasons).
- `d4s2` The Single Guy [2]: The series also starred Joey Slotnick as Eliot's best friend Sam Sloan, Ming-Na Wen as Sam's wife Trudy and Ernest Borgnine as doorman Manny, throughout its entire run.
- `d4s3` The Single Guy [3]: "The Single Guy" was created by Brad Hall.
- `d5s0` Bobby Fischer Against the World [0]: Bobby Fischer Against the World is a documentary feature film that explores the life of chess Grandmaster and 11th World Champion Bobby Fischer.
- `d5s1` Bobby Fischer Against the World [1]: It incorporates interviews with chess players Anthony Saidy, Larry Evans, Sam Sloan, Susan Polgar, Garry Kasparov, Asa Hoffmann, Friðrik Ólafsson, Lothar Schmid and others.
- `d5s2` Bobby Fischer Against the World [2]: It includes rare archive footage from the World Chess Championship 1972.
- `d6s0` Michelle Butterly [0]: Michelle Butterly (born 5 February 1970 English actress.
- `d6s1` Michelle Butterly [1]: She graduated from the Central School of Speech and Drama.
- `d6s2` Michelle Butterly [2]: She has played Julie Oldroyd in "Soldier Soldier" in 1997, Melanie Dyson in "Casualty" from 1999 to 2001, and she has appeared in "Pie in the Sky", "The Bill", "No Angels", "Midsomer Murders", and "Dangerfield".
- `d6s3` Michelle Butterly [3]: She appeared for two series as Ms Perin in the BBC2 sitcom "Beautiful People", and played Trudy in the fifth series of "Benidorm".
- `d7s0` It's JerryTime! [0]: It's JerryTime!
- `d7s1` It's JerryTime! [1]: is an animated diary of a middle-aged single guy whose life is just a bit harder than it should be.
- `d7s2` It's JerryTime! [2]: Jerry and Orrin Zucker (no relation to Airplane!
- `d7s3` It's JerryTime! [3]: ) began by amusing friends and each other on the Internet with a series of short, animated films made in Orrin's basement, based on the weird things that befall Jerry.
- `d7s4` It's JerryTime! [4]: Orrin Zucker, a 20-year veteran of broadcast design, animates and directs the shorts.
- `d7s5` It's JerryTime! [5]: Jerry Zucker, a comic writer, is the storyteller and composer of the ragtime piano background music.
- `d8s0` Ming-Na Wen [0]: Ming-Na Wen (; born November 20, 1963) is an American actress.
- `d8s1` Ming-Na Wen [1]: (She has been credited with and without her family name "Wen", but most credits since the late 1990s have been without it.
- `d8s2` Ming-Na Wen [2]: She has been known by such variants of her name as Ming-Na, Ming Na, Ming Na Wen and Ming Wen.)
- `d8s3` Ming-Na Wen [3]: She is known for playing the role of Melinda May in the ABC action drama series "Agents of S.H.I.E.L.D." and for voicing Fa Mulan, one of the Disney Princesses, in the films "Mulan" and "Mulan II", the video game "Kingdom Hearts II", and in the Disney animated series "Sofia the First".
- `d8s4` Ming-Na Wen [4]: She is due to reprise her role as Mulan in "".
- `d9s0` Mr. Monk and the End [0]: "Mr. Monk and the End" is the two-part series finale of the USA Network original criminal mystery dramedy television series, "Monk".
- `d9s1` Mr. Monk and the End [1]: It is the fifteenth and sixteenth episodes of the eighth and final season, and is the 124th and 125th episodes in the series overall.
- `d9s2` Mr. Monk and the End [2]: Adrian Monk (Tony Shalhoub) finally discovers his wife Trudy's (Melora Hardin) murderer after twelve years of searching, concluding a seven-year, eight-season long arc.
- `d9s3` Mr. Monk and the End [3]: When "Part 2" aired, it set a series high and a new viewership record for the most watched episode of a regular drama series ever in basic cable with 9.4 million viewers.
- `d9s4` Mr. Monk and the End [4]: Both parts were written by series creator Andy Breckman and directed by Randall Zisk.
- `d10s0` Brad Hall [0]: William Brad Hall (born March 21, 1958) is an American actor, comedian, director and writer.
- `d10s1` Brad Hall [1]: He is best known as a "Saturday Night Live" news anchor on "Saturday Night News" and for creating the sitcoms "The Single Guy" and "Watching Ellie".

</details>

## Q289 — `hotpotqa_5ae222ec5542996483e648ff` (revised draft)

> What production company was co-created by the lead singer of the band Poison?

Source answer: Sheen Michaels Entertainment

Gold final answer: Sheen Michaels Entertainment

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: lead singer of Poison | false | Bret Michaels | — | [d1s1] OR [d3s0] OR [d4s0] OR [d6s0] OR [d7s0] OR [d9s0] OR [d10s1] | — |
| u2: production company co-created by {u1} | true | Sheen Michaels Entertainment | u1 | [d8s0] OR [d9s2] | — |

Evidence:

- `d1s1` Bret Michaels [1]: He gained fame as the lead singer of the glam metal band Poison who have sold over 50 million records worldwide and 15 million records in the United States alone.
- `d3s0` Rock of Love with Bret Michaels (season 1) [0]: Rock of Love with Bret Michaels is a competition-driven reality television series starring Bret Michaels, the lead singer of the band Poison.
- `d4s0` Songs of Life (Bret Michaels album) [0]: Songs of Life is the second solo studio album by Bret Michaels, lead singer of the rock band Poison.
- `d6s0` Ballads, Blues &amp; Stories [0]: Ballads, Blues & Stories is a unique storytellers music CD from Bret Michaels, the lead singer of the rock band Poison.
- `d7s0` A Letter from Death Row (album) [0]: A Letter from Death Row is the debut solo album by Bret Michaels, the lead singer of the rock band Poison.
- `d8s0` In God's Hands (film) [0]: In God's Hands (1998) is a film by Zalman King released through "Sheen Michaels Entertainment" a production company created by actor Charlie Sheen and Bret Michaels.
- `d9s0` A Letter from Death Row (film) [0]: A Letter From Death Row is a 1998 psychological thriller film directed by Marvin Baker and Bret Michaels, lead singer of the hard rock band Poison.
- `d9s2` A Letter from Death Row (film) [2]: The film was released by Sheen Michaels Entertainment, a company created by Bret Michaels and actor Charlie Sheen.
- `d10s1` Rock of Love with Bret Michaels [1]: It stars Bret Michaels, the lead singer from the band Poison.

Notes:

- 补齐主唱身份六条备选及公司创办d9s2；d9文档可独立完成两跳。

<details><summary>All source context</summary>

- `d1s0` Bret Michaels [0]: Bret Michael Sychak (born March 15, 1963), professionally known as Bret Michaels, is an American singer-songwriter and musician.
- `d1s1` Bret Michaels [1]: He gained fame as the lead singer of the glam metal band Poison who have sold over 50 million records worldwide and 15 million records in the United States alone.
- `d1s2` Bret Michaels [2]: The band has also charted ten singles to the Top 40 of the "Billboard" Hot 100, including six Top 10 singles and a number-one single, "Every Rose Has Its Thorn".
- `d2s0` Shut Up, Make Love [0]: "Shut Up, Make Love" is a song by American rock band Poison; released in 2000, it was the first single presented to radio stations from their 2000 "Crack a Smile...and More!
- `d2s1` Shut Up, Make Love [1]: " album.
- `d2s2` Shut Up, Make Love [2]: The song also appears on the second promo single "Be the One" as a B-side.
- `d2s3` Shut Up, Make Love [3]: "Crack a Smile" is Poison's fifth studio album, released on March 14, 2000, and charting at #131 on The Billboard 200.
- `d2s4` Shut Up, Make Love [4]: The song was the first Poison single with lead guitarist Blues Saraceno.
- `d3s0` Rock of Love with Bret Michaels (season 1) [0]: Rock of Love with Bret Michaels is a competition-driven reality television series starring Bret Michaels, the lead singer of the band Poison.
- `d3s1` Rock of Love with Bret Michaels (season 1) [1]: The 12-episode series, which premiered July 15, 2007 on VH1 (a VSPOT online premiere showcased on July 10), was created by Cris Abrego and Mark Cronin (co-founders of the production company 51 Minds).
- `d4s0` Songs of Life (Bret Michaels album) [0]: Songs of Life is the second solo studio album by Bret Michaels, lead singer of the rock band Poison.
- `d4s1` Songs of Life (Bret Michaels album) [1]: The album was released April 22, 2003 and coincides with the same date of his two-year-old daughter Raine's birthday.
- `d4s2` Songs of Life (Bret Michaels album) [2]: The album is written and produced by Bret Michaels, Cliff Calabro and co-produced by Jeremy Rubolino.
- `d4s3` Songs of Life (Bret Michaels album) [3]: The music is inspired by events from Bret Michael's life.
- `d5s0` Stand (Poison song) [0]: "Stand" is a song recorded by American band Poison, written by Richie Kotzen prior to joining the band.
- `d5s1` Stand (Poison song) [1]: It was the 1st single from their 1993 "Native Tongue" album.
- `d5s2` Stand (Poison song) [2]: The song reached number 15 on the Mainstream rock chart, #35 on the top 40 mainstream chart and #50 on the "Billboard" Hot 100.
- `d5s3` Stand (Poison song) [3]: The song also charted at number 25 on the UK Singles chart, it was also the first Poison single and music video to feature lead guitarist Richie Kotzen.
- `d5s4` Stand (Poison song) [4]: The song fuses elements of country rock and gospel music; the album version includes the Los Angeles First A.M.E. Church choir on backing vocals.
- `d6s0` Ballads, Blues &amp; Stories [0]: Ballads, Blues & Stories is a unique storytellers music CD from Bret Michaels, the lead singer of the rock band Poison.
- `d6s1` Ballads, Blues &amp; Stories [1]: Released in 2001 it consists of Bret Michaels' solo music and Poison songs, with a recorded story before each song, about how the songs were created and written.
- `d7s0` A Letter from Death Row (album) [0]: A Letter from Death Row is the debut solo album by Bret Michaels, the lead singer of the rock band Poison.
- `d7s1` A Letter from Death Row (album) [1]: The album was released August 25, 1998, and is a soundtrack to the movie "A Letter from Death Row" which Bret Michaels wrote, directed and starred in.
- `d8s0` In God's Hands (film) [0]: In God's Hands (1998) is a film by Zalman King released through "Sheen Michaels Entertainment" a production company created by actor Charlie Sheen and Bret Michaels.
- `d8s1` In God's Hands (film) [1]: The basic story is of three young surfers on a roller coaster action tour of the globe's most exotic and dangerous surfing spots.
- `d8s2` In God's Hands (film) [2]: They travel to Madagascar, Mexico, Bali and Hawaii seeking the ultimate wave, a 40-foot force of nature that travels at speeds up to 35 miles per hour.
- `d9s0` A Letter from Death Row (film) [0]: A Letter From Death Row is a 1998 psychological thriller film directed by Marvin Baker and Bret Michaels, lead singer of the hard rock band Poison.
- `d9s1` A Letter from Death Row (film) [1]: Bret Michaels also wrote the film and starred in it.
- `d9s2` A Letter from Death Row (film) [2]: The film was released by Sheen Michaels Entertainment, a company created by Bret Michaels and actor Charlie Sheen.
- `d9s3` A Letter from Death Row (film) [3]: The film was produced by Shane Stanley and also stars Martin Sheen, Charlie Sheen, and Kristi Gibson, who was Michaels' girlfriend at the time.
- `d10s0` Rock of Love with Bret Michaels [0]: Rock of Love with Bret Michaels is an American reality television dating game show.
- `d10s1` Rock of Love with Bret Michaels [1]: It stars Bret Michaels, the lead singer from the band Poison.
- `d10s2` Rock of Love with Bret Michaels [2]: The show closely resembles its sister show "Flavor of Love".
- `d10s3` Rock of Love with Bret Michaels [3]: The first season featured 25 women competing to be Michaels' girlfriend.
- `d10s4` Rock of Love with Bret Michaels [4]: Each week, the women face challenges, the winner of which gets to go on a date with Michaels.
- `d10s5` Rock of Love with Bret Michaels [5]: Some of the challenges were based on situations that they might encounter if chosen to be Michaels' girlfriend.
- `d10s6` Rock of Love with Bret Michaels [6]: The first season winner was 24-year-old Jes Rickleff from Naperville, Illinois.
- `d10s7` Rock of Love with Bret Michaels [7]: At the reunion, she revealed that she did not have romantic feelings for Michaels, and that she thought that he should have chosen the runner-up, Heather.

</details>

## Q290 — `hotpotqa_5ae26af3554299492dc91c1c` (revised draft)

> Which building is taller Bertelsmann Building or 432 Park Avenue?

Source answer: 432 Park Avenue

Gold final answer: 432 Park Avenue

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: height of Bertelsmann Building | false | 733 ft | — | [d3s0] | — |
| u2: topped-out height of 432 Park Avenue | false | 1396 ft | — | [d10s1] OR [d9s3] | — |
| u3: Which building is taller Bertelsmann Building or 432 Park Avenue? | true | 432 Park Avenue | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d3s0` Bertelsmann Building [0]: The former Bertelsmann Building, now known as 1540 Broadway, is a 44-story, 733 foot (223 m) office tower in Times Square in Manhattan, New York City, standing at West 45th Street.
- `d9s3` List of tallest buildings in New York City [3]: The second-tallest building in the city is 432 Park Avenue, standing at 1396 ft , and the third-tallest is the 102-story Empire State Building in Midtown Manhattan, which was finished in 1931 and rises to 1250 ft , increased to 1454 ft by its antenna.
- `d10s1` 432 Park Avenue [1]: Originally proposed to be 1300 ft in 2011, the structure topped out at 1396 ft .

Notes:

- 补1396 ft的独立备选，保持建成高度口径。

<details><summary>All source context</summary>

- `d1s0` 245 Park Avenue [0]: 245 Park Avenue (formerly American Tobacco Company Building, American Brands Building and Bear Stearns Building) is a 648-ft (198 m) tall skyscraper in New York City, New York.
- `d1s1` 245 Park Avenue [1]: It was completed in 1967 and has 48 floors (1.7 million square feet).
- `d1s2` 245 Park Avenue [2]: Shreve, Lamb and Harmon designed the building.
- `d1s3` 245 Park Avenue [3]: The Building Owners and Managers Association awarded the 2000/2001 Pinnacle Award to 245 Park Avenue.
- `d1s4` 245 Park Avenue [4]: The site used to be occupied by the second Grand Central Palace exhibition hall, which was demolished in 1964 to make way for 245 Park Avenue.
- `d2s0` 655 Park Avenue [0]: 655 Park Avenue is a Georgian-style co-op residential building on Manhattan's Upper East Side, located on Park Avenue between 67th Street and 68th Street, adjacent to the Park Avenue Armory.
- `d2s1` 655 Park Avenue [1]: It was developed in 1924 by Dwight P. Robinson & Company.
- `d2s2` 655 Park Avenue [2]: The building at 655 Park Avenue was designed by architects James Edwin Ruthven Carpenter, Jr., often referred to by the initials "J.E.R. Carpenter", and Mott B. Schmidt.
- `d2s3` 655 Park Avenue [3]: Carpenter is considered the leading architect for luxury residential high-rise buildings in New York City in the early 1900s, while Schmidt is known for his buildings in the American Georgian Classical style, including Sutton Place and houses for New York City's society figures and business elite.
- `d3s0` Bertelsmann Building [0]: The former Bertelsmann Building, now known as 1540 Broadway, is a 44-story, 733 foot (223 m) office tower in Times Square in Manhattan, New York City, standing at West 45th Street.
- `d3s1` Bertelsmann Building [1]: The building was the North American headquarters of media conglomerate Bertelsmann from 1992 until the company vacated and sold the property, of which they occupied all office-use floors, in 2004.
- `d3s2` Bertelsmann Building [2]: The building housed US satellites of central functions such as Corporate Development, Corporate Communications and the Office of the Chairman and CEO, as well as serving as worldwide headquarters for the Bertelsmann Music Group and Bertelsmann Book Group (what has later taken on the umbrella brand name Random House).
- `d3s3` Bertelsmann Building [3]: Today's office tenants include Viacom, China Central Television, KEMP Technologies, Adobe and Pillsbury Winthrop Shaw Pittman.
- `d3s4` Bertelsmann Building [4]: The building retained the Bertelsmann name and signage facing Broadway until its eventual removal in late 2013.
- `d4s0` Princess Tower [0]: The Princess Tower (Arabic: برج الأميرة‎ ‎ ) is a 101 story, 413.4 m tall residential-only skyscraper located in the Marina district of Dubai, UAE.
- `d4s1` Princess Tower [1]: Princess Tower is currently the second tallest building in Dubai, after the Burj Khalifa, and the 24th tallest building in the world.
- `d4s2` Princess Tower [2]: Princess Tower was the tallest residential building in the world from 2012 to 2015, when it was overtaken by 432 Park Avenue in New York City.
- `d5s0` John Hancock Center [0]: The John Hancock Center is a 100-story, 1,128-foot (343.7 m) supertall skyscraper at 875 North Michigan Avenue, Chicago, Illinois, United States.
- `d5s1` John Hancock Center [1]: It was constructed under the supervision of Skidmore, Owings and Merrill, with chief designer Bruce Graham and structural engineer Fazlur Khan.
- `d5s2` John Hancock Center [2]: When the building topped out on May 6, 1968, it was the second tallest building in the world and the tallest outside of New York City.
- `d5s3` John Hancock Center [3]: It is currently the fourth-tallest building in Chicago and the eighth-tallest in the United States, after One World Trade Center, the Willis Tower, 432 Park Avenue, the Trump Tower Chicago, the Empire State Building, the Bank of America Tower, and the Aon Center.
- `d5s4` John Hancock Center [4]: When measured to the top of its antenna masts, it stands at 1500 ft .
- `d5s5` John Hancock Center [5]: The building is home to offices and restaurants, as well as about 700 condominiums, and contains the third highest residence in the world, after the Burj Khalifa in Dubai and the Trump Tower in Chicago.
- `d5s6` John Hancock Center [6]: The building was named for John Hancock Mutual Life Insurance Company, a developer and original tenant of the building.
- `d6s0` One57 [0]: One57, formerly known as Carnegie 57 and nicknamed "The Billionaire Building", is a 75-story (marketed as 90-story) supertall skyscraper at 157 West 57th Street between Sixth and Seventh Avenues in the Midtown neighborhood of Manhattan, New York City.
- `d6s1` One57 [1]: Upon completion in 2014, it stood at 1,005 ft tall, making it the tallest residential building in the city for a few months until the completion of 432 Park Avenue.
- `d6s2` One57 [2]: The building has 92 condominium units on top of a new Park Hyatt Hotel with 210 rooms, which is set to become the flagship Hyatt property.
- `d7s0` 311 South Wacker Drive [0]: 311 South Wacker Drive in Chicago, USA, is a post-modern 65-story skyscraper completed in 1990.
- `d7s1` 311 South Wacker Drive [1]: At 961 feet (293 m) tall, it is the seventh tallest building in Chicago and the 24th tallest in the United States.
- `d7s2` 311 South Wacker Drive [2]: It was once the tallest reinforced concrete building in the world.
- `d7s3` 311 South Wacker Drive [3]: Until 2015, 311 South Wacker was also the tallest building in the world known only by its street address, when it was replaced by New York's 432 Park Avenue.
- `d8s0` Park Avenue House [0]: The Park Avenue House is a high rise residential building located at 2305 Park Avenue in the Park Avenue Historic District in Downtown Detroit, Michigan.
- `d8s1` Park Avenue House [1]: It was listed on the National Register of Historic Places in 1996.
- `d8s2` Park Avenue House [2]: It should not be confused with the nearby Park Avenue Hotel, which was demolished in 2015.
- `d9s0` List of tallest buildings in New York City [0]: New York City, the most populous city in the United States, is home to over 6486 completed high rise building of at least 35 meters, of which at least 113 completed are taller than 600 ft .
- `d9s1` List of tallest buildings in New York City [1]: The tallest building in New York is One World Trade Center, which rises 1776 ft .
- `d9s2` List of tallest buildings in New York City [2]: The 104-story skyscraper also stands as the tallest building in the United States, the tallest building in the Western Hemisphere, and the sixth-tallest building in the world.
- `d9s3` List of tallest buildings in New York City [3]: The second-tallest building in the city is 432 Park Avenue, standing at 1396 ft , and the third-tallest is the 102-story Empire State Building in Midtown Manhattan, which was finished in 1931 and rises to 1250 ft , increased to 1454 ft by its antenna.
- `d9s4` List of tallest buildings in New York City [4]: It is the fifth-tallest building in the United States and the 25th-tallest building in the world.
- `d10s0` 432 Park Avenue [0]: 432 Park Avenue is a residential skyscraper in New York City that overlooks Central Park.
- `d10s1` 432 Park Avenue [1]: Originally proposed to be 1300 ft in 2011, the structure topped out at 1396 ft .
- `d10s2` 432 Park Avenue [2]: It was developed by CIM Group and features 104 condominium apartments.
- `d10s3` 432 Park Avenue [3]: Construction began in 2012 and was completed on December 23, 2015.

</details>

## Q291 — `hotpotqa_5ae2e73a55429928c4239545` (revised draft)

> What is the nickname of Stephan Lichtsteiner that refers to the character from the 1994 American comedy-drama film based on the novel by Winston Groom?

Source answer: Forrest Gump

Gold final answer: Forrest Gump

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: title character of the 1994 comedy-drama adaptation of a Winston Groom novel | false | Forrest Gump | — | [d10s0, d10s2] OR [d10s0, d2s0] | — |
| u2: nickname of Stephan Lichtsteiner matching {u1} | true | Forrest Gump | u1 | [d9s1] | — |

Evidence:

- `d2s0` Forrest Gump (character) [0]: Forrest Gump is a fictional character who first appears in the 1986 novel by Winston Groom.
- `d9s1` Stephan Lichtsteiner [1]: An attacking right-back or wing-back, he is known for his energetic runs down the right wing, as well as his stamina and athleticism, which earned him the nicknames "Forrest Gump" and "The Swiss Express".
- `d10s0` Forrest Gump [0]: Forrest Gump is a 1994 American comedy-drama film based on the 1986 novel of the same name by Winston Groom.
- `d10s2` Forrest Gump [2]: The story depicts several decades in the life of Forrest Gump, a slow-witted but kind-hearted, good-natured and athletically prodigious man from Alabama, who witnesses, and in some cases influences, some of the defining events of the latter half of the 20th century in the United States; more specifically, the period between Forrest's birth in 1944 and 1982.

Notes:

- 先按电影条件定位角色，再核验球员昵称；补人物条目路径，避免先输出两个候选昵称。

<details><summary>All source context</summary>

- `d1s0` Forrest Gump (novel) [0]: Forrest Gump is a 1986 novel by Winston Groom.
- `d1s1` Forrest Gump (novel) [1]: The title character retells adventures ranging from shrimp boating and ping pong championships, to thinking about his childhood love, as he bumbles his way through American history, with everything from the Vietnam War to college football becoming part of the story.
- `d2s0` Forrest Gump (character) [0]: Forrest Gump is a fictional character who first appears in the 1986 novel by Winston Groom.
- `d2s1` Forrest Gump (character) [1]: Forrest Gump also appeared on screen in the 1994 film of the same name directed by Robert Zemeckis.
- `d2s2` Forrest Gump (character) [2]: Forrest was portrayed as a child by Michael Humphreys and portrayed as an adult by Tom Hanks, who won an Academy Award for the role.
- `d2s3` Forrest Gump (character) [3]: The portrayal of Forrest in the novel is notably different from the portrayal in the film.
- `d2s4` Forrest Gump (character) [4]: He later reappears in the 1995 sequel novel "Gump and Co."
- `d3s0` As Summers Die [0]: As Summers Die is a 1986 American made-for-television drama film starring Scott Glenn, Jamie Lee Curtis, Bette Davis and Beah Richards, directed by Jean-Claude Tramont.
- `d3s1` As Summers Die [1]: The film is loosely based on Winston Groom's 1980 novel of the same name about greed, bigotry and justice in late 1950s segregationist southern Louisiana.
- `d3s2` As Summers Die [2]: It was filmed in Valdosta, Georgia and premiered on HBO on May 18, 1986.
- `d3s3` As Summers Die [3]: It was later released on VHS.
- `d4s0` My Girl 2 [0]: My Girl 2 is a 1994 American comedy-drama film and a sequel to "My Girl" (1991) starring Anna Chlumsky, Dan Aykroyd, Christine Ebersole, Jamie Lee Curtis, Richard Masur, and Austin O'Brien.
- `d4s1` My Girl 2 [1]: A book based on the script was written by Patricia Hermes in 1994.
- `d5s0` A Simple Twist of Fate [0]: A Simple Twist of Fate is a 1994 American comedy-drama film directed by Gillies MacKinnon.
- `d5s1` A Simple Twist of Fate [1]: The screenplay by Steve Martin is loosely based on the 1861 novel "Silas Marner" by George Eliot.
- `d6s0` Nobody's Fool (1994 film) [0]: Nobody's Fool is a 1994 American comedy-drama film based on the 1993 novel of the same name by Richard Russo.
- `d6s1` Nobody's Fool (1994 film) [1]: The film was written for the screen and directed by Robert Benton and stars Paul Newman, Jessica Tandy, Bruce Willis, Melanie Griffith, Dylan Walsh, Pruitt Taylor Vince, Gene Saks, Josef Sommer, Philip Seymour Hoffman, and Philip Bosco.
- `d6s2` Nobody's Fool (1994 film) [2]: It was Paramount's final production under its Paramount Communications ownership and Jessica Tandy's final produced film before her death on September 11, 1994.
- `d7s0` Gump and Co. [0]: Gump & Co. (or Forrest Gump and Co.) is a 1995 novel by Winston Groom.
- `d7s1` Gump and Co. [1]: It is the sequel to his novel "Forrest Gump" (1986), and the Academy Award-winning film of the same name released in 1994, with Tom Hanks.
- `d7s2` Gump and Co. [2]: It was written to chronicle Forrest's life throughout the 1980s.
- `d8s0` List of accolades received by Forrest Gump [0]: "Forrest Gump" is a 1994 epic romantic comedy-drama film based on the 1986 novel of the same name by Winston Groom.
- `d8s1` List of accolades received by Forrest Gump [1]: The film premiered in Los Angeles, California on June 23, 1994 and was released into the United States and Canada on July 6, 1994, opening into 1,595 domestic theaters and earning $24,450,602 on its first weekend.
- `d8s2` List of accolades received by Forrest Gump [2]: "Forrest Gump" grossed $677 million and was at its time the fourth highest grossing film of all time (behind only "E.T. the Extra-Terrestrial", "Star Wars IV: A New Hope", and "Jurassic Park").
- `d8s3` List of accolades received by Forrest Gump [3]: Despite its praise, it has only a 72% approval rating on Rotten Tomatoes.
- `d9s0` Stephan Lichtsteiner [0]: Stephan Lichtsteiner (born 16 January 1984) is a Swiss professional footballer who plays for Italian club Juventus and the Switzerland national team.
- `d9s1` Stephan Lichtsteiner [1]: An attacking right-back or wing-back, he is known for his energetic runs down the right wing, as well as his stamina and athleticism, which earned him the nicknames "Forrest Gump" and "The Swiss Express".
- `d10s0` Forrest Gump [0]: Forrest Gump is a 1994 American comedy-drama film based on the 1986 novel of the same name by Winston Groom.
- `d10s1` Forrest Gump [1]: The film was directed by Robert Zemeckis and stars Tom Hanks, Robin Wright, Gary Sinise, Mykelti Williamson, and Sally Field.
- `d10s2` Forrest Gump [2]: The story depicts several decades in the life of Forrest Gump, a slow-witted but kind-hearted, good-natured and athletically prodigious man from Alabama, who witnesses, and in some cases influences, some of the defining events of the latter half of the 20th century in the United States; more specifically, the period between Forrest's birth in 1944 and 1982.
- `d10s3` Forrest Gump [3]: The film differs substantially from Winston Groom's novel, including Gump's personality and several events that were depicted.

</details>

## Q292 — `hotpotqa_5a78b59d554299148911f958` (revised draft)

> Which musician was born first, John Tardy or Tom Barman?

Source answer: John Tardy

Gold final answer: John Tardy

Question type: `comparison` (source type `comparison`)

Replaces: `hotpotqa_5ae31bbd55429928c42395fc`

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: birth year of John Tardy | false | 1968 | — | [d9s0] | — |
| u2: birth year of Tom Barman | false | 1972 | — | [d8s0] | — |
| u3: Which musician was born first, John Tardy or Tom Barman? | true | John Tardy | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d8s0` Tom Barman [0]: Thomas Andrew Barman, normally known as Tom Barman (born 1 January 1972), is a Belgian musician and film director.
- `d9s0` John Tardy [0]: John Tardy (born March 15, 1968) is an American vocalist best known for his work with the death metal band Obituary and Tardy Brothers.

Notes:

- 替换：上下文只给London；当前规则未允许city→country常识映射。 新题保留原source type，人工核对两条显式事实及答案。

<details><summary>All source context</summary>

- `d1s0` 0110 [0]: The 0110 concerts, held on October 1, 2006 in Antwerp, Brussels, Charleroi and Ghent, were organised by dEUS frontman Tom Barman, Arno Hintjens and Frederik Sioen to promote tolerance in Belgian society, and "against Vlaams Belang, extremism and gratuitous violence".
- `d2s0` Zanna [0]: "Zanna" is a song originally written and performed by Belgian musician Luc Van Acker and American singer Anna Domino in 1984.
- `d2s1` Zanna [1]: A successful cover was performed by Belgian musician and songwriter Selah Sue, Tom Barman and The Subs.
- `d2s2` Zanna [2]: This version was released on 25 November 2011 as a digital download in Belgium.
- `d2s3` Zanna [3]: It is the theme song for the charity event "Music for life 2011".
- `d2s4` Zanna [4]: In 2012 the song made a comeback due to the success it had with "Music for Life".
- `d2s5` Zanna [5]: Luc Van Acker performed at the Suicker Rock festival with a 14-year-old girl who was named after the song "Zanna".
- `d2s6` Zanna [6]: Luc Van Acker has previously met the family in 1998 after having made a remix using the sound of her heartbeat in vitro.
- `d2s7` Zanna [7]: However, in 2012, music brought the two back together after having found Zanna Ramaekers 's A cappella cover of "Zanna" on YouTube.
- `d2s8` Zanna [8]: They performed on the stage at SuickerRock and at a Belgian national TV show VillaVanthilt.
- `d3s0` Any Way the Wind Blows (film) [0]: Any Way the Wind Blows is a 2003 film by dEUS' singer-songwriter-director Tom Barman.
- `d4s0` Magnus (band) [0]: Magnus is a Belgian joint dance project of Tom Barman (from the rock band dEUS) and CJ Bolland.
- `d4s1` Magnus (band) [1]: Magnus' debut album, "The Body Gave You Everything", was released on March 29, 2004.
- `d4s2` Magnus (band) [2]: Two of its tracks, "Summer's Here" and "Jumpneedle", were released as singles.
- `d5s0` Jacque Alexander Tardy [0]: Jacque Alexander Tardy (1767 – June 15, 1827) better known as "Tardy the Pirate", (a.k.a. John Tardy or John Late) was an unsuccessful and atypical pirate who usually poisoned his victims.
- `d6s0` Obituary (band) [0]: Obituary is an American death metal band formed in October 1984 in Tampa, Florida.
- `d6s1` Obituary (band) [1]: Initially called Executioner, the band changed their name to Xecutioner in 1986 to avoid confusion with the thrash metal band Executioner from Boston, and then changed their name once again to Obituary in 1988.
- `d6s2` Obituary (band) [2]: The band's current lineup consists of vocalist John Tardy, lead guitarist Kenny Andrews, rhythm guitarist Trevor Peres, bassist Terry Butler, and drummer Donald Tardy.
- `d6s3` Obituary (band) [3]: Obituary has gone through several lineup changes, with Peres and the Tardy brothers being the only constant members.
- `d6s4` Obituary (band) [4]: The band was a fundamental act in the development of death metal music, and is one of the most successful death metal bands of all time.
- `d6s5` Obituary (band) [5]: To date, Obituary has released ten studio albums, and with the exception of their 1997–2003 split, they continue to perform live around the world.
- `d7s0` Deus (band) [0]: Deus (styled as dEUS) is a rock band based in Antwerp, Belgium, whose only continuous members up to the present day are Tom Barman (vocals, guitars) and Klaas Janzoons (keyboards, violin).
- `d7s1` Deus (band) [1]: The rest of the band's line-up currently consists of drummer Stéphane Misseghers, bassist Alan Gevaert and guitarist/backing vocalist Mauro Pawlowski.
- `d8s0` Tom Barman [0]: Thomas Andrew Barman, normally known as Tom Barman (born 1 January 1972), is a Belgian musician and film director.
- `d9s0` John Tardy [0]: John Tardy (born March 15, 1968) is an American vocalist best known for his work with the death metal band Obituary and Tardy Brothers.
- `d9s1` John Tardy [1]: He is the brother of Donald Tardy who is the drummer of Obituary.
- `d10s0` Donald Tardy [0]: Donald 'DT' Tardy (born January 28, 1970) is the drummer of death metal band Obituary and the brother of John Tardy, who is the lead singer of the band.
- `d10s1` Donald Tardy [1]: Besides Obituary, they have a band called Tardy Brothers, where, as primary songwriter and engineer, Donald also plays guitar and bass, as well as drums.
- `d10s2` Donald Tardy [2]: Donald also played drums for Andrew W.K on the album I Get Wet and was Andrew W.K.'s first touring drummer who also assisted with assembling the original Andrew W.K. lineup.

</details>

## Q293 — `hotpotqa_5ae361dc5542992f92d822aa` (revised draft)

> The Facts Behind the Helsinki Roccamatios was published by the creator of the award-winning fantasy adventure novel that was published in what year?

Source answer: 2001

Gold final answer: 2001

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: author of The Facts Behind the Helsinki Roccamatios | false | Yann Martel | — | [d1s0] | — |
| u2: award-winning fantasy adventure novel by {u1} | false | Life of Pi | u1 | [d1s1, d9s0] | — |
| u3: publication year of {u2} | true | 2001 | u2 | [d9s0] | — |

Evidence:

- `d1s0` The Facts Behind the Helsinki Roccamatios [0]: The Facts Behind the Helsinki Roccamatios and Other Stories is a book of short stories by Canadian author Yann Martel.
- `d1s1` The Facts Behind the Helsinki Roccamatios [1]: First published as a paperback by Knopf Canada in the spring of 1993, it received little attention outside Canada until 2004, after Martel's award-winning "Life of Pi" gained worldwide popularity and people became interested in the author's work.
- `d9s0` Life of Pi [0]: Life of Pi is a Canadian fantasy adventure novel by Yann Martel published in 2001.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` The Facts Behind the Helsinki Roccamatios [0]: The Facts Behind the Helsinki Roccamatios and Other Stories is a book of short stories by Canadian author Yann Martel.
- `d1s1` The Facts Behind the Helsinki Roccamatios [1]: First published as a paperback by Knopf Canada in the spring of 1993, it received little attention outside Canada until 2004, after Martel's award-winning "Life of Pi" gained worldwide popularity and people became interested in the author's work.
- `d2s0` Silvana De Mari [0]: Silvana De Mari is an Italian doctor and children's writer known in the English-speaking world for "The Last Dragon", an award-winning fantasy novel published in English in 2006.
- `d2s1` Silvana De Mari [1]: As of 2014 it remains the only one of her many books to be translated into English.
- `d3s0` Watership Down [0]: Watership Down is a fantasy adventure novel by English author Richard Adams, published by Rex Collings Ltd of London in 1972.
- `d3s1` Watership Down [1]: Set in southern England, the story features a small group of rabbits.
- `d3s2` Watership Down [2]: Although they live in their natural environment, they are anthropomorphised, possessing their own culture, language, proverbs, poetry, and mythology.
- `d3s3` Watership Down [3]: Evoking epic themes, the novel follows the rabbits as they escape the destruction of their warren and seek a place to establish a new home, encountering perils and temptations along the way.
- `d4s0` Agone [0]: Agone is an epic fantasy roleplaying game based on novels by award-winning fantasy writer Mathieu Gaborit.
- `d4s1` Agone [1]: "Agone" is set in the land of Harmundia – also known as the Twilight Realms.
- `d4s2` Agone [2]: The game was published in French starting in 1999 by the now-defunct company Multisim, which also translated five books into English starting in 2001.
- `d4s3` Agone [3]: There are over 30 books and supplements for the game published in French.
- `d5s0` That Hell-Bound Train [0]: "That Hell-Bound Train" is an award-winning fantasy short story by American writer Robert Bloch.
- `d5s1` That Hell-Bound Train [1]: It was originally published in "The Magazine of Fantasy & Science Fiction" in September 1958.
- `d6s0` The Jade Trilogy [0]: The Jade Trilogy is a set of three fantasy novels written by Japanese award-winning fantasy writer Noriko Ogiwara.
- `d6s1` The Jade Trilogy [1]: The trilogy consists of the original novel and its two sequels.
- `d7s0` The Giant Under The Snow [0]: The Giant Under The Snow is a children's fantasy adventure novel by John Gordon.
- `d7s1` The Giant Under The Snow [1]: First published in 1968 the story tells the tale of three school friends who discover an ancient treasure and become embroiled in the final act of an epic battle of good against evil.
- `d7s2` The Giant Under The Snow [2]: It is John Gordon's début novel and has been published in at least four languages.
- `d8s0` Sofia Samatar [0]: Sofia Samatar (born October 24, 1971) is a Somali American educator, poet and writer.
- `d8s1` Sofia Samatar [1]: She is an Assistant Professor of English at James Madison University, and serves as a nonfiction and poetry editor for "Interfictions: A Journal of Interstitial Arts".
- `d8s2` Sofia Samatar [2]: In 2013, she published the award-winning fantasy novel "A Stranger in Olondria".
- `d9s0` Life of Pi [0]: Life of Pi is a Canadian fantasy adventure novel by Yann Martel published in 2001.
- `d9s1` Life of Pi [1]: The protagonist is Piscine Molitor "Pi" Patel, an Indian boy from Pondicherry who explores issues of spirituality and practicality from an early age.
- `d9s2` Life of Pi [2]: He survives 227 days after a shipwreck while stranded on a lifeboat in the Pacific Ocean with a Bengal tiger named Richard Parker.
- `d10s0` The Serpent's Shadow (Riordan novel) [0]: The Serpent's Shadow is a 2012 fantasy adventure novel based on Egyptian mythology written by American author Rick Riordan.
- `d10s1` The Serpent's Shadow (Riordan novel) [1]: It is the third and final novel in "The Kane Chronicles" series.
- `d10s2` The Serpent's Shadow (Riordan novel) [2]: It was published by Disney Hyperion on May 1, 2012.

</details>

## Q294 — `hotpotqa_5ae48aff5542996836b02cce` (revised draft)

> When was George Harrison's second single from his album, that was made with rising conflicts with Warner Bros., released in the United States? 

Source answer: 20 July 1981

Gold final answer: 20 July 1981

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: Harrison album made during conflicts with Warner Bros. Records | false | Somewhere in England | — | [d7s0, d7s2, d7s3] | — |
| u2: second single from {u1} | false | Teardrops | u1 | [d5s1] | — |
| u3: U.S. release date of {u2} | true | 20 July 1981 | u2 | [d5s0] | — |

Evidence:

- `d5s0` Teardrops (George Harrison song) [0]: "Teardrops" is a single by George Harrison, released on 20 July 1981 in the United States and 31 July in the UK.
- `d5s1` Teardrops (George Harrison song) [1]: It was the second single from the album "Somewhere in England" and reached number 51 on the US "Billboard" Top Tracks chart and number 102 on the "Billboard" Bubbling Under the Hot 100 chart.
- `d7s0` Somewhere in England [0]: Somewhere in England is the ninth studio album by George Harrison, released in 1981.
- `d7s2` Somewhere in England [2]: The album's making was a long one, during which conflicts with Warner Bros.
- `d7s3` Somewhere in England [3]: Records arose.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Learning How to Love You [0]: "Learning How to Love You" is a song by English musician George Harrison, released in 1976 as the closing track of his debut album on his Dark Horse record label, "Thirty Three & 1/3".
- `d1s1` Learning How to Love You [1]: Harrison wrote the song for Herb Alpert, sometime singer and co-head of A&M Records, which at the time was the worldwide distributor for Dark Horse.
- `d1s2` Learning How to Love You [2]: Although the relationship with A&M soured due to Harrison's failure to deliver "Thirty Three & 1/3" on schedule, resulting in litigation and a new distribution deal with Warner Bros.
- `d1s3` Learning How to Love You [3]: Records, Harrison still dedicated the song to Alpert in the album's liner notes.
- `d2s0` Love Comes to Everyone [0]: "Love Comes to Everyone" is a song by English musician George Harrison that was released as the opening track of his 1979 album "George Harrison".
- `d2s1` Love Comes to Everyone [1]: It was also issued as the second single off the album.
- `d2s2` Love Comes to Everyone [2]: The recording contains musical contributions from Steve Winwood and Eric Clapton.
- `d3s0` Thirty Three &amp; 1/3 [0]: Thirty Three & ⅓ (stylised as Thirty Three & 1/ on the album cover) is the seventh studio album by English musician George Harrison, released in November 1976.
- `d3s1` Thirty Three &amp; 1/3 [1]: It was Harrison's first album release on his Dark Horse record label, the worldwide distribution for which changed from A&M Records to Warner Bros. as a result of his late delivery of the album's master tapes.
- `d3s2` Thirty Three &amp; 1/3 [2]: Among other misfortunes affecting its creation, Harrison suffered hepatitis midway through recording, and the copyright infringement suit regarding his 1970–71 hit song "My Sweet Lord" was decided in favour of the plaintiff, Bright Tunes Music.
- `d3s3` Thirty Three &amp; 1/3 [3]: The album contains the hit singles "This Song" – Harrison's satire on that court case and the notion of plagiarism in pop music – and "Crackerbox Palace".
- `d3s4` Thirty Three &amp; 1/3 [4]: Despite the problems associated with the album, many music critics recognised "Thirty Three & ⅓" as a return to form for Harrison after his poorly received work during 1974–75, and considered it his strongest collection of songs since 1970's acclaimed "All Things Must Pass".
- `d4s0` Dark Horse Records [0]: Dark Horse Records is a record label founded by former Beatle George Harrison in 1974.
- `d4s1` Dark Horse Records [1]: The label's formation coincided with the winding down of the Beatles' Apple Records and allowed Harrison to continue supporting other artists' projects while maintaining his solo career.
- `d4s2` Dark Horse Records [2]: The initial signings were Indian musician Ravi Shankar and Splinter, the last of whom provided the label with its only significant commercial success until Harrison signed with Dark Horse in 1976.
- `d4s3` Dark Horse Records [3]: The label was distributed internationally by A&M Records for the first two years of its operation.
- `d4s4` Dark Horse Records [4]: Following a highly publicised split with A&M, Harrison and Dark Horse formed a long-term partnership with Warner Bros.
- `d4s5` Dark Horse Records [5]: Records that lasted until the expiration of his contract in 1994.
- `d5s0` Teardrops (George Harrison song) [0]: "Teardrops" is a single by George Harrison, released on 20 July 1981 in the United States and 31 July in the UK.
- `d5s1` Teardrops (George Harrison song) [1]: It was the second single from the album "Somewhere in England" and reached number 51 on the US "Billboard" Top Tracks chart and number 102 on the "Billboard" Bubbling Under the Hot 100 chart.
- `d5s2` Teardrops (George Harrison song) [2]: In Japan, it was released on 25 September.
- `d6s0` Soft Touch [0]: "Soft Touch" is a song by English musician George Harrison from his 1979 album "George Harrison".
- `d6s1` Soft Touch [1]: It was also issued as the B-side of the album's lead single, "Blow Away", apart from in North America, where it was the B-side of the second single, "Love Comes to Everyone".
- `d6s2` Soft Touch [2]: Harrison wrote the song while in the Virgin Islands with his future wife, Olivia Arias, shortly before recording his 1976 album "Thirty Three & 1/3".
- `d6s3` Soft Touch [3]: The song is a love song in which Harrison also conveys his wonder at the idyllic island setting.
- `d7s0` Somewhere in England [0]: Somewhere in England is the ninth studio album by George Harrison, released in 1981.
- `d7s1` Somewhere in England [1]: The album was recorded as Harrison was becoming increasingly frustrated with the music industry.
- `d7s2` Somewhere in England [2]: The album's making was a long one, during which conflicts with Warner Bros.
- `d7s3` Somewhere in England [3]: Records arose.
- `d7s4` Somewhere in England [4]: "Somewhere in England" was the first Harrison album to be released after the death of his former Beatles bandmate John Lennon; the lyrics of its first single, "All Those Years Ago", pay tribute to Lennon.
- `d8s0` Best of Dark Horse 1976–1989 [0]: Best of Dark Horse 1976–1989 is a compilation album by English musician George Harrison, released in October 1989.
- `d8s1` Best of Dark Horse 1976–1989 [1]: His second compilation, after the Capitol/EMI collection "The Best of George Harrison" (1976), it contains songs from Harrison's releases on his Dark Horse record label between 1976 and 1987.
- `d8s2` Best of Dark Horse 1976–1989 [2]: The album also includes a 1989 single, "Cheer Down", which was Harrison's contribution to the soundtrack of the film "Lethal Weapon 2", and two tracks recorded specifically for the collection: "Poor Little Girl" and "Cockamamie Business".
- `d8s3` Best of Dark Horse 1976–1989 [3]: Despite the popularity of Harrison's work over this period – both as a solo artist with his "Cloud Nine" album (1987), and as a member of the Traveling Wilburys – the compilation failed to achieve commercial success.
- `d9s0` What Is Life [0]: "What Is Life" is a song by the English musician George Harrison, released on his 1970 triple album "All Things Must Pass".
- `d9s1` What Is Life [1]: In many countries, it was issued as the second single from the album, in February 1971, becoming a top-ten hit in the United States, Canada and elsewhere, and topping singles charts in Australia and Switzerland.
- `d9s2` What Is Life [2]: In the United Kingdom, "What Is Life" appeared as the B-side to "My Sweet Lord", which was the best-selling single there of 1971.
- `d9s3` What Is Life [3]: Harrison's backing musicians on the song include Eric Clapton and the entire Delaney & Bonnie Friends band, with whom he had toured during the final months of the Beatles.
- `d9s4` What Is Life [4]: Harrison co-produced the recording with Phil Spector, whose Wall of Sound production also employed a prominent string arrangement by John Barham and multiple acoustic rhythm guitars, played by Harrison's fellow Apple Records signings Badfinger.
- `d10s0` When We Was Fab [0]: "When We Was Fab" is a song by English musician George Harrison, which he released on his 1987 album "Cloud Nine".
- `d10s1` When We Was Fab [1]: It was also issued as the second single from the album, in January 1988.
- `d10s2` When We Was Fab [2]: The lyrics serve as a nostalgic reflection by Harrison on the days of Beatlemania during the 1960s, when the Beatles were first referred to as "the Fab Four".
- `d10s3` When We Was Fab [3]: Harrison co-wrote the song with Jeff Lynne, who also co-produced the track.
- `d10s4` When We Was Fab [4]: The recording references the psychedelic sound that the Beatles had helped popularise in 1967, through its use of sitar, cello, and backwards-relayed effects.
- `d10s5` When We Was Fab [5]: Harrison's former Beatles bandmate Ringo Starr is among the other musicians on the track.
- `d10s6` When We Was Fab [6]: The single was accompanied by an innovative music video, directed by the partnership of Kevin Godley and Lol Creme.
- `d10s7` When We Was Fab [7]: One of Harrison's most popular songs, "When We Was Fab" has appeared on the compilations "Best of Dark Horse 1976–1989" (1989) and "" (2009).

</details>

## Q295 — `hotpotqa_5a77431355429972597f14de` (revised draft)

> Who is older, Rohan Bopanna or Sherwood Stewart?

Source answer: Sherwood Stewart

Gold final answer: Sherwood Stewart

Question type: `comparison` (source type `comparison`)

Replaces: `hotpotqa_5ae4ebeb55429908b63264bb`

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: birth year of Rohan Bopanna | false | 1980 | — | [d7s0] | — |
| u2: birth year of Sherwood Stewart | false | 1946 | — | [d5s0] | — |
| u3: Who is older, Rohan Bopanna or Sherwood Stewart? | true | Sherwood Stewart | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d5s0` Sherwood Stewart [0]: Sherwood Stewart (born June 6, 1946, in Goose Creek, Texas, United States) played amateur and professional tennis in the 1970s and 1980s.
- `d7s0` Rohan Bopanna [0]: Rohan Bopanna (born 4 March 1980) is an Indian professional tennis player.

Notes:

- 替换：district与province层级不一致，且没有可用的行政层级推理规则。 新题保留原source type，人工核对两条显式事实及答案。

<details><summary>All source context</summary>

- `d1s0` 2016 MercedesCup – Doubles [0]: Rohan Bopanna and Florin Mergea were the defending champions, but Bopanna chose to compete in s'Hertogenbosch instead.
- `d1s1` 2016 MercedesCup – Doubles [1]: Mergea played alongside Horia Tecău, but lost in the semifinals to Marcus Daniell and Artem Sitak.
- `d2s0` 2009 LA Tennis Open – Doubles [0]: Rohan Bopanna and Eric Butorac were the defending champions, but Bopanna did not participate that year.
- `d2s1` 2009 LA Tennis Open – Doubles [1]: <BR>Butorac partnered with Scott Lipsky, but lost in the first round to Denis Istomin and Leonardo Mayer.
- `d2s2` 2009 LA Tennis Open – Doubles [2]: <BR>Bob Bryan and Mike Bryan won in the final 6–4, 7–6 against Benjamin Becker and Frank Moser.
- `d3s0` 2012 If Stockholm Open – Doubles [0]: Rohan Bopanna and Aisam-ul-Haq Qureshi were the defending champions but Bopanna decided not to participate.
- `d3s1` 2012 If Stockholm Open – Doubles [1]: <br>
- `d4s0` 2012 Gerry Weber Open – Doubles [0]: Rohan Bopanna and Aisam-ul-Haq Qureshi were the defending champions but Bopanna decided not to participate.
- `d4s1` 2012 Gerry Weber Open – Doubles [1]: <br>
- `d5s0` Sherwood Stewart [0]: Sherwood Stewart (born June 6, 1946, in Goose Creek, Texas, United States) played amateur and professional tennis in the 1970s and 1980s.
- `d5s1` Sherwood Stewart [1]: Stewart was ranked as high as No. 60 in the world in singles on the ATP Rankings on December 31, 1978, and No. 4 in doubles on January 3, 1983.
- `d6s0` 2014 Open 13 – Doubles [0]: Rohan Bopanna and Colin Fleming were the defending champions, but Bopanna chose not to participate.
- `d6s1` 2014 Open 13 – Doubles [1]: Fleming played alongside Ross Hutchins, but lost in the quarterfinals to Marin Draganja and Mate Pavić.
- `d6s2` 2014 Open 13 – Doubles [2]: <br>
- `d7s0` Rohan Bopanna [0]: Rohan Bopanna (born 4 March 1980) is an Indian professional tennis player.
- `d7s1` Rohan Bopanna [1]: His singles career high ranking was World No. 213 in 2007 and his career high ranking in doubles was World No. 3 on 22 July 2013.
- `d7s2` Rohan Bopanna [2]: Recently, most of his appearances in professional tournaments have been in doubles matches.
- `d7s3` Rohan Bopanna [3]: He is a member of the Indian Davis Cup team since 2002.
- `d7s4` Rohan Bopanna [4]: In 2010, he finished as a runner-up in doubles at the US Open, partnering with Aisam-ul-Haq Qureshi.
- `d7s5` Rohan Bopanna [5]: He won the 2017 French Open - Mixed Doubles title with Gabriela Dabrowski of Canada becoming the fourth Indian player to win a Grand Slam title.
- `d8s0` 2012 Western &amp; Southern Open – Men's Doubles [0]: Mahesh Bhupathi and Leander Paes were the defending champions.
- `d8s1` 2012 Western &amp; Southern Open – Men's Doubles [1]: However, they chose not to play together.
- `d8s2` 2012 Western &amp; Southern Open – Men's Doubles [2]: Bhupathi played with Rohan Bopanna and Paes played with Radek Štěpánek
- `d9s0` 2013 BNP Paribas Masters – Doubles [0]: Mahesh Bhupathi and Rohan Bopanna were the defending champions, but Bhupathi decided not to participate.
- `d9s1` 2013 BNP Paribas Masters – Doubles [1]: Bopanna played alongside Édouard Roger-Vasselin.
- `d10s0` 2016 Dubai Tennis Championships – Men's Doubles [0]: Rohan Bopanna and Daniel Nestor were the defending champions, but chose not to compete together.
- `d10s1` 2016 Dubai Tennis Championships – Men's Doubles [1]: Bopanna played alongside Florin Mergea, but lost in the first round to Nestor and Radek Štepánek.
- `d10s2` 2016 Dubai Tennis Championships – Men's Doubles [2]: Nestor and Štepánek lost in the quarterfinals to Łukasz Kubot and Marcin Matkowski.
- `d10s3` 2016 Dubai Tennis Championships – Men's Doubles [3]: <br>

</details>

## Q296 — `hotpotqa_5ae5072e55429960a22e0246` (revised draft)

> Who is the current drummer of the band who did the song "What Lovers Do"?

Source answer: Matt Flynn

Gold final answer: Matt Flynn

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: band performing What Lovers Do | false | Maroon 5 | — | [d4s0] | — |
| u2: drummer of {u1} in the source lineup | true | Matt Flynn | u1 | [d1s1] | — |

Evidence:

- `d1s1` Maroon 5 [1]: It currently consists of lead vocalist Adam Levine, keyboardist and rhythm guitarist Jesse Carmichael, bassist Mickey Madden, lead guitarist James Valentine, drummer Matt Flynn and keyboardist PJ Morton.
- `d4s0` What Lovers Do [0]: "What Lovers Do" is a song by American pop rock band Maroon 5 featuring American R&B singer Sza.

Notes:

- Current refers to the source lineup, not today.
- 复核后保留原标注；原note为说明或未发现需要修改的证据/依赖问题。

<details><summary>All source context</summary>

- `d1s0` Maroon 5 [0]: Maroon 5 is an American pop rock band that originated in Los Angeles, California.
- `d1s1` Maroon 5 [1]: It currently consists of lead vocalist Adam Levine, keyboardist and rhythm guitarist Jesse Carmichael, bassist Mickey Madden, lead guitarist James Valentine, drummer Matt Flynn and keyboardist PJ Morton.
- `d2s0` Timothy &quot;Yogi&quot; Watts [0]: Timothy "Yogi" Watts is second and current drummer for the Christian Metal band, Demon Hunter.
- `d2s1` Timothy &quot;Yogi&quot; Watts [1]: He was the fourth drummer for The Showdown, original drummer for The Lonely Hearts (originally named Holland), and fill-in drummer for Throwdown as well as The Becoming.
- `d3s0` Mark Castillo [0]: Mark Castillo, (born October 10, 1980) is an American musician.
- `d3s1` Mark Castillo [1]: He is a former drummer of the deathcore band Emmure, a former drummer of the hard rock band Crossfade, a former drummer of the progressive metal band Between the Buried and Me, and a founding member and current drummer of American metalcore band Bury Your Dead.
- `d4s0` What Lovers Do [0]: "What Lovers Do" is a song by American pop rock band Maroon 5 featuring American R&B singer Sza.
- `d4s1` What Lovers Do [1]: It was released on August 30, 2017, as the third single from the band's upcoming sixth studio album (2017).
- `d4s2` What Lovers Do [2]: The song contains an interpolation of the 2016 song "Sexual" by Neiked featuring Dyo, therefore Victor Rådström, Dyo and Elina Stridh are credited as songwriters.
- `d5s0` 4 Tune Kookies [0]: 4 Tune Kookies is an Indian classic-rock band formed about thirty-five years ago (as ‘People’).
- `d5s1` 4 Tune Kookies [1]: The band was started in the 1970s when the band culture was fairly unknown in India.
- `d5s2` 4 Tune Kookies [2]: The band comprises Babu(Saiprasad)Choudhary - (lead guitarist), Hosi Nanji (bass guitarist), Ranjit Barot (former drummer), Derick Gomes (current drummer) and Ronnie Desai (vocalist, rhythm guitarist and song writer)
- `d6s0` Raimund Marasigan [0]: Raimund Emmanuel Parcon Marasigan, (born May 22, 1971) or simply known as Raimund Marasigan, is a Rock musician and record producer in the Philippines.
- `d6s1` Raimund Marasigan [1]: Often, his first name is misspelled as "Raymond", "Raymund", "Raimond" and other variants.
- `d6s2` Raimund Marasigan [2]: The breadth of his projects has made him one of the most well-respected mainstays of the Philippine rock band scene.
- `d6s3` Raimund Marasigan [3]: He was the drummer, vocalist and lyricist alongside bandmate Ely Buendia of The Eraserheads, and the current keyboard/synths player for Pedicab, former rhythm guitarist and now frontman of Sandwich, current drummer of Cambio, vocalist of Project 1 and the man behind Squid 9.
- `d6s4` Raimund Marasigan [4]: Currently, he holds bass for his newest band, Gaijin.
- `d6s5` Raimund Marasigan [5]: Aside from writing songs and being a musician, he is also a record producer, voice actor, TV host and product endorser.
- `d7s0` Peter Morén (drummer) [0]: Peter Morén (born in Gävle, Sweden) is the current drummer of the bands Tad Morose, Steel Attack and Inmoria.
- `d7s1` Peter Morén (drummer) [1]: Peter is perhaps most known as being the drummer for the metal band Tad Morose.
- `d7s2` Peter Morén (drummer) [2]: In the summer of 1994 that band asked Peter to join, and he did.
- `d7s3` Peter Morén (drummer) [3]: Therefore he left his at that time current band called Bedtime Circus, which pretty early after that was disbanded.
- `d7s4` Peter Morén (drummer) [4]: Peter's first recording with Tad Morose was with their album "Sender of Thoughts" in 1994, and he has since then been the band's drummer.
- `d8s0` Kent Stax [0]: Kent Stax is the original and current drummer of the DC hardcore punk band Scream, considered, with perhaps the exception of Minor Threat (both of these bands recorded on the now famous underground Dischord Records label), one of the most influential and successful hardcore punk band to emerge from the music movement which thrived during the 1980s.
- `d8s1` Kent Stax [1]: Along with brothers Franz and Peter Stahl and bassist Skeeter Thompson, Stax helped create the lightning-fast tempo that was a trademark of the punk rock genre.
- `d8s2` Kent Stax [2]: Considered one of the fastest and most energetic drummers in the field at that time, his talents lent themselves to keeping a thrashing powerful musical force under control, giving Scream its homegrown reputation as pioneers in the genre which transcended into some international notoriety.
- `d8s3` Kent Stax [3]: In the late eighties Stax left the band for personal reasons and David Grohl, a local drummer who was working with local band Dain Bramage replaced the longtime drummer.
- `d8s4` Kent Stax [4]: Stax played drums in a series of bands throughout the 1990s that drew influence from English punk and Oi music, most notably The Suspects (a band that had many muttering about a DC hardcore revival not seen since 1983) United 121 and Spitfires United.
- `d8s5` Kent Stax [5]: In the 2000s he played drums in the DC Oi-core band Alleged Bricks.
- `d9s0` Hans Orifice [0]: Hans Orifice is a drummer best known as a member of Gwar.
- `d9s1` Hans Orifice [1]: Born Jim Thomson, in Alexandria, Virginia, he first took the name Hans Sphincter, and assumed his current name in 1987.
- `d9s2` Hans Orifice [2]: Thomson left due to touring commitments with his main band, the Alter Natives, who released three albums on SST Records.
- `d9s3` Hans Orifice [3]: Richmond drummer Rob Mosby of the Richmond, Virginia punk group White Cross then joined Gwar until 1989.
- `d9s4` Hans Orifice [4]: Hans Orifice returned briefly in 1989 after Mosby left the group.
- `d9s5` Hans Orifice [5]: During this time Thomson co-wrote "Sick of You" with the band and completed a U.S. and Canadian tour.
- `d9s6` Hans Orifice [6]: After the tour Thomson left Gwar on good terms to tour with The Alter Natives.
- `d9s7` Hans Orifice [7]: He was replaced by current drummer Jizmak Da Gusha.
- `d10s0` The Unguided [0]: The Unguided is a melodic death metal band from Sweden, formed by Richard Sjunnesson, after his departure from Sonic Syndicate.
- `d10s1` The Unguided [1]: Later, he was joined by (also former Sonic Syndicate singer) Roland Johansson, and (then) Sonic Syndicate guitarist Roger Sjunnesson and drummer John Bengtsson and current Cipher System bassist Henric Liljesand.
- `d10s2` The Unguided [2]: Drummer John Bengtsson left the band and in late 2012 The Unguided found their current drummer, Richard Schill.
- `d10s3` The Unguided [3]: In December 2016, the band revealed that vocalist/guitarist Roland Johansson had left the band and they found their current vocalist/guitarist, former touring member Jonathan Thorpenberg.

</details>

## Q297 — `hotpotqa_5ae52ba755429908b6326538` (revised draft)

> Which professional stock racing driver has won the Xfinity Series twice, and beat Kevin Harvick in the 2016 Bojangles' Southern 500?

Source answer: Martin Truex Jr.

Gold final answer: Martin Truex Jr.

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: winner of the 2016 Bojangles Southern 500 who held off Kevin Harvick | false | Martin Truex Jr. | — | [d7s2] | — |
| u2: driver {u1} who won two Xfinity Series titles | true | Martin Truex Jr. (accepted alternatives: Martin Lee Truex Jr.) | u1 | [d3s2] | — |

Evidence:

- `d3s2` Martin Truex Jr. [2]: Truex is a two-time Xfinity Series champion; having won the title in 2004 and 2005.
- `d7s2` 2016 Bojangles' Southern 500 [2]: Furniture Row Racing's Martin Truex Jr. won the race by holding off Kevin Harvick to earn his second victory of the 2016 season.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Daniel Suárez [0]: Daniel Alejandro Suárez Garza (born January 7, 1992) is a Mexican professional stock car racing driver.
- `d1s1` Daniel Suárez [1]: He currently competes full-time in the Monster Energy NASCAR Cup Series, driving the No. 19 Toyota Camry for Joe Gibbs Racing, and part-time in the Xfinity Series, driving the No. 18 and No. 20 Camrys for JGR.
- `d1s2` Daniel Suárez [2]: Previously he drove in the NASCAR Toyota Series in Mexico for Telcel Racing, and the K&N Pro Series East for Rev Racing as a member of the Drive for Diversity program.
- `d1s3` Daniel Suárez [3]: He is the 2016 NASCAR Xfinity Series champion.
- `d2s0` Kevin Harvick [0]: Kevin Michael Harvick (born December 8, 1975) is an American professional stock car racing driver.
- `d2s1` Kevin Harvick [1]: He currently competes full-time in the Monster Energy NASCAR Cup Series, driving the No. 4 Ford Fusion for Stewart-Haas Racing and part-time in the Xfinity Series, driving the No. 41 Ford Mustang for SHR.
- `d2s2` Kevin Harvick [2]: Harvick is the former owner of Kevin Harvick Incorporated, a race team that fielded cars in the Xfinity and Camping World Truck Series between 2004 and 2011.
- `d2s3` Kevin Harvick [3]: He is the 2014 NASCAR Sprint Cup Series champion and a two-time Xfinity Series champion.
- `d2s4` Kevin Harvick [4]: Harvick holds the all-time record for Cup Series wins at Phoenix International Raceway with eight wins.
- `d2s5` Kevin Harvick [5]: Harvick is also the third winningest driver in Xfinity Series history with 46 wins.
- `d3s0` Martin Truex Jr. [0]: Martin Lee Truex Jr. (born June 29, 1980) is an American championship professional stock car racing driver.
- `d3s1` Martin Truex Jr. [1]: He currently competes full-time in the Monster Energy NASCAR Cup Series, driving the No. 78 Toyota Camry for Furniture Row Racing.
- `d3s2` Martin Truex Jr. [2]: Truex is a two-time Xfinity Series champion; having won the title in 2004 and 2005.
- `d3s3` Martin Truex Jr. [3]: His younger brother, Ryan is a champion in the K&N Pro Series East division and currently races in the Camping World Truck Series, while his cousin Curtis raced for JR Motorsports.
- `d4s0` 2013 Bojangles' Southern 500 [0]: The 2013 Bojangles' Southern 500, the 64th running of the event, was a NASCAR Sprint Cup Series stock car race held on May 11, 2013, at Darlington Raceway in Darlington, South Carolina, United States.
- `d4s1` 2013 Bojangles' Southern 500 [1]: The race was contested over 367 laps on the 1.366–mile (2.198 km) oval, it was the eleventh race of the 2013 Sprint Cup Series championship.
- `d4s2` 2013 Bojangles' Southern 500 [2]: Matt Kenseth of Joe Gibbs Racing won the race, his third win of the 2013 season, while his teammate Denny Hamlin finished second.
- `d4s3` 2013 Bojangles' Southern 500 [3]: Jeff Gordon grabbed his 300th top 5 finish in his 700th Sprint Cup start, while Jimmie Johnson and Kevin Harvick rounded out the top five.
- `d5s0` Roush Fenway Racing [0]: Roush Fenway Racing, originally Roush Racing, is an American professional stock car racing team that currently competes in the Monster Energy NASCAR Cup Series, and the Xfinity Series.
- `d5s1` Roush Fenway Racing [1]: Once one of NASCAR's largest premier racing teams, Roush runs teams in the Monster Energy Cup Series, Xfinity Series, and formerly in the Camping World Truck Series and ARCA Racing Series.
- `d5s2` Roush Fenway Racing [2]: In the NASCAR Cup Series, the team fields the No. 6 Ford Fusion full-time for Trevor Bayne, and the No. 17 Fusion full-time for Ricky Stenhouse Jr. In the Xfinity Series, the team currently fields the No. 16 Ford Mustang full-time for Ryan Reed, and the No. 60 Mustang part-time for Ty Majeski
- `d6s0` O'Reilly Auto Parts 300 (fall race) [0]: The O'Reilly Auto Parts 300 is a NASCAR Xfinity Series stock car race that takes place at Texas Motor Speedway in Fort Worth, Texas.
- `d6s1` O'Reilly Auto Parts 300 (fall race) [1]: The race came about from the results of the Ferko lawsuit in 2004.
- `d6s2` O'Reilly Auto Parts 300 (fall race) [2]: With Darlington Raceway forced to forfeit its Southern 500 weekend as a result of the lawsuit, TMS gained a second weekend on the schedule for the Monster Energy NASCAR Cup Series and Xfinity Series racing, and fifth race for the NASCAR Xfinity Series playoffs.
- `d7s0` 2016 Bojangles' Southern 500 [0]: The 2016 Bojangles' Southern 500, the 67th running of the event, was a NASCAR Sprint Cup Series stock car race that was held on September 4, 2016 at Darlington Raceway in Darlington, South Carolina.
- `d7s1` 2016 Bojangles' Southern 500 [1]: Contested over 367 laps on the 1.366 mi egg-shaped oval, it was the 25th race of the 2016 NASCAR Sprint Cup Series season.
- `d7s2` 2016 Bojangles' Southern 500 [2]: Furniture Row Racing's Martin Truex Jr. won the race by holding off Kevin Harvick to earn his second victory of the 2016 season.
- `d8s0` List of NASCAR race wins by Kevin Harvick [0]: Kevin Harvick is an American racing driver who won a Monster Energy NASCAR Cup Series championship.
- `d8s1` List of NASCAR race wins by Kevin Harvick [1]: Over the course of his racing career, Harvick has won multiple races, 36 of which were in Monster Energy NASCAR Cup Series as well as 46 in Xfinity Series and 14 in Camping World Truck Series for a total of 96 wins across NASCAR's top 3 Series.
- `d9s0` 2014 Bojangles' Southern 500 [0]: The 2014 Bojangles' Southern 500, the 58th running of the event that traces its lineage to the 1957 Rebel 300, was a NASCAR Sprint Cup Series stock car race held on April 12, 2014, at Darlington Raceway in Darlington, South Carolina.
- `d9s1` 2014 Bojangles' Southern 500 [1]: The race was contested over 374 laps – extended from 367 laps due to two attempts at a green–white–checker finish – on the 1.366 mi oval, it was the eighth race of the 2014 NASCAR Sprint Cup Series.
- `d9s2` 2014 Bojangles' Southern 500 [2]: Kevin Harvick of Stewart-Haas Racing won the race, his second win of the season and first at Darlington, while Dale Earnhardt, Jr. finished second.
- `d9s3` 2014 Bojangles' Southern 500 [3]: Jimmie Johnson, Matt Kenseth, and Greg Biffle rounded out the top five.
- `d9s4` 2014 Bojangles' Southern 500 [4]: The race was also the first Darlington race won by a polesitter since Dale Jarrett, in the 1997 Rebel (then a 400-mile race).
- `d9s5` 2014 Bojangles' Southern 500 [5]: The top rookies of the race were Kyle Larson (8th), Austin Dillon (11th), and Justin Allgaier (23rd).
- `d9s6` 2014 Bojangles' Southern 500 [6]: It was the longest race in Darlington Raceway history.
- `d10s0` Darrell Wallace Jr. [0]: Darrell Wallace Jr. (born October 8, 1993), also known as Bubba Wallace, is an American professional stock car racing driver.
- `d10s1` Darrell Wallace Jr. [1]: He currently competes part-time in the NASCAR Camping World Truck Series, driving the No. 99 Chevrolet Silverado for MDM Motorsports, as well as in the NASCAR Xfinity Series, driving the No. 98 Ford Mustang for Biagi-DenBeste Racing.
- `d10s2` Darrell Wallace Jr. [2]: Previously, Wallace was signed as a development driver for Joe Gibbs Racing where Wallace competed in the Camping World Truck Series, driving the No. 54 Toyota Tundra for Kyle Busch Motorsports.
- `d10s3` Darrell Wallace Jr. [3]: Afterwards, he raced in the Xfinity Series, driving the No. 6 Ford Mustang of Roush Fenway Racing, from 2015 to 2017.

</details>

## Q298 — `hotpotqa_5ae532e955429908b632656f` (revised draft)

> Does the genus Cunninghamia or Chilopsis contain only one species?

Source answer: Chilopsis

Gold final answer: Chilopsis

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: species count of Chilopsis | false | one | — | [d5s0] | — |
| u2: Does the genus Cunninghamia or Chilopsis contain only one species? | true | Chilopsis **[by_presupposition]** | u1 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d5s0` Chilopsis [0]: Chilopsis is a monotypic genus of flowering plants containing the single species Chilopsis linearis.

Notes:

- Chilopsis explicitly has one species. Cunninghamia is given as one or two. The unique named-candidate premise identifies Chilopsis; review the uncertain taxonomy before freezing.
- 保留Chilopsis的明确单种正向链路和唯一候选预设。Cunninghamia的one or two不等于明确多于一种，不增设排除证据；在报告保留分类不确定性。

<details><summary>All source context</summary>

- `d1s0` Nomascus [0]: Nomascus is the second-most speciose genus of gibbons (family Hylobatidae).
- `d1s1` Nomascus [1]: Originally, this genus was a subgenus of "Hylobates", and all individuals were considered one species, "Hylobates concolor".
- `d1s2` Nomascus [2]: Species within "Nomascus" are characterized by 52 chromosomes.
- `d1s3` Nomascus [3]: Some species are all black, some are light with a distinct black tuft of crown fur, and some have distinct, light-colored cheek patches.
- `d1s4` Nomascus [4]: "Nomascus" is found from southern China (Yunnan) to southern Vietnam, and also on Hainan Island.
- `d1s5` Nomascus [5]: One species, "Nomascus nasutus," has been deemed "the most critically endangered ape species in the world".
- `d1s6` Nomascus [6]: All species in this genus are endangered or critically endangered.
- `d2s0` Bupleurum [0]: Bupleurum is a large genus of annual or perennial herbs or woody shrubs, with about one hundred and ninety species, belonging to the Apiaceae family.
- `d2s1` Bupleurum [1]: The full size of its species may vary between a few cm to up to 3 m high.
- `d2s2` Bupleurum [2]: Their compound umbels of small flowers are adorned with bracteoles that are sometimes large and may play a role in attracting pollinators.
- `d2s3` Bupleurum [3]: Rare among Apiaceae are the simple leaves, bracts (if present) and bracteoles.
- `d2s4` Bupleurum [4]: The genus is almost exclusively native in the Old World Northern Hemisphere, with one species native to North America and one species native to southern Africa.
- `d3s0` Pseudopontia [0]: Pseudopontia is a genus of butterflies found only in wet forests of tropical Africa.
- `d3s1` Pseudopontia [1]: It is the only genus in the subfamily Pseudopontiinae.
- `d3s2` Pseudopontia [2]: It was traditionally thought to contain only one species (monotypic), "Pseudopontia paradoxa".
- `d3s3` Pseudopontia [3]: However, a recent study showed there are at least five species of "Pseudopontia" which can be distinguished genetically and by details of wing veins.
- `d3s4` Pseudopontia [4]: Each is found primarily in a different part of Africa, though several of the species have overlapping geographic distributions.
- `d4s0` Anthocharis [0]: Anthocharis is a Holarctic genus of the butterfly tribe Anthocharini, in the Pieridae family.
- `d4s1` Anthocharis [1]: These are typically small, white-hued butterflies that have colorful marks just inside the tips of the forewings.
- `d4s2` Anthocharis [2]: The tip colors are usually a red-orange hue, hence the name "orange tip".
- `d4s3` Anthocharis [3]: The larvae of these butterfly often consume cruciferous plants containing chemicals called glucosinolates.
- `d4s4` Anthocharis [4]: This genus is characterized by two of the five subcostal veins branching off before the apex of the cell, by the upper radial being only little united with the subcostal, and by the central discocellular being rather long.
- `d4s5` Anthocharis [5]: In all the species the males have at least the apical portion of the forewing orange red or yellow.
- `d4s6` Anthocharis [6]: Only one species inhabits also the northern districts of the Palearctic region, all the others are found in the south of the Palearctic region, also some species occur in North America, but not one species extends into the tropics.
- `d4s7` Anthocharis [7]: The Anthocharis species have only one brood.
- `d4s8` Anthocharis [8]: The butterflies occur in spring.
- `d5s0` Chilopsis [0]: Chilopsis is a monotypic genus of flowering plants containing the single species Chilopsis linearis.
- `d6s0` Megacheira [0]: Megacheira ("Great Hands") is an extinct class of predatory arthropods that possessed a pair of short enlarged appendages (the source of the class' name).
- `d6s1` Megacheira [1]: They strongly resemble early chelicerates.
- `d6s2` Megacheira [2]: Most of them were found in marine environments throughout the world from the lower to middle Cambrian.
- `d6s3` Megacheira [3]: The group might also contain one species ("Enalikter aphson") described from the Silurian Herefordshire Lagerstätte of the United Kingdom, and one species ("Bundenbachiellus giganteus") known from the Early Devonian of Germany; however, the interpretation of these taxa as megacheirans was challenged by Struck "et al." (2015).
- `d6s4` Megacheira [4]: Megacheirans were important components of several faunas, including the Burgess, Wheeler and Maotianshan Shales Lagerstatten.
- `d6s5` Megacheira [5]: Genera referred to the class include "Leanchoilia", "Alalcomenaeus", "Oestokerkus", "Yohoia", "Fortiforceps" and "Jianfengia".
- `d7s0` Giraffe [0]: The giraffe ("Giraffa") is a genus of African even-toed ungulate mammals, the tallest living terrestrial animals and the largest ruminants.
- `d7s1` Giraffe [1]: The genus currently consists of one species, "Giraffa camelopardalis", the type species.
- `d7s2` Giraffe [2]: Seven other species are extinct, prehistoric species known from fossils.
- `d7s3` Giraffe [3]: Taxonomic classifications of one to eight extant giraffe species have been described, based upon research into the mitochondrial and nuclear DNA, as well as morphological measurements of "Giraffa," but the IUCN currently recognizes only one species with nine subspecies.
- `d8s0` Oligoryzomys fulvescens [0]: Oligoryzomys fulvescens, also known as the fulvous colilargo, fulvous pygmy rice rat, or northern pygmy rice rat, is a species of rodent in the genus "Oligoryzomys" of family Cricetidae.
- `d8s1` Oligoryzomys fulvescens [1]: It is found from southern Mexico through Central America into South America, where it occurs south into Peru and Brazil, and includes numerous synonyms, including the type species of the genus, "Oryzomys navus" Bangs, 1899.
- `d8s2` Oligoryzomys fulvescens [2]: The taxonomy of this species is unresolved, and it may be found to contain more than one species.
- `d8s3` Oligoryzomys fulvescens [3]: Its karyotype has 2n = 54-60 and FNa = 68-74.
- `d9s0` Argyrochosma [0]: Argyrochosma is a genus of ferns known commonly as false cloak ferns.
- `d9s1` Argyrochosma [1]: The genus is included in the Cheilanthoideae subfamily of the Pteridaceae.
- `d9s2` Argyrochosma [2]: Species now in this genus were previously treated as members of related genera "Notholaena" or "Pellaea" but were segregated into their own genus in 1987.
- `d9s3` Argyrochosma [3]: These ferns, of which there are about 20 species, are mostly native to the Americas, from North to South and including the Caribbean, while one species, "A. connectens", is known from Sichuan, China.
- `d9s4` Argyrochosma [4]: They are commonly found growing in cracks between rocks.
- `d9s5` Argyrochosma [5]: Their leaves are generally shorter than 40 centimeters and have rounded bluish or grayish green segments.
- `d9s6` Argyrochosma [6]: Often the lower surface of the segments is coated in a white dust, and the sporangia contain brown spores.
- `d10s0` Cunninghamia [0]: Cunninghamia is a genus of one or two living species of evergreen coniferous trees in the cypress family Cupressaceae.
- `d10s1` Cunninghamia [1]: They are native to China, northern Vietnam and Laos, and perhaps also Cambodia.
- `d10s2` Cunninghamia [2]: They may reach 50 m in height.
- `d10s3` Cunninghamia [3]: In vernacular use, it is most often known as "Cunninghamia", but is also sometimes called "China-fir" (though it is not a fir).
- `d10s4` Cunninghamia [4]: The genus name "Cunninghamia" honours Dr. James Cunningham, a British doctor who introduced this species into cultivation in 1702 and botanist Allan Cunningham.

</details>

## Q299 — `hotpotqa_5ae5b25d5542990ba0bbb2bb` (revised draft)

> Who has more distinct professions explicitly listed in the context, Christopher Guest or Roman Karmen?

Source answer: Christopher Haden-Guest

Gold final answer: Christopher Haden-Guest

Question type: `comparison` (source type `comparison`)

Original question: Who has a wider scope of profession, Christopher Guest or  Roman Karmen?

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: occupations explicitly listed for Christopher Guest | false | screenwriter, composer, musician, director, actor, comedian | — | [d4s0] | — |
| u2: occupations explicitly listed for Roman Karmen | false | camera-man, film director | — | [d5s0] | — |
| u3: Who has more distinct professions explicitly listed in the context, Christopher Guest or Roman Karmen? | true | Christopher Haden-Guest (accepted alternatives: Christopher Guest) | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d4s0` Christopher Guest [0]: Christopher Haden-Guest, 5th Baron Haden-Guest (born February 5, 1948), simply known as Christopher Guest, is an English-American screenwriter, composer, musician, director, actor, and comedian who holds dual British and American citizenship.
- `d5s0` Roman Karmen [0]: Roman Lazarevich Karmen (Russian: Рома́н Ла́заревич Карме́н ; 29 November [O.S. 16 November] 1906 in Odessa – 28 April 1978 in Moscow) was a Soviet war camera-man and film director and one of the most influential figures in documentary film making.

Notes:

- 补题干姓名别名。
- 题干澄清：将主观wider scope明确为文档列举职业数量，按6与2比较。

<details><summary>All source context</summary>

- `d1s0` Slavery in Libya [0]: Slavery in Libya has a long history and a lasting impact on the Libyan culture.
- `d1s1` Slavery in Libya [1]: It is closely connected with the wider context of slavery in north Africa.
- `d1s2` Slavery in Libya [2]: Therefore, it is better understood when this wider scope is taken into account.
- `d2s0` Great Is My Country [0]: Vast is my Native Land (1958), also known as "Great is my Country", (Russian: Широка страна моя родная , "Shiroka strana moya rodnaya" ), from the song of the same name, which is featured in the film, by the Russian composer Isaac Dunaevsky) was the first film shot in the Soviet wide-screen film format known as Kinopanorama.
- `d2s1` Great Is My Country [1]: The film was directed by Roman Karmen, known for various documentary films produced in the Soviet Union.
- `d2s2` Great Is My Country [2]: The music was composed by Kirill Molchanov, a noted composer of music for ballet and opera.
- `d3s0` Oleg Makara [0]: Oleg Makara-Kalmáry (born October 13, 1954, Czechoslovakia) is a film director, screenwriter and Slovak writer.
- `d3s1` Oleg Makara [1]: In 1969, he wrote his debut as a screenwriter "Pozlátené dievča" at the age of 14.
- `d3s2` Oleg Makara [2]: He then went on to study film directing at All States Institute (now Gerasimov Institute of Cinematography) in Moscow under Roman Karmen.
- `d3s3` Oleg Makara [3]: A pseudonym is after his grandfather, art carpenter, Eduard Kalmáry.
- `d3s4` Oleg Makara [4]: E. Kalmáry was a chief manager of water sawmill in Remetské Hámre, East Slovakia, owned by family Vanderbilts.
- `d4s0` Christopher Guest [0]: Christopher Haden-Guest, 5th Baron Haden-Guest (born February 5, 1948), simply known as Christopher Guest, is an English-American screenwriter, composer, musician, director, actor, and comedian who holds dual British and American citizenship.
- `d4s1` Christopher Guest [1]: Guest is most widely known in Hollywood for having written, directed and starred in his series of comedy films shot in mock-documentary (mockumentary) style.
- `d4s2` Christopher Guest [2]: Many scenes and character backgrounds in Guest's films are written and directed, although actors have no rehearsal time and the ensemble improvise scenes while filming them.
- `d4s3` Christopher Guest [3]: The series of films began with "This Is Spinal Tap" (directed by Rob Reiner), and continued with "Waiting for Guffman", "Best In Show", "A Mighty Wind", "For Your Consideration", and "Mascots".
- `d5s0` Roman Karmen [0]: Roman Lazarevich Karmen (Russian: Рома́н Ла́заревич Карме́н ; 29 November [O.S. 16 November] 1906 in Odessa – 28 April 1978 in Moscow) was a Soviet war camera-man and film director and one of the most influential figures in documentary film making.
- `d6s0` Music for Dogs [0]: Music for Dogs is the third studio album by American indie rock band Gardens & Villa.
- `d6s1` Music for Dogs [1]: Released on 21 August 2015 by independent record label Secretly Canadian.
- `d6s2` Music for Dogs [2]: The album was orchestrated with the help of visionary producer Jacob Portrait of Unknown Mortal Orchestra.
- `d6s3` Music for Dogs [3]: The band hoped ""Music for Dogs"" would maintain a wider scope than some of their other work by making it sound just as much like the futuristic music of tomorrow as it does the classic tunes of '76
- `d7s0` Gerold, Prefect of Bavaria [0]: Gerold (died 799) was an Alamannian nobleman who served the Frankish King, Charlemagne, as Margrave of the Avarian March and Prefect of Bavaria in what is now South-Eastern Germany.
- `d7s1` Gerold, Prefect of Bavaria [1]: Gerold played a significant role in the integration of Bavaria into the Frankish Kingdom during Carolingian expansion in the late 8th, and early 9th centuries.
- `d7s2` Gerold, Prefect of Bavaria [2]: Gerold both aided the continuity of Agilofing rule of Bavaria, as well as took steps to integrate Bavarians into the wider scope of the Frankish Kingdom.
- `d7s3` Gerold, Prefect of Bavaria [3]: Gerold was related both to the Agilofing family, the ruling class of Bavaria, as well as the Carolingian family.
- `d7s4` Gerold, Prefect of Bavaria [4]: The Agilofings had ruled Bavaria since Duke Garibald I in 548.
- `d7s5` Gerold, Prefect of Bavaria [5]: Gerold was born into the Agilofings, and his sister Hildegard was married to Charlemagne in 771.
- `d7s6` Gerold, Prefect of Bavaria [6]: From these familial connections, he was appointed Prefect of Bavaria following the deposition of Duke Tassilo III in 788.
- `d7s7` Gerold, Prefect of Bavaria [7]: Gerold was heralded as a superb military commander, giving rise to his promotion to Prefect as a defender of the eastern border of the Frankish Kingdom.
- `d7s8` Gerold, Prefect of Bavaria [8]: In 799, Gerold is said to have fallen in battle against the Avars, shortly after the same Avars killed his ally, Erich, Duke of Friuli, through treachery.
- `d8s0` Science Supercourse [0]: Science Supercourse is a free online accessible educational resource currently encompassing more than 165,000 downloadable PowerPoint lectures covering four main areas of science; Public Health, Computer Engineering, Environment and Agriculture.
- `d8s1` Science Supercourse [1]: It represents an extension to ""Supercourse"" initiative which started out at the University of Pittsburgh by scientist Ronald LaPorte in the 80's.
- `d8s2` Science Supercourse [2]: It is mirrored at the Library of Alexandria, and networks over 56,000 scientists in 174 countries.
- `d8s3` Science Supercourse [3]: Being a useful tool for at least one million students from around the globe, Supercourse has been a well-established starting point which triggered the emergence of the new Science Supercourse in 2008 with a wider scope in terms of content and functionalities.
- `d9s0` Nuremberg Trials (film) [0]: The Nuremberg Trials is a 1947 Soviet-made documentary film about the trials of the Nazi leadership.
- `d9s1` Nuremberg Trials (film) [1]: It was produced by Roman Karmen, and was an English-language version of the Russian language film "Суд народов" (Judgment of the Peoples).
- `d10s0` Women's Missionary and Service Commission [0]: The Women's Missionary and Service Commission, previously known as the Women's Missionary and Service Auxiliary and abbreviated WMSC or WMSA, was a women's organization of the "old" Mennonite Church that originated out of the Mennonite Sewing Circle movement.
- `d10s1` Women's Missionary and Service Commission [1]: Named the WMSC in 1971, there were many precursor organizations and it has since involved into Mennonite Women USA, an organization with a much wider scope.

</details>

## Q300 — `hotpotqa_5a90bd6555429933b8a205cf` (revised draft)

> What is the nationality of the singer-songwriter who wrote the poetry collection Early Work ?

Source answer: American

Gold final answer: American

Question type: `bridge` (source type `bridge`)

Replaces: `hotpotqa_5ae6050f55429929b0807a5e`

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: author of the poetry collection Early Work | false | Patti Smith | — | [d9s0] | — |
| u2: nationality of {u1} | true | American | u1 | [d8s0] | — |

Evidence:

- `d8s0` Patti Smith [0]: Patricia Lee Smith (born December 30, 1946) is an American singer-songwriter, poet, and visual artist who became an influential component of the New York City punk rock movement with her 1975 debut album "Horses".
- `d9s0` Early Work [0]: Early Work is a poetry collection by Patti Smith, published in 1994.

Notes:

- 替换：Jim Cummings配音的是Dr. Robotnik，作品名Sonic不是刺猬角色配音证据。 新题保留原source type，人工核对两条显式事实及答案。

<details><summary>All source context</summary>

- `d1s0` Sandy Shreve [0]: Sandy Shreve is a Canadian poet, editor and visual artist living on Pender Island, British Columbia.
- `d1s1` Sandy Shreve [1]: Shreve has written, edited and/or co-edited eight books and two chapbooks.
- `d1s2` Sandy Shreve [2]: Her latest poetry collection is "Waiting for the Albatross".
- `d1s3` Sandy Shreve [3]: Recent work has appeared in her chapbooks, "Cedar Cottage Suite" and "Level Crossing".
- `d1s4` Sandy Shreve [4]: Her work is widely anthologized and has won or been shortlisted for several awards, including the Earle Birney Prize (for "Elles", published in "Prism Magazine", 2000) and the Milton Acorn Peoples Poetry Award (for "Belonging", Sono Nis Press, 1997).
- `d1s5` Sandy Shreve [5]: She co-edited, with Kate Braid, the anthology "In Fine Form – The Canadian Book of Form Poetry" (2005) and "In Fine Form, 2nd edition - A Contemporary Look and Canadian Form Poetry"(2016); edited "Working For A Living", a collection of poems and stories by women about their work (Room of One’s Own, 1988) and founded BC’s "Poetry in Transit" program, which has been displaying BC poetry in SkyTrain cars and buses across the province since 1996.
- `d2s0` B. H. Fairchild [0]: B.H. Fairchild (born 1942) is an American poet and former college professor.
- `d2s1` B. H. Fairchild [1]: His most recent book is "Usher" (W.W. Norton, 2009), and his poems have appeared in literary journals and magazines including "The New Yorker", "The Paris Review", "The Southern Review", "Poetry", "TriQuarterly", "The Hudson Review", "Salmagundi", "The Sewanee Review."
- `d2s2` B. H. Fairchild [2]: His third poetry collection, "The Art of the Lathe," winner of the 1997 Beatrice Hawley Award (Alice James Books, 1998), brought Fairchild's work to national prominence, garnering him a large number of awards and fellowships including the William Carlos Williams Award, Kingsley Tufts Poetry Award, California Book Award, Natalie Ornish Poetry Award, PEN Center USA West Poetry Award, National Book Award (finalist), Capricorn Poetry Award, and Rockefeller and Guggenheim fellowships.
- `d2s3` B. H. Fairchild [3]: The book ultimately gave him international prominence, as The Way Weiser Press in England published the U.K. edition of the book.
- `d2s4` B. H. Fairchild [4]: "The Los Angeles Times" wrote that ""The Art of the Lathe" by B.H. Fairchild has become a contemporary classic—a passionate example of the plain style, so finely crafted and perfectly pitched...workhorse narratives suffused with tenderness and elegiac music."
- `d3s0` Saeed Ahmad Akhtar [0]: Saeed Ahmad Akhtar was an Urdu poet, playwright and educationist.
- `d3s1` Saeed Ahmad Akhtar [1]: He came up with his 1st Urdu poetry collection “Diyaar e Shab” in 1976.
- `d3s2` Saeed Ahmad Akhtar [2]: It was the best selling book of the year and got many awards including the "Abbasin Arts Council Award" for the best book of the year.
- `d3s3` Saeed Ahmad Akhtar [3]: He published 12 Urdu poetry collections and one English poetry collection so far.
- `d3s4` Saeed Ahmad Akhtar [4]: All his books sold out like hot cakes.
- `d3s5` Saeed Ahmad Akhtar [5]: He also wrote many plays and documentaries for Pakistan television and Radio Pakistan.
- `d4s0` Kevin MacNeil [0]: Kevin MacNeil is a Scottish novelist, poet and playwright born and raised in the Outer Hebrides.
- `d4s1` Kevin MacNeil [1]: His latest novel, "The Brilliant & Forever", was published by Polygon in March 2016.
- `d4s2` Kevin MacNeil [2]: MacNeil's previous novels, "A Method Actor's Guide to Jekyll and Hyde" (Polygon, 2011) and best-selling debut, "The Stornoway Way" (Hamish Hamilton, 2005), were both published to widespread critical acclaim.
- `d4s3` Kevin MacNeil [3]: MacNeil’s first book, the poetry collection "Love and Zen in the Outer Hebrides" (Canongate, 1998), won the Tivoli Europa Giovani International Poetry Prize for best poetry collection published in Europe by a writer under 35.
- `d4s4` Kevin MacNeil [4]: He is also the author of "Be Wise Be Otherwise" (Canongate) and the plays "Sweetness", an adaptation of a novel by Swedish author Torgny Lindgren, and "The Callanish Stoned" (Theatre Hebrides), and his short stories have been published extensively.
- `d4s5` Kevin MacNeil [5]: MacNeil's anthology of poetry from the Scottish islands, "These Islands, We Sing", was published by Polygon in June 2011.
- `d5s0` Bhau Panchbhai [0]: Bhau Panchabhai(1 March 1944 - 21Jan 2016 @ 5.30am) is a Marathi poet, writer, and Dalit activist.
- `d5s1` Bhau Panchbhai [1]: Panchbhai is best known for his first poetry collection "Hunkaar Vadaalnche (हुंकार वादळांचे)" for which he was awarded by Government of Maharashtra for best poetry collection that year(1989).
- `d5s2` Bhau Panchbhai [2]: His poetry is considered as a prototype of Ambedkarite poetry and is translated in various languages including English.
- `d5s3` Bhau Panchbhai [3]: He lives at Nagpur and works as a lawyer.
- `d6s0` Heichū Monogatari [0]: Tales of Heichū (Heichū monogatari) belongs to the genre of uta monogatari poem tales that emerged in Japanese literature from the mid 10th to the early 11th centuries.
- `d6s1` Heichū Monogatari [1]: As early as the "Collection of Ten-Thousand Leaves" ("Manyōshū"), a poetry collection completed around 759, there appeared poems introduced by brief prose narrations.
- `d6s2` Heichū Monogatari [2]: The imperial court began to come alive with poetry from around this time.
- `d6s3` Heichū Monogatari [3]: People exchanged poetry with one another on topics as diverse as love and politics and religion.
- `d6s4` Heichū Monogatari [4]: Towards the end of the 9th century it was common for individual poets to keep compilations of their own verse, sometimes explaining in prose the circumstances behind a poem's composition.
- `d6s5` Heichū Monogatari [5]: The highest honor was to have ones poem selected for inclusion in the "Collection of Ancient and Modern Poetry" (Kokinshū), the first imperial poetry collection, which was completed around 905.
- `d6s6` Heichū Monogatari [6]: By the middle of the 10th century the idea of a poem paired with a prose narration seems to have taken hold, and "Tales of Ise" (Ise monogatari), "Tales of Heichū", and "Tales of Yamato" (Yamato monogatari) seem to have emerged at about this same time.
- `d6s7` Heichū Monogatari [7]: Also, the second imperial poetry collection, "Collection of Later Poetry" (Gosenshū), commissioned in 951 and compiled shortly thereafter, has many narrative qualities.
- `d6s8` Heichū Monogatari [8]: The only extant manuscript of "Tales of Heichū" is a 61-page codex discovered in 1931 that seems to date from the Kamakura Period (1185–1333), some three hundred years after the work's probable date of composition.
- `d7s0` The Poetry Collection [0]: A University at Buffalo Libraries Special Collection, The Poetry Collection at the University at Buffalo, The State University of New York, is devoted to 20th century poetry in English and English translation.
- `d7s1` The Poetry Collection [1]: Founded by Charles David Abbott, the University at Buffalo's first Director of Libraries, The Poetry Collection contains over 100,000 volumes by every major and many minor poet writing in English.
- `d7s2` The Poetry Collection [2]: Recordings of poets reading from their own works, poets' notebooks, letters and manuscripts, and a wide variety of literary magazines are also included in this collection.
- `d7s3` The Poetry Collection [3]: Approximately 5,000 little magazine titles, 1,200 current subscriptions, and a number of portraits, sculptures, and photographs round out the collection.
- `d7s4` The Poetry Collection [4]: Also included in the Poetry Collection is the James Joyce Archive, the world's largest collection of James Joyce manuscripts, books and artifacts.
- `d8s0` Patti Smith [0]: Patricia Lee Smith (born December 30, 1946) is an American singer-songwriter, poet, and visual artist who became an influential component of the New York City punk rock movement with her 1975 debut album "Horses".
- `d9s0` Early Work [0]: Early Work is a poetry collection by Patti Smith, published in 1994.
- `d10s0` Bjarki Karlsson [0]: Bjarki Már Karlsson (b. 1965) is a poet, linguist, and systems analyst.
- `d10s1` Bjarki Karlsson [1]: His first poetry collection, "Árleysi alda", won the Bókmenntaverðlaun Tómasar Guðmundssonar (Tómas Guðmundsson Award) for 2013.
- `d10s2` Bjarki Karlsson [2]: and the Bókmenntaverðlaun starfsfólks bókaverslana in the poetry category in the same year.
- `d10s3` Bjarki Karlsson [3]: The book was Iceland's best-selling poetry collection in 2013.

</details>
