from typing import Iterable, Generator
from .task import Task

class TaskQueue:
    def __init__(self):
        self._tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        self._tasks.append(task)

    def add_tasks(self, tasks: Iterable[Task]) -> None:
        for task in tasks:
            self._tasks.append(task)

    def __iter__(self):
        return iter(self._tasks)

    def filter_by_status(self, status: str) -> Generator[Task, None, None]:
        for task in self:
            if task.status == status:
                yield task

    def filter_by_priority(self, min_priority: int) -> Generator[Task, None, None]:
        for task in self:
            if task.priority >= min_priority:
                yield task
