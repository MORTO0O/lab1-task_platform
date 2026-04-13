import pytest
from src.task import Task
from src.exceptions import InvalidPriorityError

def test_priority_descriptor_valid_range():
    task = Task(task_id="T1", description="Тест", payload={}, priority=1)
    for p in range(1, 6):
        task.priority = p
        assert task.priority == p

def test_priority_out_of_range_raises():
    task = Task(task_id="T1", description="Тест", payload={}, priority=1)
    with pytest.raises(InvalidPriorityError):
        task.priority = 10
    with pytest.raises(InvalidPriorityError):
        task.priority = 0

def test_priority_invalid_type_raises():
    task = Task(task_id="T1", description="Тест", payload={}, priority=1)
    with pytest.raises(InvalidPriorityError):
        task.priority = "high"

def test_access_log_descriptor(capsys):
    task = Task(task_id="T1", description="Тест", payload={}, priority=1)
    _ = task.access_log
    captured = capsys.readouterr()
    assert "Чтение данных задачи" in captured.out