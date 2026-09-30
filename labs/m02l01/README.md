# m02l01 · Event Correlation Rules, Thresholds & Anomaly Pipelines

Module 2: Log Ingestion & Detection Engineering · lesson 2.1 · Pro · [Open the lesson](https://learnsome.tech/learn/secops-course/m02l01)

**Goal:** You can build threshold, correlation and baseline anomaly rules over parsed auth logs and explain what each one misses.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l01-02](m02l01-02/) | First look: count the auth log with awk | Graded |
| [m02l01-03](m02l01-03/) | Parse each line into fields once | Graded |
| [m02l01-04](m02l01-04/) | Threshold rule: five failures in a sliding window | Graded |
| [m02l01-05](m02l01-05/) | Correlation rule: failures, then a success | Graded |
| [m02l01-07](m02l01-07/) | Static limit versus per account baseline | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: move the limits and predict

1. In threshold.py set LIMIT = 3 and WINDOW to 300 seconds; predict which addresses alert, then run
2. Add two Failed password lines for jsmith just before 09:20:19; predict correlate.py, then run
3. In baseline.py only let the z score alert when today's count is at least 10; which rows change?

> **Hint:** The window test is e['ts'] - q[0] > WINDOW. correlate.py looks back LOOKBACK from each success.

## Check yourself

- 192.0.2.77 failed once every 90 seconds, then logged in. Why did the 5-in-60s threshold stay silent while the correlation rule alerted?
- Why does authlog.py put a year in front of the syslog timestamp before calling strptime?
- A static limit of 50 logons a day alerts on the deploy service account every day. What does the per-account baseline do differently, and where can it fail?
- The correlation rule fires on a colleague who mistyped three times and then logged in. Which change removes that false positive while still catching 203.0.113.45?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
