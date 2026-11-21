"""Decompose the unique questions in B's actual SFT splits, without modifying B."""
import argparse
from collections import Counter
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import subprocess
from turntaking.decompose import decompose
from turntaking.llm import ChatClient


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, obj):
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')
    temp.replace(path)


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', '<br>')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--b-root', type=Path, required=True)
    ap.add_argument('--export-dir', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--base-url', default='http://127.0.0.1:8000/v1')
    ap.add_argument('--model', default='Qwen/Qwen3-14B')
    ap.add_argument('--prepare-only', action='store_true')
    ap.add_argument('--local-model', type=Path)
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    args.export_dir.mkdir(parents=True, exist_ok=True)
    base = args.b_root / 'b_work/step4'
    paths = [base/'sft/sft_train.jsonl', base/'sft/sft_dev.jsonl',
             base/'prepared/samples_sft_candidates.jsonl', base/'gold_sft.jsonl']
    hashes = {str(p): digest(p) for p in paths}
    samples = {r['sample_id']: r for r in read_jsonl(paths[2])}
    gold = {r['sample_id']: r for r in read_jsonl(paths[3])}
    questions, seen = [], set()
    for split, path in zip(('train', 'dev'), paths[:2]):
        grouped = {}
        for row in read_jsonl(path):
            sid = row['metadata']['sample_id']
            assert row['metadata']['split'] == split
            # Read the question actually used by SFT; cross-check the source record.
            content = row['messages'][-2]['content']
            assert content.startswith('Question: ')
            question = content[len('Question: '):].split('\n\nUnits:\n', 1)[0]
            assert question == samples[sid]['question'], sid
            assert samples[sid]['project_split'] == split, sid
            if sid in grouped:
                assert grouped[sid]['question'] == question
                grouped[sid]['sft_snapshot_count'] += 1
            else:
                grouped[sid] = dict(sample_id=sid, split=split, question=question,
                                    sft_snapshot_count=1)
        assert not seen.intersection(grouped), 'train/dev overlap'
        seen.update(grouped)
        questions.extend(grouped.values())
    assert seen == set(gold), 'SFT IDs do not match selected gold'
    write_json(args.export_dir/'questions.json', questions)
    source = Path(__file__).parent/'turntaking/decompose.py'
    meta = dict(backend='transformers-greedy-unconstrained' if args.local_model else 'vllm-json-schema', model_path=str(args.local_model) if args.local_model else None, model=args.model, temperature=0, enable_thinking=False, max_tokens=1024,
                a_commit=subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
                b_commit=subprocess.check_output(['git', '-C', str(args.b_root), 'rev-parse', 'HEAD'], text=True).strip(),
                decomposer_sha256=digest(source), source_sha256=hashes,
                question_counts=dict(Counter(q['split'] for q in questions)),
                note='Model sees question only. Draft units, not reviewed gold or rebuilt SFT targets.')
    manifest_path = args.export_dir/'manifest.json'
    if manifest_path.exists():
        old = json.loads(manifest_path.read_text())
        for key in meta:
            assert old[key] == meta[key], f'resume configuration changed: {key}'
    write_json(manifest_path, meta)
    print(json.dumps(meta['question_counts']), flush=True)
    if args.prepare_only:
        return
    checkpoint = args.export_dir/'decompositions.jsonl'
    done = {r['sample_id']: r for r in read_jsonl(checkpoint)} if checkpoint.exists() else {}
    if len(done) == len(questions):
        client = None
    elif args.local_model:
        from turntaking.local_decompose_client import LocalDecomposeClient
        client = LocalDecomposeClient(str(args.local_model), [q['question'] for q in questions if q['sample_id'] not in done])
    else:
        client = ChatClient(args.base_url, args.model,
                            extra_body={'chat_template_kwargs': {'enable_thinking': False}}, max_tokens=1024)
    with checkpoint.open('a') as output, (args.out/'llm_calls.jsonl').open('a') as tape:
        for q in questions:
            if q['sample_id'] in done:
                assert done[q['sample_id']]['question'] == q['question']
                continue
            qtype, units, fallback = decompose(q['question'], client)
            record = dict(q, question_type=qtype, units=[asdict(u) for u in units],
                          fell_back=fallback, status='needs_review',
                          latency_s=client.calls[-1].latency_s)
            output.write(json.dumps(record, ensure_ascii=False)+'\n'); output.flush()
            tape.write(json.dumps(client.tape[-1], ensure_ascii=False)+'\n'); tape.flush()
            done[q['sample_id']] = record
            print(f"{len(done)}/{len(questions)} {q['sample_id']} {qtype} fallback={fallback}", flush=True)
    for split in ('train', 'dev'):
        records = [done[q['sample_id']] for q in questions if q['split'] == split]
        write_json(args.export_dir/f'{split}.json', dict(annotation_version='a-decompose-v1',
                   status='needs_review', records=records))
        lines = [f'# {split}: A decomposer review', '',
                 '模型仅看到问题。新单元未经人工复核；旧 gold 仅供对照，不作为新单元标签。', '']
        for index, r in enumerate(records, 1):
            lines += [f"## {index}. {r['sample_id']}", '', f"Question: {r['question']}", '',
                      f"Type: {r['question_type']} · fallback: {r['fell_back']} · SFT snapshots: {r['sft_snapshot_count']}", '',
                      '### New decomposer units', '', '| ID | Description | Necessary | Depends on |',
                      '|---|---|---|---|']
            for u in r['units']:
                lines.append('| '+' | '.join(cell(u[k]) for k in ('unit_id','description','necessary','depends_on'))+' |')
            lines += ['', '### Original human gold (reference only)', '',
                      '| ID | Description | Necessary | Depends on | Expected answer | Support sets |',
                      '|---|---|---|---|---|---|']
            for u in gold[r['sample_id']]['units']:
                lines.append('| '+' | '.join(cell(u.get(k,'')) for k in ('unit_id','description','necessary','depends_on','expected_answer','support_sets'))+' |')
            lines += ['', '### Source documents (reference only)', '']
            for document_id, (title, sentences) in enumerate(samples[r['sample_id']]['context'], 1):
                lines += [f'**d{document_id}: {cell(title)}**', '']
                lines += [f'- [d{document_id}s{i}] {sentence}' for i, sentence in enumerate(sentences)]
                lines.append('')
        (args.export_dir/f'{split}.md').write_text('\n'.join(lines)+'\n')
    assert all(digest(Path(p)) == h for p,h in hashes.items()), 'B input changed during run'
    meta.update(completed=True, fallback_count=sum(r['fell_back'] for r in done.values()),
                question_types=dict(Counter(r['question_type'] for r in done.values())))
    write_json(manifest_path, meta)


if __name__ == '__main__':
    main()
