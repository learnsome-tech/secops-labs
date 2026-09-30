# m01l02-05 · Grouping alerts into cases

**Lesson:** [Alert Triage, False Positive Reduction & Fatigue Mitigation](https://learnsome.tech/learn/secops-course/m01l02) (lesson 1.2, module 1: SOC Architecture & SIEM Engineering) · Free  
**Check:** Graded

## Goal

You can classify alert outcomes, find the rules that fill the queue, write a scoped exclusion that does not hide attackers, and group alerts into cases.

In the lesson: Fatigue does not only come from bad rules. A password spray against the V P N raises one alert per attempt, and twenty six alerts about one attack are twenty six chances for an analyst to stop reading. Grouping turns them into one case. The script sets a sixty minute window, then loads the alerts from the SIEM export. It builds a key from the rule name and the entity, meaning the address, user or pod the alert is about. For each alert it looks for a case with the same key whose first alert is inside the window, and joins it; otherwise it opens a new case. Run it. Thirty three alerts become five cases. Look at the last line: the same address came back after an hour and started a second case. Grouping cuts the reading, not the thinking, so the analyst still has to notice that two cases share one attacker.

## Files

- [`starter/group_alerts.py`](starter/group_alerts.py): the listing from the lesson
- [`starter/siem_alerts.jsonl`](starter/siem_alerts.jsonl)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-05/starter`
2. Read `group_alerts.py` the way the lesson builds it:
   - Lines 1–5: sets a sixty minute window
   - Lines 6–8: loads the alerts
   - Lines 9–11: builds a key from the rule name
   - Lines 12–18: for each alert it looks for
   - Lines 19–22: run it
3. Run it: `python3 group_alerts.py`.
4. Check it from the repository root: `./check m01l02-05`.

## Expected output

```text
33 alerts became 5 cases
 26 x Password spray from one IP, 203.0.113.77 from 01:50
  2 x Impossible travel sign-in, j.doe@example.com from 02:14
  1 x Impossible travel sign-in, m.lee@example.com from 02:20
  1 x Shell spawned in container, shop/web-6c9f8d7b5-x2k4q from 02:41
  3 x Password spray from one IP, 203.0.113.77 from 03:05
```

## How to check

`./check m01l02-05` copies `starter/` into a scratch directory and runs `python3 group_alerts.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
