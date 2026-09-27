# Exercises — Windows Event Logs, Sysmon & Linux Auditd Telemetry

Lesson `m02l04` · [Watch](https://learnsome.tech/courses/secops-course/watch?lesson=m02l04)

## Exercise 1: Your turn: extend each parser

1. In winevt.py add Security 4625 with TargetUserName, Status and IpAddress, plus a sample event
2. In audit.log set auid=4294967295 on event 4521; which soc.rules line would have skipped it?
3. Add a k8s audit event: a get on secrets/payments/db-creds by jsmith; predict the output
4. Rewrite audit-policy.yaml with the catch-all first; which rules can no longer match?

> **Hint**: 4294967295 is how auditd writes an unset auid, the value daemons started at boot carry.


---

© LearnSome.tech · support@iwantto.learnsome.tech
