# m02l01-05 · Correlation rule: failures, then a success

**Lesson:** [Event Correlation Rules, Thresholds & Anomaly Pipelines](https://learnsome.tech/learn/secops-course/m02l01) (lesson 2.1, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Graded

## Goal

You can build threshold, correlation and baseline anomaly rules over parsed auth logs and explain what each one misses.

In the lesson: A correlation rule asks a sharper question: did a successful logon follow repeated failures from the same address? The rule remembers every failure per source. When a success arrives, it looks back ten minutes, and three or more earlier failures turn that success into an alert that names the account that got in and every account that was tried. Both attackers show up now, including the slow one, because this rule cares about order, not speed. The user J Smith, who mistyped once, stays quiet. The price is state. The rule holds ten minutes of failures for every address that has ever failed, and an internet facing host sees thousands of addresses, so real SIEM engines expire old entries and cap memory per rule.

## Files

- [`starter/auth.log`](starter/auth.log)
- [`starter/authlog.py`](starter/authlog.py)
- [`starter/correlate.py`](starter/correlate.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-05/starter`
2. Read `correlate.py` the way the lesson builds it:
   - Lines 1–7: remembers every failure per source
   - Lines 8–14: it looks back ten minutes
   - Lines 15–18: both attackers show up now
3. Run it: `python3 correlate.py`.
4. Check it from the repository root: `./check m02l01-05`.

## Expected output

```text
09:15:10 alert deploy from 203.0.113.45  after 6 failure(s), tried: admin deploy oracle root test
09:20:19 ok    jsmith from 198.51.100.23 after 1 failure(s), tried: jsmith
09:36:00 alert backup from 192.0.2.77    after 4 failure(s), tried: backup
```

## How to check

`./check m02l01-05` copies `starter/` into a scratch directory and runs `python3 correlate.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
