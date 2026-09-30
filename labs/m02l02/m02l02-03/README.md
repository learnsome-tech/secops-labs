# m02l02-03 · Extract sshd fields into ECS names

**Lesson:** [Log Parsing, Schema Normalization (OCSF/ECS) & Extraction](https://learnsome.tech/learn/secops-course/m02l02) (lesson 2.2, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Graded

## Goal

You can extract fields from text and JSON logs, map them onto ECS and OCSF, and catch the time zone and parse-failure bugs that break queries.

In the lesson: The sshd mapper does two jobs. Extraction first: one regular expression pulls out the timestamp, host, result, account and address, and it accepts any method, so publickey and keyboard interactive logons parse as well as passwords. A line that does not match returns None, and the caller counts it. Silent drops are how parsers rot after a vendor upgrade. Then mapping: each fact goes into its E C S field, with accepted becoming success and failed becoming failure. The timestamp needs care. This bastion logs London local time with no offset, so the parser attaches the Europe London zone and converts to U T C. Ten thirteen local in July becomes nine thirteen U T C in the output.

## Files

- [`starter/auth.log`](starter/auth.log)
- [`starter/cloudtrail.json`](starter/cloudtrail.json)
- [`starter/sshd_to_ecs.py`](starter/sshd_to_ecs.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-03/starter`
2. Read `sshd_to_ecs.py` the way the lesson builds it:
   - Lines 1–6: one regular expression pulls out the timestamp
   - Lines 7–9: returns none, and the caller counts it
   - Lines 10–16: then mapping
   - Lines 17–21: converts to u t c
3. Run it: `python3 sshd_to_ecs.py`.
4. Check it from the repository root: `./check m02l02-03`.

## Expected output

```text
@timestamp      2026-07-03T09:13:58Z
event.category  authentication
event.provider  sshd
event.outcome   failure
user.name       jsmith
source.ip       198.51.100.23
host.name       bastion
```

## How to check

`./check m02l02-03` copies `starter/` into a scratch directory and runs `python3 sshd_to_ecs.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
