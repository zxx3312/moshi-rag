"""Per-run metrics computed from a trace JSON written by ``scripts/latency_job.py``.

Pure stdlib, so it can be re-run on a login node with different thresholds.

Time convention: every ``*_time`` is in seconds on the model stream clock,
i.e. ``step / frame_rate`` since the first input frame of the sample (step 0).
Wall-clock times are meaningless here because offline inference runs faster
than real time.

Precision of each field (see README "What is measured and how precisely"):
- exact by construction: retrieval_request_time, retrieval_complete_time
- exact to the frame (80 ms): retrieval_trigger_time, reference_injection_time
  (the condition takes effect on the next LM step, i.e. within ~1-2 frames)
- approximate (energy / string heuristics): user_end_time, assistant_first_audio_time,
  first_informative_content_time, silence and filler statistics
"""

from __future__ import annotations

import re
import unicodedata
from typing import Any

PAD = "<pad>"
SPECIAL_TOKEN_RE = re.compile(r"^<[^>]+>$")
NON_ALNUM_RE = re.compile(r"[^a-z0-9\s]+")
WS_RE = re.compile(r"\s+")

# Heuristic filler / progress-utterance lexicon. Matches are counted, not judged:
# whether a phrase is a "natural" progress utterance needs human or LLM judgement.
FILLER_PHRASES = (
    "um",
    "uh",
    "hmm",
    "well",
    "let me see",
    "let me think",
    "let me check",
    "good question",
    "great question",
    "that s a good question",
    "that s a great question",
    "i think",
    "you know",
    "so",
    "okay",
    "oh",
)

DEFAULT_SPEECH_DB = -45.0  # user input frame counts as speech above this RMS (dBFS)
DEFAULT_AUDIBLE_DB = -45.0  # model output frame counts as audible above this RMS (dBFS)


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii").lower()
    return WS_RE.sub(" ", NON_ALNUM_RE.sub(" ", text)).strip()


def is_content_piece(piece: str | None) -> bool:
    return bool(piece) and piece != PAD and not SPECIAL_TOKEN_RE.match(piece)


def pieces_to_text(pieces: list[str]) -> str:
    parts = [p.replace("▁", " ") for p in pieces if is_content_piece(p)]
    return WS_RE.sub(" ", "".join(parts)).strip()


def _t(step: int | None, fr: float) -> float | None:
    return None if step is None or step < 0 else round(step / fr, 4)


def _audible(db: float | None, threshold: float) -> bool:
    return db is not None and db > threshold


def _longest_run(flags: list[bool]) -> int:
    best = cur = 0
    for f in flags:
        cur = cur + 1 if f else 0
        best = max(best, cur)
    return best


def _runs(flags: list[bool]) -> list[int]:
    out, cur = [], 0
    for f in flags:
        if f:
            cur += 1
        elif cur:
            out.append(cur)
            cur = 0
    if cur:
        out.append(cur)
    return out


def _window_stats(trace: dict[str, Any], start: int | None, end: int | None, audible_db: float) -> dict[str, Any]:
    """Speech/text statistics for model output steps in ``[start, end)``."""
    fr = float(trace["experiment"]["frame_rate"])
    model_text: list[str] = trace.get("model_text") or []
    rms: list[float | None] = trace.get("model_rms_db") or []
    if start is None or end is None or end <= start:
        return {"duration_s": 0.0, "transcript": "", "num_words": 0, "num_text_tokens": 0,
                "speech_s": 0.0, "silence_s": 0.0, "longest_silence_s": 0.0}
    end = min(end, len(model_text))
    pieces = model_text[start:end]
    text = pieces_to_text(pieces)
    audible = [_audible(rms[i] if i < len(rms) else None, audible_db) for i in range(start, end)]
    return {
        "duration_s": round((end - start) / fr, 4),
        "transcript": text,
        "num_words": len(text.split()),
        "num_text_tokens": sum(1 for p in pieces if is_content_piece(p)),
        "speech_s": round(sum(audible) / fr, 4),
        "silence_s": round((len(audible) - sum(audible)) / fr, 4),
        "longest_silence_s": round(_longest_run([not a for a in audible]) / fr, 4),
    }


