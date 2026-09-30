import hashlib, shutil, subprocess

subprocess.run(["python3", "image.py"], check=True, capture_output=True)
recorded = open("evidence.img.sha256").read().split()
shutil.copy("evidence.img", "working.img")      # analysis happens on a copy

with open("working.img", "r+b") as f:           # a tool writes one byte
    f.seek(5 * 65536 + 1234)
    old = f.read(1)
    f.seek(-1, 1)
    f.write(bytes([old[0] ^ 0x01]))

BLOCK = 64 * 1024
for name in ("evidence.img", "working.img"):
    with open(name, "rb") as f:
        now = [hashlib.sha256(b).hexdigest()
               for b in iter(lambda: f.read(BLOCK), b"")]
    bad = [i for i, (a, b) in enumerate(zip(recorded, now)) if a != b]
    print(f"{name}: {len(now) - len(bad)} of {len(now)} blocks match")
    for i in bad:
        print(f"  block {i}: bytes {i * BLOCK} to {(i + 1) * BLOCK - 1} differ")
