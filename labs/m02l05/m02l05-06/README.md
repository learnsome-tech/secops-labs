# m02l05-06 · Hash IOC, exact bytes, loose rule, real rule

**Lesson:** [YARA Rule Authoring & File Signature Matching](https://learnsome.tech/learn/secops-course/m02l05) (lesson 2.5, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Graded

## Goal

You can write a YARA rule with text, wide and hex strings and a condition that matches a malware family while rejecting clean files.

In the lesson: Now the same four files against four ways of detecting them. The hash from yesterday's incident catches variant A and nothing else. A hex string with no wildcards, copied straight from variant A, does the same, because variant B has a different key byte. The loose approach, alert if any string appears, catches both variants, but also flags the harmless updater and the support note. Those are two false positives out of four files. The real rule is the only column that is right on every row. That is the craft of rule writing: specific enough to skip clean files, general enough to survive the next build.

## Files

- [`starter/compare.py`](starter/compare.py): the listing from the lesson
- [`starter/make_samples.py`](starter/make_samples.py)
- [`starter/yara_like.py`](starter/yara_like.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-06/starter`
2. Read `compare.py` the way the lesson builds it:
   - Lines 1–5: now the same four files
   - Lines 6–7: a hex string with no wildcards
   - Lines 8–13: the loose approach
   - Lines 14–18: the real rule is the only column
3. Run it: `python3 compare.py`.
4. Check it from the repository root: `./check m02l05-06`.

## Expected output

```text
sample         sha256 IOC   exact bytes  any string   loader rule
invoice_a.exe  hit          hit          hit          hit
invoice_b.exe  -            -            hit          hit
updater.exe    -            -            hit          -
gate_help.txt  -            -            hit          -
```

## How to check

`./check m02l05-06` copies `starter/` into a scratch directory and runs `python3 compare.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
