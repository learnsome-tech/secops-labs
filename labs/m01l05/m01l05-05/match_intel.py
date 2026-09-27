# Security Operations & Threat Hunting (SOC) — lesson m01l05 — Threat Intelligence Platforms & STIX/TAXII Ingestion
# https://learnsome.tech/courses/secops-course/watch?lesson=m01l05
# © LearnSome.tech
import json
from datetime import datetime, timezone

objects = json.load(open("intel_bundle.json"))["objects"]
actor_of = {r["source_ref"]: a for r in objects for a in objects
            if r.get("relationship_type") == "indicates"
            and r["target_ref"] == a["id"]}
watch = {o["pattern"].split("'")[1]: o for o in objects if "pattern" in o}

for line in open("access.log"):
    stamp, _, client, _, _, _, dest, _, peer, _ = line.split()
    seen = datetime.fromtimestamp(float(stamp), timezone.utc)
    for value in (dest.rsplit(":", 1)[0], peer.split("/")[1]):
        if (ind := watch.get(value)) is None:
            continue
        if seen > datetime.fromisoformat(ind["valid_until"]):
            print(f"{seen:%H:%M} {client} {value}: indicator expired, ignored")
            continue
        actor = actor_of[ind["id"]]
        phase = ind["kill_chain_phases"][0]["phase_name"]
        print(f"{seen:%H:%M} {client} {value}: {phase},", actor["name"],
              actor["threat_actor_types"], actor["primary_motivation"])
