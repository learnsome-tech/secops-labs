# m01l03-02 · Receiving syslog and decoding its priority

**Lesson:** [SIEM Architecture: Ingestion Pipelines & Indexing](https://learnsome.tech/learn/secops-course/m01l03) (lesson 1.3, module 1: SOC Architecture & SIEM Engineering) · Free  
**Check:** Graded

## Goal

You can trace an event through a SIEM pipeline, decode syslog priority, and explain why field indexes and full text indexes each miss different evidence.

In the lesson: Syslog is still how most firewalls, switches and Linux hosts ship events, so start there. This program is a tiny collector and a sender in one process, talking over U D P on the loopback address. The two tables decode the priority value: every syslog message starts with a number in angle brackets, and that number is the facility times eight plus the severity. The collector binds to a free port on localhost, and the sender replays four lines from a forwarding log. The loop receives each datagram, matches the header of the newer syslog format, R F C fifty four twenty four, and splits the priority with divmod. Run it. Thirty eight decodes to auth and info: an S S H failure. Four is kernel and warning: a firewall drop. Eighty five is authpriv and notice: a sudo. The printer line has no header at all, so the collector stores it raw rather than dropping it. A pipeline that discards what it cannot parse makes gaps nobody sees.

## Files

- [`starter/collector.py`](starter/collector.py): the listing from the lesson
- [`starter/forwarded.log`](starter/forwarded.log)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-02/starter`
2. Read `collector.py` the way the lesson builds it:
   - Lines 1–5: the two tables decode the priority value
   - Lines 6–12: the collector binds to a free port
   - Lines 13–22: the loop receives each datagram
3. Run it: `python3 collector.py`.
4. Check it from the repository root: `./check m01l03-02`.

## Expected output

```text
auth.info       bastion.example.com sshd   Failed password for invalid user admi
kern.warning    fw01.example.com    kernel DROP IN=eth0 OUT= SRC=203.0.113.9 DST
authpriv.notice bastion.example.com sudo   j.doe : TTY=pts/1 ; PWD=/home/j.doe ;
no header, stored raw: printer03 paper jam in tray 2
```

## How to check

`./check m01l03-02` copies `starter/` into a scratch directory and runs `python3 collector.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
