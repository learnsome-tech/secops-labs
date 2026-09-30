# m01l03-03 · Parsed fields and a real index

**Lesson:** [SIEM Architecture: Ingestion Pipelines & Indexing](https://learnsome.tech/learn/secops-course/m01l03) (lesson 1.3, module 1: SOC Architecture & SIEM Engineering) · Free  
**Check:** Graded

## Goal

You can trace an event through a SIEM pipeline, decode syslog priority, and explain why field indexes and full text indexes each miss different evidence.

In the lesson: Now indexing. Most SIEMs keep each event two ways at once: as extracted fields, and as raw text. This script shows the field side with SQLite, whose indexes are B trees like most databases. It creates an events table, then reads a real format auth log. For each line it splits off the host, pulls the source address with a regular expression, and inserts a row. The query asks for every event from the intruder's address, and the plan helper asks SQLite how it would run that query. Run it. Without an index the plan is a scan, reading every row: fine for eight lines, hopeless for a year of logs. After the index is created the plan becomes a search on it. Four events come back. Now notice what is missing. The same intruder's sudo command has no from address in its text, so the parser never filled the field. A field search only finds what the parser understood.

## Files

- [`starter/auth.log`](starter/auth.log)
- [`starter/field_index.py`](starter/field_index.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-03/starter`
2. Read `field_index.py` the way the lesson builds it:
   - Lines 1–5: it creates an events table
   - Lines 6–11: for each line it splits off the host
   - Lines 12–15: the plan helper asks SQLite
   - Lines 16–21: run it
3. Run it: `python3 field_index.py`.
4. Check it from the repository root: `./check m01l03-03`.

## Expected output

```text
without index: SCAN events
with index:    SEARCH events USING INDEX events_src_ip (src_ip=?)
4 events from 203.0.113.9
```

## How to check

`./check m01l03-03` copies `starter/` into a scratch directory and runs `python3 field_index.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
