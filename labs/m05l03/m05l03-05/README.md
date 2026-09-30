# m05l03-05 · Finding injected regions the way malfind does

**Lesson:** [Memory Forensics: Process Trees & Injection](https://learnsome.tech/learn/secops-course/m05l03) (lesson 5.3, module 5: Digital Forensics & Malware Triage) · Pro  
**Check:** Graded

## Goal

You can read a process tree from a memory image for impossible parents, and pick out injected code by its memory protection, missing file backing and first bytes.

In the lesson: Volatility's windows dot malfind plugin applies this idea. Here are a few lines of Python applying the same logic to a trimmed V A D listing and the dumped bytes of each private region, so every decision is visible. The verdict function looks at the first bytes. An M Z header, with a P E signature where the header points, means a complete program lives in private memory. Bytes starting with c l d, then and r s p with minus sixteen, open many public x sixty four shellcode stubs, Metasploit's among them. Anything else needs context. The loop below skips regions that are not executable or are backed by a file, and hands the rest to the verdict. The svchost region at the usual image base holds a private P E: that is our hollowed process. The rundll thirty two region is shellcode.

## Files

- [`starter/build_dumps.py`](starter/build_dumps.py)
- [`starter/malfind.py`](starter/malfind.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-05/starter`
2. Read `malfind.py` the way the lesson builds it:
   - Lines 1–2: the dumped bytes of each private region
   - Lines 3–13: The verdict function looks at the first bytes
   - Lines 14–21: The loop below skips
3. Notes from the lesson:
   - Line 17: image-mapped or non-executable regions are skipped
4. Run it: `python3 malfind.py`.
5. Check it from the repository root: `./check m05l03-05`.

## Expected output

```text
svchost.exe 6204 0x7ff6b2d40000 PAGE_EXECUTE_READWRITE
   MZ and PE header, machine 0x8664: a whole program
powershell.exe 5388 0x1c2a0000 PAGE_EXECUTE_READWRITE
   no header: JIT output or shellcode, needs context
rundll32.exe 5460 0x2b0000 PAGE_EXECUTE_READWRITE
   opens with cld; and rsp,-16: a common x64 shellcode stub
```

## How to check

`./check m05l03-05` copies `starter/` into a scratch directory and runs `python3 malfind.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
