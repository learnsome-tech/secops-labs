# m03l01-04 · Loading the real ATT&CK tactic mapping

**Lesson:** [Cyber Kill Chain vs MITRE ATT&CK Framework](https://learnsome.tech/learn/secops-course/m03l01) (lesson 3.1, module 3: Threat Intelligence & MITRE ATT&CK Mapping) · Pro  
**Check:** Graded

## Goal

You can map one intrusion onto both the Cyber Kill Chain and MITRE ATT&CK, and explain what each view reveals and hides.

In the lesson: This script loads a trimmed copy of the Enterprise bundle. It holds the real entries for our eleven techniques, cut down to the fields we use. For each attack pattern object, it finds the external reference from mitre attack, which carries the T number, and keeps only the phases whose kill chain name is mitre attack. Then it reads the incident file and prints each row with its tactics. Look at the scheduled task row. One observation serves three tactics at once: execution, persistence and privilege escalation. That is not a mistake in the data. A task that runs as SYSTEM at every logon really does all three jobs. A strictly ordered model has nowhere to put that fact.

## Files

- [`starter/attack_view.py`](starter/attack_view.py): the listing from the lesson
- [`starter/enterprise-attack.json`](starter/enterprise-attack.json)
- [`starter/incident.csv`](starter/incident.csv)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-04/starter`
2. Read `attack_view.py` the way the lesson builds it:
   - Lines 1–5: loads a trimmed copy of the Enterprise bundle
   - Lines 6–14: only the phases whose kill chain name is mitre attack
   - Lines 15–17: prints each row with its tactics
3. Run it: `python3 attack_view.py`.
4. Check it from the repository root: `./check m03l01-04`.

## Expected output

```text
08:02 T1566.001  initial-access
08:05 T1204.002  execution
08:05 T1059.001  execution
08:06 T1053.005  execution, persistence, privilege-escalation
08:07 T1071.001  command-and-control
10:40 T1003.001  credential-access
11:15 T1021.001  lateral-movement
11:30 T1560.001  collection
12:10 T1567.002  exfiltration
13:00 T1486      impact
```

## How to check

`./check m03l01-04` copies `starter/` into a scratch directory and runs `python3 attack_view.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
