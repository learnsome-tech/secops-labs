# m02l04-07 · An audit policy that protects secrets and records exec

**Lesson:** [Windows Event Logs, Sysmon & Linux Auditd Telemetry](https://learnsome.tech/learn/secops-course/m02l04) (lesson 2.4, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Checker

## Goal

You can parse Windows Security and Sysmon XML, reassemble auditd records, and write and read a Kubernetes audit policy to see who touched secrets or exec'd into pods.

In the lesson: Here is a policy file in that shape. Omit stages drops the request received stage, which roughly halves the volume without losing the outcome. The secrets rule comes first and uses Metadata on purpose. At Request or RequestResponse level the audit log would contain the secret values themselves, and your log store would become the easiest place to steal them from. Exec, attach and port forward get Request level, so you keep the parameters of the command. Next, kube proxy watch traffic is dropped as noise. The final catch all rule records everything else at Metadata. Order matters: move the catch all to the top and every later rule is ignored.

## Files

- [`starter/audit-policy.yaml`](starter/audit-policy.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-07/starter`
2. Read `audit-policy.yaml` the way the lesson builds it:
   - Lines 1–4: omit stages drops the request received stage
   - Lines 5–10: the secrets rule comes first
   - Lines 11–15: exec, attach and port forward
   - Lines 16–19: kube proxy watch traffic
   - Lines 20–21: the final catch all rule
3. Notes from the lesson:
   - Line 7: Never Request level for secrets: bodies hold the values
4. Edit `audit-policy.yaml` and check it: `kubeconform -strict -summary audit-policy.yaml`.
5. Check it from the repository root: `./check m02l04-07`.

## How to check

`./check m02l04-07` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary audit-policy.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
