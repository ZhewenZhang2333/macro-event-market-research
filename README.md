# Macro Events & Cross-Market Forecasting

**English** · [简体中文](README.zh-CN.md)

A widely expected rate hike and a surprise hike can have the same headline. An oil rally can signal stronger demand or a disruption in supply. **Can a forecast tell these stories apart using only what was known at the time?**

We are building a research benchmark to test that question across rates, currencies, energy, gold and equity indices. Our aim is to trace a forecast back to the public release that informed it, the mechanism it assumes and the market outcome that could prove it wrong.

[Research workflow](#research-workflow) · [Evidence so far](#evidence-so-far) · [Try the example](#try-the-example) · [Research agenda](#research-agenda)

## Research workflow

![A labor-market factor goes from a fixed question and dated evidence to a statistical model and a separate Qwen forecast.](assets/workflow-en.png)

In the November 2 labor-market experiment, the agent read a 2012 speech by Ben Bernanke and historical labor data. It proposed using the quarterly change in the labor force when payroll employment was above its trailing twelve-quarter average, and zero otherwise. A fixed program computed the feature. Logistic regression received an extra column. In a separate forecasting context, Qwen received the formula and its computed value.

That distinction mattered. An incorrect unit description reached the Qwen prompt. Logistic regression consumed the numeric column, and all 644 saved probabilities could be reproduced from its coefficients. The original Qwen forecasts still reflect the wording it saw.

## Evidence so far

| Research question | What we have checked |
| --- | --- |
| Can we match a forecast to a prediction market? | We reviewed the original rules of **30 Polymarket markets** and retrieved nonempty historical probability samples for **23**. Matching an individual forecast still requires the same question, cutoff and settlement rule. |
| Did the labor factor improve forecasts? | For the probability of a monthly rise in U.S. unemployment, adding the factor moved the Brier score from **0.2398 to 0.2351** on validation and from **0.1950 to 0.2029** on historical replay. Lower is better. |
| Can we catch a plausible-looking leak? | In a separate November 4 experiment, Qwen3-8B received **275 monthly observations**. Its proposed formula used unemployment in the very quarter being forecast. The check stopped the run before fitting. [Read the case](docs/cases.en.md) |
| What can we assess prospectively? | As of November 7, 2026, **3 of 6** frozen questions have verified outcomes. The full set awaits scoring. |

![The 2000–2019 model-fitting period contains two factor-development windows. Validation and replay follow on later historical dates.](assets/time-splits-en.png)

The validation and replay scores use 35 and 44 scorable forecast dates, respectively. Both belong to a historical experiment. Early missing windows and uncertainty about when some inputs became available still limit what these results tell us about future forecasts.

## Try the example

On January 15, 2023, which U.S. unemployment figure could a forecaster use? From the repository root, run this offline example with Python 3.11. It uses only the standard library.

```shell
python examples/release_cutoff.py
```

```text
2022-12  3.5%  BEFORE_CUTOFF
2023-01  3.4%  AFTER_CUTOFF
```

The reference month tells you what the observation describes. Its release date tells you when it could enter the forecast. [Case notes and ALFRED source](docs/cases.en.md)

## Research agenda

| Direction | What we want to learn |
| --- | --- |
| **Before an event** | Can an agent assign better-calibrated probabilities to policy decisions and macro releases than a historical baseline or a crowd pricing the same contract? We want to freeze the forecast and the comparison price before the answer is public. |
| **Across markets** | When policy or supply conditions change, which assets react, in which direction and for how long? We aim to follow the same event over weekly, monthly and event-specific horizons, including assets with no corresponding prediction market. |
| **Mechanisms under test** | We want to turn competing explanations from official texts and dated analyst commentary into testable claims. Given the same information, does a suggested mechanism add predictive value beyond a simple model? Tracking revisions and counterexamples is part of that test. |

The public repository contains worked cases, diagrams and a runnable example. A broader point-in-time dataset and a prospective comparison across markets remain research goals. Research and simulation only (`NO_ORDER`).
