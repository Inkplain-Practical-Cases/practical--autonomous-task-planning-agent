# The application door wires the planning router; business logic lives in the feature.
from fastapi import FastAPI
from app.features.planning.router import router

app = FastAPI(title="Autonomous Task Planning Agent — STEP-1")
app.include_router(router, prefix="/api")
