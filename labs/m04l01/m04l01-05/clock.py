# Security Operations & Threat Hunting (SOC) — lesson m04l01 — NIST SP 800-61 Incident Lifecycle & Management
# https://learnsome.tech/courses/secops-course/watch?lesson=m04l01
# © LearnSome.tech
import csv
from datetime import datetime

def first(phase, rows):
    return next(r["at"] for r in rows if r["phase"] == phase)

def last(phase, rows):
    return [r["at"] for r in rows if r["phase"] == phase][-1]

with open("timeline.csv", newline="") as f:
    rows = list(csv.DictReader(f))
for r in rows:
    r["at"] = datetime.fromisoformat(r["time"])

alert = first("detection", rows)
print("dwell before alert    ", alert - first("adversary", rows))
print("alert to triage       ", first("analysis", rows) - alert)
print("alert to first contain", first("containment", rows) - alert)
print("alert to all contained", last("containment", rows) - alert)
print("alert to recovered    ", first("recovery", rows) - alert)
