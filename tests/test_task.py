from collections.abc import Iterable

from task_platform.task import Task, TaskSource


def test_task_dataclass():
    task = Task(id="test-123", payload={"user": "ivan"})
    assert task.id == "test-123"
    assert task.payload == {"user": "ivan"}


def test_task_source_protocol_runtime_checkable():

    class GoodSource:
        def get_tasks(self) -> Iterable[Task]:
            yield Task("1", {})

    class BadSource:
        pass

    good = GoodSource()
    bad = BadSource()

    assert isinstance(good, TaskSource) is True
    assert isinstance(bad, TaskSource) is False