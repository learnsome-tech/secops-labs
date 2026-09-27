# Security Operations & Threat Hunting (SOC) — lesson m03l03 — Indicator of Compromise Extraction & Threat Hunting Feeds
# https://learnsome.tech/courses/secops-course/watch?lesson=m03l03
# © LearnSome.tech
import csv
from datetime import date

TODAY = date(2026, 9, 27)
TTL_DAYS = {"ipv4": 30, "domain": 90, "sha256": 365}
MIN_CONFIDENCE = 60
KNOWN_GOOD = {"corp.example.com",
              "e3b0c44298fc1c149afbf4c8996fb924"
              "27ae41e4649b934ca495991b7852b855"}
for row in csv.DictReader(open("feed.csv")):
    age = (TODAY - date.fromisoformat(row["last_seen"])).days
    if row["value"] in KNOWN_GOOD:
        verdict = "drop: known benign"
    elif age > TTL_DAYS[row["type"]]:
        verdict = f"drop: last seen {age} days ago"
    elif int(row["confidence"]) < MIN_CONFIDENCE:
        verdict = f"drop: confidence {row['confidence']}"
    else:
        verdict = "keep"
    print(f"{row['type']:<7}{row['value'][:26]:<27}{verdict}")
