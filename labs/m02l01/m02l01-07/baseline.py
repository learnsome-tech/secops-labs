# Security Operations & Threat Hunting (SOC) — lesson m02l01 — Event Correlation Rules, Thresholds & Anomaly Pipelines
# https://learnsome.tech/courses/secops-course/watch?lesson=m02l01
# © LearnSome.tech
import csv
from statistics import mean, stdev

with open("logons_per_day.csv") as f:
    rows = list(csv.DictReader(f))
history, today = rows[:-1], rows[-1]
STATIC, Z_LIMIT = 50, 3.0

print("account  today   mean    sd       z  static  baseline")
for user in ("deploy", "jsmith", "backup"):
    past = [int(r[user]) for r in history]
    now = int(today[user])
    mu, sd = mean(past), stdev(past)
    z = (now - mu) / sd
    static = "alert" if now > STATIC else "quiet"
    base = "alert" if abs(z) > Z_LIMIT else "quiet"
    print(f"{user:8} {now:5} {mu:6.1f} {sd:5.1f} {z:7.1f}  {static:6}  {base}")
