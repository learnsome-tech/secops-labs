import json

SUPPRESS = {
    "broad": {"proc.name": "sh"},
    "scoped": {"k8s.ns.name": "backup", "proc.pname": "cron",
               "proc.cmdline": "sh -c /usr/local/bin/backup.sh"},
}

with open("falco_alerts.jsonl") as f:
    alerts = [json.loads(line)["output_fields"] for line in f]

def hidden(fields, rule):
    return all(fields.get(key) == value for key, value in rule.items())

for name, rule in SUPPRESS.items():
    shown = [a for a in alerts if not hidden(a, rule)]
    print(f"{name}: hides {len(alerts) - len(shown)}, shows {len(shown)}")
    for a in shown:
        pod = a["k8s.ns.name"] + "/" + a["k8s.pod.name"]
        print("  ", pod, a["proc.pname"], "->", a["proc.cmdline"])
