---
id: sources.apple-hig
layer: sources
version: 1.4.0
status: active
budget: none
evidence_kind: publisher-guidance
checked_on: 2026-09-08
verification_status: partial
source_version: "Historical June 2026 notes without an immutable snapshot; live Writing, Alerts, Buttons and Menus checked September 8, 2026"
source_urls:
  - https://developer.apple.com/design/human-interface-guidelines/writing
  - https://developer.apple.com/design/human-interface-guidelines/alerts
  - https://developer.apple.com/design/human-interface-guidelines/buttons
  - https://developer.apple.com/design/human-interface-guidelines/menus
  - https://www.w3.org/WAI/WCAG2/supplemental/patterns/o3p01-clear-words/
  - https://www.w3.org/WAI/WCAG2/supplemental/about/
verification_note: "Current checks cover the four named Apple pages and public W3C supplemental guidance, not the whole HIG, all OS versions, or a product accessibility assessment. Other surface notes remain historical paraphrases or identified house guidance."
source:
  title: "Apple Human Interface Guidelines"
  publisher: "Apple Inc."
  year: 2026
  extent: "Historical foundations/patterns/component notes; original coverage count not independently reproduced"
  baseline: "Prior notes described a June 2026 baseline reviewed August 9, 2026; September checks are limited to the named live pages"
  license: "Copyrighted. Rules restated in original wording; no guideline text reproduced."
consumers:
  - domains/user-interface/accessibility.md
  - domains/user-interface/apple-hig.md
  - domains/user-interface/applications.md
  - domains/user-interface/charts.md
  - domains/user-interface/website.md
---

# Source: Apple Human Interface Guidelines

Primary evidence base for the `domains/user-interface/` layer. Unbudgeted by design: nothing here is loaded alongside a draft. This is what you read when you author or revise an interface module.

This dossier restates every rule in original wording. Apple's HIG is copyrighted, and this file reproduces none of it. Where a specific string appears — `Cancel`, `Add to Cart`, `Notification` — it appears as an identifier, because the literal string is the finding.

## Why This Source

The HIG gives useful component-specific guidance for writing during a task. It is publisher guidance, not a controlled experiment showing that this repository's prompts improve writing.

The useful detail includes alert-title punctuation, menu ellipses, action labels and error placement. Other platform and accessibility sources also address interface text; no claim of unique coverage is made here.

Published guidance and shipped interfaces are different evidence. A product convention observed in an app is not automatically a documented requirement, and neither proves that all third-party apps follow it.

Its task-centered framing transfers usefully: wording belongs to a situation, device and reader. The transfer beyond Apple remains an editorial choice, not a reason to impose Apple mechanics everywhere.

## September 2026 verification ledger

The HTML pages use JavaScript; their public DocC JSON under `https://developer.apple.com/tutorials/data/design/human-interface-guidelines/` was read for `writing.json`, `alerts.json`, `buttons.json` and `menus.json`.

| Location | Verified support | Limit |
| --- | --- | --- |
| Writing, voice/tone and language-pattern paragraphs | Actual audience, situational tone, consistent vocabulary and per-element capitalization choices; component-specific exceptions control | No universal casing rule for every control follows |
| Alerts, Content | Complete-sentence titles use sentence-style capitalization and punctuation; fragments use title style without terminal punctuation | Applies to alert titles, not every heading |
| Alerts, Buttons | A default is trailing in a row or first in a stack; Cancel is not the alert default; no default is appropriate when readers should consider the alert | A physical right-hand position is not universal |
| Alerts, Buttons | Deliberately requested Empty Trash can be confirmed with Return without destructive styling; include Cancel with a destructive choice | Default behavior and destructive styling are distinct |
| Buttons, primary-role guidance | Do not give a destructive action the primary role | Do not conflate the general button role with every alert's keyboard default |
| Menus, labels | Generally prefer title-style capitalization; use an ellipsis for an action requiring further input or choices | The page allows established game-writing differences |
| Buttons, macOS push buttons | An ellipsis signals opening another window, view or app for further input | A component/platform-specific convention |
| W3C, clear-words pattern and supplemental-guidance status | Reader-oriented language support; supplemental guidance is not required for WCAG conformance | This is not a product conformance finding |

