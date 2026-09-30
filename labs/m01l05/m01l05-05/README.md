# m01l05-05 · Matching indicators against a proxy log

**Lesson:** [Threat Intelligence Platforms & STIX/TAXII Ingestion](https://learnsome.tech/learn/secops-course/m01l05) (lesson 1.5, module 1: SOC Architecture & SIEM Engineering) · Free  
**Check:** Graded

## Goal

You can relate threat actor types to their motives, read a STIX 2.1 indicator, poll a TAXII 2.1 collection incrementally, and match indicators against proxy logs with expiry.

In the lesson: Intelligence earns its keep when it meets your logs. This script loads the same bundle and builds two lookups. The first follows every indicates relationship from an indicator to its threat actor. The second maps each watched value to its indicator, taking the value out of the pattern by splitting on the quotes. That shortcut only works for single equality patterns like these; real patterns can combine comparisons, so production code uses a proper pattern matcher. Then it reads a Squid proxy access log. Each line gives an epoch time, the client, the host it tunnelled to, and the upstream address, and both host and address are checked. An indicator whose valid until has passed is ignored. Run it. A laptop reached the Crew Seven beacon domain: command and control, a crime syndicate after money. The expired hit is most likely a legitimate portal on a recycled address. Last, a workstation connected to the leak site: exfiltration, for an activist group.

## Files

- [`starter/access.log`](starter/access.log)
- [`starter/intel_bundle.json`](starter/intel_bundle.json)
- [`starter/match_intel.py`](starter/match_intel.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l05/m01l05-05/starter`
2. Read `match_intel.py` the way the lesson builds it:
   - Lines 1–7: follows every indicates relationship
   - Lines 8: maps each watched value
   - Lines 9–13: reads a Squid proxy access log
   - Lines 14–18: an indicator whose valid until has passed
   - Lines 19–22: run it
3. Run it: `python3 match_intel.py`.
4. Check it from the repository root: `./check m01l05-05`.

## Expected output

```text
08:14 192.0.2.44 update-check.example.net: command-and-control, Example Crew Seven ['crime-syndicate'] personal-gain
08:20 192.0.2.61 198.51.100.23: indicator expired, ignored
09:47 192.0.2.52 drop.leak-front.example.org: exfiltration, Example Leak Front ['activist'] ideology
```

## How to check

`./check m01l05-05` copies `starter/` into a scratch directory and runs `python3 match_intel.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
