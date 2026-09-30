# m04l03-05 · Sweep every host before removing anything

**Lesson:** [Containment & Eradication: Host, Net & Identity](https://learnsome.tech/learn/secops-course/m04l03) (lesson 4.3, module 4: Incident Response Lifecycle & Playbooks) · Pro  
**Check:** Graded

## Goal

You can choose a containment strategy, isolate a host without leaving live attacker sessions open, show why revoking sessions and not a password reset stops a stolen token, and sweep every in-scope host before a single coordinated eradication.

In the lesson: Eradication starts with knowing every place the attacker left something, before you touch any of them. This sweep runs over artefacts collected from the three hosts in scope. The indicators come from triage on the bastion: the fingerprint of the attacker's S S H key, and the path of a dropped binary. For every authorized keys file, ssh keygen computes each key's fingerprint and the script keeps the lines that match. Then grep searches everything collected for the dropper path. The script sorts the findings and names the hosts. Read the results. The same key sits under three accounts on three hosts, and on the database it carries the comment backup at db one, dressed up as a local key. Matching on the comment would have missed it; the fingerprint cannot be disguised. The dropper starts from a systemd unit on app two and a cron job on the database.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/hosts/app02/etc/systemd/system/dbus-helper.service`](starter/hosts/app02/etc/systemd/system/dbus-helper.service)
- [`starter/hosts/app02/home/deploy/.ssh/authorized_keys`](starter/hosts/app02/home/deploy/.ssh/authorized_keys)
- [`starter/hosts/bastion01/home/deploy/.ssh/authorized_keys`](starter/hosts/bastion01/home/deploy/.ssh/authorized_keys)
- [`starter/hosts/bastion01/home/ops/.ssh/authorized_keys`](starter/hosts/bastion01/home/ops/.ssh/authorized_keys)
- [`starter/hosts/db01/home/backup/.ssh/authorized_keys`](starter/hosts/db01/home/backup/.ssh/authorized_keys)
- [`starter/hosts/db01/var/spool/cron/crontabs/backup`](starter/hosts/db01/var/spool/cron/crontabs/backup)
- [`starter/sweep.sh`](starter/sweep.sh): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-05/starter`
2. Read `sweep.sh` the way the lesson builds it:
   - Lines 1–3: The indicators come from triage
   - Lines 4–9: For every authorized keys file
   - Lines 10–11: grep searches
   - Lines 12–14: sorts the findings
3. Run it: `bash sweep.sh`.
4. Check it from the repository root: `./check m04l03-05`.

## Expected output

```text
app02/etc/systemd/system/dbus-helper.service runs dropper
app02/home/deploy/.ssh/authorized_keys key deploy@build-02
bastion01/home/deploy/.ssh/authorized_keys key deploy@build-02
db01/home/backup/.ssh/authorized_keys key backup@db01
db01/var/spool/cron/crontabs/backup runs dropper
clean together: app02 bastion01 db01
```

## How to check

`./check m04l03-05` copies `starter/` into a scratch directory and runs `bash sweep.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/secops-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
