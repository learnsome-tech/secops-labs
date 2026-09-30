# m02l04-04 · auditd rules that record exec and identity changes

**Lesson:** [Windows Event Logs, Sysmon & Linux Auditd Telemetry](https://learnsome.tech/learn/secops-course/m02l04) (lesson 2.4, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Read along

## Goal

You can parse Windows Security and Sysmon XML, reassemble auditd records, and write and read a Kubernetes audit policy to see who touched secrets or exec'd into pods.

In the lesson: On Linux the kernel audit system does the job Sysmon does on Windows. The auditd daemon writes what the kernel reports, and rules decide what gets reported. The first pair of rules records every execve system call, one line for sixty four bit programs and one for thirty two bit, but only for sessions with a real login user. That is the audit user id, or a u i d. It is set at login and survives sudo, so it names the human even when the process runs as root. The watch rules record writes and attribute changes to password, shadow and sudoers files. Each rule has a key, which is how you search for it later with ausearch dash k. The last line locks the rules until reboot.

## Files

- [`starter/soc.rules`](starter/soc.rules): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/soc.rules` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: the first pair of rules
   - Lines 5–9: the watch rules record writes
   - Lines 10–11: the last line locks the rules
3. Notes from the lesson:
   - Line 3: auid: the login user, unchanged by sudo or su

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l04-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
