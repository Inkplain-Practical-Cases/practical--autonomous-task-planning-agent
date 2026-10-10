# STEP-2 inherits STEP-1 input checks but now returns a three-task draft graph.
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_valid_goal_returns_bounded_draft():
    response = client.post("/api/plans", json={"tenant_id": "fictional-team", "goal": "Prepare office opening"})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "draft" and data["executed"] is False
    assert len(data["tasks"]) == 3
    assert data["tasks"][0]["depends_on"] == []

def test_invalid_goal_is_rejected():
    assert client.post("/api/plans", json={"tenant_id": "fictional-team", "goal": "x"}).status_code == 422

def test_bad_tenant_id_is_rejected():
    assert client.post("/api/plans", json={"tenant_id": "../other", "goal": "Prepare office opening"}).status_code == 422

def test_unbounded_task_request_is_rejected():
    assert client.post("/api/plans", json={"tenant_id": "fictional-team", "goal": "Prepare office opening", "max_tasks": 100}).status_code == 422
