import hashlib, struct
import build_sample
pe = open("invoice_0342.exe", "rb").read()
u32 = lambda at: struct.unpack_from("<I", pe, at)[0]
text = lambda at: pe[at:pe.index(b"\0", at)].decode()
nt = u32(0x3C)                              # e_lfanew points at PE\0\0
count, opt_size = struct.unpack_from("<H12xH", pe, nt + 6)
table = [struct.unpack_from("<8xII4xI", pe, nt + 24 + opt_size + 40 * i)
         for i in range(count)]             # (size, rva, file offset)
off = lambda rva: next(rva - va + raw for size, va, raw in table
                       if va <= rva < va + size)    # RVA to file offset
imports, parts, d = {}, [], off(u32(nt + 24 + 120))  # directory 1: imports
while u32(d):                               # an all-zero entry ends the list
    dll, entry = text(off(u32(d + 12))), off(u32(d))
    while thunk := struct.unpack_from("<Q", pe, entry)[0]:
        imports.setdefault(dll, []).append(text(off(thunk) + 2))
        entry += 8
    d += 20
for dll, funcs in imports.items():
    print(dll, " ".join(funcs))
    parts += [f"{dll.lower().removesuffix('.dll')}.{f.lower()}" for f in funcs]
print("imphash", hashlib.md5(",".join(parts).encode()).hexdigest())
