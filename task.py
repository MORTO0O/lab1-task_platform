from dataclasses import dataclass
from typing import Any, Iterable, Protocol, runtime_checkable

@dataclass(frozen=True) #frozen=True - immutable
class Task:
    id: str
    payload: Any

@runtime_checkable
class TaskSource(Protocol):
    def get_tasks(self) -> Iterable[Task]:
        ...