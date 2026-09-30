# m02l01-03 · Parse each line into fields once

**Lesson:** [Event Correlation Rules, Thresholds & Anomaly Pipelines](https://learnsome.tech/learn/secops-course/m02l01) (lesson 2.1, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Graded

## Goal

You can build threshold, correlation and baseline anomaly rules over parsed auth logs and explain what each one misses.

In the lesson: Every rule needs the same four facts from each line: when, which result, which account and which address. This module pulls them out with one regular expression, so no rule ever touches raw text again. The pattern anchors on the sshd tag, accepts both failed and accepted, and skips the words invalid user, which sshd inserts when the account does not exist on the box. Next, the timestamp. Syslog timestamps carry no year, so the parser supplies one; without it, Python assumes nineteen hundred and a log that spans New Year sorts December after January. Running the module on its own prints the first three parsed attempts. That quick look is how you check a parser before you trust any alert built on top of it.

## Files

- [`starter/auth.log`](starter/auth.log)
- [`starter/authlog.py`](starter/authlog.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-03/starter`
2. Read `authlog.py` the way the lesson builds it:
   - Lines 1–7: pulls them out with one regular expression
   - Lines 8–17: next, the timestamp
   - Lines 18–21: prints the first three parsed attempts
3. Notes from the lesson:
   - Line 6: sshd adds 'invalid user' when the account does not exist
4. Run it: `python3 authlog.py`.
5. Check it from the repository root: `./check m02l01-03`.

## Expected output

```text
2026-03-03 09:14:02 Failed admin 203.0.113.45
2026-03-03 09:14:07 Failed root 203.0.113.45
2026-03-03 09:14:13 Failed oracle 203.0.113.45
```

## How to check

`./check m02l01-03` copies `starter/` into a scratch directory and runs `python3 authlog.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
