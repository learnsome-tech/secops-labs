# m04l03-03 · A tiny identity provider, to watch revocation work

**Lesson:** [Containment & Eradication: Host, Net & Identity](https://learnsome.tech/learn/secops-course/m04l03) (lesson 4.3, module 4: Incident Response Lifecycle & Playbooks) · Pro  
**Check:** Read along

## Goal

You can choose a containment strategy, isolate a host without leaving live attacker sessions open, show why revoking sessions and not a password reset stops a stolen token, and sweep every in-scope host before a single coordinated eradication.

In the lesson: Identity next, which is where incident teams most often get caught out. Think back to the mailbox case from lesson one. This is a deliberately small identity provider in plain Python, so we can watch the mechanism. It issues refresh tokens: the long lived tokens an app swaps for short lived access tokens. Each token carries the user and the time it was issued, signed with an H M A C over those claims, so nobody can change them without the key. The redeem function checks the signature first, then compares the token's issue time with the user's valid from time. That field is the revocation mechanism: move it forward and every token issued earlier stops working. Notice what redeem never looks at. The password.

## Files

- [`starter/idp.py`](starter/idp.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/idp.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: deliberately small identity provider
   - Lines 5–12: It issues refresh tokens
   - Lines 13–21: The redeem function
3. Notes from the lesson:
   - Line 19: valid_from is the revocation switch

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
