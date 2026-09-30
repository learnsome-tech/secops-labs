import json

def from_cloudtrail(r):
    """One CloudTrail ConsoleLogin record as ECS authentication fields."""
    return {"@timestamp": r["eventTime"],
            "event.category": "authentication",
            "event.provider": r["eventSource"],
            "event.outcome": r["responseElements"]["ConsoleLogin"].lower(),
            "event.reason": r.get("errorMessage", ""),
            "user.name": r["userIdentity"]["userName"],
            "source.ip": r["sourceIPAddress"],
            "cloud.account.id": r["recipientAccountId"]}

if __name__ == "__main__":
    with open("cloudtrail.json") as f:
        for record in json.load(f)["Records"]:
            for k, v in from_cloudtrail(record).items():
                print(f"{k:16} {v}")
