---
id: user-interface.applications
layer: user-interface
version: 1.1.0
status: draft
budget: 1874
tokens: 1874
kind: medium
medium: app
mechanics: house
elements: [label, button, form field, error, alert, permission prompt, empty state, progress, onboarding, notification, setting]
evidence:
  - tests/sources/apple-hig.md
  - tests/sources/kill-ai-slop.md
  - tests/sources/stop-slop.md
---

# Interface: Applications

Text inside a product someone is using to get something done. The reader did not open the app to read, and every word is a toll on the way to what they came for.

Platform-neutral house rules. For Apple platforms, load `domains/user-interface/apple-hig.md` as well; it wins on mechanics.

## Detect

- **Marketing voice on a working surface.** *Say goodbye to, meet your new, supercharge, unlock the power of, seamless, effortless, blazing fast.* A landing page may sell. A settings screen may not.
- **Enthusiasm the moment does not contain.** *Awesome! You're all set!* on the completion of a chore.
- **The reader in the third person** — *the user can*, *players are able to* — or `we` doing the reader's work.
- Apology inflation: *Oops, uh-oh, sorry about that.* A joke on a surface the reader crosses every day.
- **Synonym churn.** *Delete*, *Remove*, *Trash*, and *Discard* for one action. *Workspace*, *team*, and *organization* for one container.
- Internal vocabulary unexplained to this reader: *entity, tenant, endpoint, payload, job.* Keep terms an expert reader actually uses.
- Widget names in guiding copy: *dismiss the modal*, *the button in the popover.* Platform verb mismatch: *click* on a phone.
- `(s)` and slashes standing in for a plural the writer would not choose.
- Register drift between surfaces — jokes in the empty state, legalese in the error, marketing in a settings footer.
- Text that describes the product instead of the reader's situation.

## Write

Address the person: *you*, *your*. Keep *we* for the company doing something the reader needs to know about, and use it rarely. Present tense, active voice, the reader as subject.

One voice, many tones. Tone belongs to the situation, not the brand: a failed payment and a finished workout do not sound alike.

Say the specific thing you can support. *Opens in under a second* needs an applicable measurement; do not invent one to replace *blazing fast*. When performance evidence is missing, describe a known function or omit the claim.

One name per thing and one verb per action, decided once and written down. Use the reader's noun, not an unexplained schema label. Keep *objects* when that is the product concept the reader knows; do not rename a distinct concept *files* merely to sound simpler. Name the thing or action rather than an irrelevant widget.

Define a term the first time it appears on a screen, because the reader did not necessarily arrive from the previous one.

Do not apologize for something the reader has not been told about yet. Say what happened first.

Write about people first and disability second, unless the community has said otherwise — `domains/medical.md` holds that exception and it survives this layer. Never borrow the name of a condition to label something bad.

## Surfaces

**Labels and actions.** Name the result, usually verb first. Prefer a short label, but retain the words that distinguish actions or explain a consequential choice. Reserve `OK` for an alert that informs and offers no choice; anywhere there is a decision, the button names the action. `Cancel` means abandoning an action without proceeding. Follow the platform/component's safe-default policy; a safe alternative or no default may be appropriate. Do not preselect an irreversible action merely to make the flow faster. Hold one capitalization convention per element type. No terminal period. Where the platform uses this convention, a trailing ellipsis means more input is needed before the command completes. A menu command that flips a state names the action it will perform — *Turn HDR Off* when HDR is on. A badge is a status claim; remove it when that claim no longer applies.

**Forms.** Every field gets a persistent label; the placeholder shows format (`name@example.com`), never the question. State the requirement before the attempt, not in an error after it. Validate when the answer is complete. Write the fix, not the fault, beside the field. Accept supported formats; normalize only where doing so preserves meaning and the product actually supports it. Mark the smaller set — if most fields are required, mark the optional ones. Use appropriate known defaults without exposing sensitive information.

**Errors.** Three jobs: what happened, what it means here, what to do next. Lead in the past tense and in the reader's terms. Name what was kept and what was lost when known; make an unknown save or sync state explicit rather than promising safety. Give the next action as a button, or say who can fix it. Give a timeframe only when supported. Keep a useful diagnostic code after the sentence, not an irrelevant stack trace. Repeated failures may require a product fix, not just new wording.

**Alerts and permissions.** Interrupt for a necessary decision or a consequential, unexpected loss. Title the consequence: *Delete 14 photos?* Add detail when it changes the decision, including scope, reversibility and a known recovery period. Do not routinely confirm an expected, undoable action. Destructive behavior, destructive styling and keyboard defaults are separate choices governed by the target component; wording must accurately describe the result. Ask for a permission where the feature is used, and say what the reader gets for it.

**Empty states.** Four different screens: nothing yet, nothing matching, nothing left, nothing available. Write only the one you are in. *Nothing yet* names what will appear and gives the action that makes it appear. *Nothing matching* echoes the query and the active filters and offers the widening move. *Nothing left* is a plain confirmation. *Nothing available* is a failure — write it as an error. Put nothing permanent on a screen designed to disappear.

**Status and progress.** Name the object and the stage when those details help. Give a proportion or duration only when it can be tracked honestly, and prefer counts when available — *4 of 12 files*. Change the button while its action runs. Offer `Cancel` or `Pause` when supported and useful; do not promise controls or saved progress the product lacks. When a process stalls, replace the status with what happened. Distinguish offline from failed. Confirm silently where the result is already visible.

