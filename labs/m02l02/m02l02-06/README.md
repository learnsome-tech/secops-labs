# m02l02-06 · Translate ECS fields into an OCSF Authentication event

**Lesson:** [Log Parsing, Schema Normalization (OCSF/ECS) & Extraction](https://learnsome.tech/learn/secops-course/m02l02) (lesson 2.2, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Graded

## Goal

You can extract fields from text and JSON logs, map them onto ECS and OCSF, and catch the time zone and parse-failure bugs that break queries.

In the lesson: OCSF describes the same facts with a different philosophy. Every event belongs to a numbered class. Authentication is class three thousand and two, in category three, identity and access management. Inside the class, activity one means logon, and status one means success while two means failure. Numbers instead of words make the schema compact and language neutral. Time is milliseconds since the Unix epoch, not a string. The user and source address become nested objects; this table flattens them with dots so the two columns fit side by side. Read across a row and both sources agree on every field. Tools that consume OCSF, such as Amazon Security Lake, can now treat the bastion and the console as one kind of event.

## Files

- [`starter/auth.log`](starter/auth.log)
- [`starter/cloudtrail.json`](starter/cloudtrail.json)
- [`starter/sshd_to_ecs.py`](starter/sshd_to_ecs.py)
- [`starter/to_ocsf.py`](starter/to_ocsf.py): the listing from the lesson
- [`starter/trail_to_ecs.py`](starter/trail_to_ecs.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-06/starter`
2. Read `to_ocsf.py` the way the lesson builds it:
   - Lines 1–5: a different philosophy
   - Lines 6–13: every event belongs to a numbered class
   - Lines 14–20: read across a row
3. Notes from the lesson:
   - Line 10: OCSF status_id: 1 success, 2 failure
   - Line 11: OCSF time is epoch milliseconds, not text
4. Run it: `python3 to_ocsf.py`.
5. Check it from the repository root: `./check m02l02-06`.

## Expected output

```text
field                  sshd                   cloudtrail
class_uid              3002                   3002
activity_id            1                      1
status_id              2                      2
time                   1783070038000          1783070047000
user.name              jsmith                 jsmith
src_endpoint.ip        198.51.100.23          198.51.100.23
metadata.product.name  sshd                   signin.amazonaws.com
```

## How to check

`./check m02l02-06` copies `starter/` into a scratch directory and runs `python3 to_ocsf.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
