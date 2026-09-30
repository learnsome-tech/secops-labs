import re
import socket

FACILITY = {0: "kern", 4: "auth", 10: "authpriv"}
SEVERITY = "emerg alert crit err warning notice info debug".split()

collector = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
collector.bind(("127.0.0.1", 0))
sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
lines = open("forwarded.log", "rb").read().splitlines()
for line in lines:
    sender.sendto(line, collector.getsockname())

for _ in lines:
    data = collector.recv(8192).decode()
    m = re.match(r"<(\d{1,3})>1 (\S+) (\S+) (\S+) \S+ \S+ \S+ (.*)", data)
    if not m:
        print("no header, stored raw:", data)
        continue
    facility, severity = divmod(int(m[1]), 8)
    label = f"{FACILITY[facility]}.{SEVERITY[severity]}"
    print(f"{label:<16}{m[3]:<20}{m[4]:<7}{m[5][:37]}")
