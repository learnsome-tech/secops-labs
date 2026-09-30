# m01l04-02 · A runbook for MFA push fatigue

**Lesson:** [SOC Runbooks, Shift Handoffs & Escalation Paths](https://learnsome.tech/learn/secops-course/m01l04) (lesson 1.4, module 1: SOC Architecture & SIEM Engineering) · Free  
**Check:** Checker

## Goal

You can write a runbook with evidence, authority and escalation triggers, generate a shift handoff that flags risk, and replay a time based escalation against its target.

In the lesson: Here is a real one, for M F A push fatigue: an attacker with a stolen password sends push prompts until the tired user taps approve. The header names the trigger, an owner, and the date it was last reviewed, so a stale runbook is obvious at a glance. The steps are short commands, each producing something to record. Look at the second step: call the user on the number in the H R system, not the one in the alert, because the attacker may have changed the contact details. The third step grants authority to revoke sessions and reset M F A without asking. The escalation block is an escalation path in miniature: tier two if the user did not approve or cannot be reached within fifteen minutes, the incident manager at once if the account has admin rights. The close codes at the bottom are the same dispositions the precision numbers in the triage lesson depend on.

## Files

- [`starter/rb-017-mfa-fatigue.yaml`](starter/rb-017-mfa-fatigue.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-02/starter`
2. Read `rb-017-mfa-fatigue.yaml` the way the lesson builds it:
   - Lines 1–5: the header names the trigger
   - Lines 6–10: the steps are short commands
   - Lines 11–15: the escalation block
   - Lines 16–19: the close codes at the bottom
3. Notes from the lesson:
   - Line 8: Contact details in the alert may belong to the attacker
4. Edit `rb-017-mfa-fatigue.yaml` and check it: `yamllint rb-017-mfa-fatigue.yaml`.
5. Check it from the repository root: `./check m01l04-02`.
6. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m01l04-02 --command=<id>`:
   - `lint` (Lint): `yamllint -d relaxed rb-017-mfa-fatigue.yaml`
   - `strict` (Lint strictly): `yamllint rb-017-mfa-fatigue.yaml`

## How to check

`./check m01l04-02` copies `starter/` into a scratch directory and runs `yamllint rb-017-mfa-fatigue.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it lints the YAML with yamllint's `relaxed` rules: it passes when there are no errors. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
