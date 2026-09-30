"""Writes vads.txt (a trimmed VAD listing) and pid.<pid>.<start>.dmp files
holding the bytes of each private region, as a memory tool would dump them.
The bytes are inert: headers and opening instructions only.
"""
import struct

ROWS = [
    ("3112", "explorer.exe", "0x7ffb1c0a0000", "0x7ffb1c28ffff",
     "PAGE_EXECUTE_WRITECOPY", "0", r"\Windows\System32\ntdll.dll", None),
    ("1880", "svchost.exe", "0x7ff6b2d40000", "0x7ff6b2d4ffff",
     "PAGE_EXECUTE_WRITECOPY", "0", r"\Windows\System32\svchost.exe", None),
    ("6204", "svchost.exe", "0x7ff6b2d40000", "0x7ff6b2d4ffff",
     "PAGE_EXECUTE_READWRITE", "1", "-", "pe"),
    ("5388", "powershell.exe", "0x1c2a0000", "0x1c2affff",
     "PAGE_EXECUTE_READWRITE", "1", "-", "jit"),
    ("5460", "rundll32.exe", "0x2b0000", "0x2bffff",
     "PAGE_EXECUTE_READWRITE", "1", "-", "stub"),
    ("5460", "rundll32.exe", "0x2d0000", "0x2dffff",
     "PAGE_READWRITE", "1", "-", "data"),
]


def region(kind):
    buf = bytearray(4096)
    if kind == "pe":
        buf[0:2] = b"MZ"
        struct.pack_into("<I", buf, 0x3C, 0xF0)
        buf[0xF0:0xF4] = b"PE\0\0"
        struct.pack_into("<HH", buf, 0xF4, 0x8664, 6)
    elif kind == "jit":
        buf[0:12] = bytes.fromhex("48895c2408574883ec20488b")
    elif kind == "stub":
        buf[0:10] = bytes.fromhex("fc4883e4f0e8c0000000")
    else:
        buf[0:16] = b"session=7f3a9c01"
    return bytes(buf)


with open("vads.txt", "w") as f:
    f.write("PID Process Start End Protection Private File\n")
    for pid, name, start, end, prot, private, path, kind in ROWS:
        f.write(" ".join((pid, name, start, end, prot, private, path)) + "\n")
        if kind:
            with open(f"pid.{pid}.{start}.dmp", "wb") as d:
                d.write(region(kind))
