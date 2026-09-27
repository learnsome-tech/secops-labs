# Security Operations & Threat Hunting (SOC) — lesson m05l04 — Malware Triage: Hashes, Strings & Sandboxing
# https://learnsome.tech/courses/secops-course/watch?lesson=m05l04
# © LearnSome.tech
import hashlib
import build_sample                  # writes invoice_0342.exe, a harmless PE

data = open("invoice_0342.exe", "rb").read()
print("size  ", len(data), "bytes")
for algo in ("md5", "sha1", "sha256"):
    print(f"{algo:6}", hashlib.new(algo, data).hexdigest())

variant = bytearray(data)
variant[0x400] ^= 0x01               # flip one bit in the code section
a = hashlib.sha256(data).hexdigest()
b = hashlib.sha256(variant).hexdigest()
print("variant sha256", b)
same = sum(x == y for x, y in zip(a, b))
print(f"hex digits in the same place: {same} of 64")