def _filler_stats(text: str) -> dict[str, Any]:
    norm = f" {normalize_text(text)} "
    counts = {}
    for phrase in FILLER_PHRASES:
        n = norm.count(f" {phrase} ")
        if n:
            counts[phrase] = n
    words = norm.split()
    max_ngram_repeat = 0
    for n in (2, 3):
        grams: dict[tuple[str, ...], int] = {}
        for i in range(len(words) - n + 1):
            g = tuple(words[i : i + n])
            grams[g] = grams.get(g, 0) + 1
        if grams:
            max_ngram_repeat = max(max_ngram_repeat, max(grams.values()))
    return {
        "filler_counts": counts,
        "filler_total": sum(counts.values()),
        "max_ngram_repeat": max_ngram_repeat,
        "repeated_filler": any(v >= 2 for v in counts.values()) or max_ngram_repeat >= 2,
    }


def _answer_mention_step(trace: dict[str, Any], start: int, answers: list[str]) -> tuple[int | None, str | None]:
    """First step >= start at which the cumulative model transcript contains a gold answer string."""
    targets = [a for a in (normalize_text(x) for x in answers) if a]
    if not targets:
        return None, None
    model_text: list[str] = trace.get("model_text") or []
    cumulative = ""
    for i in range(max(start, 0), len(model_text)):
        p = model_text[i]
        if not is_content_piece(p):
            continue
        cumulative += p.replace("▁", " ")
        norm = f" {normalize_text(cumulative)} "
        for a in targets:
            if f" {a} " in norm:
                return i, a
    return None, None


def answers_from_field(answer: Any) -> list[str]:
    if answer is None:
        return []
    if isinstance(answer, str):
        return [answer]
    if isinstance(answer, (list, tuple)):
        return [str(a) for a in answer]
    if isinstance(answer, dict):
        out = []
        for k in ("value", "normalized_value"):
            if answer.get(k):
                out.append(str(answer[k]))
        for k in ("aliases", "normalized_aliases"):
            out.extend(str(a) for a in answer.get(k) or [])
        return out
    return [str(answer)]


