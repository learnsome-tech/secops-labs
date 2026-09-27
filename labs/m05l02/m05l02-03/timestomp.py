# Security Operations & Threat Hunting (SOC) — lesson m05l02 — Disk Forensics: MFT, UsnJrnl & Prefetch
# https://learnsome.tech/courses/secops-course/watch?lesson=m05l02
# © LearnSome.tech
import struct
from datetime import datetime, timedelta
from mft import records, attributes

def filetime(rec, at):
    ticks = struct.unpack_from("<Q", rec, at)[0]      # 100 ns since 1601
    return datetime(1601, 1, 1) + timedelta(microseconds=ticks // 10), ticks

for number, rec in records("MFT.bin"):
    for kind, body in attributes(rec):
        if kind == 0x10:                               # $STANDARD_INFORMATION
            si, si_ticks = filetime(rec, body)
        if kind == 0x30:                               # $FILE_NAME
            fn, _ = filetime(rec, body + 8)
            chars = rec[body + 64]
            name = rec[body + 66:body + 66 + 2 * chars].decode("utf-16-le")
    print(f"{name:11} SI created {si:%Y-%m-%d %H:%M:%S}"
          f"  FN created {fn:%Y-%m-%d %H:%M:%S}")
    if si < fn:
        print("  SI creation is earlier than FN creation")
    if si_ticks % 10_000_000 == 0:
        print("  SI time has no fraction of a second")
