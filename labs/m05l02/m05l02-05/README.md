# m05l02-05 · Reading USN records from $J

**Lesson:** [Disk Forensics: MFT, UsnJrnl & Prefetch](https://learnsome.tech/learn/secops-course/m05l02) (lesson 5.2, module 5: Digital Forensics & Malware Triage) · Pro  
**Check:** Graded

## Goal

You can parse MFT records and USN journal entries exported from an image, spot timestomping, and say what Prefetch adds as evidence of execution.

In the lesson: Each record is a U S N record version two: a length, a version, the file reference, the parent's reference, the update number, a timestamp, the reason flags and the name. Dollar J is a sparse file whose start reads as zeros, so the loop skips empty space eight bytes at a time. The lower forty eight bits of the file reference are the M F T record number, which lets you join the journal back to the records parsed earlier. The output reads like a story. A PowerShell script appears, is written and closed. Update dot t m p is created, renamed to update dot exe, and just over a second later gets a basic info change, which is the timestomp we saw in the M F T. Then the script is deleted. Its M F T record said deleted; the journal says when.

## Files

- [`starter/build_ntfs.py`](starter/build_ntfs.py)
- [`starter/usn.py`](starter/usn.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-05/starter`
2. Read `usn.py` the way the lesson builds it:
   - Lines 1–8: Each record is a U S N record version two
   - Lines 9–13: skips empty space eight bytes at a time
   - Lines 14–20: The lower forty eight bits
3. Notes from the lesson:
   - Line 19: ref & 0xFFFFFFFFFFFF: MFT record number, sequence dropped
4. Run it: `python3 usn.py`.
5. Check it from the repository root: `./check m05l02-05`.

## Expected output

```text
08:52:11.402877 mft 43 stage.ps1  FILE_CREATE
08:52:11.419003 mft 43 stage.ps1  FILE_CREATE DATA_EXTEND CLOSE
08:52:14.906311 mft 42 update.tmp FILE_CREATE DATA_EXTEND CLOSE
08:52:15.117420 mft 42 update.tmp RENAME_OLD_NAME
08:52:15.117420 mft 42 update.exe RENAME_NEW_NAME CLOSE
08:52:16.530962 mft 42 update.exe BASIC_INFO_CHANGE CLOSE
08:53:02.771045 mft 43 stage.ps1  FILE_DELETE CLOSE
```

## How to check

`./check m05l02-05` copies `starter/` into a scratch directory and runs `python3 usn.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
