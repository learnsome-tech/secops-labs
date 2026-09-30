# m05l04 · Malware Triage: Hashes, Strings & Sandboxing

Module 5: Digital Forensics & Malware Triage · lesson 5.4 · Pro · [Open the lesson](https://learnsome.tech/learn/secops-course/m05l04)

**Goal:** You can handle a suspicious file as evidence, triage it with hashes, strings and its import table, and sweep endpoint logs for the indicators it yields.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l04-02](m05l04-02/) | Hashes: identity, and why identity is fragile | Graded |
| [m05l04-03](m05l04-03/) | Strings in both encodings | Graded |
| [m05l04-04](m05l04-04/) | The import table and the import hash | Graded |
| [m05l04-06](m05l04-06/) | Sweeping endpoint logs for the sample's indicators | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Change the sample and the logs

1. In strings.py lower the minimum run from 6 to 4; how much noise appears?
2. Remove Sleep from IMPORTS in build_sample.py; predict which hashes and the imphash change.
3. Add a Sysmon event 3 with DestinationIp 198.51.100.23 and teach sweep.py to match it.
4. Decide what you would collect from WS-117 before anyone reimages it, and why.

> **Hint:** The imphash depends only on imported names and their order; file hashes depend on every byte.

## Check yourself

- Why should an analyst search a public scanning service by hash before uploading a suspicious file to it?
- Flipping one bit changed almost every hex digit of the SHA-256. Why does that make exact hashes good for identifying a file but poor for detecting a malware family?
- Why would an ASCII-only strings search miss the run key and the mutex in this sample?
- In the sweep, WS-117 matched only the domain and WS-203 matched only the imphash. What does each match tell you?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
