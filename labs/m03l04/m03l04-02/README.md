# m03l04-02 · A cluster profile as a STIX intrusion set

**Lesson:** [Tracking Advanced Persistent Threats & Profiles](https://learnsome.tech/learn/secops-course/m03l04) (lesson 3.4, module 3: Threat Intelligence & MITRE ATT&CK Mapping) · Pro  
**Check:** Read along

## Goal

You can keep an evidence-based cluster profile, resolve vendor aliases, link incidents through infrastructure and weighted technique overlap, and state attribution confidence honestly.

In the lesson: Here is one of our own clusters written as the STIX intrusion set object, so any threat intelligence platform can store and share it. The name is internal. CL AMBER tells you nothing about who they are, and that is deliberate, because we do not know yet. Then first seen and last seen, which you update every time new activity is linked, and which tell a reader whether this cluster is still active. Goals are free text, while resource level and primary motivation take values from STIX open vocabularies, here financial gain. At the bottom sits a confidence from zero to one hundred. Techniques, malware and infrastructure are not stuffed into this object. They hang off it as separate objects joined by relationships of type uses, so each link carries its own dates and its own source.

## Files

- [`starter/cl-amber.json`](starter/cl-amber.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/cl-amber.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–8: the STIX intrusion set object
   - Lines 9–11: first seen and last seen
   - Lines 12–16: a confidence from zero to one hundred

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
