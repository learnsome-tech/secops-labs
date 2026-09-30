# m02l01-04 · Threshold rule: five failures in a sliding window

**Lesson:** [Event Correlation Rules, Thresholds & Anomaly Pipelines](https://learnsome.tech/learn/secops-course/m02l01) (lesson 2.1, module 2: Log Ingestion & Detection Engineering) · Pro  
**Check:** Graded

## Goal

You can build threshold, correlation and baseline anomaly rules over parsed auth logs and explain what each one misses.

In the lesson: Here is the classic brute force threshold. For each source address the rule keeps a queue of recent failure times. Each new failure goes on the end, and anything older than sixty seconds drops off the front. That is the sliding window. When the queue reaches five, the rule fires once. The output shows one alert, for the address ending forty five, at nine fourteen and twenty four seconds. Now look at the peak lines. The address ending seventy seven never had more than one failure inside any minute, because it waited ninety seconds between guesses. It still got in, and this rule stayed silent. Guessing slowly to stay under common thresholds is a standard technique, so a threshold on its own is never the whole answer.

## Files

- [`starter/auth.log`](starter/auth.log)
- [`starter/authlog.py`](starter/authlog.py)
- [`starter/threshold.py`](starter/threshold.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-04/starter`
2. Read `threshold.py` the way the lesson builds it:
   - Lines 1–8: keeps a queue of recent failure times
   - Lines 9–16: drops off the front
   - Lines 17–19: when the queue reaches five
   - Lines 20–22: now look at the peak lines
3. Notes from the lesson:
   - Line 15: Slide: forget failures older than the window
4. Run it: `python3 threshold.py`.
5. Check it from the repository root: `./check m02l01-04`.

## Expected output

```text
09:14:24 alert: 5 failures from 203.0.113.45
203.0.113.45    peak 6 failure(s) in any 60s window
198.51.100.23   peak 1 failure(s) in any 60s window
192.0.2.77      peak 1 failure(s) in any 60s window
```

## How to check

`./check m02l01-04` copies `starter/` into a scratch directory and runs `python3 threshold.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
