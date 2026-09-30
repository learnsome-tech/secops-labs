# m02l03-02 · A Sigma rule for encoded PowerShell

**Lesson:** [Detection as Code: Authoring & Testing Sigma Rules](https://learnsome.tech/learn/secops-course/m02l03) (lesson 2.3, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Checker

## Goal

You can read and write a Sigma rule, test it against true and false positive events, and name the log indicators behind common attack families.

In the lesson: Here is a real Sigma rule. The top is metadata a reviewer reads: title, a unique id, status, author, and tags that map it to MITRE ATT and CK technique one zero five nine point zero zero one, PowerShell. The log source block says which events it applies to: process creation on Windows, which covers Sysmon event one and Security event four six eight eight. The detection block is the logic. Each named map is a selection. Inside one map, different fields must all match, and a list of values means any one of them will do. The pipe after a field name is a modifier, such as ends with or contains. Last comes the condition: both selections must hit, and the SCCM filter must not.

## Files

- [`starter/rule.yml`](starter/rule.yml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-02/starter`
2. Read `rule.yml` the way the lesson builds it:
   - Lines 1–9: the top is metadata a reviewer reads
   - Lines 10–12: the log source block says
   - Lines 13–19: the detection block is the logic
   - Lines 20–21: last comes the condition
3. Notes from the lesson:
   - Line 15: A list of values: any one may match
   - Line 19: filter_ removes a known benign parent
4. Edit `rule.yml` and check it: `yamllint rule.yml`.
5. Check it from the repository root: `./check m02l03-02`.
6. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m02l03-02 --command=<id>`:
   - `lint` (Lint): `yamllint -d relaxed rule.yml`
   - `strict` (Lint strictly): `yamllint rule.yml`

## How to check

`./check m02l03-02` copies `starter/` into a scratch directory and runs `yamllint rule.yml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it lints the YAML with yamllint's `relaxed` rules: it passes when there are no errors. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
