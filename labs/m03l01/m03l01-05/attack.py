# Security Operations & Threat Hunting (SOC) — lesson m03l01 — Cyber Kill Chain vs MITRE ATT&CK Framework
# https://learnsome.tech/courses/secops-course/watch?lesson=m03l01
# © LearnSome.tech
import json


def load_tactics(path="enterprise-attack.json"):
    # Map each ATT&CK technique ID to the tactics it serves.
    with open(path) as f:
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
    return tactics
