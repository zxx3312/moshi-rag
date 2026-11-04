"""Score structured claims without calling a model or guessing unclear mappings."""

from collections import Counter
import re
import unicodedata

from .records import normalize_log, require


PLACEHOLDER = re.compile(r"\[[^\]\n]*<-[^\]\n]*\]")


def normalize_answer(text):
    """Use lowercase text without accents, punctuation, articles, or extra spaces."""
    text = unicodedata.normalize("NFKD", text.casefold())
    text = "".join(c for c in text if not unicodedata.combining(c) and not unicodedata.category(c).startswith("P"))
    return " ".join(word for word in text.split() if word not in {"a", "an", "the"})


def answer_scores(value, answers):
    """Return the best exact match and token F1 across accepted answer forms."""
    predicted = normalize_answer(value).split()
    exact, best_f1 = 0.0, 0.0
    for answer in answers:
        expected = normalize_answer(answer).split()
        exact = max(exact, float(predicted == expected and bool(expected)))
        overlap = sum((Counter(predicted) & Counter(expected)).values())
        if overlap:
            best_f1 = max(best_f1, 2.0 * overlap / (len(predicted) + len(expected)))
    return exact, best_f1


def answers_of(unit):
    """Read the main answer and its accepted surface forms."""
    return [unit["expected_answer"]] + unit.get("aliases", [])


def contains_value(text, value):
    """Check whole tokens, so the value 'no' does not match 'Norman'."""
    value = normalize_answer(value)
    return bool(value) and (" " + value + " ") in (" " + normalize_answer(text) + " ")


def supported_units(units, visible):
    """Apply gold support/dependency rules to one fixed evidence snapshot."""
    memo = {}

    def supported(uid):
        """Gold graphs are checked for cycles before this function is called."""
        if uid not in memo:
            unit = units[uid]
            parents = [supported(parent) for parent in unit["depends_on"]]
            deps_ok = all(parents)
            direct = any(set(inner) <= visible for inner in unit["support_sets"])
            premise = any(set(inner) <= visible for inner in unit.get("presupposition_sets", []))
            # A question premise may replace missing branches, but still needs visible evidence.
            memo[uid] = (direct and deps_ok) or (premise and (any(parents) or not parents))
        return memo[uid]

    return {uid for uid in units if supported(uid)}


def citation_support(uid, units, visible, citations):
    """Require a full cited support set, not just evidence that happened to arrive."""
    supported = supported_units(units, visible)
    memo = {}

    def cited(unit_id):
        """For a comparison with no new evidence, check its parents' citations."""
        if unit_id not in memo:
            unit = units[unit_id]
            parents = unit["depends_on"]
            result = False
            if unit_id in supported:
                # A premise path cannot make a blocked normal support path valid.
                normal_sets = unit["support_sets"] if all(parent in supported for parent in parents) else []
                for inner in normal_sets:
                    if inner and set(inner) <= citations:
                        result = True
                    elif not inner:
                        parent_cites = [parent in supported and cited(parent) for parent in parents]
                        result = result or all(parent_cites)
                premise = any(set(inner) <= citations for inner in unit.get("presupposition_sets", []))
                result = result or (premise and (not parents or any(p in supported for p in parents)))
            memo[unit_id] = bool(result)
        return memo[unit_id]

    # The log checker already requires every citation to be in the visible snapshot.
    return cited(uid)


