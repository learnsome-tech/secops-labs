# Security Operations & Threat Hunting (SOC) — lesson m04l04 — Recovery & System Validation Testing
# https://learnsome.tech/courses/secops-course/watch?lesson=m04l04
# © LearnSome.tech
# Reconnection gate: a restored host leaves quarantine only if it passes
for snap in snapshots/*/; do
  name=$(basename "$snap")
  if python3 validate.py "$snap"; then
    echo "$name: pass, move to the production security group"
  else
    echo "$name: fail, stays in quarantine"
  fi
done
