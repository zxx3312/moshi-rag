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
- If "Still checking" lists anything, end with at most 8 words on what you are still checking. Do not guess it.
- If "Could not confirm" lists anything, end by saying you could not confirm it.
- Do not repeat anything under "Already said". Do not greet, read out these headings, or use lists. Keep it under 25 words in total.
Reply with JSON only."""

FREE_SYSTEM = """You are a voice assistant answering a question. Using the evidence you have so far, give your best answer now in one or two short spoken sentences, without lists.
Also list each answer alone in as few words as possible, one item per thing the question asks, for example a name, a date, "yes" or "no".
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
                 said: Sequence[str], search_finished: bool) -> Tuple[str, float]:
        """say: (description, value). Returns (text, latency)."""
        facts = "\n".join(f"- {d}: {v}" for d, v in say) or "(nothing new)"
        heading = "Could not confirm" if search_finished else "Still checking"
        pending = f"{heading}:\n" + "\n".join(f"- {m}" for m in missing) + "\n\n" if missing else ""
        request = (f"Question: {question}\n\nSay:\n{facts}\n\n{pending}"
                   f"Already said: {' '.join(said) or '(nothing)'}")
        raw, latency = self._call([{"role": "system", "content": GROUNDED_SYSTEM}, {"role": "user", "content": request}],
                                  GROUNDED_SCHEMA)
        text = raw.get("text") if isinstance(raw.get("text"), str) else None
        if text and len(text.split()) <= MAX_SPOKEN_WORDS and all(find_value(text, v) >= 0 for _, v in say if v):
            return text, latency
        self.fallbacks += 1
        plain = " ".join(f"{d}: {v}." for d, v in say)
        tail = "I could not confirm the rest." if search_finished else "I'm still checking the rest."
        return " ".join(p for p in (plain, tail if missing or not plain else "") if p), latency

    def free(self, question: str, evidence: Sequence[Tuple[Optional[str], str]]) -> Tuple[str, List[str], float]:
        """Returns (text, answers, latency). An unusable or abstaining reply has no answers, so it claims nothing."""
        request = f"Question: {question}\n\nEvidence so far:\n{_evidence_lines(evidence)}"
        raw, latency = self._call([{"role": "system", "content": FREE_SYSTEM}, {"role": "user", "content": request}],
                                  FREE_SCHEMA)
        text = raw.get("text") if isinstance(raw.get("text"), str) else None
        answers = raw.get("answers") if isinstance(raw.get("answers"), list) else []
        return text or "I'm not sure.", [a for a in answers if isinstance(a, str) and not _is_abstention(a)], latency
