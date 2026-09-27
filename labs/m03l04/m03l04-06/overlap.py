# Security Operations & Threat Hunting (SOC) — lesson m03l04 — Tracking Advanced Persistent Threats & Profiles
# https://learnsome.tech/courses/secops-course/watch?lesson=m03l04
# © LearnSome.tech
import json
from collections import Counter
from math import log

profiles = {k: set(v) for k, v in json.load(open("profiles.json")).items()}
incident = set(open("incident.txt").read().split())
seen_in = Counter(t for techs in profiles.values() for t in techs)

def rarity(t):
    return log((len(profiles) + 1) / (seen_in[t] + 1))

def score(a, b, weight=lambda t: 1):
    return sum(map(weight, a & b)) / sum(map(weight, a | b))

for name, techs in profiles.items():
    print(f"{name:<12} jaccard {score(incident, techs):.2f}  "
          f"weighted {score(incident, techs, rarity):.2f}  "
          f"unseen {' '.join(sorted(techs - incident))}")
