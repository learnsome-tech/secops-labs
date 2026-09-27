# Security Operations & Threat Hunting (SOC) — lesson m03l04 — Tracking Advanced Persistent Threats & Profiles
# https://learnsome.tech/courses/secops-course/watch?lesson=m03l04
# © LearnSome.tech
import json
import re


def key(name):
    return re.sub(r"[^a-z0-9]", "", name.lower())


groups = json.load(open("groups.json"))
index = {}
for gid, group in groups.items():
    for name in [group["name"], *group["aliases"]]:
        index[key(name)] = f"{gid} {group['name']}"

for mention in open("mentions.txt").read().splitlines():
    found = index.get(key(mention), "no match, possible new cluster")
    print(f"{mention:<20} {found}")
