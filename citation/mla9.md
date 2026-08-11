---
id: citation.mla9
layer: citation
version: 1.0.0
status: draft
budget: 1025
tokens: 1025
edition: 9th (2021); AI guidance updated Aug. 2025, modified Oct. 2025
---

# Citation: MLA 9

## Detect

- **A comma between author and bare page.** `(Ali, 42)`. Author and page sit together unpunctuated. A comma *is* correct before a shortened title, `(Ali, "Archive" 42)`, and before a labeled locator, `(Ali, par. 4)` — do not strip those.
- **A comma before a bare timestamp.** `(Ali, 00:12:04)`. Use the comma before a named locator label such as `par.` or `sec.`, not before a timestamp that functions like a page number.
- **`p.` inside the parentheses.** `(Ali p. 42)`. The abbreviation belongs in Works Cited, not in the text.
- **Missing `p.`/`pp.` in Works Cited**, where it is required.
- **A protocol on a plain URL.** MLA strips `https://` from a bare URL — but keeps it on a DOI, which stays `https://doi.org/10.xxxx`.
- **Uncompressed page ranges.** `pp. 225-250` where MLA elides to `pp. 225-50`.
- **Format labels standing in for containers.** *Web article*, *PDF*, *online journal*. MLA wants the container — the larger work the source sits inside.
- **Sentence case on a title.** MLA keeps title case throughout.
- **The author named twice**, once in the sentence and again in the parentheses.
- **A Works Cited list out of alphabetical order**, or holding works never cited in the text.
- **An access date on a stable, dated source.**
- **A trailing period after a block-quote citation.** Inline citations precede the period; block citations follow it and end bare.

## Write

Author and page, nothing between: `(Ali 42)`. Name the author in the sentence and the parentheses carry the page alone: `Ali argues ... (42)`. Where two sources share an author, a shortened title separates them, and there the comma returns: `(Ali, "Archive" 42)`. Sources without pages take a labeled locator — `par.`, `ch.`, `sec.` — after a comma. A timestamp is a locator too, but it is not a label: use `(Ali 00:12:04)`, not `(Ali, 00:12:04)`.

Build every entry from the nine core elements, in order, skipping any that do not apply: author, title of source, title of container, other contributors, version, number, publisher, publication date, location. A source nested in two containers — an article in a journal in a database — runs the template again from the third element for the second container, filling only the slots that apply, which is usually a title and a location.

```
Author. "Title of Source." Title of Container, Other contributors, Version,
    Number, Publisher, Publication date, Location.
```

Punctuate by position, not by source type: period after the author, period after the title of the source, commas between the container's elements, period at the end. That single pattern replaces the format-specific recipes of earlier editions.

Italicize the title of a container and of any work that stands on its own — a journal, a book, a website, a film, a database, a generative-AI tool. Put the title of a part inside a container in quotation marks: an article, a chapter, a poem, an episode. The two marks are how a reader tells the levels of the container apart, so a container left roman collapses the structure the whole system is built on.

Head the list `Works Cited`. Alphabetize by surname; hanging indent. Use `p.` for one page and `pp.` for a range, dropping the repeated leading digits of the second number and keeping at least two of them — `pp. 225-50`, but `pp. 100-10` and `pp. 96-102`. Prefer a DOI; then a permalink; then a URL with the protocol removed.

Block prose running more than four lines and verse running more than three: indented, no quotation marks, citation after the closing period with no period of its own.

For literary texts, prefer the divisions scholars can share across editions: act.scene.line numbers for plays when supplied; line numbers for poems, with `line` or `lines` in the first citation; book, canto, chapter, or section for long works. For editions, translations, and anthology pieces, cite the work you actually used, naming editors or translators in the contributor slot when their work matters.

For repeated authors MLA has long used three unspaced hyphens, or three em dashes, in place of the repeated name. MLA is retiring that convention for screen-reader accessibility; both the dashes and the repeated name are currently acceptable. Prefer repeating the name.

## Examples

**Comma inside the citation**

> (Ali, p. 42)

> (Ali 42)

**Comma that belongs — shortened title, and a labeled locator**

> (Ali "Archive" 42) and (Ali par. 4)

> (Ali, "Archive" 42) and (Ali, par. 4)

**Timestamp without a comma**

> (Ali, 00:12:04)

> (Ali 00:12:04)

**Author already named in the sentence**

> Ali argues the archive is unreliable (Ali 42).

> Ali argues the archive is unreliable (42).

**Format label instead of a container; unstripped URL; unelided pages**

> Ali, Nadia. "The Unreliable Archive." Web article, *Winslow Quarterly*, 2024, pp. 225-250, https://example.org/archive.

> Ali, Nadia. "The Unreliable Archive." *Winslow Quarterly*, vol. 12, no. 3, 2024, pp. 225-50, example.org/archive.

**A DOI keeps its protocol**

> ... vol. 12, no. 3, 2024, pp. 225-50, doi.org/10.1234/wq.2024.12.

> ... vol. 12, no. 3, 2024, pp. 225-50, https://doi.org/10.1234/wq.2024.12.

**Literary divisions over edition-only pages**

> Moreau's envoy admits kinship "too late for mercy" (88).

> Moreau's envoy admits kinship "too late for mercy" (3.2.41-46).

**Generative AI.** No author element. The prompt becomes the title, followed by the word *prompt* outside the closing quotation mark; the tool is the container; the model goes in the version slot as `model GPT-4o`. Prefer a stable shareable link.

> ChatGPT. OpenAI, 2025.

> "Describe the provenance of the Winslow archive" prompt. *ChatGPT*, model GPT-4o, OpenAI, 14 Aug. 2025, chatgpt.com/share/abcd-1234.
