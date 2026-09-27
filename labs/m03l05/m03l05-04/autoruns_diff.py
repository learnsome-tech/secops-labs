# Security Operations & Threat Hunting (SOC) — lesson m03l05 — Detecting Persistence: Tasks, Registry & Services
# https://learnsome.tech/courses/secops-course/watch?lesson=m03l05
# © LearnSome.tech
import xml.etree.ElementTree as ET

NS = {"e": "http://schemas.microsoft.com/win/2004/08/events/event"}
FIELDS = {"7045": ("ServiceName", "ImagePath"),
          "13": ("TargetObject", "Details")}
RISKY = ("\\users\\", "\\temp\\", "\\programdata\\", "powershell",
         "cmd.exe /c", "mshta", "rundll32")
baseline = set(open("baseline.txt").read().splitlines())

for event in ET.parse("events.xml").getroot():
    eid = event.findtext("e:System/e:EventID", namespaces=NS)
    data = {d.get("Name"): d.text for d in event.iterfind(".//e:Data", NS)}
    name, command = (data[f] for f in FIELDS[eid])
    command = command.lower()
    if command in baseline:
        verdict = "in baseline"
    else:
        verdict = "new: " + ", ".join(r for r in RISKY if r in command)
    print(f"{eid:<5}{name.split(chr(92))[-1]:<22}{verdict}")
