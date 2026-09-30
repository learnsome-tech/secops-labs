import csv
from attack import load_tactics

AOO = "Actions on Objectives"
PHASE = {"reconnaissance": "Reconnaissance",
         "resource-development": "Weaponization",
         "initial-access": "Delivery", "execution": "Exploitation",
         "persistence": "Installation",
         "command-and-control": "Command and Control"}
tactics = load_tactics()
seen = {p: [] for p in ["Reconnaissance", "Weaponization", "Delivery",
                        "Exploitation", "Installation",
                        "Command and Control", AOO]}
with open("incident.csv") as f:
    for row in csv.DictReader(f):
        for phase in {PHASE.get(t, AOO) for t in tactics[row["technique"]]}:
            seen[phase].append(row["time"][11:16])
for phase, times in seen.items():
    span = f"{times[0]} to {times[-1]}" if times else "no evidence"
    print(f"{phase:<22}{len(times)}  {span}")
