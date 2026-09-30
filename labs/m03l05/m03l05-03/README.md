# m03l05-03 · Parsing the task hidden inside the event

**Lesson:** [Detecting Persistence: Tasks, Registry & Services](https://learnsome.tech/learn/secops-course/m03l05) (lesson 3.5, module 3: Threat Intelligence & MITRE ATT&CK Mapping) · Pro  
**Check:** Graded

## Goal

You can find scheduled task, service and Run key persistence in Windows event XML, diff autostarts against a baseline, and spot Kubernetes persistence in API server audit logs.

In the lesson: The script needs two X M L namespaces, one for the event envelope and one for the task schema, plus names for the well known security identifiers. It reads the event, collects the data fields by name, and then parses the task content a second time. ElementTree has already turned the escaped text back into real X M L, so this second parse is all it takes. Then it prints the five facts. Every line of that output is a reason to worry. A service account created a task on a workstation. It runs as SYSTEM with the highest privileges, it fires at every logon, and it launches hidden PowerShell from a script in a user's AppData folder. Legitimate software installs to Program Files and rarely needs a hidden window. In ATTACK terms, this is Scheduled Task, used for persistence and privilege escalation.

## Files

- [`starter/parse_4698.py`](starter/parse_4698.py): the listing from the lesson
- [`starter/task-4698.xml`](starter/task-4698.xml)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l05/m03l05-03/starter`
2. Read `parse_4698.py` the way the lesson builds it:
   - Lines 1–6: two X M L namespaces
   - Lines 7–13: parses the task content a second time
   - Lines 14–19: prints the five facts
3. Run it: `python3 parse_4698.py`.
4. Check it from the repository root: `./check m03l05-03`.

## Expected output

```text
host    WS-114.corp.example.com
created \OneDriveSync by svc_backup
runs as SYSTEM HighestAvailable
trigger LogonTrigger
command powershell.exe -w hidden -File C:\Users\jo\AppData\sync.ps1
```

## How to check

`./check m03l05-03` copies `starter/` into a scratch directory and runs `python3 parse_4698.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
