# HTTP door: FastAPI validates GoalRequest and forwards it to one handler.
from fastapi import APIRouter
from app.features.planning.models.goal_request import GoalRequest
from app.features.planning.handlers.handle_plan import handle_plan

router = APIRouter()

@router.post("/plans")
def receive_goal(request: GoalRequest) -> dict:
    # Do not put task planning, authorization or provider calls in the door.
    return handle_plan(request)
