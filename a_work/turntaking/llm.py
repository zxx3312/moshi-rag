"""Minimal client for an OpenAI-compatible chat endpoint (vLLM, or a hosted API).

Stdlib only. Every call is timed so judge latency can be reported and charged to the clock.
"""
from __future__ import annotations

import json
import re
import time
import urllib.request
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class CallRecord:
    purpose: str
    latency_s: float
    prompt_tokens: Optional[int]
    completion_tokens: Optional[int]


@dataclass
class ChatClient:
    base_url: str  # e.g. http://127.0.0.1:8000/v1
    model: str
    timeout_s: float = 120.0
    api_key: str = "EMPTY"
    extra_body: Dict[str, Any] = field(default_factory=dict)  # e.g. vLLM chat_template_kwargs
    calls: List[CallRecord] = field(default_factory=list)

    def chat_json(self, messages: List[dict], *, purpose: str, schema: Optional[dict] = None,
                  max_tokens: int = 1024) -> dict:
        """Send a chat request and parse the reply as one JSON object."""
        body = {"model": self.model, "messages": messages, "temperature": 0.0, "max_tokens": max_tokens,
                **self.extra_body}
        if schema is not None:
            body["response_format"] = {"type": "json_schema", "json_schema": {"name": purpose, "schema": schema}}
        req = urllib.request.Request(
            self.base_url.rstrip("/") + "/chat/completions",
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {self.api_key}"},
        )
        t0 = time.monotonic()
        with urllib.request.urlopen(req, timeout=self.timeout_s) as resp:
            reply = json.loads(resp.read().decode("utf-8"))
        usage = reply.get("usage") or {}
        self.calls.append(CallRecord(purpose, time.monotonic() - t0,
                                     usage.get("prompt_tokens"), usage.get("completion_tokens")))
        return parse_json_object(reply["choices"][0]["message"]["content"])


def parse_json_object(text: str) -> dict:
    """Parse a JSON object, tolerating code fences, <think> blocks and surrounding prose."""
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.S).strip()
    try:
        obj = json.loads(text)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start < 0 or end <= start:
            raise ValueError(f"no JSON object in model reply: {text[:200]!r}")
        obj = json.loads(text[start:end + 1])
    if not isinstance(obj, dict):
        raise ValueError(f"expected a JSON object, got {type(obj).__name__}")
    return obj


class FakeClient:
    """Test double: answers each call with the next scripted reply (dict or callable(messages) -> dict)."""

    def __init__(self, replies: List[Any]):
        self.replies = list(replies)
        self.calls: List[CallRecord] = []
        self.messages: List[List[dict]] = []

    def chat_json(self, messages, *, purpose, schema=None, max_tokens=1024) -> dict:
        self.messages.append(messages)
        self.calls.append(CallRecord(purpose, 0.0, None, None))
        reply = self.replies.pop(0)
        return reply(messages) if callable(reply) else reply

