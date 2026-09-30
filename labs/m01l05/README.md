# m01l05 · Threat Intelligence Platforms & STIX/TAXII Ingestion

Module 1: SOC Architecture & SIEM Engineering · lesson 1.5 · Free · [Open the lesson](https://learnsome.tech/learn/secops-course/m01l05)

**Goal:** You can relate threat actor types to their motives, read a STIX 2.1 indicator, poll a TAXII 2.1 collection incrementally, and match indicators against proxy logs with expiry.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l05-03](m01l05-03/) | One STIX indicator, field by field | Read along |
| [m01l05-04](m01l05-04/) | Polling a TAXII collection, page by page | Graded |
| [m01l05-05](m01l05-05/) | Matching indicators against a proxy log | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: feed and match

1. Add an indicator and an indicates relationship for 203.0.113.80. Predict match_intel.py output.
2. Set valid_until on the beacon domain to 2026-03-08T00:00:00Z and rerun the match.
3. In taxii_poll.py set added_after to the last date added you saw. Predict what comes back.
4. Change limit to 5 and predict the number of pages before running.

> **Hint:** Without the relationship, actor_of has no entry and the script raises KeyError. Eight objects at five a page is two pages.

## Check yourself

- Unusual access to a finance server fires an alert. How would your next steps differ if intelligence linked it to organised crime rather than a nation-state group?
- Why does the STIX indicator not name its threat actor, and which object in the bundle made that link in the demo?
- What should a TAXII client keep after each poll, and how does it use that value on the next one?
- The proxy log matched 198.51.100.23 but the script ignored it. Why was that right, and what does it say about address indicators?
- A report is marked TLP AMBER+STRICT. May you paste it into a ticket shared with your managed service provider?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
