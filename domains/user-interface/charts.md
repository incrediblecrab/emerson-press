---
id: user-interface.charts
layer: user-interface
version: 1.1.0
status: draft
budget: 1246
tokens: 1246
kind: overlay
standalone: true
medium: data
mechanics: house
elements: [chart title, axis label, unit, legend, annotation, tooltip, caption, alt text, empty state, dashboard tile]
evidence:
  - tests/sources/apple-hig.md
  - tests/sources/kill-ai-slop.md
---

# Interface: Charts

A chart may support a finding or let a reader explore data. Its words should make the measure and limits intelligible, not supply a conclusion the data cannot support.

Covers the words around data — titles, axes, legends, annotations, tooltips, captions, and the sentence a reader hears when they cannot see the picture. Use the relevant medium for an interface, or use this module alone for a report figure.

## Detect

- **A title that hides an intended finding.** *Revenue by Month* is suitable for exploration, but may under-explain a chart presented to support a specific conclusion.
- Or the opposite: a headline conclusion the data does not support — *Explosive growth* over three quarters of noise.
- **Missing units.** A y-axis reading `0, 50, 100` with no dollars, percent, count, or scale. `1.2M` with no currency. Percent of what, unstated.
- **Missing measurement context.** A time-varying figure needs its relevant period and source; a refresh-sensitive figure may also need an as-of date.
- **Percent change and percentage points confused**: 4% to 6% is two percentage points, not two percent, and not a 2% rise.
- A truncated y-axis with no note. A dual axis chosen so two lines cross.
- **Legend entries that are column names** — `rev_usd_net`, `Series 1`.
- Series ordered alphabetically or by database order rather than by value.
- **Decimals the measurement cannot support.** *48.3721% of respondents*, from a sample of 210.
- Rounded numbers stated as exact: *10,000 users* when the recorded count is 9,847. *About 10,000* may be an appropriate honest summary.
- **Long-run trend or acceleration claims from an inadequate series.** A difference between observed dates does not by itself establish a continuing trend.
- Correlation stated as cause. *Because* where only *alongside* is supported.
- **Chartjunk carrying words**: 3-D bars, gradients, an icon per bar, a gridline for every unit, a label repeating every value already on the axis.
- Interpolation across a gap in collection, unmarked.
- A caption that describes the picture — *the blue line goes up* — instead of the finding.
- An empty chart that reads *No data* whether the query returned nothing, the filter excluded everything, or the pipeline failed.

## Write

Title the finding, in a sentence a reader could repeat: *Signups doubled after the free tier launched in March.* Where the chart is exploratory and has no finding, name the variables plainly and let the axes carry the rest.

Put the unit where the number is. `Revenue (USD, millions)`. `Response time (ms, p95)`. Say what the denominator is every time you write a percent.

Identify the relevant period, source and, where needed, as-of date in the title, caption or associated description. Ask for missing context rather than inventing it; static quantities do not need a fabricated refresh date.

Flag a misleading encoding as a design issue, not something a stronger headline fixes. A bar's length normally needs a zero baseline; a line chart can use a restricted range when clearly shown. Explain relevant breaks or limits without implying that copy has changed the chart.

Name series the way the reader names them, and order them by value, by category order, or by the last point on a line, so the legend matches what the eye sees.

Match precision to the measurement and the reader's task. Use an exact count where useful; mark a rounded approximation honestly. State a known sample size or denominator when needed to interpret a rate. Never add a sample, confidence interval, population claim or sampling assumption that the evidence does not supply.

Describe change with the shape you can defend. Two points give a difference, not a trend. Say *rose* only if it did, and say by how much and over what.

Annotate a relevant documented event, not merely the shape. An outage label may supply context for a dip, but coincident timing alone does not establish its cause.

Write the alt text as the finding, the range, and the outlier if there is one, not as a description of the drawing. Name the chart type first, because the encoding carries meaning here — this is the one place `accessibility`'s ban on opening with the medium does not apply. Give the underlying table to anything that cannot render the picture.

## Surfaces

**Tooltips.** One row: the category, the exact value with unit, and the comparison the chart is about. No sentence, no restatement of the axis name.

