# m03l05-02 · Event 4698: a scheduled task is registered

**Lesson:** [Detecting Persistence: Tasks, Registry & Services](https://learnsome.tech/learn/secops-course/m03l05) (lesson 3.5, module 3: Threat Intelligence & MITRE ATT&CK Mapping) · Pro  
**Check:** Read along

## Goal

You can find scheduled task, service and Run key persistence in Windows event XML, diff autostarts against a baseline, and spot Kubernetes persistence in API server audit logs.

In the lesson: Here is event four six nine eight from the Security auditing provider on the workstation from the phishing case. It only appears if the audit policy for other object access events is switched on, which is off by default, so check that before you rely on it. The event data says who created it, the service account the attacker stole, and the task name. The valuable part is the task content field. Windows puts the full task definition in there as escaped X M L: a document inside the document. It holds the trigger, the account the task runs as, written as a security identifier, the run level, and the exact command. Reading those four things tells you almost everything about a task, so the next script pulls them out properly instead of searching the text.

## Files

- [`starter/task-4698.xml`](starter/task-4698.xml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/task-4698.xml` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–7: from the Security auditing provider
   - Lines 8–11: who created it
   - Lines 12–22: the full task definition

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l05-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
