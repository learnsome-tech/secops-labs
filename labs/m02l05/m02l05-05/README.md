# m02l05-05 · Scan the samples and report offsets

**Lesson:** [YARA Rule Authoring & File Signature Matching](https://learnsome.tech/learn/secops-course/m02l05) (lesson 2.5, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Graded

## Goal

You can write a YARA rule with text, wide and hex strings and a condition that matches a malware family while rejecting clean files.

In the lesson: The scan prints, per file, the verdict and the offset of the first hit for each string, much as the real yara command does with the dash s flag. Both variants match, even though their keys differ, because the key byte is a wildcard. Variant B has no PowerShell string, but two of three is enough. The updater hits the decode loop at the same offset as the loaders, and nothing else, so the condition rejects it. The support note contains the gate path but is not a Windows executable, so the M Z check rejects it before any string counts. Each part of the condition is there to throw away one kind of false positive.

## Files

- [`starter/make_samples.py`](starter/make_samples.py)
- [`starter/scan.py`](starter/scan.py): the listing from the lesson
- [`starter/yara_like.py`](starter/yara_like.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-05/starter`
2. Read `scan.py` the way the lesson builds it:
   - Lines 1–3: the scan prints, per file
   - Lines 4–9: the offset of the first hit
3. Run it: `python3 scan.py`.
4. Check it from the repository root: `./check m02l05-05`.

## Expected output

```text
invoice_a.exe  Loader_XorStub  $mutex@0x48 $gate@0x71 $ps@0x85 $xor@0x40
invoice_b.exe  Loader_XorStub  $mutex@0x70 $gate@0x99 $xor@0x40
updater.exe    -               $xor@0x40
gate_help.txt  -               $gate@0x20
```

## How to check

`./check m02l05-05` copies `starter/` into a scratch directory and runs `python3 scan.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
