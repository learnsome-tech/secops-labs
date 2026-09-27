# Exercises — Indicator of Compromise Extraction & Threat Hunting Feeds

Lesson `m03l03` · [Watch](https://learnsome.tech/courses/secops-course/watch?lesson=m03l03)

## Exercise 1: Your turn: harden the pipeline

1. Add two defanged IOCs to report.txt using hxxp and [:]//; predict what iocs.py prints
2. Make sweep.py skip values in feed_filter.py's KNOWN_GOOD and rerun it
3. Change TODAY to 2026-10-30 and predict which rows expire before running
4. Add a CIDR 203.0.113.0/24 feed row; decide how the IP check must change

> **Hint**: Move KNOWN_GOOD into iocs.py and filter there, so the sweep and the feed share one list.


---

© LearnSome.tech · support@iwantto.learnsome.tech
