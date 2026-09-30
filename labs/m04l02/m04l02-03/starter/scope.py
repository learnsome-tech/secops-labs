import csv, re

SSHD = re.compile(r"([\d:]+) (\S+) sshd\[\d+\]: (Accepted|Failed) "
                  r"password for (\S+) from (\S+)")
with open("inventory.csv", newline="") as f:
    ip_of = {r["host"]: r["ip"] for r in csv.DictReader(f)}
name_of = {ip: host for host, ip in ip_of.items()}
tainted, scope, tried = {"203.0.113.50"}, [], set()
for line in open("auth.log"):
    when, host, result, user, src = SSHD.search(line).groups()
    if src not in tainted:
        continue
    source = name_of.get(src, src)
    print(f"{when} {host:10} {user:7} from {source:13} {result}")
    if result == "Accepted":
        tainted.add(ip_of[host])
        scope.append(host)
    tried.add(host)
print("in scope:", ", ".join(dict.fromkeys(scope)))
print("watch:   ", ", ".join(sorted(tried - set(scope))))
