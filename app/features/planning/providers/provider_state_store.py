# Why: durable state between calls; without it workflows forget completed actions.
# Local JSON store is a teaching fixture, not a multi-process transactional database.
import json
import os
from pathlib import Path

class VersionConflict(ValueError):
    """The caller attempted a transition from an outdated snapshot."""

class StateStore:
    def __init__(self, root: str):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def load(self, workflow_id: str) -> dict | None:
        path = self.root / f"{workflow_id}.json"
        return json.loads(path.read_text()) if path.exists() else None

    def save(self, workflow: dict, expected_version: int | None = None) -> dict:
        workflow_id = workflow["workflow_id"]
        if not workflow_id.isalnum():
            raise ValueError("Workflow ID must be alphanumeric")
        previous = self.load(workflow_id)
        actual = previous["version"] if previous else None
        if actual != expected_version:
            raise VersionConflict("stale workflow version")
        updated = json.loads(json.dumps(workflow))
        updated["version"] = (actual or 0) + 1
        path = self.root / f"{workflow_id}.json"
        temporary = self.root / f"{workflow_id}.json.tmp"
        temporary.write_text(json.dumps(updated, indent=2, sort_keys=True))
        os.replace(temporary, path)
        return updated
