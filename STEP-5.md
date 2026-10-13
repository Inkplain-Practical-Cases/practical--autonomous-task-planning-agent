# STEP-5: Gate privileged actions and bound retries

## What changed
- service_approval_gate: A human must approve the exact pending privileged action.
- service_replan: Retry selection is bounded by policy.

## Run and verify
```bash
python -m pip install -r requirements.txt
python -m pytest -q
uvicorn app.main:app --reload
```

Follow the component dependency and inspect evidence in the versioned state store.

## Database (Entity) Relations
This STEP persists one `workflows` JSON document per workflow through `StateStore` (`app/features/planning/providers/provider_state_store.py`). The `tasks`, `audit` and, from STEP-5, `approvals` fields are embedded inside the workflow document, so there are no independent foreign-key relations. The file `STEP-5.erd` is generated from source and visualized in the `STEP-5-ERD` Simulator tab.
