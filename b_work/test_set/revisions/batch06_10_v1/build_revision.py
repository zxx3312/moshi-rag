"""Rebuild isolated Q151–Q300 revision; never writes the original batches.
Run from the repository root. Uses only the standard library and local source data.
"""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
import unicodedata
from collections import Counter

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
VERSION = 'eval-revised-v1'
sys.path.insert(0, str(ROOT / 'b_work/step4'))
from build_gold_sft import validate as validate_sft
sys.path.insert(0, str(ROOT / 'b_work/step3'))
from build_gold import source_texts
sys.path.insert(0, str(ROOT))
from b_work.eval.score import supported_units
from b_work.eval.records import check_gold

def read_jsonl(p): return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]
def dump(p, x): p.write_text(json.dumps(x, ensure_ascii=False, indent=2)+'\n')
def jsonl(p, xs): p.write_text(''.join(json.dumps(x, ensure_ascii=False)+'\n' for x in xs))
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(x): return ' '.join(re.findall(r'\w+', unicodedata.normalize('NFKC',x).casefold()))
def U(desc, ans, sets, deps=(), necessary=False, aliases=(), **extra):
    u=dict(description=desc, expected_answer=ans, support_sets=sets, depends_on=list(deps), necessary=necessary)
    if aliases: u['aliases']=list(aliases)
    u.update(extra)
    return u

sources=read_jsonl(ROOT/'b_work/step2/prepared/samples_eval_reserved.jsonl')
S={i+1:copy.deepcopy(s) for i,s in enumerate(sources)}
A={}; original_notes={}; protected={}
for n in range(6,11):
    base=ROOT/f'b_work/test_set/batches/batch_{n:02}'
    for name in ('review.md','gold.jsonl','annotations.json','checks.json'):
        p=base/name
        protected[str(p.relative_to(ROOT))]=digest(p)
    for a in json.loads((base/'annotations.json').read_text())['records']:
        A[a['question_number']]=copy.deepcopy(a)
    for section in re.split(r'(?=^## Q)',(base/'review.md').read_text(),flags=re.M)[1:]:
        q=int(re.match(r'## Q(\d+)',section)[1])
        original_notes[q]=section.split('<details>',1)[0].split('Notes:',1)[1].strip()
OLD_A=copy.deepcopy(A); OLD_S=copy.deepcopy(S)
reasons={}; decisions={}; edits={}; exceptions={}

def explain(q,text):
    reasons.setdefault(q,[]).append(text)

def set_units(q, units, kind=None):
    for i,u in enumerate(units,1):u['unit_id']=f'u{i}'
    A[q]['units']=units
    if kind:A[q]['question_type']=kind

def single(q,desc,ans,sets,aliases=(),presup=None):
    kw={} if not presup else dict(presupposition_sets=presup,by_presupposition=True)
    set_units(q,[U(desc,ans,sets,necessary=True,aliases=aliases,**kw)],'single')

def add(q,idx,*sets):
    for st in sets:
        if st not in A[q]['units'][idx-1]['support_sets']:A[q]['units'][idx-1]['support_sets'].append(st)

def word(q,new,why):
    S[q]['question']=new
    edits[q]=why
    # Keep conclusion descriptions synchronized with rewritten questions.
    for u in A[q]['units']:
        if u['description']==OLD_S[q]['question']:u['description']=new
    explain(q,'题干澄清：'+why)

def choice(q, facts, answer, aliases=()):
    """One fact per candidate; OR shortcuts cite only an established fact."""
    us=[]; shortcuts=[]
    for desc,value,sets,omission in facts:
        us.append(U(desc,value,sets,by_omission=True) if omission else U(desc,value,sets))
        shortcuts.extend(sets)
    us.append(U(S[q]['question'],answer,[[]],deps=('u1','u2'),necessary=True,
                aliases=aliases,by_presupposition=True,presupposition_sets=shortcuts))
    set_units(q,us,'comparison')

