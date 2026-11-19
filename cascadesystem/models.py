"""Validated, answer-free plans and timestamped evidence."""
from dataclasses import asdict, dataclass, field
import re


@dataclass(frozen=True)
class Unit:
    unit_id: str
    description: str
    necessary: bool
    depends_on: tuple[str, ...]
    queries: tuple[str, ...]
    subject: str = ""


@dataclass(frozen=True)
class Evidence:
    evidence_id: str
    title: str
    url: str
    text: str
    visible_time_s: float
    requested_subject: str = ""
    resolved_title: str = ""
    entity_resolution: str = "unspecified"


def title_conflicts_with_subject(title, subject):
    """A differently qualified namesake is not the unqualified or another qualified entity."""
    normalize = lambda s: re.sub(r"\s+", " ", s.replace("_", " ")).strip().casefold()
    title, subject = normalize(title), normalize(subject)
    if not subject or title == subject:
        return False
    base_title = re.sub(r"\s*\([^()]*\)$", "", title)
    base_subject = re.sub(r"\s*\([^()]*\)$", "", subject)
    return base_title == base_subject and title != subject


def citation_identity_conflicts(source, subject, context=''):
    """Check namesakes while allowing an explicitly self-described article type.

    Live search keeps its stricter title resolution. A trace may omit Wikipedia's
    redundant type suffix; the cited lead must establish the same generic type.
    Geographic, dated and differently qualified namesakes remain blocked.
    """
    if source.entity_resolution == 'ambiguous':
        return True
    canonical = (source.resolved_title if source.requested_subject.casefold() == subject.casefold()
                 and source.resolved_title else subject)
    if not title_conflicts_with_subject(source.title, canonical):
        return False
    normalized = lambda text: re.sub(r'\s+', ' ', text.replace('_', ' ')).strip().casefold()
    title, target = normalized(source.title), normalized(canonical)
    split = lambda value: re.fullmatch(r'(.*?)\s*\(([^()]*)\)', value)
    left, right = split(title), split(target)
    # Never let evidence about one qualified identity override a different one.
    if left and right:
        return True
    qualified = left or right
    role = qualified.group(2) if qualified else ''
    generic_types = {'album', 'film', 'song', 'novel', 'book', 'band', 'director',
                     'actor', 'writer', 'singer', 'photographer', 'scientist', 'politician'}
    if role not in generic_types:
        return True
    if left and not re.search(r'\b' + re.escape(role) + r'\b', context, re.I):
        return True
    base = qualified.group(1).strip()
    lead = normalized(source.text.split('\n', 1)[0][:700])
    # A title alone is not enough. Require the lead's subject and explicit type.
    self_description = (re.escape(base) + r'(?:\s*\([^()]*\))?\s*,?\s+(?:is|was|are|were)\b'
                        + r'[^.!?]{0,240}\b' + re.escape(role) + r'\b')
    match = re.match(self_description, lead)
    if not match:
        return True
    predicate = re.split(r'\b(?:is|was|are|were)\b', match.group(), maxsplit=1)[-1]
    return bool(re.search(r'\b(?:of|by|about|with|replica|remake|copy|branch|friend|son|daughter)\b', predicate))


@dataclass
class Judgment:
    label: str = "UNRESOLVED"
    value: str = ""
    citations: list[str] = field(default_factory=list)
    quotes: list[dict] = field(default_factory=list)
    reason: str = ""


def plan_from_json(raw, max_units=8):
    if not isinstance(raw, dict):
        raise ValueError('Plan must be a JSON object')
    rows = raw.get("units")
    if not isinstance(rows, list) or not 1 <= len(rows) <= max_units:
        raise ValueError("Plan must contain 1..max_units units")
    units = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("Each unit must be an object")
        uid, description = row.get("unit_id"), row.get("description")
        deps, queries = row.get("depends_on"), row.get("queries")
        if not isinstance(uid, str) or not re.fullmatch(r"u[1-9][0-9]*", uid):
            raise ValueError("Unit IDs must be u1, u2, ...")
        if not isinstance(description, str) or not description.strip() or len(description) > 500:
            raise ValueError("Invalid unit description")
        if type(row.get("necessary")) is not bool:
            raise ValueError("necessary must be a boolean")
        if not isinstance(deps, list) or any(not isinstance(d, str) for d in deps) or len(deps) != len(set(deps)):
            raise ValueError("Invalid dependencies")
        if not isinstance(queries, list) or not 1 <= len(queries) <= 2 or any(not isinstance(q, str) or not q.strip() or len(q) > 400 for q in queries):
            raise ValueError("Each unit needs 1 or 2 short search queries")
        subject = row.get("subject", "")
        if not isinstance(subject, str) or len(subject) > 300 or any(c in subject for c in "|\n\r"):
            raise ValueError("Invalid subject title")
        units.append(Unit(uid, description, row["necessary"], tuple(deps), tuple(queries), subject.strip()))
    ids = {u.unit_id for u in units}
    if len(ids) != len(units) or not any(u.necessary for u in units):
        raise ValueError("Duplicate unit IDs or no necessary units")
    by_id = {u.unit_id: u for u in units}
    visiting, visited = set(), set()

    def visit(uid):
        if uid in visiting:
            raise ValueError("Dependency cycle")
        if uid in visited:
            return
        visiting.add(uid)
        for dep in by_id[uid].depends_on:
            if dep not in ids:
                raise ValueError("Unknown dependency")
            visit(dep)
        visiting.remove(uid)
        visited.add(uid)

    for unit in units:
        visit(unit.unit_id)
        for text in (unit.description, unit.subject, *unit.queries):
            if any(ref not in unit.depends_on for ref in re.findall(r"\{(u[0-9]+)\}", text)):
                raise ValueError("Placeholders must name explicit dependencies")
    return units


