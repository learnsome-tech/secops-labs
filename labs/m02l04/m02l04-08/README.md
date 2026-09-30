# m02l04-08 · Who touched secrets or exec'd into a pod?

**Lesson:** [Windows Event Logs, Sysmon & Linux Auditd Telemetry](https://learnsome.tech/learn/secops-course/m02l04) (lesson 2.4, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Graded

## Goal

You can parse Windows Security and Sysmon XML, reassemble auditd records, and write and read a Kubernetes audit policy to see who touched secrets or exec'd into pods.

In the lesson: The audit log is one JSON event per line. This program keeps three kinds: any request touching secrets, any request on the exec subresource whatever its verb, and anything the authoriser refused. Then it prints the time, verb, target, user, source address, client and verdict. Read the output from the top. The C I deployer service account reads the payments database secret, from an outside address, using curl rather than the C I tooling. Four seconds later the same token tries to list secrets in kube system and is refused, then tries nodes and is refused again. That is a stolen token being explored. The last line is J Smith opening a shell in a payments pod, allowed, and worth confirming with a change ticket.

## Files

- [`starter/audit.jsonl`](starter/audit.jsonl)
- [`starter/k8s_audit.py`](starter/k8s_audit.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-08/starter`
2. Read `k8s_audit.py` the way the lesson builds it:
   - Lines 1–6: this program keeps three kinds
   - Lines 7–12: then it prints the time
   - Lines 13–17: read the output from the top
3. Run it: `python3 k8s_audit.py`.
4. Check it from the repository root: `./check m02l04-08`.

## Expected output

```text
09:52:10 get    secrets/payments/db-creds      system:serviceaccount:ci:deployer 203.0.113.9 curl/8.5.0 allow 200
09:52:14 list   secrets/kube-system            system:serviceaccount:ci:deployer 203.0.113.9 curl/8.5.0 forbid 403
09:52:31 get    nodes                          system:serviceaccount:ci:deployer 203.0.113.9 curl/8.5.0 forbid 403
09:53:02 create pods/exec/payments/api-7d9f    jsmith@example.com 198.51.100.23 kubectl/v1.34.1 allow 101
```

## How to check

`./check m02l04-08` copies `starter/` into a scratch directory and runs `python3 k8s_audit.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
