---
id: user-interface.website
layer: user-interface
version: 1.1.0
status: draft
budget: 1414
tokens: 1414
kind: medium
medium: web
mechanics: house
elements: [landing page, heading, navigation, page title, link text, form, 404, consent banner, documentation]
evidence:
  - tests/sources/kill-ai-slop.md
  - tests/sources/stop-slop.md
  - tests/sources/apple-hig.md
  - tests/sources/field-guide-to-ai-slop.md
---

# Interface: Website

Pages a stranger arrives at, usually sideways, usually from a search result, usually to answer one question. Unlike an application, a website is allowed to sell, and that permission is why generated slop clusters here. The register of every other landing page is the path of least resistance, and copy written in it persuades without making one checkable claim.

Use this module for informational and persuasive pages. Working product surfaces, including anonymous checkout and booking, use `domains/user-interface/applications.md`. A login does not turn an informational page into application copy.

## Detect

- **The claim that fits any product.** Swap in a competitor's name and nothing breaks. *The modern way to X.* *Built for teams that move fast.*
- **The named marketing constructions.** *It's not just X — it's Y. Say goodbye to X. Meet your new X. Supercharge your X. Unlock the power of X. In seconds, not hours.* *Seamless, effortless, blazing fast, game-changing, next-level.*
- Dismissal as a tic: *no more standup theater*, *X, reimagined.*
- **Punchy triads set as a paragraph.** *Fast. Beautiful. Yours.*
- **The unsupported stat row.** *10k+ developers, 99.9% uptime, 24/7 support* without relevant records. Round figures can be genuine; suspicious neatness is a reason to check, not proof of fabrication.
- **A kicker above each heading, restating it**, and a full marketing sentence typeset at display size.
- Ordinals — *01, 02, 03* — over sections that have no order.
- **Badge and pill spam.** *✨ New*, *🔥 Popular*, *β Beta* as decoration. Emoji as bullet markers and heading ornaments.
- Emphasis styled so that readers mistake it for a link.
- Feature grids of interchangeable cards, each with an icon that relates to nothing.
- **Throat-clearing.** *Here's the thing. In today's fast-paced world. The truth is.*
- Untraceable testimonials, invented attribution, or logos implying a customer relationship that does not exist.
- **`Learn more` four times on one page**, pointing at four destinations.
- A 404 that apologizes and offers only the home page.
- A consent banner where *Accept All* is a button and *Reject* is a link in a submenu, or one that describes the reader's rights in language written to be skipped.
- Docs that explain the platform rather than the product, or that open with what the product is *not*.
- Text set inside an image, which is invisible to search, translation, and speech.

## Write

Say what the thing is in the first sentence, in the words the reader would search for. A stranger should be able to answer *what is this and is it for me* without scrolling.

Replace empty distinguishing claims with supported functions, mechanisms or consequences. A useful general explanation may stay. Do not invent a benchmark, customer count or mechanism to make a page sound specific. Whether a marketing claim is substantiated, and how long the substantiation lasts, is `domains/marketing.md`'s concern in every layout.

Identify what a figure measures and its relevant period or as-of date. If the record lacks those details, request them or omit the unsupported figure.

Let hierarchy come from what matters, not from size. If a kicker restates its heading, one of them is empty; delete that one.

Number only genuinely ordered things — install steps, a changelog, a migration. A feature grid has no order and numbering it makes a false claim.

Write link text that stands alone, because assistive technology and search engines both read it out of context.

Use authorized, traceable attribution for a testimonial. A documented privacy or publication-policy reason may justify a descriptive attribution; never invent a name, role or company. Attribution and material-connection disclosure are `domains/marketing.md`'s concern. Give a quote weight appropriate to the claim it actually supports rather than setting it as decoration.

Keep the page in one voice. Marketing register stops at the product boundary: the pricing page may sell, the billing settings screen may not.

Put text in text. Write for the reader first and the crawler never.

## Surfaces

**Landing page.** Give the page a clear primary purpose. Lead with what the product does, relevant evidence and the next action. Use the name-substitution test on empty claims of distinction, not on useful instructions or general explanations.

**Navigation and page titles.** Name destinations in the reader's terms. *Pricing*, *Docs* and *Changelog* are useful when they describe the actual pages; broad categories such as *Resources* are legitimate when readers understand what belongs there. A title tag should identify the page and site out of context.

**Forms.** Ask for the fewest fields that let you do the next thing. Label every field persistently, state requirements before the attempt, and say what happens after submission — who replies, and roughly when. Write a validation message as the fix rather than the fault, beside the field it belongs to: *Enter an address in the form name@example.com*, not *Invalid input*.

