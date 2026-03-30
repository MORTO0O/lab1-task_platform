from typing import Any, Iterable, Protocol, runtime_checkable
from .descriptors import PriorityDescriptor, AccessLogDescriptor
from .exceptions import InvalidStatusError
from datetime import datetime

class Task:
    priority = PriorityDescriptor(min_priority=1, max_priority=5)
    __slots__ = ('_id', 'description', 'payload', '_priority', '_status', 'created_at')
    access_log = AccessLogDescriptor(message="Чтение данных задачи")

    def __init__(self, task_id: int, description: str, payload : Any, priority: int, status: str = "in_porgress") -> None:
        self._id = task_id
        self.payload = payload
        self._priority = priority
        self._status = status
        self.description = description
        self.created_at = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
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

    @property
    def ready_to_run(self) -> bool:
        return self._status == "ready" and len(self.description) > 0



@runtime_checkable
class TaskSource(Protocol):
    def get_tasks(self) -> Iterable[Task]:
        ...