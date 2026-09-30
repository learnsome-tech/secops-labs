# m03l04 · Tracking Advanced Persistent Threats & Profiles

Module 3: Threat Intelligence & MITRE ATT&CK Mapping · lesson 3.4 · Pro · [Open the lesson](https://learnsome.tech/learn/secops-course/m03l04)

**Goal:** You can keep an evidence-based cluster profile, resolve vendor aliases, link incidents through infrastructure and weighted technique overlap, and state attribution confidence honestly.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l04-02](m03l04-02/) | A cluster profile as a STIX intrusion set | Read along |
| [m03l04-04](m03l04-04/) | Resolving vendor names to one group ID | Graded |
| [m03l04-05](m03l04-05/) | Clustering infrastructure by shared features | Graded |
| [m03l04-06](m03l04-06/) | Comparing an incident with cluster profiles | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: extend the tracking

1. Add "The Dukes" and "Sofacy" to mentions.txt; predict which ID each resolves to
2. Add a row to infra.csv reusing cert 77de1f... on a new incident; predict clusters
3. Remove T1003.001 from CL-AMBER and rerun overlap.py; explain the weighted change
4. Write a one-line confidence statement for linking IR-2026-007 to IR-2025-112

> **Hint:** In overlap.py, a technique used by only one profile has the biggest weight, log(4/2).

## Check yourself

- Why did the naive infrastructure run merge IR-2026-040 into the cluster, and what feature should not create links?
- Plain Jaccard favoured CL-GRAPHITE but the weighted score favoured CL-AMBER. What caused the difference?
- A report names Midnight Blizzard and your TIP only knows APT29. What goes wrong, and what fixes it?
- Your incident shares a commercial attack framework with a known group. Why is that weak evidence of attribution?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
