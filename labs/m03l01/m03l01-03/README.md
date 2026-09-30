# m03l01-03 · One intrusion, ten observations

**Lesson:** [Cyber Kill Chain vs MITRE ATT&CK Framework](https://learnsome.tech/learn/secops-course/m03l01) (lesson 3.1, module 3: Threat Intelligence & MITRE ATT&CK Mapping) · Pro  
**Check:** Read along

## Goal

You can map one intrusion onto both the Cyber Kill Chain and MITRE ATT&CK, and explain what each view reveals and hides.

In the lesson: Here is the incident as the SOC wrote it up, one row per thing we can prove, each already tagged with a technique. It starts the usual way: an ISO image arrives by email, the user opens the shortcut inside it, and encoded PowerShell runs. Then a scheduled task called OneDriveSync is registered to run at every logon, and the machine starts beaconing over H T T P S once a minute. Two and a half hours later come credential dumping, a remote desktop hop to the file server, an encrypted archive of the finance share, an upload to cloud storage, and finally the files renamed and encrypted. Keep this file in mind. We are going to lay the same ten rows over both models and see what each one keeps and what each one throws away.

## Files

- [`starter/incident.csv`](starter/incident.csv): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/incident.csv` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: an ISO image arrives by email
   - Lines 5–6: a scheduled task called OneDriveSync
   - Lines 7–11: credential dumping, a remote desktop hop

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
