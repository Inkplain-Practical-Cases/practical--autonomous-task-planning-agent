# STEP-1 — Validated goal intake and bounded task contract

A fictional operations requester submits a goal and tenant identifier. FastAPI/Pydantic reject invalid identifiers, short goals and excessive task budgets. The handler delegates to a pure service, which uses an injected deterministic provider to return one draft task. No task executes at this stage.

Run: `python -m pip install -r requirements.txt && python -m pytest -q`.

Start API: `uvicorn app.main:app --reload`. POST `/api/plans` with `{"tenant_id":"fictional-team","goal":"Prepare office opening"}`.

Expected: `status=draft`, one task, `executed=false`. Negative tests cover malformed tenant, short goal and excessive budget. STEP-2 will replace the single seed task with validated dependency-aware decomposition.
