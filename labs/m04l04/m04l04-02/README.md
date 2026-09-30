# m04l04-02 · Choosing a restore point the attacker never touched

**Lesson:** [Recovery & System Validation Testing](https://learnsome.tech/learn/secops-course/m04l04) (lesson 4.4, module 4: Incident Response Lifecycle & Playbooks) · Pro  
**Check:** Graded

## Goal

You can choose a restore point that predates the attacker and prove it intact, gate a rebuilt host's reconnection on a scripted baseline, and weigh the benefits and costs of automating that recovery work.

In the lesson: Choosing the restore point is a small program, not a guess. The investigation put the first attacker action on the database at twelve minutes past three on the twenty eighth of February. The backup catalogue lists each nightly dump with the time it was taken and the SHA two five six hash recorded when it was written, and it lives in a separate system the attacker never reached. Newest first, the loop skips anything taken after the first attacker action. For the rest, it hashes the file and compares the result with the catalogue. The first backup that survives both checks is the restore point. In the output, the two most recent dumps fall to the time check. The dump from the twenty eighth predates the attacker, but its hash no longer matches: someone edited a customer's email address afterwards. So the restore point is the twenty seventh, and the last line tells the business which changes must be replayed.

## Files

- [`starter/backups/db01-2026-02-26.sql`](starter/backups/db01-2026-02-26.sql)
- [`starter/backups/db01-2026-02-27.sql`](starter/backups/db01-2026-02-27.sql)
- [`starter/backups/db01-2026-02-28.sql`](starter/backups/db01-2026-02-28.sql)
- [`starter/backups/db01-2026-03-01.sql`](starter/backups/db01-2026-03-01.sql)
- [`starter/backups/db01-2026-03-02.sql`](starter/backups/db01-2026-03-02.sql)
- [`starter/catalogue.csv`](starter/catalogue.csv)
- [`starter/restore_point.py`](starter/restore_point.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-02/starter`
2. Read `restore_point.py` the way the lesson builds it:
   - Lines 1–4: put the first attacker action
   - Lines 5–7: The backup catalogue
   - Lines 8–12: the loop skips anything
   - Lines 13–17: hashes the file
   - Lines 18–20: The first backup that survives
3. Run it: `python3 restore_point.py`.
4. Check it from the repository root: `./check m04l04-02`.

## Expected output

```text
backups/db01-2026-03-02.sql  taken after the first attacker action, skip
backups/db01-2026-03-01.sql  taken after the first attacker action, skip
backups/db01-2026-02-28.sql  hash differs from catalogue, skip
backups/db01-2026-02-27.sql  predates the attacker and is intact: restore
changes since 2026-02-27T02:00:00Z must be replayed or re-entered
```

## How to check

`./check m04l04-02` copies `starter/` into a scratch directory and runs `python3 restore_point.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
