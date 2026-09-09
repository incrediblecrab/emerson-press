---
id: citation.ieee
layer: citation
version: 1.1.0
status: draft
budget: 1133
tokens: 1133
edition: "IEEE living reference guidance, revision unpinned; earlier V 3.28.2025 note not independently reverified"
evidence:
  - sources/citation-authority.md
---

# Citation: IEEE

Use this adapter where the venue requests formal IEEE references. Follow its specified guide revision and local rules; the living guide's redirected document was not audited in this review. The patterns below are a working baseline, not certification of every current clause. Preserve source identity, type and supplied fields, and flag gaps instead of filling them with plausible metadata.

## Detect

- **Citation grouping inconsistent with the verified venue rule.** Range compression and bracket grouping remain unresolved in the current-guide audit. Do not declare a supported range obsolete on that basis.
- **An ambiguous citation group or locator.** This adapter's working examples use separate brackets for sources and a comma inside a bracket for a locator; check the venue before changing another accepted form.
- **Alphabetical reference list.** IEEE orders by first appearance, and the numbering is the ordering — there is nothing else to sort by.
- **A source renumbered on later mention.** One number per source, for the life of the document.
- **Surname-first authors.** IEEE leads with initials: `A. B. Nakamura`.
- **Superscripts or parentheses.** `¹` or `(1)`. IEEE brackets, on the line.
- **Bracket outside the punctuation.** `... under drift. [1]` The bracket precedes the period.
- **An invented journal abbreviation.** Use the established abbreviation, such as `IEEE Trans. Signal Process.`, rather than guessing for an unfamiliar title.
- **`https://doi.org/` in a reference.** That is APA, MLA, and Chicago form. IEEE takes a bare `doi: 10.xxxx/yyyy`.
- **URL punctuation inconsistent with the selected reference model.** The working online pattern below leaves the URL without a terminal period.
- **An online source with no `[Online]. Available:`.**
- **A conference paper, standard, patent, dataset, software package, report, preprint, or website forced into the journal-article template.**
- **`ibid.` or `op. cit.`** Numbered citation has no use for either.
- **An invented AI citation or use disclosure.** Failed retrieval does not establish that IEEE has no citation format, and a reference entry does not prove what assistance occurred.

## Write

Number sources by order of first appearance and reuse that number every time the source recurs. The reference list is that same sequence, so ordering it is not a separate decision.

The Author Center reference-guide URL redirected to a hosted Google document during this review. Its revision and detailed clauses were not independently checked. Verify the actual guide and venue instructions for disputed rules instead of repeating an old live-document date as a pinned current edition.

Put the bracket where the support lands, inside the sentence punctuation: `... under drift [1].` Constructions such as `in [1]` can avoid redundant citation wording. Preserve an author's name when it is integral to the sentence or attribution; do not delete meaningful attribution merely to make the brackets stand alone.

The working group format here is `[1], [2], [3]`; it is not evidence that the current guide abolished range compression. Keep a venue-approved alternative. Locator examples include `[3, pp. 5–10]` and `[3, Fig. 1]`, using actual pages or figure identifiers. Exact section, equation and other locator labels depend on the applicable rule; no exhaustive list was verified here. Do not invent a source location to satisfy the format.

In the list: initials before surname; article title in quotation marks and sentence case; journal or conference title abbreviated and italic in title case; then volume, number, pages, abbreviated month, year. Name up to six authors; at seven or more, give the first author and `et al.` In running text use `et al.` from three names.

```
[1] A. B. Author, "Title of paper," Abbrev. J. Title, vol. x, no. x,
    pp. xxx–xxx, Abbrev. Mon. year, doi: 10.xxxx/yyyy.
```

Where a journal numbers articles instead of paginating, use its actual article number rather than invented pages. Distinguish accepted-but-unpublished work from published early-access material and use the venue's corresponding form. Keep the supplied `thesis` or `dissertation` source type; do not change it to match an assumed degree convention.

