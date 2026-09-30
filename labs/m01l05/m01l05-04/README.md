# m01l05-04 · Polling a TAXII collection, page by page

**Lesson:** [Threat Intelligence Platforms & STIX/TAXII Ingestion](https://learnsome.tech/learn/secops-course/m01l05) (lesson 1.5, module 1: SOC Architecture & SIEM Engineering) · Free  
**Check:** Graded

## Goal

You can relate threat actor types to their motives, read a STIX 2.1 indicator, poll a TAXII 2.1 collection incrementally, and match indicators against proxy logs with expiry.

In the lesson: Now fetch a feed over TAXII. The server here is a small stand-in written for this lesson, started on localhost by the first import; it speaks just enough TAXII two point one to serve one collection. The client is the part to study. The U R L is the A P I root, then collections, the collection's identifier, and objects. The Accept header names the TAXII media type and version, and a server that cannot serve that version answers four hundred and six, not acceptable. The query asks only for objects added after the first of March, three at a time. The opener ignores proxy settings so the request stays on this machine. The loop sends a request, reads the envelope, and keeps the date added last header. While the envelope says more, it follows the next token. Run the poll. Three pages, eight objects: actors, indicators and relationships. Save that last date added and send it as added after next time, so each poll fetches only what is new.

## Files

- [`starter/intel_bundle.json`](starter/intel_bundle.json)
- [`starter/taxii_poll.py`](starter/taxii_poll.py): the listing from the lesson
- [`starter/taxii_server.py`](starter/taxii_server.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l05/m01l05-04/starter`
2. Read `taxii_poll.py` the way the lesson builds it:
   - Lines 1–3: started on localhost by the first import
   - Lines 4–6: the U R L is the A P I root
   - Lines 7: the accept header names
   - Lines 8: three at a time
   - Lines 9: the opener ignores proxy settings
   - Lines 10–20: the loop sends a request
   - Lines 21–22: run the poll
3. Run it: `python3 taxii_poll.py`.
4. Check it from the repository root: `./check m01l05-04`.

## Expected output

```text
got 3, last added 2026-03-02T09:06:00.000Z, more
got 3, last added 2026-03-03T10:00:00.000Z, more
got 2, last added 2026-03-03T10:06:00.000Z, done
8 objects: ['indicator', 'relationship', 'threat-actor']
```

## How to check

`./check m01l05-04` copies `starter/` into a scratch directory and runs `python3 taxii_poll.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
