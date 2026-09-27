# Security Operations & Threat Hunting (SOC) — lesson m02l05 — YARA Rule Authoring & File Signature Matching
# https://learnsome.tech/courses/secops-course/watch?lesson=m02l05
# © LearnSome.tech
import re

def text(s, wide=False, nocase=False):
    forms = [s.encode()] + ([s.encode("utf-16-le")] if wide else [])
    return [re.compile(re.escape(f), re.I if nocase else 0) for f in forms]

def hexstr(spec):                    # "??" matches any one byte
    parts = [b"." if t == "??" else re.escape(bytes.fromhex(t))
             for t in spec.split()]
    return [re.compile(b"".join(parts), re.S)]

STRINGS = {"$mutex": text("Global\\Xq7-updater", wide=True),
           "$gate": text("/gate.php"),
           "$ps": text("powershell -nop -w hidden", wide=True, nocase=True),
           "$xor": hexstr("8A 04 ?? 34 ?? 88 04 ??")}

def loader_rule(data):
    hit = {k: any(p.search(data) for p in v) for k, v in STRINGS.items()}
    two = sum(hit[k] for k in ("$mutex", "$gate", "$ps")) >= 2
    return data[:2] == b"MZ" and len(data) < 2 * 2**20 and hit["$xor"] and two
