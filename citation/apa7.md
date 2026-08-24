---
id: citation.apa7
layer: citation
version: 1.0.1
status: draft
budget: 1096
tokens: 1096
edition: 7th (Oct. 2019; current as of Aug. 2026); AI reference formats revised Sept. 2025
---

# Citation: APA 7

## Detect

- **A publisher's city.** `New York, NY: Basic Books`. The 7th edition dropped publication place entirely.
- **`Retrieved from` before an ordinary URL.** Retrieval dates are for mutable pages; an undated but stable source takes `(n.d.)`, not a retrieval formula.
- **A bare `doi:` prefix.** APA takes the resolver form, `https://doi.org/10.xxxx`. The bare form belongs to AMA (`doi:10.xxxx`, no space) and IEEE (`doi: 10.xxxx`, with one) — and those two differ from each other, so a bare prefix is never a safe default.
- **`&` in running prose**, or `and` inside a parenthetical citation. The ampersand lives only inside parentheses and in the reference list.
- **All authors named in text for a three-author work.** APA uses `et al.` from three authors, and from the *first* citation — there is no name-them-once-then-abbreviate step.
- **`et al.` for a two-author work.** Two authors are always both named.
- **A period after `et`.** Only `al.` takes one.
- **Title case in a reference-list article or book title.** Those go sentence case; the journal *name* stays title case.
- **An italicized issue number.** The volume italicizes; the issue in parentheses does not.
- **`. . . &` in a 21-plus-author reference.** After the ellipsis the final author follows with no ampersand.
- **A hyphen in a page range.** APA sets number ranges with an en dash: `225–250`.
- **Multiple works in one parenthetical out of alphabetical order.**
- **`personal communication` in the reference list.** It is cited in text only.
- **ChatGPT as the author.** For generative AI, the company is the author; the tool or model is the source element.
- **A citation to AI search.** If AI only helped find sources, cite the sources actually used, not the search interface.

## Write

Author and date, always: `(Ali, 2024)` parenthetically, `Ali (2024)` narratively. Add a page or paragraph for a quotation: `(Ali, 2024, p. 42)`. Three or more authors take `et al.` from first mention. Where that collapses two different works to the same form, name as many authors as it takes to tell them apart.

```
Author, A. A. (Year). Title of work in sentence case. Journal Name in Title
    Case, Volume(Issue), pages. https://doi.org/10.xxxx/yyyy
```

List up to twenty authors. At twenty-one or more, give the first nineteen, an ellipsis, then the final author — no ampersand before it.

Head the list `References`. Alphabetize by first author's surname; hanging indent. Where one author has several works in a year, suffix the years `a`, `b`, `c` by title order, and use the same suffix in text.

In the reference list, sentence case for the titles of articles, chapters, books and reports: capitalize the first word, the first word after a colon, and proper nouns only. Title case for the periodical's own name. In running text the rule inverts — a title mentioned in a sentence takes title case. Italicize the volume number with the journal name; leave the issue number roman inside parentheses.

Give a DOI whenever one exists, in resolver form, with no terminal period — a period risks being read as part of the link. Where there is no DOI, give the URL. Add a retrieval date only for content designed to change: a wiki, a live feed, a page that is rewritten in place. A missing publication date does not by itself call for one; that case takes `(n.d.)` instead.

Block a quotation of forty words or more: indent it, drop the quotation marks, and put the citation after the final period.

Cite personal communications — interviews, emails, unrecorded lectures — in text alone: `(A. Ali, personal communication, August 14, 2025)`. They never enter the reference list, because the reader cannot retrieve them.

For education-policy staples, preserve the source type in brackets: data sets use `[Data set]`; dissertations and theses name the institution and database when retrievable; conference papers, technical reports, standards, and agency reports name the sponsoring body. When the agency and publisher are the same, do not repeat it as publisher. For a source known only through another source, cite `as cited in` in text and list only the work actually read.

For generative AI, current APA guidance puts the company in the author slot. Date a shareable conversation, give it a short descriptive title, and mark it `[Generative AI chat]`; mark the tool itself, when you cite it generally, `[Large language model]`. A private or non-retrievable exchange is a personal communication. AI used only as a search engine, or as routine software assistance, normally gets no reference entry; cite the underlying sources.

## Examples

**Publisher location and the old retrieval formula**

> Ali, N. (2024). *The unreliable archive*. New York, NY: Winslow Press. Retrieved from https://example.org/archive

> Ali, N. (2024). *The unreliable archive*. Winslow Press. https://example.org/archive

**Ampersand on the wrong side of the parenthesis**

> Ali & Moreau (2024) found the opposite, and the effect held (Ali and Moreau, 2024).

> Ali and Moreau (2024) found the opposite, and the effect held (Ali & Moreau, 2024).

**Naming three authors in full**

> Ali, Moreau, and Okonkwo (2024) reported that the provenance was unresolved.

> Ali et al. (2024) reported that the provenance was unresolved.

**Title case in a reference-list entry**

> Ali, N., Moreau, C., & Okonkwo, I. (2024). The Provenance Of Municipal Archives. *Winslow Quarterly, 12*(3), 225–250.

> Ali, N., Moreau, C., & Okonkwo, I. (2024). The provenance of municipal archives. *Winslow Quarterly, 12*(3), 225–250.

**DOI form**

> ... *Winslow Quarterly, 12*(3), 225–250. doi:10.1234/wq.2024.12

> ... *Winslow Quarterly, 12*(3), 225–250. https://doi.org/10.1234/wq.2024.12

**Generative AI.** APA revised this in September 2025. The company that made the tool takes the author position — not the tool itself, which is the common error. A specific conversation is `[Generative AI chat]`, titled and dated, with a shareable link; the tool cited generally is `[Large language model]`. Where the exchange cannot be shared, it is a personal communication instead, cited in text only.

> ChatGPT. (2025, August 14). *Provenance of the Winslow archive* [Generative AI chat]. OpenAI. https://chatgpt.com/share/abcd-1234

> OpenAI. (2025, August 14). *Provenance of the Winslow archive* [Generative AI chat]. ChatGPT. https://chatgpt.com/share/abcd-1234

**The tool itself rather than one session**

> ChatGPT. (2025). *OpenAI* [Large language model]. https://chatgpt.com

> OpenAI. (2025). *ChatGPT* [Large language model]. https://chatgpt.com
