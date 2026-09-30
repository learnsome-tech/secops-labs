# m03l03-06 · Ageing and filtering a feed before use

**Lesson:** [Indicator of Compromise Extraction & Threat Hunting Feeds](https://learnsome.tech/learn/secops-course/m03l03) (lesson 3.3, module 3: Threat Intelligence & MITRE ATT&CK Mapping) · Pro  
**Check:** Graded

## Goal

You can extract and validate indicators from a threat report, sweep real proxy and endpoint logs for them, and age a feed before it reaches your SIEM.

In the lesson: Here is a feed file with those fields, and a filter that decides what goes into the SIEM watchlist. Our policy sits at the top: thirty days for an address, ninety for a domain, a year for a hash, a minimum confidence, and a small set of values we know are benign. Those numbers are a starting point for you to tune, not a standard. Every row is checked in a fixed order: known benign values go first, then age against the lifetime for its type, then confidence. The date is pinned so the output never changes. Three rows survive. The spring address and last year's loader hash have aged out, our own domain and the empty file hash are stopped by the allowlist, and a low confidence domain is dropped even though it is recent.

## Files

- [`starter/feed.csv`](starter/feed.csv)
- [`starter/feed_filter.py`](starter/feed_filter.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-06/starter`
2. Read `feed_filter.py` the way the lesson builds it:
   - Lines 1–9: Our policy sits at the top
   - Lines 10–13: known benign values go first
   - Lines 14–20: then age against the lifetime for its type
3. Run it: `python3 feed_filter.py`.
4. Check it from the repository root: `./check m03l03-06`.

## Expected output

```text
ipv4   198.51.100.23              keep
ipv4   203.0.113.14               drop: last seen 141 days ago
domain update-check.example.org   keep
domain corp.example.com           drop: known benign
domain files.example.net          drop: confidence 30
sha256 d6d0c8eb4047d89cbc0522c875 keep
sha256 a77956be47e8c23a0efaa9040a drop: last seen 403 days ago
sha256 e3b0c44298fc1c149afbf4c899 drop: known benign
```

## How to check

`./check m03l03-06` copies `starter/` into a scratch directory and runs `python3 feed_filter.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
