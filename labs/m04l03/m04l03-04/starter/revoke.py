from datetime import datetime
import idp

def at(stamp):
    return int(datetime.fromisoformat(stamp).timestamp())

stolen = idp.issue("j.okafor", at("2026-02-27T22:40:19Z"))
print("stolen token replayed   ", idp.redeem(stolen))

idp.users["j.okafor"]["password"] = "demo-only-2"
print("after password reset    ", idp.redeem(stolen))

idp.users["j.okafor"]["valid_from"] = at("2026-03-02T10:05:11Z")
print("after revoking sessions ", idp.redeem(stolen))

fresh = idp.issue("j.okafor", at("2026-03-02T12:15:00Z"))
print("user signs in again     ", idp.redeem(fresh))

forged = fresh.split(b".")[0] + b"." + stolen.split(b".")[1]
print("new date, old signature ", idp.redeem(forged))
