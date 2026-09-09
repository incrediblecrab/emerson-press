---
id: citation.apa7
layer: citation
version: 1.1.0
status: draft
budget: 1242
tokens: 1242
edition: "7th (2019) working baseline; September 2025 AI formats not independently verified"
evidence:
  - sources/citation-authority.md
---

# Citation: APA 7

Apply this adapter to formal APA citations when requested, subject to the venue's adopted edition and local requirements. Preserve source identity, source type and known fields; expose missing metadata instead of completing it by inference. The source dossier distinguishes the working print baseline from unverified living guidance. Correct formatting does not establish retrieval or factual support.

## Detect

- **A publisher's city.** `New York, NY: Basic Books`. The 7th edition dropped publication place entirely.
- **`Retrieved from` before an ordinary URL.** Retrieval dates are for mutable pages; an undated but stable source takes `(n.d.)`, not a retrieval formula.
- **A bare `doi:` prefix.** APA takes the resolver form, `https://doi.org/10.xxxx`. The bare form belongs to AMA (`doi:10.xxxx`, no space) and IEEE (`doi: 10.xxxx`, with one) — and those two differ from each other, so a bare prefix is never a safe default.
- **`&` joining cited authors in running prose**, or `and` joining them inside a parenthetical citation. This does not authorize changing an ampersand in a quotation, source title or official name.
- **All authors named in text for a three-author work.** APA uses `et al.` from three authors, and from the *first* citation — there is no name-them-once-then-abbreviate step.
- **`et al.` for a two-author work.** Two authors are always both named.
- **A period after `et`.** Only `al.` takes one.
- **Title case in a reference-list article or book title.** Those go sentence case; the journal *name* stays title case.
- **An italicized issue number.** The volume italicizes; the issue in parentheses does not.
- **`. . . &` in a 21-plus-author reference.** After the ellipsis the final author follows with no ampersand.
- **A hyphen in a page range.** APA sets number ranges with an en dash: `225–250`.
- **Multiple works in one parenthetical out of alphabetical order.**
- **`personal communication` in the reference list.** It is cited in text only.
- **An AI entry built from an unverified template.** Establish whether the citation concerns software, a particular output or another source type; do not infer current rules from another publisher.
- **A citation to AI search.** If AI only helped find sources, cite the sources actually used, not the search interface.

## Write

Use author-date citations: `(Ali, 2024)` parenthetically, `Ali (2024)` narratively. Use the manual's applicable missing-author or missing-date form when needed, not a fabricated person or year. Add an available locator for a quotation: `(Ali, 2024, p. 42)`. Do not invent pagination. Three or more authors take `et al.` from first mention. Where that collapses two different works to the same form, name as many authors as it takes to tell them apart.

```
Author, A. A. (Year). Title of work in sentence case. Journal Name in Title
    Case, Volume(Issue), pages. https://doi.org/10.xxxx/yyyy
```

List up to twenty authors. At twenty-one or more, give the first nineteen, an ellipsis, then the final author — no ampersand before it.

Head the list `References`. Alphabetize by first author's surname; hanging indent. Where one author has several works in a year, suffix the years `a`, `b`, `c` by title order, and use the same suffix in text.

In the reference list, sentence case for the titles of articles, chapters, books and reports: capitalize the first word, the first word after a colon, and proper nouns only. Title case for the periodical's own name. In running text the rule inverts — a title mentioned in a sentence takes title case. Italicize the volume number with the journal name; leave the issue number roman inside parentheses.

Give an established DOI in resolver form, with no terminal period. Use a URL where the source-specific model calls for one and a relevant address is available; a print source without a DOI or URL does not become a website. Add an actual retrieval date for content designed to change when the applicable model requires it. A missing publication date does not by itself establish mutability; use `(n.d.)` for an undated source rather than inventing a year or visit.

Block a quotation of forty words or more: indent it, drop the quotation marks, and put the citation after the final period.

Cite non-retrievable personal communications from people in text alone: `(A. Ali, personal communication, August 14, 2025)`. A published interview or recorded lecture is a different source type. Do not automatically classify a private AI exchange as personal communication merely because it lacks a public link.

