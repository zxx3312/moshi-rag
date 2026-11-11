"""Minimal client for an OpenAI-compatible chat endpoint (vLLM, or a hosted API).

Stdlib only. Every call is timed so judge latency can be reported and charged to the clock.

Every call is also kept on a tape (reply and latency, keyed by the request). A client given a tape answers
from it instead of the network, so a GPU run can be replayed on a login node with other timing settings.
"""
from __future__ import annotations

import hashlib
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


class TapeMiss(RuntimeError):
    """The tape has no reply for this request: the replayed run asks something the recorded run never did."""


def load_tape(paths) -> Dict[str, dict]:
    tape = {}
    for path in paths:
        with open(path, encoding="utf-8") as f:
            tape.update((row["key"], row) for row in map(json.loads, f) if "key" in row)
    return tape


@dataclass
class ChatClient:
    base_url: str  # e.g. http://127.0.0.1:8000/v1
    model: str
    timeout_s: float = 120.0
    api_key: str = "EMPTY"
    extra_body: Dict[str, Any] = field(default_factory=dict)  # e.g. vLLM chat_template_kwargs
    max_tokens: int = 1024  # raise for thinking mode: the reasoning counts against it
    calls: List[CallRecord] = field(default_factory=list)
    tape: List[dict] = field(default_factory=list)  # every call made, for load_tape
    replay: Optional[Dict[str, dict]] = None  # answer from this tape and never use the network
    allow_misses: bool = False  # a request the tape lacks counts as an unusable reply instead of stopping the run
    misses: int = 0

    def _from_tape(self, key: str, purpose: str) -> dict:
        row = self.replay.get(key)
        if row is None:
            self.misses += 1
            if self.allow_misses:
                raise ValueError(f"no recorded reply for this {purpose} request")
            raise TapeMiss(f"no recorded reply for this {purpose} request to {self.model}")
        self.calls.append(CallRecord(purpose, row["latency_s"], None, None))
        self.tape.append(row)
        if "error" in row:
            raise ValueError(row["error"])
        return row["reply"]

    def chat_json(self, messages: List[dict], *, purpose: str, schema: Optional[dict] = None,
                  max_tokens: Optional[int] = None) -> dict:
        """Send a chat request and parse the reply as one JSON object."""
        key = hashlib.sha1(json.dumps([self.model, messages, schema, self.extra_body], sort_keys=True)
                           .encode("utf-8")).hexdigest()
        if self.replay is not None:
            return self._from_tape(key, purpose)
        body = {"model": self.model, "messages": messages, "temperature": 0.0,
                "max_tokens": max_tokens or self.max_tokens,
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
        row = {"key": key, "purpose": purpose, "model": self.model, "latency_s": round(self.calls[-1].latency_s, 4)}
        self.tape.append(row)
        try:
            row["reply"] = parse_json_object(reply["choices"][0]["message"]["content"])
        except ValueError as e:
            row["error"] = str(e)
            raise
        return row["reply"]


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
        self.tape: List[dict] = []
        self.misses = 0

    def chat_json(self, messages, *, purpose, schema=None, max_tokens=None) -> dict:
        self.messages.append(messages)
        self.calls.append(CallRecord(purpose, 0.0, None, None))
        reply = self.replies.pop(0)
        return reply(messages) if callable(reply) else reply

