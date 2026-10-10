# Handler maps domain validation failures to explicit HTTP 422 responses.
from fastapi import HTTPException
from app.features.planning.models.goal_request import GoalRequest
from app.features.planning.services.service_build_plan import service_build_plan

def handle_plan(request: GoalRequest) -> dict:
    try:
        return service_build_plan(request)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
