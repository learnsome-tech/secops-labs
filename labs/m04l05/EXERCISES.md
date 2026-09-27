# Exercises — Post-Incident Review & Root Cause Analysis

Lesson `m04l05` · [Watch](https://learnsome.tech/courses/secops-course/watch?lesson=m04l05)

## Exercise 1: Test the rule and the review yourself

1. Add a burst to normal-day.log that should fire the rule; predict, then run replay.py
2. Set the rule's window to -2 minutes. Does incident.log still produce a hit? Why?
3. Add a timeline row at 10:40 for reaching the db owner by phone; rerun gaps.py

> **Hint**: The rule compares text timestamps, so keep SQLite's YYYY-MM-DD HH:MM:SS form. Gaps are measured between consecutive rows, so a new row splits one gap in two.


---

© LearnSome.tech · support@iwantto.learnsome.tech
