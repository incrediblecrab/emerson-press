---
id: core.formatting
layer: core
version: 1.4.0
status: draft
budget: 818
tokens: 818
evidence:
  - sources/signs-of-ai-writing.md
  - sources/field-guide-to-ai-slop.md
  - sources/ap-stylebook.md
  - sources/kill-ai-slop.md
  - sources/wida-curriculum.md
---

# Formatting

Formatting should help this reader find and understand the content. Decorative structure can conceal a thin argument, but a list, table or heading is not a defect merely because models also use it. Claims about how training produced a particular habit belong in the evidence dossier, with their limitations.

Punctuation has one job, which is to make the thought clear. A mark that does not do that job comes out.

## Detect

### Structure standing in for content

- **Inline-header bullets.** `- **Thing:** description`, repeated down the page. The signature list shape of chatbot output.
- **Bold as emphasis spray** — scattered mid-paragraph, or every instance of one term bolded, or a `Key takeaways` block.
- **Lists where prose belongs**, especially three items that each need a sentence of explanation.
- **Non-parallel list items** — a noun phrase, then a full sentence, then a question.
- **Tables that add no useful comparison**, rather than tables below an arbitrary row count.
- **Section headings with no prose between them.**

A reference list — a taxonomy, an index, a glossary, where each item is a distinct named thing — is not this tell. The fault is a list standing in for prose that had a throughline, not a genuine enumeration of discrete items.

### Markup tells

- **Heading capitalization inconsistent with the selected venue.**
- **A document starting at `###`,** skipping the level above.
- **Horizontal rules before every heading.**
- **Emoji as bullet markers or heading decoration.**
- **Unicode standing in for markup** — mathematical alphabets used to fake bold or italic text. A meaningful mathematical symbol is not decorative markup.
- **Curly quotes mixed with straight ones** in the same passage.
- **Unresolved tool artifacts** left in text: `oaicite`, `turn0search0`, `[cite: 1]`, `grok_card`, `2025-xx-xx` placeholder dates, unfilled bracketed slots. Working footnote links and required disclosure are not artifacts to remove.

### Punctuation

- **Em dash as default connector,** where a different mark would make the relation clearer. Spacing follows the selected style.
- **Parentheses holding what the sentence could not fit.** The reach for them signals a contorted sentence, not a need for brackets.
- **A colon stacked with a dash.**
- **Semicolons joining independent clauses** that wanted to be two sentences.
- **Scare quotes around ordinary words.**
- **Hyphen pileups** — if the count is getting daunting, rebuild the phrase.

### Chat register

- Assistant speech surviving into the document: `Certainly!`, `I hope this helps`, `Would you like me to`, `Here's a breakdown`, `let me know`.
- A section announcing what it is about to do before doing it.

## Write

Choose paragraphs for a throughline and lists for steps or parallel items a reader needs to scan. Keep list items grammatically parallel. Three real items do not become a fault because they need explanation.

Use consistent heading levels and descriptive headings. Sentence case is the house default, not an override of a venue's conventions. Use emphasis to identify what matters rather than making every keyword bold.

Use a table when its rows and columns make a relationship easier to compare. A small table can be useful; a larger table can still be padding.

Use consistent quotation typography appropriate to the medium. Straight quotes are the plain-text default. Keep meaningful notation and accessible links. Avoid decorative symbols that obstruct reading or substitute for structure.

Rebuild a confusing sentence rather than patching it with more punctuation. Preserve a useful parenthesis, dash or semicolon when it clarifies the relationship. The test is comprehension, not a punctuation count.

Remove unfinished placeholders, assistant chatter and unresolved tool tokens from publication-ready text. Preserve valid citations, attribution, accessibility features and required AI disclosure. Do not disguise provenance that the venue requires.

## Examples

**Inline-header bullets that should be prose**

**Supplied facts:** A fictional project plan gives the Medford-Ashfield route, phase 3 at 40% completion, a 2027 target and a projected journey-time reduction of 20-30%. The projection is not an observed result.

> **Route details:** The line starts at Medford and ends at Ashfield. **Timeline:** Phase 3 is 40% complete, with completion targeted for 2027. **Impact:** Journey times will fall by 20-30%.

> The line runs from Medford to Ashfield. Phase 3 is 40% complete, with completion targeted for 2027. The plan projects journeys 20-30% shorter after it opens.

**Bold spray**

**Supplied facts:** The definition in this exercise is a purchase financed mostly with debt. No claim about the buyer's total financial risk is supplied.

> A **leveraged buyout** relies on the **extensive use of debt**, which lets a firm **take control of a business** while committing **very little equity** of its own.

> A leveraged buyout finances most of the purchase price with borrowed money.

**Non-parallel list**

**Supplied facts:** These are three separate agenda items. The mobile item is an open question, not an approved redesign.

> - Reduce onboarding time
> - Documentation should be rewritten
> - What about the mobile flow?

> - Reduce onboarding time
> - Rewrite the documentation
> - Decide whether to change the mobile flow

**Table that wants to be a sentence**

**Supplied facts:** The source estimates the fictional market's 2024 size at about $2.1 billion.

> | Metric | Figure | | --- | --- | | Market size, 2024 | about $2.1bn |

> The market's estimated size was about $2.1 billion in 2024.

**Dash as default connector**

**Supplied facts:** The report was released Tuesday and found rising costs. No magnitude was supplied.

> The report — which was released Tuesday — found — among other things — that costs had risen.

> The report, released Tuesday, found that costs had risen.

**Parentheses propping up a sentence**

**Supplied facts:** The grant was awarded in 2021, the program's second year, and funded three positions. Payment arrived in January, but the payment year is not supplied.

> The grant (awarded in 2021, the program's second year, though the money did not arrive until January) funded three positions.

> The grant was awarded in 2021, the program's second year, but the money did not arrive until January. It funded three positions.
