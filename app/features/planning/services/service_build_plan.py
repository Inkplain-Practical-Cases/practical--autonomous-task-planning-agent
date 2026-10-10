# Builds a bounded draft from a validated request and an injected task provider.
from collections.abc import Callable
from app.features.planning.models.goal_request import GoalRequest
from app.features.planning.models.task_contract import TaskContract
from app.features.planning.providers.provider_seed_task import provider_seed_task

def service_build_plan(request: GoalRequest, seed: Callable[[str], TaskContract] = provider_seed_task) -> dict:
    # STEP-1 intentionally creates one task; STEP-2 adds graph decomposition.
    task = seed(request.goal)
    if request.max_tasks < 1:
        raise ValueError("Task budget exhausted")
    return {"tenant_id": request.tenant_id, "goal": request.goal, "max_tasks": request.max_tasks,
            "status": "draft", "tasks": [task.model_dump()], "executed": False}