**Onboarding.** Get the reader to one real result, then stop. Teach by letting them do the thing, undoably, on their own data. Ship defaults so setup is optional. Defer every permission to the moment it is needed. Keep a tip to a sentence or two, with the action at the front. Explain your own product's ideas, not the platform's. Make the tour skippable and findable afterwards.

**Notifications.** The notification is the message, not a pointer to it. Title in a few words; body as one complete sentence, left for the system to truncate. Name the actor and the object as the reader would. Assume someone else can see the preview. One notification per event. Choose the interruption level for the reader's stake, not yours; a promotion is opt-in and never urgent. Badge only what is waiting for a decision. Errors go where the reader can act, not here.

**Settings.** Label the effect, not the mechanism. A switch is named, not commanded: phrase it so that on means more of the thing named — *Notifications*, not *Disable notifications*, and not *Turn Notifications Off*, which is a menu command's shape. Write a footer only when it adds a consequence the label cannot carry, and describe the on state. Group by the reader's goal; a section called *Advanced* means the settings in it need better names. Do not restate a system setting or ask for what you can detect. Link to a setting rather than describing where it lives. Say what a setting will not do, when readers reliably expect it to.

## Boundaries

Working product surfaces, whatever the platform or authentication state: a native app, a desktop client, anonymous checkout, a booking form or a dashboard. Informational and persuasive pages use `website.md`, even when access requires sign-in. Route by the reader's task, not the login boundary. Register stays with the genre and actual reader needs; optional classroom presets do not override them. A children's app keeps its warmth, a peer tool keeps its terms of art. What this module strips is unearned enthusiasm, not earned tone.

Validation timing, focus, recovery, permissions and available controls are product dependencies. Flag a missing implementation separately; rewriting copy does not establish that the behavior exists.

Long-form product writing — release notes, help articles, in-app guides — is `domains/technical.md`. Email and other messages that arrive outside the product are neither this module nor `website.md`; use `domains/` until this axis claims them. Conversational surfaces — an assistant's replies, a chat agent's refusals — are not covered here either: they are read rather than scanned, so the attention economy this module assumes does not hold.

## Examples

These are independent synthetic product records. The supplied facts, not a desire for more vivid copy, authorize the details in each revision.

**Onboarding that tours instead of starting**

**Supplied facts:** Kestrel is a fictional notes product. This onboarding screen can open a first note; actions in that exercise are undoable, and a Skip control is available.

> Welcome to Kestrel! Let's take a quick tour of everything you can do. &nbsp; (1 of 7)

> Write your first note. &nbsp; Anything here can be undone. &nbsp; [ Skip ]

**An alert that hides the decision**

**Supplied facts:** This confirmation concerns 14 photos. Deletion also removes them from the person's other devices, an effect that may be unexpected; Recently Deleted allows recovery for 30 days. Cancel and Delete are the available actions.

> Are you sure? &nbsp; [ Cancel ] [ OK ]

> Delete 14 photos? &nbsp; They'll be removed from all your devices. You can restore them from Recently Deleted for 30 days. &nbsp; [ Cancel ] [ Delete ]

**Requirement revealed by failure**

**Supplied facts:** This fictional product requires passwords of at least 12 characters including a number. The example communicates that existing requirement; it is not a recommended password-policy specification.

> Password [ •••••••• ] ⚠ Invalid password.

> Password At least 12 characters, including a number. [ •••••••••••• ]

**Loss unaccounted for**

**Supplied facts:** Sync stopped after 40 of 212 notes. Those 40 reached the other devices; the remainder are retained locally only. Retry is available.

> Sync failed.

> Sync stopped after 40 of 212 notes. The 40 are up to date on your other devices; the rest are still only on this one. &nbsp; [ Retry ]

**One message for four empty states**

**Supplied facts:** No invoices have been created. The list displays invoices when they are created, and the product provides an action to create the first one.

> No data.

> No invoices yet. Invoices appear here when you create them. &nbsp; [ Create your first invoice ]

**Vague status**

**Supplied facts:** The product is loading 212 notes from iCloud. No reliable duration estimate is available.

> Loading…

> Loading 212 notes from iCloud.

**A notification that points instead of tells**

**Supplied facts:** In this synthetic event, Dana Osei approved the reader's Tuesday request for Editor access to "Q3 forecast." This information is appropriate for the permitted notification preview.

> Kestrel: You have a new notification. Open the app to view it.

> Dana Osei approved your access request &nbsp; Editor on "Q3 forecast," requested Tuesday.

**Setting named for its mechanism**

**Supplied facts:** The setting lets Kestrel check for new notes while the app is closed. The product team reports that enabling it uses more battery.

> Enable background fetch daemon

> Update in the background Kestrel checks for new notes while it's closed. Uses more battery.

**Synonym churn**

**Supplied facts:** The action moves a file to a recoverable Trash folder; it does not permanently delete it. Menu, confirmation, action label and status must describe that same outcome.

> Menu: *Remove.* Confirmation: *Delete this file?* Button: *Discard.* Toast: *Moved to Trash.*

> Menu: *Move to Trash.* Confirmation: *Move this file to the Trash?* Button: *Move to Trash.* Toast: *Moved to Trash.*
