# Deterministic offline adapter, never external side effects.
ALLOWED={"review-goal","verify-budget","schedule-setup"}
def provider_fixture_tools(task:dict,failures=frozenset()):
    name=task["task_id"]
    if name not in ALLOWED: raise ValueError("Tool not allowlisted")
    if name in failures: raise RuntimeError("Injected fixture failure")
    return {"receipt":f"fixture:{name}:ok"}