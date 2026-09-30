# m04l01-05 · The incident's clocks, measured from the same file

**Lesson:** [NIST SP 800-61 Incident Lifecycle & Management](https://learnsome.tech/learn/secops-course/m04l01) (lesson 4.1, module 4: Incident Response Lifecycle & Playbooks) · Pro  
**Check:** Graded

## Goal

You can place each action in an incident on its NIST lifecycle phase, spot when new scope sends a case back to analysis, measure the incident's clocks from its timeline, and explain how training, tabletops and simulations test preparation.

In the lesson: The same timeline answers the questions management will ask: how long were they in, and how long did we take? Two helpers find the first and the last row of a phase. The loader turns every time into a real datetime, so subtracting two of them gives a duration. Every line is measured from the alert, except the first. Dwell before alert is two days and ten and a half hours: that is how long the attacker had before anyone knew. Triage started seventeen minutes after the alert. Now compare the next two lines. The first containment action came at fifty one minutes, but everything was contained only at one hour fifty five, when the second account was locked. Report the second number. The first one flatters the team and hides the part of the incident that nearly got missed.

## Files

- [`starter/clock.py`](starter/clock.py): the listing from the lesson
- [`starter/timeline.csv`](starter/timeline.csv)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-05/starter`
2. Read `clock.py` the way the lesson builds it:
   - Lines 1–8: two helpers
   - Lines 9–13: turns every time
   - Lines 14–20: measured from the alert
3. Run it: `python3 clock.py`.
4. Check it from the repository root: `./check m04l01-05`.

## Expected output

```text
dwell before alert     2 days, 10:33:48
alert to triage        0:17:33
alert to first contain 0:51:04
alert to all contained 1:55:51
alert to recovered     3:00:53
```

## How to check

`./check m04l01-05` copies `starter/` into a scratch directory and runs `python3 clock.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
