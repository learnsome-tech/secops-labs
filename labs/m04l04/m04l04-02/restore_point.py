# Security Operations & Threat Hunting (SOC) — lesson m04l04 — Recovery & System Validation Testing
# https://learnsome.tech/courses/secops-course/watch?lesson=m04l04
# © LearnSome.tech
import csv, hashlib
from datetime import datetime

FIRST_ATTACKER_ACTION = datetime.fromisoformat("2026-02-28T03:12:40Z")

with open("catalogue.csv", newline="") as f:
    backups = sorted(csv.DictReader(f), key=lambda b: b["taken"], reverse=True)

for b in backups:
    if datetime.fromisoformat(b["taken"]) >= FIRST_ATTACKER_ACTION:
        print(b["file"], " taken after the first attacker action, skip")
        continue
    with open(b["file"], "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    if digest != b["sha256"]:
        print(b["file"], " hash differs from catalogue, skip")
        continue
    print(b["file"], " predates the attacker and is intact: restore")
    print("changes since", b["taken"], "must be replayed or re-entered")
    break
