# Mean-preference inference

`scripts.newsroom_stats` supplies a candidate inferential component, not a frozen
primary protocol or an experimental result. The family bank, writer allocation,
judge weights, score grids, randomization table and full acquisition plan must be
registered before primary outcomes. The original source-aware judgments remain
separate from the older `scripts.simulate` acquisition schema.

## Target and randomization

The target is the equally weighted expected family preference under the frozen
allocation. Raw judgments score win = 1, tie = 0.5 and loss = 0. Predeclared
contributions are averaged within a reporting family; repeated cases, writers
and judges do not add independent families.

For a family score `X = a / D`, draw an independent uniform integer `K` from
`0, ..., D-1` and define an **auxiliary** outcome `Y = 1` when `K < a`, otherwise
zero. Then `E[Y | X] = X`. This preserves the mean estimand, unlike discarding
tied family directions for a sign test. The auxiliary outcomes are not evaluator
votes and must never replace the recorded judgments or their fractional means.

Freeze the grids and allocation first. Draw and persist one table with
`draw_thresholds`, before inspecting primary outcomes, and bind it into the
registration. `analyze` requires that exact table and never redraws. The
implementation uses the operating system's cryptographic random source; the
mathematics assumes independent, unbiased draws. No seed or table searching is
allowed.
Each `FamilyDraw` binds both its grid denominator and its integer ticket;
analysis rejects a changed grid even if the old ticket would still fit.

This deliberately adds noise. The decision can depend on the auxiliary draw even
when the raw ratings do not change. It is chosen for finite-sample calibration of
the mean, not as a disguised deterministic fractional-binomial test.

## Interval and a raw-score safeguard

Independent families may have different expected scores. Their auxiliary sum is
Poisson-binomial, not necessarily identically distributed binomial. Ordinary
Clopper-Pearson intervals alone are not uniformly valid for the average of
arbitrary heterogeneous Bernoulli probabilities.

Let `s` be auxiliary successes among `n` families. Compute ordinary equal-tailed
95% Clopper-Pearson bounds, then widen them to:

```text
L = max(0, min(L_CP, (s - 1) / n))
U = min(1, max(U_CP, (s + 1) / n))
```

These limits restrict binomial-tail inversion to the separation regions in
[Hoeffding's Poisson-binomial comparison, reproduced in Theorem 2.1 of Tang and Tang](https://ar5iv.labs.arxiv.org/html/1908.10024#S2.Thmtheorem1).
The theorem bounds each inverted tail by 0.025; the union bound gives at least
95% coverage for the equally weighted mean under independent family outcomes.
[NIST describes the underlying binomial tail inversion](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm).
Numerical endpoints use checked floating-point calculations.

A preference signal requires **both** `L > 0.5` and the original fractional mean
above 0.5. An all-tie result therefore cannot acquire a positive conclusion from
lucky auxiliary bits. The interval is explicitly randomized; it is not the
ordinary family-bootstrap interval used in earlier descriptive reports.

## Planning and missingness

At 214 independent families, the auxiliary cutoff is 122. Its type-I error is at
most 0.02359046, and its power is at least 0.83226229 at mean preference 0.60,
under the stated comparison conditions. The extra raw-mean safeguard has its own
cost: Hoeffding's bounded-sum inequality bounds failure of that safeguard by
`exp(-2 * n * 0.1^2)`. Subtracting that bound gives **at least 0.81841963 joint
power**, not 0.83226229. This is a planning statement conditional on independent,
complete family scores and the specified mean effect, not observed repository
effectiveness. Recalculate at the final fixed family count; discrete critical
counts mean power does not rise monotonically at every additional family.

For missing components, keep their intended weights and retain `[0,1]` bounds.
Use the same `K` for each family's lower and upper possible score. Monotonicity
then gives a conservative interval containing the complete-data interval for
every possible completion. The raw-mean safeguard uses the lower possible mean.
Missing values are not observed losses or ties, and surviving judges do not gain
extra weight. No unconditional 80% claim follows for missingness, transport
completion or the separate fidelity gate.

Conventional t and percentile-bootstrap methods are not uniformly calibrated by
boundedness and a sample near 214 alone. For example, a hypothetical family law
on `[0, 0.5, 0.75]` with probabilities `[0.01, 0.97, 0.02]` has mean 0.5.
The event with no zeros, at least four 0.75 scores and at least one 0.5 score
alone causes more than 7% upper-tail rejection for t and the infinite-resample
percentile limit at a nominal 2.5% threshold. Its probability and both rejection
conditions are reproduced in `tests/test_newsroom_stats.py`. This is a
mathematical counterexample, not a distribution estimated from the writing trials.

Independence remains an audited assumption, not a consequence of file count or
fresh SDK sessions. With one writer assigned to each fixed family, the conditional
target is that realized allocation's expected mean, not the unobserved average
of both writers on every family. Broader population and human-editorial claims
need additional evidence. Neither statistical significance nor source fidelity
establishes elimination of noticeable slop; pointwise slop, fidelity, output
compliance and human review remain distinct.
