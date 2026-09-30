import struct
import build_ntfs               # writes MFT.bin, exported from an image
def records(path):
    data = open(path, "rb").read()
    for off in range(0, len(data), 1024):
        rec = bytearray(data[off:off + 1024])
        usa, count = struct.unpack_from("<HH", rec, 4)
        for i in range(1, count):        # put each sector's last two bytes back
            end = i * 512
            assert rec[end - 2:end] == rec[usa:usa + 2], "torn write"
            rec[end - 2:end] = rec[usa + 2 * i:usa + 2 * i + 2]
        yield struct.unpack_from("<I", rec, 44)[0], rec
def attributes(rec):
    at = struct.unpack_from("<H", rec, 20)[0]
    while (kind := struct.unpack_from("<I", rec, at)[0]) != 0xFFFFFFFF:
        yield kind, at + struct.unpack_from("<H", rec, at + 20)[0]
        at += struct.unpack_from("<I", rec, at + 4)[0]
if __name__ == "__main__":
    for number, rec in records("MFT.bin"):
        state = "in use" if rec[22] & 1 else "deleted"
        kinds = " ".join(hex(k) for k, _ in attributes(rec))
        print(f"record {number} {rec[:4].decode()} {state:7} attrs {kinds}")
