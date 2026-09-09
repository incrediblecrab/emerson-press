---
id: citation.ama11
layer: citation
version: 1.1.0
status: draft
budget: 1176
tokens: 1176
edition: "11th (2020) working baseline; current online updates not comprehensively verified"
evidence:
  - tests/sources/citation-authority.md
---

# Citation: AMA 11

Use this adapter where the venue requests formal AMA references. It does not replace patient-readable attribution or require superscripts on a handout with no reference list. Follow the venue's adopted rules within their scope. The source dossier records verification limits, not a fresh audit of the entire manual.

Preserve source identity and supplied metadata. Missing authors, dates, locators and identifiers stay missing until established; formatting a reference does not prove retrieval or support for a claim.

## Detect

- **A bracketed or parenthetical number where AMA superscripts are required.** Other numbered styles use different forms; do not change a venue's explicitly required system.
- **A superscript before the period or comma.** It goes after them — and before a colon or semicolon.
- **An alphabetized reference list.** AMA numbers by order of first appearance.
- **Periods or spaces in author initials.** `Smith, A. B.` AMA writes `Smith AB` — no comma, no periods, no internal space.
- **All authors listed for a seven-author paper.** Six or fewer are named in full; seven or more collapse to the first three and `et al`.
- **`https://doi.org/` in a reference.** AMA takes the bare `doi:10.xxxx`, lowercase, with no space after the colon. This is the reverse of APA, MLA and Chicago.
- **An unverified journal abbreviation.** Use the applicable NLM form when established; do not invent an abbreviation for an unfamiliar title.
- **Title case on an article title.** Sentence case there; the abbreviated journal name stays title case and italic.
- **Spaces inside the year-volume-issue-page cluster.** It closes up: `2024;12(3):225-231.`
- **An invented access date**, or a URL that points to a different source from the supplied DOI.
- **An en dash where a hyphen belongs** in a span of three or more consecutive references.
- **A space-limited reference format carried into a manuscript without permission.** Verify which short form the venue accepts.
- **AI use or verification asserted without a record.** Citation, assistance disclosure and permission to use the tool are separate questions.

## Write

Cite with a superscript numeral, numbered by first appearance and reused for every later mention of the source. Place it after a period or comma, before a colon or semicolon, and outside a closing quotation mark. Where a name carries the sentence, the numeral follows the name directly: `Ali et al⁴ reported ...`

Separate several references with commas and no spaces: `¹,³,⁵`. Compress three or more consecutive references with a hyphen: `⁶⁻⁸`. Two consecutive references stay a comma pair, `⁴,⁵`, and a mixed run reads `³,⁵⁻⁷`.

```
Author AB, Author CD, Author EF. Article title in sentence case. Abbrev J Name.
    Year;Volume(Issue):FirstPage-LastPage. doi:10.xxxx/yyyy
```

Name up to six authors; at seven or more give the first three and `et al`. In a reference-list author element this appears as `et al.` because the period closes that element; in running prose write `Ali et al` without a period unless the sentence itself ends there. Write surname then initials, closed up and unpunctuated. Abbreviate the journal name to the NLM form, which carries no internal periods — `N Engl J Med`, not `N. Engl. J. Med.` A single period still closes the element.

Keep the publication cluster tight — no spaces around the semicolon, the parentheses or the colon. Where a journal has no issue number, omit the parentheses. For an article published online ahead of an issue, use the applicable published-online form and its actual publication date. Do not substitute an access date, invent a posting date, or confuse published-online and accepted-but-unpublished status.

Use a supplied DOI in the `doi:` form, with no terminal period. Preserve its identifier. For a web reference without a DOI, retain the actual URL and distinguish publication, revision and access dates. The exact AMA ordering of those web-reference elements was not verified in this review; consult the applicable rule rather than guessing whether the access date precedes or follows the URL. Never claim an access date for a visit that did not occur.

Give inclusive page numbers in full: `225-231`, never `225-31`. AMA does not elide repeated digits, which is the reverse of MLA (`pp. 225-50`) and of Chicago's more elaborate rule. Check this one whenever a reference has been carried over from another style.

