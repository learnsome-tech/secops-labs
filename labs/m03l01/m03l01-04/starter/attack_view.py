import csv
import json
with open("enterprise-attack.json") as f:
    bundle = json.load(f)
tactics = {}
for obj in bundle["objects"]:
    if obj["type"] != "attack-pattern":
        continue
    ref = next(r for r in obj["external_references"]
               if r["source_name"] == "mitre-attack")
    tactics[ref["external_id"]] = [
        p["phase_name"] for p in obj["kill_chain_phases"]
        if p["kill_chain_name"] == "mitre-attack"]
with open("incident.csv") as f:
    for row in csv.DictReader(f):
        tid = row["technique"]
        print(row["time"][11:16], f"{tid:<10}", ", ".join(tactics[tid]))
