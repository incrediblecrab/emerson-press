---
id: citation.chicago18
layer: citation
version: 1.1.0
status: draft
budget: 1316
tokens: 1316
edition: 18th (Sept. 2024)
evidence:
  - tests/sources/citation-authority.md
---

# Citation: Chicago 18

Use this adapter where formal Chicago citations are requested, subject to the venue's selected system and adopted rules. Preserve source identity and supplied bibliographic fields; incomplete records stay visibly incomplete. Selected public guidance was checked, not every rule in the full manual. The source dossier identifies that scope; formatting alone does not establish retrieval or support.

## Detect

- **The two systems mixed.** Notes-bibliography and author-date are alternatives, not a menu. A superscript note beside a `(Ali 2024)` parenthetical means the document has not chosen.
- **A modern book citation called incomplete solely because it lacks a publication place.** Place is no longer required; its presence is not automatically an error.
- **A repeated-author convention changed without checking the venue.** This adapter prefers repeated names for readability, not automatic rejection of every dash-form entry.
- **Author counts copied from a different edition or citation context.** The public journal-article guidance names up to six in a bibliography and up to two in a note or author-date in-text citation.
- **Three authors spelled out in a note.** That was the old rule. Three is already `et al.` territory.
- **`Ibid.` with an unclear referent.** A shortened note is a useful default, but an unambiguous, venue-accepted `Ibid.` is not itself an error.
- **A full note repeated** where a shortened note belongs.
- **An invented access date**, or a claim that a source was consulted when it was not.
- **A bare `doi:` prefix.** Chicago takes `https://doi.org/`.
- **A missing final period after a URL or DOI.** Chicago's examples close the citation with ordinary terminal punctuation.
- **A page range demanded on a chapter in an edited book.** It is no longer required in a bibliography; a journal article normally gives its whole page range or article identifier when applicable.
- **`headline style` or `sentence style`.** Renamed to title case and sentence case.
- **A four-letter preposition capitalized in a title.** The cutoff moved: five letters and up now capitalize.
- **A periodical's official `The` mishandled.** In running text, keep and capitalize it when it is part of the masthead; in citations, it may be omitted.
- **`self-published` or a retail platform as publisher.** Prefer `published by the author`; do not cite Amazon merely as the distribution platform.
- **Humanities sources flattened into book form.** Archives, manuscripts, letters, interviews, translations, multivolume works, reprints, exhibition catalogs, dissertations, scores and recordings need their own Chicago patterns.

## Write

Choose a system first. Notes-bibliography suits history, literature and the arts: a superscript numeral in the text, a note carrying the citation, and usually a bibliography behind it. Author-date suits the sciences and social sciences: `(Ali 2024, 42)` in the text against a reference list.

In the ordinary notes system, give a full first citation and shortened later notes — author's surname, shortened title and relevant locator. Follow a venue's explicitly different arrangement.

```
1. Firstname Lastname, Title of Book (Publisher, Year), page.
2. Lastname, Shortened Title, page.
```

Notes and bibliography entries identify the same source but can differ in author counts and locator scope as well as punctuation. A journal-article note points to the cited pages; its bibliography entry normally gives the whole article's page range or article identifier. Notes run on commas with the publication facts in parentheses; bibliography entries break on periods and drop the parentheses. Invert a Western-order first author's name for alphabetizing, but preserve names whose convention already places the family name first.

```
Lastname, Firstname. Title of Book. Publisher, Year.
```

Count authors by context. The public journal-article models name up to six in the bibliography or reference list; at seven or more they give the first three and `et al.` A note or author-date in-text citation names up to two; at three or more it gives the first and `et al.` Check the relevant entry for unusual source types and exceptions.

Give the publisher and year for an ordinary modern book; publication place is not required, rather than categorically forbidden. For books published before 1900, consult the applicable place-instead-of-publisher model. Use title case for English titles, italics for whole works and quotation marks for parts. The working title-case convention here capitalizes prepositions of five letters or more; check the adopted rule before enforcing an exception. In running text, preserve a periodical's official leading `The`; source-specific citation models may omit it.

