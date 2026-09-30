# m01l01-03 · The raw material: an incident timeline export

**Lesson:** [SOC Operating Models, Tiers & Key Performance Metrics](https://learnsome.tech/learn/secops-course/m01l01) (lesson 1.1, module 1: SOC Architecture & SIEM Engineering) · Free  
**Check:** Read along

## Goal

You can explain SOC tiers and operating models, compute detection and response times from case timestamps, and set a key risk indicator with agreed limits.

In the lesson: Every SOC metric starts with timestamps, so here is the raw material: six closed incidents exported from the case management system. Each row carries four times. Compromise is when the attacker first acted, which you only learn afterwards from the investigation. Alerted is when a detection fired or someone reported it. Acknowledged is when an analyst picked the case up. Contained is when the attacker lost their foothold. The source column says what raised the alarm: the endpoint agent, a SIEM rule, a user phoning the service desk, or intel. Look at the fourth row. The compromise is on the twenty sixth of February but the alert only comes on the fifth of March, and the source is intel: an outside threat intelligence report told us, not our own tooling.

## Files

- [`starter/incidents.csv`](starter/incidents.csv): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/incidents.csv` alongside the lesson.
2. Notes from the lesson:
   - Line 5: Compromised a week before anyone noticed, found by an outside report

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
