"""Environment configuration; secrets never enter run manifests."""
from dataclasses import dataclass, field
import math
import os
from pathlib import Path
from urllib.parse import urlsplit


def local_environment(path=None):
    """Load only known settings; environment variables override the ignored local file."""
    path = Path(path) if path is not None else Path(__file__).with_name(".env")
    values = {}
    allowed = {"TINKER_API_KEY", "CASCADE_LLM_API_KEY", "CASCADE_BASE_URL", "CASCADE_MODEL",
               "CASCADE_TIMEOUT_S", "CASCADE_MAX_TOKENS", "CASCADE_REASONING_EFFORT",
               "CASCADE_WIKI_LANGUAGE", "CASCADE_USER_AGENT", "CASCADE_PROGRESS_S", "CASCADE_FEEDBACK_TIMEOUT_S",
               "CASCADE_JUDGE_MODEL", "CASCADE_JUDGE_REASONING_EFFORT"}
    if path.is_file():
        if path.stat().st_size > 16_384:
            raise ValueError("Local .env is unexpectedly large")
        for number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, separator, value = line.partition("=")
            key, value = key.strip(), value.strip()
            if not separator or key not in allowed:
                raise ValueError(f"Invalid setting at .env line {number}; use KEY=value")
            if value[:1] in {"'", '"'}:
                if len(value) < 2 or value[-1] != value[0]:
                    raise ValueError(f"Unclosed quote at .env line {number}")
                value = value[1:-1]
            values[key] = value
    return {**values, **os.environ}


@dataclass(frozen=True)
class Settings:
    base_url: str = "https://tinker.thinkingmachines.dev/services/tinker-prod/oai/api/v1"
    model: str = "openai/gpt-oss-120b"
    judge_model: str = ""
    judge_reasoning_effort: str = "low"
    api_key: str = field(default="", repr=False)
    timeout_s: float = 45.0
    max_tokens: int = 4096
    reasoning_effort: str = "low"
    wiki_language: str = "en"
    user_agent: str = "CascadeSystem/0.1 (educational research prototype)"
    search_limit: int = 3
    max_units: int = 8
    max_searches: int = 16
    max_sources: int = 24
    source_chars: int = 5000
    evidence_chars: int = 30_000
    progress_s: float = 3.0
    feedback_timeout_s: float = 6.0
    concurrency: int = 3

    def __post_init__(self):
        parsed = urlsplit(self.base_url)
        if parsed.scheme not in {"http", "https"} or not parsed.hostname or parsed.username or parsed.password or parsed.query or parsed.fragment:
            raise ValueError("CASCADE_BASE_URL must be an HTTP(S) API base URL without credentials or query")
        if parsed.scheme == "http" and parsed.hostname not in {"localhost", "127.0.0.1", "::1"}:
            raise ValueError("Use HTTPS for a remote LLM endpoint")
        if not self.wiki_language.isalpha() or not 2 <= len(self.wiki_language) <= 12:
            raise ValueError("CASCADE_WIKI_LANGUAGE must be a Wikipedia language code")
        if not isinstance(self.judge_model, str) or len(self.judge_model) > 500 or any(c in self.judge_model for c in '\r\n'):
            raise ValueError('Invalid CASCADE_JUDGE_MODEL')
        for name in ("timeout_s", "progress_s", "feedback_timeout_s"):
            value = getattr(self, name)
            if not math.isfinite(value) or value <= 0:
                raise ValueError(name + " must be positive and finite")
        for name in ("max_tokens", "search_limit", "max_units", "max_searches", "max_sources", "source_chars", "evidence_chars", "concurrency"):
            if getattr(self, name) <= 0:
                raise ValueError(name + " must be positive")

    @classmethod
    def from_env(cls, env_file=None):
        env = local_environment(env_file)
        return cls(
            base_url=env.get("CASCADE_BASE_URL", cls.base_url).rstrip("/"),
            model=env.get("CASCADE_MODEL", cls.model),
            judge_model=env.get("CASCADE_JUDGE_MODEL", ""),
            judge_reasoning_effort=env.get("CASCADE_JUDGE_REASONING_EFFORT", "low"),
            api_key=env.get("TINKER_API_KEY", "") or env.get("CASCADE_LLM_API_KEY", ""),
            timeout_s=float(env.get("CASCADE_TIMEOUT_S", "45")),
            max_tokens=int(env.get("CASCADE_MAX_TOKENS", "4096")),
            reasoning_effort=env.get("CASCADE_REASONING_EFFORT", "low"),
            wiki_language=env.get("CASCADE_WIKI_LANGUAGE", "en"),
            user_agent=env.get("CASCADE_USER_AGENT", cls.user_agent),
            progress_s=float(env.get("CASCADE_PROGRESS_S", "3")),
            feedback_timeout_s=float(env.get("CASCADE_FEEDBACK_TIMEOUT_S", "6")),
        )
