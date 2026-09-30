# m01l05-03 · One STIX indicator, field by field

**Lesson:** [Threat Intelligence Platforms & STIX/TAXII Ingestion](https://learnsome.tech/learn/secops-course/m01l05) (lesson 1.5, module 1: SOC Architecture & SIEM Engineering) · Free  
**Check:** Read along

## Goal

You can relate threat actor types to their motives, read a STIX 2.1 indicator, poll a TAXII 2.1 collection incrementally, and match indicators against proxy logs with expiry.

In the lesson: Here is one STIX indicator exactly as it sits in a feed. The type and spec version say what it is. The identifier is the type name, two dashes and a U U I D, and every other object refers to it by that string. The pattern is the detection itself, in the STIX patterning language: square brackets around an object path, a comparison, and a value in single quotes. This one matches any domain name equal to update check dot example dot net. Valid from and valid until bound when a match means anything; after the first of June the producer no longer vouches for it. Kill chain phases place it in the attack: command and control, in the MITRE attack framework's naming. Notice what is missing: the actor. That link lives in a separate relationship object, so one indicator can be tied to several actors and reports.

## Files

- [`starter/indicator.json`](starter/indicator.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/indicator.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: the type and spec version
   - Lines 4: the identifier is the type name
   - Lines 5–10: the pattern is the detection itself
   - Lines 11–12: valid from and valid until
   - Lines 13–16: kill chain phases place it

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l05-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