Older page-level claims below have not all been independently rechecked. Treat their named limits as part of the evidence rather than upgrading the entire dossier to current verification.

### The repurposing caveat

The HIG is a platform specification for Apple operating systems. It exists so that third-party apps feel like the system they run on. `emerson-press` uses it for something wider: writing interface text anywhere. Four consequences follow, and the third is the one that causes real errors.

- **Platform guidance is not all text guidance.** Layout, symbols, roles and APIs need implementation knowledge. Copy can flag a dependency without proving it is implemented.

- **Some rules are conventions, not truths.** The current Writing page permits app-appropriate per-element choices, while Alerts and Menus provide more specific guidance. `domains/user-interface/applications.md` keeps consistent house mechanics; the Apple overlay applies the relevant component exception rather than exporting one answer as universal law.

- **Some rules are load-bearing and look arbitrary.** The ellipsis on a menu item means more input is required before anything happens. `Cancel` always names the control that abandons the action. These are not typography preferences; they are a vocabulary the reader has already learned, and breaking them costs comprehension rather than polish. Distinguishing this category from the previous one is most of the work of reading this source.

- **Its register is Apple's.** Neutral, direct, low-humor, low-apology. That is a defensible default for interface text and it is the default `domains/user-interface/applications.md` takes, but it is a choice. A game, a children's app, or a product with a real editorial voice will diverge, and the `domains/` module governs that, not this source.

## What It Says About Voice

The stated position, restated: address the person directly with *you* and *your*; referring to them as *the user* or *the player* makes the product feel distant. Reserve *we* for the company or the software itself, and use it sparingly, because it can imply a personal relationship the reader has not agreed to.

Establish a voice, then vary the tone by situation. The worked contrast is between an alert about a serious condition and a congratulation on finishing a workout: same voice, opposite tone. Situational factors change both what is said and how it is displayed.

On alert copy specifically: be direct, neutral, and approachable; do not be oblique or accusatory; do not mask the severity of what happened.

On humor: subjective, hard to translate, and it wears out. The stated risks are confusing people who do not get it, irritating people who meet it repeatedly, and insulting people who read it differently. The third is the one that matters for a surface the reader cannot avoid.

On register generally: use words familiar to the actual audience and support accessibility and localization. Credentials do not establish familiarity; necessary specialist terms can be the clearest words for an expert task.

## What It Says About Consistency

Consistency matters when people repeat tasks and learn a product's vocabulary. Use the same term for the same action without renaming genuinely different concepts for surface uniformity.

The stated practice is to build language patterns and reuse them: decide title case or sentence case per element type and hold it; decide first person or second — *My Favorites* or *Your Saved Items* — and never ship both; decide `Continue` or `Next` for a multi-step flow, hold it, and change the word at the end so the last step reads differently.

Vocabulary must match the platform: do not say *click* on a touch device or *tap* on a desktop.

Prefer the action and the control's exact name to irrelevant widget jargon. A technical explanation can name a component when the reader needs that concept.

Define specialized terms or drop them. Replace colloquial expressions, and the stated reason is not brevity: some idioms carry exclusionary histories that the writer may not know, and the plain sentence also translates better.

## What It Says Per Surface

Condensed. The modules carry the detail.

**Alerts — currently checked.** Avoid interrupting for common undoable actions; uncommon irreversible actions can need confirmation. Use an informative title with the documented sentence/fragment casing. Prefer concise action labels without sacrificing a necessary distinction; `OK` belongs to purely informational alerts. Cancel abandons the action and accompanies a destructive choice, but is not the alert default. The verified Buttons section explicitly permits no default and distinguishes a deliberate destructive action from destructive styling. Follow the ledger rather than a blanket ban on every destructive default.

**Errors and validation.** The current Writing page recommends placing an error close to the problem, avoiding blame and explaining how to fix it. It does not require every error to become an alert. Validation timing and focus need product implementation, not just a new sentence.

