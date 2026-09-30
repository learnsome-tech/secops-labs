# m02l03-04 · Hunt: run the rule over process creation events

**Lesson:** [Detection as Code: Authoring & Testing Sigma Rules](https://learnsome.tech/learn/secops-course/m02l03) (lesson 2.3, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Graded

## Goal

You can read and write a Sigma rule, test it against true and false positive events, and name the log indicators behind common attack families.

In the lesson: The detection block from the YAML is copied here as a Python dictionary, since the standard library has no YAML reader. Compare it with the rule line by line: same names, same modifiers, same values. The program reads five process creation events, stored one JSON object per line, the way a SIEM exports them. The output gives a verdict, the parent process and the command line. Word spawning an encoded PowerShell alerts. So does P W S H with the full parameter name, because matching ignores case. The SCCM agent is filtered out. The admin backup script is quiet. Now the last line: Word again, hidden window, encoded payload, and no alert. The attacker typed dash e c.

## Files

- [`starter/hunt.py`](starter/hunt.py): the listing from the lesson
- [`starter/process_creation.jsonl`](starter/process_creation.jsonl)
- [`starter/sigma_match.py`](starter/sigma_match.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-04/starter`
2. Read `hunt.py` the way the lesson builds it:
   - Lines 1–9: copied here as a python dictionary
   - Lines 10–16: reads five process creation events
3. Run it: `python3 hunt.py`.
4. Check it from the repository root: `./check m02l03-04`.

## Expected output

```text
alert WINWORD.EXE  powershell.exe -nop -w hidden -enc dwBoAG8AYQBtAGkA
-     CcmExec.exe  powershell.exe -NoProfile -enc RwBlAHQALQBQAHIAbwBjAGUAcwBzAA==
alert cmd.exe      pwsh.exe -EncodedCommand dwBoAG8AYQBtAGkA
-     explorer.exe powershell.exe -ExecutionPolicy Bypass -File C:\Scripts\backup.ps1
-     WINWORD.EXE  powershell.exe -w hidden -ec dwBoAG8AYQBtAGkA
```

## How to check

`./check m02l03-04` copies `starter/` into a scratch directory and runs `python3 hunt.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
