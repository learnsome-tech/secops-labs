# Security Operations & Threat Hunting (SOC) — lesson m02l03 — Detection as Code: Authoring & Testing Sigma Rules
# https://learnsome.tech/courses/secops-course/watch?lesson=m02l03
# © LearnSome.tech
import copy, json
from sigma_match import matches
from hunt import DETECTION

def variant(values):
    d = copy.deepcopy(DETECTION)
    d["selection_cli"]["CommandLine|contains"] = values
    return d

RULES = {"v1 as written": DETECTION,
         "broadened": variant([" -e"]),
         "v2": variant([" -e ", " -en ", " -enc ", " -enco", " -ec "])}

with open("tests.jsonl") as f:
    cases = [json.loads(line) for line in f]
for name, rule in RULES.items():
    bad = [c["name"] for c in cases if matches(c["event"], rule) != c["expect"]]
    print(f"{name:14} {len(cases) - len(bad)}/{len(cases)} pass", *bad)
