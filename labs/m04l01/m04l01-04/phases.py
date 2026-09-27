# Security Operations & Threat Hunting (SOC) — lesson m04l01 — NIST SP 800-61 Incident Lifecycle & Management
# https://learnsome.tech/courses/secops-course/watch?lesson=m04l01
# © LearnSome.tech
import csv

ORDER = ["detection", "analysis", "containment",
         "eradication", "recovery", "lessons"]

with open("timeline.csv", newline="") as f:
    rows = [r for r in csv.DictReader(f) if r["phase"] != "adversary"]

previous = None
for r in rows:
    phase = r["phase"]
    if phase == previous:
        continue
    move = "start" if previous is None else "forward"
    if previous and ORDER.index(phase) < ORDER.index(previous):
        move = "back"
    when = r["time"][5:16].replace("T", " ")
    print(f"{when}  {move:8} {phase:12} {r['entry']}")
    previous = phase
