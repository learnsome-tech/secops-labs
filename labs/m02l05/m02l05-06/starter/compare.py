import hashlib
from make_samples import build
from yara_like import STRINGS, hexstr, loader_rule

samples = build()
ioc = hashlib.sha256(samples["invoice_a.exe"]).hexdigest()  # yesterday's IOC
exact = hexstr("8A 04 0E 34 5A 88 04 0E")                  # no wildcards
every = [p for pats in STRINGS.values() for p in pats]
checks = {
    "sha256 IOC": lambda d: hashlib.sha256(d).hexdigest() == ioc,
    "exact bytes": lambda d: any(p.search(d) for p in exact),
    "any string": lambda d: any(p.search(d) for p in every),
    "loader rule": loader_rule,
}
print(f"{'sample':14}", *(f"{c:12}" for c in checks))
for name, data in samples.items():
    marks = ["hit" if f(data) else "-" for f in checks.values()]
    print(f"{name:14}", *(f"{m:12}" for m in marks))
