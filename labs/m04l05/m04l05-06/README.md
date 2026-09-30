# m04l05-06 · Replaying the incident through the new rule

**Lesson:** [Post-Incident Review & Root Cause Analysis](https://learnsome.tech/learn/secops-course/m04l05) (lesson 4.5, module 4: Incident Response Lifecycle & Playbooks) · Pro  
**Check:** Graded

## Goal

You can run a blameless review from the incident timeline, find branching root causes with five whys and a fishbone, and prove a corrective detection works by replaying the incident's own logs through it.

In the lesson: The replay program turns raw auth log lines into rows. A regular expression takes the time, host, result, user and source, including the invalid user form open S S H writes for accounts that do not exist. Each file goes into a fresh SQLite table held in memory, the rule runs, and every hit is printed. Two inputs matter. The incident's own log must produce a hit, and it does: the deploy login at twenty two forty on the twenty seventh, after seven failures, about two and a half days before the alert that actually fired. A normal day's log must stay quiet, and it does, despite a colleague who mistyped twice and a scanner that failed a dozen times. It also stays quiet for five failures spread over half an hour, which is the blind spot to write down. Keep both logs beside the rule as its regression test.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/incident.log`](starter/incident.log)
- [`starter/normal-day.log`](starter/normal-day.log)
- [`starter/replay.py`](starter/replay.py): the listing from the lesson
- [`starter/success_after_failures.sql`](starter/success_after_failures.sql)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l05/m04l05-06/starter`
2. Read `replay.py` the way the lesson builds it:
   - Lines 1–6: A regular expression
   - Lines 7–15: Each file goes into
   - Lines 16–19: every hit is printed
3. Run it: `python3 replay.py incident.log normal-day.log`.
4. Check it from the repository root: `./check m04l05-06`.

## Expected output

```text
incident.log: 1 hit(s)
  2026-02-27 22:40:19 bastion01 deploy from 203.0.113.50 after 7 failures
normal-day.log: 0 hit(s)
```

## How to check

`./check m04l05-06` copies `starter/` into a scratch directory and runs `python3 replay.py incident.log normal-day.log` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