def compute_metrics(
    trace: dict[str, Any],
    speech_db: float = DEFAULT_SPEECH_DB,
    audible_db: float = DEFAULT_AUDIBLE_DB,
) -> dict[str, Any]:
    exp = trace["experiment"]
    fr = float(exp["frame_rate"])
    model_text: list[str] = trace.get("model_text") or []
    rms: list[float | None] = trace.get("model_rms_db") or []
    user_rms: list[float | None] = trace.get("user_rms_db") or []
    n_steps = len(model_text)
    input_frames = int(exp["input_frames"])

    # User end: last input frame above the speech threshold (approximate, energy based).
    speech_frames = [i for i, db in enumerate(user_rms) if db is not None and db > speech_db]
    user_speech_end_step = (speech_frames[-1] + 1) if speech_frames else None
    user_end_step = user_speech_end_step if user_speech_end_step is not None else input_frames

    events: list[dict[str, Any]] = trace.get("retrieval_events") or []
    first = events[0] if events else None
    trigger_step = first["trigger_step"] if first else None
    request_step = first["request_step"] if first else None
    available_step = first["available_step"] if first else None
    injection_step = first.get("injection_step") if first else None
    injection_len = first.get("injection_num_steps") if first else None

    # Assistant onset after the user stopped speaking.
    first_text_step = next((i for i in range(user_end_step, n_steps) if is_content_piece(model_text[i])), None)
    first_audio_step = next(
        (i for i in range(user_end_step, min(n_steps, len(rms))) if _audible(rms[i], audible_db)), None
    )
    last_text_step = next((i for i in range(n_steps - 1, user_end_step - 1, -1) if is_content_piece(model_text[i])), None)
    last_audio_step = next(
        (i for i in range(min(n_steps, len(rms)) - 1, user_end_step - 1, -1) if _audible(rms[i], audible_db)), None
    )

    # Silences inside the response (between user end and the last audible frame).
    gap_runs: list[int] = []
    if last_audio_step is not None:
        inaudible = [not _audible(rms[i], audible_db) for i in range(user_end_step, last_audio_step + 1)]
        gap_runs = _runs(inaudible)

    answers = answers_from_field(trace.get("answer"))
    mention_step, mention = _answer_mention_step(trace, user_end_step, answers)

    pre_trigger = _window_stats(trace, user_end_step, trigger_step, audible_db) if trigger_step is not None else None
    pre_rag = _window_stats(trace, trigger_step, injection_step if injection_step is not None else n_steps, audible_db) \
        if trigger_step is not None else None
    wait_window = _window_stats(trace, user_end_step, injection_step, audible_db) if injection_step is not None else None
    post_rag = _window_stats(trace, injection_step, n_steps, audible_db) if injection_step is not None else None

    out: dict[str, Any] = {
        "sample_id": exp["sample_id"],
        "question": exp.get("question"),
        "retrieval_delay_condition": exp["delay_condition_s"],
        "effective_delay_s": exp["effective_delay_s"],
        "delay_steps": exp["delay_steps"],
        "seed": exp["seed"],
        "status": exp.get("status"),
        "stop_reason": exp.get("stop_reason"),
        "rag_triggered": first is not None,
        "num_retrievals": len(events),
        # --- timestamps (stream seconds since sample start) ---
        "input_end_time": _t(input_frames, fr),
        "user_end_time": _t(user_end_step, fr),
        "user_end_time_source": "energy" if user_speech_end_step is not None else "input_end",
        "retrieval_trigger_time": _t(trigger_step, fr),
        "retrieval_request_time": _t(request_step, fr),
        "retrieval_complete_time": _t(available_step, fr),
        "reference_injection_time": _t(injection_step, fr),
        "reference_ingestion_end_time": _t(injection_step + injection_len, fr)
        if injection_step is not None and injection_len is not None else None,
        "assistant_first_text_time": _t(first_text_step, fr),
        "assistant_first_audio_time": _t(first_audio_step, fr),
        "first_informative_content_time": _t(mention_step, fr),
        "first_informative_content_match": mention,
        "response_end_time": _t(last_audio_step + 1, fr) if last_audio_step is not None else None,
        "response_end_text_time": _t(last_text_step + 1, fr) if last_text_step is not None else None,
        # --- derived latencies (seconds) ---
        "trigger_to_injection_s": _t(injection_step - trigger_step, fr)
        if injection_step is not None and trigger_step is not None else None,
        "response_onset_latency_s": _t(first_audio_step - user_end_step, fr) if first_audio_step is not None else None,
        "first_text_latency_s": _t(first_text_step - user_end_step, fr) if first_text_step is not None else None,
        "first_informative_latency_s": _t(mention_step - user_end_step, fr) if mention_step is not None else None,
        "answer_mentioned_before_injection": (mention_step < injection_step)
        if mention_step is not None and injection_step is not None else None,
        "trigger_before_user_end": (trigger_step < user_end_step) if trigger_step is not None else None,
        # --- silence ---
        "longest_response_silence_s": _t(max(gap_runs), fr) if gap_runs else 0.0,
        "num_silences_ge_1s": sum(1 for r in gap_runs if r / fr >= 1.0),
        "num_silences_ge_2s": sum(1 for r in gap_runs if r / fr >= 2.0),
        # --- windows ---
        "pre_trigger": pre_trigger,
        "pre_rag": pre_rag,  # [trigger, injection)
        "wait_window": wait_window,  # [user_end, injection)
        "post_rag": post_rag,  # [injection, end)
        "pre_rag_filler": _filler_stats(pre_rag["transcript"]) if pre_rag else None,
        # --- texts ---
        "assistant_transcript": pieces_to_text(model_text),
        "pre_rag_transcript": pre_rag["transcript"] if pre_rag else None,
        "post_rag_transcript": post_rag["transcript"] if post_rag else None,
        "user_transcript_stt": pieces_to_text(trace.get("user_text") or []),
        "reference_text": trace.get("reference_text"),
        "answer": trace.get("answer"),
        "output_audio_path": exp.get("output_audio_path"),
        "stereo_audio_path": exp.get("stereo_audio_path"),
        "trace_path": exp.get("trace_path"),
        "wall_elapsed_s": exp.get("wall_elapsed_s"),
        "thresholds": {"speech_db": speech_db, "audible_db": audible_db},
    }
    return out
