# m04l05-03 · The five whys, allowed to branch

**Lesson:** [Post-Incident Review & Root Cause Analysis](https://learnsome.tech/learn/secops-course/m04l05) (lesson 4.5, module 4: Incident Response Lifecycle & Playbooks) · Pro  
**Check:** Read along

## Goal

You can run a blameless review from the incident timeline, find branching root causes with five whys and a fishbone, and prove a corrective detection works by replaying the incident's own logs through it.

In the lesson: Here is the heart of the written review. Each question from the timeline gets its own chain of whys. Why was the bastion login not detected? No rule alerts on a success after repeated failures. Why not? The bastion's logs never reached the SIEM. Why not? Because it was built by hand, outside the standard image, so log onboarding was skipped. A second branch asks why a guessed password worked at all, and ends at a hardening baseline nobody checks after a build. A third explains the fifty minute wait. This is the five whys technique, and its known weakness shows here: a single chain would have found one cause and stopped. Real incidents have several contributing causes, so let the questions branch, and make sure every action at the bottom has an owner, a due date and a proof.

## Files

- [`starter/review.md`](starter/review.md): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/review.md` alongside the lesson.
2. Notes from the lesson:
   - Line 6: Chain ends at something the organisation can change
   - Line 9: A second branch: a separate contributing cause
   - Line 18: Every action has an owner, a date and a proof

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l05-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
