# m05l02-03 · Timestomping: when the two clocks disagree

**Lesson:** [Disk Forensics: MFT, UsnJrnl & Prefetch](https://learnsome.tech/learn/secops-course/m05l02) (lesson 5.2, module 5: Digital Forensics & Malware Triage) · Pro  
**Check:** Graded

## Goal

You can parse MFT records and USN journal entries exported from an image, spot timestomping, and say what Prefetch adds as evidence of execution.

In the lesson: Timestomping is an attacker setting a file's times so that a tool dropped this morning looks as if it arrived with the operating system years ago. The easy tools only reach standard information. This program reuses the parser, converts the raw sixty four bit values, which count hundred nanosecond ticks since the first of January sixteen oh one, and prints the created time from both attributes. Report dot docx agrees with itself. Update dot exe claims a standard information creation date in twenty nineteen, while its file name attribute says it was created this March, and on a file nobody has tampered with those two creation times normally agree. The second clue is precision: real timestamps carry a fraction of a second, and this one lands exactly on a whole second, which is what you get when someone types a date into a tool.

## Files

- [`starter/build_ntfs.py`](starter/build_ntfs.py)
- [`starter/mft.py`](starter/mft.py)
- [`starter/timestomp.py`](starter/timestomp.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-03/starter`
2. Read `timestomp.py` the way the lesson builds it:
   - Lines 1–7: converts the raw sixty four bit values
   - Lines 8–18: prints the created time from both attributes
   - Lines 19–22: The second clue is precision
3. Run it: `python3 timestomp.py`.
4. Check it from the repository root: `./check m05l02-03`.

## Expected output

```text
report.docx SI created 2026-02-27 14:03:51  FN created 2026-02-27 14:03:51
update.exe  SI created 2019-06-11 10:20:00  FN created 2026-03-02 08:52:14
  SI creation is earlier than FN creation
  SI time has no fraction of a second
stage.ps1   SI created 2026-03-02 08:52:11  FN created 2026-03-02 08:52:11
```

## How to check

`./check m05l02-03` copies `starter/` into a scratch directory and runs `python3 timestomp.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
