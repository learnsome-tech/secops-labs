# Security Operations & Threat Hunting (SOC) — lesson m05l04 — Malware Triage: Hashes, Strings & Sandboxing
# https://learnsome.tech/courses/secops-course/watch?lesson=m05l04
# © LearnSome.tech
"""Writes invoice_0342.exe: a harmless training sample laid out as a PE32+
file. It has real DOS, PE, section and import structures and the kind of
strings a loader carries, but its code section is filled with int3 (0xCC)
and it does nothing if run.
"""
import struct

IMPORTS = {
    "KERNEL32.dll": ["OpenProcess", "VirtualAllocEx", "WriteProcessMemory",
                     "CreateRemoteThread", "Sleep"],
    "WININET.dll": ["InternetOpenA", "InternetOpenUrlA", "InternetReadFile"],
    "ADVAPI32.dll": ["RegSetValueExW"],
}
ASCII = [b"https://cdn.example.com/update/p.bin", b"198.51.100.23",
         b"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"]
WIDE = [r"Software\Microsoft\Windows\CurrentVersion\Run",
        r"Global\mtx-7f3a9c01", r"%APPDATA%\Microsoft\updsvc.exe"]

TEXT_RVA, TEXT_RAW, RDATA_RVA, RDATA_RAW = 0x1000, 0x400, 0x2000, 0x600


def rdata():
    """Import directory, lookup tables, hint/name entries, then strings."""
    dlls = list(IMPORTS)
    desc_size = 20 * (len(dlls) + 1)
    blob = bytearray(desc_size)
    lookups = []
    for dll in dlls:  # reserve an 8-byte slot per function plus terminator
        lookups.append(len(blob))
        blob += bytes(8 * (len(IMPORTS[dll]) + 1))
    for i, dll in enumerate(dlls):
        name_rva = RDATA_RVA + len(blob)
        blob += dll.encode() + b"\0"
        blob += b"\0" * (len(blob) % 2)
        for j, func in enumerate(IMPORTS[dll]):
            struct.pack_into("<Q", blob, lookups[i] + 8 * j,
                             RDATA_RVA + len(blob))
            blob += struct.pack("<H", 0) + func.encode() + b"\0"
            blob += b"\0" * (len(blob) % 2)
        ilt = RDATA_RVA + lookups[i]
        struct.pack_into("<IIIII", blob, 20 * i, ilt, 0, 0, name_rva, ilt)
    for s in ASCII:
        blob += b"\0\0" + s + b"\0"
    for s in WIDE:
        blob += b"\0\0" + s.encode("utf-16-le") + b"\0\0"
    return bytes(blob)


def build(path="invoice_0342.exe"):
    body = rdata()
    rdata_size = (len(body) + 0x1FF) // 0x200 * 0x200
    dos = bytearray(0x80)
    dos[0:2] = b"MZ"
    struct.pack_into("<I", dos, 0x3C, 0x80)
    dos[0x4E:0x4E + 39] = b"This program cannot be run in DOS mode."
    coff = struct.pack("<4sHHIIIHH", b"PE\0\0", 0x8664, 2, 0x67E2A1C0, 0, 0,
                       240, 0x22)
    opt = bytearray(240)
    struct.pack_into("<HBBIIIII", opt, 0, 0x20B, 14, 0, 0x200, rdata_size, 0,
                     TEXT_RVA, TEXT_RVA)
    struct.pack_into("<QII", opt, 24, 0x140000000, 0x1000, 0x200)
    struct.pack_into("<HHHHHH", opt, 40, 6, 0, 0, 0, 6, 0)
    struct.pack_into("<I", opt, 108, 16)
    struct.pack_into("<III", opt, 56, 0x3000, 0x400, 0)
    struct.pack_into("<H", opt, 68, 2)  # subsystem: Windows GUI
    struct.pack_into("<II", opt, 120, RDATA_RVA, 20 * (len(IMPORTS) + 1))
    sections = (struct.pack("<8sIIIIIIHHI", b".text", 0x200, TEXT_RVA, 0x200,
                            TEXT_RAW, 0, 0, 0, 0, 0x60000020)
                + struct.pack("<8sIIIIIIHHI", b".rdata", len(body), RDATA_RVA,
                              rdata_size, RDATA_RAW, 0, 0, 0, 0, 0x40000040))
    headers = bytes(dos) + coff + bytes(opt) + sections
    image = headers.ljust(TEXT_RAW, b"\0") + b"\xcc" * 0x200
    image += body.ljust(rdata_size, b"\0")
    with open(path, "wb") as f:
        f.write(image)


build()
