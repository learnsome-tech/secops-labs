# m02l05 · YARA Rule Authoring & File Signature Matching

Module 2: Log Ingestion & Detection Engineering · lesson 2.5 · Pro · [Open the lesson](https://learnsome.tech/learn/secops-course/m02l05)

**Goal:** You can write a YARA rule with text, wide and hex strings and a condition that matches a malware family while rejecting clean files.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l05-02](m02l05-02/) | A YARA rule for the loader family | Read along |
| [m02l05-03](m02l05-03/) | Build four sample files to scan | Graded |
| [m02l05-04](m02l05-04/) | YARA's matching rules in a few lines of Python | Read along |
| [m02l05-05](m02l05-05/) | Scan the samples and report offsets | Graded |
| [m02l05-06](m02l05-06/) | Hash IOC, exact bytes, loose rule, real rule | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: break the rule, then harden it

1. Change invoice_b's key to 0x7F and its register byte 0x0E to 0x0F; predict compare.py first
2. Remove the gate string from invoice_b; does the rule still match? Which string would save it?
3. Teach hexstr YARA jumps: turn [1-3] into .{1,3} and test { 8A 04 [1-2] 34 ?? }
4. Add a clean PE with the stub and '/gate.php' only; decide whether the rule needs changing

> **Hint:** A jump [n-m] in a hex string means any n to m bytes; in a bytes regex that is .{n,m} with re.S.

## Check yourself

- Variant B differs from variant A only in its XOR key byte and some padding. Why did the sha256 IOC and the exact-bytes string both miss it?
- What does the `wide` modifier on $mutex make YARA look for?
- The updater.exe sample contained the same decode loop. Which part of the condition stopped it matching?
- A colleague proposes the hex string { ?? ?? 34 ?? } to catch more variants. What is the main problem?

---

[Course README](../../README.md) · [Security Operations & Threat Hunting (SOC) on LearnSome.tech](https://learnsome.tech/courses/secops-course)
