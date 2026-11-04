"""Build judge-SFT examples from gold units and training traces (standard library only).

For every question in gold_sft.jsonl:

1. Training traces: --orders random document arrival orders, one document per step (step i arrives
   at i seconds). Events use the same d<N>s<M> IDs and fields as b_work/step3/build_traces.py. These
   schedules are a training augmentation, never used for latency results.
2. Snapshots: after each arrival, every event that has arrived is visible.
3. Input: A's judge_messages() and JUDGE_SCHEMA, read from --a-ref (default origin/a-prompt-judge) with
   git, applied to the gold unit descriptions and depends_on without answers, as in A's eval_judge.py.
4. Target: computed from gold. A unit is SUPPORTED when a support set is visible and all its
   dependencies are SUPPORTED, citing that set ([[]] cites the dependencies' evidence); otherwise when a
   presupposition set is visible and at least one dependency is SUPPORTED (or the unit has no dependencies),
   by_presupposition. For a question naming exactly two candidates with a unique answer, explicitly ruling
   out one candidate may identify the other by presupposition. Else UNRESOLVED.

Snapshots with the same visible set are kept once per question. A snapshot is "changed" when a label
changes, or a unit becomes blocked (its own evidence is visible but a dependency is unsupported).
Unchanged snapshots (a distractor arrived) are kept up to --max-unchanged per question; the snapshot
with all evidence is always kept; at most --max-per-question examples per question.
"""

import argparse
from collections import Counter
import importlib
import json
import math
from pathlib import Path
import random
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE.parent / "step2"))
sys.path.insert(0, str(HERE.parent / "step3"))
from build_traces import SCHEMA_VERSION, validate as validate_trace  # noqa: E402
from prepare_step2 import question_key  # noqa: E402

DATA_VERSION = "sft-v0"
SUPPORTED, UNRESOLVED = "SUPPORTED", "UNRESOLVED"
PRESUPPOSITION_EXTENSION = (
    "\n  For exactly two named candidates where the question presupposes one unique answer, evidence "
    "explicitly ruling out one candidate also identifies the other. Label the conclusion SUPPORTED with "
    "by_presupposition true."
)


def load_a_judge(ref):
    """Import A's turntaking.judge and turntaking.schema from a git ref; return (module, commit)."""
    commit = subprocess.run(["git", "rev-parse", ref], cwd=REPO, check=True, capture_output=True, text=True).stdout.strip()
    package = Path(tempfile.mkdtemp(prefix="a_judge_")) / "turntaking"
    package.mkdir()
    for name in ["__init__.py", "schema.py", "judge.py"]:
        text = subprocess.run(["git", "show", commit + ":a_work/turntaking/" + name], cwd=REPO, check=True,
                              capture_output=True, text=True).stdout
        (package / name).write_text(text, encoding="utf-8")
    sys.path.insert(0, str(package.parent))
    return importlib.import_module("turntaking.judge"), importlib.import_module("turntaking.schema"), commit


def training_trace(sample, order, name):
    events = []
    for step, number in enumerate(order, start=1):
        title, sentences = sample["context"][number - 1]
        for index, text in enumerate(sentences):
            events.append({
                "evidence_id": "d" + str(number) + "s" + str(index),
                "scheduled_time_s": float(step),
                "visible_time_s": float(step),
                "text": text.strip(),
                "source": {"dataset": sample["dataset"], "document_id": title,
                           "document_index": number, "sentence_index": index},
            })
    trace = {
        "schema_version": SCHEMA_VERSION, "data_version": DATA_VERSION, "sample_id": sample["sample_id"],
        "trace_id": sample["sample_id"] + "_" + name, "question": sample["question"], "time_origin": "question_end",
        "clock": "simulated", "trace_type": "controlled_mock", "events": events,
        "retrieval_complete_time_s": float(len(order)),
    }
    validate_trace(trace, sample)
    return trace


