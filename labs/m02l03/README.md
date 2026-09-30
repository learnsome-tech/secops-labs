# m02l03 · Detection as Code: Authoring & Testing Sigma Rules

Module 2: Log Ingestion & Detection Engineering · lesson 2.3 · Pro · [Open the lesson](https://learnsome.tech/learn/secops-course/m02l03)

**Goal:** You can read and write a Sigma rule, test it against true and false positive events, and name the log indicators behind common attack families.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l03-02](m02l03-02/) | A Sigma rule for encoded PowerShell | Checker |
| [m02l03-03](m02l03-03/) | The same matching rules in a few lines of Python | Read along |
| [m02l03-04](m02l03-04/) | Hunt: run the rule over process creation events | Graded |
| [m02l03-05](m02l03-05/) | Tests catch the miss, and the over-correction | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: extend the tests, then write a rule

1. Add a test case for 'powershell.exe /enc dwBoAG8AYQBtAGkA'; predict v2's result, then run
2. Change v2 so the slash form alerts without re-breaking the ExecutionPolicy test
3. Write web.yml: category webserver, cs-uri-query|contains 'union select' and '../'
4. Translate its detection into a dict and test it on two attack and two clean URIs

> **Hint:** Add ' /enc ' style values, or read the Sigma spec for the windash modifier and mimic it.

## Check yourself

- The first rule missed 'powershell.exe -w hidden -ec ...'. Why was changing the value to ' -e' the wrong fix?
- In a Sigma selection, Image|endswith has two values and CommandLine|contains has two values in the same map. What must an event satisfy?
- Logs show 400 failed logons from one address in an hour, spread across 380 different accounts, and no lockouts. Which attack does this indicate?
- Why is the SCCM agent handled with a filter_ selection inside the rule, rather than by suppressing its alerts in the SIEM?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
