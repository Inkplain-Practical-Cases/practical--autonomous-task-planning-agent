# A human must approve the exact pending privileged action.
def service_approval_gate(workflow,store,task_id,reviewer_id,approved):
    if not reviewer_id or not isinstance(approved,bool): raise ValueError("explicit approval required")
    task=next((x for x in workflow["tasks"] if x["task_id"]==task_id),None)
    if task is None or task["state"]!="pending": raise ValueError("invalid approval target")
    workflow.setdefault("approvals",{})[task_id]={"reviewer":reviewer_id,"approved":approved}
    if not approved: task["state"]="blocked"
    workflow["audit"].append({"sequence":len(workflow["audit"])+1,"task_id":task_id,"event":"approved" if approved else "denied"})
    return store.save(workflow,expected_version=workflow["version"])