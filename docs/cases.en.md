# Two worked cases

**English** · [简体中文](cases.md)

## Which unemployment figure was available?

The forecast cutoff was January 15, 2023 at 23:00 UTC. The target was the January U.S. unemployment rate, the seasonally adjusted household-survey series UNRATE.

| Reference month | Initial release date | Initial value | Role at the cutoff |
| --- | --- | --- | --- |
| December 2022 | January 6, 2023 | 3.5% | Latest available full month, eligible as a historical input for this question. |
| January 2023 | February 3, 2023 | 3.4% | Became available later and can be used to check the outcome. |

The research cross-checked ALFRED's real-time and initial-release archives. The example treats a date-only release as a UTC interval wide enough to cover civil time zones. A date fully before the cutoff qualifies. An interval that straddles the cutoff returns `INDETERMINATE`. The full admission decision also depends on the series definition, the validity of that vintage at the cutoff and its source history. [ALFRED data](https://alfred.stlouisfed.org/series/downloaddata?seid=UNRATE) · [Offline example](../examples/release_cutoff.py)

## Why was a proposed factor rejected?

A separate experiment supplied Qwen3-8B with 275 monthly U.S. unemployment observations from January 1998 through November 2020. It returned `diff(UNRATE, 2)`. After the experiment's specified quarterly aggregation, the expression subtracts the average two quarters earlier from the current quarter's average.

The rule for forecasting quarter Q required every input to come from an earlier quarter. Knowing Q−2 was insufficient to compute the formula because Q itself was still unknown. The candidate also lacked the required citations to individual monthly observations. The run stopped at the candidate check, before statistical fitting, feedback or forecasts.

The first case checks when a data point could be read. The second checks when a *calculation* could have been made. [Back to the project](../README.md)
