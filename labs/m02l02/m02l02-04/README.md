# m02l02-04 · Map the CloudTrail record into the same names

**Lesson:** [Log Parsing, Schema Normalization (OCSF/ECS) & Extraction](https://learnsome.tech/learn/secops-course/m02l02) (lesson 2.2, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Graded

## Goal

You can extract fields from text and JSON logs, map them onto ECS and OCSF, and catch the time zone and parse-failure bugs that break queries.

In the lesson: The CloudTrail mapper has no regular expression, because the source is already structured. Extraction here means walking the JSON: the user name sits inside user identity, the outcome inside response elements. The mapping lower cases Failure to failure, since E C S expects the exact values success, failure or unknown. The error message goes into event dot reason rather than being thrown away. Mapping to a small set of outcome values is useful for queries, but the reason is what an analyst reads to tell a wrong password from a locked account. The output lines up with the sshd document above: same timestamp format, same outcome value, same field for the address.

## Files

- [`starter/auth.log`](starter/auth.log)
- [`starter/cloudtrail.json`](starter/cloudtrail.json)
- [`starter/trail_to_ecs.py`](starter/trail_to_ecs.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-04/starter`
2. Read `trail_to_ecs.py` the way the lesson builds it:
   - Lines 1–3: walking the json
   - Lines 4–9: lower cases failure to failure
   - Lines 10: the error message goes into event dot reason
   - Lines 11–18: the output lines up
3. Run it: `python3 trail_to_ecs.py`.
4. Check it from the repository root: `./check m02l02-04`.

## Expected output

```text
@timestamp       2026-07-03T09:14:07Z
event.category   authentication
event.provider   signin.amazonaws.com
event.outcome    failure
event.reason     Failed authentication
user.name        jsmith
source.ip        198.51.100.23
cloud.account.id 111122223333
```

## How to check

`./check m02l02-04` copies `starter/` into a scratch directory and runs `python3 trail_to_ecs.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
