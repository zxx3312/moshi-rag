# Revised Gold — batch 7

原始review保持不变。本文是依据原note生成的修订草稿；完整修改说明见[修改报告](../change_report.md)。

句子带有文档标题；允许使用标题解析该文档中的人名及代词。support_sets内为AND，组间为OR；presupposition_sets按现有评估器表示预设捷径。

## Q181 — `hotpotqa_5a81ff1a554299676cceb1c2` (revised draft)

> Oscar is what type of animal with black fur that may be a mixed or specific breed?

Source answer: black cat

Gold final answer: black cat

Question type: `single` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: animal type of Oscar | true | black cat | — | [d6s0] | — |

Evidence:

- `d6s0` Oscar (bionic cat) [0]: Oscar is an all black cat owned by Kate Allan and Mike Nolan who lives on the Channel Island of Jersey.

Notes:

- u1已给出完整答案，移除黑猫定义的重复桥接。

<details><summary>All source context</summary>

- `d1s0` Breed registry [0]: A breed registry, also known as a herdbook, studbook or register, in animal husbandry and the hobby of animal fancy, is an official list of animals within a specific breed whose parents are known.
- `d1s1` Breed registry [1]: Animals are usually registered by their breeders when they are still young.
- `d1s2` Breed registry [2]: The terms "studbook" and "register" are also used to refer to lists of male animals "standing at stud", that is, those animals actively breeding, as opposed to every known specimen of that breed.
- `d1s3` Breed registry [3]: Such registries usually issue certificates for each recorded animal, called a pedigree, pedigreed animal documentation, or most commonly, an animal's "papers".
- `d1s4` Breed registry [4]: Registration papers may consist of a simple certificate or a listing of ancestors in the animal's background, sometimes with a chart showing the lineage.
- `d2s0` Puppy nutrition [0]: The developmental life stage of dogs requires a specific intake of nutrients to ensure proper growth and development and to meet energy requirements.
- `d2s1` Puppy nutrition [1]: Despite the fact that puppies have different nutritional requirements compared to their adult counterparts, of the 652 breeders surveyed in the United States and Canada in 2012, 8.7% report feeding puppies commercial diets not intended for the developmental life stage of canines.
- `d2s2` Puppy nutrition [2]: Large and small dog breeds have even more specific nutrient requirements during growth, such as adjusted calcium to phosphorus ratio, and as such should receive a breed specific growth formula.
- `d2s3` Puppy nutrition [3]: Feeding diets formulated by a nutritionist for specific breed and life stage differences in nutrient requirements ensures a growing puppy will receive the proper nutrition associated with appropriate skeletal, neurological and immune development.
- `d2s4` Puppy nutrition [4]: This includes nutrients such as protein, fibre, essential fatty acids, calcium and vitamin E.
- `d2s5` Puppy nutrition [5]: It is therefore important to feed puppies a diet that meets the minimum and/or maximum requirements established by the National Research Council.
- `d3s0` Lonk [0]: The Lonk is a domestic sheep of a specific breed, found in the hills of the central and south Pennines, in the north of England.
- `d3s1` Lonk [1]: The name "Lonk" derives from the Lancashire word "lanky", meaning long and thin, usually in a person.
- `d3s2` Lonk [2]: Their range extends into only three counties; Lancashire, Yorkshire and Derbyshire.
- `d3s3` Lonk [3]: Also known as the Improved Haslingden, the Lonk is of the Blackfaced Mountain type, and is similar to the Derbyshire Gritstone, apart from the absence of horns in that breed.
- `d4s0` Carriage dog [0]: A carriage dog or coach dog refers to a type of dog rather than a specific breed.
- `d4s1` Carriage dog [1]: Dogs of this type were usually bred and trained to trot alongside carriages to protect the occupants from banditry or other interference.
- `d4s2` Carriage dog [2]: They were usually owned and used by the wealthy or traders and merchants.
- `d4s3` Carriage dog [3]: The dogs were trained to attack the horses used by highwaymen, giving the owners' human security time to respond to the actual robbers.
- `d5s0` Black cat [0]: A black cat is a domestic cat with black fur that may be a mixed or specific breed.
- `d5s1` Black cat [1]: The Cat Fanciers' Association (CFA) recognizes 22 cat breeds that can come with solid black coats.
- `d5s2` Black cat [2]: The Bombay breed is exclusively black.
- `d5s3` Black cat [3]: All-black fur pigmentation is slightly more prevalent in male cats than female cats.
- `d5s4` Black cat [4]: Their high melanin pigment content causes most black cats to have yellow (golden) eyes (irises).
- `d6s0` Oscar (bionic cat) [0]: Oscar is an all black cat owned by Kate Allan and Mike Nolan who lives on the Channel Island of Jersey.
- `d6s1` Oscar (bionic cat) [1]: In 2009 Oscar had both hind paws severed by a combine harvester.
- `d6s2` Oscar (bionic cat) [2]: Since then he has undergone a pioneering operation to add prosthetic feet.
- `d6s3` Oscar (bionic cat) [3]: The treatment has since been considered for use with humans.
- `d6s4` Oscar (bionic cat) [4]: A book about Oscar's story, "Oscar the Bionic Cat" was published in 2013.
- `d7s0` Nilgiri langur [0]: The Nilgiri langur ("Trachypithecus johnii") is a lutung (a type of Old World monkey) found in the Nilgiri Hills of the Western Ghats in South India.
- `d7s1` Nilgiri langur [1]: Its range also includes Kodagu in Karnataka, Kodayar Hills in Tamil Nadu, and many other hilly areas in Kerala and Tamil Nadu.
- `d7s2` Nilgiri langur [2]: This primate has glossy black fur on its body and golden brown fur on its head.
- `d7s3` Nilgiri langur [3]: It is similar in size and long-tailed like the gray langurs. Females have a white patch of fur on the inner thigh.
- `d7s4` Nilgiri langur [4]: It typically lives in troops of nine to ten monkeys.
- `d7s5` Nilgiri langur [5]: Its diet consists of fruits, shoots and leaves.
- `d7s6` Nilgiri langur [6]: The species is classified as vulnerable due to habitat destruction and poaching for its fur and flesh, the latter believed to have aphrodisiac properties.
- `d8s0` Karakul (hat) [0]: A karakul (or qaraqul) hat (Pashto/Persian: قراقلی) is a hat made from the fur of the Qaraqul breed of sheep, often from the fur of aborted lamb foetuses.
- `d8s1` Karakul (hat) [1]: The triangular hat is part of the costume of the native people of Kabul which has been worn by many generations of men in Afghanistan.
- `d8s2` Karakul (hat) [2]: The fur from which it is made is referred to as "Astrakhan", "broadtail", "qaraqulcha", or "Persian lamb".
- `d8s3` Karakul (hat) [3]: Qaraqul means black fur in Turkic, similar types of hats are common among Turkic peoples.
- `d8s4` Karakul (hat) [4]: The hat is peaked, and folds flat when taken off of the wearer's head.
- `d9s0` Breed club [0]: Breed clubs are associations or clubs with activities centered on a single, specific breed of a particular species of domesticated animal.
- `d9s1` Breed club [1]: The purpose of the association will vary with the species of animal and the goals and needs of the members of the association.
- `d9s2` Breed club [2]: Breed associations or clubs may vary in their goals, activities and nomenclature from country to country, even for the same breed.
- `d9s3` Breed club [3]: Most domesticated animals, whether they are agricultural animals such as cattle, llamas, poultry, sheep and pigs, or companion animals such as pigeons, horses, cats and dogs, have breed clubs associated with the breed.
- `d10s0` Kolpik [0]: A kolpik is a type of traditional headgear worn in families of some Chassidic "rebbes" (Hasidic rabbis), by unmarried children on Shabbat, and by some "rebbes" on some special occasions other than Shabbat or major holidays.
- `d10s1` Kolpik [1]: The kolpik is made from brown fur, as opposed to a "spodik", worn by Polish chassidic dynasties, which is fashioned out of black fur.

</details>

## Q182 — `hotpotqa_5a822a5e55429926c1cdae43` (revised draft)

> What occupations do Charles Burnett and Alan J. Pakula have in common?

Source answer: film director, film producer, writer

Gold final answer: film director, film producer, writer

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: occupations of Charles Burnett | false | film director, film producer, writer, editor, actor, photographer, cinematographer | — | [d1s0] | — |
| u2: occupations of Alan J. Pakula | false | film director, writer, producer | — | [d4s0] | — |
| u3: What occupations do Charles Burnett and Alan J. Pakula have in common? | true | film director, film producer, writer | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d1s0` Charles Burnett (director) [0]: Charles Burnett (born April 13, 1944, in Vicksburg, Mississippi) is an African-American film director, film producer, writer, editor, actor, photographer, and cinematographer.
- `d4s0` Alan J. Pakula [0]: Alan Jay Pakula ( ; April 7, 1928 – November 19, 1998) was an American film director, writer and producer.

Notes:

- Take the common roles. Producer is used in the film context of both defining sentences.
- 复核后保留原标注；原note为说明或未发现需要修改的证据/依赖问题。

<details><summary>All source context</summary>

- `d1s0` Charles Burnett (director) [0]: Charles Burnett (born April 13, 1944, in Vicksburg, Mississippi) is an African-American film director, film producer, writer, editor, actor, photographer, and cinematographer.
- `d1s1` Charles Burnett (director) [1]: His most popular films include "Killer of Sheep" (1978), "My Brother's Wedding" (1983), "To Sleep with Anger" (1990), "The Glass Shield" (1994), and "" (2007).
- `d1s2` Charles Burnett (director) [2]: He has been involved in other types of motion pictures including shorts, documentaries, and a TV series.
- `d2s0` Orphans (1987 film) [0]: Orphans is a 1987 American drama film directed by Alan J. Pakula.
- `d2s1` Orphans (1987 film) [1]: It was written by Lyle Kessler, based on his play of the same name.
- `d2s2` Orphans (1987 film) [2]: 
- `d3s0` The Pelican Brief (film) [0]: The Pelican Brief is a 1993 American legal political thriller based on the novel of the same name by John Grisham.
- `d3s1` The Pelican Brief (film) [1]: Directed by Alan J. Pakula, the film stars Julia Roberts in the role of young law student Darby Shaw and Denzel Washington as "Washington Herald" reporter Gray Grantham.
- `d3s2` The Pelican Brief (film) [2]: The film, which features music composed by James Horner, was the last film that featured Pakula as a writer or producer before his death.
- `d4s0` Alan J. Pakula [0]: Alan Jay Pakula ( ; April 7, 1928 – November 19, 1998) was an American film director, writer and producer.
- `d4s1` Alan J. Pakula [1]: He was nominated for three Academy Awards: Best Picture for "To Kill a Mockingbird" (1962), Best Director for "All the President's Men" (1976) and Best Adapted Screenplay for "Sophie's Choice" (1982).
- `d5s0` Presumed Innocent (film) [0]: Presumed Innocent is a 1990 American legal drama film based on the 1987 novel of the same name by Scott Turow.
- `d5s1` Presumed Innocent (film) [1]: Directed by Alan J. Pakula, and written by Pakula and Frank Pierson, it stars Harrison Ford, Brian Dennehy, Raúl Juliá, Bonnie Bedelia, Paul Winfield and Greta Scacchi.
- `d5s2` Presumed Innocent (film) [2]: "Presumed Innocent" follows Rusty Sabich (Ford), a prosecutor who is charged with the murder of his colleague and mistress Carolyn Polhemus (Scacchi).
- `d6s0` See You in the Morning (film) [0]: See You in the Morning is a 1989 American romantic comedy film written and directed by Alan J. Pakula, and starring Jeff Bridges, Alice Krige and Farrah Fawcett.
- `d6s1` See You in the Morning (film) [1]: It features music by Nat King Cole and Cherri Red.
- `d6s2` See You in the Morning (film) [2]: The film's music was composed by Michael Small.
- `d7s0` Love and Pain and the Whole Damn Thing [0]: Love and Pain and the Whole Damn Thing is a 1973 American comedy-drama film directed by Alan J. Pakula.
- `d7s1` Love and Pain and the Whole Damn Thing [1]: It is often categorized as a drama, but contains many comic elements.
- `d7s2` Love and Pain and the Whole Damn Thing [2]: Maggie Smith and Timothy Bottoms star.
- `d8s0` Robert Mulligan [0]: Robert Patrick Mulligan (August 23, 1925 – December 20, 2008) was an American film and television director best known as the director of humanistic American dramas, including "To Kill a Mockingbird" (1962), "Summer of '42" (1971), "The Other" (1972), "Same Time, Next Year" (1978) and "The Man in the Moon" (1991).
- `d8s1` Robert Mulligan [1]: He was also known in the 1960s for his extensive collaborations with producer Alan J. Pakula.
- `d8s2` Robert Mulligan [2]: He was the elder brother of actor Richard Mulligan.
- `d9s0` Klute [0]: Klute is a 1971 American neo-noir crime-thriller film directed and produced by Alan J. Pakula, written by Andy and Dave Lewis, and starring Jane Fonda, Donald Sutherland, Charles Cioffi, and Roy Scheider.
- `d9s1` Klute [1]: It tells the story of a high-priced prostitute who assists a detective in solving a missing person case.
- `d10s0` Comes a Horseman [0]: Comes a Horseman is a 1978 American western drama film starring Jane Fonda, James Caan, Jason Robards, and Richard Farnsworth, directed by Alan J. Pakula.

</details>

## Q183 — `hotpotqa_5a829fab55429954d2e2eb83` (revised draft)

> Between Joe Orton and Henry James, which author is the adjective "Ortonesque" used to refer to his work?

Source answer: John Kingsley "Joe" Orton

Gold final answer: John Kingsley "Joe" Orton

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: whether Ortonesque refers to the work of Joe Orton | false | yes | — | [d7s0, d7s1, d7s2, d7s3] | — |
| u2: Between Joe Orton and Henry James, which author is the adjective "Ortonesque" used to refer to his work? | true | John Kingsley "Joe" Orton (accepted alternatives: Joe Orton; John Kingsley Orton) **[by_presupposition]** | u1 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d7s0` Joe Orton [0]: John Kingsley "Joe" Orton (1 January 1933 – 9 August 1967) was an English playwright and author.
- `d7s1` Joe Orton [1]: His public career was short but prolific, lasting from 1964 until his death three years later.
- `d7s2` Joe Orton [2]: During this brief period he shocked, outraged, and amused audiences with his scandalous black comedies.
- `d7s3` Joe Orton [3]: The adjective "Ortonesque" is sometimes used to refer to work characterised by a similarly dark yet farcical cynicism.

Notes:

- 保留正向确认链路；补题干短名Joe Orton为答案别名，不从Henry James的职业介绍推断作品命名关系。

<details><summary>All source context</summary>

- `d1s0` The Henry James Review [0]: The Henry James Review is a triannual peer-reviewed academic journal established in 1979 and is the official publication of the Henry James Society.
- `d1s1` The Henry James Review [1]: It is dedicated to the scholarly, critical, and theoretical study of the American writer Henry James.
- `d1s2` The Henry James Review [2]: Each issue focuses on a specific theme of interest and seeks to promote understanding and study of James' contributions.
- `d1s3` The Henry James Review [3]: The journal is published by the Johns Hopkins University Press and the current editor-in-chief is Susan M. Griffin (University of Louisville).
- `d2s0` Prick Up Your Ears [0]: Prick Up Your Ears is a 1987 British film, directed by Stephen Frears, about the playwright Joe Orton and his lover Kenneth Halliwell.
- `d2s1` Prick Up Your Ears [1]: The screenplay was written by Alan Bennett, based on the biography by John Lahr.
- `d2s2` Prick Up Your Ears [2]: The film stars Gary Oldman as Orton, Alfred Molina as Halliwell, Wallace Shawn as Lahr and Vanessa Redgrave as Peggy Ramsay.
- `d3s0` Julie Rivkin [0]: Julie H. Rivkin (born 1952) is an American literary critic and professor of English at Connecticut College since 1982.
- `d3s1` Julie Rivkin [1]: She is best known for her publications on literary theory and Henry James, and has published several works on both subjects.
- `d3s2` Julie Rivkin [2]: Rivkin received her B.A. and PhD from Yale University and is currently the Associate Dean of Faculty at Connecticut College, a member of the Modern Language Association, and Vice President of the Henry James Society.
- `d3s3` Julie Rivkin [3]: Her other specializations include American literature and gender studies (publisher of the "Henry James Review").
- `d4s0` Henry James [0]: Henry James, OM ((1843--)15 1843 – (1916--)28 1916 ) was an American author regarded as a key transitional figure between literary realism and literary modernism, and is considered by many to be among the greatest novelists in the English language.
- `d4s1` Henry James [1]: He was the son of Henry James, Sr. and the brother of renowned philosopher and psychologist William James and diarist Alice James.
- `d5s0` The Ruffian on the Stair [0]: The Ruffian On the Stair is a play by British playwright Joe Orton which was first broadcast on BBC Radio in August 1964.
- `d5s1` The Ruffian on the Stair [1]: It is an unsympathetic yet comedic one-act portrayal of working class England, as played out by a couple and a mysterious young man who toys with their lives.
- `d5s2` The Ruffian on the Stair [2]: It was based on "The Boy Hairdresser", a novel by Orton and his lover Kenneth Halliwell.
- `d5s3` The Ruffian on the Stair [3]: The title and play are based on a few lines from poet and dramatist William Ernest Henley: "Madam Life's a piece in bloom, / Death goes dogging everywhere: / She's the tenant of the room, / He's the ruffian on the stair."
- `d5s4` The Ruffian on the Stair [4]: "Ruffian" is not as renowned as other works such as "Loot" and "What the Butler Saw", but it is still staged on occasion.
- `d6s0` Simon Bent [0]: Simon Bent is a British screenwriter and playwright, notable for work including BBC TV drama "" (2006), the screenplay for the feature film "Christie Malry's Own Double-Entry" (2000), and the Joe Orton biographical play "Prick Up Your Ears" based on John Lahr's book.
- `d7s0` Joe Orton [0]: John Kingsley "Joe" Orton (1 January 1933 – 9 August 1967) was an English playwright and author.
- `d7s1` Joe Orton [1]: His public career was short but prolific, lasting from 1964 until his death three years later.
- `d7s2` Joe Orton [2]: During this brief period he shocked, outraged, and amused audiences with his scandalous black comedies.
- `d7s3` Joe Orton [3]: The adjective "Ortonesque" is sometimes used to refer to work characterised by a similarly dark yet farcical cynicism.
- `d8s0` Plain Clothes Theatre Productions [0]: Plain Clothes Theatre Productions is a Bristol-based theatre company producing contemporary plays from around the globe.
- `d8s1` Plain Clothes Theatre Productions [1]: Formed in 2003 by artistic director Sam Berger, the company has produced work in London, Bristol, Cheltenham, Toronto and Vancouver.
- `d8s2` Plain Clothes Theatre Productions [2]: Their work has included plays by Joe Orton, Laura Wade and David Mamet, and their style is based around the teachings of American acting coach Sanford Meisner.
- `d9s0` What the Butler Saw (play) [0]: What the Butler Saw is a farce written by the English playwright Joe Orton.
- `d9s1` What the Butler Saw (play) [1]: It was premièred at the Queen's Theatre in London on 5 March 1969.
- `d9s2` What the Butler Saw (play) [2]: It was Orton's final play and the second to be performed after his death, following "Funeral Games" in 1968.
- `d10s0` Prick Up Your Ears (play) [0]: Prick Up Your Ears is a play by Simon Bent, based on the life of playwright Joe Orton.
- `d10s1` Prick Up Your Ears (play) [1]: Produced by Sonia Friedman it opened at the Comedy Theatre in London's West End on 30 September 2009 following previews from 17 September.
- `d10s2` Prick Up Your Ears (play) [2]: It starred Chris New as Joe Orton and Matt Lucas as Orton's lover and murderer, Kenneth Halliwell.

</details>

## Q184 — `hotpotqa_5a82efe355429966c78a6aa1` (revised draft)

> Polk County Florida's second most populated city is home to which mall?

Source answer: Winter Haven Mall

Gold final answer: Winter Haven Mall

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: second most populated city in Polk County in the stated 2015 estimates | false | Winter Haven | — | [d5s2] | — |
| u2: mall in {u1} | true | Winter Haven Mall | u1 | [d4s4] | — |

Evidence:

- `d4s4` Eagle Ridge Mall [4]: Sears relocated from an existing mall, Winter Haven Mall, in nearby Winter Haven.
- `d5s2` Winter Haven, Florida [2]: According to the U.S. Census Bureau's 2015 estimates, the city had a population of 37,689, making it the second most populated city in Polk County.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Belleville, Illinois [0]: Belleville (French: "Belle ville", meaning "Beautiful city") is a city in St. Clair County, Illinois, United States, coterminous with the now defunct Belleville Township.
- `d1s1` Belleville, Illinois [1]: The population was 42,034 according to the Census Bureau's 2015 estimates.
- `d1s2` Belleville, Illinois [2]: It is the eighth-most populated city outside the Chicago Metropolitan Area and the most populated city south of Springfield in the state of Illinois.
- `d1s3` Belleville, Illinois [3]: It is the county seat of St. Clair County, and the seat of the Roman Catholic Diocese of Belleville and the National Shrine of Our Lady of the Snows.
- `d1s4` Belleville, Illinois [4]: Belleville is the most populated city in the Metro-East region of the St. Louis Metropolitan Area and in Southern Illinois.
- `d1s5` Belleville, Illinois [5]: Due to its proximity to Scott Air Force Base, the population receives a boost from military and federal civilian personnel, defense contractors, and military retirees.
- `d2s0` Lakeland Square Mall [0]: Lakeland Square Mall is a shopping mall located on the northern side of Lakeland, Florida in the United States.
- `d2s1` Lakeland Square Mall [1]: It is one of two enclosed malls serving Polk County.
- `d2s2` Lakeland Square Mall [2]: It is owned and managed by Rouse Properties, one of the largest mall owners in the United States.
- `d2s3` Lakeland Square Mall [3]: It is the only shopping mall located off of I-4 between Tampa and Orlando, and it serves the populations of western Polk County.
- `d3s0` Lake Hancock [0]: Lake Hancock is a lake located north of Bartow, Florida in Polk County, Florida.
- `d3s1` Lake Hancock [1]: Lake Hancock is located in the Polk Upland area between the Winter Haven Ridge and Lakeland Ridge.
- `d3s2` Lake Hancock [2]: As part of the upper Peace River watershed, the lake has ecological importance throughout southwest Florida according to the Southwest Florida Water Management District.
- `d3s3` Lake Hancock [3]: Lake Hancock is shallow with an average depth of four feet and a maximum depth of 16 ft .
- `d3s4` Lake Hancock [4]: At 4573 acre , the lake is one of the largest lakes in Polk County, Florida; the center of the cities of Bartow, Lakeland, and Winter Haven roughly form an equilateral triangle with sides of 12 mi and Lake Hancock forms over 25% of that triangle.
- `d3s5` Lake Hancock [5]: The first settlements in the area occurred in 1849 when small farms were established in the area as a result of migration from a hurricane in the Tampa Bay area.
- `d4s0` Eagle Ridge Mall [0]: Eagle Ridge Mall is a regional, enclosed shopping mall located on the north side of Lake Wales, Florida.
- `d4s1` Eagle Ridge Mall [1]: This mall has two anchor stores: JCPenney and Dillard's.
- `d4s2` Eagle Ridge Mall [2]: It also has a Regal Cinemas, which has twelve theatres, and a large entertainment center, which contains a bowling alley, a large video arcade, a restaurant and meeting rooms.
- `d4s3` Eagle Ridge Mall [3]: On the north side of the mall is a large food court and a carousel.
- `d4s4` Eagle Ridge Mall [4]: Sears relocated from an existing mall, Winter Haven Mall, in nearby Winter Haven.
- `d5s0` Winter Haven, Florida [0]: Winter Haven is a city in Polk County, Florida, United States.
- `d5s1` Winter Haven, Florida [1]: The population was 33,874 at the 2010 census.
- `d5s2` Winter Haven, Florida [2]: According to the U.S. Census Bureau's 2015 estimates, the city had a population of 37,689, making it the second most populated city in Polk County.
- `d5s3` Winter Haven, Florida [3]: It is a principal city of the Lakeland-Winter Haven, Florida Metropolitan Statistical Area.
- `d6s0` Tenoroc High School [0]: Tenoroc High School (THS) is a public secondary school in Lakeland, Florida.
- `d6s1` Tenoroc High School [1]: The current principal is Jason Looney, and is assisted by four Assistant principals, Bradley Hardesty, Haley Mason, Summer Fisher and Brandi Blanchard.
- `d6s2` Tenoroc High School [2]: The School Board of Polk County established Tenoroc to relieve overcrowding problems at Lakeland High School, Lake Gibson High School, Auburndale High School, and Lake Region High School.
- `d6s3` Tenoroc High School [3]: It is also one of the more technologically advanced schools owned by the School Board of Polk County and hosts a specialized learning center known as "Power Academy."
- `d6s4` Tenoroc High School [4]: Power Academy is a 4-year training program for students intending to be employed at Lakeland Electric, Polk County's municipal utility company.
- `d7s0` April 1958 Florida tornado outbreak [0]: The April 1958 Florida tornado outbreak was a severe weather event that primarily affected the Florida peninsula on April 15, 1958.
- `d7s1` April 1958 Florida tornado outbreak [1]: A total of five tornadoes touched down in the state of Georgia between 12–5 p.m. EST.
- `d7s2` April 1958 Florida tornado outbreak [2]: 80 percent of the tornadoes were recorded in Florida, while 75 percent of the Florida events attained F3 intensity or greater.
- `d7s3` April 1958 Florida tornado outbreak [3]: The strongest tornado produced F4 damage on the Fujita scale in Polk County, Florida, becoming one of only two F4 tornadoes recorded in the U.S. state of Florida.
- `d7s4` April 1958 Florida tornado outbreak [4]: The second F4 tornado occurred on April 4, 1966, in Polk County near Gibsonia and Galloway.
- `d7s5` April 1958 Florida tornado outbreak [5]: In total, 65–72 people were injured during the 1958 outbreak, but no deaths were directly related to the tornadoes.
- `d7s6` April 1958 Florida tornado outbreak [6]: In addition to confirmed tornadoes, an unconfirmed tornado was also reported near Wimauma, Florida.
- `d8s0` Ridge Community High School [0]: Ridge Community High School or RCHS is a public high school located on the Davenport, Florida and Haines City, Florida Line.
- `d8s1` Ridge Community High School [1]: RCHS was established in 2005 in Polk County.
- `d8s2` Ridge Community High School [2]: It currently serves 2,600 students and has 106 teachers on campus.
- `d8s3` Ridge Community High School [3]: Ridge Community High School is one of many schools with a separate 9th Grade campus with its own front office.
- `d8s4` Ridge Community High School [4]: The main campus holds students in 10th, 11th, and 12th grade with some exceptions.
- `d8s5` Ridge Community High School [5]: Ridge Community High School sits on 76 acre of land.
- `d8s6` Ridge Community High School [6]: Ridge Community High School is zoned for Davenport and Haines City.
- `d8s7` Ridge Community High School [7]: Ridge Community High School's rivals include Haines City High School, Lake Wales High School and others in Polk County.
- `d8s8` Ridge Community High School [8]: The principal of RCHS is currently Russell Donnelly who replaced Sherry Wells, the acting principal between the school's opening in 2005 and 2015 and has a few assistant principals.
- `d8s9` Ridge Community High School [9]: Ridge Community High School is part of the Polk County School Board.
- `d8s10` Ridge Community High School [10]: RCHS's mascot is the Bolt, and the school motto is Once a Bolt, always a Bolt.
- `d9s0` Livingston, Texas [0]: Livingston is a city in and the county seat of Polk County, Texas, United States.
- `d9s1` Livingston, Texas [1]: With a population of 5,335 at the 2010 census, it is the largest city in Polk County.
- `d9s2` Livingston, Texas [2]: It is located approximately seventy-five miles north of Houston and was originally settled in 1835 as Springfield.
- `d9s3` Livingston, Texas [3]: Its name was changed to Livingston and became the county seat of Polk County in 1846.
- `d10s0` Lakeland, Florida [0]: Lakeland is a city in Polk County, Florida, located along Interstate 4 east of Tampa.
- `d10s1` Lakeland, Florida [1]: It is generally considered part of the Tampa Bay Area.
- `d10s2` Lakeland, Florida [2]: According to the 2013 U.S. Census Bureau estimate, the city had a population of 100,710.
- `d10s3` Lakeland, Florida [3]: Lakeland is a principal city of the Lakeland–Winter Haven Metropolitan Statistical Area (coterminous with Polk County), which had an estimated population of 623,009 in July 2013 based on data from the University of Florida Bureau of Economic and Business Research.
- `d10s4` Lakeland, Florida [4]: It is twinned with Richmond Hill, Ontario; Imabari, Ehime, Japan; Bălți, Moldova; Portmore, Jamaica; and Chongming County, Shanghai, China through the Lakeland chapter of Sister Cities International.

