# m03l03-03 · Refang, extract and validate

**Lesson:** [Indicator of Compromise Extraction & Threat Hunting Feeds](https://learnsome.tech/learn/secops-course/m03l03) (lesson 3.3, module 3: Threat Intelligence & MITRE ATT&CK Mapping) · Pro  
**Check:** Graded

## Goal

You can extract and validate indicators from a threat report, sweep real proxy and endpoint logs for them, and age a feed before it reaches your SIEM.

In the lesson: The extractor starts with a table that undoes the defanging. Then one regular expression per indicator type. Domains are limited to three top level domains here to keep it short; a real one checks against the public suffix list. Hashes are recognised by length: sixty four hex characters for SHA two five six, thirty two for M D five, and word boundaries stop the shorter pattern matching inside the longer one. After matching, the function drops private and loopback addresses using the ipaddress module, which also rejects anything that is not a valid address. The main block prints what survived. Look at what survived: the internal share and the loopback address are gone, but the victim's own domain and that last hash are still here. Syntax checks cannot tell you intent.

## Files

- [`starter/iocs.py`](starter/iocs.py): the listing from the lesson
- [`starter/report.txt`](starter/report.txt)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-03/starter`
2. Read `iocs.py` the way the lesson builds it:
   - Lines 1–3: a table that undoes the defanging
   - Lines 4–9: one regular expression per indicator type
   - Lines 10–17: drops private and loopback addresses
   - Lines 18–20: prints what survived
3. Run it: `python3 iocs.py`.
4. Check it from the repository root: `./check m03l03-03`.

## Expected output

```text
url    https://cdn-update.example.net/api/v2/check
ipv4   198.51.100.23
domain cdn-update.example.net
domain corp.example.com
domain update-check.example.org
sha256 d6d0c8eb4047d89cbc0522c87591e36924ad86be3f9f98ed8fffed8ab3bea1dc
sha256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
md5    ba6b4fe0fe4d2a8e6381ed572a74e248
```

## How to check

`./check m03l03-03` copies `starter/` into a scratch directory and runs `python3 iocs.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
