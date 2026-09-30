# m03l05 · Detecting Persistence: Tasks, Registry & Services

Module 3: Threat Intelligence & MITRE ATT&CK Mapping · lesson 3.5 · Pro · [Open the lesson](https://learnsome.tech/learn/secops-course/m03l05)

**Goal:** You can find scheduled task, service and Run key persistence in Windows event XML, diff autostarts against a baseline, and spot Kubernetes persistence in API server audit logs.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l05-02](m03l05-02/) | Event 4698: a scheduled task is registered | Read along |
| [m03l05-03](m03l05-03/) | Parsing the task hidden inside the event | Graded |
| [m03l05-04](m03l05-04/) | Services and Run keys against a baseline | Graded |
| [m03l05-06](m03l05-06/) | Finding persistence in the API server audit log | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: extend both detectors

1. In task-4698.xml swap LogonTrigger for TimeTrigger; predict the trigger line, then run
2. Add a 7045 service for C:\Windows\System32\svchost.exe to events.xml; is it flagged?
3. Add a DaemonSet create by build-bot to audit.log; make detail() show its image
4. List every persistence mechanism found on WS-114, FS-02 and the cluster, for eradication

> **Hint:** A DaemonSet's image sits at spec.template.spec.containers[0].image in requestObject.

## Check yourself

- The 4698 event shows UserId S-1-5-18, a LogonTrigger and a script in AppData. Why is that combination alarming?
- Why does autoruns_diff.py check the baseline before the risky markers, and what would change if it did not?
- An attacker's static pod keeps coming back after you delete it with the API. Why, and where must you remove it?
- The audit log shows build-bot creating a ClusterRoleBinding to cluster-admin. Why is that persistence as well as escalation?
- Your audit policy logs these resources at Metadata level only. Which detail in the lesson's output would you lose?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
