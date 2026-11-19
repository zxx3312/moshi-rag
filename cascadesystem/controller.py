"""Single-question, event-driven cascade with incremental evidence visibility."""
import asyncio
from dataclasses import asdict
import re
import time
from urllib.parse import urlsplit

from .llm import GENERATE, VERIFY
from .models import Evidence, Judgment, resolve_text, validate_judgments
from .protocol import completion_review, decompose, judge as judge_snapshot
from .grounding import draft_units_valid, verification_context
from .presentation import detect_language, finish_sentence, matches_language
from .transport import ProviderError
from .feedback import FeedbackComposer
from .wording import fact_sentences, label_style, missing_sentence
from .conversation import ClarificationNeeded, resolve_context


class Cascade:
    def __init__(self, llm, search, settings):
        self.llm, self.search, self.settings = llm, search, settings

    async def run(self, question, on_event=None, *, language="auto", started_at=None, history=None,
                  evidence_stream=None):
        if not isinstance(question, str) or not question.strip() or len(question) > 4000:
            raise ValueError("Question must contain 1..4000 characters")
        started = time.monotonic() if started_at is None else started_at
        original_question, used_history_ids = question, []
        call_start = len(getattr(self.llm, "calls", []))
        diagnostic_start = len(getattr(self.search, "diagnostics", []))
        events, units, sources = [], [], []
        judgments, queued, searches, failures = {}, {}, [], []
        pending = {}
        used_queries, source_keys = set(), set()
        count, progress_sent, finished = 0, False, False
        stage, output_epoch, final_output = "planning", 0, False
        language = detect_language(question, language)
        chinese = language == "zh"
        composer = FeedbackComposer(self.llm, self.settings.feedback_timeout_s)
        stream = evidence_stream.__aiter__() if evidence_stream is not None else None
        stream_finished = False

        async def emit(kind, **data):
            if kind == "utterance":
                data["language"] = language
            event = {"sequence": len(events), "time_s": round(time.monotonic() - started, 6),
                     "type": kind, **data}
            events.append(event)
            if on_event is not None:
                await on_event(event)

        def execution_state():
            return {"stage": stage, "searches_started": count, "searches_completed": len(searches),
                    "active_searches": sum(not task.done() for task in pending),
                    "evidence_count": len(sources),
                    "supported_units": sum(j.label == "SUPPORTED" for j in judgments.values()),
                    "output_units": len(queued)}

        async def render_feedback(kind):
            epoch = output_epoch
            request_state = execution_state()
            await emit("feedback_requested", feedback_kind=kind, execution_state=request_state)
            result = await composer.compose(question, kind, language, execution_state)
            if finished or final_output or epoch != output_epoch or (kind == "opening" and queued):
                await emit("feedback_discarded", feedback_kind=kind, reason="answer_already_advanced")
                return False
            await emit("utterance", action="Backchannel" if kind == "opening" else "Progress",
                       text=result.text, claims=[], feedback_source=result.source,
                       feedback_status_claim=result.status_claim, feedback_fallback_reason=result.reason,
                       execution_state=execution_state())
            last_output[0] = time.monotonic()
            return True

        async def feedback():
            nonlocal progress_sent
            while True:
                await asyncio.sleep(min(self.settings.progress_s, 0.25))
                if not opening.done():
                    continue
                if not finished and not progress_sent and time.monotonic() - last_output[0] >= self.settings.progress_s:
                    progress_sent = True
                    if not await render_feedback("progress"):
                        progress_sent = False

        def description(unit):
            text = unit.description
            for uid, judgment in judgments.items():
                if judgment.label == "SUPPORTED":
                    text = text.replace("{" + uid + "}", judgment.value)
            return re.sub(r"\{u[0-9]+\}", "前置实体" if chinese else "the unresolved entity", text)

        async def speak(action, ids, missing=()):
            nonlocal progress_sent, stage, output_epoch, final_output
            stage = "formulating"
            strict = getattr(self.llm, 'requires_output_unit_ids', False)
            facts = [{"unit_id": uid, "description": description(by_id[uid]),
                      "value": judgments[uid].value, "citations": judgments[uid].citations,
                      "quotes": judgments[uid].quotes} for uid in ids]
            text, fallback = "", False
            if facts:
                context = verification_context(ids, units, judgments, sources)
                payload = {"question": question, "output_language": language,
                           "units": [asdict(by_id[uid]) for uid in ids], "APPROVED_FACTS": facts,
                           "action": action, "output_unit_ids": list(ids),
                           "already_output_unit_ids": list(queued), "unresolved_unit_ids": list(missing),
                           "speech_style": "natural_complete_sentences"}
                def fact_template():
                    return fact_sentences(facts, language, natural=strict)
                try:
                    raw = await self.llm.complete("generate", GENERATE, payload)
                    text = raw.get("text")
                    if not isinstance(text, str) or not text.strip() or len(text) > 1500 or not matches_language(text, language) or any(f["value"].casefold() not in text.casefold() for f in facts):
                        raise ValueError("Draft omitted a value or had invalid length")
                    if strict and label_style(text, facts):
                        raise ValueError("Draft copied a unit-label/value pair instead of a sentence")
                    text = finish_sentence(text, language)
                except ValueError as error:
                    await emit('generation_fallback', reason=str(error), output_unit_ids=list(ids))
                    text, fallback = fact_template(), True
                # Even a template draft must pass fact verification. Provider failures propagate.
                checked = await self.llm.complete("verify", VERIFY, {**payload, **context, "draft": text})
                await emit("verification_reply", reply=checked, output_unit_ids=list(ids),
                           output_action=action, dependency_unit_ids=[u["unit_id"] for u in context["dependency_units"]],
                           evidence_snapshot_ids=[e["evidence_id"] for e in context["evidence"]])
                if checked.get("facts_valid") is False or ((strict or any(by_id[uid].subject for uid in ids)) and checked.get("facts_valid") is not True):
                    await emit("facts_rejected", unit_ids=ids, reason=str(checked.get("reason", "Facts not established")))
                    for uid in ids:
                        judgments[uid] = Judgment(reason="Final verifier rejected fact support or entity identity")
                    # A rejected ancestor must not leave a supported descendant behind.
                    refreshed = validate_judgments({'judgments': [asdict(judgments[u.unit_id]) | {'unit_id': u.unit_id}
                                                                 for u in units]}, units, sources)
                    judgments.update(refreshed)
                    return False
                accounted = draft_units_valid(checked, ids) if strict or 'expressed_unit_ids' in checked else True
                if checked.get("approved") is not True or not accounted:
                    await emit("draft_rejected", reason="Draft wording or output-unit accounting rejected",
                               output_unit_ids=list(ids), expressed_unit_ids=checked.get("expressed_unit_ids"))
                    text, fallback = fact_template(), True
            if missing:
                text += ' ' + missing_sentence([description(by_id[uid]) for uid in missing], language, natural=strict)
            if not text.strip():
                text = "已回答全部已确认的信息。" if chinese else "That completes the confirmed information."
            output_epoch += 1
            if action == "Final Answer":
                final_output = True
            await emit("utterance", action=action, text=finish_sentence(text, language), claims=facts,
                       unresolved=list(missing), fallback=fallback,
                       evidence_snapshot_ids=[e.evidence_id for e in sources])
            # This means enqueued for output, not already spoken. Audio records actual completion separately.
            for uid in ids:
                queued[uid] = judgments[uid].value
            progress_sent, last_output[0] = False, time.monotonic()
            return True

        async def search_one(query, subject):
            begin = time.monotonic()
            try:
                search_scoped = getattr(self.search, "search_subject", None)
                documents = await search_scoped(query, subject) if subject and search_scoped is not None else await self.search.search(query)
                return {"query": query, "subject": subject, "status": "ok", "documents": documents,
                        "returned_pages": [{"title": p.get("title"), "url": p.get("url"),
                                            "entity_resolution": p.get("entity_resolution", "unspecified")} for p in documents],
                        "latency_s": time.monotonic() - begin}
            except (ProviderError, ValueError) as exc:
                return {"query": query, "subject": subject, "status": "error", "documents": [], "returned_pages": [],
                        "error": str(exc), "latency_s": time.monotonic() - begin}

        async def schedule():
            nonlocal count, stream_finished
            if stream is not None:
                if pending or stream_finished:
                    return
                async def receive_batch():
                    nonlocal stream_finished
                    try:
                        documents = await anext(stream)
                    except StopAsyncIteration:
                        documents, stream_finished = [], True
                    return {"query": "[scheduled evidence]", "subject": "", "status": "ok",
                            "documents": documents, "returned_pages": [], "mode": "trace"}
                count += 1
                task = asyncio.create_task(receive_batch())
                pending[task] = "__scheduled_evidence__"
                await emit("trace_batch_requested")
                return
            busy = set(pending.values())
            for unit in units:
                uid = unit.unit_id
                if uid in busy or judgments[uid].label in {"SUPPORTED", "CONTRADICTED"}:
                    continue
                if any(judgments[d].label != "SUPPORTED" for d in unit.depends_on):
                    continue
                for template in unit.queries:
                    query = resolve_text(template, judgments)
                    key = (uid, query)
                    if key in used_queries:
                        continue
                    if count >= self.settings.max_searches:
                        return
                    used_queries.add(key)
                    count += 1
                    subject = resolve_text(unit.subject, judgments) if unit.subject else ""
                    task = asyncio.create_task(search_one(query, subject))
                    pending[task] = uid
                    await emit("search_started", unit_id=uid, query=query, subject=subject)
                    break

        async def judge(review=False):
            nonlocal judgments, stage, output_epoch
            if not sources:
                return
            stage = "checking"
            if review:
                targets = [u.unit_id for u in units if u.necessary and judgments[u.unit_id].label == "UNRESOLVED"]
                if not targets:
                    return
                updated = await completion_review(self.llm, question, language, units, sources, judgments, targets, emit)
                if updated is None:
                    return
                judgments = updated
            else:
                judgments = await judge_snapshot(self.llm, question, language, units, sources, emit,
                                                 previous_judgments=judgments)
            await emit("judgments", judgments={uid: asdict(j) for uid, j in judgments.items()},
                       evidence_snapshot_ids=[e.evidence_id for e in sources], semantic_review=review)
            for uid, value in list(queued.items()):
                if judgments[uid].label != "SUPPORTED" or judgments[uid].value != value:
                    queued.pop(uid)
                    output_epoch += 1
                    await emit("utterance", action="Correction", claims=[], unit_id=uid,
                               text=(f"关于“{description(by_id[uid])}”，先前内容需要重新核实，请暂不采用。" if chinese else
                                     f"Please disregard my earlier statement about {description(by_id[uid])}; it needs verification."))

        last_output = [time.monotonic()]
        opening = asyncio.create_task(render_feedback("opening"))
        heartbeat = asyncio.create_task(feedback())
        status = "error"
        try:
            if history:
                stage = "contextualizing"
                question, used_history_ids = await resolve_context(self.llm, question, language, history)
                await emit("context_resolved", original_question=original_question, standalone_question=question,
                           used_turn_ids=used_history_ids, history_is_evidence=False)
            stage = "planning"
            units = await decompose(self.llm, question, language, self.settings, emit)
            by_id = {u.unit_id: u for u in units}
            judgments = {u.unit_id: Judgment() for u in units}
            await emit("plan", units=[asdict(u) for u in units])
            await schedule()
            while pending:
                stage = "searching"
                done, _ = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
                for task in sorted(done, key=lambda t: pending[t]):
                    uid = pending.pop(task)
                    result = task.result()
                    documents = result.pop("documents")
                    result["unit_id"] = uid
                    searches.append(result)
                    if result["status"] == "error":
                        failures.append(result)
                    await emit("search_finished", **result)
                    for document in documents:
                        title, url, text = document.get("title"), document.get("url"), document.get("text")
                        if not all(isinstance(v, str) and v.strip() for v in (title, url, text)) or urlsplit(url).scheme not in {"https", "http"}:
                            continue
                        key = (url, text)
                        if key in source_keys or len(sources) >= self.settings.max_sources:
                            continue
                        remaining = self.settings.evidence_chars - sum(len(e.text) for e in sources)
                        if remaining <= 0:
                            continue
                        source_keys.add(key)
                        evidence_id = document.get("evidence_id") if stream is not None else f"e{len(sources) + 1}"
                        if not isinstance(evidence_id, str) or not evidence_id or any(e.evidence_id == evidence_id for e in sources):
                            raise ValueError("Invalid or duplicate scheduled evidence ID")
                        evidence = Evidence(evidence_id, title, url, text[:min(self.settings.source_chars, remaining)], time.monotonic() - started,
                                            requested_subject=document.get("requested_subject", ""),
                                            resolved_title=document.get("resolved_title", ""), entity_resolution=document.get("entity_resolution", "unspecified"))
                        sources.append(evidence)
                        await emit("evidence", evidence=asdict(evidence))
                if stream_finished:
                    break
                # Search workers never expose their completed results to the model before ingestion here.
                await judge()
                necessary = [u.unit_id for u in units if u.necessary]
                new = [u.unit_id for u in units if judgments[u.unit_id].label == "SUPPORTED" and u.unit_id not in queued]
                if all(judgments[uid].label == "SUPPORTED" for uid in necessary):
                    if await speak("Final Answer", [uid for uid in new if by_id[uid].necessary]):
                        status = "complete"
                        break
                    new = [u.unit_id for u in units if judgments[u.unit_id].label == "SUPPORTED" and u.unit_id not in queued]
                await schedule()
                if pending and new:
                    await speak("Partial Answer", new)
            if status != "complete":
                await judge(review=True)
                missing = [u.unit_id for u in units if u.necessary and judgments[u.unit_id].label != "SUPPORTED"]
                new = [u.unit_id for u in units if judgments[u.unit_id].label == "SUPPORTED" and u.unit_id not in queued]
                accepted = await speak("Final Answer", new, missing)
                if not accepted:
                    missing = [u.unit_id for u in units if u.necessary and judgments[u.unit_id].label != "SUPPORTED"]
                    await speak("Final Answer", [], missing)
                status = "complete" if accepted and not missing else "incomplete"
        except ClarificationNeeded as exc:
            status, final_output = "needs_clarification", True
            await emit("utterance", action="Final Answer", claims=[], clarification=True,
                       text=finish_sentence(str(exc), language))
        except (ProviderError, ValueError) as exc:
            await emit("failure", error=str(exc))
            final_output = True
            await emit("utterance", action="Final Answer", claims=[], text=(
                "查询或证据核对未能完成，我暂时不能给出可靠答案。" if chinese else
                "The search or verification failed, so I cannot give a reliable answer yet."))
        finally:
            finished = True
            heartbeat.cancel()
            opening.cancel()
            for task in pending:
                task.cancel()
            background = await asyncio.gather(heartbeat, opening, *pending, return_exceptions=True)
            for name, result in zip(("progress", "opening"), background[:2]):
                if isinstance(result, Exception):
                    await emit("feedback_failure", component=name, error_type=type(result).__name__)
        await emit("finished", status=status)
        return {
            "question": original_question, "resolved_question": question, "used_history_turn_ids": used_history_ids,
            "response_language": language, "status": status, "clock": "wall_monotonic",
            "time_origin": "question_text_ready_after_optional_asr",
            "model": self.settings.model, "judge_model": self.settings.judge_model or self.settings.model,
            "units": [asdict(u) for u in units],
            "judgments": {uid: asdict(j) for uid, j in judgments.items()},
            "evidence": [asdict(e) for e in sources], "searches": searches,
            "search_failures": failures, "llm_calls": list(getattr(self.llm, "calls", []))[call_start:],
            "search_diagnostics": list(getattr(self.search, "diagnostics", []))[diagnostic_start:],
            "output_enqueued_units": queued, "events": events,
            "note": "Prototype model judgments are not independent gold scores. Output event times are not spoken claim times.",
            "evidence_mode": "scheduled_trace" if stream is not None else "search",
        }
