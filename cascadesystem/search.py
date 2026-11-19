"""Replaceable async search protocol and keyless Wikipedia retrieval."""
import asyncio
from collections import Counter
import re
from typing import Protocol
from urllib.parse import urlencode

from .transport import HTTP, ProviderError
from .models import title_conflicts_with_subject


class SearchProvider(Protocol):
    async def search(self, query: str) -> list[dict]:
        """Return title, url and actual source text; not an LLM-generated answer."""
        ...


def select_passages(text, query, budget):
    """Keep source wording, page identity and query-relevant paragraphs, including late sections."""
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    if not paragraphs:
        return ""

    def tokens(value):
        words = re.findall(r"[^\W_]+", value.casefold(), flags=re.UNICODE)
        return {re.sub(r"(?:ing|ed|s)$", "", w) if len(w) > 4 else w for w in words if len(w) > 2}

    terms = tokens(query) - {"the", "and", "what", "which", "when", "where", "did", "was", "were"}
    paragraph_terms = [tokens(p) for p in paragraphs]
    frequency = Counter(t for ts in paragraph_terms for t in ts)
    ranked = sorted(range(1, len(paragraphs)),
                    key=lambda i: (-sum(1 / frequency[t] for t in terms & paragraph_terms[i]), i))
    # Always preserve the lead to disambiguate the subject. Additional passages stay in page order.
    selected = {0: paragraphs[0][:min(1000, budget)]}
    remaining = budget - len(selected[0])
    for index in ranked:
        if remaining <= 2:
            break
        if not (terms & paragraph_terms[index]):
            continue
        passage = paragraphs[index][:min(1800, remaining - 2)]
        selected[index] = passage
        remaining -= len(passage) + 2
    return "\n\n".join(selected[i] for i in sorted(selected))[:budget]


class WikipediaSearch:
    def __init__(self, settings, http=None):
        self.settings = settings
        self.http = http or HTTP(settings.timeout_s)
        self.semaphore = asyncio.Semaphore(settings.concurrency)
        self.title_cache = {}
        self.diagnostics = []

    async def _request(self, parameters):
        params = {"action": "query", "format": "json", "formatversion": "2",
                  "prop": "extracts|info|pageprops", "ppprop": "disambiguation",
                  "explaintext": "1", "exlimit": str(self.settings.search_limit), "inprop": "url",
                  **parameters}
        url = f"https://{self.settings.wiki_language}.wikipedia.org/w/api.php?" + urlencode(params)
        async with self.semaphore:
            raw = await asyncio.to_thread(self.http.json, url, headers={"User-Agent": self.settings.user_agent})
        if "error" in raw:
            raise ProviderError("Wikipedia rejected the search request")
        pages = raw.get("query", {}).get("pages", [])
        if not isinstance(pages, list):
            raise ProviderError("Unexpected Wikipedia response")
        return sorted(pages, key=lambda p: p.get("index", 0))

    async def search(self, query):
        return await self.search_subject(query, "")

    async def search_subject(self, query, subject):
        """Resolve the entity separately from relation keywords; retain search for supplementary text."""
        diagnostic = {"query": query, "subject": subject, "title_lookup": "not_requested"}
        primary = []
        if subject:
            try:
                if subject not in self.title_cache:
                    self.title_cache[subject] = await self._request({"titles": subject, "redirects": "1"})
                primary = [p for p in self.title_cache[subject] if not p.get("missing") and not p.get("invalid")]
                diagnostic["title_lookup"] = "resolved" if primary else "missing"
            except ProviderError as exc:
                diagnostic.update(title_lookup="error", title_error=str(exc))
        candidates = await self._request({"generator": "search", "gsrsearch": query,
                                          "gsrnamespace": "0", "gsrlimit": str(self.settings.search_limit)})
        canonical = primary[0].get("title", "") if primary else ""
        ambiguous = bool(primary and "disambiguation" in primary[0].get("pageprops", {}))
        if ambiguous:
            diagnostic["title_lookup"] = "ambiguous"
            primary = []
        diagnostic.update(resolved_title=canonical, candidate_titles=[p.get("title") for p in candidates], excluded_titles=[])
        found = []
        seen = set()
        for page in primary + candidates:
            title, text, source_url = page.get("title"), page.get("extract"), page.get("fullurl")
            if isinstance(title, str) and isinstance(text, str) and text.strip() and isinstance(source_url, str):
                if source_url in seen:
                    continue
                if subject and not ambiguous and title_conflicts_with_subject(title, canonical or subject):
                    diagnostic["excluded_titles"].append(title)
                    continue
                seen.add(source_url)
                found.append({"title": title, "text": select_passages(text, query, self.settings.source_chars), "url": source_url,
                              "requested_subject": subject, "resolved_title": canonical,
                              "entity_resolution": "ambiguous" if ambiguous else "primary" if primary and title == canonical else "search"})
        diagnostic["returned_titles"] = [p["title"] for p in found]
        self.diagnostics.append(diagnostic)
        return found
