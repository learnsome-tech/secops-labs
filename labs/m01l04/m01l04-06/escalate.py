# Security Operations & Threat Hunting (SOC) — lesson m01l04 — SOC Runbooks, Shift Handoffs & Escalation Paths
# https://learnsome.tech/courses/secops-course/watch?lesson=m01l04
# © LearnSome.tech
import json
from datetime import datetime, timedelta

with open("p1_escalation.json") as f:
    policy = json.load(f)

alert_at = datetime.fromisoformat("2026-03-10T02:10")
ack_at = datetime.fromisoformat("2026-03-10T02:47")

for level in policy["levels"]:
    page_at = alert_at + timedelta(minutes=level["after_minutes"])
    if page_at >= ack_at:
        print(f"never paged: {level['notify']}")
        continue
    print(f"{page_at:%H:%M} level {level['level']}: page {level['notify']}")

waited = int((ack_at - alert_at).total_seconds() // 60)
target = policy["ack_target_minutes"]
verdict = "met" if waited <= target else "missed"
print(f"{ack_at:%H:%M} acknowledged after {waited} min,",
      f"target {target} min: {verdict}")
