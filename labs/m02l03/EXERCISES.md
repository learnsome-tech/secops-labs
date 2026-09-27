# Exercises — Detection as Code: Authoring & Testing Sigma Rules

Lesson `m02l03` · [Watch](https://learnsome.tech/courses/secops-course/watch?lesson=m02l03)

## Exercise 1: Your turn: extend the tests, then write a rule

1. Add a test case for 'powershell.exe /enc dwBoAG8AYQBtAGkA'; predict v2's result, then run
2. Change v2 so the slash form alerts without re-breaking the ExecutionPolicy test
3. Write web.yml: category webserver, cs-uri-query|contains 'union select' and '../'
4. Translate its detection into a dict and test it on two attack and two clean URIs

> **Hint**: Add ' /enc ' style values, or read the Sigma spec for the windash modifier and mimic it.


---

© LearnSome.tech · support@iwantto.learnsome.tech
