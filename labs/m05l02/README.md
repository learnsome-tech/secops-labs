# m05l02 · Disk Forensics: MFT, UsnJrnl & Prefetch

Module 5: Digital Forensics & Malware Triage · lesson 5.2 · Pro · [Open the lesson](https://learnsome.tech/learn/secops-course/m05l02)

**Goal:** You can parse MFT records and USN journal entries exported from an image, spot timestomping, and say what Prefetch adds as evidence of execution.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l02-02](m05l02-02/) | Walking a FILE record byte by byte | Graded |
| [m05l02-03](m05l02-03/) | Timestomping: when the two clocks disagree | Graded |
| [m05l02-05](m05l02-05/) | Reading USN records from $J | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Change the evidence and predict the parser

1. In build_ntfs.py give report.docx whole-second times; predict what timestomp.py flags.
2. Add USN_REASON_SECURITY_CHANGE (0x800) to REASONS and an event that uses it.
3. In records(), set rec[511] = 0 before the fixup loop; predict what mft.py does.
4. Print each USN record's parent MFT number next to the file name.

> **Hint:** The parent reference is the second Q in the unpack format; mask it like the file one.

## Check yourself

- Why can a user-mode tool change $STANDARD_INFORMATION timestamps but not $FILE_NAME ones, and how does that expose timestomping?
- What would mft.py read in the last two bytes of each 512-byte sector if it skipped the fixup step?
- stage.ps1 no longer exists as a live file. Which two artefacts from this lesson prove it existed, and what does each add?
- A Windows server has no Prefetch file for a suspicious binary. Why is that weak evidence that the binary never ran?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
