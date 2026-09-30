# m01l04-06 · Replaying a time based escalation

**Lesson:** [SOC Runbooks, Shift Handoffs & Escalation Paths](https://learnsome.tech/learn/secops-course/m01l04) (lesson 1.4, module 1: SOC Architecture & SIEM Engineering) · Free  
**Check:** Graded

## Goal

You can write a runbook with evidence, authority and escalation triggers, generate a shift handoff that flags risk, and replay a time based escalation against its target.

In the lesson: Here is time based escalation replayed for one real night. The policy file, in the shape most paging tools use, lists four levels, each with the minutes after the alert at which it is paged, and a target of fifteen minutes to acknowledge. The script sets when the P one alert fired and when someone finally acknowledged it. For each level it works out the page time and either prints the page or, if the acknowledgement came first, notes that the level was never paged. Last it compares the wait with the target. Run the replay. Primary, secondary and the SOC manager were all paged, and acknowledgement came thirty seven minutes after the alert, missing the target by more than twenty minutes. The review question is not who to blame. It is why two on-call phones stayed silent, and whether fifteen minute steps suit a P one at all.

## Files

- [`starter/escalate.py`](starter/escalate.py): the listing from the lesson
- [`starter/p1_escalation.json`](starter/p1_escalation.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-06/starter`
2. Read `escalate.py` the way the lesson builds it:
   - Lines 1–5: the policy file
   - Lines 6–8: sets when the P one alert fired
   - Lines 9–15: for each level it works out
   - Lines 16–21: last it compares the wait
3. Run it: `python3 escalate.py`.
4. Check it from the repository root: `./check m01l04-06`.

## Expected output

```text
02:10 level 1: page tier2 primary on-call
02:25 level 2: page tier2 secondary on-call
02:40 level 3: page SOC manager
never paged: head of security
02:47 acknowledged after 37 min, target 15 min: missed
```

## How to check

`./check m01l04-06` copies `starter/` into a scratch directory and runs `python3 escalate.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
