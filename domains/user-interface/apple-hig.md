---
id: user-interface.apple-hig
layer: user-interface
version: 1.1.0
status: draft
budget: 1338
tokens: 1338
kind: overlay
medium: apple
mechanics: hig
elements: [button, menu item, alert, notification, setting, purpose string]
evidence:
  - tests/sources/apple-hig.md
---

# Interface: Apple HIG

Some Apple conventions establish a recognizable style; others communicate behavior, such as a menu ellipsis signaling further input. Apply the guidance for the actual component and platform rather than treating every convention as universal.

Specializes `domains/user-interface/applications.md` for documented Apple component mechanics and behavior. The source dossier distinguishes current public checks from historical notes and house preferences. Genre, actual reader needs, factual fidelity and required disclosure still apply.

## Mechanics

**Capitalization.** Apple's Writing guidance calls for consistent choices by UI element type and app voice, with specific component guidance taking precedence. Alert buttons use title-style capitalization; Menus generally recommends it, with room for a game's established style. Do not turn those recommendations into a universal title-case requirement for every label, view or control. Follow the target component and Apple's capitalization guidance rather than an invented word-length formula.

An alert title takes whichever case its shape calls for. A fragment or a short question is title case with no period — `Delete Draft?`. A title written as a complete sentence is sentence case and takes terminal punctuation — `Your subscription expired on August 3.`

**Terminal punctuation.** Alert buttons and fragment titles have no terminal period. Complete-sentence alert titles and body text take appropriate ending punctuation. Apply the relevant component or consistent house convention to other elements.

**Ellipsis.** A menu ellipsis signals that the action needs more information or choices before it can complete — for example, a configured `Save As…` flow. Apple's macOS push-button guidance also uses it for opening another window, view or app for input. Check the actual flow; a progress display alone does not establish the need for an ellipsis.

**Ampersand — house preference.** Prefer *and* in body text; use `&` where an established element convention calls for it. This is not presented as a verified HIG requirement. Preserve proper names and literal interface strings.

## Detect

