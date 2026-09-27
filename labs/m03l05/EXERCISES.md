# Exercises — Detecting Persistence: Tasks, Registry & Services

Lesson `m03l05` · [Watch](https://learnsome.tech/courses/secops-course/watch?lesson=m03l05)

## Exercise 1: Your turn: extend both detectors

1. In task-4698.xml swap LogonTrigger for TimeTrigger; predict the trigger line, then run
2. Add a 7045 service for C:\Windows\System32\svchost.exe to events.xml; is it flagged?
3. Add a DaemonSet create by build-bot to audit.log; make detail() show its image
4. List every persistence mechanism found on WS-114, FS-02 and the cluster, for eradication

> **Hint**: A DaemonSet's image sits at spec.template.spec.containers[0].image in requestObject.


---

© LearnSome.tech · support@iwantto.learnsome.tech
