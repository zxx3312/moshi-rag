"""Fictional regression cases: a matching value does not locate a relation."""
from pathlib import Path
import sys
import unittest

EVAL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EVAL))
sys.path.insert(0, str(EVAL.parent))
from eval_replay import policy_rows


class ClaimContextTests(unittest.TestCase):
    def rows(self, text, facts):
        run = {'status': 'complete', 'events': [{'type': 'utterance', 'sequence': 0,
               'action': 'Final Answer', 'time_s': 1, 'text': text,
               'claims': [{'unit_id': f'u{i}', 'value': v, 'citations': ['d1s0']}
                          for i, v in enumerate(facts, 1)]}]}
        trace = {'schema_version': '1.0', 'data_version': 'debug-v0', 'sample_id': 'fiction',
                 'trace_id': 'fiction_short', 'time_origin': 'question_end', 'clock': 'simulated'}
        return policy_rows(run, trace)[0][0]['claim_spans']

    def test_same_value_for_two_people_does_not_select_the_first_person_twice(self):
        text = 'Mira is Asterian. Liora is Asterian.'
        spans = self.rows(text, ['Asterian', 'Asterian'])
        self.assertTrue(all(s['text'] == text for s in spans))
        self.assertTrue(all(s['span_basis'] == 'utterance_context_unaligned' for s in spans))

    def test_comparison_winner_is_not_attached_to_an_earlier_biographical_sentence(self):
        text = 'Mira was born in 2044. Liora was born in 2040. Mira was born later.'
        spans = self.rows(text, ['2044', '2040', 'Mira'])
        self.assertEqual(spans[2]['text'], text)
        self.assertIn('Mira was born later.', spans[2]['text'])

    def test_unique_unshared_values_can_keep_their_individual_sentences(self):
        text = 'The Silver Ship launched in 2044. It returned in 2045.'
        spans = self.rows(text, ['2044', '2045'])
        self.assertEqual(spans[0]['text'], 'The Silver Ship launched in 2044.')
        self.assertEqual(spans[1]['text'], 'It returned in 2045.')
        self.assertTrue(all(s['span_basis'] == 'unique_value_sentence' for s in spans))

    def test_unspoken_metadata_is_not_added_to_text_or_given_an_audio_time(self):
        text = 'The evidence is not conclusive.'
        span = self.rows(text, ['Aster'])[0]
        self.assertEqual(span['text'], text)
        self.assertNotIn('Aster', span['text'])
        self.assertIsNone(span['start'])
        self.assertIsNone(span['end'])


if __name__ == '__main__':
    unittest.main()
