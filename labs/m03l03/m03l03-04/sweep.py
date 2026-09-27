# Security Operations & Threat Hunting (SOC) — lesson m03l03 — Indicator of Compromise Extraction & Threat Hunting Feeds
# https://learnsome.tech/courses/secops-course/watch?lesson=m03l03
# © LearnSome.tech
import csv
from urllib.parse import urlsplit
from iocs import extract

ioc = extract(open("report.txt").read())
ips, hashes = set(ioc["ipv4"]), set(ioc["sha256"] + ioc["md5"])

for line in open("proxy.log"):
    f = line.split()
    url, peer = f[6], f[8].split("/")[1]
    host = urlsplit(url if "://" in url else "//" + url).hostname
    hits = [d for d in ioc["domain"] if host == d or host.endswith("." + d)]
    if hits or peer in ips:
        print("proxy", f[2], host, "matched", *(hits or [peer]))

for row in csv.DictReader(open("file_events.csv")):
    if row["sha256"] in hashes:
        print("file ", row["host"], row["path"], row["size"], "bytes")
