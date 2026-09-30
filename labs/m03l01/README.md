# m03l01 · Cyber Kill Chain vs MITRE ATT&CK Framework

Module 3: Threat Intelligence & MITRE ATT&CK Mapping · lesson 3.1 · Pro · [Open the lesson](https://learnsome.tech/learn/secops-course/m03l01)

**Goal:** You can map one intrusion onto both the Cyber Kill Chain and MITRE ATT&CK, and explain what each view reveals and hides.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l01-03](m03l01-03/) | One intrusion, ten observations | Read along |
| [m03l01-04](m03l01-04/) | Loading the real ATT&CK tactic mapping | Graded |
| [m03l01-05](m03l01-05/) | The same rows squeezed into seven phases | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: stretch both views

1. Append a row: an attacker logs in to the VPN as svc_backup, technique T1078
2. Predict both outputs first: how many tactics, and which kill chain phases?
3. Move privilege-escalation into Installation in PHASE and rerun killchain_view.py
4. Find the row that now lands in the most phases and explain why

> **Hint:** T1078 Valid Accounts is already in enterprise-attack.json; look at its kill_chain_phases.

## Check yourself

- Why does the scheduled task row print three tactics, and what does that tell you about ordering?
- In the kill chain view, why were reconnaissance and weaponisation empty for this incident?
- An attacker signs in to a cloud console with a stolen password. Which kill chain phases fit poorly?
- Why is a green heatmap cell for T1053.005 weak evidence that you detect scheduled task abuse?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
