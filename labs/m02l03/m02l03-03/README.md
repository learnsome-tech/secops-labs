# m02l03-03 · The same matching rules in a few lines of Python

**Lesson:** [Detection as Code: Authoring & Testing Sigma Rules](https://learnsome.tech/learn/secops-course/m02l03) (lesson 2.3, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Read along

## Goal

You can read and write a Sigma rule, test it against true and false positive events, and name the log indicators behind common attack families.

In the lesson: pySigma is not installed on this machine, and a SIEM would run the converted query anyway, so this is a few lines of Python that apply the same matching rules. Nothing more is claimed for it. The modifier table covers equals, contains, starts with and ends with. A selection loops over its fields and fails as soon as one field has no matching value, which is the and between fields. Inside a field, any one listed value is enough, which is the or. Values are compared in lower case because Sigma string matching ignores case by default. The last function implements this rule's condition shape only: all selections, and no filter.

## Files

- [`starter/sigma_match.py`](starter/sigma_match.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/sigma_match.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–6: the modifier table covers equals
   - Lines 7–15: a selection loops over its fields
   - Lines 16–22: the last function implements
3. Notes from the lesson:
   - Line 12: Sigma string matches are case-insensitive by default

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
