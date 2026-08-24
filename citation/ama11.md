---
id: citation.ama11
layer: citation
version: 1.0.1
status: draft
budget: 1006
tokens: 1006
edition: 11th (2020), with online updates through 2026
---

# Citation: AMA 11

## Detect

- **A bracketed or parenthetical number in the text.** `[1]` is IEEE, `(1)` is neither. AMA sets the numeral as a superscript.
- **A superscript before the period or comma.** It goes after them — and before a colon or semicolon.
- **An alphabetized reference list.** AMA numbers by order of first appearance.
- **Periods or spaces in author initials.** `Smith, A. B.` AMA writes `Smith AB` — no comma, no periods, no internal space.
- **All authors listed for a seven-author paper.** Six or fewer are named in full; seven or more collapse to the first three and `et al`.
- **`https://doi.org/` in a reference.** AMA takes the bare `doi:10.xxxx`, lowercase, with no space after the colon. This is the reverse of APA, MLA and Chicago.
- **A journal name spelled out.** AMA abbreviates per the NLM list, without periods.
- **Title case on an article title.** Sentence case there; the abbreviated journal name stays title case and italic.
- **Spaces inside the year-volume-issue-page cluster.** It closes up: `2024;12(3):225-231.`
- **An access date with no URL**, or a URL where a DOI already answers.
- **An en dash where a hyphen belongs** in a span of three or more consecutive references.
- **A full manuscript reference squeezed onto a poster, or a short-form poster reference used in a manuscript.** AMA now has a short-form option, but only for space-limited formats.
- **An AI tool treated as an author.** AMA documents LLM use in methods or acknowledgments, not as an ordinary source in the reference list.

## Write

Cite with a superscript numeral, numbered by first appearance and reused for every later mention of the source. Place it after a period or comma, before a colon or semicolon, and outside a closing quotation mark. Where a name carries the sentence, the numeral follows the name directly: `Ali et al⁴ reported ...`

Separate several references with commas and no spaces: `¹,³,⁵`. Compress three or more consecutive references with a hyphen: `⁶⁻⁸`. Two consecutive references stay a comma pair, `⁴,⁵`, and a mixed run reads `³,⁵⁻⁷`.

```
AuthorAB, AuthorCD, AuthorEF. Article title in sentence case. Abbrev J Name.
    Year;Volume(Issue):FirstPage-LastPage. doi:10.xxxx/yyyy
```

Name up to six authors; at seven or more give the first three and `et al`. In a reference-list author element this appears as `et al.` because the period closes that element; in running prose write `Ali et al` without a period unless the sentence itself ends there. Write surname then initials, closed up and unpunctuated. Abbreviate the journal name to the NLM form, which carries no internal periods — `N Engl J Med`, not `N. Engl. J. Med.` A single period still closes the element.

Keep the publication cluster tight — no spaces around the semicolon, the parentheses or the colon. Where a journal has no issue number, omit the parentheses. Where an article has appeared online without an issue, replace the cluster with `Published online` and the date.

Close with a DOI when one exists, bare and lowercase, with no terminal period. Only where there is no DOI does a URL follow, and only then does an access date follow that: `Accessed March 7, 2024.` The URL takes no period; the access date does.

Give inclusive page numbers in full: `225-231`, never `225-31`. AMA does not elide repeated digits, which is the reverse of MLA (`pp. 225-50`) and of Chicago's more elaborate rule. Check this one whenever a reference has been carried over from another style.

For health-policy sources that are not journal articles, keep the AMA order rather than forcing a journal shell: author or agency; title; container or publisher; date; DOI or, if no DOI, access date plus URL. Books take publisher and year; chapters add `In:` editors, book title, publisher, year, and pages. Reports, websites, package inserts, ClinicalTrials.gov records, preprints, data sets, conference presentations, and "cited by" references need enough type labels and dates for a reader to identify exactly what was used.

Use §3.18 short-form references only where space is constrained, such as posters or slides. Short form trims references to the identifying essentials; do not use it to shorten a normal manuscript reference list.

## Examples

**Bracketed number, and a superscript on the wrong side of the period**

> Three trials [4] found no effect. A fourth trial disagreed⁵.

> Three trials found no effect.⁴ A fourth trial disagreed.⁵

**Superscript against a colon**

> The pattern held in every cohort:⁶ children, adults, and the elderly.

> The pattern held in every cohort⁶: children, adults, and the elderly.

**Author initials**

> Ali, N. A., Moreau, C. R., & Okonkwo, I. T.

> Ali NA, Moreau CR, Okonkwo IT.

**Journal name, capitalization, spacing and DOI form**

> Ali NA, Moreau CR. The Provenance Of Municipal Archives. *Journal of Clinical Archiving*. 2024; 12 (3): 225-231. https://doi.org/10.1234/jca.12

> Ali NA, Moreau CR. The provenance of municipal archives. *J Clin Arch*. 2024;12(3):225-231. doi:10.1234/jca.12

**Seven authors**

> Ali NA, Moreau CR, Okonkwo IT, Bell RS, Nakamura AB, Vidal PJ, Osei KL.

> Ali NA, Moreau CR, Okonkwo IT, et al.

**Reference spans**

> Several trials⁶,⁷,⁸ and two reviews³,⁵,⁶,⁷ agree.

> Several trials⁶⁻⁸ and two reviews³,⁵⁻⁷ agree.

**Online ahead of an issue.** `In press` is not an error — it is a different status, for work accepted but not yet posted. Once the article is online with a DOI, it takes the published-online form.

> Ali NA. The provenance of municipal archives. *J Clin Arch*. 2024;[Epub ahead of print]. doi:10.1234/jca.12

> Ali NA. The provenance of municipal archives. *J Clin Arch*. Published online February 15, 2024. doi:10.1234/jca.12

**Generative AI.** The 11th edition's online updates added guidance on AI content and on citing online searches. Name the tool, its version or model, the company, the date of generation, and the prompt, and disclose the use in the methods or acknowledgments rather than leaving the reference to carry it alone.

> OpenAI. ChatGPT response to policy memo prompt. Generated June 12, 2026.

> In drafting the background paragraph, the author queried ChatGPT (GPT-4o, OpenAI) on June 12, 2026, with the prompt "List common implementation barriers in school vaccine programs"; the output was checked against cited sources and is not listed as a reference.
