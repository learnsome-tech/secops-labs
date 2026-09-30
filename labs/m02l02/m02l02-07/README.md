# m02l02-07 · The time zone bug that breaks correlation

**Lesson:** [Log Parsing, Schema Normalization (OCSF/ECS) & Extraction](https://learnsome.tech/learn/secops-course/m02l02) (lesson 2.2, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Graded

## Goal

You can extract fields from text and JSON logs, map them onto ECS and OCSF, and catch the time zone and parse-failure bugs that break queries.

In the lesson: Here is the most common normalisation bug, shown on the same two events. The first pass pretends the bastion logs in U T C, which is what a parser does when nobody configured a zone. The second pass uses the zone the host really runs in. With the wrong assumption the sshd failure lands an hour after the console failure, and a ten minute correlation window never sees them together. With the right zone they are nine seconds apart. Syslog text carries no offset, so the fix is configuration, not code: record each host's zone at onboarding, or better, make hosts log in U T C or with an explicit offset, as the high precision timestamp option in rsyslog does.

## Files

- [`starter/auth.log`](starter/auth.log)
- [`starter/cloudtrail.json`](starter/cloudtrail.json)
- [`starter/sshd_to_ecs.py`](starter/sshd_to_ecs.py)
- [`starter/trail_to_ecs.py`](starter/trail_to_ecs.py)
- [`starter/tz_bug.py`](starter/tz_bug.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-07/starter`
2. Read `tz_bug.py` the way the lesson builds it:
   - Lines 1–9: on the same two events
   - Lines 10–12: the first pass pretends
   - Lines 13–15: with the wrong assumption
3. Run it: `python3 tz_bug.py`.
4. Check it from the repository root: `./check m02l02-07`.

## Expected output

```text
assumed UTC    sshd 2026-07-03T10:13:58Z  console 2026-07-03T09:14:07Z  gap -3591s
Europe/London  sshd 2026-07-03T09:13:58Z  console 2026-07-03T09:14:07Z  gap +9s
```

## How to check

`./check m02l02-07` copies `starter/` into a scratch directory and runs `python3 tz_bug.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
