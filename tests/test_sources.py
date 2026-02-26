from task_platform.sources.file_source import FileTaskSource
from task_platform.sources.generator_source import GeneratorTaskSource
from task_platform.sources.API_source import APITaskSource
from task_platform.task import Task, TaskSource


def test_file_source(temp_task_file):
    source = FileTaskSource(temp_task_file)
    tasks = list(source.get_tasks())

    assert len(tasks) == 3
    assert all(isinstance(t, Task) for t in tasks)
    assert tasks[0].id == "file_001"


def test_generator_source():
    source = GeneratorTaskSource(count=5)
    tasks = list(source.get_tasks())

    assert len(tasks) == 5
    assert tasks[0].id == "gen_0000"
    assert isinstance(tasks[0], Task)


def test_API_source():
    source = APITaskSource()
    tasks = list(source.get_tasks())

    assert len(tasks) == 3
    assert tasks[0].id == "api001"
    assert isinstance(tasks[0], Task)


def test_all_sources_implement_protocol():
    sources = [
        FileTaskSource("tasks.json"),
        GeneratorTaskSource(),
        APITaskSource(),
    ]
    for source in sources:
        assert isinstance(source, TaskSource)