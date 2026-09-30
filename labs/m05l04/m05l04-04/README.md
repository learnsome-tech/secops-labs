# m05l04-04 · The import table and the import hash

**Lesson:** [Malware Triage: Hashes, Strings & Sandboxing](https://learnsome.tech/learn/secops-course/m05l04) (lesson 5.4, module 5: Digital Forensics & Malware Triage) · Pro  
**Check:** Graded

## Goal

You can handle a suspicious file as evidence, triage it with hashes, strings and its import table, and sweep endpoint logs for the indicators it yields.

In the lesson: A Windows program lists the functions it needs from each D L L in its import table, and that list tells you what the program is able to do. This parser follows the real format. The D O S header's field at hex three C points to the P E header. The section table translates addresses in memory into offsets in the file. Data directory one points at the import descriptors, one per D L L, ending with an all zero entry, and each descriptor leads to the function names. OpenProcess, VirtualAllocEx, WriteProcessMemory and CreateRemoteThread together are the classic recipe for injecting code into another process, the thing you hunted in memory. The WinINet functions fetch a payload, and RegSetValueExW writes the run key. Finally the import hash: library name without its extension, a dot, the function name, all lower case, joined with commas, then M D five.

## Files

- [`starter/build_sample.py`](starter/build_sample.py)
- [`starter/imports.py`](starter/imports.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l04/m05l04-04/starter`
2. Read `imports.py` the way the lesson builds it:
   - Lines 1–6: at hex three C points
   - Lines 7–11: The section table translates
   - Lines 12–18: Data directory one points
   - Lines 19–22: Finally the import hash
3. Notes from the lesson:
   - Line 16: + 2 skips the two-byte hint in front of each name
4. Run it: `python3 imports.py`.
5. Check it from the repository root: `./check m05l04-04`.

## Expected output

```text
KERNEL32.dll OpenProcess VirtualAllocEx WriteProcessMemory CreateRemoteThread Sleep
WININET.dll InternetOpenA InternetOpenUrlA InternetReadFile
ADVAPI32.dll RegSetValueExW
imphash 82a7041495e66185c753f958d7a33f65
```

## How to check

`./check m05l04-04` copies `starter/` into a scratch directory and runs `python3 imports.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
