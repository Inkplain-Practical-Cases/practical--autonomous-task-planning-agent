from app.features.planning.providers.provider_state_store import StateStore
from app.features.planning.services.service_start_workflow import service_start_workflow
from app.features.planning.services.service_execute_workflow import service_execute_workflow
def test_failed_dependency(tmp_path):
    store=StateStore(str(tmp_path))
    plan={"tenant_id":"demo","goal":"open office","tasks":[{"task_id":"review-goal","depends_on":[]},{"task_id":"verify-budget","depends_on":["review-goal"]},{"task_id":"schedule-setup","depends_on":["verify-budget"]}]}
    state=service_start_workflow(plan,"x",store)
    state=service_execute_workflow(state,store,frozenset({"verify-budget"}))
    assert [x["state"] for x in state["tasks"]]==["succeeded","failed","pending"]