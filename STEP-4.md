# STEP-4: Execute ready tasks with offline tools

## What changed
- provider_fixture_tools: Deterministic offline adapter, never external side effects.
- service_execute_workflow: Commit every task transition before scheduling its dependents.

## Run and verify
```bash
python -m pip install -r requirements.txt
python -m pytest -q
uvicorn app.main:app --reload
```

Follow the component dependency and inspect evidence in the versioned state store.

## Database (Entity) Relations
This STEP persists one `workflows` JSON document per workflow through `StateStore` (`app/features/planning/providers/provider_state_store.py`). The `tasks`, `audit` and, from STEP-5, `approvals` fields are embedded inside the workflow document, so there are no independent foreign-key relations. The file `STEP-4.erd` is generated from source and visualized in the `STEP-4-ERD` Simulator tab.
