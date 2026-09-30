import csv
from collections import defaultdict

SHARED = {"redacted@privacy.example"}
def clusters(rows, ignore):
    parent = {}
    def find(x):
        while parent.setdefault(x, x) != x:
            x = parent[x]
        return x
    for row in rows:
        for field in ("cert_sha1", "registrant"):
            if row[field] not in ignore | {"-"}:
                parent[find(row["incident"])] = find(row[field])
    groups = defaultdict(set)
    for row in rows:
        groups[find(row["incident"])].add(row["incident"])
    return sorted(sorted(g) for g in groups.values())

rows = list(csv.DictReader(open("infra.csv")))
for label, ignore in (("naive", set()), ("shared values ignored", SHARED)):
    print(label, *(", ".join(g) for g in clusters(rows, ignore)), sep="\n  ")
