# m04l02-05 · Rating the same incident before and after scoping

**Lesson:** [Incident Triage, Severity Scoping & Communication](https://learnsome.tech/learn/secops-course/m04l02) (lesson 4.2, module 4: Incident Response Lifecycle & Playbooks) · Pro  
**Check:** Graded

## Goal

You can scope an incident by following an attacker's logins across hosts, rate its severity from NIST's impact factors using a written mapping, and run stakeholder communication out of band with legal owning regulatory clocks.

In the lesson: This program applies one organisation's mapping. At the top are the data classes in order of harm, and the people each severity pulls in: the incident commander, the chief information security officer, legal, the data protection officer and the communications lead. The rating rule uses two of NIST's factors: information impact, taken from the worst data class in scope, and the count of critical services touched, standing in for functional impact. Recoverability is a judgement you add as the case develops. The last two lines rate the incident twice, first with the initial report and then with the scoped result. Look at the difference. One host with no data is severity three, and only the SOC lead hears about it. Three hosts including the customer database is severity one, and legal and the data protection officer need to be involved straight away.

## Files

- [`starter/inventory.csv`](starter/inventory.csv)
- [`starter/severity.py`](starter/severity.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l02/m04l02-05/starter`
2. Read `severity.py` the way the lesson builds it:
   - Lines 1–8: the data classes
   - Lines 9–18: The rating rule
   - Lines 19–21: rate the incident twice
3. Run it: `python3 severity.py`.
4. Check it from the repository root: `./check m04l02-05`.

## Expected output

```text
first report: 1 hosts, data none, 0 critical
  SEV3, notify SOC lead
after scoping: 3 hosts, data personal, 2 critical
  SEV1, notify IC, CISO, legal, DPO, comms lead
```

## How to check

`./check m04l02-05` copies `starter/` into a scratch directory and runs `python3 severity.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
