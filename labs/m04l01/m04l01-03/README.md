# m04l01-03 · The case timeline, attacker and responders together

**Lesson:** [NIST SP 800-61 Incident Lifecycle & Management](https://learnsome.tech/learn/secops-course/m04l01) (lesson 4.1, module 4: Incident Response Lifecycle & Playbooks) · Pro  
**Check:** Read along

## Goal

You can place each action in an incident on its NIST lifecycle phase, spot when new scope sends a case back to analysis, measure the incident's clocks from its timeline, and explain how training, tabletops and simulations test preparation.

In the lesson: This is the case timeline for that mailbox incident, exported from the case tool as a plain file. Every row has a time in U T C, a phase, who acted, and what happened. The first three rows are the adversary's own actions. Nobody saw them live; the analysts added them afterwards from sign-in logs, once they knew what to look for. Keep attacker activity and responder activity in one timeline, because the gap between them is the story. The first responder row is the alert from the SIEM. The analysts acknowledge it, confirm the forwarding rule, revoke the sessions and remove the rule. Then look at the row at two minutes past eleven. It records a threat hunt through sign-in logs that found the same source address using a second account. That single row changes the scope of the whole incident.

## Files

- [`starter/timeline.csv`](starter/timeline.csv): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/timeline.csv` alongside the lesson.
2. Notes from the lesson:
   - Line 2: Adversary rows are added later, from log review
   - Line 5: Detection: the moment the SOC first knew
   - Line 10: One hunt result widens the scope

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
