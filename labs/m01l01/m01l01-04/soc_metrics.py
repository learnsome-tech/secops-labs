# Security Operations & Threat Hunting (SOC) — lesson m01l01 — SOC Operating Models, Tiers & Key Performance Metrics
# https://learnsome.tech/courses/secops-course/watch?lesson=m01l01
# © LearnSome.tech
import csv
from datetime import datetime
from statistics import mean, median

def minutes(row, start, end):
    gap = datetime.fromisoformat(row[end]) - datetime.fromisoformat(row[start])
    return gap.total_seconds() / 60

with open("incidents.csv", newline="") as f:
    rows = list(csv.DictReader(f))

for name, start, end in [("detect", "compromise", "alerted"),
                         ("acknowledge", "alerted", "acknowledged"),
                         ("contain", "alerted", "contained")]:
    values = [minutes(r, start, end) for r in rows]
    print(f"time to {name:<11}  mean {mean(values):5.0f} min"
          f"  median {median(values):4.0f} min")

worst = max(rows, key=lambda r: minutes(r, "compromise", "alerted"))
print("slowest detection:", worst["id"], "found by", worst["source"])
