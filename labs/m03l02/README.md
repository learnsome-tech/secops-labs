# m03l02 · Adversary Tactics, Techniques & Procedures (TTP) Mapping

Module 3: Threat Intelligence & MITRE ATT&CK Mapping · lesson 3.2 · Pro · [Open the lesson](https://learnsome.tech/learn/secops-course/m03l02)

**Goal:** You can read raw auth, web and sign-in logs, name the attack and ATT&CK technique they prove, and tell an attempt from a success.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l02-02](m03l02-02/) | Spraying or guessing? Let the auth log decide | Graded |
| [m03l02-03](m03l02-03/) | Application attacks in a web access log | Graded |
| [m03l02-06](m03l02-06/) | Impossible travel from sign-in records | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: tune and break the detectors

1. Give 203.0.113.9 failures against five new user names; predict its label, then run
2. Remove unquote() from web_attacks.py and count which hits disappear
3. Add a sign-in for bob from Singapore one hour after Paris and predict the speed
4. Write the technique ID and the proving log line for each finding

> **Hint:** The spraying label depends only on distinct accounts per source, not on time or count.

## Check yourself

- Six failures against six accounts from one address, then a success: which technique, and why is lockout no help?
- Why must the web detector URL-decode the request before matching, and what would it miss otherwise?
- The traversal request returned status 200 with about 1800 bytes. What does that suggest, and why?
- Alice signs in from London then Singapore seventy minutes later. What innocent explanation must you rule out?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
