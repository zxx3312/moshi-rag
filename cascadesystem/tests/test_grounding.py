"""Fictional regressions for output scope, dependency context and one final review."""
from copy import deepcopy
from dataclasses import asdict
import asyncio
import unittest

from cascadesystem.config import Settings
from cascadesystem.controller import Cascade
from cascadesystem.demo import DemoLLM
from cascadesystem.grounding import draft_units_valid, verification_context
from cascadesystem.models import Evidence, Judgment, plan_from_json, validate_judgments
from cascadesystem.protocol import completion_review
from cascadesystem.transport import ProviderError


def unit(uid, description, *, necessary=True, parents=()):
    return {'unit_id': uid, 'description': description, 'necessary': necessary,
            'depends_on': list(parents), 'queries': ['fictional ' + uid]}


def fact(uid, value, eid, text):
    return {'unit_id': uid, 'label': 'SUPPORTED', 'value': value, 'citations': [eid],
            'quotes': [{'evidence_id': eid, 'text': text}]}


def chain():
    units = plan_from_json({'units': [
        unit('u1', 'Silver Ship captain', necessary=False),
        unit('u2', 'parent of {u1}', necessary=False, parents=['u1']),
        unit('u3', 'birthplace of {u2}', parents=['u2']),
        unit('u4', 'unrelated task', necessary=False)]})
    evidence = [Evidence('e1', 'Silver Ship', 'https://example.invalid/ship', 'The captain is Aster.', 0),
                Evidence('e2', 'Aster', 'https://example.invalid/aster', 'Aster is a child of Beryl.', 0),
                Evidence('e3', 'Beryl', 'https://example.invalid/beryl', 'Beryl was born in Cedar.', 0),
                Evidence('e4', 'Unrelated', 'https://example.invalid/noise', 'Unrelated text.', 0)]
    rows = [fact(uid, value, source.evidence_id, source.text) for uid, value, source in
            zip(['u1', 'u2', 'u3'], ['Aster', 'Beryl', 'Cedar'], evidence)]
    rows.append({'unit_id': 'u4', 'label': 'UNRESOLVED'})
    judgments = validate_judgments({'judgments': rows}, units, evidence)
    return units, evidence, judgments


class ContextTests(unittest.TestCase):
    def test_transitive_dependencies_are_context_not_extra_output(self):
        units, evidence, judgments = chain()
        context = verification_context(['u3'], units, judgments, evidence)
        self.assertEqual([e['evidence_id'] for e in context['evidence']], ['e1', 'e2', 'e3'])
        self.assertEqual([f['unit_id'] for f in context['DEPENDENCY_FACTS']], ['u1', 'u2'])
        self.assertTrue(all(f['context_only'] for f in context['DEPENDENCY_FACTS']))
        self.assertNotIn('Unrelated', str(context))
        self.assertEqual(context['DEPENDENCY_FACTS'][1]['description'], 'parent of Aster')

    def test_invisible_dependency_cannot_be_used_for_verification(self):
        units, evidence, judgments = chain()
        with self.assertRaisesRegex(ValueError, 'invisible'):
            verification_context(['u3'], units, judgments, evidence[1:])

    def test_unsupported_parent_cannot_be_used_for_output(self):
        units, evidence, judgments = chain()
        judgments['u1'] = Judgment()
        with self.assertRaisesRegex(ValueError, 'dependencies'):
            verification_context(['u3'], units, judgments, evidence)

    def test_output_unit_accounting_rejects_extra_missing_and_duplicate_units(self):
        for reply in [{}, {'expressed_unit_ids': ['u1', 'u3']}, {'expressed_unit_ids': ['u1', 'u1']},
                      {'expressed_unit_ids': []}, {'expressed_unit_ids': [1]}]:
            with self.subTest(reply=reply):
                self.assertFalse(draft_units_valid(reply, ['u1']))
        self.assertTrue(draft_units_valid({'expressed_unit_ids': ['u1']}, ['u1']))

    def test_evidence_backed_no_is_supported_and_not_a_conflict(self):
        units = plan_from_json({'units': [unit('u1', 'whether the fictional hatch is open')]})
        source = Evidence('e1', 'Hatch', 'https://example.invalid/hatch', 'The hatch is not open.', 0)
        result = validate_judgments({'judgments': [fact('u1', 'No', 'e1', source.text)]}, units, [source])
        self.assertEqual(result['u1'].label, 'SUPPORTED')
        self.assertEqual(result['u1'].value, 'No')


