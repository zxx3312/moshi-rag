# batch_09：人工审查（30 题）

全局题号 241–270；train 3 题 / dev 27 题。原训练/验证归属保持不变。

[返回分配索引](../README.md) · [完整对比报告](../../comparison_human.md)

**原则：新旧单元都合理时保留拆题器拆法，人工监督向新单元对齐。** 本批已由用户审核，按最新 Note 完成调整。

审查人：________　完成日期：________

本批已依据人工 Note 调整；原始拆题保存在 JSON 的 `raw_decomposition`。下方 Adjusted units 为当前标注，旧 gold 仅供参照。标注已更新；逐时刻 SFT 快照尚未重建。

## 1. hotpotqa_5ae71f455542996d980e7ca9

原位置：`train` 第 241 题 · 全局第 241 题 · `sample_id: hotpotqa_5ae71f455542996d980e7ca9`

Question: Soul Axiom included a port for the Microsoft game console announced in what month?

Note: 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

Type: bridge · fallback: False · SFT snapshots: 5

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | Microsoft game console for which Soul Axiom included a port | False | [] | Xbox One | [["d6s4", "d7s0"], ["d6s4", "d7s4"]] | context |
| u2 | month in which {u1} was announced | True | ["u1"] | May 2013 | [["d7s1"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | Microsoft game console for which Soul Axiom included a port | False | [] | Xbox One | [['d6s4', 'd7s0'], ['d6s4', 'd7s4']] |
| u2 | month in which {u1} was announced | True | ['u1'] | May 2013 | [['d7s1']] |

### Source documents (reference only)

**d1: Kinect Adventures!**

- [d1s0] Kinect Adventures!
- [d1s1]  is a sports video game released by Microsoft Game Studios for the Xbox 360.
- [d1s2]  Released in 2010, it is a collection of five adventure and sports minigames and was developed by Good Science Studio, a subsidiary of Microsoft Game Studios.
- [d1s3]  The game utilizes the Kinect motion camera and was offered as a pack-in game with the console.
- [d1s4]  It was unveiled at the 2010 Electronic Entertainment Expo and went on to become the best-selling game on the Xbox 360, selling 24 million units worldwide.

**d2: Halo: Reach**

- [d2s0] Halo: Reach is a first-person shooter video game developed by Bungie and published by Microsoft Game Studios for the Xbox 360 home video game console.
- [d2s1]  The sixth installment in the "Halo" series, "Reach" was released worldwide in September 2010.
- [d2s2]  The game takes place in the year 2552, where humanity is locked in a war with the alien Covenant.
- [d2s3]  Players control Noble Six, a member of an elite supersoldier squad, when the human world known as Reach falls under Covenant attack.

**d3: Microsoft Studios**

- [d3s0] Microsoft Studios is the video game production wing for Microsoft, responsible for the development and publishing of games for the Xbox, Xbox 360, Xbox One, Games for Windows, Steam, Windows Store, Windows Phone and Nintendo DS platforms.
- [d3s1]  They were established in 2002 as Microsoft Game Studios to coincide with the already released Xbox, before being re-branded in 2011.
- [d3s2]  The subsidiary had also been known as Microsoft Game Division and simply Microsoft Games before 2002.
- [d3s3]  Microsoft Studios develops and publishes games in conjunction with first and third party development studios under their publishing label.

**d4: Halo 2**

- [d4s0] Halo 2 is a 2004 first-person shooter video game developed by Bungie Studios.
- [d4s1]  Released for the Xbox video game console on November 9, 2004, the game is the second installment in the "Halo" franchise and the sequel to 2001's critically acclaimed "".
- [d4s2]  A Microsoft Windows version of the game was released on May 31, 2007, developed by an internal team at Microsoft Game Studios known as Hired Gun.
- [d4s3]  The game features a new game engine, as well as using the Havok physics engine; added weapons and vehicles, and new multiplayer maps.
- [d4s4]  The player alternately assumes the roles of the human Master Chief and the alien Arbiter in a 26th-century conflict between the human United Nations Space Command and genocidal Covenant.

**d5: Wales Interactive**

- [d5s0] Wales Interactive Limited is a British independent video game developer and publisher established in 2011 and based in Pencoed, Wales.
- [d5s1]  The studio, best known for "Soul Axiom", "The Bunker" and "Master Reboot", have published over 20 video game titles across 10 platforms and have won a BAFTA Cymru Games Award and a MCV Indie Games Label 2017 nomination.
- [d5s2]  The studio supports PlayStation 4, Xbox One, Wii U and Microsoft Windows as well as all the latest virtual reality devices including HTC Vive, Oculus Rift and PlayStation VR.
- [d5s3]  Wales Interactive develop and publish their own original IP as well as third-party titles.

**d6: Soul Axiom**

- [d6s0] Soul Axiom is a first-person adventure-puzzle video game developed and published by Wales Interactive.
- [d6s1]  The game is set inside a "Digital Soul Provider" called Elysia, and combines exploration with puzzle solving elements to unlock the mystery of your character's digital afterlife.
- [d6s2]  It follows a similar visual style from its predecessor, Master Reboot, and while it's not a direct sequel, it is set in the same world but with new characters, a new story and new set of game mechanics.
- [d6s3]  The game was released on February 29, 2016.
- [d6s4]  PlayStation 4 and Xbox One ports were released in June 2016.
- [d6s5]  The Wii U launch is planned for September 29, 2016.

**d7: Xbox One**

- [d7s0] Xbox One is a line of eighth generation home video game consoles developed by Microsoft.
- [d7s1]  Announced in May 2013, it is the successor to Xbox 360 and the third console in the Xbox family.
- [d7s2]  It was first released in North America, parts of Europe, Australia, and Brazil in November 2013, and in Japan, China, and other European countries in September 2014.
- [d7s3]  It is the first Xbox game console to be released in China, specifically in the Shanghai Free-Trade Zone.
- [d7s4]  Microsoft marketed the device as an "all-in-one entertainment system".
- [d7s5]  The Xbox One line mainly competes against consoles such as Sony's PlayStation 4 and Nintendo's Wii U and Switch.

**d8: Halo Wars**

- [d8s0] Halo Wars is a real-time strategy (RTS) video game developed by Ensemble Studios and published by Microsoft Game Studios for the Xbox 360 video game console.
- [d8s1]  It was released in Japan and Australia on February 26, 2009; in Europe on February 27; and in North America on March 3.
- [d8s2]  The game is set in the science fiction universe of the "Halo" series in the year 2531, 21 years before the events of "".
- [d8s3]  The player leads human soldiers aboard the warship "Spirit of Fire" in an effort to stop an ancient fleet of ships from falling into the hands of the genocidal alien Covenant.

**d9: Perfect Dark Zero**

- [d9s0] Perfect Dark Zero is a first-person shooter video game developed by Rare and published by Microsoft Game Studios.
- [d9s1]  It was exclusively released as a launch title for the Xbox 360 video game console on November 22, 2005 in North America and December 2, 2005 in Europe.
- [d9s2]  The game is part of the "Perfect Dark" series and a prequel to the original "Perfect Dark".
- [d9s3]  The story of the game follows bounty hunter Joanna Dark as she joins the Carrington Institute agency to prevent rival corporation dataDyne from getting possession of an ancient artefact which endows individuals with superhuman powers.

**d10: Ultravision Video Arcade System**

- [d10s0] The Ultravision Video Arcade System (VAS) was an unreleased gaming console announced in 1983.
- [d10s1]  The slogan provided by the company, ""It's a game!
- [d10s2]  A computer!
- [d10s3]  A color TV!""
- [d10s4] , was intended to demonstrate how the game console was going to be a computer that was accessible and non-threatening to consumers.

## 2. hotpotqa_5ae74ae95542997b22f6a688

原位置：`train` 第 242 题 · 全局第 242 题 · `sample_id: hotpotqa_5ae74ae95542997b22f6a688`

Question: Rani Velu Nachiyar was a famous queen before which queen that was a leading figure of the Indian Rebellion of 1857?

Note: 保留新反向顺序；末单元明确输出女王而非真假陈述，按新顺序交换证据。

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新反向顺序；末单元明确输出女王而非真假陈述，按新顺序交换证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | queen that was a leading figure of the Indian Rebellion of 1857 | False | [] | Rani of Jhansi | [["d8s1"]] | context |
| u2 | queen among {u1} whom Rani Velu Nachiyar preceded in fighting the British | True | ["u1"] | Rani of Jhansi | [["d3s1"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | famous queen whom Rani Velu Nachiyar came before in fighting the British | False | [] | Rani of Jhansi | [['d3s1']] |
| u2 | queen who was a leading figure of the Indian Rebellion of 1857, given {u1} | True | ['u1'] | Rani of Jhansi | [['d8s1']] |

### Source documents (reference only)

**d1: Vellacci**

- [d1s0] Vellacci or Vellachi Nachiyar was the second queen of Sivaganga estate in 1790-1793.
- [d1s1]  She is the daughter of Muthu Vaduganatha Periyavudaya Thevar and Velu Nachiyar.
- [d1s2]  She was made the heir to the throne of Sivagangai by her mother Velu Nachiyar after the recapture of Sivagangai from the British.

**d2: Indian Rebellion of 1857**

- [d2s0] The Indian Rebellion of 1857 was a major, but ultimately unsuccessful, uprising in India in 1857–58 against the rule of the British East India Company, which functioned as a sovereign power on behalf of the British Crown.
- [d2s1]  The rebellion began on 10 May 1857 in the form of a mutiny of sepoys of the Company's army in the garrison town of Meerut, 40 miles northeast of Delhi (now Old Delhi).
- [d2s2]  It then erupted into other mutinies and civilian rebellions chiefly in the upper Gangetic plain and central India, though incidents of revolt also occurred farther north and east.
- [d2s3]  The rebellion posed a considerable threat to British power in that region, and was contained only with the rebels' defeat in Gwalior on 20 June 1858.
- [d2s4]  On 1 November 1858, the British granted amnesty to all rebels not involved in murder, though they did not declare the hostilities formally to have ended until 8 July 1859.
- [d2s5]  The rebellion is known by many names, including the Sepoy Mutiny, the Indian Mutiny, the Great Rebellion, the Revolt of 1857, the Indian Insurrection, and India's First War of Independence.

**d3: Velu Nachiyar**

- [d3s0] Rani Velu Nachiyar (1730-1796), was a queen of Sivaganga estate in 1760-1790.
- [d3s1]  She was the first queen to fight against the British colonial power in India, even long before the famous Rani of Jhansi.
- [d3s2]  She is celebrated by Tamilians as "Veeramangai" (brave women).

**d4: Jhalkaribai**

- [d4s0] Jhalkaribai (22 November 1830 – 1858) (Hindi: झलकारीबाई ] ) was a Dalit woman soldier who played an important role in the Indian Rebellion of 1857.
- [d4s1]  She served in the women's army of Queen Laxmibai of Jhansi.
- [d4s2]  Born into a Kori family, she eventually rose to a position of a prominent advisor to the queen, Rani of Jhansi herself.
- [d4s3]  At the height of the battle of fort of Jhansi, she disguised herself as the Queen and fought on her behalf, on the front, allowing the Queen to escape safely out of the fort.

**d5: Laxmibai Nagar**

- [d5s0] Laxmi Bai Nagar is a residential government colony in New Delhi, India.
- [d5s1]  Laxmi Bai, meaning "city of Lakshmibai", is named for the Rani (queen) of the Maratha-ruled Jhansi State in India, which is now a province of modern Uttar Pradesh state.
- [d5s2]  She fought for independence from the British Raj during the Indian Rebellion of 1857 and died in combat.

**d6: Sivaganga Palace**

- [d6s0] Sivaganga Palace is a palace in Sivaganga district, Tamil Nadu, southern India, about 40 km from Madurai.
- [d6s1]  It is an old royal palace, with many historical connections.
- [d6s2]  The palace was used as residence by queens Velu Nachiyar (1780–90), Vellacci Nachiyar (1790–93) and Rani Kaathama Nachiar (1864–77).
- [d6s3]  No remains of the original Sivaganga Palace exist, but a new palace, known as "Gowri Vilasam", was built by Padamathur Gowry Vallabha Thevar (1801-1829) in the year 19th century.
- [d6s4]  A heritage site of Chettinad, it was the property of Rani Velu Nachiar.

**d7: Royal Indian Artillery**

- [d7s0] The Royal Regiment of Indian Artillery, generally known as the Royal Indian Artillery (RIA), was an administrative corps of the British Indian Army.
- [d7s1]  The East India Company raised the first regular company of Artillery in 1748, with a small percentage of Indian Gunners called Gun Lashkars, Tindals and Serangs.A few Indian Mountain Batteries, officered by the British, were raised in the 19th century and formed part of the Royal Artillery.
- [d7s2]  Royal Indian Artillery (RIA) of British India Army, was raised on September 28, 1827, as a part of the Bombay Army, a presidency army of the Bombay Presidency.
- [d7s3]  It was later renamed as 5 Bombay Mountain Battery, and involved in First Anglo-Afghan War (1839–1842).
- [d7s4]  The Indian Rebellion of 1857 was sparked off in Meerut on 10 May 1857, primarily by native artillery of Bengal Army, following which all Indian artillery units were banned except mountain artillery batteries, though for his service during the Indian Rebellion, Major Richard Keatinge of Bombay Artillery, was awarded the Victoria Cross in 1858.

**d8: Rani of Jhansi**

- [d8s0] Lakshmibai, the Rani of Jhansi (   ; 19 November 1828 – 18 June 1858), was the queen of the princely state of Jhansi in North India currently present in Jhansi district in Uttar Pradesh, India.
- [d8s1]  She was one of the leading figures of the Indian Rebellion of 1857 and became a symbol of resistance to the British Raj for Indian nationalists.

**d9: Rani Mahal**

- [d9s0] The Rani Mahal is a royal palace in the city of Jhansi, Uttar Pradesh, India.
- [d9s1]  The palace was built by Raghu Nath-II of the Newalkar family (1769-96).
- [d9s2]  This palace later formed one of the residences for Rani Lakshmibai.
- [d9s3]  Architecturally, it is a flat-roofed, two-storeyed building having a quadrangular courtyard with a small well and one fountain on opposing sides.
- [d9s4]  The palace consists of six halls and parallel corridors with multi-foiled arches and a number of small rooms.
- [d9s5]  The Darbar Hall, approached by a flight of steps, is beautifully decorated with paintings in bright colours exhibiting various floral, faunal and geometrical motifs.
- [d9s6]  The arches are embellished with peacock and rosette patterns.
- [d9s7]  The major part of it was damaged by British bombardment during the Indian Rebellion of 1857.
- [d9s8]  The ground floor of the palace houses stone sculptures collected from Madanpur, Barua Sagar, Dudhai and Chandpur dating from the Gupta to Medieval periods (9th to 12th centuries).

**d10: Natore Rajbari**

- [d10s0] Natore Rajbari (also known as Pagla Raja's Palace, Natore Palace) was a prominent royal palace in Natore, Bangladesh.
- [d10s1]  It was the residence and seat of the Rajshahi Raj family of zamindars.
- [d10s2]  Famous queen Rani Bhabani lived here and after the death of her husband, expanded both the estate and the palace.

## 3. hotpotqa_5ae752255542995703ce8be5

原位置：`train` 第 243 题 · 全局第 243 题 · `sample_id: hotpotqa_5ae752255542995703ce8be5`

Question: Which river that streams westward from Pittsburgh, Pennsylvania, to Cairo, Illinois is the northern boundary of Downtown Louisville?

Note: 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | river that streams westward from Pittsburgh to Cairo, Illinois | False | [] | Ohio River | [["d6s0"]] | context |
| u2 | river forming the northern boundary of Downtown Louisville, given {u1} | True | ["u1"] | Ohio River | [["d8s1"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | river that streams westward from Pittsburgh to Cairo, Illinois | False | [] | Ohio River | [['d6s0']] |
| u2 | river forming the northern boundary of Downtown Louisville, given {u1} | True | ['u1'] | Ohio River | [['d8s1']] |

### Source documents (reference only)

**d1: Lima river**

- [d1s0] The Lima River ("Lima" in Portuguese and Limia in Spanish) is a river, which streams westward from Galicia in Spain) to Portugal, with a length of 108 km .

**d2: East Nashville, Tennessee**

- [d2s0] East Nashville is an area east of downtown Nashville, Tennessee across the Cumberland River.
- [d2s1]  The area is mostly residential and mixed-use areas with businesses lining the main boulevards.
- [d2s2]  The main thoroughfare is Gallatin Avenue and Ellington Parkway with smaller arteries interconnecting the neighborhoods.
- [d2s3]  Some of these smaller arteries include Main Street, Shelby Avenue, Porter Road, Riverside Drive, Eastland Avenue, McFerrrin Avenue, and Woodland Street in no significant order.
- [d2s4]  Ellington Parkway, which parallels Gallatin Avenue and Main Street, bypasses I-24 and I-65 and connects Briley Parkway and downtown Nashville and many other secondary streets along the way.
- [d2s5]  The Cumberland River confines most of the area with a semicircle design on the south, southwest and east.
- [d2s6]  Since East Nashville has no real boundaries on the west and north, many times it is different.
- [d2s7]  Some would say that Ellington Parkway creates a boundary on the west and northwest, while Cahal Avenue and Porter Road in the north, in the confines of zipcode 37206.
- [d2s8]  Many would now state that I-65 and I-24 create the western border and Briley Parkway as the northern boundary, which is called Greater East Nashville.

**d3: West Aurora Public School District 129**

- [d3s0] West Aurora Public School District 129 is a unit school district in southeastern Kane County, Illinois.
- [d3s1]  The present "West Side" school district covers the city of Aurora, Illinois with an eastern boundary of the Fox River, a southern boundary of the Kane County and Kendall County line, a western boundary of Aurora's city limits, and a northern boundary of the village limits of North Aurora, Illinois.
- [d3s2]  Students from Aurora, North Aurora, Montgomery, Illinois and Sugar Grove, Illinois attend West Aurora schools.

**d4: Ridgefield Township, New Jersey**

- [d4s0] Ridgefield Township was a township that existed in Bergen County, New Jersey.
- [d4s1]  The township was created in 1871, when Hackensack Township was trisected to form Palisades Township in the northernmost third, Englewood Township in the central strip and Ridgefield Township encompassing the southernmost portion, stretching from the Hudson River on the east to the Hackensack River, with Hudson County to the south.
- [d4s2]  Much of the area had been during the colonial area known as the English Neighborhood.
- [d4s3]  As described in the 1882 book, "History of Bergen and Passaic counties, New Jersey," "Ridgefield is the first township in Bergen County which the traveler enters in passing up the Palisades.
- [d4s4]  His first impressions are much like those of old Hendrick Hudson in speaking of a wider extent of country: "A very good land to fall in with, and a pleasant land to see."
- [d4s5]  The valley of the Hackensack invited early settlers in the seventeenth century, and the valley of the Overpeck Creek, a navigable arm of the Hackensack, also attracted settlers quite as early in this direction.
- [d4s6]  Sloops and schooners can pass up this creek nearly to the northern boundary of the township.
- [d4s7]  Ridgefield is bounded on the north by Englewood, on the east by the Hudson, on the south by Hudson County, and on the west by the Hackensack River.
- [d4s8]  The southern boundary is less than two miles in extent, and the northern less than four, and the length of the township from north to south does not exceed four miles.
- [d4s9]  Bellman's Creek, forming part of the southern boundary, the Hackensack, the Overpeck, the Hudson, with more than a dozen other smaller streams and rivulets, bountifully supply the whole township with water.
- [d4s10]  From the western border of the Palisades the land descends to the Overpeck, forming a most beautiful valley, with the land again rising to a high ridge midway between the Overpeck and the Hackensack.
- [d4s11]  From this long ridge, extending far to the north beyond this township, it took its name of Ridgefield.
- [d4s12] <br><br>The New York, Susquehanna and Western, formerly the Midland Railroad, the Jersey City and Albany Railroad, and the Northern Railway of New Jersey—all running northward through the township— afford ample railroad accommodations.
- [d4s13]  The Susquehanna enters the township at Bellman's Creek, and the Northern at about one hundred feet south of the creek, and at a point north and east of the Susquehanna.
- [d4s14]  The Albany road in this locality is not yet constructed, diverging at present from the track of the Susquehanna between Little Ferry and Bogota stations.
- [d4s15]  It has, however, an independent line projected and now under construction to New York City.
- [d4s16] <br><br>Early Settlements.
- [d4s17]  Ridgefield embraces the earliest settlements in the ancient township of Hackensack, antedating even the organization of that township in 1693, and of the county of Bergen in 1675.
- [d4s18]  There seems to have been no town or village compactly built, like the village of Bergen, but there were settlements both of Dutch and English in and about what was subsequently known as English Neighborhood prior to 1675.
- [d4s19]  The Westervelts, the Zimcrmans, the Bantas, and the Blauvelts, all coming from Holland, settled in the middle of the seventeenth century in that locality.
- [d4s20]  The ancestors of Jacob P. Westervelt, now of Hackensack Village, with himself, were born in English Neighborhood.
- [d4s21]  His father was born there in 1776, and was the son of Christopher Westervelt, who was born there certainly as early as 1690, and he was the son of the original ancestor of this family, who came from Holland and settled on Overpeck Creek, within the present limits of Ridgefield township, probably about 1670."

**d5: Geography of Illinois**

- [d5s0] Illinois is in the midwestern United States.
- [d5s1]  Surrounding states are Wisconsin to the north, Iowa and Missouri to the west, Kentucky to the south, and Indiana to the east.
- [d5s2]  Illinois also borders Michigan, but only via a northeastern water boundary in Lake Michigan.
- [d5s3]  Nearly the entire western boundary is the Mississippi River, except for a few areas where the river has changed course.
- [d5s4]  Illinois' southeastern and southern boundary is along the Wabash River and the Ohio River.
- [d5s5]  Whereas, its northern boundary and much of its eastern boundary are straight survey (longitudinal and latitudinal) lines.
- [d5s6]  Illinois has a maximum north-south distance of 390 miles (630 km) and 210 miles (340 km) east-west.
- [d5s7]  Its total area is 57918 sqmi .

**d6: Ohio River**

- [d6s0] The Ohio River, which streams westward from Pittsburgh, Pennsylvania, to Cairo, Illinois, is the largest tributary, by volume, of the Mississippi River in the United States.
- [d6s1]  At the confluence, the Ohio is considerably bigger than the Mississippi (Ohio at Cairo: 281,500 cu ft/s (7,960 m/s); Mississippi at Thebes: 208,200 cu ft/s (5,897 m/s)) and, thus, is hydrologically the main stream of the whole river system.

**d7: Little Walker Caldera**

- [d7s0] Little Walker Caldera is a depression in the eastern Sierra Nevada that is adjacent to the Sweetwater Mountains.
- [d7s1]  The caldera is very large, measuring about 18 km in diameter.
- [d7s2]  The Little Walker Caldera is named for the Little Walker River; it is the river that is little, not the caldera.
- [d7s3]  U.S. Route 395 in California crosses the Northern boundary of the caldera, just west of the Devil's Gate Pass.
- [d7s4]  California State Route 108 follows more of the northern boundary of the caldera.

**d8: Downtown Louisville**

- [d8s0] Downtown Louisville is the largest central business district in the Commonwealth of Kentucky and the urban hub of the Louisville, Kentucky Metropolitan Area.
- [d8s1]  Its boundaries are the Ohio River to the north, Hancock Street to the east, York and Jacob Streets to the south, and 9th Street to the west.
- [d8s2]  As of 2000, the population of Downtown Louisville was 2,575.

**d9: Main Line (Pittsburgh to St. Louis)**

- [d9s0] The Pittsburgh to St. Louis Main Line was a rail line owned and operated by the Pennsylvania Railroad in the U.S. states of Pennsylvania, Ohio, Indiana, and Illinois.
- [d9s1]  The line ran from Pittsburgh, Pennsylvania west via Steubenville, Ohio, Columbus, Ohio, Dayton, Ohio, Indianapolis, Indiana, Terre Haute, Indiana, and Vandalia, Illinois to East St. Louis, Illinois.
- [d9s2]  In addition to its east end in downtown Pittsburgh, where it met the Main Line and Pittsburgh to Chicago Main Line, junctions included the Columbus to Chicago Main Line at Columbus, the C&X Branch (to Cincinnati) at Xenia, the Columbus to Indianapolis Main Line via Bradford (a freight bypass of Dayton) at New Paris, the Richmond Branch and Fort Wayne Branch at Richmond, the Louisville Branch and I&F Branch at Indianapolis, and the Peoria Branch at Farrington, Illinois.

**d10: U.S. Route 60 in Kentucky**

- [d10s0] U.S. Route 60 (US 60) in the state of Kentucky parallels the Ohio River (the northern boundary of the state) from Cairo, Illinois, to Louisville, and then takes a direct eastward route (near Interstate 64, I-64) to rejoin the Ohio River at Kenova, West Virginia.

## 4. 2wikimultihopqa_008905100baf11ebab90acde48001122

原位置：`dev` 第 1 题 · 全局第 244 题 · `sample_id: 2wikimultihopqa_008905100baf11ebab90acde48001122`

Question: Who is Apama Iii's father-in-law?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | spouse of Apama Iii | False | [] | Prusias I of Bithynia | [["d7s8"]] | context |
| u2 | father of {u1}, Apama Iii's father-in-law | True | ["u1"] | Ziaelas of Bithynia | [["d4s5"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | spouse of Apama III | False | [] | Prusias I of Bithynia | [['d7s8']] |
| u2 | father of {u1}, Apama III's father-in-law | True | ['u1'] | Ziaelas of Bithynia | [['d4s5']] |

### Source documents (reference only)

**d1: Harry Smith (athlete)**

- [d1s0] Harry James Smith( July 30, 1888 – November 20, 1962) was an American long- distance runner.
- [d1s1] He was most notable for competing in the 1912 Olympics in Stockholm.
- [d1s2] He was also the father of Hart wrestling family matriarch Helen Hart and the father- in- law of Stu Hart.

**d2: John Vernou Bouvier III**

- [d2s0] John Vernou" Black Jack" Bouvier III( May 19, 1891 – August 3, 1957) was an American Wall Street stockbroker and socialite.
- [d2s1] He was the father of First Lady Jacqueline Kennedy Onassis and of socialite Lee Radziwill, and was the father- in- law of John F. Kennedy.

**d3: Ogawa Mataji**

- [d3s0] Viscount was a general in the early Imperial Japanese Army.
- [d3s1] He was also the father- in- law of Field Marshal Gen Sugiyama.

**d4: Prusias I of Bithynia**

- [d4s0] Prusias I Cholus
- [d4s1] (Greek:
- [d4s2] Προυσίας
- [d4s3] ὁ Χωλός
- [d4s4] "the Lame")
- [d4s5] (lived c. 243 – 182 BC, reigned c. 228 – 182 BC) was a king of Bithynia, the son of Ziaelas of Bithynia.

**d5: Peter Burroughs**

- [d5s0] Peter Burroughs( born 27 January 1947) is a British television and film actor, the director of Willow Management.
- [d5s1] He is the father- in- law of actor and TV presenter Warwick Davis.

**d6: James Armour (Master mason)**

- [d6s0] James Armour (15 January 1730 – 20 September 1798) was a master mason and father of Jean Armour, and therefore the father-in-law of the poet Robert Burns.

**d7: Apama III**

- [d7s0] Apama III, sometimes known as Apame III( born c. 250 BC, flourished 3rd and 2nd century BC) was a Greek princess from the Antigonid dynasty.
- [d7s1] Apama was of Greek Macedonian and Persian descent.
- [d7s2] She was the child born to the King Demetrius II Aetolicus and Queen Stratonice of Macedon.
- [d7s3] Her paternal grandparents were the Antigonid Monarchs Antigonus II Gonatas and Phila, while her maternal grandparents were the Seleucid Monarchs Antiochus I Soter and Stratonice of Syria.
- [d7s4] From her father ’s second marriage, she had a younger paternal half- brother called Philip V of Macedon who would eventually succeed as king.
- [d7s5] Apama was the namesake of her maternal aunt Apama II, who was the wife of King Magas of Cyrene and mother of the Ptolemaic Queen Berenice II.
- [d7s6] Apama was born and raised in Macedonia.
- [d7s7] Her father formed an alliance with the Greek King of Anatolia Prusias I of Bithynia.
- [d7s8] Apama later married Prusias I and through her marriage, became Queen of Bithynia.
- [d7s9] Apama bore Prusias I, a son and his successor called Prusias II of Bithynia, sometimes known as" Prusias II CynegusCynegus" means" the Hunter".
- [d7s10] Her husband was also an ally to her half brother, Philip V. After Philip V, took the port city of Prusa, her husband rebuilt the city around 202 BC and renamed the city" Apamea Myrlea", which still bears her name.
- [d7s11] Her daughter- in- law was her niece and namesake Apame IV.
- [d7s12] Apame IV was one of the daughters of her half brother and later married her son.

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

**d9: John Adams (merchant)**

- [d9s0] John Adams( 1672 or 1673 – 1745) was an American- born Canadian merchant and member of the Nova Scotia Council.
- [d9s1] He was the father- in- law of Henry Newton( politician).

**d10: Ludwig von Westphalen**

- [d10s0] Johann Ludwig von Westphalen( 11 July 1770 – 3 March 1842) was a liberal Prussian civil servant and the father- in- law of Karl Marx.

## 5. 2wikimultihopqa_363145e20baf11ebab90acde48001122

原位置：`dev` 第 2 题 · 全局第 245 题 · `sample_id: 2wikimultihopqa_363145e20baf11ebab90acde48001122`

Question: Who is the paternal grandfather of Helvis Of Cyprus?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | father of Helvis Of Cyprus | False | [] | Amalric II of Jerusalem | [["d2s0"]] | context |
| u2 | father of {u1}, Helvis Of Cyprus's paternal grandfather | True | ["u1"] | Hugh VIII of Lusignan | [["d9s0", "d9s2"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Helvis of Cyprus | False | [] | Amalric II of Jerusalem | [['d2s0']] |
| u2 | father of {u1}, Helvis of Cyprus's paternal grandfather | True | ['u1'] | Hugh VIII of Lusignan | [['d9s0', 'd9s2']] |

### Source documents (reference only)

**d1: Fred Le Deux**

- [d1s0] Frederick" Fred" Le Deux( born 4 December 1934) was an Australian rules footballer who played with Geelong in the Victorian Football League( VFL).
- [d1s1] He is the grandfather of Tom Hawkins.

**d2: Helvis of Cyprus**

- [d2s0] Helvis of Lusignan (c. 1190 – c. 1218) was the daughter of Amalric II of Jerusalem, King of Cyprus, and his wife, Eschive d'Ibelin.
- [d2s1] She was married twice.
- [d2s2] Firstly, she was given in marriage to Eudes de Dampierre, a French knight, in about 1205.
- [d2s3] With Eudes she had children, including eldest son
- [d2s4] The details of her second marriage are revealed in a letter from Pope Innocent III to the archbishop of Antioch, dated September 1211.
- [d2s5] Helvis had been taken from her husband (or fled him) by the young Raymond-Roupen of Antioch, designated heir to the Armenian throne, and although ecclesiastical authorities commanded the return to her husband Eudes de Dampierre, Helvis refused.
- [d2s6] The young couple seem to have been encouraged by Helvis' brother-in-law, Walter of Montbéliard, which infuriated Helvis' brother King Hugh.
- [d2s7] She and Raymond-Roupen had issue:

**d3: Phoebus of Lusignan**

- [d3s0] Phoebus of Lusignan( died after July, 1485 in Rome)( also called Febo or Febos in Portuguese) was a titular Marshal of Armenia and also titular Lord of Sidon, the illegitimate son of Peter of Lusignan, titular Count of Tripoli.

**d4: Kaya Alp**

- [d4s0] Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

**d5: Helvis of Brunswick-Grubenhagen**

- [d5s0] Helvis of Brunswick- Grubenhagen( 1353 – 15 January 1421), was the Queen consort of Cyprus and Queen consort of Armenia as the wife of King James I of Cyprus.
- [d5s1] He was also titular King of Jerusalem.
- [d5s2] She was styled Queen of Cyprus from 1382 to 1398; although at the time of his ascension to the Cypriot throne, he and Helvis were imprisoned in Genoa after they had been captured by the Genoese on the island of Rhodes.
- [d5s3] Almost all of Helvis' 12 children were born to her while she was held prisoner.
- [d5s4] In 1385, after negotiations and many ruinous concessions to the Genoese, they were released and James was crowned king.
- [d5s5] In 1393, she became Queen of Armenia.

**d6: John of Lusignan**

- [d6s0] John of Lusignan( or Jean de Lusignan)( c. 1329 or 1329/1330–1375), regent of the Kingdom of Cyprus and titular Prince of Antioch.
- [d6s1] He was son of King Hugh IV of Cyprus and his second wife, Alix of Ibelin.
- [d6s2] He was a member of the House of Lusignan.

**d7: Isabella of Lusignan**

- [d7s0] Isabella of Lusignan( c.1224 – 14 January 1300) was a daughter of Hugh X of Lusignan and his wife Isabella of Angoulême, Dowager Queen of England.
- [d7s1] Isabella was half- sister to King Henry III of England.
- [d7s2] She was Dame de Beauvoir- sur Mer et de Mercillac.

**d8: Henry Krause**

- [d8s0] Henry J." Red" Krause, Jr.( August 28, 1913 – February 20, 1987) was an American football offensive lineman in the National Football League for the Brooklyn Dodgers and the Washington Redskins.
- [d8s1] He played college football at St. Louis University.
- [d8s2] He is the grandfather of Jennifer Krause
- [d8s3] He is the great grandfather of Payton Hoeing

**d9: Aimery of Cyprus**

- [d9s0] Aimery of Lusignan ("Amorí"; before 11551 April 1205), erroneously referred to as Amalric or Amaury in earlier scholarship, was the first King of Cyprus, reigning from 1196 to his death.
- [d9s1] He also reigned as King of Jerusalem from his marriage to Isabella I in 1197 to his death.
- [d9s2] He was the younger son of Hugh VIII of Lusignan, a nobleman in Poitou.
- [d9s3] After participating in a rebellion against Henry II of England in 1168, he went to the Holy Land and settled in the Kingdom of Jerusalem.
- [d9s4] His marriage to Eschiva of Ibelin (whose father, Baldwin of Ibelin was an influential nobleman) strengthened his position in the kingdom.
- [d9s5] His younger brother, Guy, married Sibylla, the sister of and heir to Baldwin IV of Jerusalem.
- [d9s6] Baldwin made Aimery Constable of Jerusalem around 1180.
- [d9s7] He was one of the commanders of the Christian army in the Battle of Hattin, which ended with decisive defeat at the hands of the army of Saladin, the Ayyubid sultan of Egypt and Syria, on 4 July 1187.
- [d9s8] Aimery supported his brother, Guy, even after Guy had lost his claim to the Kingdom of Jerusalem according to most barons of the realm, because of the death of Sibylla and their two daughters.
- [d9s9] The new king of Jerusalem, Henry of Champagne, arrested him for a short period.
- [d9s10] After his release, he retired to Jaffa which was the fief of his elder brother, Geoffrey of Lusignan, who had left the Holy Land.
- [d9s11] After Guy died in May 1194, his vassals in Cyprus elected Aimery as their lord.
- [d9s12] He accepted the suzerainty of the Holy Roman Emperor, Henry VI.
- [d9s13] With the emperor's authorization, Aimery was crowned King of Cyprus in September 1197.
- [d9s14] He soon married Henry of Champagne's widow, Isabella I of Jerusalem.
- [d9s15] He and his wife were crowned king and queen of Jerusalem in January 1198.
- [d9s16] He signed a truce with Al-Adil I, the Ayyubid sultan of Egypt, which secured the Christian possession of the coastline from Acre to Antioch.
- [d9s17] His rule was a period of peace and stability in both of his realms.

**d10: Maria of Antioch-Armenia**

- [d10s0] Maria of Antioch- Armenia( 1215–1257) was lady of Toron from 1229 to her death.
- [d10s1] She was the elder daughter of Raymond- Roupen, prince of Antioch, and of Helvis of Lusignan.
- [d10s2] She derived her title of Lady of Toron and claim to the throne of Armenia from her father.
- [d10s3] Maria's paternal grandmother Alice became lady of Toron when emperor Frederick II, at the end of the Sixth Crusade, negotiated the return of lands conquered by Saladin; Maria succeeded her as she was the closest surviving relative.
- [d10s4] In 1240 she married Philip of Montfort, Lord of Tyre, previously lord of Castres, and they had the following children:
- [d10s5] She was the great- granddaughter of Roupen III, prince of Armenia( Roupen III's daughter was Alice), who had been succeeded by his brother Leo I. Maria thus unsuccessfully claimed rights to the throne of Armenia, something her father and grandmother had previously attempted and failed.

## 6. 2wikimultihopqa_3a2fe93e0bda11eba7f7acde48001122

原位置：`dev` 第 3 题 · 全局第 246 题 · `sample_id: 2wikimultihopqa_3a2fe93e0bda11eba7f7acde48001122`

Question: What nationality is Keith Batey's wife?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | wife of Keith Batey | False | [] | Mavis Batey | [["d2s0"]] | context |
| u2 | nationality of {u1} | True | ["u1"] | British | [["d3s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | wife of Keith Batey | False | [] | Mavis Batey | [['d2s0']] |
| u2 | nationality of {u1} | True | ['u1'] | British | [['d3s0']] |

### Source documents (reference only)

**d1: Iraqi nationality law**

- [d1s0] Iraqi nationality is transmitted by one's parents.

**d2: Keith Batey**

- [d2s0] Keith Batey( 4 July 1919 – 28 August 2010) was a codebreaker who, with his wife, Mavis Batey( 5 May 1921 – 12 November 2013), worked on the German Enigma machine at Bletchley Park during World War II.

**d3: Mavis Batey**

- [d3s0] Mavis Lilian Batey, MBE( née Lever; 5 May 1921 – 12 November 2013), was an English code- breaker during World War II.
- [d3s1] Her work at Bletchley Park was one of the keys to the success of D- Day.
- [d3s2] She later became an historian of gardening, who campaigned to save historic parks and gardens, and an author.
- [d3s3] Batey was awarded the Veitch Memorial Medal in 1985, and made a Member of the Order of the British Empire( MBE) in 1987, in both cases for her work on the conservation of gardens.

**d4: Nayelly Hernández**

- [d4s0] Nayelly Hernández( born 23 February 1986) is a former Mexican female professional squash player.
- [d4s1] She has represented Mexico internationally in several international competitions including the Central American and Caribbean Games, Pan American Games, Women's World Team Squash Championships.
- [d4s2] Nayelly achieved her highest career ranking of 57 in October 2011 during the 2011 PSA World Tour.
- [d4s3] Her husband Chris Walker whose nationality is English is also a professional squash player.
- [d4s4] She joined the Trinity College in 2008 as the first Mexican female to join a US college for squash and graduated in 2010.

**d5: Baglan Mailybayev**

- [d5s0] Baglan Mailybayev( in Kazakh Бағлан Асаубайұлы Майлыбаев) was born on 20 May 1975 in Zhambyl region, Kazakhstan.
- [d5s1] His nationality is Kazakh.
- [d5s2] He is a politician of the Republic of Kazakhstan, Deputy Head of the Presidential Administration of the Republic of Kazakhstan, Doctor of Law( 2002)( under the supervision of Professor Zimanov S.Z.- scientific advisor and academician of National Academy of Sciences of the Republic of Kazakhstan) and Ph.D. in Political Science( 1998).

**d6: Eleni Gabre-Madhin**

- [d6s0] Eleni Zaude Gabre- Madhin, an Ethiopian economist with Swiss nationality, is a former Chief Executive Officer of the Ethiopia Commodity Exchange( ECX).
- [d6s1] She has had many years of experience working on agricultural markets – particularly in Sub- Saharan Africa – and has held senior positions in the World Bank, the International Food Policy Research Institute( Washington), and United Nations( Geneva).

**d7: Mário Laginha**

- [d7s0] Mário João Laginha dos Santos,( born April 25, 1960 in Lisbon), a pianist and composer, is one of the most well- known Portuguese jazz musicians today.
- [d7s1] He is mostly recognized for his collaborations with Portuguese jazz singer Maria João, with whom he recorded over a dozen albums and toured worldwide extensively.
- [d7s2] Other acknowledged collaboration work includes four- handed piano sessions with Bernardo Sassetti and Pedro Burmester.
- [d7s3] Mário's main influence on piano is Keith Jarrett.

**d8: Ali Rahuma**

- [d8s0] Ali Khalifa Rahuma( born May 16, 1982) is a Libyan football midfielder who's nationality is Libyan.
- [d8s1] He currently plays for Al- Ittihad, and is a member of the Libya national football team.

**d9: Malcolm Sinclair (actor)**

- [d9s0] Malcolm Sinclair( born 5 June 1950) is a British stage and television actor and former President of Trade Union, Equity 2010 – 18 when he stood down after 4 terms and was replaced by Maureen Beattie.
- [d9s1] He is perhaps best known for his role as Assistant Chief Constable Freddy Fisher in the television series" Pie in the Sky"( 1994 – 1997), although he has an extensive number of film, television and theatre roles to his credit.
- [d9s2] His brother is Keith Sinclair, the Bishop of Birkenhead.

**d10: Rebirth (Keith Sweat album)**

- [d10s0] Rebirth is Keith Sweat's eighth studio album.

## 7. 2wikimultihopqa_4dc594f408cd11ebbd93ac1f6bf848b6

原位置：`dev` 第 4 题 · 全局第 247 题 · `sample_id: 2wikimultihopqa_4dc594f408cd11ebbd93ac1f6bf848b6`

Question: Which film has the director died earlier, Schwarzwaldmelodie or Vacations in the Other World?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | director of Schwarzwaldmelodie | False | [] | Géza von Bolváry | [["d5s0"]] | context |
| u2 | death date of {u1} | False | ["u1"] | 10 August 1961 | [["d10s0"]] | context |
| u3 | director of Vacations in the Other World | False | [] | Mario Soffici | [["d2s0"]] | context |
| u4 | death date of {u3} | False | ["u3"] | 10 May 1977 | [["d7s0"]] | context |
| u5 | which film's director died earlier | True | ["u2", "u4"] | Schwarzwaldmelodie | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Schwarzwaldmelodie | False | [] | Géza von Bolváry | [['d5s0']] |
| u2 | date of death of {u1} | False | ['u1'] | 10 August 1961 | [['d10s0']] |
| u3 | director of film Vacations in the Other World | False | [] | Mario Soffici | [['d2s0']] |
| u4 | date of death of {u3} | False | ['u3'] | 10 May 1977 | [['d7s0']] |
| u5 | which of the two films has the director who died earlier | True | ['u2', 'u4'] | Schwarzwaldmelodie | [[]] |

### Source documents (reference only)

**d1: Le Masque de la Méduse**

- [d1s0] Le masque de la Méduse is a 2009 fantasy horror film directed by Jean Rollin.
- [d1s1] The film is a modern-day telling of the Greek mythological tale of the Gorgon and was inspired by the 1964 classic Hammer Horror film of the same name and the 1981 cult classic" Clash of the Titans".
- [d1s2] It was Rollin's final film, as the director died in 2010.

**d2: Vacations in the Other World**

- [d2s0] Vacations in the Other World or Vacaciones en el otro mundo is a 1942 Argentine film directed by Mario Soffici.
- [d2s1] The film, a seriocomedy, explores the gap between the high- pressure world of business and the ambience of domestic living.

**d3: A Groom from the Other World**

- [d3s0] A Groom from the Other World or is a 1958 Soviet comedy film directed by Leonid Gaidai.

**d4: Thulasi (1987 film)**

- [d4s0] Thulasi is a 1987 Tamil romantic drama film directed by Ameerjan.
- [d4s1] The film features Murali and Seetha in lead roles.
- [d4s2] The film, produced by P. S. V. Hariharan, had musical score by Sampath Selvam and was released on 27 November 1987.
- [d4s3] The music director died before the release of the film.

**d5: Schwarzwaldmelodie**

- [d5s0] Schwarzwaldmelodie is a 1956 West German film directed by Géza von Bolváry.
- [d5s1] The film was produced in de Ufa-Studios Berlin and in the Circus Roland.

**d6: Vacations in Majorca**

- [d6s0] Vacations in Majorca is a 1959 Italian comedy film directed by Giorgio Bianchi.

**d7: Mario Soffici**

- [d7s0] Mario Soffici( 14 May 1900 – 10 May 1977) was an Argentine film director, actor and screenwriter of the classic era.
- [d7s1] A native of Florence, Soffici moved to Argentina in the 1920s and began acting in 1931 and directing in 1935 on the film" El Alma de Bandoneón", working with popular actors of the period such as Libertad Lamarque in tango- based musical films.
- [d7s2] He directed some 40 films between 1935 and 1962, most notably" Prisioneros de la tierra"( 1939)( often cited as one of the greatest in Argentine cinema)," El Curandero"( 1955)," El hombre que debía una muerte"( 1955) and" Rosaura a las 10"( 1958).
- [d7s3] He directed and co- wrote with Eduardo Boneo and Francisco Madrid" La cabalgata del circo," where Eva Duarte played a supporting role.
- [d7s4] He died in Buenos Aires in 1977.

**d8: Mohsen Eslamzadeh**

- [d8s0] Mohsen Eslamzadeh is an Iranian documentary filmmaker.
- [d8s1] He is the director of" Alone Among The Taliban".
- [d8s2] This film has won the best documentary award at the 44th Athens International Film and Video Festival in the United States.
- [d8s3] This film has won the best documentary award at the 12th Marbella International Film Festival in Spain.
- [d8s4] This film has won the Shahid Avini Award offers.

**d9: Querelle**

- [d9s0] Querelle is a 1982 West German- French English- language drama film directed by Rainer Werner Fassbinder and starring Brad Davis, adapted from French author Jean Genet's 1947 novel" Querelle of Brest".
- [d9s1] It marked Fassbinder's final film as a writer/ director; it was posthumously released just months after the director died of a drug overdose in June 1982.

**d10: Géza von Bolváry**

- [d10s0] Géza von Bolváry (full name Géza Maria von Bolváry-Zahn; 26 December 1897 – 10 August 1961) was a Hungarian actor, screenwriter and film director, who worked principally in Germany and Austria.

## 8. 2wikimultihopqa_5ea97157099411ebbdb0ac1f6bf848b6

原位置：`dev` 第 5 题 · 全局第 248 题 · `sample_id: 2wikimultihopqa_5ea97157099411ebbdb0ac1f6bf848b6`

Question: Are Rasas and Barakuh, Roshtkhar located in the same country?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: comparison · fallback: False · SFT snapshots: 7

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | country of Rasas | False | [] | Syria | [["d9s0"]] | context |
| u2 | country of Barakuh, Roshtkhar | False | [] | Iran | [["d10s0"]] | context |
| u3 | whether Rasas and Barakuh, Roshtkhar are in the same country | True | ["u1", "u2"] | no | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country of Rasas | False | [] | Syria | [['d9s0']] |
| u2 | country of Barakuh, Roshtkhar | False | [] | Iran | [['d10s0']] |
| u3 | whether Rasas and Barakuh, Roshtkhar are located in the same country | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Satellite tournament**

- [d1s0] A satellite tournament is either a minor tournament or event on a competitive sporting tour or one of a group of such tournaments that form a series played in the same country or region.

**d2: Language Management**

- [d2s0] Language management is a discipline that consists of satisfying the needs of people who speak multiple different languages.
- [d2s1] These may be in the same country, in companies, and in cultural or international institutions where one must use multiple languages.

**d3: Kumaradeva**

- [d3s0] Kumaradeva was an Indian sculptor from the 8th century.
- [d3s1] His works include" The Buddhist Goddess Shyama Tara( Green Tara) Attended by Sita Tara( White Tara) and Bhrikuti"
- [d3s2] He is also the author of the treatise" Silparatna", which provides an account of the Fresco- secco painting technology in detail.
- [d3s3] According to this text, a picture should be painted with appropriate colours along with proper forms and sentiments( rasas), and moods and actions( bhavas).

**d4: 1992 Copa Libertadores**

- [d4s0] The 1992 Copa Libertadores was the 33rd edition of the Copa Libertadores, CONMEBOL's annual international club tournament.
- [d4s1] São Paulo won the competition.
- [d4s2] The participating teams were divided into five groups, in which teams of the same country were placed in the same group.
- [d4s3] Each country was represented by two teams.
- [d4s4] The countries were paired as follows:

**d5: Telephone numbers in Ascension Island**

- [d5s0] Country Code:+ 247< br> International Call Prefix: 00 Ascension Island does not share the same country code( +290) with the rest of St Helena.

**d6: 2001–02 UEFA Champions League second group stage**

- [d6s0] Eight winners and eight runners- up from the first group stage were drawn into four groups of four teams, each containing two group winners and two runners- up.
- [d6s1] Teams from the same country or from the same first round group could not be drawn together.
- [d6s2] The top two teams in each group advanced to the quarter- finals.

**d7: 1993 Copa Libertadores**

- [d7s0] The Copa Libertadores 1993 was the 34th edition of the Copa Libertadores, CONMEBOL's annual international club tournament.
- [d7s1] São Paulo won the competition.
- [d7s2] The participating teams were divided into five groups, in which teams of the same country were placed in the same group.
- [d7s3] Each country was represented by two teams.
- [d7s4] The countries were paired as follows:

**d8: 1971 Copa Libertadores**

- [d8s0] The Copa Libertadores 1971 was the 12th edition of the Copa Libertadores, CONMEBOL's annual international club tournament.
- [d8s1] Nacional won the competition.
- [d8s2] The participating teams were divided into five groups, in which teams of the same country were placed in the same group.
- [d8s3] Each country was represented by two teams.
- [d8s4] The countries were paired as follows:

**d9: Rasas**

- [d9s0] Rasas( also spelled Rsas) is a village in southern Syria, administratively part of the al- Suwayda Governorate, located south of al- Suwayda.
- [d9s1] Nearby localities include' Ira to the southwest, Sahwat Bilata to the east, al- Ruha to the northeast and Umm Walad to the west.
- [d9s2] According to the Syria Central Bureau of Statistics( CBS), Rasas had a population of 3,332 in the 2004 census.

**d10: Barakuh, Roshtkhar**

- [d10s0] Barakuh( also Romanized as Barākūh) is a village in Roshtkhar Rural District, in the Central District of Roshtkhar County, Razavi Khorasan Province, Iran.
- [d10s1] At the 2006 census, its population was 872, in 221 families.

## 9. 2wikimultihopqa_640bede1095311ebbdaeac1f6bf848b6

原位置：`dev` 第 6 题 · 全局第 249 题 · `sample_id: 2wikimultihopqa_640bede1095311ebbdaeac1f6bf848b6`

Question: Are Daher-Socata and Dsf Refractories & Minerals Ltd both located in the same country?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: comparison · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | country where Daher-Socata is located | False | [] | France | [["d6s1"]] | context |
| u2 | country where Dsf Refractories & Minerals Ltd is located | False | [] | United Kingdom | [["d4s0"]] | context |
| u3 | whether Daher-Socata and Dsf Refractories & Minerals Ltd are located in the same country | True | ["u1", "u2"] | no | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country of DAHER-SOCATA | False | [] | France | [['d6s1']] |
| u2 | country of DSF Refractories & Minerals Ltd | False | [] | United Kingdom | [['d4s0']] |
| u3 | whether Daher-Socata and DSF Refractories & Minerals Ltd are located in the same country | True | ['u1', 'u2'] | no | [[]] |

### Source documents (reference only)

**d1: Adam Sulzdorf-Liszkiewicz**

- [d1s0] Adam Sulzdorf- Liszkiewicz is a designer, scholar, and educator who teaches at Occidental College and is CEO of RUST LTD, both in Los Angeles.
- [d1s1] He is best known for his designs for popular virtual reality games and serious games.

**d2: Jawty**

- [d2s0] Jawty is part of the name of two villages, both located in Gmina Susz, within Iława County, Warmian- Masurian Voivodeship, Poland:

**d3: List of Capcom subsidiaries**

- [d3s0] Apart from the head office building and the R&D building of Capcom Co., Ltd., both located in Chūō -ku, Osaka, the Japanese parent company also has a branch office in the Shinjuku Mitsui Building in Nishi- Shinjuku, Shinjuku, Tokyo.
- [d3s1] It also has the Ueno Facility.
- [d3s2] a branch office in Iga, Mie Prefecture.
- [d3s3] The international Capcom Group currently encompasses 15 subsidiaries in Japan, North America, Europe, and East Asia.
- [d3s4] Affiliated companies include Koko Capcom Co., Ltd. in South Korea, Street Fighter Film, LLC in the United States, and Dellgamadas Co., Ltd.

**d4: DSF Refractories & Minerals Ltd**

- [d4s0] DSF Refractories and Minerals Limited (formerly Derbyshire Silica Firebrick Co Ltd) is the last major British producer of refractory products, both shaped and unshaped.
- [d4s1] DSF is located in Friden within the Derbyshire's Peak National Park.
- [d4s2] DSF also a processor and supplier of crushed and graded refractory raw materials for other applications such as coloured road-stone.
- [d4s3] By the 1960s, the business diversified into supplying other industries including steel, glass and cement.
- [d4s4] DSF was established in 1993 following the receivership of DSF Refractories Ltd and its parent company BH-F. British Hartford-Fairmont Ltd 'BH-F' had owned the company since 1987.
- [d4s5] They acquired DSF to support their business in the glass industry from West Group International 'WGI' who had as West Gas Improvement formed the company in 1892 as Derbyshire Silica Firebrick Ltd to support WGI's gas development business by the manufacture of refractories for use in the production of town gas.
- [d4s6] Nowadays the brickworks at Friden makes high-alumina refractory bricks and blocks which are exported worldwide for use by the heat containment industries, such as glass, cement, steel and petrochemical manufacturers.
- [d4s7] The company also supplies refractory minerals to other refractory manufacturers for use in the ceramics industries as well as in welding and road surface products.
- [d4s8] Despite the closure in the 1990s of the nearby silica pits which supplied raw materials, the company remains a major local employer.
- [d4s9] As at 2015, it employed approximately 115 people.

**d5: First Quantum Minerals**

- [d5s0] First Quantum Minerals Ltd. is a Canadian- based mining and metals company whose principal activities include mineral exploration, development and mining.
- [d5s1] Its main product is copper, which accounts for 80% of revenues as of 2016.
- [d5s2] First Quantum's common shares are listed for trading on the Toronto Stock Exchange in Canada( symbol" FM").
- [d5s3] Until 2016, First Quantum also maintained a secondary listing on the London Stock Exchange( symbol" FQM"), in the United Kingdom.

**d6: DAHER-SOCATA**

- [d6s0] DAHER- SOCATA( formerly SOCATA and EADS Socata) is a producer of general aviation aircraft propelled by piston engines and turboprops, including business planes, small personal or training aircraft, as well as the production of aircraft structures for other manufacturers such as Airbus, Dassault, Embraer, Eurocopter and Lockheed Martin.
- [d6s1] The company headquarters is currently located in Tarbes, France.
- [d6s2] In March 2015 the company name was again changed to just" Daher" as part of a rebranding to align the division with its parent company Daher.

**d7: Newhaven, Derbyshire**

- [d7s0] Newhaven is a hamlet in the county of Derbyshire, England, east of Hartington and west of Cromford.
- [d7s1] The principal employer in the area is DSF Refractories& Minerals Ltd.
- [d7s2] The hamlet is located within the Peak District National Park.

**d8: Lac Minerals Ltd v International Corona Resources Ltd**

- [d8s0] Lac Minerals Ltd v International Corona Resources Ltd is a leading Supreme Court of Canada decision on the nature of fiduciary and confidential relationships that can be created in the course of business, together with appropriate remedies for restitution when such relationships are breached.

**d9: Lubnowy**

- [d9s0] Lubnowy is part of the name of two villages, both located in Gmina Susz, within Iława County, Warmian- Masurian Voivodeship, Poland:

**d10: Radzice**

- [d10s0] Radzice is part of the name of two villages, both located in Gmina Drzewica, within Opoczno County, Łódź Voivodeship, Poland:

## 10. 2wikimultihopqa_6968dcf40bdc11eba7f7acde48001122

原位置：`dev` 第 7 题 · 全局第 250 题 · `sample_id: 2wikimultihopqa_6968dcf40bdc11eba7f7acde48001122`

Question: When is Adele Khoury Graham's husband's birthday?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | husband of Adele Khoury Graham | False | [] | Bob Graham | [["d7s1"]] | context |
| u2 | birthday of {u1} | True | ["u1"] | November 9, 1936 | [["d2s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | husband of Adele Khoury Graham | False | [] | Bob Graham | [['d7s1']] |
| u2 | date of birth of {u1} | True | ['u1'] | November 9, 1936 | [['d2s0']] |

### Source documents (reference only)

**d1: Theodred II (Bishop of Elmham)**

- [d1s0] Theodred II was a medieval Bishop of Elmham.
- [d1s1] The date of Theodred's consecration unknown, but the date of his death was sometime between 995 and 997.

**d2: Bob Graham**

- [d2s0] Daniel Robert Graham (born November 9, 1936) is an American politician and author who served as the 38th governor of Florida from 1979 to 1987 and a United States senator from Florida from 1987 to 2005.
- [d2s1] He is a member of the Democratic Party.
- [d2s2] Born in Coral Gables, Florida, Graham won election to the Florida Legislature after graduating from Harvard Law School.
- [d2s3] After serving in both houses of the Florida Legislature, Graham won the 1978 Florida gubernatorial election, and was reelected in 1982.
- [d2s4] In the 1986 Senate elections, Graham defeated incumbent Republican Senator Paula Hawkins.
- [d2s5] He helped found the Democratic Leadership Council and eventually became Chairman of the Senate Intelligence Committee.
- [d2s6] Graham ran for the 2004 Democratic presidential nomination, but dropped out before the first primaries.
- [d2s7] He declined to seek reelection in 2004 and retired from the Senate.
- [d2s8] Graham served as co-chair of the National Commission on the BP "Deepwater Horizon" Oil Spill and Offshore Drilling and as a member of the Financial Crisis Inquiry Commission and the CIA External Advisory Board.
- [d2s9] He works at the Bob Graham Center for Public Service at his undergraduate alma mater, the University of Florida.
- [d2s10] He also served as Chairman of the Commission on the Prevention of WMD proliferation and terrorism.
- [d2s11] Through the WMD policy center he advocates for the recommendations in the Commission's report, "World at Risk."
- [d2s12] In 2011, Graham published his first novel, the thriller "The Keys to the Kingdom".
- [d2s13] He has also written three nonfiction books: "
- [d2s14] Workdays: Finding Florida on the Job,Intelligence Matters", and "America: The Owner's Manual".

**d3: Pamela Jain**

- [d3s0] Pamela Jain is an Indian playback singer.
- [d3s1] Date of Birth:16th March.

**d4: Moffat Sinkala**

- [d4s0] Moffat Sinkala( date of birth unknown, died June 2004) was a Zambian footballer.
- [d4s1] He competed in the men's tournament at the 1980 Summer Olympics.

**d5: Etan Boritzer**

- [d5s0] Etan Boritzer( born 1950) is an American writer of children ’s literature who is best known for his book" What is God?" first published in 1989.
- [d5s1] His best selling" What is?" illustrated children's book series on character education and difficult subjects for children is a popular teaching guide for parents, teachers and child- life professionals.
- [d5s2] Boritzer gained national critical acclaim after" What is God?" was published in 1989 although the book has caused controversy from religious fundamentalists for its universalist views.
- [d5s3] The other current books in the" What is?" series include
- [d5s4] What is Love?,
- [d5s5] What is Death?,
- [d5s6] What is Beautiful?,
- [d5s7] What is Funny?,
- [d5s8] What is Right?,
- [d5s9] What is Peace?,
- [d5s10] What is Money?,
- [d5s11] What is Dreaming?,
- [d5s12] What is a Friend?,
- [d5s13] What is True?,
- [d5s14] What is a Family?,
- [d5s15] What is a Feeling?"
- [d5s16] The series is now also translated into 15 languages.
- [d5s17] Boritzer was first published in 1963 at the age of 13 when he wrote an essay in his English class at Wade Junior High School in the Bronx, New York on the assassination of John F. Kennedy.
- [d5s18] His essay was included in a special anthology by New York City public school children compiled and published by the New York City Department of Education.
- [d5s19] Boritzer now lives in Venice, California and maintains his publishing office there also.
- [d5s20] He has helped numerous other authors to get published through" How to Get Your Book Published!" programs.
- [d5s21] Boritzer is also a yoga teacher who teaches regular classes locally and guest- teaches nationally.
- [d5s22] He is also recognized nationally as an erudite speaker on" The Teachings of the Buddha."

**d6: Les Richards**

- [d6s0] Les Richards( date of birth unknown) was an Australian rules footballer who played with North Melbourne in the Victorian Football League( VFL).

**d7: Adele Khoury Graham**

- [d7s0] Adele Khoury Graham (born April 4, 1938) is an American educator and the former First Lady of Florida from 1979 to 1987.
- [d7s1] She is the wife of the 38th Governor of Florida and former United States Senator Bob Graham.
- [d7s2] Adele Graham was the First Lady of the state of Florida from 1979 to 1987.
- [d7s3] She spent her career as public school teacher in Massachusetts and Miami, Florida.
- [d7s4] In all, the Grahams have four children and 11 grandchildren.

**d8: Brian Saunders (weightlifter)**

- [d8s0] Brian Saunders( date of birth and death unknown) was a male weightlifter who competed for England.

**d9: Mark Kenneth Woods**

- [d9s0] Mark Kenneth Woods( date of birth unknown) is a Canadian comedy writer, actor, producer, director and TV host.

**d10: Terence Robinson**

- [d10s0] Terence D. Robinson( date of birth and death unknown) was a male wrestler who competed for England.

## 11. 2wikimultihopqa_6be60084088e11ebbd70ac1f6bf848b6

原位置：`dev` 第 8 题 · 全局第 251 题 · `sample_id: 2wikimultihopqa_6be60084088e11ebbd70ac1f6bf848b6`

Question: Which film has the director born earlier, Two Can Play or The Faithful River (Film)?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | director of Two Can Play | False | [] | Nat Ross | [["d3s0"]] | context |
| u2 | birth date of {u1} | False | ["u1"] | June 13, 1902 | [["d1s0"]] | context |
| u3 | director of The Faithful River (Film) | False | [] | Tadeusz Chmielewski | [["d10s0"]] | context |
| u4 | birth date of {u3} | False | ["u3"] | 7 June 1927 | [["d2s0"]] | context |
| u5 | which film's director was born earlier | True | ["u2", "u4"] | Two Can Play | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of Two Can Play | False | [] | Nat Ross | [['d3s0']] |
| u2 | date of birth of {u1} | False | ['u1'] | June 13, 1902 | [['d1s0']] |
| u3 | director of The Faithful River (film) | False | [] | Tadeusz Chmielewski | [['d10s0']] |
| u4 | date of birth of {u3} | False | ['u3'] | 7 June 1927 | [['d2s0']] |
| u5 | which of Two Can Play and The Faithful River has the director born earlier | True | ['u2', 'u4'] | Two Can Play | [[]] |

### Source documents (reference only)

**d1: Nat Ross**

- [d1s0] Nat Ross( June 13, 1902 – February 24, 1941) was an American film director and producer of the silent era.
- [d1s1] He directed 61 films between 1922 and 1931.
- [d1s2] He was born in San Francisco, California.
- [d1s3] He was shot dead in Los Angeles in 1941 by a disgruntled employee whom Ross had fired from the plant where Ross was working as foreman.
- [d1s4] He was the nephew of producer Carl Laemmle.

**d2: Tadeusz Chmielewski**

- [d2s0] Tadeusz Chmielewski (7 June 1927 – 4 December 2016) was a Polish film director, screenwriter and film producer, most notable for being one of the pioneers of popular Polish comedy.
- [d2s1] During World War II and until 1948, he was a soldier for the National Armed Forces and the Home Army.

**d3: Two Can Play**

- [d3s0] Two Can Play is a 1926 American silent drama film directed by Nat Ross and starring George Fawcett, Allan Forrest and Clara Bow.

**d4: Two Can Play That Game (film)**

- [d4s0] Two Can Play That Game is a 2001 romantic comedy film written and directed by Mark Brown and starring Vivica A. Fox and Morris Chestnut.

**d5: Fred Roy Krug**

- [d5s0] Fred R. Krug is an American film and television producer- director born in Bern, Switzerland.

**d6: Claude Weisz**

- [d6s0] Claude Weisz is a French film director born in Paris.

**d7: Three Can Play That Game**

- [d7s0] Three Can Play That Game is a 2007 romantic comedy film directed by Samad Davis and starring Jason George, Jazsmin Lewis, and Vivica A. Fox.
- [d7s1] It is a sequel to the 2001 film "Two Can Play That Game".

**d8: Jacques Décombe**

- [d8s0] Jacques Décombe is a French author, actor and director born in 1953.

**d9: Sepideh Farsi**

- [d9s0] Sepideh Farsi is an Iranian film director, born in Tehran in 1965.

**d10: The Faithful River (film)**

- [d10s0] The Faithful River is a Polish historical film directed by Tadeusz Chmielewski.
- [d10s1] It was produced in 1983 and released in 1987.

## 12. 2wikimultihopqa_75be1186086711ebbd5eac1f6bf848b6

原位置：`dev` 第 9 题 · 全局第 252 题 · `sample_id: 2wikimultihopqa_75be1186086711ebbd5eac1f6bf848b6`

Question: Are director of film Vivasaayi Magan and director of film When The Evening Bells Ring (1951 Film) both from the same country?

Note: 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | director of Vivasaayi Magan | False | [] | Ramarajan | [["d9s0"]] | context |
| u2 | nationality of {u1} | False | ["u1"] | Indian | [["d1s0"]] | context |
| u3 | director of When the Evening Bells Ring (1951 film) | False | [] | Alfred Braun | [["d3s0"]] | context |
| u4 | nationality of {u3} | False | ["u3"] | German | [["d4s0"]] | context |
| u5 | whether the directors of Vivasaayi Magan and When the Evening Bells Ring (1951 film) are from the same country | True | ["u2", "u4"] | no | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of Vivasaayi Magan | False | [] | Ramarajan | [['d9s0']] |
| u2 | nationality of {u1} | False | ['u1'] | Indian | [['d1s0']] |
| u3 | director of When the Evening Bells Ring (1951 film) | False | [] | Alfred Braun | [['d3s0']] |
| u4 | nationality of {u3} | False | ['u3'] | German | [['d4s0']] |
| u5 | whether the directors of Vivasaayi Magan and When the Evening Bells Ring (1951 film) are from the same country | True | ['u2', 'u4'] | no | [[]] |

### Source documents (reference only)

**d1: Ramarajan**

- [d1s0] Ramarajan is an Indian Tamil film Actor, Writer and Director who specialised in acting and directing films on village- based subjects.
- [d1s1] He is also known as" Makkal Nayagan".
- [d1s2] Many of his films were successful.
- [d1s3] He was called the rural box office emperor in the late 1980s.
- [d1s4] He is known for his colourful gaudy costumes and excessive makeup.
- [d1s5] His pairings with Rekha in Tamil cinema were his biggest hits.
- [d1s6] He has worked in more than 40 films and has directed more than 10 films.

**d2: When the Evening Bells Ring (1930 film)**

- [d2s0] When the Evening Bells Ring( German: Wenn die Abendglocken läuten) is a 1930 German silent drama film directed by Hanns Beck- Gaden and starring Josef Berger, Rosa Kirchner- Lang and Hanns Beck- Gaden.
- [d2s1] It is a heimatfilm set in Bavaria.

**d3: When the Evening Bells Ring (1951 film)**

- [d3s0] When the Evening Bells Ring is a 1951 West German drama film directed by Alfred Braun and starring Willy Birgel, Maria Holst and Paul Hörbiger.
- [d3s1] It is unrelated to the 1930 silent film of the same title.

**d4: Alfred Braun**

- [d4s0] Alfred Braun( 13 May 1888 – 3 January 1978) was a German screenwriter, actor and film director.

**d5: Ian Barry (director)**

- [d5s0] Ian Barry is an Australian director of film and TV.

**d6: Brian Johnson (special effects artist)**

- [d6s0] Brian Johnson( born 1939 or 1940) is a British designer and director of film and television special effects.

**d7: Ben Cura**

- [d7s0] Ben Cura( born 30 September 1988) is a British- Argentine actor and director of film, television and theatre.

**d8: Peter Levin**

- [d8s0] Peter Levin is an American director of film, television and theatre.

**d9: Vivasaayi Magan**

- [d9s0] Vivasaayi Magan is a 1997 Indian Tamil film, directed by Ramarajan and produced by Rani Azhakappan.
- [d9s1] The film stars Ramarajan, Devayani, K. R. Vijaya and Vadivelu in lead roles.
- [d9s2] The film had musical score by Sirpy.

**d10: Hanro Smitsman**

- [d10s0] Hanro Smitsman, born in 1967 in Breda( Netherlands), is a writer and director of film and television.

## 13. 2wikimultihopqa_7728ea720bb011ebab90acde48001122

原位置：`dev` 第 10 题 · 全局第 253 题 · `sample_id: 2wikimultihopqa_7728ea720bb011ebab90acde48001122`

Question: Who is Mariota, Countess Of Ross's father-in-law?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | husband of Mariota, Countess Of Ross | False | [] | Domhnall of Islay, Lord of the Isles | [["d5s1"]] | context |
| u2 | father of {u1}, Mariota, Countess Of Ross's father-in-law | True | ["u1"] | John of Islay | [["d6s1"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | spouse of Mariota, Countess of Ross | False | [] | Domhnall of Islay, Lord of the Isles | [['d5s1']] |
| u2 | father of {u1}, Mariota's father-in-law | True | ['u1'] | John of Islay | [['d6s1']] |

### Source documents (reference only)

**d1: James Armour (Master mason)**

- [d1s0] James Armour (15 January 1730 – 20 September 1798) was a master mason and father of Jean Armour, and therefore the father-in-law of the poet Robert Burns.

**d2: Alexander Leslie, Earl of Ross**

- [d2s0] Alexander Leslie, Earl of Ross( died 1402) was a Scottish nobleman.
- [d2s1] Born between 1367 and 1382, he was the son of Walter Leslie, Lord of Ross and Euphemia I, Countess of Ross.
- [d2s2] In around 1394 he became Earl of Ross and sometime before 1398 he married Isabel Stewart, daughter of Robert Stewart, Duke of Albany.
- [d2s3] They had one child, Euphemia.
- [d2s4] He died at Dingwall, Scotland on 8 May 1402.

**d3: Ogawa Mataji**

- [d3s0] Viscount was a general in the early Imperial Japanese Army.
- [d3s1] He was also the father- in- law of Field Marshal Gen Sugiyama.

**d4: Ludwig von Westphalen**

- [d4s0] Johann Ludwig von Westphalen( 11 July 1770 – 3 March 1842) was a liberal Prussian civil servant and the father- in- law of Karl Marx.

**d5: Mariota, Countess of Ross**

- [d5s0] Mariota, Countess of Ross( Mairead, also called Mary and Margaret; died 1440) was the daughter of Euphemia I, Countess of Ross and her husband, the crusading war- hero Walter Leslie, Lord of Ross.
- [d5s1] Upon the death of her brother, Alexander Leslie, Earl of Ross, she became the heir- presumptive of her niece Euphemia II, Countess of Ross although her husband Domhnall of Islay, Lord of the Isles pressed Mariota's superior claim to the earldom.
- [d5s2] Domhnall attempted to gain control of the earldom, and sometime after 1405 but before 1411, Domhnall gained control of Dingwall Castle.
- [d5s3] In the year after the death of the nominal king Robert III of Scotland( 1406), in August 1407, Domhnall sent emissaries to England to the heir of the throne, the captive James Stewart.
- [d5s4] King Henry IV of England sent his own emissaries the following year to negotiate an alliance against Robert Stewart, Duke of Albany, the Guardian of Scotland who was controlling Euphemia and the earldom.
- [d5s5] With control over the principal seat of the earldom of Ross and support of the exiled heir to the Scottish throne, in 1411 Domhnall felt strong enough to march against Albany's main northern ally, Alexander Stewart, Earl of Mar.
- [d5s6] At the Battle of Harlaw Domhnall failed to inflict a decisive victory, and withdrew back to the western highlands.
- [d5s7] In the aftermath, Albany was able to retake Dingwall and seize control of Easter Ross.
- [d5s8] In 1415, Euphemia was persuaded by Albany to resign the earldom to his own second son, John Stewart, Earl of Buchan.
- [d5s9] This action was challenged by Domhnall of Islay, who continued to claim the earldom on behalf of Mariota.
- [d5s10] After the return of King James the latter destroyed the power of the Albany Stewarts, executing the Albany's son and successor Murdoch Stewart, Duke of Albany.
- [d5s11] Domhnall had died in 1423, but Mariota continued to enjoy the support of his successor and her own son, Alexander.
- [d5s12] Alexander took over her claims, and in 1437 her son was recognized as earl by the king.
- [d5s13] She died in 1440.
- [d5s14] She had two known children, Alexander and Mariota.

**d6: Donald of Islay, Lord of the Isles**

- [d6s0] Donald, Lord of the Isles
- [d6s1] (Gaelic: "Dómhnall"; died 1423), was the son and successor of John of Islay, Lord of the Isles and chief of Clan Donald.
- [d6s2] The Lordship of the Isles was based in and around the Scottish west-coast island of Islay, but under Donald's father had come to include many of the other islands off the west coast of Scotland, as well as Morvern, Garmoran, Lochaber, Kintyre and Knapdale on the mainland.
- [d6s3] Donald was the grandson of King Robert II of Scotland and first cousin of King Robert III; he took pride in his royal blood, even adopting the royal tressure to surround his coat of arms.
- [d6s4] While it is customary to portray the Lords of the Isles as divorced from the mainstream of Scottish political life, and as representatives of a brand of lordship distinct from the rest of Scotland, this view obscures the fact that Donald was only one of many magnates who held large lordships with little interference from the crown in late 14th and early 15th century Scotland.
- [d6s5] The Douglas kindred of southern Scotland and the Albany Stewarts had similar roles as Donald.

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

**d8: William III, Earl of Ross**

- [d8s0] William( or Uilleam) III, 5th Earl of Ross( d. 1372) was a fourteenth- century Scottish nobleman.
- [d8s1] He was the fifth O’ Beolan earl of Ross, descending from the founder of the line, Fearchar of Ross( or Fearchar MacTaggart).

**d9: John Adams (merchant)**

- [d9s0] John Adams( 1672 or 1673 – 1745) was an American- born Canadian merchant and member of the Nova Scotia Council.
- [d9s1] He was the father- in- law of Henry Newton( politician).

**d10: Peter Burroughs**

- [d10s0] Peter Burroughs( born 27 January 1947) is a British television and film actor, the director of Willow Management.
- [d10s1] He is the father- in- law of actor and TV presenter Warwick Davis.

## 14. 2wikimultihopqa_7b9cef6a0bdb11eba7f7acde48001122

原位置：`dev` 第 11 题 · 全局第 254 题 · `sample_id: 2wikimultihopqa_7b9cef6a0bdb11eba7f7acde48001122`

Question: What is the cause of death of director of film The Magic Of Lassie?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | director of film The Magic Of Lassie | False | [] | Don Chaffey | [["d5s0"]] | context |
| u2 | cause of death of {u1} | True | ["u1"] | heart failure | [["d1s2"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film The Magic of Lassie | False | [] | Don Chaffey | [['d5s0']] |
| u2 | cause of death of {u1} | True | ['u1'] | heart failure | [['d1s2']] |

### Source documents (reference only)

**d1: Don Chaffey**

- [d1s0] Donald Chaffey (5 August 1917 – 13 November 1990) was a British film director, writer, producer, and art director.
- [d1s1] Chaffey's film career began as an art director in 1947, and his directorial debut was in 1953.
- [d1s2] He remained active in the industry until his death in 1990 from heart failure.
- [d1s3] His 1973 film "Charley One-Eye" was entered into the 24th Berlin International Film Festival
- [d1s4] He is chiefly known for his fantasy films, which include "Jason and the Argonauts" (1963), "The Three Lives of Thomasina" (1963), "One Million Years B.C." (1966), "The Viking Queen" (1967), "Creatures the World Forgot" (1971), "Pete's Dragon" (1977), and "C.H.O.M.P.S." (1979), his final feature film.
- [d1s5] Concurrent with his theatrically released films, Chaffey directed numerous British television series episodes, including several for "The PrisonerDanger Man", and "The Avengers".
- [d1s6] From the 1980s until his death, all of his work was in American made-for-TV movies, and in such TV series as "Fantasy IslandStingrayMacGyverVega$T. J. HookerMatt Houston" and "Charlie's Angels".

**d2: Josh Magette**

- [d2s0] Josh Magette( born November 28, 1989) is an American professional basketball player for the Orlando Magic of the National Basketball Association( NBA), on a two- way contract with the Lakeland Magic of the NBA G League.
- [d2s1] He played college basketball for the University of Alabama in Huntsville.

**d3: The Cutting Edge: The Magic of Movie Editing**

- [d3s0] The Cutting Edge: The Magic of Movie Editing is a 2004 documentary film directed by filmmaker Wendy Apple.
- [d3s1] The film is about the art of film editing.
- [d3s2] Clips are shown from many groundbreaking films with innovative editing styles.

**d4: Michael Sharrett**

- [d4s0] Stuart Michael Sharrett( born July 18, 1965) is an American actor.
- [d4s1] Best known for his role in the 1978 classic family movie" The Magic of Lassie" with James Stewart, Sharrett additionally co-starred in the 1985 action film" Savage Dawn" and in the 1986 Wes Craven horror film" Deadly Friend", for which he received a Young Artist Award nomination as the" Best Young Actor in a Horror Motion Picture".

**d5: The Magic of Lassie**

- [d5s0] The Magic of Lassie is a 1978 American family musical drama film directed by Don Chaffey, starring Lassie, James Stewart, Stephanie Zimbalist, Pernell Roberts, and Michael Sharrett, with cameo appearances by Mickey Rooney and Alice Faye (in her final film appearance).
- [d5s1] James Stewart is featured in one of only three musical film roles that he played
- [d5s2] : the first was "Born to Dance" (1936)
- [d5s3] in which he introduced the Cole Porter standard "Easy To Love" and the second was "Pot O' Gold" (1941).
- [d5s4] This was also his final onscreen appearance in a live-action film.
- [d5s5] The screenplay and song score are supplied by the prolific Sherman Brothers of "Mary Poppins" fame.
- [d5s6] Their song "
- [d5s7] When You're Loved" was nominated for an Academy Award for "Best Original Song" and was sung by Debby Boone.
- [d5s8] It is also the only musical film featuring Lassie.
- [d5s9] Released in the wake of "Star Wars", the film was panned as old-fashioned, and flopped at the box office.
- [d5s10] Critics expressed dismay at Stewart singing unmemorable songs as the grandfather.
- [d5s11] Following the film's failure, he semiretired from acting.

**d6: Ken Dancyger**

- [d6s0] Kennet Dancyger is a scriptwriting theoretician, film historian and expert on film editing and film production.
- [d6s1] He is professor of film and TV at Maurice Kanbar Institute of Film, Television,& New Media, Undergraduate.
- [d6s2] He has been the president of University Film and Video Association.
- [d6s3] He has taught film in the U.S. and Canada since 1968.
- [d6s4] His 2002 book contains a detailed comparison of screwball comedy and film noir.( p. 68) He has collaborated as historical consultant for the 2004 documentary" The Cutting Edge: The Magic of Movie Editing", about the art of film editing.

**d7: Courage of Lassie**

- [d7s0] Courage of Lassie is a 1946 Technicolor MGM feature film starring Elizabeth Taylor, Frank Morgan, and dog actor Pal in a story about a collie named Bill and his young companion, Kathie Merrick.
- [d7s1] When Bill is separated from Kathie following a vehicular accident, he is trained as a war dog, performs heroically, and, after many tribulations, is eventually reunited with his beloved Kathie.
- [d7s2] " Courage of Lassie" is the third of seven MGM films featuring a canine star called Lassie, based on Eric Knight's fictional character.
- [d7s3] Pal, a male Rough Collie, using the stage name Lassie, appeared as the title character in the first film," Lassie Come Home" and as Laddie in its sequel," Son of Lassie".
- [d7s4] Despite this film's title, the character Lassie does not appear in" Courage of Lassie"; Pal( credited as Lassie) portrays" Bill", also referred to as" Duke" for part of the movie.
- [d7s5] " Courage of Lassie" has been released to VHS and DVD.

**d8: Son of Lassie**

- [d8s0] Son of Lassie( also known as Laddie, Son of Lassie) is a 1945 Technicolor feature film produced by MGM based on characters created by Eric Knight, and starring Peter Lawford, Donald Crisp, June Lockhart and Pal( credited as Lassie).
- [d8s1] A sequel to" Lassie Come Home", the film focuses on the now adult Joe Carraclough after he joins the Royal Air Force during World War II and is shot down over Nazi-occupied Norway along with a stowaway, Lassie's son" Laddie" – played by Pal." Son of Lassie" was released theatrically on April 20, 1945, by Loew's.

**d9: Richard T. Jones**

- [d9s0] Richard Timothy Jones( born January 16, 1972) is an American actor.
- [d9s1] Jones is best known for his portrayals of Laveinio in the dramatic film" The Wood"( 1999) and Mike of the dramatic films" Why Did I Get Married?"( 2007) and" Why Did I Get Married Too?"( 2010).
- [d9s2] He is also well known for his role as Bruce Van Exel, court services officer on the CBS television series" Judging Amy" that aired from 1999 to 2005.

**d10: B. J. Johnson (basketball)**

- [d10s0] Robert" B. J." Johnson Jr.( born December 21, 1995) is an American professional basketball player for the Orlando Magic of the National Basketball Association( NBA), on a two- way contract with the Lakeland Magic of the NBA G League.
- [d10s1] He played college basketball for La Salle and Syracuse.

## 15. 2wikimultihopqa_874c55c20bda11eba7f7acde48001122

原位置：`dev` 第 12 题 · 全局第 255 题 · `sample_id: 2wikimultihopqa_874c55c20bda11eba7f7acde48001122`

Question: What is the date of death of the director of film The Social Buccaneer (1916 Film)?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | director of The Social Buccaneer (1916 Film) | False | [] | Jack Conway | [["d1s0"]] | context |
| u2 | date of death of {u1} | True | ["u1"] | October 11, 1952 | [["d2s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film The Social Buccaneer (1916 film) | False | [] | Jack Conway | [['d1s0']] |
| u2 | date of death of {u1} | True | ['u1'] | October 11, 1952 | [['d2s0']] |

### Source documents (reference only)

**d1: The Social Buccaneer (1916 film)**

- [d1s0] The Social Buccaneer is a 1916 American silent drama film directed by Jack Conway and starring J. Warren Kerrigan, Louise Lovely and Maude George.

**d2: Jack Conway (filmmaker)**

- [d2s0] Jack Ryan Conway (July 17, 1887 – October 11, 1952) was an American film director and film producer, as well as an actor of many films in the first half of the 20th century.

**d3: Peter Levin**

- [d3s0] Peter Levin is an American director of film, television and theatre.

**d4: Etan Boritzer**

- [d4s0] Etan Boritzer( born 1950) is an American writer of children ’s literature who is best known for his book" What is God?" first published in 1989.
- [d4s1] His best selling" What is?" illustrated children's book series on character education and difficult subjects for children is a popular teaching guide for parents, teachers and child- life professionals.
- [d4s2] Boritzer gained national critical acclaim after" What is God?" was published in 1989 although the book has caused controversy from religious fundamentalists for its universalist views.
- [d4s3] The other current books in the" What is?" series include
- [d4s4] What is Love?,
- [d4s5] What is Death?,
- [d4s6] What is Beautiful?,
- [d4s7] What is Funny?,
- [d4s8] What is Right?,
- [d4s9] What is Peace?,
- [d4s10] What is Money?,
- [d4s11] What is Dreaming?,
- [d4s12] What is a Friend?,
- [d4s13] What is True?,
- [d4s14] What is a Family?,
- [d4s15] What is a Feeling?"
- [d4s16] The series is now also translated into 15 languages.
- [d4s17] Boritzer was first published in 1963 at the age of 13 when he wrote an essay in his English class at Wade Junior High School in the Bronx, New York on the assassination of John F. Kennedy.
- [d4s18] His essay was included in a special anthology by New York City public school children compiled and published by the New York City Department of Education.
- [d4s19] Boritzer now lives in Venice, California and maintains his publishing office there also.
- [d4s20] He has helped numerous other authors to get published through" How to Get Your Book Published!" programs.
- [d4s21] Boritzer is also a yoga teacher who teaches regular classes locally and guest- teaches nationally.
- [d4s22] He is also recognized nationally as an erudite speaker on" The Teachings of the Buddha."

**d5: Ian Barry (director)**

- [d5s0] Ian Barry is an Australian director of film and TV.

**d6: Thomas Scott (diver)**

- [d6s0] Thomas Scott( 1907- date of death unknown) was an English diver.

**d7: Harry Wainwright (footballer)**

- [d7s0] Harry Wainwright( born 1899; date of death unknown) was an English footballer.

**d8: Bill Smith (footballer, born 1897)**

- [d8s0] William Thomas Smith( born 9 April 1897, date of death unknown) was an English professional footballer.

**d9: Albert Thompson (footballer, born 1912)**

- [d9s0] Albert Thompson( born 1912, date of death unknown) was a Welsh footballer.

**d10: Theodred II (Bishop of Elmham)**

- [d10s0] Theodred II was a medieval Bishop of Elmham.
- [d10s1] The date of Theodred's consecration unknown, but the date of his death was sometime between 995 and 997.

## 16. 2wikimultihopqa_8e463167086c11ebbd61ac1f6bf848b6

原位置：`dev` 第 13 题 · 全局第 256 题 · `sample_id: 2wikimultihopqa_8e463167086c11ebbd61ac1f6bf848b6`

Question: Which film has the director who died later, The Purple Heart or How Mcdougall Topped The Score?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | director of The Purple Heart | False | [] | Lewis Milestone | [["d10s0"]] | context |
| u2 | death date of {u1} | False | ["u1"] | September 25, 1980 | [["d7s0"]] | context |
| u3 | director of How Mcdougall Topped The Score | False | [] | Victor Upton-Brown | [["d8s0"]] | context |
| u4 | death date of {u3} | False | ["u3"] | 23 May 1964 | [["d9s0"]] | context |
| u5 | which film's director died later | True | ["u2", "u4"] | The Purple Heart | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film The Purple Heart | False | [] | Lewis Milestone | [['d10s0']] |
| u2 | date of death of {u1} | False | ['u1'] | September 25, 1980 | [['d7s0']] |
| u3 | director of film How McDougall Topped the Score | False | [] | Victor Upton-Brown | [['d8s0']] |
| u4 | date of death of {u3} | False | ['u3'] | 23 May 1964 | [['d9s0']] |
| u5 | which of The Purple Heart and How McDougall Topped the Score has the director who died later | True | ['u2', 'u4'] | The Purple Heart | [[]] |

### Source documents (reference only)

**d1: Danny Dietz**

- [d1s0] Daniel Phillip Dietz Jr (January 26, 1980 – June 28, 2005) was a Navy SEAL who was awarded the U.S. Navy's second highest decoration, the Navy Cross, along with the Purple Heart, for his actions during the War in Afghanistan.

**d2: Don W. Sears**

- [d2s0] Don W. Sears was the eighth Dean and Professor Emeritus of Law at the University of Colorado Law School.
- [d2s1] Sears was also a two- time recipient of the Purple Heart and Bronze Star for his military service during World War II.

**d3: Tyler Ziegel**

- [d3s0] Tyler W." Ty" Ziegel( October 16, 1982 – December 26, 2012) was a United States Marine Corps sergeant who suffered severe burns during the Iraq War.
- [d3s1] He received the Purple Heart medal.

**d4: Joe Steffy**

- [d4s0] Joseph Benton" Joe" Steffy, Jr.( April 3, 1926 – May 22, 2011) was an American football player.
- [d4s1] He went to fight in the Korean War and received the Bronze Star Medal and the Purple Heart.
- [d4s2] Steffy was inducted into the College Football Hall of Fame.

**d5: Annie Fox (nurse)**

- [d5s0] Lt. Annie G. Fox( August 4, 1893 – January 20, 1987) was the first woman to receive the Purple Heart for combat.
- [d5s1] She served as the chief nurse in the Army Nurse Corps at Hickam Field during the Japanese attack on Pearl Harbor, on December 7, 1941.
- [d5s2] At that time the awarding of the Purple Heart did not require the service member to be injured.
- [d5s3] The requirements were changed after the attack of Pearl Harbor and Lt. Fox was awarded the Bronze Star because Fox was not wounded in the attack.

**d6: Needham Roberts**

- [d6s0] Needham Roberts( April 28, 1901 – April 18, 1949) was an American soldier in the Harlem Hellfighters and recipient of the Purple Heart and the Croix de Guerre for his valor during World War I.

**d7: Lewis Milestone**

- [d7s0] Lewis Milestone( born Leib Milstein; September 30, 1895 – September 25, 1980) was a Russian- born American motion picture director.
- [d7s1] He is known for directing" Two Arabian Knights"( 1927) and" All Quiet on the Western Front"( 1930), both of which received Academy Awards for Best Director.
- [d7s2] He also directed" The Front Page"( 1931 – nomination)," The General Died at Dawn"( 1936)," Of Mice and Men"( 1939)," Ocean's 11"( 1960), and received the directing credit for" Mutiny on the Bounty"( 1962), though Marlon Brando largely appropriated his responsibilities during its production.

**d8: How McDougall Topped the Score**

- [d8s0] How McDougall Topped the Score is a 1924 Australian silent film directed by Victor Upton-Brown.
- [d8s1] It is based on a famous poem by Thomas Edward Spencer about a cricket match won when a dog steals a ball, enabling the batting team to score plenty of runs.
- [d8s2] It is considered a lost film.

**d9: Victor Upton-Brown**

- [d9s0] Victor Upton-Brown (1 November 1880 – 23 May 1964) was an Australian rules football coach who coached University for a season while they were in the Victorian Football League (VFL).
- [d9s1] Upton-Brown coached University when Gerald Brosnan stepped aside for the 1913 season but couldn't steer the club to a single win from his 18 games in charge.
- [d9s2] When not coaching, Upton-Brown spent some time as a boundary and field umpire in the VFL.
- [d9s3] He was involved in the early Australian movie industry, writing and directing a movie based on the play 'How McDougall Topped the Score' which was released in 1924.
- [d9s4] He is also credited as having acted in the 1920 film: The Kelly Gang, which starred Godfrey Cass.
- [d9s5] He also taught at Wesley College in Melbourne and is credited as the lyricist of several school songs, including "Grey Towers".
- [d9s6] He was also the editor of the 1910 version of that school's songbook.
- [d9s7] He opened the South Yarra Cinema in the suburb of South Yarra, Melbourne, on 22 November 1915, where he lectured on movies.
- [d9s8] He was an occasional contributor to "The Argus" newspaper in Melbourne, Australia, during 1914 and 1915.

**d10: The Purple Heart**

- [d10s0] The Purple Heart is a 1944 American black- and- white war film, produced by Darryl F. Zanuck, directed by Lewis Milestone, and starring Dana Andrews, Richard Conte, Don" Red" Barry, Sam Levene and Trudy Marshall.
- [d10s1] Eighteen- year- old Farley Granger had a supporting role.
- [d10s2] The film is a dramatization of the" show trial" of a number of US airmen by the Japanese government during World War II.
- [d10s3] It is loosely based on the trial of eight US airmen who took part in the April 18, 1942, Doolittle Raid on Japan.
- [d10s4] Three were later executed and one died as a POW.
- [d10s5] This film was the first to deal directly with the Japanese treatment of POWs and ran into opposition from the US War Department, which was afraid that such films would provoke reprisals from the Japanese government.

## 17. 2wikimultihopqa_8ec76c0808db11ebbd9cac1f6bf848b6

原位置：`dev` 第 14 题 · 全局第 257 题 · `sample_id: 2wikimultihopqa_8ec76c0808db11ebbd9cac1f6bf848b6`

Question: Do both films: All The Winners and Mano Po 6: A Mother'S Love have the directors from the same country?

Note: 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | director of All the Winners | False | [] | Geoffrey Malins | [["d7s0"]] | context |
| u2 | nationality of {u1} | False | ["u1"] | British | [["d6s0"]] | context |
| u3 | director of Mano Po 6: A Mother's Love | False | [] | Joel Lamangan | [["d10s4"]] | context |
| u4 | nationality of {u3} | False | ["u3"] | Filipino | [["d5s0"]] | context |
| u5 | whether the directors of All the Winners and Mano Po 6: A Mother's Love are from the same country | True | ["u2", "u4"] | no | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of All the Winners | False | [] | Geoffrey Malins | [['d7s0']] |
| u2 | nationality of {u1} | False | ['u1'] | British | [['d6s0']] |
| u3 | director of Mano Po 6: A Mother's Love | False | [] | Joel Lamangan | [['d10s4']] |
| u4 | nationality of {u3} | False | ['u3'] | Filipino | [['d5s0']] |
| u5 | whether the directors of All the Winners and Mano Po 6: A Mother's Love are from the same country | True | ['u2', 'u4'] | no | [[]] |

### Source documents (reference only)

**d1: Mano Po 5: Gua Ai Di**

- [d1s0] Mano Po 5: Gua Ai Di( also billed parenthetically as Mano Po 5: Gua Ai Di( I Love You)) is a 2006 Filipino film starring Filipino actors Angel Locsin as Charity and Richard Gutierrez as Nathan.
- [d1s1] Nathan is a veterinarian with playboy tendencies who falls in love with Charity, a Chinese Filipino who always follows tradition.
- [d1s2] In order to woo not only Charity but also her family, Nathan tries to follow and adapt Chinese culture, but with hilarious results.
- [d1s3] Unlike the other films in the series," Mano Po 5" is a romantic comedy- drama film.
- [d1s4] The film stars Lorna Tolentino, Angel Locsin and Richard Gutierrez, which already starred together in" Mano Po 2: My Home".
- [d1s5] Asia's Superstar and" Star In A Million" finalist Christian Bautista also appeared in his first film at the height of his successful musical career.

**d2: Mano Po III: My Love**

- [d2s0] Mano Po III: My Love is the third installment of the Mano Po anthology, following the success of" Mano Po" and" Mano Po 2: My Home".
- [d2s1] Produced by Regal Entertainment through MAQ Productions," Mano Po III" stars Vilma Santos in the leading role.

**d3: Ako Legal Wife**

- [d3s0] Mano Po 4: Ako Legal Wife is Regal Entertainment's entry for the 2005 Metro Manila Film Festival.
- [d3s1] The film focuses on the lives of the Chinese- Filipino community, but rather in a wackiest way unlike in the first 3 Mano Po installments which are used in a melodramatic way.
- [d3s2] It stars Jay Manalo, Zsa Zsa Padilla as Chona the Legal Wife, Cherry Pie Picache as Patty the Lucky Wife and Rufa Mae Quinto as Gloria the Latest Wife.
- [d3s3] The title is considered as the fourth installment of Mano Po and was based on the line of Zsa Zsa Padilla in the movie Mano Po 2: My Home," Ako Legal Wife!"
- [d3s4] Aside from the other Mano Po films this film is the first comedy from the series since three of the films in the beginning centered on perplex drama

**d4: Mano Po**

- [d4s0] Mano Po is Regal Entertainment's entry for the 2002 Metro Manila Film Festival.
- [d4s1] The film focuses on the lives of the Chinese Filipino community.
- [d4s2] " Mano Po" stars an all- star cast headed by Maricel Soriano, Richard Gomez, Kris Aquino and Ara Mina.
- [d4s3] Eddie Garcia and Boots Anson- Roa play the patriarch and matriarch of the Go clan respectively.
- [d4s4] The film won the most major awards in the film- awarding bodies, including 12 awards in the 28th Manila Film Festival in 2002.
- [d4s5] It was named Best Picture, Best Actor( for Eddie Garcia), Best Actress( for Ara Mina), Best Supporting Actress( for Kris Aquino) and Best Director( for Joel Lamangan).
- [d4s6] " Mano Po" was among the top- grossing films in time for the Metro Manila Filmfest.
- [d4s7] The film's success was followed by another episode," Mano Po 2: My Home" and a spin- off, that was released in 2007.

**d5: Joel Lamangan**

- [d5s0] Joel Lamangan( born September 21, 1952) is a Filipino film director, television director and actor.
- [d5s1] His award- winning films includes" The Flor Contemplacion StorySidhiDeathrowHubogAishte Imasu 1941 Blue Moon" and" Mano Po".
- [d5s2] On August 19, 2008, Lamangan directed his first indie movie" Walang Kawala" produced by DMV Entertainment.
- [d5s3] It stars Polo Ravales and Joseph Bitangcol, with the special participation of Jean Garcia.
- [d5s4] Joel also directs" Obra" and will soon start shooting Desperadas
- [d5s5] 2.
- [d5s6] He started production for the next Sine Novela:" Una Kang Naging Akin" starring Angelika dela Cruz, Wendell Ramos, and Maxene Magalona.
- [d5s7] In 2013 Elections he ran as congressman for Cavite's 1st District under the Lakas- CMD/ United Nationalist Alliance/ Partido Magdalo.
- [d5s8] However he backed out in the race.
- [d5s9] In 2013, Lamangan was named as the artistic director of Gantimpala Theater Foundation.
- [d5s10] Lamangan will direct an original musical titled" Katipunan: Mga Anak ng Bayan" and it will star actors Sandino Martin and Anna Fegi.
- [d5s11] The show toured in August and September 2013 around provinces of Manila to celebrate the 150th anniversary of the birth of Philippine hero, Andres Bonifacio.
- [d5s12] Lamangan is a member of the international Order of DeMolay from Baja Chapter, Cavite City.
- [d5s13] He was conferred with the highest honor being a DeMolay to the rank of Legion of Honor last November 14, 2015, by the Grand Master Victor Antonio T. Espejo of the Supreme Council Order of DeMolay Philippines for outstanding leadership in his field of endeavor, for service to humanity, for success in fraternal life, including adult service to the Order of DeMolay.
- [d5s14] The Supreme Council Order of DeMolay is an appendant body of Freemasonry.

**d6: Geoffrey Malins**

- [d6s0] Arthur" Geoffrey" Herbert Malins( 18 November 1886 – 1940) was a British film director most famous for camera and editing work on the 1916 war film" The Battle of the Somme", which combined documentary and propaganda, and reached an audience of over 20 million viewers.

**d7: All the Winners**

- [d7s0] All the Winners is a 1920 British silent sports film directed by Geoffrey Malins and starring Owen Nares, Maudie Dunham and Sam Livesey.
- [d7s1] It is set in the horse racing world.
- [d7s2] It was made at Isleworth Studios.

**d8: Mano Po 7: Tsinoy**

- [d8s0] Mano Po 7: Chinoy is a Filipino film starring Richard Yap, Jean Garcia and Enchong Dee.
- [d8s1] The film is the 7th installment of the Mano Po franchise from Regal Entertainment.
- [d8s2] It tells the story of a modern Chinese Filipino family.
- [d8s3] Beneath the facade of a typical well- off Chinese Filipino family, it also tackles the struggles of family life as well as how they managed to reunite themselves as one.
- [d8s4] The film was shown in theatres starting December 14, 2016.
- [d8s5] But was delayed due to insistent public demand that film was re-run in theatres starting February 8, 2017.
- [d8s6] The film starred Richard Yap making him the first male main protagonist in the entire Mano Po film series.
- [d8s7] It was also the second Mano Po movie that was not directed by Joel Lamangan who directed" Mano PoMano
- [d8s8] Po 4: Ako Legal Wife" and.

**d9: Mano Po 2: My Home**

- [d9s0] Mano
- [d9s1] Po 2: My Home is the second installment of the Mano Po franchise, after Mano Po( 2002).
- [d9s2] Produced by Regal Entertainment, Mano Po 2 stars Susan Roces in the leading role.
- [d9s3] This was also the first Mano Po movie that was not directed by Joel Lamangan, director of the first movie; rather it was directed by Erik Matti.
- [d9s4] It was one of the official entries in the 2003 Metro Manila Film Festival which garnered 5 awards alongside Filipinas.

**d10: Mano Po 6: A Mother's Love**

- [d10s0] Mano
- [d10s1] Po 6: A Mother's Love is the sixth installment in the Mano Po film franchise, following in 2006.
- [d10s2] Produced by Regal Entertainment," Mano Po 6" marks the first appearance of Sharon Cuneta in a Regal movie.
- [d10s3] Co- starring with Sharon are: Zsa Zsa Padilla( in her third Mano Po role), Christopher De Leon, Boots Anson- Roa( fourth appearance in the Mano Po series), Kris Aquino( in her third Mano Po role), Dennis Trillo( in another Mano Po appearance, last seen in), former ABS- CBN talent and GMA actress Heart Evangelista, and Ciara Sotto.
- [d10s4] Joel Lamangan, who had last worked with Sharon in Walang Kapalit, was at the helm, in his fifth Mano Po directorial job.
- [d10s5] The movie which was a 2009 Metro Manila Film Festival entry had its theater run from 25 December 2009 to January 2010.

## 18. 2wikimultihopqa_971f9d7a0bd911eba7f7acde48001122

原位置：`dev` 第 15 题 · 全局第 258 题 · `sample_id: 2wikimultihopqa_971f9d7a0bd911eba7f7acde48001122`

Question: When was the director of film The Big Bang (1989 Film) born?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | director of The Big Bang (1989 Film) | False | [] | James Toback | [["d5s0"]] | context |
| u2 | birth date of {u1} | True | ["u1"] | November 23, 1944 | [["d4s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film The Big Bang (1989 film) | False | [] | James Toback | [['d5s0']] |
| u2 | date of birth of {u1} | True | ['u1'] | November 23, 1944 | [['d4s0']] |

### Source documents (reference only)

**d1: Ian Barry (director)**

- [d1s0] Ian Barry is an Australian director of film and TV.

**d2: Kevin Sussman**

- [d2s0] Kevin Sussman( born December 4, 1970) is an American actor and comedian.
- [d2s1] He played Walter on the ABC comedy- drama" Ugly Betty" and Stuart Bloom on the CBS sitcom" The Big Bang Theory".
- [d2s2] Starting with the sixth season of" The Big Bang Theory", he was promoted to a series regular.

**d3: Ralph Asher Alpher**

- [d3s0] Ralph Asher Alpher( February 3, 1921 – August 12, 2007) was an American cosmologist, who carried out pioneering work in the early 1950s on the Big Bang model, including Big Bang nucleosynthesis and predictions of the cosmic microwave background radiation.

**d4: James Toback**

- [d4s0] James Toback (born November 23, 1944) is an American screenwriter and film director.
- [d4s1] He was nominated for the Academy Award for Best Original Screenplay in 1991 for "Bugsy".
- [d4s2] He has directed films including "The Pick-up ArtistTwo Girls and a Guy" and "Black and White".
- [d4s3] On October 22, 2017, the "Los Angeles Times" reported that 38 women have accused Toback of sexual harassment or assault.
- [d4s4] Since the article was published, 357 additional women contacted "Los Angeles Times" and said that Toback had sexually harassed them.
- [d4s5] The accounts stretch over a 40-year period.
- [d4s6] Toback has denied all the allegations.

**d5: The Big Bang (1989 film)**

- [d5s0] The Big Bang is a 1989 documentary film, directed by Academy Award- nominated screenwriter James Toback.
- [d5s1] The film addresses questions about life and existence.
- [d5s2] It was released to theaters May 11, 1990, and aired on PBS on August 6, 1991.

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

**d7: Eric Lerner**

- [d7s0] Eric J. Lerner( born May 31, 1947) is an American popular science writer, and independent plasma researcher.
- [d7s1] He wrote the 1991 book" The Big Bang Never Happened", which advocates Hannes Alfvén's plasma cosmology instead of the Big Bang theory.
- [d7s2] He is founder, president, and chief scientist of Lawrenceville Plasma Physics, Inc.

**d8: Theodred II (Bishop of Elmham)**

- [d8s0] Theodred II was a medieval Bishop of Elmham.
- [d8s1] The date of Theodred's consecration unknown, but the date of his death was sometime between 995 and 997.

**d9: Brian Saunders (weightlifter)**

- [d9s0] Brian Saunders( date of birth and death unknown) was a male weightlifter who competed for England.

**d10: Terence Robinson**

- [d10s0] Terence D. Robinson( date of birth and death unknown) was a male wrestler who competed for England.

## 19. 2wikimultihopqa_9eb9f3480baf11ebab90acde48001122

原位置：`dev` 第 16 题 · 全局第 259 题 · `sample_id: 2wikimultihopqa_9eb9f3480baf11ebab90acde48001122`

Question: Who is the paternal grandfather of Princess Jeguk?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | father of Princess Jeguk | False | [] | Kublai Khan | [["d9s2"]] | context |
| u2 | father of {u1}, Princess Jeguk's paternal grandfather | True | ["u1"] | Tolui | [["d4s3"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Princess Jeguk | False | [] | Kublai Khan | [['d9s2']] |
| u2 | father of {u1}, Princess Jeguk's paternal grandfather | True | ['u1'] | Tolui | [['d4s3']] |

### Source documents (reference only)

**d1: Abd al-Muttalib**

- [d1s0] Abd al- Muttalib Shaybah ibn Hashim( c. 497 – 578) was the grandfather of Islamic prophet Muhammad.

**d2: Fred Le Deux**

- [d2s0] Frederick" Fred" Le Deux( born 4 December 1934) was an Australian rules footballer who played with Geelong in the Victorian Football League( VFL).
- [d2s1] He is the grandfather of Tom Hawkins.

**d3: John Westley**

- [d3s0] Rev. John Westley( 1636 – 78) was an English nonconformist minister.
- [d3s1] He was the grandfather of John Wesley( founder of Methodism).

**d4: Kublai Khan**

- [d4s0] Kublai  was the fifth Khagan (Great Khan) of the Mongol Empire ("Ikh Mongol Uls"), reigning from 1260 to 1294
- [d4s1] (although after the division of the empire this was a nominal position).
- [d4s2] He also founded the Yuan dynasty in China as a conquest dynasty in 1271, and ruled as the first Yuan emperor until his death in 1294.
- [d4s3] Kublai was the fourth son of Tolui (his second son with Sorghaghtani Beki) and a grandson of Genghis Khan.
- [d4s4] He succeeded his older brother Möngke as Khagan in 1260, but had to defeat his younger brother Ariq Böke in the Toluid Civil War lasting until 1264.
- [d4s5] This episode marked the beginning of disunity in the empire.
- [d4s6] Kublai's real power was limited to China and Mongolia, though as Khagan he still had influence in the Ilkhanate and, to a significantly lesser degree, in the Golden Horde.
- [d4s7] If one counts the Mongol Empire at that time as a whole, his realm reached from the Pacific Ocean to the Black Sea, from Siberia to what is now Afghanistan.
- [d4s8] In 1271, Kublai established the Yuan dynasty, which ruled over present-day Mongolia, China, Korea, and some adjacent areas, and assumed the role of Emperor of China.
- [d4s9] By 1279, the Mongol conquest of the Song dynasty was completed and Kublai became the first non-Han emperor to conquer all of China.
- [d4s10] The imperial portrait of Kublai was part of an album of the portraits of Yuan emperors and empresses, now in the collection of the National Palace Museum in Taipei.
- [d4s11] White, the color of the royal costume of Kublai, was the imperial color of the Yuan dynasty.

**d5: Lyon Cohen**

- [d5s0] Lyon Cohen( 1868–1937) was a Polish- born Canadian businessman and a philanthropist.
- [d5s1] He was the grandfather of singer/ poet Leonard Cohen.

**d6: Henry Krause**

- [d6s0] Henry J." Red" Krause, Jr.( August 28, 1913 – February 20, 1987) was an American football offensive lineman in the National Football League for the Brooklyn Dodgers and the Washington Redskins.
- [d6s1] He played college football at St. Louis University.
- [d6s2] He is the grandfather of Jennifer Krause
- [d6s3] He is the great grandfather of Payton Hoeing

**d7: Kaya Alp**

- [d7s0] Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

**d8: John Mackay (poet)**

- [d8s0] John Mackay( 1656–1754), known as( The Blind Piper), was a Scottish Gaelic poet and composer, and the grandfather of William Ross.

**d9: Princess Jeguk**

- [d9s0] "Daejang"-Princess Jeguk (28 June 1259 – 21 May 1297, "Princess-Aunt of the State of Je") or Empress Inmyeong was queen consort to king Chungnyeol of Goryeo and the mother of king Chungseon of Goryeo.
- [d9s1] She was the first Mongol queen of Korea, having gone to Goryeo from the Yuan dynasty.
- [d9s2] Her father was Kublai Khan.
- [d9s3] Princesses qualified as  were aunts of the emperor.
- [d9s4] She was the aunt of Temür Khan, who later succeeded her father as the Yuan emperor.

**d10: Zhao Shoushan**

- [d10s0] Zhao Shoushan( 12 November 1894 – 20 June 1965) was a KMT general and later Chinese Communist Party politician.
- [d10s1] He is the grandfather of Zhao Leji.

## 20. 2wikimultihopqa_b200fa00097e11ebbdb0ac1f6bf848b6

原位置：`dev` 第 17 题 · 全局第 260 题 · `sample_id: 2wikimultihopqa_b200fa00097e11ebbdb0ac1f6bf848b6`

Question: Which film was released earlier, It'S Kind Of A Funny Story (Film) or The Education Of Nicky?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: comparison · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | release year of It'S Kind Of A Funny Story (Film) | False | [] | 2010 | [["d5s0"], ["d5s2"], ["d8s1"]] | context |
| u2 | release year of The Education Of Nicky | False | [] | 1921 | [["d4s0"]] | context |
| u3 | which film was released earlier | True | ["u1", "u2"] | The Education of Nicky | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | release year of It's Kind of a Funny Story | False | [] | 2010 | [['d5s0'], ['d5s2'], ['d8s1']] |
| u2 | release year of The Education of Nicky | False | [] | 1921 | [['d4s0']] |
| u3 | which of It's Kind of a Funny Story and The Education of Nicky was released earlier | True | ['u1', 'u2'] | The Education of Nicky | [[]] |

### Source documents (reference only)

**d1: A Cinderella Story: Christmas Wish**

- [d1s0] A Cinderella Story: Christmas
- [d1s1] Wish is a 2019 American teen comedy musical film written and directed by Michelle Johnston and starring Laura Marano and Gregg Sulkin.
- [d1s2] It is the fifth installment of" A Cinderella Story" film series.
- [d1s3] The film was released digitally on October 15, 2019, and DVD on October 29, 2019.

**d2: The Education of Fairies**

- [d2s0] The Education of Fairies  is a 2006 international co-production drama film directed by José Luis Cuerda.

**d3: Hum Hai Raahi Car Ke**

- [d3s0] Hum Hai Raahi
- [d3s1] Car
- [d3s2] Ke is a comedy misadventure love story film directed by Jyotin Goel, that was released in India on 24 May 2013.

**d4: The Education of Nicky**

- [d4s0] The Education of Nicky is a 1921 British silent romance film directed by Arthur Rooke and starring James Knight, Marjorie Villis and Constance Worth.
- [d4s1] It was based on a novel by May Wynn.

**d5: It's Kind of a Funny Story (film)**

- [d5s0] It's Kind of a Funny Story is a 2010 American comedy- drama film written and directed by Anna Boden and Ryan Fleck, an adaptation of Ned Vizzini's 2006 novel of the same name.
- [d5s1] The film stars Keir Gilchrist, Zach Galifianakis, Emma Roberts, and Viola Davis.
- [d5s2] It was released in the United States on October 8, 2010, and received mixed to positive reviews.

**d6: The Wonderful World of Captain Kuhio**

- [d6s0] The film was released in Japan on 10 October 2009.

**d7: Hate Story**

- [d7s0] Hate Story is a 2012 Indian Hindi- language erotic thriller film directed by Vivek Agnihotri and produced by Vikram Bhatt.
- [d7s1] It stars Nikhil Dwivedi, Gulshan Devaiya and Paoli Dam in lead roles and the film was released on 20 April 2012.
- [d7s2] The first installment in the" Hate Story" film series the film was a commercial and critical success.
- [d7s3] The premise of the film chronicles a woman and her struggle to fight against the man that betrayed her.

**d8: Keir Gilchrist**

- [d8s0] Keir David Peters Gilchrist( born 28 September 1992) is an English- born Canadian actor.
- [d8s1] Gilchrist is known for playing Marshall Gregson on Showtime's original series" United States of Tara", Craig Gilner in the 2010 comedy- drama film" It's Kind of a Funny Story", Paul in" It Follows", and Sam Gardner in the Netflix original series" Atypical".

**d9: The Education of Sonny Carson**

- [d9s0] The Education of Sonny Carson is a 1974 film based on the best- selling autobiography of Sonny Carson.

**d10: Hate Story 3**

- [d10s0] Hate Story 3 is a 2015 Indian Hindi- language Bollywood erotic thriller film directed by Vishal Pandya.
- [d10s1] Produced by T- Series, it stars Sharman Joshi, Karan Singh Grover, Zareen Khan and Daisy Shah in lead roles, and Priyanshu Chatterjee in a pivotal role.
- [d10s2] Written by Vikram Bhatt and Madhuri Banerji, the film is part of the" Hate Story" film series.
- [d10s3] The film was released on 4 December 2015.
- [d10s4] The film was a box office success.

## 21. 2wikimultihopqa_ba5637db098c11ebbdb0ac1f6bf848b6

原位置：`dev` 第 18 题 · 全局第 261 题 · `sample_id: 2wikimultihopqa_ba5637db098c11ebbdb0ac1f6bf848b6`

Question: Are Nahr-E Shahab and Bazm, Fars located in the same country?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | country of Nahr-E Shahab | False | [] | Iran | [["d8s0"]] | context |
| u2 | country of Bazm, Fars | False | [] | Iran | [["d10s0"]] | context |
| u3 | whether Nahr-E Shahab and Bazm, Fars are located in the same country | True | ["u1", "u2"] | yes | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country where Nahr-e Shahab is located | False | [] | Iran | [['d8s0']] |
| u2 | country where Bazm, Fars is located | False | [] | Iran | [['d10s0']] |
| u3 | whether Nahr-e Shahab and Bazm, Fars are located in the same country | True | ['u1', 'u2'] | yes | [[]] |

### Source documents (reference only)

**d1: Language Management**

- [d1s0] Language management is a discipline that consists of satisfying the needs of people who speak multiple different languages.
- [d1s1] These may be in the same country, in companies, and in cultural or international institutions where one must use multiple languages.

**d2: 2001–02 UEFA Champions League second group stage**

- [d2s0] Eight winners and eight runners- up from the first group stage were drawn into four groups of four teams, each containing two group winners and two runners- up.
- [d2s1] Teams from the same country or from the same first round group could not be drawn together.
- [d2s2] The top two teams in each group advanced to the quarter- finals.

**d3: 1971 Copa Libertadores**

- [d3s0] The Copa Libertadores 1971 was the 12th edition of the Copa Libertadores, CONMEBOL's annual international club tournament.
- [d3s1] Nacional won the competition.
- [d3s2] The participating teams were divided into five groups, in which teams of the same country were placed in the same group.
- [d3s3] Each country was represented by two teams.
- [d3s4] The countries were paired as follows:

**d4: 1992 Copa Libertadores**

- [d4s0] The 1992 Copa Libertadores was the 33rd edition of the Copa Libertadores, CONMEBOL's annual international club tournament.
- [d4s1] São Paulo won the competition.
- [d4s2] The participating teams were divided into five groups, in which teams of the same country were placed in the same group.
- [d4s3] Each country was represented by two teams.
- [d4s4] The countries were paired as follows:

**d5: Telephone numbers in Ascension Island**

- [d5s0] Country Code:+ 247< br> International Call Prefix: 00 Ascension Island does not share the same country code( +290) with the rest of St Helena.

**d6: 1993 Copa Libertadores**

- [d6s0] The Copa Libertadores 1993 was the 34th edition of the Copa Libertadores, CONMEBOL's annual international club tournament.
- [d6s1] São Paulo won the competition.
- [d6s2] The participating teams were divided into five groups, in which teams of the same country were placed in the same group.
- [d6s3] Each country was represented by two teams.
- [d6s4] The countries were paired as follows:

**d7: Zelzal**

- [d7s0] Zelzal( meaning" Earthquake") is a series of artillery rockets developed by Iran.
- [d7s1] The series consists of:
- [d7s2] These rockets were developed by SAHID Hassan Tehrani Moghaddam, after developed the Shahab- 1 and the Shahab- 2.

**d8: Nahr-e Shahab**

- [d8s0] Nahr -e Shahab( also Romanized as Nahr -e Shahāb; also known as Shahāb) is a village in Buzi Rural District, in the Central District of Shadegan County, Khuzestan Province, Iran.
- [d8s1] At the 2006 census, its existence was noted, but its population was not reported.

**d9: Satellite tournament**

- [d9s0] A satellite tournament is either a minor tournament or event on a competitive sporting tour or one of a group of such tournaments that form a series played in the same country or region.

**d10: Bazm, Fars**

- [d10s0] Bazm( also known as Bāz) is a village in Sarvestan Rural District, in the Central District of Bavanat County, Fars Province, Iran.
- [d10s1] At the 2006 census, its population was 422, in 111 families.

## 22. 2wikimultihopqa_bc7761cc088511ebbd6dac1f6bf848b6

原位置：`dev` 第 19 题 · 全局第 262 题 · `sample_id: 2wikimultihopqa_bc7761cc088511ebbd6dac1f6bf848b6`

Question: Do both films, Joe Somebody and Figures of the Night, have the directors who are from the same country?

Note: 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### Adjusted units and annotation

**执行结果：** 采用旧版多单元/查询目标，保留可独立表达的中间事实；按 context 核对答案与证据。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | director of Joe Somebody | False | [] | John Pasquin | [["d8s0"]] | context |
| u2 | nationality of {u1} | False | ["u1"] | American | [["d3s0"]] | context |
| u3 | director of Figures of the Night | False | [] | Richard Oswald | [["d1s0"]] | context |
| u4 | nationality of {u3} | False | ["u3"] | Austrian | [["d10s0"]] | context |
| u5 | whether the directors of Joe Somebody and Figures of the Night are from the same country | True | ["u2", "u4"] | no | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of Joe Somebody | False | [] | John Pasquin | [['d8s0']] |
| u2 | nationality of {u1} | False | ['u1'] | American | [['d3s0']] |
| u3 | director of Figures of the Night | False | [] | Richard Oswald | [['d1s0']] |
| u4 | nationality of {u3} | False | ['u3'] | Austrian | [['d10s0']] |
| u5 | whether the directors of Joe Somebody and Figures of the Night are from the same country | True | ['u2', 'u4'] | no | [[]] |

### Source documents (reference only)

**d1: Figures of the Night**

- [d1s0] Figures of the Night( German:Nachtgestalten) is a 1920 German silent horror film written, directed and produced by Richard Oswald and starring Paul Wegener, Conrad Veidt, Reinhold Schünzel and Erna Morena.
- [d1s1] It is based on the novel" Eleagabal Kuperus" by Karl Hans Strobl.
- [d1s2] Strobl was the editor of a German horror fiction magazine called" Der Orchideengarten" which was said to have been influenced by the works of Edgar Allan Poe.
- [d1s3] Strobl was an anti-Semitic and later willingly joined the Nazi Party, which may explain why he has become an obscure literary figure today.
- [d1s4] The film's art direction was by Hans Dreier, and Carl Hoffmann handled the cinematography.
- [d1s5] Hoffmann went on to collaborate with such noted German directors as Fritz Lang and F.W. Murnau.
- [d1s6] It was filmed at the Babelsberg Studio in Berlin.

**d2: The Night and You**

- [d2s0] The Night and You( Spanish: La Noche y tú) is a 1946 Mexican film.
- [d2s1] It was directed by Chano Urueta.

**d3: John Pasquin**

- [d3s0] John Pasquin( born November 30, 1944) is an American director of film, television and theatre.

**d4: You and the Night and the Music (Helen Merrill album)**

- [d4s0] You and The Night and The Music is a 1998 studio album by Helen Merrill.

**d5: After the Night and the Music**

- [d5s0] After the Night and the Music is a one- act play in three parts, written by Elaine May.
- [d5s1] It opened in 2005.
- [d5s2] May derived the name of the play from the Howard Dietz song" You and the Night and the Music".

**d6: Matt Corboy**

- [d6s0] Matt Corboy( born June 4, 1973) is an American actor.
- [d6s1] He has appeared in both films and television series.

**d7: Night and Day**

- [d7s0] Night and Day may refer to:

**d8: Joe Somebody**

- [d8s0] Joe Somebody is a 2001 American comedy-drama film written by John Scott Shepherd and directed by John Pasquin.
- [d8s1] The film stars Tim Allen as an ordinary man forced into violence by a workplace bully.
- [d8s2] The film also stars Julie Bowen, Kelly Lynch, Greg Germann, Hayden Panettiere, Patrick Warburton and Jim Belushi.
- [d8s3] Screenwriter John Scott Shepherd wrote the script based on his experiences working in advertising.
- [d8s4] Though originally offered to Jim Carrey, the role of Joe Scheffer would eventually be taken by Allen.
- [d8s5] The film marked Allen and Pasquin's third feature together, after 1994's "The Santa Clause" and 1997's "Jungle 2 Jungle".
- [d8s6] The entire film was shot over a nearly eight-week span in Minnesota.
- [d8s7] The film was released in the U.S. on December 21, 2001, to negative reviews.
- [d8s8] Produced on a $38 million budget, the film ended its theatrical run with $24.5 million worldwide, making it a financial failure.
- [d8s9] The film received one award nomination, which went to young Panettiere's performance as the title character's daughter.

**d9: Francis Gouldman**

- [d9s0] Francis Gouldman(" c." 1607–1688/89) was a Church of England clergyman and lexicographer whose Latin- English dictionary( 1664) went through several editions.
- [d9s1] Gouldman was also one of the directors who oversaw the publication of the monumental" Critici sacri", a major collection of Biblical criticism.

**d10: Richard Oswald**

- [d10s0] Richard Oswald (5 November 1880 – 11 September 1963) was an Austrian director, producer, and screenwriter.

## 23. 2wikimultihopqa_bf1ebaa80bda11eba7f7acde48001122

原位置：`dev` 第 20 题 · 全局第 263 题 · `sample_id: 2wikimultihopqa_bf1ebaa80bda11eba7f7acde48001122`

Question: What is the date of death of Lord Frederick Spencer Hamilton's mother?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | mother of Lord Frederick Spencer Hamilton | False | [] | Lady Louisa Jane Russell | [["d7s0"]] | context |
| u2 | date of death of {u1} | True | ["u1"] | 31 March 1905 | [["d5s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | mother of Lord Frederick Spencer Hamilton | False | [] | Lady Louisa Jane Russell | [['d7s0']] |
| u2 | date of death of {u1} | True | ['u1'] | 31 March 1905 | [['d5s0']] |

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

**d2: Sophie Winkleman**

- [d2s0] Sophie Lara Winkleman (born 5 August 1980) is an English actress.
- [d2s1] She is the wife of Lord Frederick Windsor, son of Queen Elizabeth II's first cousin Prince Michael of Kent, and as such is also known as Lady Frederick Windsor.

**d3: Thomas Scott (diver)**

- [d3s0] Thomas Scott( 1907- date of death unknown) was an English diver.

**d4: Lord Frederick Cavendish-Bentinck**

- [d4s0] Major-General Lord Frederick Cavendish-Bentinck (2 November 1781 – 10 February 1828) known as Lord Frederick Bentinck was a British soldier and politician.
- [d4s1] The youngest child and fourth son of William Cavendish-Bentinck, 3rd Duke of Portland and Lady Dorothy Cavendish, Cavendish-Bentinck attended Westminster School before joining the army.

**d5: Louisa Hamilton, Duchess of Abercorn**

- [d5s0] Louisa Jane Hamilton, Duchess of Abercorn, VA( née Lady Louisa Jane Russell)( 8 July 1812 – 31 March 1905) was a member of the British aristocracy.
- [d5s1] She was the sister of Prime Minister John Russell, 1st Earl Russell, and among her descendants are two British princesses( Diana and Sarah) and Prince Richard, Duke of Gloucester.

**d6: Frederick Robb**

- [d6s0] Major- General Sir Frederick Spencer Wilson Robb,( 8 October 1858 – 8 February 1948) was a senior British Army officer who went on to be Military Secretary.

**d7: Lord Frederick Spencer Hamilton**

- [d7s0] Lord Frederick Spencer Hamilton (13 October 1856 – 11 August 1928) was a Conservative Party politician in the United Kingdom, the sixth son of James Hamilton, 1st Duke of Abercorn and Lady Louisa Jane Russell.
- [d7s1] He was Second Secretary of the Diplomatic Service (1877–1884) and Member of Parliament (MP) for Manchester South West (1885–1886) and North Tyrone (1892–1895).
- [d7s2] Lord Frederick also wrote the books "
- [d7s3] Here, There and
- [d7s4] EverywhereThe Days Before Yesterday" and "Vanished Pomps of Yesterday" which was first published in 1920 by Hodder and Stoughton Ltd, London.
- [d7s5] These give vivid accounts of his life in the diplomatic service.
- [d7s6] While serving as aide-de-camp to Lord Lansdowne, then Governor-General of Canada, in Ottawa, Lord Frederick was the first person to introduce skiing to Canada.
- [d7s7] From 1896 to 1900, he was editor of the Pall Mall Magazine.
- [d7s8] He never married and died without children.

**d8: Lord Frederick Paulet**

- [d8s0] Lieutenant General Lord Frederick Paulet,( 12 May 1810 – 1 January 1871) was a senior British Army officer.

**d9: Bill Smith (footballer, born 1897)**

- [d9s0] William Thomas Smith( born 9 April 1897, date of death unknown) was an English professional footballer.

**d10: Theodred II (Bishop of Elmham)**

- [d10s0] Theodred II was a medieval Bishop of Elmham.
- [d10s1] The date of Theodred's consecration unknown, but the date of his death was sometime between 995 and 997.

## 24. 2wikimultihopqa_d690e9a809bc11ebbdb0ac1f6bf848b6

原位置：`dev` 第 21 题 · 全局第 264 题 · `sample_id: 2wikimultihopqa_d690e9a809bc11ebbdb0ac1f6bf848b6`

Question: Are both high schools, Warwick Valley High School and Yoncalla High School, located in the same country?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: comparison · fallback: False · SFT snapshots: 9

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | country where Warwick Valley High School is located | False | [] | United States | [["d3s0"]] | context |
| u2 | country where Yoncalla High School is located | False | [] | United States | [["d5s0"]] | context |
| u3 | whether both high schools are located in the same country | True | ["u1", "u2"] | yes | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | country where Warwick Valley High School is located | False | [] | United States | [['d3s0']] |
| u2 | country where Yoncalla High School is located | False | [] | United States | [['d5s0']] |
| u3 | whether Warwick Valley High School and Yoncalla High School are located in the same country | True | ['u1', 'u2'] | yes | [[]] |

### Source documents (reference only)

**d1: North Valley High School**

- [d1s0] North Valley High School is a public high school located in Grants Pass, Oregon, United States.

**d2: Calloway County High School**

- [d2s0] Calloway County
- [d2s1] High School is a public high school located in Murray, Kentucky.
- [d2s2] The school was formed from the consolidation of six high schools from across the county: Hazel High School, Lynn Grove High School, Kirksey High School, Almo High School, New Concord High School, and Faxon High School.

**d3: Warwick Valley High School**

- [d3s0] Warwick Valley High School( WVHS) is located on Sanfordville Road outside the Village of Warwick, New York, United States.
- [d3s1] It educates students in grades 9 through 12 in the Warwick Valley Central School District, which covers most of the village and town of Warwick, including the hamlet of Pine Island.
- [d3s2] Students in those portions of the town near the village of Florida and the village of Greenwood Lake attend other high schools.
- [d3s3] A referendum to send students from the latter community to WVHS failed in 2007.

**d4: Metea Valley High School**

- [d4s0] Metea Valley High School is a high school in Aurora, Illinois that opened in August 2009 in DuPage County.
- [d4s1] The school is one of four high schools operated by the Indian Prairie School District.
- [d4s2] The others in Aurora are Waubonsie Valley High School and Indian Plains, while Neuqua Valley High School is in Naperville.

**d5: Yoncalla High School**

- [d5s0] Yoncalla High School is a public high school in Yoncalla, Oregon, United States.

**d6: Sioux Valley High School**

- [d6s0] Sioux Valley High School is a high school located in Volga, South Dakota, USA.

**d7: Midland High School (Midland, Michigan)**

- [d7s0] Midland High School is a three- story public high school located in Midland, Michigan.
- [d7s1] It is the older of two high schools in the Midland Public Schools district, and a member of the Saginaw Valley High School Association.

**d8: River Valley High School (Michigan)**

- [d8s0] River Valley High School is the high school for the River Valley School District located in Three Oaks, Michigan, United States.
- [d8s1] River Valley High School houses grades 6-12.

**d9: Eagle Valley High School**

- [d9s0] Eagle Valley High School( EVHS) is a high school located in Gypsum, Colorado.

**d10: Tippecanoe Valley High School**

- [d10s0] Tippecanoe Valley High School is a high school located in Akron, Indiana.
- [d10s1] Home of the Vikings.

## 25. 2wikimultihopqa_d996cdce0baf11ebab90acde48001122

原位置：`dev` 第 22 题 · 全局第 265 题 · `sample_id: 2wikimultihopqa_d996cdce0baf11ebab90acde48001122`

Question: Who is the child of Uday Tikekar?

Note: 保留 single，context 直接说明 Swanandi 是 Uday 的女儿，不需要配偶链，也不从妻子的孩子推断父亲。

Type: single · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留 single，context 直接说明 Swanandi 是 Uday 的女儿，不需要配偶链，也不从妻子的孩子推断父亲。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | child of Uday Tikekar | True | [] | Swanandi Tikekar | [["d4s0", "d4s1"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | spouse of Uday Tikekar | False | [] | Arati Ankalikar-Tikekar | [['d6s2']] |
| u2 | child of Uday Tikekar, given {u1} as his spouse | True | ['u1'] | Swanandi Tikekar | [['d1s4'], ['d4s1']] |

### Source documents (reference only)

**d1: Arati Ankalikar-Tikekar**

- [d1s0] Arati Ankalikar-Tikekar (born January 27, 1963 in Vijayapura, Karnataka) is a two-time National Award-winning Indian classical singer who is active mostly in Marathi, Konkani and Hindi film Industry; known for high-pitch singing and style, earned in Agra as well as Gwalior and Jaipur.
- [d1s1] Arati has been credited by audio cassettes and CD recordings.
- [d1s2] She was the main playback singer for the Sham Benegal's film, "Sardari Begum".
- [d1s3] She is known for her albums "Tejomay NadbrahmRaag-Rang", and, playback for the movies "AntarnaadDe dhakkaSavlee", and the hit "Sardari BegumEk Hazarachi Note".
- [d1s4] Her daughter Swanandi Tikekar who is in her mid-twenties dabbles in acting as well.

**d2: Chakrabongse Bhuvanath**

- [d2s0] Field Marshal Chakrabongse Bhuvanath, the Prince of Bishnulok( 3 March 1883 – 13 June 1920), was the 40th child of King Chulalongkorn and the fourth child of Queen Sri Bajarindra.

**d3: Prince Hodong of Goguryeo**

- [d3s0] Hodong is a child of Daemusin of Goguryeo who was the third king of Goguryeo.

**d4: Swanandi Tikekar**

- [d4s0] Swanandi Tikekar(born 13 November) in a Marathi actress.
- [d4s1] She is daughter of Uday Tikekar and Aarti Ankalikar.
- [d4s2] She pursued a masters in law from ILS College.
- [d4s3] She is well known for her role as Minal in Dil Dosti Duniyadari and Mukta in Dil Dosti Dobara.
- [d4s4] She was also seen in the plays "Ek Shoonya Teen" and "Don't Worry Be Happy."

**d5: Ingegerd Birgersdotter of Bjelbo**

- [d5s0] Ingegerd( or" Ingegärd")
- [d5s1] Birgersdotter of Bjelbo( or" Bjälbo"; ca.
- [d5s2] 1180 – 7 April after 1210, possibly 1230) was a Swedish Queen Consort, second spouse of King Sverker II of Sweden.
- [d5s3] Ingegerd was born into one of Sweden's most powerful noble families, the Bjälbo family, as the child of the powerful Jarl Birger Brosa and the Queen Dowager Brigida Haraldsdotter; her mother was the child of King Harald Gille of Norway and had, in her first marriage, herself been the Queen of Sweden in 1160 – 1161.

**d6: Uday Tikekar**

- [d6s0] Uday Tikekar( Marathi: उदय टिकेकर) is an Indian film and television actor.
- [d6s1] He began his career in Marathi theatre, also putting up performances in Hindi theatre.
- [d6s2] He is married to classical singer Arati Ankalikar- Tikekar, who is a 2- time National Film Award winner.

**d7: U. R. Lalit**

- [d7s0] U. R. Lalit is a senior counsel practising at Supreme Court of India and a former additional judge of the Delhi High Court.
- [d7s1] He is father of Uday U. Lalit, judge of Supreme Court of India.

**d8: Princess Hyomyeong**

- [d8s0] Princess Hyomyeong/ Hyo-Myung( 1637- 1700), was the child of King Injo, the sixteenth king of the Joseon dynasty in Korea, and his Consort, Lady Gwi- in Jo.
- [d8s1] She was the only daughter of King Injo.

**d9: Benito di Paula**

- [d9s0] Benito di Paula, stage name of Uday Velloso( born 28 November 1941), is a Brazilian singer- songwriter and pianist.

**d10: Latif Yahia**

- [d10s0] Latif Yahia(" Laṭīf Yaḥīa"; born 14 June 1964) is an Iraqi- born author and former combatant in the Iran – Iraq War.
- [d10s1] Two journalists have disputed this and other claims made by Yahia.
- [d10s2] He is best known for being the alleged former body double of Uday Hussein, the son of Iraqi dictator Saddam Hussein.

## 26. 2wikimultihopqa_e5f6937a0bae11ebab90acde48001122

原位置：`dev` 第 23 题 · 全局第 266 题 · `sample_id: 2wikimultihopqa_e5f6937a0bae11ebab90acde48001122`

Question: Who is the maternal grandfather of Tiberius Gemellus?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | mother of Tiberius Gemellus | False | [] | Livilla | [["d10s3"]] | context |
| u2 | father of {u1}, Tiberius Gemellus's maternal grandfather | True | ["u1"] | Nero Claudius Drusus | [["d4s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | mother of Tiberius Gemellus | False | [] | Livilla | [['d10s3']] |
| u2 | father of {u1}, Tiberius Gemellus's maternal grandfather | True | ['u1'] | Nero Claudius Drusus | [['d4s0']] |

### Source documents (reference only)

**d1: Kaya Alp**

- [d1s0] Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

**d2: John Westley**

- [d2s0] Rev. John Westley( 1636 – 78) was an English nonconformist minister.
- [d2s1] He was the grandfather of John Wesley( founder of Methodism).

**d3: Abd al-Muttalib**

- [d3s0] Abd al- Muttalib Shaybah ibn Hashim( c. 497 – 578) was the grandfather of Islamic prophet Muhammad.

**d4: Livilla**

- [d4s0] Claudia Livia Julia (Classical Latin: ; c. 13 BC – AD 31) was the only daughter of Nero Claudius Drusus and Antonia Minor and sister of the Roman Emperor Claudius and general Germanicus, and thus the paternal aunt of the emperor Caligula and maternal great-aunt of emperor Nero, as well as the niece and daughter-in-law of Tiberius.
- [d4s1] She was named after her grandmother, Augustus' wife Livia Drusilla, and commonly known by her family nickname Livilla ("little Livia").
- [d4s2] She was born after Germanicus and before Claudius.
- [d4s3] She was twice married to the potential successor in the Julio-Claudian dynasty, first to Augustus' grandson Gaius Caesar
- [d4s4] (died 4 AD) and later to Tiberius' son Drusus the Younger (died AD 23).
- [d4s5] Allegedly, she helped her lover Sejanus in poisoning her second husband and died shortly after Sejanus fell from power in AD 31.

**d5: Zhao Shoushan**

- [d5s0] Zhao Shoushan( 12 November 1894 – 20 June 1965) was a KMT general and later Chinese Communist Party politician.
- [d5s1] He is the grandfather of Zhao Leji.

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

**d9: John Mackay (poet)**

- [d9s0] John Mackay( 1656–1754), known as( The Blind Piper), was a Scottish Gaelic poet and composer, and the grandfather of William Ross.

**d10: Tiberius Gemellus**

- [d10s0] Tiberius Julius Caesar Nero Gemellus, known as Tiberius Gemellus (Latin: "
- [d10s1] Tiberius Caesar Drusus filius
- [d10s2] Tiberius Augustus nepos divus
- [d10s3] Augustus pronepos"; 10 October AD 19–37/38) was the son of Drusus and Livilla, the grandson of the Emperor Tiberius, and the second cousin of the Emperor Caligula.
- [d10s4] "
- [d10s5] Gemellus" is a nickname meaning "the twin".
- [d10s6] His twin brother, Tiberius Claudius Caesar Germanicus II Gemellus, died while still an infant in 23.
- [d10s7] His father and older cousins died, and are suspected by contemporary sources as having been systematically eliminated by the powerful praetorian prefect Sejanus.
- [d10s8] Their removal allowed Gemellus and Caligula to be named joint-heirs by Tiberius in 35, a decision that ultimately resulted in Caligula assuming power and having Gemellus killed, or by forcing him to kill himself, in late 37 or early 38.

## 27. 2wikimultihopqa_e95cb5fc085d11ebbd5cac1f6bf848b6

原位置：`dev` 第 24 题 · 全局第 267 题 · `sample_id: 2wikimultihopqa_e95cb5fc085d11ebbd5cac1f6bf848b6`

Question: Which film whose director was born first, Zanjeer (1973 Film) or The Legend Of Lylah Clare?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge_comparison · fallback: False · SFT snapshots: 10

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | director of Zanjeer (1973 Film) | False | [] | Prakash Mehra | [["d8s0"]] | context |
| u2 | birth date of {u1} | False | ["u1"] | 13 July 1939 | [["d1s0"]] | context |
| u3 | director of The Legend Of Lylah Clare | False | [] | Robert Aldrich | [["d6s0"]] | context |
| u4 | birth date of {u3} | False | ["u3"] | August 9, 1918 | [["d5s0"]] | context |
| u5 | which film's director was born first | True | ["u2", "u4"] | The Legend of Lylah Clare | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of Zanjeer (1973 film) | False | [] | Prakash Mehra | [['d8s0']] |
| u2 | date of birth of {u1} | False | ['u1'] | 13 July 1939 | [['d1s0']] |
| u3 | director of The Legend of Lylah Clare | False | [] | Robert Aldrich | [['d6s0']] |
| u4 | date of birth of {u3} | False | ['u3'] | August 9, 1918 | [['d5s0']] |
| u5 | which of Zanjeer (1973 film) and The Legend of Lylah Clare has the director born first | True | ['u2', 'u4'] | The Legend of Lylah Clare | [[]] |

### Source documents (reference only)

**d1: Prakash Mehra**

- [d1s0] Prakash Mehra( 13 July 1939 – 17 May 2009) was an Indian film director and producer known for his blockbuster Hindi films.
- [d1s1] He was one of the pioneers of masala films, along with Nasir Hussain, and Manmohan Desai.
- [d1s2] His collaborations with the actor Amitabh Bachchan resulted in several box office blockbusters and classics, due to which Mehra was considered among the' Golden Directors' of his time.

**d2: Henry Moore (cricketer)**

- [d2s0] Henry Walter Moore( 1849 – 20 August 1916) was an English- born first- class cricketer who spent most of his life in New Zealand.

**d3: The Legend of the Silver Fir**

- [d3s0] The Legend of the Silver Fir is a 1973 Czechoslovak film directed by František Vláčil.

**d4: Wale Adebanwi**

- [d4s0] Wale Adebanwi( born 1969) is a Nigerian- born first Black Rhodes Professor at St Antony's College, Oxford.

**d5: Robert Aldrich**

- [d5s0] Robert Burgess Aldrich( August 9, 1918 – December 5, 1983) was an American film director, producer, and screenwriter.
- [d5s1] His notable credits include" Vera Cruz"( 1954)," Kiss Me Deadly"( 1955)," The Big Knife"( 1955)," Autumn Leaves"( 1956)," Attack"( 1956)," What Ever Happened to Baby Jane?"( 1962)," Hush ... Hush, Sweet Charlotte"( 1964)," The Flight of the Phoenix"( 1965)," The Dirty Dozen"( 1967) and" The Longest Yard"( 1974).
- [d5s2] Aldrich was portrayed by Alfred Molina in the television miniseries" Feud"( 2017).

**d6: The Legend of Lylah Clare**

- [d6s0] The Legend of Lylah Clare is a 1968 American drama film released by Metro- Goldwyn- Mayer and directed by Robert Aldrich.
- [d6s1] The film stars Peter Finch, Kim Novak( in multiple roles), Ernest Borgnine, Michael Murphy, and Valentina Cortese.
- [d6s2] The film was based on a 1962" DuPont Show of the Week" TV drama co-written by" Wild in the Streets" creator Robert Thom.
- [d6s3] A satire on Hollywood, full of references to similar films, it recounts how an untalented beginner is hired to play the legendary Lylah Clare, a tempestuous actress who died mysteriously 20 years ago, and is herself consumed by the system.
- [d6s4] Although Aldrich's previous 1960s efforts were praised by critics," Lylah Clare" opened to negative reviews.

**d7: The Legend of Frank Woods**

- [d7s0] The Legend of Frank Woods is a 1977 western film.
- [d7s1] " The Legend of Frank Woods" is a re-edited version a 1972 film entitled" To Hell You Preach".

**d8: Zanjeer (1973 film)**

- [d8s0] Zanjeer is a 1973 Indian Hindi- language action film written by Salim- Javed( mostly by Salim Khan, with assistance from Javed Akhtar), directed and produced by Prakash Mehra, and starring Amitabh Bachchan, Jaya Bachchan, Pran, Ajit and Bindu.
- [d8s1] The film changed Hindi cinema's trend from romance films to action films, and pioneered Bachchan's new image of a brooding but explosive person who fights back when cornered, known as" The Angry Young Man."
- [d8s2] The film started a new wave in Bollywood.
- [d8s3] At a time when India was suffering from corruption and low economic growth, and the common man was left with frustration and anger over the system," Zanjeer" began shifting Hindi cinema in a violent and aggressive direction.
- [d8s4] Reflecting the anger of the masses, Amitabh Bachchan was seen as the new hero, who had the courage to fight against the wrongs while maintaining moral values at the same time.
- [d8s5] This film also ended the struggling period for Bachchan, and turned him into a rising star.
- [d8s6] The film was a blockbuster success, domestically in India and overseas in the Soviet Union.
- [d8s7] It was the first of many collaborations between screenwriter duo Salim- Javed and Amitabh Bachchan.
- [d8s8] Ever since" Zanjeer", Salim- Javed wrote many of their subsequent scripts with Bachchan in mind for the lead role, and insisted on him being cast for their later films, including blockbusters such as" Deewaar"( 1975) and" Sholay"( 1975), establishing Bachchan as a superstar.
- [d8s9] In addition to being a turning point for Bachchan's career and Hindi cinema," Zanjeer" was also a turning point for South Indian cinema, with Bachchan's acting inspiring future Tamil Superstar Rajinikanth.
- [d8s10] " Zanjeer" remains an important film in the history of Indian cinema and is regarded as a classic today.

**d9: The Legend of the Boy and the Eagle**

- [d9s0] The Legend of the Boy and the Eagle is a 1967 American live- action Walt Disney film.

**d10: The Legend of Ero of Armenteira**

- [d10s0] The legend of Saint Ero of Armenteira.
- [d10s1] The romanic monastery of Armenteira has always been related to the legend of its founder, the abbot Ero.

## 28. 2wikimultihopqa_ea8045620bdb11eba7f7acde48001122

原位置：`dev` 第 25 题 · 全局第 268 题 · `sample_id: 2wikimultihopqa_ea8045620bdb11eba7f7acde48001122`

Question: What nationality is the director of film Lorai: Play To Live?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | director of film Lorai: Play To Live | False | [] | Parambrata Chatterjee | [["d2s0"]] | context |
| u2 | nationality of {u1} | True | ["u1"] | Indian | [["d5s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | director of film Lorai: Play to Live | False | [] | Parambrata Chatterjee | [['d2s0']] |
| u2 | nationality of {u1} | True | ['u1'] | Indian | [['d5s0']] |

### Source documents (reference only)

**d1: Peter Levin**

- [d1s0] Peter Levin is an American director of film, television and theatre.

**d2: Lorai: Play to Live**

- [d2s0] Lorai: Play to Live is an Indian Bengali sports drama film directed by Parambrata Chatterjee, which stars Prosenjit Chatterjee, Payel Sarkar and Indrasish Roy in lead roles.
- [d2s1] The film is produced by Shyam Sunder Dey under the "Greentouch Entertainment".
- [d2s2] The film was released on 9 January 2015.

**d3: Brian Kennedy (gallery director)**

- [d3s0] Brian Patrick Kennedy( born 5 November 1961) is an Irish- born art museum director who has worked in Ireland and Australia, and now lives and works in the United States.
- [d3s1] He is currently the director of the Peabody Essex Museum.
- [d3s2] He was the director of the Toledo Museum of Art in Ohio from 2010 to 2019.
- [d3s3] He was the director of the Hood Museum of Art from 2005 to 2010, and the National Gallery of Australia( Canberra) from 1997- 2004.

**d4: John Farrell (businessman)**

- [d4s0] John Farrell is the director of YouTube in Latin America.

**d5: Parambrata Chatterjee**

- [d5s0] Parambrata Chattopadhyay (born 27 June 1980) is an Indian film actor, director, producer, and television personality.
- [d5s1] He has a significant following in West Bengal, India.
- [d5s2] Parambrata started his career with Bengali television and films.
- [d5s3] He made his Hindi debut in Kahaani (2012), starring along with Vidya Balan and Nawazuddin Siddiqui.
- [d5s4] He also acted in "Bhalo Theko" (2003), which is Vidya Balan's debut film.
- [d5s5] He has a very good knowledge of world music and has sung for few Bengali films like Chaya Manush and Samantaral.

**d6: Dana Blankstein**

- [d6s0] Dana Blankstein- Cohen( born March 3, 1981) is the director of the Israeli Academy of Film and Television.
- [d6s1] She is a film director, and an Israeli culture entrepreneur.

**d7: Ian Barry (director)**

- [d7s0] Ian Barry is an Australian director of film and TV.

**d8: Michael Govan**

- [d8s0] Michael Govan( born 1963) is the director of the Los Angeles County Museum of Art since 2006.
- [d8s1] Prior to this, Govan worked as the director of the Dia Art Foundation in New York City.

**d9: John Donatich**

- [d9s0] John Donatich is the Director of Yale University Press.

**d10: Olav Aaraas**

- [d10s0] Olav Aaraas( born 10 July 1950) is a Norwegian historian and museum director.
- [d10s1] He was born in Fredrikstad.
- [d10s2] From 1982 to 1993 he was the director of Sogn Folk Museum, from 1993 to 2010 he was the director of Maihaugen and from 2001 he has been the director of the Norwegian Museum of Cultural History.
- [d10s3] In 2010 he was decorated with the Royal Norwegian Order of St. Olav.

## 29. 2wikimultihopqa_f48d9c60093011ebbdaeac1f6bf848b6

原位置：`dev` 第 26 题 · 全局第 269 题 · `sample_id: 2wikimultihopqa_f48d9c60093011ebbdaeac1f6bf848b6`

Question: Which film was released first, Upasane or Emilio (Film)?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。 口径说明：新查询为年份，暂以 context 的影片年份 2008 标注；旧 2016 是美国院线上映年。结论仍是 Upasane，是正确的

Type: comparison · fallback: False · SFT snapshots: 7

### Adjusted units and annotation

**执行结果：** 按 Note 采用 context 的影片年份口径：1974 与 2008，结论 Upasane；2016 为美国院线上映年份，不作为 2008 的别名。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | release year of Upasane | False | [] | 1974 | [["d2s0"]] | context |
| u2 | release year of Emilio (Film) | False | [] | 2008 | [["d10s0"]] | context |
| u3 | which film was released first | True | ["u1", "u2"] | Upasane | [[]] | derived_from_dependencies |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | release date of Upasane | False | [] | 1974 | [['d2s0']] |
| u2 | U.S. theatrical release date of Emilio | False | [] | November 4, 2016 | [['d10s1']] |
| u3 | which of Upasane and Emilio was released first | True | ['u1', 'u2'] | Upasane | [[]] |

### Source documents (reference only)

**d1: Bommalattam (2008 film)**

- [d1s0] Bommalattam is a 2008 Indian Tamil film directed by Bharathiraja starring Arjun Sarja and Nana Patekar in the lead roles.
- [d1s1] Originally filmed in Hindi under the title" Cinema", the film was released first in Tamil.
- [d1s2] Hindi version retitled" Final Cut of Director" had a limited release in 2016.
- [d1s3] This marked Nana Patekar's Tamil film debut.

**d2: Upasane**

- [d2s0] Upasane( English: Worship) is a 1974 Kannada musical drama film, directed by Puttanna Kanagal.
- [d2s1] The film produced by Rashi brothers, is based on the novel of the same name, written by Devaki Murthy.
- [d2s2] The film mostly had women playing the lead roles, consisting of Aarathi, Leelavathi, M. N. Lakshmi Devi, G. V. Sharadha and Advani Lakshmi Devi. Dr. Govinda Mannur, K. S. Ashwath and Seetharam played the male supporting roles.
- [d2s3] Actor Seetharam was colloquially named as" Upasane" Seetharam for the rest of his career after the release of this film.
- [d2s4] The film dealt with the plight of Sharadha( Aarathi) who intends to pursue her career in classical music.
- [d2s5] The film went on to win multiple high- profile awards at the Karnataka State Film Awards for the year 1974- 75 including Best Film, Best Screenplay and Best Cinematography.
- [d2s6] Aarathi, who played the protagonist at the age of 19, won the Filmfare Best Actress award.

**d3: Lloyd (film)**

- [d3s0] Lloyd is a 2001 American comedy film.
- [d3s1] The film was released on May 4, 2001.

**d4: Single Video Theory**

- [d4s0] Single Video Theory is a music documentary directed by Mark Pellington that follows the making of "Yield", the fifth album by the American alternative rock band Pearl Jam.
- [d4s1] It was released first on VHS on August 4, 1998, and then on DVD on November 24, 1998.

**d5: Coney Island Baby (film)**

- [d5s0] Coney Island Baby is a 2003 comedy- drama in which film producer Amy Hobby made her directorial debut.
- [d5s1] Karl Geary wrote the film and Tanya Ryno was the film's producer.
- [d5s2] The music was composed by Ryan Shore.
- [d5s3] The film was shot in Sligo, Ireland, which is known locally as" Coney Island".
- [d5s4] The film was screened at the Newport International Film Festival.
- [d5s5] Hobby won the Jury Award for" Best First Time Director".
- [d5s6] The film made its premiere television broadcast on the Sundance Channel.

**d6: Empties**

- [d6s0] Empties is a 2007 film directed by Jan Svěrák and written by his father Zdeněk Svěrák, who also stars in the film.
- [d6s1] It was released first in the Czech Republic in March 2007.
- [d6s2] The film is a comedy from the same team which made Kolya.

**d7: Rakka (film)**

- [d7s0] The film was released on YouTube and Steam on 14 June 2017.

**d8: Invasion of the Neptune Men**

- [d8s0] The film was released in 1961 in Japan and was later released in the United States on television.
- [d8s1] In 1998, the film was featured on an episode of" Mystery Science Theater 3000".

**d9: The Wonderful World of Captain Kuhio**

- [d9s0] The film was released in Japan on 10 October 2009.

**d10: Emilio (film)**

- [d10s0] Emilio is a 2008 American drama film written and directed by Kim Jorgensen, starring Walter Perez, Danny Martinez, Alejandro Patino, Wendell Wright, Jesse Garcia, and Ryan McTavish.
- [d10s1] It was released theatrically in the U.S. on November 4, 2016.

## 30. 2wikimultihopqa_f5972e880baf11ebab90acde48001122

原位置：`dev` 第 27 题 · 全局第 270 题 · `sample_id: 2wikimultihopqa_f5972e880baf11ebab90acde48001122`

Question: Who is Erzsébet Thurzó's paternal grandfather?

Note: 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

Type: bridge · fallback: False · SFT snapshots: 8

### Adjusted units and annotation

**执行结果：** 保留新版单元；按语义对应旧答案，并核对 context 中的支持集合。

| ID | Description | Necessary | Depends on | Expected answer | Support sets | Support basis |
|---|---|---|---|---|---|---|
| u1 | father of Erzsébet Thurzó | False | [] | Imre Thurzó | [["d10s0"]] | context |
| u2 | father of {u1}, Erzsébet Thurzó's paternal grandfather | True | ["u1"] | György Thurzó | [["d8s0"]] | context |

### Original human gold (reference only)

| ID | Description | Necessary | Depends on | Expected answer | Support sets |
|---|---|---|---|---|---|
| u1 | father of Erzsébet Thurzó | False | [] | Imre Thurzó | [['d10s0']] |
| u2 | father of {u1}, Erzsébet Thurzó's paternal grandfather | True | ['u1'] | György Thurzó | [['d8s0']] |

### Source documents (reference only)

**d1: John Westley**

- [d1s0] Rev. John Westley( 1636 – 78) was an English nonconformist minister.
- [d1s1] He was the grandfather of John Wesley( founder of Methodism).

**d2: Kaya Alp**

- [d2s0] Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

**d3: Lyon Cohen**

- [d3s0] Lyon Cohen( 1868–1937) was a Polish- born Canadian businessman and a philanthropist.
- [d3s1] He was the grandfather of singer/ poet Leonard Cohen.

**d4: Fred Le Deux**

- [d4s0] Frederick" Fred" Le Deux( born 4 December 1934) was an Australian rules footballer who played with Geelong in the Victorian Football League( VFL).
- [d4s1] He is the grandfather of Tom Hawkins.

**d5: Miklós Szilágyi**

- [d5s0] Miklós Szilágyi de Alsó- Baksán et Nagy- Dobán( was born at the end of the 14th century), was a Hungarian nobleman, member of the House of Szilágyi, grandfather of Erzsébet Szilágyi and Michael Szilágyi, maternal great- grandfather of King Matthias of Hungary

**d6: Henry Krause**

- [d6s0] Henry J." Red" Krause, Jr.( August 28, 1913 – February 20, 1987) was an American football offensive lineman in the National Football League for the Brooklyn Dodgers and the Washington Redskins.
- [d6s1] He played college football at St. Louis University.
- [d6s2] He is the grandfather of Jennifer Krause
- [d6s3] He is the great grandfather of Payton Hoeing

**d7: Abd al-Muttalib**

- [d7s0] Abd al- Muttalib Shaybah ibn Hashim( c. 497 – 578) was the grandfather of Islamic prophet Muhammad.

**d8: Imre Thurzó**

- [d8s0] Count Imre Thurzó de Bethlenfalva (11 September 1598 – 19 October 1621) was a Hungarian aristocrat, son of Palatine György Thurzó, who served as Perpetual Ispán (Count; "comes") of Árva County between 1616 and 1621.
- [d8s1] Count Imre also functioned as Rector of the University of Wittenberg from 1616 to 1621.
- [d8s2] He was the last male member of the prestigious Thurzó family.

**d9: Gergely Szilágyi**

- [d9s0] Count Gergely Szilágyi( was born at the end of the 14th century), was a Hungarian nobleman, member of the House of Szilágyi, uncle of Erzsébet Szilágyi and Michael Szilágyi.

**d10: Erzsébet Thurzó**

- [d10s0] Countess Erzsébet Thurzó de Bethlenfalva (20 February 1621 – 4 July 1642) was a Hungarian noblewoman, daughter of Count Imre Thurzó and Baroness Krisztina Nyáry.