- Case that conflicts with the target component's guidance or the app's consistent element convention; for example, title case throughout an alert body.
- **A period on a button**, or on an alert title written as a fragment.
- **Case chosen by element rather than by shape** in an alert title: a fragment set in sentence case, a full sentence set in title case.
- An ellipsis on a command that acts immediately, or a missing ellipsis on one that opens a dialog to collect input.
- **`OK` on a button that acts.** `OK` means *I have read this* on an alert that offers no choice. Where there is a decision, the button carries the verb.
- `Cancel` used for anything other than abandoning the alert action, made an alert's default, or paired with a confusing `Cancel`/`Don't Cancel` question.
- **`Yes` and `No` as button labels**, which forces the reader back to the title to find out what they are agreeing to.
- An alert default placed contrary to its row/stack convention; a destructive action given a general button's primary role; or an accidental Return keypress triggering a consequential action the reader needs to consider.
- **Platform-wrong verbs**: *click* on iOS, *tap* on macOS, *press* for a pointer.
- Explaining Apple's own conventions — how a gesture works, what a share sheet is — which the reader learned from the system, not from you.
- A notification title that repeats the app name the system already shows.
- **Apple's proper nouns renamed or miscapitalized**: *touch ID*, *iCloud drive*. Use the names appropriate to the target version; do not rename quoted legacy interface strings.

## Write

Use Apple's terms for Apple's things — *Sign in with Apple*, *iCloud Drive*, *Face ID*, *the Home Screen* — capitalized as Apple capitalizes them, and use your own terms for yours.

Prefer *turn on* and *turn off* to *enable* and *disable*, *choose* for an option and *select* for an object, *sign in* rather than *log in*.

Prefer a cross-device verb such as *choose* when it communicates the action. Use an accurate device-specific gesture when it is part of the instruction.

Write for translation and the actual reader. Avoid unnecessary idioms and directions that rely only on position, such as *below* or *to the left*. Layout can mirror and translated strings can grow; do not assume one expansion percentage for a language.

## Surfaces

**Alerts.** Case the title by its shape and the body in sentence case. Action labels use title-style capitalization and no period; prefer concise verbs without dropping a necessary distinction. Apple's Alerts guidance explicitly places a default on the trailing side of a row or at the top of a stack; Cancel is typically leading or at the bottom. Include Cancel with a destructive choice, and do not make Cancel the alert default. When the reader needs to consider the alert rather than reflexively press Return, use no default button.

**Roles, defaults and destruction.** These are separate concepts. Apple's general Buttons guidance says not to give a destructive action the primary role. Its Alerts guidance separately permits a deliberately requested action such as Empty Trash to be confirmed with Return without destructive styling. Do not infer that every destructive action is forbidden as an alert default, or that an unstyled action is safe. Use the applicable component rule and the actual loss/recovery behavior. For an unexpected consequential choice requiring review, use no default rather than preselecting the loss.

**Purpose strings.** Apple shows your sentence inside the system's own prompt, so write one sentence in sentence case naming the feature and the data it uses. When to ask is `applications`.

**Notifications.** Title in a few words, body as one complete sentence in sentence case. Never repeat the app name; the system already shows it.

**Settings.** Footers in sentence case, describing the on state. What a setting is called, and how it is grouped, is `applications`.

## Boundaries

Follow documented Apple component mechanics on the target Apple platform. Do not export them as requirements for the web or Android; those surfaces have their own conventions.

This module covers verified component-specific exceptions, not a complete interaction or accessibility assessment. `applications.md` supplies broader task-copy guidance; `website.md` and `charts.md` retain their own scope. An instruction to remove a default is an implementation requirement, not evidence that keyboard behavior has already been changed.

## Examples

These independent synthetic product records supply the behavior. Bold labels denote a keyboard default only where explicitly shown.

**Ellipsis on a command that acts**

**Supplied facts:** Delete acts immediately. Print and Save As open input/choice flows before completing. These are menu commands using Apple's documented ellipsis convention.

> Delete… &nbsp; Print &nbsp; Save As

> Delete &nbsp; Print… &nbsp; Save As…

**`Yes`/`No` on a decision**

**Supplied facts:** Discard permanently loses the current draft; Cancel preserves it. The requested alert needs a deliberate choice, with no default action.

> Are you sure you want to discard this draft? &nbsp; [ No ] [ Yes ]

> Discard Draft? &nbsp; You can't undo this. &nbsp; [ Cancel ] [ Discard ]

**Default button on the destructive action**

**Supplied facts:** This alert presents an unexpected bulk move of 40 items to Trash. The task requires the reader to review it before acting; Cancel is safe. The proposed design uses no default, not a default Cancel button. This is not the deliberate Empty Trash exception.

> Move 40 items to the Trash? &nbsp; [ **Move to Trash** ] [ Cancel ]

> Move 40 Items to the Trash? &nbsp; [ Cancel ] [ Move to Trash ]

*Implementation requirement: neither button is the default; Return alone must not execute the move.*

**Alert with no decision in it**

**Supplied facts:** Saving succeeded and the saved file is visibly present. The task asks whether this extra informational interruption is useful; no hidden failure or acknowledgment requirement is involved.

> Success! Your file has been saved successfully. &nbsp; [ OK ]

*Delete the alert. The saved file is the confirmation.*

**Purpose string that describes the system, not the reader**

**Supplied facts:** Location access lets Kestrel add a place to a note. The person can enter the place manually instead. No broader claim that every product feature works without location is supplied.

> This app would like to access your location.

> Location lets Kestrel add a place to your notes; you can enter a place manually instead.

**Alert title cased by element instead of by shape**

**Supplied facts:** The subscription expired on August 3. The brief asks the alert to offer the existing renewal flow: Renew opens options without charging, while Not Now dismisses it. Renew is the specified nondestructive default.

> your subscription expired on august 3. &nbsp; [ OK ]

> Your subscription expired on August 3. &nbsp; [ Not Now ] [ **Renew** ]

**A platform verb and a word that carries the layout**

**Supplied facts:** Continue is the displayed label. Choosing it closes this view. The instruction is shared across pointer and touch devices and needs no positional description.

> Tap the blue button below to dismiss this modal.

> Choose Continue.

**Notification repeating the app name**

**Supplied facts:** The system already shows the app name. In this synthetic event, Dana Osei comments on "Q3 forecast" with the exact text "Can you check the March number before Friday?" That preview is permitted.

> Kestrel &nbsp; Kestrel: New comment on your note

> Dana Osei commented on "Q3 forecast" "Can you check the March number before Friday?"
