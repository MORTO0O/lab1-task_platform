from typing import Iterable
from ..task import Task


class APITaskSource:
    def get_tasks(self) -> Iterable[Task]:
        #Нормальная задача
        yield Task(task_id="api001", payload={"data": 1}, priority=1, status="in_progress")

        #Нормальная задача с высоким приоритетом
        yield Task(task_id="api002", payload={"data": 2}, priority=5, status="ready")

        #Задача с ошибкой
        yield Task(task_id="api003", payload={"data": 3}, priority=3)