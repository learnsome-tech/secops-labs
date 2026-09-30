import csv
from datetime import datetime, timedelta

NOW = datetime.fromisoformat("2026-03-09T08:00")
SILENT = timedelta(hours=24)
# class: (amber above this share, red at or above this share)
LIMITS = {"crown": (0.0, 0.25), "standard": (0.05, 0.20)}

with open("assets.csv", newline="") as f:
    assets = list(csv.DictReader(f))

for cls, (amber, red) in LIMITS.items():
    group = [a for a in assets if a["class"] == cls]
    quiet = [a["host"] for a in group
             if NOW - datetime.fromisoformat(a["last_log"]) > SILENT]
    share = len(quiet) / len(group)
    status = "red" if share >= red else "amber" if share > amber else "green"
    print(f"{cls:<8} silent {len(quiet)} of {len(group)} ({share:.0%})", status)
    for host in quiet:
        print("  ", host)
