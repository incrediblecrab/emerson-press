"""Synthetic mathematical fixtures only; no model calls or editorial outcomes."""

from fractions import Fraction
import itertools
import math
import unittest
from unittest.mock import patch

from scripts import newsroom_stats as stats
from scripts.modules import DocumentError


class NewsroomStatisticsTests(unittest.TestCase):
    def test_exact_grid_randomization_preserves_each_fractional_mean(self):
        for denominator in (2, 4, 8, 12):
            for numerator in range(denominator + 1):
                score = Fraction(numerator, denominator)
                row = stats.FamilyBounds("synthetic-family", score, score, denominator)
                outcomes = [
                    stats.analyze([row], {
                        "synthetic-family": stats.FamilyDraw(denominator, threshold),
                    })["auxiliary_success_bounds"][0]
                    for threshold in range(denominator)
                ]
                self.assertEqual(Fraction(sum(outcomes), denominator), score)

    def test_missing_preferences_keep_the_fixed_denominator(self):
        row = stats.from_preferences("synthetic-family", [Fraction(1), None, Fraction(1, 2), None])
        self.assertEqual(row.lower, Fraction(3, 8))
        self.assertEqual(row.upper, Fraction(7, 8))
        self.assertEqual(row.grid_denominator, 8)
        missing = stats.from_preferences("synthetic-missing", [None, None])
        report = stats.analyze([missing], {"synthetic-missing": stats.FamilyDraw(4, 1)})
        self.assertEqual(report["original_mean_bounds"], [0, 1])
        self.assertEqual(report["randomized_mean_ci95"], [0, 1])
        self.assertIsNone(report["original_mean"])
        self.assertFalse(report["data_complete"])
        self.assertFalse(report["statistical_signal"])

    def test_all_ties_cannot_gain_a_signal_from_lucky_auxiliary_bits(self):
        rows = [
            stats.from_preferences(f"synthetic-family-{i}", [Fraction(1, 2)] * 2)
            for i in range(214)
        ]
        report = stats.analyze(rows, {row.family_id: stats.FamilyDraw(4, 0) for row in rows})
        self.assertGreater(report["randomized_mean_ci95"][0], 0.5)
        self.assertEqual(report["original_mean"], 0.5)
        self.assertFalse(report["raw_mean_advantage_guaranteed"])
        self.assertFalse(report["statistical_signal"])
        self.assertFalse(report["promotion_eligible"])
        self.assertFalse(report["human_verified"])

    def test_fractional_means_are_not_substituted_for_auxiliary_counts(self):
        rows = [
            stats.from_preferences(f"synthetic-family-{i}", [Fraction(1), Fraction(1, 2)])
            for i in range(20)
        ]
        draws = {
            row.family_id: stats.FamilyDraw(4, 0 if i < 10 else 3)
            for i, row in enumerate(rows)
        }
        report = stats.analyze(rows, draws)
        self.assertEqual(report["original_mean"], 0.75)
        self.assertEqual(report["auxiliary_success_bounds"], [10, 10])
        self.assertTrue(report["raw_mean_advantage_guaranteed"])
        self.assertFalse(report["statistical_signal"])

    def test_planning_accounts_for_the_additional_raw_mean_gate(self):
        plan = stats.power_plan(214)
        self.assertEqual(plan["critical_auxiliary_successes"], 122)
        self.assertAlmostEqual(plan["alpha_upper_bound"], 0.023590457587993774)
        self.assertAlmostEqual(plan["iid_auxiliary_power_at_060"], 0.8322622872236244)
        self.assertAlmostEqual(plan["joint_power_lower_bound_at_060"], 0.8184196251371448)
        self.assertLess(plan["joint_power_lower_bound_at_060"], plan["iid_auxiliary_power_at_060"])
        self.assertTrue(plan["conditional_target_power_met"])
        self.assertFalse(plan["unconditional_power_established"])
        self.assertFalse(stats.power_plan(199)["conditional_target_power_met"])
        self.assertIsNone(stats.power_plan(2)["critical_auxiliary_successes"])
        self.assertEqual(stats.power_plan(2)["joint_power_lower_bound_at_060"], 0)

    def test_binomial_recurrence_matches_direct_probabilities(self):
        for n, probability in itertools.product((1, 12, 214), (0, 0.01, 0.5, 0.6, 0.99, 1)):
            observed = stats._binomial_distribution(n, probability)
            expected = [
                math.comb(n, k) * probability ** k * (1 - probability) ** (n - k)
                for k in range(n + 1)
            ]
            self.assertAlmostEqual(math.fsum(observed), 1)
            self.assertLess(max(abs(a - b) for a, b in zip(observed, expected)), 1e-12)

    def test_exact_interval_matches_nist_and_heterogeneous_boundary_guard(self):
        lower, upper = stats._clopper_pearson(20, 4, tail=0.05)
        # NIST's displayed endpoints are approximate; verify the tail equations too.
        self.assertAlmostEqual(lower, 0.071354, delta=1e-6)
        self.assertAlmostEqual(upper, 0.401029, delta=1e-6)
        self.assertAlmostEqual(math.fsum(
            math.comb(20, k) * lower ** k * (1 - lower) ** (20 - k)
            for k in range(4, 21)
        ), 0.05, places=12)
        self.assertAlmostEqual(math.fsum(
            math.comb(20, k) * upper ** k * (1 - upper) ** (20 - k)
            for k in range(5)
        ), 0.05, places=12)
        self.assertEqual(stats.mean_interval(214, 1)[0], 0)
        self.assertEqual(stats.mean_interval(214, 213)[1], 1)
        self.assertLessEqual(stats.mean_interval(214, 121)[0], 0.5)
        self.assertGreater(stats.mean_interval(214, 122)[0], 0.5)
        for successes in range(13):
            lower, upper = stats.mean_interval(12, successes)
            self.assertLessEqual(lower, upper)
            if successes:
                previous = stats.mean_interval(12, successes - 1)
                self.assertGreaterEqual(lower, previous[0])
                self.assertGreaterEqual(upper, previous[1])

    def test_safe_intervals_cover_enumerated_heterogeneous_examples(self):
        examples = (
            [0.5] * 12,
            [0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.98],
            [0.001] * 11 + [0.03],
        )
        for probabilities in examples:
            distribution = [1.0]
            for probability in probabilities:
                updated = [0.0] * (len(distribution) + 1)
                for k, mass in enumerate(distribution):
                    updated[k] += mass * (1 - probability)
                    updated[k + 1] += mass * probability
                distribution = updated
            mean = sum(probabilities) / len(probabilities)
            coverage = math.fsum(
                probability for k, probability in enumerate(distribution)
                if stats.mean_interval(len(probabilities), k)[0] <= mean
                <= stats.mean_interval(len(probabilities), k)[1]
            )
            self.assertGreaterEqual(coverage, 0.95 - 1e-12)

    def test_sparse_null_counterexample_exceeds_nominal_conventional_error(self):
        n, df = 214, 213
        self.assertEqual(Fraction(97, 100) * Fraction(1, 2) + Fraction(2, 100) * Fraction(3, 4),
                         Fraction(1, 2))
        false_positive_subset = Fraction(sum(
            math.comb(n, k) * 2 ** k * 97 ** (n - k) for k in range(4, n)
        ), 100 ** n)
        self.assertGreater(false_positive_subset, Fraction(7, 100))
        self.assertGreater(math.sqrt(4 * (n - 1) / (n - 4)), 2)
        coefficient = math.exp(math.lgamma((df + 1) / 2) - math.lgamma(df / 2)) / math.sqrt(df * math.pi)
        step = 2 / 2048
        density = [
            coefficient * (1 + (i * step) ** 2 / df) ** (-(df + 1) / 2)
            for i in range(2049)
        ]
        cdf_at_two = 0.5 + step / 3 * (
            density[0] + density[-1] + 4 * math.fsum(density[1:-1:2])
            + 2 * math.fsum(density[2:-1:2])
        )
        self.assertGreater(cdf_at_two, 0.975)
        self.assertLess(Fraction(n - 4, n) ** n, Fraction(1, 40))

    def test_missing_component_interval_contains_every_tested_completion(self):
        observed = [Fraction(1), None, None, Fraction(1, 2)]
        bounded = stats.from_preferences("synthetic-family", observed)
        for fixed_successes in (6, 11):
            fixed = [
                stats.from_preferences(f"synthetic-fixed-{i}", [Fraction(int(i < fixed_successes))])
                for i in range(11)
            ]
            for threshold in range(bounded.grid_denominator):
                draws = {row.family_id: stats.FamilyDraw(2, 0) for row in fixed}
                draws[bounded.family_id] = stats.FamilyDraw(bounded.grid_denominator, threshold)
                outer = stats.analyze([*fixed, bounded], draws)
                for first, second in itertools.product(stats.PREFERENCES, repeat=2):
                    complete = stats.from_preferences(
                        "synthetic-family", [Fraction(1), first, second, Fraction(1, 2)],
                    )
                    inner = stats.analyze([*fixed, complete], draws)
                    self.assertLessEqual(outer["randomized_mean_ci95"][0], inner["randomized_mean_ci95"][0])
                    self.assertGreaterEqual(outer["randomized_mean_ci95"][1], inner["randomized_mean_ci95"][1])
                    self.assertLessEqual(outer["auxiliary_success_bounds"][0], inner["auxiliary_success_bounds"][0])
                    self.assertGreaterEqual(outer["auxiliary_success_bounds"][1], inner["auxiliary_success_bounds"][1])
                    if outer["statistical_signal"]:
                        self.assertTrue(inner["statistical_signal"])

    def test_drawing_is_separate_from_reproducible_analysis(self):
        with patch.object(stats, "randbelow", side_effect=[1, 3]) as draw:
            thresholds = stats.draw_thresholds({"synthetic-b": 8, "synthetic-a": 4})
        self.assertEqual(thresholds, {
            "synthetic-a": stats.FamilyDraw(4, 1),
            "synthetic-b": stats.FamilyDraw(8, 3),
        })
        self.assertEqual([call.args for call in draw.call_args_list], [(4,), (8,)])
        rows = [
            stats.from_preferences("synthetic-a", [Fraction(1), Fraction(1, 2)]),
            stats.from_preferences("synthetic-b", [Fraction(1)] * 4),
        ]
        with patch.object(stats, "randbelow", side_effect=AssertionError("analysis must not redraw")):
            self.assertEqual(stats.analyze(rows, thresholds), stats.analyze(rows, thresholds))

    def test_invalid_bounds_grids_and_bank_changes_are_rejected(self):
        for lower, upper, grid in (
            (0.0, Fraction(1), 4),
            (Fraction(1), Fraction(0), 4),
            (Fraction(-1), Fraction(0), 4),
            (Fraction(0), Fraction(2), 4),
            (Fraction(1, 3), Fraction(1), 4),
            (Fraction(0), Fraction(1), True),
        ):
            with self.subTest(lower=lower, upper=upper, grid=grid), self.assertRaises(DocumentError):
                stats.FamilyBounds("synthetic-family", lower, upper, grid)
        row = stats.from_preferences("synthetic-family", [Fraction(1)])
        for thresholds in (
            {}, {"other-family": stats.FamilyDraw(2, 0)}, {"synthetic-family": True},
            {"synthetic-family": stats.FamilyDraw(4, 0)},
        ):
            with self.subTest(thresholds=thresholds), self.assertRaises(DocumentError):
                stats.analyze([row], thresholds)
        with self.assertRaises(DocumentError):
            stats.analyze([row, row], {"synthetic-family": stats.FamilyDraw(2, 0)})
        for grid, ticket in ((0, 0), (True, 0), (4, True), (4, -1), (4, 4)):
            with self.subTest(grid=grid, ticket=ticket), self.assertRaises(DocumentError):
                stats.FamilyDraw(grid, ticket)
        for preferences in ([], [1.0], [True], [Fraction(1, 3)]):
            with self.subTest(preferences=preferences), self.assertRaises(DocumentError):
                stats.from_preferences("synthetic-family", preferences)
        for n, successes in ((0, 0), (True, 1), (10, True), (10, 11)):
            with self.subTest(n=n, successes=successes), self.assertRaises(DocumentError):
                stats.mean_interval(n, successes)


if __name__ == "__main__":
    unittest.main()
