# m02l02 · Log Parsing, Schema Normalization (OCSF/ECS) & Extraction

Module 2: Log Ingestion & Detection Engineering · lesson 2.2 · Pro · [Open the lesson](https://learnsome.tech/learn/secops-course/m02l02)

**Goal:** You can extract fields from text and JSON logs, map them onto ECS and OCSF, and catch the time zone and parse-failure bugs that break queries.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l02-02](m02l02-02/) | A CloudTrail ConsoleLogin record, trimmed | Read along |
| [m02l02-03](m02l02-03/) | Extract sshd fields into ECS names | Graded |
| [m02l02-04](m02l02-04/) | Map the CloudTrail record into the same names | Graded |
| [m02l02-05](m02l02-05/) | One query across both sources | Graded |
| [m02l02-06](m02l02-06/) | Translate ECS fields into an OCSF Authentication event | Graded |
| [m02l02-07](m02l02-07/) | The time zone bug that breaks correlation | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: add a source and break a parser

1. Add a line 'Failed keyboard-interactive/pam for jsmith from 198.51.100.23 port 61030 ssh2'
2. Predict query.py's output, run it, and confirm the new failure appears in order
3. Add a second CloudTrail record with ConsoleLogin 'Success' and map it to OCSF status_id 1
4. Set the bastion zone to America/New_York and see how far the gap moves

> **Hint:** Timestamps must stay in the auth.log format 'Jul  3 10:14:20'; the regex accepts any method word.

## Check yourself

- The bastion logs London local time with no offset, and the parser assumes UTC. What happens to a 10-minute correlation between an SSH failure and a console failure nine seconds apart?
- Why does from_sshd return None for a line it cannot parse instead of skipping it?
- A ConsoleLogin failure and a disabled-account failure both map to OCSF status_id 2. How do you keep them distinguishable?
- What does one normalised query over sshd and CloudTrail show that neither source shows alone?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
