<img src="https://learnsome.tech/logo.png" width="48" alt="LearnSome.tech">

# Security Operations & Threat Hunting (SOC)

5 modules, 24 lessons: SOC Architecture & SIEM Engineering; Log Ingestion & Detection Engineering; Threat Intelligence & MITRE ATT&CK Mapping; Incident Response Lifecycle & Playbooks; Digital Forensics & Malware Triage.

## Watch and read

- **Course page**: [https://learnsome.tech/courses/secops-course](https://learnsome.tech/courses/secops-course)
- **Video player**: [https://learnsome.tech/courses/secops-course/watch](https://learnsome.tech/courses/secops-course/watch)
- **Handbook PDF**: [https://learnsome.tech/handbooks/secops/book.pdf](https://learnsome.tech/handbooks/secops/book.pdf)
- **On-site handbook**: [https://learnsome.tech/courses/secops-course/book](https://learnsome.tech/courses/secops-course/book)

## What is in this repository

This repository contains code artifacts, exercises and reference files for the lessons in this course.
24 lessons include a `labs/<lessonId>/` folder.
Each folder is named after the lesson identifier (e.g. `labs/m01l01/`) and contains the
artifact files shown in the course video, an `EXERCISES.md` with hands-on tasks, and
sub-directories named by artifact reference (e.g. `m01l01-02/`).

## Lessons

| # | Lesson | Watch | Labs | Handbook |
|---|--------|-------|------|----------|
| | **SOC Architecture & SIEM Engineering** | | | |
| 1 | SOC Operating Models, Tiers & Key Performance Metrics | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m01l01) | [labs/m01l01/](labs/m01l01/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-1-1) |
| 2 | Alert Triage, False Positive Reduction & Fatigue Mitigation | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m01l02) | [labs/m01l02/](labs/m01l02/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-1-2) |
| 3 | SIEM Architecture: Ingestion Pipelines & Indexing | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m01l03) | [labs/m01l03/](labs/m01l03/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-1-3) |
| 4 | SOC Runbooks, Shift Handoffs & Escalation Paths | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m01l04) | [labs/m01l04/](labs/m01l04/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-1-4) |
| 5 | Threat Intelligence Platforms & STIX/TAXII Ingestion | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m01l05) | [labs/m01l05/](labs/m01l05/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-1-5) |
| | **Log Ingestion & Detection Engineering** | | | |
| 6 | Event Correlation Rules, Thresholds & Anomaly Pipelines | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m02l01) | [labs/m02l01/](labs/m02l01/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-2-1) |
| 7 | Log Parsing, Schema Normalization (OCSF/ECS) & Extraction | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m02l02) | [labs/m02l02/](labs/m02l02/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-2-2) |
| 8 | Detection as Code: Authoring & Testing Sigma Rules | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m02l03) | [labs/m02l03/](labs/m02l03/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-2-3) |
| 9 | Windows Event Logs, Sysmon & Linux Auditd Telemetry | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m02l04) | [labs/m02l04/](labs/m02l04/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-2-4) |
| 10 | YARA Rule Authoring & File Signature Matching | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m02l05) | [labs/m02l05/](labs/m02l05/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-2-5) |
| | **Threat Intelligence & MITRE ATT&CK Mapping** | | | |
| 11 | Cyber Kill Chain vs MITRE ATT&CK Framework | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m03l01) | [labs/m03l01/](labs/m03l01/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-3-1) |
| 12 | Adversary Tactics, Techniques & Procedures (TTP) Mapping | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m03l02) | [labs/m03l02/](labs/m03l02/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-3-2) |
| 13 | Indicator of Compromise Extraction & Threat Hunting Feeds | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m03l03) | [labs/m03l03/](labs/m03l03/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-3-3) |
| 14 | Tracking Advanced Persistent Threats & Profiles | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m03l04) | [labs/m03l04/](labs/m03l04/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-3-4) |
| 15 | Detecting Persistence: Tasks, Registry & Services | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m03l05) | [labs/m03l05/](labs/m03l05/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-3-5) |
| | **Incident Response Lifecycle & Playbooks** | | | |
| 16 | NIST SP 800-61 Incident Lifecycle & Management | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m04l01) | [labs/m04l01/](labs/m04l01/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-4-1) |
| 17 | Incident Triage, Severity Scoping & Communication | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m04l02) | [labs/m04l02/](labs/m04l02/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-4-2) |
| 18 | Containment & Eradication: Host, Net & Identity | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m04l03) | [labs/m04l03/](labs/m04l03/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-4-3) |
| 19 | Recovery & System Validation Testing | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m04l04) | [labs/m04l04/](labs/m04l04/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-4-4) |
| 20 | Post-Incident Review & Root Cause Analysis | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m04l05) | [labs/m04l05/](labs/m04l05/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-4-5) |
| | **Digital Forensics & Malware Triage** | | | |
| 21 | Forensics Principles, Custody & Imaging | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m05l01) | [labs/m05l01/](labs/m05l01/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-5-1) |
| 22 | Disk Forensics: MFT, UsnJrnl & Prefetch | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m05l02) | [labs/m05l02/](labs/m05l02/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-5-2) |
| 23 | Memory Forensics: Process Trees & Injection | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m05l03) | [labs/m05l03/](labs/m05l03/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-5-3) |
| 24 | Malware Triage: Hashes, Strings & Sandboxing | [▶](https://learnsome.tech/courses/secops-course/watch?lesson=m05l04) | [labs/m05l04/](labs/m05l04/) | [§](https://learnsome.tech/courses/secops-course/book#lesson-5-4) |

## Exercises

Each lesson folder contains an `EXERCISES.md` with hands-on tasks drawn directly from the course material.
Open the file for a lesson to see the tasks and, where provided, hints.

---

© LearnSome.tech · support@iwantto.learnsome.tech
