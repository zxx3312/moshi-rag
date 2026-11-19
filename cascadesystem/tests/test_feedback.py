"""Dynamic feedback never consumes evidence/answers or invents execution progress."""
import asyncio
from dataclasses import replace
import unittest
from unittest.mock import patch

from cascadesystem.config import Settings
from cascadesystem.controller import Cascade
from cascadesystem.demo import DemoLLM, DemoSearch, QUESTION
from cascadesystem.feedback import FeedbackComposer
from cascadesystem.llm import TinkerLLM
from cascadesystem.transport import ProviderError


def state(**changes):
    return {"stage": "planning", "searches_started": 0, "searches_completed": 0,
            "active_searches": 0, "evidence_count": 0, "supported_units": 0, "output_units": 0, **changes}


class FeedbackLLM:
    def __init__(self, text="I'll look up the silver observatory's opening date.", claim="intent", safe=True):
        self.text, self.claim, self.safe = text, claim, safe
        self.requests = []

    async def complete_feedback(self, purpose, system, payload):
        self.requests.append((purpose, payload))
        if purpose == "feedback_generate":
            return {"text": self.text, "status_claim": self.claim}
        return {"safe": self.safe}


class FeedbackTests(unittest.IsolatedAsyncioTestCase):
    async def test_opening_is_question_specific_without_answers_or_evidence(self):
        llm = FeedbackLLM()
        result = await FeedbackComposer(llm, 1).compose("When did the silver observatory open?", "opening", "en", state)
        self.assertEqual(result.source, "model")
        self.assertIn("silver observatory", result.text)
        self.assertEqual([p for p, _ in llm.requests], ["feedback_generate", "feedback_verify"])
        self.assertNotIn("evidence", llm.requests[0][1])
        self.assertNotIn("APPROVED_FACTS", llm.requests[0][1])

    async def test_early_answer_is_not_spoken(self):
        llm = FeedbackLLM("The answer is Aster City.")
        result = await FeedbackComposer(llm, 1).compose("Where is the silver observatory?", "opening", "en", state)
        self.assertEqual(result.source, "fallback")
        self.assertNotIn("Aster", result.text)

    async def test_checking_cannot_be_claimed_before_evidence_arrives(self):
        llm = FeedbackLLM("I'm checking the sources.", "checking")
        result = await FeedbackComposer(llm, 1).compose("Where is it?", "progress", "en", state)
        self.assertEqual(result.source, "fallback")
        self.assertEqual(result.status_claim, "processing")

    async def test_progress_semantic_check_can_reject_unearned_discovery(self):
        llm = FeedbackLLM("I have located the sources.", "processing", safe=False)
        result = await FeedbackComposer(llm, 1).compose("Where is it?", "progress", "en", state)
        self.assertEqual(result.source, "fallback")
        self.assertEqual(result.reason, "feedback_not_approved")

    async def test_state_is_checked_again_after_model_verification(self):
        current = state(stage="searching", active_searches=1)

        class ChangingLLM(FeedbackLLM):
            async def complete_feedback(self, purpose, system, payload):
                result = await super().complete_feedback(purpose, system, payload)
                if purpose == "feedback_verify":
                    current.update(stage="checking", active_searches=0, evidence_count=1)
                return result

        llm = ChangingLLM("I'm searching for the observatory's opening date.", "searching")
        result = await FeedbackComposer(llm, 1).compose("When did it open?", "progress", "en", lambda: dict(current))
        self.assertEqual(result.source, "fallback")
        self.assertEqual(result.status_claim, "checking")

    async def test_state_change_can_regenerate_a_current_dynamic_progress(self):
        current = state(stage="searching", active_searches=1)

        class AdaptiveLLM:
            def __init__(self):
                self.generations = 0

            async def complete_feedback(self, purpose, system, payload):
                if purpose == "feedback_generate":
                    self.generations += 1
                    if self.generations == 1:
                        current.update(stage="checking", active_searches=0, evidence_count=1)
                        return {"text": "I'm searching for the observatory's opening date.", "status_claim": "searching"}
                    return {"text": "I'm checking the sources about the observatory's opening date.", "status_claim": "checking"}
                return {"safe": True}

        llm = AdaptiveLLM()
        result = await FeedbackComposer(llm, 1).compose("When did it open?", "progress", "en", lambda: dict(current))
        self.assertEqual(result.source, "model")
        self.assertEqual(result.status_claim, "checking")
        self.assertEqual(llm.generations, 2)

    async def test_wrong_language_feedback_is_rejected(self):
        result = await FeedbackComposer(FeedbackLLM(), 1).compose("银色天文台何时开放？", "opening", "zh", state)
        self.assertEqual(result.source, "fallback")
        self.assertEqual(result.text, "让我查一下。")

    async def test_fabricated_time_estimate_is_rejected(self):
        llm = FeedbackLLM("I'll have an answer in 5 seconds.")
        result = await FeedbackComposer(llm, 1).compose("When did it open?", "opening", "en", state)
        self.assertEqual(result.source, "fallback")

    async def test_feedback_timeout_is_bounded(self):
        class SlowLLM:
            async def complete_feedback(self, *args):
                await asyncio.sleep(1)
        result = await FeedbackComposer(SlowLLM(), 0.01).compose("Where is it?", "opening", "en", state)
        self.assertEqual(result.source, "fallback")
        self.assertEqual(result.reason, "TimeoutError")

    async def test_feedback_provider_failure_preserves_safe_fallback(self):
        class FailedFeedback:
            async def complete_feedback(self, *args):
                raise ProviderError("simulated feedback outage")
        result = await FeedbackComposer(FailedFeedback(), 1).compose("Where is it?", "progress", "en", state)
        self.assertEqual(result.source, "fallback")
        self.assertEqual(result.reason, "ProviderError")

    async def test_tinker_feedback_has_its_own_token_and_transport_budget(self):
        class FakeHTTP:
            def __init__(self):
                self.body = None

            def json(self, url, *, body, headers):
                self.body = body
                return {"choices": [{"finish_reason": "stop", "message": {"content": '{"safe":true}'}}]}

        http = FakeHTTP()
        settings = Settings(api_key="fixture-key", max_tokens=4096, timeout_s=45, feedback_timeout_s=6)
        with patch("cascadesystem.llm.HTTP", return_value=http) as factory:
            llm = TinkerLLM(settings, http=http)
            await llm.complete_feedback("feedback_verify", "fixture", {})
        factory.assert_called_once_with(6)
        self.assertEqual(http.body["max_completion_tokens"], 512)
        self.assertEqual(llm.calls[0]["purpose"], "feedback_verify")

    async def test_late_opening_is_cancelled_after_answer(self):
        class SlowOpening(DemoLLM):
            async def complete_feedback(self, purpose, system, payload):
                await asyncio.sleep(1)
                return await super().complete_feedback(purpose, system, payload)

        result = await Cascade(SlowOpening(), DemoSearch(), Settings()).run(QUESTION)
        self.assertEqual(result["status"], "complete")
        self.assertFalse(any(e.get("action") == "Backchannel" for e in result["events"]))
        final_index = next(e["sequence"] for e in result["events"] if e.get("action") == "Final Answer")
        self.assertFalse(any(e.get("action") in {"Backchannel", "Progress"} and e["sequence"] > final_index for e in result["events"]))

    async def test_feedback_does_not_block_search_and_factual_answer(self):
        class VerySlowFeedback(DemoLLM):
            async def complete_feedback(self, *args):
                await asyncio.sleep(10)
        result = await asyncio.wait_for(Cascade(VerySlowFeedback(), DemoSearch(), replace(Settings(), feedback_timeout_s=5)).run(QUESTION), timeout=1)
        self.assertEqual(result["status"], "complete")
        self.assertTrue(any(e["type"] == "search_finished" for e in result["events"]))


if __name__ == "__main__":
    unittest.main()
