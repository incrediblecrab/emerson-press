---
id: user-interface.charts
layer: user-interface
version: 1.0.0
status: draft
budget: 1151
tokens: 1151
kind: overlay
medium: data
mechanics: house
elements: [chart title, axis label, unit, legend, annotation, tooltip, caption, alt text, empty state, dashboard tile]
evidence:
  - sources/apple-hig.md
  - sources/kill-ai-slop.md
---

# Interface: Charts

Every chart is an argument, and the text is where the argument is stated, or where it hides. A number with no unit, an axis that starts above zero, a smoothed line over four data points: each is a claim about the world made without saying so.

Covers the words around data — titles, axes, legends, annotations, tooltips, captions, and the sentence a reader hears when they cannot see the picture. Loads on top of a medium module, never instead of one.

## Detect

- **A title that names the variables instead of the finding.** *Revenue by Month.* The reader has to derive the point the chart was drawn to make.
- Or the opposite: a headline conclusion the data does not support — *Explosive growth* over three quarters of noise.
- **Missing units.** A y-axis reading `0, 50, 100` with no dollars, percent, count, or scale. `1.2M` with no currency. Percent of what, unstated.
- **No time frame, no source, no as-of date.** A number without a date is a rumor.
- **Percent change and percentage points confused**: 4% to 6% is two percentage points, not two percent, and not a 2% rise.
- A truncated y-axis with no note. A dual axis chosen so two lines cross.
- **Legend entries that are column names** — `rev_usd_net`, `Series 1`.
- Series ordered alphabetically or by database order rather than by value.
- **Decimals the measurement cannot support.** *48.3721% of respondents*, from a sample of 210.
- Rounded numbers stated as exact: *approximately 10,000 users* where the real figure is 9,847 and available.
- **Trend language over too few points.** *Rising*, *accelerating*, *plateauing* for three observations.
- Correlation stated as cause. *Because* where only *alongside* is supported.
- **Chartjunk carrying words**: 3-D bars, gradients, an icon per bar, a gridline for every unit, a label repeating every value already on the axis.
- Interpolation across a gap in collection, unmarked.
- A caption that describes the picture — *the blue line goes up* — instead of the finding.
- An empty chart that reads *No data* whether the query returned nothing, the filter excluded everything, or the pipeline failed.

## Write

Title the finding, in a sentence a reader could repeat: *Signups doubled after the free tier launched in March.* Where the chart is exploratory and has no finding, name the variables plainly and let the axes carry the rest.

Put the unit where the number is. `Revenue (USD, millions)`. `Response time (ms, p95)`. Say what the denominator is every time you write a percent.

Date everything. Time frame in the title or subtitle, source and as-of date in the caption or footnote.

Start a bar axis at zero, because bar length is the encoding. A line chart may crop — say so in the axis label or a note.

Name series the way the reader names them, and order them by value, by category order, or by the last point on a line, so the legend matches what the eye sees.

Round to the precision you actually have, and use the exact number when you have it. State the sample size next to any rate derived from one.

Describe change with the shape you can defend. Two points give a difference, not a trend. Say *rose* only if it did, and say by how much and over what.

Annotate the event, not the shape. A dated label on the week the outage happened explains the dip; an arrow reading *drop* does not.

Write the alt text as the finding, the range, and the outlier if there is one, not as a description of the drawing. Name the chart type first, because the encoding carries meaning here — this is the one place `accessibility`'s ban on opening with the medium does not apply. Give the underlying table to anything that cannot render the picture.

## Surfaces

**Tooltips.** One row: the category, the exact value with unit, and the comparison the chart is about. No sentence, no restatement of the axis name.

**Legends.** Cut the legend when there are two series and you can label them at the line ends. Keep the same color for the same series across every chart in a document.

**Empty and partial states.** The same four an app screen distinguishes, with one substitution: a gap in the series takes the place of *nothing left*, which time data does not have. Say which of the four you are in, and for a gap, break the line rather than drawing through it.

**Dashboards.** Every tile carries its own time frame, because readers screenshot tiles. State the refresh time. A tile whose value nobody has acted on in a quarter is decoration.

## Boundaries

Text attached to a data display, wherever it appears: a dashboard tile, a report figure, a chart on a landing page. The surrounding medium still governs — load this on top of `applications.md` or `website.md`, not instead of one.

Encoding choices — which mark, which scale, which color — are outside this module. It governs only the words: the title, the labels, the units, the annotation, the alt text. Statistical claims in running prose are `core/accuracy.md`.

## Examples

**Title names the axes, not the finding**

> Weekly Active Users by Week

> Weekly active users doubled after the free tier launched in March *n = 12 weeks. Source: product analytics, as of 6 Jul 2026.*

**Number with no unit or denominator**

> Conversion: 4.2 → 6.1 (+2%)

> Trial-to-paid conversion (% of trials started) rose from 4.2% to 6.1% between Q1 and Q2 — 1.9 percentage points, or a 45% relative increase. Q1 n = 1,204; Q2 n = 1,377.

**Trend language over two points**

> Support volume is trending sharply downward.

> Support tickets fell from 412 in May to 380 in June. Two months is not enough to call a trend.

**Precision the sample cannot support**

> 48.3721% of respondents preferred the new layout.

> 48% of respondents preferred the new layout (101 of 210, ±7 points).

**Legend from the schema**

> Series 1 &nbsp; Series 2 &nbsp; rev_usd_net

> Free &nbsp; Pro &nbsp; Enterprise

**Annotation describing the shape**

> ↓ Big drop here!

> 14 Mar: API outage, 06:00–11:20 UTC

**Alt text describing the drawing**

> A line chart with a blue line showing data over time.

> Line chart. Weekly active users, Jan–Jul 2026, rising from 4,100 to 9,200, with the steepest gain in the two weeks after the free tier launched in March and a flat stretch through June. Table follows.

**One empty message for four causes**

> No data

> No sessions match these filters. Widest available range is 1 Jan – 6 Jul 2026. &nbsp; [ Clear filters ]
