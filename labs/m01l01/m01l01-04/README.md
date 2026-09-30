# m01l01-04 · Mean time to detect, acknowledge and contain

**Lesson:** [SOC Operating Models, Tiers & Key Performance Metrics](https://learnsome.tech/learn/secops-course/m01l01) (lesson 1.1, module 1: SOC Architecture & SIEM Engineering) · Free  
**Check:** Graded

## Goal

You can explain SOC tiers and operating models, compute detection and response times from case timestamps, and set a key risk indicator with agreed limits.

In the lesson: This script turns those rows into the numbers most SOC scorecards open with. The minutes helper subtracts one timestamp from another and returns minutes. Next it reads the export with the standard C S V reader. The loop then measures three gaps. Time to detect runs from compromise to alert. Time to acknowledge runs from alert to pickup. Time to respond is measured here from alert to containment; some teams stop that clock at closure instead, so print your definition on the scorecard itself. For each gap it prints both the mean and the median, and the last lines name the incident with the slowest detection. Run it and compare the two columns. The mean time to detect is more than a day, yet the median is about half an hour. One incident, the one intel found, drags the mean up on its own. Report the median for the typical case and name the outliers, because each outlier is a detection gap somebody should close.

## Files

- [`starter/incidents.csv`](starter/incidents.csv)
- [`starter/soc_metrics.py`](starter/soc_metrics.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-04/starter`
2. Read `soc_metrics.py` the way the lesson builds it:
   - Lines 1–7: the minutes helper subtracts
   - Lines 8–10: reads the export with the standard
   - Lines 11–17: the loop then measures three gaps
   - Lines 18–20: the last lines name the incident
3. Run it: `python3 soc_metrics.py`.
4. Check it from the repository root: `./check m01l01-04`.

## Expected output

```text
time to detect       mean  1592 min  median   32 min
time to acknowledge  mean    24 min  median   10 min
time to contain      mean   161 min  median  144 min
slowest detection: IR-44 found by intel
```

## How to check

`./check m01l01-04` copies `starter/` into a scratch directory and runs `python3 soc_metrics.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
