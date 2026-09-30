# m03l05-06 · Finding persistence in the API server audit log

**Lesson:** [Detecting Persistence: Tasks, Registry & Services](https://learnsome.tech/learn/secops-course/m03l05) (lesson 3.5, module 3: Threat Intelligence & MITRE ATT&CK Mapping) · Pro  
**Check:** Graded

## Goal

You can find scheduled task, service and Run key persistence in Windows event XML, diff autostarts against a baseline, and spot Kubernetes persistence in API server audit logs.

In the lesson: Every one of those leaves a record in the A P I server audit log, one J S O N event per line, if your audit policy records request bodies for these resources. The script keeps only writes: create, update and patch. For each resource type it pulls out the one detail that matters: the host path a pod mounts, the role a binding grants, a secret's type, or a CronJob's schedule. It skips the Argo C D controller, because in this cluster Git is supposed to be the only source of workloads, and anything it creates was reviewed as a pull request. Four lines, one actor. Within three minutes the C I build bot created a CronJob in kube system, bound itself to cluster admin, minted a long lived token, and mounted the static pod directory from a node.

## Files

- [`starter/audit.log`](starter/audit.log)
- [`starter/audit_persistence.py`](starter/audit_persistence.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l05/m03l05-06/starter`
2. Read `audit_persistence.py` the way the lesson builds it:
   - Lines 1–4: only writes
   - Lines 5–12: pulls out the one detail that matters
   - Lines 13–21: skips the Argo C D controller
3. Run it: `python3 audit_persistence.py`.
4. Check it from the repository root: `./check m03l05-06`.

## Expected output

```text
03:13:02 build-bot cronjobs kube-system/log-rotate */10 * * * *
03:13:30 build-bot clusterrolebindings cluster/ci-admin grants cluster-admin
03:14:05 build-bot secrets kube-system/metrics-token service-account-token
03:15:44 build-bot pods default/node-debug hostPath /etc/kubernetes/manifests
```

## How to check

`./check m03l05-06` copies `starter/` into a scratch directory and runs `python3 audit_persistence.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