class NoSearch:
    async def search(self, query):
        raise AssertionError('This test uses scheduled evidence only')


async def stream_batches(*batches):
    for batch in batches:
        await asyncio.sleep(.01)
        yield batch


def document(eid, text, title='Silver Ship'):
    return {'evidence_id': eid, 'title': title, 'text': text, 'url': 'https://example.invalid/' + eid}


class ScopeLLM(DemoLLM):
    requires_output_unit_ids = True

    def __init__(self, *, extra=False, missing_contract=False):
        super().__init__()
        self.requests = []
        self.extra, self.missing_contract = extra, missing_contract

    async def complete(self, purpose, system, payload):
        self.requests.append((purpose, deepcopy(payload)))
        if purpose == 'decompose':
            return {'units': [unit('u1', 'Silver Ship launch year'), unit('u2', 'Silver Ship return year')]}
        if purpose == 'judge':
            rows = []
            for uid, word, value in [('u1', 'launched', '2044'), ('u2', 'returned', '2045')]:
                source = next((e for e in payload['evidence'] if word in e['text']), None)
                rows.append(fact(uid, value, source['evidence_id'], source['text']) if source else
                            {'unit_id': uid, 'label': 'UNRESOLVED'})
            return {'judgments': rows}
        if purpose == 'generate':
            text = ' '.join(f"The {f['description']} was {f['value']}." for f in payload['APPROVED_FACTS'])
            if self.extra and payload['action'] == 'Partial Answer':
                text += ' Therefore, the mission succeeded.'
            return {'text': text}
        if purpose == 'verify':
            # A partial answer is valid on its selected fact alone, even with missing other parts.
            reply = {'facts_valid': True, 'approved': True}
            if not self.missing_contract:
                reply['expressed_unit_ids'] = list(payload['output_unit_ids'])
                if self.extra and payload['action'] == 'Partial Answer':
                    reply['expressed_unit_ids'].append('u3')
            return reply
        return await super().complete(purpose, system, payload)


