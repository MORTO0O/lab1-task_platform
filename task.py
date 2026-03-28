from typing import Any, Iterable, Protocol, runtime_checkable
from .descriptors import PriorityDescriptor, AccessLogDescriptor
from .exceptions import InvalidStatusError


class Task:
    priority = PriorityDescriptor(min_priority=1, max_priority=5)

    access_log = AccessLogDescriptor(message="Чтение данных задачи")
    def __init__(self, task_id: int, payload : Any, priority: int, status: str = "in_porgress") -> None:
        self._id = task_id
        self.payload = payload
        self.priority = priority
        self._status = status

    @property
    def id(self) -> int:
        return self._id

    @property
    def is_high_priority(self) -> int:
        return self.priority == 5

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, new_status: str) -> None:
        valid_statuses = ["in_porgress", "ready", "sent"]
        if new_status not in valid_statuses:
            raise InvalidStatusError(f"Статус '{new_status}' недопустим. Доступные: {valid_statuses}")
        self._status = new_status


@runtime_checkable
class TaskSource(Protocol):
    def get_tasks(self) -> Iterable[Task]:
        ...