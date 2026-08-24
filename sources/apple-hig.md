---
id: sources.apple-hig
layer: sources
version: 1.3.0
status: active
budget: none
source:
  title: "Apple Human Interface Guidelines"
  publisher: "Apple Inc."
  year: 2026
  extent: "Foundations, patterns, components, inputs; ~150 pages read for text guidance"
  baseline: "The June 2026 revision, written to the OS 27 generation then in beta; reviewed 2026-08-09"
  license: "Copyrighted. Rules restated in original wording; no guideline text reproduced."
consumers:
  - user-interface/accessibility.md
  - user-interface/apple-hig.md
  - user-interface/applications.md
  - user-interface/charts.md
  - user-interface/website.md
---

# Source: Apple Human Interface Guidelines

Primary evidence base for the `user-interface/` layer. Unbudgeted by design: nothing here is loaded alongside a draft. This is what you read when you author or revise an interface module.

This dossier restates every rule in original wording. Apple's HIG is copyrighted, and this file reproduces none of it. Where a specific string appears — `Cancel`, `Add to Cart`, `Notification` — it appears as an identifier, because the literal string is the finding.

## Why This Source

Nothing else covers this ground with this much specificity.

The interface-writing literature is mostly conference talks and agency blog posts, and it repeats itself: be clear, be concise, be human. The HIG is the only widely available document that goes down to the level that actually decides copy — whether an alert title takes a period, when an ellipsis is required, what a button in an informational alert may be called, what the placeholder does when the field is not empty. Those are the decisions a writer gets wrong, and they are decisions a general style guide cannot reach because they depend on the component.

Apple also enforces it, shipping tens of thousands of strings under it and reviewing third-party apps against parts of it. The rules have therefore met real products at scale rather than only an argument in a post. That is a different kind of evidence from a taxonomy of tells, and it is the kind `user-interface/` needs: not *this reads as machine-made*, but *this fails*.

And it carries the one thing the anti-slop sources have no theory of at all — what interface text is *for*. Its framing is that the words are part of the experience, read by someone in the middle of doing something else, on a device whose size and setting change what can be said. Prose sources assume a reader who chose to read.

### The repurposing caveat

The HIG is a platform specification for Apple operating systems. It exists so that third-party apps feel like the system they run on. `emerson-press` uses it for something wider: writing interface text anywhere. Four consequences follow, and the third is the one that causes real errors.

- **Platform guidance is not text guidance.** Most of the document is layout, color, symbols, and API surface. Only the writing rules transfer, and whoever built this file threw out roughly nine-tenths of what they read.

- **Some rules are conventions, not truths.** Apple capitalizes button and menu labels in title case. Material Design uses sentence case. Neither is correct; each is a house convention held consistently, which is the part that matters. `user-interface/applications.md` therefore states the rule as *hold one convention per element type*, and `user-interface/apple-hig.md` carries Apple's answer as the worked example. Anywhere the HIG's answer is arbitrary-but-consistent, the module must say so rather than export Apple's answer as law.

- **Some rules are load-bearing and look arbitrary.** The ellipsis on a menu item means more input is required before anything happens. `Cancel` always names the control that abandons the action. These are not typography preferences; they are a vocabulary the reader has already learned, and breaking them costs comprehension rather than polish. Distinguishing this category from the previous one is most of the work of reading this source.

- **Its register is Apple's.** Neutral, direct, low-humor, low-apology. That is a defensible default for interface text and it is the default `user-interface/applications.md` takes, but it is a choice. A game, a children's app, or a product with a real editorial voice will diverge, and the `domain/` module governs that, not this source.

## What It Says About Voice

The stated position, restated: address the person directly with *you* and *your*; referring to them as *the user* or *the player* makes the product feel distant. Reserve *we* for the company or the software itself, and use it sparingly, because it can imply a personal relationship the reader has not agreed to.

