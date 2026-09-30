# m03l02-06 · Impossible travel from sign-in records

**Lesson:** [Adversary Tactics, Techniques & Procedures (TTP) Mapping](https://learnsome.tech/learn/secops-course/m03l02) (lesson 3.2, module 3: Threat Intelligence & MITRE ATT&CK Mapping) · Pro  
**Check:** Graded

## Goal

You can read raw auth, web and sign-in logs, name the attack and ATT&CK technique they prove, and tell an attempt from a success.

In the lesson: Impossible travel is one of the few indicators you can compute exactly. The first function is the haversine formula, the great circle distance between two sign ins on a sphere the size of the Earth. The script sorts the sign ins by user and time, then compares each pair of consecutive sign ins for the same user: distance divided by elapsed time. Anything faster than a thousand kilometres an hour is beyond an airliner's normal cruising speed, so we call it impossible. Alice went from London to Singapore in seventy minutes, which no plane can do. That maps to Valid Accounts, because somebody is using her real credentials. Bob's hop to Paris in four hours is fine. Before you escalate, check the obvious explanation: a corporate V P N or a mobile carrier can make one person appear in two countries.

## Files

- [`starter/impossible_travel.py`](starter/impossible_travel.py): the listing from the lesson
- [`starter/signins.jsonl`](starter/signins.jsonl)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-06/starter`
2. Read `impossible_travel.py` the way the lesson builds it:
   - Lines 1–10: great circle distance between two sign ins
   - Lines 11–13: sorts the sign ins by user and time
   - Lines 14–21: faster than a thousand kilometres an hour
3. Run it: `python3 impossible_travel.py`.
4. Check it from the repository root: `./check m03l02-06`.

## Expected output

```text
alice@example.com  London-Singapore 10,848 km, 9,298 km/h, impossible travel
bob@example.com    London-Paris 343 km, 86 km/h, plausible
```

## How to check

`./check m03l02-06` copies `starter/` into a scratch directory and runs `python3 impossible_travel.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
