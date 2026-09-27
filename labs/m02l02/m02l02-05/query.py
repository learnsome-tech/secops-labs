# Security Operations & Threat Hunting (SOC) — lesson m02l02 — Log Parsing, Schema Normalization (OCSF/ECS) & Extraction
# https://learnsome.tech/courses/secops-course/watch?lesson=m02l02
# © LearnSome.tech
import json
from zoneinfo import ZoneInfo
from sshd_to_ecs import from_sshd
from trail_to_ecs import from_cloudtrail

with open("auth.log") as f:
    parsed = [from_sshd(line, ZoneInfo("Europe/London")) for line in f]
with open("cloudtrail.json") as f:
    records = json.load(f)["Records"]
docs = [d for d in parsed if d] + [from_cloudtrail(r) for r in records]
print(f"{len(docs)} events, {parsed.count(None)} unparsed sshd line(s)")

# One question, asked once, answered across every source
for d in sorted(docs, key=lambda d: d["@timestamp"]):
    if d["source.ip"] == "198.51.100.23" and d["event.outcome"] == "failure":
        print(d["@timestamp"], d["event.provider"], d["user.name"])
