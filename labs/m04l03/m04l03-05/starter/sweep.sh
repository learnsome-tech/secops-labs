# Indicators from bastion triage: the attacker's key and dropped binary
key="SHA256:tyD5HoDUdthX4SMXrVqLI+5MBfE0iPp6aCl3OUKjNU8"
dropper="/var/tmp/.cache/upd"

for f in hosts/*/home/*/.ssh/authorized_keys; do
  ssh-keygen -lf "$f" | grep -F "$key" | while read -r bits fp comment kind; do
    echo "${f#hosts/} key $comment"
  done
done > findings.txt
grep -rlF "$dropper" hosts | sed "s|^hosts/||; s|$| runs dropper|" \
  >> findings.txt

sort findings.txt
echo "clean together: $(cut -d/ -f1 findings.txt | sort -u | xargs)"
