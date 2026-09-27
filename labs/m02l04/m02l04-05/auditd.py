# Security Operations & Threat Hunting (SOC) — lesson m02l04 — Windows Event Logs, Sysmon & Linux Auditd Telemetry
# https://learnsome.tech/courses/secops-course/watch?lesson=m02l04
# © LearnSome.tech
import re
from collections import defaultdict
from datetime import datetime, timezone

HEAD = re.compile(r"type=(\w+) msg=audit\((\d+)\.\d+:(\d+)\): (.*)")
FIELD = re.compile(r'(\w+)=("[^"]*"|\S+)')

events = defaultdict(lambda: defaultdict(list))   # serial -> type -> records
with open("audit.log") as f:
    for line in f:
        rtype, secs, serial, rest = HEAD.match(line).groups()
        fields = {k: v.strip('"') for k, v in FIELD.findall(rest)}
        events[(secs, serial)][rtype].append(fields)

for (secs, serial), recs in events.items():
    sc = recs["SYSCALL"][0]
    cmd = bytes.fromhex(recs["PROCTITLE"][0]["proctitle"]).replace(b"\0", b" ")
    when = datetime.fromtimestamp(int(secs), timezone.utc).strftime("%H:%M:%S")
    print(f"{when} #{serial} key={sc['key']} auid={sc['auid']} uid={sc['uid']}")
    print(f"  cmd: {cmd.decode()}  paths:", *(p["name"] for p in recs["PATH"]))
