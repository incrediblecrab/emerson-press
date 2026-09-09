from copy import deepcopy
from fractions import Fraction
import unittest

from tests.scripts import evaluate, newsroom_results as results, newsroom_stats
from tests.scripts.modules import digest


def fixture():
    models = ["model-a", "model-b"]
    families = [{
        "family_id": "family-a", "case_ids": ["case-a1", "case-a2"],
        "writer": models[0], "preference_components": 4, "score_grid_denominator": 8,
    }, {
        "family_id": "family-b", "case_ids": ["case-b1"],
        "writer": models[1], "preference_components": 2, "score_grid_denominator": 4,
    }]
    cases, slots = [], []
    for family in families:
        for identifier in family["case_ids"]:
            case = {
                "case_id": identifier, "family_id": family["family_id"], "writer": family["writer"],
                "full_is_a": identifier != "case-b1",
                "writing_job_ids": {variant: f"write-{identifier}-{variant}" for variant in results.VARIANTS},
                "request_sha256": {variant: digest(f"synthetic-{identifier}-{variant}") for variant in results.VARIANTS},
            }
            cases.append(case)
            for judge in models:
                for kind, variant in (("preference", None), ("pointwise", "full"), ("pointwise", "bare-task")):
                    slots.append({
                        "id": f"{kind}-{identifier}-{variant}-{judge}", "kind": kind,
                        "case_id": identifier, "family_id": family["family_id"],
                        "writer": family["writer"], "judge": judge, "variant": variant,
                    })
    allocation = evaluate.seal({
        "schema_version": 1, "kind": "newsroom-primary-allocation",
        "fixture_notice": "Synthetic unit fixture; not a registered experiment or captured model output.",
        "writers": models, "judges": models, "variants": list(results.VARIANTS),
        "case_count": 3, "family_count": 2, "writing_calls_planned": 6,
        "preference_calls_planned": 6, "pointwise_calls_planned": 12,
        "cases": cases, "families": families, "judgment_slots": slots,
    }, "allocation_sha256")
    draws = {row["family_id"]: newsroom_stats.FamilyDraw(row["score_grid_denominator"], 0) for row in families}
    preferences = {row["id"]: Fraction(1) for row in slots if row["kind"] == "preference"}
    pointwise = {
        row["id"]: results.Pointwise("absent", "no_flag") for row in slots if row["kind"] == "pointwise"
    }
    responses = {
        job: "# Synthetic headline\n\nFactual fixture.\n\nNote: fixture."
        for case in cases for job in case["writing_job_ids"].values()
    }
    return allocation, draws, preferences, pointwise, responses


def reseal(value):
    value.pop("allocation_sha256", None)
    return evaluate.seal(value, "allocation_sha256")


