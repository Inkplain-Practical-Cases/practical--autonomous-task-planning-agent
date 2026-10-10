# STEP-2 tests the new decomposition and dependency validator offline.
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.features.planning.models.task_contract import TaskContract
from app.features.planning.services.service_validate_dag import service_validate_dag

client = TestClient(app)

def test_dependency_chain():
    response = client.post('/api/plans', json={'tenant_id':'fictional-team','goal':'Prepare office opening'})
    assert response.status_code == 200
    tasks = response.json()['tasks']
    assert [task['task_id'] for task in tasks] == ['review-goal','verify-budget','schedule-setup']
    assert tasks[2]['depends_on'] == ['verify-budget']

def test_task_budget_is_enforced():
    response = client.post('/api/plans', json={'tenant_id':'fictional-team','goal':'Prepare office opening','max_tasks':2})
    assert response.status_code == 422

def test_cycles_are_rejected():
    tasks = [TaskContract(task_id='a',title='A',depends_on=['b']),TaskContract(task_id='b',title='B',depends_on=['a'])]
    with pytest.raises(ValueError, match='Cyclic'): service_validate_dag(tasks, 5)

def test_unknown_dependencies_are_rejected():
    with pytest.raises(ValueError, match='Unknown'): service_validate_dag([TaskContract(task_id='a',title='A',depends_on=['missing'])],5)
