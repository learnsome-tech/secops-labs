import csv
from collections import Counter, defaultdict

by_rule = defaultdict(Counter)
with open("closed_alerts.csv", newline="") as f:
    for row in csv.DictReader(f):
        by_rule[row["rule"]][row["disposition"]] += 1

total = sum(sum(c.values()) for c in by_rule.values())
print(f"{'rule':<30} fired  true benign false precision queue")
for rule, c in sorted(by_rule.items(), key=lambda kv: -kv[1].total()):
    fired = c.total()
    true = c["true_positive"]
    print(f"{rule:<30} {fired:5} {true:5} {c['benign_true_positive']:6}"
          f" {c['false_positive']:5} {true / fired:9.0%} {fired / total:5.0%}")
