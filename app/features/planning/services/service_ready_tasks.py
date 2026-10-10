# Select only pending tasks whose dependencies succeeded.
def service_ready_tasks(workflow: dict) -> list[dict]:
    states = {task['task_id']: task['state'] for task in workflow['tasks']}
    return [task for task in workflow['tasks'] if task['state'] == 'pending' and all(states.get(dep) == 'succeeded' for dep in task['depends_on'])]