def label_units(units, visible):
    """Target judgment per unit ID for the visible evidence IDs (see module docstring)."""
    by_id = {u["unit_id"]: u for u in units}
    out = {}

    def visit(uid):
        if uid not in out:
            unit = by_id[uid]
            parents = [visit(p) for p in unit["depends_on"]]
            ok = [p["label"] == SUPPORTED for p in parents]
            result = {"unit_id": uid, "label": UNRESOLVED, "value": None, "citations": [],
                      "by_omission": False, "by_presupposition": False}
            complete = [s for s in unit["support_sets"] if set(s) <= visible]
            presupposed = [s for s in unit.get("presupposition_sets", []) if set(s) <= visible]
            if complete and all(ok):
                cites = complete[0]
                if not cites:  # [[]]: a conclusion cites the evidence of its dependencies
                    cites = [c for p in parents for c in p["citations"]]
                result.update(label=SUPPORTED, value=unit["expected_answer"], citations=list(dict.fromkeys(cites)),
                              by_omission=bool(unit.get("by_omission")))
            elif presupposed and (any(ok) or not ok):
                result.update(label=SUPPORTED, value=unit["expected_answer"], citations=list(presupposed[0]),
                              by_presupposition=True)
            out[uid] = result
        return out[uid]

    return [visit(u["unit_id"]) for u in units]


def cross_check(judge, schema, gold, sample, evidence, targets):
    """Disagreements with A's code: OracleJudge + resolve_dependencies for units with no presupposition set
    on themselves or their dependencies, and derive_conclusion for conclusions SUPPORTED by_presupposition."""
    units = [schema.Unit(u["unit_id"], u["description"], u["necessary"], tuple(u["depends_on"])) for u in gold["units"]]
    obs = schema.Observation(sample["sample_id"], sample["question"], 0.0, tuple(evidence), tuple(units), False)
    oracle = judge.resolve_dependencies(units, judge.OracleJudge([gold]).judge(obs))
    labels = {t["unit_id"]: schema.UnitJudgment(t["label"], tuple(t["citations"]), t["value"], t["by_omission"],
                                                t["by_presupposition"]) for t in targets}
    # OracleJudge does not read presupposition_sets, so skip units that use one directly or through a dependency.
    by_id = {u["unit_id"]: u for u in gold["units"]}

    def presupposed(uid):
        unit = by_id[uid]
        return bool(unit.get("presupposition_sets")) or any(presupposed(p) for p in unit["depends_on"])

    problems = []
    for unit, target in zip(units, targets):
        if not presupposed(unit.unit_id) and oracle[unit.unit_id].label != target["label"]:
            problems.append(unit.unit_id + ": oracle " + oracle[unit.unit_id].label)
        # A's current derive_conclusion implements the positive-candidate form of Section 5.6 only.
        # The approved B-side extension also permits a unique answer after one of exactly two named
        # candidates is explicitly ruled out. Cross-check the former against A and treat the latter as
        # an intentional extension until A adopts the same rule.
        supported_parent_values = [labels[p].value for p in unit.depends_on
                                   if labels[p].label == SUPPORTED]
        has_confirmed_positive = any(str(value).casefold() == "yes" for value in supported_parent_values)
        if target["by_presupposition"] and judge.is_conclusion(unit) and has_confirmed_positive:
            label, _, _ = judge.derive_conclusion(unit, labels, target["value"], True, sample["question"])
            if label != SUPPORTED:
                problems.append(unit.unit_id + ": derive_conclusion " + label)
    return problems