</details>

## Q185 — `hotpotqa_5a834ed95542990548d0b1ca` (revised draft)

> Which tower is taller, 712 Fifth Avenue or Manhattan Life Insurance Building?

Source answer: 712 5th Avenue

Gold final answer: 712 5th Avenue

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: height of 712 Fifth Avenue | false | 650 ft | — | [d8s0] | — |
| u2: height of Manhattan Life Insurance Building | false | 348 ft | — | [d5s0] | — |
| u3: Which tower is taller, 712 Fifth Avenue or Manhattan Life Insurance Building? | true | 712 5th Avenue | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d5s0` Manhattan Life Insurance Building [0]: The Manhattan Life Insurance Building was a 348 ft tower at 64-66 Broadway in New York City completed in 1894 to the designs of the architects of Kimball & Thompson and slightly extended north in 1904 making its new address 64-70 Broadway.
- `d8s0` 712 Fifth Avenue [0]: 712 5th Avenue is a 650 ft skyscraper at 56th Street and Fifth Avenue in the Midtown neighborhood of Manhattan, New York City.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Whole life insurance [0]: Whole life insurance, or whole of life assurance (in the Commonwealth of Nations), sometimes called "straight life" or "ordinary life," is a life insurance policy which is guaranteed to remain in force for the insured's entire lifetime, provided required premiums are paid, or to the maturity date.
- `d1s1` Whole life insurance [1]: As a life insurance policy it represents a contract between the insured and insurer that as long as the contract terms are met, the insurer will pay the death benefit of the policy to the policy's beneficiaries when the insured dies.
- `d1s2` Whole life insurance [2]: Because whole life policies are guaranteed to remain in force as long as the required premiums are paid, the premiums are typically much higher than those of term life insurance where the premium is fixed only for a limited term.
- `d1s3` Whole life insurance [3]: Whole life premiums are fixed, based on the age of issue, and usually do not increase with age.
- `d1s4` Whole life insurance [4]: The insured party normally pays premiums until death, except for limited pay policies which may be paid-up in 10 years, 20 years, or at age 65.
- `d1s5` Whole life insurance [5]: Whole life insurance belongs to the cash value category of life insurance, which also includes universal life, variable life, and endowment policies.
- `d2s0` Manhattan Life Insurance Company [0]: Manhattan Life Insurance Company, incorporated on May 29, 1850, is a life insurance company domiciled in New York but operates as a subsidiary of Manhattan Life Group in Houston, Texas.
- `d3s0` New York Life Building [0]: The New York Life Insurance Building, New York, located at 51 Madison Avenue, Manhattan, New York City, across from Madison Square Park, is the headquarters of the New York Life Insurance Company.
- `d4s0` Supreme Life Building [0]: The Supreme Life Building is a historic insurance building located at 3501 S. Dr. Martin Luther King Drive in the Douglas community area of Chicago, Illinois.
- `d4s1` Supreme Life Building [1]: Built in 1921, the building served as the headquarters of the Supreme Life Insurance Company, which was founded two years earlier.
- `d4s2` Supreme Life Building [2]: The company, originally known as the Liberty Life Insurance Company, was the first African-American owned insurance company in the northern United States.
- `d4s3` Supreme Life Building [3]: Since white-owned insurance firms regularly denied black customers life insurance when the firm was founded, the firm played an important role in providing life insurance to Chicago's African-American community.
- `d4s4` Supreme Life Building [4]: The company ultimately became the largest African-American owned business in the northern states and became a symbol of the predominantly black Bronzeville neighborhood's economic success from the 1920s to the 1950s.
- `d5s0` Manhattan Life Insurance Building [0]: The Manhattan Life Insurance Building was a 348 ft tower at 64-66 Broadway in New York City completed in 1894 to the designs of the architects of Kimball & Thompson and slightly extended north in 1904 making its new address 64-70 Broadway.
- `d5s1` Manhattan Life Insurance Building [1]: It was the first skyscraper to pass 100 m in Manhattan.
- `d6s0` New York Life Insurance Building (Montreal) [0]: Montreal's New York Life Insurance Building (also known as the Quebec Bank Building) is an office building at Place d'Armes in what is now known as Old Montreal, erected in 1887-1889.
- `d6s1` New York Life Insurance Building (Montreal) [1]: At the time of its completion, it was the tallest commercial building in Montreal with the first eight floors were designed for retail office space, that quickly filled with the city's best lawyers and financiers.
- `d6s2` New York Life Insurance Building (Montreal) [2]: When the clock tower was completed, the owner filled the ninth and tenth floors with the largest legal library in the entire country as a gift to tenants.
- `d6s3` New York Life Insurance Building (Montreal) [3]: The building is next to another historic office tower, Aldred Building.
- `d7s0` Francis H. Kimball [0]: Francis Hatch Kimball (1845–1919) was an American architect practicing in New York City, best known for his work on skyscrapers in lower Manhattan and terra-cotta ornamentation.
- `d7s1` Francis H. Kimball [1]: He was an associate with the firm Kimball & Thompson.
- `d7s2` Francis H. Kimball [2]: His work includes the Empire Building, Manhattan Life Insurance Building, and Casino Theatre (Broadway).
- `d7s3` Francis H. Kimball [3]: All but one of Kimball's work was in the United States.
- `d8s0` 712 Fifth Avenue [0]: 712 5th Avenue is a 650 ft skyscraper at 56th Street and Fifth Avenue in the Midtown neighborhood of Manhattan, New York City.
- `d8s1` 712 Fifth Avenue [1]: It was constructed from 1990 to 1991 and is the 53rd tallest building in New York City.
- `d8s2` 712 Fifth Avenue [2]: The tower's design had to accommodate the landmarked facades of the Coty and Rizzoli Buildings at the base of the tower.
- `d8s3` 712 Fifth Avenue [3]: It was purchased by the Bannister Trust in 2007 in a "Private Treaty", and placed in "Property Fund #1" managed by JP Morgan.
- `d8s4` 712 Fifth Avenue [4]: The building is sometimes referred to as the Henri Bendel building.
- `d9s0` Flatiron Building [0]: The Flatiron Building, originally the Fuller Building, is a triangular 22-story steel-framed landmarked building located at 175 Fifth Avenue in the borough of Manhattan, New York City, and is considered to be a groundbreaking skyscraper.
- `d9s1` Flatiron Building [1]: Upon completion in 1902, it was one of the tallest buildings in the city at 20 floors high and one of only two skyscrapers north of 14th Street – the other being the Metropolitan Life Insurance Company Tower, one block east.
- `d9s2` Flatiron Building [2]: The building sits on a triangular block formed by Fifth Avenue, Broadway, and East 22nd Street, with 23rd Street grazing the triangle's northern (uptown) peak.
- `d9s3` Flatiron Building [3]: As with numerous other wedge-shaped buildings, the name "Flatiron" derives from its resemblance to a cast-iron clothes iron.
- `d10s0` Physicians Mutual [0]: Physicians Mutual is a privately held insurance company headquartered in Omaha, Nebraska, United States, that consists of Physicians Mutual Insurance Company and Physicians Life Insurance Company.
- `d10s1` Physicians Mutual [1]: Founded as Physicians Mutual Insurance Company in 1902 by Edwin E. Elliott, Physicians Mutual began by selling health insurance to medical professionals.
- `d10s2` Physicians Mutual [2]: Policies were offered to the general public starting in 1962, and by 1970 the company expanded into life insurance when it founded Physicians Life Insurance Company.
- `d10s3` Physicians Mutual [3]: Today the company offers a variety of insurance products, annuities, Medicare, Medigap, Medicare Supplement, Term Life Insurance, Whole Life Insurance, Cancer and funeral pre-planning services.
- `d10s4` Physicians Mutual [4]: It holds over US$3 billion in assets and employs over one thousand people.
- `d10s5` Physicians Mutual [5]: Robert A. Reed is chief executive officer and president.

</details>

## Q186 — `hotpotqa_5a83a7e15542992ef85e2347` (revised draft)

> Who voices Homer Simpson's character on the animated television series? 

Source answer: Daniel Louis Castellaneta

Gold final answer: Dan Castellaneta

Question type: `single` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: actor who voices Homer Simpson | true | Dan Castellaneta (accepted alternatives: Daniel Louis Castellaneta) | — | [d3s1] OR [d5s1] OR [d4s1] | — |

Evidence:

- `d3s1` Homer Simpson [1]: He is voiced by Dan Castellaneta and first appeared on television, along with the rest of his family, in "The Tracey Ullman Show" short "Good Night" on April 19, 1987.
- `d4s1` Dan Castellaneta [1]: Noted for his long-running role as Homer Simpson on the animated television series "The Simpsons", he also voices many other characters for the show, including Abraham "Grampa" Simpson, Barney Gumble, Krusty the Clown, Sideshow Mel, Groundskeeper Willie, Mayor Quimby and Hans Moleman.
- `d5s1` Citizen Joe [1]: The episode features known voice actor Dan Castellaneta, who voices Homer Simpson in "The Simpsons".

Notes:

- 合并为single，移除全名转换；d3s0仅介绍角色，按标题可解析He时不单独要求该句；补d5s1、d4s1备选。

<details><summary>All source context</summary>

- `d1s0` Moe Szyslak [0]: Morris "Moe" Szyslak is a fictional character from the American animated television series "The Simpsons".
- `d1s1` Moe Szyslak [1]: He is voiced by Hank Azaria and first appeared in the series premiere episode "Simpsons Roasting on an Open Fire".
- `d1s2` Moe Szyslak [2]: Moe is the proprietor and bartender of Moe's Tavern, a Springfield bar frequented by Homer Simpson, Barney Gumble, Carl Carlson, Lenny Leonard, Sam, Larry, and others.
- `d2s0` Homer Simpson, This Is Your Wife [0]: "Homer Simpson, This Is Your Wife" is the fifteenth episode of the seventeenth season of the American animated television sitcom "The Simpsons".
- `d2s1` Homer Simpson, This Is Your Wife [1]: It originally aired on the Fox network in the United States on March 26, 2006, and was watched by around ten million people during that broadcast.
- `d2s2` Homer Simpson, This Is Your Wife [2]: In the episode, Homer signs the Simpson family up for a reality show in which the mothers of two families switch places.
- `d2s3` Homer Simpson, This Is Your Wife [3]: Marge gets to live with a friendly man named Charles and his perfect son, while Homer, Bart, and Lisa must spend time with Charles' strict wife Verity.
- `d3s0` Homer Simpson [0]: Homer Jay Simpson is a fictional character and the main protagonist of the American animated television series "The Simpsons" as the patriarch of the eponymous family.
- `d3s1` Homer Simpson [1]: He is voiced by Dan Castellaneta and first appeared on television, along with the rest of his family, in "The Tracey Ullman Show" short "Good Night" on April 19, 1987.
- `d3s2` Homer Simpson [2]: Homer was created and designed by cartoonist Matt Groening while he was waiting in the lobby of James L. Brooks' office.
- `d3s3` Homer Simpson [3]: Groening had been called to pitch a series of shorts based on his comic strip "Life in Hell" but instead decided to create a new set of characters.
- `d3s4` Homer Simpson [4]: He named the character after his father, Homer Groening.
- `d3s5` Homer Simpson [5]: After appearing for three seasons on "The Tracey Ullman Show", the Simpson family got their own series on Fox that debuted December 17, 1989.
- `d4s0` Dan Castellaneta [0]: Daniel Louis Castellaneta ( ; born October 29, 1957) is an American actor, voice actor, comedian and screenwriter.
- `d4s1` Dan Castellaneta [1]: Noted for his long-running role as Homer Simpson on the animated television series "The Simpsons", he also voices many other characters for the show, including Abraham "Grampa" Simpson, Barney Gumble, Krusty the Clown, Sideshow Mel, Groundskeeper Willie, Mayor Quimby and Hans Moleman.
- `d5s0` Citizen Joe [0]: "Citizen Joe" is the fifteenth episode for season eight of the Canadian-American military science fiction television series "Stargate SG-1".
- `d5s1` Citizen Joe [1]: The episode features known voice actor Dan Castellaneta, who voices Homer Simpson in "The Simpsons".
- `d5s2` Citizen Joe [2]: The episode was written by executive producer Robert C. Cooper, the episode was directed by Andy Mikita.
- `d5s3` Citizen Joe [3]: The episode received a below average Nielsen household rating and received no syndication rating to compare.
- `d5s4` Citizen Joe [4]: The episode got strong reviews from major media publishers worldwide.
- `d6s0` Ned Flanders [0]: Nedward "Ned" Flanders, Jr. is a recurring fictional character in the animated television series "The Simpsons".
- `d6s1` Ned Flanders [1]: He is voiced by Harry Shearer, and first appeared in the series premiere episode "Simpsons Roasting on an Open Fire".
- `d6s2` Ned Flanders [2]: He is the good-natured, cheery next-door neighbor to the Simpson family and is generally loathed by Homer Simpson.
- `d6s3` Ned Flanders [3]: A devout Evangelical Christian with an annoyingly perfect family, he is among the friendliest and most compassionate of Springfield's residents and is generally considered a pillar of the Springfield community.
- `d7s0` Homer to the Max [0]: "Homer to the Max" is the thirteenth episode of "The Simpsons"<nowiki>'</nowiki> tenth season.
- `d7s1` Homer to the Max [1]: It originally aired on the Fox network in the United States on February 7, 1999.
- `d7s2` Homer to the Max [2]: In the episode, Homer discovers that a new television show, "Police Cops", has a hero also named Homer Simpson.
- `d7s3` Homer to the Max [3]: He is delighted with the positive attention he receives because of his name, but when the television character is rewritten from a hero to a bumbling idiot, he is mocked and taunted, so he changes his name to "Max Power" to rid himself of the negative attention.
- `d7s4` Homer to the Max [4]: Max gains new friends, and is forced into a protest to prevent a forest from being knocked down.
- `d7s5` Homer to the Max [5]: In the end, he changes his name back to Homer Simpson.
- `d8s0` Grampa Simpson [0]: Abraham Jedediah Simpson II, often known as Grampa, is a fictional character in the animated television series "The Simpsons".
- `d8s1` Grampa Simpson [1]: He made his first appearance in the episode entitled "Grampa and the Kids", a Simpsons short on "The Tracey Ullman Show".
- `d8s2` Grampa Simpson [2]: Voiced by Dan Castellaneta, he is the father of Homer Simpson and the grandfather of Bart, Lisa and Maggie Simpson.
- `d8s3` Grampa Simpson [3]: In the 1000th issue of "Entertainment Weekly", Grampa was selected as the Grandpa for "The Perfect TV Family".
- `d9s0` Santa's Little Helper [0]: Santa's Little Helper is a recurring character in the American animated television series "The Simpsons".
- `d9s1` Santa's Little Helper [1]: He is the pet greyhound of the Simpson family.
- `d9s2` Santa's Little Helper [2]: The dog was introduced in the first episode of the show, the 1989 Christmas special "Simpsons Roasting on an Open Fire", in which his owner abandons him for finishing last in a greyhound race.
- `d9s3` Santa's Little Helper [3]: Homer Simpson and his son Bart, who are at the race track in hope of winning some money for Christmas presents, see this and decide to adopt the dog.
- `d10s0` Girly Edition [0]: "Girly Edition" is the twenty-first episode in the ninth season of the American animated television series "The Simpsons".
- `d10s1` Girly Edition [1]: It originally aired on the Fox network in the United States on April 19, 1998.
- `d10s2` Girly Edition [2]: In the episode, Lisa and Bart Simpson must co-anchor a new news program, though when Bart is seen as a more successful news anchor, Lisa becomes jealous and seeks revenge.
- `d10s3` Girly Edition [3]: Meanwhile, in the subplot, Homer Simpson gets a monkey helper because of his laziness.
- `d10s4` Girly Edition [4]: "Girly Edition" was the first episode written by Larry Doyle and was directed by Mark Kirkland.
- `d10s5` Girly Edition [5]: Much of the subplot was inspired by the film "Monkey Shines".
- `d10s6` Girly Edition [6]: Critics gave the episode positive reviews and it was well received by Lisa's voice actress Yeardley Smith.

</details>

## Q187 — `hotpotqa_5a83b4d35542996488c2e495` (revised draft)

> The Sophia Amalia was named after the wife of a king that ruled which two countries in 1648?

Source answer: Denmark and Norway

Gold final answer: Denmark and Norway

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: king whose wife gave the Sophia Amalia her name | false | Frederick III | — | [d7s0] | — |
| u2: countries ruled by {u1} starting in 1648 | true | Denmark and Norway | u1 | [d6s0] | — |

Evidence:

- `d6s0` Frederick III of Denmark [0]: Frederick III (Danish: "Frederik" ; 18 March 1609 – 9 February 1670) was king of Denmark and Norway from 1648 until his death in 1670.
- `d7s0` HDMS Sophia Amalia [0]: The Sophia Amalia was a ship of the Royal Dano-Norwegian Navy named after Sophia Amalia, the wife of King Frederick III.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Sophia Amalia Marschalk [0]: Sophia Amalia Marschalk, also called Anna Marschalk, was a Danish noble and courtier.
- `d1s1` Sophia Amalia Marschalk [1]: She was the favorite of the queen of Sweden, Ulrika Eleonora of Denmark.
- `d2s0` Saudi Arabia–United States relations [0]: Bilateral relations between the Kingdom of Saudi Arabia and the United States began in 1933 when full diplomatic relations were established.
- `d2s1` Saudi Arabia–United States relations [1]: Despite the differences between the two countries—an ultraconservative Islamic absolute monarchy, and a secular, democratic republic—the two countries have been allies.
- `d2s2` Saudi Arabia–United States relations [2]: In recent years, the two countries have occasionally been described as having a "Special Relationship" with one another.
- `d2s3` Saudi Arabia–United States relations [3]: Former Presidents George W. Bush and Barack Obama have close and strong relations with senior members of the Saudi Royal Family.
- `d3s0` Malawi–Mozambique relations [0]: Malawi–Mozambique relations refers to the current and historical relationship between the countries of Malawi and Mozambique.
- `d3s1` Malawi–Mozambique relations [1]: As Malawi shares a large border with Mozambique, much of the substance of their foreign relations pertain to the border separating the two nations.
- `d3s2` Malawi–Mozambique relations [2]: Both of the sovereign states have amicably agreed that lacustrine borders on Lake Malawi remain the largest priority between the two countries, as the exploitation of natural resources within the waters of Lake Malawi remain an issue the two countries continue to resolve.
- `d3s3` Malawi–Mozambique relations [3]: The moment considered an act of generosity and sympathy within the two countries relations is when, during the Mozambique Civil War, Malawi housed over one million Mozambican refugees between 1985 and 1995.
- `d3s4` Malawi–Mozambique relations [4]: After this gesture, Malawian relations with Mozambique crumbled under the tenure of Bingu wa Mutharika, notoriously reaching a nadir when Malawian police launched a raid into Mozambique's territory.
- `d4s0` Uruguay River pulp mill dispute [0]: The pulp mill dispute was a dispute between Argentina and Uruguay concerning the construction of pulp mills on the Uruguay River.
- `d4s1` Uruguay River pulp mill dispute [1]: The presidents at the time were Néstor Kirchner (Argentina) and Tabaré Vázquez (Uruguay).
- `d4s2` Uruguay River pulp mill dispute [2]: As a diplomatic, economic, and public relations conflict between both parties, the dispute has also affected tourism and transportation as well as the otherwise amicable relations between the two countries.
- `d4s3` Uruguay River pulp mill dispute [3]: The feud was unprecedented between the two countries, which have shared historical and cultural ties.
- `d4s4` Uruguay River pulp mill dispute [4]: Proceedings were brought before the International Court of Justice as a case formally named Pulp Mills on the River Uruguay "(Argentina v. Uruguay)".
- `d4s5` Uruguay River pulp mill dispute [5]: It ruled that, although Uruguay failed to inform Argentina of the operations, it did not pollute the river, so closing the pulp mill would be unjustified.
- `d4s6` Uruguay River pulp mill dispute [6]: The conflict ended in 2010, during the presidencies of Cristina Fernández de Kirchner (Argentina) and José Mujica (Uruguay), with the establishment of a joint coordination of the activities in the river.
- `d5s0` Reconquest of Angola [0]: The Reconquest of Angola (Portuguese: "Reconquista de Angola" ) (1641-1648) was Portugal's campaign to regain its colony in Angola from the Dutch.
- `d5s1` Reconquest of Angola [1]: In 1641 Johan Maurits sent an expedition under Admiral Cornelis Jol from Recife in Dutch Brazil to seize the Angolan capital of Luanda.
- `d5s2` Reconquest of Angola [2]: The Dutch were able to easily capture Luanda in August as the Portuguese forces were occupied inland in a campaign against the Kingdom of Kongo.
- `d5s3` Reconquest of Angola [3]: The two countries fought to a stalemate over Angola, until in 1648 the governor of Rio de Janeiro and Angola, Salvador de Sá, reached Luanda and finding the port defended by only 50 Dutch troops, regained it for Angola exactly seven years after its loss.
- `d6s0` Frederick III of Denmark [0]: Frederick III (Danish: "Frederik" ; 18 March 1609 – 9 February 1670) was king of Denmark and Norway from 1648 until his death in 1670.
- `d6s1` Frederick III of Denmark [1]: He also governed under the name Frederick II as diocesan administrator (colloquially referred to as prince-bishop) of the Prince-Bishopric of Verden (1623–29 and again 1634–44), and the Prince-Archbishopric of Bremen (1635–45).
- `d7s0` HDMS Sophia Amalia [0]: The Sophia Amalia was a ship of the Royal Dano-Norwegian Navy named after Sophia Amalia, the wife of King Frederick III.
- `d7s1` HDMS Sophia Amalia [1]: The ship was built at Hovedøen in Christiania under the direction of English shipbuilder James Robbins and was launched in 1650.
- `d7s2` HDMS Sophia Amalia [2]: She was 51.8 meters long and at that time one of the largest naval vessels in the world.
- `d7s3` HDMS Sophia Amalia [3]: She was commissioned by King Christian IV specifically to surpass the British ship  .
- `d7s4` HDMS Sophia Amalia [4]: The ship was manned by a crew of 680 and had an armament of 108 guns, surpassing "Sovereign of the Seas" by eight guns.
- `d8s0` James Robbins (shipbuilder) [0]: James Robbins, died 1680, was an English shipbuilder in Danish service who built Sophia Amalia and other ships for the Danish navy.
- `d9s0` Covered interest arbitrage [0]: Covered interest arbitrage is an arbitrage trading strategy whereby an investor capitalizes on the interest rate differential between two countries by using a forward contract to "cover" (eliminate exposure to) exchange rate risk.
- `d9s1` Covered interest arbitrage [1]: Using forward contracts enables arbitrageurs such as individual investors or banks to make use of the forward premium (or discount) to earn a riskless profit from discrepancies between two countries' interest rates.
- `d9s2` Covered interest arbitrage [2]: The opportunity to earn riskless profits arises from the reality that the interest rate parity condition does not constantly hold.
- `d9s3` Covered interest arbitrage [3]: When spot and forward exchange rate markets are not in a state of equilibrium, investors will no longer be indifferent among the available interest rates in two countries and will invest in whichever currency offers a higher rate of return.
- `d9s4` Covered interest arbitrage [4]: Economists have discovered various factors which affect the occurrence of deviations from covered interest rate parity and the fleeting nature of covered interest arbitrage opportunities, such as differing characteristics of assets, varying frequencies of time series data, and the transaction costs associated with arbitrage trading strategies.
- `d10s0` France–United Kingdom relations [0]: France–United Kingdom relations are the relations between the governments of the French Republic and the United Kingdom of Great Britain and Northern Ireland (UK).
- `d10s1` France–United Kingdom relations [1]: The historical ties between the two countries are long and complex, including conquest, wars, and alliances at various points in history.
- `d10s2` France–United Kingdom relations [2]: The Roman era saw both areas, except Scotland and Northern Ireland, conquered by Rome, whose fortifications exist in both countries to this day, and whose writing system introduced a common alphabet to both areas; however, the language barrier remained.
- `d10s3` France–United Kingdom relations [3]: The Norman conquest of England in 1066 decisively shaped English history, as well as the English language.
- `d10s4` France–United Kingdom relations [4]: In the medieval period, the countries were often bitter enemies, with both nations' monarchs claiming control over France.
- `d10s5` France–United Kingdom relations [5]: The Hundred Years' War stretched from 1337 to 1453 resulting in French victory.
- `d10s6` France–United Kingdom relations [6]: Britain and France fought a series of five major wars , culminating in the Coalition victory over Napoleon in 1815.
- `d10s7` France–United Kingdom relations [7]: After that there were some tensions, but peace generally prevailed and as the 19th century progressed, the relationship became better.
- `d10s8` France–United Kingdom relations [8]: Closer ties between the two began with the 1904 Entente cordiale, particularly via the alliances in World War I and World War II, wherein both countries fought against Germany, and in the latter conflict British armies helped to liberate occupied France from the Nazis.
- `d10s9` France–United Kingdom relations [9]: Both nations opposed the Soviet Union during the Cold War and were founding members of NATO.
- `d10s10` France–United Kingdom relations [10]: In recent years the two countries have experienced a quite close relationship, especially on defence and foreign policy issues; the two countries tend, however, to disagree on a range of other matters, most notably the European Union.
- `d10s11` France–United Kingdom relations [11]: The British press relishes the chance to refer to France and Britain as "historic rivals" or emphasize the perceived ever-lasting competition that still opposes the two countries.

</details>

## Q188 — `hotpotqa_5a83c2e25542996488c2e4bc` (revised draft)

> The 2014 Baylor Bears football games were played at the stadium whose name was changed during what month?

Source answer: December 2013

Gold final answer: December 2013

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: stadium used by the 2014 Baylor Bears football team | false | McLane Stadium | — | [d3s2] | — |
| u2: month and year when {u1} received that name | true | December 2013 | u1 | [d4s2] | — |

Evidence:

- `d3s2` 2014 Baylor Bears football team [2]: Playing their 116th football season, this was the team's first in the new McLane Stadium in Waco, Texas.
- `d4s2` McLane Stadium [2]: Originally named "Baylor Stadium", the name was changed to McLane Stadium in December 2013 to honor alumnus and business magnate Drayton McLane, Jr., who provided the lead gift for the stadium construction.

Notes:

- 删除题干没有的新体育场限定new，其余链路由d3s2和d4s2明确支持。

<details><summary>All source context</summary>

- `d1s0` Carroll Field [0]: Carroll Field was owned by Baylor University; the Baylor Bears football program played games there from 1906 to 1925, and from 1930 to 1935.
- `d1s1` Carroll Field [1]: Following the construction of the Carroll Science Building in 1902, the field was located between the building and Waco Creek; the field took over as the location of football games from an unnamed field adjacent to and northwest of Old Main.
- `d1s2` Carroll Field [2]: From 1926 to 1929, Baylor football games were played at the Cotton Palace in Waco.
- `d2s0` 2014 Baylor Bears baseball team [0]: The 2014 Baylor Bears baseball team represents Baylor University in the 2014 college baseball season.
- `d2s1` 2014 Baylor Bears baseball team [1]: Baylor competes in Division I of the National Collegiate Athletic Association (NCAA) as a charter member of the Big 12 Conference.
- `d2s2` 2014 Baylor Bears baseball team [2]: The Bears play home games at Baylor Ballpark on the university's campus in Waco, Texas.
- `d2s3` 2014 Baylor Bears baseball team [3]: Twenty year head coach Steve Smith leads the Bears, a former pitcher for the team during the 1982 and 1983 seasons.
- `d3s0` 2014 Baylor Bears football team [0]: The 2014 Baylor Bears football team represented Baylor University in the 2014 NCAA Division I FBS football season.
- `d3s1` 2014 Baylor Bears football team [1]: The Bears were coached by Art Briles.
- `d3s2` 2014 Baylor Bears football team [2]: Playing their 116th football season, this was the team's first in the new McLane Stadium in Waco, Texas.
- `d3s3` 2014 Baylor Bears football team [3]: The Bears were members of the Big 12 Conference.
- `d3s4` 2014 Baylor Bears football team [4]: They finished the season 11–2, 8–1 in Big 12 play to win a share of the Big 12 title with TCU.
- `d3s5` 2014 Baylor Bears football team [5]: They were invited to the Cotton Bowl Classic where they lost to Michigan State.
- `d4s0` McLane Stadium [0]: McLane Stadium is an American football stadium in Waco, Texas.
- `d4s1` McLane Stadium [1]: It is owned and operated by Baylor University.
- `d4s2` McLane Stadium [2]: Originally named "Baylor Stadium", the name was changed to McLane Stadium in December 2013 to honor alumnus and business magnate Drayton McLane, Jr., who provided the lead gift for the stadium construction.
- `d4s3` McLane Stadium [3]: Baylor's first game at McLane was played August 31, 2014, with the Bears defeating SMU 45–0.
- `d4s4` McLane Stadium [4]: The stadium has a capacity of 45,140 spectators and is expandable to 55,000.
- `d4s5` McLane Stadium [5]: McLane Stadium replaced Floyd Casey Stadium as the home field for the Baylor Bears football program.
- `d5s0` 1972 Baylor Bears football team [0]: The 1972 Baylor Bears football team represented the Baylor University in the 1972 college football season.
- `d5s1` 1972 Baylor Bears football team [1]: Grant Teaff was hired to resurrect the moribund football team at Baylor.
- `d5s2` 1972 Baylor Bears football team [2]: Baylor originally hired Rudy Feldman from New Mexico, but Feldman quit after one day, leaving the job to Teaff.
- `d5s3` 1972 Baylor Bears football team [3]: Baylor had been 7–43–1 in the five seasons preceding Teaff's arrival.
- `d5s4` 1972 Baylor Bears football team [4]: The Bears offense scored 180 points, while the Bears defense allowed 156 points.
- `d5s5` 1972 Baylor Bears football team [5]: In the Battle of the Brazos, the Bears beat Texas A&M by a score of 15–13.
- `d6s0` Baylor Bears football statistical leaders [0]: The Baylor Bears football statistical leaders are individual statistical leaders of the Baylor Bears football program in various categories, including passing, rushing, receiving, total offense, defensive stats, and kicking.
- `d6s1` Baylor Bears football statistical leaders [1]: Within those areas, the lists identify single-game, single-season, and career leaders.
- `d6s2` Baylor Bears football statistical leaders [2]: The Bears represent the Baylor University in the NCAA's Big 12 Conference.
- `d7s0` 1961 Baylor Bears football team [0]: The 1961 Baylor Bears football team represented Baylor University during the 1961 college football season.
- `d7s1` 1961 Baylor Bears football team [1]: The Bears were led by third-year head coach John Bridgers and played their home games at Baylor Stadium in Waco, Texas.
- `d7s2` 1961 Baylor Bears football team [2]: They competed as members of the Southwest Conference, finishing in sixth with a regular season record of 5–5 (2–5 SWC).
- `d7s3` 1961 Baylor Bears football team [3]: Baylor was invited to the first Gotham Bowl, where they beat the previously-undefeated Utah State Aggies, 24–9.
- `d8s0` 1899 Baylor football team [0]: The 1899 Baylor Bears football team represented Baylor University in the 1899 college football season.
- `d8s1` 1899 Baylor football team [1]: This was the first football season for Baylor.
- `d8s2` 1899 Baylor football team [2]: They all four games at home games in Waco, Texas.
- `d8s3` 1899 Baylor football team [3]: They were coached by head coach R. H. Hamilton.
- `d8s4` 1899 Baylor football team [4]: Initially, Baylor played its home games on an undetermined field near the university.
- `d8s5` 1899 Baylor football team [5]: Baylor played its first game against Texas A&M, which would become a rivalry, the Battle of the Brazos, with over 100 games played in the series by 2003.
- `d9s0` 1988 Baylor Bears football team [0]: The 1988 Baylor Bears football team represented the Baylor University in the 1988 NCAA Division I-A football season.
- `d9s1` 1988 Baylor Bears football team [1]: The Bears finished the season fourth in the Southwest Conference.
- `d9s2` 1988 Baylor Bears football team [2]: Baylor Stadium's name was officially changed to Floyd Casey Stadium during halftime of the homecoming game against Arkansas on November 5.
- `d10s0` List of Baylor Bears head football coaches [0]: The Baylor Bears football program is a college football team that represents Baylor University in the Big 12 Conference in the National Collegiate Athletic Association.
- `d10s1` List of Baylor Bears head football coaches [1]: The team has had 25 head coaches since it started playing organized football in 1899.
- `d10s2` List of Baylor Bears head football coaches [2]: Baylor was a charter member of the Southwest Conference (SWC), joining in 1915.
- `d10s3` List of Baylor Bears head football coaches [3]: They later became a charter member of the Big 12 in 1996 when the SWC disbanded.
- `d10s4` List of Baylor Bears head football coaches [4]: After playing without a nickname for 15 years, the school chose "Bears" as the team nickname in 1914.
- `d10s5` List of Baylor Bears head football coaches [5]: There were three seasons where Baylor did not field a team.
- `d10s6` List of Baylor Bears head football coaches [6]: In 1906, the university banned football due to the violent nature of the sport.
- `d10s7` List of Baylor Bears head football coaches [7]: However, student protests persuaded school officials to reinstate it the next year.
- `d10s8` List of Baylor Bears head football coaches [8]: In 1943 and 1944, the school cancelled the football program due to World War II.
- `d10s9` List of Baylor Bears head football coaches [9]: The Bears have played in 1,099 games during their 108 seasons.
- `d10s10` List of Baylor Bears head football coaches [10]: In those seasons, seven coaches have led Baylor to postseason bowl games: Bob Woodruff, George Sauer, Sam Boyd, John D. Bridgers, Grant Teaff, Chuck Reedy, and Art Briles.
- `d10s11` List of Baylor Bears head football coaches [11]: Five coaches have won conference championships with the Bears: Charles P. Mosley, Frank Bridges, Teaff, Reedy and Briles.

</details>

## Q189 — `hotpotqa_5a77bd595542995d83181291` (revised draft)

> Between two tennis players Kim Clijsters and Mary Pierce, who is older?

Source answer: Mary Pierce

Gold final answer: Mary Pierce

Question type: `comparison` (source type `comparison`)

Replaces: `hotpotqa_5a83f07455429933447460be`

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: birth year of Kim Clijsters | false | 1983 | — | [d8s0] | — |
| u2: birth year of Mary Pierce | false | 1975 | — | [d9s0] | — |
| u3: Between two tennis players Kim Clijsters and Mary Pierce, who is older? | true | Mary Pierce | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d8s0` Kim Clijsters [0]: Kim Antonie Lode Clijsters (] ; born 8 June 1983) is a Belgian former professional tennis player.
- `d9s0` Mary Pierce [0]: Mary Pierce (born 15 January 1975) is a French retired tennis professional who played on the Women's Tennis Association (WTA) tour.

