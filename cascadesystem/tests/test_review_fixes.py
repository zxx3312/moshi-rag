"""Fictional regressions for semantic review, identity and quote contracts."""
from copy import deepcopy
import unittest

from cascadesystem.config import Settings
from cascadesystem.models import Evidence, Judgment, plan_from_json, validate_judgments
from cascadesystem.protocol import completion_review, decompose, judge, literal_quote_whitespace
from cascadesystem.tests.test_protocol import Recorder, Replies
from cascadesystem.wording import fact_sentences


def unit(description='singer of the album Silver Echo', subject='Silver Echo (album)'):
    return {'unit_id': 'u1', 'description': description, 'subject': subject,
            'necessary': True, 'depends_on': [], 'queries': ['Silver Echo singer']}


def supported(value='Aster Rowan', quote='by Aster Rowan'):
    return {'unit_id': 'u1', 'label': 'SUPPORTED', 'value': value,
            'citations': ['e1'], 'quotes': [{'evidence_id': 'e1', 'text': quote}]}


def source(title='Silver Echo', text='Silver Echo is a studio album by Aster Rowan.', **extra):
    return Evidence('e1', title, 'https://example.invalid/fiction', text, 0, **extra)


class PlanSemanticReviewTests(unittest.IsolatedAsyncioTestCase):
    async def test_question_only_review_can_remove_an_extra_ancestor_before_execution(self):
        bad = {'units': [unit('father of Liora', ''),
            {**unit('father of {u1}', ''), 'unit_id': 'u2', 'depends_on': ['u1'], 'necessary': False},
            {**unit('father of {u2}, grandfather of Liora', ''), 'unit_id': 'u3', 'depends_on': ['u2']}]}
        fixed = deepcopy(bad)
        fixed['units'] = fixed['units'][:2]
        fixed['units'][0]['necessary'] = False
        fixed['units'][1]['necessary'] = True
        llm = Replies(bad, fixed)
        llm.requires_plan_review = True
        recorder = Recorder()
        result = await decompose(llm, 'Who is fictional Liora\'s grandfather?', 'en', Settings(), recorder)
        self.assertEqual([u.unit_id for u in result if u.necessary], ['u2'])
        self.assertEqual([p for p, _ in llm.requests], ['decompose', 'plan_review'])
        review = llm.requests[-1][1]
        self.assertEqual(set(review), {'question', 'output_language', 'proposed_units'})
        self.assertTrue(next(e for e in recorder.events if e['type'] == 'plan_review_finished')['changed'])

    async def test_choice_review_can_avoid_an_unnecessary_negative_prerequisite(self):
        candidate = {**unit('whether Liora won the fictional Silver Medal', ''), 'necessary': False}
        initial = {'units': [candidate, {**unit('which of Liora and Mira won the medal', ''),
                       'unit_id': 'u2', 'depends_on': ['u1']}]}
        fixed = {'units': [{**unit('which of Liora and Mira won the fictional Silver Medal', '')}]}
        llm = Replies(initial, fixed)
        llm.requires_plan_review = True
        result = await decompose(llm, 'Which of Liora and Mira won the fictional Silver Medal?',
                                 'en', Settings(), Recorder())
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].depends_on, ())

    async def test_invalid_review_is_not_executed_or_given_an_unbounded_retry(self):
        llm = Replies({'units': [unit()]}, {'units': []})
        llm.requires_plan_review = True
        with self.assertRaises(ValueError):
            await decompose(llm, 'Who sang Silver Echo?', 'en', Settings(), Recorder())
        self.assertEqual(len(llm.requests), 2)


class IdentityScopeTests(unittest.TestCase):
    def check(self, plan, evidence, row):
        return validate_judgments({'judgments': [row]}, plan_from_json({'units': [plan]}), [evidence])['u1']

    def test_explicit_album_lead_can_support_a_redundantly_qualified_album_subject(self):
        self.assertEqual(self.check(unit(), source(), supported()).label, 'SUPPORTED')

    def test_role_qualified_person_needs_both_role_context_and_self_description(self):
        p = unit('birthplace of director Mira Rowan', 'Mira Rowan')
        e = source('Mira Rowan (director)', 'Mira Rowan is an Aster-born film director.')
        self.assertEqual(self.check(p, e, supported('Aster', 'Aster-born')).label, 'SUPPORTED')
        p['description'] = 'birthplace of Mira Rowan'
        self.assertEqual(self.check(p, e, supported('Aster', 'Aster-born')).label, 'UNRESOLVED')

    def test_mentioning_another_person_with_the_role_is_not_self_identification(self):
        e = source('Mira Rowan (director)', 'Mira Rowan is a friend of the director Aster.')
        p = unit('birthplace of director Mira Rowan', 'Mira Rowan')
        self.assertEqual(self.check(p, e, supported('Aster', 'Aster')).label, 'UNRESOLVED')

    def test_geographic_dated_and_differently_qualified_namesakes_remain_blocked(self):
        for title, subject in [('Silver Echo (Cedar City)', 'Silver Echo'),
                               ('Silver Echo (2044 film)', 'Silver Echo'),
                               ('Silver Echo (film)', 'Silver Echo (album)')]:
            with self.subTest(title=title):
                e = source(title, 'Silver Echo is a studio album by Aster Rowan.')
                self.assertEqual(self.check(unit(subject=subject), e, supported()).label, 'UNRESOLVED')

    def test_ambiguous_sources_are_not_rescued_by_a_generic_type(self):
        e = source(entity_resolution='ambiguous')
        self.assertEqual(self.check(unit(), e, supported()).label, 'UNRESOLVED')


