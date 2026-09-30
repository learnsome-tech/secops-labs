# m05l03 · Memory Forensics: Process Trees & Injection

Module 5: Digital Forensics & Malware Triage · lesson 5.3 · Pro · [Open the lesson](https://learnsome.tech/learn/secops-course/m05l03)

**Goal:** You can read a process tree from a memory image for impossible parents, and pick out injected code by its memory protection, missing file backing and first bytes.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l03-02](m05l03-02/) | windows.pstree output, trimmed | Read along |
| [m05l03-03](m05l03-03/) | Checking parents against how Windows starts | Graded |
| [m05l03-05](m05l03-05/) | Finding injected regions the way malfind does | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Teach the checks something new

1. Add a second services.exe under explorer.exe in pstree.txt; predict which checks fire.
2. Add a rule to lineage.py: report cmd.exe or powershell.exe whose parent is services.exe.
3. In build_dumps.py make the 0x2b0000 region PAGE_EXECUTE_READ; is it still reported?
4. Set the hollowed region's e_lfanew to 0x200 and predict the verdict before running.

> **Hint:** lineage.py only knows the parents listed in PARENT; any other name passes silently.

## Check yourself

- csrss.exe and wininit.exe show a parent PID that is not in the process list. Why is that normal, when svchost.exe under explorer.exe is not?
- Why can windows.psscan show a process that windows.pslist does not?
- A private PAGE_EXECUTE_READWRITE region starts with MZ and has a PE signature at e_lfanew. What does that suggest, and what makes it look like hollowing rather than plain injection?
- Why is a headerless executable private region inside powershell.exe not enough on its own to call it injection?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
