# m04l02 · Incident Triage, Severity Scoping & Communication

Module 4: Incident Response Lifecycle & Playbooks · lesson 4.2 · Pro · [Open the lesson](https://learnsome.tech/learn/secops-course/m04l02)

**Goal:** You can scope an incident by following an attacker's logins across hosts, rate its severity from NIST's impact factors using a written mapping, and run stakeholder communication out of band with legal owning regulatory clocks.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l02-02](m04l02-02/) | The asset inventory scoping depends on | Read along |
| [m04l02-03](m04l02-03/) | Following the attacker's logins from host to host | Graded |
| [m04l02-05](m04l02-05/) | Rating the same incident before and after scoping | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Change the logs, predict the scope and severity

1. Append a line where app03 accepts a login from 192.0.2.30 at 09:10; predict scope.py
2. Rate the new scope in severity.py. Does the severity change? Does anything else?
3. Move the 07:58 db01 backup login to 08:55 and explain why db01 is now in scope
4. Set db01's data to proprietary, rerun severity.py; who drops off the notify list?

> **Hint:** Lines are processed in order, so a login only counts once its source is tainted. Copy an existing auth.log line and edit it so the regular expression still matches.

## Check yourself

- The first report was one bastion host holding no data. Why would rating severity at that point have been a mistake?
- Why did the 07:58 backup login from the bastion to db01 not put db01 in scope, when the 09:03 login did?
- Which NIST impact factor captures customer records being copied out, and which captures a billing service being unavailable to all users?
- The attacker holds an administrator account. Why should the incident not be coordinated over company email or chat?
- Legal counsel issues a legal hold halfway through the incident. What does that change for the responders?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
