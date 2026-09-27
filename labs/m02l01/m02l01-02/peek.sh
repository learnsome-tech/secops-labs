# Security Operations & Threat Hunting (SOC) — lesson m02l01 — Event Correlation Rules, Thresholds & Anomaly Pipelines
# https://learnsome.tech/courses/secops-course/watch?lesson=m02l01
# © LearnSome.tech
# Two raw lines, exactly as sshd wrote them
head -n 2 auth.log
# Failed passwords per source address, busiest first
awk '/Failed password/ {n[$(NF-3)]++} END {for (ip in n) print n[ip], ip}' \
  auth.log | sort -rn
# Every successful password logon: time, account, source
awk '/Accepted password/ {print $3, $9, $11}' auth.log
