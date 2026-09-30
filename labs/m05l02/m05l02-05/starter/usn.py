import struct
from datetime import datetime, timedelta
import build_ntfs                    # writes J.bin, the $UsnJrnl:$J stream

REASONS = {0x100: "FILE_CREATE", 0x2: "DATA_EXTEND", 0x200: "FILE_DELETE",
           0x1000: "RENAME_OLD_NAME", 0x2000: "RENAME_NEW_NAME",
           0x8000: "BASIC_INFO_CHANGE", 0x80000000: "CLOSE"}
data, at = open("J.bin", "rb").read(), 0
while at < len(data):
    size = struct.unpack_from("<I", data, at)[0]
    if size == 0:                    # $J is sparse: skip the zero padding
        at += 8
        continue
    ref, _, usn, stamp, reason = struct.unpack_from("<QQqQI", data, at + 8)
    length, offset = struct.unpack_from("<HH", data, at + 56)
    name = data[at + offset:at + offset + length].decode("utf-16-le")
    when = datetime(1601, 1, 1) + timedelta(microseconds=stamp // 10)
    what = " ".join(v for k, v in REASONS.items() if reason & k)
    print(f"{when:%H:%M:%S.%f} mft {ref & 0xFFFFFFFFFFFF} {name:10} {what}")
    at += size
