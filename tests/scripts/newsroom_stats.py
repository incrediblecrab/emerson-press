"""Mean-preserving, model-only inference for a prospectively frozen family bank."""

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from fractions import Fraction
import math
from secrets import randbelow

from tests.scripts.evaluate import require
from tests.scripts.simulate import ALPHA, positive_integer, sign_design, slug


HALF = Fraction(1, 2)
PREFERENCES = {Fraction(0), HALF, Fraction(1)}


@dataclass(frozen=True)
class FamilyBounds:
    family_id: str
    lower: Fraction
    upper: Fraction
    grid_denominator: int

    def __post_init__(self):
        slug(self.family_id, "family_id")
        require(isinstance(self.lower, Fraction) and isinstance(self.upper, Fraction),
                "family score bounds must be exact Fractions")
        require(0 <= self.lower <= self.upper <= 1, "family bounds must satisfy 0 <= lower <= upper <= 1")
        positive_integer(self.grid_denominator, "grid_denominator")
        require(all((value * self.grid_denominator).denominator == 1
                    for value in (self.lower, self.upper)),
                "family bounds do not lie on the predeclared score grid")


@dataclass(frozen=True)
class FamilyDraw:
    grid_denominator: int
    ticket: int

    def __post_init__(self):
        positive_integer(self.grid_denominator, "grid_denominator")
        require(type(self.ticket) is int and 0 <= self.ticket < self.grid_denominator,
                "auxiliary ticket is outside the predeclared score grid")


def from_preferences(family_id: str, preferences: Sequence[Fraction | None]) -> FamilyBounds:
    require(isinstance(preferences, Sequence) and not isinstance(preferences, (str, bytes))
            and bool(preferences), "expected a nonempty sequence of planned preferences")
    require(all(value is None or isinstance(value, Fraction) and value in PREFERENCES
                for value in preferences), "preferences must be exact 0, 1/2, 1 or missing")
    known = sum((value for value in preferences if value is not None), Fraction(0))
    missing = sum(value is None for value in preferences)
    count = len(preferences)
    return FamilyBounds(family_id, known / count, (known + missing) / count, 2 * count)


def draw_thresholds(grids: Mapping[str, int]) -> dict[str, FamilyDraw]:
    """Draw once after allocation is frozen; persist this table before outcomes."""
    require(isinstance(grids, Mapping) and bool(grids), "expected nonempty family score grids")
    for family_id, denominator in grids.items():
        slug(family_id, "family_id")
        positive_integer(denominator, "grid_denominator")
    return {family_id: FamilyDraw(grids[family_id], randbelow(grids[family_id]))
            for family_id in sorted(grids)}


def _binomial_distribution(n: int, p: float) -> list[float]:
    if p == 0:
        return [1.0] + [0.0] * n
    if p == 1:
        return [0.0] * n + [1.0]
    mode = min(n, int((n + 1) * p))
    mass = [0.0] * (n + 1)
    mass[mode] = 1.0
    for k in range(mode, 0, -1):
        mass[k - 1] = mass[k] * k / (n - k + 1) * (1 - p) / p
    for k in range(mode, n):
        mass[k + 1] = mass[k] * (n - k) / (k + 1) * p / (1 - p)
    total = math.fsum(mass)
    return [value / total for value in mass]


def _clopper_pearson(n: int, successes: int, tail: float = ALPHA) -> tuple[float, float]:
    lower, upper = 0.0, 1.0
    if successes:
        left, right = 0.0, 1.0
        for _ in range(64):
            middle = (left + right) / 2
            if math.fsum(_binomial_distribution(n, middle)[successes:]) < tail:
                left = middle
            else:
                right = middle
        lower = (left + right) / 2
    if successes < n:
        left, right = 0.0, 1.0
        for _ in range(64):
            middle = (left + right) / 2
            if math.fsum(_binomial_distribution(n, middle)[:successes + 1]) > tail:
                left = middle
            else:
                right = middle
        upper = (left + right) / 2
    return lower, upper


def mean_interval(n: int, successes: int) -> tuple[float, float]:
    positive_integer(n, "families")
    require(type(successes) is int and 0 <= successes <= n,
            "auxiliary successes must be an integer between zero and the family count")
    lower, upper = _clopper_pearson(n, successes)
    # Restrict inversion to the Hoeffding Poisson-binomial tail-comparison regions.
    return max(0.0, min(lower, (successes - 1) / n)), min(1.0, max(upper, (successes + 1) / n))


