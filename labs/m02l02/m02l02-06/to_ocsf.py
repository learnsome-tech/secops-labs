# Security Operations & Threat Hunting (SOC) — lesson m02l02 — Log Parsing, Schema Normalization (OCSF/ECS) & Extraction
# https://learnsome.tech/courses/secops-course/watch?lesson=m02l02
# © LearnSome.tech
import json
from datetime import datetime
from zoneinfo import ZoneInfo
from sshd_to_ecs import from_sshd
from trail_to_ecs import from_cloudtrail
def to_ocsf(d):
    """ECS authentication fields to OCSF Authentication, class 3002."""
    t = datetime.fromisoformat(d["@timestamp"])
    return {"class_uid": 3002, "activity_id": 1,
            "status_id": 1 if d["event.outcome"] == "success" else 2,
            "time": int(t.timestamp() * 1000), "user.name": d["user.name"],
            "src_endpoint.ip": d["source.ip"],
            "metadata.product.name": d["event.provider"]}
line = open("auth.log").readline()
ssh = to_ocsf(from_sshd(line, ZoneInfo("Europe/London")))
with open("cloudtrail.json") as f:
    aws = to_ocsf(from_cloudtrail(json.load(f)["Records"][0]))
print(f"{'field':22} {'sshd':22} cloudtrail")
for key in ssh:
    print(f"{key:22} {ssh[key]!s:22} {aws[key]}")
