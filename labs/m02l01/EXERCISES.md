# Exercises — Event Correlation Rules, Thresholds & Anomaly Pipelines

Lesson `m02l01` · [Watch](https://learnsome.tech/courses/secops-course/watch?lesson=m02l01)

## Exercise 1: Your turn: move the limits and predict

1. In threshold.py set LIMIT = 3 and WINDOW to 300 seconds; predict which addresses alert, then run
2. Add two Failed password lines for jsmith just before 09:20:19; predict correlate.py, then run
3. In baseline.py only let the z score alert when today's count is at least 10; which rows change?

> **Hint**: The window test is e['ts'] - q[0] > WINDOW. correlate.py looks back LOOKBACK from each success.


---

© LearnSome.tech · support@iwantto.learnsome.tech
