import csv

with open("inventory.csv", newline="") as f:
    assets = {r["host"]: r for r in csv.DictReader(f)}
DATA = ["none", "proprietary", "personal"]
NOTIFY = {"SEV1": "IC, CISO, legal, DPO, comms lead",
          "SEV2": "IC, CISO, service owners",
          "SEV3": "SOC lead"}

def rate(label, hosts):
    rows = [assets[h] for h in hosts]
    worst = max((r["data"] for r in rows), key=DATA.index)
    critical = sum(r["critical"] == "yes" for r in rows)
    sev = "SEV2" if worst == "proprietary" or critical else "SEV3"
    if worst == "personal":
        sev = "SEV1"
    print(f"{label}: {len(rows)} hosts, data {worst}, {critical} critical")
    print(f"  {sev}, notify {NOTIFY[sev]}")

rate("first report", ["bastion01"])
rate("after scoping", ["bastion01", "app02", "db01"])
