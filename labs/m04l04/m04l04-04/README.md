# m04l04-04 · The reconnection gate: fail stays quarantined

**Lesson:** [Recovery & System Validation Testing](https://learnsome.tech/learn/secops-course/m04l04) (lesson 4.4, module 4: Incident Response Lifecycle & Playbooks) · Pro  
**Check:** Graded

## Goal

You can choose a restore point that predates the attacker and prove it intact, gate a rebuilt host's reconnection on a scripted baseline, and weigh the benefits and costs of automating that recovery work.

In the lesson: Here the check becomes a gate. The shell script loops over every snapshot collected from a candidate host, and the validator's exit status decides the branch. In a real pipeline the pass branch would move the host into the production security group and the fail branch would open a ticket; here each one prints what it would do. The results are plain. The full system image from the first of March carries an account called sys upd with user id zero, which makes it a second root. It also has a listener on port four four four four, and password authentication switched back on. That image stays in quarantine. The host rebuilt from the golden image, with data restored from the twenty seventh, passes all three checks and is allowed back.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/gate.sh`](starter/gate.sh): the listing from the lesson
- [`starter/snapshots/db01-image-0301/passwd`](starter/snapshots/db01-image-0301/passwd)
- [`starter/snapshots/db01-image-0301/ss.txt`](starter/snapshots/db01-image-0301/ss.txt)
- [`starter/snapshots/db01-image-0301/sshd-T.txt`](starter/snapshots/db01-image-0301/sshd-T.txt)
- [`starter/snapshots/db01-rebuilt/passwd`](starter/snapshots/db01-rebuilt/passwd)
- [`starter/snapshots/db01-rebuilt/ss.txt`](starter/snapshots/db01-rebuilt/ss.txt)
- [`starter/snapshots/db01-rebuilt/sshd-T.txt`](starter/snapshots/db01-rebuilt/sshd-T.txt)
- [`starter/validate.py`](starter/validate.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-04/starter`
2. Read `gate.sh` the way the lesson builds it:
   - Lines 1–3: loops over every snapshot
   - Lines 4–9: decides the branch
3. Run it: `bash gate.sh`.
4. Check it from the repository root: `./check m04l04-04`.

## Expected output

```text
  db01-image-0301: login shell for unexpected user sysupd
  db01-image-0301: unexpected listener on port 4444
  db01-image-0301: sshd -T lacks 'passwordauthentication no'
db01-image-0301: fail, stays in quarantine
db01-rebuilt: pass, move to the production security group
```

## How to check

`./check m04l04-04` copies `starter/` into a scratch directory and runs `bash gate.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
