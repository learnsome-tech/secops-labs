# m02l01-07 · Static limit versus per account baseline

**Lesson:** [Event Correlation Rules, Thresholds & Anomaly Pipelines](https://learnsome.tech/learn/secops-course/m02l01) (lesson 2.1, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Graded

## Goal

You can build threshold, correlation and baseline anomaly rules over parsed auth logs and explain what each one misses.

In the lesson: The C S V file holds fourteen days of successful logons per account, plus today on the last row. The program works out each account's mean and standard deviation from history, then judges today twice: once against a static limit of fifty, once against a z score limit of three. Compare the two verdict columns. The static rule alerts on deploy, which is behaving normally, and stays quiet on J Smith, whose thirty one logons are far beyond anything seen before. The baseline gets both right. Two cautions before you trust it. An account with almost no variation, like backup, has a tiny standard deviation, so two extra logons in a day would score above three. Most teams therefore add a minimum count before a z score can raise an alert.

## Files

- [`starter/baseline.py`](starter/baseline.py): the listing from the lesson
- [`starter/logons_per_day.csv`](starter/logons_per_day.csv)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-07/starter`
2. Read `baseline.py` the way the lesson builds it:
   - Lines 1–7: plus today on the last row
   - Lines 8–14: works out each account's mean and standard deviation
   - Lines 15–17: judges today twice
3. Run it: `python3 baseline.py`.
4. Check it from the repository root: `./check m02l01-07`.

## Expected output

```text
account  today   mean    sd       z  static  baseline
deploy     212  201.5   8.5     1.2  alert   quiet
jsmith      31    3.6   1.2    22.4  quiet   alert
backup       1    1.1   0.4    -0.4  quiet   quiet
```

## How to check

`./check m02l01-07` copies `starter/` into a scratch directory and runs `python3 baseline.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
