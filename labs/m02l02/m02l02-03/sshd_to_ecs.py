# Security Operations & Threat Hunting (SOC) — lesson m02l02 — Log Parsing, Schema Normalization (OCSF/ECS) & Extraction
# https://learnsome.tech/courses/secops-course/watch?lesson=m02l02
# © LearnSome.tech
import re
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

SSHD = re.compile(r"(\w{3} [ \d]\d [\d:]{8}) (\S+) sshd\[\d+\]: (Failed|"
                  r"Accepted) \S+ for (?:invalid user )?(\S+) from (\S+) port")
def from_sshd(line, tz, year=2026):
    if not (m := SSHD.match(line)):
        return None      # caller counts unparsed lines; never drop them quietly
    ts, host, result, user, ip = m.groups()
    t = datetime.strptime(f"{year} {ts}", "%Y %b %d %H:%M:%S")
    utc = t.replace(tzinfo=tz).astimezone(timezone.utc)
    return {"@timestamp": utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "event.category": "authentication", "event.provider": "sshd",
            "event.outcome": "success" if result == "Accepted" else "failure",
            "user.name": user, "source.ip": ip, "host.name": host}

if __name__ == "__main__":
    line = open("auth.log").readline()
    for k, v in from_sshd(line, ZoneInfo("Europe/London")).items():
        print(f"{k:15} {v}")
