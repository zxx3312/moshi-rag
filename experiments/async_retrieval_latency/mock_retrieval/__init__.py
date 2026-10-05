"""Deterministic mock retrieval backend for the async retrieval latency experiment."""

from .fixed_reference import FixedReferenceBackend, RetrievalResult, delay_to_steps

__all__ = ["FixedReferenceBackend", "RetrievalResult", "delay_to_steps"]
