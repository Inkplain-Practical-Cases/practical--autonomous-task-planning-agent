# A typed task contract with explicit dependencies, not a claim of execution.
from pydantic import BaseModel, Field

class TaskContract(BaseModel):
    task_id: str = Field(min_length=1)
    title: str = Field(min_length=1)
    depends_on: list[str] = Field(default_factory=list)
