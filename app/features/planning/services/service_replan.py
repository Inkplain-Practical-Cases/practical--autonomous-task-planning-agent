# Retry selection is bounded by policy.
def service_replan(workflow,max_retries=1):
    if not 0<=max_retries<=3: raise ValueError("retry limit")
    for task in workflow["tasks"]:
        if task["state"]=="failed" and task["attempts"]<=max_retries:
            task["state"]="pending"
            workflow["audit"].append({"sequence":len(workflow["audit"])+1,"event":"retry_planned","task_id":task["task_id"]})
    return workflow