def power_plan(families: int) -> dict:
    n = positive_integer(families, "families")
    binary = sign_design(n)
    critical = binary["critical_wins"]
    null_comparison = critical - 1 >= Fraction(n, 2)
    alternative_comparison = critical <= Fraction(3 * n, 5)
    require(null_comparison, "binomial cutoff is outside the heterogeneous null comparison region")
    reduction_power = binary["power"] if alternative_comparison else 0.0
    raw_gate_failure = math.exp(-n / 50)
    joint_power = max(0.0, reduction_power - raw_gate_failure)
    return {
        "method": "randomized-heterogeneous-mean-with-raw-advantage",
        "families": n, "null_mean": 0.5, "planning_alternative_mean": 0.6,
        "alpha_one_sided": ALPHA,
        "critical_auxiliary_successes": critical if critical <= n else None,
        "alpha_upper_bound": binary["actual_alpha"],
        "iid_auxiliary_power_at_060": binary["power"],
        "heterogeneous_power_comparison_holds": alternative_comparison,
        "heterogeneous_auxiliary_power_lower_bound_at_060": reduction_power,
        "raw_mean_gate_failure_upper_bound_at_060": raw_gate_failure,
        "joint_power_lower_bound_at_060": joint_power,
        "conditional_target_power_met": joint_power >= 0.8,
        "unconditional_power_established": False,
        "assumptions": [
            "Independent [0,1] family scores with equally weighted average expectation 0.60.",
            "Independent, unbiased auxiliary randomization on each fixed score grid.",
            "Complete family scores; missingness and fidelity gates have no unconditional 80% guarantee.",
        ],
        "qualification": "Planning bound, not observed prose evidence or proof of corpus independence.",
    }


def analyze(bounds: Sequence[FamilyBounds], thresholds: Mapping[str, FamilyDraw]) -> dict:
    require(isinstance(bounds, Sequence) and bool(bounds)
            and all(isinstance(row, FamilyBounds) for row in bounds), "expected nonempty family bounds")
    identifiers = [row.family_id for row in bounds]
    require(len(identifiers) == len(set(identifiers)), "duplicate family scores")
    require(isinstance(thresholds, Mapping) and set(thresholds) == set(identifiers),
            "thresholds must cover exactly the predeclared family bank")
    auxiliary_lower, auxiliary_upper = 0, 0
    for row in bounds:
        draw = thresholds[row.family_id]
        require(isinstance(draw, FamilyDraw), f"{row.family_id}: expected a frozen family draw")
        require(draw.grid_denominator == row.grid_denominator,
                f"{row.family_id}: score grid differs from the frozen randomization")
        auxiliary_lower += draw.ticket < (row.lower * row.grid_denominator).numerator
        auxiliary_upper += draw.ticket < (row.upper * row.grid_denominator).numerator
    n = len(bounds)
    lower_mean = sum((row.lower for row in bounds), Fraction(0)) / n
    upper_mean = sum((row.upper for row in bounds), Fraction(0)) / n
    lower = mean_interval(n, auxiliary_lower)[0]
    upper = mean_interval(n, auxiliary_upper)[1]
    incomplete = [row.family_id for row in bounds if row.lower != row.upper]
    raw_advantage = lower_mean > HALF
    return {
        "method": "randomized-heterogeneous-mean-with-raw-advantage",
        "family_count": n,
        "complete_family_scores": n - len(incomplete),
        "incomplete_families": incomplete,
        "original_mean": float(lower_mean) if not incomplete else None,
        "original_mean_bounds": [float(lower_mean), float(upper_mean)],
        "auxiliary_success_bounds": [auxiliary_lower, auxiliary_upper],
        "randomized_mean_ci95": [lower, upper],
        "raw_mean_advantage_guaranteed": raw_advantage,
        "statistical_signal": lower > 0.5 and raw_advantage,
        "data_complete": not incomplete,
        "human_verified": False,
        "promotion_eligible": False,
        "plan": power_plan(n),
        "limitations": [
            "Auxiliary successes are randomization outcomes, not evaluator votes or fabricated ratings.",
            "The interval concerns expected model-rated family preference under the frozen allocation.",
            "Original ratings and fractional means remain unchanged; rerandomizing after outcomes is not allowed.",
            "Missing components retain fixed weights and [0,1] bounds, not imputed ties or observed losses.",
            "Independence, measurement validity and broader editorial generalization remain assumptions or separate work.",
        ],
    }
