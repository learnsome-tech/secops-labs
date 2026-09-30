# m03l04-05 · Clustering infrastructure by shared features

**Lesson:** [Tracking Advanced Persistent Threats & Profiles](https://learnsome.tech/learn/secops-course/m03l04) (lesson 3.4, module 3: Threat Intelligence & MITRE ATT&CK Mapping) · Pro  
**Check:** Graded

## Goal

You can keep an evidence-based cluster profile, resolve vendor aliases, link incidents through infrastructure and weighted technique overlap, and state attribution confidence honestly.

In the lesson: Now infrastructure. Each row ties a domain to one of our incidents, with the S H A one fingerprint of the certificate it served and the registrant address from its domain registration. At the top is a set of values we know are shared by strangers, here a privacy proxy's address. The clustering is a union find. Every incident starts as its own group, and incidents whose rows share a certificate fingerprint or registrant are joined. Links chain, so if A shares with B and B shares with C, all three end up together. The script runs it twice. The naive run puts all four incidents in one cluster. Ignoring the privacy proxy, incident forty falls out. The other three stay linked by a reused certificate and a reused registrant, which are much harder to share by accident.

## Files

- [`starter/cluster_infra.py`](starter/cluster_infra.py): the listing from the lesson
- [`starter/infra.csv`](starter/infra.csv)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l04/m03l04-05/starter`
2. Read `cluster_infra.py` the way the lesson builds it:
   - Lines 1–4: values we know are shared
   - Lines 5–10: The clustering is a union find
   - Lines 11–18: share a certificate fingerprint or registrant
   - Lines 19–22: runs it twice
3. Run it: `python3 cluster_infra.py`.
4. Check it from the repository root: `./check m03l04-05`.

## Expected output

```text
naive
  IR-2025-112, IR-2026-007, IR-2026-031, IR-2026-040
shared values ignored
  IR-2025-112, IR-2026-007, IR-2026-031
  IR-2026-040
```

## How to check

`./check m03l04-05` copies `starter/` into a scratch directory and runs `python3 cluster_infra.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
