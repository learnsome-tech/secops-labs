# Two raw lines, exactly as sshd wrote them
head -n 2 auth.log
# Failed passwords per source address, busiest first
awk '/Failed password/ {n[$(NF-3)]++} END {for (ip in n) print n[ip], ip}' \
  auth.log | sort -rn
# Every successful password logon: time, account, source
awk '/Accepted password/ {print $3, $9, $11}' auth.log
