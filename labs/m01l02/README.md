# m01l02 · Alert Triage, False Positive Reduction & Fatigue Mitigation

Module 1: SOC Architecture & SIEM Engineering · lesson 1.2 · Free · [Open the lesson](https://learnsome.tech/learn/secops-course/m01l02)

**Goal:** You can classify alert outcomes, find the rules that fill the queue, write a scoped exclusion that does not hide attackers, and group alerts into cases.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l02-02](m01l02-02/) | Which rules fill the queue | Graded |
| [m01l02-03](m01l02-03/) | The noisy rule, and a scoped exception | Checker |
| [m01l02-04](m01l02-04/) | A broad exclusion against a scoped one | Graded |
| [m01l02-05](m01l02-05/) | Grouping alerts into cases | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: tune, then try to break it

1. In suppress.py, scope by k8s.ns.name alone. Predict which attack disappears, then run it.
2. Add an alert for a bash shell in the backup pod to falco_alerts.jsonl. Which rules hide it?
3. Set WINDOW to three hours in group_alerts.py. Predict the number of cases before running.
4. Add a column to rule_precision.py showing false positives per true positive.

> **Hint:** A namespace-only rule hides everything in backup, including the wget line. At three hours the spray is one case.

## Check yourself

- The container shell rule is mostly benign true positives while impossible travel is mostly false positives. Why do they need different fixes?
- Which alert in the suppression demo proves that the broad exclusion created a false negative, and why did the scoped one still show it?
- Why does the Falco exception for the backup job list three fields rather than just the process name?
- After grouping, the same address appears in two password spray cases. What should the analyst conclude, and what would a longer window change?
- What should you check before shipping a new exclusion, and what failure does that check catch?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
