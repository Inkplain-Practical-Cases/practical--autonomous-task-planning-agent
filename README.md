# Autonomous Task Planning Agent

Six cumulative, independently runnable Python/FastAPI learning steps. This branch is STEP-1: typed goal intake and bounded draft task contract; it **does not** execute tools or create a dependency DAG yet.

## Run

`python -m pip install -r requirements.txt`

`python -m pytest -q`

`uvicorn app.main:app --reload`

Synthetic fixture only. No secrets or real external services.
