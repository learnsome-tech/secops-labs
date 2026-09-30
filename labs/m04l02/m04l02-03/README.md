# m04l02-03 · Following the attacker's logins from host to host

**Lesson:** [Incident Triage, Severity Scoping & Communication](https://learnsome.tech/learn/secops-course/m04l02) (lesson 4.2, module 4: Incident Response Lifecycle & Playbooks) · Pro  
**Check:** Graded

## Goal

You can scope an incident by following an attacker's logins across hosts, rate its severity from NIST's impact factors using a written mapping, and run stakeholder communication out of band with legal owning regulatory clocks.

In the lesson: Here is scoping as a program you can read. One regular expression pulls the time, host, result, user and source address out of each open S S H line. Two lookups translate between host names and addresses using the inventory. The walk starts from the attacker's address. Any successful login from a tainted source taints the destination, so that host's own address joins the set. That is how the program follows the attacker from the bastion to the billing server, and from there to the database with the backup account. Failed attempts are printed too, but only put a host on a watch list. Notice what it ignored: the backup login to the database at two minutes to eight came from the bastion before the bastion was compromised. The result is three hosts in scope, with app three to watch.

## Files

- [`starter/auth.log`](starter/auth.log)
- [`starter/inventory.csv`](starter/inventory.csv)
- [`starter/scope.py`](starter/scope.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l02/m04l02-03/starter`
2. Read `scope.py` the way the lesson builds it:
   - Lines 1–4: One regular expression
   - Lines 5–7: Two lookups
   - Lines 8–20: The walk starts
3. Notes from the lesson:
   - Line 16: A success taints the destination host
4. Run it: `python3 scope.py`.
5. Check it from the repository root: `./check m04l02-03`.

## Expected output

```text
08:41:09 bastion01  root    from 203.0.113.50  Failed
08:41:15 bastion01  deploy  from 203.0.113.50  Failed
08:42:30 bastion01  deploy  from 203.0.113.50  Accepted
08:51:47 app02      deploy  from bastion01     Accepted
08:52:10 app03      deploy  from bastion01     Failed
09:03:33 db01       backup  from app02         Accepted
in scope: bastion01, app02, db01
watch:    app03
```

## How to check

`./check m04l02-03` copies `starter/` into a scratch directory and runs `python3 scope.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
