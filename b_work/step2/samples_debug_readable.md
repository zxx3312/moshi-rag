# Debug Questions for Manual Review

This document presents all 20 records from `samples_debug.jsonl` in their original order. Questions, answers, context sentences, source annotations, and metadata are preserved. Supporting sentences are displayed before the full context for easier review.

**Review status:** The source annotations are reproduced as provided. This formatting conversion does not validate the answers or complete human review.

**Sentence numbering:** Sentence indices start at **0**, matching the source file. The label **SUPPORT** marks a sentence referenced in `supporting_facts`; it is a source annotation, not a new review judgment.

## Dataset Summary

| Dataset | Questions |
| --- | ---: |
| 2WikiMultiHopQA | 8 |
| Custom | 4 |
| HotpotQA | 8 |

## Question Index

1. [2WikiMultiHopQA — Who is Caroline Emily Nevill's paternal grandfather?](#question-01)
2. [2WikiMultiHopQA — Which film has the director who died later, The Obsessed Of Catule or Countess Ironing-Maid?](#question-02)
3. [2WikiMultiHopQA — Where was the director of film Being Twenty born?](#question-03)
4. [2WikiMultiHopQA — Who is Margaret Fiennes, 11Th Baroness Dacre's paternal grandfather?](#question-04)
5. [2WikiMultiHopQA — Who was born later, Mark Gurr or William Eythe?](#question-05)
6. [2WikiMultiHopQA — Which film has the director who died later, Hotel Paradis or Devil'S Doorway?](#question-06)
7. [2WikiMultiHopQA — Are Brian Part and John Mosca both from the same country?](#question-07)
8. [2WikiMultiHopQA — What is the place of birth of the director of film A Nightmare On Elm Street 5: The Dream Child?](#question-08)
9. [Custom — On what date did Apollo 11 launch, and on what date did it splash down on Earth?](#question-09)
10. [Custom — On what date did Perseverance launch, and on what date did it land on Mars?](#question-10)
11. [Custom — On what date did Voyager 1 launch, and on what date was its closest approach to Jupiter?](#question-11)
12. [Custom — On what date did Voyager 2 launch, and on what date did it fly by Neptune?](#question-12)
13. [HotpotQA — Hall of Fame Racing was created by Troy Aikman, Bill Saunders, and which Dallas Cowboys quarterback known as "Captain Comback"?](#question-13)
14. [HotpotQA — Who appeared in the Olympics first, Piet Norval or Emilio Sánchez?](#question-14)
15. [HotpotQA — The birthplace of George McCall Theal is a port city of what bay?](#question-15)
16. [HotpotQA — Are William Kronick and Jon Turteltaub both television writers ?](#question-16)
17. [HotpotQA — In between Anaïs Nin and Odysseas Elytis who was awarded the Nobel Prize in Literature?](#question-17)
18. [HotpotQA — What job did Newt Gingrich have prior to producing Nine Days that Changed the World?](#question-18)
19. [HotpotQA — Are the genera Gordonia and Osbeckia in the same family?](#question-19)
20. [HotpotQA — What is the mononym of the Fillipino singer that released the album "My Inspiration"?](#question-20)

<a id="question-01"></a>

## Question 01

**Dataset:** 2WikiMultiHopQA  
**Sample ID:** `2wikimultihopqa_062884f40bb011ebab90acde48001122`  
**Review status:** `pending_human_review`

### Question

> Who is Caroline Emily Nevill's paternal grandfather?

### Reference Answer

> Henry Nevill, 2nd Earl of Abergavenny

### Annotated Supporting Sentences

**1. Caroline Emily Nevill — sentence [1]**

> The daughter of William Nevill, 4th Earl of Abergavenny,
> she and her sisters Henrietta (1830–1912) and Isabel (1831–1915) were together known as "The Trio" when they exhibited at the London Photographic Society in 1854.

**2. William Nevill, 4th Earl of Abergavenny — sentence [2]**

> The fourth son of Henry Nevill, 2nd Earl of Abergavenny, he was ordained in 1816 and occupied two of the family livings until 1844.

### Annotated Evidence Relations

| Subject | Relation | Object |
| --- | --- | --- |
| Caroline Emily Nevill | father | William Nevill, 4th Earl of Abergavenny |
| William Nevill, 4th Earl of Abergavenny | father | Henry Nevill, 2nd Earl of Abergavenny |

### Full Context

#### Document 1 — Peter Schermerhorn

**[0]**

> Peter Schermerhorn( October 1, 1749 – January 28, 1826) was a wealthy New York City merchant and land owner.

**[1]**

> He was the father of Abraham Schermerhorn and the grandfather of Caroline Schermerhorn Astor.

#### Document 2 — Mrs. Lovett Cameron

**[0]**

> Mrs. Lovett Cameron or Caroline" Emily" Sharp( 1844 – 1921) was a British romantic fiction author.

**[1]**

> She wrote more than fourteen three- volume novels.

#### Document 3 — Caroline Emily Nevill

**[0]**

> Lady Caroline Emily Nevill (1829–1887) was an early English photographer.

**[1] SUPPORT**

> The daughter of William Nevill, 4th Earl of Abergavenny,
> she and her sisters Henrietta (1830–1912) and Isabel (1831–1915) were together known as "The Trio" when they exhibited at the London Photographic Society in 1854.

**[2]**

> Lady Caroline was a pioneering member of the Photographic Exchange Club (founded 1855) contributing architectural views of Kent from 1855 to 1858.

**[3]**

> From 1859, she also contributed to the Amateur Photographic Association.

#### Document 4 — Lyon Cohen

**[0]**

> Lyon Cohen( 1868–1937) was a Polish- born Canadian businessman and a philanthropist.

**[1]**

> He was the grandfather of singer/ poet Leonard Cohen.

#### Document 5 — Guillaume Wittouck

**[0]**

> Guillaume Wittouck( 1749- 1829) was a Belgian lawyer and High Magistrate.

**[1]**

> He was the Grandfather of industrialist Paul Wittouck.

#### Document 6 — Kaya Alp

**[0]**

> Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

#### Document 7 — William Nevill, 4th Earl of Abergavenny

**[0]**

> William Nevill, 4th Earl of Abergavenny (28 June 1792 – 17 August 1868), styled Hon.

**[1]**

> William Nevill until 1845, was a British peer and clergyman.

**[2] SUPPORT**

> The fourth son of Henry Nevill, 2nd Earl of Abergavenny, he was ordained in 1816 and occupied two of the family livings until 1844.

**[3]**

> He succeeded his brother as Earl of Abergavenny the following year.

#### Document 8 — Abd al-Muttalib

**[0]**

> Abd al- Muttalib Shaybah ibn Hashim( c. 497 – 578) was the grandfather of Islamic prophet Muhammad.

#### Document 9 — John Westley

**[0]**

> Rev. John Westley( 1636 – 78) was an English nonconformist minister.

**[1]**

> He was the grandfather of John Wesley( founder of Methodism).

#### Document 10 — Prithvipati Shah

**[0]**

> Prithvipati Shah( ?–1716) was the king of the Gorkha Kingdom in the Indian subcontinent, present- day Nepal.

**[1]**

> He was the grandfather of Nara Bhupal Shah.

### Additional Metadata

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "source_split": "dev",
  "source_id": "062884f40bb011ebab90acde48001122",
  "project_split": "debug",
  "type": "inference",
  "answer_id": "Q7611230",
  "evidences_id": [
    [
      "Q16062798",
      "father",
      "Q7611188"
    ],
    [
      "Q7611188",
      "father",
      "Q7611230"
    ]
  ],
  "entity_ids": "Q16062798_Q7611188"
}
```

[Back to question index](#question-index)


<a id="question-02"></a>

## Question 02

**Dataset:** 2WikiMultiHopQA  
**Sample ID:** `2wikimultihopqa_36ec2b3a086411ebbd5eac1f6bf848b6`  
**Review status:** `pending_human_review`

### Question

> Which film has the director who died later, The Obsessed Of Catule or Countess Ironing-Maid?

### Reference Answer

> The Obsessed Of Catule

### Annotated Supporting Sentences

**1. The Obsessed of Catule — sentence [0]**

> The Obsessed of Catule is a 1965 Brazilian drama film directed by Anselmo Duarte.

**2. Countess Ironing-Maid — sentence [0]**

> Countess Ironing- Maid( German: Gräfin Plättmamsell) is a 1926 German silent comedy film directed by Constantin J. David and starring Ossi Oswalda, Curt Bois and Robert Garrison.

**3. Anselmo Duarte — sentence [0]**

> Anselmo Duarte( April 21, 1920 – November 7, 2009) was a Brazilian actor, screenwriter and film director.

**4. Constantin J. David — sentence [0]**

> Constantin J. David (18 February 1886 – 19 February 1964) was a German journalist, film director, film producer, and actor.

### Annotated Evidence Relations

| Subject | Relation | Object |
| --- | --- | --- |
| The Obsessed of Catule | director | Anselmo Duarte |
| Countess Ironing-Maid | director | Constantin J. David |
| Anselmo Duarte | date of death | November 7, 2009 |
| Constantin J. David | date of death | 19 February 1964 |

### Full Context

#### Document 1 — Elliot Silverstein

**[0]**

> Elliot Silverstein( born August 3, 1927, in Boston, Massachusetts) is an American director, who is best known for being the director of the movie" Cat Ballou"( 1965).

#### Document 2 — G. Marthandan

**[0]**

> G. Marthandan is an Indian film director who works in Malayalam cinema.

#### Document 3 — Ben Palmer

**[0]**

> Ben Palmer is a British film and television director who is known for being the director of" Bo' Selecta" and" The Inbetweeners".

#### Document 4 — Anselmo Duarte

**[0] SUPPORT**

> Anselmo Duarte( April 21, 1920 – November 7, 2009) was a Brazilian actor, screenwriter and film director.

**[1]**

> His film" O Pagador de Promessas"( 1962)( also" The Given Word" and" The Keeper of Promises") won the Golden Palm at the 1962 Cannes Film Festival, becoming, to date, the only Brazilian feature film to be so distinguished and the first Cannes' Southern Hemisphere Golden Palm for best feature film.

**[2]**

> The film was also nominated for the Academy Award for Best Foreign Language Film.

**[3]**

> In 1962" O Pagador de Promessas" was also awarded best film and best musical score at the San Francisco international film festival and best film at the Acapulco( Mexico), Cartagena( Colombia), Karlovy Vary( Czechoslovakia) and Edinburgh( Scotland) international film festivals.

**[4]**

> His 1964 film ¨ Vereda da Salvação The Obsessed of Catule" was entered into the 15th Berlin International Film Festival.

**[5]**

> He also was a freemason.

**[6]**

> The President of Brazil, Luis Inacio Lula da Silva, awarded Duarte the Order of The Cultural Merit, Brazil's highest cultural civilian honor, and the Governor of São Paulo, José Serra, awarded Duarte the Order of Ipiranga, which is the state's highest civilian honor.

**[7]**

> Duarte was awarded titles of merit citizenship by numerous Brazilian municipalities including Rio de Janeiro, São Paulo and Salto, his birthplace.

**[8]**

> In 2009, the municipality of Salto inaugurated a multimillion- dollar cultural and educational center named" Centro Cultural e Educacional Anselmo Duarte", housing a 500 audience amphitheater for film and theatrical events.

**[9]**

> The center also displays for public view the original" Golden Palm" awarded to Duarte at the 1962 Cannes Film Festival.

**[10]**

> In 2008, at 88, Duarte founded a cultural organization( Instituto Anselmo Duarte) dedicated to restoring selected Brazilian films and creating special, free of charge, educational projects aimed at young filmmakers to improve their technical filmmaking skills.

**[11]**

> After his death, his son, Ricardo Duarte, 69, became the institute's president.

**[12]**

> Upon being diagnosed by suffering Alzheimer's dementia in 2002, Duarte spent his last 7 years of life under the care of his son, Ricardo, and his grandchild, Daphne, a preeminent Brazilian artist.

**[13]**

> Anselmo had 4 children.

**[14]**

> Reaching stage 6 on his Alzheimer illness condition a bladder cancer was detected which led to a severe blood hemorrhage, precipitating a heart stroke.

**[15]**

> Although both the bladder cancer and heart conditions had been successfully treated, a sudden massive hemorrhagic brain stroke left the legendary Brazilian actor and filmmaker in a coma for 6 days.

**[16]**

> Duarte died on November 7, 2009, due to complications from a stroke.

#### Document 5 — Abhishek Saxena

**[0]**

> Abhishek Saxena is an Indian Bollywood and Punjabi film director who directed the movie Phullu.

**[1]**

> The Phullu movie was released in theaters on 16 June 2017, in which film Sharib Hashmi is the lead role.

**[2]**

> Apart from these, he has also directed Patiala Dreamz, this is a Punjabi film.

**[3]**

> This film was screened in cinemas in 2014.

#### Document 6 — The Obsessed of Catule

**[0] SUPPORT**

> The Obsessed of Catule is a 1965 Brazilian drama film directed by Anselmo Duarte.

**[1]**

> It was entered into the 15th Berlin International Film Festival.

#### Document 7 — Constantin J. David

**[0] SUPPORT**

> Constantin J. David (18 February 1886 – 19 February 1964) was a German journalist, film director, film producer, and actor.

**[1]**

> He is also known for his marriage to the Hungarian actress, singer, and model Käthe von Nagy.

#### Document 8 — Brian Kennedy (gallery director)

**[0]**

> Brian Patrick Kennedy( born 5 November 1961) is an Irish- born art museum director who has worked in Ireland and Australia, and now lives and works in the United States.

**[1]**

> He is currently the director of the Peabody Essex Museum.

**[2]**

> He was the director of the Toledo Museum of Art in Ohio from 2010 to 2019.

**[3]**

> He was the director of the Hood Museum of Art from 2005 to 2010, and the National Gallery of Australia( Canberra) from 1997- 2004.

#### Document 9 — Drew Esocoff

**[0]**

> Drew Esocoff( born c. 1957) is an American television sports director, who as of 2006 has been the director of NBC Sunday Night Football.

#### Document 10 — Countess Ironing-Maid

**[0] SUPPORT**

> Countess Ironing- Maid( German: Gräfin Plättmamsell) is a 1926 German silent comedy film directed by Constantin J. David and starring Ossi Oswalda, Curt Bois and Robert Garrison.

**[1]**

> The film's sets were designed by the art director Rudi Feld.

### Additional Metadata

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "source_split": "dev",
  "source_id": "36ec2b3a086411ebbd5eac1f6bf848b6",
  "project_split": "debug",
  "type": "bridge_comparison",
  "answer_id": "Q7754647",
  "evidences_id": [],
  "entity_ids": "Q7754647_Q58411439_Q569649_Q1127862"
}
```

[Back to question index](#question-index)


<a id="question-03"></a>

## Question 03

**Dataset:** 2WikiMultiHopQA  
**Sample ID:** `2wikimultihopqa_378759440bdd11eba7f7acde48001122`  
**Review status:** `pending_human_review`

### Question

> Where was the director of film Being Twenty born?

### Reference Answer

> San Ferdinando di Puglia

### Annotated Supporting Sentences

**1. Being Twenty — sentence [0]**

> Being Twenty (also known as To Be Twenty) is a 1978 Italian erotic-drama film directed by Fernando Di Leo and starring Gloria Guida and Lilli Carati.

**2. Fernando Di Leo — sentence [0]**

> Fernando Di Leo( 11 January 1932 – 2 December 2003) was an Italian film director and script writer born in San Ferdinando di Puglia, Italy.

### Annotated Evidence Relations

| Subject | Relation | Object |
| --- | --- | --- |
| Being Twenty | director | Fernando Di Leo |
| Fernando Di Leo | place of birth | San Ferdinando di Puglia |

### Full Context

#### Document 1 — Ian Barry (director)

**[0]**

> Ian Barry is an Australian director of film and TV.

#### Document 2 — Jesse E. Hobson

**[0]**

> Jesse Edward Hobson( May 2, 1911 – November 5, 1970) was the director of SRI International from 1947 to 1955.

**[1]**

> Prior to SRI, he was the director of the Armour Research Foundation.

#### Document 3 — Brian Kennedy (gallery director)

**[0]**

> Brian Patrick Kennedy( born 5 November 1961) is an Irish- born art museum director who has worked in Ireland and Australia, and now lives and works in the United States.

**[1]**

> He is currently the director of the Peabody Essex Museum.

**[2]**

> He was the director of the Toledo Museum of Art in Ohio from 2010 to 2019.

**[3]**

> He was the director of the Hood Museum of Art from 2005 to 2010, and the National Gallery of Australia( Canberra) from 1997- 2004.

#### Document 4 — Olav Aaraas

**[0]**

> Olav Aaraas( born 10 July 1950) is a Norwegian historian and museum director.

**[1]**

> He was born in Fredrikstad.

**[2]**

> From 1982 to 1993 he was the director of Sogn Folk Museum, from 1993 to 2010 he was the director of Maihaugen and from 2001 he has been the director of the Norwegian Museum of Cultural History.

**[3]**

> In 2010 he was decorated with the Royal Norwegian Order of St. Olav.

#### Document 5 — S. N. Mathur

**[0]**

> S.N. Mathur was the Director of the Indian Intelligence Bureau between September 1975 and February 1980.

**[1]**

> He was also the Director General of Police in Punjab.

#### Document 6 — Fernando Di Leo

**[0] SUPPORT**

> Fernando Di Leo( 11 January 1932 – 2 December 2003) was an Italian film director and script writer born in San Ferdinando di Puglia, Italy.

**[1]**

> During his career from 1964 to 1985, Di Leo directed 20 films and was involved in the writing process in 43.

**[2]**

> His films influenced many popular contemporary directors, such as Quentin Tarantino and John Woo.

**[3]**

> Di Leo started his career mostly writing scripts for spaghetti westerns.

**[4]**

> He worked on the script for" Per un pugno di dollariA Fistful of Dollars", 1964) and later as assistant director and assistant to Sergio Leone in" Per qualche dollaro in più For a Few Dollars More", 1965).

**[5]**

> Later, he wrote scripts for such westerns as" Navajo Joe"( 1966) and" Johnny Yuma"( 1967).

**[6]**

> Di Leo is now best remembered for his" poliziotteschi" films, especially the" Milieu Trilogy", which he both wrote and directed.

**[7]**

> The trilogy contains" Caliber 9"( 1972)," La mala ordinaManhunt", 1972) and" Il Boss The Boss", 1973).

#### Document 7 — Giovanni Anni

**[0]**

> Giovanni Anni( born 8 May 1936) is an Italian field hockey player.

**[1]**

> He competed in the men's tournament at the 1960 Summer Olympics.

#### Document 8 — Mario Anni

**[0]**

> Mario Anni( born 22 November 1943) is an Italian racing cyclist.

**[1]**

> He rode in the 1970 Tour de France.

#### Document 9 — Peter Levin

**[0]**

> Peter Levin is an American director of film, television and theatre.

#### Document 10 — Being Twenty

**[0] SUPPORT**

> Being Twenty (also known as To Be Twenty) is a 1978 Italian erotic-drama film directed by Fernando Di Leo and starring Gloria Guida and Lilli Carati.

### Additional Metadata

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "source_split": "dev",
  "source_id": "378759440bdd11eba7f7acde48001122",
  "project_split": "debug",
  "type": "compositional",
  "answer_id": "Q23217",
  "evidences_id": [
    [
      "Q1114299",
      "director",
      "Q920161"
    ],
    [
      "Q920161",
      "place of birth",
      "Q23217"
    ]
  ],
  "entity_ids": "Q1114299_Q920161"
}
```

[Back to question index](#question-index)


<a id="question-04"></a>

## Question 04

**Dataset:** 2WikiMultiHopQA  
**Sample ID:** `2wikimultihopqa_37a7af5a0bb011ebab90acde48001122`  
**Review status:** `pending_human_review`

### Question

> Who is Margaret Fiennes, 11Th Baroness Dacre's paternal grandfather?

### Reference Answer

> Sir Thomas Fiennes

### Annotated Supporting Sentences

**1. Margaret Fiennes, 11th Baroness Dacre — sentence [1]**

> She was the daughter of Thomas Fiennes, 9th Baron Dacre who was executed for murder in the year of her birth.

**2. Thomas Fiennes, 9th Baron Dacre — sentence [1]**

> Dacre was the son of Sir Thomas Fiennes and Jane Sutton daughter of Edward Sutton, 2nd Baron Dudley.

### Annotated Evidence Relations

| Subject | Relation | Object |
| --- | --- | --- |
| Margaret Fiennes, 11th Baroness Dacre | father | Thomas Fiennes, 9th Baron Dacre |
| Thomas Fiennes, 9th Baron Dacre | father | Sir Thomas Fiennes |

### Full Context

#### Document 1 — Margaret Fiennes, 11th Baroness Dacre

**[0]**

> Margaret Fiennes, 11th Baroness Dacre (1541 – 16 March 1612) was a "suo jure" peeress having been created Baroness Dacre by King James I of England in 1604.

**[1] SUPPORT**

> She was the daughter of Thomas Fiennes, 9th Baron Dacre who was executed for murder in the year of her birth.

**[2]**

> His title and lands had been forfeited to the crown.

**[3]**

> Baroness Margaret's husband was Sampson Lennard MP.

**[4]**

> She was also known as Baroness Dacre of the South.

#### Document 2 — Gregory Fiennes, 10th Baron Dacre

**[0]**

> Gregory Fiennes, 10th Baron Dacre (25 June 1539, Hurstmonceaux, Sussex – 25 December 1594, Chelsea, Middlesex, England) was an English courtier.

**[1]**

> He was the son of Thomas Fiennes, 9th Baron Dacre (c. 1515-1541) and Mary Neville.

**[2]**

> His father was convicted of the murder of a gamekeeper and hanged like a common criminal at Tyburn in 1541, and the aftermath the family was stripped of its lands and titles by Henry VIII.

**[3]**

> In the following years, his mother battled to have the properties restored on behalf of her children, and on her ascension in 1558 Queen Elizabeth restored the title of Baron Dacre to Gregory, his elder brother Thomas having died of the plague at age 15.

**[4]**

> In 1565, he married Anne Sackville, daughter of Sir Richard Sackville and Winifred Brydges.

**[5]**

> They had one daughter, Elizabeth, who died young.

**[6]**

> Fiennes, his wife, and their daughter, are buried at Chelsea Old Church within a magnificent marble tomb.

**[7]**

> Fiennes also had an illegitimate daughter named Mary in about 1571, but no mention of this child is made in the tomb heraldry.

**[8]**

> Gregory Fiennes is a sitter with his mother in a significant portrait by Hans Eworth.

**[9]**

> He was succeeded by his sister Margaret Fiennes, 11th Baroness Dacre.

#### Document 3 — Thomas Fiennes, 9th Baron Dacre

**[0]**

> Thomas Fiennes, 9th Baron Dacre (ca. 1515 – 1541) was an English aristocrat notable for his conviction and execution for murder.

**[1] SUPPORT**

> Dacre was the son of Sir Thomas Fiennes and Jane Sutton daughter of Edward Sutton, 2nd Baron Dudley.

**[2]**

> When his father died in 1528 he became heir apparent to his grandfather's title and the family seat at Herstmonceux Castle in Sussex, and he succeeded to the title at the age of approximately 19 in 1533.

**[3]**

> In 1536 he married Mary Neville, daughter of George Neville, 5th Baron Bergavenny.

**[4]**

> They had three children.

**[5]**

> His only sister Anne married John Mantell, who was hanged along with his brother-in-law.

**[6]**

> He was a member of the jury at the trial of Anne Boleyn in 1536, and of Thomas, Lord Darcy, and John, Lord Hussey in May 1537 (for their part in the Pilgrimage of Grace), and of Baron Montagu and the Marquess of Exeter in 1538 for the Exeter Conspiracy.

**[7]**

> On 30 April 1541 Dacre led a party of gentlemen including his brother-in-law John Mantell, John Frowds, George Roidon, Thomas Isleie, and two yeomen Richard Middleton and John Goldwell, to poach on the lands of Sir Nicholas Pelham of Laughton.

**[8]**

> During the escapade they encountered John Busbrig (or Busbridge), James Busbrig, and Richard Summer who were servants of Pelham.

**[9]**

> The encounter turned into an affray during which John Busbrig was fatally wounded.

**[10]**

> Dacre and several others were charged with murder and arraigned before the Lord High Steward, Lord Audley of Walden on 27 June.

**[11]**

> Dacre originally entered a plea of not guilty but was later persuaded to change it to guilty and throw himself upon the King's mercy in the hope of a reprieve.

**[12]**

> Unlike many of his contemporaries he was not executed by beheading but was hanged at Tyburn on 29 June 1541.

**[13]**

> An account of the execution in Hall's Chronicle says:
> Mantell, Frowds and Roidon were also executed for the crime.

**[14]**

> Dacre's family were stripped of their lands and title, but the title was restored to his second son Gregory in 1558

**[15]**

> (the elder son Thomas died before the restitution, aged 15).

#### Document 4 — Sampson Lennard

**[0]**

> Sampson Lennard( died 20 September 1615), of Chevening in Kent, was an English Member of Parliament who represented an unusually large number of different constituencies during the reigns of Elizabeth I and James I.

**[1]**

> A prominent member of the Kent and Sussex gentry, Lennard was High Sheriff of Kent in 1590 – 1.

**[2]**

> He entered Parliament in 1571 as member for Launceston( Cornwall).

**[3]**

> He subsequently also represented Bramber( 1584 – 5), St Mawes( 1586 – 7), Christchurch( 1589), St Germans( 1593), Rye( 1597), Liskeard( 1601) and Sussex( 1614).

**[4]**

> Lennard married Margaret Fiennes( 1541 – 1612), daughter of Thomas Fiennes, 9th Baron Dacre, and after her brother's death in 1594 he successfully claimed the barony on her behalf, so that she became the 11th Baroness Dacre.

**[5]**

> They had seven children, and their younger son, Sir Henry Lennard( 1570 – 1616), succeeded his mother as 12th Baron Dacre.

#### Document 5 — Robert More

**[0]**

> Sir Robert More( 21 May

**[1]**

> 1581 – February 1626) was an English politician who sat in the House of Commons from 1601.

**[2]**

> More was the eldest son of Sir George More of Loseley and his first wife Anne Poynings, daughter of Sir Adrian Poynings.

**[3]**

> He entered Corpus Christi College, Oxford in 1595 and was awarded BA in 1598.

**[4]**

> In 1600 he entered the Inner Temple, and also became with his father joint keeper of Farnham Little Park.

**[5]**

> In 1601, More was elected Member of Parliament for Guildford.

**[6]**

> He was knighted between 17 October 1601 and 28 February 1604.

**[7]**

> He was joint constable with his father of Farnham Castle from about 1603 to 1608 and probably became a gentleman pensioner early in the reign of King James.

**[8]**

> In 1604 he was elected MP for Surrey.

**[9]**

> He was a J.P. for Surrey during the reign of James I.

**[10]**

> In 1614 he was elected MP for Guildford again.

**[11]**

> He was a Deputy Lieutenant of Surrey by 1619.

**[12]**

> In 1621 he was re-elected MP for Guildford.

**[13]**

> He was elected MP for Surrey again in 1624 and was elected MP for Guildford again in 1625.

**[14]**

> More died on 2 or 10 February 1626 at the age of 44 and was outlived by his father.

**[15]**

> He was buried in the Loseley chapel at St Nicholas ’s, Guildford.

**[16]**

> More married Frances Lennard, daughter of Sampson Lennard and his wife Margaret Fiennes, 11th Baroness Dacre.

**[17]**

> They had six sons and five daughters.

#### Document 6 — Kaya Alp

**[0]**

> Kaya Alp was, according to Ottoman tradition, the son of Kızıl Buğa and the father of Suleyman Shah, who was, in turn, the grandfather of Ertuğrul, and the great grandfather of the Ottoman Empire founder, Osman I.

#### Document 7 — Abd al-Muttalib

**[0]**

> Abd al- Muttalib Shaybah ibn Hashim( c. 497 – 578) was the grandfather of Islamic prophet Muhammad.

#### Document 8 — Anne Sackville, Baroness Dacre

**[0]**

> Anne Fiennes, Baroness Dacre( died 10 May 1595) was an English gentlewoman and benefactress.

#### Document 9 — Henry Lennard, 12th Baron Dacre

**[0]**

> Henry Lennard, 12th Baron Dacre (25 March 1570 – 8 August 1616) was an English baron and politician.

**[1]**

> He was the son of Margaret Fiennes, 11th Baroness Dacre and Sampson Lennard.

**[2]**

> He was the Member of Parliament for West Looe in 1597–1598 and Baron Dacre.

**[3]**

> He married in 1589 Chrysogona Baker, by whom he had issue:

#### Document 10 — Lyon Cohen

**[0]**

> Lyon Cohen( 1868–1937) was a Polish- born Canadian businessman and a philanthropist.

**[1]**

> He was the grandfather of singer/ poet Leonard Cohen.

### Additional Metadata

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "source_split": "dev",
  "source_id": "37a7af5a0bb011ebab90acde48001122",
  "project_split": "debug",
  "type": "inference",
  "answer_id": "Q75272765",
  "evidences_id": [
    [
      "Q6759401",
      "father",
      "Q7789582"
    ],
    [
      "Q7789582",
      "father",
      "Q75272765"
    ]
  ],
  "entity_ids": "Q6759401_Q7789582"
}
```

[Back to question index](#question-index)


<a id="question-05"></a>

## Question 05

**Dataset:** 2WikiMultiHopQA  
**Sample ID:** `2wikimultihopqa_39751c8a08d811ebbd9aac1f6bf848b6`  
**Review status:** `pending_human_review`

### Question

> Who was born later, Mark Gurr or William Eythe?

### Reference Answer

> Mark Gurr

### Annotated Supporting Sentences

**1. Mark Gurr — sentence [0]**

> Mark Gurr( born February 18, 1966) is a retired tennis player from Zimbabwe, who represented his native country as a qualifier at the 1988 Summer Olympics in Seoul, South Korea.

**2. William Eythe — sentence [0]**

> William Eythe( April 7, 1918 – January 26, 1957) was an American actor of film, radio, television and stage.

### Annotated Evidence Relations

| Subject | Relation | Object |
| --- | --- | --- |
| Mark Gurr | date of birth | February 18, 1966 |
| William Eythe | date of birth | April 7, 1918 |

### Full Context

#### Document 1 — William of St. Barbara

**[0]**

> William of St. Barbara or William of Ste Barbe( died 1152) was a medieval Bishop of Durham.

#### Document 2 — William Middleton (bishop)

**[0]**

> William Middleton( or William de Middleton; died 31 August or 1 September 1288) was a medieval Bishop of Norwich.

#### Document 3 — William Eythe

**[0] SUPPORT**

> William Eythe( April 7, 1918 – January 26, 1957) was an American actor of film, radio, television and stage.

#### Document 4 — William de Turbeville

**[0]**

> William de Turbeville( or William Turbe; c. 1095 – January 1174) was a medieval Bishop of Norwich.

#### Document 5 — William Lamb alias Paniter

**[0]**

> William Lamb, or William Paniter alias Lamb,( c. 1493- 1550) was a Scottish cleric, lawyer, and author.

#### Document 6 — W. Augustus Barratt

**[0]**

> W. Augustus Barratt( 1873- 1947) was a Scottish- born, later American, songwriter and musician.

#### Document 7 — Mark Gurr

**[0] SUPPORT**

> Mark Gurr( born February 18, 1966) is a retired tennis player from Zimbabwe, who represented his native country as a qualifier at the 1988 Summer Olympics in Seoul, South Korea.

**[1]**

> There he lost in the first round of the men's singles competition to Spain's Sergio Casal.

**[2]**

> He lost in the second round of the men's doubles competition to Sweden's eventual bronze medalists Anders Järryd and Stefan Edberg, while partnering Philip Tuckniss.

**[3]**

> Mark went to Oriel Boys High School in Harare together with Byron Black and Graig Rodgers, and played in the Davis Cup.

#### Document 8 — William Scott, Lord Balwearie

**[0]**

> Sir William Scott, Lord Balwearie( died 1532), or William Scot, was a Scottish judge.

#### Document 9 — William of March

**[0]**

> William of March( or William March; died 1302) was a medieval Treasurer of England and a Bishop of Bath and Wells.

#### Document 10 — Catherine I of Russia

**[0]**

> Catherine I( born, later known as Marta Samuilovna Skavronskaya; –) was the second wife of Peter the Great and Empress of Russia from 1725 until her death.

### Additional Metadata

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "source_split": "dev",
  "source_id": "39751c8a08d811ebbd9aac1f6bf848b6",
  "project_split": "debug",
  "type": "comparison",
  "answer_id": "Q6767844",
  "evidences_id": [],
  "entity_ids": "Q6767844_Q3568601"
}
```

[Back to question index](#question-index)


<a id="question-06"></a>

## Question 06

**Dataset:** 2WikiMultiHopQA  
**Sample ID:** `2wikimultihopqa_4f8e349e08e111ebbda2ac1f6bf848b6`  
**Review status:** `pending_human_review`

### Question

> Which film has the director who died later, Hotel Paradis or Devil'S Doorway?

### Reference Answer

> Devil'S Doorway

### Annotated Supporting Sentences

**1. Hotel Paradis — sentence [0]**

> Hotel Paradis is a 1931 Danish drama directed by George Schnéevoigt.

**2. Devil's Doorway — sentence [0]**

> Devil's Doorway is a 1950 western film directed by Anthony Mann and starring Robert Taylor as an Indian who returns home from the American Civil War a hero awarded the Medal of Honor.

**3. George Schnéevoigt — sentence [0]**

> George Schnéevoigt( 23 December 1893 – 6 February 1961) was a Danish film director, cinematographer, and actor of the 1930s and early 1940s.

**4. Anthony Mann — sentence [0]**

> Anthony Mann( June 30, 1906 – April 29, 1967) was an American actor and film director, best remembered for his work in the film noir and Westerns genres.

### Annotated Evidence Relations

| Subject | Relation | Object |
| --- | --- | --- |
| Hotel Paradis | director | George Schnéevoigt |
| Devil's Doorway | director | Anthony Mann |
| George Schnéevoigt | date of death | 6 February 1961 |
| Anthony Mann | date of death | April 29, 1967 |

### Full Context

#### Document 1 — Abhishek Saxena

**[0]**

> Abhishek Saxena is an Indian Bollywood and Punjabi film director who directed the movie Phullu.

**[1]**

> The Phullu movie was released in theaters on 16 June 2017, in which film Sharib Hashmi is the lead role.

**[2]**

> Apart from these, he has also directed Patiala Dreamz, this is a Punjabi film.

**[3]**

> This film was screened in cinemas in 2014.

#### Document 2 — George Schnéevoigt

**[0] SUPPORT**

> George Schnéevoigt( 23 December 1893 – 6 February 1961) was a Danish film director, cinematographer, and actor of the 1930s and early 1940s.

**[1]**

> Schnéevoigt was born in Copenhagen, Denmark to actress Siri Schnéevoigt, and he is the father of actor and director Alf Schnéevoigt.

#### Document 3 — Devil's Doorway

**[0] SUPPORT**

> Devil's Doorway is a 1950 western film directed by Anthony Mann and starring Robert Taylor as an Indian who returns home from the American Civil War a hero awarded the Medal of Honor.

**[1]**

> However, his hopes for a peaceful life are shattered by bigotry and greed.

#### Document 4 — G. Marthandan

**[0]**

> G. Marthandan is an Indian film director who works in Malayalam cinema.

#### Document 5 — Witchboard 2: The Devil's Doorway

**[0]**

> Witchboard 2: The Devil's Doorway is a 1993 American supernatural horror film written and directed by Kevin S. Tenney.

**[1]**

> It stars Ami Dolenz as an artist possessed by a ghost of a former occupant of her new apartment.

**[2]**

> The film is a sequel to the 1986 film" Witchboard".

#### Document 6 — James Strange French

**[0]**

> James Strange French( 1807- 1886) was a lawyer, novelist, and later hotel keeper.

#### Document 7 — Ben Palmer

**[0]**

> Ben Palmer is a British film and television director who is known for being the director of" Bo' Selecta" and" The Inbetweeners".

#### Document 8 — Hotel Paradis

**[0] SUPPORT**

> Hotel Paradis is a 1931 Danish drama directed by George Schnéevoigt.

**[1]**

> The film, based on a novel by Einar Rousthøj, stars Eyvind Johan- Svendsen and Inger Stender.

**[2]**

> The film was also known as" Hotel Paradisets hemlighed The Secret of the Paradise Hotel").

#### Document 9 — Next Stop Paradise (1980 film)

**[0]**

> Næste Stop Paradis or Next Stop Paradise is a 1980 Danish romantic drama film directed and written by Jon Bang Carlsen.

**[1]**

> The film stars Karen Lykkehus.

#### Document 10 — Anthony Mann

**[0] SUPPORT**

> Anthony Mann( June 30, 1906 – April 29, 1967) was an American actor and film director, best remembered for his work in the film noir and Westerns genres.

**[1]**

> As a director, he often collaborated with the cinematographer John Alton.

**[2]**

> He directed films for a variety of production companies, from RKO to MGM, and worked with many major stars of the era.

**[3]**

> He made several Westerns with James Stewart, such as" Winchester'73"( 1950), and he was the director of the medieval epic" El Cid"( 1961), working with Charlton Heston and Sophia Loren.

**[4]**

> He also directed the big- budget film" Cimarron"( 1960), which starred Glenn Ford and Maria Schell.

### Additional Metadata

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "source_split": "dev",
  "source_id": "4f8e349e08e111ebbda2ac1f6bf848b6",
  "project_split": "debug",
  "type": "bridge_comparison",
  "answer_id": "Q3211814",
  "evidences_id": [],
  "entity_ids": "Q5911826_Q3211814_Q3101912_Q269975"
}
```

[Back to question index](#question-index)


<a id="question-07"></a>

## Question 07

**Dataset:** 2WikiMultiHopQA  
**Sample ID:** `2wikimultihopqa_94415cd008e911ebbda7ac1f6bf848b6`  
**Review status:** `pending_human_review`

### Question

> Are Brian Part and John Mosca both from the same country?

### Reference Answer

> yes

### Annotated Supporting Sentences

**1. Brian Part — sentence [0]**

> Brian Part( born March 24, 1962 in Los Angeles, California) was an American child actor best known for his role of the adopted son of Mr. Edwards( Victor French) on television's" Little House on the Prairie".

**2. John Mosca — sentence [1]**

> ( May 6, 1925 Chicago Heights, Illinois – July 13, 2011, Harahan, Louisiana) was an American restaurateur and owner( and co-founder) of the famed Mosca's, a Louisiana Creole and Italian restaurant in Avondale, Louisiana, near New Orleans.

### Annotated Evidence Relations

| Subject | Relation | Object |
| --- | --- | --- |
| Brian Part | country of citizenship | American |
| John Mosca | country of citizenship | American |

### Full Context

#### Document 1 — Godwin Davy

**[0]**

> Godwin Davy( born 15 December 1979) is an Anguillan international footballer who plays as a goalkeeper.

**[1]**

> He made his international debut in a World Cup qualifying match against El Salvador, resulting in a lopsided match, losing 12- 0 in February 2008, and also played in the 4 – 0 loss to the same country in the return match in March 2008.

#### Document 2 — Andy Linden (actor)

**[0]**

> Andy Linden is an English actor.

**[1]**

> He is best known for his roles as Mundungus Fletcher in" Harry Potter and the Deathly Hallows – Part 1" and John the Watch in" Count Arthur Strong".

#### Document 3 — Willem Brakman

**[0]**

> Willem Pieter Jacobus Brakman( 1922 – 2008) was a Dutch writer who made his literary debut with the novel" Een winterreis" in 1961.

**[1]**

> Brakman received the P. C. Hooft Award in 1980.

**[2]**

> He was born on June 13th, 1922 in The Hague, Netherlands, and died on May 8th, 2008 in the same country.

#### Document 4 — Dusted (Canadian band)

**[0]**

> Dusted is a Canadian indie rock band, whose core members are Brian Borcherdt and Leon Taheny.

**[1]**

> Their music features Borchert's songs and vocals.

#### Document 5 — 2001–02 UEFA Champions League second group stage

**[0]**

> Eight winners and eight runners- up from the first group stage were drawn into four groups of four teams, each containing two group winners and two runners- up.

**[1]**

> Teams from the same country or from the same first round group could not be drawn together.

**[2]**

> The top two teams in each group advanced to the quarter- finals.

#### Document 6 — Brian Part

**[0] SUPPORT**

> Brian Part( born March 24, 1962 in Los Angeles, California) was an American child actor best known for his role of the adopted son of Mr. Edwards( Victor French) on television's" Little House on the Prairie".

**[1]**

> He now writes and performs music with his wife Melody Part.

#### Document 7 — Kala (band)

**[0]**

> KALA is a Filipino band that blends funk, nu- disco, acid jazz, electronic and rock music.

**[1]**

> Its members are Brian Tanchanco, Raymond Daylo, and Jade Justine.

#### Document 8 — John Mosca

**[0]**

> John Mosca( pronounced" Mohsca")

**[1] SUPPORT**

> ( May 6, 1925 Chicago Heights, Illinois – July 13, 2011, Harahan, Louisiana) was an American restaurateur and owner( and co-founder) of the famed Mosca's, a Louisiana Creole and Italian restaurant in Avondale, Louisiana, near New Orleans.

#### Document 9 — Ming Luhulima

**[0]**

> Ming Luhulima aka Lou Lima was a well known Netherlands based recording artist originally from the Maluku Islands which were part of the Dutch East Indies.

**[1]**

> He made multiple recordings during his career.

**[2]**

> One of the artists he was closely associated with was Rudi Wairata.

**[3]**

> Not only did Luhulima come from the same country as Wairata, he also recorded music in the same genre.

**[4]**

> He was also a member of the Amboina Serenaders and the Mena Moeria Minstrels.

**[5]**

> He also led the Krontjong Ensemble Pantja Warna.

#### Document 10 — Kyōen Kobanzame

**[0]**

> There are two parts of the film: the first part and the second part.

**[1]**

> Both parts have the same staff and the same actors.

### Additional Metadata

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "source_split": "dev",
  "source_id": "94415cd008e911ebbda7ac1f6bf848b6",
  "project_split": "debug",
  "type": "comparison",
  "answer_id": null,
  "evidences_id": [
    [
      "Q2924973",
      "country of citizenship",
      "Q30"
    ],
    [
      "Q6249594",
      "country of citizenship",
      "Q30"
    ]
  ],
  "entity_ids": "Q2924973_Q6249594"
}
```

[Back to question index](#question-index)


<a id="question-08"></a>

## Question 08

**Dataset:** 2WikiMultiHopQA  
**Sample ID:** `2wikimultihopqa_d2f969d40bd911eba7f7acde48001122`  
**Review status:** `pending_human_review`

### Question

> What is the place of birth of the director of film A Nightmare On Elm Street 5: The Dream Child?

### Reference Answer

> Jamaican

### Annotated Supporting Sentences

**1. A Nightmare on Elm Street 5: The Dream Child — sentence [1]**

> It is the fifth installment in the" A Nightmare on Elm Street" film series, and stars Lisa Wilcox, and Robert Englund as Freddy Krueger.

**2. Stephen Hopkins (director) — sentence [0]**

> Stephen Hopkins is a Jamaican-born British-Australian director and producer of film and television.

### Annotated Evidence Relations

| Subject | Relation | Object |
| --- | --- | --- |
| A Nightmare on Elm Street 5: The Dream Child | director | Stephen Hopkins |
| Stephen Hopkins | place of birth | Jamaican |

### Full Context

#### Document 1 — A Nightmare on Elm Street

**[0]**

> A Nightmare on Elm Street is a 1984 American slasher film written and directed by Wes Craven, and produced by Robert Shaye.

**[1]**

> It is the first installment in the" A Nightmare on Elm Street" film series and stars Heather Langenkamp, John Saxon, Ronee Blakley, Robert Englund as Freddy Krueger, and Johnny Depp in his film debut.

**[2]**

> The plot concerns four teenagers living on one street in the fictitious town of Springwood, Ohio, who are invaded and killed in their dreams, and thus killed in reality, by a burnt killer with a bladed leather glove.

**[3]**

> Craven filmed" A Nightmare on Elm Street" on an estimated budget of$ 1.8 million, a sum the film earned back during its first week.

**[4]**

> The film was released on November 9, 1984, where it went on to gross over$ 25 million at the United States box office.

**[5]**

> " A Nightmare on Elm Street" was met with rave critical reviews and is considered to be one of the greatest horror films ever made, spawning a franchise consisting of six sequels, a television series, a crossover with" Friday the 13th", and various other merchandise.

**[6]**

> A remake of the same name was released in 2010.

**[7]**

> The film is credited with using many of the tropes found in the low- budget horror films of the 1970s and 1980s that originated with John Carpenter's" Halloween"( 1978) and led this subgenre to be called the slasher film.

**[8]**

> The film includes a morality play where sexually promiscuous teenagers are killed.

**[9]**

> Critics and film historians state that the film's premise is the struggle to define the distinction between dreams and reality, manifested by the lives and dreams of the teens in the film.

**[10]**

> Critics today praise the film's ability to transgress" the boundaries between the imaginary and real", toying with audience perceptions.

**[11]**

> The film was followed by.

#### Document 2 — A Nightmare on Elm Street 4: The Dream Master

**[0]**

> A Nightmare on Elm Street 4: The Dream Master is a 1988 American fantasy slasher film and the fourth installment in the" Nightmare on Elm Street" series.

**[1]**

> The film was directed by Renny Harlin and stars Robert Englund, Lisa Wilcox, and Danny Hassel.

**[2]**

> Following the death of Nancy Thompson, Freddy Krueger reappears in the dreams of Kristen Parker, Joey Crusel, and Roland Kincaid.

**[3]**

> After completing his revenge against the families who killed him, Krueger uses Kristen's best friend, Alice Johnson, to gain access to new victims in order to sate his murderous needs.

**[4]**

> The film is a sequel to( 1987) and was followed by( 1989).

**[5]**

> " The Dream Master" is often popularly referred to as" the MTV Nightmare" of the franchise.

**[6]**

> The film was released on August 19, 1988.

**[7]**

> It grossed$ 49.4 million at the box office on a budget of$ 13 million, which made it the highest- grossing film in the franchise until the release of" Freddy vs. Jason", a crossover with the" Friday the 13th" film series, in 2003.

#### Document 3 — A Nightmare on Elm Street 3: Dream Warriors

**[0]**

> A Nightmare on Elm Street 3: Dream Warriors is a 1987 American fantasy slasher film directed by Chuck Russell.

**[1]**

> The story was developed by Wes Craven and Bruce Wagner.

**[2]**

> It is the third installment in the" Nightmare on Elm Street" series and stars Heather Langenkamp, Patricia Arquette, Larry Fishburne, Priscilla Pointer, Craig Wasson, and Robert Englund as Freddy Krueger.

**[3]**

> The plot centers around the antagonist, who seeks to murder the remaining children of the parents who burned him to death.

**[4]**

> The kids are committed to a psychiatric hospital where Nancy Thompson, whose parents helped to kill Krueger, works.

**[5]**

> Freddy does not know that Nancy is training the kids to control their dreams in order to fight him.

**[6]**

> " Dream Warriors" was theatrically released on February 27, 1987, and grossed$ 44.8 million on a budget of$ 5 million.

**[7]**

> The film was followed by a sequel,, a year later.

#### Document 4 — Niki Marvin

**[0]**

> Niki Marvin is a film producer active since the 1980s.

**[1]**

> ...

**[2]**

> aka A Nightmare On Elm Street Part III( USA: closing credits title)

#### Document 5 — A Nightmare on Elm Street 2: Freddy's Revenge

**[0]**

> A Nightmare on Elm Street 2: Freddy's Revenge is a 1985 American slasher film directed by Jack Sholder and written by David Chaskin.

**[1]**

> It stars Mark Patton, Kim Myers, Robert Englund as Freddy Krueger, and Robert Rusler.

**[2]**

> It is the second installment in the" A Nightmare on Elm Street" film series.

**[3]**

> The film follows Jesse Walsh, a teenager who begins having recurring nightmares about Freddy Krueger after moving into the former home of Nancy Thompson from the first film.

**[4]**

> " Freddy's Revenge" was released on November 1, 1985, and grossed$ 30 million at the box office on a budget of$ 3 million.

**[5]**

> It received mixed reviews from critics upon release, with many comparing it unfavorably to its predecessor.

**[6]**

> However, it has enjoyed later success as a cult classic, with critics having reassessed the film's homoerotic themes and subject material.

**[7]**

> It was distributed by New Line Cinema.

**[8]**

> The film was followed by.

#### Document 6 — A Nightmare on Elm Street (2010 film)

**[0]**

> A Nightmare on Elm Street is a 2010 American slasher film directed by Samuel Bayer, and written by Wesley Strick and Eric Heisserer.

**[1]**

> The film stars Jackie Earle Haley, Kyle Gallner, Rooney Mara, Katie Cassidy, Thomas Dekker, and Kellan Lutz.

**[2]**

> It is a remake of Wes Craven's 1984 film of the same name.

**[3]**

> Produced by Michael Bay and Platinum Dunes, the film was designed to reboot the "Nightmare on Elm Street" franchise and is the ninth installment in the series.

**[4]**

> The film is set in a fictitious town of Ohio and centers around a group of teenagers living on one street who are stalked and murdered in their dreams by a disfigured man named Freddy Krueger.

**[5]**

> The teenagers discover that they all share a common link from their childhood that makes them targets for Krueger.

**[6]**

> In January 2008, Variety reported that Bay and his Platinum Dunes production company would be rebooting the "Nightmare on Elm Street" franchise with a remake of the original 1984 film. "

**[7]**

> A Nightmare on Elm Street" was originally to follow the same design as Platinum Dunes' other remake, "Friday the 13th", where the writers took the best elements from each of the films in the original series and created a single storyline with them.

**[8]**

> Eventually, they decided to use Craven's original storyline but tried to create a scarier film.

**[9]**

> To that end, they decided to remove the one-line quipping Freddy, who had become less scary and more comical over the years, and bring back his darker nature.

**[10]**

> The writers developed the character to be a child molester, something that Craven wanted to do originally in 1984 but changed to a child killer instead.

**[11]**

> Freddy's physical appearance was changed with the use of computer-generated imagery to be closer to that of a burn victim.

**[12]**

> Because of the positive experiences Platinum Dunes' producers had in the area, "A Nightmare on Elm Street" was filmed primarily in Illinois.

**[13]**

> Craven expressed his displeasure when he was not consulted on the project.

**[14]**

> Robert Englund, who portrayed Freddy in the previous eight films, voiced his support of the remake and the casting of Haley in the role of Freddy.

**[15]**

> "A Nightmare on Elm Street" was produced by New Line Cinema and had its world premiere at Hollywood on April 27, 2010, and was theatrically released in North America on April 30, 2010, by Warner Bros. Pictures.

**[16]**

> The film received generally negative reviews from critics, who criticized the teenage characters and story while offering some praise for Bayer's direction and Haley's performance.

**[17]**

> Regardless, "A Nightmare on Elm Street" broke the record for midnight openings for a horror film and grossed more in its opening weekend than the total gross of four other "Nightmare on Elm Street" films.

**[18]**

> The film earned over $63 million at the domestic box office and over $115 million worldwide.

#### Document 7 — Stephen Hopkins (director)

**[0] SUPPORT**

> Stephen Hopkins is a Jamaican-born British-Australian director and producer of film and television.

**[1]**

> He directed "Predator 2Blown

**[2]**

> AwayThe Life and Death of Peter Sellers", and the Jesse Owens

**[3]**

> biopic "Race".

**[4]**

> He also produced and directed several episodes of the first season of "24".

#### Document 8 — A Nightmare on Elm Street 5: The Dream Child

**[0]**

> A Nightmare on Elm Street 5: The Dream Child is a 1989 American gothic slasher film directed by Stephen Hopkins and written by Leslie Bohem.

**[1] SUPPORT**

> It is the fifth installment in the" A Nightmare on Elm Street" film series, and stars Lisa Wilcox, and Robert Englund as Freddy Krueger.

**[2]**

> The film follows Krueger, using a now pregnant Alice Johnson's baby's dreams to claim new victims.

**[3]**

> The film's general tone is much darker than that of the previous films.

**[4]**

> A blue filter lighting technique is used in most of the scenes.

**[5]**

> It is one of the final slasher films released in the 1980s.

**[6]**

> " The Dream Child" was released on August 11, 1989, and grossed$ 22.2 million at the box office on a budget of$ 6 million.

**[7]**

> The film was followed by( 1991).

#### Document 9 — A Wet Dream on Elm Street

**[0]**

> A Wet Dream on Elm Street is a 2011 pornographic horror film written and directed by Lee Roy Myers and starring Sophie Dee, Gracie Glam, Giselle Leon, Tommy Pistol, Jennifer White, Chris Johnson, Charley Chase, and Anthony Rosano.

**[1]**

> It is a parody of the 1984 horror film classic" A Nightmare on Elm Street".

#### Document 10 — Freddy vs. Jason

**[0]**

> Freddy vs. Jason is a 2003 American slasher film directed by Ronny Yu and written by Damian Shannon and Mark Swift.

**[1]**

> The film, a crossover between the" A Nightmare on Elm Street" and" Friday the 13th" series, retroactively establishes them in a shared universe and pits Freddy Krueger and Jason Voorhees against each other.

**[2]**

> It is the last film in each series before their respective reboots, and the last to feature Robert Englund as Freddy Krueger.

**[3]**

> The film is the eighth in the" A Nightmare on Elm Street" franchise and the eleventh in the" Friday the 13th" franchise.

**[4]**

> In the film, Freddy( Robert Englund) has become incapable of haunting people's dreams; the residents of Springwood, Ohio, have largely forgotten about him after his death and descent into hell.

**[5]**

> To regain his power( and freedom), he resurrects Jason( Ken Kirzinger) and manipulates him into traveling to Springwood to cause panic and fear; this sparks rumors that Freddy has returned.

**[6]**

> Although Jason arouses enough fear for Freddy to haunt the town again, he angers Freddy by depriving him of potential victims.

**[7]**

> This culminates in a climactic battle between the two supernatural killers.

**[8]**

> " Freddy vs. Jason" was released in the United States on August 15, 2003.

**[9]**

> It grossed$ 114 million, the highest- grossing film in the" Friday the 13th" series and the second- highest- grossing film in the" Nightmare on Elm Street" series.

**[10]**

> The film is Englund's final cinematic appearance as Freddy Krueger, although he appeared as the character in an episode of" The Goldbergs".

### Additional Metadata

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "source_split": "dev",
  "source_id": "d2f969d40bd911eba7f7acde48001122",
  "project_split": "debug",
  "type": "compositional",
  "answer_id": "Q766",
  "evidences_id": [
    [
      "Q1410735",
      "director",
      "Q709076"
    ],
    [
      "Q709076",
      "place of birth",
      "Q766"
    ]
  ],
  "entity_ids": "Q1410735_Q709076"
}
```

[Back to question index](#question-index)


<a id="question-09"></a>

## Question 09

**Dataset:** Custom  
**Sample ID:** `custom_nasa_apollo11`  
**Review status:** `pending_human_review`

### Question

> On what date did Apollo 11 launch, and on what date did it splash down on Earth?

### Reference Answer

> Launch: July 16, 1969. Splashdown: July 24, 1969.

### Annotated Supporting Sentences

**1. Apollo 11 — launch — sentence [0]**

> Apollo 11 launched on July 16, 1969.

**2. Apollo 11 — splashdown — sentence [0]**

> Apollo 11 returned to Earth with splashdown on July 24, 1969.

### Source Records

**url:**

<https://www.nasa.gov/mission/apollo-11/>

**accessed_date:**

> 2026-10-15

**publisher:**

> NASA

**source_excerpt:**

> Launch
> July 16, 1969
> SPLASHDOWN
> July 24, 1969

**review_status:**

> pending_human_review

### Full Context

#### Document 1 — Apollo 11 — launch

**[0] SUPPORT**

> Apollo 11 launched on July 16, 1969.

#### Document 2 — Apollo 11 — splashdown

**[0] SUPPORT**

> Apollo 11 returned to Earth with splashdown on July 24, 1969.

### Additional Metadata

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "source_split": "custom_debug",
  "source_id": "nasa_apollo11",
  "project_split": "debug",
  "type": "custom_multipart",
  "context_origin": "source-derived paraphrases for debug only"
}
```

[Back to question index](#question-index)


<a id="question-10"></a>

## Question 10

**Dataset:** Custom  
**Sample ID:** `custom_nasa_perseverance`  
**Review status:** `pending_human_review`

### Question

> On what date did Perseverance launch, and on what date did it land on Mars?

### Reference Answer

> Launch: July 30, 2020. Mars landing: February 18, 2021.

### Annotated Supporting Sentences

**1. Perseverance — launch — sentence [0]**

> The Perseverance mission launched on July 30, 2020.

**2. Perseverance — Mars landing — sentence [0]**

> Perseverance landed on Mars on February 18, 2021.

### Source Records

**url:**

<https://science.nasa.gov/mission/mars-2020-perseverance/>

**accessed_date:**

> 2026-10-15

**publisher:**

> NASA

**source_excerpt:**

> Launch / Landing
> July 30, 2020 / Feb. 18, 2021

**review_status:**

> pending_human_review

### Full Context

#### Document 1 — Perseverance — launch

**[0] SUPPORT**

> The Perseverance mission launched on July 30, 2020.

#### Document 2 — Perseverance — Mars landing

**[0] SUPPORT**

> Perseverance landed on Mars on February 18, 2021.

### Additional Metadata

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "source_split": "custom_debug",
  "source_id": "nasa_perseverance",
  "project_split": "debug",
  "type": "custom_multipart",
  "context_origin": "source-derived paraphrases for debug only"
}
```

[Back to question index](#question-index)


<a id="question-11"></a>

## Question 11

**Dataset:** Custom  
**Sample ID:** `custom_nasa_voyager1`  
**Review status:** `pending_human_review`

### Question

> On what date did Voyager 1 launch, and on what date was its closest approach to Jupiter?

### Reference Answer

> Launch: September 5, 1977. Jupiter closest approach: March 5, 1979.

### Annotated Supporting Sentences

**1. Voyager 1 — launch — sentence [0]**

> The launch date of Voyager 1 was September 5, 1977.

**2. Voyager 1 — Jupiter flyby — sentence [0]**

> Voyager 1 made its closest approach to Jupiter on March 5, 1979.

### Source Records

**url:**

<https://science.nasa.gov/mission/voyager/voyager-1/>

**accessed_date:**

> 2026-10-15

**publisher:**

> NASA

**source_excerpt:**

> Launch Date and Time | Sept. 5, 1977 / 12:56:01 UT
> Key Dates | March 5, 1979: Jupiter flyby - closest approach

**review_status:**

> pending_human_review

### Full Context

#### Document 1 — Voyager 1 — launch

**[0] SUPPORT**

> The launch date of Voyager 1 was September 5, 1977.

#### Document 2 — Voyager 1 — Jupiter flyby

**[0] SUPPORT**

> Voyager 1 made its closest approach to Jupiter on March 5, 1979.

### Additional Metadata

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "source_split": "custom_debug",
  "source_id": "nasa_voyager1",
  "project_split": "debug",
  "type": "custom_multipart",
  "context_origin": "source-derived paraphrases for debug only"
}
```

[Back to question index](#question-index)


<a id="question-12"></a>

## Question 12

**Dataset:** Custom  
**Sample ID:** `custom_nasa_voyager2`  
**Review status:** `pending_human_review`

### Question

> On what date did Voyager 2 launch, and on what date did it fly by Neptune?

### Reference Answer

> Launch: August 20, 1977. Neptune flyby: August 25, 1989.

### Annotated Supporting Sentences

**1. Voyager 2 — launch — sentence [0]**

> Voyager 2 launched on August 20, 1977.

**2. Voyager 2 — Neptune flyby — sentence [0]**

> The Neptune flyby of Voyager 2 took place on August 25, 1989.

### Source Records

**url:**

<https://science.nasa.gov/mission/voyager/voyager-2/>

**accessed_date:**

> 2026-10-15

**publisher:**

> NASA

**source_excerpt:**

> launch
> Aug. 20, 1977
> Aug 25, 1989: Neptune Flyby

**review_status:**

> pending_human_review

### Full Context

#### Document 1 — Voyager 2 — launch

**[0] SUPPORT**

> Voyager 2 launched on August 20, 1977.

#### Document 2 — Voyager 2 — Neptune flyby

**[0] SUPPORT**

> The Neptune flyby of Voyager 2 took place on August 25, 1989.

### Additional Metadata

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "source_split": "custom_debug",
  "source_id": "nasa_voyager2",
  "project_split": "debug",
  "type": "custom_multipart",
  "context_origin": "source-derived paraphrases for debug only"
}
```

[Back to question index](#question-index)


<a id="question-13"></a>

## Question 13

**Dataset:** HotpotQA  
**Sample ID:** `hotpotqa_5a77dadd5542997042120b59`  
**Review status:** `pending_human_review`

### Question

> Hall of Fame Racing was created by Troy Aikman, Bill Saunders, and which Dallas Cowboys quarterback known as "Captain Comback"?

### Reference Answer

> Roger Thomas Staubach (born February 5, 1942)

### Annotated Supporting Sentences

**1. Hall of Fame Racing — sentence [0]**

> Hall of Fame Racing was a NASCAR Sprint Cup Series racing team principally owned by Jeff Moorad, Tom Garfinkel, and Tom Davin.

**2. Hall of Fame Racing — sentence [1]**

>  The team was created as a joint venture between former Dallas Cowboys quarterbacks Roger Staubach, Troy Aikman and  Bill Saunders.

**3. Roger Staubach — sentence [0]**

> Roger Thomas Staubach (born February 5, 1942), nicknamed "Roger the Dodger", "Captain America" and "Captain Comeback", is a former American football quarterback in the National Football League (NFL).

### Full Context

#### Document 1 — Roger Staubach

**[0] SUPPORT**

> Roger Thomas Staubach (born February 5, 1942), nicknamed "Roger the Dodger", "Captain America" and "Captain Comeback", is a former American football quarterback in the National Football League (NFL).

#### Document 2 — 1993 Cleveland Browns season

**[0]**

> The 1993 Cleveland Browns season was the team's 44th season with the National Football League.

**[1]**

>  This season was notable for coach Bill Belichick deciding to bench, and then ultimately release, longtime starting quarterback Bernie Kosar in favor of Vinny Testaverde.

**[2]**

>  Kosar resurfaced during the season with the Dallas Cowboys, when he was part of the eventual Super Bowl champions as a fill-in for injured quarterback Troy Aikman.

**[3]**

>  The Browns get off to a 5-2 start despite the Quarterback Controversy.

**[4]**

>  Prior to the start of the season the Browns signed Free Agent Quarterback Vinny Testaverde.

**[5]**

>  Originally Testaverde was supposed to back-up his former University of Miami teammate Bernie Kosar.

**[6]**

>  However, when Testaverde performed better when given the opportunity to play some felt there should be a change at the Quarterback position.

**[7]**

>  However, the Browns went beyond that by unceremoniously releasing Kosar in the middle of the season.

**[8]**

>  The Browns lost their next four games and seven of their last nine games to finish with a 7-9 record.

#### Document 3 — Troy Aikman

**[0]**

> Troy Kenneth Aikman (born November 21, 1966) is a former American football quarterback who played for the Dallas Cowboys in the National Football League (NFL).

**[1]**

>  The number one overall draft pick in 1989, Aikman played twelve consecutive seasons as quarterback with the Cowboys.

**[2]**

>  During his career he was a six-time Pro Bowl selection, led the team to three Super Bowl victories, and was the Super Bowl XXVII MVP.

**[3]**

>  Aikman was elected to the Pro Football Hall of Fame in 2006 and to the College Football Hall of Fame on December 9, 2008 in New York City.

#### Document 4 — Brett Faryniarz

**[0]**

> Brett Allen Faryniarz (born July 23, 1965) is a former professional American football player who played linebacker for seven seasons in the NFL.

**[1]**

>  In college, he was a defensive standout for the San Diego State Aztecs, starring on the team's much-maligned "Ocean Breeze" defense.

**[2]**

>  The name derived from a comment by former UCLA quarterback Troy Aikman, who compared the team's pass defense to "just playing catch in the open air."

**[3]**

>  Despite the defense's generally poor caliber, Faryniarz developed a reputation as a "solid quarterback sacker" and laid out Aikman twice during the SDSU UCLA game in the Rose Bowl.

**[4]**

>  After starting three years for the Aztecs, Faryniarz played for the then-Los Angeles Rams, where he played linebacker.

**[5]**

>  He finished his career on the inaugural Carolina Panthers team in 1995.

#### Document 5 — Hall of Fame Racing

**[0] SUPPORT**

> Hall of Fame Racing was a NASCAR Sprint Cup Series racing team principally owned by Jeff Moorad, Tom Garfinkel, and Tom Davin.

**[1] SUPPORT**

>  The team was created as a joint venture between former Dallas Cowboys quarterbacks Roger Staubach, Troy Aikman and  Bill Saunders.

**[2]**

>  The team has closed following the 2009 season, with its best season coming with Tony Raines and Ron Fellows (for the road courses) behind the wheel of the No. 96 DLP Chevrolet, finishing 25th in owners points in 2007.

#### Document 6 — 2002 Dallas Cowboys season

**[0]**

> The 2002 Dallas Cowboys season was the 43rd season for the team in the National Football League.

**[1]**

>  It was Emmitt Smith's 13th and final season with the team, officially marking the end of the famed "triplets" tenure in Dallas after wide receiver Michael Irvin was forced to retire prematurely after the 1999 season and quarterback Troy Aikman retired prior to the start of the 2001 season.

**[2]**

>  All three players would eventually be inducted to the Pro Football Hall of Fame.

**[3]**

>  It was also the last of three consecutive 5-11 finishes for the Cowboys, beginning in 2000.

#### Document 7 — Mark Tuinei

**[0]**

> Mark Pulemau Tuinei (March 31, 1960 – May 6, 1999) was an American football offensive tackle in the National Football League for the Dallas Cowboys.

**[1]**

>  Known as a "gentle giant", his career lasted for 15 years (1983–1997) and his ability to protect quarterback Troy Aikman and to run-block for running back Emmitt Smith helped them win Super Bowls in 1992, 1993, and 1995 and the NFC East Division in 1985 and 1992-96.

**[2]**

>  He was also selected for the Pro Bowl in 1994 and 1995.

#### Document 8 — Michael Irvin

**[0]**

> Michael Jerome Irvin (born March 5, 1966) is a retired American football player, actor, and sports commentator.

**[1]**

>  Irvin played college football at the University of Miami, then for the Dallas Cowboys of the National Football League (NFL) for his entire pro athletic career (1988-1999), which ended due to a spinal cord injury.

**[2]**

>  Irvin was nicknamed "The Playmaker" due to his penchant for making big plays in big games during his college and pro careers.

**[3]**

>  He is one of three key Cowboys offensive players who helped the team attain three Super Bowl wins: he is known as one of "The Triplets" along with Troy Aikman and Emmitt Smith.

**[4]**

>  He is also a former broadcaster for ESPN's "Sunday NFL Countdown" and currently an analyst for NFL Network.

**[5]**

>  In 2007, he was selected to the Pro Football Hall of Fame.

#### Document 9 — The 440 Alliance

**[0]**

> The 440 Alliance is an American cello rock band from Arlington, Texas consisting of five cellists and a percussionist.

**[1]**

>  The group formed in 2004 and is known for their diverse approach to the cello, incorporating electric effects, turntables, piano, and mallet percussion.

**[2]**

>  They received national exposure on NPR's "All Songs Considered", the Drew Pearson Show on Fox Sports, and on Fox's musical reality show, "The Next Great American Band".

**[3]**

>  The group has performed at a number of private parties for celebrities including Troy Aikman (Former NFL Quarterback for the Dallas Cowboys), Jerry Jones (Dallas Cowboys owner), John Kirtland (Former drummer for Deep Blue Something and owner of Kirtland Records), Janine Turner (from Northern Exposure), members of the Dallas Symphony Orchestra, as well as the Dallas, TX movie premier for the film 'The Soloist' (starring Jamie Foxx and Robert Downey Jr.).

#### Document 10 — 2000 Dallas Cowboys season

**[0]**

> The 2000 Dallas Cowboys season was the 41st season for the team in the National Football League.

**[1]**

>  Cowboys owner Jerry Jones would promote the team's long-time defensive coordinator, Dave Campo, to be the fifth head coach of the Dallas Cowboys.

**[2]**

>  This was also Troy Aikman's last season with the team.

### Additional Metadata

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "source_split": "dev",
  "source_id": "5a77dadd5542997042120b59",
  "project_split": "debug",
  "type": "bridge",
  "level": "hard"
}
```

[Back to question index](#question-index)


<a id="question-14"></a>

## Question 14

**Dataset:** HotpotQA  
**Sample ID:** `hotpotqa_5a8335d95542993344745ff1`  
**Review status:** `pending_human_review`

### Question

> Who appeared in the Olympics first, Piet Norval or Emilio Sánchez?

### Reference Answer

> Sanchez

### Annotated Supporting Sentences

**1. Piet Norval — sentence [1]**

>  The right-hander represented his native country in the doubles competition at the 1992 Summer Olympics in Barcelona, where he partnered Wayne Ferreira.

**2. Emilio Sánchez — sentence [1]**

>  He won three Grand Slam doubles titles and the men's doubles silver medal at the 1988 Olympic Games.

**3. Emilio Sánchez — sentence [3]**

>  Sanchez since retiring captained his nation to Davis Cup success in 2008.

**4. Emilio Sánchez — sentence [4]**

>  In 2012 Sanchez was a tournament director for two wheelchair tennis events.

### Full Context

#### Document 1 — 2000 Estoril Open – Men's Doubles

**[0]**

> Tomás Carbonell and Donald Johnson were the defending champions, but did not participate together this year.

**[1]**

>  Carbonell partnered Juan Balcells, losing in the first round.

**[2]**

>  Johnson partnered Piet Norval and successfully defended his title.

#### Document 2 — Piet Norval

**[0]**

> Pieter ("Piet") Norval (born 7 April 1970) is a former tennis player from South Africa, who turned professional in 1988.

**[1] SUPPORT**

>  The right-hander represented his native country in the doubles competition at the 1992 Summer Olympics in Barcelona, where he partnered Wayne Ferreira.

**[2]**

>  The pair won the silver medal, after losing the final to Boris Becker and Michael Stich from Germany.

**[3]**

>  Norval reached his highest singles ATP-ranking on 19 June 1989, when he became the no. 125 of the world.

#### Document 3 — 2000 Grand Prix de Tennis de Lyon – Doubles

**[0]**

> Piet Norval and Kevin Ullyett were the defending champions, but did not participate this year.

#### Document 4 — 1994 Grand Prix Hassan II – Doubles

**[0]**

> Mike Bauer and Piet Norval were the defending champions, but did not participate this year.

#### Document 5 — 1991 Donnay Indoor Championships – Doubles

**[0]**

> Emilio Sánchez and Slobodan Živojinović were the defending champions, but Sánchez did not participate this year.

**[1]**

>  Živojinović partnered Boris Becker, withdrawing prior to their semifinals match.

#### Document 6 — Emilio Sánchez

**[0]**

> Emilio Ángel Sánchez Vicario (born 29 May 1965) is a former professional tennis player from Spain.

**[1] SUPPORT**

>  He won three Grand Slam doubles titles and the men's doubles silver medal at the 1988 Olympic Games.

**[2]**

>  He is the brother of multiple Grand Slam winner Arantxa.

**[3] SUPPORT**

>  Sanchez since retiring captained his nation to Davis Cup success in 2008.

**[4] SUPPORT**

>  In 2012 Sanchez was a tournament director for two wheelchair tennis events.

#### Document 7 — 2000 Majorca Open – Doubles

**[0]**

> Lucas Arnold and Tomás Carbonell were the defending champions, but did not participate together this year.

**[1]**

>  Arnold partnered Martín García, losing in the first round.

**[2]**

>  Carbonell partnered Piet Norval, losing in the first round.

#### Document 8 — 1994 Australian Open – Mixed Doubles

**[0]**

> Arantxa Sánchez Vicario and Todd Woodbridge were the defending champions but they competed with different partners that year, Sánchez Vicario with Emilio Sánchez and Woodbridge with Helena Suková.

#### Document 9 — Bent-Ove Pedersen

**[0]**

> Bent-Ove Pedersen (born 11 July 1967 in Oslo) is a former tennis player from Norway, who turned professional in 1992.

**[1]**

>  He spent several years playing tennis at Berkeley in California.

**[2]**

>  The right-hander represented his native country in the doubles competition at the 1992 Summer Olympics in Barcelona, where he partnered Christian Ruud.

**[3]**

>  The pair was defeated in the first round by South Africa's eventual runners-up Wayne Ferreira and Piet Norval.

**[4]**

>  Pedersen reached his highest singles ATP-ranking on 13 September 1993, when he became the number 366 of the world.

**[5]**

>  He was in quarterfinal in US Open doubles, 1991, partnering Matt Lucena from the US.

**[6]**

>  He became the number 78 on the doubles ranking 30.

**[7]**

>  August 1993.

#### Document 10 — 1997 ABN AMRO World Tennis Tournament – Doubles

**[0]**

> David Adams and Marius Barnard were the defending champions but they competed with different partners that year, Adams with Olivier Delaître and Barnard with Piet Norval.

### Additional Metadata

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "source_split": "dev",
  "source_id": "5a8335d95542993344745ff1",
  "project_split": "debug",
  "type": "comparison",
  "level": "hard"
}
```

[Back to question index](#question-index)


<a id="question-15"></a>

## Question 15

**Dataset:** HotpotQA  
**Sample ID:** `hotpotqa_5a852cd05542997b5ce3ffb0`  
**Review status:** `pending_human_review`

### Question

> The birthplace of George McCall Theal is a port city of what bay?

### Reference Answer

> Bay of Fundy

### Annotated Supporting Sentences

**1. George McCall Theal — sentence [0]**

> George McCall Theal (11 April 1837, Saint John, New Brunswick – 17 April 1919, Wynberg, Cape Town), was the most prolific and influential South African historian, archivist and genealogist of the late nineteenth and early twentieth century.

**2. Saint John, New Brunswick — sentence [0]**

> Saint John (] ) is the port city of the Bay of Fundy in the Canadian province of New Brunswick.

### Full Context

#### Document 1 — Poti

**[0]**

> Poti (Georgian: ფოთი ] ; Mingrelian: ფუთი; Laz: ჶაში/Faşi or ფაში/Paşi) is a port city in Georgia, located on the eastern Black Sea coast in the region of Samegrelo-Zemo Svaneti in the west of the country.

**[1]**

>  Built near the site of the ancient Greek colony of Phasis and deriving its name from the same, the city has become a major port city and industrial center since the early 20th century.

**[2]**

>  It is also home to a main naval base and the headquarters of the Georgian navy.

**[3]**

>  Adjacent to the Poti port area is the RAKIA owned Free Industrial Zone.

**[4]**

>  Inaugurated in April 2008, it has registered a number of businesses, including those from Iranian businesspeople trying to evade sanctions against Iran.

#### Document 2 — George McCall Courts

**[0]**

> George McCall Courts (February 16, 1888 – August 1, 1932) was born in the District of Columbia.

**[1]**

>  He graduated from the United States Naval Academy in 1907.

**[2]**

>  He received the Medal of Honor for actions at the United States occupation of Veracruz, 1914.

#### Document 3 — Oakland, California

**[0]**

> Oakland is the largest city and the county seat of Alameda County, California, United States.

**[1]**

>  A major West Coast port city, Oakland is the largest city in the East Bay region of the San Francisco Bay Area, the third largest city overall in the San Francisco Bay Area, the eighth largest city in California, and the 45th largest city in the United States, with a population of 419,267 as of 2015 .

**[2]**

>  It serves as a trade center for the San Francisco Bay Area; its Port of Oakland is the busiest port in the San Francisco Bay, the entirety of Northern California, and the fifth busiest in the United States of America.

**[3]**

>  The city was incorporated in 1852.

#### Document 4 — August Frederik Beutler

**[0]**

> August Frederik Beutler (c. 1728 in Dinkelsbühl – ?

**[1]**

>  in Cape Town) was an ensign (sergeant 1747–49, ensign 1749–54) in the employ of the Dutch East India Company who headed an epic 1752 reconnaissance expedition lasting 8 months from 29 February to November, eastward from Cape Town as far as the present-day site of Butterworth.

**[2]**

>  Beutler wrote a comprehensive account of his pioneering expedition which was first published in 1896 by the historian George McCall Theal and in 1922 by the Dutch historian Everhardus Cornelis Godée Molsbergen (1875–1940).

**[3]**

>  The mandate of the expedition was to report on the tribes living along the route, the possibility of trade and on anything else that might be profitable to the Dutch East India Company.

#### Document 5 — 1968 Men's National Tennis League

**[0]**

> The 1968 Men's National Tennis League (NTL) was the inaugural series of professional tennis tournaments founded by George McCall, among others: Rod Laver, Roy Emerson, Ken Rosewall, Andrés Gimeno, Pancho Gonzales and Fred Stolle.

#### Document 6 — Port Sudan

**[0]**

> Port Sudan (Arabic: بور سودان‎ ‎ "Būr Sūdān ") is a port city in eastern Sudan, and the capital of the state of Red Sea.

**[1]**

>  s of 2007 , it has 489,725 residents.

**[2]**

>  Located on the Red Sea, it is the Republic of Sudan's main port city.

#### Document 7 — Saint John, New Brunswick

**[0] SUPPORT**

> Saint John (] ) is the port city of the Bay of Fundy in the Canadian province of New Brunswick.

**[1]**

>  The port is Canada’s third largest port by tonnage with a cargo base that includes dry and liquid bulk, break bulk, containers, and cruise.

**[2]**

>  In 2016, after a decades long decline, the city fell from being the most populous city in New Brunswick to the second most populous city in the province for the first time, with a population of 67,575 over an area of 315.82 sqkm .

**[3]**

>  The Saint John metropolitan area covers a land area of 3,362.95 sqkm across the Caledonia Highlands, with a population (as of 2016) of 126,202.

**[4]**

>  After the partitioning of the colony of Nova Scotia in 1784, the new colony of New Brunswick was thought to be named 'New Ireland' with the capital to be in Saint John before being vetoed by Britain's King George III.

**[5]**

>  Saint John is the oldest incorporated city in Canada.

**[6]**

>  During the reign of George III, the municipality was created by royal charter in 1785.

#### Document 8 — Port of Chittagong

**[0]**

> The Port of Chittagong (Bengali: চট্টগ্রাম বন্দর ) is the busiest seaport on the coastline of the Bay of Bengal, and the second busiest in the overall region of countries dependent on the Bay of Bengal.

**[1]**

>  According to Lloyd's, it ranked as the 76th busiest port in the world in 2016.

**[2]**

>  Located in the Bangladeshi port city of Chittagong and on the banks of the Karnaphuli River, the port of Chittagong handles 90% of Bangladesh's export-import trade, and has been used by India, Nepal and Bhutan for transshipment.

#### Document 9 — George McCall Theal

**[0] SUPPORT**

> George McCall Theal (11 April 1837, Saint John, New Brunswick – 17 April 1919, Wynberg, Cape Town), was the most prolific and influential South African historian, archivist and genealogist of the late nineteenth and early twentieth century.

#### Document 10 — George A. McCall School

**[0]**

> General George A. McCall School is a public K–8 school in the Society Hill section of Center City, Philadelphia.

**[1]**

>  The McCall School, located at 325 S. 7th Street, serves Society Hill, Chinatown, and Old City.

**[2]**

>  The school, a part of the School District of Philadelphia, is named after George A. McCall.

### Additional Metadata

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "source_split": "dev",
  "source_id": "5a852cd05542997b5ce3ffb0",
  "project_split": "debug",
  "type": "bridge",
  "level": "hard"
}
```

[Back to question index](#question-index)


<a id="question-16"></a>

## Question 16

**Dataset:** HotpotQA  
**Sample ID:** `hotpotqa_5adf72d35542992d7e9f9369`  
**Review status:** `pending_human_review`

### Question

> Are William Kronick and Jon Turteltaub both television writers ?

### Reference Answer

> no

### Annotated Supporting Sentences

**1. William Kronick — sentence [0]**

> William Kronick is an American film and television writer, director and producer.

**2. Jon Turteltaub — sentence [0]**

> Jonathan Charles Turteltaub (born August 8, 1963) is an American film director and producer.

### Full Context

#### Document 1 — William Kronick

**[0] SUPPORT**

> William Kronick is an American film and television writer, director and producer.

**[1]**

>  He worked in the film industry from 1960 to 2000, when he segued into writing novels.

#### Document 2 — Jon Turteltaub

**[0] SUPPORT**

> Jonathan Charles Turteltaub (born August 8, 1963) is an American film director and producer.

#### Document 3 — National Treasure (film)

**[0]**

> National Treasure is a 2004 American adventure heist film produced and released by Walt Disney Pictures.

**[1]**

>  It was written by Jim Kouf and the Wibberleys, produced by Jerry Bruckheimer and directed by Jon Turteltaub.

**[2]**

>  It is the first film in the "National Treasure" franchise and stars Nicolas Cage, Harvey Keitel, Jon Voight, Diane Kruger, Sean Bean, Justin Bartha and Christopher Plummer.

#### Document 4 — Jericho (2006 TV series)

**[0]**

> Jericho is an American post-apocalyptic action-drama television series, which centers on the residents of the fictional city of Jericho, Kansas, in the aftermath of a limited nuclear attack on 23 major cities in the contiguous United States.

**[1]**

>  The show was produced by CBS Paramount Network Television and Junction Entertainment, with executive producers Jon Turteltaub, Stephen Chbosky, and Carol Barbee.

**[2]**

>  It was shown in more than 30 countries.

#### Document 5 — Last Vegas

**[0]**

> Last Vegas is a 2013 American comedy film directed by Jon Turteltaub, written by Dan Fogelman and starring Michael Douglas, Robert De Niro, Morgan Freeman, Kevin Kline and Mary Steenburgen.

**[1]**

>  The plot surrounds three retirees who travel to Las Vegas to have a bachelor party for their last remaining single friend.

#### Document 6 — List of Jericho episodes

**[0]**

> "Jericho" is an American television drama series produced by Carol Barbee, Jon Turteltaub, Dan Shotz, Jonathan Steinberg, Josh Schaer, and Stephen Chbosky.

**[1]**

>  The series is set in the fictional town of Jericho, Kansas in the aftermath of the simultaneous nuclear attacks on 23 American cities.

**[2]**

>  Significant story arcs in the first season are the immediate aftermath of detonation of the bombs, the resulting isolation of the town, and confrontations between family, friends, bandits, and neighboring towns.

**[3]**

>  The second season focuses on the arrival of a new federal government, the imposition of a police state, and Jake Green's (Skeet Ulrich) and Robert Hawkins' (Lennie James) attempt to expose the masterminds behind the attack.

#### Document 7 — National Treasure: Book of Secrets

**[0]**

> National Treasure: Book of Secrets (released on home video as National Treasure 2: Book of Secrets) is a 2007 mystery adventure film directed by Jon Turteltaub and produced by Jerry Bruckheimer.

**[1]**

>  It is a sequel to the 2004 film "National Treasure" and is the second part of the "National Treasure" franchise.

**[2]**

>  The film stars Nicolas Cage, Diane Kruger, Justin Bartha, Jon Voight, Harvey Keitel, Ed Harris, Bruce Greenwood, and Helen Mirren.

#### Document 8 — Jon Stone

**[0]**

> Jon Stone (April 13, 1932 – March 30, 1997) was an American award-winning writer, director and producer, who was best known for being an original crew member on "Sesame Street" and is credited with helping develop characters such as Cookie Monster, Oscar the Grouch and Big Bird.

**[1]**

>  Stone won 18 television Emmy Awards Many regard him as one of the best children's television writers.

#### Document 9 — Trabbi Goes to Hollywood

**[0]**

> Trabbi Goes to Hollywood (English title: Driving Me Crazy) is a 1991 US comedy film directed by Jon Turteltaub, starring Thomas Gottschalk, Billy Dee Williams, Dom DeLuise, and James Tolkan.

#### Document 10 — Television Writers Vault

**[0]**

> The Television Writers Vault is an online marketplace within the television industry used for scouting and selling original TV formats, concepts, and intellectual properties to produce as new television shows.

**[1]**

>  It is the first website to deliver new show ideas from people outside of the industry, resulting in successful productions by major networks.

**[2]**

>  2012 saw the global broadcast of two reality television concepts discovered from the site; "Saw Dogs" (aired on Discovery Channel, TV4 Sweden, and OLN) and "Deals From The Darkside" (aired on SyFy, A&E Australia, OLN, UKTV).

**[3]**

>  2014 saw the premiere of "Kim of Queens" on Lifetime TV, whose star, Kim Gravel, was discovered pitching her own concepts at the TV Writers Vault.

### Additional Metadata

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "source_split": "dev",
  "source_id": "5adf72d35542992d7e9f9369",
  "project_split": "debug",
  "type": "comparison",
  "level": "hard"
}
```

[Back to question index](#question-index)


<a id="question-17"></a>

## Question 17

**Dataset:** HotpotQA  
**Sample ID:** `hotpotqa_5ae0159855429925eb1afc09`  
**Review status:** `pending_human_review`

### Question

> In between Anaïs Nin and Odysseas Elytis who was awarded the Nobel Prize in Literature?

### Reference Answer

> Odysseas Elytis

### Annotated Supporting Sentences

**1. Anaïs Nin — sentence [0]**

> Anaïs Nin (] ; born Angela Anaïs Juana Antolina Rosa Edelmira Nin y Culmell; February 21, 1903 – January 14, 1977) was an essayist and memoirist born to Cuban parents in France, where she was also raised.

**2. Odysseas Elytis — sentence [0]**

> Odysseas Elytis (Greek: Οδυσσέας Ελύτης , ] , pen name of Odysseas Alepoudellis, Greek: Οδυσσέας Αλεπουδέλλης ; 2 November 1911 – 18 March 1996) was regarded as a major exponent of romantic modernism in Greece and the world.

**3. Odysseas Elytis — sentence [1]**

>  In 1979 he was awarded the Nobel Prize in Literature.

### Full Context

#### Document 1 — Collages (novel)

**[0]**

> Collages, published in 1964, was Anaïs Nin's last published novel (excluding her erotica).

**[1]**

>  It is very different from the previous novels of the "Cities of the Interior" series, because it contains none of the familiar characters in those novels.

**[2]**

>  It is also different in that it takes place on two continents, has about two dozen important characters, and for the first time in Anaïs Nin's work the female lead is not seeking psychological wholeness.

**[3]**

>  Most of Anaïs Nin's other novels only have a few main characters, there is rarely much geographical movement in the other novels, and usually the lead character is a woman seeking psychological wholeness.

#### Document 2 — Nearer the Moon

**[0]**

> Nearer the Moon: From a Journal of Love (full title "Nearer the Moon: From a Journal of Love, the Unexpurgated Diary of Anaïs Nin (1937–1939)") is a 1996 book based upon material excerpted from the unpublished diaries of Anaïs Nin.

**[1]**

>  It corresponds temporally to part of Nin's published diaries.

**[2]**

>  It consists mainly of material that was left out of the published version because it would have hurt people involved or their relationships with Anaïs Nin had it been published at the time.

#### Document 3 — Anaïs Nin: A Biography

**[0]**

> Anaïs Nin: A Biography is Deirdre Bair's award-winning biography of writer Anaïs Nin.

**[1]**

>  It is considered arguably by many to be the most comprehensive, well-researched, and scholarly biography available of Nin.

**[2]**

>  Though the biography has received praise, it has also angered some fans of Anaïs Nin as well as some of her former associates, some of whom claim that Bair's critical and rigorous investigation of Anaïs Nin's life is unsympathetic.

#### Document 4 — Incest: From a Journal of Love

**[0]**

> Incest: From a Journal of Love: The Unexpurgated Diary of Anaïs Nin (1932–1934) is a 1992 non-fiction book by Anaïs Nin.

**[1]**

>  It is a continuation of the diary entries first published in "Henry and June: From the Unexpurgated Diary of Anaïs Nin".

**[2]**

>  It features Nin's relationships with writer Henry Miller, his wife June Miller, the psychoanalyst Otto Rank, her father Joaquín Nin, and her husband Hugh Parker Guiler.

**[3]**

>  She also copied some of her correspondence with these people into her diary.

**[4]**

>  Much of this book was written in English, although those of her letters which were originally written in French and Spanish were translated.

**[5]**

>  Most of this diary takes place in France, particularly Clichy, Paris and Louveciennes.

#### Document 5 — Odysseas Elytis

**[0] SUPPORT**

> Odysseas Elytis (Greek: Οδυσσέας Ελύτης , ] , pen name of Odysseas Alepoudellis, Greek: Οδυσσέας Αλεπουδέλλης ; 2 November 1911 – 18 March 1996) was regarded as a major exponent of romantic modernism in Greece and the world.

**[1] SUPPORT**

>  In 1979 he was awarded the Nobel Prize in Literature.

#### Document 6 — Anaïs Nin

**[0] SUPPORT**

> Anaïs Nin (] ; born Angela Anaïs Juana Antolina Rosa Edelmira Nin y Culmell; February 21, 1903 – January 14, 1977) was an essayist and memoirist born to Cuban parents in France, where she was also raised.

**[1]**

>  She spent some time in Spain and Cuba, but lived most of her life in the United States, where she became an established author.

**[2]**

>  She wrote journals (which span more than 60 years, beginning when she was 11 years old and ending shortly before her death), novels, critical studies, essays, short stories, and erotica.

**[3]**

>  A great deal of her work, including "Delta of Venus" and "Little Birds", was published posthumously.

#### Document 7 — Seduction of the Minotaur

**[0]**

> Seduction of the Minotaur is an autobiographical novel by the mixed nationality writer Anaïs Nin, the last part of her "Cities of the Interior" sequence.

**[1]**

>  It is about a woman named Lillian, and her self-psychoanalysis.

**[2]**

>  The setting is taken from Anaïs' diary account of her first trip to Acapulco in 1947, and the novel repeats much of the first part of "The Diary of Anaïs Nin" volume V.

**[3]**

>  Since the author was concerned with psychology rather than physical adventure, there is actually less violence in the novel than in the diary account.

**[4]**

>  The exception is that the doctor allows himself to be shot because he is loved only as a doctor and never as a man, perhaps patterned after her understanding of Otto Rank's death.

#### Document 8 — The Diary of Anaïs Nin

**[0]**

> The Diary of Anaïs Nin is the published version of Anaïs Nin's own private manuscript diary, which she began at age 11 in 1914 during a trip from Europe to New York with her mother and two brothers.

**[1]**

>  Anaïs Nin would later say she had begun the diary as a letter to her father, Cuban composer Joaquín Nin, who had abandoned the family a few years earlier.

#### Document 9 — Henry and June

**[0]**

> Henry and June: From the Unexpurgated Diary of Anaïs Nin (full title "Henry and June: From A Journal of Love: the Unexpurgated Diary of Anaïs Nin (1931–1932)") is a 1986 book that is based upon material excerpted from the unpublished diaries of Anaïs Nin.

#### Document 10 — Fire: From a Journal of Love

**[0]**

> Fire: From the Unexpurgated Diary of Anaïs Nin (full title "Fire: From A Journal of Love: the Unexpurgated Diary of Anaïs Nin (1934–1937)") is a 1995 book that is based on material excerpted from the unpublished diaries of Anais Nin.

**[1]**

>  It corresponds temporally to part of Anaïs Nin's published diaries, but consists mostly of material about her love life that was too sensitive or secret to publish in her lifetime or in that of others involved.

### Additional Metadata

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "source_split": "dev",
  "source_id": "5ae0159855429925eb1afc09",
  "project_split": "debug",
  "type": "comparison",
  "level": "hard"
}
```

[Back to question index](#question-index)


<a id="question-18"></a>

## Question 18

**Dataset:** HotpotQA  
**Sample ID:** `hotpotqa_5ae250b45542996483e64977`  
**Review status:** `pending_human_review`

### Question

> What job did Newt Gingrich have prior to producing Nine Days that Changed the World?

### Reference Answer

> former Speaker of the U.S. House of Representatives

### Annotated Supporting Sentences

**1. Nine Days that Changed the World — sentence [0]**

> Nine Days that Changed the World is a 2010 documentary film produced by Newt Gingrich and his wife Callista that centers on the role played by Pope John Paul II in the fall of Communism in Europe and the rise of labour union Solidarity.

**2. Callista Gingrich — sentence [1]**

>  She is married to former Speaker of the U.S. House of Representatives and 2012 Republican presidential candidate Newt Gingrich.

### Full Context

#### Document 1 — Texas Patriots PAC

**[0]**

> Texas Patriots PAC is a Super PAC based in The Woodlands in southeastern Texas.

**[1]**

>  The group gained national attention when it hosted a Republican presidential debate in November 2011 between candidates Herman Cain and Newt Gingrich.

**[2]**

>  The debate was conducted in the "Lincoln-Douglas" style, which Gingrich then went on to make a central theme of his campaign, promising to challenge President Obama to seven "Lincoln-Douglas" style debates, at three hours each, should he win the GOP nomination.

#### Document 2 — Joseph Gaylord

**[0]**

> Joseph Gaylord is a political consultant formerly closely linked to former U.S. Representative and Speaker of the House Newt Gingrich.

**[1]**

>  He was executive director of the National Republican Congressional Committee in the mid-1980s and worked for GOPAC, a political action committee which was "Gingrich's main vehicle for the long campaign that in 1994 resulted in the Republican takeover of the House after years of Democratic domination."

**[2]**

>  Gaylord was one of the people behind the Contract With America that won the Republican Party control of the United States Congress in the 1994 midterm elections.

#### Document 3 — Nine Days that Changed the World

**[0] SUPPORT**

> Nine Days that Changed the World is a 2010 documentary film produced by Newt Gingrich and his wife Callista that centers on the role played by Pope John Paul II in the fall of Communism in Europe and the rise of labour union Solidarity.

#### Document 4 — Callista Gingrich

**[0]**

> Callista Louise Gingrich (née Bisek; born March 4, 1966) is an American political aide, businesswoman, and author.

**[1] SUPPORT**

>  She is married to former Speaker of the U.S. House of Representatives and 2012 Republican presidential candidate Newt Gingrich.

**[2]**

>  In May 2017, President Donald Trump nominated her to be the United States Ambassador to the Holy See, a post requiring United States Senate confirmation.

#### Document 5 — Congressional Review Act

**[0]**

> The Congressional Review Act (CRA) is a law that was enacted by the United States Congress under House Speaker Newt Gingrich as Section 251 of the Contract with America Advancement Act of 1996 (Pub.L.

**[1]**

>  104–121 ) and signed into law by President Bill Clinton on March 29, 1996.

**[2]**

>  The law empowers Congress to review, by means of an expedited legislative process, new federal regulations issued by government agencies and, by passage of a joint resolution, to overrule a regulation.

**[3]**

>  Once a rule is thus repealed, the CRA also prohibits the reissuing of the rule in substantially the same form or the issuing of a new rule that is substantially the same "unless the reissued or new rule is specifically authorized by a law enacted after the date of the joint resolution disapproving the original rule" (5 U.S. Code § 801(b)(2)).

**[4]**

>  Congress has a window of time lasting 60 "legislative" days (i.e., days that Congress is actually in session, rather than simple calendar days) to disapprove of any given rule by simple majority vote; otherwise, the rule will go into effect at the end of this period.

#### Document 6 — R.C. Hammond

**[0]**

> R.C. Hammond (born 1979) is an American political strategist and communications director.

**[1]**

>  He is currently a communications adviser for Secretary of State Rex Tillerson.

**[2]**

>  Hammond served as the press secretary to Newt Gingrich's 2012 presidential campaign.

**[3]**

>  He previously served Gingrich at his American Solutions for Winning the Future PAC.

**[4]**

>  Hammond has worked as press secretary or communications director for Senator Gordon H. Smith, Senator John E. Sununu and Representative Shelly Moore Capito.

**[5]**

>  He founded R. C. Hammond Public Affairs in 2012.

#### Document 7 — Political positions of Newt Gingrich

**[0]**

> Newt Gingrich has declared his position on many political issues through his public comments and legislative record, including as Speaker of the House.

**[1]**

>  The political initiative with which he is most widely identified was the Contract With America, which outlined an economic and social agenda designed to improve the efficiency of government while reducing its burden on the American taxpayer.

**[2]**

>  Passage of the Contract helped establish Gingrich's reputation as a public intellectual.

**[3]**

>  His engagement of public issues has continued through to the present, in particular as the founder of American Solutions for Winning the Future.

#### Document 8 — Rediscovering God in America

**[0]**

> Rediscovering God in America is a book written by former House Speaker Newt Gingrich with photography from his wife Callista Gingrich.

**[1]**

>  and a film series based upon the book and narrated by the two Gingriches.

**[2]**

>  The book was a "New York Times" bestseller.

#### Document 9 — Winning the Future

**[0]**

> Winning the Future: A 21st Century Contract with America is a book by former U.S. Speaker of the House Newt Gingrich that outlines Gingrich's plans for the United States of America.

**[1]**

>  Published in 2005 by Regnery Publishing, its themes include: Social Security reform, immigration reform, education reform, increasing the usage of health savings accounts, allowing the disabled the option of working, and American interests within the world trading system.

#### Document 10 — Candace Gingrich

**[0]**

> Candace Gingrich ( ; born June 2, 1966) is an American LGBT rights activist at the Human Rights Campaign.

**[1]**

>  They are the half-sibling of former Speaker of the House Newt Gingrich, who is more than 20 years their senior.

### Additional Metadata

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "source_split": "dev",
  "source_id": "5ae250b45542996483e64977",
  "project_split": "debug",
  "type": "bridge",
  "level": "hard"
}
```

[Back to question index](#question-index)


<a id="question-19"></a>

## Question 19

**Dataset:** HotpotQA  
**Sample ID:** `hotpotqa_5ae3f4fe5542995ad6573ce8`  
**Review status:** `pending_human_review`

### Question

> Are the genera Gordonia and Osbeckia in the same family?

### Reference Answer

> no

### Annotated Supporting Sentences

**1. Gordonia (plant) — sentence [0]**

> Gordonia is a genus of flowering plants in the family Theaceae, related to "Franklinia", "Camellia" and "Stewartia".

**2. Osbeckia — sentence [0]**

> Osbeckia is a genus of plants in the family Melastomataceae.

### Full Context

#### Document 1 — Gordonia (plant)

**[0] SUPPORT**

> Gordonia is a genus of flowering plants in the family Theaceae, related to "Franklinia", "Camellia" and "Stewartia".

**[1]**

>  Of the roughly 40 species, all but two are native to southeast Asia in southern China, Taiwan and Indochina.

**[2]**

>  The remaining species, "G. lasianthus" (Loblolly-bay), is native to southeast North America, from Virginia south to Florida and west to Louisiana; "G. fruticosa" is native to the tropical rainforests of Central and South America, from Costa Rica to Brazil.

#### Document 2 — Osbeckia stellata

**[0]**

> Osbeckia stellata (Thai: จุกนารี ) is a flowering plant in the family Melastomataceae.

#### Document 3 — Gordonia singaporeana

**[0]**

> Gordonia singaporeana is a species of plant in the Theaceae family.

**[1]**

>  It is a tree found in Peninsular Malaysia and Singapore.

**[2]**

>  It is threatened by habitat loss.

#### Document 4 — Gondysia similis

**[0]**

> The Gordonia Darkwing ("Gondysia similis", formerly "Dysgonia similis") is a moth of the Noctuidae family.

**[1]**

>  It is found in North America, from North Carolina to Mississippi and Florida.

**[2]**

>  The food plant occurs in Alabama and Mississippi and the moth could be expected from these areas as well.

#### Document 5 — Gordonia taipingensis

**[0]**

> Gordonia taipingensis is a species of plant in the Theaceae family.

**[1]**

>  It is a tree endemic to Peninsular Malaysia.

**[2]**

>  It is threatened by habitat loss.

#### Document 6 — Osbeckia

**[0] SUPPORT**

> Osbeckia is a genus of plants in the family Melastomataceae.

**[1]**

>  It was named by Carl Linnaeus for the Swedish explorer and naturalist Pehr Osbeck (1723–1805).

#### Document 7 — Osbeckia octandra

**[0]**

> Eight Stamen Osbeckia, (Osbeckia octandra), is a plant species in the genus "Osbeckia" of the family Melastomataceae.

**[1]**

>  It is considered to be endemic to Sri Lanka, where it is known as "Heen Bovitiya - හීන් බෝවිටියා" in Sinhala language.

**[2]**

>  But some texts indicate that it is also found in Tamil Nadu of India.

**[3]**

>  Fruits are dry capsules with numerous seeds.

**[4]**

>  Leaves and young stems are edible, whereas leaves, stem and bark also widely used as a valuable medicine in Ayurveda for treating Diabetes mellitus, Hepatitis, Jaundice, and Hyperlipidaemia.

**[5]**

>  The juice extracted from "Osbeckia octandra" leaves is an effective treatment for liver damage caused by Paracetamol poisoning

#### Document 8 — Gordonia villosa

**[0]**

> Gordonia villosa is a species of plant in the Theaceae family.

**[1]**

>  It is endemic to Jamaica.

#### Document 9 — Gordonia lasianthus

**[0]**

> Gordonia lasianthus (loblolly-bay, holly-bay, gordonia, or bay) is a small to medium-sized evergreen tree or shrub found in acid, swampy soils of pinelands and bays on the Atlantic and Gulf Coastal Plains of the southeastern United States.

**[1]**

>  It is a member of the Tea or Theaceae family.

**[2]**

>  It is slow growing with soft, light-colored(Varies in color from Cream to Carmine), fine-grained wood of little commercial value, although loblolly-bay could be managed as a source of pulpwood.

**[3]**

>  When older specimens are cut, the wood exudes a strong scent.

**[4]**

>  It is similar to a mixture of fresh oranges and pine sap.

**[5]**

>  The bark of the adult tree varies from medium grey to a red brown coloration.

**[6]**

>  Dead adult specimens of loblolly bay exhibit a lustorous shine when exposed to sunlight for several years.

**[7]**

>  The white showy flowers and shiny foliage make it a desirable ornamental, but it is not easy to cultivate.

**[8]**

>  Deer browse stump sprouts heavily.

#### Document 10 — Osbeckia aspera

**[0]**

> Rough Osbeckia, (Osbeckia aspera), also known as Rough small-leaved spider flower, is a plant species in the genus "Osbeckia" of the family Melastomataceae.

**[1]**

>  It is native to India and Sri Lanka.

**[2]**

>  Leaves are elliptic-lanceolate, base attenuate with more or less velvet-hairy on both sides.

**[3]**

>  Flowers are pink in color, show terminal cymes inflorescence.

**[4]**

>  Fruits are single seeded capsule.

### Additional Metadata

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "source_split": "dev",
  "source_id": "5ae3f4fe5542995ad6573ce8",
  "project_split": "debug",
  "type": "comparison",
  "level": "hard"
}
```

[Back to question index](#question-index)


<a id="question-20"></a>

## Question 20

**Dataset:** HotpotQA  
**Sample ID:** `hotpotqa_5ae641f65542992ae0d162a3`  
**Review status:** `pending_human_review`

### Question

> What is the mononym of the Fillipino singer that released the album "My Inspiration"?

### Reference Answer

> Charice

### Annotated Supporting Sentences

**1. My Inspiration — sentence [0]**

> My Inspiration is a full-length studio album, released in the Philippines only, by Filipino singer Jake Zyrus.

**2. Jake Zyrus — sentence [0]**

> Jake Zyrus (born Charmaine Clarice Relucio Pempengco; May 10, 1992), who performed under the mononym Charice until his gender transition to male, is a Filipino singer who rose to popularity through YouTube.

### Full Context

#### Document 1 — Danilla Riyadi

**[0]**

> Danilla Riyadi (known professionally by the mononym Danilla) is an Indonesian singer.

**[1]**

>  She has released just one studio album so far: Telisik (2014), and has appeared in several compilation albums, notably for the Tiga Dara remake soundtrack where she sung ""Bimbang Tanpa Pegangan"" and ""Pilih Menantu"" with Indra Aziz.

**[2]**

>  Her debut album was placed on number #18 of Rolling Stone Indonesia album of the year.

#### Document 2 — Humood AlKhudher

**[0]**

> Humood Othman AlKhudher (in Arabic حمود عثمان الخضر; born 1989), sometimes known only by his mononym Humood is a Kuwaiti singer.

**[1]**

>  He had a successful solo career, first as a child singer, and then as an independent artist.

**[2]**

>  He released his debut album "Fekra" in 2013.

**[3]**

>  In 2015 he was signed to Awakening Records and launched his album "Aseer Ahsan" with the label.

**[4]**

>  The album includes 10 uplifting songs produced by Awakening Records.

#### Document 3 — My Inspiration

**[0] SUPPORT**

> My Inspiration is a full-length studio album, released in the Philippines only, by Filipino singer Jake Zyrus.

**[1]**

>  It was released on May 1, 2009 and is credited under the name Charice, which Zyrus used prior to his gender transition.

**[2]**

>  It is a concept cover album dedicated to his mother Racquel Pempengco.

**[3]**

>  However, despite its ten cover versions (one of which is a remix), this second album by Zyrus features one original song (in both a single and extended version), called "Always You", written by the Metropop Song Festival and Awit Award-winning songwriter Jonathan Manalo.

**[4]**

>  The album has been certified platinum.

**[5]**

>  Like his previous release, the album was also made available for digital download through Amazon.com MP3 Download on June 23, 2009.

**[6]**

>  Some package versions include a second CD, which features a karaoke version of every song, very popular in Asian countries.

#### Document 4 — Holy Smoke (Gin Wigmore album)

**[0]**

> Holy Smoke is the debut album from New Zealand pop singer Gin Wigmore, released under the mononym Gin.

**[1]**

>  Singles released off the album included "Oh My", "I Do" and "Hey Ho".

**[2]**

>  The Cardinals play on every track and backed Wigmore on her subsequent tour.

#### Document 5 — Jake Zyrus

**[0] SUPPORT**

> Jake Zyrus (born Charmaine Clarice Relucio Pempengco; May 10, 1992), who performed under the mononym Charice until his gender transition to male, is a Filipino singer who rose to popularity through YouTube.

#### Document 6 — Banks (singer)

**[0]**

> Jillian Rose Banks (born June 16, 1988), known professionally by the mononym Banks (often stylized as BANKS), is an American singer and songwriter from Orange County, California.

**[1]**

>  She is signed to Harvest Records and Good Years Recordings.

**[2]**

>  Following the release of two extended plays, "Fall Over" and "London", in 2013, Banks released her debut album, "Goddess", on September 5, 2014, to positive reviews from contemporary music critics.

**[3]**

>  It reached number 12 on the US Billboard 100, while its most successful single, "Beggin for Thread", was certified gold by the RIAA.

**[4]**

>  Her second studio album, "The Altar", was released on September 30, 2016, to a similar positive reception.

#### Document 7 — Janna Hurmerinta

**[0]**

> Janna-Mari Hurmerinta (born 20 December 1981), better known by her mononym Janna, is a Finnish R&B, and pop singer, songwriter and pianist.

**[1]**

>  Her debut album "Right Now" was released in June 2007 to critical acclaim.

**[2]**

>  followed by "The Makings of Me" in 2008.

**[3]**

>  In 2013, she was signed to Universal Music Finland.

**[4]**

>  Her self-titled album "Janna" topped the Finnish album chart in June 2014.

#### Document 8 — Myra (singer)

**[0]**

> Mayra Caról Ambriz Quintana (born May 21, 1986 in Los Angeles, California)—better known under the mononym, Myra— is the daughter of Salvador Ambriz and Consuelo Quintana.

**[1]**

>  Myra is an American singer, dancer and choreographer of Mexican descent.

**[2]**

>  She is the first Latina artist to have been signed to Hollywood Records, Walt Disney Records, and Avex Trax.

**[3]**

>  She rose to prominence in 2001 after recording a cover of Martha and the Vandellas' "Dancing in the Street" for the soundtrack to the 2001 film "" (which she would then re-record in 2002 in Spanish for the Disney Channel original movie, Gotta Kick It Up!

**[4]**

> ).

**[5]**

>  However, her first album released before being signed to Disney -released in 1997, was the Mariachi album "Mensajera del Amór", released by Briaz Promotions.

**[6]**

>  At the time of its release, Myra was then known as Mayra Caról.

**[7]**

>  During her Disney-era portion of her career, she contributed her vocals to the song "Miracles Happen (When You Believe)" to the film "The Princess Diaries", and it received a 2002 ALMA Award nomination for Outstanding Song in a Motion Picture Soundtrack.

**[8]**

>  Her debut album "Myra" included these two tracks and were released as singles and both included a music video.

**[9]**

>  The album "Myra" was released in four different formats.

#### Document 9 — Karen (singer)

**[0]**

> Karen Rosenberg (born 20 June 1975), better known by her mononym Karen is a Danish R&B singer.

**[1]**

>  She released three albums.

**[2]**

>  Her debut album "En til en" in 2000 was produced by Saqib of Outlandish and Lasse Lindholm of Hvid Sjokolade.

**[3]**

>  Her follow-up album.

**[4]**

>  The album was nominated to three awards during the Danish Music Awards eventually winning Best R&B.

**[5]**

>  She also became famous with "Vis mig du' min mand" taken from the album.

**[6]**

>  Her follow-up album "Ingen smalle steder" in 2004 was produced by her boyfriend producer Vagn Luv.

**[7]**

>  In 2009, she released "Stiletto", but with much lesser success.

**[8]**

>  the album didn't chart on the Tracklisten.

#### Document 10 — Jeremih

**[0]**

> Jeremy Felton (born July 17, 1987), better known by his mononym Jeremih ( ), is an American singer, songwriter, rapper and record producer.

**[1]**

>  In 2009, he signed a record deal with Def Jam Recordings.

**[2]**

>  Jeremih's commercial debut single, "Birthday Sex", peaked at number four on the US "Billboard" Hot 100 chart.

**[3]**

>  His self-titled debut album reached number six on the US "Billboard" 200 chart.

**[4]**

>  Jeremih's success continued with the release of his second album, "All About You", led by the single "Down on Me", which also reached the top five of the "Billboard" Hot 100.

**[5]**

>  In 2014, his single "Don't Tell 'Em" became his third top-ten hit on the "Billboard" Hot 100.

**[6]**

>  After multiple delays, Jeremih released his third studio album, "Late Nights" in 2015.

**[7]**

>  He announced that he is working on a joint album with PartyNextDoor called "Late Night Party".

**[8]**

>  He is also working on his fourth studio album, "Later That Night".

### Additional Metadata

```json
{
  "schema_version": "1.0",
  "data_version": "debug-v0",
  "source_split": "dev",
  "source_id": "5ae641f65542992ae0d162a3",
  "project_split": "debug",
  "type": "bridge",
  "level": "hard"
}
```

[Back to question index](#question-index)