For health-policy sources that are not journal articles, choose the source-specific model rather than forcing a journal shell. Books take publisher and year; chapters add `In:` editors, book title, publisher, year, and pages when supplied. Reports, websites, package inserts, ClinicalTrials.gov records, preprints, data sets, conference presentations, and "cited by" references need the applicable identifying fields. Do not manufacture them to complete a template.

Use a short-form reference only when the venue permits it for the format, such as a poster or slide. A space limit alone does not establish which elements may be omitted.

Current online AI-specific guidance was not comprehensively checked. Apply the actual journal's citation and disclosure policy. Name the tool, version, purpose or generation date only when supported by the usage record, and do not invent a prompt or claim that an output was checked. Cite underlying evidence actually consulted; a formatted AI disclosure does not verify it.

## Examples

**Bracketed number, and a superscript on the wrong side of the period**

**Supplied facts:** In this synthetic exercise, reference 4 is one trial reporting no effect and reference 5 is another trial reporting an effect. Only the citation placement needs editing.

> One trial [4] found no effect. Another trial disagreed⁵.

> One trial found no effect.⁴ Another trial disagreed.⁵

**Superscript against a colon**

**Supplied facts:** Synthetic reference 6 reports the stated pattern in the three named cohorts. Preserve the claim and cohort labels; move only the citation.

> The pattern held in every cohort:⁶ children, adults, and the elderly.

> The pattern held in every cohort⁶: children, adults, and the elderly.

**Author initials**

**Supplied facts:** The synthetic author record gives surnames Ali, Moreau and Okonkwo, with initials NA, CR and IT, in that order.

> Ali, N. A., Moreau, C. R., & Okonkwo, I. T.

> Ali NA, Moreau CR, Okonkwo IT.

**Journal name, capitalization, spacing and DOI form**

**Supplied facts:** This fictional article has authors Ali NA and Moreau CR, the title shown, year 2024, volume 12, issue 3, pages 225-231 and the illustrative DOI shown. The exercise supplies `J Clin Arch` as its journal abbreviation; this is not a claim that the fictional journal has an NLM entry.

> Ali NA, Moreau CR. The Provenance Of Municipal Archives. *Journal of Clinical Archiving*. 2024; 12 (3): 225-231. https://doi.org/10.1234/jca.12

> Ali NA, Moreau CR. The provenance of municipal archives. *J Clin Arch*. 2024;12(3):225-231. doi:10.1234/jca.12

**Seven authors**

**Supplied facts:** This synthetic reference has exactly the seven authors listed below, in that order. Apply the working AMA author-count rule without changing their names.

> Ali NA, Moreau CR, Okonkwo IT, Bell RS, Nakamura AB, Vidal PJ, Osei KL.

> Ali NA, Moreau CR, Okonkwo IT, et al.

**Reference spans**

**Supplied facts:** The first synthetic comparison cites sources 6, 7 and 8; the second cites 3, 5, 6 and 7. These are overlapping source sets, not a claim about a count of trials or reviews.

> The first comparison⁶,⁷,⁸ and the second³,⁵,⁶,⁷ draw on different source sets.

> The first comparison⁶⁻⁸ and the second³,⁵⁻⁷ draw on different source sets.

**Online ahead of an issue**

**Supplied facts:** The fictional article's publication record supplies the author, title, abbreviation and DOI below, confirms online publication on February 15, 2024, and assigns no issue yet. That date is publication metadata, not an inferred access date.

> Ali NA. The provenance of municipal archives. *J Clin Arch*. 2024;[Epub ahead of print]. doi:10.1234/jca.12

> Ali NA. The provenance of municipal archives. *J Clin Arch*. Published online February 15, 2024. doi:10.1234/jca.12

**Generative AI without a verification record**

**Supplied facts:** The author reports querying ChatGPT, made by OpenAI, about a policy memo on June 12, 2026. The record does not give the model, exact prompt, section drafted or any source-checking activity. Review the proposed disclosure; do not certify its compliance with an unread journal policy.

> OpenAI. ChatGPT response to policy memo prompt. Generated June 12, 2026.

> The author queried ChatGPT (OpenAI) about a policy memo on June 12, 2026.

Review note: confirm the actual use and the venue's required disclosure fields before publication. Nothing in the record establishes a model version, the exact prompt or verification against cited sources.
