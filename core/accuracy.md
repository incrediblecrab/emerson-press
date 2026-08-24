---
id: core.accuracy
layer: core
version: 1.2.0
status: draft
budget: 1026
tokens: 1026
evidence:
  - sources/ap-stylebook.md
  - sources/signs-of-ai-writing.md
  - sources/ai-slop-research.md
---

# Accuracy

Padded or imprecise language misinforms a reader even when no sentence in it is false. Accuracy is therefore a craft obligation in every genre, not a specialty of the regulated ones.

## Detect

### Claims without support

- A checkable claim with no source.
- Invented specifics: a name, date, figure, quote, or citation that reads plausible and was never checked.
- Unverified superlatives: `first`, `only`, `biggest`, `fastest-growing`.
- Attribution to an unnamed authority, or to a real named person who did not say it.
- A press release restated as reporting, with no independent confirmation.
- Undisclosed interest — funder, employer, or stake — behind a cited claim.

### Citations that cannot be checked

- A book cited with no page number. Unfalsifiable by construction.
- A page number that does not support the claim.
- Links dead on arrival, with nothing in an archive to suggest they lived.
- Identifiers that fail their own checksum, or that resolve to an unrelated paper. This last one is the dangerous variant, because the link works.
- Provenance parameters left in a URL: `utm_source=chatgpt.com`, `utm_source=openai`, `referrer=grok.com`.
- References listed but never cited in the text, or cited but never listed.

### Confidence outrunning evidence

- Causal verbs on correlational evidence: `causes`, `proves`, `drives`.
- A single study carrying a general claim.
- Statistical significance reported as real-world importance.
- Two positions given equal weight when the evidence behind them is not equal.
- Speculation following a disclaimer. Announcing that something is `not widely documented` and then guessing, hedged with `likely`. The claim that a thing is undocumented is itself unverified — usually it means the search failed.

### Numbers that mislead

- False precision beyond what the method supports, where every digit supplied implies every digit matters.
- A bare figure with nothing to compare it against.
- Raw counts comparing groups of different sizes, where a rate is needed.
- Percent change confused with percentage-point change.
- Percent change computed off a small base.
- `Average` reported where a median was calculated.
- Averages taken across averages.
- Margin of error omitted, or a lead claimed inside it.
- Relative risk quoted without the absolute numbers, so a rise from two cases per 100,000 to four is reported only as a doubling.
- Too many digits in one paragraph to hold.

### Handling of sources

- A quotation smoothed into clean grammar.
- An ellipsis that changes what a speaker meant.
- Material found online treated as verified because it looks plausible.
- A correction made silently, or worded to obscure what was wrong.

## Write

Attribute anything a reader could dispute, and name the source. If one person said it, write that one person said it.

Say what is unconfirmed rather than writing around it. When you did not find something, report where you looked and stop there. A failed search is a finding; a guess after a disclaimer is not.

Cite so a reader can check: page numbers for books, resolvable identifiers, a link that loads. A citation that cannot be verified is not a citation.

Own every claim regardless of what drafted it. A wrong date, a fabricated reference, a borrowed sentence — the name on the work answers for all of it, however the draft was produced, and the venues that have written this rule down allow no exception for tooling. Verification is part of authorship.

Keep confidence proportional to evidence. One study is provisional. Prefer `linked to` over `causes`, and say what would have to be true for the causal reading to hold.

Give numbers something to sit against — a prior year, another place, a benchmark measured the same way. Use rates to compare groups of different sizes. Name the measure you are reporting. Round to the precision the method earns, and state the uncertainty and sample size rather than presenting a figure as firmer than it is.

Quote exactly or paraphrase openly. If a quotation is too tangled to paraphrase faithfully, do not use it.

Treat anything found online at the same evidentiary bar as anything else. Trace it to its origin, confirm it against an independent source, and check that the detail matches the claimed time and place. Plausibility is not verification.

Correct in plain sight. Say what was wrong, not that something has been updated.

A reading level sets register, not truth. Simplifying for a reader never licenses a smaller fact. Simplify by spending words — a concrete instance, a slower build — not by cutting the mechanism or trading a precise term for a wrong one. Name the real term and gloss it rather than routing around it. Where you have flattened something, say so in a clause. If the content cannot be stated truly at the target level, the level is wrong, not the fact.

## Examples

**Invented citation**

> A 2019 Stanford study found remote workers were 13% more productive.

If you cannot name the authors, the journal, and how you verified it, the study does not exist for your purposes.

> Nicholas Bloom and three co-authors ran a randomized trial at the travel agency Ctrip and reported a 13% productivity gain (*Quarterly Journal of Economics*, 2015). I have not checked whether later work replicated it.

**Unverifiable citation**

> Traditionalists appeal to prudence and stability, while reactionaries invoke moral urgency.[^1]
>
> [^1]: Goldwater, Barry. *The Conscience of a Conservative*. 1960, p. 12.

> I could not find this argument in Goldwater. It comes from Corey Robin's *The Reactionary Mind* (2011), pp. 43-47, where it is his own framing.

**Confidence outrunning evidence**

> Intermittent fasting improves metabolic health.

> One trial of 116 people found no weight difference between fasting and normal eating. Larger trials are still running.

**Causation from correlation**

> Owning a library card causes higher lifetime earnings.

> Library-card holders earn more on average. The people who get cards also tend to have more schooling, which likely explains most of the gap.

**False precision and a lead inside the margin**

> Support for the measure stands at 51.7%, ahead of the 48.3% opposed.

> The poll put support at 52% and opposition at 48%, within its 3-point margin of error — too close to call a lead.

**Percentage points**

> The unemployment rate rose 0.2% last quarter.

> Unemployment rose from 4.1% to 4.3% — two-tenths of a percentage point, which is a 5% rise in the rate itself.

**Relative risk without absolute numbers**

> Daily consumption doubles the risk of the disease.

> Risk rises from about 2 cases per 100,000 people to about 4.

**Speculation after a disclaimer**

> While details of the company's early funding are not widely available, it likely relied on angel investment during this formative period.

> The company's filings before 2016 are not public, and neither founder would discuss funding.

**Smoothed quotation**

> "We were unprepared for the scale of the demand," she said.

> "We just — nobody thought it'd be that many people," she said.

**Buried correction**

> This article has been updated.

> An earlier version said the vote was unanimous. Two members abstained.
