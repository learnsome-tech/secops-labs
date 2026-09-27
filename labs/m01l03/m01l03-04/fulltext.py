# Security Operations & Threat Hunting (SOC) — lesson m01l03 — SIEM Architecture: Ingestion Pipelines & Indexing
# https://learnsome.tech/courses/secops-course/watch?lesson=m01l03
# © LearnSome.tech
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE VIRTUAL TABLE logs USING fts5(host, msg)")
with open("auth.log") as f:
    for line in f:
        month, day, clock, host, msg = line.split(maxsplit=4)
        db.execute("INSERT INTO logs VALUES (?, ?)", (host, msg.strip()))

db.execute("CREATE VIRTUAL TABLE terms USING fts5vocab(logs, row)")
ip_terms = db.execute("SELECT term FROM terms WHERE term IN "
                      "('203', '0', '113', '9', '203.0.113.9')").fetchall()
print("terms stored for the address:", [t for (t,) in ip_terms])

for search in ['"203.0.113.9" AND accepted', "shadow"]:
    print("search:", search)
    for host, msg in db.execute(
            "SELECT host, msg FROM logs WHERE logs MATCH ?", (search,)):
        print("  ", host, msg[-60:])
