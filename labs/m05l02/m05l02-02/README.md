# m05l02-02 · Walking a FILE record byte by byte

**Lesson:** [Disk Forensics: MFT, UsnJrnl & Prefetch](https://learnsome.tech/learn/secops-course/m05l02) (lesson 5.2, module 5: Digital Forensics & Malware Triage) · Pro  
**Check:** Graded

## Goal

You can parse MFT records and USN journal entries exported from an image, spot timestomping, and say what Prefetch adds as evidence of execution.

In the lesson: Here is a parser written against the raw bytes. A helper writes three records the way they come out of an image. First, the fixups. N T F S guards each record against a half finished write by replacing the last two bytes of every five hundred and twelve byte sector with a check value, and keeping the real bytes in an update sequence array near the start. The loop confirms each sector ends with the check value, which is how torn writes get caught, and then puts the real bytes back. Skip this and you read wrong values at every sector boundary. Next, the attribute walk: start at the offset given in the header, read each attribute's type and length, and stop at the end marker. The program prints each record's state and attribute types. Record forty three is marked deleted, yet everything in it is still readable.

## Files

- [`starter/build_ntfs.py`](starter/build_ntfs.py)
- [`starter/mft.py`](starter/mft.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-02/starter`
2. Read `mft.py` the way the lesson builds it:
   - Lines 1–2: A helper writes three records
   - Lines 3–12: First, the fixups
   - Lines 13–17: Next, the attribute walk
   - Lines 18–22: prints each record's state
3. Notes from the lesson:
   - Line 10: each sector must end in the check value, or the write was torn
4. Run it: `python3 mft.py`.
5. Check it from the repository root: `./check m05l02-02`.

## Expected output

```text
record 41 FILE in use  attrs 0x10 0x30 0x80
record 42 FILE in use  attrs 0x10 0x30 0x80
record 43 FILE deleted attrs 0x10 0x30 0x80
```

## How to check

`./check m05l02-02` copies `starter/` into a scratch directory and runs `python3 mft.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