# Batch 6
single(152,'location of the National Gallery of Art','Washington, D.C.',[['d9s0'],['d10s0'],['d3s2']],('Washington DC',))
explain(152,'题干已点名美术馆，删除画作桥接；新增d10s0、d3s2备选。')
word(152,OLD_S[152]['question'].replace('which state?','which city?'),'Washington, D.C.不是州，改问城市，保留原题及源答案供追溯。')
add(155,2,['d4s1']);exceptions[155]='按用户note，本题将founding year作为opening date；不推广到其他题。'
explain(155,'按用户明确口径，用d4s1的1861支持u2；u3继续按年份比较。')
add(158,2,['d1s3'],['d6s2']);add(158,1,['d10s1'])
explain(158,'d1s3写的是Khan Kluay，因此补入u2而非u1；另补u2的d6s2与u1的d10s1。')
A[159]['units'][1].update(expected_answer='Betsy Ross flag',support_sets=[['d9s0','d9s2']])
word(159,'What flag features 13 stars and is popularly attributed to the woman after whom the memorial bridge connecting Pennsylvania and New Jersey is named?', '将creator改为popularly attributed，避免把原文明确存疑的归属写成事实。')
explain(159,'将人名答案改为Betsy Ross flag；用d9s0+d9s2支持旗帜及13颗星，保留桥梁人物定位。')
choice(161,[('whether Strange Synergy is a card game published by Steve Jackson Games','yes',[['d5s0']],False),('whether Qwirkle is a card game published by Steve Jackson Games','no',[['d2s0']],True)],'Strange Synergy')
explain(161,'每个候选各建一个非necessary事实unit；Qwirkle的定义支持类别排除，结论支持确认和排除两条预设链路。')
set_units(162,[U('actress with the surname Saravanan','Jyothika Saravanan',[['d3s0']],aliases=('Jyothika',)),U('actress {u1} who starred in the 2004 Tamil film Arul','Jyothika Saravanan',[['d5s0']],('u1',),True,('Jyothika',))],'bridge')
explain(162,'先按题干姓氏定位女演员，再验证出演Arul；删除提前泄漏Jyothika的描述。')
decisions[163]='已检索完整上下文；d3s1只说明Hawking创办中心，不能替代Director of Research证据。保留d5s0及现有链路。'
single(164,'brewer whose advertising mascot was Alex the Dog',"Stroh's",[['d9s0']],('Stroh',))
explain(164,'Alex the Dog已在题干出现，删除Spuds MacKenzie桥接；d9s0直接定位品牌。')
add(165,1,['d9s0','d9s1']);add(165,2,['d7s2'])
explain(165,'d9s0单独没有magic主题，不能独自定位电影；增加d9s0+d9s1链路，并补d7s2的2006作为年份备选。')
choice(166,[('whether Old German Shepherd Dog has origins outside the United States','yes',[],False),('whether Black Mouth Cur has origins outside the United States','no',[['d8s0']],False)],'Old German Shepherd Dog')
explain(166,'补建两候选事实unit，保留由Black Mouth Cur的美国起源排除得到答案的链路。d5s0是另一种传统牧羊犬群体，d2s0是German Shepherd，均不强行作为目标变种的直接起源证据；u1仍UNRESOLVED但不阻塞结论。')
A[167]['units'][-1]['aliases']=['Teru','TERU','Teruhiko Kobashi'];explain(167,'出生日期比较符合规则；补齐题干艺名Teru及全名别名，避免只接受Teruhiko。')
choice(170,[('whether Hot toddy is traditionally drunk before bed','yes',[['d1s1']],False),('whether Kir is traditionally drunk before bed','no',[],False)],'Hot toddy')
explain(170,'补建Kir事实unit，定义未记载饮用习惯，不能by_omission；Hot toddy正向证据独立完成结论。')
decisions[173]='问题意思是“James Tully于1928年当选代表的选区，以谁命名？”d4s4先定位Barton，d2s1再给出Sir Edmund Barton，现有两跳正确。'
add(179,1,['d3s5'],['d10s0']);explain(179,'补充d3s5和d10s0：均联系Neiman Marcus、Dallas及1907；不使用只说明现在总部的d8s0。')
word(180,'Comparing the lineups stated in the context, which band has more members, Chvrches or Goodbye Mr. Mackenzie?','限定为文档列出的阵容，避免比较当前阵容与历史全体成员。')

# Batch 7
single(181,'animal type of Oscar','black cat',[['d6s0']]);explain(181,'u1已给出完整答案，移除黑猫定义的重复桥接。')
A[183]['units'][-1]['aliases']=['Joe Orton','John Kingsley Orton'];explain(183,'保留正向确认链路；补题干短名Joe Orton为答案别名，不从Henry James的职业介绍推断作品命名关系。')
single(186,'actor who voices Homer Simpson','Dan Castellaneta',[['d3s1'],['d5s1'],['d4s1']],('Daniel Louis Castellaneta',))
explain(186,'合并为single，移除全名转换；d3s0仅介绍角色，按标题可解析He时不单独要求该句；补d5s1、d4s1备选。')
A[188]['units'][0]['description']='stadium used by the 2014 Baylor Bears football team';explain(188,'删除题干没有的新体育场限定new，其余链路由d3s2和d4s2明确支持。')
single(191,'scheduled release date of Flicker in the source','20 October 2017',[['d3s1']])
# Preserve the source date surface form from the old unit.
A[191]['units'][0]['expected_answer']=OLD_A[191]['units'][-1]['expected_answer']
explain(191,'Flicker已在题干中，删除演员/歌手桥接；保留来源当时的计划发行日期。')
word(192,'Who has more pen names explicitly listed in the context, George Orwell or Nelson DeMille?','限定为文档列举的笔名数量，不断言终身总数。')
A[192]['units'][-1]['aliases']=['Nelson DeMille'];explain(192,'继续比较1与4，新增题干短名Nelson DeMille。')
decisions[193]='保留。English→England是国别形容词归一化；题干问from而非公民身份，出生地与国别描述可用于本题。'
add(200,2,['d7s1']);A[200]['units'][1]['aliases']=['Secretary of the Interior']
explain(200,'d7s1本来已支持u1，同时直接说明辞职后任Secretary of the Interior，补作u2备选；无需等d3s0扩展官职名称。')
choice(203,[('whether Zach Bogosian is a record producer','no',[['d5s0','d5s1']],True),('whether Daron Malakian is a record producer','yes',[['d8s0']],False)],'Daron Vartan Malakian',('Daron Malakian',))
explain(203,'按SFT两候选格式补建Bogosian的职业排除unit；确认与排除各自可完成结论，补短名别名。')
single(206,'election Bob Beers announced in January 2014 he would enter against Harry Reid','2016 U.S. Senate election',[['d9s2']],('The 2016 United States Senate election','2016 United States Senate election in Nevada'))
word(206,'In January 2014, what election did Bob Beers announce he would enter against Senator Harry Reid in Nevada?','将含混的was at限定为原文记载的2014年竞选宣布，不暗示实际参加或出席2016年选举。')
explain(206,'删除全名桥接，d9s2即可回答；保留完整选举名称为别名。')
choice(208,[('whether Sigmund Freud left to escape the Nazis','yes',[['d4s5']],False),('whether Evelyn Waugh left to escape the Nazis','no',[],False)],'Sigmund Freud')
explain(208,'已检查d10s0–d10s3的Waugh介绍，没有逃离纳粹的信息；历史事件不能用职业遗漏排除。补候选unit但仅启用Freud正向链路。')
decisions[209]='保留两跳。铁路名称含Bodie不等于题干明确给出终点；d5s0仍是确认ghost-town terminus所需证据，不能仅按名称跳过。'

