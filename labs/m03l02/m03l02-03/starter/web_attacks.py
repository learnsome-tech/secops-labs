import re
from urllib.parse import unquote

LOG = re.compile(r'(\S+) \S+ \S+ \[(.+?)\] "\S+ (\S+) [^"]*" (\d+) (\d+)')
CHECKS = [
    ("directory traversal", re.compile(r"\.\./")),
    ("SQL injection", re.compile(r"'\s*or\s|union\s+select", re.I)),
    ("oversized input", re.compile(r"[^&=?]{1024,}")),
]

with open("access.log") as f:
    for line in f:
        src, when, target, status, size = LOG.match(line).groups()
        path = unquote(target)
        for name, pattern in CHECKS:
            if pattern.search(path):
                print(f"{when[12:20]} {src} {name:<19} "
                      f"status {status} bytes {size:>4}  T1190")
