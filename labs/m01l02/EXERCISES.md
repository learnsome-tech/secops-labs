# Exercises — Alert Triage, False Positive Reduction & Fatigue Mitigation

Lesson `m01l02` · [Watch](https://learnsome.tech/courses/secops-course/watch?lesson=m01l02)

## Exercise 1: Your turn: tune, then try to break it

1. In suppress.py, scope by k8s.ns.name alone. Predict which attack disappears, then run it.
2. Add an alert for a bash shell in the backup pod to falco_alerts.jsonl. Which rules hide it?
3. Set WINDOW to three hours in group_alerts.py. Predict the number of cases before running.
4. Add a column to rule_precision.py showing false positives per true positive.

> **Hint**: A namespace-only rule hides everything in backup, including the wget line. At three hours the spray is one case.


---

© LearnSome.tech · support@iwantto.learnsome.tech
