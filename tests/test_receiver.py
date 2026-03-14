import pytest

from src.receiver import TaskReceiver
from src.sources.generator_source import GeneratorTaskSource
from src.sources.API_source import APITaskSource
from src.task import Task


class InvalidSource:
    pass


def test_receiver_add_invalid_source_raises():
    receiver = TaskReceiver()
    invalid = InvalidSource()

    with pytest.raises(TypeError) as exc_info:
        receiver.add_source(invalid)

    assert "is not a duck!" in str(exc_info.value)


def test_receiver_stream_tasks():
    receiver = TaskReceiver()
    receiver.add_source(GeneratorTaskSource(count=2))
    receiver.add_source(APITaskSource())

    tasks = list(receiver.stream_tasks())

    assert len(tasks) == 5
    assert all(isinstance(t, Task) for t in tasks)


def test_receiver_collect_tasks():
    receiver = TaskReceiver()
    receiver.add_source(GeneratorTaskSource(count=1))

    tasks = receiver.collect_tasks()

    assert isinstance(tasks, list)
    assert len(tasks) == 1


def test_receiver_lazy_streaming():
    receiver = TaskReceiver()
    receiver.add_source(GeneratorTaskSource(count=1000))

    tasks = []
    for task in receiver.stream_tasks():
        tasks.append(task)
        if len(tasks) == 3:
            break

    assert len(tasks) == 3