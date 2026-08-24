---
id: user-interface.accessibility
layer: user-interface
version: 1.0.1
status: draft
budget: 1218
tokens: 1218
kind: overlay
medium: assistive
mechanics: house
elements: [accessibility label, alt text, accessibility hint, link text, heading, form field, caption, transcript, announcement]
evidence:
  - sources/apple-hig.md
  - sources/kill-ai-slop.md
---

# Interface: Accessibility

Text a screen reader speaks is still copy, and it is usually the copy nobody edits. It is also the only version of the interface some readers get, which makes an unlabeled control a missing feature for them.

Cuts across every other module in this layer. Applies to an app, a web page, and a chart alike. Where this module and a medium module both cover a surface, this one decides what must be announced and the medium module decides the wording.

## Detect

- **An unlabeled control.** An icon-only button announced by its file name, or as *button*.
- A label naming the glyph rather than the action: *magnifier*, *three dots*.
- **Alt text opening with `Image of` or `Photo of`.** The reader already knows. A chart is the exception: name the chart type first, because the encoding carries meaning — `charts` holds that rule.
- Decorative images described anyway, or one alt text repeated across a set.
- **Link text that cannot stand alone.** *Click here*, *Read more*, *this page*, listed out of context by the dozen.
- A hint repeating the label instead of saying what happens next.
- Position or color as the instruction: *the button on the right*, *the items in red*.
- State that is only visual — selected, expanded, required, invalid — never announced.
- Emoji inside labels, which get spoken in full and at length.
- Text baked into an image, invisible to search, translation, and speech.
- Announcements that interrupt, repeat, or fire on every keystroke.
- *Captions*, *subtitles*, *audio description*, and *transcript* used interchangeably. They are four different things.
- **A person described by their diagnosis** — *the blind*, *wheelchair-bound*, *suffers from*, *normal users* — or a disability borrowed to name a bad quality: *tone-deaf*, *crippled by*, *blind spot*, *sanity check*.
- An accessibility statement that claims compliance in place of listing what is known to be broken.

## Write

Label every control with the action it performs, in the words the visible label would have used. *Search*, not *magnifier*.

Write the hint for what happens after, and only when it is not obvious. A short phrase, not a repeat of the label. Most controls need none.

Describe an image for the job it does on this screen. The same rule cuts both ways: on a staff list, *Amara Boateng, chief scientist*; in a maintenance report, *a corroded pipe joint, about 2 cm of scale*. Decorative images get an empty description so they are skipped.

Write link text that survives being read alone. WCAG requires only that purpose be recoverable from the surrounding context — 2.4.4, Level A; standing alone is 2.4.9, Level AAA. Write to the stricter rule anyway, because a screen reader user listing every link on a page has no surrounding context. Refer to things by name, never by where they sit or what color they are.

Announce state changes once, when they happen, in stable wording that is recognizable at speed.

Keep emoji and decorative symbols out of labels and headings. Put text in text: if a word matters, it cannot live inside an image.

Use the four terms precisely. Captions carry dialogue and meaningful sound for a viewer who cannot hear; subtitles translate dialogue for one who can; audio description narrates what is only visible; a transcript is the whole thing as a document.

Write about people first and the disability second, and only where it is relevant — but follow a community's stated preference over the general rule, which is `domain/medical.md`'s call and stands: *autistic person*, *Deaf person*. Say what a person uses or does, not what they lack. Never reach for a disability as a metaphor for a flaw.

## Surfaces

**Structure.** Headings are the navigation. Write them as a real outline — one `h1`, no skipped levels — because a screen reader user lists them to decide where to go. Give every page, view, and window a name that identifies it in a list of twenty.

**Forms and errors.** Tie the label to the field so the field announces its own name. Announce required, invalid, and character-limit state in text, not in color or an asterisk alone. On failure, say how many fields need attention and name them, then move focus to the first one.

**Media.** Caption meaningful sound, not just speech: *[door slams]* changes the scene. Name who is speaking when more than one person is. Offer a transcript for anything long, since reading is faster than scrubbing.

**Charts and tables.** Give the finding, the range, and the outlier in a sentence, then link the table; `charts` holds the wording. Never encode a category in color alone. Write table headers as headers, so a cell can be announced with the row and column it belongs to.

**Plain language.** Cognitive accessibility is a writing problem more than a markup one. Short sentences, the common word, one idea per paragraph, the instruction before the caveat. Expand an abbreviation the first time. Give a timeout a way to extend, and say so in words.

**Accessibility statements.** Name what works, what does not, the standard you are measuring against, and where to report a problem. Vagueness here is the tell that nobody tested.

## Boundaries

The text assistive technology reads, on any surface in any medium. This module loads alongside a medium module and never instead of one.

Non-text accessibility — contrast, target size, focus order, motion — is outside it. Those are real requirements and this module does not cover them.

## Examples

**Icon button labeled by its glyph**

> label: `icon-dots-vertical`

> label: `More options`

**Alt text describing itself**

> Image of a chart showing data about our quarterly performance.

> Bar chart. Revenue by quarter, 2024–2026. Flat until Q3 2025, then rising to $4.2M.

**Link text that can't stand alone**

> To see our security practices, click here. For our data retention policy, click here.

> Read our security practices. See how long we keep data.

**Hint repeating the label**

> label: `Delete` &nbsp; hint: `Deletes the item`

> label: `Delete` &nbsp; hint: `Moves this note to Recently Deleted`

**Instruction by position and color**

> Tap the blue button in the top right, then fix the fields shown in red.

> Tap Publish. Two fields need attention: Title and Publish date.

**Emoji in a label**

> label: `🚀 Launch`

> label: `Launch`

**A person described by their diagnosis**

> Our app is designed for the blind and for wheelchair-bound users who suffer from limited mobility.

> Kestrel works with VoiceOver, and every action has a keyboard equivalent.

**An accessibility statement that claims instead of tells**

> Kestrel is fully accessible and committed to inclusion for all users.

> Kestrel targets WCAG 2.2 AA. The editor and settings meet it. The chart view does not yet expose data to VoiceOver; a table alternative shipped in July, and audio graphs are planned for the autumn release. Report a problem at access@kestrel.app.

**Form error that says nothing to a screen reader**

> ⚠ (two fields turn red)

> 2 fields need attention: Email and Publish date. Focus moves to Email. "Email — enter an address in the form name@example.com."
