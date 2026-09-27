# Security Operations & Threat Hunting (SOC) — lesson m05l04 — Malware Triage: Hashes, Strings & Sandboxing
# https://learnsome.tech/courses/secops-course/watch?lesson=m05l04
# © LearnSome.tech
import re
import build_sample

data = open("invoice_0342.exe", "rb").read()
ascii_runs = [m.decode() for m in re.findall(rb"[\x20-\x7e]{6,}", data)]
wide_runs = [m.decode("utf-16-le")
             for m in re.findall(rb"(?:[\x20-\x7e]\x00){6,}", data)]
LOOK_FOR = {
    "url": r"https?://",
    "ipv4": r"^\d{1,3}(\.\d{1,3}){3}$",
    "run key": r"CurrentVersion\\Run",
    "mutex": r"^Global\\",
    "drop path": r"%APPDATA%",
    "user agent": r"^Mozilla/",
}
print(len(ascii_runs), "ASCII and", len(wide_runs), "UTF-16 strings")
for s in ascii_runs + wide_runs:
    for label, pattern in LOOK_FOR.items():
        if re.search(pattern, s):
            print(f"{label:10} {s}")
