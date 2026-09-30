from make_samples import build
from yara_like import STRINGS, loader_rule

for name, data in build().items():
    offsets = {k: [m.start() for p in pats for m in p.finditer(data)]
               for k, pats in STRINGS.items()}
    shown = [f"{k}@{o[0]:#x}" for k, o in offsets.items() if o]
    verdict = "Loader_XorStub" if loader_rule(data) else "-"
    print(f"{name:14} {verdict:15}", *shown)
