# m03l02-03 · Application attacks in a web access log

**Lesson:** [Adversary Tactics, Techniques & Procedures (TTP) Mapping](https://learnsome.tech/learn/secops-course/m03l02) (lesson 3.2, module 3: Threat Intelligence & MITRE ATT&CK Mapping) · Pro  
**Check:** Graded

## Goal

You can read raw auth, web and sign-in logs, name the attack and ATT&CK technique they prove, and tell an attempt from a success.

In the lesson: Application attacks leave their marks in the web server's access log. This script parses the combined log format, which is the nginx default and a common Apache setting, then runs three checks: directory traversal, which climbs out of the web root with dot dot slash, S Q L injection, and input far longer than any real parameter, which is what a buffer overflow attempt usually looks like. Before any of that, it U R L decodes the request first. Attackers percent encode their payloads, so a search for dot dot slash on the raw line finds nothing. Every hit maps to the same technique, exploiting a public facing application. Read the status codes. The traversal got status two hundred and about eighteen hundred bytes back, roughly the size of a password file, so assume it worked. The injections got server errors, and the customer searching for O'Brien, apostrophe and all, is not flagged, and the oversized request got a bad gateway, which hints the back end crashed.

## Files

- [`starter/access.log`](starter/access.log)
- [`starter/web_attacks.py`](starter/web_attacks.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-03/starter`
2. Read `web_attacks.py` the way the lesson builds it:
   - Lines 1–4: parses the combined log format
   - Lines 5–9: three checks
   - Lines 10–18: U R L decodes the request
3. Run it: `python3 web_attacks.py`.
4. Check it from the repository root: `./check m03l02-03`.

## Expected output

```text
14:02:11 203.0.113.77 directory traversal status 200 bytes 1843  T1190
14:02:30 203.0.113.77 SQL injection       status 500 bytes  312  T1190
14:02:41 203.0.113.77 SQL injection       status 500 bytes  312  T1190
14:03:20 203.0.113.77 oversized input     status 502 bytes  166  T1190
```

## How to check

`./check m03l02-03` copies `starter/` into a scratch directory and runs `python3 web_attacks.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
