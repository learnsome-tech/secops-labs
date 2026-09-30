# m03l03-04 · Sweeping proxy and endpoint telemetry

**Lesson:** [Indicator of Compromise Extraction & Threat Hunting Feeds](https://learnsome.tech/learn/secops-course/m03l03) (lesson 3.3, module 3: Threat Intelligence & MITRE ATT&CK Mapping) · Pro  
**Check:** Graded

## Goal

You can extract and validate indicators from a threat report, sweep real proxy and endpoint logs for them, and age a feed before it reaches your SIEM.

In the lesson: Now the sweep. The script imports the extractor, then walks a Squid proxy log in its native format: field seven is the U R L or, for a tunnel, host and port, and field nine holds the address the proxy really connected to. A domain matches exactly or as a parent domain, and an address matches the upstream peer. Then it reads endpoint file events exported from the E D R and compares hashes. Seven hits, and only four are real: one workstation reached both command servers, another fetched from the fallback address, and the dropper sits in a Downloads folder. The portal hit is our own domain. The last two file hits share one hash, because it is the SHA two five six of an empty file, and it matches every zero byte file on every host you own.

## Files

- [`starter/file_events.csv`](starter/file_events.csv)
- [`starter/iocs.py`](starter/iocs.py)
- [`starter/proxy.log`](starter/proxy.log)
- [`starter/report.txt`](starter/report.txt)
- [`starter/sweep.py`](starter/sweep.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-04/starter`
2. Read `sweep.py` the way the lesson builds it:
   - Lines 1–6: imports the extractor
   - Lines 7–14: Squid proxy log in its native format
   - Lines 15–18: endpoint file events
3. Run it: `python3 sweep.py`.
4. Check it from the repository root: `./check m03l03-04`.

## Expected output

```text
proxy 192.0.2.50 cdn-update.example.net matched cdn-update.example.net
proxy 192.0.2.50 update-check.example.org matched update-check.example.org
proxy 192.0.2.77 portal.corp.example.com matched corp.example.com
proxy 192.0.2.64 198.51.100.23 matched 198.51.100.23
file  WS-114 C:\Users\jo\Downloads\invoice_0914.lnk 2331 bytes
file  WS-114 C:\Users\jo\AppData\Local\Temp\~DF3A1.tmp 0 bytes
file  WS-120 C:\ProgramData\Backup\sync.lock 0 bytes
```

## How to check

`./check m03l03-04` copies `starter/` into a scratch directory and runs `python3 sweep.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
