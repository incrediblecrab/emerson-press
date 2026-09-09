---
id: user-interface.accessibility
layer: user-interface
version: 1.1.0
status: draft
budget: 1323
tokens: 1323
kind: overlay
medium: assistive
mechanics: house
elements: [accessibility label, alt text, accessibility hint, link text, heading, form field, caption, transcript, announcement]
evidence:
  - tests/sources/apple-hig.md
  - tests/sources/kill-ai-slop.md
---

# Interface: Accessibility

Text a screen reader speaks is still copy, and it is usually the copy nobody edits. It is also the only version of the interface some readers get, which makes an unlabeled control a missing feature for them.

Cuts across every other module in this layer. Applies to an app, a web page, and a chart alike. Where this module and a medium module both cover a surface, this one decides what must be announced and the medium module decides the wording.

## Detect

- **An unlabeled control.** An icon-only button announced by its file name, or as *button*.
- A label naming the glyph rather than the action: *magnifier*, *three dots*.
- **Redundant alt text opening with `Image of` or `Photo of`.** Usually the role already supplies this information. Name the medium when it matters to the purpose, including a chart type when that helps explain the encoding.
- Decorative images described anyway, or one alt text repeated across a set.
- **Link text that cannot stand alone.** *Click here*, *Read more*, *this page*, listed out of context by the dozen.
- A hint repeating the label instead of saying what happens next.
- Position or color as the instruction: *the button on the right*, *the items in red*.
- State that is only visual — selected, expanded, required, invalid — never announced.
- Emoji inside labels, which get spoken in full and at length.
- Text baked into an image, invisible to search, translation, and speech.
- Announcements that interrupt, repeat, or fire on every keystroke.
- Media tracks whose labels conceal what they provide: dialogue alone, speech and meaningful sounds, visual description, or a text equivalent.
- **A person described by their diagnosis** — *the blind*, *wheelchair-bound*, *suffers from*, *normal users* — or a disability borrowed to name a bad quality: *tone-deaf*, *crippled by*, *blind spot*, *sanity check*.
- An accessibility statement that claims compliance in place of listing what is known to be broken.

## Write

Label every control with the action it performs, in the words the visible label would have used. *Search*, not *magnifier*.

Write the hint for what happens after, and only when it is not obvious. A short phrase, not a repeat of the label. Most controls need none.

Describe an image for the job it does on this screen. The same rule cuts both ways: on a staff list, *Amara Boateng, chief scientist*; in a maintenance report, *a corroded pipe joint, about 2 cm of scale*. Decorative images get an empty description so they are skipped.

Write link text that survives being read alone. WCAG requires only that purpose be recoverable from the surrounding context — 2.4.4, Level A; standing alone is 2.4.9, Level AAA. Write to the stricter rule anyway, because a screen reader user listing every link on a page has no surrounding context. Refer to things by name, never by where they sit or what color they are.

Announce state changes once, when they happen, in stable wording that is recognizable at speed.

Keep emoji and decorative symbols out of labels and headings. Put text in text: if a word matters, it cannot live inside an image.

Describe the actual media alternative. Captions include dialogue and meaningful sounds; dialogue-only translation is not an equivalent substitute. The word *subtitles* is used differently across services, including for deaf and hard-of-hearing audiences, so identify what the track contains. Audio description narrates relevant visual content. A transcript provides a text version and needs relevant visual information when a complete alternative is promised.

Write about people first and the disability second, and only where it is relevant — but follow a community's stated preference over the general rule, which is `domains/medical.md`'s call and stands: *autistic person*, *Deaf person*. Say what a person uses or does, not what they lack. Never reach for a disability as a metaphor for a flaw.

## Surfaces

**Structure.** Headings are navigation. Use a coherent hierarchy, with a clear page heading and meaningful section levels; do not present a house preference for one `h1` as the complete WCAG requirement. Give every page, view and window a name that identifies it out of context.

**Forms and errors.** Supply persistent labels, required/invalid state and useful limit messages. Do not rely on color or an asterisk alone. On failure, provide a summary naming the affected fields and messages that explain each fix. Label associations, announcements and appropriate focus handling are implementation requirements; flag missing behavior separately instead of claiming a wording change implements it.

**Media.** Caption meaningful sound, not just speech: *[door slams]* changes the scene. Name who is speaking when more than one person is. Offer a transcript for anything long, since reading is faster than scrubbing.

