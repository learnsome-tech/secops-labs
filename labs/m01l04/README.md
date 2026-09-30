# m01l04 · SOC Runbooks, Shift Handoffs & Escalation Paths

Module 1: SOC Architecture & SIEM Engineering · lesson 1.4 · Free · [Open the lesson](https://learnsome.tech/learn/secops-course/m01l04)

**Goal:** You can write a runbook with evidence, authority and escalation triggers, generate a shift handoff that flags risk, and replay a time based escalation against its target.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l04-02](m01l04-02/) | A runbook for MFA push fatigue | Checker |
| [m01l04-04](m01l04-04/) | Generating the handoff from the case queue | Graded |
| [m01l04-06](m01l04-06/) | Replaying a time based escalation | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: run the next shift

1. Set SHIFT_END in handoff.py to 23:00. Predict which cases change state, then run it.
2. Give IR-63 a next action, add a P1 opened at 22:50, and rerun the handoff.
3. In p1_escalation.json make each level 5 minutes apart. Who is paged before a 02:47 ack?
4. Add a runbook step for a user who is travelling, and decide where it escalates.

> **Hint:** Before you add a case, only IR-64 is on track at 23:00. Five minute steps page all four levels by 02:25.

## Check yourself

- Why does the MFA fatigue runbook tell the analyst to call the number in the HR system rather than the one in the alert?
- In the handoff report, which case is most likely to be lost overnight, and which part of the output tells you?
- What is the difference between functional and hierarchical escalation? Give one trigger for each from the runbook.
- The P1 was acknowledged after thirty seven minutes. What would you bring to the review from the replay, and what would you change first?
- Why does the share of escalations sent back as not needed belong on the SOC scorecard, and what might a value near zero mean?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
