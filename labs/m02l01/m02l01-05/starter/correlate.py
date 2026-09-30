from collections import defaultdict
from datetime import timedelta
from authlog import events

LOOKBACK = timedelta(minutes=10)
MIN_FAILS = 3
fails = defaultdict(list)     # source address -> [(time, account)]

for e in events("auth.log"):
    ip, ts = e["ip"], e["ts"]
    if e["result"] == "Failed":
        fails[ip].append((ts, e["user"]))
        continue
    prior = [(t, u) for t, u in fails[ip] if ts - t <= LOOKBACK]
    tried = " ".join(sorted({u for _, u in prior}))
    verdict = "alert" if len(prior) >= MIN_FAILS else "ok"
    print(f"{ts:%H:%M:%S} {verdict:5} {e['user']:6} from {ip:13} "
          f"after {len(prior)} failure(s), tried: {tried}")
