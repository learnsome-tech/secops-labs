# m04l03-02 · Network isolation that actually cuts the attacker off

**Lesson:** [Containment & Eradication: Host, Net & Identity](https://learnsome.tech/learn/secops-course/m04l03) (lesson 4.3, module 4: Incident Response Lifecycle & Playbooks) · Pro  
**Check:** Read along

## Goal

You can choose a containment strategy, isolate a host without leaving live attacker sessions open, show why revoking sessions and not a password reset stops a stolen token, and sweep every in-scope host before a single coordinated eradication.

In the lesson: Network isolation first. If your E D R product has an isolate button, use it; underneath, it does something like this nftables ruleset. We cannot run nftables on this machine, so read it. Both chains drop by default, in and out. Loopback stays up so local services do not fall over. The incident response workstation keeps S S H access, and the host may still reach the E D R relay on port four hundred and forty three, so you keep telemetry and a way in. What is missing matters more. There is no blanket rule accepting established connections. Many firewall templates start with one, and here it would keep the attacker's already open command and control session alive. One more caution: an attacker with root on this host can delete this table. Back it up with a block on the switch, the cloud security group or the upstream firewall.

## Files

- [`starter/quarantine.nft`](starter/quarantine.nft): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/quarantine.nft` alongside the lesson.
2. Notes from the lesson:
   - Line 4: Default drop, inbound and outbound
   - Line 6: Responders keep SSH from one address
   - Line 7: Replies accepted only from named peers

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
