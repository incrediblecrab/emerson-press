---
id: domain.education-level.graduate
layer: domain
sublayer: education-level
kind: ladder
version: 1.3.0
status: active
budget: 1057
tokens: 1057
stage: masters
evidence_rung: 5
evidence:
  - sources/ap-stylebook.md
---

# Education: Graduate

An optional preset for an explicitly requested master's thesis, research report or related scholarly task. A master's student or graduate reader is not necessarily expert in this subject. For ordinary help or an introductory explanation, follow the actual task and reader needs without imposing a thesis structure.

For a research introduction, one useful house outline establishes the topic, identifies the question or gap and explains the work's response. This is not a universal sequence or a requirement that every assignment discover something new. The AP evidence link supports mechanics, not a claim that this research-writing outline is a publisher requirement.

## Detect

### Under-reach

- Introduction reports what is known but never says what is missing, contested, or unresolved. The niche move is simply absent.
- No sentence states the paper's contribution relative to the literature it cites.
- Method or evidence-handling glossed, so a reader cannot reconstruct how a claim was produced.
- Literature cited as an undifferentiated list rather than grouped by position, method, or period.
- No engagement with counterevidence or a competing explanation of the same data.
- Hedges stacked, redundant, or attached to uncontested background facts, obscuring which claims are actually uncertain.

### Over-reach

- A field-wide debate resolved on the strength of one study, one dataset, one case.
- Boosters attached to claims the stated method cannot carry: `proves`, `undeniably`, `the definitive account`.
- Limitations thin, missing, or perfunctory relative to the scope of the claims — only the harmless limitations listed.
- Certainty running throughout with no hedges on inferential claims, even where the sample or the consensus is narrow.
- Theory imported wholesale without saying what it does for this argument.
- Prose density used as a proxy for rigor: nominalization chains, agentless passives, abstraction where a concrete noun exists.

### Either way

- A gap asserted beyond the scope of the literature actually reviewed.
- Hedging uniform rather than calibrated, so a reader cannot tell which claims the writer would defend.
- False balance: an unsupported claim given equal footing with a well-evidenced one in the name of fairness.

## Write

- For research writing, locate the question and the work's response in the literature actually reviewed. A synthesis, replication or null result can be a contribution; do not invent novelty.
- Support a claimed gap with the supplied review. A limited reading list does not establish that nobody has studied a topic.
- State the contribution or research question clearly enough for the intended audience to check.
- Make evidence-handling visible enough that a reader can evaluate the claim rather than trust it.
- Group sources by position or method, not by publication order. Show where they agree and where they split.
- Calibrate hedges to what the design actually supports. Reserve boosters for claims your evidence carries directly; hedge inference that goes past it.
- Name the limitation that would most worry a critical reviewer, and address it before being asked.
- Scope claims to the population, sample, or case actually studied, and say what would have to be true to generalize further.
- Use theory as an instrument. Name the work it performs here.
- Report a newsworthy false claim as false rather than as one side of a legitimate debate.
- Keep a hard term, a long sentence, or a dense noun group where it does work no plainer form can do. The test is whether you could defend the choice, not whether the prose is hard.
- Make the boldest claim your evidence will carry, and no bolder.

## Mechanics

Do not infer fluency from credentials. Follow the selected genre/manual and apply these checks when the material calls for them:

- Supplied margins of error, confidence intervals and p-values stated and interpreted appropriately, not added to qualitative work as decoration.
- Relative risk distinguished from absolute risk.
- Percentage change distinguished from percentage-point change.
- Study design named and weighted: experimental, observational, modeled, single study, meta-analysis.
- Causal language matched to what the design supports.
- A denominator or comparator supplied when needed to interpret the figure; unknown values remain unknown.
- Citation apparatus consistent with one style family throughout, per the `citation/` module in force.

## Evidence

The legacy `evidence_rung: 5` marks attention to how a research claim was produced and what it supports. Report numerical uncertainty when the underlying work supplies it and it is relevant. Qualitative work can explain evidence and limitations in words without apologizing for lacking an interval. Never invent a power calculation, uncertainty estimate, replication or design detail to satisfy this preset.

The task and domain set the applicable safeguards. A reader preset changes support and presentation, never the truth standard or the work that actually took place.

## Boundaries

Research-writing requirements follow the assignment, not the author's degree. Do not require a literature gap, original study or quantitative estimate for a coursework summary, patient explanation or ordinary instruction.

The doctoral preset adds checks for substantial scholarly submissions when appropriate. Traceability, critical review and honest limitations also matter in earlier work. Reporting must respect ethical, privacy and access limits rather than promise reproduction from prose alone.

## Examples

These independent synthetic study and literature records supply the facts. They are not claims about the state of an actual field.

**A local literature gap rather than a universal claim**

**Supplied facts:** The three fictional corpus studies reviewed for this paper use English data and report a relation between input frequency and vocabulary growth. The proposed paper examines Finnish. No exhaustive review of language-acquisition research is available.

Before: There has been a lot of research on how children acquire language. This paper looks at how children learn language and what factors are involved.

After: The three corpus studies reviewed here use English data. This paper examines whether their reported relation between input frequency and vocabulary growth also appears in Finnish.

**A contribution without erasing an existing role**

**Supplied facts:** Two fictional papers reviewed here analyze remittances as household income. The new case records also show expected remittances being used as collateral. The task is to describe that additional credit role, not claim that income and collateral are mutually exclusive.

Before: Many scholars have written about migration. Smith discusses labor flows. Chen examines policy. This study looks at migration too.

After: The two papers reviewed here analyze remittances as household income. In these case records, expected remittances also serve as collateral. This paper examines that credit role alongside their contribution to income.

**A finding scoped to its study**

**Supplied facts:** A fictional randomized study includes 212 students at four schools, all with existing advising infrastructure. Persistence is six percentage points higher in the intervention group. The observed difference is larger for first-generation students, but the subgroup estimates are imprecise. Other districts were not studied.

Before: This groundbreaking study definitively proves that the intervention works and should be adopted widely.

After: In this randomized study of 212 students at four schools, persistence was six percentage points higher in the intervention group. The observed difference was larger for first-generation students, but the subgroup estimates were imprecise. The study does not establish whether the result holds in districts without existing advising infrastructure.

**Uncertainty without an invented replication**

**Supplied facts:** The reported difference is 0.08 standard deviations, with a 95% confidence interval from -0.04 to 0.20. No replication or Section 6 result has been supplied.

Before: It is possible that there may be some potential indication that the results could perhaps suggest an effect.

After: The estimated difference is 0.08 standard deviations (95% confidence interval, -0.04 to 0.20). The interval is compatible with a small negative difference, no difference or a positive difference; the estimate is not precise enough to distinguish them.

**An observed difference without causal promotion**

**Supplied facts:** Outcomes in the program group are 0.3 standard deviations higher than in the comparison group. Schools opted in; assignment was not random, and the analysis does not isolate a program effect from selection.

Before: The treatment group showed improved outcomes, demonstrating that the program causes better performance.

After: The program group outperformed the comparison group by 0.3 standard deviations. Schools opted in, so the difference could reflect selection as well as a program effect. This design does not separate them.