Notes:

- 替换：美国到非欧洲需要额外地理映射，当前guide明确不允许。 新题保留原source type，人工核对两条显式事实及答案。

<details><summary>All source context</summary>

- `d1s0` Clijsters–Henin rivalry [0]: Justine Henin and Kim Clijsters are Belgian professional tennis players who engaged in a long-standing rivalry which spanned twenty-five meetings over a twelve-year period, with eight taking place in a Grand Slam tournament.
- `d1s1` Clijsters–Henin rivalry [1]: Their final competitive meeting came at the 2010 Wimbledon Championships in the fourth round, with Clijsters winning in 3 sets, this brought their head to head record to 13–12 in Clijsters' favour.
- `d1s2` Clijsters–Henin rivalry [2]: The Belgians have met eight times in Grand Slam tournaments, three of which were finals.
- `d1s3` Clijsters–Henin rivalry [3]: Henin leads 5–3 in Grand Slam play including winning all their final match-ups.
- `d2s0` 2003 WTA Tour Championships [0]: The 2003 WTA Tour Championships, also known by its sponsored name Bank of America WTA Tour Championships Presented by Porsche, was a women's tennis tournament played on indoor hard courts at the Staples Center in Los Angeles, United States.
- `d2s1` 2003 WTA Tour Championships [1]: It was the 33rd edition of the year-end singles championships, the 28th edition of the year-end doubles championships, and was part of the 2003 WTA Tour.
- `d2s2` 2003 WTA Tour Championships [2]: The tournament was held between November 4 and November 10, 2003.
- `d2s3` 2003 WTA Tour Championships [3]: First-seeded Kim Clijsters won the singles event and earned $1,000,030 first-prize money as well as 485 ranking points.
- `d2s4` 2003 WTA Tour Championships [4]: With her victory Clijsters became the first female tennis player to earn $US4 million in a season.
- `d2s5` 2003 WTA Tour Championships [5]: For the first time since 1978 a round robin system was used, after the men's Tennis Masters Cup.
- `d2s6` 2003 WTA Tour Championships [6]: Two groups of four players were formed and each contender had to play three matches.
- `d2s7` 2003 WTA Tour Championships [7]: Also, for singles, instead of the top sixteen players qualifying, only top eight qualified for the WTA Tour Championships.
- `d2s8` 2003 WTA Tour Championships [8]: For doubles, the top four pairs (previously top eight) pairs qualified for the WTA Tour Championships, but still continued with the single elimination format.
- `d3s0` 1999 French Open – Girls' Doubles [0]: Kim Clijsters and Jelena Dokić were the defending champions, but only Clijsters competed with year with Mia Buric
- `d4s0` 2016 French Open – Women's Legends Doubles [0]: Kim Clijsters and Martina Navratilova were the defending champions, but decided not to compete together this year.
- `d4s1` 2016 French Open – Women's Legends Doubles [1]: Clijsters played alongside Tracy Austin-Holt, but they were eliminated at the round-robin stage.
- `d5s0` 2010 Billie Jean King Cup [0]: The 2010 Billie Jean King Cup was the 2nd edition of this tennis exhibition tournament.
- `d5s1` 2010 Billie Jean King Cup [1]: Seven-time Grand Slam champion Venus Williams, 2009 French Open Champion Svetlana Kuznetsova, and 2009 US Open Champion Kim Clijsters participated.
- `d5s2` 2010 Billie Jean King Cup [2]: 2009 Australian Open and Wimbledon Champion Serena Williams had to withdraw from the event due to a leg injury.
- `d5s3` 2010 Billie Jean King Cup [3]: She was replaced by 2008 French Open Champion Ana Ivanovic.
- `d5s4` 2010 Billie Jean King Cup [4]: In the first semifinal, Clijsters defeated Ivanovic in a tiebreaker (7–2), despite Ivanovic having match point at 5–4 up.
- `d5s5` 2010 Billie Jean King Cup [5]: Williams defeated Kuznetsova in the second semifinal, 6–4.
- `d5s6` 2010 Billie Jean King Cup [6]: Williams defeated Clijsters in the championship match by a score of 6–4 3–6 7–5.
- `d6s0` Eva Dyrberg [0]: Eva Dyrberg (born 17 February 1980) is a Danish former tennis player.
- `d6s1` Eva Dyrberg [1]: As a junior player, she won 1998 Wimbledon Championships with Jelena Kostanić and 1998 US Open with Kim Clijsters.
- `d6s2` Eva Dyrberg [2]: In 1998, Dyrberg was also ranked World No. 1 in junior doubles and was named ITF Junior Girls Doubles World Champion.
- `d6s3` Eva Dyrberg [3]: During her professional career, she won four singles and five doubles events organized by the International Tennis Federation, defeating players such as Magdalena Maleeva, Tathiana Garbin, Maria Elena Camerin, Nicole Pratt, and reaching one doubles final at WTA Tour, at Sanex Trophy in 2000.
- `d6s4` Eva Dyrberg [4]: She retired from professional tennis after the 2003 Australian Open.
- `d7s0` 2004 Wimbledon Championships – Women's Doubles [0]: Kim Clijsters and Ai Sugiyama were the defending champions.
- `d7s1` 2004 Wimbledon Championships – Women's Doubles [1]: however Clijsters did not compete in the tournament this year.
- `d7s2` 2004 Wimbledon Championships – Women's Doubles [2]: Sugiyama played alongside Liezel Huber and they reached the final where they were defeated by Cara Black and Rennae Stubbs, 6–3, 7–6.
- `d8s0` Kim Clijsters [0]: Kim Antonie Lode Clijsters (] ; born 8 June 1983) is a Belgian former professional tennis player.
- `d8s1` Kim Clijsters [1]: Clijsters is a former world No. 1 in both singles and doubles.
- `d9s0` Mary Pierce [0]: Mary Pierce (born 15 January 1975) is a French retired tennis professional who played on the Women's Tennis Association (WTA) tour.
- `d9s1` Mary Pierce [1]: Born in Canada, she is a citizen of Canada, and the United States.
- `d9s2` Mary Pierce [2]: Pierce played for France in team competitions and in the Olympics.
- `d10s0` 2004 French Open – Women's Doubles [0]: Kim Clijsters and Ai Sugiyama were the defending champions, but Clijsters was chose not to participate.
- `d10s1` 2004 French Open – Women's Doubles [1]: Sugiyama played alongside Liezel Huber, but they lost in the first round to Shinobu Asagoe and Rika Fujiwara in the first round.

</details>

## Q190 — `hotpotqa_5a769ac95542993569682c4f` (revised draft)

> Who was born first, Odysseas Elytis or Cornel West?

Source answer: Odysseas Elytis

Gold final answer: Odysseas Elytis

Question type: `comparison` (source type `comparison`)

Replaces: `hotpotqa_5a840e8a5542992ef85e239e`

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: birth year of Odysseas Elytis | false | 1911 | — | [d6s0] | — |
| u2: birth year of Cornel West | false | 1953 | — | [d1s0] | — |
| u3: Who was born first, Odysseas Elytis or Cornel West? | true | Odysseas Elytis | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d1s0` Cornel West [0]: Cornel Ronald West (born June 2, 1953) is an American philosopher, political activist, social critic, author, public intellectual, and prominent member of the Democratic Socialists of America.
- `d6s0` Odysseas Elytis [0]: Odysseas Elytis (Greek: Οδυσσέας Ελύτης , ] , pen name of Odysseas Alepoudellis, Greek: Οδυσσέας Αλεπουδέλλης ; 2 November 1911 – 18 March 1996) was regarded as a major exponent of romantic modernism in Greece and the world.

Notes:

- 替换：Hole的两个创办者不是完整阵容；未找到可比较的成员总数。 新题保留原source type，人工核对两条显式事实及答案。

<details><summary>All source context</summary>

- `d1s0` Cornel West [0]: Cornel Ronald West (born June 2, 1953) is an American philosopher, political activist, social critic, author, public intellectual, and prominent member of the Democratic Socialists of America.
- `d1s1` Cornel West [1]: West is an outspoken voice in American leftist politics, and as such has been critical of many center-left figures, including President Barack Obama and former Secretary of State and 2016 Democratic Presidential nominee Hillary Clinton.
- `d1s2` Cornel West [2]: He has held professorships at Harvard University, Princeton University, Yale University, Union Theological Seminary, and the University of Paris during his career.
- `d1s3` Cornel West [3]: He is also a frequent commentator on politics and social issues in many media outlets.
- `d2s0` David Connolly (translator) [0]: David John Connolly (born 1954) is an English-born Greek literary translator.
- `d2s1` David Connolly (translator) [1]: He has translated poetry and novels from Greek to English, including writing by Nikiforos Vrettakos, Odysseas Elytis, Kiki Dimoula and Nikos Engonopoulos.
- `d3s0` David Carrasco [0]: Davíd Lee Carrasco (born November 21, 1944) is a Mexican-American academic historian of religion, anthropologist, and Mesoamericanist scholar.
- `d3s1` David Carrasco [1]: As of 2001 he holds the inaugural appointment as Neil L. Rudenstine Professor of Latin America Studies at the Harvard Divinity School, in a joint appointment with the Faculty of Arts and Sciences' Department of Anthropology at Harvard University.
- `d3s2` David Carrasco [2]: Carrasco previously taught at the University of Colorado, Boulder and Princeton University and is known for his research and extensive publications on Mesoamerican religion and history, his public speaking as well as wider contributions within Latin American studies and Latino/a studies.
- `d3s3` David Carrasco [3]: He has made powerful critical statements about Latino contributions to US democracy in public dialogues with Cornel West, Toni Morrison, and Samuel P. Huntington.
- `d3s4` David Carrasco [4]: His work is known primarily for his illuminating writings on the ways human societies orient themselves with sacred places.
- `d4s0` Race Matters [0]: Race Matters is a social sciences book by Cornel West.
- `d4s1` Race Matters [1]: The book was first published on April 1, 1993 by Beacon Press.
- `d4s2` Race Matters [2]: The book analyzes moral authority and racial debates concerning skin color in the United States.
- `d4s3` Race Matters [3]: The book questions matters of economics and politics, as well as ethical issues and spirituality, and also addresses the crisis in black leadership.
- `d4s4` Race Matters [4]: West's collection of moral essays on race relations in America was on the "New York Times" best-seller lists for many weeks.
- `d4s5` Race Matters [5]: The profound book continues to be as important today as it was 25 years ago.
- `d4s6` Race Matters [6]: Beacon Press will publish a 25th Anniversary edition on December 5, 2017.
- `d5s0` Tragoudia Gia Tous Mines [0]: Tragoudia Gia Tous Mines (Songs For The Months; Greek: Τραγούδια Για Τους Μήνες ) is an album by popular Greek artist Eleftheria Arvanitaki and it was released in 1996.
- `d5s1` Tragoudia Gia Tous Mines [1]: It was written and arranged by Dimitris Papadimitriou and the lyrics are poems by Sappho, Maria Polydouri, Kostas Karyotakis, Odysseas Elytis and Michalis Ganas, as well as traditional couplets.
- `d5s2` Tragoudia Gia Tous Mines [2]: It sold over 60,000 copies in Greece and was certified Platinum.
- `d5s3` Tragoudia Gia Tous Mines [3]: The vinyl collector's edition release of the album was in the form of a small record player.
- `d5s4` Tragoudia Gia Tous Mines [4]: The CD album's package and the disk itself featured extensive artwork following mostly a theme on the sky and the constellations.
- `d6s0` Odysseas Elytis [0]: Odysseas Elytis (Greek: Οδυσσέας Ελύτης , ] , pen name of Odysseas Alepoudellis, Greek: Οδυσσέας Αλεπουδέλλης ; 2 November 1911 – 18 March 1996) was regarded as a major exponent of romantic modernism in Greece and the world.
- `d6s1` Odysseas Elytis [1]: In 1979 he was awarded the Nobel Prize in Literature.
- `d7s0` Tavis Smiley [0]: Tavis Smiley ( ; born September 13, 1964) is an American talk show host and author.
- `d7s1` Tavis Smiley [1]: Smiley was born in Gulfport, Mississippi, and grew up in Bunker Hill, Indiana.
- `d7s2` Tavis Smiley [2]: After attending Indiana University, he worked during the late 1980s as an aide to Tom Bradley, the mayor of Los Angeles.
- `d7s3` Tavis Smiley [3]: Smiley became a radio commentator in 1991 and, starting in 1996, he hosted the talk show "BET Talk" (later renamed "BET Tonight") on Black Entertainment Television (BET).
- `d7s4` Tavis Smiley [4]: After Smiley sold an exclusive interview of Sara Jane Olson to ABC News in 2001, BET declined to renew his contract that year.
- `d7s5` Tavis Smiley [5]: Smiley then began hosting "The Tavis Smiley Show" on National Public Radio (NPR) (2002–04) and currently hosts "Tavis Smiley" on the Public Broadcasting Service (PBS) on weekdays and "The Tavis Smiley Show" on Public Radio International (PRI).
- `d7s6` Tavis Smiley [6]: From 2010 to 2013, Smiley and Cornel West joined forces to host their own radio talk show, "Smiley & West".
- `d7s7` Tavis Smiley [7]: They were featured together interviewing musician Bill Withers in the 2009 documentary film "Still Bill".
- `d7s8` Tavis Smiley [8]: He is the new host of "Tavis Talks" on BlogTalkRadio's Tavis Smiley Network.
- `d8s0` Kyriakos Charalambides [0]: Kyriakos Charalambides (Greek: Κυριάκος Χαραλαμπίδης , Kyriacos Charalambides) is one of the most renowned and celebrated living Cypriot poets.
- `d8s1` Kyriakos Charalambides [1]: His poetry, essays, translations, and critical analysis celebrate the ideas of Western civilisation, expressed through the language and history of Greek culture.
- `d8s2` Kyriakos Charalambides [2]: His poetic opus adds to the tradition established by such modern Greek poets as Constantine P. Cavafy, Giorgos Seferis and Odysseas Elytis.
- `d8s3` Kyriakos Charalambides [3]: His poetry though holds steadfastly to the Greek Cypriot linguistic register.
- `d9s0` Mytilene International Airport [0]: Mytilene International Airport "Odysseas Elytis" (IATA: MJT, ICAO: LGMT) is the international airport of Mytilene, the capital of the Greek island Lesbos.
- `d10s0` Mourning in America and Dreaming in Color [0]: Mourning in America and Dreaming in Color is the fifth studio album by American rapper Brother Ali.
- `d10s1` Mourning in America and Dreaming in Color [1]: It was released via Rhymesayers Entertainment on September 18, 2012.
- `d10s2` Mourning in America and Dreaming in Color [2]: Entirely produced by Jake One, it includes a guest appearance from Dr. Cornel West.
- `d10s3` Mourning in America and Dreaming in Color [3]: It reached number 44 on the "Billboard" 200 chart.
- `d10s4` Mourning in America and Dreaming in Color [4]: It sold 10,000 copies in its first week of release.

</details>

## Q191 — `hotpotqa_5a843f305542996488c2e51d` (revised draft)

> When will Flicker, created by a member of One Direction, be released?

Source answer: October 20, 2017

Gold final answer: October 20, 2017

Question type: `single` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: scheduled release date of Flicker in the source | true | October 20, 2017 | — | [d3s1] | — |

Evidence:

- `d3s1` Flicker (album) [1]: It is scheduled for release on October 20, 2017, through Neon Haze Music and Capitol Records. "

Notes:

- Flicker已在题干中，删除演员/歌手桥接；保留来源当时的计划发行日期。

<details><summary>All source context</summary>

- `d1s0` One Direction: This Is Us [0]: One Direction: This Is Us is a 2013 British-American 3-D documentary concert film centering on British-Irish group One Direction.
- `d1s1` One Direction: This Is Us [1]: It opened in the United Kingdom on 29 August 2013, followed a day later in the United States.
- `d1s2` One Direction: This Is Us [2]: The movie shows many clips and songs of One Direction.
- `d2s0` Niall Horan [0]: Niall James Horan (born 13 September 1993) is an Irish singer and songwriter.
- `d2s1` Niall Horan [1]: He is best known as a member of the boy band One Direction.
- `d2s2` Niall Horan [2]: In 2010, Horan auditioned as a solo artist for British televised singing competition "The X Factor".
- `d2s3` Niall Horan [3]: After being eliminated as a solo performer, Horan joined four other contestants to form One Direction.
- `d2s4` Niall Horan [4]: The band has released five commercially successful albums, performed on four worldwide tours, and won a number of awards.
- `d3s0` Flicker (album) [0]: Flicker is the upcoming debut studio album by Irish singer and songwriter Niall Horan.
- `d3s1` Flicker (album) [1]: It is scheduled for release on October 20, 2017, through Neon Haze Music and Capitol Records. "
- `d3s2` Flicker (album) [2]: This Town" was released on 29 September 2016, as the album's lead single, followed by 2017 singles "Slow Hands" and "Too Much to Ask".
- `d4s0` One Direction: Where We Are – The Concert Film [0]: One Direction: Where We Are – The Concert Film, also known as One Direction: Where We Are - Live from San Siro Stadium is the second concert film by English-Irish boy band One Direction and the sequel to "".
- `d4s1` One Direction: Where We Are – The Concert Film [1]: The film takes place during the 28 and 29 June 2014 shows of the band's Where We Are Tour at San Siro Stadium in Milan, Italy.
- `d4s2` One Direction: Where We Are – The Concert Film [2]: It contains a 15-minute interview with the band with exclusive behind-the-scenes footage.
- `d5s0` Only One Direction [0]: Only One Direction is an international production and theatre show about English-Irish boyband One Direction.
- `d5s1` Only One Direction [1]: The band has performed to hundreds of thousands worldwide.
- `d5s2` Only One Direction [2]: In October 2015, Only One Direction - The One Direction Story opened in London's West End.
- `d6s0` Liam Payne [0]: Liam James Payne (born 29 August 1993) is an English singer and songwriter.
- `d6s1` Liam Payne [1]: He rose to fame as a member of the boy band One Direction.
- `d6s2` Liam Payne [2]: Payne made his debut as a singer when he auditioned for the British television series "The X Factor" in 2008.
- `d6s3` Liam Payne [3]: After being eliminated as a solo performer, he auditioned again in 2010 and was put into a group with four other contestants to form One Direction.
- `d6s4` Liam Payne [4]: One Direction has released five commercially successful albums, performed on four worldwide tours, and won multiple awards.
- `d7s0` Midnight Memories [0]: " Midnight Memories" is the third studio album by British-Irish boy band One Direction, released on 25 November 2013 by Columbia Records, Syco Music and Sony Music.
- `d7s1` Midnight Memories [1]: The album was described as having a "slightly rockier tone" than their previous efforts.
- `d7s2` Midnight Memories [2]: It has become the fastest-selling album in Amazon UK's history, breaking the record set by One Direction's previous release, "Take Me Home" (2012).
- `d7s3` Midnight Memories [3]: The album debuted at number one on the US "Billboard" 200, making One Direction the first group in history to debut at number one in the US with their first three albums.
- `d7s4` Midnight Memories [4]: The album was preceded by the release of the singles "Best Song Ever" and "Story of My Life".
- `d8s0` Take Me Home (One Direction album) [0]: Take Me Home is the second studio album by British-Irish group One Direction, released on 9 November 2012 by Syco Music and Columbia Records.
- `d8s1` Take Me Home (One Direction album) [1]: As a follow-up to One Direction's internationally successful debut album "Up All Night" (2011), "Take Me Home" was written in groups and has an average of just under five songwriters per track.
- `d8s2` Take Me Home (One Direction album) [2]: Largely recorded and composed in Sweden during 2012, Savan Kotecha, Rami Yacoub and Carl Falk, who composed One Direction's hits, "What Makes You Beautiful" and "One Thing", spent six months in Stockholm developing songs for the album, and were able to shape melodies around the members' tones.
- `d9s0` Louis Tomlinson [0]: Louis William Tomlinson (born Louis Troy Austin; 24 December 1991) is an English singer and songwriter.
- `d9s1` Louis Tomlinson [1]: He is known as a member of the boy band One Direction.
- `d9s2` Louis Tomlinson [2]: Tomlinson began his career as an actor, appearing in ITV drama film "If I Had You" and the BBC drama "Waterloo Road".
- `d9s3` Louis Tomlinson [3]: In 2010, he became a member of One Direction after being eliminated as a solo artist on the British music competition series "The X Factor".
- `d9s4` Louis Tomlinson [4]: Tomlinson is one of the main songwriters of One Direction's repertoire.
- `d9s5` Louis Tomlinson [5]: Following the band's hiatus, Tomlinson released the singles "Just Hold On" and "Back to You".
- `d9s6` Louis Tomlinson [6]: The latter will be included in his debut studio album, which will be released in 2017 by Epic Records.
- `d10s0` Up All Night (One Direction album) [0]: Up All Night is the debut studio album by English-Irish group One Direction, released by Syco Records in November 2011 in Ireland and the United Kingdom, followed by a worldwide release during 2012.
- `d10s1` Up All Night (One Direction album) [1]: Four months after finishing third in the seventh series of British reality singing contest "The X Factor" in December 2010, One Direction began recording the album in Sweden, UK and the United States, working with a variety of writers and producers.
- `d10s2` Up All Night (One Direction album) [2]: The album is predominantly a pop music album which orientates into pop rock, dance-pop, teen pop and power pop.
- `d10s3` Up All Night (One Direction album) [3]: The album's lyrical content regards being young, relationships, heartbreak and empowerment.
- `d10s4` Up All Night (One Direction album) [4]: Staged in support of the album, One Direction performed the album's songs live on televised shows, at awards ceremonies, and during their worldwide Up All Night Tour.

</details>

## Q192 — `hotpotqa_5a84de255542991dd0999e06` (revised draft)

> Who has more pen names explicitly listed in the context, George Orwell or Nelson DeMille?

Source answer: Nelson Richard DeMille

Gold final answer: Nelson Richard DeMille

Question type: `comparison` (source type `comparison`)

Original question: Who had more pen names, George Orwell or Nelson DeMille?

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: pen names explicitly listed for George Orwell | false | 1 | — | [d8s0] | — |
| u2: pen names explicitly listed for Nelson DeMille | false | 4 | — | [d10s2] | — |
| u3: Who has more pen names explicitly listed in the context, George Orwell or Nelson DeMille? | true | Nelson Richard DeMille (accepted alternatives: Nelson DeMille) | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d8s0` George Orwell [0]: Eric Arthur Blair (25 June 1903 – 21 January 1950), better known by his pen name George Orwell, was an English novelist, essayist, journalist, and critic.
- `d10s2` Nelson DeMille [2]: DeMille has also written under the pen names Jack Cannon, Kurt Ladner, Ellen Kay and Brad Matthews.

