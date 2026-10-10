# Missing approval must not cause an external side effect.
from app.features.planning.providers.provider_state_store import StateStore
from app.features.planning.services.service_start_workflow import service_start_workflow
from app.features.planning.services.service_execute_workflow import service_execute_workflow
def test_missing_approval_stops(tmp_path):
    store=StateStore(str(tmp_path))
    w=service_start_workflow({"tenant_id":"test","goal":"office","tasks":[{"task_id":"schedule-setup","depends_on":[]}]},"k",store)
    done=service_execute_workflow(w,store)
    assert done["tasks"][0]["state"]=="pending"
    assert done["tasks"][0]["attempts"]==0
