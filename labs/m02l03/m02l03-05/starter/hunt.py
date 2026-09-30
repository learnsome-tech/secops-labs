import json
from sigma_match import matches

# rule.yml's detection block as Python: the standard library has no YAML
DETECTION = {
    "selection_img": {"Image|endswith": ["\\powershell.exe", "\\pwsh.exe"]},
    "selection_cli": {"CommandLine|contains": [" -enc ", " -encodedcommand "]},
    "filter_sccm": {"ParentImage|endswith": "\\CcmExec.exe"},
}

if __name__ == "__main__":
    with open("process_creation.jsonl") as f:
        for e in map(json.loads, f):
            verdict = "alert" if matches(e, DETECTION) else "-"
            parent = e["ParentImage"].rsplit("\\", 1)[-1]
            print(f"{verdict:5} {parent:12} {e['CommandLine']}")
