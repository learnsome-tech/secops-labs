# m01l04-04 · Generating the handoff from the case queue

**Lesson:** [SOC Runbooks, Shift Handoffs & Escalation Paths](https://learnsome.tech/learn/secops-course/m01l04) (lesson 1.4, module 1: SOC Architecture & SIEM Engineering) · Free  
**Check:** Graded

## Goal

You can write a runbook with evidence, authority and escalation triggers, generate a shift handoff that flags risk, and replay a time based escalation against its target.

In the lesson: This script builds the case part of the handoff from the ticketing export. It fixes the shift end at seven in the evening. The target table gives the minutes allowed from opening to containment for each severity; yours will differ, but it must be written down somewhere. It reads the open cases, then works out for each one how many minutes remain before its target at the moment of handoff. The report sorts by time left, so the most urgent case is always first, and flags any case with no next action. Run the handoff. IR sixty two has already breached by over an hour and a half, and its note says to watch sign-ins until nine, so the incoming shift inherits a breach they must explain. IR sixty one is a P one with forty minutes left, waiting on IT to confirm isolation. IR sixty three has no next action at all, which is exactly how cases get lost.

## Files

- [`starter/handoff.py`](starter/handoff.py): the listing from the lesson
- [`starter/open_cases.csv`](starter/open_cases.csv)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-04/starter`
2. Read `handoff.py` the way the lesson builds it:
   - Lines 1–4: fixes the shift end
   - Lines 5–6: the target table gives
   - Lines 7–9: it reads the open cases
   - Lines 10–14: how many minutes remain
   - Lines 15–21: the report sorts by time left
3. Run it: `python3 handoff.py`.
4. Check it from the repository root: `./check m01l04-04`.

## Expected output

```text
Handoff at 19:00, 5 open cases
IR-62 P2 breached -105 min m.reyes  Watch j.doe sign-ins until 21:00
IR-61 P1 due soon   40 min a.okafor Chase IT: laptop isolation not confirmed
IR-63 P2 on track   90 min a.okafor no next action written
IR-65 P1 on track  200 min m.reyes  Sessions revoked; user not reached yet
IR-64 P3 on track  785 min l.chen   Vendor ticket open for proxy log gap
```

## How to check

`./check m01l04-04` copies `starter/` into a scratch directory and runs `python3 handoff.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
