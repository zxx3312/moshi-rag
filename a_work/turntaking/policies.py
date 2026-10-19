"""Turn-taking policies: the evidence-aware controller and four rule baselines.

Each policy is stateful within one trace; call reset() before every trace.
decide() is only called while the agent is not speaking.
"""
from __future__ import annotations

from typing import Set

from .judge import Judge, resolve_dependencies, sufficiency_state
from .schema import (
    BACKCHANNEL, FINAL, FULLY_SUFFICIENT, PARTIAL, PROGRESS, SUPPORTED, WAIT,
    Decision, Observation,
)


def _answer_everything(obs: Observation) -> Decision:
    """Naive full answer: claim every necessary unit, citing whatever is visible."""
    cited = tuple(e.evidence_id for e in obs.evidence)
    units = tuple(u.unit_id for u in obs.units if u.necessary)
    return Decision(FINAL, units, {uid: cited for uid in units})


class Policy:
    name = "policy"

    def reset(self) -> None:
        pass

    def decide(self, obs: Observation) -> Decision:
        raise NotImplementedError


class WaitAll(Policy):
    """Stay silent until retrieval completes, then answer."""
    name = "wait_all"

    def decide(self, obs):
        return _answer_everything(obs) if obs.retrieval_done else Decision(WAIT)


class FixedProgress(Policy):
    """Say one progress utterance at a fixed time, then behave like Wait-All."""
    name = "fixed_progress"

    def __init__(self, progress_at_s: float = 1.0):
        self.progress_at_s = progress_at_s

    def reset(self):
        self._said_progress = False

    def decide(self, obs):
        if obs.retrieval_done:
            return _answer_everything(obs)
        if not self._said_progress and obs.time_s >= self.progress_at_s:
            self._said_progress = True
            return Decision(PROGRESS)
        return Decision(WAIT)


class TimeOnly(Policy):
    """Answer at a fixed elapsed time, whatever evidence has arrived."""
    name = "time_only"

    def __init__(self, answer_at_s: float = 3.0):
        self.answer_at_s = answer_at_s

    def decide(self, obs):
        if obs.retrieval_done or obs.time_s >= self.answer_at_s:
            return _answer_everything(obs)
        return Decision(WAIT)


class FirstEvidence(Policy):
    """Answer as soon as any evidence is visible."""
    name = "first_evidence"

    def decide(self, obs):
        if obs.retrieval_done or obs.evidence:
            return _answer_everything(obs)
        return Decision(WAIT)


class EvidenceAware(Policy):
    """Ours: map the judged sufficiency state to an action.

    insufficient -> Backchannel once, Progress once after progress_after_s, else Wait
    partial      -> Partial Answer with newly supported units, else as insufficient
    full         -> Final Answer with the necessary units not yet said
    Retrieval finished but still not full -> Final Answer with only the supported units.
    """
    name = "evidence_aware"

    def __init__(self, judge: Judge, progress_after_s: float = 3.0):
        self.judge = judge
        self.progress_after_s = progress_after_s
        self.name = f"evidence_aware+{judge.name}"

    def reset(self):
        self._said_units: Set[str] = set()
        self._said_backchannel = False
        self._said_progress = False

    def decide(self, obs):
        labels = resolve_dependencies(obs.units, self.judge.judge(obs))
        label_names = {uid: j.label for uid, j in labels.items()}
        supported = [u for u in obs.units if labels[u.unit_id].label == SUPPORTED]
        new = [u for u in supported if u.unit_id not in self._said_units]

        def claim(action, units):
            ids = tuple(u.unit_id for u in units)
            self._said_units.update(ids)
            return Decision(action, ids, {i: labels[i].citations for i in ids}, label_names)

        if sufficiency_state(obs.units, labels) == FULLY_SUFFICIENT:
            return claim(FINAL, [u for u in new if u.necessary])
        if obs.retrieval_done:
            return claim(FINAL, new)
        if new:
            return claim(PARTIAL, new)
        if not self._said_backchannel:
            self._said_backchannel = True
            return Decision(BACKCHANNEL, unit_labels=label_names)
        if not self._said_progress and not self._said_units and obs.time_s >= self.progress_after_s:
            self._said_progress = True
            return Decision(PROGRESS, unit_labels=label_names)
        return Decision(WAIT, unit_labels=label_names)
