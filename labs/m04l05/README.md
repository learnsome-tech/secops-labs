# m04l05 · Post-Incident Review & Root Cause Analysis

Module 4: Incident Response Lifecycle & Playbooks · lesson 4.5 · Pro · [Open the lesson](https://learnsome.tech/learn/secops-course/m04l05)

**Goal:** You can run a blameless review from the incident timeline, find branching root causes with five whys and a fishbone, and prove a corrective detection works by replaying the incident's own logs through it.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l05-02](m04l05-02/) | Where the hours went | Graded |
| [m04l05-03](m04l05-03/) | The five whys, allowed to branch | Read along |
| [m04l05-05](m04l05-05/) | Action two, written as a detection rule | Read along |
| [m04l05-06](m04l05-06/) | Replaying the incident through the new rule | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Test the rule and the review yourself

1. Add a burst to normal-day.log that should fire the rule; predict, then run replay.py
2. Set the rule's window to -2 minutes. Does incident.log still produce a hit? Why?
3. Add a timeline row at 10:40 for reaching the db owner by phone; rerun gaps.py

> **Hint:** The rule compares text timestamps, so keep SQLite's YYYY-MM-DD HH:MM:SS form. Gaps are measured between consecutive rows, so a new row splits one gap in two.

## Check yourself

- The review finds that an engineer enabled password login on the bastion. Why is 'human error' not an acceptable root cause?
- Why did a single five whys chain risk missing causes in this incident?
- Why replay the new rule against both the incident's log and a normal day's log?
- The longest gap in the timeline ended with the DLP alert. Why could nothing the responders did that morning shorten it?
- A similar incident happens six months later. What does that tell you about the previous review?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
