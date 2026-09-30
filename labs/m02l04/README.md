# m02l04 · Windows Event Logs, Sysmon & Linux Auditd Telemetry

Module 2: Log Ingestion & Detection Engineering · lesson 2.4 · Pro · [Open the lesson](https://learnsome.tech/learn/secops-course/m02l04)

**Goal:** You can parse Windows Security and Sysmon XML, reassemble auditd records, and write and read a Kubernetes audit policy to see who touched secrets or exec'd into pods.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l04-02](m02l04-02/) | A Sysmon event one, as XML | Read along |
| [m02l04-03](m02l04-03/) | Read Security and Sysmon events with ElementTree | Graded |
| [m02l04-04](m02l04-04/) | auditd rules that record exec and identity changes | Read along |
| [m02l04-05](m02l04-05/) | Reassemble auditd records into events | Graded |
| [m02l04-07](m02l04-07/) | An audit policy that protects secrets and records exec | Checker |
| [m02l04-08](m02l04-08/) | Who touched secrets or exec'd into a pod? | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: extend each parser

1. In winevt.py add Security 4625 with TargetUserName, Status and IpAddress, plus a sample event
2. In audit.log set auid=4294967295 on event 4521; which soc.rules line would have skipped it?
3. Add a k8s audit event: a get on secrets/payments/db-creds by jsmith; predict the output
4. Rewrite audit-policy.yaml with the catch-all first; which rules can no longer match?

> **Hint:** 4294967295 is how auditd writes an unset auid, the value daemons started at boot carry.

## Check yourself

- auditd shows curl running with uid=0 and auid=1001. What does that tell you?
- Why is the Kubernetes audit policy rule for secrets set to Metadata rather than RequestResponse?
- The CI service account read a secret from 203.0.113.9 with curl, then got 403 on kube-system secrets and on nodes. Which reading is most defensible?
- In winevt.py the WANT table is keyed on (provider, event id) rather than event id alone. What would break with event id alone?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
