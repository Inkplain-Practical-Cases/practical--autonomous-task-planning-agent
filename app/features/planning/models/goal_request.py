# Validates the caller's goal before the request reaches the planning handler.
from pydantic import BaseModel, Field

class GoalRequest(BaseModel):
    tenant_id: str = Field(min_length=1, max_length=64, pattern=r"^[a-zA-Z0-9_-]+$")
    goal: str = Field(min_length=5, max_length=500)
    max_tasks: int = Field(default=6, ge=1, le=12)
