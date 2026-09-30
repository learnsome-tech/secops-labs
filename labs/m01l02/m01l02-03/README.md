# m01l02-03 · The noisy rule, and a scoped exception

**Lesson:** [Alert Triage, False Positive Reduction & Fatigue Mitigation](https://learnsome.tech/learn/secops-course/m01l02) (lesson 1.2, module 1: SOC Architecture & SIEM Engineering) · Free  
**Check:** Checker

## Goal

You can classify alert outcomes, find the rules that fill the queue, write a scoped exclusion that does not hide attackers, and group alerts into cases.

In the lesson: Take the noisiest rule. This is its source, written for Falco, the open source runtime sensor. The condition fires whenever a new process starts in a container and its name is one of four common shells. The output line records the namespace, pod, parent process, command line and image, which is the context an analyst needs to triage without logging in anywhere. Priority is warning, and the tags map it to execution. At the bottom is the tuning, written as a Falco exception. It names three fields and one row of values: the backup namespace, a parent process of cron, and the exact backup command line. An alert is dropped only when all three match at once. That is the shape a good exclusion has: several fields, each as narrow as you can make it.

## Files

- [`starter/shell_in_container.yaml`](starter/shell_in_container.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-03/starter`
2. Read `shell_in_container.yaml` the way the lesson builds it:
   - Lines 1–5: the condition fires whenever
   - Lines 6–11: the output line records
   - Lines 12–16: at the bottom is the tuning
3. Edit `shell_in_container.yaml` and check it: `yamllint shell_in_container.yaml`.
4. Check it from the repository root: `./check m01l02-03`.

## How to check

`./check m01l02-03` copies `starter/` into a scratch directory and runs `yamllint shell_in_container.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it lints the YAML with yamllint's `relaxed` rules: it passes when there are no errors. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
