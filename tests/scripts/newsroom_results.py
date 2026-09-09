"""Fixed-family summaries of already validated model-only newsroom assessments."""

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from statistics import median
from typing import Mapping

from tests.scripts import evaluate, newsroom_stats


VARIANTS = ("full", "bare-task")
LEVELS = ("absent", "minor", "salient", "unassessable")
FIDELITY = ("no_flag", "flag", "uncertain")
HALF = Fraction(1, 2)


@dataclass(frozen=True)
class Pointwise:
    level: str
    fidelity: str

    def __post_init__(self):
        evaluate.require(isinstance(self.level, str) and self.level in LEVELS, "unknown pointwise level")
        evaluate.require(isinstance(self.fidelity, str) and self.fidelity in FIDELITY, "unknown fidelity label")


def score_preference(winner: str, full_is_a: bool) -> Fraction:
    evaluate.require(isinstance(winner, str) and winner in ("a", "b", "tie"), "unknown winner")
    evaluate.require(type(full_is_a) is bool, "full_is_a must be a boolean")
    if winner == "tie":
        return HALF
    return Fraction(int((winner == "a") == full_is_a))


def _positive_count(value, label):
    evaluate.require(type(value) is int and value > 0, f"{label}: expected a positive integer")


def validate_allocation(allocation: dict) -> dict:
    evaluate.require(isinstance(allocation, dict), "expected an allocation object")
    evaluate.verify_seal(allocation, "allocation_sha256")
    evaluate.version(allocation)
    evaluate.require(allocation.get("kind") == "newsroom-primary-allocation", "wrong allocation kind")
    for field in ("writers", "judges"):
        values = allocation.get(field)
        evaluate.require(isinstance(values, list) and len(values) == 2
                         and all(isinstance(value, str) and value.strip() and value != "auto" for value in values)
                         and len(set(values)) == 2, f"{field}: expected two explicit distinct models")
    evaluate.require(set(allocation["writers"]) == set(allocation["judges"]), "both writers must judge every case")
    evaluate.require(allocation.get("variants") == list(VARIANTS), "expected full versus genuine bare-task")
    for field in ("family_count", "case_count"):
        _positive_count(allocation.get(field), field)
    families, cases = allocation.get("families"), allocation.get("cases")
    evaluate.require(isinstance(families, list) and len(families) == allocation["family_count"], "family count mismatch")
    evaluate.require(isinstance(cases, list) and len(cases) == allocation["case_count"], "case count mismatch")
    case_map, job_ids = {}, set()
    for case in cases:
        evaluate.require(isinstance(case, dict), "expected a case allocation")
        identifier = evaluate.nonempty(case.get("case_id"), "case_id")
        evaluate.require(identifier not in case_map, "duplicate allocated case")
        evaluate.nonempty(case.get("family_id"), "family_id")
        evaluate.require(case.get("writer") in allocation["writers"], "unallocated writer")
        evaluate.require(type(case.get("full_is_a")) is bool, "invalid blinded orientation")
        for field in ("writing_job_ids", "request_sha256"):
            evaluate.require(isinstance(case.get(field), dict) and set(case[field]) == set(VARIANTS),
                             f"{identifier}: incomplete {field}")
        for variant in VARIANTS:
            job = evaluate.nonempty(case["writing_job_ids"][variant], "writing job ID")
            evaluate.require(job not in job_ids, "duplicate writing job ID")
            job_ids.add(job)
            value = case["request_sha256"][variant]
            evaluate.require(isinstance(value, str) and evaluate.HASH.fullmatch(value) is not None,
                             "invalid prepared-request seal")
        evaluate.require(len(set(case["request_sha256"].values())) == 2, "both variants cannot share a request")
        case_map[identifier] = case
    evaluate.require({row["writer"] for row in cases} == set(allocation["writers"]),
                     "each declared writer must have assigned cases")
    family_ids, assigned_cases = set(), set()
    for family in families:
        evaluate.require(isinstance(family, dict), "expected a family allocation")
        identifier = evaluate.nonempty(family.get("family_id"), "family_id")
        evaluate.require(identifier not in family_ids, "duplicate family")
        family_ids.add(identifier)
        members = family.get("case_ids")
        evaluate.require(isinstance(members, list) and bool(members)
                         and all(isinstance(value, str) for value in members)
                         and len(members) == len(set(members)), "invalid family members")
        evaluate.require(set(members) <= set(case_map) and assigned_cases.isdisjoint(members),
                         "missing or multiply assigned family member")
        assigned_cases.update(members)
        for member in members:
            evaluate.require(case_map[member]["family_id"] == identifier
                             and case_map[member]["writer"] == family.get("writer"),
                             "family/case allocation mismatch")
        components = 2 * len(members)
        evaluate.require(type(family.get("preference_components")) is int
                         and family["preference_components"] == components, "planned judge weight mismatch")
        evaluate.require(type(family.get("score_grid_denominator")) is int
                         and family["score_grid_denominator"] == 2 * components, "planned score grid mismatch")
    evaluate.require(assigned_cases == set(case_map), "unassigned cases")
    slots = allocation.get("judgment_slots")
    evaluate.require(isinstance(slots, list), "expected planned judgment slots")
    observed, slot_ids = set(), set()
    for slot in slots:
        evaluate.fields(slot, {"id", "kind", "case_id", "family_id", "writer", "judge", "variant"}, "judgment slot")
        identifier = evaluate.nonempty(slot["id"], "judgment slot ID")
        evaluate.require(identifier not in slot_ids, "duplicate judgment slot ID")
        slot_ids.add(identifier)
        evaluate.require(isinstance(slot["case_id"], str) and slot["case_id"] in case_map, "unknown slot case")
        case = case_map[slot["case_id"]]
        evaluate.require(slot["family_id"] == case["family_id"] and slot["writer"] == case["writer"],
                         "judgment slot allocation mismatch")
        evaluate.require(slot["judge"] in allocation["judges"], "unknown planned judge")
        evaluate.require(slot["kind"] in ("preference", "pointwise"), "unknown assessment kind")
        valid_variant = slot["variant"] is None if slot["kind"] == "preference" else slot["variant"] in VARIANTS
        evaluate.require(valid_variant, "unexpected assessment variant")
        key = (slot["case_id"], slot["kind"], slot["variant"], slot["judge"])
        evaluate.require(key not in observed, "duplicate planned assessment")
        observed.add(key)
    expected = {
        (case, kind, variant, judge)
        for case in case_map for judge in allocation["judges"]
        for kind, variant in (("preference", None), ("pointwise", "full"), ("pointwise", "bare-task"))
    }
    evaluate.require(observed == expected, "planned assessments omit or add contributions")
    counts = {
        "writing_calls_planned": len(job_ids),
        "preference_calls_planned": 2 * len(cases),
        "pointwise_calls_planned": 4 * len(cases),
    }
    for field, count in counts.items():
        evaluate.require(type(allocation.get(field)) is int and allocation[field] == count, f"{field}: mismatch")
    return allocation


