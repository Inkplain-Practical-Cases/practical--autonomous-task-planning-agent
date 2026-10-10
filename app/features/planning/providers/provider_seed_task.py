# Offline deterministic provider: a safe placeholder before STEP-2 decomposition.
from app.features.planning.models.task_contract import TaskContract

def provider_seed_task(goal: str) -> TaskContract:
    # The first step is a review task; no external tool is invoked.
    return TaskContract(task_id="review-goal", title=f"Review: {goal}", depends_on=[])
