<p>
  <a href="https://learnsome.tech/courses/secops-course">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".github/assets/wordmark-inverse.svg">
      <img src=".github/assets/wordmark.svg" alt="LearnSome.tech" width="260">
    </picture>
  </a>
</p>

# Security Operations & Threat Hunting (SOC)

**SIEM Telemetry, Sigma Rules, YARA Hunting, MITRE ATT&CK & Volatile Forensics**

5 modules, 24 lessons: SOC Architecture & SIEM Engineering; Log Ingestion & Detection Engineering; Threat Intelligence & MITRE ATT&CK Mapping; Incident Response Lifecycle & Playbooks; Digital Forensics & Malware Triage. Intermediate level, about 3 hours.

This repository holds the labs of the LearnSome.tech course [Security Operations & Threat Hunting (SOC)](https://learnsome.tech/courses/secops-course): each lab's starter files, a README with the goal, the steps and the expected output, and `./check`, which tests your work the way the site does.

## Start

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/learnsome-tech/secops-labs?quickstart=1)

- **Codespaces:** the badge opens this repository in a dev container with Python 3.14.7, kubeconform 0.8.0 and ansible-core and yamllint, as in the site's lab sandbox.
- **On your machine:**

  ```sh
  git clone https://github.com/learnsome-tech/secops-labs.git
  cd secops-labs
  ./check m01l01-04
  ```

  You need Python 3 for `./check`, and for the labs themselves Python 3.14.7, kubeconform 0.8.0 and ansible-core and yamllint. Other versions mostly work, but only the sandbox's versions are sure to print what the site prints. VS Code's Dev Containers extension builds the same container as Codespaces (x86-64).

## Doing a lab

1. Open the lesson on LearnSome.tech and the lab folder beside it: `labs/<lesson>/<lab>/`. The lab README has the goal, the steps and the expected output.
2. Work in the lab's `starter/` folder.
3. From the repository root, run `./check <lab>` (for example `./check m01l01-04`), or `./check <lesson>` for all labs of a lesson, or `./check --all`. `./check --list` shows every lab and how it is checked.

`./check` runs your starter the way the site's lab sandbox does: in a scratch copy that is its working directory and `HOME`, with `LANG=C.UTF-8`, `TZ=UTC`, `input.txt` on standard input, 10 seconds and 256 KiB of output per stream. It then compares the output with the site's own rules, so a pass here is a pass on the site.

| Check | What `./check` does | Labs |
| --- | --- | --- |
| Graded | Runs the program and compares its output with `expected.txt`. | 66 |
| Checker | Validates the file with the checker the site uses (hadolint, kubeconform, actionlint, yamllint, `ansible-playbook --syntax-check` or `terraform validate`); passes when it finds no errors. | 4 |
| Read along | Nothing to run here: the site shows the listing read-only, and the lab README says honestly what it needs (Docker, a cluster, a cloud account...). | 21 |

## What is published, and what is not

Every lab's starter is the code the lesson shows on screen, which is also what the lab editor on the site opens with. Where that code is the whole program, such as a recorded shell session or a script from the video, it is published as it is: it is the lesson content. Nothing beyond the lesson is published. There are no reference solutions and no answers to the lesson exercises, and nothing the site keeps private.

Pro lessons' labs are here as starters too. LearnSome.tech runs and grades your labs in its sandbox, hosts the videos and keeps your progress; running and grading a Pro lab on the site needs Pro.

## Modules and lessons

