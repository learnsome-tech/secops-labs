# m03l01-05 · The same rows squeezed into seven phases

**Lesson:** [Cyber Kill Chain vs MITRE ATT&CK Framework](https://learnsome.tech/learn/secops-course/m03l01) (lesson 3.1, module 3: Threat Intelligence & MITRE ATT&CK Mapping) · Pro  
**Check:** Graded

## Goal

You can map one intrusion onto both the Cyber Kill Chain and MITRE ATT&CK, and explain what each view reveals and hides.

In the lesson: Now the contrast. The loader from the last step lives in a module called attack, and above it is our own rough table from tactic to kill chain phase. Lockheed Martin publishes no official mapping, so treat this as a judgement, not a standard. Initial access becomes delivery, execution becomes exploitation, persistence becomes installation, and everything else falls into actions on objectives. The script prints how many rows landed in each phase and the time span they cover. Actions on objectives swallows six entries across five hours, from the task's privilege escalation to the encryption. Reconnaissance and weaponisation are empty, because they happened on the attacker's side where we had no logs. That is the blind spot for a SOC: the kill chain is detailed before the breach and coarse after it, which is exactly where analysts spend their day.

## Files

- [`starter/attack.py`](starter/attack.py)
- [`starter/enterprise-attack.json`](starter/enterprise-attack.json)
- [`starter/incident.csv`](starter/incident.csv)
- [`starter/killchain_view.py`](starter/killchain_view.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-05/starter`
2. Read `killchain_view.py` the way the lesson builds it:
   - Lines 1–9: Lockheed Martin publishes no official mapping
   - Lines 10–17: everything else falls into actions on objectives
   - Lines 18–20: prints how many rows landed in each phase
3. Run it: `python3 killchain_view.py`.
4. Check it from the repository root: `./check m03l01-05`.

## Expected output

```text
Reconnaissance        0  no evidence
Weaponization         0  no evidence
Delivery              1  08:02 to 08:02
Exploitation          3  08:05 to 08:06
Installation          1  08:06 to 08:06
Command and Control   1  08:07 to 08:07
Actions on Objectives 6  08:06 to 13:00
```

## How to check

`./check m03l01-05` copies `starter/` into a scratch directory and runs `python3 killchain_view.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
