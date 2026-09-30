# m02l01-02 · First look: count the auth log with awk

**Lesson:** [Event Correlation Rules, Thresholds & Anomaly Pipelines](https://learnsome.tech/learn/secops-course/m02l01) (lesson 2.1, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Graded

## Goal

You can build threshold, correlation and baseline anomaly rules over parsed auth logs and explain what each one misses.

In the lesson: Before writing a rule, look at the evidence the way an analyst would at a shell. This file is an excerpt from an Ubuntu bastion, where the S S H daemon logs to var log auth dot log; Red Hat systems use var log secure. The script prints the first two raw lines so you can see the format, then counts failed passwords per source address, then lists every accepted password logon. Now read the output together. The address ending forty five failed six times and then logged in as deploy. The address ending seventy seven failed four times and then logged in as backup. Neither fact sits on any one line. You only see it by counting and lining events up in time, which is exactly the work the rules in the next segments automate.

## Files

- [`starter/auth.log`](starter/auth.log)
- [`starter/command.txt`](starter/command.txt)
- [`starter/peek.sh`](starter/peek.sh): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-02/starter`
2. Read `peek.sh` the way the lesson builds it:
   - Lines 1–2: prints the first two raw lines
   - Lines 3–5: counts failed passwords per source address
   - Lines 6–7: lists every accepted password logon
3. Run it: `bash peek.sh`.
4. Check it from the repository root: `./check m02l01-02`.

## Expected output

```text
Mar  3 09:14:02 bastion sshd[4410]: Failed password for invalid user admin from 203.0.113.45 port 50122 ssh2
Mar  3 09:14:07 bastion sshd[4412]: Failed password for root from 203.0.113.45 port 50130 ssh2
6 203.0.113.45
4 192.0.2.77
1 198.51.100.23
09:15:10 deploy 203.0.113.45
09:20:19 jsmith 198.51.100.23
09:36:00 backup 192.0.2.77
```

## How to check

`./check m02l01-02` copies `starter/` into a scratch directory and runs `bash peek.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