class OutputTests(unittest.IsolatedAsyncioTestCase):
    async def run_scope(self, llm):
        return await Cascade(llm, NoSearch(), Settings()).run(
            'When did the fictional Silver Ship launch and return?',
            evidence_stream=stream_batches([document('d1', 'The Silver Ship launched in 2044.')],
                                           [document('d2', 'The Silver Ship returned in 2045.')]))

    async def test_partial_answer_is_allowed_and_final_does_not_repeat_earlier_fact(self):
        llm = ScopeLLM()
        result = await self.run_scope(llm)
        answers = [e for e in result['events'] if e['type'] == 'utterance' and e.get('claims')]
        self.assertEqual(result['status'], 'complete')
        self.assertEqual([e['action'] for e in answers], ['Partial Answer', 'Final Answer'])
        self.assertEqual([f['unit_id'] for f in answers[0]['claims']], ['u1'])
        self.assertEqual([f['unit_id'] for f in answers[1]['claims']], ['u2'])
        self.assertNotIn('2044', answers[1]['text'])
        checks = [p for purpose, p in llm.requests if purpose == 'verify']
        self.assertEqual(checks[0]['action'], 'Partial Answer')
        self.assertEqual(checks[1]['already_output_unit_ids'], ['u1'])
        self.assertFalse(answers[0]['fallback'])

    async def test_unselected_conclusion_is_not_output_and_does_not_invalidate_the_fact(self):
        result = await self.run_scope(ScopeLLM(extra=True))
        partial = next(e for e in result['events'] if e['type'] == 'utterance' and e['action'] == 'Partial Answer')
        self.assertTrue(partial['fallback'])
        self.assertNotIn('mission succeeded', partial['text'])
        self.assertEqual(partial['claims'][0]['value'], '2044')
        self.assertEqual(result['status'], 'complete')
        self.assertTrue(any(e['type'] == 'draft_rejected' for e in result['events']))

    async def test_strict_provider_missing_output_contract_uses_only_fact_template(self):
        result = await self.run_scope(ScopeLLM(missing_contract=True))
        answers = [e for e in result['events'] if e['type'] == 'utterance' and e.get('claims')]
        self.assertEqual(result['status'], 'complete')
        self.assertTrue(all(e['fallback'] for e in answers))

    async def test_missing_fact_validity_does_not_release_facts_for_strict_provider(self):
        class MissingValidity(ScopeLLM):
            async def complete(self, purpose, system, payload):
                if purpose == 'verify':
                    return {'approved': True, 'expressed_unit_ids': payload['output_unit_ids']}
                return await super().complete(purpose, system, payload)
        result = await self.run_scope(MissingValidity())
        self.assertEqual(result['status'], 'incomplete')
        self.assertFalse(result['output_enqueued_units'])

    async def test_generation_fallback_still_undergoes_fact_verification(self):
        class InvalidGenerator(ScopeLLM):
            async def complete(self, purpose, system, payload):
                if purpose == 'generate':
                    return {'text': 'A draft that omits the date.'}
                if purpose == 'verify':
                    self.requests.append((purpose, deepcopy(payload)))
                    return {'approved': False, 'facts_valid': False, 'expressed_unit_ids': payload['output_unit_ids']}
                return await super().complete(purpose, system, payload)
        llm = InvalidGenerator()
        result = await self.run_scope(llm)
        self.assertEqual(result['status'], 'incomplete')
        checks = [p for purpose, p in llm.requests if purpose == 'verify']
        self.assertTrue(checks)
        self.assertIn('2044', checks[0]['draft'])
        self.assertFalse(result['output_enqueued_units'])

    async def test_verification_failure_does_not_fall_back_to_unchecked_speech(self):
        class FailedVerification(ScopeLLM):
            async def complete(self, purpose, system, payload):
                if purpose == 'verify':
                    raise ProviderError('simulated verification outage')
                return await super().complete(purpose, system, payload)
        result = await self.run_scope(FailedVerification())
        self.assertEqual(result['status'], 'error')
        self.assertFalse(any(e.get('claims') for e in result['events'] if e['type'] == 'utterance'))

    async def test_generation_provider_failure_stops_without_another_provider_call(self):
        class FailedGeneration(ScopeLLM):
            async def complete(self, purpose, system, payload):
                if purpose == 'generate':
                    raise ProviderError('HTTP 401 from fictional.invalid')
                return await super().complete(purpose, system, payload)
        llm = FailedGeneration()
        result = await self.run_scope(llm)
        self.assertEqual(result['status'], 'error')
        self.assertFalse(any(purpose == 'verify' for purpose, _ in llm.requests))
        self.assertFalse(result['output_enqueued_units'])

    async def test_rejected_parent_invalidates_previously_supported_child(self):
        class RejectedParent(ScopeLLM):
            async def complete(self, purpose, system, payload):
                if purpose == 'decompose':
                    return {'units': [unit('u1', 'Silver Ship captain'),
                                      unit('u2', 'parent of {u1}', necessary=False, parents=['u1'])]}
                if purpose == 'judge':
                    return {'judgments': [fact('u1', 'Aster', 'd1', 'The captain is Aster.'),
                                          fact('u2', 'Beryl', 'd2', 'Aster is a child of Beryl.')]}
                if purpose == 'verify':
                    return {'approved': False, 'facts_valid': False, 'expressed_unit_ids': payload['output_unit_ids']}
                return await super().complete(purpose, system, payload)
        result = await Cascade(RejectedParent(), NoSearch(), Settings()).run('Who captains the fictional Silver Ship?',
            evidence_stream=stream_batches([document('d1', 'The captain is Aster.'),
                                           document('d2', 'Aster is a child of Beryl.')]))
        self.assertEqual(result['status'], 'incomplete')
        self.assertEqual(result['judgments']['u2']['label'], 'UNRESOLVED')
        self.assertFalse(result['output_enqueued_units'])

    async def test_final_verifier_receives_full_bridge_chain_but_outputs_only_requested_fact(self):
        units, evidence, judgments = chain()
        class Bridge(ScopeLLM):
            async def complete(self, purpose, system, payload):
                self.requests.append((purpose, deepcopy(payload)))
                if purpose == 'decompose':
                    return {'units': [asdict(u) | {'depends_on': list(u.depends_on), 'queries': list(u.queries)} for u in units]}
                if purpose == 'judge':
                    return {'judgments': [asdict(judgments[u.unit_id]) | {'unit_id': u.unit_id} for u in units]}
                if purpose == 'generate':
                    return {'text': 'Beryl was born in Cedar.'}
                if purpose == 'verify':
                    valid = {e['evidence_id'] for e in payload['evidence']} == {'e1', 'e2', 'e3'}
                    return {'approved': valid, 'facts_valid': valid, 'expressed_unit_ids': ['u3']}
                return await super().complete(purpose, system, payload)
        llm = Bridge()
        result = await Cascade(llm, NoSearch(), Settings()).run(
            "Where was the fictional Silver Ship captain's parent born?",
            evidence_stream=stream_batches([document(e.evidence_id, e.text, e.title) for e in evidence]))
        self.assertEqual(result['status'], 'complete')
        output = next(e for e in result['events'] if e['type'] == 'utterance' and e.get('claims'))
        self.assertEqual([f['unit_id'] for f in output['claims']], ['u3'])
        self.assertFalse(output['fallback'])


