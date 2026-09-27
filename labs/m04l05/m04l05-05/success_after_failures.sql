# Security Operations & Threat Hunting (SOC) — lesson m04l05 — Post-Incident Review & Root Cause Analysis
# https://learnsome.tech/courses/secops-course/watch?lesson=m04l05
# © LearnSome.tech
-- A password login that succeeds after five or more failures
-- from the same source address in the ten minutes before it.
SELECT ok.ts, ok.host, ok.user, ok.src, COUNT(bad.rowid) AS failures
FROM auth AS ok
JOIN auth AS bad
  ON bad.src = ok.src
 AND bad.result = 'Failed'
 AND bad.ts BETWEEN datetime(ok.ts, '-10 minutes') AND ok.ts
WHERE ok.result = 'Accepted'
GROUP BY ok.rowid
HAVING failures >= 5;
