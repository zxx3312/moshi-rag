"""Fictional namesake and verifier regression cases; no benchmark inputs."""
from urllib.parse import parse_qs, urlsplit
import unittest

from cascadesystem.config import Settings
from cascadesystem.controller import Cascade
from cascadesystem.models import Evidence, plan_from_json, validate_judgments
from cascadesystem.search import WikipediaSearch
from cascadesystem.transport import ProviderError


def page(title, text='The Silver Tower is in Aster City.', **extra):
    return {'title': title, 'extract': text, 'fullurl': 'https://example.invalid/' + title.replace(' ', '_'), **extra}


class EntityHTTP:
    def __init__(self, primary, candidates, fail_title=False):
        self.primary, self.candidates, self.fail_title = primary, candidates, fail_title
        self.requests = []

    def json(self, url, **kwargs):
        params = parse_qs(urlsplit(url).query)
        self.requests.append(params)
        if 'titles' in params:
            if self.fail_title:
                raise ProviderError('simulated title lookup outage')
            rows = self.primary
        else:
            rows = self.candidates
        return {'query': {'pages': rows}}


def plan(subject='Silver Tower', queries=None):
    return {'units': [{'unit_id': 'u1', 'description': 'The city containing the Silver Tower',
                       'subject': subject, 'necessary': True, 'depends_on': [],
                       'queries': queries or ['Silver Tower city']}]}


def judgment(value='Cedar City'):
    return {'judgments': [{'unit_id': 'u1', 'label': 'SUPPORTED', 'value': value,
                           'citations': ['e1'], 'quotes': [{'evidence_id': 'e1', 'text': 'The replica is in Cedar City.'}]}]}


class EntityValidationTests(unittest.TestCase):
    def test_real_quote_about_namesake_cannot_answer_original(self):
        units = plan_from_json(plan())
        evidence = [Evidence('e1', 'Silver Tower (Cedar City)', 'https://example.invalid/replica',
                             'The replica is in Cedar City.', 1)]
        result = validate_judgments(judgment(), units, evidence)
        self.assertEqual(result['u1'].label, 'UNRESOLVED')
        self.assertIn('entity identity', result['u1'].reason)

    def test_explicitly_requested_namesake_is_valid(self):
        units = plan_from_json(plan('Silver Tower (Cedar City)'))
        evidence = [Evidence('e1', 'Silver Tower (Cedar City)', 'https://example.invalid/replica',
                             'The replica is in Cedar City.', 1)]
        self.assertEqual(validate_judgments(judgment(), units, evidence)['u1'].label, 'SUPPORTED')

    def test_ambiguous_title_needs_disambiguation(self):
        units = plan_from_json(plan())
        evidence = [Evidence('e1', 'Silver Tower', 'https://example.invalid/tower',
                             'The replica is in Cedar City.', 1, 'Silver Tower', 'Silver Tower', 'ambiguous')]
        self.assertEqual(validate_judgments(judgment(), units, evidence)['u1'].label, 'UNRESOLVED')


class EntitySearchTests(unittest.IsolatedAsyncioTestCase):
    async def test_primary_article_precedes_search_and_replica_is_excluded(self):
        http = EntityHTTP([page('Silver Tower')], [page('Silver Tower (Cedar City)'), page('Silver Tower')])
        provider = WikipediaSearch(Settings(), http)
        rows = await provider.search_subject('Silver Tower location city', 'Silver Tower')
        self.assertEqual([r['title'] for r in rows], ['Silver Tower'])
        self.assertEqual(rows[0]['entity_resolution'], 'primary')
        self.assertEqual(provider.diagnostics[0]['excluded_titles'], ['Silver Tower (Cedar City)'])

    async def test_explicit_qualified_entity_is_not_filtered_out(self):
        title = 'Silver Tower (Cedar City)'
        rows = await WikipediaSearch(Settings(), EntityHTTP([page(title)], [page(title)])).search_subject('Silver Tower city', title)
        self.assertEqual(rows[0]['title'], title)
        self.assertEqual(rows[0]['entity_resolution'], 'primary')

    async def test_title_redirect_uses_resolved_name(self):
        provider = WikipediaSearch(Settings(), EntityHTTP([page('Silver Tower')], []))
        rows = await provider.search_subject('Silver Spire location', 'Silver Spire')
        self.assertEqual(rows[0]['requested_subject'], 'Silver Spire')
        self.assertEqual(rows[0]['resolved_title'], 'Silver Tower')
        await provider.search_subject('Silver Spire opening date', 'Silver Spire')
        self.assertEqual(sum('titles' in p for p in provider.http.requests), 1)

    async def test_disambiguation_page_is_not_a_primary_fact_source(self):
        provider = WikipediaSearch(Settings(), EntityHTTP([page('Silver Tower', pageprops={'disambiguation': ''})], [page('Silver Tower (Cedar City)')]))
        rows = await provider.search_subject('Silver Tower city', 'Silver Tower')
        self.assertEqual(rows[0]['entity_resolution'], 'ambiguous')
        self.assertEqual(provider.diagnostics[0]['title_lookup'], 'ambiguous')

    async def test_title_lookup_failure_keeps_search_and_records_failure(self):
        provider = WikipediaSearch(Settings(), EntityHTTP([], [page('Silver Tower')], fail_title=True))
        rows = await provider.search_subject('Silver Tower city', 'Silver Tower')
        self.assertTrue(rows)
        self.assertEqual(provider.diagnostics[0]['title_lookup'], 'error')


class FactReviewLLM:
    def __init__(self, recover=False):
        self.verifications = 0
        self.recover = recover

    async def complete(self, purpose, system, payload):
        if purpose == 'decompose':
            return plan(queries=['Silver Tower city', 'Silver Tower primary article'])
        if purpose == 'judge':
            return judgment()
        if purpose == 'generate':
            return {'text': 'The Silver Tower is in Cedar City.'}
        if purpose == 'verify':
            self.verifications += 1
            return {'approved': True, 'facts_valid': self.recover and self.verifications > 1,
                    'reason': 'The approved facts must concern the requested entity.'}
        raise AssertionError(purpose)


class FactReviewSearch:
    async def search(self, query):
        return [{'title': 'Silver Tower', 'url': 'https://example.invalid/tower',
                 'text': 'The replica is in Cedar City.'}]


class FactReviewTests(unittest.IsolatedAsyncioTestCase):
    async def test_rejected_facts_never_reach_fallback_speech(self):
        result = await Cascade(FactReviewLLM(), FactReviewSearch(), Settings()).run('Which city contains the Silver Tower?')
        self.assertEqual(result['status'], 'incomplete')
        self.assertTrue(any(e['type'] == 'facts_rejected' for e in result['events']))
        self.assertFalse(any(e.get('claims') for e in result['events'] if e['type'] == 'utterance'))

    async def test_rejected_facts_trigger_alternative_query(self):
        result = await Cascade(FactReviewLLM(recover=True), FactReviewSearch(), Settings()).run('Which city contains the Silver Tower?')
        self.assertEqual(result['status'], 'complete')
        self.assertEqual(len(result['searches']), 2)
        finals = [e for e in result['events'] if e.get('action') == 'Final Answer']
        self.assertEqual(len(finals), 1)
        self.assertTrue(finals[0]['claims'])


if __name__ == '__main__':
    unittest.main()
