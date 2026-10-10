# STEP-2 — Task decomposition and dependency graph

This cumulative branch adds a deterministic three-task decomposition and a graph validator. The planner rejects cycles, missing dependencies, duplicate task identifiers and plans exceeding max_tasks. No business actions execute.

Install: `python -m pip install -r requirements.txt`. Test: `python -m pytest -q`. Run: `uvicorn app.main:app --reload`.

POST `/api/plans` with `{"tenant_id":"fictional-team","goal":"Prepare office opening"}`. Expected order: review-goal, verify-budget, schedule-setup. Next: persisted execution state.