For a source consulted online, prefer an established DOI in resolver form or another appropriate stable URL, and close the citation with a final period. The public web-page model calls for an actual access date when no publication or revision date is given. A venue may impose additional requirements. Do not invent any date or archive link.

Use block quotation treatment for longer extracts when the applicable manual or venue calls for it. The word and line thresholds were not verified in this review; do not present a single universal cutoff as established. Preserve the quoted text and apply the selected system's citation placement.

Prefer repeating an author's name in consecutive bibliography entries as this adapter's accessible working default. If the venue adopts a dash convention, follow it; this preference is not a reason to label every older bibliography wrong.

For self-published books, use `published by the author` in bibliography form and `pub. by author` in a note. For archival and manuscript material, lead with the item and date, then name the collection, box or folder when useful, and repository; do not pretend it is a published book. For translations, editions, reprints, multivolume works, dissertations, interviews, scores, recordings and exhibition catalogs, choose the matching Chicago model before smoothing the prose.

For AI output, establish what was generated, by which tool, when, and whether a real retrievable record exists. Current AI-specific details were not verified from the full manual here; do not import APA or MLA's author/container rules as Chicago's. Check the applicable citation and disclosure policy, and do not invent a share URL or make a private exchange public without permission.

## Examples

**Optional publication place**

**Supplied facts:** This fictional modern book has the author, title, publisher, city and year shown. The venue requests the shorter public Chicago 18 book model. Omitting the city meets that request; a city is not inherently false or forbidden.

> Ali, Nadia. *The Unreliable Archive*. Chicago: Winslow Press, 2024.

> Ali, Nadia. *The Unreliable Archive*. Winslow Press, 2024.

**Author count in a note — the threshold is now two**

**Supplied facts:** The fictional book has the three named authors in that order, the publisher and year shown, and a cited passage on page 42. For this exercise the venue explicitly applies the first-author-plus-`et al.` note form.

> 1. Nadia Ali, Claire Moreau, and Ifeoma Okonkwo, *The Unreliable Archive* (Winslow Press, 2024), 42.

> 1. Nadia Ali et al., *The Unreliable Archive* (Winslow Press, 2024), 42.

**A repeated full note**

**Supplied facts:** Notes 4 and 5 refer to the same fictional book by Nadia Ali. Page 42 and page 96 are both supplied locators, and no other work makes the shortened title ambiguous.

> 4. Nadia Ali, *The Unreliable Archive* (Winslow Press, 2024), 42. 5. Nadia Ali, *The Unreliable Archive* (Winslow Press, 2024), 96.

> 4. Nadia Ali, *The Unreliable Archive* (Winslow Press, 2024), 42. 5. Ali, *Unreliable Archive*, 96.

**Repeating an author's name**

**Supplied facts:** Nadia Ali wrote both fictional books, with the titles, publisher and dates shown. The task requests this adapter's repeated-name preference while preserving the supplied entry order.

> Ali, Nadia. *The Unreliable Archive*. Winslow Press, 2024. ———. *Provenance and Its Discontents*. Winslow Press, 2019.

> Ali, Nadia. *The Unreliable Archive*. Winslow Press, 2024. Ali, Nadia. *Provenance and Its Discontents*. Winslow Press, 2019.

**Title case cutoff**

**Supplied facts:** These are fictional English titles, not quoted typography or titles in another language. The exercise explicitly requests the working convention that lowercases the four-letter preposition `with` and capitalizes the five-letter preposition `about`.

> *A Season With the Cartographers* and *Notes about the Winslow Archive*

> *A Season with the Cartographers* and *Notes About the Winslow Archive*

**Generative AI with an unverified public record**

**Supplied facts:** The record supplies ChatGPT, OpenAI, the quoted prompt and August 14, 2025. The URL below is a placeholder, not an actual share link. No permission to publish the conversation or source text establishing the current Chicago AI format is supplied.

> 1. OpenAI, response to "Describe the provenance of the Winslow archive," August 14, 2025, https://chatgpt.com/share/abcd-1234.

> Citation incomplete: remove the placeholder URL and preserve the known tool, provider, prompt and date in the editing record. Confirm the applicable Chicago/venue treatment before completing the citation; do not manufacture a publicly retrievable exchange.
