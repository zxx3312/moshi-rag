"""Write what the agent says: the LLM step of the cascade (controller -> LLM -> TTS).

Evidence-aware actions get only the units the judge supported and their values, plus what is still missing,
so a Partial Answer cannot be asked to state more. The evidence text is left out: the judge has already checked
it, and the model read it aloud. Rule baselines get all visible evidence and give their best answer, so they
can be wrong; the short answers they report are what gets scored, one claim each.
"""
from __future__ import annotations

import json
import re
from typing import Dict, List, Optional, Sequence, Tuple

GROUNDED_SYSTEM = """You are a voice assistant answering a question while a search is still running. Write what to say aloud next.

Rules:
- State every fact listed under "Say" in natural speech, with each value written exactly as given. Add nothing else, not even from your own knowledge.
- Say only those facts: nothing about what is left to do.
- Do not greet, read out these headings, or use lists. Keep it under 20 words in total.
Reply with JSON only."""

FREE_SYSTEM = """You are a voice assistant answering a question. Using the evidence you have so far, give your best answer now in one or two short spoken sentences, without lists.
Also list the answer alone in as few words as possible, for example a name, a date, "yes" or "no". List only what the question asks for, one item per thing asked, never supporting details: "Who was born later, A or B?" has one answer, the name; "When did X start and end?" has two.
Reply with JSON only."""

GROUNDED_SCHEMA = {"type": "object", "properties": {"text": {"type": "string"}}, "required": ["text"]}
FREE_SCHEMA = {"type": "object", "properties": {"text": {"type": "string"},
                                                "answers": {"type": "array", "items": {"type": "string"}}},
               "required": ["text", "answers"]}
MAX_SPOKEN_WORDS = 40  # past the 25 asked for: the model is reading out more than the facts


def find_value(text: str, value: Optional[str]) -> int:
    """Position of the value in the text as whole words, or -1, so "no" is not found in "know"."""
    if not value:
        return -1
    m = re.search(rf"(?<!\w){re.escape(value)}(?!\w)", text, re.IGNORECASE)
    return m.start() if m else -1


def adds_terms(text: str, request: str) -> bool:
    """Numbers, or capitalised words past a sentence start, that the request does not contain: facts nobody judged."""
    known = {w.lower() for w in re.findall(r"[\w'-]+", request)}
    terms = re.findall(r"(?<![.!?]\s)(?<!^)\b[A-Z][\w'-]*|\b\d+(?:,\d+)*\b", text)
    return any(t.lower() not in known and t.lower().removesuffix("'s") not in known for t in terms)


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

    def __init__(self, client):
        self.client = client
        self._cache: Dict[str, tuple] = {}
        self.fallbacks = 0
        self.log: List[dict] = []

    def _call(self, messages: List[dict], schema: dict) -> Tuple[dict, float]:
        key = json.dumps(messages, sort_keys=True)
        if key not in self._cache:
            n_calls = len(self.client.calls)
            try:
                raw = self.client.chat_json(messages, purpose="generate", schema=schema)
            except (ValueError, OSError):
                raw = {}
            latency = sum(c.latency_s for c in self.client.calls[n_calls:])
            self._cache[key] = (raw, latency)
            self.log.append({"request": messages[-1]["content"], "reply": raw, "latency_s": round(latency, 3)})
        return self._cache[key]

    def grounded(self, question: str, say: Sequence[Tuple[str, str]], missing: Sequence[str],
                 search_finished: bool) -> Tuple[str, float]:
        """say: (description, value). Returns (text, latency). The tail is fixed: the model's own ran as long
        as the facts and kept the Final Answer waiting, and it said "still checking" when nothing was."""
        tail = "I could not confirm the rest." if search_finished else "I'm still checking the rest."
        if not say:
            return (tail if missing else "That's all I found."), 0.0
        facts = "\n".join(f"- {d}: {v}" for d, v in say)
        request = f"Question: {question}\n\nSay:\n{facts}"
        raw, latency = self._call([{"role": "system", "content": GROUNDED_SYSTEM}, {"role": "user", "content": request}],
                                  GROUNDED_SCHEMA)
        text = raw.get("text") if isinstance(raw.get("text"), str) else None
        if not (text and len(text.split()) <= MAX_SPOKEN_WORDS and all(find_value(text, v) >= 0 for _, v in say if v)
                and "still checking" not in text.lower() and not adds_terms(text, request)):
            self.fallbacks += 1
            text = " ".join(f"{d}: {v}." for d, v in say)
        return f"{text} {tail}" if missing else text, latency

    def free(self, question: str, evidence: Sequence[Tuple[Optional[str], str]]) -> Tuple[str, List[str], float]:
        """Returns (text, answers, latency). An unusable or abstaining reply has no answers, so it claims nothing."""
        request = f"Question: {question}\n\nEvidence so far:\n{_evidence_lines(evidence)}"
        raw, latency = self._call([{"role": "system", "content": FREE_SYSTEM}, {"role": "user", "content": request}],
                                  FREE_SCHEMA)
        text = raw.get("text") if isinstance(raw.get("text"), str) else None
        answers = raw.get("answers") if isinstance(raw.get("answers"), list) else []
        return text or "I'm not sure.", [a for a in answers if isinstance(a, str) and not _is_abstention(a)], latency