### Module 1: SOC Architecture & SIEM Engineering

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 1.1 | [SOC Operating Models, Tiers & Key Performance Metrics](https://learnsome.tech/learn/secops-course/m01l01) | [3 labs](labs/m01l01/) | Free |
| 1.2 | [Alert Triage, False Positive Reduction & Fatigue Mitigation](https://learnsome.tech/learn/secops-course/m01l02) | [4 labs](labs/m01l02/) | Free |
| 1.3 | [SIEM Architecture: Ingestion Pipelines & Indexing](https://learnsome.tech/learn/secops-course/m01l03) | [3 labs](labs/m01l03/) | Free |
| 1.4 | [SOC Runbooks, Shift Handoffs & Escalation Paths](https://learnsome.tech/learn/secops-course/m01l04) | [3 labs](labs/m01l04/) | Free |
| 1.5 | [Threat Intelligence Platforms & STIX/TAXII Ingestion](https://learnsome.tech/learn/secops-course/m01l05) | [3 labs](labs/m01l05/) | Free |

### Module 2: Log Ingestion & Detection Engineering

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 2.1 | [Event Correlation Rules, Thresholds & Anomaly Pipelines](https://learnsome.tech/learn/secops-course/m02l01) | [5 labs](labs/m02l01/) | Pro |
| 2.2 | [Log Parsing, Schema Normalization (OCSF/ECS) & Extraction](https://learnsome.tech/learn/secops-course/m02l02) | [6 labs](labs/m02l02/) | Pro |
| 2.3 | [Detection as Code: Authoring & Testing Sigma Rules](https://learnsome.tech/learn/secops-course/m02l03) | [4 labs](labs/m02l03/) | Pro |
| 2.4 | [Windows Event Logs, Sysmon & Linux Auditd Telemetry](https://learnsome.tech/learn/secops-course/m02l04) | [6 labs](labs/m02l04/) | Pro |
| 2.5 | [YARA Rule Authoring & File Signature Matching](https://learnsome.tech/learn/secops-course/m02l05) | [5 labs](labs/m02l05/) | Pro |

### Module 3: Threat Intelligence & MITRE ATT&CK Mapping

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 3.1 | [Cyber Kill Chain vs MITRE ATT&CK Framework](https://learnsome.tech/learn/secops-course/m03l01) | [3 labs](labs/m03l01/) | Pro |
| 3.2 | [Adversary Tactics, Techniques & Procedures (TTP) Mapping](https://learnsome.tech/learn/secops-course/m03l02) | [3 labs](labs/m03l02/) | Pro |
| 3.3 | [Indicator of Compromise Extraction & Threat Hunting Feeds](https://learnsome.tech/learn/secops-course/m03l03) | [4 labs](labs/m03l03/) | Pro |
| 3.4 | [Tracking Advanced Persistent Threats & Profiles](https://learnsome.tech/learn/secops-course/m03l04) | [4 labs](labs/m03l04/) | Pro |
| 3.5 | [Detecting Persistence: Tasks, Registry & Services](https://learnsome.tech/learn/secops-course/m03l05) | [4 labs](labs/m03l05/) | Pro |

### Module 4: Incident Response Lifecycle & Playbooks

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 4.1 | [NIST SP 800-61 Incident Lifecycle & Management](https://learnsome.tech/learn/secops-course/m04l01) | [3 labs](labs/m04l01/) | Pro |
| 4.2 | [Incident Triage, Severity Scoping & Communication](https://learnsome.tech/learn/secops-course/m04l02) | [3 labs](labs/m04l02/) | Pro |
| 4.3 | [Containment & Eradication: Host, Net & Identity](https://learnsome.tech/learn/secops-course/m04l03) | [4 labs](labs/m04l03/) | Pro |
| 4.4 | [Recovery & System Validation Testing](https://learnsome.tech/learn/secops-course/m04l04) | [3 labs](labs/m04l04/) | Pro |
| 4.5 | [Post-Incident Review & Root Cause Analysis](https://learnsome.tech/learn/secops-course/m04l05) | [4 labs](labs/m04l05/) | Pro |

### Module 5: Digital Forensics & Malware Triage

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 5.1 | [Forensics Principles, Custody & Imaging](https://learnsome.tech/learn/secops-course/m05l01) | [4 labs](labs/m05l01/) | Pro |
| 5.2 | [Disk Forensics: MFT, UsnJrnl & Prefetch](https://learnsome.tech/learn/secops-course/m05l02) | [3 labs](labs/m05l02/) | Pro |
| 5.3 | [Memory Forensics: Process Trees & Injection](https://learnsome.tech/learn/secops-course/m05l03) | [3 labs](labs/m05l03/) | Pro |
| 5.4 | [Malware Triage: Hashes, Strings & Sandboxing](https://learnsome.tech/learn/secops-course/m05l04) | [4 labs](labs/m05l04/) | Pro |

**Free** lessons are open to anyone with a free LearnSome.tech account; **Pro** lessons need a Pro membership to watch, run and grade on the site.

## Licence

- **Code** (starter files, `check` and `.learnsome/`, the dev container and the workflows) is under the [MIT licence](LICENSE).
- **Written text** (the READMEs, lab instructions, lesson text, exercises and questions) is under [CC BY-NC-SA 4.0](LICENSE-text.md): share and adapt it with attribution to LearnSome.tech, not commercially, under the same licence.
- The LearnSome.tech name and logo are not covered by either licence.

## Contributing and security

This repository is generated from the course. Report a broken lab or a content error [as an issue](../../issues/new/choose); see [CONTRIBUTING.md](CONTRIBUTING.md). Security reports go to [SECURITY.md](SECURITY.md).

© 2026 LearnSome.tech
