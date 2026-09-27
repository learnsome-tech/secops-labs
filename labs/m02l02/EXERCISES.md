# Exercises — Log Parsing, Schema Normalization (OCSF/ECS) & Extraction

Lesson `m02l02` · [Watch](https://learnsome.tech/courses/secops-course/watch?lesson=m02l02)

## Exercise 1: Your turn: add a source and break a parser

1. Add a line 'Failed keyboard-interactive/pam for jsmith from 198.51.100.23 port 61030 ssh2'
2. Predict query.py's output, run it, and confirm the new failure appears in order
3. Add a second CloudTrail record with ConsoleLogin 'Success' and map it to OCSF status_id 1
4. Set the bastion zone to America/New_York and see how far the gap moves

> **Hint**: Timestamps must stay in the auth.log format 'Jul  3 10:14:20'; the regex accepts any method word.


---

© LearnSome.tech · support@iwantto.learnsome.tech
