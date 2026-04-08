import pytest
from src.task import Task
from src.exceptions import InvalidStatusError

def test_task_initialization():
    task = Task(task_id="T1", payload="data", priority=3, status="ready")
    assert task.id == "T1"
    assert task.priority == 3
    assert task.status == "ready"

def test_task_id_is_readonly():
    task = Task("T1", {}, 1)
    with pytest.raises(AttributeError):
        task.id = "new-id"

def test_is_high_priority():
    low_task = Task("T1", {}, 1)
    high_task = Task("T2", {}, 5)
    assert low_task.is_high_priority is False
    assert high_task.is_high_priority is True

def test_invalid_status_raises_error():
    task = Task("T1", {}, 1)
    with pytest.raises(InvalidStatusError):
        task.status = "invalid_status"

def test_valid_status_change():
    task = Task("T1", {}, 1, status="in_porgress")
    task.status = "sent"
    assert task.status == "sent"