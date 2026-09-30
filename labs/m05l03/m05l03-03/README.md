# m05l03-03 · Checking parents against how Windows starts

**Lesson:** [Memory Forensics: Process Trees & Injection](https://learnsome.tech/learn/secops-course/m05l03) (lesson 5.3, module 5: Digital Forensics & Malware Triage) · Pro  
**Check:** Graded

## Goal

You can read a process tree from a memory image for impossible parents, and pick out injected code by its memory protection, missing file backing and first bytes.

In the lesson: Eyeballing a tree works for twenty processes, not for two hundred, so encode the rules. The program reads the pstree text, strips the depth stars and keeps each process's parent, name and start time. Three checks follow. Core processes must have their expected parent: lsass and services come from wininit, svchost from services. Anything started by an Office application is reported, because a document editor launching other programs deserves a look. And processes that should exist once, lsass among them, are reported when a second copy shows up. Four lines come out, and together they sketch the attack: a document started PowerShell, and within a minute a fake svchost and a fake lsass appeared under explorer, named to blend in.

## Files

- [`starter/lineage.py`](starter/lineage.py): the listing from the lesson
- [`starter/pstree.txt`](starter/pstree.txt)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-03/starter`
2. Read `lineage.py` the way the lesson builds it:
   - Lines 1–4: encode the rules
   - Lines 5–9: strips the depth stars
   - Lines 10–19: Three checks follow
3. Run it: `python3 lineage.py`.
4. Check it from the repository root: `./check m05l03-03`.

## Expected output

```text
08:51:58 powershell.exe 5388: child of WINWORD.EXE
08:52:31 svchost.exe 6204: parent explorer.exe, expected services.exe
08:52:33 lsass.exe 6310: parent explorer.exe, expected wininit.exe
08:52:33 lsass.exe 6310: second copy, first is pid 644
```

## How to check

`./check m05l03-03` copies `starter/` into a scratch directory and runs `python3 lineage.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