# Batch 8
word(215,'Where is the transmitter of the television station licensed to Topeka, KS, located?','区分电视台许可城市Topeka与发射机所在地Maple Hill；证据和答案不变。')
single(218,"city where the Salon d'Automne was first held",'Paris',[['d8s0']])
word(218,"In which city has the Salon d'Automne been held since its first exhibition in 1903?",'删除不唯一的画家筛选，将founding location明确为1903年开始的展览举办城市。')
explain(218,'single直接使用d8s0；不再事后挑选Vallotton，也不将创办者住所当作展览地点。')
A[221]['units'][-1].update(expected_answer='yes',support_sets=[[]]);explain(221,'d10s0与d9s0均列lemon juice，修正no→yes，u3由两组成分交集推出。源答案no留在来源记录。')
A[222]['units'][0]['description']='river on which Widnes is located';add(222,1,['d7s3']);explain(222,'按题干去掉north bank额外限定，补d7s3备选。')
single(223,'novella on which Eyes Wide Shut is based',OLD_A[223]['units'][1]['expected_answer'],[['d3s1']],('Traumnovelle','Dream Story'));explain(223,'题干已给电影名，移除Vinessa Shaw桥接。')
A[224]['units'][0].update(description='Grand Slam title counts listed for Liezel Huber',expected_answer="4 women's doubles with Cara Black; 1 with Lisa Raymond; 2 mixed doubles with Bob Bryan")
explain(224,'事实unit保留原文4、1、2，不把7冒充原文值；u3按确定性算术4+1+2=7<39比较。')
choice(228,[('whether Frankie Valli sang with Hellogoodbye','no',[],False),('whether Frankie Valli sang with The Four Seasons','yes',[['d4s3']],False)],'The Four Seasons')
explain(228,'补两候选结构。另一乐队的创办者信息不能证明Valli从未加入，关系属性不按遗漏排除；仅启用Four Seasons确认链路。')
A[230]['units'][1].update(expected_answer='born 27 February 1934; alive in 2007 under the accepted award-based bound',support_sets=[['d3s0','d3s3']])
A[230]['units'][2]['support_sets']=[[]]
exceptions[230]='按用户明确认可，将2007年获奖记载视为在世年龄下界；这是本题获准的推断，不宣称来源明确写出寿命或普遍证明奖项只能颁给在世者。'
explain(230,'补d3s0+d3s3。按用户接受的获奖年龄下界，2007年最早也已72年10个月，超过Glasgow约72年7个月，u3可比较；不使用今天日期。')
add(231,2,['d2s1'],['d3s1']);explain(231,'补两个明确two species的备选证据。')
word(232,'What author wrote a three-book memoir series whose books include works studied in school systems around the world?','限定系列中有作品被学校采用，不把个别作品的教学使用扩大为全部三本。')
word(235,'Which four business areas are explicitly named for the company chaired by the wealthiest person in Georgia in the stated 2017 list?','将four divisions改为four named business areas，并限定来源2017年榜单；不把other businesses删除。')
add(236,2,['d4s2'],['d10s1']);explain(236,'补两条明确说明Toussaint Louverture领导Haitian Revolution的备选。')
choice(237,[('whether Southwest Oregon Regional Airport is operated by the Coos County Airport District','yes',[['d4s1']],False),('whether Lawton–Fort Sill Regional Airport is operated by the Coos County Airport District','no',[],False)],'Southwest Oregon Regional Airport')
explain(237,'补两候选结构，城市所有权不是运营者证据；保留正向确认链路，不臆造另一机场运营关系。')
A[238]['units'][0].update(description='listed distribution regions of Cussonia',expected_answer='Africa (South Africa and the Mascarene Islands; Afrotropics)',support_sets=[['d5s1'],['d5s0']])
A[238]['units'][2]['support_sets']=[[]]
exceptions[238]='按用户note接受Afrotropics及South Africa到Africa的地域归一化，仅用于本题分布证据；不推广到无证据的经纬度比较。'
explain(238,'将origin描述改为distribution，按用户要求补d5s0备选；d5s1使用的是center of distribution部分，u3以两种植物的非洲分布交集推出。')
single(240,'author of the series containing A Wind in the Door',"Madeleine L'Engle",[['d2s1','d7s0']],presup=[['d2s0']])
exceptions[240]='按用户要求，单本小说作者捷径依赖本题同作者系列的预设；明确放在presupposition_sets，不当作“书作者必等于系列作者”的普遍证据。'
explain(240,'保留两条路径：d2s0为预设捷径；d2s1+d7s0为完整系列桥接证据。合并到一个必要unit，避免无条件依赖u1挡住捷径。')

# Batch 9
A[242]['units'][0]['description']='American author of a series of four vampire-themed fantasy romance novels';explain(242,'删除题干未给出的Twilight，避免描述提前泄漏中间信息。')
add(246,1,['d2s0'],['d4s0'],['d5s0'],['d10s0']);explain(246,'补齐四条Brooklyn属于New York City的明确备选证据。')
add(250,1,['d1s1','d1s2']);add(250,2,['d10s0']);explain(250,'保留至少3的下界，精确3也支持该下界；补Laurus和Liriodendron备选。')
add(252,2,['d10s0'],['d10s0','d10s2']);explain(252,'电影written by已支持编剧职业；另收录全名与screenwriter Mutrux的组合，避免单靠姓氏对应。')
add(253,2,['d4s1']);explain(253,'标题The Simpsons (season 10)提供季名，d4s1同时说明首集和集数，可独立替代d1s0。')
single(254,'location where the 1920 Politics strategy operated','Hawaii',[['d8s0']],('Territory of Hawaii',))
word(254,'In what U.S. territory did the 1920 Politics strategy operate?','改为历史领地，不把1920年的Hawaii称为当时的州；Territory of Hawaii与Hawaii作为名称归一化。')
explain(254,'删除领地升州的额外桥接，用d8s0直接回答。')
A[255]['units'][0].update(description='upper bound on the mainland branch-office counts reported for China CITIC Bank',expected_answer='at most 773',support_sets=[['d2s4'],['d2s5']])
word(255,"Using the branch counts stated in the context, which is larger: China CITIC Bank's mainland branch network or UniCredit's network?",'限定为原文提供的两个网络口径，不推断同一时点全球网点总量。')
explain(255,'u1采用共同上界773：78+622=700及2011年的773都满足；与UniCredit的>8500比较，避免把两个不同值当作同一个精确值。')
add(256,1,['d2s1']);explain(256,'补博物馆位于Winter Park的备选d2s1。')
choice(257,[('whether The Seine Meets Paris is a French documentary','yes',[['d8s0']],False),('whether Great Old Amusement Parks is a French documentary','no',[],False)],'The Seine Meets Paris')
explain(257,'补另一候选unit。d6s0列PBS和作者而未列国籍，不满足“已列出该属性其他值”的omission条件，故仅保留正向确认。')
single(260,'Australian politician representing Goulburn in the source','Pru Goward',[['d9s1'],['d3s3']],('Prudence Jane Goward','Jane Goward'))
explain(260,'删除全名桥接，按标题可解析Goward，补d3s3备选；接受Pru和全名以及源短名。')
set_units(264,[U('company founded by the person after whom Henry W. Bloch School of Management is named','H&R Block',[['d4s2']]),U('city where {u1} is based','Kansas City',[['d9s1']],('u1',),True)],'bridge')
explain(264,'同句给出冠名人物及公司，合并为公司定位unit，保留公司到所在地的真正第二跳。')
decisions[265]='保留d3s1→d5s0两跳。d3s1只说明来自Cradle of Filth，未说明创始成员；题干没有点名该乐队，也不能排除他在多个乐队任职，故不把一般成员关系直接升级为founder捷径。'
single(268,'railway serving Summerseat and running between Heywood and Rawtenstall','East Lancashire Railway',[['d5s1'],['d6s0']]);explain(268,'每句都同时满足两个条件，合并为single且两句互为备选。')
add(269,2,['d3s0','d3s3']);A[269]['units'][2]['support_sets']=[[]]
explain(269,'民军两用且主要服务居住于美国东部的波多黎各人，组合明确描述民用旅客服务；补u2并使u3可推导。d8s1只说charter，未区分客运货运，不单独接受。')