Notes:

- 题干澄清：限定为文档列举的笔名数量，不断言终身总数。
- 继续比较1与4，新增题干短名Nelson DeMille。

<details><summary>All source context</summary>

- `d1s0` George Orwell: A Life in Pictures [0]: George Orwell: A Life in Pictures is a 2003 BBC Television docudrama telling the life story of the British author George Orwell.
- `d1s1` George Orwell: A Life in Pictures [1]: Chris Langham plays the part of Orwell.
- `d1s2` George Orwell: A Life in Pictures [2]: No surviving sound recordings or video of the real George Orwell have been found.
- `d2s0` The Lion (2010 novel) [0]: The Lion is a 2010 novel by American author Nelson DeMille.
- `d2s1` The Lion (2010 novel) [1]: It is the fifth of DeMille's novels to feature Detective John Corey, now working as a contractor for the fictional FBI Anti-Terrorist Task Force in New York City.
- `d2s2` The Lion (2010 novel) [2]: The novel is the sequel to "Wild Fire".
- `d2s3` The Lion (2010 novel) [3]: The Lion is followed by DeMille’s 2012 novel, "The Panther".
- `d3s0` Lionel Snell [0]: Ramsey Dukes is the current and most well-known pen name of Lionel Snell, a contemporary English magician, publisher and author on magic and philosophy.
- `d3s1` Lionel Snell [1]: He has also under the pen names Lemuel Johnston.
- `d3s2` Lionel Snell [2]: Angerford and Lea, Adamai Philotunus and Per Anum Ad Astra.
- `d3s3` Lionel Snell [3]: His regular satirical column "The Satanist's Diary" was published in the magazine "Aquarian Arrow" during the 1980s and early 1990s under the pen name The Hon Hugo C StJ l'Estrange and included a multitude of other pen names as contributors.
- `d4s0` Wandering Stars [0]: Wandering Stars is an anthology of Jewish fantasy and science fiction, edited by American writer Jack Dann, originally published by Harper & Row in 1974.
- `d4s1` Wandering Stars [1]: It represented, according to the book cover, "the first time in science fiction that the Jew - and the richness of his themes and particular points of view -- will appear without a mask."
- `d4s2` Wandering Stars [2]: In his introduction, "Why Me?"
- `d4s3` Wandering Stars [3]: , Isaac Asimov discussed how many Jewish science fiction writers prior to that time had used gentile pen names in order to get published: "Many of the Jewish pulp writers, however, used pen names as a matter of sound business.
- `d4s4` Wandering Stars [4]: A story entitled "War Gods of the Oyster-Men of Deneb" did not carry conviction if it was written by someone named Chaim Itzkowitz."
- `d4s5` Wandering Stars [5]: He then goes on to discuss the pen names of various Jewish writers included in this book.
- `d4s6` Wandering Stars [6]: "Wandering Stars" is therefore of historical significance as the first science fiction anthology where Jewish writers openly identified themselves as such.
- `d4s7` Wandering Stars [7]: It was followed by a second anthology, "More Wandering Stars", also edited by Jack Dann, published by Doubleday in 1981.
- `d5s0` The Lion's Game [0]: The Lion's Game is a 2000 novel by American author Nelson DeMille.
- `d5s1` The Lion's Game [1]: It is the second of DeMille's novels to feature the detective John Corey, now working as a contractor for the fictional FBI Anti-Terrorist Task Force in New York City.
- `d5s2` The Lion's Game [2]: The 2000 novel The Lion’s Game is the sequel to Plum Island and is followed by the 2004 book Night Fall.
- `d5s3` The Lion's Game [3]: The book also briefly mentions events from other DeMille novels like "The Charm School" and "The Gold Coast", that aren't strictly part of the Corey-universe.
- `d6s0` Wild Fire (novel) [0]: Wild Fire is a 2006 novel by American author, Nelson DeMille.
- `d6s1` Wild Fire (novel) [1]: It is the fourth of DeMille's novels to feature Detective John Corey, now working as a contractor for the fictional FBI Anti-Terrorist Task Force in New York City.
- `d6s2` Wild Fire (novel) [2]: The novel is the sequel to Night Fall and takes place approximately one year later.
- `d6s3` Wild Fire (novel) [3]: Wild Fire is followed by DeMille’s 2010 novel, The Lion.
- `d7s0` George Orwell bibliography [0]: The bibliography of George Orwell includes journalism, essays, novels and non-fiction books written by the British writer Eric Blair (1903–50), either under his own name or, more usually, under his pen name George Orwell.
- `d7s1` George Orwell bibliography [1]: Orwell was a prolific writer on topics related to contemporary English society and literary criticism, whom the British newsweekly "The Economist" in 2008 declared "perhaps the 20th century's best chronicler of English culture."
- `d7s2` George Orwell bibliography [2]: His non-fiction cultural and political criticism constitutes the majority of his work, but Orwell also wrote in several genres of fictional literature.
- `d8s0` George Orwell [0]: Eric Arthur Blair (25 June 1903 – 21 January 1950), better known by his pen name George Orwell, was an English novelist, essayist, journalist, and critic.
- `d8s1` George Orwell [1]: His work is marked by lucid prose, awareness of social injustice, opposition to totalitarianism, and outspoken support of democratic socialism.
- `d9s0` The Panther (novel) [0]: The Panther is a 2012 novel by American author Nelson DeMille.
- `d9s1` The Panther (novel) [1]: It is the sixth of DeMille's novels to feature Detective John Corey, now working as a contractor for the fictional FBI Anti-Terrorist Task Force in New York City.
- `d9s2` The Panther (novel) [2]: The novel is the sequel to "The Lion".
- `d9s3` The Panther (novel) [3]: The Panther is followed by DeMille’s 2015 novel, "Radiant Angel".
- `d9s4` The Panther (novel) [4]: Also featured in this novel is DeMille’s other fictional character, Paul Brenner, who appears in The General's Daughter and Up Country.
- `d10s0` Nelson DeMille [0]: Nelson Richard DeMille (born August 23, 1943) is an American author of action adventure and suspense novels.
- `d10s1` Nelson DeMille [1]: His novels include "Plum Island", "The Charm School", and "The Gold Coast".
- `d10s2` Nelson DeMille [2]: DeMille has also written under the pen names Jack Cannon, Kurt Ladner, Ellen Kay and Brad Matthews.

</details>

## Q193 — `hotpotqa_5a8549c65542997b5ce3ffe6` (revised draft)

> Are both Barry Unsworth and P. G. Wodehouse from the same country?

Source answer: yes

Gold final answer: yes

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: country of origin stated for Barry Unsworth | false | England | — | [d3s0] | — |
| u2: country descriptor of P. G. Wodehouse | false | England | — | [d1s0] | — |
| u3: Are both Barry Unsworth and P. G. Wodehouse from the same country? | true | yes | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d1s0` P. G. Wodehouse [0]: Sir Pelham Grenville Wodehouse {'1': ", '2': ", '3': ", '4': "} ( ; 15 October 188114 February 1975) was an English author and one of the most widely read humorists of the 20th century.
- `d3s0` Barry Unsworth [0]: Unsworth was born on 10 August 1930 in Wingate, a mining village in County Durham, England, to a family of miners.

Notes:

- English is normalized to England for the question about where the authors are from. Do not turn birthplace into a separate citizenship claim.
- 保留。English→England是国别形容词归一化；题干问from而非公民身份，出生地与国别描述可用于本题。

<details><summary>All source context</summary>

- `d1s0` P. G. Wodehouse [0]: Sir Pelham Grenville Wodehouse {'1': ", '2': ", '3': ", '4': "} ( ; 15 October 188114 February 1975) was an English author and one of the most widely read humorists of the 20th century.
- `d1s1` P. G. Wodehouse [1]: Born in Guildford, the son of a British magistrate based in Hong Kong, Wodehouse spent happy teenage years at Dulwich College, to which he remained devoted all his life.
- `d1s2` P. G. Wodehouse [2]: After leaving school he was employed by a bank but disliked the work and turned to writing in his spare time.
- `d1s3` P. G. Wodehouse [3]: His early novels were mostly school stories, but he later switched to comic fiction, creating several regular characters who became familiar to the public over the years.
- `d1s4` P. G. Wodehouse [4]: They include the jolly gentleman of leisure Bertie Wooster and his sagacious valet, Jeeves; the immaculate and loquacious Psmith; Lord Emsworth and the Blandings Castle set; the Oldest Member, with stories about golf; and Mr Mulliner, with tall tales on subjects ranging from bibulous bishops to megalomaniac movie moguls.
- `d2s0` The Greeks Have a Word For It [0]: The Greeks Have a Word For It is the second novel by Booker Prize-winning author Barry Unsworth published by Hutchinson in 1967.
- `d2s1` The Greeks Have a Word For It [1]: It has since been republished by Weidenfeld & Nicolson in 1993 and W. W. Norton & Company in 2002.
- `d2s2` The Greeks Have a Word For It [2]: It has been praised for its 'utterly convincing characterizations'.
- `d3s0` Barry Unsworth [0]: Unsworth was born on 10 August 1930 in Wingate, a mining village in County Durham, England, to a family of miners.
- `d3s1` Barry Unsworth [1]: His father first entered the mines at age 12 and ordinarily Unsworth would have followed him as a miner.
- `d3s2` Barry Unsworth [2]: However, when his father was 19, he travelled to the United States for a few years and on returning to Britain entered the insurance business and thus began moving his family up the economic ladder and out of the mines.
- `d3s3` Barry Unsworth [3]: "He rescued my brother and me from that long chain of continuity that happens in mining villages," Unsworth said.
- `d4s0` Pascali's Island (novel) [0]: Pascali's Island is a novel by Barry Unsworth, first published in 1980.
- `d4s1` Pascali's Island (novel) [1]: The first United States publication of the book by Simon & Schuster was titled The Idol Hunter.
- `d5s0` Sacred Hunger [0]: Sacred Hunger is a historical novel by Barry Unsworth first published in 1992.
- `d5s1` Sacred Hunger [1]: It shared the Booker Prize that year with Michael Ondaatje's "The English Patient".
- `d6s0` Losing Nelson [0]: Losing Nelson is a 1999 novel by Barry Unsworth.
- `d6s1` Losing Nelson [1]: Its protagonist is Charles Cleasby, who is obsessed with Lord Nelson, attempts to re-enact events of "Horatio"'s life to the point of feeling that he is the admiral, and who is writing a hagiographic biography.
- `d6s2` Losing Nelson [2]: His typist, the down-to-earth Miss Lily, serves as his foil in her criticism of Nelson's ego and treatment of his wife.
- `d6s3` Losing Nelson [3]: At the end, when Cleasby has journeyed to Naples to do research in the hope of exonerating his hero for his execution of Admiral Caracciolo and other Neapolitan Jacobins, he murders a child near the location of Nelson's betrayal, simultaneously imagining that he is killing the child Nelson and that the act forever merges him with Nelson.
- `d7s0` The Ruby in her Navel [0]: The Ruby in Her navel is a historical novel by Barry Unsworth first published in 2006.
- `d7s1` The Ruby in her Navel [1]: It was long listed for the Booker Prize that year.
- `d8s0` Pascali's Island (film) [0]: Pascali's Island is a 1988 British drama film, based on the novel by Barry Unsworth.
- `d8s1` Pascali's Island (film) [1]: It was written and directed by James Dearden.
- `d8s2` Pascali's Island (film) [2]: It stars Ben Kingsley, Charles Dance and Helen Mirren.
- `d8s3` Pascali's Island (film) [3]: It was entered into the 1988 Cannes Film Festival.
- `d9s0` The Songs of the Kings [0]: The Songs of Kings was a novel published in 2002 by Barry Unsworth that retells the story of "Iphigenia at Aulis" told by the Greek tragic poet Euripides.
- `d10s0` Morality Play (novel) [0]: Morality Play is a semi-historical detective novel by Barry Unsworth.
- `d10s1` Morality Play (novel) [1]: The book, published in 1995 by Hamish Hamilton was shortlisted for the Man Booker Prize.

</details>

## Q194 — `hotpotqa_5a85f5115542991dd0999ed9` (revised draft)

> What kind of ships have been named after the King of Norway who ascended the throne in 1991?

Source answer: motor ships

Gold final answer: motor ships

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: King of Norway who ascended the throne in 1991 | false | Harald V | — | [d3s0] | — |
| u2: kind of ships bearing a name after {u1} | true | motor ships | u1 | [d4s0] | — |

Evidence:

- `d3s0` Harald V of Norway [0]: Harald V (] ; born 21 February 1937) is the King of Norway, having ascended the throne following the death of his father on 17 January 1991.
- `d4s0` MS Kronprins Harald [0]: Several motor ships have borne the name Kronprins Harald, after Harald V of Norway:

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Ramesuan (king of Ayutthaya) [0]: Somdet Phra Ramesuan (Thai: สมเด็จพระราเมศวร ) (1339–1395), son of king Ramathibodi I, reigned as the second and fifth king of the kingdom of Ayutthaya.
- `d1s1` Ramesuan (king of Ayutthaya) [1]: When King Ramathibodi ascended to the throne of Ayuthaya, he sent King Ramesuan to reign in Lavo.
- `d1s2` Ramesuan (king of Ayutthaya) [2]: Upon King Ramathibodi's death in 1369, King Ramesuan traveled to Ayutthaya to assume the throne, but held it for less than a year before being deposed by his uncle, King Borommaracha I, the ruler of Suphanburi.
- `d1s3` Ramesuan (king of Ayutthaya) [3]: Sources differ over the nature of their conflict; official chronicles state that the older Boromaracha ruled with the willing consent of his nephew, while Jeremias van Vliet's "Short History of Thailand" indicated that Boromaracha's ascension came only after a bloody conflict bordering on civil war.
- `d2s0` Minhlange [0]: Minhlange (Burmese: မင်းလှငယ် , ] ; 1418–1425) was king of Ava for about three months in 1425.
- `d2s1` Minhlange [1]: Minhlange ascended to the throne in August 1425 after his father King Thihathu had been killed in an ambush by raiders from the Shan State of Hsipaw (Thibaw).
- `d2s2` Minhlange [2]: He was only about seven years old.
- `d2s3` Minhlange [3]: The ambush was arranged by Thihathu's powerful queen Shin Bo-Me who wanted to place her lover, Kale Kyetaungnyo, the Saopha of Kale, on the throne.
- `d2s4` Minhlange [4]: About three months later, Shin Bo-Me poisoned the young king in early November 1425 and made Kyetaungnyo king a few days later.
- `d3s0` Harald V of Norway [0]: Harald V (] ; born 21 February 1937) is the King of Norway, having ascended the throne following the death of his father on 17 January 1991.
- `d4s0` MS Kronprins Harald [0]: Several motor ships have borne the name Kronprins Harald, after Harald V of Norway:
- `d5s0` Martanda Cinkaiariyan [0]: Martanda Cinkaiariyan (Tamil: மார்த்தாண்ட சிங்கையாரியன் ) (died 1348) ascended the throne of Jaffna Kingdom under the throne name Pararasasekaram III.
- `d5s1` Martanda Cinkaiariyan [1]: He is one of the early Aryacakravarti kings about whom historical and epigraphical evidence is available.
- `d5s2` Martanda Cinkaiariyan [2]: He was noted by Ibn Battuta in his well-known travelogue as well as he has left behind a few inscriptions.
- `d5s3` Martanda Cinkaiariyan [3]: He oversaw the international trade of the Jaffna kingdom with Yemen via the kingdom's powerful trading ships.
- `d5s4` Martanda Cinkaiariyan [4]: Martanda Cinkaiariyan accompanied Battuta to the peak of "Sivanoli Padam Malai" along with Yogis and other Hindus and companions of the king who visited the sacred Shiva site annually.
- `d6s0` Coloman, King of Hungary [0]: Coloman the Learned, also the Book-Lover or the Bookish (Hungarian: "Könyves Kálmán" ; Croatian: "Koloman" ; Slovak: "Koloman Učený" ; 10703February 1116) was King of Hungary from 1095 and King of Croatia from 1097 until his death.
- `d6s1` Coloman, King of Hungary [1]: Because Coloman and his younger brother Álmos were underage when their father King Géza I of Hungary died, their uncle LadislausI ascended the throne in 1077.
- `d6s2` Coloman, King of Hungary [2]: Ladislaus prepared Colomanwho was "half-blind and humpbacked", according to late medieval Hungarian chroniclesfor a church career, and Coloman was eventually appointed bishop of Eger or Várad (Oradea, Romania) in the early 1090s.
- `d6s3` Coloman, King of Hungary [3]: The dying King Ladislaus preferred Álmos to Coloman when nominating his heir in early 1095.
- `d6s4` Coloman, King of Hungary [4]: Coloman fled from Hungary but returned around 19 July 1095 when his uncle died.
- `d6s5` Coloman, King of Hungary [5]: He was crowned in early 1096; the circumstances of his accession to the throne are unknown.
- `d6s6` Coloman, King of Hungary [6]: He granted the Hungarian Duchyone-third of the Kingdom of Hungaryto Álmos.
- `d7s0` Parakrama Pandyan I [0]: Parakrama Pandyan I was a Pandyan king of Tamilakkam, ruling from the Pandyan capital in Madurai.
- `d7s1` Parakrama Pandyan I [1]: He was besieged in a Pandyan war by his contemporary, rival and throne claimant Kulasekhara Pandyan in 1169, a vassal of the Chola Dynasty.
- `d7s2` Parakrama Pandyan I [2]: Parakrama Pandyan I sought assistance from the Ceylonese king Parakramabahu I of Polonnaruwa but was subsequently executed.
- `d7s3` Parakrama Pandyan I [3]: Kulasekhara Pandyan ascended to the Madurai throne but was eventually forced to seek refuge in Chola country in 1171.
- `d7s4` Parakrama Pandyan I [4]: Parakrama Pandyan I's son Vira Pandyan III ascended on the Pandyan throne before he was defeated by Chola forces.
- `d7s5` Parakrama Pandyan I [5]: In 1212 CE a succeeding namesake royal of the dynasty, Parakrama Pandyan II invaded Ceylon and became monarch at Polonnaruwa for three years with the title Parakrama Pandya of Polonnaruwa.
- `d8s0` Lü Buwei [0]: Lü Buwei (291–235 BC) was a politician of the Qin state in the Warring States period of ancient China.
- `d8s1` Lü Buwei [1]: Originally an influential merchant from the Wey (衛) state, Lü Buwei met and befriended King Zhuangxiang of Qin, who was then a minor prince serving as a hostage in the Zhao state.
- `d8s2` Lü Buwei [2]: Through bribes and machinations, Lü Buwei succeeded in helping King Zhuangxiang become the heir apparent to the Qin throne.
- `d8s3` Lü Buwei [3]: In 249 BC, after King Zhuangxiang ascended the throne following the death of his father, King Xiaowen, he appointed Lü Buwei as his chancellor (相國) and ennobled him as "Marquis Wenxin" (文信侯).
- `d8s4` Lü Buwei [4]: After King Zhuangxiang's death in 247 BC, Lü Buwei became the chancellor and regent to King Zhuangxiang's young son, Ying Zheng, who later became Qin Shi Huang (First Emperor of the Qin Dynasty).
- `d9s0` Coenwulf of Mercia [0]: Coenwulf (also spelled Cenwulf, Kenulf, or Kenwulph) was King of Mercia from December 796 until his death in 821.
- `d9s1` Coenwulf of Mercia [1]: He was a descendant of a sibling of King Penda, who had ruled Mercia in the middle of the 7th century.
- `d9s2` Coenwulf of Mercia [2]: He succeeded Ecgfrith, the son of Offa; Ecgfrith only reigned for five months, and Coenwulf ascended to the throne in the same year that Offa died.
- `d9s3` Coenwulf of Mercia [3]: In the early years of Coenwulf's reign he had to deal with a revolt in Kent, which had been under Offa's control.
- `d9s4` Coenwulf of Mercia [4]: Eadberht Præn returned from exile in Francia to claim the Kentish throne, and Coenwulf was forced to wait for papal support before he could intervene.
- `d9s5` Coenwulf of Mercia [5]: When Pope Leo agreed to anathematize Eadberht, Coenwulf invaded and retook the kingdom; Eadberht was taken prisoner, was blinded, and had his hands cut off.
- `d9s6` Coenwulf of Mercia [6]: Coenwulf also appears to have lost control of the kingdom of East Anglia during the early part of his reign, as an independent coinage appears under King Eadwald.
- `d9s7` Coenwulf of Mercia [7]: Coenwulf's coinage reappears in 805, indicating that the kingdom was again under Mercian control.
- `d9s8` Coenwulf of Mercia [8]: Several campaigns of Coenwulf's against the Welsh are recorded, but only one conflict with Northumbria, in 801, though it is likely that Coenwulf continued to support the opponents of the Northumbrian king Eardwulf.
- `d10s0` Sen Soulintha [0]: Sen Soulintha, Saen Surintha or Sen Sourintha (1511–1582) was born Chane Tian and became King of Lan Xang reigning 1571-1575 and again 1580-1582.
- `d10s1` Sen Soulintha [1]: Sen Soulintha was not of noble birth, rising from royal page to King Setthatirath’s Chief Minister.
- `d10s2` Sen Soulintha [2]: During the succession disputes in the Kingdom of Lan Na between King Setthatirath and King Mekuti, Sen Soulintha served Setthatirath as a general and successfully took several cities of Lan Na including Chiang Saen for which he was given the honorific name "Lusai" meaning “victory.”
- `d10s3` Sen Soulintha [3]: Sen Soulintha supported Setthatirath in leading the guerrilla campaigns during the Burmese invasions of King Bayinnaung.
- `d10s4` Sen Soulintha [4]: When Setthatirath died near Attapeu under suspicious circumstances in 1572, Sen Soulintha led the armies of Lan Xang back to Vientiane.
- `d10s5` Sen Soulintha [5]: A succession dispute erupted, which nearly led to civil war and provided a pretext for another Burmese invasion ordered by Bayinnaung and led by the Chief Minister Binnya Dala.
- `d10s6` Sen Soulintha [6]: Sen Soulintha defeated the Burmese and Lan Na forces led by Binnya Dala, an event which led to the latter’s exile, only to face a more massive invasion led by Bayinnaug the following year.
- `d10s7` Sen Soulintha [7]: Sen Soulintha again attempted to resort to guerilla tactics, but lacked popular support from his seizure of the throne.
- `d10s8` Sen Soulintha [8]: He and his son Ong Lo (Nakhon Noi) were captured by Bayinnaung and exiled to Pegu.
- `d10s9` Sen Soulintha [9]: The Burmese placed Setthathirath’s brother, and former "Ouphahat" or Viceroy, Prince Tha Heua on the throne.
- `d10s10` Sen Soulintha [10]: According to the Luang Prabang chronicles it was this brother, who had led a rebellion in Luang Prabang and tried to seize the throne from Setthathirath on the death of their father Photisarath.
- `d10s11` Sen Soulintha [11]: Prince Tha Heua took the regnal name Voravongsa and reigned under Burmese suzerainty from 1575-1579.
- `d10s12` Sen Soulintha [12]: Voravongsa was never popular, and drowned with his family while attempting to flee Vientiane in the face of popular uprising.
- `d10s13` Sen Soulintha [13]: In 1579, Bayinnaung dispatched a sizable army to restore order.
- `d10s14` Sen Soulintha [14]: According to Lao histories Sen Soulintha was then installed as king a second time in 1580.
- `d10s15` Sen Soulintha [15]: By that time Sen Soulintha was an old man and reigned only for two years before his son ascended the throne as Nakhon Noi and another succession dispute ensued.

</details>

## Q195 — `hotpotqa_5ac2c3545542990b17b1548b` (revised draft)

> Chang Ucchin was born in korea during a time that ended with the conclusion of what? 

Source answer: World War II

Gold final answer: World War II

Question type: `bridge` (source type `bridge`)

Replaces: `hotpotqa_5a862da855429960ec39b640`

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: historical period in Korea when Chang Ucchin was born | false | Japanese colonial rule | — | [d10s1] | — |
| u2: war whose conclusion ended {u1} in Korea | true | World War II | u1 | [d5s0] | — |

Evidence:

- `d5s0` Korea under Japanese rule [0]: Korea under Japanese rule began with the end of the short-lived Korean Empire in 1910 and ended at the conclusion of World War II in 1945.
- `d10s1` Chang Ucchin [1]: Chang was born when Korea was still under Japanese colonial rule.

Notes:

- 替换：创建奖项不等于赞助奖项；上下文没有明确赞助关系。 新题保留原source type，人工核对两条显式事实及答案。

<details><summary>All source context</summary>

- `d1s0` May 16 coup [0]: The May 16 coup (Hangul: 5.16 군사정변 ; Hanja: 五一六軍事政變 ; RR: "O-illyuk gunsa-jeongbyeon " ) was a military coup d'état in South Korea in 1961, organized and carried out by Park Chung-hee and his allies who formed the Military Revolutionary Committee, nominally led by Army Chief of Staff Chang Do-yong after the latter's acquiescence on the day of the coup.
- `d1s1` May 16 coup [1]: The coup rendered powerless the democratically elected government of Yun Bo-seon and ended the Second Republic, installing a reformist military Supreme Council for National Reconstruction effectively led by Park, who took over as Chairman after General Chang's arrest in July.
- `d2s0` Han Myeong-sook [0]: Han Myeong-sook (born March 24, 1944; Korean: 한명숙 ] ) was the Prime Minister of South Korea from April 2006 to March 2007.
- `d2s1` Han Myeong-sook [1]: She is South Korea's first female prime minister (second female prime minister overall if the acting premiership of Chang Sang is included).
- `d2s2` Han Myeong-sook [2]: She was from the United New Democratic Party (UNDP) as a member of the Korean National Assembly (representative) for Ilsan-gab, and is a graduate of Ewha Womans University in Seoul with a degree in French literature.
- `d2s3` Han Myeong-sook [3]: She resigned as Prime Minister on March 7, 2007 and declared her presidential candidacy.
- `d2s4` Han Myeong-sook [4]: But she did not succeed in the nominations.
- `d2s5` Han Myeong-sook [5]: In 2008 she ran for parliament, but was not elected.
- `d2s6` Han Myeong-sook [6]: However, in January 2012 she was elected leader of the main oppositional Democratic United Party (DUP) before the April legislative elections and became a member of parliament.
- `d2s7` Han Myeong-sook [7]: But the liberals did not manage to defeat the ruling Saenuri Party and Han stepped down as party leader in April 2012.
- `d2s8` Han Myeong-sook [8]: In August 2015, Han was convicted of receiving illegal donations at the amount of 900 million KRW, and sentence to two years in prison.
- `d2s9` Han Myeong-sook [9]: She is ineligible to run for public office for ten years after her prison term.
- `d2s10` Han Myeong-sook [10]: She became the first former prime minister of the Republic of Korea to serve a prison time.
- `d3s0` Chang Dae-hwan [0]: Chang Dae-hwan (also Chang Dae-whan; born 21 March 1952) is a South Korean businessman.
- `d3s1` Chang Dae-hwan [1]: He is best known as the president of the "Maeil Business Newspaper", South Korea's main business daily.
- `d3s2` Chang Dae-hwan [2]: He also served a brief stint as South Korea's acting prime minister in August 2002 under president Kim Dae-jung, but the National Assembly voted not to confirm him.
- `d4s0` Chang Won-jun [0]: Chang Won-jun (Hangul: 장원준, Hanja: 張元準) (born July 31, 1985 in Seoul) is a South Korean starting pitcher who currently plays for the Doosan Bears.
- `d4s1` Chang Won-jun [1]: Chang played for the Lotte Giants in the Korea Baseball Organization from 2004 to 2011.
- `d4s2` Chang Won-jun [2]: He bats and throws left-handed.
- `d5s0` Korea under Japanese rule [0]: Korea under Japanese rule began with the end of the short-lived Korean Empire in 1910 and ended at the conclusion of World War II in 1945.
- `d5s1` Korea under Japanese rule [1]: Japanese rule of Korea was the outcome of a process that began with the Japan–Korea Treaty of 1876, whereby a complex coalition of the Meiji government, military, and business officials sought to integrate Korea both politically and economically into the Empire of Japan.
- `d5s2` Korea under Japanese rule [2]: A major stepping-stone towards the Japanese occupation of Korea was the Japan–Korea Treaty of 1905, in which the then-Korean Empire was declared a protectorate of Japan.
- `d5s3` Korea under Japanese rule [3]: The annexation of Korea by Japan was set up in the Japan–Korea Treaty of 1910, which was never actually signed by the Korean Regent, Gojong.
- `d6s0` Tommy Chang (martial artist) [0]: Born and raised in Kyong Ki Do, South Korea, Master Tommy Chang is a Korean-Canadian world-renowned 7th degree Taekwondo and 8Th Degree Hapkido instructor and Grandmaster, actor, stunt performer, stunt coordinator and producer.
- `d6s1` Tommy Chang (martial artist) [1]: With over 40 years of training and experience in Taekwondo and Hapkido, Master Chang also trained extensively in ITF/WTF TKD, Moo Duk Kwan, and Judo.
- `d6s2` Tommy Chang (martial artist) [2]: He is also an 8th Degree Black Belt in Hap Ki-Do, specializing in pressure points, take-downs and grappling.
- `d6s3` Tommy Chang (martial artist) [3]: His martial arts expertise also encompasses mastery of several weapons.
- `d6s4` Tommy Chang (martial artist) [4]: In addition, he is a WTF-certified Master Instructor of Taekwondo and a Canadian National Referee (1st Class).
- `d7s0` United States in the Korean War [0]: At the conclusion of World War II the Allied nations began the process of disarmament of Axis controlled regions.
- `d7s1` United States in the Korean War [1]: Japan occupied Korea at this time and had been in control since 1910.
- `d7s2` United States in the Korean War [2]: In 1945, the decision was made to have American Marines forces oversee Japanese surrender and disarmament south of the 38th parallel and the Soviet Union would facilitate the change of power to the north.
- `d7s3` United States in the Korean War [3]: At the time there was no political motivation and seemed to be a logical and convenient plan of action.
- `d7s4` United States in the Korean War [4]: The original agreement and intent was to create a unified and independent Korea out of the post Japanese occupation era.
- `d7s5` United States in the Korean War [5]: Instead each side of the 38th parallel established its own government under the influence of the occupational country; the United States in South Korea and the Soviet Union in North Korea.
- `d7s6` United States in the Korean War [6]: Both new Korean governments discredited the other and claimed to be the only legitimate political system.
- `d7s7` United States in the Korean War [7]: Tensions between the North and South escalated and each side began to petition foreign powers for resources and support.
- `d7s8` United States in the Korean War [8]: South Korea wanted weapons and supplies from Truman and the United States government while North Korea sought help from Stalin and the Soviet Union.
- `d7s9` United States in the Korean War [9]: The United States was still war weary from the disruptive World War II campaign and refused South Korea's request for weapons and troops.
- `d7s10` United States in the Korean War [10]: North Korea convinced the Soviet Union to supply them with the weapons and support they requested.
- `d7s11` United States in the Korean War [11]: This decision coincided with the United States withdrawing the last remaining combat troops from South Korea.
- `d7s12` United States in the Korean War [12]: North Korea saw its opportunity and attacked South Korean forces at the 38th parallel on June 25, 1950 and thus initiating the Korean War.
- `d8s0` Chang Mi-hee [0]: Chang Mi-hee (born December 8, 1958) is a South Korean actress active since 1976.
- `d8s1` Chang Mi-hee [1]: She was born Lee Yun-hui in Seoul, South Korea in 1957.
- `d8s2` Chang Mi-hee [2]: Chang debuted as an actress in 1976 as starring in "Seong Chun-hyang jeon" directed by Park Tae-won and TBC TV drama, "Haenyeo Dang-sil" (Sea Woman Dang-sil).
- `d8s3` Chang Mi-hee [3]: Chang was commonly referred to as "New Troika" or "Second Troika" along with her rival actresses, Jeong Yun-hui and Yu Ji-in of the 1970s and 1980s after the "First Troika", Moon Hee, Nam Jeong-im, and Yoon Jeong-hee of the 1960s.
- `d9s0` Chang Yong-hak [0]: Chang Yong-hak (25 April 1921 – 31 August 1999) was a Korean writer.
- `d9s1` Chang Yong-hak [1]: Chang was born in Hamyeong Buk-do in what is now North Korea.
- `d9s2` Chang Yong-hak [2]: He studied at Waseda University in Japan, before being drafted into the Japanese army.
- `d9s3` Chang Yong-hak [3]: After the end of World War Two, he taught high school in Korea, writing fiction on the side.
- `d10s0` Chang Ucchin [0]: Chang Ucchin (26 November 1917 – 27 December 1990) is one of the representatives of modern Korean fine art.
- `d10s1` Chang Ucchin [1]: Chang was born when Korea was still under Japanese colonial rule.
- `d10s2` Chang Ucchin [2]: He studied western art at Tokyo's Imperial School of Art.
- `d10s3` Chang Ucchin [3]: He became a professor of fine arts at Seoul National University in 1954, but resigned to paint full-time from 1960.

</details>

## Q196 — `hotpotqa_5ab808755542990e739ec7f2` (revised draft)

> Which movie was released first, The Hunchback of Notre Dame or Saludos Amigos?

Source answer: Saludos Amigos

Gold final answer: Saludos Amigos

Question type: `comparison` (source type `comparison`)

Replaces: `hotpotqa_5a864d9e5542994775f6073d`

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: film year of The Hunchback of Notre Dame | false | 1996 | — | [d7s0] | — |
| u2: film year of Saludos Amigos | false | 1942 | — | [d9s0] | — |
| u3: Which movie was released first, The Hunchback of Notre Dame or Saludos Amigos? | true | Saludos Amigos | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d7s0` The Hunchback of Notre Dame (1996 film) [0]: The Hunchback of Notre Dame is a 1996 American animated musical drama film produced by Walt Disney Feature Animation for Walt Disney Pictures.
- `d9s0` Saludos Amigos [0]: Saludos Amigos (Spanish for "Greetings, Friends") is a 1942 American live-action animated package film produced by Walt Disney and released by RKO Radio Pictures.

