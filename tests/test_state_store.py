# Educational checks for persistence, replay, stale writes and idempotency.
import pytest
from app.features.planning.providers.provider_state_store import StateStore, VersionConflict
from app.features.planning.services.service_start_workflow import service_start_workflow

def test_versioned_store_and_replay(tmp_path):
    store = StateStore(str(tmp_path))
    plan = {"tenant_id": "sample", "goal": "open office", "tasks": [{"task_id":"a","depends_on":[]}]}
    first = service_start_workflow(plan, "request-1", store)
    assert first["version"] == 1
    assert service_start_workflow(plan, "request-1", store) == first
    with pytest.raises(VersionConflict):
        store.save(first, expected_version=0)
    second = store.save(first, expected_version=1)
    assert second["version"] == 2