Establish a voice, then vary the tone by situation. The worked contrast is between an alert about a serious condition and a congratulation on finishing a workout: same voice, opposite tone. Situational factors change both what is said and how it is displayed.

On alert copy specifically: be direct, neutral, and approachable; do not be oblique or accusatory; do not mask the severity of what happened.

On humor: subjective, hard to translate, and it wears out. The stated risks are confusing people who do not get it, irritating people who meet it repeatedly, and insulting people who read it differently. The third is the one that matters for a surface the reader cannot avoid.

On register generally: an academic tone welcomes only readers with a lot of education. Plain language is framed as an inclusion requirement, not a simplification.

## What It Says About Consistency

The strongest section, and the one with no equivalent in any prose source, because prose has no equivalent problem. A reader meets a paragraph once. A reader meets a product's word for *delete* a thousand times.

The stated practice is to build language patterns and reuse them: decide title case or sentence case per element type and hold it; decide first person or second — *My Favorites* or *Your Saved Items* — and never ship both; decide `Continue` or `Next` for a multi-step flow, hold it, and change the word at the end so the last step reads differently.

Vocabulary must match the platform: do not say *click* on a touch device or *tap* on a desktop.

Never name the widget in copy that guides. Guidance that mentions the popover should describe the button instead. When directing someone to a control, use the control's exact title, without quotation marks around it.

Define specialized terms or drop them. Replace colloquial expressions, and the stated reason is not brevity: some idioms carry exclusionary histories that the writer may not know, and the plain sentence also translates better.

## What It Says Per Surface

Condensed. The modules carry the detail.

**Alerts.** They interrupt; do not use one merely to inform. Do not alert at launch — show cached or placeholder content and a quiet label instead. Do not warn about data loss the reader intended and can undo; warn when loss is unexpected and irreversible. A title that says only *Error*, or that recites an error number, conveys nothing; the title should say what happened, in what context, and why. Title in a complete sentence takes sentence case and punctuation; a fragment takes title case and no period. Buttons are one or two words, title case, no period, and name the result. `OK` is acceptable only in a purely informational alert; on anything consequential the reader cannot tell whether it means *proceed* or *understood*. Use the specific verb instead. `Cancel` always titles the button that abandons the action, always accompanies a destructive one, and is never the default. Destructive styling is for an action the reader did not deliberately choose; emptying the trash on purpose is not styled as a warning.

**Errors and validation.** An error goes in an alert, never a notification. Validate at the moment that helps: an email address when focus leaves the field, a new password before focus leaves it. Give feedback the instant a problem is detectable, so it can be fixed in place. When a command cannot run, say why.

**Forms.** Placeholder text disappears on the first keystroke, so a field that needs a name needs a separate label as well. A placeholder can show format by example or describe the content. Prefill sensible defaults; never prefill a password. Offer a choice instead of demanding typed text. Do not assume a number, currency, or date format — presentation is locale-dependent.

**Empty and loading.** If nothing appears while content loads, the reader reads the blank as a failure; show placeholder content and replace it. Say that content is loading and roughly how long. Reasonable defaults let someone start without configuring anything.

**Status and progress.** Vague words such as *loading* and *authenticating* add nothing; name the task. Pacing that runs to ninety percent in five seconds and takes five minutes for the rest reads as deceptive. A refresh control's title should carry information about the content, not explain how to refresh. Offer `Cancel`; offer `Pause` as well when interrupting would cost work. When a process halts, explain what happened and what can be done.

**Onboarding and help.** Teach by letting someone safely do the thing. Context-specific tips beat a single upfront flow. Keep a tip to one or two sentences, action-oriented, never promotional. Do not explain standard components. Keep licensing out of onboarding. Ask for permission where the function is used, unless the product cannot function without it, in which case say what the reader gets. Let people use the product before asking for a rating. Put no text on a launch screen, because it never gets localized.

