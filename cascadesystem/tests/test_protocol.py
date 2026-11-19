"""Fictional output-contract regressions; no benchmark examples or network calls."""
import asyncio
from copy import deepcopy
from dataclasses import replace
import unittest

from cascadesystem.config import Settings
from cascadesystem.controller import Cascade
from cascadesystem.demo import DemoLLM, DemoSearch, QUESTION
from cascadesystem.models import Evidence, plan_from_json
from cascadesystem.protocol import decompose, explicit_dependencies, judge, judgment_contract
from cascadesystem.transport import ProviderError


def plan():
    return {'units': [
        {'unit_id': 'u1', 'description': 'Captain of the fictional Silver Ship', 'necessary': False,
         'depends_on': [], 'queries': ['Silver Ship captain']},
        {'unit_id': 'u2', 'description': 'Birth year of {u1}', 'necessary': True,
         'depends_on': ['u1'], 'queries': ['{u1} birth year']}]}


def judgment_rows():
    return {'judgments': [{'unit_id': 'u1', 'label': 'UNRESOLVED'}, {'unit_id': 'u2', 'label': 'UNRESOLVED'}]}


class Recorder:
    def __init__(self):
        self.events = []
    async def __call__(self, kind, **data):
        self.events.append({'type': kind, **data})


class Replies:
    def __init__(self, *rows):
        self.rows = iter(rows)
        self.requests = []
    async def complete(self, purpose, system, payload):
        self.requests.append((purpose, deepcopy(payload)))
        reply = next(self.rows)
        if isinstance(reply, Exception):
            raise reply
        return deepcopy(reply)


class DependencyTests(unittest.TestCase):
    def test_only_explicit_known_dependencies_are_added_without_mutating_the_plan(self):
        original = plan()
        original['units'][1]['depends_on'] = []
        original['units'][1]['subject'] = '{u1}'
        repaired, changes = explicit_dependencies(original)
        self.assertEqual(original['units'][1]['depends_on'], [])
        self.assertEqual(repaired['units'][1]['depends_on'], ['u1'])
        self.assertEqual(changes, [{'unit_id': 'u2', 'added_dependencies': ['u1']}])
        self.assertEqual(repaired['units'][1]['queries'], original['units'][1]['queries'])
        self.assertEqual(len(plan_from_json(repaired)), 2)
        with self.assertRaises(ValueError):
            plan_from_json(original)  # The strict validator has not been weakened.

    def test_unknown_or_self_references_are_not_completed_by_guessing(self):
        for target in ['u2', 'u99']:
            original = plan()
            original['units'][1]['depends_on'] = []
            original['units'][1]['queries'] = ['{' + target + '} birth year']
            _, changes = explicit_dependencies(original)
            self.assertFalse(changes)

    def test_shape_diagnostics_distinguish_missing_duplicate_and_extra_ids(self):
        details = judgment_contract({'judgments': [{'unit_id': 'u1'}, {'unit_id': 'u1'}, {'unit_id': 'u9'}, {}]}, plan_from_json(plan()))
        self.assertEqual(details['missing_unit_ids'], ['u2'])
        self.assertEqual(details['duplicate_unit_ids'], ['u1'])
        self.assertEqual(details['unexpected_unit_ids'], ['u9'])
        self.assertEqual(details['malformed_rows'], 1)


class PlanRepairTests(unittest.IsolatedAsyncioTestCase):
    async def test_known_placeholder_omission_is_repaired_without_an_extra_api_call(self):
        initial = plan()
        initial['units'][1]['depends_on'] = []
        client, recorder = Replies(initial), Recorder()
        units = await decompose(client, 'When was the fictional captain born?', 'en', Settings(), recorder)
        self.assertEqual(units[1].depends_on, ('u1',))
        self.assertEqual(len(client.requests), 1)
        self.assertTrue(any(e['type'] == 'protocol_normalized' for e in recorder.events))
        self.assertEqual(recorder.events[0]['reply'], initial)

    async def test_other_invalid_plans_receive_one_full_rewrite(self):
        initial = plan()
        initial['units'][1]['unit_id'] = 'u1'
        client, recorder = Replies(initial, plan()), Recorder()
        units = await decompose(client, 'A fictional question?', 'en', Settings(), recorder)
        self.assertEqual([u.unit_id for u in units], ['u1', 'u2'])
        self.assertEqual([r[0] for r in client.requests], ['decompose', 'decompose_repair'])
        self.assertIn('validation_error', client.requests[1][1])
        self.assertEqual(client.requests[1][1]['question'], 'A fictional question?')

    async def test_cycles_remain_invalid_and_repair_attempts_are_bounded(self):
        initial = plan()
        initial['units'][0]['depends_on'] = ['u2']
        client, recorder = Replies(initial, initial), Recorder()
        with self.assertRaisesRegex(ValueError, 'cycle'):
            await decompose(client, 'A fictional question?', 'en', Settings(), recorder)
        self.assertEqual(len(client.requests), 2)
        self.assertTrue(any(e['type'] == 'protocol_repair_exhausted' for e in recorder.events))

    async def test_provider_failure_does_not_trigger_a_repair_request(self):
        client = Replies(ProviderError('HTTP 401 from example.invalid'))
        with self.assertRaises(ProviderError):
            await decompose(client, 'A question?', 'en', Settings(), Recorder())
        self.assertEqual(len(client.requests), 1)