# Batch 10
choice(271,[('whether W. Somerset Maugham was ordained to the priesthood','no',[],False),('whether Thomas Merton was ordained to the priesthood','yes',[['d8s2']],False)],'Thomas Merton')
explain(271,'补两候选结构。按当前guide，ordination是事件而非职业，d9s0的作家职业介绍不能证明未受圣职；纠正旧note，保留Merton正向链路。')
set_units(273,[U('film adaptation of a play by Ira Lewis','Chinese Coffee',[['d4s1','d4s2']]),U('whether {u1} stars an actor whose name includes Jerome Bernard','Chinese Coffee',[['d4s2','d3s0']],('u1',),True)],'bridge')
# The answer unit asks for the film, not a yes/no value.
A[273]['units'][1]['description']='film {u1} starring an actor whose name includes Jerome Bernard'
explain(273,'先确定Ira Lewis戏剧的电影，再用演员表及完整姓名验证Jerome Bernard；不从部分姓名任意选Orbach。Karabel也不被误称为演员。')
set_units(274,[U('federal agency founded in 1935','FBI',[['d2s1']],aliases=('Federal Bureau of Investigation',)),U('agency {u1} that maintains the wanted-person list','FBI',[['d1s0'],['d4s0']],('u1',),True,('Federal Bureau of Investigation','the Federal Bureau of Investigation (FBI)'))],'bridge')
explain(274,'删除全名转换用途；先核对1935年成立，再验证通缉名单，补d4s0。两项筛选都保留，不能因回答出FBI就忽略年份。')
single(276,'whether A Cure for Wellness is science fiction','yes',[['d3s0']]);explain(276,'是非题答案改为yes，类型和年份片段保留在来源中。')
set_units(277,[U('network owned by the Bell Media division of BCE since 2000 in the source','CTV',[['d8s1']]),U('network {u1} that aired Gameshow Marathon','CTV',[['d3s2']],('u1',),True)],'bridge')
explain(277,'反转筛选顺序，先所有权条件再播出关系；去掉Canadian额外限定，不从CBS/CTV中事后选答案。')
add(280,1,['d2s2']);explain(280,'d2s2明确说明影片发布于BBC iPlayer，可支持题干所指BBC发布机构，补作u1备选。')
A[282]['units'][-1]['aliases']=['director','film director','director and screenwriter','screenwriter and director'];explain(282,'题干只问共同职业，screenwriter及film director都成立，加入其他有效答案；此处aliases承载可接受答案集合，不声称两种职业语义等同。')
add(289,1,*[[e] for e in ('d3s0','d4s0','d6s0','d7s0','d9s0','d10s1')]);add(289,2,['d9s2']);explain(289,'补齐主唱身份六条备选及公司创办d9s2；d9文档可独立完成两跳。')
add(290,2,['d9s3']);explain(290,'补1396 ft的独立备选，保持建成高度口径。')
set_units(291,[U('title character of the 1994 comedy-drama adaptation of a Winston Groom novel','Forrest Gump',[['d10s0','d10s2'],['d10s0','d2s0']]),U('nickname of Stephan Lichtsteiner matching {u1}','Forrest Gump',[['d9s1']],('u1',),True)],'bridge')
explain(291,'先按电影条件定位角色，再核验球员昵称；补人物条目路径，避免先输出两个候选昵称。')
decisions[298]='保留Chilopsis的明确单种正向链路和唯一候选预设。Cunninghamia的one or two不等于明确多于一种，不增设排除证据；在报告保留分类不确定性。'
A[299]['units'][-1]['aliases']=['Christopher Guest'];explain(299,'补题干姓名别名。')
word(299,'Who has more distinct professions explicitly listed in the context, Christopher Guest or Roman Karmen?','将主观wider scope明确为文档列举职业数量，按6与2比较。')