**Legends.** Cut the legend when there are two series and you can label them at the line ends. Keep the same color for the same series across every chart in a document.

**Empty and partial states.** The same four an app screen distinguishes, with one substitution: a gap in the series takes the place of *nothing left*, which time data does not have. Say which of the four you are in, and for a gap, break the line rather than drawing through it.

**Dashboards.** Every tile carries its own time frame, because readers screenshot tiles. State the refresh time. A tile whose value nobody has acted on in a quarter is decoration.

## Boundaries

Text attached to a data display, wherever it appears: a dashboard tile, a report figure, a chart on a landing page. For an interface, the selected `applications.md` or `website.md` module governs its surrounding surface. A report figure can load this module without either medium; its genre and citation requirements still apply.

Implementing encodings — marks, scales and colors — is outside this module. Flag dependencies that affect whether the text is truthful, but do not silently redesign the figure while claiming to copyedit it. Statistical claims in running prose are `stop-the-slop/accuracy.md`.

## Examples

These are independent synthetic data records. No sample, interval, event, source or table may be inferred merely because a caption would benefit from one.

**Title names the axes, not the finding**

**Supplied facts:** Twelve weekly product-analytics observations run from April 20 to July 6, 2026. Weekly active users rise from 4,600 to 9,200. The record is current as of July 6; no cause for the change is established.

> Weekly Active Users by Week

> Weekly active users doubled from April 20 to July 6, 2026. *12 weekly observations. Source: product analytics, as of July 6, 2026.*

**Number with no unit or denominator**

**Supplied facts:** Reported trial-to-paid conversion is 4.2% for Q1 2026 and 6.1% for Q2, each rounded to one decimal place. Denominators are 1,204 and 1,377 trials started in those quarters, respectively.

> Conversion: 4.2 → 6.1 (+2%)

> Trial-to-paid conversion (% of trials started) rose from 4.2% in Q1 2026 to 6.1% in Q2 — about 1.9 percentage points, or about a 45% relative increase based on the rounded rates. Q1 n = 1,204; Q2 n = 1,377.

**Trend language over two points**

**Supplied facts:** The supplied support record contains 412 tickets in May and 380 in June. It provides no longer series or forecast.

> Support volume is trending sharply downward.

> Support tickets fell from 412 in May to 380 in June. Two months is not enough to call a trend.

**Precision the sample cannot support**

**Supplied facts:** 101 of 210 respondents preferred the new layout. No sampling design, population inference or uncertainty interval has been supplied. The reported count supports correcting the percentage.

> 48.3721% of respondents preferred the new layout.

> 48% of respondents preferred the new layout (101 of 210).

**Legend from the schema**

**Supplied facts:** The three series count accounts on the Free, Pro and Enterprise plans, in that order. Their internal column names are free_accounts, pro_accounts and enterprise_accounts.

> free_accounts &nbsp; pro_accounts &nbsp; enterprise_accounts

> Free &nbsp; Pro &nbsp; Enterprise

**Annotation describing the shape**

**Supplied facts:** The incident record gives an API outage on March 14 from 06:00 to 11:20 UTC. It does not establish whether that event caused the plotted decline.

> ↓ Big drop here!

> Mar 14: API outage, 06:00–11:20 UTC

**Alt text describing the drawing**

**Supplied facts:** The supplied line chart covers January–July 2026, rises from 4,100 to 9,200 weekly active users, has its steepest gain in the two weeks after a March free-tier launch and is flat through June. An accompanying data table follows the figure. Timing does not establish causation.

> A line chart with a blue line showing data over time.

> Line chart. Weekly active users, Jan–Jul 2026, rising from 4,100 to 9,200, with the steepest gain in the two weeks after the free tier launched in March and a flat stretch through June. Table follows.

**One empty message for four causes**

**Supplied facts:** The query succeeded but no sessions match the active filters. Available records run from January 1 to July 6, 2026. Clear filters is an available action.

> No data

> No sessions match these filters. Widest available range is Jan 1 – Jul 6, 2026. &nbsp; [ Clear filters ]
