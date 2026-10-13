# STEP-6: Verify termination and failure recovery

## What changed
- service_completion_report: Terminal status reflects persisted evidence, not an imagined plan.
- service_failure_fixture: Reproducible failure injection.

## Run and verify
```bash
python -m pip install -r requirements.txt
python -m pytest -q
uvicorn app.main:app --reload
```

Follow the component dependency and inspect evidence in the versioned state store.

## Database (Entity) Relations
This STEP persists one `workflows` JSON document per workflow through `StateStore` (`app/features/planning/providers/provider_state_store.py`). The `tasks`, `audit` and, from STEP-5, `approvals` fields are embedded inside the workflow document, so there are no independent foreign-key relations. The file `STEP-6.erd` is generated from source and visualized in the `STEP-6-ERD` Simulator tab.
