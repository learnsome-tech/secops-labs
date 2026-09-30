import json
from datetime import datetime
from math import asin, cos, radians, sin, sqrt

def km(a, b):
    la1, lo1 = radians(a["lat"]), radians(a["lon"])
    la2, lo2 = radians(b["lat"]), radians(b["lon"])
    h = (sin((la2 - la1) / 2) ** 2
         + cos(la1) * cos(la2) * sin((lo2 - lo1) / 2) ** 2)
    return 2 * 6371 * asin(sqrt(h))

with open("signins.jsonl") as f:
    rows = sorted(map(json.loads, f), key=lambda e: (e["user"], e["time"]))
for a, b in zip(rows, rows[1:]):
    if a["user"] != b["user"]:
        continue
    gap = datetime.fromisoformat(b["time"]) - datetime.fromisoformat(a["time"])
    speed = km(a, b) / (gap.total_seconds() / 3600)
    verdict = "impossible travel" if speed > 1000 else "plausible"
    print(f"{a['user']:<18} {a['city']}-{b['city']} {km(a, b):,.0f} km,"
          f" {speed:,.0f} km/h, {verdict}")