Notes:

- 替换：French Air Force任职不等于法国来源/国籍；没有其他支持u2的句子。 新题保留原source type，人工核对两条显式事实及答案。

<details><summary>All source context</summary>

- `d1s0` 2009 Notre Dame Fighting Irish football team [0]: The 2009 Notre Dame Fighting Irish football team represented the University of Notre Dame in the 2009 NCAA Division I FBS football season.
- `d1s1` 2009 Notre Dame Fighting Irish football team [1]: The team was coached by Charlie Weis and played its home games at Notre Dame Stadium in South Bend, Indiana.
- `d1s2` 2009 Notre Dame Fighting Irish football team [2]: Weis entered his fifth season as head coach with the expectation from the Notre Dame administration that his team would be in position to compete for a BCS Bowl berth.
- `d1s3` 2009 Notre Dame Fighting Irish football team [3]: Notre Dame started the first part of the season 4-2, with close losses to Michigan and USC but ended the season with four straight losses, including a second loss to Navy loss in three years.
- `d1s4` 2009 Notre Dame Fighting Irish football team [4]: Weis was fired as head coach the Monday after the Stanford loss at the end of the season.
- `d1s5` 2009 Notre Dame Fighting Irish football team [5]: Although Notre Dame was bowl eligible with 6 wins, the University announced on December 4 that the Irish had chosen not to play in a bowl game.
- `d1s6` 2009 Notre Dame Fighting Irish football team [6]: Irish athletic director Jack Swarbrick hired Cincinnati head coach Brian Kelly after a 10-day coaching search.
- `d2s0` Notre Dame of Genio Edcor Inc. [0]: Notre Dame of Genio Edcor, Inc. (Old name: "Notre Dame of Edcor" ) is a private, Catholic academic institution run by the Oblates of Notre Dame located in Alamada, Cotabato, Philippines.This school is a member of the Notre Dame Educational Association.
- `d2s1` Notre Dame of Genio Edcor Inc. [1]: Established in 1958,It has been one of the pioneering school under the Notre Dame Educational System run by the Oblates of Notre Dame in the province of North Cotabato, Philippines.
- `d3s0` Notre Dame of Midsayap College [0]: Notre Dame of Midsayap College (Tagalog: "Dalubhasaang Notre Dame ng Midsayap" or "Kolehiyong Notre Dame ng Midsayap") (colloquially known as "NDMC" or simply "Notre Dame") is a private, Catholic academic institution run by the Missionary Oblates of Mary Immaculate in Midsayap, Cotabato.
- `d3s1` Notre Dame of Midsayap College [1]: Established on 13 June 1941 making it as the "First Notre Dame School in Asia and in the Philippines", it was the first link in the long chain of Notre Dame Schools in the Philippines that form the Notre Dame Educational Association under the patronage of the Blessed Virgin Mary, the school Patroness and St. Eugene De Mazenod as the school's patron saint.
- `d4s0` South of the Border with Disney [0]: South of the Border with Disney is a 1942 Disney short documentary film.
- `d4s1` South of the Border with Disney [1]: It was shot in the same occasion "Saludos Amigos" was, when Walt Disney and a group of eighteen artists, musicians and writers went to South America looking for inspirations for a movie.
- `d4s2` South of the Border with Disney [2]: While "Saludos Amigos" is the result of this voyage, alternating animated shorts to the sequences from the travel that inspired them, "South of the Border with Disney" is more of a behind-the-scenes documentary showing only the travel and the genesis of cartoons not only for "Saludos Amigos" and "The Three Caballeros", but also some others used in later occasions.
- `d4s3` South of the Border with Disney [3]: The most notable example is a female Armadillo used for a 1943 Pluto cartoon, "Pluto and the Armadillo".
- `d4s4` South of the Border with Disney [4]: Film also includes some pencil test animation.
- `d5s0` Notre Dame Fighting Irish football [0]: The Notre Dame Fighting Irish football team is the intercollegiate football team representing the University of Notre Dame in Notre Dame, Indiana.
- `d5s1` Notre Dame Fighting Irish football [1]: The team is currently coached by Brian Kelly and plays its home games at the campus's Notre Dame Stadium, which has a capacity of 80,795 fans.
- `d5s2` Notre Dame Fighting Irish football [2]: Notre Dame is one of four schools that competes as an Independent at the National Collegiate Athletic Association (NCAA) Football Bowl Subdivision level; however, they play five games a year against opponents from the Atlantic Coast Conference (ACC), which Notre Dame is a member of in all other sports except ice hockey.
- `d6s0` Notre Dame Shakespeare Festival [0]: The Notre Dame Shakespeare Festival (formerly Summer Shakespeare) at the University of Notre Dame is an annual festival that seeks to combine professional productions of the works of William Shakespeare with community outreach and educational programs.
- `d6s1` Notre Dame Shakespeare Festival [1]: The Notre Dame Shakespeare Festival is a part of the University of Notre Dame's Shakespeare initiative entitled "Shakespeare at Notre Dame", a program that recognizes the centrality of the study of Shakespeare in humanistic pedagogy at the University.
- `d6s2` Notre Dame Shakespeare Festival [2]: Its fifteenth season (summer of 2014) was known as the 15/150, also celebrating the 450th birthday of William Shakespeare, and the 150th anniversary of the first full production of Shakespeare at the university in 1864 (Records indicate the first performance of Shakespeare at the University of Notre Dame took place in 1847, a collection of scenes also from "Henry IV)."
- `d6s3` Notre Dame Shakespeare Festival [3]: The anniversary season consisted of the Professional Company production of "Henry IV" (directed by Michael Goldberg), the Young Company performance of "The Merry Wives of Windsor" (directed by West Hyler), and the annual ShakeScenes shows featuring actors of all ages from South Bend and the surrounding community.
- `d7s0` The Hunchback of Notre Dame (1996 film) [0]: The Hunchback of Notre Dame is a 1996 American animated musical drama film produced by Walt Disney Feature Animation for Walt Disney Pictures.
- `d7s1` The Hunchback of Notre Dame (1996 film) [1]: The 34th Disney animated feature film, the film is based on Victor Hugo's novel of the same name.
- `d7s2` The Hunchback of Notre Dame (1996 film) [2]: The plot centers on Quasimodo, the deformed bell-ringer of Notre Dame, and his struggle to gain acceptance into society.
- `d7s3` The Hunchback of Notre Dame (1996 film) [3]: Directed by Kirk Wise and Gary Trousdale and produced by Don Hahn, the film's voice cast features Tom Hulce, Demi Moore, Tony Jay, Kevin Kline, Paul Kandel, Jason Alexander, Charles Kimbrough, David Ogden Stiers, and Mary Wickes in her final film role.
- `d8s0` Notre Dame–Stanford football rivalry [0]: The Notre Dame–Stanford football rivalry is an American college football rivalry between the Notre Dame Fighting Irish football team of the University of Notre Dame and Stanford Cardinal football team of Stanford University.
- `d8s1` Notre Dame–Stanford football rivalry [1]: As of 2016, the Notre Dame Fighting Irish and Stanford Cardinal have met 31 times, beginning in 1925 (though the modern series began in 1988).
- `d8s2` Notre Dame–Stanford football rivalry [2]: The Notre Dame–Stanford game has been played annually since 1997, with the teams meeting at Notre Dame Stadium earlier in the season (late September to mid-October) in even-numbered years, and at Stanford Stadium on the weekend following Thanksgiving in odd-numbered years since 1999.
- `d8s3` Notre Dame–Stanford football rivalry [3]: The game typically alternates positions in Notre Dame's schedule with its other Pac-12 opponent, USC.
- `d9s0` Saludos Amigos [0]: Saludos Amigos (Spanish for "Greetings, Friends") is a 1942 American live-action animated package film produced by Walt Disney and released by RKO Radio Pictures.
- `d9s1` Saludos Amigos [1]: It is the sixth Disney animated feature film and the first of the six package films produced by Walt Disney Productions in the 1940s.
- `d9s2` Saludos Amigos [2]: Set in Latin America, it is made up of four different segments; Donald Duck stars in two of them and Goofy stars in one.
- `d9s3` Saludos Amigos [3]: It also features the first appearance of José Carioca, the Brazilian cigar-smoking parrot.
- `d9s4` Saludos Amigos [4]: "Saludos Amigos" was popular enough that Walt Disney decided to make another film about Latin America, "The Three Caballeros", to be produced two years later.
- `d9s5` Saludos Amigos [5]: "Saludos Amigos" premiered in Rio de Janeiro on August 24, 1942.
- `d9s6` Saludos Amigos [6]: It was released in the United States on February 6, 1943.
- `d9s7` Saludos Amigos [7]: At 42 minutes, it is Disney's shortest animated feature to date.
- `d9s8` Saludos Amigos [8]: It garnered positive reviews and was theatrically reissued in 1949, when it was shown on a double bill with the first reissue of "Dumbo".
- `d10s0` 2007 Navy vs. Notre Dame football game [0]: The 2007 Navy vs. Notre Dame football game ended the longest all-time college football consecutive wins streak by one team over another.
- `d10s1` 2007 Navy vs. Notre Dame football game [1]: On November 3, 2007, the Navy Midshipmen defeated the Notre Dame Fighting Irish 46–44 in triple-overtime at Notre Dame's home field, Notre Dame Stadium in South Bend, Indiana.
- `d10s2` 2007 Navy vs. Notre Dame football game [2]: Notre Dame came into this annual game with 43 straight wins against Navy since the last loss against Heisman Trophy winner Roger Staubach in 1963.
- `d10s3` 2007 Navy vs. Notre Dame football game [3]: With the win, Navy improved to 5–4 and Notre Dame fell to 1–8 on the season.

</details>

## Q197 — `hotpotqa_5a87191155429960ec39b73d` (revised draft)

> What private university in Virginia did Jamal Benjamin Brooks play college football at?

Source answer: Hampton University

Gold final answer: Hampton University

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: university where Jamal Brooks played college football | false | Hampton University | — | [d4s1] | — |
| u2: private university in Virginia identified by {u1} | true | Hampton University | u1 | [d1s0] | — |

Evidence:

- `d1s0` Hampton University [0]: Hampton University (also HU, or Home by the Sea) is a private historically black university located in Hampton, Virginia, United States.
- `d4s1` Jamal Brooks [1]: He played college football at Hampton University.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Hampton University [0]: Hampton University (also HU, or Home by the Sea) is a private historically black university located in Hampton, Virginia, United States.
- `d1s1` Hampton University [1]: It was founded in 1868 by black and white leaders of the American Missionary Association after the American Civil War to provide education to freedmen.
- `d1s2` Hampton University [2]: In 1878, it established a program for teaching Native Americans, which lasted until 1923.
- `d2s0` Seantrel Henderson [0]: Seantrel Henderson (born January 21, 1992) is an American football offensive tackle for the Buffalo Bills of the National Football League (NFL).
- `d2s1` Seantrel Henderson [1]: He was drafted by the Bills in the seventh round of the 2014 NFL Draft.
- `d2s2` Seantrel Henderson [2]: He played college football at Miami.
- `d2s3` Seantrel Henderson [3]: Henderson attended Cretin-Derham Hall High School and originally signed a letter of intent to play college football at the University of Southern California, but was released from his commitment in July 2010 and eventually committed to the University of Miami.
- `d3s0` Jamal Anderson [0]: Jamal Sharif Anderson (born September 30, 1972) is a former American football running back of the National Football League.
- `d3s1` Jamal Anderson [1]: He was drafted by the Atlanta Falcons in the seventh round of the 1994 NFL Draft.
- `d3s2` Jamal Anderson [2]: He played high school football at El Camino Real High School, where he was named to the CIF Los Angeles City Section 4-A All-City first team in 1989.
- `d3s3` Jamal Anderson [3]: He went on to play college football at Moorpark College for the Moorpark College Raiders before playing at Utah.
- `d4s0` Jamal Brooks [0]: Jamal Benjamin Brooks (born November 9, 1976) is a former American football linebacker in the National Football League for the Dallas Cowboys and St. Louis Rams.
- `d4s1` Jamal Brooks [1]: He played college football at Hampton University.
- `d5s0` 1891 Purdue football team [0]: The 1891 Purdue football team was an American football team that represented Purdue University during the 1891 college football season.
- `d5s1` 1891 Purdue football team [1]: The team compiled a 4–0 record in the university's fourth season fielding an intercollegiate football team.
- `d5s2` 1891 Purdue football team [2]: For the 1891 season, Purdue hired Knowlton Ames as its football coach.
- `d5s3` 1891 Purdue football team [3]: Ames played for Princeton from 1886 to 1889 and was considered one of the greatest players ever to play college football, after scoring 730 points for Princeton.
- `d5s4` 1891 Purdue football team [4]: The 1891 Purdue team shut out all four opponents, outscoring Wabash, DePauw, Indiana, and Butler by a combined score of 192 to 0.
- `d5s5` 1891 Purdue football team [5]: Purdue's 60–0 victory over Indiana was the first installment in a rivalry which later became noted for the award of the Old Oaken Bucket trophy.
- `d6s0` George Thomas (American football) [0]: George Carroll Thomas, Jr. (March 4, 1928 – May 23, 1989) was an American football halfback and defensive back in the National Football League for the Washington Redskins and the New York Giants.
- `d6s1` George Thomas (American football) [1]: He was a standout high school basketball player, which led to his being recruited to play college basketball for Tulane University.
- `d6s2` George Thomas (American football) [2]: However, first year OU football coach, Jim Tatum, convinced him stay in Oklahoma and play college football at the University of Oklahoma.
- `d6s3` George Thomas (American football) [3]: Thomas was a standout for the Sooners, lettering in '46, '47,'48 and '49.
- `d6s4` George Thomas (American football) [4]: He earned All-American status in 1949 List of Oklahoma Sooners football All-Americans.
- `d6s5` George Thomas (American football) [5]: Thomas graduated from OU with a degree in Business Administration in 1950.
- `d7s0` Obi Egekeze [0]: Egekeze was born in Augusta, Georgia in 1985.
- `d7s1` Obi Egekeze [1]: He attended Westside High School in Augusta, where he was a three-year starter in football, basketball and soccer.
- `d7s2` Obi Egekeze [2]: A placekicker and punter for the school's football team, he was selected as an all-state player as a senior.
- `d7s3` Obi Egekeze [3]: Egekze also maintained a high school grade point average of 3.86 and was recruited to play college football by several major universities, including the University of Georgia, Ohio State University, University of Texas, and Penn State.
- `d7s4` Obi Egekeze [4]: He accepted a scholarship to attend the University of Maryland.
- `d8s0` Baron Batch [0]: Baron Batch (born December 21, 1987), self-styled "The Artist", a Pittsburgh-based entrepreneur and former American football running back who retired from the NFL in 2013.
- `d8s1` Baron Batch [1]: He is known for his "FREE" art drops, where he posts pictures of giveaway paintings on Instagram and Twitter, leaving clues to their location.
- `d8s2` Baron Batch [2]: He played college football at Texas Tech University.
- `d8s3` Baron Batch [3]: Batch chose to play college football at Texas Tech University over offers from Northwestern University, Duke University, and New Mexico State University.
- `d8s4` Baron Batch [4]: Batch is from Midland, Texas.
- `d8s5` Baron Batch [5]: He is the owner and creator of Angry Man Salsa and creative director of Studio AM.
- `d8s6` Baron Batch [6]: He is the brother of Brian Batch of the band Alpha Rev.
- `d9s0` Jamal Robertson [0]: Jamal Robertson (born January 10, 1977) is a former Canadian football running back and kick returner who played in the Canadian Football League and National Football League.
- `d9s1` Jamal Robertson [1]: He was originally signed by the Calgary Stampeders as an undrafted free agent in 2001.
- `d9s2` Jamal Robertson [2]: He played college football at Ohio Northern.
- `d9s3` Jamal Robertson [3]: Jamal was one of the greatest athletes in Ohio Northern University (ONU) history.
- `d9s4` Jamal Robertson [4]: During his career at ONU, he amassed numerous school records and won the Division III National Player of the Year award.
- `d9s5` Jamal Robertson [5]: Jamal is an alumnus of Walter E. Stebbins High School in Dayton, Ohio, where he was an all state running back and a state champion in track & field.
- `d10s0` Johnson Bademosi [0]: Johnson Bademosi (born July 23, 1990) is an American football cornerback and special teamer for the New England Patriots of the National Football League (NFL).
- `d10s1` Johnson Bademosi [1]: He was signed by the Browns as an undrafted free agent in 2012.
- `d10s2` Johnson Bademosi [2]: He was a member of the football, rugby, and track and field teams at Gonzaga College High School and went on to play college football for Stanford University.

</details>

## Q198 — `hotpotqa_5a87411d5542994846c1cd37` (revised draft)

> What job did Jörgen Smit work, where he was working in the world center for the anthroposophical movement?

Source answer: member of the Executive Council of the General Anthroposophical Society

Gold final answer: member of the Executive Council of the General Anthroposophical Society

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: world center for the anthroposophical movement | false | Goetheanum | — | [d9s0] | — |
| u2: job Jorgen Smit held at {u1} | true | member of the Executive Council of the General Anthroposophical Society | u1 | [d1s1] | — |

Evidence:

- `d1s1` Jörgen Smit [1]: He was the general secretary of the Norwegian Anthroposophical Society, co-founder of the Rudolf Steiner Seminar in Järna, Sweden and member of the Executive Council of the General Anthroposophical Society at the Goetheanum in Dornach, Switzerland.
- `d9s0` Goetheanum [0]: The Goetheanum, located in Dornach (near Basel), Switzerland, is the world center for the anthroposophical movement.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Jörgen Smit [0]: Jörgen Smit (July 21, 1916 in Bergen – May 10, 1991 in Arlesheim) was a Norwegian teacher, teachers teacher, speaker and writer, mainly in the context of the Anthroposophical Society and the Waldorfschool Movement.
- `d1s1` Jörgen Smit [1]: He was the general secretary of the Norwegian Anthroposophical Society, co-founder of the Rudolf Steiner Seminar in Järna, Sweden and member of the Executive Council of the General Anthroposophical Society at the Goetheanum in Dornach, Switzerland.
- `d2s0` Triodos Bank [0]: Triodos Bank N.V. is a bank based in the Netherlands with branches in Belgium, Germany, United Kingdom and Spain.
- `d2s1` Triodos Bank [1]: It claims to be a pioneer in ethical banking.
- `d2s2` Triodos Bank [2]: Triodos Bank finances companies which it thinks add cultural value and benefit both people and the environment.
- `d2s3` Triodos Bank [3]: That includes companies in the fields of solar energy, organic farming or culture.
- `d2s4` Triodos Bank [4]: The name Triodos is derived from the Greek "τρὶ ὁδος - tri hodos," meaning "three-way approach" (people, planet, profit).
- `d2s5` Triodos Bank [5]: Triodos Bank's balance sheet was worth EUR 5.3 billion by the end of 2012.
- `d2s6` Triodos Bank [6]: It is influenced by the anthroposophical movement.
- `d3s0` Polaris (composition) [0]: Polaris: Voyage for Orchestra is an orchestral composition by the British composer Thomas Adès.
- `d3s1` Polaris (composition) [1]: The work was co-commissioned by the New World Symphony under the direction of Michael Tilson Thomas for the opening of the New World Center.
- `d3s2` Polaris (composition) [2]: The New World Symphony was joined in commission by the Royal Concertgebouw Orchestra, the New York Philharmonic, the Calouste Gulbenkian Foundation, the Barbican Centre, the Los Angeles Philharmonic, and the San Francisco Symphony.
- `d3s3` Polaris (composition) [3]: It was given its world premiere by Michael Tilson Thomas and the New World Symphony at the New World Center in Miami Beach on January 26, 2011.
- `d4s0` Howard Smit [0]: Howard J. Smit (April 19, 1911 – August 1, 2009) was a pioneering American film make-up artist known for his work on films including "The Birds" and "The Wizard of Oz".
- `d4s1` Howard Smit [1]: Smit also spearheaded the movement to establish the Academy Award for Best Makeup to recognize the profession within the film industry.
- `d4s2` Howard Smit [2]: He also successfully pushed studios to credit film make-up artists in a movie's screen credits.
- `d5s0` Verlag Freies Geistesleben &amp; Urachhaus [0]: The Verlag Freies Geistesleben & Urachhaus GmbH is a publishing company based in Stuttgart, publishing under the imprints of "Verlag Freies Geistesleben" and "Verlag Urachhaus".
- `d5s1` Verlag Freies Geistesleben &amp; Urachhaus [1]: The company has its roots in the Anthroposophical movement, and is publishing a wide range of titles, including many classic titles.
- `d6s0` Marriott's Orlando World Center [0]: The Marriott's Orlando World Center Resort is a hotel and convention center near Orlando, Florida.
- `d6s1` Marriott's Orlando World Center [1]: The resort, which is close by to Walt Disney World, is located off of World Center Drive, which was renamed from International Drive to the resort's namesake after the southern extension of I-Drive was built.
- `d7s0` Willem Zeylmans van Emmichoven [0]: Frederick William Zeylmans van Emmichoven, (Helmond, November 23, 1893 - Cape Town, November 18, 1961) was a Dutch psychiatrist and anthroposophist.
- `d7s1` Willem Zeylmans van Emmichoven [1]: From 1923 until his death in 1961 he was chairman of the Dutch Anthroposophical Society.
- `d7s2` Willem Zeylmans van Emmichoven [2]: He was a familiar figure in public life and had a considerable influence on the anthroposophic movement, particularly through his numerous lectures and his work as an author, which included the first biography of Rudolf Steiner.
- `d8s0` U.S. Bank Tower (Los Angeles) [0]: U.S. Bank Tower, formerly Library Tower and First Interstate Bank World Center, is a 1018 ft skyscraper at 633 West Fifth Street in downtown Los Angeles, California.
- `d8s1` U.S. Bank Tower (Los Angeles) [1]: It is the third tallest building in California, the second tallest building in LA, the fifteenth tallest in the United States, the third tallest west of the Mississippi River after the Salesforce Tower and the Wilshire Grand Center, and the 92nd tallest building in the world, after being surpassed by the Wilshire Grand Center.
- `d8s2` U.S. Bank Tower (Los Angeles) [2]: Because local building codes required all high-rise buildings to have a helipad, it was known as the tallest building in the world with a roof-top heliport from its completion in 1989 to 2004 when Taipei 101 opened.
- `d8s3` U.S. Bank Tower (Los Angeles) [3]: It is also the third tallest building in a major active seismic region; its structure was designed to resist an earthquake of 8.3 on the Richter scale.
- `d8s4` U.S. Bank Tower (Los Angeles) [4]: It consists of 73 stories above ground and two parking levels below ground.
- `d8s5` U.S. Bank Tower (Los Angeles) [5]: Construction began in 1987 with completion in 1989.
- `d8s6` U.S. Bank Tower (Los Angeles) [6]: The building was designed by Henry N. Cobb of the architectural firm Pei Cobb Freed & Partners and cost $350 million to build.
- `d8s7` U.S. Bank Tower (Los Angeles) [7]: It is one of the most recognizable buildings in Los Angeles, and often appears in establishing shots for the city in films and television programs.
- `d9s0` Goetheanum [0]: The Goetheanum, located in Dornach (near Basel), Switzerland, is the world center for the anthroposophical movement.
- `d9s1` Goetheanum [1]: The building was designed by Rudolf Steiner and named after Johann Wolfgang von Goethe.
- `d9s2` Goetheanum [2]: It includes two performance halls (1500 seats), gallery and lecture spaces, a library, a bookstore, and administrative spaces for the Anthroposophical Society; neighboring buildings house the Society's research and educational facilities.
- `d9s3` Goetheanum [3]: Conferences focusing on themes of general interest or directed toward teachers, farmers, doctors, therapists, and other professionals are held at the center throughout the year.
- `d10s0` Job sharing [0]: Job sharing or work sharing is an employment arrangement where typically two people are retained on a part-time or reduced-time basis to perform a job normally fulfilled by one person working full-time.
- `d10s1` Job sharing [1]: Since all positions are shared thus leads to a net reduction in per-employee income.
- `d10s2` Job sharing [2]: The people sharing the job work as a team to complete the job task and are equally responsible for the job workload.
- `d10s3` Job sharing [3]: Compensation is apportioned between the workers, Working hours, pay and holidays are divided equally.
- `d10s4` Job sharing [4]: The Pay As You Go system helps make deductions for national insurance and superannuations are made as a straightforward percentage.

</details>

## Q199 — `hotpotqa_5a88f7855542993b751ca8da` (revised draft)

> In what year did a movie that starred both Nicholas Cage and Cher come out? 

Source answer: 1987

Gold final answer: 1987

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: film in which Nicolas Cage and Cher both starred | false | Moonstruck | — | [d10s1] | — |
| u2: film year of {u1} | true | 1987 | u1 | [d10s0] | — |

Evidence:

- `d10s0` Moonstruck [0]: Moonstruck is a 1987 American romantic comedy film directed by Norman Jewison and written by John Patrick Shanley.
- `d10s1` Moonstruck [1]: It is about a widowed 37-year-old Italian-American woman (Cher) who falls in love with her fiancé's (Danny Aiello) estranged, hot-tempered younger brother (Nicolas Cage).

Notes:

- Nicholas in the question is a spelling variant of Nicolas Cage in the source.
- 复核后保留原标注；原note为说明或未发现需要修改的证据/依赖问题。

<details><summary>All source context</summary>

- `d1s0` Cher filmography [0]: Throughout her acting career, Cher has mainly in comedy, drama, and romance films.
- `d1s1` Cher filmography [1]: She has appeared in thirteen films, including two as a cameo.
- `d1s2` Cher filmography [2]: She has also appeared in one starring theater role, numerous television commercials and directed a piece of the motion picture "If These Walls Could Talk" in 1996 and some of her music videos of the Geffen-era in late 1980s and in early 1990s.
- `d1s3` Cher filmography [3]: Cher has starred in various international television commercials, as well as high-profile print advertising for Lori Davis (1992).
- `d1s4` Cher filmography [4]: Before she started her film career, she had a couple of hits in the 1960s, as a solo artist, and with her ex-husband Sonny Bono as the couple Sonny & Cher.
- `d2s0` Where Do You Go (Cher song) [0]: "Where Do You Go" is a song written by Sonny Bono.
- `d2s1` Where Do You Go (Cher song) [1]: It was released as the first single by Cher in the later quarter of 1965 for her second album "The Sonny Side of Cher".
- `d2s2` Where Do You Go (Cher song) [2]: It fell short of the "Billboard" Hot 100's top 20, but still earned Cher a moderate success, by reaching the Top 40.
- `d2s3` Where Do You Go (Cher song) [3]: It was followed by the U.S. #2 smash hit "Bang Bang (My Baby Shot Me Down)" which saw a release early the following year.
- `d2s4` Where Do You Go (Cher song) [4]: It was a bigger hit in Canada, where it reached #5 on the singles chart.
- `d3s0` 2012 in Cage Warriors [0]: The year 2012 is the 11th year in the history of Cage Warriors, a mixed martial arts promotion based in the United Kingdom.
- `d3s1` 2012 in Cage Warriors [1]: In 2012 Cage Warriors held 12 events beginning with, "Cage Warriors Fight Night 3".
- `d4s0` Nicolas Cage [0]: Nicolas Kim Coppola (born January 7, 1964), known professionally as Nicolas Cage, is an American actor, director and producer.
- `d4s1` Nicolas Cage [1]: During his early career, Cage starred in a variety of films such as "Valley Girl" (1983), "Racing with the Moon" (1984), "Birdy" (1984), "Peggy Sue Got Married" (1986), "Raising Arizona" (1987), "Moonstruck" (1987), "Vampire's Kiss" (1989), "Wild at Heart" (1990), "Fire Birds" (1990), "Honeymoon in Vegas" (1992), and "Red Rock West" (1993).
- `d5s0` Jimmy Tatro [0]: James Richard Tatro (born February 16, 1992) is an American actor, comedian, writer and YouTube personality.
- `d5s1` Jimmy Tatro [1]: He is the creator and star of the YouTube channel "LifeAccordingToJimmy", which has about 2.7 million subscribers and over 440 million video views.
- `d5s2` Jimmy Tatro [2]: Tatro writes, produces and directs each of his video sketches with his friend, Christian A. Pierce.
- `d5s3` Jimmy Tatro [3]: Tatro has appeared in "Divergent", "Grown Ups 2", "22 Jump Street" and "", and will appear in the film "Camp Manna" alongside Gary Busey, set to be released in 2017.
- `d5s4` Jimmy Tatro [4]: He is also starring in the true-crime satire, "American Vandal", in which he plays Dylan Maxwell, the accused vandal.
- `d5s5` Jimmy Tatro [5]: He will also appear in the movie, Action No. 1, a film about a group of people who attempt to steal the first comic book with Superman off the actor Nicholas Cage.
- `d6s0` Tony Bonello [0]: Tony Bonello is an Australian professional mixed martial artist and grappler who is currently signed to ONE FC.
- `d6s1` Tony Bonello [1]: A professional competitor since 2000, he has formerly competed for EliteXC, King of the Cage and Pancrase.
- `d6s2` Tony Bonello [2]: Bonello is the former, King of the Cage Middleweight Superfight Champion, the former King of the Cage Light Heavyweight Champion, and the former King of the Cage Cruiserweight Champion.
- `d6s3` Tony Bonello [3]: 14 of his 16 career wins have come by way of submission.
- `d7s0` Nicholas Mele [0]: Nicholas Mele is an actor who has starred in many movies and on television.
- `d7s1` Nicholas Mele [1]: His first movie role was in the 1976 movie "The Ritz".
- `d7s2` Nicholas Mele [2]: Other movie roles include "Some Kind of Hero" (1982) and "Young Doctors in Love" (1982).
- `d7s3` Nicholas Mele [3]: His most well-known film role was in the 1988 hit horror movie "" as Dennis Johnson.
- `d7s4` Nicholas Mele [4]: A year later, he reprised his role in the hit sequel "".
- `d7s5` Nicholas Mele [5]: His most recent movie is the 2003 film "The Great Gabble".
- `d8s0` Saint Nicholas Day [0]: Saint Nicholas' Day, observed on December 6 in Western Christian countries, December 5 in the Netherlands and December 19 in Eastern Christian countries, is the feast day of Saint Nicholas.
- `d8s1` Saint Nicholas Day [1]: It is celebrated as a Christian festival with particular regard to his reputation as a bringer of gifts, as well as through the attendance of Mass or worship services.
- `d8s2` Saint Nicholas Day [2]: In Europe, especially in "Germany and Poland, boys would dress as bishops begging alms for the poor."
- `d8s3` Saint Nicholas Day [3]: In Ukraine, children wait for St. Nicholas to come and to put a present under their pillows provided that the children were good during the year.
- `d8s4` Saint Nicholas Day [4]: Children who behaved badly may expect to find a twig or a piece of coal under their pillows.
- `d8s5` Saint Nicholas Day [5]: In the Netherlands, "Dutch children put out a clog filled with hay and a carrot for Saint Nicholas' horse.
- `d8s6` Saint Nicholas Day [6]: On Saint Nicholas' Day, gifts are tagged with personal humorous rhymes written by the sender."
- `d8s7` Saint Nicholas Day [7]: In the United States, one custom associated with Saint Nicholas Day is children leaving their shoes in the foyer on Saint Nicholas Eve in hope that Saint Nicholas will place some coins on the soles, for them to awake to.
- `d9s0` Fayard Nicholas [0]: Fayard Antonio Nicholas (October 20, 1914 – January 24, 2006) was an American choreographer, dancer and actor.
- `d9s1` Fayard Nicholas [1]: He and his younger brother Harold Nicholas made up the Nicholas Brothers tap-dance duo, who starred in the MGM musicals "An All-Colored Vaudeville Show" (1935), "Stormy Weather" (1943), "The Pirate" (1948), and "Hard Four" (2007).
- `d9s2` Fayard Nicholas [2]: The Nicholas brothers also starred in the 20th Century-Fox musicals "Down Argentine Way" (1940), "Sun Valley Serenade" (1941), and "Orchestra Wives" (1942).
- `d10s0` Moonstruck [0]: Moonstruck is a 1987 American romantic comedy film directed by Norman Jewison and written by John Patrick Shanley.
- `d10s1` Moonstruck [1]: It is about a widowed 37-year-old Italian-American woman (Cher) who falls in love with her fiancé's (Danny Aiello) estranged, hot-tempered younger brother (Nicolas Cage).
- `d10s2` Moonstruck [2]: Vincent Gardenia and Olympia Dukakis play supporting roles.

</details>

## Q200 — `hotpotqa_5a8a21a455429930ff3c0caf` (revised draft)

> On May 25, 2017 Greg Gianforte won the special election following the resignation of a politican that current holds what position?

Source answer: United States Secretary of the Interior

Gold final answer: United States Secretary of the Interior

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: politician whose resignation preceded Greg Gianforte's 2017 special-election win | false | Ryan Zinke | — | [d7s1] | — |
| u2: office held by {u1} in the historical source | true | United States Secretary of the Interior (accepted alternatives: Secretary of the Interior) | u1 | [d3s0] OR [d7s1] | — |

Evidence:

- `d3s0` Ryan Zinke [0]: Ryan Keith Zinke (born November 1, 1961) is an American politician and businessman who is currently the 52nd United States Secretary of the Interior, serving in the Trump administration.
- `d7s1` Greg Gianforte [1]: On May 25, 2017, he won the special election following Rep. Ryan Zinke's resignation to become Secretary of the Interior.

Notes:

- d7s1本来已支持u1，同时直接说明辞职后任Secretary of the Interior，补作u2备选；无需等d3s0扩展官职名称。

<details><summary>All source context</summary>

- `d1s0` Mike Aguirre [0]: Jules Michael Aguirre (born 1949), more commonly known as "Michael Jules Aguirre," was the City Attorney for the City of San Diego, California from 2004 to 2008.
- `d1s1` Mike Aguirre [1]: In 2013, he was a candidate for mayor in a special election following Mayor Bob Filner's resignation.
- `d2s0` Beth Turner [0]: Beth P. Turner (born 13 May 1958 in Maine) is an American politician from Maine.
- `d2s1` Beth Turner [1]: A Republican, Turner represents portions of Aroostook County and Penobscot County in the Maine House of Representatives.
- `d2s2` Beth Turner [2]: She was first elected in March 2011 in a special election following the death of Rep. Everett McLeod in December 2010.
- `d3s0` Ryan Zinke [0]: Ryan Keith Zinke (born November 1, 1961) is an American politician and businessman who is currently the 52nd United States Secretary of the Interior, serving in the Trump administration.
- `d3s1` Ryan Zinke [1]: Zinke served as the U.S. representative for Montana's at-large congressional district from 2015 until 2017.
- `d3s2` Ryan Zinke [2]: From 2009 to 2013, he served as a member of the Montana Senate, representing the 2nd district.
- `d4s0` David Jacoby [0]: David "Dave" Jacoby (born 1956) is the Iowa State Representative from the 30th District.
- `d4s1` David Jacoby [1]: A Democrat, he has served in the Iowa House of Representatives since 2003, when he was elected in a special election following the resignation of Dick Myers.
- `d5s0` Kevin Aguiar [0]: Kevin Aguiar is an American politician who represented the 7th Bristol district in the Massachusetts House of Representatives.
- `d5s1` Kevin Aguiar [1]: He was first elected in a 2008 special election following Robert Correia's resignation to become Mayor of Fall River, Massachusetts.
- `d5s2` Kevin Aguiar [2]: From 2002-2009, Aguiar served as a member of the Fall School Committee.
- `d5s3` Kevin Aguiar [3]: He was defeated for re-election in the 2012 Democratic primary by challenger Alan Silvia, who succeeded him.
- `d6s0` San Diego mayoral special election, 2005 [0]: The 2005 San Diego mayoral special election was a special election held on Tuesday, November 8, 2005, to elect the mayor for San Diego.
- `d6s1` San Diego mayoral special election, 2005 [1]: The special election was necessary due to the resignation of former Mayor Dick Murphy.
- `d7s0` Greg Gianforte [0]: Gregory Richard Gianforte (born April 17, 1961) is an American businessman, engineer, and politician who is the U.S. Representative for Montana's at-large congressional district.
- `d7s1` Greg Gianforte [1]: On May 25, 2017, he won the special election following Rep. Ryan Zinke's resignation to become Secretary of the Interior.
- `d7s2` Greg Gianforte [2]: Gianforte and his wife founded RightNow Technologies, a customer relationship management software company.
- `d8s0` Louisiana State Treasurer special election, 2017 [0]: The Louisiana State Treasurer special election will take place on October 14, 2017, to elect the State Treasurer of Louisiana, with a runoff election to be held on November 18, 2017, if necessary.
- `d8s1` Louisiana State Treasurer special election, 2017 [1]: Incumbent Republican State Treasurer John Kennedy was elected to the U.S. Senate in 2016.
- `d8s2` Louisiana State Treasurer special election, 2017 [2]: First Assistant Treasurer Ron Henson replaced Kennedy as Treasurer, and will serve until the special election.
- `d8s3` Louisiana State Treasurer special election, 2017 [3]: Henson will not run in the special election.
- `d9s0` Benjamin Peterson [0]: Ben Peterson, M.S.M., is a Canadian social entrepreneur and venture capitalist.
- `d9s1` Benjamin Peterson [1]: In 2002 he co-founded Journalists for Human Rights (JHR), a leading Canadian non-governmental organization (NGO), where he served as Executive Director until November 2011.
- `d9s2` Benjamin Peterson [2]: He now holds the position of "Chair Emeritus" at the charity.
- `d9s3` Benjamin Peterson [3]: In January 2012, he co-founded Newsana, an online news community.
- `d9s4` Benjamin Peterson [4]: He served as Newsana's CEO until September 2015, when the business was sold to a Toronto-based creative agency.
- `d9s5` Benjamin Peterson [5]: He current holds the position of Senior Partner at AHL Venture Partners, an impact-focused venture capital firm in Africa.
- `d10s0` Tony Yarber [0]: Tony Tarzell Yarber (born April 16, 1978) is an American pastor, educator and politician in Jackson, Mississippi.
- `d10s1` Tony Yarber [1]: In April 2014 he was elected as Mayor of Jackson in a special election following the death in office of Chokwe Lumumba.
- `d10s2` Tony Yarber [2]: A native of Jackson and experienced city councillor, Yarber is noted for his passion for youth causes, and has been described as "a consensus builder".
- `d10s3` Tony Yarber [3]: He was succeeded as Mayor of Jackson by his predecessor's son Chokwe Antar Lumumba on July 3, 2017.

</details>

## Q201 — `hotpotqa_5a7cbd7c554299452d57b9e6` (revised draft)

> Who was born first Neil LaBute or H. Bruce Humberstone?

Source answer: H. Bruce "Lucky" Humberstone

Gold final answer: H. Bruce Humberstone

Question type: `comparison` (source type `comparison`)

Replaces: `hotpotqa_5a8abb115542992d82986f66`

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: birth year of Neil LaBute | false | 1963 | — | [d8s0] | — |
| u2: birth year of H. Bruce Humberstone | false | 1901 | — | [d2s0] | — |
| u3: Who was born first Neil LaBute or H. Bruce Humberstone? | true | H. Bruce Humberstone (accepted alternatives: H. Bruce "Lucky" Humberstone) | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d2s0` H. Bruce Humberstone [0]: H. Bruce "Lucky" Humberstone (November 18, 1901 – October 11, 1984) was a movie actor (as a child), a script clerk, an assistant director, working with directors such as King Vidor, Edmund Goulding and Allan Dwan and, ultimately, a director.
- `d8s0` Neil LaBute [0]: Neil N. LaBute (born March 19, 1963) is an American film director, screenwriter, playwright and actor.

Notes:

- 替换：没有县与镇的政府层级规则，不能从两地所有者直接推出higher。 新题保留原source type，人工核对两条显式事实及答案。

<details><summary>All source context</summary>

- `d1s0` The Shape of Things [0]: The Shape of Things is a 2001 play by American author and film director Neil LaBute and a 2003 American romantic drama film.
- `d1s1` The Shape of Things [1]: It premièred at the Almeida Theatre, London in 2001 with Paul Rudd as Adam, Rachel Weisz as Evelyn, Gretchen Mol as Jenny, and Fred Weller as Phillip.
- `d1s2` The Shape of Things [2]: The play was directed by LaBute himself.
- `d1s3` The Shape of Things [3]: According to the author's instructions, it is to be performed without an interval or a curtain call.
- `d2s0` H. Bruce Humberstone [0]: H. Bruce "Lucky" Humberstone (November 18, 1901 – October 11, 1984) was a movie actor (as a child), a script clerk, an assistant director, working with directors such as King Vidor, Edmund Goulding and Allan Dwan and, ultimately, a director.
- `d3s0` Tarzan and the Lost Safari [0]: Tarzan and the Lost Safari (1957) is an action adventure film featuring Edgar Rice Burroughs' famous jungle hero Tarzan and starring Gordon Scott, Robert Beatty, Yolande Donlan and Betta St. John.
- `d3s1` Tarzan and the Lost Safari [1]: The movie was directed by H. Bruce Humberstone, and was the first Tarzan movie released in color, Eastman Color.
- `d3s2` Tarzan and the Lost Safari [2]: It was also MGM's first "Tarzan" film since 1942 and filmed in Nairobi, British East Africa.
- `d3s3` Tarzan and the Lost Safari [3]: The character of Jane does not appear in this motion picture.
- `d4s0` Charlie Chan in Honolulu [0]: Charlie Chan in Honolulu is a 1938 American film directed by H. Bruce Humberstone, starring Sidney Toler as the fictional Chinese-American detective Charlie Chan.
- `d4s1` Charlie Chan in Honolulu [1]: The film is the first appearance of both Toler as Chan and Victor Sen Yung as "number two son" Jimmy.
- `d5s0` In the Company of Men [0]: In the Company of Men is a 1997 Canadian/American black comedy written and directed by Neil LaBute and starring Aaron Eckhart, Matt Malloy, and Stacy Edwards.
- `d5s1` In the Company of Men [1]: The film, which was adapted from a play written by LaBute, and served as his feature film debut, won him the Independent Spirit Award for Best First Screenplay.
- `d6s0` If I Had a Million [0]: If I Had a Million is a 1932 American pre-Code Paramount Studios anthology film.
- `d6s1` If I Had a Million [1]: There were seven directors: Ernst Lubitsch, Norman Taurog, Stephen Roberts, Norman Z. McLeod, James Cruze, William A. Seiter, and H. Bruce Humberstone.
- `d6s2` If I Had a Million [2]: Lubitsch, Cruze, Seiter, and Humberstone were each responsible for a single vignette, Roberts and McLeod directed two each, and Taurog was in charge of the prologue and epilogue.
- `d6s3` If I Had a Million [3]: The screenplays were scripted by many different writers, with Joseph L. Mankiewicz making a large contribution.
- `d6s4` If I Had a Million [4]: "If I Had a Million" is based on a novel by Robert Hardy Andrews.
- `d7s0` She's Working Her Way Through College [0]: She's Working Her Way Through College is a 1952 American comedy film produced by Warner Bros. A musical comedy in Technicolor, it was directed by H. Bruce Humberstone, and starred Virginia Mayo and Ronald Reagan.
- `d7s1` She's Working Her Way Through College [1]: "She's Working Her Way through College" is adapted quite loosely from the 1942 film of James Thurber's and Elliott Nugent's First Amendment comedy/drama "The Male Animal" that starred Olivia de Havilland and Henry Fonda and which, in turn, was based on the 1940 Broadway play of the same name and written by the same authors.
- `d8s0` Neil LaBute [0]: Neil N. LaBute (born March 19, 1963) is an American film director, screenwriter, playwright and actor.
- `d8s1` Neil LaBute [1]: He is best-known for a play that he wrote and later turned into a film, "In the Company of Men" (1997), which won awards from the Sundance Film Festival, the Independent Spirit Awards, and the New York Film Critics Circle.
- `d8s2` Neil LaBute [2]: He wrote and directed the films "Possession" (2002) (based on the A.S. Byatt novel), "The Shape of Things" (2003) (based on his play of the same name), "The Wicker Man" (2006), "Some Velvet Morning" (2013), and "Dirty Weekend" (2015).
- `d8s3` Neil LaBute [3]: He directed the films "Nurse Betty" (2000), "Lakeview Terrace" (2008), and "Death at a Funeral" (2010).
- `d8s4` Neil LaBute [4]: LaBute created the TV series "Billy & Billie", writing and directing all of the episodes and is also creator of "Van Helsing".
- `d8s5` Neil LaBute [5]: He also directed several episodes for shows such as "Hell on Wheels" and "Billions".
- `d9s0` Some Girl(s) (film) [0]: Some Girl(s) is a 2013 American comedy film directed by Daisy von Scherler Mayer and written by Neil LaBute.
- `d9s1` Some Girl(s) (film) [1]: It is based on the play of the same name, also written by LaBute.
- `d9s2` Some Girl(s) (film) [2]: The film stars Adam Brody, Kristen Bell, Zoe Kazan, Mía Maestro, Jennifer Morrison and Emily Watson.
- `d9s3` Some Girl(s) (film) [3]: The film was released on June 26, 2013, by Leeden Media.
- `d10s0` Happy Go Lovely [0]: Happy Go Lovely is a 1951 British musical comedy film with Technicolor, directed by H. Bruce Humberstone and starring Vera Ellen, David Niven, and Cesar Romero.
- `d10s1` Happy Go Lovely [1]: The film was made and first released in the UK, and distributed in the US by RKO Radio Pictures in 1952.

</details>

## Q202 — `hotpotqa_5a8af94455429971feec45b6` (revised draft)

> Jon S. Cardin is the nephew of a senator who has been in office since when ?

Source answer: since 2007

Gold final answer: since 2007

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: senator who is Jon S. Cardin's uncle | false | Ben Cardin | — | [d8s3] | — |
| u2: start of {u1}'s service as U.S. Senator | true | since 2007 (accepted alternatives: 2007) | u1 | [d6s0] | — |

Evidence:

- `d6s0` Ben Cardin [0]: Benjamin Louis Cardin (born October 5, 1943) is an American politician and member of the Democratic Party who serves as the senior United States Senator from Maryland, in office since 2007.
- `d8s3` Jon S. Cardin [3]: Cardin is the nephew of Ben Cardin, a United States Senator from Maryland.

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` List of United States Senators from Utah [0]: Utah was admitted to the Union on January 4, 1896, and elects senators to Class 1 and Class 3.
- `d1s1` List of United States Senators from Utah [1]: Its current senators are Republicans Mike Lee and Orrin Hatch.
- `d1s2` List of United States Senators from Utah [2]: In office since 1977, Hatch is currently the longest-serving Senator in Utah history, the longest-serving Republican Senator and the second most senior Senator overall, after Vermont's Patrick Leahy.
- `d1s3` List of United States Senators from Utah [3]: Senator Hatch has also been the President pro tempore of the United States Senate since 2015.
- `d2s0` Penland Post Office and General Store [0]: Penland Post Office and General Store, also known as Bailey Lumber Company Office Building and Bailey Lumber Company Office and General Merchandise Store, is a historic post office and general store located at Penland, Mitchell County, North Carolina.
- `d2s1` Penland Post Office and General Store [1]: It was built about 1900, and is a long, one-story, frame building with a front-gable roof and rough-sawn board and batten siding.
- `d2s2` Penland Post Office and General Store [2]: The building housed the office and store of the Bailey Lumber Company from about 1900 to 1916, and a general store from about 1902 to 1974.
- `d2s3` Penland Post Office and General Store [3]: It has housed the Penland post office since 1934 and is the oldest active post office facility in Mitchell County and is the county’s last remaining Fourth Class post office.
- `d3s0` Pat Toomey [0]: Patrick Joseph Toomey (born November 17, 1961) is an American businessman, politician, and the junior United States Senator from Pennsylvania, in office since 2011.
- `d3s1` Pat Toomey [1]: A member of the Republican Party, Toomey served as the United States Representative for Pennsylvania 's 15 congressional district for three terms, from 1999 to 2005, but he did not seek a fourth term in compliance with a term limits pledge he had made while running for office in 1998.
- `d4s0` Texas Senate, District 24 [0]: District 24 of the Texas Senate is a senatorial district that currently serves Bell, Blanco, Brown, Burnet, Callahan, Coleman, Comanche, Eastland, Erath, Gillespie, Hamilton, Kerr, Kimble, Lampasas, Llano, Mason, McCulloch, Menard, Mills, San Saba and Taylor counties in the U.S. state of Texas.
- `d4s1` Texas Senate, District 24 [1]: The current Senator from District 24 is Republican Troy Fraser who has held the office since 1997.
- `d4s2` Texas Senate, District 24 [2]: In 2015, he announced his intention to retire from the office in January 2017.
- `d5s0` Dick Durbin [0]: Richard Joseph Durbin (born November 21, 1944) is an American politician who is the senior United States Senator from Illinois, in office since 1997.
- `d5s1` Dick Durbin [1]: He has been the Assistant Democratic Leader (whip), the second highest position in the Democratic Party leadership in the Senate, since 2005, serving as Minority Whip from 2005 to 2007, Majority Whip from 2007 to 2015, and Minority Whip again since 2015.
- `d6s0` Ben Cardin [0]: Benjamin Louis Cardin (born October 5, 1943) is an American politician and member of the Democratic Party who serves as the senior United States Senator from Maryland, in office since 2007.
- `d6s1` Ben Cardin [1]: Before his election to the Senate, Cardin was previously a member of the United States House of Representatives, representing  's 3 congressional district (1987–2007).
- `d6s2` Ben Cardin [2]: He also served in the Maryland House of Delegates (1967–87), serving as Speaker (1979–87).
- `d6s3` Ben Cardin [3]: He was the youngest Speaker in Maryland history.
- `d6s4` Ben Cardin [4]: In half a century as an elected official, he has never lost an election.
- `d7s0` John Hoeven [0]: John Henry Hoeven III (born March 13, 1957) is an American politician and the senior United States Senator from North Dakota, in office since 2011.
- `d7s1` John Hoeven [1]: A member of the North Dakota Republican Party, he previously served as the 31st Governor of North Dakota from December 2000 to December 2010.
- `d7s2` John Hoeven [2]: Hoeven was elected to the U.S. Senate in the November 2, 2010 general election.
- `d7s3` John Hoeven [3]: He replaced junior Senator Byron L. Dorgan, who chose not to seek re-election.
- `d7s4` John Hoeven [4]: Hoeven became the senior Senator in 2013 after Kent Conrad retired and was replaced by Heidi Heitkamp, who was once Hoeven's opponent for the Governor's office.
- `d8s0` Jon S. Cardin [0]: Jon S. Cardin (born January 12, 1970) is an American politician from Maryland and a member of the Democratic Party.
- `d8s1` Jon S. Cardin [1]: Previously he served in the Maryland House of Delegates, representing Maryland's District 11 in Baltimore County, and was a member of the Ways and Means Committee.
- `d8s2` Jon S. Cardin [2]: Cardin chaired the Election Law Subcommittee.
- `d8s3` Jon S. Cardin [3]: Cardin is the nephew of Ben Cardin, a United States Senator from Maryland.
- `d9s0` Rob Portman [0]: Robert Jones Portman (born December 19, 1955) is an American lawyer and the junior United States Senator from Ohio, and a member of the Republican Party.
- `d9s1` Rob Portman [1]: He has been in office since 2011.
- `d9s2` Rob Portman [2]: Previously he served as a congressman, as the 14th United States Trade Representative, and as the 35th Director of the Office of Management and Budget.
- `d10s0` Eddie Baza Calvo [0]: Edward Jerome "Eddie" Baza Calvo (born August 29, 1961) is an American Guamanian politician, the eighth and current Governor of the United States territory of Guam, in office since 2011.
- `d10s1` Eddie Baza Calvo [1]: A member of the Republican Party, Calvo was a five-term Senator within the Legislature of Guam.
- `d10s2` Eddie Baza Calvo [2]: He became the Governor of Guam, having defeated Democrat Carl Gutierrez in the 2010 gubernatorial election.
- `d10s3` Eddie Baza Calvo [3]: Calvo chose Senator Ray Tenorio as his running mate for Lieutenant Governor of Guam.

</details>

## Q203 — `hotpotqa_5a8b036d55429971feec45fe` (revised draft)

> Which is a record producer, Zach Bogosian or Daron Malakian?

Source answer: Daron Vartan Malakian

Gold final answer: Daron Vartan Malakian

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: whether Zach Bogosian is a record producer | false | no **[by_omission]** | — | [d5s0, d5s1] | — |
| u2: whether Daron Malakian is a record producer | false | yes | — | [d8s0] | — |
| u3: Which is a record producer, Zach Bogosian or Daron Malakian? | true | Daron Vartan Malakian (accepted alternatives: Daron Malakian) **[by_presupposition]** | u1, u2 | `[[]]`：由全部依赖推出 | [d5s0, d5s1] OR [d8s0] |

Evidence:

- `d5s0` Zach Bogosian [0]: Zachary M. Bogosian (Armenian: Զաքարի Մ.
- `d5s1` Zach Bogosian [1]: Պողոսյան , born July 15, 1990) is an American professional ice hockey defenseman currently playing for the Buffalo Sabres.
- `d8s0` Daron Malakian [0]: Daron Vartan Malakian (Armenian: Տարօն/Տարոն Վարդան Մալաքեան, born July 18, 1975) is an Armenian–American singer-songwriter, multi-instrumentalist, and record producer.

Notes:

- 按SFT两候选格式补建Bogosian的职业排除unit；确认与排除各自可完成结论，补短名别名。

<details><summary>All source context</summary>

- `d1s0` Bad Acid Trip [0]: Bad Acid Trip is an American metal band, currently signed to System of a Down lead singer Serj Tankian's record label, Serjical Strike Records.
- `d1s1` Bad Acid Trip [1]: Their 2004 album, "Lynch the Weirdo", was produced by Daron Malakian, another System of a Down member.
- `d1s2` Bad Acid Trip [2]: In 2006 they performed on the second stage at the Ozzfest summer tour.
- `d1s3` Bad Acid Trip [3]: The band has three full-length releases ("For the Weird by the Weird", "Lynch the Weirdo", and "Humanly Possible") and multiple EPs.
- `d2s0` Zach Crowell [0]: Zach Crowell is a Grammy Award-winning songwriter and record producer, who was born and raised in Nashville, Tennessee.
- `d2s1` Zach Crowell [1]: Crowell is involved in a joint publishing deal with Warner/Chappell Music, Combustion Music and Taperoom Music.
- `d3s0` Eusonia Records [0]: Eusonia Records is an independent record label founded by American record producer, songwriter and multi-intrumentalist Scott Jacoby.
- `d3s1` Eusonia Records [1]: The label currently has four artists on its roster: Maiysha, SiLyA, Zach Deputy and Jacoby himself, as well as the soundtrack for the 2013 film "My Last Day Without You".
- `d4s0` Daron Jones [0]: Daron Tavaris Jones (born December 27, 1976) is an American singer-songwriter, record producer.
- `d4s1` Daron Jones [1]: He is a member in Bad Boy Records group 112.
- `d4s2` Daron Jones [2]: His debut solo album titled "Uncensored" was released December 5, 2010.
- `d4s3` Daron Jones [3]: The first single from the album is the digitally-released "Money."
- `d4s4` Daron Jones [4]: Daron digitally released "Christmas in Atlanta" in December 2014, which reached the top 30 on the iTunes R&B chart.
- `d4s5` Daron Jones [5]: Daron is currently in the studio working on new music.
- `d5s0` Zach Bogosian [0]: Zachary M. Bogosian (Armenian: Զաքարի Մ.
- `d5s1` Zach Bogosian [1]: Պողոսյան , born July 15, 1990) is an American professional ice hockey defenseman currently playing for the Buffalo Sabres.
- `d5s2` Zach Bogosian [2]: Bogosian attended Cushing Academy in Massachusetts before he joined the Peterborough Petes of the Ontario Hockey League (OHL) in 2006.
- `d5s3` Zach Bogosian [3]: He played two seasons in the OHL, and was nominated for the Red Tilson Trophy as the league's most outstanding player in his second season.
- `d5s4` Zach Bogosian [4]: Bogosian was regarded as a complete, physical defenseman who could contribute on both offense and defense; he was rated as one of the top players heading into the 2008 NHL Entry Draft, where the Atlanta Thrashers selected him third overall.
- `d5s5` Zach Bogosian [5]: He signed a contract with the team a few weeks after the draft and began the season with the Thrashers, though he missed several weeks of his rookie year due to injury.
- `d5s6` Zach Bogosian [6]: In his second season, he tied a team record for goals by a defenseman.
- `d5s7` Zach Bogosian [7]: Bogosian first played in an international tournament when he joined the American national team at the 2009 IIHF World Championship.
- `d6s0` Raleigh Moncrief [0]: Raleigh Moncrief is an American electronic musician, record producer and recording engineer who has worked with Zach Hill, Dirty Projectors and !!!
- `d6s1` Raleigh Moncrief [1]: .
- `d7s0` Odell Borg [0]: Odell Borg is a native flute maker, teacher, and record producer.
- `d7s1` Odell Borg [1]: He has produced records with Jan 'Looking Wolf', Zach Farley, Harry Seavey, Travis Terry, and Naomi Littletree.
- `d7s2` Odell Borg [2]: Before making flutes, Odell was a leather craftsman and a draftsman.
- `d7s3` Odell Borg [3]: In 1988, Odell received his first native flute as a gift, and after a few of years playing it he began making flutes of his own.
- `d8s0` Daron Malakian [0]: Daron Vartan Malakian (Armenian: Տարօն/Տարոն Վարդան Մալաքեան, born July 18, 1975) is an Armenian–American singer-songwriter, multi-instrumentalist, and record producer.
- `d8s1` Daron Malakian [1]: He is best known as the guitarist, songwriter and second vocalist of the rock band System of a Down and as the lead vocalist, lead guitarist and songwriter of the band Scars on Broadway.
- `d8s2` Daron Malakian [2]: Like the rest of the Hollywood-based band System of a Down, he is of Armenian ancestry, but he is the only member to have been born in the United States.
- `d8s3` Daron Malakian [3]: Daron Malakian is known for his distinctive playing and is ranked 40th in Loudwire's list of "Top 50 Hard Rock + Metal Guitarists Of All Time" and #11 in MusicRadar's poll, "The 20 Greatest Metal Guitarists Ever".
- `d8s4` Daron Malakian [4]: He is placed 30th in Guitar World's List of The 100 Greatest Heavy Metal Guitarists of All Time.

</details>

## Q204 — `hotpotqa_5a8b78f055429971feec471a` (revised draft)

> Was Steve Sekely and Willian King Baggot known by multiple names or nicknames?

Source answer: yes

Gold final answer: yes

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: whether Steve Sekely was known by several names | false | yes | — | [d3s1] | — |
| u2: whether King Baggot was known by multiple nicknames | false | yes | — | [d4s2] | — |
| u3: Was Steve Sekely and Willian King Baggot known by multiple names or nicknames? | true | yes | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d3s1` Steve Sekely [1]: Born Székely István, he was known by several names, based on his changing professional and immigration status, including Stefan Szekely.
- `d4s2` King Baggot [2]: The first individually publicized leading man in America, Baggot was referred to as "King of the Movies," "The Most Photographed Man in the World" and "The Man Whose Face Is As Familiar As The Man In The Moon."

Notes:

- 无待处理note，保留原标注。

<details><summary>All source context</summary>

- `d1s0` Lady in the Death House [0]: Lady in the Death House is a 1944 American film directed by Steve Sekely, starring Jean Parker and Lionel Atwill.
- `d2s0` Flying Gold [0]: Flying Gold (Hungarian: Repülő arany or Repülö arany) is a 1932 Hungarian crime film directed by Steve Sekely and starring Steven Geray, Gyula Kabos and Lajos Gárday.
- `d2s1` Flying Gold [1]: A shipment of gold being flown from Paris to Budapest is robbed in mid-air.
- `d2s2` Flying Gold [2]: A French-language version "Rouletabille aviateur" was also released.
- `d3s0` Steve Sekely [0]: Steve Sekely (1899-1979) was a Hungarian film director.
- `d3s1` Steve Sekely [1]: Born Székely István, he was known by several names, based on his changing professional and immigration status, including Stefan Szekely.
- `d4s0` King Baggot [0]: William King Baggot (November 7, 1879 – July 11, 1948) was an American actor, film director and screenwriter.
- `d4s1` King Baggot [1]: He was an internationally famous movie star of the silent film era.
- `d4s2` King Baggot [2]: The first individually publicized leading man in America, Baggot was referred to as "King of the Movies," "The Most Photographed Man in the World" and "The Man Whose Face Is As Familiar As The Man In The Moon."
- `d5s0` The Fabulous Suzanne [0]: The Fabulous Suzanne is a 1946 American romantic comedy film directed by Steve Sekely and starring Barbara Britton, Rudy Vallee and Otto Kruger.
- `d5s1` The Fabulous Suzanne [1]: A waitress inherits a fortune from one of her customers.
- `d6s0` Number 111 (1938 film) [0]: Number 111 is a 1938 Hungarian thriller film directed by Steve Sekely and starring Jenő Törzs, Pál Jávor and Mária Lázár.
- `d6s1` Number 111 (1938 film) [1]: It is a remake of the 1919 film "Number 111", directed by Alexander Korda, which was itself an adaptation of a novel by Jenő Heltai.
- `d7s0` Cafe Moscow [0]: Cafe Moscow (Hungarian:Café Moszkva) is a 1936 Hungarian adventure film directed by Steve Sekely and starring Anna Tõkés, Gyula Csortos and Ferenc Kiss.
- `d7s1` Cafe Moscow [1]: Art direction was by József Pán.
- `d7s2` Cafe Moscow [2]: It is also known by the alternative title Only One Night.
- `d7s3` Cafe Moscow [3]: The film is set during the First World War on the Eastern Front between Russia and the Austro-Hungarian Empire.
- `d7s4` Cafe Moscow [4]: The film was intended to convey an anti-war message.
- `d8s0` A Tremendously Rich Man [0]: A Tremendously Rich Man (German: Ein steinreicher Mann) is a 1932 German comedy film directed by Steve Sekely and starring Curt Bois, Dolly Haas and Adele Sandrock.
- `d8s1` A Tremendously Rich Man [1]: It premiered on 13 February 1932.
- `d8s2` A Tremendously Rich Man [2]: The film was a co-production between the German subsidiary of Universal Pictures and the German firm Tobis Film.
- `d9s0` King Baggot (cinematographer) [0]: Stephen King Baggot, A.S.C. (born August 15, 1943) is an American cinematographer.
- `d9s1` King Baggot (cinematographer) [1]: Baggot is a member of the American Society of Cinematographers.
- `d9s2` King Baggot (cinematographer) [2]: He is the grandson of actor/director of the early 20th century, King Baggot.
- `d10s0` Emmy (film) [0]: Emmy is a 1934 Hungarian comedy film directed by Steve Sekely and starring Gábor Rajnay, Irén Ágay and Ella Gombaszögi.
- `d10s1` Emmy (film) [1]: It is based on a novel by Viktor Rákosi.

</details>

## Q205 — `hotpotqa_5a79f2185542996a35c1703d` (revised draft)

> Who was born first George Marshall or Allan Dwan ?

Source answer: Allan Dwan

Gold final answer: Allan Dwan

Question type: `comparison` (source type `comparison`)

Replaces: `hotpotqa_5a8baf4b5542996e8ac889c5`

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: birth year of George Marshall | false | 1891 | — | [d4s0] | — |
| u2: birth year of Allan Dwan | false | 1885 | — | [d9s0] | — |
| u3: Who was born first George Marshall or Allan Dwan ? | true | Allan Dwan | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d4s0` George Marshall (director) [0]: George E. Marshall (December 29, 1891 – February 17, 1975) was an American actor, screenwriter, producer, film and television director, active through the first six decades of movie history.
- `d9s0` Allan Dwan [0]: Allan Dwan (3 April 1885 – 28 December 1981) was a pioneering Canadian-born American motion picture director, producer and screenwriter.

Notes:

- 替换：bimonthly在上下文未消歧，无法确定比monthly多还是少。 新题保留原source type，人工核对两条显式事实及答案。

<details><summary>All source context</summary>

- `d1s0` The Conspiracy (1914 film) [0]: The Conspiracy is a 1914 American drama silent film directed by Allan Dwan and written by Robert M. Baker, Allan Dwan and John Emerson.
- `d1s1` The Conspiracy (1914 film) [1]: The film stars John Emerson, Lois Meredith, Harold Lockwood, Iva Shepard, Francis Byrne and Hal Clarendon.
- `d1s2` The Conspiracy (1914 film) [2]: The film was released on December 10, 1914, by Paramount Pictures.
- `d2s0` The Unwelcome Mrs. Hatch [0]: The Unwelcome Mrs. Hatch is a 1914 American drama film directed by Allan Dwan and written by Allan Dwan and Mrs. Burton Harrison.
- `d2s1` The Unwelcome Mrs. Hatch [1]: The film stars Henrietta Crosman, Walter Craven, Lorraine Huling, Minna Gale and Harold Lockwood.
- `d2s2` The Unwelcome Mrs. Hatch [2]: The film was released on September 10, 1914, by Paramount Pictures.
- `d3s0` The Unlawful Trade [0]: The Unlawful Trade is a 1914 American silent short drama film directed by Allan Dwan and starring Pauline Bush, William Lloyd, George Cooper, and Lon Chaney.
- `d3s1` The Unlawful Trade [1]: George Cooper and directed Allan Dwan also wrote the script.
- `d3s2` The Unlawful Trade [2]: The film is now considered lost.
- `d4s0` George Marshall (director) [0]: George E. Marshall (December 29, 1891 – February 17, 1975) was an American actor, screenwriter, producer, film and television director, active through the first six decades of movie history.
- `d5s0` David Harum (1915 film) [0]: David Harum is a 1915 American silent comedy-drama romance film written and directed by Allan Dwan, produced by Famous Players Film Company and distributed by Paramount Pictures.
- `d5s1` David Harum (1915 film) [1]: It is based on the 1899 novel of the same name by Edward Noyes Westcott and the 1900 Broadway play based on the novel, starring William H. Crane (Crane also starred in two subsequent Broadway revivals).
- `d5s2` David Harum (1915 film) [2]: Crane agreed to star in the film (which was his debut) only if the film was written exactly as the play.
- `d5s3` David Harum (1915 film) [3]: "David Harum" is the only film of Dwan's for Famous Players that still survives.
- `d5s4` David Harum (1915 film) [4]: A print is preserved at the George Eastman House in Rochester, New York and the Cinémathèque Française in Paris.
- `d6s0` Abroad with Two Yanks [0]: Abroad with Two Yanks is a 1944 American comedy film directed by Allan Dwan and starring Helen Walker, William Bendix and Dennis O'Keefe as the title characters.
- `d6s1` Abroad with Two Yanks [1]: It was Bendix's third and final role in a film as a US Marine and the first of Dwan's three films about the United States Marine Corps.
- `d7s0` 15 Maiden Lane [0]: 15 Maiden Lane is a 1936 American crime film directed by Allan Dwan and starring Claire Trevor and Cesar Romero, with Lloyd Nolan.
- `d7s1` 15 Maiden Lane [1]: The plot involves an insurance investigator (Trevor) who infiltrates a gang who had stolen jewels from the eponymous building on Maiden Lane in the Fulton Street District of Manhattan.
- `d7s2` 15 Maiden Lane [2]: The neighborhood had been the center of New York City's Diamond District since the 19th century before its gradual relocation uptown to 47th Street after World War II.
- `d7s3` 15 Maiden Lane [3]: The Museum of Modern Art in New York City screened a restored print of the film in June 2013 as part of an Allan Dwan retrospective.
- `d8s0` South Sea Rose [0]: South Sea Rose is a 1929 American comedy-drama film distributed by the Fox Film Corporation and produced and directed by Allan Dwan.
- `d8s1` South Sea Rose [1]: This picture was Dwan's second collaboration with star Lenore Ulric, their first being "Frozen Justice".
- `d8s2` South Sea Rose [2]: Much of the cast and crew on "Frozen Justice" returned for this film.
- `d9s0` Allan Dwan [0]: Allan Dwan (3 April 1885 – 28 December 1981) was a pioneering Canadian-born American motion picture director, producer and screenwriter.
- `d10s0` The Habit of Happiness [0]: The Habit of Happiness is a 1916 American silent comedy film directed by Allan Dwan and filmed by cinematographer Victor Fleming.
- `d10s1` The Habit of Happiness [1]: The film was written by Allan Dwan and Shannon Fife from a suggestion by D. W. Griffith and stars Douglas Fairbanks.
- `d10s2` The Habit of Happiness [2]: A 16mm print of the film is preserved in a private collection.

</details>

## Q206 — `hotpotqa_5a8bc1565542996e8ac88a0c` (revised draft)

> In January 2014, what election did Bob Beers announce he would enter against Senator Harry Reid in Nevada?

Source answer: The 2016 United States Senate election

Gold final answer: 2016 U.S. Senate election

Question type: `single` (source type `bridge`)

Original question: What election was Senator Harry Reid at in Nevada?

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: election Bob Beers announced in January 2014 he would enter against Harry Reid | true | 2016 U.S. Senate election (accepted alternatives: The 2016 United States Senate election; 2016 United States Senate election in Nevada) | — | [d9s2] | — |

Evidence:

- `d9s2` Bob Beers (Nevada) [2]: He ran unsuccessfully for the Republican nomination for Governor of Nevada in 2006 and in January 2014, he announced that he would run against Democratic Senator Harry Reid in the 2016 U.S. Senate election, but he withdrew from the race in June 2015.

Notes:

- 题干澄清：将含混的was at限定为原文记载的2014年竞选宣布，不暗示实际参加或出席2016年选举。
- 删除全名桥接，d9s2即可回答；保留完整选举名称为别名。

<details><summary>All source context</summary>

- `d1s0` Political positions of Harry Reid [0]: Former United States Senator Harry Reid has declared his position on many political issues through his public comments and his senatorial voting record.
- `d2s0` Dean Rhoads [0]: Dean Rhoads is a Republican member of the Nevada Senate, representing the Northern Nevada District (map) since 1984.
- `d2s1` Dean Rhoads [1]: Previously he served in the Nevada Assembly from 1976 through 1982.
- `d2s2` Dean Rhoads [2]: In October 2010, Senator Rhoads broke with the Republican establishment to endorse Harry Reid over Sharon Angle in that year's Senate Race.
- `d3s0` United States Senate election in Nevada, 1992 [0]: The 1992 United States Senate election in Nevada was held on November 3, 1992.
- `d3s1` United States Senate election in Nevada, 1992 [1]: Although nearly 10% of the electorate voted for neither of the two major U.S. political parties, incumbent Democratic U.S. Senator Harry Reid ultimately won a majority of votes cast and, with that, re-election to a second term.
- `d4s0` United States Senate election in Nevada, 1998 [0]: The 1998 United States Senate election in Nevada was held on November 3, 1998.
- `d4s1` United States Senate election in Nevada, 1998 [1]: Incumbent Democratic U.S. Senator Harry Reid won re-election to a third term.
- `d5s0` Bill Clinton judicial appointment controversies [0]: During President Bill Clinton's first and second terms of office, he nominated 24 people for 20 federal appellate judgeships but the nominees were not processed by the Republican-controlled Senate Judiciary Committee.
- `d5s1` Bill Clinton judicial appointment controversies [1]: Three of the nominees who were not processed (Christine Arguello, Andre M. Davis and S. Elizabeth Gibson) were nominated after July 1, 2000, the traditional start date of the unofficial Thurmond Rule during a presidential election year.
- `d5s2` Bill Clinton judicial appointment controversies [2]: Democrats claim that Senate Republicans of the 106th Congress purposely tried to keep open particular judgeships as a political maneuver to allow a future Republican president to fill them.
- `d5s3` Bill Clinton judicial appointment controversies [3]: Of the 20 seats in question, four were eventually filled with different Clinton nominees, fourteen were later filled with Republican nominees by President George W. Bush and two continued to stay open during Bush's presidency.
- `d5s4` Bill Clinton judicial appointment controversies [4]: Senator Harry Reid, the Democratic leader of the United States Senate during the 110th Congress, and Senator Patrick Leahy, the Democratic leader of the Senate Judiciary Committee under Reid, repeatedly mentioned the controversy over President Clinton's court of appeals nominees during the controversy involving the confirmation of Republican court of appeals nominees during the last two years of Bush's second term.
- `d5s5` Bill Clinton judicial appointment controversies [5]: Republicans claimed that Democrats were refusing to confirm certain longstanding Bush nominees in order to allow a future Democratic president in 2009 to fill those judgeships.
- `d6s0` Lula J. Davis [0]: Lula Johnson Davis was Secretary for the Majority of the United States Senate from 2008 to 2011.
- `d6s1` Lula J. Davis [1]: Davis was born in Louisiana.
- `d6s2` Lula J. Davis [2]: She received a B.S. in office administration and an M.Ed., in guidance counseling from Southern University in Baton Rouge, Louisiana.
- `d6s3` Lula J. Davis [3]: She began her career with the Senate as a legislative correspondent for Senator Russell B. Long of Louisiana.
- `d6s4` Lula J. Davis [4]: After Senator Long retired from the Senate in January 1987, Davis worked as an office assistant for the Democratic Policy Committee’s Senate floor staff office.
- `d6s5` Lula J. Davis [5]: In 1993, she became a member of the Democratic floor staff.
- `d6s6` Lula J. Davis [6]: In 1995, she was promoted to chief floor assistant.
- `d6s7` Lula J. Davis [7]: In 1997, she assumed the position of assistant secretary.
- `d6s8` Lula J. Davis [8]: After the retirement of Martin P. Paone, in January 2008, the Senate elected Davis Secretary for the Majority.
- `d6s9` Lula J. Davis [9]: As Secretary for the Majority, she was a senior procedural advisor to the Senate Majority Leader, Senator Harry Reid, and supervised the day-to-day Senate schedule.
- `d6s10` Lula J. Davis [10]: In so doing, she often worked with Secretary for the Minority David J. Schiappa.
- `d6s11` Lula J. Davis [11]: Davis told Senators what they could and could not do when it came to rules and procedure.
- `d6s12` Lula J. Davis [12]: Consequently, Davis was called “one of the most powerful unelected people in the U.S. Senate.”
- `d6s13` Lula J. Davis [13]: Davis retired at the end of the 111th Congress.
- `d7s0` United States Senate election in Nevada, 2016 [0]: The 2016 United States Senate election in Nevada was held on November 8, 2016 to elect a member of the United States Senate to represent the State of Nevada, concurrently with the 2016 U.S. presidential election, as well as other elections to the United States Senate in other states and elections to the United States House of Representatives and various state and local elections.
- `d7s1` United States Senate election in Nevada, 2016 [1]: The state primary election was held on June 14, 2016.
- `d8s0` United States Senate election in Nevada, 2004 [0]: The 2004 United States Senate election in Nevada was held on November 2, 2004.
- `d8s1` United States Senate election in Nevada, 2004 [1]: Incumbent Democratic U.S. Senator Harry Reid, the Senate Minority Whip, won re-election to a fourth term.
- `d9s0` Bob Beers (Nevada) [0]: Robert T. Beers (born October 14, 1959) is an American accountant (CPA) and member of the Republican Party who currently serves as a member of the Las Vegas City Council, representing Ward 2.
- `d9s1` Bob Beers (Nevada) [1]: He was previously a member of the Nevada Assembly from 1998 to 2004 and the Nevada Senate from 2005 to 2008.
- `d9s2` Bob Beers (Nevada) [2]: He ran unsuccessfully for the Republican nomination for Governor of Nevada in 2006 and in January 2014, he announced that he would run against Democratic Senator Harry Reid in the 2016 U.S. Senate election, but he withdrew from the race in June 2015.
- `d10s0` Rory Reid [0]: Rory Jason Reid (born July 11, 1963) is an American attorney and politician.
- `d10s1` Rory Reid [1]: He served as elected Chairman of the Clark County Commission in Clark County, Nevada and was the Democratic nominee for Governor of Nevada in the 2010 gubernatorial election.
- `d10s2` Rory Reid [2]: Reid is a member of the Democratic Party and a son of former United States Senator Harry Reid.
- `d10s3` Rory Reid [3]: In 2007, the "Las Vegas Sun" called Reid a political "rising star" in Nevada.

</details>

## Q207 — `hotpotqa_5a8c5569554299240d9c2126` (revised draft)

> Are Daryl Hall and Gerry Marsden both musicians?

Source answer: yes

Gold final answer: yes

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: musical occupations of Daryl Hall | false | singer, keyboardist, guitarist, songwriter, producer | — | [d6s0] | — |
| u2: musical occupation of Gerry Marsden | false | musician | — | [d10s0] | — |
| u3: Are Daryl Hall and Gerry Marsden both musicians? | true | yes | u1, u2 | `[[]]`：由全部依赖推出 | — |

Evidence:

- `d6s0` Daryl Hall [0]: Daryl Franklin Hohl (born October 11, 1946), known professionally as Daryl Hall, is an American rock, R&B, and soul singer; keyboardist, guitarist, songwriter, and producer, best known as the co-founder and lead vocalist of Hall & Oates (with guitarist and songwriter John Oates).
- `d10s0` Gerry Marsden [0]: Gerard Marsden MBE (born 24 September 1942) is an English musician and television personality, best known for being leader of the British Merseybeat band Gerry and the Pacemakers.

Notes:

- Singer and instrumentalist roles explicitly establish work as a musician.
- 复核后保留原标注；原note为说明或未发现需要修改的证据/依赖问题。

<details><summary>All source context</summary>

- `d1s0` Did It in a Minute [0]: "Did It in a Minute" is a song performed by American musical duo Hall & Oates.
- `d1s1` Did It in a Minute [1]: Written by member Daryl Hall with Sara and Janna Allen.
- `d1s2` Did It in a Minute [2]: The song was released as the third of four singles from their tenth studio album "Private Eyes" in March 1982.
- `d1s3` Did It in a Minute [3]: Daryl Hall performs lead vocals, while John Oates provides backing harmony vocals.
- `d2s0` One on One (song) [0]: "One on One" is a song performed by American musical duo Hall & Oates.
- `d2s1` One on One (song) [1]: Written by member Daryl Hall, the song was released as the second single from their eleventh studio album "HO" on January 29, 1983.
- `d2s2` One on One (song) [2]: Backed by minimalistic, synthesizer-based production, the song's lyrics incorporate various sports metaphors to describe seduction.
- `d2s3` One on One (song) [3]: Daryl Hall performs lead vocals, while John Oates provides backing harmony vocals.
- `d3s0` Janna Allen [0]: Janna Allen (May 12, 1957 – August 25, 1993) was an American songwriter.
- `d3s1` Janna Allen [1]: She is best known as a co-writer of some of the biggest hits recorded by Daryl Hall & John Oates, in collaboration variously with Daryl Hall, John Oates and her sister Sara Allen, who was Hall's longtime girlfriend and the person for whom the duo's hit song "Sara Smile" was written.
- `d4s0` Live from Daryl's House [0]: Live from Daryl's House (simply known as Daryl's House, and often abbreviated as LFDH) is an online series that was first created in fall 2007.
- `d4s1` Live from Daryl's House [1]: The show features singer-songwriter Daryl Hall performing with his band and various guest artists at his home in Millerton, New York.
- `d4s2` Live from Daryl's House [2]: The show provides a performance space that is an alternative to live concerts and studio sessions for popular artists.
- `d4s3` Live from Daryl's House [3]: This allows the artists to "…have fun and [be] creatively spontaneous".
- `d4s4` Live from Daryl's House [4]: The majority of shows include a segment in which Hall and the guest artist prepare food from different cuisines for everyone to eat.
- `d4s5` Live from Daryl's House [5]: The food comes from various local restaurants and the chefs of those establishments walk Hall and guest through the preparation of the food.
- `d4s6` Live from Daryl's House [6]: "Live From Daryl's House" expanded to broadcast TV but remained unchanged.
- `d4s7` Live from Daryl's House [7]: Hall was quoted by Billboard.com as saying "it's an Internet show that is being shown on television, so I'm not adapting the show at all in any way to be a 'TV' show."
- `d4s8` Live from Daryl's House [8]: The show debuted in 95 markets on September 24, 2011, with back-to-back half-hour episodes featuring Train (Episode 33) and Fitz & the Tantrums (Episode 35).
- `d4s9` Live from Daryl's House [9]: Starting with the 66th episode of "Live From Daryl's House", the shows are filmed at Hall's club, Daryl's House, in Pawling, New York.
- `d5s0` Don't Let the Sun Catch You Crying [0]: "Don't Let the Sun Catch You Crying" is a song written and originally performed by British beat group Gerry and the Pacemakers.
- `d5s1` Don't Let the Sun Catch You Crying [1]: The songwriting is credited to Gerry Marsden and the other band members, Freddie Marsden, Les Chadwick and Les Maguire.
- `d5s2` Don't Let the Sun Catch You Crying [2]: It was first recorded by Louise Cordet, and then recorded by the group themselves in early 1964.
- `d6s0` Daryl Hall [0]: Daryl Franklin Hohl (born October 11, 1946), known professionally as Daryl Hall, is an American rock, R&B, and soul singer; keyboardist, guitarist, songwriter, and producer, best known as the co-founder and lead vocalist of Hall & Oates (with guitarist and songwriter John Oates).
- `d7s0` Ferry Cross the Mersey [0]: "Ferry Cross the Mersey" (sometimes written Ferry 'Cross the Mersey) is a song written by Gerry Marsden.
- `d7s1` Ferry Cross the Mersey [1]: It was first recorded by his band Gerry and the Pacemakers and released in late 1964 in the UK and in 1965 in the United States.
- `d7s2` Ferry Cross the Mersey [2]: It was a hit on both sides of the Atlantic, reaching number six in the United States and number eight in the UK.
- `d7s3` Ferry Cross the Mersey [3]: The song is from the film of the same name and was released on its soundtrack album.
- `d7s4` Ferry Cross the Mersey [4]: In the mid-1990s a musical theatre production also titled "Ferry Cross the Mersey" related Gerry Marsden's Merseybeat days; it premiered in Liverpool and played in the UK, Australia, and Canada.
- `d8s0` Jonathan Wolfson [0]: Jonathan Wolfson (born December 1, 1970) is an American television executive, manager, and publicist.
- `d8s1` Jonathan Wolfson [1]: He is known for his managerial work with the musical group Daryl Hall & John Oates and the Canadian-rock group Loverboy.
- `d8s2` Jonathan Wolfson [2]: He was previously well known for his publicity work with Suge Knight through his company Wolfson Public Relations.
- `d8s3` Jonathan Wolfson [3]: Jonathan has executive produced Daryl Hall’s TV shows "Daryl’s Restoration Over-Hall" and "Live From Daryl’s House".
- `d9s0` Hall &amp; Oates [0]: Daryl Hall and John Oates, often referred to as Hall & Oates, are an American musical duo from Philadelphia.
- `d9s1` Hall &amp; Oates [1]: Daryl Hall is generally the lead vocalist of the pairing.
- `d9s2` Hall &amp; Oates [2]: John Oates primarily plays electric guitar and provides backing vocals.
- `d9s3` Hall &amp; Oates [3]: The two write most of the songs they perform, either separately or in collaboration.
- `d9s4` Hall &amp; Oates [4]: They achieved their greatest fame from the late 1970s to the mid-1980s with a fusion of rock and roll and rhythm and blues.
- `d10s0` Gerry Marsden [0]: Gerard Marsden MBE (born 24 September 1942) is an English musician and television personality, best known for being leader of the British Merseybeat band Gerry and the Pacemakers.

</details>

## Q208 — `hotpotqa_5a8cd381554299653c1aa12b` (revised draft)

> who had to escape nazis, Sigmund Freud or Evelyn Waugh?

Source answer: Sigmund Freud

Gold final answer: Sigmund Freud

Question type: `comparison` (source type `comparison`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: whether Sigmund Freud left to escape the Nazis | false | yes | — | [d4s5] | — |
| u2: whether Evelyn Waugh left to escape the Nazis | false | no | — | `[]`：无直接支持 | — |
| u3: who had to escape nazis, Sigmund Freud or Evelyn Waugh? | true | Sigmund Freud **[by_presupposition]** | u1, u2 | `[[]]`：由全部依赖推出 | [d4s5] |

Evidence:

- `d4s5` Sigmund Freud [5]: In 1938 Freud left Austria to escape the Nazis.

Notes:

- 已检查d10s0–d10s3的Waugh介绍，没有逃离纳粹的信息；历史事件不能用职业遗漏排除。补候选unit但仅启用Freud正向链路。

<details><summary>All source context</summary>

- `d1s0` Statue of Sigmund Freud, Hampstead [0]: The statue of Sigmund Freud is a seated bronze statue of the founder of psychoanalysis, Sigmund Freud, situated on a limestone plinth at the junction of Fitzjohn's Avenue and Belsize Lane in Hampstead, North London.
- `d1s1` Statue of Sigmund Freud, Hampstead [1]: Freud lived at nearby 20 Maresfield Gardens, for the last months of his life.
- `d1s2` Statue of Sigmund Freud, Hampstead [2]: His house is now the Freud Museum.
- `d2s0` Sigmund Freud Museum (Vienna) [0]: The Sigmund Freud Museum in Vienna is a museum founded in 1971 covering Sigmund Freud's life story.
- `d2s1` Sigmund Freud Museum (Vienna) [1]: It is located in the Alsergrund district, at Berggasse 19.
- `d2s2` Sigmund Freud Museum (Vienna) [2]: In 2003 the museum was put in the hands of the newly established Sigmund Freud Foundation, which has since received the entire building as an endowment.
- `d2s3` Sigmund Freud Museum (Vienna) [3]: It also covers the history of psychoanalysis.
- `d3s0` The Assault on Truth [0]: The Assault on Truth: Freud's Suppression of the Seduction Theory is a book by Jeffrey Moussaieff Masson, in which the author argues that Sigmund Freud deliberately suppressed his early hypothesis, known as the seduction theory, that hysteria is caused by sexual abuse during infancy, because he refused to believe that children are the victims of sexual violence and abuse within their own families.
- `d3s1` The Assault on Truth [1]: Masson reached this conclusion while he had access to some of Freud's unpublished letters as projects director of the Sigmund Freud Archives.
- `d3s2` The Assault on Truth [2]: "The Assault on Truth" was first published in 1984, and several revised editions have since been published.
- `d4s0` Sigmund Freud [0]: Sigmund Freud ( ; ] ; born Sigismund Schlomo Freud; 6 May 1856 – 23 September 1939) was an Austrian neurologist and the founder of psychoanalysis, a clinical method for treating psychopathology through dialogue between a patient and a psychoanalyst.
- `d4s1` Sigmund Freud [1]: Freud was born to Galician Jewish parents in the Moravian town of Freiberg, in the Austrian Empire.
- `d4s2` Sigmund Freud [2]: He qualified as a doctor of medicine in 1881 at the University of Vienna.
- `d4s3` Sigmund Freud [3]: Upon completing his habilitation in 1885, he was appointed a docent in neuropathology and became an affiliated professor in 1902.
- `d4s4` Sigmund Freud [4]: Freud lived and worked in Vienna, having set up his clinical practice there in 1886.
- `d4s5` Sigmund Freud [5]: In 1938 Freud left Austria to escape the Nazis.
- `d4s6` Sigmund Freud [6]: He died in exile in the United Kingdom in 1939.
- `d5s0` Sigmund Freud Prize [0]: The Sigmund Freud Prize or Sigmund Freud Prize for Scientific Prose (German "Sigmund Freud-Preis für wissenschaftliche Prosa") is a German literary award named after Sigmund Freud and awarded by the Deutsche Akademie für Sprache und Dichtung.
- `d5s1` Sigmund Freud Prize [1]: It was first awarded in 1964.
- `d6s0` Freud and Philosophy [0]: Freud and Philosophy: An Essay on Interpretation (French: "De l'interprétation.
- `d6s1` Freud and Philosophy [1]: Essai sur Sigmund Freud" ) is a 1965 book about Sigmund Freud by the philosopher Paul Ricœur.
- `d6s2` Freud and Philosophy [2]: Sometimes grouped with works such as Jürgen Habermas's "Knowledge and Human Interests" (1968), "Freud and Philosophy" has received praise, but critics have argued Ricœur provides a mistaken interpretation of Freud.
- `d7s0` Sigmund Freud Archives [0]: The Sigmund Freud Archives mainly consist of a trove of documents housed at the US Library of Congress and in the former residence of Sigmund Freud during the last year of his life at 20 Maresfield Gardens in northwest London.
- `d7s1` Sigmund Freud Archives [1]: They were at the center of a complicated scandal which is described in Janet Malcolm's book "In the Freud Archives."
- `d7s2` Sigmund Freud Archives [2]: Jeffrey Masson writes about it in Chapter Nine: "Disillusions" of his book "Final Analysis".
- `d8s0` Freud: A Life for Our Time [0]: Freud: A Life for Our Time is a 1988 biography of Sigmund Freud, the founder of psychoanalysis, by the historian Peter Gay.
- `d8s1` Freud: A Life for Our Time [1]: The work is based partly on new material that has become available since the publication of Ernest Jones' "The Life and Work of Sigmund Freud" (1953).
- `d8s2` Freud: A Life for Our Time [2]: The book has been praised, but has also been criticized by several authors skeptical of psychoanalysis.
- `d9s0` The Life and Work of Sigmund Freud [0]: The Life and Work of Sigmund Freud is a biography of Sigmund Freud by Ernest Jones.
- `d9s1` The Life and Work of Sigmund Freud [1]: The most famous and influential biography of Freud, "The Life and Work of Sigmund Freud" was originally published in three volumes (first volume 1953, second volume 1955, third volume 1957); a one-volume edition abridged by literary critics Lionel Trilling and Steven Marcus followed in 1961.
- `d9s2` The Life and Work of Sigmund Freud [2]: When first published, "The Life and Work of Sigmund Freud" was acclaimed, and sales exceeded expectations.
- `d9s3` The Life and Work of Sigmund Freud [3]: Although his biography has retained its status as a classic, Jones has been criticized for presenting an overly favorable image of Freud.
- `d10s0` Evelyn Waugh [0]: Arthur Evelyn St. John Waugh ( ; 28 October 1903 – 10 April 1966) was an English writer of novels, biographies and travel books.
- `d10s1` Evelyn Waugh [1]: He was also a prolific journalist and reviewer of books.
- `d10s2` Evelyn Waugh [2]: His most famous works include the early satires "Decline and Fall" (1928) and "A Handful of Dust" (1934), the novel "Brideshead Revisited" (1945) and the Second World War trilogy "Sword of Honour" (1952–61).
- `d10s3` Evelyn Waugh [3]: Waugh is recognised as one of the great prose stylists of the English language in the 20th century.

</details>

## Q209 — `hotpotqa_5a8d50fb55429941ae14dfa2` (revised draft)

> The Bodie & Benton Railway was a narrow gauge common carrier railroad in California, from the Mono Mills to a terminus in a ghost town located how many miles away from Lake Tahoe ?

Source answer: 75 mi

Gold final answer: 75 mi

Question type: `bridge` (source type `bridge`)

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: ghost-town terminus of the Bodie and Benton Railway | false | Bodie | — | [d5s0] | — |
| u2: distance between {u1} and Lake Tahoe | true | 75 mi | u1 | [d3s0] | — |

Evidence:

- `d3s0` Bodie, California [0]: Bodie ( ) is a ghost town in the Bodie Hills east of the Sierra Nevada mountain range in Mono County, California, United States, about 75 mi southeast of Lake Tahoe.
- `d5s0` Bodie and Benton Railway and Commercial Company [0]: The Bodie & Benton Railway was a narrow gauge common carrier railroad in California, from the Mono Mills to a terminus in Bodie, now a ghost town, in Mono County.

Notes:

- 保留两跳。铁路名称含Bodie不等于题干明确给出终点；d5s0仍是确认ghost-town terminus所需证据，不能仅按名称跳过。

<details><summary>All source context</summary>

- `d1s0` Kauai Railway [0]: The Kauai Railway is a former narrow gauge railway company in Hawaii, United States.
- `d1s1` Kauai Railway [1]: It was created 1906 and operated a 30 km long railroad line with narrow gauge track from Port Allen,to Koloa and Kalaheo on the south coast of the island of Kauai.
- `d1s2` Kauai Railway [2]: It did not have a connection to the other common carrier railway on the island, the Ahukini Terminal and Railway, although both were built to the same track gauge.
- `d1s3` Kauai Railway [3]: Almost all railway trackage on Kauai was connected together due to an agreement with the U.S. Government to interconnect the common carriers and sugarcane plantation railways.
- `d1s4` Kauai Railway [4]: The government imposed this as a condition before they would agree to improve the port of Nawiliwili for oceangoing ships.
- `d1s5` Kauai Railway [5]: The line was opened 1907.
- `d1s6` Kauai Railway [6]: In 1936 the company name was changed to the Kauai Terminal Company.
- `d1s7` Kauai Railway [7]: The last train ran 1947, with rail operations replaced by trucks.
- `d1s8` Kauai Railway [8]: The company continues to exist as the present-day Kauai Commercial Company.
- `d2s0` Oahu Railway and Land Company [0]: The Oahu Railway and Land Company, or OR&L, was a narrow gauge common carrier railway that served much of the Hawaiian island of Oahu, and was the largest narrow gauge class one common carrier in the U.S, until its dissolution in 1947.
- `d3s0` Bodie, California [0]: Bodie ( ) is a ghost town in the Bodie Hills east of the Sierra Nevada mountain range in Mono County, California, United States, about 75 mi southeast of Lake Tahoe.
- `d3s1` Bodie, California [1]: It is located 12 mi east-southeast of Bridgeport, at an elevation of 8379 feet (2554 m).
- `d3s2` Bodie, California [2]: As Bodie Historic District, the U.S. Department of the Interior recognizes it as a National Historic Landmark.
- `d4s0` Lakeside and Marblehead Railroad [0]: Incorporated on April 17, 1886, at Marblehead, Ohio, the Lakeside and Marblehead Railroad (L&M) was a short standard gauge railroad that spanned about seven miles (11.3 km) in length.
- `d4s1` Lakeside and Marblehead Railroad [1]: It extended from Marblehead through Lakeside to a connection with the Lake Shore and Michigan Southern Railway (later the New York Central Railroad) at Danbury (an unincorporated hamlet bordering Sandusky Bay).
- `d4s2` Lakeside and Marblehead Railroad [2]: A common carrier, it carried both freight and passengers.
- `d4s3` Lakeside and Marblehead Railroad [3]: It was abandoned as a common carrier railroad July 31, 1964, operated for the last time as a private industrial railroad in Summer 1978, and its tracks were removed in Fall 1997.
- `d5s0` Bodie and Benton Railway and Commercial Company [0]: The Bodie & Benton Railway was a narrow gauge common carrier railroad in California, from the Mono Mills to a terminus in Bodie, now a ghost town, in Mono County.
- `d5s1` Bodie and Benton Railway and Commercial Company [1]: It was unusual among U.S. railroads in that it was completely isolated from the rest of the railroad system.
- `d6s0` Sandy River Railroad [0]: The Sandy River Railroad was a narrow gauge railway built to serve the towns of Strong and Phillips in the Sandy River valley upstream of Farmington.
- `d6s1` Sandy River Railroad [1]: The Sandy River Railroad was the first narrow gauge common carrier railroad built in the State of Maine.
- `d7s0` Phillips and Rangeley Railroad [0]: The Phillips and Rangeley Railroad was a narrow gauge common carrier railroad in the State of Maine.
- `d8s0` Sandy River and Rangeley Lakes Railroad [0]: The Sandy River & Rangeley Lakes Railroad (SR&RL) was a narrow gauge common carrier railroad that operated approximately 112 mi of track in Franklin County, Maine.
- `d8s1` Sandy River and Rangeley Lakes Railroad [1]: Former equipment from the SR&RL continues to operate in the present day on a revived, short segment of the railway in Phillips, Maine.
- `d9s0` Mono Mills Junction, California [0]: Mono Mills Junction (may sometimes be referred to as "Benton Junction") is a location within the Mono Basin in central Mono County where the Mono Mills Road California State Route 120, proceeds eastward from U.S. Route 395.
- `d9s1` Mono Mills Junction, California [1]: Route 120 accesses the Mono Lake Tufa State Reserve, including Navy Beach and South Tufa along the shores of Mono Lake, and leads through Mono Mills to Benton where it reaches the U.S. Route 6.
- `d10s0` Mono Mills, California [0]: Mono Mills (also, Mono) is a ghost town in Mono County, California.
- `d10s1` Mono Mills, California [1]: It is located 9.5 mi east-southeast of Lee Vining, at an elevation of 7356 feet (2242 m).
- `d10s2` Mono Mills, California [2]: Mono Mills has nearly vanished.
- `d10s3` Mono Mills, California [3]: Its site is along California State Route 120, 9.1 mi east from the junction with U.S. Route 395.

</details>

## Q210 — `hotpotqa_5adf8d5b5542995534e8c7e1` (revised draft)

> What year was the winner of the 2016 Marrakesh ePrix born?

Source answer: 1988

Gold final answer: 1988

Question type: `bridge` (source type `bridge`)

Replaces: `hotpotqa_5a8da81e554299068b959d7e`

| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |
|---|---|---|---|---|---|
| u1: winner of the 2016 Marrakesh ePrix | false | Sébastien Buemi | — | [d5s2] | — |
| u2: birth year of {u1} | true | 1988 | u1 | [d7s0] | — |

Evidence:

- `d5s2` 2016 Marrakesh ePrix [2]: The 33-lap race was won by e.Dams-Renault driver Sébastien Buemi, who started from the seventh position.
- `d7s0` Sébastien Buemi [0]: Sébastien Olivier Buemi (born 31 October 1988) is a Swiss professional racing driver, who formerly competed for Scuderia Toro Rosso in Formula One.

Notes:

- 替换：producer不能直接等同impresario；按用户要求替换。 新题保留原source type，人工核对两条显式事实及答案。

<details><summary>All source context</summary>

- `d1s0` Anu Namshir [0]: ANU NAMSHIR (Mongolian: НАМШИРЫН АНУ , , Korean: 아누 남시르 ) born April 12, 1991 is a Mongolian miss, model, graphic designer and titleholder.
- `d1s1` Anu Namshir [1]: She won the "Miss Mongolia" 2013 title and was later crowned as World Bikini Model International 2014 (1st runner up) and "Miss Manzhouli 2014" (winner) in China, Asian Star Model 2015 Supermodel International 2015 (winner) in Korea and Miss World Mongolia 2015 (national winner).
- `d1s2` Anu Namshir [2]: And then she represented Mongolia in the Miss World 2015.
- `d1s3` Anu Namshir [3]: In 2016, September 26, she also was crowned Miss Tourism Queen International 2016 (winner) and awarded Miss Charity.
- `d1s4` Anu Namshir [4]: And then December 1, 2016, she has participated first in Goyol 2017 which was organized by Mongolian Designers Association annually was awarded Photo Model.
- `d1s5` Anu Namshir [5]: She worked at Mongolia's Next Top Model show 14th number representing Z24 online ticket reservation through Z24 face.
- `d2s0` Walter Payton NFL Man of the Year Award [0]: The Walter Payton NFL Man of the Year award is presented annually by the National Football League (NFL) honoring a player's volunteer and charity work, as well as his excellence on the field.
- `d2s1` Walter Payton NFL Man of the Year Award [1]: Prior to 1999, it was called simply the NFL Man of the Year Award.
- `d2s2` Walter Payton NFL Man of the Year Award [2]: Shortly after Chicago Bears running back Walter Payton died (having been the 1977 recipient himself), the award was renamed to honor his legacy as a humanitarian.
- `d2s3` Walter Payton NFL Man of the Year Award [3]: Each year, a winner is selected from 32 nominees from the 32 different teams.
- `d2s4` Walter Payton NFL Man of the Year Award [4]: A panel of judges, which includes the Commissioner of the NFL, Connie Payton (widow of Walter Payton), the previous year's winner, and a number of former players select the winner of the award.
- `d2s5` Walter Payton NFL Man of the Year Award [5]: The Man of the Year winner receives a $50,000 donation in his name to a charity of his choice.
- `d2s6` Walter Payton NFL Man of the Year Award [6]: The other 31 finalists also receive donations in their name of $5,000 each to charities of their choice.
- `d2s7` Walter Payton NFL Man of the Year Award [7]: The Chicago Bears and Kansas City Chiefs have had more winners of the award than any other team, with 5 winners each.
- `d2s8` Walter Payton NFL Man of the Year Award [8]: The winners for the 2016 award are New York Giants quarterback Eli Manning and Arizona Cardinals wide receiver Larry Fitzgerald.
- `d3s0` Carole Dieschbourg [0]: Carole Dieschbourg (born 1977) is a Luxembourg politician and writer.
- `d3s1` Carole Dieschbourg [1]: Since December 2013, she has been Minister for the Environment representing the Green in the government coalition consisting of the Democratic Party, the Luxembourg Socialist Workers' Party and the Green Party.
- `d3s2` Carole Dieschbourg [2]: She represented Luxembourg at the COP22 Climate Change Conference in Marrakesh, November 2016.
- `d4s0` Jérôme d'Ambrosio [0]: Jérôme d'Ambrosio (born 27 December 1985) is a Belgian professional racing driver.
- `d4s1` Jérôme d'Ambrosio [1]: He drove for Marussia Virgin Racing during the 2011 Formula One World Championship.
- `d4s2` Jérôme d'Ambrosio [2]: As a result of the one-race ban given to Romain Grosjean for actions at the start of the 2012 Belgian Grand Prix, d'Ambrosio replaced the Frenchman for the 2012 Italian Grand Prix.
- `d4s3` Jérôme d'Ambrosio [3]: In 2016, he is competing in Formula E driving for Dragon Racing.
- `d4s4` Jérôme d'Ambrosio [4]: D'Ambrosio achieved his first Formula E victory in 2015 at the 2015 Berlin ePrix, and a second at the 2016 Mexican ePrix, both as a result of Lucas di Grassi's disqualification.
- `d5s0` 2016 Marrakesh ePrix [0]: The 2016 Marrakesh ePrix (formally the 2016 FIA Formula E Marrakesh ePrix) was a Formula E motor race held on 12 November 2016 at the Circuit Moulay El Hassan in Marrakesh, Morocco in front of a crowd of 7,000 people.
- `d5s1` 2016 Marrakesh ePrix [1]: It was the second round of the 2016–17 Formula E season and the first time the series had visited the African continent.
- `d5s2` 2016 Marrakesh ePrix [2]: The 33-lap race was won by e.Dams-Renault driver Sébastien Buemi, who started from the seventh position.
- `d5s3` 2016 Marrakesh ePrix [3]: Sam Bird finished second for the Virgin team and Mahindra driver Felix Rosenqvist came in third.
- `d6s0` 2016 BBC Sports Personality of the Year Award [0]: The 2016 BBC Sports Personality of the Year Award took place on 18 December 2016 at the Genting Arena in Birmingham.
- `d6s1` 2016 BBC Sports Personality of the Year Award [1]: It was the 63rd presentation of the BBC Sports Personality of the Year Award.
- `d6s2` 2016 BBC Sports Personality of the Year Award [2]: Awarded annually by the British Broadcasting Corporation (BBC), the main award honours an individual's British sporting achievement over the past year, with the winner selected by public vote from a sixteen-person shortlist; the winner was Tennis player Andy Murray, who became the first person to win the award three times.
- `d7s0` Sébastien Buemi [0]: Sébastien Olivier Buemi (born 31 October 1988) is a Swiss professional racing driver, who formerly competed for Scuderia Toro Rosso in Formula One.
- `d7s1` Sébastien Buemi [1]: Buemi is currently a reserve driver for Scuderia Toro Rosso's sister team, Red Bull Racing, as well as being a member of Toyota's FIA World Endurance Championship squad and e.dams Renault in the FIA Formula E Championship.
- `d7s2` Sébastien Buemi [2]: Along with teammate Anthony Davidson, Buemi became World Champion in the LMP1 class of the FIA World Endurance Championship, in 2014.
- `d7s3` Sébastien Buemi [3]: He won the second ever Formula E championship, the season held across 2015–2016, by two points for setting the fastest lap time in the final race despite not finishing the event.
- `d8s0` Lucas di Grassi [0]: Lucas Tucci di Grassi (born 11 August 1984) is a Brazilian professional racing driver who currently competes for Audi Sport ABT in Formula E and is the 2016-17 World Champion.
- `d8s1` Lucas di Grassi [1]: In 2014, di Grassi became the first driver in motorsport history to win a motor race in an all-electric single-seater racing car at the 2014 Beijing ePrix.
- `d8s2` Lucas di Grassi [2]: He was also runner-up in the 2007 GP2 Series, 2015-16 FIA Formula E and 2016 FIA World Endurance Championship, and drove for Virgin Racing in the 2010 Formula One season.
- `d9s0` BBC Sports Personality of the Year Award [0]: The BBC Sports Personality of the Year Award is the main award of the BBC Sports Personality of the Year ceremony, which takes place each December.
- `d9s1` BBC Sports Personality of the Year Award [1]: The winner is the sportsperson, judged by a public vote, to have achieved the most that year.
- `d9s2` BBC Sports Personality of the Year Award [2]: The recipient must either be British or reside and play a significant amount of their sport in the United Kingdom.
- `d9s3` BBC Sports Personality of the Year Award [3]: The winner is selected by a public-vote from a pre-determined shortlist.
- `d9s4` BBC Sports Personality of the Year Award [4]: The most recent award winner is tennis player Andy Murray, who won in 2016.
- `d10s0` FPAI Indian Player of the Year [0]: The FPAI Indian Player of the Year is an annual award given to an Indian player who is adjudged to have been the best of the year in Indian football.
- `d10s1` FPAI Indian Player of the Year [1]: The award has been presented since the 2009–10 season and the winner is chosen by a vote amongst the members of the players' trade union, the Football Players' Association of India.
- `d10s2` FPAI Indian Player of the Year [2]: The first winner of the award was Dempo striker Sunil Chhetri.
- `d10s3` FPAI Indian Player of the Year [3]: Anas Edathodika, the Defender of Mohun Bagan  and Indian national team has been the recent winner, for 2016–17.

</details>
