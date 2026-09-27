# Exercises — Malware Triage: Hashes, Strings & Sandboxing

Lesson `m05l04` · [Watch](https://learnsome.tech/courses/secops-course/watch?lesson=m05l04)

## Exercise 1: Change the sample and the logs

1. In strings.py lower the minimum run from 6 to 4; how much noise appears?
2. Remove Sleep from IMPORTS in build_sample.py; predict which hashes and the imphash change.
3. Add a Sysmon event 3 with DestinationIp 198.51.100.23 and teach sweep.py to match it.
4. Decide what you would collect from WS-117 before anyone reimages it, and why.

> **Hint**: The imphash depends only on imported names and their order; file hashes depend on every byte.


---

© LearnSome.tech · support@iwantto.learnsome.tech
