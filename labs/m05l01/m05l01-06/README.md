# m05l01-06 · The custody record for one laptop

**Lesson:** [Forensics Principles, Custody & Imaging](https://learnsome.tech/learn/secops-course/m05l01) (lesson 5.1, module 5: Digital Forensics & Malware Triage) · Pro  
**Check:** Read along

## Goal

You can decide what to collect first, acquire a disk image whose hashes prove it is unchanged, and keep a chain of custody with no gaps.

In the lesson: Here is the custody record for one item, the laptop tagged L T zero four one nine, exported from the case system. One row per handover: the time in U T C, who released it, who received it, what was done, and the first sixteen hex digits of the image hash whenever someone checked it. Read it the way opposing counsel would, row by row, asking who had the laptop between one signature and the next.

## Files

- [`starter/custody-LT-0419.csv`](starter/custody-LT-0419.csv): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/custody-LT-0419.csv` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1: One row per handover
   - Lines 2–7: Read it the way opposing counsel would

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l01-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
