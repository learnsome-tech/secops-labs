# m04l05-02 · Where the hours went

**Lesson:** [Post-Incident Review & Root Cause Analysis](https://learnsome.tech/learn/secops-course/m04l05) (lesson 4.5, module 4: Incident Response Lifecycle & Playbooks) · Pro  
**Check:** Graded

## Goal

You can run a blameless review from the incident timeline, find branching root causes with five whys and a fishbone, and prove a corrective detection works by replaying the incident's own logs through it.

In the lesson: Start from the timeline, not from opinions. This program reads the case timeline for the bastion and database incident and measures the gap before every row the organisation wrote, ignoring gaps that end with the attacker's own actions. Each gap is labelled by the row that ended it, and the four longest are printed. The longest gap, over two days, ended when data loss prevention flagged a large export from the database. That is the detection gap, and nothing the responders did that morning could shrink it. Second is fifty minutes waiting for the database owner to approve isolation. Third is thirty eight minutes before tier one picked up the alert. Now the review has an agenda built on evidence: why were we blind for two days, and why did containment wait for a sign off?

## Files

- [`starter/gaps.py`](starter/gaps.py): the listing from the lesson
- [`starter/timeline.csv`](starter/timeline.csv)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l05/m04l05-02/starter`
2. Read `gaps.py` the way the lesson builds it:
   - Lines 1–7: reads the case timeline
   - Lines 8–11: the gap before every row
   - Lines 12–14: the four longest
3. Run it: `python3 gaps.py`.
4. Check it from the repository root: `./check m04l05-02`.

## Expected output

```text
2 days, 6:07:20   until dlp: large export from db01 flagged
0:50:00           until db-owner: isolation of db01 approved
0:38:00           until tier1: alert acknowledged
0:35:00           until tier2: sweep complete: three hosts
```

## How to check

`./check m04l05-02` copies `starter/` into a scratch directory and runs `python3 gaps.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
