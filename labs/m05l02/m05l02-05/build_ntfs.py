# Security Operations & Threat Hunting (SOC) — lesson m05l02 — Disk Forensics: MFT, UsnJrnl & Prefetch
# https://learnsome.tech/courses/secops-course/watch?lesson=m05l02
# © LearnSome.tech
"""Writes MFT.bin and J.bin: NTFS artefacts as they would be exported from
an image (three $MFT FILE records and a $UsnJrnl:$J excerpt). Layouts follow
the on-disk NTFS structures; the content is a made-up case.
"""
import struct
from datetime import datetime, timedelta


def ft(text):
    """ISO time with microseconds -> FILETIME (100 ns ticks since 1601)."""
    d = datetime.fromisoformat(text) - datetime(1601, 1, 1)
    return (d.days * 86400 + d.seconds) * 10_000_000 + d.microseconds * 10


def attr(kind, ident, content):
    header = struct.pack("<IIBBHHHIHBx", kind, 0, 0, 0, 0x18, 0, ident,
                         len(content), 0x18, 0)
    body = header + content
    body += b"\0" * (-len(body) % 8)
    return body[:4] + struct.pack("<I", len(body)) + body[8:]


def record(number, name, parent, si, fn, in_use=True, data=b""):
    si_body = struct.pack("<QQQQ", *si) + b"\0" * 40
    raw = name.encode("utf-16-le")
    fn_body = (struct.pack("<QQQQQQQII", parent | (5 << 48), *fn, 4096,
                           len(data), 0x20, 0)
               + struct.pack("<BB", len(name), 3) + raw)
    attrs = (attr(0x10, 0, si_body) + attr(0x30, 2, fn_body)
             + attr(0x80, 3, data) + struct.pack("<II", 0xFFFFFFFF, 0))
    used = 56 + len(attrs)
    rec = bytearray(1024)
    struct.pack_into("<4sHHQHHHHIIQHHI", rec, 0, b"FILE", 48, 3,
                     0x2A3F10 + number, 1, 1, 56, 1 if in_use else 0,
                     used, 1024, 0, 4, 0, number)
    rec[56:56 + len(attrs)] = attrs
    usn = struct.pack("<H", 0x0007)
    usa = usn + bytes(rec[510:512]) + bytes(rec[1022:1024])
    rec[48:54] = usa
    rec[510:512] = usn
    rec[1022:1024] = usn
    return bytes(rec)


def four(text):
    return [ft(text)] * 4


MFT = [
    record(41, "report.docx", 3112, four("2026-02-27 14:03:51.228417"),
           four("2026-02-27 14:03:51.228417"), data=b"PK\x03\x04"),
    record(42, "update.exe", 3112, four("2019-06-11 10:20:00"),
           four("2026-03-02 08:52:14.906311"), data=b"MZ\x90\x00"),
    record(43, "stage.ps1", 3112, four("2026-03-02 08:52:11.402877"),
           four("2026-03-02 08:52:11.402877"), in_use=False,
           data=b"iwr https"),
]

EVENTS = [
    (43, "stage.ps1", "2026-03-02 08:52:11.402877", 0x100),
    (43, "stage.ps1", "2026-03-02 08:52:11.419003", 0x80000102),
    (42, "update.tmp", "2026-03-02 08:52:14.906311", 0x80000102),
    (42, "update.tmp", "2026-03-02 08:52:15.117420", 0x1000),
    (42, "update.exe", "2026-03-02 08:52:15.117420", 0x80002000),
    (42, "update.exe", "2026-03-02 08:52:16.530962", 0x80008000),
    (43, "stage.ps1", "2026-03-02 08:53:02.771045", 0x80000200),
]


def usn_record(usn, ref, name, when, reason):
    raw = name.encode("utf-16-le")
    size = 60 + len(raw)
    size += -size % 8
    head = struct.pack("<IHHQQqQIIIIHH", size, 2, 0, ref | (1 << 48),
                       3112 | (5 << 48), usn, ft(when), reason, 0, 0, 0x20,
                       len(raw), 60)
    return (head + raw).ljust(size, b"\0")


with open("MFT.bin", "wb") as f:
    f.write(b"".join(MFT))

journal = bytearray(4096)  # $J starts sparse: zeros before the live records
for ref, name, when, reason in EVENTS:
    journal += usn_record(0x1D4C000 + len(journal), ref, name, when, reason)
with open("J.bin", "wb") as f:
    f.write(journal)