def _mean_bounds(rows: list[newsroom_stats.FamilyBounds]) -> dict:
    lower = sum((row.lower for row in rows), Fraction(0)) / len(rows)
    upper = sum((row.upper for row in rows), Fraction(0)) / len(rows)
    return {
        "families": len(rows), "complete_families": sum(row.lower == row.upper for row in rows),
        "lower": float(lower), "upper": float(upper),
        "lower_fraction": str(lower), "upper_fraction": str(upper),
        "kind": "fixed-weight missing-score bounds, not a confidence interval",
    }


def _counts(values: list[Fraction | None]) -> dict:
    return {
        "planned": len(values), "full_wins": values.count(Fraction(1)),
        "ties": values.count(HALF), "bare_wins": values.count(Fraction(0)),
        "missing": values.count(None),
    }


def summarize(
    allocation: dict,
    thresholds: Mapping[str, newsroom_stats.FamilyDraw],
    preferences: Mapping[str, Fraction | None],
    pointwise: Mapping[str, Pointwise | None],
    responses: Mapping[str, str | None],
) -> dict:
    """Summarize validated inputs; this function does not authenticate SDK captures."""
    validate_allocation(allocation)
    families, cases, judges = allocation["families"], allocation["cases"], allocation["judges"]
    case_map = {row["case_id"]: row for row in cases}
    slots = allocation["judgment_slots"]
    for kind, values in (("preference", preferences), ("pointwise", pointwise)):
        evaluate.require(isinstance(values, Mapping)
                         and set(values) == {row["id"] for row in slots if row["kind"] == kind},
                         f"{kind}: supply every planned slot, with explicit None for missing")
    evaluate.require(isinstance(responses, Mapping) and set(responses) == {
        job for case in cases for job in case["writing_job_ids"].values()
    }, "responses: supply every planned writing slot, with explicit None for missing")
    for value in preferences.values():
        evaluate.require(value is None or isinstance(value, Fraction) and value in (0, HALF, 1),
                         "preferences must be exact Fraction scores or explicit None")
    for value in pointwise.values():
        evaluate.require(value is None or isinstance(value, Pointwise), "expected a pointwise rating or None")
    for value in responses.values():
        evaluate.require(value is None or isinstance(value, str) and bool(value.strip()), "invalid writing response")
    preference_by_key, pointwise_by_key = {}, {}
    for slot in slots:
        case = case_map[slot["case_id"]]
        variants = VARIANTS if slot["kind"] == "preference" else (slot["variant"],)
        available = all(responses[case["writing_job_ids"][variant]] is not None for variant in variants)
        value = preferences[slot["id"]] if slot["kind"] == "preference" else pointwise[slot["id"]]
        evaluate.require(available or value is None, "an assessment cannot exist without its writing input")
        if slot["kind"] == "preference":
            preference_by_key[(slot["case_id"], slot["judge"])] = value
        else:
            pointwise_by_key[(slot["case_id"], slot["variant"], slot["judge"])] = value

    def preference_families(writer=None, judge=None):
        return [newsroom_stats.from_preferences(row["family_id"], [
            preference_by_key[(case, rater)]
            for case in row["case_ids"] for rater in ([judge] if judge else judges)
        ]) for row in families if writer is None or row["writer"] == writer]

    bounds = preference_families()
    primary = newsroom_stats.analyze(bounds, thresholds)
    breakdowns = []
    for writer, judge in [(None, model) for model in judges] + [
        (model, None) for model in allocation["writers"]
    ] + [(writer, judge) for writer in allocation["writers"] for judge in judges]:
        subset = preference_families(writer, judge)
        values = [
            preference_by_key[(case["case_id"], rater)]
            for case in cases if writer is None or case["writer"] == writer
            for rater in ([judge] if judge else judges)
        ]
        breakdowns.append({
            "writer": writer, "judge": judge, "mean_bounds": _mean_bounds(subset),
            "per_judgment_counts": _counts(values), "inferential_claim": False,
        })
    agreement, exact, reversals, ties_differ, complete = {}, 0, 0, 0, 0
    for case in cases:
        first, second = [preference_by_key[(case["case_id"], judge)] for judge in judges]
        if first is None or second is None:
            agreement[case["case_id"]] = None
        else:
            complete += 1
            exact += first == second
            reversals += {first, second} == {Fraction(0), Fraction(1)}
            ties_differ += first != second and HALF in (first, second)
            agreement[case["case_id"]] = Fraction(int(first == second))
    agreement_bounds = [newsroom_stats.from_preferences(row["family_id"], [
        agreement[case] for case in row["case_ids"]
    ]) for row in families]
    def pointwise_summary(variant, writer=None, judge=None):
        raters = [judge] if judge else judges
        chosen_families = [row for row in families if writer is None or row["writer"] == writer]
        values = [
            pointwise_by_key[(case, variant, rater)]
            for family in chosen_families for case in family["case_ids"] for rater in raters
        ]
        salient, flags = [], []
        for family in chosen_families:
            rows = [pointwise_by_key[(case, variant, rater)] for case in family["case_ids"] for rater in raters]
            salient.append(newsroom_stats.from_preferences(family["family_id"], [
                None if value is None or value.level == "unassessable" else Fraction(int(value.level == "salient"))
                for value in rows
            ]))
            flags.append(newsroom_stats.from_preferences(family["family_id"], [
                None if value is None else Fraction(int(value.fidelity == "flag")) for value in rows
            ]))
        return {
            "planned_ratings": len(values), "missing_ratings": values.count(None),
            "assessable_style_ratings": sum(value is not None and value.level != "unassessable" for value in values),
            "level_counts": {level: sum(value is not None and value.level == level for value in values) for level in LEVELS},
            "fidelity_label_counts": {
                label: sum(value is not None and value.fidelity == label for value in values) for label in FIDELITY
            },
            "salient_rate_bounds": _mean_bounds(salient), "model_flag_rate_bounds": _mean_bounds(flags),
        }

    pointwise_results = {}
    for variant in VARIANTS:
        level_matrix, fidelity_matrix = Counter(), Counter()
        level_agreement, unassessable_pairs = {}, 0
        for case in cases:
            first, second = [pointwise_by_key[(case["case_id"], variant, judge)] for judge in judges]
            if first is None or second is None:
                level_agreement[case["case_id"]] = None
            else:
                level_matrix[(first.level, second.level)] += 1
                fidelity_matrix[(first.fidelity, second.fidelity)] += 1
                unassessable_pairs += "unassessable" in (first.level, second.level)
                level_agreement[case["case_id"]] = Fraction(int(first.level == second.level))
        pointwise_results[variant] = {
            **pointwise_summary(variant),
            "breakdowns": [{
                "writer": writer, "judge": judge, "inferential_claim": False,
                **pointwise_summary(variant, writer, judge),
            } for writer, judge in [(None, model) for model in judges] + [
                (model, None) for model in allocation["writers"]
            ] + [(writer, judge) for writer in allocation["writers"] for judge in judges]],
            "judge_agreement": {
                "judges_in_matrix_order": judges, "complete_cases": sum(level_matrix.values()),
                "cases_with_unassessable_rating": unassessable_pairs,
                "level_matrix": [[level_matrix[(first, second)] for second in LEVELS] for first in LEVELS],
                "level_matrix_labels": list(LEVELS),
                "fidelity_matrix": [[fidelity_matrix[(first, second)] for second in FIDELITY] for first in FIDELITY],
                "fidelity_matrix_labels": list(FIDELITY),
                "family_weighted_level_agreement_bounds": _mean_bounds([
                    newsroom_stats.from_preferences(row["family_id"], [
                        level_agreement[case] for case in row["case_ids"]
                    ]) for row in families
                ]),
            },
        }
    bare = pointwise_results["bare-task"]["salient_rate_bounds"]
    full = pointwise_results["full"]["salient_rate_bounds"]
    reduction_lower = Fraction(bare["lower_fraction"]) - Fraction(full["upper_fraction"])
    reduction_upper = Fraction(bare["upper_fraction"]) - Fraction(full["lower_fraction"])
    lengths = [{
        "case_id": case["case_id"], "family_id": case["family_id"], "writer": case["writer"],
        "words": {
            variant: None if (text := responses[case["writing_job_ids"][variant]]) is None else len(text.split())
            for variant in VARIANTS
        },
    } for case in cases]
    length_summary = {}
    for variant in VARIANTS:
        values = [row["words"][variant] for row in lengths if row["words"][variant] is not None]
        length_summary[variant] = {
            "planned": len(cases), "captured": len(values), "missing": len(cases) - len(values),
            "minimum": min(values) if values else None, "median": median(values) if values else None,
            "maximum": max(values) if values else None,
        }
    return {
        "schema_version": 1, "kind": "model-only-primary-newsroom-summary",
        "allocation_sha256": allocation["allocation_sha256"],
        "primary_preference": primary, "preference_mean_bounds": _mean_bounds(bounds),
        "family_preference_scores": [{
            "family_id": row.family_id, "lower_fraction": str(row.lower), "upper_fraction": str(row.upper),
            "grid_denominator": row.grid_denominator,
        } for row in bounds],
        "per_judgment_counts": _counts(list(preferences.values())), "preference_breakdowns": breakdowns,
        "judge_agreement": {
            "planned_cases": len(cases), "complete_cases": complete, "exact": exact,
            "direct_reversals": reversals, "tie_disagreements": ties_differ,
            "family_weighted_exact_agreement_bounds": _mean_bounds(agreement_bounds),
        },
        "pointwise": pointwise_results,
        "salient_reduction_bounds": {
            "lower": float(reduction_lower), "upper": float(reduction_upper),
            "lower_fraction": str(reduction_lower), "upper_fraction": str(reduction_upper),
            "direction": "bare-task minus full; positive means fewer salient model ratings for full",
            "inferential_claim": False,
        },
        "word_count_convention": "Whitespace-separated tokens in the entire unchanged response, including headlines and commentary.",
        "word_counts": lengths, "word_count_summary": length_summary,
        "human_reviews": 0, "human_editorial_superiority_established": False,
        "noticeable_slop_elimination_established": False,
        "limitations": [
            "Callers must authenticate captures, source bindings and strict parser results before supplying these values.",
            "Only the frozen, equally weighted family-preference contrast receives primary inference.",
            "Writer subsets are different assigned families; subgroup results are descriptive, not model rankings.",
            "Unassessable slop ratings retain [0,1] uncertainty for salient prevalence; they are not absence.",
            "Fidelity labels are model assertions. No_flag is not verified truth; flag counts are not confirmed errors.",
            "Missing-score bounds, category counts and length summaries are not confidence intervals or licensed AP audits.",
            "A preference signal, or zero observed salient ratings, cannot establish universal slop elimination or human quality.",
        ],
    }
