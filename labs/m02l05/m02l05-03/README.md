# m02l05-03 · Build four sample files to scan

**Lesson:** [YARA Rule Authoring & File Signature Matching](https://learnsome.tech/learn/secops-course/m02l05) (lesson 2.5, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Graded

## Goal

You can write a YARA rule with text, wide and hex strings and a condition that matches a malware family while rejecting clean files.

In the lesson: YARA is not installed on this machine, so everything that runs from here on is a few lines of Python that apply the same matching logic, and the samples are built in memory rather than downloaded. None of them is malware. Two are fake loaders: variant A with X O R key five A, variant B with key three C, extra padding and no PowerShell string. The updater is a harmless program that happens to contain a similar decode loop, because X O R loops are common in ordinary code. The text file is a support note that mentions the gate path. The output lists sizes and the start of each SHA two five six. Variants A and B share a family, but their hashes share nothing.

## Files

- [`starter/make_samples.py`](starter/make_samples.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-03/starter`
2. Read `make_samples.py` the way the lesson builds it:
   - Lines 1–15: two are fake loaders
   - Lines 16: the updater is a harmless program
   - Lines 17–18: the text file is a support note
   - Lines 19–22: the output lists sizes
3. Run it: `python3 make_samples.py`.
4. Check it from the repository root: `./check m02l05-03`.

## Expected output

```text
invoice_a.exe   183 bytes  sha256 7c737f2f7ee543a2...
invoice_b.exe   173 bytes  sha256 44fab07539b88295...
updater.exe      92 bytes  sha256 43649b177da763ae...
gate_help.txt    42 bytes  sha256 83b104da4d9a4132...
```

## How to check

`./check m02l05-03` copies `starter/` into a scratch directory and runs `python3 make_samples.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
