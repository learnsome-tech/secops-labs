# m05l01-04 · A working copy changes, and the hashes say where

**Lesson:** [Forensics Principles, Custody & Imaging](https://learnsome.tech/learn/secops-course/m05l01) (lesson 5.1, module 5: Digital Forensics & Malware Triage) · Pro  
**Check:** Graded

## Goal

You can decide what to collect first, acquire a disk image whose hashes prove it is unchanged, and keep a chain of custody with no gaps.

In the lesson: Analysis always happens on a working copy, and this listing shows why the piecewise hashes were worth keeping. It reruns the acquisition quietly, copies the image to a working file, then imitates a careless tool: it flips a single bit about a third of a mebibyte in. Mounting an image read and write, or opening it in a program that saves its own metadata, does this sort of thing without asking. Then the program checks both files block by block against the list recorded at acquisition. The evidence image matches all sixteen blocks. The working copy fails one, and we know the exact byte range. A whole image hash only tells you that something changed. Piecewise hashes tell you where, so you can show the change sits away from the data your findings rest on, or make a fresh copy from the verified image.

## Files

- [`starter/image.py`](starter/image.py)
- [`starter/make_disk.py`](starter/make_disk.py)
- [`starter/verify.py`](starter/verify.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-04/starter`
2. Read `verify.py` the way the lesson builds it:
   - Lines 1–5: copies the image to a working file
   - Lines 6–11: flips a single bit
   - Lines 12–21: checks both files block by block
3. Run it: `python3 verify.py`.
4. Check it from the repository root: `./check m05l01-04`.

## Expected output

```text
evidence.img: 16 of 16 blocks match
working.img: 15 of 16 blocks match
  block 5: bytes 327680 to 393215 differ
```

## How to check

`./check m05l01-04` copies `starter/` into a scratch directory and runs `python3 verify.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
