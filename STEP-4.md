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
