# m05l03-02 · windows.pstree output, trimmed

**Lesson:** [Memory Forensics: Process Trees & Injection](https://learnsome.tech/learn/secops-course/m05l03) (lesson 5.3, module 5: Digital Forensics & Malware Triage) · Pro  
**Check:** Read along

## Goal

You can read a process tree from a memory image for impossible parents, and pick out injected code by its memory protection, missing file backing and first bytes.

In the lesson: This is output from windows dot pstree for the infected workstation, trimmed to four columns: process I D, parent process I D, image name and creation time. Stars mark depth in the tree. Read it the way Windows builds it. System starts smss, which starts csrss and wininit and then exits, so those two appear at the top with a parent that no longer exists. Wininit starts services and lsass. Services starts every svchost. Explorer belongs to the logged on user. Now look further down: Word starting PowerShell, a svchost under explorer, and a second lsass.

## Files

- [`starter/pstree.txt`](starter/pstree.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/pstree.txt` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1: trimmed to four columns
   - Lines 2–12: Read it the way Windows builds it
   - Lines 13–17: Now look further down

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
