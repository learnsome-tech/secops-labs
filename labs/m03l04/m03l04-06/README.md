# m03l04-06 · Comparing an incident with cluster profiles

**Lesson:** [Tracking Advanced Persistent Threats & Profiles](https://learnsome.tech/learn/secops-course/m03l04) (lesson 3.4, module 3: Threat Intelligence & MITRE ATT&CK Mapping) · Pro  
**Check:** Graded

## Goal

You can keep an evidence-based cluster profile, resolve vendor aliases, link incidents through infrastructure and weighted technique overlap, and state attribution confidence honestly.

In the lesson: Techniques are the third pivot. The script loads three cluster profiles and the techniques from our latest incident, then counts how many profiles use each technique. The rarity weight is a logarithm that falls to zero for a technique every profile uses. Phishing attachments, PowerShell and web command channels are everywhere, so they say nothing about who you are facing. The score is Jaccard similarity: shared techniques divided by all techniques, plain or weighted. It prints both scores and the techniques each cluster uses that we have not seen yet. Plain Jaccard picks GRAPHITE, because it shares many common techniques. Weighted, AMBER leads, because it shares the rare ones: L S A S S dumping and exfiltration to cloud storage. The unseen column is the useful part. It is a hunting list for what AMBER might do next.

## Files

- [`starter/incident.txt`](starter/incident.txt)
- [`starter/overlap.py`](starter/overlap.py): the listing from the lesson
- [`starter/profiles.json`](starter/profiles.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l04/m03l04-06/starter`
2. Read `overlap.py` the way the lesson builds it:
   - Lines 1–7: how many profiles use each technique
   - Lines 8–13: the rarity weight
   - Lines 14–18: prints both scores
3. Run it: `python3 overlap.py`.
4. Check it from the repository root: `./check m03l04-06`.

## Expected output

```text
CL-GRAPHITE  jaccard 0.62  weighted 0.22  unseen T1105
CL-AMBER     jaccard 0.50  weighted 0.38  unseen T1021.001 T1486 T1560.001
CL-SLATE     jaccard 0.50  weighted 0.16  unseen T1190 T1486 T1505.003
```

## How to check

`./check m03l04-06` copies `starter/` into a scratch directory and runs `python3 overlap.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
