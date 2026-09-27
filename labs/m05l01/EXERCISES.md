# Exercises — Forensics Principles, Custody & Imaging

Lesson `m05l01` · [Watch](https://learnsome.tech/courses/secops-course/watch?lesson=m05l01)

## Exercise 1: Break the evidence, then catch it

1. In verify.py flip a bit in block 0 instead of block 5; predict the byte range first.
2. Set BLOCK to 4096 in both image.py and verify.py; how precise is the damaged range now?
3. Move row 6's time before row 5's in the CSV and predict what custody.py prints.
4. Add a rule to custody.py that flags a row whose released_by equals its received_by.

> **Hint**: A byte at offset n sits in block n // BLOCK; the range printed is that whole block.


---

© LearnSome.tech · support@iwantto.learnsome.tech