def score_claim(record, claim, record_index, claim_index, units, reviews, aligned_policies, allow_value_match):
    """Map one declared claim to gold, or keep it for human/external review."""
    value = claim.get("value")
    candidates = [uid for uid, unit in units.items()
                  if isinstance(value, str) and answer_scores(value, answers_of(unit))[0] == 1]
    result = {"run_id": record["run_id"], "trace_id": record["trace_id"],
              "record_index": record_index, "claim_index": claim_index,
              "text": claim["text"], "value": value, "candidate_gold_unit_ids": candidates,
              "gold_unit_id": None, "mapping_source": None, "label": "NEEDS_REVIEW",
              "reason": None, "em": None, "f1": None,
              "start": claim["start"], "end": claim["end"],
              "by_omission": False, "by_presupposition": False}
    if not isinstance(value, str) or not value.strip():
        result["reason"] = "missing_claim_value"
        return result
    key = (record["run_id"], record_index, claim_index)
    if key in reviews:
        uid, source = reviews[key]["gold_unit_id"], "review"
        require(uid in units, "Review names an unknown gold unit: " + uid)
    elif record["policy"] in aligned_policies and claim.get("controller_unit_id") in units:
        uid, source = claim["controller_unit_id"], "aligned_policy"
    else:
        necessary = [uid for uid, unit in units.items() if unit["necessary"]]
        # A's free-answer baseline uses 'answer' for the whole question.
        if claim.get("controller_unit_id") == "answer" and record["action"] == "Final Answer" and len(necessary) == 1:
            uid, source = necessary[0], "single_answer"
        elif allow_value_match and len(candidates) == 1:
            uid, source = candidates[0], "value_guess"
        else:
            result["reason"] = "ambiguous_gold_value" if len(candidates) > 1 else "claim_mapping_required"
            return result
    unit = units[uid]
    exact, f1 = answer_scores(value, answers_of(unit))
    # A correct value in metadata is not enough: it must also occur in the output.
    spoken = contains_value(claim["text"], value)
    if exact == 1:
        spoken = spoken or any(contains_value(claim["text"], answer) for answer in answers_of(unit))
    if not spoken:
        result["reason"] = "value_not_found_in_claim_text"
        return result
    snapshot = set(record["evidence_snapshot_ids"])
    cited = set(claim["cited_evidence_ids"])
    supported = exact == 1 and citation_support(uid, units, snapshot, cited)
    result.update(gold_unit_id=uid, mapping_source=source, em=exact, f1=f1,
                  label="SUPPORTED" if supported else "UNSUPPORTED",
                  reason="gold_support_and_citations" if supported else ("wrong_gold_value" if exact != 1 else "missing_gold_support_or_citation"),
                  by_omission=supported and unit.get("by_omission", False),
                  by_presupposition=supported and unit.get("by_presupposition", False))
    return result


def empty_metrics():
    """Unknown or excluded scores stay null instead of becoming zero."""
    return {"unit_em": None, "unit_f1": None, "answer_complete": None,
            "grounded_complete": None, "unsupported_claim_rate": None,
            "unsupported_rate_on_scored_claims": None, "claim_coverage": None,
            "ttfr_s": None, "ttfgi_s": None, "ttca_s": None}


