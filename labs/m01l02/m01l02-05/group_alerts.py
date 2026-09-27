# Security Operations & Threat Hunting (SOC) — lesson m01l02 — Alert Triage, False Positive Reduction & Fatigue Mitigation
# https://learnsome.tech/courses/secops-course/watch?lesson=m01l02
# © LearnSome.tech
import json
from datetime import datetime, timedelta

WINDOW = timedelta(minutes=60)
cases = []

with open("siem_alerts.jsonl") as f:
    alerts = [json.loads(line) for line in f]

for a in alerts:
    key = (a["rule"], a["entity"])
    at = datetime.fromisoformat(a["time"])
    case = next((c for c in cases if c["key"] == key
                 and at - c["first"] <= WINDOW), None)
    if case is None:
        case = {"key": key, "first": at, "ids": []}
        cases.append(case)
    case["ids"].append(a["id"])

print(len(alerts), "alerts became", len(cases), "cases")
for c in cases:
    print(f"{len(c['ids']):3} x {', '.join(c['key'])} from {c['first']:%H:%M}")
