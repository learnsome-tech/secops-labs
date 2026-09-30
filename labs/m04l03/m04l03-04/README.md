# m04l03-04 · Password reset versus session revocation

**Lesson:** [Containment & Eradication: Host, Net & Identity](https://learnsome.tech/learn/secops-course/m04l03) (lesson 4.3, module 4: Incident Response Lifecycle & Playbooks) · Pro  
**Check:** Graded

## Goal

You can choose a containment strategy, isolate a host without leaving live attacker sessions open, show why revoking sessions and not a password reset stops a stolen token, and sweep every in-scope host before a single coordinated eradication.

In the lesson: Now replay the attack against it. The stolen token was issued at the attacker's first sign-in, days before the alert, and it redeems happily. Then the helpdesk resets the password, the step most playbooks start with. Redeem the stolen token again: still accepted, because the token never depended on the password. Only when sessions are revoked, moving the valid from time to five past ten, is the token rejected. The real user signs in again and gets a fresh token that works. The last line is the attacker trying to be clever, pasting the old signature onto a token with a later issue time. The H M A C check rejects it. Real identity platforms behave the same way in principle: revoking sessions is its own action, and access tokens already issued can keep working until they expire, often after about an hour.

## Files

- [`starter/idp.py`](starter/idp.py)
- [`starter/revoke.py`](starter/revoke.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-04/starter`
2. Read `revoke.py` the way the lesson builds it:
   - Lines 1–8: The stolen token
   - Lines 9–11: the helpdesk resets the password
   - Lines 12–14: sessions are revoked
   - Lines 15–20: The real user signs in again
3. Run it: `python3 revoke.py`.
4. Check it from the repository root: `./check m04l03-04`.

## Expected output

```text
stolen token replayed    accepted: access token for j.okafor
after password reset     accepted: access token for j.okafor
after revoking sessions  rejected: issued before sessions were revoked
user signs in again      accepted: access token for j.okafor
new date, old signature  rejected: bad signature
```

## How to check

`./check m04l03-04` copies `starter/` into a scratch directory and runs `python3 revoke.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
