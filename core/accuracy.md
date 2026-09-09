---
id: core.accuracy
layer: core
version: 1.3.1
status: draft
budget: 1216
tokens: 1216
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

- A passage-specific citation without a usable locator. Pages, sections or other stable locators may serve; a whole-work citation does not always need one.
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
- Unweighted averages of group averages when the group sizes differ.
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

Preserve the supplied record when editing. Do not add a cause, date, sample, quotation, bibliographic field, archive link or verification claim to make the text sound better supported. Correct errors against an identified source. If the record does not settle a question, flag it, omit the unsupported claim or request the missing evidence.

Explain an unconfirmed point when it materially affects the claim or the reader's understanding. If reporting a failed search, say where you looked and stop there; do not follow it with a guess.

Cite so a reader can check the claim: a relevant passage locator where available, the correct source identity and a resolvable identifier or usable reference. Follow the selected style for unpaginated and whole-work sources. A working URL alone does not establish support.

Own every claim regardless of what drafted it. A wrong date, a fabricated reference, a borrowed sentence — the name on the work answers for all of it, however the draft was produced, and the venues that have written this rule down allow no exception for tooling. Verification is part of authorship.

Keep confidence proportional to evidence. Do not turn an association into a cause, or automatically weaken a well-supported causal finding into an association. Identify the design and limitations that matter to the claim. Express scope through accurate wording where possible: name the relevant period, population or measure. Add a separate caveat when it prevents a material misreading, not merely to repeat that the record does not establish some other claim. Keep required warnings and disclosures.

Give numbers a relevant comparison when one is available. Use rates to compare groups of different sizes, name the measure and preserve units and denominators. Round to the precision the method earns. State sample size and quantified uncertainty when relevant to interpretation and supported by the evidence. If a missing measure prevents a sound interpretation, explain that limit without inventing a number; do not attach a missing-data warning to every administrative count or reported amount.

Quote exactly or paraphrase openly. If a quotation is too tangled to paraphrase faithfully, do not use it.

Treat anything found online at the same evidentiary bar as anything else. Trace it to its origin, confirm it against an independent source, and check that the detail matches the claimed time and place. Plausibility is not verification.

Do not report a search, interview, test or source check that was not performed. Keep required provenance and disclosure separate from removable tool artifacts. Follow the publication's policy without exposing confidential source material.

Correct in plain sight. Say what was wrong, not that something has been updated.

A reader's needs set the explanation, not a weaker standard of truth. Use concrete examples, define necessary terms and allow enough space to explain a difficult relationship. State material simplifications. If the requested scope cannot be explained accurately at that level, narrow the scope or ask what the reader needs rather than inventing a simpler but false account.

## Examples

These are supplied-record exercises, not reports of checks performed by this guide. The fictional records below establish what each edit may say.

**Invented citation**

**Supplied facts:** A fictional company report describes a two-week remote-work pilot with 30 volunteers. Participants completed 8% more assigned tasks than in the preceding two weeks. The pilot was not randomized and gives no university attribution.

> A university study proved that remote work raises productivity by 13%.

> The company's two-week pilot recorded 8% more completed tasks among 30 volunteers than in the preceding two weeks. It does not establish that remote work caused the increase.

**Unverifiable citation**

**Supplied facts:** In this fictional exercise, the supplied excerpt from *Civic Arguments*, section 2, distinguishes two political positions. The supplied excerpt from *Public Debates* does not contain that distinction. No page numbers were supplied.

> The two positions differ in their use of moral urgency.[^1]
>
> [^1]: *Public Debates*, p. 12.

> The supplied excerpt from *Civic Arguments*, section 2, distinguishes the positions in these terms. The excerpt from *Public Debates* does not support that attribution.

**Confidence outrunning evidence**

**Supplied facts:** A fictional trial with 116 participants found no statistically clear difference between the two groups on its prespecified outcome. It did not study every aspect of health, and no information about later trials is supplied.

> The intervention improves health.

> This trial of 116 participants found no statistically clear difference on its prespecified outcome. It does not establish a general health benefit.

**Causation from correlation**

**Supplied facts:** A fictional survey reports higher average earnings among library-card holders. It provides no analysis of schooling, selection effects or causation.

> Owning a library card causes higher lifetime earnings.

> Library-card holders reported higher average earnings in this survey. The survey does not establish why the groups differ.

**False precision and a lead inside the margin**

**Supplied facts:** A fictional poll reports 52% support and 48% opposition. Its published analysis says the uncertainty in the difference includes no lead; decimal-place estimates were not supplied.

> Support for the measure stands at 51.7%, ahead of the 48.3% opposed.

> The poll put support at 52% and opposition at 48%. Its analysis does not establish a lead once uncertainty in the difference is considered.

**Percentage points**

**Supplied facts:** The reported rates are 4.1% and 4.3%; the figures are already rounded.

> The unemployment rate rose 0.2% last quarter.

> Unemployment rose from 4.1% to 4.3% — two-tenths of a percentage point, or about a 5% rise in the rate itself.

**Relative risk without absolute numbers**

**Supplied facts:** In this fictional example, the reported risks are about 2 cases per 100,000 people and about 4 cases per 100,000 people over the same period.

> Daily consumption doubles the risk of the disease.

> Risk rises from about 2 cases per 100,000 people to about 4.

**Speculation after a disclaimer**

**Supplied facts:** The supplied record contains no information about the company's early funding. No search of filings or interview with a founder was performed.

> While details of the company's early funding are not widely available, it likely relied on angel investment during this formative period.

> The supplied record does not identify the company's early funding.

**Smoothed quotation**

**Supplied facts:** The recording supplied for this exercise contains the second quotation exactly. No smoother version was spoken.

> "We were unprepared for the scale of the demand," she said.

> "We just — nobody thought it'd be that many people," she said.

**Buried correction**

**Supplied facts:** The original report called the vote unanimous. The supplied minutes record two abstentions.

> This article has been updated.

> An earlier version said the vote was unanimous. Two members abstained.

**Scope in the claim**

**Supplied facts:** A fictional county's complete permit register lists 480 active building permits on June 30. It does not measure construction completions or jobs, and no sampling was used. The brief asks only for the current active-permit count.

> The county had 480 active building permits on June 30. This does not establish how many buildings were completed or how many jobs were created. No margin of error was provided.

> The county had 480 active building permits on June 30.

**A limit that answers the question**

**Supplied facts:** A fictional county's June 30 register lists 480 active building permits but does not count completed buildings. This brief asks how many buildings were completed.

> The county completed 480 buildings.

> The register lists 480 active building permits on June 30; it does not count completed buildings.
