# m03l03-02 · A threat note, as it reaches you

**Lesson:** [Indicator of Compromise Extraction & Threat Hunting Feeds](https://learnsome.tech/learn/secops-course/m03l03) (lesson 3.3, module 3: Threat Intelligence & MITRE ATT&CK Mapping) · Pro  
**Check:** Read along

## Goal

You can extract and validate indicators from a threat report, sweep real proxy and endpoint logs for them, and age a feed before it reaches your SIEM.

In the lesson: This is the kind of note a partner or vendor sends. The network indicators are defanged, with brackets around the dots and h x x p instead of h t t p, so nobody clicks them and no mail filter acts on them. Our code has to reverse that. Then come the file hashes: a SHA two five six for the dropper and an M D five for stage two. Two traps sit at the bottom. The internal share and the loopback address are context, not indicators. The victim's own domain is mentioned because staff were phished there. And the last hash is a file the sandbox saw, which sounds sinister until you notice what it is. Keep that hash in mind, because it is going to cause trouble in a minute.

## Files

- [`starter/report.txt`](starter/report.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/report.txt` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–6: defanged, with brackets around the dots
   - Lines 7–9: a SHA two five six for the dropper
   - Lines 10–15: Two traps sit at the bottom

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
