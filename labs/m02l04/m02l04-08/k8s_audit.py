# Security Operations & Threat Hunting (SOC) — lesson m02l04 — Windows Event Logs, Sysmon & Linux Auditd Telemetry
# https://learnsome.tech/courses/secops-course/watch?lesson=m02l04
# © LearnSome.tech
import json

def interesting(e):
    ref = e.get("objectRef", {})
    return (ref.get("resource") == "secrets" or ref.get("subresource") == "exec"
            or e["annotations"]["authorization.k8s.io/decision"] == "forbid")

with open("audit.jsonl") as f:
    for e in filter(interesting, map(json.loads, f)):
        ref = e["objectRef"]
        what = "/".join(filter(None, (ref["resource"], ref.get("subresource"),
                                      ref.get("namespace"), ref.get("name"))))
        agent = e["userAgent"].split(" ")[0]
        print(e["stageTimestamp"][11:19], f"{e['verb']:6} {what:30}",
              e["user"]["username"], e["sourceIPs"][0], agent,
              e["annotations"]["authorization.k8s.io/decision"],
              e["responseStatus"]["code"])
