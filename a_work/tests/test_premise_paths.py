"""The agreed binary rule exercised through the shared judge and dependency resolver."""
import sys
import unittest
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from eval_premise_paths import examples
from turntaking.judge import PromptJudge, resolve_dependencies
from turntaking.llm import FakeClient
from turntaking.schema import Evidence, Unit, SUPPORTED, UNRESOLVED


def judgment(uid, value, cites=(), *, omitted=False, premise=False):
    return {'unit_id': uid, 'value': value, 'label': SUPPORTED if value is not None else UNRESOLVED,
            'citations': list(cites), 'by_omission': omitted, 'by_presupposition': premise}


class PremisePathsTest(unittest.TestCase):
    cases = {name: (obs, expected) for name, obs, expected in examples()}

    def evaluate(self, obs, *items):
        judge = PromptJudge(FakeClient([{'units': items}]), strict_candidate_paths=True)
        result = resolve_dependencies(obs.units, judge.judge(obs))
        return result, judge.log[0]['candidate_paths']

    def fixture(self, case, a, b, winner='Bea Vale'):
        obs, expected = self.cases[case]
        result, paths = self.evaluate(obs, a, b, judgment('u3', winner, premise=True))
        actual = result['u3']
        self.assertEqual((actual.label, actual.value, actual.citations, actual.by_presupposition), expected)
        return paths

    def test_agreed_cases(self):
        absent_a, absent_b = judgment('u1', None), judgment('u2', None)
        omission = judgment('u1', 'no', ('e1',), omitted=True)
        direct_b = judgment('u2', 'yes', ('e2',))
        explicit_no = judgment('u1', 'no', ('e3',))
        self.assertEqual(self.fixture('omission_only', omission, absent_b), {})
        direct = self.fixture('direct_confirmation', absent_a, direct_b)
        self.assertEqual(direct['u3'], {'kind': 'direct', 'depends_on': ['u2'], 'citations': ['e2']})
        exclusion = self.fixture('explicit_exclusion', explicit_no, absent_b)
        self.assertEqual(exclusion['u3'], {'kind': 'exclusion', 'depends_on': ['u1'], 'citations': ['e3']})
        self.assertEqual(self.fixture('omission_plus_direct', omission, direct_b), direct)
        self.fixture('which_of_without_uniqueness', explicit_no, absent_b)
        self.fixture('interrogative_uniqueness', explicit_no, absent_b)
        self.fixture('reject_unconfirmed_choice', judgment('u1', 'yes', ('e4',)), absent_b, winner='Ari Lane')

    def test_unmarked_or_wrong_subject_negative_cannot_license_answer(self):
        for statement in ('Ari Lane is a poet.', 'Cora Venn did not win the Amber Prize.',
                          'Ari Lane may not have won the Amber Prize.'):
            with self.subTest(statement=statement):
                obs, _ = self.cases['explicit_exclusion']
                obs = replace(obs, evidence=(Evidence('e3', statement, 0, {}),))
                result, _ = self.evaluate(obs, judgment('u1', 'no', ('e3',)), judgment('u3', 'Bea Vale', premise=True))
                self.assertEqual(result['u3'].label, UNRESOLVED)

    def test_cannot_use_omission_through_an_intermediate_unit(self):
        obs, _ = self.cases['explicit_exclusion']
        obs = replace(obs, units=(Unit('u0', 'source of negative inference', False),
                                   replace(obs.units[0], depends_on=('u0',)), *obs.units[1:]))
        result, _ = self.evaluate(obs, judgment('u0', 'no', ('e3',), omitted=True),
                                  judgment('u1', 'no', ('e3',)), judgment('u3', 'Bea Vale', premise=True))
        self.assertEqual(result['u3'].label, UNRESOLVED)

    def test_positive_on_wrong_candidate_cannot_license_answer(self):
        obs, _ = self.cases['reject_unconfirmed_choice']
        result, _ = self.evaluate(obs, judgment('u1', 'yes', ('e4',)), judgment('u3', 'Bea Vale', premise=True))
        self.assertEqual(result['u3'].label, UNRESOLVED)

    def test_both_question_keeps_conjunctive_rule(self):
        obs, _ = self.cases['omission_plus_direct']
        obs = replace(obs, question='Were Ari Lane and Bea Vale both winners of the Amber Prize?')
        result, paths = self.evaluate(obs, judgment('u1', 'no', ('e1',), omitted=True),
                                      judgment('u2', 'yes', ('e2',)), judgment('u3', 'no'))
        self.assertEqual((result['u3'].label, result['u3'].value, paths), (SUPPORTED, 'no', {}))
