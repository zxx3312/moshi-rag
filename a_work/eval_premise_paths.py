"""Compare old and new candidate validation on identical judge outputs."""
from collections import Counter
from pathlib import Path
import argparse
import json

from turntaking.judge import PromptJudge, normalize_reply, resolve_dependencies
from turntaking.llm import ChatClient, TapeMiss, load_tape
from turntaking.replay import load_jsonl, write_jsonl
from turntaking.schema import Evidence, Observation, SUPPORTED, UNRESOLVED, Unit


def examples():
    """Fictional cases with a controlled evidence snapshot and independent expected results."""
    units = (Unit('u1', 'whether Ari Lane won the Amber Prize', False),
             Unit('u2', 'whether Bea Vale won the Amber Prize', False),
             Unit('u3', 'which candidate won the Amber Prize', True, ('u1', 'u2')))
    source = {'e1': 'Ari Lane is a poet and editor.', 'e2': 'Bea Vale won the Amber Prize.',
              'e3': 'Ari Lane did not win the Amber Prize.', 'e4': 'Ari Lane won the Amber Prize.'}
    plain = 'Which of Ari Lane and Bea Vale won the Amber Prize?'
    unique = 'Exactly one of Ari Lane and Bea Vale won the Amber Prize. Which one?'
    for name, question, ids, label, value, citations, premise in [
        ('omission_only', unique, ('e1',), UNRESOLVED, None, (), False),
        ('direct_confirmation', plain, ('e2',), SUPPORTED, 'Bea Vale', ('e2',), False),
        ('explicit_exclusion', unique, ('e3',), SUPPORTED, 'Bea Vale', ('e3',), True),
        ('omission_plus_direct', plain, ('e1', 'e2'), SUPPORTED, 'Bea Vale', ('e2',), False),
        ('which_of_without_uniqueness', plain, ('e3',), UNRESOLVED, None, (), False),
        ('interrogative_uniqueness', 'Exactly one of Ari Lane and Bea Vale won the Amber Prize?', ('e3',),
         UNRESOLVED, None, (), False),
        ('reject_unconfirmed_choice', plain, ('e4',), SUPPORTED, 'Ari Lane', ('e4',), False),
    ]:
        evidence = tuple(Evidence(eid, source[eid], 0.0, {}) for eid in ids)
        yield name, Observation(name, question, 0.0, evidence, units, False), (label, value, citations, premise)


def states(reply, observation):
    evidence = {e.evidence_id: e for e in observation.evidence}
    legacy, _ = normalize_reply(reply, observation.units, evidence, observation.question)
    strict, _ = normalize_reply(reply, observation.units, evidence, observation.question, candidate_evidence=evidence)
    return (resolve_dependencies(observation.units, legacy), resolve_dependencies(observation.units, strict))


def compare(reply, obs, model, case=None, expected=None):
    old, new = states(reply, obs)
    row = {'model': model, 'sample_id': obs.sample_id, 'visible_ids': [e.evidence_id for e in obs.evidence],
           'case': case, 'changes': [{'unit_id': uid, 'old': vars(old[uid]), 'new': vars(new[uid])}
                                     for uid in old if old[uid] != new[uid]]}
    if expected is not None:
        def result(j):
            return (j.label, j.value, j.citations, j.by_presupposition)
        row.update(expected=expected, old_pass=result(old['u3']) == expected, new_pass=result(new['u3']) == expected,
                   old=vars(old['u3']), new=vars(new['u3']), raw_reply=reply)
    return row


def debug_observations(traces, run):
    lookup = {}
    for t in load_jsonl(traces):
        # Sentence IDs and text are shared across the three debug schedules.
        lookup.setdefault(t['sample_id'], t)
    units = {r['sample_id']: tuple(Unit(u['unit_id'], u['description'], u['necessary'], tuple(u['depends_on']))
                                  for u in r['units']) for r in load_jsonl(run / 'decompositions.jsonl')}
    seen = set()
    for call in load_jsonl(run / 'judge_calls.jsonl'):
        sid = call['sample_id']
        key = sid, tuple(call['evidence'])
        if key in seen or not call['evidence']:
            continue
        seen.add(key)
        trace = lookup[sid]
        events = {e['evidence_id']: e for e in trace['events']}
        evidence = tuple(Evidence(e['evidence_id'], e['text'], 0.0, e['source'])
                         for e in (events[eid] for eid in call['evidence']))
        yield Observation(sid, trace['question'], call['time_s'], evidence, units[sid], False)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--trace', type=Path, required=True, help='Approved debug traces.')
    ap.add_argument('--recorded-prompt', type=Path, required=True)
    ap.add_argument('--recorded-lora', type=Path, required=True)
    ap.add_argument('--base-url')
    ap.add_argument('--model', default='Qwen/Qwen3-14B')
    ap.add_argument('--judge-base-url')
    ap.add_argument('--judge-model', default='judge')
    args = ap.parse_args()
    rows, unmatched = [], Counter()
    for name, run, endpoint, model in [('prompt', args.recorded_prompt, args.base_url, args.model),
                                     ('lora', args.recorded_lora, args.judge_base_url, args.judge_model)]:
        replay = None if endpoint else load_tape([run / 'llm_calls.jsonl'])
        client = ChatClient(endpoint or '', model, replay=replay,
                            extra_body={'chat_template_kwargs': {'enable_thinking': False}})
        judge = PromptJudge(client, with_examples=name == 'prompt', strict_candidate_paths=True)
        if endpoint:
            for case, obs, expected in examples():
                judge.judge(obs)
                rows.append(compare(judge.log[-1]['reply'], obs, name, case, expected))
        for obs in debug_observations(args.trace, run):
            try:
                judge.judge(obs)
            except TapeMiss:
                # v7 can log a snapshot for the gold units only. Never evaluate its reply as model units.
                unmatched[name] += 1
                continue
            rows.append(compare(judge.log[-1]['reply'], obs, name))
        write_jsonl(args.out / f'{name}_judge_calls.jsonl', judge.log)
    write_jsonl(args.out / 'candidate_path_comparisons.jsonl', rows)
    summary = {}
    for name in ('prompt', 'lora'):
        debug = [r for r in rows if r['model'] == name and r['case'] is None]
        cases = [r for r in rows if r['model'] == name and r['case'] is not None]
        summary[name] = {'debug_questions': len({r['sample_id'] for r in debug}), 'debug_snapshots': len(debug),
                         'unmatched_recorded_requests': unmatched[name],
                         'changed_debug_snapshots': sum(bool(r['changes']) for r in debug),
                         'debug_label_changes': dict(Counter(c['old']['label'] + ' -> ' + c['new']['label']
                             for r in debug for c in r['changes'] if c['old']['label'] != c['new']['label'])),
                         'synthetic': {r['case']: {'old_pass': r['old_pass'], 'new_pass': r['new_pass']}
                                       for r in cases}}
    summary['mode'] = 'live_models' if args.base_url or args.judge_base_url else 'saved_debug_replies'
    output = json.dumps(summary, ensure_ascii=False, indent=2)
    (args.out / 'summary.json').write_text(output + '\n', encoding='utf-8')
    print(output)


if __name__ == '__main__':
    main()
