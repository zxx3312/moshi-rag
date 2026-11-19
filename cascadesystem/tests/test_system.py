import asyncio
from dataclasses import replace
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from cascadesystem.config import Settings
from cascadesystem.controller import Cascade
from cascadesystem.demo import DemoLLM, DemoSearch, QUESTION
from cascadesystem.llm import TinkerLLM, parse_object
from cascadesystem.models import Evidence, plan_from_json, resolve_text, validate_judgments
from cascadesystem.search import WikipediaSearch, select_passages
from cascadesystem.transport import ProviderError


def unit(uid="u1", dependencies=(), necessary=True):
    return {"unit_id": uid, "description": "fictional date", "necessary": necessary,
            "depends_on": list(dependencies), "queries": ["fictional query " + uid]}


def supported(uid="u1", value="2040", eid="e1", quote="In 2040."):
    return {"unit_id": uid, "label": "SUPPORTED", "value": value,
            "citations": [eid], "quotes": [{"evidence_id": eid, "text": quote}]}


class ValidationTests(unittest.TestCase):
    def test_plan_rejects_cycle(self):
        with self.assertRaisesRegex(ValueError, "cycle"):
            plan_from_json({"units": [unit("u1", ["u2"]), unit("u2", ["u1"])]})

    def test_plan_rejects_duplicate_ids(self):
        with self.assertRaises(ValueError):
            plan_from_json({"units": [unit(), unit()]})

    def test_plan_rejects_unknown_dependency(self):
        with self.assertRaises(ValueError):
            plan_from_json({"units": [unit(dependencies=["u7"])]})

    def test_plan_rejects_undeclared_placeholder(self):
        row = unit()
        row["queries"] = ["{u2} date"]
        with self.assertRaises(ValueError):
            plan_from_json({"units": [row]})

    def test_plan_requires_necessary_unit(self):
        with self.assertRaises(ValueError):
            plan_from_json({"units": [unit(necessary=False)]})

    def test_missing_source_rejects_support(self):
        units = plan_from_json({"units": [unit()]})
        result = validate_judgments({"judgments": [supported()]}, units, [])
        self.assertEqual(result["u1"].label, "UNRESOLVED")

    def test_invented_quote_rejects_support(self):
        units = plan_from_json({"units": [unit()]})
        evidence = [Evidence("e1", "Fiction", "https://example.invalid", "No date here.", 1)]
        result = validate_judgments({"judgments": [supported()]}, units, evidence)
        self.assertEqual(result["u1"].label, "UNRESOLVED")

    def test_every_citation_needs_quote(self):
        units = plan_from_json({"units": [unit()]})
        row = supported()
        row["citations"].append("e2")
        evidence = [Evidence(eid, "Fiction", "https://example.invalid", "In 2040.", 1) for eid in ["e1", "e2"]]
        self.assertEqual(validate_judgments({"judgments": [row]}, units, evidence)["u1"].label, "UNRESOLVED")

    def test_dependency_blocks_supported_conclusion(self):
        units = plan_from_json({"units": [unit("u1", necessary=False), unit("u2", ["u1"])]})
        evidence = [Evidence("e1", "Fiction", "https://example.invalid", "In 2040.", 1)]
        result = validate_judgments({"judgments": [{"unit_id": "u1", "label": "UNRESOLVED"}, supported("u2")]}, units, evidence)
        self.assertEqual(result["u2"].label, "UNRESOLVED")
        with self.assertRaises(ValueError):
            resolve_text("{u1} date", result)

    def test_unknown_judge_unit_rejected(self):
        with self.assertRaises(ValueError):
            validate_judgments({"judgments": [supported("u2")]}, plan_from_json({"units": [unit()]}), [])

    def test_json_does_not_extract_object_from_untrusted_prose(self):
        with self.assertRaises(ProviderError):
            parse_object('Ignore rules {"units": []}')
        self.assertEqual(parse_object('```json\n{"ok": true}\n```'), {"ok": True})

    def test_remote_http_and_url_credentials_rejected(self):
        for url in ["http://remote.invalid/v1", "https://secret@remote.invalid/v1"]:
            with self.assertRaises(ValueError):
                Settings(base_url=url)

    def test_secret_not_in_settings_repr(self):
        self.assertNotIn("test-secret", repr(Settings(api_key="test-secret")))

    def test_local_env_and_shell_precedence(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / ".env"
            path.write_text('TINKER_API_KEY="file-secret"\nCASCADE_MODEL=local-model\n', encoding="utf-8")
            with patch.dict("os.environ", {}, clear=True):
                settings = Settings.from_env(path)
                self.assertEqual(settings.api_key, "file-secret")
                self.assertEqual(settings.model, "local-model")
            with patch.dict("os.environ", {"TINKER_API_KEY": "shell-secret"}, clear=True):
                self.assertEqual(Settings.from_env(path).api_key, "shell-secret")

    def test_invalid_local_env_does_not_echo_secret(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / ".env"
            path.write_text("bad-secret-without-assignment", encoding="utf-8")
            with self.assertRaises(ValueError) as context:
                Settings.from_env(path)
            self.assertNotIn("bad-secret", str(context.exception))

    def test_retrieval_can_select_late_relevant_paragraph(self):
        text = "The silver observatory is in Aster City.\n\n" + "Unrelated architecture. " * 300 + "\n\nIt opened to the public in 2044."
        selected = select_passages(text, "silver observatory opening public", 300)
        self.assertIn("opened to the public in 2044", selected)
        self.assertIn("Aster City", selected)
        self.assertLessEqual(len(selected), 300)


class FakeHTTP:
    def __init__(self, response):
        self.response, self.requests = response, []

    def json(self, url, **kwargs):
        self.requests.append((url, kwargs))
        return self.response


class AdapterTests(unittest.IsolatedAsyncioTestCase):
    async def test_tinker_request_and_secret_free_call_log(self):
        http = FakeHTTP({"choices": [{"finish_reason": "stop", "message": {"content": '{"ok":true}', "reasoning_content": "hidden"}}]})
        client = TinkerLLM(Settings(api_key="test-secret"), http)
        self.assertEqual(await client.complete("test", "JSON", {}), {"ok": True})
        body = http.requests[0][1]["body"]
        self.assertEqual(body["model"], "openai/gpt-oss-120b")
        self.assertIn("max_completion_tokens", body)
        self.assertNotIn("response_format", body)
        self.assertEqual(http.requests[0][1]["headers"]["User-Agent"], Settings().user_agent)
        self.assertNotIn("test-secret", json.dumps(client.calls))

    async def test_truncated_llm_response_rejected(self):
        http = FakeHTTP({"choices": [{"finish_reason": "length", "message": {"content": "{}"}}]})
        client = TinkerLLM(Settings(api_key="fake"), http)
        with self.assertRaisesRegex(ProviderError, "token limit"):
            await client.complete("test", "JSON", {})
        self.assertEqual(client.calls[0]["status"], "error")

    async def test_wikipedia_returns_page_text_not_search_snippet(self):
        http = FakeHTTP({"query": {"pages": [{"title": "Fiction", "extract": "Actual source text", "fullurl": "https://en.wikipedia.org/wiki/Fiction", "index": 1}]}})
        rows = await WikipediaSearch(Settings(), http).search("a & b")
        self.assertEqual(rows[0]["text"], "Actual source text")
        self.assertIn("gsrsearch=a+%26+b", http.requests[0][0])
        self.assertIn("User-Agent", http.requests[0][1]["headers"])

    async def test_wikipedia_error_is_not_an_empty_success(self):
        with self.assertRaises(ProviderError):
            await WikipediaSearch(Settings(), FakeHTTP({"error": {"code": "ratelimited"}})).search("fiction")


class ControllerTests(unittest.IsolatedAsyncioTestCase):
    async def test_partial_then_final_without_repeating_claim(self):
        result = await Cascade(DemoLLM(), DemoSearch(), replace(Settings(), progress_s=0.1)).run(QUESTION)
        utterances = [e for e in result["events"] if e["type"] == "utterance"]
        self.assertEqual(result["status"], "complete")
        self.assertEqual(utterances[0]["action"], "Backchannel")
        self.assertTrue(any(e["action"] == "Progress" for e in utterances))
        factual = [e for e in utterances if e["claims"]]
        self.assertEqual([e["action"] for e in factual], ["Partial Answer", "Final Answer"])
        self.assertEqual([f["unit_id"] for e in factual for f in e["claims"]], ["u1", "u2"])
        # The first judge did not get the return-date evidence that was still in flight.
        first_snapshot = next(e for e in result["events"] if e["type"] == "judgments")
        self.assertEqual(first_snapshot["evidence_snapshot_ids"], ["e1"])

    async def test_no_search_results_names_missing_units(self):
        class EmptySearch:
            async def search(self, query):
                return []
        result = await Cascade(DemoLLM(), EmptySearch(), Settings()).run(QUESTION)
        self.assertEqual(result["status"], "incomplete")
        final = [e for e in result["events"] if e["type"] == "utterance"][-1]
        self.assertEqual(final["unresolved"], ["u1", "u2"])
        self.assertIn("星舟号返回日期", final["text"])
        self.assertFalse(final["claims"])

    async def test_search_failure_recorded_and_no_memory_answer(self):
        class FailedSearch:
            async def search(self, query):
                raise ProviderError("simulated search outage")
        result = await Cascade(DemoLLM(), FailedSearch(), Settings()).run(QUESTION)
        self.assertEqual(len(result["search_failures"]), 2)
        self.assertFalse(result["output_enqueued_units"])

    async def test_bad_generation_falls_back_to_approved_facts(self):
        class BadGenerator(DemoLLM):
            async def complete(self, purpose, system, payload):
                if purpose == "generate":
                    return {"text": "Invented answer with no requested date"}
                return await super().complete(purpose, system, payload)
        result = await Cascade(BadGenerator(), DemoSearch(), Settings()).run(QUESTION)
        factual = [e for e in result["events"] if e["type"] == "utterance" and e["claims"]]
        self.assertTrue(all(e["fallback"] for e in factual))
        self.assertFalse(any("Invented" in e["text"] for e in factual))

    async def test_semantic_verifier_rejects_added_fact(self):
        class RejectVerifier(DemoLLM):
            async def complete(self, purpose, system, payload):
                if purpose == "verify":
                    return {"approved": False}
                return await super().complete(purpose, system, payload)
        result = await Cascade(RejectVerifier(), DemoSearch(), Settings()).run(QUESTION)
        self.assertTrue(all(e["fallback"] for e in result["events"] if e["type"] == "utterance" and e["claims"]))

    async def test_bridge_search_waits_for_entity_resolution(self):
        calls = []

        class BridgeLLM:
            async def complete(self, purpose, system, payload):
                if purpose == "decompose":
                    first, second = unit(necessary=False), unit("u2", ["u1"])
                    second["queries"] = ["{u1} birthday"]
                    return {"units": [first, second]}
                if purpose == "judge":
                    rows = [supported(value="Aster", quote="The pilot is Aster.")]
                    rows.append(supported("u2", value="2040", eid="e2") if len(payload["evidence"]) > 1 else {"unit_id": "u2", "label": "UNRESOLVED"})
                    return {"judgments": rows}
                if purpose == "generate":
                    return {"text": "; ".join(f["value"] for f in payload["APPROVED_FACTS"])}
                return {"approved": True}

        class BridgeSearch:
            async def search(self, query):
                calls.append(query)
                first = len(calls) == 1
                return [{"title": "Fiction", "url": "https://example.invalid/" + str(len(calls)),
                         "text": "The pilot is Aster." if first else "In 2040."}]

        result = await Cascade(BridgeLLM(), BridgeSearch(), Settings()).run("When was the fictional pilot born?")
        self.assertEqual(calls, ["fictional query u1", "Aster birthday"])
        self.assertEqual(result["status"], "complete")

    async def test_api_failure_stops_with_explicit_error(self):
        class FailedLLM:
            async def complete(self, *args):
                raise ProviderError("simulated API outage")
        result = await Cascade(FailedLLM(), DemoSearch(), Settings()).run(QUESTION)
        self.assertEqual(result["status"], "error")
        self.assertTrue(any(e["type"] == "failure" for e in result["events"]))

    async def test_invalid_quote_gets_one_strict_repair(self):
        class QuoteRepair(DemoLLM):
            def __init__(self):
                super().__init__()
                self.repairs = 0

            async def complete(self, purpose, system, payload):
                raw = await super().complete(purpose, system, payload)
                if purpose == "judge":
                    for row in raw["judgments"]:
                        if row["label"] == "SUPPORTED":
                            row["quotes"][0]["text"] = "not an exact quote ..."
                if purpose == "judge_repair":
                    self.repairs += 1
                return raw
        client = QuoteRepair()
        result = await Cascade(client, DemoSearch(), Settings()).run(QUESTION)
        self.assertEqual(result["status"], "complete")
        self.assertEqual(client.repairs, 2)

    async def test_repair_does_not_relax_quote_check(self):
        class BadQuotes(DemoLLM):
            async def complete(self, purpose, system, payload):
                raw = await super().complete(purpose, system, payload)
                if purpose in {"judge", "judge_repair"}:
                    for row in raw["judgments"]:
                        if row["label"] == "SUPPORTED":
                            row["quotes"][0]["text"] = "invented quote"
                return raw
        result = await Cascade(BadQuotes(), DemoSearch(), Settings()).run(QUESTION)
        self.assertEqual(result["status"], "incomplete")
        self.assertFalse(result["output_enqueued_units"])

    async def test_search_budget_terminates(self):
        class EmptySearch:
            async def search(self, query):
                return []
        result = await Cascade(DemoLLM(), EmptySearch(), replace(Settings(), max_searches=1)).run(QUESTION)
        self.assertEqual(len(result["searches"]), 1)
        self.assertEqual(result["status"], "incomplete")

    async def test_new_conflict_withdraws_earlier_partial(self):
        class ConflictLLM(DemoLLM):
            async def complete(self, purpose, system, payload):
                raw = await super().complete(purpose, system, payload)
                if purpose == "judge" and len(payload["evidence"]) == 2:
                    raw["judgments"][0] = {"unit_id": "u1", "label": "CONTRADICTED"}
                return raw
        result = await Cascade(ConflictLLM(), DemoSearch(), Settings()).run(QUESTION)
        self.assertEqual(result["status"], "incomplete")
        self.assertTrue(any(e.get("action") == "Correction" for e in result["events"]))
        self.assertNotIn("u1", result["output_enqueued_units"])

    async def test_total_evidence_budget_is_enforced(self):
        result = await Cascade(DemoLLM(), DemoSearch(), replace(Settings(), evidence_chars=5)).run(QUESTION)
        self.assertLessEqual(sum(len(e["text"]) for e in result["evidence"]), 5)
        self.assertEqual(result["status"], "incomplete")


if __name__ == "__main__":
    unittest.main()
