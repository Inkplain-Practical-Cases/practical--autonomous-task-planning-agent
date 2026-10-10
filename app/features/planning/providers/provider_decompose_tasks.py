# Deterministic offline task decomposition; no real actions or model calls.
from app.features.planning.models.task_contract import TaskContract

def provider_decompose_tasks(goal: str) -> list[TaskContract]:
    # Stable IDs and explicit dependencies make this plan testable.
    return [TaskContract(task_id='review-goal', title=f'Review: {goal}'),
            TaskContract(task_id='verify-budget', title='Verify approved budget', depends_on=['review-goal']),
            TaskContract(task_id='schedule-setup', title='Schedule setup', depends_on=['verify-budget'])]
