---
id: core.formatting
layer: core
version: 1.3.0
status: draft
budget: 847
tokens: 847
evidence:
  - sources/signs-of-ai-writing.md
  - sources/field-guide-to-ai-slop.md
  - sources/ap-stylebook.md
  - sources/kill-ai-slop.md
  - sources/wida-curriculum.md
---

# Formatting

Models overproduce structure for a traceable reason: human raters scored bullet-heavy answers higher because those answers looked organized, and preference tuning locked the habit in. Bold came by a different road, out of readmes, decks, listicles, and sales copy. The pull toward structure is therefore strongest exactly where the material is thinnest. Treat a sudden outbreak of formatting as a signal to check whether the writer said anything.

Punctuation has one job, which is to make the thought clear. A mark that does not do that job comes out.

## Detect

### Structure standing in for content

- **Inline-header bullets.** `- **Thing:** description`, repeated down the page. The signature list shape of chatbot output.
- **Bold as emphasis spray** — scattered mid-paragraph, or every instance of one term bolded, or a `Key takeaways` block.
- **Lists where prose belongs**, especially three items that each need a sentence of explanation.
- **Non-parallel list items** — a noun phrase, then a full sentence, then a question.
- **Two-row tables**, or a table with one real column.
- **Section headings with no prose between them.**

A reference list — a taxonomy, an index, a glossary, where each item is a distinct named thing — is not this tell. The fault is a list standing in for prose that had a throughline, not a genuine enumeration of discrete items.

### Markup tells

- **Title Case Headings.**
- **A document starting at `###`,** skipping the level above.
- **Horizontal rules before every heading.**
- **Emoji as bullet markers or heading decoration.**
- **Unicode standing in for markup** — mathematical bold or italic characters, decorative arrows, `×` for multiplication.
- **Curly quotes mixed with straight ones** in the same passage.
- **Provenance artifacts** left in text: `oaicite`, `turn0search0`, `[cite: 1]`, `grok_card`, `↩` around footnotes, `2025-xx-xx` placeholder dates, unfilled bracketed slots.

### Punctuation

- **Em dash as default connector,** where a comma or a period was the honest mark. Spaced dashes throughout.
- **Parentheses holding what the sentence could not fit.** The reach for them signals a contorted sentence, not a need for brackets.
- **A colon stacked with a dash.**
- **Semicolons joining independent clauses** that wanted to be two sentences.
- **Scare quotes around ordinary words.**
- **Hyphen pileups** — if the count is getting daunting, rebuild the phrase.

### Chat register

- Assistant speech surviving into the document: `Certainly!`, `I hope this helps`, `Would you like me to`, `Here's a breakdown`, `let me know`.
- A section announcing what it is about to do before doing it.

## Write

Default to paragraphs. A list earns bullets when items are genuinely parallel — same part of speech, same voice, same tense — and when the reader will scan rather than read. Three items that each need explaining are a paragraph.

Sentence case headings, in order, with prose under each. Use bold sparingly — to define a term on first use, not to spray emphasis. How strictly to hold that, and where the edge cases fall, `restraint` decides.

Use a table only when rows and columns both earn their place: several rows, at least two columns carrying real data. If it holds a single comparison, it is a sentence.

Use straight quotes, keep emoji out of the structure, and do not let Unicode stand in for markup.

If a sentence leans on two dashes or a pair of parentheses to stand up, the construction failed earlier than the punctuation. Rebuild it rather than propping it up. The fault is the contortion, not the count. If it is cluttered with commas, semicolons, and dashes together, start it over.

Strip every artifact of how the text was produced before it reaches a reader.

## Examples

**Inline-header bullets that should be prose**

> **Route details:** The line starts at Medford and ends at Ashfield. **Timeline:** Phase 3 is 40% complete, with completion targeted for 2027. **Impact:** Journey times will fall by 20-30%.

> The line runs from Medford to Ashfield. Phase 3 is 40% complete and due in 2027; when it opens, the trip should be about a quarter shorter.

**Bold spray**

> A **leveraged buyout** relies on the **extensive use of debt**, which lets a firm **take control of a business** while committing **very little equity** of its own.

> In a leveraged buyout, the purchase is paid for mostly by borrowing, so the buyer risks little of its own money.

**Non-parallel list**

> - Reduce onboarding time
> - Documentation should be rewritten
> - What about the mobile flow?

> - Reduce onboarding time
> - Rewrite the documentation
> - Redesign the mobile flow

**Table that wants to be a sentence**

> | Metric | Figure | | --- | --- | | Market size, 2024 | about $2.1bn |

> The market was worth about $2.1 billion in 2024.

**Dash as default connector**

> The report — which was released Tuesday — found — among other things — that costs had risen.

> The report, released Tuesday, found that costs had risen.

**Parentheses propping up a sentence**

> The grant (awarded in 2021, the program's second year, though the money did not arrive until January) funded three positions.

> The grant was awarded in 2021 and paid out that January. It funded three positions.
