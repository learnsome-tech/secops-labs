# m03l02-02 · Spraying or guessing? Let the auth log decide

**Lesson:** [Adversary Tactics, Techniques & Procedures (TTP) Mapping](https://learnsome.tech/learn/secops-course/m03l02) (lesson 3.2, module 3: Threat Intelligence & MITRE ATT&CK Mapping) · Pro  
**Check:** Graded

## Goal

You can read raw auth, web and sign-in logs, name the attack and ATT&CK technique they prove, and tell an attempt from a success.

In the lesson: Here is a real format Open S S H auth log from a bastion host, and a regular expression that pulls the result, the account and the source address out of every Failed and Accepted line. The script groups failures by source, and remembers any source that later logged in successfully. Then we count how many different accounts each source tried. The first address tried six accounts once each. That is password spraying: one likely password against many accounts, staying under the lockout threshold. The second hammered root seven times, which is brute force guessing, and on a Windows domain that pattern is what trips an account lockout. The last line matters most. The spraying address then logged in as carol. The threshold of three accounts is our choice, so tune it to your own traffic.

## Files

- [`starter/auth.log`](starter/auth.log)
- [`starter/spray_or_guess.py`](starter/spray_or_guess.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-02/starter`
2. Read `spray_or_guess.py` the way the lesson builds it:
   - Lines 1–5: pulls the result, the account and the source address
   - Lines 6–14: groups failures by source
   - Lines 15–21: count how many different accounts each source tried
3. Run it: `python3 spray_or_guess.py`.
4. Check it from the repository root: `./check m03l02-02`.

## Expected output

```text
198.51.100.23  fails 6, distinct users 6: T1110.003 spraying
203.0.113.9    fails 7, distinct users 1: T1110.001 guessing
198.51.100.23  then logged in as carol: treat as compromised
```

## How to check

`./check m03l02-02` copies `starter/` into a scratch directory and runs `python3 spray_or_guess.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