class JudgeRepairTests(unittest.IsolatedAsyncioTestCase):
    async def test_missing_duplicate_extra_and_non_object_replies_are_repaired(self):
        variants = [
            {'judgments': [{'unit_id': 'u1', 'label': 'UNRESOLVED'}]},
            {'judgments': judgment_rows()['judgments'] + [{'unit_id': 'u1', 'label': 'UNRESOLVED'}]},
            {'judgments': judgment_rows()['judgments'] + [{'unit_id': 'u3', 'label': 'UNRESOLVED'}]},
            ['invalid root'],
        ]
        for initial in variants:
            with self.subTest(initial=initial):
                client, recorder = Replies(initial, judgment_rows()), Recorder()
                result = await judge(client, 'A question?', 'en', plan_from_json(plan()), [], recorder)
                self.assertEqual(set(result), {'u1', 'u2'})
                self.assertEqual([r[0] for r in client.requests], ['judge', 'judge_repair'])
                self.assertEqual(client.requests[1][1]['required_unit_ids'], ['u1', 'u2'])
                self.assertEqual(recorder.events[0]['reply'], initial)

    async def test_invalid_second_reply_is_not_silently_filled_from_old_state(self):
        initial = {'judgments': [{'unit_id': 'u1', 'label': 'UNRESOLVED'}]}
        client, recorder = Replies(initial, initial), Recorder()
        with self.assertRaisesRegex(ValueError, 'every unit'):
            await judge(client, 'A question?', 'en', plan_from_json(plan()), [], recorder)
        self.assertEqual(len(client.requests), 2)
        failure = next(e for e in recorder.events if e['type'] == 'protocol_validation_failed')
        self.assertEqual(failure['missing_unit_ids'], ['u2'])

    async def test_invalid_citations_cannot_become_supported_after_repair(self):
        units = plan_from_json({'units': [{**plan()['units'][0], 'necessary': True}]})
        invalid = {'judgments': [{'unit_id': 'u1', 'label': 'SUPPORTED', 'value': 'Aster',
                                  'citations': ['future'], 'quotes': [{'evidence_id': 'future', 'text': 'Aster'}]}]}
        source = Evidence('e1', 'Fiction', 'https://example.invalid', 'The captain is Aster.', 0)
        client = Replies(invalid, invalid)
        result = await judge(client, 'Who is captain?', 'en', units, [source], Recorder())
        self.assertEqual(result['u1'].label, 'UNRESOLVED')
        self.assertEqual(result['u1'].value, '')
        self.assertEqual(client.requests[1][1]['visible_evidence_ids'], ['e1'])
        self.assertNotIn('future', [e['evidence_id'] for e in client.requests[1][1]['evidence']])

    async def test_bad_quote_then_structural_failure_does_not_get_a_second_repair(self):
        units = plan_from_json({'units': [{**plan()['units'][0], 'necessary': True}]})
        invalid = {'judgments': [{'unit_id': 'u1', 'label': 'SUPPORTED', 'value': 'Aster',
                                  'citations': ['e1'], 'quotes': [{'evidence_id': 'e1', 'text': 'invented'}]}]}
        client = Replies(invalid, {'judgments': []})
        with self.assertRaises(ValueError):
            await judge(client, 'Who is captain?', 'en', units,
                        [Evidence('e1', 'Fiction', 'https://example.invalid', 'The captain is Aster.', 0)], Recorder())
        self.assertEqual(len(client.requests), 2)


class ControllerRepairTests(unittest.IsolatedAsyncioTestCase):
    async def test_completed_future_search_is_not_visible_to_a_repair(self):
        class MissingRow(DemoLLM):
            snapshots = []
            async def complete(self, purpose, system, payload):
                raw = await super().complete(purpose, system, payload)
                if purpose == 'judge' and len(payload['evidence']) == 1:
                    raw['judgments'] = raw['judgments'][:1]
                if purpose == 'judge_repair':
                    await asyncio.sleep(0.3)  # The next search finishes while the first snapshot is repaired.
                    self.snapshots.append(deepcopy(payload['evidence']))
                return raw
        client = MissingRow()
        result = await Cascade(client, DemoSearch(), Settings()).run(QUESTION)
        self.assertEqual(result['status'], 'complete')
        self.assertEqual([e['evidence_id'] for e in client.snapshots[0]], ['e1'])
        failed_reply = next(e for e in result['events'] if e['type'] == 'judge_reply')
        self.assertEqual(len(failed_reply['reply']['judgments']), 1)

    async def test_unrepairable_judge_never_releases_even_its_valid_subset(self):
        class MissingRow(DemoLLM):
            repairs = 0
            async def complete(self, purpose, system, payload):
                raw = await super().complete(purpose, system, payload)
                if purpose in {'judge', 'judge_repair'}:
                    raw['judgments'] = raw['judgments'][:1]
                    self.repairs += purpose == 'judge_repair'
                return raw
        client = MissingRow()
        result = await Cascade(client, DemoSearch(), Settings()).run(QUESTION)
        self.assertEqual(result['status'], 'error')
        self.assertEqual(client.repairs, 1)
        self.assertFalse(result['output_enqueued_units'])
        self.assertFalse(any(e.get('claims') for e in result['events'] if e['type'] == 'utterance'))


if __name__ == '__main__':
    unittest.main()
