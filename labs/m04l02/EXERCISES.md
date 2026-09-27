# Exercises — Incident Triage, Severity Scoping & Communication

Lesson `m04l02` · [Watch](https://learnsome.tech/courses/secops-course/watch?lesson=m04l02)

## Exercise 1: Change the logs, predict the scope and severity

1. Append a line where app03 accepts a login from 192.0.2.30 at 09:10; predict scope.py
2. Rate the new scope in severity.py. Does the severity change? Does anything else?
3. Move the 07:58 db01 backup login to 08:55 and explain why db01 is now in scope
4. Set db01's data to proprietary, rerun severity.py; who drops off the notify list?

> **Hint**: Lines are processed in order, so a login only counts once its source is tainted. Copy an existing auth.log line and edit it so the regular expression still matches.


---

© LearnSome.tech · support@iwantto.learnsome.tech
