# Security Operations & Threat Hunting (SOC) — lesson m01l03 — SIEM Architecture: Ingestion Pipelines & Indexing
# https://learnsome.tech/courses/secops-course/watch?lesson=m01l03
# © LearnSome.tech
import re
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE events (host TEXT, prog TEXT, src_ip TEXT, raw TEXT)")
with open("auth.log") as f:
    for raw in f:
        month, day, clock, host, rest = raw.split(maxsplit=4)
        ip = re.search(r"from (\S+) port", rest)
        db.execute("INSERT INTO events VALUES (?, ?, ?, ?)",
                   (host, rest.split("[")[0], ip and ip[1], raw.strip()))

query = "SELECT prog FROM events WHERE src_ip = '203.0.113.9'"
def plan():
    return db.execute("EXPLAIN QUERY PLAN " + query).fetchone()[3]

print("without index:", plan())
db.execute("CREATE INDEX events_src_ip ON events (src_ip)")
print("with index:   ", plan())
rows = db.execute(query).fetchall()
print(len(rows), "events from 203.0.113.9")
