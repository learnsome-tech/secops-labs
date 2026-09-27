# Security Operations & Threat Hunting (SOC) — lesson m02l01 — Event Correlation Rules, Thresholds & Anomaly Pipelines
# https://learnsome.tech/courses/secops-course/watch?lesson=m02l01
# © LearnSome.tech
from collections import defaultdict, deque
from datetime import timedelta
from authlog import events

WINDOW = timedelta(seconds=60)
LIMIT = 5
recent = defaultdict(deque)   # source address -> recent failure times
peak = defaultdict(int)

for e in events("auth.log"):
    if e["result"] != "Failed":
        continue
    q = recent[e["ip"]]
    q.append(e["ts"])
    while e["ts"] - q[0] > WINDOW:
        q.popleft()
    peak[e["ip"]] = max(peak[e["ip"]], len(q))
    if len(q) == LIMIT:
        print(f"{e['ts']:%H:%M:%S} alert: {LIMIT} failures from {e['ip']}")

for ip, n in peak.items():
    print(f"{ip:<15} peak {n} failure(s) in any 60s window")
