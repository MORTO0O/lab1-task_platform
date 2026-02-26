from collections.abc import Iterable
from typing import List

from .task import Task, TaskSource

class TaskReceiver:
    def __init__(self) -> None:
        self._sources: List[TaskSource] = []

    def add_source(self, source: TaskSource) -> None:
        if not isinstance(source, TaskSource):
            raise TypeError(f'Object {type(source).__name__} is not a duck!')
        self._sources.append(source)

    def stream_tasks(self) -> Iterable[Task]:
        for source in self._sources:
            yield from source.get_tasks()

    def collect_tasks(self) -> Iterable[Task]:
        return list(self.stream_tasks())

