# Security Operations & Threat Hunting (SOC) — lesson m03l05 — Detecting Persistence: Tasks, Registry & Services
# https://learnsome.tech/courses/secops-course/watch?lesson=m03l05
# © LearnSome.tech
import json

GITOPS = "system:serviceaccount:argocd:argocd-application-controller"
WRITES = {"create", "update", "patch"}

def detail(res, obj):
    if res == "pods":
        return "hostPath " + " ".join(v["hostPath"]["path"]
            for v in obj["spec"].get("volumes", []) if "hostPath" in v)
    if res == "clusterrolebindings":
        return "grants " + obj["roleRef"]["name"]
    return obj.get("type", "").split("/")[-1] or obj["spec"]["schedule"]

for line in open("audit.log"):
    ev = json.loads(line)
    ref, who = ev["objectRef"], ev["user"]["username"]
    if ev["verb"] not in WRITES or who == GITOPS:
        continue
    where = f"{ref.get('namespace', 'cluster')}/{ref['name']}"
    print(ev["requestReceivedTimestamp"][11:19], who.split(":")[-1],
          ref["resource"], where, detail(ref["resource"], ev["requestObject"]))