class NewsroomResultsTests(unittest.TestCase):
    def test_both_blinded_orientations_and_ties(self):
        for full_is_a in (True, False):
            self.assertEqual(results.score_preference("tie", full_is_a), Fraction(1, 2))
            self.assertEqual(results.score_preference("a", full_is_a), Fraction(int(full_is_a)))
            self.assertEqual(results.score_preference("b", full_is_a), Fraction(int(not full_is_a)))
        for winner, orientation in [("full", True), (True, True), ("a", 1), ("a", "true")]:
            with self.subTest(winner=winner, orientation=orientation), self.assertRaises(evaluate.DocumentError):
                results.score_preference(winner, orientation)

    def test_families_not_files_or_judgments_determine_mean(self):
        allocation, draws, preferences, pointwise, responses = fixture()
        for slot in allocation["judgment_slots"]:
            if slot["kind"] == "preference" and slot["family_id"] == "family-b":
                preferences[slot["id"]] = Fraction(0)
        report = results.summarize(allocation, draws, preferences, pointwise, responses)
        self.assertEqual(report["per_judgment_counts"], {
            "planned": 6, "full_wins": 4, "ties": 0, "bare_wins": 2, "missing": 0,
        })
        self.assertEqual(report["preference_mean_bounds"]["lower_fraction"], "1/2")
        self.assertEqual(report["primary_preference"]["original_mean"], 0.5)
        self.assertEqual(report["primary_preference"]["family_count"], 2)
        self.assertFalse(report["primary_preference"]["statistical_signal"])

    def test_missing_judge_keeps_its_planned_weight(self):
        allocation, draws, preferences, pointwise, responses = fixture()
        for slot in allocation["judgment_slots"]:
            if slot["kind"] != "preference":
                continue
            if slot["family_id"] == "family-b":
                preferences[slot["id"]] = Fraction(0)
            elif slot["case_id"] == "case-a1" and slot["judge"] == "model-b":
                preferences[slot["id"]] = None
        report = results.summarize(allocation, draws, preferences, pointwise, responses)
        self.assertEqual(report["preference_mean_bounds"]["lower_fraction"], "3/8")
        self.assertEqual(report["preference_mean_bounds"]["upper_fraction"], "1/2")
        self.assertEqual(report["per_judgment_counts"]["missing"], 1)
        self.assertEqual(report["primary_preference"]["incomplete_families"], ["family-a"])

    def test_all_missing_has_no_favorable_fallback(self):
        allocation, draws, preferences, pointwise, responses = fixture()
        report = results.summarize(
            allocation, draws, dict.fromkeys(preferences), dict.fromkeys(pointwise), dict.fromkeys(responses)
        )
        self.assertEqual(report["primary_preference"]["original_mean_bounds"], [0.0, 1.0])
        self.assertEqual(report["primary_preference"]["randomized_mean_ci95"], [0.0, 1.0])
        self.assertFalse(report["primary_preference"]["statistical_signal"])
        self.assertEqual(report["judge_agreement"]["complete_cases"], 0)
        for variant in results.VARIANTS:
            self.assertEqual(report["word_count_summary"][variant]["captured"], 0)
            self.assertIsNone(report["word_count_summary"][variant]["median"])
            self.assertEqual(report["pointwise"][variant]["missing_ratings"], 6)

    def test_unassessable_is_not_absent_and_zero_flags_is_not_truth(self):
        allocation, draws, preferences, pointwise, responses = fixture()
        for slot in allocation["judgment_slots"]:
            if slot["kind"] != "pointwise":
                continue
            if slot["variant"] == "bare-task":
                pointwise[slot["id"]] = results.Pointwise("salient", "no_flag")
            elif slot["case_id"] == "case-a2":
                pointwise[slot["id"]] = results.Pointwise("unassessable", "uncertain")
        report = results.summarize(allocation, draws, preferences, pointwise, responses)
        candidate = report["pointwise"]["full"]
        self.assertEqual(candidate["level_counts"]["unassessable"], 2)
        self.assertEqual(candidate["missing_ratings"], 0)
        self.assertEqual(candidate["assessable_style_ratings"], 4)
        self.assertEqual(candidate["salient_rate_bounds"]["lower"], 0)
        self.assertEqual(candidate["salient_rate_bounds"]["upper"], 0.25)
        self.assertEqual(candidate["fidelity_label_counts"]["uncertain"], 2)
        self.assertEqual(candidate["model_flag_rate_bounds"]["upper"], 0)
        self.assertEqual(report["salient_reduction_bounds"]["lower"], 0.75)
        self.assertEqual(report["salient_reduction_bounds"]["upper"], 1)
        self.assertFalse(report["noticeable_slop_elimination_established"])
        self.assertFalse(report["human_editorial_superiority_established"])
        self.assertEqual(report["human_reviews"], 0)

    def test_pointwise_matrices_and_subgroups_keep_disagreement_visible(self):
        allocation, draws, preferences, pointwise, responses = fixture()
        for slot in allocation["judgment_slots"]:
            if slot["kind"] == "pointwise" and slot["variant"] == "full":
                if slot["case_id"] == "case-a1":
                    level = "salient" if slot["judge"] == "model-a" else "minor"
                    pointwise[slot["id"]] = results.Pointwise(level, "no_flag")
                elif slot["case_id"] == "case-a2" and slot["judge"] == "model-a":
                    pointwise[slot["id"]] = results.Pointwise("unassessable", "uncertain")
        candidate = results.summarize(allocation, draws, preferences, pointwise, responses)["pointwise"]["full"]
        agreement = candidate["judge_agreement"]
        self.assertEqual(agreement["complete_cases"], 3)
        self.assertEqual(agreement["cases_with_unassessable_rating"], 1)
        self.assertEqual(agreement["level_matrix"], [
            [1, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [1, 0, 0, 0],
        ])
        self.assertEqual(agreement["family_weighted_level_agreement_bounds"]["lower_fraction"], "1/2")
        self.assertEqual(candidate["salient_rate_bounds"]["lower_fraction"], "1/8")
        self.assertEqual(candidate["salient_rate_bounds"]["upper_fraction"], "1/4")
        self.assertEqual(len(candidate["breakdowns"]), 8)
        for row in candidate["breakdowns"]:
            self.assertFalse(row["inferential_claim"])
            if row["writer"] is None and row["judge"] == "model-a":
                self.assertEqual(row["salient_rate_bounds"]["lower_fraction"], "1/4")
                self.assertEqual(row["salient_rate_bounds"]["upper_fraction"], "1/2")

    def test_agreement_counts_and_family_weighting(self):
        allocation, draws, preferences, pointwise, responses = fixture()
        for slot in allocation["judgment_slots"]:
            if slot["kind"] != "preference":
                continue
            if slot["case_id"] == "case-a2" and slot["judge"] == "model-b":
                preferences[slot["id"]] = Fraction(0)
            elif slot["case_id"] == "case-b1" and slot["judge"] == "model-a":
                preferences[slot["id"]] = Fraction(1, 2)
        agreement = results.summarize(allocation, draws, preferences, pointwise, responses)["judge_agreement"]
        self.assertEqual(agreement["complete_cases"], 3)
        self.assertEqual(agreement["exact"], 1)
        self.assertEqual(agreement["direct_reversals"], 1)
        self.assertEqual(agreement["tie_disagreements"], 1)
        self.assertEqual(agreement["family_weighted_exact_agreement_bounds"]["lower_fraction"], "1/4")

    def test_word_counts_include_all_material_and_unicode_whitespace(self):
        allocation, draws, preferences, pointwise, responses = fixture()
        responses[allocation["cases"][0]["writing_job_ids"]["full"]] = (
            "# Fixture\n\nOne\u0085two\u2028three\u2029four.\n\nNote: five."
        )
        report = results.summarize(allocation, draws, preferences, pointwise, responses)
        self.assertEqual(report["word_counts"][0]["words"], {"full": 8, "bare-task": 7})
        self.assertEqual(report["word_count_summary"]["full"]["maximum"], 8)

    def test_missing_or_extra_slots_are_errors_not_implicit_missingness(self):
        for which in ("preferences", "pointwise", "responses"):
            for mutation in ("omit", "add"):
                allocation, draws, preferences, pointwise, responses = fixture()
                target = {"preferences": preferences, "pointwise": pointwise, "responses": responses}[which]
                if mutation == "omit":
                    target.pop(next(iter(target)))
                else:
                    target["not-planned"] = None
                with self.subTest(which=which, mutation=mutation), self.assertRaises(evaluate.DocumentError):
                    results.summarize(allocation, draws, preferences, pointwise, responses)

    def test_invalid_score_types_and_orphaned_assessments_reject(self):
        for value in (True, 1, 0.5, "win", Fraction(1, 3)):
            allocation, draws, preferences, pointwise, responses = fixture()
            preferences[next(iter(preferences))] = value
            with self.subTest(value=value), self.assertRaises(evaluate.DocumentError):
                results.summarize(allocation, draws, preferences, pointwise, responses)
        allocation, draws, preferences, pointwise, responses = fixture()
        responses[allocation["cases"][0]["writing_job_ids"]["full"]] = None
        with self.assertRaisesRegex(evaluate.DocumentError, "without its writing input"):
            results.summarize(allocation, draws, preferences, pointwise, responses)
        for level, fidelity in [("clean", "no_flag"), ("absent", "correct"), (True, "flag")]:
            with self.subTest(level=level, fidelity=fidelity), self.assertRaises(evaluate.DocumentError):
                results.Pointwise(level, fidelity)

    def test_seals_grids_family_members_and_slot_coverage_are_checked(self):
        allocation, draws, preferences, pointwise, responses = fixture()
        changed = deepcopy(allocation)
        changed["case_count"] = 999
        with self.assertRaisesRegex(evaluate.DocumentError, "hash mismatch"):
            results.validate_allocation(changed)
        mutations = [
            lambda value: value["families"][0].update(score_grid_denominator=4),
            lambda value: value["families"][0].update(preference_components=True),
            lambda value: value["families"][1].update(case_ids=["case-a1"]),
            lambda value: value["cases"][0].update(full_is_a=1),
            lambda value: value["cases"][0].update(writer="not-a-writer"),
            lambda value: value.update(family_count=True),
            lambda value: value["judgment_slots"].pop(),
            lambda value: value["judgment_slots"].append(value["judgment_slots"][0]),
            lambda value: value["cases"][1].update(writing_job_ids=value["cases"][0]["writing_job_ids"]),
        ]
        for mutate in mutations:
            changed = deepcopy(allocation)
            mutate(changed)
            with self.subTest(mutation=mutate), self.assertRaises(evaluate.DocumentError):
                results.validate_allocation(reseal(changed))
        draws["family-a"] = newsroom_stats.FamilyDraw(4, 0)
        with self.assertRaisesRegex(evaluate.DocumentError, "grid"):
            results.summarize(allocation, draws, preferences, pointwise, responses)
        changed = deepcopy(allocation)
        changed["families"][1]["writer"] = "model-a"
        changed["cases"][2]["writer"] = "model-a"
        with self.assertRaisesRegex(evaluate.DocumentError, "each declared writer"):
            results.validate_allocation(reseal(changed))

    def test_breakdowns_do_not_promote_subgroups_to_primary_inference(self):
        allocation, draws, preferences, pointwise, responses = fixture()
        report = results.summarize(allocation, draws, preferences, pointwise, responses)
        self.assertEqual(len(report["preference_breakdowns"]), 8)
        for row in report["preference_breakdowns"]:
            self.assertFalse(row["inferential_claim"])
            self.assertEqual(row["mean_bounds"]["families"], 2 if row["writer"] is None else 1)


if __name__ == "__main__":
    unittest.main()
