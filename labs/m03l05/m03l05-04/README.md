# m03l05-04 · Services and Run keys against a baseline

**Lesson:** [Detecting Persistence: Tasks, Registry & Services](https://learnsome.tech/learn/secops-course/m03l05) (lesson 3.5, module 3: Threat Intelligence & MITRE ATT&CK Mapping) · Pro  
**Check:** Graded

## Goal

You can find scheduled task, service and Run key persistence in Windows event XML, diff autostarts against a baseline, and spot Kubernetes persistence in API server audit logs.

In the lesson: One task is easy. A real estate has thousands of autostart entries, so the useful question becomes: what is new? This script reads exported events of two more kinds, service installs and Sysmon registry writes. For each event I D, a small table says which field names the thing and which names what runs. Then comes a short list of risky markers: user writable folders, script interpreters, and system binaries that attackers use to launch code. Each command is compared first with a known good baseline taken from your standard build, and only then with the markers. Two entries match the baseline: the backup agent and the Windows security tray icon. The other two are new and noisy: a service that runs cmd and PowerShell from ProgramData, and a Run key pointing into a Temp folder.

## Files

- [`starter/autoruns_diff.py`](starter/autoruns_diff.py): the listing from the lesson
- [`starter/baseline.txt`](starter/baseline.txt)
- [`starter/events.xml`](starter/events.xml)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l05/m03l05-04/starter`
2. Read `autoruns_diff.py` the way the lesson builds it:
   - Lines 1–5: which field names the thing and which names what runs
   - Lines 6–8: a short list of risky markers
   - Lines 9–19: known good baseline
3. Run it: `python3 autoruns_diff.py`.
4. Check it from the repository root: `./check m03l05-04`.

## Expected output

```text
7045 Contoso Backup Agent  in baseline
13   SecurityHealth        in baseline
13   OneDriveUpdate        new: \users\, \temp\
7045 WinDefendUpdate       new: \programdata\, powershell, cmd.exe /c
```

## How to check

`./check m03l05-04` copies `starter/` into a scratch directory and runs `python3 autoruns_diff.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
