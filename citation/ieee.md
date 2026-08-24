---
id: citation.ieee
layer: citation
version: 1.0.2
status: draft
budget: 1261
tokens: 1261
edition: IEEE Reference Guide, V 3.28.2025 (live Author Center Google Doc checked Aug. 9, 2026); IEEE Editorial Style Manual for Authors
---

# Citation: IEEE

## Detect

- **Range compression in brackets.** `[1]-[4]` and `[1]–[4]`. The current Reference Guide abolished the dash form. Every number gets its own brackets: `[1], [2], [3], [4]`.
- **Numbers sharing a bracket.** `[1, 2, 3]`. A comma inside the bracket introduces a *locator*, not another source.
- **Stacked brackets.** `[1][2][3]` with no separator.
- **Alphabetical reference list.** IEEE orders by first appearance, and the numbering is the ordering — there is nothing else to sort by.
- **A source renumbered on later mention.** One number per source, for the life of the document.
- **Surname-first authors.** IEEE leads with initials: `A. B. Nakamura`.
- **Superscripts or parentheses.** `¹` or `(1)`. IEEE brackets, on the line.
- **Bracket outside the punctuation.** `... under drift. [1]` The bracket precedes the period.
- **Spelled-out journal titles.** IEEE abbreviates: `IEEE Trans. Signal Process.`
- **`https://doi.org/` in a reference.** That is APA, MLA, and Chicago form. IEEE takes a bare `doi: 10.xxxx/yyyy`.
- **A period after a URL.** URLs never take one; everything else does.
- **An online source with no `[Online]. Available:`.**
- **A conference paper, standard, patent, dataset, software package, report, preprint, or website forced into the journal-article template.**
- **`ibid.` or `op. cit.`** Numbered citation has no use for either.
- **An invented format for AI output.** IEEE publishes no citation form for generative AI — only a disclosure requirement.

## Write

Number sources by order of first appearance and reuse that number every time the source recurs. The reference list is that same sequence, so ordering it is not a separate decision.

IEEE serves the Reference Guide as a living Author Center Google Doc. As checked on Aug. 9, 2026, the live guide still displays `V 3.28.2025`; treat that as a checked live stamp, not as a stable edition name.

Put the bracket where the support lands, inside the sentence punctuation: `... under drift [1].` Both bare and anchored forms work — the Reference Guide treats brackets as nouns, so `[1] shows` is not an error, and a preposition may anchor them, `in [1]`, `according to [1]`. An author's name may not: the Editorial Style Manual directs `In Smith [1]` to be changed to `in [1]` unless the name is integral to the sentence. Avoid `reference [1]` outright; the Style Manual rules it out rather than merely omitting it.

Cite several sources as separate brackets in a comma series: `[1], [2], [3]`. Do not compress and do not combine. A comma *inside* a bracket introduces a locator: `[3, pp. 5–10]`, `[3, Fig. 1]`, `[3, eq. (2)]`, `[3, Sect. 4.5]`, `[3, Ch. 2, pp. 5–10]`, `[3, Thm. 1]`, `[3, Lemma 2]`, `[3, Algorithm 5]`, `[3, Appendix I]`. Those nine are the guide's whole list, and its capitalization is uneven on purpose — `pp.` and `eq.` lowercase, the rest capitalized, `Algorithm` never shortened. Leave all of it as the guide has it; the `Sec.`, `Th.` and `Alg.` that circulate in secondary guides are not IEEE's forms. Page spans inside a locator take an en dash.

In the list: initials before surname; article title in quotation marks and sentence case; journal or conference title abbreviated and italic in title case; then volume, number, pages, abbreviated month, year. Name up to six authors; at seven or more, give the first author and `et al.` In running text use `et al.` from three names.

```
[1] A. B. Author, "Title of paper," Abbrev. J. Title, vol. x, no. x,
    pp. xxx–xxx, Abbrev. Mon. year, doi: 10.xxxx/yyyy.
```

Where a journal numbers articles instead of paginating, replace the page range with `Art. no. xxx`. Use `to be published` for accepted work — never `to appear in`, which the guide rules out — and the early-access form for material published ahead of an issue. Keep whichever of `thesis` or `dissertation` the author used; the guide forbids changing it to match an assumed convention for the degree level.

Do not force non-journal sources into the journal pattern. Conference proceedings use the paper title, `in` the abbreviated conference name, year, pages, and DOI if supplied. Presented-only conference papers use `presented at`. Standards start with the standard title and number. Patents lead with the inventor and the patent title in quotation marks, then the patent number and the date; only the online form inverts this, leading with the invention name, then `by` and the inventor. Technical reports use `Rep. no.` when there is one. Datasets give author, date, dataset title, source, and DOI or URL. Software/code should identify authors, software name, repository or location, version, release date, and persistent identifier when available. arXiv preprints use the year and arXiv number.

Close online sources with `Accessed: Mar. 2, 2026. [Online]. Available:` and the URL. Nothing follows the URL — no period. A DOI, when it ends the reference, does take one.

## Examples

**Range compression, abolished in the current guide**

> Several groups report this [1]-[3].

> Several groups report this [1], [2], [3].

**Numbers sharing a bracket**

> Later trials confirmed the effect [2, 5, 9].

> Later trials confirmed the effect [2], [5], [9].

**Renumbering a source already cited**

> ... confirmed in [2]. The same report gives the drift figure in [5].

> ... confirmed in [2]. The same report gives the drift figure in [2].

**Author order, journal abbreviation, DOI form**

> [1] Nakamura, Akira B., "Sparse recovery under drift," *IEEE Transactions on Signal Processing*, 2023. https://doi.org/10.1109/TSP.2023.0000

> [1] A. B. Nakamura, "Sparse recovery under drift," *IEEE Trans. Signal Process.*, vol. 71, no. 4, pp. 210–219, Apr. 2023, doi: 10.1109/TSP.2023.0000.

**Bracket position against the period**

> The estimator diverges above 40 dB. [4]

> The estimator diverges above 40 dB [4].

**Locator inside the bracket**

> See page 7 of [3] and figure 1 of [3].

> See [3, p. 7] and [3, Fig. 1].

**Conference paper, not a journal article**

> [2] B. L. Ortega, "Clock drift in field radios," *Journal of Signal Networking*, 2026, doi: 10.1109/NET.2026.0002.

> [2] B. L. Ortega, "Clock drift in field radios," in *Proc. IEEE Int. Conf. Netw. Protocols*, 2026, pp. 44–49, doi: 10.1109/NET.2026.0002.

**Generative AI.** IEEE has no citation format for AI output. Disclose the use in the acknowledgments; do not build a reference entry for it.

> [7] ChatGPT, OpenAI, 2025. [Online]. Available: https://chat.openai.com

> The authors used a large language model to draft portions of Section III. (in the acknowledgments; no reference entry)
