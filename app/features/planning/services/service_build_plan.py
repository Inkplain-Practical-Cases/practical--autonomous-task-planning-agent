# Build a draft DAG through injected decomposition and explicit validation.
from collections.abc import Callable
from app.features.planning.models.goal_request import GoalRequest
from app.features.planning.models.task_contract import TaskContract
from app.features.planning.providers.provider_decompose_tasks import provider_decompose_tasks
from app.features.planning.services.service_validate_dag import service_validate_dag

def service_build_plan(request: GoalRequest, decompose: Callable[[str], list[TaskContract]] = provider_decompose_tasks) -> dict:
    # Provider output is untrusted until graph and budget checks succeed.
    tasks = decompose(request.goal)
    service_validate_dag(tasks, request.max_tasks)
    return {'tenant_id': request.tenant_id, 'goal': request.goal, 'max_tasks': request.max_tasks,
            'status': 'draft', 'tasks': [task.model_dump() for task in tasks], 'executed': False}
