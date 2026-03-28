from dataclasses import dataclass
from typing import Any, Iterable, Protocol, runtime_checkable


class Task:
    def __init__(self, id: int, payload : Any, priority: int) -> None:
        self.id = id
        self.payload = payload
        self.priority = priority

@runtime_checkable
class TaskSource(Protocol):
    def get_tasks(self) -> Iterable[Task]:
        ...