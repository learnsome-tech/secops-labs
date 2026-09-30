# m05l01 · Forensics Principles, Custody & Imaging

Module 5: Digital Forensics & Malware Triage · lesson 5.1 · Pro · [Open the lesson](https://learnsome.tech/learn/secops-course/m05l01)

**Goal:** You can decide what to collect first, acquire a disk image whose hashes prove it is unchanged, and keep a chain of custody with no gaps.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l01-03](m05l01-03/) | Acquire an image and hash it in the same pass | Graded |
| [m05l01-04](m05l01-04/) | A working copy changes, and the hashes say where | Graded |
| [m05l01-06](m05l01-06/) | The custody record for one laptop | Read along |
| [m05l01-07](m05l01-07/) | Checking the custody record for gaps | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Break the evidence, then catch it

1. In verify.py flip a bit in block 0 instead of block 5; predict the byte range first.
2. Set BLOCK to 4096 in both image.py and verify.py; how precise is the damaged range now?
3. Move row 6's time before row 5's in the CSV and predict what custody.py prints.
4. Add a rule to custody.py that flags a row whose released_by equals its received_by.

> **Hint:** A byte at offset n sits in block n // BLOCK; the range printed is that whole block.

## Check yourself

- A responder powers off a BitLocker-protected laptop before imaging it. What is lost, and why does the order of volatility put it first?
- Why does image.py hash the data while copying it, and then hash the finished image again?
- verify.py found evidence.img matching all 16 blocks and working.img failing block 5. What does that prove, and what does it not prove?
- The custody record shows the laptop received by Store 2, and the next row has J. Lind releasing it. Why does that matter even though the hash on that row matches?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
