from typing import Iterable
from ..task import Task


class APITaskSource:
    def get_tasks(self) -> Iterable[Task]:
        #Нормальная задача
        yield Task(task_id="api001", description='API Task Low', payload={"data": 1}, priority=1, status="in_progress")

        #Нормальная задача с высоким приоритетом
        yield Task(task_id="api002",description='API Task Medium', payload={"data": 2}, priority=3)

        #Задача с ошибкой
        yield Task(task_id="api003",description='API Task High', payload={"data": 3}, priority=5, status="ready")