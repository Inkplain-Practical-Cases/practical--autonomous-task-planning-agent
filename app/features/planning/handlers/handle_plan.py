# The handler delegates to the pure planning service; it has no side effects.
from app.features.planning.models.goal_request import GoalRequest
from app.features.planning.services.service_build_plan import service_build_plan

def handle_plan(request: GoalRequest) -> dict:
    # Validated request crosses into the domain through one explicit call.
    return service_build_plan(request)
