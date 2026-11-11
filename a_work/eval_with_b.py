"""Score a replay run with B's evaluator, next to A's own self-check.

    python3 a_work/eval_with_b.py a_work/results/replay/RUN [--ref origin/b-data-eval]

B's evaluator lives on B's branch, so it is unpacked from that git ref into a temporary folder and run from
there; nothing is copied into this branch. Writes RUN/b_eval/ (B's own reports) and RUN/b_eval/both.md.
Use --reviews FILE --out DIR to score assisted/reviewed mappings separately from the original evaluation.

Policies that use gold unit ids (`+oracle`, and a judge on gold units) are passed as aligned. The rest map
by value, which B counts as approximate; claims it cannot map wait in its review queue and are not scored.
B's evaluator is a draft that scores only the structured claims, so these are not final numbers either.
"""
import argparse
import hashlib
import io
import json
import subprocess
import sys
import tarfile
import tempfile
from collections import defaultdict
from pathlib import Path


def unpack_evaluator(repo: Path, ref: str, folder: str) -> None:
    archive = subprocess.run(["git", "archive", ref, "b_work/eval"], cwd=repo, check=True, capture_output=True).stdout
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        tar.extractall(folder, **({"filter": "data"} if hasattr(tarfile, "data_filter") else {}))


def inputs_of(run: Path) -> dict:
    """Traces and gold the run used: run_config.json, or the header of an older run's summary."""
    config = run / "run_config.json"
    if config.exists():
        return json.loads(config.read_text(encoding="utf-8"))
    header = (run / "summary.md").read_text(encoding="utf-8").split("\n")[2]
    return {"trace": header.split("traces `")[1].split("`")[0], "gold": header.split("gold `")[1].split("`")[0]}


def aligned(policy: str) -> bool:
    """Evidence-aware on gold units; `_real` runs use the model's own units."""
    return policy.startswith("evidence_aware+") and "_real" not in policy


def check_review_source(reviews: Path, log: Path) -> None:
    """Honor optional log hashes on assisted reviews so edits cannot silently reuse their indices."""
    digest = hashlib.sha256(log.read_bytes()).hexdigest()
    for line in reviews.read_text(encoding="utf-8").splitlines():
        if line.strip():
            recorded = json.loads(line).get("source_log_sha256")
            if recorded is not None and recorded != digest:
                raise ValueError("Review source_log_sha256 does not match policy_log.jsonl")


def table(run: Path, out: Path) -> str:
    ours = defaultdict(list)
    for line in open(run / "trace_metrics.jsonl", encoding="utf-8"):
        row = json.loads(line)
        ours[row["policy"]].append(row)
    theirs = defaultdict(list)
    for line in open(out / "run_scores.jsonl", encoding="utf-8"):
        row = json.loads(line)
        theirs[row["policy"]].append(row)

    def mean(values):
        values = [v for v in values if v is not None]
        return f"{sum(values) / len(values):.3f} ({len(values)})" if values else "-"

    lines = ["| policy | B: completed | B: unit EM (runs scored) | B: unsupported / scored claims | B: claims to review "
             "| A: asked answer correct | A: unsupported / claims |", "|---|---|---|---|---|---|---|"]
    for policy, rows in ours.items():
        b = theirs.get(policy, [])
        lines.append(
            f"| {policy} | {sum(r['ttca_s'] is not None for r in b)}/{len(b)} | {mean(r['unit_em'] for r in b)} "
            f"| {sum(r['unsupported_claims'] for r in b)}/{sum(r['claims_scored'] for r in b)} "
            f"| {sum(r['claims_needing_review'] for r in b)} "
            f"| {sum(bool(r.get('final_correct')) for r in rows)}/{len(rows)} "
            f"| {sum(r['unsupported'] for r in rows)}/{sum(r['claims'] for r in rows)} |")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run", type=Path)
    ap.add_argument("--ref", default="origin/b-data-eval", help="Git ref that holds b_work/eval.")
    ap.add_argument("--reviews", type=Path, help="B-compatible claim-to-gold mappings; does not override values or support.")
    ap.add_argument("--out", type=Path, help="Output directory; required with --reviews to preserve the original evaluation.")
    ap.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1],
                    help="Repository root; set explicitly when running a frozen copy of this script.")
    args = ap.parse_args()
    if args.reviews and args.out is None:
        ap.error("--reviews requires a separate --out directory")

    run = args.run.resolve()
    out = args.out.resolve() if args.out else run / "b_eval"
    if args.reviews and out == run / "b_eval":
        ap.error("--reviews must not overwrite the original b_eval directory")
    if args.reviews:
        try:
            check_review_source(args.reviews.resolve(), run / "policy_log.jsonl")
        except (OSError, ValueError) as error:
            ap.error(str(error))
    inputs = inputs_of(run)
    policies = list(dict.fromkeys(json.loads(line)["policy"] for line in open(run / "trace_metrics.jsonl", encoding="utf-8")))
    repo = args.repo.resolve()
    command = [sys.executable, "-m", "b_work.eval.run_eval", "--logs", str(run / "policy_log.jsonl"),
               "--traces", str(repo / inputs["trace"]), "--gold", str(repo / inputs["gold"]),
               "--timing-kind", "estimated", "--allow-value-match", "--expected-policies", *policies, "--out", str(out)]
    if args.reviews:
        command += ["--reviews", str(args.reviews.resolve())]
    for policy in filter(aligned, policies):
        command += ["--aligned-policy", policy]
    commit = subprocess.run(["git", "rev-parse", args.ref], cwd=repo, check=True, capture_output=True, text=True).stdout.strip()
    with tempfile.TemporaryDirectory() as folder:
        unpack_evaluator(repo, commit, folder)
        done = subprocess.run(command, cwd=folder, capture_output=True, text=True)
    if done.returncode not in (0, 1):  # 1: some log rows are invalid, the reports say which
        sys.exit(done.stderr or done.stdout)
    review_note = (f"Mappings from `{args.reviews.resolve()}`; see reviewer identities in that file. "
                   "Mapping review does not resolve missing values, unspoken values, or gold-rule disagreements.\n\n"
                   if args.reviews else "")
    text = (f"# B's evaluator and A's self-check\n\nRun `{run.name}`, evaluator at `{args.ref}` ({commit}), exit code "
            f"{done.returncode}. B scores only claims it can map to a gold unit and requires cited support; A's "
            f"columns are the self-check from trace_metrics.jsonl.\n\n" + review_note + table(run, out))
    (out / "both.md").write_text(text, encoding="utf-8")
    print(text)
    return done.returncode


if __name__ == "__main__":
    sys.exit(main())
