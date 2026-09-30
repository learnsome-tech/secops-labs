# m05l01-07 · Checking the custody record for gaps

**Lesson:** [Forensics Principles, Custody & Imaging](https://learnsome.tech/learn/secops-course/m05l01) (lesson 5.1, module 5: Digital Forensics & Malware Triage) · Pro  
**Check:** Graded

## Goal

You can decide what to collect first, acquire a disk image whose hashes prove it is unchanged, and keep a chain of custody with no gaps.

In the lesson: The checks a reviewer makes are mechanical, so here they are as a short program. It loads the rows in order and tracks the current holder, starting with the person who seized the laptop. Three rules: whoever releases the item must be the last person recorded as receiving it, times must not go backwards, and any hash written down must match the acquisition hash from earlier. Two problems come out. Row five has J Lind releasing the laptop, but no row shows the store handing it to J Lind. Row six records a hash that does not match. Either someone copied it wrongly or the image changed, and both need an explanation in the case notes before anyone relies on this item.

## Files

- [`starter/custody-LT-0419.csv`](starter/custody-LT-0419.csv)
- [`starter/custody.py`](starter/custody.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-07/starter`
2. Read `custody.py` the way the lesson builds it:
   - Lines 1–6: loads the rows in order
   - Lines 7–8: tracks the current holder
   - Lines 9–17: Three rules
3. Run it: `python3 custody.py`.
4. Check it from the repository root: `./check m05l01-07`.

## Expected output

```text
row 5: released by J. Lind, but the last recorded holder is Store 2
row 6: hash 4be0c7d2e91a5f03 does not match acquisition
6 entries checked, item now held by Store 2
```

## How to check

`./check m05l01-07` copies `starter/` into a scratch directory and runs `python3 custody.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
