# Security Operations & Threat Hunting (SOC) — lesson m01l05 — Threat Intelligence Platforms & STIX/TAXII Ingestion
# https://learnsome.tech/courses/secops-course/watch?lesson=m01l05
# © LearnSome.tech
import json
import urllib.request
from taxii_server import start  # the local stand-in server

collection = "91a7b528-80eb-42ed-a74d-c6fbd5a26116"
url = f"{start()}/api1/collections/{collection}/objects/"
accept = {"Accept": "application/taxii+json;version=2.1"}
query = "?added_after=2026-03-01T00:00:00Z&limit=3"
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

objects, cursor = [], ""
while cursor is not None:
    request = urllib.request.Request(url + query + cursor, headers=accept)
    with opener.open(request) as response:
        envelope = json.load(response)
        last = response.headers["X-TAXII-Date-Added-Last"]
    objects += envelope["objects"]
    print(f"got {len(envelope['objects'])}, last added {last},",
          "more" if envelope["more"] else "done")
    cursor = "&next=" + envelope["next"] if envelope["more"] else None

print(len(objects), "objects:", sorted({o["type"] for o in objects}))
