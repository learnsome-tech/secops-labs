import ipaddress
import re
REFANG = [("hxxp", "http"), ("[.]", "."), ("[:]", ":")]
LOCAL = [ipaddress.ip_network(n) for n in
         ("10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16", "127.0.0.0/8")]
PATTERNS = {"url": r"https?://[^\s\"'<>]+",
            "ipv4": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
            "domain": r"\b(?:[a-z0-9-]+\.)+(?:com|net|org)\b",
            "sha256": r"\b[a-f0-9]{64}\b", "md5": r"\b[a-f0-9]{32}\b"}

def extract(text):
    for old, new in REFANG:
        text = text.replace(old, new)
    found = {k: sorted(set(re.findall(p, text))) for k, p in PATTERNS.items()}
    found["ipv4"] = [v for v in found["ipv4"] if not any(
        ipaddress.ip_address(v) in net for net in LOCAL)]
    return found
if __name__ == "__main__":
    for kind, values in extract(open("report.txt").read()).items():
        print(*(f"{kind:<7}{v}" for v in values), sep="\n")
