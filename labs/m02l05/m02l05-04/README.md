# m02l05-04 · YARA's matching rules in a few lines of Python

**Lesson:** [YARA Rule Authoring & File Signature Matching](https://learnsome.tech/learn/secops-course/m02l05) (lesson 2.5, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Read along

## Goal

You can write a YARA rule with text, wide and hex strings and a condition that matches a malware family while rejecting clean files.

In the lesson: This module mirrors the rule. The text helper encodes a string once as plain bytes, and again as U T F sixteen little endian when the rule says wide. Nocase becomes a case insensitive regular expression, which on bytes only folds A to Z, as YARA's nocase does. The hex helper turns each pair of hex digits into that exact byte and each double question mark into a dot, which matches any single byte. The strings table repeats the four declarations from the rule file. The rule function is the condition written out by hand: M Z at the start, size under two megabytes, the decode loop present, and at least two of the three text strings. This is not the YARA engine; it applies the same logic.

## Files

- [`starter/yara_like.py`](starter/yara_like.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/yara_like.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–6: the text helper encodes
   - Lines 7–11: the hex helper turns each pair
   - Lines 12–16: the strings table repeats
   - Lines 17–20: the rule function is the condition

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l05-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
