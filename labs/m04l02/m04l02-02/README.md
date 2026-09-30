# m04l02-02 · The asset inventory scoping depends on

**Lesson:** [Incident Triage, Severity Scoping & Communication](https://learnsome.tech/learn/secops-course/m04l02) (lesson 4.2, module 4: Incident Response Lifecycle & Playbooks) · Pro  
**Check:** Read along

## Goal

You can scope an incident by following an attacker's logins across hosts, rate its severity from NIST's impact factors using a written mapping, and run stakeholder communication out of band with legal owning regulatory clocks.

In the lesson: Scoping needs two things: the authentication logs from every host, and an asset inventory that says what each host is. This is the inventory, exported from the configuration database. Each row has a host name, its address, its role, the most sensitive class of data it holds, and whether it runs a critical service. The bastion holds no data at all, which is exactly why attackers like it: every administrator's session passes through it. The last row is the customer database, holding personal data. If that host ends up in scope, this is a different kind of incident. The logs beside it are ordinary open S S H lines in the usual auth log format: the time, the host, accepted or failed, the user, and the source address.

## Files

- [`starter/inventory.csv`](starter/inventory.csv): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/inventory.csv` alongside the lesson.
2. Notes from the lesson:
   - Line 2: No data, but every admin session passes through it
   - Line 5: Personal data: this row brings in legal

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
