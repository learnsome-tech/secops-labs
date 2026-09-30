# m05l04-06 · Sweeping endpoint logs for the sample's indicators

**Lesson:** [Malware Triage: Hashes, Strings & Sandboxing](https://learnsome.tech/learn/secops-course/m05l04) (lesson 5.4, module 5: Digital Forensics & Malware Triage) · Pro  
**Check:** Graded

## Goal

You can handle a suspicious file as evidence, triage it with hashes, strings and its import table, and sweep endpoint logs for the indicators it yields.

In the lesson: Now take the indicators to your own telemetry to find every host involved. The data is an export of Sysmon events from three workstations. Event one is process creation, and its Hashes field carries M D five, S H A two fifty six and the import hash when Sysmon is configured to record them. Event twenty two is a D N S query. The program first hashes the sample and sets out three indicators: that hash, the import hash from the last listing and the download domain. Then it parses the X M L with the standard library, splits the Hashes field into its parts and checks every event against every indicator. W S zero four two ran the sample and resolved the domain. W S one one seven never ran that file, but rundll thirty two resolved the same domain. W S two zero three ran a different file with the same import hash: a rebuilt variant the S H A two fifty six missed.

## Files

- [`starter/build_sample.py`](starter/build_sample.py)
- [`starter/sweep.py`](starter/sweep.py): the listing from the lesson
- [`starter/sysmon.xml`](starter/sysmon.xml)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l04/m05l04-06/starter`
2. Read `sweep.py` the way the lesson builds it:
   - Lines 1–9: sets out three indicators
   - Lines 10–17: splits the Hashes field
   - Lines 18–21: checks every event against every indicator
3. Run it: `python3 sweep.py`.
4. Check it from the repository root: `./check m05l04-06`.

## Expected output

```text
08:52:14 WS-042 event 1  SHA256 match, image invoice_0342.exe
08:52:14 WS-042 event 1  IMPHASH match, image invoice_0342.exe
08:52:15 WS-042 event 22 QueryName match, image invoice_0342.exe
09:30:05 WS-117 event 22 QueryName match, image rundll32.exe
10:11:40 WS-203 event 1  IMPHASH match, image invoice_0343.exe
```

## How to check

`./check m05l04-06` copies `starter/` into a scratch directory and runs `python3 sweep.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
