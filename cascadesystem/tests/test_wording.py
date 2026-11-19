"""Speech wording must keep approved values and avoid internal task labels."""
from copy import deepcopy
import unittest

from cascadesystem.config import Settings
from cascadesystem.controller import Cascade
from cascadesystem.tests.test_grounding import NoSearch, ScopeLLM, document, stream_batches
from cascadesystem.wording import fact_sentences, label_style, missing_sentence


class WordingTests(unittest.TestCase):
    def test_english_fact_has_subject_and_predicate_without_changing_approved_name(self):
        facts = [{'description': 'Identify the father of Mira', 'value': 'Aster Rowan, Captain of the Silver Ship'}]
        before = deepcopy(facts)
        text = fact_sentences(facts, 'en')
        self.assertEqual(text, 'The father of Mira is Aster Rowan, Captain of the Silver Ship.')
        self.assertEqual(facts, before)
        self.assertFalse(label_style(text, facts))

    def test_chinese_fact_is_a_sentence_and_preserves_the_date(self):
        facts = [{'description': '查询银舟号的发射日期', 'value': '2044年5月4日'}]
        self.assertEqual(fact_sentences(facts, 'zh'), '银舟号的发射日期是2044年5月4日。')
        self.assertEqual(missing_sentence(['查询银舟号的返回日期'], 'zh'), '我目前还无法确认银舟号的返回日期。')

    def test_label_detection_does_not_forbid_colons_in_real_times_or_titles(self):
        facts = [{'description': 'return time of Silver Ship', 'value': '12:30'}]
        self.assertFalse(label_style('Silver Ship returned at 12:30.', facts))
        self.assertTrue(label_style('return time of Silver Ship: 12:30', facts))
        title = [{'description': 'director of Silver Ship: Dawn', 'value': 'Mira'}]
        self.assertFalse(label_style('Mira directed Silver Ship: Dawn.', title))

    def test_missing_information_is_first_person_uncertainty_without_an_invented_value(self):
        text = missing_sentence(['Find the return date of Silver Ship'], 'en')
        self.assertEqual(text, 'I could not confirm the return date of Silver Ship.')
        self.assertNotIn(':', text)


class NaturalOutputTests(unittest.IsolatedAsyncioTestCase):
    async def test_label_draft_falls_back_to_complete_sentences_and_is_still_verified(self):
        class Labels(ScopeLLM):
            async def complete(self, purpose, system, payload):
                if purpose == 'generate':
                    self.requests.append((purpose, deepcopy(payload)))
                    return {'text': ' '.join(f"{f['description']}: {f['value']}." for f in payload['APPROVED_FACTS'])}
                return await super().complete(purpose, system, payload)
        llm = Labels()
        result = await Cascade(llm, NoSearch(), Settings()).run('When did the fictional Silver Ship launch and return?',
            evidence_stream=stream_batches([document('d1', 'The Silver Ship launched in 2044.')],
                                           [document('d2', 'The Silver Ship returned in 2045.')]))
        answers = [e for e in result['events'] if e['type'] == 'utterance' and e.get('claims')]
        self.assertEqual(result['status'], 'complete')
        self.assertEqual(len(answers), 2)
        self.assertTrue(all(e['fallback'] for e in answers))
        self.assertTrue(all(' is ' in e['text'] for e in answers))
        self.assertTrue(all(not label_style(e['text'], e['claims']) for e in answers))
        checks = [p for purpose, p in llm.requests if purpose == 'verify']
        self.assertEqual(len(checks), 2)
        self.assertIn('2044', checks[0]['draft'])
        self.assertIn('2045', checks[1]['draft'])


if __name__ == '__main__':
    unittest.main()
