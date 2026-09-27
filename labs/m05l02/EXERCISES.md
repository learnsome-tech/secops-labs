# Exercises — Disk Forensics: MFT, UsnJrnl & Prefetch

Lesson `m05l02` · [Watch](https://learnsome.tech/courses/secops-course/watch?lesson=m05l02)

## Exercise 1: Change the evidence and predict the parser

1. In build_ntfs.py give report.docx whole-second times; predict what timestomp.py flags.
2. Add USN_REASON_SECURITY_CHANGE (0x800) to REASONS and an event that uses it.
3. In records(), set rec[511] = 0 before the fixup loop; predict what mft.py does.
4. Print each USN record's parent MFT number next to the file name.

> **Hint**: The parent reference is the second Q in the unpack format; mask it like the file one.


---

© LearnSome.tech · support@iwantto.learnsome.tech
