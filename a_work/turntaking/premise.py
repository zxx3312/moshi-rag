"""Conservative checks for selecting a named candidate from boolean subclaims."""
from __future__ import annotations

import re
import unicodedata


def words(text):
    return " ".join(re.findall(r"[^\W_]+", unicodedata.normalize("NFKC", text).casefold()))


def mentioned(name, text):
    return bool(name) and f" {name} " in f" {text} "


def candidate_name(description, normalized_name):
    """Read a candidate's original spelling from its 'whether NAME ...' unit."""
    text = unicodedata.normalize("NFKC", description)
    tokens = list(re.finditer(r"[^\W_]+", text))
    return text[tokens[1].start():tokens[len(normalized_name.split())].end()]


def candidate_relation(left, right):
    """Recover names and their shared predicate from two 'whether NAME PREDICATE' units."""
    left, right = words(left).split(), words(right).split()
    if left[:1] != ["whether"] or right[:1] != ["whether"]:
        return None
    left, right = left[1:], right[1:]
    predicate = []
    while len(left) > 1 and len(right) > 1 and left[-1] == right[-1]:
        predicate.append(left.pop())
        right.pop()
    if not predicate or left == right:
        return None
    return " ".join(left), " ".join(right), " ".join(reversed(predicate))


def states_unique(question, left, right, predicate):
    """Check for an affirmative uniqueness statement binding both candidates and the same predicate."""
    clauses = [words(clause) for clause in re.split(r"(?<=[.;!?])\s+", question) if not clause.rstrip().endswith("?")]
    for first, second in ((left, right), (right, left)):
        names = f"{re.escape(first)} (?:and|or) {re.escape(second)}"
        if any(re.fullmatch(f"(?:exactly|only) one of {names} {re.escape(predicate)}", clause)
               for clause in clauses):
            return True
    return False


def explicitly_excludes(name, predicate, citations, visible):
    """Accept an explicit negation of the same predicate, scoped to the eliminated person.

    This recognizer intentionally uses a small set of literal English forms. A date,
    paraphrase or loose mention with no matching negative claim cannot unlock this shortcut.
    """
    verb, _, rest = predicate.partition(" ")
    negations = {f"never {predicate}"}
    if verb in {"is", "are", "was", "were", "has", "have", "had"}:
        negations.add(f"{verb} not {rest}")
    else:
        base = {"won": "win", "wrote": "write", "made": "make", "worked": "work",
                "joined": "join", "received": "receive", "played": "play", "led": "lead",
                "starred": "star", "directed": "direct"}.get(verb)
        if base:
            negations.add(f"did not {base} {rest}".strip())
    for cite in citations:
        evidence = visible[cite]
        subjects = [name]
        if words((evidence.source or {}).get("document_id") or "") == name:
            subjects += ["he", "she", "they", "it"]
        sentence = words(evidence.text.replace("n’t", " not").replace("n't", " not"))
        if any(sentence == f"{subject} {negative}".strip() for subject in subjects for negative in negations):
            return True
    return False
