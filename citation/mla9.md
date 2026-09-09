---
id: citation.mla9
layer: citation
version: 1.1.0
status: draft
budget: 1240
tokens: 1240
edition: "9th (2021); selected public August 2025 AI guidance checked September 8, 2026"
evidence:
  - sources/citation-authority.md
---

# Citation: MLA 9

Use this adapter where formal MLA citations are requested, subject to the venue's adopted edition and requirements. Preserve the source actually used, including its type, author, edition and locators. Missing metadata is not permission to invent it. The source dossier identifies the public guidance checked; it does not certify every handbook entry or prove that a cited source was consulted.

## Detect

- **A comma between author and bare page.** `(Ali, 42)`. Author and page sit together unpunctuated. A comma *is* correct before a shortened title, `(Ali, "Archive" 42)`, and before a labeled locator, `(Ali, par. 4)` — do not strip those.
- **A comma before a bare timestamp.** `(Ali, 00:12:04)`. Use the comma before a named locator label such as `par.` or `sec.`, not before a timestamp that functions like a page number.
- **`p.` inside the parentheses.** `(Ali p. 42)`. The abbreviation belongs in Works Cited, not in the text.
- **Missing `p.`/`pp.` in Works Cited**, where it is required.
- **URL presentation inconsistent with the requested format.** The working MLA form here omits the protocol in ordinary URL display text but retains it for a DOI. Keep functioning link destinations when the medium requires clickable links.
- **Uncompressed page ranges.** `pp. 225-250` where MLA elides to `pp. 225-50`.
- **Format labels standing in for containers.** *Web article*, *PDF*, *online journal*. MLA wants the container — the larger work the source sits inside.
- **Sentence case on a title.** MLA keeps title case throughout.
- **The author named twice**, once in the sentence and again in the parentheses.
- **A Works Cited list out of alphabetical order**, or holding works never cited in the text.
- **An invented access date**, or the deletion of a venue-required one. An optional access date is not inherently an error.
- **A trailing period after a block-quote citation.** Inline citations precede the period; block citations follow it and end bare.

## Write

With supplied pagination, put author and page together: `(Ali 42)`. Name the author in the sentence and the parentheses carry the page alone: `Ali argues ... (42)`. Where two sources share an author, a shortened title separates them: `(Ali, "Archive" 42)`. For an unpaginated source, use an available source-supplied locator when appropriate; do not manufacture pages or hand-count paragraphs to force one. If no suitable locator exists, cite the work without inventing one. Check the applicable label form for the medium. A supplied timestamp can function like a page number: `(Ali 00:12:04)`.

Build entries from the nine core elements, in order, skipping those that do not apply: author, title of source, title of container, other contributors, version, number, publisher, publication date, location. Distinguish an inapplicable field from an applicable one whose value is unknown; flag the latter instead of pretending the record is complete. A source nested in two containers — an article in a journal in a database — repeats the applicable container elements.

```
Author. "Title of Source." Title of Container, Other contributors, Version,
    Number, Publisher, Publication date, Location.
```

Punctuate by position, not by source type: period after the author, period after the title of the source, commas between the container's elements, period at the end. That single pattern replaces the format-specific recipes of earlier editions.

Italicize the title of a container and of any work that stands on its own — a journal, a book, a website, a film, a database, a generative-AI tool. Put the title of a part inside a container in quotation marks: an article, a chapter, a poem, an episode. The two marks are how a reader tells the levels of the container apart, so a container left roman collapses the structure the whole system is built on.

Head the list `Works Cited`. Alphabetize by surname; hanging indent. Use `p.` for one page and `pp.` for a range, dropping the repeated leading digits of the second number and keeping at least two of them — `pp. 225-50`, but `pp. 100-10` and `pp. 96-102`. Prefer a DOI; then a permalink; then a URL with the protocol removed.

Block prose running more than four lines and verse running more than three: indented, no quotation marks, citation after the closing period with no period of its own.

