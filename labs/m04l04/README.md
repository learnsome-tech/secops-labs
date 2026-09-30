# m04l04 · Recovery & System Validation Testing

Module 4: Incident Response Lifecycle & Playbooks · lesson 4.4 · Pro · [Open the lesson](https://learnsome.tech/learn/secops-course/m04l04)

**Goal:** You can choose a restore point that predates the attacker and prove it intact, gate a rebuilt host's reconnection on a scripted baseline, and weigh the benefits and costs of automating that recovery work.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l04-02](m04l04-02/) | Choosing a restore point the attacker never touched | Graded |
| [m04l04-03](m04l04-03/) | A validator for what a clean host looks like | Read along |
| [m04l04-04](m04l04-04/) | The reconnection gate: fail stays quarantined | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Tighten the gate and the restore rules

1. Copy db01-rebuilt, set permitrootlogin yes in its sshd-T.txt; predict gate.sh, then run it
2. Make restore_point.py skip backups older than 2026-02-20; what should it print if none remain?
3. Add a validate.py check for any uid 0 account other than root; run it on both snapshots

> **Hint:** The gate trusts only the exit status, so every new failure must be appended to found. Compare backup times with a fixed date, never with today.

## Check yourself

- Why is the restore point chosen from the first attacker action rather than from the time of the alert?
- The dump from 28 February predates the attacker, but its hash does not match the catalogue. What does that tell you, and why must the catalogue be stored elsewhere?
- Why does validate.py read the output of sshd -T rather than the sshd_config file?
- Why does validate.py exit with status 1 on failure instead of only printing its findings?
- What risk does the orchestration server that moves hosts between security groups introduce?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
