# Validate dependency graphs before any execution is considered.
from app.features.planning.models.task_contract import TaskContract

def service_validate_dag(tasks: list[TaskContract], max_tasks: int) -> None:
    # Reject empty, oversized and duplicate-ID plans.
    if not tasks or len(tasks) > max_tasks: raise ValueError('Task count exceeds budget')
    by_id = {task.task_id: task for task in tasks}
    if len(by_id) != len(tasks): raise ValueError('Duplicate task identifier')
    for task in tasks:
        if task.task_id in task.depends_on or any(dep not in by_id for dep in task.depends_on):
            raise ValueError('Unknown or self dependency')
    visiting, visited = set(), set()
    def walk(task_id: str) -> None:
        if task_id in visiting: raise ValueError('Cyclic dependency')
        if task_id in visited: return
        visiting.add(task_id)
        for dep in by_id[task_id].depends_on: walk(dep)
        visiting.remove(task_id)
        visited.add(task_id)
    for task_id in by_id: walk(task_id)
