import xml.etree.ElementTree as ET

EV = {"e": "http://schemas.microsoft.com/win/2004/08/events/event"}
T = {"t": "http://schemas.microsoft.com/windows/2004/02/mit/task"}
SIDS = {"S-1-5-18": "SYSTEM", "S-1-5-19": "LOCAL SERVICE",
        "S-1-5-20": "NETWORK SERVICE"}

event = ET.parse("task-4698.xml").getroot()
data = {d.get("Name"): d.text for d in event.iterfind(".//e:Data", EV)}
task = ET.fromstring(data["TaskContent"])
user = task.findtext(".//t:UserId", namespaces=T)
action = [task.findtext(f".//t:Exec/t:{f}", "", T)
          for f in ("Command", "Arguments")]

print("host   ", event.findtext(".//e:Computer", namespaces=EV))
print("created", data["TaskName"], "by", data["SubjectUserName"])
print("runs as", SIDS.get(user, user), task.findtext(".//t:RunLevel", "", T))
print("trigger", *(el.tag.split("}")[1] for el in task.find("t:Triggers", T)))
print("command", " ".join(action))
