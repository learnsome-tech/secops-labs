# m01l01 · SOC Operating Models, Tiers & Key Performance Metrics

Module 1: SOC Architecture & SIEM Engineering · lesson 1.1 · Free · [Open the lesson](https://learnsome.tech/learn/secops-course/m01l01)

**Goal:** You can explain SOC tiers and operating models, compute detection and response times from case timestamps, and set a key risk indicator with agreed limits.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l01-03](m01l01-03/) | The raw material: an incident timeline export | Read along |
| [m01l01-04](m01l01-04/) | Mean time to detect, acknowledge and contain | Graded |
| [m01l01-05](m01l01-05/) | A key risk indicator: silent log sources | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: move the numbers

1. Add an incident to incidents.csv detected in 5 minutes. Predict the mean and median, then run.
2. Make soc_metrics.py also print the 90th percentile using statistics.quantiles.
3. Set dc02's last_log in assets.csv to 2026-03-07T12:00. Predict the crown status, then run.
4. Add a laptop class to the KRI with limits you would defend to a manager.

> **Hint:** statistics.quantiles(values, n=10)[-1] is the 90th percentile. Two of four crown hosts silent is 50%.

## Check yourself

- Why does the incident found by an outside report pull the mean time to detect so far above the median, and which would you put on the scorecard?
- A provider triages your alerts overnight but is not allowed to isolate hosts. What must be agreed before the first night-time incident, and why?
- Log coverage of crown jewel servers is a key risk indicator rather than a key performance indicator. What is the difference?
- Tier one is judged only on time to close. What behaviour do you expect, and which quality measure would expose it?
- The payroll database stopped sending logs on Saturday evening. Why is that a risk even though no alert has fired?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