def score_run(rows, trace, gold, reviews=None, aligned_policies=(), allow_value_match=False,
              allow_placeholder=False, timing_kind="unknown"):
    """Check one run, then score its supplied structured claims with clear limits."""
    reviews = {} if reviews is None else reviews
    require(timing_kind in {"unknown", "estimated", "observed"}, "Unknown timing kind")
    require(timing_kind != "observed" or trace["clock"] == "audio_stream",
            "Observed speech timing needs an audio_stream trace")
    first = rows[0]
    result = {key: first[key] for key in ["run_id", "trace_id", "sample_id", "policy", "seed"]}
    result.update(data_version=trace["data_version"], clock=trace["clock"], timing_kind=timing_kind,
                  status="ok", final_answer_attempted=False, records=len(rows), claims_total=0,
                  claims_scored=0, claims_needing_review=0, supported_claims=0, unsupported_claims=0,
                  approximate_mapping_claims=0, by_omission_supported=0, by_presupposition_supported=0,
                  validation_issues=[], review_reasons=[], **empty_metrics())
    clean = []
    previous_time = -float("inf")
    for index, row in enumerate(rows):
        try:
            record = normalize_log(row, trace)
            require(all(record[key] == first[key] for key in ["run_id", "trace_id", "sample_id", "policy", "seed"]), "Identity changes within run")
            require(record["decision_time_s"] >= previous_time, "Decisions go backwards")
            previous_time = record["decision_time_s"]
            clean.append(record)
        except (ValueError, TypeError, KeyError) as error:
            result["validation_issues"].append({"record_index": index, "reason": str(error)})
    if result["validation_issues"]:
        result["status"] = "invalid"
        return result, []
    result["claims_total"] = sum(len(record["claim_spans"]) for record in clean)
    result["final_answer_attempted"] = any(record["action"] == "Final Answer" for record in clean)
    if any(record["status"] == "error" for record in clean):
        result["status"] = "error"
        return result, []
    placeholder = any(PLACEHOLDER.search(record["text"]) for record in clean)
    if placeholder and not allow_placeholder:
        result["status"] = "placeholder"
        result["review_reasons"].append("Run used A's placeholder renderer; no answer scores were produced.")
        return result, []
    if placeholder:
        result["status"] = "diagnostic"
    units = {unit["unit_id"]: unit for unit in gold["units"]}
    necessary = {uid for uid, unit in units.items() if unit["necessary"]}
    all_evidence = {event["evidence_id"] for event in trace["events"]}
    result["unreachable_necessary_units"] = sorted(necessary - supported_units(units, all_evidence))
    result["missing_gold_evidence_ids"] = sorted({eid for unit in units.values()
                                                for field in ["support_sets", "presupposition_sets"]
                                                for inner in unit.get(field, []) for eid in inner} - all_evidence)
    claims = []
    for record_index, record in enumerate(clean):
        for claim_index, claim in enumerate(record["claim_spans"]):
            claims.append(score_claim(record, claim, record_index, claim_index, units,
                                      reviews, set(aligned_policies), allow_value_match))
    scored = [claim for claim in claims if claim["label"] != "NEEDS_REVIEW"]
    grounded = [claim for claim in scored if claim["label"] == "SUPPORTED"]
    pending = [claim for claim in claims if claim["label"] == "NEEDS_REVIEW"]
    total, count = len(claims), len(scored)
    unsupported = count - len(grounded)
    result.update(claims_scored=count, claims_needing_review=len(pending), supported_claims=len(grounded),
                  unsupported_claims=unsupported, approximate_mapping_claims=sum(c["mapping_source"] == "value_guess" for c in scored),
                  by_omission_supported=sum(c["by_omission"] for c in grounded),
                  by_presupposition_supported=sum(c["by_presupposition"] for c in grounded))
    if total:
        result["claim_coverage"] = count / total
        result["unsupported_rate_lower_bound"] = unsupported / total
        result["unsupported_rate_upper_bound"] = (unsupported + len(pending)) / total
        if not pending:
            result["unsupported_claim_rate"] = unsupported / total
    if count:
        result["unsupported_rate_on_scored_claims"] = unsupported / count
    for uid in units:
        attempts = [c for c in scored if c["gold_unit_id"] == uid]
        # Do not silently choose the good answer when later output may correct or retract it.
        if len({normalize_answer(c["value"]) for c in attempts}) > 1 and any(c["em"] != 1 for c in attempts):
            result["review_reasons"].append("conflicting_values_for_unit:" + uid)
    final_positions = [i for i, record in enumerate(clean) if record["action"] == "Final Answer"]
    if final_positions and final_positions[0] < len(clean) - 1:
        result["review_reasons"].append("output_after_final_answer")
    best_em = {uid: max([c["em"] for c in scored if c["gold_unit_id"] == uid] or [0.0]) for uid in necessary}
    best_f1 = {uid: max([c["f1"] for c in scored if c["gold_unit_id"] == uid] or [0.0]) for uid in necessary}
    needs_review = bool(pending or result["review_reasons"])
    if not needs_review:
        result["unit_em"] = sum(best_em.values()) / len(necessary)
        result["unit_f1"] = sum(best_f1.values()) / len(necessary)
        result["answer_complete"] = all(score == 1 for score in best_em.values())
        result["grounded_complete"] = necessary <= {c["gold_unit_id"] for c in grounded}
    if timing_kind != "unknown":
        audible = [record for record in clean if record["action"] != "Wait" and record["text"].strip()]
        starts = [record["output_start_time_s"] for record in audible]
        if starts and None not in starts:
            result["ttfr_s"] = min(starts)
        if grounded and not needs_review and all(c["start"] is not None for c in grounded):
            result["ttfgi_s"] = min(c["start"] for c in grounded)
        if result["grounded_complete"]:
            required_claims = [c for c in grounded if c["gold_unit_id"] in necessary]
            if all(c["end"] is not None for c in required_claims):
                first_ends = [min(c["end"] for c in required_claims if c["gold_unit_id"] == uid) for uid in necessary]
                result["ttca_s"] = max(first_ends)
    return result, claims
