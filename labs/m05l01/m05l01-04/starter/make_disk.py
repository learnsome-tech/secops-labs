"""Builds suspect.raw, a one mebibyte stand-in for a seized drive.

The bytes are pseudo-random but fixed, so every run produces the same image
and the same hashes. A real acquisition reads the drive's device node through
a write blocker instead of this file.
"""
import hashlib


def build(path="suspect.raw", size=1024 * 1024):
    out = bytearray()
    counter = 0
    while len(out) < size:
        out += hashlib.sha256(b"LT-0419 sector stream %d" % counter).digest()
        counter += 1
    del out[size:]
    out[510:512] = b"\x55\xaa"  # MBR boot signature
    note = b"invoice_0342.exe downloaded from cdn.example.com"
    out[0x50000:0x50000 + len(note)] = note
    with open(path, "wb") as f:
        f.write(out)
