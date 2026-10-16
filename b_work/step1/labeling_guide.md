# Evidence Labels and Action Meanings — B Group v1

Status: B GROUP LABELING CONVENTIONS v1 FOR INTEGRATION. A/C should use these names and report concrete compatibility issues; no all-group sign-off is required to start B data preparation.

## 1. Label a specific candidate claim

Assess a candidate factual claim against evidence visible at the time of assessment. Question, candidate claim, timestamp, and visible evidence must be recorded. Labeling a broad topic without an explicit candidate claim is ambiguous.

| Label | Rule |
|---|---|
| `SUPPORTED` | Current evidence explicitly supports the full candidate claim, required dependencies are satisfied, and required citations point to valid supporting evidence. |
| `UNRESOLVED` | Current evidence is insufficient or a required dependency is missing. Lack of support does not imply contradiction. |
| `CONTRADICTED` | Current evidence explicitly conflicts with the candidate claim. |

Split compound statements into atomic claims before labeling. If a claim has both explicit support and conflicting evidence, mark the example for human review; freeze a conflict-resolution rule before including such cases in automatic scoring or SFT.

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

Each annotation should record `sample_id`, candidate claim, assessment time, visible evidence IDs, label, supporting/conflicting source spans, annotator ID, rationale, and review status. Gold answer access is permitted for B's annotation and evaluation, not for ordinary inference inputs.

B should check the fictional example and several real examples before expanding annotation. Invite A/C feedback on ambiguous cases and resolve disagreements against source text. Record any changes to the rules. Do not label from future evidence or from the expected answer alone.

## 5. Integration checks and remaining scoring decisions

- A should consume the three label names and produce the five exact action strings, or report an adapter requirement.
- Confirm whether citations must be machine-readable, spoken, or both.
- Confirm how useful partial answers are distinguished from internal reasoning facts.
- Confirm how conflicting evidence, corrections, and retractions are scored.
- Keep A's judge predictions separate from B's independent evaluation labels.
