import random
from typing import Iterable
from ..task import Task

class GeneratorTaskSource:
    def __init__(self, count: int = 10) -> None:
        self.count = count

    def get_tasks(self) -> Iterable[Task]:
        for i in range(self.count):
            yield Task(
                task_id=f"gen_{i:04d}", 
                payload={"type": "generated", "value": i * 10},
                priority=random.randint(1, 5),
                description = f"Auto-generated task number {i}"
            )