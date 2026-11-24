"""Local fail-closed readiness check; not a clinical or legal determination."""
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
data = json.loads((root / "requirements.json").read_text())
blocked = []
for req in data["requirements"]:
    # A placeholder file alone never satisfies a gate.
    ready = (req["status"] == "verified" and (root / req["artifact"]).is_file()
             and bool(req["evidence"]) and bool(req["reviewer"]))
    print(f'{req["id"]}: {"VERIFIED" if ready else "BLOCKED"} — {req["requirement"]}')
    if req["mandatory"] and not ready:
        blocked.append(req["id"])
print("NOT READY: " + ", ".join(blocked) if blocked else "Recorded gates pass; human release still required.")
raise SystemExit(1 if blocked else 0)
