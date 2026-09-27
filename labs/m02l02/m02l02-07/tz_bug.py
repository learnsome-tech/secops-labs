# Security Operations & Threat Hunting (SOC) — lesson m02l02 — Log Parsing, Schema Normalization (OCSF/ECS) & Extraction
# https://learnsome.tech/courses/secops-course/watch?lesson=m02l02
# © LearnSome.tech
import json
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from sshd_to_ecs import from_sshd
from trail_to_ecs import from_cloudtrail

with open("cloudtrail.json") as f:
    console = from_cloudtrail(json.load(f)["Records"][0])["@timestamp"]
line = open("auth.log").readline()
t_console = datetime.fromisoformat(console)
for label, tz in [("assumed UTC", timezone.utc),
                  ("Europe/London", ZoneInfo("Europe/London"))]:
    ssh = from_sshd(line, tz)["@timestamp"]
    gap = (t_console - datetime.fromisoformat(ssh)).total_seconds()
    print(f"{label:14} sshd {ssh}  console {console}  gap {gap:+.0f}s")
