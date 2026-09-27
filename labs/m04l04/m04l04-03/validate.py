# Security Operations & Threat Hunting (SOC) — lesson m04l04 — Recovery & System Validation Testing
# https://learnsome.tech/courses/secops-course/watch?lesson=m04l04
# © LearnSome.tech
import pathlib, sys

LOGIN_USERS = {"root", "postgres", "ops"}
PORTS = {"22", "5432"}
SSHD_MUST = {"passwordauthentication no", "permitrootlogin no"}

snap = pathlib.Path(sys.argv[1])
found = []
for line in (snap / "passwd").read_text().splitlines():
    user, shell = line.split(":")[0], line.split(":")[-1]
    if not shell.endswith(("nologin", "false")) and user not in LOGIN_USERS:
        found.append(f"login shell for unexpected user {user}")
for line in (snap / "ss.txt").read_text().splitlines()[1:]:
    port = line.split()[3].rsplit(":", 1)[1]
    if port not in PORTS:
        found.append(f"unexpected listener on port {port}")
sshd = set((snap / "sshd-T.txt").read_text().splitlines())
found += [f"sshd -T lacks '{s}'" for s in sorted(SSHD_MUST - sshd)]
for problem in found:
    print(f"  {snap.name}: {problem}")
sys.exit(1 if found else 0)
