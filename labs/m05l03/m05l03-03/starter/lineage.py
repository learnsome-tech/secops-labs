PARENT = {"smss.exe": "System", "services.exe": "wininit.exe",
          "lsass.exe": "wininit.exe", "svchost.exe": "services.exe"}
OFFICE = {"WINWORD.EXE", "EXCEL.EXE", "POWERPNT.EXE", "OUTLOOK.EXE"}
SINGLE = {"lsass.exe", "services.exe", "wininit.exe"}

procs = {}
for line in open("pstree.txt").read().splitlines()[1:]:
    pid, ppid, name, day, time = line.lstrip("* ").split()
    procs[pid] = (ppid, name, time)
seen = {}
for pid, (ppid, name, time) in procs.items():
    parent = procs[ppid][1] if ppid in procs else f"pid {ppid} (exited)"
    if name in PARENT and parent != PARENT[name]:
        print(f"{time} {name} {pid}: parent {parent}, expected {PARENT[name]}")
    if parent in OFFICE:
        print(f"{time} {name} {pid}: child of {parent}")
    if name in SINGLE and name in seen:
        print(f"{time} {name} {pid}: second copy, first is pid {seen[name]}")
    seen.setdefault(name, pid)
