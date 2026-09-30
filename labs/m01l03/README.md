# m01l03 · SIEM Architecture: Ingestion Pipelines & Indexing

Module 1: SOC Architecture & SIEM Engineering · lesson 1.3 · Free · [Open the lesson](https://learnsome.tech/learn/secops-course/m01l03)

**Goal:** You can trace an event through a SIEM pipeline, decode syslog priority, and explain why field indexes and full text indexes each miss different evidence.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l03-02](m01l03-02/) | Receiving syslog and decoding its priority | Graded |
| [m01l03-03](m01l03-03/) | Parsed fields and a real index | Graded |
| [m01l03-04](m01l03-04/) | Full text search, and how an address is tokenised | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: follow an event through the pipe

1. Add a line starting <165>1 to forwarded.log. Predict facility and severity, then run it.
2. In field_index.py, add a user column filled for the sudo line, then query it for j.doe.
3. In fulltext.py, search the phrase "203.0.113" and explain what else it would match.

> **Hint:** 165 is 20 times 8 plus 5: local4, notice. FACILITY has no entry for 20, so the script raises KeyError.

## Check yourself

- A syslog message starts with <4>. Which facility and severity does that encode, and how do you work it out?
- Why did the query on the src_ip field miss the intruder's sudo command, and which search found it?
- What did the vocabulary table show about how the address 203.0.113.9 was indexed, and why does that matter when a search comes back empty?
- The auth log timestamps carry no year or time zone. What goes wrong when you correlate them with firewall events, and what should the pipeline store?
- Why does a SIEM put a queue between collectors and indexers, and what happens without one when an indexer is down?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
