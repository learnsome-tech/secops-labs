# Exercises — Memory Forensics: Process Trees & Injection

Lesson `m05l03` · [Watch](https://learnsome.tech/courses/secops-course/watch?lesson=m05l03)

## Exercise 1: Teach the checks something new

1. Add a second services.exe under explorer.exe in pstree.txt; predict which checks fire.
2. Add a rule to lineage.py: report cmd.exe or powershell.exe whose parent is services.exe.
3. In build_dumps.py make the 0x2b0000 region PAGE_EXECUTE_READ; is it still reported?
4. Set the hollowed region's e_lfanew to 0x200 and predict the verdict before running.

> **Hint**: lineage.py only knows the parents listed in PARENT; any other name passes silently.


---

© LearnSome.tech · support@iwantto.learnsome.tech