# Replace unrepairable questions using manually reviewed unused train examples.
replacement_specs={
153:(0,'u1不唯一且d10s3未给SexyBack第一名；这是桥接定位和关键排名缺证据，不能据源答案补造。'),
156:(3,'山峰被错标为subrange；按用户要求替换。'),
174:(7,'只有城市，无南北方位或纬度；当前guide不允许隐含地理知识。'),
189:(20,'美国到非欧洲需要额外地理映射，当前guide明确不允许。'),
190:(30,'Hole的两个创办者不是完整阵容；未找到可比较的成员总数。'),
195:(2,'创建奖项不等于赞助奖项；上下文没有明确赞助关系。'),
196:(32,'French Air Force任职不等于法国来源/国籍；没有其他支持u2的句子。'),
201:(36,'没有县与镇的政府层级规则，不能从两地所有者直接推出higher。'),
205:(42,'bimonthly在上下文未消歧，无法确定比monthly多还是少。'),
210:(14,'producer不能直接等同impresario；按用户要求替换。'),
226:(47,'乐队成员关系不唯一且用户明确要求换题。'),
239:(48,'WPX没有部门数量，不能将沉默算成0。'),
241:(21,'四名回归球员，题干没有唯一定位条件。'),
247:(49,'Ural上下文未说明公立性质；前身名称不能补出合并后性质。'),
249:(50,'缺少原始阵容及保持原阵容录制的专辑数，不能由主唱离队倒推。'),
261:(25,'third after A and B未明确两者顺序，不能支持紧邻的next smaller关系。'),
266:(51,'Ainslee文档未给出版频率。'),
270:(52,'缺少东西相对方位或经度。'),
279:(54,'缺少东西相对方位或经度。'),
287:(35,'母公司创始人不能直接当作电视网络创始人。'),
288:(38,'Fred Taylor及Corey Dillon均满足条件，答案不唯一。'),
292:(55,'上下文只给London；当前规则未允许city→country常识映射。'),
295:(56,'district与province层级不一致，且没有可用的行政层级推理规则。'),
300:(41,'Jim Cummings配音的是Dr. Robotnik，作品名Sonic不是刺猬角色配音证据。'),
}
# Export selected immutable source records separately; candidate indices were for review only.
replacement_source=OUT/'replacement_sources.jsonl'
if not replacement_source.exists():
    candidates=read_jsonl(Path('/tmp/replacement_candidates.jsonl'))
    jsonl(replacement_source,[candidates[k] for k,_ in replacement_specs.values()])
R=read_jsonl(replacement_source)
assert len(R)==len(replacement_specs)
bridge_data={
153:('hotel company associated with the Oberoi family','The Oberoi Group','d2s0','city of the head office of {u1}','Delhi','d7s0'),
195:('historical period in Korea when Chang Ucchin was born','Japanese colonial rule','d10s1','war whose conclusion ended {u1} in Korea','World War II','d5s0'),
210:('winner of the 2016 Marrakesh ePrix','Sébastien Buemi','d5s2','birth year of {u1}','1988','d7s0'),
241:('son of Fannie Lee Chaney','James Chaney','d10s0','date of birth of {u1}','May 30, 1943','d6s0'),
261:('city where Foeke Booy was born','Leeuwarden','d5s0','population of {u1} in the source','108,249','d1s0'),
287:('town where Kerry Saxby-Junna was born','Young, New South Wales','d3s1','2011 census population of {u1}','6,960','d7s1'),
288:('actress playing Trudy, the wife of Sam Sloan, in The Single Guy','Ming-Na Wen','d4s2','nationality of {u1}','American','d8s0'),
300:('author of the poetry collection Early Work','Patti Smith','d9s0','nationality of {u1}','American','d8s0'),
}
comparison_data={
156:('Pablo Trapero','1971','d3s0','Aleksander Ford','1908','d9s0','Aleksander Ford'),
174:('Glenn Hughes','1951','d5s0','Ross Lynch','1995','d3s0','Glenn Hughes'),
189:('Kim Clijsters','1983','d8s0','Mary Pierce','1975','d9s0','Mary Pierce'),
190:('Odysseas Elytis','1911','d6s0','Cornel West','1953','d1s0','Odysseas Elytis'),
196:('The Hunchback of Notre Dame','1996','d7s0','Saludos Amigos','1942','d9s0','Saludos Amigos'),
201:('Neil LaBute','1963','d8s0','H. Bruce Humberstone','1901','d2s0','H. Bruce Humberstone'),
205:('George Marshall','1891','d4s0','Allan Dwan','1885','d9s0','Allan Dwan'),
226:('Joe Manganiello','1976','d3s0','Kirk Kerkorian','1917','d10s0','Kirk Kerkorian'),
239:('Vincent Walker','1980','d5s0','David Usher','1966','d1s0','David Usher'),
247:('Beyond the Gates of Splendor','2004','d6s0','Jesus Camp','2006','d8s0','Beyond the Gates of Splendor'),
249:('Martin Heidegger','1889','d8s0','Lydia Davis','1947','d10s0','Martin Heidegger'),
266:('Lorraine Hansberry','1930','d4s0','Sandra Gulland','1944','d6s0','Lorraine Hansberry'),
270:('Almost Sunrise','2016','d5s0','51 Birch Street','2005','d10s0','51 Birch Street'),
279:('Tanya Donelly','1966','d6s0','Trace Cyrus','1989','d2s0','Tanya Donelly'),
292:('John Tardy','1968','d9s0','Tom Barman','1972','d8s0','John Tardy'),
295:('Rohan Bopanna','1980','d7s0','Sherwood Stewart','1946','d5s0','Sherwood Stewart'),
}
for (q,(k,why)),s in zip(replacement_specs.items(),R):
    assert s['type']==OLD_S[q]['type'], (q,s['type'])
    S[q]=copy.deepcopy(s)
    A[q]=dict(question_number=q,sample_id=s['sample_id'],status='draft',question_type=s['type'],units=[],review_flags=[],notes=[])
    if q in bridge_data:
        d,v,e,fd,fv,fe=bridge_data[q]
        set_units(q,[U(d,v,[[e]]),U(fd,fv,[[fe]],('u1',),True)],'bridge')
    else:
        n1,v1,e1,n2,v2,e2,answer=comparison_data[q]
        attr='film year of ' if q in (196,247,270) else 'birth year of '
        aliases=[S[q]['answer']] if answer!=S[q]['answer'] else []
        set_units(q,[U(attr+n1,v1,[[e1]]),U(attr+n2,v2,[[e2]]),U(S[q]['question'],answer,[[]],('u1','u2'),True,aliases)],'comparison')
        assert answer==(n1 if int(v1)<int(v2) else n2)
    explain(q,'替换：'+why+' 新题保留原source type，人工核对两条显式事实及答案。')