class ExactQuoteRepairTests(unittest.IsolatedAsyncioTestCase):
    async def test_unique_whitespace_recovery_retains_raw_reply_and_uses_no_extra_call(self):
        p = unit(subject='')
        raw = {'judgments': [supported(quote='by Aster Rowan')]}
        e = source(text='Silver Echo is a studio album by Aster  Rowan.')
        llm, recorder = Replies(raw), Recorder()
        result = await judge(llm, 'Who sang Silver Echo?', 'en', plan_from_json({'units': [p]}), [e], recorder)
        self.assertEqual(result['u1'].label, 'SUPPORTED')
        self.assertEqual(result['u1'].quotes[0]['text'], 'by Aster  Rowan')
        self.assertEqual(raw['judgments'][0]['quotes'][0]['text'], 'by Aster Rowan')
        self.assertEqual(len(llm.requests), 1)
        self.assertEqual(recorder.events[0]['reply'], raw)

    async def test_completion_can_repair_a_quote_once_on_the_same_visible_sources(self):
        p = unit(subject='')
        units, sources = plan_from_json({'units': [p]}), [source()]
        bad = {'judgments': [supported(quote='Silver Echo ... by Aster Rowan')]}
        good = {'judgments': [supported()]}
        llm = Replies(bad, good)
        llm.repairs_completion_quotes = True
        result = await completion_review(llm, 'Who sang Silver Echo?', 'en', units, sources,
                                         {'u1': Judgment()}, ['u1'], Recorder())
        self.assertEqual(result['u1'].label, 'SUPPORTED')
        self.assertEqual([p for p, _ in llm.requests], ['judge', 'judge_repair'])
        self.assertEqual(llm.requests[1][1]['visible_evidence_ids'], ['e1'])
        self.assertEqual(llm.requests[1][1]['literal_quote_sources'][0]['text'], sources[0].text)

    async def test_quote_repair_cannot_change_the_answer_or_keep_retrying(self):
        units = plan_from_json({'units': [unit(subject='')]})
        bad = {'judgments': [supported(quote='missing text')]}
        for repaired in [bad, {'judgments': [supported(value='Mira')]}]:
            llm = Replies(bad, repaired)
            llm.repairs_completion_quotes = True
            result = await completion_review(llm, 'Who sang Silver Echo?', 'en', units, [source()],
                                             {'u1': Judgment()}, ['u1'], Recorder())
            self.assertEqual(result['u1'].label, 'UNRESOLVED')
            self.assertEqual(len(llm.requests), 2)

    def test_ellipsis_changed_words_repeated_matches_and_invisible_sources_are_not_normalized(self):
        for text in ['Silver Echo ... Aster Rowan', 'by Mira Rowan', 'BY Aster Rowan']:
            raw = {'judgments': [supported(quote=text)]}
            self.assertEqual(literal_quote_whitespace(raw, [source()]), (raw, []))
        repeated = source(text='by Aster  Rowan; by Aster  Rowan')
        raw = {'judgments': [supported()]}
        self.assertEqual(literal_quote_whitespace(raw, [repeated]), (raw, []))
        self.assertEqual(literal_quote_whitespace(raw, []), (raw, []))

    async def test_contract_repair_cannot_turn_a_quote_failure_into_a_semantic_conflict(self):
        units = plan_from_json({'units': [unit(subject='')]})
        llm = Replies({'judgments': [supported(quote='missing text')]},
                      {'judgments': [{'unit_id': 'u1', 'label': 'CONTRADICTED'}]})
        llm.repairs_completion_quotes = True
        recorder = Recorder()
        result = await completion_review(llm, 'Who sang Silver Echo?', 'en', units, [source()],
                                         {'u1': Judgment()}, ['u1'], recorder)
        self.assertEqual(result['u1'].label, 'UNRESOLVED')
        self.assertTrue(any(e['type'] == 'completion_quote_repair_rejected' for e in recorder.events))


class BooleanWordingTests(unittest.TestCase):
    def test_occupation_is_spoken_as_a_predicate_and_keeps_literal_yes(self):
        text = fact_sentences([{'description': "Mira's occupation includes a poet", 'value': 'Yes'}], 'en')
        self.assertEqual(text, 'Yes, Mira is a poet.')

    def test_negative_both_does_not_turn_into_neither(self):
        text = fact_sentences([{'description': 'whether Mira and Liora are both poets', 'value': 'No'}], 'en')
        self.assertIn('No, it is not the case that Mira and Liora are both poets', text)
        self.assertNotIn('are not both', text)
        self.assertNotIn('are both not', text)

    def test_family_negative_keeps_no_for_a_literal_value_scorer(self):
        text = fact_sentences([{'description': 'whether the fictional genera belong to the same family', 'value': 'No'}], 'en')
        self.assertEqual(text, 'No, the fictional genera do not belong to the same family.')


if __name__ == '__main__':
    unittest.main()