class ReviewLLM(ScopeLLM):
    def __init__(self, mode='recover'):
        super().__init__()
        self.mode = mode

    async def complete(self, purpose, system, payload):
        self.requests.append((purpose, deepcopy(payload)))
        if purpose == 'decompose':
            return {'units': [unit('u1', 'Silver Ship launch year')]}
        if purpose == 'judge':
            if payload.get('review_mode') == 'retrieval_complete':
                if self.mode == 'provider_error':
                    raise ProviderError('HTTP 401 from fictional.invalid')
                if self.mode == 'malformed':
                    return {'judgments': []}
                if self.mode == 'recover':
                    return {'judgments': [fact('u1', '2044', 'd1', 'The Silver Ship launched in 2044.')]}
                if self.mode == 'future':
                    return {'judgments': [fact('u1', '2044', 'future', 'Future text.') ]}
            return {'judgments': [{'unit_id': 'u1', 'label': 'CONTRADICTED' if self.mode == 'conflict' else 'UNRESOLVED'}]}
        return await super().complete(purpose, system, payload)


class CompletionReviewTests(unittest.IsolatedAsyncioTestCase):
    async def test_changed_ancestor_invalidates_other_children_but_preserves_unrelated_facts(self):
        units = plan_from_json({'units': [unit('u1', 'pilot', necessary=False),
                                         unit('u2', 'pilot birthplace', parents=['u1']),
                                         unit('u3', 'pilot launch year', parents=['u1']),
                                         unit('u4', 'planet name', necessary=False)]})
        sources = [Evidence('e1', 'Ship', 'https://example.invalid/ship', 'The pilot is Aster.', 0),
                   Evidence('e2', 'Aster', 'https://example.invalid/aster', 'Aster launched in 2044.', 0),
                   Evidence('e3', 'Planet', 'https://example.invalid/planet', 'The planet is Fable.', 0)]
        rows = [fact('u1', 'Aster', 'e1', sources[0].text), {'unit_id': 'u2', 'label': 'UNRESOLVED'},
                fact('u3', '2044', 'e2', sources[1].text), fact('u4', 'Fable', 'e3', sources[2].text)]
        previous = validate_judgments({'judgments': rows}, units, sources)
        class Reply:
            async def complete(self, *args):
                return {'judgments': [{'unit_id': u.unit_id, 'label': 'CONTRADICTED' if u.unit_id == 'u1' else 'UNRESOLVED'} for u in units]}
        async def emit(*args, **kwargs):
            pass
        result = await completion_review(Reply(), 'A fictional question?', 'en', units, sources, previous, ['u2'], emit)
        self.assertEqual(result['u3'].label, 'UNRESOLVED')
        self.assertEqual(result['u4'].label, 'SUPPORTED')
        self.assertEqual(result['u4'].value, 'Fable')

    async def run_review(self, mode):
        llm = ReviewLLM(mode)
        result = await Cascade(llm, NoSearch(), Settings()).run('When did the fictional Silver Ship launch?',
            evidence_stream=stream_batches([document('d1', 'The Silver Ship launched in 2044.')]))
        return llm, result

    async def test_one_review_can_recover_a_missed_fact_from_the_same_snapshot(self):
        llm, result = await self.run_review('recover')
        self.assertEqual(result['status'], 'complete')
        judges = [p for purpose, p in llm.requests if purpose == 'judge']
        self.assertEqual(len(judges), 2)
        self.assertEqual(judges[0]['evidence'], judges[1]['evidence'])
        self.assertEqual(judges[1]['review_unit_ids'], ['u1'])
        self.assertEqual(sum(e['type'] == 'semantic_review_requested' for e in result['events']), 1)

    async def test_genuinely_unresolved_stays_unresolved_without_a_loop(self):
        llm, result = await self.run_review('unresolved')
        self.assertEqual(result['status'], 'incomplete')
        self.assertEqual(sum(purpose == 'judge' for purpose, _ in llm.requests), 2)
        self.assertFalse(result['output_enqueued_units'])

    async def test_review_cannot_use_future_or_invented_citations(self):
        llm, result = await self.run_review('future')
        self.assertEqual(result['status'], 'incomplete')
        self.assertFalse(result['output_enqueued_units'])
        review = next(p for purpose, p in llm.requests if p.get('review_mode'))
        self.assertEqual(review['visible_evidence_ids'], ['d1'])
        self.assertFalse(any(purpose == 'judge_repair' for purpose, _ in llm.requests))

    async def test_malformed_review_preserves_previous_judgment(self):
        _, result = await self.run_review('malformed')
        self.assertEqual(result['status'], 'incomplete')
        self.assertTrue(any(e['type'] == 'semantic_review_rejected' for e in result['events']))

    async def test_actual_conflict_is_not_forced_into_a_negative_answer(self):
        llm, result = await self.run_review('conflict')
        self.assertEqual(result['status'], 'incomplete')
        self.assertEqual(result['judgments']['u1']['label'], 'CONTRADICTED')
        self.assertFalse(any(p.get('review_mode') for _, p in llm.requests))

    async def test_auth_failure_during_review_is_not_retried_or_hidden(self):
        llm, result = await self.run_review('provider_error')
        self.assertEqual(result['status'], 'error')
        self.assertEqual(sum(purpose == 'judge' for purpose, _ in llm.requests), 2)
        self.assertTrue(any(e['type'] == 'failure' for e in result['events']))


if __name__ == '__main__':
    unittest.main()
