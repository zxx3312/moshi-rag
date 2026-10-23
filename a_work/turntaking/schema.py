"""Names and record types shared with B's interface v1.

Action and label strings must match b_work/step1/experiment_config.json exactly.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Optional, Tuple

SCHEMA_VERSION = "1.0"

ACTIONS = ("Wait", "Backchannel", "Progress", "Partial Answer", "Final Answer")
WAIT, BACKCHANNEL, PROGRESS, PARTIAL, FINAL = ACTIONS

LABELS = ("SUPPORTED", "UNRESOLVED", "CONTRADICTED")
SUPPORTED, UNRESOLVED, CONTRADICTED = LABELS

# Sufficiency states (proposal Sec. 3.1).
INSUFFICIENT, PARTIALLY_SUFFICIENT, FULLY_SUFFICIENT = "insufficient", "partial", "full"


@dataclass(frozen=True)
class Evidence:
    evidence_id: str
    text: str
    visible_time_s: float
    source: dict


@dataclass(frozen=True)
class Unit:
    """Controller-side answer unit. Never carries a gold answer."""
    unit_id: str
    description: str
    necessary: bool
    depends_on: Tuple[str, ...] = ()


@dataclass(frozen=True)
class Observation:
    """Everything an ordinary policy may see at time t (no future evidence, no gold)."""
    sample_id: str
    question: str
    time_s: float
    evidence: Tuple[Evidence, ...]
    units: Tuple[Unit, ...]
    retrieval_done: bool


@dataclass(frozen=True)
class UnitJudgment:
    label: str
    citations: Tuple[str, ...] = ()
    value: Optional[str] = None


@dataclass
class Decision:
    action: str
    claimed_units: Tuple[str, ...] = ()
    citations: Dict[str, Tuple[str, ...]] = field(default_factory=dict)
    unit_labels: Optional[Dict[str, str]] = None
