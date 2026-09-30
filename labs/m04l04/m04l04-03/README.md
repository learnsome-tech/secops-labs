# m04l04-03 · A validator for what a clean host looks like

**Lesson:** [Recovery & System Validation Testing](https://learnsome.tech/learn/secops-course/m04l04) (lesson 4.4, module 4: Incident Response Lifecycle & Playbooks) · Pro  
**Check:** Read along

## Goal

You can choose a restore point that predates the attacker and prove it intact, gate a rebuilt host's reconnection on a scripted baseline, and weigh the benefits and costs of automating that recovery work.

In the lesson: Before a rebuilt host rejoins the network, it has to match what a clean host looks like, checked by a script rather than by eye. The expected state is at the top: which users may have a login shell, which ports may listen, and two S S H settings that must be in force. The script reads the passwd file and flags any account with a real shell that is not on the list. It then walks the socket listing, taken from ss with the T C P, listening and numeric flags, and flags any unexpected port. For S S H it reads the effective configuration printed by sshd with the capital T flag, not the config file, because settings in included files can change what the main file appears to say. Findings are printed, and the exit status is one on failure and zero on success. That exit status is what lets automation act on the result.

## Files

- [`starter/validate.py`](starter/validate.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/validate.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: The expected state
   - Lines 6–12: reads the passwd file
   - Lines 13–16: walks the socket listing
   - Lines 17–18: the effective configuration
   - Lines 19–21: the exit status is one

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l04-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
