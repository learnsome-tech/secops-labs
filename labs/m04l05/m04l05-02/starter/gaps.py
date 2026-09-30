import csv
from datetime import datetime

with open("timeline.csv", newline="") as f:
    rows = list(csv.DictReader(f))
for r in rows:
    r["at"] = datetime.fromisoformat(r["time"])

# Time the organisation spent before each of its own rows
gaps = [(b["at"] - a["at"], b) for a, b in zip(rows, rows[1:])
        if b["who"] != "attacker"]
gaps.sort(key=lambda g: g[0], reverse=True)
for gap, ended_by in gaps[:4]:
    print(f"{str(gap):17} until {ended_by['who']}: {ended_by['entry']}")
