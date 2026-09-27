# Security Operations & Threat Hunting (SOC) — lesson m02l01 — Event Correlation Rules, Thresholds & Anomaly Pipelines
# https://learnsome.tech/courses/secops-course/watch?lesson=m02l01
# © LearnSome.tech
import re
from datetime import datetime

SSHD = re.compile(
    r"^(?P<ts>\w{3} [ \d]\d \d\d:\d\d:\d\d) (?P<host>\S+) sshd\[\d+\]: "
    r"(?P<result>Failed|Accepted) password for (?:invalid user )?"
    r"(?P<user>\S+) from (?P<ip>\S+) port \d+ ssh2$")

def events(path, year=2026):
    """One dict per sshd password attempt. Syslog omits the year."""
    with open(path) as f:
        for line in f:
            if m := SSHD.match(line.rstrip("\n")):
                e = m.groupdict()
                stamp = f"{year} {e['ts']}"
                e["ts"] = datetime.strptime(stamp, "%Y %b %d %H:%M:%S")
                yield e

if __name__ == "__main__":
    for e in list(events("auth.log"))[:3]:
        print(e["ts"], e["result"], e["user"], e["ip"])