def resolve_text(text, judgments):
    for uid, judgment in judgments.items():
        if judgment.label == "SUPPORTED":
            text = text.replace("{" + uid + "}", judgment.value)
    if re.search(r"\{u[0-9]+\}", text):
        raise ValueError("Cannot search an unresolved dependency")
    return text


def validate_judgments(raw, units, evidence):
    """Exact quotes and visible IDs are checked here; semantic support is still model judged."""
    if not isinstance(raw, dict):
        raise ValueError('Judge reply must be a JSON object')
    rows = raw.get("judgments")
    if not isinstance(rows, list):
        raise ValueError("Judge must return judgments")
    by_id = {u.unit_id: u for u in units}
    sources = {e.evidence_id: e for e in evidence}
    if any(not isinstance(r, dict) for r in rows):
        raise ValueError("Invalid judge row")
    ids = [r.get("unit_id") for r in rows]
    if any(not isinstance(i, str) for i in ids) or len(ids) != len(set(ids)) or set(ids) != set(by_id):
        raise ValueError("Judge must return every unit exactly once")
    result = {}
    for row in rows:
        label = row.get("label")
        if label not in {"SUPPORTED", "UNRESOLVED", "CONTRADICTED"}:
            raise ValueError("Unknown judgment label")
        judgment = Judgment(label=label, reason=str(row.get("reason", ""))[:500])
        if label == "SUPPORTED":
            value, citations, quotes = row.get("value"), row.get("citations"), row.get("quotes")
            valid = (isinstance(value, str) and bool(value.strip()) and len(value) <= 1000
                     and isinstance(citations, list) and bool(citations)
                     and all(isinstance(c, str) and c in sources for c in citations)
                     and isinstance(quotes, list) and bool(quotes))
            if valid:
                quoted = set()
                for quote in quotes:
                    if not isinstance(quote, dict):
                        valid = False
                        break
                    eid, text = quote.get("evidence_id"), quote.get("text")
                    if not isinstance(eid, str) or eid not in citations or not isinstance(text, str) or not text.strip() or text not in sources[eid].text:
                        valid = False
                        break
                    quoted.add(eid)
                valid = valid and quoted == set(citations)
            if valid:
                judgment.value, judgment.citations, judgment.quotes = value.strip(), list(dict.fromkeys(citations)), quotes
            else:
                judgment = Judgment(reason="Rejected: missing value, invisible citation, or non-exact quote")
        result[row["unit_id"]] = judgment

    def identity_context(uid):
        related, pending = set(), [uid]
        while pending:
            current = pending.pop()
            if current not in related:
                related.add(current)
                pending.extend(by_id[current].depends_on)
        return ' '.join(by_id[current].description for current in related)

    def block(uid):
        for dep in by_id[uid].depends_on:
            block(dep)
        if result[uid].label == "SUPPORTED" and any(result[d].label != "SUPPORTED" for d in by_id[uid].depends_on):
            result[uid] = Judgment(reason="Dependency is not supported")
        if result[uid].label == "SUPPORTED" and by_id[uid].subject:
            target = resolve_text(by_id[uid].subject, result)
            for eid in result[uid].citations:
                source = sources[eid]
                if citation_identity_conflicts(source, target, identity_context(uid)):
                    result[uid] = Judgment(reason="Rejected entity identity: citation concerns an ambiguous or differently qualified namesake")
                    break

    for uid in by_id:
        block(uid)
    return result


def jsonable(value):
    return asdict(value)
