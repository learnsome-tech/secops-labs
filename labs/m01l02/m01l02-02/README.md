# m01l02-02 · Which rules fill the queue

**Lesson:** [Alert Triage, False Positive Reduction & Fatigue Mitigation](https://learnsome.tech/learn/secops-course/m01l02) (lesson 1.2, module 1: SOC Architecture & SIEM Engineering) · Free  
**Check:** Graded

## Goal

You can classify alert outcomes, find the rules that fill the queue, write a scoped exclusion that does not hide attackers, and group alerts into cases.

In the lesson: Before tuning anything, find out where the noise comes from. This script reads a month of closed alerts exported from the case system, each carrying the disposition the analyst recorded at closure, and counts dispositions per rule. Then it prints each rule sorted by how often it fired, with its precision, meaning the share that were true positives, and its share of the whole queue. Run it and read down the queue column. Two rules produce nearly four in five of all alerts. The container shell rule fired fifty eight times for one real finding, and most of the rest were benign: the same nightly job, again and again. Impossible travel is mostly false positives, which points at bad logic rather than an allowed activity. The Office rule is the opposite: few alerts, most of them real. That table tells you where an hour of tuning pays back, and it only exists if every closed alert carries a disposition.

## Files

- [`starter/closed_alerts.csv`](starter/closed_alerts.csv)
- [`starter/rule_precision.py`](starter/rule_precision.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-02/starter`
2. Read `rule_precision.py` the way the lesson builds it:
   - Lines 1–7: counts dispositions per rule
   - Lines 8–15: then it prints each rule sorted
3. Run it: `python3 rule_precision.py`.
4. Check it from the repository root: `./check m01l02-02`.

## Expected output

```text
rule                           fired  true benign false precision queue
Shell spawned in container        58     1     49     8        2%   48%
Impossible travel sign-in         37     2      5    30        5%   30%
New member of Domain Admins       12     1     11     0        8%   10%
Password spray from one IP         9     3      0     6       33%    7%
Office app spawns PowerShell       6     4      0     2       67%    5%
```

## How to check

`./check m01l02-02` copies `starter/` into a scratch directory and runs `python3 rule_precision.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
