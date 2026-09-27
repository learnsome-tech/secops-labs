# Security Operations & Threat Hunting (SOC) — lesson m05l04 — Malware Triage: Hashes, Strings & Sandboxing
# https://learnsome.tech/courses/secops-course/watch?lesson=m05l04
# © LearnSome.tech
import hashlib
import xml.etree.ElementTree as ET
import build_sample

NS = "{http://schemas.microsoft.com/win/2004/08/events/event}"
sample = open("invoice_0342.exe", "rb").read()
iocs = {"SHA256": hashlib.sha256(sample).hexdigest().upper(),
        "IMPHASH": "82A7041495E66185C753F958D7A33F65",
        "QueryName": "cdn.example.com"}

for event in ET.parse("sysmon.xml").getroot():
    host = event.find(f"{NS}System/{NS}Computer").text.split(".")[0]
    eid = event.find(f"{NS}System/{NS}EventID").text
    data = {d.get("Name"): d.text for d in event.iter(f"{NS}Data")}
    hashes = data.get("Hashes", "")        # "MD5=..,SHA256=..,IMPHASH=.."
    fields = dict(h.split("=") for h in hashes.split(",") if h) | data
    image = data["Image"].split("\\")[-1]
    for key, value in iocs.items():
        if fields.get(key) == value:
            print(f"{data['UtcTime'][11:19]} {host} event {eid:2} "
                  f"{key} match, image {image}")