**Notifications.** Provide the information, not an instruction to go and find it; the reader will not remember an instruction after dismissing it. Never send the same notification twice. Keep sensitive content out of previews. The title is brief with no ending punctuation; the body is a complete sentence, punctuated, never truncated by hand. Do not put the app's name in the copy — the system already shows it. Action labels are short, title case, and name the result. Choose the interruption level honestly: the top level is for health and safety. Marketing requires explicit opt-in and is never time-sensitive. Badges count things waiting, not scores or prices.

**Settings.** Fewer settings is better; a long list is harder to search than a short one. Do not restate a systemwide setting inside the product — it implies the system's own setting might not apply. Do not ask for something detectable. Describe what a setting does when it is on, and let the off state be inferred. To send someone to a setting, link to it rather than describing where it lives.

**Accessibility.** Label every interface element; unlabeled controls break VoiceOver, Voice Control, Switch Control, and Full Keyboard Access alike. Provide text equivalents for audio and video — captions, subtitles, audio descriptions, transcripts are distinct things, not synonyms. For an action that is hard to undo, confirm twice in the Assistive Access context. Write about disability people-first, and never use a disability to name a bad quality.

**Inclusive language.** Rewrite around gendered singular pronouns rather than stacking them; the plural subject is both more inclusive and easier to localize into languages with gendered pronouns. Where gender must be collected, offer non-binary, self-describe, and decline options. Avoid prompts that assume a shared background — the worked example replaces security questions about college subjects and first cars with questions anyone can answer.

## Where It Is Thin

Named so the modules do not pretend to a citation they do not have.

- **Empty states get one sentence.** The zero-result screen, the filtered-to-nothing screen, and the you-finished-everything screen are not distinguished anywhere. The four-way split under `## Surfaces` in `user-interface/applications.md` is built from the loading and alert guidance plus practice, and it is the weakest-sourced passage in the axis.
- **No VoiceOver label formula.** The document repeats that elements must be labeled and defers the *how* to a separate page outside the mined set. Alt-text construction, hint phrasing, and announcement etiquette are not specified.
- **Little on error-message construction.** There is a strong rule about what an alert title must not be, and much less about what the body should contain. The what-happened / what-it-means / what-now shape in the errors passage of `user-interface/applications.md` is inferred from the alert-title rule and the password example, not stated.
- **Nothing on the ampersand.** The mined set has no line on `&` against *and*, in body text or anywhere else. The rule in `user-interface/apple-hig.md` — spell *and* in body text, allow `&` only where space is tight and the element already uses it — is an inference. Its second half stands on the mined *hold one convention per element type* principle recorded under `### The repurposing caveat`, which is real. Its first half, the *and*-by-default, does not: nothing here establishes which of the two Apple treats as unmarked. Read the whole rule as sound interface practice rather than as Apple's word, and do not cite this file for it.
- **Nothing about string concatenation or plural rules**, despite an otherwise careful localization thread. The length and format warnings are there; the assembly problem is not.
- **Nothing explicit on default button position.** The trailing-default convention in `user-interface/apple-hig.md` is read off shipped system alerts and off the `Cancel`-is-never-the-default rule, not stated in the mined set.
- **No account of tone under failure at scale** — outages, data loss, billing. The register guidance assumes recoverable situations.

## What `user-interface/` Takes

1. **The reader is mid-task.** The organizing assumption of the whole axis.
2. **Second person, present tense, situational tone** as the default register.
3. **Per-element mechanics** — capitalization, terminal punctuation, ellipsis semantics, length — which is the layer no prose source reaches.
4. **The `OK` argument.** A button must name its outcome, because the reader is deciding, not acknowledging. The single most portable rule in the document.
5. **The interruption budget.** An alert, a notification, and a permission prompt each spend something, and the guidance is consistently about whether the spend is justified.
6. **Consistency as a first-class requirement**, with the concrete tests: one case convention per element, one person, one word per action.
7. **Plain language as inclusion**, which is a better argument for it than brevity and one that survives contact with a technical audience.
8. **Labeling as a hard requirement**, not an enhancement.
