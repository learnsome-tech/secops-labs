# Exercises — Recovery & System Validation Testing

Lesson `m04l04` · [Watch](https://learnsome.tech/courses/secops-course/watch?lesson=m04l04)

## Exercise 1: Tighten the gate and the restore rules

1. Copy db01-rebuilt, set permitrootlogin yes in its sshd-T.txt; predict gate.sh, then run it
2. Make restore_point.py skip backups older than 2026-02-20; what should it print if none remain?
3. Add a validate.py check for any uid 0 account other than root; run it on both snapshots

> **Hint**: The gate trusts only the exit status, so every new failure must be appended to found. Compare backup times with a fixed date, never with today.


---

© LearnSome.tech · support@iwantto.learnsome.tech