# Avoid leaking a value in the schema's description even when it lists answer options.
for q in range(151,301):
    for u in A[q]['units']:
        if 'public or private status' in u['description']:
            u['description']=u['description'].replace('public or private status','institutional funding classification')
            explain(q,'将public or private答案选项从unit描述移至属性名institutional funding classification，避免SFT描述泄漏校验误判。')

# Record review dispositions for every original note, including unchanged decisions.
for q in range(151,301):
    if q not in reasons and q not in decisions:
        decisions[q]='复核后保留原标注；原note为说明或未发现需要修改的证据/依赖问题。' if original_notes[q] else '无待处理note，保留原标注。'
    A[q]['status']='draft'  # Generated revision is not a claim of human approval.
    A[q]['notes']=(OLD_A[q].get('notes',[]) if q not in reasons else []) + reasons.get(q,[]) + ([decisions[q]] if q in decisions else [])
    if q in exceptions:A[q]['notes'].append('本题局部约定：'+exceptions[q])
    A[q]['review_flags']=[]
    if q in exceptions:A[q]['review_flags']=['explicit_local_annotation_convention']
    if q==298:A[q]['review_flags']=['other_candidate_species_count_uncertain']
    A[q]['revision']={'original_sample_id':OLD_A[q]['sample_id'],'disposition':'replaced' if q in replacement_specs else ('adjusted' if q in reasons else 'retained'),'original_review_note':original_notes[q]}

# Reproducibility and leakage audit; never silently overwrite a changed original.
manifest_path=OUT/'manifest.json'
if manifest_path.exists():
    previous=json.loads(manifest_path.read_text())['original_file_sha256']
    assert protected==previous,'Original inputs changed since this revision was built; create a new revision directory.'
exclusions=[ROOT/'b_work/step2/prepared/samples_debug.jsonl',ROOT/'b_work/step2/prepared/samples_eval_reserved.jsonl',ROOT/'b_work/step4/prepared/samples_sft_candidates.jsonl',ROOT/'b_work/step4/gold_sft.jsonl']
used_ids=set();used_questions=set()
for p in exclusions:
    for s in read_jsonl(p):
        used_ids.add(s['sample_id'])
        if 'question' in s:used_questions.add(norm(s['question']))
for q in replacement_specs:
    assert S[q]['sample_id'] not in used_ids,('leakage id',q)
    assert norm(S[q]['question']) not in used_questions,('leakage question',q)
assert len({S[q]['sample_id'] for q in range(151,301)})==150
assert len({norm(S[q]['question']) for q in range(151,301)})==150
# Verify every replacement remains an exact source excerpt, not fabricated context.
raw_path=ROOT/'b_work/step2/raw/hotpot_train_v1.1_hf.json'
raw=json.loads(raw_path.read_text())
raw_by_id={r['_id']:r for r in raw if 'hotpotqa_'+r['_id'] in {s['sample_id'] for s in R}}
for s in R:
    r=raw_by_id[s['sample_id'].removeprefix('hotpotqa_')]
    for f in ('question','answer','context','supporting_facts','type'):assert s[f]==r[f],(s['sample_id'],f)
del raw,raw_by_id

def gold(q):
    return dict(schema_version='1.0',data_version=VERSION,sample_id=S[q]['sample_id'],question_type=A[q]['question_type'],source_type=S[q]['type'],units=A[q]['units'])

def fmt_sets(sets):
    if sets==[]:return '`[]`：无直接支持'
    if sets==[[]]:return '`[[]]`：由全部依赖推出'
    return ' OR '.join('['+', '.join(x)+']' for x in sets)
def cell(x):return str(x).replace('|','\\|').replace('\n','<br>')
def render(q):
    s=S[q];a=A[q];g=gold(q);texts=source_texts(s)
    lines=[f'## Q{q} — `{s["sample_id"]}` (revised draft)','', '> '+s['question'],'', 'Source answer: '+s['answer'],'', 'Gold final answer: '+next(u['expected_answer'] for u in g['units'] if u['necessary']),'',f'Question type: `{g["question_type"]}` (source type `{g["source_type"]}`)','']
    if q in replacement_specs:lines += ['Replaces: `'+OLD_A[q]['sample_id']+'`','']
    if q in edits:lines += ['Original question: '+OLD_S[q]['question'],'']
    lines += ['| Unit | Necessary | Expected answer | Depends on | Support sets | Presupposition sets |','|---|---|---|---|---|---|']
    cited=set()
    for u in g['units']:
        answer=u['expected_answer']
        if u.get('aliases'):answer+=' (accepted alternatives: '+'; '.join(u['aliases'])+')'
        for flag in ('by_omission','by_presupposition'):
            if u.get(flag):answer+=' **['+flag+']**'
        lines.append('| '+' | '.join(map(cell,[u['unit_id']+': '+u['description'],str(u['necessary']).lower(),answer,', '.join(u['depends_on']) or '—',fmt_sets(u['support_sets']),fmt_sets(u['presupposition_sets']) if u.get('presupposition_sets') else '—']))+' |')
        for f in ('support_sets','presupposition_sets'):
            cited.update(e for st in u.get(f,[]) for e in st)
    lines += ['','Evidence:','']
    for e in sorted(cited,key=lambda x:tuple(map(int,re.findall(r'\d+',x)))):
        t,i,txt=texts[e];lines.append(f'- `{e}` {t} [{i}]: {txt}')
    lines += ['','Notes:','']+['- '+t for t in a['notes']]+['','<details><summary>All source context</summary>','']
    for e,(t,i,txt) in texts.items():lines.append(f'- `{e}` {t} [{i}]: {txt}')
    lines += ['','</details>','']
    return '\n'.join(lines)

