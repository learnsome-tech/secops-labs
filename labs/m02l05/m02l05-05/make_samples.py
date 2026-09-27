# Security Operations & Threat Hunting (SOC) — lesson m02l05 — YARA Rule Authoring & File Signature Matching
# https://learnsome.tech/courses/secops-course/watch?lesson=m02l05
# © LearnSome.tech
import hashlib

def pe_like(body):          # an MZ header, zero padding, then the body
    return b"MZ" + bytes(62) + body

def xor_stub(key):          # mov al,[esi+ecx]; xor al,key; mov [esi+ecx],al
    return bytes([0x8A, 0x04, 0x0E, 0x34, key, 0x88, 0x04, 0x0E])

def build():
    mutex = "Global\\Xq7-updater".encode("utf-16-le")
    gate = b"POST /gate.php HTTP/1.1\r\n"
    ps = "PowerShell -NoP -W Hidden".encode("utf-16-le")
    return {
        "invoice_a.exe": pe_like(xor_stub(0x5A) + mutex + gate + ps),
        "invoice_b.exe": pe_like(xor_stub(0x3C) + bytes(40) + mutex + gate),
        "updater.exe": pe_like(xor_stub(0x21) + b"Example Updater 4.2\0"),
        "gate_help.txt": b"Support note: the form posts to /gate.php\n",
    }
if __name__ == "__main__":
    for name, data in build().items():
        digest = hashlib.sha256(data).hexdigest()[:16]
        print(f"{name:14} {len(data):4} bytes  sha256 {digest}...")
