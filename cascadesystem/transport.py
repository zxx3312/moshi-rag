"""Bounded standard-library HTTP. Authenticated requests never follow redirects."""
import json
from urllib import error, request
from urllib.parse import urlsplit


class ProviderError(RuntimeError):
    pass


class NoRedirect(request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class HTTP:
    def __init__(self, timeout_s=45.0):
        self.timeout_s = timeout_s

    def read(self, url, *, body=None, headers=None, max_bytes=2_000_000):
        data = json.dumps(body, ensure_ascii=False).encode("utf-8") if body is not None else None
        req = request.Request(url, data=data, headers=headers or {})
        try:
            opener = request.build_opener(NoRedirect())
            with opener.open(req, timeout=self.timeout_s) as response:
                result = response.read(max_bytes + 1)
            if len(result) > max_bytes:
                raise ProviderError("Provider response exceeded the size limit")
            return result
        except error.HTTPError as exc:
            # Do not expose response bodies, request headers or credentials.
            raise ProviderError(f"HTTP {exc.code} from {urlsplit(url).hostname}") from None
        except (error.URLError, TimeoutError, OSError):
            raise ProviderError(f"Connection failed or timed out: {urlsplit(url).hostname}") from None

    def json(self, url, *, body=None, headers=None):
        combined = {"Accept": "application/json", **(headers or {})}
        if body is not None:
            combined["Content-Type"] = "application/json"
        try:
            value = json.loads(self.read(url, body=body, headers=combined))
        except (ValueError, UnicodeError):
            raise ProviderError("Provider returned invalid JSON") from None
        if not isinstance(value, dict):
            raise ProviderError("Provider JSON must be an object")
        return value
