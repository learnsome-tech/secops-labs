# m01l03-04 · Full text search, and how an address is tokenised

**Lesson:** [SIEM Architecture: Ingestion Pipelines & Indexing](https://learnsome.tech/learn/secops-course/m01l03) (lesson 1.3, module 1: SOC Architecture & SIEM Engineering) · Free  
**Check:** Graded

## Goal

You can trace an event through a SIEM pipeline, decode syslog priority, and explain why field indexes and full text indexes each miss different evidence.

In the lesson: The raw side is a full text index, the same idea behind keyword search in Splunk and Elasticsearch: split every event into terms, and record which events contain each term. SQLite ships one called F T S five. The script loads the same auth log into it, then opens the vocabulary table to see which terms were stored for the intruder's address. Finally it runs two searches. Look at the first line of output. The address was not stored as one term. The tokenizer broke it at the dots into two hundred and three, zero, one hundred and thirteen, and nine. Quoting the address turns it into a phrase search, and combined with accepted it finds the successful login. The second search, for shadow, finds the sudo line the field query missed. When a search for an address returns nothing, check how the indexer tokenised it before concluding it never happened.

## Files

- [`starter/auth.log`](starter/auth.log)
- [`starter/fulltext.py`](starter/fulltext.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-04/starter`
2. Read `fulltext.py` the way the lesson builds it:
   - Lines 1–4: SQLite ships one called
   - Lines 5–8: loads the same auth log into it
   - Lines 9–13: opens the vocabulary table
   - Lines 14–19: finally it runs two searches
3. Run it: `python3 fulltext.py`.
4. Check it from the repository root: `./check m01l03-04`.

## Expected output

```text
terms stored for the address: ['0', '113', '203', '9']
search: "203.0.113.9" AND accepted
   bastion Accepted password for j.doe from 203.0.113.9 port 51102 ssh2
search: shadow
   bastion D=/home/j.doe ; USER=root ; COMMAND=/usr/bin/cat /etc/shadow
```

## How to check

`./check m01l03-04` copies `starter/` into a scratch directory and runs `python3 fulltext.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
