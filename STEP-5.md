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
