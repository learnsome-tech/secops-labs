# m04l03 · Containment & Eradication: Host, Net & Identity

Module 4: Incident Response Lifecycle & Playbooks · lesson 4.3 · Pro · [Open the lesson](https://learnsome.tech/learn/secops-course/m04l03)

**Goal:** You can choose a containment strategy, isolate a host without leaving live attacker sessions open, show why revoking sessions and not a password reset stops a stolen token, and sweep every in-scope host before a single coordinated eradication.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l03-02](m04l03-02/) | Network isolation that actually cuts the attacker off | Read along |
| [m04l03-03](m04l03-03/) | A tiny identity provider, to watch revocation work | Read along |
| [m04l03-04](m04l03-04/) | Password reset versus session revocation | Graded |
| [m04l03-05](m04l03-05/) | Sweep every host before removing anything | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Break the sweep and the revocation on purpose

1. Add hosts/app03 with the attacker key under a new comment; predict sweep.sh, then run it
2. In revoke.py set valid_from before the stolen token's time. What prints, and why?
3. Add an exp claim in idp.issue and make redeem reject expired tokens; test both cases

> **Hint:** ssh-keygen -lf prints bits, fingerprint, comment and key type; only the fingerprint is tied to the key. Revocation compares issue times, so reason in timestamps.

## Check yourself

- An isolation ruleset begins with 'ct state established,related accept'. What does that leave working, and why does it matter?
- After the password reset, the stolen refresh token was still accepted. What did revoking sessions change that the reset did not?
- Why did the sweep match on the key fingerprint rather than the key comment?
- Why remove the bastion key, the systemd unit and the cron job in one window rather than as each is found?
- The attacker had root on db01. Why rebuild rather than delete the cron job and move on?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
