# m04l01-04 · Walking the phases, and catching the step back

**Lesson:** [NIST SP 800-61 Incident Lifecycle & Management](https://learnsome.tech/learn/secops-course/m04l01) (lesson 4.1, module 4: Incident Response Lifecycle & Playbooks) · Pro  
**Check:** Graded

## Goal

You can place each action in an incident on its NIST lifecycle phase, spot when new scope sends a case back to analysis, measure the incident's clocks from its timeline, and explain how training, tabletops and simulations test preparation.

In the lesson: A few lines of Python walk that file and print every change of phase. The phases have a fixed order, from detection through to lessons. The program reads the timeline with the standard C S V reader and skips the adversary rows, because here we want the responders' path. Then it compares each phase with the one before; if the new phase sits earlier in the order, that is a step back. Read the output from the top. Detection, analysis, containment, eradication: a textbook run, finished by twenty past ten. At two minutes past eleven the case goes back to analysis because of the hunt, and runs containment and eradication again for the second mailbox. That backward step is normal. It is also the reason nobody should call an incident contained the moment the first account is locked.

## Files

- [`starter/phases.py`](starter/phases.py): the listing from the lesson
- [`starter/timeline.csv`](starter/timeline.csv)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-04/starter`
2. Read `phases.py` the way the lesson builds it:
   - Lines 1–4: a fixed order
   - Lines 5–7: skips the adversary rows
   - Lines 8–19: compares each phase
3. Run it: `python3 phases.py`.
4. Check it from the repository root: `./check m04l01-04`.

## Expected output

```text
03-02 09:14  start    detection    impossible travel alert j.okafor
03-02 09:31  forward  analysis     acknowledged; case IR-0142 opened
03-02 10:05  forward  containment  j.okafor sessions revoked
03-02 10:20  forward  eradication  rule and OAuth grant removed
03-02 11:02  back     analysis     same IP signed in as m.reyes
03-02 11:09  forward  containment  m.reyes sessions revoked
03-02 11:40  forward  eradication  m.reyes mailbox clean
03-02 12:15  forward  recovery     mailboxes back; MFA re-registered
03-05 14:00  forward  lessons      review held; three actions raised
```

## How to check

`./check m04l01-04` copies `starter/` into a scratch directory and runs `python3 phases.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
