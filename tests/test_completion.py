from app.features.planning.services.service_completion_report import service_completion_report
def test_incomplete():
    result=service_completion_report({"workflow_id":"1","version":1,"audit":[],"tasks":[{"task_id":"a","state":"pending"}]})
    assert result["status"]=="incomplete"