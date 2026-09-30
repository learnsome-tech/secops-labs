# m02l02-02 · A CloudTrail ConsoleLogin record, trimmed

**Lesson:** [Log Parsing, Schema Normalization (OCSF/ECS) & Extraction](https://learnsome.tech/learn/secops-course/m02l02) (lesson 2.2, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Read along

## Goal

You can extract fields from text and JSON logs, map them onto ECS and OCSF, and catch the time zone and parse-failure bugs that break queries.

In the lesson: Here is the cloud half of the evidence, a CloudTrail record for a failed console sign in, trimmed to the fields that matter. CloudTrail delivers files holding a Records list, one object per A P I call. The user identity block says who: an I A M user called J Smith in the documentation account. Event time is already U T C with a Z on the end, which is a gift. The event source is signin dot amazonaws dot com and the event name is ConsoleLogin. The result is not a status code. It lives in response elements, as the word Failure, with a human reason in the error message. Nothing about this shape resembles an sshd line, and that is the whole problem.

## Files

- [`starter/cloudtrail.json`](starter/cloudtrail.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/cloudtrail.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: the user identity block says who
   - Lines 6–8: the event name is consolelogin
   - Lines 9–19: it lives in response elements
3. Notes from the lesson:
   - Line 6: Already UTC: the Z suffix means zero offset
   - Line 14: The outcome hides here, not in a status field

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
