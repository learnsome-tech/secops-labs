# Security Operations & Threat Hunting (SOC) — lesson m03l02 — Adversary Tactics, Techniques & Procedures (TTP) Mapping
# https://learnsome.tech/courses/secops-course/watch?lesson=m03l02
# © LearnSome.tech
import re
from collections import defaultdict

LINE = re.compile(r"(Failed|Accepted) \w+ for (?:invalid user )?(\S+)"
                  r" from (\S+) port")
fails = defaultdict(list)
wins = []
with open("auth.log") as f:
    for m in filter(None, map(LINE.search, f)):
        result, user, src = m.groups()
        if result == "Failed":
            fails[src].append(user)
        elif src in fails:
            wins.append((src, user))

for src, users in fails.items():
    spread = len(set(users))
    kind = "T1110.003 spraying" if spread > 3 else "T1110.001 guessing"
    print(f"{src:<14} fails {len(users)}, distinct users {spread}: {kind}")
for src, user in wins:
    print(f"{src:<14} then logged in as {user}: treat as compromised")
