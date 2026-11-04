"""Write what the agent says: the LLM step of the cascade (controller -> LLM -> TTS).

Evidence-aware actions get only the units the judge supported, with their values and evidence, plus what
is still missing, so a Partial Answer cannot be asked to state more. Rule baselines get all visible
evidence and give their best answer, so they can be wrong; the short answer they report is what gets scored.
"""
from __future__ import annotations

import json
from typing import Dict, List, Optional, Sequence, Tuple

GROUNDED_SYSTEM = """You are a voice assistant answering a question while a search is still running. Write what to say aloud next.

Rules:
- State only the facts listed under "Say", using their exact values. Add nothing else, not even from your own knowledge.
- If anything is listed under "Still missing", end by saying briefly what you are still checking. Do not guess it.
- If "Search finished" is yes and something is still missing, say you could not confirm it.
- Do not repeat what you already said. Do not greet or use lists. One or two short spoken sentences.
Reply with JSON only."""

FREE_SYSTEM = """You are a voice assistant answering a question. Using the evidence you have so far, give your best answer now in one or two short spoken sentences, without lists.
Also report the answer alone in as few words as possible, for example a name, a date, "yes" or "no".
Reply with JSON only."""

GROUNDED_SCHEMA = {"type": "object", "properties": {"text": {"type": "string"}}, "required": ["text"]}
FREE_SCHEMA = {"type": "object", "properties": {"text": {"type": "string"}, "answer": {"type": "string"}},
               "required": ["text", "answer"]}


def _evidence_lines(evidence: Sequence[Tuple[Optional[str], str]]) -> str:
    return "\n".join(f"({title}) {text}" if title else text for title, text in evidence) or "(none)"


class Generator:
    """Results are cached, and the real call's latency is reported again on a cache hit: another
    delay schedule would have waited for that call too."""

    def __init__(self, client):
        self.client = client
        self._cache: Dict[str, tuple] = {}
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

    def grounded(self, question: str, say: Sequence[Tuple[str, str, Sequence]], missing: Sequence[str],
                 said: Sequence[str], search_finished: bool) -> Tuple[str, float]:
        """say: (description, value, [(title, text), ...]). Returns (text, latency); falls back to the plain facts."""
        facts = "\n".join(f"- {d}: {v}\n  Evidence: {_evidence_lines(e)}" for d, v, e in say) or "(nothing new)"
        request = (f"Question: {question}\n\nSay:\n{facts}\n\n"
                   f"Still missing:\n" + ("\n".join(f"- {m}" for m in missing) or "(nothing)") + "\n\n"
                   f"Search finished: {'yes' if search_finished else 'no'}\n\n"
                   f"Already said: {' '.join(said) or '(nothing)'}")
        raw, latency = self._call([{"role": "system", "content": GROUNDED_SYSTEM}, {"role": "user", "content": request}],
                                  GROUNDED_SCHEMA)
        text = raw.get("text") if isinstance(raw.get("text"), str) else None
        return (text or " ".join(f"{d}: {v}." for d, v, _ in say) or "I could not confirm that."), latency

    def free(self, question: str, evidence: Sequence[Tuple[Optional[str], str]]) -> Tuple[str, Optional[str], float]:
        """Returns (text, short answer, latency). An unusable reply counts as no answer."""
        request = f"Question: {question}\n\nEvidence so far:\n{_evidence_lines(evidence)}"
        raw, latency = self._call([{"role": "system", "content": FREE_SYSTEM}, {"role": "user", "content": request}],
                                  FREE_SCHEMA)
        text = raw.get("text") if isinstance(raw.get("text"), str) else None
        answer = raw.get("answer") if isinstance(raw.get("answer"), str) else None
        return text or "I'm not sure.", answer, latency
