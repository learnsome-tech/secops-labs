# m04l05-05 · Action two, written as a detection rule

**Lesson:** [Post-Incident Review & Root Cause Analysis](https://learnsome.tech/learn/secops-course/m04l05) (lesson 4.5, module 4: Incident Response Lifecycle & Playbooks) · Pro  
**Check:** Read along

## Goal

You can run a blameless review from the incident timeline, find branching root causes with five whys and a fishbone, and prove a corrective detection works by replaying the incident's own logs through it.

In the lesson: Action two was a detection rule, and the best test of a new rule is the incident that inspired it. Here is the rule as SQL. Most SIEM query languages can express the same join, and SQLite lets us run it on this machine. For every accepted login, it counts failed logins from the same source address in the ten minutes before it, and reports the login when there are five or more. The threshold and the window are judgement calls, and the review should record them. Too short a window, and an attacker who spaces out guesses slips underneath it. Too low a threshold, and every colleague who mistypes a password twice becomes an alert.

## Files

- [`starter/success_after_failures.sql`](starter/success_after_failures.sql): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/success_after_failures.sql` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: Here is the rule
   - Lines 4–8: counts failed logins
   - Lines 9–11: five or more

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l05-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