**Error pages.** A 404 says the page is gone and offers the two or three places the reader probably wanted, plus search. A 500 says the failure is ours and whether to retry. Neither needs a joke or an illustration of a lost astronaut.

**Consent and legal.** State the known collection, purposes and recipients plainly. As a house safeguard, give acceptance and rejection of optional processing equal weight and reach; the applicable jurisdiction and policy may impose additional requirements. Distinguish essential functions from optional tracking. Do not invent privacy promises or imply that a layout alone establishes compliance.

**Documentation.** Open with what the thing does and an appropriate example. Do not call an unrun example tested. Order material by task and identify relevant versions. Explain platform or language prerequisites when this reader needs them; link to fuller instruction instead of duplicating an unrelated tutorial.

## Boundaries

Informational and persuasive pages, including documentation, whether public or access-controlled. Settings, dashboards, checkout and other working-product tasks use `applications.md`, whether signed in or anonymous. The seam is the reader's task, not authentication or rendering technology.

Marketing claims themselves — what may be asserted, whether it is substantiated, how a testimonial is attributed — are `domains/marketing.md`, in every medium. This module governs the page: hero, kicker, badge, stat row, display type, navigation, link text and the surface conventions that go with them. A tell listed in both places is listed once as a page convention and once as a claim about the world; where they meet, the substantiation floor is not negotiable by layout.

## Examples

These independent synthetic briefs supply the facts for each revision. They do not report measurements or privacy practices of a real product.

**A claim that fits any product**

**Supplied facts:** The fictional Kestrel product turns forwarded email threads into workspace notes. Its supplied forwarding address is notes@kestrel.app. No delivery-time measurement is available.

> The modern platform for teams that move fast. Seamless, effortless, built for scale.

> Kestrel turns email threads into notes. Forward a thread to notes@kestrel.app to add it to your workspace.

**Negative parallelism plus a triad**

**Supplied facts:** This code editor supports split panes and a built-in terminal. No startup-time or comparative memory benchmark has been supplied.

> It's not just a code editor — it's a movement. Fast. Beautiful. Yours.

> A code editor with split panes and a built-in terminal.

**The invented stat row**

**Supplied facts:** The approved fictional records show 1,840 accounts as of July 31, 2026, uptime of 99.7% over the 90 days ending then, and weekday support replies usually within four hours. A status page reports the uptime record.

> 10k+ developers &nbsp; 99.9% uptime &nbsp; 24/7 support

> 1,840 accounts as of July 31, 2026 &nbsp; 99.7% uptime over the 90 days ending July 31 (status page) &nbsp; Support replies weekdays, usually within four hours

**Kicker restating its heading**

**Supplied facts:** This section documents a supported one-pass import from Jira.

> PLATFORM ## Our Platform

> ## Import from Jira in one pass

**Navigation named for the company, not the visitor**

**Supplied facts:** The four destinations are the pricing page, documentation, changelog and customer stories. The old labels obscure those destinations.

> Solutions &nbsp; Platform &nbsp; Resources &nbsp; Why Kestrel

> Pricing &nbsp; Docs &nbsp; Changelog &nbsp; Customers

**A 404 that only apologizes**

**Supplied facts:** The requested documentation route cannot be found. Its cause is unknown. Search, Changelog and API reference are available destinations.

> Oops! 🚀 Looks like you're lost in space! &nbsp; [ Go home ]

> That page could not be found. &nbsp; [ Search docs ] [ Changelog ] [ API reference ]

**A consent banner written to be skipped**

**Supplied facts:** This fictional site's sign-in cookies maintain the session. Optional analytics records which documentation pages are read and sends those data to the fictional processor Harbor Metrics. The supplied policy says the data are not sold. Accept and Reject control optional analytics, not the session cookies.

> We value your privacy. We and our 847 partners use cookies to enhance your experience. &nbsp; [ Accept All ] &nbsp; *Manage preferences*

> Sign-in cookies keep your session active. Optional analytics tells us which docs pages get read and sends those data to Harbor Metrics. We do not sell the data. &nbsp; [ Accept analytics ] [ Reject analytics ]

**Documentation that starts anywhere but the point**

**Supplied facts:** The fictional API creates and updates notes, requires bearer authentication, and lists notes through GET /v1/notes. The endpoint and request below come from the supplied API brief; the request has not been run.

> Welcome to the Kestrel documentation! In today's fast-paced development landscape, managing notes has never been more crucial.

> Kestrel's API creates and updates notes. Every request needs a bearer token. To list notes:
>
> ```bash
> curl -H "Authorization: Bearer $TOKEN" https://api.kestrel.app/v1/notes
> ```
