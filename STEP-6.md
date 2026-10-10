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