Do not force non-journal sources into the journal pattern. Conference proceedings use the paper title, `in` the actual conference name, year, pages and DOI when supplied; a presented-only paper is a different type. Standards, patents, technical reports, datasets, software and preprints need their own identifying fields. Keep actual standard or patent numbers, issuing bodies, versions, dates, repositories and persistent identifiers. Never infer a conference or journal identity from a DOI's shape or invent an abbreviation for an unknown container.

For the working online-reference model, use `Accessed: [actual access date]. [Online]. Available:` followed by the URL without a terminal period. Omit or flag unknown fields as the applicable model allows; do not supply today's date as evidence of a visit. A DOI at the end of the working journal model takes a period.

Check the actual IEEE venue's AI-use, disclosure and citation policy. No universal current AI-reference form was verified here, which is not proof that none exists. Describe only recorded assistance; do not invent a model, a section drafted, source checking or an acknowledgment placement.

## Examples

**Grouping under an explicit venue rule**

**Supplied facts:** Synthetic references 1, 2 and 3 support the statement. This exercise's venue explicitly requests separate brackets. The edit does not claim that all IEEE venues forbid compressed ranges.

> Several groups report this [1]-[3].

> Several groups report this [1], [2], [3].

**Numbers sharing a bracket**

**Supplied facts:** Synthetic references 2, 5 and 9 are trials supporting the stated effect. The venue requests separate source brackets, not a grouped form.

> Later trials confirmed the effect [2, 5, 9].

> Later trials confirmed the effect [2], [5], [9].

**Renumbering a source already cited**

**Supplied facts:** Both mentions identify the same fictional report, first assigned number 2. Its supplied contents include the confirmation and drift figure. Number 5 was an accidental renumbering, not a different source.

> ... confirmed in [2]. The same report gives the drift figure in [5].

> ... confirmed in [2]. The same report gives the drift figure in [2].

**Author order, journal abbreviation, DOI form**

**Supplied facts:** The illustrative record supplies author Akira B. Nakamura, the title, journal, year and DOI shown, and the established journal abbreviation `IEEE Trans. Signal Process.` No volume, issue, page range or month is supplied. The fictional article and DOI are not a claim of an actual publication.

> [1] Nakamura, Akira B., "Sparse recovery under drift," *IEEE Transactions on Signal Processing*, 2023. https://doi.org/10.1109/TSP.2023.0000

> [1] A. B. Nakamura, "Sparse recovery under drift," *IEEE Trans. Signal Process.*, 2023, doi: 10.1109/TSP.2023.0000.

Review note: verify the missing publication fields before treating this as a complete reference. They cannot be supplied by formatting alone.

**Bracket position against the period**

**Supplied facts:** Synthetic source 4 supports the exact statement that the estimator diverges above 40 dB. Only bracket placement is being edited; no new threshold or test result is inferred.

> The estimator diverges above 40 dB. [4]

> The estimator diverges above 40 dB [4].

**Locator inside the bracket**

**Supplied facts:** The requested locations in synthetic source 3 are page 7 and figure 1. The venue accepts the locator forms used below.

> See page 7 of [3] and figure 1 of [3].

> See [3, p. 7] and [3, Fig. 1].

**Source type is not inferred from a DOI**

**Supplied facts:** The record explicitly identifies this fictional work as a journal article with the author, title, journal, year and DOI below. It supplies no proceedings title, conference record or page range.

> [2] B. L. Ortega, "Clock drift in field radios," *Journal of Signal Networking*, 2026, doi: 10.1109/NET.2026.0002.

> [2] B. L. Ortega, "Clock drift in field radios," *Journal of Signal Networking*, 2026, doi: 10.1109/NET.2026.0002.

Review note: preserve the journal identity and verify the remaining fields and abbreviation. The DOI's appearance does not justify turning the source into a conference paper.

**Generative AI without a usage record**

**Supplied facts:** The proposed entry supplies only ChatGPT, OpenAI, 2025 and the tool URL. There is no record of which model was used, what it did, which section it affected or the venue's required disclosure format.

> [7] ChatGPT, OpenAI, 2025. [Online]. Available: https://chat.openai.com

> Disclosure incomplete: confirm the actual assistance and the applicable venue policy. This entry does not establish that any section was drafted by the tool or that an acknowledgment is the required form.
