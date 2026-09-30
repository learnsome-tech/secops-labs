import re, sqlite3, sys
from datetime import datetime

SSHD = re.compile(r"(\w+ +\d+ [\d:]+) (\S+) sshd\[\d+\]: (Accepted|Failed) "
                  r"password for (?:invalid user )?(\S+) from (\S+)")
rule = open("success_after_failures.sql").read()

for path in sys.argv[1:]:
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE auth (ts, host, result, user, src)")
    for line in open(path):
        stamp, *fields = SSHD.search(line).groups()
        ts = datetime.strptime("2026 " + stamp, "%Y %b %d %H:%M:%S")
        db.execute("INSERT INTO auth VALUES (?, ?, ?, ?, ?)",
                   (ts.isoformat(" "), *fields))
    hits = db.execute(rule).fetchall()
    print(f"{path}: {len(hits)} hit(s)")
    for ts, host, user, src, failures in hits:
        print(f"  {ts} {host} {user} from {src} after {failures} failures")
