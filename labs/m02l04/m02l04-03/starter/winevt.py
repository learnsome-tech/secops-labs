import xml.etree.ElementTree as ET

NS = {"e": "http://schemas.microsoft.com/win/2004/08/events/event"}
SEC, SYSMON = "Microsoft-Windows-Security-Auditing", "Microsoft-Windows-Sysmon"
WANT = {  # event ids are unique per provider, so key on both
    (SEC, "4624"): ["TargetUserName", "LogonType", "IpAddress"],
    (SEC, "4688"): ["NewProcessName", "CommandLine"],
    (SYSMON, "1"): ["ParentCommandLine", "User"],
}

for ev in ET.parse("events.xml").getroot().iterfind("e:Event", NS):
    sys_ = ev.find("e:System", NS)
    provider = sys_.find("e:Provider", NS).get("Name")
    eid = sys_.findtext("e:EventID", namespaces=NS)
    when = sys_.find("e:TimeCreated", NS).get("SystemTime")[11:19]
    data = {d.get("Name"): d.text for d in ev.iterfind(".//e:Data", NS)}
    shown = [data[k] for k in WANT.get((provider, eid), [])]
    source = provider.removeprefix("Microsoft-Windows-")
    print(when, f"{source:17} {eid:>4}", " | ".join(shown))
