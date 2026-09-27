# Exercises — Threat Intelligence Platforms & STIX/TAXII Ingestion

Lesson `m01l05` · [Watch](https://learnsome.tech/courses/secops-course/watch?lesson=m01l05)

## Exercise 1: Your turn: feed and match

1. Add an indicator and an indicates relationship for 203.0.113.80. Predict match_intel.py output.
2. Set valid_until on the beacon domain to 2026-03-08T00:00:00Z and rerun the match.
3. In taxii_poll.py set added_after to the last date added you saw. Predict what comes back.
4. Change limit to 5 and predict the number of pages before running.

> **Hint**: Without the relationship, actor_of has no entry and the script raises KeyError. Eight objects at five a page is two pages.


---

© LearnSome.tech · support@iwantto.learnsome.tech
