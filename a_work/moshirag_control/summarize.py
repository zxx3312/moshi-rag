"""Per-run metrics, a per-condition table, and a human review sheet for a control run.

    python3 a_work/moshirag_control/summarize.py RUN_DIR

Stdlib only. Steps are 80 ms frames; all reported times are seconds after the question ends.
Wrong answers cannot be detected by string matching; they are left to the review sheet.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

AUDIBLE_DB = -45.0
QUIET_MODES = ("silence", "held")
CLOSURES = ("anything else", "does that help", "hope that helps")


def _pieces_to_text(pieces) -> str:
    return "".join(p.replace("▁", " ") for p in pieces if p not in ("<pad>", "[RET]")).strip()


def _mentions(text: str, aliases) -> bool:
    low = text.lower()
    return any(a.lower() in low for a in aliases)


def analyze_trace(trace: dict) -> dict:
    ctrl = trace["control"]
    exp = trace["experiment"]
    fr = float(exp["frame_rate"])
    text = trace["model_text"]
    rms = trace.get("model_rms_db") or []
    q = ctrl["question_end_step"]
    n = len(text)

    evidence = [i for i in ctrl["injections"] if i["label"] != "not_ready"]
    first_ev = evidence[0]["scheduled_step"] if evidence else n
    final_ev = evidence[-1]["scheduled_step"] if evidence else n

    def window(a, b):
        return _pieces_to_text(text[max(a, 0):min(b, n)])

    def t(step):
        return None if step is None else round((step - q) / fr, 2)

    # Did the hard constraints hold? Quiet modes must produce no words and (ideally) no sound.
    quiet = [r["step"] for r in ctrl["rows"] if r["mode"] in QUIET_MODES and r["step"] < n]
    leaked = [s for s in quiet if text[s] not in ("<pad>", "[RET]")]
    quiet_audible = [s for s in quiet if s < len(rms) and rms[s] is not None and rms[s] > AUDIBLE_DB]
    say_steps = [r["step"] for r in ctrl["rows"] if r["mode"] == "say" and r["restricted"] and r["step"] < n]

    first_word = next((i for i in range(q, n) if text[i] not in ("<pad>", "[RET]")), None)
    first_sound = next((i for i in range(q, min(n, len(rms))) if rms[i] is not None and rms[i] > AUDIBLE_DB), None)

    unit_rows = []
    for u in ctrl["units"]:
        support = [e["visible_time_s"] for e in ctrl["events"] if e["evidence_id"] in u["support"]]
        sup_step = q + round(max(support) * fr) if support else n
        said = next((i for i in range(q, n) if _mentions(window(q, i + 1), u["answer"])), None)
        unit_rows.append({
            "unit_id": u["unit_id"], "necessary": u["necessary"],
            "first_mention_s": t(said),
            "mentioned_before_support": said is not None and said < sup_step,
            "mentioned_after_support": _mentions(window(sup_step, n), u["answer"]),
        })
    necessary = [u for u in unit_rows if u["necessary"]]

    return {
        "run_id": exp["run_id"], "sample_id": exp["sample_id"], "condition": ctrl["condition"],
        "seed": exp["seed"], "status": exp.get("status"), "stop_reason": exp.get("stop_reason"),
        "first_word_s": t(first_word), "first_sound_s": t(first_sound),
        "quiet_frames": len(quiet), "quiet_word_leaks": len(leaked),
        "quiet_audible_frac": round(len(quiet_audible) / len(quiet), 3) if quiet else None,
        "say_frames": len(say_steps),
        "units": unit_rows,
        "all_necessary_correct": all(u["mentioned_after_support"] for u in necessary),
        "closure_before_final": any(c in window(q, final_ev).lower() for c in CLOSURES),
        "words_before_first_evidence": len(window(q, first_ev).split()),
        "text_before_question_end": window(0, q),
        "text_before_first_evidence": window(q, first_ev),
        "text_between_evidence": window(first_ev, final_ev),
        "text_after_final_evidence": window(final_ev, n),
        "ret_times_s": [t(s) for s in ctrl["ret_steps"]],
        "injections": [{"label": i["label"], "t": t(i["scheduled_step"]), "num_steps": i["num_steps"]}
                       for i in ctrl["injections"]],
    }


def _rate(rows, key):
    vals = [r[key] for r in rows if r[key] is not None]
    return f"{sum(bool(v) for v in vals)}/{len(vals)}" if vals else "-"


def _median(vals):
    vals = sorted(v for v in vals if v is not None)
    return None if not vals else vals[len(vals) // 2]


def table(rows) -> str:
    by_cond = defaultdict(list)
    for r in rows:
        by_cond[r["condition"]].append(r)
    head = ("| condition | runs | correct after evidence | answer before evidence | closure before final "
            "| median first word (s) | word leaks in quiet | audible in quiet |")
    lines = [head, "|" + "---|" * 8]
    for cond in ("free", "wait", "progress", "notready", "ours"):
        rs = by_cond.get(cond)
        if not rs:
            continue
        before = [any(u["mentioned_before_support"] for u in r["units"] if u["necessary"]) for r in rs]
        quiet = [r["quiet_audible_frac"] for r in rs if r["quiet_audible_frac"] is not None]
        lines.append(
            f"| {cond} | {len(rs)} | {_rate(rs, 'all_necessary_correct')} | {sum(before)}/{len(rs)} "
            f"| {_rate(rs, 'closure_before_final')} | {_median([r['first_word_s'] for r in rs])} "
            f"| {sum(r['quiet_word_leaks'] for r in rs)} "
            f"| {'-' if not quiet else f'{sum(quiet) / len(quiet):.0%}'} |"
        )
    return "\n".join(lines)


def review_sheet(rows) -> str:
    out = ["# Control run review", "",
           "For each run, check the text before the evidence: is it a concrete wrong answer (yes/no)? "
           "For `ours`, is the text between evidence arrivals supported by the first evidence only?", ""]
    by_sample = defaultdict(list)
    for r in rows:
        by_sample[r["sample_id"]].append(r)
    for sample, rs in by_sample.items():
        out += [f"## {sample}", "", "| condition | before first evidence | between evidence | after final evidence | wrong answer before evidence? |",
                "|---|---|---|---|---|"]
        for r in rs:
            cells = [r["text_before_first_evidence"], r["text_between_evidence"], r["text_after_final_evidence"]]
            cells = [c.replace("|", "/") or "(silent)" for c in cells]
            out.append(f"| {r['condition']} | {cells[0]} | {cells[1]} | {cells[2]} | |")
        out.append("")
    return "\n".join(out)


def main(run_dir: Path) -> None:
    rows = [analyze_trace(json.loads(p.read_text(encoding="utf-8")))
            for p in sorted((run_dir / "traces").glob("*.json"))]
    analysis = run_dir / "analysis"
    analysis.mkdir(exist_ok=True)
    with open(analysis / "per_run.jsonl", "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    (analysis / "summary.md").write_text(table(rows) + "\n", encoding="utf-8")
    (analysis / "review.md").write_text(review_sheet(rows), encoding="utf-8")
    print(table(rows))
    print(f"\nwrote {analysis}/per_run.jsonl, summary.md, review.md")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