def examples_for(sample, gold, args, judge, schema):
    rng = random.Random(str(args.seed) + ":" + sample["sample_id"])
    documents = list(range(1, len(sample["context"]) + 1))
    orders = []
    while len(orders) < min(args.orders, math.factorial(len(documents))):
        order = documents[:]
        rng.shuffle(order)
        if order not in orders:
            orders.append(order)
    units = [schema.Unit(u["unit_id"], u["description"], u["necessary"], tuple(u["depends_on"])) for u in gold["units"]]
    seen, changed, unchanged, final, problems = set(), [], [], None, []
    for number, order in enumerate(orders, start=1):
        trace = training_trace(sample, order, "sftorder" + str(number))
        previous = None
        for step in range(1, len(order) + 1):
            evidence = [schema.Evidence(e["evidence_id"], e["text"], e["visible_time_s"], e["source"])
                        for e in trace["events"] if e["visible_time_s"] <= step]
            visible = frozenset(e.evidence_id for e in evidence)
            targets = label_units(gold["units"], visible)
            # A unit is blocked when its own evidence is visible but a dependency is not supported yet;
            # the step where that starts is as informative as a label change.
            blocked = [t["label"] == UNRESOLVED and any(s and set(s) <= visible for s in u["support_sets"])
                       for u, t in zip(gold["units"], targets)]
            labels = [t["label"] for t in targets] + blocked
            snapshot = {"trace_id": trace["trace_id"], "time_s": float(step), "order": order[:step],
                        "evidence": evidence, "targets": targets}
            if visible not in seen:
                seen.add(visible)
                problems += [sample["sample_id"] + " " + trace["trace_id"] + " t=" + str(step) + " " + p
                             for p in cross_check(judge, schema, gold, sample, evidence, targets)]
                if step == len(order):
                    final = snapshot
                elif labels != previous and (previous is not None or SUPPORTED in labels or any(blocked)):
                    changed.append(snapshot)
                else:
                    unchanged.append(snapshot)
            previous = labels
    rng.shuffle(unchanged)
    chosen = changed + unchanged[:args.max_unchanged]
    rng.shuffle(chosen)
    chosen = sorted(chosen[:args.max_per_question - 1], key=lambda s: (s["trace_id"], s["time_s"])) + [final]
    records = []
    for snapshot in chosen:
        obs = schema.Observation(sample["sample_id"], sample["question"], snapshot["time_s"],
                                 tuple(snapshot["evidence"]), tuple(units), snapshot["time_s"] == len(documents))
        messages = judge.judge_messages(obs)
        messages = [dict(message) for message in messages]
        messages[0]["content"] += PRESUPPOSITION_EXTENSION
        if args.no_examples:
            messages = messages[:1] + messages[-1:]
        reply = {"units": snapshot["targets"]}
        records.append({
            "messages": messages + [{"role": "assistant", "content": json.dumps(reply, ensure_ascii=False)}],
            "metadata": {"data_version": DATA_VERSION, "sample_id": sample["sample_id"], "split": sample["project_split"],
                         "question_type": gold["question_type"], "trace_id": snapshot["trace_id"],
                         "time_s": snapshot["time_s"], "document_order": snapshot["order"],
                         "labels": {t["unit_id"]: t["label"] for t in snapshot["targets"]}},
        })
    return records, problems


