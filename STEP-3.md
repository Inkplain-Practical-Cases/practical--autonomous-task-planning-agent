# STEP-3 — Persist workflow state and audit events

This cumulative branch adds service_start_workflow, provider_state_store. Each component has one responsibility and a test in tests/.

## Run

```bash
python -m pip install -r requirements.txt
python -m pytest -q
uvicorn app.main:app --reload
```

## Verify
Inspect the STEP-3.crd dependency map, execute the tests, and compare recorded status with actual evidence. The project uses deterministic local fixtures; no real business system is called.
