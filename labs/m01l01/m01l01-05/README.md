# m01l01-05 · A key risk indicator: silent log sources

**Lesson:** [SOC Operating Models, Tiers & Key Performance Metrics](https://learnsome.tech/learn/secops-course/m01l01) (lesson 1.1, module 1: SOC Architecture & SIEM Engineering) · Free  
**Check:** Graded

## Goal

You can explain SOC tiers and operating models, compute detection and response times from case timestamps, and set a key risk indicator with agreed limits.

In the lesson: Mean times describe incidents that already happened. A key risk indicator looks forward: it tells leadership that the chance of a bad outcome is rising before anything has gone wrong. A useful one for a SOC is log coverage, because a server that stops sending logs is a server where nothing can be detected. The script fixes the clock at eight on Monday morning and counts any host quiet for more than twenty four hours as silent. The limits table is the part leadership agrees in advance. For crown jewel systems any silent host is amber and a quarter of them is red; standard hosts get more slack. Then it reads the asset inventory, with the time each host last sent a log, and grades each class. Run the check. The payroll database has been silent since Saturday evening, which turns the crown class red, and a print server has been quiet for a week. Neither is an incident, but both are blind spots.

## Files

- [`starter/assets.csv`](starter/assets.csv)
- [`starter/log_coverage_kri.py`](starter/log_coverage_kri.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-05/starter`
2. Read `log_coverage_kri.py` the way the lesson builds it:
   - Lines 1–5: counts any host quiet
   - Lines 6–7: the limits table is the part
   - Lines 8–10: reads the asset inventory
   - Lines 11–20: grades each class
3. Run it: `python3 log_coverage_kri.py`.
4. Check it from the repository root: `./check m01l01-05`.

## Expected output

```text
crown    silent 1 of 4 (25%) red
   sql-payroll.corp.example.com
standard silent 1 of 6 (17%) amber
   print01.corp.example.com
```

## How to check

`./check m01l01-05` copies `starter/` into a scratch directory and runs `python3 log_coverage_kri.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