validation=[]
for q in range(151,301):
    g=gold(q);text=source_texts(S[q]);check_gold(g);validate_sft(g,S[q]['question'])
    for u in g['units']:
        for f in ('support_sets','presupposition_sets'):
            for st in u.get(f,[]):
                assert len(st)==len(set(st)),(q,u['unit_id'],'duplicate evidence')
                for e in st:assert e in text,(q,e)
    visible=set(text);byid={u['unit_id']:u for u in g['units']}
    full=supported_units(byid,visible);final=next(u for u in g['units'] if u['necessary'])
    assert final['unit_id'] in full,(q,'final unsupported')
    assert not supported_units(byid,set()),(q,'supported without evidence')
    for u in g['units']:
        # Verify each alternate explicit set works with all necessary dependencies supplied.
        def parent_evidence(uid):
            p=byid[uid];out=set(p['support_sets'][0] if p['support_sets'] else [])
            for dep in p['depends_on']:out |= parent_evidence(dep)
            return out
        parents=set().union(*(parent_evidence(d) for d in u['depends_on'])) if u['depends_on'] else set()
        for st in u['support_sets']:
            # An unresolved candidate can keep AND path closed; OR path is separately checked.
            if all(d in full for d in u['depends_on']):
                assert u['unit_id'] in supported_units(byid,set(st)|parents),(q,u['unit_id'],st)
    validation.append({'question_number':q,'sample_id':g['sample_id'],'final_supported_with_full_context':True,'unresolved_optional_units':[u['unit_id'] for u in g['units'] if u['unit_id'] not in full]})

# Minimal visibility tests exercise the actual evaluation code, not just schema validity.
scenarios=[(161,{'d5s0'},True),(161,{'d2s0'},True),(161,set(),False),
(166,{'d8s0'},True),(166,{'d5s0'},False),(170,{'d1s1'},True),
(200,{'d7s1'},True),(203,{'d8s0'},True),(203,{'d5s0','d5s1'},True),
(208,{'d10s0'},False),(208,{'d4s5'},True),
(240,{'d2s0'},True),(240,{'d2s1','d7s0'},True),(240,{'d7s0'},False),
(253,{'d1s3','d4s1'},True),(257,{'d6s0'},False),
(268,{'d5s1'},True),(268,{'d6s0'},True),
(271,{'d9s0'},False),(271,{'d8s2'},True),
(289,{'d9s0','d9s2'},True),(298,{'d10s0'},False)]
for q,visible,expected in scenarios:
    g=gold(q);byid={u['unit_id']:u for u in g['units']};f=next(u['unit_id'] for u in g['units'] if u['necessary'])
    assert (f in supported_units(byid,visible))==expected,(q,visible,expected)

all_gold=[];all_samples=[];all_changes=[]
for n in range(6,11):
    dest=OUT/f'batch_{n:02}';dest.mkdir(exist_ok=True)
    qs=list(range((n-1)*30+1,n*30+1))
    gs=[gold(q) for q in qs]
    ss=[]
    for q in qs:
        s=copy.deepcopy(S[q]);s['question_number']=q;s['data_version']=VERSION;s['project_split']='eval'
        if q in edits:s['original_question']=OLD_S[q]['question']
        if q in replacement_specs:s['replaces_sample_id']=OLD_S[q]['sample_id']
        s['gold_answer']=next(u['expected_answer'] for u in A[q]['units'] if u['necessary'])
        ss.append(s)
    jsonl(dest/'gold.jsonl',gs);jsonl(dest/'samples.jsonl',ss)
    dump(dest/'annotations.json',{'schema_version':'1.0','data_version':VERSION,'records':[A[q] for q in qs]})
    preamble='# Revised Gold — batch '+str(n)+'\n\n原始review保持不变。本文是依据原note生成的修订草稿；完整修改说明见[修改报告](../change_report.md)。\n\n句子带有文档标题；允许使用标题解析该文档中的人名及代词。support_sets内为AND，组间为OR；presupposition_sets按现有评估器表示预设捷径。\n\n'
    (dest/'review.md').write_text(preamble+'\n'.join(render(q) for q in qs))
    dump(dest/'checks.json',{'count':30,'checks_passed':True,'records':[x for x in validation if x['question_number'] in qs]})
    all_gold+=gs;all_samples+=ss
for q in range(151,301):
    all_changes.append({'question_number':q,'batch':(q-1)//30+1,'disposition':A[q]['revision']['disposition'],
        'original_sample_id':OLD_A[q]['sample_id'],'sample_id':S[q]['sample_id'],
        'original_question':OLD_S[q]['question'],'question':S[q]['question'],
        'original_source_answer':OLD_S[q]['answer'],'source_answer':S[q]['answer'],
        'original_question_type':OLD_A[q]['question_type'],'question_type':A[q]['question_type'],
        'original_units':OLD_A[q]['units'],'units':A[q]['units'],
        'original_note':original_notes[q], 'resolution':A[q]['notes']})
jsonl(OUT/'gold.jsonl',all_gold);jsonl(OUT/'samples.jsonl',all_samples);dump(OUT/'changes.json',all_changes)
counts=Counter(x['disposition'] for x in all_changes)
manifest={'data_version':VERSION,'date':'2026-11-12','status':'revised_draft_not_human_approved',
    'counts':dict(counts),'question_count':150,'question_wording_changes':sorted(edits),
    'original_file_sha256':protected,'replacement_source':str(raw_path.relative_to(ROOT)),
    'replacement_source_sha256':digest(raw_path),'replacement_source_split':'train',
    'replacement_exclusion_files':{str(p.relative_to(ROOT)):digest(p) for p in exclusions},
    'replacement_ids':[S[q]['sample_id'] for q in replacement_specs],
    'replacement_original_source_types':dict(Counter(OLD_S[q]['type'] for q in replacement_specs)),
    'source_type_counts':dict(Counter(g['source_type'] for g in all_gold)),
    'question_type_counts':dict(Counter(g['question_type'] for g in all_gold)),
    'local_conventions':exceptions,'semantics':'b_work/eval/score.py:supported_units',
    'limitations':['仓库未提供A端decompose实现，按本地labeling_guide、SFT格式及实际评估器核对；未调用线上拆词器。','训练源替代题仅从本项目未使用记录选取；不保证外部预训练模型未见过原数据。','新的presupposition_sets必须用支持该字段的评估器和本文渲染器；Step3旧validate/review不支持该字段。']}
