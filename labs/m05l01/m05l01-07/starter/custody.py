import csv

ACQUIRED = "36d94d69f8a28cc1"       # first 16 hex digits of the image hash

with open("custody-LT-0419.csv", newline="") as f:
    rows = list(csv.DictReader(f))
holder, when = rows[0]["received_by"], rows[0]["utc"]
for n, row in enumerate(rows[1:], start=2):
    if row["released_by"] != holder:
        print(f"row {n}: released by {row['released_by']}, "
              f"but the last recorded holder is {holder}")
    if row["utc"] < when:
        print(f"row {n}: {row['utc']} is earlier than the entry before it")
    if row["sha256"] and row["sha256"] != ACQUIRED:
        print(f"row {n}: hash {row['sha256']} does not match acquisition")
    holder, when = row["received_by"], row["utc"]
print(f"{len(rows)} entries checked, item now held by {holder}")
