from app.features.planning.providers.provider_state_store import StateStore
from app.features.planning.services.service_start_workflow import service_start_workflow
from app.features.planning.services.service_approval_gate import service_approval_gate
def test_denial(tmp_path):
    s=StateStore(str(tmp_path))
    w=service_start_workflow({"tenant_id":"demo","goal":"x","tasks":[{"task_id":"schedule-setup","depends_on":[]}]},"k",s)
    w=service_approval_gate(w,s,"schedule-setup","human",False)
    assert w["tasks"][0]["state"]=="blocked"