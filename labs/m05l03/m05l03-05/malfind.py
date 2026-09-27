# Security Operations & Threat Hunting (SOC) — lesson m05l03 — Memory Forensics: Process Trees & Injection
# https://learnsome.tech/courses/secops-course/watch?lesson=m05l03
# © LearnSome.tech
import struct
import build_dumps          # writes vads.txt and a .dmp per private region

def verdict(buf):
    if buf[:2] == b"MZ":
        pe = struct.unpack_from("<I", buf, 0x3C)[0]
        if buf[pe:pe + 4] == b"PE\0\0":
            machine = struct.unpack_from("<H", buf, pe + 4)[0]
            return f"MZ and PE header, machine {machine:#x}: a whole program"
        return "MZ without a PE header: check by hand"
    if buf.startswith(bytes.fromhex("fc4883e4f0")):
        return "opens with cld; and rsp,-16: a common x64 shellcode stub"
    return "no header: JIT output or shellcode, needs context"

for line in open("vads.txt").read().splitlines()[1:]:
    pid, name, start, end, protect, private, path = line.split()
    if "EXECUTE" not in protect or private == "0":
        continue
    buf = open(f"pid.{pid}.{start}.dmp", "rb").read()
    print(f"{name} {pid} {start} {protect}")
    print("  ", verdict(buf))
