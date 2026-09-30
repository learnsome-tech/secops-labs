# m02l05-02 · A YARA rule for the loader family

**Lesson:** [YARA Rule Authoring & File Signature Matching](https://learnsome.tech/learn/secops-course/m02l05) (lesson 2.5, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Read along

## Goal

You can write a YARA rule with text, wide and hex strings and a condition that matches a malware family while rejecting clean files.

In the lesson: Here is a rule for that loader family. Meta holds author, description and date; it does not affect matching. The strings section declares four patterns. The mutex is a text string marked ascii and wide, so it matches both plain bytes and the U T F sixteen form Windows programs use, where each character is followed by a zero byte. The gate string is plain ascii. The PowerShell string adds nocase. The last one is a hex string: bytes of the decode loop, with question marks as wildcards for the register and the X O R key, which change between builds. The condition checks the first two bytes are M Z, read as the little endian number zero x five A four D, keeps files under two megabytes, and needs the loop plus any two of the three text strings.

## Files

- [`starter/loader.yar`](starter/loader.yar): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/loader.yar` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–6: meta holds author, description and date
   - Lines 7–11: the strings section declares four patterns
   - Lines 12–15: the condition checks the first two bytes
3. Notes from the lesson:
   - Line 8: wide: UTF-16LE, a zero byte after each ASCII char
   - Line 11: ?? = any byte: the register and XOR key vary

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l05-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