**Charts and tables.** Give the finding, the range, and the outlier in a sentence, then link the table; `charts` holds the wording. Never encode a category in color alone. Write table headers as headers, so a cell can be announced with the row and column it belongs to.

**Plain language.** Use familiar words, manageable sentences and explicit connections suited to the actual reader. Retain necessary expert terms and meaningful qualifications. Put an action-critical precondition before the action; place other caveats where they are easiest to understand. Expand unfamiliar abbreviations. W3C's supplemental cognitive-accessibility guidance informs these choices but is not itself a conformance requirement. If a task needs a timeout extension, flag the product requirement and describe the control only when it exists.

**Accessibility statements.** Name the supplied assessment scope, known limitations, target standard and reporting route. A target is not a conformance finding. Do not invent tests, shipped alternatives, planned fixes or compliance claims; vague copy alone does not prove that nobody tested.

## Boundaries

The text assistive technology reads, on any surface in any medium. This module loads alongside a medium module and never instead of one.

Non-text accessibility — contrast, target size, focus order, motion — needs implementation and assessment beyond this module. Copy can identify a dependency or missing alternative; it cannot certify that the product implements it.

## Examples

These are independent synthetic records. Feature, chart and assessment details are supplied explicitly; a copyedit cannot establish them.

**Icon button labeled by its glyph**

**Supplied facts:** The icon button opens a menu of additional options. No more specific action applies to the button itself.

> label: `icon-dots-vertical`

> label: `More options`

**Alt text describing itself**

**Supplied facts:** A supplied bar chart shows quarterly revenue for 2024–2026, flat until Q3 2025 and then rising to $4.2 million. No causal explanation is supplied.

> Image of a chart showing data about our quarterly performance.

> Bar chart. Revenue by quarter, 2024–2026. Flat until Q3 2025, then rising to $4.2M.

**Link text that can't stand alone**

**Supplied facts:** The first link opens security practices. The second opens a policy explaining how long data are retained.

> To see our security practices, click here. For our data retention policy, click here.

> Read our security practices. See how long we keep data.

**Hint repeating the label**

**Supplied facts:** Delete moves the selected note to Recently Deleted rather than permanently erasing it. That consequence is not otherwise announced with the control.

> label: `Delete` &nbsp; hint: `Deletes the item`

> label: `Delete` &nbsp; hint: `Moves this note to Recently Deleted`

**Instruction by position and color**

**Supplied facts:** The action is Publish. The invalid fields are Title and Publish date. Their position and color are not necessary to identify them.

> Tap the blue button in the top right, then fix the fields shown in red.

> Tap Publish. Two fields need attention: Title and Publish date.

**Emoji in a label**

**Supplied facts:** Launch is the control's complete action name. The rocket is decorative and does not distinguish this control from another.

> label: `🚀 Launch`

> label: `Launch`

**A person described by their diagnosis**

**Supplied facts:** The brief names the intended audience as people who are blind or have limited mobility. It supplies no assistive-technology compatibility or keyboard assessment.

> Our app is designed for the blind and for wheelchair-bound users who suffer from limited mobility.

> Designed for people who are blind or have limited mobility.

**An accessibility statement that claims instead of tells**

**Supplied facts:** This fictional team targets WCAG 2.2 AA but has not completed a conformance assessment. Its editor and settings have passed the team's keyboard-navigation tests. The chart view does not expose interactive data to VoiceOver; an accessible table alternative is available. No release date for audio graphs is approved. The feedback address is access@kestrel.app.

> Kestrel is fully accessible and committed to inclusion for all users.

> Kestrel targets WCAG 2.2 AA; a conformance assessment is not complete. The editor and settings have passed our keyboard-navigation tests. The chart view does not yet expose interactive data to VoiceOver, but an accessible table alternative is available. Report a problem at access@kestrel.app.

**Form error that says nothing to a screen reader**

**Supplied facts:** Email and Publish date need correction. The email field requires an address. This is proposed copy plus a separately identified implementation requirement, not a claim that focus handling has already shipped.

> ⚠ (two fields turn red)

> 2 fields need attention: Email and Publish date.
>
> Email: Enter an address in the form name@example.com.

*Implementation requirement: associate the messages with their fields and provide appropriate error-summary and focus behavior.*

**A necessary long label**

**Supplied facts:** One action exports anonymized survey responses; another exports identifiable logs. The existing label fits its control and distinguishes the action accurately.

> Export anonymized survey responses

*No change. Shortening this to "Export" loses the distinction.*
