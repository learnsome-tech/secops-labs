# m03l03 · Indicator of Compromise Extraction & Threat Hunting Feeds

Module 3: Threat Intelligence & MITRE ATT&CK Mapping · lesson 3.3 · Pro · [Open the lesson](https://learnsome.tech/learn/secops-course/m03l03)

**Goal:** You can extract and validate indicators from a threat report, sweep real proxy and endpoint logs for them, and age a feed before it reaches your SIEM.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l03-02](m03l03-02/) | A threat note, as it reaches you | Read along |
| [m03l03-03](m03l03-03/) | Refang, extract and validate | Graded |
| [m03l03-04](m03l03-04/) | Sweeping proxy and endpoint telemetry | Graded |
| [m03l03-06](m03l03-06/) | Ageing and filtering a feed before use | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: harden the pipeline

1. Add two defanged IOCs to report.txt using hxxp and [:]//; predict what iocs.py prints
2. Make sweep.py skip values in feed_filter.py's KNOWN_GOOD and rerun it
3. Change TODAY to 2026-10-30 and predict which rows expire before running
4. Add a CIDR 203.0.113.0/24 feed row; decide how the IP check must change

> **Hint:** Move KNOWN_GOOD into iocs.py and filter there, so the sweep and the feed share one list.

## Check yourself

- Why did two unrelated hosts match the same SHA-256 from the report, and how would you stop it recurring?
- The sweep flagged portal.corp.example.com. Was that a compromise, and what in the report caused it?
- Why does an IP address from last spring's C2 deserve a shorter lifetime than a file hash?
- Which extractor step would you remove to make the sweep miss the attacker's domains entirely, and why?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
