# m02l03-05 · Tests catch the miss, and the over-correction

**Lesson:** [Detection as Code: Authoring & Testing Sigma Rules](https://learnsome.tech/learn/secops-course/m02l03) (lesson 2.3, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Graded

## Goal

You can read and write a Sigma rule, test it against true and false positive events, and name the log indicators behind common attack families.

In the lesson: PowerShell accepts any unambiguous prefix of a parameter name, and dash e c is a documented alias for encoded command, so the rule has to cover several spellings. Detection as code means that finding becomes a test case, not a memory. Each test file line is a named event plus the verdict it should get. The first attempt at a fix broadens the match to dash e, which catches everything, including the admin script that uses dash execution policy. A test that expects silence catches that. Version two lists the short forms with a space after them, plus dash e n c o to cover every longer spelling, and passes all five. Sigma's windash modifier would also cover the slash form that powershell dot exe accepts.

## Files

- [`starter/hunt.py`](starter/hunt.py)
- [`starter/sigma_match.py`](starter/sigma_match.py)
- [`starter/test_rule.py`](starter/test_rule.py): the listing from the lesson
- [`starter/tests.jsonl`](starter/tests.jsonl)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-05/starter`
2. Read `test_rule.py` the way the lesson builds it:
   - Lines 1–4: detection as code means that finding becomes a test case
   - Lines 5–12: the first attempt at a fix
   - Lines 13–18: each test file line is a named event
3. Run it: `python3 test_rule.py`.
4. Check it from the repository root: `./check m02l03-05`.

## Expected output

```text
v1 as written  4/5 pass short -ec flag
broadened      4/5 pass admin -ExecutionPolicy
v2             5/5 pass
```

## How to check

`./check m02l03-05` copies `starter/` into a scratch directory and runs `python3 test_rule.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