def check_record(record, schema_def, labels):
    """Every target unit has the reply fields, a known label, and citations to visible evidence only."""
    reply = json.loads(record["messages"][-1]["content"])
    request = record["messages"][-2]["content"]
    required = schema_def["properties"]["units"]["items"]["required"]
    for unit in reply["units"]:
        if sorted(unit) != sorted(required) or unit["label"] not in labels:
            raise ValueError(record["metadata"]["sample_id"] + ": target does not match JUDGE_SCHEMA")
        if unit["label"] == SUPPORTED and not all("[" + c + "]" in request for c in unit["citations"]):
            raise ValueError(record["metadata"]["sample_id"] + ": citation not visible in the request")
        if unit["label"] != SUPPORTED and (unit["citations"] or unit["value"] is not None):
            raise ValueError(record["metadata"]["sample_id"] + ": UNRESOLVED unit with a value or citations")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates", type=Path, default=HERE / "prepared" / "samples_sft_candidates.jsonl")
    parser.add_argument("--gold", type=Path, default=HERE / "gold_sft.jsonl")
    parser.add_argument("--step2", type=Path, default=HERE.parent / "step2" / "prepared")
    parser.add_argument("--out", type=Path, default=HERE / "sft")
    parser.add_argument("--a-ref", default="origin/a-prompt-judge", help="git ref that holds A's a_work/turntaking")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--orders", type=int, default=3, help="random document orders per question")
    parser.add_argument("--max-unchanged", type=int, default=2)
    parser.add_argument("--max-per-question", type=int, default=10)
    parser.add_argument("--no-examples", action="store_true", help="drop A's few-shot examples from the input")
    args = parser.parse_args()

    judge, schema, commit = load_a_judge(args.a_ref)
    samples = {json.loads(line)["sample_id"]: json.loads(line)
               for line in args.candidates.read_text(encoding="utf-8").splitlines()}
    golds = [json.loads(line) for line in args.gold.read_text(encoding="utf-8").splitlines()]

    held_out_ids, held_out_questions = set(), set()
    for name in ["samples_debug.jsonl", "samples_eval_reserved.jsonl"]:
        for line in (args.step2 / name).read_text(encoding="utf-8").splitlines():
            row = json.loads(line)
            held_out_ids.add(row["sample_id"])
            held_out_questions.add(question_key(row["question"]))

    splits = {"train": [], "dev": []}
    problems = []
    for gold in golds:
        sample = samples[gold["sample_id"]]
        if sample["sample_id"] in held_out_ids or question_key(sample["question"]) in held_out_questions:
            raise ValueError(sample["sample_id"] + ": overlaps the debug or reserved evaluation set")
        records, found = examples_for(sample, gold, args, judge, schema)
        for record in records:
            check_record(record, judge.JUDGE_SCHEMA, schema.LABELS)
        splits[sample["project_split"]] += records
        problems += found
    if {r["metadata"]["sample_id"] for r in splits["train"]} & {r["metadata"]["sample_id"] for r in splits["dev"]}:
        raise ValueError("A question appears in both train and dev")

    args.out.mkdir(parents=True, exist_ok=True)
    stats = {"data_version": DATA_VERSION, "a_ref": args.a_ref, "a_commit": commit, "seed": args.seed,
             "orders": args.orders, "max_unchanged": args.max_unchanged, "max_per_question": args.max_per_question,
             "few_shot_examples": not args.no_examples, "cross_check_disagreements": problems}
    for split, records in splits.items():
        with (args.out / ("sft_" + split + ".jsonl")).open("w", encoding="utf-8") as file:
            for record in records:
                file.write(json.dumps(record, ensure_ascii=False) + "\n")
        targets = [u for r in records for u in json.loads(r["messages"][-1]["content"])["units"]]
        lengths = sorted(sum(len(m["content"]) for m in r["messages"]) for r in records)
        stats[split] = {
            "questions": len({r["metadata"]["sample_id"] for r in records}),
            "examples": len(records),
            "examples_by_question_type": dict(Counter(r["metadata"]["question_type"] for r in records)),
            "unit_labels": dict(Counter(u["label"] for u in targets)),
            "by_omission": sum(u["by_omission"] for u in targets),
            "by_presupposition": sum(u["by_presupposition"] for u in targets),
            "all_unresolved_examples": sum(all(u["label"] == UNRESOLVED for u in json.loads(r["messages"][-1]["content"])["units"])
                                           for r in records),
            "chars_median_max": [lengths[len(lengths) // 2], lengths[-1]] if lengths else None,
        }
    (args.out / "sft_stats.json").write_text(json.dumps(stats, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({s: stats[s] for s in splits}, indent=1))
    print("cross-check disagreements with A's code: " + str(len(problems)))
    for problem in problems[:20]:
        print("  " + problem)


if __name__ == "__main__":
    main()