For education-policy staples, choose source-specific fields: data sets use `[Data set]`; dissertations and theses identify the actual institution and retrievable source; conference papers, technical reports, standards and agency reports retain their real sponsoring or issuing body where applicable. Do not add a bracketed source-type label to every entry. When an agency is both author and publisher, do not repeat it as publisher. For a source known only through another source, cite `as cited in` in text and list only the work actually read.

The September 2025 AI citation formats were not verified in this review. Do not impose a purported current `[Generative AI chat]` format, a private-chat rule or a share-link requirement on that basis. Check the actual APA guidance and venue policy for the source being cited. Preserve the recorded tool, provider, model, date and link without inventing missing fields. Citation does not replace required assistance disclosure; AI-assisted discovery does not justify citing underlying sources that nobody consulted.

## Examples

**Publisher location and the old retrieval formula**

**Supplied facts:** The fictional 2024 book is by Nadia Ali, published by Winslow Press in New York, with the stable online address shown. The task requests the working APA 7 book form; no retrieval date is supplied or needed for this stable source.

> Ali, N. (2024). *The unreliable archive*. New York, NY: Winslow Press. Retrieved from https://example.org/archive

> Ali, N. (2024). *The unreliable archive*. Winslow Press. https://example.org/archive

**Ampersand on the wrong side of the parenthesis**

**Supplied facts:** The synthetic work is by Ali and Moreau, dated 2024, and supports the two statements as drafted. Only the author-citation punctuation is at issue.

> Ali & Moreau (2024) found the opposite, and the effect held (Ali and Moreau, 2024).

> Ali and Moreau (2024) found the opposite, and the effect held (Ali & Moreau, 2024).

**Naming three authors in full**

**Supplied facts:** Ali, Moreau and Okonkwo wrote the fictional 2024 work in that order and reported unresolved provenance. No other cited work creates an ambiguous short form.

> Ali, Moreau, and Okonkwo (2024) reported that the provenance was unresolved.

> Ali et al. (2024) reported that the provenance was unresolved.

**Title case in a reference-list entry**

**Supplied facts:** The fictional source has exactly the authors, journal, year, volume, issue and pages shown. Its article title contains no proper noun. Change title capitalization, not bibliographic fields.

> Ali, N., Moreau, C., & Okonkwo, I. (2024). The Provenance Of Municipal Archives. *Winslow Quarterly, 12*(3), 225–250.

> Ali, N., Moreau, C., & Okonkwo, I. (2024). The provenance of municipal archives. *Winslow Quarterly, 12*(3), 225–250.

**DOI form**

**Supplied facts:** The supplied illustrative DOI is `10.1234/wq.2024.12`. The ellipsis stands for an unchanged reference prefix; no source lookup or additional metadata is implied.

> ... *Winslow Quarterly, 12*(3), 225–250. doi:10.1234/wq.2024.12

> ... *Winslow Quarterly, 12*(3), 225–250. https://doi.org/10.1234/wq.2024.12

**Generative AI with an unverified link and format**

**Supplied facts:** The record names ChatGPT, OpenAI, the topic and August 14, 2025, but supplies no actual conversation URL or model. The URL below is an unverified placeholder. Review the entry; the proposed 2025 APA source-type format has not been established.

> ChatGPT. (2025, August 14). *Provenance of the Winslow archive* [Generative AI chat]. OpenAI. https://chatgpt.com/share/abcd-1234

> Citation incomplete: retain the recorded tool, provider, topic and date, but remove the placeholder URL. Confirm the source type and applicable APA/venue format before completing the entry.

**The tool itself rather than one session**

**Supplied facts:** This formatting exercise explicitly supplies a venue's software-style template: provider as author, supplied release year, italicized tool name, `[Large language model]`, then tool URL. The record gives OpenAI, ChatGPT, 2025 and `https://chatgpt.com`; it does not identify a conversation or model version. This demonstrates the supplied template, not verification of a current APA AI update.

> ChatGPT. (2025). *OpenAI* [Large language model]. https://chatgpt.com

> OpenAI. (2025). *ChatGPT* [Large language model]. https://chatgpt.com
