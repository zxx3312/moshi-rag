"""Write what the agent says: the LLM step of the cascade (controller -> LLM -> TTS).

Evidence-aware actions get only the units the judge supported and their values, plus what is still missing,
so a Partial Answer cannot be asked to state more. The evidence text is left out: the judge has already checked
it, and the model read it aloud. Rule baselines get all visible evidence and give their best answer, so they
can be wrong; the short answers they report are what gets scored, one claim each.

Phrasing given facts needs less of a model than finding an answer in evidence, so the grounded sentences can
come from a smaller, faster model (grounded_client) while the baselines keep the large one.
"""
from __future__ import annotations

import json
import re
import unicodedata
from typing import Dict, List, Optional, Sequence, Tuple

GROUNDED_SYSTEM = """You are a voice assistant answering a question while a search is still running. Write what to say aloud next.

Rules:
- State every fact listed under "Say" in natural speech, with each value written exactly as given. Add nothing else, not even from your own knowledge.
- Say only those facts: nothing about what is left to do, and nothing else the question asks about.
- A value of "yes" or "no" must be heard as that word: start with "Yes," or "No,".
- Use as few words as natural speech allows, without repeating the question. Do not greet, read out these headings, or use lists.
Reply with JSON only."""

FREE_SYSTEM = """You are a voice assistant answering a question. Using the evidence you have so far, give your best answer now in one short spoken sentence, without lists. Use as few words as natural speech allows, without repeating the question.
Also list the answer alone in as few words as possible, for example a name, a date, "yes" or "no". List only what the question asks for, one item per thing asked, never supporting details: "Who was born later, A or B?" has one answer, the name; "When did X start and end?" has two. Each listed answer must appear word for word in what you say.
Reply with JSON only."""

GROUNDED_SCHEMA = {"type": "object", "properties": {"text": {"type": "string"}}, "required": ["text"]}
FREE_SCHEMA = {"type": "object", "properties": {"text": {"type": "string"},
                                                "answers": {"type": "array", "items": {"type": "string"}}},
               "required": ["text", "answers"]}
MAX_SPOKEN_WORDS = 40  # past the 25 asked for: the model is reading out more than the facts


def fold(text: str) -> str:
    """Lowercase without accents, still one character per character, so positions carry over."""
    return "".join((unicodedata.normalize("NFKD", c)[0].lower() or c)[0] for c in text)


def find_value(text: str, value: Optional[str]) -> int:
    """Position of the value in the text as whole words, or -1, so "no" is not found in "know".
    Case and accents are ignored: a judge that writes Sanchez has still said Sánchez."""
    if not value:
        return -1
    m = re.search(rf"(?<!\w){re.escape(fold(value))}(?!\w)", fold(text))
    return m.start() if m else -1


def adds_terms(text: str, request: str) -> bool:
    """Numbers, or capitalised words past a sentence start, that the request does not contain: facts nobody judged."""
    known = set(re.findall(r"[\w'-]+", fold(request)))
    terms = re.findall(r"(?<![.!?]\s)(?<!^)\b[A-Z][\w'-]*|\b\d+(?:,\d+)*\b", text)
    return any(t not in known and t.removesuffix("'s") not in known for t in map(fold, terms))


def _is_abstention(answer: str) -> bool:
    return answer.strip().strip(".").lower() in {"", "unknown", "not sure", "n/a", "none", "no answer"}


def _evidence_lines(evidence: Sequence[Tuple[Optional[str], str]]) -> str:
    return "\n".join(f"({title}) {text}" if title else text for title, text in evidence) or "(none)"


class Generator:
    """Results are cached, and the real call's latency is reported again on a cache hit: another
    delay schedule would have waited for that call too.

    A grounded reply that leaves out a value is replaced by the plain facts: what was never said must not
    earn credit. An abstaining baseline reports no answer, which makes no claim.
    """

    def __init__(self, client, grounded_client=None):
        self.client = client
        self.grounded_client = grounded_client or client
        self._cache: Dict[str, tuple] = {}
        self.fallbacks = 0
        self.log: List[dict] = []

    def _call(self, client, messages: List[dict], schema: dict) -> Tuple[dict, float]:
        key = json.dumps(messages, sort_keys=True)
        if key not in self._cache:
            n_calls = len(client.calls)
            try:
                raw = client.chat_json(messages, purpose="generate", schema=schema)
            except (ValueError, OSError):
                raw = {}
            latency = sum(c.latency_s for c in client.calls[n_calls:])
            self._cache[key] = (raw, latency)
            self.log.append({"request": messages[-1]["content"], "reply": raw, "latency_s": round(latency, 3)})
        return self._cache[key]

    def grounded(self, question: str, say: Sequence[Tuple[str, str]], missing: Sequence[str],
                 search_finished: bool) -> Tuple[str, float]:
        """say: (description, value). Returns (text, latency). While the search runs this is the facts alone: the
        policy decides what follows them once they are said, when it knows whether the search has caught up."""
        tail = "I could not confirm the rest." if search_finished else ""
        if not say:
            return (tail if missing else "That's all I found."), 0.0
        facts = "\n".join(f"- {d}: {v}" for d, v in say)
        request = f"Question: {question}\n\nSay:\n{facts}"
        raw, latency = self._call(self.grounded_client, [{"role": "system", "content": GROUNDED_SYSTEM},
                                                         {"role": "user", "content": request}], GROUNDED_SCHEMA)
        text = raw.get("text") if isinstance(raw.get("text"), str) else None
        if not (text and len(text.split()) <= MAX_SPOKEN_WORDS and all(find_value(text, v) >= 0 for _, v in say if v)
                and "still checking" not in text.lower() and not adds_terms(text, request)):
            self.fallbacks += 1
            text = " ".join(f"{d}: {v}." for d, v in say)
        return f"{text} {tail}" if missing and tail else text, latency

    def free(self, question: str, evidence: Sequence[Tuple[Optional[str], str]]) -> Tuple[str, List[str], float]:
        """Returns (text, answers, latency). An unusable or abstaining reply has no answers, so it claims nothing."""
        request = f"Question: {question}\n\nEvidence so far:\n{_evidence_lines(evidence)}"
        raw, latency = self._call(self.client, [{"role": "system", "content": FREE_SYSTEM},
                                                {"role": "user", "content": request}], FREE_SCHEMA)
        text = raw.get("text") if isinstance(raw.get("text"), str) else None
        answers = raw.get("answers") if isinstance(raw.get("answers"), list) else []
        return text or "I'm not sure.", [a for a in answers if isinstance(a, str) and not _is_abstention(a)], latency
