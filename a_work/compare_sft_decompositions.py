"""Validate a completed vLLM export and compare with the earlier Transformers run."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
from turntaking.decompose import build_messages, UNIT_SCHEMA, validate_units


def read_lines(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=Path('a_work/sft_decomposed_v1'))
    parser.add_argument('--previous', type=Path, default=Path('a_work/sft_decomposed_transformers_v1'))
    parser.add_argument('--calls', type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads((args.out/'manifest.json').read_text())
    assert manifest['completed'] and manifest['backend'] == 'vllm-json-schema'
    rows = read_lines(args.out/'decompositions.jsonl')
    old_rows = read_lines(args.previous/'decompositions.jsonl')
    old = {r['sample_id']: r for r in old_rows}
    assert len(rows) == len(old) == 300
    assert len({r['sample_id'] for r in rows}) == 300
    assert {r['sample_id'] for r in rows} == set(old)
    calls = {r['key']: r for r in read_lines(args.calls)}
    differences = []
    shape = lambda units: [(u['necessary'], u['depends_on']) for u in units]
    for row in rows:
        validate_units(row)
        previous = old[row['sample_id']]
        assert row['question'] == previous['question'] and row['split'] == previous['split']
        assert all(set(u) == {'unit_id','description','necessary','depends_on'} for u in row['units'])
        key = hashlib.sha1(json.dumps([manifest['model'],build_messages(row['question']),UNIT_SCHEMA,
                         {'chat_template_kwargs':{'enable_thinking':False}}],sort_keys=True).encode()).hexdigest()
        assert key in calls and calls[key]['purpose'] == 'decompose', row['sample_id']
        flags = dict(type_changed=row['question_type'] != previous['question_type'],
                     count_changed=len(row['units']) != len(previous['units']),
                     structure_changed=shape(row['units']) != shape(previous['units']),
                     units_changed=row['units'] != previous['units'])
        if any(flags.values()):
            differences.append(dict(sample_id=row['sample_id'],split=row['split'],question=row['question'],
                                    transformers_type=previous['question_type'],vllm_type=row['question_type'],
                                    transformers_units=previous['units'],vllm_units=row['units'],**flags))
    for split, count in [('train',243),('dev',57)]:
        exported=json.loads((args.out/f'{split}.json').read_text())['records']
        assert len(exported) == count
        assert {r['sample_id'] for r in exported} == {r['sample_id'] for r in rows if r['split']==split}
        assert (args.out/f'{split}.md').read_text().count('### New decomposer units') == count
    for path, digest in manifest['source_sha256'].items():
        assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == digest
    summary = dict(questions=300, splits=dict(Counter(r['split'] for r in rows)),
                   fallback_count=sum(r['fell_back'] for r in rows),
                   question_types=dict(Counter(r['question_type'] for r in rows)),
                   exact_decomposition_matches=300-len(differences),
                   changed_questions=len(differences),
                   **{key:sum(r[key] for r in differences) for key in ['type_changed','count_changed','structure_changed','units_changed']},
                   b_source_hashes_unchanged=True,
                   note='Exact equality compares question_type and all unit fields. Structural equality is not semantic equivalence; differences cannot be attributed solely to JSON constraints because backends and hardware also differ.')
    (args.out/'comparison_transformers.json').write_text(json.dumps(dict(summary=summary,records=differences),ensure_ascii=False,indent=2)+'\n')
    lines=['# vLLM 拆题结果与 Transformers 版本对比','','共 300 道题：train 243、dev 57。模型仅接收问题；新单元待复核，不含新答案和证据标签。','',
           '| 检查项 | 数量 |','|---|---|',
           f"| vLLM fallback | {summary['fallback_count']} |",f"| 拆解字段完全相同 | {summary['exact_decomposition_matches']} |",
           f"| 存在差异的题目 | {summary['changed_questions']} |",f"| 题型不同 | {summary['type_changed']} |",
           f"| 单元数量不同 | {summary['count_changed']} |",f"| necessary/depends_on 结构不同 | {summary['structure_changed']} |",'',
           '统计可能重叠。文字不同不一定代表语义不同；相同结构也不代表语义等价。差异同时涉及推理后端、JSON 约束和 GPU，不能单独归因于某一个因素。','',
           'B 源文件哈希、train/dev 归属、300 个 ID 以及问题提示词对应的模型调用记录均已检查。','',
           '| Split | Sample ID | Transformers → vLLM 题型 | 单元数 | 依赖/necessary结构变化 |','|---|---|---|---|---|']
    for r in differences:
        lines.append(f"| {r['split']} | {r['sample_id']} | {r['transformers_type']} → {r['vllm_type']} | {len(r['transformers_units'])} → {len(r['vllm_units'])} | {r['structure_changed']} |")
    (args.out/'comparison_transformers.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps(summary,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
