# Security Operations & Threat Hunting (SOC) — lesson m05l01 — Forensics Principles, Custody & Imaging
# https://learnsome.tech/courses/secops-course/watch?lesson=m05l01
# © LearnSome.tech
import hashlib
import make_disk

make_disk.build("suspect.raw")          # our stand-in for the seized drive
BLOCK = 64 * 1024
md5, sha = hashlib.md5(), hashlib.sha256()
pieces, total = [], 0                   # one SHA-256 per block
with open("suspect.raw", "rb") as src, open("evidence.img", "wb") as dst:
    while block := src.read(BLOCK):
        md5.update(block)
        sha.update(block)
        pieces.append(hashlib.sha256(block).hexdigest())
        dst.write(block)
        total += len(block)

with open("evidence.img", "rb") as f:
    again = hashlib.file_digest(f, "sha256").hexdigest()
open("evidence.img.sha256", "w").write("\n".join(pieces) + "\n")
print("bytes acquired:", total, "in", len(pieces), "blocks")
print("md5   ", md5.hexdigest())
print("sha256", sha.hexdigest())
print("image re-hash matches acquisition:", again == sha.hexdigest())
