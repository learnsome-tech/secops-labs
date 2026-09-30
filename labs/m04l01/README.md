# m04l01 · NIST SP 800-61 Incident Lifecycle & Management

Module 4: Incident Response Lifecycle & Playbooks · lesson 4.1 · Pro · [Open the lesson](https://learnsome.tech/learn/secops-course/m04l01)

**Goal:** You can place each action in an incident on its NIST lifecycle phase, spot when new scope sends a case back to analysis, measure the incident's clocks from its timeline, and explain how training, tabletops and simulations test preparation.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l01-03](m04l01-03/) | The case timeline, attacker and responders together | Read along |
| [m04l01-04](m04l01-04/) | Walking the phases, and catching the step back | Graded |
| [m04l01-05](m04l01-05/) | The incident's clocks, measured from the same file | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Extend the incident by one more account

1. Add a hunt row at 2026-03-02T13:05:00Z finding a third account, then a containment row
2. Predict what phases.py and clock.py will print, then run both and compare
3. Put preparation first in ORDER and add a tabletop row dated 2026-02-20 at the top
4. Rerun phases.py: which move does the tabletop row get, and what follows it?

> **Hint:** Rows are read in file order, so place new rows where their time belongs. The all-contained clock uses the last containment row.

## Check yourself

- A hunt finds a second compromised account after eradication has started. Which phase does the case return to, and why?
- Why should the adversary's actions and the responders' actions sit in one timeline?
- The first containment action came at 0:51 after the alert, but the last account was contained at 1:55. Which do you report as time to contain, and why?
- What does a simulation test that a tabletop exercise does not?
- Forty failed sign-ins against one mailbox: event, adverse event or incident? What would change your answer?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
