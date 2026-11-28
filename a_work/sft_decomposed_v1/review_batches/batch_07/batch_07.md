# batch_07：人工审查（30 题）

全局题号 181–210；train 30 题 / dev 0 题。原训练/验证归属保持不变。

[返回分配索引](../README.md) · [完整对比报告](../../comparison_human.md)

**原则：新旧单元都合理时保留拆题器拆法，人工监督向新单元对齐。** 本批已由用户审核，按最新 Note 完成调整。

审查人：________　完成日期：________

本批已依据人工 Note 调整；原始拆题保存在 JSON 的 `raw_decomposition`。下方 Adjusted units 为当前标注，旧 gold 仅供参照。标注已更新；逐时刻 SFT 快照尚未重建。

## 1. hotpotqa_5ab4da805542996a3a969fd8

原位置：`train` 第 181 题 · 全局第 181 题 · `sample_id: hotpotqa_5ab4da805542996a3a969fd8`

Question: Until which year did this Polish professional boxer who lost to Joe Smith Jr. in 2016 in a knockout victory hold the IBO light heavyweight title?

Note: 保留旧的gold

Type: bridge · fallback: False · SFT snapshots: 7

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | Polish professional boxer who lost to Joe Smith Jr. by knockout in 2016 | False | [] | Andrzej Fonfara | [["d4s1", "d9s0"]] | context |
| u2 | year until which {u1} held the IBO light heavyweight title | True | ["u1"] | 2013 | [["d9s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | Polish professional boxer who lost to Joe Smith Jr. by knockout in 2016 | False | [] | Andrzej Fonfara | [['d4s1', 'd9s0']] |
| u2 | year until which {u1} held the IBO light heavyweight title | True | ['u1'] | 2013 | [['d9s0']] |

### Source documents (reference only)

**d1: Glen Johnson (boxer)**

- [d1s0] Glengoffe Donovan "Glen" Johnson (born 2 January 1969) is a Jamaican professional boxer.
- [d1s1]  A veteran of the sport for more than twenty years, he held the IBF light heavyweight title in 2004; and the IBO and "Ring" magazine light heavyweight titles from 2004 to 2005.
- [d1s2]  Johnson is best known for his upset knockout victory over Roy Jones Jr. in 2004, as well as his iron chin and relentless pressure fighting style.

**d2: Steve Aczel**

- [d2s0] Steve Aczel ( (1954--) 08 1954 (age (2017)-(1954)-((11)<(09)or(11)==(09)and(30)<(08)) ) ) born in Budapest is an Australian professional light heavy/cruiser/heavyweight boxer of the 1980s, '90s and 2000s who won the Australasian light heavyweight title, Australian light heavyweight title, Australian heavyweight title, Oriental and Pacific Boxing Federation (OPBF) heavyweight title, Queensland State (Australia) heavyweight title, and Commonwealth light heavyweight title, drew with Maile Haumona for the South Pacific heavyweight title, and was a challenger for the Australian cruiserweight title against Tony Mundine, and Commonwealth cruiserweight title against Stewart Lithgo, his professional fighting weight varied from 172 lb , i.e. light heavyweight to 203+1/2 lb , i.e. heavyweight.
- [d2s1]  He was inducted into the Australian National Boxing Hall of Fame in 2011.

**d3: Neil Simpson (boxer)**

- [d3s0] Neil "Simmo" Simpson ( (1974--) 23 1974 (age (2017)-(1974)-((11)<(01)or(11)==(01)and(30)<(23)) ) ) born in London, now based in Coventry, is an English professional light heavy/cruiser/heavyweight boxer of the 1990s and 2000s, who won the British Boxing Board of Control (BBBofC) Midlands Area light heavyweight title, BBBofC British light heavyweight title, British Masters Cruiserweight title, and Commonwealth light heavyweight title, and was a challenger for the International Boxing Organization (IBO) Inter-Continental light heavyweight title against Darren Corbett, European Boxing Union (EBU) light heavyweight title against Yawe Davis, World Boxing Union (WBU) light heavyweight title against Tony Oakey, and BBBofC British light heavyweight title against Peter Oboh, his professional fighting weight varied from 169 lb , i.e. light heavyweight to 216 lb , i.e. heavyweight.

**d4: Joe Smith Jr.**

- [d4s0] Joe Smith Jr. (born September 20, 1989) is an American professional boxer who held the regional WBC International light heavyweight title from 2016 to 2017.
- [d4s1]  He rose to prominence in 2016 by scoring an upset knockout victory over Andrzej Fonfara, and later becoming the first boxer to score a stoppage victory over former world champion Bernard Hopkins, who retired after their fight.

**d5: Garry Delaney**

- [d5s0] Gary Delaney ( (1970--) 12 1970 (age (2017)-(1970)-((11)<(08)or(11)==(08)and(30)<(12)) ) ) born in Newham is an English professional light heavy/cruiser/heavyweight boxer of the 1990s and 2000s.
- [d5s1]  He won the British Boxing Board of Control (BBBofC) Southern Area light heavyweight title, World Boxing Board (WBB) light heavyweight title, World Boxing Organization (WBO) Inter-Continental light heavyweight title, BBBofC Southern Area cruiserweight title, and Commonwealth light heavyweight title (twice), and was a challenger for the BBBofC British heavyweight title, and Commonwealth heavyweight title against Julius Francis, World Boxing Organization (WBO) Inter-Continental cruiserweight title against John Keeton, and Jesper Kristiansen, BBBofC British cruiserweight title, and Commonwealth (British Empire) cruiserweight title against Bruce Scott, and World Boxing Union cruiserweight title against Sebastiaan Rothmann, and Enzo Maccarinelli, his professional fighting weight varied from 174 lb , i.e. light heavyweight to 231 lb , i.e. heavyweight.

**d6: Guy Waters**

- [d6s0] Guy "Arc Angel" Waters ( (1964--) 25 1964 (age (2017)-(1964)-((11)<(01)or(11)==(01)and(30)<(25)) ) ) is an Australian professional welter/light middle/middle/super middle/light heavy/cruiserweight boxer of the 1980s, 1990s and 2000s who won the New South Wales State (Australia) light heavyweight title, Australian light heavyweight title, Oriental and Pacific Boxing Federation (OPBF) light heavyweight title, Australasian Light Heavyweight Title, World Boxing Federation (WBF) light heavyweight title, International Boxing Federation (IBF) Pan Pacific super middleweight title, Oriental and Pacific Boxing Federation (OPBF) super middleweight title, and Commonwealth light heavyweight title, and was a challenger for the WBC light heavyweight title against Dennis Andries, World Boxing Association (WBA) World light heavyweight title against Virgil Hill, World Boxing Council (WBC) cruiserweight title against Juan Carlos Gómez, and Commonwealth super middleweight title against David Starie, his professional fighting weight varied from 167+1/2 lb , i.e. super middleweight to 185+1/4 lb , i.e. cruiserweight.

**d7: Crawford Ashley**

- [d7s0] Crawford "Chilling" Ashley (born Gary Crawford, 20 May 1964 in Leeds is an English professional super middle/light heavy/cruiser/heavyweight boxer of the 1980s, '90s and 2000s, who won the British Boxing Board of Control (BBBofC) Central Area light heavyweight title, BBBofC British light heavyweight title, European Boxing Union (EBU) light heavyweight title (twice), and Commonwealth light heavyweight title (twice), drew with Yawe Davis for the vacant European Boxing Union (EBU) light heavyweight title, and was a challenger for the European Boxing Union (EBU) light heavyweight title against Graciano Rocchigiani, World Boxing Association (WBA) World super middleweight title against Michael Nunn, World Boxing Association (WBA) World light heavyweight title against Virgil Hill, and World Boxing Union (WBU) cruiserweight title against Sebastiaan Rothmann, his professional fighting weight varied from 163 lb , i.e. super middleweight to 211 lb , i.e. heavyweight.

**d8: Umar Salamov**

- [d8s0] Umar Salamov (born 7 June 1994, Alkhan-Kala, Russia) is a Russian light-heavyweight professional boxer.
- [d8s1]  Salamov has held the WBO Youth World Light Heavyweight title, IBO Youth World Light Heavyweight title and the IBO World Light Heavyweight title.
- [d8s2]  Salamov is currently ranked 8th in the WBO world rankings and 19th in Boxrec independent computerized rankings.

**d9: Andrzej Fonfara**

- [d9s0] Andrzej Fonfara (born 4 November 1987) is a Polish professional boxer who held the IBO light heavyweight title from 2012 to 2013.
- [d9s1]  He currently resides in Chicago, the city with the third largest Polish population in the world behind Warsaw and New York City.

**d10: Erik Skoglund (boxer)**

- [d10s0] Erik Skoglund (born 24 May 1991) is a Swedish professional boxer.
- [d10s1]  He currently holds the WBA International light heavyweight title.
- [d10s2]  As of December 2016, he is ranked #12 in the world at light heavyweight.
- [d10s3]  He previously held the IBO International light heavyweight title, the IBF Inter-Continental Light Heavyweight title, and the EBU-EU light heavyweight title which he defended three times.

## 2. hotpotqa_5ab5344c5542991751b4d7c5

原位置：`train` 第 182 题 · 全局第 182 题 · `sample_id: hotpotqa_5ab5344c5542991751b4d7c5`

Question: In which year was this former Australian footballer who played for the Collingwood Football Club and who is an older brother of the Australian rules footballer Robbie Tarrant born?

Note: 

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | former Australian footballer who played for the Collingwood Football Club and is an older brother of Robbie Tarrant | False | [] | Chris Tarrant | [["d9s1"]] | context |
| u2 | birth year of {u1} | True | ["u1"] | 1980 | [["d8s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | former Australian footballer who played for Collingwood and is an older brother of Robbie Tarrant | False | [] | Chris Tarrant | [['d9s1']] |
| u2 | birth year of {u1} | True | ['u1'] | 1980 | [['d8s0']] |

### Source documents (reference only)

**d1: Tom Langdon**

- [d1s0] Tom Langdon (born 9 June 1994) is a professional Australian rules footballer playing for the Collingwood Football Club in the Australian Football League (AFL).
- [d1s1]  He was recruited by the Collingwood Football Club with the 65th overall selection in the 2013 national draft.
- [d1s2]  He made his debut in Round 1, 2014, against Fremantle at Etihad Stadium, after featuring in all three senior pre-season games, averaging 15 disposals.
- [d1s3]  He is the older brother of Ed Langdon, who plays for Fremantle.

**d2: Andrew Dimattina**

- [d2s0] Andrew Dimattina (born 9 November 1977) is a former Australian rules footballer who played primarily as a midfielder for Collingwood Football Club in the Australian Football League (AFL).
- [d2s1]  Dimattina was 22 years old when he made his senior debut for Collingwood and played mainly as a run-with player.
- [d2s2]  He is the brother of Paul Dimattina who played for Western Bulldogs and is the son of Frank Dimattina who played for Richmond and North Melbourne.

**d3: Jackson Paine**

- [d3s0] Jackson Paine is a former professional Australian rules footballer who played for the Collingwood Football Club and Brisbane Lions in the Australian Football League (AFL).
- [d3s1]  He was recruited by the Collingwood Football Club with pick 50 in the 2011 national draft.
- [d3s2]  Paine made his debut in round 1, 2012 against Hawthorn .
- [d3s3]  He was traded in a straight swap for Patrick Karnezis in the 2013 trade period.
- [d3s4]  He was delisted by Brisbane in October 2015, however, he was re-drafted in the 2016 rookie draft.
- [d3s5]  He was delisted again by Brisbane at the conclusion of the 2016 season.

**d4: Grantley Fielke**

- [d4s0] Grantley Craig Fielke (born 18 March 1962 in Loxton, South Australia) is a former Australian rules footballer who played for West Adelaide Football Club in the South Australian National Football League (SANFL), and the Collingwood Football Club and Adelaide Football Club in the Victorian/Australian Football League (VFL/AFL).

**d5: Billy Picken**

- [d5s0] Billy Picken (born 7 June 1956) is a former Australian Australian rules footballer who played for the Collingwood Football Club and the Sydney Swans.
- [d5s1]  Picken arrived at Collingwood in 1974 from Macarthur as a forward but developed into one of the games finest centre-half backs.
- [d5s2]  Despite playing in four losing Grand Finals Picken maintained his reputation as a finals performer & was recognised for his fine contributions when named in the Collingwood Team of the century.
- [d5s3]  When Picken controversially moved to the Swans in 1984 he was hit by a succession of injuries for the first time in his career.
- [d5s4]  He later returned to Victoria Park to captain-coach the reserves.

**d6: Patrick Karnezis**

- [d6s0] Patrick Karnezis (born 23 April 1992) is a former professional Australian rules footballer who played for the Brisbane Lions and Collingwood Football Club in the Australian Football League (AFL).
- [d6s1]  He was taken at pick number 25 in the 2010 national draft by the Brisbane Lions.
- [d6s2]  Karnezis made his debut in round 13 of the 2011 season, against Richmond .
- [d6s3]  On 25 October 2013 he was traded to the Collingwood Football Club in exchange for Jackson Paine.
- [d6s4]  He retired from AFL at the conclusion of the 2015 season.

**d7: Josh Williams (Australian footballer)**

- [d7s0] Josh Williams (born 12 June 1998) is a professional Australian rules footballer playing for the North Melbourne Football Club in the Australian Football League (AFL).
- [d7s1]  He was drafted by North Melbourne with their third selection and thirty-sixth overall in the 2016 national draft.
- [d7s2]  He made his debut in the twenty-seven point loss to Essendon at Etihad Stadium in round eighteen of the 2017 season as a late inclusion for Robbie Tarrant.

**d8: Chris Tarrant (footballer)**

- [d8s0] Chris Tarrant (born 18 September 1980) is a former Australian footballer who played for the Collingwood Football Club, and has also played for the Fremantle Football Club.
- [d8s1]  He announced at the end of the 2010 AFL season that he would return to Melbourne for personal reasons and would not extend his contract with Fremantle for the 2011 season.
- [d8s2]  He returned to the Collingwood Football Club via a trade.
- [d8s3]  He made his name as a key forward, but upon his move to Fremantle in 2009, Tarrant found a new position in the backline.
- [d8s4]  Tarrant was noted for his spectacular high marking, athleticism and pace on a lead.

**d9: Robbie Tarrant**

- [d9s0] Robbie Tarrant (born 25 April 1989) is an Australian rules footballer who plays for the North Melbourne Football Club in the Australian Football League (AFL).
- [d9s1]  He is the younger brother of former Collingwood and Fremantle player, Chris Tarrant.

**d10: Cameron Cloke**

- [d10s0] Cameron Cloke (born 20 December 1984) is a former professional Australian rules footballer who played for the Collingwood Football Club, Carlton Football Club and Port Adelaide Football Club in the Australian Football League (AFL).
- [d10s1]  He is the son of former Richmond and Collingwood player, David Cloke and the brother of Jason and Travis Cloke.

## 3. hotpotqa_5ab679e1554299110f219a16

原位置：`train` 第 183 题 · 全局第 183 题 · `sample_id: hotpotqa_5ab679e1554299110f219a16`

Question: Graham Gold is a DJ who broadcasts live Friday nights on a radio station that also broadcasts on what around the UK?

Note: 保留旧版

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | radio station on which Graham Gold's sets broadcast live on Friday nights | False | [] | Kiss | [["d1s1"]] | context |
| u2 | what {u1} also broadcasts on around the UK | True | ["u1"] | DAB Digital Radio | [["d2s1"], ["d2s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | radio station on which Graham Gold's sets broadcast live on Friday nights | False | [] | Kiss | [['d1s1']] |
| u2 | what {u1} also broadcasts on around the UK | True | ['u1'] | DAB Digital Radio | [['d2s1'], ['d2s0']] |

### Source documents (reference only)

**d1: Graham Gold**

- [d1s0] Graham Gold (born 5 July 1954) is a British DJ.
- [d1s1]  Gold is primarily known as a DJ whose sets were broadcast live Friday nights on Kiss (UK radio station) and distributed on the Universal Music TV label.
- [d1s2]  These weekly live broadcasts were considered revolutionary in the industry.
- [d1s3]  Gold's popular weekly show played a major role in Kiss FM growing into a radio powerhouse.
- [d1s4]  Gold was ranked #83 by Dash Berlin in Dash's "Most Popular DJs in the World of All Time."

**d2: Kiss (UK radio station)**

- [d2s0] Kiss is a UK radio station which broadcasts on FM and National DAB and specialises in pop, hip hop, R&B, urban and electronic dance music.
- [d2s1]  It also broadcasts on DAB Digital Radio around the UK & nationally on Freeview, Sky and Virgin Media.
- [d2s2]  Owned by Hamburg based Bauer Media Group, Kiss forms part of Bauer's National portfolio of radio brands.
- [d2s3]  Kiss spin-off brands include Kiss TV, Kisstory and Kiss Fresh.

**d3: KBEM-FM**

- [d3s0] KBEM-FM (88.5 FM, "Jazz88") is a Minneapolis, Minnesota public radio station broadcasting a jazz format.
- [d3s1]  The station is operated by the Minneapolis public school system and has been partnering since 1989 with the Minnesota Department of Transportation (Mn/DOT), providing traffic congestion reports for commuters in the Minneapolis-St.
- [d3s2]  Paul metropolitan area.
- [d3s3]  KBEM also broadcasts live headliner performances from the Twin Cities Jazz Festival each June.
- [d3s4]  KBEM is a member of Minnesota's AMPERS network.

**d4: KQIP-LP**

- [d4s0] KQIP-LP (107.1 FM) is a radio station licensed to Chico, California, United States, the station serves the Chico area.
- [d4s1]  The station is currently owned by Calvary Chapel of Chico.
- [d4s2]  KQIP 107.1 FM is a low power FM radio station in Chico, California however it also broadcasts online.
- [d4s3]  The radio station airs Bible studies from several Calvary Chapel pastors, as well as a small selection of Christian music.
- [d4s4]  The radio station also airs Pastor Sam Allen from Calvary Chapel Chico on The Calvary Road Radio Broadcast, a weekday radio program.
- [d4s5]  Listen Live at: http://ccchico.com/KQIP

**d5: WZMF**

- [d5s0] WZMF is an AM broadcasting radio station licensed to the city of Nanticoke, Pennsylvania and serves the Wilkes-Barre, Scranton, and Hazleton radio markets with a Classic Hits format, switching from Adult Standards and Tropical and Spanish language adult contemporary format in December 2008.
- [d5s1]  The station simulcasts sister WGMF located in Tunkhannock, Pennsylvania.
- [d5s2]  WZMF broadcasts at a frequency of 730 kHz with 1,000 Watts of power during the daytime with a non-directional antenna.
- [d5s3]  During the nighttime hours, the station must reduce its power substantially to just 12 Watts which limits its listen able area to just the local Nanticoke area.
- [d5s4]  The power reduction at nighttime is required by rules set by the Federal Communications Commission in order to avoid interference from CKAC, a Canadian radio station also on 730 kHz.
- [d5s5]  WZMF also broadcasts at a frequency of 104.5 MHz with 27 Watts of power from a site atop Dewey/West Mtn near Keyser Valley/Scranton, Pennsylvania which covers Scranton, Old Forge, Avoca, Dickson City, Pittston, and Jessup, Pennsylvania.
- [d5s6]  WZMF also broadcasts at a frequency of 92.5 MHz with 250 Watts of power from a site atop Penobscot Mountain near Mountain Top, Pennsylvania which covers Wilkes-Barre, Mountain Top, Wyoming, Nanticoke, Hazleton, Dallas, West Pittston, and Kingston, Pennsylvania.

**d6: Q102.9**

- [d6s0] Q102.9, "Northwest's Best Music", is a radio station based in Derry, County Londonderry.
- [d6s1]  It broadcasts on FM 102.9 to the north west of Northern Ireland, Q102 also broadcasts via DAB (Digital Radio) throughout Northern Ireland via the Score NI multiplex.
- [d6s2]  It is part of the Q Radio Network, which also owns a number of other stations in Northern Ireland.
- [d6s3]  The station also broadcasts to parts of County Donegal, chiefly Inishowen and East Donegal.

**d7: Yle Radio Suomi**

- [d7s0] Yle Radio Suomi is a Finnish radio station owned by Yleisradio (Yle).
- [d7s1]  Radio Suomi is oriented towards sports and music, but also broadcasts a mixture of other programmes, including news and contact programmes.
- [d7s2]  The station also broadcasts music festivals.
- [d7s3]  In addition, regional stations produce programmes for Radio Suomi.

**d8: Hawkesbury Radio**

- [d8s0] Hawkesbury Radio (call sign: 2VTR) was a fully licensed community radio station.
- [d8s1]  Its primary purpose is to serve the residents of the Australian City of Hawkesbury.
- [d8s2]  Hawkesbury Radio broadcasts on the frequency 89.9 FM.
- [d8s3]  The station is staffed by volunteers and broadcasts live non-stop.
- [d8s4]  Hawkesbury Radio was the only Community Radio Station in Australia to have Broadcast rights of NRL which featured Penrith Panthers NRL matches, from 1997 to 2009.
- [d8s5]  In 2016 the station gained broadcast rights to Western Sydney Wanderers A-League matches as well as W-League, National Youth League and FFA Cup matches involving the Wanderers

**d9: CIUT-FM**

- [d9s0] CIUT-FM is a campus and community radio station owned and operated by the University of Toronto.
- [d9s1]  The station broadcasts live and continuously from Toronto on the 89.5 FM frequency.
- [d9s2]  Programming can also be heard nationally via channel 826 on Shaw Direct, and over the internet via the CIUT website.
- [d9s3]  The station is financially supported by donations and an undergraduate student levy.
- [d9s4]  CIUT-FM also broadcasts a Punjabi and Urdu language station, Sur Sagar Radio on a Subsidiary Communications Multiplex Operation frequency.

**d10: WAJM**

- [d10s0] WAJM, assigned to 88.9 FM and licensed to Atlantic City, New Jersey, is a high school radio station owned by the Atlantic City Board of Education and is operated by the students of Atlantic City High School.
- [d10s1]  Currently, WAJM broadcasts live Monday thru Friday from 7:00am to 3:30pm and during after hours, on weekends, holidays and when Atlantic City High School is closed due to inclement weather the station operates on an automated system where music, station IDs and PSA are shuffled and broadcast on-air.
- [d10s2]  Starting at its inception WAJM had been broadcasting with a jazz radio format until 2009 when it flipped to a freeform radio format using the moniker 88.9 The Jam.
- [d10s3]  The studios, offices and transmitter are located on the campus of Atlantic City High School on North Albany Avenue in Atlantic City.
- [d10s4]  In 2009 WAJM began simulcasting its live and automated broadcasts via the Internet in both an audio only feed and audio/video feed.
- [d10s5]  The station was a creation of Mr.Norman Draper.
- [d10s6]  The first school year of on air broadcasting was 1996-97.
- [d10s7]  That year the students interviewed "Sugar" Ray Leonard, and did a live simulcast from the grand opening of the new Atlantic City Convention Center.

## 4. hotpotqa_5ab781f255429928e1fe3862

原位置：`train` 第 184 题 · 全局第 184 题 · `sample_id: hotpotqa_5ab781f255429928e1fe3862`

Question: Did School of Fish and The Commuters perform music in the same genre?

Note: 

Type: comparison · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | genre of School of Fish | False | [] | alternative rock | [["d4s0"]] | context |
| u2 | genre of The Commuters | False | [] | alternative rock | [["d5s0"]] | context |
| u3 | whether School of Fish and The Commuters performed music in the same genre | True | ["u1", "u2"] | yes | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | music genre of School of Fish | False | [] | alternative rock | [['d4s0']] |
| u2 | music genre of The Commuters | False | [] | alternative rock | [['d5s0']] |
| u3 | whether School of Fish and The Commuters performed music in the same genre | True | ['u1', 'u2'] | yes | [[]] |

### Source documents (reference only)

**d1: Singing**

- [d1s0] Singing is the act of producing musical sounds with the voice and augments regular speech by the use of sustained tonality, rhythm, and a variety of vocal techniques.
- [d1s1]  A person who sings is called a singer or vocalist.
- [d1s2]  Singers perform music (arias, recitatives, songs, etc.) that can be sung with or without accompaniment by musical instruments. Singing is often done in an ensemble of musicians, such as a choir of singers or a band of instrumentalists.
- [d1s3]  Singers may perform as soloists, or accompanied by anything from a single instrument (as in art song or some jazz styles) up to a symphony orchestra or big band.
- [d1s4]  Different singing styles include art music such as opera and Chinese opera, Hindustani music, and religious music styles such as gospel, traditional music styles, world music, jazz, blues, gazal and popular music styles such as pop, rock, electronic dance music, and filmi

**d2: Music technology (mechanical)**

- [d2s0] Mechanical music technology is the use of any device, mechanism, machine or tool by a musician or composer to make or perform music; to compose, notate, play back or record songs or pieces; or to analyze or edit music.
- [d2s1]  The earliest known applications of technology to music was prehistoric peoples' use of a tool to hand-drill holes in bones to make simple flutes.
- [d2s2]  Ancient Egyptians developed stringed instruments, such as harps, lyres and lutes, which required making thin strings and some type of peg system for adjusting the pitch of the strings.
- [d2s3]  Ancient Egyptians also used wind instruments such as double clarinets and percussion instruments such as cymbals.
- [d2s4]  In Ancient Greece, instruments included the double-reed aulos and the lyre.
- [d2s5]  Numerous instruments are referred to in the Bible, including the horn, pipe, lyre, harp, and bagpipe.
- [d2s6]  During Biblical times, the cornet, flute, horn, organ, pipe, and trumpet were also used.
- [d2s7]  During the Middle Ages, hand-written music notation was developed to write down the notes of religious Plainchant melodies; this notation enabled the Catholic church to disseminate the same chant melodies across its entire empire.

**d3: School Bands in Singapore**

- [d3s0] School Bands in Singapore are made up of student in the band CCA who perform music together with their respective instruments.
- [d3s1]  In Singapore, the school band is a Co-Curriculum Activity (CCA) that can typically be found in Primary schools, Secondary schools, and Junior colleges.
- [d3s2]  Being outside classroom school activities, CCAs act as an integral part of the students’ holistic, well-rounded education, and are aimed at nurturing student qualities, and preparing them to adapt and thrive in a rapidly changing world.
- [d3s3]  As with other CCAs, the programmes in Singapore school bands follow the Ministry of Education (MOE)’s CCAs guiding principles of building team spirit and responsibility, being broad based with opportunities to specialize, being responsive to inculcating national values and skills, as well as promoting social integration.

**d4: School of Fish**

- [d4s0] School of Fish was an alternative rock band which formed in 1989 and disbanded in 1994.
- [d4s1]  The core members were Josh Clayton-Felt (lead vocals and guitar) and Michael Ward (guitar).
- [d4s2]  School of Fish released two albums and are remembered for the hit single "3 Strange Days" (1991).

**d5: The Commuters**

- [d5s0] The Commuters are an American alternative rock band from Manhattan, New York.
- [d5s1]  The group was formed in 2010 by singer, songwriter and musician Zeeshan Zaidi.
- [d5s2]  The band released their first full length album "Rescue" on April 17, 2012 on the Communal Records label.

**d6: The Philharmonic Orchestra**

- [d6s0] The Philharmonic Orchestra (TPO) is an amateur orchestra in Singapore, initiated as a project by Maestro Lim Yau in 1998.
- [d6s1]  The orchestra consists of adults who have a keen and serious interest to perform music.
- [d6s2]  Formerly known as the Philharmonic Chamber Orchestra Society (PCOS), the group became The Philharmonic Orchestra (TPO) to better reflect its intention to perform both symphonic and chamber works.

**d7: Music software**

- [d7s0] Music software is software used for musical composition, digital recording, the creation of electronic music, and other musical applications.
- [d7s1]  Music software has been around for nearly 40 years.
- [d7s2]  It has been seen to have profound impacts on education involving music and creative expression.
- [d7s3]  Musical software has become an outlet for people who do not bond with traditional musical instruments, giving people new and creative ways to compose and perform music in ways that has never been seen before.

**d8: Hoketus**

- [d8s0] Hoketus was an amplified musical ensemble founded by Dutch composer Louis Andriessen in the Netherlands in 1976.
- [d8s1]  The group was originally formed to perform Louis Andriessen's minimal composition "Hoketus", but remained together and began to perform music composed for the group by other composers (many of whom came from within the group's ranks).
- [d8s2]  The group disbanded in 1987.

**d9: Choir**

- [d9s0] A choir ( ) (also known as a quire, chorale or chorus) is a musical ensemble of singers.
- [d9s1]  Choral music, in turn, is the music written specifically for such an ensemble to perform.
- [d9s2]  Choirs may perform music from the classical music repertoire, which spans from the Medieval era to the present, or popular music repertoire.
- [d9s3]  Most choirs are led by a conductor, who leads the performances with arm and face gestures.

**d10: Music of Remembrance**

- [d10s0] Music of Remembrance is a classical music ensemble based in Seattle whose purpose is to find and perform music composed by victims of The Holocaust, irrespective of their background, as well as to perform related newly commissioned works.

## 5. hotpotqa_5ab7f9b65542991d322237f0

原位置：`train` 第 185 题 · 全局第 185 题 · `sample_id: hotpotqa_5ab7f9b65542991d322237f0`

Question: Metro Broadcast s a wholly owned subsidiary of a company that has its executive office in which city ?

Note: 

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | parent company of Metro Broadcast | False | [] | WPP plc | [["d9s1"]] | context |
| u2 | city where {u1} has its executive office | True | ["u1"] | Dublin | [["d4s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | company of which Metro Broadcast is a wholly owned subsidiary | False | [] | WPP plc | [['d9s1']] |
| u2 | city in which {u1} has its executive office | True | ['u1'] | Dublin | [['d4s0']] |

### Source documents (reference only)

**d1: Johnsonburg, Kane, Warren and Irvine Railroad**

- [d1s0] The Johnsonburg, Kane, Warren and Irvine Railroad (reporting mark JKWI) was a railroad company in Pennsylvania, United States, formed on May 24, 1982, by Sloan Cornell who also owned the Knox and Kane Railroad.
- [d1s1]  The JKWI was the designated operator of the Irvine, Warren, Kane & Johnsonburg Railroad, that was a partnership of Brock Railroad (a wholly owned subsidiary of Warren Car Company), Irvine Railroad (a wholly owned subsidiary of National Forge Company) and Struthers Wells Inter-American Corporation (a subsidiary of Struthers Wells), all three being Pennsylvania corporations, and had acquired from Conrail the following railroad line segments: MP 58.52 to MP 66.7 (Irvine to Warren) and MP 92.5 to MP 111.0 (Kane to Johnsonburg).

**d2: John Hancock Financial**

- [d2s0] John Hancock Financial is an informal term for a United States insurance company which existed, in various forms, from its founding on April 21, 1862, until its acquisition in 2004 by the Canadian insurance company Manulife Financial.
- [d2s1]  It was named in honor of John Hancock, a prominent Patriot.
- [d2s2]  The company continues to operate as a wholly owned subsidiary of Manulife and its headquarters remains in Boston, Massachusetts.
- [d2s3]  John Hancock Financial Network (JHFN) is the retail distribution company of John Hancock Life Insurance Company, U.S.A., which is a wholly owned subsidiary of Manulife Financial Corporation.

**d3: Murrin Murrin Joint Venture**

- [d3s0] The Murrin Murrin Joint Venture is a major nickel-cobalt mining operation being conducted in the North Eastern Goldfields, approximately 45 km east of Leonora, Western Australia.
- [d3s1]  The Project was a joint venture between Murrin Murrin Holdings Pty Ltd, a wholly owned subsidiary of Minara Resources Ltd (whose share is 60%) and Glenmurrin Pty Ltd, a wholly owned subsidiary of Glencore International AG, which had a 40% share but also owned 70% of Minara.
- [d3s2]  As of November 2011, Minara Resources was fully acquired and is now wholly owned by Glencore International.
- [d3s3]  The mine opened in 1999.

**d4: WPP plc**

- [d4s0] WPP plc, (Wire and Plastic Products) is a British multinational advertising and public relations company with its main management office in London, England, and its executive office in Dublin, Ireland.
- [d4s1]  It owns a number of advertising, public relations and market research networks, including IMRB, Millward Brown, Grey, Burson-Marsteller, Hill & Knowlton, JWT, Ogilvy & Mather, TNS, Young & Rubicam and Cohn & Wolfe.

**d5: Millennium Pharmaceuticals**

- [d5s0] Millennium Pharmaceuticals, Inc., The Takeda Oncology Company was a leading biopharmaceutical company based in Cambridge, Massachusetts.
- [d5s1]  Millennium has gradually been absorbed by its parent Takeda and renamed Takeda Oncology.
- [d5s2]  The Company marketed Velcade (bortezomib) for injection, a cancer product, and has a growing clinical development pipeline of product candidates.
- [d5s3]  Millennium's research, development and commercialization activities focused in two therapeutic areas: oncology and inflammation.
- [d5s4]  By applying its knowledge of the human genome, understanding of disease mechanisms and industrialized drug discovery platform, Millennium developed a line of new product candidates.
- [d5s5]  It was one of the first companies to systematically search for genes linked to disease, but none of the drugs which it is marketing or has in clinical trial, with one partial exception, have been the results of that research.
- [d5s6]  On May 14, 2008, Japanese company Takeda Pharmaceutical announced the completion of its acquisition of Millennium for US$25.00 per share in cash—a deal worth $8.8 billion.
- [d5s7]  Takeda completed the acquisition through a tender offer and subsequent merger of a wholly owned subsidiary of Takeda into Millennium.
- [d5s8]  Millennium is now a wholly owned subsidiary of Takeda.

**d6: Fuqi International**

- [d6s0] Fuqi International (formerly traded as NASDAQ: FUQI ) is a designer of precious metal (gold and platinum) jewelry for the luxury goods market in China.
- [d6s1]  It also manufactures jewelry items that contain diamonds and other precious stones on a custom-order basis.
- [d6s2]  Fuqi is a Delaware corporation with its principal executive office located in Shenzen, China.
- [d6s3]  Fuqi operates through its wholly owned subsidiary, Fuqi International Holdings Co., Ltd., a British Virgin Islands corporation and its wholly owned subsidiary, Shenzhen Fuqi Jewelry Co., Ltd., a company established under the laws of China.

**d7: Braun (company)**

- [d7s0] Braun GmbH ( ; ] ), formerly Braun AG, is a German consumer products company based in Kronberg.
- [d7s1]  From 1984 until 2007, Braun was a wholly owned subsidiary of The Gillette Company, which had purchased a controlling interest in the company in 1967.
- [d7s2]  Braun is now a wholly owned subsidiary of Procter & Gamble, which acquired Gillette in 2005.
- [d7s3]  On 16 April 2012, De'Longhi bought perpetual rights to manufacture Braun branded products from Procter & Gamble in the small appliance segment.
- [d7s4]  Procter & Gamble will continue to own the Braun brand.

**d8: Sun Hung Kai Financial**

- [d8s0] Sun Hung Kai Financial Limited (SHKFL), is a 70%-owned subsidiary of Everbright Securities Company Limited (SSE: 601788, HKEX: 6178, “Everbright Securities”).
- [d8s1]  With its foundation dating back to 1969 when Fung King Hey, Kwok Tak Seng and Lee Shau Kee teamed up to start the Sun Hung Kai partnership, SHKFL was a wholly owned subsidiary of Sun Hung Kai & Co. Limited (SEHK: 86,　“SHKCO”).
- [d8s2]  SHKCO is chaired by Lee Seng Huang and controlled by the Lee & Lee Trust following the acquisition of the Fung family’s equity interest in the company by Allied Properties (H.K.) Limited via its wholly owned subsidiary in 1996.
- [d8s3]  In June 2015, Everbright Securities acquired 70% of SHKFL from SHKCO, making SHKFL a subsidiary of Everbright Securities since then.
- [d8s4]  SHKCO remains a 30% shareholder of SHKFL.

**d9: Metro Broadcast**

- [d9s0] Metro Broadcast Ltd. is a UK-based corporate event supplier with its Head Office in London and a satellite operation in Scotland with offices in Edinburgh, Glasgow and Aberdeen.
- [d9s1]  The company is a wholly owned subsidiary of WPP plc.

**d10: Copperweld Corp. v. Independence Tube Corp.**

- [d10s0] Copperweld Corp. v. Independence Tube Corp., 467 U.S. 752 (1984) , is a major US antitrust law case decided by the Supreme Court concerning the Pittsburgh firm Copperweld Corporation and the Chicago firm Independence Tube.
- [d10s1]  It that held that a parent company is incapable of conspiring with its wholly owned subsidiary for purposes of Section 1 of the Sherman Act because they cannot be considered separate economic entities.
- [d10s2]  Section 1 of the Sherman Act states that "Every contract, combination in the form of trust or otherwise, or conspiracy, in restraint of trade or commerce among the several States, or with foreign nations, is declared to be illegal."
- [d10s3]  However, for a condition of conspiracy to exist, there must be at least two parties involved.
- [d10s4]  "Copperweld" held that separate incorporation was not enough to render a parent and its subsidiary capable of conspiring, since forcibly the economic interests of a wholly owned subsidiary must be those of its parent.
- [d10s5]  It does not apply to partially owned subsidiaries.

## 6. hotpotqa_5ab8292c55429934fafe6cfe

原位置：`train` 第 186 题 · 全局第 186 题 · `sample_id: hotpotqa_5ab8292c55429934fafe6cfe`

Question: Anna Ranch Heritage Center is a former cattle ranch in a census-designated place with a population of what in 2010?

Note: 是否可以按照原题的方法拆分

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | census-designated place in which the former cattle ranch Anna Ranch Heritage Center is located | False | [] | Waimea, Hawaii County, Hawaii | [["d3s0"]] | context |
| u2 | population of {u1} in 2010 | True | ["u1"] | 9,212 | [["d7s1"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | census-designated place in which the former cattle ranch Anna Ranch Heritage Center is located | False | [] | Waimea, Hawaii County, Hawaii | [['d3s0']] |
| u2 | population of {u1} in 2010 | True | ['u1'] | 9,212 | [['d7s1']] |

### Source documents (reference only)

**d1: Amargosa, Texas**

- [d1s0] Amargosa is an unincorporated community and census-designated place in Jim Wells County, Texas, United States.
- [d1s1]  Its population was 291 as of the 2010 census.
- [d1s2]  Prior to 2010, the community was grouped with nearby Owl Ranch as part of the Owl Ranch-Amargosa census-designated place.
- [d1s3]  The community is named for the Amargosa Creek that runs nearby.
- [d1s4]  The word "amargosa" means "bitter" in Spanish.

**d2: Stevenson Ranch, California**

- [d2s0] Stevenson Ranch is a census-designated place in Los Angeles County, California.
- [d2s1]  The community is located in the Santa Clarita Valley.
- [d2s2]  Often incorrectly referred to as part of the city of Santa Clarita, the community does not actually fall within the Santa Clarita city limits and is instead in an unincorporated area.
- [d2s3]  Stevenson Ranch encompasses about 6.4 mi2 .
- [d2s4]  About 1000 acre are set aside as parks, recreation areas, and open space.
- [d2s5]  Stevenson Ranch is set in the foothills of the Santa Susana Mountains and lies west of Interstate 5.
- [d2s6]  This area backs up to the historic, oil-mining town of Mentryville, founded in 1875.
- [d2s7]  A master-planned community, it was approved by the county in 1987.
- [d2s8]  The population was 17,557 at the time of the 2010 census.

**d3: Anna Ranch Heritage Center**

- [d3s0] Anna Ranch Heritage Center is a former cattle ranch in Waimea, Hawaii County, Hawaii named for Anna Leialoha Lindsey Perry-Fiske (1900–1995).

**d4: Owl Ranch, Texas**

- [d4s0] Owl Ranch is an unincorporated community and census-designated place in Jim Wells County, Texas, United States.
- [d4s1]  Its population was 225 as of the 2010 census.
- [d4s2]  Prior to 2010, the community was grouped with nearby Amargosa as part of the Owl Ranch-Amargosa census-designated place.

**d5: Burnt Ranch, California**

- [d5s0] Burnt Ranch is a census-designated place (CDP) in Trinity County, California.
- [d5s1]  It has a school and a post office.
- [d5s2]  The ZIP Code is 95527.
- [d5s3]  The community is inside area code 530.
- [d5s4]  Burnt Ranch sits at an elevation of 1502 ft .
- [d5s5]  The 2010 United States census reported Burnt Ranch's population was 281.

**d6: Forest Ranch, California**

- [d6s0] Forest Ranch is a census-designated place in Butte County, California.
- [d6s1]  It includes Forest Ranch Elementary School (K-6), its own post office, and a CDF fire station.
- [d6s2]  The community's ZIP code is 95942, and is shared with the community of Butte Meadows.
- [d6s3]  The area code is 530.
- [d6s4]  Forest Ranch's population was 1,184 at the 2010 census.

**d7: Waimea, Hawaii County, Hawaii**

- [d7s0] Waimea is a census-designated place (CDP) in Hawaiʻ i County, Hawaiʻ i, United States.
- [d7s1]  The population was 7,028 at the 2000 census and 9,212 at the 2010 census.
- [d7s2]  Since each U.S. state cannot have more than one post office of the same name, and there is a post office in Waimea, Kauai County, the official US Post Office name for Waimea is Kamuela.

**d8: La Tina Ranch, Texas**

- [d8s0] La Tina Ranch is a census-designated place (CDP) in Cameron County, in the U.S. state of Texas.
- [d8s1]  The population was 618 at the 2010 census.
- [d8s2]  Prior to the 2010 census the community was part of the Arroyo Gardens-La Tina Ranch CDP.
- [d8s3]  It is part of the Brownsville–Harlingen Metropolitan Statistical Area.

**d9: Chesapeake Ranch Estates, Maryland**

- [d9s0] The Chesapeake Ranch Estates (CRE), also known locally as the Ranch Club, is located in Lusby, Maryland, in southern Calvert County.
- [d9s1]  CRE was founded in 1958 and is governed by a homeowners' association, which is officially called the "Property Owner's Association of the Chesapeake Ranch Estates" (POACRE).
- [d9s2]  Today, CRE is composed of over 4,000 homes.
- [d9s3]  The community is counted as a census-designated place for population statistics, with a residential population of 10,519 as of the 2010 census.
- [d9s4]  At the 2000 census, the area was part of the Chesapeake Ranch Estates-Drum Point CDP.

**d10: Highlands Ranch, Colorado**

- [d10s0] Highlands Ranch is a census-designated place (CDP) in Douglas County, Colorado, United States.
- [d10s1]  The population was 96,713 at the 2010 census.
- [d10s2]  Located 12 miles south of Denver, Highlands Ranch is an unincorporated community and was the twelfth most populous CDP in the United States in 2010.

## 7. hotpotqa_5ab8f1ae55429916710eb0c8

原位置：`train` 第 187 题 · 全局第 187 题 · `sample_id: hotpotqa_5ab8f1ae55429916710eb0c8`

Question: Banks are subject to minimum capital requiremets based on what banking regulation recommendations issued by the Basel COmmittee on Banking Supervision? 

Note: 这样的题目采用旧版，让模型可以先说一部分事实

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | international set of capital standards on which banks' minimum capital requirements are based | False | [] | Basel Accords | [["d1s3"]] | context |
| u2 | banking regulation recommendations issued by the Basel Committee on Banking Supervision, given {u1} | True | ["u1"] | Basel Accords | [["d8s0"], ["d10s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | international set of capital standards on which banks' minimum capital requirements are based | False | [] | Basel Accords | [['d1s3']] |
| u2 | banking regulation recommendations issued by the Basel Committee on Banking Supervision, given {u1} | True | ['u1'] | Basel Accords | [['d8s0'], ['d10s0']] |

### Source documents (reference only)

**d1: Bank**

- [d1s0] A bank is a financial institution that accepts deposits from the public and creates credit.
- [d1s1]  Lending activities can be performed either directly or indirectly through capital markets. Due to their importance in the financial stability of a country, banks are highly regulated in most countries.
- [d1s2]  Most nations have institutionalized a system known as fractional reserve banking under which banks hold liquid assets equal to only a portion of their current liabilities.
- [d1s3]  In addition to other regulations intended to ensure liquidity, banks are generally subject to minimum capital requirements based on an international set of capital standards, known as the Basel Accords.

**d2: Basel III**

- [d2s0] Basel III (or the Third Basel Accord) is a global, voluntary regulatory framework on bank capital adequacy, stress testing, and market liquidity risk.
- [d2s1]  It was agreed upon by the members of the Basel Committee on Banking Supervision in 2010–11, and was scheduled to be introduced from 2013 until 2015; however, changes from 1 April 2013 extended implementation until 31 March 2018 and again extended to 31 March 2019.
- [d2s2]  The third installment of the Basel Accords ("see Basel I, Basel II") was developed in response to the deficiencies in financial regulation revealed by the financial crisis of 2007–08.
- [d2s3]  Basel III is intended to strengthen bank capital requirements by increasing bank liquidity and decreasing bank leverage.

**d3: Tier 2 capital**

- [d3s0] Tier 2 capital, or supplementary capital, includes a number of important and legitimate constituents of a bank's capital base.
- [d3s1]  These forms of banking capital were largely standardized in the Basel I accord, issued by the Basel Committee on Banking Supervision and left untouched by the Basel II accord.
- [d3s2]  National regulators of most countries around the world have implemented these standards in local legislation.
- [d3s3]  In the calculation of regulatory capital, Tier 2 is limited to 100% of Tier 1 capital.

**d4: Basel I**

- [d4s0] Basel I is the round of deliberations by central bankers from around the world, and in 1988, the Basel Committee on Banking Supervision (BCBS) in Basel, Switzerland, published a set of minimum capital requirements for banks.
- [d4s1]  This is also known as the 1988 Basel Accord, and was enforced by law in the Group of Ten (G-10) countries in 1992.
- [d4s2]  A new set of rules known as Basel II was later developed with the intent to supersede the Basel I accords.
- [d4s3]  However they were criticized by some for allowing banks to take on additional types of risk, which was considered part of the cause of the US subprime financial crisis that started in 2008.
- [d4s4]  In fact, bank regulators in the United States took the position of requiring a bank to follow the set of rules (Basel I or Basel II) giving the more conservative approach for the bank.
- [d4s5]  Because of this it was anticipated that only the few very largest US banks would operate under the Basel II rules, the others being regulated under the Basel I framework.
- [d4s6]  Basel III was developed in response to the financial crisis; it does not supersede either Basel I or II , but focuses on different issues primarily related to the risk of a bank run.

**d5: Net stable funding ratio**

- [d5s0] During the financial crisis of 2007–2008, several banks, including the UK's Northern Rock and the U.S. investment banks Bear Stearns and Lehman Brothers, suffered a liquidity crisis, due to their over-reliance on short-term wholesale funding from the interbank lending market.
- [d5s1]  As a result, the G20 launched an overhaul of banking regulation known as Basel III.
- [d5s2]  In addition to changes in capital requirements, Basel III also contains two entirely new liquidity requirements: the net stable funding ratio (NSFR) and the liquidity coverage ratio (LCR).
- [d5s3]  On October 31, 2014, the Basel Committee on Banking Supervision issued its final Net Stable Funding Ratio (it was initially proposed in 2010 and re-proposed in January 2014).

**d6: Risk-weighted asset**

- [d6s0] Risk-weighted asset (also referred to as RWA) is a bank's assets or off-balance-sheet exposures, weighted according to risk.
- [d6s1]  This sort of asset calculation is used in determining the capital requirement or Capital Adequacy Ratio (CAR) for a financial institution.
- [d6s2]  In the Basel I accord published by the Basel Committee on Banking Supervision, the Committee explains why using a risk-weight approach is the preferred methodology which banks should adopt for capital calculation.

**d7: Basel Committee on Banking Supervision**

- [d7s0] The Basel Committee on Banking Supervision (BCBS) is a committee of banking supervisory authorities that was established by the central bank governors of the Group of Ten countries in 1974.
- [d7s1]  It provides a forum for regular cooperation on banking supervisory matters.
- [d7s2]  Its objective is to enhance understanding of key supervisory issues and improve the quality of banking supervision worldwide.
- [d7s3]  The Committee frames guidelines and standards in different areas – some of the better known among them are the international standards on capital adequacy, the Core Principles for Effective Banking Supervision and the Concordat on cross-border banking supervision.
- [d7s4]  The Committee's Secretariat is located at the Bank for International Settlements (BIS) in Basel, Switzerland.
- [d7s5]  However, the BIS and the Basel Committee remain two distinct entities.

**d8: Basel Accords**

- [d8s0] The Basel Accords (see alternative spellings below) refer to the banking supervision Accords (recommendations on banking regulations)—Basel I, Basel II and Basel III—issued by the Basel Committee on Banking Supervision (BCBS).

**d9: Minimum capital**

- [d9s0] Minimum capital is a concept used in corporate law and banking regulation to stipulate what assets the organisation must hold as a minimum requirement.
- [d9s1]  The purpose of minimum capital in corporate law is to ensure that in the event of insolvency or financial instability, the corporation has a sufficient asset base to satisfy the claims of creditors.

**d10: Basel II**

- [d10s0] Basel II is the second of the Basel Accords, (now extended and partially superseded by Basel III), which are recommendations on banking laws and regulations issued by the Basel Committee on Banking Supervision.

## 8. hotpotqa_5ab95b28554299743d22eb09

原位置：`train` 第 188 题 · 全局第 188 题 · `sample_id: hotpotqa_5ab95b28554299743d22eb09`

Question: Jack and Jill and Forbes are both what?

Note: 参照原版

Type: comparison · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | what Jack and Jill is | False | [] | magazine | [["d5s0"]] | context |
| u2 | what Forbes is | False | [] | magazine | [["d3s0"]] | context |
| u3 | what Jack and Jill and Forbes both are | True | ["u1", "u2"] | magazine | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | what Jack and Jill is | False | [] | magazine | [['d5s0']] |
| u2 | what Forbes is | False | [] | magazine | [['d3s0']] |
| u3 | what Jack and Jill and Forbes both are | True | ['u1', 'u2'] | magazine | [[]] |

### Source documents (reference only)

**d1: Eric Stephens (comics)**

- [d1s0] Eric Stephens (1909–2001) was a British comic strip artist who contributed to "Jack and Jill", drawing episodes of the cover strip 'Jack and Jill of Buttercup Farm' and colouring a number of centre-spread features such as 'There Was An Old Woman Who Lived in a Shoe' and 'Our Village'.
- [d1s1]  Stephens also contributed episodes of 'Sonny and Sally' to "Playhour" and 'Paddington Park' to "Bonnie".

**d2: Jack Horner (comics)**

- [d2s0] Jack Horner is a fictional character in the comic book series "Fables" by Bill Willingham.
- [d2s1]  His first appearance was in issue #1 of "Fables" and continued as a regular character of the series until leaving the series for his own title, "Jack of Fables".
- [d2s2]  The character is based on various nursery rhymes and fables with characters named Jack including "Little Jack Horner", "Jack and the Beanstalk", "Jack and Jill", Jack Be Nimble, Jack Frost, Jack O'Lantern, and Jack the Giant Killer and others.

**d3: Forbes**

- [d3s0] Forbes ( ) is an American business magazine.
- [d3s1]  Published bi-weekly, it features original articles on finance, industry, investing, and marketing topics.
- [d3s2]  "Forbes" also reports on related subjects such as technology, communications, science, politics, and law.
- [d3s3]  Its headquarters is located in Jersey City, New Jersey.
- [d3s4]  Primary competitors in the national business magazine category include "Fortune" and "Bloomberg Businessweek".
- [d3s5]  The magazine is well known for its lists and rankings, including its lists of the richest Americans (the Forbes 400) and rankings of world's top companies (the Forbes Global 2000).
- [d3s6]  Another well-known list by the magazine is The World's Billionaires list.

**d4: Mighty Jill Off**

- [d4s0] Mighty Jill Off is a 2D platform independently developed freeware video game designed by Anna Anthropy, with art by James Harvey and music by Andrew Toups.
- [d4s1]  It stars a submissive named Jill, who has a boot fetish and is forced to climb up a tower after her Queen kicks her down it as punishment.
- [d4s2]  Jill does this by jumping and slowly descending over obstacles.
- [d4s3]  Jill can be defeated in one hit by these obstacles, but will return to the last check point.
- [d4s4]  The game serves as an homage to the 1986 arcade game "Mighty Bomb Jack".
- [d4s5]  It had follow-ups, such as "Mighty Jill Off - Jill Off Harder Edition" and "Jill Off With One Hand".
- [d4s6]  Jill made a cameo appearance in the 2010 video game "Super Meat Boy" as a playable character.

**d5: Jack and Jill (magazine)**

- [d5s0] Jack and Jill is an American bimonthly magazine for children 7 to 12 years old that takes its title from the nursery rhyme of the same name.
- [d5s1]  It features stories and educational activities.

**d6: Four Jacks and a Jill**

- [d6s0] Four Jacks and a Jill is a South African folk rock ensemble.
- [d6s1]  They originally formed in 1964 without a "Jill" under the name "The Nevadas".
- [d6s2]  Subsequently, they became the first group in South Africa to wear their hair long and they changed their name to "The Zombies" (different from the well-known British group).
- [d6s3]  Later they added lead singer Glenys Lynne and changed the group's name to "Four Jacks and A Jill".
- [d6s4]  The group included Clive Harding (bass guitar), Till Hanamann (rhythm guitar, trumpet and organ), Bruce Bark (lead guitar, harmonica and saxophone), Tony Hughes (drums) and Glenys Lynne (lead vocal and organ).
- [d6s5]  In South Africa, they had a hit song, "Timothy".
- [d6s6]  In 1968 they cracked the American charts with the song "Master Jack", hitting the "Billboard" Hot 100 at no. 18 and reaching no. 3 on the Adult Contemporary chart.
- [d6s7]  The song also reached no. 10 on Cashbox and went to no. 1 in South Africa, Canada, Australia, New Zealand, Malaysia, and Rhodesia (now Zimbabwe).
- [d6s8]  The follow-up single, "Mr. Nico", peaked at no. 98 in the United States.
- [d6s9]  That was their last hit in the U.S., but the group continued to score hits in their native country.

**d7: Jack and Jill: A Village Story**

- [d7s0] Jack and Jill: A Village Story by Louisa May Alcott, is a children's book originally published in 1880.
- [d7s1]  It takes place in a small New England town after the Civil War.
- [d7s2]  The story of two good friends named Jack and Janey, "Jack and Jill" tells of the aftermath of a serious sledding accident.

**d8: Jill Jack**

- [d8s0] Jill Jack is an American singer-songwriter based in Ferndale, Michigan.
- [d8s1]  As of December 2016, she has released 11 albums, ranging from soul to rock, to folk and country.
- [d8s2]  She leads a band of the same name, as well as a jazz ensemble dedicated to standards, "Jill Jack and the American Songbook Band."

**d9: Consideration under American law**

- [d9s0] Consideration is the central concept in the common law of contracts and is required, in most cases, for a contract to be enforceable.
- [d9s1]  Consideration is the price one pays for another's promise.
- [d9s2]  It can take a number of forms: money, property, a promise, the doing of an act, or even refraining from doing an act.
- [d9s3]  In broad terms, if one agrees to do something he was not otherwise legally obligated to do, it may be said that he has given consideration.
- [d9s4]  For example, Jack agrees to sell his car to Jill for $100.
- [d9s5]  Jill's payment of $100 (or her promise to do so) is the consideration for Jack's promise to give Jill the car, and Jack's promise to give Jill the car is consideration for Jill's payment of $100.

**d10: Jack and Jill vs. the World**

- [d10s0] Jack and Jill vs. the World is a film by Vanessa Parise.
- [d10s1]  It was released on April 4, 2008 and stars Freddie Prinze Jr. and Taryn Manning as Jack and Jill.

## 9. hotpotqa_5ab9d58855429939ce03dc3a

原位置：`train` 第 189 题 · 全局第 189 题 · `sample_id: hotpotqa_5ab9d58855429939ce03dc3a`

Question: The expert mentor to the celebrities that perform on "Splash!" won the 2009 FINA World Championionship in the individual event at what age? 

Note: 

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | expert mentor to the celebrities that perform on "Splash!" | False | [] | Tom Daley | [["d2s3"]] | context |
| u2 | age at which {u1} won the 2009 FINA World Championship in the individual event | True | ["u1"] | 15 | [["d1s1"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | expert mentor to the celebrities that perform on "Splash!" | False | [] | Tom Daley | [['d2s3']] |
| u2 | age at which {u1} won the 2009 FINA World Championship in the individual event | True | ['u1'] | 15 | [['d1s1']] |

### Source documents (reference only)

**d1: Tom Daley**

- [d1s0] Thomas Robert Daley (born 21 May 1994) is a British diver.
- [d1s1]  Tom Daley specialises in the 10-metre platform event and is a double World champion in the event; he won the 2009 FINA World Championionship in the individual event at the age of 15, before regaining it in 2017.
- [d1s2]  He was the 2012 Olympic bronze medalist in the event.

**d2: Splash! (UK TV series)**

- [d2s0] Splash!
- [d2s1]  is a British television series that follows celebrities as they try to master the art of diving.
- [d2s2]  The celebrities perform each week in front of a panel of judges and a live audience in an Olympic-size diving pool with the result each week partly determined by public vote.
- [d2s3]  Gabby Logan and Vernon Kay present the show, whilst Team GB Olympic Bronze Medal winning diver Tom Daley is the expert mentor to the celebrities.
- [d2s4]  It is filmed at the Inspire: Luton Sports Village, which is based in Stopsley, Luton.
- [d2s5]  The show premiered on ITV on 5 January 2013 winning the ratings battle for its 7.15pm-8.15pm slot with an average audience of 5.6 million viewers, a network share of 23.6%, however, it was cancelled on 15 February 2014 after just two series.

**d3: Zoe Arancini**

- [d3s0] Zoe Arancini (born 14 July 1991) is an Australian club water polo player who plays driver, counter-attacker, or outside shooter.
- [d3s1]  Several of her family members have represented her country in water polo.
- [d3s2]  She plays club water polo in the National Water Polo League for the Fremantle Marlins, where she has won the league championship in 2005, 2007 and 2008 and is coached by her mother.
- [d3s3]  She has represented the country as a member of the Australia women's national water polo team on the junior and senior level, with over eighty appearances for national team between the two levels.
- [d3s4]  She has earned a gold medal at the 2011 Canada Cup, silver medals at the 2010 FINA World League Super Finals and 2010 FINA World Cup, and bronze medals at the 2009 FINA World League Super Finals and 2011 FINA Junior World Championships.
- [d3s5]  She has been included on the roster to represent the country at the 2012 Summer Olympics.

**d4: Nikitas Kocheilas**

- [d4s0] Nikitas Kocheilas (Greek: Νικήτας Κόχειλας ; born 1 March 1983) is a Greek water polo player.
- [d4s1]  As a member of Greece men's national water polo team, he won the bronze medal at the 2006 FINA World League and competed at the 2006 European Championship, the 2006 FINA World Cup and the 2008 FINA World League.
- [d4s2]  Kocheilas was also part of the Greek national team that was crowned World Champion at the 2001 Junior World Championship in Istanbul.

**d5: Eszter Tomaskovics**

- [d5s0] Eszter Anita Tomaskovics (born 23 August 1987) is an Hungarian female water polo player.
- [d5s1]  She was a member of the Hungary Women's National Team.
- [d5s2]  She was a part of the Hungarian team that claimed the gold medal at the 2005 FINA World Championship in Montreal, Canada.
- [d5s3]  She also competed in the 2007 and 2009 FINA World Championships.
- [d5s4]  At club level, she has played most notably for Vasas, Honvéd (2005–2008) and Olympiacos (2008–2010), winning numerous titles.

**d6: Alicia McCormack**

- [d6s0] Alicia McCormack (born 7 June 1983 in Helensburgh, New South Wales) is an Australian water polo goalkeeper.
- [d6s1]  Her playing career started at the age of fourteen with the Kirrawee High School water polo team, and today she plays for the Cronulla Water Polo Club in the National Water Polo League and is a member of the Australia women's national water polo team.
- [d6s2]  Although she did not play water polo in 2010 due to injury, McCormack has won gold medals at the 2006 Commonwealth Games and the 2006 FINA World Cup; a silver medal at the 2007 FINA World Championships; and bronze medals at the 2008 and 2012 Summer Olympics, 2005 FINA World League Super Finals, 2008 FINA World League Super Finals and 2009 FINA World League Super Finals.
- [d6s3]  Currently working at the New South Wales Institute of Sport, McCormack is studying for a Bachelor of Primary Education.

**d7: Major achievements in swimming by nation**

- [d7s0] This is a list of the best results achieved by athletes from different nations at four major competitions where swimming events are (or were) competed.
- [d7s1]  Results are based on major competitions according to FINA's historical records: the swimming and open water swimming events at the Olympic Games, the swimming and open water swimming events at the FINA World Aquatics Championships, the FINA Short Course Swimming World Championships and the defunct FINA World Open Water Swimming Championships.
- [d7s2]  The results listed here only refer to swimming and open water swimming events.
- [d7s3]  Medals earned by athletes from defunct NOCs or historical teams have been merged with the results achieved by their immediate successor states, as follows: Russia inherits medals from the Soviet Union and the Unified Team; Serbia inherits medals from Yugoslavia; Australia inherits medals from Australasia; and Germany inherits medals from West Germany and East Germany.
- [d7s4]  The table is pre-sorted by total number of gold medal results, silver medal results and bronze medal results, respectively.
- [d7s5]  When equal ranks are given, countries are listed in alphabetical order.

**d8: FINA World Masters Championships**

- [d8s0] The FINA World Masters Championships (or "Masters Worlds") is an international Aquatics championships for adults (per FINA rules, Masters are 25 years old and older).
- [d8s1]  The championships is held biennially, with competition in all five of FINA's disciplines: Swimming, Diving, Water polo, Open water swimming, and Synchronized swimming.
- [d8s2]  Starting in 2015, the competition will be held jointly with the FINA World Aquatics Championships.

**d9: Glencora Ralph**

- [d9s0] Glencora Ralph (born 8 August 1988) is an Australian water polo centre back/driver.
- [d9s1]  She attended the Curtin University of Technology and is a dental therapist.
- [d9s2]  She competes for the Fremantle Marlins in the National Water Polo League, and was on sides that won the league championship in 2003, 2004, 2006 and 2007.
- [d9s3]  She has been a member of the Australia women's national water polo team on the junior and senior level.
- [d9s4]  She has won gold medals at the 2011 Canada Cup and at the 2007 FINA Junior World Championships.
- [d9s5]  She won silver medals at the 2010 FINA World League Super Finals and at the 2010 FINA Women's Water Polo World Cup.
- [d9s6]  She won a bronze medal at the 2009 FINA World League Super Finals.
- [d9s7]  She was part of the Australian water polo team that won bronze at the 2012 Summer Olympics.

**d10: 2010 FINA Diving World Cup**

- [d10s0] The 2010 FINA Diving World Cup was held in Changzhou, Jiangsu, People's Republic of China from June 2 to June 6, 2010.
- [d10s1]  It was the 17th FINA Diving World Cup competition.
- [d10s2]  146 divers from 33 countries and regions competed in this World Cup.
- [d10s3]  The 2010 FINA Diving World Cup is held one year after the 2009 FINA Diving World Championships which was held in Rome.

## 10. hotpotqa_5aba9af255429901930fa856

原位置：`train` 第 190 题 · 全局第 190 题 · `sample_id: hotpotqa_5aba9af255429901930fa856`

Question: The city in which Calisto da Costa trained prior to his participation in the Sydney Olympic Games lies on which sea?

Note: 

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | city where Calisto da Costa trained prior to the Sydney Olympic Games | False | [] | Darwin | [["d4s2"]] | context |
| u2 | sea on which {u1} lies | True | ["u1"] | Timor Sea | [["d6s1"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | city in which Calisto da Costa trained prior to his participation in the Sydney Olympic Games | False | [] | Darwin | [['d4s2']] |
| u2 | sea on which {u1} lies | True | ['u1'] | Timor Sea | [['d6s1']] |

### Source documents (reference only)

**d1: Sydney Olympic Park Hockey Centre**

- [d1s0] The Sydney Olympic Park Hockey Centre, also known as the State Hockey Centre of New South Wales is a multi-use stadium in Sydney, Australia.
- [d1s1]  It was built in 1998 as part of Sydney Olympic Park sporting complex, having held matches for the field hockey events at the 2000 Summer Olympics.
- [d1s2]  Its current capacity is 8,000 people, with seating capacity for 4,000.
- [d1s3]  For the Sydney Olympic Games capacity was boosted to 15,000 through the use of temporary stands.

**d2: North Sydney Olympic Pool**

- [d2s0] The North Sydney Olympic Pool is a swimming and exercise complex located adjacent to Sydney Harbour at Milsons Point in North Sydney between the Sydney Harbour Bridge and Luna Park.
- [d2s1]  Designed by architects Rudder & Grout in the Inter-War Free Classical style with art deco-style decorations, the Olympic-sized outdoor pool was built on part of the Dorman Long workshops site following the completion of the Harbour Bridge.
- [d2s2]  The pool opened 4 April 1936 and hosted the swimming and diving events for the 1938 Empire Games.
- [d2s3]  Heating was added in 2000 and a 25m indoor pool was added in 2001.
- [d2s4]  Despite the name, it was not the aquatic venue for the 2000 Sydney Olympic Games; the aquatic events took place at the Sydney International Aquatic Centre in Sydney Olympic Park.

**d3: João Costa (sport shooter)**

- [d3s0] João Carlos Calvete Pereira da Costa (born 28 October 1964 in Luanda, Angola) is a Portuguese sports shooter who competed in the Summer Olympic Games in 2000, 2004 and 2008.
- [d3s1]  Costa has also qualified to compete in the men's 10 m air pistol event at the 2012 Summer Olympics.
- [d3s2]  In the 2012 Olympic Competition, Costa placed 8th in the qualifying round with a score of 583.
- [d3s3]  He placed 7th after the final with a combined score of 682.3.

**d4: Calisto da Costa**

- [d4s0] Calisto da Costa (born 6 February 1979) is a East Timorese athlete.
- [d4s1]  He was one of the first athletes to represent East Timor at the Olympic Games, when he competed at the Men's Marathon at the 2000 Summer Olympics in Sydney, though he technically competed as an individual athlete because East Timor was newly independent and had not yet been formally recognized by the International Olympic Committee.
- [d4s2]  Costa was one of the ten East Timorese athletes who received training in Darwin, Northern Territory prior to his participation in the Sydney Olympic Games.
- [d4s3]  He finished in 71st place at 2:33:11.

**d5: Stadium Australia**

- [d5s0] Stadium Australia, commercially known as ANZ Stadium and formerly as Telstra Stadium, is a multi-purpose stadium located in the Sydney Olympic Park, in Sydney, Australia.
- [d5s1]  The stadium, which in Australia is sometimes referred to as Sydney Olympic Stadium, Homebush Stadium or simply as the Olympic Stadium, was completed in March 1999 at a cost of A$690 million to host the 2000 Summer Olympics.
- [d5s2]  The current chairman of the stadium's Advisory Board is Robert Webster.
- [d5s3]  Every year since the stadium was built, the New South Wales rugby league team's home games in the State of Origin series have been played there.
- [d5s4]  Also the stadium has since hosted the annual National Rugby League grand final.
- [d5s5]  ANZ Stadium also hosted the 2003 Rugby World Cup finals and Bledisloe Cup matches, regular Sydney Swans and Greater Western Sydney Giants AFL matches, as well as international soccer matches featuring Australia's national team the Socceroos, and exhibition games by Sydney-based A-League team Sydney FC.
- [d5s6]  The stadium also hosted the 2015 AFC Asian Cup final.

**d6: Darwin, Northern Territory**

- [d6s0] is the capital city of the Northern Territory of Australia.
- [d6s1]  Situated on the Timor Sea, Darwin is the largest city in the sparsely populated Northern Territory, with a population of 142,300.
- [d6s2]  It is the smallest and most northerly of the Australian capital cities, and acts as the Top End's regional centre.

**d7: Stéphane Da Costa**

- [d7s0] Stéphane Da Costa (born 11 July 1989) is a French-Polish professional ice hockey player currently an unrestricted free agent.
- [d7s1]  He most recently played for CSKA Moscow of the Kontinental Hockey League (KHL).
- [d7s2]  Born in France, Da Costa moved to the United States as a junior to develop as a player.
- [d7s3]  After junior, Da Costa moved on to NCAA collegiate hockey, playing two seasons with Merrimack College.
- [d7s4]  He then signed as a free agent with the National Hockey League (NHL)'s Ottawa Senators in 2011, and played three seasons in the organization, including 47 games with Ottawa.
- [d7s5]  In 2014, he left the organization as a free agent, signing with CSKA Moscow.

**d8: Sydney Olympic Park**

- [d8s0] Sydney Olympic Park is a large sports and entertainment complex in western Sydney.
- [d8s1]  It is also an official suburb of Sydney, commonly known as Olympic Park but officially named Sydney Olympic Park.
- [d8s2]  Sydney Olympic Park is located 16 kilometres west of the Sydney central business district, in the local government area of City of Parramatta.

**d9: Victor Ramos (boxer)**

- [d9s0] Victor Ramos (born 14 April 1970) is a retired East Timorese boxer.
- [d9s1]  He was one of the first athletes to represent East Timor at the Olympic Games, when he competed at the Men's lightweight Boxing event at the 2000 Summer Olympics in Sydney, though he technically competed as an individual athlete because East Timor was newly independent and had not yet been formally recognized by the International Olympic Committee.
- [d9s2]  He was also the flag bearer for the Independent Olympians at the 2000 Summer Olympics.
- [d9s3]  Ramos was one of the ten East Timorese athletes who received training in Darwin prior to his participation in the Sydney Olympic Games.
- [d9s4]  However, he lost in round 1 against Ghanaian boxer Raymond Narh and did not advance any further.

**d10: Lucina da Costa Gomez-Matheeuws**

- [d10s0] Lucina Elena da Costa Gomez-Matheeuws (5 April 1929 – 7 January 2017) was a Dutch Antillean politician for the National People's Party (PNP).
- [d10s1]  She served as the Prime Minister of the Netherlands Antilles, an office her husband Moises Frumencio da Costa Gomez previously held, briefly in 1977.
- [d10s2]  She was also the first female to hold the office.
- [d10s3]  Prior to this, she was the Minister of Health and Environment, Welfare, Youth, Sports, Culture and Recreation (1970–1977).

## 11. hotpotqa_5abb155c55429966062416c8

原位置：`train` 第 191 题 · 全局第 191 题 · `sample_id: hotpotqa_5abb155c55429966062416c8`

Question: The narrator for "Pound Shop Wars" also narrated what Channel 4 reality television series from its inception in 2013 until April 2016?

Note: 

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | narrator of "Pound Shop Wars" | False | [] | Caroline Aherne | [["d9s1"]] | context |
| u2 | Channel 4 reality television series narrated by {u1} from 2013 to April 2016 | True | ["u1"] | Gogglebox | [["d3s1"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | narrator of "Pound Shop Wars" | False | [] | Caroline Aherne | [['d9s1']] |
| u2 | Channel 4 reality television series {u1} narrated from its inception in 2013 until April 2016 | True | ['u1'] | Gogglebox | [['d3s1']] |

### Source documents (reference only)

**d1: Chantelle Houghton**

- [d1s0] Chantelle Vivien Houghton (born 21 August 1983) is an English television personality, glamour model, media personality, television presenter, columnist and novelist.
- [d1s1]  She was the first 'non-celebrity' to feature in the Channel 4 reality television show "Celebrity Big Brother" in 2006.

**d2: Jacko hoax**

- [d2s0] The Jacko hoax was a Canadian newspaper story about a gorilla supposedly caught near Yale, British Columbia in 1884.
- [d2s1]  The story, titled "What is it?
- [d2s2] , A strange creature captured above Yale.
- [d2s3]  A British Columbia Gorilla", appeared in the British Columbia newspaper the "Daily Colonist" on July 4, 1884.
- [d2s4]  The original newspaper article describes "Jacko" as a gorilla and not a Sasquatch.
- [d2s5]  However, the "Jacko" story has been used by Bigfoot advocates as evidence for the existence of Sasquatch.
- [d2s6]  Many books about Bigfoot and cryptids have featured the event and cite the original newspaper article.
- [d2s7]  In 2008 Michael Cremo discussed the story as possible proof for the existence of Sasquatch.
- [d2s8]  The "Jacko" story was featured on the A&E television documentary series "Ancient Mysteries" about Bigfoot, season 4, episode 18 narrated by Leonard Nimoy.
- [d2s9]  The story was also mentioned on the Bigfoot episode of the television series "In Search Of...", season 1, episode 5, also narrated by Nimoy.
- [d2s10]  The Jacko story was mentioned in a 1976 documentary called The Mysterious Monsters.

**d3: Caroline Aherne**

- [d3s0] Caroline Mary Aherne (24 December 1963 – 2 July 2016) was an English comedian and BAFTA-winning writer and actress, best known for performing as the acerbic chat show host "Mrs Merton", various roles in "The Fast Show", and as the lead role in "The Royle Family", which she co-wrote.
- [d3s1]  She narrated the Channel 4 reality television series "Gogglebox "from its inception in 2013 until April 2016.

**d4: Imogen Thomas**

- [d4s0] Imogen Mary Thomas (born 29 November 1982) is a Welsh model and television personality.
- [d4s1]  She came to prominence in 2003, after winning Miss Wales, and achieved further notability in 2006, when she lasted three months on the seventh series of Channel 4 reality television programme "Big Brother".

**d5: Big Brother 3 (UK)**

- [d5s0] Big Brother 2002, also known as Big Brother 3, was the third series of the British reality television series "Big Brother".
- [d5s1]  It is based upon the Netherlands series of the same name, which gained notoriety in 1999 and 2000.
- [d5s2]  The series premiered on Channel 4 on 24 May 2002 and lasted nine weeks (64 days) until the live finale on 26 July 2002.
- [d5s3]  The third edition saw a ratings increase for the series.
- [d5s4]  The finale had a total of 10 million viewers which is not only the most watched episode of "Big Brother" to date but, based on Live +7 data supplied by BARB, is Channel 4's most watched broadcast since the channel's inception in 1982.
- [d5s5]  In total, over 8.6 million votes were cast to determine the winner of the series.
- [d5s6]  In terms of average viewers, "Big Brother 3" is the highest rated series of the show to date, averaging 5.9 million viewers throughout the whole season.
- [d5s7]  It is one of only two seasons of the main series to have over five million average viewers.
- [d5s8]  More than 150,000 viewers applied to be on this season, more than double the number of applicants from the previous edition.
- [d5s9]  Davina McCall returned as host.

**d6: Shipwrecked: Battle of the Islands 2009**

- [d6s0] Shipwrecked: Battle of the Islands 2009 is a United Kingdom reality television series, part of the "Shipwrecked" strand which aired on Channel 4's youth programming label T4 in different formats from 2000 until 2012.
- [d6s1]  The 2009 series is the seventh series of Shipwrecked overall, and the fourth and final to adopt the "Battle of the Islands" format.
- [d6s2]  The Series was recommissioned by Channel 4 on Thursday 26 June 2008.
- [d6s3]  Castaway auditions took place during the summer and filming for the series commenced in September 2008 and finished in early November 2008.
- [d6s4]  It began airing on Sunday 1 February 2009 at 12:30pm on Channel 4.

**d7: Lydia Bright**

- [d7s0] Lydia-Rose Bright is an English television personality.
- [d7s1]  She is best known for starring in the ITVBe reality television series "The Only Way Is Essex".
- [d7s2]  In 2016, she took part in "Celebrity Island with Bear Grylls".
- [d7s3]  In February and March 2017, she took part in the fourth series of Channel 4 reality series "The Jump".

**d8: Elementfour**

- [d8s0] Elementfour (variants Element Four and Element 4) was a music producing duo made up of Paul Oakenfold and Andy Gray.
- [d8s1]  They collaborated in writing and producing the tune as a theme song for the Channel 4 reality series "Big Brother" and "Celebrity Big Brother".
- [d8s2]  The single entitled "Big Brother UK TV Theme" became a hit in August and September 2000 reaching #4 on the UK British Singles Chart.
- [d8s3]  The original name for the track, as evidenced by promotional copies, was "Tast-E", and this was before the duo had settled on a collective name for themselves either.
- [d8s4]  The theme is still used to the present day even though "Big Brother" and "Celebrity Big Brother" moved to Channel 5 on 18 August 2011.

**d9: Pound Shop Wars**

- [d9s0] Pound Shop Wars is a British factual television series that was first broadcast on BBC One from 7 November 2012 until 30 September 2015.
- [d9s1]  Narrated by Caroline Aherne, the series shows the competition between rival pound shops, focusing on Poundworld.
- [d9s2]  The second series, comprising eight episodes, began on 12 August 2015.

**d10: Joey Essex**

- [d10s0] Joey Donald Essex (born 29 July 1990) is an English television personality.
- [d10s1]  He rose to fame in 2011 after appearing in the ITV2 television series "The Only Way Is Essex" with several of his family and friends.
- [d10s2]  Essex and his sister Frankie left the show in 2013, although his cousin, Chloe Sims, remains on it.
- [d10s3]  In 2013, Essex took part in the first series of the celebrity diving show "Splash!
- [d10s4] " and the thirteenth series of "I'm a Celebrity...Get Me Out of Here!
- [d10s5] ", where he finished in fourth place.
- [d10s6]  In 2015, he won the Channel 4 reality series "The Jump".

## 12. hotpotqa_5abbdaaa5542996606241732

原位置：`train` 第 192 题 · 全局第 192 题 · `sample_id: hotpotqa_5abbdaaa5542996606241732`

Question: Team2015 was setup by this politician who was former Minister of State at the Department for what?

Note: 

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | politician who setup Team2015 | False | [] | Grant Shapps | [["d5s1"]] | context |
| u2 | Department for which {u1} was former Minister of State | True | ["u1"] | International Development | [["d1s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | politician who set up Team2015 | False | [] | Grant Shapps | [['d5s1']] |
| u2 | department at which {u1} was formerly Minister of State | True | ['u1'] | International Development | [['d1s0']] |

### Source documents (reference only)

**d1: Grant Shapps**

- [d1s0] Grant Shapps (born 14 September 1968) is a British Conservative Party politician, former Minister of State at the Department for International Development.
- [d1s1]  A former co-chairman of the Conservative Party, he is the current member of parliament for Welwyn Hatfield in England.
- [d1s2]  He was returned to parliament in the general election of 8 June 2017 with 26,374 votes (51%).

**d2: Sanjaasürengiin Oyuun**

- [d2s0] Sanjaasuren Oyun (Mongolian: Санжаасүрэнгийн Оюун ), also transcribed S. Oyun, is a prominent Mongolian politician.
- [d2s1]  She is the leader of the Civil Will Party, is the Former Minister of Environment and Green Development, and has been a Member of Parliament of Mongolia (State Great Khural) since 1998.
- [d2s2]  She is also a former Minister of Foreign Affairs and is the current head of the Zorig Foundation.
- [d2s3]  Now she is new head of Global Water Partnersip GWP.
- [d2s4]  In 2003, Eisenhower Fellowships awarded Oyun a fellowship program in the United States.
- [d2s5]  In 2006, Oyun was selected as a Young Global Leader (YGL) by the Davos World Economic Forum (WEF).
- [d2s6]  She has been an active member of the YGL community since.
- [d2s7]  On June, 24th 2014 Dr. Oyun Sanjaasuren was elected the first president of the United Nations Environment Assembly (UNEA).

**d3: Olu Agunloye**

- [d3s0] Olu Agunloye is a Nigerian politician who is former Minister of Power and Steel and former Minister of State for Defence (Navy).
- [d3s1]  In 2016 he joined the Social Democratic Party and became a candidate for Governor of Ondo State.

**d4: Giorgos Papakonstantinou**

- [d4s0] Giorgos Papakonstantinou (Greek: Γιώργος Παπακωνσταντίνου ), born October 30, 1961 in Athens, Greece, is a Greek economist and politician and former Minister for the Environment, Energy and Climate Change of Greece and former Minister for Finance.
- [d4s1]  He is currently working in an advisory capacity in the private sector.

**d5: Team2015**

- [d5s0] Team2015 is a political campaign initiative by the Conservative Party UK aiming to recruit volunteers for the 2015 general election.
- [d5s1]  It was set up by Grant Shapps, Conservative Party Chairman, as a vehicle for organizing volunteers to campaign in the target 40/40 seats.
- [d5s2]  The core leads of the team are Stella Kyriazis, Charles Spungin and the Party Chairman's Office.
- [d5s3]  As of December 2014 there were approximately 40,000 volunteers who joined the initiative.

**d6: Zafer Çağlayan**

- [d6s0] Mehmet Zafer Çağlayan (born 10 November 1957 in Muş) is a Turkish politician and former Minister.
- [d6s1]  He is a member of parliament from the ruling Justice and Development Party and the former Minister of Economic Affairs under Prime Minister Recep Tayyip Erdoğan.

**d7: Ukpor**

- [d7s0] Ukpor is the headquarters of Nnewi South Local Government Area in Anambra State, South-East Nigeria.
- [d7s1]  Ukpor has a collection of villages, with each coming from different quarters.
- [d7s2]  A foremost native of this community is Chief Mbazulike Amechi, former Minister of Aviation, in the Federal Republic of Nigeria.
- [d7s3]  Ukpor is noted for its highly hilly topography, with one of the most notable of the hills, traditionally known as "ugwu ekwensu", which implies "the devil's own hill".
- [d7s4]  In modern times however,continuous grading of the road that hosts this hill has been reducing the height of this specific (historic) high land.
- [d7s5]  Ukpor people were predominantly farmers in the past.
- [d7s6]  Subsequently, the town's leading lights became mainly traders and sundry types of business men and women.
- [d7s7]  In contemporary times however,Ukpor has become the ancestral home of very many successful women and men of all walks of life.
- [d7s8]  Hence,Nigeria's highly influential former Minister of Education/former Minister of Solid Minerals, Dr Obiageli Ezekwesili, hails from this community (by birth).
- [d7s9]  The Ukpor Improvement Union (U.I.U) remains the super-structural political, social and cultural organization in the town of Ukpor.
- [d7s10]  Among the all-time most influential leaders of this union must be counted Chief Gabriel Akachukwu Okeke (1929-1991).
- [d7s11]  Fondly called Gab Okeke by his contemporaries, he was Secretary-General of this great union from 1961-1987 ( a period of twenty-six years).

**d8: Omar Davies**

- [d8s0] Dr. Omar Davies (born 28 May 1947) is a Jamaican politician with the People's National Party (PNP), and the former Minister of Transport, Works and Housing and the former Minister of Finance of Jamaica.
- [d8s1]  He was preceded by Audley Shaw & by extension Dwight Nelson and Don Wehby from the opposing Jamaica Labour Party (JLP) [2007 - 2012].
- [d8s2]  He received his doctorate in Economics from Northwestern University.
- [d8s3]  His service in academia includes work at Stanford University (1973 - 1976) and the University of the West Indies.
- [d8s4]  He is the current Member of Parliament for South St. Andrew; an infamous PNP garrison constituency.

**d9: Ekwow Spio-Garbrah**

- [d9s0] Hon Dr Ekwow Spio-Garbrah (born 1953) is a Ghanaian diplomat and politician.
- [d9s1]  He is a former Ghanaian Minister for Trade and Industry, Former Minister of Communications, Former Minister of Education and a former Acting Minister of Mines & Energy.
- [d9s2]  He also previously served as Ghana's ambassador to the United States and Mexico .
- [d9s3]  He is a former CEO of the Commonwealth Telecommunications Organisation (CTO) based in London.

**d10: Dušan Petrović**

- [d10s0] Dušan Petrović (, ] , born 8 September 1966) is a Serbian politician, a former long-time member of Democratic Party (DS) and the former Minister of Agriculture, Trade, Forestry and Water Management between 2011 and 2012 and former Minister of Justice in the Government of Serbia between 2007 and 2008.

## 13. hotpotqa_5abc47d055429959677d6a70

原位置：`train` 第 193 题 · 全局第 193 题 · `sample_id: hotpotqa_5abc47d055429959677d6a70`

Question: Are Rex Wilson and Scott Treleaven both artists who have made use of the film medium?

Note: 

Type: comparison · fallback: False · SFT snapshots: 7

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | whether Rex Wilson has made use of the film medium | False | [] | yes | [["d3s0"], ["d1s0"], ["d2s0"], ["d4s0"], ["d5s0"], ["d6s0"], ["d7s0"], ["d8s0"], ["d10s0"]] | context |
| u2 | whether Scott Treleaven has made use of the film medium | False | [] | yes | [["d9s0"]] | context |
| u3 | whether both Rex Wilson and Scott Treleaven have made use of the film medium | True | ["u1", "u2"] | yes | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Rex Wilson has made use of the film medium | False | [] | yes | [['d3s0'], ['d1s0'], ['d2s0'], ['d4s0'], ['d5s0'], ['d6s0'], ['d7s0'], ['d8s0'], ['d10s0']] |
| u2 | whether Scott Treleaven has made use of the film medium | False | [] | yes | [['d9s0']] |
| u3 | whether Rex Wilson and Scott Treleaven are both artists who have made use of the film medium | True | ['u1', 'u2'] | yes | [[]] |

### Source documents (reference only)

**d1: Pillars of Society (film)**

- [d1s0] Pillars of Society is a 1920 British silent drama film directed by Rex Wilson and starring Ellen Terry, Norman McKinnel and Mary Rorke.
- [d1s1]  It was based on the 1877 play "The Pillars of Society" by Henrik Ibsen.
- [d1s2]  Location shooting was done in Norway.

**d2: Unmarried (1920 film)**

- [d2s0] Unmarried is a 1920 British silent drama film directed by Rex Wilson and starring Gerald du Maurier, Malvina Longfellow and Edmund Gwenn.
- [d2s1]  The film portrays an unmarried mother and the social workers who support her.

**d3: Rex Wilson (director)**

- [d3s0] Rex Wilson (1873–1951) was a British film director of the silent era.
- [d3s1]  until he was caught molesting a child actor on the set of his 1923 film, St. Elmo.
- [d3s2]  Unable to find work, he moved to New Zealand to take up teaching.

**d4: Tilly of Bloomsbury (1921 film)**

- [d4s0] Tilly of Bloomsbury is a 1921 British silent comedy film directed by Rex Wilson and starring Edna Best, Tom Reynolds, Henry Kendall and Isabel Jeans.
- [d4s1]  It is based on the play "Tilly of Bloomsbury" by Ian Hay, and was the first of three film adaptations.

**d5: Tom Brown's Schooldays (1916 film)**

- [d5s0] Tom Brown's Schooldays is a 1916 British silent drama film directed by Rex Wilson and starring Joyce Templeton, Jack Coleman and Evelyn Boucher.
- [d5s1]  It is an adaptation of the novel "Tom Brown's School Days" by Thomas Hughes.
- [d5s2]  It is set at Rugby School in the 1830s where Tom Brown encounters the villainous bully Flashman.
- [d5s3]  It was made at Catford Studios.

**d6: Mrs. Thompson**

- [d6s0] Mrs. Thompson is a 1919 British silent drama film directed by Rex Wilson and starring Minna Grey, C.M. Hallard and Isobel Elsom.
- [d6s1]  It was released in the United States on 6 April 1923.
- [d6s2]  It was adapted from a novel by William Babington Maxwell.

**d7: Onward Christian Soldiers (film)**

- [d7s0] Onward Christian Soldiers is a 1918 British silent romance film directed by Rex Wilson and starring Isobel Elsom, Owen Nares and Minna Grey.

**d8: Quinneys (1919 film)**

- [d8s0] Quinneys is a 1919 British romance film directed by Rex Wilson and starring Henry Ainley, Isobel Elsom and Eric Harrison.
- [d8s1]  It is an adaptation of the play "Quinneys" by Horace Annesley Vachell which was again made into a film in 1927.

**d9: Scott Treleaven**

- [d9s0] Scott Treleaven is a Canadian artist whose work employs a variety of media including collage, film, video, drawing, photography and installation.

**d10: St. Elmo (1923 British film)**

- [d10s0] St. Elmo is a 1923 British silent drama film directed by Rex Wilson and starring Shayle Gardner, Gabrielle Gilroy and Madge Tree.
- [d10s1]  It was an adaptation of the 1866 novel "St. Elmo" by Augusta Jane Evans.
- [d10s2]  An American adaptation "St. Elmo" was released the same year.

## 14. hotpotqa_5abca3065542993a06baf93a

原位置：`train` 第 194 题 · 全局第 194 题 · `sample_id: hotpotqa_5abca3065542993a06baf93a`

Question: In which American animated educational interactive children's television program,  created and executive produced by Chris Gifford and Valerie Walsh, did Harrison Chad have a role?

Note: 

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | American animated educational interactive children's television program created and executive produced by Chris Gifford and Valerie Walsh | False | [] | Go, Diego, Go! | [["d1s2"]] | context |
| u2 | television program in which Harrison Chad had a role, given {u1} | True | ["u1"] | Go, Diego, Go! | [["d9s1"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | American animated educational interactive children's television program created and executive produced by Chris Gifford and Valerie Walsh | False | [] | Go, Diego, Go! | [['d1s2']] |
| u2 | program created and executive produced by Chris Gifford and Valerie Walsh in which Harrison Chad had a role, given {u1} | True | ['u1'] | Go, Diego, Go! | [['d9s1']] |

### Source documents (reference only)

**d1: Go, Diego, Go!**

- [d1s0] Go, Diego, Go!
- [d1s1]  is an American animated educational interactive children's television program that originally aired on the Nickelodeon children's cable network in the United States and produced by Nickelodeon Animation Studio.
- [d1s2]  Created and executive produced by Chris Gifford and Valerie Walsh, the series is a spin-off of "Dora the Explorer" and follows Dora's cousin Diego, an 8-year-old boy whose adventures frequently involve rescuing animals and protecting their environment.

**d2: The Simpsons (season 5)**

- [d2s0] "The Simpsons"' fifth season originally aired on the Fox network between September 30, 1993 and May 19, 1994.
- [d2s1]  The showrunner for the fifth production season was David Mirkin who executive produced 20 episodes.
- [d2s2]  Al Jean and Mike Reiss executive produced the remaining two, which were both hold overs that were produced for the previous season.
- [d2s3]  The season contains some of the series' most acclaimed episodes, including "Cape Feare" and "Rosebud".
- [d2s4]  It also includes the 100th episode, "Sweet Seymour Skinner's Baadasssss Song".
- [d2s5]  The season was nominated for two Primetime Emmy Awards and won an Annie Award for Best Animated Television Program as well as an Environmental Media Award and a Genesis Award.
- [d2s6]  The DVD box set was released in Region 1 on December 21, 2004, Region 2 on March 21, 2005, and Region 4 on March 23, 2005.

**d3: Reading Rainbow**

- [d3s0] Reading Rainbow is an American half-hour children's television series that aired on PBS Kids from June 6, 1983, to November 10, 2006, with a total of 155 half-hour episodes spanning over 21 seasons.
- [d3s1]  The show encouraged children to read.
- [d3s2]  In 2012, an iPad and Kindle Fire educational interactive book reading and video field trip application was launched bearing the name of the program.

**d4: Chris Gifford (actor)**

- [d4s0] Chris Gifford (born May 3, 1959) is a writer and executive producer at Nickelodeon, where he co-created the Peabody Award-winning children's series "Dora the Explorer" where he was the voice of the Big Red Chicken, the Grumpy Old Troll, the Pirate Captain Pig, etc. and its successful spin-off "Go, Diego, Go!
- [d4s1] ".
- [d4s2]  He was also a cast member (Danny) on the 1980s syndicated children's series, "The Great Space Coaster".

**d5: Talk 'n Play**

- [d5s0] Talk 'n Play was an American interactive desktop educational toy book reader with a built in microphone and action buttons that was sold from 1983 to 1992 as an entertaining and educational toy manufactured by CBS Toys, Hasbro, and Kiddesigns.
- [d5s1]  It appears to work utilizing the two sets of right/left tracts to have the "interactive" mono audio segments.
- [d5s2]  It then also provided a record capability so as a child could ad in their own voice and create interactions with characters on the program.
- [d5s3]  It was invented and Patented by Michael J. Freeman Ph.D. and licensed for use by the Children's Television Workshop (owners of Sesame Street) and the Walt Disney Company, among others (see list below).
- [d5s4]  Similar to adapted 4 channels of educational information (and recordings from the child) to produce interactivity, but the main voices were created and produced by Sesame Street and Disney characters under License.
- [d5s5]  Because the toy contained an integrative book reader, some considered it an early lower tech version of the kindle.
- [d5s6]  Talk'N play would say turn the page now.
- [d5s7]  Story programs were produced by othwers Talk'N Play had many music programs where children could add in or take out, different instruments as the song is played.

**d6: Arthur (TV series)**

- [d6s0] Arthur is a Canadian/American animated educational television series for children, created by Cookie Jar Group (formerly known as Cinar) and WGBH for PBS.
- [d6s1]  The show is set in the fictional American city of Elwood City, and revolves around the lives of 8-year-old Arthur Read, an anthropomorphic aardvark, his friends and family, and their daily interactions with each other.

**d7: Ni Hao, Kai-Lan**

- [d7s0] Ni Hao, Kai-Lan (; "Hello, Kai-Lan") is an American animated (anime-influenced) interactive children's television series which premiered on Nickelodeon on November 5, 2007, and on Noggin (now Nick Jr.) on December 15, 2008.
- [d7s1]  It also premiered on the Canadian television channel Treehouse TV.

**d8: High Street Blues**

- [d8s0] High Street Blues was a short-lived British television sitcom series produced by LWT for ITV from 6 January to 10 February 1989.
- [d8s1]  It ran for six episodes, each 30 minutes long.
- [d8s2]  The series starring Phil McCall, Ron Pember, Elizabeth Stewart, Georgia Mitchell, Valerie Walsh, Chris Pitt, Victoria Hasted, Martin Turner, Johnny Shannon, Eve Bland and Shirley Dixon.

**d9: Harrison Chad**

- [d9s0] Harrison Chad (born July 17, 1992, in Plainview, New York, U.S.) is an American actor and voice actor.
- [d9s1]  His roles include young Tarzan in the film "Tarzan 2", Boots on "Dora the Explorer" (2000-2007) and "Go, Diego, Go!
- [d9s2] ", the singing voice of Leo on "Little Einsteins" (2005-2009) and Cardigan from "".
- [d9s3]  He also has performed in a number of live-action movies, such as the Comedy Central movie, "Hebrew Hammer" and the Showtime movie, "Carry Me Home".

**d10: Dora the Explorer**

- [d10s0] Dora the Explorer is an American educational animated TV series created by Chris Gifford, Valerie Walsh, and Eric Weiner.
- [d10s1]  "Dora the Explorer" became a regular series in 2000.
- [d10s2]  The show is carried on the Nickelodeon cable television network, including the associated Nick Jr. channel.
- [d10s3]  It aired on CBS until September 2006.
- [d10s4]  A Spanish-dubbed version first aired as part of a "Nick en español" block on NBC Universal-owned Telemundo through September 2006; since April 2008, this version of the program has been carried on Univision as part of the "Planeta U" block.
- [d10s5]  The series is co-produced by Nickelodeon Productions and Nickelodeon Animation Studio.
- [d10s6]  "Dora the Explorer" is one of the longest-running shows of Nick Jr.
- [d10s7]  During the sixth season, the show became the Nick Jr. series with the most episodes, surpassing "Blue's Clues" with 143 episodes, having 144 after it had completed broadcasting on television.
- [d10s8]  It won a Peabody Award in 2003 "for outstanding efforts in making learning a pleasurable experience for pre-schoolers."
- [d10s9]  It ended on June 5, 2014 after 8 seasons and 172 episodes.

## 15. hotpotqa_5abcff15554299114383a1c2

原位置：`train` 第 195 题 · 全局第 195 题 · `sample_id: hotpotqa_5abcff15554299114383a1c2`

Question: Were the documentaties Powaqqatsi and Inside Job directed by the same person?

Note: 

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | director of Powaqqatsi | False | [] | Godfrey Reggio | [["d9s0"]] | context |
| u2 | director of Inside Job | False | [] | Charles H. Ferguson | [["d5s0"]] | context |
| u3 | whether the directors of Powaqqatsi and Inside Job are the same | True | ["u1", "u2"] | no | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of the documentary Powaqqatsi | False | [] | Godfrey Reggio | [['d9s0']] |
| u2 | director of the documentary Inside Job | False | [] | Charles H. Ferguson | [['d5s0']] |
| u3 | whether Powaqqatsi and Inside Job were directed by the same person | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Inside Job (1946 film)**

- [d1s0] Inside Job is a 1946 American crime film noir directed by Jean Yarbrough starring Preston Foster, Ann Rutherford, Alan Curtis and Milburn Stone.

**d2: Taking You Home**

- [d2s0] "Taking You Home" is a 2000 track from Don Henley's CD "Inside Job".
- [d2s1]  The track was written by Henley along with Stuart Brawley and Stan Lynch and was Henley's only number one on the Adult Contemporary chart as a solo artist.
- [d2s2]  "Taking You Home" stayed at number one for four weeks and went to number 58 on the "Billboard" Hot 100.

**d3: S v Tandwa**

- [d3s0] In S v Tandwa (2007), the seven appellants were convicted of a bank robbery and appealed this.
- [d3s1]  The allegation was that it was an "inside job," as Tandwa was an employee of the bank.
- [d3s2]  It looked like Tandwa was a victim, but he was actually working with the bank robbers.

**d4: Inside Job (TV series)**

- [d4s0] Inside Job is a reality show on TNT, which premiered on February 28, 2014.
- [d4s1]  In each episode of "Inside Job", a group of four people compete to win a job at a large company; although one of the four contestants is secretly already an employee at that company, and is there not to compete but to judge the others' skills and character.

**d5: Inside Job (2010 film)**

- [d5s0] Inside Job is a 2010 documentary film, directed by Charles H. Ferguson, about the late-2000s financial crisis.
- [d5s1]  Ferguson says the film is about "the systemic corruption of the United States by the financial services industry and the consequences of that systemic corruption".
- [d5s2]  In five parts, the film explores how changes in the policy environment and banking practices helped create the financial crisis.

**d6: The Alpha Caper**

- [d6s0] The Alpha Caper, also known as "The Inside Job", is a made-for-television crime thriller directed by Robert Michael Lewis and released in 1973.
- [d6s1]  It stars Henry Fonda as an embittered parole officer forced into early retirement, who decides to take revenge against the city officials by stealing a gold shipment being moved to a new depository.
- [d6s2]  The television film was the final production of producer Aubrey Schenck and was a television pilot for an American television series called "Crime".

**d7: Inside Job (novella)**

- [d7s0] Inside Job is a novella by Connie Willis, originally published in the January 2005 issue of "Asimov's Science Fiction" and later as a hardback by Subterranean Press.
- [d7s1]  In the story, a debunker of pseudoscience encounters a fake medium who seems to be genuinely channelling the disruptive spirit of H. L. Mencken.
- [d7s2]  It was the winner of the 2006 Hugo Award for Best Novella.

**d8: Inside Job**

- [d8s0] Inside job refers to a crime committed by a person in a position of trust, or with the help of someone either employed by the victim or entrusted with access to the victim's affairs or premises.

**d9: Powaqqatsi**

- [d9s0] Powaqqatsi ( ), or Powaqqatsi: Life in Transformation, is a 1988 American documentary film directed by Godfrey Reggio and the sequel to Reggio's experimental 1982 film, "Koyaanisqatsi".
- [d9s1]  It is the second film in the Qatsi trilogy.

**d10: Inside job**

- [d10s0] An inside job is a crime, usually larceny, robbery or embezzlement, committed by a person with a position of trust who is authorized to access a location or procedure with little or no supervision, e.g., a key employee or manager.
- [d10s1]  The perpetrator can also be a former employee who still has specialized knowledge necessary to facilitate the crime.

## 16. hotpotqa_5abdc7fb55429965af743e3a

原位置：`train` 第 196 题 · 全局第 196 题 · `sample_id: hotpotqa_5abdc7fb55429965af743e3a`

Question: John William Maule Ramsay served as Secretary for Scotland in the administration of a British Liberal statesman and Britian's oldest what?

Note: 保留原版

Type: bridge · fallback: False · SFT snapshots: 7

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | British Liberal statesman in whose administration John William Maule Ramsay served as Secretary for Scotland | False | [] | William Ewart Gladstone | [["d6s0", "d6s1", "d10s0"]] | context |
| u2 | office of which {u1} was Britain's oldest holder | True | ["u1"] | Prime Minister | [["d10s2"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | British Liberal statesman in whose administration John William Maule Ramsay served as Secretary for Scotland | False | [] | William Ewart Gladstone | [['d6s0', 'd6s1', 'd10s0']] |
| u2 | office of which {u1} was Britain's oldest holder | True | ['u1'] | Prime Minister | [['d10s2']] |

### Source documents (reference only)

**d1: Sir William Maule**

- [d1s0] Sir William Maule was the eldest son of Sir Peter Maule and Christina de Valognes, Baron and Baroness of Panmure and Benvie.
- [d1s1]  William succeeded as Baron in 1254 on his father's death.
- [d1s2]  He was married to Ethana de Vallibus, daughter of John Vaux, Lord of Dirleton, and left one son, Henry Maule, who succeeded him as Baron.

**d2: Charles Maule Ramsay**

- [d2s0] Lieutenant-Colonel the Honourable Charles Maule Ramsay (27 January 1859 – 7 April 1936) was a British army officer and briefly a Liberal Unionist Member of Parliament (MP).

**d3: Henry Maule**

- [d3s0] Sir Henry Maule was the son and heir of Sir William Maule, Baron of Panmure and Benvie and Ethana de Vallibus, daughter of John Vaux, Lord of Dirleton.
- [d3s1]  William succeeded as Baron on his father's death and was married to Margaret Hay, daughter of Sir William Hay of Locherworth.

**d4: Edward Grey, 1st Viscount Grey of Fallodon**

- [d4s0] Edward Grey, 1st Viscount Grey of Fallodon, KG, PC, DL, FZS (25 April 1862 – 7 September 1933), better known as Sir Edward Grey (he was the 3rd Baronet Grey of Fallodon), was a British Liberal statesman.
- [d4s1]  An adherent of the "New Liberalism", he served as foreign secretary from 1905 to 1916, the longest continuous tenure of any person in that office.
- [d4s2]  He is probably best remembered for his "the lamps are going out" remark on 3 August 1914 on the outbreak of the First World War.
- [d4s3]  He signed the Sykes-Picot Agreement on 16 May 1916.
- [d4s4]  Ennobled in 1916, he was Ambassador to the United States between 1919 and 1920 and Leader of the Liberal Party in the House of Lords between 1923 and 1924.

**d5: Herbert Gladstone, 1st Viscount Gladstone**

- [d5s0] Herbert John Gladstone, 1st Viscount Gladstone, (7 January 1854 – 6 March 1930) was a British Liberal statesman.
- [d5s1]  The youngest son of William Ewart Gladstone, he was Home Secretary from 1905 to 1910 and Governor-General of the Union of South Africa from 1910 to 1914.

**d6: John Ramsay, 13th Earl of Dalhousie**

- [d6s0] John William Maule Ramsay, 13th Earl of Dalhousie KT, PC (29 January 1847 – 25 November 1887), styled Lord Ramsay between 1874 and 1880, was a Scottish naval commander, courtier and Liberal politician.
- [d6s1]  He served as Secretary for Scotland in William Ewart Gladstone's short-lived 1886 administration.

**d7: Alexander Ramsay of Mar**

- [d7s0] Captain Alexander Arthur Alfonso David Maule Ramsay of Mar DL (21 December 1919 – 20 December 2000) was the only child of Princess Patricia of Connaught, who renounced her royal title and style when she married then-Captain the Hon. Alexander Ramsay in February 1919.
- [d7s1]  His mother was the youngest child of Prince Arthur, Duke of Connaught, the third son of Queen Victoria and Prince Albert.
- [d7s2]  His father was the third son of John Ramsay, 13th Earl of Dalhousie.
- [d7s3]  Alexander was the first cousin of the Queen Ingrid of Denmark, Prince Gustaf Adolf (the father of the current King of Sweden) and their siblings, because their mother, Princess Margaret of Connaught, was Alexander's aunt and wife to the Crown Prince of Sweden.

**d8: Alexander Ramsay (Royal Navy officer)**

- [d8s0] Admiral Sir Alexander Robert Maule Ramsay, {'1': ", '2': ", '3': ", '4': "} (29 May 1881 – 8 October 1972) was a British Royal Navy officer.
- [d8s1]  He was the husband of Princess Patricia of Connaught, the youngest child of The Duke of Connaught, third son of Queen Victoria.
- [d8s2]  He served with distinction during the First World War.
- [d8s3]  During the 1920s and 1930s, he held several important Naval Aviation commands.

**d9: Archibald Maule Ramsay**

- [d9s0] Captain Archibald Henry Maule Ramsay (4 May 1894 – 11 March 1955) was a British Army officer who later went into politics as a Scottish Unionist Member of Parliament (MP).
- [d9s1]  From the late 1930s, he developed increasingly strident antisemitic views.
- [d9s2]  In 1940, after his involvement with a suspected spy at the United States embassy, he became the only British MP to be interned under Defence Regulation 18B.

**d10: William Ewart Gladstone**

- [d10s0] William Ewart Gladstone, ( ; 29 December 1809 – 19 May 1898) was a British Liberal statesman and earlier Conservative politician.
- [d10s1]  In a career lasting over 60 years, he served as Prime Minister four separate times (1868–74, 1880–85, February–July 1886 and 1892–94), more than any other person, and served as Chancellor of the Exchequer four times.
- [d10s2]  Gladstone was also Britain's oldest Prime Minister; he resigned for the final time when he was 84 years old.

## 17. hotpotqa_5ac04afa5542996f0d89cb80

原位置：`train` 第 197 题 · 全局第 197 题 · `sample_id: hotpotqa_5ac04afa5542996f0d89cb80`

Question: Wells Cathedral School is a co-educational independent school located in Wells, Somerset, England, the school is one of the five specialist musical schools for school-age children in the United Kingdom, includes which specialist music school for children, located in the town of Bushey, in which south location?

Note: 应该同时输出学校和地区两个答案

Type: multipart · fallback: False · SFT snapshots: 5

### Adjusted units and annotation

**执行结果：** 按 Note 同时回答学校和地区：两个单元均为 necessary=true，保留地区对学校的依赖；答案为 Purcell School 和 Hertfordshire，均由 d4s0 支持。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | specialist music school for children located in Bushey | True | [] | Purcell School | [["d4s0"]] | context |
| u2 | county in whose southern part {u1} is located | True | ["u1"] | Hertfordshire | [["d4s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | specialist music school for children located in the town of Bushey | False | [] | Purcell School | [['d4s0']] |
| u2 | south location in which {u1} is located | True | ['u1'] | Hertfordshire | [['d4s0']] |

### Source documents (reference only)

**d1: St Mary's Music School**

- [d1s0] St Mary's Music School is a music school in Scotland in Edinburgh, for boys and girls aged 9 to 19 and is also the Choir School of St Mary's Episcopal Cathedral.
- [d1s1]  The school, which is non-denominational, provides education for children with a special talent in music, and is Scotland's only full-time independent specialist music school.
- [d1s2]  In 2017 the school has 80 pupils from many different backgrounds and from all parts of Scotland, the rest of the UK and abroad - 49 day pupils and 31 boarders, plus one student on the school's Part-time Pathways to Specialism scheme.

**d2: Yehudi Menuhin School**

- [d2s0] The Yehudi Menuhin School is a specialist music school in Surrey, England, founded in 1963 by violinist Yehudi Menuhin.
- [d2s1]  The school is one of the five established musical schools for school-age children in the United Kingdom, along with Chetham's School of Music, Wells Cathedral School, the Purcell School and St. Mary's Music School, Edinburgh.

**d3: Chetham's School of Music**

- [d3s0] Chetham's School of Music (pronounced with a long "e", , although sometimes known familiarly as "Chets", ) is an independent co-educational boarding specialist music school in Manchester in North West England.
- [d3s1]  It is the largest of nine schools across England and Scotland to be fully funded through the UK government's Music and Dance Scheme, under which students showing potential in music or dance may receive up to full fees for specialist tuition.
- [d3s2]  Funding is means tested and subject only to residency criteria.
- [d3s3]  90% of Chetham's students receive full or partial funding for their education or boarding through this scheme.

**d4: Purcell School**

- [d4s0] The Purcell School for Young Musicians is a specialist music school for children, located in the town of Bushey, south Hertfordshire, England, and is the oldest specialist music school in the UK.
- [d4s1]  The school was awarded the UNESCO Mozart Medal in 2003, which was received on behalf of the school by Prince Charles, who is a patron of the school.
- [d4s2]  Sir Simon Rattle is honorary president of the school.
- [d4s3]  Many of the pupils subsequently study at the Royal College of Music or Royal Academy of Music.
- [d4s4]  In 2015, the School became the very first Fazioli Pianoforti Centre of Excellence.

**d5: City of Edinburgh Music School**

- [d5s0] The City of Edinburgh Music School is a state-maintained music school in Scotland in Edinburgh, Scotland.
- [d5s1]  Founded as the Lothian Specialist Music School in 1980, it changed its name in 1996 when Lothian Regional Council was dissolved into four separate unitary councils.
- [d5s2]  It is a non-residential school, and because it is funded by the City of Edinburgh Council, it charges no fees.
- [d5s3]  Unlike residential music schools, pupils attend comprehensive schools for their academic classes: Flora Stevenson Primary and Broughton High School.

**d6: Warwick School**

- [d6s0] Warwick School is an independent school with boarding facilities (also known as a public school) for boys in Warwick, England.
- [d6s1]  It is the fifth-oldest surviving school in England after King's School, Canterbury, King's School, Rochester, St Peter's School, York and Wells Cathedral School.
- [d6s2]  It is the oldest boys-only school in the United Kingdom.
- [d6s3]  It was active in the reign of King Edward the Confessor (reigned 1042–1066) and it is speculated that it existed before this date.
- [d6s4]  Its headmasters have been members of the Headmaster and Headmistresses Conference since 1896.

**d7: Simon de Souza**

- [d7s0] Simon de Souza (born c. 1964) is a horn teacher in the United Kingdom.
- [d7s1]  He taught at the Birmingham Conservatoire (where he has been professor of horn since 2004), was horn tutor at Wells Cathedral School and the Purcell School, and was also involved with the Junior departments of the Trinity College of Music and Royal Academy of Music.
- [d7s2]  He has worked with many youth orchestras, including the National Youth Wind Orchestra, National Children’s Wind Orchestra, National Schools Symphony Orchestra and National Children’s Orchestra.
- [d7s3]  He has written on horn teaching matters for publications including "Music Teacher" and the "Hornplayer" magazine, journal of the British Horn Society, of which he was vice-chair and educational consultant.

**d8: Queen's College, Taunton**

- [d8s0] Queen's College is a co-educational independent school located in Taunton, the county town of Somerset, England.
- [d8s1]  It is a day/boarding school for children aged 0–18.
- [d8s2]  The school incorporates Nursery, Pre-Prep, Junior and Senior schools.
- [d8s3]  The current Head Teacher of the Senior School (11–18) is Dr Lorraine Earps.
- [d8s4]  Mrs Tracey Khodabandehloo is Headmistress of the Junior School (0–11)

**d9: Wells Cathedral School**

- [d9s0] Wells Cathedral School is a co-educational independent school located in Wells, Somerset, England.
- [d9s1]  The school is one of the five specialist musical schools for school-age children in the United Kingdom, along with Chetham's School of Music, the Yehudi Menuhin School, the Purcell School and St. Mary's Music School, Edinburgh.
- [d9s2]  The principal, Elizabeth Cairncross, is a member of the Headmasters' Conference.

**d10: Bablake School**

- [d10s0] Bablake School is a co-educational Independent school located in Coventry, England and founded in 1344 by Queen Isabella, making it one of the oldest schools in the United Kingdom (List of the oldest schools in the United Kingdom).
- [d10s1]  Bablake is part of the Coventry School Foundation, a registered charity, along with King Henry VIII School, King Henry VIII Preparatory School and Cheshunt School.
- [d10s2]  The current headmaster is John Watson, who succeeded Dr Stuart Nuttall following his retirement in 2006.
- [d10s3]  Today Bablake is a selective, fee-paying independent school and a member of the HMC.

## 18. hotpotqa_5ac119595542992a796dede5

原位置：`train` 第 198 题 · 全局第 198 题 · `sample_id: hotpotqa_5ac119595542992a796dede5`

Question: Cherokee Lake is a reservoir formed by theimpoundment of what river flowing from Kingsport to Knoxville, Tennessee?

Note: 题干中涵已知信息，这种类型的题按照新方法的single拆分

Type: single · fallback: False · SFT snapshots: 7

### Adjusted units and annotation

**执行结果：** 按用户 Note 将河流流向视为题干给定限定，single 只查水库所拦河流，沿用旧 u1 的直接支持。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | river impounded to form Cherokee Lake | True | [] | Holston River | [["d1s0"], ["d9s0", "d9s2"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | river whose impoundment forms Cherokee Lake | False | [] | Holston River | [['d1s0'], ['d9s0', 'd9s2']] |
| u2 | river flowing from Kingsport to Knoxville, Tennessee whose impoundment forms Cherokee Lake, given {u1} | True | ['u1'] | Holston River | [['d8s0']] |

### Source documents (reference only)

**d1: Cherokee Lake**

- [d1s0] Cherokee Lake, also known as Cherokee Reservoir, is a reservoir in Tennessee formed by the impoundment of the Holston River behind Cherokee Dam.

**d2: Djab wurrung**

- [d2s0] The Djab wurrung, also "Tjapwurrung," people are Indigenous Australians who occupy the volcanic plains of central Victoria from the Mount William Range of Gariwerd in the west to the Pyrenees range in the east encompassing the Wimmera River flowing north and the headwaters of the Hopkins River flowing south.
- [d2s1]  The towns of Ararat, Stawell and Hamilton are within their territory.
- [d2s2]  There were 41 Djab wurrung clans who formed an alliance with the neighboring Jardwadjali people through intermarriage, shared culture, trade and moiety system.

**d3: Fort Nelson River**

- [d3s0] The Fort Nelson River is in north-eastern British Columbia, Canada.
- [d3s1]  It flows 517 km generally north-westward to the Liard River, a tributary of the Mackenzie River, which empties into the Arctic Ocean.
- [d3s2]  The river drains a watershed of 55900 km2 and is formed by the confluence of the Fontas River flowing from the east, and the Sikanni Chief River flowing from the south.
- [d3s3]  These, along with the Sahtaneh and Muskwa Rivers constitute the major tributaries.
- [d3s4]  The source of the Sikanni Chief, on the eastern slope of the Rocky Mountains, is ultimately the headwater of the Fort Nelson River.

**d4: Lake Red Rock (Des Moines River)**

- [d4s0] Originally the city of Red Rock, Lake Red Rock, also referred to as Red Rock Reservoir is a reservoir formed by Red Rock Dam on the Des Moines River, about 55 miles southeast of the city of Des Moines, Iowa, United States.
- [d4s1]  The dam was completed in 1969 as a flood control project by the United States Army Corps of Engineers, creating the largest lake in Iowa.
- [d4s2]  The lake is essentially confined to Marion County.
- [d4s3]  The damface is a few miles west and south of Pella, and similarly, a few miles northeast of Knoxville.

**d5: Theodore Roosevelt Lake**

- [d5s0] Theodore Roosevelt Lake (usually called Roosevelt Lake, sometimes Lake Roosevelt) is a large reservoir formed by Theodore Roosevelt Dam on the Salt River in Arizona as part of the Salt River Project (SRP).
- [d5s1]  Located roughly 80 miles (130 km) northeast of Phoenix in the Salt River Valley, Theodore Roosevelt is the largest lake or reservoir located entirely within the state of Arizona (Lake Mead and Lake Powell are larger but both are located partially within the neighboring states of Nevada and Utah respectively).
- [d5s2]  Both the reservoir and the masonry dam that created it, Roosevelt Dam, were named for U.S. President Theodore Roosevelt who dedicated the dam himself in March 1911.
- [d5s3]  Roosevelt Lake is a popular recreation destination within the Tonto National Forest, as such the facilities located at this lake are managed by that authority.

**d6: Narva River**

- [d6s0] The Narva (Estonian: "Narva jõgi" , Russian: Нарва ) (or Narova) is a river flowing into the Baltic Sea, the largest river in Estonia by discharge.
- [d6s1]  Draining Lake Peipsi, the river forms the border of Estonia and Russia and flows through the towns of Narva/Ivangorod and Narva-Jõesuu into Narva Bay.
- [d6s2]  Though the river is only 77 km long, in terms of volume discharged it is the second largest river flowing into the Gulf of Finland.
- [d6s3]  The river gives its name to the Narva culture and the city of Narva.

**d7: Selbusjø**

- [d7s0] Selbusjø or Selbusjøen is the 17th largest lake in Norway.
- [d7s1]  It is located in Sør-Trøndelag county, primarily in the municipality of Selbu, although the western end of it lies in Klæbu.
- [d7s2]  The 58.26 km2 lake is the largest lake in Sør-Trøndelag county.
- [d7s3]  Selbusjø is part of the Nea-Nidelv watershed, with the Nea River flowing into it on the eastern end and the Nidelva River flowing out the western end.
- [d7s4]  The villages of Selbustrand, Fossan, Tømra, Trøa, Innbygda, Mebonden, Vikvarvet, and Sjøbygda lie around the lake.

**d8: Holston River**

- [d8s0] The Holston River is a 136 mi river that flows from Kingsport, Tennessee, to Knoxville, Tennessee.
- [d8s1]  Along with its three major forks (North Fork, Middle Fork and South Fork), it comprises a major river system that drains much of northeastern Tennessee, southwestern Virginia, and northwestern North Carolina.
- [d8s2]  The Holston's confluence with the French Broad River at Knoxville marks the beginning of the Tennessee River.

**d9: Cherokee Dam**

- [d9s0] Cherokee Dam is a hydroelectric dam located on the Holston River in Grainger County and Jefferson County, Tennessee, in the southeastern United States.
- [d9s1]  The dam is operated and maintained by the Tennessee Valley Authority, which built the dam in the early 1940s to help meet urgent demands for energy at the outbreak of World War II.
- [d9s2]  Cherokee Dam is 175 ft high and impounds the 28780 acre Cherokee Lake.
- [d9s3]  It has a generating capacity of 135,200 kilowatts.
- [d9s4]  The dam was named for the Cherokee, a Native American tribe that controlled much of East Tennessee when the first European settlers arrived in the mid-18th century.

**d10: Chusovaya River**

- [d10s0] The Chusovaya River (Russian: Чусова́я ) is a river flowing in Perm Krai, Sverdlovsk Oblast and Chelyabinsk Oblast of Russia.
- [d10s1]  A tributary of the Kama River, which in turn is a tributary of the Volga River, it discharges into the Chusovskoy Cove of the Kamsky Reservoir.
- [d10s2]  The river is remarkable in that it originates on the eastern slopes of the Ural Mountains in Asia, crosses the mountains, and mostly runs on their western slopes in Europe.
- [d10s3]  The Chusovaya River is widely used as a source of water.
- [d10s4]  In particular, its water is taken from the Volchikhinsky Reservoir, 37 km2 , to the Verkhneisetsky Reservoir to supply the major city of Yekaterinburg.
- [d10s5]  Fifteen smaller reservoirs are spread over about 150 tributaries of the river.

## 19. hotpotqa_5ac11f47554299294b2190ae

原位置：`train` 第 199 题 · 全局第 199 题 · `sample_id: hotpotqa_5ac11f47554299294b2190ae`

Question: Which running bank was drafted by the 1983 Los Angeles Rams and later was inducted into the Hall of Fame?

Note: 

Type: bridge · fallback: False · SFT snapshots: 5

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | running back drafted by the 1983 Los Angeles Rams | False | [] | Eric Dickerson | [["d9s1"]] | context |
| u2 | running back inducted into the Hall of Fame, given {u1} | True | ["u1"] | Eric Dickerson | [["d2s5"], ["d9s1"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | running back drafted by the 1983 Los Angeles Rams | False | [] | Eric Dickerson | [['d9s1']] |
| u2 | running back drafted by the 1983 Los Angeles Rams who was later inducted into the Hall of Fame, given {u1} | True | ['u1'] | Eric Dickerson | [['d2s5'], ['d9s1']] |

### Source documents (reference only)

**d1: List of Los Angeles Rams first-round draft picks**

- [d1s0] The Los Angeles Rams, a professional American football team based in Los Angeles, joined the National Football League (NFL) as Cleveland Rams in 1937.
- [d1s1]  The Rams began playing in 1936 as a charter member of the second American Football League.
- [d1s2]  Although the NFL granted membership to the same owner, the NFL considers it a separate entity.
- [d1s3]  In 1946, Rams' owner Dan Reeves, fed up with poor attendance at Cleveland Stadium, moved the Rams to Los Angeles, and the team played there from 1946 to 1979.
- [d1s4]  Before his death in 1979, later Rams owner Carroll Rosenbloom planned a move within the Los Angeles metropolitan area to Anaheim, using the venue now known as Angel Stadium, and his widow and successor Georgia Frontiere went through with the move in 1980, with the team still officially representing Los Angeles.
- [d1s5]  The Rams moved to St. Louis in 1995 and renamed the team St. Louis Rams.
- [d1s6]  In January 2016, the Rams and the NFL announced that the team would return to Los Angeles.
- [d1s7]  The team now plays in its original L.A. venue, the Los Angeles Memorial Coliseum, while awaiting the 2020 opening of its new stadium in suburban Inglewood.

**d2: Eric Dickerson**

- [d2s0] Eric Demetric Dickerson (born September 2, 1960) is a former college and professional American football player who was a running back in the National Football League (NFL) for eleven seasons during the 1980s and 1990s.
- [d2s1]  Dickerson played college football for the SMU Mustangs of Southern Methodist University and was recognized as an All-American.
- [d2s2]  He was selected in the first round of the 1983 NFL Draft and played professionally for the Los Angeles Rams, Indianapolis Colts, Los Angeles Raiders, and Atlanta Falcons of the NFL.
- [d2s3]  During his NFL career, he rushed for over 13,000 yards.
- [d2s4]  He holds the NFL's single-season rushing record with 2,105 yards, set in 1984.
- [d2s5]  Dickerson was inducted into the Pro Football Hall of Fame in 1999.

**d3: 1983 Los Angeles Raiders season**

- [d3s0] The 1983 Los Angeles Raiders season began with the team trying to improve on their 8–1 record from 1982.
- [d3s1]  The 1983 season was the second season in Los Angeles.
- [d3s2]  The 1983 season is also the Raiders third Super Bowl winning season.
- [d3s3]  To date, it was the team's most recent NFL championship season.
- [d3s4]  NFL Films titled the season highlights of the 1983 Los Angeles Raiders, "Just Win, Baby!"
- [d3s5] , narrated by John Facenda, and on November 24, 2006, NFL Network aired , the 1983 Los Angeles Raiders, ranking them #20, with team commentary from Marcus Allen, Todd Christensen and Howie Long, and narrated by Alec Baldwin.

**d4: Los Angeles Rams Cheerleaders**

- [d4s0] The Los Angeles Rams Cheerleaders are the cheerleading squad for the Los Angeles Rams professional football team.
- [d4s1]  They were established in 1974 during the team's original tenure in Los Angeles and were known as the Embraceable Ewes.
- [d4s2]  The cheerleading organization became known as the "St. Louis Rams Cheerleaders" when the team moved to St. Louis, Missouri.
- [d4s3]  Beginning with the 2016 NFL season, the organization changed their name to the "Los Angeles Rams Cheerleaders" to associate themselves with the recently relocated Los Angeles Rams football team.

**d5: History of the Los Angeles Rams**

- [d5s0] The Los Angeles Rams are a professional American football team that play in the National Football League (NFL).
- [d5s1]  The Rams franchise was founded in 1936 as the Cleveland Rams in the short-lived second American Football League before joining the NFL the next year.
- [d5s2]  In 1946, the franchise moved to Los Angeles.
- [d5s3]  The Rams franchise remained in the metro area until 1994, when they moved to St. Louis, and were known as the St. Louis Rams from 1995 to 2015.
- [d5s4]  The Rams franchise returned to Los Angeles in 2016.
- [d5s5]  This article chronicles the franchise's history during their time in Los Angeles, from playing at the Los Angeles Memorial Coliseum between 1946 and 1979, to playing at Anaheim Stadium (now known as Angel Stadium of Anaheim) in Anaheim from 1980 to 1994, and its return to Southern California beginning with the season.

**d6: List of Los Angeles Rams seasons**

- [d6s0] This article is a list of seasons completed by the Los Angeles Rams American football franchise (known as the Cleveland Rams from 1936 to 1945 and the St. Louis Rams from 1995 to 2015) in organized play.
- [d6s1]  The list documents the season-by-season records of the Los Angeles Rams franchise from 1936 to present, including conference standings, division standings, postseason records, league awards for individual players or head coaches, and team awards for individual players.
- [d6s2]  The Rams franchise was founded in Cleveland in 1936 when the team was playing in the newly formed American Football League (AFL).
- [d6s3]  The franchise joined the National Football League (NFL) the following year.
- [d6s4]  In 1943 operations were suspended due a depleted player roster due to World War II, and play resumed the following year.
- [d6s5]  The Rams were the only team to suspend completely in 1943.
- [d6s6]  The franchise has changed home cities thrice, moving to Los Angeles in 1946, moving to St. Louis in 1995, and returning to Los Angeles in 2016.

**d7: List of Los Angeles Rams head coaches**

- [d7s0] The Los Angeles Rams are a professional football team based in the Los Angeles metropolitan area.
- [d7s1]  The Rams compete in the National Football League (NFL) as a member club of the league's National Football Conference (NFC) West division.
- [d7s2]  The Rams played their first season in 1936 in Cleveland, Ohio.
- [d7s3]  During World War II, the Rams did not play during the 1943 season because of wartime restrictions and shortages.
- [d7s4]  The team became known as the Los Angeles Rams after it moved to Los Angeles, California in 1946.
- [d7s5]  After the 1979 season, the Rams moved south to the suburbs in nearby Orange County, playing their home games at Anaheim Stadium in Anaheim for fifteen seasons (–) but kept their Los Angeles name.
- [d7s6]  The club moved east to St. Louis, Missouri before the 1995 season, and moved back to Los Angeles before the 2016 season.

**d8: Bob Waterfield**

- [d8s0] Robert Stanton Waterfield (July 26, 1920 – March 25, 1983) was an American football player and coach and motion picture actor and producer.
- [d8s1]  He played quarterback for the UCLA Bruins and Cleveland/Los Angeles Rams and was inducted into the Pro Football Hall of Fame in 1965.
- [d8s2]  His No. 7 jersey was retired by the Los Angeles Rams in 1952.

**d9: 1983 Los Angeles Rams season**

- [d9s0] The 1983 Los Angeles Rams season was the team's 46th year with the National Football League and the 38th season in the city of Los Angeles.
- [d9s1]  The franchise drafted a future Hall of Fame Running Back in Eric Dickerson.
- [d9s2]  The season saw the team attempt to improve on its 2-7 record from 1982.
- [d9s3]  The team started out 5-2 before splitting their next 4 games and then lost at home to Washington to sit at 7-5.
- [d9s4]  They would split their last 4 games to finish 9-7 and make the playoffs for the first time since 1980 after a 2-year absence.
- [d9s5]  In the playoffs, they defeated the Cowboys 24-17 in Dallas to advance to the Divisional Round.
- [d9s6]  However, in the game, the Rams were annihilated 51-7 by the Redskins, who would go to the Super Bowl later.

**d10: Carver Shannon**

- [d10s0] Carver Beauregard Shannon (born April 28, 1938) was an American and Canadian football player who played for the Winnipeg Blue Bombers and Hamilton Tiger-Cats.
- [d10s1]  He won the Grey Cup with Winnipeg in 1959 and 1961.
- [d10s2]  He played college football in Carbondale, Illinois with Southern Illinois University where he was nominated for the 1958 All-American team.
- [d10s3]  Shannon was also drafted into the National Football League in the 1959 NFL draft by the Los Angeles Rams (Round 19, #224 overall).
- [d10s4]  He played for the Rams from 1962 to 1964, following his career in Canadian football.
- [d10s5]  After his time with the Rams he went to play for the Chicago Bears where he sustained a knee injury and retired from professional football.
- [d10s6]  From 1983 through 1985 Shannon was a line judge in the NFL, wearing uniform number 56.
- [d10s7]  He is a member of the Southern Illinois University Sport Hall of Fame, inducted in 1978.
- [d10s8]  He later worked in the aerospace industry following his sports career and lives in Los Angeles.

## 20. hotpotqa_5ac1334b55429964131be184

原位置：`train` 第 200 题 · 全局第 200 题 · `sample_id: hotpotqa_5ac1334b55429964131be184`

Question: What American author known for the Outlander series of novels, created her sixth novel, from the same series, called A Breath of Snow?

Note: 保留single

Type: single · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留用户指定 single，联合书籍作者和美国作家/Outlander 身份证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | American author known for the Outlander series who created A Breath of Snow | True | [] | Diana Gabaldon | [["d7s0", "d6s0"], ["d7s0", "d10s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | author of A Breath of Snow, the sixth novel of the Outlander series | False | [] | Diana Gabaldon | [['d7s0']] |
| u2 | American author known for the Outlander series of novels, given {u1} | True | ['u1'] | Diana Gabaldon | [['d6s0'], ['d10s0']] |

### Source documents (reference only)

**d1: Cauldron (McDevitt novel)**

- [d1s0] Cauldron is a science fiction novel by American author Jack McDevitt.
- [d1s1]  It is the sixth novel in the Academy series, featuring Priscilla Hutchins.

**d2: Lord John series**

- [d2s0] The "Lord John" series is a sequence of historical mystery novels and shorter works written by Diana Gabaldon that center on Lord John Grey, a recurring secondary character in the author's "Outlander" series.
- [d2s1]  Secretly homosexual "in a time when that particular predilection could get one hanged," the character has been called "one of the most complex and interesting" of the hundreds of characters in Gabaldon's "Outlander" novels.
- [d2s2]  Starting with the 1998 novella "Lord John and the Hellfire Club", the "Lord John" spin-off series currently consists of five novellas and three novels.

**d3: John Everson**

- [d3s0] John Everson (born March 14, 1966) is an American author of contemporary horror, dark fantasy, science fiction and fantasy fiction.
- [d3s1]  He is the author of eight novels and four short fiction collections, as well as three mini-collections, all focusing on horror and the supernatural.
- [d3s2]  His novel "Covenant", was originally released in a limited edition hardcover by Delirium Books in 2004 and won the Bram Stoker Award for a First Novel the following year from the Horror Writers Association.
- [d3s3]  His sixth novel, "NightWhere", was a finalist for the Bram Stoker Award in 2012.

**d4: Melissa de la Cruz**

- [d4s0] Melissa de la Cruz (born 1971) is a Filipina American author known for her work in young adult fiction.
- [d4s1]  She has written several series of young adult novels, including the "Au Pair" series and the "Blue Bloods" series, and a contemporary fiction series following "The Beauchamp Family", as well as a number of stand-alone novels.

**d5: Game of Thrones (season 5)**

- [d5s0] The fifth season of the fantasy drama television series "Game of Thrones" premiered on HBO on April 12, and concluded on June 14, 2015.
- [d5s1]  It was broadcast on Sunday at 9:00 pm in the United States, consisting of 10 episodes, each running approximately 50–60 minutes.
- [d5s2]  The season primarily adapts material from "A Feast for Crows" and "A Dance with Dragons", the fourth and fifth novels in George R. R. Martin's "A Song of Ice and Fire" series, though it also uses elements from the third novel, "A Storm of Swords", as well as the upcoming sixth novel "The Winds of Winter".
- [d5s3]  It also contains original content not found in Martin's novels.
- [d5s4]  The series is adapted for television by David Benioff and D. B. Weiss.

**d6: Diana Gabaldon**

- [d6s0] Diana J. Gabaldon (born January 11, 1952) is an American author, known for the "Outlander" series of novels.
- [d6s1]  Her books merge multiple genres, featuring elements of historical fiction, romance, mystery, adventure and science fiction/fantasy.
- [d6s2]  A television adaptation of the novels called "Outlander" premiered on Starz in 2014.

**d7: A Breath of Snow and Ashes**

- [d7s0] A Breath of Snow and Ashes is the sixth book in the "Outlander" series of novels by Diana Gabaldon.
- [d7s1]  Centered on time travelling 20th century doctor Claire Randall and her 18th century Scottish Highlander warrior husband Jamie Fraser, the books contain elements of historical fiction, romance, adventure and science fiction/fantasy.

**d8: Lord John Grey (character)**

- [d8s0] Lord John William Grey is a fictional character created by Diana Gabaldon.
- [d8s1]  He is a recurring secondary character in Gabaldon's "Outlander" series of novels, and the main character of the "Lord John" series of historical mystery novels and novellas.
- [d8s2]  Secretly homosexual "in a time when that particular predilection could get one hanged", the character has been called "one of the most complex and interesting" of the hundreds of characters in Gabaldon's "Outlander" novels.

**d9: Angel Mountain Saga**

- [d9s0] The Angel Mountain Saga of eight novels was written by Welsh author Brian John, and was first published at the rate of one volume per year in 2001-2005, with later volumes in 2007, 2009 and 2012.
- [d9s1]  The publisher is Greencroft Books, based in Newport, Pembrokeshire.
- [d9s2]  The novels tell of the life and times of Mistress Martha Morgan, a feisty heroine who starts the series in 1796 as a pregnant and suicidal eighteen-year-old and finishes it by going to her grave in 1855.
- [d9s3]  In the sixth novel she is resurrected (or is she?)
- [d9s4]  and has further adventures in Merthyr Tydfil and further afield.
- [d9s5]  Volumes seven and eight are placed into gaps in the narrative related in Volume Three.
- [d9s6]  The eight novels are "On Angel Mountain" (2001), "House of Angels" (2002), "Dark Angel" (2003), "Rebecca and the Angels" (2004), "Flying with Angels" (2005), "Guardian Angel" (2007), "Sacrifice" (2009) and "Conspiracy of Angels" (2012).

**d10: Jamie Fraser (character)**

- [d10s0] James "Jamie" Fraser is a fictional character in the "Outlander" series of multi-genre novels by American author Diana Gabaldon, and its television adaptation.
- [d10s1]  In the series, married World War II nurse Claire Randall is visiting Scotland when she finds herself transported from 1945 back to 1743.
- [d10s2]  There she finds adventure, war and romance with the dashing Highland warrior Jamie Fraser.
- [d10s3]  Jamie also appears in two novels in the "Lord John" series of historical mysteries, and in the 2013 novella "Virgins".

## 21. hotpotqa_5ac16e3055429964131be1f3

原位置：`train` 第 201 题 · 全局第 201 题 · `sample_id: hotpotqa_5ac16e3055429964131be1f3`

Question: Big Dreamers and This Is Elvis are both what type of film?

Note: 

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | type of film Big Dreamers is | False | [] | documentary film | [["d5s0"]] | context |
| u2 | type of film This Is Elvis is | False | [] | documentary film | [["d2s0"]] | context |
| u3 | common type of film for Big Dreamers and This Is Elvis | True | ["u1", "u2"] | documentary film | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | type of film Big Dreamers is | False | [] | documentary film | [['d5s0']] |
| u2 | type of film This Is Elvis is | False | [] | documentary film | [['d2s0']] |
| u3 | type of film that Big Dreamers and This Is Elvis both are | True | ['u1', 'u2'] | documentary film | [[]] |

### Source documents (reference only)

**d1: Elvis Gratton**

- [d1s0] Bob 'Elvis' Gratton is a fictional character, the subject of multiple films and a television series of the same name by Quebec director Pierre Falardeau: a series of short films ("Elvis Gratton", 1981; "Les Vacances d'Elvis Gratton", 1983; "Pas encore Elvis Gratton!"
- [d1s1] , 1985) released on VHS as the single 1985 film "Elvis Gratton: Le king des kings", and then two sequels: "Elvis Gratton II: Miracle à Memphis" (1999) and "Elvis Gratton 3: La vengeance d'Elvis Wong" (2004).
- [d1s2]  Most recently, a television series entitled "" began on January 15, 2007, and finished its third and final season in 2009.

**d2: This Is Elvis**

- [d2s0] This Is Elvis is a 1981 documentary film written and directed by Andrew Solt and Malcolm Leo, based on the life of Elvis Presley.
- [d2s1]  It combined archival footage with reenactments, and voice-over narration by pop singer Ral Donner, imitating Presley's speaking voice.
- [d2s2]  It was screened out of competition at the 1981 Cannes Film Festival.
- [d2s3]  The film grossed $2 million at the box office in the U.S. and Canada, ranking #92 for 1981.

**d3: Elvis Has Left the Building**

- [d3s0] Elvis Has Left the Building is a 2004 black comedy film directed by Joel Zwick and starring Kim Basinger as a cosmetics saleswoman who accidentally kills a series of Elvis impersonators as they travel to a convention in Las Vegas.
- [d3s1]  John Corbett plays an advertising executive and her love interest.
- [d3s2]  Tom Hanks has a cameo appearance as one of the dead Elvis impersonators.
- [d3s3]  Angie Dickinson plays Basinger's mother, a former mechanic for the real Elvis.

**d4: Pete Vallee**

- [d4s0] Pete Vallee or Pete "Big Elvis" Vallee as he is professionally known is an Elvis impersonator.
- [d4s1]  At one stage and possibly even now, he is the world's heaviest Elvis impersonator.

**d5: Big Dreamers**

- [d5s0] Big Dreamers is a 55-minute documentary film showcasing the Big Things of Australia.
- [d5s1]  Directed by Camille Hardman, and produced by Camille Hardman and John Fink, "Big Dreamers" features the construction of The Biggest Gumboot in the world in Tully, in far North Queensland.

**d6: Dreamers (film)**

- [d6s0] Dreamers is a Bosnian short documentary film produced by the East West Theatre Company and directed by Nermin Hamzagic.
- [d6s1]  The film follows the story of Samir Karić and Amir Muminović, young hip-hop artists from the village of Hajvazi, near the north-eastern Bosnian town of Kalesija.
- [d6s2]  The mayor's son gave the hip-hop duo a bad beating because of their song which criticized municipal authorities.
- [d6s3]  A newspaper report on the incident intrigues East West Theatre Company, a theatre and film production company from Sarajevo.
- [d6s4]  Shortly after the incident, Samir and Amir become part of the cast of Class Enemy a play about disenfranchised youth in a violent secondary school in Bosnia and Herzegovina.
- [d6s5]  Samir and Amir eventually end up touring the world with the East West Theatre Company's production.
- [d6s6]  The film "Dreamers" is devised as a road movie.

**d7: As Recorded at Madison Square Garden**

- [d7s0] Elvis: As Recorded at Madison Square Garden is a live musical album recorded by American singer and musician Elvis Presley and released in June 1972 by RCA Records peaking on the charts in July 1972.
- [d7s1]  Recorded at the Madison Square Garden arena in New York City on Saturday June 10, 1972, the concert, and the subsequent album, were promoted as being Presley's first live concerts in the Big Apple since the 1950s.
- [d7s2]  It was certified Gold on August 4, 1972, Platinum on May 20, 1988, 2x Platinum on March 27, 1992 and 3x Platinum on July 15, 1999 by the RIAA.
- [d7s3]  Along with "" it ranked as the top 1970's RCA live album by Elvis Presley.

**d8: A Date with Elvis (The Cramps album)**

- [d8s0] A Date with Elvis is the third full-length studio album by the American garage punk band the Cramps, released in the UK on Big Beat Records in 1986.
- [d8s1]  The title was appropriated from "A Date with Elvis" (1959), the eighth album by Elvis Presley.
- [d8s2]  The album was recorded in fall 1985 and engineered by Steve McMillan and Mark Ettel at Ocean Way Studios in Hollywood, California.
- [d8s3]  The album was first released in the US in 1990 by Enigma Records, with the bonus tracks "Blue Moon Baby", "Georgia Lee Brown", "Give Me a Woman" and "Get Off the Road".
- [d8s4]  The Cramps reissued the album (with bonus tracks) on their own Vengeance Records in 2001.
- [d8s5]  The original album was reissued in the UK by Big Beat in 2013 on orange vinyl, and subsequently reissued again by Vengeance Records in the US, UK and Canada in 2014.

**d9: Clearance Giddens**

- [d9s0] Clearance Giddens is an African American Elvis impersonator from Melfa, Virginia, who has been billed as the "Black Elvis".
- [d9s1]  He has appeared on the "The Arsenio Hall Show" and the "Geraldo Show", and in the film "Honeymoon in Vegas".
- [d9s2]  In the early 1990s, he also sang on stage in a duet with Jimmy Buffett singing "Jailhouse Rock".
- [d9s3]  He is listed in the book "I Am Elvis: A Guide to Elvis Impersonators".

**d10: Love Me Tender (song)**

- [d10s0] "Love Me Tender" is a 1956 song recorded by Elvis Presley and published by Elvis Presley Music from the eponymous 20th Century Fox film.
- [d10s1]  The words and music are credited to Ken Darby under the pseudonym "Vera Matson", the name of his wife, and Elvis Presley.
- [d10s2]  The RCA Victor recording by Elvis Presley was no. 1 on both the "Billboard" and "Cashbox" charts in 1956.
- [d10s3]  The song was adapted from the tune of "Aura Lee", a sentimental Civil War ballad.
- [d10s4]  The song is also featured in many other films such as "FM, Touched By Love, This is Elvis, Porky's Revenge, Wild at Heart, Die Hard 2, Honeymoon in Vegas, Backbeat, Gaudi Afternoon, Machine Gun Molly, , William Eggleston in the Real World, California Dreamin', Love in Space, Devil's Due, Just Before I Go," and "90 Minutes in Heaven."

## 22. hotpotqa_5ac250355542992f1f2b384b

原位置：`train` 第 202 题 · 全局第 202 题 · `sample_id: hotpotqa_5ac250355542992f1f2b384b`

Question: Who had more diverse credits in films, Charles Burnett or Patricio Guzmán?

Note: 

Type: comparison · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版 film credits；答案为文档列出的角色，不把旧人数 7/1 填入角色查询；结论比较角色多样性。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | film credits of Charles Burnett | False | [] | film director, film producer, writer, editor, actor, photographer, cinematographer | [["d1s0"]] | context |
| u2 | film credits of Patricio Guzmán | False | [] | documentary film director | [["d9s0"]] | context |
| u3 | who had more diverse film credits | True | ["u1", "u2"] | Charles Burnett | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | number of distinct film roles explicitly listed for Charles Burnett | False | [] | 7 | [['d1s0']] |
| u2 | number of distinct film roles explicitly listed for Patricio Guzmán | False | [] | 1 | [['d9s0']] |
| u3 | which of Charles Burnett and Patricio Guzmán has more distinct film roles explicitly listed by the documents | True | ['u1', 'u2'] | Charles Burnett | [[]] |

### Source documents (reference only)

**d1: Charles Burnett (director)**

- [d1s0] Charles Burnett (born April 13, 1944, in Vicksburg, Mississippi) is an African-American film director, film producer, writer, editor, actor, photographer, and cinematographer.
- [d1s1]  His most popular films include "Killer of Sheep" (1978), "My Brother's Wedding" (1983), "To Sleep with Anger" (1990), "The Glass Shield" (1994), and "" (2007).
- [d1s2]  He has been involved in other types of motion pictures including shorts, documentaries, and a TV series.

**d2: Selma, Lord, Selma**

- [d2s0] Selma, Lord, Selma is a 1999 American film based on true events that happened in March 1965, known as Bloody Sunday in Selma, Alabama.
- [d2s1]  The film tells the story through the eyes of an 11-year-old African-American girl named Sheyann Webb (Jurnee Smollett).
- [d2s2]  It was directed by Charles Burnett, one of the pioneers of black American independent cinema.
- [d2s3]  It premiered as a television movie on ABC on January 17, 1999.

**d3: Salvador Allende (film)**

- [d3s0] Salvador Allende is a 2004 documentary film about Chilean president Salvador Allende, from his election campaign to the "coup d'état" which ended his life.
- [d3s1]  It was directed by Patricio Guzmán and screened out of competition at the 2004 Cannes Film Festival.

**d4: Nostalgia for the Light**

- [d4s0] Nostalgia for the Light (Spanish: "Nostalgia de la Luz" ) is a documentary released in 2010 by Patricio Guzmán to address the lasting impacts of Augusto Pinochet’s dictatorship.
- [d4s1]  Guzmán focuses on the similarities between astronomers researching humanity’s past, in an astronomical sense, and the struggle of many Chilean women who still search, after decades, for the remnants of their relatives executed during the dictatorship.
- [d4s2]  Patricio Guzmán narrates the documentary himself and the documentary includes interviews and commentary from those affected and from astronomers and archeologists.

**d5: Killer of Sheep**

- [d5s0] Killer of Sheep is a 1978 American drama film written, directed, produced, and shot by Charles Burnett.
- [d5s1]  It features Henry G. Sanders, Kaycee Moore, and Charles Bracy, among others.
- [d5s2]  The drama depicts the culture of urban African-Americans in Los Angeles' Watts district.
- [d5s3]  The film's style is often likened to Italian neorealism.

**d6: Hey Joe**

- [d6s0] "Hey Joe" is an American popular song from the 1960s that has become a rock standard and has been performed in many musical styles by hundreds of different artists.
- [d6s1]  "Hey Joe" tells the story of a man who is on the run and planning to head to Mexico after shooting his unfaithful wife.
- [d6s2]  The song was registered for copyright in the U.S. in 1962 by Billy Roberts.
- [d6s3]  However, diverse credits and claims have led to confusion about the song's authorship.
- [d6s4]  The earliest known commercial recording of the song is the late-1965 single by the Los Angeles garage band The Leaves; the band then re-recorded the track and released it in 1966 as a follow-up single which became a hit.
- [d6s5]  The best-known version is The Jimi Hendrix Experience's 1966 recording.
- [d6s6]  The song title is sometimes given as "Hey Joe, Where You Gonna Go?"
- [d6s7]  or similar variations.

**d7: Austin Film Society**

- [d7s0] The Austin Film Society (AFS) is a non-profit film society based in Austin, Texas.
- [d7s1]  Founded in 1985 to exhibit independent, experimental, foreign and various other non-mainstream art films, the film society has grown from just film exhibition to fostering independent filmmaking in Texas and has served as a cornerstone in building the film industry in Austin.
- [d7s2]  The film society also owns and maintains Austin Studios, hosts the annual Texas Film Awards gala, and oversees the Austin Film Society grant program.
- [d7s3]  The film society was founded by film director Richard Linklater, who currently serves on the board as artistic director.
- [d7s4]  Other notable members on the board and advisory board include Tim McCanlies, Robert Rodriguez, Charles Burnett, Guillermo del Toro, Jonathan Demme, Mike Judge, John Sayles, Steven Soderbergh, Paul Stekler and Quentin Tarantino.

**d8: The Compass Rose (film)**

- [d8s0] The Compass Rose (Spanish: "La rosa de los vientos" ) is a 1983 Spanish drama film directed by Patricio Guzmán.
- [d8s1]  It was entered into the 13th Moscow International Film Festival.

**d9: Patricio Guzmán**

- [d9s0] Patricio Guzmán Lozanes (born August 11, 1941) is a Chilean documentary film director.
- [d9s1]  He is internationally renowned for films such as "The Battle of Chile" and "Salvador Allende".

**d10: The Pearl Button**

- [d10s0] The Pearl Button (Spanish: El botón de nácar ) is a 2015 Chilean documentary film directed by Patricio Guzmán.
- [d10s1]  It was screened in the main competition section of the 65th Berlin International Film Festival where it won the Silver Bear for Best Script.
- [d10s2]  It won the Lumières Award for Best Documentary at the 21st Lumières Awards.
- [d10s3]  The filmmaker has described the work as part of a triptych with "Nostalgia for the Light" and potentially a third film focusing on the Andes.

## 23. hotpotqa_5ac3aa9955429939154138a5

原位置：`train` 第 203 题 · 全局第 203 题 · `sample_id: hotpotqa_5ac3aa9955429939154138a5`

Question: What Chinese novel was the inspiration for the franchise where Sean Schemmel had his most famous or notable voice role?

Note: 

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | franchise where Sean Schemmel had his most famous or notable voice role | False | [] | Dragon Ball | [["d1s1"]] | context |
| u2 | Chinese novel that inspired {u1} | True | ["u1"] | Journey to the West | [["d5s2"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | franchise of Sean Schemmel's most notable voice role | False | [] | Dragon Ball | [['d1s1']] |
| u2 | Chinese novel that inspired {u1} | True | ['u1'] | Journey to the West | [['d5s2']] |

### Source documents (reference only)

**d1: Sean Schemmel**

- [d1s0] Sean Christian Schemmel (born November 21, 1968) is an American voice actor, ADR director, and screenwriter who has worked for Funimation, OkraTron 5000, NYAV Post, 4K Media Inc., Central Park Media and DuArt Film and Video.
- [d1s1]  He has provided voices for a number of English adaptations of Japanese anime, as well as various animated series and video games. His most notable voice role has been the adult version of Goku in the Funimation dub of the "Dragon Ball" anime franchise.

**d2: Ever Since We Love**

- [d2s0] Ever Since We Love is a 2015 Chinese film directed by Li Yu based on one of the stories in the 2001 Chinese novel "Everything Grows" by Feng Tang (the Chinese title is the same as the novel).
- [d2s1]  The film was released on April 17, 2015.

**d3: David Hawkes (sinologist)**

- [d3s0] David Hawkes (6 July 1923 – 31 July 2009) was a British sinologist and translator.
- [d3s1]  After being introduced to Japanese through codebreaking during the Second World War, Hawkes studied Chinese and Japanese at Oxford University between 1945 and 1947 before studying at Peking University from 1948 to 1951.
- [d3s2]  He then returned to Oxford, where he completed his D.Phil.
- [d3s3]  and later became Shaw Professor of Chinese.
- [d3s4]  In 1971, Hawkes resigned his position to focus entirely on his translation of the famous Chinese novel "The Story of the Stone" (also known as "Dream of the Red Chamber"), which was published in three volumes between 1973 and 1980.
- [d3s5]  He retired in 1984 to rural Wales before returning to Oxford in his final years.

**d4: Lucario**

- [d4s0] Lucario (ルカリオ , Rukario ) is a Pokémon species in Nintendo and Game Freak's "Pokémon" franchise.
- [d4s1]  Created by Ken Sugimori, Lucario first appeared as a central character in the film "", and later appeared in the video games "Pokémon Diamond" and "Pearl" and subsequent sequels, also appearing in various merchandise, spin-off titles and animated and printed adaptations of the franchise.
- [d4s2]  Lucario is voiced by Daisuke Namikawa, Daisuke Sakaguchi, Rikako Aikawa and Kiyotaka Furushima in Japanese, and Bill Rogers and Sean Schemmel in English.

**d5: Dragon Ball**

- [d5s0] Dragon Ball (Japanese: ドラゴンボール , Hepburn: Doragon Bōru ) is a Japanese media franchise created by Akira Toriyama.
- [d5s1]  The initial manga, written and illustrated by Toriyama, was serialized in "Weekly Shōnen Jump" from 1984 to 1995, with the 519 individual chapters collected into 42 "tankōbon" volumes by its publisher Shueisha.
- [d5s2]  "Dragon Ball" was initially inspired by the classical Chinese novel "Journey to the West".
- [d5s3]  The series follows the adventures of the protagonist, Son Goku, from his childhood through adulthood as he trains in martial arts and explores the world in search of the seven orbs known as the Dragon Balls, which summon a wish-granting dragon when gathered.
- [d5s4]  Along his journey, Goku makes several friends and battles a wide variety of villains, many of whom also seek the Dragon Balls.

**d6: Jad Saxton**

- [d6s0] Jād Brennon Saxton is an American voice actress who works for Funimation and Sentai Filmworks.
- [d6s1]  Her name is an acronym of her parents' names, Jimmy and David, and is pronounced as Jade.
- [d6s2]  Her singing led to her first voice role in "" as Eimi Mori, and her first major voice role was Masako Hara in "Ghost Hunt".
- [d6s3]  She graduated summa cum laude from Texas Wesleyan University with a Bachelor of Arts in Music in 2005.
- [d6s4]  Some of her other major roles in anime include Akatsuki in "Log Horizon", Carla in "Fairy Tail", Hatchin in "Michiko & Hatchin", Sena Kashiwazaki in "Haganai", Haruna in "Is This a Zombie?
- [d6s5] ", and Koneko Tojo in "High School DxD".

**d7: Yukari Tamura**

- [d7s0] Yukari Tamura (田村 ゆかり , Tamura Yukari , born February 27, 1976 in Fukuoka Prefecture) is a Japanese voice actress and singer affiliated with Amuleto, formerly Arts Vision and I'm Enterprise.
- [d7s1]  Affectionately called Yukarin by her fans, she is also known for her high-pitched voice and interest in Lolita fashion.
- [d7s2]  She debuted as a voice actress in 1997, releasing her debut single "Yūki o Kudasai" on March 26, 1997.
- [d7s3]  Several of her releases have been used as opening and ending themes for anime series, while some have reached the Oricon top 100 singles and album charts.
- [d7s4]  Her role as Nanoha Takamachi in the "Magical Girl Lyrical Nanoha" series contributed to a rise in her popularity, as several of her singles ("Little Wish: Lyrical Step", "Spiritual Garden", "Hoshizora no Spica", "Beautiful Amulet") were used as the ending themes for the franchise's anime adaptations.
- [d7s5]  Besides "Nanoha", she voices the title characters Haruka Minazuki / Red Angel in "Kaitō Tenshi Twin Angel", Ringo Kinoshita in "No-Rin", Yamada in "B Gata H Kei", and Kaoru Tsunashi in "I Can't Understand What My Husband Is Saying".
- [d7s6]  Other major voice roles in anime include Ranpha Franboise in "Galaxy Angel", Mai Kawasumi in "Kanon", Mei Sunohara in "Clannad", and Saku Tōyama in "Tantei Opera Milky Holmes", Rika Furude in "Higurashi When They Cry", and Tenten in "Naruto".
- [d7s7]  In video games, besides the ones that were adapted into anime, she voices Talim in "Soulcalibur" and Myao in "Marl Kingdom".
- [d7s8]  In tokusatsu, she is known for her voice role as Navi in 35th Super Sentai Series, "Kaizoku Sentai Gokaiger".

**d8: Mark Elliot (voice-over artist)**

- [d8s0] Mark Elliot (born September 24, 1939) is an American voice-over artist best known as the primary voice for Walt Disney Entertainment from 1983 to 2008.
- [d8s1]  He also provided voice overs for trailers of non-Disney films, logos, feature presentation bumpers and commercials.
- [d8s2]  He's well known for his voice overs in theatrical and home video trailers for films produced by The Walt Disney Studios from the 1980s to the 2000s.
- [d8s3]  He was also the voice of CBS and FOX throughout the 1980s and 1990s, and various theatrical trailers for such non-Disney animated movies as "All Dogs Go to Heaven", "The Seventh Brother", "Rover Dangerfield", "Rock-A-Doodle", "", "The Magic Voyage", "The Thief and the Cobbler", "Once Upon a Forest", "The Princess And The Goblin", "Andre", "Asterix Conquers America", "The Swan Princess", "The Pagemaster", "The Pebble and the Penguin", "Balto", "All Dogs Go to Heaven 2", "Tiny Heroes" ("Vacak 2 - az erdő hőse"), "Zeus and Roxanne", "The Fearless Four", "The Prince of Egypt", "The Adventures of Brer Rabbit", "", "House Arrest", and "".
- [d8s4]  In addition to his behind-the-scenes work, Elliott starred with four other notable voice artists in the 1997 short film "5 Men and a Limo".
- [d8s5]  One of his most well-known voice-overs for Disney is the catchphrase "And now, our feature presentation," which he says at the start of most animated Disney films on video on a "Feature Presentation" bumper.

**d9: Water Margin**

- [d9s0] Water Margin is a Chinese novel attributed to Shi Nai'an.
- [d9s1]  Considered one of the Four Great Classical Novels of Chinese literature, the novel is written in vernacular Chinese rather than Classical Chinese.

**d10: Dream of the Red Chamber Award**

- [d10s0] The Dream of the Red Chamber Award: The World's Distinguished Novel in Chinese (紅樓夢獎：世界華文長篇小說獎) is a biennial novel prize presented by Hong Kong Baptist University.
- [d10s1]  The prize is named after the famous Chinese novel "Dream of the Red Chamber".

## 24. hotpotqa_5ac3cbbd5542995ef918c23c

原位置：`train` 第 204 题 · 全局第 204 题 · `sample_id: hotpotqa_5ac3cbbd5542995ef918c23c`

Question: Which singer was a member of the band Mindless Self Indulgence, Jimmy Urine or Soyou?

Note: 

Type: comparison · fallback: False · SFT snapshots: 6

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | whether Jimmy Urine was a member of the band Mindless Self Indulgence | False | [] | yes | [["d1s1"], ["d5s4"]] | context |
| u2 | whether Soyou was a member of the band Mindless Self Indulgence | False | [] | no | [] | no_direct_support |
| u3 | which singer was a member of the band Mindless Self Indulgence | True | ["u1", "u2"] | Jimmy Urine | [[]] | question_presupposition |

- u2：无直接支持集合；不能仅由 expected_answer 将本单元标为 SUPPORTED。候选题结论可按独立的 presupposition_sets 路径判断。

- u3：`by_presupposition=true`，预设路径 `[["d1s1"], ["d5s4"]]`；不是直接证据。

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Jimmy Urine was a member of the band Mindless Self Indulgence | False | [] | yes | [['d1s1'], ['d5s4']] |
| u2 | whether Soyou was a member of the band Mindless Self Indulgence | False | [] | no | [] |
| u3 | which of Jimmy Urine and Soyou was a member of the band Mindless Self Indulgence | True | ['u1', 'u2'] | Jimmy Urine | [[]] |

### Source documents (reference only)

**d1: Jimmy Urine**

- [d1s0] James Euringer (born September 7, 1969), known professionally as Jimmy Urine, is an American singer, songwriter, and musician.
- [d1s1]  He is best known as the lead singer and programmer of electropunk band Mindless Self Indulgence.

**d2: The Left Rights (album)**

- [d2s0] The Left Rights is the self-titled debut album by the Mindless Self Indulgence side project featuring members Little Jimmy Urine and Steve, Righ?
- [d2s1] .
- [d2s2]  The album also contains a video of Mindless Self Indulgence performing "Panty Shot" live at CBGBs in New York City.

**d3: You'll Rebel to Anything**

- [d3s0] You'll Rebel to Anything is the third studio album by New York City band Mindless Self Indulgence released on April 12, 2005.
- [d3s1]  The album was released outside of the US on November 5, 2007, in an "Expanded and Remastered" edition.
- [d3s2]  On January 22, 2008, the "Expanded and Remastered" version was released in the US.
- [d3s3]  A special Japanese version of the remastered edition was released on March 5, 2008, which includes a demo version of "Bomb This Track", the completed version of which can be found on "If".

**d4: Alienating Our Audience**

- [d4s0] Alienating Our Audience is a live album by the band Mindless Self Indulgence, released on October 8, 2002 (see 2002 in music).
- [d4s1]  The album contains many fan favorites from the "Tight" era, as well as six previously unreleased tracks.
- [d4s2]  The recordings took place throughout the band's tour with System of a Down (February 14-March 1), but mostly pulled material from two shows: May 13 at CBGB's in New York City, NY and May 15 at The Whiskey A-Go-Go in Los Angeles, CA.

**d5: Liar (Fake Shark – Real Zombie! album)**

- [d5s0] Liar is the third album by Vancouver indie band Fake Shark – Real Zombie!
- [d5s1] .
- [d5s2]  It was released on February 14, 2013.
- [d5s3]  The album is a bit of direction change for the band, and the first with label, Light Organ Records.
- [d5s4]  Guests include Care Failure of the band Die Mannequin, Jimmy Urine of Mindless Self Indulgence, Steve Bays of Hot Hot Heat, and Henry Rollins.

**d6: On It**

- [d6s0] "On It" is a single by American electropunk band Mindless Self Indulgence, released in the U.S. on July 8, 2008.
- [d6s1]  The single reached number 2 on the "Billboard" Hot 100 Singles Sales chart.

**d7: Our Pain, Your Gain**

- [d7s0] Our Pain, Your Gain is the first live DVD release by New York-based punk band Mindless Self Indulgence, released on September 11, 2007.
- [d7s1]  The DVD is compiled from three shows the band played at New York, New York's Webster Hall in July 2005.

**d8: Tight (album)**

- [d8s0] Tight is the debut album by the American rock band Mindless Self Indulgence.
- [d8s1]  The album was originally released on April 20, 1999 through Uppity Cracker Recording Group.
- [d8s2]  After having been out of print for many years, the album was reissued as Tighter on April 26, 2011 through The End Records.
- [d8s3]  The reissue features updated artwork and packaging, 12 previously unreleased tracks, and a bonus DVD.

**d9: Ulrich Wild**

- [d9s0] Ulrich Wild is an American record producer, engineer and mixer specializing in the rock and metal genres.
- [d9s1]  Born and raised in Switzerland, Ulrich is now a naturalized citizen in the United States, living in Los Angeles, California.
- [d9s2]  In a career that has spanned over 20 years, his numerous credits include producing or engineering albums for bands such as Dethklok (a virtual metal band), Sex Slaves, Project 86, Pantera, Here Comes The Kraken, Static-X, Otep, Stabbing Westward, Powerman 5000, Deftones, Seether, Bleeding Through, Breaking Benjamin, Taproot, SOiL, World Entertainment War, and many other artists, and for soundtracks including "Freddy vs. Jason", "", and "House of Wax".
- [d9s3]  He has also remixed songs by the band Mindless Self Indulgence.
- [d9s4]  He was nominated for a Grammy for best engineered non-classical album in 1995 for his work with White Zombie.

**d10: Soyou**

- [d10s0] Kang Ji-hyun (Hangul: 강지현 ; born February 12, 1992), better known by her stage name Soyou (소유 ), is a South Korean singer.
- [d10s1]  She is best known as a former member of the South Korean girl group Sistar under Starship Entertainment.

## 25. hotpotqa_5ac445975542995c82c4ad16

原位置：`train` 第 205 题 · 全局第 205 题 · `sample_id: hotpotqa_5ac445975542995c82c4ad16`

Question: Which historic edifice has been a focal point of global and national activism since its inception, 1 Wall Street or Riverside Church?

Note: 

Type: comparison · fallback: False · SFT snapshots: 6

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | whether 1 Wall Street has been a focal point of global and national activism since its inception | False | [] | no | [] | no_direct_support |
| u2 | whether Riverside Church has been a focal point of global and national activism since its inception | False | [] | yes | [["d2s6"]] | context |
| u3 | which historic edifice has been a focal point of global and national activism since its inception | True | ["u1", "u2"] | Riverside Church | [[]] | question_presupposition |

- u1：无直接支持集合；不能仅由 expected_answer 将本单元标为 SUPPORTED。候选题结论可按独立的 presupposition_sets 路径判断。

- u3：`by_presupposition=true`，预设路径 `[["d2s6"]]`；不是直接证据。

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Riverside Church has been a focal point of global and national activism since its inception | False | [] | yes | [['d2s6']] |
| u2 | whether 1 Wall Street has been a focal point of global and national activism since its inception | False | [] | no | [] |
| u3 | which of 1 Wall Street and Riverside Church has been a focal point of global and national activism since its inception | True | ['u1', 'u2'] | Riverside Church | [[]] |

### Source documents (reference only)

**d1: Alabama City Wall Street Historic District**

- [d1s0] The Alabama City Wall Street Historic District is a historic district in Gadsden, Alabama.
- [d1s1]  Wall Street was the main commercial street in the town of Alabama City.
- [d1s2]  The city was founded in 1891 halfway between Gadsden and Attalla, with intentions of becoming the major industrial hub of Northeast Alabama.
- [d1s3]  In 1895 the town landed its first major concern, a cotton mill built by the Dwight Manufacturing Company of Chicopee, Massachusetts.
- [d1s4]  Its second major factory, the Alabama Steel and Wire Company, was opened in 1902.
- [d1s5]  By 1915, a thriving commercial district had grown up around 7th Avenue, which became known as "Little Wall Street".
- [d1s6]  A fire in 1927 damaged or destroyed many structures along Wall Street and Meighan Avenue.
- [d1s7]  The city would never recover from the loss, especially as neighboring Gadsden flourished; Alabama City voted to merge into Gadsden in 1932.
- [d1s8]  The architecture of the district represent the changing commercial styles of the 1910s through the 1930s.
- [d1s9]  Most are constructed in simple, brick styles with parapet roofs, some with more decorative brickwork.
- [d1s10]  Art Deco-influenced features such as terra cotta coping and glass tile accents are present on later buildings.
- [d1s11]  Other notable buildings are an Art Deco fire station (built 1936) and the Classical Revival library (built 1938).
- [d1s12]  The district was listed on the National Register of Historic Places in 2002.

**d2: Riverside Church**

- [d2s0] Riverside Church is a Christian church in Morningside Heights, Upper Manhattan, New York City.
- [d2s1]  It opened its doors on October 5, 1930.
- [d2s2]  It is situated at 120th Street and 490 Riverside Drive, within the Columbia University Morningside Heights Campus, across the street from, and one block south of, President Grant's Tomb.
- [d2s3]  Although interdenominational, it is also associated with the American Baptist Churches USA and the United Church of Christ.
- [d2s4]  It is famous for its large size and elaborate Neo-Gothic architecture as well as its history of social justice.
- [d2s5]  It was described by "The New York Times" in 2008 as "a stronghold of activism and political debate throughout its 75-year history ... influential on the nation's religious and political landscapes."
- [d2s6]  It has been a focal point of global and national activism since its inception.

**d3: Downtown Anaheim**

- [d3s0] Downtown Anaheim is the administrative and historic center of Anaheim, California.
- [d3s1]  It is also known as Anaheim Colony Historic District and is bordered by East, West, North, and South streets.
- [d3s2]  The historic center of the city is Anaheim Blvd (originally named Los Angeles Street) and Center Street.
- [d3s3]  Unlike most big city downtowns, Downtown Anaheim is not the economic heart and focal point of this city.
- [d3s4]  The economic heart and focal point of Anaheim and Orange County is the adjacent district just south of Downtown Anaheim —the Anaheim Resort District, which includes the Disneyland Resort and the Anaheim Convention Center.
- [d3s5]  Another prominent district located south east of Downtown Anaheim, and adjacent to the Anaheim Resort, is the Platinum Triangle District.

**d4: The Wall Street Journal Europe**

- [d4s0] The Wall Street Journal Europe is a daily English-language newspaper that covers global and regional business news for Europe, the Middle East and Africa (EMEA).
- [d4s1]  Published by Dow Jones & Company (a News Corp company), it forms part of the business publication franchise which includes "The Wall Street Journal", "The Wall Street Journal Asia", and The Wall Street Journal Online (WSJ.com).
- [d4s2]  Together, these publications have a total circulation of 3.8 million.

**d5: St. Andrew's Church (LeRoy, Wisconsin)**

- [d5s0] St. Andrew's Church is a historic Roman Catholic church in LeRoy, Wisconsin, United States.
- [d5s1]  The Gothic Revival church was designed by architect Anton Dohmen and built 1899-1901, largely by parishioners.
- [d5s2]  The Emil Frei Stained Glass Company later added over 20 stained glass windows to the church; these windows were described as "works of art with vivid colors and intricate details" by the Wisconsin Historical Society.
- [d5s3]  The church's congregation was composed of German farmers from the surrounding area, who paid for the church and constructed parts of its interior; the church has historically served as a focal point for community life.
- [d5s4]  The church has been called the "Cathedral on the Marsh" due to its proximity to the Horicon Marsh.
- [d5s5]  On January 27, 2010, the church was added to the National Register of Historic Places.

**d6: Sarisbury**

- [d6s0] Sarisbury is a village to the west of Park Gate within the borough of Fareham.
- [d6s1]  Its focal point, The Green, originated as a tongue of land at the extremity of Titchfield Common which was left when the rest was enclosed.
- [d6s2]  Its focal point is still the parish church of St Paul, built in 1836 to a design by Jacob Owen.
- [d6s3]  In previous times it was a rural locality dependent on fruit growing, but is now largely populated by urban workers who commute to Fareham, Southampton or even London from the nearby Swanwick railway station.
- [d6s4]  At the 2011 Census the population of the ward was 7,385.

**d7: 1 Wall Street**

- [d7s0] One Wall Street (originally the Irving Trust Company Building, then the Bank of New York Building after 1988, and now known as the BNY Mellon Building since 2007), is an Art-Deco-style skyscraper in Lower Manhattan, New York City.
- [d7s1]  It is located in Manhattan's Financial District on the corner of Wall Street and Broadway.
- [d7s2]  Up until September 30, 2015, it served as the global headquarters of The Bank of New York Mellon Corporation.
- [d7s3]  In May, 2014 the bank sold the building to a joint venture led by Harry B. Macklowe's Macklowe Properties for $585 million.

**d8: 1 Wall Street Court**

- [d8s0] 1 Wall Street Court in the Financial District of Manhattan, also known as The Beaver Building and The Cocoa Exchange (as the former home of the New York Cocoa Exchange) is a triangular-shaped building reminiscent of the Flatiron Building.
- [d8s1]  The building, designed by Clinton and Russell and completed in 1904, is located at the intersection of Wall Street, Pearl Street, and Beaver Street.

**d9: Wall Street reform**

- [d9s0] Wall Street Reform or Financial Reform refers to reform of the financial industry and the regulation of the financial industry in the United States.
- [d9s1]  Wall Street is the home of the country's two largest stock exchanges, and "Wall Street" is a metonym for the American financial sector.
- [d9s2]  Major Wall Street reform bills include the Federal Reserve Act of 1913, the Glass-Steagall Act of 1933, the Truth in Lending Act of 1968, the Community Reinvestment Act of 1977, the Gramm–Leach–Bliley Act of 1999, and the Sarbanes-Oxley Act of 2002.
- [d9s3]  The most recent Wall Street reform bill, the Dodd–Frank Wall Street Reform and Consumer Protection Act, was signed by President of the United States Barack Obama on July 22, 2010, following a global financial crisis.

**d10: G. H. Walker &amp; Co.**

- [d10s0] G.H. Walker & Co. was an investment banking and brokerage firm founded in 1900 by George Herbert Walker, grandfather and great-grandfather of Presidents George Herbert Walker Bush and George Walker Bush, and located at 1 Wall Street.

## 26. hotpotqa_5ac51d3355429924173fb5be

原位置：`train` 第 206 题 · 全局第 206 题 · `sample_id: hotpotqa_5ac51d3355429924173fb5be`

Question: Are Welcome to Nollywood and Burma VJ both documentary films?

Note: 

Type: comparison · fallback: False · SFT snapshots: 6

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | whether Welcome to Nollywood is a documentary film | False | [] | yes | [["d10s0"], ["d8s0"]] | context |
| u2 | whether Burma VJ is a documentary film | False | [] | yes | [["d4s0"]] | context |
| u3 | whether both Welcome to Nollywood and Burma VJ are documentary films | True | ["u1", "u2"] | yes | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | whether Welcome to Nollywood is a documentary film | False | [] | yes | [['d10s0'], ['d8s0']] |
| u2 | whether Burma VJ is a documentary film | False | [] | yes | [['d4s0']] |
| u3 | whether Welcome to Nollywood and Burma VJ are both documentary films | True | ['u1', 'u2'] | yes | [[]] |

### Source documents (reference only)

**d1: Zhou Bing**

- [d1s0] Zhou Bing (simplified Chinese: 周兵; pinyin: Zhōu Bing , Zhoubing ; born 1 April 1968), famous Chinese documentary director, a PhD from History College of Nankai University, have successively served as the column scenarist and special program production manager of the program titled with “Oriental Biography” and director of special program division of CND Film Group.
- [d1s1]  Zhou Bing was titled with annual director of Chinese documentary film for three times, and the documentary films created and produced by him amounts to 100 hundred units.
- [d1s2]  His masterpieces including Palace, Dun Huang and "Road of Millenia Bodhi were" aired on CCTV, National Geographic, SKY TV, History Channel, Arte, and NDR.
- [d1s3]  Currently he establishes Beijing Oriental Elites Culture Development Co Ltd and works with Tiong Hiew King, the datuk of Tan Sri, Malaysia to setup Sun Media International Co. Ltd and Zero Media International Co. Ltd.
- [d1s4]  Zhou Bing attempted to join in the development of industrialization process of documentary films with the identity of independent directors.
- [d1s5]  Zhou Bing is also a Adjunct Professor in the Department of Media and Communication of City University of Hong Kong.
- [d1s6]  It is art dream of Mr Zhou who has been desiring to realize through images to broadcast Chinese culture and to build oriental aesthetic approach with the images recognized by the world.

**d2: VJ Adams**

- [d2s0] Adams Ibrahim Adebola (born 5 May 1988), popularly known as VJ Adams, is a Nigerian video jockey, television presenter, entrepreneur, musician cum executive producer.
- [d2s1]  His journey into limelight came after he contested at the 2008 edition of Next Movie Star West Africa.
- [d2s2]  VJ Adams is renowned as a presenter on "Soundcity TV", a Nigerian music channel based in Lagos.
- [d2s3]  He co-anchored the Official Red Carpet at the 8th Africa Movie Academy Award with Nollywood Actress, Alex Okoroji and co-anchored 2014 edition of City People Entertainment Awards ceremony which was held in Lagos.

**d3: Andy Whittaker**

- [d3s0] Andy Whittaker is the founder of UK film distributor Dogwoof, who focus on social issue films such as "Food, Inc." and "Burma VJ".

**d4: Burma VJ**

- [d4s0] Burma VJ: Reporting from a Closed Country is a 2008 Danish documentary film directed by Anders Østergaard.
- [d4s1]  It follows the Saffron Revolution against the military regime in Burma.
- [d4s2]  The "VJ" in the title stands for "video journalists."
- [d4s3]  Some of it was filmed on hand-held cameras.
- [d4s4]  The footage was smuggled out of the country, physically or over the Internet.
- [d4s5]  Other parts of it were reconstructed, which caused controversy.

**d5: Boulder International Film Festival**

- [d5s0] The Boulder International Film Festival (BIFF), sponsored by the Colorado Film Society, is held annually on Presidents Day Weekend in Boulder, Colorado USA, and has developed a reputation as one of the most compelling young film festivals in the U.S., exhibiting a number of new-but-unknown feature films, documentaries, animations, and shorts that have gone on to significant box-office success and multiple Oscar nominations, including "Monsieur Lazhar, Burma VJ, Revanche, Wasp, Miracle Fish, The Conscience of Nhem Eh, Waste Land, Incident in New Baghdad, Instead of Abracadabra, Raju, The Fantastic Flying Books of Mr. Morris Lessmore, West Bank Story, The Secret of Kells, 5 Broken Cameras, Chasing Ice, Curfew, Asad," "The Missing Picture," and "The Wind Rises."
- [d5s1]  More than 23,600 filmmakers, national media, special guests and film enthusiasts attended the four-day BIFF 2014.

**d6: Jamie Meltzer**

- [d6s0] Jamie Meltzer is an American movie and documentary film director.
- [d6s1]  He has made "True Conviction", ""Off the Charts: The Song-Poem Story"", ""Welcome to Nollywood"", ""La Caminata"" (a short film), and the feature-length documentary film ""Informant"".
- [d6s2]  He teaches documentary film production in the Art Department of Stanford University, as part of the MFA Program in Documentary Film.

**d7: Yair Qedar**

- [d7s0] Yair Qedar (Hebrew: יאיר קדר‎ ‎ , born June 13, 1969) is an Israeli filmmaker and a civil-rights activist.His academic training on 20th-century Hebrew literature (Tel Aviv University), propelled him into to The Hebrews — a trans media project on the Hebrew literary canon, centered on filmic portraits of the Hebrew writers.
- [d7s1]  Eight documentary films were made in this framwork and six others are currently shot.
- [d7s2]  The documentary films which he produced, wrote and directed are —"Bialik - King of the Jews", "The 5 Houses of Lea Goldberg" and "The Seven Tapes of Yona Wallach", 'the Awakener - the story of Y.H Brener' and 'Simple Woman -Zelda'— as well as the three films which he produced in the project - "Song of loves, Rabbi David Bouzaglo", "the Raven, Zeev Jabotinki" and "Mrs Rachel Bluestein" – aired on Israeli TV, circulated far and wide in cinematheques, community and cultural centers, in Israel and around the world (USA and Canada, Europe, Australia and Russia) earning 10 awards (2016: first prize for filmmaking in the field of Jewish culture by the ministry of Education in Israel, 2015: the "Hebrews" films won the prize for best television project in the Israeli Documentary competition).
- [d7s3]  The project, both digital and print, offers altogether eight documentary films, a video archive and several books.

**d8: This Is Nollywood**

- [d8s0] This Is Nollywood is a 2007 Nigerian documentary film by Franco Sacchi and Robert Caputo, detailing the Nigerian film industry, much along the same lines as the acclaimed 2007 documentary "Welcome to Nollywood" by Jamie Meltzer

**d9: Shan George**

- [d9s0] Shan George is a Nollywood actress, singer, film producer and director.
- [d9s1]  Prior to debuting in the movie "Thorns of Rose", she had previously featured in a 1997 soap opera titled "Winds of Destiny".
- [d9s2]  She is best known for her role in the movies "Outkast" and "Welcome to Nollywood".

**d10: Welcome to Nollywood**

- [d10s0] Welcome to Nollywood is a 2007 documentary film directed by Jamie Meltzer, which premiered at the Full Frame Documentary Film Festival, and also played at the Avignon Film Festival and the Melbourne International Film Festival in the summer of 2007.

## 27. hotpotqa_5adbf7d855429947ff173879

原位置：`train` 第 207 题 · 全局第 207 题 · `sample_id: hotpotqa_5adbf7d855429947ff173879`

Question: Which group contains more species, Willow or Stipa?

Note: 

Type: comparison · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | number of species in Willow | False | [] | around 400 | [["d3s0"]] | context |
| u2 | number of species in Stipa | False | [] | around 300 | [["d10s0"]] | context |
| u3 | which group contains more species | True | ["u1", "u2"] | Willow | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | number of species of willow | False | [] | around 400 | [['d3s0']] |
| u2 | number of species in the genus Stipa | False | [] | around 300 | [['d10s0']] |
| u3 | which of Willow and Stipa contains more species | True | ['u1', 'u2'] | Willow | [[]] |

### Source documents (reference only)

**d1: Formica rufa species group**

- [d1s0] The "Formica rufa" group is a subgeneric group within the genus "Formica", first proposed by William Morton Wheeler.
- [d1s1]  This group contains the mound-building species of "Formica" commonly termed "wood ants" or "thatch-mound ants", which build prominent nests consisting of a mound of grass, litter, or conifer needles.
- [d1s2]  The species "Formica rufa" or the red wood ant is the type species of this sub group.

**d2: Chrysidinae**

- [d2s0] The subfamily Chrysidinae contains those species that are most commonly recognized as cuckoo wasps, being by far the largest and most familiar subfamily.
- [d2s1]  The group contains some 3000 species in 48 genera in four tribes worldwide.
- [d2s2]  They are highly sculptured, with brilliantly metallic-coloredbodies, and capable of folding their bodies over (or, more commonly, rolling into a ball) as a defensive mechanism.
- [d2s3]  They are most diverse in desert regions of the world, as they are typically associated with solitary bee and wasp species, which are also most diverse in such areas.

**d3: Willow**

- [d3s0] Willows, also called sallows, and osiers, form the genus Salix, around 400 species of deciduous trees and shrubs, found primarily on moist soils in cold and temperate regions of the Northern Hemisphere.
- [d3s1]  Most species are known as willow, but some narrow-leaved shrub species are called osier, and some broader-leaved species are referred to as sallow (from Old English "sealh", related to the Latin word "salix", willow).
- [d3s2]  Some willows (particularly arctic and alpine species) are low-growing or creeping shrubs; for example, the dwarf willow ("Salix herbacea") rarely exceeds 6 cm in height, though it spreads widely across the ground.

**d4: List of cotingas**

- [d4s0] The cotingas (Cotingidae) are a clade of suboscines bird species of neotropical distribution in South America and Central America.
- [d4s1]  The group contains more than 60 living species and is in the clade Tyrannides (along with Pipridae, Oxyruncidae, Onychorhynchidae, Tityridae, Pipritidae, Platyrinchidae, Tachurididae, Rhynchocyclidae, Tyrannidae, Melanopareiidae, Conopophagidae, Thamnophilidae, Grallariidae, Rhinocryptidae, Formicariidae, and Furnariidae).

**d5: Piperaceae**

- [d5s0] The Piperaceae, also known as the pepper family, are a large family of flowering plants.
- [d5s1]  The group contains roughly 3,600 currently accepted species in 13 genera.
- [d5s2]  The vast majority of peppers can be found within the two main genera: "Piper" (2000 species) and "Peperomia" (1600 species).

**d6: Swiftlet**

- [d6s0] Swiftlets are birds contained within the four genera "Aerodramus", "Hydrochous", "Schoutedenapus" and "Collocalia".
- [d6s1]  They form the Collocaliini tribe within the swift family Apodidae.
- [d6s2]  The group contains around thirty species mostly confined to southern Asia, south Pacific islands, and northeastern Australia, all within the tropical and subtropical regions.
- [d6s3]  They are in many respects typical members of the Apodidae, having narrow wings for fast flight, with a wide gape and small reduced beak surrounded by bristles for catching insects in flight.
- [d6s4]  What distinguishes many but not all species from other swifts and indeed almost all other birds is their ability to use a simple but effective form of echolocation to navigate in total darkness through the chasms and shafts of the caves where they roost at night and breed.
- [d6s5]  The nests of some species are built entirely from threads of their saliva, and are collected for the famous Chinese delicacy bird's nest soup.

**d7: Salix sepulcralis group**

- [d7s0] The "Salix sepulcralis" group is a cultivar group containing all cultivars of hybrids between "Salix alba" and "Salix babylonica".
- [d7s1]  The "sepulcralis" or × "sepulcralis" trees are sometimes referred to as white weeping willow or glaucous weeping willow in reference to the mixed appearance from the parent species.
- [d7s2]  It was first described by L. Simonkai in 1890 from trees growing in Romania.
- [d7s3]  The group contains both weeping and nonweeping cultivars, though the best-known of its cultivars is 'Chrysocoma', the most widely grown weeping tree.
- [d7s4] .

**d8: Cuckoo paper wasp**

- [d8s0] The name cuckoo paper wasp refers to a monophyletic species group of brood-parasitic paper wasps in the genus "Polistes".
- [d8s1]  This species group contains only three species; "Polistes atrimandibularis", "P. semenowi", and "P. sulcifer", all of them obligate social parasites on other "Polistes" species.

**d9: Ostariophysi**

- [d9s0] Ostariophysi is the second-largest superorder of fish.
- [d9s1]  Members of this superorder are called ostariophysians.
- [d9s2]  This diverse group contains almost 8,000 species, about 28% of known fish species in the world and 68% of freshwater species, and are present on all major continents except Antarctica.
- [d9s3]  They have a number of common characteristics such as an alarm substance and a Weberian apparatus.
- [d9s4]  Members of this group include fish important to people for food, sport, the aquarium industry, and research.

**d10: Stipa**

- [d10s0] Stipa is a genus of around 300 large perennial hermaphroditic grasses collectively known as feather grass, needle grass, and spear grass.
- [d10s1]  They are placed in the subfamily Pooideae and the tribe Stipeae.

## 28. hotpotqa_5adc0b3a5542996e685252b8

原位置：`train` 第 208 题 · 全局第 208 题 · `sample_id: hotpotqa_5adc0b3a5542996e685252b8`

Question: What live-action television series was produced for Adult Swim and had Kristen Joy Schaal as an actor?

Note: 

Type: bridge · fallback: False · SFT snapshots: 6

### Adjusted units and annotation

**执行结果：** 保留三单元交集结构；u2 联合真人剧、演员及全名对应证据，u3 依赖两方，不使用旧第二跳直接证据冒充结论。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | live-action television series produced for Adult Swim | False | [] | The Heart, She Holler | [["d3s0"]] | context |
| u2 | live-action television series with Kristen Joy Schaal as an actor | False | [] | The Heart, She Holler | [["d3s0", "d3s1", "d10s0"]] | context |
| u3 | live-action television series that is both {u1} and {u2} | True | ["u1", "u2"] | The Heart, She Holler | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | television series in which Kristen Joy Schaal acted | False | [] | The Heart, She Holler | [['d10s1'], ['d3s1']] |
| u2 | live-action television series produced for Adult Swim with Kristen Joy Schaal as an actor, given {u1} | True | ['u1'] | The Heart, She Holler | [['d3s0']] |

### Source documents (reference only)

**d1: Dream Corp, LLC**

- [d1s0] Dream Corp, LLC is an American live-action/animated television series created by Daniel Stessen for Adult Swim.
- [d1s1]  The series concerns Dr. Roberts (Jon Gries) and his team of dream-analyzing doctors at an eponymous psychotherapeutic facility.
- [d1s2]  The series is the first on Adult Swim to use rotoscoping.
- [d1s3]  It premiered on October 23, 2016.

**d2: List of The Brak Show episodes**

- [d2s0] This is a list of episodes for the animated Adult Swim television series, "The Brak Show".
- [d2s1]  The pilot episode, "Mr. Bawk Ba Gawk", aired unannounced on December 21, 2000, on Cartoon Network.
- [d2s2]  The series officially premiered with "Goldfish" on September 2, 2001, on Adult Swim, and ended with three seasons and 28 episodes on December 31, 2003, with "Cardburkey".
- [d2s3]  On May 24, 2007, an additional webisode entitled "Space Adventure" was released on Adult Swim Video, no further webisodes have ever been produced.

**d3: The Heart, She Holler**

- [d3s0] The Heart, She Holler is a live-action television series produced by Vernon Chatman, John Lee and Alyson Levy for Adult Swim.
- [d3s1]  The series, described as "Southern Gothic drama" and "an inside-out blend of soap opera and politically incorrect surrealist comedy", is about the long-hidden and isolated son of the Heartshe dynasty – played by Patton Oswalt – returning to run the town and being locked in conflict with sisters Hurshe played by Kristen Schaal and Amy Sedaris and also Hambrosia played by Heather Lawless.
- [d3s2]  The show premiered on November 6, 2011, for a six-episode first season.
- [d3s3]  A 14-episode second season premiered on September 11, 2013, and a third season premiered in December 2014.

**d4: Sealab 2021**

- [d4s0] Sealab 2021 is an American adult animated television series created by Adam Reed and Matt Thompson.
- [d4s1]  It was shown on Cartoon Network's late-night programming block, Adult Swim.
- [d4s2]  Cartoon Network aired the show's first three episodes in December 2000 before the official inception of the Adult Swim channel on September 2, 2001, with the final episode airing on April 25, 2005.
- [d4s3]  "Sealab 2021" is a spin-off of "Space Ghost Coast to Coast", and is one of the four original Williams Street series that premiered in 2000 before Adult Swim officially launched, the others being "Aqua Teen Hunger Force", "The Brak Show" and "Harvey Birdman, Attorney at Law".

**d5: Your Pretty Face Is Going to Hell**

- [d5s0] Your Pretty Face Is Going to Hell is an American live-action television series on Cartoon Network's late night programming block, Adult Swim.
- [d5s1]  The series made its official debut on April 18, 2013, on Adult Swim.
- [d5s2]  The show is a live-action workplace comedy about Gary, an associate demon, as he attempts to capture souls on earth in order to climb the corporate ladder of the underworld.
- [d5s3]  Gary hopes to advance in Hell, but he may be too stupid, lazy and kind-hearted to realize his dreams of promotion.

**d6: Rick and Morty (season 3)**

- [d6s0] The third season of the animated television series "Rick and Morty" originally aired in the United States on Cartoon Network's late night programming block, Adult Swim.
- [d6s1]  It premiered with "The Rickshank Rickdemption," which aired unannounced on April 1, 2017 and was replayed every half hour from 8pm to 12am ET, as part of Adult Swim's annual April Fools' prank.
- [d6s2]  The episode was also simulcast as a looping live stream on Adult Swim's site.
- [d6s3]  The remaining episodes began airing on July 30, 2017.
- [d6s4]  The season will feature a total of 10 episodes.

**d7: Mike Tyson Mysteries**

- [d7s0] Mike Tyson Mysteries is an American adult animated television series, and the first to be produced by Warner Bros.
- [d7s1]  Animation for Adult Swim.
- [d7s2]  It premiered October 27, 2014.
- [d7s3]  The series features Mike Tyson solving mysteries, in the style of "", "Scooby-Doo!
- [d7s4] ", "Jonny Quest" and "Mr. T".
- [d7s5]  On December 10, 2014, Adult Swim renewed the series for a second season, which premiered on November 1, 2015.
- [d7s6]  A third season premiered on May 14, 2017.
- [d7s7]  The show has been renewed for a fourth season.

**d8: Mostly 4 Millennials**

- [d8s0] Mostly 4 Millennials is an upcoming American comedy television series on Adult Swim.
- [d8s1]  The series, a look at the Millennial generation, is created by comedian Derrick Beckles and produced by Eric Andre.
- [d8s2]  Beckles formerly created "Totally for Teens" for Adult Swim in 2011.

**d9: G.I. Joe: Resolute**

- [d9s0] G.I. Joe: Resolute is an animated television series based on the G.I. Joe franchise.
- [d9s1]  It was written by Warren Ellis, directed by Joaquim Dos Santos, and produced by Sam Register.
- [d9s2]  It debuted on the web at Adult Swim Video April 18, 2009 as a series of ten 5-minute episodes and one 10-minute final episode, with a Content Rating of TV-14-V, and premiered in its entirety as a 60-minute movie on air on Canadian television network Teletoon on April 24, 2009.
- [d9s3]  In the United States, the movie aired on Adult Swim April 26, 2009.
- [d9s4]  "Resolute" departs from recent depictions of futuristic technology, adopting a more realistic aesthetic.
- [d9s5]  It has been described as a more "mature" take on the franchise.
- [d9s6]  The film uses elements from both the cartoons and the comics, and is described by Warren Ellis as a "fusion".

**d10: Kristen Schaal**

- [d10s0] Kristen Joy Schaal ( ; born January 24, 1978) is an American comedian, actress, voice artist and writer.
- [d10s1]  She is known for her roles of Mel on the HBO series "Flight of the Conchords", The Heart, She Holler as over-sexed Hurshe, Louise Belcher on FOX animated comedy "Bob's Burgers", and Mabel Pines on "Gravity Falls".
- [d10s2]  Other roles include her appearances as a commentator on "The Daily Show", Amanda Simmons on "The Hotwives of Orlando", Hazel Wassername on "30 Rock", Victoria Best on "WordGirl", Trixie from the "Toy Story" franchise, Anne on "Wilfred" and she has appeared on Celebrity Family Feud.
- [d10s3]  Since 2015, she has co-starred alongside Will Forte in the Fox comedy "The Last Man on Earth", playing the role of Carol.
- [d10s4]  She was nominated for a Primetime Emmy for her role of Sarah Lynn in "BoJack Horseman".

## 29. hotpotqa_5add1b765542990d50227de3

原位置：`train` 第 209 题 · 全局第 209 题 · `sample_id: hotpotqa_5add1b765542990d50227de3`

Question: During which years was the German politician, who issued the Nero Decree, Chancellor of Germany?

Note: 

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | German politician who issued the Nero Decree | False | [] | Adolf Hitler | [["d3s0"]] | context |
| u2 | years {u1} was Chancellor of Germany | True | ["u1"] | 1933 to 1945 | [["d2s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | German politician who issued the Nero Decree | False | [] | Adolf Hitler | [['d3s0']] |
| u2 | years during which {u1} was Chancellor of Germany | True | ['u1'] | 1933 to 1945 | [['d2s0']] |

### Source documents (reference only)

**d1: Gerhard Schröder**

- [d1s0] Gerhard Fritz Kurt Schröder (] ; born 7 April 1944) is a German politician, and served as Chancellor of Germany from 1998 to 2005.
- [d1s1]  As a member of the Social Democratic Party of Germany (SPD), he led a coalition government of the SPD and the Greens.
- [d1s2]  Before becoming a full-time politician, he was a lawyer, and before becoming Chancellor he served as Prime Minister of Lower Saxony (1990–1998).
- [d1s3]  Following the 2005 federal election, which his party lost, after three weeks of negotiations he stood down as Chancellor in favour of Angela Merkel of the rival Christian Democratic Union.
- [d1s4]  He is currently the chairman of the board of Nord Stream AG, after having been hired as a global manager by investment bank Rothschild, and also the chairman of the board of football club Hannover 96.

**d2: Adolf Hitler**

- [d2s0] Adolf Hitler (] ; 20 April 1889 – 30 April 1945) was a German politician who was the leader of the Nazi Party ("Nationalsozialistische Deutsche Arbeiterpartei"; NSDAP), Chancellor of Germany from 1933 to 1945 and Führer ("Leader") of Nazi Germany from 1934 to 1945.
- [d2s1]  As dictator, Hitler initiated World War II in Europe with the invasion of Poland in September 1939, and was central to the Holocaust.

**d3: Nero Decree**

- [d3s0] The Nero Decree (German: "Nerobefehl" ) was issued by Adolf Hitler on March 19, 1945 ordering the destruction of German infrastructure to prevent their use by Allied forces as they penetrated deep within Germany.
- [d3s1]  It was officially titled Demolitions on Reich Territory Decree ("Befehl betreffend Zerstörungsmaßnahmen im Reichsgebiet") and has subsequently become known as the Nero Decree, after the Roman Emperor Nero, who supposedly engineered the Great Fire of Rome in 64 AD.
- [d3s2]  The decree was deliberately disobeyed by Albert Speer.

**d4: Reichstag Fire Decree**

- [d4s0] The Reichstag Fire Decree (German: "Reichstagsbrandverordnung" ) is the common name of the Decree of the Reich President for the Protection of People and State (German: "Verordnung des Reichspräsidenten zum Schutz von Volk und Staat" ) issued by German President Paul von Hindenburg on the advice of Chancellor Adolf Hitler on 28 February 1933 in immediate response to the Reichstag fire.
- [d4s1]  The decree nullified many of the key civil liberties of German citizens.
- [d4s2]  With Nazis in powerful positions in the German government, the decree was used as the legal basis for the imprisonment of anyone considered to be opponents of the Nazis, and to suppress publications not considered "friendly" to the Nazi cause.
- [d4s3]  The decree is considered by historians as one of the key steps in the establishment of a one-party Nazi state in Germany.

**d5: Egon Franke (politician)**

- [d5s0] Egon Franke (11 April 1913 – 26 April 1995) was a German politician and a member of the Social Democratic Party of Germany.
- [d5s1]  He was Federal Minister for Intra-German Relations from 1969 to 1982 and Vice Chancellor of West Germany in 1982.
- [d5s2]  With a tenure of 14 days he was the Vice Chancellor with the shortest time in office.

**d6: Horst Köhler**

- [d6s0] Horst Köhler (] ; born 22 February 1943) is a German politician of the Christian Democratic Union, and served as President of Germany from 2004 to 2010.
- [d6s1]  As the candidate of the two Christian Democratic sister parties, the CDU and the CSU, and the liberal FDP, Köhler was elected to his first five-year term by the Federal Assembly on 23 May 2004 and was subsequently inaugurated on 1 July 2004.
- [d6s2]  He was reelected to a second term on 23 May 2009.
- [d6s3]  Just a year later, on 31 May 2010, he resigned from his office in a controversy over his comment on the role of the German Bundeswehr in light of a visit to the troops in Afghanistan.
- [d6s4]  During his tenure as German President, whose office is mostly concerned with ceremonial matters, Köhler was a highly popular politician, with approval rates above those of both chancellor Schröder and later chancellor Merkel.

**d7: Time of the Innocent**

- [d7s0] Time of the Innocent (German: Die Zeit der Schuldlosen ) is a 1964 German drama film directed by Thomas Fantl, based on a play by Siegfried Lenz.
- [d7s1]  It was distributed by Columbia-Bavaria Filmgesellschaft in Germany and represented by Export-Film Bischoff world wide.
- [d7s2]  It was entered into the 14th Berlin International Film Festival.
- [d7s3]  It opened in the presence of President Lübke and his wife, German Chancellor Erhard, Vice Chancellor Mende, Secretary of State Schröder, Minister Westrick, "Bundespressechef" von Haase in Berlin's famous Zoo-Palast, which is one of the highest attendances of German politician to a Berlinale premiere.

**d8: Ludwig Erhard**

- [d8s0] Ludwig Wilhelm Erhard (] ; 4 February 1897 – 5 May 1977) was a German politician affiliated with the CDU and the second Chancellor of the Federal Republic of Germany (West Germany) from 1963 until 1966.
- [d8s1]  He is often famed for leading German postwar economic reforms and economic recovery (""Wirtschaftswunder,"" German for "economic miracle") in his role as Minister of Economic Affairs under Chancellor Konrad Adenauer from 1949 to 1963.
- [d8s2]  During that period he promoted the concept of the social market economy ("soziale Marktwirtschaft"), on which Germany's economic policy in the 21st century continues to be based.
- [d8s3]  In his tenure as chancellor, however, Erhard failed to win confidence in his handling of a budget deficit and his direction of foreign policy, and his popularity waned.
- [d8s4]  He resigned his chancellorship on 1 December 1966.

**d9: Guido Westerwelle**

- [d9s0] Guido Westerwelle (] ; 27 December 1961 – 18 March 2016) was a German politician who served as Foreign Minister in the second cabinet of Chancellor Angela Merkel and as Vice Chancellor of Germany from 2009 to 2011, being the first openly gay person to hold any of these positions.
- [d9s1]  He was also the chairman of the Free Democratic Party of Germany (FDP) from May 2001 until he stepped down in 2011.
- [d9s2]  A lawyer by profession, he was a member of the Bundestag from 1996 to 2013.

**d10: Kurt Georg Kiesinger**

- [d10s0] Kurt Georg Kiesinger (] ; 6 April 1904 – 9 March 1988) was a German politician who served as Chancellor of Germany (West Germany) from 1 December 1966 to 21 October 1969.
- [d10s1]  Before he became Chancellor he served as Minister President of Baden-Württemberg from 1958 to 1966 and as President of the Federal Council from 1962 to 1963.
- [d10s2]  He was Chairman of the Christian Democratic Union from 1967 to 1971.

## 30. hotpotqa_5add24625542994734353874

原位置：`train` 第 210 题 · 全局第 210 题 · `sample_id: hotpotqa_5add24625542994734353874`

Question: What is the name of the film that Anne Archer starred in that was a sequel to The Hunt for Red October?

Note: 

Type: bridge · fallback: False · SFT snapshots: 7

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | film sequel to The Hunt for Red October | False | [] | Patriot Games | [["d3s1"]] | context |
| u2 | film starring Anne Archer that is {u1} | True | ["u1"] | Patriot Games | [["d3s1"], ["d10s2"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | film that is a sequel to The Hunt for Red October | False | [] | Patriot Games | [['d3s1']] |
| u2 | film starring Anne Archer that was a sequel to The Hunt for Red October, given {u1} | True | ['u1'] | Patriot Games | [['d3s1'], ['d10s2']] |

### Source documents (reference only)

**d1: Red October (fictional submarine)**

- [d1s0] Red October (Russian: Красный Oктябрь , [ˈkrasnɨj ɐkˈtʲabrʲ] "Krasniy Oktyabr") is a modified "Typhoon" class submarine in the Tom Clancy novel "The Hunt for Red October" and the film of the same name.
- [d1s1]  It was built with a revolutionary stealth propulsion system called a "caterpillar drive", which is described as a pump-jet system in the book.
- [d1s2]  In the film however, it is shown as being a magnetohydrodynamic drive.

**d2: Crazy Ivan**

- [d2s0] Crazy Ivan is a cold war term used in the US to describe two different concepts.
- [d2s1]  The most common usage was the name given to a maneuver used by Soviet submarines to clear their baffles to see if they were being followed.
- [d2s2]  The second use was a catch-all term for the possibility of a rogue Soviet leader committing to military action, typically in reference to a limited launch of ICBMs against the US.
- [d2s3]  The term Red October was sometimes used to describe the second concept, a reference to the 1984 Tom Clancy novel "The Hunt for Red October" in which a rogue Soviet submarine commander appears to threaten to launch a nuclear strike on the US.
- [d2s4]  The novel uses the first version of the term as a plot point.

**d3: Patriot Games (film)**

- [d3s0] Patriot Games is a 1992 American spy thriller film directed by Phillip Noyce and based on Tom Clancy's novel of the same name.
- [d3s1]  It is a sequel to the 1990 film "The Hunt for Red October", but with different actors in the leading roles, Harrison Ford starring as Jack Ryan and Anne Archer as his wife.
- [d3s2]  James Earl Jones is the lone holdover, reprising his role as Admiral James Greer.
- [d3s3]  The cast also includes Sean Bean, Patrick Bergin, Thora Birch, Samuel L. Jackson, James Fox, and Richard Harris.

**d4: Sam Neill**

- [d4s0] Nigel John Dermot Neill {'1': ", '2': ", '3': ", '4': "} (born 14 September 1947), known professionally as Sam Neill, is a New Zealand actor who first achieved leading roles in films such as "" and "Dead Calm" and on television in "Reilly, Ace of Spies".
- [d4s1]  He won a broad international audience in 1993 for his roles as Alisdair Stewart in "The Piano" and Dr. Alan Grant in "Jurassic Park", a role he reprised in 2001's "Jurassic Park III".
- [d4s2]  Neill also had notable roles in "Merlin", "The Hunt for Red October", "Peaky Blinders", and "The Tudors".
- [d4s3]  In 2016, he starred in "Hunt for the Wilderpeople" alongside Julian Dennison, to great acclaim.

**d5: The Art of War (film)**

- [d5s0] The Art of War is a 2000 Canadian-American action film directed by Christian Duguay and starring Wesley Snipes, Michael Biehn, Anne Archer and Donald Sutherland.
- [d5s1]  The film's title refers to the ancient Chinese text of the same name by war strategist Sun Tzu.
- [d5s2]  The film was followed by two direct-to-video sequels, "" and "", which the latter did not feature Snipes.

**d6: The Hunt for Red October (1990 video game)**

- [d6s0] The Hunt for Red October is video game based on the movie "The Hunt for Red October".
- [d6s1]  It was developed by Images Software and released by Grandslam Interactive Ltd. in 1990 and was available for the Amiga, Amstrad CPC, Atari ST, Commodore 64, MS-DOS, and ZX Spectrum.

**d7: The Hunt for Red October (console game)**

- [d7s0] The Hunt for Red October is a video game based on the movie "The Hunt for Red October".
- [d7s1]  It was first released in 1991 for the Nintendo Entertainment System.
- [d7s2]  Versions for the Game Boy and Super NES were subsequently released.

**d8: The Blue Knight (film)**

- [d8s0] The Blue Knight is a 1973 made-for-TV film based on Joseph Wambaugh's 1973 novel "The Blue Knight".
- [d8s1]  It gave rise to the 1975 TV series also named "The Blue Knight".
- [d8s2]  It ran originally on NBC TV in November 1973, was directed by Robert Butler, and starred an all star cast headed by William Holden as Police Officer Bumper Morgan.
- [d8s3]  The additional cast includes Lee Remick, Anne Archer, Sam Elliott, Joe Santos, and Vic Tayback.
- [d8s4]  The film was a four-hour series.

**d9: The Hunt for Red October (1987 video game)**

- [d9s0] The Hunt for Red October is a video game based on the book The Hunt for Red October.
- [d9s1]  It was released in 1987 and was available for the Atari ST, Amiga, Apple II, ZX Spectrum, MSX, Commodore 64 and IBM PC.
- [d9s2]  A port for the Apple IIGS was released in 1989.
- [d9s3]  The player must navigate the "Red October" towards U.S. waters while avoiding the Soviet Navy.
- [d9s4]  The game is a combination of submarine simulator and strategy game.

**d10: Anne Archer**

- [d10s0] Anne Archer (born August 24, 1947) is an American actress.
- [d10s1]  She was nominated for the Academy Award for Best Supporting Actress for the 1987 film "Fatal Attraction".
- [d10s2]  Her other film appearances include "Paradise Alley" (1978), "Patriot Games" (1992), "Short Cuts" (1993), "Clear and Present Danger" (1994) and "Lullaby" (2014).
- [d10s3]  On stage, she starred as Mrs. Robinson in the West End production of "The Graduate" in 2001, and in the title role of "The Trial of Jane Fonda" at the 2014 Edinburgh Festival Fringe.
