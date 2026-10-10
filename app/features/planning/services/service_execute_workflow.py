# Commit every task transition before scheduling its dependents.
from app.features.planning.services.service_ready_tasks import service_ready_tasks
from app.features.planning.providers.provider_fixture_tools import provider_fixture_tools
def service_execute_workflow(workflow,store,failures=frozenset(),max_actions=12):
    if not 1<=max_actions<=100: raise ValueError("action budget")
    for _ in range(max_actions):
        ready=service_ready_tasks(workflow)
        if not ready: break
        task=ready[0]
        try:
            evidence=provider_fixture_tools(task,failures)
            task["state"]="succeeded"
        except (ValueError,RuntimeError) as exc:
            evidence={"error":str(exc)}
            task["state"]="failed"
        task["attempts"]+=1
        task["evidence"]=evidence
        workflow["audit"].append({"sequence":len(workflow["audit"])+1,"task_id":task["task_id"],"event":task["state"],"evidence":evidence})
        workflow=store.save(workflow,expected_version=workflow["version"])
    return workflow