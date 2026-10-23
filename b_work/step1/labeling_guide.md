# Evidence Labels and Action Meanings — B Group v1.1

Status: B GROUP LABELING CONVENTIONS v1.1 FOR INTEGRATION. A/C should use these names and report concrete compatibility issues; no all-group sign-off is required to start B data preparation. v1.1 adds the explicit-support rule and its two exceptions (Section 1.1); see Section 6 for the change log.

## 1. Label a specific candidate claim

Assess a candidate factual claim against evidence visible at the time of assessment. Question, candidate claim, timestamp, and visible evidence must be recorded. Labeling a broad topic without an explicit candidate claim is ambiguous.

| Label | Rule |
|---|---|
| `SUPPORTED` | Current evidence explicitly supports the full candidate claim, required dependencies are satisfied, and required citations point to valid supporting evidence. |
| `UNRESOLVED` | Current evidence is insufficient or a required dependency is missing. Lack of support does not imply contradiction. |
| `CONTRADICTED` | Current evidence explicitly conflicts with the candidate claim. |

Split compound statements into atomic claims before labeling. If a claim has both explicit support and conflicting evidence, mark the example for human review; freeze a conflict-resolution rule before including such cases in automatic scoring or SFT.

### 1.1 What counts as explicit support (v1.1)

**Rule: explicit statements only.** Evidence must state the candidate value. Inference is not support. Example: "Being Twenty is an Italian film directed by Fernando Di Leo" does not support "Di Leo was born in Italy."

There are two exceptions. Both apply to gold annotation and B's evaluation.

**Exception 1: deterministic comparison.** A comparison conclusion unit (`support_sets: [[]]` in `schema.md` 4.2) is `SUPPORTED` when all its dependency units are `SUPPORTED` and the conclusion follows from their values by a deterministic comparison, such as ordering two dates or checking whether two nationalities are equal. The citation is the dependency units' evidence.

**Exception 2: omission from a defining description.** A negative claim may be labeled `SUPPORTED` when all of the following hold:

1. The evidence is a defining description of the entity, usually the opening sentence of an encyclopedia article.
2. The attribute is one that such descriptions normally list: occupation, nationality, or category (e.g., taxonomic family).
3. The description lists values for that attribute, and the claimed value is not among them.
4. No visible evidence states the claimed value positively. If one does, the omission exception does not apply.

Mark such units `by_omission: true` in gold. Example: "Jon Turteltaub is an American film director and producer" supports "Turteltaub is not a television writer." This matches how HotpotQA and 2WikiMultiHopQA gold answers treat such questions.

The exception does not cover:

- Negatives that need world knowledge. Example: evidence says an airport is in Minnesota; this does not support "it is not in Europe." Label `UNRESOLVED` until a rule is agreed.
- Attributes that defining descriptions do not normally list, such as awards, events, or relationships. Example: Anaïs Nin's description ("an essayist and memoirist…") does not support "Nin did not win the Nobel Prize in Literature." Label `UNRESOLVED`.

## 2. Fictional annotation example

Question: Who leads Alpha, and when was it released?

- e1 arrives at 2 seconds: Alpha is led by Alice.
- e2 arrives at 8 seconds: Alpha was released on June 1.

| Time | Visible evidence | Candidate claim | Label |
|---|---|---|---|
| 0 s | None | Alpha is led by Alice. | `UNRESOLVED` |
| 2 s | e1 | Alpha is led by Alice. | `SUPPORTED` |
| 2 s | e1 | Alpha was released on June 1. | `UNRESOLVED` |
| 2 s | e1 | Alpha is led by Bob. | `CONTRADICTED` |
| 8 s | e1, e2 | Alpha was released on June 1. | `SUPPORTED` |

At 2 seconds, a supported partial answer is possible. At 8 seconds, both necessary answer units have support. This describes evidence sufficiency; output correctness still needs independent evaluation.

## 3. Actions are separate from evidence labels

| Exact action string | Meaning | Constraint |
|---|---|---|
| `Wait` | Produce no output now. | Empty output text. |
| `Backchannel` | Brief acknowledgment. | Do not add unsupported factual content. |
| `Progress` | Describe the ongoing process. | Process statements must be accurate; do not claim a search is ongoing after it has ended. |
| `Partial Answer` | Answer a useful supported part while leaving another required part open. | Every factual claim must have current support. |
| `Final Answer` | Attempt to answer all necessary parts. | The action name is not a correctness or completion label. |

Examples: at 2 seconds, “Alpha is led by Alice. I am still checking the release date” is a possible partial answer only if checking is actually ongoing. At 8 seconds, “Alpha is led by Alice and was released on June 1” is a possible full answer.

Do not use `PARTIAL` as a replacement for the claim-level labels in this v1 specification. Partial completion of the question and support for a particular claim are different concepts.

## 4. Annotation record and review

Each annotation should record `sample_id`, candidate claim, assessment time, visible evidence IDs, label, supporting/conflicting source spans, annotator ID, rationale, review status, and whether an exception from Section 1.1 was used. Gold answer access is permitted for B's annotation and evaluation, not for ordinary inference inputs.

B should check the fictional example and several real examples before expanding annotation. Invite A/C feedback on ambiguous cases and resolve disagreements against source text. Record any changes to the rules. Do not label from future evidence or from the expected answer alone.

## 5. Integration checks and remaining scoring decisions

- A should consume the three label names and produce the five exact action strings, or report an adapter requirement.
- Confirm whether citations must be machine-readable, spoken, or both.
- ~~Confirm how useful partial answers are distinguished from internal reasoning facts.~~ Resolved in v1.1: every gold unit, including `necessary: false` intermediate hops, counts as useful grounded information (`schema.md` 4.3).
- Confirm how conflicting evidence, corrections, and retractions are scored.
- Keep A's judge predictions separate from B's independent evaluation labels.
- Decide how to annotate answers that rely on the question's presupposition rather than evidence. Example: "In between Anaïs Nin and Odysseas Elytis, who was awarded the Nobel Prize in Literature?" Elytis's win is explicit, but Nin's non-win has no support under Section 1.1.
- Decide whether A's runtime judge may apply Exception 2, or whether it is limited to gold annotation and evaluation.
- Decide how to label negatives that need world knowledge.
- Decide whether deterministic comparisons are computed by a rule or by the judge.

## 6. Change log

| Version | Date | Change |
|---|---|---|
| v1 | 2026-10-15 | Initial labeling conventions. |
| v1.1 | 2026-10-23 | Added Section 1.1: explicit-support rule, deterministic-comparison exception, and omission exception with `by_omission`, from A's `unit_schema.md` v0.1 draft. Marked the partial-answer item resolved and added four pending decisions. |
