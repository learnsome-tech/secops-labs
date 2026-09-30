# m02l02-05 · One query across both sources

**Lesson:** [Log Parsing, Schema Normalization (OCSF/ECS) & Extraction](https://learnsome.tech/learn/secops-course/m02l02) (lesson 2.2, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Graded

## Goal

You can extract fields from text and JSON logs, map them onto ECS and OCSF, and catch the time zone and parse-failure bugs that break queries.

In the lesson: This is the payoff. Both mappers feed one list of documents, and the program first reports how many events it has and how many sshd lines did not parse. One line fell through: the connection closed message, which is not a logon attempt at all. You want that count on a dashboard, because a jump means the format changed. Then one question, asked once: failures from the address ending twenty three. Two S S H failures and one console failure come back in true time order, nine seconds apart in total. Someone tried J Smith's password on the bastion and then on the AWS console. Neither source alone tells that story.

## Files

- [`starter/auth.log`](starter/auth.log)
- [`starter/cloudtrail.json`](starter/cloudtrail.json)
- [`starter/query.py`](starter/query.py): the listing from the lesson
- [`starter/sshd_to_ecs.py`](starter/sshd_to_ecs.py)
- [`starter/trail_to_ecs.py`](starter/trail_to_ecs.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-05/starter`
2. Read `query.py` the way the lesson builds it:
   - Lines 1–4: both mappers feed one list
   - Lines 5–11: how many sshd lines did not parse
   - Lines 12–16: then one question, asked once
3. Run it: `python3 query.py`.
4. Check it from the repository root: `./check m02l02-05`.

## Expected output

```text
4 events, 1 unparsed sshd line(s)
2026-07-03T09:13:58Z sshd jsmith
2026-07-03T09:14:03Z sshd jsmith
2026-07-03T09:14:07Z signin.amazonaws.com jsmith
```

## How to check

`./check m02l02-05` copies `starter/` into a scratch directory and runs `python3 query.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
