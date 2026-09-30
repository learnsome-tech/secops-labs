# m02l04-02 · A Sysmon event one, as XML

**Lesson:** [Windows Event Logs, Sysmon & Linux Auditd Telemetry](https://learnsome.tech/learn/secops-course/m02l04) (lesson 2.4, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Read along

## Goal

You can parse Windows Security and Sysmon XML, reassemble auditd records, and write and read a Kubernetes audit policy to see who touched secrets or exec'd into pods.

In the lesson: This is what Sysmon writes for a process creation, trimmed and wrapped for the screen. Every Windows event has the same System block: the provider that wrote it, the event id, the time in U T C, the channel, and the computer. The provider matters, because event ids are only unique within one provider. Sysmon event one and some other product's event one mean different things. The Event Data block is a list of named Data elements, and those names differ for every event id. Here the image is certutil, a signed Windows tool, run with the url cache flag to download a file. Its parent was cmd dot exe. That parent and child pair is what a hunter reads first.

## Files

- [`starter/sysmon_event1.xml`](starter/sysmon_event1.xml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/sysmon_event1.xml` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–8: the same system block
   - Lines 9–17: the event data block is a list
   - Lines 18–19: its parent was cmd dot exe
3. Notes from the lesson:
   - Line 3: Event ids are only unique per provider
   - Line 12: certutil -urlcache: a signed tool fetching a file

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
