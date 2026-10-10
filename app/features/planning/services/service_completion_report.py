# Terminal status reflects persisted evidence, not an imagined plan.
def service_completion_report(workflow):
    states={x["task_id"]:x["state"] for x in workflow["tasks"]}
    status="completed" if all(x=="succeeded" for x in states.values()) else ("failed_or_blocked" if any(x in ("failed","blocked") for x in states.values()) else "incomplete")
    return {"workflow_id":workflow["workflow_id"],"status":status,"states":states,"version":workflow["version"],"audit_events":len(workflow["audit"])}