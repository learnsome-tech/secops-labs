# m05l04-02 · Hashes: identity, and why identity is fragile

**Lesson:** [Malware Triage: Hashes, Strings & Sandboxing](https://learnsome.tech/learn/secops-course/m05l04) (lesson 5.4, module 5: Digital Forensics & Malware Triage) · Pro  
**Check:** Graded

## Goal

You can handle a suspicious file as evidence, triage it with hashes, strings and its import table, and sweep endpoint logs for the indicators it yields.

In the lesson: The sample here is a harmless training file built by a helper script. It has the real structure of a sixty four bit Windows program, but its code section is filled with breakpoint instructions and does nothing. First the three hashes you meet in threat intelligence feeds and E D R consoles: M D five, S H A one and S H A two fifty six. Quote the S H A two fifty six. Then the program flips one bit in the code section and hashes again. Compare the two S H A two fifty six values: only a handful of hex digits line up, about what chance would give. That is exactly what a cryptographic hash should do, and it is also why an exact hash only ever catches that exact file. Recompile it or add one byte and every hash block list misses it.

## Files

- [`starter/build_sample.py`](starter/build_sample.py)
- [`starter/hashes.py`](starter/hashes.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l04/m05l04-02/starter`
2. Read `hashes.py` the way the lesson builds it:
   - Lines 1–2: built by a helper script
   - Lines 3–7: the three hashes
   - Lines 8–15: flips one bit in the code section
3. Run it: `python3 hashes.py`.
4. Check it from the repository root: `./check m05l04-02`.

## Expected output

```text
size   2560 bytes
md5    77a7915c2934e6964be4c6726efaa2e7
sha1   e331e09c70c1af84c85cf9210aa056d087665380
sha256 a63d5dcd5c75f4b86e72fd43e0a6989d963068caaf19be0bdcd20452d7044946
variant sha256 689d73a03f0971733484e82e04996a5ee4b294ababebfa9c2c22db893f620d1f
hex digits in the same place: 4 of 64
```

## How to check

`./check m05l04-02` copies `starter/` into a scratch directory and runs `python3 hashes.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
