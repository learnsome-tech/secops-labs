# Exercises — Containment & Eradication: Host, Net & Identity

Lesson `m04l03` · [Watch](https://learnsome.tech/courses/secops-course/watch?lesson=m04l03)

## Exercise 1: Break the sweep and the revocation on purpose

1. Add hosts/app03 with the attacker key under a new comment; predict sweep.sh, then run it
2. In revoke.py set valid_from before the stolen token's time. What prints, and why?
3. Add an exp claim in idp.issue and make redeem reject expired tokens; test both cases

> **Hint**: ssh-keygen -lf prints bits, fingerprint, comment and key type; only the fingerprint is tied to the key. Revocation compares issue times, so reason in timestamps.


---

© LearnSome.tech · support@iwantto.learnsome.tech
