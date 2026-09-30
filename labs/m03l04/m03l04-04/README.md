# m03l04-04 · Resolving vendor names to one group ID

**Lesson:** [Tracking Advanced Persistent Threats & Profiles](https://learnsome.tech/learn/secops-course/m03l04) (lesson 3.4, module 3: Threat Intelligence & MITRE ATT&CK Mapping) · Pro  
**Check:** Graded

## Goal

You can keep an evidence-based cluster profile, resolve vendor aliases, link incidents through infrastructure and weighted technique overlap, and state attribution confidence honestly.

In the lesson: The fix is an alias index. The groups file holds two real ATTACK entries, cut down to a few of their associated names. The key function folds each name to lower case letters and digits, so A P T space two nine, a hyphenated cozy bear and the official spelling all collapse to the same key. The script builds one index from every name and alias, then looks up each name mentioned in this week's reports. Six mentions resolve to just two group identifiers, which means six reports you would otherwise have read as six different threats. The last one matches nothing. That is not an error. A new nickname is either a group you do not track yet, or a vendor's fresh cluster that may later be merged into a known one, so it goes on a list to revisit rather than being forced into a match.

## Files

- [`starter/groups.json`](starter/groups.json)
- [`starter/mentions.txt`](starter/mentions.txt)
- [`starter/resolve_alias.py`](starter/resolve_alias.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l04/m03l04-04/starter`
2. Read `resolve_alias.py` the way the lesson builds it:
   - Lines 1–6: folds each name to lower case letters and digits
   - Lines 7–13: builds one index from every name and alias
   - Lines 14–17: looks up each name mentioned
3. Run it: `python3 resolve_alias.py`.
4. Check it from the repository root: `./check m03l04-04`.

## Expected output

```text
Midnight Blizzard    G0016 APT29
NOBELIUM             G0016 APT29
APT 29               G0016 APT29
cozy-bear            G0016 APT29
Forest Blizzard      G0007 APT28
STRONTIUM            G0007 APT28
Velvet Loader crew   no match, possible new cluster
```

## How to check

`./check m03l04-04` copies `starter/` into a scratch directory and runs `python3 resolve_alias.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