**Forms — historical notes.** Persistent labels and format hints serve different purposes. Use appropriate known defaults, supported choices and locale-aware presentation. Do not confuse secure password autofill with publishing a secret in a form; current platform/autofill rules need their own check.

**Empty and loading — historical notes and house application.** Give useful loading state rather than an unexplained blank. Report a duration only if supported. Defaults can reduce unnecessary setup; they must still suit the task.

**Status and progress — historical notes and house application.** Name the task when that helps. Report progress honestly; do not invent an estimate or a Cancel/Pause control. When a process halts, explain the known state and available next action.

**Onboarding and help — historical notes.** Prefer safe, relevant practice and concise contextual tips. Explain unfamiliar prerequisites when the actual reader needs them. Defer avoidable interruptions, but retain legally or operationally required information. Permission, launch-screen and rating behavior need current component guidance rather than a blanket copy rule.

**Notifications — historical notes.** Deliver useful information, avoid pointless duplication and protect preview privacy. Use the target component's title/body and action-label conventions. Do not repeat an app name the system already supplies. Check current permission and interruption-level requirements before describing a notification as urgent or compliant.

**Settings.** The currently checked Writing page recommends practical labels and a useful explanation of the on state. The broader historical preference for fewer settings is not a reason to remove a needed control or infer unsupported system behavior.

**Accessibility — partial coverage.** Meaningful controls need accessible names; decorative elements need not be announced. Describe what each media alternative actually supplies, rather than assuming every service uses the same terminology. Assistive Access has component-specific behavior that needs separate verification; the prior exact confirmation count is not carried forward as a universal rule. Respect community language preferences and do not turn disability into a pejorative.

**Inclusive language — partial coverage.** The current Writing page recommends accessible, localizable language and avoidance of unnecessary gendered terminology. Preserve a known person's pronouns and meaningful distinctions. Broader collection and identity-design choices need their own policy and reader context rather than inference from a writing preference.

## Where It Is Thin

Named so the modules do not pretend to a citation they do not have.

- **The four-way empty-state taxonomy is house guidance.** The retained source notes did not establish it as an Apple taxonomy. That limited coverage does not show that Apple never distinguishes these states.
- **No complete accessibility specification was checked.** Current label, hint, alternative-text and announcement guidance needs the relevant component and accessibility sources, not an inference from missing notes.
- **Little on error-message construction.** There is a strong rule about what an alert title must not be, and much less about what the body should contain. The what-happened / what-it-means / what-now shape in the errors passage of `domains/user-interface/applications.md` is inferred from the alert-title rule and the password example, not stated.
- **The ampersand preference is house style.** The reviewed subset does not establish the overlay's *and*-by-default preference as a HIG rule. This does not assert that all Apple publications lack guidance on ampersands.
- **String assembly and plural rules need separate developer guidance.** Their absence from the retained notes is not absence from Apple documentation.
- **The old default-position uncertainty is resolved for Alerts.** Its current Buttons section explicitly distinguishes rows and stacks and permits no default. It does not establish one physical position for every Apple control.
- **Broader incident communication remains outside this check.** Do not claim that Apple lacks such guidance merely because outages or billing incidents were not independently reviewed here.

## What `domains/user-interface/` Takes

1. **The reader is mid-task.** The organizing assumption of the whole axis.
2. **Second person, present tense, situational tone** as the default register.
3. **Per-element mechanics** — capitalization, terminal punctuation, ellipsis semantics, length — which is the layer no prose source reaches.
4. **The `OK` argument.** A button must name its outcome, because the reader is deciding, not acknowledging. The single most portable rule in the document.
5. **The interruption budget.** An alert, a notification, and a permission prompt each spend something, and the guidance is consistently about whether the spend is justified.
6. **Consistency as a first-class requirement**, with the concrete tests: one case convention per element, one person, one word per action.
7. **Plain language as inclusion**, which is a better argument for it than brevity and one that survives contact with a technical audience.
8. **Labeling as a hard requirement**, not an enhancement.
