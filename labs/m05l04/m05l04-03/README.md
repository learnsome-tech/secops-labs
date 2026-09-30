# m05l04-03 · Strings in both encodings

**Lesson:** [Malware Triage: Hashes, Strings & Sandboxing](https://learnsome.tech/learn/secops-course/m05l04) (lesson 5.4, module 5: Digital Forensics & Malware Triage) · Pro  
**Check:** Graded

## Goal

You can handle a suspicious file as evidence, triage it with hashes, strings and its import table, and sweep endpoint logs for the indicators it yields.

In the lesson: Strings come next: pull out every run of printable characters and read what the author left behind. The program does what the strings tool does. One regular expression finds runs of six or more printable A S C I I bytes. A second finds text stored as U T F sixteen, each character followed by a zero byte, which is how Windows programs usually keep text, and which a plain A S C I I search misses entirely. Then it matches a few patterns worth an analyst's attention. Out come a download U R L, a raw I P address, a browser user agent, the registry run key used for persistence, a mutex name the malware checks so it only runs once, and a drop path under app data. Every one is a hunting lead, and the mutex and run key are good material for a YARA rule.

## Files

- [`starter/build_sample.py`](starter/build_sample.py)
- [`starter/strings.py`](starter/strings.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l04/m05l04-03/starter`
2. Read `strings.py` the way the lesson builds it:
   - Lines 1–5: runs of six or more printable
   - Lines 6–7: stored as U T F sixteen
   - Lines 8–15: matches a few patterns
   - Lines 16–20: Out come a download U R L
3. Run it: `python3 strings.py`.
4. Check it from the repository root: `./check m05l04-03`.

## Expected output

```text
16 ASCII and 3 UTF-16 strings
url        https://cdn.example.com/update/p.bin
ipv4       198.51.100.23
user agent Mozilla/5.0 (Windows NT 10.0; Win64; x64)
run key    Software\Microsoft\Windows\CurrentVersion\Run
mutex      Global\mtx-7f3a9c01
drop path  %APPDATA%\Microsoft\updsvc.exe
```

## How to check

`./check m05l04-03` copies `starter/` into a scratch directory and runs `python3 strings.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