For literary texts, use shared divisions when the actual source provides them: act.scene.line numbers for plays, line numbers for poems, or suitable book, canto, chapter or section identifiers. Preserve a supplied page locator when no supported alternative is available. For editions, translations and anthology pieces, cite the work actually used, naming editors or translators where applicable; do not silently substitute another edition's locations.

Prefer repeating an author's name for accessibility as a house choice where the venue permits it. The claimed retirement of repeated-author dashes was not independently verified here; follow the actual adopted rule rather than declaring a compliant bibliography obsolete.

The public August 2025 AI guidance does not put the tool in the author element. Describe the generated material in the source-title element, name the tool as container, the actual model in the version element, the provider as publisher and the generation date. Prefer a stable, shareable URL; the public fallback to a tool URL applies when the tool lacks that feature. Do not invent a share link or expose a private conversation without permission; resolve restricted-record handling with the venue. Consult and cite underlying sources directly when relying on them, rather than implying that an AI summary establishes their contents. Citation does not replace required disclosure of substantial assistance.

## Examples

**Comma inside the citation**

**Supplied facts:** The fictional source is by Ali, and the supplied passage is on page 42. No shortened title is needed.

> (Ali, p. 42)

> (Ali 42)

**Comma that belongs — shortened title, and a labeled locator**

**Supplied facts:** The first fictional citation needs the shortened title `Archive` and page 42. The second source explicitly numbers its paragraphs, and the supplied passage is paragraph 4. No paragraph count is inferred.

> (Ali "Archive" 42) and (Ali par. 4)

> (Ali, "Archive" 42) and (Ali, par. 4)

**Timestamp without a comma**

**Supplied facts:** The fictional recording is credited to Ali and the supplied passage begins at timestamp 00:12:04. Preserve that timestamp.

> (Ali, 00:12:04)

> (Ali 00:12:04)

**Author already named in the sentence**

**Supplied facts:** Ali makes the stated argument on page 42 of the fictional source. The author is already named in the sentence and no other work creates ambiguity.

> Ali argues the archive is unreliable (Ali 42).

> Ali argues the archive is unreliable (42).

**Container and page formatting without invented metadata**

**Supplied facts:** The fictional journal article is by Nadia Ali, titled "The Unreliable Archive," in Winslow Quarterly, dated 2024, on pages 225-250, with the URL shown. No volume or issue number is supplied. The venue requests the ordinary URL display and page-range forms below.

> Ali, Nadia. "The Unreliable Archive." Web article, *Winslow Quarterly*, 2024, pp. 225-250, https://example.org/archive.

> Ali, Nadia. "The Unreliable Archive." *Winslow Quarterly*, 2024, pp. 225-50, example.org/archive.

Review note: check whether the actual record has volume and issue fields. Do not invent them to make this incomplete record look finished.

**A DOI keeps its protocol**

**Supplied facts:** The supplied illustrative DOI is `10.1234/wq.2024.12`; the volume, issue, year and pages shown are part of this separate synthetic record. The ellipsis stands for an unchanged prefix.

> ... vol. 12, no. 3, 2024, pp. 225-50, doi.org/10.1234/wq.2024.12.

> ... vol. 12, no. 3, 2024, pp. 225-50, https://doi.org/10.1234/wq.2024.12.

**Literary divisions only when supplied**

**Supplied facts:** The fictional passage gives the quoted words exactly and locates them on page 88 of the edition used. No act, scene or line numbers are provided. The task is a citation check, not a change of edition.

> Moreau's envoy admits kinship "too late for mercy" (88).

> Moreau's envoy admits kinship "too late for mercy" (88).

No change: the supplied page is a valid location; a more elaborate locator would be invented.

**Generative AI with incomplete metadata**

**Supplied facts:** The record identifies only ChatGPT, OpenAI and the year 2025. It supplies no prompt or generated-material description, model, exact generation date or shareable URL.

> ChatGPT. OpenAI, 2025.

> Citation incomplete: retain the known tool, provider and year, but obtain the actual generated-material description, model, generation date and appropriate location before completing the entry. Do not invent a prompt or share link.
