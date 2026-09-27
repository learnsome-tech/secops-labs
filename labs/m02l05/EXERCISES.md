# Exercises — YARA Rule Authoring & File Signature Matching

Lesson `m02l05` · [Watch](https://learnsome.tech/courses/secops-course/watch?lesson=m02l05)

## Exercise 1: Your turn: break the rule, then harden it

1. Change invoice_b's key to 0x7F and its register byte 0x0E to 0x0F; predict compare.py first
2. Remove the gate string from invoice_b; does the rule still match? Which string would save it?
3. Teach hexstr YARA jumps: turn [1-3] into .{1,3} and test { 8A 04 [1-2] 34 ?? }
4. Add a clean PE with the stub and '/gate.php' only; decide whether the rule needs changing

> **Hint**: A jump [n-m] in a hex string means any n to m bytes; in a bytes regex that is .{n,m} with re.S.


---

© LearnSome.tech · support@iwantto.learnsome.tech