dump(manifest_path,manifest)
report=['# Batch 6–10 修订报告','',f'保留原始五份review以及原gold/annotations不变。共150题：原题调整{counts["adjusted"]}题，替换{counts["replaced"]}题，核查后保留{counts["retained"]}题。仍保留每batch 30题及Q151–Q300编号。','',
'## 交付与使用','',
'- 各batch目录含新的 `samples.jsonl`、`annotations.json`、`gold.jsonl`、`review.md`、`checks.json`。',
'- [150题gold](gold.jsonl)和[samples](samples.jsonl)必须配套使用；替换题的ID和部分题干已变化。',
'- [changes.json](changes.json)保存150题逐题前后unit、原始note及处理结论；[manifest.json](manifest.json)记录源哈希、去重边界和局部约定。',
'- 后续重新抽取SFT候选时，必须把本目录samples.jsonl的ID及归一化题干加入排除集合；原Step2保留名单尚未切换到新版。',
'- 本次为修订草稿，不标作人工已批准，不修改原数据或生成训练样本。运行 `python b_work/test_set/revisions/batch06_10_v1/build_revision.py` 可重建本目录产物。','',
'## 处理原则与核查结论','',
'同一组证据内为AND，不同组为OR。真实依赖全部满足后才走普通support；命中presupposition_sets且至少一个父unit已支持时可走预设链路。证据句带原文档标题，可据标题解析代词/姓氏，不能据标题猜属性。', '',
'二选一题沿用SFT的两候选事实+结论格式；无法证明的另一候选保留UNRESOLVED，不能为了消除空support捏造否定。尤其Q166的old German herding dogs与目标变种不是同一实体；Q271的受圣职是事件，Q257未列国籍，均不满足旧note建议的omission条件。', '',
'Q230按用户明确认可使用获奖年份年龄下界；Q238按用户要求接受非洲分布归一化；Q240的小说作者捷径明确标成预设路径，不冒充系列作者的直接证据。这三项局部约定在gold review和manifest中单独说明。', '',
'没有找到A端拆词器实现，因此“符合规则”仅指本地guide/SFT结构及评估器验证，不声称完成线上模型输出对齐。','',
'## 修改清单','', '| 题号 | 处理 | 修改方法 |','|---|---|---|']
for x in all_changes:
    if x['disposition']=='retained':continue
    q=x['question_number'];n=x['batch']
    report.append(f'| [Q{q}](batch_{n:02}/review.md) | '+('替换' if q in replacement_specs else '调整')+' | '+cell(' '.join(x['resolution']))+' |')
report+=['','## 替换题映射','', '24道替代题来自本地HotpotQA train源；按ID和归一化题干排除原debug、原评估全集、SFT全部候选及已选gold。保留原source type（8 bridge、16 comparison），但比较子类型偏向可直接验证的日期/年份，未宣称细粒度难度分布不变。','', '| 原题号 | 新sample_id | 新问题 | 新答案 |','|---|---|---|---|']
for q in replacement_specs:report.append('| '+str(q)+' | `'+S[q]['sample_id']+'` | '+cell(S[q]['question'])+' | '+cell(next(u['expected_answer'] for u in A[q]['units'] if u['necessary']))+' |')
report+=['','## 已核查并保留的note','', '| 题号 | 结论 |','|---|---|']
for q in range(151,301):
    if q not in reasons and original_notes[q]:report.append(f'| Q{q} | '+cell(decisions[q])+' |')
report+=['','## 题干澄清（保留原文供追溯）','']
for q,why in edits.items():report += [f'### Q{q}','', '- 原题：'+OLD_S[q]['question'],'- 新题：'+S[q]['question'],'- 原因：'+why,'']
report+=['## 校验','', '- 150/150题结构、证据ID、依赖无环及最终答案在全上下文下可支持。','- 空上下文没有任何unit被错误支持；22个实际评估器最小证据场景通过。','- 24道替代题的题干、答案、context及supporting_facts与训练原始记录逐字段一致。','- 原五批20个review/gold/annotation/check文件SHA256前后相同。','- 另有非必要候选unit维持UNRESOLVED，属于未提供证据的事实，不阻塞已验证的预设最终路径。','']
(OUT/'change_report.md').write_text('\n'.join(report))
index=['# Batch 6–10 修订版','',
       '[逐题修改报告](change_report.md) · [新gold（150题）](gold.jsonl) · [配套samples](samples.jsonl) · [校验结果](validation_report.json)','',
       '原始batch目录不变。新样本和gold须配套使用。','',
       '| Batch | 调整原题 | 替换 | 保留 | 新review |','|---|---:|---:|---:|---|']
for n in range(6,11):
    c=Counter(x['disposition'] for x in all_changes if x['batch']==n)
    index.append(f'| {n} | {c["adjusted"]} | {c["replaced"]} | {c["retained"]} | [review.md](batch_{n:02}/review.md) |')
index += ['','每个batch还提供独立gold、samples、annotations和checks。12题题干澄清的原文与新版对照见修改报告；所有原note与处理决定见changes.json。','',
          '重建：`python b_work/test_set/revisions/batch06_10_v1/build_revision.py`。替代题来源快照在replacement_sources.jsonl，构建时核对本地训练原始文件。','',
          '后续重采样训练候选时需加入新版samples的排除清单。没有修改原Step2/SFT抽样程序。','']
(OUT/'README.md').write_text('\n'.join(index))
assert all(digest(ROOT/p)==h for p,h in protected.items())
dump(OUT/'validation_report.json',{'passed':True,'question_count':150,'batch_counts':{f'batch_{n:02}':30 for n in range(6,11)},'minimal_visibility_scenarios':len(scenarios),'replacement_count':len(R),'replacement_source_verified':True,'original_files_unchanged':True,'records':validation})
print(json.dumps({'counts':dict(counts),'wording_changes':sorted(edits),'scenarios':len(scenarios),'out':str(OUT)},ensure_ascii=False))
