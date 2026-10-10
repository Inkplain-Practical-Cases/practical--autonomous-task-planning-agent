# Why: connect a validated plan to an idempotent state identity and audit history.
import hashlib
from app.features.planning.providers.provider_state_store import StateStore

def service_start_workflow(plan: dict, request_key: str, store: StateStore) -> dict:
    if not request_key or len(request_key) > 128:
        raise ValueError("Request key must contain 1–128 characters")
    identity = f'{plan["tenant_id"]}:{request_key}'.encode()
    workflow_id = hashlib.sha256(identity).hexdigest()[:24]
    existing = store.load(workflow_id)
    if existing:
        if existing["goal"] != plan["goal"] or existing["tenant_id"] != plan["tenant_id"]:
            raise ValueError("Idempotency key reused with different goal")
        return existing
    workflow = {"workflow_id": workflow_id, "tenant_id": plan["tenant_id"],
                "goal": plan["goal"], "tasks": [{**task, "state": "pending", "attempts": 0} for task in plan["tasks"]],
                "audit": [{"event": "created", "reason": "validated DAG", "sequence": 1}], "version": 0}
    return store.save(workflow)
