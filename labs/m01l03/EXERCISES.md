# Exercises — SIEM Architecture: Ingestion Pipelines & Indexing

Lesson `m01l03` · [Watch](https://learnsome.tech/courses/secops-course/watch?lesson=m01l03)

## Exercise 1: Your turn: follow an event through the pipe

1. Add a line starting <165>1 to forwarded.log. Predict facility and severity, then run it.
2. In field_index.py, add a user column filled for the sudo line, then query it for j.doe.
3. In fulltext.py, search the phrase "203.0.113" and explain what else it would match.

> **Hint**: 165 is 20 times 8 plus 5: local4, notice. FACILITY has no entry for 20, so the script raises KeyError.


---

© LearnSome.tech · support@iwantto.learnsome.tech
