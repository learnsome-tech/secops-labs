# Security Operations & Threat Hunting (SOC) — lesson m01l04 — SOC Runbooks, Shift Handoffs & Escalation Paths
# https://learnsome.tech/courses/secops-course/watch?lesson=m01l04
# © LearnSome.tech
import csv
from datetime import datetime, timedelta

SHIFT_END = datetime.fromisoformat("2026-03-09T19:00")
# minutes from opening to containment, by severity
TARGET = {"P1": 240, "P2": 480, "P3": 1440}

with open("open_cases.csv", newline="") as f:
    cases = list(csv.DictReader(f))

for c in cases:
    due = datetime.fromisoformat(c["opened"]) + timedelta(
        minutes=TARGET[c["sev"]])
    c["left"] = int((due - SHIFT_END).total_seconds() // 60)

print(f"Handoff at {SHIFT_END:%H:%M}, {len(cases)} open cases")
for c in sorted(cases, key=lambda c: c["left"]):
    left = c["left"]
    state = "breached" if left < 0 else "due soon" if left < 60 else "on track"
    print(f'{c["id"]} {c["sev"]} {state:<8} {left:>4} min {c["owner"]:<8}',
          c["next"] or "no next action written")
